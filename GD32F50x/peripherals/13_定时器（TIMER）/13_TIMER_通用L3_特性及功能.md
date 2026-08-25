## 13.3. 通用定时器 L3（TIMERx, x=15,16）

## 13.3.1. 简介

通用定时器 L3（TIMER15/16）是 3 通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。通用定时器 L3 含有一个 16 位无符号计数器。

通用定时器 L3 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器

通用定时器 L3 包含了一个死区时间插入模块，非常适合电机控制。

定时器和定时器之间是相互独立，但是他们可以被同步在一起形成一个更大的定时器，这些定时器的计数器一致地增加。

## 13.3.2. 主要特性

 总通道数：3；

 计数器宽度：16位；

 时钟源可选：内部时钟，内部触发，外部输入；

 多种计数模式：向上计数，向下计数和中央计数；

 可编程的预分频器：16位，运行时可以被改变；

 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

 可编程的死区时间；

 自动重装载功能；

 可编程的计数器重复功能；

 中止输入功能：BREAK；

 中断输出和DMA请求：更新事件，比较/捕获事件和中止事件；

 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

 定时器主-从管理。

## 13.3.3. 结构框图

13-70. L3 提供了通用定时器 L3 的内部配置细节


图 13-70. 通用定时器 L3结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/208ba8ef591d62e9eb56e9898e982b773f1d2b5075804f97408ed6aa47242d55.jpg)


## 13.3.4. 功能描述

## 时钟源选择

通用定时器 L3 可以由内部时钟源 TIMER_CK 或者由 SYSCFG_TIMERxCFG(x=15,16)寄存器中的 TSCFGy[4:0] (y=3..6,15)位域。

当SYSCFG_TIMERxCFG(x=15,16)寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } \mathsf { b 0 0 0 0 0 } ( \mathsf { y } = 3 . . 6 , 1 5 )$ ，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 SYSCFG_TIMERxCFG(x=15,16)寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 \mathsf { b 0 0 0 0 0 } \ ( \mathsf { y } = 3 . 6 , 1 5 )$ ，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER

如果 SYSCFG_TIMERxCFG(x=15,16)寄存器中的 TSCFG6[4:0]位域设置为非零值，预分频器被其他时钟源驱动，具体在下文说明。当 TSCFGy[4:0] (y=3,4,5)被设置为非零值时，计数器预分频器时钟源由内部时钟 TIMER_CK 驱动。


图 13-71. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/889e31c3d0bd2a627a13d2470d72b749f3f9cc13dc52c63d83f214b6c565e8c2.jpg)



 TSCFG6[4:0]设置为非零值（外部时钟模式0），定时器选择外部输入引脚作为时钟源


计数器预分频器可以在 TIMERx_CI0/ TIMERx_CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[4:0]为 0x5~0x7 和 0xB。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x1~0x4。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 13-72. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/e453ef1adf86a955aa5ec3e75f5f3c063b7cc0ded49fbb9270c85ee9fc17b463.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数。如果设置了重复计数器，在（TIMERx_CREP0+1）次上溢后产生更新事件，否则在每次上溢时都会产生更新事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

13-73. PSC=0/2 和 13-74. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 13-73. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/cea6a64b3613f00d5e5ed380db56a189cef6a0ce498a51cb31c10ef2c9b0a837.jpg)



图 13-74. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/5375cd9b9d9916fd139794c11f52ece9b812cad852aa9a805eb0ca9559f71b75.jpg)


## 向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数并产生下溢事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

13-53. PSC=0/2 和 13-54. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 13-75. 向下计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/e19219b2471505130b8d3a055f90d60c9e1366b2b23a9b8179c8331e6bd890fb.jpg)



图 13-76. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c416dfa8dc0be92d406858338f704c939a9c87b9e7655da6c6e40ba9874bc4ee.jpg)


## 中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（TIMERx_CAR-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。计数方向被硬件自动更新。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1，然而 CHxIF 位置 1 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 13-55. 。如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

