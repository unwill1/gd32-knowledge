## 14. 模数转换器（ADC）

## 14.1. 简介

MCU片上集成了12位逐次逼近式模数转换器模块（ADC），可以采样来自于16个外部通道和4个内部通道上的模拟信号。这20个ADC采样通道都支持多种运行模式，采样转换后，转换结果可以按照最低有效位对齐或最高有效位对齐的方式保存在相应的数据寄存器中。片上的硬件过采样机制可以通过减少来自MCU的相关计算负担来提高性能。

## 14.2. 主要特征

◼ 高性能：

ADC 采样分辨率：12 位、10 位、8 位和 6 位分辨率；

前置校准功能；

可编程的采样时间；

数据存储模式：最高有效位对齐和最低有效位对齐；

DMA 请求。

◼ 双时钟域架构（APB时钟和 ADC 时钟）。

◼ 模拟输入通道：

16 个外部模拟输入通道；

1 个内部温度传感通道（V<sub>SENSE</sub>）；

- 1 个内部参考电压输入通道（V<sub>REFINT</sub>）；

- 1 个监测外部 V<sub>BAT</sub>引脚的内部输入通道（V<sub>BAT</sub>）；

1 个监测 SLCD 电压的内部输入通道（V<sub>SLCD</sub>）。

◼ 转换开始的发起：

软件触发；

硬件触发。

◼ 运行模式：

- 转换单个通道，或者扫描一序列通道；

单次运行模式，每次触发转换一次选择的输入通道；

连续运行模式，连续转换所选择的输入通道；

间断运行模式。

◼ 中断的产生：

常规序列转换结束；

模拟看门狗事件。

◼ 模转换结果阈值监测器功能：模拟看门狗。

◼ 模块供电要求：1.8V到 3.6V，一般电源电压为 3.3V。

◼ 过采样：

16 位的数据寄存器；

可调整的过采样率，范围从 2x 到 256x；

- 高达 8 位的可编程数据移位。

◼ 通道输入范围：V<sub>SSA</sub> /V<sub>SS</sub> ≤V<sub>IN</sub> ≤V<sub>DDA</sub>/V<sub>DD</sub>。

## 14.3. 引脚和内部信号

14-1. ADC 给出了 ADC 模块框图。 14-1. ADC 和 14-2. ADC给出了 ADC 内部信号和引脚定义。


表 14-1. ADC 内部输入信号


<table><tr><td>内部信号名称</td><td>说明</td></tr><tr><td><eq>V_{SENSE}</eq></td><td>内部温度传感器电压输出</td></tr><tr><td><eq>V_{REFINT}</eq></td><td>内部参考电压输出</td></tr><tr><td><eq>V_{BAT}</eq></td><td><eq>V_{BAT}</eq>引脚上电压除以3</td></tr><tr><td><eq>V_{SLCD}</eq></td><td><eq>V_{SLCD}</eq>引脚上电压除以3</td></tr></table>


表 14-2. ADC 输入引脚定义


<table><tr><td>名称</td><td>注释</td></tr><tr><td><eq>V_{DDA} /V_{DD}</eq></td><td>模拟电源输入等于<eq>V_{DD}</eq>,<eq>1.8\ V \leq V_{DDA} \leq 3.6\ V</eq></td></tr><tr><td><eq>V_{SSA} /V_{SS}</eq></td><td>模拟地,等于<eq>V_{SS}</eq></td></tr><tr><td>ADCx_IN [15:0]</td><td>多达16路外部通道</td></tr></table>

## 14.4. 功能说明


图 14-1. ADC 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/3365b8fea5cd9906da11be1b83e3aaf102fb1e3599d5ed0ab9b76d4278cc1aac.jpg)



（1） 该触发源仅适用于GD32L235xx系列产品，在GD32L233xx系列产品中，对应取值保留。


## 14.4.1. 前置校准功能

在前置校准期间，ADC计算一个校准因子，这个因子应用于ADC的内部，它直到ADC下次掉电才无效。在校准期间，应用程序不能使用ADC，必须等到校准完成。在开始A/D转换前应执行校准操作。通过软件设置CLB=1启动校准。在校准期间CLB位会一直保持1。一旦校准完成，该位由硬件清0。

