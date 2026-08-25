## 26. 控制器局域网络（CAN）

## 26.1. 简介

CAN（Controller Area Network）总线是一种可以在无主机情况下实现微处理器或者设备之间相互通信的总线标准。

GD32E513xx 和 GD32E517xx 系列的 CAN 网络接口遵循 CAN 总线协议 2.0A、2.0B 规范，而在 GD32E518xx 系列中还遵循 ISO11898-1:2015 和 BOSCH CAN-FD 规范。CAN 总线控制器可以处理总线上的数据收发，CAN0 和 CAN1 共享 28 个过滤器，而 CAN2 拥有 14 个独立的过滤器。用户可以通过 3 个发送邮箱将待发送数据传输至总线，邮箱发送的顺序由发送调度器决定。并通过 2 个深度为 3 的接收 FIFO 获取总线上的数据，接收 FIFO 的管理完全由硬件控制。同时 CAN 总线控制器硬件支持时间触发通信（Time-trigger communication）功能。

## 26.2. 主要特征

 支持 CAN 总线协议 2.0A 和 2.0B；

 常规帧：通信波特率最大为 1Mbit/s；

 支持时间触发通信（Time-triggered communication）；

 中断使能和清除；

 支持 CAN-FD 帧（仅在 GD32E518xx 系列）；

 CAN-FD 帧：通信波特率最大为 8Mbit/s（仅在 GD32E518xx 系列）；

 支持传输延迟补偿（仅在 GD32E518xx 系列）。

## 发送功能

 3 个发送邮箱；

 支持发送优先级；

 支持发送时间戳。

## 接收功能

 2 个深度为 3 的接收 FIFO；

 CAN0 和 CAN1 具有 28 个标识符过滤器；

 CAN2 拥有 14 个独立的标识符过滤器；

 FIFO 锁定功能。

## 时间触发通信

 在时间触发通信模式下禁用自动重传；

 16 位定时器；

 接收时间戳；

 发送时间戳。

## 26.3. 功能说明

CAN 模块结构框图如 26-1. CAN 所示。


图 26-1. CAN 模块结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/5ecddf22454d473541d529fb9c88cc096f887a55fd4af839afb3cb9ae810feaa.jpg)


## 26.3.1. 工作模式

CAN 总线控制器有 3 种工作模式：

 睡眠工作模式；

 初始化工作模式；

 正常工作模式。

## 睡眠工作模式

芯片复位后，CAN 总线控制器处于睡眠工作模式。该模式下 CAN 总线控制器的时钟停止工作并处于一种低功耗状态。

将 CAN_CTL 寄存器的 SLPWMOD 位置 1，可以使 CAN 总线控制器进入睡眠工作模式。当进入睡眠工作模式后，CAN_STAT 寄存器的 SLPWS 位将被硬件置 1。

将 CAN_CTL 寄存器的 AWU 位置 1，并当 CAN 检测到总线活动时，CAN 总线控制器将自动退出睡眠工作模式。将 CAN_CTL 寄存器的 SLPWMOD 位清 0，也可以退出睡眠工作模式。

由睡眠模式进入初始化工作模式：将 CAN_CTL 寄存器的 IWMOD 位置 1，SLPWMOD 位清0。

由睡眠模式进入正常工作模式：将 CAN_CTL 寄存器的 IWMOD 位和 SLPWMOD 位清 0。

## 初始化工作模式

如果需要配置 CAN 总线通信参数，CAN 总线控制器必须进入初始化工作模式。将 CAN_CTL寄存器的 IWMOD 位置 1，使 CAN 总线控制器进入初始化工作模式，将其清 0 则离开初始化工作模式。在进入初始化工作模式后，CAN_STAT 寄存器的 IWS位将被硬件置 1。

由初始化模式进入睡眠模式：CAN_CTL 寄存器的 SLPWMOD 位置 1，IWMOD 位清 0。

由初始化模式进入正常工作模式：CAN_CTL 寄存器的 SLPWMOD 位和 IWMOD 位清 0。

## 正常工作模式

在初始化工作模式中配置完 CAN 总线通信参数后，将 CAN_CTL 寄存器的 IWMOD 位清 0 可以进入正常工作模式并与 CAN 总线网络中的节点进行正常通信。

由正常工作模式进入睡眠工作模式：CAN_CTL 寄存器的 SLPWMOD 位置 1，并等待当前数据收发过程结束。

由正常工作模式初始化工作模式：CAN_CTL 寄存器的 IWMOD 位置 1，并等待当前数据收发过程结束。

## 26.3.2. 通信模式

CAN 总线控制器有 4 种通信模式：

 静默（Silent）通信模式；

 回环（Loopback）通信模式；

 回环静默（Loopback and Silent）通信模式；

 正常（Normal）通信模式。

## 静默（Silent）通信模式

