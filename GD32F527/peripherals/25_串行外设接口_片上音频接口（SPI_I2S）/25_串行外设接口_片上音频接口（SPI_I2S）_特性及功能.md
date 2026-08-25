## 25. 串行外设接口/片上音频接口（SPI/I2S）

## 25.1. 简介

SPI/I2S 模块可以通过 SPI 协议或 I2S 音频协议与外部设备进行通信。

串行外设接口（Serial Peripheral Interface，缩写为 SPI）提供了基于 SPI 协议的数据发送和接收功能，可以工作于主机或从机模式。SPI 接口支持具有硬件 CRC 计算和校验的全双工和单工模式。SPI5 还支持 SPI 四线主机模式。

片上音频接口（Inter-IC Sound，缩写为 I2S）支持四种音频标准，分别是 I2S 飞利浦标准，MSB 对齐标准，LSB对齐标准和 PCM 标准。它可以在四种模式下运行，包括主机发送模式，主机接收模式，从机发送模式和从机接收模式。通过使用附加的 I2S 模块：I2S1_ADD 和I2S2_ADD，I2S1 和 I2S2 支持 I2S 全双工模式。

## 25.2. 主要特性

## 25.2.1. SPI 主要特性

- 具有全双工和单工模式的主从操作；

- 16位宽度，独立的发送和接收缓冲区；

- 8位或16位数据帧格式；

- 低位在前或高位在前的数据位顺序；

- 软件和硬件NSS管理；

- 硬件CRC计算、发送和校验；

- 发送和接收支持DMA模式；

- 支持SPI TI模式；

- 支持SPI四线功能的主机模式（只有SPI5）。

## 25.2.2. I2S 主要特性

- 具有发送和接收功能的主从操作；

- 具有全双工模式的主从操作（仅在SPI1和SPI2中）；

- 支持四种I2S音频标准：飞利浦标准，MSB对齐标准，LSB对齐标准和PCM标准；

- 数据长度可以为16位，24位和32位；

- 通道长度为16位或32位；

- 16位缓冲区用于发送和接收；

- 通过I2S时钟分频器，可以得到8 KHz到192 KHz的音频采样频率；

- 可编程空闲状态时钟极性；

- 可以输出主时钟（MCK）；

- 发送和接收支持DMA功能。

## 25.3. SPI 结构框图


图 25-1. SPI 结构框图


![image](images/6b985ca8079e.jpg)


## 25.4. SPI信号线描述

## 25.4.1. 常规配置（非 SPI四线模式）


表 25-1. SPI 信号描述


<table><tr><td>引脚名称</td><td>方向</td><td>描述</td></tr><tr><td>SCK</td><td>I/O</td><td>主机:SPI时钟输出从机:SPI时钟输入</td></tr><tr><td>MISO</td><td>I/O</td><td>主机:数据接收线从机:数据发送线主机双向线模式:不使用从机双向线模式:数据发送和接收线</td></tr><tr><td>MOSI</td><td>I/O</td><td>主机:数据发送线从机:数据接收线主机双向线模式:数据发送和接收线从机双向线模式:不使用</td></tr><tr><td>NSS</td><td>I/O</td><td>软件NSS模式:不使用主机硬件NSS模式:NSSDRV=1时,为NSS输出,适用于单主机模式;NSSDRV=0时,为NSS输入,适用于多主机模式。从机硬件NSS模式:为NSS输入,作为从机的片选信号</td></tr></table>

## 25.4.2. SPI 四线配置

SPI 默认配置为单路模式，当 SPI_QCTL 中的 QMOD 位置 1 时，配置为 SPI 四线模式（只适

用于 SPI5）。SPI 四线模式只能工作在主机模式。

在 SPI 四线模式下，SPI 通过以下 6 个引脚与外部设备连接：


表 25-2. SPI 四线信号描述


<table><tr><td>引脚名称</td><td>方向</td><td>描述</td></tr><tr><td>SCK</td><td>O</td><td>SPI 时钟输出</td></tr><tr><td>MOSI</td><td>I/O</td><td>发送或接收数据 0</td></tr><tr><td>MISO</td><td>I/O</td><td>发送或接收数据 1</td></tr><tr><td>IO2</td><td>I/O</td><td>发送或接收数据 2</td></tr><tr><td>IO3</td><td>I/O</td><td>发送或接收数据 3</td></tr><tr><td>NSS</td><td>O</td><td>NSS 输出</td></tr></table>

## 25.5. SPI 功能描述

## 25.5.1. SPI 时序和数据帧格式

SPI_CTL0 寄存器中的 CKPL 位和 CKPH 位决定了 SPI 时钟和数据信号的时序。CKPL 位决定了空闲状态时 SCK 的电平，CKPH 位决定了第一个或第二个时钟跳变沿为有效采样边沿。在 TI 模式下，这两位没有意义。


图 25-2. 常规模式下的 SPI 时序图


![image](images/55ad9e6b91ee.jpg)



图 25-3. SPI 四线模式下的 SPI 时序图（CKPL=1, CKPH=1, LF=0）


![image](images/0b66defbcaf5.jpg)



在常规模式中，通过 SPI_CTL0 中的 FF16 位配置数据长度，当 FF16=1 时，数据长度为 16位，否则为 8 位。在 SPI 四线模式下，数据帧长度固定为 8 位。


通过设置 SPI_CTL0 中的 LF 位可以配置数据顺序，当 LF=1 时，SPI 先发送 LSB 位，当 LF=0时，则先发送 MSB 位。在 TI 模式中，数据顺序固定为先发 MSB位。

## 25.5.2. NSS 功能

## 从机模式

当配置为从机模式（MSTMOD = 0）时，在硬件 NSS 模式（SWNSSEN = 0）下，SPI 从 NSS引脚获取 NSS 电平，在软件 NSS 模式（SWNSSEN = 1）下，SPI 根据 SWNSS 位得到 NSS电平。只有当 NSS 为低电平时，才能发送或接收数据。在软件 NSS 模式下，不使用 NSS 引脚。


表 25-3. 从机模式 NSS 功能


<table><tr><td>模式</td><td>寄存器配置</td><td>描述</td></tr><tr><td>从机硬件 NSS 模式</td><td>MSTMOD = 0SWNSSEN = 0</td><td>SPI 从机 NSS 电平从 NSS 引脚获取。</td></tr><tr><td>从机软件 NSS 模式</td><td>MSTMOD = 0SWNSSEN = 1</td><td>SPI 从机 NSS 电平由 SWNSS 位决定。SWNSS = 0: NSS 电平为低SWNSS = 1: NSS 电平为高</td></tr></table>

## 主机模式

