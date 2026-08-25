## 13. 实时时钟（RTC）

## 13.1. 简介

RTC 模块提供了一个包含日期（年/月/日）和时间（时/分/秒/亚秒）的日历功能。除亚秒用二进制码显示外，时间和日期都以 BCD 码的形式显示。RTC 可以进行夏令时补偿。RTC 可以工作在省电模式下。RTC 支持外接更高精度的低频时钟，用以达到更高的日历精度。

## 13.2. 主要特征

◼ 通过软件设置来实现夏令时补偿。

◼ 参考时钟检测功能：通过外接更高精度的低频率时钟源（50Hz或60Hz）来提高日历精度。

◼ 数字校准功能：通过调整最小时间单位（最大可调精度0.95ppm）来进行日历校准。

◼ 通过移位功能进行亚秒级调整。

◼ 记录事件时间的时间戳功能。

◼ 可编程的日历和一个位域可屏蔽的闹钟。

◼ 可屏蔽的中断源：

闹钟 0；

时间戳检测；

◼ 4个16位（共16字节）通用备份寄存器，能够在省电模式下保存数据。

## 13.3. 功能描述


图 13-1. RTC 结构框图


![image](images/9d365fcb4ca6.jpg)


RTC 单元包括：

◼ 闹钟事件/中断。

◼ 可选的RTC输出功能：

512Hz（默认预分频值）：RTC_OUT0(PC13：48 引脚封装 / PA4：20/28/32 引脚封

装) 或 RTC_OUT1(PA4)；

1Hz（默认预分频值）：RTC_OUT0(PC13：48 引脚封装 / PA4：20/28/32 引脚封装)或 RTC_OUT1(PA4)；

闹钟事件（极性可配置）：RTC_OUT0(PC13：48 引脚封装 / PA4：20/28/32 引脚封装) 或 RTC_OUT1(PA4)；

◼ 可选的RTC输入功能：

时间戳事件检测：RTC_TS（PC13：48 引脚封装 / PA4：20/28/32 引脚封装）；

- 参考时钟输入：RTC_REFIN（PB15/PB7）；

## 13.3.1. 时钟源和预分频

RTC 单元有三个可选的独立时钟源：LXTAL、IRC32K 和 HXTAL 的 32（由 RCU_CTL1 寄存器配置）分频后的时钟。

在 RTC 单元，有两个预分频器用来实现日历功能和其他功能。一个分频器是 7 位异步预分频器，另一个是 15 位同步预分频器。异步分频器主要用来降低功率消耗。如果两个分频器都被使用，建议异步分频器的值尽可能大。

两个预分频器的频率计算公式如下：

$$
\mathsf {f} _ {\mathsf {c k \_ a p r e}} = \frac {\mathsf {f} _ {\mathsf {r t c c l k}}}{\mathsf {F A C T O R \_ A + 1}}\tag{13-1}
$$

$$
f _ {c k \_ s p r e} = \frac {f _ {c k \_ a p r e}}{\text { FACTOR } _ {S} + 1} = \frac {f _ {\text { rtcclk }}}{(\text { FACTOR } _ {A} + 1) ^ {*} (\text { FACTOR } _ {S} + 1)}\tag{13-2}
$$

ck_apre 用于为 RTC_SS 亚秒寄存器自减计数器提供时钟，该寄存器值为二进制，表示到达下一秒时间，该寄存器自减到 0 时，自动加载 FACTOR_S 的值。Ck_spre 用于为日历寄存器提供时钟，每个时钟增加一秒。

## 13.3.2. 影子寄存器

当APB总线访问RTC日历寄存器RTC_DATE、RTC_TIME和RTC_SS时，BPSHAD位决定是访问影子寄存器还是真实日历寄存器。默认情况下BPSHAD为0，APB总线访问影子日历寄存器。每两个RTC时钟，影子日历寄存器值会更新为真实日历寄存器的值，与此同时RSYNF位也会再次置位。在Deep-sleep和Standby模式下，影子寄存器不会更新。退出这两种模式时，软件必须清除RSYNF位。如果想要在BPSHAD=0的情况下读日历寄存器的值，须等待RSYNF置（最大的等待时间是2个RTC时钟周期）。

注意：在BPSHAD=0下，读日历寄存器（RTC_SS，RTC_TIME，RTC_DATE）的APB时钟的频率 $( \mathsf { f } _ { \mathsf { a p b } } )$ ）必须至少是RTC时钟频率 $\scriptstyle ( \mathsf { f } _ { \mathsf { r t c c l k } } )$ 的七倍。

