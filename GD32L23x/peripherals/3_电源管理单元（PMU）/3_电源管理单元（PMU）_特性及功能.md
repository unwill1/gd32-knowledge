## 3. 电源管理单元（PMU）

## 3.1. 简介

功耗设计是 GD32L23x 系列产品比较注重的问题之一。对于 GD32L233xx，电源管理单元提供了十种省电模式，包括运行模式，运行模式 1，运行模式 2，睡眠模式，睡眠模式 1，睡眠模式 2，深度睡眠模式，深度睡眠模式 1，深度睡眠模式 2 和待机模式。对于 GD32L235xx，电源管理单元提供了六种省电模式，包括运行模式，睡眠模式，深度睡眠模式，深度睡眠模式 1，深度睡眠模式 2 和待机模式。这些模式能减少电源能耗，且使得应用程序可以在 CPU 运行时间要求、速度和功耗的相互冲突中获得最佳折衷。如 3-1. GD32L233xx 和 3-2.GD32L235xx 所示，GD32L23x 系列设备有三个电源域，包括 V<sub>DD</sub> / V<sub>DDA</sub> 域，V<sub>CORE</sub>域和备份域。V /V 域由电源直接供电。在 V /V 域中嵌入了一个 LDO，用来为 V域供电。在备份域中有一个电源切换器，当 V 电源关闭时，电源切换器可以将备份域的电源切换到 VBAT 引脚，此时备份域由 VBAT 引脚（电池）供电。

## 3.2. 主要特征

◼ 三个电源域：备份域、V<sub>DD</sub> / V<sub>DDA</sub>域和V<sub>CORE</sub>电源域。

◼ 提供低电压检测器，当电压低于所设定的阈值时能发出中断或事件。

◼ 当V<sub>DD</sub>供电关闭时，由VBAT（电池）为备份域供电。

◼ LDO输出电压用于节约能耗。

◼ 低驱动模式用于在深入睡眠模式 / 深度睡眠模式1 / 深度睡眠模式2下超低功耗。

◼ SRAM1可单独断电。

◼ CPU可以在COREOFF0关闭时保留其寄存器的值，使MCU在唤醒时可以继续执行指令，而无需重新加载程序。

对于GD32L233xx产品：

◼ 内部电压调节器（LDO）为V 电源域提供V 电源。

◼ 十种模式：运行模式、运行模式1、运行模式2、睡眠模式、睡眠模式1、睡眠模式2、深度睡眠模式、深度睡眠模式1、深度睡眠模式2和待机模式。

◼ CAU可单独断电。

对于GD32L235xx产品：

◼ 内部电压调节器（LDO）为V 电源域提供V 电源。

六种模式：运行模式、睡眠模式、深度睡眠模式、深度睡眠模式1、深度睡眠模式2和待机模式。

厂 在深度睡眠模式1和深度睡眠模式2下，低功耗内部电压调节器（LPLDO）为V<sub>CORE</sub>电源域提供V<sub>CORE</sub>电源。

◼ 深度睡眠模式下，EFLASH可单独掉电。

## 3.3. 功能说明

3-1. GD32L233xx 和 3-2. GD32L235xx 提供了 及相关电源域的内部结构框图。


图3-1. GD32L233xx电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/e7c01679fb9a3176715f3817d0687ef9b4dbc4628a217f3235a98762239c4167.jpg)


注意：对于版本E及以后的GD32L233xx器件，POR/PDR和BOR电路在VDD域中实现，用于检测VDD并生成电源重置信号，当供应电压低于指定阈值时，该信号会重置整个芯片。


图3-2. GD32L235xx电源域概览


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/7fb83f36251a68099ec466e168a9886b96106628d0044fb728086e2c091d4a20.jpg)


## 3.3.1. 电池备份域

电池备份域由内部电源切换器来选择 VDD 供电或 VBAT（电池）供电，然后由 V 为备份域供电，该备份域包含 RTC（实时时钟）、LXTAL（低速外部晶体振荡器）和 BPOR（备份域上电复位），以及 PC13 至 PC15 共 3 个 PAD。为了确保备份域中寄存器的内容及 RTC 正常工作，当 V 关闭时，VBAT 引脚可以连接至电池或其他备份电源供电。电源切换器是由 V /V 域掉电复位电路控制的。对于没有外部电池的应用，建议将 VBAT 引脚通过 100nF 的外部陶瓷去耦电容连接到 VDD 引脚上。

