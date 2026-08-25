## 20. 通用同步异步收发器（USART）

## 20.1. 通用同步异步收发器（USARTx, x=0..4）

## 20.1.1. 简介

通用同步异步收发器（USART）提供了一个灵活方便的串行数据交换接口，数据帧可以通过全双工或半双工，同步或异步的方式进行传输。USART 提供了可编程的波特率发生器，能对UCLK（PCLK1，PCLK2）进行分频产生 USART 发送和接收所需的特定频率。

USART 不仅支持标准的异步收发模式，还实现了一些其他类型的串行数据交换模式，如红外编码规范，SIR，智能卡协议，LIN，以及同步单双工模式。它还支持多处理器通信和 Modem流控操作（CTS/RTS）。数据帧支持从 LSB 或者 MSB 开始传输。数据位的极性和 TX/RX 引脚都可以灵活配置。

USARTx（x = 0, 1, 2）和 UART3 支持 DMA 功能，以实现高速率的数据通信。UART4 不支持DMA 功能。

## 20.1.2. 主要特性

 NRZ标准格式（Mark/Space）；

 全双工异步通信；

 半双工单线通信；

 可编程的波特率产生器：

由外设时钟分频产生，其中USART0由PCLK2分频得到，USART1/2和UART3/4由PCLK1分频得到；

8或16倍过采样；

当时钟频率为180M，过采样为8，最高速度可到22.5MBits/s；

 完全可编程的串口特性：

– 偶校验位，奇校验位，无校验位的生成/检测；

– 数据位（8或9位）；

– 产生0.5，1，1.5或者2个停止位；

 发送器和接收器可分别使能；

 支持硬件Modem流控操作（CTS/RTS）；

 DMA访问数据缓冲区；

 LIN断开帧的产生和检测；

 支持红外数据协议（IrDA）；

 同步传输模式以及为同步传输输出发送时钟；

 支持兼容ISO7816-3的智能卡接口：

– 字节模式（T=0）；

块模式（T=1）；

– 直接和反向转换；

 多处理器通信：

– 如果地址不匹配，则进入静默模式；

通过线路空闲检测或者地址匹配检测从静默模式唤醒；

 多种状态标志：

传输检测标志：接收缓冲区不为空（RBNE），发送缓冲区为空（TBE），传输完成（TC），忙（BSY）；

错误检测标志：过载错误（ORERR），噪声错误（NERR），帧格式错误（FERR），奇偶校验错误（PERR）；

硬件流控操作标志：CTS变化（CTSF）；

LIN模式标志：LIN断开检测（LBDF）；

多处理器通信模式标志：IDLE帧检测（IDLEF）；

智能卡模式标志：块结束（EBF）和接收超时（RTF）；

– 若相应的中断使能，这些事件发生将会触发中断。

USART0/1/2完全实现上述功能，但是UART3/4只实现了上面所介绍功能的部分，下面这些功能在UART3/4中没有实现：

 智能卡模式；

 同步模式；

 硬件流操作（CTS/RTS）；

 设置数据极性。

## 20.1.3. 功能描述

USART 接口通过 20-1. USART 中主要引脚从外部连接到其他设备。


表 20-1. USART 重要引脚描述


<table><tr><td>引脚</td><td>类型</td><td>描述</td></tr><tr><td>RX</td><td>输入</td><td>接收数据</td></tr><tr><td>TX</td><td>输出I/O(单线模式/智能卡模式)</td><td>发送数据。当USART使能后,若无数据发送,默认为高电平</td></tr><tr><td>CK</td><td>输出</td><td>用于同步通信的串行时钟信号</td></tr><tr><td>nCTS</td><td>输入</td><td>硬件流控模式发送使能信号</td></tr><tr><td>nRTS</td><td>输出</td><td>硬件流控模式发送请求信号</td></tr></table>


图 20-1. USART 模块内部框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/d6034feabff89306626b86eb49c59c15cfb9c9d14a19b6c5f546d0ca82e6a72b.jpg)


## USART 帧格式

USART 数据帧开始于起始位，结束于停止位。USART_CTL0 寄存器中WL 位可以设置数据长度。将 USART_CTL0 寄存器中 PCEN 置位，最后一个数据位可以用作校验位。若 WL 位为0，第七位为校验位。若WL 位置 1，第八位为校验位。USART_CTL0 寄存器中 PM 位用于选择校验位的计算方法。


图 20-2. USART 字符帧 （8 数据位和 1 停止位）


<table><tr><td colspan="10">时钟</td></tr><tr><td rowspan="2">起始位</td><td colspan="6">数据帧</td><td colspan="3">或校验位</td></tr><tr><td>bit0</td><td>bit1</td><td>bit2</td><td>bit3</td><td>bit4</td><td>bit5</td><td>bit6</td><td>bit7</td><td>Stop</td></tr><tr><td rowspan="2"></td><td colspan="9">空闲帧</td></tr><tr><td colspan="9">断开帧</td></tr></table>

在发送和接收中，停止位可以由 USART_CTL1 寄存器中 STB[1:0]位域配置。


表 20-2. 停止位配置


<table><tr><td>STB[1:0]</td><td>停止位长度(位)</td><td>功能描述</td></tr><tr><td>00</td><td>1</td><td>默认值</td></tr><tr><td>01</td><td>0.5</td><td>智能卡模式接收</td></tr><tr><td>10</td><td>2</td><td>标准 USART 和单线模式</td></tr><tr><td>11</td><td>1.5</td><td>智能卡模式发送和接收</td></tr></table>

在一个空闲帧中，所有位都为 1。数据帧长度与正常 USART 数据帧长度相同。

紧随停止位后多个低电平为中断帧。USART 数据帧的传输速度由 PCLK 时钟频率，波特率发生器的配置，以及过采样模式共同决定。

## 波特率发生

波特率分频系数是一个 16 位的数字，包含 12 位整数部分和 4 位小数部分。波特率发生器使用这两部分组合所得的数值来确定波特率。由于具有小数部分的波特率分频系数，将使 USART能够产生所有标准波特率。

波特率分频系数 （USARTDIV） 与系统时钟 UCLK 具有如下关系：

如果过采样率是 16，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{1 6 \times \text { Baud   Rate }}\tag{20-1}
$$

当过采样率是 8 时，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{8 \times \text { Baud   Rate }}\tag{20-2}
$$

例如，当过采样是 16：

1. 由USART_BAUD寄存器的值得到USARTDIV：

假设 USART_BAUD=0x21D，则 INTDIV=33 （0x21），FRADIV=13 （0xD）。

$$
\mathrm{UASRTDIV} = 3 3 + 1 3 / 1 6 = 3 3. 8 1 。
$$

2. 由USARTDIV得到USART_BAUD寄存器的值：

假设要求 UASRTDIV=30.37，INTDIV=30（0x1E）

$1 6 ^ { \star } 0 . 3 7 { = } 5 . 9 2$ ，接近整数 6，所以 FRADIV=6（0x6）

USART_BAUD=0x1E6。 

注意：若取整后 FRADIV=16（溢出），则进位必须加到整数部分。

## USART 发送器

如果 USART_CTL0 寄存器的发送使能位（TEN）被置位，当发送数据缓冲区不为空时，发送器将会通过 TX 引脚发送数据帧。TX 引脚的极性可以通过 USART_CTL3 寄存器中 TINV位来配置。时钟脉冲通过 CK引脚输出。

TEN 置位后发送器会发出一个空闲帧。TEN 位在数据发送过程中是不可以被复位的。

