## 23. 串行外设接口/片上音频接口（SPI/I2S）

## 23.1. 简介

SPI/I2S模块可以通过SPI协议或I2S音频协议与外部设备进行通信。

串行外设接口（Serial Peripheral Interface，缩写为SPI）提供了基于SPI协议的数据发送和接收功能，可以工作于主机或从机模式。SPI接口支持具有硬件CRC计算和校验的全双工和单工模式。只有SPI0支持SPI四线主机模式。

片上音频接口（Inter-IC Sound，缩写为I2S）支持四种音频标准，分别是I2S飞利浦标准，MSB对齐标准，LSB对齐标准和PCM标准。它可以在四种模式下运行，包括主机发送模式，主机接收模式，从机发送模式和从机接收模式。

## 23.2. 主要特性

## 23.2.1. SPI 主要特性

◼ 具有全双工和单工模式的主从操作。

◼ 16位宽度，独立的发送和接收缓冲区（只有SPI1）。

◼ 32位宽度，独立的发送和接收FIFO（只有SPI0）。

◼ 8位或16位数据帧格式（只有SPI1）。

◼ 4位到16位的数据帧格式（只有SPI0）。

◼ 低位在前或高位在前的数据位顺序。

◼ 软件和硬件NSS管理。

◼ 硬件CRC计算、发送和校验。

◼ 发送和接收支持DMA模式。

◼ 支持SPI TI模式。

◼ 支持SPI NSS脉冲模式。

◼ 支持SPI四线功能的主机模式（只有SPI0）。

## 23.2.2. I2S 主要特性

◼ 具有发送和接收功能的主从操作。

◼ 支持四种I2S音频标准：飞利浦标准，MSB对齐标准，LSB对齐标准和PCM标准。

◼ 数据长度可以为16位，24位和32位。

◼ 通道长度为16位或32位。

◼ 16位缓冲区用于发送和接收。

◼ 通过I2S时钟分频器，可以得到8 kHz到192 kHz的音频采样频率。

◼ 可编程空闲状态时钟极性。

◼ 可以输出主时钟（MCK）。

◼ 发送和接收支持DMA功能。

## 23.3. SPI 功能说明

## 23.3.1. SPI 结构框图


图 23-1. SPI 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/01edc44507f8001dc797b33b90487bfeb4cfd05375efef1f63ebfa6534fe9df6.jpg)


## 23.3.2. SPI 信号线描述

常规配置（非 SPI四线模式）


表 23-1. SPI 信号描述


<table><tr><td>引脚名称</td><td>方向</td><td>描述</td></tr><tr><td>SCK</td><td>I/O</td><td>主机:SPI时钟输出从机:SPI时钟输入</td></tr><tr><td>MISO</td><td>I/O</td><td>主机:数据接收线从机:数据发送线主机双向线模式:不使用从机双向线模式:数据发送和接收线</td></tr><tr><td>MOSI</td><td>I/O</td><td>主机:数据发送线从机:数据接收线主机双向线模式:数据发送和接收线从机双向线模式:不使用</td></tr><tr><td>NSS</td><td>I/O</td><td>软件NSS模式:不使用主机硬件NSS模式:NSSDRV=1时,为NSS输出,适用于单主机模式;NSSDRV=0时,为NSS输入,适用于多主机模式。从机硬件NSS模式:为NSS输入,作为从机的片选信号。</td></tr></table>

## SPI 四线配置

SPI默认配置为单线模式，当SPI_QCTL中的QMOD位置1时，配置为SPI四线模式（只适用于

SPI0）。SPI四线模式只能工作在主机模式。

在SPI四线模式下，SPI通过以下6个引脚与外部设备连接：


表 23-2. SPI 四线信号描述


<table><tr><td>引脚名称</td><td>方向</td><td>描述</td></tr><tr><td>SCK</td><td>O</td><td>SPI 时钟输出</td></tr><tr><td>MOSI</td><td>I/O</td><td>发送或接收数据 0</td></tr><tr><td>MISO</td><td>I/O</td><td>发送或接收数据 1</td></tr><tr><td>IO2</td><td>I/O</td><td>发送或接收数据 2</td></tr><tr><td>IO3</td><td>I/O</td><td>发送或接收数据 3</td></tr><tr><td>NSS</td><td>O</td><td>NSS 输出</td></tr></table>

## 23.3.3. SPI 时序和数据帧格式

SPI_CTL0寄存器中的CKPL位和CKPH位决定了SPI时钟和数据信号的时序。CKPL位决定了空闲状态时SCK的电平，CKPH位决定了第一个或第二个时钟跳变沿为有效采样边沿。在TI模式下，这两位没有意义。

在SPI0常规模式中，通过SPI_CTL1中的DZ[3:0]位域配置数据长度，可以设置为4位至16位。该设置不仅适用于数据的发送也适用于数据的接收。不论设置的数据长度是多少，对FIFO的读访问必须与SPI_CTL1寄存器中的BYTEN位设置的对齐。在SPI四线模式下，数据长度固定为8位。

同样，通过设置SPI_CTL0中的LF位可以配置数据顺序，当LF=1时，SPI先发送LSB位，当LF=0时，则先发送MSB位。在TI模式中，数据顺序固定为先发MSB位。

当访问SPI_DATA寄存器时，数据帧总是右对齐成一个字节（如果数据长度小于或等于一个字节）或一个半字。通讯时，只有数据长度内的位会随时钟输出。


图 23-2. SPI0 常规模式下的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/fca56868fded20fb2f50606d5cf57dd0c8eb0394a5790221e85cd3d3c04de924.jpg)



图 23-3. SPI0 数据帧右对齐示意图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/862aafce5f1aecfc60c7b39ae49ba51a3bdc88ed1bb4c3d53dc92d9ef9370102.jpg)


在SPI1常规模式中，通过SPI_CTL0中的FF16位配置数据长度，当FF16=1时，数据长度为16位，否则为8位。

通过设置SPI_CTL0中的LF位可以配置数据顺序，当LF=1时，SPI1先发送LSB位，当LF=0时，则先发送MSB位。在TI模式中，数据顺序固定为先发MSB位。


图 23-4. SPI1 常规模式下的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/a697e74e6f0fd9526618cbb90152da7e3e73e45d5810bbdeaedb9c560827e0ff.jpg)



图 23-5. SPI0 四线模式下的 SPI 时序图（CKPL=1, CKPH=1, LF=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/a568fad28965498227058ed116391e3bbb63410a5baadb2a2a9355085e888813.jpg)


## 23.3.4. 独立发送和接收缓冲区

独立的32位的接收缓冲区（RXFIFO）和发送缓冲区（TXFIFO）分别用于SPI数据传输的不同方向，它们使得SPI可以连续工作（只适用于SPI0）。


图 23-6. 发送/接收缓冲区


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/d220b304378e29f02c82ff97654a48544876d659f723755be21699833b81bd59.jpg)


当当前TXFIFO的存储量小于或等于整体存储能力的一半时，TXFIFO被视为空<sup>（</sup>1<sup>）</sup>并且此时TBE被硬件置1。当TBE位置位时，向SPI_DATA寄存器写数据，会把数据存入发送FIFO的末尾。当当RXFIFO被视为非空<sup>（</sup>2<sup>）</sup>时硬件将RBNE位置1。当RBNE位置位时，从SPI_DATA寄存器读数据，将从接收FIFO获得最早数据。

注意：

