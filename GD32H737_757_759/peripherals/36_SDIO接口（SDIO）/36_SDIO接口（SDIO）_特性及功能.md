# 36. SDIO 接口（SDIO）

# 36.1. 简介

安全的数字输入/输出接口（SDIO）定义了 SD 卡、SD I/O 卡和嵌入式多媒体卡（e•MMC）主机接口，提供 AHB 系统总线与 SD 存储卡、SD I/O 卡以及 e•MMC 设备之间的命令和数据传输。

所支持的 SD 存储卡和 SD I/O 卡系统规格书可以通过 SD 卡协会网站（www.sdcard.org）获取。

所支持的嵌入式多媒体卡（e•MMC）系统规格书可以通过多媒体卡协会网站（www.jedec.org）获取，由 JEDEC 固态技术协会出版。

# 36.2. 主要特征

SDIO 的主要特征如下：

e•MMC：兼容嵌入式多媒体卡系统规格书 V4.51 及之前的版本。有五种不同的数据总线模式：1 位（默认）、4 位（包括 SDR 和 DDR）和 8 位（包括 SDR 和 DDR）；

SD 卡：与 SD 存储卡规格版本 3.0 全兼容；

SD I/O：与 SD I/O 卡规格版本 3.0 全兼容，有三种不同的数据总线模式：1 位（默认）和4 位（包括 SDR 和 DDR）；

104MHz 数据传输频率和 8 位数据传输模式；

中断和 DMA请求；

数据传输支持 DDR 模式。

注意：SDIO 在同一时间仅支持一个 SD、SD I/O 卡或 e•MMC，但可支持多个 e•MMC。

两个 SDIO 接口的实现特点如 36-1. SDIO 所示。


表 36-1. 两个 SDIO


<table><tr><td>SDIO features</td><td>SDIO0</td><td>SDIO1</td></tr><tr><td>延迟模块(SDR104,HS200)</td><td>+</td><td>+</td></tr><tr><td>SDIO_CLKIN</td><td>+</td><td>-</td></tr><tr><td>SDIO_CMDDIR,SDIO_DAT0DIR,SDIO_DAT123DIR</td><td>+</td><td>-</td></tr><tr><td>MDMA 命令结束、MDMA 数据结束和MDMA 缓存结束的触发信号</td><td>+</td><td>-</td></tr></table>


注意：“-”表示不支持，“+”表示支持。


# 36.3. SDIO 功能说明

# 36.3.1. SDIO 总线拓扑

上电复位之后，主机必须通过特殊的基于消息的总线协议来初始化卡。

每个消息是由以下部分中的一个来表示：

命令：命令是启动一个操作的令牌，从主机发送到卡。命令串行传输在 CMD 线上。

响应：响应是从卡发送到主机，作为先前接收到的命令的回应。响应串行传输在 CMD 线上。

数据：数据可以从卡传输到主机或者从主机传输到卡。数据通过数据线传送。用于数据传输的数据线的数目可以是 1（DAT0）、4（DAT0-DAT3）或 8（DAT0-DAT7）。

命令，响应和数据块的结构在 章节中介绍。一次数据传输就是一个总线操作。

有几种不同类型的操作。一般操作总是包含一个命令和响应。此外，一些操作还有一个数据令牌。还有一些其他操作直接将他们的信息包含在命令或响应结构中。在这种情况下，操作没有数据令牌。在 DAT0-DAT7 和 CMD 信号线上的比特位根据主机时钟同步传输。

三种类型的数据传输命令定义如下：

流命令：这些命令发起连续的数据流，只有当 CMD 信号线上出现停止命令时，数据传输终止。该模式将命令的开销减少到最低（仅支持e•MMC）。

面向块的命令：这些命令成功发送一个数据块后紧跟一个 CRC 校验。读和写操作允许单个或多个块传输。与流命令相同，当 CMD 信号线上出现停止命令时，多块传输终止。

多字节模式：支持大小为 1-512 字节范围的数据块。（仅 SD/SD I/O 支持）

总线上的基本操作是命令/响应操作（参考 36-1. SDIO “ ” “ ” 。这种类型的总线事务直接在命令或响应结构中传递它们的信息。此外，有些操作还有数据令牌。卡与设备之间的数据传输通过块完成。


图 36-1. SDIO “无响应” 和 “无数据” 操作


![image](images/bf6afb8208e6.jpg)


多块操作模式比单块操作速度更快。当 CMD 信号线上出现停止命令时，多块传输终止。主机数据传输可以使用单个或多个数据线。多个块的读操作如 36-2. SDIO 所示，多个块的写操作如 36-3. SDIO 所示。块的写操作在数据（DAT0）信号线上使用忙

信号。


图 36-2. SDIO 多块读操作


![image](images/34fa0fe7a342.jpg)



图 36-3. SDIO 多块写操作


![image](images/154177bd265c.jpg)


SD 存储卡和 SD I/O 卡（包括仅 IO 卡和组合卡）直接的数据传输是以数据块的方式完成的。e•MMC 卡以数据块或数据流方式进行数据传输。 36-4. SDIO 和 36-5. SDIO分别是数据流的读和写操作。


图 36-4. SDIO 数据流读操作


![image](images/b7a59352b08b.jpg)



图 36-5. SDIO 数据流写操作


![image](images/0850ef87cfb3.jpg)


# 36.3.2. SDIO 操作模式


表 36-2. SDIO 适用 SD & SD/IO 卡的操作模式


<table><tr><td>总线速度模式</td><td>最大总线速度[Mbyte/s]</td><td>最大时钟频率[MHz]</td><td>电压[V]</td></tr><tr><td>DS</td><td>12.5</td><td>25</td><td>3.3</td></tr><tr><td>HS</td><td>25</td><td>50</td><td>3.3</td></tr><tr><td>SDR12</td><td>12.5</td><td>25</td><td>1.8</td></tr><tr><td>SDR25</td><td>25</td><td>50</td><td>1.8</td></tr><tr><td>DDR50</td><td>50</td><td>50</td><td>1.8</td></tr><tr><td>SDR50</td><td>50</td><td>100</td><td>1.8</td></tr><tr><td>SDR104</td><td>104</td><td>208</td><td>1.8</td></tr></table>


表 36-3. SDIO 适用 e•MMC 卡的操作模式


<table><tr><td>总线速度模式</td><td>最大总线速度[Mbyte/s]</td><td>最大时钟频率[MHz]</td><td>电压[V]</td></tr><tr><td>向后兼容 MMC 卡</td><td>26</td><td>26</td><td>3/1.8</td></tr><tr><td>HS SDR</td><td>52</td><td>52</td><td>3/1.8</td></tr><tr><td>HS DDR</td><td>104</td><td>52</td><td>3/1.8</td></tr><tr><td>HS200</td><td>200</td><td>200</td><td>1.8</td></tr></table>

注意：1. DS 表示默认速度，HS表示高速模式；2.SDR 表示单倍数据速率信号传输，DDR 表示双倍数据速率信号传输；3. SD/SD I/O 卡最大的总线速度时，总线宽度为 4 位；e•MMC 最大的总线速度时，总线宽度为 8 位；4. 最大的频率取决于 I/O 速度；5. SDR104 模式和 HS200模式需要使用延迟模块来支持采样调谐，但 SDR50 模式时延迟模块是可选择的。

# 36.3.3. SDIO 框图

36-6. SDIO 显示了 SDIO 的结构框图，主要有三大部分：

SDIO 适配器：由控制单元、命令单元和数据单元组成。控制单元管理时钟信号，命令单元管理命令的传输，数据单元管理数据的传输。

AHB 接口：包括通过 AHB 总线访问的寄存器、用于数据传输的 FIFO 单元以及产生中断和 DMA 请求信号。

内部 DMA（IDMA）以及 AHB 主机接口


图 36-6. SDIO 框图


![image](images/e80e40a855f0.jpg)


# 36.3.4. SDIO 引脚和内部信号


表 36-4. SDIO 内部输入/输出信号


<table><tr><td>信号</td><td>信号类型</td><td>描述</td></tr><tr><td>CK_SDIO</td><td>输入</td><td>SDIO 内核时钟</td></tr><tr><td>HCLK</td><td>输入</td><td>AHB 时钟</td></tr><tr><td>SDIOIT</td><td>输出</td><td>SDIO 全局中断</td></tr><tr><td>SDIO_CMD_END</td><td>输出</td><td>MDMA 的 SDIO 命令结束触发信号</td></tr><tr><td>SDIO_DATA_END</td><td>输出</td><td>MDMA 的 SDIO 数据结束触发信号</td></tr><tr><td>SDIO_BUF_END</td><td>输出</td><td>MDMA 的 SDIO IDMA 缓存结束触发</td></tr><tr><td>SDIO_IN_CLK</td><td>输入</td><td>卡的反馈时钟,信号连接到 SDIO_CLK 脚,用于 DS/HS 模式</td></tr><tr><td>SDIO_FB_CLK</td><td>输入</td><td>CPDM 延迟模块后的 SD/SD I/O/e•MMC 卡调节反馈时钟(用于 SDR50、DDR50、SDR104 以及 HS200)</td></tr></table>


表 36-5. SDIO 引脚介绍


<table><tr><td>信号</td><td>信号类型</td><td>描述</td></tr><tr><td>SDIO_CLK</td><td>输出</td><td>SD/SD I/O/e•MMC 卡的时钟</td></tr><tr><td>SDIO_CLKIN</td><td>输入</td><td>来自卡的外部驱动的时钟反馈(用于 SDR12,SDR25,SDR50,DDR50)</td></tr><tr><td>SDIO_CMD</td><td>输入/输出</td><td>双向命令/响应信号</td></tr><tr><td>SDIO_CMDDIR</td><td>输出</td><td>SDIO_CMD 的方向指示信号</td></tr><tr><td>SDIO_DAT[7:0]</td><td>输入/输出</td><td>用于数据输入/输出的数据线</td></tr><tr><td>SDIO_DAT0DIR</td><td>输出</td><td>SDIO_DAT0 数据线的方向指示</td></tr><tr><td>SDIO_DAT123DIR</td><td>输出</td><td>SDIO_DAT[3:1]数据线的方向指示</td></tr></table>

# 36.3.5. SDIO 介绍

SDIO_DAT[7:0]线具有不同的工作模式：

上电后默认情况下，使用 1 位数据总线（SDIO_DAT0），初始化后，主机可以通过修改寄存器来更改数据总线宽度。

对于 SD 或 SDIO 卡，可以使用 1 位（SDIO_DAT0）或 4 位（SDIO_DAT0[3:0]）的数据总线宽度。所有数据线均以推挽模式运行。

对于 e•MMC，可以使用 1 位（SDIO_DAT0）、4 位（SDIO_DAT0[3:0]）或 8 位（SDIO_DAT0[7:0]）的数据总线宽度。

为了连接电压切换收发器，使用 I/O 方向信号指示数据线上的数据流方向。SDIO_DAT0DIR 信号指示 SDIO_DAT0 数据线的 I/O 方向，SDIO_DAT123DIR 则指示 SDIO_DAT[3:1]数据线的方向。SDIO_CMD 线上的数据流方向用 I/O 方向信号 SDIO_CMDDIR 表示。SDIO_CMD 只能在推挽模式下运行。

卡的时钟 SDIO_CLK 源自 CK_SDIO 时钟：

当 CK_SDIO 的占空比为 50%时，即使分频因子 DIV = 0，也可以使用。

◼ 当 CK_SDIO 的占空比不是 50%时，必须满足分频因子 DIV > 0，才可以使用。

SDIO_CMD 和 SDIO_DAT[7:0]输出与 SDIO_CLK 之间的相位关系可以通过 CLKEDGE位选择，相位关系取决于 DIV、CLKEDGE 以及 DRSEL 设置，详细如 36-6. SDIO和数据输出的相位选择。


表 36-6. SDIO 命令和数据输出的相位选择


<table><tr><td>DIV</td><td>DRSEL</td><td>CLKEDGE</td><td>SDIO_CLK</td><td>命令输出</td><td>数据输出</td></tr><tr><td>=0</td><td>-</td><td>-</td><td>=CK_SDIO</td><td colspan="2">在CK_SDIO的下降沿生成</td></tr><tr><td>&gt;0</td><td>0</td><td>0</td><td rowspan="2">产生于CK_SDIO的上升沿</td><td colspan="2">在SDIO_CLK上升沿后的CK_SDIO下降沿生成</td></tr><tr><td>&gt;0</td><td>0</td><td>1</td><td colspan="2">在SDIO_CLK下降沿后的CK_SDIO上升沿生成</td></tr><tr><td>&gt;0</td><td>1</td><td>0</td><td rowspan="2">产生于CK_SDIO的上升沿</td><td>在SDIO_CLK上升沿后的CK_SDIO下降沿生成</td><td rowspan="2">在SDIO_CLK边沿后的CK_SDIO下降沿生成</td></tr><tr><td>&gt;0</td><td>1</td><td>1</td><td>在SDIO_CLK下降沿后的CK_SDIO上升沿生成</td></tr></table>

默认情况下，选择源自 SDIO_CLK 引脚的 SDIO_IN_CLK 反馈时钟输入来采样 SDIO 接收通道中的传入的数据。为了调整采样时钟的相位以适应接收数据的时序，可以将设备上的 CPDM延迟块连接到 SDIO_FB_CLK 时钟信号和 SDIO_IN_CLK 信号之间。然后选择 SDIO_FB_CLK作为数据接收通道的时钟，对接收的数据使用相位调整的采样时钟。该功能是 SDR104、HS200工作模式下必须满足的以及 SDR50、DDR50 工作模式下可选的。

当使用外部驱动器（电压开关收发器）时，可以选择 SDIO_CLKIN 反馈时钟输入信号来采样接收的数据。

SD/SD I/O/e•MMC 卡的时钟频率范围为 0 到 208MHz（最高的时钟频率受限于 I/O 速度）。

根据所选的总线模式（SDR 或 DDR），每个时钟周期在 SDIO_DAT[7:0]线上传输一位或两位。SDIO_CMD 线每个时钟周期仅传输一位。

# 36.3.6. SDIO 适配器

SDIO 适配器包括控制单元、命令单元和数据单元，并且可以向卡生成信号。这些信号的具体描述如下：

SDIO_CLK：SDIO 控制器提供给卡的时钟。每个时钟周期在命令线（SDIO_CMD）上只发送一位命令或数据。对于 MMC 卡 V4.2 版本可以在 0 MHz 到 48MHz 之间，对于 e•MMC V4.51版本可以在 0 MHz 到 200MHz 之间，对于 SD 或 SD I/O 卡可以在 0 MHz 到 208MHz。

SDIO 使用两个时钟信号：SDIO 适配器时钟和 AHB总线时钟（HCLK）。

SDIO_CMD：该信号是双向命令通道，用于卡的初始化和命令的传输。命令从 SDIO 控制器发送到卡，响应从卡发送到主机。CMD 信号有两种操作模式：用于初始化的开漏模式（仅用于e•MMC 卡的初始化）和用于命令传送的推挽模式（SD 卡/SD I/O 卡的初始化时以及 e•MMC卡的数据传输时使用）。

SDIO_DAT[7:0]：这些信号线都是双向数据通道。数据信号线操作在推挽模式。每次只有卡或者主机会驱动这些信号。默认情况下，上电或者复位后仅 DAT0 用于数据传输。SDIO 适配器可以配置更宽的数据总线用于数据传输，使用 DAT0-DAT3 或者 DAT0-DAT7（仅适用于e•MMC）。SDIO 对数据信号线 DAT1-DAT7 有内部上拉。在进入 4 位模式后，卡断开 DAT1 和DAT3 的内部上拉。相应地，在进入 8 位模式后，断开 DAT1-DAT7 的内部上拉。

SDIO_CLKIN：该信号线是数字输入信号线，用于 SD/SD I/O/e•MMC 卡的外部驱动的时钟反馈。（用于 SDR12，SDR25，SDR50，DDR50）

