## 13.1. 高级定时器（TIMERx, x=0, 7）

## 13.1.1. 简介

高级定时器（TIMER0/7）是四通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。高级定时器含有一个 16 位无符号计数器。

高级定时器是可编程的，可以用于计数，其外部事件可以驱动其他定时器。

高级定时器包含了一个死区时间插入模块，非常适合电机控制。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 13.1.2. 主要特性

 总通道数：4；

 计数器宽度：16位；

 时钟源可选：内部时钟，内部触发，外部输入，外部触发；

 多种计数模式：向上计数，向下计数和中央计数；

 正交译码器接口：用来追踪运动和分辨旋转方向和位置；

 霍尔传感器接口：用来进行三相电机控制；

 可编程的预分频器：16位，运行时可以被改变；

每个通道相互独立且可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式和触发输出；

 可编程的死区时间和独立的死区时间配置；

 自动重装载功能；

 可编程的计数器重复功能；

 中止输入功能：BREAK和通道0/1/2中止；

 中断输出和DMA请求：更新事件，触发事件，比较/捕获事件和中止事件；

 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

 定时器主-从管理。

## 13.1.3. 结构框图

13-1. 提供了高级定时器的内部配置细节。


图 13-1. 高级定时器结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/4f3fa04299e268d44eb312f7f01305c4c57cf1e3364a63e21d98094ecec41c9f.jpg)


## 13.1.4. 功能描述

## 时钟源选择

高级定时器可以由内部时钟源 CK_TIMER 或者由 SYSCFG_TIMERxCFG(x=0,7)寄存器中的TSCFGy[4:0] (y=0...6)位域控制的复用时钟源驱动。

 当 $\mathsf { I S Y S C F G \_ T I M E R x C F G } ( \mathsf { x } = 0 , 7 )$ 寄存器中的TSCFGy[4:0]=5’b00000(y=0...6)时，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 SYSCFG_TIMERxCFG(x=0,7)寄存器中的 ${ \mathsf { T S C F G y } } [ 4 ; 0 ] = 5 { \mathsf { b 0 0 0 0 0 } } ( { \mathsf { y = 0 \ldots 6 } } )$ ，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

如果 $\mathtt { S Y S C F G \_ T I M E R x C F G } ( x = 0 , 7 )$ 寄存器中的 TSCFGy[4:0] (y=0..2,6)位域设置为非零值，预分频器被其他时钟源驱动，具体在下文说明。当 TSCFGy[4:0] (y=3,4,5)被设置为非零值时，计数器预分频器时钟源由内部时钟 TIMER_CK 驱动。


图 13-2. 内部时钟分频为 1时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/4a98d71276bde5b56fad13edcc12b6ac7e2eeaafb18bc105f19d1b79eae7306e.jpg)



■ TSCFG6[4:0] !=5’b00000（外部时钟模式0），定时器选择外部输入引脚作为时钟源



计数器预分频器可以在 TIMERx_CHn（n=0..3）引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[4:0]为 0x5~0x7 和 0x9/0xA 来选择。


计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x1~0x4 来选择。

■ SMC1=1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG 寄存器中的 SMC1 位为 1 来选择。另一种选择 ETI 信号作为时钟源方式是，设置 TSCFG6[4:0]为 0x8。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择 ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 13-3. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/ff8efe2f5df5d2bb599150d0fc146f673e7c8d197ea695ed6b2827dce75bef05.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数。如果设置了重复计数器，在（TIMERx_CREP0+1）次上溢后产生更新事件，否则在每次上溢时都会产生更新事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

13-4. PSC=0/2 和 13-5. TIMERx_CAR给出一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 13-4. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/9b13861e8c2f85cda2584b0ff3c24b057cb4a7d294f25bff6cc26bc3057e0b8b.jpg)



图 13-5. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/69798b2305d5476d50c0b764f82a9ffd8e51e1d86584a070ba46e79e6f8a17f0.jpg)


## 向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数。如果设置了重复计数器，在（TIMERx_CREP0+1）次下溢后产生更新事件，否则在每次下溢时都会产生更新事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

13-6. PSC=0/2 和 13-7. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 13-6. 向下计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/d6f4b49b050dd1e0d685732f5b4b5735672a0328a869537f7c87b8e65d8153aa.jpg)



图 13-7. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/9607dd79189d0562ffdf265662c6c03e9ed3c41a652eaa6a60ad2b78d87aa169.jpg)


## 中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（TIMERx_CAR-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。计数方向被硬件自动更新。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1，然而 CHxIF 位置 1 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 13-8. 。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

13-8.            给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为。


图 13-8. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/f86cdba3ed6c63c51cda5657c4faa4a863cadce5b07013ae064c317948cb1a6f.jpg)


## 重复计数器

重复计数器是用来在（N+1）个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP0寄存器的CREP0的值。向上计数模式下，重复计数器在每次计数器上溢时递减；向下计数模式下，重复计数器在每次计数器下溢时递减；在中央对齐模式下，重复计数器在计数器上溢和下溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP0 寄存器中 CREP0 的值并产生一个更新事件。

新写入的 CREP0 值将在下一次更新事件到来时生效。当 CREP0 的值为奇数，并且计数器在中央对齐模式下计数时，更新事件发生在上溢或下溢取决于写入的 CREP0 值何时生效。如果在写入奇数到 CREP0 寄存器后由软件生成更新事件（UPG 位置 1），则在下溢时产生更新事件。如果在写入奇数到 CREP0 寄存器后下一个更新事件发生在上溢，此后将在上溢时产生更新事件。


图 13-9. 中央计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/8b7deb32cd8da24294a4a15ed589d93885a2932d56b9ccfc906791c4d46008bd.jpg)



图 13-10. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/2ce73b9c3327f5ea0ddfed9cc2aeb99610a496df32631842f8347c78783c54cf.jpg)



图 13-11. 在向下计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/9e9adda813903bf9acf65af28c5c0152ca7e6997143d53b114e0ddb91b85587d.jpg)


## 捕获/比较通道

高级定时器拥有 4 个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

##  输入捕获模式

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV（x=0..3）寄存器会捕获计数器当前的值，同时 CHxIF（x=0..3）位置 1，如果CHxIE =1（x=0..3），则产生相应的通道中断。


图 13-12. 通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/1e6796c1f65fb246bb1775ae53214d4114a35460697cc85aa3ab24e12bbed8c2.jpg)



通道输入信号 CIx 有两种选择，一种是 TIMERx_CHx 信号，另一种是 TIMERx_CH0，TIMERx_CH1和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。