（1）对于SPI0，TXFIFO空意味着TXFIFO当前的存储量小于或等于TXFIFO整体存储能力的一半。TXFIFO满的意义与之相反。所以，当数据长度不大于8位时，TXFIFO最多能存储3个数据帧。如果下文出现TXFIFO空或者满，如无特殊说明，意义与这里说明的相同。

（2）对于SPI0，RXFIFO空的意义分为以下两种情况：如果SPI_CTL1中BYTEN位为1时，RXFIFO空意味着当前RXFIFO的存储量小于RXFIFO整体存储能力的四分之一。此时，当数据长度不大于8位时，RXFIFO最多可以存储4个数据帧。如果SPI_CTL1中BYTEN位为0时，RXFIFO空意味着当前RXFIFO的存储量小于RXFIFO整体存储能力的一半。RXFIFO满的意义与之相反。如果下文出现RXFIFO空或者满，如无特殊说明，意义与这里说明的相同。

## 数据合并（仅适用于 SPI0）

在SPI_CTL1寄存器中DZ[3:0]配置传输数据位宽为8位或者小于8位的情况下，通过配置SPI_CTL1寄存器中BYTEN位为0，开启数据合并传输模式功能。在配置SPI_CTL1寄存器中DZ[3:0]配置传输数据位宽为小于等于8位时，该功能可以实现当对SPI_DATA寄存器进行16位写访问时，两个数据帧的发送是并行方式而不是串行方式。同样的，在接收端接收器通过对SPI_DATA的一次16位读访问，获取这两个数据帧，并且这两帧数据在接收时，仅会产生一个RBNE事件。

注意：当被传输的数据为奇数个字节时，在发送端，需要用8位访问SPI_DATA，发出最后一个数据帧。在接收端，为了产生最后一个字节的RBNE事件，接收器必须在接收最后一个数据帧时，改变BYTEN位。

## 23.3.5. NSS 功能

## 从机模式

当配置为从机模式（MSTMOD=0）时，在硬件NSS模式（SWNSSEN = 0）下，SPI从NSS引脚获取NSS电平，在软件NSS（SWNSSEN = 1）下，SPI根据SWNSS位得到NSS电平。只有当NSS为低电平时，发送或接收数据。在软件NSS模式下，不使用NSS引脚。


表 23-3. 从机模式 NSS 功能


<table><tr><td>模式</td><td>寄存器配置</td><td>描述</td></tr><tr><td>从机硬件 NSS 模式</td><td>MSTMOD = 0SWNSSEN = 0</td><td>SPI 从机 NSS 电平从 NSS 引脚获取。</td></tr><tr><td>从机软件 NSS 模式</td><td>MSTMOD = 0SWNSSEN = 1</td><td>SPI 从机 NSS 电平由 SWNSS 位决定。SWNSS = 0: NSS 电平为低SWNSS = 1: NSS 电平为高</td></tr></table>

## 主机模式

在主机模式（MSTMOD=1）下，如果应用程序使用多主机连接方式，NSS可以配置为硬件输入模式（SWNSSEN=0，NSSDRV=0）或者软件模式（SWNSSEN=1）。一旦NSS引脚（在硬件NSS模式下）或SWNSS位（在软件NSS模式下）被拉低，SPI将自动进入从机模式，并且产生主机配置错误，CONFERR位置1。

如 果应 用 程 序 希 望 使 用NSS引 脚控 制SPI从设备，NSS应 该配 置 为 硬 件 输 出 模 式（SWNSSEN=0，NSSDRV=1）。使能SPI之后，NSS变为低电平。

应用程序可以使用一个通用I/O口作为NSS引脚，以实现更加灵活的NSS应用。


表 23-4. 主机模式 NSS 功能


<table><tr><td>模式</td><td>寄存器配置</td><td>描述</td></tr><tr><td>主机硬件 NSS 输出模式</td><td>MSTMOD = 1SWNSSEN = 0NSSDRV=1</td><td>适用于单主机模式,主机使用 NSS 引脚控制 SPI 从设备,此时 NSS 配置为硬件输出模式。使能 SPI 后 NSS 为低电平。</td></tr><tr><td>主机硬件 NSS 输入模式</td><td>MSTMOD = 1SWNSSEN = 0NSSDRV=0</td><td>适用于多主机模式,此时 NSS 配置为硬件输入模式,一旦 NSS 引脚被拉低,SPI 将自动进入从机模式,并且产生主机配置错误,CONFERR 位置 1。</td></tr><tr><td rowspan="2">主机软件 NSS 模式</td><td>MSTMOD = 1SWNSSEN = 1SWNSS = 0NSSDRV:不要求</td><td>适用于多主机模式,一旦 SWNSS = 0,SPI 将自动进入从机模式,并且产生主机配置错误,CONFERR 位置 1。</td></tr><tr><td>MSTMOD = 1SWNSSEN = 1SWNSS = 1NSSDRV:不要求</td><td>从机可以使用硬件或软件 NSS 模式</td></tr></table>

## 23.3.6. SPI 运行模式


表 23-5. SPI 运行模式


<table><tr><td>模式</td><td>描述</td><td>寄存器配置</td><td>数据引脚用法</td></tr><tr><td>MFD</td><td>全双工主机模式</td><td>MSTMOD = 1RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 发送MISO: 接收</td></tr><tr><td>MTU</td><td>单向线连接主机发送模式</td><td>MSTMOD = 1RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 发送MISO: 不使用</td></tr><tr><td>MRU</td><td>单向线连接主机接收模式</td><td>MSTMOD = 1RO = 1BDEN = 0BDOEN: 不要求</td><td>MOSI: 不使用MISO: 接收</td></tr><tr><td>MTB</td><td>双向线连接主机发送模式</td><td>MSTMOD = 1RO = 0BDEN = 1BDOEN = 1</td><td>MOSI: 发送MISO: 不使用</td></tr><tr><td>MRB</td><td>双向线连接主机接收模式</td><td>MSTMOD = 1RO = 0BDEN = 1BDOEN = 0</td><td>MOSI: 接收MISO: 不使用</td></tr><tr><td>SFD</td><td>全双工从机模式</td><td>MSTMOD = 0RO = 0BDEN = 0BDOEN:不要求</td><td>MOSI: 接收MISO:发送</td></tr><tr><td>STU</td><td>单向线连接从机发送模式</td><td>MSTMOD = 0RO = 0BDEN = 0BDOEN:不要求</td><td>MOSI:不使用MISO:发送</td></tr><tr><td>SRU</td><td>单向线连接从机接收模式</td><td>MSTMOD = 0RO = 1BDEN = 0BDOEN:不要求</td><td>MOSI:接收MISO:不使用</td></tr><tr><td>STB</td><td>双向线连接从机发送模式</td><td>MSTMOD = 0RO = 0BDEN = 1BDOEN = 1</td><td>MOSI:不使用MISO:发送</td></tr><tr><td>SRB</td><td>双向线连接从机接收模式</td><td>MSTMOD = 0RO = 0BDEN = 1BDOEN = 0</td><td>MOSI:不使用MISO:接收</td></tr></table>


图 23-7. 典型的全双工模式连接


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/1e70b01bd40606b233e0396b1246c57a3d48be5ca4e9e124f18a78225647a6f6.jpg)



图 23-8. 典型的单工模式连接（主机：接收，从机：发送）


