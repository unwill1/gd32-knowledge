## 5. 复位和时钟单元（RCU）

高密度产品的复位和时钟控制单元（RCU）

## 5.1. 复位控制单元（RCTL）

## 5.1.1. 简介

GD32E51x 复位控制包括三种控制方式：电源复位、系统复位和备份域复位。电源复位又称为冷复位，其复位除了备份域的所有系统。系统复位将复位除了 SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设 IP。备份域复位将复位备份区域。复位能够被外部信号、内部事件和复位发生器触发。后续章节将介绍关于这些复位的详细信息。

## 5.1.2. 功能描述

## 电源复位

当发生以下任一事件时，产生电源复位：上电/掉电复位（POR/PDR 复位），从待机模式中返回后由内部复位发生器产生。电源复位复位所有的寄存器除了备份域。电源复位为低电平有效，当内部 LDO 电源基准准备好提供 1.1V 电压时，电源复位电平将变为无效。复位入口向量被固定在存储器映射的地址 0x0000_0004。

## 系统复位

当发生以下任一事件时，产生一个系统复位：

 上电复位（POWER_RSTn）；

 外部引脚复位（NRST）；

 窗口看门狗计数终止（WWDGT_RSTn）；

 独立看门狗计数终止（FWDGT_RSTn）；

 Cortex<sup>®</sup>-M33的中断应用和复位控制寄存器中的SYSRESETREQ位置‘1’（SW_RSTn）；

 用 户 选 择 字 节 寄 存 器nRST_STDBY设置为0， 并 且 进 入 待 机 模 式 时 将 产 生 复 位（OB_STDBY_RSTn）；

 用户选择字节寄存器nRST_DPSLP设置为0，并且进入深度睡眠模式时将产生复位（OB_DPSLP_RSTn）。

系统复位将复位除了 SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设 IP。

系统复位脉冲发生器保证每一个复位源（外部或内部）都能有至少 20μs 的低电平脉冲延时。


图 5-1. 系统复位电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/a00124063db7e810b78eba23edb85eb6f2b8215b9d43af1e33094b6d5e0774e0.jpg)


## 备份域复位

以下事件之一发生时，产生备份域复位：1、设置备份域控制寄存器中的 BKPRST 位为‘1’；2、备份域电源上电复位（在 $\mathsf { V } _ { \mathsf { D D } }$ 和 $\mathsf { V } _ { \mathsf { B A T } }$ 两者都掉电的前提下， $\mathsf { V } _ { \mathsf { D D } }$ 或 $\mathsf { V } _ { \mathsf { B A T } }$ 上电）。

## 5.2. 时钟控制单元（CCTL）

## 5.2.1. 简介

时钟控制单元提供了一系列频率的时钟功能，包括一个内部 8M RC 振荡器时钟（IRC8M）、一个内部 48M RC 振荡器时钟（IRC48M）、一个外部高速晶体振荡器时钟（HXTAL）、一个内部 40K RC 振荡器时钟（IRC40K）、一个外部低速晶体振荡器时钟（LXTAL）、一个锁相环（PLL）、一个 HXTAL 时钟监视器、时钟预分频器、时钟多路复用器和时钟门控电路。

AHB、APB 和 Cortex®-M33 时钟都源自系统时钟（CK_SYS），系统时钟的时钟源可以选择IRC8M、HXTAL 或 PLL。系统时钟的最大运行时钟频率可以达到 180MHz。


图 5-2. 时钟树


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/da80b7b0afe3ea4efb31a6fc2cb6aaf439b13907e6b7aac59c4236b5fb2edc53.jpg)



预分频器可以配置 AHB、APB2 和 APB1 域的时钟频率。AHB、APB2、APB1 域的最高时钟频率分别为 180MHz、180MHz、90MHz。RCU 通过 AHB 时钟（HCLK）8 分频后作为 Cortex<sup>®</sup>系统定时器（SysTick）的外部时钟。通过对 SysTick 控制和状态寄存器的设置，可选择上述时钟或 AHB（HCLK）时钟作为 SysTick 时钟。


ADC 时钟由 APB2 时钟经 2、4、6、8、12、16 分频或由 AHB 时钟经 5、6、10、20 分频获得，它们是通过设置 RCU_CFG0 和 RCU_CFG1 寄存器的 ADCPSC 位来选择。