当ADC运行条件改变（例如供电电压V 、温度等）时，建议重新执行一次校准操作。

内部的模拟校准可以通过设置ADC_CTL1寄存器的RSTCLB位来重置。

软件校准过程：

1. 确保 ADCON=1；

2. 延迟 14 个 CK_ADC 以等待 ADC 稳定；

3. 设置 RSTCLB（该步骤是可选的）；

4. 设置 CLB=1；

5. 等待直到 CLB =0。

## 14.4.2. 双时钟域架构

除了APB接口时钟，ADC的子模块时钟还可以由ADC时钟提供。ADC时钟和APB时钟异步，并独立于APB时钟。

应用程序能够在低功耗运行时，降低PLCK时钟频率，同时ADC仍能保持最佳运行状态。

想要更多ADC时钟产生的信息，可以参考RCU章节的 $4 . 2 . 1$ 部分。

## 14.4.3. ADCON 使能

ADC_CTL1寄存器中的ADCON位是ADC模块的使能开关。如果该位为0，则ADC模块保持复位状态。为了省电，当ADCON位为0时，ADC模拟子模块将会进入掉电模式。ADC使能后需等待t<sub>ST(ADC)</sub>时间后才能采样，t<sub>ST(ADC)</sub>数值详见芯片数据手册。

注意: 当ADC使用内部基准VREF（VREFEN=1，HIPM=0）时，在使能ADC之前，请确保VREF_CS寄存器中的VREFRDY位置1。

## 14.4.4. 单端和差分输入通道

在GD32L23xx系列产品中，该功能仅适用于GD32L235xx系列产品。通过配置ADC_DIFCTL寄存器中的DIFCTL[14:0]位域，可以配置ADC通道为单端输入模式或差分输入模式。只有在ADC禁能（ADCON = 0）的情况下才能进行该配置。

单端输入模式下，通道n要转换的模拟电压是外部电压V （正输入）和V （负输入）之间的差。差分输入模式下，通道n要转换的模拟电压是外部电压 $\mathsf { V } _ { \mathsf { I N n } }$ （正输入）和 $V _ { \mathsf { I N } ( \mathsf { n } + 1 ) }$ （负输入）之间的差。此时，通道（n+1）不能用于单端模式和差分模式，且不能配置转换功能。

通道15、16、17、18和19被强制为单端配置（相应的DIFCTL[n]位始终为零），因为它们已连接到内部通道。

当通道n用于差分输入模式时，两个通道的输入电压应为差分信号（共模电压为V /2），电压输入范围仍为 $( V _ { R E F N } { \sim } V _ { R E F P } )$ 。

以最低有效位对齐，12位分辨率为例，

1) 当V<sub>INn</sub>为V<sub>REFP</sub>，V<sub>IN(n+1)</sub>为V<sub>REFN</sub>时，通道n的转换结果为0x0FFF；

2) 当V 为V ，V 为V 时，通道n的转换结果为0x0000；

3) 当 $\mathsf { \backslash V _ { I N n } }$ 为V<sub>REFP</sub>/2，V<sub>IN(n+1)</sub>为V<sub>REFP</sub>/2时，通道n的转换结果为0x07FF。

$\mathsf { D } _ { \mathsf { o u t } }$ 是ADC通道n的转换结果，则通道n转换的差分电压为：

$$
V _ {I n n} - V _ {I N (n + 1)} = V _ {R E F P} ^ {*} \left(2 ^ {*} D _ {\text {out}} / 4 0 9 5 - 1\right)\tag{14-1}
$$

## 14.4.5. 常规序列

通道管理电路可以将采样通道组织成一个序列：常规序列。常规序列支持最多16个通道，每个通道成为常规通道。

ADC_RSQ0寄存器的RL[3:0]位规定了整个常规序列的长度。ADC_RSQ0~ADC_RSQ2寄存器

规定了常规序列的通道选择。

## 14.4.6. 运行模式

