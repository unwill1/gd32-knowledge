## 18.2. 通用定时器 L0（TIMERx, x=1,2,3,4）

## 18.2.1. 简介

通用定时器 L0（定时器 1，2，3，4）是 4 通道定时器，支持输入捕获，输出比较，产生 PWM信号控制电机和电源管理。通用定时器 L0 计数器是 16 位（定时器 2~4）或 32 位（定时器 1）无符号计数器。

通用定时器 L0 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 18.2.2. 主要特性

 总通道数：4；

 计数器宽度：16位（定时器2~4），32位（定时器1）；

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

## 18.2.3. 结构框图

18-30. L0 提供了通用定时器 L0 的内部细节。


图 18-30. 通用定时器 L0结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/6f112d5508a6cc5c9b59101e43ef8e09830d17cd8d2da41eb366dcc9591679b2.jpg)


## 18.2.4. 功能描述

## 时钟源配置

通用定时器 L0 可以由内部时钟源 CK_TIMER 或者由 SMC（TIMERx_SMCFG 寄存器位[2:0]）控制的复用时钟源驱动。

 $\mathtt { S M C } [ 2 : 0 ] = = 3 ^ { , } \ \mathtt { b } 0 0 0$ ，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 $\mathtt { S M C } [ 2 : 0 ] = = 3 ^ { \prime } \ \mathtt { b } 0 0 0$ ，默认用来驱动计数器预分频器的是内部时钟源CK_TIMER。当CEN置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。如果将 TIMERx_SMCFG 寄存器的 SMC[2:0]设置为 0x1、0x2、0x3 和 0x7，预分频器被其他时钟源(由 TIMERx_SMCFG 寄存器的 TRGS [2:0]区域选择)驱动，在下文说明。当 SMC 位被设置为 0x4、0x5 和 0x6，计数器预分频器时钟源由内部时钟 CK_TIMER 驱动。


图 18-31. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/7b395eb56484301bba07985b511fa89a4507c15688ffb1642629c1a6a16e856b.jpg)



 SMC[2:0]==3’b111(外部时钟模式0)，定时器选择外部输入引脚作为时钟源


计数器预分频器可以在 TIMERx_CI0/ TIMERx_CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 SMC [2:0]为 0x7 同时设置 TRGS [2:0]为 0x4，0x5 或 0x6 来选择。CIx 是TIMERx_CIx 通过数字滤波器采样后的信号。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置 SMC[2:0]为 0x7 同时设置 TRGS [2:0]为 0x0, 0x1, 0x2 或者 0x3。

 SMC==1’b1(外部时钟模式1)，定时器选择外部输入引脚ETI作为时钟源

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 SMC [2:0]为 0x7 同时设置 TRGS [2:0]为 0x7。注意 ETI 信号是通过数字滤波器采样 ET引脚得到的。如果选择 ETIF 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK)频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-32. 当 PSC 数值从 0 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/151197f9ac4430cc499d36c3396891fa7615ccf60400c984842f61a44ea32802.jpg)


## 计数器向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器(计数器自动重载寄存器，预分频寄存器)都将被更新。

图18-33.向上计数时序图：PSC=0/2和图18-34.向上计数时序图，在运行时改变TIMFRx CAR寄存器的值给出了一些例子，当 TIMERx CAR=0x99 时，计数器在不同预分频因子下的行为。


图 18-33. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/91a997854e073c21721d61b6dad6874d0924085a6497c8e0fd37553c149fe205.jpg)



图 18-34. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/537e1a2330bbdc6d354be3a8ff9307a2e1ff5ad83a317b8367f8e0ddd4f61997.jpg)


## 计数器向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数并产生下溢事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器(计数器自动重载寄存器，预分频寄存器)都将被更新。

18-35. PSC=0/2 和 18-36.TIMERx_CAR 给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 18-35. 向下计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/34ead66e38f346ae3187a98f2be64a97d3f802ee8f3d6fcba55f88cea4bf5747.jpg)



图 18-36. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/4668e4c6869187e985be5c79c8fdd09831f5f607afd6f13d259acda0f35218a1.jpg)


