## 9. 复位和时钟单元（RCU）

## 9.1. 复位控制单元（RCTL）

## 9.1.1. 简介

GD32F50x 复位控制包括三种控制方式：电源复位、系统复位和备份域复位。电源复位又称为冷复位，其复位除了备份域的所有系统。系统复位将复位除了 SW-DP 控制器和备份域之外的其余部分，包括处理器内核和外设 IP。备份域复位将复位备份区域。复位能够被外部信号、内部事件和复位发生器触发。后续章节将介绍关于这些复位的详细信息。

## 9.1.2. 功能说明

## 电源复位

当发生以下任一事件时，产生电源复位：上电/掉电复位（POR/PDR 复位），从待机模式中返回后由内部复位发生器产生。电源复位复位所有的寄存器除了备份域。电源复位为低电平有效，当内部LDO 电源基准准备好提供 V<sub>CORE</sub>域电压时，电源复位电平将变为无效。复位入口向量被固定在存储器映射的地址 0x0000_0004。

## 系统复位

当发生以下任一事件时，产生一个系统复位：

 上电复位（POWER_RSTn）；

 外部引脚复位（NRST）；

 窗口看门狗计数终止（WWDGT_RSTn）；

 独立看门狗计数终止（FWDGT_RSTn）；

■ Cortex<sup>®</sup>-M33的中断应用和复位控制寄存器中的SYSRESETREQ位置‘1’（SW_RSTn）；

 用户选择字节寄存器nRST_STDBY设 置为0， 并 且 进 入 待 机 模 式 时 将 产 生 复 位（OB_STDBY_RSTn）；

 用户选择字节寄存器nRST_DPSLP设置为0，并且进入深度睡眠模式时将产生复位（OB_DPSLP_RSTn）。

系统复位将复位除了 SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设 IP。

系统复位脉冲发生器保证每一个复位源（外部或内部）都能有至少 20μs 的低电平脉冲延时。


图 9-1. 系统复位电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/980f52f485d2341e9b82df2c63f7a3248c9704afb8b7a8795bba6b96fde8200a.jpg)


## 备份域复位

以下事件之一发生时，产生备份域复位：1、设置备份域控制寄存器中的 BKPRST 位为‘1’；2、备份域电源上电复位（在 V<sub>DD</sub>和 V<sub>BAT</sub>两者都掉电的前提下，V<sub>DD</sub>或 V<sub>BAT</sub>上电）。

## 9.2. 时钟控制单元（CCTL）

## 9.2.1. 简介

时钟控制单元提供了一系列频率的时钟功能，包括一个内部 8M RC 振荡器时钟（IRC8M）、一个内部 48M RC 振荡器时钟（IRC48M）、一个外部高速晶体振荡器时钟（HXTAL）、一个内部 40KRC 振荡器时钟（IRC40K）、一个外部低速晶体振荡器时钟（LXTAL）、两个锁相环（PLL）、一个HXTAL 时钟监视器、一个 LXTAL 时钟监视器、时钟频率监视器、时钟预分频器、时钟多路复用器和时钟门控电路。

AHB、APB和Cortex<sup>®</sup>-M33时钟都源自系统时钟（CK_SYS），系统时钟的时钟源可以选择IRC8M、HXTAL 或 PLL。系统时钟的最大运行时钟频率可以达到 200MHz（适用于 GD32F502xx）、252MHz（适用于 GD32F503xx）或 280MHz（适用于 GD32F505xx）。

注意：在低频和高频之间进行切换时（如 8MHz与 280MHz之间切换），需要加切频补丁。具体实现可参考固件库 system_gd32f50x.c 中相关代码，时钟切换配置说明可参考《AN250 GD32 时钟切换配置使用指南》。


图 9-2. 时钟树（适用于 GD32F502xx）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/85275514fae7c7a7f0931b474b680eb64a2d8f6c28b13ac024b015ec3cb4d1bf.jpg)



