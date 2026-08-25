## 23. SPI/QPI（SQPI）

## 23.1. 简介

SQPI 接口是一个用于串行、双线、四线接口存储设备的控制器。例如，控制 SQPI-PSRAM 和SQPI- FLASH。

利用 SQPI 接口可以像使用 SRAM 一样使用 SQPI 接口的存储器。

GD32EPRTxxA 系列芯片内部叠封了 PSRAM，连接 PSRAM 的 SQPI 引脚不能用于其他用途。

## 23.2. 主要特性

 两组独立的寄存器用于读操作和写操作；

 支持ID长度配置；

 读操作时SQPI时钟的采样边沿可配置；

 支持命令阶段、地址阶段、和等待周期阶段的长度配置；

 支持时钟输出由AHB时钟分频；

 支持无地址阶段和数据阶段的特殊指令；

 一个AHB读ID指令可以获取大于32位的ID数据；

 支持AHB突发操作和8、16、32位的AHB指令；

 支持256MB的外部存储空间，逻辑地址范围：0xB000 0000 - 0xBFFF FFFF；

 支持六种模式，这些模式是不同的命令阶段，地址阶段，等待阶段，和数据阶段的组合。

## 23.3. 功能描述

## 23.3.1. SQPI 模式定义

模式定义的命名，第一个字符表示命令阶段的有效 IO 个数，第二个字符表示地址阶段的有效IO 个数，第三个字符表示数据阶段的有效 IO 个数。对于每个字符，S 表示 1 个 IO 口，D 表示 2 个 IO 口，Q 表示 4 个 IO 口。


表 23-1. SQPI 控制器模式定义


<table><tr><td rowspan="2">引脚</td><td rowspan="2">方向</td><td colspan="6">操作模式</td></tr><tr><td>SSS</td><td>SSQ</td><td>SQQ</td><td>QQQ</td><td>SSD</td><td>SDD</td></tr><tr><td>SQPI_CLK</td><td>输出</td><td colspan="6">串行时钟</td></tr><tr><td>SQPI_CSN</td><td>输出</td><td colspan="6">片选(低电平有效)</td></tr><tr><td colspan="8">命令阶段</td></tr><tr><td>SQPI_D0</td><td>输出</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td>SQPI_D1</td><td>输出</td><td>X</td><td>X</td><td>X</td><td>O</td><td>X</td><td>X</td></tr><tr><td>SQPI_D2</td><td>输出</td><td>0</td><td>0</td><td>0</td><td>O</td><td>0</td><td>0</td></tr><tr><td>SQPI_D3</td><td>输出</td><td>1</td><td>1</td><td>1</td><td>O</td><td>1</td><td>1</td></tr><tr><td colspan="8">地址阶段</td></tr><tr><td>SQPI_D0</td><td>输出</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td>SQPI_D1</td><td>输出</td><td>X</td><td>X</td><td>O</td><td>O</td><td>X</td><td>O</td></tr><tr><td>SQPI_D2</td><td>输出</td><td>0</td><td>0</td><td>O</td><td>O</td><td>0</td><td>0</td></tr><tr><td>SQPI_D3</td><td>输出</td><td>1</td><td>1</td><td>O</td><td>O</td><td>1</td><td>1</td></tr><tr><td colspan="8">等待周期阶段</td></tr><tr><td>SQPI_D0</td><td>输入输出</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>SQPI_D1</td><td>输入输出</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>SQPI_D2</td><td>输入输出</td><td>0</td><td>X</td><td>X</td><td>X</td><td>0</td><td>0</td></tr><tr><td>SQPI_D3</td><td>输入输出</td><td>1</td><td>X</td><td>X</td><td>X</td><td>1</td><td>1</td></tr><tr><td colspan="8">数据阶段</td></tr><tr><td>SQPI_D0</td><td>输入输出</td><td>O</td><td>IO</td><td>IO</td><td>IO</td><td>IO</td><td>IO</td></tr><tr><td>SQPI_D1</td><td>输入输出</td><td>I</td><td>IO</td><td>IO</td><td>IO</td><td>IO</td><td>IO</td></tr><tr><td>SQPI_D2</td><td>输入输出</td><td>X</td><td>IO</td><td>IO</td><td>IO</td><td>X</td><td>X</td></tr><tr><td>SQPI_D3</td><td>输入输出</td><td>X</td><td>IO</td><td>IO</td><td>IO</td><td>X</td><td>X</td></tr></table>

Note: O – 输出, I –输入, IO – 输入输出, 0 –输出 0, 1 – 输出 1, X – 高阻态

## 23.3.2. SQPI控制器采样极性

SQPI 控制器的在读操作时采用极性（SQPI_PL）选择功能支持用户改变控制器的采样时间。这个功能在 SQPI 时钟高的时候非常有用。示例如下：


图 23-1. SQPI 采样极性


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/c52c80846fb5bdd769aa437fa3c03ce0b606c4904ca4e2f30581438621051f7d.jpg)


