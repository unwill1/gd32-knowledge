## 13.2. 通用定时器 L0（TIMERx, x=1,2,3,4）

## 13.2.1. 简介

通用定时器 L0（TIMER1/2/3/4）是 4 通道定时器，支持输入捕获，输出比较，产生 PWM 信号控制电机和电源管理。通用定时器 L0 的计数器是 16 位或 32 位无符号计数器。

通用定时器 L0 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 13.2.2. 主要特性

 总通道数：4；

 计数器宽度：16位（TIMER2/3/4）和32位（TIMER1）；

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

## 13.2.3. 结构框图

13-48. L0 提供了通用定时器 L0 的内部细节


图 13-48. 通用定时器 L0结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/30fe6a0477ec09235bf6ce0220805ee2c8d04055012d4ca1a93c76927033309f.jpg)


## 13.2.4. 功能描述

## 时钟源选择

通用定时器 L0 可以由内部时钟源 CK_TIMER 或者由 SYSCFG_TIMERxCFG(x=1..4)寄存器中的TSCFGy[4:0] (y=0..6,9..15)位域控制的复用时钟源驱动。

 当 $\mathsf { I S Y S C F G \_ T I M E R x C F G } ( \mathsf { x } = 1 \ldots 4 )$ 寄存器中的 $\mathsf { T S C F G y } [ 4 ; 0 ] = 5 ^ { \prime } \mathsf { b 0 0 0 0 0 } ( \mathsf { y } = \mathsf { y } = 0 . . 6 , 9 . . 1 5 )$ 时，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 $\mathtt { S Y S C F G \_ T I M E R x C F G } ( { \tt x } = 1 \_ { 4 } )$ 寄存器中的 ${ \mathsf { T S C F G y } } [ 4 ; 0 ] = 5 { \mathsf { b 0 0 0 0 0 } } \ ( \forall \mathbf { = } 0 . . 6 , 9 . . 1 5 )$ ，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

如果 $\mathtt { S Y S C F G \_ T I M E R x C F G } ( { \tt x } = 1 \_ { 4 } )$ 寄存器中的 TSCFGy[4:0] (y=0..2,6,9..14)位域设置为非零值，预分频器被其他时钟源驱动，具体在下文说明。当 TSCFGy[4:0] (y=3,4,5)被设置为非零值时，计数器预分频器时钟源由内部时钟 TIMER_CK 驱动。


图 13-49. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/af3aa2cfa6916afa3f2f9138f278f863d5929e16165b2de0dbeb27246a84a261.jpg)



 TSCFG6[4:0] !=5’b00000（外部时钟模式0），定时器选择外部输入引脚作为时钟源


计数器预分频器可以在 TIMERx_CI0/ TIMERx_CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[4:0]为 0x5，0x6 或 0x7 来选择。CIx 是 TIMERx_CIx 通过数字滤波器采样后的信号。

计数器预分频器也可以在内部触发信号 ITI0~ITI3 的上升沿计数。这种模式可以通过设置TSCFG6[4:0]为 0x1~0x4 来选择。

SMC1= 1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG 寄存器中的 SMC1 位为 1 来选择。另一种选择 ETI 信号作为时钟源方式是，设置 TSCFG6[4:0]为 0x8。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择 ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 13-50. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/e24ff8150af65d649329a89406fc537f8c8edf3d1b319e69b62444ec3a9b7885.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

13-51. PSC=0/2 和 13-52. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 13-51. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/1c084dc9d6ada0b125cd7bf980a771b74291f0b351839267aec560d4009171a3.jpg)



图 13-52. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/820388a188d556f14887f643a6438093405a06914c9583763b421f2c1e39abd5.jpg)


## 向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数并产生下溢事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

13-53. PSC=0/2 和 13-54. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 13-53. 向下计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/02c7a87ed64f76b3fc3ed462b66ea5e789c06d625b9f418b3f1955dd4aab0e09.jpg)