图 9-3. 时钟树（适用于 GD32F503xx）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/f187085bf08e8b3e9efe424381f223dc4ee234ef9e1827fff59afdb89598f5a5.jpg)



图 9-4. 时钟树（适用于 GD32F505xx）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/8609cabca7ced73e15317ebcff5cd245d42b322743c52ec44f720ca9eadc15b6.jpg)


预分频器可以配置 AHB、APB2 和 APB1 域的时钟频率。AHB、APB2、APB1 域的最高时钟频率分别为 200MHz、200MHz、100MHz（适用于 GD32F502xx），252MHz、252MHz、126MHz（适用于 GD32F503xx）或 280MHz、280MHz、140MHz（适用于 GD32F505xx）。RCU 通过 AHB 时钟（HCLK）8 分频后作为 Cortex 系统定时器（SysTick）的外部时钟。通过对 SysTick 控制和状态寄存器的设置，可选择上述时钟或 AHB（HCLK）时钟作为 SysTick 时钟。

ADC 时钟由 APB2 时钟经 2、4、6、8、12、16 分频或由 AHB 时钟经 3、5、6、10、20 分频获得，它们是通过设置 RCU_CFG0 和 RCU_CFG1 寄存器的 ADCPSC 位来选择。

TIMER 时钟由 CK_APB1 和 CK_APB2 时钟分频获得，如果 APBx 的分频系数为 1，则 TIMER 时钟为 CK_APBx；如果 APBx 的分频系数不为 1，则 TIMER 时钟为 CK_APBx 的两倍。

USBFS 的时钟由 CK48M 时钟提供。通过配置 RCU_ADDCTL 寄存器的 CK48MSEL 及PLL48MSEL 位可以选择 CK_PLL0 时钟或 IRC48M 时钟做为 CK48M 的时钟源。

CTC 时钟由 IRC48M 时钟提供，通过 CTC 单元，可以实现 IRC48M 时钟精度的自动调整。

I2S 的时钟由 CK_SYS 或 CK_PLL1 提供，通过配置 RCU_CFG1 寄存器的 I2SxSEL（x = 1，2）

来选择。

FMC 接口时钟可通过 RCU_ADDCTL 寄存器中的 FMCSEL 位域选择为 CK_AHB、CK_SYS、CK_PLL0 和 CK_PLL1 中的一个，并通过 FMCDIV 分频后提供。

通过配置 RCU_BDCTL 寄存器的 RTCSRC 位，RTC 时钟可以选择由 LXTAL 时钟、IRC40K 时钟或 HXTAL 时钟的 128 分频提供。RTC 时钟选择 HXTAL 时钟的 128 分频做为时钟源后，当内核电压域掉电时，时钟将停止。RTC 时钟选择 IRC40K 时钟做为时钟源后，当 V<sub>DD</sub>掉电时，时钟将停止。RTC 时钟选择 LXTAL 时钟做为时钟源后，当 V<sub>DD</sub>和 V<sub>BAT</sub>都掉电时，时钟将停止。

当 FWDGT 启动时，FWDGT 时钟被强制选择由 IRC40K 时钟做为时钟源。

## 9.2.2. 主要特征

 4到40MHz外部高速晶体振荡器（HXTAL）；

 内部8MHz RC振荡器（IRC8M）；

 内部48MHz RC振荡器（IRC48M）；

 32,768 Hz外部低速晶体振荡器（LXTAL）；

 内部40KHz RC振荡器（IRC40K）；

 PLL0时钟源可选HXTAL、IRC8M或IRC48M；

 HXTAL时钟监视器；

 LXTAL时钟监视器；

 时钟频率监视器。

## 9.2.3. 功能说明

## 外部高速晶体振荡时钟（HXTAL）

4 到 40M 的外部高速晶体振荡器可为系统时钟提供更为精确时钟源。带有特定频率的晶体必须靠近两个 HXTAL 的引脚连接。和晶体连接的外部电阻和电容必须根据所选择的振荡器来调整。


