## 24. 通用同步异步收发器（USART）

## 24.1. 简介

通用同步异步收发器（USART）提供了一个灵活方便的串行数据交换接口，数据帧可以通过全双工或半双工，同步或异步的方式进行传输。USART 提供了可编程的波特率发生器，能对 UCLK（PCLK1 或 PCLK2）进行分频产生 USART 发送和接收所需的特定频率。

USART 不仅支持标准的异步收发模式，还实现了一些其他类型的串行数据交换模式，如红外编码规范，SIR，智能卡协议，LIN，半双工以及同步模式。它还支持多处理器通信和 Modem 流控操作（CTS/RTS）。数据帧支持从 LSB 或者 MSB 开始传输。数据位的极性和 TX/RX 引脚都可以灵活配置。

USART 支持 DMA 功能，以实现高速率的数据通信，除了 UART4。

## 24.2. 主要特征

 NRZ标准格式（Mark/Space）。

 全双工异步通信。

 半双工单线通信。

 可编程的波特率产生器：

由外设时钟分频产生，其中USART0由PCLK2分频得到，USART1/2和UART3/4由PCLK1分频得到。

‐ 8倍或16倍过采样。

当时钟频率为280M，过采样为8，最高速度可到35MBits/s。

 完全可编程的串口特性：

‐ 偶校验位，奇校验位，无校验位的生成/检测。

数据位（8或9位）；

‐ 产生0.5，1，1.5或者2个停止位。

 发送器和接收器可分别使能。

 支持硬件Modem流控操作（CTS/RTS）。

 DMA访问数据缓冲区。

 LIN断开帧的产生和检测。

 支持红外数据协议（IrDA）。

 同步传输模式以及为同步传输输出发送时钟。

 支持兼容ISO7816-3的智能卡接口：

‐ 字节模式（T=0）

‐ 块模式（T=1）

‐ 直接和反向转换

 多处理器通信：

‐ 如果地址不匹配，则进入静默模式。

通过线路空闲检测或者地址匹配从静默模式唤醒。

 多种状态标志：

传输检测标志：接收缓冲区不为空（RBNE），发送缓冲区为空（TBE），传输完成(TC)，忙（BSY）。

错误检测标志：过载错误（ORERR），噪声错误（NERR），帧格式错误（FERR），奇偶校验错误（PERR）。

‐ 硬件流控操作标志：CTS变化（CTSF）。

‐ LIN模式标志：LIN断开检测（LBDF）。

多处理器通信模式标志：IDLE帧检测（IDLEF）。

‐ 智能卡模式标志：块结束(EBF)和接收超时（RTF）。

‐ 若相应的中断使能，这些事件发生将会触发中断。

USART0/1/2完全实现上述功能，但是UART3/4只实现了上面所介绍的部分功能，下面这些功能在UART3/4中没有实现：

 智能卡模式

 同步模式

 硬件流操作（CTS/RTS）

 设置数据极性

 接收超时

## 24.3. 功能说明

USART接口通过 24-1. USART 中主要引脚从外部连接到其他设备。


表 24-1. USART 重要引脚描述


<table><tr><td>引脚</td><td>类型</td><td>描述</td></tr><tr><td>RX</td><td>输入</td><td>接收数据</td></tr><tr><td>TX</td><td>输出I/O(单线模式/智能卡模式)</td><td>发送数据。当USART使能后,若无数据发送,默认为高电平</td></tr><tr><td>CK</td><td>输出</td><td>用于同步通信的串行时钟信号</td></tr><tr><td>nCTS</td><td>输入</td><td>硬件流控模式发送使能信号</td></tr><tr><td>nRTS</td><td>输出</td><td>硬件流控模式发送请求信号</td></tr></table>


图 24-1. USART 模块内部框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/b9b82260aa424d43e7cc64a8671547acc502daf97f427381d9b8130ab35b7f5f.jpg)