系统上电后，TBE默认为高电平。在 USART_STAT0寄存器中 TBE 置位时，数据可以在不覆盖前一个数据的情况下写入 USART_DATA 寄存器。当数据写入 USART_DATA 寄存器，TBE位将被清 0。在数据由 USART_DATA 移入移位寄存器后，该位由硬件置 1。如果数据在一个发送过程正在进行时被写入 USART_DATA 寄存器，它将首先被存入发送缓冲区，在当前发送过程完成时传输到发送移位寄存器中。如果数据在写入 USART_DATA 寄存器时，没有发送过程正在进行，TBE位将被清零然后迅速置位，原因是数据将立刻传输到发送移位寄存器。

假如一帧数据已经发送出去，并且 TBE 位已经置位，那么 USART_STAT0 寄存器中 TC 位将被置 1。如果 USART_CTL0 寄存器中的中断使能位（TCIE）为 1，将会产生中断。

20-3. USART 给出了 USART 发送步骤。软件操作按以下流程进行：

1. 在 USART_CTL0 寄存器中置位 UEN 位，使能 USART；

2. 通过 USART_CTL0 寄存器的 WL 设置字长；

3. 在 USART_CTL1 寄存器中写 STB[1:0]位来设置停止位的长度；

4. 如果选择了多级缓存通信方式，应该在 USART_CTL2寄存器中使能 DMA （DENT 位）；

5. 在 USART_BAUD 寄存器中设置波特率；

6. 在 USART_CTL0 寄存器中设置 TEN 位；

7. 等待 TBE 置位；

8. 向 USART_DATA 寄存器写数据；

9. 若 DMA 未使能，每发送一个字节都需重复步骤 7-8；

10. 等待 TC=1，发送完成。


图 20-3. USART 发送步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/8be1bb0a81c32719dc6ce96ffa453bfb130b33f917688593f59b9519b2713764.jpg)



在禁用 USART 或进入低功耗状态之前，必须等待 TC 置位。先读 USART_STAT0 然后再写USART_DATA 可将 TC 位清 0。在多级缓存通信方式（DENT=1）下，直接向 TC 写 0，也能清 TC。


## USART 接收器

上电后，USART 接收器使能按以下步骤进行：

1. 在USART_CTL0寄存器中置位UEN位，使能USART；

2. 写USART_CTL0寄存器的WL去设置字长；

3. 在USART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

4. 如果选择了多级缓存通信方式，应该在USART_CTL2寄存器中使能DMA（DENR位）；

5. 在USART_BAUD寄存器中设置波特率；

6. 在USART_CTL0中设置REN位。

接收器在使能后若检测到一个有效的起始脉冲便开始接收码流。在接收一个数据帧的过程中会检测噪声错误，奇偶校验错误，帧错误和过载错误。

当接收到一个数据帧，USART_STAT0 寄存器中的 RBNE 置位，如果设置了 USART_CTL0 寄存器中相应的中断使能位 RBNEIE，将会产生中断。在 USART_STAT0 寄存器中可以观察接

收状态标志。

软件可以通过读 USART_DATA 寄存器或者 DMA 方式获取接收到的数据。不管是直接读寄存器还是通过 DMA，只要是对 USART_DATA 寄存器的一个读操作都可以清除 RBNE 位。

在接收过程中，需使能 REN 位，不然当前的数据帧将会丢失。

在默认情况下，接收器通过获取三个采样点的值来估计该位的值。如果是 8 倍过采样模式，选择第 3、4、5 个采样点；如果是 16 倍过采样模式，选择第 7、8、9 个采样点。如果在 3 个采样点中有 2 个或 3 个为 0，该数据位被视为 0，否则为 1。如果 3 个采样点中有一个采样点的值与其他两个不同，不管是数据位，奇偶校验位或者停止位，都将产生噪声错误（NERR）。如果使能 DMA，并置位 USART_CTL2 寄存器中 ERRIE，将会产生中断。如果在 USART_CTL2中置位 OSB，接收器将仅获取一个采样点来估计一个数据位的值。在这种情况下将不会检测到噪声错误。


图 20-4. 过采样方式接收一个数据位（OSB=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/bca2034396f330566d3923ee8b086fb3b1f21a2e17c4ca6a0c7fd4dd46b241f5.jpg)


通过置位 USART_CTL0 寄存器中的 PCEN 位使能奇偶校验功能，接收器在接收一个数据帧时计算预期奇偶校验值，并将其与接收到的奇偶校验位进行比较。如果不相等，USART_STAT0寄存器中 PERR 被置位。如果设置了 USART_CTL0 寄存器中的 PERRIE 位，将产生中断。

如果在停止位传输过程中 RX 引脚为 0，将产生帧错误，USART_STAT0 寄存器中 FERR 置位。如果使能 DMA并置位 USART_CTL2 寄存器中 ERRIE位，将产生中断。

当接收到一帧数据，而 RBNE 位还没有被清零，随后的数据帧将不会存储在数据接收缓冲区中。USART_STAT0 寄存器中的溢出错误标志位 ORERR 将置位。如果使能 DMA 并置位USART_CTL2 寄存器中 ERRIE 位或者置位 RBNEIE，将产生中断。

若接收过程中，产生了噪声错误（NERR）、校验错误（PERR）、帧错误（FERR）或溢出错误（ORERR），则 NERR、PERR、FERR 或 ORERR 将和 RBNE 同时置位。如果没有使能 DMA，RBNE 中断发生时，软件需检查是否有噪声错误、校验错误、帧错误或溢出错误产生。

## DMA方式访问数据缓冲区

为减轻处理器的负担，可以采用 DMA 访问发送缓冲区或者接收缓冲区。置位 USART_CTL2寄存器中DENT 位可以使能DMA 发送，置位 USART_CTL2寄存器中 DENR位可以使能 DMA接收。

当 DMA 用于 USART 发送时，DMA 将数据从片内 SRAM 传送到 USART 的数据缓冲区。配

置步骤如 20-5. DMA USART 所示。


图 20-5. 采用 DMA方式实现 USART 数据发送配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/0d1ba3fb6a0e2366d4405722a7606877a00750dd3b38b943ef53f1645263b06c.jpg)


所有数据帧都传输完成后，USART_STAT0 寄存器中 TC 位置 1。如果 USART_CTL0 寄存器中 TCIE置位，将产生中断。

当 DMA 用于 USART 接收时，DMA 将数据从接收缓冲区传送到片内 SRAM。配置步骤如20-6. DMA USART 所示。如果将 USART_CTL2 寄存器中ERRIE 位置 1，USART_STAT0 寄存器中的错误标志位（FERR、ORERR 和 NERR）被置位时将产生中断。


图 20-6. 采用 DMA方式实现 USART 数据接收配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/68568c69b31e9bb7eb97c38b17c67f2f4e612aa64e045267f8229ad5827ded9b.jpg)



当 USART 接收到的数据数量达到了 DMA 传输数据数量，DMA模块将产生传输完成中断。


## 硬件流控制

硬件流控制功能通过 nCTS 和 nRTS引脚来实现。通过将 USART_CTL2 寄存器中 RTSEN 位置 1 来使能 RTS 流控，将 USART_CTL2 寄存器中 CTSEN 位置 1 来使能 CTS 流控。


图 20-7. 两个 USART 之间的硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/f352f3208f0c4ca8da0da132676a9e3c277b063ac2782146a31f9a8f95105c52.jpg)


## RTS 流控

USART 接收器输出 nRTS，它用于反映接收缓冲区状态。当一帧数据接收完成，nRTS变成高电平，这样是为了阻止发送器继续发送下一帧数据。当接收缓冲区满时，nRTS 保持高电平，可以通过读 USART_DATA寄存器来清零。

## CTS 流控

USART 发送器监视 nCTS输入引脚来决定数据帧是否可以发送。如果 USART_STAT0 寄存器中 TBE 位是 0 且 nCTS 为低电平，发送器发送数据帧。在发送期间，若 nCTS 信号变为高电平，发送器将会在当前数据帧发送完成后停止发送。