图 9-5. HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/aaca619922fbf52f9b44ca9dc4cf6dee5a989219659fc60c7ae1b4c9b5b34a5f.jpg)


HXTAL 晶体振荡器可以通过设置控制寄存器 RCU_CTL 的 HXTALEN 位来启动或关闭，在控制寄存器 ${ \mathsf { R C U \_ C T L } }$ 中的 HXTALSTB位用来指示外部高速振荡器是否已稳定。在启动时，直到这一位被硬件置‘1’，时钟才被释放出来。这个特定的延迟时间被称为振荡器的启动时间。当 HXTAL 时钟稳定后，如果在中断寄存器 RCU_INT 中的相应中断使能位 HXTALSTBIE 位被置‘1’，将会产生相应中断。此时，HXTAL 时钟可以被直接用作系统时钟源或者 PLL 输入时钟。

将控制寄存器 RCU_CTL 的 HXTALBPS和 HXTALEN 位置‘1’可以设置外部时钟旁路模式。旁路输入时，信号接至 OSCIN，OSCOUT 保持悬空状态，如 9-6. HXTAL 所示。此时，CK_HXTAL 等于驱动 OSCIN 管脚的外部时钟。


图 9-6. 旁路模式下 HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/6e16c321f6a964013b3bd7a6f9491e48e4ae320ef4e8724c665a5f969af545b1.jpg)


## 内部 8M RC 振荡器时钟（IRC8M）

内部 8MHz RC 振荡器时钟，简称 IRC8M 时钟，拥有 8MHz 的固定频率，设备上电后 CPU 默认选择其做为系统时钟源。IRC8M RC 振荡器能够在不需要任何外部器件的条件下为用户提供更低成本类型的时钟源。IRC8M RC 振荡器可以通过设置控制寄存器（RCU_CTL）中的 IRC8MEN 位被启动和关闭。控制寄存器 RCU_CTL 中的 IRC8MSTB 位用来指示 IRC8M 内部 RC 振荡器是否稳定。IRC8M 振荡器的启动时间比 HXTAL 晶体振荡器要更短。如果中断寄存器 RCU_INT 中的相应中断使能位 IRC8MSTBIE 被置‘1’，在 IRC8M 稳定以后，将产生一个中断。IRC8M 时钟也可用作系统时钟源或 PLL0 输入时钟。

工厂会校准 IRC8M 时钟频率的精度，但是它的精度仍然比 HXTAL 时钟要差。用户可以根据需求、环境条件和成本决定选择哪个时钟作为系统时钟源。

如果HXTAL或者PLL0 被选择为系统时钟源，为了最大程度减小系统从深度睡眠模式恢复的时间，当系统从深度睡眠模式初始唤醒时，硬件会强制 IRC8M 时钟作为系统时钟。

## 内部 48M RC 振荡器时钟（IRC48M）

内部 48MHz RC 振荡器时钟，简称 IRC48M 时钟，拥有 48MHz 的固定频率，当使用 USBFS 模块时，IRC48M 振荡器在不需要任何外部器件的条件下为用户提供了一种成本更低的时钟源选择。IRC48M RC 振荡器可以通过设置 RCU_ADDCTL 寄存器中的 IRC48MEN 位被启动和关闭。RCU_ADDCTL 寄存器中的 IRC48MSTB 位用来指示内部 48MHz RC 振荡器是否稳定。如果RCU_ADDINT 寄存器中的相应中断使能位 IRC48MSTBIE 被置‘1’，在 IRC48M 稳定以后，将产生一个中断。IRC48M 时钟可做为 USBFS 的系统时钟。

工厂会校准 IRC48M 时钟频率的精度，但是它的精度仍然不够精准。因为 USB 模块需要的时钟频率必须满足 48MHz（500ppm）。CTC 单元提供了一种硬件自动执行动态调整的功能将 IRC48M 时

