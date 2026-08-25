## 29. 通用串行总线全速接口（USBFS）

## 29.1. 概述

USB全速（USBFS）控制器为便携式设备提供了一套USB互联解决方案。USBFS支持主机模式和设备模式。USBFS包含了一个内部的全速USB PHY，并且不再需要外部PHY芯片。USBFS可以支持USB 2.0协议所定义的所有四种传输方式（控制传输、批量传输、中断传输和同步传输）。

## 29.2. 主要特性

 支持USB 2.0全速（12Mb/s）/低速（1.5Mb/s）主机模式；

 支持USB 2.0全速（12Mb/s）设备模式；

 支持所有的4种传输方式：控制传输、批量传输、中断传输和同步传输；

 在主机模式下，包含USB事务调度器，用于有效地处理USB事务请求；

 包含一个1.25KB的FIFO RAM；

 在主机模式下，支持8个通道；

 在主机模式下，包含2个发送FIFO（周期性发送FIFO和非周期性发送FIFO）和1个接收FIFO（由所有的通道共享）；

 在设备模式下，包含4个发送FIFO（每个IN端点一个发送FIFO）和1个接收FIFO（由所有的OUT端点共享）；

 在设备模式下，支持4个OUT端点和4个IN端点；

 在设备模式下，支持远程唤醒功能；

 包含一个支持USB协议的全速USB PHY；

 在主机模式下，SOF的时间间隔可动态调节；

 可将SOF脉冲输出到PAD；

 在主机模式下，需要外部部件为连接的USB设备提供电源。

## 29.3. 结构框图


图 29-1. USBFS 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/446d7392c8a50e8ef3b8ce79c8db4221e877d44570207a2f732aed5f4edbee5d.jpg)


## 29.4. 信号线描述


表 29-1. USBFS 信号线描述


<table><tr><td>I/O 端口</td><td>类型</td><td>描述</td></tr><tr><td>DM</td><td>输入/输出</td><td>差分信号 D-端口</td></tr><tr><td>DP</td><td>输入/输出</td><td>差分信号 D+端口</td></tr><tr><td>SOF</td><td>输出</td><td>USB SOF 信号输出</td></tr></table>

## 29.5. 功能描述

## 29.5.1. USBFS 时钟及工作模式

USBFS可以作为一个主机、一个设备，并且包含一个内部全速PHY。USBFS可支持的最大速率为全速。

内部PHY支持全速和低速的主机模式、全速的设备模式。USBFS所使用的USB时钟需要配置为48MHz。该48MHz USB时钟从系统内部时钟产生，并且其时钟源和分频器需要在RCU模块中配置。

上拉或下拉电阻已经集成在内部全速PHY的内部，并且USBFS可根据当前模式（主机、设备）和连接状态进行自动控制。一个利用内部全速PHY的典型连接示意图如 29-2.连接示意图所示。


图 29-2. 在主机或设备模式下连接示意图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/907bc25556a2e7441905e207eeb72a603c3f342964a07834ff5068cc78a27917.jpg)


当 USBFS 工作在主机模式下时（FHM 控制位置位、FDM 控制位清除），VBUS 为 USB 协议所定义的 5V 电源检测引脚。内部 PHY不能提供 5V VBUS 电源，仅在 VBUS 信号线上具有电压比较器和充电、放电电路。所以，如果应用需要提供 VBUS 电源，那么则需要一个外部的供电电源 IC。在主机模式下，USBFS 和 USB 连接头之间的 VUBS 连接可以被忽略，这是由于 USBFS 并不检测 VBUS引脚的电平状态，并假定 5V供电电源一直存在。

## 29.5.2. USB 主机功能

## USB主机端口状态

主机应用可以通过 USBFS_HPCS 寄存器控制 USB 端口状态。系统初始化之后，USB 端口保持掉电状态。通过软件置位 PP控制位后，内部 USB PHY 将被上电，并且 USB 端口变为断开状态。检测到连接后，USB 端口变为连接状态。在 USB 总线上产生一个复位后，USB 端口将变为使能状态。


图 29-3. 主机端口状态转移图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/6022308b78ee11f8223bb7e023258585353e84697f5e7bab75fe7dcd28a95e5d.jpg)


## 连接、复位和速度识别

作为 USB 主机，在检测到一个连接事件后，USBFS 会为应用触发一个连接标志；同样，若检测到一个断开事件后，将会触发一个断开标志。