系统复位将复位影子寄存器。

## 13.3.3. 位域可屏蔽可配置的闹钟

RTC闹钟功能被划分为多个位域并且每一个位域有一个该域的可屏蔽位。

RTC闹钟功能的使能由RTC_CTL寄存器中的ALRMxEN（x=0）位控制。当 $A L R M x E N = 1 ( x = 0 )$ 

并且闹钟所有位域的值与对应的日历时间值匹配，ALRMxF（x=0）标志位将会置位。

注意：当秒字段未被屏蔽时（RTC_ALRMxTD 寄存器的 MSKS=0），为确保正常运行，RTC_PSC寄存器的同步预分频系数（FACTOR_S）应大于等于 3。

如果一个位域被屏蔽，这个位域被认为在逻辑上匹配的。如果所有的位域被屏蔽，在 ALRMxEN位被置位 3 个 RTC 时钟周期后，ALRMxF 位将置位。

## 13.3.4. RTC初始化和配置

## RTC寄存器写保护

在默认情况下，PMU_CTL0寄存器的BKPWEN位被清0。所以写RTC寄存器前需要软件提前设置BKPWEN位。

上电复位后，大多数RTC寄存器是被写保护的。写入这些寄存器的第一步是解锁这些保护。

通过下面的步骤，可以解锁这些保护：

1. 写‘0xCA’到RTC_WPK寄存器；

2. 写‘0x53’到RTC_WPK寄存器。

写一个错误的值到RTC_WPK会使写保护再次生效。

备份寄存器复位后，一些RTC寄存器被写保护：RTC_TIME，RTC_DATE，RTC_CTL，RTC_STAT，RTC_PSC，RTC_ALRM0TD，RTC_HRFC，RTC_SHIFTCTL，RTC_ALRM0SS。

## 日历初始化和配置

通过以下步骤可以设置日历和预分频器的值：

1. 设置 INITM 位为 1 进入初始化模式。等待 INITF 位被置 1。

2. 在 RTC_PSC 寄存器中，设置同步和异步预分频器的分频系数。

3. 在影子寄存器（RTC_TIME 和 RTC_DATE）中写初始的日历值，并且通过设置 RTC_CTL寄存器的 CS位来配置时间的格式（12 或 24 小时制）。

4. 清除 INITM 位退出初始化模式。

大约4个RTC时钟周期后，真正的日历寄存器将从影子寄存器载入时间和日期的设定值，同时日历计数器将要重新开始运行。

注意：初始化以后如果要读取日历寄存器（BPSHAD=0），软件应该确保RSYNF位已经置1。

YCM标志表明日历是否完成初始化，该标志会硬件检查日历的年份值。

## 夏令时

通过S1H，A1H和DSM位配置，RTC模块可以支持夏令时补偿调节功能。

当日历正在运行时，S1H和A1H能使日历减去或加上1小时。S1H和A1H功能可以重复设置，可以软件配置DSM位来记录这个调节操作。设置S1H或A1H位后，减或加1小时将在下一秒钟到来时生效。

## 闹钟功能操作步骤

为了避免意外的闹钟标记置位和亚稳态，闹钟功能的操作应遵循如下流程：

1. 清除寄存器 RTC_CTL 的 ALRMxEN（x=0）位，禁用闹钟；

2. 设置 Alarm 寄存器（RTC_ALRMxTD/RTC_ALRMxSS（x=0））；

3. 设置寄存器 RTC_CTL 的 ALRMxEN（x=0）位，使能闹钟功能。

## 13.3.5. 读取日历

## 当 BPSHAD=0时，读日历寄存器

当BPSHAD=0，从影子寄存器读日历的值。由于同步机制的存在，正常读取日历需要满足一个基本要求：APB总线时钟频率必须大于或等于RTC时钟频率的7倍。在任何情况下APB总线时钟的频率都不能低于RTC的时钟频率。例如，如果系统时钟使用LXTAL，RTC时钟就不能选择HXTAL的32分频，因为HXTAL的32分频大于LXTAL时钟频率。

当APB总线时钟频率低于7倍RTC时钟频率时，日历的读取应该遵守以下流程：

1. 读取两次日历时间和日期寄存器；

2. 如果两次的值相等，那么这个值就是正确的；

3. 如果这两次的值不相等，应该再读一次；

4. 第三次的值可以认为是正确的。

RSYNF每2个RTC时钟周期被置位一次。在这时，影子日历寄存器会更新为真实的日历时间和日期。