钟调整到需要的频率。

## 锁相环（PLL）

时钟部分有两个锁相环，PLL0，PLL1。

PLL0 可以通过设置 RCU_CTL 寄存器中的 PLL0EN 位被启动和关闭。RCU_CTL 寄存器中的PLL0STB位用来指示PLL0时钟是否稳定。如果RCU_INT寄存器中的相应中断使能位PLL0STBIE被置‘1’，在 PLL0 稳定以后，将产生一个中断。

PLL1 可以通过设置 RCU_CTL 寄存器中的 PLL1EN 位被启动和关闭。RCU_CTL 寄存器中的PLL1STB位用来指示PLL1时钟是否稳定。如果RCU_INT寄存器中的相应中断使能位PLL1STBIE被置‘1’，在 PLL1 稳定以后，将产生一个中断。

当进入 Deepsleep/Standby 模式或者 HXTAL 监视器检测到时钟阻塞时（HXTAL 作为锁相环的输入时钟），两个 PLL 将被关闭。

## 外部低速晶体振荡器时钟（LXTAL）

LXTAL 是一个频率为 32.768kHz的外部低速晶体或陶瓷谐振器。它为实时时钟电路提供一个低功耗且高精准的时钟源。LXTAL 振荡器可以通过设置备份域控制寄存器（RCU_BDCTL）中的LXTALEN 位被启动和关闭。备份域控制寄存器 RCU_BDCTL 中的 LXTALSTB 位用来指示 LXTAL时钟是否稳定。如果中断寄存器 RCU_INT 中的相应中断使能位 LXTALSTBIE 被置‘1’，在 LXTAL稳定以后，将产生一个中断。

将备份域控制寄存器 RCU_BDCTL 的 LXTALBPS 和 LXTALEN 位置‘1’可以选择外部时钟旁路模式。CK_LXTAL 与连到 OSC32IN 脚上外部时钟信号一致。

## 内部 40K RC 振荡器时钟（IRC40K）

IRC40K 内部 RC 振荡器时钟担当一个低功耗时钟源的角色，不需要外部器件，它的时钟频率大约40kHz，为独立看门狗和实时时钟电路提供时钟。IRC40K RC 振荡器可以通过设置复位源/时钟寄存器 RCU_RSTSCK 中的 IRC40KEN 位被启动和关闭。复位源/时钟寄存器 RCU_RSTSCK 中的IRC40KSTB 位用来指示 IRC40K 时钟是否已稳定。如果复位源/时钟寄存器 RCU_RSTSCK 中的相应中断使能位 IRC40KSTBIE 被置‘1’，在 IRC40K 稳定以后，将产生一个中断。

工厂会校准 IRC40K 时钟频率的精度。

## 系统时钟（CK_SYS）选择

系统复位后，IRC8M 时钟默认做为 CK_SYS 的时钟源，改变配置寄存器 0（RCU_CFG0）中的系统时钟变换位 SCS 可以切换系统时钟源为 HXTAL 或 CK_PLL0P。当 SCS 的值被改变，系统时钟将使用原来的时钟源继续运行直到转换的目标时钟源稳定。当一个时钟源被直接或通过 PLL0 间接作为系统时钟时，它将不能被停止。

## HXTAL 时钟监视器（HCKM）

设置控制寄存器 RCU_CTL 中的 HXTAL 时钟监视使能位 HCKMEN，HXTAL 可以使能时钟监视功能。该功能必须在 HXTAL 启动延迟完毕后使能，在 HXTAL 停止后禁止。一旦监测到 HXTAL 故障，HXTAL 将自动被禁止，中断寄存器 RCU_INT 中的 HXTAL 时钟阻塞中断标志位 HCKMIF 将被置‘1’，产生 HXTAL 故障事件。这个故障引发的中断和 Cortex®-M33 的不可屏蔽中断 NMI 相连。如果 HXTAL 被选作系统，PLL 或是 RTC 的时钟源，HXTAL 故障将促使选择 IRC8M 为系统时钟源，PLL 将被自动禁止，RTC 的时钟源需要重新配置。