## 计数器中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（自动加载值-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1，然而 CHxIF 位置 1 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 18-37.如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器(计数器自动重载寄存器，预分频寄存器)都将被更新。

18-37. 给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为


图 18-37. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/7f269de2e603a6b0eedad5e4870e121376ff067fa6d0325619b95f1d6ff5e37a.jpg)


## 输入捕获和输出比较通道

通用定时器 L0 拥有四个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

##  输入捕获功能

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 CHxIF 位被置 1，如果 CHxIE = 1 则产生通道中断。


图 18-38. 通道输入捕获原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/b361f989d1347ad66bbe579c8016cff05911f1e6bed8e2e432e4b1c4b6e9e186.jpg)


通 道 输 入 信 号 CIx 有 两 种 选 择 ， 一 种 是 TIMERx_CHx 信 号 ， 另 一 种 是TIMERx_CH0,TIMERx_CH1 和 TIMERx_CH2 异或之后的信号。通道输入信号 CIx 先被TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 选择使用上升沿或者下降沿。配置CHxMS.，可以选择其他通道的输入信号，内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，CHxVAL 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0 寄存器中 CHxCAPFLT）：

根据输入信号和请求信号的质量，配置相应的 CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2 寄存器中 CHxP）：

配置 CHxP 选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0 寄存器中 CHxMS）：

一旦通过配置 CHxMS 选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x0），而且TIMERx_CHxCV 寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN 寄存器中 CHxIE 和 CHxDEN）：

使能相应中断，可以获得中断和 DMA请求。

第五步：捕获使能（TIMERx_CHCTL2 寄存器中 CHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV 被设置成当前计数器的值，CHxIF 为置 1。如果 CHxIF 位已经为 1，则 CHxOF 位置 1。根据 TIMERx_DMAINTEN 寄存器中 CHxIE 和CHxDEN 的配置，相应的中断和 DMA 请求会被提出。

直接产生：软件设置 CHxG 位，会直接产生中断和 DMA 请求。

通道输入捕获功能也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV寄存器测量PWM的周期值，TIMERx_CH1CV寄存器测量PWM占空比值。

 通道输出比较功能


图 18-39. 输出比较原理（x=0,1,2,3）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/169b0452dc89065ee7b8bd931b6e5e79514e038abe80c5f35565d5063d79f01a.jpg)


18-39. x=0,1,2,3 给出了输出比较的原理电路。通道输出信号 CHx_O 与OxCPRE 信号（详情请见 ）的关系描述如下：OxCPRE 信号高电平有效，CHx_O 的输出情况与 OxCPRE 信号，CHxP 位和 CHxEN 位有关（具体情况请见TIMERx_CHCTL2 寄存器中的描述）。例如，当设置 CHxP=0（CHx_O 高电平有效，与 OxCPRE输出极性相同）、CHxEN=1（CHx_O 输出使能）时：

若 OxCPRE 输出有效（高）电平，则 CHx_O 输出有效（高）电平；

若 OxCPRE 输出无效（低）电平，则 CHx_O 输出无效（低）电平。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 寄存器与计数器的值匹配时，根据 的配置，这个通道的输出可以被置高电平，被置低电平或者反转。当计数器的值与CHxCV寄存器的值匹配时，位被置 ，如果 则会产生中断，如果 则会产生 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

设置 CHxCOMSEN 位来配置输出比较影子寄存器；

设置 CHxCOMCTL 位来配置输出模式（置高电平/置低电平/反转）；

设置 CHxP 位来选择有效电平的极性；

设置 CHxEN 使能输出。

第三步：通过 CHxIE/CxCDE 位配置中断/DMA 请求使能。

第四步：通过 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器配置输出比较时基：

CHxVAL 可以在运行时根据你所期望的波形而改变。

第五步：设置 CEN 位使能定时器。

18-40. 显示了三种比较输出模式：反转/置高电平/置低电平，CAR=0x63,CHxVAL=0x3。


图 18-40. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="95">Overflow</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="90">match toggle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="85">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="81">match set</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">match clear</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 输出 PWM功能

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 3’b110，PWM 模式 1 是配置CHxCOMCTL 为 3’b111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM(边沿对齐 PWM)和 CAPWM(中央对齐PWM)。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。18-41. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 18-42. CAPWM 显示了 CAPWM 的输出波形和中断。