备份域的复位源包括备份域上电复位和备份域软件复位。在 V 没有完全上电前，BPOR 信号强制设备处于复位状态。应用软件可以通过设置 RCU_BDCTL 寄存器 BKPRST 位来触发备份域软件复位。

的时钟源可以是低速内部 振荡器（ ）或低速外部晶体振荡器（ ），或高速外部晶体振荡器（HXTAL）时钟32分频。当V 被关闭时，RTC只能选择LXTAL作为时钟源。在通过WFI / WFE指令进入省电模式之前，Cortex®-M23需要通过RTC寄存器预期的唤醒时间并启用唤醒功能，以实现RTC定时器唤醒事件。进入省电模式一定时间之后，当经过的时间与预设的唤醒时间匹配时，RTC将唤醒设备。RTC的配置和操作的细节将在 RTC来描述。

当备份域由V<sub>DD</sub>供电（V<sub>BAK</sub>连接至V<sub>DD</sub>）时，以下功能可用：

◼ PC13可以作为通用I/O口或RTC功能引脚（参见 RTC ）；

◼ PC14和PC15可以作为通用I/O口或LXTAL晶振引脚。

当备份域由VBAT电源供电时（V<sub>BAK</sub>连接至VBAT），以下功能可用：

PC13仅可以作为RTC功能引脚（参见 RTC ）；

◼ PC14和PC15仅可作为LXTAL晶振引脚。

注意：由于 PC13 至 PC15 引脚是通过电源切换器供电的，电源切换器仅可通过小电流，因此当PC13至PC15的GPIO口在输出模式时，其工作的速度不能超过2MHz(最大负载为30pF)。

V<sub>DD</sub>可以通过一个内部电阻给外部电池充电。通过配置 PMU_CTL0 寄存器中 VCRSEL 位，可以选择内部电阻 5K 欧姆或 1.5K 欧姆用于外部 VBAT 电池充电。将 PMU_CTL0 寄存器中VCEN 位置 1 可以使能 VBAT 电池充电。在 BKP_ONLY 模式，VBAT 电池充电不可用。

注意：在 BKP_ONLY 模式下，V<sub>DD</sub>掉电，备份域由 VBAT 引脚供电。

## 3.3.2. V<sub>DD</sub> / V<sub>DDA</sub> 电源域

V<sub>DD</sub> / V<sub>DDA</sub> 域包括 V<sub>DD</sub> 域和 V<sub>DDA</sub> 域两部分。

V 域包括 FWDGT（独立看门狗定时器）、HXTAL（高速外部晶体振荡器）、IRC16M（内部16MHz RC 振荡器）、IRC48M（内部 48M RC 振荡器）、PLL（锁相环）、NPLDO（正常功耗电压调节器）和除 PC13、PC14和 PC15 之外的所有 PAD 等等。

V<sub>DDA</sub>域包括 IRC32K（内部 32KHz RC 振荡器）、ADC / DAC（AD / DA 转换器）、POR / PDR（上电 / 掉电复位）、BOR（欠压复位）、LPLDO（低功耗电压调节器）和 LVD（低电压检测器）等等。

## V<sub>DD</sub> 域

为 V 域供电的 LDO（电压调节器），其复位后保持使能。可以被配置为不同的工作状态：包括睡眠模式（1.1V 全供电状态、0.9V 全供电状态和低功耗状态）、深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2（全供电或低功耗状态）和待机模式（关闭状态）。

## V<sub>DDA</sub> 域

POR/ PDR（上电 / 掉电复位）电路检测 V 并在电压低于特定阈值时产生电源复位信号复位除备份域之外的整个芯片。 3-3. BOR0 显示了供电电压和电源复位信号之间的关系。V 表示 BOR0 复位的阈值电压。迟滞电压 $\vee _ { \mathsf { h y s t } }$ 值和复位延时 t 参考数据手册。


图3-3. BOR0波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/1bde550217d2e6de6d4cb78886dd785a5499dd2562490d34dd9ab9f8307e7034.jpg)