在静默通信模式下，可以从 CAN 总线接收数据，但不向总线发送任何数据。将 CAN_BT 寄存器中的 SCMOD 位置 1，使 CAN 总线控制器进入静默通信模式，将其清 0 可以退出静默通信模式。

静默通信模式可以用来监控 CAN 网络上的数据传输。

## 回环（Loopback）通信模式

在回环通信模式下，由 CAN 总线控制器发送的数据可以被自己接收并存入接收 FIFO，同时这些发送数据也送至 CAN 网络。将 CAN_BT 寄存器中的 LCMOD 位置 1，使 CAN 总线控制器进入回环通信模式，将其清 0 可以退出回环通信模式。

回环通信模式通常用来进行 CAN 通信自测。

## 回环静默（Loopback and Silent）通信模式

在回环静默通信模式下，CAN 的 RX 和 TX 引脚与 CAN 网络断开。CAN 总线控制器既不从CAN 网络接收数据，也不向 CAN 网络发送数据，其发送的数据仅可以被自己接收。将 CAN_BT寄存器中的 LCMOD 位和 SCMOD 位置 1，使 CAN 总线控制器进入回环静默通信模式，将它们清 0 可以退出回环静默通信模式。

回环静默通信模式通常用来进行 CAN 通信自测。对外 TX 引脚保持隐性状态（逻辑 1），RX 引脚保持高阻态。

## 正常（Normal）通信模式

CAN 总线控制器通常工作在正常通信模式下，可以从 CAN 总线接收数据，也可以向 CAN 总线发送数据。这时需要将 CAN_BT 寄存器的 LCMOD 位和 SCMOD 位清 0。

## 26.3.3. 数据发送

## 发送寄存器

数据发送通过 3 个发送邮箱进行，可以通过寄存器 CAN_TMIx，CAN_TMPx，CAN_TMDATA0x和 CAN_TMDATA1x 对发送邮箱进行配置。如 26-2. 所示。


图 26-2. 发送寄存器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/75205bc28af2b23cd8887e56e89165de87871d88f0425063a2805d804d95e68d.jpg)



如果想要发送 CAN-FD 帧，使用发送邮箱 x（x 等于 0 到 2）时，仅需要写对应的 TMDATA0x（x 等于 0 到 2）寄存器。例如软件想要使用发送邮箱 0 发送 64 字节数据，需要通过写TMDATA00 寄存器 16 次将待发送数据写入内部专用 SRAM 区。


## 发送邮箱状态转换

当发送邮箱处于 empty 状态时，应用程序才可以对邮箱进行配置。当邮箱被配置完成后，可以将 CAN_TMIx 寄存器的 TEN 位置 1，从而向 CAN 总线控制器提交发送请求，这时发送邮箱处于 pending 状态。当超过 1 个邮箱处于 pending 状态时，需要对多个邮箱进行调度，这时发送邮箱处于 scheduled 状态。当调度完成后，发送邮箱中的数据开始向 CAN 总线上发送，这时发送邮箱处于 transmit 状态。当数据发送完成，邮箱变为空闲，可以再次交给应用程序使用，这时发送邮箱重新变为 empty 状态。如 26-3. 所示。


图 26-3. 发送邮箱状态转换


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/06e1b89e08ad35bc878c91611b12d04c51a4dc37cbcd2317f96c143fedec9bb5.jpg)


## 发送状态和错误信息

CAN_TSTAT 寄存器中的 MTF，MTFNERR，MAL 和 MTE 位用来说明发送状态和错误信息。

 MTF：发送完成标志位。当数据发送完成时，MTF 置 1。

 MTFNERR：无错误发送完成标志位。当数据发送完成且没有错误时，MTFNERR 置 1。

 MAL：仲裁失败标志位。当发送数据过程中出现仲裁失败时，MAL置1。

 MTE：发送错误标志位。当发送过程中检测到总线错误时，MTE置1。

## 数据发送步骤

数据发送步骤如下：

第 1 步：选择一个空闲发送邮箱；

第 2 步：根据应用程序要求，配置 4 个发送寄存器；

第 3 步：将 CAN_TMIx 寄存器的 TEN 置 1；

第 4 步：检测发送状态和错误信息。典型情况是检测到 MTF 和 MTFNERR 置 1，说明数据被成功发送。

## 发送选项

## 中止数据发送

将 CAN_TSTAT 寄存器的 MST 置 1，可以中止数据发送。

当发送邮箱处于 pending 和 scheduled 状态，CAN_TSTAT 寄存器的 MST 置 1 可以立即中止数据发送。

当发送邮箱处于 transmit 状态，则面临两种情况。一种情况是数据发送被成功地完成，MTF和 MTFNERR 为 1，这时发送邮箱将转换为 empty 状态。相对的，如果数据发送过程中出现了问题，这时发送邮箱将转换为 scheduled 状态，这时数据发送被中止。