图 20-8. 硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/cd963c7c87a37be99f6f115bda6e780791a209ae020d10225939d411b46a90b7.jpg)



如果 CTS 流控制被使能，在 nCTS引脚信号发生变化时，USART_STAT0 寄存器中 CTSF 位会置 1。如果 USART_CTL2 寄存器中的 CTSIE位被置位，将会产生中断。


## 多处理器通信

在多处理器通信中，多个 USART 被连接成一个网络。对于一个设备来说，监视所有来自 RX引脚的消息，是一种巨大的负担。为减轻设备负担，软件可以通过将 USART_CTL0 寄存器中RWU 位置 1 使一个 USART 进入静默模式。

如果 USART 处于静默模式，所有的接收状态标志位将不会被置位。软件可以通过对 RWU 清零来唤醒 USART。

此外，USART 可以由硬件用以下两种方式中的一种来唤醒：空闲总线检测和地址匹配检测。

设备默认使用空闲总线检测方法唤醒 USART。当在 RX 引脚检测到空闲帧时，硬件会将 RWU清零，从而退出静默模式，但 USART_STAT0 寄存器中 IDLEF 位不会被置 1。

当 USART_CTL0 寄存器中 WM被置位，数据最高位会被认为是地址标志位。如果地址标志位为1，该字节被认为是地址字节。如果地址字节的低4位与USART_CTL1寄存器中的ADDR[3:0]相同，硬件会将 RWU 清零，并退出静默模式。接收到将 USART 唤醒的数据帧，RBNE 将置位。状态标志可以从 USART_STAT0 寄存器中获取。如果地址字节的低 4 位与 USART_CTL1寄存器中的 ADDR[3:0]不相同，硬件会置位 RWU 并进入静默模式。在这种情况下，RBNE 不会被置位。

如果采用地址掩码检测，默认情况下，接收器对地址字节不做奇偶校验。如果 USART_CHC 寄存器中 PCEN 位被置位，地址字节最高位被视为校验位，其余位被视为地址。

## LIN 模式

将 USART_CTL1 寄存器的 LMEN 置位即可使能本地互联网络模式。

在 LIN 模式下，USART_CTL1 寄存器中 CKEN，WL，STB[1:0]以及 USART_CTL2 的 SCEN，HDEN，IREN 位都应该被清 0。

在发送一个普通数据帧时，LIN 发送过程与普通发送过程相同。当 USART_CTL0 寄存器中SBKCMD 置位时，USART 在发送完一个停止位后会连续发送 13 个 0。

断开检测功能完全独立于普通 USART 接收器。因此，断开检测可以是在空闲状态下，也可以在数据传输过程中。USART_CTL1 寄存器中 LBLEN 位可以选择断开帧长度。如果在 RX 引脚检测到大于或等于与预期断开帧长度相等数量的 0（LBLEN=0 时，10 个 0；LBLEN=1 时，11个 0），USART_STAT0 寄存器中 LBDF 置位。如果 USART_CTL1 寄存器中 LBDIE 被置位，将产生中断。

如 20-9. 所示，如果断开帧发生在空闲状态下，USART 接收器会接收到一个全 0 数据帧，同时 FERR 置位。


图 20-9. 空闲状态下检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/160d51fb2ac0888cc230e3e9910d448a601dc3e8ff3c017df14d819ffd33700b.jpg)


如 20-10. 所示，如果断开帧发生在数据传输过程中，当前传输帧发生错误，FERR 置位。


图 20-10. 数据传输过程中检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/46022ed331b7e0b970f8c727f3ae6a26a2fec5efd7cfa14aba9c436d2d709310.jpg)


## 同步通信模式

USART 支持主机模式下的全双工同步串行通信，可以通过置位 USART_CTL1 的CKEN 位来使能。在同步模式下，USART_CTL1 的 LMEN 和 USART_CTL2 的 SCEN，HDEN，IREN 位应该被清 0。CK引脚作为 USART 同步发送器的时钟输出，仅仅当 TEN 位被使能时，它才被激活。在起始位和停止位传送期间，不会从 CK 引脚输出时钟脉冲。USART_CTL1 的 CLEN位用来决定在最低位（地址索引位）发送期间是否有时钟信号输出。USART_CTL1 的 CPH 位用来决定数据在第一个时钟沿被采样还是在第二个时钟沿被采样。USART_CTL1 的 CPL 位用来决定在 USART 同步模式空闲状态下，时钟引脚的电平。

CK 引脚输出波形由 USART_CTL1 寄存器中 CPL，CPH，CLEN 位决定。软件仅在 USART

禁用（UEN=0）时才可以改变它们的值。

如果USART_CTL0寄存器中REN置位，接收器的工作方式与普通模式下接收方式是不同的。接收器在时钟捕获沿采样数据，并无任何过采样。


图 20-11. 同步模式下的 USART 示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/dc342ffdc97727ebfcdf2f381d106261bcd24f1d66eb4d203b2430f320226954.jpg)



图 20-12. 8-bit 格式的 USART 同步通信波形（CLEN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/cec2b239844f9c07699653c29d3ad0cda90b5f5bef4e9b9bdc6ecc8e7ed7a2ff.jpg)


## 串行红外（IrDA SIR）编解码功能模块

串行红外编解码功能通过置位 USART_CTL2 寄存器中 IREN 使能。在 IrDA 模式下，USART_CTL1 寄存器的 LMEN，STB[1:0]，CKEN 位和 USART_CTL2 寄存器的 HDEN，SCEN位将被清 0。

在 IrDA 模式下，USART 数据帧由 SIR 发送正交译码器进行调制，调制后的信号经由红外 LED进行发送，经解调后将数据发送至USART接收器。对于正交译码器而言，波特率应小于115200。


图 20-13. IrDA SIR ENDEC 模块


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/712ebe29534d6ec1944eba4cf4bfb3d6a31259bb7a9fd8b55037018ebbb75e94.jpg)


在 IrDA 模式下，TX 引脚电平与 RX 引脚不同。TX 引脚通常为低电平，RX 引脚通常为高电平。IrDA 引脚电平保持稳定代表逻辑‘1’，红外光源脉冲（RTZ 信号）代表逻辑‘0’。其脉冲宽度通常占一个位时间的 3/16。IrDA 无法检测到宽度小于一个 1 个 PSC 时钟的脉冲。如果脉冲宽度大于 1 但是小于 2 倍 PSC 时钟，IrDA 则无法可靠的检测到。

由于 IrDA 是一种半双工协议，因此在 IrDA SIR ENDEC 模块中，发送和接收不得同时进行。


图 20-14. IrDA 数据调制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/b0b4d9c27c9d74c93f04355e91a232dad8545ca406e8dc23ec76c7119bd54090.jpg)


将 USART_CTL2 寄存器中 IRLP置位可以使 SIR 子模块工作在低功耗模式下。发送编码器由PCLK 分频得到的低速时钟来驱动。分频系数在 USART_GP 寄存器中 PSC[7:0]位配置，USART_BAUD寄存器需配置为16*PSC[7:0]。TX引脚脉冲宽度可以为低功耗波特率的 3倍。接收器解码器工作模式与正常 IrDA 模式相同。

## 半双工通信模式

通过设置 USART_CTL2 寄存器的 HDEN 位，可以使能半双工模式。

在半双工通信模式下，USART_CTL1 寄存器的 LMEN，CKEN 位和 USART_CTL2 寄存器的SCEN，IREN 位清零。

半双工模式下仅用单线通信，TX 引脚和 RX 引脚从内部连接到一起，RX 引脚不再使用。TX

有校验错误的ISO7816-3帧

引脚应被配置为开漏模式，通信冲突由软件处理。

