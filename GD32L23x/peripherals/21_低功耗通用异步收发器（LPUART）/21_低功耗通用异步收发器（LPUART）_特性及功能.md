## 21. 低功耗通用异步收发器（LPUART）

## 21.1. 简介

低功耗通用异步收发器（LPUART）提供了一个低功耗的灵活方便的串行数据交换接口。即使功耗很低，LPUART也可以执行异步串行通信。数据帧可以通过全双工或半双工，异步的方式进行传输。提供了可编程的波特率发生器，能对LPUCLK（PCLK1，CK_SYS，LTXAL或IRC16M）时钟进行分频产生LPUART发送和接收所需的特定宽范围波特率时钟。

LPUART不仅支持标准的异步收发模式，还实现了半双工串行数据交换模式。它还支持多处理器通信和硬件流控操作（CTS/RTS）。数据帧支持从LSB或者MSB开始传输。数据位的极性和TX/RX引脚都可以灵活配置。

LPUART支持DMA功能，以实现高速率的数据通信。

## 21.2. 主要特征

◼ NRZ标准格式；

◼ 全双工异步通信；

◼ 半双工单线通信；

◼ 双时钟域：

互为异步关系的PCLK和独立于PCLK时钟的LPUART时钟；

不依赖LPUCLK设置的波特率设置；

◼ 使用LXTAL时钟，可编程产生300 – 9600波特率；

◼ 可编程的波特率产生器，当时钟频率为32MHz，最高速度可达10Mbits/s；

◼ 完全可编程的串口特性：

数据位（7或8或9位）低位或高位在前；

偶校验位，奇校验位，无校验位的生成或检测；

– 产生1或2个停止位；

◼ 可互换的Tx/Rx引脚；

◼ 可配置的数据极性；

◼ 支持硬件Modem流控操作（CTS/RTS）和RS485驱动使能；

◼ 借助集中式DMA，实现可配置的多级缓存通信；

◼ 发送器和接收器可分别使能；

◼ 奇偶校验位控制：

– 发送奇偶校验位；

– 检测接收的数据字节的奇偶校验位；

◼ 多处理器通信：

如果地址不匹配，则进入静默模式；

通过线路空闲检测或者地址匹配检测从静默模式唤醒；

◼ 从深度睡眠模式唤醒：

通过标准的RBNE中断；

通过WUF中断；

◼ 多种状态标志：

传输检测标志：接收缓冲区不为空（RBNE），发送缓冲区为空（TBE），传输完成（TC）；

错误检测标志：过载错误（ORERR），噪声错误（NERR），帧格式错误（FERR），奇偶校验错误（PERR）；

硬件流控操作标志：CTS变化（CTSF）；

多处理器通信模式标志：IDLE帧检测（IDLEF）；

从深度睡眠模式唤醒标志（WUF）；

– 若相应的中断使能，这些事件发生将会触发中断。

## 21.3. 功能说明

LPUART 接口通过 20-1. USART 中主要引脚从外部连接到其他设备。


表 21-1. LPUART 重要引脚描述


<table><tr><td>引脚</td><td>类型</td><td>描述</td></tr><tr><td>RX</td><td>输入</td><td>接收数据</td></tr><tr><td>TX</td><td>输出 I/O(单线模式)</td><td>发送数据。当 LPUART 使能后,若无数据发送,默认为高电平</td></tr><tr><td>nCTS</td><td>输入</td><td>硬件流控模式发送使能信号</td></tr><tr><td>nRTS</td><td>输出</td><td>硬件流控模式发送请求信号</td></tr></table>


图 21-1. LPUART 模块内部框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/140c62c21b1b2fca2d3a2898caa14de4da3ae210e511e680395e405695410e57.jpg)


## 21.3.1. LPUART 帧格式

LPUART数据帧开始于起始位，结束于停止位。LPUART_CTL0寄存器中WL[1:0]位可以设置数据长度，参考 21-2. LPUART 。将LPUART_CTL0寄存器中PCEN置位，最后一个数据位可以用作校验位。LPUART_CTL0寄存器中PM位用于选择校验位的计算方法。

