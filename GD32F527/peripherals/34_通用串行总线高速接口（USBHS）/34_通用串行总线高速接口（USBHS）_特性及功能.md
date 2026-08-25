## 34. 通用串行总线高速接口（USBHS）

## 34.1. 概述

USB高速（USBHS）控制器为便携式设备提供了一套USB互联解决方案。USBHS不仅支持主机模式和设备模式，也支持遵循HNP（主机协商协议）和SRP（会话请求协议）的OTG模式。USBHS为外部USB物理层（PHY）提供了一个ULPI接口，并且其也包含了一个内部的全速USBPHY。所以，对于全速和低速操作，不再需要外部的USB PHY。USBHS可以支持USB 2.0协议所定义的所有四种传输方式（控制传输、批量传输、中断传输和同步传输）。当USBHS操作在高速主机模式下时，USBHS支持HUB连接。另外，在USBHS内部还有一个DMA引擎操作，可作为AHB总线主机在USBHS和系统之间加速数据传输。

## 34.2. 主要特性

- 支持USB 2.0高速（480Mb/s）/全速（12Mb/s）/低速（1.5Mb/s）主机模式；

- 支持USB 2.0高速（480Mb/s）/全速（12Mb/s）设备模式；

- 支持遵循HNP（主机协商协议）和SRP（会话请求协议）的OTG协议；

- 支持所有的4种传输方式：控制传输、批量传输、中断传输和同步传输；

- 支持高带宽中断和同步传输；

- 在主机模式下，包含USB事务调度器，用于有效地处理USB事务请求；

- 包含一个4KB的FIFO RAM；

- 在主机模式下，支持12个通道；

- 在主机模式下，包含2个发送FIFO（周期性发送FIFO和非周期性发送FIFO）和1个接收FIFO（由所有的通道共享）；

- 在设备模式下，包含6个发送FIFO（每个IN端点一个发送FIFO）和1个接收FIFO（由所有的OUT端点共享）；

- 在主机模式下，若在高速模式下操作，支持PING协议；

- 在设备模式下，支持6个OUT端点和6个IN端点；

- 在设备模式下，支持远程唤醒功能；

- 包含一个支持USB协议的全速USB PHY；

- 包含一个内部DMA调度器和引擎，每个应用请求都可在USBHS和系统之间执行数据拷贝；

- 在主机模式下，SOF的时间间隔可动态调节；

- 可将SOF脉冲输出到PAD；

- 可检测ID引脚电平和VBUS电压；

- 在主机模式或者OTG A设备模式下，需要外部部件为连接的USB设备提供电源。

## 34.3. 结构框图


图 34-1. USBHS 结构框图


![image](images/12bab2a48c70.jpg)


## 34.4. 信号线描述


表 34-1. USBHS 信号线描述


<table><tr><td>I/O 端口</td><td>类型</td><td>描述</td><td>注意</td></tr><tr><td>VBUS</td><td>输入</td><td>总线电源端口</td><td>仅内部 PHY 使用</td></tr><tr><td>DM</td><td>输入/输出</td><td>差分信号线 - 端口</td><td>仅内部 PHY 使用</td></tr><tr><td>DP</td><td>输入/输出</td><td>差分信号线 + 端口</td><td>仅内部 PHY 使用</td></tr><tr><td>ID</td><td>输入</td><td>USB 识别:微连接器识别接口</td><td>仅内部 PHY 使用</td></tr><tr><td>ULPI_D[7:0]</td><td>输入/输出</td><td>ULPI 数据线</td><td>外部 ULPI PHY 使用</td></tr><tr><td>ULPI_NXT</td><td>输入</td><td>ULPI 下个信号线</td><td>外部 ULPI PHY 使用</td></tr><tr><td>ULPI_DIR</td><td>输入</td><td>ULPI 方向</td><td>外部 ULPI PHY 使用</td></tr><tr><td>ULPI_STP</td><td>输出</td><td>ULPI 停止</td><td>外部 ULPI PHY 使用</td></tr><tr><td>ULPI_CLK</td><td>输入</td><td>ULPI 时钟</td><td>外部 ULPI PHY 使用</td></tr></table>

## 34.5. 功能描述

## 34.5.1. USBHS PHY选择、时钟及工作模式

USBHS可以作为一个主机、一个设备或者一个DRD（双角色设备），并且支持两种连接类型：内部全速PHY和外部ULPI PHY。根据用户需求，应用可以选择两种连接类型的任何一种。

若使用内部PHY，USBHS支持的最大速度为全速；若使用外部高速ULPI PHY，USBHS支持的最大速度为高速。应用也可以在主机模式下使用USBHS_HCTL寄存器内的SPDFSLS控制位和在设备模式下使用USBHS_DCFG寄存器内的DS[1:0]控制位将外部ULPI PHY的最大速度限制至全速。具体配置如表34-2. USBHS支持速度列表所示。


表 34-2. USBHS 支持速度列表


<table><tr><td colspan="2">寄存器配置</td><td>主机支持速度</td><td>设备支持速度</td></tr><tr><td>EMBPHY=1(内部PHY)</td><td></td><td>全速低速</td><td>全速</td></tr><tr><td rowspan="2">EMBPHY=0(外部 ULPI PHY)</td><td>DS = 01 (设备模式)SPDFSLS = 1(主机模式)</td><td>全速低速</td><td>全速</td></tr><tr><td>DS = 00(设备模式)SPDFSLS = 0(主机模式)</td><td>高速全速低速</td><td>高速全速</td></tr></table>