<table><tr><td>主机MRU</td><td>从机STU</td></tr><tr><td>SCK</td><td>SCK</td></tr><tr><td>MISO</td><td>MISO</td></tr><tr><td>MOSI</td><td>MOSI</td></tr><tr><td>NSS</td><td>NSS</td></tr></table>


图 23-9. 典型的单工模式连接（主机：只发送，从机：接收）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/304ff0fc778f6d4fcbf284f755b5c827e9eb73e563bff99baa677fc3efd761c2.jpg)



图 23-10. 典型的双向线连接


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/74c7fb2a14bd090bce6b52198ce611d25f465fec1684b66b76e386d3819f35d6.jpg)


## SPI 初始化流程

## SPI0：

1. 如果工作在主机模式或从机TI模式，配置SPI_CTL0中的PSC[2:0]位来生成预期波特率的SCK信号，或配置TI模式下的Td时间。否则，忽略此步骤。

2. 配置时钟时序（SPI_CTL0中的CKPL位和CKPH位）。

3. 配置帧格式（SPI_CTL0中的LF位）。

4. 配置数据格式（SPI_CTL1中的DZ[3:0]位域）和SPI_DATA的访问方式（SPI_CTL1中的BYTEN）。

5. 按照上文NSS 的描述，根据应用程序的需求，配置NSS模式（SPI_CTL0中的SWNSSEN位和NSSDRV位）。

6. 如果工作在TI模式，需要将SPI_CTL1中的TMOD位置1，否则，忽略此步骤。

7. 如果工作在 NSSP 模式，需要将 SPI_CTL1 中的 NSSP位置 1，否则，忽略此步骤。

8. 根据 23-5. SPI ，配置MSTMOD位、RO位、BDEN位和BDOEN位。

9. 根据应用程序的需求，配置TXDMA_ODD和RXDMA_ODD位。

10. 如果工作在SPI四线模式，需要将SPI_QCTL中的QMOD位置1，如果不是，则忽略此步骤。

11. 使能SPI（将SPIEN位置1）。

注意：在通信过程中，不应更改CKPH、CKPL、MSTMOD、PSC[2:0]、LF、DZ[3:0]位。

## SPI1：

在发送或接收数据之前，应用程序应遵循如下的SPI初始化流程：

1. 如果工作在主机模式或从机TI模式，配置SPI_CTL0中的PSC[2:0]位来生成预期波特率的

SCK信号，或配置TI模式下的Td时间。否则，忽略此步骤。

2. 配置数据格式（SPI_CTL0中的FF16位）。

3. 配置时钟时序（SPI_CTL0中的CKPL位和CKPH位）。

4. 配置帧格式（SPI_CTL0中的LF位）。

5. 按照上文NSS 的描述，根据应用程序的需求，配置NSS模式（SPI_CTL0中的SWNSSEN位和NSSDRV位）。

6. 如果工作在TI模式，需要将SPI_CTL1中的TMOD位置1，否则，忽略此步骤。

7. 如果工作在NSSP模式，需要将SPI_CTL1中的NSSP位置1，否则，忽略此步骤。

8. 根据 23-5. SPI ，配置MSTMOD位、RO位、BDEN位和BDOEN位。

9. 使能SPI（将SPIEN位置1）。

注意：在通信过程中，不应更改CKPH、CKPL、MSTMOD、PSC[2:0]、LF位。

## SPI 基本发送和接收流程

## 发送流程

在完成初始化过程之后，SPI模块使能并保持在空闲状态。在主机模式下，当软件写一个数据到发送缓冲区/发送FIFO时，发送过程开始。在从机模式下，当SCK引脚上的SCK信号开始翻转，且NSS引脚电平为低，发送过程开始。所以，在从机模式下，应用程序必须确保在数据发送开始前，数据已经写入发送缓冲区/发送FIFO中。

当SPI开始发送一个数据帧时，首先将这个数据帧从数据缓冲区/发送FIFO加载到移位寄存器中，然后开始发送加载的数据。在数据帧的第一位发送之后，TBE（发送缓冲区/发送FIFO空）位置1。TBE标志位置1，说明发送缓冲区/发送FIFO为空，此时如果需要发送更多数据，软件应该继续写SPI_DATA寄存器。

在主机模式下，若想要实现连续发送功能，那么在当前数据帧发送完成前，软件应该将下一个数据写入SPI_DATA寄存器中。

## 接收流程

在最后一个采样时钟边沿之后，接收到的数据将从移位寄存器存入到接收缓冲区/接收FIFO，且RBNE（接收缓冲区/接收FIFO非空）位置1。软件通过读SPI_DATA寄存器获得接收的数据，此操作会自动清除RBNE标志位。在MRU和MRB模式中，为了接收下一个数据帧，硬件需要连续发送时钟信号，而在全双工主机模式（ ）中，仅当发送缓冲区 发送 非空时，硬件才接收下一个数据帧。

## SPI 不同模式下的操作流程（非 SPI四线模式，TI 模式或 NSSP模式）

在全双工模式下，无论是MFD模式或者SFD模式，应用程序都应该监视RBNE标志位和TBE标志位，并且遵循上文描述的操作流程。

发送模式（MTU，MTB，STU或STB）与全双工模式中的发送流程类似，不同的是需要忽略RBNE位和RXORERR位。

相比于发送模式的情况，主机接收模式（MRU或MRB）与全双工的接收流程大不相同。在MRU模式或MRB模式下，在SPI使能后，SPI产生连续的SCK信号，直到SPI停止。所以，软件应该忽略TBE标志位，并且在RBNE位置1后，读出接收缓冲区/接收FIFO内的数据，否则，将会产

生接收过载错误。

除了忽略TBE标志位，且只执行上述的接收流程之外，从机接收模式（SRU或SRB）与全双工模式类似。

## SPI TI 模式

SPI TI模式将NSS作为一种特殊的帧头标志信号，它的操作流程与上文描述的常规模式类似。上文描述的模式（MFD，MTU，MRU，MTB，MRB，SFD，STU，SRU，STB和SRB）都支持TI模式。但是，在TI模式中，SPI_CTL0中的CKPL位和CKPH位是没有意义的，SCK信号的采样边沿为下降沿。


图 23-11. 主机 TI 模式在不连续发送时的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/d4b684fd11b67bb2b645810d8f2536d9226974a9d342b1c90918224d2c853a46.jpg)



图 23-12. 主机 TI 模式在连续发送时的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/da3f4a2b7730cc7a1b9e10568c9cd7175a1f13185f8f77b8440f1989e409f036.jpg)


在主机TI模式下，SPI模块可实现连续传输或者不连续传输。如果主机写SPI_DATA的速度很快，那么就是连续传输，否则，为不连续传输。在不连续传输中，在每个字节传输前需要一个额外的时钟周期。在连续传输中，额外的时钟周期只存在于第一个字节之前，随后字节的起始时钟周期被前一个字节的最后一位的时钟周期覆盖。


图 23-13. 从机 TI 模式时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/b4adcb1599202f65a1a57a37c91ce264b5956b56617f96e6c6f3a71a76cac6aa.jpg)


在从机TI模式中，在SCK信号的最后一个上升沿，从机开始发送最后一个字节的LSB位，在半位的时间之后，主机开始采集数据。为了确保主机采集到正确的数据，在释放该引脚之前，从机需要在SCK信号的下降沿之后继续驱动该位一段时间，这段时间称为 $\mathsf { T _ { d } }$ ， $\mathsf { T _ { d } }$ 通过SPI_CTL0寄存器中的PSC[2:0]位来设置。