BOR 电路检测 V 并在电压低于选项字节的 BOR_TH 定义的阈值时产生电源复位信号复位除备份域之外的整个芯片。注意 BOR0 电路总是处于检测状态。 3-4. BOR 显示了供电电压和 BOR 复位信号之间的关系。V 表示 BOR 复位的阈值电压，该值在选项字节BOR_TH 中定义。迟滞电压 $\mathsf { V } _ { \mathsf { h y s t } }$ 值参考数据手册。


图3-4. BOR波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/f51d78868538cb2b8ca5d01ba59b69e74c07d5a23e3c3bd16dd4c95a2d2cb521.jpg)



注意：对于版本E及以后的GD32L233xx器件，POR/PDR和BOR电路在VDD域中实现，用于检测VDD并生成电源重置信号，当供应电压低于指定阈值时，该信号会重置整个芯片。


LVD 的功能是检测 V 供电电压是否低于低电压检测阈值，该阈值由电源控制寄存器 0（PMU_CTL0）中的 LVDT[2:0]位进行配置。LVD 通过 LVDEN 置位使能，位于电源控制状态寄存器（PMU_CS）中的 LVDF 位表示低电压事件是否出现，该事件连接至 EXTI 的第 16 线，用户可以通过配置 EXTI 的第 16 线产生相应的中断。 3-5. LVD 显示了 V<sub>DDA</sub>供电电压和 LVD 输出信号的关系。（LVD 中断信号依赖于 EXTI 第 16 线的上升或下降沿配置）。迟滞电压 $\Vdash _ { \tt V S t }$ 值参考数据手册。

注意：当 LVDT[2:0]位配置为“111”时，PB7 引脚上的输入电压与 0.8V 进行比较，LVDF 位

表示输入电压高于或低于 0.8V。


图 3-5. LVD 阈值波形图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/3b0daffad79d19ae545a05c517948955a7311afdf8cbb6cf67e44ff1ef1c3f23.jpg)


一般来说，数字电路由 V 供电，而大多数的模拟电路由 V 供电。为了提高 ADC 和 DAC的转换精度，为 V<sub>DDA</sub>独立供电可使模拟电路达到更好的特性。为避免噪声，V<sub>DDA</sub>通过外部滤波电路连接至 V<sub>DD</sub>，相应的 V<sub>SSA</sub>通过特定电路连接至 V<sub>SS</sub>。否则，当 V<sub>DD</sub>和 V<sub>DDA</sub>不是同一个电源提供时，在上电和运行过程中 V<sub>DD</sub>与 V<sub>DDA</sub>差值不超过 0.3V。

为提高 ADC 和 DAC 的精度，可将独立的外部参考电压连接至 ADC / DAC 引脚 VREFP。根据不同的封装，VREFP 可被连接至 VDDA 引脚，或者外部参考电压。

## 3.3.3. V<sub>CORE</sub> 电源域

主要功能包括 Cortex<sup>®</sup>-M23 内核逻辑、AHB / APB 外设、备份域和 V / V 域的 APB 接口等。当 V 电压上电后，POR 将在 V 域中产生一个复位序列，复位完成后，如果要进入指定的省电模式，须先配置相关的控制位，之后一旦执行 WFI 或 WFE指令，设备便进入该省电模式。详细内容将在以下章节予以说明。V<sub>CORE</sub>电压值请参考数据手册。

## SRAM1 电源域

SRAM1（对于 GD32L233xx 产品，0x20004000~0x20007FFF。对于 GD32L235xx 产品，0x20002000~0x20005FFF）可独立断电。SRAM1 在系统复位后默认是上电的。为了降低GD32L233xx 产品运行模式 / 运行模式 1 / 运行模式 2 的功耗和 GD32L235xx 产品运行模式的功耗，可以将 SRAM1 断电。为了进一步降低低功耗模式（对于 GD32L233xx 产品，睡眠模式 / 睡眠模式 1 / 睡眠模式 2 / 深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2，对于GD32L235xx 产品，睡眠模式 / 深度睡眠模式 / 深度睡眠模式 1/ 深度睡眠模式 2）的功耗，在进入低功耗模式之前可以将 SRAM1 断电。

## COREOFF1 电源域（对于 GD32L233xx 产品）

