## 23.4. 通用定时器 L4（TIMERx, x = 15, 16）

## 23.4.1. 简介

通用定时器 L4（TIMER15 / 16）是 2 通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。通用定时器 L4 含有一个 16 位无符号计数器。

通用定时器 L4 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器。

通用定时器 L4 包含了一个死区时间插入模块，非常适合电机控制。

## 23.4.2. 主要特征

 总通道数：2；

 计数器宽度：16位；

 时钟源可选：内部时钟；

 计数模式：向上计数；

 可编程的预分频器：16位，运行时可以被改变；

 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

 可编程的死区时间；

 自动重装载功能；

 可编程的计数器重复功能；

 中止输入功能：BREAK0；

 中断输出和DMA请求：更新事件，比较/捕获事件和中止事件。

## 23.4.3. 结构框图

23-123. L4 提供了通用定时器 L4 的内部配置细节


图 23-123. 通用定时器 L4 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/55d3a5bb86304f50cd2397624b65d2f424637393c5d254e9f0fcc4c1d2a2ab74.jpg)


## 23.4.4. 功能描述

## 时钟源选择

通用定时器 L4 由内部时钟源 TIMER_CK.

 定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

通用定时器 L4 只有一个时钟源：内部时钟源。用来驱动计数器预分频器的是内部时钟源CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。


图 23-124. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/8cf03c758d09922ed21924fab72aedecab0df774f06413feac89187fed4f780d.jpg)


## 预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 23-125. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/bf501872ff6b635f632c580aa1536e4656a2d681b8d63663bc218270231f6d90.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数。如果设置了重复计数器，在（TIMERx_CREP0 / 1 + 1）次上溢后产生更新事件，否则在每次上溢时都会产生更新事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

23-126. PSC = 0 / 2 和 23-127.TIMERx_CAR 给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 23-126. 向上计数时序图，PSC = 0 / 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/adad853d3ca7edee9fd36ec53c0f5b57c551ebd39aa8d38d0eecaa46a5581279.jpg)



图 23-127. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/2889496a5cd4284c23982a292897d05e5e4448ff161ac3ea45db50b11225989e.jpg)


## 重复计数器

通用L3定时器有两个重复寄存器TIMERx_CREP0 / 1，可通过配置TIMERx_CFG寄存器中的CREPSEL位来选择。其中TIMERx_CREP0寄存器中的CREP0[7:0]是8位的，TIMERx_CREP1寄存器中的CREP1[31:0]是32位，用户可根据需求选择使用。

重复计数器是用来在 N + 1 个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP0 / 1 寄存器的 CREP0 / 1。向上计数模式下，重复计数器在每次计数器上溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP0 / 1 寄存器中 CREP0 / 1 的值并产生一个更新事件。


图 23-128. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/919b7ac4955c2a40fe054374a8d69147f39c39c0955a8ecd349f5b3bec75e275.jpg)


## 捕获/比较通道

通用定时器 L4 拥有 2 个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

当通道用于输入时，通道 x 和多模式通道 x 可独立进行输入捕获；当通道用于比较输出时，通道 x和多模式通道 x 可输出独立和互补。

##  输入捕获模式

当 MCHxMSEL=2’b00（独立模式）时，通道 x 和多模式通道 x 才可以独立进行输入捕获。

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV / TIMERx_MCHxCV（x = 0）寄存器会捕获计数器当前的值，同时CHxIF / MCHxIF（x = 0）位置 1，如果 CHxIE / MCHxIE =1（x = 0），则产生相应的通道中断。


图 23-129. 通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/3780df3cb7211ceff6827d5ec9a4f926ad2b10a5db61bacd64ba36cae359232c.jpg)



图 23-130. 多模式通道 0 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/47445591238ca797f5b67e1d27e67b91134ffe9bfdfc0a27267a3c6c52e99288.jpg)



通道输入信号 CIx / MCIx 有两种选择，一种是 TIMERx_CHx / TIMERx_MCHxCV 信号，另一种是 TIMERx_CH0，TIMERx_CH1 和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。


通道输入信号 CIx / MCIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP /MCHxP、MCHxFP选择使用上升沿或者下降沿。配置 CHxMS / MCHxMS，可以选择其他通道的输入信号或内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV / TIMERx_MCHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT位和TIMERx_MCHCTL0寄存器中CHxMCAPFLT）：

根据输入信号和请求信号的质量，配置相应的CHxCAPFLT / CHxMCAPFLT位。第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP和MCHxP位，TIMERx_MCHCTL2寄存器中MCHxFP[1:0]位域）：

