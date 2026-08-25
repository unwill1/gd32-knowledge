## 25. 段码 LCD 控制器（SLCD）

## 25.1. 简介

SLCD 驱动器通过自动产生 SEG 和 COM 交流电压信号来直接驱动 LCD 显示。该驱动器可以驱动单色液晶显示器（LCD），这是一种由若干段（像素或完整的符号）构成的，有可见和不可见两种状态的显示屏。SLCD 驱动器支持最大 32 个 SEG 和 8 个 COM。

## 25.2. 主要特征

◼ 可配置帧率；

◼ 单个SEG或所有SEG的闪烁；

◼ 支持静态、1/2、1/3、1/4、1/6和1/8占空比；

◼ 支持1/2、1/3和1/4偏置；

◼ 双路缓冲器可多达8x32位寄存器来存储SLCD_DATAx；

◼ 对比度也可通过配置死区时间来调整；

◼ 可配置电压输出驱动用于增强SLCD驱动能力（仅适用于GD32L233系列）

## 25.3. 功能描述

## 25.3.1. SLCD 架构

SLCD控制器框图如下所示：


图 25-1. SLCD 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/f37ead1bb634c2a0b3e270e20491c93f64b5d74b38232d2ac673876862439b13.jpg)


SLCD REG 是 SLCD 控制器的寄存器，包括 SLCD_CTL、SLCD_CFG、SLCD_STAT、SLCD_STATC 和 SLCD_DATAx 五个寄存器，它们可通过 APB 总线配置，且可使 CPU 产生中断。

时钟发生器可以从输入时钟产生 SLCD 时钟，SLCD 时钟可以驱动闪烁控制和 SEG/COM 驱动器。闪烁控制可以产生闪烁频率和闪烁像素，SEG/COM 驱动器可产生 SEG 和 COM 信号输送到 ANALOG 矩阵，且 ANALOG 矩阵可实现 SEG 和 COM 电压。

## 25.3.2. 时钟发生器

SLCD 输入时钟与 RTCCLK 共用，允许三种不同的时钟源：通过配置 RCU_BDCTL 寄存器的RTCSRC 位域，可以选择 LXTAL、IRC32K 或 HXTAL 的 32 分频。输入时钟频率变化范围为32KHz 到 1MHz。

SLCD控制器可使用从集成时钟分频器输出的SLCD时钟信号来产生SEG和COM线的时序。SLCD 时钟信号来自于 RCU 输入时钟。SLCD 时钟频率可在 SLCD_CFG 寄存器中的 PSC 位和 DIV位来选择，由此产生的时钟频率计算结果如下：

$$
f _ {S L C D} = \frac {f _ {\text { in\_clk }}}{2 ^ {P S C} \times (D I V + 1 6)}\tag{25-1}
$$

SLCD 时钟作为 SLCD 控制器的时钟基准。SLCD 的时钟频率相当于相频率。一个 SLCD 帧是一个奇数帧或一个偶数帧，它们拥有与有效的 COM 一样多的相。占空比定义为 1/（SLCD 屏显示需要的 COM 数）。因此帧频率计算结果如下：

$$
f _ {\text {frame}} = f _ {\text {SLCD}} \times \text {Duty}\tag{25-2}
$$

注意：Duty 的数值定义为：1/（SLCD 使用的 COM 口数量）。

在帧起始，SLCD_STAT 寄存器的 SOF 位由硬件置位，如果 SLCD_CFG 寄存器的 SOFIE 位被置位，SLCD 中断将被执行。向 SLCD_STATC 寄存器的 SOFC 位写 1 将清除 SOF 位。


图 25-2. 1/3 偏置，1/4 占空比


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/0d94bb762f004ae336e788a388c75ddfaedfdd075a75aaa888c195c0984149e8.jpg)


## 25.3.3. 闪烁控制

SLCD控制器也支持闪烁功能。闪烁模式可通过SLCD_CFG寄存器中的BLKMOD位来控制，BLKMOD = 01 表示允许在 SEG0 和 COM0 上闪烁单个段，BLKMOD = 10 表示允许闪烁所有COM 和 SEG0，BLKMOD = 11 表示允许闪烁所有 COM 和所有 SEG，BLKMOD = 00 表示禁

用闪烁。

闪烁频率源于 SLCD 时钟，可通过 SLCD_CFG 中 BLKDIV 位来选择，由此产生的 BLINK 频率计算结果如下：

