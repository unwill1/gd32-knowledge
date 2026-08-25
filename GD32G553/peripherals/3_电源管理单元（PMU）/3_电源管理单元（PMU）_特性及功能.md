## 3. 电源管理单元（PMU）

## 3.1. 简介

功耗设计是 GD32G553 系列产品比较注重的问题之一。电源管理单元提供了三种省电模式，包括睡眠模式，深度睡眠模式，和待机模式。这些模式能减少电源能耗，且使得应用程序可以在 CPU运行时间要求、速度和功耗的相互冲突中获得最佳折衷。如 3-1. 所示，GD32G553系列设备有三个电源域，包括 V<sub>DD</sub> / V<sub>DDA</sub>域，V<sub>CORE</sub>域和备份域。V<sub>DD</sub> / V<sub>DDA</sub>域由电源直接供电。在 V<sub>DD</sub> / V<sub>DDA</sub>域嵌入的 LDO 用来为 V<sub>CORE</sub>域供电。在备份域中有一个电源切换器，当 V<sub>DD</sub>电源关闭时，电源切换器可以将备份域的电源切换到 VBAT 引脚，此时备份域由 VBAT 引脚（电池）供电。

## 3.2. 主要特征

 三个电源域：备份域、V<sub>DD</sub> / V<sub>DDA</sub>域和V<sub>CORE</sub>电源域。

 三种省电模式：睡眠模式，深度睡眠模式，和待机模式。

 内部电压调节器（LDO）为核心电源域V<sub>CORE</sub>提供V<sub>CORE</sub>电源。

 提供低电压检测器（LVD），当电压低于所设定的阈值时能发出中断或事件。

 当V<sub>DD</sub>供电关闭时，由V<sub>BAT</sub>（电池）为备份域供电。

 供电监控：POR / PDR监控、BOR监控、LVD监控、VOVD监控、VAVD监控、VUVD监控、V<sub>BAK</sub>阈值监测、温度阈值监测。

## 3.3. 功能说明

3-1. 提供了 PMU 及相关电源域的内部结构框图。


图 3-1. 电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/45e349eca90e97bbc113ffc82d7625a1319dccafb0a541e1b219a0d10540effc.jpg)



图 3-2. V<sub>CORE</sub> 电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/8bd3409a85b037be8e0b956ea110addf7ea56e7966e4373c233cb310e0008f9e.jpg)



如图 3-2. VCORE 所示，V<sub>CORE</sub>域包含两个部分：


1. V<sub>COREOFF0</sub> 域包含：总线，Cortex®-M33 CPU，剩余 96K SRAM（除前 32K），外设；

2. 深度睡眠保持供电模块：FMC，PMU，RCU，EXTI，GPIO，前 32K SRAM，DBG，FWDGT，JTAG，I2C0，LPTIMER，SYSCFG，USART0。

电源切换器 S0 用于省电模式的供电控制。

## 3.3.1. 备份域

电池备份域由内部电源切换器来选择 V 供电或 V （电池）供电，然后由 V 为备份域供电，该备份域包含 RTC（实时时钟）、LXTAL（低速外部晶体振荡器），BPOR（备份域上电复位）和BREG（备份寄存器），PC13 至 PC15 共 3 个 BKP PAD，BVD（V<sub>BAK</sub>电压检测器），VBC（V<sub>BAK</sub>电池充电）以及 BKP_BGP（备份域带隙基准）。为了确保备份域中寄存器的内容及 RTC 正常工作，当 V<sub>DD</sub>关闭时，VBAT 引脚可以连接至电池或其他备份电源供电。电源切换器是由 V<sub>DD</sub>/ V<sub>DDA</sub>域掉电复位电路控制的。对于没有外部电池的应用，建议将 VBAT 引脚通过 100nF 的外部陶瓷去耦电容连接到 VDD 引脚上。

备份域的复位源包括备份域上电复位和备份域软件复位。在 V<sub>BAK</sub>没有完全上电前，BPOR 信号强制设备处于复位状态。应用软件可以通过设置 RCU_BDCTL 寄存器 BKPRST 位来触发备份域软件复位。

