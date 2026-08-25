## 23.3. 通用定时器 L3（TIMERx, x = 14）

## 23.3.1. 简介

通用定时器 L3（TIMER14）是 3 通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。通用定时器 L3 含有一个 16 位无符号计数器。

通用定时器 L3 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器

通用定时器 L3 包含了一个死区时间插入模块，非常适合电机控制。

定时器和定时器之间是相互独立，但是他们可以被同步在一起形成一个更大的定时器，这些定时器的计数器一致地增加。

## 23.3.2. 主要特征

 总通道数：3；

 计数器宽度：16位；

 时钟源可选：内部时钟，内部触发，外部输入；

 计数模式：向上计数；

 可编程的预分频器：16位，运行时可以被改变；

 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

 可编程的死区时间；

 自动重装载功能；

 可编程的计数器重复功能；

 中止输入功能：BREAK0；

 中断输出和DMA请求：更新事件，比较/捕获事件和中止事件；

 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

 定时器主-从管理。

## 23.3.3. 结构框图

23-92. L3 提供了通用定时器 L3 的内部配置细节


图 23-92. 通用定时器 L3结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/50836280917f43986af721817084db1ce8e02ff94aa752bc791875fbe8ffe6ba.jpg)


## 23.3.4. 功能描述

## 时钟源选择

通用定时器 L3 可以由内部时钟源 TIMER_CK 或者由 SYSCFG_TIMERxCFG(x = 14)寄存器中的TSCFGy[4:0] (y = 3..7, 15)位域。

当 $\mathsf { I S Y S C F G \_ T I M E R x C F G } ( \mathsf { x } = 1 4 )$ 寄存器中的 $\mathsf { S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } { \mathsf { b 0 0 0 0 0 } } ( \mathsf { y } = 3 . 7 , \ 1 5 )$ ，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 $\mathsf { S Y S C F G \_ T I M E R x C F G } ( \mathsf { x } = 1 4 )$ 寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } \mathsf { b 0 0 0 0 0 } \ ( \mathsf { y } = 3 . 7 , \ 1 5 )$ ，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER

如果 ${ \mathsf { S Y S C F G } } _ { - } { \mathsf { T I M E R x C F G } } ( \mathsf { x } = 1 4 )$ 寄存器中的 TSCFG6[4:0]位域设置为非零值，预分频器被其他时钟源驱动，具体在下文说明。当 $\mathsf { T S C F G y } [ 4 ; 0 ] ( \mathsf { y } = 3 , 4 , 5 , 7 )$ 被设置为非零值时，计数器预分

频器时钟源由内部时钟 TIMER_CK 驱动。


图 23-93. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/19df0c2c68e5c58ea7c5cefa67db2f46e149710bf6bfc967a881b8bf892cc7f2.jpg)


 TSCFG6[4:0]设置为非零值（外部时钟模式0），定时器选择外部输入引脚作为时钟源

计数器预分频器可以在 CI0 / CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x5 ~ 0x7 来选择。

计数器预分频器也可以在内部触发信号 ITI0 ~ 10 / ITI14 的上升沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x1 ~ 0x4，0x9 ~ 0xF 和 0x13 来选择。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 23-94. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/c9b0c8ad2d7d57c5ce234b8d10595709c2b064ce2fac741d299c93c2cba21c2c.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数。如果设置了重复计数器，在（TIMERx_CREP0/1 + 1）次上溢后产生更新事件，否则在每次上溢时都会产生更新事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

23-95. PSC=0 / 2 和 23-96. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 23-95. 向上计数时序图，PSC=0 / 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/1c6e194d247a97e2a3a9489a23b103c53e45e52b1723668feae5f3b4a9136e01.jpg)



图 23-96. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/8f69bb1e6510c16a5bbca5101d94f3667f0ea347461b40fc613d12c47ec94a96.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/3b616d1f7a864c5f29cf7e6cd0a0ed512ea802935ac37b65354621cf2483968c.jpg)


## 重复计数器

通用L3定时器有两个重复寄存器TIMERx_CREP0 / 1，可通过配置TIMERx_CFG寄存器中的CREPSEL位来选择。其中TIMERx_CREP0寄存器中的CREP0[7:0]是8位的，TIMERx_CREP1寄存器中的CREP1[31:0]是32位，用户可根据需求选择使用。

重复计数器是用来在 N+1 个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP0/1 寄存器的 CREP0/1。向上计数模式下，重复计数器在每次计数器上溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP0/1 寄存器中 CREP0/1 的值并产生一个更新事件。


图 23-97. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/df954aea750f0160121cb591c54d9575bfbcabba7fc61de66c58632bbcaa25f5.jpg)


## 捕获/比较通道

通用定时器 L3 拥有 3 个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

当通道用于输入时，通道 x 和多模式通道 x 可独立进行输入捕获；当通道用于比较输出时，通道 x和多模式通道 x 可输出独立和互补。

##  输入捕获模式

