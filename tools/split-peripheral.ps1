<#
.SYNOPSIS
    将单个外设 Markdown 文件按"特性及功能 + 寄存器"拆分为多个子文件。

.DESCRIPTION
    适用于 GD32 知识库中由 PDF 转换而来的大 MD 文件。
    自动识别子模块边界和寄存器章节起点，按子模块拆分。

.PARAMETER FilePath
    要拆分的 MD 文件完整路径。

.PARAMETER Prefix
    输出文件名前缀（如 "24_TIMER"、"22_WDGT"）。不指定则自动从章节号和缩写推断。

.PARAMETER RegisterPattern
    用于识别"寄存器章节"开头的正则表达式。
    默认: '^\d+\.\d+\.\d+\.\s*.+寄存器'

.PARAMETER SubModulePattern
    用于识别"子模块大标题"的正则表达式（如 "24.1. 高级定时器"）。
    默认: '^\d+\.\d+\.\s'

.PARAMETER DryRun
    仅分析结构，不实际写文件。

.EXAMPLE
    .\split-peripheral.ps1 -FilePath "E:\gd32-knowledge\GD32H737_757_759\peripherals\24_定时器（TIMER）\24_定时器（TIMER）.md"

.EXAMPLE
    # 自定义子模块名
    .\split-peripheral.ps1 -FilePath "path\to\file.md" -Prefix "24_TIMER" -DryRun
#>