PRST 控制位用于实现 USB 复位序列。应用可以置位该控制位以启动一个 USB 复位序列，或者清除该控制位以结束 USB 复位序列。仅当端口在连接或使能状态时，该控制位有效。

USBFS在对设备连接和复位时执行速度检测，并且速度检测的结果会反馈在 USBFS_HPCS 寄存器的 PS位域中。USBFS 以 DM 或 DP 的电平状态确定设备速度，如 USB 协议所描述，全速设备上拉 DP信号线，而低速设备上拉 DM 信号线。

## 挂起和复位

USBFS 支持挂起和复位状态，当 USBFS 端口在使能状态时，向 USBFS_HPCS 寄存器的 PSP控制位写 1，USBFS 会进入到挂起状态。在挂起状态下，USBFS 停止在 USB 总线上发送 SOF，并且这样会让所连接的 USB 设备在 3ms 后进入挂起状态。应用程序能够置位 USBFS_HPCS 寄存器中的 PREM 控制位以启动一个恢复序列，从而唤醒挂起的设备，当清除该控制位时，则可以停止恢复序列。如果主机在挂起状态下检测到一个远程唤醒信号，将会置位 USBFS_GINTF 寄存器的WKUPIF 标志位，并且触发 USBFS唤醒中断。

## SOF产生器

在主机模式下，USBFS 向 USB 总线发送 SOF 令牌包。如 USB 2.0 协议所描述，全速连接下，每毫秒产生一次 SOF 令牌包（由主机控制器或者 HUB 事务转换器产生）。

每当 USBFS 进入到使能状态后，它将会按照 USB2.0 所定义的周期发送 SOF 令牌包。然而，应用程序可以通过写 USBFS_HFT 寄存器中的 FRI 位来调整一帧的间隔。FRI 位定义了在一帧中的USB 时钟周期个数，并且应用程序应该基于 USBFS 所使用的 USB时钟频率计算该值。FRT 位显示当前帧剩余的时钟周期个数，并且在挂起状态时，该值将停止改变。

USBFS 能够在每个 SOF 令牌包中产生一个脉冲信号，并且将其输出至一个引脚。该脉冲信号长度为 12 个 HCLK 周期。如果应用程序希望使用该功能，需要置位 USBFS_GCCFG 寄存器的SOFOEN 控制位，并且配置相应的引脚寄存器为 GPIO 功能。

## USB通道和事务

USBFS 在主机模式下包含 8 个独立的通道。每个通道能够与一个 USB 设备端点通信。通道的传输类型、方向、数据包长和其他信息都在通道相应的寄存器中配置，例如 USBFS_HCHxCTL 和USBFS_HCHxLEN 寄存器。

USBFS支持所有的四种传输类型：控制、批量、中断和同步。USB 2.0 协议将这些传输类型划分为两类：非周期性传输（控制和批量）和周期性传输（中断和同步）。基于此，为了有效地进行事务调度，USBFS 包含两种请求队列：周期性请求队列和非周期性请求队列。在上述请求队列中的请求条目可能代表一个 USB 事务请求或者一个通道操作请求。

如果应用程序想要在 USB 总线上启动一个 OUT 事务，需要通过 AHB寄存器接口向数据 FIFO 中写入数据包。USBFS 硬件会在整包数据写完后，自动产生一个事务请求并进入请求队列。

请求队列中的请求条目通过事务控制模块按顺序处理。USBFS通常首先尝试处理周期性请求队列，然后处理非周期性请求队列。

帧起始后，USBFS 首先开始处理周期性队列，直到队列为空抑或当前周期性请求队列所需时间不够，然后处理非周期性队列。这种做法保证了一帧中周期性传输的带宽。每次 USBFS 从请求队列中读取并取出一个请求条目。如果取出的是通道禁用请求，这将直接禁用通道并准备处理下个条目。

如果当前请求是一个事务请求并且 USB总线时间能够处理这个请求，USBFS 会使用 SIE在 USB总线上产生该事务。

在当前帧内，当前请求所需的总线时间不足时，如果当前请求为周期性请求，USBFS 停止处理该周期性请求队列，并启动处理非周期性请求。如果当前请求为非周期性请求，USBFS 会停止处理任何队列，并等待直到当前帧结束。

## 29.5.3. USB 设备功能

## USB设备连接

在设备模式下，USBFS 在初始化后保持掉电状态。利用 VBUS 引脚上的 5V 电源连接 USB 主机后，USBFS 将进入供电状态。USBFS 首先打开 DP 信号线上的上拉电阻，之后主机将会检测到一个连接事件。