$$
T _ {d} = \frac {T _ {\text { bit }}}{2} + 5 ^ {*} T _ {\text { pclk }}\tag{23-1}
$$

例如，如果 ${ \mathsf { P S C } } [ 2 ; 0 ] = 0 1 0$ ，那么 $\mathsf { T _ { d } }$ 数值为 $9 ^ { \star } \mathsf { T } _ { \mathsf { p c l k } }$ 

在从机模式下，从机需要监视NSS信号，如果检测到错误的NSS信号，将会置位FERR标志位。例如，NSS信号在一个字节的中间位发生翻转。

## NSS脉冲模式操作流程

配置SPI_CTL1寄存器中的NSSP位使能该功能，为了确保使用该功能实现，需满足以下几个条件：配置设备为主机模式，使用普通SPI协议的数据帧格式，同时在第一个时钟跳变沿采样数据。

总之：MSTMOD = 1，NSSP = 1，CKPH = 0。

当使用NSS脉冲模式时，根据内部数据发送缓冲区/发送FIFO的状态，NSS脉冲会在两个连续的数据帧之间产生，且持续时间至少为1个SCK时钟周期。如果数据发送缓冲区/发送FIFO保持为空，可能会持续多个SCK时钟周期。NSS脉冲功能专为单一的主从应用设计，支持从机锁存数据。

下图描述了NSS脉冲模式在主机连续发送时的时序图。


图 23-14. NSS 脉冲模式时序图（主机连续发送）


<table><tr><td>NSS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SCK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MOSI</td><td>MSB</td><td></td><td>LSB</td><td>MSB</td><td></td><td>LSB</td><td></td></tr><tr><td>MISO</td><td>忽略</td><td>MSB</td><td></td><td>LSB</td><td>忽略</td><td>MSB</td><td></td></tr></table>

## SPI 四线模式操作流程

SPI四线模式用于控制四线SPI flash外设。

要配置成SPI四线模式，首先要确认TBE位置1，且TRANS位清零，然后将SPI_QCTL寄存器中的QMOD位置1。在SPI四线模式，SPI_CTL0寄存器中BDEN位、BDOEN位、CRCEN位、CRCNT位、CRCNT位、RO位和LF位保持清零，DZ[3:0]位域配置数据长度为8位，且MSTMOD位置1，以保证SPI工作于主机模式。SPIEN位、PSC位、CKPL位和CKPH位根据需要进行配置。

SPI四线模式有两种运行模式：四线写模式和四线读模式，通过SPI_QCTL寄存器中的QRD位进行配置。

## 四线写模式

当SPI_QCTL寄存器中的QMOD位置1且QRD位清零时，SPI工作在四线写模式。在四线写模式中，MOSI、MISO、IO2和IO3都用作输出引脚，在SCK产生时钟信号后，一旦数据写入SPI_DATA寄存器（TBE位清零）且SPIEN位置1时，将会通过这四个引脚发送写入的数据。SPI开始数据传输之后，每发送一个数据帧都要检测TBE标志位，若不能满足条件则停止传输。

四线模式下发送操作流程：

1. 根据应用需求，配置SPI_CTL0和SPI_CTL1中的时钟预分频、时钟极性、相位等参数；

2. 将SPI_QCTL中的QMOD位置1，然后将SPI_CTL0中的SPIEN位置1来使能SPI功能；

3. 向SPI_DATA寄存器中写入一个字节的数据，TBE标志位将会清零；

4. 等待硬件将TBE位重新置位，然后写入下一个字节数据。


图 23-15. SPI 四线模式四线写操作时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/da16c4154489f96fae4f1a7a2967e0ba396565ded6e25b8612016e157d0ffcdf.jpg)


## 四线读模式

当SPI_QCTL寄存器中的QMOD位和QRD位都置1时，SPI工作在四线读模式。在四线读模式中，MOSI、MISO、IO2和IO3都用作输入引脚，一旦数据写入SPI_DATA寄存器（TBE位清零）且SPIEN位置1时，在SCK信号线产生时钟信号。写数据到SPI_DATA寄存器只是为了产生SCK时钟信号，所以可以写入任何数据。SPI开始数据传输之后，每发送一个数据帧都要检测SPIEN位和TBE位，若条件不满足则停止传输。所以软件需要一直向SPI_DATA写空闲数据，以产生SCK时钟信号。

四线模式下接收操作流程：

1. 根据应用需求，配置SPI_CTL0和SPI_CTL1中时钟预分频、时钟极性、相位等参数；

2. 将SPI_QCTL中的QMOD位和QRD位置1，然后将SPI_CTL0中的SPIEN位置1来使能SPI功能；

3. 写任意数据（例如0xFF）到SPI_DATA寄存器；

4. 等待RBNE位置1，然后读SPI_DATA寄存器来获取接收的数据；

5. 写任意数据（例如0xFF）到SPI_DATA寄存器，以接收下一个字节数据。


图 23-16. SPI 四线模式四线读操作时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/3df3ff90f9ec168989f8896eb8b5fcc56313b80bcd56167bf0843366823d3505.jpg)


## SPI 停止流程

不同运行模式下采用不同的流程来停止SPI功能。

## MFD SFD

SPI0： 

等待TXLVL[1:0]=00和TRANS=0，接着通过清零SPIEN位关闭SPI。最后，读取数据直到RXLVL[1:0]=00。

SPI1： 

等待最后一个RBNE位并接收最后一个数据，等待TBE=1和TRANS=0，最后，通过清零SPIEN位关闭SPI。

## MTU MTB STU STB

SPI0： 

等待TXLVL[1:0]=00和TRANS=0，接着通过清零SPIEN位关闭SPI。

SPI1： 

将最后一个数据写入SPI_DATA寄存器，等待TBE位置1，等待TRANS位清零，通过清零SPIEN位关闭SPI。

## MRU MRB

SPI0： 

应用程序可以在任何时候关闭SPI功能，然后等待TRANS=0，读取数据直到RXLVL[1:0]=00。

SPI1： 

等待倒数第二个RBNE位置1，从SPI_DATA寄存器读数据，等待一个SCK时钟周期，然后通过清零SPIEN位关闭SPI。等待最后一个RBNE位置1，并从SPI_DATA读数据。

## SRU SRB

SPI0：应用程序可以在任何时候关闭SPI功能，然后等待TRANS=0，读取数据直到RXLVL[1:0]=00。SPI1：应用程序可以在任何时候关闭SPI功能，然后等待TRANS=0以确保当前通信过程结束。

## TI模式

TI模式的停止流程与上面描述过程相同。

## NSS脉冲模式

NSS脉冲模式的停止流程与上面描述过程相同。

## SPI四线模式

在禁用SPI四线模式和关闭SPI功能之前，软件应该先检查：TBE位置1，TRANS位清零，SPI_QCTL中的QMOD位和SPI_CTL0中的SPIEN位清零。

## 23.3.7. DMA 功能

DMA功能在传输过程中将应用程序从数据读写过程中释放出来，从而提高了系统效率。

通过置位SPI_CTL1寄存器中的DMATEN位和DMAREN位，使能SPI模式的DMA功能。为了使用DMA功能，软件首先应当正确配置DMA模块，然后通过初始化流程配置SPI模块，最后使能SPI。