13-55. 给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为


图 13-77. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/98c96483516133649990e5d967c19418736acd87f30ab5cf354df48b9714c467.jpg)


## 重复计数器

重复计数器是用来在（N+1）个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP0寄存器的CREP0的值。向上计数模式下，重复计数器在每次计数器上溢时递减；向下计数模式下，重复计数器在每次计数器下溢时递减；在中央对齐模式下，重复计数器在计数器上溢和下溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP0 寄存器中 CREP0 的值并产生一个更新事件。

新写入的 CREP0 值将在下一次更新事件到来时生效。当 CREP0 的值为奇数，并且计数器在中央对齐模式下计数时，更新事件发生在上溢或下溢取决于写入的 CREP0 值何时生效。如果在写入奇数到 CREP0 寄存器后由软件生成更新事件（UPG 位置 1），则在下溢时产生更新事件。如果在写入奇数到 CREP0 寄存器后下一个更新事件发生在上溢，此后将在上溢时产生更新事件。


图 13-78. 中央计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/6a157c6168f800d9e1eed0bc52989a608f8a3693b1c65c64e2480ee657c962d6.jpg)



图 13-79. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/6f8167323087acd2272b2231c9cb5e375694b62c9af1755db3d5803046035b51.jpg)



图 13-80. 在向下计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/4d99527a69d41d38dbec1705c7c5a9d18da1e87a2ad8647eae968c181ec5a05a.jpg)


## 捕获/比较通道

通用定时器 L3 拥有 3 个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

当通道用于输入时，通道 x 和多模式通道 x 可独立进行输入捕获；当通道用于比较输出时，通道 x和多模式通道 x 可输出独立和互补。

##  输入捕获模式

当 MCHxMSEL=2’b00（独立模式）时，通道 x 和多模式通道 x 才可以独立进行输入捕获。

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV/ TIMERx_MCH0CV（x=0,1）寄存器会捕获计数器当前的值，同时 CHxIF${ \mathsf { M C H } } 0 | \mathsf { F } \ ( \mathsf { x } { = } 0 , 1 )$ 位置 1，如果 ${ \mathsf { C H } } { \mathsf { x } } { \mathsf { I E } } / { \mathsf { M C H } } { \mathsf { 0 } } { \mathsf { I E } } = 1 { \mathsf { \Omega } } ( { \mathsf { x } } { \mathsf { = } } 0 , 1 { \mathsf { \Omega } } )$ ），则产生相应的通道中断。


图 13-81. 通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/f0124acfe1b48fc49aeca0c778bd34b7fe6b89cfd9c8f89903559acb4bfc78a2.jpg)



图 13-82. 多模式通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c40d31dbb49d1eccc6b01346b62a76676fac18ca7d53fd7f33f9a2e059aba5f5.jpg)



通道输入信号 CIx/ MCIx 有两种选择，一种是 TIMERx_CHx/ TIMERx_MCHxCV 信号，另一种是TIMERx_CH0，TIMERx_CH1 和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。


通道输入信号 CIx/ MCIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP/ MCHxP、MCHxFP选择使用上升沿或者下降沿。配置 CHxMS/ MCHxMS，可以选择其他通道的输入信号或内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV/ TIMERx_MCHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0 寄存器中 CHxCAPFLT 位和 TIMERx_MCHCTL0 寄存器中 CHxMCAPFLT）：

根据输入信号和请求信号的质量，配置相应的 CHxCAPFLT/ CHxMCAPFLT 位。

第二步：边沿选择（TIMERx_CHCTL2 寄存器中 CHxP 和 MCHxP 位，TIMERx_MCHCTL2 寄存器中 MCHxFP[1:0]位域）：

配置 CHxP和 MCHxP 位或 MCHxFP 位域选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0 寄存器中 CHxMS、TIMERx_MCHCTL0 寄存器中MCHxMS）：

