# GD32H737/757/759 应用笔记与勘误索引

> 覆盖 GD32H737xx、GD32H757xx 和 GD32H759xx。Markdown 用于检索与导航；涉及电气参数、寄存器、EFUSE、时序和代码时，以同目录 PDF 原文为准。

| 类型 | 文档 | 版本 / 日期 | 主题 | 涉及模块 | Markdown | PDF |
|---|---|---|---|---|---|---|
| 应用笔记 | AN109 GD32H73x_75x 系列硬件开发指南 | Rev1.6 / 2026-03-06 | 硬件设计、电源与复位、时钟、Boot、PCB 与封装 | PMU、RCU、GPIO、ADC、USBHS、OSPI、调试接口 | [打开 Markdown](AN109_GD32H73x_75x系列硬件开发指南_Rev1.6/AN109_GD32H73x_75x系列硬件开发指南_Rev1.6.md) | [打开 PDF](<AN109_GD32H73x_75x系列硬件开发指南_Rev1.6/AN109 GD32H73x_75x系列硬件开发指南_Rev1.6.pdf>) |
| 应用笔记 | AN111 GD32H73x_75x 软件开发指南 | Rev1.1 / 2026-02-11 | Boot/EFUSE、PMU、时钟、Cache/DMA、外设软件使用 | RCU、ADC、Secure JTAG、CAN、EXMC、SAI、ENET、USBHS、SDIO、MDMA、IDMA | [打开 Markdown](AN111_GD32H73x_75x_软件开发指南_Rev1.1/AN111_GD32H73x_75x_软件开发指南_Rev1.1.md) | [打开 PDF](<AN111_GD32H73x_75x_软件开发指南_Rev1.1/AN111 GD32H73x_75x 软件开发指南_Rev1.1.pdf>) |
| 勘误手册 | Device limitations of GD32H73x_H75x | Rev1.7 / 2025-11-15 | 已知限制、影响与规避方法 | SYSTEM、FMC、PMU、GPIO、TRNG、DBG、ADC、RTC、TIMER、USART、I2S、OSPI、EXMC、LPDTS、CAN、USBHS、Core | [打开 Markdown](<Device limitations of GD32H73x_H75x_Rev1.7/Device limitations of GD32H73x_H75x_Rev1.7.md>) | [打开 PDF](<Device limitations of GD32H73x_H75x_Rev1.7/Device limitations of GD32H73x_H75x_Rev1.7.pdf>) |

## 查询约定

- 查硬件设计、供电、复位、时钟、PCB 和封装时，先读 AN109。
- 查软件配置、EFUSE、Cache/DMA 一致性或外设使用注意事项时，先读 AN111。
- 查“已知限制 / 勘误 / workaround”时，先读勘误手册，再结合用户手册和应用笔记。
- 该索引只适用于 `GD32H737_757_759` 分组，不跨型号分组套用。

## 转换质量状态

- AN109：已对照 PDF 修复主要电源符号、上下标、ADC 参考电压条件和 LVD/POR/BOR 段落的转换错误。
- AN111：已对照 PDF 修复主要代码块、ARMv7-M 地址表和 SD 卡总线配置表的转换错误。
- 勘误手册：正文内容完整，已修复主要标题断行、列表误识别和重复伪表格。