SDIO_CMDDIR：该信号是数字输入信号，作为 SDIO_CMD 信号线上数据流的输入/输出方向指示信号。

SDIO_DAT0DIR：该信号是数字输入信号，作为 SDIO_DAT0 数据线上数据流的输入/输出方向指示信号。

SDIO_DAT123DIR：该信号是数字输入信号，作为 SDIO_DAT[3:1]数据线上数据流的输入/输出方向指示信号。

SDIO 适配器是总线设备，提供与 SD/SD I/O /e•MMC 卡的接口，它由几个子单元组成：

# 控制单元

控制单元包含电源管理功能、用于存储卡时钟的时钟管理功能以及 I/O 方向管理功能。

电源管理是由 SDIO_PWRCTL 寄存器控制的，实现电源的掉电、上电。电源管理子单元会在复位后、断电阶段和上电阶段中禁止卡总线输出信号。通过设置 SDIO_CLKCTL 的CLKPWRSAV 位来配置省电模式，实现当总线空闲时，关闭 SDIO_CLK。

时钟管理使用 CK_SDIO 向卡生成 SDIO_CLK 时钟信号，并提供分频控制。适配器寄存器和FIFO 使用 AHB 时钟域（HCLK）。控制单元、命令发送通道和数据发送通道使用 SDIO 适配器时钟域（CK_SDIO）。命令响应通道和数据接收通道使用来自 SDIO_IN_CLK、SDIO_CLKIN或 SDIO_FB_CLK（由 CPDM 生成）的 SDIO 配器反馈时钟域。

I/O 方向管理控制外部电压收发器以及控制 SDIO_CMDDIR、SDIO_D0DIR 和 SDIO_D123DIR的信号。

# 命令单元

命令单元包含命令发送通道和响应接收通道，作用是在 SDIO_CMD 线上实现向卡发送命令和接收响应。命令发送通道由 SDIO_CLK 提供时钟，响应接收通道有专用的 SDIO 内部接收时钟，数据传输流由命令状态机（CSM）控制。在对 SDIO_CMDCTL 寄存器进行一次写操作并设置该寄存器的 CSMEN 位为 1 后，命令传输开始。首先向卡发送一个命令，这个命令包含 48位，通过 SDIO_CMD 线发出，每个 SDIO_CLK 发送一个比特数据。这 48 位命令包含 1 位起始位、1 位传输位、6 位命令索引（由 SDIO_CMDCTL 寄存器的 CMDIDX 位定义）、32 位参数（由 SDIO_CMDAGMT 定义）、7 位 CRC 和 1 位停止位。然后接收来自卡的响应（在SDIO_CMDCTL 寄存器的 CMDRESP 位不为 0b00 的情况下），响应分为 48 位的短响应和136 位的长响应，响应都存在 SDIO_RESP0 - SDIO_RESP3 寄存器中。命令单元同样可以产生命令状态标志（在 SDIO_STAT 寄存器中定义）。


命令状态机


<table><tr><td colspan="2">CS_Idle</td><td colspan="3">复位后准备发送命令</td></tr><tr><td rowspan="5"></td><td colspan="2">1.CSM 被使能并且 WAITDEND 使能</td><td>→</td><td>CS_Pend</td></tr><tr><td colspan="2">2.CSM 被使能并且 WAITDEND 失能并且 BOOT 未使能</td><td>→</td><td>CS_Send</td></tr><tr><td colspan="2">3.CSM 被关闭</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="2">4.BOOTMODEN 置位</td><td>→</td><td>CS_Boot</td></tr><tr><td colspan="4">注意:命令状态机在空闲状态至少保持 8 个 SDIO_CLK 周期,以满足 <eq>N_{CC}</eq> 和 <eq>N_{RC}</eq> 时序限制。<eq>N_{CC}</eq> 是两个主机命令之间的最小时间间隔,<eq>N_{RC}</eq> 是主机命令与卡响应之间的最小时间间隔。</td></tr></table>

<table><tr><td colspan="2">CS_Pend</td><td colspan="3">等待数据传输结束</td></tr><tr><td rowspan="3"></td><td colspan="2">1.数据传送完成</td><td>→</td><td>CS_Send</td></tr><tr><td colspan="2">2.CSM 被关闭</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="4">注意:DATALEN =&lt; 5 时,CSM 直接变为 CS_Send 状态;DATALEN &gt; 5 时,CSM 会等待 DSM 的信号后再变为 CS_Send 状态。</td></tr></table>

<table><tr><td colspan="2">CS_Send</td><td colspan="3">发送命令</td></tr><tr><td rowspan="3"></td><td colspan="2">1.命令发送后有响应</td><td>→</td><td>CS_Wait</td></tr><tr><td colspan="2">2.命令发送后无响应</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="2">3.CSM 被关闭</td><td>→</td><td>CS_Idle</td></tr></table>

<table><tr><td colspan="2">CS_Wait</td><td colspan="3">等待响应起始位</td></tr><tr><td rowspan="4"></td><td colspan="2">1.接收到响应(检测到起始位)</td><td>→</td><td>CS_Receive</td></tr><tr><td colspan="2">2.接收响应超时</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="2">3.CSM 被关闭</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="4">注意:命令超时时间固定为 64 个 SDIO_CLK 时钟周期。</td></tr></table>

<table><tr><td>CS_Receive</td><td>接收响应并检测 CRC</td></tr></table>

<table><tr><td>1.CSM 被关闭</td><td>→</td><td>CS_Idle</td></tr><tr><td>2.收到响应</td><td>→</td><td>CS_Idle</td></tr><tr><td>3.命令 CRC 检测失败</td><td>→</td><td>CS_Idle</td></tr></table>

<table><tr><td colspan="2">CS_Boot</td><td colspan="3">从卡读取引导数据</td></tr><tr><td rowspan="3"></td><td colspan="2">1.选择正常引导模式且使能引导模式</td><td>→</td><td>CS_Boot</td></tr><tr><td colspan="2">2.选择正常引导模式且禁止引导模式</td><td>→</td><td>CS_Idle</td></tr><tr><td colspan="2">3.选择备用引导模式</td><td>→</td><td>CS_Send</td></tr></table>

# 数据单元

数据单元实现主机与卡之间的数据传输。当数据宽度为 8 位（SDIO_CLKCTL 寄存器的BUSMODE 位为 0b10）时，数据传输使用 SDIO_DAT[7:0]信号线；当数据宽度为 4 位（SDIO_CLKCTL 寄存器的 BUSMODE 位为 0b01）时，数据传输使用 SDIO_DAT[3:0]信号线；当数据宽度为 1 位（SDIO_CLKCTL 寄存器的 BUSMODE 位为 0b00）时，数据传输使用SDIO_DAT[0]信号线。数据传输流由数据状态机（DSM）控制。在对 SDIO_DATACTL 寄存器进行一次写操作并将 SDIO_DATACTL 寄存器的 DATAEN 位为 1，数据传输开始。当SDIO_DATACTL 寄存器的 DATADIR 位为 0 时，数据是从控制器到卡；当 DATADIR 位为 1时，数据是从卡到控制器。数据单元同样可以产生数据状态标志（在 SDIO_STAT 寄存器中定义）。数据接收时，对于包含引导确认操作时，DSM 变为 DS_WaitACK 状态并等待引导确认，然后再变为 DS_WaitR 状态。


数据状态机


<table><tr><td colspan="2">DS_Idle</td><td colspan="3">数据单元不工作,等待发送和接收数据</td></tr><tr><td rowspan="3"></td><td colspan="2">1.(DSM使能或者DATAEN位使能)并且(DSM不忙且数据传输方向为主机到卡)</td><td>→</td><td>DS_WaitS</td></tr><tr><td colspan="2">2.(DSM使能或者DATAEN位使能)且禁用引导确认且数据传输方向为卡到主机</td><td>→</td><td>DS_WaitR</td></tr><tr><td colspan="2">3.DSM使能、使引导确认且数据传输方向为卡到主机</td><td>→</td><td>DS_WaitACK</td></tr></table>

<table><tr><td colspan="2">DS_WaitS</td><td colspan="3">等待数据 FIFO 为空标志无效或者数据传输结束</td></tr><tr><td rowspan="4"></td><td colspan="2">1.数据传输结束</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">2.DSM 被关闭且数据 FIFO 为空</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">3.数据传送保持标志置位</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">4.数据 FIFO 为空标志无效且数据保持标志清零</td><td>→</td><td>DS_Send</td></tr></table>

<table><tr><td colspan="2">DS_Send</td><td colspan="3">发送数据到卡</td></tr><tr><td rowspan="3"></td><td colspan="2">1.数据块已发送</td><td>→</td><td>DS_Busy</td></tr><tr><td colspan="2">2.DSM 被关闭</td><td>→</td><td>DS_Busy</td></tr><tr><td colspan="2">3.内部 CRC 错误</td><td>→</td><td>DS_Busy</td></tr><tr><td colspan="2">DS_Busy</td><td colspan="3">等待 CRC 状态标志</td></tr><tr><td rowspan="5"></td><td colspan="2">1.接收到正确 CRC 状态并且卡不繁忙</td><td>→</td><td>DS_WaitS</td></tr><tr><td colspan="2">2.没有接收到正确 CRC 状态且卡不繁忙</td><td>→</td><td>DS_WaitS</td></tr><tr><td colspan="2">3.接收到错误的 CRC 状态且卡不繁忙</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">4.DSM 被关闭且卡不繁忙</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="4">注意:命令超时时间设置在数据超时寄存器(SDIO_DATATO)中。</td></tr></table>

<table><tr><td colspan="2">DS_WaitR</td><td colspan="3">等待接收数据的起始位</td></tr><tr><td rowspan="5"></td><td colspan="2">1.数据接收结束</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">2.DSM 被关闭</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">3.数据保持且 FIFO 为空</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">4.在超时前收到起始位</td><td>→</td><td>DS_Receive</td></tr><tr><td colspan="4">注意:命令超时时间设置在数据超时寄存器(SDIO_DATATO)中。</td></tr></table>

<table><tr><td colspan="2">DS_Receive</td><td colspan="3">接收卡的数据并将其写入数据 FIFO</td></tr><tr><td rowspan="5"></td><td colspan="2">1.数据块已接收且读等待模式禁用</td><td>→</td><td>DS_WaitR</td></tr><tr><td colspan="2">2.数据传输结束且读等待模式禁用</td><td>→</td><td>DS_WaitR</td></tr><tr><td colspan="2">3.数据FIFO上溢错误发生</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">4.DSM被关闭且FIFO为空</td><td>→</td><td>DS_Idle</td></tr><tr><td colspan="2">5.CRC错误且数据接收完成</td><td>→</td><td>DS_Idle</td></tr></table>

<table><tr><td colspan="2">DS_WaitACK</td><td colspan="3">等待引导确认令牌</td></tr><tr><td rowspan="3"></td><td colspan="2">1.及时收到引导确认,且检验 OK</td><td>→</td><td>DS_WaitR</td></tr><tr><td colspan="2">2.确认超时或收到错误的确认</td><td>→</td><td>DS_WaitACK</td></tr><tr><td colspan="2">3.DSM 被关闭且 FIFO 为空</td><td>→</td><td>DS_Idle</td></tr></table>

# CRU 单元

CRU 单元为 SDIO 内部接收时钟选择时钟源，SDIO 内部接收时钟用于接收数据和命令响应。

通过配置 RCLK[1:0]寄存器来选择 SDIO 内部接收时钟的时钟源，有三种时钟可供选择：

SDIO_IN_CLK 总线主反馈时钟

SDIO_CLKIN 外部总线反馈时钟

SDIO_FB_CLK 总线调谐反馈时钟

注意：1. 当没有外部驱动且使用 DS/HS 总线模式时，选择 SDIO_IN_CLK。2. 当有外部总线驱动且在 SDR12、SDR25、SDR50、DDR50 总线模式时，选择 SDIO_CLKIN 时钟。3. 使用CPDM 延迟模块时，如果是 SDR104、HS200 模式，则必须选择 SDIO_FB_CLK 时钟输入；如果是 SDR50、DDR50 则可选择 SDIO_FB_CLK 时钟输入。4. 如果 CPM 和 DSM 都处于空闲状态时，SDIO 内部接收时钟的时钟源必须被改变。


图 36-7. CRU 单元


![image](images/e7b7f0ce7ace.jpg)


# 36.3.7. AHB 从接口

AHB 从接口用于访问 SDIO 寄存器、数据 FIFO 以及生成中断。包括数据 FIFO 单元、寄存器单元和中断。

AHB 从机接口包含以下子单元：

# 中断

当选择的状态标志中至少有一位为高时，中断逻辑产生中断。单元提供了中断使能寄存器逻辑来控制相应中断产生的开关。如果设置了相应的中断使能标志，则状态标志寄存器中产生一个中断请求。一些状态标志需要在中断标志清除寄存器中隐式清除。

# 寄存器单元

寄存器单元包含所有系统寄存器，目的是管理控制器与卡之间通信的信号。

# 数据 FIFO

数据 FIFO 单元有一个数据缓冲区，用于发送和接收 FIFO。FIFO 包含一个每个字的宽度为 32位，深度为 32 字的数据缓冲区。当使用半字或字节访问 FIFO 时，会产生 AHB 总线故障。

发送 FIFO 用于写数据到卡的操作。将要发送的数据通过 AHB 总线写入发送 FIFO，SDIO 适配器中的数据单元从发送 FIFO 读取数据，然后将数据发送到卡上。当 DATALEN 不是 4 的整数倍时，最后剩余的数据（1/2/3 字节）将以字传输的方式写入。

接收 FIFO 用于从卡读取数据的操作。将要传输的数据从卡读取，然后写入接收 FIFO。接收FIFO 中的数据在需要时读取到 AHB总线。当 DATALEN 不是 4 的整数倍时，读取最后剩余的数据（1/2/3 字节）时使用填充 0 值字节的字传输。

# 36.3.8. AHB 主接口

AHB 主接口使用 SDIO 内部 DMA（IDMA）在存储和 FIFO 之间进行数据传输。

# IDMA

IDMA 在存储和 FIFO 之间提供了一个双向高速数据传输通道。

通过 IDMAEN 位来使能 IDMA，IDMA 支持 8 节拍的突发模式传输。

突发模式具体分为突发模式发送和突发模式接收：

# 突发模式发送

只要 FIFO 对突发传输次数为空，数据就会以突发的形式从内存中获得，直到 DATALEN所指示的所有数据都传输完毕。如果 DATALEN 不是突发大小的倍数，则小于突发大小的剩余数据将以单次传输方式传输。当 DATALEN 不是 4 的倍数时，最后剩余的数据（1、2 或 3 字节）通过字传输获得。

# 突发模式接收

只要 FIFO 对突发传输次数为空，数据就会以突发的形式存储在内存中，直到 DATALEN所指示的所有数据都传输完毕。如果 DATALEN 不是突发大小的倍数，则小于突发大小的剩余数据将以单次传输方式传输。当 DATALEN 不是 4 的倍数时，最后剩余的数据（1、2 或 3 字节）以半字或字节传输的方式存储。

此外，IDMA 还提供了两种通道配置（由 BUFMOD 位选择）。

# 单缓冲通道

在单个缓冲区配置中，访问内存端的数据是从基址 IDMAADDR0 线性访问的。当 IDMA完成所有数据的传输，DSM 也完成传输时，DTEND 标志设为 1。

# 双缓冲通道

在双缓冲区配置中，内存端的数据从两个缓冲区访问，一个来自 IDMAADDR0，另一个来自 IDMAADDR1。这样，当 IDMA 访问其中一个内存缓冲区时，固件可以处理另一个。内存缓冲区的大小由 IDMASIZE 定义。缓冲区大小应该是突发大小的倍数。当通道被启用时，缓冲区的基址可以立即被更新。

在双缓冲通道模式下，通过 BUFSEL 寄存器位配置访问内存的地址。

◼ 当 BUFSEL 位为“0”时，IDMA硬件使用 IDMAADDR0 访问内存。当尝试通过固件写入该位寄存器时，写入操作将被忽略，IDMAADDR0 数据不会改变。但允许固件写入IDMAADDR1。

