## 18.5. 基本定时器（TIMERx，x=5，6）

## 18.5. 1. 简介

基本定时器（TIMER5，6）包含一个无符号 16 位计数器。基本定时器可以配置产生 DMA 请求，TRGO 触发连接到 DAC。

## 18.5.2. 主要特征

◼ 计数器宽度：16位；

◼ 定时器时钟源只有内部时钟；

◼ 计数模式：向上计数；

◼ 可编程的预分频器：16位，运行时可以被改变；

◼ 自动重装载功能；

◼ 中断输出和DMA请求：更新事件。

## 18.5.3. 结构框图

18-91. 提供了基本定时器内部配置的细节。


图 18-91. 基本定时器结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/d05fd9d1cb39091fff33b465f43d92ec094238648d4602ad7bccadda1591317c.jpg)


## 18.5.4. 功能说明

## 时钟源配置

基本定时器可以是内部时钟源 CK_TIMER 驱动。

基本定时器仅有一个时钟源 CK_TIMER，用来驱动计数器预分频器。当 CEN 置位，CK_TIMER经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。


图 18-92. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/f32e3302257e90b4dabac515d96446fc336b9dd81f68d4cab2a8d6f7d4a3ab83.jpg)


## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-93. 当 PSC 数值从 0 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/d0cbae9399bb4f6295a0cf4a23587796c058e9af7cbfaf8eb53254c9a359d0a6.jpg)


## 计数器向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器（计数器自动重载寄存器，预分频寄存器）都将被更新。

18-94. PSC=0/2 和 18-95.TIMERx_CAR 给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 18-94. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/a4468a91c457e841a246b9ef3d6b3fb2af63dc0e28208d86c394eb164f33c805.jpg)



图 18-95. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/426f05e466aa0ee29b8f0dcaeee146d23715a92ac8d225704f87dcab67a194c0.jpg)


## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，则使能单脉冲模式。当SPM置1，计数器在下次更新事件到来后清零并停止计数。

一旦设置定时器运行在单脉冲模式下，需要设置TIMERx_CTL0寄存器的定时器使能位CEN=1来使能计数器，此后CEN位一直保持为1直到更新事件发生或者CEN位被软件写0。如果CEN位被软件清0，计数器停止工作，计数值被保持。

## 定时器调试模式

当 Cortex<sup>®</sup>-M23 内核停止，DBG_CTL0 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。
