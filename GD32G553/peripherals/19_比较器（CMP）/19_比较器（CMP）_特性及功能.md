## 19. 比较器（CMP）

## 19.1. 简介

通用比较器可独立工作，其输出端可用于 I / O 口，也可和定时器结合使用。

比较器可通过模拟信号将MCU从低功耗模式中唤醒，在一定的条件下，可将模拟信号作为TIMER的触发源，结合 DAC 和 TIMER 的 PWM 输出，可以实现电流控制。

## 19.2. 主要特征

 轨对轨比较器；

 迟滞可配置；

 速度、功耗可配置；

 每个比较器可配置以下模拟信号作为输入源：

DAC 输出；

多路复用 I / O 引脚；

0.25、0.5、0.75、1 倍的内部参考电压；

 比较器输出消隐；

 输出到 I / O 口；

 作为触发源输出到定时器；

 输出到 EXTI；

 输出到 NVIC；

 输出到 TRIGSEL；

 系统复位时输出保持。

## 19.3. 功能描述

比较器的框图展示如下：


图 19-1.比较器框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/b6f7993bd5e7d55f8b8de4d76b84773b4dbce9547eb27807b54749d1694803ec.jpg)


注意：

1) V<sub>REFINT</sub> 是 1.2V。

2) CMPx(x=1,2..7)和 CMP0 结构相似，CMPxPSEL、CMPxBLK、CMPxMSEL 等参考 19-1.CMP 和寄存器。

## 19.3.1. 比较器时钟

比较器与 APB 总线连接，时钟与 PCLK 同步。

## 19.3.2. 比较器的 I/O 配置

在被选为比较器输入端之前，相应管脚必须配置为模拟模式。

比较器的输出可同时实现内部和外部输出。

参考 Datasheet 的引脚定义，比较器输出可以通过 GPIO 的备用功能连接到对应的 I / O 口。

比较器输出内部连接到定时器，他们的连接关系如下：

 CMP输出连接到定时器中止功能（通过 TRIGSEL）。

为了在深度睡眠模式下工作，比较器端口的极性选择和输出重定向不会因为 PCLK 关闭。

19-1. CMP 详细描述了 CMP 的输入和输出。.


表 19-1. CMP 的输入和输出总结


<table><tr><td></td><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td><td>CMP4</td><td>CMP5</td><td>CMP6</td><td>CMP7</td></tr><tr><td>CMP 同相</td><td>PA1</td><td>PA7</td><td>PA0</td><td>PB0</td><td>PB13</td><td>PB11</td><td>PB14</td><td>PC2</td></tr><tr><td>输入连接到I/O</td><td>PB1</td><td>PA3</td><td>PC1</td><td>PE7</td><td>PD12</td><td>PD11</td><td>PD14</td><td>PE9</td></tr><tr><td>CMP反相输入连接到I/O</td><td>PA4PA0</td><td>PA5PA2</td><td>PF1PC0</td><td>PE8PB2</td><td>PB10PD13</td><td>PD10PB15</td><td>PD15PB12</td><td>PD8PD9</td></tr><tr><td>CMP反相输入连接到内部信号</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC2_OUT0DAC0_OUT0</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC2_OUT1DAC0_OUT1</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC2_OUT0DAC0_OUT0</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC2_OUT1DAC0_OUT0</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC3_OUT0DAC0_OUT1</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC3_OUT1DAC1_OUT0</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC3_OUT0DAC1_OUT0</td><td><eq>V_{REFINT}/4</eq>, <eq>V_{REFINT}/2</eq>, <eq>V_{REFINT} * 3/4</eq>, <eq>V_{REFINT}</eq>, DAC3_OUT1DAC1_OUT1</td></tr><tr><td>CMP输出连接到I/O</td><td>PA0PA6PA11PB8PF4</td><td>PA2PA7PA12PB9</td><td>PB7PB15PC2</td><td>PB1PB6PB14</td><td>PA9PC7</td><td>PC6PA10</td><td>PC8PA8</td><td>PA13PA14</td></tr><tr><td>CMP输出连接到EXTI</td><td colspan="8">●</td></tr><tr><td>CMP输出连接到TRIGSEL</td><td colspan="8">●</td></tr><tr><td>CMP输出连接到NVIC</td><td colspan="8">●</td></tr><tr><td>CMP输出连接到内部信号</td><td colspan="8">TIMER0, TIMER1, TIMER2, TIMER3, TIMER4, TIMER7, TIMER19, LPTIMER, HRTIMER</td></tr><tr><td rowspan="2">CMP输出连接到break信号</td><td colspan="8">BREAK0(TIMER0, TIMER7, TIMER14, TIMER15, TIMER16, TIMER19)</td></tr><tr><td colspan="8">BREAK1(TIMER0, TIMER7, TIMER19)</td></tr></table>

## 19.3.3. 比较器迟滞

为了避免噪声信号所引起的假输出，电路设计了可编程的迟滞功能，通过配置控制状态寄存器来控制迟滞电压值。该功能可以在无需要时关闭。


图 19-2. 比较器迟滞


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/2e8b42009f4d3e6caedbd487c508f173270c357dda8675dd998df4b2d330c9bb.jpg)


## 19.3.4. 比较器寄存器写保护

比较器的控制状态寄存器（CMPx_CS）可通过设置 CMPxLK 位为 1 来进行写保护，CMPx_CS 寄存器，包含 CMPxLK 位，就会变为只读位，只有在 MCU 复位时才可以复位。

## 19.3.5. 比较器输出消隐

比较器输出消隐功能可以避免比较器输入信号中的短脉冲对输出信号的干扰。如果 CMPx_CS 寄存器中的 CMPxBLK[2:0]位域设置为有效值，则比较器最终输出的信号由所选消隐信号的互补信号和比较器的原始输出进行“与”运算获得。

19-3. 显示了比较器的输出消隐功能。


图 19-3. 比较器的输出消隐


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/6d7b60a559aaa363dd7c8554e4d9591382c29ab2ee53f0a20eb55c469459b2c0.jpg)


## 19.3.6. 电压定标器功能

电压定标器功能可为 CMP 输入提供可选择的 1 / 4、1 / 2、3 / 4 参考电压。它由位于 CMPx 控制状态寄存器中的 CMPxSEN 位和 CMPxBEN 位控制，CMPxSEN 位和 CMPxBEN 位分别用于使能 V<sub>REFINT</sub>电压输出和分压电路，以产生所选择的电压。

## 19.3.7. 比较器中断

CMP 输出连接到 EXTI，EXTI 线对每个 CMP 都是独占的。通过这个功能，可以产生中断或者事件，用于退出省电模式。

CMP还可以输出到 NVIC 产生中断。它是一个序列逻辑信号，因此需要 PCLK。

## 19.3.8. 复位保持功能

复位保持功能可以通过在 CMPx_CS 寄存器中设置 CMPxRSTMD 位来启用。除了上电复位外，输出通道将在所有复位过程中保持。
