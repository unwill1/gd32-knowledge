## 18.5. 通用定时器 L3（TIMERx,x=14）

## 18.5.1. 简介

通用定时器 L3（TIMER14）是两通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。通用定时器 L3 含有一个 16 位无符号计数器。

通用定时器 L3 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器

通用定时器 L3 包含了一个死区时间插入模块，非常适合电机控制。

定时器和定时器之间是相互独立，但是他们可以被同步在一起形成一个更大的定时器，这些定时器的计数器一致地增加。

## 18.5.2. 主要特性

 总通道数：2；

 计数器宽度：16位；

 时钟源可选：内部时钟，内部触发，外部输入；

 计数模式：向上计数；

 可编程的预分频器：16位，运行时可以被改变；

 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

 可编程的死区时间；

 自动重装载功能；

 可编程的计数器重复功能；

 中止输入功能；

 中断输出和DMA请求：更新事件，比较/捕获事件和中止事件；

 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

 定时器主-从管理。

## 18.5.3. 结构框图

18-68. L3 提供了通用定时器 L3 的内部配置细节。


图 18-68. 通用定时器 L3结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/11b6be6a910e5f95ac7e0037263492bd6394bcc3b9730133ffd09a96af739ebf.jpg)


## 18.5.4. 功能描述

## 时钟源配置

通用定时器 L0 可以是内部时钟源 CK_TIMER，或者是由 SMC（TIMERx_SMCFG 寄存器位[2:0]）位确定的时钟源。

 SMC[2:0]=3’b000，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 SMC[2:0]=3’b000，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

如果将 TIMERx_SMCFG 寄存器的 SMC[2:0]设置为 0x1、0x2、0x3 和 0x7，预分频器被其他时钟源(由 TIMERx_SMCFG 寄存器的 TRGS[2:0]区域选择)驱动，在下文说明。当 SMC 位被设置为 0x4、0x5 和 0x6，计数器预分频器时钟源由内部时钟 CK_TIMER 驱动。


图 18-69. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/5b9be1d9be40d14d4263aa8b82da5c8c5babf62b5fee62d6b46994debbeeabbd.jpg)



 SMC[2:0]=3’b111（外部时钟模式0），定时器选择外部输入引脚作为时钟源。


计数器预分频器可以在 TIMERx_CH0/ TIMERx_CH1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 SMC[2:0]为 0x7 同时设置 TRGS[2:0]为 0x4，0x5 或 0x6 来选择。CIx 是TIMERx_CIx 通过数字滤波器采样后的信号。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置SMC[2:0]为 0x7 同时设置 TRGS[2:0]为 0x0，0x1，0x2 或者 0x3。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK)频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-70. 当 PSC 数值从 0 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/40fae28f602dfc77e8de0bd72a428a64617b0bc2633a7d525da885014dba568f.jpg)


## 计数器向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器(重复计数寄存器，计数器自动重载寄存器，预分频寄存器)都将被更新。

18-71.        PSC=0/2 和 18-72.TIMERx_CAR 给出了一些例子，当TIMERx_CAR=0x99时，计数器在不同预分频因子下的行为。


图 18-71. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/f12bc0b45a1b1a0f0d6fd0d1608f416672052c6ed4755f3e44bf9f5713b055aa.jpg)



图 18-72. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/feb2b3236e876ba09736ea98033e2347fb5c6515b271281b9b0d23f890e265b1.jpg)


## 更新事件（来自上溢/下溢）频率配置

重复计数器是用来在（N+1）个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP 寄存器的 CREP 位的值。向上计数模式下，重复计数器在每次计数器上溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP 寄存器中 CREP 的值并产生一个更新事件。


图 18-73. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/32030b6d7b28fd4fa95aeeb11cd41b99abb19902fe8d6c90ccc6251e1d1d14c0.jpg)


## 输入捕获和输出比较通道

通用定时器 L3 拥有两个独立的通道用于捕获输入或比较输出。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

##  通道输入捕获功能

通道输入捕获功能允许通道测量一个波形的时序，频率，周期和占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 CHxIF 位被置 1，若 CHxIE=1则产生通道中断。


图 18-74. 通道输入捕获原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/4ebaf25d6d2aaa35a71d7dfe138f4dfdbfb11221edebfd36ef3c449151c922a9.jpg)


