## 34. 高性能数字滤波器（HPDF）

## 34.1 . 简介

GD32G553 内部集成了一种专门用于外部 Σ-Δ 调制器的高性能数字滤波器模块（HPDF）。HPDF支持 SPI 接口和曼彻斯特编码单线接口，通过串行接口可将外部的 Σ-Δ 调制器与 MCU 连接，并对 Σ-Δ 调制器输出的串行数据流进行滤波。此外，HPDF 还支持并行数据流输入功能，实现对内部外设 ADC 或 MCU 内部存储器里的数据进行滤波处理。

## 34.2. 主要特性

 8 个复用数字串行输入通道；

可配置的SPI和曼切斯特接口；

 8 个内部数字并行输入通道；

高达 16 位分辨率的输入；

内部源：ADC 数据或内存（CPU / DMA 写）数据流；

 可配置的 Sinc 滤波器和积分器；

可配置 Sinc 滤波器的阶数、过采样率（抽取率）；;

可配置积分器的采样率

 阈值监视功能；

独立的 Sinc 滤波器，可配置阶数和过采样率（抽取率）；

可配置的数据输入源：串行通道输入数据或 HPDF 输出数据；

 故障监视功能；

拥有 8 位的计数器，用于监视串行通道输入数据流中连续的 0 或 1；

 极值监视器功能；

存储 HPDF 输出数据的最大值和最小值；

 高达 24 位的输出数据分辨率；

 可向外部 Σ-Δ调制器提供时钟信号；

通过 CKOUT 引脚提供可配置的时钟信号；

 具有灵活的转换配置功能；

转换通道分为规则组和注入组；

- 支持多种转换模式和启动模式；

 HPDF 输出数据为有符号格式。

## 34.3. 功能描述

## 34.3.1. HPDF 结构框图

HPDF 的结构框图如 34-1. HPDF 所示。


图 34-1. HPDF 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/9faafa68c11769ae3f70e93b27ef5457d1fb9b399ed7203d36c3d1b00731d4a1.jpg)



HPDF 接口通过 34-1. HPDF 中的引脚实现与外部 Σ-Δ调制器的通信连接。



表 34-1. HPDF 引脚定义


<table><tr><td>引脚</td><td>类型</td><td>描述</td></tr><tr><td>EXTRG[1:0]</td><td>外部触发输入</td><td>外部触发信号源输入引脚,触发信号源为EXTI11和EXTI15,作为注入组触发启动信号HPDF_ITRG[24]和HPDF_ITRG[25]。</td></tr><tr><td>CKOUT</td><td>时钟输出</td><td>HPDF模块的时钟输出信号,给外部的Σ-Δ调制器提供时钟信号。</td></tr><tr><td>CKINx</td><td>时钟输入</td><td>外部Σ-Δ调制器提供给串行接口的时钟信号。</td></tr><tr><td>DATAINx</td><td>数据输入</td><td>外部Σ-Δ调制器通过该引脚向串行通道传输1bit 位的数据流。</td></tr></table>


表 34-2. HPDF 断路连接


<table><tr><td>断路名称</td><td>断路目标</td></tr><tr><td>HPDF_BREAK[0]</td><td>TIMER0 break0 / TIMER14 break0 / TIMER19 break0</td></tr><tr><td>HPDF_BREAK[1]</td><td>TIMER0 break1 / TIMER15 break0 / TIMER19 break1</td></tr><tr><td>HPDF_BREAK[2]</td><td>TIMER7 break0 / TIMER16 break0</td></tr><tr><td>HPDF_BREAK[3]</td><td>TIMER7 break1</td></tr></table>

## 34.3.2. HPDF 开关控制

在正常启动 HPDF 模块时，可通过将 HPDF_CH0CTL 寄存器中的 HPDFEN 置 1，从而全局使能HPDF 模块。然后再将 HPDF_CHxCTL 中的 CHEN 位和 HPDF_FLTyCTL0 中的 FLTEN 位置 1，可分别使能输入通道和通道数字滤波器。此外只要输入通道使能，输入通道会立即开始接收串行数据。

HPDF 在工作期间，可通过将 FLTEN 清零的方式进入停止模式。进入停止模式之后，HPDF 模块正在进行的转换任务都会立即停止，且寄存器的配置保持不变（除 HPDF_FLTySTAT 和HPDF_FLTyTMSTAT 寄存器被复位外）。

在停止模式下，HPDF 系统时钟会自动停止。在停止系统时钟，进入停止模式之前，必须清零HPDFEN 位。

## 低功耗模式

HPDF 模块对降低功耗进行了优化，在正常的工作模式下，当未有执行的转换任务时，滤波器和积分器会自动进入空闲状态，以实现降低功耗的目的。

## 34.3.3. HPDF 时钟

HPDF 的时钟包含驱动内部模块的系统时钟和串行接口使用的串行时钟。

## 系统时钟

HPDF 的系统时钟 f<sub>HPDFCLK</sub>用于驱动通道收发器、数字滤波器、积分器、阈值监视器、故障监视器、极值监视器和控制模块。HPDF 系统时钟源可由 RCU 章节 RCU_CFG1 寄存器中的 HPDFSEL 位进行配置。

## 串行输入时钟

HPDF 的串行接口通过 CKINx 引脚可接收来自外部 Σ-Δ调制器的时钟信号，以此实现接收 Σ-Δ调制器发送的串行数据流。

串行接口使用外部输入时钟会受到时钟频率的限制。如果使用标准的 SPI 接口，系统时钟 f<sub>HPDFCLK</sub>≥ 4f<sub>CKIN</sub>；如果使用曼切斯特编码接口，则需要系统时钟 f<sub>HPDFCLK</sub> ≥ 6f<sub>CKIN</sub>。

## 串行输出时钟

HPDF 支持输出串行时钟的功能，可通过输出的串行时钟驱动与之相连接的 Σ-Δ 调制器。通过HPDF_CH0CTL 寄存器中 CKOUTSEL 位可选择串行输出时钟的时钟源。当 CKOUTSEL=0 时，串行输出时钟源为 HPDF 系统时钟；当 CKOUTSEL=1 时，串行输出时钟源为音频时钟，音频时钟的配置可参考 RCU 章节的 RCU_CFG1 寄存器中的 HPDFAUDIOSEL[1:0]位域配置。

串行输出时钟源确定后，可通过配置 HPDF_CH0CTL 寄存器中的 CKOUTDIV[7:0]位域对输出时钟分频控制。当 CKOUTDIV[7:0]≠0 时，串行输出时钟分频器的值为 CKOUTDIV[7:0]+1。当CKOUTDIV[7:0]=0 时，串行输出时钟被禁止，CKOUT 引脚保持低电平状态。

