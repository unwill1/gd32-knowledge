## 17. 模数转换器（ADC）

## 17.1. 简介

MCU 片上集成了 12 位逐次逼近式模数转换器模块（ADC），ADC0 有 14 个外部通道，5 个内部通道（内部温度传感通道（V ）、电池电压（V ）通道、DAC0_OUT0 通道、DAC0_OUT1通道和参考电压输入通道（V<sub>REFINT</sub>）），ADC1 有 16 个外部通道，3 个内部通道（DAC1_OUT0通道、DAC1_OUT1 通道和参考电压输入通道（V<sub>REFINT</sub>）），ADC2 有 15 个外部通道，5 个内部通道（参考电压输入通道（V<sub>REFINT</sub>）、DAC2_OUT0 通道、DAC2_OUT1 通道、高精度温度传感器通道（V<sub>SENSE2</sub>）和电池电压（V<sub>BAT</sub>）通道），ADC3 有 18 个外部通道，3 个内部通道（DAC3_OUT0通道、DAC3_OUT1 通道和参考电压输入通道（V<sub>REFINT</sub>））。ADC 采样通道均支持多种运行模式，采样转换后，转换结果可以按照最低有效位对齐或最高有效位对齐的方式保存在相应的数据寄存器中。片上的硬件过采样机制可以通过减少来自 MCU 的相关计算负担来提高性能。

## 17.2. 主要特征

 高性能：

ADC采样分辨率：12位、10位、8位或者6位分辨率；

ADC采样率：12位分辨率为5.3 MSPs，10位分辨率为6.15 MSPs，8位分辨率为7.27MSPs，6位分辨率为8.89 MSPs。分辨率越低，转换越快；

前置校准时间：902个ADC时钟周期；

可编程采样时间；

数据存储模式：最高有效位对齐和最低有效位对齐；

DMA请求。

 模拟输入通道：

ADC0有14个外部模拟输入通道，ADC1有16个外部模拟输入通道，ADC2有15个外部模拟输入通道，ADC3有18个外部模拟输入通道；

– 1个内部温度传感通道（V<sub>SENSE</sub>）；

– 1个内部参考电压输入通道（V<sub>REFINT</sub>）；

– 1个外部监测电池V<sub>BAT</sub>供电引脚输入通道；

– 1个内部高精度温度传感器通道（V<sub>SENSE2</sub>）；

– 与DAC内部通道连接。

 转换开始的发起：

– 软件；

TRIGSEL触发。

 运行模式：

转换单个通道，或者扫描一序列的通道；

– 单次运行模式，每次触发转换一次选择的输入通道；

连续运行模式，连续转换所选择的输入通道；

间断运行模式；

同步模式（适用于具有两个或多个ADC的设备）。

 转换结果阈值监测器功能：模拟看门狗。

 常规序列转换结束、模拟看门狗事件和溢出事件都可以产生中断。

 过采样：

32位的数据寄存器；

可调整的过采样率，从2x到1024x；

11位的可编程数据移位。

 通道输入范围：V<sub>REFN</sub> ≤V<sub>IN</sub> ≤V<sub>REFP</sub>；

 数据可以路由到HPDF进行后期处理。

## 17.3. 引脚和内部信号

17-1. ADC 给出了 ADC 框图。 17-1. ADC 给出了 ADC 内部信号。17-2. ADC 给出了 ADC 引脚说明。


表 17-1. ADC 内部输入信号


<table><tr><td>内部信号名称</td><td>说明</td></tr><tr><td><eq>V_{SENSE}</eq></td><td>内部温度传感器输出电压</td></tr><tr><td><eq>V_{SENSE2}</eq></td><td>内部高精度温度传感器输出电压</td></tr><tr><td><eq>V_{REFINT}</eq></td><td>内部参考输出电压</td></tr><tr><td><eq>V_{BAT}</eq></td><td>外部电池电压</td></tr></table>


表 17-2. ADC 输入引脚定义


<table><tr><td>名称</td><td>注释</td></tr><tr><td><eq>V_{DDA}</eq></td><td>模拟电源输入等于<eq>V_{DD}</eq></td></tr><tr><td><eq>V_{SSA}</eq></td><td>模拟地,等于<eq>V_{SS}</eq></td></tr><tr><td><eq>V_{REFP}</eq></td><td>ADC正参考电压</td></tr><tr><td><eq>V_{REFN}</eq></td><td>ADC负参考电压</td></tr><tr><td>ADCx_IN[17:0]</td><td>多达18路外部通道</td></tr></table>


注意：V<sub>DDA</sub> 和 V<sub>SSA</sub> 必须分别连接到 V<sub>DD</sub> 和 V<sub>SS</sub>。


## 17.4. 功能描述


图 17-1. ADC 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/9c7ae95c9961c3ad7f3b23b881ba77b4175c381babb1c301fc2c3de1cc2936dd.jpg)


## 17.4.1. 前置校准功能

在前置校准期间，ADC 计算一个校准系数，这个系数是应用于 ADC 内部的，它直到 ADC 下次掉电才无效。在校准期间，应用不能使用 ADC，它必须等到校准完成。在 A/D 转换前应执行校准操作。通过软件设置 CLB=1 来对校准进行初始化，在校准期间 CLB 位会一直保持 1，直到校准完成，该位由硬件清 0。

当 ADC 运行条件改变（例如，V<sub>DDA</sub>、V<sub>REFP</sub> 以及温度等），建议重新执行一次校准操作。