通道输入信号 CIx 来源于 TIMERx_CHx 信号。通道输入信号 CIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP选择使用上升沿或者下降沿。通过配置 CHxMS，还可以选择其他通道的输入信号或内部触发信号作为捕获信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0 寄存器中 CHxCAPFLT）：

根据输入信号和请求信号的质量，配置相应的 CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2 寄存器中 CHxP/CHxNP）：

配置 CHxP/CHxNP 选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0 寄存器中 CHxMS）：

一旦通过配置 CHxMS 选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x0），而且TIMERx_CHxCV 寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN 寄存器中 CHxIE 和 CHxDEN）：

使能相应中断，可以获得中断和 DMA请求。

第五步：捕获使能（TIMERx_CHCTL2 寄存器中 CHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV 被设置成当前计数器的值，CHxIF 为置 1。如果 CHxIF 位已经为 1，则 CHxOF 位置 1。根据 TIMERx_DMAINTEN 寄存器中 CHxIE 和CHxDEN 的配置，来确定是否提出相应的中断和 DMA 请求。

直接产生：软件设置 CHxG 位，会直接产生中断和 DMA 请求。

通道输入捕获功能也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0，同时设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0，同时设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV寄存器测量PWM的周期值，TIMERx_CH1CV寄存器测量PWM占空比值。

 通道输出比较模式


图 18-75. 通道输出比较原理（带有互补输出的通道，x=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/c3fd6433b3d8e2b519c0b073ee52751dc1475f2c5664b5682718e24cde7ebd35.jpg)



图 18-76. 通道输出比较原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/64b376780c8dc2366d43fbba299612e4f4fc8c983448d70918dd76fe6b150a2b.jpg)


图18-75.通道输出比较原理（带有互补输出的通道，x=0）和图18-76.通道输出比较原理分别给出了输出比较的逻辑电路。通道输出信号CHx_O/CHx_ON与OxCPRE信号（详情请见）的关系描述如下：OxCPRE信号高电平有效，CHx_O/CHx_ON的输出情况与OxCPRE信号，CHxP/CHxNP位和CHxE/CHxNE位有关（具体情况请见TIMERx_CHCTL2寄存器中的描述）。例如：

1）当设置 CHxP=0（CHx_O 高电平有效，与 OxCPRE 输出极性相同）、CHxE=1（CHx_O 输出使能）时：

若 OxCPRE 输出有效（高）电平，则 CHx_O 输出有效（高）电平；

若 OxCPRE 输出无效（低）电平，则 CHx_O 输出无效（低）电平。

2）当设置 CHxNP=1（CHx_ON 低电平有效，与 OxCPRE 输出极性相反）、CHxNE=1（CHx_ON输出使能）时：

若 OxCPRE 输出有效（高）电平，则 CHx_ON 输出有效（低）电平；

若 OxCPRE 输出无效（低）电平，则 CHx_ON 输出无效（高）电平。

当 CH0_O 和 CH0_ON 同时输出时，CH0_O 和 CH0_ON 的具体输出情况还与 TIMERx_CCHP

寄存器中的相关位（ROS、IOS、POE 和 DTCFG 等位）有关。详情请见。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的TIMERx_CHxCV寄存器与计数器的值匹配时，根据CHxCOMCTL的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 TIMERx_CHxCV 寄存器的值匹配时，CHxIF 位被置 1，如果 CHxIE = 1 则会产生中断，如果 CxCDE=1 则会产生DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

 设置CHxCOMSEN位来配置输出比较影子寄存器；

 设置CHxCOMCTL位来配置输出模式（置高电平/置低电平/翻转）；

 设置CHxP/CHxNP位来选择有效电平的极性；

 设置CHxEN使能输出。

第三步：通过 CHxIE/CxCDE 位配置中断/DMA 请求使能。

第四步：通过 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器配置输出比较时基：

TIMERx_CHxCV 可以在运行时根据你所期望的波形而改变。

第五步：设置 CEN 位使能定时器。

18-77. 显示了三种比较输出模式：翻转/置高电平/置低电平，CAR=0x63，CHxVAL=0x3。


图 18-77. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="95">Overflow</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="90">match toggle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="85">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="81">match set</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">match clear</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="14">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 输出 PWM功能

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 3’b110，PWM 模式 1 是配置CHxCOMCTL 为 3’b111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

PWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。 $\boxtimes$ 18-78. PWM 显示了 PWM 的输出波形和中断。