## 图21-2. LPUART字符帧

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/e2b8d70df7a43881f34c603bc01c1415e7f8def32e01561998103331046e911e.jpg)


在发送和接收中，停止位可以在LPUART_CTL1寄存器中STB[1:0]位域中配置：

$$
\begin{array}{r l} {-} & {\mathrm{STB} [ 1: 0 ] = 0 0: 1 \text {个停止位}} \\ {-} & {\mathrm{STB} [ 1: 0 ] = 1 0: 2 \text {个停止位}} \end{array}
$$

在一个空闲帧中，所有位都为1。数据帧长度与正常LPUART数据帧长度相同。

## 21.3.2. 波特率发生

波特率分频系数是一个20位的数值，波特率发生器使用该数值来确定波特率。波特率分频系数（LPUARTDIV）与LPUCLK具有如下关系：

$$
\text { LPUARTDIV } = \frac {2 5 6 \times \text { LPUCLK }}{\text { Baud   Rate }}\tag{21-1}
$$

其中：

LPUARTDIV：波特率分频系数，在 LPUART_BAUD 寄存器中定义

注意：

1. LPUART_BAUD[19:0]中的值必须大于 0x300。

2. （3x 波特率） ≤ LPUCLK ≤ （4096x 波特率）。

3. 在通信期间 LPUART_BAUD 寄存器的值不能被改动。

## 21.3.3. LPUART 发送器

如果LPUART_CTL0寄存器的发送使能位（TEN）被置位，当发送数据缓冲区不为空时，发送器将会通过TX引脚发送数据帧。TX引脚的极性可以通过LPUART_CTL1寄存器中TINV位来配置。

TEN置位后发送器会发出一个空闲帧。TEN位在数据发送过程中是不可以被复位的。

系统上电后，TBE默认为高电平。在LPUART_STAT寄存器中TBE置位时，数据可以在不覆盖前一个数据的情况下写入LPUART_TDATA寄存器。当数据写入LPUART_TDATA寄存器，TBE位将被清0。在数据由LPUART_TDATA移入移位寄存器后，该位由硬件置1。如果数据在一个发送过程正在进行时被写入LPUART_TDATA寄存器，它将首先被存入发送缓冲区，在当前发送过程完成时传输到发送移位寄存器中。如果数据在写入LPUART_TDATA寄存器时，没有发送过程正在进行，TBE位将被清零然后迅速置位，原因是数据被立刻传输到发送移位寄存器。

假如一帧数据已经被发送出去，并且TBE位已被置位，那么LPUART_STAT寄存器中TC位将被置1。如果LPUART_CTL0寄存器中的中断使能位（TCIE）为1，将会产生中断。

20-3. USART 给出了 LPUART 发送步骤。软件操作按以下流程进行：

1. 通过LPUART_CTL0寄存器的WL[1:0]设置字长；

2. 在LPUART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

3. 如果选择了多级缓存通信方式，应该在LPUART_CTL2寄存器中使能DMA（DENT位）；

4. 在LPUART_BAUD寄存器中设置波特率；

5. 在LPUART_CTL0寄存器中置位UEN位，使能LPUART；

6. 在LPUART_CTL0寄存器中设置TEN位；

7. 等待TBE置位；

8. 向LPUART_TDATA寄存器写数据；

9. 若DMA未使能，每发送一个字节都需重复步骤7-8；

10. 等待TC=1，发送完成。


图 21-3. LPUART 发送步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/31553fefbb96b07c8c63b2881c42ecde061157618d4c0e57957b174913de4ab1.jpg)


在禁用LPUART或进入低功耗状态之前，必须等待TC置位。通过将LPUART_INTC寄存器的TCC位置1可以将TC位清零。

## 21.3.4. LPUART 接收器

上电后，按以下步骤使能LPUART接收器：

1. 写LPUART_CTL0寄存器的WL[1:0]位去设置字长；

2. 在LPUART_CTL1寄存器中写STB[1:0]位来设置停止位的长度；