SPI使能后，如果DMATEN位置1，每当TBE=1时，SPI将会发出一个DMA请求，然后DMA应答该请求，并自动写数据到SPI_DATA寄存器。如果DMAREN位置1，每当RBNE=1时，发出一个DMA请求，然后DMA应答该请求，并自动从SPI_DATA寄存器读取数据。

## DMA数据合并传输（只有 SPI0）

采用DMA进行数据传输，当BYTEN设置为0且DZ[3:0]配置的数据长度小于或等于8位且数据合

并模式使能时，DMA将会以16位方式访问SPI_DATA寄存器，自动完成数据的发送。

在数据合并模式使能且传输数据帧的帧数不是偶数倍的情况下，为了避免最后一次DMA传输多一帧数据的问题，需要将SPI_CTL1寄存器中TXDMA_ODD/RXDMA_ODD位为设置为1。

## 23.3.8. CRC 功能

SPI模块包含两个CRC计算单元：分别用于发送数据和接收数据。CRC计算单元使用SPI_CRCPOLY寄存器中定义的多项式。

通过配置SPI_CTL0中的CRCEN位使能CRC功能。对于数据线上每个发送和接收的数据，CRC单元逐位计算CRC值，计算得到的CRC值可以从SPI_TCRC寄存器和SPI_RCRC寄存器中读取。

为了传输计算得到的CRC值，应用程序需要在最后一个数据写入发送缓冲区之后，设置SPI_CTL0中的CRCNT位。在全双工模式（MFD或SFD），当SPI发送一个CRC值并且准备校验接收到的CRC值时，会将最新接收到的数据当作CRC值。在接收模式（MRB，MRU，SRU和SRB）下，在倒数第二个数据帧被接收后，软件将CRCNT位置1。在CRC校验失败时，CRCERR错误标志位将会置1。

对于SPI1，如果是8位数据长度，CRC计算基于CRC8标准进行。如果是16位数据长度，CRC计算基于CRC16标准进行。如果使能了DMA功能，软件不需要设置CRCNT位，硬件将会自动处理CRC传输和校验。

对于SPI0，只有数据长度为8位或者16位时，SPI提供CRC计算，且独立于数据长度，可以固定设置为8位或16位CRC计算。对于其他所有的数据长度，CRC无效。CRC数据交换，通常需要在数据序列结束后，再占用一个或多个数据通信的时间。例如，当设置为8位的数据长度并做16位CRC检查时，发送完整的CRC数据就要两帧。如果使能了DMA功能，硬件将会自动处理CRC传输和校验，但SPI需设置DMA发送通道和接收通道的计数器值。发送DMA计数器值为不包括CRC帧的数据帧的数量。接收DMA计数器值的配置如下：

1.全双工模式：假设SPI接收的数据量为L，当CRCL = 0且DZ = 8时，，则DMA接收通道的计数值等于L + 1，否则DMA接收通道的计数值等于L + 2。

2.只接收模式：DMA接收通道计数值只等于接收的数据量。接收数据完成后，通过软件读取SPI_RCRC寄存器的方式获取CRC值。

注意：当SPI处于从机模式且CRC功能使能时，无论SPI是否使能，CRC计算器都对输入SCK时钟敏感。只有当时钟稳定时，软件才能启用CRC，以避免错误的CRC计算。当SPI作为从机工作时，在数据阶段和CRC阶段之间，内部NSS信号需要保持低电平。

当配置SPI为从模式并且使用CRC功能时，即使NSS引脚为高时仍然会执行CRC的计算(当NSS信号为高时，只要SCK引脚上有时钟脉冲，则CRC计算会继续执行)。当主设备交替地与多个从设备进行通信时，将会出现这种情况,此时建议在NSS信号为低时重启CRC功能。当从设备未选中(NSS信号为高)转换到被选中为一个新的从设备(NSS信号为低)的时候，为了保持主从设备端下次CRC计算结果的同步，应该清除主从两端的CRC数值。建议按照下述步骤清除CRC数值：

1. 关闭SPI模块（SPIEN=0）；

2. 清除CRCEN位（CRCEN=0）；

3. 设置CRCEN位（CRCEN=1）；

4. 使能SPI模块（SPIEN=1）。

## 23.3.9. SPI 中断

## 状态标志位

## ◼ 发送缓冲区空标志位（TBE）

当发送缓冲区为空或当前发送FIFO的存储量小于或等于总存储量的一半时，TBE置位。软件可以通过写SPI_DATA寄存器将下一个待发送数据写入发送缓冲区/发送FIFO。

## ◼ 接收缓冲区非空标志位（RBNE）

对于SPI0，该位根据SPI_CTL1中的BYTEN位设置：如果BYTEN=0，则当前接收FIFO的存储量大于或等于总存储量的1/2时，RBNE置位。如果BYTEN=1，则当前接收FIFO的存储量大于或等于总存储量的1/4时，RBNE置位。表示此时接收到数据，并已存入接收FIFO中，软件可以通过读SPI_DATA寄存器来读取此数据。

对于SPI1，当接收缓冲区非空时，RBNE置位，表示此时接收到一个数据，并已存入到接收缓冲区中，软件可以通过读SPI_DATA寄存器来读取此数据。

## ◼ SPI通信进行中标志位（TRANS）

TRANS位是用来指示当前传输是否正在进行或结束的状态标志位，它由内部硬件置位和清除，无法通过软件控制。该标志位不会产生任何中断。

## 错误标志

## ◼ 配置错误标志（CONFERR）

在主机模式中，CONFERR位是一个错误标志位。在硬件NSS模式中，如果NSSDRV没有使能，当NSS被拉低时，CONFERR位被置1。在软件NSS模式中，当SWNSS位为0时，CONFERR位置1。当CONFERR位置1时，SPIEN位和MSTMOD位由硬件清除，SPI关闭，设备强制进入从机模式。

在CONFERR位清零之前，SPIEN位和MSTMOD位保持写保护，从机的CONFERR位不能置1。在多主机配置中，设备可以在CONFERR位置1时进入从机模式，这意味着发生了系统控制的多主冲突。

## ◼ 接收过载错误（RXORERR）

在RBNE位为1时，如果再有数据被接收，RXORERR位将会置1。对于SPI1，这说明，上一帧数据还未被读出而新的数据已经接收了。对于SPI0，这说明，接收FIFO没有足够的空间来存储接收到的数据了。接收缓冲区/接收FIFO的内容不会被新接收的数据覆盖，所以新接收的数据丢失。

## ◼ 帧错误（FERR）

在TI从机模式下，从机也要监视NSS信号，如果检测到错误的NSS信号，将会置位FERR标志

位。例如，NSS信号在一个字节的中间位发生翻转。

## ◼ CRC错误（CRCERR）

当CRCEN位置1时，SPI_RCRC寄存器中接收到的数据的CRC计算值将会和紧随着最后一帧数据后接收到的CRC值进行比较，当两者不同时，CRCERR位将会置1。


表 23-6. SPI 中断请求