$$
f _ {B L I N K} = \frac {f _ {S L C D}}{2 ^ {(B L K D I V + 3)}}\tag{25-3}
$$

在选择 BLKMOD = 01，10 或 11 中的一种闪烁模式后，使能的 SEG 或所有 SEG 都会在下一帧分界变成空白，且会停留半个 BLKCLK 周期，然后它们会在一个帧分界再次变白之前完成下一帧分界激活并继续停留另半个 BLKCLK 周期时间。

## 25.3.4. SEG/COM 驱动器

SEG/COM 驱动器可以产生 SEG 和 COM 信号。

偏置发生器：

偏置可通过 SLCD_CTL 寄存器中 BIAS 位来选择，仅在对应的一个帧周期的段内可以达到最大幅值 VSLCD 或 VSS。奇数帧电压和偶数帧电压如下表所示：


表25-1. 奇数帧电压


<table><tr><td>偏置</td><td>静态</td><td>1/2 偏置</td><td>1/3 偏置</td><td>1/4 偏置</td></tr><tr><td>COM 有效</td><td>VSLCD</td><td>VSLCD</td><td>VSLCD</td><td>VSLCD</td></tr><tr><td>COM 无效</td><td>/</td><td>1/2 VSLCD</td><td>1/3 VSLCD</td><td>1/4 VSLCD</td></tr><tr><td>SEG 有效</td><td>VSS</td><td>VSS</td><td>VSS</td><td>VSS</td></tr><tr><td>SEG 无效</td><td>VSLCD</td><td>VSLCD</td><td>2/3 VSLCD</td><td>1/2 VSLCD</td></tr></table>


表25-2. 偶数帧电压


<table><tr><td>偏置</td><td>静态</td><td>1/2 偏置</td><td>1/3 偏置</td><td>1/4 偏置</td></tr><tr><td>COM 有效</td><td>VSS</td><td>VSS</td><td>VSS</td><td>VSS</td></tr><tr><td>COM 无效</td><td>/</td><td>1/2 VSLCD</td><td>2/3 VSLCD</td><td>3/4 VSLCD</td></tr><tr><td>SEG 有效</td><td>VSLCD</td><td>VSLCD</td><td>VSLCD</td><td>VSLCD</td></tr><tr><td>SEG 无效</td><td>VSS</td><td>VSS</td><td>1/3 VSLCD</td><td>1/2 VSLCD</td></tr></table>

## COM信号：

COM 信号可通过 SLCD_CTL 寄存器中的 DUTY 位来选择。当 DUTY 是 000 时，静态占空比被选择，仅 COM[0]被使用，且仅一段在奇数帧或偶数帧内，COM[0]驱动器信号一直有效。当DUTY 是 001 时，仅 COM[1:0]和 2 段被使用。当 DUTY 是 010 时，仅 COM[2:0]和 3 段被使用。当 DUTY 是 011 时，仅 COM[3:0]和 4 段被使用。当 DUTY 是 100 时，COM[7:0]和 8 段被使用。当 DUTY 是 101 时，COM[5:0]和 6 段被使用。所有的 COM 信号驱动器如下表所示：


表25-3. 所有COM信号驱动器


<table><tr><td>段</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>COM0</td><td>有效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td></tr><tr><td>COM1</td><td>无效</td><td>有效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td></tr><tr><td>COM2</td><td>无效</td><td>无效</td><td>有效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td></tr><tr><td>COM3</td><td>无效</td><td>无效</td><td>无效</td><td>有效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td></tr><tr><td>COM4</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>有效</td><td>无效</td><td>无效</td><td>无效</td></tr><tr><td>COM5</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>有效</td><td>无效</td><td>无效</td></tr><tr><td>COM6</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>有效</td><td>无效</td></tr><tr><td>COM7</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>无效</td><td>有效</td></tr></table>

## SEG信号：

SEG 信号从 SLCD_DATAx 寄存器中读取。SLCD_DATAx 表示相 x 的 SEG 信号数据。当该位为 1 时，对应的 SEG 驱动有效信号，当该位为 0 时，对应的 SEG 驱动无效信号。