USART5 时钟由 IRC8M 或 LXTAL 或 CK_SYS 或 APB2 时钟提供，通过配置 RCU_CFG2 寄存器的 USART5SEL 位来选择。

I2C2 的时钟由 IRC8M 或 CK_SYS 或 APB1 时钟提供，通过配置 RCU_CFG2 寄存器的I2C2SEL 位来选择。

SDIO, EXMC 的时钟由 CK_AHB 提供。

TIMER 时钟由 CK_APB1 和 CK_APB2 时钟分频获得，如果 APBx（x = 0，1）的分频系数不为 1，则 TIMER 时钟为 CK_APBx（x = 0，1）的两倍。

USBD 的时钟由 CK48M 时钟提供。通过配置 RCU_ADDCTL 寄存器的 CK48MSEL 及PLL48MSEL 位可以选择 CK_PLL 时钟或 IRC48M 时钟做为 CK48M 的时钟源。

CTC 时钟由 IRC48M 时钟提供，通过 CTC 单元，可以实现 IRC48M 时钟精度的自动调整。

I2S 的时钟由 CK_SYS 提供。

通过配置 RCU_BDCTL 寄存器的 RTCSRC 位，RTC 时钟可以选择由 LXTAL 时钟、IRC40K时钟或 HXTAL 时钟的 128 分频提供。RTC 时钟选择 HXTAL 时钟的 128 分频做为时钟源后，当 1.1V 内核电压域掉电时，时钟将停止。RTC 时钟选择 IRC40K 时钟做为时钟源后，当 V<sub>DD</sub>掉电时，时钟将停止。RTC 时钟选择 LXTAL 时钟做为时钟源后，当 V 和 V 都掉电时，时钟将停止。

当 FWDGT 启动时，FWDGT 时钟被强制选择由 IRC40K 时钟做为时钟源。

当 FMC 启动时，FMC 时钟被强制选择由 IRC8M 时钟作为时钟源。

SHRTIMER时钟由CK_APB2或CK_SYS提供。通过配置RCU_CFG1寄存器的SHRTIEMRSEL位来选择。

如 果 用 户 不 需 要 使 用SHRTIMER高 分 辨 率 模 式 ， 可 以 保 持RCU_CFG1寄 存 器 中 的SHRTIMERSEL位清零，在这种情况下，SHRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值必须大于或等于5（预分频比大于或等于64）。

如果用户需要使用SHRTIMER高分辨率模式，必须在系统时钟源选择为PLL时，通过配置RCU_CFG1 寄 存 器 中 的 SHRTIMERSEL 位 为 1 ， 选 择 CK_SYS 为 时 钟 源 ， 此 时SHRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值可以配置为任何可选值。

注意：在高分辨率配置中，必须配置 AHB 和 APB2 预分频器（RCU_CFG0 寄存器中的AHBPSC[3:0]和 APB2PSC[2:0]位），将系统时钟 CK_SYS 与 APB2 时钟 PCLK2 之间的比率为 1，2 或 4。

## 5.2.2. 主要特性

 4到32MHz外部高速晶体振荡器（HXTAL）；

 内部8MHz RC振荡器（IRC8M）；

 内部48MHz RC振荡器（IRC48M）；

 32,768 Hz外部低速晶体振荡器（LXTAL）；

 内部40KHz RC振荡器（IRC40K）；

 PLL时钟源可选HXTAL、IRC8M或IRC48M；

 HXTAL时钟监视器。

## 5.2.3. 功能描述

外部高速晶体振荡器时钟（HXTAL）

4 到 32M 的外部高速晶体振荡器可为系统时钟提供更为精确时钟源。带有特定频率的晶体必须靠近两个 HXTAL 的引脚连接。和晶体连接的外部电阻和电容必须根据所选择的振荡器来调整。


图 5-3. HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/60123b53f20f8d10e1a1c5d5ca2dea315b42fb0573e327e10c2b0fee9325902b.jpg)


