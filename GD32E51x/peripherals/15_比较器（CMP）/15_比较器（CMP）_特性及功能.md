## 15. 比较器（CMP）

## 15.1. 简介

通用比较器可独立工作，其输出端可用于 I / O 口，也可和定时器结合使用。

比较器在一定的条件下，可将模拟信号作为 TIMER 的触发源。

## 15.2. 主要特征

 轨对轨比较器；

 每个比较器可配置以下模拟信号作为输入源；

– DAC 输出；

– 多路复用 I / O 引脚；

0.25、0.5、0.75、1 倍的内部参考电压；

 比较器输出消隐；

 输出到 I / O 口；

 作为触发源输出到定时器。

## 15.3. 功能描述

比较器的框图展示如下：


图 15-1. 比较器框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/28e11442ade680e182d6b014755986d15874eedabf058dbae24d608cb2209654.jpg)



注意：V<sub>REFINT</sub> 是 1.2V.


## 15.3.1. 比较器时钟

比较器与 APB 总线连接，时钟与 PCLK 同步。

## 15.3.2. 比较器的 I / O配置

在被选为比较器输入端之前，相关引脚必须配置为模拟模式。

比较器的输出可同时实现内部和外部输出。

参考 Datasheet 的引脚定义，比较器输出可以通过 GPIO 的备用功能连接到对应的 I / O 口。

比较器输出内部连接到定时器，他们的连接关系如下：

 CMP输出连接到定时器输入通道。

 CMP输出连接到定时器中止功能。

15-1. CMP 详细描述了 CMP的输入和输出。


表 15-1. CMP 的输入和输出总结


<table><tr><td></td><td>CMP1</td><td>CMP3</td><td>CMP5</td></tr><tr><td>CMP 同相输入连接到I/O</td><td>PA7</td><td>PB0</td><td>PB11</td></tr><tr><td rowspan="3">CMP 反相输入连接到I/O</td><td>PA2</td><td>PA4</td><td>PA4</td></tr><tr><td>PA4</td><td>PA5</td><td>PA5</td></tr><tr><td>PA5</td><td>PB2</td><td>PB15</td></tr><tr><td rowspan="7">CMP 反相输入连接到内部信号</td><td><eq>V_{REFINT} / 4</eq></td><td><eq>V_{REFINT} / 4</eq></td><td><eq>V_{REFINT} / 4</eq></td></tr><tr><td><eq>V_{REFINT} / 2</eq></td><td><eq>V_{REFINT} / 2</eq></td><td><eq>V_{REFINT} / 2</eq></td></tr><tr><td><eq>V_{REFINT} * 3 / 4</eq></td><td><eq>V_{REFINT} * 3 / 4</eq></td><td><eq>V_{REFINT} * 3 / 4</eq></td></tr><tr><td><eq>V_{REFINT}</eq></td><td><eq>V_{REFINT}</eq></td><td><eq>V_{REFINT}</eq></td></tr><tr><td>DAC0_OUT0</td><td>DAC0_OUT0</td><td>DAC0_OUT0</td></tr><tr><td>DAC0_OUT1</td><td>DAC0_OUT1</td><td>DAC0_OUT1</td></tr><tr><td>DAC1_OUT0</td><td>DAC1_OUT0</td><td>DAC1_OUT0</td></tr><tr><td rowspan="5">CMP 输出连接到I/O</td><td>PA2</td><td></td><td>PA10</td></tr><tr><td>PA12</td><td>PB1</td><td>PC6</td></tr><tr><td>PB9</td><td>PE9</td><td>PE10</td></tr><tr><td>PE8</td><td>PE12</td><td>PE11</td></tr><tr><td>PE13</td><td></td><td></td></tr><tr><td rowspan="5">CMP 输出连接到内部信号</td><td>TIMER0_CH0</td><td>TIMER2_CH2</td><td>TIMER1_CH1</td></tr><tr><td>TIMER1_CH3</td><td>SHRTIMER_EXEV1</td><td>SHRTIMER_EXEV2</td></tr><tr><td>TIMER2_CH0</td><td>SHRTIMER_EXEV6</td><td>SHRTIMER_EXEV7</td></tr><tr><td>SHRTIMER_EXEV0</td><td>TIMER14_CH1</td><td>TIMER15_CH0</td></tr><tr><td>SHRTIMER_EXEV5</td><td></td><td></td></tr><tr><td>CMP 输出(电机控制保护)</td><td colspan="3">TIMER0 BRKIN</td></tr></table>


注意：CMP1/3/5 的输出直接连接到 SHRTIMER 外设。


## 15.3.3. 比较器寄存器写保护

比较器的控制状态寄存器（CMPx_CS）可通过设置 CMPxLK位为 1 来进行写保护，CMPx_CS寄存器，包含 CMPxLK 位，就会变为只读位，只有在 MCU 复位时才可以复位。

## 15.3.4. 比较器输出消隐

比较器输出消隐功能可以避免比较器输入信号中的短脉冲对输出信号的干扰。如果 CMPx_CS寄存器中的 CMPxBLK[2:0]位域设置为有效值，则比较器最终输出的信号由所选消隐信号的互补信号和比较器的原始输出进行“与”运算获得。

15-2. 显示了比较器的输出消隐功能。


图 15-2. 比较器的输出消隐


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/6a1ebcc48e76610ba33a4fe7ace31aa5efc8fcde378cd44548e6f2cd00ffbe88.jpg)

