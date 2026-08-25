## 7. 电源管理单元（PMU）

## 7.1. 简介

功耗设计是本系列产品比较注重的问题之一。电源管理单元提供了三种省电模式，包括睡眠模式，深度睡眠模式和待机模式。这些模式能减少电源能耗，且使得应用程序可以在CPU运行时间要求、速度和功耗的相互冲突中获得最佳折衷。如 7-1. 所示，本系列设备有三个电源域，包括V / V 域，VCORE域和备份域。V / V 域由电源直接供电。在V / V 域中嵌入了一个LDO，用来为VCORE域供电。在备份域中有一个电源切换器，当VDD电源关闭时，电源切换器可以将备份域的电源切换到VBAT引脚，此时备份域由VBAT引脚（电池）供电。

## 7.2. 主要特征

 三个电源域：备份域、V<sub>DD</sub> / V<sub>DDA</sub>域和VCORE电源域；

 三种省电模式：睡眠模式、深度睡眠模式和待机模式；

 内部电压调节器（LDO）提供VCORE电源；

 提供低电压检测器（LVD），当电压低于所设定的阈值时能发出中断或事件；

 当V<sub>DD</sub>供电关闭时，由VBAT（电池）为备份域供电；

 LDO输出电压用于节约能耗；

 供电监控：POR/PDR监控、LVD监控、VAVD监控、VOVD监控、VUVD监控；

 低驱动模式用于在深入睡眠模式下超低功耗。

## 7.3. 功能说明

7-1. 提供了PMU及相关电源域的内部结构框图。


图7-1. 电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/413994702a3419391ceddbc2eee41275094f668499a0fb301ef929f0bfce4fd2.jpg)



VAVD:模拟电压检测器


## 7.3.1. 电池备份域

电池备份域由内部电源切换器来选择VDD供电或VBAT（电池）供电，然后由VBAK为备份域供电，该备份域包含RTC（实时时钟）、LXTAL（低速外部晶体振荡器）、BPOR（备份域上电复位）、BREG（备份寄存器），以及PC13至PC15共3个BKP PAD。为了确保备份域中寄存器的内容及RTC正常工作，当VDD关闭时，VBAT引脚可以连接至电池或其他电源等备份源供电。电源切换器是由V<sub>DD</sub>/ V<sub>DDA</sub>域掉电复位电路控制的。对于没有外部电池的应用，建议将VBAT引脚通过100nF的外部陶瓷去耦电容连接到VDD引脚上。

备份域的复位源包括备份域上电复位和备份域软件复位。在VBAK没有完全上电前，BPOR信号强制设备处于复位状态。应用软件可以通过设置RCU_BDCTL寄存器BKPRST位来触发备份域软件复位。

RTC的时钟源可以是低速内部RC振荡器（IRC40K）或低速外部晶体振荡器（LXTAL），或高速外部晶体振荡器（HXTAL）时钟128分频，或AHB时钟10分频。当VDD被关闭时，RTC只能选择LXTAL作为时钟源。在通过WFI/WFE指令进入省电模式之前，Cortex®-M33需要通过RTC寄存器设置预期的唤醒时间并启用唤醒功能，以实现RTC定时器唤醒事件。进入省电模式一定时间之后，当经过的时间与预设的唤醒时间匹配时，RTC将唤醒设备。RTC的配置和操作的细节将在 RTC来描述。

当备份域由VDD供电（VBAK连接至VDD）时，以下功能可用：

 PC13可以作为通用I / O口或RTC功能引脚（参见 RTC ）；

 PC14和PC15可以作为通用I / O口或LXTAL晶振引脚。

当备份域由VBAT电源供电时（VBAK连接至VBAT），以下功能可用：

PC13仅可以作为RTC功能引脚（参见 RTC ）；

 PC14和PC15仅可作为LXTAL晶振引脚。

注意：由于PC13至PC15引脚是通过电源切换器供电的，电源切换器仅可通过小电流，因此当PC13至PC15的GPIO口在输出模式时，其工作的速度不能超过2MHz（最大负载为30Pf）。

## 7.3.2. VDD / VDDA 电源域

V<sub>DD</sub>/ V<sub>DDA</sub>域包括 V<sub>DD</sub>域和 V<sub>DDA</sub>域两部分。V<sub>DD</sub>域包括 HXTAL（高速外部晶体振荡器）、LDO（电压调节器）、LVD（低电压检测器）、POR / PDR（上电/掉电复位）、FWDGT（独立看门狗定时器）、IRC8M（内部 8M RC 振荡器）、IRC48M（内部 48M RC 振荡器）、VAVD(模拟电压检测)、IRC40K（内部 40KHz RC 振荡器）和 PLLs（锁相环）和除 PC13、PC14 和 PC15 之外的所有 PAD 等。V<sub>DDA</sub>域包括 ADC / DAC（AD / DA 转换器）、CMP(比较器)等。