在 PWM0 模式下 $( C H \times C O M C T L = = 3 ^ { \prime } 6 1 1 0 )$ ，如果 TIMERx_CHxCV 寄 存 器 的 值 大 于TIMERx_CAR 寄存器的值，通道输出一直为有效电平。

在 PWM0 模式下 $( \mathsf { C H x C O M C T L } = = 3 ^ { \prime } \mathsf { b } 1 1 0 )$ ，如果 TIMERx_CHxCV 寄存器的值等于 0，通道输出一直为无效电平。


图 18-78. PWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/25fa37c2d321e83aabecc11134d4da3263175361be550b6b3226754870d4d6ad.jpg)


## 通道输出准备信号

根据 18-75. x=0 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前会产生一个中间信号 OxCPRE 信号(通道 x 输出准备信号)。设置 CHxCOMCTL 位可以定义 OxCPRE 信号类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域为 0x06或0x07可以配置 PWM模式0/PWM模式1。在这些模式中，根据计数器值和 TIMERx_CHxCV寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL=0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 通道输出互补 PWM

CHx_O 和 CHx_ON 是一对互补输出通道，这两个信号不能同时有效。TIMERx 有四路通道，只有前三路有互补输出通道。互补信号 CHx_O 和 CHx_ON 是由一组参数来决定：TIMERx_CHCTL2 寄存器中的 CHxEN 和 CHxNEN 位，TIMERx_CCHP 寄存器中的 POEN、ROS 和 IOS 位，TIMERx_CTL1 寄存器中的 ISOx 和 ISOxN 位。输出极性由 TIMERx_CHCTL2寄存器中的 CHxP和 CHxNP 位来决定。


表 18-7. 由参数控制的互补输出表


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>CHxNEN</td><td>CHx_O</td><td>CHx_ON</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / CHx_ON = LOWCHx_O / CHx_ON 输出禁能(1)</td></tr><tr><td>1</td><td rowspan="3" colspan="2">CHx_O/CHx_ON输出关闭状态(2):通道先输出无效电平:CHx_O = CHxP,CHx_ON = CHxNP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,CHx_ON = ISOxN(3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/CHx_ON输出关闭状态:通道先输出无效电平:CHx_O = CHxP,CHx_ON = CHxNP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,CHx_ON = ISOxN</td></tr><tr><td rowspan="8">1</td><td rowspan="4">0</td><td rowspan="8">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/CHx_ON = LOWCHx_O/CHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>CHx_ON=OxCPRE⊕(4)CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON = LOWCHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON=(!OxCPRE)(5)⊕CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="4">1</td><td rowspan="2">0</td><td>0</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>CHx_ON = CHxNPCHx_ON输出关闭状态</td></tr><tr><td>1</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>CHx_O=OxCPRE⊕CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON = CHxNPCHx_ON输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON=(!OxCPRE)⊕CHxNPCHx_ON输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / CHx_ON 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / CHx_ON 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；



（3） 详情见中止模式章节。



（4） ⊕：异或操作；



（5） (!OxCPRE)：OxCPRE 信号的互补信号。


## 互补 PWM插入死区时间

设置 CHxEN 和 CHxNEN 为 1’b1 同时设置 POEN，死区插入就会被使能。DTCFG 位域定义了死区时间，死区时间对通道 0 有效。死区时间的细节，请参考 TIMERx_CCHP 寄存器。死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM0 模式，当通道 x 匹配发生时（TIMERx 计数器= CHxVAL），OxCPRE 翻转。18-79. 中的 A点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而CHx_ON信号立刻变为低电平。同样，在 B点，计数器再次匹配（TIMERx计数器= CHxVAL），OxCPRE 信号被清 0，CHx_O 信号被立即清零，CHx_ON 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。

有时会有一些死角事件发生，例如：

厂 如果死区延时大于或者等于CHx_O信号的占空比，CHx_O信号一直为无效值（如 18-79.带死区时间的互补输出)。

 如果死区延时大于或者等于CHx_ON信号的占空比，CHx_ON信号一直为无效值。


图 18-79. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/2ff5dedbcf602c4e582a1db6d41f4da3a52271617f0d78923e1ab120a0d10548.jpg)


## 中止模式