当 MCHxMSEL=2’b00（独立模式）时，通道 x 和多模式通道 x 才可以独立进行输入捕获。

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV / TIMERx_MCHxCV（x = 0, 1）寄存器会捕获计数器当前的值，同时 CHxIF /MCHxIF（x = 0,1）位置 1，如果 CHxIE/ MCHxIE =1（x = 0, 1），则产生相应的通道中断。


图 23-98. 通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/de434c0bfa4075dc7444f7b11f7d8f48e95b7e4d698eb383dcaf00ecc38090b4.jpg)



图 23-99. 多模式通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/8434d13b238dd76f70bc87d899bf3d22a9bc211d9b3ed508ef703ab424451793.jpg)



通道输入信号 CIx/ MCIx 有两种选择，一种是 TIMERx_CHx/ TIMERx_MCHxCV 信号，另一种是TIMERx_CH0，TIMERx_CH1 和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。


通道输入信号 CIx/ MCIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP/ MCHxP、MCHxFP选择使用上升沿或者下降沿。配置 CHxMS/ MCHxMS，可以选择其他通道的输入信号或内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV/ TIMERx_MCHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT位和TIMERx_MCHCTL0寄存器中CHxMCAPFLT）：

根据输入信号和请求信号的质量，配置相应的CHxCAPFLT/ CHxMCAPFLT位。第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP和MCHxP位，TIMERx_MCHCTL2寄存器中MCHxFP[1:0]位域）：

配置CHxP和MCHxP位或MCHxFP位域选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS、TIMERx_MCHCTL0寄存器中MCHxMS）：

一旦通过配置CHxMS/ MCHxMS选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x000或MCHxMS!=0x000），而且TIMERx_CHxCV/TIMERx_MCHxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中CHxIE、CHxDEN位和MCHxIE、MCHxDEN位）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中CHxEN/ MCHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV/ TIMERx_MCHxCV被设置成当前计数器的值，CHxIF/ MCHxIF位置1。如果CHxIF/ MCHxIF位已经为1，则CHxOF/ MCHxOF位置1。根据TIMERx_DMAINTEN寄存器中CHxIE、CHxDEN位和MCHxIE、MCHxDEN位的配置，相应的中断和DMA请求会被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

输入捕获模式也可用来测量 TIMERx_CHx 和 TIMERx_MCHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 3’b001，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 3’b010，选择通道1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV 寄存器测量 PWM 的周期值，TIMERx_CH1CV 寄存器测量 PWM 占空比值。

##  输出比较模式

23-100. MCHxMSEL = 2’b00 x = 0 ， 23-101.MCHxMSEL = 2’b11 x = 0 和 23-102. x = 1 给出了通道的输出比较逻辑。


图 23-100. 输出比较逻辑（当 MCHxMSEL = 2’b00 时，x = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/383ea03d6d98f3320b714366776f88124b1f452e6abeecb799ac60be7e508047.jpg)



图 23-101. 输出比较逻辑（当 MCHxMSEL = 2’b11 时，x = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/8711d19b3d54c72b618594b5f44c1a0ed9b7b103b8d3ace1be8794ae48d9b59b.jpg)



图 23-102. 输出比较逻辑（x = 1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/dc23caa8b157a63b8563e9c7a71349236ea59815dbf7b0f2fa8bd66a1728f32a.jpg)


通道输出信号CHx_O / MCHx_O与OxCPRE / MOxCPRE信号（详情请见 ）的关系描述如下（OxCPRE / MOxCPRE信号高电平有效）：

当MCHxMSEL = 2’b00（TIMERx_CTL2寄存器中），MCHx_O输出与CHx_O输出相互独立。CHx_O 输 出 电 平 取 决 于 OxCPRE 信 号 、 CHxP 位 和 CHxEN 位 （ 详 细 内 容 参 考TIMERx_CHCTL2寄存器）。MCHx_O输出电平取决于MOxCPRE信号、MCHxFP[1:0]位和MCHxEN位（详细内容参考TIMERx_CHCTL2和TIMERx_MCHCTL2寄存器）。请参考23-100. MCHxMSEL = 2’b00 x = 0 。

当MCHxMSEL = 2’b11，MCHx_O输出和CHx_O输出互补。CHx_O/MCHx_O输出电平取决于OxCPRE信号、CHxP/ MCHxP位和CHxEN/ MCHxEN位。请参考 23-101.MCHxMSEL = 2’b11 x = 0 。

例如（MCHx_O输出与CHx_O输出相互独立）：

1）当设置CHxP=0（CHx_O高电平有效，与OxCPRE输出极性相同）、CHxEN=1（CHx_O输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_O输出有效（高）电平；

若OxCPRE输出无效（低）电平，则CHx_O输出无效（低）电平。

2）当设置MCHxP=1（MCHx_O低电平有效，与MOxCPRE输出极性相反）、MCHxEN=1（MCHx_O输出使能）时：

若MOxCPRE输出有效（高）电平，则MCHx_O输出有效（低）电平；

若MOxCPRE输出无效（低）电平，则MCHx_O输出无效（高）电平。

