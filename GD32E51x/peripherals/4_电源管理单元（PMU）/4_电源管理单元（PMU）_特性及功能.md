## 4. 电源管理单元（PMU）

## 4.1. 简介

功耗设计是 GD32E51x 系列产品比较注重的问题之一。电源管理单元提供了五种省电模式，包括睡眠模式，深度睡眠模式，深度睡眠模式 1，深度睡眠模式 2 和待机模式。这些模式能减少电源能耗，且使得应用程序可以在 CPU 运行时间要求、速度和功耗的相互冲突中获得最佳折衷。如 4-1. 所示，GD32E51x 系列设备有三个电源域，包括 V / V 域，V 域和备份域。V / V 域由电源直接供电。在 V / V 域中嵌入了一个 LDO，用来为 V 域供电。在备份域中有一个电源切换器，当 VDD 电源关闭时，电源切换器可以将备份域的电源切换到 VBAT 引脚，此时备份域由 VBAT 引脚（电池）供电。

## 4.2. 主要特性

 三个电源域：备份域、 $\mathsf { V } _ { \mathsf { D D } } / \mathsf { V } _ { \mathsf { D D A } }$ 域和V<sub>CORE</sub>电源域；

 五种省电模式：睡眠模式、深度睡眠模式，深度睡眠模式1，深度睡眠模式2和待机模式；

 内部电压调节器（LDO）为V<sub>CORE</sub>电源域提供V<sub>CORE</sub>电源；

 提供低电压检测器，当电压低于所设定的阈值时能发出中断或事件；

 当VDD供电关闭时，由VBAT（电池）为备份域供电；

 LDO输出电压用于节约能耗；

 低驱动模式用于在深入睡眠模式 / 深度睡眠模式1 / 深度睡眠模式2下超低功耗。高驱动模式用在高频模式中。

## 4.3. 功能描述

4-1. 提供了 PMU 及相关电源域的内部结构框图。


图 4-1. 电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/ffe8118b693397063bf3666e0df5b2a353176829857e6588f32f6c887aff923c.jpg)



图 4-2. V<sub>CORE</sub> 电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/ff77ed1f9667745c75d26c7f492b1b3e3bb6b0497af42850e994a22ca32ad388.jpg)



如图 4-2. VCORE 所示，V 域包含三个部分：


1. COREOFF1 域包含：ENET，SHRTIMER，USBHS（USBHS 逻辑控制部分），TMU 外设。

2. COREOFF0 域包含：

– 剩余AHB/APB IPs：除了FMC，PMU，RCU，EXTI，GPIO，DBG，FWDGT（仅寄存器），WWDGT，USART5，I2C2，以及COREOFF1域之外的所有V<sub>CORE</sub>域外设；剩余96K SRAM：SRAM（除前32K）；

$$
- \quad \text { Cortex } ^ {\text { R }} \text {-M33 CPU; }
$$

– 总线：包括一个AHB互联矩阵、两个AHB总线和两个APB总线。

3. 深度睡眠保持供电模块：FMC，PMU，RCU，EXTI，GPIO，DBG，FWDGT（仅寄存器），WWDGT，USART5，I2C2，以及前 32K SRAM。

电源切换器 S0 和 S1 用于省电模式的供电控制。

## 4.3.1. 备份域

备份域由内部电源切换器来选择 VDD 供电或 VBAT（电池）供电，然后由 V 为备份域供电，该备份域包含 RTC（实时时钟）、LXTAL（低速外部晶体振荡器）、BPOR（备份域上电复位）、BREG（备份寄存器），以及 PC13 至 PC15 共 3 个 PAD。为了确保备份域中寄存器的内容及RTC 正常工作，当 VDD 关闭时，VBAT 引脚可以连接至电池或其他电源等备份源供电。电源切换器是由 V<sub>DD</sub>/ V<sub>DDA</sub>域掉电复位电路控制的。对于没有外部电池的应用，建议将 VBAT 引脚通过 100nF 的外部陶瓷去耦电容连接到 V 引脚上。

备份域的复位源包括备份域上电复位和备份域软件复位。在 V 没有完全上电前，BPOR 信号强制设备处于复位状态。应用软件可以通过设置 RCU_BDCTL 寄存器 BKPRST 位来触发备份域软件复位。