在主机模式（MSTMOD=1）下，如果应用程序使用多主机连接方式，NSS 可以配置为硬件输入模式（SWNSSEN=0, NSSDRV=0）或者软件模式（SWNSSEN=1）。一旦 NSS 引脚（在硬件 NSS 模式下）或 SWNSS位（在软件 NSS 模式下）被拉低，SPI 将自动进入从机模式，并且产生主机配置错误，CONFERR 位置 1。

如果应用程序希望使用 NSS 引脚控制 SPI 从设备，NSS 应该配置为硬件输出模式（SWNSSEN=0, NSSDRV=1）。使能 SPI 之后，NSS 变为低电平。

应用程序可以使用一个通用 I/O 口作为 NSS 引脚，以实现更加灵活的 NSS 应用。


表 25-4. 主机模式 NSS 功能


<table><tr><td>模式</td><td>寄存器配置</td><td>描述</td></tr><tr><td>主机硬件 NSS 输出模式</td><td>MSTMOD = 1SWNSSEN = 0NSSDRV=1</td><td>适用于单主机模式,主机使用 NSS 引脚控制 SPI 从设备,此时 NSS 配置为硬件输出模式。使能 SPI 后 NSS 为低电平。</td></tr><tr><td>主机硬件 NSS 输入模式</td><td>MSTMOD = 1SWNSSEN = 0NSSDRV=0</td><td>适用于多主机模式,此时 NSS 配置为硬件输入模式,一旦 NSS 引脚被拉低,SPI 将自动进入从机模式,并且产生主机配置错误,CONFERR 位置 1。</td></tr><tr><td rowspan="2">主机软件 NSS 模式</td><td>MSTMOD = 1SWNSSEN = 1SWNSS = 0NSSDRV:不要求</td><td>适用于多主机模式,一旦 SWNSS = 0,SPI 将自动进入从机模式,并且产生主机配置错误,CONFERR 位置 1。</td></tr><tr><td>MSTMOD = 1SWNSSEN = 1SWNSS = 1NSSDRV:不要求</td><td>从机可以使用硬件或软件 NSS 模式</td></tr></table>

## 25.5.3. SPI 运行模式


表 25-5. SPI 运行模式


<table><tr><td>模式</td><td>描述</td><td>寄存器配置</td><td>使用的数据引脚</td></tr><tr><td>MFD</td><td>全双工主机模式</td><td>MSTMOD = 1RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 发送MISO: 接收</td></tr><tr><td>MTU</td><td>单向线连接主机发送模式</td><td>MSTMOD = 1RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 发送MISO: 不使用</td></tr><tr><td>MRU</td><td>单向线连接主机接收模式</td><td>MSTMOD = 1RO = 1BDEN = 0BDOEN: 不要求</td><td>MOSI: 不使用MISO: 接收</td></tr><tr><td>MTB</td><td>双向线连接主机发送模式</td><td>MSTMOD = 1RO = 0BDEN = 1BDOEN = 1</td><td>MOSI: 发送MISO: 不使用</td></tr><tr><td>MRB</td><td>双向线连接主机接收模式</td><td>MSTMOD = 1RO = 0BDEN = 1BDOEN = 0</td><td>MOSI: 接收MISO: 不使用</td></tr><tr><td>SFD</td><td>全双工从机模式</td><td>MSTMOD = 0RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 接收MISO: 发送</td></tr><tr><td>STU</td><td>单向线连接从机发送模式</td><td>MSTMOD = 0RO = 0BDEN = 0BDOEN: 不要求</td><td>MOSI: 不使用MISO: 发送</td></tr><tr><td>SRU</td><td>单向线连接从机接收模式</td><td>MSTMOD = 0RO = 1BDEN = 0BDOEN: 不要求</td><td>MOSI: 接收MISO: 不使用</td></tr><tr><td>STB</td><td>双向线连接从机发送模式</td><td>MSTMOD = 0RO = 0BDEN = 1BDOEN = 1</td><td>MOSI: 不使用MISO: 发送</td></tr><tr><td>SRB</td><td>双向线连接从机接收模式</td><td>MSTMOD = 0RO = 0BDEN = 1BDOEN = 0</td><td>MOSI: 不使用MISO: 接收</td></tr></table>


图 25-4. 典型的全双工模式连接


<table><tr><td>主机MFD</td><td>从机SFD</td></tr><tr><td>SCK</td><td>SCK</td></tr><tr><td>MISO</td><td>MISO</td></tr><tr><td>MOSI</td><td>MOSI</td></tr><tr><td>NSS</td><td>NSS</td></tr></table>


图 25-5. 典型的单工模式连接（主机：接收，从机：发送）


![image](images/8b95f29dfa55.jpg)



图 25-6. 典型的单工模式连接（主机：只发送，从机：接收）


<table><tr><td colspan="2">Master MTU</td><td>Slave SRU</td></tr><tr><td>SCK</td><td></td><td>SCK</td></tr><tr><td>MISO</td><td></td><td>MISO</td></tr><tr><td>MOSI</td><td></td><td>MOSI</td></tr><tr><td>NSS</td><td></td><td>NSS</td></tr></table>


图 25-7. 典型的双向线连接


<table><tr><td>MasterMTB/MRB</td><td>SlaveSRB/STB</td></tr><tr><td>SCK</td><td>SCK</td></tr><tr><td>MISO</td><td>MISO</td></tr><tr><td>MOSI</td><td>MOSI</td></tr><tr><td>NSS</td><td>NSS</td></tr></table>

## SPI 初始化流程

在发送或接收数据之前，应用程序应遵循如下的 SPI 初始化流程：

1. 如果工作在主机模式或从机TI模式，配置SPI_CTL0中的PSC[2:0]位来生成预期波特率的SCK信号，或配置TI模式下的Td时间。否则，忽略此步骤。

2. 配置数据格式（SPI_CTL0中的FF16位）

3. 配置时钟时序（SPI_CTL0中的CKPL位和CKPH位）。

4. 配置帧格式（SPI_CTL0中的LF位）。

5. 按照上文NSS功能的描述，根据应用程序的需求，配置NSS模式（SPI_CTL0中的SWNSSEN位和SPI_CTL1中的NSSDRV位）。

6. 如果工作在TI模式，需要将SPI_CTL1中的TMOD位置1，否则，忽略此步骤。

7. 根据表25-5. SPI运行模式，配置MSTMOD位、RO位、BDEN位和BDOEN位。

8. 如果工作在SPI四线模式，需要将SPI_QCTL中的QMOD位置1，如果不是，则忽略此步骤。

9. 使能SPI（将SPIEN位置1）。