1 当 BUFSEL 位为“1”时，IDMA硬件使用 IDMAADDR1 访问内存。当尝试通过固件写入该寄存器时，写入操作将被忽略，IDMAADDR1 数据将不会更改。但允许固件写入IDMAADDR0。

当 IDMA 在其中一个缓冲区完成数据传输时，将缓冲区传输完成标志（IDMAEND）设置为 1，并翻转 BUFSEL 位，然后 IDMA 将继续从另一个缓冲区传输数据。当 IDMA 完成所有数据的传输，DSM 也完成传输时，DTEND 标志设为 1。

IDMAADDR0 和 IDMAADDR1 地址应该是字对齐的。

# 36.3.9. MDMA 请求

SDIO 的内部触发线（SDIO_DATA_END、SDIO_CMD_END 和 SDIO_BUF_END 线）可以直接向 MDMA 控制器发送请求，实现从/到不同内部 RAM 地址的连续传输，而不需要 CPU 参

与。

MDMA 的请求输入信号通过 SDIO_DATA_END 引脚传输。同时，输入信号会触发清除 DTEND和 CMDRECV 两个标志，通过 MDMA 直接访问 SDIO 控制和配置寄存器，开始新的传输，而无需 CPU 干预。

当成功接收到对命令的响应时，将置位 CMDRECV 标志。R1b 响应忙状态结束后，清除状态寄存器 DAT0BSY 的标志位并置位 DAT0BSYEND 标志位。当与最终繁忙信号相关联的序列命令响应结束时，设置连接到 MDMA 的 SDIO_CMD_END 输出。因此，MDMA 可以通过清除CMDRECV 和 DAT0BSYEND 状态标志来管理 CMD12（STOP_TRANSMISSION）命令（需要支持开放模式传输）。

在使用 Linux 操作系统时，要通过 SDIO 总线传输的数据包含在设备内部内存中的不连续地址的 1-4Kbyte 大小的数据块中。双缓冲模式允许改变 IDMA 在内部内存中的目标地址。每次缓冲区传输完成时，会置位状态寄存器的 IDMAEND 标志。通过连接到 MDMA 请求输入的SDIO_BUF_END 输出将此事件发送给 MDMA，新的缓冲区基地址可以在不需要 CPU 干预的情况下自动填充 IDMAADDR0 / IDMAADDR1 字段。

36-7. SDIO MDMA 显示了根据 SDIO 的请求在 MDMA 中的编程动作：


表 36-7. SDIO 与 MDMA 的连接


<table><tr><td>触发信号</td><td>事件</td><td>条件</td><td>MDMA 传输配置</td><td>MDMA 动作</td></tr><tr><td>SDIO_DATA_END</td><td>数据成功传输结束</td><td>DTEND = 1</td><td>单独</td><td>置位 DTENDC</td></tr><tr><td>SDIO_CMD_END</td><td>命令序列结束</td><td>CMDSEND = 1,或(CMDRECV = 1 且 DAT0BSY = 0)</td><td>单独</td><td>置位 CMDSENDC置位 CMDRECVC置位 DAT0BSYENDC</td></tr><tr><td>SDIO_BUF_END</td><td>到达缓冲区尾</td><td>IDMAENDC = 1</td><td>联动</td><td>置位 IDMAENDC更新 IDMAADDR0/1</td></tr></table>

# 36.3.10. AHB 总线与 SDIO_CLK 时钟的关系

AHB总线传输速度带宽应当是 SDIO总线带宽的3 倍以上。


表 36-8. AHB 和 e•MMC 时钟频率关系


<table><tr><td>SDIO 总线模式</td><td>总线宽度</td><td>最大 SDIO_CLK 时钟频率 [MHz]</td><td>最小 AHB 时钟频率 [MHz]</td></tr><tr><td>DS</td><td>8</td><td>26</td><td>19.5</td></tr><tr><td>HS</td><td>8</td><td>52</td><td>39</td></tr><tr><td>HS DDR</td><td>8</td><td>52</td><td>78</td></tr><tr><td>HS200</td><td>8</td><td>200</td><td>150</td></tr></table>


表 36-9. AHB 和 SD/SD I/O 卡时钟频率关系


<table><tr><td>SDIO 总线模式</td><td>总线宽度</td><td>最大 SDIO_CLK 时钟频率 [MHz]</td><td>最小 AHB 时钟频率 [MHz]</td></tr><tr><td>SDR12 (DS)</td><td>4</td><td>25</td><td>9.4</td></tr><tr><td>SDR25 (HS)</td><td>4</td><td>50</td><td>18.8</td></tr><tr><td>SDR50</td><td>4</td><td>100</td><td>37.5</td></tr><tr><td>DDR50</td><td>4</td><td>50</td><td>37.5</td></tr><tr><td>SDR104</td><td>4</td><td>208</td><td>78</td></tr></table>

# 36.3.11. 硬件流控制

硬件流控制功能在数据传输期间通过停止 SDIO_CLK 来冻结状态机，从而阻止 FIFO 下溢（发送数据）和上溢（接收数据）的错误发生。

当 FIFO 不能够发送或接收数据时，数据传输会暂停，保持暂停状态直到发送 FIFO 数据发送了一半或 DATALEN 长度的数据被存储，或直到接收 FIFO 数据已经接收了一半。当状态机冻结时，AHB 接口会保持活跃状态，因此即使执行硬件流控制时 FIFO 依旧可以操作。

硬件流控制通过置位 HWEN 寄存器位使能。

只有当 SDIO_DAT 数据与 SDIO_CLK 周期对齐时，才使用硬件流控制。SDR104 模式使用CPDM 延迟块不能使用硬件流控制。


图 36-8 硬件流控制时序


![image](images/1e0d445619bc.jpg)


# 36.4. 卡功能描述

# 36.4.1. 卡寄存器

卡内部定义了接口寄存器：OCR，CID，CSD，EXT_CSD，RCA，DSR 和 SCR。这些寄存器只能通过相应的命令来访问。OCR，CID，CSD 和 SCR 寄存器包含卡的一些特定信息，而 RCA和 DSR 寄存器是配置寄存器，存储实际的配置参数。EXT_CSD 寄存器同时包含卡的特定信息和实际的结构参数。有关具体信息，请参考相关的规范。

OCR寄存器：32位操作条件寄存器（OCR）储存卡的V 电压描述和存取模式指示（e•MMC）。另外，该寄存器包括一个状态信息位。如果卡上电过程已经完成该状态位被置位。该寄存器在e•MMC 和 SD 卡之间有一点不同。主机可以使用 CMD1（e•MMC），ACMD41（SD 存储卡），CMD5（SD I/O）来获取该寄存器的内容。

CID 寄存器：卡识别寄存器（CID）是 128 位宽。它包含在卡识别阶段使用的卡识别信息。每个读/写（RW）卡应具有唯一的标识号。主机可以使用 CMD2 和 CMD10 得到这个寄存器的内容。

CSD 寄存器：卡特定数据寄存器提供访问卡中的内容信息。CSD 定义了数据格式、错误校正类型、最大数据访问时间、数据传输速度、DSR 寄存器是否可以使用等。寄存器的可编程部分可通过 CMD27 来修改。主机可以使用 CMD9 得到这个寄存器的内容。

扩展 CSD 寄存器：只有 e•MMC4.51 有该寄存器。扩展 CSD 寄存器定义卡属性和选择模式。它的长度为 512 字节。最高 320 字节为属性段，定义了卡的功能，并且不能由主机修改。最低192 字节是模式段，定义了卡工作在哪种配置下。这些模式可以由主机通过 SWITCH 命令来修改。主机可以使用 CMD8（仅 e•MMC 支持这个命令），以获取该寄存器的内容。

RCA 寄存器：可写的 16 位相对卡地址寄存器存放卡地址，该地址在卡的初始化期间由卡向外发布。这个地址用于卡识别过程之后，所寻址的主机和卡通信。主机可以使用 CMD3 要求卡发布一个新的相对地址（RCA）。

注意：RCA 的寄存器的缺省值是 0x0001（e•MMC）或 0x0000（SD/SD I/O）。这个数值是保留值，用于通过 CMD7 设置所有卡到待机（Stand-by）状态。

DSR 寄存器（可选）：16 位驱动阶段寄存器是可选的，可用于在扩展操作条件中提高总线性能（取决于类似于总线长度，传输速率和卡数目这些参数）。CSD 寄存器中有 DSR 寄存器使用情况的信息。DSR 寄存器的默认值是 0x404。主机可以使用 CMD4 得到这个寄存器的内容。

SCR 寄存器：仅 SD/ SD I/O（如果有存储模块）有这个寄存器。除了 CSD 寄存器，还有另一种配置寄存器名为 SD 卡配置寄存器（SCR），它仅用于 SD 卡。SCR 提供了被配置到特定 SD存储卡的特殊功能的信息。SCR 寄存器的大小是 64 位。该寄存器应在出厂前通过 SD 存储卡制造商进行设置。主机可以使用 ACMD51 得到这个寄存器的内容。

# 36.4.2. 命令

# 命令类型

有四种控制卡的命令：

◼ 广播命令（bc），发送到所有卡，没有响应；

带响应的广播命令（bcr），发送到所有卡，同时从所有卡收到响应；

寻址（点对点）命令（ac），发送到寻址的卡上，DAT 信号线没有数据传输；

寻址（点对点）的数据传输的命令（adtc），发送到寻址的卡上，DAT 信号线进行数据传输。

# 命令格式

所有命令都是 48 位的固定码长，如 36-9. 所示，需要 1.92 us（25 MHz）0.96us（50 MHz）和 0.92us（52 MHz）的发送时间。


图 36-9. 命令标记格式


![image](images/0170631e8170.jpg)