## 单次运行模式

单次运行模式下，ADC_RSQ2寄存器的RSQ0[4:0]位规定了ADC的转换通道。当ADCON位被置1时，一旦相应软件触发或者外部触发发生，ADC就会采样和转换一个通道。


图 14-2. 单次运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/ba20c1a7633cd28e8d32044cd81f9fc5986e1f8bb41fb4630e4054d00ee0407d.jpg)


常规通道单次转换结束后，转换数据将被存放于ADC_RDATA寄存器中，EOC将会置1。如果EOCIE位被置1，将产生一个中断。

常规序列单次运行模式的软件流程：

1. 确保ADC_CTL0寄存器的DISRC位和SM位以及ADC_CTL1寄存器中的CTN位为0；

2. 用模拟通道编号来配置RSQ0；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，可以配置ADC_CTL1寄存器中的ETERC位和ETSRC位；

5. 设置SWRCST位，或者为常规序列产生一个外部触发信号；

6. 等到EOC置1；

7. 延迟一个CK_ADC后，从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EOC标志位。

注意：当EOC置1后，需延迟一个CK_ADC再读取ADC转换结果。

## 连续运行模式

对ADC_CTL1寄存器中的CTN位置1，可以使能连续运行模式。在此模式下，ADC执行由RSQ0[4:0]规定的转换通道。当ADCON位被置1，一旦相应软件触发或者外部触发产生，ADC就会采样和转换规定的通道。转换数据保存在ADC_RDATA寄存器中。


图 14-3. 连续运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/60bde2edd9881fca4a1fe5ddb2518dac739f3f725014b79e9eaef3a06528b79b.jpg)



常规序列连续运行模式的软件流程：


1. 设置ADC_CTL1寄存器中的CTN位为1；

2. 根据模拟通道编号来配置RSQ0；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETERC和ETSRC位；

5. 设置SWRCST位，或者给常规序列产生一个外部触发信号；

6. 等待EOC标志位置1；

7. 延迟一个CK_ADC后，从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EOC标志位；

9. 如果需要进行连续转换，重复步骤6~8。

注意：当EOC置1后，需延迟一个CK_ADC再读取ADC转换结果。

可以使用DMA来传输转换数据，不需循环查询EOC标志位：

1. 设置ADC_CTL1寄存器的CTN位为1；

2. 根据模拟通道编号配置RSQ0；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETERC位和ETSRC位；

5. 准备DMA模块，用于传输来自ADC_RDATA寄存器的数据；

6. 设置SWRCST位，或者给常规序列产生一个外部触发。

## 扫描运行模式

扫描运行模式可以通过将ADC_CTL0寄存器的SM位置1来使能。在此模式下，ADC扫描转换所有被ADC_RSQ0~ADC_RSQ2寄存器选中的所有通道。一旦ADCON位被置1，当相应软件触发或者外部触发产生，ADC就会一个接一个的采样和转换常规序列通道。转换数据存储在ADC_RDATA寄存器中。常规序列转换结束后，EOC位将被置1。如果EOCIE位被置1，将产生中断。当常规序列工作在扫描模式下时，ADC_CTL1寄存器的DMA位必须设置为1。

如果ADC_CTL1寄存器的CTN位也被置1，则在常规序列转换完之后，转换自动重新开始。


图 14-4. 扫描运行模式，且连续运行模式失能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/87c708be495b8c1593b22cd2eba1a831d2ad37a356e57054d6bfc3e0a8d7976b.jpg)


常规序列扫描运行模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 SM 位和 ADC_CTL1 寄存器的 DMA 位为 1；

2. 配置 ADC_RSQx 和 ADC_SAMPTx 寄存器；

3. 如果有需要，配置 ADC_CTL1 寄存器中的 ETERC 和 ETSRC 位；

4. 准备 DMA 模块，用于传输来自 ADC_RDATA 寄存器的数据；

5. 设置 SWRCST 位，或者给常规序列产生一个外部触发；

6. 等待 EOC 标志位置 1；

7. 写 0 清除 EOC 标志位。


