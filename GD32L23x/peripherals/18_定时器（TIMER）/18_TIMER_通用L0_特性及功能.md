## 18.2. 通用定时器 L0（TIMERx，x=1，2）

## 18.2. 1. 简介

通用定时器 L0（TIMER1，2）是 4 通道定时器，支持输入捕获，输出比较，产生 PWM 信号控制电机和电源管理。通用定时器 L0 计数器是 16 位无符号计数器。

通用定时器 L0 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 18.2.2. 主要特征

◼ 总通道数：4；

◼ 计数器宽度：16位；

◼ 时钟源可选：内部时钟，内部触发，外部输入，外部触发；

◼ 多种计数模式：向上计数，向下计数和中央计数；

◼ 正交译码器接口：被用来追踪运动和分辨旋转方向和位置；

◼ 霍尔传感器接口：用来做三相电机控制；

◼ 可编程的预分频器：16位，运行时可以被改变；

◼ 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

◼ 自动重装载功能；

◼ 中断输出和DMA请求：更新事件，触发事件，比较/捕获事件；

◼ 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

◼ 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

◼ 定时器主-从管理。

## 18.2.3. 结构框图

18-32. GD32L233 L0 提供了通用定时器 L0 的内部细节。


图 18-32. GD32L233 通用定时器 L0 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/ac9c2b6b28e98331d4f8d033281208f83da75fa9cd6833870a04e7cb481dcaee.jpg)



18-33. GD32L235 L0 提供了通用定时器 L0 的内部细节。



图 18-33. GD32L235 通用定时器 L0 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/c969cf31b9c5fc8439e5ad2ca3f182eed07585e98b6c93018f7c45da7087358b.jpg)


## 18.2.4. 功能说明

GD32L233 时钟源配置

通用定时器 L0 可以是内部时钟源 CK_TIMER，或者是由 SMC（TIMERx_SMCFG 寄存器位[2:0]）位确定的时钟源。

◼ SMC[2:0]=3’b000，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 SMC[2:0]=3’b000，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

如果将 TIMERx_SMCFG 寄存器的 SMC[2:0]设置为 0x1、0x2、0x3 和 0x7，预分频器被其他时钟源（由 TIMERx_SMCFG 寄存器的 TRGS[2:0]区域选择）驱动，在下文说明。当 SMC 位被设置为 0x4、0x5 和 0x6，计数器预分频器时钟源由内部时钟 CK_TIMER 驱动。


图 18-34. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/f8a0b8e0903fb8af505c3df9719f2a94aec7a0ebb53d594649d7bda522c5114f.jpg)



◼ SMC[2:0]=3’b111（外部时钟模式0），定时器选择外部输入引脚作为时钟源。


计数器预分频器可以在 TIMERx_CH0/ TIMERx_CH1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 SMC[2:0]为 0x7 同时设置 TRGS[2:0]为 0x4，0x5 或 0x6 来选择。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置SMC[2:0]为 0x7 同时设置 TRGS[2:0]为 0x0，0x1，0x2 或者 0x3。

◼ SMC1=1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源。

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 SMC[2:0]为 0x7 同时设置 TRGS[2:0]为 0x7。注意 ETI 信号是通过数字滤波器采样 ET引脚得到的。如果选择 ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## GD32L235 时钟源配置

通用定时器 L0 可以是内部时钟源 CK_TIMER，或者是由 TSCFGy[3:0]位确定的时钟源，TSCFGy[3:0]位于 SYSCFG_TIMER0CFG，（y=0,1…7）。

TSCFGy[3:0] =4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或SYSCFG_TIMER2CFG，（y=0,1…7），定时器选择内部时钟源（连接到RCU模块的CK_TIMER）。

当 TSCFGy[3:0] =4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或SYSCFG_TIMER2CFG，（y=0,1…7），默认用来驱动计数器预分频器的是内部时钟源CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

如 果 TSCFGy[3:0] !=4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或SYSCFG_TIMER2CFG，（y=0,1,2,6），预分频器被其他时钟源（由TSCFG6[3:0]区域选择）驱动，更多细节在下文说明，当TSCFGy[3:0]（y=3,4,5）设置为有效值时，计数器预分频器时钟源由内部时钟TIMER_CK驱动。


