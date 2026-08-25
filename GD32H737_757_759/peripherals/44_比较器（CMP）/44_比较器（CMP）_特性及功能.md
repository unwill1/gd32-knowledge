# 44. 比较器（CMP）

# 44.1. 简介

通用比较器可独立工作，其输出端可用于 I / O 口，也可和定时器结合使用。

比较器可通过模拟信号将 MCU 从低功耗模式中唤醒，在一定的条件下，可将模拟信号作为TIMER 的触发源，结合 DAC 和 TIMER 的 PWM 输出，可以实现电流控制。

# 44.2. 主要特征

轨对轨比较器；

迟滞可配置；

速度、功耗可配置；

每个比较器可配置以下模拟信号作为输入源：

DAC 输出；

多路复用 I / O 引脚；

0.25、0.5、0.75、1 倍的内部参考电压；

比较器输出消隐；

窗口比较器；

输出到 I / O 口；

作为触发源输出到定时器；

输出到 EXTI；

输出到 NVIC；

输出到 TRIGSEL。

# 44.3. 功能描述

比较器的框图展示如下：


图 44-1.比较器框图


![image](images/f621763b96cb.jpg)



注意：VREFINT 是 1.2V。


# 44.3.1. 比较器时钟

比较器与 APB 总线连接，时钟与 PCLK 同步。

# 44.3.2. 比较器的 I/O配置

在被选为比较器输入端之前，相应管脚必须配置为模拟模式。

比较器的输出可同时实现内部和外部输出。

参考 Datasheet 的引脚定义，比较器输出可以通过 GPIO 的备用功能连接到对应的 I / O 口。

比较器输出内部连接到定时器，他们的连接关系如下：

CMP输出连接到定时器输入通道；\
CMP输出连接到定时器中止功能。

为了在深度睡眠模式下工作，比较器端口的极性选择和输出重定向不会因为 PCLK 关闭。

44-1. CMP 详细描述了 CMP 的输入和输出。


表 44-1. CMP 的输入和输出总结


<table><tr><td></td><td>CMP0</td><td>CMP1</td></tr><tr><td rowspan="2">CMP 同相输入连接到I/O</td><td>PB0</td><td>PE9</td></tr><tr><td>PB2</td><td>PE11</td></tr><tr><td rowspan="2">CMP 反相输入连接到I/O</td><td>PB1</td><td>PE10</td></tr><tr><td>PC4</td><td>PE7</td></tr><tr><td>CMP 反相输入连接到内部信号</td><td><eq>V_{REFINT}/4</eq>,<eq>V_{REFINT}/2</eq>,<eq>V_{REFINT}*3/4</eq>,<eq>V_{REFINT}</eq>,DAC0_OUT0,DAC0_OUT1</td><td><eq>V_{REFINT}/4</eq>,<eq>V_{REFINT}/2</eq>,<eq>V_{REFINT}*3/4</eq>,<eq>V_{REFINT}</eq>,DAC0_OUT0,DAC0_OUT1</td></tr><tr><td>CMP 输出连接到 I/O</td><td>PC5(AF13)PE12(AF13)</td><td>PE8(AF13)PE13(AF13)</td></tr><tr><td>CMP 输出连接到 EXTI</td><td colspan="2">●</td></tr><tr><td>CMP 输出连接到TRIGSEL</td><td colspan="2">●</td></tr><tr><td>CMP 输出连接到 NVIC</td><td colspan="2">●</td></tr><tr><td>CMP 输出连接到内部信号</td><td colspan="2">●</td></tr><tr><td>CMP 输出连接到TIMER break</td><td colspan="2">●</td></tr><tr><td>CMP_MUX_OUT(由 AFSE[x]控制)</td><td colspan="2">PA6(AF10)PA8(AF12)PB12(AF13)PE6(AF11)PE15(AF13)PG2(AF11)PG3(AF11)PG4(AF11)PK0(AF11)PK1(AF11)PK2(AF10)</td></tr></table>

# 注意：

1. 有关CMP输出连接到内部信号的详细信息，请参阅系统配置寄存器；

2. 有关CMP输出连接到TIMER break的详细信息，请参阅TIMER模块；

# 44.3.3. 比较器供电模式

对于给定的程序，在比较器功耗和传输迟滞之间存在着权衡，可通过寄存器 CMPx_CS 的位CMPxM [1:0]的配置进行调整。当 CMPxM [1:0]为 2’b 00 时，比较器以运行速度最快和功耗最大模式工作，但当 CMPxM[1:0]位 2’b 11 时，比较器以运行速度最慢和功耗最小的模式工作。

# 44.3.4. 比较器窗口模式

如果寄存器 CMP1_CS 的 WNDEN 位被置位，比较器的窗口模式被使能，比较器 1 的同相输入端即与比较器 0 的同相输入端相连。如果 CMP0 和 CMP1 的反相输入端连接不同的内部电压，可以通过分析 CMP0 和 CMP1 的输出结果监测输入电压的范围，该范围的上下限由反相输入端所连接的内部电压值决定。

# 44.3.5. 比较器迟滞

为了避免噪声信号所引起的假输出，电路设计了可编程的迟滞功能，通过配置控制状态寄存器来控制迟滞电压值。该功能可以在无需要时关闭。


图 44-2. 比较器迟滞


![image](images/dc551dffff1f.jpg)


# 44.3.6. 比较器寄存器写保护

比较器的控制状态寄存器（CMPx_CS）和外部选择寄存器（CMP_SR）可通过设置 CMPxLK位为 1 来进行写保护，CMPx_CS 寄存器，包含 CMPxLK位，就会变为只读位，只有在 MCU复位时才可以复位。

# 44.3.7. 比较器输出消隐

比较器输出消隐功能可以避免比较器输入信号中的短脉冲对输出信号的干扰。如果 CMPx_CS寄存器中的 CMPxBLK[2:0]位域设置为有效值，则比较器最终输出的信号由所选消隐信号的互补信号和比较器的原始输出进行“与”运算获得。


44-3. 显示了比较器的输出消隐功能。



图 44-3. 比较器的输出消隐


![image](images/96bb23390553.jpg)


# 44.3.8. 电压定标器功能

电压定标器功能可为 CMP 输入提供可选择的 1/4、1/2、3/4 参考电压。它由位于 CMPx 控制状态寄存器中的 CMPxSEN 位和 CMPxBEN 位控制，CMPxSEN 位和 CMPxBEN 位分别用于使能 VREFINT电压输出和分压电路，以产生所选择的电压。

# 44.3.9. 比较器中断

CMP输出连接到 EXTI，EXTI 线对每个 CMP都是独占的。通过这个功能，可以产生中断或者事件，用于退出省电模式。

CMP还可以输出到 NVIC 产生中断。它是一个序列逻辑信号，因此需要 PCLK。