RTC的时钟源可以是低速内部32KHz RC振荡器（IRC32K）或低速外部晶体振荡器（LXTAL），或由高速外部晶体振荡器（HXTAL）时钟32分频。当V<sub>DD</sub>被关闭时，RTC只能选择LXTAL作为时钟源。在通过WFI / WFE指令进入省电模式之前，Cortex®-M33能够通过RTC寄存器预期的唤醒时间并启用唤醒功能或者根据EXTI，以实现RTC定时器唤醒事件。进入省电模式一定时间之后，当经过的时间与预设的唤醒时间匹配时，RTC将唤醒设备。RTC的配置和操作的细节将在 RTC来描述。

当备份域由V<sub>DD</sub>供电（V<sub>BAK</sub>连接至V<sub>DD</sub>）时，以下功能可用：

 PC13可以作为通用I/O口或RTC功能引脚（参见 RTC ）；

 PC14和PC15可以作为通用I/O口或LXTAL晶振引脚。

当备份域由V<sub>BAT</sub>电源供电时（V<sub>BAK</sub>连接至V<sub>BAT</sub>），以下功能可用：

 PC13仅可以作为RTC功能引脚（参见 RTC ）；

 PC14和PC15仅可作为LXTAL晶振引脚。

注意：由于 PC13 至 PC15 引脚是通过电源切换器供电的，电源切换器仅可通过小电流，因此当PC13至 PC15 的 GPIO 口在输出模式时，其工作的速度不能超过 2MHz（最大负载为 30pF）。

V<sub>DD</sub>可以通过一个内部电阻给外部电池充电。通过配置 PMU_CTL2 寄存器中 VCRSEL 位，可以选择内部电阻 5K 欧姆或 1.5K欧姆用于外部 V<sub>BAT</sub>电池充电。将 PMU_CTL2 寄存器中 VCEN 位置1 可以使能 V<sub>BAT</sub>电池充电。在 BKP only模式，V<sub>BAT</sub>电池充电不可用。

## 备份域电压阈值监测

芯片内部有一个内部电源开关，可以选择备份域的电压源为 V 或 V 。当 VBTMEN 位置位时，备份域（V<sub>BAK</sub>）的电源电压可以通过上限电压和下限电压（V<sub>BAKT</sub>和 V<sub>BAKB</sub>）进行监控，如果 V<sub>BAK</sub>超过 V<sub>BAKT</sub>，则标志位 VBATHF 将设置，如果 V<sub>BAK</sub> 低于 V<sub>BAKB</sub>，则标志位 VBATLF 将设置。 3-3.，显示了备用域电压阈值监测。


图 3-3. 备用域电压阈值的波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/fb2eaa024923089d8d0b45f241de02d1bcef1f8ce336ddf0783998ad177a094e.jpg)


## 温度电压阈值监测

和备份域电压阈值监测类似，通过与温度高、低两个阈值水平比较可以来监测结温。PMU_CTL1寄存器中 TEMPHF 和 TEMPLF 标志指示设备温度是否高于或低于阈值。可以通过 PMU_CTL1 寄存器中的 VBTMEN 位使能 / 关闭温度电压阈值监测。使能后，温度阈值监测将增加功耗。温度阈值监测可以用来触发执行温度控制任务的相关的程序。只有 PMU_CTL1 寄存器中的 BKPVSEN位置位，温度阈值监测才有效。

TEMPH 和 TEMPL 唤醒中断可用于 RTC 侵入信号


图 3-4. 温度阈值监测


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/0fd9019d8ac0c3332dbc68b62866440b8270ac0b0237ecd5529f23d2f2a212d9.jpg)


## 3.3.2. V<sub>DD</sub> / V<sub>DDA</sub> 电源域

V<sub>DD</sub> / V<sub>DDA</sub> 域包括 V<sub>DD</sub> 域和 V<sub>DDA</sub> 域两部分。V<sub>DD</sub> 域包括 HXTAL（高速外部晶体振荡器）、IRC8M（内部 8MHz RC 振荡器时钟）、IRC32K（内部 32KHz RC 振荡器时钟）、LDO（电压调节器）、BOR（欠压复位）、FWDGT（独立看门狗定时器）、PLL（锁相环）、LVD（低电压检测器）、VOVD（V<sub>CORE</sub>过压检测器）、VAVD（V<sub>DDA</sub>电压检测器）、VUVD（V<sub>CORE</sub>低压检测器）和除 PC13、PC14和 PC15 之外的所有 PAD 等。V<sub>DDA</sub>域包括 ADC / DAC（AD / DA 转换器）、POR / PDR（上电 /掉电复位）、CMP（比较器），HATS（高精度温度传感器）、LTD_BGR（低温漂带隙基准）、VREF_BUF（电压缓冲器）等。