例如，应用程序需要激活像素 COM2-SEG2，COM3-SEG2 和 COM5-SEG4，则 SLCD_DATA2寄存器的 bit2、SLCD_DATA3 寄存器的 bit2、SLCD_DATA5 寄存器的 bit4 应被置位。这样SEG2 信号将在每个奇数帧与偶数帧的第三、四相变为有效，SEG4 信号将在每个奇数帧与偶数帧的第六相变为有效。有效与无效电压请参考 25-1. 和 25-2. 。25-3. 1/4 1/6 展现了当配置为 1/4 偏置，1/6 占空比时的 SEG 信号。


图 25-3. 1/4 偏置 1/6 占空比


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/21973772ab7baa7b4292c72a4598870d9eb9b63c369d51750ba38cfe9b55e86e.jpg)


## 死区时间：

死区时间通过 SLCD_CFG 寄存器中 DTD 位来配置，它在每个偶数帧后插入 VSS，插入的段数时间由 DTD 位定义。应用程序可以通过配置死区时间调节对比度。


图 25-4. SLCD 死区时间（1/3 偏置，1/4 占空比）


<table><tr><td></td><td>奇数帧</td><td>偶数帧</td><td>死区时间</td><td>奇数帧</td><td>偶数帧</td></tr><tr><td>COM</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SEG</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 25.3.5. 双缓冲存储

双缓冲存储用于确保显示信息的连续性。

应用程序通过修改 SLCD_DATAx 寄存器组访问第一缓冲区。在将显示信息写入 SLCD_DATAx寄存器组后，应用程序需要将 SLCD_STAT 寄存器的 UPRF 位置位，之后硬件将数据从第一缓冲区传入第二缓冲区，在传输的这段时间内，UPRF 位将保持置位，同时 SLCD_DATAx 寄存器组将写保护。当传输结束后，UPRF 位被清除同时 UPDF 位将被硬件置位，如果 UPDIE位被置位，将会产生一个中断。SEG 信号由第二缓冲区内的数据驱动，因此写 SLCD_DATAx寄存器组将不会对显示信息造成影响。

如果 UPRF 位在显示失能（SLCDON=0）时被置位，传输将不会发生，直到 SLCDON 置位。

## 25.3.6. 模拟矩阵

模拟矩阵提供 SLCD 电压。SLCD 电压电平可由 VSLCD 引脚或内部电压升压转换器产生（由SLCD_CTL 寄存器中 VSRC 位选择）。

GD32L233 系列中，当使用内部电压源时，VSLCD 的值可以通过配置 SLCD_CFG 寄存器的CONR[2:0]位域从 VSLCD0 到 VSLCD7 中选择（VSLCDx 的值请参考产品数据手册）。应用程序可以通过改变 VLCD 的值调节对比度。

GD32L235 系列中，当使用内部电压源时，VDD 电压作为内部电压源。

另外，用户也可用修改死区时间的方法调节对比度。

模拟矩阵通过如 25-5. GD32L233 SLCD 和 25-6. GD32L235SLCD 所示的内部电阻分压网络提供 VSS 和 VSLCD 中间的电压电平（1/3VSLCD、2/3 VSLCD 或 1/4 VSLCD、2/4 VSLCD 和 3/4 VSLCD）。


图 25-5. GD32L233 系列 SLCD 电阻分压网络


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/121f48f2e205b90594eecda08c9075352fff78ab232f76e72f3612a5a24b0615.jpg)



图 25-6. GD32L235 系列 SLCD 电阻分压网络


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/000e937c5698a874d4253b570cf8fce83af0bbce5936419412a22bcea506469a.jpg)



在转换期间，为了快速到达静态状态，低值电阻（R<sub>L</sub>）被使用以增加电流。之后低值电阻被关闭，高值电阻（R<sub>H</sub>）被使用以减小功耗。R<sub>L</sub> 被使用的时间长度依据 SLCD_CFG 寄存器的PULSE[2:0]位域的值。通过配置 SLCD_CFG 寄存器的 HDEN 位， $\mathsf { R } _ { \mathsf { L } }$ 可以一直被使用。


## 增强模式：

在 GD32L233 系列中，SLCD 模块集成了可配置的电压输出驱动器，可通过配置 SLCD_CTL寄存器的 VODEN 位进入增强模式。启用电压输出驱动器，可以减少由电桥上的 LCD 电容负载引起的电压干扰，从而获得稳定的电压，达到增强 SLCD 驱动能力的目的。

在增强模式下，高值电阻器桥（RHN）将产生一个中间电压，HDEN 位或 PULSE 位配置将被忽略，低值电阻器桥（RLN）将被自动禁用，从而降低了功耗。