图 14-5. 扫描运行模式，连续运行模式使能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/519389c092a8b6f11a0e37a0550790d0522a681eaa95d47db0597daa44db4dcd.jpg)


## 间断运行模式

当 ADC_CTL0 寄存器的 DISRC 位被置 1 时，常规序列间断运行模式被使能。该模式下，可以执行一次 n 个通道的短序列转换（n<=8），这个短序列是 ADC_RSQ0~RSQ2 寄存器所选择的转换序列的一部分。数值 n 由 ADC_CTL0 寄存器的 DISNUM[2:0]位给出。当相应的软件触发或外部触发发生，ADC 就会采样和转换在 ADC_RSQ0~RSQ2 寄存器所选择通道中接下来的 n 个通道，直到常规序列中所有的通道转换完成。每个常规序列转换周期结束后，EOC 位将被置 1。如果 EOCIE 位被置 1 将产生一个中断。


图 14-6. 间断运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/d853fc064b92ddc9b0ea242dcf8309dde1358095c157d0adaca4072d9ea7adee.jpg)


常规序列间断运行模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 DISRC 位和 ADC_CTL1 寄存器的 DMA 位为 1；

2. 配置 ADC_CTL0 寄存器的 DISNUM[2:0]位；

3. 配置 ADC_RSQx 和 ADC_SAMPTx 寄存器；

4. 如果有需要，配置 ADC_CTL1 寄存器中的 ETERC 位和 ETSRC 位；

5. 准备 DMA 模块，用于传输来自 ADC_RDATA 寄存器中的数据；

6. 设置 SWRCST 位，或者给常规序列产生一个外部触发；

7. 如果需要，重复步骤 6；

8. 等待 EOC 标志位置 1；

9. 写 0 清除 EOC 标志位。

## 14.4.7. 转换结果阈值监测功能

ADC_CTL0 寄存器中的 RWDEN 位置 1 时，将使能常规序列的模拟看门狗功能。该功能用于监测转换结果是否超过设定的阈值。如果 ADC 的模拟转换电压低于低阈值或高于高阈值时，ADC_STAT 状态寄存器的 WDE 位将被置 1。如果 WDEIE 位被置 1，将产生中断。ADC_WDHT和 ADC_WDLT 寄存器用来设定高低阈值。内部数据的比较在对齐之前完成，因此阈值与ADC_CTL1 寄存器中的 DAL 位确定的对齐方式无关。ADC_CTL0 寄存器的 RWDEN，WDSC和 WDCHSEL[4:0]位可以用来选择模拟看门狗监控单一通道或多通道。

常规通道数据

## 14.4.8. 数据存储模式

ADC_CTL1 寄存器的 DAL 位确定转换后数据存储的对齐方式。

在最高有效位对齐中，12/10/8 位数据按半字方式对齐，而 6 位数据按照字节的方式对齐的，如下 14-7. 12 ， 14-8. 10 ， 14-9. 8 和14-10. 6 所示。


图 14-7. 12 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


DAL=0 



常规通道数据


<table><tr><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>


DAL=1 



图 14-8. 10 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


常规通道数据


<table><tr><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>


DAL=1 



图 14-9. 8 位数据存储模式


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


常规通道数据


<table><tr><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>


DAL=1 



图 14-10. 6 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td></tr></table>


DAL=1 


## 14.4.9. 采样时间配置

ADC 使用多个 CK_ADC 周期对输入电压采样，采样周期数目可以通过 ADC_SAMPT0 和ADC_SAMPT1 寄存器的 SPTn[2:0]位配置。每个通道可以使用不同的时间采样。例如，在 12位分辨率的情况下，总转换时间=采样时间+12.5 个 CK_ADC 周期。

例如：

CK_ADC = 16MHz，采样时间为 2.5 个周期，那么总的转换时间为：“2.5+12.5”个 CK_ADC周期，即 0.9375us。

## 14.4.10. 外部触发配置

外部触发输入的上升沿可以触发常规序列的转换。常规序列的外部触发源由 ADC_CTL1 寄存器的 ETSRC[2:0]位控制。


