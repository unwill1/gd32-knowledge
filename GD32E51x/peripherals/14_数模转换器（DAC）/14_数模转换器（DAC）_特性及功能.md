## 14. 数模转换器（DAC）

## 14.1 . 简介

数字/模拟转换器可以将 12 位的数字数据转换为外部引脚上的电压输出。数据可以采用 8 位或12 位模式，左对齐或右对齐模式。当使能了外部触发，DMA 可被用于更新输入端数字数据。

在输出电压时，可以利用 DAC 输出缓冲区来获得更高的驱动能力。

DAC0 有两个通道 DAC0_OUT0 和 DAC0_OUT1，两个通道可以独立或并发工作。DAC1 仅有一个通道 DAC1_OUT0，只能独立工作。

## 14.2. 主要特征

DAC 的主要特征如下：

 8 位或 12 位分辨率；

 数据左对齐或右对齐；

 DMA功能与欠载检测；

 同步更新转换；

 外部事件触发转换；

 可配置的内部缓冲区；

 输入参考电压 V<sub>REFP</sub>；

 输出 FIFO；

 噪声波生成（LSFR 噪声模式和三角噪声模式）；

 DACx 双通道并发模式。

14-1. DAC 为 DAC 的结构框图， 14-1. DAC 给出了引脚描述。


图 14-1. DAC 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/c62d8fe5a379bdbf2138d95fd204e37d693a3eb0b87b024c117e80e4871cf667.jpg)



表 14-1. DAC 引脚


<table><tr><td>名称</td><td>描述</td><td>信号类型</td></tr><tr><td><eq>V_{DDA}</eq></td><td>模拟电源</td><td>输入,模拟电源</td></tr><tr><td><eq>V_{SSA}</eq></td><td>模拟电源地</td><td>输入,模拟电源地</td></tr><tr><td><eq>V_{REFP}</eq></td><td>DAC 正参考电压</td><td>输入,模拟正参考电压</td></tr><tr><td>DACy_OUTx</td><td>DAC 模拟输出</td><td>模拟输出信号</td></tr></table>


下表详细列出了 DAC 的触发与输出信号。



表 14-2. DAC 触发与输出


<table><tr><td></td><td colspan="2">DAC0</td><td>DAC1</td></tr><tr><td>通道</td><td>通道0</td><td>通道1</td><td>通道0</td></tr><tr><td>DAC输出I/O</td><td>PA4</td><td>PA5</td><td>PA6</td></tr><tr><td>DAC输出BUFFER功能</td><td>●</td><td>●</td><td>●</td></tr><tr><td>软件触发功能</td><td colspan="3">●</td></tr><tr><td>EXTI触发信号</td><td colspan="3">EXTI_9</td></tr><tr><td>TIMER触发信号</td><td colspan="3">TIMER1_TRGO互联型产品: TIMER2_TRGO 非互联型产品: TIMER7_TRGOTIMER3_TRGOTIMER4_TRGOTIMER5_TRGOTIMER6_TRGOTIMER14_TRGO</td></tr><tr><td>SHRTIMER触发信号</td><td colspan="3">SHRTIMER_DACTRIG0SHRTIMER_DACTRIG1SHRTIMER_DACTRIG2</td></tr></table>


注意：在使能 DAC 模块前，GPIO 口（DAC 输出 I/O）应配置为模拟模式。


## 14.3. 功能描述

## 14.3.1. DAC 使能

将 DAC_CTL0 寄存器中的 DENx 位置 1，可以给 DAC 模块上电，DAC 子模块完全启动需要等待 t<sub>WAKEUP</sub> 时间。

## 14.3.2. DAC 输出缓冲

为了降低输出阻抗，并在没有外部运算放大器的情况下驱动外部负载，每个 DAC 模块内部各集成了一个输出缓冲区。

缺省情况下，输出缓冲区是开启的，可以通过设置 DAC_CTL0 寄存器的 DBOFFx 位来开启或关闭缓冲区。

## 14.3.3. DAC数据配置

对 于 12 位 的 DAC 保 持 数 据 （OUTx_DH）， 可 以 通 过 对 DAC_OUTx_R12DH、DAC_OUTx_L12DH 和 DAC_OUTx_R8DH 中的任意一个寄存器写入数据来配置。当数据被加载到 DAC_OUTx_R8DH 寄存器时，只有 8 位最高有效位是可配置，4 位最低有效位被强制置为 4’b0000。

## 14.3.4. DAC 触发

DAC 可以通过软件或者外部信号的上升沿触发。外部触发可以通过设置 DAC_CTL0 寄存器中DTENx 位来使能。触发源可以通过 DAC_CTL0 寄存器中 DTSELx 位来进行选择，如 14-3.DAC 所示。


表 14-3. DAC 外部触发


<table><tr><td>DTSELx[3:0]</td><td>Trigger Source</td><td>Trigger Type</td></tr><tr><td>4b'0000</td><td>TIMER5_TRGO</td><td rowspan="7">硬件触发</td></tr><tr><td>4b'0001</td><td>互联型产品: TIMER2_TRGO非互联型产品: TIMER7_TRGO</td></tr><tr><td>4b'0010</td><td>TIMER6_TRGO</td></tr><tr><td>4b'0011</td><td>TIMER4_TRGO</td></tr><tr><td>4b'0100</td><td>TIMER1_TRGO</td></tr><tr><td>4b'0101</td><td>TIMER3_TRGO</td></tr><tr><td>4b'0110</td><td>EXTI_9</td></tr><tr><td>4b'0111</td><td>SWTR</td><td>软件触发</td></tr><tr><td>4b'1000</td><td>SHRTIMER_DACTRIG0</td><td rowspan="4">硬件触发</td></tr><tr><td>4b'1001</td><td>SHRTIMER_DACTRIG1</td></tr><tr><td>4b'1010</td><td>SHRTIMER_DACTRIG2</td></tr><tr><td>4b'1011</td><td>TIMER14_TRGO</td></tr><tr><td>4b'1100~1111</td><td>保留</td><td>保留</td></tr></table>