配置CHxP和MCHxP位或MCHxFP位域选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS、TIMERx_MCHCTL0寄存器中MCHxMS）：

一旦通过配置CHxMS / MCHxMS选择输入捕获源，必须确保通道配置在输入模式（CHxMS != 0x000或MCHxMS != 0x000），而且TIMERx_CHxCV / TIMERx_MCHxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中CHxIE、CHxDEN位和MCHxIE、MCHxDEN位）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中CHxEN / MCHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV / TIMERx_MCHxCV被设置成当前计数器的值，CHxIF / MCHxIF位置1。如果CHxIF / MCHxIF位已经为1，则CHxOF / MCHxOF位置1。根据TIMERx_DMAINTEN寄存器中CHxIE、CHxDEN位和MCHxIE、MCHxDEN位的配置，相应的中断和DMA请求会被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

 输出比较模式

23-131. MCHxMSEL = 2’b00 x = 0 和 23-132.MCHxMSEL = 2’b11 x = 0 给出了通道的输出比较逻辑。


图 23-131. 输出比较逻辑（当 MCHxMSEL = 2’b00 时，x = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/7ae5b13acb1767b796af0754183bff8d27b0ee30f501eed02e3a656e3627baaa.jpg)



图 23-132. 输出比较逻辑（当 MCHxMSEL = 2’b11 时，x = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/ab03e9aabecfdd02467b47fffd3bef8d5ee81cee7f3e932582446a99ff068ba1.jpg)


通道输出信号CHx_O / MCHx_O与OxCPRE / MOxCPRE信号（详情请见 ）的

关系描述如下（OxCPRE / MOxCPRE信号高电平有效）：

当MCHxMSEL=2’b00（TIMERx_CTL2寄存器中），MCHx_O输出与CHx_O输出相互独立。CHx_O 输 出 电 平 取 决 于 OxCPRE 信 号 、 CHxP 位 和 CHxEN 位 （ 详 细 内 容 参 考TIMERx_CHCTL2寄存器）。MCHx_O输出电平取决于MOxCPRE信号、MCHxFP[1:0]位和MCHxEN位（详细内容参考TIMERx_CHCTL2和TIMERx_MCHCTL2寄存器）。请参考23-131. MCHxMSEL = 2’b00 x = 0 。

当MCHxMSEL=2’b11，MCHx_O输出和CHx_O输出互补。CHx_O / MCHx_O输出电平取决于OxCPRE信号、CHxP / MCHxP位和CHxEN / MCHxEN位。请参考 23-132.MCHxMSEL = 2’b11 x = 0 。

例如（MCHx_O输出与CHx_O输出相互独立）：

1）当设置CHxP=0（CHx_O高电平有效，与OxCPRE输出极性相同）、CHxEN=1（CHx_O输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_O输出有效（高）电平；

若OxCPRE输出无效（低）电平，则CHx_O输出无效（低）电平。

2）当设置MCHxP=1（MCHx_O低电平有效，与MOxCPRE输出极性相反）、MCHxEN=1（MCHx_O输出使能）时：

若MOxCPRE输出有效（高）电平，则MCHx_O输出有效（低）电平；

若MOxCPRE输出无效（低）电平，则MCHx_O输出无效（高）电平。

当MCHxMSEL=2’b11，CHx_O和MCHx_O同时输出时，CHx_O和MCHx_O的具体输出情况还与TIMERx_CCHP0寄存器中的相关位（ROS、IOS、POE和DTCFG等位）有关。详情请见 。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 TIMERx_CHxCV / TIMERx_MCHxCV 寄存器与计数器的值匹配时，根据CHxCOMCTL / MCHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 TIMERx_CHxCV / TIMERx_MCHxCV 寄存器的值匹配时，CHxIF / MCHxIF 位被置 1，如果 CHxIE / MCHxIE = 1 则会产生中断，如果 CHxDEN / MCHxDEN =1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

 设置CHxCOMSEN / MCHxCOMSEN位来配置输出比较影子寄存器；

■ 设置CHxCOMCTL / MCHxCOMCTL位来配置输出模式（置高电平/置低电平/翻转）；

 设置CHxP/ MCHxP / MCHxFP位来选择有效电平的极性；

 设置CHxEN/MCHxEN使能输出。

第三步：通过CHxIE/ MCHxIE / CHxDEN / MCHxDEN位配置中断 / DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

TIMERx_CHxCV / TIMERx_MCHxCV可以在运行时根据你所期望的波形而改变。第五步：设置CEN位使能定时器。

23-133. 显示了三种比较输出模式：翻转/置高电平/置低电平，CAR=0x63，CHxVAL=0x3。