## 24.3.1. USART 帧格式

USART 数据帧开始于起始位，结束于停止位。USART_CTL0 寄存器中WL 位可以设置数据长度。将 USART_CTL0 寄存器中 PCEN 置位，最后一个数据位可以用作校验位。若 WL 位为 0，第七位为校验位。若WL 位置 1，第八位为校验位。USART_CTL0 寄存器中 PM 位用于选择校验位的计算方法。


图 24-2. USART 字符帧 (8 数据位和 1 停止位)


<table><tr><td colspan="10">时钟</td></tr><tr><td rowspan="2">起始位</td><td colspan="5">数据帧</td><td colspan="4">或校验位</td></tr><tr><td>bit0</td><td>bit1</td><td>bit2</td><td>bit3</td><td>bit4</td><td>bit5</td><td>bit6</td><td>bit7</td><td>Stop</td></tr><tr><td colspan="10">空闲帧</td></tr><tr><td colspan="10">断开帧</td></tr></table>

在发送和接收中，停止位可以由 USART_CTL1 寄存器中 STB[1:0]位域配置。


表 24-2. 停止位配置


<table><tr><td>STB[1:0]</td><td>停止位长度(位)</td><td>功能描述</td></tr><tr><td>00</td><td>1</td><td>默认值</td></tr><tr><td>01</td><td>0.5</td><td>智能卡模式接收</td></tr><tr><td>10</td><td>2</td><td>标准 USART,单线以及调制解调模式</td></tr><tr><td>11</td><td>1.5</td><td>智能卡模式发送和接收</td></tr></table>

在一个空闲帧中，所有位都为 1。数据帧长度与正常 USART 数据帧长度相同。

紧随停止位后多个低电平为中断帧。USART 数据帧的传输速度由 UCLK时钟频率，波特率发生器的配置共同决定。

## 24.3.2. 波特率发生

波特率分频系数是一个 18 位的数字，包含 14 位整数部分和 4 位小数部分。波特率发生器使用这两部分组合所得的数值来确定波特率。由于具有小数部分的波特率分频系数，将使 USART 能够产生所有标准波特率。

波特率分频系数（USARTDIV）与系统时钟具有如下关系：

如果过采样率是 16，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{1 6 \times \text { Baud   Rate }}\tag{23-1}
$$

如果过采样率是 8，公式为：

$$
\text { USARTDIV } = \frac {\text { UCLK }}{8 \times \text { Baud   Rate }}\tag{23-2}
$$

例如，当过采样是 16：

1. 由USART_BAUD寄存器的值得到USARTDIV：

假设 USART_BAUD=0x21D，则 INTDIV=33（0x21），FRADIV=13（0xD）。

UASRTDIV=33+13/16=33.81。 

2. 由USARTDIV得到USART_BAUD寄存器的值：

假设要求 UASRTDIV=30.37，INTDIV=30（0x1E）。

16*0.37=5.92，接近整数 6，所以 FRADIV=6（0x6）。

USART_BAUD=0x1E6。 

注意：若取整后 FRADIV=16（溢出），则进位必须加到整数部分。

## 24.3.3. USART 发送器

如果 USART_CTL0 寄存器的发送使能位（TEN）被置位，当发送数据缓冲区不为空时，发送器将会通过 TX 引脚发送数据帧。TX 引脚的极性可以通过 USART_CTL3 寄存器中 TINV 位来配置。

时钟脉冲通过 CK 引脚输出。

TEN 置位后发送器会发出一个空闲帧。TEN 位在数据发送过程中是不可以被复位的。