COREOFF1 域可单独断电。COREOFF1 域在系统复位后默认是断电的。在使用 COREOFF1域中模块时需要将 COREOFF1 域上电。为了降低运行模式 / 运行模式 1 / 运行模式 2 的功耗，可以将 COREOFF1 域断电。为了进一步降低低功耗模式（睡眠模式 / 睡眠模式 1/ 睡眠模式 2 / 深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2）的功耗，在进入低功耗模式之前可以将 COREOFF1 域断电。

COREOFF1 电源域包含 CAU 模块。

## EFLASH 电源域（对于 GD32L235xx 产品）

EFLASH 可单独断电。EFLASH 在系统复位后默认是上电的。内核电压可以从 1.1V 切换到0.9V 甚至更低电压，由于 EFLASH 无法正常工作，需要在 PMU_CTL1 寄存器中将 EFPSLEEP位置 1 来关闭 EFLASH。当 MCU 进入深度睡眠模式时，通过在 PMU_CTL1 寄存器中将EFDSPSLEEP 位置 1 来关闭 EFLASH。

当LDO电压为1.1V时，EFLASH电源域才能正常工作。在这种情况下，代码应该存储在SRAM中。

## COREOFF0 电源域

在进入深度睡眠模式 2 时，COREOFF0 电源域断电，在退出深度睡眠模式 2 时，COREOFF0电源域上电。

COREOFF0 电源域包含以下模块：

CPU / BUS / ADC / CMP / CRC / CTC / DAC / DMA / I2C0 / I2C1 / SLCD / TRNG / SPI0/ SPI1/ TIMER1 / TIMER2 / TIMER5 / TIMER6 / TIMER8 / TIMER11 / USART0 / USART1 / UART3/ UART4 / USBD。对于 GD32L235xx 产品，COREOFF0 电源域还包含 TIMER0 / TIMER14 /TIMER40 / CAU。

注意：对于 GD32L233xx 产品，可以通过配置 PMU_CTL1 寄存器中 NRRD2 位来选择在进入/ 退出深度睡眠模式 2 时 CPU 寄存器的值是否保留。

## 3.3.4. 省电模式

系统复位或电源复位后，GD32L23x MCU 处于全功能状态且电源域全部处于供电状态。实现较低的功耗的方法有三种：减慢系统时钟（ ， 和 ），关闭未使用的外设的时钟。此外，对于 GD32L233xx 产品，十种省电模式可以实现更低的功耗，它们是运行模式，运行模式 1，运行模式 2，睡眠模式，睡眠模式 1，睡眠模式 2，深度睡眠模式，深度睡眠模式1，深度睡眠模式 2 和待机模式。对于 GD32L235xx 产品，六种省电模式可以实现更低的功耗，它们是运行模式，睡眠模式，深度睡眠模式，深度睡眠模式 1，深度睡眠模式 2 和待机模式。

## 运行模式

在系统复位、上电复位或从待机模式唤醒产生复位后，MCU 进入运行模式，NPLDO（正常功耗 LDO）工作在 1.1V模式。

## 运行模式 1

在运行模式1下，NPLDO必须通过配置PMU_CTL0寄存器中的LDOVS位来选择工作在0.9V模式。在该模式下，系统时钟频率不可以超过 16MHz。

注意：运行模式 1 仅存在与 GD32L233xx 产品。

## 运行模式 2

在运行模式2下，NPLDO必须通过配置PMU_CTL0寄存器中的LDOVS位来选择工作在0.9V模式，同时必须通过配置 PMU_CTL0 寄存器中的 LDNP 位来选择低驱动模式。在该模式下，系统时钟频率不可以超过 16MHz 且 AHB时钟频率不可以超过 2MHz。

注意：运行模式 2 仅存在与 GD32L233xx 产品。

## 睡眠模式

睡眠模式与 Cortex<sup>®</sup>-M23 的 SLEEPING 模式相对应。在睡眠模式下，仅关闭 Cortex<sup>®</sup>-M23 的时钟。如需进入睡眠模式，只要清除 Cortex®-M23 系统控制寄存器中的 SLEEPDEEP 位，并执行一条 WFI 或 WFE 指令即可。如果睡眠模式是通过执行 WFI 指令进入的，任何中断都可以唤醒系统。如果睡眠模式是通过执行 WFE 指令进入的，任何唤醒事件都可以唤醒系统（如果 SEVONPEND 为 1，任何中断都可以唤醒系统，请参考 Cortex®-M23 技术手册）。由于无需在进入或退出中断上消耗时间，该模式所需的唤醒时间最短。