内部的模拟校准通过设置 ADC_CTL1 寄存器的 RSTCLB位来重置。

软件校准过程：

1. 确保ADCON=1；

2. 延迟14个CK_ADC以等待ADC稳定；

3. 设置RSTCLB （可选的）；

4. 设置CLB=1；

5. 等待直到CLB=0。

## 17.4.2. 双时钟域架构

时钟控制器提供的 CK_ADC 时钟与 AHB 时钟同步。在此模式下，ADC_SYNCCTL 寄存器中的ADCSCK[3:0]不能设置为 0000。分割因子可以是 2、4、6、8、10、12、14、16，最大频率为 80MHz。

CK_ADC 也可以由 CK_PLLR 或 CK_SYS 提供，后者可以是异步的，独立于 AHB 时钟。在此模式下，ADC_SYNCCTL 中的 ADCSCK[3:0]应设置为 0000。可通过 ADC_SYNCCTL的 ADCCK[3:0]配置分割因子。

RCU 控制器具有专用于 ADC 时钟的可编程预分频器。

注意：ADC1 和 ADC2 时钟共享 ADC0 时钟，当使用 ADC1 和 ADC2 时，必须打开 ADC0 时钟，且只能通过 ADC0 进行时钟分频。

## 17.4.3. ADCON 使能

ADC_CTL1 寄存器中的 ADCON 位是 ADC 模块的使能开关。如果该位为 0，则 ADC 模块保持复位状态。为了省电，当 ADCON 位为 0 时，ADC 模拟子模块将会进入掉电模式。ADC 使能后需等待 t<sub>SU</sub>时间后才能采样，t<sub>SU</sub>数值详见芯片数据手册。

## 17.4.4. 单端和差分输入通道

通过配置 ADC_DIFCTL 寄存器中的 DIFCTL[21:0]位域，可以配置 ADC 通道为单端输入模式或差分输入模式。只有在 ADC 禁能（ADCON = 0）的情况下才能进行该配置。

单端输入模式下，通道 n 要转换的模拟电压是外部电压 $\mathsf { V } _ { \mathsf { I N n } }$ （正输入）和 $V _ { R E F N }$ （负输入）之间的差。差分输入模式下，通道 n 要转换的模拟电压是外部电压 $\mathsf { V } _ { \mathsf { I N n } }$ （正输入）和通道 m 外部电压 $\mathsf { V } _ { \mathsf { I N m } }$ （负输入）之间的差。差分通道引脚分配如 17-3. ADC 。


表 17-3. ADC 差分通道引脚匹配


<table><tr><td rowspan="2">差分通道n编号</td><td colspan="2">ADC0</td><td colspan="2">ADC1</td><td colspan="2">ADC2</td><td colspan="2">ADC3</td></tr><tr><td><eq>V_{INn}</eq>引脚</td><td><eq>V_{INm}</eq>引脚</td><td><eq>V_{INn}</eq>引脚</td><td><eq>V_{INm}</eq>引脚</td><td><eq>V_{INn}</eq>引脚</td><td><eq>V_{INm}</eq>引脚</td><td><eq>V_{INn}</eq>引脚</td><td><eq>V_{INm}</eq>引脚</td></tr><tr><td>0</td><td>PA0</td><td>PA1</td><td>PA0</td><td>PA1</td><td>PB1</td><td>PE9</td><td>PE14</td><td>PE15</td></tr><tr><td>1</td><td>PA1</td><td>PA2</td><td>PA1</td><td>PA6</td><td>PE9</td><td>PE13</td><td>PE15</td><td>PB12</td></tr><tr><td>2</td><td>PA2</td><td>PA3</td><td>PA6</td><td>PA7</td><td>PE13</td><td>PE7</td><td>PB12</td><td>PB14</td></tr><tr><td>3</td><td>PA3</td><td>PB14</td><td>PA7</td><td>PC4</td><td>PE7</td><td>PB13</td><td>PB14</td><td>PB15</td></tr><tr><td>4</td><td>PB14</td><td>PC0</td><td>PC4</td><td>PC0</td><td>PB13</td><td>PE8</td><td>PB15</td><td>PE8</td></tr><tr><td>5</td><td>PC0</td><td>PC1</td><td>PC0</td><td>PC1</td><td>PE8</td><td>PD10</td><td>PE8</td><td>PD10</td></tr><tr><td>6</td><td>PC1</td><td>PC2</td><td>PC1</td><td>PC2</td><td>PD10</td><td>PD11</td><td>PD10</td><td>PD11</td></tr><tr><td>7</td><td>PC2</td><td>PC3</td><td>PC2</td><td>PC3</td><td>PD11</td><td>PD12</td><td>PD11</td><td>PD12</td></tr><tr><td>8</td><td>PC3</td><td>PF0</td><td>PC3</td><td>PF1</td><td>PD12</td><td>PD13</td><td>PD12</td><td>PD13</td></tr><tr><td>9</td><td>PF0</td><td>PB12</td><td>PF1</td><td>PC5</td><td>PD13</td><td>PD14</td><td>PD13</td><td>PD14</td></tr><tr><td>10</td><td>PB12</td><td>PB1</td><td>PC5</td><td>PB2</td><td>PD14</td><td>PB0</td><td>PD14</td><td>PD8</td></tr><tr><td>11</td><td>PB1</td><td>PB0</td><td>PB2</td><td>PA5</td><td>PE11</td><td>PE10</td><td>PD8</td><td>PD9</td></tr><tr><td>12</td><td>PB0</td><td>PB1</td><td>PA5</td><td>PB11</td><td>PE10</td><td>PE11</td><td>PD9</td><td>PE10</td></tr><tr><td>13</td><td>PB11</td><td>PB0</td><td>PB11</td><td>PB15</td><td>PE12</td><td>PE11</td><td>PE10</td><td>PE11</td></tr><tr><td>14</td><td>PB12</td><td>PB11</td><td>PA5</td><td>PA4</td><td>PB1</td><td>PB0</td><td>PE11</td><td>PE12</td></tr><tr><td>15</td><td>PB11</td><td>PB12</td><td>PA4</td><td>PA5</td><td>PB0</td><td>PB1</td><td>PE12</td><td>PE14</td></tr><tr><td>16</td><td>PC1</td><td>PC0</td><td>PC1</td><td>PC0</td><td>PE10</td><td>PE9</td><td>PA8</td><td>PA9</td></tr><tr><td>17</td><td>PC2</td><td>PC1</td><td>PC2</td><td>PC1</td><td>PE9</td><td>PE10</td><td>PA9</td><td>PA8</td></tr><tr><td>18</td><td>PC3</td><td>PC2</td><td>PC3</td><td>PC2</td><td>PD14</td><td>PD13</td><td>PB15</td><td>PD8</td></tr><tr><td>19</td><td>PA1</td><td>PA0</td><td>PA1</td><td>PA0</td><td>PD13</td><td>PD12</td><td>PD8</td><td>PB15</td></tr><tr><td>20</td><td>PA2</td><td>PA1</td><td>PC4</td><td>PA7</td><td>PD12</td><td>PD11</td><td>PD9</td><td>PD8</td></tr><tr><td>21</td><td>PA3</td><td>PA2</td><td>PA7</td><td>PA6</td><td>PD11</td><td>PD10</td><td>PE15</td><td>PE14</td></tr></table>