3. 如果选择了多级缓存通信方式，应该在LPUART_CTL2寄存器中使能DMA（DENR位）；

4. 在LPUART_BAUD寄存器中设置波特率；

5. 在LPUART_CTL0寄存器中置位UEN位，使能LPUART；

6. 在LPUART_CTL0中设置REN位。

接收器在使能后，RX线上有一个下降沿发生则检测到起始位，然后在起始位的中间进行采样以确认电平是否仍为0。若起始位采样为1，则噪声错误标志（NERR）置位，该起始位被忽略，如果设置了LPUART_CTL2寄存器中的ERRIE位则会产生一个中断。接收器在检测到一个有效的起始脉冲便开始接收码流。接收器在数据位的中间进行一次采样来评估该数据位的值，数据位的采样没有噪声检测。

当接收到一个数据帧，LPUART_STAT寄存器中的RBNE置位，如果设置了LPUART_CTL0寄存器中相应的中断使能位RBNEIE，将会产生中断。在LPUART_STAT寄存器中可以观察接收状态标志。

软件可以通过读LPUART_RDATA寄存器或者DMA方式获取接收到的数据。不管是直接读寄存器还是通过DMA，只要是对LPUART_RDATA寄存器的一个读操作都可以清除RBNE位。

在接收过程中，需使能REN位，不然当前的数据帧将会丢失。

通过置位LPUART_CTL0寄存器中的PCEN位使能奇偶校验功能，接收器在接收一个数据帧时计算预期奇偶校验值，并将其与接收到的奇偶校验位进行比较。如果不相等，LPUART_STAT寄存器中PERR被置位。如果设置了LPUART_CTL0寄存器中的PERRIE位，将产生中断。

如果在停止位传输过程中RX引脚为0，将产生帧错误，LPUART_STAT寄存器中FERR将置位。如果设置了LPUART_CTL2寄存器中的ERRIE位，将产生一个中断。当被配置为1个停止位时，在停止位的中间进行采样。当被配置为2个停止位时，在第二个停止位的中间进行采样，第一个停止位不检测帧错误。

当接收到一帧数据，而RBNE位还没有被清零，随后的数据帧将不会存储在数据接收缓冲区中。LPUART_STAT寄存器中的溢出错误标志位ORERR将置位。如果设置了LPUART_CTL2寄存器中ERRIE位或者RBNEIE位，将产生中断。

在一个接收过程中，NERR、PERR、FERR、ORERR总是分别和RBNE同时置位。如果没有使能DMA，软件需检查RBNE中断是否由NERR、PERR、FERR或者ORERR置位产生。

## 21.3.5. DMA方式访问数据缓冲区

为减轻处理器的负担，可以采用DMA访问发送缓冲区或者接收缓冲区。置位LPUART_CTL2寄存器中DENT位可以使能DMA发送，置位LPUART_CTL2寄存器中DENR位可以使能DMA接收。

当 DMA 用于 LPUART 发送时，DMA 将数据从片内 SRAM 传送到 LPUART 的数据缓冲区。配置步骤如 20-5. DMA USART 所示。


图 21-4. 采用 DMA 方式实现 LPUART 数据发送配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/66b16326c9da3bbc5b7fbba80abe38de60beaf6202aea5ddf27fd4a684e99b7c.jpg)


所有数据帧都传输完成后，LPUART_STAT寄存器中TC位置1。如果LPUART_CTL0寄存器中TCIE置位，将产生中断。

当 DMA 用于 LPUART 接收时，DMA 将数据从接收缓冲区传送到片内 SRAM。配置步骤如 20-6. DMA USART 所示。如果将 LPUART_CTL2 寄存器中 ERRIE 位置 1，LPUART_STAT 寄存器中的错误标志位（FERR、ORERR 和 NERR）置位时将产生中断。


图 21-5. 采用 DMA 方式实现 LPUART 数据接收配置步骤


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/7e210e1bbc79a9258fdcb391766e8e5cc5be3fcd3c1dc4844ed51d17c9b42230.jpg)