根据 Cortex®-M23 中 SCR（系统控制寄存器）的 SLEEPONEXIT 位，有两种睡眠进入机制可选：

■ Sleep-now：如果SLEEPONEXIT位被清零，一旦执行WFI或WFE指令，MCU立即进入睡眠模式；

◼ Sleep-on-exit：如果SLEEPONEXIT位被置位，当系统从最低优先级的中断处理程序离开后，MCU立即进入睡眠模式。

## 睡眠模式 1

睡眠模式 1 对应于运行模式 1 的 Cortex<sup>®</sup>-M23 的 SLEEPING 模式。NPLDO 必须通过配置PMU_CTL0 寄存器中的 LDOVS 位来选择工作在 0.9V。

注意：睡眠模式 1 仅存在与 GD32L233xx 产品。

## 睡眠模式 2

睡眠模式 2 对应于运行模式 2 的 Cortex<sup>®</sup>-M23 的 SLEEPING 模式。NPLDO 必须通过配置PMU_CTL0 寄存器中的 LDOVS 位来选择工作在 0.9V。同时必须通过配置 PMU_CTL0 寄存器中的 LDNP 位来选择低驱动模式。

注意：睡眠模式 2 仅存在与 GD32L233xx 产品。

## 深度睡眠模式

深度睡眠模式与 Cortex®-M23 的 SLEEPDEEP 模式相对应。在深度睡眠模式下，V<sub>CORE</sub>域中的所有时钟全部关闭，IRC16M、IRC48M、HXTAL 及 PLLs 也全部被禁用。SRAM 和寄存器中的内容被保留。根据 PMU_CTL0 寄存器的 LDNPDSP位的配置，可控制 NPLDO 工作在正常模式或低功耗模式。进入深度睡眠模式之前，先将 Cortex®-M23 系统控制寄存器的SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的 LPMOD 位域配置为“00”，然后执行 WFI或 WFE 指令即可进入深度睡眠模式。如果睡眠模式是通过执行 WFI 指令进入的，任何来自

EXTI 的中断可以将系统从深度睡眠模式中唤醒。如果睡眠模式是通过执行 WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式中唤醒（如果 SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M23 技术手册）。刚退出深度睡眠模式时，IRC16M 被选中作为系统时钟。请注意，如果 LDO 工作在低驱动模式，那么唤醒时需额外的延时时间。

注意：为了顺利进入深度睡眠模式，所有 EXTI 线上的挂起状态（在 EXTI_PD 寄存器中）和相关外设标志位必须被复位，参考 6-4. GD32L233xx EXTI 。否则，程序将直接跳过深度睡眠模式进入过程而继续执行下面的程序。

## 深度睡眠模式 1

深度睡眠模式 1 与 Cortex®-M23 的 SLEEPDEEP 模式相对应。在深度睡眠模式 1 下，V<sub>CORE</sub>域中的所有时钟全部关闭，IRC16M、IRC48M、HXTAL 及 PLLs 也全部被禁用。LPLDO（低功耗 LDO）可以替代 NPLDO 正常工作。进入深度睡眠模式 1 之前，先将 Cortex®-M23 系统控制寄存器的 SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的 LPMOD 位域配置为“01”,然后执行 WFI 或 WFE 指令即可进入深度睡眠模式 1。如果睡眠模式是通过执行 WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式 1 中唤醒。如果睡眠模式是通过执行WFE 指令进入的，任何来自 EXTI 的事件可以将系统从深度睡眠模式 1 中唤醒（如果SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M23 技术手册）。刚退出深度睡眠模式 1 时，IRC16M 被选中作为系统时钟。从深度睡眠模式 1 中唤醒需要额外的延迟来唤醒 NPLDO。

注意：如果上电或者从待机模式唤醒，在进入深度睡眠模式 1 之前需要等待至少 600us。

## 深度睡眠模式 2