图 23-133. 三种输出比较模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e7e48bb1f36d41036d1c412a29f2c691bb12873892f30265661c014f75bf4f17.jpg)


## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL / MCHxCOMCTL 为 4’b0110，PWM 模式 1 是配置 CHxCOMCTL / MCHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和TIMERx_CHxCV / TIMERx_MCHxCV 寄存器的值，输出 PWM 波形。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV / TIMERx_MCHxCV寄存器值决定。 23-134. PWM 显示了 EAPWM 的输出波形和中断。

当计数器向上计数时，在PWM0模式下（CHxCOMCTL / MCHxCOMCTL =4’b0110），如果TIMERx_CHxCV / TIMERx_MCHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为有效电平；PWM1模式下（CHxCOMCTL / MCHxCOMCTL=4’b0111），如果TIMERx_CHxCV /TIMERx_MCHxCV寄存器的值大于TIMERx_CAR寄存器的值，通道输出一直为无效电平。


图 23-134. PWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/9646d1465150211023a2680a2d5d5f4bcdfdf0e5126ca6ac4f1e74e6e353f4cd.jpg)


## 微调模式

请参考 L3 TIMERx, x = 14 。

## 通道输出准备信号

23-131. MCHxMSEL = 2’b00 x = 0 和 23-132.MCHxMSEL = 2’b11 x = 0 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前将产生一个中间信号，即 OxCPRE 或 MOxCPRE 信号（通道 x 或多模式通道 x 参考信号）。OxCPRE 和 MOxCPRE 信号有若干类型的输出功能，通过配置 CHxCOMCTL 位定义 OxCPRE 信号类型，通过配置 MCHxCOMCTL 位定义 MOxCPRE 信号类型。

下面以 OxCPRE 为 例 进 行 说 明 ， 设 置 CHxCOMCTL=0x00 可 以 保 持 原 始 电 平 ； 设 置CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域为 0x06 或0x07 可以配置 PWM 模式 0 / PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFE 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 清除通道输出准备信号

请参考 L3 TIMERx, x = 14 。

## 互补输出

CHx_O 和 MCHx_O 的输出具有两种情况：

 MCHxMSEL=2’b00：MCHx_O输出独立于CHx_O输出。

 MCHxMSEL=2’b11 ： MCHx_O 输 出 与 CHx_O 输 出 互 补 ， 且 MCHx_O 的 输 出 不 由MCHxCOMCTL位配置。

当 CHx_O 和 MCHx_O 输出互补时，这两个信号不能同时有效。TIMERx 有 1 对通道具有此功能。互补信号 CHx_O 和 MCHx_O 是由一组参数来决定：TIMERx_CHCTL2 寄存器中的 CHxEN 和MCHxEN 位，TIMERx_CCHP0 寄存器中和 TIMERx_CTL1 寄存器中的 POEN、ROS、IOS、ISOx和 ISOxN 位。输出极性由 TIMERx_CHCTL2 寄存器中的 CHxP 和 MCHxP 位来决定。

当 CHx_O 和 MCHx_O 的输出互补时，有三种输出情况：输出使能、输出关闭状态和输出禁能，具体情况可参考 23-22. MCHxMSEL = 2’b11 。


表 23-22. 由参数控制的互补输出表（MCHxMSEL = 2’b11）


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>MCHxEN</td><td>CHx_O</td><td>MCHx_O</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / MCHx_O = LOWCHx_O / MCHx_O 输出禁能(1)</td></tr><tr><td>1</td><td rowspan="3" colspan="2">CHx_O/MCHx_O输出关闭状态(2):通道先输出无效电平: CHx_O = CHxP, MCHx_O = CHxNP); 如果死区产生时钟未失效, 在死区时间之后: CHx_O = ISOx, MCHx_O = ISOxN (3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/MCHx_O输出关闭状态:通道先输出无效电平: CHx_O = CHxP, MCHx_O = CHxNP); 如果死区产生时钟未失效, 在死区时间之后: CHx_O = ISOx, MCHx_O = ISOxN</td></tr><tr><td rowspan="4">1</td><td rowspan="4">0</td><td rowspan="4">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/MCHx_O = LOWCHx_O/MCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>MCHx_O=OxCPRE ⊕(2)MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE ⊕CHxPCHx_O输出使能</td><td>MCHx_O = LOWMCHx_O输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕CHxPCHx_O输出使能</td><td>MCHx_O=(!OxCPRE)(3) ⊕MCHxPMCHx_O输出使能</td></tr></table>