当通道 n 用于差分输入模式时，两个通道的输入电压应为差分信号（共模电压为 V<sub>REFP</sub>/2），电压输入范围仍为（V<sub>REFN</sub>~V<sub>REFP</sub>）。


以右对齐，12 位分辨率为例，

1) 当V<sub>INn</sub>为V<sub>REFP</sub>，V<sub>INm</sub>为V<sub>REFN</sub>时，通道n的转换结果为0x0FFF；

2) 当V<sub>INn</sub>为V<sub>REFN</sub>，V<sub>INm</sub>为V<sub>REFP</sub>时，通道n的转换结果为0x0000；

3) 当 $\mathsf { \partial } \mathsf { V } _ { \mathsf { I N n } }$ 为 $N _ { \mathsf { R E F P } } / 2$ $\mathsf { V } _ { \mathsf { I N m } }$ 为V<sub>REFP</sub>/2时，通道n的转换结果为0x07FF。

$\mathsf { D } _ { \mathsf { o u t } }$ 是 ADC 通道 n 的转换结果，则通道 n 转换的差分电压为：

$$
V _ {I N n} - V _ {I N m} = V _ {R E F P} ^ {*} (2 ^ {*} D _ {\text {out}} / 4 0 9 5 - 1)\tag{17-1}
$$

## 17.4.5. 常规序列

通道管理电路可以将采样通道组织成一个序列：常规序列。常规序列支持最多 22 个通道，每个通道称为常规通道。

ADC_RSQ0~ADC_RSQ8 寄存器规定了常规序列的通道选择。ADC_RSQ0 寄存器的 RL[3:0]位规定了整个常规序列的长度。

注意：尽管 ADC 支持 22 个通道，但常规序列一次最多转换 16 个通道。

## 17.4.6. 运行模式

单次运行模式

单次转换模式下，ADC_RSQ8 寄存器的 RSQ0[4:0]位规定了 ADC 的转换通道。当 ADCON 位被置 1，一旦相应软件触发或者 TRIGSEL 触发发生，ADC 就会采样和转换一个通道。


图 17-2. 单次运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/c8963d71f323635883363415c3b59a504fda4d5c8c567a9a6cec3cb1bb1e6750.jpg)


常规序列的通道单次转换结束后，转换数据将被存放于 ADC_RDATA 寄存器中，EOC 将会置 1。如果 EOCIE 位被置 1，将产生一个中断。

常规序列单次转换模式的软件流程：

1. 确保ADC_CTL0寄存器的DISRC和SM位以及ADC_CTL1寄存器的CTN位为0；

2. 用模拟通道编号来配置RSQ0；

3. 配置ADC_RSQx寄存器；

4. 如果有需要，可以配置ADC_CTL1寄存器的ETMRC[1:0]位；

5. 设置SWRCST位，或者为常规序列产生一个TRIGSEL触发信号；

6. 等到EOC置1；

7. 从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EOC标志位。

## 连续运行模式

对 ADC_CTL1 寄存器的 CTN 位置 1 可以使能连续运行模式。在此模式下，ADC 执行由 RSQ0 规定的转换通道。当 ADCON 位被置 1，一旦相应软件触发或者 TRIGSEL 触发产生，ADC 就会采样和转换规定的通道。转换数据保存在 ADC_RDATA 寄存器中。


图 17-3. 连续运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/da153c81f8aecb1451a9c0bdf72d9f1ddd6f2b6892a13f252c183a7de94f8b30.jpg)


常规序列连续运行模式的软件流程：

1. 设置ADC_CTL1寄存器的CTN位为1；