注意：在通信过程中，不应更改 CKPH、CKPL、MSTMOD、PSC[2:0]、LF 位。

## SPI 基本发送和接收流程

## 发送流程

在完成初始化过程之后，SPI 模块使能并保持在空闲状态。在主机模式下，当软件写一个数据到发送缓冲区时，发送过程开始。在从机模式下，当 SCK 引脚上的 SCK 信号开始翻转，且NSS 引脚电平为低，发送过程开始。所以，在从机模式下，应用程序必须确保在数据发送开始前，数据已经写入发送缓冲区中。

当 SPI 开始发送一个数据帧时，首先将这个数据帧从数据缓冲区加载到移位寄存器中，然后开始发送加载的数据。在数据帧的第一位发送之后， （发送缓冲区空）位置 。 标志位置 1，说明发送缓冲区为空，此时如果需要发送更多数据，软件应该继续写 SPI_DATA寄存器。

在主机模式下，若想要实现连续发送功能，那么在当前数据帧发送完成前，软件应该将下一个数据写入 SPI_DATA 寄存器中。

## 接收流程

在最后一个采样时钟边沿之后，接收到的数据将从移位寄存器存入到接收缓冲区，且 RBNE（接收缓冲区非空）位置 。软件通过读 寄存器获得接收的数据，此操作会自动清除RBNE 标志位。在 MRU 和 MRB 模式中，为了接收下一个数据帧，硬件需要连续发送时钟信号，而在全双工主机模式（MFD）中，当发送缓冲区非空时，硬件才接收下一个数据帧。

## SPI 不同模式下的操作流程（非 SPI四线模式或 TI 模式）

在全双工模式下，无论是 MFD 模式或者 SFD 模式，应用程序都应该监视 RBNE 标志位和 TBE标志位，并且遵循上文描述的操作流程。

发送模式（MTU，MTB，STU 或 STB）与全双工模式中的发送流程类似，不同的是需要忽略RBNE 位和 RXORERR 位。

相比于发送模式的情况，主机接收模式（MRU 或 MRB）与全双工的接收流程大不相同。在模式或 模式下，在 使能后， 产生连续的 信号，直到 停止。所以，软件应该忽略 TBE标志位，并且在 RBNE 位置 1 后，读出接收缓冲区内的数据，否则，将会产生接收过载错误。

除了忽略 TBE 标志位，且只执行上述的接收流程之外，从机接收模式(SRU 或 SRB)与全双工模式类似。

## SPI TI 模式

SPI TI模式将NSS作为一种特殊的帧头标志信号，它的操作流程与上文描述的常规模式类似。上文描述的模式（MFD，MTU，MRU，MTB，MRB，SFD，STU，SRU，STB 和 SRB）都支持 TI 模式。但是，在 TI 模式中，SPI_CTL0 中的 CKPL 位和 CKPH 位是没有意义的，SCK信号的采样边沿为下降沿。


图 25-8. 主机 TI模式在不连续发送时的时序图


![image](images/471eee58e9db.jpg)



图 25-9. 主机 TI模式在连续发送时的时序图


![image](images/f0d7c60bd46e.jpg)


在主机 TI 模式下，SPI 模块可实现连续传输或者不连续传输。如果主机写 SPI_DATA 的速度很快，那么就是连续传输，否则，为不连续传输。在不连续传输中，在每个字节传输前需要一个额外的时钟周期。但是在连续传输中，额外的时钟周期只存在于第一个字节之前，随后字节的起始时钟周期被前一个字节的最后一位的时钟周期覆盖。


图 25-10. 从机 TI 模式时序图


![image](images/af533c4c2c7d.jpg)


在从机 TI 模式中，在 SCK 信号的最后一个上升沿，从机开始发送最后一个字节的 LSB 位，在半位的时间之后，主机开始采集数据。为了确保主机采集到正确的数据，在释放该引脚之前，从机需要在 SCK 信号的下降沿之后继续驱动该位一段时间，这段时间称为 $\mathsf { T _ { d } }$ ， $\mathsf { T _ { d } }$ 通过SPI_CTL0 寄存器中的 PSC[2:0]位来设置。

$$
T _ {d} = \frac {T _ {\text {bit}}}{2} + 5 ^ {*} T _ {\text {pclk}}\tag{25-1}
$$

例如，如果 PSC[2:0] = 010，那么 ${ \sf T _ { d } }$ 数值为 9*Tpclk。

在从机模式下，从机需要监视 NSS 信号，如果检测到错误的 NSS信号，将会置位 FE标志位。例如，NSS 信号在一个字节的中间位发生翻转。

## SPI 四线模式操作流程

SPI 四线模式用于控制四线 SPI Flash 外设。

要配置成 SPI 四线模式，首先要确认 TBE 位置 1，且 TRANS 位清零，然后将 SPI_QCTL 寄存器中的 QMOD 位置 1。在 SP 四线模式，SPI_CTL0 寄存器中 BDEN 位、BDOEN 位、CRCEN 位、CRCNT 位、FF16 位、RO 位和 LF 位保持清零，且 MSTMOD 位置 1，以保证SPI 工作于主机模式。SPIEN 位、PSC 位、CKPL 位和 CKPH 位根据需要进行配置。

SPI 四线模式有两种运行模式：四线写模式和四线读模式，通过 SPI_QCTL 寄存器中的 QRD位进行配置。

## 四线写模式

当SPI_QCTL寄存器中的QMOD位置1且QRD位清零时，SPI工作在四线写模式。在四线写模式中，MOSI、MISO、IO2和IO3都用作输出引脚，在SCK产生时钟信号后，一旦数据写入SPI_DATA寄存器（TBE位清零）且SPIEN位置1时，将会通过这四个引脚发送写入的数据。SPI开始数据传输之后，每发送一个数据帧都要检测TBE标志位，若不能满足条件则停止传输。

四路模式下发送操作流程：

1. 根据应用需求，配置SPI_CTL0和SPI_CTL1中的时钟预分频、时钟极性、相位等参数；

2. 将SPI_QCTL中的QMOD位置1，然后将SPI_CTL0中的SPIEN位置1来使能SPI功能；

3. 向SPI_DATA寄存器中写入一个字节的数据，TBE标志位将会清零；

4. 等待硬件将TBE位重新置位，然后写入下一个字节数据。


图 25-11. SPI 四线模式写操作时序图


![image](images/a6756b0ad85f.jpg)


## 四线读模式

当 SPI_QCTL 寄存器中的 QMOD 位和 QRD 位都置 1 时，SPI 工作在四路读模式。在四路读模式中，MOSI、MISO、IO2 和 IO3 都用作输入引脚。当数据写入 SPI_DATA 寄存器（此时