RTC 的时钟源可以是低速内部 RC 振荡器（IRC40K）或低速外部晶体振荡器（LXTAL），或高速外部晶体振荡器（HXTAL）时钟 128 分频。当 VDD 被关闭时，RTC 只能选择 LXTAL 作为时钟源。在通过 WFI/WFE 指令进入省电模式之前，Cortex®-M33 需要通过 RTC 寄存器设置预期的闹钟时间并启用闹钟功能，通过 EXTI 线获取 RTC 闹钟事件。进入省电模式一定时间之后，当经过的时间与预设的闹钟时间匹配时，RTC 将唤醒设备。RTC 的配置和操作的细节将在 RTC 来描述。

当备份域由 VDD 供电（V<sub>BAK</sub>连接至 V<sub>DD</sub>）时，以下功能可用：

 PC13可以作为通用I/O口或RTC功能引脚（参见 RTC ）；

 PC14和PC15可以作为通用I/O口或LXTAL晶振引脚。

当备份域由 VBAT 电源供电时（V 连接至 V ），以下功能可用：

PC13仅可以作为RTC功能引脚（参见 RTC ）；

 PC14和PC15仅可作为LXTAL晶振引脚。

注意：由于 PC13至 PC15 引脚是通过电源切换器供电的，电源切换器仅可通过小电流，因此当PC13至PC15的GPIO口在输出模式时，其工作的速度不能超过2MHz(最大负载为30pF)。

## 4.3.2. V<sub>DD</sub> / V<sub>DDA</sub> 电源域

V<sub>DD</sub> / V<sub>DDA</sub>域包括 V<sub>DD</sub>域和 V<sub>DDA</sub>域两部分。V<sub>DD</sub>域包括 HXTAL（高速外部晶体振荡器）、LDO（电压调节器）、FWDGT（独立看门狗定时器）和除 PC13、PC14 和 PC15 之外的所有 PAD等等。V<sub>DDA</sub>域包括 POR / PDR（上电 / 掉电复位）、ADC / DAC（AD / DA 转换器）、CMP（比较器）、IRC8M（内部 8M RC 振荡器）、IRC48M（内部 48M RC 振荡器）、IRC40K（内部 40KHz

RC 振荡器）、PLLs（锁相环）和 LVD（低电压检测器）等等。

## V<sub>DD</sub> 域

为 V 域供电的 LDO（电压调节器），其复位后保持使能。可以被配置为三种不同的工作状态：包括睡眠模式（全供电状态）、深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2（全供电或低功耗状态）和待机模式（关闭状态）。

BOR 电路检测 VDD 并在电压低于选项字节的 BOR_TH 定义的阈值且该阈值不为 0b11（BOR_TH=0b11，BOR 功能关闭）时产生电源复位信号复位除备份域之外的整个芯片。不管选项字节 BOR_TH 的值是否为 0b11，POR/ PDR（上电/掉电复位）电路会一直处于检测状态。 4-3. BOR 显示了供电电压和 BOR 复位信号之间的关系。V<sub>BOR</sub>表示 BOR 复位的阈值电压，该值在选项字节 BOR_TH 中定义。迟滞电压 V<sub>hyst</sub>值参考数据手册。


图 4-3. BOR 波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/459de08e676ac12d909404dae48f21121b71c53fef50b8b1488a4181ec863c29.jpg)


## V<sub>DDA</sub> 域

POR / PDR（上电 / 掉电复位）电路检测 VDDA并在电压低于特定阈值时产生电源复位信号复位除备份域之外的整个芯片。 4-4. / 显示了供电电压和电源复位信号之间的关系。V<sub>POR</sub>表示上电复位的阈值电压，V<sub>PDR</sub>表示掉电复位的阈值电压。迟滞电压 V<sub>hys</sub>值参考数据手册。


图 4-4. 上电/掉电复位波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/821b92df7f75f628294989d232fbf20d39fc656a8c9b6e5703fe934ab11e635a.jpg)


LVD 的功能是检测 VDDA 供电电压是否低于低电压检测阈值，该阈值由电源控制寄存器(PMU_CTL0)中的 LVDT[2:0]位进行配置。LVD 通过 LVDEN 置位使能，位于电源状态寄存器(PMU _CS0)中的 LVDF 位表示低电压事件是否出现，该事件连接至 EXTI 的第 16 线，用户可以通过配置 EXTI 的第 16 线产生相应的中断。 4-5. LVD 显示了 VDDA 供电电压和 LVD 输出信号的关系。（LVD 中断信号依赖于 EXTI第 16 线的上升或下降沿配置）。迟滞电压 $\vee _ { \mathsf { h y s t } }$ 值参考数据手册。


图 4-5. LVD 阈值波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/68a66699164edc2a6244742fb58e069bbc83df1ca14803d7b9e432a32b275945.jpg)