2. 根据模拟通道编号配置RSQ0；

3. 配置ADC_RSQx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETMRC[1:0]位；

5. 设置SWRCST位，或者给常规序列产生一个TRIGSEL触发信号；

6. 等待EOC标志位置1；

7. 从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EOC标志位；

9. 只要还需要进行连续转换，重复步骤6~8。

由于要循环查询 EOC 标志位，DMA可以被用来传输转换数据，软件流程如下：

1. 设置ADC_CTL1寄存器的CTN位为1；

2. 根据模拟通道编号配置RSQ0；

3. 配置ADC_RSQx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETMRC[1:0]位；

5. 准备DMA模块，用于传输来自ADC_RDATA的数据；

6. 设置SWRCST位，或者给常规序列产生一个TRIGSEL触发。

## 扫描运行模式

扫描转换模式可以通过将 ADC_CTL0 寄存器的 SM 位置 1 来使能。在此模式下，ADC 扫描转换所有被 ADC_RSQ1~ADC_RSQ8 寄存器选中的所有通道。一旦 ADCON 位被置 1，当相应软件触发或者 TRIGSEL 触发产生，ADC 就会一个接一个的采样和转换常规序列通道。转换数据存储在ADC_RDATA寄存器中。常规序列转换结束后，EOC 位将被置 1。如果 EOCIE 被置 1，将产生中断。当常规序列工作在扫描模式下时，ADC_CTL1 寄存器的 DMA位必须设置为 1。

如果 ADC_CTL1 寄存器的 CTN 位也被置 1，则在常规序列转换完之后，这个转换自动重新开始。


图 17-4. 扫描转换模式，且连续转换模式失能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/fd1b7b753e56abfd52dffd9220b7994af12d63624f1dc449a1d2f2445f204987.jpg)


常规序列扫描转换模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 SM 位和 ADC_CTL1 寄存器的 DMA 位为 1；

2. 配置 ADC_RSQx 寄存器；

3. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMRC[1:0]位；

4. 准备 DMA 模块，用于传输来自 ADC_RDATA 的数据；

5. 设置 SWRCST 位，或者给常规序列产生一个 TRIGSEL 触发；

6. 等待 EOC 标志位置 1；

7. 写 0 清除 EOC 标志位。


图 17-5. 扫描转换模式，连续转换模式使能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/e243eaa66d613257b1193965f9230ef08179a8a7a9e094a6b098041ac1c58eb2.jpg)


## 间断模式

ADC_CTL0 寄存器的 DISRC 位置 1 时，常规序列使能间断运行模式。该模式下可以执行一次 n个通道的短序列转换（n 不超过 8），该序列是 ADC_RSQ0~ADC_RSQ8 寄存器所选择的转换序列的一部分。数值n由ADC_CTL0寄存器的DISCNUM[2:0]位配置。当相应的软件触发或TRIGSEL触发发生，ADC 就会采样和转换在 ADC_RSQ0~ADC_RSQ8 寄存器所选择通道中接下来的 n 个通道，直到常规序列中所有的通道转换完成。每个常规序列转换周期结束后，EOC 位将被置 1。如果 EOCIE 位被置 1 将产生一个中断。


图 17-6. 间断运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/923bc36686e0cbd94feee25b7d90751dd4e4b4ba95b4f8999ecd899c2ea5500d.jpg)


常规序列断模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 DISRC 位和 ADC_CTL1 寄存器的 DMA 位为 1；

2. 配置 ADC_CTL0 寄存器的 DISNUM[2:0]位；

3. 配置 ADC_RSQx 寄存器；

4. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMR[1:0]位；

5. 准备 DMA 模块，用于传输来自 ADC_RDATA 的数据（参考 DMA模块）；

6. 设置 SWRCST 位，或者给常规序列产生一个 TRIGSE 触发；

7. 如果需要，重复步骤 6；

8. 等待 EOC 标志位置 1；

9. 写 0 清除 EOC 标志位。

## 17.4.7. 转换结果阈值监测功能

模拟看门狗 0

配置 ADC_CTL0 寄存器的 RWD0EN 位为 1，可使能常规序列的模拟看门狗功能 0。

如果 ADC 的模拟转换电压低于低阈值或高于高阈值时，ADC_STAT 状态寄存器的WDE0 位将置1。若 WDE0IE 位置 1，将产生中断。ADC_WDHT0 和 ADC_WDLT0 寄存器用来设定高低阈值。内部数据的比较在对齐之前完成，因此阀值与ADC_CTL1寄存器的DAL位确定的对齐方式无关。ADC_CTL0 寄存器的 RWD0EN，WD0SC 和 WD0CHSEL[4:0]位可以用来选择模拟看门狗 0 监控单一通道或者多个通道。

## 模拟看门狗 1/2

模拟看门狗 1/2 更加的灵活，可以进行单个或多个通道的看门狗功能配置。

通过配置 ADC_WD1SR 寄存器中的 AWD1CS[21:0]位域中的相应位，可以使能相应通道的模拟看门狗 1 功能，同理，可以配置看门狗 2 功能。模拟看门狗 1/2 的高/低阈值可在 ADC_WDLT1,ADC_WDHT1, ADC_WDLT2 和 ADC_WDHT2 寄存器中进行配置。

注：如果 OVSEN=1，模拟看门狗 0/1/2可以将转换的模拟电压（过采样后）与低阈值或高阈值进行比较。如果 OVSEN=0，模拟看门狗 0/1/2 可以将转换的模拟电压（过采样前）与低阈值或高阈值进行比较。

