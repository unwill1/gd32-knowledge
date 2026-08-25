# GD32F50x 应用笔记与勘误索引

> 覆盖 GD32F502、GD32F503 和 GD32F505。Markdown 用于检索与导航；涉及电气参数、寄存器、选项字节、时序和代码时，以同目录 PDF 原文为准。

| 类型 | 文档 | 版本 / 日期 | 主题 | 涉及模块 | Markdown | PDF |
|---|---|---|---|---|---|---|
| 应用笔记 | AN270 GD32F50x 软件开发指南 | Rev1.2 / 2026-05-11 | Boot、SRAM ECC、Flash 与时钟限制、TIMER 和 CMP 使用说明 | FMC、RCU、SRAM ECC、TIMER、CMP、PMU | [打开 Markdown](AN270_GD32F50x软件开发指南_Rev1.2/AN270_GD32F50x软件开发指南_Rev1.2.md) | [打开 PDF](<AN270_GD32F50x软件开发指南_Rev1.2/AN270 GD32F50x软件开发指南_Rev1.2.pdf>) |
| 应用笔记 | AN278 GD32F50x 系列硬件开发指南 | Rev1.0 / 2025-10-31 | 供电与复位、时钟、Boot、典型外设电路、PCB、焊接和封装 | PMU、RCU、GPIO、USART/UART、CAN、I2C、SPI、USB、ADC、DAC、调试接口 | —（仅 PDF） | [打开 PDF](AN278_GD32F50x系列硬件开发指南_Rev1.0/AN278_GD32F50x系列硬件开发指南_Rev1.0.pdf) |
| 勘误手册 | Device limitations of GD32F50x | Rev1.1 / 2025-11-05 | 已知限制、影响与规避方法 | I2C、CAN、Cortex-M33 Core | [打开 Markdown](<Device limitations of GD32F50x_Rev1.1/Device limitations of GD32F50x_Rev1.1.md>) | [打开 PDF](<Device limitations of GD32F50x_Rev1.1/Device limitations of GD32F50x_Rev1.1.pdf>) |

## 查询约定

- 查 Boot、SRAM ECC、Flash/FMC 时钟限制、TIMER 或 CMP 软件使用注意事项时，先读 AN270。
- 查供电、复位、晶振、典型外设硬件连接、PCB Layout 和封装时，查阅 AN278 PDF。
- 查“已知限制 / 勘误 / workaround”时，先读勘误手册，再结合用户手册和应用笔记。
- 该索引只适用于 `GD32F50x` 分组，不跨型号分组套用。

## 转换质量状态

- AN270：Markdown 正文和代码主体完整；已修复主要缺字、异常断行、标题层级及外链图片问题。
- AN278：当前仅提供 PDF，未提供 Markdown，不标记为已转换。
- 勘误手册：正文完整；已修复主要标题断行、CAN 汇总表与修订历史粘连、列表漏项。
- AN278 PDF 封面标注“2025 年 08 月”，版本历史将 Rev1.0 首发日期记为“2025 年 10 月 31 日”；索引日期按版本历史记录。
