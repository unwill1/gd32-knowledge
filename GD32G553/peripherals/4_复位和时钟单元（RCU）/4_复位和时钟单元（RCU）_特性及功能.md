## 4. 复位和时钟单元（RCU）

## 4.1. 复位控制单元（RCTL）

## 4.1.1. 简介

GD32G553复位控制包括三种控制方式：电源复位、系统复位和备份域复位。电源复位又称为冷复位，其复位除了备份域的所有系统。系统复位将复位除了SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设IP。备份域复位将复位备份区域。复位能够被外部信号、内部事件和复位发生器触发。后续章节将介绍关于这些复位的详细信息。

## 4.1.2. 功能描述

## 电源复位

当发生以下任一事件时，产生电源复位：上电/掉电复位（POR/PDR复位），从待机模式中返回后由内部复位发生器产生。电源复位复位所有的寄存器除了备份域。电源复位为低电平有效，当内部LDO电源基准准备好提供V<sub>CORE</sub>电压时，电源复位电平将变为无效。复位入口向量被固定在存储器映射的地址0x0000_0004。

## 系统复位

当发生以下任一事件时，产生一个系统复位：

 上电复位（POWER_RSTn）

 外部引脚复位（NRST）

 窗口看门狗计数终止（WWDGT_RSTn）

 独立看门狗计数终止（FWDGT_RSTn）

■ Cortex<sup>®</sup>-M33的中断应用和复位控制寄存器中的SYSRESETREQ位置‘1’（SW_RSTn）

 选项字节重载复位（OBL_RSTn）

 用户选择字节寄存器nRST_STDBY设置为0，并且进入待机模式时将产生复位（OB_STDBY_RSTn）

■ 用户选择字节寄存器nRST_DPSLP设置为0，并且进入深度睡眠模式时（OB_DPSLP_RSTn）

注意：NRST引脚通过配置选项字节NRST_MDSEL[1:0]配置成以下三种模式下：

1. 输入/输出模式（默认模式）：在这种模式下，NRST pin的GPIO功能不可用。复位信号可以从NRST引脚传输到MCU，导致MCU复位，复位脉冲信号可以通过NRST引脚反应出来，最小复位脉冲持续时间为20us。

2. 输入模式：在这种模式下，NRST引脚的GPIO功能不可用，复位信号可以从NRST引脚传输到MCU，导致MCU复位，但在NRST引脚上不可见该MCU的内部复位。

3. GPIO模式：NRST引脚只能作为标准GPIO使用，复位功能不可用，复位信号仅在MCU内部，不反映在NRST引脚上。

系统复位将复位除了SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设IP。

系统复位脉冲发生器保证每一个复位源（外部或内部）都能有至少20μs的低电平脉冲延时。


图4-1. 系统复位电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/34c53ad862fa103c5bb31d81f3a4b9d1ebdf8e9c89731d73e6bc2cbd66f4a9b8.jpg)


## 备份域复位

以下事件之一发生时，产生备份域复位：1、设置备份域控制寄存器中的BKPRST位为‘1’；2、备份域电源上电复位（在VDD和VBAT两者都掉电的前提下，VDD或VBAT上电）。

## 4.2. 时钟控制单元（CCTL）

## 4.2.1. 简介

时钟控制单元提供了一系列频率的时钟功能，包括一个内部8M RC振荡器时钟（IRC8M）、一个外部高速晶体振荡器时钟（HXTAL）、一个内部32K RC振荡器时钟（IRC32K）、一个外部低速晶体振荡器时钟（LXTAL）、一个锁相环（PLL）、一个HXTAL时钟监视器、一个LXTAL时钟监视器、时钟预分频器、时钟多路复用器和时钟门控电路。

AHB、APB和Cortex<sup>®</sup>-M33时钟都源自系统时钟（CK_SYS），系统时钟的时钟源可以选择IRC8M、HXTAL或PLL。系统时钟的最大运行时钟频率可以达到216MHz。


图4-2. 时钟树


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/0f991755e87cadec4405a027be93c94ac608ac8cdf7da47967e5fe10528c8aaf.jpg)


预分频器可以配置 AHB、APB3、APB2 和 APB1 域的时钟频率。AHB、APB3、APB2、APB1 域的最高时钟频率分别为 216MHz / 216MHz / 216MHz / 216MHz。RCU 通过 AHB 时钟（HCLK）8 分频后作为 Cortex®系统定时器（SysTick）的外部时钟。通过对 SysTick 控制和状态寄存器的设置，可选择上述时钟或 AHB（HCLK）时钟作为 SysTick 时钟。