## 17.4.8. 数据存储模式

ADC_CTL1 寄存器的 DAL 位确定转换后数据存储的对齐方式。


图 17-7. 12 位数据存储模式


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>

<table><tr><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>


DAL=1 


6 位分辨率的数据存储模式不同于 12 位/10 位/8 位分辨率数据存储模式，如 17-8. 6。


图 17-8. 6 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td></tr></table>


DAL=1 


注意：ADC_OVSAMPCTL 寄存器中的 OVSEN 置位时，ADC_CTL1 寄存器中的 DAL 位值将被忽略，ADC 仅支持 LSB对齐。

## 17.4.9. 采样时间配置

ADC 使用若干个 CK_ADC 周期对输入电压采样，采样周期数目可以通过 ADC_RSQ0~ADC_RSQ8 寄存器的 RSMPn[9:0]位更改。每个序列可以用不同的时间采样。在 12 位分辨率的情况下，总转换时间=采样时间+12.5 个 CK_ADC 周期。

例如：

CK_ADC = 40MHz ，采样时间为 2.5 个周期，那么总的转换时间为：“2.5+12.5”个 CK_ADC 周期，即 0.375us。

## 17.4.10. 外部触发配置

TRIGSEL或者 SWRCST的上升沿可以触发常规序列的转换。常规序列的触发源由ADC_CTL1寄存器中的 ETMRC[1:0]位控制。


表 17-4. 常规序列外部触发源


<table><tr><td>ETMRC[1:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>01, 10, 11</td><td>TRIGSEL</td><td>来自TRIGSEL的信号</td></tr><tr><td>00</td><td>SWRCST</td><td>软件触发</td></tr></table>

## 17.4.11. DMA 请求

DMA请求，可以通过设置 ADC_CTL1 寄存器的 DMA 位来使能，它用于常规序列多个通道的转换结果。ADC 在常规序列一个通道转换结束后产生一个 DMA请求，DMA接受到请求后可以将转换的数据从 ADC_RDATA 寄存器传输到用户指定的目的地址。

## 17.4.12. 溢出检测

当 DMA 使能的时候，将 ADC_CTL1 寄存器的 EOCM 位置 1 可以使能溢出检测。如果一个常规转换在上一个常规转换数据读出之前已经完成，则会产生一个溢出事件，相应的 ADC_STAT 状态寄存器的 ROVF 标志位会置位。如果 ADC_CTL0 寄存器的 ROVFIE 置位，溢出中断产生。

为了使得 ADC 从 ROVF 溢出状态中恢复过来，建议对 DMA模块重新进行初始化。内部状态机复位，以保证常规转换数据正确的传输。ADC 转换将会停止，直到 ROVF 位被清零。

ADC 从 ROVF 状态恢复的软件流程如下：

1. 将 ADC_CTL1 寄存器的 DMA 位清 0；

2. 将 ADC_CTL1 寄存器的 ADCON 位清 0；

3. 将 DMA_CHxCTL 寄存器的 CHEN 位清 0，用于重新初始化 DMA 模块；

4. 将 ADC_STAT 寄存器的 ROVF 位清 0；

5. 将 DMA_CHxCTL 寄存器的 CHEN 位置 1；

6. 将 ADC_CTL1 寄存器的 DMA 位置 1；

7. 将 ADC_CTL1 的 ADCON 位置 1；

8. 等待 T（setup）；

9. 通过软件或触发开始 ADC 转换。

## 17.4.13. ADC 内部通道

将 ADC_CTL1 寄存器的 TSVEN1 位置 1 可以使能温度传感器通道（ADC0_IN14），将 ADC_CTL1寄存器的 TSVEN2 位置 1 可以使能高精度温度传感器通道（ADC2_IN18）。将 ADC_CTL1 寄存器的 INREFEN 位置 1 可以使能内部电压参考通道（ADC0_IN18 / ADC1_IN18 / ADC2_IN15 /ADC3_IN20）。温度传感器可以用来测量器件周围的温度。传感器输出电压能被 ADC 转换成数字量。建议温度传感器的采样时间至少设置为 $\mathrm { t s \_ t e m p \ \mu s }$ （具体数值请参考 datasheet 文档）。温度传感器不用时，复位 TSVEN1 和 TSVEN2，可以将其置于掉电模式。

温度传感器（只针对普通温度传感器）的输出电压随温度会发生线性变化，由于芯片生产过程的多样化，温度变化曲线的偏差在芯片间会有不同（最多相差 $45 \textdegree$ ）。内部温度传感器更适用于检测温度的变化，而不是用于测量绝对温度。如果需要测量精确的温度，应该使用一个外置的温度传感器来校准这个偏移错误。

内部电压参考 $( V _ { R E F | N T } )$ 提供了一个稳定的（带隙基准）电压输出给 ADC 和比较器。 $V _ { R E F | N \top }$ 内部连接到 ADC0_IN18、ADC1_IN18、ADC2_IN15、ADC3_IN20 输入通道。

## 使用温度传感器：

1．配置温度传感器通道（ADC0_IN14）的转换序列和采样时间为 t<sub>s_temp</sub> us；

2．置位 ADC_CTL1 寄存器中的 TSVEN1 位，使能温度传感器；

3．置位 ADC_CTL1 寄存器的 ADCON 位，或者由外部触发 ADC 转换；

4．从 ADC 数据寄存器中读取并计算温度传感器数据 V<sub>temperature</sub>，并由下面公式计算出实际温度：

$$
\text { 温度 } \left(^ {\circ} \mathrm{C}\right) = \left\{\left(\mathrm{V} _ {2 5} - \mathrm{V} _ {\text { temperature }}\right) / \text { Avg\_Slope } \right\} + 2 5
$$

$\vee _ { 2 5 } \colon$ 内部温度传感器在 $2 5 ^ { \circ } \mathsf { C }$ 下的电压，典型值及出厂校准值地址请参考 datasheet（参考Temperature sensor characteristics 章节）。

Avg_Slope：温度与内部温度传感器电压曲线的均值斜率，典型值请参考 datasheet（参考Temperature sensor characteristics 章节）。

## 使用高精度温度传感器：

1．配置 ADC 时钟（不超过 5MHz）；

2．配置温度传感器通道（ADC2_IN18）的转换序列和采样时间为 t<sub>s_temp</sub> us；

3．置位 ADC_CTL1 寄存器中的 TSVEN2 位，使能温度传感器；

4．置位 ADC_CTL1 寄存器的 ADCON 位，或者由外部触发 ADC 转换；

5．从 ADC 数据寄存器中读取并计算温度传感器数据 V<sub>temperature</sub>，并由下面公式计算出实际温度：

$$
\text { 温度 } \left(^ {\circ} \mathrm{C}\right) = \left\{\left(\mathrm{V} _ {\text { temperature }} - \mathrm{V} _ {2 5}\right) / \text { Avg\_Slope } \right\} + 2 5
$$

V<sub>25</sub>：内部温度传感器在 $2 5 ^ { \circ } \mathsf { C }$ 下的电压，典型值及出厂校准值地址请参考 datasheet（参考 High-precision temperature sensor characteristics 章节）。

Avg_Slope：温度与内部温度传感器电压曲线的均值斜率，典型值请参考 datasheet（参考 High-precision temperature sensor characteristics 章节）。

注意：

1) 当高精度温度传感器使能，至少需要等待 3 个 ADC 采样周期，前三个转换数据应当被舍弃；2) 可以通过过采样和软件平均提高高精度温度传感器准确度。