为了确保这3个值（RTC_SS，RTC_TIME，RTC_DATE）为同一时间，硬件上采取了如下一致性机制：

1. 读RTC_SS锁定RTC_TIME和RTC_DATE的更新；

2. 读RTC_TIME锁定RTC_DATE的更新；

3. 读 RTC_DATE 解锁 RTC_TIME 和 RTC_DATE 的更新。

如果想在一个很短的时间间隔内（少于2个RTCCLK）读取日历，应先清除RSYNF位并等待其置位后再读取。

下面几种情况，软件须等待RSYNF置位后才能读日历寄存器（RTC_SS，RTC_TIME，RTC_DATE）：

1. 系统复位之后；

2. 日历初始化之后；

3. 一次移位操作之后。

特别是从低功耗模式唤醒后，软件必须清除RSYNF位并等待RSYNF再次置位后才能读取日历寄存器。

## 当 BPSHAD=1时，读日历寄存器

当BPSHAD=1，RSYNF位会被硬件清0，读日历寄存器不需考虑RSYNF位。当前真实的日历寄存器值会被直接读取。如此配置的好处是当从低功耗模式（Deep-sleep/Standby模式）唤醒后，软件可以立即获取当前日历寄存器的值而无需加入任何等待延迟（此延迟最大为2个RTC

时钟周期）。

由于没有RSYNF位周期性的置位，如果两次读日历寄存器之间出现ck_apre时钟边沿，不同寄存器（RTC_SS/RTC_TIME/RTC_DATE）的值可能并非同一时刻。

另外，如果日历寄存器的值正在发生变化的时刻被APB总线读取，那么有可能APB总线读取的值是不准确的。

为了确保日历值的正确性和一致性，读取时软件须如下操作：连续读取所有日历寄存器的值两次，如果上两次的值是一样的，那么这个值就是一致的且准确的。

## 13.3.6. RTC 复位

在RTC单元，有两个复位源可用：系统复位和备份寄存器复位。

当系统复位有效时，日历影子寄存器和RTC_STAT寄存器的某些位将要复位到默认值。

备份寄存器复位将会影响下面的寄存器，但系统复位不会对它们产生影响：

RTC 真实的日历寄存器；

RTC 控制寄存器（RTC_CTL）；

RTC 预分频寄存器（RTC_PSC）；

RTC 高精度频率补偿寄存器（RTC_HRFC）；

RTC 移位控制寄存器（RTC_SHIFTCTL）；

RTC 时间戳寄存器（RTC_SSTS/RTC_TTS/RTC_DTS）；

RTC 闹钟寄存器（RTC_ALRMxSS/RTC_ALRMxTD(x=0)）。

RTC 备份寄存器（RTC_BKPx）；

当系统复位或者进入省电模式的时候，RTC单元将会继续运行。但是如果备份寄存器复位，RTC将会停止计数并且所有的寄存器会复位。

## 13.3.7. RTC移位功能

当用户有一个高精度的远程时钟而且RTC1Hz时钟（ck_spre）和远程时钟只有一个亚秒级的偏差，RTC单元提供一个称作移位的功能去消除这个偏差来提高秒钟的精确性。

以二进制格式显示亚秒值，RTC运行时该值是递减计数。因此通过增加RTC_SHIFTCTL寄存器的SFS[14：0]的值到RTC_SS同步预分频器计数器值SSC[15：0]）或通过增加SFS[14：0]的值到同步预分频器计数器SSC[15：0]并且同时置位A1S位，能分别延迟或提前下一秒到达的时间。

RTC_SS的最大值取决于RTC_PSC寄存器的FACTOR_S的值。FACTOR_S越大，调整的精度也就越高。

因为1Hz的时钟（ck_spre）由FACTOR_A和FACTOR_S共同产生，越高的FACTOR_S值就意味着越低的FACTOR_A值，同时越低的FACTOR_A意味着越高的功耗。

注意：在使用移位功能之前，软件必须检查 RTC_SS 中 SSC 的第 15 位（SSC[15]）并确保该位为 0。写 RTC_SHIFTCTL 寄存器之后，RTC_STAT 寄存器的 SOPF 位将会再次置位。当同步移位操作完成时，SOPF 位被硬件清 0。系统复位不影响 SOPF 位。当 REFEN=0 时，移位操作才能正确的工作。如果 REFEN=1，软件禁止写入 RTC_SHIFTCTL。

## 13.3.8. RTC参考时钟检测