当LPUART接收到的数据数量达到了DMA传输数据数量，DMA模块将产生传输完成中断。


## 21.3.6. 硬件流控制

硬件流控制功能通过nCTS和nRTS引脚来实现。通过将LPUART_CTL2寄存器中RTSEN位置1来使能RTS流控，将LPUART_CTL2寄存器中CTSEN位置1来使能CTS流控。


图 21-6. 两个 LPUART 之间的硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/0cc5e1dd6819964f36551d19b2e7cfb3128388615678949de12944956ba8fffe.jpg)


## RTS 流控

LPUART接收器输出nRTS，它用于反映接收缓冲区状态。当一帧数据接收完成，nRTS变成高电平，这样是为了阻止发送器继续发送下一帧数据。当接收缓冲区满时，nRTS保持高电平。

## CTS 流控

LPUART发送器监视nCTS输入引脚来决定数据帧是否可以发送。如果LPUART_STAT寄存器中TBE位是0且nCTS为低电平，发送器发送数据帧。在发送期间，若nCTS信号变为高电平，发送器将会在当前数据帧发送完成后停止发送。


图 21-7. 硬件流控制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/fc9bcf1f7ff44cd66128f666022026aee71923e7a2583488b5232323ff209174.jpg)


## RS485 驱动使能

驱动使能功能通过设置LPUART_CTL2控制寄存器的DEM位来打开。它允许用户通过DE（Driver Enable）信号激活外部收发器控制。提前时间是驱动使能信号和第一个字节的起始位之间的时间间隔。这个时间可以在LPUART_CTL0控制器的DEA[4:0]位域中进行设置。滞后时间是一个发送信息最后一个字节的停止位与释放DE信号之间的时间间隔。这个时间可以在LPUART_CTL0控 制 寄 存 器的DED[4:0]位 域 中进 行 设 置 。DE信 号的 极 性 可 以 通 过LPUART_CTL2控制寄存器的DEP位进行设置。

LPUART的DEA和DED通过LPUCLK $( \mathsf { f } _ { \mathsf { c } \mathsf { k } } )$ 表示，如 21-2 所示：


表 21-2 驱动使能提前时间和滞后时间


<table><tr><td>BRR[14:11]</td><td>驱动使能提前时间</td><td>驱动使能滞后时间</td></tr><tr><td>BRR[14:11] = 0</td><td>(1+DEA) ×<eq>f_{ck}</eq></td><td>(1+DED) ×<eq>f_{ck}</eq></td></tr><tr><td>BRR[14:11] ≠ 0</td><td>(1+ (DEA×BRR[14:11]) ) ×<eq>f_{ck}</eq></td><td>(1+ (DED×BRR[14:11]) ) ×<eq>f_{ck}</eq></td></tr></table>

## 21.3.7. 多处理器通信

在多处理器通信中，多个LPUART被连接成一个网络。对于一个设备来说，监视所有来自RX引脚的消息，是一种巨大的负担。为减轻设备负担，用户可通过LPUART_CTL0寄存器中的MEN位使能静默模式，并将LPUART_CMD寄存器中MMCMD位置1使LPUART进入静默模式。

如果LPUART处于静默模式，所有的接收状态标志位将不会被置位。此外，LPUART可以由硬件用以下两种方式中的一种来唤醒：空闲总线检测和地址匹配检测。

设备默认使用空闲总线检测方法唤醒LPUART。如果RWU位为0，RX引脚检测到空闲帧，LPUART_STAT寄存器中的IDLEF位会置位。如果RWU位置位，RX引脚检测到空闲帧时，硬件会将RWU清零，从而退出静默模式，当它是被空闲帧唤醒时，LPUART_STAT寄存器中IDLEF位不会被置1。