应用可以使用USBHS_GUSBCS寄存器中的FHM和FDM控制位选择USBHS的工作模式：主机模式(FHM=1)或设备模式(FDM=1)。当这两个控制位被清除时，USBHS工作在OTG模式，即系统复位后的默认模式。

## 内部嵌入式全速PHY

USBHS包含一个内部嵌入式全速PHY，该内部嵌入式PHY支持主机模式下的全速和低速、设备模式下全速以及具备HNP和SRP的OTG协议。软件需要置位USBHS_GUSBCS寄存器中的EMBPHY控制位来使用该内部嵌入式全速PHY。如果内部全速PHY被选择，USBHS所使用的USB时钟需要配置为48MHz。该48MHz USB时钟从系统内部时钟产生，并且其时钟源和分频器需要在RCU模块中配置。

上拉或下拉电阻已经集成在内部全速PHY的内部，并且USBHS可根据当前模式（主机、设备或OTG模式）和连接状态进行自动选择。一个利用内部全速PHY的典型连接示意图如图34-2.在主机或设备模式下，利用内部PHY的连接示意图所示。


图 34-2. 在主机或设备模式下，利用内部 PHY 的连接示意图


![image](images/7b41a4cafb2e.jpg)



当USBHS工作在主机模式下时（FHM控制位置位、FDM控制位清除），VBUS为USB协议所定


义的5V电源检测引脚。内部PHY不能提供5V VBUS电源，仅在VBUS信号线上具有电压比较器和充电放电电路。所以，如果应用需要提供VBUS电源，那么则需要一个外部的供电电源IC。在主机模式下，USBHS和USB连接头之间的VBUS连接可以被忽略，这是由于USBHS并不检测VBUS引脚的电平状态，并假定5V供电电源一直存在。

当USBHS工作在设备模式下时（FHM控制位清除、FDM控制位置位），VBUS检测电路由USBHS_GCCFG寄存器中的VBUSIG控制位配置。因此，如果设备不需要检测VBUS引脚电压，可以置位VBUSIG控制位，并可释放VBUS引脚作为其他用途。否则，VBUS引脚的连接不能够被忽略，并且USBHS需要不断的检测VBUS电平状态，一旦VBUS电压降至所需有效值以下，需要立即关闭DP信号线上的上拉电阻，从而产生一个断开状态。

OTG模式连接示意图如图34-3. OTG模式下使用内部嵌入式PHY连接示意图所示。当USBHS工作在OTG模式下时，USBHS_GUSBCS寄存器内的FHM、FDM控制位应该被清除。在这种模式下，USBHS需要以下四个引脚：DM、DP、VBUS和ID，并且需要使用若干个电压比较器检测这些引脚的电压。USBHS也包含VBUS充电和放电电路，用以完成OTG协议中所描述的SRP请求。OTG A设备或B设备由ID引脚的电平状态所决定。在实现HNP协议的过程中，USBHS控制上拉和下拉电阻。


图 34-3. OTG 模式下使用内部嵌入式 PHY 连接示意图


![image](images/59c0616dd8b4.jpg)


## 外部ULPI PHY

USBHS为外部PHY提供了一个ULPI接口。如果需要使用USBHS模块完成高速USB应用，那么则需要一个外部高速ULPI PHY。结合外部ULPI PHY，USBHS支持高速主机和设备，也支持前文中内部嵌入式全速PHY所描述的所有模式。

软件需要清除USBHS_GUSBCS寄存器中的EMBPHY控制位以使能ULPI接口。当ULPI模式能使，USB时钟需要配置到60MHz，并且需要从ULPI_CLK引脚引入。软件可以在RCU模块中打开或关闭该60MHz ULPI时钟。


图 34-4. 使用外部 ULPI PHY 的连接示意图


![image](images/54f0f88da408.jpg)


## 34.5.2. USB 主机功能

## USB主机端口状态

主机应用可以通过USBHS_HPCS寄存器控制USB端口状态，如图34-5. 主机端口状态转移图所示。在系统初始化之后，USB端口保持掉电状态。通过软件置位PP控制位后，USB PHY（内部或外部）将被上电，并且USB端口变为断开状态。检测到连接后，USB端口变为连接状态。在USB总线上产生一个复位后，USB端口将变为使能状态。


图 34-5. 主机端口状态转移图


![image](images/fccc8419297b.jpg)


## 连接、复位和速度识别

作为USB主机，在检测到一个连接事件后，USBHS会为应用触发一个连接标志；同样，若检测到一个断开事件后，将会触发一个断开标志。

PRST控制位用于实现USB复位序列。应用可以置位该控制位以启动一个USB复位序列，或者清除该控制位以结束USB复位序列。仅当端口在连接或使能状态时，该控制位有效。

USBHS在对设备的连接和复位时执行速度检测，并且速度检测的结果会反馈在USBHS_HPCS寄存器的PS[1:0]位域中。

如果最大支持速度被配置为全速（SPDFSLS=1），USBHS仅仅在设备连接的过程中执行速度识别，并且从DM或DP的电平状态决定设备速度。就像USB协议中所描述的那样，全速设备上拉DP信号线，而低速设备上拉DM信号线。

如果最大支持速度被配置为高速（SPDFSLS=0），USBHS首先在连接的过程中执行速度检测，如果检测到全速设备连接，USBHS会在连接事件后的每个USB复位序列中，尝试执行高速检测（USB2.0协议中所描述的CHIRP序列）。所以，在主机上的应用应该在一个连接事件后提供一个USB复位，并且再次检查PS[1:0]标志位，以确定其连接的是否为高速设备。