RTC参考时钟是另外一种提高RTC秒级精度的方法。为了使能这项功能，需要有一个相对于LXTAL有更高精度的外部参考时钟源（50Hz或60Hz）。

使能这项功能之后（REFEN=1），每一个秒更新的时钟（1Hz）边沿将与最近的RTC_REFIN参考时钟沿进行对比。在大多数情况下，这两个时钟沿是对齐的。但当两个时钟沿由于LXTAL准确度的原因没有对齐的时候，RTC参考时钟的检测功能会偏移1Hz时钟沿一点相位，使得下一个1Hz时钟沿和参考时钟沿对齐。

当REFEN=1，每一秒前后都会有一个进行检测的时间窗，处于不同的检测状态，时间窗时长也不同。当检测状态处于检测第一个参考时钟边沿时，使用7个ck_apre时长的时间窗，当检测状态处于边沿对齐操作时，使用3个ck_apre时长的时间窗。

无论使用哪一种时间窗，当参考时钟在时间窗中被检测到的时候，同步预分频计数器会被强制重载。当两个时钟（ck_spre和参考时钟）边沿是对齐的，这个重载操作对1Hz日历更新没有任何影响。但是当两个时钟边沿没有对齐时，这个重载操作将会移动ck_spre时钟边沿，以使得ck_spre（1Hz）时钟边沿和参考时钟边沿对齐。

当参考检测功能正在运行中但外部参考时钟消失（在3个ck_apre时长时间窗内没有发现参考时钟边沿），日历也能通过LXTAL继续自动更新。如果这个参考时钟重新恢复，参考时钟检测功能会先用7个ck_apre时长时间窗口去检测参考时钟，然后用3个ck_apre时长时间窗口去调节ck_spre（1Hz）时钟边沿。

注意：使能参考时钟检测功能之前（REFEN=1），软件必须配置 FACTOR_A 为 0x7F，FACTOR_S 为 0xFF。

待机模式下，参考时钟检测功能不可用。

## 13.3.9. RTC数字平滑校准

RTC平滑校准是一种用于校准RTC频率的方法，该方法通过调整校准周期内的RTC时钟脉冲个数的方式来实现校准。

完成一次这种校准相当于在一次校准周期内，RTC时钟的脉冲个数增加或者减少了一定的数目。这种校准的分辨率大约为0.954ppm，范围为从-487.1ppm到+488.5ppm。

校准周期的时间可以配置到 220/219/218 RTC 时钟周期，如果 RTC 的输入频率是 32.768KHz，这些校准周期时间分别代表 32/16/8 秒。

高精度频率补偿寄存器（RTC_HRFC）指定了在校准周期内要屏蔽的RTC时钟数目，CMSK[8：0]位能屏蔽0到511个RTC时钟，这样RTC的频率最多降低487.1PPM。

为了提高RTC频率可以设置FREQI位。如果FREQI位被置位，将会有512个额外的RTC时钟周期增加到校准周期（32/16/8 秒）时间期间，这意味着每211/210/29 RTC时钟插入一个RTC时钟周期。

因此使用FREQI可以使RTC频率增加488.5ppm。

同时使用CMSK和FREQI，每个周期时间可以调整-511到+512个RTC时钟周期。这意味着在0.954ppm分辨率的情况下，调整范围为从-487.1ppm到+488.5ppm。

当数字平滑校准功能正在运行时，按如下公式计算输出校准频率：

$$
f _ {c a l} = f _ {r t c c l k} \times (1 + \frac {F R E Q I \times 5 1 2 - C M S K}{2 ^ {N} + C M S K - F R E Q I \times 5 1 2})\tag{13-3}
$$

注意： N=20/19 /18（32/16/8 秒）校准时间周期。

## 当 FACTOR_A < 3 时校准：

当异步预分频器值（FACTOR_A）被设置小于3时，若要使用校准功能，软件不能将FREQI位设置为1。当FACTOR_A<3，FREQI位设置将会被忽略。

当FACTOR_A小于3时，FACTOR_S值应小于标称值。假设RTC时钟频率是正常的32.768KHz，对应的FACTOR_S应该按下面所示设置：

FACTOR_A = 1：FACTOR_S减少4（32.768KHz下16379）

FACTOR_A = 0：FACTOR_S减少8（32.768KHz下32759）

当FACTOR_A小于3，CMSK为0x100，校准频率公式如下：