通道输入信号 CIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP/ CHxNP 选择使用上升沿或者下降沿。配置 CHxMS，可以选择其他通道的输入信号或内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0 寄存器中 CHxCAPFLT 位）：

根据输入信号和请求信号的质量，配置相应的 CHxCAPFLT 位。

第二步：边沿选择（TIMERx_CHCTL2 寄存器中 CHxP 和 CHxNP 位）：

配置 CHxP和 CHxNP 位选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0 寄存器中 CHxMS）：

一旦通过配置 CHxMS 选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x000），而且TIMERx_CHxCV 寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN 寄存器中 CHxIE、CHxDEN 位）：

使能相应中断，可以获得中断和 DMA请求。

第五步：捕获使能（TIMERx_CHCTL2 寄存器中 CHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV 被设置成当前计数器的值，CHxIF 位置 1。如果 CHxIF 位已经为 1，则 CHxOF 位置 1。根据 TIMERx_DMAINTEN 寄存器中 CHxIE、CHxDEN位的配置，相应的中断和 DMA请求会被提出。

直接产生：软件设置 CHxG 位，会直接产生中断和 DMA 请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 3’b001，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 3’b010，选择通道 1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV 寄存器测量PWM 的周期值，TIMERx_CH1CV 寄存器测量 PWM 占空比值。

 输出比较模式

13-13. 给出了通道的输出比较逻辑。


图 13-13. 输出比较逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/b67e3a27841335cf82d0be79d7dadfd346f1296aea503f22e981fcd0b8bfa3b9.jpg)


在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 TIMERx_CHxCV 寄存器与计数器的值匹配时，根据 CHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 TIMERx_CHxCV 寄存器的值匹配时，CHxIF 位被置 1，如果 CHxIE = 1 则会产生中断，如果 CHxDEN =1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

 设置CHxCOMSEN位来配置输出比较影子寄存器；

 设置CHxCOMCTL位来配置输出模式（置高电平/置低电平/翻转）；

 设置CHxP/CHxNP位来选择有效电平的极性；

 设置CHxEN/CHxNEN使能输出。

第三步：通过 CHxIE/ CHxDEN 位配置中断/DMA 请求使能。

第四步：通过 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器配置输出比较时基：

TIMERx_CHxCV 可以在运行时根据你所期望的波形而改变。

第五步：设置 CEN 位使能定时器。

13-14. 显示了三种比较输出模式：翻转/置高电平/置低电平，CAR=0x63,

CHxVAL=0x3。 


图 13-14. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="97">CNT_REG</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="96">上溢</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="91">匹配翻转</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="87">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="83">匹配位置</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">匹配清零</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 4’b0110，PWM 模式 1 是配置CHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。13-15. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 13-16. CAPWM 显示了 CAPWM 的输出波形和中断。

当计数器向上计数时，在 PWM0 模式下（CHxCOMCTL =4’b0110），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为有效电平；PWM1 模式下（CHxCOMCTL=4’b0111），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为无效电平。


图 13-15. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/dfea01abaafdce19aa2a55e58141f46a287299110721481400b92b2f13e7d505.jpg)



图 13-16. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/8bd83d2861c107610fdd2e789edc562a54a79d3319d5f2795ae184f454f7903c.jpg)


## 复合 PWM 模式

在复合 PWM 模式中 $( { \mathsf { C H x C P W M E N } } = 1 ^ { \prime } { \mathsf { b 1 } } , { \mathsf { C H x M S } } [ 2 : 0 ] = 3 ^ { \prime } { \mathsf { b 0 0 0 } } { \mathit { \# } } \mathbb { I } { \mathsf { C H x C O M C T L } } = 4 ^ { \prime } { \mathsf { b 0 1 } } 0 { \mathsf { 0 2 } } .$ 4’b0111），通道 x（x=0..3）上的 PWM 输出信号由 CHxVAL 和 CHxCOMVAL_ADD 位确定。

如果 $\mathsf { C H x C O M C T L } = 4 ^ { \prime } 6 0 1 1 0 \mathrm { ~ ( P W M }$ 模式 0）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL= 4’b0111（PWM 模式 1）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为低。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为高。

如果 CHxCOMCTL =4’b0111（PWM 模式 1）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL=4’b0110（PWM 模式 0）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为高。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为低。

当 CHxVAL 或 CHxCOMVAL_ADD = 0 / CARL ， 通 道 输 出 被 进 行 了 特 殊 处 理 ， 通 过TIMERx_CHCTL2 寄存器的 CHxPERFOREN 位置位，强制 OxCPRE 输出高电平或低电平（根据所选复合 PWM 模式确定）。

PWM 的周期取决于（CARL + 0x0001），PWM 脉冲宽度可以下 13-2 PWM 计算。


表 13-2 复合 PWM 脉冲宽度


<table><tr><td>条件</td><td>模式</td><td>PWM脉冲宽度</td></tr><tr><td rowspan="2">CHxVAL &lt; CHxCOMVAL_ADD ≤ CARL</td><td>PWM模式0</td><td>(CARL + 0x0001) +(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &lt; CHxVAL ≤ CARL</td><td>PWM模式0</td><td>(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CARL + 0x0001) +(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">(CHxVAL = CHxCOMVAL_ADD ≤ CARL)或 (CHxVAL &gt; CARL &gt; CHxCOMVAL_ADD)</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>100%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>0%</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &gt; CARL &gt; CHxVAL</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>0%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>100%</td></tr><tr><td>(CHxVAL&gt;CARL)且 (CHxCOMVAL_ADD &gt; CARL)</td><td>-</td><td>CHx_O输出保持</td></tr></table>


当计数器计数到 CHxVAL，CHxIF 位置 1 且如果 CHxIE=1 通道 x 产生中断，如果 CHxDEN=1，则产生 DMA 请求。当计数器计数到 CHxCOMVAL_ADD 时，CHxCOMADDIF 位置 1（该中断标志位只在复合 PWM 模式有效，CHxCPWMEN=1），如果 CHxCOMADDIE = 1 通道 x 附加比较中断产生（只有中断产生，没有 DMA 请求响应）。


根据 CHxVAL，CHxCOMVAL_ADD 和 CARL 之间的关系，可以分为四种情况：

## 1） CHxVAL < CHxCOMVAL_ADD，CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。


图 13-17. 通道 x 输出 PWM（CHxVAL < CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/9f8375e6e408b24462cf14c0704818383096634295f01b5eef3b2a4f114a1c77.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/b032d87041350b19c37606307968b7b42a65524c855299dd46297ae8016f35a8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/2e6169fe9d80a42aad69a42e0a6f1b9b0bd16e5c6ea5df4b41386a1bfeb50564.jpg)



2） CHxVAL = CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13-18. 通道 x 输出 PWM（CHxVAL = CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/754131ae2824ff723d11753aa8991661fa97f0ac13e2017000820b6ce441cf8c.jpg)



3） CHxVAL > CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13-19. 通道 x 输出 PWM（CHxVAL > CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/d31f4998678b6131e23bd981ee9e8ad6e96571fd208ce136747a51337c0783b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/dbb06973ff89445bf4d4782151b169969e27399fa02d4a0533311f26b4c25371.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/5db9ad9381b37999e54a7ff244d8143cb788bcfd98e04fe4a97464c128568d1d.jpg)



4） CHxVAL或CHxCOMVAL_ADD值大于CARL。



图 13-20. 通道 x 输出 PWM（CHxVAL 或 CHxCOMVAL_ADD > CARL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/d2579495a7b8f6fae5e58631c092d6ae13f3f9f13c7bd25e39520449c06c888f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/8b057c16b5f4a0c924e476dfa31a659c4544161a881875750dc8c8e6a14bff0a.jpg)



复合 PWM 模式支持不修改周期只修改占空比的 PWM 信号的生成。 13-21. x PWMCHxCOMVAL_ADD 显示 PWM 输出和中断波形。


在某些情况下，CHxCOMVAL_ADD 的匹配事件可以发生在下一个计数周期（CHxCOMVAL_ADD值在计数器到达 CHxVAL 值之后被写入，且 CHxCOMVAL_ADD 值小于或者等于 CHxVAL 值）。


图 13-21. 通道 x 输出 PWM 占空比随着 CHxCOMVAL_ADD 值而改变


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/cc957a0f1e6e73ea3aac93263cb9600be39bbf59a5822775628e2f856826f662.jpg)


如果多个通道配置为复合 PWM 模式，可以为每对通道 x 的匹配边沿设定一个偏移量（相对于其它通道）。这种特性在产生照明 PWM 控制信号时非常有用，因为在这种情况下，希望彼此边缘不重合，以消除噪声的产生。CHxVAL 寄存器值是 PWM脉冲相对于计数器周期开始的偏移。


图 13-22. 复合 PWM 模式下四通道输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/3a8ff485c623f30fbe190c74622c9633eff4d546fa1f74cd40ff6c0d37a1202e.jpg)