<table><tr><td>中断事件</td><td>描述</td><td>清除方式</td><td>中断使能位</td></tr><tr><td>TBE</td><td>发送缓冲区/发送FIFO空</td><td>写SPI_DATA寄存器</td><td>TBEIE</td></tr><tr><td>RBNE</td><td>接收缓冲区/接收FIFO非空</td><td>读SPI_DATA寄存器</td><td>RBNEIE</td></tr><tr><td>CONFERR</td><td>配置错误</td><td>读或写 SPI_STAT 寄存器,然后写 SPI_CTL0 寄存器</td><td rowspan="4">ERRIE</td></tr><tr><td>RXORERR</td><td>接收过载错误</td><td>读SPI_DATA寄存器,然后读 SPI_STAT寄存器</td></tr><tr><td>CRCERR</td><td>CRC错误</td><td>写0到CRCERR位</td></tr><tr><td>FERR</td><td>TI模式帧错误</td><td>写0到FERR位</td></tr></table>

## 23.4. I2S功能说明

## 23.4.1. I2S 结构框图


图 23-17. I2S 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/fcd5f25e9e1a34408f01cc98a3e366aa3bc6c3fab72a1d1c92b927c783ceef4a.jpg)


I2S功能有5个子模块，分别是控制寄存器、时钟生成器、主机控制逻辑、从机控制逻辑和移位寄存器。所有的用户可配置寄存器都在控制寄存器模块实现，其中包括发送缓冲区和接收缓冲区。时钟生成器用来在主机模式下生成I2S通信时钟。主机控制逻辑用来在主机模式下生成信号并控制通信。从机控制逻辑根据接收到的 和 信号来控制从机模式的通信。移位寄存器控制I2S_SD上的串行数据发送和接收。

## 23.4.2. I2S 信号线描述

I2S接口有4个引脚，分别是I2S_CK、I2S_WS、I2S_SD和I2S_MCK。I2S_CK是串行时钟信号，与SPI_SCK共享引脚。I2S_WS是数据帧控制信号，与SPI_NSS共享引脚。I2S_SD是串行数据信号，与SPI_MOSI共享引脚。I2S_MCK是主时钟信号，它最大可提供一个256倍于Fs的时钟频率，其中Fs是音频采样率。

## 23.4.3. I2S 音频标准

I2S音频标准是通过设置SPI_I2SCTL寄存器中的I2SSTD位来选择的，可以选择四种音频标准：I2S飞利浦标准，MSB对齐标准，LSB对齐标准和PCM标准。除PCM之外的所有标准都是两个通道（左通道和右通道）的音频数据分时复用I2S接口的，并通过I2S_WS信号来区分当前数据属于哪个通道。对于PCM标准，I2S_WS信号表示帧同步信息。

数据长度和通道长度可以通过SPI_I2SCTL寄存器中的DTLEN位和CHLEN位来设置。由于通道长度必须大于或等于数据长度，所以有四种数据包类型可供选择。它们分别是：16位数据打包成16位数据帧格式，16位数据打包成32位数据帧格式，24位数据打包成32位数据帧格式，32位数据打包成32位数据帧格式。用于发送和接收的数据缓冲区都是16位宽度。所以，要完成数据长度为24位或32位的数据帧传输，SPI_DATA寄存器需要被访问2次；而要完成数据长度为16位的数据帧传输，SPI_DATA寄存器只需被访问1次。如需将16位数据打包成32位数据帧，硬件会自动插入16位0将16位数据扩展为32位格式。

对于所有标准和数据包类型来说，数据的最高有效位总是最先被发送的。对于所有基于两通道分时复用的标准来说，总是先发送左通道，然后是右通道。

## I2S飞利浦标准

对于I2S飞利浦标准，I2S_WS和I2S_SD在I2S_CK的下降沿变化，I2S_WS在数据的前一个时钟开始有效。各种配置情况的时序图如下所示。


图 23-18. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/657115e5c9d71e924723002f9824c8f3ec74ec99bfba36c1c5528a9dc1dfb924.jpg)



图 23-19. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/41ab1f0a29f07b974dcc584c9a3ce8916aa1b3910bcd897b734a1b7457396cef.jpg)


当 16 位数据打包成 16 位数据帧时，每完成一帧数据的传输只需要访问 SPI_DATA 寄存器一次。


图 23-20. I2S 飞利浦标准时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/150711d5df9770b94f2954dfd87041cbdc8c42d266f6854ab793cc47f31fd0d1.jpg)



图 23-21. I2S 飞利浦标准时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/f7a3141fc5c878b1df7e29a38c481a3ac4156be65f5eaed0bd57fbb5556af133.jpg)


当32位数据打包成32位数据帧的帧格式时，每完成1帧数据的传输需要访问SPI_DATA寄存器2次。在发送模式下，如果要发送一个32位数据，第一个写入SPI_DATA寄存器的数据应该是高16位数据，第二个数据应该是低16位数据。在接收模式下，如果要接收一个32位数据，第一个从SPI_DATA寄存器读到的数据应该是高16位数据，第二个数据应该是低16位数据。


图 23-22. I2S 飞利浦标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/0b6993141808f82d33633951ad2b54dc717c05cd35f2b796e05f51fe01f82a5c.jpg)



图 23-23. I2S 飞利浦标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/e59ccba18f7f178b01b1282ac5262d8c60f62774f02db1f5e7c5b28b06504c0d.jpg)


当24位数据打包成32位数据帧的帧格式时，每完成1帧数据的传输需要访问SPI_DATA寄存器2次。在发送模式下，如果要发送一个24位数据D[23:0]，第一个写入SPI_DATA寄存器的数据应该是高16位数据D[23:8]，第二个数据应该是一个16位数据，该16位数据的高8位是D[7:0]，低8位数据可以是任意值。在接收模式下，如果要接收一个24位数据D[23:0]，第一个从SPI_DATA寄存器读到的数据应该是高16位数据D[23:8]，第二个数据应该是一个16位数据，该16位数据的高8位是D[7:0]，低8位数据全是0。


图 23-24. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/72519de31b23f1c1061cde2a020d4f5d02b3ce793187bde2cc3313b8cdfae6e2.jpg)



图 23-25. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/616e2d8bc936d19b756b3d3e8a4922eaaba3852f3635e165352e1fd364868cc2.jpg)


当16位数据打包成32位数据帧时，每完成一帧数据的传输只需要访问SPI_DATA寄存器一次。为了将该16位数据扩展成32位数据，剩下的16位被硬件强制填充为0x0000。

## MSB对齐标准

对于MSB对齐标准，I2S_WS和I2S_SD在I2S_CK的下降沿变化。SPI_DATA 寄存器的处理方式与I2S飞利浦标准完全相同。各个配置情况的时序图如下所示。


图 23-26. MSB 对齐标准时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/ec7d13496edcc79e5a6106680a1d974941972e38c3d150119042df6e7802b5e5.jpg)



图 23-27. MSB 对齐标准时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/3162c2590bcae46726614fe6de10130f5d6e7dea33f108716ba0c8d03c453d82.jpg)



图 23-28. MSB 对齐标准时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/3e15b488226b614db959128c8673e0fc7217cf0cd1f56c52a0eef43d362638b1.jpg)



图 23-29. MSB 对齐标准时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/64cf9137b474313a52334d030544dead7c89f2fcc31014eb3b387062a7232948.jpg)



图 23-30. MSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/d01a485031f4fb760e836ec437e9b469d0ce1b60e24a59fe98e1b7d405f2af06.jpg)



图 23-31. MSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/5a5b951f565dcfa3c7d2ee60120897c41a3faca700bfa0019bfcccf0d7a6d09f.jpg)



图 23-32. MSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/1fcfd8b16d0b51ae7e0611a37da417e2605a433c6f9459d6857696ea1c87d2ce.jpg)