ADCx（x = 0，1，2，3）的时钟由CKPLLR或者CK_SYS或者HCKL经2、4、6、8、10、12、14、16分频获得，通过配置RCU_CFG2寄存器中的ADCxSEL（x=0，1，2）位和ADC_SYNCCTL寄存

器的ADCSCK位来选择。

CANx（x=0，1，2）的时钟由IRC8M或者HXTAL或者PLLQ或者APB2提供，通过配置RCU_CFG1寄存器中的CANxSEL（x=0，1，2）位来选择。

HPDF_AUDIO的时钟由CK_PLLQ或者CK_IRC8M或者外部HPDF_CKIN引脚提供。通过配置RCU_CFG1寄存器中HPDFAUDIOSEL位来选择。

TRNG的时钟由CK_PLLQ时钟的2到15分频提供。通过配置RCU_CFG2寄存器中TRNGPSC位来选择。

QSPI的时钟由IRC8M或者PLLQ或者PLLR或者系统时钟提供。通过配置RCU_CFG2寄存器的QSPISEL位来选择。

USART0的 时 钟 由IRC8M或 者LXTAL时 钟 或 者 系 统 时 钟 或 者APB2时 钟 提 供。 通 过 配 置RCU_CFG1寄存器的USART0SEL位来选择。USARTx（x = 1，2）的时钟由IRC8M或者HXTAL或者系统时钟或者APB1时钟提供。通过配置RCU_CFG1寄存器的USARTxSEL（x = 1，2）位来选择。

HPDF的时钟由AHB或者APB2时钟提供。通过配置RCU_CFG1寄存器的HPDFSEL位来选择。

HRTIMER 的 时 钟 由 CK_APB2或 者CK_SYS时 钟 提 供。通 过 配 置 RCU_CFG2 寄存器的HRTIMERSEL位来选择。

如果用户不需要使用HRTIMER高分辨率模式，可以保持RCU_CFG2寄存器中的HRTIMERSEL位清零，在这种情况下，HRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值必须大于或等于5（预分频比大于或等于32）。

如果用户需要使用HRTIMER高分辨率模式，必须在系统时钟源选择为PLL时，通过配置RCU_CFG2寄存器中的HRTIMERSEL位为1，选择CK_SYS为时钟源，此时HRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值可以配置为任何可选值。

注意：在高分辨率配置中，必须配置AHB和APB2预分频器（RCU_CFG0寄存器中的AHBPSC[3:0]和APB2PSC[2:0]位），将系统时钟CK_SYS与APB2时钟PCLK2之间的比率为1，2或4。

LPTIMER的时钟由CK_APB1或者CK_IRC32K或者CK_LXTAL或者IRC8M时钟提供。通过配置RCU_CFG2寄存器的LPTIMERSEL位来选择。

TIMER时钟由CK_APB1和CK_APB2时钟分频获得，如果APBx（x=0,1）的分频系数不为1，则TIMER时钟为CK_APBx（x = 0,1）的两倍。

通过配置RCU_BDCTL寄存器的RTCSRC位，RTC时钟可以选择由LXTAL时钟、IRC32K时钟或HXTAL时钟的32分频提供。RTC时钟选择HXTAL时钟的32分频做为时钟源后，当V<sub>CORE</sub>电源域掉电时，时钟将停止。RTC时钟选择IRC32K时钟做为时钟源后，当V<sub>DD</sub>掉电时，时钟将停止。RTC时钟选择LXTAL时钟做为时钟源后，当V<sub>DD</sub>和V<sub>BAT</sub>都掉电时，时钟将停止。

当FWDGT启动时，FWDGT时钟被强制选择由IRC32K时钟做为时钟源。

## 4.2.2. 主要特性

 4到48MHz外部高速晶体振荡器（HXTAL）；

 内部8MHz RC振荡器（IRC8M）；

 32768 Hz外部低速晶体振荡器（LXTAL）；

 内部32KHz RC振荡器（IRC32K）；

 PLL时钟源可选HXTAL、IRC8M；

 HXTAL时钟监视器;

 LXTAL时钟监视器。

## 4.2.3. 功能描述

外部高速晶体振荡时钟（HXTAL）

4到48M的外部高速晶体振荡器可为系统时钟提供更为精确时钟源。带有特定频率的晶体必须靠近两个HXTAL的引脚连接。和晶体连接的外部电阻和电容必须根据所选择的振荡器来调整。