$$
f _ {c a l} = f _ {r t c c l k} \times (1 + \frac {2 5 6 - C M S K}{2 ^ {N} + C M S K - 2 5 6})\tag{13-4}
$$

注意： N=20/19 /18（32/16/8 秒）校准时间周期。

## 验证 RTC校准

提供1Hz校准时钟的输出用于协助软件测量并验证RTC的精度。

在有限的测量周期内测量RTC的频率，最高可能发生2个RTCCLK的测量误差。

为了消除这一测量误差，测量周期应该和校准周期一致。

◼ 校准周期设为32秒（默认配置）

用准确的32秒周期去测量1Hz校准输出的准确性能保证这个测量误差在0.477ppm（在32秒周期内0.5个RTCCLK）之内。

◼ 校准周期设为16秒（通过设置CWND16位）

使用此配置，CMSK[0]被硬件置0。

用准确的16秒周期去测量1Hz校准输出的准确性能保证这个测量误差在0.954ppm（在16秒周期内0.5个RTCCLK）之内。

◼ 校准周期设为8秒（通过设置CWND8位）

使用此配置，CMSK[1：0]被硬件置0。

用准确的8秒周期去测量1Hz校准输出的准确性能保证这个测量误差在1.907ppm（在8秒周期内0.5个RTCCLK）之内。

## 运行中重校准

当INITF位是0，用下面的步骤，软件可以更新RTC_HRFC：

1. 等待SCPF位置0；

2. 写一个新的值到RTC_HRFC寄存器；

3. 3 个 ck_apre 时钟周期之后，新的校准设置开始生效。

## 13.3.10. 时间戳功能

时间戳功能由 $\mathsf { R T C \_ T S }$ 管脚输入，通过配置TSEN位来使能。

当RTC_TS管 脚 检 测 到 时 间 戳 事 件 发 生 时 ， 会 将 日 历 的 值 保 存 在 时 间 戳 寄 存 器 中（RTC_DTS/RTC_TTS/RTC_SSTS），同时时间戳标志（TSF）也将由硬件置1。如果时间戳中断使能被启用（TSIE），时间戳事件会产生一个中断。

时间戳寄存器只会在时间戳事件第一次发生的时刻（TSF=0）记录日历时间，而当TSF=1时，时间戳事件的值不会被记录。

注意：因为同步机制的原因，当时间戳事件发生时，TSF 会延迟 2 个 ck_apre 周期置位。

## 13.3.11. 校准时钟输出

如果COEN位设置为1，RTC_OUT0/1会输出参考校准时钟。

当COS位设置为0（默认值）并且异步预分频器（FACTOR_A）设为0x7F时，RTC_CALIB的频率是 $f _ { \mathrm { r t c c l k } } / 6 4$ 。因此若RTCCLK的频率为32.768KHz，RTC_CALIB对应的输出为512Hz。因为下降沿存在轻微的抖动，因此推荐使用RTC_CALIB输出的上升沿。

当COS位设置为1时，RTC_CALIB的频率计算公式为：

$$
f _ {\text { rtc\_calib }} = \frac {f _ {\text { rtcclk }}}{(\text { FACTOR\_A } + 1) \times (\text { FACTOR\_S } + 1)}\tag{13-5}
$$

若RTCCLK为32.768KHz，如果预分频器是默认值，那么RTC_CALIB对应的输出是1Hz。

## 13.3.12. 闹钟输出

当OS控制位不为0x00时，RTC_ALARM复用输出功能被启用。这个功能将直接输出RTC_STAT寄存器的闹钟标志ALRMxF。

RTC_CTL寄存器中的OPOL位可以配置ALRMxF标志或者WTF标志输出时候的极性，因此RTC_ALARM的输出电平有可能与相应的位值相反。

## 13.3.13. RTC 引脚配置

RTC_OUT，RTC_TS都使用同一个(PC13 /PA4)引脚。无论(PC13 /PA4)的GPIO是什么配置(PC13 /PA4)的功能由RTC控制。

$$
(P C 1 3 / P A 4) \text {的输出优先级如表} \tag {13-1. RTC (PC13/PA4)} \text {引脚配置}
$$


表 13-1. RTC (PC13 /PA4)引脚配置


