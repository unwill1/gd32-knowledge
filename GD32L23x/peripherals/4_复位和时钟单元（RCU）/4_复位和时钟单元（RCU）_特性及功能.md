## 4. 复位和时钟单元（RCU）

## 4.1. 复位控制单元（RCTL）

## 4.1.1. 简介

GD32L23x复位控制包括三种复位控制：电源复位、系统复位和备份域复位。电源复位又称为冷复位，电源启动时复位除了备份域的所有系统。除了SW-DP控制器和备份域，系统复位将复位处理器内核和外设IP部分。备份域复位复位备份区域。复位被外部信号、内部事件和复位发生器触发。接下来的章节将详细介绍这些复位。

## 4.1.2. 功能说明

## 电源复位

当以下事件中之一发生时，产生电源复位：1、上电/掉电复位（POR/PDR复位）；2、从待机模式中返回后由内部复位发生器产生。电源复位复位所有的寄存器除了备份域。电源复位为低电平有效，当内部LDO电源基准准备好提供1.1V电压给GD32L23x产品时，电源复位电平将变为无效。复位入口向量被固定在存储器映射地址0x0000_0004。

## 系统复位

当发生以下任一事件时，产生一个系统复位：

◼ 电源复位（POWER_RSTn）；

◼ 外部引脚复位（NRST）；

◼ 窗口看门狗定时器计数终止（WWDGT_RSTn）；

◼ 独立看门狗定时器计数终止（FWDGT_RSTn）；

■ Cortex<sup>®</sup>-M23的中断应用和复位控制寄存器中的SYSRESETREQ位置‘1（SW_RSTn）；

◼ 用户选择字节寄存器nRST_STDBY设置为0，并且进入待机模式时（OB_STDBY_RSTn）；

◼ 用 户 选 择 字 节 寄 存 器 nRST_DPSLP 设 置 为 0 ， 并 且 进 入 深 度 睡 眠 模 式 时（OB_DPSLP_RSTn）。

除了SW-DP控制器和备份域，系统复位将复位处理器内核和外设IP部分。

系统复位脉冲发生器保证每一个复位源（外部或内部）都能有至少20μs的低电平脉冲延时。


图 4-1. 系统复位电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/affed01a563db89697a80d0a34999f1b34f4c3f2b8456cbe161e074e512212c7.jpg)


## 备份域复位

当以下事件之一发生时，产生备份域复位。1、设置备份域控制寄存器中的BKPRST位为‘1’；2、备份域电源上电复位（V<sub>DD</sub>重新上电）。

## 4.2. 时钟控制单元（CCTL）

## 4.2.1. 简介

时钟控制单元提供了一系列频率和时钟功能，包括一个内部16M RC振荡器时钟（IRC16M）、一个内部48M RC振荡器时钟（IRC48M）、一个外部高速晶体振荡器时钟（HXTAL）、一个内部低速RC振荡器时钟（IRC32K）、一个外部低速晶体振荡器时钟（LXTAL）、一个锁相环（PLL）、一个HXTAL时钟监视器、一个LXTAL时钟监视器，时钟预分频器、时钟多路复用器和时钟选通电路。

AHB、APB和Cortex<sup>®</sup>-M23时钟都源自系统时钟（CK_SYS），系统时钟的时钟源为IRC16M、IRC48M、HXTAL、IRC32K（仅适用于GD32L235xx系列）或PLL。系统时钟的最大运行时钟频率可以达到64MHz。


图4-2. GD32L233xx产品时钟树


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/726003c6afc546fac5d672a5c0d99042741396a36a1f1900813293bc936c8445.jpg)



图4-3. GD32L235xx产品时钟树


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/605dc78c440e3e1991ed38cc907bded67de9dacfe7da4b8d66b64c55cd260997.jpg)


预分频器可以配置AHB、APB2和APB1域的时钟频率。AHB、APB2和APB1域的最高时钟频率分别为64MHz、64MHz和32MHz。RCU通过AHB时钟（HCLK）8分频后作为Cortex系统定时器（SysTick）的外部时钟。通过对SysTick控制与状态寄存器的设置，可选择上述时钟或APB（HCLK）时钟作为SysTick时钟。

在GD32L23x产品中ADC时钟由APB2时钟经2、4、6、8、10、12、14、16分频或由AHB时钟经3、5、7、9、11、13、15、17分频或IRC16M获得，它们是通过设置配置寄存器2（RCU_CFG2）的ADCSEL位来选择ADC时钟源的。