此外清零 HPDFEN 后，也可实现停止串行输出时钟信号。当串行输出时钟源为系统时钟时（CKOUTSEL=0），清零 HPDFEN，在 4 个系统时钟后停止串行输出时钟。当串行输出时钟源为音频时钟时（CKOUTSEL=1），清零 HPDFEN，在 1 个系统时钟和 3 个音频时钟后停止串行输出时钟。

串行输出时钟源只有在 HPDFEN=0 时，才可修改。为了避免 CKOUT 引脚上产生毛刺信号，软件必须在串行输出时钟停止后修改 HPDF_CH0CTL 寄存器中 CKOUTSEL 位的值。

串行输出时钟的频率的范围为 0-20MHz。

## 34.3.4. 复用串行数据通道

HPDF 有 8 个复用串行数据通道，支持 SPI 编码和曼切斯特编码。通过配置 HPDF_CHxCTL 寄存器中的 SITYP[1:0]位域选择当前通道支持的接口类型。

## SPI 数据接口

在标准的 SPI 接口下，Σ-Δ 调制器通过 DATAINx 引脚向串行通道发送 1bit 的数据流。HPDF 与 Σ-Δ调制器之间的时钟信号可以由 CKOUT 引脚输出，也可由 CKINx 引脚输入。

SPI 通信时的数据采样点由 HPDF_CHxCTL 寄存器中的 SITYP[1:0]位域和 SPICKSS[1:0]位域共同决定。SPI 通信时的数据采样点如表。


表 34-3. SPI 接口时钟配置


<table><tr><td>SPICKSS[1:0]</td><td>时钟源</td><td>SITYP[1:0]</td><td>采样点</td><td>描述</td></tr><tr><td rowspan="2">00</td><td rowspan="2">CKINx 信号</td><td>00</td><td>上升沿</td><td>数据在外部串行输入时钟信号的上升沿被采样</td></tr><tr><td>01</td><td>下降沿</td><td>数据在外部串行输入时钟信号的下降沿被采样</td></tr><tr><td>01</td><td>CKOUT 信号</td><td>00</td><td>上升沿</td><td>数据在内部串行输出时钟信号的上升沿被采样</td></tr><tr><td></td><td></td><td>01</td><td>下降沿</td><td>数据在内部串行输出时钟信号的下降沿被采样</td></tr><tr><td>10</td><td>CKOUT/2 信号(在 CKOUT 上升沿生成)</td><td>xx</td><td>每第二个CKOUT 信号的下降沿</td><td>外部 Σ-Δ 调制器将 CKOUT 信号进行2 分频,来生成串行输入通信时钟。数据在每第二个 CKOUT 下降沿被采样。</td></tr><tr><td>11</td><td>CKOUT/2 信号(在 CKOUT 下降沿生成)</td><td>xx</td><td>每第二个CKOUT 信号的上升沿</td><td>外部 Σ-Δ 调制器将 CKOUT 信号进行2 分频,来生成串行输入通信时钟。数据在每第二个 CKOUT 上升沿被采样。</td></tr></table>


根据 34-3. SPI ，SPI 数据传输的时序图如下图所示。



图 34-2. SPI 数据传输时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/660925a7e78173aa8184bccfc5bd359d603398546495d584e09d7b74d63decd3.jpg)



注意：如果采用 SPI 数据接口，时钟源的频率范围为 0-20MHz，且小于 f<sub>HPDFCLK</sub>/4。


## 曼切斯特数据接口

HPDF 有 8 个复用串行数据通道可使用曼切斯特编码格式。通过 HPDF_CHxCTL 中的 SITYP[1:0]位域可配置两种方式的编码格式：

1. 当 SITYP[1:0]=2 时，曼切斯特编码格式：上升沿=逻辑 0，下降沿=逻辑 1。

2. 当 SITYP[1:0]=3 时，曼切斯特编码格式：上升沿=逻辑 1，下降沿=逻辑 0。

采用曼切斯特编码时，外部的 Σ-Δ 调制器与 HPDF 之间只通过 DATAINx 引脚进行数据流的传输。经 HPDF 模块曼切斯特解码后，从串行的数据流中将时钟信号和数据恢复，恢复的时钟信号频率必须在 0-10MHz 之间，且小于 f<sub>HPDFCLK</sub>/6。曼切斯特数据传输的时序图如下图所示。


图 34-3. 曼切斯特数据传输时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/9584de47a464b40f3f001d9d4ced60a21f8f1e932e68b5ae6f3f93ac95439c36.jpg)


为 了 能 够 正 确 地 接 收 曼 切 斯 特 数 据 及 解 码 ， 需 要 根 据 预 期 的 曼 切 斯 特 数 据 流 速 率 对CKOUTDIV[7:0]分频器进行配置。CKOUTDIV[7:0]的值参考以下格式计算：

$$
((C K O U T D I V + 1) \times T _ {S Y S C L K}) <   T _ {M a n c h e s t e r \_ c l o c k} <   (2 \times C K O U T D I V \times T _ {S Y S C L K})\tag{34-1}
$$

## 串行通信编码同步

串行通道使能之后，必须实现成功同步后才能正确接收数据。对于 SPI 编码的同步发生在 SPI 数据流第一次检测到时钟输入信号之后。如果通道使用曼切斯特编码，首次同步发生在通道接收数据流由 1-0 或 0-1 的变化。

串行通道的收发器在未实现同步之前，通道的时钟丢失标志位被置 1，当成功同步之后，可通过CKLFC[7:0]将时钟丢失标志位清零。在串行通道的收发器未实现同步时，无法通过 CKLFC[7:0]将时钟丢失标志位清零。因此，可通过软件循环地查询 CKLF[7:0]位的方式来判断串行通道的收发器是否成功同步。下图为曼切斯特编码首次同步的时序图。


图 34-4. 曼切斯特同步时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/dc809c23c8940491e9bfc2a1aad9ce96b8467747f1300fb61b6915e3a66c9350.jpg)


## 外部串行时钟频率测量

通道串行时钟输入频率的测量提供来自外部Σ-Δ调制器的实际数据速率，这对于应用目的很重要。