## 非对称 PWM 模式

非对称 PWM 波允许两个中央对齐的 PWM 波之间产生一个可编程的相位偏移。在非对称 PWM 波模式下 $( \mathsf { C H x C O M C T L } [ 3 : 0 ] = 4 ^ { \prime } \mathsf { b 1 0 1 0 } / 4 ^ { \prime } \mathsf { b 1 0 1 1 a n d C H x M S } [ 2 : 0 ] = 3 ^ { \prime } \mathsf { b 0 0 0 }$ ），在通道上输出的PWM 波信号是由 CHxVAL 和 CHxCOMVAL_ADD 位共同控制的，非对称 PWM 波只在中央对齐模式下有效。

如果 $\mathsf { C H x C O M C T L } = 4 ^ { \prime } \mathsf { b } 1 0 1 0$ （非对称 PWM 波模式 0），向上计数模式 $( \mathsf { D } | \mathsf { R } = 1 ^ { \prime } \mathsf { b } 0 )$ ），当计

数值达到 CHxVAL 的值时，输出强制为低电平。

如果 CHxCOMCTL = 4’b1010（非对称 PWM 波模式 0），向下计数模式 $( \mathsf { D } | \mathsf { R } = 1 ^ { \prime } \mathsf { \Delta } \mathsf { b } 1 )$ ），当计数值达到 CHxCOMVAL_ADD 的值时，输出强制为高电平。

如果 CHxCOMCTL = 4’b1011（非对称 PWM 波模式 1），向上计数模式 $( \mathsf { D } | \mathsf { R } = 1 ^ { \prime } \mathsf { \Delta } \mathsf { b } 0 )$ ），当计数值达到 CHxVAL 的值时，输出强制为高电平。

如果 CHxCOMCTL = 4’b1011（非对称 PWM 波模式 1），向下计数模式（DIR = 1’b1），当计数值达到 CHxCOMVAL_ADD 的值时，输出强制为低电平。

与复合 PWM 模式相比，非对称 PWM 模式只在中央对齐模式下有效，同时 CHxVAL 只在向上计数模式时有效，CHxCOMVAL_ADD 只在向下计数模式时有效。当 CHxVAL 或 CHxCOMVAL_ADD= 0 / CARL，通道输出被进行了特殊处理，通过 TIMERx_CHCTL2 寄存器的 CHxPERFOREN 位置位，强制 OxCPRE 输出高电平或低电平（根据所选非对称 PWM 模式确定）。

当 CHxVAL = 0，在非对称 PWM0 模式下，通道输出被强制为低电平，在非对称 PWM1 模式下，通道输出被强制为高电平。

当 CHxCOMVAL_ADD = 0，在非对称 PWM0 模式下，通道输出被强制为高电平，在非对称 PWM1模式下，通道输出被强制为低电平。

当 CHxVAL =CARL，在非对称 PWM0 模式下，通道输出被强制为低电平，在非对称 PWM1 模式下，通道输出被强制为高电平。

当 CHxCOMVAL_ADD = CARL，在非对称 PWM0 模式下，通道输出被强制为高电平，在非对称PWM1 模式下，通道输出被强制为低电平。

PWM 的周期取决于 2*CARL，PWM 脉冲宽度可以下 13-3 PWM 计算。


表 13-3 非对称 PWM 脉冲宽度


<table><tr><td>条件</td><td>模式</td><td>PWM 脉冲宽度</td></tr><tr><td rowspan="2">CHxVAL &lt; CHxCOMVAL_ADD ≤ CARL 或者 CHxCOMVAL_ADD &lt; CHxVAL ≤ CARL 或者 CHxVAL = CHxCOMVAL_ADD</td><td>非对称 PWM 模式 0</td><td>CHxCOMVAL_ADD + CHxVAL</td></tr><tr><td>非对称 PWM 模式 1</td><td>2*CARL - CHxCOMVAL_ADD - CHxVAL</td></tr><tr><td rowspan="2">CHxVAL &gt; CARL &gt; CHxCOMVAL_ADD</td><td>非对称 PWM 模式 0</td><td>100%</td></tr><tr><td>非对称 PWM 模式 1</td><td>0%</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &gt; CARL &gt; CHxVAL</td><td>非对称 PWM 模式 0</td><td>0%</td></tr><tr><td>非对称 PWM 模式 1</td><td>100%</td></tr><tr><td>(CHxVAL&gt;CARL)且 (CHxCOMVAL_ADD &gt; CARL)</td><td>-</td><td>CHx_O 输出保持</td></tr></table>

当计数器计数到 CHxVAL，CHxIF 位置 1 且如果 CHxIE=1 通道 x 产生中断，如果 CHxDEN=1，则产生 DMA 请求。当计数器计数到 CHxCOMVAL_ADD 时，CHxCOMADDIF 位置 1（该中断标志位只在复合 PWM 模式和非对称 PWM 模式有效，当 CHxCOMCTL[3:2]= 2’b10），如果CHxCOMADDIE = 1 通道 x 附加比较中断产生（只有中断产生，没有 DMA 请求响应）。

根据 CHxVAL，CHxCOMVAL_ADD 和 CARL 之间的关系，可以分为四种情况：


1） CHxVAL < CHxCOMVAL_ADD，CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13.23 通道 x 输出 PWM（CHxVAL < CHxCOMVAL_ADD / CHxCOMVAL_ADD < CHxVAL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/dcc8f50393a3abff695856ecfbfabf6767fcdf0a4ae951bde9a918f5728e8f54.jpg)