系统上电后，TBE 默认为高电平。在 USART_STAT0 寄存器中 TBE 置位时，数据可以在不覆盖前一个数据的情况下写入 USART_DATA 寄存器。当数据写入 USART_DATA 寄存器，TBE 位将被清 0。在数据由 USART_DATA移入移位寄存器后，该位由硬件置 1。如果数据在一个发送过程正在进行时被写入 USART_DATA寄存器，它将首先被存入发送缓冲区，在当前发送过程完成时传输到发送移位寄存器中。如果数据在写入 USART_DATA 寄存器时，没有发送过程正在进行，TBE位将被清零然后迅速置位，原因是数据将立刻传输到发送移位寄存器。

假如一帧数据已经发送出去，并且 TBE位已经置位，那么 USART_STAT0 寄存器中 TC 位将被置1。如果 USART_CTL0 寄存器中的中断使能位（TCIE）为 1，将会产生中断。

24-3. USART 给出了 USART 发送步骤。软件操作按以下流程进行：

1. 在USART_CTL0寄存器中置位UEN位，使能USART；

2. 通过USART_CTL0寄存器的WL设置字长；

3. 在USART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

4. 如果选择了多级缓存通信方式，应该在USART_CTL2寄存器中使能DMA（DENT位）；

5. 在USART_BAUD寄存器中设置波特率；

6. 在USART_CTL0寄存器中设置TEN位；

7. 等待TBE置位；

8. 向USART_DATA寄存器写数据；

9. 若DMA未使能，每发送一个字节都需重复步骤7-8；

10. 等待TC=1，发送完成。


图 24-3. USART 发送步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/21ea77521637ff6c6d0e96dcacc56f9962d12f8be42e88a17bf43fc2558f36e7.jpg)


在禁用 USART 或进入低功耗状态之前，必须等待 TC 置位。先读 USART_STAT0 然后再写USART_DATA 可将 TC 位清 0。在多级缓存通信方式（DENT=1）下，直接向 TC 写 0，也能清TC。

## 24.3.4. USART 接收器

上电后，USART 接收器使能按以下步骤进行：

1. 在USART_CTL0寄存器中置位UEN位，使能USART；

2. 写USART_CTL0寄存器的WL去设置字长；

3. 在USART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

4. 如果选择了多级缓存通信方式，应该在USART_CTL2寄存器中使能DMA（DENR位）；

5. 在USART_BAUD寄存器中设置波特率；

6. 在USART_CTL0中设置REN位。

接收器在使能后若检测到一个有效的起始脉冲便开始接收码流。在接收一个数据帧的过程中会检测噪声错误，奇偶校验错误，帧错误和过载错误。

当接收到一个数据帧，USART_STAT0 寄存器中的 RBNE 置位，如果设置了 USART_CTL0 寄存器中相应的中断使能位 RBNEIE，将会产生中断。在 USART_STAT0 寄存器中可以观察接收状态标志。

软件可以通过读 USART_DATA 寄存器或者 DMA方式获取接收到的数据。不管是直接读寄存器还是通过 DMA，只要是对 USART_DATA寄存器的一个读操作都可以清除 RBNE 位。

在接收过程中，需使能 REN 位，不然当前的数据帧将会丢失。

在默认情况下，接收器通过获取三个采样点的值来估计该位的值。如果是 8 倍过采样模式，选择第 3、4、5 个采样点；如果是 16 倍过采样模式，选择第 7、8、9 个采样点。如果在 3 个采样点中有 2 个或 3 个为 0，该数据位被视为 0，否则为 1。如果 3 个采样点中有一个采样点的值与其他两个不同，不管是数据位，奇偶校验位或者停止位，都将产生噪声错误（NERR）。如果使能 DMA，并置位 USART_CTL2 寄存器中 ERRIE，将会产生中断。如果在 USART_CTL2 中置位 OSB，接收器将仅获取一个采样点来估计一个数据位的值。在这种情况下将不会检测到噪声错误。


图 24-4. 过采样方式接收一个数据位（OSB=0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/ce73c9e8a4d7e413c19849157b16bf062109da68a39a1315a87adb7e47ab6aff.jpg)