图 23-33. MSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/f78451f0ef6da1a0b3dd6cbe7eeb7b5f4de59310fdc1aef197feb0a06ae412a2.jpg)


## LSB 对齐标准

对于 对齐标准， 和 在 的下降沿变化。在通道长度与数据长度相同的情况下，LSB对齐标准和MSB对齐标准是完全相同的。对于通道长度大于数据长度的情况，LSB对齐标准的有效数据与最低位对齐，而MSB对齐标准的有效数据与最高位对齐。通道长度大于数据长度的各种配置情况时序图如下所示。


图 23-34. LSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/93ba9f3e595f28f7c2285107e68e299f4694e1bff2cad7028058edac0a949ab6.jpg)



图 23-35. LSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/a2ad57258d7da91be9915c2631a0a1d7539ac95808d474870911fd9497f8920a.jpg)


当24位数据打包成32位数据帧的帧格式时，每完成1帧数据的传输需要访问SPI_DATA寄存器2次。在发送模式下，如果要发送一个24位数据D[23:0]，第一个写入SPI_DATA寄存器的数据应该是一个16位数据，该16位数据的高8位可以是任意值，低8位是D[23:16]，第二个数据应该是低16位数据D[15:0]。在接收模式下，如果要接收一个24位数据D[23:0]，第一个从SPI_DATA寄存器读到的数据应该是一个16位数据，该16位数据的高8位是0，低8位是D[23:16]，第二个数据应该是低16位数据D[15:0]。


图 23-36. LSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/6156f9763ab87fe44fd448eab831b621930047561e839bf49b6b0acfed9fe3ef.jpg)



图 23-37. LSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/9d2f2db5b1e030f26e31e7890cdb3d40b8c9540028a4b4ccecb6f1cd283b99ec.jpg)


当16位数据打包成32位数据帧时，每完成一帧数据的传输只需要访问SPI_DATA寄存器一次。为了将该16位数据扩展成32位数据，剩下的16位被硬件强制填充为0x0000。

## PCM 标准

对于PCM标准，I2S_WS和I2S_SD在I2S_CK的上升沿变化，I2S_WS信号表示帧同步信息。可以通过SPI_I2SCTL寄存器的PCMSMOD位来选择短帧同步模式和长帧同步模式。SPI_DATA寄存器的处理方式与I2S飞利浦标准完全相同。短帧同步模式的各种配置情况时序图如下所示。


图 23-38. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/dc30c37fefc5b4dfe73772efae58cc372897c8b4797df8322de15b364d820f81.jpg)



图 23-39. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/6128b2e8d7d748f8f70167c1398970029e806a4a6a348bcef1458512f8d85b3c.jpg)



图 23-40. PCM 标准短帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/39f26ded659653e9b1182b12620d17d373bb2acb5492d51ef5603bce9768e86b.jpg)



图 23-41. PCM 标准短帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/6260538cca9c6efacd12e657c1a2a09bf88c2cb2d6dc6242f38974a27d626f55.jpg)



图 23-42. PCM 标准短帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/e0030fd04a39d4a78212eb520b8238c27760cb22c0d053fad16130383394a659.jpg)



图 23-43. PCM 标准短帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/84e57826e64c382d0ea341b413c99d454a4e0ce0a6bb111196f1373cdfb9408f.jpg)



图 23-44. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/cd7073ce24301841f4b6dd5d4fc48d49f06f67b44c07b0131d622162ef7c6da6.jpg)



图 23-45. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/7a079f7a410c5b5ff0c881ac9805c9e16a67680c662df600d2a04de18bc3b6af.jpg)



长帧同步模式的各种配置情况时序图如下所示。



图 23-46. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/0f84869ce9b3bb516172743d584564da5c619edb8934ae0912c526c822504800.jpg)



图 23-47. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/f4e1807bc95fe61f5c1f665a65cd7752624e68251e6ca6c551a995163ec192bf.jpg)



图 23-48. PCM 标准长帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/fbe00f4d0cc0a5271982d30cf148ffbcf6b5e92b3fba70359a73c430317a5a59.jpg)



图 23-49. PCM 标准长帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/69709830ed9daa8ab46096ee134341374da757574375ec0e70ac7621c14a39fd.jpg)



图 23-50. PCM 标准长帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/036e13293a91d79c1ec43dd5810f39feb41634daf20d30e54ce7fb654254d478.jpg)



图 23-51. PCM 标准长帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/8f0dbf42603b4c8ccdcbdfa3c0926fa4a189158fc0e021db676fa43c3557ce87.jpg)



图 23-52. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/4cddad0ee0d83ee4a11d9b3776ef404c311fe0acb56ea135b72f2a4736176422.jpg)



图 23-53. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/b6220c880e9bf22cf88b238af973045b01b95798b0c3153b613cc1586b428ab9.jpg)


## 23.4.4. I2S 时钟


图 23-54. I2S 时钟生成结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/21380fc94f4ad26b31242b97b72d297998d9cb7b0d024801918b98ecd120ee04.jpg)


I2S 时钟生成器框图如 23-54. I2S 所示。I2S 接口时钟是通过 SPI_I2SPSC寄存器的 位， 位和 位以及 寄存器的 位来配置的。时钟源是系统时钟（CK_SYS）。I2S比特率可以通过 23-7. I2S 所示的公式计算。


表 23-7. I2S 比特率计算公式


