## 23.2. 通用定时器 L0（TIMERx, x = 1, 2 ,3, 4）

## 23.2.1. 简介

通用定时器 L0（TIMER1 / 2 / 3 / 4）是 4 通道定时器，支持输入捕获，输出比较，产生 PWM 信号控制电机和电源管理。通用定时器 L0 的计数器是 16 位或 32 位无符号计数器。

通用定时器 L0 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 23.2.2. 主要特征

 总通道数：4；

 计数器宽度：16位（TIMER2 / 3）和32位（TIMER1 / 4）；

 时钟源可选：内部时钟，内部触发，外部输入，外部触发；

 多种计数模式：向上计数，向下计数和中央计数；

 正交译码器接口：被用来追踪运动和分辨旋转方向和位置；

 霍尔传感器接口：用来做三相电机控制；

 可编程的预分频器：16位，运行时可以被改变；

 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

 自动重装载功能；

 中断输出和DMA请求：更新事件，触发事件，比较/捕获事件；

 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

 定时器主-从管理。

## 23.2.3. 结构框图

23-64. L0 提供了通用定时器 L0 的内部细节


图 23-64. 通用定时器 L0结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/8d2b8a6f2228b7e19ae0cd98cbdd447f30ad0e81203fae180a25173cfaed1025.jpg)


## 23.2.4. 功能描述

## 时钟源选择

通用定时器 L0 可以由内部时钟源 CK_TIMER 或者由 SYSCFG_TIMERxCFG(x = 1..4)寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ]$ $( \mathsf { y } = 0 . . . 9 , 1 5 )$ 位域控制的复用时钟源驱动。

 当 $1 { \tt S Y S C F G } _ { - } { \tt T I M E R x C F G } ( \tt x = 1 . 4 )$ 寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } \mathsf { b 0 0 0 0 0 } ( \mathsf { y } = 0 . . . 1 5 )$ 时，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 ${ \mathsf { S Y S C F G } } _ { - } { \mathsf { T I M E R x C F G } } ( \mathsf { x } = 1 . . 4 )$ 寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } \mathsf { b 0 0 0 0 0 } ( \mathsf { y } = 0 \ldots 1 5 )$ ，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

如果 ${ \mathsf { S Y S C F G } } _ { - } { \mathsf { T I M E R x C F G } } ( \mathsf { x } = 1 . . 4 )$ 寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] ( \mathsf { y } = 0 . . . 2 , 6 , 8 , 9 )$ 位域设置为非零值，预分频器被其他时钟源驱动，具体在下文说明。当 $\mathsf { T S C F G y } [ 4 ; 0 ]$ (y = 3, 4, 5, 7)被设置为非零值时，计数器预分频器时钟源由内部时钟 TIMER_CK 驱动。


图 23-65. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/dbee27eebb2e7528ebdfbc1dc41000ff2191f6f9a100382bf3c9f08c662659ac.jpg)



 TSCFG6[4:0] !=5’b00000（外部时钟模式0），定时器选择外部输入引脚作为时钟源


计数器预分频器可以在 CI0 / CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x5 ~ 0x7 来选择。

计数器预分频器也可以在内部触发信号 ITI0 ~ 10 / ITI14 的上升沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x1 ~ 0x4，0x9 ~ 0xF 和 0x13 来选择。

■ SMC1= 1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG 寄存器中的 SMC1 位为 1 来选择。另一种选择 ETI 信号作为时钟源方式是，设置 TSCFG6[4:0]为 0x08。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择 ETI信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

注意：ETI 信号可以从外部 ETI 引脚输入，也可由片上外设提供，具体情况可以参考 TIMER1_ETITRIGSEL_TIMER1ETI 、 TIMER2_ETITRIGSEL_TIMER2ETI 、 TIMER3_ETI       TRIGSEL_TIMER3ETI 和TIMER4_ETI TRIGSEL_TIMER4ETI 模块。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 23-66. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/aa9319023635b52b9e590fbe34be5ac2250f892e00a28ef07d05f175bf7ce061.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

23-67. PSC=0 / 2 和 23-68. TIMERx_CAR给出了一些例子，当 TIMERx_CAR = 0x99 时，计数器在不同预分频因子下的行为。


图 23-67. 向上计数时序图，PSC=0 / 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/81dfe4df742e5b4afae4354ebc1a37b4ea7290a73887ebd82a1cadeb389445df.jpg)