通过置位 USART_CTL0 寄存器中的 PCEN 位使能奇偶校验功能，接收器在接收一个数据帧时计算预期奇偶校验值，并将其与接收到的奇偶校验位进行比较。如果不相等，USART_STAT0 寄存器中 PERR 被置位。如果设置了 USART_CTL0 寄存器中的 PERRIE位，将产生中断。

如果在停止位传输过程中 RX 引脚为 0，将产生帧错误，USART_STAT0 寄存器中 FERR 置位。如果使能 DMA 并置位 USART_CTL2 寄存器中 ERRIE 位，将产生中断。

当接收到一帧数据，而 RBNE 位还没有被清零，随后的数据帧将不会存储在数据接收缓冲区中。

USART_STAT0寄存器中的溢出错误标志位ORERR将置位。如果使能DMA并置位USART_CTL2寄存器中 ERRIE 位或者置位 RBNEIE，将产生中断。

若接收过程中，产生了噪声错误（NERR）、校验错误（PERR）、帧错误（FERR）或溢出错误（ORERR），则 NERR、PERR、FERR 或 ORERR 将和 RBNE 同时置位。如果没有使能 DMA，RBNE 中断发生时，软件需检查是否有噪声错误、校验错误、帧错误或溢出错误产生。

## 24.3.5. DMA 方式访问数据缓冲区

为减轻处理器的负担，可以采用 DMA访问发送缓冲区或者接收缓冲区。置位 USART_CTL2 寄存器中 DENT 位可以使能 DMA 发送，置位 USART_CTL2 寄存器中 DENR 位可以使能 DMA 接收。

当 DMA 用于 USART 发送时，DMA 将数据从片内 SRAM 传送到 USART 的数据缓冲区。配置步骤如 24-5. DMA USART 所示。


图 24-5. 采用 DMA方式实现 USART 数据发送配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/b2c8dc68a42fcd4065f8b728cc74e5ed26a74910f104f5aecef96b92fc2b3bf6.jpg)



所有数据帧都传输完成后，USART_STAT0 寄存器中 TC 位置 1。如果 USART_CTL0 寄存器中TCIE置位，将产生中断。


当 DMA 用于 USART 接收时，DMA将数据从接收缓冲区传送到片内 SRAM。配置步骤如 24-6.DMA USART 所示。如果将 USART_CTL2 寄存器中 ERRIE 位置 1，USART_STAT0 寄存器中的错误标志位（FERR、ORERR 和 NERR）被置位时将产生中断。


图 24-6. 采用 DMA方式实现 USART 数据接收配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/7546d841eba03e11d7790b3c6305994ed65d119ff6b26a3d05047bc1b7235a40.jpg)



当 USART 接收到的数据数量达到了 DMA 传输数据数量，DMA模块将产生传输完成中断。


## 24.3.6. 硬件流控制

硬件流控制功能通过 nCTS 和 nRTS引脚来实现。通过将 USART_CTL2 寄存器中 RTSEN 位置 1来使能 RTS 流控，将 USART_CTL2 寄存器中 CTSEN 位置 1 来使能 CTS 流控。


图 24-7. 两个 USART 之间的硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/c603df713e0a2a899131b497f0c4c4500931b6d363c42aa629aef41dd85af040.jpg)


## RTS 流控

USART 接收器输出 nRTS，它用于反映接收缓冲区状态。当一帧数据接收完成，nRTS 变成高电平，这样是为了阻止发送器继续发送下一帧数据。当接收缓冲区满时，nRTS 保持高电平，可以通过读 USART_DATA 寄存器来清零。

## CTS 流控

USART 发送器监视 nCTS 输入引脚来决定数据帧是否可以发送。如果 USART_STAT0 寄存器中TBE 位是 0 且 nCTS 为低电平，发送器发送数据帧。在发送期间，若 nCTS 信号变为高电平，发送器将会在当前数据帧发送完成后停止发送。