## 发送优先级

当有2个及其以上发送邮箱等待发送时，寄存器CAN_CTL的TFO位的值可以决定发送顺序。

当 TFO 为 1，所有等待发送的邮箱按照先来先发送（FIFO）的顺序进行。

当 TFO 为 0，具有最小标识符（Identifier）的邮箱最先发送。如果所有的标识符（Identifier）相等，具有最小邮箱编号的邮箱最先发送。

## 26.3.4. 数据接收

## 接收寄存器

应用程序通过 2 个深度为 3 的 FIFO 接收来自 CAN 网络的数据。

寄存器 CAN_RFIFOx 可以操作 FIFO，也包含 FIFO 状态。寄存器 CAN_RFIFOMIx，CAN_RFIFOMPx，CAN_RFIFOMDATA0x 和 CAN_RFIFOMDATA1x 用于接收数据帧。

如 26-4. 所示。


图 26-4. 接收寄存器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/e8ad16a41713f226cc53b28db3fccf287aff7fc49a49c9a63524c279ab63cf01.jpg)


## 接收 FIFO

每个接收 FIFO 包含 3 个接收邮箱，用来接收存储数据帧。这些邮箱按照先进先出方式进行组织，最早从 CAN 网络接收的数据，最早被应用程序处理。

寄存器 CAN_RFIFOx 包含 FIFO 状态信息和帧的数量。当 FIFO 中包含数据时，可以通过寄存器 CAN_RFIFOMIx，CAN_RFIFOMPx，CAN_RFIFOMDATA0x 和 CAN_RFIFOMDATA1x 读取数据，之后将寄存器 CAN_RFIFOx 的 RFD 位置 1 释放邮箱，并且等待其由硬件自动清 0。

如 果 接 收 到 CAN-FD 帧 ， 数 据 将 被 存 储 到 内 部 专 用 SRAM 中 ， 并 通 过 多 次 读CAN_RFIFOMDATA0x 寄存器将数据取出。FIFO0 使用 CAN_RFIFOMDATA00，FIFO1 使用CAN_RFIFOMDATA01 寄存器。例如，如果软件想要从 FIFO0 中读 64 字节数据，需要通过读CAN_RFIFOMDATA00 寄存器 16 次将数据全部读出。

## 接收 FIFO 状态信息

接收 FIFO 状态信息包含在寄存器 CAN_RFIFOx 中。

RFL：FIFO 中包含的帧数量。FIFO 为空时，RFL 为 0；FIFO 为满时，RFL 为 3。

RFF：FIFO 满状态标志位。这时 RFL 为 3。

RFO：FIFO 溢出标志位。当 FIFO 已经包含了 3 个数据帧时，新的数据帧到来使 FIFO 发生溢出。如果 CAN_CTL 寄存器的 RFOD 位被置 1，新的数据帧将丢弃。如果该位被清 0，新的数据帧将覆盖接收 FIFO 中最后一帧数据。

## 数据接收步骤

第 1 步：查看 FIFO 中帧的数量。

第 2 步 ： 通 过 CAN_RFIFOMIx ， CAN_RFIFOMPx ， CAN_RFIFOMDATA0x 和CAN_RFIFOMDATA1x 读取数据。

第 3 步：将寄存器 CAN_RFIFOx 的 RFD 置 1 释放邮箱，并且等待其由硬件自动清 0。

## 26.3.5. 过滤功能

一个待接收的数据帧会根据其标识符（Identifier）进行过滤：硬件会将通过过滤的帧送至接收FIFO，并丢弃没有通过过滤的帧。

## 过滤器位宽

CAN0 和 CAN1 的过滤器包含 28 个单元，它们是 bank0 到 bank27。CAN2 的过滤器包含 14个独立的单元。

每一个过滤器单元有 2 个寄存器 CAN_FxDATA0 和 CAN_ FxDATA1，它们可以配置为 2 种位宽：32-bit 位宽和 16-bit 位宽。

32-bit 位宽：CAN_FxDATAy 包含字段 SFID[10:0]，EFID[17:0]，FF 和 FT。如 26-5. 32-bit位宽过滤器所示。


图 26-5. 32-bit 位宽过滤器


<table><tr><td>FDATA[31:21]</td><td colspan="2">FDATA[20:3]</td><td colspan="3">FDATA[2:0]</td></tr><tr><td></td><td colspan="2"></td><td colspan="3"></td></tr><tr><td>SFID[10:0]</td><td colspan="2">EFID[17:0]</td><td>FF</td><td>FT</td><td>0</td></tr></table>

16-bit 位宽：CAN_FxDATAy 包含字段：SFID[10:0]，FT，FF 和 EFID[17:15]。如 26-6. 16-bit 所示。


图 26-6. 16-bit 位宽过滤器