图 13-54. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/89db5c0227cf210971c0ead330e2299a2de04c20516bf7c7bc66ad1544e8785d.jpg)


## 中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（TIMERx_CAR-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。计数方向被硬件自动更新。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1，然而 CHxIF 位置 1 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 13-55. 。如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

13-55. 给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为


图 13-55. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c1c7d49c65b4d5eeb4a3aff9d6ccb2f3b9eac78375ae5d297918f317914f0291.jpg)


## 捕获/比较通道

通用定时器 L0 拥有四个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

##  输入捕获模式

捕获模式允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 CHxIF 位被置 1，如果 CHxIE = 1 则产生通道中断。


图 13-56. 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/f6513d66f41001a5bc6d5b236bed6ad0ca5813056d861b6440b5731baa6aa00e.jpg)


通道输入信号 CIx 有两种选择，一种是 TIMERx_CHx 信号，另一种是 TIMERx_CH0,TIMERx_CH1和 TIMERx_CH2 异或之后的信号（仅限于 CI0）。通道输入信号 CIx 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP选择使用上升沿或者下降沿。配置 CHxMS，可以选择其他通道的输入信号，内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，CHxVAL 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0 寄存器中 CHxCAPFLT）：

根据输入信号和请求信号的质量，配置相应的 CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2 寄存器中 CHxP）：

配置 CHxP选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0 寄存器中 CHxMS）：

一旦通过配置 CHxMS 选择输入捕获源，必须确保通道配置在输入模式（CHxMS!=0x0），而且TIMERx_CHxCV 寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN 寄存器中 CHxIE 和 CHxDEN）：

使能相应中断，可以获得中断和 DMA请求。

第五步：捕获使能（TIMERx_CHCTL2 寄存器中 CHxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV 被设置成当前计数器的值，CHxIF 为置 1。如果 CHxIF 位已经为 1，则 CHxOF 位置 1。根据 TIMERx_DMAINTEN 寄存器中 CHxIE 和 CHxDEN的配置，相应的中断和 DMA 请求会被提出。

直接产生：软件设置 CHxG 位，会直接产生中断和 DMA 请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0 并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV 寄存器测量PWM 的周期值，TIMERx_CH1CV 寄存器测量 PWM 占空比值。

 输出比较模式


图 13-57. 输出比较逻辑（x=0,1,2,3）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/c98b7cade121814144ef6fc646a1d26eba5edcde46d49b0d4f65edcded5a9e86.jpg)


13-57. x=0,1,2,3 给出了输出比较的逻辑电路。通道输出信号 CHx_O 与OxCPRE 信号（详情请见 ）的关系描述如下：OxCPRE 信号高电平有效，CHx_O的输出情况与 OxCPRE 信号，CHxP 位和 CHxEN 位有关（具体情况请见 TIMERx_CHCTL2 寄存器中的描述）。例如，当设置 CHxP=0（CHx_O 高电平有效，与 OxCPRE 输出极性相同）、CHxEN=（CHx_O 输出使能）时：

若 OxCPRE 输出有效（高）电平，则 CHx_O 输出有效（高）电平；

若 OxCPRE 输出无效（低）电平，则 CHx_O 输出无效（低）电平。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 CHxCV 寄存器与计数器的值匹配时，根据 CHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者翻转。当计数器的值与 CHxCV 寄存器的值匹配时，CHxIF 位被置 1，如果 CHxIE = 1 则会产生中断，如果 CxCDE=1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

设置 CHxCOMSEN 位来配置输出比较影子寄存器；

设置 CHxCOMCTL 位来配置输出模式（置高电平/置低电平/翻转）；

设置 CHxP位来选择有效电平的极性；

设置 CHxEN 使能输出。

第三步：通过 CHxIE/CxCDE 位配置中断/DMA 请求使能。

第四步：通过 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器配置输出比较时基：

CHxVAL 可以在运行时根据你所期望的波形而改变。

第五步：设置 CEN 位使能定时器。