一 旦 通 过 配 置 CHxMS/ MCHxMS 选 择 输 入 捕 获 源 ， 必 须 确 保 通 道 配 置 在 输 入 模 式（CHxMS!=0x000 或 MCHxMS!=0x000），而且 TIMERx_CHxCV/TIMERx_MCHxCV 寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN 寄存器中 CHxIE、CHxDEN 位和 MCHxIE、MCHxDEN位）：

使能相应中断，可以获得中断和 DMA请求。

第五步：捕获使能（TIMERx_CHCTL2 寄存器中 CHxEN/ MCHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV/ TIMERx_MCHxCV 被设置成当前计数器的值，CHxIF/ MCHxIF 位置 1。如果 CHxIF/ MCHxIF 位已经为 1，则 CHxOF/ MCHxOF 位置 1。根据TIMERx_DMAINTEN 寄存器中 CHxIE、CHxDEN 位和 MCHxIE、MCHxDEN 位的配置，相应的中断和 DMA请求会被提出。

直接产生：软件设置 CHxG 位，会直接产生中断和 DMA 请求。

输入捕获模式也可用来测量 TIMERx_CHx 和 TIMERx_MCHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 3’b001，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 3’b010，选择通道1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV 寄存器测量 PWM 的周期值，TIMERx_CH1CV 寄存器测量 PWM 占空比值。

 输出比较模式

13-83. MCHxMSEL = 2’00 x=0 ， 13-84.MCHxMSEL = 2’11 x=0 和 13-85. x=1 给出了通道的输出比较逻辑。


图 13-83. 输出比较逻辑（当 MCHxMSEL = 2’00 时，x=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/dbe816641ab33f4f419cad46337b43ff83d74a52aec4b2c0e4aba77b26edf044.jpg)



图 13-84. 输出比较逻辑（当 MCHxMSEL = 2’11 时，x=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/315732712a4130237d96f53c2ca914bc7815a78aef7c508fc12c1cd6386eabf6.jpg)



图 13-85. 输出比较逻辑（x=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/fb25ba71e0b0df594056e0256178f6f1dbfae663e3af6fc0dd04bd764a5331a1.jpg)


通道输出信号 CHx_O/MCHx_O 与 OxCPRE/ MOxCPRE 信号（详情请见 ）的关系描述如下（OxCPRE/ MOxCPRE 信号高电平有效）：

当MCHxMSEL=2’b00（TIMERx_CTL2寄存器中），MCHx_O输出与CHx_O输出相互独立。CHx_O 输 出 电 平 取 决 于 OxCPRE 信 号 、 CHxP 位 和 CHxEN 位 （ 详 细 内 容 参 考TIMERx_CHCTL2寄存器）。MCHx_O输出电平取决于MOxCPRE信号、MCHxFP[1:0]位和MCHxEN位（详细内容参考TIMERx_CHCTL2和TIMERx_MCHCTL2寄存器）。请参考 13-83.MCHxMSEL = 2’00 x=0 。

当MCHxMSEL=2’b11，MCHx_O输出和CHx_O输出互补。CHx_O/MCHx_O输出电平取决于OxCPRE信号、CHxP/ MCHxP位和CHxEN/ MCHxEN位。请参考 13-84.MCHxMSEL = 2’11 x=0 。

例如（MCHx_O 输出与 CHx_O 输出相互独立）：

1）当设置 CHxP=0（CHx_O 高电平有效，与 OxCPRE 输出极性相同）、CHxEN=1（CHx_O 输出使能）时：

若 OxCPRE 输出有效（高）电平，则 CHx_O 输出有效（高）电平；

若 OxCPRE 输出无效（低）电平，则 CHx_O 输出无效（低）电平。

2）当设置 MCHxP=1（MCHx_O 低电平有效，与 MOxCPRE 输出极性相反）、MCHxEN=1（MCHx_O输出使能）时：

若 MOxCPRE 输出有效（高）电平，则 MCHx_O 输出有效（低）电平；

若 MOxCPRE 输出无效（低）电平，则 MCHx_O 输出无效（高）电平。