<table><tr><td colspan="2">FDATA[31:21]</td><td colspan="2">FDATA[20:16]</td><td colspan="2">FDATA[15:5]</td><td colspan="2">FDATA[4:0]</td></tr><tr><td colspan="8"></td></tr><tr><td>SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td><td>SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td></tr></table>

## 掩码模式

对于一个待过滤的数据帧的标识符（Identifier），掩码模式用来指定哪些位必须与预设的标识符相同，哪些位无需判断。

一个 32-bit 位宽掩码模式过滤器如 26-7. 32-bit 所示。


图 26-7. 32-bit 位宽掩码模式过滤器


<table><tr><td rowspan="2">IDMask</td><td>FDATA0[31:21]</td><td colspan="2">FDATA0[20:3]</td><td colspan="2">FDATA0[2:0]</td></tr><tr><td>FDATA1[31:21]</td><td colspan="2">FDATA1[20:3]</td><td colspan="2">FDATA1[2:0]</td></tr><tr><td></td><td>SFID[10:0]</td><td>EFID[17:0]</td><td>FF</td><td>FT</td><td>0</td></tr></table>


图 26-8. 16-bit 位宽掩码模式过滤器


<table><tr><td rowspan="2">IDMask</td><td>FDATA0[15:5]</td><td>FDATA0[4:0]</td><td>FDATA1[15:5]</td><td>FDATA1[4:0]</td><td></td></tr><tr><td>FDATA0[31:21]</td><td>FDATA0[20:16]</td><td>FDATA1[31:21]</td><td>FDATA1[20:16]</td><td></td></tr><tr><td colspan="5"></td><td></td></tr><tr><td colspan="2">SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td><td></td></tr><tr><td colspan="3">SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td></tr></table>

## 列表模式

对于一个待过滤的数据帧的标识符（Identifier），列表模式用来表示与预设的标识符列表中能够匹配则通过，否则丢弃。

一个 32-bit 位宽列表模式过滤器如 26-9. 32-bit 所示。


图 26-9. 32-bit 位宽列表模式过滤器


<table><tr><td>ID</td><td>FDATA0[31:21]</td><td>FDATA0[20:3]</td><td colspan="3">FDATA0[2:0]</td></tr><tr><td>ID</td><td>FDATA1[31:21]</td><td>FDATA1[20:3]</td><td colspan="3">FDATA1[2:0]</td></tr><tr><td></td><td>SFID[10:0]</td><td>EFID[17:0]</td><td>FF</td><td>FT</td><td>0</td></tr></table>


图 26-10. 16-bit 位宽列表模式过滤器


<table><tr><td>ID</td><td colspan="2">FDATA0[31:21]</td><td colspan="2">FDATA0[20:16]</td><td colspan="2">FDATA0[15:5]</td><td colspan="2">FDATA0[4:0]</td></tr><tr><td></td><td>SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td><td>SFID[10:0]</td><td>FT</td><td>FF</td><td>EFID[17:15]</td></tr></table>

## 过滤序号

过滤器由若干过滤单元（Bank）组成，每个过滤单元因为位宽和模式的选择不同，而具有不同的过滤效果。例如 26-1. 32-bit 所示的 2 个过滤单元，Bank0 是 32-bit 位宽掩码模式，Bank1 是 32-bit 位宽列表模式。


表 26-1. 32-bit 过滤序号


<table><tr><td>过滤单元</td><td>过滤器数据寄存器</td><td>过滤序号</td></tr><tr><td rowspan="2">0</td><td>F0DATA0-32bit-ID</td><td rowspan="2">0</td></tr><tr><td>F0DATA1-32bit-Mask</td></tr><tr><td rowspan="2">1</td><td>F1DATA0-32bit-ID</td><td>1</td></tr><tr><td>F1DATA1-32bit-ID</td><td>2</td></tr></table>

## 过滤器关联的 FIFO

28 个过滤单元均可以关联接收 FIFO0 或接收 FIFO1。一旦一个过滤单元关联到接收 FIFO，

只有通过这个过滤单元的帧才会被传送到接收 FIFO 中存储。

## 过滤器激活控制

一个过滤单元如果被应用程序用到，就必须激活。通过 CAN_FW 寄存器可以进行配置。

## 过滤索引

一个包含过滤序号（Fiter Number）N 的过滤单元通过了某个帧，则该帧数据的过滤索引（Filtering Index）为 N。这时 CAN_RFIFOMPx 中 FI 的值为 N。

在 26-2. 中，如果一个帧通过了 FIFO0 中过滤序号 10（Filter Number=10）的过滤单元，那么该帧的过滤索引为 10。这时 CAN_RFIFOMPx 中 FI 的值为 10。

过滤序号不关心对应的过滤单元（Bank）是否处于工作状态。例如 Bank3 被关联到 FIFO0，且为“不激活”状态，但它仍然包含过滤序号 3 和 4。