TBE 位被清零）且 SPIEN 位置 1 时，SPI 开始在 SCK 信号线上产生时钟信号。写数据到SPI_DATA 寄存器只是为了产生 SCK 时钟信号，所以可以写入任何数据。SPI 开始数据传输之后，每发送一个数据帧都要检测 SPIEN 位和 TBE 位，若条件不满足则停止传输。所以软件需要一直向 SPI_DATA 写空闲数据，以产生 SCK 时钟信号。

四线模式下接收操作流程：

1. 根据应用需求，配置SPI_CTL0和SPI_CTL1中时钟预分频、时钟极性、相位等参数；

2. 将SPI_QCTL中的QMOD位和QRD位置1，然后将SPI_CTL0中的SPIEN位置1来使能SPI功能；

3. 写任意数据（例如0xFF）到SPI_DATA寄存器；

4. 等待RBNE位置1，然后读SPI_DATA寄存器来获取接收的数据；

5. 写任意数据（例如0xFF）到SPI_DATA寄存器，以接收下一个字节数据。


图 25-12. SPI 四线模式读操作时序图


![image](images/0706acd86a18.jpg)


## SPI 停止流程

不同运行模式下采用不同的流程来停止 SPI 功能：

## MFD SFD

等待最后一个 RBNE 置位并接收最后一个数据，等待 TBE=1 和 TRANS=0。最后，通过清零SPIEN 位关闭 SPI。

## MTU MTB STU STB

将最后一个数据写入 SPI_DATA 寄存器，等待 TBE 位置 1。然后等待 TRANS 位清零，通过清零 SPIEN 位关闭 SPI。

## MRU MRB

等待倒数第二个 RBNE 位置 1，从 SPI_DATA寄存器读数据，等待一个 SCK时钟周期，然后通过清零 SPIEN 位关闭 SPI。等待最后一个 RBNE位置 1，并从 SPI_DATA 读数据。

## SRU SRB

当应用程序不想接收数据时，可以禁用SPI，然后等待TRANS=0以确保正在进行的传输完成。

## TI 模式

TI 模式的停止流程与上面描述过程相同。

## SPI 四线模式

在禁用 SPI 四路模式或者关闭 SPI 功能之前，软件应该先检查：TBE位置 1，TRANS位清零，SPI_QCTL 中的 QMOD 位和 SPI_CTL0 中的 SPIEN 位清零。

## 25.5.4. DMA 功能

DMA功能在传输过程中将应用程序从数据读写过程中释放出来，从而提高了系统效率。

通过置位 SPI_CTL1 寄存器中的 DMATEN 位和 DMAREN 位，使能 SPI 模式的 DMA 功能。为了使用 DMA 功能，软件首先应当正确配置 DMA模块，然后通过初始化流程配置 SPI 模块，最后使能 SPI。

SPI 使能后，如果 DMATEN 位置 1，每当 TBE=1 时，SPI 将会发出一个 DMA 请求，然后 DMA应答该请求，并自动写数据到 SPI_DATA寄存器。如果 DMAREN 位置 1，每当 RBNE=1 时，SPI 将会发出一个 DMA请求，然后 DMA应答该请求，并自动从 SPI_DATA 寄存器读取数据。

## 25.5.5. CRC 功能

SPI 模块包含两个 CRC 计算单元：分别用于发送数据和接收数据。CRC 计算单元使用SPI_CRCPOLY 寄存器中定义的多项式。

通过配置 SPI_CTL0 中的 CRCEN 位使能 CRC 功能。对于数据线上每个发送和接收的数据，CRC 单元逐位计算 CRC 值，计算得到的 CRC 值可以从 SPI_TCRC 寄存器和 SPI_RCRC 寄存器中读取。

为了传输计算得到的 值，应用程序需要在最后一个数据写入发送缓冲区之后，设置SPI_CTL0 中的 CRCNT 位。在全双工模式（MFD 或 SFD），当 SPI 发送一个 CRC 值并且准备校验接收到的 C C 值时，会将最新接收到的数据当作 C C 值。在接收模式（ ， ，SRU 和 SRB）下，在倒数第二个数据帧被接收后，软件应该把 CRCNT 位置 1。在 CRC 校验失败时，CRCERR 错误标志位将会置 1。

如果使能了 DMA 功能，软件不需要设置 CRCNT 位，硬件将会自动处理 CRC 传输和校验。

注意：当 SPI 处于从机模式且 CRC 功能使能时，无论 SPI 是否使能，CRC 计算器都对输入SCK 时钟敏感。只有当时钟稳定时，软件才能启用 CRC，以避免错误的 CRC 计算。当 SPI 作为从机工作时，在数据阶段和 CRC 阶段之间，内部 NSS信号需要保持低电平。

当配置SPI为从模式并且使用CRC功能时，即使NSS引脚为高时仍然会执行CRC的计算(当NSS信号为高时，只要SCK引脚上有时钟脉冲，则CRC计算会继续执行)。当主设备交替地与多个从设备进行通信时，将会出现这种情况,此时建议在NSS信号为低时重启CRC功能。当从设备未选中(NSS信号为高)转换到被选中为一个新的从设备(NSS信号为低)的时候，为了保持主从设备端下次CRC计算结果的同步，应该清除主从两端的CRC数值。建议按照下述步骤清除CRC数值：

1. 关闭SPI模块（SPIEN=0）;

2. 清除CRCEN位（CRCEN=0）;

3. 设置CRCEN位（CRCEN=1）;

4. 使能SPI模块（SPIEN=1）。

## 25.6. SPI 中断

## 25.6.1. 状态标志位

- 发送缓冲区空标志位（TBE）

当发送缓冲区为空时，TBE 置位。软件可以通过写 SPI_DATA 寄存器将下一个待发送数据写入发送缓冲区。

- 接收缓冲区非空标志位（RBNE）

当接收缓冲区非空时，RBNE 置位，表示此时接收到一个数据，并已存入到接收缓冲区中，软件可以通过读 SPI_DATA寄存器来读取此数据。

- SPI通信进行中标志位（TRANS）

位是用来指示当前传输是否正在进行或结束的状态标志位，它由内部硬件置位和清除，无法通过软件控制。该标志位不会产生任何中断。

## 25.6.2. 错误标志

- 配置错误标志（CONFERR）

在主机模式中，CONFERR 位是一个错误标志位。在硬件 NSS 模式中，如果 NSSDRV 没有使能，当 NSS 被拉低时，CONFERR 位被置 1。在软件 NSS 模式中，当 SWNSS位为 0 时，CONFERR 位置 1。当 CONFERR 位置 1 时，SPIEN 位和 MSTMOD 位由硬件清除，SPI 关闭，设备强制进入从机模式。