当 MCHxMSEL=2’b11，CHx_O 和 MCHx_O 同时输出时，CHx_O 和 MCHx_O 的具体输出情况还与 TIMERx_CCHP0 寄存器中的相关位（ROS、IOS、POE 和 DTCFG 等位）有关。详情请见互补输出。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 TIMERx_CHxCV/ TIMERx_MCHxCV 寄存器与计数器的值匹配时，根据CHxCOMCTL/ MCHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 TIMERx_CHxCV/ TIMERx_MCHxCV 寄存器的值匹配时，CHxIF/ MCHxIF 位被置 1，如果 CHxIE/ MCHxIE = 1 则会产生中断，如果 CHxDEN/ MCHxDEN =1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

 设置CHxCOMSEN/ MCHxCOMSEN位来配置输出比较影子寄存器；

 设置CHxCOMCTL/ MCHxCOMCTL位来配置输出模式（置高电平/置低电平/翻转）；

 设置CHxP/ MCHxP/ MCHxFP位来选择有效电平的极性；

 设置CHxEN/MCHxEN使能输出。

第三步：通过 CHxIE/ MCHxIE/ CHxDEN/ MCHxDEN 位配置中断/DMA 请求使能。

第四步：通过 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器配置输出比较时基：

TIMERx_CHxCV/ TIMERx_MCHxCV 可以在运行时根据你所期望的波形而改变。

第五步：设置 CEN 位使能定时器。

13-86. 显示了三种比较输出模式：翻转/置高电平/置低电平，CAR=0x63,CHxVAL=0x3。


图 13-86. 三种输出比较模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/71d27589e348313b7ee59d335f9604737d9da9368210ede062cd35347a33556b.jpg)


## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL/ MCHxCOMCTL 为 4’b0110，PWM 模式 1 是配置 CHxCOMCTL/ MCHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和TIMERx_CHxCV/ TIMERx_MCHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV/ TIMERx_MCHxCV寄存器值决定。 13-15. EAPWM 显示了 EAPWM的输出波形和中断。

CAPWM 的 周 期 由 （ 2*TIMERx_CAR 寄 存 器 值 ） 决 定 ， 占 空 比 由 （ 2*TIMERx_CHxCV/TIMERx_MCHxCV 寄存器值）决定。 13-16. CAPWM 显示了 CAPWM 的输出波形和中断。

当计数器向上计数时，在 PWM0 模式下（CHxCOMCTL/ MCHxCOMCTL =4’b0110），如果TIMERx_CHxCV/ TIMERx_MCHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为有效电平；PWM1 模式下（CHxCOMCTL/ MCHxCOMCTL=4’b0111），如果 TIMERx_CHxCV/TIMERx_MCHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为无效电平。


图 13-87. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/5dd20a7c5affadc6cdb6cbbf58b61f772f4ff93ec217e2bc8392c04c7cfe45e7.jpg)



图 13-88. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/1b66f9398e7a632650f17d4d1e9701fc06216a1e0fe7eca49dea6242e31fc548.jpg)


## 复合 PWM 模式