GD32G553 用户手册


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>CHxEN</td><td>MCHxEN</td><td>CHx_O</td><td>MCHx_O</td></tr><tr><td rowspan="4"></td><td rowspan="4">1</td><td rowspan="4"></td><td rowspan="2">0</td><td>0</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O = CHxPCHx_O输出关闭状态</td><td>MCHx_O=OxCPRE ⊕ MCHxPMCHx_O输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE ⊕ CHxPCHx_O输出使能</td><td>MCHx_O = MCHxPMCHx_O输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE ⊕ CHxPCHx_O输出使能</td><td>MCHx_O=(!OxCPRE) ⊕MCHxPMCHx_O输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / MCHx_O 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / MCHx_O 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；


（3） 详情见中止模式章节。

（4） ⊕：异或操作；

（5） (!OxCPRE)：OxCPRE 信号的互补信号。

## 死区时间插入

设置 MCHxMSEL=2’b11，CHxEN 和 MCHxEN 为 1’b1，同时设置 POEN=1，就可以使能死区插入功能。DTCFG 位域定义了死区时间，死区时间对所有通道有效。死区时间设置的细节请参考0 TIMERx_CCHP0 。

死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM0 模式，当通道 x 匹配发生时（TIMERx 计数器=TIMERx_CHxCV），OxCPRE 翻转。在23-135. 中的 A点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而 MCHx_O 信号立刻变为低电平。同样，在 B点，计数器再次匹配（TIMERx计数器值等于 TIMERx_CHxCV），OxCPRE 信号被清 0，CHx_O 信号被立即清零，MCHx_O 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。

有时会有一些死角事件发生，例如：如果死区延时大于或者等于 CHx_O 信号的占空比，CHx_O信号一直为无效值，如 23-135. 所示。


图 23-135. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e0ee4c20ba71fa37cd8c82a144c839849cf4d0239a84508c8250f96794d0cc04.jpg)


## 不同的死区时间插入

当DTDIFEN位（在TIMERx_CCHP1寄存器中）设置为1时，CHx_O和MCHx_O信号可以输出不同的死区时间，具体如 23-136. DTDIFEN=1 所示。

通道输出准备信号OxCPRE上升沿的死区时间由TIMERx_CCHP0寄存器或TIMERx_FCCHPy寄存器中的DTCFG[7:0]位域配置。OxCPRE信号的下降沿的死区时间由TIMERx_CCHP1寄存器或TIMERx_FCCHPy寄存器中的DTFCFG[7:0]位域配置。

可以在CHx_O和MCHx_O信号输出时修改死区时间。当TIMERx_CCHP1寄存器中的DTMODEN位置1时，可以使能该功能。DTCFG[7:0]位域和DTFCFG[7:0]位域的新值将会在下一次更新事件发生时生效。


图 23-136.不同死区时间的互补输出（DTDIFEN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/25182a1a49f55c8cd74c7902c02eb12dc0e60c77522e67ce39e3f613c555f19b.jpg)


## 中止功能

当 MCHxMSEL = 2’b11（MCHx_O 的输出不使用 MCHxCOMCTL 位配置）时，MCHx_O 输出与CHx_O 输出互补。在这种情况下，CHx_O 和 MCHx_O 信号不能同时设置为有效电平。

通用 L3 定时器具有 BREAK0 中止功能。可以通过将 TIMERx_CCHP0 寄存器中的 BRK0EN 位置1 来使能。中止输入极性由 TIMERx_CCHP0 寄存器中的 BRK0P 位配置，电平有效。

使用 BREAK0 功能时，CHx_O 和 MCHx_O 信号的输出电平由以下位控制：TIMERx_CCHP0 寄存器的 POEN、IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。

中止事件是所有源逻辑或运算的结果。中止功能可以处理三种类型的事件源：

 外部信号源：来自BRKIN0输入；

 系统源：由RCU中的时钟监视器CKM生成的HXTAL卡住事件、LVD锁定事件，Cortex®-M33锁定事件、SRAM奇偶校验错误或FLASH ECC错误事件；

 片上外设源：比较器输出、HPDF的看门狗输出。

BREAK0中止事件也可以由软件置位TIMERx_SWEVG寄存器中的BRK0G位产生。如 23-137.BREAK0 所示，BRKIN0可以从TRIGSEL模块选择GPIO引脚，具体可参考TIMER15_BRKIN TRIGSEL_TIMER15BRKIN 和TIMER16_BRKINTRIGSEL_TIMER16BRKIN 。


图 23-137. BREAK0 中止功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/f4181a3c6c28ca42ab751b26d61fbc84c9f9811bd2403a506bd055ac40d60c34.jpg)