b. 0 < CH1VAL < CH1VAL_ADD = CARL / 0 < CH2VAL_ADD < CH2VAL = CARL, 同时CH1VAL = CH2VAL_ADD


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/a2e23574c352144258060c9fc781f099362dcb11b1e1dc38ab03444f557fca92.jpg)



c. 0 = CH1VAL < CH1VAL_ADD < CARL / 0 = CH2VAL_ADD < CH2VAL < CARL, 同时


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/bd3f2c99091073bd86998f891ace77c223b204bab27f7bdccda8a97a074b6237.jpg)



2） CHxVAL = CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13.24. 通道 x 输出 PWM（CHxVAL = CHxCOMVAL_ADD）



0 < CH1VAL = CH1VAL_ADD < CARL / CH2VAL = CH2VAL_ADD = 0 / CH3VAL = CH3VAL_ADD = CARL


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/4c62be9ee71fa80fe3373236d0c369528366b830a61a75dccb97d2e535ff7105.jpg)



3） CHxVAL或CHxCOMVAL_ADD值大于CARL。



图 13.25. 通道 x 输出 PWM（CHxVAL 或 CHxCOMVAL_ADD > CARL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/dd2415d3d19d338bed6a85acc6d9183de395f873ddead587092bc4cc901c8bdd.jpg)


## 输出匹配脉冲选择

当发生匹配事件时，CHx_O（x=0..3）的输出由 CHxCOMCTL[3:0]（x=0..3）位设置，通过配置CHxOMPSEL[1:0]（x=0..3）位，可选择 CHx_O（x=0..3）的输出信号正常或者脉冲。

当匹配事件发生时，CHxOMPSEL[1:0]（x=0..3）用于选择 OxCPRE 信号输出（驱动 CHx_O）：

 CHxOMPSEL = 2’b00，OxCPRE信号根据CHxCOMCTL[3:0]位的配置正常输出；

 CHxOMPSEL = 2’b01，只有在计数器向上计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b10，只有在计数器向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b11，无论计数器向上计数还是向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；


图 13-26. 边沿对齐模式下 CHx_O 输出脉冲（CHxOMPSEL≠2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/58f57e47017637faf8bea1af304ecd8165e787efbb6c8cb9facbe4702e2ddf9e.jpg)



图 13-27. 中央对齐模式下 CHx_O 输出脉冲（CHxOMPSEL≠2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/a983d2a43a7d0ee5a61aa7c241417c59a794f5939837e2940404b4dcd931eec5.jpg)


## 通道输出参考信号

如 13-13. 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前将产生一个中间信号，即 OxCPRE 信号（通道 x 参考信号）。

OxCPRE 信号有若干类型的输出功能，通过配置 CHxCOMCTL 位定义 OxCPRE 信号类型。

下面以 OxCPRE 为 例 进 行 说 明 ， 设 置 CHxCOMCTL=0x00 可 以 保 持 原 始 电 平 ； 设 置CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器

的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06 或0x07 可以配置 PWM 模式 0/PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件（OCPRECIVM = 1）或者上溢/下溢事件（OCPRECIVM = 0）到来时，OxCPRE 信号才会回到有效电平状态。

## 互补输出

CHx_O 和 CHx_ON 是一对互补输出通道，这两个信号不能同时有效。TIMERx 有 4 对通道，所有4 对通道都具有此功能。互补信号 CHx_O 和 CHx_ON 是由一组参数来决定：TIMERx_CHCTL2寄存器中的 CHxEN 和 CHxNEN 位，TIMERx_CCHP0 寄存器中和 TIMERx_CTL1 寄存器中的POEN&CHPOENx(x=0...2)、ROS、IOS、ISOx 和 ISOxN 位。输出极性由 TIMERx_CHCTL2 寄存器中的 CHxP 和 CHxNP 位来决定。

当 CHx_O 和 CHx_ON 的输出互补时，有三种输出情况：输出使能、输出关闭状态和输出禁能，具体情况可参考 13-4. 。