## 复位和速度识别

USB 主机在检测到设备连接之后，总是会启动一个 USB 复位序列，并且在设备模式下，检测到USB 总线复位事件后，USBFS 会为软件触发一个复位中断。

在复位序列后，USBFS 将会触发 USBFS_GINTF 寄存器中的 ENUMF 中断，并且利用USBFS_DSTAT 寄存器内的 ES 标志位指示当前枚举设备速度，该位总是为 0b ‘11’（全速）。

如 USB 2.0 协议所描述，USBFS在外设模式下不支持低速。

## 挂起和唤醒

USB 总线保持 IDLE 状态并且数据线 3 毫秒无变化，USB 设备将会进入挂起状态。当 USB 设备在挂起状态时，软件能够关闭大部分的时钟以节省电能。USB主机可以通过在 USB 总线上产生恢复信号，来唤醒挂起的设备。USBFS检测到恢复信号后，将置位USBFS_GINTF寄存器的WKUPIF标志位并且触发 USBFS 唤醒中断。

在挂起设备模式，USBFS 也能够远程唤醒 USB 总线。软件可以通过置位 USBFS_DCTL 寄存器的 RWKUP 控制位来发送一个远程唤醒信号，并且如果 USB 主机支持远程唤醒，主机会在 USB总线上启动发送一个恢复信号。

## 软件断开

USBFS 支持软件断开。设备进入到供电状态后，USBFS 会打开 DP 信号线的上拉电阻，并且这样主机会检测到设备连接。然后，软件可以通过置位 USBFS_DCTL 寄存器中 SD 控制位进行强制断开。在 SD 控制位被置位后，USBFS 将会直接关闭上拉电阻。这样，USB 主机将会在 USB 总线上检测到设备断开。

## SOF跟踪

当 USBFS 在 USB 总线上接收到一个 SOF 令牌包时，将触发一个 SOF 中断，并且开始利用本地USB 时钟计算总线时间。当前帧的帧号将会反应在 USBFS_DSTAT 寄存器的 FNRSOF 位域中。当 USB 总线时间达到 EOF1 或 EOF2 点（帧结束，在 USB 2.0 协议中描述），USBFS 会触发USBFS_GINTF 寄存器中的 EOPFIF 中断。软件能够使用这些标志位和寄存器以获得当前总线时间和位置信息。

## 29.5.4. 数据 FIFO

USBFS 中采用 1.25K 字节数据 FIFO 存储包数据，数据 FIFO 是通过 USBFS 的内部 SRAM 实现的。

## 主机模式

主机模式下，数据 FIFO 空间分为三个部分，分别是：用于接收数据包的 Rx FIFO、用于非周期性发送数据包的非周期性 Tx FIFO 和用于周期性发送数据包的周期性 Tx FIFO。所有的 IN 通道通过共享 Rx FIFO 接收数据。所有的周期性 OUT 通道通过共享周期性 Tx FIFO 来发送数据，所有的非周期性 OUT 通道通过共享非周期性 Tx FIFO 来发送数据。通过寄存器 USBFS_GRFLEN、USBFS_HNPTFLEN 和 USBFS_HPTFLEN，软件可以配置以上数据 FIFO 的大小和起始偏移地址。 29-4. FIFO 所描述的是 SRAM 中各 FIFO 的结构，图中的数值是按照 32 位为单位写的。


图 29-4. 主机模式 FIFO 空间


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/e956299347bb1c83f99130e1dfc9a89ec8f04235d753ae474afdc78ff81ca01b.jpg)


USBFS 为程序提供了专有寄存器空间来读写数据 FIFO。 29-5. FIFO所描述的是数据 FIFO 所访问的寄存器存储空间，图中的数值是以字节为单位寻址。尽管所有的非周期通道共享相同的 FIFO 以及所有的周期通道共享相同的 FIFO，每个通道都拥有它们的FIFO 访问寄存器空间。对 USBFS 而言，获知当前压入数据包的通道号是非常重要的，通过寄存器 USBFS_GRXTATR/USBFS_GRSTATP 来访问数据包所从属的 Rx FIFO。


图 29-5. 主机模式 FIFO 访问寄存器映射表


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/4f7666f5eb8b0110b6e608c5621a59a1f5dd0b3a0fe65e8ac4da24950b2dcd68.jpg)


## 设备模式