## 挂起和复位

USBHS支持挂起和复位状态，当USBHS端口在使能状态时，向USBHS_HPCS寄存器的PSP控制位写1，USBHS会进入到挂起状态。在挂起状态，USBHS停止在USB总线上发送SOF，并且这样会让连接的USB设备在3ms后进入挂起状态。应用程序能够置位USBHS_HPCS寄存器中的PREM控制位以启动一个恢复序列，从而唤醒挂起的设备，当清除该控制位时，则可以停止恢复序列。如果主机在挂起状态下检测到一个远程唤醒信号，将会置位USBHS_GINTF寄存器的WKUPIF标志位，并且触发USBHS唤醒中断。

## SOF产生器

在主机模式下，USBHS向USB总线发送SOF令牌包。如USB 2.0协议所描述，全速连接下，SOF令牌包每1ms产生一次(由主机控制器或者HUB事务转换器产生)；高速连接下，SOF令牌包将在接下来的七个125 µs周期后产生。

每当USBHS进入到使能状态后，它将会按照USB2.0所定义的周期发送SOF令牌包。然而，应用程序可以通过写USBHS_HFT寄存器中的FRI[15:0]位来调整一帧或者一微帧的间隔。FRI位定义了在一帧或一微帧中的USB时钟周期个数，并且应用程序应该基于USBHS所使用的USB时钟频率计算该值。FRT[15:0]位显示当前帧或微帧剩余的时钟周期个数，并且在挂起状态时，该值将停止改变。

USBHS能够在每个SOF令牌包中产生一个脉冲信号，并且将其输出至一个引脚。该脉冲信号长度为16个HCLK周期。如果应用程序希望使用该功能，需要置位USBHS_GCCFG寄存器的SOFOEN控制位，并且配置相应的引脚寄存器为GPIO功能。

## USB通道和事务

USBHS在主机模式下包含12个独立的通道。每个通道能够与一个USB设备端点通信。通道的传输类型、方向、数据包长和其他信息都在通道相应的寄存器中配置，例如USBHS_HCHxCTL和USBHS_HCHxLEN寄存器。

USBHS支持所有的四种传输类型：控制、批量、中断和同步。USB 2.0协议将这些传输类型划分为两类：非周期性传输（控制和批量）和周期性传输（中断和同步）。基于此，为了有效地进行事务调度， 包含两种请求队列：周期性请求队列和非周期性请求队列。在上述请求队列中的请求条目可能代表一个 S 事务请求或者一个通道操作请求。

在无DMA模式下，如果应用想要在USB总线上启动一个OUT事务，应用需要通过AHB寄存器接口向数据FIFO中写入数据包。USBHS硬件会在应用写完整包数据后，自动产生一个事务请求并进入请求队列。在DMA模式下，应用仅需要配置通道属性和通道数据缓冲区地址，USBHS内部的DMA引擎会执行数据包拷贝和请求条目的产生工作。当应用使能IN通道时，USBHS自动产生IN请求条目。

请求队列中的请求条目通过事务控制模块按顺序处理。USBHS通常首先尝试处理周期性请求队列，然后处理非周期性请求队列。

帧起始后，USBHS首先开始处理周期性队列，直到队列为空或者当前周期性请求队列所需时间不够，然后处理非周期性队列。这种做法保证了一帧或微帧中周期性传输的带宽。每次USBHS从请求队列中读取并取出一个请求条目。如果取出的是通道禁用请求，这将直接禁用通道并准备处理下个条目。

如果当前请求是一个事务请求并且USB总线时间能够处理这个请求，USBHS会使用SIE在USB总线上产生该事务。

在当前帧内，当前请求所需的总线时间不足时，如果当前请求为周期性请求，USBHS停止处理该周期性请求队列，并启动处理非周期性请求。如果当前请求为非周期性请求，USBHS会停止处理任何队列，并等待直到当前帧结束。

## 34.5.3. USB设备功能

## USB设备连接

在设备模式下，USBHS在初始化后保持掉电状态。利用VBUS引脚上的5V电源连接USB主机后或者置位USBHS_GCCFG寄存器中VBUSIG控制位，USBHS将进入供电状态。USBHS首先打开DP信号线上的上拉电阻，之后主机方将会检测到一个连接事件。

## 复位和速度识别

USB主机在检测到设备连接之后，总是会启动一个USB复位序列，并且在设备模式下，检测到USB总线复位事件后，USBHS会为软件触发一个复位中断。

如果最大支持速度被配置为全速（USBHS_DCFG寄存器内DS[1:0] = 01），USBHS会以全速设备操作，然而如果最大支持速度被配置为高速（USBHS_DCFG寄存器内DS[1:0] = 00），在复位序列中，USBHS设备会尝试和主机启动一个速度识别（USB2.0协议中描述的一个CHIRP序列）。如果和主机的 序列握手成功，设备将会进入高速模式，否则，仍然停留在全速模式。

在复位序列和速度识别过程完成后，USBHS将会触发USBHS_GINTF寄存器中的ENUMF标志中断，并且利用 寄存器内的 标志位反映当前枚举设备速度。所以，如果软件想要实现一个高速设备，必须等待ENUMF中断，然后读取ES[1:0]控制位以获得速度识别结果。

如USB2.0协议所需要，USBHS在外设模式下不支持低速。

## 挂起和唤醒

USB总线保持IDLE状态并且数据线3ms无变化，USB设备将会进入挂起状态。当USB设备在挂起状态时，软件能够关闭大部分的时钟以节省电能。USB主机可以通过在USB总线上产生恢复信号，来唤醒挂起的设备。USBHS检测到恢复信号后，将置位USBHS_GINTF寄存器的