BREAK0可用于处理系统源、片上外设和外部输入信号源的故障，当发生BREAK0中止事件时，输出强制为无效电平，或在死区持续时间之后，输出将以预定的电平（有效或无效）强制输出。

当 MCHxMSEL = 2’b11 且发生 BREAK0 中止事件时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 MCHx_O 的输出由 TIMERx_CTL1 寄存器中的 ISOx 位和 ISOxN 位确定。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。当 IOS=1 时，通道输出情况如 23-138.BREAK0 IOS=1 所示，首先通道互补输出为复位状态，然后死区时间发生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx和 ISOxN 位配置。


图 23-138. 通道响应 BREAK0 中止输入（高电平有效）时，输出信号的行为（IOS=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/58c7814f5f10f03d7ada7cb4aaad8022c1fcf670ec4d36abb2872586f247cb18.jpg)



发生中止事件时，TIMERx_INTF 寄存器的 BRK0IF/BRK1IF 位被置 1。如果 BRKIE=1，中断产生。


## 锁存中止功能

通用定时器L3的中止输入引脚BRKIN0具有锁存中止功能，可通过设置TIMERx_CCHP0寄存器中的BRK0LK位为1，将相应的BRKIN0引脚配置为锁存中止功能。

当使能了锁存中止功能时，需要将 BRKIN0 引脚设置为开漏模式，且低电平有效（BRK0P =0，BRK0IN0P =0）。任何中止源请求发生时，都可以将相应的 BRKIN0 引脚强制为低电平。若 BRKIN0引脚设置为高电平有效（BRK0P=1，BRK0IN0P=1），则锁存中止功能被禁止。

当中止功能使能（将TIMERx_CCHP0寄存器中的BRK0EN=1）时，通过软件将TIMERx_SWEVG寄存器中的BRK0G位置1也可以将BRKIN0引脚强制为低电平。

当中止功能未使能（将TIMERx_CCHP0寄存器中的BRK0EN位为0）时，通过软件将BRK0G位置1，对BRKIN0引脚无影响。但BRK0F标志位会置位，通道输出为安全状态。

将 TIMERx_CCHP0 寄存器中的 BRK0REL 位置 1，可以释放 BRKIN0 引脚，当中止输入源无效时，BRK0REL 位由硬件清零，BRKIN0 引脚将恢复锁存中止功能。

在下面两种情况下，不能释放中止输入引脚 BRKIN0：

 中止输入源有效：虽然BRK0REL位置1，释放了BRKIN0引脚，但由于中止源仍然存在，故中止事件仍然有效；

 POEN=1：通道输出使能时，即使BRK0REL位置1，也不能释放BRKIN0引脚。


表 23-23. 中止功能锁存/释放条件


<table><tr><td>POEN</td><td>BRK0LK</td><td>BRK0REL</td><td>中止输入引脚状态</td></tr><tr><td rowspan="2">0</td><td>1</td><td>0</td><td>锁存</td></tr><tr><td>1</td><td>1</td><td>释放</td></tr></table>

BREAK0 输入引脚 BRKIN0 的锁存中止功能默认是使能的（BRK0REL=0），当 BREAK0 中止事件发生时，可以通过下面的方法来重新配置锁存中止功能：

 BRK0REL=1，释放BRKIN0引脚；

 软件等待系统中止源无效，可通过软件清除SYSBIF标志位；

 软件轮询BRK0REL位，直到BRK0REL=0（硬件实现）。

上述过程完成后，BREAK0 锁存中止功能重新使能，此时，可通过软件将 POEN 置 1 来恢复 PWM输出。


图 23-139. BREAK0 的 BRKIN0 引脚锁存功能逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/f5f782d7a0d41822b026c2cc9933bb9ecd500c76951a3670c36f2c9a51102380.jpg)


## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，可使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL / MCHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE / MOxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。


图 23-140. 单脉冲模式，TIMERx_CHxCV = 0x04，TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e5a8aba688f23f4c09700b80bc7692fc60d798d039bceadb1c4819b928d63c79.jpg)


## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA 请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4，DMATA+0x8, DMATA+0xc 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## UPIF 位备份功能

可以通过配置TIMERx_CTL0寄存器中的UPIFBUEN位来使能UPIF位的备份功能，UPIF和UPIFBU位之间没有延迟，两者完全同步。

使能该功能后，TIMERx_INTF寄存器中的UPIF位将会被实时备份到TIMERx_CNT寄存器中的UPIFBU位。这可以避免在读计数器和中断处理时产生冲突的情况。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL1 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