在设备模式下，数据 FIFO 分为多个部分，其中包含 1 个 Rx FIFO 和 4 个 Tx FIFO，每个 Tx FIFO对应着一个 IN 端点，所有的 OUT 端点通过共享 Rx FIFO 接收数据包。通过寄存器USBFS_GRFLEN 和 USBFS_DIEPxTFLEN （x=0…3），程序可配置数据 FIFO 的大小和起始偏移地址。 29-6. FIFO 所描述的是 SRAM 中各 FIFO 的结构，图中的数值是以按照 32 位写的。


图 29-6. 设备模式 FIFO 空间


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/09f6bf3651c81c597677b76c72e22cb28de3f243cc32d2303f86a5f36a8f542e.jpg)


USBFS 为程序提供了专有寄存器空间来读写数据 FIFO。 29-7. FIFO所描述的是数据 FIFO 所访问的寄存器存储空间，图中的数值是以字节为单位寻址。每个端点都拥有它们的 FIFO 访问寄存器空间。通过寄存器 USBFS_GRXTATR/USBFS_GRSTATP 来访问Rx FIFO。


图 29-7. 设备模式 FIFO 访问寄存器映射表


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/de1f5f1b808586160f8215339166db76f7f2fa7751a63c009cf777352c02255e.jpg)


## 29.5.5. 操作手册

该部分描述的是 USBFS 的操作手册。

## 主机模式

全局寄存器初始化顺序：

1. 根据应用的需求，如Tx FIFO的空阈值等，设置寄存器USBFS_GAHBCS，此时，GINTEN

位需要保持清零状态；

2. 根据应用的需求，如操作模式（主机、设备），设置寄存器USBFS_GUSBCS；

3. 根据应用的需求，设置寄存器USBFS_GCCFG；

4. 根据应用的需求，设置寄存器USBFS_GRFLEN、USBFS_HNPTFLEN_DIEP0TFLEN、USBFS_HPTFLEN，配置数据FIFO；

5. 通过设置寄存器USBFS_GINTEN使能模式错误和主机端口中断，置位USBFS_GAHBCS寄存器的GINTEN位使能全局中断；

6. 设置寄存器USBFS_HPCS，置位PP位；

7. 等待设备连接，当设备连接后，触发寄存器USBFS_HPCS的PCD位，然后置位PRST位，执行一次端口复位，等待至少10毫秒后，清除PRST位；

8. 等待USBFS_HPCS寄存器的PEDC中断，然后读取PE位以确认端口被成功地使能，读取PS位以获取连接的设备速度，之后，如果软件需要改变SOF间隔，设置USBFS_HFT寄存器。

## 通道初始化和使能顺序：

1. 根据期望的传输类型、方向、包大小等信息，设置寄存器USBFS_HCHxCTL，在设置期间，要保证位CEN和CDIS保持清除；

2. 设置寄存器USBFS_HCHxINTEN，设置期望的中断使能位；

3. 设置寄存器USBFS_HCHxLEN，PCNT表示一次传输中的包数，TLEN表示一次传输中发送或接收的包数据的总字节数；

对于 OUT 通道，如果 PCNT 为 1，单包的大小等于 TLEN。如果 PCNT 大于 1，前 PCNT-1 个包被认定为最大包长度的包，其大小是由寄存器 USBFS_HCHxCTL 的位 MPL 所定义。最后一包的大小可通过 PCNT、TLEN 和 MPL 计算得到。如果程序想要发出一个零长度的包，应该设定 TLEN为 0，PCNT 位 1；

对于 IN 通道，因为在 IN 事务结束之前，程序不知道实际接收的数据大小，程序可将 TLEN 设定为 Rx FIFO 所支持的最大值；

4. 置位寄存器USBFS_HCHxCTL中的CEN位以使能通道。

## 通道除能顺序：

程序可以通过同时置位 CEN 和 CDIS 除能通道。在寄存器操作后，USBFS 将在请求队列中产生一个通道除能请求条目。当这个请求条目到达请求队列的顶部时，USBFS 立即进行处理。

对于 OUT 通道而言，特定的通道将被立即除能。然后，会产生 CH 标志，USBFS 将清除 CEN 和CDIS 位。

对于 IN 通道而言，USBFS 将通道除能状态条目压入 Rx FIFO，然后，程序应该处理 Rx FIFO 非空事件：读和取出该状态条目，然后会产生 CH 标志，USBFS 将清除 CEN 和 CDIS 位。

## IN传输操作顺序：

1. 初始化USBFS全局寄存器；

2. 初始化相应的通道；

3. 使能相应的通道；