在 CONFERR 位清零之前，SPIEN 位和 MSTMOD 位保持写保护，从机的 CONFERR 位不能置 1。在多主机配置中，设备可以在 CONFERR 位置 1 时进入从机模式，这意味着发生了系统控制的多主冲突。

- 接收过载错误（RXORERR）

在 RBNE 位为 1 时，如果再有数据被接收，RXORERR 位将会置 1。这说明，上一帧数据还未被读出而新的数据已经接收了。接收缓冲区的内容不会被新接收的数据覆盖，所以新接收的数据丢失。

- 帧错误（FERR）

在 TI 从机模式下，从机也要监视 NSS 信号，如果检测到错误的 NSS 信号，将会置位 FERR

标志位。例如，NSS信号在一个字节的中间位发生翻转。

- CRC错误（CRCERR）

当 CRCEN 位置 1 时，SPI_RCRC 寄存器中接收到的 CRC 值将会和紧随着最后一帧数据接收到的 CRC 值进行比较。当两者不同时，CRCERR 位将会置 1。


表 25-6. SPI 中断请求


<table><tr><td>中断事件</td><td>描述</td><td>清除方式</td><td>中断使能位</td></tr><tr><td>TBE</td><td>发送缓冲区空</td><td>写SPI_DATA寄存器</td><td>TBEIE</td></tr><tr><td>RBNE</td><td>接收缓冲区非空</td><td>读SPI_DATA寄存器</td><td>RBNEIE</td></tr><tr><td>CONFERR</td><td>配置错误</td><td>读或写 SPI_STAT 寄存器,然后写 SPI_CTL0 寄存器</td><td rowspan="4">ERRIE</td></tr><tr><td>RXORERR</td><td>接收过载错误</td><td>读SPI_DATA寄存器,然后读 SPI_STAT寄存器</td></tr><tr><td>CRCERR</td><td>CRC错误</td><td>写0到CRCERR位</td></tr><tr><td>FERR</td><td>TI模式帧错误</td><td>写0到FERR位</td></tr></table>

## 25.7. I2S结构框图


图 25-13. I2S 结构框图


![image](images/bbc1cce462cc.jpg)


S功能有 个子模块，分别是控制寄存器、时钟生成器、主机控制逻辑、从机控制逻辑和移位寄存器。所有的用户可配置寄存器都在控制寄存器模块实现，其中包括发送缓冲区和接收缓冲区。时钟生成器用来在主机模式下生成 I2S 通信时钟。主机控制逻辑用来在主机模式下生成I2S_WS 信号并控制通信。从机控制逻辑根据接收到的 I2SCK 和 I2S_WS 信号来控制从机模式的通信。移位寄存器控制 I2S_SD 上的串行数据发送和接收。

## 25.8. I2S信号线描述

I2S 接口有 4 个引脚，分别是 I2S_CK、I2S_WS、I2S_SD 和 I2S_MCK。I2S_CK 是串行时钟信号，与 SPI_SCK 共享引脚。I2S_WS 是数据帧控制信号，与 SPI_NSS 共享引脚。I2S_SD是串行数据信号，与 SPI_MOSI 共享引脚。I2S_MCK 是主时钟信号，在 SPI0，SPI3 和 SPI4中，与 SPI_MISO 共享引脚，而在 SPI1 和 SPI2 中，I2S_MCK 有一个专用引脚。I2S_MCK对于 I2S 接口而言是个可选信号，它提供了一个 256 倍于 Fs 的时钟频率，其中 Fs 是音频采样率。

## 25.9. I2S 功能描述

## 25.9.1. I2S 音频标准

I2S 音频标准是通过设置 SPI_I2SCTL 寄存器中的 I2SSTD[1:0]位域来选择的，可以选择四种音频标准：I2S 飞利浦标准，MSB对齐标准，LSB对齐标准和 PCM 标准。除 PCM 之外的所有标准都是两个通道(左通道和右通道)的音频数据分时复用 I2S 接口的，并通过 I2S_WS信号来区分当前数据属于哪个通道。对于 PCM 标准，I2S_WS信号表示帧同步信息。

数据长度和通道长度可以通过 寄存器中的 位和 位来设置。由于通道长度必须大于或等于数据长度，所以有四种数据包类型可供选择。它们分别是：16 位数据打包成 16 位数据帧格式，16 位数据打包成 32 位数据帧格式，24 位数据打包成 32 位数据帧格式，32 位数据打包成 32 位数据帧格式。用于发送和接收的数据缓冲区都是 16 位宽度。所以，要完成数据长度为 24 位或 32 位的数据帧传输，SPI_DATA寄存器需要被访问 2 次；而要完成数据长度为 16 位的数据帧传输，SPI_DATA 寄存器只需被访问 1 次。如需将 16 位数据打包成 32 位数据帧，硬件会自动插入 16 位 0 将 16 位数据扩展为 32 位格式。

对于所有标准和数据包类型来说，数据的最高有效位总是最先被发送的。对于所有基于两通道分时复用的标准来说，总是先发送左通道，然后是右通道。

## I2S飞利浦标准

对于 I2S 飞利浦标准，I2S_WS 和 I2S_SD 在 I2S_CK 的下降沿变化，I2S_WS 在数据的前一个时钟开始有效。各种配置情况的时序图如下所示。


图 25-14. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](images/7ef8d26647d2.jpg)



图 25-15. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](images/6b722f262ff6.jpg)



当 16 位数据打包成 16 位数据帧时，每完成一帧数据的传输只需要访问 SPI_DATA 寄存器一


次。


图 25-16. I2S 飞利浦标准时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](images/d795ff0eeece.jpg)



图 25-17. I2S 飞利浦标准时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](images/327335a28e82.jpg)


当 32 位数据打包成 32 位数据帧的帧格式时，每完成 1 帧数据的传输需要访问 SPI_DATA 寄存器 2 次。在发送模式下，如果要发送一个 32 位数据，第一个写入 SPI_DATA 寄存器的数据应该是高 16 位数据，第二个数据应该是低 16 位数据。在接收模式下，如果要接收一个 32 位数据，第一个从 SPI_DATA 寄存器读到的数据应该是高 16 位数据，第二个数据应该是低 16位数据。


图 25-18. I2S 飞利浦标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](images/08ea16eb65db.jpg)



图 25-19. I2S 飞利浦标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](images/a4ca6687cbf4.jpg)