<table><tr><td colspan="2">功能配置和引脚功能</td><td>OS[1:0](输出选择)</td><td>COEN(校准输出)</td><td>OUT1EN</td><td>ALARMOUTTYPE(闹钟输出类型)</td><td>DISPU</td><td>TSEN(时间戳使能)</td></tr><tr><td rowspan="4">闹钟开漏输出</td><td rowspan="2">无上拉</td><td rowspan="2">01或10或11</td><td>-</td><td>0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">-</td></tr><tr><td>1</td><td>1</td></tr><tr><td rowspan="2">内部上拉</td><td rowspan="2">01或10或11</td><td>-</td><td>0</td><td rowspan="2">0</td><td rowspan="2">1</td><td rowspan="2">-</td></tr><tr><td>1</td><td>1</td></tr><tr><td rowspan="2" colspan="2">闹钟推挽输出</td><td rowspan="2">01或10或11</td><td>-</td><td>0</td><td rowspan="2">1</td><td rowspan="2">0</td><td rowspan="2">-</td></tr><tr><td>1</td><td>1</td></tr><tr><td colspan="2">校准推挽输出</td><td>00</td><td>1</td><td>0</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="2">时间戳浮空输入</td><td>00</td><td>0</td><td>-</td><td>-</td><td>-</td><td>1</td></tr><tr><td rowspan="3" colspan="2">唤醒引脚或者标准GPIO</td><td>00</td><td>0</td><td>-</td><td rowspan="3">-</td><td rowspan="3">-</td><td rowspan="3">0</td></tr><tr><td>00</td><td>1</td><td rowspan="2">1</td></tr><tr><td>-</td><td>0</td></tr></table>


PC13 /PA4引脚可以用于以下功能：


⚫ RTC_ALARM 输出：通过 RTC_CTL 寄存器 OS [1:0] 位域配置

⚫ RTC_CALIB 输出： 通过 RTC_CTL 寄存器 COEN [23] 位配置

⚫ RTC_TS：时间戳事件检测

RTC_TYPE寄存器中ALRMOUTTYPE位可以选择RTC_ALRM输出是开漏还推挽配置RTC_CTL寄存器的OUT1EN位，可以在PA4引脚输出RTC_OUT1信号。


表 13-2. RTC_OUT 配置


<table><tr><td>OS [1:0]ALARM 输出使能</td><td>COEN(校准输出使能</td><td>OUT1EN</td><td>RTC_OUT0</td><td>RTC_OUT1</td></tr><tr><td>00</td><td>0</td><td rowspan="3">0</td><td>-</td><td>-</td></tr><tr><td>00</td><td>1</td><td>CALIB</td><td>-</td></tr><tr><td>01 or 10 or 11</td><td>-</td><td>ALRM</td><td>-</td></tr><tr><td>00</td><td>0</td><td rowspan="4">1</td><td>-</td><td>-</td></tr><tr><td>00</td><td>1</td><td>-</td><td>CALIB</td></tr><tr><td>01 or 10 or 11</td><td>0</td><td>-</td><td>ALRM</td></tr><tr><td>01 or 10 or 11</td><td>1</td><td>ALRM</td><td>CALIB</td></tr></table>


表 13-3. RTC 低功耗模式管理


<table><tr><td>模式</td><td>模式下能否工作</td><td>退出该模式的方法</td></tr><tr><td>睡眠模式</td><td>是</td><td>RTC中断</td></tr><tr><td>深度睡眠</td><td>当时钟源是LXTAL或IRC32K时可以工作</td><td>RTC闹钟/时间戳事件</td></tr><tr><td>待机模式</td><td>当时钟源是LXTAL或IRC32K时可以工作</td><td>RTC闹钟/时间戳事件</td></tr></table>

## 13.3.14. RTC 中断

所有的RTC中断都被连接到EXTI控制器。

如果想使用RTC闹钟/时间戳中断，应按下面步骤操作：

1. 设置并使能对应的 EXTI 中连接到 RTC 闹钟/时间戳的中断线，然后配置该线为上升沿触发模式；

2. 配置并使能 RTC 闹钟/时间戳的全局中断；

3. 配置并使能 RTC 闹钟/时间戳功能。


表 13-4. RTC 中断控制


<table><tr><td>中断</td><td>事件标志</td><td>控制位</td><td>退出睡眠模式</td><td>退出深度睡眠模式和待机模式</td></tr><tr><td>闹钟0</td><td>ALRM0F</td><td>ALRM0IE</td><td>Y</td><td><eq>Y^{(1)}</eq></td></tr><tr><td>时间戳</td><td>TSF</td><td>TSIE</td><td>Y</td><td><eq>Y^{(1)}</eq></td></tr></table>

（1）. 仅当RTC时钟源为LXTAL或IRC32K时，才可以从深度睡眠和待机模式唤醒。