图 23-68. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/b49265d261c9b273da3e9f7bb9538da0b742ff5e3da9d80a3577cf6ce5243793.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/82f85527cbf6fe448f0f167bc78a2c4e9a5c9c60b53138e57c1b2709482b6db1.jpg)


## 向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数并产生下溢事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

23-69. PSC=0 / 2 和 23-70. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 23-69. 向下计数时序图，PSC=0 / 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/887bca2afc12a54f7c4e3374bdb57ad1c9f5cb7e75c144ddb9450e237482e0e8.jpg)



图 23-70. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/f498a5d6a448cc00a8d0c37b8f80df4840f16528e1ff018eb57f608cc5dbbb8c.jpg)


## 中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（TIMERx_CAR-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。计数方向被硬件自动更新。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1，然而 CHxIF 位置 1 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 23-71.如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

23-71. 给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为


图 23-71. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/0438ad3152062d86bf231c63a56f6e7360d9e4416198d2906208f4b9776e14b4.jpg)


## 捕获 / 比较通道

通用定时器 L0 拥有四个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

##  输入捕获模式

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 CHxIF 位被置 1，如果 CHxIE = 1 则产生通道中断。


图 23-72. 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/d4baeb0a4c2691225163a8a15e9514f8ffb466e98ccbcb7bbfa9521772332cbc.jpg)


通道输入信号 CIx 有两种选择，一种是 TIMERx_CHx 信号，另一种是 TIMERx_CH0，TIMERx_CH1和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。通道输入信号 CIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP选择使用上升沿或者下降沿。配置 CHxMS，可以选择其他通道的输入信号，内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，CHxVAL 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT）：根据输入信号和请求信号的质量，配置相应的CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP）：配置CHxP选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS）：一旦通过配置CHxMS选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x0），而且TIMERx_CHxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中CHxIE和CHxDEN）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中CHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV被设置成当前计数器的值，CHxIF为置1。如果CHxIF位已经为1，则CHxOF位置1。根据TIMERx_DMAINTEN寄存器中CHxIE和CHxDEN的配置，相应的中断和DMA请求会被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV 寄存器测量PWM 的周期值，TIMERx_CH1CV 寄存器测量 PWM 占空比值。

 输出比较模式


图 23-73. 输出比较逻辑 $( \pmb { x } = \pmb { 0 } , 1 , 2 , 3 )$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/82ec84a18e01051eb0537e36c7463b96dbc45ff30e651d89a4a3bee166198fbc.jpg)


23-73. $( { \pmb x } = { \pmb 0 } , \ { \pmb 1 } , \ { \pmb 2 } , \ { \pmb 3 } )$ 给出了输出比较的逻辑电路。通道输出信号CHx_O与${ \mathsf { O x C P R E } }$ 信号（详情请见 ）的关系描述如下：OxCPRE信号高电平有效，CHx_O的输出情况与 $\mathsf { \Pi } _ { \mathsf { J } } { \mathsf { O x C P R E } }$ 信号，CHxP位和CHxEN位有关（具体情况请见TIMERx_CHCTL2寄存器中的描述）。例如，当设置 ${ \mathsf { C H } } \times { \mathsf { P } } { = } 0$ （CHx_O高电平有效，与 $\mathsf { 1 O x C P R E }$ 输出极性相同）、 $C H \times E N = 1$ （CHx_O输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_O输出有效（高）电平；

若 ${ \mathsf { O x C P R E } }$ 输出无效（低）电平，则CHx_O输出无效（低）电平。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 CHxCV 寄存器与计数器的值匹配时，根据 CHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 ${ \mathsf { C H } } { \mathsf { x C V } }$ 寄存器的值匹配时，CHxIF 位被置 1，如果 ${ \mathsf { C H } } { \times } | \mathsf { E } = 1$ 则会产生中断，如果 ${ \mathsf { C } } { \mathsf { x C D E } } { = } 1$ 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

设置 $\mathsf { C H x C O M S E N }$ 位来配置输出比较影子寄存器；

设置 ${ \mathsf { C H x C O M C 7 } }$ L位来配置输出模式（置高电平/置低电平/翻转）；

设置 ${ \mathsf { C H } } { \mathsf { x P } }$ 位来选择有效电平的极性；