外部串行时钟输入频率可以通过在一个转换持续时间内计数 HPDF 时钟（f<sub>HPDFCLK</sub>）的定时器来测量。计数从转换触发（常规或注入）后的第一个输入数据时钟开始，到转换结束前的最后一个输入数据时钟结束（设置转换结束标志）。当转换完成（ICEF = 1 或 RCEF = 1）时，每个转换持续时间（第一个串行采样和最后一个串行采样之间的时间）在寄存器 HPDF_FLTxCT 中的计数器CNVCNT[27:0]中更新。然后，用户可以根据数字滤波器设置（SFO、SFOR、IOR、FAST）计算数据速率。外部串行频率测量只有在滤波器被旁路时才会停止（SFOR=0，只有积分器有效，HPDF_FLTxCT 寄存器中的 CNVCNT[27:0] = 0）。

在并行数据输入的情况下，测得的频率是一次转换期间的平均输入数据速率。

注意：当转换被中断（通过禁用 / 启用所选通道）时，中断时间也计入 CNVCNT[27:0]。因此，建议不要中断转换以获得正确的转换持续时间结果。

转换时间：

注入转换或 FAST = 0 的常规转换（如果 FAST=1，则为第一次转换）：

对于 Sincx 过滤器：

$$
T = \text { CNVCNT } / f _ {\text { HPDFCLK }} = [ \text { SFOR } * (\text { IOR - 1 } + \text { SFO }) + \text { SFO } ] / f _ {\text { CKIN }}
$$

对于 FastSinc 滤波器：

$$
T = \text { CNVCNT } / f _ {\text { HPDFCLK }} = [ \text { SFOR } * (\text { IOR - 1 + 4 }) + 2 ] / f _ {\text { CKIN }})
$$

FAST = 1 的常规转换（第一次转换除外）：

对于 Sincx 和 FastSinc 滤波器：

$$
T = \text { CNVCNT } / f _ {\text { HPDFCLK }} = [ \text { SFOR } * \text { IOR - 1 } ] / f _ {\text { CKIN }})
$$

如果 FOSR = FOSR[9:0]+1 = 1（滤波器被旁路，仅激活积分器）：

$$
T = I O R / f _ {C K I N} (\text {但CNVCNT} = 0)
$$

其中：

 f<sub>CKIN</sub>是通道输入时钟频率（在给定通道 CKINx 引脚上）或输入数据速率（在并行数据输入的情况下）

 SFOR 是滤波器过采样率：SFOR = SFOR[9:0]+1（见 HPDF_FLTxSCFFG 寄存器）

 IOR 是积分器过采样率：IOR = IOR[7:0]+1（见 HPDF_FLTxSFCFG 寄存器）

 SFO 是过滤器阶数：SFO = SFO[2:0]（见 HPDF_FLTxSCFFG 寄存器）

## 时钟丢失检测

时钟丢失检测是指通过检测通道串行输入时钟（CKINx 信号）是否丢失，以确保串行通道转换（或阈值监视器和故障监视器）的数据是否存在错误。如果产生了时钟信号丢失事件，则应丢弃给定的数据。使用时钟丢失检测功能时，必须将 CKOUT 信号源配置为系统时钟。

时钟丢失检测功能可由 HPDF_CHxCTL 中的 CKLEN 位使能或禁止。当使能时钟丢失检测功能和时钟丢失中断 CKLIE，若产生了时钟丢失事件，则通道的时钟丢失标志位会被置 1 并产生时钟丢失中断。可通过将 CKLFC[7:0]位域来清除相应的中断标志位。

当通道的串行接口的收发器尚未被同步时，通道的时钟丢失标志位被置 1，且无法将相应的时钟丢失标志位清零。所以正确的使用时钟丢失功能的步骤如下：

1. 使能给定通道 CHEN=1。

2. 循环地查询时钟丢失标志位并对给定通道的 CKLFC 写 1，当确认相应的 CKLF 位被清零时，以此判断串行通道的收发器同步成功。

3. 使能时钟丢失检测功能 CKLEN=1，若要检测可能产生的时钟丢失，可使能时钟丢失中断CKLIE=1。

如果串行通道使用 SPI 接口，使用时钟丢失检测功能时，将外部串行输入时钟（CKINx 信号）与串行输出时钟（CKOUT 信号）进行比较。外部串行输入时钟信号必须在每 8 个 CKOUT 信号周期内至少翻转一次，否则产生时钟丢失事件。

如果串行通道使用曼切斯特接口，时钟丢失检测在曼切斯特编码首次成功同步之后开始，将外部串行输入数据（DATAINx 信号）与串行输出时钟（CKOUT 信号）进行比较。串行输入数据 DATAINx必须在每 2 个 CKOUT 信号周期内发送变化，否则产生时钟丢失事件。时钟丢失的时序如下图所示。


图 34-5. 时钟丢失检测时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/f91b14ff165efdc42e2dab146358084b7bb70f3b7e02539980d2cdb41ab46ff3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/41955583fa564d8da780211330774ce710591141a7054e1fe998dc8192315d2c.jpg)



注意：曼切斯特编码数据流最大速率必须小于时钟输出 CKOUT 信号。


## 通道引脚重定向

通道引脚重定向是指串行通道 0 的引脚可以配置为通道 1 的引脚，即通道 0 可从 DATAIN1 和CKIN1 引脚读取信息。引脚重定向功能适用于采集 PDM 麦克风的音频数据。PDM 麦克风音频信号包含数据和时钟信号，数据分为左/右通道数据，左通道数据在时钟信号的上升沿采集，右通道数据在时钟信号的下降沿采集。

PDM 麦克风数据流输入串行通道时，其配置流程如下：

1. 选择 PDM 麦克风数据流输入的 HPDF 串行通道 1。

2. 将通道 1 的 HPDF_CHxCTL 寄存器中的 CHPINSEL 位写 0，通道 1 的输入引脚为自身引脚DATAIN1 和 CKIN1。将 SITYP[1:0]=0，串行数据流在时钟信号的上升沿被采样，即通道 1 输入的为左通道数据。

3. 将通道0的CHPINSEL位置1，通道0的输入引脚为引脚DATAIN1和CKIN1。将SITYP[1:0]=1，

串行数据流在时钟信号的下降沿被采样，即通道 0 输入的为右通道数据。

4. 将通道 0 和通道 1 配置相应的滤波器，对 PDM 麦克风左右通道数据进行滤波处理。

HPDF 模块的通道引脚重定向示意图如 34-6. 所示。


图 34-6. 通道引脚重定向


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/c49952193aee349b6d8c8eceb174c3d59b619bf446712d477803c74f8ecc8070.jpg)


## 脉冲跳频