表 13-4. 由参数控制的互补输出表


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN &amp;CHP OENx</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>CHxNEN</td><td>CHx_O</td><td>CHx_ON</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / CHx_ON = LOWCHx_O / CHx_ON 输出禁能(1)</td></tr><tr><td>1</td><td colspan="2" rowspan="3">CHx_O/CHx_ON输出关闭状态(2):通道先输出无效电平:CHx_O = CHxP,CHx_ON = CHxNP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,CHx_ON = ISOxN(3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/CHx_ON输出关闭状态:通道先输出无效电平:CHx_O = CHxP,CHx_ON = CHxNP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,CHx_ON = ISOxN</td></tr><tr><td rowspan="2">1</td><td rowspan="2">0</td><td rowspan="2">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/CHx_ON = LOWCHx_O/CHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>CHx_ON=OxCPRE⊕(4)CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="6"></td><td rowspan="2"></td><td rowspan="6"></td><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE ⊕ CHxP CHx_O输出使能</td><td>CHx_ON = LOW CHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕ CHxP CHx_O输出使能</td><td>CHx_ON = (!OxCPRE)<eq>^{(5)}</eq> ⊕ CHxNP CHx_ON输出使能</td></tr><tr><td rowspan="4">1</td><td rowspan="2">0</td><td>0</td><td>CHx_O = CHxP CHx_O输出关闭状态</td><td>CHx_ON = CHxNP CHx_ON输出关闭状态</td></tr><tr><td>1</td><td>CHx_O = CHxP CHx_O输出关闭状态</td><td>CHx_ON = OxCPRE ⊕ CHxNP CHx_ON输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE ⊕ CHxP CHx_O输出使能</td><td>CHx_ON = CHxNP CHx_ON输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕ CHxP CHx_O输出使能</td><td>CHx_ON = (!OxCPRE) ⊕ CHxNP CHx_ON输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / CHx_ON 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / CHx_ON 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；



（3） 详情见中止模式章节。


（4） ⊕：异或操作；

（5） (!OxCPRE)：OxCPRE 信号的互补信号。

## 死区时间插入

设置 CHxEN 和 CHxNEN 为 1’b1 同时设置 POEN&CHPOENx(x=0...2)，死区插入就会被使能。DTCFG 位域定义了死区时间，死区时间对所有通道有效。死区时间设置的细节请参考0 TIMERx_CCHP0 。

死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM0 模式，当通道 x 匹配发生时（TIMERx 计数器=TIMERx_CHxCV），OxCPRE 翻转。在13-28. 的 A 点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而 CHx_ON 信号立刻变为低电平。同样，在 B 点，计数器再次匹配（TIMERx计数器=TIMERx_CHxCV），OxCPRE 信号被清 0，CHx_O 信号被立即清零， CHx_ON 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。

有时会有一些死角事件发生，例如：如果死区延时大于或者等于 CHx_O 信号的占空比，CHx_O

信号一直为无效值。如 13-28. 所示。


图 13-28. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/648ba4e60382769c4cc2a83f750da2eb94ddb9092dc8ede34c3fd948378e74e3.jpg)



通过配置 TIMERx_CTL2 寄存器中的 DTIENCHx（x = 0..3）位，可实现对每对通道的死区插入功能的独立控制。当 DTIENCHx（x = 0..3）位为“0”时，相应的通道 CHx_O 和 CHx_ON 将不会插入死区。


## 不同的死区时间插入

当 DTDIFEN 位（在 TIMERx_CCHP1 寄存器中）设置为 1 时，CHx_O 和 CHx_ON 信号可以输出不同的死区时间，具体如 13-29. DTDIFEN=1）所示。

通道输出准备信号 OxCPRE 上升沿的死区时间由 TIMERx_CCHP0 寄存器中的 DTCFG[7:0]位域配置。OxCPRE 信号的下降沿的死区时间由 TIMERx_CCHP1 寄存器中的 DTFCFG[7:0]位域配置。DTDIFEN 位必须在使能计数器之前写入，且当 CEN=1 时不能修改。


图 13-29. 不同死区时间的互补输出（DTDIFEN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/4cfeecfca45ed7c58f50b544ac5aedac6991f3299e283a65e2388c0a81bf7957.jpg)


## 中止功能

使用中止功能时，CHx_O 和 CHx_ON 信号的输出电平由以下位控制：TIMERx_CCHP0 寄存器的POEN、IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。在这种情况下，CHx_O 和CHx_ON 信号不能同时设置为有效电平。

中止事件是所有源逻辑或运算的结果。中止功能可以处理三种类型的事件源：

 外部信号源：来自BRKIN0输入；

 系统源： LVD锁定事件，Cortex®-M33锁定事件或SRAM奇偶校验错误事件；

 片上外设源：比较器输出。

中止事件也可以由软件置位 TIMERx_SWEVG 寄存器中的 BRKG 位产生。

BREAK 中止功能逻辑如 13-30. BREAK 所示，其中 BRKIN0 可以从 TRIGSEL模块选择 GPIO 引脚，具体可参考 TIMER0_BRKIN TRIGSEL_TIMER0BRKIN和 TIMER7_BRKIN TRIGSEL_TIMER7BRKIN


图 13-30. BREAK 中止功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/331c0c2d0081a2e173cebc8ec10cdd240d3d89b5b574a8fc188259fb0d435b04.jpg)



BREAK 可用于处理系统源、片上外设和外部输入信号源的故障，当发生 BREAK 中止事件时，输出强制为无效电平，或在死区持续时间之后，输出将以预定的电平（有效或无效）强制输出；


当发生 BREAK 中止事件时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 CHx_ON 的输出由 TIMERx_CTL1 寄存器中的 ISOx 位和 ISOxN 位确定。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。当 IOS=1 时，通道输出情况如 13-31. BREAK电平有效） $^ { \sharp \sharp , }$ IOS=1 所示，首先通道互补输出为复位状态，然后死区时间发生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx 和 ISOxN 位配置。


图 13-31. 通道响应 BREAK 中止输入（高电平有效）时，输出信号的行为（IOS=1）


<table><tr><td rowspan="2"></td><td>BREAK</td><td></td><td></td><td></td></tr><tr><td>OxCPRE</td><td></td><td></td><td></td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 1CHxP : 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td colspan="2">= ISOx</td></tr><tr><td>CHx_ON</td><td></td><td colspan="2">= ISOxN</td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP: 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td colspan="2">= ISOx</td></tr><tr><td>CHx_ON</td><td></td><td colspan="2">= ISOxN</td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP : 0 CHxNP : 0ISOx = ISOxN</td><td>CHx_O</td><td></td><td></td><td></td></tr><tr><td>CHx_ON</td><td></td><td></td><td></td></tr></table>


表 13-5. BREAK 输入信号时，TIMER 互补通道输出情况（break 输入高电平有效）


<table><tr><td rowspan="2">BREAK 输入</td><td colspan="2">Output Status</td></tr><tr><td>CHx_O</td><td>CHx_ON</td></tr><tr><td>高电平</td><td>IOS=1: CHx_O 输出无效,然后在一个死区时间之后输出空闲电平(由 IOSx 位确定)。IOS=0: CHx_O 输出禁能(无效)</td><td>IOS=1: CHx_ON 输出无效,然后在一个死区时间之后输出空闲电平(由 IOSxN 位确定)。IOS=0: CHx_ON 输出禁能(无效)</td></tr><tr><td>低电平</td><td>CHx_O 输出禁能(无效)</td><td>CHx_ON 输出禁能(无效)</td></tr></table>