WKUPIF标志位并且触发USBHS唤醒中断。

在挂起设备模式，USBHS也能够远程唤醒USB总线。软件可以通过置位USBHS_DCTL寄存器的RWKUP控制位来发送一个远程唤醒信号，并且如果USB主机支持远程唤醒，主机会在USB总线上启动发送一个恢复信号。

## 软件断开

USBHS支持软件断开。设备进入到供电状态后，USBHS会打开DP信号线的上拉电阻，并且这样主机会检测到设备连接。然后，软件可以通过置位USBHS_DCTL寄存器中SD控制位进行强制断开。SD控制位置位后，如果当前设备速度为高速，USBHS会首先返回到全速设备，然后关闭DP信号线上的上拉电阻；如果当前设备速度为全速，USBHS将会直接关闭上拉电阻。这样，USB主机将会在USB总线上检测到设备断开。

## SOF跟踪

当USBHS在USB总线上接收到一个SOF令牌包时，将触发一个SOF标志/中断，并且开始利用本地USB时钟计算总线时间。当前帧的帧号将会反应在USBHS_DSTAT寄存器的FNRSOF[13:0]位域。当USB总线时间达到EOF1或EOF2点（帧结束，在USB 2.0协议中描述），USBHS会触发USBHS_GINTF寄存器中的EOPFIF标志/中断。软件能够使用这些标志位和寄存器以获得当前总线时间和位置信息。

## 34.5.4. OTG 功能概述

USBHS支持OTG协议1.3中所描述的OTG功能，OTG功能包括SRP和HNP。

## A设备和B设备

当标准A或微型A插头插入相应的插座时，具有OTG能力的USB设备为A设备。A设备向VBUS供电，并且在会话开始时默认为主机。当标准 、微型 、迷你 插头插入相应的插座或采用一端为标准A插头的不可分离电缆时，具有OTG能力的USB设备为B设备。B设备在会话开始时默认为外设。 使用 引脚电平状态决定 设备或 设备。 引脚状态反馈在USBHS_GOTGCS寄存器的IDPS状态位。为了了解A设备和B设备之间传输的详细状态，请参考OTG1.3协议。

## HNP

主机协商协议（ ）允许主机功能在两个直接连接的O G设备之间转换，并且用户不需要为了设备之间通信控制的改变而切换电缆线的连接。典型地，HNP协议是由B设备上的用户或应用启动，HNP只能通过设备上的微型AB插座执行。

一旦O G设备具有一个微型 插座，该O G设备可通过插入的插头类型决定默认为主机或设备（微型 插头插入为主机，微型 插头插入为设备）。通过使用主机协商协议（ ），一个默认为外设的OTG设备可以请求成为主机。主机角色切换的过程在下段中描述。此协议使用户不需要为了更改连接设备的角色而切换电缆线的连接。

当 S S工作在O G 主机模式时，并且其想放弃主机角色，可以首先置位 S S CS寄存器的PSP控制位来使USB总线进入挂起状态。然后B设备在3ms后进入挂起状态。如果B设备想要变为主机，软件需要置位USBHS_GOTGCS寄存器的HNPREQ控制位，然后USBHS会开始在总线上执行HNP协议，最后，HNP的结果会反馈在USBHS_GOTGCS寄存器的HNPS状态位。另外，软件总能从USBHS_GINTF寄存器的COPM状态位获取当前设备角色（主机或外设）。

## SRP

会话请求协议（SRP）允许B设备请求A设备打开VBUS并启动一个会话。该协议允许A设备（或许是电池供电）当总线无活动时通过关闭VBUS以节省电能，并为B设备启动总线活动提供了一种方法。如OTG协议中所描述，OTG设备必须和几个阈值比较VBUS电压，并且将比较结果反馈在USBHS_GOTGCS寄存器的ASV和BSV状态位中。

当USBHS工作在B设备OTG模式时，软件可以通过置位USBHS_GOTGCS寄存器的SRPREQ控制位来启动一个SRP请求，并且如果SRP请求成功，USBHS会在USBHS_GOTGCS寄存器中产生一个成功标志位SRPS。

当USBHS工作在OTG A设备模式且从B设备检测到一个SRP请求时，USBHS将会置位USBHS_GINTF寄存器中的SESIF标志位。软件获取该标志位后，需要准备为VBUS引脚打开5V供电电源。

## 34.5.5. 数据 FIFO

USBHS中采用4K字节数据FIFO存储包数据，数据FIFO是通过USBHS的内部SRAM实现的。

## 主机模式

主机模式下，数据 空间分为三个部分，分别是：用于接收数据包的 、用于非周期性发送数据包的非周期性Tx FIFO和用于周期性发送数据包的周期性Tx FIFO。所有的IN通道通过共享Rx FIFO接收数据。所有的周期性OUT通道通过共享周期性Tx FIFO来发送数据，所有的非周期性OUT通道通过共享非周期性Tx FIFO发送数据。通过寄存器USBHS_GRFLEN、USBHS_HNPTFLEN 和USBHS_HPTFLEN，软件可以配置以上数据FIFO的大小和起始偏移地址。图34-6. 主机模式FIFO空间所描述的是SRAM中各FIFO的结构，图中的数值是以32位为单位。


图 34-6. 主机模式 FIFO 空间


![image](images/58c7f9c8d1b5.jpg)