脉冲跳频功能是指串行输入数据流在进入滤波器前，跳过指定数量的时钟脉冲后才进入滤波器进行滤波处理，以达到丢弃一定数量的 bit 位的目的。与未跳过的数据流相比，此操作将导致来自滤波器的最终输出样本（和下一个样本）将从后续的输入数据计算得出。

脉冲跳频要跳过的脉冲数由 HPDF_CHxPS 寄存器中的 PLSK[5:0]位域决定。将 PLSK[5:0]位域写入值，指定通道将开始执行脉冲跳频功能。读取 PLSK[5:0]的值，表示剩余未执行的跳频脉冲数。对 PLSK[5:0]单次写操作时，执行的最大跳频脉冲数为 63 个。可通过多次写入 PLSK[5:0]位域来获得更多数量的跳频脉冲。

## 串行输入接口配置

HPDF 模块的串行输入接口配置步骤如下：

1. 配置时钟输出预分频器：通过配置 HPDF_CH0CTL 寄存器中的 CKOUTDIV[7:0]位域，预分频的系数为 CKOUTDIV[7:0]+1。

2. 配置串行接口类型和输入时钟相位：通过 HPDF_CHxCTL 寄存器中 SITYP[1:0]位域配置串行接口类型为 SPI 编码或曼切斯特编码，并确定时钟输入采样边沿。

3. 配置输入时钟源：通过配置 HPDF_CHxCTL 寄存器中 SPICKSS[1:0]选择串行接口的时钟源为串行输入时钟或串行输出时钟。

4. 配置数据偏移校正和右移位数：HPDF_CHxCFG0 寄存器中 DTRS[4:0]定义了最终数据右移的位数，数据移位后执行 CALOFF[23:0]位域定义的偏移校正。

5. 使能故障监视和时钟丢失检测功能：通过对 MMEN 和 CKLEN 置 1，使能故障监视和时钟丢失检测功能。

6. 设置阈值监视器的滤波器和故障监视器：阈值监视器的滤波器参数、故障监视器的短路信号分配及计数器阈值都由 HPDF_CHxCFG1 寄存器进行配置。

## 34.3.5. 并行数据输入

HPDF 模 块 可 通 过 配 置 通 道 复 用 来 选 择 并 行 数 据 作 为 通 道 的 数 据 输 入 源 。 通 过 配 置HPDF_CHxCTL 中的 CMSD[1:0]位域来决定通道数据输入源是来自串行数据还是并行数据。每个通道提供了一个 32 位的并行数据输入寄存器 HPDF_CHxPDI，可通过 CPU / DMA 写入两个 16位并行数据，该寄存器的两个 16 位数据均为有符号格式。

## 内部 ADC 输入

对于并行 ADC 数据输入（CMSD[1:0]=1），ADC[x]结果被分配至通道 x 输入（ADC1 填充HPDF_CHxPDI 寄存器）。来自 ADC[x]的转换结束事件会导致更新通道 x 的数据（来自 ADC[x]的并行数据被用作数字滤波器的下一个采样）。转换结束事件发生时，来自 ADC[x]的数据被写入HPDF_CHxPDI 寄存器（INDAT0[15:0]字段）。

数据封装模式设置（HPDF_CHxCTL 寄存器中的 DPM[1:0]）对 ADC 数据输入无影响。

## CPU/DMA 写入并行数据

并行数据的写入方式有 2 种：CPU 直接写入和 DMA写入方式。在使用 DMA 的方式写入并行数据时，DMA应配置为存储器到存储器模式，其目标地址为并行数据输入寄存器 HPDF_CHxPDI 的地址。

注意：写入并行数据的 DMA与读取 HPDF 模块最终转换数据的 DMA 不同。后者需要配置为外设到存储器模式。

## 并行数据封装模式

存储在 HPDF_CHxPDI 寄 存 器 中 的 数 据 会 经 过 通 道 滤 波 器 进 行 滤 波 器 处 理 。 存 储 在HPDF_CHxPDI 寄存器中的并行数据有 3 种模式。在不同数据封装模式下，允许加载的滤波器采样次数也不同，具体取决于 HPDF_CHxCTL 寄存器中的 DPM[1:0]位域的值。关于不同数据封装模式具体如下：

## 1. 标准模式（DPM[1:0]= 2’b00）：

此模式下，HPDF_CHxPDI 寄存器中的高 16 位被写保护，CPU/DMA 写入的 16 位数据存储在低16 位的 DATAIN0[15:0]位域。CPU / DMA 配置为 16 位访问方式，写入一次 16 位数据时，通道滤波器必须执行一次输入采样来清除 HPDF_CHxPDI 寄存器。

## 2. 交错模式（DPM[1:0]= 2’b01）：

此模式下，CPU / DMA 配置为 32 位访问方式，数据存储在低 16 位的 DATAIN0[15:0]位域和高 16位的 DATAIN1[15:0]位域。写入一次 32 位数据时，通道滤波器必须执行两次输入采样来清除HPDF_CHxPDI 寄存器。通道滤波器第一次采样 DATAIN0[15:0]位域，第二次采样 DATAIN1[15:0]位域.

## 3. 双通道模式（DPM[1:0]= 2’b10）：

此模式下，CPU / DMA 配置为 32 位访问方式，数据存储在低 16 位的 DATAIN0[15:0]位域和高 16位的 DATAIN1[15:0]位域。其中 DATAIN0[15:0]位域的数据用于当前通道 x，而 DATAIN1[15:0]位域的数据会自动被复制到通道 x+1 的并行数据输入寄存器的低 16 位，并将该数据用于通道 x+1。CPU / DMA 写入一次数据，数字滤波器执行两次采样，第一次执通道 x 的采样，第二次执行通道x+1 采样。

HPDF 模块中只有偶数通道（通道 0）支持双通道模式，如果将奇数通道（通道 1）配置为双通道模式，则该通道的并行数据输入寄存器 HPDF_CHxPDI 被写保护。如果通道 x 为偶数通道，且被配置为双通道模式，则奇数通道 x+1 必须配置成标准模式。

并行数据输入寄存器 HPDF_CHxPDI 的操作模式如下表所示：


表 34-4. 并行数据封装模式