HXTAL 晶体振荡器可以通过设置控制寄存器 RCU_CTL 的 HXTALEN 位来启动或关闭，在控制寄存器 中的 位用来指示外部高速振荡器是否已稳定。在启动时，直到这一位被硬件置‘1’，时钟才被释放出来。这个特定的延迟时间被称为振荡器的启动时间。当 HXTAL 时钟稳定后，如果在中断寄存器 RCU_INT 中的相应中断使能位 HXTALSTBIE 位被置‘1’，将会产生相应中断。此时，HXTAL 时钟可以被直接用作系统时钟源或者 PLL 输入时钟。

将控制寄存器RCU_CTL的HXTALBPS和HXTALEN位置‘1’可以设置外部时钟旁路模式。旁路输入时，信号接至 OSCIN，OSCOUT 保持悬空状态，如 5-4. HXTAL所示。此时，CK_HXTAL 等于驱动 OSCIN 管脚的外部时钟。


图 5-4. 旁路模式下 HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/ed215125d0dcd7fd757c3f8c1341ae01f7d910a5bcaff4e447f51d55d130657a.jpg)


## 内部 8M RC 振荡器时钟（IRC8M）

内部 8MHz RC 振荡器时钟，简称 IRC8M 时钟，拥有 8MHz的固定频率，设备上电后 CPU 默认选择其做为系统时钟源。IRC8M RC 振荡器能够在不需要任何外部器件的条件下为用户提供更低成本类型的时钟源。IRC8M RC 振荡器可以通过设置控制寄存器（RCU_CTL）中的IRC8MEN 位被启动和关闭。控制寄存器 RCU_CTL 中的 IRC8MSTB 位用来指示 IRC8M 内部RC 振荡器是否稳定。IRC8M 振荡器的启动时间比 HXTAL 晶体振荡器要更短。如果中断寄存器 RCU_INT 中的相应中断使能位 IRC8MSTBIE 被置‘1’，在 IRC8M 稳定以后，将产生一个中断。IRC8M 时钟也可用作系统时钟源或 PLL 输入时钟。

工厂会校准 IRC8M 时钟频率的精度，但是它的精度仍然比 HXTAL 时钟要差。用户可以根据需求、环境条件和成本决定选择哪个时钟作为系统时钟源。

如果 HXTAL 或者 PLL 被选择为系统时钟源，为了最大程度减小系统从深度睡眠模式恢复的时间，当系统从深度睡眠模式初始唤醒时，硬件会强制 IRC8M 时钟作为系统时钟。

## 内部 48M RC 振荡器时钟（IRC48M）

内部 48MHz RC 振荡器时钟，简称 IRC48M 时钟，拥有 48MHz 的固定频率，当使用 USBD模块时，IRC48M 振荡器在不需要任何外部器件的条件下为用户提供了一种成本更低的时钟源选择。IRC48M RC 振荡器可以通过设置 RCU_ADDCTL 寄存器中的 IRC48MEN 位被启动和关闭。RCU_ADDCTL 寄存器中的 IRC48MSTB 位用来指示内部 48MHz RC 振荡器是否稳定。如果 RCU_ADDINT 寄存器中的相应中断使能位 IRC48MSTBIE 被置‘1’，在 IRC48M 稳定以后，将产生一个中断。IRC48M时钟可做为 USBD 的系统时钟。

工厂会校准 IRC48M 时钟频率的精度，但是它的精度仍然不够精准。因为 USB 模块需要的时钟频率必须满足 48MHz（500ppm）。CTC 单元提供了一种硬件自动执行动态调整的功能将IRC48M 时钟调整到需要的频率。

## 锁相环（PLL）

内部有一个锁相环。

PLL 可以通过设置 RCU_CTL 寄存器中的 PLLEN 位被启动和关闭。RCU_CTL 寄存器中的PLLSTB位用来指示PLL时钟是否稳定。如果RCU_INT寄存器中的相应中断使能位PLLSTBIE被置‘1’，在 PLL 稳定以后，将产生一个中断。

当进入 Deepsleep/Standby 模式或者 HXTAL 监视器检测到时钟阻塞时（HXTAL 做为锁相环的输入时钟），PLL 将被关闭。

## 外部低速晶体振荡器时钟（LXTAL）

LXTAL 是一个频率为 32.768kHz 的外部低速晶体或陶瓷谐振器。它为实时时钟电路提供一个低功耗且高精准的时钟源。LXTAL 振荡器可以通过设置备份域控制寄存器（RCU_BDCTL）中的 LXTALEN 位被启动和关闭。备份域控制寄存器 RCU_BDCTL 中的 LXTALSTB 位用来指示LXTAL 时钟是否稳定。如果中断寄存器 RCU_INT 中的相应中断使能位 LXTALSTBIE 被置‘1’，在 LXTAL 稳定以后，将产生一个中断。