13-58. 显示了三种比较输出模式：翻转/置高电平/置低电平，CAR=0x63,CHxVAL=0x3。


图 13-58. 三种输出比较模式


<table><tr><td>CNT_CLK</td><td></td></tr><tr><td>CEN</td><td></td></tr><tr><td>CNT_REG</td><td>00 01 02 03 04 05 ... 62 63 00 01 02 03 04 05 ... 62 63 00 01 02 03 04 05 ...</td></tr><tr><td>上溢</td><td></td></tr><tr><td colspan="2">匹配翻转</td></tr><tr><td>OxCPRE</td><td></td></tr><tr><td colspan="2">匹配位置</td></tr><tr><td>OxCPRE</td><td></td></tr><tr><td colspan="2">匹配清零</td></tr><tr><td>OxCPRE</td><td></td></tr></table>

## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 4’b0110，PWM 模式 1 是配置CHxCOMCTL 为 4’b0111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。13-59. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）

决定。 13-60. CAPWM 显示了 CAPWM 的输出波形和中断。

当计数器向上计数时，在 PWM0 模式下（CHxCOMCTL =4’b0110），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为有效电平；PWM1 模式下（CHxCOMCTL=4’b0111），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为无效电平。


图 13-59. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/50bd84285f6bf475c7a80c36749580138c9c82f1e426f4b1fb97adbc5cd25448.jpg)



图 13-60. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/146b4cdba24b03476b1dc11e779c5401fc783e0ca8d4a8f563e27b34eefa2792.jpg)


## 通道输出参考信号

根据 13-57. x=0,1,2,3 所示，当 TIMERx 用于输出匹配比较模式下，设置CHxCOMCTL 位可以定义 OxCPRE 信号（通道 x 准备信号）类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06 或0x07 可以配置 PWM 模式 0/PWM 模式 1。在这些模式中，根据计数器值和 TIMERx_CHxCV 寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。

## 正交译码器

正交译码器功能使用由 TIMERx_CH0 和 TIMERx_CH1 引脚生成的 CI0 和 CI1 正交信号各自相互作用产生计数值。在每个输入源改变期间，DIR 位被硬件自动改变。

输入源可以是只有 CI0，可以只有 CI1，或着可以同时有 CI0 和 CI1，通过设置 TSCFGy[4:0]( y =0, 1, 2, 13, 14) != 5’b00000 来选择使用哪种模式。计数器计数方向改变的机制如 13-6.所示。其中，CI0FE0、CI1FE1 是经过滤波和极性选择后的 CI0、CI1 信号。正交译码器可以当作一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动加载值之间连续的计数。因此，用户必须在计数器开始计数前配置 TIMERx_CAR 寄存器。


表 13-8. 不同译码器模式下的计数方向


<table><tr><td rowspan="2">计数模式</td><td rowspan="2">电平</td><td colspan="2">CI0FE0</td><td colspan="2">CI1FE1</td></tr><tr><td>上升</td><td>下降</td><td>上升</td><td>下降</td></tr><tr><td rowspan="2">正交译码器模式0TSCFG0[4:0]!= 5'b00000</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>-</td><td>-</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>-</td><td>-</td></tr><tr><td rowspan="2">正交译码器模式1TSCFG1[4:0]!= 5'b00000</td><td>CI0FE0=1</td><td>-</td><td>-</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>-</td><td>-</td><td>向下</td><td>向上</td></tr><tr><td rowspan="4">正交译码器模式2TSCFG2[4:0]!= 5'b00000</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>X</td><td>X</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>X</td><td>X</td></tr><tr><td>CI0FE0=1</td><td>X</td><td>X</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>X</td><td>X</td><td>向下</td><td>向上</td></tr><tr><td rowspan="2">正交译码器模式3TSCFG13[4:0]!= 5'b00000</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>-</td><td>-</td></tr><tr><td>CI1FE1=0</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>正交译码器模式4</td><td>CI0FE0=1</td><td>-</td><td>-</td><td>向上</td><td>向下</td></tr><tr><td>TSCFG14[4:0]!= 5'b00000</td><td>CI0FE0=0</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>