<table><tr><td rowspan="3">通道编号</td><td colspan="6">封装模式</td></tr><tr><td colspan="2">标准模式</td><td colspan="2">交错模式</td><td colspan="2">双通道模式</td></tr><tr><td>DATAIN1</td><td>DATAIN0</td><td>DATAIN1</td><td>DATAIN0</td><td>DATAIN1</td><td>DATAIN0</td></tr><tr><td>通道0</td><td>写保护</td><td>CH0采样</td><td>CH0第二次采样</td><td>CH0第一次采样</td><td>CH1采样</td><td>CH0采样</td></tr><tr><td>通道1</td><td>写保护</td><td>CH1采样</td><td>CH1第二次采样</td><td>CH1第一次采样</td><td>写保护</td><td>CH1采样</td></tr><tr><td>通道2</td><td>写保护</td><td>CH2采样</td><td>CH2第二次采样</td><td>CH2第一次采样</td><td>CH3采样</td><td>CH2采样</td></tr><tr><td>通道3</td><td>写保护</td><td>CH3采样</td><td>CH3第二次采样</td><td>CH3第一次采样</td><td>写保护</td><td>CH3采样</td></tr><tr><td>通道4</td><td>写保护</td><td>CH4采样</td><td>CH4第二次采样</td><td>CH4第一次采样</td><td>CH5采样</td><td>CH4采样</td></tr><tr><td>通道5</td><td>写保护</td><td>CH5采样</td><td>CH5第二次采样</td><td>CH5第一次采样</td><td>写保护</td><td>CH5采样</td></tr><tr><td>通道6</td><td>写保护</td><td>CH6采样</td><td>CH6第二次采样</td><td>CH6第一次采样</td><td>CH7采样</td><td>CH6采样</td></tr><tr><td>通道7</td><td>写保护</td><td>CH7采样</td><td>CH7第二次采样</td><td>CH7第一次采样</td><td>写保护</td><td>CH7采样</td></tr></table>

CPU / DMA 向 HPDF_CHxPDI 寄存器写操作应当在通道使能之后，因为在使能通道之后，通道转换会开启，在通道转换开启之前会丢弃 HPDF_CHxPDI 寄存器中的数据。

## 34.3.6. 规则组转换

HPDF 模块有 8 个复用通道，可分别用于规则组转换或注入组转换。如果通道被禁止（CHEN=0），使能通道转换，会导致通道一直处于转换状态。只有通过使能通道（CHEN=1）或禁止 HPDF 模块（HPDFEN=0）才能恢复正常。

规则组只选择 8 个通道中的一个，由 HPDF_FLTyCTL0 寄存器中的 RCS 位决定。在同一时刻内，只能有一个规则转换处于执行或待处理状态。如果已有规则转换请求尚未完成，则会忽略新的规则转换启动请求。规则转换的优先级低于注入组转换，能被注入组转换请求中断。

规则组的转换时间 t=CTCNT[27:0] / f<sub>HPDFCLK</sub>。

## 转换启动模式

规则组转换只能通过软件的启动的方式实现。软件启动分为 2 种模式，具体方法如下：

1. 常规软件启动：向 HPDF_FLTyCTL0 寄存器中的 SRCS 位写 1。

2. 软件同步启动：将 HPDF_FLTyCTL0 寄存器中同步启动 RCSYN 位置 1，当使用常规软件启动 HPDF_FLT0 的常规转换时，则 HPDF_FLTy 也同步地启动规则转换。

## 转换模式

规则组转换支持连续模式和快速模式。

## 连续模式

通过将 HPDF_FLTyCTL0 中的 RCCM 位置 1 使能连续模式。在连续模式下，软件启动规则组转换后，重复执行转换规则组通道转换。清零 RCCM 位后，在连续模式下进行的规则转换会立即停止。

## 快速模式

通过将 HPDF_FLTyCTL0 中的 FAST 位置 1 使能快速模式。在快速模式，能够提升连续模式下的数据速率。因为在连续模式下，如果从一个通道连续转换，则无需新的数据填充滤波器，因为滤波器内的数据是来自先前连续模式下采样的有效数据。数据速率的提升由所选滤波器阶数决定。

启动连续转换后，在快速模式的首次转换于未开启快速模式的时间相同，然后会以较短的时间间隔完成后续的转换。

## 34.3.7. 注入组转换

注入组转换通道必须至少选择 8 个通道中的任意一个。可通过 HPDF_FLTyIGCS 寄存器中的IGCSEL[7:0]位域选择哪个通道为注入组转换，IGCSEL[x]=1 表示通道 x 为注入组通道。

注入组的优先级高于规则组，正在进行中的规则组转换会被注入组转换请求中断，等待注入组完成转换后重启被中断的常规转换。在同一时刻内，只能有一个注入转换处于执行或待处理状态。如果已有注入转换请求尚未完成，则会忽略新的注入转换启动请求。

注入组的转换时间 t=CTCNT[27:0] / f<sub>HPDFCLK</sub>。

## 启动转换方式

注入组转换可通过软件启动和触发启动的方式实现，具体方法如下：

1. 常规软件启动：向 HPDF_FLTyCTL0 寄存器中的 SICC 位写 1。

2. 软件同步启动：将 HPDF_FLTyCTL0 寄存器中同步启动 ICSYN 位置 1，当使用常规软件启动HPDF_FLT0 的注入组转换时，则 HPDF_FLT1 也同步地启动注入转换。

3. 触发启动：当 HPDF_FLTyCTL0 寄存器中 ICTSSEL[4:0]位域写入非 0 的值时表示使能触发启动并同时选择了触发信号源。触发的有效边沿则由 ICTEEN[1:0]位域决定。

注入组的触发信号如下表所示：


表 34-5. 注入组的触发信号


<table><tr><td>触发信号名称</td><td>信号源</td></tr><tr><td>HPDF_ITRG0</td><td>TIMER0_TRGO0</td></tr><tr><td>HPDF_ITRG1</td><td>TIMER0_TRGO1</td></tr><tr><td>HPDF_ITRG2</td><td>TIMER7_TRGO0</td></tr><tr><td>HPDF_ITRG3</td><td>TIMER7_TRGO1</td></tr><tr><td>HPDF_ITRG4</td><td>TIMER2_TRGO0</td></tr><tr><td>HPDF_ITRG5</td><td>TIMER3_TRGO0</td></tr><tr><td>HPDF_ITRG6</td><td>TIMER15_CH1</td></tr><tr><td>HPDF_ITRG7</td><td>TIMER5_TRGO0</td></tr><tr><td>HPDF_ITRG8</td><td>TIMER6_TRGO0</td></tr><tr><td>HPDF_ITRG[9~10]</td><td>保留</td></tr><tr><td>HPDF_ITRG11</td><td>保留</td></tr><tr><td>HPDF_ITRG12</td><td>保留</td></tr><tr><td>HPDF_ITRG[13~23]</td><td>保留</td></tr><tr><td>HPDF_ITRG24</td><td>EXTI11</td></tr><tr><td>HPDF_ITRG25</td><td>EXTI15</td></tr><tr><td>HPDF_ITRG26</td><td>-</td></tr><tr><td>HPDF_ITRG27</td><td>-</td></tr><tr><td>HPDF_ITRG28</td><td>-</td></tr><tr><td>HPDF_ITRG[29~30]</td><td>保留</td></tr><tr><td>HPDF_ITRG31</td><td>HPDF_ITRG</td></tr></table>

