from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


KB_ROOT = Path(r"E:\gd32-knowledge\GD32H77x_H78x")
SOURCE_MD = Path(r"E:\Edge下载\merged (7)_localized\merged (7).md")
SOURCE_IMAGES = SOURCE_MD.parent / "images"
SOURCE_PDF = Path(r"E:\Firmware_pack\H7\UM-GD32H78x_77x-User Manual-CN-Rev0.5.pdf")


CHAPTER_DIRS = {
    1: "1_系统及存储器架构",
    2: "2_硬件信号量（HWSEM）",
    3: "3_中断_事件控制器（EXTI）",
    4: "4_直接存储器访问控制器（DMA）",
    5: "5_主机直接存储器访问控制器（MDMA）",
    6: "6_DMA请求多路复用器（DMAMUX）",
    7: "7_非易失性存储器控制器（NVMC）",
    8: "8_RAM_ECC监视器单元（RAMECCMU）",
    9: "9_电源管理单元（PMU）",
    10: "10_复位和时钟单元（RCU）",
    11: "11_时钟校准控制器（CTC）",
    12: "12_时钟相位延迟模块（CPDM）",
    13: "13_通用和备用输入_输出接口（GPIO和AFIO）",
    14: "14_触发选择控制器（TRIGSEL）",
    15: "15_定时器（TIMER）",
    16: "16_实时时钟（RTC）",
    17: "17_看门狗定时器（WDGT）",
    18: "18_调试（DBG）",
    19: "19_循环冗余校验管理单元（CRC）",
    20: "20_真随机数生成器（TRNG）",
    21: "21_加密处理器（CAU）",
    22: "22_哈希处理器（HAU）",
    23: "23_公钥加密处理器（PKCAU）",
    24: "24_实时解密（RTDEC）",
    25: "25_模数转换器（ADC）",
    26: "26_数模转换器（DAC）",
    27: "27_比较器（CMP）",
    28: "28_VREF",
    29: "29_低功耗数字温度传感器（LPDTS）",
    30: "30_TFT-LCD接口（TLI）",
    31: "31_DSI主机控制器（DSI）",
    32: "32_快速傅里叶变换（FFT）",
    33: "33_高性能数字滤波器（HPDF）",
    34: "34_三角函数加速器（TMU）",
    35: "35_滤波算法加速器（FAC）",
    36: "36_图像处理加速器（IPA）",
    37: "37_编码器分频输出控制器（EDOUT）",
    38: "38_编码器接口模块（EDIM）",
    39: "39_旋变数字转换模块（RDCM）",
    40: "40_通用同步异步收发器（USART）",
    41: "41_串行外设接口_片上音频接口（SPI_I2S）",
    42: "42_内部集成电路总线接口（I2C）",
    43: "43_控制器局域网络（CAN）",
    44: "44_OSPI_I_O管理器（OSPIM）",
    45: "45_八线SPI接口（OSPI）",
    46: "46_SDIO接口（SDIO）",
    47: "47_管理数据输入_输出接口（MDIO）",
    48: "48_外部存储器控制器（EXMC）",
    49: "49_数字摄像头接口（DCI）",
    50: "50_通用并行从机接口（GPSI）",
    51: "51_S_P数字音频接口接收器（RSPDIF）",
    52: "52_串行音频接口（SAI）",
    53: "53_通用串行总线高速接口（USBHS）",
    54: "54_以太网（ENET）",
    55: "55_EtherCAT®从站控制(ESC)",
}


TIMER_TYPES = {
    1: "高级",
    2: "通用L0",
    3: "通用L3",
    4: "通用L4",
    5: "基本",
}

EDIM_TYPES = {
    1: "A-format",
    2: "T-format",
    3: "EnDat2.2",
    4: "BiSS-C",
    5: "HIPERFACE-DSL",
}