param(
    [Parameter(Mandatory)]
    [string]$FilePath,

    [string]$Prefix,

    [string]$RegisterPattern = '^\d+\.\d+\.\d+\.\s*.+寄存器',

    [string]$SubModulePattern = '^\d+\.\d+\.\s',

    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# --- 读取文件 ---
if (-not (Test-Path $FilePath)) { throw "文件不存在: $FilePath" }
$content = [System.IO.File]::ReadAllText($FilePath)
$dir = Split-Path $FilePath
$enc = [System.Text.UTF8Encoding]::new($false)

Write-Host "文件大小: $([math]::Round($content.Length/1024,1)) KB" -ForegroundColor Cyan

# --- 扫描所有 H1/H2 标题及其偏移 ---
$headings = [regex]::Matches($content, '(?m)^#{1,2}\s+(.+)$')
Write-Host "找到 $($headings.Count) 个标题（H1/H2）" -ForegroundColor Cyan

# --- 识别子模块边界 ---
# 子模块 = 匹配 SubModulePattern 的标题（如 "24.1. 高级定时器..."）
$subModules = @()
foreach ($h in $headings) {
    $title = $h.Groups[1].Value
    if ($title -match $SubModulePattern) {
        $subModules += [PSCustomObject]@{
            Title  = $title
            Offset = $h.Index
        }
    }
}

if ($subModules.Count -eq 0) {
    throw "未找到子模块标题（模式: $SubModulePattern）。请检查文件结构或调整 -SubModulePattern。"
}

Write-Host "`n找到 $($subModules.Count) 个子模块:" -ForegroundColor Green
$subModules | ForEach-Object { Write-Host "  [$($_.Offset)] $($_.Title)" }

# --- 在每个子模块内找寄存器章节分割点 ---
$splits = @()
for ($i = 0; $i -lt $subModules.Count; $i++) {
    $startOff = $subModules[$i].Offset
    $endOff = if ($i -lt $subModules.Count - 1) { $subModules[$i + 1].Offset } else { $content.Length }

    # 在该子模块范围内找"寄存器"标题
    $regHeading = $null
    foreach ($h in $headings) {
        if ($h.Index -gt $startOff -and $h.Index -lt $endOff) {
            if ($h.Groups[1].Value -match $RegisterPattern) {
                $regHeading = $h
                break
            }
        }
    }

    $splits += [PSCustomObject]@{
        Title       = $subModules[$i].Title
        FeatStart   = $startOff
        RegStart    = if ($regHeading) { $regHeading.Index } else { $null }
        End         = $endOff
        HasRegSplit = ($null -ne $regHeading)
    }
}

# --- 推断前缀 ---
if (-not $Prefix) {
    $firstTitle = $headings[0].Groups[1].Value
    if ($firstTitle -match '^(\d+)\.\s*.+（(\w+)）') {
        $Prefix = "$($Matches[1])_$($Matches[2])"
    } else {
        $Prefix = "split"
    }
    Write-Host "`n自动推断前缀: $Prefix" -ForegroundColor Yellow
}

# --- 推断子模块短名 ---
function Get-ShortName($title) {
    # 尝试提取中文名关键字+级别标记
    # 例: "24.1. 高级定时器（TIMERx, x=0, 7）" -> "高级"
    # 例: "24.2. 通用定时器 L0（TIMERx...）" -> "通用L0"
    # 例: "22.1. 独立看门狗定时器（FWDGT）" -> "独立看门狗"
    # 例: "24.6. 基本定时器..." -> "基本"
    if ($title -match '^\d+\.\d+\.\s*(.+?定时器)\s*(L\d+)?') {
        $base = $Matches[1].Trim()
        $level = if ($Matches[2]) { $Matches[2] } else { '' }
        # "高级定时器" -> "高级", "独立看门狗定时器" -> "独立看门狗"
        $base = $base -replace '定时器$', ''
        return "${base}${level}"
    }
    if ($title -match '^\d+\.\d+\.\s*(.+)$') {
        $name = $Matches[1].Trim()
        # 截断到合理长度
        if ($name.Length -gt 10) { $name = $name.Substring(0, 10) }
        return $name
    }
    return "unknown"
}

# --- 生成概览文件（子模块之前的内容） ---
$preambleEnd = $subModules[0].Offset
$results = @()

if ($preambleEnd -gt 100) {
    $preambleContent = $content.Substring(0, $preambleEnd)
    $preambleFile = "${Prefix}_概览与分类.md"
    $results += [PSCustomObject]@{ File = $preambleFile; Size = $preambleContent.Length; Content = $preambleContent }
}

# --- 生成子模块文件 ---
foreach ($s in $splits) {
    $shortName = Get-ShortName $s.Title

    if ($s.HasRegSplit) {
        # 拆为：特性及功能 + 寄存器
        $featContent = $content.Substring($s.FeatStart, $s.RegStart - $s.FeatStart)
        $regContent = $content.Substring($s.RegStart, $s.End - $s.RegStart)

        $featFile = "${Prefix}_${shortName}_特性及功能.md"
        $regFile = "${Prefix}_${shortName}_寄存器.md"

        $results += [PSCustomObject]@{ File = $featFile; Size = $featContent.Length; Content = $featContent }
        $results += [PSCustomObject]@{ File = $regFile; Size = $regContent.Length; Content = $regContent }
    } else {
        # 无寄存器章节，整体作为一个文件
        $wholeContent = $content.Substring($s.FeatStart, $s.End - $s.FeatStart)
        $wholeFile = "${Prefix}_${shortName}.md"
        $results += [PSCustomObject]@{ File = $wholeFile; Size = $wholeContent.Length; Content = $wholeContent }
    }
}

# --- 输出计划 ---
Write-Host "`n拆分计划 ($($results.Count) 个文件):" -ForegroundColor Green
Write-Host ("-" * 60)
foreach ($r in $results) {
    $sizeKB = [math]::Round($r.Size / 1024, 1)
    Write-Host "  $($sizeKB) KB`t$($r.File)"
}
Write-Host ("-" * 60)

# --- 验证图片引用 ---
$imgDir = Join-Path $dir "images"
if (Test-Path $imgDir) {
    $imgs = (Get-ChildItem $imgDir -File).Name
    $totalRefs = 0; $missingRefs = 0
    foreach ($r in $results) {
        $refs = [regex]::Matches($r.Content, 'images/([a-f0-9]+\.jpg)')
        foreach ($ref in $refs) {
            $totalRefs++
            if ($ref.Groups[1].Value -notin $imgs) {
                $missingRefs++
                Write-Host "  [MISS] $($r.File) -> $($ref.Groups[1].Value)" -ForegroundColor Red
            }
        }
    }
    Write-Host "`n图片引用验证: 共 $totalRefs 处, 缺失 $missingRefs 处" -ForegroundColor $(if($missingRefs -eq 0){'Green'}else{'Red'})
}

# --- 写入文件 ---
if ($DryRun) {
    Write-Host "`n[DryRun] 未写入文件。去掉 -DryRun 参数实际执行。" -ForegroundColor Yellow
} else {
    foreach ($r in $results) {
        $outPath = Join-Path $dir $r.File
        [System.IO.File]::WriteAllText($outPath, $r.Content, $enc)
    }
    Write-Host "`n已写入 $($results.Count) 个文件到: $dir" -ForegroundColor Green
    Write-Host "原文件未删除，确认无误后可手动删除: $FilePath" -ForegroundColor Yellow
}