当MCHxMSEL=2’b11，CHx_O和MCHx_O同时输出时，CHx_O和MCHx_O的具体输出情况还与TIMERx_CCHP0寄存器中的相关位（ROS、IOS、POE和DTCFG等位）有关。详情请见 。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 TIMERx_CHxCV / TIMERx_MCHxCV 寄存器与计数器的值匹配时，根据CHxCOMCTL/ MCHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 TIMERx_CHxCV / TIMERx_MCHxCV 寄存器的值匹配时，CHxIF / MCHxIF 位被置 1，如果 CHxIE/ MCHxIE = 1 则会产生中断，如果 CHxDEN / MCHxDEN =1 则会产生 DMA 请求。

配置步骤如下：

## 第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

 设置CHxCOMSEN / MCHxCOMSEN位来配置输出比较影子寄存器；

 设置CHxCOMCTL / MCHxCOMCTL位来配置输出模式（置高电平/置低电平/翻转）；

 设置CHxP / MCHxP / MCHxFP位来选择有效电平的极性；

 设置CHxEN / MCHxEN使能输出。

第三步：通过CHxIE / MCHxIE/ CHxDEN/ MCHxDEN位配置中断/DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

TIMERx_CHxCV / TIMERx_MCHxCV可以在运行时根据你所期望的波形而改变。

第五步：设置CEN位使能定时器。

23-103. 显示了三种比较输出模式：翻转/置高电平/置低电平， $\mathsf { C A R } { = } 0 \times 6 3$ ${ \mathsf { C H x V A L } } = 0 \times 3$ 。


图 23-103. 三种输出比较模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/6ab95e31a3440a614d76bf6a811cc26950717c74382aef5fd14e2e14e884f6fd.jpg)


## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL/ MCHxCOMCTL 为 4’b0110，PWM 模式 1 是配置 CHxCOMCTL/ MCHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和TIMERx_CHxCV/ TIMERx_MCHxCV 寄存器的值，输出 PWM 波形。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV/ TIMERx_MCHxCV寄存器值决定。 23-104. PWM 显示了 EAPWM 的输出波形和中断。

当计数器向上计数时，在PWM0模式下（CHxCOMCTL/ MCHxCOMCTL =4’b0110），如果TIMERx_CHxCV/ TIMERx_MCHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为有效电平；PWM1模式下（CHxCOMCTL/ MCHxCOMCTL=4’b0111），如果TIMERx_CHxCVTIMERx_MCHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为无效电平。


图 23-104. PWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/bc603150a36ba3776d8a8c65b1557b1374e55a406a2005333c3f816a5954120d.jpg)


## 微调模式

通过配置TIMERx_CTL0寄存器中的ADMEN位为1，可以使能微调模式。该模式可以提高输出PWM波的有效分辨率，通过TIMERx_CHxCV寄存器中的CHxVAL[19:0]位域可以提高占空比分辨率，通过TIMERx_CAR寄存器中的CARL[19:0]位域可以提高PWM频率的分辨率。

当微调模式使能时，CHxVAL位域和CARL位域的低16位[15:0]用于整数部分，高4位[19:16]用于微调的小数部分。通过预定义的方式，在连续16个周期内对CHxVAL值或CARL值进行微调（每次调整不超过一个TIMER时钟周期），可增加16倍的分辨率。


图 23-105. 微调模式：数据格式和寄存器位域


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/7c2c9806a11f79f722aa06c54e58cb1642773e0f66819a1ee64438b4d2066a81.jpg)


根据ADMEN位的配置（置位或清零），CHxVAL位域和CARL位域将自动更新。当需要对ADMEN位进行清零时，需要遵循以下步骤：

1. CEN位和ARSE位必须清零；

2. CARL[19:16]位域必须清零；

3. ADMEN位必须清零；

4. CHxIF位必须清零；

5. 可以将CEN位置1。

以下公式可以计算PWM分辨率：

$$
\text { Resolution } = f _ {\text { PSC\_CLK }} / f _ {\text { pwm }}\tag{23-9}
$$

由式(23-9)可得，微调模式禁能时（ADMEN=0），PWM的最小频率 $\mathsf { f } _ { \mathsf { p w m } }$ :

$$
(f _ {p w m}) _ {\min} = f _ {P S C \_ C L K} / 6 5 5 3 6\tag{23-10}
$$

微调模式使能时（ADMEN=1），

$$
\left(f _ {p w m}\right) _ {\min} = f _ {P S C \_ C L K} / (6 5 5 3 5 + 1 5 / 1 6)\tag{23-11}
$$

当微调模式使能时，CHxVAL[19:0]位域和CARL[19:0]位域的最大值为0xFFFFE（整数部分为0xFFFE，小数部分为0xF）。

在连续 16 个周期内，占空比和周期的变化情况，具体如 23-106. PWM 和 23-17.CHxVAL CARL 所示。


图 23-106. PWM 微调模式原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/0daadfb34a0225b86c47cd95fbb4d15c927240197f566d5734217d7969850531.jpg)



表 23-17. 边沿对齐模式中 CHxVAL 和 CARL 位域的变化