在某些应用程序中可以启用冲突检测，例如多个发送设备所共享的一条数据线上的数据传输。通过将 USART_GDCTL 寄存器中的 CDEN 位置 1 使能该功能。当 txd 线上发生数据冲突时，CD 位置 1，如果 CDIE位置 1，将会产生中断。

## 智能卡（ISO7816-3）模式

智能卡模式是一种异步通信模式，支持ISO7816-3协议。支持字节模式（T=0）和块模式（T=1）。将 USART_CTL2 寄存器的 SCEN 位置 1，即可使能智能卡模式。在智能卡模式下，USART_CTL1 寄存器的 LMEN 位和 USART_CTL2 的 HDEN，IREN 位应该清 0。

如果 CKEN 位被置位，USART 通过 CK 引脚向智能卡提供一个由 PCLK分频得到的时钟。分频系数可在 USART_GP 寄存器中 PSC[4:0]配置。CK 引脚只为智能卡提供时钟源。

智能卡模式是一种半双工通信协议模式。当与智能卡连接时，TX 引脚需要被设置成开漏模式，外接上拉电阻，这个引脚将会与智能卡驱动同一条双向连线。智能卡模式下的帧格式为：1 起始位+9 数据位（包括 1 奇偶校验位）+1.5 停止位。其中 0.5 个停止位被配置为接收器的停止位。


图 20-15. ISO7816-3 数据帧格式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/4f1642905bd34421db229daeb7daf608b6670e49615746101569a9221f7b8321.jpg)


## 字节模式（T=0）

相较于正常操作模式下的时序，从发送移位寄存器到 TX 引脚的传递时间延迟了半个波特率时钟，并且 TC 标志的置位将根据 USART_GP 寄存器的 GUAT[7:0]设置延迟某一特定时间。在智能卡模式下，在最后一帧数据的停止位之后，内部保护时间计数器将开始计数，GUAT[7:0]的值配置为 ISO7816-3 协议的 CGT 减 12。在保护时间寄存器向上计数这段时间 TC 将被强制拉低，当计数达到设定值时，TC 被置位。

在 USART 发送期间，如果检测到有奇偶校验错误，TX 引脚在停止位最后一个位时间内被拉低，智能卡发送一个 NACK 信号。根据协议，USART 会自动重发 SCRTNUM 次。在重发数据帧前面会插入 2 位的帧间隔。最后一次重发字节后，TC 会立即被置位。如果在最大重发次数后仍然收到 NACK 信号，USART 将会停止发送，帧错误标志被置位。USART 不会将 NACK信号作为起始位。

在 USART 接收期间，如果在当前数据帧检测到校验错误，TX 引脚在停止位的最后一个位时间内会被拉低。智能卡会接收到 NACK 信号。然后在智能卡端会产生一个帧错误。如果接收到的字节是错误的，RBNE 中断和接收 DMA 请求都不会被激活。根据协议，智能卡将要重新发送数据。如果在最大的重新发送次数后（这个次数的具体值在 SCRTNUM 位域），接收到的字符仍然是错误的，USART 停止发送 NACK 信号和标注这个错误为奇偶校验错误。将

USART_CTL2 寄存器中的 NKEN 置位可以使能 NACK 信号。

空闲帧和断开帧在智能卡模式下不适用。

## 块模式（T=1）

在 T=1（块模式）下，USART_CTL2 寄存器的 NKEN 位应该清零来关闭校验错误发送。

当要从智能卡读取数据时，软件必须将 USART_RT 寄存器设置成 BWT （块等待）-11 的值并将 置位。这个超时时间体现在波特时间单元。如果这个时间到了，还没有从智能卡收到应答，USART_STAT1 寄存器中 RTF 位被置位。如果设置了 USART_CTL3 寄存器中 RTIE位，将会产生中断。如果在超时之前收到了第一个字节，则会引起 RBNE 中断。如果用 DMA从智能卡读取数据，也只能在第一个字节接收好后再去使能 DMA。

第一个字节接收到后，RT[23:0]的值设置成 CWT（字节等待时间）-11 来使能两个连续字节间最大帧间隔自动校验。如果在 RT[23:0]周期内智能卡停止发送字节，USART_STAT1 寄存器中RTF 将被置位。

USART 用一个块长度计数器统计收到的字节数，这个计数器在 USART 开始发送的时候自动清 0（TBE=0）。这个块长度信息位于智能卡发出数据的第三个字节（序言部分），这个值必须写入 USART_RT 寄存器 BL[7:0]。块长度计数器从 0 开始计数到最大值 BL[7:0]+4。在块计数器计数到最大值时，USART_STAT1 寄存器中块结束状态标志位 EBF 置位。如果设置了USART_CTL3 寄存器中的 EBIE位，将会产生中断。如果块长度发生错误，RTF 置位。

当使用 DMA 模式接收时，在块开始之前，这个寄存器必须被设定为最小值（0x0）。为了得到这个值，在收到第四个字节后，会引起一个中断。软件可以从接收缓冲区读取第三个字节作为块长度。

如果接收时不使用DMA方式，为避免产生EBF状态标志，BL[7:0]需首先配置为最大值0xFF。在收到第三个字节后，真正的块长度值可以重新写入到 BL[7:0]。

## 直接和反向转换

智能卡协议定义了两种转换方式：直接转换和反向转换。

如果选择直接转换，从数据帧的最低位开始传输，TX 引脚高电平代表逻辑‘1’，偶校验。在这种情况下，USART_CTL3 寄存器中 MSBF 位和 DINV 位都为 0（默认值）。

如果选择反向转换，从数据帧的最高位开始传输，TX 引脚高电平代表逻辑‘0’，偶校验。在这种情况下，USART_CTL3 寄存器中 MSBF 位和 DINV 位都为 1。

## USART 中断

USART 中断事件和标志如 20-3. USART 所示：


表 20-3. USART 中断请求


<table><tr><td>中断事件</td><td>事件标志</td><td>控制寄存器</td><td>使能控制位</td></tr><tr><td>发送数据寄存器空</td><td>TBE</td><td>USART_CTL0</td><td>TBEIE</td></tr><tr><td>CTS 标志</td><td>CTSF</td><td>USART_CTL2</td><td>CTSIE</td></tr><tr><td>发送结束</td><td>TC</td><td>USART_CTL0</td><td>TCIE</td></tr><tr><td>接收到的数据可以读取</td><td>RBNE</td><td rowspan="2">USART_CTL0</td><td rowspan="2">RBNEIE</td></tr><tr><td>检测到过载错误</td><td>ORERR</td></tr><tr><td>检测到线路空闲</td><td>IDLEF</td><td>USART_CTL0</td><td>IDLEIE</td></tr><tr><td>奇偶校验错误</td><td>PERR</td><td>USART_CTL0</td><td>PERRIE</td></tr><tr><td>LIN 模式下,检测到断开标志</td><td>LBDF</td><td>USART_CTL1</td><td>LBDIE</td></tr><tr><td>接收超时错误</td><td>RTF</td><td>USART_CTL3</td><td>RTIE</td></tr><tr><td>发现块尾</td><td>EBF</td><td>USART_CTL3</td><td>EBIE</td></tr><tr><td>当 DMA 接收使能时,接收错误(噪声错误、溢出错误、帧错误)</td><td>NERR 或 ORERR 或 FERR</td><td>USART_CTL2</td><td>ERRIE</td></tr><tr><td>检测到冲突</td><td>CD</td><td>USART_GDCTL</td><td>CDIE</td></tr></table>


在发送给中断控制器之前，所有的中断事件是逻辑或的关系。因此在任何时候 USART 只能向控制器产生一个中断请求。不过软件可以在一个中断服务程序里处理多个中断事件。



图 20-16. USART 中断映射框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/789f2b3722b94df7c6fc54f01531ba3a52847b1e1c8bffb4731674364d80f5cc.jpg)


## 20.2. 通用同步异步收发器（USARTx, x=5）