一般来说，数字电路由 VDD 供电，而大多数的模拟电路由 VDDA供电。为了提高 ADC 和 DAC的转换精度，为 VDDA 独立供电可使模拟电路达到更好的特性。为避免噪声，VDDA通过外部滤波电路连接至 VDD，相应的 VSSA 通过特定电路连接至 VSS。否则，当 VDD 和 VDDA 不是同一个电源提供时，在上电和运行过程中 V 与 V 差值不超过 0.3V。

为提高 ADC 和 DAC 的精度，可将独立的外部参考电压连接至 ADC / DAC 引脚 VREFP /

VREFN。根据不同的封装，VREFP可被连接至 VDDA 引脚，或者外部参考电压，外部参考电压的范围请参考 13-2. ADC 和 14-1. DAC 。VREFN 须被连接至 VSSA引脚，VREFP 引脚仅存在于不小于 100-pin 封装上，而在 64-pin 或更少引脚封装不存在，因其内部已经连接至 VDDA 和 VSSA。VREFN 仅存在于不小于 100-pin 封装上，在其他封装里，其内部连接至 VSSA。

## 4.3.3. V<sub>CORE</sub> 电源域

主要功能包括 Cortex<sup>®</sup>-M33 内核逻辑、AHB / APB 外设、备份域和 V<sub>DD</sub> / V<sub>DDA</sub> 域的 APB 接口等。当 V 电压上电后，POR 将在 V 域中产生一个复位序列，复位完成后，如果要进入指定的省电模式，须先配置相关的控制位，之后一旦执行WFI 或WFE 指令，设备便进入该省电模式。关于这方面的详细内容，将在以下章节予以说明。V 电压值请参考数据手册。

## 高驱动模式

如果 V<sub>CORE</sub>电源域工作在高频状态下，且打开了多种功能，建议进入高驱动模式。使用高驱动模式有以下步骤：

 选择系统时钟为IRC8M或HXTAL；

 将PMU_CTL0寄存器的HDEN置1，使能高驱动模式；

 等待PMU_CS0寄存器的HDRF被置位；

 将PMU_CTL0寄存器的HDS置1，将LDO切换到高驱动模式；

 等待PMU_CS0寄存器的HDSRF被置位。进入高驱动模式；

 工作在高频状态。

在选择 IRC8M 或 HXTAL 作为系统时钟后，可以通过将 PMU_CTL0 寄存器的 HDEN 和 HDS清 0 退出高驱动模式。当系统退出深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 时，将会自动退出高驱动模式。

## 4.3.4. 省电模式

系统复位或电源复位后，GD32E51x MCU 处于全功能状态且电源域全部处于供电状态。实现较低的功耗的方法有三种：减慢系统时钟（HCLK，PCLK1，PCLK2），关闭未使用的外设的时钟。此外，五种省电模式可以实现更低的功耗，它们是睡眠模式、深度睡眠模式，深度睡眠模式 1，深度睡眠模式 2 和待机模式。

## 睡眠模式

睡眠模式与 Cortex<sup>®</sup>-M33 的 SLEEPING 模式相对应。在睡眠模式下，仅关闭 Cortex<sup>®</sup>-M33 的时钟。如需进入睡眠模式，只要清除 Cortex®-M33 系统控制寄存器中的 SLEEPDEEP 位，并执行一条 WFI 或 WFE 指令即可。如果睡眠模式是通过执行 WFI 指令进入的，任何中断都可以唤醒系统。如果睡眠模式是通过执行 WFE 指令进入的，任何唤醒事件都可以唤醒系统（如果 SEVONPEND 为 1，任何中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。由于无需在进入或退出中断上消耗时间，该模式所需的唤醒时间最短。

根据 Cortex®-M33 中 SCR（系统控制寄存器）的 SLEEPONEXIT 位，有两种睡眠进入机制可选：

 Sleep-now：如果SLEEPONEXIT位被清零，一旦执行WFI或WFE指令，MCU立即进入睡眠模式；

 Sleep-on-exit：如果SLEEPONEXIT位被置位，当系统从最低优先级的中断处理程序离开后，MCU立即进入睡眠模式。

## 深度睡眠模式