图 18-35. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/90addc3d45ea022fc45a12de9ae64be1dedd9cc3b995bbdee755c0fdd0a16cf6.jpg)


◼ TSCFG6[3:0] !=4’b0000（外部时钟模式0），定时器选择外部输入引脚作为时钟源。

计数器预分频器可以在 TIMERx_CH0/ TIMERx_CH1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[3:0]为 0x5，0x6 或 0x7 来选择。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置TSCFG6[3:0]为 0x1，0x2，0x3 或者 0x4。

◼ SMC1=1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源。

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 TSCFG6[3:0]为 0x8。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-36. 当 PSC 数值从 0 变到 2 时，计数器的时序图


<table><tr><td>TIMER_CK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CEN</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PSC value</td><td>0</td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td></tr><tr><td>Prescaler shadow</td><td>0</td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>Prescaler CNT</td><td>0</td><td></td><td></td><td>0</td><td>1</td><td>2</td><td>0</td><td>1</td><td>2</td></tr><tr><td>PSC_CLK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT_REG</td><td>94</td><td>95</td><td>96</td><td>97</td><td>98</td><td>99</td><td>0</td><td>1</td><td>2</td></tr><tr><td>UPG</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reload Pulse</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 计数器向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器（计数器自动重载寄存器，预分频寄存器）都将被更新。

18-37. PSC=0/2 和 18-38.

TIMERx_CAR 给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同预分频因子下的行为。


图 18-37. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/6557bc4562bd91ad26352468bbebf4679475edfd628f245aa7457083c0195193.jpg)



图 18-38. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/bbec0e731834f2abf2514d240bd7a50075e3c15baaf33bb949ed79a165deb9b3.jpg)


## 计数器向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数并产生下溢。在向下计数模式中，TIMERx_CTL0寄存器中的计数方向控制位DIR应该被设置成1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器（计数器自动重载寄存器，预分频寄存器）都将被更新。

18-39. PSC=0/2 和 18-40.TIMERx_CAR 给出了一些例子，当 TIMERx_CAR=0x99 时，计数器在不同时钟频率下的行为。


图 18-39. 向下计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/cc3fbcc580920a2e1e16552b55ae3fc309d01f58f1728acfb4d071f3a9f44eaa.jpg)



图 18-40. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/6c796071067ce4f7f430c2385d5569ea4b4d82aed1c74097d9f919f1ba88381e.jpg)


## 计数器中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（自动加载值-1）产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0寄存器中的计数方向控制位 DIR 只读，表明了的计数方向。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时， 寄存器中的 位都会被置 。但是 位是否置 与TIMERx_CTL0 寄存器中 CAM 的值有关。具体细节参考 18-41.。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器（计数器自动重载寄存器，预分频寄存器）都将被更新。

18-41. 给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x99 ，TIMERx_PSC=0x0 时，计数器的行为。


图 18-41. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/edf69cd135cdb51869f22b6e302d87422f2cd649f7f43ee7e543372f0ad68d41.jpg)


## 输入捕获和输出比较通道

通用定时器 L0 拥有四个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

## 通道输入捕获功能

通道输入捕获功能允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 ChxIF 位被置 1，如果 ChxIE =1 则产生通道中断。


图 18-42. 通道输入捕获原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/be32f7a4b4602c1e11059ff2c785a8b2f50035b17fa9b8982f6a2e52e2f5b227.jpg)


通道输入信号 Cix 有两种选择，一种是 TIMERx_CHx 信号，另一种是 TIMERx_CH0，TIMERx_CH1 和 TIMERx_CH2 异或之后的信号。通道输入信号 Cix 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP选择使用上升沿或者下降沿。配置 CHxMS，可以选择其他通道的输入信号，内部触发信号。配置 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，CHxVAL 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT）：根据输入信号和请求信号的质量，配置相应的CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP）：配置CHxP选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS）：一旦通过配置CHxMS选 择 输 入 捕 获 源 ， 必 须 确 保 通 道 配 置 在 输 入 模 式（CHxMS!=0x0），而且TIMERx_CHxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中ChxIE 和 CHxDEN）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中ChxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV被设置成当前计数器的值，ChxIF为置1。如果ChxIF位已经为1，则ChxOF位置1。根据TIMERx_DMAINTEN寄存器中ChxIE和CHxDEN的配置，相应的中断和DMA请求会被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV寄存器测量PWM的周期值，TIMERx_CH1CV寄存器测量PWM占空比值。