USART0的时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB2时钟，通过设置配置寄存器2（RCU_CFG2）的USART0SEL位域来选择。

USART1的时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的USART1SEL位域来选择。

在GD32L233xx产品中，LPUART的时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的LPUARTSEL位域来选择。在GD32L235xx产品中，LPUARTx（x = 0, 1）时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的LPUARTxSEL（x = 0, 1）位域来选择。

I2Cx（x=0,1,2）的时钟可以选择IRC16MDIV时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的I2CxSEL（x = 0, 1, 2）位域来选择。

RTC时钟可以选择LXTAL时钟、IRC32K时钟或HXTAL时钟32分频，通过设置备用域控制寄存器（RCU_BDCTL）的RTCSRC位域来选择。

FWDGT时钟可以选择IRC32K时钟，当FWDGT启动时强制选择。

在GD32L233xx产品中，LPTIMER的时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的LPTIMERSEL位域来选择。在GD32L235xx产品中，LPTIMERx（x = 0, 1）的时钟可以选择IRC16MDIV时钟、LXTAL时钟、系统时钟或APB1时钟，通过设置配置寄存器2（RCU_CFG2）的LPTIMERxSEL（x = 0, 1）位域来选择。如果APB时钟分频系数为1，定时器的时钟频率与所在AHB总线频率一致。否则，定时器的时钟频率被设为与其相连的APB总线频率的2倍。

## 4.2.2. 主要特征

◼ 4到32 MHz外部高速晶体振荡器（HXTAL）；

◼ 16 MHz内部高速RC振荡器（IRC16M）；

◼ 48 MHz内部高速RC振荡器（IRC48M）；

◼ 32,768 Hz外部低速晶体振荡器（LXTAL）；

◼ 32 KHz内部低速RC振荡器（IRC32K）；

◼ PLL时钟源可以是HXTAL，IRC16M，IRC32K或IRC48M；

◼ HXTAL和LXTAL时钟监视。

## 4.2.3. 功能说明

## 高速外部晶体振荡器时钟（HXTAL）

4到48MHz的外部振荡器可为系统提供更为精确的主时钟。带有特定频率的晶体必须靠近两个HXTAL的引脚。和晶体连接的外部电阻和电容必须根据所选择的振荡器来调整。


图4-4. HXTAL时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/900b922efd0eb1aa88c90738953bee0bd5462afbd6bbac46f04204dfb60b41f7.jpg)


HXTAL晶体可以通过设置时钟控制寄存器RCU_CTL的HXTALEN位来启动或关闭，在时钟控制寄存器RCU_CTL中的HXTALSTB位用来指示高速外部振荡器是否已稳定。在启动时，直到这一位被硬件置‘1’，时钟才被释放出来。这个特定的延迟时间又称启动时间。当HXTAL时钟稳定后，如果在时钟中断寄存器RCU_INT中的相应中断使能位HXTALSTBIE位被置‘1’，将会产生相应中断。在这一点上，HXTAL时钟可以被直接用作系统时钟源或者PLL输入时钟。

将控制寄存器RCU_CTL的HXTALBPS和HXTALEN位置‘1’可以设置外部时钟旁路模式。旁路输入时，信号接至OSCIN，OSCOUT保持悬空状态，如 4-5. HXTAL 所示。此时，CK_HXTAL等于驱动OSCIN管脚的外部时钟。


图4-5. 旁路模式下HXTAL时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/99278a374d19bd92850a1370407400eb60ddbe4d1138343d6240cdeb103858d9.jpg)


## 高速内部 16MHz RC 振荡器时钟（IRC16M）

高速内部16MHz RC振荡器时钟，简称IRC16M时钟，拥有16MHz的固定频率，设备上电后CPU默认选择的时钟源就是IRC16M时钟。IRC16M RC振荡器能够在不需要任何外部器件的条件下提供更低成本类型的时钟源。IRC16M晶体可以通过设置时钟控制寄存器（RCU_CTL）中的IRC16MEN位被启动和关闭。时钟控制寄存器RCU_CTL中的IRC16MSTB位用来指示IRC16M内部RC振荡器是否稳定。IRC16M振荡器的启动时间比HXTAL晶体振荡器要更短。如果时钟中断寄存器RCU_INT中的相应中断使能位IRC16MSTBIE被置‘1’，在IRC16M稳定以后，将产生一个中断。IRC16M时钟也可用作PLL输入时钟。