深度睡眠模式与 Cortex®-M33 的 SLEEPDEEP 模式相对应。在深度睡眠模式下，V 域中的所有时钟全部关闭，IRC8M、IRC48M、HXTAL 及 PLLs 也全部被禁用。SRAM 和寄存器中的内容被保留。根据 PMU_CTL0 寄存器的 LDOLP位的配置，可控制 LDO 工作在正常模式或低功耗模式。进入深度睡眠模式之前，先将 Cortex®-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再清除 PMU_CTL0 寄存器的 STBMOD 位，然后执行 WFI 或 WFE 指令即可进入深度睡眠模式。如果睡眠模式是通过执行WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式中唤醒。如果睡眠模式是通过执行 WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式中唤醒（如果 SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。刚退出深度睡眠模式时，IRC8M 被选中作为系统时钟。请注意，如果 LDO 工作在低功耗模式，那么唤醒时需额外的延时时间。

在深度睡眠模式下，通过配置 PMU_CTL0 寄存器的 LDEN，LDNP，LDLP，LDOLP 位可以进入低驱动模式。低驱动模式具有低驱动能力，低功耗模式工作能耗很低。

正常驱动/正常功耗：将 PMU_CTL0 寄存器的 LDEN 位配置为 00，深度睡眠模式就工作在正常驱动模式下。将 PMU_CTL0 寄存器的 LDOLP 清 0 可以退出低功耗模式。

正常驱动/低功耗：将 PMU_CTL0 寄存器的 LDEN 位配置为 00，深度睡眠模式就工作在正常驱动模式下。将 PMU_CTL0 寄存器的 LDOLP 置 1 可以进入低功耗模式。

低驱动/正常功耗：将 PMU_CTL0 寄存器的 LDEN 设置为 0b11，LDNP 置 1 可以进入深度睡眠模式的低驱动模式。将 PMU_CTL0 寄存器的 LDOLP 清 0 可以使 LDO 处于正常功耗模式。

低驱动/低功耗：将 PMU_CTL0 寄存器的 LDEN 设置为 0b11，LDLP 置 1 可以进入深度睡眠模式的低驱动模式。将 PMU_CTL0 寄存器的 LDOLP 置 1 可以使 LDO 处于低功耗模式。

非低驱动：将 PMU_CTL0 寄存器的 LDEN 设置为 00，深度睡眠模式将不会处在低驱动模式。

注意：为了顺利进入深度睡眠模式，所有 EXTI 线上的挂起状态（在 EXTI_PD 寄存器中）和和相关外设标志位必须被复位，参考 7-3. EXTI 。否则，程序将直接跳过深度睡眠模式进入过程而继续执行下面的程序。

## 深度睡眠模式 1

深度睡眠模式 1 与 Cortex®-M33 的 SLEEPDEEP 模式相对应。在深度睡眠模式 1 下，V域中的所有时钟全部关闭，IRC8M、IRC48M、HXTAL 及 PLLs 也全部被禁用。COREOFF1域停止供电。COREOFF1 域寄存器中的内容全部丢失。根据 PMU_CTL0 寄存器的 LDOLP 位的配置，可控制 LDO 工作在正常模式或低功耗模式。进入深度睡眠模式 1 之前，先将 Cortex®-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再清除 PMU_CTL0 寄存器的 STBMOD 位，再置位 PMU_CTL1 寄存器的 DPMOD1 位，然后执行 WFI 或 WFE 指令即可进入深度睡眠模式1。如果睡眠模式是通过执行 WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式 1 中唤醒。如果睡眠模式是通过执行 WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式 1 中唤醒（如果 SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。刚退出深度睡眠模式 1 时，IRC8M 被选中作为系统时钟。从深度睡眠模式 1 唤醒需要额外的延时时间用于给 COREOFF1 域上电。请注意，如果LDO 工作在低功耗模式，那么唤醒时需额外的延时时间。

在深度睡眠模式 1 下，通过配置 PMU_CTL0 寄存器的 LDEN，LDNP，LDLP，LDOLP 位可以进入低驱动模式。低驱动模式具有低驱动能力，低功耗模式工作能耗很低。

## 深度睡眠模式 2