## VDD 域

为 VCORE 域供电的 LDO（电压调节器），其复位后保持使能。可以被配置为三种不同的工作状态：包括睡眠模式（全供电状态）、深度睡眠模式（全供电或低功耗状态）和待机模式（关闭状态）。

POR / PDR（上电/掉电复位）电路检测 V 并在电压低于特定阈值时产生电源复位信号复位除备份域之外的整个芯片。 7-2. / 显示了供电电压和电源复位信号之间的关系。V<sub>POR</sub> 表示上电复位的阈值电压，V<sub>PDR</sub> 表示掉电复位的阈值电压, V<sub>hyst</sub> 表示迟滞电压，具体数值可参考值 datasheet。


图7-2. 上电/掉电复位波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/6059ce64ea477cf1d22e3691ff3a1cb4cc74af2bcf53e77fa2c3c3566ceb1419.jpg)



LVD 的功能是检测 $\mathsf { V } _ { \mathsf { D D } }$ 供电电压是否低于低电压检测阈值，该阈值由电源控制寄存器（PMU_CTL0）中的 LVDT[2:0]位进行配置。LVD 通过 LVDEN 置位使能，位于电源状态寄存器（PMU_CS）中的LVDF 位表示低电压事件是否出现，该事件连接至 EXTI 的第 16 线，用户可以通过配置 EXTI 的第16 线产生相应的中断。 7-3. LVD 显示了 $\mathsf { V } _ { \mathsf { D D } }$ 供电电压和 LVD 输出信号的关系。迟滞电压 $\Vdash _ { \tt N S t }$ 值参考 datasheet。



图7-3. LVD阈值波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/7f5a18c93985df0f8bde947c3a0d34ff0bbfb1b1d7e64d6d70ae74142801d282.jpg)


## VDDA 域

V 模拟电压检测器（VAVD）用于检测 V 电源电压是否低于电源控制寄存器（PMU_CTL0）中VAVDVC[1:0]位域选择的编程阈值。通过置位 VAVDEN 位能够使能 VAVD，PMU_CS 寄存器中的VAVDF 位指示 V<sub>DDA</sub> 高于或低于指定的 VAVD 阈值。 7-4. VAVD 显示了 VAVD门限与 VAVDF 之间的关系。迟滞电压 $\mathsf { V } _ { \mathsf { h y s t } }$ 值参考 datasheet。


图 7-4. VAVD 阈值监测波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/59e938a1cd57f89d38c96ef13d217327734024cddb02240f87682ba4394c10cc.jpg)



一般来说，数字电路由 VDD 供电，而大多数的模拟电路由 VDDA 供电。为了提高 ADC 和 DAC的转换精度，为 VDDA 独立供电可使模拟电路达到更好的特性。为避免噪声，VDDA 通过外部滤波电路连接至 VDD，相应的 V<sub>SSA</sub>通过特定电路连接至 VSS。否则，当 VDD /VDDA 不是同一个电源提供时，在上电和运行过程中 V<sub>DD</sub>与 V<sub>DDA</sub>差值不超过 0.3V。


为提高ADC和DAC 的精度，可将独立的外部参考电压连接至ADC / DAC 引脚VREFP / VREFN<sub>-</sub>。根据不同的封装，VREFP 可被连接至 V 引脚，或者外部参考电压，外部参考电压的范围请参考21-2. ADC 和 22-1. DAC 。VREFN 须被连接至 VSSA 引脚。VREFN 仅存在于不小于 48-pin 封装上，在其他封装里，其内部连接至 VSSA。

## 7.3.3. VCORE 电源域

VCORE 电源域为 Cortex<sup>®</sup>-M33 内核逻辑、AHB / APB 外设、备份域和 V<sub>DD</sub> / V<sub>DDA</sub> 域的 APB 接口等供电。包括 VUVD （VCORE 欠压检测器）和 VOVD（VCORE 过压检测器）。当 VCORE 电压上电后，POR 将在 VCORE 域中产生一个复位序列，复位完成后，如果要进入指定的省电模式，须先配置相关的控制位，之后一旦执行 WFI 或 WFE 指令，设备便进入该省电模式。关于这方面的详细内容，将在以下章节予以说明。该电源域的电压可以通过PMU CTL0寄存器中的LDOVS[2:0]配置。V<sub>CORE</sub>电压值请参考数据手册。

## VCORE电源域电源监测