设置 ${ \mathsf { C H x E N } }$ 使能输出。

第三步：通过 $\mathsf { C H x l E / C x C D E }$ 位配置中断/DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

${ \mathsf { C H x V A L } }$ 可以在运行时根据你所期望的波形而改变。

第五步：设置CEN位使能定时器。

23-74. 显示了三种比较输出模式：翻转/置高电平/置低电平， $\mathsf { C A R } { = } 0 \times 6 3$ 

CHxVAL=0x3。 


图 23-74. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="95">上溢</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="91">匹配翻转</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="86">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="82">匹配位置</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="12">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="12">匹配清零</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="12">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 4’b0110，PWM 模式 1 是配置CHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。23-75. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 23-76. CAPWM 显示了 CAPWM 的输出波形和中断。

当计数器向上计数时，在PWM0模式下（CHxCOMCTL =4’b0110），如果TIMERx_CHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为有效电平；PWM1模式下（CHxCOMCTL=4’b0111），如果TIMERx_CHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为无效电平。


图 23-75. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/5f56a923b23ea8f51fc95399c89c71af0e60d2b44bcf04fe5d368d20b02e288e.jpg)



图 23-76. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/fa4d1bad4c8c789bee5f5bd202fcba8f4f05ab5d0e6ec63c6306d65fdfa5e1b3.jpg)


## 微调模式

通过配置TIMERx_CTL0寄存器中的ADMEN位为1，可以使能微调模式。该模式可以提高输出PWM波的有效分辨率，通过TIMERx_CHxCV寄存器中的CHxVAL[19:0]位域（TIMER2 / 3）或CARL[31:0]位域（TIMER1 / 4）可以提高占空比分辨率，通过TIMERx_CAR寄存器中的CHxVAL[19:0]位域（TIMER2 / 3）或CARL[31:0]位域（TIMER1 / 4）可以提高PWM频率的分辨率。

当微调模式使能时，CHxVAL位域和CARL位域的低16位[15:0]（TIMER2 / 3）或低28位[27:0]（TIMER1 / 4）用于整数部分，高4位[19:16]（TIMER2 / 3）或[31:28]（TIMER1 / 4）用于微调的小数部分。通过预定义的方式，在连续16个周期内对CHxVAL值或CARL值进行微调（每次调整不超过一个TIMER时钟周期），可增加16倍的分辨率。


图 23-77. 微调模式：数据格式和寄存器位域


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/d1fe029f04ce59e03f93500a8ad1758ea8ff2b1cfa1558860fd65aadb72abfb3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/5f9084e41ac3df5c99f2ca34627801314f203824d543f0b5e1802b20bf614a9f.jpg)


根据ADMEN位的配置（置位或清零），CHxVAL位域和CARL位域将自动更新。当需要对ADMEN位进行清零时，需要遵循以下步骤：

1. CEN位和ARSE位必须清零；

2. CARL[19:16]位域（TIMER2 / 3）或CARL[31:28]位域（TIMER1 / 4）必须清零；

3. ADMEN位必须清零；

4. CHxIF位必须清零；

5. 可以将CEN位置1。

以下公式可以计算PWM分辨率：

$$
\text { Resolution } = f _ {\text { PSC\_CLK }} / f _ {\text { pwm }}\tag{23-4}
$$

由式(23-4)可得，微调模式禁能时（ADMEN=0），PWM的最小频率 $\mathsf { f } _ { \mathsf { p w m } }$ :

16位（TIMER2/3），

$$
\left(f _ {p w m}\right) _ {\min} = f _ {P S C \_ C L K} / 6 5 5 3 6\tag{23-5}
$$

32位（TIMER1/4），

$$
(f _ {\text {pwm}}) _ {\min} = f _ {\text {PSC\_CLK}} / 2 ^ {2 8}\tag{23-6}
$$

微调模式使能时（ADMEN=1），

16位（TIMER2 / 3），

$$
\left(f _ {p w m}\right) _ {\min} = f _ {P S C \_ C L K} / (6 5 5 3 5 + 1 5 / 1 6)\tag{23-7}
$$

32位（TIMER1 / 4），

$$
(f _ {\text {pwm}}) _ {\min} = f _ {\text {PSC\_CLK}} / \left[ (2 ^ {2 8} - 1) + 1 5 / 1 6 \right]\tag{23-8}
$$