深度睡眠模式 2 与 Cortex®-M33 的 SLEEPDEEP 模式相对应。在深度睡眠模式 2 下，V<sub>CORE</sub>域中的所有时钟全部关闭，IRC8M、IRC48M、HXTAL 及 PLLs 也全部被禁用。COREOFF0 /COREOFF1 域停止供电。SRAM（除前 32K）和 COREOFF0/COREOFF1 域寄存器中的内容全部丢失。根据 PMU_CTL0 寄存器的 LDOLP 位的配置，可控制 LDO 工作在正常模式或低功耗模式。进入深度睡眠模式 2 之前，先将 Cortex®-M33 系统控制寄存器的 SLEEPDEEP 位置1，再清除 PMU_CTL0 寄存器的 STBMOD 位，再置位 PMU_CTL1 寄存器的 DPMOD2 位，然后执行 WFI 或 WFE 指令即可进入深度睡眠模式 2。如果睡眠模式是通过执行 WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式 2 中唤醒。如果睡眠模式是通过执行WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式 2 中唤醒（如果SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M33 技术手册）。刚退出深度睡眠模式 2 时，IRC8M 被选中作为系统时钟。从深度睡眠模式 2 唤醒需要额外的延时时间用于给 COREOFF0 / COREOFF1 域上电。请注意，如果 LDO 工作在低功耗模式，那么唤醒时需额外的延时时间。

在深度睡眠模式 2 下，通过配置 PMU_CTL0 寄存器的 LDEN，LDNP，LDLP，LDOLP 位可以进入低驱动模式。低驱动模式具有低驱动能力，低功耗模式工作能耗很低。

## 待机模式

待机模式是基于 Cortex®-M33 的 SLEEPDEEP 模式实现的。在待机模式下，整个 V 域全部停止供电，同时 LDO 和包括 IRC8M、IRC48M、HXTAL 和 PLL 也会被关闭。进入待机模式前，先将 Cortex<sup>®</sup>-M33 系统控制寄存器的 SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的STBMOD 位置 1，再清除 PMU_CS0 寄存器的 WUF 位，然后执行 WFI 或 WFE 指令，系统进入待机模式，PMU_CS0 寄存器的 STBF 位状态表示 MCU 是否已进入待机模式。待机模式有四个唤醒源，包括来自 NRST 引脚的外部复位，RTC 报警，FWDGT 复位，WKUP 引脚的上升沿。待机模式可以达到最低的功耗，但唤醒时间最长。另外，一旦进入待机模式，SRAM和 V<sub>CORE</sub>电源域寄存器的内容都会丢失。退出待机模式时，会发生上电复位，复位之后 Cortex®-M33 将从 0x00000000 地址开始执行指令代码。


表 4-1. 节电模式总结


<table><tr><td>模式</td><td>睡眠</td><td>深度睡眠</td><td>深度睡眠1</td><td>深度睡眠2</td><td>待机</td></tr><tr><td>描述</td><td>仅关闭CPU时钟</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC8M、IRC48M、HXTAL和PLL</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC8M、IRC48M、HXTAL和PLL3、关闭SHRTIMER、USBHS、TMU、ENET的供电</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC8M、IRC48M、HXTAL和PLL3、关闭CPU、SRAM(除前32K)、COREOFF0/COREOFF1域外设的供电</td><td>1、关闭VCORE电源域的供电2、关闭IRC8M、IRC48M、HXTAL和PLL</td></tr><tr><td>LDO状态</td><td>开启(正常功耗模式)</td><td>开启(正常功耗模式或者低功耗模式,正常驱动或者低驱动模式)</td><td>开启(正常功耗模式或者低功耗模式,正常驱动或者低驱动模式)</td><td>开启(正常功耗模式或者低功耗模式,正常驱动或者低驱动模式)</td><td>关闭</td></tr><tr><td>配置</td><td>SLEEPDEEP=0</td><td>SLEEPDEEP=1STBMOD=0</td><td>SLEEPDEEP=1STBMOD=0DPMOD1=1</td><td>SLEEPDEEP=1STBMOD=0DPMOD2=1</td><td>SLEEPDEEP=1STBMOD=1,WURST=1</td></tr><tr><td>进入指令</td><td>WFI或WFE</td><td>WFI或WFE</td><td>WFI或WFE</td><td>WFI或WFE</td><td>WFI或WFE</td></tr><tr><td>唤醒</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>1、NRST引脚2、WKUP引脚3、FWDGT复位4、RTC</td></tr><tr><td>唤醒延迟</td><td>无</td><td>IRC8M唤醒时间如果LDO处于低功耗模式,需增加LDO唤醒时间</td><td>IRC8M唤醒时间COREOFF1域上电时间如果LDO处于低功耗模式,需增加LDO唤醒时间</td><td>IRC8M唤醒时间COREOFF0/COREOFF1域上电时间如果LDO处于低功耗模式,需增加LDO唤醒时间</td><td>上电序列</td></tr></table>


注意：在待机模式下，除了 RESET 引脚，配置为 RTC 功能的 PC13，用作 LXTAL 晶振引脚的 PC14 和 PC15，使能的 WKUP 引脚，其他所有 I / O 都处于高阻态。

