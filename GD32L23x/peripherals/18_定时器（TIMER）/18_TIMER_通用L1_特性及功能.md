## 18.3. 通用定时器 L1（TIMERx, x=8,11）

## 18.3. 1. 简介

通用定时器 L1（Timer8, 11）是两通道定时器，支持输入捕获和输出比较，可以产生 PEM 信号控制电机和电源管理。通用定时器 L1 含有一个 16 位无符号计数器。

通用定时器 L1 是可编程的，可以被用来计数，其外部事件可以驱动其他定时器

定时器和定时器之间是相互独立，但是他们可以被同步在一起形成一个更大的定时器，这些定时器的计数器一致地增加。

## 18.3.2. 主要特征

◼ 总通道数：2；

◼ 计数器宽度：16位；

◼ 时钟源可选：内部时钟，内部触发，外部输入，外部触发；

◼ 计数模式：向上计数；

◼ 可编程的预分频器：16位，运行时可以被改变；

◼ 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

◼ 自动重装载功能；

◼ 中断输出：更新事件，触发事件，比较/捕获事件和中止事件；

◼ 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

◼ 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

◼ 定时器主-从管理。

## 18.3.3. 结构框图

18-56. GD32L233 L1 提供了通用定时器 L1 的内部配置细节。


图 18-56. GD32L233 通用定时器 L1 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/6feeb0eb47756d445830ee5a1995bdd9875fe4c934e4039fd576d0eea9435679.jpg)


18-57. GD32L235 L1 提供了通用定时器 L1 的内部配置细节。


图 18-57. GD32L235 通用定时器 L1 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/53590b1e2d8c2c4229ec374e543b07fc80354c90b62599a5e56e4bcd14adfba5.jpg)


## 18.3.4. 功能描述

## GD32L233 时钟源配置

通用定时器L1 可以由内部时钟源CK_TIMER 或者由 SMC（TIMERx_SMCFG 寄存器位[2:0]）控制的复用时钟源驱动。

◼ SMC[2:0]==3’b000，定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

如果 SMC[2:0]==3’b000，默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。如果将 TIMERx_SMCFG 寄存器的 SMC[2:0]设置为 0x1、0x2、0x3 和 0x7，预分频器被其他时钟源（由 TIMERx_SMCFG 寄存器的 TRGS [2:0]区域选择）驱动，在下文说明。当 SMC 位被设置为 0x4、0x5 和 0x6，计数器预分频器时钟源由内部时钟 CK_TIMER 驱动。


图 18-58. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/d1149bf42c699216bb84544b7ff9625001f82873a8fce0cbc34bb7014f8eedbb.jpg)


## ◼ SMC[2:0]==3’b111（外部时钟模式0），定时器选择外部输入引脚作为时钟源

计数器预分频器可以在 TIMERx_CI0/ TIMERx_CI1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 SMC [2:0]为 0x7 同时设置 TRGS [2:0]为 0x4，0x5 或 0x6 来选择。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置 SMC[2:0]为 0x7 同时设置 TRGS [2:0]为 0x0, 0x1, 0x2 或者 0x3。

SMC==1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 SMC [2:0]为 0x7 同时设置 TRGS [2:0]为 0x7。注意 ETI 信号是通过数字滤波器采样 ETI引脚得到的。。如果选择 ETIF 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## GD32L235 时钟源配置

通用定时器 L1 可以是内部时钟源 CK_TIMER，或者是由 TSCFGy[3:0]位确定的时钟源，TSCFGy[3:0]位于 SYSCFG_TIMER0CFG，（y=0,1…7）。

TSCFGy[3:0] =4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或SYSCFG_TIMER2CFG，（y=0,1…7），定时器选择内部时钟源（连接到RCU模块的CK_TIMER）。

当 TSCFGy[3:0] =4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或SYSCFG_TIMER2CFG，（y=0,1…7），默认用来驱动计数器预分频器的是内部时钟源CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

如 果 TSCFGy[3:0] !=4’b0000 ， TSCFGy[3:0] 位 于 SYSCFG_TIMER1CFG 或

SYSCFG_TIMER2CFG，（y=0,1,2,6），预分频器被其他时钟源（由TSCFG6[3:0]区域选择）驱动，更多细节在下文说明，当TSCFGy[3:0]（y=3,4,5）设置为有效值时，计数器预分频器时钟源由内部时钟TIMER_CK驱动。


图 18-59. 内部时钟分频为 1 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/9dad727a3374311cd0d9439a680e713c07d265ca6d61f18d523bdd4b371273dc.jpg)


◼ TSCFG6[3:0] !=4’b0000（外部时钟模式0），定时器选择外部输入引脚作为时钟源。

