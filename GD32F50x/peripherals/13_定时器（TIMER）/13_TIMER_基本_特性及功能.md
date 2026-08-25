## 13.4. 基本定时器（TIMERx, x=5,6）

## 13.4.1. 简介

基本定时器（TIMER5/6）包含一个无符号 16 位计数器。可以被用作通用定时器和为 DAC（数字到模拟转换器）提供时钟。基本定时器可以配置产生 DMA请求，TRGO 触发连接到 DAC。

## 13.4.2. 主要特性

 计数器宽度：16位（TIMER5/6）

 时钟源只有内部时钟

 计数模式：向上计数

 可编程的预分频器：16位，运行时可以被改变

 自动重装载功能.

 中断输出和DMA请求：更新事件

## 13.4.3. 结构框图

13-103. 提供了基本定时器内部配置的细节。


图 13-103. 基本定时器结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/97bf94ff64be4e9f7832fb8cc6bbd47c35b6fbb74456a978a9ece06732728353.jpg)


## 13.4.4. 功能描述

## 时钟源选择

基本定时器只能由内部时钟源 CK_TIMER 驱动（来自 RCU 模块）。

TIMER_CK 用来驱动计数器预分频器。当 CEN 置位，TIMER_CK 经过预分频器（预分频值由TIMERx_PSC 寄存器确定）产生 PSC_CLK。


图 13-104. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/350692f805de208909f05b63ab4848bbd1d7daf1cc0384d22c0b50146833183c.jpg)


## 预分频

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 13-105. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/188e59c43a7207da25062d5eccc72a44c74a7975c83413f2d0e443027c7ad64e.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

下面这些图给出了一些例子，当 TIMERx_CAR=0x99（TIMERx, x=5,6）时，计数器在不同预分频因子下的行为。


图 13-106. 向上计数时序图，PSC=0/2（TIMERx, x=5,6）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/3a7f40d5fd5f60d6e8dfec32715e70f9c3ea22adee079a934c315a3a2abd4d72.jpg)



图 13-107. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值（TIMERx, x=5,6）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/8a2cef8fc9707478fe85190c55af7d34469e1c7b3cc03d97cdea9ff5d5913cd7.jpg)


## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL0 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