在DMA模式下，DMA负责系统存储区和数据FIFO之间的数据包传输。在非DMA模式下，程序将包数据写入数据FIFO或从数据FIFO读取包数据。USBHS为程序提供了专有寄存器空间来读写数据FIFO。图34-7. 主机模式FIFO访问寄存器映射表所描述的是数据FIFO所访问的寄存器存储空间，图中的数值是以字节为单位寻址。尽管所有的非周期通道共享相同的 以及所有的周期通道共享相同的FIFO，每个通道都拥有它们的FIFO访问寄存器空间。对USBHS而言，获 知 当 前 压 入 数 据 包 的 通 道 号 是 非 常 重 要 的 ， 通 过 寄 存 器USBHS_GRSTATR/USBHS_GRSTATP来访问数据包所从属的Rx FIFO。


图 34-7. 主机模式 FIFO 访问寄存器映射表


![image](images/0b16af65e6cf.jpg)


## 设备模式

在设备模式下，数据FIFO分为多个部分，其中包含1个Rx FIFO和6个Tx FIFO，每个Tx FIFO对应着一个IN端点，所有的OUT端点通过共享Rx FIFO接收数据包。通过寄存器USBHS_GRFLEN和USBHS_DIEPxTFLEN （x=0…5），程序可配置数据FIFO的大小和起始偏移地址。图34-8. 设备模式FIFO空间所描述的是SRAM中各FIFO的结构，图中的数值是以按照32位写的。


图 34-8. 设备模式 FIFO 空间


![image](images/4a9c1c771be3.jpg)


在 模式下， 负责系统存储区和数据 之间的数据包传输。在非 模式下，程序将包数据写入数据 或从数据 读取包数据。 为程序提供了专有寄存器空间来读写数据FIFO。图34-9. 设备模式FIFO访问寄存器映射表所描述的是数据FIFO所访问的寄存器存储空间，图中的数值是以字节为单位寻址。每个端点都拥有它们的FIFO访问寄存器空间。通过寄存器USBHS_GRSTATR/USBHS_GRSTATP来访问Rx FIFO。


图 34-9. 设备模式 FIFO 访问寄存器映射表


![image](images/769f61365186.jpg)


## 34.5.6. DMA 功能

该部分描述USBHS的DMA调度器和引擎。

## DMA请求和调度器

DMA功能通过置位寄存器USBHS_GAHBCS的位DMAEN获得使能。当一个IN/OUT通道或IN端点被适当地配置和使能，或Rx FIFO非空，USBHS将生成DMA请求。USBHS的DMA调度器负责应答这些DMA请求。

当同时存在多个请求时，DMA调度器负责仲裁这些请求。这些请求分为三类：Rx FIFO DMA请求、周期性传输DMA请求和非周期性传输DMA请求。在仲裁中，Rx FIFO DMA请求是最高优先级，周期性传输DMA请求是中级优先级，非周期性传输DMA请求是最低优先级。在处理周期性和非周期性传输DMA请求中，DMA调度器实行循环仲裁方法。

综上所述，DMA将自动处理Rx FIFO非空事件，所以，在DMA模式下，程序中可以忽略寄存器USBHS_GINTF的RXFNEIF标志位。

## DMA引擎

在主机或设备模式下，当Rx FIFO DMA请求获得仲裁后，DMA驱动器开始从Rx FIFO读取包数据或状态条目。对于包数据而言，DMA将数据写到特定的系统地址，该地址配置在寄存器USBHS_HCHxDMAADDR或USBHS_DIEPxDMAADDR/ USBHS_DIEPxDMAADDR。对于表目状态而言，在相关的通道或端点，DMA将生成特定的标志位或中断。

## 主机传输

当一个IN周期性或非周期性通道DMA请求获得仲裁后，DMA将IN请求条目写入周期性或非周期性请求队列。当一个预期的IN传输完成，或一个AHB/USB总线错误发生后，DMA停止特定的通道，生成寄存器USBHS_HCHxINTF的TF和CH标志位。如上文所述，在Rx FIFO DMA请求生成后，在IN传输的过程中所接受的包数据被复制到系统存储区。

当一个OUT周期性或非周期性通道DMA请求获得仲裁后，DMA从系统存储区读取包数据，或将包数据写到内部的Tx FIFO。当每次完成包数据复制后，DMA总是将OUT请求条目写入请求队列。当一个预期的OUT传输完成，或一个AHB/USB总线错误发生后，DMA停止特定的通道，生成寄存器USBHS_HCHxINTF的TF和CH标志位。

## 设备传输

在设备模式下，当一个IN端点DMA请求获得仲裁后，DMA从系统存储区读取包数据，或将包数据写到端点的Tx FIFO。当USBHS获取IN端点的IN令牌后，将发送DMA引擎所复制的包数据。

## 34.5.7. 操作手册

该部分描述的是USBHS的操作手册。

## 主机模式

## 全局寄存器初始化顺序：

1、根据应用的需求，如是否使能DMA、DMA的传输类型、Tx FIFO的空阈值等，设置寄存器USBHS_GAHBCS，此时，GINTEN位需要保持清零状态。

2、根据应用的需求，如操作模式（主机、设备或OTG）、某些OTG参数、ULPI和USB协议，设置寄存器USBHS_GUSBCS。

3、根据应用的需求，设置寄存器USBHS_GCCFG。

4、 根据应用的需求，设置寄存器USBHS_GRFLEN、USBHS_HNPTFLEN_DIEP0TFLEN、USBHS_HPTFLEN，配置数据FIFO。

5、 通过设置寄存器USBHS_GINTEN使能模式错误和主机端口中断，置位USBHS_GAHBCS寄存器的GINTEN位使能全局中断。