## 图4-3. HXTAL时钟源

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/d5226dce532062971d312c831167e94f7c47d10e2ae7b11d04516776df01cbfe.jpg)


HXTAL晶体振荡器可以通过设置控制寄存器RCU_CTL的HXTALEN位来启动或关闭，在控制寄存器RCU_CTL中的HXTALSTB位用来指示外部高速振荡器是否已稳定。在启动时，直到这一位被硬件置‘1’，时钟才被释放出来。这个特定的延迟时间被称为振荡器的启动时间。当HXTAL时钟稳定后，如果在中断寄存器RCU_INT中的相应中断使能位HXTALSTBIE位被置‘1’，将会产生相应中断。此时，HXTAL时钟可以被直接用作系统时钟源或者PLL输入时钟。

将控制寄存器RCU_CTL的HXTALBPS和HXTALEN位置‘1’可以设置外部时钟旁路模式。旁路输入时，信号接至OSCIN，OSCOUT保持悬空状态，如 4-4. HXTAL 所示。此时，CK_HXTAL等于驱动OSCIN管脚的外部时钟。


图4-4. 旁路模式下HXTAL时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/1c7db6e3ad9019a230f25f4b38a8435181cb1c5aa0e0a150008128c412ac2994.jpg)


## 内部 8M RC 振荡器时钟（IRC8M）

内部8MHz RC振荡器时钟，简称IRC8M时钟，拥有8MHz的固定频率，设备上电后CPU默认选择其做为系统时钟源。IRC8M RC振荡器能够在不需要任何外部器件的条件下为用户提供更低成本类型的时钟源。IRC8M RC振荡器可以通过设置控制寄存器（RCU_CTL）中的IRC8MEN位被启动和关闭。控制寄存器RCU_CTL中的IRC8MSTB位用来指示IRC8M内部RC振荡器是否稳定。IRC8M振荡器的启动时间比HXTAL晶体振荡器要更短。如果中断寄存器RCU_INT中的相应中断使能位IRC8MSTBIE被置‘1’，在IRC8M稳定以后，将产生一个中断。IRC8M时钟也可用作系统时钟源或PLL输入时钟。

工厂会校准IRC8M时钟频率的精度，但是它的精度仍然比HXTAL时钟要差。用户可以根据需求、环境条件和成本决定选择哪个时钟作为系统时钟源。

如果HXTAL或者PLL被选择为系统时钟源，为了最大程度减小系统从深度睡眠模式恢复的时间，当系统从深度睡眠模式初始唤醒时，硬件会强制IRC8M时钟作为系统时钟。

## 锁相环（PLL）

内部有一个锁相环，PLL，可以提供16 ~ 216 MHz时钟的输出, 基本参考频率2 ~ 40 MHz的2 ~ 31倍。

PLL可以通过设置RCU_CTL寄存器中的PLLEN位被启动和关闭。RCU_CTL寄存器中的PLLSTB位用来指示PLL时钟是否稳定。如果RCU_INT寄存器中的相应中断使能位PLLSTBIE被置‘1’，在PLL稳定以后，将产生一个中断。

通过配置PLLPEN、PLLQEN、PLLREN来使能所需的PLL输出。PLLP时钟可用于产生系统时钟(不超过216MHz)，PLLQ时钟可以提供给TRNG / QSPI / CAN外设。PLLR时钟可以提供给到ADC外设。每个PLL输出时钟(PLLPEN,PLLPEN,PLLREN)的使能可以在不停止对应的PLL的情况下修改。如果CK_PLLP被用作系统时钟,那么PLLPEN不能失能。

当进入Deepsleep/Standby模式或者HXTAL监视器检测到时钟阻塞时（HXTAL做为锁相环的输入时钟），PLL将被关闭。

## 外部低速晶体振荡器时钟（LXTAL）

LXTAL是一个频率为32.768kHz的外部低速晶体或陶瓷谐振器。它为实时时钟电路提供一个低功耗且高精准的时钟源。LXTAL振荡器可以通过设置备份域控制寄存器（RCU_BDCTL）中的LXTALEN位被启动和关闭。备份域控制寄存器RCU_BDCTL中的LXTALSTB位用来指示LXTAL时钟是否稳定。如果中断寄存器RCU_INT中的相应中断使能位LXTALSTBIE被置‘1’，在LXTAL稳定以后，将产生一个中断。

将备份域控制寄存器RCU_BDCTL的LXTALBPS和LXTALEN位置‘1’可以选择外部时钟旁路模式。CK_LXTAL与连到OSC32IN脚上外部时钟信号一致。