使用中止模式时，输出 CHx_O 和 CHx_ON 信号电平被以下位控制，TIMERx_CCHP 寄存器的 POEN, IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。当中止事件发生时，CHx_O 和 CHx_ON 信号输出不能同时设置为有效电平。中止源可以选择中止输入引脚，也可以选择 HXTAL 时钟失效事件。时钟失败事件由 RCU 中的时钟监视器(CKM)产生。将TIMERx_CCHP 寄存器的 BRKEN 位置 1 可以使能中止功能。TIMERx_CCHP 寄存器的 BRKP位决定了中止输入极性。

发生中止时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 CHx_ON 被 TIMERx_CTL1寄存器中的 ISOx 位和 ISOxN 驱动。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。起初互补输出被置于复位状态，然后死区时间产生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx 和 ISOxN 位配置。

发生中止时，TIMERx_INTF 寄存器的 BRKIF 位被置 1。如果 BRKIE=1，中断产生。


图 18-80. 通道响应中止输入（高电平有效）时，输出信号的行为


<table><tr><td rowspan="2"></td><td>BRKIN</td><td></td><td></td><td></td></tr><tr><td>OxCPRE</td><td></td><td></td><td></td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 1CHxP : 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td>= ISOx</td><td></td></tr><tr><td>CHx_ON</td><td></td><td>= ISOxN</td><td></td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP: 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td>= ISOx</td><td></td></tr><tr><td>CHx_ON</td><td></td><td>= ISOxN</td><td></td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP : 0 CHxNP : 0ISOx = ISOxN</td><td>CHx_O</td><td></td><td></td><td></td></tr><tr><td>CHx_ON</td><td></td><td></td><td></td></tr></table>

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式，可以通过设置TIMERx_SMCFG 寄存器中的 SMC [2:0]配置这些模式。这些模式的输入触发源可以通过设置TIMERx_SMCFG 寄存器中的 TRGS [2:0]来选择。


表 18-8. 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>SMC[2:0]3'b100(复位模式)3'b101(暂停模式)3'b110(事件模式)</td><td>TRGS[2:0]000: ITI0001: ITI1010: ITI2011: ITI3100: CI0F_ED101: CI0FE0110: CI1FE1111: 保留</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和 CHxNP来选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Clx,配置CHxCAPFLT设置滤波,分频不可用</td></tr><tr><td>例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TRGIS[2:0]=3'b000选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td></td><td colspan="4">图18-81.复位模式下的控制电路</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TRGIS[2:0]=3'b101选择CI0FE0为触发源</td><td>TI0S=0.(非异或)[CH0NP==0,CH0P==0]不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-82.暂停模式下的控制电路</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TRGIS[2:0]=3'b101选择CI0FE0为触发源.</td><td>TI0S=0(非异或)[CH0NP==0,CH0P==0]不反相</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-83.事件模式下的控制电路</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置 TIMERx_CTL0 寄存器的 SPM 位置 1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置 CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。为了最大限度减少延迟，用户可以将 TIMERx_CHCTL0 寄存器的 CHxCOMFEN 位置 1。单脉冲模式下，触发上升沿产生之后，OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。只有输出通道配置为 PWM0 或 PWM1 输出运行模式下时 CHxCOMFEN 位才可用，触发源来源于触发信号。

18-84. TIMERx_CHxCV = 4 TIMERx_CAR=99 展示了一个例子。


图 18-84. 单脉冲模式，TIMERx_CHxCV = 4 TIMERx_CAR=99


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/66974142e1b1aa9b2627a0913838f70abf06be8c48f0ed526f566acd508d77e8.jpg)


## 定时器互连

参考 .


表 18-9. TIMERx(x=14)定时器内部互连


<table><tr><td>Slave TIMER</td><td>ITI0(TRGS = 000)</td><td>ITI1(TRGS = 001)</td><td>ITI2(TRGS = 010)</td><td>ITI3(TRGS = 011)</td></tr><tr><td>TIMER14</td><td>保留</td><td>TIMER2</td><td>保留</td><td>保留</td></tr></table>

## 定时器 DMA模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。必须使能相应的 DMA 请求位，一些内部中断事件才可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA配置成 M2P（传输方向为从内存到外设）模式，PADDR（外设基地址）为 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC位域值为 0，表示 1 次传输，定时器发送 1 个 DMA请求就可以完成。如果 TIMERx_DMACFG寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次DMA请求。在这 3 次请求下，DMA对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的DMATA+0x4，DMATA+0x8，DMATA+0xC 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL1 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