表 26-2. 过滤索引


<table><tr><td>过滤单元</td><td>FIFO0</td><td>激活</td><td>过滤序号</td><td>过滤单元</td><td>FIFO1</td><td>激活</td><td>过滤序号</td></tr><tr><td rowspan="2">0</td><td>F0DATA0-32bits-ID</td><td rowspan="2">是</td><td rowspan="2">0</td><td rowspan="4">2</td><td>F2DATA0[15:0]-16bits-ID</td><td rowspan="4">是</td><td rowspan="2">0</td></tr><tr><td>F0DATA1-32bits-Mask</td><td>F2DATA0[31:16]-16bits-Mask</td></tr><tr><td rowspan="2">1</td><td>F1DATA0-32bits-ID</td><td rowspan="2">是</td><td>1</td><td>F2DATA1[15:0]-16bits-ID</td><td rowspan="2">1</td></tr><tr><td>F1DATA1-32bits-ID</td><td>2</td><td>F2DATA1[31:16]-16bits-Mask</td></tr><tr><td rowspan="4">3</td><td>F3DATA0[15:0]-16bits-ID</td><td rowspan="4">否</td><td rowspan="2">3</td><td rowspan="2">4</td><td>F4DATA0-32bits-ID</td><td rowspan="2">否</td><td rowspan="2">2</td></tr><tr><td>F3DATA0[31:16]-16bits-Mask</td><td>F4DATA1-32bits-Mask</td></tr><tr><td>F3DATA1[15:0]-16bits-ID</td><td rowspan="2">4</td><td rowspan="2">5</td><td>F5DATA0-32bits-ID</td><td rowspan="2">否</td><td>3</td></tr><tr><td>F3DATA1[31:16]-16bits-Mask</td><td>F5DATA1-32bits-ID</td><td>4</td></tr><tr><td rowspan="4">7</td><td>F7DATA0[15:0]-16bits-ID</td><td rowspan="4">否</td><td>5</td><td rowspan="4">6</td><td>F6DATA0[15:0]-16bits-ID</td><td rowspan="4">是</td><td>5</td></tr><tr><td>F7DATA0[31:16]-16bits-ID</td><td>6</td><td>F6DATA0[31:16]-16bits-ID</td><td>6</td></tr><tr><td>F7DATA1[15:0]-16bits-ID</td><td>7</td><td>F6DATA1[15:0]-16bits-ID</td><td>7</td></tr><tr><td>F7DATA1[31:16]-16bits-ID</td><td>8</td><td>F6DATA1[31:16]-16bits-ID</td><td>8</td></tr><tr><td rowspan="2">8</td><td>F8DATA0[15:0]-16bits-ID</td><td rowspan="2">是</td><td>9</td><td rowspan="2">10</td><td>F10DATA0[15:0]-16bits-ID</td><td rowspan="2">否</td><td rowspan="2">9</td></tr><tr><td>F8DATA0[31:16]-16bits-ID</td><td>10</td><td>F10DATA0[31:16]-16bits-Mask</td></tr><tr><td rowspan="2"></td><td>F8DATA1[15:0]-16bits-ID</td><td rowspan="2"></td><td>11</td><td rowspan="2"></td><td>F10DATA1[15:0]-16bits-ID</td><td rowspan="2"></td><td rowspan="2">10</td></tr><tr><td>F8DATA1[31:16]-16bits-ID</td><td>12</td><td>F10DATA1[31:16]-16bits-Mask</td></tr><tr><td rowspan="4">9</td><td>F9DATA0[15:0]-16bits-ID</td><td rowspan="4">是</td><td rowspan="2">13</td><td rowspan="4">11</td><td>F11DATA0[15:0]-16bits-ID</td><td rowspan="4">否</td><td>11</td></tr><tr><td>F9DATA0[31:16]-16bits-Mask</td><td>F11DATA0[31:16]-16bits-ID</td><td>12</td></tr><tr><td>F9DATA1[15:0]-16bits-ID</td><td rowspan="2">14</td><td>F11DATA1[15:0]-16bits-ID</td><td>13</td></tr><tr><td>F9DATA1[31:16]-16bits-Mask</td><td>F11DATA1[31:16]-16bits-ID</td><td>14</td></tr><tr><td rowspan="2">12</td><td>F12DATA0-32bits-ID</td><td rowspan="2">是</td><td rowspan="2">15</td><td rowspan="2">13</td><td>F13DATA0-32bits-ID</td><td rowspan="2">是</td><td>15</td></tr><tr><td>F12DATA1-32bits-Mask</td><td>F13DATA1-32bits-ID</td><td>16</td></tr></table>

## 优先级

过滤器优先级规则如下：

1、32-bits 位宽模式高于 16-bits 位宽模式；

2、列表模式高于掩码模式；