<table><tr><td rowspan="2">CHxVAL[19:16] / CARL[19:16]</td><td colspan="16">周期</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>0000</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0001</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0010</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0011</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0100</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0101</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0110</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0111</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1001</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1010</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1011</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1100</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1101</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1110</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1111</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr></table>

## 复合 PWM 模式

在复合 PWM 模式中（CHxCPWMEN = 1’b1，CHxMS[2:0] = 3’b000 和 CHxCOMCTL = 4’b0110、4’b0111），通道 x（x = 0, 1））上的 PWM 输出信号由 CHxVAL 和 CHxCOMVAL_ADD 位确定。如果 CHxCOMCTL = 4’b0110（PWM 模式 0）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL= 4’b0111（PWM 模式 1）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为低。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为高。如果 CHxCOMCTL =4’b0111（PWM 模式 1）且 DIR = 1’b0（向上计数模式），或者 CHxCOMCTL=4’b0110（PWM 模式 0）且 DIR = 1’b1（向下计数模式），当计数器和 CHxVAL 的值相匹配时通道 x 输出强制为高。当计数器与 CHxCOMVAL_ADD 的值相匹配时，通道 x 输出强制为低。PWM 的周期取决于（CARL + 0x0001），PWM 脉冲宽度可以下 23-18.  PWM 计算。


表 23-18. 复合 PWM 脉冲宽度


<table><tr><td>条件</td><td>模式</td><td>PWM 脉冲宽度</td></tr><tr><td rowspan="2">CHxVAL &lt; CHxCOMVAL_ADD ≤ CARL</td><td>PWM 模式 0</td><td>(CARL + 0x0001) + (CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM 模式 1</td><td>(CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD &lt; CHxVAL ≤ CARL</td><td>PWM 模式 0</td><td>(CHxVAL - CHxCOMVAL_ADD)</td></tr><tr><td>PWM 模式 1</td><td>(CARL + 0x0001) + (CHxCOMVAL_ADD - CHxVAL)</td></tr><tr><td>(CHxVAL = CHxCOMVAL_ADD ≤</td><td>PWM 模式 0(向上计数)</td><td>100%</td></tr><tr><td rowspan="2">CARL)或(CHxVAL&gt;CARL&gt;CHxCOMVAL_ADD)</td><td>或PWM模式1(向下计数)</td><td></td></tr><tr><td>PWM模式0(向下计数)或PWM模式1(向上计数)</td><td>0%</td></tr><tr><td rowspan="2">CHxCOMVAL_ADD&gt;CARL&gt;CHxVAL</td><td>PWM模式0(向上计数)或PWM模式1(向下计数)</td><td>0%</td></tr><tr><td>PWM模式0(向下计数)或PWM模式1(向上计数)</td><td>100%</td></tr><tr><td>(CHxVAL&gt;CARL)且(CHxCOMVAL_ADD&gt;CARL)</td><td>-</td><td>CHx_O输出保持</td></tr></table>


当计数器计数到CHxVAL，CHxIF位置1且如果CHxIE=1通道x产生中断，如果CHxDEN=1，则产生DMA请求。当计数器计数到CHxCOMVAL_ADD时，CHxCOMADDIF位置1（该中断标志位只在复合PWM模式有效，CHxCPWMEN=1），如果CHxCOMADDIE = 1通道x附加比较中断产生（只有中断产生，没有DMA请求响应）。



根据CHxVAL，CHxCOMVAL_ADD和CARL之间的关系，可以分为四种情况：


 CHxVAL < CHxCOMVAL_ADD，CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。


图 23-107 通道 x 输出 PWM（CHxVAL < CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/6fc65b297744516f12576d5617e9fdda94a77f9a8ef3843e5085005f56287112.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/0d82bcbd4fc0795b25065060984dd2e4edfd124c511fbce1262042e40c267f1e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/c60d9cb8da31973e266e5cfd571b7ea77551368cd0554b9f56e8c05fff8c502e.jpg)


 CHxVAL = CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。


图 23-108. 通道 x 输出 PWM（CHxVAL = CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/ff3db735fb02edd22c366ecc505f73083d40d099f95b78ce0df2ca5347c7d837.jpg)



 CHxVAL > CHxCOMVAL_ADD, CHxVAL和CHxCOMVAL_ADD值介于0和CARL之间。



图 23-109. 通道 x 输出 PWM（CHxVAL > CHxCOMVAL_ADD）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/73faa6a193da97eb8ade0ff24c24a04935f074cc21c58b121babff44bd7ef28c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/6b4441d03062446c6f306f1f691f0cb116b213441ff5cc820fbbf93449c6e124.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/2ad19d9120baabb37e2da5c61ef7574d08d559d2317efd2f04b61e3437d4de3b.jpg)



 CHxVAL或CHxCOMVAL_ADD值大于CARL。



图 23-110. 通道 x 输出 PWM（CHxVAL 或 CHxCOMVAL_ADD > CARL）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/44a4220295f6e6009297ad87a4978c4b4cf51f12b4aeadc4909b6f77b275302a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/dd2fd6a072d8175dc86ca4984ea92afaaf2c146eb0c73ec41b09b482bd4af71d.jpg)