## V<sub>DD</sub> 域

为 V<sub>CORE</sub>域供电的 LDO（电压调节器），其复位后保持使能。可以被配置为不同的工作状态：包括睡眠模式（V<sub>CORE</sub>全供电状态）、深度睡眠模式（低功耗状态）和待机模式（关闭状态）。

POR / PDR（上电 / 掉电复位）电路检测 V<sub>DD</sub> / V<sub>DDA</sub>并在电压低于特定阈值时产生电源复位信号复位除备份域之外的整个芯片。 3-5. / 显示了供电电压和电源复位信号之间的关系。V 表示上电复位的阈值电压， V 表示掉电复位的阈值电压。迟滞电压 $\vee _ { \mathsf { h y s t } }$ 值参考 datasheet。


图 3-5. 上电 / 掉电复位波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/808a83b0efef34b25a6aa1c2e2b817879a297f2caedbe97451cec449b6880674.jpg)


BOR 电路检测 V<sub>DD</sub> / V<sub>DDA</sub>并在 BOR_TH 不为 0b11，同时电压低于选项字节的 BOR_TH 定义的阈值时产生电源复位信号复位除备份域之外的整个芯片。POR / PDR（上电/掉电复位）电路处于检测状态，无论选项字节的 BOR_TH 是否为 0b11。 3-6. BOR 显示了供电电压和 BOR 复位信号之间的关系。V<sub>BOR</sub>表示 BOR 复位的阈值电压，该值在选项字节 BOR_TH 中定义。迟滞电压 $\mathsf { V } _ { \mathsf { h y s t } }$ 值参考 datasheet。


图 3-6. BOR 波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/12831f19b01befd149cb38e0fc777702b791c3f39955799361a748a37b664a01.jpg)


## V<sub>DDA</sub> 域

LVD 的功能是检测 V<sub>DD</sub> / V<sub>DDA</sub> 供电电压是否低于低电压检测阈值，该阈值由电源控制寄存器 0（PMU_CTL0）中的 LVDT[2:0]位进行配置。LVD 通过 LVDEN 置位使能，位于电源控制状态寄存器（PMU_CS）中的 LVDF 位表示低电压事件是否出现，该事件连接至 EXTI 的第 16 线，用户可以通过配置 EXTI 的第 16 线产生相应的中断。 3-7.LVD 显示了 V<sub>DD</sub>/ V<sub>DDA</sub>供电电压和 LVD 输出信号的关系。（LVD 中断信号依赖于 EXTI 第 16 线的上升或下降沿配置）。迟滞电压$\Vdash _ { \mathsf { h y s t } }$ 值参考 datasheet。


图 3-7. LVD 阈值波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/8cf6a231e0918b18e6864d835a978d2ea6e93366366eb814af9cf8141bc1a20d.jpg)


V<sub>DDA</sub> 模拟电压检测器（VAVD）用于检测 V<sub>DDA</sub> 电源电压是否低于电源控制寄存器（PMU_CTL0）中 VAVDVC[1:0]位域选择的编程阈值。通过置位 VAVDEN 位能够使能 VAVD，PMU_CS 寄存器中的 VAVDF 位指示 V<sub>DDA</sub>高于或低于指定的 VAVD 阈值，如果 VAVDF 置位能够产生对应的事件，这个事件在内部连接到 EXTI 第 16 线。如果通过 EXTI 寄存器使能，可以产生一个中断。

3-8. VAVD 显示了 VAVD 门限与 VAVDF 之间的关系。迟滞电压 $\mathsf { V } _ { \mathsf { h y s t } }$ 值参考datasheet。


图 3-8. VAVD 阈值监测波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/d18a728e42b77bc08290f90febaf9f7766e14446924a2c760ed78b1efadab960.jpg)


$$
V _ {D D A}
$$

$$
V _ {D D A}
$$

$$
V _ {D D}
$$

为提高 ADC 和 DAC 的精度，可将独立的外部参考电压连接至 ADC / DAC 引脚 VREFP。根据不同的封装，VREFP 可被连接至 VDDA 引脚，或者外部参考电压，外部参考电压的范围请参考17-2. ADC 和 18-1. DAC 。