深度睡眠模式 2 与 Cortex®-M23 的 SLEEPDEEP 模式相对应。在深度睡眠模式 2 下，V<sub>CORE</sub>域中的所有时钟全部关闭，IRC16M、IRC48M、HXTAL 及 PLLs 也全部被禁用。对于GD32L233xx 产品，COREOFF0 / SRAM1 / COREOFF1 域停止供电。COREOFF0 / SRAM1/ COREOFF1 域寄存器中的内容全部丢失。对于 GD32L235xx 产品，COREOFF0 / SRAM1域停止供电。COREOFF0 / SRAM1 域寄存器中的内容全部丢失。LPLDO 可以替代 NPLDO正常工作。进入深度睡眠模式 2 之前，先将 Cortex®-M23 系统控制寄存器的 SLEEPDEEP 位置 1，再将 PMU_CTL0 寄存器的 LPMOD 位域配置为“10”，然后执行 WFI 或 WFE 指令即可进入深度睡眠模式 2。如果睡眠模式是通过执行 WFI 指令进入的，任何来自 EXTI 的中断可以将系统从深度睡眠模式 2 中唤醒。如果睡眠模式是通过执行 WFE指令进入的，任何来自 EXTI的事件可以将系统从深度睡眠模式 2 中唤醒（如果 SEVONPEND 为 1，任何来自 EXTI 的中断都可以唤醒系统，请参考 Cortex®-M23 技术手册）。刚退出深度睡眠模式 2 时，IRC16M 被选中作为系统时钟。从深度睡眠模式 2 中唤醒需要额外的延迟来唤醒 NPLDO。

注意：如果上电或者从待机模式唤醒，在进入深度睡眠模式 2 之前需要等待至少 600us。

## 待机模式

待机模式是基于 Cortex®-M23 的 SLEEPDEEP 模式实现的。在待机模式下，整个 V 域全部停止供电，NPLDO / LPLDO 关闭，同时包括 IRC16M、IRC48M、HXTAL 和 PLLs 也会被关闭。进入待机模式前，先将 PMU_CTL0 寄存器的 LPMOD 位域配置为“11”，再清除 PMU_CS寄存器的 WUF 位，再将 Cortex<sup>®</sup>-M23 系统控制寄存器的 SLEEPDEEP 位置 1，然后执行 WF或 WFE 指令，系统进入待机模式，PMU_CS 寄存器的 STBF 位状态表示 MCU 是否已进入待机模式。待机模式有四个唤醒源，包括来自 NRST 引脚的外部复位，RTC 闹钟 / 时间戳 / 侵入 / 自动唤醒事件，FWDGT 复位，WKUP 引脚的上升沿。待机模式可以达到最低的功耗，但唤醒时间最长。另外，一旦进入待机模式，SRAM 和 V<sub>CORE</sub>电源域寄存器的内容都会丢失。退出待机模式时，会发生上电复位，复位之后 Cortex®-M23 将从 0x00000000 地址开始执行指令代码。


表3-1. 节电模式总结（GD32L233xx产品）


<table><tr><td>模式</td><td>描述</td><td>LDO状态</td><td>进入指令</td><td>唤醒</td><td>唤醒后模式</td><td>唤醒延时</td></tr><tr><td>运行</td><td>对所有时钟无影响,全部开启</td><td>NPLDO开启LPLDO开启</td><td>系统/上电复位或从待机模式唤醒</td><td>-</td><td>-</td><td>-</td></tr><tr><td>运行1</td><td>系统时钟&lt;=16Mhz</td><td>NPLDO开启LPLDO开启</td><td>LDOVS配置为0.9V</td><td>清除LDVOS</td><td>-</td><td>-</td></tr><tr><td>运行2</td><td>系统时钟&lt;=2Mhz</td><td>NPLDO工作在低驱动模式LPLDO开启</td><td>LDOVS配置为0.9V且LDNP置1</td><td>清除LDVOS和LDNP</td><td>-</td><td>-</td></tr><tr><td>睡眠</td><td>仅关闭CPU时钟</td><td>NPLDO开启LPLDO开启</td><td>SLEEPDEEP=0,在运行模式下执行WFI或WFE</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>运行模式</td><td>-</td></tr><tr><td>睡眠1</td><td>仅关闭CPU时钟</td><td>NPLDO开启LPLDO开启</td><td>SLEEPDEEP=0,在运行模式1下执行WFI或WFE</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>运行模式1</td><td>-</td></tr><tr><td>睡眠2</td><td>仅关闭CPU时钟</td><td>NPLDO工作在低驱动模式LPLDO开启</td><td>SLEEPDEEP=0,在运行模式2下执行WFI或WFE</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>运行模式2</td><td>-</td></tr><tr><td>深度睡眠</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs</td><td>NPLDO工作在低驱动模式或正常驱动模式LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=00,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式/运行模式1/运行模式2</td><td>IRC16M唤醒时间+Flash唤醒时间</td></tr><tr><td>深度睡眠1</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs3、LPLDO代替NPLDO</td><td>NPLDO关闭LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=01,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式/运行模式1/运行模式2</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>深度睡眠2</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs3、LPLDO代替NPLDO4、COREOFF0/SRAM1掉电5.对于GD32L233xx产品,COREOFF1掉电</td><td>NPLDO关闭LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=10,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式/运行模式1/运行模式2</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>待机</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs</td><td>NPLDO关闭LPLDO关闭</td><td>SLEEPDEEP=1,LPMOD=11,执行WFI或WFE</td><td>1、NRST引脚2、WKUP引脚3、FWDGT复位4、RTC闹钟</td><td>运行模式</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>BKP_ONLY</td><td>VDD域/VCORE域全部掉电</td><td>NPLDO关闭LPLDO关闭</td><td>VDD关闭</td><td>VDD开启</td><td>运行模式</td><td>VDD上电序列</td></tr></table>