注意：“-”意思是“无计数”；“X" 意思是不可能。“0”意思是低电平，“1”意思是高电平。



图 13-61. 译码器接口模式下计数器运行例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/747271329655feb31ebcb0675d154d0e23f763938b573bf7c80f9cd1dd6f2d0c.jpg)



图 13-62. CI0FE0 极性反相的译码器接口模式下的例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/ea6be67b5badd4cb3c788044250cc8348b9e134947dd8c61bf91c0726ebca139.jpg)



当正交译码器模式下计数器计数方向发生变化时，TIMERx_CTL0 寄存器中的 DIR 位发生改变。


## 正交译码器信号检测

支持两种正交译码器信号检测：信号跳变检测和断线检测。

正交译码器信号跳变检测功能可用于检测两个正交译码器输入信号 CI0、CI1 的电平跳变沿（上升沿或下降沿）是否同时发生，可通过将 TIMERx_CTL2 寄存器中的 DECJDEN 位置 1 来使能。当DECJDEN=1 时，若两个正交信号 CI0 和 CI1 的电平跳变同时发生，则中断标志位 DECJIF 置位。若 DECJIE=1，则相应的中断产生。

正交译码器信号断线检测功能可用于检测正交译码器输入信号 CI0、CI1 是否正常，可通过将TIMERx_CTL2 寄存器中的 DECDISDEN 位置 1 来使能。正交译码器信号检测模块包括 2 个 32位的看门狗计数器和 1 个周期寄存器，具体如 13-63. 所示，CI0FE0、CI1FE1 信号分别用于复位 2 个看门狗计数器。

当 DECDISDEN=1 时，2 个看门狗计数器同时开始向上计数，若看门狗计数器计数到看门狗周期值（该值由 TIMERx_WDGPER 寄存器中的 WDGPER[31:0]位域确定），则看门狗计数器计数超时，中断标志位 DECDISIF 置位。若 DECDISIE=1，则相应的中断产生。


图 13-63. 正交译码器信号断线检测框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/301cbf46101fabb35d4a02ea2a04f80c098c728562496fd79a49a96267617096.jpg)


## 非正交译码器

非正交译码器功能有 4 种模式：非正交译码器模式 0~3，通过设置 TSCFGy[4:0](y = 9, 10, 11,12) != 5’b00000 来选择。这 4 种计数模式下的输入源有两个：CI0 和 CI1，其中，CI0FE0、CI1FE1是经过滤波和极性选择后的 CI0、CI1 信号。

使用非正交译码器模式 0/1 时，CI0FE0 作为计数方向信号，CI1FE1 作为计数脉冲。

其中，CH0P用于计数方向选择：当 CH0P=0 时，CI0FE0 为高电平时向上计数，CI0FE0 为低电平时向下计数；当 CH0P=1 时，CI0FE0 为高电平时向下计数，CI0FE0 为低电平时向上计数。

CH1P用于选择 CI1FE1 信号的计数边沿：非正交译码器模式 0 时，计数器在 CI1FE1 信号的上升沿和下降沿进行计数；非正交译码器模式 1 时，当 CH1P=0 时，在 CI1FE1 信号的上升沿计数，当 CH1P=1 时，在 CI1FE1 信号的下降沿计数。更多非正交译码器模式 1 的细节如 13-9.1 和 13-64. 0/1 CH1P=0 所示。


表 13-9.非正交译码器模式 1 的计数情况


<table><tr><td>CH1P</td><td>电平</td><td>计数器计数情况</td></tr><tr><td rowspan="2">0</td><td>CI0FE0为高电平</td><td>计数器在CI1FE1信号的上升沿向上计数</td></tr><tr><td>CI0FE0为低电平</td><td>计数器在CI1FE1信号的上升沿向下计数</td></tr><tr><td rowspan="2">1</td><td>CI0FE0为高电平</td><td>计数器在CI1FE1信号的下降沿向上计数</td></tr><tr><td>CI0FE0为低电平</td><td>计数器在CI1FE1信号的下降沿向下计数</td></tr></table>