## 扫描转换模式

通过将 HPDF_FLTyCTL0 寄存器中 SCMOD 位置 1，可使能注入组转换的扫描转换模式。在扫描模式下，每次触发注入组转换时，注入组中的所有通道会从最低通道开始依次转换。

如果禁止扫描模式，则每次触发注入组转换时，只会转换注入组里的一个通道，下一次的触发会选择另一个通道。在禁止扫描模式下，对 IGCSEL[7:0]位域写操作会将最低通道作为选择的转换通道。

## 转换请求优先级

注入组的转换具有比规则组转换更高的优先级。已在进行的规则转换会被注入转换的请求立即中断。若注入转换序列结束时，如果 RCCM 仍处于置位状态，则连续的规则转换将再次启动。被打断的规则转换重新启动，RCHPDT 位的值表示被打断的规则转换延迟启动。

如果一个注入转换被挂起或已在进行中，则无法启动其他注入转换：只要 ICPF=1，启动注入转换的任何请求（软件或触发启动）都将被忽略。对于规则转换也是如此。

当注入转换正在进行（ICPF=1）时，对 HPDF_FLTyCTL0 的 SRCS 位写 1，请求规则转换。当注入序列完成时，优先级指示下一步执行规则转换，并以 RCHPDT 位表示延迟启动。

## 34.3.8. 数字滤波器

HPDF 模块的数字滤波器为 SincX类型。输入的数据流经 SincX进行滤波，从而降低输出数据速率并提高输出数据分辨率。通过 HPDF_FLTySFCFG 寄存器中的 SFO[2:0]位域和 SFOR[9:0]位域配置 SincX 滤波器的阶数和过采样率（抽取率）。用户可根据所需的分辨率配置 SincX 滤波器的阶数和过采样率。SincX滤波的最大输出分辨率与过采样率的关系如下表：


表 34-6. Sinc<sup>X</sup> 滤波的最大输出分辨率与过采样滤的关系


<table><tr><td>SFOR</td><td>Sinc</td><td><eq>Sinc^2</eq></td><td>FastSinc</td><td><eq>Sinc^3</eq></td><td><eq>Sinc^4</eq></td><td><eq>Sinc^5</eq></td></tr><tr><td>x</td><td>±x</td><td><eq>±x^2</eq></td><td><eq>±2x^2</eq></td><td><eq>±x^3</eq></td><td><eq>±x^4</eq></td><td><eq>±x^5</eq></td></tr><tr><td>4</td><td>±4</td><td>±16</td><td>±32</td><td>±64</td><td>±256</td><td>±1024</td></tr><tr><td>8</td><td>±8</td><td>±64</td><td>±64</td><td>±512</td><td>±4096</td><td>±32768</td></tr><tr><td>32</td><td>±32</td><td>±1024</td><td>±2048</td><td>±32768</td><td>±1048576</td><td>±33554432</td></tr><tr><td>64</td><td>±64</td><td>±4096</td><td>±8192</td><td>±262144</td><td>±16777216</td><td>±1073741824</td></tr><tr><td>128</td><td>±128</td><td>±16384</td><td>±32768</td><td>±2097152</td><td>±268435456</td><td>-</td></tr><tr><td>256</td><td>±256</td><td>±65536</td><td>±131072</td><td>±16777216</td><td rowspan="2" colspan="2">在满量程输入的条件下,结果会溢出</td></tr><tr><td>1024</td><td>±1024</td><td>±1048576</td><td>±2097152</td><td>±1073741824</td></tr></table>


注意：该表中最大输出分辨率来自滤波器输出的峰值数据值。


## 34.3.9. 积分器

积分器对来自数字滤波器的数据执行进一步的过采样率（抽取率）和分辨率提高。积分器对来自滤波器中给定数量的数据采样执行简单的求和操作。积分器输出数据是来自滤波器的数据采样求和而 来 ， 数 据 采 样 的 数 量 由 积 分 的 过 采 样 率 决 定 。 积 分 器 的 过 采 样 率 （ 抽 取 率 ） 可 由HPDF_FLTySFCFG 寄存器中的 IOR[7:0]配置。积分器的最大输出分辨率、过采样率、Sinc 滤波器阶数的关系如下表：


表 34-7. 积分器的最大输出分辨率与 IOR、SFOR、SFO 之间的关系


<table><tr><td>滤波器类型</td><td>积分器最大输出分辨率</td></tr><tr><td>Sinc</td><td>±(SFOR×IOR)</td></tr><tr><td><eq>Sinc^2</eq></td><td>±(SFOR<eq>^2</eq>×IOR)</td></tr><tr><td>FastSinc</td><td>±(2SFOR<eq>^2</eq>×IOR)</td></tr><tr><td><eq>Sinc^3</eq></td><td>±(SFOR<eq>^3</eq>×IOR)</td></tr><tr><td><eq>Sinc^4</eq></td><td>±(SFOR<eq>^4</eq>×IOR)</td></tr><tr><td><eq>Sinc^5</eq></td><td>±(SFOR<eq>^5</eq>×IOR)</td></tr></table>

## 34.3.10. 阈值监视器

HPDF 模块的阈值监视器用于监视通道的串行输入数据或通道转换后最终输出的数据，当数据达到阈值监视器设定的阈值（上限或下限阈值）时，会产生中断或断路事件。高阈值由HPDF_FLTyTMHT 寄存器中的 HTVAL[23:0]位决定，低阈值由 HPDF_FLTyTMLT 寄存器中的LTVAL[23:0]位决定。

HPDF 模块的拥有 4 个阈值监视器，通过配置 HPDF_FLTyCTL1 寄存器中的 TMCHEN[7:0]位域决定阈值监视器 x 是否监视输入通道。如 HPDF_FLT0CTL1 寄存器中的 TMCHEN[1]=1 表示阈值监视器 0 监视通道 1 的阈值。

## 阈值监视器工作模式

阈值监视器工作模式分为标准模式和快速模式。快速模式是配置阈值监视器监视通道的串行输入数据并与设定的阈值比较。标准模式是配置阈值监视器监视通道转换后输出的最终数据（存储在注入组数据寄存器 HPDF_FLTyIDATA 或规则组数据寄存器 HPDF_FLTyRDATA）。阈值监视器的快速模式可通过 HPDF_FLTyCTL0 中的 TMFM 位使能快速模式。两种模式的下的特性如下表：