6、通过设置寄存器USBHS_HCTL的SPDFSLS位，判断是否将设备速度限制为全速。

7、 设置寄存器USBHS_HPCS，置位PP位。

8、等待设备连接，当设备连接后，触发寄存器USBHS_HPCS的PCD位，然后置位PRST位，执行一次端口复位，等待至少10毫秒后，清除PRST位。

9、等待USBHS_HPCS寄存器的PEDC中断，然后读取PE位以确认端口被成功地使能，读取PS位以获取连接的设备速度，之后，如果软件需要改变SOF间隔，设置USBHS_HFT寄存器。

## 通道初始化和使能顺序：

1、根据期望的传输类型、方向、包大小等信息，设置寄存器USBHS_HCHxCTL，在设置期间，要保证位CEN和CDIS保持清除。

2、 设置寄存器USBHS_HCHxINTEN，设置期望的中断使能位。

3、 在DMA使能的前提下，设置寄存器USBHS_HCHxDMAADDR。

、 设置寄存器 ， 表示一次传输中的包数， 表示一次传输中发送或接收的包数据的总字节数。

对于OUT通道，如果PCNT为1，单包的大小等于TLEN。如果PCNT大于1，前PCNT-1个包被认定为最大包长度的包，其大小是由寄存器USBHS_HCHxCTL的位MPL所定义。最后一包的大小可通过PCNT、TLEN和MPL计算得到。如果程序想要发出一个零长度的包，应该设定TLEN为0，PCNT位1。

对于IN通道，因为在IN事务结束之前，程序不知道实际接收的数据大小，程序可将TLEN设定为Rx FIFO所支持的最大值。

5、 置位寄存器USBHS_HCHxCTL中的CEN位以使能通道。

## 通道除能顺序：

程序可以通过同时置位CEN和CDIS除能通道。在寄存器操作后，USBHS将在请求队列中产生一个通道除能请求条目。当这个请求条目到达请求队列的顶部时，USBHS立即进行处理。

对于OUT通道而言，特定的通道将被立即除能。然后，会产生CH标志，USBHS将清除CEN和CDIS位。

对于IN通道而言，USBHS将通道除能状态条目压入Rx FIFO，然后，程序应该处理Rx FIFO非空事件：读和取出该状态条目，然后会产生CH标志，USBHS将清除CEN和CDIS位。

## IN传输操作顺序（DMA除能）：

1、 初始化USBHS全局寄存器。

2、初始化相应的通道。

3、使能相应的通道。

4、通过软件使能IN通道后，USBHS在相应请求队列中生成一个Rx请求条目。

5、当Rx请求条目到达请求队列的顶部时，USBHS开始执行该请求条目。对于由请求条目所指示的事务而言，如果总线时间足够，USBHS在USB总线上开始IN事务。

6、当IN事务结束时（收到ACK握手包），USBHS将接收到的数据包压入Rx FIFO，ACK标志位被触发，否则，状态标志（NAK）会指示事务结果。

7、如果步骤5所描述的IN事务完成后，步骤2的PCNT的数值比1大，程序将会返回步骤3，继续接收剩下的数据包。如果步骤5中描述的IN事务没有成功完成，程序将会返回步骤3来再次发送该数据包。

8、在所有的传输中的所有事务都被成功接收后，USBHS将TF状态条目压入Rx FIFO的最后的数据包的顶部，这样，软件在读取所有接收的包数据后，再读取TF状态条目。USBHS生成TF标志来指示传输成功结束。

9、除能通道，当通道处于空闲状态，即可为其他传输做准备。

## IN传输操作顺序（DMA使能）：

1、 初始化USBHS全局寄存器。

2、初始化并使能相应通道。

3、在通过软件使能IN通道后，USBHS在相应请求队列中生成一个Rx请求条目。

4、USBHS逐一处理IN请求队列中的请求条目，并将它们所指示的IN事务发到USB总线上。

5、当一个IN事务获得NAK握手包时，DMA可以自动地再发IN令牌直至USBHS获得预期的数据包的数目。

6、 在USBHS获取寄存器USBHS_HCHxLEN的位PCNT中期望数据包数目后，USBHS生成TF和CH标志来表示传输成功完成，相应通道除能。如果在这些事务期间发生USB总线错误或DMA取值错误，DMA将触发相关的错误标志，停止该通道的操作，最后除能该通道，触发

CH标志。

注意：在DMA模式下，因为DMA将自动处理Rx FIFO，程序不再使能或处理RXFNEIF中断。

## OUT传输操作顺序（DMA除能）：

1、 初始化USBHS全局寄存器。

2、初始化及使能相应通道。

3、将数据包写入通道的Tx FIFO（周期性Tx FIFO或非周期性Tx FIFO）。在所有的数据包都被写入FIFO后，USBHS在相应的请求队列中产生一个Tx请求条目，并且将USBHS_HCHxLEN中的TLEN值减少，减少的数值等于已写的包大小。

4、当请求条目到达请求队列的顶部时，USBHS开始执行该请求条目。如果请求条目对应的事务的总线时间足够，USBHS在USB总线上开展OUT事务。

5、 当由请求条目所指示的OUT事务结束时，寄存器USBHS_HCHxLEN的位PCNT减1。如果该事务完成（收到ACK握手包），ACK标志位被触发，否则，状态标志（NAK）会指示事务结果。

6、如果步骤5所描述的OUT事务完成后且步骤2的PCNT的数值比1大，程序将会返回步骤3，继续发送剩下的数据包。如果步骤5中描述的OUT事务没有成功完成，程序将会返回步骤3来再次发送该包。