## 20.2.1 . 简介

通用同步/异步收发器（USART）提供了一个灵活方便的串行数据交换接口。数据帧可以通过全双工或半双工，同步或异步的方式进行传输。USART 提供了可编程的波特率发生器，能对UCLK（PCLK2、CK_USART5）进行分频产生 USART 发送和接收所需的特定频率。

USART 不仅支持标准的异步收发模式，还实现了一些其他类型的串行数据交换模式，如红外编码规范，SIR，智能卡模式，LIN，以及同步和单双工模式。它还支持多处理器通信。数据帧支持从 LSB 或者 MSB开始传输。数据位的极性和 TX/RX 引脚都可以灵活配置。

所有 USART 都支持 DMA 功能，以实现高速率的数据通信。

## 20.2.2. 主要特性

- NRZ标准格式
- 全双工异步通信
- 半双工单线通信
- 接收FIFO功能
- 双时钟域：
  - 互为异步关系的APB时钟和USART时钟
  - 不依赖PCLK设置的波特率设置
- 可编程的波特率产生器，当时钟频率为180MHz，过采样为8，最高速度可达22.5MBits/s
- 完全可编程的串口特性：
  - 数据位（8或9位）低位或高位在前
  - 偶校验位，奇校验位，无校验位的生成或检测
  - 产生0.5，1，1.5或者2个停止位
- 可互换的Tx/Rx引脚
- 可配置的数据极性
- 可配置的多级缓存通信DMA访问数据缓冲区
- 发送器和接收器可分别使能
- 奇偶校验位控制：
  - 发送奇偶校验位
  - 检测接收的数据字节的奇偶校验位
- LIN断开帧的产生和检测
- 支持红外数据协议（IrDA）
- 同步传输模式以及为同步传输输出发送时钟
- 支持兼容ISO7816-3的智能卡接口：
  - 字节模式（T=0）
  - 块模式（T=1）
  - 直接和反向转换
- 多处理器通信：
  - 如果地址不匹配，则进入静默模式

通过线路空闲检测或者地址匹配检测从静默模式唤醒

 支持ModBus通信：

– 超时功能

CR/LF字符识别

 从深度睡眠模式，深度睡眠模式1和深度睡眠模式2唤醒：

通过标准的RBNE中断

通过WUF中断

 多种状态标志：

传输检测标志：接收缓冲区不为空（RBNE），接收FIFO满（RFF），发送缓冲区为空（TBE），传输完成（TC）

错误检测标志：过载错误（ORERR），噪声错误（NERR），帧格式错误

LIN模式标志：LIN断开检测（LBDF）

多处理器通信模式标志：IDLE帧检测（IDLEF）

ModBus通信标志：地址/字符匹配（AMF），接收超时（RTF）

– 智能卡模式标志：块结束（EBF）和接收超时（RTF）

从深度睡眠模式唤醒标志

– 若相应的中断使能，这些事件发生将会触发中断

## 20.2.3. 功能描述

USART 接口通过 20-4. USART 中主要引脚从外部连接到其他设备。


表 20-4. USART 重要引脚描述


<table><tr><td>引脚</td><td>类型</td><td>描述</td></tr><tr><td>RX</td><td>输入</td><td>接收数据</td></tr><tr><td>TX</td><td>输出I/O(单线模式/智能卡模式)</td><td>发送数据。当USART使能后,若无数据发送,默认为高电平</td></tr><tr><td>CK</td><td>输出</td><td>用于同步通信的串行时钟信号</td></tr></table>


图 20-17. USART 模块内部框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/25b03c648cbccb0cbeda118e190459410f3e3f07033ea24043f954b7466f162f.jpg)


## USART 帧格式

USART 数据帧开始于起始位，结束于停止位。USART_CTL0 寄存器中WL 位可以设置数据长度。将 USART_CTL0 寄存器中 PCEN 置位，最后一个数据位可以用作校验位。若 WL 位为0，第七位为校验位。若WL 位置 1，第八位为校验位。USART_CTL0 寄存器中 PM 位用于选择校验位的计算方法。


图20-18. USART字符帧（8数据位和1停止位）


<table><tr><td colspan="10">时钟</td></tr><tr><td rowspan="2">起始位</td><td colspan="5">数据帧</td><td colspan="4">或校验位</td></tr><tr><td>bit0</td><td>bit1</td><td>bit2</td><td>bit3</td><td>bit4</td><td>bit5</td><td>bit6</td><td>bit7</td><td>Stop</td></tr><tr><td></td><td colspan="9">空闲帧</td></tr><tr><td></td><td colspan="9">断开帧</td></tr></table>

在发送和接收中，停止位可以在 USART_CTL1 寄存器中 STB[1:0]位域中配置。


表 20-5. 停止位配置


<table><tr><td>STB[1:0]</td><td>停止位长度(位)</td><td>功能描述</td></tr><tr><td>00</td><td>1</td><td>默认值</td></tr><tr><td>01</td><td>0.5</td><td>智能卡模式接收</td></tr><tr><td>10</td><td>2</td><td>标准 USART 和单线模式</td></tr><tr><td>11</td><td>1.5</td><td>智能卡模式发送和接收</td></tr></table>

在一个空闲帧中，所有位都为 1。数据帧长度与正常 USART 数据帧长度相同。

紧随停止位后多个低电平为中断帧。USART 数据帧的传输速度由 UCLK时钟频率，波特率发生器的配置，以及过采样模式共同决定。

## 波特率发生

波特率分频系数是一个 16 位的数字，包含 12 位整数部分和 4 位小数部分。波特率发生器使用这两部分组合所得的数值来确定波特率。由于具有小数部分的波特率分频系数，将使 USART能够产生所有标准波特率。

波特率分频系数（USARTDIV）与 UCLK 具有如下关系：

如果过采样率是 16，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{1 6 \times \text { Baud   Rate }}\tag{20-3}
$$

如果过采样是 8，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{8 \times \text { Baud   Rate }}\tag{20-4}
$$

例如，当过采样是16：

1. 由USART_BAUD寄存器的值得到USARTDIV：假设USART_BAUD=0x21D，则INTDIV=33 （0x21），FRADIV=13 （0xD）。UASRTDIV=33+13/16=33.81。

2. 由USARTDIV得到USART_BAUD寄存器的值：

假设要求UASRTDIV=30.37，INTDIV=30 （0x1E）

注意：若取整后FRADIV=16（溢出），则进位必须加到整数部分。

## USART 发送器

如果 USART_CTL0 寄存器的发送使能位（TEN）被置位，当发送数据缓冲区不为空时，发送器将会通过 TX 引脚发送数据帧。TX 引脚的极性可以通过 USART_CTL1 寄存器中 TINV位来配置。时钟脉冲通过 CK引脚输出。

TEN 置位后发送器会发出一个空闲帧。TEN 位在数据发送过程中是不可以被复位的。

系统上电后，TBE 默认为高电平。在 USART_STAT 寄存器中 TBE 置位时，数据可以在不覆盖前一个数据的情况下写入 USART_TDATA 寄存器。当数据写入 USART_TDATA 寄存器，TBE 位将被清 0。在数据由 USART_TDATA 移入移位寄存器后，该位由硬件置 1。如果数据在一个发送过程正在进行时被写入 USART_TDATA 寄存器，它将首先被存入发送缓冲区，在当前发送过程完成时传输到发送移位寄存器中。如果数据在写入 USART_TDATA 寄存器时，没有发送过程正在进行，TBE位将被清零然后迅速置位，原因是数据被立刻传输到发送移位寄存器。

假如一帧数据已经被发送出去，并且 TBE 位已被置位，那么 USART_STAT 寄存器中 TC 位将被置 1。如果 USART_CTL0 寄存器中的中断使能位（TCIE）为 1，将会产生中断。