通道输出比较功能


图 18-43. 通道输出比较原理（x=0，1，2，3）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/1853f93a55203d8ed52b9b1d9c086cacd0290506c9d49cf6717a0408c76d9691.jpg)


18-43. x=0 1 2 3 给出了输出比较的原理电路。通道输出信号 CHx_O与 OxCPRE 信号（详情请见 ）的关系描述如下：OxCPRE 信号高电平有效，CHx_O 的 输 出 情 况 与 OxCPRE 信 号 ，CHxP 位 和 ChxE 位 有 关 （ 具 体 情 况 请 见TIMERx_CHCTL2 寄存器中的描述）。例如，当设置 CHxP=0（CHx_O 高电平有效，与 OxCPRE输出极性相同）、ChxE=1（CHx_O 输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_O输出有效（高）电平；

若OxCPRE输出无效（低）电平，则CHx_O输出无效（低）电平。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 CHxCV 寄存器与计数器的值匹配时，根据 CHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者反转。当计数器的值与CHxCV寄存器的值匹配时，ChxIF 位被置 1，如果 ChxIE = 1 则会产生中断，如果 CxCDE=1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

设置CHxCOMSEN位来配置输出比较影子寄存器；

设置 $\mathsf { C H x C O M C T L }$ 位来配置输出模式（置高电平/置低电平/反转）；

设置 ${ \mathsf { C H } } { \mathsf { x P } }$ 位来选择有效电平的极性；

设置ChxEN使能输出。

第三步：通过ChxIE/CxCDE位配置中断/DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

CHxVAL可以在运行时根据你所期望的波形而改变。

第五步：设置CEN位使能定时器。

18-44. 显示了三种比较输出模式：反转/置高电平/置低电平，CAR=0x63，

CHxVAL=0x3。 


图 18-44. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="95">Overflow</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="90">match toggle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="85">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="80">match set</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="15">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="15">match clear</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="15">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 输出 PWM功能

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 3’b110，PWM 模式 1 是配置CHxCOMCTL 为 3’b111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐 PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。18-45. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 18-46. CAPWM 显示了 CAPWM 的输出波形和中断。

在向上计数模式中， PWM 模式 0 下（CHxCOMCTL=3’b110），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为无效电平；PWM 模式 1 下（CHxCOMCTL=3’b111），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为有效电平。


图 18-45. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/90fb8f14a8cddc2c96e9e374343f171a85a7312c9119a6906035e776aff9d806.jpg)



图 18-46. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/3827d486e701212c644688c4d60c073b36145587aafed93cdec320c46986f556.jpg)


## 通道输出准备信号

根据 18-43. x=0 1 2 3 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前会产生一个中间信号 OxCPRE 信号（通道 x 输出准备信号）。设置CHxCOMCTL 位可以定义 OxCPRE 信号类型。当 TIMERx 用于输出匹配比较模式下，设置CHxCOMCTL 位可以定义 OxCPRE 信号（通道 x 输出准备信号）类型。OxCPRE 信号有若干类型的输出功能，包括，设置CHxCOMCTL=0x00可以保持原始电平；设置CHxCOMCTL=0x01可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域为 0x06或0x07可以配置 PWM模式0/PWM 模式1。在这些模式中，根据计数器值和 TIMERx_CHxCV寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL=0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 正交译码器

正交译码器功能使用由TIMERx_CH0和TIMERx_CH1引脚生成的CI0FE0和CI1FE1正交信号各自相互作用产生计数值。在每个输入源改变期间，DIR位会发生改变。输入源可以是只有CI0FE0，可以只有CI1FE1，或着可以同时有CI0FE0和CI1FE1。

◼ 对于GD32L233，通过设置SMC=0x01, 0x02或0x03来选择使用哪种模式。

◼ 对于GD32L235，通过设置TSCFGy[3:0] != 4’b0000（y=0,1,2）来选择使用哪种模式。