在复合 PWM 模式中 $( { \mathsf { C H x C P W M E N } } = 1 ^ { \prime } { \mathsf { b 1 } } , { \mathsf { C H x M S } } [ 2 : 0 ] = 3 ^ { \prime } { \mathsf { b 0 0 0 } } { \mathit { \# } } \mathbb { I } { \mathsf { C H x C O M C T L } } = 4 ^ { \prime } { \mathsf { b 0 1 } } 0 { \mathsf { 0 2 } } .$ 4’b0111），通道 x（x=0..1）上的 PWM 输出信号由 CHxVAL 和 CHxCOMVAL_ADD 位确定。

如果 $\mathsf { C H x C O M C T L } = 4 ^ { \prime } 6 0 1 1 0 \mathrm { ~ ( P W M }$ 模式 0）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL= 4’b0111（PWM 模式 1）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为低。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为高。

如果 CHxCOMCTL =4’b0111（PWM 模式 1）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL=4’b0110（PWM 模式 0）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为高。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为低。

当 CHxVAL 或 CHxCOMVAL_ADD = 0 / CARL ， 通 道 输 出 被 进 行 了 特 殊 处 理 ， 通 过TIMERx_CHCTL2 寄存器的 CHxPERFOREN 位置位，强制 OxCPRE 输出高电平或低电平（根据所选复合 PWM 模式确定）。

PWM 的周期取决于（CARL + 0x0001），PWM 脉冲宽度可以下 13-12. PWM 计算。


表 13-12. 复合 PWM 脉冲宽度


<table><tr><td>条件</td><td>模式</td><td>PWM脉冲宽度</td></tr><tr><td rowspan="2">CHxVAL &lt; CHxCOMVAL_ADD ≤ CARL</td><td>PWM模式0</td><td>(CARL + 0x0001) +(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &lt; CHxVAL ≤ CARL</td><td>PWM模式0</td><td>(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM模式1</td><td>(CARL + 0x0001) +(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">(CHxVAL = CHxCOMVAL_ADD ≤ CARL)或 (CHxVAL &gt; CARL &gt; CHxCOMVAL_ADD)</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>100%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>0%</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &gt; CARL &gt; CHxVAL</td><td>PWM模式0(向上计数)或 PWM模式1(向下计数)</td><td>0%</td></tr><tr><td>PWM模式0(向下计数)或 PWM模式1(向上计数)</td><td>100%</td></tr><tr><td>(CHxVAL&gt;CARL)且 (CHxCOMVAL_ADD &gt; CARL)</td><td>-</td><td>CHx_O输出保持</td></tr></table>


当计数器计数到 CHxVAL，CHxIF 位置 1 且如果 CHxIE=1 通道 x 产生中断，如果 CHxDEN=1，则产生 DMA 请求。当计数器计数到 CHxCOMVAL_ADD 时，CHxCOMADDIF 位置 1（该中断标志位只在复合 PWM 模式有效，CHxCPWMEN=1），如果 CHxCOMADDIE = 1 通道 x 附加比较中断产生（只有中断产生，没有 DMA 请求响应）。


根据 CHxVAL，CHxCOMVAL_ADD 和 CARL 之间的关系，可以分为四种情况：

## 1） CHxVAL < CHxCOMVAL_ADD，CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。


图 13-89. 通道 x 输出 PWM（CHxVAL < CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/73b2166b2984079e52787753099d2df4ad6f53d9389d6ad71362912dcb2c8688.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/134dc892584091ec56558d678fc73decaee43050fa3021b1422da48e88544e2b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/261153d6c667f787a26deb896195ecda4423262ff995413879f1f78ffe837b0e.jpg)



2） CHxVAL = CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13-90. 通道 x 输出 PWM（CHxVAL = CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/21465860c4072f33e4a22ec2850087f4143c740b6ca0a959a8126f8ed5b1f6f9.jpg)



3） CHxVAL > CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 13-91. 通道 x 输出 PWM（CHxVAL > CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/2aa41ab1530fd2fcdd728fca829971b8808b04b8325317be822b29aee63c3136.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/0de9831c1d2431360abd5f2108b95eb18908a93d3bb0fc64a31985693d05646b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/e3a6c68f451b33d88785121353c59d07c77e8dbcafc8692c2d7137609e959427.jpg)



4） CHxVAL或CHxCOMVAL_ADD值大于CARL。



图 13-92. 通道 x 输出 PWM（CHxVAL 或 CHxCOMVAL_ADD > CARL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/668db0c00f63c07f02e3f8fc5fc719005cff9b2b5a1a450f93d6dea889143630.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/cb054cd9b5593cd8289a0f214930fb9b7042308cc5ca7c6bcfb97ea740b0ea7f.jpg)



复合 PWM 模式支持不修改周期只修改占空比的 PWM 信号的生成。 13-93. x PWMCHxCOMVAL_ADD 显示 PWM 输出和中断波形。


在某些情况下，CHxCOMVAL_ADD 的匹配事件可以发生在下一个计数周期（CHxCOMVAL_ADD值在计数器到达 CHxVAL 值之后被写入，且 CHxCOMVAL_ADD 值小于或者等于 CHxVAL 值）。


图 13-93. 通道 x 输出 PWM 占空比随着 CHxCOMVAL_ADD 值而改变


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/f045ba4a4c1b34945b648d841a5bcd054d3736d2f19b21a84d740e62daa2d731.jpg)


如果多个通道配置为复合 PWM 模式，可以为每对通道 x 的匹配边沿设定一个偏移量（相对于其它通道）。这种特性在产生照明 PWM 控制信号时非常有用，因为在这种情况下，希望彼此边缘不重合，以消除噪声的产生。CHxVAL 寄存器值是 PWM脉冲相对于计数器周期开始的偏移。

## 输出匹配脉冲选择

当发生匹配事件时，CHx_O（x=0，1）的输出由 CHxCOMCTL[3:0]（x=0，1）位设置，通过配置CHxOMPSEL[1:0]（x=0，1）位，可选择 CHx_O（x=0，1）的输出信号正常或者脉冲。

当匹配事件发生时，CHxOMPSEL[1:0]（x=0，1）用于选择 OxCPRE 信号输出（驱动 CHx_O）：

 CHxOMPSEL = 2’b00，OxCPRE信号根据CHxCOMCTL[3:0]位的配置正常输出；

CHxOMPSEL = 2’b01，只有在计数器向上计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b10，只有在计数器向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；

 CHxOMPSEL = 2’b11，无论计数器向上计数还是向下计数，发生匹配事件时，OxCPRE信号输出一个脉冲，且脉冲宽度为一个CK_TIMER时钟周期；


图 13-94. 边沿对齐模式下 CHx_O 输出脉冲（CHxOMPSEL≠2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/9436aacb4e2aece62eb9ae242331a089a8e6c1926c56421bf58e1d1d70d60214.jpg)



图 13-95. 中央对齐模式下 CHx_O 输出脉冲（CHxOMPSEL≠2’b00）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c362f08533da7485dabab09a877254d1bc951de19a749cdd373b3d6eef8c747e.jpg)