## 3.3.3. V<sub>CORE</sub> 电源域

主要功能包括 Cortex®-M33 内核逻辑、AHB / APB 外设、备份域和 V<sub>DD</sub> / V<sub>DDA</sub> 域的 APB 接口等。当 V<sub>CORE</sub>电压上电后，POR 将在 V<sub>CORE</sub>域中产生一个复位序列，复位完成后，如果要进入指定的省电模式，须先配置相关的控制位，之后一旦执行 WFI 或 WFE 指令，设备便进入该省电模式。可通过 PMU_CTL0 寄存器中的 LDOVS[4:0]配置该电源域的电压。

## V<sub>CORE</sub>电源域电源监测

芯片内部有一个V<sub>CORE</sub>电源域电压监测器，当VOVDEN为0b1，将使能V<sub>CORE</sub>电源域电压检测器。一旦 V<sub>CORE</sub>电源域超过电源控制寄存器（PMU_CTL0）中 VOVDVC[1:0]位选择的编程阈值，在模拟两个触发器同步后，VOVDF0 将立即被置位。该事件在内部连接到 EXTI16，如果通过 EXTI 使能，则可以产生中断。通过配置 PMU_CTL3 寄存器中的 VOVDO_DNF[7:0]位，可以使用数字滤波后的 VOVDF1。允许抑制峰值的可编程长度为 $1 0 2 4 ^ { \star } \mathsf { T } _ { \mathsf { p c l k } }$ 的 1 到 255。VOVDF1 中断与 IRQ63内部连接。滞电压 $\Vdash _ { \tt N S t }$ 值参考 datasheet。


图 3-9. VOVD 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/6dca10d5788aef5bf550774173e3214f37c0431ee7cf46b6bbe9594bab343f13.jpg)


芯片内部有一个 $\mathsf { V } _ { \mathsf { C O R E } }$ 电源域电压监测器，当 VUVDEN 为0b1，将使能 $\mathsf { V } _ { \mathsf { C O R E } }$ 电源域电压检测器。一旦 V<sub>CORE</sub>电源域低于电源控制寄存器（PMU_CTL0）中 VUVDVC[1:0]位选择的编程阈值，在模拟两个触发器同步后，VUVDF0 将立即被置位。该事件在内部连接到 EXTI16，如果通过 EXTI 使能，则可以产生中断。通过配置 PMU_CTL3 寄存器中的 VUVDO_DNF[7:0]位，可以使用数字滤波后的 VUVDF1。允许抑制峰值的可编程长度为 $1 0 2 4 ^ { \star } \mathsf { T } _ { \mathsf { p c l k } }$ 的 1 到 255。VUVDF1 中断与 IRQ63内部连接。滞电压 $\Vdash _ { \mathsf { h y s t } }$ 值参考 datasheet。


图 3-10. VUVD 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/d6ad705c4a6bde021d2673bc1db2fdd9ca4179670bca8290090379761dbe7d29.jpg)


## 3.3.4. 省电模式

系统复位或电源复位后，GD32G553MCU 处于全功能状态且电源域全部处于供电状态。实现较低的功耗的方法有三种：减慢系统时钟（HCLK，PCLK1，PCLK2 和 PCLK3），或者关闭未使用的外设的时钟。此外，三种省电模式可以实现更低的功耗，它们是睡眠模式，深度睡眠模式和待机模式。


表3-1. 节电模式总结


<table><tr><td>模式</td><td>睡眠</td><td>深度睡眠</td><td>待机</td></tr><tr><td>描述</td><td>仅关闭CPU时钟</td><td>1. 关闭VCORE电源域的所有时钟2. 关闭IRC8M、HXTAL和PLL</td><td>1. 关闭VCORE电源域的所有时钟2. 关闭IRC8M、HXTAL和PLL</td></tr><tr><td>LDO状态</td><td>开启</td><td>开启或者低功耗模式</td><td>关闭</td></tr><tr><td>配置</td><td>SLEEPDEEP=0</td><td>SLEEPDEEP=1,STBMOD=0</td><td>SLEEPDEEP=1STBMOD=1,WURST=1</td></tr><tr><td>进入指令</td><td>执行WFI或WFE</td><td>执行WFI或WFE</td><td>执行WFI或WFE</td></tr><tr><td>唤醒</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(当SEVONPEND=1时的中断)均可唤醒</td><td>若通过WFI进入,来自EXTI的任何中断均可唤醒;若通过WFE进入,来自EXTI任何事件(当SEVONPEND=1时的中断)可唤醒</td><td>1. NRST引脚2. WKUP引脚3. FWDGT复位4. RTC5. LCKMD</td></tr><tr><td>唤醒延时</td><td>无</td><td>IRC8M唤醒时间,如果LDO在低功耗模式,增加LDO唤醒时间</td><td>上电序列</td></tr></table>