4. 通过软件使能IN通道后，USBFS在相应请求队列中生成一个Rx请求条目；

5. 当Rx请求条目到达请求队列的顶部时，USBFS开始执行该请求条目。对于由请求条目所指示的事务而言，如果总线时间足够，USBFS在USB总线上开始IN事务；

6. 当IN事务结束时（收到ACK握手包），USBFS将接收到的数据包压入Rx FIFO，ACK标志位被触发，否则，状态标志（NAK）会指示事务结果；

7. 如果步骤5所描述的IN事务完成后，步骤2的PCNT的数值比1大，程序将会返回步骤3，继续接收剩下的数据包。如果步骤5中描述的IN事务没有成功完成，程序将会返回步骤3来再次发送该数据包；

8. 在所有的传输中的所有事务都被成功接收后，USBFS将TF状态条目压入Rx FIFO的最后的数据包的顶部，这样，软件在读取所有接收的数据包后，再读取TF状态条目。USBFS生成TF标志来指示传输成功结束；

9. 除能通道，当通道处于空闲状态，即可为其他传输做准备。

## OUT传输操作顺序：

1. 初始化USBFS全局寄存器；

2. 初始化及使能相应通道；

3. 将数据包写入通道的Tx FIFO（周期性TxFIFO或非周期性Tx FIFO）。在所有的数据包都被写入FIFO后，USBFS在相应的请求队列中产生一个Tx请求条目，并且将USBFS_HCHxTLEN中的TLEN值减少，减少的数值等于已写的包大小；

4. 当请求条目到达请求队列的顶部时，USBFS开始执行该请求条目。如果请求条目对应的事务的总线时间足够，USBFS在USB总线上开展OUT事务；

5. 当由请求条目所指示的OUT事务结束时，寄存器USBFS_HCHnTLEN的位PCNT减1。如果该事务完成（收到ACK握手包），ACK标志位被触发，否则，状态标志（NAK）会指示事务结果；

6. 如果步骤5所描述的OUT事务完成后且步骤2的PCNT的数值比1大，程序将会返回步骤3，继续发送剩下的数据包。如果步骤5中描述的OUT事务没有成功完成，程序将会返回步骤3来再次发送该包；

7. 在所有的传输中的所有事务都被成功送达后，USBFS生成TF标志来指示传输成功结束；

8. 除能通道，当通道处于空闲状态，即可为其他传输做准备。

## 设备模式

## 全局寄存器初始化顺序：

1. 根据应用的需求，如Tx FIFO的空阈值等，设置寄存器USBFS_GAHBCS，此时，GINTEN位需要保持清零状态；

2. 根据应用的需求，如操作模式（主机、设备），设置寄存器USBFS_GUSBCS；

3. 根据应用的需求，设置寄存器USBFS_GCCFG；

4. 根据应用的需求，设置寄存器USBFS_GRFLEN、USBFS_HNPTFLEN_DIEP0TFLEN、USBFS_HPTFLEN，配置数据FIFO；

5. 通过设置寄存器USBFS_GINTEN使能模式错误、挂起、SOF、枚举完成和USB复位中断，

置位USBFS_GAHBCS寄存器的GINTEN位使能全局中断；

6. 根据应用的需求，如设备的地址等，设置寄存器USBFS_DCFG；

7. 在设备连接上主机上后，主机在USB总线上执行端口复位，触发寄存器USBFS_GINTF的RST中断；

8. 等待寄存器USBFS_GINTF的ENUMF中断。

## 端点初始化和使能顺序：

1. 根 据 预 期 的 传 输 类 型、 包 大 小 等 信 息 ， 设置 寄 存 器 USBFS_DIEPxCTL 或USBFS_DOEPxCTL；

2. 设定寄存器 USBFS_DIEPINTEN 或 USBFS_DOEPINTEN，置位相应中断使能位；

3. 设定寄存器 USBFS_DIEPxLEN 或 USBFS_DOEPxLEN，PCNT 表示一次传输中的包数，TLEN 表示一次传输中发送或接收的数据包的总字节数；

对于 IN 端点，如果 PCNT 等于 1，单数据包的大小等于 TLEN。如果 PCNT 大于 1，前 PCNT-1个包被认定为最大包长度的包，其大小是由寄存器 USBFS_DIEPxCTL 的位 MPL 所定义。最后一包的大小可通过 PCNT、TLEN 和 MPL 计算得到。如果程序想要发出一个零长度的包，应该设定TLEN 为 0，PCNT 位 1；