芯片内部有一个 VCORE 电源域电压监测器，当 VOVDEN 为 0b1，将使能 VCORE 电源域电压检测器。一旦 VCORE 电源域超过电源控制寄存器（PMU_CTL0）中 VOVDVC[1:0]位选择的编程阈值，在模拟两个触发器同步后，VOVDF 将立即被置位。通过配置 PMU_CTL1 寄存器中的

VOVDO_DNF[7:0]位，可以使用数字滤波后的 VOVDF。允许抑制峰值的可编程长度为 1024*T<sub>PCLK</sub>(PCLK1 的周期)的 1 到 255。 7-5. VOVD 显示了 VOVD 门限与 VOVDF之间的关系,迟滞电压 $\vee _ { \mathsf { h y s t } }$ 值参考 datasheet。

注意：使能 VOVD 前，需要先使能 LVD，延迟 50us 之后，再使能 VOVD。否则 VOVD 会有误触发信号产生。后面 LVD 可以维持使能状态也可以关闭。


图7-5. VOVD阈值监测波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/2fdebcdc32b2e8aabd39593cbf807d16b9907eeb50eeec7197b55cdee93442f5.jpg)


芯片内部有一个 VCORE 电源域电压监测器，当 VUVDEN 为 0b1，将使能 VCORE 电源域电压检测器。一旦 VCORE 电源域低于电源控制寄存器（PMU_CTL0）中 VUVDVC[1:0]位选择的编程阈值，在模拟两个触发器同步后，VUVDF0 将立即被置位。通过配置 PMU_CTL1 寄存器中的VUVDO_DNF[7:0]位，可以使用数字滤波后的 VUVDF1。允许抑制峰值的可编程长度为 1024*$T _ { \mathsf { p c l k } } ( \mathsf { P C L K 1 }$ 的周期)的 1 到 255。 7-6. VUVD 显示了 VOVD 门限与 VOVDF 之间的关系,迟滞电压 $\Vdash _ { \tt V S t }$ 值参考 datasheet。


图7-6. VUVD阈值监测波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/86b9928173494a73e8bba47c911e98d75dfc2aeb66ce77356b851c1e955b18bf.jpg)


## 7.3.4. 省电模式

系统复位或电源复位后，MCU 处于全功能状态且电源域全部处于供电状态。实现较低的功耗的方法有三种：减慢系统时钟（HCLK，PCLK1，PCLK2），关闭未使用的外设的时钟或通过 PMU_CTL0寄存器的 LDOVS 来配置 LDO 输出电压。LDOVS 只有在 PLL 关闭情况下才可以配置，在 PLL 打开时，被配置的 LDO 输出电压才会被用来驱动 VCORE 电源域。当 PLL 关闭时，LDO 输出低电压模式驱动 VCORE 电源域。此外，三种省电模式可以实现更低的功耗，它们是睡眠模式、深度睡眠模式和待机模式。

## 睡眠模式

睡眠模式与 Cortex<sup>®</sup>-M33 的 SLEEPING 模式相对应。在睡眠模式下，仅关闭 Cortex<sup>®</sup>-M33 的时钟。如需进入睡眠模式，只要清除 Cortex®-M33 系统控制寄存器中的 SLEEPDEEP 位，并执行一条WFI 或WFE 指令即可。如果睡眠模式是通过执行WFI 指令进入的，任何中断都可以唤醒系统。如果睡眠模式是通过执行 WFE 指令进入的，任何唤醒事件都可以唤醒系统（如果 SEVONPEND为 1，任何中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。由于无需在进入或退出中断上消耗时间，该模式所需的唤醒时间最短。

根据 Cortex®-M33 中 SCR（系统控制寄存器）的 SLEEPONEXIT 位，有两种睡眠进入机制可选：

 Sleep-now：如果SLEEPONEXIT位被清零，一旦执行WFI或WFE指令，MCU立即进入睡眠模式；

 Sleep-on-exit：如果SLEEPONEXIT位被置位，当系统从最低优先级的中断处理程序离开后，

MCU立即进入睡眠模式。

## 深度睡眠模式

深度睡眠模式与 Cortex®-M33 的 SLEEPDEEP 模式相对应。在深度睡眠模式下，VCORE 域中的所有时钟全部关闭，IRC8M、IRC48M,、HXTAL 及 PLLs 也全部被禁用。SRAM 和寄存器中的内容被保留。根据 PMU_CTL0 寄存器的 LDOLP 位的配置，可控制 LDO 工作在正常模式或低功耗模式。进入深度睡眠模式之前，先将 Cortex®-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再清除 PMU_CTL0 寄存器的 STBMOD 位，然后执行WFI或WFE 指令即可进入深度睡眠模式。如果睡眠模式是通过执行WFI指令进入的，任何来自EXTI的中断可以将系统从深度睡眠模式中唤醒。如果睡眠模式是通过执行WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式中唤醒（如果 SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。刚退出深度睡眠模式时，IRC8M 被选中作为系统时钟。请注意，如果 LDO 工作在低功耗模式，那么唤醒时需额外的延时时间。