复合PWM模式支持不修改周期只修改占空比的PWM信号的生成。 23-111. x PWMCHxCOMVAL_ADD 显示PWM输出和中断波形。

在某些情况下，CHxCOMVAL_ADD的匹配事件可以发生在下一个计数周期（CHxCOMVAL_ADD值在计数器到达CHxVAL值之后被写入，且CHxCOMVAL_ADD值小于或者等于CHxVAL值）。


图 23-111. 通道 x 输出 PWM 占空比随着 CHxCOMVAL_ADD 值而改变


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/3c7fcbf9c08728a1806e8681e7f52c447db4a0591bc50be9ebba342bb7bf634c.jpg)


如果多个通道配置为复合PWM模式，可以为每对通道x的匹配边沿设定一个偏移量（相对于其它通道）。这种特性在产生照明PWM控制信号时非常有用，因为在这种情况下，希望彼此边缘不重合，以消除噪声的产生。CHxVAL寄存器值是PWM脉冲相对于计数器周期开始的偏移。

## 输出匹配脉冲选择

当发生匹配事件时，CHx_O（x = 0, 1）的输出由CHxCOMCTL[3:0] $( \mathsf { x } = 0 , 1 )$ 位设置，通过配置CHxOMPSEL[1:0]（x = 0, 1）位，可选择CHx_O $( \mathsf { x } = 0 , 1 )$ 的输出信号正常或者脉冲。

当匹配事件发生时， $\mathsf { C H x O M P S E L } [ 1 : 0 ]$ $( \mathsf { x } = 0 , \mathsfit { 1 } )$ 用于选择OxCPRE信号输出（驱动CHx_O）：

 $\mathsf { C H x O M P S E L } = 2 ^ { \prime } \mathsf { b 0 0 }$ ${ \mathsf { O x C P R E } }$ 信号根据CHxCOMCTL[3:0]位的配置正常输出；

 $\mathsf { C H x O M P S E L } = 2 ^ { \prime } \mathsf { b } 0 1$ ，只有在计数器向上计数，发生匹配事件时，OxCPRE信号输出一个脉

冲，且脉冲宽度为一个CK_TIMER时钟周期；


图 23-112. 边沿对齐模式下 CHx_O 输出脉冲（CHxOMPSEL = 2’b01）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/fbda70a5abff6c5dc8f7bb1afb177665590b9bdacefb107f9e4eb1aca4393edd.jpg)


## 通道输出准备信号

如 23-100. MCHxMSEL = 2’b00 x = 0 ， 23-101.MCHxMSEL = 2’b11 x = 0 和 23-102. x = 1 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前将产生一个中间信号，即 OxCPRE 或 MOxCPRE 信号（通道 x 或多模式通道 x 参考信号）。

OxCPRE 和 MOxCPRE 信号有若干类型的输出功能，通过配置 CHxCOMCTL 位定义 OxCPRE 信号类型，通过配置 MCHxCOMCTL 位定义 MOxCPRE 信号类型。

下面以 OxCPRE 为 例 进 行 说 明 ， 设 置 CHxCOMCTL=0x00 可 以 保 持 原 始 电 平 ； 设 置CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将OxCPRE 信号设置为低电平；设置 CHxCOMCTL = 0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06 或0x07 可以配置 PWM 模式 0/PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL = 0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 清除通道输出准备信号

当CHxCOMCEN位或MCHxCOMCEN位（在TIMERx_CHCTLy / TIMERx_MCHCTLy寄存器中）

置 1 时 ， OxCPRE 和 MOxCPRE 信 号 可 以 由 OCPRE_CLR_INT 信 号 清 除 。 该 功 能 用 于CHxCOMCTL[3:0]位域或MCHxCOMCTL[3:0]位域（4'b0100和4'b0101除外）中配置的比较输出模式。

OCPRE_CLR_INT 连接到 OCPRE_CLR 输入。OxCPRE /MOxCPRE 信号被 OCPRE_CLR_INT信号的高电平清除，直到下一个更新事件发生时才会恢复输出。在 TIMERx_AFCTL1 寄存器的OCRINSEL[2:0]位域中选择 OCPRE_CLR 的输入。

## 互补输出

CHx_O 和 MCHx_O 的输出具有两种情况：

 MCHxMSEL = 2’b00：MCHx_O输出独立于CHx_O输出。

 MCHxMSEL = 2’b11 ： MCHx_O 输 出 与 CHx_O 输 出 互 补 ， 且 MCHx_O 的 输 出 不 由MCHxCOMCTL位配置。

当 CHx_O 和 MCHx_O 输出互补时，这两个信号不能同时有效。TIMERx 的 1 对通道具有此功能。互补信号 CHx_O 和 MCHx_O 是由一组参数来决定：TIMERx_CHCTL2 寄存器中的 CHxEN 和MCHxEN 位，TIMERx_CCHP0 寄存器中和 TIMERx_CTL1 寄存器中的 POEN、ROS、IOS、ISOx和 ISOxN 位。输出极性由 TIMERx_CHCTL2 寄存器中的 CHxP 和 MCHxP 位来决定。