发生中止事件时，TIMERx_INTF 寄存器的 BRKIF 位被置 1。如果 BRKIE=1，中断产生。


通过配置 TIMERx_CTL2 寄存器中的 BRKENCHx（x = 0..3）位，可实现对每对通道的中止功能进行独立控制。当 BRKENCHx（x = 0..3）位为“0”且发生中止事件时，相应的通道 CHx_O 和CHx_ON 输出保持不变。

为了增强中止功能的灵活性，对于高级定时器，每对通道都有单独的中止输入 CHxBRKIN（x=0...2），当相应的 CHxBRKIN（x=0...2）输入有效电平时，可以异步对相应的 CHPOENx（x=0...2）清 0，可实现单独的中止输入控制对应的每对通道中止后输出。通过在 TIMERx_CCHP0 寄存器中设置CHBRKEN 位，可以开启通道中止。通过在 TIMERx_CCHP0 寄存器中设置 CHBRKP 位，可以配置通道中止的极性。

此外，如果启用了通道的中止功能，CHx_O 和 CHx_ON（x=0...2）不仅受 POEN 控制，还受CHPOENx（x=0...2）控制。CHx 和 CHx_ON（x=0...2）在被中止后的输出与 BREAK 功能相同。

每个通道中止输入都有自己的使能位CHBRKxINEN（x=0...2）和极性控制位CHBRKxINP（x=0...2），并与 BREAK 有相同的滤波配置位域 BRKF[3:0]。请参考 13-32. 。

当通道 x（x=0...2）的 BREAK 输入有效电平时，相应的通道中止标志位 CHxBRKIF（x=0...2）会被设置为 1。如果通道 x（x=0...2）的 BREAK 输入在多个周期内保持有效状态，标志位 CHxBRKMIF（x=0...2）将被设置为 1。周期计数可以通过配置 TIMERx_CHBRKPER 寄存器来确定。


图 13-32. 通道中止功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/40665ab382d0a9271e4fcb35f3c13df4d08afa82cf106d3d99e4d4b708165b6d.jpg)


## 正交译码器

正交译码器功能使用由 TIMERx_CH0 和 TIMERx_CH1 引脚生成的 CI0 和 CI1 正交信号各自相互作用产生计数值。在每个输入源改变期间，DIR 位被硬件自动改变。

输入源可以是只有 CI0，可以只有 CI1，或着可以同时有 CI0 和 CI1，通过设置 TSCFGy[4:0]( y=0,1, 2) != 5’b00000 来选择使用哪种模式。计数器计数方向改变的机制如 13-6.所示。其中，CI0FE0、CI1FE1 是经过滤波和极性选择后的 CI0、CI1 信号。正交译码器可以当作一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动加载值之间连续的计数。因此，用户必须在计数器开始计数前配置 TIMERx_CAR 寄存器。


表 13-6. 不同译码器模式下的计数方向


<table><tr><td rowspan="2">计数模式</td><td rowspan="2">电平</td><td colspan="2">CI0FE0</td><td colspan="2">CI1FE1</td></tr><tr><td>上升</td><td>下降</td><td>上升</td><td>下降</td></tr><tr><td rowspan="2">正交译码器模式0TSCFG0[4:0]!= 5&#x27;b00000</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>-</td><td>-</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>-</td><td>-</td></tr><tr><td rowspan="2">正交译码器模式1TSCFG1[4:0]!= 5&#x27;b00000</td><td>CI0FE0=1</td><td>-</td><td>-</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>-</td><td>-</td><td>向下</td><td>向上</td></tr><tr><td rowspan="4">正交译码器模式2TSCFG2[4:0]!= 5&#x27;b00000</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>X</td><td>X</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>X</td><td>X</td></tr><tr><td>CI0FE0=1</td><td>X</td><td>X</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>X</td><td>X</td><td>向下</td><td>向上</td></tr></table>


注意：“-”意思是“无计数”；“X" 意思是不可能。“0”意思是低电平，“1”意思是高电平。



图 13-33. 译码器接口模式下计数器运行例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/4a220a1d7cd8c5cbb13f2aa8d766a9117613b655661d8f5c001ba9c59ef8f656.jpg)



图 13-34. CI0FE0 极性反相的译码器接口模式下的例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/434b4dedc7ceae32b3805f7d826fb207e726803eeee23331ffd3dd9022c96aa6.jpg)


## 正交译码器和非正交译码器的时钟输出

定时器可以通过 TRGO 输出译码器时钟输出信号。该功能仅用于正交译码器模式 0~2，通过将TIMERx_CTL1 寄存器中 MMC[3:0]位域设置为 4'b1000 来使能。

## 霍尔传感器接口功能

高级定时器支持霍尔传感器接口功能，该功能可以用来控制 BLDC 电机。

13-35. BLDC 是定时器和电机的连接示意图。众所周知，我们要两个定时器。TIMER_in 定时器（可以是高级定时器或者通用 L0 定时器）接收来自电机霍尔传感器的三路信号，这三路信号是电机转子的位置信号。

三个霍尔传感器与 TIMER_in 定时器的三路输入捕获引脚一一对应连接，每个霍尔传感器输入一路波形到输入引脚，分析三路霍尔信号可以计算出转子的位置和速度。

通过定时器内部连接，例如 TRGO-ITIx，TIMER_in 定时器和 TIMER_out 定时器可以连接在一起。TIMER_out 定时器根据 ITIx 触发信号输出 PWM 波，驱动 BLDC 电机，控制 BLDC 电机的速度。这样，TIMER_in 定时器和 TIMER_out 定时器的连接形成了一个反馈电路，可以根据需求改变配置。

TIMER_in 定时器需要具备输入异或功能，所以可以选择高级定时器和通用 L0 定时器。

TIMER_out 定时器需要具备互补输出和死区插入功能，所以可以选择高级定时器。

另外，可以通过 TRIGSEL 模块，选择互连的定时器，例如：

$$
\text { TIMER\_in } (\text { TIMER0 }) \rightarrow \text { TIMER\_out } (\text { TIMER7   ITI0 })
$$

$$
\text { TIMER\_in } (\text { TIMER1 }) \rightarrow \text { TIMER\_out } (\text { TIMER0   ITI1 })
$$