计数器计数方向改变的机制如 18-6. 所示。正交译码器可以当作一个带有方向选择的外部时钟，这意味着计数器会在0和自动加载值之间连续的计数。因此，用户必须在计数器开始计数前配置TIMERx_CAR寄存器。


表18-6. 不同正交译码器模式下的计数方向


<table><tr><td rowspan="2">计数模式</td><td rowspan="2">电平</td><td colspan="2">CI0FE0</td><td colspan="2">CI1FE1</td></tr><tr><td>上升</td><td>下降</td><td>上升</td><td>下降</td></tr><tr><td rowspan="2">正交译码器模式0SMC[2:0]=3&#x27;b001</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>-</td><td>-</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>-</td><td>-</td></tr><tr><td rowspan="2">正交译码器模式1SMC [2:0]=3&#x27;b010</td><td>CI0FE0=1</td><td>-</td><td>-</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>-</td><td>-</td><td>向下</td><td>向上</td></tr><tr><td rowspan="4">正交译码器模式2SMC [2:0]=3&#x27;b011</td><td>CI1FE1=1</td><td>向下</td><td>向上</td><td>X</td><td>X</td></tr><tr><td>CI1FE1=0</td><td>向上</td><td>向下</td><td>X</td><td>X</td></tr><tr><td>CI0FE0=1</td><td>X</td><td>X</td><td>向上</td><td>向下</td></tr><tr><td>CI0FE0=0</td><td>X</td><td>X</td><td>向下</td><td>向上</td></tr></table>


注意: “-“ 意思是”无计数”; “X” 意思是不可能。”0” 意思是低电平, “1” 意思是高电平。



图 18-47. 在正交译码器模式 2 且 CI0FE0极性不反相时计数器行为


<table><tr><td>CI0FE0</td><td></td></tr><tr><td>CI1FE1</td><td></td></tr><tr><td>TIMERx_CAR</td><td>99</td></tr><tr><td>CNT_REG</td><td>20 21 22 23 24 25 24 23 22 21 20 19</td></tr></table>


图 18-48. 在正交译码器模式 2 且 CI0FE0极性反相时计数器行为


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/713f2f480d9fb7d1f122963196469f2d36989fa20f3c2cf64dd8b29154b9aa26.jpg)


## 霍尔传感器接口功能

通用定时器 L0 支持霍尔传感器接口功能，该功能可以用来控制 BLDC 电机。

三个霍尔传感器与 TIMER_in 定时器的三路输入捕获引脚一一对应连接，每个霍尔传感器输入一路波形到输入引脚，分析三路霍尔信号可以计算出转子的位置和速度。

置位 TI0S 可以使能异或功能，则每个输入信号电平发生变化时 CI0 都会翻转。CH0VAL 将会记录 CI0 翻转时的计数器数值。

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式。

◼ 对于GD32L233，可以通过设置TIMERx_SMCFG寄存器中的SMC [2:0]配置这些模式。这些模式的输入触发源可以通过设置TIMERx_SMCFG寄存器中的TRGS [2:0]来选择。

◼ 对于GD32L235，可以通 过设置SYSCFG_TIMER1CFG 或 SYSCFG_TIMER2CFG（y=3,4,5）寄存器中的TSCFGy[3:0] != 4b’0000（y=3,4,5）配置这些模式。


表 18-7. GD32L233 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>SMC[2:0]3&#x27;b100(复位模式)3&#x27;b101(暂停模式)3&#x27;b110(事件模式)</td><td>TRGS[2:0]000: ITI0001: ITI1010: ITI2011: ITI3100: CI0F_ED101: CI0FE0110: CI1FE1111: ETIFP</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相如果触发源是ETIF,配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Cix,配置CHxCAPFLT设置滤波,分频不可用触发源是ETIF,滤波和预分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TRGS[2:0]=3&#x27;b000选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图18-49. 复位模式下的控制电路</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TRGS[2:0]=3&#x27;b101选择CI0FE0为触发源</td><td>TIOS=0.(非异或)[CHONP==0, CHOP==0]不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-50. 暂停模式下的控制电路<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/8165fac502addae8709c04dc13c85e70967c58ead0a13168e6b3428ddc930e42.jpg"/></td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="2">极性选择</td><td>滤波和预分频</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TRGS[2:0]=3&#x27;b111选择ETIF为触发源.</td><td>ETP = 0 没有极性改变</td><td colspan="2">ETPSC = 1, 2分频.ETFC = 0,无滤波</td></tr><tr><td colspan="5">图18-51. 事件模式下的控制电路<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/50f7e4fa190f58f9195227bb32a70a02b274bc8a864f7929883c5fa3737fda18.jpg"/></td></tr></table>


