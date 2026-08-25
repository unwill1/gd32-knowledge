@echo off
chcp 65001 >nul
setlocal

REM ============================================================
REM  外设MD文件拆分工具
REM  用法:
REM    split-peripheral.bat "文件路径.md"
REM    split-peripheral.bat "文件路径.md" --dry-run
REM    split-peripheral.bat "文件路径.md" --prefix 24_TIMER
REM ============================================================

if "%~1"=="" (
    echo 用法: split-peripheral.bat "外设MD文件路径" [--dry-run] [--prefix 前缀]
    echo.
    echo 示例:
    echo   split-peripheral.bat "E:\gd32-knowledge\...\24_定时器（TIMER）.md"
    echo   split-peripheral.bat "E:\gd32-knowledge\...\22_看门狗定时器（WDGT）.md" --dry-run
    exit /b 1
)

set "FILE=%~1"
set "DRYRUN="
set "PREFIX="

:parseArgs
shift
if "%~0"=="" goto :run
if /i "%~0"=="--dry-run" ( set "DRYRUN=-DryRun" & goto :parseArgs )
if /i "%~0"=="--prefix" ( shift & set "PREFIX=-Prefix '%~0'" & goto :parseArgs )
goto :parseArgs

:run
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0split-peripheral.ps1" -FilePath "%FILE%" %DRYRUN% %PREFIX%

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [错误] 拆分失败，请检查输出信息。
    pause
    exit /b 1
)

echo.
echo 完成。
pause