FOOTER = re.compile(
    r"(?:\d{1,4})?Preliminary\s*version\s*Confidential,\s*"
    r"under\s*NDA\s*for\s*engineering\s*evaluation\s*only",
    re.IGNORECASE,
)
IMAGE_REF = re.compile(r"!\[[^\]]*\]\((?:\./)?images/([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def find_unique(pattern: str, text: str, label: str) -> re.Match[str]:
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    if len(matches) != 1:
        raise RuntimeError(f"{label}: expected one boundary, found {len(matches)}")
    return matches[0]


def clean_text(text: str) -> str:
    text = FOOTER.sub("", text)
    text = re.sub(r"(?mi)^\s*Preliminary\s+version\s*$", "", text)
    text = text.replace("<td>null</td>", "<td>—</td>")
    text = text.replace(
        "时钟的三种时钟源： 、 和 时钟的 分频（通过配置 寄存器的RTCDIV位域）",
        "RTC时钟的三种时钟源：LXTAL、IRC32K和HXTAL时钟的2-63分频"
        "（通过配置RCU_CFG0寄存器的RTCDIV位域）",
    )
    text = re.sub(r"(?m)^#\s+(?!GigaDevice)(.+)$", r"### \1", text)

    def numbered_heading(match: re.Match[str]) -> str:
        number = match.group(1)
        title = match.group(2)
        depth = len([x for x in number.rstrip(".").split(".") if x])
        return f"{'#' * min(depth, 6)} {number} {title}"

    text = re.sub(r"(?m)^##\s+(\d+(?:\.\d+)*\.)\s*(.+)$", numbered_heading, text)
    text = re.sub(r"(?m)^##\s+(\d+[:：].*)$", r"\1", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def normalized_title(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    return "".join(char.lower() for char in text if char.isalnum())


def demote_false_chapter_headings(text: str, chapter_number: int) -> str:
    def replace(match: re.Match[str]) -> str:
        number = int(match.group(1))
        if number == chapter_number:
            return match.group(0)
        return f"### {match.group(1)}. {match.group(2)}"

    return re.sub(r"(?m)^# (\d+)\. (.*)$", replace, text)


def split_chapters(source: str) -> dict[int, str]:
    starts: dict[int, int] = {}
    for number in range(1, 56):
        expected = normalized_title(CHAPTER_DIRS[number].split("_", 1)[1])
        candidates = list(re.finditer(rf"^## {number}\. (.+)$", source, re.MULTILINE))
        matches = [m for m in candidates if normalized_title(m.group(1)) == expected]
        if len(matches) != 1:
            headings = [m.group(1) for m in candidates]
            raise RuntimeError(
                f"chapter {number}: exact title boundary count {len(matches)}; "
                f"candidates={headings[:10]}"
            )
        match = matches[0]
        starts[number] = match.start()
    chapters: dict[int, str] = {}
    for number in range(1, 56):
        if number < 55:
            end = starts[number + 1]
        else:
            appendix = re.search(r"^## 56\. .+$", source[starts[number] :], re.MULTILINE)
            end = starts[number] + appendix.start() if appendix else len(source)
        chapters[number] = demote_false_chapter_headings(
            clean_text(source[starts[number] : end]), number
        )
    return chapters


def split_at_register(chapter: str, number: int) -> tuple[str, str]:
    match = re.search(
        rf"(?m)^#{{2,6}}\s+{number}\.\d+(?:\.\d+)*\.?\s+.*(?:寄存器|寄存器定义).*$",
        chapter,
    )
    if not match:
        raise RuntimeError(f"chapter {number}: register boundary not found")
    return chapter[: match.start()].strip() + "\n", chapter[match.start() :].strip() + "\n"


def subsection_bounds(chapter: str, chapter_number: int, count: int) -> list[tuple[int, int]]:
    starts = []
    for index in range(1, count + 1):
        match = find_unique(
            rf"^##\s+{chapter_number}\.{index}\.\s+.+$",
            chapter,
            f"chapter {chapter_number}.{index}",
        )
        starts.append(match.start())
    return [
        (start, starts[i + 1] if i + 1 < len(starts) else len(chapter))
        for i, start in enumerate(starts)
    ]


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_chapter_files(output: Path, chapters: dict[int, str]) -> list[Path]:
    written: list[Path] = []
    for number, chapter in chapters.items():
        directory_name = CHAPTER_DIRS[number]
        chapter_dir = output / directory_name
        chapter_dir.mkdir(parents=True, exist_ok=True)

        if number == 15:
            bounds = subsection_bounds(chapter, 15, 5)
            overview = chapter[: bounds[0][0]].strip() + "\n"
            path = chapter_dir / "15_TIMER_概览与分类.md"
            write_markdown(path, overview)
            written.append(path)
            for index, (start, end) in enumerate(bounds, 1):
                feature, registers = split_at_register(chapter[start:end], 15)
                label = TIMER_TYPES[index]
                for suffix, content in (("特性及功能", feature), ("寄存器", registers)):
                    path = chapter_dir / f"15_TIMER_{label}_{suffix}.md"
                    write_markdown(path, content)
                    written.append(path)
        elif number == 17:
            bounds = subsection_bounds(chapter, 17, 2)
            prefix = chapter[: bounds[0][0]].strip()
            for index, (start, end) in enumerate(bounds, 1):
                feature, registers = split_at_register(chapter[start:end], 17)
                if index == 1 and prefix:
                    feature = prefix + "\n\n" + feature
                label = "独立看门狗" if index == 1 else "窗口看门狗"
                for suffix, content in (("特性及功能", feature), ("寄存器", registers)):
                    path = chapter_dir / f"17_WDGT_{label}_{suffix}.md"
                    write_markdown(path, content)
                    written.append(path)
        elif number == 38:
            bounds = subsection_bounds(chapter, 38, 5)
            overview = chapter[: bounds[0][0]].strip() + "\n"
            path = chapter_dir / "38_EDIM_概览与分类.md"
            write_markdown(path, overview)
            written.append(path)
            for index, (start, end) in enumerate(bounds, 1):
                feature, registers = split_at_register(chapter[start:end], 38)
                label = EDIM_TYPES[index]
                for suffix, content in (("特性及功能", feature), ("寄存器", registers)):
                    path = chapter_dir / f"38_EDIM_{label}_{suffix}.md"
                    write_markdown(path, content)
                    written.append(path)
        else:
            feature, registers = split_at_register(chapter, number)
            for suffix, content in (("特性及功能", feature), ("寄存器", registers)):
                path = chapter_dir / f"{directory_name}_{suffix}.md"
                write_markdown(path, content)
                written.append(path)
    return written


def copy_referenced_images(markdown_files: list[Path]) -> tuple[int, int]:
    copied = 0
    unique: set[str] = set()
    for markdown in markdown_files:
        refs = set(IMAGE_REF.findall(markdown.read_text(encoding="utf-8")))
        if not refs:
            continue
        image_dir = markdown.parent / "images"
        image_dir.mkdir(exist_ok=True)
        for name in refs:
            source = SOURCE_IMAGES / name
            if not source.is_file():
                raise FileNotFoundError(f"missing source image: {source}")
            target = image_dir / name
            if not target.exists():
                shutil.copy2(source, target)
                copied += 1
            unique.add(name)
    return copied, len(unique)


def validate(markdown_files: list[Path]) -> None:
    if len(markdown_files) != 130:
        raise RuntimeError(f"expected 130 markdown files, found {len(markdown_files)}")
    problems: list[str] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if "�" in text:
            problems.append(f"replacement character: {path}")
        if FOOTER.search(text):
            problems.append(f"unclean footer: {path}")
        if text.count("<table") != text.count("</table>"):
            problems.append(f"unbalanced table: {path}")
        if text.count("```") % 2:
            problems.append(f"unbalanced fence: {path}")
        for image in IMAGE_REF.findall(text):
            target = path.parent / "images" / image
            if not target.is_file() or target.stat().st_size == 0:
                problems.append(f"missing image: {target}")
    if problems:
        raise RuntimeError("\n".join(problems[:30]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    for required in (SOURCE_MD, SOURCE_IMAGES, SOURCE_PDF):
        if not required.exists():
            raise FileNotFoundError(required)

    source = SOURCE_MD.read_text(encoding="utf-8")
    chapters = split_chapters(source)
    if args.dry_run:
        for number, chapter in chapters.items():
            if number not in (15, 17, 38):
                split_at_register(chapter, number)
        subsection_bounds(chapters[15], 15, 5)
        subsection_bounds(chapters[17], 17, 2)
        subsection_bounds(chapters[38], 38, 5)
        print("dry-run OK: 55 chapters and all split boundaries found")
        return

    output = KB_ROOT / "peripherals"
    if output.resolve() != Path(r"E:\gd32-knowledge\GD32H77x_H78x\peripherals").resolve():
        raise RuntimeError(f"refusing to replace unexpected path: {output}")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    markdown_files = write_chapter_files(output, chapters)
    copied, unique = copy_referenced_images(markdown_files)
    validate(markdown_files)

    sources = KB_ROOT / "sources"
    sources.mkdir(exist_ok=True)
    pdf_target = sources / SOURCE_PDF.name
    if not pdf_target.exists() or pdf_target.stat().st_size != SOURCE_PDF.stat().st_size:
        shutil.copy2(SOURCE_PDF, pdf_target)
    print(
        f"generated {len(markdown_files)} markdown files; "
        f"copied {copied} chapter image files ({unique} unique source names)"
    )


if __name__ == "__main__":
    main()