表 14-3. ADC 的外部触发源


<table><tr><td>ETSRC[2:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>000</td><td>TIMER8_CH0</td><td rowspan="7">硬件触发</td></tr><tr><td>001</td><td>TIMER8_CH1</td></tr><tr><td>010</td><td>TIMER0_CH2(1)</td></tr><tr><td>011</td><td>TIMER1_CH1</td></tr><tr><td>100</td><td>TIMER2_TRGO</td></tr><tr><td>101</td><td>TIMER11_CH0</td></tr><tr><td>110</td><td>EXTI_11</td></tr><tr><td>111</td><td>SWRCST</td><td>软件触发</td></tr></table>


(1)该触发源仅适用于GD32L235xx系列产品，在GD32L233xx系列产品中，对应取值保留。


## 14.4.11. DMA 请求

DMA请求，可以通过设置ADC_CTL1寄存器的DMA位来使能，用来传输常规序列多个通道的转换结果。ADC在常规序列一个通道转换结束后产生一个DMA请求，DMA接受到请求后可以将转换的数据从ADC_RDATA寄存器传输到用户指定的目的地址。

## 14.4.12. ADC 内部通道

将 ADC_CTL1 寄存器的 TSVEN 位置 1，可以使能温度传感器通道（ADC_IN16）。温度传感器可以用来测量器件周围的温度。传感器输出电压能被 ADC 转换成数字量。建议温度传感器的采样时间至少设置为 t<sub>s_temp</sub>（具体数值请参考 datasheet 文档）。温度传感器不用时，复位TSVEN 位可以将其置于掉电模式。

温度传感器的输出电压随温度会发生线性变化，由于芯片生产过程的多样化，温度变化曲线的偏移在不同的芯片上会有不同（具体请见数据手册）。

使用温度传感器：

1. 配置 ADC 时钟（不超过 5MHz）；

2. 配置温度传感器通道（ADC_IN16）的转换序列和采样时间大于 $\mathrm { t s \_ t e m p }$ 

3. 置位 ADC_CTL1 寄存器中的 TSVEN 位，使能温度传感器；

4. 置位 ADC_CTL1 寄存器的 ADCON 位，或者由外部触发启动 ADC 转换；

5. 读取内部温度传感器输出电压 V<sub>temperature</sub>并由下面公式计算出实际温度：

对于 GD32L233xx 系列产品：

$$
\text { 温度 } \left(^ {\circ} \mathrm{C}\right) = \left\{\left(\mathrm{V} _ {\text { temperature }} - \mathrm{V} _ {3 0}\right) / \text { Avg\_Slope } \right\} + 3 0\tag{14-2}
$$

对于 GD32L235xx 系列产品：

$$
\text { 温度 } \left(^ {\circ} \mathrm{C}\right) = \left\{\left(\mathrm{V} _ {\text { temperature }} - \mathrm{V} _ {2 5}\right) / \text { Avg\_Slope } \right\} + 2 5\tag{14-3}
$$

V<sub>temperature</sub>：当前温度传感器采样得到的实际温度码值

V / V ：内部温度传感器在 $3 0 ^ { \circ } \mathsf { C } \mathrm { ~ / ~ } 2 5 ^ { \circ } \mathsf { C }$ 时的输出电压。芯片出厂时记录了温度传感器在 $3 0 ^ { \circ } \mathsf { C } / 2 5 ^ { \circ } \mathsf { C }$ 下对应的 ADC 转换结果。这个出厂校准值存储在 FLASH 中的只读区域，具体存储地址请见数据手册。

Avg_Slope：温度与内部温度传感器电压曲线的均值斜率，典型值请参考相关型号datasheet。

注意：

1）温度传感器使能后，需等待至少 3 个采样周期，ADC 转换码值才认为有效，前 3 个转换数据应舍弃；

2）可通过硬件过采样或软件求均值的方式提高温度传感器采样精度。

内部电压参考（V<sub>REFINT</sub>）提供了一个稳定的（带隙基准）电压输出给 ADC 和比较器。V<sub>REFINT</sub>内部连接到 ADC_IN17 输入通道。

当 ADC_CTL1 寄存器中的 INREFEN 位置 1 时，可以使能内部参考 V<sub>REFINT</sub>通道（ADC_IN17）。内部参考电压 V<sub>REFINT</sub>可以为 ADC 和比较器提供稳定的电压（带隙基准）， $V _ { R E F | N \top }$ 内部连接到到 $\mathsf { A D C \_ I N 1 7 } .$ 

## 14.4.13. 电池电压检测

V<sub>BAT</sub>通道可以用于监测从 V<sub>BAT</sub>引脚过来的备份电池电压。当ADC_CTL1寄存器中的VBATEN位置 1 时，使能 $\mathsf { V } _ { \mathsf { B A T } }$ 通道（ADC_IN18），同时一个集成在 V 引脚上的 3 分压桥也随之自动使能。由于 $\mathsf { V } _ { \mathsf { B A T } }$ 可能比 VDDA 高，所以使用这个 3 分压桥来确保 ADC 能够正常运行。它将 $A D C \_ N 1 8$ 输入通道连接到 ${ \tt V } _ { \tt B A T / 3 }$ ，所以，ADC_IN18 输入通道转换的值是 ${ \mathsf { V } } _ { \mathsf { B A T } } / 3 .$ 。为了防止不必要的电池能量消耗，推荐仅在需要时才使能 3 分压桥。

## 14.4.14. SLCD 电压检测

$V _ { \mathsf { S L C D } }$ 通道可以用于监测从 $V _ { \mathsf { S L C D } }$ 引脚上的电压。当 ADC_CTL1 寄存器中的 VSLCDEN 位置 1时，使能 $V \mathsf { s L C D }$ 通道（ADC_IN19），同时一个集成在 $V _ { \mathsf { S L C D } }$ 引脚上的 3 分压桥也随之自动使能。由于 $V _ { \mathsf { S L C D } }$ 可能比 VDDA 高，所以使用这个 3 分压桥来确保 ADC 能够正常运行。它将ADC_IN19 输入通道连接到 $\mathsf { V s L C D } / 3$ ，所以，ADC_IN19 输入通道转换的值是 $\mathsf { V s L C D } / 3$ o

## 14.4.15. 可编程分辨率（DRES）

ADC 分辨率可以通过寄存器 ADC_CTL0 中的 DRES[1:0]位进行配置。对于那些不需要高精度数据的应用，可以使用较低的分辨率来实现更快速地转换。只有在 ADCON 位为 0 时，才能修改 DRES[1:0]的值。较低的分辨率能够减少转换时间，如 14-4. tCONV所示，较低的分辨率能够减少逐次逼近步骤所需的转换时间 t<sub>ADC</sub>。


表 14-4. 不同分辨率对应的 t<sub>CONV</sub>时间


<table><tr><td>DRES [1:0] bits</td><td>tCONV (ADC时钟周期)</td><td>tCONV (ns)(fADC=16MHz)</td><td>tSMPL (ADC时钟周期)</td><td>tADC (ADC时钟周期)</td><td>tADC (ns)(fADC=16MHz)</td></tr><tr><td>12</td><td>12.5</td><td>781ns</td><td>2.5</td><td>15</td><td>937.5ns</td></tr><tr><td>10</td><td>10.5</td><td>656ns</td><td>2.5</td><td>13</td><td>812.5ns</td></tr><tr><td>8</td><td>8.5</td><td>531ns</td><td>2.5</td><td>11</td><td>687.5ns</td></tr><tr><td>6</td><td>6.5</td><td>406ns</td><td>2.5</td><td>9</td><td>562.5ns</td></tr></table>

## 14.4.16. 片上硬件过采样

片上硬件过采样单元执行数据预处理以减轻 CPU 负担。它能够处理多个转换，并将多个转换的结果取平均，得出一个 16 位宽的数据。

其结果根据如下公式计算得出，其中，N 和 M 的值可以被调整，过采样单元可以通过设置ADC_OVSAMPCTL 寄存器中的 OVSEN 位来使能，它是以降低数据输出率为代价，换取较高的数据分辨率。 $\mathsf { D } _ { \mathsf { o u t } }$ （n）是指 ADC 输出的第 n 个数字信号：

$$
\text { Result } = \frac {1}{M} * \sum_ {n = 0} ^ {n = N - 1} D _ {\text { OUT }} (n)\tag{14-3}
$$

片上硬件过采样单元执行两个功能：求和和位右移。过采样率 N 是在 ADC_OVSAMPCTL 寄存器的 OVSR[2:0]位定义，它的取值范围为 2x 到 256x。除法系数 M 定义了一个多达 8 位的右移，它通过 ADC_OVSAMPCTL 寄存器 OVSS[3:0]位进行配置。

求和单元能够生成一个多达 20 位（256*12 位）的值。首先，将这个值进行右移，将移位后剩余的部分再通过取整转化一个近似值，最后将高位截断，仅保留最低 16 位有效位作为最终值传入对应的数据寄存器中。


图 14-11. 20 位到 16 位的结果截断


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/480c1f133cc3ed4382b9bc1af0b5c52d0a6b9f86b0ef06ba1f976a931aff0514.jpg)