TIMERx_TRGO 信号是由定时器生成的，SHRTIMER_DACTRIGx 信号是由高精度定时器SHRTIMER 提供，而软件触发是通过设置 DAC_SWT 寄存器的 SWTRx 位生成的。


## 14.3.5. DAC 转换

如果使能了外部触发（通过设置 DAC_CTL0 寄存器的 DTENx 位），当已经选择的触发事件发生，DAC 保持数据（OUTx_DH）会被转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。而在外部触发未使能的情况下，DAC 保持数据（OUTx_DH）会被自动转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。

当 DAC 保持数据（OUTx_DH）加载到 DAC_OUTx_DO 寄存器时，经过 t<sub>SETTLING</sub> 时间之后，模拟输出变得有效，t<sub>SETTLING</sub>的值与电源电压和模拟输出负载有关。

## 14.3.6. DAC 噪声波

有两种方式可以将噪声波加载到 DAC 输出数据：LFSR 噪声波和三角波。噪声波模式可以通过 DAC_CTL0 寄存器的 DWMx 位来进行选择。噪声的幅值可以通过配置 DAC_CTL0 寄存器的 DAC 噪声波位宽（DWBWx）位来进行设置。

LFSR 噪声模式：在 DAC 控制逻辑中有一个线性反馈移位寄存器（LFSR）。在此模式下，LFSR的值与 OUTx_DH 值相加后，被写入到 DAC 数据输出寄存器（DAC_OUTx_DO）。当配置的DAC 噪声波位宽小于 12 时，LFSR 的值等于 LFSR 寄存器最低的 DWBWx 位，高位被屏蔽。


图 14-2. DAC LFSR 算法


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/5bcc716262694bd2d4ca7b5ead8ede204f4e15789b9b4160d9128e4eb95ddbb9.jpg)



三角噪声模式：三角波幅值与 OUTx_DH 值相加后，被写入到 DAC 数据输出寄存器（DAC_OUTx_DO）。三角波幅值的最小值为 0，最大值为(2 << DWBWx) - 1。



图 14-3. DAC 三角噪声模式生成的波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/848462dabce87d589f9e9406dc734d8402c7a65bc0b8d6d75bafe9dc0b3d68a7.jpg)


## 14.3.7. DAC输出电压

DAC 引脚上的模拟输出电压取决于下面的等式：

$$
V _ {D A C \_ O U T} = V _ {R E F P} * O U T x \_ D O / 4 0 9 6\tag{144-1}
$$

数字输入被线性地转换成模拟输出电压，输出范围为 0 到 V<sub>REFP</sub>。

## 14.3.8. DMA 请求

在外部触发使能的情况下，通过设置 DAC_CTL0 寄存器的 DDMAENx 位来使能 DMA 请求。当有外部硬件触发的时候（不是软件触发），则产生一个 DMA 请求。

如果在前一个请求响应之前第二个外部触发到达，则不响应新到的触发请求，并且发生欠载错误事件。DAC_STAT0 寄存器中的 DDUDRx 位置 1，如果 DAC_CTL0 寄存器中的 DDUDRIEx位置 1，则会产生中断。

## 14.3.9. DAC 并发转换

当 DAC0 的两个通道同时工作时，为了在特定应用中最大限度利用总线带宽，DAC 的两个通道可以被配置为并发模式。在并发模式中，DAC 的 OUTx_DH 和 OUTx_DO 值将同时被更新。

有 3 个并发寄存器可用于加载 OUTx_DH 的值，分别是：DACC_R8DH、DACC_R12DH 和DACC_L12DH 寄存器，配置其中的任意一个寄存器都可实现同时驱动 DAC 的两个通道。

当使能了外部触发时，DAC 两个通道的 DTENx 位都需要置 1，需要配置 DTSEL0/1 相同来保证同时触发。

当使能了 DMA 功能时，DAC 任一通道的 DDMAENx 位置 1 即可。

噪声模式和噪声位宽可以根据使用情况配置为相同或不同。

## 14.3.10. DAC 输出 FIFO

在数据保持寄存器和输出寄存器之间有一个 4 位深度的数据 FIFO。通过将 DAC_CTL1 寄存器中的 FIFOENx 位置 1，可以使能输出数据 FIFO。

当 FIFOENx 位置 1 时，需要软件设置 DDMAENx=0（DAC_OUTx DMA 模式禁能）和 DTENx=1（DAC_OUTx 触发使能）。

当数据 FIFO 中数据满了时，FIFO 为满载状态，FIFOFx 标志位会置 1；当数据 FIFO 中数据为空时，FIFO 为空载状态，FIFOEx 标志位会置 1。

当数据 FIFO 中数据已满，但没有触发到来时，过载标志位 FIFOOVRx 置 1；当数据 FIFO 为空，但有触发到来时，欠载标志位 FIFOUDRx 置 1。如果设置了相应的中断使能位，则在发生过载或欠载时将产生中断。

通过读取 DAC_STAT1 寄存器内容，可以获取数据 FIFO 的状态（满载、空载、过载和欠载）。