当微调模式使能时，CHxVAL[19:0]位域和CARL[19:0]位域的最大值为0xFFFFE（整数部分为0xFFFE，小数部分为0xF），CHxVAL[31:0]位域和CARL[31:0]位域的最大值为0xFFFFFFFE（整数部分为0xFFFFFFE，小数部分为0xF）。

在连续16个周期内，占空比和周期的变化情况，具体如 23-78. PWM 16 和23-13. CHxVAL CARL 所示。


图 23-78. PWM 微调模式原理（16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/6c669fb0fcfd2bdd21f7763aab9f647b5313305d07595f6bdb94b467616b8998.jpg)



表 23-13. 边沿对齐模式中 CHxVAL 和 CARL 位域的变化


<table><tr><td rowspan="2">CHxVAL[19:16]/CARL[19:16]</td><td colspan="16">周期</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>0000</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0001</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0010</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0011</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0100</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0101</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0110</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0111</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1001</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1010</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1011</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1100</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1101</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1110</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1111</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr></table>

PWM微调模式也适用于中央对齐模式，具体请见 23-14. CHxVAL CARL，微调模式应用在8个连续的PWM周期。


表 23-14. 中央对齐模式中 CHxVAL 和 CARL 位域的变化


<table><tr><td rowspan="3">CHxVAL[19:16]/CARL[19:16]</td><td colspan="15">周期</td><td></td></tr><tr><td colspan="2">1</td><td colspan="2">2</td><td colspan="2">3</td><td colspan="2">4</td><td colspan="2">5</td><td colspan="2">6</td><td colspan="2">7</td><td>8</td><td></td></tr><tr><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td><td>向上计数</td><td>向下计数</td></tr><tr><td>0000</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0001</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0010</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0011</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0100</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0101</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0110</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0111</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1001</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1010</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1011</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1100</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1101</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1110</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1111</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr></table>

## 复合 PWM 模式

在复合 PWM 模式中（CHxCPWMEN = 1’b1，CHxMS[2:0] = 3’b000 和 CHxCOMCTL = 4’b0110、4’b0111），通道 x（x = 0…3）上的 PWM 输出信号由 CHxVAL 和 CHxCOMVAL_ADD 位确定。

如果 CHxCOMCTL = 4’b0110（PWM 模式 0）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL= 4’b0111（PWM 模式 1）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为低。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为高。

如果 CHxCOMCTL =4’b0111（PWM 模式 1）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL=4’b0110（PWM 模式 0）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为高。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为低。

PWM 的周期取决于（CARL + 0x0001），PWM 脉冲宽度可以下 23-15. PWM 计算。


表 23-15. 复合 PWM 脉冲宽度


<table><tr><td>条件</td><td>模式</td><td>PWM脉冲宽度</td></tr><tr><td rowspan="2">CHxVAL &lt; CHxCOMVAL_ADD ≤ CARL</td><td>PWM模式0</td><td>(CARL + 0x0001) + (CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &lt; CHxVAL ≤ CARL</td><td>PWM模式0</td><td>(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CARL + 0x0001) + (CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">(CHxVAL = CHxCOMVAL_ADD ≤ CARL)或 (CHxVAL &gt; CARL &gt; CHxCOMVAL_ADD)</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>100%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>0%</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &gt; CARL &gt; CHxVAL</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>0%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>100%</td></tr><tr><td>(CHxVAL&gt;CARL)且 (CHxCOMVAL_ADD &gt; CARL)</td><td>-</td><td>CHx_O输出保持</td></tr></table>

当计数器计数到CHxVAL，CHxIF位置1且如果CHxIE=1通道x产生中断，如果CHxDEN=1，则产生DMA请求。当计数器计数到CHxCOMVAL_ADD时，CHxCOMADDIF位置1（该中断标志位只在复合PWM模式有效，CHxCPWMEN=1），如果CHxCOMADDIE = 1通道x附加比较中断产生（只有中断产生，没有DMA请求响应）。

根据CHxVAL，CHxCOMVAL_ADD和CARL之间的关系，可以分为四种情况：

 CHxVAL < CHxCOMVAL_ADD，CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。


图 23-79 通道 x 输出 PWM（CHxVAL < CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/011df4e61fb8e25197298b0e7e266cab56b2e1b10bd5b8b6f805765d15bf375e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/a4b0321313ed70bd1e981053d765e7b1ef5d20769a85beb9c9605b4f3c9125f3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/cd37b84e8ff31bd7cca077f7461933355ab19aa35d3efe3cd223e8840dc2a122.jpg)



 CHxVAL = CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 23-80. 通道 x 输出 PWM（CHxVAL = CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/413eed12a919f36c6b8ad0db7559b12f5c12a7ff899ef56627a892fe0b689389.jpg)



 CHxVAL > CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 23-81. 通道 x 输出 PWM（CHxVAL > CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/c1563eac5a382b287f90688b1ef34775758479b42e649b31d8cea24ede337fd8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/aeeaec8310867d9057da565543a2dcef28a9b798433853ea929af974b93cc7f6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/85a589004d856ca4ce7b368982e71a399d04651d7ab10d5ef76c22e5f5fedb46.jpg)



 CHxVAL或CHxCOMVAL_ADD值大于CARL。