3、较小的过滤序号（Filter Number）具有较高的优先级。

## 26.3.6. 时间触发通信

时间触发通信是 CAN 数据链路层应用协议。CAN 网络中的所有节点都按照一个预先设定的时间序列进行通信，尤其适合于时间周期性应用和时间确定性应用。

在这种通信模式下，一个内部的 16-bit 计数器开始工作，在每一个 CAN 位时间（Bit time）增1。这个内部计数器为数据发送和数据接收提供时间戳，这些时间戳存放在寄存器CAN_RFIFOMPx 和 CAN_TMPx 中。

在这种通信模式下，自动重发功能是禁止的。

## 26.3.7. 通信参数

## 自动重发禁止模式

在时间触发通信模式下，要求自动重发必须是禁止的，可以通过将 CAN_CTL 寄存器的 ARD位置 1 满足要求。

在这种模式下，数据只会被发送一次，如果因为仲裁失败或者总线错误而导致发送失败，CAN总线控制器不会像通常那样进行数据自动重发。

发送结束时，寄存器CAN_TSTAT的MTF位被硬件置1，而发送状态信息可以通过MTFNERR，MAL 和 MTE 获得。

## 位时序（Bit time）

CAN 协议采用位同步传输方式。这种方式不仅增大了传输容量，而且意味着需要一种复杂的位同步方法。面向字节传输的位同步方式适用于接收在每个字节前都有起始位的情况，而同步传输协议只要求数据帧的最开始有一个起始位。为保证接收器能正确读取信息，需要不断地进行重新同步。因此，在相位缓冲段采样点前面和后面都应该插入一个帧间隔。

可以通过位操作仲裁方式访问 CAN 总线。信号从发送器到接收器，再回到发送器必须在一个位时间内完成。为了达到同步的目的，除了相位缓冲段外，还需要一个传输延时段。在信号传输过程中，传输延时段被视为发送或接收延时。

CAN 总线控制器将位时间分为 3 个部分。

同步段（Synchronization segment），记为 SYNC_SEG。该段占用 1 个时间单元 $( \mathbf { \nabla } \mathbf { \mathcal { 1 } } \times \bigsqcup _ { \bigstar } )$ 0

位段 1（Bit segment 1），记为 BS1。该段占用 1 到 16 个时间单元。相对于 CAN 协议而言，BS1 相当于传播时间段（Propagation delay segment）和相位缓冲段 1（Phase buffer segment1）。

位段 2（Bit segment 2），记为 BS2。该段占用 1 到 8 个时间单元。相对于 CAN 协议而言，BS2 相当于相位缓冲段 2（Phase buffer segment 2）。

对比与 CAN 协议，位时序如 26-11. 所示。


图 26-11. 位时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/ea150f28944852084e3e3419c23b8a7cbdc62d2c13ff0e049217b0766a8399bd.jpg)


再同步补偿宽度 SJW（resynchronization Jump Width）对 CAN 网络节点同步误差进行补偿，占用 1 到 4 个时间单元。

有效跳变沿定义为只有当在前一个采样点检测到的总线状态为隐性（recessive）时，一个位时间内从隐性位到显性位的第一次转变。

如果有效跳变在 BS1 期间被检测到，而不是 SYNC_SEG 期间，BS1 将会最多被延长 SJW，因此采样点延时。

相反，如果有效跳变在 BS2 期间被检测到，而不是 SYNC_SEG 期间，BS2 将会最多被缩短SJW，因此采样点提前。

注：有关硬同步和再同步的详细说明，请参考ISO 11898标准。

波特率

波特率计算公式如下：

$$
\text { BaudRate } = \frac {1}{\text { Normal   Bit   Time }}\tag{26-1}
$$

$$
\text { Normal   Bit   Time } = t _ {\text { SYNC\_SEG }} + t _ {\text { BS1 }} + t _ {\text { BS2 }}\tag{26-2}
$$

其中：

$$
t _ {\text { SYNC\_SEG }} = 1 \times t _ {q}\tag{26-3}
$$

$$
t _ {B S 1} = (1 + B T. B S 1) \times t _ {q}\tag{26-4}
$$

$$
\mathrm{t} _ {\mathrm{BS2}} = (1 + \mathrm{BT.BS2}) \times \mathrm{t} _ {\mathrm{q}}\tag{26-5}
$$

$$
t _ {q} = (1 + B T. B A U D P S C) \times t _ {P C L K 1}
$$

(26-6) 

## 26.3.8. CAN-FD 操作

通过将 CAN_FDCTL 寄存器的 FDEN 位置 1，可以使能 CAN FD (CAN with Flexible Data rate)功能。如果 FDEN 位被清 0，CAN 总线控制器仅支持常规帧（标准帧和扩展帧）的收发，若FDEN 位被置 1，则 CAN 总线控制器同时支持常规帧（标准帧和扩展帧）以及 FD 帧的收发。根据协议，当前帧是否为 FD 帧是通过帧的 FDF 位来判断（在常规帧中该位为保留位）。如果FDF 位为隐性，表示是 CAN FD 帧；如果为显性，表示是常规帧。