当 CHx_O 和 MCHx_O 的输出互补时，有三种输出情况：输出使能、输出关闭状态和输出禁能，具体情况可参考 23-19. MCHxMSEL=2’b11 。


表 23-19. 由参数控制的互补输出表（MCHxMSEL=2’b11）


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>MCHxEN</td><td>CHx_O</td><td>MCHx_O</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / MCHx_O = LOWCHx_O / MCHx_O 输出禁能(1)</td></tr><tr><td>1</td><td rowspan="3" colspan="2">CHx_O/MCHx_O输出关闭状态(2):通道先输出无效电平: CHx_O = CHxP, MCHx_O = CHxNP); 如果死区产生时钟未失效, 在死区时间之后: CHx_O = ISOx, MCHx_O = ISOxN (3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/MCHx_O输出关闭状态:通道先输出无效电平: CHx_O = CHxP, MCHx_O = CHxNP); 如果死区产生时钟未失效, 在死区时间之后: CHx_O = ISOx, MCHx_O = ISOxN</td></tr><tr><td rowspan="3">1</td><td rowspan="3">0</td><td rowspan="3">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/MCHx_O = LOWCHx_O/MCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>MCHx_O=OxCPRE⊕(2)MCHxPMCHx_O输出使能</td></tr><tr><td>1</td><td>0</td><td>CHx_O=OxCPRE⊕CHxP</td><td>MCHx_O = LOW</td></tr></table>


GD32G553 用户手册


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>MCHxEN</td><td>CHx_O</td><td>MCHx_O</td></tr><tr><td rowspan="6"></td><td rowspan="2"></td><td rowspan="6"></td><td rowspan="2"></td><td></td><td>CHx_O输出使能</td><td>MCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕ CHxPCHx_O输出使能</td><td><eq>\text{MCHx}_\text{O}=(!OxCPRE)^{(3)} \oplus</eq>MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="4">1</td><td rowspan="2">0</td><td>0</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O=OxCPRE ⊕ MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE ⊕ CHxPCHx_O输出使能</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕ CHxPCHx_O输出使能</td><td>MCHx_O=!OxCPRE ⊕MCHxPMCHx_O输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / MCHx_O 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / MCHx_O 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；


（3） 详情见中止模式章节。

（4） ⊕：异或操作；

（5） (!OxCPRE)：OxCPRE 信号的互补信号。

## 死区时间插入

设置 MCHxMSEL = 2’b11，CHxEN 和 MCHxEN 为 1’b1，同时设置 POEN=1，就可以使能死区插入功能。DTCFG 位域定义了死区时间，死区时间对所有通道有效。死区时间设置的细节请参考0 TIMERx_CCHP0 。

死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM0 模式，当通道 x 匹配发生时（TIMERx 计数器=TIMERx_CHxCV），OxCPRE 翻转。在23-113. 中的 A点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而 MCHx_O 信号立刻变为低电平。同样，在 B点，计数器再次匹配（TIMERx计数器=TIMERx_CHxCV），OxCPRE 信号被清 0，CHx_O 信号被立即清零，MCHx_O 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。有时会有一些死角事件发生，例如：如果死区延时大于或者等于 CHx_O 信号的占空比，CHx_O 信号一直为无效值，如 23-113.时间的互补输出所示。


图 23-113. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/d8a4d0955a4e50acd43a6e275424e98aae84321e57b75a2f9e27ddb7fe0b2c11.jpg)


## 不同的死区时间插入

当DTDIFEN位（在TIMERx_CCHP1寄存器中）设置为1时，CHx_O和MCHx_O信号可以输出不同的死区时间，具体如 23-114. DTDIFEN=1 所示。

通道输出准备信号OxCPRE上升沿的死区时间由TIMERx_CCHP0寄存器或TIMERx_FCCHPy寄存器中的DTCFG[7:0]位域配置。OxCPRE信号的下降沿的死区时间由TIMERx_CCHP1寄存器或TIMERx_FCCHPy寄存器中的DTFCFG[7:0]位域配置。

可以在CHx_O和MCHx_O信号输出时修改死区时间。当TIMERx_CCHP1寄存器中的DTMODEN位置1时，可以使能该功能。DTCFG[7:0]位域和DTFCFG[7:0]位域的新值将会在下一次更新事件发生时生效。


图 23-114.不同死区时间的互补输出（DTDIFEN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/be102a5a529cd9f0f361f50d96d3f484b0dbb07c318b5682335cd9f899363aa1.jpg)


## 中止功能

当 MCHxMSEL = 2’b11（MCHx_O 的输出不使用 MCHxCOMCTL 位配置）时，MCHx_O 输出与CHx_O 输出互补。在这种情况下，CHx_O 和 MCHx_O 信号不能同时设置为有效电平。

通用 L3 定时器具有 BREAK0 中止功能。可以通过将 TIMERx_CCHP0 寄存器中的 BRK0EN 位置1 来使能。中止输入极性由 TIMERx_CCHP0 寄存器中的 BRK0P 位配置，电平有效。