工厂会校准IRC16M时钟频率的精度，但是它的精度仍然比HXTAL时钟要差。用户需求、环境条件和成本将决定选择哪个时钟作为系统时钟源。

如果HXTAL或者PLL是系统时钟源，为了最大程度减小系统从深度睡眠模式启动的时间，系统从深度睡眠模式初始唤醒的时候硬件强制IRC16M时钟作为系统时钟。

在深度睡眠模式下，可以通过LPUART（LPUART0 / LPUART1） / USART0 / USART1 / I2C0/I2C1/I2C2打开IRC16M。如果IRC16M在深度睡眠状态下打开，则应禁用未工作的外围设备以节省电源。

## 内部 48M RC 振荡器时钟（IRC48M）

内部48MHz RC振荡器时钟，简称IRC48M时钟，拥有48MHz的固定频率，当使用USBD模块时，IRC48M振荡器在不需要任何外部器件的条件下为用户提供了一种成本更低的时钟源选择。IRC48M RC振荡器可以通过设置RCU_CTL寄存器中的IRC48MEN位被启动和关闭。RCU_ADDCTL寄存器中的IRC48MSTB位用来指示内部48MHz RC振荡器是否稳定。如果RCU_ADDINT寄存器中的相应中断使能位IRC48MSTBIE被置‘1’，在IRC48M稳定以后，将产生一个中断。IRC48M时钟可做为USBD的系统时钟。

工厂会校准IRC48M时钟频率的精度，但是它的精度仍然不够精准。因为USB模块需要的时钟频率必须满足48MHz（500ppm）。CTC单元提供了一种硬件自动执行动态调整的功能将IRC48M时钟调整到需要的频率。

## 锁相环（PLL）

内部锁相环PLL通过对输入参考频率为4 ~ 48MHz的时钟基准2 ~ 64倍频，可以提供16 ~ 64

MHz的时钟输出。

PLL可以通过设置时钟控制寄存器（RCU_CTL）中的PLLEN位被启动和关闭。时钟控制寄存器RCU_CTL中的PLLSTB位用来指示PLL时钟是否稳定。如果时钟中断寄存器RCU_INT中的相应中断使能位PLLSTBIE被置‘1’，在PLL稳定以后，将产生一个中断。

## 低速外部晶体振荡器时钟（LXTAL）

LXTAL晶体是一个32.768KHz的低速外部晶体或陶瓷谐振器。它为实时时钟电路提供一个低功耗且精确的时钟源。LXTAL时钟可以通过设置备份域控制寄存器（RCU_BDCTL）中的LXTALEN位被启动和关闭。备份域控制寄存器RCU_BDCTL中的LXTALSTB位用来指示LXTAL时钟是否稳定。如果时钟中断寄存器RCU_INT中的相应中断使能位LXTALSTBIE被置‘1’，在LXTAL稳定以后，将产生一个中断。

将备份域控制寄存器RCU_BDCTL的LXTALBPS和LXTALEN位置‘1’可以选择外部时钟旁路模式。CK_LXTAL与连到OSC32IN脚上外部时钟信号一致。

当LPUART / LPUART0 / LPUART1 / USART0 / USART1使用LXTAL作为功能时钟时，可以打开LXTAL。

## 低速内部 RC振荡器时钟（IRC32K）

IRC32K RC振荡器时钟担当一个低功耗时钟源的角色，它的时钟频率大约32KHz，为独立看门狗定时器和实时时钟电路提供时钟。IRC32K提供低成本的时钟源，因为不需要外部器件。IRC32K RC振荡器可以通过设置复位源/时钟寄存器RCU_RSTSCK中的IRC32KEN位被启动和关闭。复位源/时钟寄存器RCU_RSTSCK中的IRC32KSTB位用来指示IRC32K时钟是否已稳定。如果时钟中断寄存器RCU_INT中的相应中断使能位IRC32KSTBIE被置‘1’，在IRC32K稳定以后，将产生一个中断。

## 系统时钟（CK_SYS）选择

系统复位后，IRC16M时钟被选为系统时钟，改变时钟配置寄存器RCU_CFG0中的系统时钟变换位SCS可以切换系统时钟源为HXTAL，PLL，IRC32K（仅适用于GD32L235xx产品）或者IRC48M。当SCS的值改变，系统时钟将使用原来的时钟源继续运行直到转换的目标时钟源稳定。当一个时钟源被直接或通过PLL间接作为系统时钟时，它将不能被停止。

## HXTAL 时钟监视器（CKM）