对于 OUT 端点，因为在 IN 事务结束之前，程序不知道实际接收的数据大小，程序可将 TLEN 设定为 Rx FIFO 所支持的最大值；

4. 置位 USBFS_DIEPxCTL 或 USBFS_DOEPxCTL 寄存器 EPEN 位使能端点。

## 端点除能顺序:

当 USBFS_DIEPxCTL 或 USBFS_DOEPxCTL 寄存器的 EPEN 位被清除时，程序可以在任何时候除能端点

## IN传输操作顺序：

1. 初始化USBFS全局寄存器；

2. 初始化和使能IN端点；

3. 将数据包写入端点的Tx FIFO，每当数据包写入FIFO，USBFS减少USBFS_DIEPxLEN寄存器的TLEN域的数值，其减少的数值等于已写的数据包大小；

4. 当IN令牌接收后，USBFS发送数据包，在USB总线上的事务完成后，USBFS_DIEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果；

5. 在一次传输的所有数据包都被成功发送，USBFS生成一个TF标志位以表明传输成功结束，除能相应IN端点。

## OUT传输操作顺序（DMA除能）：

1. 初始化USBFS全局寄存器；

2. 初始化和使能端点；

3. 当OUT令牌接收后，USBFS接收数据包或基于Rx FIFO状态和寄存器配置回复NAK握手包。如果事务成功完成（USBFS接收并保存数据到Rx FIFO，发送ACK握手包），

USBFS_DOEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果；

4. 在一次传输的所有数据包都被成功接收，USBFS将TF状态条目压入Rx FIFO的最后的数据包的顶部，这样，软件在读取所有接收的数据包后，再读取TF状态条目。USBFS生成TF标志来指示传输成功结束。USBFS生成一个TF标志位以表明传输成功结束，除能相应OUT端点。

## 29.6. 中断

USBFS有两种中断：全局中断、唤醒中断。

全局中断是软件需要处理的主要中断，全局中断的标志位可在 USBFS_GINTF 寄存器读取，列举在 29-2. USBFS 。


表 29-2. USBFS 全局中断


<table><tr><td>中断标志</td><td>描述</td><td>运行模式</td></tr><tr><td>SESIF</td><td>会话中断</td><td>主机或设备模式</td></tr><tr><td>DISCIF</td><td>断开连接中断标志</td><td>主机模式</td></tr><tr><td>PTXFEIF</td><td>周期性 Tx FIFO 空中断标志</td><td>主机模式</td></tr><tr><td>HCIF</td><td>主机通道中断标志</td><td>主机模式</td></tr><tr><td>HPIF</td><td>主机端口中断</td><td>主机模式</td></tr><tr><td>PXNCIF/ ISOONCIF</td><td>周期性传输未完成中断标志 /同步OUT传输未完成中断标志</td><td>主机或设备模式</td></tr><tr><td>ISOINCIF</td><td>同步 IN 传输未完成中断标志</td><td>设备模式</td></tr><tr><td>OEPIF</td><td>OUT 端点中断标志</td><td>设备模式</td></tr><tr><td>IEPIF</td><td>IN 端点中断标志</td><td>设备模式</td></tr><tr><td>EOPFIF</td><td>周期性帧尾中断标志</td><td>设备模式</td></tr><tr><td>ISOOPDIF</td><td>同步 OUT 丢包中断标志</td><td>设备模式</td></tr><tr><td>ENUMF</td><td>枚举完成</td><td>设备模式</td></tr><tr><td>RST</td><td>USB 复位</td><td>设备模式</td></tr><tr><td>SP</td><td>USB挂起</td><td>设备模式</td></tr><tr><td>ESP</td><td>早挂起</td><td>设备模式</td></tr><tr><td>GONAK</td><td>全局OUT NAK有效</td><td>设备模式</td></tr><tr><td>GNPINAK</td><td>全局非周期IN NAK有效</td><td>设备模式</td></tr><tr><td>NPTXFEIF</td><td>非周期Tx FIFO空中断标志</td><td>主机模式</td></tr><tr><td>RXFNEIF</td><td>Rx FIFO非空中断标志</td><td>主机或设备模式</td></tr><tr><td>SOF</td><td>帧首</td><td>主机或设备模式</td></tr><tr><td>MFIF</td><td>模式错误中断标志</td><td>主机或设备模式</td></tr></table>

唤醒中断可以在 USBFS 处于挂起状态时触发，即使 USBFS的时钟停止。寄存器 USBFS_GINTF的位WKUPIF 是唤醒源。