通过配置CAN_FDCTL寄存器的NISO位，可以选择CAN-FD功能支持ISO11898-1或BOSCHCAN FD 规范 V1.0。

在 CAN-FD 帧的帧结构中，FDF 位之后是保留位和 BRS位。BRS位决定数据位速率，当 BRS位为显性时，表示不能通过配置 CAN_DBT 寄存器来切换数据位速率。当 BRS 位为隐性时，可以通过配置 CAN_DBT 寄存器使得数据段（从 BRS 位到 ACK 场之前）的位速率高于仲裁段的位速率。详情请参考 ISO11898-1 或 BOSCH CAN FD 规范 V1.0。

通过将 CAN_FDCTL 寄存器的 PRED 位清 0，可以使能协议异常处理功能。此时，在接收帧数据过程中检测到隐性的保留位时，该功能将使操作状态转变为 IDLE 并在下一个采样点中止当前帧。反之，将 PRED 位置 1，该功能将被禁止，隐性的保留位将被视为格式错误，并当做错误帧来进行处理，同时 CAN_FDSTAT 寄存器的 PRE位将被置 1。

ISO11898-1 或 BOSCH CAN FD 规范 V1.0 规定的发送 ESI 位（该位位于 CAN FD 帧的 DLC位域之前）功能通过 CAN_FDCTL 寄存器的 ESIMOD 位和 CAN_TMPx 寄存器的 ESI 位来实现。如果将 ESIMOD 位清 0，当 CAN 总线控制器处于被动错误状态时，该位为隐性；当处于主动错误状态时，该位为显性。若将 ESIMOD 位置 1，将根据 CAN_TMPx 寄存器的 ESI 位的值来决定该位为显性还是隐性。

发送帧 FDF 位和 BRS 位的总线电平逻辑由 CAN_TMPx 寄存器的 FDF 位和 BRS 位的值决定。

## 26.3.9. 传输延迟补偿

CAN-FD 协议支持传输延迟补偿机制。由于 CAN 收发器存在回路延迟，因此当发送 CAN-FD帧的高速数据段的位时间长度小于收发器内部回路延迟的限定值时，该机制可以避免当采样点到来时发送节点还没有收到其自己发出的位，从而报错的情况发生。关于传输延迟补偿的具体定义，请参考 ISO11898-1 或 BOSCH CAN FD 规范 V1.0。

将 CAN_FDCTL 寄存器的 TDCEN 位置 1 将使能传输延迟补偿。

传输延迟补偿机制可以调节次级采样点（SSP）的位置。SSP_Delay被定义为 CANTX 上的信号到 SSP 采样点的延迟。如果 CAN_FDCTL 寄存器的 TDCMOD 位被置 1，SSP_Delay 的值由 CAN_FDTDC 寄存器的 TDCO 位域软件配置决定。如果 TDCMOD 位被清 0，硬件将自动计算位速率转换之前的 FDF 位到 RES0 位的下降沿在 CAN_TX 与 CAN_RX 上出现的延迟，并将计算值存入 CAN_FDSTAT 寄存器的 TDCV 位域。由于存在信号毛刺，可能导致硬件自动计算的 SSP 位置比预期的提前，为了避免 TDCV 的值过小，可以使用 CAN_FDTDC 寄存器的 TDCF 位域。如果 TDCV 的值大于 TDCF，SSP_Delay 的值被定义为 TDCO 加上 TDCV，否则 SSP_Delay 的值被定义为 TDCO 加上 TDCF。

SSP_Delay的值不能大于 3 个数据位时间。


图 26-12 传输延迟测量


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/2ec23652-00b6-4360-8c3f-50f5b87204b9/3a3a104ff738381a14d9bdd0a4f2422a24434b0b598840255fa78780ae15c982.jpg)


## 26.3.10. 错误标志

CAN 总线的状态可以通过 CAN_ERR 寄存器的发送错误计数值（Transmit Error Counter，TECNT）和接收错误计数值（Receive Error Counter， RECNT）反映，其值会根据错误的情况由硬件增加或减少，软件可以通过这些值判断 CAN 网络的稳定性。关于错误计数值的详细信息请参考 CAN 协议相关章节。

通过使能 CAN_INTEN 寄存器中的相应位（ERRIE等），软件可以在检测到错误时产生相应中断。

## 离线恢复

当 TECNT 大于 255 时，CAN 总线控制器进入离线状态，这时寄存器 CAN_ERR 中的 BOERR置 1，并且发送和接收失效。