图 24-8. 硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/d87a982696a1912753d54cd6f5b68a4d42ea72b06faad3ed892a003d13b8f547.jpg)


如果 CTS 流控制被使能，在 nCTS引脚信号发生变化时，USART_STAT0 寄存器中 CTSF 位会置1。如果 USART_CTL2 寄存器中的 CTSIE 位被置位，将会产生中断。

## 24.3.7. 多处理器通信

在多处理器通信中，多个 USART 被连接成一个网络。对于一个设备来说，监视所有来自 RX 引脚的消息，是一种巨大的负担。为减轻设备负担，软件可以通过将 USART_CTL0 寄存器中 RWU 位置 1 使一个 USART 进入静默模式。

如果 USART 处于静默模式，所有的接收状态标志位将不会被置位。软件可以通过对 RWU 清零来唤醒 USART。

此外，USART 可以由硬件用以下两种方式中的一种来唤醒：空闲总线检测和地址匹配检测。

设备默认使用空闲总线检测方法唤醒 USART。当在 RX 引脚检测到空闲帧时，硬件会将 RWU 清零，从而退出静默模式，但 USART_STAT0 寄存器中 IDLEF 位不会被置 1。

当 USART_CTL0 寄存器中 WM 被置位，数据最高位会被认为是地址标志位。如果地址标志位为1，该字节被认为是地址字节。如果地址字节的低 4 位与 USART_CTL1 寄存器中的 ADDR[3:0]相同，硬件会将 RWU 清零，并退出静默模式。接收到将 USART 唤醒的数据帧，RBNE 将置位。状态标志可以从 USART_STAT0 寄存器中获取。如果地址字节的低 4 位与 USART_CTL1 寄存器中的 ADDR[3:0]不相同，硬件会置位 RWU 并进入静默模式。在这种情况下，RBNE 不会被置位。

如果采用地址匹配检测，默认情况下，IDLEF 不会置位并且接收器对地址字节不做奇偶校验。如果USART_CHC 寄存器中 PCM 位以及 USART_CTL0 寄存器中 PCEN 位被置位，则 MSB 位将被检查为奇偶校验位，并且 MSB位之前的位被检测为地址标志。

当 RBNE为 0 时，RWU 可以被写为 0 或 1。

## 24.3.8. LIN 模式

将 USART_CTL1 寄存器的 LMEN 置位即可使能本地互联网络模式。

在 LIN 模式下，USART_CTL1 寄存器中 CKEN，WL，STB[1:0]以及 USART_CTL2 的 SCEN，HDEN，IREN 位都应该被清 0。

在发送一个普通数据帧时，LIN 发送过程与普通发送过程相同。当 USART_CTL0 寄存器中SBKCMD 置位时，USART 在发送完一个停止位后会连续发送 13 个 0。

断开检测功能完全独立于普通 USART 接收器。因此，断开检测可以是在空闲状态下，也可以在数据传输过程中。USART_CTL1 寄存器中 LBLEN 位可以选择断开帧长度。如果在 RX 引脚检测到大于或等于与预期断开帧长度相等数量的 0(LBLEN=0 时，10 个 0；LBLEN=1 时，11 个 0)，USART_STAT0 寄存器中 LBDF 置位。如果 USART_CTL1 寄存器中 LBDIE 被置位，将产生中断。

如 24-9. 所示，如果断开帧发生在空闲状态下，USART 接收器会接收到一个全 0 数据帧，同时 FERR 置位。


图 24-9. 空闲状态下检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/8a15b95a51a32f2dd718630af910598135c190123067d04fbc3193d460d69ec4.jpg)



如 24-10. 所示，如果断开帧发生在数据传输过程中，当前传输帧发生错误，FERR 置位。



图 24-10. 数据传输过程中检测断开帧


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/e58cc520594900171c21d16a4d612dafe50f7fd5b9d25315921a0918067688d1.jpg)


## 24.3.9. 同步通信模式