将备份域控制寄存器 RCU_BDCTL 的 LXTALBPS 和 LXTALEN 位置‘1’可以选择外部时钟旁路模式。CK_LXTAL 与连到 OSC32IN 脚上外部时钟信号一致。

## 内部 40K RC 振荡器时钟（IRC40K）

IRC40K 内部 RC 振荡器时钟担当一个低功耗时钟源的角色，不需要外部器件，它的时钟频率大约 40kHz，为独立看门狗和实时时钟电路提供时钟。IRC40K RC 振荡器可以通过设置复位源/时钟寄存器 RCU_RSTSCK 中的 IRC40KEN 位被启动和关闭。复位源/时钟寄存器

RCU_RSTSCK 中的 IRC40KSTB 位用来指示 IRC40K 时钟是否已稳定。如果复位源/时钟寄存器 RCU_RSTSCK 中的相应中断使能位 IRC40KSTBIE 被置‘1’，在 IRC40K 稳定以后，将产生一个中断。

TIMER4_CH3 可以捕获 IRC40K 的时钟，进而对 RTC 和 FWDGT 的计数器进行校准，详细的信息可以参考 AFIO_PCF0 寄存器的位 TIMER4CH3_IREMAP。

## 系统时钟（CK_SYS）选择

系统复位后，IRC8M 时钟默认做为 CK_SYS 的时钟源，改变配置寄存器 0（RCU_CFG0）中的系统时钟变换位 SCS可以切换系统时钟源为 HXTAL 或 CK_PLL。当 SCS 的值被改变，系统时钟将使用原来的时钟源继续运行直到转换的目标时钟源稳定。当一个时钟源被直接或通过PLL间接作为系统时钟时，它将不能被停止。

## HXTAL 时钟监视器（CKM）

设置控制寄存器 RCU_CTL 中的 HXTAL 时钟监视使能位 CKMEN，HXTAL 可以使能时钟监视功能。该功能必须在 HXTAL 启动延迟完毕后使能，在 HXTAL 停止后禁止。一旦监测到HXTAL 故障，HXTAL 将自动被禁止，中断寄存器 RCU_INT 中的 HXTAL 时钟阻塞中断标志位 CKMIF 将被置‘1’，产生 HXTAL 故障事件。这个故障引发的中断和 Cortex®-M33 的不可屏蔽中断 NMI 相连。如果 HXTAL 被选作系统，PLL 或是 RTC 的时钟源，HXTAL 故障将促使选择 IRC8M 为系统时钟源，PLL 将被自动禁止，RTC 的时钟源需要重新配置。

## 时钟输出功能

时钟输出功能输出从 4MHz 到 180MHz 的时钟。通过设置时钟配置寄存器 0（RCU_CFG0）中的 CK_OUT0 时钟源选择位域 CKOUT0SEL 能够选择不同的时钟信号。相应的 GPIO 引脚应该被配置成备用功能 I/O（AFIO）模式来输出选择的时钟信号。


表 5-1. 时钟输出 0 的时钟源选择


<table><tr><td>时钟输出 0 的时钟源选择位域</td><td>时钟源</td></tr><tr><td>0xx</td><td>NO CLK</td></tr><tr><td>100</td><td>CK_SYS</td></tr><tr><td>101</td><td>CK_IRC8M</td></tr><tr><td>110</td><td>CK_HXTAL</td></tr><tr><td>111</td><td>CK_PLL/2</td></tr></table>

## 电压控制

深度睡眠模式电压寄存器（RCU_DSV）中的 DSLPVS[2:0]位域可以控制 1.1V 域在深度睡眠模式下的电压。


表 5-2. 深度睡眠模式下 1.1V域电压选择


<table><tr><td>DSLPVS[2:0]</td><td>深度睡眠模式电压(V)</td></tr><tr><td>000</td><td>1.0</td></tr><tr><td>001</td><td>0.9</td></tr><tr><td>010</td><td>0.8</td></tr><tr><td>011</td><td>0.7</td></tr></table>