## 23.3.3. SQPI控制器特殊指令

SQPI 控制器特殊命令功能可以只发送命令，而没有地址阶段，等待周期阶段和数据阶段。特殊指令功能由硬件强制使用 SSS 模式。如果设置 SQPI_SCMD 位为 1，需要在其他存储访问操作之前读取该位并等待被清 0，这样可以确保该操作被执行完成。


图 23-2. SQPI_SCMD 示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/733e070ef5dfe621c87587e1438bf93413da7d42707a5bd36aac70a2a3eea186.jpg)


## 23.3.4. SQPI 读 ID 命令

对于超过 32 位的 ID 数据，SQPI_RDID 功能也可以提供支持。使用该功能，首先需要设置SQPI_IDLEN 位为 0x00(默认的 64 位)，然后设置 SQPI_RDID 为 1 并轮询该位直到被硬件清0，最后读取 SQPI_IDL 和 SQPI_IDH 寄存器。该命令的执行被硬件强制使用 SSS模式。


图 23-3. SQPI_RDID 示例(SQPI_IDLEN=00)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/3c1c89db42978de3d0205d6b2f34db73b592e708660b87124f8dc6130d3243ff.jpg)


## 23.3.5. SQPI控制器输出时钟配置

SQPI 时钟周期由 SQPI_CLKDIV 位配置，SQPI 的时钟频率公式如下：

$$
\begin{array}{r l} \square_ {\square \square \square \square \_ \square \square \square} & = \frac {\square \quad \square \square \square}{\square \square \square \square \_ \square \square \square \square \square + 1} \end{array}\tag{23-1}
$$

注意: SQPI_CLKDIV 不能为 0。当 SPI_CLKDIV 位域为偶数时，时钟输出的高电平时间要比低电平时间多一个 AHB 时钟周期。为了支持一些旧版本的 PSRAM,在 SQPI_CSN 引脚上升沿之后，在 SQPI_CLK引脚上会有一个时钟周期的 AHB时钟。


图 23-4. SQPI_CLK 示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/fb7d20c90d6d93dc1e8d3f0e35b551b25707598298c0ef52321e041908da96c7.jpg)


## 23.3.6. SQPI控制器初始化

在开始配置时，用户可以编程初始化寄存器 SQPI_INIT。数据采样边沿可以通过 SQPI_PL 位配置，设备的 ID 长度可以通过 SQPI_IDLEN 位域配置，地址位数可以通过 SQPI_ADDRBIT位域配置，命令位数可以通过 SQPI_CMDBIT 位域配置，时钟频率通过 SQPI_CLKDIV 位域配置。

## 23.3.7. 读 ID命令流程

首先，用户需要通过 SQPI_RCMD 位域配置读 ID 命令。（例如 SQPIPSRAM 的读 ID 命令为0x9F）并且在 SQPI_RCMD 寄存器中配置等待周期数。然后，设置 SQPI_RID 位为 1 并等待被清 0。最后，可以通过 SQPI_IDL 和 SQPI_IDH 寄存器获取 ID 值。

## 23.3.8. 读写操作流程

提供六种模式进行存储访问，需要在读写操作之前配置访问模式。读写操作的模式通过SQPI_RMODE 和 SQPI_WMODE 位域进行配置。等待周期由 SQPI_RWAITCYCLE andSQPI_WWAITCYCLE 位域进行配置。通过 SQPI_RCMD 和 SQPI_WCMD 位域配置存储器规定的操作命令，读写操作的设置分别位于 SQPI_RCMD 和 SQPI_WCMD 寄存器

在存储设备的访问配置完成后，用户可以通过 SQPI 的逻辑地址像访问 SRAM 一样直接访问外部存储设备。

## 23.3.9. SQPI控制器模式时序

QSPI 的读/写操作时序如下图，每次通过 AHB 读或者写访问 SQPI 逻辑地址时会发送下列时序。


图 23-5. SQPI SSS 模式时序(SPI)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/e48ee1967b681fbd3fa3d799c404e8bdb09d6d647f683ac45d4e41f23c7200f5.jpg)



图 23-6. SQPI SSQ 模式时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/e324a0ffaf1d247c1e9e34a3f065055b1435d0d7840c721ee128b78556215dc9.jpg)



图 23-7. SQPI SQQ 模式时序(SQPI)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/cd5339be0f312e358f183caf88ffef16619c04b1de2bfcc8b70b0d0120aeab2d.jpg)



图 23-8. SQPI QQQ 模式时序(QPI)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/88a1b0ae6c9f3bb0793787f7d31e8cb89a75875f71678194503f44e475bb14b7.jpg)



图 23-9. SQPI SSD 模式时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/91228d977ba394f63895182aadebbfc3aab3bc331857ecfcfdef0f68c7aa5d53.jpg)



图 23-10. SQPI SDD 模式时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/e8706ad13488043b292cbc40b29525359fe4373acd59377048d2370723fd21db.jpg)