在深度睡眠模式下，通过配置 PMU_CTL0 寄存器的 LDEN，LDNP，LDLP，LDOLP 位可以进入低驱动模式。低驱动模式具有低驱动能力，低能耗。

正常驱动/正常功耗：将 PMU_CTL0 寄存器的 LDEN 位配置为 0b00，深度睡眠模式就工作在正常驱动模式下。将 PMU_CTL0 寄存器的 LDOLP 清 0 可以退出低功耗模式。

正常驱动/低功耗：将 PMU_CTL0 寄存器的 LDEN 位配置为 0b00，深度睡眠模式就工作在正常驱动模式下。将 PMU_CTL0 寄存器的 LDOLP 置 1 可以进入低功耗模式。

低驱动/正常功耗：将 PMU_CTL0寄存器的 LDEN 设置为 0b11，LDNP 置 1 可以进入深度睡眠模式的低驱动模式。将 PMU_CTL0 寄存器的 LDOLP 清 0 可以使 LDO 处于正常功耗模式。

低驱动/低功耗：将 PMU_CTL0 寄存器的 LDEN 设置为 0b11，LDLP 置 1 可以进入深度睡眠模式的低驱动模式。将 PMU_CTL0 寄存器的 LDOLP 清 1 可以使 LDO 处于正常功耗模式。

非低驱动：将 PMU_CTL0 寄存器的 LDEN 设置为 0b00，深度睡眠模式将不会处在低驱动模式。注意：为了顺利进入深度睡眠模式，所有 EXTI 线上的挂起状态（在 EXTI_PD 寄存器中）和相关外设标志位必须被复位，参考 3-3. EXTI 。否则，程序将直接跳过深度睡眠模式进入过程而继续执行下面的程序。

## 待机模式

待机模式是基于 Cortex®-M33 的 SLEEPDEEP 模式实现的。在待机模式下，整个 VCORE 域全部停止供电，同时 LDO 和包括 IRC8M、IRC48M、HXTAL 和 PLL 也会被关闭。进入待机模式前，先将 Cortex<sup>®</sup>-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的 STBMOD位置 1，再清除 PMU_CS 寄存器的 WUF 位，然后执行WFI 或WFE 指令，系统进入待机模式，PMU_CS 寄存器的 STBF 位状态表示 MCU 是否已进入待机模式。待机模式有四个唤醒源，包括来自 NRST 引脚的外部复位，RTC 报警，FWDGT 复位，WKUP 引脚的上升沿。待机模式可以达到最低的功耗，但唤醒时间最长。另外，一旦进入待机模式，SRAM 和 VCORE 电源域寄存器的内容都会丢失。退出待机模式时，会发生上电复位，复位之后 Cortex®-M33 将从 0x00000000 地

址开始执行指令代码。


表7-1. 节电模式总结


<table><tr><td>模式</td><td>睡眠</td><td>深度睡眠</td><td>待机</td></tr><tr><td>描述</td><td>仅关闭CPU时钟</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC8M、IRC48M、HXTAL和PLL</td><td>1、关闭VCORE电源域的供电2、关闭IRC8M、IRC48M、HXTAL和PLL</td></tr><tr><td>LDO状态</td><td>开启(正常功耗模式、正常驱动模式)</td><td>开启(正常功耗模式或低功耗模式、正常驱动模式或低驱动模式)</td><td>关闭</td></tr><tr><td>配置</td><td>SLEEPDEEP=0</td><td>SLEEPDEEP=1STBMOD=0</td><td>SLEEPDEEP=1STBMOD=1,WURST=1</td></tr><tr><td>进入指令</td><td>WFI或WFE</td><td>WFI或WFE</td><td>WFI或WFE</td></tr><tr><td>唤醒</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>1.NRST引脚2.WKUP引脚3.FWDGT复位4.RTC</td></tr><tr><td>唤醒延迟</td><td>无</td><td>IRC8M唤醒时间如果LDO处于低功耗模式,需增加LDO唤醒时间</td><td>上电序列</td></tr></table>


注意：在待机模式下，除了 NRST 引脚，配置为 RTC 功能的 PC13，用作 LXTAL 晶振引脚的 PC14和 PC15，使能的WKUP 引脚，其他所有 I / O 都处于高阻态。