## 17.4.14. 电池电压检测电路

V<sub>BAT</sub>通道可用于测量V<sub>BAT</sub>引脚上的备用电池电压。当ADC_CTL1寄存器中的VBATEN位置位时，V<sub>BAT</sub>通道（ADC0_IN15 / ADC2_IN19）被启用，集成在 V<sub>BAT</sub>引脚上的 3 分压桥也被自动启用。由于V<sub>BAT</sub>可能高于V<sub>DDA</sub>，此桥用于确保ADC正确运行。它将V<sub>BAT</sub>/3连接到 ADC0_IN15 / ADC2_IN19通道中。因此，转换后的数字值为 V<sub>BAT</sub>/3。为了防止不必要的电池能耗，建议仅在需要时启用桥接器。

## 17.4.15. 使用 HPDF 管理转换结果

高性能数字滤波器（HPDF）可用于管理 ADC 转换结果。在这种情况下，HPDFCFG 位必须置 1，DMA 位 SYNCDMA[1:0]位域和 SYNCDDM 位必须清除为 0。如果 DMA 和 HPDF 并行工作，只有 DMA 生效。ADC 将常规数据寄存器数据的 16 个最低有效位传输到 HPDF，一旦传输完成，HPDF 将重置 EOC 标志。如 17-9. HFDF ADC 所示。


图 17-9. HFDF 与 ADC 模块握手信号示意图


<table><tr><td>PCLK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ADC0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>常规触发</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EOC_ADC0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EOC_ADC0_ACK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HPDFCFG</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 17.4.16. 可编程分辨率（DRES）

对寄存器 ADC_CTL0 中的 DRES[1:0]位进行编程即可配置分辨率为 6、8、10 及 12 位。对于那些不需要高精度数据的应用，可以使用较低的分辨率来实现更快速地转换。只有在 ADCON 位为 0时，才能修改 DRES[1:0]的值。ADC 转换的结果只有 12 位，其余没有被用到的低位读出来都是为

0。较低的分辨率能够减少转换时间。如 17-5. ADC tCONV 所示，较低的分辨率能够减少逐次逼近步骤所需的转换时间 t<sub>ADC</sub>。


表 17-5. ADC 不同分辨率对应的 $\tan$ 时间


<table><tr><td>DRES[1:0] bits</td><td>tCONV(ADC clock cycles)</td><td>tCONV(ns) at <eq>f_{ADC}=40MHz</eq></td><td>tSMPL(min)(ADC clock cycles)</td><td>tADC(ADC clock cycles)</td><td>tADC(ns) at <eq>f_{ADC}=40MHz</eq></td></tr><tr><td>12</td><td>12.5</td><td>312.5ns</td><td>2.5</td><td>15</td><td>375 ns</td></tr><tr><td>10</td><td>10.5</td><td>262.5 ns</td><td>2.5</td><td>13</td><td>325 ns</td></tr><tr><td>8</td><td>8.5</td><td>212.5ns</td><td>2.5</td><td>11</td><td>275 ns</td></tr><tr><td>6</td><td>6.5</td><td>162.5 ns</td><td>2.5</td><td>9</td><td>225 ns</td></tr></table>

## 17.4.17. 片上硬件过采样