## 通道输出参考信号

如 13-83. MCHxMSEL = 2’00 x=0 ， 13-84.MCHxMSEL = 2’11 x=0 和 13-85. x=1 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前将产生一个中间信号，即 OxCPRE 或 MOxCPRE 信号（通道 x或多模式通道 x 参考信号）。

OxCPRE 和 MOxCPRE 信号有若干类型的输出功能，通过配置 CHxCOMCTL 位定义 OxCPRE 信号类型，通过配置 MCHxCOMCTL 位定义 MOxCPRE 信号类型。

下面以 OxCPRE 为 例 进 行 说 明 ， 设 置 CHxCOMCTL=0x00 可 以 保 持 原 始 电 平 ； 设 置CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06 或0x07 可以配置 PWM 模式 0/PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 互补输出

CHx_O 和 MCHx_O 的输出具有两种情况：

 MCHxMSEL=2’b00：MCHx_O输出独立于CHx_O输出。

 MCHxMSEL=2’b11：MCHx_O输出与CHx_O输出互补，且MCHx_O的输出不由CHxMOMCTL位配置。

当 CHx_O 和 MCHx_O 输出互补时，这两个信号不能同时有效。TIMERx 的 1 对通道具有此功能。互补信号 CHx_O 和 MCHx_O 是由一组参数来决定：TIMERx_CHCTL2 寄存器中的 CHxEN 和MCHxEN 位，TIMERx_CCHP0 寄存器中和 TIMERx_CTL1 寄存器中的 POEN、ROS、IOS、ISOx和 ISOxN 位。输出极性由 TIMERx_CHCTL2 寄存器中的 CHxP 和 MCHxP 位来决定。