7、在所有的传输中的所有事务都被成功送达后，USBHS生成TF标志来指示传输成功结束。

8、除能通道，当通道处于空闲状态，即可为其他传输做准备。

## OUT传输操作顺序（DMA使能）：

1、 初始化USBHS全局寄存器。

2、 初始化并使能相应通道。

3、 USBHS的DMA开始从寄存器USBHS_HCHxDMAADDR的位DMAADDR中所指示的地址取包数据，并且将数据写入相应通道的Tx FIFO（周期性Tx FIFO或非周期性Tx FIFO）。每当一个完整的包数据被写入FIFO中，USBHS在相应的请求队列中生成一个Tx请求条目，并减少寄存器USBHS_HCHxTLEN的位TLEN的数值，所减少的数值与所完成写操作的包大小相同。

4、 USBHS逐一处理请求队列中的请求条目，并将它们所指示的事务发到USB总线上。

5、 当一个事务获得NAK或PING握手包时，DMA可以再取或是再发数据包，在执行PING协议时也会自动像这样执行。

6、 如果所有的事务都被成功发送到USB总线上，USBHS生成TF和CH标志来表示传输成功完成，相应通道除能。如果在这些事务期间发生USB总线错误或DMA取值错误，DMA将触发相关的错误标志，停止该通道的操作，最后除能该通道，触发CH标志。

注意：在DMA模式下，因为DMA将自动处理Rx FIFO，程序不再使能或处理RXFNEIF中断。

## 设备模式

## 全局寄存器初始化顺序：

1、 根据应用的需求，如是否使能DMA、DMA的传输类型、Tx FIFO的空阈值等，设置寄存器USBHS_GAHBCS，此时，GINTEN位需要保持清零状态。

2、根据应用的需求，如操作模式（主机、设备或OTG）、某些OTG参数、ULPI和USB协议，设置寄存器USBHS_GUSBCS。

3、根据应用的需求，设置寄存器USBHS_GCCFG。

4、 根据应用的需求，设置寄存器USBHS_GRFLEN、USBHS_HNPTFLEN_DIEP0TFLEN、USBHS_DIEPxTFLEN，配置数据FIFO。

5、通过设置寄存器USBHS_GINTEN使能模式错误、挂起、SOF、枚举完成和USB复位中断，置位USBHS_GAHBCS寄存器的GINTEN位使能全局中断。

6、根据应用的需求，如设备的地址和设备的速度等，设置寄存器USBHS_DCFG。

7、在设备连接上主机上后，主机在USB总线上执行端口复位，触发寄存器USBHS_GINTF的RST中断。

8、 等 待 寄 存 器 USBHS_GINTF 的 ENUMF 中 断 ， 在 中 断 处 理 中 读 取 寄 存 器USBHS_DIEPxTFLEN的位域ES[1:0]获取当前枚举的设备速度。

## 端点初始化和使能顺序：

1、 根 据 预 期 的 传 输 类 型 、 包 大 小 等 信 息 ， 设 置 寄 存 器 USBHS_DIEPxCTL 或USBHS_DOEPxCTL。

2、 设定寄存器 USBHS_DIEPINTEN 或 USBHS_DOEPINTEN，置位相应中断使能位。

3、 如果DMA使能，设定寄存器USBHS_DIEPxDMAADDR或USBHS_DOEPxDMAADDR。

4、 设定寄存器 USBHS_DIEPxLEN 或 USBHS_DOEPxLEN，PCNT 表示一次传输中的包数，TLEN 表示一次传输中发送或接收的包数据的总字节数。

对于IN端点，如果PCNT等于1，单数据包的大小等于TLEN。如果PCNT大于1，前PCNT-1个包被认定为最大包长度的包，其大小是由寄存器USBHS_DIEPxCTL的位MPL所定义。最后一包的大小可通过PCNT、TLEN和MPL计算得到。如果程序想要发出一个零长度的包，应该设定TLEN为0，PCNT位1。

对于OUT端点，因为在IN事务结束之前，程序不知道实际接收的数据大小，程序可将TLEN设定为Rx FIFO所支持的最大值。

5、 置位 USBHS_DIEPxCTL 或 USBHS_DOEPxCTL 寄存器 EPEN 位使能端点。

## 端点除能顺序：

当USBHS_DIEPxCTL或USBHS_DOEPxCTL寄存器的EPEN位被清除时，程序可以在任何时候除能端点。

## IN传输操作顺序（DMA除能）：

1、 初始化USBHS全局寄存器。

2、初始化和使能IN端点。

3、 将数据包写入端点的Tx FIFO，每当数据包写入FIFO，USBHS减少USBHS_DIEPxLEN寄存器的 域的数值，其减少的数值等于已写的数据包大小。

4、 当IN令牌接收后，USBHS发送数据包，在USB总线上的事务完成后，USBHS_DIEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果。

、在一次传输的所有数据包都被成功发送， 生成一个 标志位以表明传输成功结束，除能相应IN端点。

## IN传输操作顺序（DMA使能）：

1、 初始化USBHS全局寄存器。

2、初始化并使能相应IN端点。

3、 USBHS 的 DMA 开始从寄存器 USBHS_DIEPxDMAADDR 的位 DMAADDR 中所指示的地址取包数据，并且将数据写入相应通道的 Tx FIFO。每当一个完整的包数据被写入 FIFO中，USBHS 将减少寄存器 USBHS_DIEPxLEN 的位域 TLEN 的数值，所减少的数值与所完成写操作的包大小相同。