20-19. USART 给出了 USART 发送步骤。软件操作按以下流程进行：

1. 通过USART_CTL0寄存器的WL设置字长；

2. 在USART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

3. 如果选择了多级缓存通信方式，应该在USART_CTL2寄存器中使能DMA（DENT位）；

4. 在USART_BAUD寄存器中设置波特率；

5. 在USART_CTL0寄存器中置位UEN位，使能USART；

6. 在USART_CTL0寄存器中设置TEN位；

7. 等待TBE置位；

8. 向USART_TDATA寄存器写数据；

9. 若DMA未使能，每发送一个字节都需重复步骤7-8；

10. 等待TC=1，发送完成。


图 20-19. USART 发送步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/19229c7d8a6b906c4ae0dc2d7e7739926c4870a520e9f7ba96d46d52a32dcb59.jpg)



在禁用 USART 或进入低功耗状态之前，必须等待 TC 置位。通过向 USART_INTC 寄存器的TCC 位写 1 可将 TC 位清 0。


当 SBKCMD 置位时，会发送一个断开帧，发送完成后，SBKCMD 将被清 0。

## USART 接收器

上电后，按以下步骤使能USART接收器：

1. 写USART_CTL0寄存器的WL位去设置字长；

2. 在USART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

3. 如果选择了多级缓存通信方式，应该在USART_CTL2寄存器中使能DMA（DENR位）

4. 在USART_BAUD寄存器中设置波特率；

5. 在USART_CTL0寄存器中置位UEN位，使能USART；

6. 在USART_CTL0中设置REN位。

接收器在使能后若检测到一个有效的起始脉冲便开始接收码流。在接收一个数据帧的过程中会检测噪声错误，奇偶校验错误，帧错误和过载错误。

当接收到一个数据帧，USART_STAT 寄存器中的 RBNE 置位，如果设置了 USART_CTL0 寄存器中相应的中断使能位 RBNEIE，将会产生中断。在 USART_STAT 寄存器中可以观察接收状态标志。

软件可以通过读 USART_RDATA 寄存器或者 DMA 方式获取接收到的数据。不管是直接读寄存器还是通过 DMA，只要是对 USART_RDATA 寄存器的一个读操作都可以清除 RBNE 位。

在接收过程中，需使能 REN 位，不然当前的数据帧将会丢失。

在默认情况下，接收器通过获取三个采样点的值来估计该位的值。如果是 8 倍过采样模式，选择第 3、4、5 个采样点；如果是 16 倍过采样模式，选择第 7、8、9 个采样点。如果在 3 个采样点中有 2 个或 3 个为 0，该数据位被视为 0，否则为 1。如果 3 个采样点中有一个采样点的值与其他两个不同，不管是数据位，奇偶校验位或者停止位，都将产生噪声错误（NERR）。如果使能 DMA，并置位 USART_CTL2 寄存器中 ERRIE，将会产生中断。如果在 USART_CTL2中置位 OSB，接收器将仅获取一个采样点来估计一个数据位的值。在这种情况下将不会检测到噪声错误。


图 20-20. 过采样方式接收一个数据位（OSB=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/021adec5035ac3a181a7ac1e74e504c01ff540d7bc1263f3a93686d7d2499f09.jpg)


通过置位 USART_CTL0 寄存器中的 PCEN 位使能奇偶校验功能，接收器在接收一个数据帧时计算预期奇偶校验值，并将其与接收到的奇偶校验位进行比较。如果不相等，USART_STAT 寄存器中 PERR 被置位。如果置位了 USART_CTL0 寄存器中的 PERRIE 位，将产生中断。

如果在停止位传输过程中 RX 引脚为 0，将产生帧错误，USART_STAT 寄存器中 FERR 置位。如果使能 DMA 并置位 USART_CTL2 寄存器中 ERRIE 位，将产生中断。

当接收到一帧数据，而 RBNE 位还没有被清零，随后的数据帧将不会存储在数据接收缓冲区中。USART_STAT 寄存器中的溢出错误标志位 ORERR 将置位。如果使能 DMA 并置位USART_CTL2 寄存器中 ERRIE 位或者置位 RBNEIE，将产生中断。

若接收过程中，产生了噪声错误（NERR）、校验错误（PERR）、帧错误（FERR）或溢出错误（ORERR），则NERR、PERR、FERR或ORERR将和RBNE同时置位。如果没有使能DMA，RBNE中断发生时，软件需检查是否有噪声错误、校验错误、帧错误或溢出错误产生。

## DMA方式访问数据缓冲区

为减轻处理器的负担，可以采用 DMA 访问发送缓冲区或者接收缓冲区。置位 USART_CTL2寄存器中DENT 位可以使能DMA 发送，置位 USART_CTL2寄存器中 DENR位可以使能 DMA接收。

当 DMA 用于 USART 发送时，DMA 将数据从片内 SRAM 传送到 USART 的数据缓冲区。配置步骤如 20-21. DMA USART 所示。


图 20-21. 采用 DMA方式实现 USART 数据发送配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/ed8bb7194098f4bfcd949c7f1475c23c0727b8cb7d1103db2805006d8b37988d.jpg)


所有数据帧都传输完成后，USART_STAT 寄存器中 TC 位置 1。如果 USART_CTL0 寄存器中TCIE置位，将产生中断。

当 DMA 用于 USART 接收时，DMA 将数据从接收缓冲区传送到片内 SRAM。配置步骤如20-22. DMA USART 所示。如果将 USART_CTL2 寄存器中ERRIE 位置 1，USART_STAT 寄存器中的错误标志位（FERR、ORERR 和 NERR）置位时将产生中断。


图 20-22. 采用 DMA方式实现 USART 数据接收配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/bb57aa1aeea2b14cc162f45654a80e5a263ae73b25d40ad4923c09178356c8e3.jpg)



当 USART 接收到的数据数量达到了 DMA 传输数据数量，DMA模块将产生传输完成中断。


## 多处理器通信

在多处理器通信中，多个 USART 被连接成一个网络。对于一个设备来说，监视所有来自 RX引脚的消息，是一种巨大的负担。为减轻设备负担，软件可以通过将 USART_CMD 寄存器中MMCMD 位置 1 使 USART 进入静默模式。

如果 USART 处于静默模式，所有的接收状态标志位将不会被置位。此外，USART 可以由硬件用以下两种方式中的一种来唤醒：空闲总线检测和地址标记检测。

设备默认使用空闲总线检测方法唤醒 USART。当在 RX 引脚检测到空闲帧时，硬件会将 RWU清零，从而退出静默模式，但 USART_STAT 寄存器中 IDLEF 位不会被置 1。

当 USART_CTL0 寄存器中 WM被置位，数据最高位会被认为是地址标志位。如果地址标志位为 1，该字节被认为是地址字节。如果地址标志位是 0，该字节被认为是数据字节。如果地址字节的低 4 位或低 7 位与 USART_CTL1 寄存器中的 ADDR 位相同，硬件会将 RWU 清零，并退出静默模式。接收到将USART唤醒的数据帧，RBNE将置位。状态标志可以从USART_STAT寄存器中获取。如果地址字节的低 4 位或低 7 位与 USART_CTL1 寄存器中的 ADDR 位不相同，硬件会置位 RWU 并自动进入静默模式。在这种情况下，RBNE 不会被置位。

如果 USART_CTL0 寄存器中 PCEN 位被置位，地址字节最高位被视为校验位，其余位被视为地址位。如果 ADDM 位被置位，且接收帧为 7 位的数据，其中最低的 6 位将与 ADDR[5:0]比较。如果 ADDM 位被置位，且接收帧为 9 位的数据，其中低 8 位将与 ADDR[7:0]进行比较。

## LIN 模式