<table><tr><td>MCKOEN</td><td>CHLEN</td><td>公式</td></tr><tr><td>0</td><td>0</td><td>I2SCLK / (DIV * 2 + OF)</td></tr><tr><td>0</td><td>1</td><td>I2SCLK / (DIV * 2 + OF)</td></tr><tr><td>1</td><td>0</td><td>I2SCLK / (8 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>1</td><td>I2SCLK / (4 * (DIV * 2 + OF))</td></tr></table>


音频采样率（Fs）和I2S比特率的关系由如下公式定义：


Fs = I2S比特率 /（通道长度 * 通道数）

所以，为了得到期望的音频采样率，时钟生成器需要按 23-8. 所列的公式进行配置。


表 23-8. 音频采样频率计算公式


<table><tr><td>MCKOEN</td><td>CHLEN</td><td>公式</td></tr><tr><td>0</td><td>0</td><td>I2SCLK / (32 * (DIV * 2 + OF))</td></tr><tr><td>0</td><td>1</td><td>I2SCLK / (64 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>0</td><td>I2SCLK / (256 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>1</td><td>I2SCLK / (256 * (DIV * 2 + OF))</td></tr></table>


注意：I2S串行时钟的配置值需设置为低于PCLK时钟的1/6倍以下(不包含1/6)。


## 23.4.5. 运行

## 运行模式

运行模式是通过SPI_I2SCTL寄存器的I2SOPMOD位来选择的。共有四种运行模式可供选择：主机发送模式，主机接收模式，从机发送模式和从机接收模式。各种运行模式下 I2S 接口信号的方向如 23-9. I2S 所示。


表 23-9. 各种运行模式下 I2S接口信号的方向


<table><tr><td>运行模式</td><td>I2S_MCK</td><td>I2S_CK</td><td>I2S_WS</td><td>I2S_SD</td></tr><tr><td>主机发送</td><td>输出或 NU(1)</td><td>输出</td><td>输出</td><td>输出</td></tr><tr><td>主机接收</td><td>输出或 NU(1)</td><td>输出</td><td>输出</td><td>输入</td></tr><tr><td>从机发送</td><td>输出或 NU(1)</td><td>输入</td><td>输入</td><td>输出</td></tr><tr><td>从机接收</td><td>输出或 NU(1)</td><td>输入</td><td>输入</td><td>输入</td></tr></table>


1. NU表示该引脚没有被I2S使用，可以用于其他功能。


## I2S初始化流程

I2S初始化过程如 23-55. I2S 所示。


图 23-55. I2S 初始化流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/201ede7240193aa0664ad04f332dc59a51ad9e10c892cfd86ac3ec68f0c8628f.jpg)


## I2S主机发送流程

TBE标志位被用来控制发送流程。如前文所述，TBE标志位表示发送缓冲区空，此时，如果SPI_CTL1寄存器的TBEIE位为1，将产生中断。首先，发送缓冲区为空（TBE为1），且移位寄存器中没有发送序列。当16位数据被写入SPI_DATA寄存器时（TBE变为0），数据立即从发送缓冲区装载到移位寄存器中（TBE变为1）。此时，发送序列开始。

数据是并行地装载到16位移位寄存器中的，然后串行地从I2S_SD引脚发出（高位先发）。下一个数据应该在TBE为1时写入SPI_DATA寄存器。数据写入SPI_DATA寄存器之后，TBE变为0。当前发送序列结束时，发送缓冲区的数据会自动装载到移位寄存器中，然后TBE标志变回1。为了保证连续的音频数据发送，下一个将要发送的数据必须在当前发送序列结束之前写入SPI_DATA寄存器。

对于除PCM标准外的所有标准，I2SCH标志用来区别当前传输数据所属的通道。I2SCH标志在每次TBE标志由0变1的时候更新。刚开始I2SCH标志为0，表示左通道的数据应该被写入SPI_DATA寄存器。

为了关闭I2S，I2SEN位必须在TBE标志为1且TRANS标志为0之后清零。

## I2S主机接收流程

RBNE标志被用来控制接收序列。如前文所述，RBNE标志表示接收缓冲区非空，如果SPI_CTL1寄存器的RBNEIE位为1，将产生中断。当SPI_I2SCTL寄存器的I2SEN位被置1时，接收流程立即开始。首先，接收缓冲区为空（RBNE为0）。当一个接收流程结束时，接收到的数据将从移位寄存器装载到接收缓冲区（RBNE变为1）。当RBNE为1时，用户应该将数据从SPI_DATA寄存器中读走。读操作完成后，RBNE变为0。必须在下一次接收结束之前读走SPI_DATA寄存器中的数据，否则将发生接收过载错误。此时RXORERR标志位会被置1，如果SPI_CTL1寄存器的ERRIE位为1，将会产生中断。这种情况下，必须先关闭I2S再打开I2S，然后再恢复通讯。

对于除PCM之外的所有标准来说，I2SCH标志用来区分当前传输数据所属的通道。I2SCH标志在每次RBNE标志由0变1时更新。

为了关闭I2S，不同的音频标准，数据长度和通道长度采用不同的操作步骤。每种情况的操作如 23-56. I2S 所示。


图 23-56. I2S 主机接收禁能流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/634ae3c87d712e66ca39dcaa77a5cff6f6fb565c2dbe30ec429c0e3f4a56f2c9.jpg)


## I2S从机发送流程

从机发送流程和主机发送流程相似，不同之处如下：

在从机模式下，从机需要在外部主机开始通讯之前使能。当外部主机开始发送时钟信号且I2S_WS信号请求传输数据时，发送流程开始。数据需要在外部主机发起通讯之前写入SPI_DATA寄存器。为了确保音频数据的连续传输，必须在当前发送序列结束之前将下一个待发送的数据写入SPI_DATA寄存器，否则会产生发送欠载错误。此时TXURERR标志会置1，如果SPI_CTL1寄存器的ERRIE位为1，将会产生中断。这种情况下，必须先关闭I2S再打开I2S来恢复通讯。从机模式下，I2SCH标志是根据外部主机发送的I2S_WS信号而变化的。

为关闭I2S，必须在TBE标志变为1且TRANS标志变为0之后，才能清除I2SEN位。

## I2S从机接收流程

从机接收流程与主机接收流程类似。不同之处如下。

在从机模式下，从机需要在外部主机开始通讯之前使能。当外部主机开始发送时钟信号且I2S_WS信号指示数据开始时，接收流程开始。从机模式下，I2SCH标志是根据外部主机发送

的I2S_WS信号而变化的。

为了关闭I2S，必须在收到最后一个RBNE之后立即清除I2SEN位。

## 23.4.6. DMA 功能

DMA功能与SPI模式完全一样，唯一不同的地方就是I2S模式不支持CRC功能。

## 23.4.7. I2S 中断

状态标志位

SPI_STAT寄存器中有4个可用的标志位，分别是TBE、RBNE、TRANS和I2SCH，用户通过这些标志位可以全面监视I2S总线的状态。

◼ 发生缓冲区空标志（TBE）：

当发送缓冲区为空时，TBE置位。软件可以通过写SPI_DATA寄存器将下一个数据写入发送缓冲区。

◼ 接收缓冲区非空标志（RBNE）：

接收缓冲区非空时，RBNE置位，表示此时接收到一个数据，并已存入接收缓冲区中，软件可以通过读SPI_DATA寄存器来读取此数据。

◼ I2S通信进行中标志（TRANS）：

TRANS是用来指示当前传输是否正在进行或结束的状态标志，它由内部硬件置位和清除，无法进行软件操作。该标志位不会产生任何中断。

◼ I2S通道标志（I2SCH）：

I2SCH用来表明当前传输数据的通道信息，对PCM音频标准来说没有意义。在发送模式下，I2SCH标志在每次TBE由0变1时更新，在接收模式下，I2SCH标志在每次RBNE由0变1时更新。该标志位不会产生任何中断。

## 错误标志

有三个错误标志：

◼ 发送欠载错误标志（TXURERR）：

在从发送模式下，有效的SCK信号开始发送，当发送缓冲区为空时，发送欠载错误标志TXURERR置位。

◼ 接收过载错误标志（RXORERR）：

当接收缓冲区已满且又接收到一个新的数据时，接收过载错误标志RXORERR置位。当接收过载发生时，接收缓冲区中的数据没有更新，新接收的数据丢失。

◼ 帧格式错误（FERR）：

在从I2S模式下，I2S模块监视I2S_WS信号，如果I2S_WS信号在一个错误的位置发生翻转，将会置位FERR帧错误标志位。

23-10. I2S 总结了I2S中断事件和相应的使能位。


表 23-10. I2S 中断


<table><tr><td>中断标志</td><td>描述</td><td>清除方式</td><td>中断使能位</td></tr><tr><td>TBE</td><td>发送缓冲区空</td><td>写 SPI_DATA 寄存器</td><td>TBEIE</td></tr><tr><td>RBNE</td><td>接收缓冲区非空</td><td>读 SPI_DATA 寄存器</td><td>RBNEIE</td></tr><tr><td>TXURERR</td><td>发送欠载错误</td><td>读 SPI_STAT 寄存器</td><td rowspan="3">ERRIE</td></tr><tr><td>RXORERR</td><td>接收过载错误</td><td>读 SPI_DATA 寄存器,然后再读 SPI_STAT 寄存器</td></tr><tr><td>FERR</td><td>I2S 帧错误</td><td>读 SPI_STAT 寄存器</td></tr></table>