当 CHx_O 和 MCHx_O 的输出互补时，有三种输出情况：输出使能、输出关闭状态和输出禁能，具体情况可参考 13-13. MCHxMSEL=2’b11 。


表 13-13. 由参数控制的互补输出表（MCHxMSEL=2’b11）


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>POEN</td><td>POEN</td><td>POEN</td><td>POEN</td><td>CHx_O</td><td>MCHx_O</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / MCHx_O = LOWCHx_O / MCHx_O 输出禁能(1)</td></tr><tr><td>1</td><td colspan="2" rowspan="3">CHx_O/MCHx_O输出关闭状态(2):通道先输出无效电平:CHx_O = CHxP,MCHx_O = MCHxP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,MCHx_O = ISOxN(3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/MCHx_O输出关闭状态:通道先输出无效电平:CHx_O = CHxP,MCHx_O = MCHxP);如果死区产生时钟未失效,在死区时间之后:CHx_O = ISOx,MCHx_O = ISOxN</td></tr><tr><td rowspan="8">1</td><td rowspan="4">0</td><td rowspan="8">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/MCHx_O = LOWCHx_O/MCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>MCHx_O=OxCPRE<eq>\oplus</eq>(4)MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE<eq>\oplus</eq>CHxPCHx_O输出使能</td><td>MCHx_O = LOWMCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE<eq>\oplus</eq>CHxPCHx_O输出使能</td><td>MCHx_O=(!OxCPRE)(5)<eq>\oplus</eq>MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="4">1</td><td rowspan="2">0</td><td>0</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O=OxCPRE<eq>\oplus</eq>MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE<eq>\oplus</eq>CHxPCHx_O输出使能</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE<eq>\oplus</eq>CHxPCHx_O输出使能</td><td>MCHx_O=(!OxCPRE)<eq>\oplus</eq>MCHxPMCHx_O输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / CHx_ON 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / CHx_ON 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；


（3） 详情见中止模式章节。

（4） ⊕：异或操作；

（5） (!OxCPRE)：OxCPRE 信号的互补信号。

## 死区时间插入

设置 MCHxMSEL=2’b11，CHxEN 和 MCHxEN 为 1’b1，同时设置 POEN=1，就可以使能死区插入功能。DTCFG 位域定义了死区时间，死区时间对所有通道有效。死区时间设置的细节请参考0 TIMERx_CCHP0 。

死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM0 模式，当通道 x 匹配发生时（TIMERx 计数器=TIMERx_CHxCV），OxCPRE 翻转。在13-96. 中的 A 点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而 MCHx_O 信号立刻变为低电平。同样，在 B点，计数器再次匹配（TIMERx计数器=TIMERx_CHxCV），OxCPRE 信号被清 0，CHx_O 信号被立即清零，MCHx_O 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。有时会有一些死角事件发生，例如：如果死区延时大于或者等于 CHx_O 信号的占空比，CHx_O 信号一直为无效值，如 13-96.间的互补输出所示。


图 13-96. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c207f2c4d7b252695fad07d4fbddad41d4f075a029f0e031af5fe53d24f05273.jpg)


## 中止功能

当 MCHxMSEL = 2’b11（MCHx_O 的输出不使用 CHxMOMCTL 位配置）时，MCHx_O 输出与CHx_O 输出互补。在这种情况下，CHx_O 和 MCHx_O 信号不能同时设置为有效电平。

通用 L3 定时器具有 BREAK 中止功能。可以通过将 TIMERx_CCHP0 寄存器中的 BRKEN 位置 1来使能。中止输入极性由 TIMERx_CCHP0 寄存器中的 BRKP位配置，电平有效。

使用 BREAK 功能时，CHx_O 和 MCHx_O 信号的输出电平由以下位控制：TIMERx_CCHP0 寄存器的 POEN、IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。