## 睡眠模式

睡眠模式与 Cortex<sup>®</sup>-M33 的 SLEEPING 模式相对应。在睡眠模式下，仅关闭 Cortex<sup>®</sup>-M33 的时钟。如需进入睡眠模式，只要清除 Cortex®-M33 系统控制寄存器中的 SLEEPDEEP 位，并执行一条WFI 或WFE 指令即可。如果睡眠模式是通过执行WFI 指令进入的，任何中断都可以唤醒系统。如果睡眠模式是通过执行 WFE 指令进入的，任何唤醒事件都可以唤醒系统（如果 SEVONPEND为 1，任何中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。由于无需在进入或退出中断上消耗时间，该模式所需的唤醒时间最短。

根据 Cortex®-M33 中 SCR（系统控制寄存器）的 SLEEPONEXIT 位，有两种睡眠进入机制可选：

 Sleep-now：如果SLEEPONEXIT位被清零，一旦APB系统复位或者执行WFI / WFE指令，MCU立即进入睡眠模式；

 Sleep-on-exit：如果SLEEPONEXIT位被置位，当系统从最低优先级的中断处理程序离开后，

MCU立即进入睡眠模式。

## 深度睡眠模式

深度睡眠模式与 Cortex®-M33 的 SLEEPDEEP 模式相对应。在深度睡眠模式下，V 域中的所有时钟全部关闭，IRC8M、HXTAL 及 PLL 也全部被禁用。SRAM 和寄存器的内容被保留。根据PMU_CTL0 寄存器中的 LDOLP位，LDO 可以正常工作，也可以在低功耗模式下工作。进入深度睡眠模式之前，先将 Cortex<sup>®</sup>-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再清除 PMU_CTL0寄存器的 STBMOD 位，然后执行 WFI 或 WFE 指令即可进入深度睡眠模式。如果睡眠模式是通过执行 WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式中唤醒。如果睡眠模式是通过执行WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式中唤醒（如果SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。当退出深度睡眠模式时，IRC8M 被选择为系统时钟。注意，如果 LDO 在低功耗模式下工作，则会产生额外的唤醒延迟。

注意：为了顺利进入深度睡眠模式，必须重置所有 EXTI 挂起状态（EXTI_PD 寄存器）和相关的外设标志。如果没有，程序将跳过深度睡眠模式的进入过程，继续执行下面程序。

## 待机模式

待机模式是基于 Cortex®-M33 的 SLEEPDEEP 模式实现的。在待机模式下，整个 V<sub>CORE</sub>域全部停止供电，LDO 关闭，同时包括 IRC4M、HXTAL 和 PLL 也会被关闭。进入待机模式前，先将 Cortex®-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的 STBMOD 位域置位，再清除 PMU_CS 寄存器的 WUF 位，然后执行WFI 或 WFE指令，系统进入待机模式，PMU_CS寄存器的 STBF 位状态表示 MCU 是否已进入待机模式。待机模式有五个唤醒源，包括来自 NRST引脚的外部复位，RTC 闹钟，FWDGT 复位，LXTAL 时钟失败检测，WKUP 引脚的上升沿。待机模式可以达到最低的功耗，但唤醒时间最长。另外，一旦进入待机模式，SRAM 和 V<sub>CORE</sub>电源域寄存器的内容都会丢失。退出待机模式时，会发生上电复位，复位之后 Cortex®-M33 将从0x00000000 地址开始执行指令代码。

## BKP 模式

当 VDD 引脚被外部电源开关切断时，进入 BKP 模式。当 VBAT 供电时，BKP 域包括 RTC/LXTAL/BKP POR 是开启的。在这种模式下，用户可以使用 RTC，当 VDD 引脚供电时，退出 BKP模式。