USART 支持主机模式下的全双工同步串行通信，可以通过置位 USART_CTL1 的 CKEN 位来使能。在同步模式下，USART_CTL1 的 LMEN 和 USART_CTL2 的 SCEN，HDEN，IREN 位应该被清 0。CK引脚作为 USART 同步发送器的时钟输出，仅仅当 TEN 位被使能时，它才被激活。在起始位和停止位传送期间，不会从 CK 引脚输出时钟脉冲。USART_CTL1 的 CLEN 位用来决定在最低位（地址索引位）发送期间是否有时钟信号输出。USART_CTL1 的 CPH 位用来决定数据在第一个时钟沿被采样还是在第二个时钟沿被采样。USART_CTL1 的 CPL 位用来决定在 USART 同步模式空闲状态下，时钟引脚的电平。

CK 引脚输出波形由 USART_CTL1 寄存器中 CPL，CPH，CLEN 位决定。软件仅在 USART 禁用（UEN=0）时才可以改变它们的值。

如果 USART_CTL0 寄存器中 REN 置位，接收器的工作方式与普通模式下接收方式是不同的。接收器在时钟捕获沿采样数据，并无任何过采样。


图 24-11. 同步模式下的 USART 示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/42bf608d9207a8f954ec0995b32ced7a50423cc407e72202bb7625278c11841a.jpg)



图 24-12. 8-bit 格式的 USART 同步通信波形(CLEN=1)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/b7e96064786c280d884f8b1107a8e806b7e43ffd7e836d20ad6ac6b240a92499.jpg)


## 24.3.10. 串行红外(IrDA SIR)编解码功能模块

串行红外编解码功能通过置位 USART_CTL2 寄存器中 IREN 使能。在 IrDA 模式下，USART_CTL1寄存器的 LMEN，STB[1:0]，CKEN 位和 USART_CTL2 寄存器的 HDEN，SCEN 位将被清 0。

在 IrDA 模式下，USART 数据帧由 SIR 发送编码器进行调制，调制后的信号经由红外 LED 进行发送，经解调后将数据发送至 USART 接收器。对于编码器而言，波特率应小于 115200。


图 24-13. IrDA SIR ENDEC 模块


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/0711939895beaabdd0fd1be2937fe098f0ccde9ace4a8aaa67142c2ec9b509ea.jpg)


在 IrDA 模式下，TX 引脚电平与 RX 引脚不同。TX 引脚通常为低电平，RX 引脚通常为高电平。IrDA 引脚电平保持稳定代表逻辑‘1’，红外光源脉冲（RTZ 信号）代表逻辑‘0’。其脉冲宽度通常占一个位时间的 3/16。IrDA 无法检测到宽度小于一个 1 个 PSC 时钟的脉冲。如果脉冲宽度大于 1但是小于 2 倍 PSC 时钟，IrDA 则无法可靠的检测到。

由于 IrDA 是一种半双工协议，因此在 IrDA SIR ENDEC 模块中，发送和接收不得同时进行。


图 24-14. IrDA 数据调制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/bf74abca15a0d08104c365cbda65b9d8bcaa18cbf4d6ade795f94cc9f39cce18.jpg)


将USART_CTL2寄存器中IRLP置位可以使SIR子模块工作在低功耗模式下。发送编码器由PCLK分频得到的低速时钟来驱动。分频系数在 USART_GP 寄存器中 PSC[7:0]位配置，USART_BAUD寄存器需配置为 16*PSC[7:0]。TX 引脚脉冲宽度可以为低功耗波特率的 3 倍。接收器解码器工作模式与正常 IrDA 模式相同。

## 24.3.11. 半双工通信模式

通过设置 USART_CTL2 寄存器的 HDEN 位，可以使能半双工模式。

在半双工通信模式下，USART_CTL1寄存器的LMEN，CKEN位和USART_CTL2寄存器的SCEN，IREN 位清零。