表 18-8. GD32L235 从模式例子列表


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[3:0]y=3&#x27;b100(复位模式)y=3&#x27;b101(暂停模式)y=3&#x27;b110(事件模式)</td><td>TSCFGy[3:0]0001: ITI00010: ITI10011: ITI20100: ITI30101: CI0F_ED0110: CI0FE00111: CI1FE11000: ETIFP</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相如果触发源是ETIF,配置ETP选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Cix,配置CHxCAPFLT设置滤波,分频不可用触发源是ETIF,滤波和预分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[3:0]=4&#x27;b0001选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图18-52. 复位模式下的控制电路</td></tr></table>

<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td colspan="2">极性选择</td><td>滤波和预分频</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[3:0] = 4&#x27;b0110选择CI0FE0为触发源</td><td colspan="2">TIOS=0.(非异或)[CH0NP==0, CHOP==0]不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="5">图18-53.暂停模式下的控制电路</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[3:0] = 4&#x27;b1000选择ETIF为触发源.</td><td>ETP = 0 没有极性改变</td><td colspan="2">ETPSC = 1, 2分频.ETFC = 0,无滤波</td></tr><tr><td colspan="5">图18-54.事件模式下的控制电路</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置 TIMERx_CTL0 寄存器的 SPM 位置 1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置 CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和

TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。为了最大限度减少延迟，用户可以将 TIMERx_CHCTL0/1 寄存器的 CHxCOMFEN 位置 1。单脉冲模式下，触发上升沿产生之后， OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。只有输出通道配置为 PWM1 或 PWM2 输出运行模式下时 CHxCOMFEN 位才可用，触发源来源于触发信号。


18-55. TIMERx_CHxCV = 4 TIMERx_CAR=99 展示了一个例子



图 18-55. 单脉冲模式，TIMERx_CHxCV = 4 TIMERx_CAR=99


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/a559969b89b1b207a90a15e3d1107bebd87efae91a11be4a37913569599f0980.jpg)


## 定时器互连

定时器之间的相互连接可以实现定时器的级联或者同步。可以通过配置一个定时器工作在主模式，另一个定时器工作在从模式来实现。

## ◼ 定时器 2 作为定时器 1 的预分频器

1. 配置定时器2为主模式，选择其更新事件（UPE）为触发输出（配置TIMER2_CTL1寄存器的MMC=3’b010）。定时器2在每次计数器溢出产生更新事件时，输出一个周期信号；

2. 配置定时器2周期（TIMER2_CAR寄存器）；

3. 选择定时器1输入触发源为定时器2, 配置定时器1在外部时钟模式0；

对 于 GD32L233, 配 置 TIMER1_SMCFG 寄 存 器 的 TRGS=3’b000 同 时 配 置TIMER1_SMCFG寄存器的SMC=3’b111对于GD32L235,配置SYSCFG_TIMERxCFG寄存器的TSCFG6[3:0] = 4’b 0001

4. 写1到CEN位启动定时器1（TIMER1_CTL0寄存器）；

5. 写1到CEN位启动定时器2（TIMER2_CTL0寄存器）。

## 定时器 DMA模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。必须使能相应的 DMA 请求位，一些内部中断事件才可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA配置成 M2P（传输方向为从内存到外设）模式，PADDR（外设基地址）为 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC位域值为 0，表示 1 次传输，定时器发送 1 个 DMA请求就可以完成。如果 TIMERx_DMACFG寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次DMA请求。在这 3 次请求下，DMA对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的DMATA+0x4，DMATA+0x8，DMATA+0xC 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex<sup>®</sup>-M23 内核停止，DBG_CTL0 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。