选择好合适的互连定时器，定时器和 BLDC 的线路也已经连接好，我们就可以配置定时器了。有以下关键配置：

 设置TI0S，使能异或功能。三路输入信号的任何一路发生变化，CI0都会翻转，CH0VAL此时会捕获计数器的当前值。

 设置CCUC和CCSE，使能ITIx直接连接到换相功能。

 根据需求配置PWM参数。


图 13-35. 霍尔传感器用在 BLDC 电机控制中


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/858ba6fc4e51e493259da4de857fbbbf5ab16dfb3736c1e7be4acbc05c643590.jpg)



图 13-36. 两个定时器之间的霍尔传感器时序图



高级/通用L0定时器TIMER_in工作在输入捕获模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/d7ce2cde3a04f9749b54131afc6948b1eeaa9993ea21fd9b053a3d652a9d6b95.jpg)



高级定时器TIMERout工作在输出比较模式（带有死区的PWM）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/dfe0c7e6df79a79d151fef9ff6bde1fcaf9b6c5e1168b0fa6239acf66a744537.jpg)


## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式等，可以通过设置SYSCFG_TIMERxCFG(x=0,7)寄存器中的 TSCFGy[4:0] (y=3..6)位域来确定，具体的输入触发源可以通过 TSCFGy[4:0] (y=3..6)位域值来选择。


表 13-7. 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="2">极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[4:0]y=3:复位模式y=4:暂停模式y=5:事件模式y=6:外部时钟模式0</td><td>TSCFGy[4:0]00000:Mode disable00001:ITI000010:ITI100011:ITI200100: ITI300101: CI0F_ED00110: CI0FE000111: CI1FE101000: ETIFP(1)01001: CI2FE201010: CI3FE3</td><td colspan="2">如果触发源是CIxFEx(x=0..3),配置CHxP、CHxNP来选择极性和反相。如果触发源是ETIFP(滤波后的ETI外部触发输入),配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源CIx,配置CHxCAPFLT设置滤波,分频不可用</td></tr><tr><td></td><td></td><td></td><td colspan="2"></td><td>触发源是ETIFP,配置ETFC设置滤波,配置ETPSC设置预分频</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[4:0]5'b00001,选择ITIO为触发源</td><td colspan="2">触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="5">图13-37. 复位模式<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/c4f03b0a0fdb0a41891b1096444217085f39034ac4ae0e9404ceb1b4f308d1ec.jpg"/></td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[4:0]=5'b00110,选择CI0FE0为触发源</td><td colspan="2">TIOS=0(非异或)[CHONP=0,CHOP=0]CI0FE0不反相,在上升沿捕获。</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="5">图13-38. 暂停模式下的控制电路<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/ae9274e0034918e4e325ec3df91154a61f910df7be919de32a95d123a0583b28.jpg"/></td></tr><tr><td>例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[4:0]=5'b01000,选择ETIFP为触发源</td><td>ETP = 0没有极性改变</td><td colspan="2">ETPSC = 1,2分频ETFC = 0,无滤波</td></tr><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td><td></td></tr><tr><td rowspan="6"></td><td colspan="4">图13-39.事件模式</td><td></td></tr><tr><td>TIMER_CK</td><td></td><td></td><td></td><td></td></tr><tr><td>ETI</td><td></td><td></td><td></td><td></td></tr><tr><td>ETIFP</td><td></td><td></td><td></td><td></td></tr><tr><td>CNT_REG</td><td>5E</td><td>5F</td><td>60</td><td>61</td></tr><tr><td>TRGIF</td><td></td><td></td><td></td><td></td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，可使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。

单脉冲模式也同样适用于复合 PWM 模式（ $\mathsf { C H x C P W M E N } = 1 ^ { \prime } \mathsf { b } 1$ 和 $\mathsf { C } \mathsf { H } \times \mathsf { M } \mathsf { S } [ 2 : 0 ] = 3 ^ { \prime } \mathsf { b } 0 0 0 $ ）。


图 13-40. 单脉冲模式，TIMERx_CHxCV = 0x04 TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/0fcc1044cf3220c5e8a9df3755a258a346f8d759124ebda84af475b4db7b4cde.jpg)


## 定时器互连

定时器之间可以内部级联或者同步，通过配置一个定时器工作在主模式另一个定时器工作在从模式来实现。

互连的例子：

##  定时器2作为定时器0的预分频器

配置定时器 2 为定时器 0 的预分频器，步骤如下：

1. 配置定时器2为主模式，选择其更新事件（UPE）为触发输出（配置TIMER2_CTL1寄存器的MMC=4’b0010）。定时器2在每次计数器溢出产生更新事件时，输出一个周期信号；

2. 配置定时器2周期（TIMER2_CAR寄存器）；

3. 配置定时器0工作在外部时钟模式0，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG1寄存器中的 $\mathsf { T S C F G 6 } [ 4 ; 0 ] = 5 \mathsf { b } ^ { \prime } 0 0 0 1 1 $ ）；

4. 写1到CEN位启动定时器0（TIMER0_CTL0寄存器）；

5. 写1到CEN位启动定时器2（TIMER2_CTL0寄存器）。

 用定时器2的使能/更新信号来启动定时器0

用定时器 2 的使能信号来启动定时器 0，见 13-41. 2 0。在定时器 2 使能信号输出后，定时器 0 按照分频后的内部时钟从当前值开始计数。

当定时器 0 接收到触发信号，它的 CEN 位被自动置 1，计数器计数直到禁能定时器 0。两个定时器的计数器频率都是 TIMER_CK 经过预分频器 3 分频后频率 $( \mathsf { f } _ { \mathsf { C N T \_ C L K } } = \mathsf { f } _ { \mathsf { T I M E R \_ C K } } / 3 )$ ）。步骤如下：

1. 配置定时器2为主模式，发送它的使能信号作为触发输出（配置TIMER2_CTL1寄存器的MMC=4’b0001）；

2. 配置定时器0工作在事件模式，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG0寄存器中的TSCFG5[4:0] = 5b’00011）；

3. 写1到CEN来开启定时器2（TIMER2_CTL0寄存器）。


图 13-41. 用定时器 2 的使能信号触发定时器 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/a20c70d7f0b2ce11bb5a5af26825b6b28dbc864adf1110bedd1d85db8846efac.jpg)


在这个例子中，我们也可以使用更新事件代替使能信号作为触发源。见 13-42. 2新事件来触发定时器0，按以下步骤进行：

1. 配置定时器2为主模式，发送它的更新事件（UPE）作为触发输出（配置TIMER2_CTL1寄存器的MMC=4’b0010）；