在 PWM0 模式下(CHxCOMCTL==3’b110)，如果 TIMERx_CHxCV 寄 存 器 的 值 大 于TIMERx_CAR 寄存器的值，通道输出一直为有效电平。

在 PWM0 模式下(CHxCOMCTL==3’b110)，如果 TIMERx_CHxCV 寄存器的值等于 0，通道输出一直为无效电平。


图 18-41. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/4876976f1fbacf608953ccb022c9eae0a4dd41257b5a3c866ddc85ac254740f0.jpg)



图 18-42. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/c03c3af09b2c6d3f9a2de06e61fdfb573c101c5132ccf030b88727f0bc0277cd.jpg)


## 通道输出准备信号

根据 18-39. x=0,1,2,3 所示，当 TIMERx 用于输出匹配比较模式下，设置CHxCOMCTL 位可以定义 OxCPRE 信号(通道 x 准备信号)类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06或0x07可以配置 PWM模式0/PWM模式1。在这些模式中，根据计数器值和 TIMERx_CHxCV寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFE 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 正交译码器

参考 。

## 霍尔传感器接口功能

参考霍尔传感器接口功能

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式，可以通过设置TIMERx_SMCFG 寄存器中的 SMC [2:0]配置这些模式。这些模式的输入触发源可以通过设置TIMERx_SMCFG 寄存器中的 TRGS [2:0]来选择。


表 18-5. 从模式列表和举例


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>SMC[2:0]3&#x27;b100 (复位模式)3&#x27;b101 (暂停模式)3&#x27;b110 (事件模式)</td><td>TRGS[2:0]000: ITI0001: ITI1010: ITI2011: ITI3100: CI0F_ED101: CI0FE0110: CI1FE1111: ETIFP</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP来选择极性和反相如果触发源是ETIF,配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Clx,配置CHxCAPFLT设置滤波,分频不可用触发源是ETIF,滤波和预分频不可用</td></tr><tr><td>例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TRGIS[2:0]=3&#x27;b000选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="3">极性选择</td><td>滤波和预分频</td></tr><tr><td rowspan="2"></td><td colspan="6">图18-43.复位模式</td></tr><tr><td colspan="6">TIMER_CKCENCNT_REG5E5F606162630001020304000102UPIFITIOTRIGIFInternal sync delay</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TRGIS[2:0]=3&#x27;b101选择CIOFE0为触发源</td><td colspan="3">TIOS=0.(非异或)CHOP==0不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="6">图18-44.暂停模式</td></tr><tr><td>例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TRGIS[2:0]=3&#x27;b111选择ETIF为触发源.</td><td colspan="2">ETP=0没有极性改变</td><td colspan="2">ETPSC=1,2分频.ETFC=0,无滤波</td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td></td><td colspan="4">图18-45.事件模式</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置 TIMERx_CTL0 寄存器的 SPM 位置 1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置 CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。为了最大限度减少延迟，用户可以将 TIMERx_CHCTL0/1 寄存器的 CHxCOMFEN 位置 1。单脉冲模式下，触发上升沿产生之后， OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。只有输出通道配置为 PWM0 或 PWM1 输出运行模式下时 CHxCOMFEN 位才可用，触发源来源于触发信号。

18-46. TIMERx_CHxCV = 4 TIMERx_CAR=99展示了一个例子。


图 18-46. 单脉冲模式，TIMERx_CHxCV = 4 TIMERx_CAR=99


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/33674089-c356-4ef9-9780-23070496ac3a/d11efa7c6ad9f00ee111c17bf8f8e84687d76692d370460f19ed4a502e3dabc1.jpg)


## 定时器互连

参考 。

## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA配置成 M2P 模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA请求就可以完成。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示4次传输，定时器就需要再多发3次DMA请求。在这3次请求下，DMA对TIMERx_DMATB寄存器的访问会映射到访问定时器的DMATA+0x4, DMATA+0x8, DMATA+0xc寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL0 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