半双工模式下仅用单线通信，TX 引脚和 RX 引脚将从内部连接到一起，RX 引脚不再使用。TX 引脚应被配置为开漏模式，通信冲突由软件处理。

## 24.3.12. 智能卡(ISO7816-3)模式

智能卡模式是一种异步通信模式，支持 ISO7816-3 协议。支持字节模式(T=0)和块模式(T=1)。将USART_CTL2 寄存器的 SCEN 位置 1，即可使能智能卡模式。在智能卡模式下，USART_CTL1寄存器的 LMEN 位和 USART_CTL2 的 HDEN，IREN 位应该清 0。

如果 CKEN 位被置位，USART 通过 CK 引脚向智能卡提供一个由 PCLK 分频得到的时钟。分频系数可在 USART_GP 寄存器中 PSC[4:0]配置。CK引脚只为智能卡提供时钟源。

智能卡模式是一种半双工通信协议模式。当与智能卡连接时，TX 引脚需要被设置成开漏模式，外接上拉电阻，这个引脚将会与智能卡驱动同一条双向连线。智能卡模式下的帧格式为：1 起始位+9数据位(包括 1 奇偶校验位)+1.5 停止位。其中 0.5 个停止位被配置为接收器的停止位。


图 24-15. ISO7816-3 数据帧格式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/aff5f2a7a20b85335b44a31857b0cea6170af476c19b817dfde56d5d79cc39f1.jpg)


## 字节模式（T=0）

相较于正常操作模式下的时序，从发送移位寄存器到 TX 引脚的传递时间延迟了半个波特率时钟，并且 TC 标志的置位将根据 USART_GP寄存器的 GUAT[7:0]设置延迟某一特定时间。在智能卡模式下，在最后一帧数据的停止位之后，内部保护时间计数器将开始计数，GUAT[7:0]的值配置为ISO7816-3 协议的 CGT 减 12。在保护时间寄存器向上计数这段时间 TC 将被强制拉低，当计数达到设定值时，TC 被置位。

在 USART 发送期间，如果检测到有奇偶校验错误，TX 引脚在停止位最后一个位时间内被拉低，智能卡发送一个 NACK 信号。根据协议，USART 会自动重发 SCRTNUM 次。在重发数据帧前面会插入 2 位时间的帧间隔。最后一次重发字节后，TC 会立即被置位。如果在最大重发次数后仍然收到 NACK信号，USART 将会停止发送，帧错误标志被置位。USART 不会将 NACK 信号作为起始位。

在 USART 接收期间，如果在当前数据帧检测到校验错误，TX 引脚在停止位的最后一个位时间内会被拉低。智能卡会接收到 NACK 信号。然后在智能卡端会产生一个帧错误。如果接收到的字节是错误的，RBNE 中断和接收 DMA 请求都不会被激活。根据协议，智能卡将要重新发送数据。如果在最大的重新发送次数后（这个次数的具体值在 SCRTNUM 位域），接收到的字符仍然是错误的，USART 停止发送 NACK信号和标注这个错误为奇偶校验错误。将 USART_CTL2 寄存器中的NKEN 置位可以使能 NACK 信号。

空闲帧和断开帧在智能卡模式下不适用。

## 块模式（T=1）

在 T=1（块模式）下，USART_CTL2 寄存器的 NKEN 位应该清零来关闭校验错误发送。

当要从智能卡读取数据时，软件必须将 USART_RT 寄存器设置成 BWT（块等待）-11 的值并将RBNEIE 置位。这个超时时间体现在波特时间单元。如果这个时间到了，还没有从智能卡收到应答，USART_STAT1 寄存器中 RTF 位被置位。如果设置了 USART_CTL3 寄存器中 RTIE 位，将会产生中断。如果在超时之前收到了第一个字节，则会引起 RBNE 中断。如果用 DMA 从智能卡读取数据，也只能在第一个字节接收好后再去使能 DMA。