将 USART_CTL1 寄存器的 LMEN 置位即可使能本地互联网络模式。在 LIN 模式下，USART_CTL1 寄存器中 CKEN，STB[1:0]和 USART_CTL2 的 SCEN，HDEN，IREN 位都应

该被清 0。

在发送一个普通数据帧时，LIN 发送过程与普通发送过程相同。数据位的长度只能为 8。一个停止位后连续 13 个 0 为断开帧。

断开检测功能完全独立于普通 USART 接收器。因此，断开检测可以是在空闲状态下，也可以在数据传输过程中。USART_CTL1 寄存器中 LBLEN 位可以选择断开帧的长度。如果在 RX 引脚检测到大于或等于与预期的断开帧长度的 0（LBLEN=0 时，10 个 0；LBLEN=1 时，11 个0），USART_STAT 寄存器中 LBDF 置位。如果 USART_CTL1 寄存器中 LBDIE 被置位，将产生中断。

如 20-23. 所示，如果断开帧发生在空闲状态下，USART 接收器会接收到一个全 0 数据帧，同时 FERR 置位。


图 20-23. 空闲状态下检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/3a942b0bf08728394757332aee41dee733eebcdca1debbac22299e52b9923304.jpg)


如 20-24. 所示，如果断开帧发生在数据传输过程中，当前传输帧发生错误，FERR 置位。


图 20-24. 数据传输过程中检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/878e89216f6e98dae1252def9170b58844c8daf0779f63a923dc4d24a5414c26.jpg)


## 同步通信模式

USART 支持主机模式下的全双工同步串行通信，可以通过置位 USART_CTL1 的CKEN 位来使能。在同步模式下，USART_CTL1 的 LMEN 和 USART_CTL2 的 SCEN，HDEN，IREN 位应被清 0。CK 引脚作为 USART 同步发送器的时钟输出，仅当 TEN 位被使能时，它才被激活。在起始位和停止位传送期间，不会从 CK 引脚输出时钟脉冲。USART_CTL1 的 CLEN 位用来决定在最低位（地址索引位）发送期间是否有时钟信号输出。在空闲状态和断开帧的发送过程中，也不会有时钟信号产生。USART_CTL1 的 CPH 位用来决定数据在第一个时钟沿被采样还是在第二个时钟沿被采样。USART_CTL1 的 CPL 位用来决定在 USART 同步模式空闲状态下，时钟引脚的电平。

CK 引脚输出波形由 USART_CTL1 寄存器中 CPL，CPH，CLEN 位决定。软件仅在 USART禁用（UEN=0）时才可以改变它们的值。

时钟与已发送的数据同步。同步模式下的接收器按照发送器的时钟进行采样，并无任何过采样。


图 20-25. 同步模式下的 USART 示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/d892d5f254024bdaaaf84184178b6884141d40c719d513172ba48177dd937ccf.jpg)



图 20-26. 8-bit 格式的 USART 同步通信波形（CLEN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/b2322202a54b543b70e717a51ccb072b941a96ea3b4da1122d4a84bbfabf088e.jpg)


## 串行红外（IrDA SIR）编解码功能模块

串行红外编解码功能通过置位 USART_CTL2 寄存器中 IREN 使能。在 IrDA 模式下，USART_CTL1 寄存器的 LMEN，STB[1:0]，CKEN 位和 USART_CTL2 寄存器的 HDEN，SCEN位应被清 0。

在 IrDA 模式下，USART 数据帧由 SIR 发送编码器进行调制，调制后的信号经由红外 LED 进行发送，经解调后将数据发送至 USART 接收器。对于编码器而言，波特率应小于 115200。


图 20-27. IrDA SIR ENDEC 模块


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/de8c8e5aaf10c3d870ac08e54e8fd4fec4f706f1fc09727b8abe144499dfe048.jpg)


在 IrDA 模式下，TX 引脚与 RX 引脚电平不同。TX 引脚通常为低电平，RX 引脚通常为高电平。IrDA 引脚电平保持稳定代表逻辑‘1’，红外光源脉冲（RTZ 信号）代表逻辑‘0’。其脉冲宽度通常占一个位时间的 3/16。IrDA 无法检测到宽度小于 1 个 PSC 时钟的脉冲。如果脉冲宽度大于 1 但是小于 2 倍 PSC 时钟，IrDA 则无法可靠地检测到。

由于 IrDA 是一种半双工协议，因此在 IrDA SIR ENDEC 模块中，发送和接收不得同时进行。


图 20-28. IrDA 数据调制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/53bfdc22d0c07ce10842523be2b96579c272cd3dd4cf283211f922c0005edb02.jpg)


将USART_CTL2寄存器中IRLP置位可以使SIR子模块工作在低功耗模式下。发送编码器由PCLK分频得到的低速时钟来驱动。分频系数在USART_GP寄存器中PSC[7:0]位配置，USART_BAUD寄存器需配置为16*PSC[7:0]。TX引脚脉冲宽度可以为低功耗波特率的3倍。接收解码器工作模式与正常IrDA模式相同。

## 半双工通信模式

通过设置 USART_CTL2 寄存器的 HDEN 位，可以使能半双工模式。在半双工通信模式下，USART_CTL1 寄存器的 LMEN，CKEN 位和 USART_CTL2 寄存器的 SCEN，IREN 位应被清零。

半双工模式下仅用单线通信， 引脚和 引脚从内部连接到一起， 引脚不再使用。引脚应被配置为开漏模式，通信冲突由软件处理。当 TEN 被置位时，在数据寄存器中的数据将会被发送。

## 智能卡（ISO7816-3）模式

智能卡模式是一种异步通信模式，支持ISO7816-3协议。支持字节模式（T=0）和块模式（T=1）。将 USART_CTL2 寄存器的 SCEN 位置 1，即可使能智能卡模式。在智能卡模式下，USART_CTL1 寄存器的 LMEN 位和 USART_CTL2 的 HDEN，IREN 位应该清 0。

如果 CKEN 位被置位，USART 将向智能卡提供一个时钟。该时钟可以分频用于其他用途。

智能卡模式下的帧格式为：1 起始位+9 数据位（包括 1 个奇偶校验位）+1.5 停止位。

智能卡模式是一种半双工通信协议模式。当与智能卡连接时，TX 引脚须被设置成开漏模式，这个引脚将会与智能卡驱动同一条双向连线。


图 20-29. ISO7816-3 数据帧格式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/4d8cf2430633a7e51a9d75c4da3ce8b435c43477339c58e0fdc5e172275807b7.jpg)



有校验错误的ISO7816-3帧


## 字节模式（T=0）

相较于正常操作模式下的时序，从发送移位寄存器到 TX 引脚的传递时间延迟了半个波特率时钟，并且 TC 标志的置位将根据 USART_GP 寄存器的 GUAT[7:0]设置延迟某一特定时间。在智能卡模式下，在最后一帧数据的停止位之后，内部保护时间计数器将开始计数，GUAT[7:0]的值配置为 ISO7816-3 协议的 CGT 减 12。在保护时间寄存器向上计数这段时间 TC 将被强制拉低，当计数达到设定值时，TC 被置位。

在 USART 发送期间，如果检测到有奇偶校验错误，TX 引脚在停止位最后一个位时间内被拉低，智能卡发送一个 NACK 信号。根据协议，USART 会自动重发 SCRTNUM 次。在重发数据帧前面会插入 2 位的帧间隔。最后一次重发字节后，TC 会立即被置位。如果在最大重发次数后仍然收到 NACK 信号，USART 将会停止发送，帧错误标志被置位。USART 不会将 NACK信号作为起始位。