VLCD 电源不用于电压输出驱动器。仅当未激活 SLCD 控制器时才能配置电压输出驱动器。

注意：GD32L235 系列不支持增强模式。

## 25.3.7. VSLCD 电压源

## V<sub>SLCD</sub> 电压监测

ADC_CTL1 寄存器中的 VSLCDEN 位用于使能 VSLCD 电压测量。由于 VSLCD 电压可能高于 VDDA，因此为了确保 ADC 的正常工作，内部 VSLCDrail1 模拟电压连接到 ADC_IN19 输入通道。

在不同 BIAS[1:0]偏置下，VSLCDrail1 的值是不同的，这是由内部模拟电路决定的。

1. $\mathsf { B l A S } \left[ 1 : 0 \right] = 0 0 , \mathsf { V } _ { \mathsf { S L C D r a i l } 1 } = 1 / 4 \mathsf { V } _ { \mathsf { S L C D } }$ ，可以使用 V<sub>SLCD</sub>电压监视功能，通过 ADC 转换获得的值是 V<sub>SLCD</sub>电压的四分之一。

2. BIAS [1:0] = 01，V<sub>SLCDrail1</sub> 是无效值，并且 VSLCD 电压监视功能无法正常使用。

3. $\mathsf { 3 l A S } \left[ 1 : 0 \right] = 1 0 , \mathsf { V _ { S L C D r a i l 1 } } = 1 / 3 \mathsf { V _ { S L C D } }$ ，可以使用 V<sub>SLCD</sub>电压监视功能，通过 ADC 转换获得的值是 V<sub>SLCD</sub>电压的三分之一。

为防止意外消耗电池电量，建议仅在执行 ADC 转换时才启用 VSLCDEN。

## V<sub>SLCD</sub>电压源配置

SLCD的电压源可通过SLCD_CTL寄存器的VSRC位配置为内部电压源或外部电压源。SLCD使用内/外电压源的注意事项如下：

## 内部电压源：

GD32L233 系列中，当 SLCD 选择内部电压源时，VSRC 位置 0，PD6 引脚需要配置为模拟模式，且在与 GND 之间需外接一个电容，其电容值请参考 Datasheet。当 SLCD 选取内部电压源，其配置流程需遵循以下方式。

1. 配置 PD6 引脚为模拟模式。

2. 配置 SLCD 寄存器，并选择内部电压源。

3. 等待外接电容完成充电（典型情况，当外接电容为 2uF 时，充电时间约为 1.5ms）。

4. 使能 SLCD 模块。

GD32L235 系列中，当 SLCD 选择内部电压源时，使用 VDD 作为内部电压源。

## 外部电压源：

当 SLCD 选择外部电压源时，VSRC 位置 1，PD6 引脚需要配置为模拟模式，并连接外部供电电压源。其配置流程需遵循以下方式。

1. 配置 PD6 引脚为模拟模式。

2. 配置 SLCD 寄存器，并选择外部电压源。

3. 使能 SLCD 模块。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>VODEN</td><td>电压输出驱动使能0:电压输出驱动禁止1:电压输出驱动使能当VODEN=1时,可以提高SLCD的电压驱动能力。</td></tr><tr><td>7</td><td>COMS</td><td>COM/SEG引脚选择该位用于COM/SEG引脚的选择。当占空比选择1/8或1/6时,SLCD_COM[7:4]总是作为SLCD_COM[7:4]功能,无论该位有无被置位。0:SLCD_COM[7:4]引脚选择SLCD_COM[7:4]1:SLCD_COM[7:4]引脚选择SLCD_SEG[31:28]</td></tr><tr><td>6:5</td><td>BIAS[1:0]</td><td>偏置选择偏置为驱动SLCD时的电压水平参数。它被定义为1/(驱动SLCD显示屏能够使用的电压水平总数-1)。00:1/4偏置(5个电压水平:VSS,1/4VSLCD,1/2VSLCD,3/4VSLCD,VSLCD)01:1/2偏置(3个电压水平:VSS,1/2VSLCD,VSLCD)10:1/3偏置(4个电压水平:VSS,1/3VSLCD,2/3VSLCD,VSLCD)11:保留</td></tr><tr><td>4:2</td><td>DUTY[2:0]</td><td>占空比选择这些位决定占空比。占空比定义为1/(SLCD显示屏需要的COM数)000:静态占空比001:1/2占空比010:1/3占空比</td></tr></table>