注意：如果移位后的中间结果还是超过 16 位，那么该结果的高位就会被直接截掉。

14-12. 5 描述了一个从原始20位的累积数值处理成16位结果值的例子。


图 14-12. 右移 5 位和取整的数例


<table><tr><td></td><td>15</td><td>11</td><td>7</td><td>3</td><td>0</td></tr><tr><td>四舍五入取近似值以及右移5位之后的结果</td><td>1</td><td>5</td><td>6</td><td>6</td><td></td></tr></table>

14-5. N M 给出了 N 和 M 的各种组合的数据格式，初始转换值为 0xFFF。


表 14-5. 不同 N 和 M 组合的最大输出值（灰色值表示截断）


<table><tr><td>过采样率</td><td>最大原始数据</td><td>无移位OVSS=0000</td><td>1位移位OVSS=0001</td><td>2位移位OVSS=0010</td><td>3位移位OVSS=0011</td><td>4位移位OVSS=0100</td><td>5位移位OVSS=0101</td><td>6位移位OVSS=0110</td><td>7位移位OVSS=0111</td><td>8位移位OVSS=1000</td></tr><tr><td>2x</td><td>0x1FFE</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td><td>0x003F</td><td>0x001F</td></tr><tr><td>4x</td><td>0x3FFC</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td><td>0x003F</td></tr><tr><td>8x</td><td>0x7FF8</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td></tr><tr><td>16x</td><td>0xFFFF0</td><td>0xFFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td></tr><tr><td>32x</td><td>0x1FFE0</td><td>0xFFE0</td><td>0xFFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td></tr><tr><td>64x</td><td>0x3FFC0</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td></tr><tr><td>128x</td><td>0x7FF80</td><td>0xFF80</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td></tr><tr><td>256x</td><td>0xFFFF00</td><td>0xFF00</td><td>0xFF80</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td></tr></table>

和标准的转换模式相比，过采样模式的转换时间不会改变：在整个过采样序列的过程中采样时间仍然保持相等。每 N 个转换就会产生一个新的数据，一个等价的延迟为：

$$
N x t _ {A D C} = N x \left(t _ {S M P L} + t _ {C O N V}\right)\tag{14-4}
$$

## 过采样配合 ADC工作模式

当过采样使能时，大多数 ADC 工作模式都是可用的。

◼ 常规序列通道

◼ 由软件触发或外部触发开始 ADC 转换

◼ 单次或扫描模式，连续或间断运行模式

◼ 可编程的采样时间

## ◼ 模拟看门狗

只有当 ADCON=0 时，才可以改变过采样的配置，并且要保证在设置 ADCON=1 之前要对过采样进行配置。

## 14.4.17. ADC 中断

以下任一个事件发生都可以产生中断：

◼ 常规序列转换结束；

◼ 模拟看门狗事件；

单独的中断使能位用于灵活设置ADC中断。