图 23-82. 通道 x 输出 PWM（CHxVAL 或 CHxCOMVAL_ADD > CARL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/676cce64d3612d7ad47b064d44fc70644867f70e0aef669ef782ce680d3d5ffe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/b0ca6524a615bcd62d73a6c5db61142dfd5f60ef1dc73cd45844496bc27ae495.jpg)



复合PWM模式支持不修改周期只修改占空比的PWM信号的生成。 23-83. x PWMCHxCOMVAL_ADD 显示PWM输出和中断波形。


在某些情况下，CHxCOMVAL_ADD的匹配事件可以发生在下一个计数周期（CHxCOMVAL_ADD值在计数器到达CHxVAL值之后被写入，且CHxCOMVAL_ADD值小于或者等于CHxVAL值）。


图 23-83. 通道 x 输出 PWM 占空比随着 CHxCOMVAL_ADD 值而改变


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/8eb3f363c395be776cb8a528e962c8c7cf2fcaa1ec3dab7bd1f249eeb10525e1.jpg)


如果多个通道配置为复合PWM模式，可以为每对通道x的匹配边沿设定一个偏移量（相对于其它通道）。这种特性在产生照明PWM控制信号时非常有用，因为在这种情况下，希望彼此边缘不重合，以消除噪声的产生。CHxVAL寄存器值是PWM脉冲相对于计数器周期开始的偏移。


图 23-84. 复合 PWM 模式下四通道输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/7ef922c1587b2ddd944a21b00d55aee678846560fcdaa2e6849199cc5a20e94c.jpg)


## 输出匹配脉冲选择

当发生匹配事件时，CHx_O（x = 0…3）的输出由CHxCOMCTL[3:0] $( \mathsf { x } = 0 . . . 3 )$ 位设置，通过配置CHxOMPSEL[1:0] $( \mathsf { x } = 0 . . . 3 )$ 位，可选择CHx_O $( \mathsf { x } = 0 . . . 3 )$ 的输出信号正常或者脉冲。

当匹配事件发生时， $\mathsf { C H x O M P S E L } [ 1 : 0 ]$ $( \mathsf { x } = 0 . . . 3 )$ 用于选择OxCPRE信号输出（驱动CHx_O）：

 $\mathsf { C H x O M P S E L } = 2 ^ { \prime } \mathsf { b 0 0 }$ ${ \mathsf { O x C P R E } }$ 信号根据 $\mathsf { C H x C O M C T L } [ 3 ; 0 ]$ 位的配置正常输出；

 $\mathsf { C H x O M P S E L } = 2 ^ { \prime } \mathsf { b } 0 1$ ，只有在计数器向上计数，发生匹配事件时，OxCPRE信号输出一个脉

冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b10，只有在计数器向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b11，无论计数器向上计数还是向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；


图 23-85. 边沿对齐模式下 CHx_O 输出脉冲（CHxOMPSEL ≠ 2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/061d46663ae381507d1b2e499bceffd28b634c8845886f6f80f01b0ca89482b7.jpg)



图 23-86. 中央对齐模式下 CHx_O 输出脉冲（CHxOMPSEL ≠ 2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/243c835b6db86ef96cd908b440ebdb36d38afbd04392439bec368ba60a11f4fd.jpg)


## 通道输出准备信号