表3-2. 节电模式总结（GD32L235xx产品）


<table><tr><td>模式</td><td>描述</td><td>LDO状态</td><td>进入指令</td><td>唤醒</td><td>唤醒后模式</td><td>唤醒延时</td></tr><tr><td>运行</td><td>对所有时钟无影响,全部开启</td><td>NPLDO开启LPLDO开启</td><td>系统/上电复位或从待机模式唤醒</td><td>-</td><td>-</td><td>-</td></tr><tr><td>睡眠</td><td>仅关闭CPU时钟</td><td>NPLDO开启</td><td>SLEEPDEEP=0,在运行模式下执行WFI或WFE</td><td>若通过WFI进入,则任何中断均可唤醒;若通过WFE进入,则任何事件(或SEVONPEND=1时的中断)均可唤醒</td><td>运行模式</td><td>-</td></tr><tr><td>深度睡眠</td><td>1、关闭VCORE电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs</td><td>NPLDO工作在低驱动模式或正常驱动模式LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=00,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式</td><td>IRC16M唤醒时间+Flash唤醒时间</td></tr><tr><td>深度睡眠1</td><td>1、关闭<eq>V_{CORE}</eq>电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs3、LPLDO代替NPLDO</td><td>NPLDO关闭LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=01,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>深度睡眠2</td><td>1、关闭<eq>V_{CORE}</eq>电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs3、LPLDO代替NPLDO4、COREOFF0/SRAM1掉电5.对于GD32L233xx产品,COREOFF1掉电</td><td>NPLDO关闭LPLDO开启</td><td>SLEEPDEEP=1,LPMOD=10,执行WFI或WFE</td><td>若通过WFI进入,来自EXTI的任何中断可唤醒;若通过WFE进入,来自EXTI的任何事件(或SEVONPEND=1时的中断)可唤醒</td><td>运行模式</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>待机</td><td>1、关闭<eq>V_{CORE}</eq>电源域的所有时钟2、关闭IRC16M、IRC48M、HXTAL和PLLs</td><td>NPLDO关闭LPLDO关闭</td><td>SLEEPDEEP=1,LPMOD=11,执行WFI或WFE</td><td>1、NRST引脚2、WKUP引脚3、FWDGT复位4、RTC闹钟</td><td>运行模式</td><td>IRC16M唤醒时间+NPLDO唤醒时间+Flash唤醒时间</td></tr><tr><td>BKP_ONLY</td><td><eq>V_{DD}</eq>域/<eq>V_{CORE}</eq>域全部掉电</td><td>NPLDO关闭LPLDO关闭</td><td><eq>V_{DD}</eq>关闭</td><td><eq>V_{DD}</eq>开启</td><td>运行模式</td><td><eq>V_{DD}</eq>上电序列</td></tr></table>


注意：



1、 在待机模式下，除了 NRST 引脚，配置为 RTC 功能的 PC13，用作 LXTAL 晶振引脚的PC14和 PC15，使能的 WKUPx 引脚，其他所有 I/O 都处于高阻态。