中止事件是所有源逻辑或运算的结果。中止功能可以处理三种类型的事件源：

 外部信号源：来自BRKIN0输入；

 系统源： LVD锁定事件，Cortex®-M33锁定事件或SRAM奇偶校验错误事件；

 片上外设源：比较器输出。

BREAK 中止事件也可以由软件置位 TIMERx_SWEVG 寄存器中的 BRKG 位产生。

如 13-97. BREAK 所示，BRKIN0 可以从 TRIGSEL 模块选择 GPIO 引脚，具体可参考 TIMER15_BRKIN TRIGSEL_TIMER15BRKIN 和 TIMER16_BRKINTRIGSEL_TIMER16BRKIN 。


图 13-97. BREAK 中止功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/93f28e7abd44a23b345b19aaf26132610c9168ebcf89e7178df4ba38cfe7d2cc.jpg)


BREAK 可用于处理系统源、片上外设和外部输入信号源的故障，当发生 BREAK 中止事件时，输出强制为无效电平，或在死区持续时间之后，输出将以预定的电平（有效或无效）强制输出。

当 MCHxMSEL = 2’b11 且发生 BREAK 中止事件时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 MCHx_O 的输出由 TIMERx_CTL1 寄存器中的 ISOx 位和 ISOxN 位确定。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。当 IOS=1 时，通道输出情况如 13-98.BREAK IOS=1 所示，首先通道互补输出为复位状态，然后死区时间发生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx 和ISOxN 位配置。


图 13-98. 通道响应 BREAK 中止输入（高电平有效）时，输出信号的行为（IOS=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/a957b83c83dba11334be23ca8a590aa2a1d975ff4c5b4b1f87aee8907bbb69e2.jpg)



发生中止事件时，TIMERx_INTF 寄存器的 BRKIF 位被置 1。如果 BRKIE=1，中断产生。


## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式等，可以通过设置SYSCFG_TIMERxCFG(x=15,16)寄存器中的 TSCFGy[4:0] (y=3..6)位域来确定，具体的输入触发源可以通过 TSCFGy[4:0] (y=3..6)位域的值来选择。


表 13-14. 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[4:0]y=3:复位模式y=4:暂停模式y=5:事件模式y=6:外部时钟模式0</td><td>TSCFGy[4:0]00000: Mode disable00001: ITI000010: ITI100011: ITI200100: ITI300101: CI0F_ED00110: CI0FE000111: CI1FE110010: MCI0FEM0</td><td>如果触发源是CIxFEx(x=0,1)或者MCIxFEMx(x=0),配置CHxP、MCHxP和MCHxFP来选择极性和反相。</td><td>触发源ITIx,滤波和预分频不可用触发源CIx/MCIx,配置CHxCAPFLT/MCHxCAPFLT设置滤波,分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[4:0]5'b00001,选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图13-99. 复位模式下的控制电路</td></tr><tr><td>例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[4:0]=5'b00110,选择CI0FE0为触发源</td><td>TIOS=0(非异或)[MCHOP=0,CHOP=0]CI0FE0不反相,在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td></td><td colspan="4">图13-100.暂停模式下的控制电路</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[4:0]=5'b01000,选择ETIFP为触发源</td><td>ETP=0没有极性改变</td><td>ETPSC=1,2分频ETFC=0,无滤波</td></tr><tr><td colspan="4">图13-101.事件模式下的控制电路</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，可使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL/ MCHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE/ MOxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。

单脉冲模式也同样适用于复合 PWM 模式（CHxCPWMEN = 1’b1 和 CHxMS[2:0] = 3’b000）。


图 13-102. 单脉冲模式，TIMERx_CHxCV = 0x04 TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/b68957c7114337848c04fdaec73405a8fbe606b932e62672ba81a31abefeb861.jpg)


## 定时器互连

参考 TIMERx, x=0, 7 。

## 计数器同步、初始方向和值刷新

参考 TIMERx, x=0, 7 。

## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA 请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4, DMATA+0x8, DMATA+0xc 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL1 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