## 内部 32K RC 振荡器时钟（IRC32K）

IRC32K内部RC振荡器时钟担当一个低功耗时钟源的角色，不需要外部器件，它的时钟频率大约32kHz，为独立看门狗和实时时钟电路提供时钟。IRC32K RC振荡器可以通过设置复位源/时钟寄存器RCU_RSTSCK中的IRC32KEN位被启动和关闭。复位源/时钟寄存器RCU_RSTSCK中的IRC32KSTB位用来指示IRC32K时钟是否已稳定。如果复位源/时钟寄存器RCU_RSTSCK中的相应中断使能位IRC32KSTBIE被置‘1’，在IRC32K稳定以后，将产生一个中断。

## 系统时钟（CK_SYS）选择

系统复位后，IRC8M时钟默认做为CK_SYS的时钟源，改变配置寄存器0（RCU_CFG0）中的系统时钟变换位SCS可以切换系统时钟源为HXTAL或CK_PLL。当SCS的值被改变，系统时钟将使用原来的时钟源继续运行直到转换的目标时钟源稳定。当一个时钟源被直接或通过PLL间接作为系统时钟时，它将不能被停止。

## HXTAL 时钟监视器（CKM）

设置控制寄存器RCU_CTL中的HXTAL时钟监视使能位CKMEN，HXTAL可以使能时钟监视功能。该功能必须在HXTAL启动延迟完毕后使能，在HXTAL停止后禁止。一旦监测到HXTAL故障，HXTAL将自动被禁止，中断寄存器RCU_INT中的HXTAL时钟阻塞中断标志位CKMIF将被置‘1’，产生HXTAL故障事件。这个故障引发的中断和Cortex®-M33的不可屏蔽中断NMI相连。如果HXTAL被选作系统，PLL或是RTC的时钟源，HXTAL故障将促使选择IRC8M为系统时钟源，PLL将被自动禁止，RTC的时钟源需要重新配置。

## LXTAL 时钟监视器（LCKM）

设置时钟控制寄存器 RCU_CTL 中的 LXTAL 时钟监视使能位 LCKMEN，LXTAL 可以使能时钟监视功能。该功能必须在 LXTAL 启动延迟完毕和 IRC32K 使能后使能。

当 LCKMEN 启用时，一个 4 位加一计数器将在 IRC32K 域工作。如果 LXTAL 时钟卡在 0/1 错误或时钟减慢约 20KHz，计数器将溢出。将发现 LXTAL 时钟故障。

## 时钟输出功能

时钟输出功能输出从32KHz到216MHz的时钟。通过设置时钟配置寄存器0（RCU_CFG0）中的CK_OUT时钟源选择位域CKOUTSEL能够选择不同的时钟信号。相应的GPIO引脚应该被配置成备用功能I/O（AFIO）模式来输出选择的时钟信号。


表4-1. 时钟输出的时钟源选择


<table><tr><td>时钟输出的时钟源选择位域</td><td>时钟源</td></tr><tr><td>000</td><td>NO CLK</td></tr><tr><td>010</td><td>CK_IRC32K</td></tr><tr><td>011</td><td>CK_LXTAL</td></tr><tr><td>100</td><td>CK_SYS</td></tr><tr><td>101</td><td>CK_IRC8M</td></tr><tr><td>110</td><td>CK_HXTAL</td></tr><tr><td>111</td><td>CK_PLLP</td></tr></table>


通过配置时钟配置寄存器 RCU_CFG0 的 CKOUTDIV[2:0]位，可以将输出时钟按比例分频，进而降低 CK_OUT 频率。


通过设置 RCU_BDCTL 寄存器的 LSCKOUSEL 位，CK_LXTAL 和 CK_IRC32K 时钟可以通过LSCK_OUT 引脚输出，即使在深度睡眠模式和待机模式。


表4-2. 低速时钟输出的时钟源选择


<table><tr><td>时钟输出的时钟源选择位域</td><td>时钟源</td></tr><tr><td>0</td><td>CK_IRC32K</td></tr><tr><td>1</td><td>LXTAL</td></tr></table>

## 深度睡眠模式时钟控制

当MCU处于深度睡眠模式时，USART0 / 1 / 2外设时钟由LXTA提供且LXTAL时钟使能时，则USART0 / 1 / 2外设可以唤醒MCU。

如果USART0 / 1 / 2时钟选择IRC8M处于深度睡眠模式时，则它们能够打开IRC8M时钟或关闭IRC8M时钟，从而使USART0 / 1 / 2从深度睡眠模式唤醒。