计数器预分频器可以在 TIMERx_CH0/ TIMERx_CH1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[3:0]为 0x5，0x6 或 0x7 来选择。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置TSCFG6[3:0]为 0x1，0x2，0x3 或者 0x4。

◼ SMC1=1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源。

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 TSCFG6[3:0]为 0x8。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 时钟预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-60. 当 PSC 数值从 0 变到 2 时，计数器的时序图


<table><tr><td>TIMER_CK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CEN</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PSC value</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>Prescaler shadow</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>Prescaler CNT</td><td>0</td><td></td><td></td><td></td><td></td><td>0</td><td>1</td><td>2</td><td>0</td><td>1</td><td>2</td></tr><tr><td>PSC_CLK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT_REG</td><td>94</td><td>95</td><td>96</td><td>97</td><td>98</td><td>99</td><td>0</td><td></td><td>1</td><td></td><td>2</td></tr><tr><td>UPG</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reload Pulse</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 计数器向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有影子寄存器（计数器自动重载寄存器，预分频寄存器）都将被更新。18-61. PSC=0/2 和 18-62.TIMFRx CAR 寄存器的值给出了一些例子，当 TIMERx CAR=0x99 时，计数器在不同预分频因子下的行为。


图 18-61. 向上计数时序图，PSC=0/2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/2baf031f7348bc354859bd3aba74e46fdb512c4514120f264c779a81d9a7e866.jpg)



图 18-62. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/c46a92f3ce624f79471529571583c39cd2afa68af582a42c4340830d1c37ee59.jpg)


## 输入捕获与输出比较通道

通用定时器 L1 拥有两个个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

◼ 通道输入捕获功能

通道输入捕获功能允许通道测量一个波形时序，频率，周期，占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 ChxIF 位被置 1，如果 ChxIE =1 则产生通道中断。


图 18-63. 通道输入捕获原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/d41ab7b0f3ac275fe982bed2ddf936fba8e7ec7e75c0d36b791e959a384ab875.jpg)


通道输入信号 Cix 先被 TIMER_CK 信号同步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP 选择使用上升沿或者下降沿。配置 CHxMS.，可以选择其他通道的输入信号，内部触发信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，CHxCV 存储计数器的值。

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT）：根据输入信号和请求信号的质量，配置相应的CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP/CHxNP）：配置CHxP/CHxNP选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS）：一旦通过配置CHxMS选 择 输 入 捕 获 源 ， 必 须 确 保 通 道 配 置 在 输 入 模 式（CHxMS!=0x0），而且TIMERx_CxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中ChxIE和CHxDEN）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中ChxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV被设置成当前计数器的值，ChxIF为置1。如果ChxIF位已经为1，则ChxOF位置1。根据TIMERx_DMAINTEN寄存器中ChxIE和

CHxDEN的配置，相应的中断和DMA请求会被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0并设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0 并设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV寄存器测量PWM的周期值，TIMERx_CH1CV寄存器测量PWM占空比值。

## ◼ 通道输出比较功能

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的 CxCV 寄存器与计数器的值匹配时，根据 CHxCOMCTL 的配置，这个通道的输出可以被置高电平，被置低电平或者反转。当计数器的值与 CxCV 寄存器的值匹配时，ChxIF 位被置 1，如果 ChxIE = 1 则会产生中断，如果 CxCDE=1 则会产生 DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

设置CHxCOMSEN位来配置输出比较影子寄存器；

设置CHxCOMCTL位来配置输出模式（置高电平/置低电平/反转）；

设置CHxP/CHxNP位来选择有效电平的极性；

设置ChxEN使能输出。

第三步：通过ChxIE/CxCDE位配置中断/DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

CxCV可以在运行时根据你所期望的波形而改变。

第五步：设置CEN位使能定时器。

18-64. 显示了三种比较输出模式：反转/置高电平/置低电平，CAR=0x63,

CxCV=0x3。 


图 18-64. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="96">Overflow</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="90">match toggle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="86">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="82">match set</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">match clear</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 输出 PWM功能

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 3’b110，PWM 模式 1 是配置CHxCOMCTL 为 3’b111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，我们可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐 PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。18-65. EAPWM 显示了 EAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 18-66. CAPWM 显示了 CAPWM 的输出波形和中断。

在 PWM0 模式下（CHxCOMCTL==3’b110），如果 TIMERx_CHxCV 寄存器的值大于TIMERx_CAR 寄存器的值，通道输出一直为有效电平。

在 PWM0 模式下（CHxCOMCTL==3’b110），如果 TIMERx_CHxCV 寄存器的值等于 0，通道输出一直为无效电平。


图 18-65. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/9ac5fe595ea96a0033c7df64ccc6e3e88800d96dbe0b5583ea6028bad6d44c8b.jpg)