使用 BREAK0 功能时，CHx_O 和 MCHx_O 信号的输出电平由以下位控制：TIMERx_CCHP0 寄存器的 POEN、IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。

中止事件是所有源逻辑或运算的结果。中止功能可以处理三种类型的事件源：

 外部信号源：来自BRKIN0输入；

系统源：由RCU中的时钟监视器CKM生成的HXTAL卡住事件、LVD锁定事件，Cortex®-M33锁定事件、SRAM奇偶校验错误或FLASH ECC错误事件；

 片上外设源：比较器输出、HPDF的看门狗输出。

BREAK0中止事件也可以由软件置位TIMERx_SWEVG寄存器中的BRK0G位产生。

如 BRKIN0 TRIGSEL GPIO TIMER14_BRKINTRIGSEL_TIMER14BRKIN

图 23-115. BREAK0 中止功能逻辑图所示，BRKIN0 可以从 TRIGSEL 模块选择 GPIO 引脚，具体可参考 TIMER14_BRKIN TRIGSEL_TIMER14BRKIN 。


图 23-115. BREAK0 中止功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/0369506dc8fd1b865659e0e60ff81bc7c51470648bdf56e0ea29ce25ffad2bb0.jpg)


BREAK0可用于处理系统源、片上外设和外部输入信号源的故障，当发生BREAK0中止事件时，输出强制为无效电平，或在死区持续时间之后，输出将以预定的电平（有效或无效）强制输出。

当 MCHxMSEL = 2’b11 且发生 BREAK0 中止事件时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 MCHx_O 的输出由 TIMERx_CTL1 寄存器中的 ISOx 位和 ISOxN 位确定。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。当 IOS=1 时，通道输出情况如 23-116.BREAK0 IOS=1 所示，首先通道互补输出为复位状态，然后死区时间发生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx和 ISOxN 位配置。


图 23-116. 通道响应 BREAK0 中止输入（高电平有效）时，输出信号的行为（IOS=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/82316f0ab8eb292ff19299baa120bf56e118960b1d89f60ae525db0132800ebc.jpg)



发生中止事件时，TIMERx_INTF 寄存器的 BRK0IF/BRK1IF 位被置 1。如果 BRKIE=1，中断产生。


## 锁存中止功能

高级定时器的中止输入引脚BRKIN0具有锁存中止功能，可通过设置TIMERx_CCHP0寄存器中的BRK0LK位为1，将相应的BRKIN0配置为锁存中止功能。

当使能了锁存中止功能时，需要将 BRKIN0 引脚设置为开漏模式，且低电平有效（BRK0P =0，BRK0IN0P=0）。任何中止源请求发生时，都可以将相应的 BRKIN0 引脚强制为低电平。若 BRKIN0引脚设置为高电平有效（BRK0 =1，BRK0IN0P=1），则锁存中止功能被禁止。

当中止功能使能（将TIMERx_CCHP0寄存器中的BRK0EN=1）时，通过软件将TIMERx_SWEVG寄存器中的BRK0G位置1也可以将BRKIN0引脚强制为低电平。

当中止功能未使能（将TIMERx_CCHP0寄存器中的BRK0EN位为0）时，通过软件将BRK0G位置1，对BRKIN0引脚无影响。但BRK0F标志位会置位，通道输出为安全状态。

将 TIMERx_CCHP0 寄存器中的 BRK0REL 位置 1，可以释放 BRKIN0 引脚，当中止输入源无效时，BRK0REL 位由硬件清零，BRKIN0 引脚将恢复锁存中止功能。

在下面两种情况下，不能释放中止输入引脚 BRKIN0：

 中止输入源有效：虽然BRK0REL位置1，释放了BRKIN0引脚，但由于中止源仍然存在，故中止事件仍然有效；

 POEN=1：通道输出使能时，即使BRK0REL位置1，也不能释放BRKIN0引脚。


表 23-20. 中止功能锁存/释放条件


<table><tr><td>POEN</td><td>BRK0LK</td><td>BRK0REL</td><td>中止输入引脚状态</td></tr><tr><td rowspan="2">0</td><td>1</td><td>0</td><td>锁存</td></tr><tr><td>1</td><td>1</td><td>释放</td></tr></table>

BREAK0 输入引脚 BRKIN0 的锁存中止功能默认是使能的（BRK0REL=0），当 BREAK0 中止事件发生时，可以通过下面的方法来重新配置锁存中止功能：

 BRK0REL=1，释放BRKIN0引脚；

 软件等待系统中止源无效，可通过软件清除SYSBIF标志位；

 软件轮询BRK0REL位，直到BRK0REL=0（硬件实现）。

上述过程完成后，BREAK0 锁存中止功能重新使能，此时，可通过软件将 POEN 置 1 来恢复 PWM输出。


图 23-117. BREAK0 的 BRKIN0 引脚锁存功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/5da5da47e6eba31c8e6b07cf24d100c3376f1c660569b752a179e5bc2c4b0311.jpg)


## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式等，可以通过设置SYSCFG_TIMERxCFG(x = 14)寄存器中的 TSCFGy[4:0] (y = 3..7)位域来确定，具体的输入触发源可以通过 TSCFGy[4:0] (y = 3..7)位域的值来选择。