根据寄存器 CAN_CTL 中的 ABOR 配置，离线恢复（变为主动错误状态）有 2 种方式。这两种方式都要求处于离线状态的 CAN 总线控制器检测到 CAN 协议所定义的离线恢复序列（在CAN_RX 检测到 128 次连续 11 个位的隐性位）时，才会自动恢复。

如果 ABOR 为 1，将在检测到离线恢复序列后自动恢复。

如果 ABOR 为 0，则必须先将 CAN_CTL 中的 IWMOD 置 1 进入初始化工作模式，然后进入正常工作模式并在检测到离线恢复序列后恢复。

## 26.3.11. 中断

CAN 总线控制器占用 4 个中断向量，通过寄存器 CAN_INTEN 进行控制。

这 4 个中断向量对应 4 类中断源：

 发送中断；

 FIFO0 中断；

 FIFO1 中断；

 错误和状态改变中断。

## 发送中断

发送中断包括：

寄存器CAN_TSTAT中的MTF0置1：发送邮箱0变为空闲。

寄存器CAN_TSTAT中的MTF1置1：发送邮箱1变为空闲。

寄存器CAN_TSTAT中的MTF2置1：发送邮箱2变为空闲。

## FIFO0 中断

FIFO0 中断包括：

FIFO0中包含待接收数据：寄存器CAN_RFIFO0中的RFL0不为0，CAN_INTEN寄存器中RFNEIE0被置位；

FIFO0满：寄存器CAN_RFIFO0中的RFF0为1，CAN_INTEN寄存器中RFFIE0被置位；

FIFO0溢出：寄存器CAN_RFIFO0中的RFO0为1，CAN_INTEN寄存器中RFOIE0被置位。

## FIFO1 中断

FIFO1 中断包括：

FIFO1中包含待接收数据：寄存器CAN_RFIFO1中的RFL1不为0，CAN_INTEN寄存器中RFNEIE1被置位；

FIFO1满：寄存器CAN_RFIFO1中的RFF1为1，CAN_INTEN寄存器中RFFIE1被置位；

FIFO1溢出：寄存器CAN_RFIFO1中的RFO1为1，CAN_INTEN寄存器中RFOIE1被置位。

## 错误和工作模式改变（EWMC）中断

错误和工作模式改变中断可由以下条件触发：

错误：CAN_STAT寄存器的ERRIF和CAN_INTEN寄存器的ERRIE被置位，请参考CAN_STAT寄存器中ERRIF位描述；

– 唤醒：CAN_STAT寄存器中的WUIF和CAN_INTEN寄存器的WIE被置位；

进入睡眠模式：CAN_STAT寄存器中的SLPIF和CAN_INTEN寄存器的SLPWIE被置

CAN 总线控制器的中断产生条件可参考 26-3. CAN / 。


表 26-3. CAN 事件/中断标志


<table><tr><td>中断事件</td><td colspan="2">事件/中断标志</td><td colspan="2">使能控制位</td></tr><tr><td rowspan="3">发送中断</td><td colspan="2">发送邮箱0空闲标志MTF0</td><td rowspan="3" colspan="2">TMEIE</td></tr><tr><td colspan="2">发送邮箱1空闲标志MTF1</td></tr><tr><td colspan="2">发送邮箱2空闲标志MTF2</td></tr><tr><td rowspan="3">FIFO0中断</td><td colspan="2">接收FIFO0中帧的数量RFL0[1:0]</td><td colspan="2">RFNEIE0</td></tr><tr><td colspan="2">接收FIFO0满RFF0</td><td colspan="2">RFFIE0</td></tr><tr><td colspan="2">接收FIFO0溢出RFO0</td><td colspan="2">RFOIE0</td></tr><tr><td rowspan="3">FIFO1中断</td><td colspan="2">接收FIFO1中帧的数量RFL1[1:0]</td><td colspan="2">RFNEIE1</td></tr><tr><td colspan="2">接收FIFO1满RFF1</td><td colspan="2">RFFIE1</td></tr><tr><td colspan="2">接收FIFO1溢出RFO1</td><td colspan="2">RFOIE1</td></tr><tr><td rowspan="6">EWMC中断</td><td>警告错误WERR</td><td rowspan="4">错误中断标志ERRIF</td><td>WERRIE</td><td rowspan="4">ERRIE</td></tr><tr><td>被动错误PERR</td><td>PERRIE</td></tr><tr><td>离线错误BOERR</td><td>BOIE</td></tr><tr><td>错误种类1&lt;=ERRN[2:0]&lt;=6</td><td>ERRNIE</td></tr><tr><td colspan="2">从睡眠工作模式唤醒的状态改变中断标志WUIF</td><td colspan="2">WIE</td></tr><tr><td colspan="2">进入睡眠工作模式的状态改变中断标志SLPIF</td><td colspan="2">SLPWIE</td></tr></table>