根据 23-73. x = 0, 1, 2, 3 所示，当 TIMERx 用于输出匹配比较模式下，设置CHxCOMCTL 位可以定义 OxCPRE 信号（通道 x 准备信号）类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将

OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06 或0x07 可以配置 PWM 模式 0/PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 清除通道输出准备信号

当 CHxCOMCEN 位 （ 在 TIMERx_CHCTLy 寄 存 器 中 ） 置 1 时 ， OxCPRE 信 号 可 以 由OCPRE_CLR_INT信号清除。该功能用于CHxCOMCTL[3:0]位域位域（4'b0100和4'b0101除外）中配置的比较输出模式。

可以通过TIMERx_SMCFG寄存器中的OCRC位来选择OCPRE_CLR_INT的信号源。

OCRC 位 清 0 时 ， OCPRE_CLR_INT 连 接 到 OCPRE_CLR 输 入 。 OxCPRE 信 号 被OCPRE_CLR_INT 信号 的高 电 平 清除 ， 直 到下 一个 更 新 事件 发 生 时才 会恢 复 输 出。 在TIMERx_AFCTL1 寄存器的 OCRINSEL[2:0]位域中选择 OCPRE_CLR 的输入。

OCRC 位置 1 时，OCPRE_CLR_INT 连接到 ETIF。由 TIMERx_SMCFG 寄存器中的 ETP 位配置 OCPRE_CLR_INT 的输入极性。此时，ETPSC[1:0]位域必须设置为 2'b00。

## 正交译码器

参考 (TIMERx,x = 0,7) 。

## 译码器

参考 (TIMERx,x = 0,7) 。

正交译码器和译码器的时钟输出

参考 (TIMERx,x = 0,7)

索引输入功能

参考 (TIMERx,x = 0,7) 。

霍尔传感器接口功能

参考 (TIMERx,x = 0,7) 。

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式等，可以通过设置SYSCFG_TIMERxCFG(x = 1..4)寄存器中的 TSCFGy[4:0] (y = 3..7)位域来确定，具体的输入触发源可以通过 TSCFGy[4:0] (y = 3..7)位域值来选择。


表 23-16. 从模式列表和举例（通用定时器 L0）


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[4:0]y = 3: 复位模式y = 4: 暂停模式y = 5: 事件模式y = 6: 外部时钟模式0y = 7: 复位+事件模式y = 8: 暂停 + 事件模式</td><td>TSCFGy[4:0]00000: 模式禁能00001: ITI000010: ITI100011: ITI200100: ITI300101: CI0F_ED00110: CI0FE000111: CI1FE101000: ETIFP(1)01001: ITI401010: ITI501011: ITI601100: ITI701101: ITI801110: ITI901111: ITI1010000: 保留10001: 保留10010: 保留10011: ITI14</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相。如果触发源是ETIFP(滤波后的ETI外部触发输入),配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Clx,配置CHxCAPFLT设置滤波,分频不可用触发源是ETIFP,滤波和预分频不可用</td></tr><tr><td>例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[4:0]5&#x27;b00001,选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="2">极性选择</td><td>滤波和预分频</td></tr><tr><td></td><td colspan="5">图23-87.复位模式<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/47e5e801051f6936078efa913b67d82fec9e49b69af8114fc34b7b1197cfb5a8.jpg"/></td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[4:0]=5&#x27;b00110,选择CI0FE0为触发源</td><td colspan="2">TIOS=0(非异或)[CH0NP=0, CHOP=0]不反相,在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="5">图23-88.暂停模式TIMER_CKCENCNT_REGCI0CI0FE0TRGIF</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[4:0]=5&#x27;b01000,选择ETIFP为触发源</td><td>ETP=0没有极性改变</td><td colspan="2">ETPSC=1,2分频ETFC=0,无滤波</td></tr><tr><td colspan="5">图23-89.事件模式<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/3979ba176665d4118281072f45a90e6e020f2644d3f5c8937685bd16835f0aab.jpg"/></td></tr><tr><td>例4</td><td colspan="5">复位+事件模式当触发输入的上升沿到来时,计数器被重新初始化并开始计数。该模式仅用于可延时的单脉冲模式。</td></tr></table>