4、 当IN令牌接收后，USBHS发送数据包，在USB总线上的事务完成后，USBHS_DIEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果。

5、在一次传输的所有数据包都被成功发送，USBHS生成一个TF和EPDIS标志位表明传输成功结束，除能相应IN端点。如果在事务期间出现USB总线错误或DMA取值错误，DMA将触发相关错误标志。

注意：在DMA模式下，因为DMA将自动处理Rx FIFO，程序不再使能或处理RXFNEIF中断。

## OUT传输操作顺序（DMA除能）：

1、 初始化USBHS全局寄存器。

2、初始化和使能OUT端点。

3、当OUT令牌接收后，USBHS接收包数据或基于Rx FIFO状态和寄存器配置回复NAK握手包。如果事务成功完成（USBHS接收并保存数据到Rx FIFO，发送ACK握手包），USBHS_DOEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果。

4、在一次传输的所有数据包都被成功接收，USBHS将TF状态条目压入Rx FIFO的最后的数据包的顶部，这样，软件在读取所有接收的包数据后，再读取TF状态条目。USBHS生成TF标志来指示传输成功结束。USBHS生成一个TF标志位表明传输成功结束，除能相应OUT端点。

## OUT传输操作顺序（DMA使能）：

1、 初始化USBHS全局寄存器。

2、初始化并使能相应OUT端点。

3、当OUT令牌接收后，USBHS接收包数据或基于Rx FIFO状态和寄存器配置回复NAK握手包。如果事务成功完成（USBHS接收并保存数据到Rx FIFO，发送ACK握手包），USBHS_DOEPxLEN寄存器的PCNT值减1。如果事务成功完成（接收到ACK握手包），ACK标志被触发，或者，其他状态标志表示事务的结果。

4、在一次传输的所有数据包都被成功发送，USBHS生成一个TF和EPDIS标志位表明传输成功结束，除能相应端点。如果在事务期间出现USB总线错误或DMA取值错误，DMA将触发相关错误标志。

注意：在DMA模式下，因为DMA将自动处理Rx FIFO，程序不再使能或处理RXFNEIF中断。

## 34.6. 中断

USBHS有四种中断：全局中断、唤醒中断、端点 1 IN 中断和端点 1 OUT 中断。

全局中断是软件需要处理的主要中断，全局中断的标志位可在 USBHS_GINTF 寄存器读取，列举在表34-3. USBHS 全局中断。


表 34-3. USBHS 全局中断


<table><tr><td>中断标志</td><td>描述</td><td>运行模式</td></tr><tr><td>SESIF</td><td>会话中断</td><td>主机或设备模式</td></tr><tr><td>DISCIF</td><td>断开连接中断标志</td><td>主机模式</td></tr><tr><td>IDPSC</td><td>ID 引脚状态变化</td><td>主机或设备模式</td></tr><tr><td>PTXFEIF</td><td>周期性 Tx FIFO 空中断标志</td><td>主机模式</td></tr><tr><td>HCIF</td><td>主机通道中断标志</td><td>主机模式</td></tr><tr><td>HPIF</td><td>主机端口中断</td><td>主机模式</td></tr><tr><td>PXNCIF / ISOONCIF</td><td>周期性传输未完成中断标志 /同步OUT传输未完成中断标志</td><td>主机或设备模式</td></tr><tr><td>ISOINCIF</td><td>同步 IN 传输未完成中断标志</td><td>设备模式</td></tr><tr><td>OEPIF</td><td>OUT 端点中断标志</td><td>设备模式</td></tr><tr><td>IEPIF</td><td>IN 端点中断标志</td><td>设备模式</td></tr><tr><td>EOPFIF</td><td>周期性帧尾中断标志</td><td>设备模式</td></tr><tr><td>ISOOPDIF</td><td>同步 OUT 丢包中断标志</td><td>设备模式</td></tr><tr><td>ENUMF</td><td>枚举完成</td><td>设备模式</td></tr><tr><td>RST</td><td>USB 复位</td><td>设备模式</td></tr><tr><td>SP</td><td>USB挂起</td><td>设备模式</td></tr><tr><td>ESP</td><td>早挂起</td><td>设备模式</td></tr><tr><td>GONAK</td><td>全局OUT NAK有效</td><td>设备模式</td></tr><tr><td>GNPINAK</td><td>全局非周期IN NAK有效</td><td>设备模式</td></tr><tr><td>NPTXFEIF</td><td>非周期Tx FIFO空中断标志</td><td>主机模式</td></tr><tr><td>RXFNEIF</td><td>Rx FIFO非空中断标志</td><td>主机或设备模式</td></tr><tr><td>SOF</td><td>帧首</td><td>主机或设备模式</td></tr><tr><td>OTGIF</td><td>OTG 中断标志</td><td>主机或设备模式</td></tr><tr><td>MFIF</td><td>模式错误中断标志</td><td>主机或设备模式</td></tr></table>

唤醒中断可以在 USBHS 处于挂起状态时触发，即使 USBHS 的时钟停止。寄存器USBHS_GINTF 的位 WKUPIF 是唤醒源。

端点 1 IN/OUT 中断是适用于端点 1 的两个特殊中断，程序可通过这两个中断快速回应端点 1的事件。这两个是中断通过寄存器 USBHS_DEP1INT 各自使能，这两个中断源来自于寄存器USBHS_DIEP1INTF 和 USBHS_DOEP1INTF ， 其 中 断 使 能 位 定 义 在 寄 存 器USBHS_DIEP1INTEN 和 USBHS_DOEP1INTEN。