图 13-64. 非正交译码器模式 0/1 计数器运行实例（CH1P=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/995294c192ebd604f710d9ada674cd0e4ac0676df936dbb7e6f1074b13553195.jpg)


非正交译码器模式 2/3 由 CI0FE0、CI1FE1 信号各自相互作用产生计数值，DIR 位被硬件自动改变。

非正交译码器模式 2 时，计数器在 CI0FE0、CI1FE1 信号的上升沿和下降沿进行计数，计数方向由 CH0P和 CH1P 确定；非正交译码器模式 3，计数器在 CI0FE0、CI1FE1 信号的上升沿或下降沿进行计数，当 CHxP=0 时，信号为高电平时计数，或在信号的下降沿计数；当 CHxP=1 时，信号为低电平时计数，或在信号上升沿计数。具体情况请见 13-65. 2 / 3CH0P / CH1P=0 和 13-10. 2 / 3 。


图 13-65. 非正交译码器模式 2 / 3 计数器运行实例（CH0P / CH1P=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/20cc90a90819ec628ac58ce56ca152a42c445a82e3fddf90e69ec8a4a1f5b652.jpg)



表 13-10. 非正交译码器模式 2 / 3 下的计数方向


<table><tr><td rowspan="2">计数模式</td><td rowspan="2">极性</td><td rowspan="2">电平</td><td colspan="2">CI0FE0</td><td colspan="2">CI1FE1</td></tr><tr><td>上升</td><td>下降</td><td>上升</td><td>下降</td></tr><tr><td rowspan="8">非正交译码器模式2TSCFG11[4:0]!= 5&#x27;b00000</td><td rowspan="4">CHxP=0(x = 0, 1)</td><td>CI1FE1=1</td><td>向下</td><td>向下</td><td>x</td><td>x</td></tr><tr><td>CI1FE1=0</td><td>-</td><td>-</td><td>x</td><td>x</td></tr><tr><td>CI0FE0=1</td><td>x</td><td>x</td><td>向上</td><td>向上</td></tr><tr><td>CI0FE0=0</td><td>x</td><td>x</td><td>-</td><td>-</td></tr><tr><td rowspan="4">CHxP=1(x = 0, 1)</td><td>CI1FE1=1</td><td>-</td><td>-</td><td>x</td><td>x</td></tr><tr><td>CI1FE1=0</td><td>向下</td><td>向下</td><td>x</td><td>x</td></tr><tr><td>CI0FE0=1</td><td>x</td><td>x</td><td>-</td><td>-</td></tr><tr><td>CI0FE0=0</td><td>x</td><td>x</td><td>向上</td><td>向上</td></tr><tr><td rowspan="8">非正交译码器模式3TSCFG12[4:0]!= 5&#x27;b00000</td><td rowspan="4">CHxP=0(x = 0, 1)</td><td>CI1FE1=1</td><td>-</td><td>向下</td><td>x</td><td>x</td></tr><tr><td>CI1FE1=0</td><td>-</td><td>-</td><td>x</td><td>x</td></tr><tr><td>CI0FE0=1</td><td>x</td><td>x</td><td>-</td><td>向上</td></tr><tr><td>CI0FE0=0</td><td>x</td><td>x</td><td>-</td><td>-</td></tr><tr><td rowspan="4">CHxP=1(x = 0, 1)</td><td>CI1FE1=1</td><td>-</td><td>-</td><td>x</td><td>x</td></tr><tr><td>CI1FE1=0</td><td>向下</td><td>-</td><td>x</td><td>x</td></tr><tr><td>CI0FE0=1</td><td>x</td><td>x</td><td>-</td><td>-</td></tr><tr><td>CI0FE0=0</td><td>x</td><td>x</td><td>向上</td><td>-</td></tr></table>