GD32G553 用户手册


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>例5</td><td colspan="4">暂停+复位模式当触发输入的上升沿或下降沿(由 TIMERx_SMCFG 寄存器中的 PRMRPSEL 位配置)到来时,计数器将复位。当触发输入高时计数器计数,当触发输入低时计数器停止。在这种模式下,计数器的开始和停止可以被控制。</td></tr></table>

(1) ETI 信号可以从外部 ETI 引脚输入，也可由片上外设提供，具体情况可以参考 TIMER1_ETITRIGSEL_TIMER1ETI 、TIMER2_ETI TRIGSEL_TIMER2ETI 、TIMER3_ETITRIGSEL_TIMER3ETI 和 TIMER4_ETI TRIGSEL_TIMER4ETI模块。

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。单脉冲模式也同样适用于复合 PWM 模式（ $\mathsf { C H x C P W M E N } = 1 ^ { \prime } \mathsf { b } 1$ 和 $\mathsf { C } \mathsf { H } \times \mathsf { M } \mathsf { S } [ 2 : 0 ] = 3 ^ { \prime } \mathsf { b } 0 0 0 $ ）。


图 23-90. 单脉冲模式，TIMERx_CHxCV = 0x04，TIMERx_CAR = 0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/595fea8045eca7c3cb87cf83012b6cf3571632382b30fe6aea843ae8f54817e7.jpg)


## 可延时的单脉冲模式

可以通过将TIMERx_CHCTLx寄存器中的CHxCOMCTL[3:0]位置1来使能可延时的单脉冲模式。在

这个模式下，通道输出准备信号OxCPRE的脉冲宽度由TIMERx_CAR寄存器值确定。

一旦设置定时器运行在可延时的单脉冲模式下，需进行以下配置：

 定时器必须工作在从模式下，SYSCFG_TIMERxCFG(x = 1..4)寄存器中的 TSCFG7[4:0] !=5’b00000，从模式选择复位 + 事件模式；

 CHxCOMCTL[3:0]位设置为 4’b1000（可延时单脉冲模式 0）或 4’b1001（可延时单脉冲模式1）

在可延时单脉冲模式0下，OxCPRE的输出情况类似与PWM模式0。在向上计数模式时，OxCPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平；在向下计数模式时，OxCPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平。

在可延时单脉冲模式1下，OxCPRE的输出情况类似与PWM模式1。在向上计数模式时，OxCPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平；在向下计数模式时，OxCPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平。

PWM微调模式也可用于可延迟的单脉冲模式。

## 注意：

 不能使用中央对齐模式，TIMERx_CTL0 寄存器中的 CAM[1:0] = 2’b00；

 在向上计数时（TIMERx_CTL0 寄存器中的 DIR = 0），TIMERx_CHxCV 的值设置为 0；在向下计数时，TIMERx_CHxCV 的值应大于或等于 TIMERx_CAR 的值。


图 23-91. 可延时单脉冲模式（TIMERx_CHxCV = 0x00，TIMERx_CAR = 0x60）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2b2e25f2-56ee-49cd-8b83-84bad9d2c415/88bdad1c051e70ace1c6d0de89d5764017f6cbe9a63829eb653509a42f56ea1c.jpg)


可编程的脉冲输出

参考 (TIMERx,x = 0,7) 。

## 定时器互连

参考 (TIMERx,x = 0,7) 。

## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4, DMATA+0x8，DMATA+0xc 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## 输出 DIR 位

DIR位可以在CH2和CH3通道上输出，配置在TIMERx_CHCTL1寄存器中的CH2COMCTL[3:0]或CH3COMCTL[3:0]位域值为4b'1011来使能该功能。

当计数器工作在中央对齐模式时，该功能可用于指示计数器的计数方向。当计数器工作在译码器模式时，此功能可用于指示外部信号的旋转方向。

## UPIF位备份功能

可以通过配置TIMERx_CTL0寄存器中的UPIFBUEN位来使能UPIF位的备份功能，UPIF和UPIFBU位之间没有延迟，两者完全同步。

使能该功能后，TIMERx_INTF寄存器中的UPIF位将会被实时备份到TIMERx_CNT寄存器中的UPIFBU位。这可以避免在读计数器和中断处理时产生冲突的情况。

## 定时器调试模式

当Cortex<sup>®</sup>-M33内核停止，DBG_CTL0寄存器中的TIMERx_HOLD配置位被置1，定时器计数器停止。