设置时钟控制寄存器RCU_CTL中的HXTAL时钟监视使能位CKMEN，HXTAL可以使能时钟监视功能。该功能必须在HXTAL启动延迟完毕后使能，在HXTAL停止后禁止。一旦监测到HXTAL故障，HXTAL将自动被禁止，时钟中断寄存器RCU_INT中的HXTAL时钟阻塞标志位CKMIF将被置‘1’，产生HXTAL故障事件。这个故障引发的中断和Cortex®-M23的不可屏蔽中断相连。如果HXTAL被选作系统或PLL的时钟源，HXTAL故障将促使选择IRC16M为系统时钟源且PLL将被自动禁止。

## LXTAL 时钟监视器（LCKM）

设置时钟控制寄存器RCU_CTL中的LXTAL时钟监视使能位LCKMEN，LXTAL可以使能时钟监

视功能。该功能必须在LXTAL启动延迟完毕和IRC32K使能后使能。

LXTAL上的时钟监视器在除VBAT以外的所有模式下工作。如果在外部32 KHz振荡器上检测到故障，可以向CPU发送中断。

然后，软件必须禁用LCKMEN位，停止有缺陷的32 KHz振荡器，并更改RTC时钟源，或采取任何必要的措施来保护应用程序。

当LCKMEN启用时，一个4位加一计数器将在IRC32K域工作。如果LXTAL时钟卡在0/1错误或时钟减慢约20KHz，计数器将溢出。将发现LXTAL时钟故障。

## 时钟输出功能

时钟输出功能输出从32KHz到64MHz的时钟。通过设置时钟配置寄存器RCU_CFG0中的CK_OUT时钟源选择位CKOUTSEL能够选择不同的时钟信号。相应的GPIO引脚应该被配置成复用功能I / O（AFIO）模式来输出选择的时钟信号。


表 4-1. 时钟源的选择


<table><tr><td>时钟源选择位</td><td>时钟源</td></tr><tr><td>000</td><td>无时钟</td></tr><tr><td>001</td><td>CK_IRC48M</td></tr><tr><td>010</td><td>CK_IRC32K</td></tr><tr><td>011</td><td>CK_LXTAL</td></tr><tr><td>100</td><td>CK_SYS</td></tr><tr><td>101</td><td>CK_IRC16M</td></tr><tr><td>110</td><td>CK_HXTAL</td></tr><tr><td>111</td><td>CK_PLL 或 CK_PLL/2</td></tr></table>

通过配置时钟配置寄存器RCU_CFG0的CKOUTDIV[2:0]位，可以将输出时钟按比例分频，进而降低CK_OUT频率。

## 深度睡眠 1 / 2模式时钟控制

当MCU处于深度睡眠1 / 2模式时，LPUART / LPUART0 / LPUART1 / USART0 / USART1外设时钟由LXTA提供且LXTAL时钟使能时，则LPUART / LPUART0 / LPUART1 / USART0 /USART1外设可以唤醒MCU。

如果LPUART / LPUART0 / LPUART1 / USART0 / USART1时钟选择IRC16M_DIV处于深度睡眠1 / 2模式时，则它们能够打开IRC16M时钟或关闭IRC16M时钟，从而使LPUART /LPUART0 / LPUART1 /USART0 / USART1 / I2C0 / I2C1 / I2C2从深度睡眠模式唤醒。

如果LPUART / LPUART0 / LPUART1 / USART0 / USART1时钟选择LXTAL处于深度睡眠1 /2模式时，则它们能够打开LXTAL时钟或关闭LXTAL时钟（如果LXTAL由软件打开，则LPUART/ LPUART0 / LPUART1 / USART0 / USART1不能关闭LXTAL），从而使LPUART从深度睡眠1/2模式唤醒。

如果I2C0 / I2C1 / I2C2选择IRC16M_DIV作为时钟源并处于深度睡眠1/2模式，则它们能够打开或关闭IRC16M时钟，从而使I2C0 / I2C1 / I2C2从深度睡眠1/2模式唤醒。

如果FMC和PMU在深度睡眠1/2模式下工作时，可以打开或关闭IRC16M时钟。

为了在深度睡眠1/2模式下省电，如果FMC / LPUART / LPUART0 / LPUART1/ USART0 /USART1未在深度睡眠1/2模式下工作，则它们的时钟可以单独选通。但I2C0 / I2C1 / I2C2、ADC、LPTIMER、PMU功能时钟不能由硬件选通，可以由软件禁用。