当 24 位数据打包成 32 位数据帧的帧格式时，每完成 1 帧数据的传输需要访问 SPI_DATA 寄存器 2 次。在发送模式下，如果要发送一个 24 位数据 D[23:0]，第一个写入 SPI_DATA 寄存器的数据应该是高 16 位数据 D[23:8]，第二个数据应该是一个 16 位数据，该 16 位数据的高 8位是 D[7:0]，低 8 位数据可以是任意值。在接收模式下，如果要接收一个 24 位数据 D[23:0]，第一个从 SPI_DATA 寄存器读到的数据应该是高 16 位数据 D[23:8]，第二个数据应该是一个16 位数据，该 16 位数据的高 8 位是 D[7:0]，低 8 位数据全是 0。


图 25-20. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](images/5e333acb611c.jpg)



图 25-21. I2S 飞利浦标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](images/2573702e1c7b.jpg)


当 16 位数据打包成 32 位数据帧时，每完成一帧数据的传输只需要访问 SPI_DATA 寄存器一次。为了将该 16 位数据扩展成 32 位数据，剩下的 16 位被硬件强制填充为 0x0000。

## MSB对齐标准

对于MSB对齐标准，I2S_WS和I2S_SD在I2S_CK的下降沿变化。SPI_DATA寄存器的处理方式与I2S飞利浦标准完全相同。各个配置情况的时序图如下所示。


图 25-22. MSB 对齐标准时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](images/fe3c2f7ed8dc.jpg)



图 25-23. MSB 对齐标准时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](images/84d377386ae8.jpg)



图 25-24. MSB 对齐标准时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](images/591bdd05cded.jpg)



图 25-25. MSB 对齐标准时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](images/e863aa0d3c71.jpg)



图 25-26. MSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](images/28b6f792892c.jpg)



图 25-27. MSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](images/740390cd468f.jpg)



图 25-28. MSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](images/6228803320bf.jpg)



图 25-29. MSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](images/945299dbe603.jpg)


## LSB对齐标准

对于 LSB对齐标准，I2S_WS 和 I2S_SD 在 I2S_CK 的下降沿变化。在通道长度与数据长度相同的情况下，LSB 对齐标准和 MSB对齐标准是完全相同的。对于通道长度大于数据长度的情况，LSB对齐标准的有效数据与最低位对齐，而 MSB 对齐标准的有效数据与最高位对齐。通道长度大于数据长度的各种配置情况时序图如下所示。


图 25-30. LSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](images/8ade1d67ac79.jpg)



图 25-31. LSB 对齐标准时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](images/b73a2a27f39c.jpg)


当 24 位数据打包成 32 位数据帧的帧格式时，每完成 1 帧数据的传输需要访问 SPI_DATA 寄存器 2 次。在发送模式下，如果要发送一个 24 位数据 D[23:0]，第一个写入 SPI_DATA 寄存器的数据应该是一个 16 位数据，该 16 位数据的高 8 位可以是任意值，低 8 位是 D[23:16]，第二个数据应该是低 16 位数据 D[15:0]。在接收模式下，如果要接收一个 24 位数据 D[23:0]，第一个从 SPI_DATA 寄存器读到的数据应该是一个 16 位数据，该 16 位数据的高 8 位是 0，低 8 位是 D[23:16]，第二个数据应该是低 16 位数据 D[15:0]。


图 25-32. LSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](images/62fd1eec918a.jpg)



图 25-33. LSB 对齐标准时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](images/04f4bc83609d.jpg)


当 16 位数据打包成 32 位数据帧时，每完成一帧数据的传输只需要访问 SPI_DATA 寄存器一次。为了将该 16 位数据扩展成 32 位数据，剩下的 16 位被硬件强制填充为 0x0000。

## PCM 标准

对于 PCM 标准，I2S_WS 和 I2S_SD 在 I2S_CK 的上升沿变化，I2S_WS 信号表示帧同步信息。可以通过 SPI_I2SCTL 寄存器的 PCMSMOD 位来选择短帧同步模式和长帧同步模式。SPI_DATA寄存器的处理方式与 I2S 飞利浦标准完全相同。短帧同步模式的各种配置情况时序图如下所示。


图 25-34. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](images/3c0ed80eb110.jpg)



图 25-35. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](images/df5efad63f69.jpg)



图 25-36. PCM 标准短帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](images/ade9d141871b.jpg)



图 25-37. PCM 标准短帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](images/1f4ce4ab7749.jpg)



图 25-38. PCM 标准短帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](images/b5c9a9320c8d.jpg)



图 25-39. PCM 标准短帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](images/edcbe9f756ed.jpg)



图 25-40. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](images/efcb007de047.jpg)



图 25-41. PCM 标准短帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](images/279083d56ddd.jpg)



长帧同步模式的各种配置情况时序图如下所示。



图 25-42. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=0）


![image](images/c8338a517a57.jpg)



图 25-43. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=0, CKPL=1）


![image](images/27511e8d5204.jpg)



图 25-44. PCM 标准长帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=0）


![image](images/9d42e13e1c83.jpg)



图 25-45. PCM 标准长帧同步模式时序图（DTLEN=10, CHLEN=1, CKPL=1）


![image](images/ee6d77c12142.jpg)



图 25-46. PCM 标准长帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=0）


![image](images/d8b3788f50a2.jpg)



图 25-47. PCM 标准长帧同步模式时序图（DTLEN=01, CHLEN=1, CKPL=1）


![image](images/b31d7b04f281.jpg)



图 25-48. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=0）


![image](images/9cb3e2743f73.jpg)



图 25-49. PCM 标准长帧同步模式时序图（DTLEN=00, CHLEN=1, CKPL=1）


![image](images/2d78b796eb46.jpg)


## 25.9.2. I2S 时钟


图 25-50. I2S 时钟生成结构框图


![image](images/4ecd9f22e6f5.jpg)



I2S 时钟生成器如图25-50. I2S 时钟生成结构框图所示。I2S 接口时钟是通过 SPI_I2SPSC 寄存器的 DIV 位，OF 位和 MCKOEN 位以及 SPI_I2SCTL 寄存器的 CHLEN 位来配置的。I2S比特率可以通过表25-7. I2S 比特率计算公式所示的公式计算。



表 25-7. I2S 比特率计算公式


