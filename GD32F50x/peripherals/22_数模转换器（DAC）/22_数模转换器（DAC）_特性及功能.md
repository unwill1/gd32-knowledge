## 22. 数模转换器（DAC）

## 22.1. 简介

数字/模拟转换器可以将 12 位的数字数据转换为外部引脚上的电压输出。数据可以采用 8 位或 12位模式，左对齐或右对齐模式。当使能了外部触发，DMA可被用于更新输入端数字数据。

在输出电压时，可以利用 DAC 输出缓冲区来获得更高的驱动能力。

## 22.2. 主要特征

DAC 的主要特征如下：

 8 位或 12 位分辨率；

 数据左对齐或右对齐；

 DMA功能与欠载检测；

 同步更新转换；

 外部事件触发转换；

 可配置的内部缓冲区；

 输入参考电压 V<sub>REFP</sub>；

 噪声波生成（LSFR 噪声模式和三角噪声模式）；

22-1. DAC 为 DAC 的结构框图， 22-1. DAC 给出了引脚描述。


图 22-1. DAC 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/86f3c14c07a851e7055271e0626cd63ec66165dcb7644f1fbd612332f7be8cbb.jpg)



表 22-1. DAC 引脚


<table><tr><td>名称</td><td>描述</td><td>信号类型</td></tr><tr><td><eq>V_{DDA}</eq></td><td>模拟电源</td><td>输入,模拟电源</td></tr><tr><td><eq>V_{SSA}</eq></td><td>模拟电源地</td><td>输入,模拟电源地</td></tr><tr><td><eq>V_{REFP}</eq></td><td>DAC 正参考电压</td><td>输入,模拟正参考电压</td></tr><tr><td>DACy_OUTx</td><td>DAC 模拟输出</td><td>模拟输出信号</td></tr></table>


下表详细列出了 DAC 的触发与输出信号。



表 22-2. DAC 触发与输出


<table><tr><td></td><td>DAC0</td></tr><tr><td>通道</td><td>通道 0</td></tr><tr><td>DAC 输出 I/O</td><td>PA4 / PA5</td></tr><tr><td>DAC 输出 BUFFER 功能</td><td>●</td></tr><tr><td>软件触发功能</td><td>●</td></tr><tr><td>TRIGSEL 触发信号</td><td>●</td></tr></table>


注意：在使能 DAC 模块前，GPIO 口（DAC 输出 I/O）应配置为模拟模式。


## 22.3. 功能描述

## 22.3.1. DAC 使能

将 DAC_CTL0 寄存器中的 DENx 位置 1，可以给 DAC 模块上电，DAC 子模块完全启动需要等待t<sub>WAKEUP</sub> 时间。

## 22.3.2. DAC输出缓冲

为了降低输出阻抗，并在没有外部运算放大器的情况下驱动外部负载，每个 DAC 模块内部各集成了一个输出缓冲区。

默认情况下，输出缓冲区是开启的，可以通过设置 DAC_CTL0 寄存器的 DBOFFx 位来开启或关闭缓冲区。

## 22.3.3. DAC数据配置

对于 12 位的 DAC 保持数据（OUTx_DH），可以通过对 DAC_OUTx_R12DH、DAC_OUTx_L12DH和 DAC_OUTx_R8DH 中的任意一个寄存器写入数据来配置。当数据被加载到 DAC_OUTx_R8DH寄存器时，只有 8 位最高有效位是可配置，4 位最低有效位被强制置为 4’b0000。

## 22.3.4. DAC 触发

DAC 可以通过软件或者外部信号的上升沿触发。外部触发可以通过设置 DAC_CTL0 寄存器中DTENx 位来使能。触发源可以通过 DAC_CTL0 寄存器中 DTSELx 位来进行选择，如 22-3. DAC外部触发所示。


表 22-3. DAC 外部触发


<table><tr><td>DTSELx[1:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>2b&#x27;00</td><td>TRIGSEL</td><td>硬件触发</td></tr><tr><td>2b&#x27;01 /2b&#x27;10</td><td>保留</td><td>保留</td></tr><tr><td>2b&#x27;11</td><td>SWTR</td><td>软件触发</td></tr></table>

外部触发器由 TRIGSEL 生成，软件触发是通过设置 DAC_SWT 寄存器的 SWTRx 位生成的。注意：只能在 dac 模块使能之后（DEN0=1），再去触发 DAC 模块。

## 22.3.5. DAC 转换

如果使能了外部触发（通过设置 DAC_CTL0 寄存器的 DTENx 位），当已经选择的触发事件发生，DAC 保持数据（OUTx_DH）会被转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。而在外部触发未使能的情况下，DAC 保持数据（OUTx_DH）会被自动转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。

当 DAC 保持数据（OUTx_DH）加载到 DAC_OUTx_DO 寄存器时，经过 t<sub>SETTLING</sub>时间之后，模拟输出变得有效，t<sub>SETTLING</sub>的值与电源电压和模拟输出负载有关。

## 22.3.6. DAC 噪声波

有两种方式可以将噪声波加载到 DAC 输出数据：LFSR 噪声波和三角波。噪声波模式可以通过DAC_CTL0寄存器的 DWMx 位来进行选择。噪声的幅值可以通过配置 DAC_CTL0 寄存器的 DAC噪声波位宽（DWBWx）位来进行设置。

LFSR 噪声模式：在 DAC 控制逻辑中有一个线性反馈移位寄存器（LFSR）。在此模式下，LFSR的值与 OUTx_DH 值相加后，被写入到 DAC 数据输出寄存器（DAC_OUTx_DO）。当配置的 DAC噪声波位宽小于 12 时，LFSR 的值等于 LFSR 寄存器最低的 DWBWx 位，高位被屏蔽。


图 22-2. DAC LFSR 算法


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/4751bd0206d0546ddbc2e77c672f486bb0ec4378a40399cdeb7c0f4c5f484918.jpg)



三角 噪声 模 式：三角 波 幅值与 OUTx_DH 值相 加后 ，被 写 入到 DAC 数据 输出 寄 存器（DAC_OUTx_DO）。三角波幅值的最小值为 0，最大值为(2 << DWBWx) - 1。



图 22-3. DAC 三角噪声模式生成的波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/55cc998db2b832e3b7b83d5b1ec0f907e016c1869b9895bb2c6c2bb65824e5fd.jpg)


## 22.3.7. DAC输出电压

DAC 引脚上的模拟输出电压取决于下面的等式：

$$
V _ {D A C \_ O U T} = V _ {R E F P} * O U T x \_ D O / 4 0 9 6\tag{22-1}
$$

数字输入被线性地转换成模拟输出电压，输出范围为 0 到 $V _ { R E F F }$ <sub>P</sub>。

## 22.3.8. DMA 请求

在外部触发使能的情况下，通过设置 DAC_CTL0 寄存器的 DDMAENx 位来使能 DMA请求。当有外部硬件触发的时候（不是软件触发），则产生一个 DMA请求。