当LPUART_CTL0寄存器中WM被置位，数据最高位会被认为是地址标志位。如果地址标志位为1，该字节被认为是地址字节。如果地址标志位是0，该字节被认为是数据字节。如果地址字节的低4位或低7位（通过LPUART_CTL1寄存器中ADDM位配置）与LPUART_CTL1寄存器中的ADDR位相同，硬件会将RWU清零，并退出静默模式。接收到将LPUART唤醒的数据帧，RBNE将置位。状态标志可以从LPUART_STAT寄存器中获取。如果地址字节的低4位或低7位与LPUART_CTL1寄存器中的ADDR位不相同，硬件会置位RWU并自动进入静默模式。在这种情况下，RBNE不会被置位。

如果LPUART_CTL0寄存器中PCEN位被置位，地址字节最高位被视为校验位，其余位被视为地址位。如果ADDM位被置位，且接收帧为7位的数据，其中最低的6位将与ADDR[5:0]比较。如果ADDM位被置位，且接收帧为9位的数据，其中低8位将与ADDR[7:0]进行比较。

注意：如果设置了MEN，WM位和RWU位被复位，RX引脚检测到空闲帧，IDLEF位会置位。如果RWU位置位，则IDLEF位不会置位。

## 21.3.8. 半双工通信模式

通过设置LPUART_CTL2寄存器的HDEN位，可以使能半双工模式。

半双工模式下仅用单线通信。TX引脚和RX引脚从内部连接到一起，TX引脚应被配置为IO管脚。通信冲突应由软件处理。当TEN被置位时，在数据寄存器中的数据将会被发送。

## 21.3.9. 从深度睡眠模式唤醒

通过标准RBNE中断或WUM中断LPUART能从深度睡眠模式唤醒MCU。

UESM位必须置1并且LPUART时钟必须设置为IRC16M或LXTAL（请参考 2RCU_CFG2 ）。当LPUART的时钟源被配置为IRC16M或LXTAL时，通过将LPUART_CTL2寄存器中的UCESM位置1，可以在深度睡眠模式下保持启用该时钟。

当使用RBNE标准中断时，必须在进入深度睡眠模式前将RBNEIE位置位。

当使用WUIE中断时，WUIE中断源可以通过WUM位来选择。

在进入深度睡眠模式前，必须禁用DMA。在进入深度睡眠模式前，软件必须检测LPUART是否正在传送数据。这可以通过LPUART_STAT寄存器中的BSY标志来判断。REA位必须被检测以确保LPUART是使能的。

当检测到唤醒事件时，无论MCU工作在深度睡眠模式还是正常模式，WUF标志位通过硬件被置1，并且在WUIE被置位的情况下，触发一个唤醒中断。

## 21.3.10. LPUART 中断

LPUART 中断事件和标志如 20-3. USART 所示：


表 21-3. LPUART 中断请求


<table><tr><td>中断事件</td><td>事件标志</td><td>使能控制位</td></tr><tr><td>发送数据寄存器空</td><td>TBE</td><td>TBEIE</td></tr><tr><td>CTS标志</td><td>CTSF</td><td>CTSIE</td></tr><tr><td>发送结束</td><td>TC</td><td>TCIE</td></tr><tr><td>接收到的数据可以读取</td><td>RBNE</td><td rowspan="2">RBNEIE</td></tr><tr><td>检测到过载错误</td><td>ORERR</td></tr><tr><td>检测到线路空闲</td><td>IDLEF</td><td>IDLEIE</td></tr><tr><td>奇偶校验错误</td><td>PERR</td><td>PERRIE</td></tr><tr><td>接收错误(噪声错误、溢出错误、帧错误)</td><td>NERR或ORERR或FERR</td><td>ERRIE</td></tr><tr><td>字符匹配</td><td>AMF</td><td>AMIE</td></tr><tr><td>从深度睡眠模式唤醒</td><td>WUF</td><td>WUIE</td></tr></table>


在发送给中断控制器之前，所有的中断事件是逻辑或的关系。因此在任何时候 LPUART 只能向控制器产生一个中断请求。不过软件可以在一个中断服务程序里处理多个中断事件。



图 21-8. LPUART 中断映射框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/67d32e5e55191599e4ef30b57d0904d2bdd0e5273b071b966d41ab11cb7028b7.jpg)