<table><tr><td>MCKOEN</td><td>CHLEN</td><td>公式</td></tr><tr><td>0</td><td>0</td><td>I2SCLK / (DIV * 2 + OF)</td></tr><tr><td>0</td><td>1</td><td>I2SCLK / (DIV * 2 + OF)</td></tr><tr><td>1</td><td>0</td><td>I2SCLK / (8 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>1</td><td>I2SCLK / (4 * (DIV * 2 + OF))</td></tr></table>


音频采样率(Fs)和 I2S比特率的关系由如下公式定义：


Fs = I2S 比特率 / (通道长度 * 通道数)

所以，为了得到期望的音频采样率，时钟生成器需要按表25-8. 音频采样频率计算公式所列的公式进行配置。


表 25-8. 音频采样频率计算公式


<table><tr><td>MCKOEN</td><td>CHLEN</td><td>公式</td></tr><tr><td>0</td><td>0</td><td>I2SCLK / (32 * (DIV * 2 + OF))</td></tr><tr><td>0</td><td>1</td><td>I2SCLK / (64 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>0</td><td>I2SCLK / (256 * (DIV * 2 + OF))</td></tr><tr><td>1</td><td>1</td><td>I2SCLK / (256 * (DIV * 2 + OF))</td></tr></table>

I2S时钟源可以由 PLLI2S 或外部 I2S_CKIN 引脚提供，在 RCU 模块进行配置。软件需要仔细计算 I2S 分频因子和 PLLI2S 以得到精确的音频采样频率。如果 PLLI2S 精度不能满足应用程序的要求，可以通过 I2S_CKIN 引脚提供精确的外部 I2S 时钟。

注意：I2S串行时钟的配置值需设置为低于 PCLK时钟的 1/6 倍以下(不包含 1/6)。

## 25.9.3. 运行

## 运行模式

运行模式是通过SPLJ2SCTL 寄存器的I2SOPMOD位来选择的.共有四种运行模式可供选择：主机发送模式，主机接收模式，从机发送模式和从机接收模式。各种运行模式下 I2S 接口信号的方向如表25-9. 各种运行模式下I2S接口信号的方向所示。


表 25-9. 各种运行模式下 I2S接口信号的方向


<table><tr><td>运行模式</td><td>I2S_MCK</td><td>I2S_CK</td><td>I2S_WS</td><td>I2S_SD</td><td>I2S_ADD_SD(2)</td></tr><tr><td>主机发送</td><td>输出或 NU(1)</td><td>输出</td><td>输出</td><td>输出</td><td>NU(1)</td></tr><tr><td>主机接收</td><td>输出或 NU(1)</td><td>输出</td><td>输出</td><td>输入</td><td>NU(1)</td></tr><tr><td>从机发送</td><td>输入或 NU(1)</td><td>输入</td><td>输入</td><td>输出</td><td>NU(1)</td></tr><tr><td>从机接收</td><td>输入或 NU(1)</td><td>输入</td><td>输入</td><td>输入</td><td>NU(1)</td></tr><tr><td>全双工</td><td>输出或 NU(1)</td><td>输出</td><td>输出</td><td>输出或输入</td><td>输入或输出</td></tr></table>

1. NU表示该引脚没有被I2S使用，可以用于其他功能。

2. I2S1和I2S2为了支持全双工运行模式，需要两个额外的片上I2S模块：I2S_ADD1和I2S_ADD2。I2S_ADD_SD引脚是I2S_ADD模块的数据引脚，在后面的章节将详细介绍全

双工模式。

## I2S初始化流程

I2S初始化过程包括以下五个步骤。如果要初始化 I2S 工作在主机模式，五个步骤都要执行。如果要初始化 I2S 工作在从机模式，只需要执行步骤 2、3、4、5。

■ 步骤1：配置SPI_I2SPSC寄存器的DIV[7:0]位，OF位和MCKOEN位，定义I2S的比特率和选择是否需要提供I2S_MCK信号。

- 步骤2：配置SPI_I2SCTL寄存器的CKPL位，定义空闲状态的时钟极性。

步 骤 3 ： 配 置 SPI_I2SCTL 寄 存 器 的 I2SSEL 位 ， I2SSTD[1:0] 位 ， PCMSMOD 位 ，I2SOPMOD[1:0]位，DTLEN[1:0]位和CHLEN位，定义I2S的特性。

- 步骤4：配置SPI_CTL1寄存器的TBEIE位，RBNEIE位，ERRIE位，DMATEN位和DMAREN位，选择中断源和DMA功能。此步骤可选。

- 步骤5：将SPI_I2SCTL寄存器的I2SEN位置1，来启动I2S。

## I2S主机发送流程

TBE 标志位被用来控制发送流程。如前文所述，TBE 标志位表示发送缓冲区空，此时，如果SPI_CTL1 寄存器的 TBEIE 位为 1，将产生中断。首先，发送缓冲区为空(TBE 为 1)，且移位寄存器中没有发送序列。当 16 位数据被写入 SPI_DATA 寄存器时(TBE 变为 0)，数据立即从发送缓冲区装载到移位寄存器中(TBE 变为 1)。此时，发送序列开始。

数据是并行地装载到 16 位移位寄存器中的，然后串行地从 I2S_SD 引脚发出（高位先发）。下一个数据应该在 TBE为 1 时写入 SPI_DATA 寄存器。数据写入 SPI_DATA 寄存器之后，TBE变为 0。当前发送序列结束时，发送缓冲区的数据会自动装载到移位寄存器中，然后 TBE标志变回 1。为了保证连续的音频数据发送，下一个将要发送的数据必须在当前发送序列结束之前写入 SPI_DATA 寄存器。

对于除 PCM 标准外的所有标准，I2SCH 标志用来区别当前传输数据所属的通道。I2SCH 标志在每次 TBE标志由 0 变 1 的时候更新。刚开始 I2SCH 标志为 0，表示左通道的数据应该被写入 SPI_DATA 寄存器。

为了关闭 I2S，I2SEN 位必须在 TBE标志为 1 且 TRANS标志为 0 之后清零。

## I2S主机接收流程

RBNE 标志被用来控制接收序列。如前文所述，RBNE 标志表示接收缓冲区非空，如果SPI_CTL1 寄存器的 RBNEIE 位为 1，将产生中断。当 SPI_I2SCTL 寄存器的 I2SEN 位被置 1时，接收流程立即开始。首先，接收缓冲区为空(RBNE 为 0)。当一个接收流程结束时，接收到的数据将从移位寄存器装载到接收缓冲区(RBNE 变为 1)。当 RBNE 为 1 时，用户应该将数据从 SPI_DATA 寄存器中读走。读操作完成后，RBNE 变为 0。必须在下一次接收结束之前读走 SPI_DATA 寄存器中的数据，否则将发生接收过载错误。发送接收过载错误时，RXORERR标志位会被置 1，如果 SPI_CTL1 寄存器的 ERRIE 位为 1，将会产生中断。这种情况下，必须先关闭 I2S 再打开 I2S，然后再恢复通讯。

对于除 PCM 之外的所有标准来说，I2SCH 标志用来区分当前传输数据所属的通道。I2SCH 标志在每次 RBNE 标志由 0 变 1 时更新。

为了关闭 I2S，不同的音频标准，数据长度和通道长度采用不同的操作步骤。每种情况的操作步骤如下所示。

- 数据长度为16位，通道长度为32位，LSB对齐标准（DTLEN = 00，CHLEN = 1，且I2SSTD= 0b10）：

1. 等待倒数第二个RBNE；

2. 等待17个I2S时钟周期（I2S_CK引脚上的时钟）；

3. 清除I2SEN位。

- 数据长度为16位，通道长度为32位，除LSB对齐标准之外的其他标准（DTLEN = 00，CHLEN = 1，且 I2SSTD不等于0b10）：

1. 等待最后一个RBNE；

2. 等待1个I2S时钟周期；

3. 清除I2SEN位。

- 其他所有情况：

1. 等待倒数第二个RBNE；

2. 等待1个I2S时钟周期；

3. 清除I2SEN位。

## I2S从机发送流程

从机发送流程和主机发送流程相似，不同之处如下：

在从机模式下，从机需要在外部主机开始通讯之前使能。当外部主机开始发送时钟信号且I2S_WS 信号请求传输数据时，发送流程开始。数据需要在外部主机发起通讯之前写入SPI_DATA寄存器。为了确保音频数据的连续传输，必须在当前发送序列结束之前将下一个待发送的数据写入 SPI_DATA 寄存器，否则会产生发送欠载错误。此时 TXURERR 标志会置 1，如果 SPI_CTL1 寄存器的 ERRIE 位为 1，将会产生中断。这种情况下，必须先关闭 I2S 再打开 I2S来恢复通讯。从机模式下，I2SCH 标志是根据外部主机发送的 I2S_WS 信号而变化的。

为了关闭 I2S，必须在 TBE 标志变为 1 且 TRANS 标志变为 0 之后，才能清除 I2SEN 位。

## I2S从机接收流程

从机接收流程与主机接收流程类似。不同之处如下。

在从机模式下，从机需要在外部主机开始通讯之前使能。当外部主机开始发送时钟信号且I2S_WS信号指示数据开始时，接收流程开始。从机模式下，I2SCH 标志是根据外部主机发送的 I2S_WS 信号而变化的。

为了关闭 I2S，必须在收到最后一个 RBNE 之后立即清除 I2SEN 位。

## I2S全双工模式

单个的 I2S 模块只支持单向传输：发送模式或接收模式，通过一个附加的 I2S模块（I2S_ADD模块）可以实现 I2S 的全双工模式。I2S_ADD 模块与 I2S模块功能一样，但只工作在从模式。一共有两个 I2S_ADD 模块：I2S_ADD1 和 I2S_ADD2，所以只有 I2S1 和 I2S2 支持全双工模式。I2S_ADD 模块的 I2S_CK 和 I2S_WS 引脚分别与对应的 I2S 模块的相应引脚内部连接，

I2S_ADD 模块的 I2S_SD 引脚映射到对应的 I2S 模块的 SPI_MISO 引脚。

为了工作在全双工模式，需要使能 I2S 模块和相应的 I2S_ADD 模块，I2S 模块支持两种全双工模式：主机模式和从机模式。

在主机全双工模式下，软件必须设置 I2S为主机，I2S_ADD 为从机，I2S_ADD 模块的WS和SCK 信号都由主机 I2S模块提供。

在从机全双工模式下，软件必须设置 I2S和 I2S_ADD 都为从机，I2S 模块和 I2S_ADD 模块的WS和 SCK信号都由外部信号提供。

应用程序可以配置 I2S 模块为发送或接收模式，然后配置 I2S_ADD 为相反的模式。在发送过程中，软件同时操作 I2S 模块和 I2S_ADD 模块的寄存器和中断来实现全双工模式发送。

## 25.9.4. DMA 功能

DMA功能与 SPI 模式完全一样，唯一不同的地方就是 I2S模式不支持 CRC 功能。

## 25.10. I2S 中断

## 25.10.1. 状态标志位

SPI_STAT 寄存器中有 4 个可用的标志位，分别是 TBE、RBNE、TRANS 和 I2SCH，用户通过这些标志位可以全面监视 I2S总线的状态。

- 发送缓冲区空标志（TBE）

当发送缓冲区为空时，TBE置位。软件可以通过写SPI_DATA寄存器将下一个数据写入发送缓冲区。

- 接收缓冲区非空标志（RBNE）

接收缓冲区非空时，RBNE置位，表示此时接收到一个数据，并已存入接收缓冲区中，软件可以通过读SPI_DATA寄存器来读取此数据。

- I2S通信进行中标志（TRANS）

是用来指示当前传输是否正在进行或结束的状态标志，它由内部硬件置位和清除，无法通过软件进行操作。该标志位不会产生如何中断。

- I2S通道标志（I2SCH）

I2SCH用来表明当前传输数据的通道信息，对PCM音频标准来说没有意义。在发送模式下，I2SCH标志在每次TBE由0变1时更新，在接收模式下，I2SCH标志在每次RBNE由0变1时更新。该标志位不会产生任何中断。

## 25.10.2. 错误标志

有三个错误标志：

- 发送欠载错误标志（TXURERR）

在从发送模式下，当有效的SCK信号开始发送时，如果发送缓冲区为空时，发送欠载错误标志TXURERR将会置位。

- 接收过载错误标志（RXORERR）

当接收缓冲区已满且又接收到一个新的数据时，接收过载错误标志RXORERR置位。当接收过载发生时，接收缓冲区中的数据没有更新，新接收的数据丢失。

- 帧错误（FERR）

在从I2S模式下，I2S模块监视I2S_WS信号，如果I2S_WS信号在一个错误的位置发生翻转，将会置位FERR帧错误标志位。

25-10. I2S 总结了 I2S中断事件和相应的使能位。


表 25-10. I2S 中断


<table><tr><td>中断事件</td><td>描述</td><td>清除方式</td><td>中断使能位</td></tr><tr><td>TBE</td><td>发送缓冲区空</td><td>写 SPI_DATA 寄存器</td><td>TBEIE</td></tr><tr><td>RBNE</td><td>接收缓冲区非空</td><td>读 SPI_DATA 寄存器</td><td>RBNEIE</td></tr><tr><td>TXURERR</td><td>发送欠载错误</td><td>读 SPI_STAT 寄存器</td><td rowspan="3">ERRIE</td></tr><tr><td>RXORERR</td><td>接收过载错误</td><td>读 SPI_DATA 寄存器,然后再读 SPI_STAT 寄存器</td></tr><tr><td>FERR</td><td>I2S 帧错误</td><td>读 SPI_STAT 寄存器</td></tr></table>