表 36-10. 命令格式


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>[39:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>宽度</td><td>1</td><td>1</td><td>6</td><td>32</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘1’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>命令索引</td><td>参数</td><td>CRC7</td><td>结束位</td></tr></table>

一个命令总是从一个起始位（始终为 0）开始，随后的位表示传输的方向（主机=1）。接下来的6 位表示命令的索引，该值被解释为一个二进制编码的数字（0 到 63 之间）。一些命令需要一个参数（例如，一个地址），由 32 位编码。上面表中的表示为“x”的值表示这个变量依赖于该命令。所有的命令有一个 CRC 7 位校验，由结束位（总是 1）终止。

# 命令分类

卡的命令集分为几类（见 36-11. CCCs ）。每类支持一组卡的功能。 36-11.CCCs 根据卡支持的命令来决定 CCC 的设置。

对于 SD 卡，类别为 0，2，4，5 和 8 的命令是强制的，应被 SD 卡支持。类别 7 中除了 CMD40以外都是强制性用于 SDHC。其他类是可选的。所支持的卡命令类（CCC）被编码为参数，设置在每个卡的卡特定数据（CSD）寄存器，提供给主机如何访问该卡信息。

对于 e•MMC 卡，类别为 0 的命令是强制性的，应被 e•MMC 卡支持。其他类只对特定类型的卡是强制或是可选的。通过使用不同的类，可以选择几种配置（例如，一个块可写的卡或流可读的卡）。所支持的卡命令类（CCC）被编码为参数，设置在每个卡的卡的特定数据（CSD）寄存器，提供给主机如何访问该卡信息。


表 36-11. 卡命令类 （CCCs）


<table><tr><td></td><td>卡命令类(CCC)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>支持的命令</td><td>类描述</td><td>basic</td><td>Stream read</td><td>Block read</td><td>Stream write</td><td>Block write</td><td>erase</td><td>write protection</td><td>Lock card</td><td>application specific</td><td>I/O mode</td><td>switch</td><td>reserved</td></tr><tr><td>CMD0</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD1</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD2</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD3</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD4</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD5</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td></tr><tr><td>CMD6</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD7</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD8</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD9</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD10</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD11</td><td>M</td><td>+</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD12</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD13</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD14</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD15</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD16</td><td>M</td><td></td><td></td><td>+</td><td></td><td>+</td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td></tr><tr><td>CMD17</td><td>M</td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD18</td><td>M</td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD19</td><td>M</td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD20</td><td>M</td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD21</td><td>M</td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD23</td><td>M</td><td></td><td></td><td>+</td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD24</td><td>M</td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD25</td><td>M</td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD26</td><td>M</td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD27</td><td>M</td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD28</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD29</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD30</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD32</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD33</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD34</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td></tr><tr><td>CMD35</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD36</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD37</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td></tr><tr><td>CMD38</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td></tr><tr><td>CMD40</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td></tr><tr><td>CMD42</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td></tr><tr><td>CMD49</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMD52</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td></tr><tr><td>CMD53</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td>+</td><td></td></tr><tr><td>CMD54</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td></tr><tr><td>CMD55</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>CMD56</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>CMD57</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td></tr><tr><td>ACMD6</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD13</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD22</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD23</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD41</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD42</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr><tr><td>ACMD51</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td></tr></table>

注意： 1. M：强制，O：可选。

2. SD 卡中 CMD5 是 0 类命令，在 e•MMC 中，CMD5 是 9 类命令。

3. 支持 UHS-I 的 SD 卡中 CMD11 是 0 类命令且强制的，其他卡中是可选的；在 e•MMC 中，CMD11 是 1 类命令。

4. CMD14，CMD20，CMD21，CMD26，CMD39，CMD40，CMD49 和 CMD54 仅用于 e•MMC；CMD32，CMD33，CMD52，CMD57 和 ACMDx 仅用于 SD 存储卡。

5. 在使用 ACMDx 命令之前发送 APP_CMD 命令（CMD55）。

6. CMD5，CMD8，CMD11 和 CMD53 对于 e•MMC 卡和 SD 卡有不同的含义。

7. 命令类 1 和 3 是被废弃的。

# 详细的命令描述

下列表详细描述了所有的总线命令。响应 R1-R7 将在 章节说明。寄存器 CID，CSD 和 DSR在 介绍。卡应忽略参数中填充位和保留位。


表 36-12. 基本命令（class 0）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td rowspan="3">CMD0</td><td>bc</td><td>[31:0] 00000000</td><td>-</td><td>GO_IDLE_STATE</td><td>复位所有的卡到空闲状态。</td></tr><tr><td>bc</td><td>[31:0] F0F0F0F0</td><td>-</td><td>GO_PRE_IDLE_STATE</td><td>复位所有的卡到 pre-idle 状态</td></tr><tr><td>-</td><td>[31:0] FFFFFFFFA</td><td>-</td><td>BOOT_INITIATION</td><td>开始备用引导操作</td></tr><tr><td>CMD1</td><td>bc</td><td>[31:0] OCR</td><td>R3</td><td>SEND_OP_COND</td><td>在空闲状态,请求卡通过 CMD 线发送响应(包含操作条件寄存器的内容)。</td></tr><tr><td>CMD2</td><td>bcr</td><td>[31:0] 填充位</td><td>R2</td><td>ALL_SEND_CID</td><td>请求任何卡通过 CMD 线发送发送 CID 数据(任何连接到主机的卡都会响应)。</td></tr><tr><td>CMD3</td><td>bcr</td><td>[31:0] 填充位</td><td>R6</td><td>SEND_RELATIVE_ADDR</td><td>请求卡发布新的相对卡地址(RCA)。</td></tr><tr><td>CMD4</td><td>bc</td><td>[31:16] DSR[15:0] 填充位</td><td>-</td><td>SET_DSR</td><td>设置所有卡的 DSR 寄存器。</td></tr><tr><td>CMD5</td><td>bcr</td><td>[31:25]保留位[24]S18R[23:0] I/O OCR</td><td>R4</td><td>IO_SEND_OP_COND</td><td>仅适用于 I/O 卡。它类似于用于 SD 存储卡的 ACMD41 命令,用于查询所需要的 I/O 卡的电压范围。</td></tr><tr><td>CMD5</td><td>ac</td><td>[31:16]RCA[15]睡眠/唤醒[14:0] 填充位</td><td>R1b</td><td>SLEEP_AWAKE</td><td>仅适用于 e•MMC,在睡眠和待机(stand-by)状态之间切换</td></tr><tr><td>CMD6</td><td>ac</td><td>[31] 模式0:检查功能1:切换功能[30:24] 保留(全‘0’)[23:20]为功能组 6保留(“0”或“F”)[19:16] 为功能组5保留(“0”或“F”)[15:12] 为功能组4保留(“0”或“F”)[11:8] 为功能组 3保留(“0”或“F”)[7:4] 功能组 2 命令系统[3:0] 功能组 1 访问模式</td><td>R1</td><td>SWITCH_FUNC</td><td>仅适用于 SD 卡。检查可以切换的功能(模式 0),卡切换功能(模式 1)。</td></tr><tr><td>CMD6</td><td>ac</td><td>[31:26] 设为 0[25:24] 访问[23:16] 索引[15:8] 值[7:3] 设为 0[2:0] 命令集</td><td>R1b</td><td>SWITCH</td><td>仅适用于 e•MMC 卡。切换所选卡的操作模式,或修改 EXT_CSD 寄存器。</td></tr><tr><td>CMD7</td><td>ac</td><td>[31:16] RCA[15:0] 填充位</td><td>R1b</td><td>SELECT/DESELECT_CARD</td><td>这个命令用于卡在待机(stand-by)状态和发送(transfer)状态之间切换,或编程(programming)状态和断开(disconnects)状态之间切换。在两种情况下,要选中该卡用它自己的相对地址,若不选中该卡用任何其他地址。地址 0 用于取消选择该卡。</td></tr><tr><td>CMD8</td><td>bcr</td><td>[31:12]保留位[11:8] 工作电压(VHS)[7:0]检查模式</td><td>R7</td><td>SEND_IF_COND</td><td>向 SD 存储卡发送接口条件,包括主机供电电压信息和询问卡是否支持电压。保留位应设为 0。</td></tr><tr><td>CMD8</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>SEND_EXT_CSD</td><td>仅用于 e•MMC 卡。卡发送自己的EXT_CSD 寄存器作为数据块。</td></tr><tr><td>CMD9</td><td>ac</td><td>[31:16] RCA[15:0] 填充位</td><td>R2</td><td>SEND_CSD</td><td>被选定的卡通过 CMD 线发送它的卡特定数据(CSD)。</td></tr><tr><td>CMD10</td><td>ac</td><td>[31:16] RCA[15:0] 填充位</td><td>R2</td><td>SEND_CID</td><td>被选定的卡通过CMD线发送它的卡标识(CID)。</td></tr><tr><td>CMD11</td><td>ac</td><td>[31:0] 00000000</td><td>R1</td><td>VOLTAGE_SWITCH</td><td>切换到1.8V总线信号水平。</td></tr><tr><td>CMD12</td><td>ac</td><td>[31:0] 填充位</td><td>R1b</td><td>STOP TRANSMISSION</td><td>强制卡停止传输。</td></tr><tr><td>CMD13</td><td>ac</td><td>[31:16] RCA[15:0] 填充位</td><td>R1</td><td>SEND_STATUS</td><td>被选定的卡发送它的状态寄存器。</td></tr><tr><td>CMD14</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>BUSTEST_R</td><td>主机从卡中读取反向的总线测试数据模式。</td></tr><tr><td>CMD15</td><td>ac</td><td>[31:16] RCA[15:0] 保留位</td><td>-</td><td>GO_INACTIVE_STATE</td><td>将被选定的卡转换到非激活(Inactive)状态。这个命令被用于当主机明确地想停用一张卡的时候。</td></tr><tr><td>CMD19</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>BUSTEST_W</td><td>主机向卡发送总线测试模式。</td></tr></table>


表 36-13. 面向块的读命令（class 2）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD16</td><td>ac</td><td>[31:0]块长度</td><td>R1</td><td>SET_BLOCKLEN</td><td>在标准容量SD卡和e•MMC卡的情况下,该命令为所有后续块命令(读,写,锁)设置块长度(以字节为单位)。默认值是512字节。只有在CSD中局部块读操作被允许时,设置长度对于存储器访问命令有效。在高容量SD存储卡的情况下,块长度是由CMD16命令设置,不会影响内存读和写命令。总是使用512字节的固定块长度。在这两种情况下,如果块长度设置大于512字节,BLOCK_LEN_ERROR位会被卡置位。</td></tr><tr><td>CMD17</td><td>adtc</td><td>[31:0]数据地址</td><td>R1</td><td>READ_SINGLE_BLOCK</td><td>在标准容量SD卡和e•MMC卡的情况下,通过SET_BLOCKLEN命令读取所选择大小的块。在高容量存储卡的情况下,块长度是固定的512字节,忽略SET_BLOCKLEN命令。</td></tr><tr><td>CMD18</td><td>adtc</td><td>[31:0]数据地址</td><td>R1</td><td>READ_MULTIPLE_BLOCK</td><td>不断从卡传输数据块到主机,直到收到STOP_TRANSMISSION命令才中断。块长度规定和READ_SINGLE_BLOCK 命令是一样的。</td></tr><tr><td>CMD21</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>SEND_TUNNING_BLOCK</td><td>e•MMC 卡,为优化 HS200 采样点发送 128 时钟的调谐模板(4 bit 总线宽度下 64 字节,8 bit 下 128 字节)</td></tr><tr><td colspan="6">注意:传输的数据不能跨越物理块边界,除非 READ_BLK_MISALIGN 在 CSD 寄存器中被设置。</td></tr></table>


表 36-14. 流读取命令（class 1）和流写入命令（class 3）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD11</td><td>adtc</td><td>[31:0]数据地址</td><td>R1</td><td>READ_DAT_UNTIL_STOP</td><td>从卡中读取数据流,起始于给定的地址,直至收到STOP_TRANSMISSION命令。</td></tr><tr><td>CMD20</td><td>adtc</td><td>[31:0]数据地址</td><td>R1</td><td>WRITE_DAT_UNTIL_STOP</td><td>从主机写数据流,起始于给定的地址,直至收到STOP_TRANSMISSION命令。</td></tr><tr><td colspan="6">注意:传输的数据不能跨越物理块边界,除非READ_BLK_MISALIGN在CSD寄存器中被设置。</td></tr></table>


表 36-15. 面向块的写命令（class 4）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD16</td><td>ac</td><td>[31:0] 块长度</td><td>R1</td><td>SET_BLOCKLEN</td><td>见表 36-13. 面向块的读命令(class 2)描述。</td></tr><tr><td>CMD23</td><td>ac</td><td>[31:16] 设为0[15:0] 块数目</td><td>R1</td><td>SET_BLOCK_COUNT</td><td>定义了将要在后续多个块的读或写命令被传输块的数目。如果参数为全0,随后的读/写操作将被认为无终止的。</td></tr><tr><td>CMD24</td><td>adtc</td><td>[31:0] 数据地址</td><td>R1</td><td>WRITE_BLOCK</td><td>在标准容量SD卡的情况下,该命令写入由 SET_BLOCKLEN 命令所选择的块长度。在高容量SD卡的情况下,块长度是固定的512字节忽略 SET_BLOCKLEN 命令。</td></tr><tr><td>CMD25</td><td>adtc</td><td>[31:0] 数据地址</td><td>R1</td><td>WRITE_MULTIPLE_BLOCK</td><td>连续写入数据块,直至收到 STOP_TRANSMISSION 命令。块长度是和 WRITE_BLOCK 命令规定一样的。</td></tr><tr><td>CMD26</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>PROGRAM_CID</td><td>对卡识别寄存器进行编程。此命令必须一次发出。该编程涉及硬件,以防止首次编程以后的操作。通常情况下这个命令是针对厂家保留。</td></tr><tr><td>CMD27</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>PROGRAM_CSD</td><td>对CSD的可编程位编程。</td></tr><tr><td>CMD49</td><td>adtc</td><td>[31:0] 填充位</td><td>R1</td><td>SET_TIME</td><td>根据512字节数据块中的RTC信息设置实时时钟</td></tr><tr><td colspan="6">注意:1.传输的数据不得跨越物理块边界。除非是在CSD设置WRITE_BLK_MISALIGN。在写入部分块不支持的情况下,块长度=默认块长度(CSD中给出)。2.标准容量SD存储卡数据地址以字节为单位,高容量SD存储卡数据地址以块(512字节)为单位。</td></tr></table>


表 36-16. 擦除命令（class 5）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD32</td><td>ac</td><td>[31:0]数据地址</td><td>R1</td><td>ERASE_WR_BLK_START</td><td>设置要被擦除数据的第一个块的地址。(SD)</td></tr><tr><td>CMD33</td><td>ac</td><td>[31:0]数据地址</td><td>R1</td><td>ERASE_WR_BLK_END</td><td>设置要被擦除数据的最后一个块地址。(SD)</td></tr><tr><td>CMD35</td><td>ac</td><td>[31:0]数据地址</td><td>R1</td><td>ERASE_GROUP_START</td><td>在选择的擦除范围内,设置第一个擦除组的地址。(e•MMC)</td></tr><tr><td>CMD36</td><td>ac</td><td>[31:0]数据地址</td><td>R1</td><td>ERASE_GROUP_END</td><td>在选择的连续擦除范围内,设置最后一个擦除组的地址。(e•MMC)</td></tr><tr><td>CMD38</td><td>ac</td><td>[31:0]填充位</td><td>R1b</td><td>ERASE</td><td>擦除所有之前选择的数据块.</td></tr><tr><td colspan="6">注意: 1. CMD34 和 CMD37 被保留,以便保持与旧版本 e•MMC 的兼容性2. 标准容量 SD 存储卡数据地址以字节为单位,高容量 SD 存储卡数据地址以块(512 字节)为单位。</td></tr></table>


表 36-17. 面向块的写保护命令（class 6）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD28</td><td>ac</td><td>[31:0] 数据地址</td><td>R1b</td><td>SET_WRITE_PROT</td><td>如果卡有写保护功能,该命令将设置地址组的写保护位。写保护的特性被编码在卡的特定数据(WP_GRP_SIZE)中。高容量SD存储卡不支持此命令。</td></tr><tr><td>CMD29</td><td>ac</td><td>[31:0] 数据地址</td><td>R1b</td><td>CLR_WRITE_PROT</td><td>如果卡有写保护功能,该命令将清除寻址组的写保护位。</td></tr><tr><td>CMD30</td><td>adtc</td><td>[31:0] 写保护数据地址</td><td>R1</td><td>SEND_WRITE_PROT</td><td>如果卡有写保护功能,该命令请求卡发送写保护位状态。</td></tr><tr><td colspan="6">注意: 1. 高容量 SD 存储卡不支持这三个命令。</td></tr></table>


表 36-18. 锁卡命令（class 7）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD16</td><td>ac</td><td>[31:0] 块长度</td><td>R1</td><td>SET_BLOCK_LEN</td><td>见表 36-13. 面向块的读命令(class 2)描述。</td></tr><tr><td>CMD42</td><td>adtc</td><td>[31:0] 保留位(所有位设为 0)</td><td>R1</td><td>LOCK_UNLOCK</td><td>用于设置/重置密码或者对卡上锁/解锁。数据块长度由命令 SET_BLOCK_LEN 设置。参数及锁卡数据结构里的保留位应设为0。</td></tr></table>


表 36-19. 特定应用命令（class 8）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>ACMD41</td><td>bcr</td><td>[31]保留位[30]HCS[29:24]保留位[23:0]<eq>V_{DD}</eq>电压窗口(OCR[23:0])</td><td>R3</td><td>SD_SEND_OP_COND</td><td>发送给主机容量支持信息(HCS),并请求访问的卡在响应中发送操作条件寄存器(OCR)的内容。当卡接收到SEND_IF_COND命令,HCS是有效的。CCS位被分配到OCR[30]。</td></tr><tr><td>ACMD42</td><td>ac</td><td>[31:1]填充位[0]set_cd</td><td>R1</td><td>SET_CLR_CARD_DETECT</td><td>在卡的CD/DAT3(引脚1)上连接[1]/断开[0]50K上拉电阻。</td></tr><tr><td>ACMD51</td><td>adtc</td><td>[31:0]填充位</td><td>R1</td><td>SEND_SCR</td><td>读SD卡配置寄存器(SCR)。</td></tr><tr><td>CMD55</td><td>ac</td><td>[31:16] RCA[15:0]填充位</td><td>R1</td><td>APP_CMD</td><td>表明卡的下一个命令是特定应用命令而不是标准命令。</td></tr><tr><td>CMD56</td><td>adtc</td><td>[31:1]填充位[0]RD/WR</td><td>R1</td><td>GEN_CMD</td><td>对于通用/特定应用命令,该命令用于向卡传输一个数据块,或从卡读取一个数据块。主机设RD/WR=1时是从卡中读数据,RD/WR=0时啊写数据到卡中。</td></tr><tr><td colspan="6">注意:1. ACMDx是针对SD存储卡的特定应用命令。</td></tr></table>


表 36-20. I/O 模式命令（class 9）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD39</td><td>ac</td><td>[31:16] RCA[15] 寄存器写标志[14:8] 寄存器地址[7:0] 寄存器数据</td><td>R4</td><td>FAST_IO</td><td>用于写入和读取8位(寄存器)的数据字段。如果写标志被设置,该命令寻址寄存器,并提供数据写入。如果写标志被清为0,R4的响应中包含从寻址寄存器中读取的数据。该命令用于访问未在MMC标准定义的应用程序相关的寄存器。</td></tr><tr><td>CMD40</td><td>bcr</td><td>[31:0] 填充位</td><td>R5</td><td>GO_IRQ_STATE</td><td>设置系统进入中断模式。</td></tr><tr><td>CMD52</td><td>adtc</td><td>[31] R/W 标志[30:28] 功能数目[27] RAW 标志[26] 填充位[25:9] 寄存器地址[8] 填充位[7:0] 写数据/填充位</td><td>R5</td><td>IO_RW_DIRECT</td><td>IO_RW_DIRECT 命令提供简单的方式访问任意I/O功能的128K存储空间的寄存器。此命令可以实现使用单个命令对寄存器的读写。一个常见的用途是初始化寄存器或查询I/O功能状态。这个命令是读或写单 I/O 寄存器最快的方法,因为它仅需要一对单一的命令/响应。</td></tr><tr><td>CMD53</td><td>adtc</td><td>[31] R/W 标志[30:28] 功能数目[27] 块模式[26] OP 码[25:9] 寄存器地址[8:0] 字节/块数</td><td></td><td>IO_RW_EXTENDED</td><td>该命令允许用一个简单命令读取或写入大量的 I/O 寄存器。</td></tr><tr><td colspan="6">注意: 1.CMD39, CMD40 仅用于 e•MMC 卡2. CMD52, CMD53 仅用于 SD I/O 卡</td></tr></table>


表 36-21. 切换功能命令（class 10）


<table><tr><td>命令索引</td><td>类型</td><td>参数</td><td>响应格式</td><td>简称</td><td>描述</td></tr><tr><td>CMD53</td><td>adtc</td><td>[31:16] 安全协议详细[15:8] 安全协议[7:0] 保留</td><td>R1</td><td>PROTOCOL_RD</td><td>仅用于SD存储卡和SD I/O卡。从卡到主机连续不断的传输数据块,数据块的个数由CMD23提供,数据传输可以被STOP_TRANSMISSION中断,该命令不支持包命令,数据块的大小固定为512字节。</td></tr><tr><td>CMD54</td><td>adtc</td><td>[31:16] 安全协议详细[15:8] 安全协议[7:0] 保留</td><td>R1</td><td>PROTOCOL_WR</td><td>仅用于SD存储卡和SD I/O卡。从主机到卡连续不断的传输数据块,数据块的个数由CMD23提供,数据传输可以被STOP_TRANSMISSION中断,该命令不支持打包命令,数据块的大小固定为512字节。</td></tr></table>

# 36.4.3. 响应

所有的响应都是通过 CMD 信号线发送，方向是由卡到主机。响应传输总是从对应响应字串的最左位开始。响应字串的长度依赖于响应类型。

# 响应类型

响应的类型有七种，分别如下：

R1 / R1b：普通命令响应

R2：CID，CSD 寄存器

R3：OCR 寄存器

R4：Fast I/O 

◼ R5：中断请求

R6：发布的 RCA响应

R7：卡接口条件

SD 存储卡支持其中的五种响应，R1 / R1b, R2, R3, R6, R7。SD I/O 卡和 e•MMC 卡支持支持额外的响应类型，名为 R4 和 R5，但对于 SD I/O 卡和 e•MMC 卡，这两种响应并不完全相同。

# 响应格式

响应有两种格式，如 36-10. 所示，所有响应经由 CMD 线发出。代码的长度取决于响应类型。除了 R2 的长度是 136 位，其他的长度均为 48 位。


图 36-10. 响应令牌格式


![image](images/ae7fcc127b44.jpg)


![image](images/71b0e42f7f41.jpg)


响应总是从一个起始位（始终为 0）开始，随后第二位表示传输的方向（卡= 0）。下面表中的“x”的值表示为可变的部分。除了 R3 类型的所有响应由 CRC 校验。每个响应字段由结束位（总是 1）终止。

# R1（普通命令响应）

代码长度为 48 位。位 45:40 指示要响应的命令索引，该值被解释为一个二进制编码的数字（0到 63 之间）。卡的状态被 32 位编码。注意，如果写数据到卡上，在每个数据块传输之后会出现 BUSY 信号，在每个数据块传输完成后主机需要检查 BUSY 信号。卡状态在章节中描述。


表 36-22. R1 响应


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>[39:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>32</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>命令索引</td><td>卡状态</td><td>CRC7</td><td>结束位</td></tr></table>

# R1b

R1b 格式与 R1 相同，但可以在数据线 DAT0 上发送忙信号。收到命令后，依据收到命令之前的状态，卡可能变为忙状态。主机应在响应中检查忙状态。

# R2（CID, CSD 寄存器）

代码长度为 136 位。CID 寄存器的内容作为对命令 CMD2 和 CMD10 的响应被发送。CSD 寄存器的内容将作为以 CMD9 响应被发送。卡只响应发送 CID 和 CSD 的位[127.. 1]，这两个寄存器保留位[0]被替换为响应的结束位。


表 36-23. R2 响应


<table><tr><td>位</td><td>135</td><td>134</td><td>[133:128]</td><td>[127:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>127</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘111111’</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>保留</td><td>CID 或 CSD 寄存器,内部 CRC7</td><td>结束位</td></tr></table>

# R3（OCR 寄存器）

代码长度为 48 位。该 OCR 寄存器的内容作为 ACMD41（SD 存储卡），CMD1（e•MMC）的响应被发送。不同卡的响应可能有一点不同。


表 36-24. R3 响应


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>[39:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>32</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘111111’</td><td>x</td><td>‘1111111’</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>保留</td><td>OCR 寄存器</td><td>保留</td><td>结束位</td></tr></table>

# R4（Fast I/O）

仅适用于 e•MMC 卡。代码长度为 48 位。参数域包括选定卡的 RCA，被读取或写入寄存器的地址，和它的内容。如果操作成功，参数域状态位置位。


表 36-25. R4 响应（e•MMC）


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td colspan="4">[39:8] 参数域</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>16</td><td>1</td><td>7</td><td>8</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘100111’</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>CMD39</td><td>RCA[31:16]</td><td>状态[15]</td><td>寄存器地址[14:8]</td><td>读寄存器的内容[7:0]</td><td>CRC7</td><td>结束位</td></tr></table>

# R4b

仅适用于 SD I/O 卡。代码长度为 48 位。SD I/O 卡接收到 CMD5 命令后会返回一个唯一的 SDI/O 卡响应 R4。


表 36-26. R4 响应（SD I/O）


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>39</td><td>[38:36]</td><td>35</td><td>[34:32]</td><td>31</td><td>[30:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>1</td><td>3</td><td>1</td><td>3</td><td>1</td><td>23</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘111111’</td><td>x</td><td>x</td><td>x</td><td>‘000’</td><td>x</td><td>x</td><td>‘1111111’</td><td>1</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>保留</td><td>C</td><td>I/O 功能数目</td><td>当前存储</td><td>填充位</td><td>S18A</td><td>I/OOCR</td><td>保留</td><td>结束位</td></tr></table>

# R5（中断请求）

仅适用于 e•MMC 卡。代码长度为 48 位。若这个响应由主机产生，参数中 RCA 域为 0x0。


表 36-27. R5 响应（MMC）


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td colspan="2">[39:8] 参数域</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>16</td><td>16</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘101000’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>CMD40</td><td>成功的卡或主机的RCA [31:16]</td><td>[15:0]未定义,可能作为中断数据</td><td>CRC7</td><td>结束位</td></tr></table>

# R5b

仅适用于 SD I/O 卡。SD I/O 卡对于 CMD52 和 CMD53 命令的响应是 R5。如果卡和主机之间的通信是在 1 位或 4 位 SD 模式下，响应应是 48 位响应（R5）。


表 36-28. R5 响应（SD I/O）


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>[39:24]</td><td>[23:16]</td><td>[15:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>16</td><td>8</td><td>8</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘11010x’</td><td>‘0’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>CMD52/53</td><td>填充位</td><td>响应标志</td><td>读或写的数据</td><td>CRC7</td><td>结束位</td></tr></table>

# R6（发布的 RCA响应）

代码长度为 48 位。位[45:40]表示对 CMD3 响应的命令索引。参数字段的 16 个最高位比特用于已发布的 RCA 号。


表 36-29. R6 响应


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td colspan="2">[39:8] 参数域</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>16</td><td>16</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘000011’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>CMD3</td><td>新发布卡的RCA</td><td>卡的状态位:23,22,19,12:0</td><td>CRC7</td><td>结束位</td></tr></table>

# R7（卡接口条件）

仅适用于 SD 存储卡。代码长度为 48 位。卡支持电压信息由 CMD8 的响应发送。位[19:16]表明该卡支持的电压范围。接受了供电电压的卡返回 R7 响应。在响应中，卡回送的参数设置电压范围和检查模式。


表 36-30. R7 响应


<table><tr><td>位</td><td>47</td><td>46</td><td>[45:40]</td><td>[39:20]</td><td>[19:16]</td><td>[15:8]</td><td>[7:1]</td><td>0</td></tr><tr><td>位宽</td><td>1</td><td>1</td><td>6</td><td>20</td><td>4</td><td>8</td><td>7</td><td>1</td></tr><tr><td>数值</td><td>‘0’</td><td>‘0’</td><td>‘001000’</td><td>‘00000h’</td><td>x</td><td>x</td><td>x</td><td>‘1’</td></tr><tr><td>描述</td><td>起始位</td><td>传输位</td><td>CMD8</td><td>保留位</td><td>可接受电压</td><td>回送检查模式</td><td>CRC7</td><td>结束位</td></tr></table>

# 36.4.4. 数据包格式

数据总线模式有 5 种，1 位、4 位 SDR/DDR 和 8 位 SDR/DDR 总线模式。1 位模式是强制的，4 位和 8 位总线模式是可选的。

# 1位数据包格式

卡复位和初始化之后，只有 DAT0 被用于传输数据。其他引脚可以用于其他用处。 36-11. 1， 36-12. 4 和 36-13. 8 显示了数据宽度是 1 位，4 位和 8 位时的数据包格式。


图 36-11. 1 位数据总线宽度


![image](images/02e994556806.jpg)


# 4位数据包格式


图 36-12. 4 位数据总线宽度


![image](images/75338db1bad9.jpg)


# 8位数据包格式


图 36-13. 8 位数据总线宽度


![image](images/47327b040f20.jpg)


# 4 位 DDR 数据包格式（DAT3-DAT0）

对于每条数据线，数据可以以每个时钟周期一位（单数据速率）或两位（双数据速率）的速率传输。DDR（双倍数据速率）信号，数据在两个 SDIO_CLK时钟沿采样。 36-14. 4 DDR和 36-15. 8 DDR 显示了数据总线宽度为 4 位 DDR 和 8 位DDR 时的数据包格式。


图 36-14. 4 位 DDR 数据包格式


![image](images/e7cfa19f43ad.jpg)


# 8 位 DDR 数据包格式（DAT7-DAT0）


图 36-15. 8 位 DDR 数据包格式


![image](images/4d47947075d3.jpg)



注意：对于 DDR 数据总线：1.字节数据不交错，但 CRC 是交错的。2.起始位在上升沿和下


降沿均有效。3.结束位仅在上升沿有效（“x”未定义）。

# 36.4.5. 卡的两种状态


注意：18, 17, 7 位仅适用于 e•MMC。14, 3 位仅适用于 SD 存储卡。


SD 存储卡支持两种状态字段，而其他的卡只支持第一种：

卡状态：执行命令的错误和状态信息，在响应中指示。

SD 状态：512 位的扩展状态信息，支持特定功能的 SD 存储卡和未来应用特定功能。

# 卡状态

响应格式 R1 包含一个名为卡状态的 32 位字段。该字段用来传送该卡的状态的信息（可以存储在本地状态寄存器）到主机。除非特别说明，卡的状态信息总是与之前发出的命令相关。

表中的类型和清除条件的缩写如下：

# 类型

•E：错误位。向主机发送错误条件。这些位一旦响应（报告错误）被发出去就会清除。

•S：状态位。这些位仅作为信息字段，并不因为对命令的响应而改变。这些位是持久性的，它们根据卡状态被设置或被清除。

•R：卡在命令解释和验证阶段（响应模式）检测到异常。

•X：卡在命令执行阶段（执行模式）检测到异常。

# 清除条件

•A：根据卡当前状态。

•B：始终与之前命令相关。接收到有效命令可清除该状态（有命令延迟）。

•C：读可清除。


表 36-31. 卡状态


<table><tr><td>位</td><td>标识符</td><td>类型</td><td>数值</td><td>说明</td><td>清除条件</td></tr><tr><td>31</td><td>OUT_OF_RANGE</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>命令的参数超出卡的允许范围。</td><td>C</td></tr><tr><td>30</td><td>ADDRESS_ERROR</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>在命令中使用与块长度不匹配的未对齐地址。</td><td>C</td></tr><tr><td>29</td><td>BLOCK_LEN_ERROR</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>所传输的块长度是卡不允许的,或者传输的字节数不匹配块的长度。</td><td>C</td></tr><tr><td>28</td><td>ERASE_SEQ_ERROR</td><td>ER</td><td>'0' = 无错误'1' = 错误</td><td>擦除命令顺序发生错误。</td><td>C</td></tr><tr><td>27</td><td>ERASE_PARAM</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>擦除时选择了无效的擦除块。</td><td>C</td></tr><tr><td>26</td><td>WP_VIOLATION</td><td>ERX</td><td>'0' = 未保护'1' = 已保护</td><td>当主机试图写一个受保护的块或暂时或永久写保护卡时置位。</td><td>C</td></tr><tr><td>25</td><td>CARD_IS_LOCKED</td><td>SX</td><td>'0' = 卡未锁'1' = 卡已锁</td><td>当设置该位,表示卡已经被主机锁住。</td><td>A</td></tr><tr><td>24</td><td>LOCK_UNLOCK_FAILED</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>在上锁/解锁中有命令的顺序错误或检测到密码错误时置位。</td><td>C</td></tr><tr><td>23</td><td>COM_CRC_ERROR</td><td>ER</td><td>'0' = 无错误'1' = 错误</td><td>之前命令的 CRC 校验错误。</td><td>B</td></tr><tr><td>22</td><td>ILLEGAL_COMMAND</td><td>ER</td><td>'0' = 无错误'1' = 错误</td><td>对于当前状态,命令非法。</td><td>B</td></tr><tr><td>21</td><td>CARD_ECC_FAILED</td><td>ERX</td><td>'0' = 成功'1' = 失败</td><td>卡的内部实施了 ECC 校验,但在更正数据时失败。</td><td>C</td></tr><tr><td>20</td><td>CC_ERROR</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>卡内部控制器错误。</td><td>C</td></tr><tr><td>19</td><td>ERROR</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>在操作过程中发生一般的或者未知的错误。</td><td>C</td></tr><tr><td>18</td><td>UNDERRUN</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>仅针对 e•MMC。该卡不支持在流读取模式下的数据传输。</td><td>C</td></tr><tr><td>17</td><td>OVERRUN</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>仅针对 e•MMC. 该卡不支持在流写入模式下的数据编程。</td><td>C</td></tr><tr><td>16</td><td>CID/CSD_OVERWRITE</td><td>ERX</td><td>'0' = 无错误'1' = 错误</td><td>可能是下面两种错误之一:- CSD 的只读部分与卡内容不匹配- 试图进行拷贝或永久写保护的反向操作,即恢复原状或解除写保护</td><td>C</td></tr><tr><td>15</td><td>WP_ERASE_SKIP</td><td>ERX</td><td>'0' = 未保护'1' = 已保护</td><td>若置位,因为存在写保护数据块仅有部分地址空间被擦除;被暂时或者永久写保护的卡被擦除。</td><td>C</td></tr><tr><td>14</td><td>CARD_ECC_DISABLED</td><td>SX</td><td>'0' = 使能'1' = 失能</td><td>执行命令时未使用内部 ECC。</td><td>A</td></tr><tr><td>13</td><td>ERASE_RESET</td><td>SR</td><td>'0' = 清除'1' = 设置</td><td>因为收到一个擦除顺序之外的命令,擦除序列在执行前被清除。</td><td>C</td></tr><tr><td>[12:9]</td><td>CURRENT_STATE</td><td>SX</td><td>0 = 空闲1 = 就绪2 = 识别3 = 待机4 = 传输5 = 发送数据6 = 接收数据7 = 编程8 = 断开9 = 总线测试10 = 睡眠11-14 = 保留15 = 保留(I/O 模式)</td><td>当收到命令时卡的状态。如果命令的执行导致状态的变化,这个变化将会在下个命令的响应中反映出来。这四个位按十进制数0 至 15 解释。睡眠状态只在 e•MMC 卡中。</td><td>B</td></tr><tr><td>8</td><td>READY_FOR_DATA</td><td>SX</td><td>'0' = 未就绪'1' = 就绪</td><td>与总线上的缓冲器空的信号一致。</td><td>A</td></tr><tr><td>7</td><td>SWITCH_ERROR</td><td>EX</td><td>'0' = 无错误'1' = 切换错误</td><td>如果置位,卡没有通过 SWITCH 命令切换到期望的模式。</td><td>B</td></tr><tr><td>6</td><td colspan="5">保留</td></tr><tr><td>5</td><td>APP_CMD</td><td>SR</td><td>'0' = 使能'1' = 失能</td><td>卡期望 ACMD,或指示命令已经被解释为 ACMD 命令。</td><td>C</td></tr><tr><td>4</td><td colspan="5">保留</td></tr><tr><td>3</td><td>AKE_SEQ_ERROR</td><td>ER</td><td>'0' = 无错误'1' = 错误</td><td>仅针对 SD 存储卡。验证过程的顺序有错误。</td><td>C</td></tr><tr><td>2</td><td colspan="5">保留给与应用特定命令。</td></tr><tr><td>[1:0]</td><td colspan="5">保留给厂商测试模式。</td></tr></table>

# SD状态寄存器

在 SD 状态寄存器中含有与 SD 存储卡的专有特征相关的状态位，并且可以被用于未来的特定应用使用。SD状态寄存器是一个512 比特大小的数据块。该寄存器的内容连同一个 16位CRC通过 DAT 总线被发送到主机上。SD 状态通过 DAT 总线被发送到主机上，作为 ACMD13 的响应（CMD55 接着用 CMD13）。ACMD13 只能在“传送状态”被发送到存储卡（卡被选中）。SD 状态结构将在下面描述。

“类型”和“清除条件”的缩写与上述卡状态描述相同。


表 36-32. SD 状态


<table><tr><td>位</td><td>标识符</td><td>类型</td><td>数值</td><td>描述</td><td>清除条件</td></tr><tr><td>[511: 510]</td><td>DAT_BUS_WIDTH</td><td>SR</td><td>'00'=1(默认)‘01'=保留‘10'=4位宽‘11'=保留</td><td>由SET_BUS_WIDTH命令显示当前定义的数据总线宽度</td><td>A</td></tr><tr><td>509</td><td>SECURED_MODE</td><td>SR</td><td>'0'=未处于安全模式'1'=处于安全模式</td><td>卡处于操作的安全模式(参考“SD安全规范”)。</td><td>A</td></tr><tr><td>[508: 496]</td><td colspan="5">保留</td></tr><tr><td>[495: 480]</td><td>SD_CARD_TYPE</td><td>SR</td><td>下列卡目前被定义为:'0000'=通用 SD读/写卡'0001'=SD ROM卡'0002'=OTP</td><td>低8位在未来被用来定义SD存储卡的不同变种(每个位将定义不同的SD卡类型)。高8位将被用来定义不符合当前SD物理层规范的SD卡。</td><td>A</td></tr><tr><td>[479:448]</td><td>SIZE_OF_PROTECTED_AREA</td><td>SR</td><td>受保护区域的大小。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[447: 440]</td><td>SPEED_CLASS</td><td>SR</td><td>卡的速度类型。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[439: 432]</td><td>PERFORMANCE_MOVE</td><td>SR</td><td>以1MB/s为单位的传输性能。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[431: 428]</td><td>AU_SIZE</td><td>SR</td><td>AU大小</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[427: 424]</td><td colspan="5">保留</td></tr><tr><td>[423: 408]</td><td>ERASE_SIZE</td><td>SR</td><td>一次要被擦除的AU数目。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[407: 402]</td><td>ERASE_TIMEOUT</td><td>SR</td><td>UNIT_OF_ERASE_AU指定的擦除区域的超时时间。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[401: 400]</td><td>ERASE_OFFSET</td><td>SR</td><td>擦除时间增加固定偏移值。</td><td>(见下面描述)</td><td>A</td></tr><tr><td>[399: 312]</td><td colspan="5">保留</td></tr><tr><td>[311: 0]</td><td colspan="5">保留给生产厂商</td></tr></table>

# SIZE_OF_PROTECTED_AREA

对于标准容量卡（SDSC）和高容量卡（SDHC/SDXC）设置该位域不同。

对于标准容量卡（SDSC），受保护区域容量计算方式如下：

受保护区域 = SIZE_OF_PROTECTED_AREA* MULT * BLOCK_LEN。

SIZE_OF_PROTECTED_AREA 以 MULT*BLOCK_LEN 为单位。

对于高容量卡（SDHC/SDXC），受保护区域容量计算方式如下：

受保护区域 = SIZE_OF_PROTECTED_AREA 。

SIZE_OF_PROTECTED_AREA 以字节为单位。

# SPEED_CLASS

这 8 位字段表示速度等级。

00h: Class 0 

01h: Class 2 

02h: Class 4 

03h: Class 6 

04h: Class 10 

05h–FFh: 保留

# PERFORMANCE_MOVE

这 8 位域指示 Pm，该值可被设为以 1MB/秒为单位。如果卡不用 RU 移动数据，应该认为 Pm

是无穷大。设置这个域为 FFh 表示无穷大。Pm 的最小值由 36-33. 中定义。


表 36-33. 移动性能字段


<table><tr><td>PERFORMANCE_MOVE</td><td>数值定义</td></tr><tr><td>00h</td><td>顺序写入</td></tr><tr><td>01h</td><td>1 [MB/sec]</td></tr><tr><td>02h</td><td>2 [MB/sec]</td></tr><tr><td>......</td><td>......</td></tr><tr><td>FEh</td><td>254 [MB/sec]</td></tr><tr><td>FFh</td><td>无穷大</td></tr></table>

# AU_SIZE

这 4 位字段指示 AU 大小，数值是 16K 字节为单位 2 的幂次的倍数。


表 36-34. AU_SIZE 字段


<table><tr><td>AU_SIZE</td><td>数值定义</td></tr><tr><td>0h</td><td>未定义</td></tr><tr><td>1h</td><td>16 KB</td></tr><tr><td>2h</td><td>32 KB</td></tr><tr><td>3h</td><td>64 KB</td></tr><tr><td>4h</td><td>128 KB</td></tr><tr><td>5h</td><td>256 KB</td></tr><tr><td>6h</td><td>512 KB</td></tr><tr><td>7h</td><td>1 MB</td></tr><tr><td>8h</td><td>2 MB</td></tr><tr><td>9h</td><td>4 MB</td></tr><tr><td>Ah</td><td>8 MB</td></tr><tr><td>Bh</td><td>12 MB</td></tr><tr><td>Ch</td><td>16 MB</td></tr><tr><td>Dh</td><td>24 MB</td></tr><tr><td>Eh</td><td>32 MB</td></tr><tr><td>Fh</td><td>64 MB</td></tr></table>

最大 AU 大小，取决于卡的容量，由 36-34. AU_SIZE 中定义。卡可以任意的设置 AU大小（由 36-35. AU 定义），只要小于或等于该卡容量所允许的最大 AU 大小。卡应该尽可能小地设置 AU 尺寸。


表 36-35. 最大 AU 大小


<table><tr><td>卡容量</td><td>最大 64MB</td><td>最大 256MB</td><td>最大 512MB</td><td>最大 32GB</td><td>最大 2TB</td></tr><tr><td>最大 AU 大小</td><td>512 KB</td><td>1 MB</td><td>2 MB</td><td>4 MB</td><td>64MB</td></tr></table>

# ERASE_SIZE

这 16 位字段表示 NERASE。当 NERASE个数的 AU 被擦除，超时时间由 ERASE_TIMEOUT 规定（参考 ERASE_TIMEOUT）。主机应确定在一次操作中要被擦除的 AU 的适当数目，以便主机可以预示擦除操作的进度。如果该字段设置为 0，则不支持擦除的超时计算。


表 36-36. 擦除大小字段


<table><tr><td>ERASE_SIZE</td><td>数值定义</td></tr><tr><td>0000h</td><td>不支持擦除的超时计算。</td></tr><tr><td>0001h</td><td>1 AU</td></tr><tr><td>0002h</td><td>2 AU</td></tr><tr><td>0003h</td><td>3 AU</td></tr><tr><td>......</td><td>......</td></tr><tr><td>FFFFh</td><td>65535 AU</td></tr></table>

# ERASE_TIMEOUT

这 6 位字段表示 TERASE，当 ERASE_SIZE 指示的多个 AU 被擦除时，这个数值给出了从偏移量算起的擦除超时时间。ERASE_TIMEOUT 的范围可以被定义为最多 63 秒，卡的制造商可以 根 据 具 体 实 现 选 择 ERASE_SIZE 和 ERASE_TIMEOUT 的 任 意 组 合 。 一 旦ERASE_TIMEOUT 被确定下来，那么 ERASE_SIZE 也确定了。主机可以通过以下公式计算任意数目的 AU 的擦除超时时间：

$$
\text { Erase   timeout   of   X   AU } = \frac {T _ {\text { ERASE }}}{N _ {\text { ERASE }}} * X + T _ {\text { OFFSET }}
$$

（式 36-1）


表 36-37. 擦除超时字段


<table><tr><td>ERASE_TIMEOUT</td><td>数值定义</td></tr><tr><td>00</td><td>不支持擦除的超时计算</td></tr><tr><td>01</td><td>1 秒</td></tr><tr><td>02</td><td>2 秒</td></tr><tr><td>03</td><td>3 秒</td></tr><tr><td>......</td><td>......</td></tr><tr><td>63</td><td>63 秒</td></tr></table>

如果 ERASE_SIZE 字段被设置为 0，则该字段应该设置为 0。

# ERASE_OFFSET

这 2 位字段表示 TOFFSET，可以选择如 36-38. 所示的四个数值之一。若ERASE_SIZE 和 ERASE_TIMEOUT 字段都设为 0，该字段无意义。


表 36-38. 擦除偏移字段


<table><tr><td>ERASE_OFFSET</td><td>数值定义</td></tr><tr><td>0h</td><td>0 秒</td></tr><tr><td>1h</td><td>1 秒</td></tr><tr><td>2h</td><td>2 秒</td></tr><tr><td>3h</td><td>3 秒</td></tr></table>

# 36.5. 编程序列

# 36.5.1. 卡识别

主机复位后进入卡识别模式，寻找总线上的新卡。在卡识别模式下，主机复位所有的卡，验证工作电压范围，识别卡并询问每个卡的相对卡地址（RCA）。这个操作是在每个卡自己的命令信号线 CMD 上分别完成的。在卡识别模式中的所有数据通信只使用命令信号线（CMD）。

在卡识别过程中，卡应该工作在时钟频率为 FOD（400 kHz）的情况下。

# 卡复位

命令 GO_IDLE_STATE（CMD0）是软件复位命令，并设置 e•MMC 和 SD 存储卡进入空闲状态（Idle State），不管当前卡的状态是什么。复位命令（CMD0）仅用于存储器或组合卡的存储器部分。为了重置只有 I/O 卡或组合卡的 I/O 部分，使用 CMD52 写 1 到 CCCR 的 RES 位。在非激活状态（Inactive State）的卡不受此命令的影响。

主机上电后，所有的卡都处于空闲状态（Idle State），包括之前已在非激活状态（Inactive State）的卡。上电或 CMD0 后，所有卡的 CMD 线处于输入模式，等待下一个命令的起始位。这些卡都是用缺省的相对卡地址（RCA）初始化，并用默认 400 kHz 的时钟频率驱动器。

# 工作电压范围验证

在主机和卡之间开始通信时，主机可能不知道卡支持的电压，并且卡可能不知道主机能否提供其支持的电压。为了验证电压，下面的命令都在相关规范中定义。

在 协 议 规 范 中 定 义 的 命 令 包 括 ： SEND_OP_COND （ CMD1 用 于 e•MMC ），SD_SEND_OP_COND（ACMD41 用于 SD 存储卡），IO_SEND_OP_COND（CMD5 用于 SDI/O 卡），这些命令提供给主机一种机制去识别和拒绝那些不匹配主机所需的 VDD范围的卡。这是由主机发送所需的 VDD电压窗口作为此命令的操作数来实现的。如果卡不能在指定的范围内进行数据传输，必须从总线断开并进入非激活状态（Inactive State）。否则，该卡将响应返回它的 VDD范围。

如果该卡可以工作在所提供的电压下，响应将返回供电电压和在命令参数中设置的检查模式。

如果该卡不能在提供的电压下工作，它不返回响应，并保持在空闲状态。初始化 SDHC 卡时强制性的在 ACMD41 命令之前发送 CMD8。收到 CMD8 是让该卡知道主机支持物理层 2.00 协议及卡支持高版本的功能。

# 卡识别过程

对于不同的卡，卡的识别过程不同。这些卡包括 e•MMC、SD，或 SD I/O 卡。支持所有类型的SD I/O 卡，即 SDIO_IO_ONLY 卡、SDIO_MEM_ONLY 卡和 SDIO COMBO 卡。卡识别过程步骤如下：

1. 检测卡是否连接。

2. 识别卡的类型：SD 卡、e•MMC 或 SD I/O 卡。

发送 CMD5 命令。如果主机接收到响应，则是 SD I/O 卡；

如果没有响应，发送 ACMD41。如果主机接收到响应，则是 SD 卡；

否则，是 e•MMC 卡。

# 3. 根据卡的类型初始化卡。

使用 FOD （400 KHz）为时钟源，并按照下列命令顺序发送命令：

SD 卡 - 发送 CMD0，ACMD41，CMD2，CMD3；

SDHC 卡 - 发送 CMD0，CMD8，ACMD41，CMD2，CMD3；

SD I/O 卡 - 如果卡没有存储器端口，发送 CMD52，CMD0，CMD5，CMD3；否则，发送 CMD52，CMD0，CMD5，ACMD41，CMD11 （可选），CMD2，CMD3；

e•MMC - 发送 CMD0，CMD1，CMD2，CMD3。

# 36.5.2. 引导操作

如果在上电或复位后（硬件复位或通过参数 0xF0F0F0F0 的 CMD0）发送第一个命令之前将CMD 线拉低 74 时钟周期以上（正常引导模式）或发送了参数为 0xFFFFFFFA 的 CMD0（备用引导模式），卡则识别出启动了引导模式，并开始内部准备引导数据。

主机通过 EXT_CSD 寄存器[179]字节的位[5:3]来选择从哪个分区读取引导数据，主机在引导操作期间可读取的数据长度可按 128KB x BOOT_SIZE_MULT（EXT_CSD 寄存器的[226]字节）计算。

主机通过 EXT_CSD 寄存器[177]字节的位[4:3]设置合适的值，来选择向后兼容接口时序的单倍数据率模式或选择高速接口时序的 SDR 或 DDR（如果支持）。EXT_CSD 寄存器[228]字节的位[2]告诉主机在引导期间设备是否支持高速时序。EXT_CSD 寄存器[228]字节的位[1]告诉主机在引导期间设备是否支持双倍数据率模式。

引导操作期间不支持 HS200 模式。

主机可以通过在 EXT_CSD 寄存器[179]字节的位[6]设置为“1”来选择从卡接收引导确认，这样主机就可以识别卡工作在引导模式下。

如果引导确认被使能，卡必须在 CMD 线被拉低后 50ms 之内向主机发送确认模式“010”。如果引导确认被禁用，卡不发送确认模式“010”。

# 正常引导操作

如果在上电后发送第一个命令之前保持 CMD 线低电平至少 74 个时钟周期，卡将识别引导模式正在启动。SDIO_CMD 线拉低 1 秒之内，卡开始在 SDIO_DAT 线上向主机发送第一个引导数据。主机必须保持 CMD 线为低电平以读取所有引导数据，主机必须采用推挽模式直至引导操作结束。期间主机可以通过拉高 SDIO_CMD 线以终止引导模式。


图 36-16. 引导操作时序


![image](images/138f54ecddd2.jpg)


执行正常的引导过程，要按照以下步骤操作：

1. 复位卡或给卡上电。

2. 如果使能引导确认（ACK），需要使能 ACKEN，设置 ACKTIME，并使能 ACKFAIL 和 ACKTO标志。

3. 通过置位 DATADIR 来使能接收数据，并设置接收的引导数据的字节数 DATALEN。使能DTTMOUT、DTEND 和 CMDSEND 中断，用于完成引导命令确认。

4. 通过设置 BOOTMOD = 0 选择正常引导操作模式，并通过 BOOTMODEN 使能启动。ACK引导确认超时被启用，且 CMD 线保持低电平。

5. ACKTO 或 ACKFAIL 标志可用于检测是否收到引导确认。

如果没有及时收到引导确认时，将出现 ACKTO 标志。

如果没有收到正确的引导确认时，将出现 ACKFAIL 标志。

6. 当接收到所有引导数据时，将出现 DTEND 标志。

当数据 CRC 失败时，会生成 DTCRCERR 标志。

当发生接收数据超时时，会生成 DTTMOUT 标志。

7. 当接收到最后一个数据时，从 FIFO 读取数据直到 FIFO 为空（RFE = 1），之后将生成数据结束标志（DTEND）。

8. 通过清零 BOOTMODEN 位来终止引导过程，这会导致 SDIO_CMD 线变为高电平。在 56个时钟之后将生成 CMDSEND 标志，用于指示引导过程结束，卡已准备好接收新命令。

# 备用引导操作

卡在上电或复位后，如果主机在 74 时钟周期之后，发送 CMD1 之前，发送了参数为0xFFFFFFFA 的 CMD0，则卡识别出备用的引导模式被启动，并内部开始准备引导数据。在主机发送带参数 0xFFFFFFFA 的 CMD0 后的 1 秒内，卡开始在 SDIO_DAT 线上发送第一个引导数据。主机可以通过发送 CMD0（复位）来终止引导操作。


图 36-17. 备用的引导操作时序


![image](images/afdf69784ed6.jpg)


执行备用的引导操作，要按照以下步骤操作：

1. 复位卡或给卡上电。

2. 如果要使能引导 ACK，需要通过使能 ACKEN，设置 ACKTIME，并使能 ACKFAIL 和 ACKTO标志。

3. 通过置位 DATADIR 来使能接收数据，并设置接收的引导数据的字节数 DATALEN。使能DTTMOUT 和 DTEND 标志。

4. 通过设置 BOOTMOD = 1 来选择备用的引导操作模式，设置命令寄存器装载参数为0xFFFFFFFA 的 CMD0。使能 CMDSEND 标志以指示完成引导命令确认，通过 BOOTMODEN使能引导，并且设置 CSMEN 为 1。ACK 引导确认超时被启用，且 CMD 线保持低电平。当命令被发送时，将生成 CMDSEND 标志位，此时 BOOTMODEN 位应清零。

5. ACKTO 或 ACKFAIL 标志可用于检测是否收到引导确认。

如果没有及时收到引导确认时，将出现 ACKTO 标志。

如果没有收到正确的引导确认时，将出现 ACKFAIL 标志。

6. 当接收到所有引导数据时，将出现 DTEND 标志。

当数据 CRC 失败时，会生成 DTCRCERR 标志。

当接收数据发生超时时，会生成 DTTMOUT 标志。

7. 当接收到最后一个数据时，从 FIFO 读取数据直到 FIFO 为空（RFE=1），之后将生成数据结束 DTEND 标志。

8. 通过发送 CMD0 来终止备用的引导操作之前需要清零 BOOTMODEN 位，这会导致 56 个时钟之后生成 CMDSEND 标志。该标志用于指示引导过程结束，卡已准备好接收新命令。当CMD0（复位）被成功发送，BOOTMOD 位必须被清除才能终止备用的引导操作。

# 36.5.3. 无数据命令

发 送 任 何 无 数 据 命 令 时 ， 软 件 需 要 用 适 当 的 参 数 设 置 SDIO_CMDCTL 寄 存 器 和SDIO_CMDAGMT 寄存器。通过这两个寄存器，主机形成命令，并将其发送到命令总线上。主机通过 SDIO_STAT 寄存器的错误标志来反映命令响应的错误。

当接收到响应时，主机设置 SDIO_STAT 寄存器 CMDRECV（CRC 校验通过）位或 CCRCERR（CRC 校验失败）位为 1。短响应被复制到 SDIO_RESP0，而长响应被复制到所有四个响应寄存器。SDIO_RESP3 寄存器的第 31 位代表的长响应的最高位，而 SDIO_RESP0 寄存器的第 0 位表示长响应最低位。

# 36.5.4. 单个数据块或多个数据块写

在发送块写入命令（CMD24 - CMD27）时，一个或多个数据块从主机传到卡。数据块由起始位（1 位或 4 位低电平），数据块，CRC 和结束位（1 位或 4 位高电平）组成。如果 CRC 失败，则卡通过 SDIO_DAT 线指示传输失败，传送数据被丢弃而不写入，并且后续发送的数据块将被忽略。

如果主机传输的部分数据累积长度不是数据块对齐，并且块错位是不允许的（未设置 CSD 参数 WRITE_BLK_MISALIGN），卡将在第一个未对齐块的开始之前检测块错位错误（设置状态寄存器的 ADDRESS_ERROR 错误位），并同时忽略后续的数据传输。如果主机试图写一个写保护区的数据，写操作也将被终止。在这种情况下，卡将设置状态寄存器中 WP_VIOLATION位。

设置 CID 和 CSD 寄存器不需要先设置块长度，传送的数据也通过 CRC 保护。如果 CSD 或CID 寄存器的一部分被存储在 ROM 中，那么不可改变部分必须与接收缓冲区的对应部分相匹配。如果匹配失败，卡将报告一个错误同时不改变任何寄存器的内容。

一些卡可能需要很长的或者不可预测的时间写入一个数据块。接收一个数据块并完成 CRC 校验后，卡将开始写操作，如果写缓冲区已满则保持 DAT0 线拉低，并且无法通过新的命令WRITE_BLOCK 接收新的数据。主机可以在任何时间用 SEND_STATUS 命令（CMD13）查询卡的状态，并且卡将返回当前状态。状态位 READY_FOR_DATA 表示卡是否可以接受新的数据或写入操作是否仍在进行中。主机可以通过发出CMD7命令不选中该卡（选择另外的卡），将该卡置于断开状态（Disconnect State），并释放 DAT 信号线而不中断写操作。当重新选择卡，如果写操作仍在进行中并且写缓冲区不可用，它会拉低 DAT 信号线重新激活忙指示。

对于 SD 卡。设置一些块被预擦除（ACMD23）操作将使多块写操作比没有 ACMD23 操作更快。主机将使用此命令来定义下一次操作将会有多少个数据块被发送。

单块或多块写操作步骤为：

1. 在 SDIO_DATALEN 寄存器中设置数据大小（以字节为单位）。

2. 在 SDIO_DATACTL 寄存器中设置数据块大小（BLKSZ，以字节为单位）；主机每次发送BLKSZ 大小的数据块。

3. 在 SDIO_CMDAGMT 寄存器中设置数据应该被写入的地址。

4. 设置 SDIO_CMDCTL 寄存器。对于 SD 存储卡和 e•MMC 卡，使用 CMD24 命令为单块写和 CMD25 命令为多块写。对于 SD I/O 卡，使用 CMD53 命令来进行单块和多块传输。

5. 将数据写入 SDIO_FIFO。

6. 软件应查询数据错误中断。如果需要，软件可以通过发送停止命令（CMD12）终止数据传输。

7. 当收到 DTEND 中断时，数据传送结束。对于开放式的块传输，如果字节计数为 0，则软件必须发送 STOP 命令。如果字节计数不为 0，则在给定的字节数传送结束时，主机应该发送停止命令。

# 36.5.5. 单个数据块或多个数据块读

读 数 据 块 是 基 于 块 的 数 据 传 输 。 数 据 传 输 的 基 本 单 位 是 块 ， 最 大 块 大 小 在 CSD（READ_BL_LEN）中被定义，块的大小始终是 512 字节。如果 READ_BL_PARTIAL（在 CSD中）被设置时，更小的块也可以被传输，其开始和结束地址被完全包含在 512 个字节的边界中。

CMD17（READ_SINGLE_BLOCK）表示开始读一个数据块，完成传输后卡返回发送状态。CMD18（READ_MULTIPLE_BLOCK）开始读连续的数据块。为了确保数据传输的完整性，每个数据块后都有一个 CRC 校验。

块长度由 CMD16 设置，可以设置为 512 字节而忽略 READ_BL_LEN 的设置。

数据块将不断传输，直到主机发出 STOP_TRANSMISSION 命令（CMD12）。由于串行命令传

输原因，停止命令有一个执行的延迟。在停止命令的结束位之后停止数据传输。

当使用 CMD18 读到用户区的最后一个块时，主机应该忽略可能会出现的 OUT_OF_RANGE错误，即使序列是正确的。

如果主机传输的部分块的累积长度不是块对齐并且不允许块错位，卡将在第一个未对齐块的开始检测出块错位，并设置状态寄存器的 ADDRESS_ERROR 错误位，中断传输和等待在数据状态的停止命令。

单块或多块读操作步骤为：

1. 在 SDIO_DATALEN 寄存器中设置数据大小的字节数。

2. 在 SDIO_DATACTL 寄存器中设置块大小（BLKSZ）。主机每次从卡中读取 BLKSZ 大小的数据。

3. 在 SDIO_CMDAGMT 寄存器中设置需要读取数据的开始地址。

4. 设置SDIO_CMDCTL寄存器。对于SD 和e•MMC卡，使用CMD17用于单块读取和CMD18为多块读取。对于 SD I/O 卡，使用 CMD53 用于单块和多块传输。

5. 软件应查询数据错误中断。如果需要，软件可以通过发送停止命令（CMD12）终止数据传输。

6. 软件应从 FIFO 中读数据，并腾出 FIFO 的空间用于接收更多的数据。

7. 当收到 DTEND 中断时，软件应读出 FIFO 中剩余的数据。

# 36.5.6. 数据流写和数据流读（仅适用于 e•MMC）

# 数据流写

数据流写（CMD20）开始从主机将数据传送到卡，从起始地址开始，直到主机发出停止命令。如果允许部分块传输（如果 CSD 参数 WRITE_BL_PARTIAL 被设置），数据流可以在卡地址空间内的任何地址启动和停止，否则应仅在块边界启动和停止。由于不预先确定要传输的数据量，CRC 不能使用。

如果主机提供了一个超出范围的地址作为参数传递给 CMD20，卡将拒绝该命令，留在传输状态，并将 ADDRESS_OUT_OF_RANGE 置位。

需要注意的是数据流写命令只适用于 1 位总线配置（DAT0 信号线上）。如果 CMD20 在其它总线配置中发出的，它被认为是非法的命令。

为了使卡保持在流模式的数据传输，接收数据所花费的时间（由总线时钟速率定义）必须比它需要写入到主存储器字段（由卡定义在 CSD 寄存器）的时间少。因此，流写入操作最大的时钟频率由下面给出的公式计算：

$$
\text { max   write   frequency } = \min \left(\text { TRAN\_SPEED }, \frac {8 * 2 ^ {\text { WRITE\_BL\_LEN }} - 1 0 0 * \text { NSAC }}{\text { TAAC } * \text { R2W\_FACTOR }}\right) \tag {式36-2}
$$

其中，TRAN_SPEED：最大的总线时钟频

WRITE_BL_LEN：最大写数据块长度

NSAC：以 CLK周期计算的数据读访问时间 2

TAAC：数据读访问时间 1

R2W_FACTOR：写速度因子

所有的参数在 CSD 寄存器中定义。如果主机试图使用更高频率，卡可能不能够对数据进行处理，并将停止编程，同时忽略所有后续的数据传输并等待（在接收数据状态）一个停止指令。由于主机发送 CMD12，该卡将 TXURE 位置位并返回传输状态。

# 数据流读

由 READ_DAT_UNTIL_STOP（CMD11）控制数据流的数据传输。此命令指示卡从指定地址发送数据，直到主机发送一个 STOP_TRANSMISSION（CMD12）命令。由于串行命令传输停止的原因，命令有一个执行的延迟。停止命令的结束位之后数据传输停止。

如果主机提供了一个超出范围的地址作为参数传递给 CMD11，该卡将拒绝该命令，留在传输状态，并将 ADDRESS_OUT_OF_RANGE 位置位。

需要注意的是数据流读取命令只工作在 1 位总线配置（DAT0 信号线）。如果 CMD11 在其它总线配置中发出的，它被认为是非法的命令。

如果数据传输的地址到达存储范围的结束处时，主机还没有发送停止命令，则后续传输的有效载荷的内容是不确定的。由于主机发送 CMD12 命令，卡将 ADDRESS_OUT_OF_RANGE 位置位并返回传输状态。

为了使卡保持在流模式的数据传输，传输数据所花费的时间（由总线时钟速率定义）必须比它需要从主存储器字段（在 CSD 寄存器中由卡定义）读出的时间少。因此，流读取操作最大的时钟频率由下面给出的公式计算：

$$
\text { max   read   frequency } = \min \left(\text { TRAN\_SPEED }, \frac {8 * 2 ^ {\text { READ\_BL\_LEN }} - 1 0 0 * \text { NSAC }}{\text { TAAC } * \text { R2W\_FACTOR }}\right) \tag {式36-3}
$$

其中，TRAN_SPEED: 最大总线时钟频率

READ_BL_LEN: 最大读数据块长度

NSAC: 以 CLK 周期计算的数据读访问时间 2

TAAC: 数据读访问时间 1

R2W_FACTOR: 写速度因子

所有的参数在 CSD 寄存器中定义。如果主机试图使用更高频率，卡可能不能够对数据进行处理，并将停止编程，同时忽略所有后续的数据传输并等待（在接收数据状态）一个停止指令。由于主机发送 CMD12，该卡将 RXORE 位置位并返回传输状态。

# 36.5.7. 擦除

SD/e•MMC 存储卡的可擦除单位是“擦除组”，擦除组是以写数据块计算的，写数据块是卡的基本写入单元。擦除组的大小是一个卡特定的参数，在 CSD 中定义。

主 机 可 以 擦 除 连 续 范 围 的 擦 除 组 。 开 始 擦 除 操 作 有 三 个 步 骤 。 首 先 ， 主 机 使 用ERASE_GROUP_START（CMD35）/ ERASE_WR_BLK_START（CMD32）命令定义了连续范围内的开始地址，然后使用 ERASE_GROUP_END（CMD36）/ ERASE_WR_BLK_END（CMD33）命令定义了连续范围内的结束地址，最后发送 ERASE（CMD38）命令启动擦除操作。在擦除命令中的地址字段是以字节为单位的擦除组地址。卡会舍弃未与擦除组大小对齐的部分，把地址边界对齐到擦除组的边界。

如果未按照定义的步骤接收到擦除命令（CMD35，CMD36 和 CMD38），卡应设置状态寄存器

的 ERASE_SEQ_ERROR 位，并重置整个序列。

如果主机提供了一个超出范围的地址作为参数传递给 CMD35 或 CMD36，卡将拒绝该命令，同时设置 ADDRESS_OUT_OF_RANGE 位，并重置整个擦除序列。

如果收到“非擦除”命令（既不是 CMD35，CMD36，CMD38 也不是 CMD13），卡应该设置ERASE_RESET 位，重置擦除序列并执行最后一个命令。

如果擦除范围包括写保护块，它们应不被擦除，只有非保护块被擦除。应设置状态寄存器的WP_ERASE_SKIP 状态位。

如上所述，对于块写入，卡将通过保持 DAT0 为低来指示擦除过程正在进行。实际擦除时间可能很长，主机可以发送 CMD7 命令以取消选择该卡。

# 36.5.8. 总线宽度选择

在主机已经验证了总线上的功能引脚后，卡初始化后可以改变总线宽度的配置。

对于 e•MMC 卡，使用 SWITCH 命令（CMD6）。总线宽度的配置是通过在 EXT_CSD 寄存器模式字段的 BUS_WIDTH 字节设置而改变的。上电或软件复位后，BUS_WIDTH 字节的内容为 0x00。如果主机试图写一个无效的值时，BUS_WIDTH 字节不会改变，同时设置SWITCH_ERROR 位，另外该寄存器是只写的。

对于 SD 存储卡，使用 SET_BUS_WIDTH 命令（ACMD6）改变总线宽度。上电或GO_IDLE_STATE 命令（CMD0）后默认总线宽度为 1 位。 SET_BUS_WIDTH（ACMD6）仅在传送状态有效，这表明仅在由 SELECT/DESELECT_CARD （CMD7）命令选择卡之后总线宽度才可以改变。

# 36.5.9. 保护管理

为了允许主机保护数据，使得其不被擦除或改写，有三种卡保护方式：

# CSD 寄存器用于卡保护 （可选的）

通过在CSD寄存器中设置永久或临时的写保护位，整个卡可以被写保护。一些卡通过设置CSD的 WP_GRP_ENABLE 位 支 持 一 组 扇 区 的 写 保 护 。 它 的 大 小 在 CSD 寄存器中的WP_GRP_SIZE 单 元 定 义 。SET_WRITE_PROT 命 令 设 置 指 定 写 保 护 组 的 写 保 护 ，CLR_WRITE_PROT 命令清除指定写保护组的写保护。

高容量 SD 存储卡不支持写保护，不响应写保护命令（CMD28，CMD29 和 CMD30）。

# 写保护开关 （SD 存储卡和SD I/O卡）

在卡的侧面有一个机械的滑动开关，提供给用户设置是否对卡进行写保护。如果滑动片处在窗口打开的位置表明该卡被写保护。如果在窗口关闭的位置则卡没有写保护。

# 卡密码上锁/解锁

卡密码上锁/解锁的保护方式在章节 / 中描述。

# 36.5.10. 卡上锁/解锁操作

密码保护的功能允许主机使用密码锁住卡，当解锁卡的时候也使用该密码。其中密码存储在128 位的 PWD 寄存器当中，密码的长度存储在 PWD_LEN 的 8 位寄存器中。这些寄存器是非易失性的，以至于电源开关不会清除他们。

已经上锁的卡支持所有的基本命令（class 0），ACMD41，CMD16 和锁卡命令（class 7）。因此主机可以对卡进行复位，初始化，选择，状态查询，但是无法获取卡上的数据。如果卡之前被设置过密码（PWD_LEN 的值为 0），卡在每次上电后会自动上锁。

与存在的 CSD 寄存器写命令相同，上锁/解锁命令也只在卡的传输态有效。这意味着，上锁/解锁命令不包含地址参数，且必须在使用该命令前卡必须被选中。

卡上锁/解锁命令与卡单块写命令有着相同的结构和总线事务类型。传输的数据块包含命令所有需要的信息（密码设置模式，密码本身，卡上锁/解锁等）。 36-39. / 为上锁/解锁命令的结构。


表 36-39. 上锁/解锁数据结构


<table><tr><td>Byte</td><td>Bit 7</td><td>Bit 6</td><td>Bit 5</td><td>Bit 4</td><td>Bit 3</td><td>Bit 2</td><td>Bit 1</td><td>Bit 0</td></tr><tr><td>0</td><td colspan="4">保留(全设置为0)</td><td>ERASE</td><td>LOCK_UNLOCK</td><td>CLR_PWD</td><td>SET_PWD</td></tr><tr><td>1</td><td colspan="8">PWDS_LEN</td></tr><tr><td>2</td><td rowspan="3" colspan="8">密码数据(PWD)</td></tr><tr><td>......</td></tr><tr><td>PWDS_LEN+1</td></tr></table>

ERASE：该位为 1 时定义了强制擦除操作。字节 0 的位 3 将被设为 1（其他位应为 0）。所有该命令的其他字节将被卡忽略。

LOCK/UNLOCK：1 = 上锁，0 = 解锁。注意，此位可以和 SET_PWD 一起设置，不可以和CLR_PWD 一起设置。

CLR_PWD：1 = 清除 PWD.

$S E 7 \_ P W D : 1 = \dot { \chi } \underline { { \nabla } } \underline { { \Psi } } \dot { \big | } H \dot { \big | } H \dot { \big | } H \underline { { J } } \dot { \big | } H \dot { \big | } P W D$ 

PWDS_LEN：定义密码长度（字节）。在改变密码的情况下，这个长度应该是新旧密码长度之和。密码长度可达 16 个字节。在密码替换的情况下，新旧密码长度总和可达 32 个字节。

密码数据（PWD）: 在设置一个新密码的情况下，它包含这个新的密码。如果修改密码，它包含旧的密码，后面是设置的新密码。

# 设置密码

如果卡之前未被选中，使用 CMD7 选中卡。

⚫ 使用 CMD16 定义数据块长度，8 位卡上锁/解锁模式，8 位密码长度（字节为单位），新密码的字节数。在密码替换完成的情况下，块的大小应考虑新旧密码都会与命令一起被发送出去。

⚫ 在数据线上，以合适的数据块大小发送卡上锁/解锁命令，包含 16 位的 CRC。数据块应指示模式（SET_PWD），密码长度（PWDS_LEN）和密码本身。在密码替换完成的情况下，密码长度值（PWDS_LEN）应为新旧密码长度之和，密码数据字段应包括旧的密码

（当前使用），后面是新的密码。需要注意的是卡需要内部处理新密码长度的计算，通过从 PWDS_LEN 字段减去旧密码长度。

⚫ 当发送的旧密码不正确（大小和内容不相同），状态寄存器中的 LOCK_UNLOCK_FAILED会被置位，并且旧的密码不会改变。如果发送的旧密码正确（大小和内容相同），新的密码数据及其长度会分别保存在 PWD 和 PWD_LEN 中。

# 复位密码

如果卡之前未被选中，使用 CMD7 选中卡。

⚫ 使用 CMD16 定义数据块长度，8 位卡上锁/解锁模式，8 位密码长度（字节为单位），当前使用的密码的字节数。

⚫ 在数据线上，以合适的数据块大小发送卡上锁/解锁命令，包含 16 位的 CRC。数据块指示模式（SET_PWD），密码长度（PWDS_LEN）和密码本身。如果 PWD 和 PWD_LEN的内容与发送的密码和其大小匹配，PWD 寄存器的内容会被清除，同时 PWD_LEN 被设为 0。如果密码不正确，状态寄存器中的 LOCK_UNLOCK_FAILED 会被置位。

# 卡上锁

如果卡之前未被选中，使用 CMD7 选中卡。

⚫ 使用 CMD16 定义数据块长度，8 位卡上锁/解锁模式，8 位密码长度（字节为单位），当前使用的密码的字节数。

⚫ 在数据线上，以合适的数据块大小发送卡上锁/解锁命令，包含 16 位的 CRC。数据块指示 LOCK 模式，密码长度（PWDS_LEN）和密码本身。

如果 PWD 内容等于发送的密码，卡将会被上锁，并且状态寄存器中卡上锁状态位（CARD_IS_LOCKED）会被置位。如果密码不正确，状态寄存器中 LOCK_UNLOCK_FAILED会被置位。

# 卡解锁

如果卡之前未被选中，使用 CMD7 选中卡。

⚫ 使用 CMD16 定义数据块长度，8 位卡上锁/解锁模式，8 位密码长度（字节为单位），当前使用的密码的字节数。

⚫ 在数据线上，以合适的数据块大小发送卡上锁/解锁命令，包含 16 位的 CRC。数据块指示UNLOCK 模式，密码长度（PWDS_LEN）和密码本身。

如果 PWD 内容等于发送的密码，卡将会被解锁，并且状态寄存器中卡上锁状态位（CARD_IS_LOCKED）会被清除。如果密码不正确，状态寄存器中 LOCK_UNLOCK_FAILED会被置位。

# 36.5.11. 睡眠

e•MMC卡可以通过CMD5在睡眠模式和待机模式之间切换。在睡眠状态下，卡的功耗最小化，此时可以关闭 VCC电源。

– 睡眠命令：CMD15 的参数的第 15 位为 1.

– 唤醒命令：CMD15 的参数的第 15 位为 0.

睡眠命令用于启动从待机状态到睡眠状态的状态转换。卡通过下拉 SDIO_DAT0 线来指示过渡阶段繁忙。在繁忙期间不应该发送其他命令。当卡停止下拉 SDIO_DAT0 线时，则达到睡眠状态，完成了状态的转换。

唤醒命令用于启动从睡眠状态到待机状态的状态转换。卡通过下拉 SDIO_DAT0 线来指示过渡阶段繁忙。在繁忙期间不应该发送其他命令。当卡停止下拉 SDIO_DAT0 线时，则达到了待机状态，完成了状态的转换。

设置卡睡眠，需要遵从以下步骤：

1. 使能 DAT0BSYEND 中断。

2. 发送 CMD5（睡眠命令）。

3. 当 DAT0BSYEND 中断出现，则卡处于睡眠状态。

4. 允许关闭 Vcc 电源。

设置卡进入待机状态，需要遵从以下步骤：

1. 打开 Vcc 电源且等待卡进入最小工作电压。

2. 使能 DAT0BSYEND 中断。

3. 发送 CMD5（唤醒命令）

4. 当 DAT0BSYEND 中断产生时，则卡已经处于待机状态。

在睡眠状态期间，Vcc 电源可能会关闭。这是为了进一步节省系统功耗。Vcc 电源只允许在达到到睡眠状态（卡已停止下拉 SDIO_DAT0 线）后，才允许关闭。在允许启动从睡眠状态到待机状态的状态过渡（唤醒命令）之前，Vcc 电源必须至少提高到最小工作电压水平。


图 36-18. CMD5 时序


![image](images/7d22ee149469.jpg)


# 36.5.12. CMD12 发送时序

CMD12 被用于停止或中止数据传输。卡的数据传输在停止传输命令的结束位后 2 个时钟周期后终止。

所有的读写命令都可以在任何时间被停止传输命令 CMD12 中止。如果数据传输正在进行，CMD12 的发送时序需要遵从以下流程：

1. 在寄存器中配置 CMD12 命令并且置位 TRSTOP 寄存器。当 DSM 收到命令，CSM 将产生中止信号。

2. 清零 WAITDEND 寄存器位。

3. 当 IDMAEN = 0 时，则置位 FIFOREST 位。

主机发送数据，当 CMDRECV 标志出现时，固件将停止传输数据到 FIFO。随后置位FIFOREST 并且刷新 FIFO。

主机接收数据，当 CMDRECV 标志出现时，固件将从 FIFO 读取剩余的数据。随后置位FIFOREST。

4. 当 IDMAEN = 1 时，硬件将操作 FIFO。

主机发送数据，当中止信号出现时，硬件将停止 IDMA。随后刷新 FIFO。

主机接收数据，当中止信号出现时，硬件将通过IDMA将FIFO中剩余的数据传输到RMA。

5. 当 FIFO 是空或者复位状态，将生成 DATABOR 标志。


表 36-40. CMD12 的用法


<table><tr><td>数据操作类型</td><td>CMD12 的作用</td></tr><tr><td>预定块数的多块写</td><td>卡接收完需求块数的数据块,然后停止传输并返回卡的传输状态。在多块写末尾的 CMD12 停止命令不是必要的,除非发生错误。</td></tr><tr><td>预定块数的多块读</td><td>卡传送完需求块数的数据块,然后停止传输并返回卡的传输状态。在多块读末尾的 CMD12 停止命令不是必要的,除非发生错误。</td></tr><tr><td>开放终点的多块写</td><td>多块写的块数没有定义,卡将一直接收并写数据直到收到 CMD12 的停止命令。</td></tr><tr><td>开放终点的多块读</td><td>多块读的块数没有定义,卡将一直接收并读数据直到收到 CMD12 的停止命令。</td></tr><tr><td>流写入</td><td>通过发送 CMD12 停止命令来停止或中止数据传输。</td></tr><tr><td>流读取</td><td>通过发送 CMD12 停止命令来停止或中止数据传输。</td></tr></table>

# 块操作中 CMD12的使用

要在数据结束时停止块传输，需要在最后一个数据块结束位之后发送 CMD12 结束位.

当写数据到卡时，需要在写数据的 CRC 令牌结束位之后发送 CMD12 结束位。CMD12 传送过程应遵循块传输时序。

停止开放终点的多块写操作遵循以下步骤：

1. 开始数据传输前设置 TRANSMOD[1:0]为“11”。

2. 等待 DTEND 标志置位，DSM 发送的数据不会超过 SDIO_DATALEN。

3. CSM 发送 CMD12，卡被设置为空闲状态。

当从卡读取数据时，CMD12 的结束位应该尽早发送，即在卡读取数据块的最后一位时发送。

停止开放终点的多块读操作遵循如下步骤：

1. 在开始数据传输前设置 TRANSMOD[1:0]为“11”。

2. 等 待 DTEND 标 志 置 位 ， 即 使 卡 发 送 更 多 的 数 据 ，DSM 接 收 的 数 据 不 会 超 过SDIO_DATALEN。

3. CSM 发送 CMD12。卡发送数据被中止且被设置在空闲状态。

# 流操作中 CMD12的使用

要在待传输的最后一个字节之后停止流传输，应在数据流的最后一个字节结束时发送 CMD12结束位时序。请按照以下的流写入步骤操作：

1. 初始化 DSM，设置 TRANSMOD[1:0]为“10”。

2. 置位 TREN，发送 WRITE_DATA_STREAM 命令。

3. 在命令寄存器中预加载 CMD12 命令，置位 TRSTOP 位。

4. 配置 CSM 为仅在 DATALEN 数据长度的最后一笔数据的等待挂起（WAITDEND = 1）结束后发送命令。

5. CSM 发送 CMD12，流数据结束位和命令结束位应对齐。

如果 DATALEN > 5，CMD12 在 CSM 中等待与数据传输结束位对齐。

如果 DATALEN < 5，CMD12 将提前启动，DSM 将保持 WaitS 状态，使数据传输结束位与 CMD12 结束位对齐。

6. 通过清零 WAITDEND位，流数据写入过程可以在任何时候停止。这将导致预加载的 CMD12立即发送并停止流写入过程。


图 36-19. CMD12 影响流操作的时序


![image](images/8ee14e52855d.jpg)


要在流读取的最后一个字节之后停止流传输过程，CMD12 结束位时序应该在数据流的最后一个字节之后发送。

注意：1. CMD12 发送前等待 DTEND=1（数据接收完成），即使卡发送更多的数据，但是 DSM不会读取超过 SDIO_DATALEN 长度的数据。2. 一旦 DATACNT=0，即使卡继续发送数据，SDIO 也不会再接收。

# 36.6. 特定操作

# 36.6.1. UHS-I 电压切换

UHS-I（即超高速总线速度 I 相，包括：SDR12、SDR25、SDR50、 SDR104 和 DDR50）工作在 1.8V 电压下，而卡上电时是 3.3V 的电压启动，所以 UHS-I 模式需要支持 3.3V 到 1.8V的电压切换。当电压切换序列成功完成时，卡将以默认 SDR12 进入 UHS-I 模式，卡输入和输出时序将发生变化。


图 36-20. CMD11 电压切换时序


![image](images/da71542cdd60.jpg)


电压切换时序需要遵循以下流程进行：

1. 在开始电压切换前，SDIO_CLK 时钟频率必须配置在 100kHz-400kHz 范围内。

2. 主机置位电压切换序列使能位（VSEN = 1）开始电压切换，并发送 CMD11。

3. 主机收到卡 R1 类型的命令响应。

如果响应的 CRC 检查通过，电压切换序列将继续，直到电压切换序列完成前主机将不再驱动 CMD 和 SDIO_DAT[3：0]信号线。响应后的若干时钟周期，SDIO_CLK 时钟停止并产生 CLKSTOP 标志。

如果响应的 CRC 检查错误（CCRCERR = 1）或者响应超时（CMDTMOUT = 1），电压切换序列被停止。

4. 在 R1 响应的下一个时钟周期，卡拉低 CMD 线和 SDIO_DAT[3：0]线。

5. 收到 R1 响应后，主机可以使用 DAT0BSY 寄存器位监视 SDIO_DAT0 线。在两个SDIO_CLK 时钟周期后采样 SDIO_D0 线。主机可以读取 DAT0BSY 标志：

当检测到 DAT0BSY 低电平时，主机将电压调节器切换到 1.8V，然后置位寄存器位VSSTART，以指示 SDIO 启动电压切换序列的时序关键部分。硬件通过保持SDIO_CLK 低至少 5ms 来继续停止时钟。

当检测到 DAT0BSY 为高电平时，主机将中止电压切换序列并对卡重新上电。

6. 如果 SDIO_CLK 信号线是低电平时，卡开始将电压切换到 1.8V。

7. SDIO 的硬件将在至少 5ms 后重新启动 SDIO_CLK 时钟。

8. 检测到 SDIO_CLK 切换后的 1ms 内，卡将拉高 CMD 线和 DAT[3：0]线至少 1 个时钟周期后，卡停止驱动 CMD 线和 DAT[3：0]。

9. SDIO 硬件在 SDIO_CLK 重启的 1ms 后，主机采样 SDIO_DAT0 通过 DAT0BSY 位，且生成电压切换关键时序完成（VSEND）标志。

10. 如果生成 VSEND 标志，主机需要读取 DAT0BSY 寄存器位来判断 SDIO_DAT0 线，来确定电压切换序列是否完成：

如果 DAT0BSY 为高，电压切换序列成功完成。

如果 DAT0BSY 为低，电压切换序列失败，主机对卡进行重新上电