## LXTAL 时钟监视器（LCKM）

设置时钟控制寄存器 RCU_BDCTL 中的 LXTAL 时钟监视使能位 LCKMEN，LXTAL 可以使能时钟监视功能。该功能必须在 LXTAL 启动延迟完毕后使能。

LXTAL 上的时钟监视器在除 V<sub>BAT</sub>以外的所有模式下工作。如果在外部 32 kHz 振荡器上检测到故障，可以向 CPU 发送中断。

然后，软件必须禁用 LCKMEN 位，停止有缺陷的 32 kHz振荡器，并更改 RTC 时钟源，或采取任何必要的措施来保护应用程序。

当 LCKMEN 启用时，一个 4 位加一个计数器将在 IRC40K 域工作。如果 LXTAL 时钟卡在 0/1 错误或减慢约 20KHz，计数器将溢出。将发现 LXTAL 时钟故障。一旦监测到 LXTAL 故障，中断寄存器 RCU_INT 中的 LXTAL 时钟阻塞中断标志位 LCKMIF 将被置‘1’，产生 LXTAL 故障事件。

## 时钟频率监视器（CKFM）

该时钟频率监测器可以使用 IRC48M 对 IRC8M、HXTAL、PLL0P 和 PLL1 的时钟频率范围进行监控。IRC8M 和 HXTAL 采用 1000 个 IRC48M 时钟周期作为监控窗口。对于 PLL0P 和 PLL1，采用 100 IRC48M 时钟周期作为监控窗口。用户可以通过配置 RCU_CKFMCFGx（x = 0，1，2，3）寄存器来配置时钟频率的监控范围。如果使能了相应的中断，并设置了时钟频率失效标志，则将发生中断。

当 IRC48M 时钟被禁用或丢失时，时钟频率监控将失效。

## 时钟输出功能

通过设置时钟配置寄存器 0（RCU_CFG0）中的 CK_OUT 时钟源选择位域 CKOUTSEL 能够选择不同的时钟信号。相应的 GPIO 引脚应该被配置成备用功能 I/O（AFIO）模式来输出选择的时钟信号。


表 9-1. 时钟输出的时钟源选择


<table><tr><td>时钟输出的时钟源选择位域</td><td>时钟源</td></tr><tr><td>000</td><td>CK_SYS</td></tr><tr><td>001</td><td>CK_IRC8M</td></tr><tr><td>010</td><td>CK_HXTAL</td></tr><tr><td>011</td><td>CK_PLL0/2</td></tr><tr><td>100</td><td>CK_PLL1/2</td></tr><tr><td>101</td><td>CK_LXTAL</td></tr><tr><td>110</td><td>CK_IRC48M</td></tr><tr><td>111</td><td>CK_IRC40K</td></tr></table>

## 电压控制

深度睡眠模式电压寄存器（RCU_DSV）中的 DSLPVS[2:0]位域可以控制 V<sub>CORE</sub>域在深度睡眠模式下的电压。


表 9-2. 深度睡眠模式下 $\forall c o _ { R E }$ 域电压选择


<table><tr><td>DSLPVS[2:0]</td><td>深度睡眠模式电压(V)</td></tr><tr><td>000</td><td>默认值</td></tr><tr><td>001</td><td>默认值-0.05</td></tr><tr><td>010</td><td>默认值-0.1</td></tr><tr><td>011</td><td>默认值-0.15</td></tr><tr><td>100</td><td>默认值-0.2</td></tr><tr><td>101</td><td>默认值-0.25</td></tr><tr><td>110</td><td>默认值-0.3</td></tr><tr><td>111</td><td>默认值-0.35</td></tr></table>