图 18-66. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/32818935e98b875c40c9b9568be0376740067794ead8eeb04a6c9627d5e95ec1.jpg)


## 通道输出准备信号

当 TIMERx 用于输出匹配比较模式下，设置 CHxCOMCTL 位可以定义 OxCPRE 信号（通道 x准备信号）类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域位 0x06或0x07可以配置 PWM模式0/PWM 模式1。在这些模式中，根据计数器值和 TIMERx_CHxCV寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL =0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFE 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 主-从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式。

◼ 对于GD32L233，可以通过设置TIMERx_SMCFG寄存器中的SMC [2:0]配置这些模式。这些模式的输入触发源可以通过设置TIMERx_SMCFG寄存器中的TRGS [2:0]来选择。

◼ 对于GD32L235，可以通 过设置SYSCFG_TIMER1CFG 或 SYSCFG_TIMER2CFG（y=3,4,5）寄存器中的TSCFGy[3:0] != 4b’0000（y=3,4,5）配置这些模式。


表 18-9. GD32L233 从机模式列表和举例


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>SMC[2:0]3'b100(复位模式)3'b101(暂停模式)3'b110(事件模式)</td><td>TRGS[2:0]000: ITI0001: ITI1010: ITI2011: ITI3100: CI0F_ED101: CI0FE0110: CI1FE1111: 保留</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源Cix,配置CHxCAPFLT设置滤波,分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TRGS[2:0]=3'b000选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图18-67. 复位模式下的控制电路</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TRGS[2:0]=3'b101选择CI0FE0为触发源</td><td>TI0S=0.(非异或)CHOP==0,不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-68.暂停模式下的控制电路</td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TRGS[2:0]=3'b101选择CI0FE0为触发源</td><td>TI0S=0.(非异或)CHOP==0,不反相.</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-69.事件模式下的控制电路</td></tr></table>


表 18-10. GD32L235 从机模式列表和举例


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[3:0]y=3(复位模式)y=4(暂停模式)y=5(事件模式)</td><td>TRGS[2:0]0001: ITI00010: ITI10011: ITI20100: ITI30101: CI0F_ED0110: CI0FE00111: CI1FE11000: 保留</td><td>如果触发源是CI0FE0 或者CI1FE1,配置CHxP和 CHxNP来选择极性和反相</td><td>触发源ITIx,滤波和预分频不可用触发源 Cix,配置CHxCAPFLT 设置滤波,分频不可用</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿,计数器清零重启</td><td>TSCFG3[3:0] = 4'b0001选择ITIO为触发源</td><td>触发源是ITIO,极性选择不可用</td><td>触发源是ITIO,滤波和预分频不可用</td></tr><tr><td colspan="4">图18-70.复位模式下的控制电路</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数</td><td>TSCFG4[3:0] = 4'b0110选择CI0FE0为触发源</td><td>TIOS=0.(非异或)CHOP==0,不反相.在上升沿捕获</td><td>在这个例子中滤波被旁路</td></tr><tr><td colspan="4">图18-71.暂停模式下的控制电路</td></tr><tr><td>例3</td><td>事件模式触发输入的上升沿计数器开始计数</td><td>TSCFG5[3:0] = 4'b0110选择CI0FE0为触发源</td><td>TIOS=0.(非异或)CHOP==0,不反相.</td><td>在这个例子中滤波被旁路</td></tr><tr><td></td><td colspan="4">图18-72.事件模式下的控制电路</td></tr></table>

## 单脉冲模式

单脉冲模式与重复模式是相反的，设置 TIMERx_CTL0 寄存器的 SPM 位置 1，则使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置 CHxCOMCTL 配置 TIMERx 为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位来使能计数器。触发信号沿或者软件写 都可以产生一个脉冲，此后 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作，计数值被保持。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。为了最大限度减少延迟，用户可以将 TIMERx_CHCTL0/1 寄存器的 CHxCOMFEN 位置 1。单脉冲模式下，触发上升沿产生之后， OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。只有输出通道配置为 PWM0 或 PWM1 输出运行模式下时 CHxCOMFEN 位才可用，触发源来源于触发信号。

18-73. TIMERx_CHxCV = 4 TIMERx_CAR=99 展示了一个例子。


图 18-73. 单脉冲模式，TIMERx_CHxCV = 4 TIMERx_CAR=99


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/5a6ee32f4c883130350dd6d9b6ded9ff61bf97f911eb7321f2206f49985a2dda.jpg)


## 定时器互连

参考 L0 TIMERx x=1 2

## 定时器调试模式

当Cortex<sup>®</sup>-M23内核停止，DBG_CTL2寄存器中的TIMERx_HOLD配置位被置1，定时器计数器停止