表 34-8. 阈值监视器工作模式特点


<table><tr><td>模式</td><td>使能位</td><td>通道数据源</td><td>阈值监视器输入数据源</td><td>输入数据分辨率</td><td>详细描述</td></tr><tr><td>标准模式</td><td>TMFM=0</td><td>串行数据流、并行数据</td><td>HPDF 最终输出数据</td><td>24 位</td><td>阈值监视器监视通道转换后输出的最终数据。响应时间慢,不适用于过流/过压等检测。</td></tr><tr><td>快速模式</td><td>TMFM=1</td><td>串行数据流</td><td>串行数据流</td><td>16 位</td><td>输入数据以连续模式提供,阈值监视器直接监视串行输入数据,与规则或注入转换无关。响应时间快,适用于过流/过压等检测。</td></tr></table>

阈值监视器在快速模式下，只使用阈值（上限阈值 HTVAL[23:0]或下限阈值 LTVAL[23:0]）的高 16位与通道的串行输入数据进行比较，即只用 HTVAL[23:0]和 LTVAL[23:0]的高 16 位定义阈值，这是因为阈值监视器的滤波器分辨率为 16 位。

阈值监视器在非快速模式下，完成右移位和偏移校正的最终数据会与 HTVAL[23:0]和 LTVAL[23:0]进行比较。

## 阈值监视器快速模式

在快速模式下，将使用阈值监视器自身的滤波器，在 HPDF_CHxCFG1 寄存器中可设置阈值监视器滤波器的过采样率（抽取率）和阶数。

阈值监视器的配置较为灵活，可通过 HPDF_FLTyCTL1 寄存器中的 TMCHEN[7:0]位域将一个阈值监视器可以配置监视多个通道。在此情况下，当多个通道发出请求时，阈值监视器优先处理通道编号 小 的 请 求 ， 然 后 再 处 理 通 道 编 号 大 的 请 求 。 每 个 阈 值 监 视 器 均 有 一 个 状 态 寄 存 器HPDF_FLTyTMSTAT，当所监视的通道发生超出阈值错误事件时，在 HTF[7:0]或 LTF[7:0]位域中对应的标志会被置位。如 HTF[0]=2b’01，表示通道 0 发生超出上限阈值错误。

每个通道发出比较请求后，会在 8 个 HPDF 时钟周期内被执行。因此，每个通道的带宽被限制为

8 个 HPDF 时钟周期（如果 TMCHEN[7:0]=3）。由于输入通道最大采样频率为 f<sub>HPDFCLK</sub>/4，因此在该输入时钟速度下，阈值监视器滤波器不能被旁路（TMFOR=0）。因此，用户必须根据输入采样时钟速度和 f<sub>HPDFCLK</sub>正确配置阈值监视器滤波器参数和所监视的通道数。

在快速模式下，读取 HPDF_CHxTMFDT 寄存器中 TMDATA[15:0]位域可获得定通道 x 的阈值监视器滤波器数据。阈值监视器滤波器输出（在串行输入时钟频率 f<sub>CKIN</sub>）一个结果所需的串行样本数如下：

## 1. 首次转换：

FastSinc 滤波器：采样数 $= ( \mathsf { T M F O R } [ 4 ; 0 ] \times 4 + 2 + 1 )$ o

$$
\text { Sinc } ^ {\mathrm{X}} \text { 滤波器   (X = 1...5):采样数 } = (((\text { TMFOR } [ 4: 0 ] + 1) \times \text { TMSFO } [ 1: 0 ]) + \text { TMSFO } [ 1: 0 ] + 1)
$$

## 2. 除首次转换外的后续转换：

FastSinc 和 $\mathtt { S i n c } ^ { \mathtt { X } }$ 滤波器（X=1...5）：采样数=(TMFOR[4:0]+1)×(IOR[7:0]+1)。

## 阈值监视器状态标志

阈值监视器的全局状态为 HPDF_FLTySTAT 寄存器中的 TMEOF 标志位，当 TMEOF=1 时，表示至少产生了一个阈值监视器事件，即有超出（上限/下限）阈值的事件产生。如果使能HPDF_FLTyCTL1 中的阈值监视器事件中断 TMIE=1，可产生看阈值监视器中断。当所有 HTF[7:0]和 LTF[7:0]都被清除时，TMEOF 位被清除。

HPDF_FLTyTMSTAT 寄存器中定义了通道发生超出阈值的错误事件标志，其中，HTF[7:0]位域表示通道 x 上是否发生超出上限阈值 HTVAL[23:0]值。LTF[7:0]位域表示通道 x 上是否发生超出下限阈值 LTVAL[23:0]值。通过将“1”写入 HPDF_FLTyTMFC 寄存器中相应的 HTFC[7:0]或 LTFC[7:0]位来清除超出阈值标志。

如 34-2. HPDF 所示，HPDF 模块中有 4 个断路输出信号，通过配置 HPDF_FLTyTMHT寄存器和 HPDF_FLTyTMLT 寄存器中的 HTBSD[3:0]和 LTBSD[3:0]位域将断路输出信号分配给阈值监视器超出阈值事件。

## 34.3.11. 故障监视器

故障监视器用于检测当前模拟信号的状态是否处于短路或开路故障（例如过电流/电压）。若故障监视器检测到上述两种状态之一时，能够以极快的响应时间产生断路事件，并输出断路信号。断路输出信号可以分配给故障监视器事件，可通过配置由 HPDF_CHxCFG1 寄存器中的 MMBSD[3:0]位域实现。断路输出信号与阈值监视器相同。

故障监视器的输入数据来自通道的串行输入数据，当通道输入数据源为并行数据时，禁止使用故障监视功能。在每个输入通道上都有一个递增计数器，用于记录在串行数据流有多少个连续的 0 或1。当计数器达到故障阈值寄存器值（HPDF_CHxCFG1 寄存器中的 MMCT[7:0]位），则产生短路或开路故障事件。若监测数据流时遇到 0-1 或 1-0 的变化，则计数器的值会被自动清零并重新计

数。

用户可以通过设置 HPDF_CHxCTL 寄存器中的 MMEN 位来使能故障监视功能。当通道产生短路或开路故障事件时，相应的故障监视标志置位 MMF[7:0]被置位。可通过 HPDF_FLTyINTC 中的MMFC[7:0]清除相应的标志，若通道 x 被禁用（CHEN=0），硬件也会清除故障监视标志。