片上硬件过采样单元执行数据预处理以减轻 CPU 负担。它能够处理多个转换，并将多个转换的结果取平均，增加数据宽度，最高可达 32 位。其结果值根据如下公式计算得出，其中 N 和 M 的值可以被调整，过采样单元可以通过设置 ADC_OVSAMPCTL 寄存器的 OVSEN 位来使能，它是以降低数据输出率为代价，换取较高的数据分辨率。 $\sf { D _ { o u t } ( n ) }$ 是指 ADC 输出的第 n 个数字信号：

$$
\mathrm{Result} = \frac {1}{M} ^ {*} \sum_ {n = 0} ^ {N - 1} D _ {\mathrm{out}} (n)\tag{17-2}
$$

片上硬件过采样单元执行两个功能：求和和位右移。过采样率 N 是在 ADC_OVSAMPCTL 寄存器的 OVSR[9:0]位定义，它的取值范围为 2x 到 1024x。除法系数 M 定义一个多达 11 位的右移，它通过 ADC_OVSAMPCTL 寄存器 OVSS[3:0]位进行配置。

求和单元能够生成一个多达 22 位（1024*12 位）的值。首先进行右移，最终值传入对应的数据寄存器中。


图 17-10. 12 位 ADC 右移 5 位和取整的数例


<table><tr><td>19</td><td>15</td><td>11</td><td>7</td><td>3</td><td>0</td></tr><tr><td>2</td><td>A</td><td>C</td><td>D</td><td>6</td><td></td></tr></table>

<table><tr><td>15</td><td>11</td><td>7</td><td>3</td><td>0</td></tr></table>


四舍五入取近似值以及右移5位之后的结果


<table><tr><td>1</td><td>5</td><td>6</td><td>6</td></tr></table>

和标准的转换模式相比，过采样模式的转换时间不会改变：在整个过采样序列的过程中采样时间仍

然保持相等。每 N 个转换就会产生一个新的数据，一个等价的延迟为：

$$
N \times t _ {A D C} = N \times \left(t _ {S M P L} + t _ {C O N V}\right)\tag{17-3}
$$

## 17.4.18. 增益模式

当 GAINEN 位在 ADC_CTL1 寄存器中置位时，对所有 ADC 转换的数据进行增益校准。每次转换后，使用下面的公式计算数据:

$$
\text { DATA } (\text { new   ADC   result }) = \text { DATA } (\text { original   ADC   result }) \times (\text { GAIN } / 4 0 9 6)\tag{17-4}
$$

可编程 GAIN 位域范围为 0 ~ 16383，实际增益因子(GAIN / 4096)为 0 ~ 3.999756。

## 17.4.19. ADC 转换信号

ADC转换信号ADC_CONV在ADC通道转换期间保持高电平状态，而在其他时间段都为低电平。ADC_CONV信号可内部通过TRIGSEL连接到CLAx模块，作为CLAx多路选择器的输入。


图 17-11. 常规序列连续转换模式下的 ADC 转换信号


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/ec687ecc9d6bfb4c1e9f8ee897de1ede2c333e1480e726eb5073b654e287b058.jpg)


## 17.5. ADC 同步模式

在具有多个 ADC 的设备上，可以使用 ADC 同步模式。

在 ADC 同步模式中，通过 ADC0 的触发器来同步 ADC1 和 ADC2 的转换。根据 ADC_SYNCCTL寄存器的 SYNCM[4:0]位来选择两个或三个 ADC 按并行模式还是交替模式进行转换。

在 ADC 同步模式中，当转换配置成外部事件触发时，ADC1 和 ADC2 的外部触发必须失能。常规通道的转换结果存储在 ADC 同步常规数据寄存器(ADC_SYNCDATA)中。

ADC 同步模式如 17-6. ADC 所示。


表 17-6. ADC 同步模式表


<table><tr><td>SYNCM[4: 0]</td><td>mode</td></tr><tr><td>00000</td><td>独立模式。所有的ADC都独立工作。</td></tr><tr><td>00110</td><td>ADC0和ADC1工作在常规并行模式。ADC2 独立工作。</td></tr><tr><td>00111</td><td>ADC0和ADC1工作在常规跟随模式。ADC2 独立工作。</td></tr><tr><td>10110</td><td>ADC0、ADC1和ADC2工作在常规并行模式。</td></tr><tr><td>10111</td><td>ADC0、ADC1和ADC2工作在常规跟随模式。</td></tr></table>

当 ADC 工作在同步模式，而非独立模式时，如果需要再将 ADC 配置成其他同步模式，则需要在配置成其他同步模式前，首先将 ADC 配置成独立模式。

ADC 同步框图如 17-12. ADC 所示。


图 17-12. ADC 同步框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/1fb8347ead33ec1c7e489e814e0ba38f6d737a9a8782c4eafe79f608b51b643b.jpg)


## 17.5.1. 独立模式

在这种模式下，ADC 同步是忽略的，每个 ADC 都独立工作。

## 17.5.2. 常规并行模式

设置 ADC_SYNCCTL 寄存器的 SYNCM[4:0]位为 00110 或 10110，使能常规并行模式。在常规并行模式中，根据 ADC0 中选择的外部触发，所有的 ADC 并行的转换常规通道。触发选择由 ADC0的 ADC_CTL1 寄存器 ETMRC[1:0]位进行配置。

根据 ADC_CTL1 寄存器中的 EOCM 位的设置，在转换结束时产生 EOC 中断（如果 ADC 接口使能了该中断）。常规并行模式的行为如 17-13. 16 所示。