当非正交译码器模式下计数器计数方向发生变化时，TIMERx_CTL0 寄存器中的 DIR 位改变。


## 正交译码器和非正交译码器的时钟输出

定时器可以通过 TRGO 输出译码器时钟输出信号。该功能仅用于正交译码器模式 0~4 和非正交译码器模式 0~3，通过将 TIMERx_CTL1 寄存器中 MMC[3:0]位域设置为 4'b1000 来使能。

## 霍尔传感器接口功能

参考 TIMERx, x=0, 7 。

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式等，可以通过设置SYSCFG_TIMERxCFG(x=1..4)寄存器中的 TSCFGy[4:0] (y=3..6)位域来确定，具体的输入触发源可以通过 TSCFGy[4:0] (y=3..6)位域值来选择。


表 13-11. 从模式列表和举例（通用定时器 L0）


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="2">极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[4:0]y=3:复位模式y=4:暂停模式y=5:事件模式y=6:外部时钟模式0</td><td>TSCFGy[4:0]00000:Mode disable00001:ITI000010:ITI100011:ITI200100:ITI300101:CI0F_ED00110:CI0FE000111:CI1FE101000:ETIFP(1)01001:CI2FE201010:CI3FE3</td><td colspan="2">如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相。如果触发源是ETIFP(滤波后的ETI外部触发输入),配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Clx,配置CHxCAPFLT设置滤</td></tr><tr><td></td><td></td><td></td><td colspan="2"></td><td>波,分频不可用触发源是ETIFP,配置ETFC设置滤波,配置ETPSC设置预分频</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[4:0]5'b00001,选择ITIO为触发源</td><td colspan="2">触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="5">图13-66.复位模式TIMER_CKCENCNT_REGUPIFITIOTRIGIF</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[4:0]=5'b00110,选择CI0FE0为触发源</td><td colspan="2">TIOS=0(非异或)[CHONP=0,CHOP=0]不反相,在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="5">图13-67.暂停模式<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/b13741fa1351ae81b3d58827fc7ae4f2b46d5c2dedf6c069662bce90675ea14e.jpg"/></td></tr><tr><td>例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[4:0]=5'b01000,选择ETIFP为触发源</td><td>ETP=0没有极性改变</td><td colspan="2">ETPSC=1,2分频ETFC=0,无滤波</td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td rowspan="6"></td><td colspan="4">图13-68.事件模式</td></tr><tr><td>TIMER_CK</td><td></td><td></td><td></td></tr><tr><td>ETI</td><td></td><td></td><td></td></tr><tr><td>ETIFP</td><td></td><td></td><td></td></tr><tr><td>CNT_REG</td><td></td><td>5E</td><td>5F 60 61</td></tr><tr><td>TRGIF</td><td></td><td></td><td></td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置TIMERx_CTL0寄存器的SPM位置1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。如果 CEN 值被硬件更新事件自动清 0，计数器将被再次初始化。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。单脉冲模式下，触发上升沿产生之后，OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。


图 13-69. 单脉冲模式，TIMERx_CHxCV = 0x04 TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/258e8a4c-c579-4dba-82fb-d3ed6b6fd31a/86902dbd0d85f0d975f0d5e4d74a96f4573b8769dafa8e076beaf920a03c6b1f.jpg)


## 定时器互连

参考 TIMERx, x=0, 7 。

## 定时器 DMA 模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。当然，必须要使能 DMA 请求，一些内部中断事件可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA 配置成 M2P模式，PADDR 是 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由 TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC 位域值为 0，表示 1 次传输，定时器的发送 1 个 DMA 请求就可以完成。如果TIMERx_DMACFG 寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次 DMA 请求。在这 3 次请求下，DMA 对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的 DMATA+0x4, DMATA+0x8，DMATA+0xc 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA 请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M33 内核停止，DBG_CTL 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。