表 23-21. 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[4:0]y = 3:复位模式y = 4:暂停模式y = 5:事件模式y = 6:外部时钟模式0y=7:复位+事件模式</td><td>TSCFGy[4:0]00000:模式禁能00001:ITI000010:ITI100011:ITI200100:ITI300101:CI0F_ED00110:CI0FE000111:CI1FE101000:保留01001:ITI401010:ITI501011:ITI601100:ITI701101:ITI801110:ITI901111:ITI1010000:保留10001:保留10010:保留10011:ITI14其他:保留</td><td>如果触发源是CIxFEx(x = 0,1)或者MCIxFEMx(x = 0,1),配置CHxP、MCHxP和MCHxFP来选择极性和反相。</td><td>触发源ITIx,滤波和预分频不可用触发源CIx/MCIX,配置CHxCAPFLT/MCHxCAPFLT设置滤波,分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[4:0]5'b00001,选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图23-118.复位模式下的控制电路</td></tr><tr><td>例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[4:0]=5'b00110,选择CI0FE0为触发源</td><td>TIOS=0(非异或)[MCHOP=0,CHOP=0]CI0FE0不反相,在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td></td><td colspan="4">图23-119.暂停模式下的控制电路<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/7e57bb263df659ec956439c2abc02023790c0110c8fb9c7efa31fcd0ce5d0d9f.jpg"/></td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[4:0]=5'b01000,选择ETIFP为触发源</td><td>ETP=0没有极性改变</td><td>ETPSC=1,2分频ETFC=0,无滤波</td></tr><tr><td colspan="4">图23-120.事件模式下的控制电路TIMER_CK ETI ETIFP CNT_REG TRGIF</td></tr><tr><td>例4</td><td colspan="4">复位+事件模式当触发输入的上升沿到来时,计数器被重新初始化并开始计数。该模式仅用于可延时的单脉冲模式。</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，可使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL / MCHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和

TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE / MOxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。

单脉冲模式也同样适用于复合 PWM 模式（CHxCPWMEN = 1’b1 和 CHxMS[2:0] = 3’b000）。


图 23-121. 单脉冲模式，TIMERx_CHxCV = 0x04 TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/6b8a72bf7ca6b3fde1faee4b78565144bbe9805e4536bd72b97929e714e83a0a.jpg)


## 可延时的单脉冲模式

可 以 通 过 将 TIMERx_CHCTLx / TIMERx_MCHCTLx 寄 存 器 中 的 CHxCOMCTL[3:0] /MCHxCOMCTL[3:0]位置1来使能可延时的单脉冲模式。在这个模式下，通道输出准备信号OxCPRE/ MOxCPRE的脉冲宽度由TIMERx_CAR寄存器值确定。

一旦设置定时器运行在可延时的单脉冲模式下，需进行以下配置：

■ 定时器必须工作在从模式下，SYSCFG_TIMERxCFG(x = 14)寄存器中的 TSCFG7[4:0] !=5’b00000，从模式选择复位 + 事件模式；

CHxCOMCTL[3:0]/ MCHxCOMCTL[3:0]位设置为 4’b1000（可延时单脉冲模式 0）或 4’b1001（可延时单脉冲模式 1）

在可延时单脉冲模式0下，OxCPRE / MOxCPRE的输出情况类似与PWM模式0。在向上计数模式时，OxCPRE / MOxCPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平；在向下计数模式时，OxCPRE / MOxCPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平。

在可延时单脉冲模式1下，OxCPRE / MOxCPRE的输出情况类似与PWM模式1。在向上计数模式时，OxCPRE / MOxCPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平；在向下计数模式时，OxCPRE / MOxCPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平。

PWM微调模式也可用于可延迟的单脉冲模式。

注意：

 不能使用中央对齐模式，TIMERx_CTL0 寄存器中的 CAM[1:0] = 2’b00；

 在向上计数时（TIMERx_CTL0 寄存器中的 DIR = 0），TIMERx_CHxCV / TIMERx_MCHxCV的值设置为 0；在向下计数时，TIMERx_CHxCV / TIMERx_MCHxCV 的值应大于或等于TIMERx_CAR 的值。


图 23-122. 可延时单脉冲模式（TIMERx_CHxCV = 0x00，TIMERx_CAR = 0x60）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/3ec318a44fc01fdda4f5e85fdf04ad471ffc6e7dc32a50626e2bb0e7068b7d26.jpg)


## 定时器互连

参考 (TIMERx,x = 0,7) 。

## 定时器 DMA模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA 请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4, DMATA+0x8, DMATA+0xc 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## UPIF 位备份功能

可以通过配置TIMERx_CTL0寄存器中的UPIFBUEN位来使能UPIF位的备份功能，UPIF和UPIFBU位之间没有延迟，两者完全同步。

使能该功能后，TIMERx_INTF寄存器中的UPIF位将会被实时备份到TIMERx_CNT寄存器中的

UPIFBU位。这可以避免在读计数器和中断处理时产生冲突的情况。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL1 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