第一个字节接收到后，RT[23:0]的值设置成 CWT（字节等待时间）-11 来使能两个连续字节间最大帧间隔自动校验。如果在 RT[23:0]周期内智能卡停止发送字节，USART_STAT1 寄存器中 RTF 将

被置位。

USART 用一个块长度计数器统计收到的字节数，这个计数器在 USART 开始发送的时候自动清 0（TBE=0）。这个块长度信息位于智能卡发出数据的第三个字节（序言部分），这个值必须写入USART_RT 寄存器 BL[7:0]。块长度计数器从 0 开始计数到最大值 BL[7:0]+4。在块计数器计数到最大值时，USART_STAT1 寄存器中块结束状态标志位 EBF 置位。如果设置了 USART_CTL3 寄存器中的 EBIE 位，将会产生中断。如果块长度发生错误，RTF 置位。

当使用 DMA模式接收时，在块开始之前，这个寄存器必须被设定为最小值（0x0）。为了得到这个值，在收到第四个字节后，会引起一个中断。软件可以从接收缓冲区读取第三个字节作为块长度。

如果接收时不使用 DMA方式，为避免产生 EBF 状态标志，BL[7:0]需首先配置为最大值 0xFF。在收到第三个字节后，真正的块长度值可以重新写入到 BL[7:0]。

## 直接和反向转换

智能卡协议定义了两种转换方式：直接转换和反向转换。

如果选择直接转换，从数据帧的最低位开始传输，TX 引脚高电平代表逻辑‘1’，偶校验。在这种情况下，USART_CTL3 寄存器中 MSBF 位和 DINV 位都为 0。

如果选择反向转换，从数据帧的最高位开始传输，TX引脚高电平代表逻辑‘1’，偶校验。在这种情况下，USART_CTL3 寄存器中 MSBF 位和 DINV 位都为 1。

## 24.3.13. USART 中断

USART 中断事件和标志如 24-3. USART 所示：


表 24-3. USART 中断请求


<table><tr><td>中断事件</td><td>事件标志</td><td>控制寄存器</td><td>使能控制位</td></tr><tr><td>发送数据寄存器空</td><td>TBE</td><td>USART_CTL0</td><td>TBEIE</td></tr><tr><td>CTS标志</td><td>CTSF</td><td>USART_CTL2</td><td>CTSIE</td></tr><tr><td>发送结束</td><td>TC</td><td>USART_CTL0</td><td>TCIE</td></tr><tr><td>接收到的数据可以读取</td><td>RBNE</td><td rowspan="2">USART_CTL0</td><td rowspan="2">RBNEIE</td></tr><tr><td>检测到过载错误</td><td>ORERR</td></tr><tr><td>检测到线路空闲</td><td>IDLEF</td><td>USART_CTL0</td><td>IDLEIE</td></tr><tr><td>奇偶校验错误</td><td>PERR</td><td>USART_CTL0</td><td>PERRIE</td></tr><tr><td>LIN模式下,检测到断开标志</td><td>LBDF</td><td>USART_CTL1</td><td>LBDIE</td></tr><tr><td>接收超时错误</td><td>RTF</td><td>USART_CTL3</td><td>RTIE</td></tr><tr><td>发现块尾</td><td>EBF</td><td>USART_CTL3</td><td>EBIE</td></tr><tr><td>接收错误(噪声错误、溢出错误、帧错误)当DMA接收使能时</td><td>NERR或ORERR或FERR</td><td>USART_CTL2</td><td>ERRIE</td></tr></table>

在发送给中断控制器之前，所有的中断事件是逻辑或的关系。因此在任何时候 USART 只能向控制器产生一个中断请求。不过软件可以在一个中断服务程序里处理多个中断事件。


图 24-16. USART 中断映射框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/04d89f4055ff480f32aea68389a3c9536952ed5e0710d17c746e2481443b24d5.jpg)