图 17-13. 基于 16 个通道的常规并行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/2c6c1b74a5aeaf50ea57d4ed0960bd8e0829a7fe1a82919172c043ee068019b1.jpg)


## 注意：

1. 在一个给定的时间，两个 ADC 不能同时转换同一个通道。（当转换同一通道时，不能覆盖采样时间）

2. 确保在没有任何一个 ADC 在进行转换的时候才触发 ADC。

3. 如果 SYNCM=5’b 00110，ADC2 工作在独立模式。

## 17.5.3. 常规跟随模式

设置 ADC_SYNCCTL 寄存器的 SYNCM[4:0]位为 5’b 00111 或 5’b 10111，使能常规跟随模式。在常规跟随模式中，根据选择的外部触发，ADC0 开始转换常规序列。外部触发选择由 ADC0 的ADC_CTL1 寄存器 ETMRC[1:0]位进行配置。经过一定的延迟之后，ADC1 开始转换常规序列，再经过另一个延迟之后，ADC2 开始转换常规序列。以上描述中提到的常规序列只能包含一个通道。

在两个连续采样阶段之间的延迟时间，由 ADC_SYNCCTL 寄存器的 SYNCDLY[3:0]位进行配置。如果 SYNCDLY[3:0]位配置的延迟时间比采样时间还短，为了避免在一个给定时间，多个 ADC 对同一个通道进行采样，会将(采样时间 + 2) CK_ADC 周期作为实际的延迟时间。

如果 ADC_CTL1 寄存器的 CNT 位置 1，选择的常规序列会被连续的转换。根据 ADC_CTL1 寄存器的 EOCM 的配置，在转换事件结束时产生 EOC 中断（如果 ADC 使能了该中断）。常规跟随模式的行为如图17-14. 一个采用连续转换模式通道上的常规跟随模式所示


图 17-14. 一个采用连续转换模式通道上的常规跟随模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/94e5d6c0a9ab1be6e0b4372da14684bdfb7d6f856b38cc172a5ac3539697ff7e.jpg)


## 注意：

1. 确保在没有任何一个 ADC 在进行转换的时候才触发 ADC（当有某些转换还没完成时，不触发 ADC0）；

2. 如果 SYNCM=5’b 00111，ADC2 工作在独立模式。

## 17.5.4. 在 ADC同步模式中使用 DMA

在 ADC 同 步 模 式 中 ，常规序列通 道 转 换 的 数 据 存 储 在 ADC 同 步常 规数据寄存器(ADC_SYNCDATA)中，DMA 可以用来传输 ADC_SYNCDATA 寄存器的数据。有以下两种 DMA工作模式，可以和各种 ADC 同步模式很好地配合使用。

## ADC 同步 DMA 模式 0

在 ADC 同步 DMA 模式 0 中，DMA 传输的位宽为 32。一次 DMA 请求传输一个数据，这个数据轮流的从各 ADC 的常规转换结果中取出。对于每次 DMA 请求，DMA 通道的源地址固定为ADC_SYNCDATA 寄存器，而这个寄存器的内容会变成 DMA要被传输的数值。当 ADC0 和 ADC1工作在同步模式时，DMA 的传输序列为：ADC0_RDATA[31:0] -> ADC1_RDATA[31:0] ->ADC0_RDATA[31:0] -> ADC1_RDATA[31:0]。当所有的 ADC 都工作在同步模式时，DMA 的传输序 列 为 ： ADC0_RDATA[31:0] -> ADC1_RDATA[31:0] -> ADC2_RDATA[31:0] ->ADC0_RDATA[31:0] -> ADC1_RDATA[31:0] -> ADC2_RDATA[31:0]。

ADC 同步 DMA 模式 0 适用于：

 ADC0 和 ADC1 工作在常规并行模式(SYNCM=00110)；

 所有的 ADC 工作在常规并行模式(SYNCM=5’b 10110)。

## ADC 同步 DMA 模式 1

在 ADC 同步 DMA 模式 1 中，DMA 传输的位宽为 32。一次 DMA 请求传输两个数据，这些数据轮流的从各 ADC 的常规通道转换结果中取出。对于每次 DMA 请求，DMA 通道的源地址固定为ADC_SYNCDATA 寄存器，而这个寄存器的内容会变成 DMA要被传输的数值。当 ADC0 和 ADC1工作在同步模式时，DMA 的数据每次都为：{ADC1_RDATA[15:0], ADC0_RDATA[15:0]}。当所有的 ADC 都工作在同步模式时，DMA 的传输序列为：{ADC1_RDATA[15:0],ADC0_RDATA[15:0]} ->{ADC0_RDATA[15:0],ADC2_RDATA[15:0]} -> {ADC2_RDATA[15:0],ADC1_RDATA[15:0]} ->{ADC1_RDATA[15:0],ADC0_RDATA[15:0]}。

ADC 同步 DMA 模式 1 适用于：

 ADC0 和 ADC1 工作在常规并行模式(SYNCM=5’b 00110)；

 ADC0 和 ADC1 工作在常规跟随模式(SYNCM=5’b 00111)；

 所有的 ADC 工作在常规跟随模式(SYNCM=5’b 10111)。

## 17.6. 中断

以下任一个事件发生都可以产生中断：

 常规序列转换结束；

 模拟看门狗事件；

 溢出事件。

ADC0 和 ADC1 都被映射到同一个中断向量 IRQ18，ADC2 被映射到同一个中断向量 IRQ47，ADC3 都被映射到同一个中断向量 IRQ61。