2. 配置定时器2的周期（TIMER2_CARL寄存器）；

3. 配置定时器0工作在事件模式，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG0寄存器中的TSCFG5[4:0] = 5b’00011）

4. 写1到CEN来开启定时器2（TIMER2_CTL0寄存器）。


图 13-42. 用定时器 2 的更新事件来触发定时器 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/bd555ec2694d1aab5a958abf1f409a6e286aedab5d3fc47056983d48383740fe.jpg)


 使用定时器2的使能/O0CPRE参考信号来使能定时器0计数。

在这个例子中，我们使用定时器 2 的使能输出来控制定时器 0 的使能。如 13-43. 20，在定时器 2 被使能后，定时器 0 在内部分频的时钟上开始计数。两个计数器的时钟频率都是由 TIMER_CK 时钟 3 分频得来 $( \mathsf { f c N T \_ c l K } = \mathsf { f _ { T I M E R \_ C K } } / 3 )$ ），步骤如下：

1. 配置定时器2在主模式，配置其输出使能信号作为触发输出（配置TIMER2_CTL1寄存器的MMC=4’b0001）；

2. 配置定时器0工作在暂停模式，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG0寄存器中的 $\mathsf { I S C F G 4 } [ 4 ; 0 ] = 5 \mathsf { b } ^ { \prime } 0 0 0 1 1 $ ）；

3. 写1到CEN位来使能定时器0（TIMER0_CTL0寄存器）；

4. 写1到CEN位来启动定时器2（TIMER0_CTL0寄存器）；

5. 写0到CEN位来停止定时器2（TIMER0_CTL0寄存器）。


图 13-43. 用定时器 2 的使能来选通定时器 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/d705880304c9310181ae8235927fa4b76703c656b548f31f5996050edd3c9220.jpg)


这个例子中，我们也可以使用定时器 2 的 O0CPRE 信号代替其使能信号输出作为触发源。步骤如下：

1. 配置定时器2在主模式下，配置O0CPRE信号为触发输出（配置TIMER2_CTL1寄存器的MMS=3’b100）；

2. 配置定时器2的O0CPRE波形（TIMER2_CH0CTL寄存器）；

3. 配置定时器0工作在暂停模式，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG0寄存器中的TSCFG4[4:0] = 5b’00011）；

4. 写1到CEN位来使能定时器0（TIMER0_CTL0寄存器）；

5. 写1到CEN位来开启定时器2（TIMER0_CTL0寄存器）。


图 13-44. 用定时器 2 的 O0CPRE 信号选通定时器 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/0f31db04d3de0c764bedd59ea8b6535eda370eee59f3b47fa459e06aa4aa1ba3.jpg)


 使用一个外部触发来同步两个定时器

配置定时器 2 的使能信号触发定时器 0 的开启，配置定时器 2 的 CI0 输入信号上升沿来触发定时器 2。为了确保两个定时器同步开启，定时器 2 必须配置在主/从模式。步骤如下：

1. 配 置 定 时 器 2 工 作 在 事 件 模 式 ， 定 时 器 2 输 入 触 发 源 为 CI0 的 触 发 输 入 CI0F_ED（SYSCFG_TIMER02CFG0寄存器中的TSCFG5[4:0] = 5b’00101）；

2. 写MSM=1（TIMER2_SMCFG寄存器）来配置定时器2工作在主/从模式；

3. 配置定时器0工作在事件模式，定时器0输入触发源为定时器2（SYSCFG_TIMER0CFG0寄存器中的TSCFG5[4:0] = 5b’00011）。

当定时器 2 的 CI0 信号产生上升沿时，两个定时器的计数器在内部时钟下开始同步计数，二者的TRGIF 标志位都被置 1。


图 13-45. 用定时器 2 的 CI0 输入来触发定时器 0和定时器 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/b0ac80c3960a6f029d0709f1a55f85b13ee92fadb46b73869890fb7f4db7f1b6.jpg)


## 计数器同步、初始方向和值刷新

在一些菊链的配置下，多个计数器被触发并且被同步在同一个时刻开始计数。由于不同的计数器之间在长时间计数之后可能会产生相位偏移，因此通过外部触发定时地刷新同步计数器来消除硬件上产生的多个计数器之间产生的相位偏移。此外，通过软件可配的计数器初始值配置（TIMERx_CINITV）,可以控制多个被触发的计数器之间的相位偏移关系。

4 个从计数器被配置存在同一触发输入源，通过使能 TIMERx_CINITCTL 寄存器的 CINITVEN 位域,可以使能计数器的初值载入功能，4 个从计数器的载入初值分别位 0，20，40，60，因此之间产生了 20 个 CK_TIMER 的等差相移。

下图中的 9998 计数值，表明了在长时间计数之后，不同计数器的之间产生了相位偏移，通过基础定时器的触发输出，刷新同步从定时器的计数值，避免了相位偏移的累积。


图 13.46. 用主计数器的 trigger 信号触发 4 个计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/57dda3bda93c478c7b5641639986492187c14d42b94647e6c63619cd0a601ee0.jpg)


当计数器处于中央对齐的计数方式时，可以通过配置 TIMERx_CINITCTL 寄存器的 CINITDIR 位域来配置计数器复位之后的计数方向。CINITDIR 只有当使能了 CINITVEN 时才会生效，另外当计数器处于向上/向下计数模式下时，CINITDIR 的配置也不会生效。

当 CINITDIR 为 0 时，复位计数器之后的计数方向为向上；当 CINITDIR 为 1 时，复位计数器之后的计数方向为向下。如下图所示：


图 13.47. CINITDIR 为 0 或 1 时的计数方向


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/e7111e075c3ba12f6a29681bd65a15dbc5c908a6bc0e92c04c4e51cbdcce82e2.jpg)


计数器的初始计数方向和初始值也可以通过软件同步事件刷新。将 TIMERx_CINITCTL 寄存器中的 SWSYNCG 位置 1，可以产生一个软件同步事件，用于刷新 TIMERx 计数器的初始计数方向和

初始值。

当高级定时器使用主模式下来同步其他高级定时器时，在 TIMERx_CTL1 寄存器中 MMC[3:0]位域需要设置为 4'b1001。此时，TIMERx 的软件同步事件（设置 SWSYNCG 位为 1 产生）可以作为TRGO 信号输出，用于同步其他高级定时器。

## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA 请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4、DMATA+0x8、DMATA+0xC 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL 寄存器中的 TIMERx_HOLD 位置 1 时，定时器的计数器停止计数。