在 USART 接收期间，如果在当前数据帧检测到校验错误，TX 引脚在停止位的最后一个位时间内会被拉低。智能卡会接收到 NACK 信号。然后在智能卡端会产生一个帧错误。如果接收到的字节是错误的，RBNE 中断和接收 DMA 请求都不会被激活。根据协议，智能卡将重新发送数据。如果在最大的重新发送次数后（这个次数的具体值在 SCRTNUM 位域），接收到的字符仍然是错误的，USART 停止发送 NACK 信号和标注这个错误为奇偶校验错误。将USART_CTL2 寄存器中的 NKEN 置位可以使能 NACK 信号。

空闲帧和断开帧在智能卡模式下不适用。

## 块模式（T=1）

在 T=1（块模式）下，USART_CTL2 寄存器的 NKEN 位应该清零来关闭校验错误发送。

当要从智能卡读取数据时，软件必须将 USART_RT 寄存器的 RT[23:0]位域设置成 BWT（块等待时间）-11 的值，并将 RBNEIE置位。如果到了这个时间，还没有从智能卡收到应答，将引起超时中断。如果在超时之前收到了第一个字节，则会引起 RBNE 中断。块模式下，如果用DMA从智能卡读取数据，也只能在第一个字节接收完后再去使能 DMA。

在接收到第一个字节之后（RBNE 中断）必须将 USART_RT 寄存器设置为 CWT（字节等待时间）-11 之间的某个值（这个时间以波特时间作为单位），这是为了自动检测两个连续字符之间的最大等待时间。如果智能卡在前一个字符发送结束后到设定的 CWT 周期之间没有发送字符，USART 会通过 RTF 标志提醒软件，当 RTIE被置位时，会引起中断。

USART 用一个块长度计数器统计收到的字节数，这个计数器在 USART 开始发送的时候自动清 （ ）。这个块长度信息位于智能卡发出数据的第三个字节（序言部分）。这个值必须写入 USART_RT 寄存器的 BL[7:0]。当使用 DMA模式时，在块开始之前，这个寄存器必须被设定为最小值（0x0）。为了得到这个值，在收到第四个字节后，会引起一个中断。软件可以从接收缓冲区读取第三个字节作为块长度。

在中断驱动接收模式，块的长度可以由软件提取出来并做检测或者通过设置 BL 的值得到。但是在块开始之前，BL（0xFF）可以被设置为最大值。实际值则要在接收到第三个字节后写到寄存器中。

整个块的长度（包括序言区，收尾区和信息区）等于 BL+4。块尾通过 EBF 标志和相应中断提醒给软件（当 EBIE 位置 1 时）。如果块长度出错，将会引起一个 RT 中断。

## 直接和反向转换

智能卡协议定义了两种转换方式：直接转换和反向转换。

如果选择直接转换，从数据帧的最低位开始传输，TX 引脚高电平代表逻辑‘1’，偶校验。在这种情况下，MSBF 位和 DINV 位都应设置为 0（默认值）。

如果选择反向转换，从数据帧的最高位开始传输，TX 引脚低电平代表逻辑‘1’，偶校验。在这种情况下，MSBF 位和 DINV 位都应设置为 1。

## ModBus 通信

通过实现块尾检测功能，USART 提供实现 ModBus/RTU 和 ModBus/ASCII 协议的基本支持。在 ModBus/RTU 模式下，通过一个超过 2 个字符长度的空闲状态来识别块尾。这个功能是通过一个可编程的超时检测功能来实现的。

为了检测空闲状态，必须置位 USART_CTL1 寄存器的 RTEN 位和 USART_CTL0 寄存器的RTIE位。USART_RT 寄存器必须被设置成与 2 个字节超时所对应的值。在最后一个停止位被接收后，当接收线在这期间是空闲的，将产生一个中断，通知软件当前块接收已经完成。

在 ModBus/ASCII 模式下，块尾被认为是一个特定的字符（CR/LF）串。USART 用字符匹配机制实现这个功能。具体是通过将 LF 的 ASCII 码配置到 ADDR 区域并激活地址匹配中断（AMIE=1）来实现。软件将在收到 LF 或可以在 DMA缓存中查找到 CR/LF 时得到提示。

## 接收 FIFO

通过将 USART_RFCS 寄存器的 RFEN 置位使能接收 FIFO，可以避免当 CPU 无法迅速响应RBNE 中断时，发生过载错误。接收 FIFO 和接收缓存区可储存多至 5 帧的数据。若接收 FIFO满，RFFINT 位将被置位。如果 RFFIE 被置位，将产生中断。


图 20-30. USART 接收 FIFO 结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/cd897e1569c0c234a90347d9b5bd3e78a432496483fe81b03d6320c0b9b5f631.jpg)


如果软件在响应 RBNE 中断时读数据接收缓冲区，在响应开始时，RBNEIE位应清 0。当所有接收的数据被读出后，RBNEIE 位应置位。在读出接收的数据前，PERR，NERR，FERR，EBF都应被清 0。

## 从 Deepsleep 模式唤醒

通过标准 RBNE 中断或 WUM 中断 USART 能从深度睡眠模式，深度睡眠模式 1 和深度睡眠模式 2 唤醒 MCU。

UESM 位必须置 1 并且 USART 时钟必须设置为 IRC8M 或 LXTAL （请参考 RCU 部分）。

当使用 RBNE 标准中断时，必须在进入深度睡眠模式，深度睡眠模式 1 和深度睡眠模式 2 前将 RBNEIE 位置位。

当使用WUIE 中断时，WUIE中断源可以通过WUM 位来选择。

在进入深度睡眠模式，深度睡眠模式 1 和深度睡眠模式 2 前，必须禁用 DMA。

在进入深度睡眠模式，深度睡眠模式 1 和深度睡眠模式 2 前，软件必须检测 USART 是否正在传送数据。这可以通过 USART_STAT 寄存器中的 BSY 标志来判断。REA 位必须被检测以确保 USART 是使能的。

当检测到唤醒事件时，无论 MCU 工作在深度睡眠模式还是正常模式，WUF 标志位通过硬件被置 1，并且在WUIE被置位的情况下，触发一个唤醒中断。

## USART 中断

USART 中断事件和标志如 20-6. USART 所示：


表 20-6. USART 中断请求


<table><tr><td>中断事件</td><td>事件标志</td><td>使能控制位</td></tr><tr><td>发送数据寄存器空</td><td>TBE</td><td>TBEIE</td></tr><tr><td>发送结束</td><td>TC</td><td>TCIE</td></tr><tr><td>接收到的数据可以读取</td><td>RBNE</td><td rowspan="2">RBNEIE</td></tr><tr><td>检测到过载错误</td><td>ORERR</td></tr><tr><td>接收FIFO满</td><td>RFFINT</td><td>RFFIE</td></tr><tr><td>检测到线路空闲</td><td>IDLEF</td><td>IDLEIE</td></tr><tr><td>奇偶校验错误</td><td>PERR</td><td>PERRIE</td></tr><tr><td>LIN模式下,检测到断开标志</td><td>LBDF</td><td>LBDIE</td></tr><tr><td>当DMA接收使能时,接收错误(噪声错误、溢出错误、帧错误)</td><td>NERR或ORERR或FERR</td><td>ERRIE</td></tr><tr><td>字符匹配</td><td>AMF</td><td>AMIE</td></tr><tr><td>接收超时错误</td><td>RTF</td><td>RTIE</td></tr><tr><td>发现块尾</td><td>EBF</td><td>EBIE</td></tr><tr><td>从Deepsleep模式唤醒</td><td>WUF</td><td>WUIE</td></tr></table>


在发送给中断控制器之前，所有的中断事件是逻辑或的关系。因此在任何时候 USART 只能向控制器产生一个中断请求。不过软件可以在一个中断服务程序里处理多个中断事件。



图 20-31. USART 中断映射框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8f43dc3e-08b8-4487-9a14-a566eeef8a83/31a1271e74238661d3950767a065e24cf5405680f40675aabae9e8e3c402b62f.jpg)