## 34.3.12. 极值监视器

极 值 监 视 器 被 用 于 采 集 最 终 输 出 数 据 字 的 最 小 值 和 最 大 值 （ 峰 值 到 峰 值 ）。 通 过 配 置HPDF_FLTyCTL1 寄存器中的 EMCS[7:0]位域，可使一个极值监视器采集多个通道的极值。

如果采集的最终输出数据字高于在极值监视器最大值寄存器中的值（HPDF_FLTyEMMAX 寄存器中的 MAXVAL[23:0]位），则用该寄存器的值被更新为当前的最终输出数据。如果采集的最终输出数据字小于在极值监视器最小值寄存器中的值（HPDF_FLTyEMMIN 寄存器中的 MINVAL[23:0]位），则该寄存器的值被更新为当前的最终输出数据。MAXDC 位和 MINDC 位的值分别指明了最大值/最小值来自哪个通道。

当读取 HPDF_FLTyEMMAX 或 HPDF_FLTyEMMIN 寄存器时，最大值或最小值被更新为复位值。

## 34.3.13. 数据单元

数据单元是整个HPDF模块中处理数据的最后一个部分，HPDF模块处理数据的流程如下图所示。


图 34-7. HPDF 模块外部输入数据处理流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/29b18f921aac443a9a5079270896e37953e593b8fd416ca840d42225d2fbdf6e.jpg)


输出数据速率取决于串行数据流速率、滤波器和积分器设置。最大输出数据速率如下表所示。


表 34-9. 最大输出速率


<table><tr><td>输入源</td><td>转换模式</td><td>滤波器类型</td><td>最大输出数据速率(采样/秒)</td></tr><tr><td rowspan="3">串行输入</td><td>非快速模式(FAST=0)</td><td><eq>Sinc^X</eq></td><td><eq>\frac{f_{CKIN}}{SFOR \times (IOR-1 + SFO) + (SFO+1)}</eq></td></tr><tr><td>非快速模式(FAST=0)</td><td>FastSinc</td><td><eq>\frac{f_{CKIN}}{SFOR \times (IOR-1 + 4) + (2 + 1)}</eq></td></tr><tr><td>快速模式(FAST=1)</td><td>FastSinc 和 <eq>Sinc^X</eq></td><td><eq>\frac{f_{CKIN}}{SFOR \times IOR}</eq></td></tr><tr><td rowspan="2">并行输入</td><td>非快速模式(FAST=0)</td><td><eq>Sinc^X</eq></td><td><eq>\frac{f_{DATA}}{SFOR \times (IOR-1 + SFO) + (SFO+1)}</eq></td></tr><tr><td>非快速模式(FAST=0)速模式(FAST=1)</td><td>FastSincFastSinc 和 <eq>Sinc^x</eq></td><td><eq>\frac{f_{DATA}}{SFOR \times (IOR-1 + 4) + (2 + 1)}</eq><eq>\frac{f_{DATA}}{SFOR×IOR}</eq></td></tr></table>


注意：表中f<sub>DATA</sub>为CPU / DMA输入的并行数据速率，当滤波器被旁路时，必须满足f<sub>DATA</sub>≤f<sub>HPDFCLK</sub>。


## 有符号的数据格式

HPDF 模块中的有符号数据：并行数据寄存器、规则和注入组数据寄存器、阈值监视器阈值、极限监视器极值、偏移校正均为有符号格式。输出数据的最高有效位表示值的符号，数据采用二进制的补码格式。

由于数字处理中的所有操作都在 32 位有符号寄存器上执行，因此必须满足以下条件才能使结果不溢出：

1. 当使用 Sinc<sup>X</sup>滤波器（x=1…5）时： $( { \mathsf { S F O R } } ^ { \mathsf { S F O } } ) { \star } { \mathsf { I O R } } \leq 2 ^ { 3 1 }$ 

2. 当使用 FastSinc 滤波器时： $2 \times ( { \mathsf { S F O R } } ^ { 2 } ) { \times } { \mathsf { I O R } } \leq 2 ^ { 3 1 }$ C

## 数据右位移

由于 HPDF 输出数据的最高分辨率为 24 位，并且来自处理路径的数据可以高达 32 位，因此在该模块中执行最终数据的右位移位。对于每个选定的输入通道，可在 HPDF_CHxCFG0 寄存器中的DTRS[4:0]位域配置右移的位数，右移位是丢弃最低位的数，取近似值。

## 数据偏移校正

HPDF 模块中，每个通道都有一个数据偏移校正值，该值存储在 HPDF_CHxCFG0 寄存器的CALOFF[23:0]位域。在进行偏移校正时，通道的输出数据中减去偏移校正值，以得到 HPDF 模块输出的最终数据。

数据偏移校正发生在数据右位移之后。

## 34.3.14. HPDF 中断

HPDF 的中断事件可分为通道转换中断事件、阈值监视器中断事件、故障监视器中断事件和通道时钟丢失中断事件。具体的中断事件描述如 34-10. HPDF 所示。


表 34-10. HPDF 中断事件


<table><tr><td>中断事件</td><td>描述</td><td>清除方式</td><td>中断使能位</td></tr><tr><td>ICEF</td><td>注入转换结束</td><td>读 HPDF_FLTyIDATA 寄存器</td><td>ICEIE</td></tr><tr><td>RCEF</td><td>规则转换结束</td><td>读 HPDF_FLTyRDATA 寄存器</td><td>RCEIE</td></tr><tr><td>ICDOF</td><td>注入转换数据溢出</td><td>写 1 到 ICDOFC 位</td><td>ICDOIE</td></tr><tr><td>RCDOF</td><td>规则转换数据溢出</td><td>写 1 到 RCDOFC 位</td><td>RCDOIE</td></tr><tr><td>TMEOF</td><td>阈值监视器事件</td><td>写 1 到 HTFC[7:0]位域</td><td>TMIE</td></tr><tr><td>HTF[7:0]LTF[7:0]</td><td></td><td>写1到LTFC[7:0]位域</td><td></td></tr><tr><td>MMF</td><td>通道发生故障事件</td><td>写1到MMFC[7:0]位</td><td>MMIE</td></tr><tr><td>CKLF</td><td>通道时钟丢失</td><td>写1到CKLFC[7:0]位</td><td>CKLIE</td></tr></table>


HPDF 中断逻辑如 34-8. HPDF 所示。



图 34-8. HPDF 中断逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/a86c117ba8c18f11a8ad1009b1e3b4f0bc604b256286a8ad33753de1e1706a47.jpg)

