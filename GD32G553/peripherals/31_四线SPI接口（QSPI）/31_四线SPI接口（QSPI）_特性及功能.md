## 31. 四线 SPI 接口（QSPI）

## 31.1 . 简介

QSPI是一种专用于和flash存储器通信的接口，可以支持单线，双线，四线SPI Flash。可以工作在普通模式、读轮询模式和内存映射模式。

## 31.2. 主要特征

 三种模式：普通模式（外部地址），读轮询模式和内存映射模式；

 可用于普通模式和内存映射模式的完全可编程的命令格式；

 集成用于接收和发送的FIFO；

 支持SDR和DDR模式；

 支持DQS信号；

 允许8位、16位或32位数据访问；

 普通模式支持DMA操作。

## 31.3. 功能描述

## 31.3.1. QSPI 结构框图

QSPI使用7根信号线和外部flash存储器连接，引脚在 31-1. QSPI 中描述。


表 31-1. QSPI 信号线描述


<table><tr><td>引脚</td><td>方向</td><td>描述</td></tr><tr><td>CSN</td><td>O</td><td>片选输出(低电平有效)</td></tr><tr><td>SCK</td><td>O</td><td>时钟输出</td></tr><tr><td>IO0/SO</td><td>I/O</td><td>单线模式:数据输出双线模式:数据输入或输出四线模式:数据输入或输出</td></tr><tr><td>IO1/SI</td><td>I/O</td><td>单线模式:数据输入双线模式:数据输入或输出四线模式:数据输入或输出</td></tr><tr><td>IO2</td><td>I/O</td><td>单线模式:连接flash的WP引脚,控制“写保护”功能双线模式:连接flash的WP引脚,控制“写保护”功能四线模式:数据输入或输出</td></tr><tr><td>IO3</td><td>I/O</td><td>单线模式:连接flash的HOLD引脚,控制“保持”功能双线模式:连接 flash 的 HOLD 引脚,控制“保持”功能四线模式:数据输入或输出</td></tr><tr><td>DQS</td><td>I</td><td>数据选通信号</td></tr></table>


QSPI 结构图框图如 31-1. QSPI 。



图 31-1. QSPI 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/0b353262422527e67f8d58fa46af8d25e9bdbb3d19e9085a97bdb8eec50ccfa5.jpg)


## 31.3.2. QSPI 命令格式

QSPI 使用不同格式的命令与 flash 存储器通信。一共最多有五个阶段：指令阶段、地址阶段、交替字节阶段、空指令阶段、数据阶段。任一阶段都可以跳过，但是至少需要包含指令阶段、地址阶段、交替字节、数据阶段的其中一个阶段，这是由软件保证，硬件设计没有任何保护方法。另外，命令的高位始终占用高位信号线。


图 31-2. QSPI 命令格式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/f08fb5a24bd1f43892bd3a64db1ec810030f8ca67314ead030da7441e52483a7.jpg)



命令和相应的配置如 31-2. QSPI 所示。



表 31-2. QSPI 命令描述


<table><tr><td>命令</td><td>发送信息</td><td>配置</td><td>注意</td></tr><tr><td>指令</td><td>8位指令</td><td>QSPI_TCFG寄存器定义指令和信号线模式</td><td>-</td></tr><tr><td>地址</td><td>1-4字节地址</td><td>QSPI_ADDR寄存器定义地址信息。QSPI_TCFG寄存器定义发送地址的字节数和信号线模式</td><td>-</td></tr><tr><td>交替字节</td><td>1-4交替字节</td><td>QSPI_ALTE寄存器定义交替字节信息,QSPI_TCFG寄存器定义交替字节的个数和信号线模式</td><td>-</td></tr><tr><td>空闲</td><td>0-31周期</td><td>QSPI_TCFG寄存器定义周期,DATAMOD位域(QSPI_TCFG寄存器)定义空闲信号线模式</td><td>这期间与外部存储器没有数据交互,等待外部存储器,准备数据。</td></tr><tr><td>数据</td><td>任意数量的字节</td><td>在普通模式下,QSPI_DTLEN寄存器定义字节数。DATAMOD位域(QSPI_TCFG寄存器)定义数据信号线模式,DATAMOD=00的配置只能在普通写模式下使用。</td><td>在内存映射模式下,传输的字节个数确定AHB总线的访问操作,可以8位,16位或者32位读写访问,相应传输1个,2个,4个字节。</td></tr></table>


注意：信号线模式可以为无指令，单线，双线或者四线。


## 31.3.3. QSPI 信号线的模式

对于 QSPI 的信号线模式，指令阶段、地址阶段、字节交替阶段、数据阶段都可以通过设置 IMOD/ ADDRMOD / ALTEMOD / DATAMOD 位域进行独立配置。


表 31-3. QSPI 信号线模式


<table><tr><td colspan="2">信号线模式</td><td>单线模式</td><td>双线模式</td><td>四线模式</td></tr><tr><td rowspan="4">配置位域</td><td>IMOD</td><td rowspan="4">01或者00</td><td rowspan="4">10或者00</td><td rowspan="4">11或者00</td></tr><tr><td>ADDRMOD</td></tr><tr><td>ALTEMOD</td></tr><tr><td>DATAMOD</td></tr><tr><td rowspan="4">引脚</td><td>IO0(SO)</td><td>输出</td><td rowspan="2">输入:数据阶段读操作(高阻状态)输出:所有其他阶段</td><td rowspan="4">输入:数据阶段读操作(高阻状态)输出:所有其他阶段</td></tr><tr><td>IO1(SI)</td><td>输入(高阻状态)</td></tr><tr><td>IO2</td><td colspan="2">输出0(禁止“写保护”功能)</td></tr><tr><td>IO3</td><td colspan="2">输出1(禁止“保持”功能)</td></tr><tr><td colspan="2">描述</td><td>DATAMOD=01时,空闲阶段IO0输出,IO1输入(高阻状态)。</td><td>DATAMOD=10时,空闲阶段IO0/IO1一直高阻状态。</td><td>DATAMOD=11时,空闲阶段IO0/IO1/IO2/IO3一直高阻状态。</td></tr></table>


IO2 / IO3 仅用于四线模式，如果五个阶段都没有配置为四线模式，IO2 / IO3 引脚被释放，即使QSPI 被使能也可以用于其他功能。


## QSPI 引脚

QSPI 最大支持 200M 时钟，但使用不同组的引脚支持的最高通信时钟频率不同，请参考 31-4.QSPI使用引脚与支持的最高通信时钟对应关系


表 31-4. QSPI 使用引脚与支持的最高通信时钟对应关系


<table><tr><td>引脚功能</td><td>最高时钟 120M</td><td>最高时钟 120M</td><td>最高时钟 200M</td><td>最高时钟 120M</td></tr><tr><td>QSPI_CSN</td><td>PA2</td><td>PB11\PE11</td><td>PD3</td><td>PA2</td></tr><tr><td>QSPI_SCK</td><td>PA3</td><td>PB10\PE10</td><td>PD2</td><td>PF10</td></tr><tr><td>QSPI_IO0</td><td>PB1</td><td>PE12</td><td>PD4</td><td>PC1\PF8</td></tr><tr><td>QSPI_IO1</td><td>PB0\PB2</td><td>PE13</td><td>PD5</td><td>PC2\PF9</td></tr><tr><td>QSPI_IO2</td><td>PA7</td><td>PE14</td><td>PD6</td><td>PC3\PF7</td></tr><tr><td>QSPI_IO3</td><td>PA6\PC4</td><td>PE15</td><td>PD7</td><td>PF6</td></tr><tr><td>QSPI_DQS</td><td>PB7</td><td>PB7</td><td>PD1</td><td>PB7</td></tr></table>


注意：强烈推荐按组使用引脚，否则无法保证 QSPI 支持的最大通信时钟频率。


## 31.3.4. QSPI DDR 模式

默认情况下，QSPI 工作在 SDR（单倍数据速率）模式，当 QSPI_TCFG 寄存器 DDREN 位置 1时，QSPI 工作在 DDR 模式（双倍数据速率）下。DDR 模式下，地址 / 字节交替 / 数据阶段，IO0、IO1、IO2、IO3 信号均在 SCK 信号的两个时钟沿（上升沿和下降沿）传输数据，指令阶段仍采用 SDR 模式传输，IO0、IO1、IO2、IO3 信号在 SCK 的下降沿采样。


图 31-3. QSPI DDR 模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/abb8a184cd9070bc7647c5c629cce587b983658341dcc1e453e96010f78dd005.jpg)


在 DDR 模式时，根据实际使用需求，可能需要通过设置 QSPI_DCFG 寄存器中 DLYSCEN 位为1 使用 CPDM 微调 QSPI 接收时钟相位。请参考 CPDM 。

## 31.3.5. DQS 信号

DQS信号通常用于高速应用程序，以指示何时存储器的输出数据可被MCU读取。开启DQS功能时，频率与SCK频率相同。对于SDR读取操作，数据只能锁存在DQS信号的上升沿上。对于DDR读操作，数据应该锁存在DQS信号的上升沿和下降沿。


图 31-4. 使用 DQS 信号 DDR 模式读


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/e2f6d9031369faa48ac181c61c9340d99e4b87645296cbe81c1e9b9af8be222c.jpg)


## 31.3.6. CSN 和 SCK 的行为

CSN 默认为高电平，它在命令开始时拉低，结束时拉高。

SCK 是从内部 sck 信号输出的一个门信号，内部 sck 信号是一直存在的。

为了适应一些高速设备，QSPI 支持通过配置 QSPI_DCFG 寄存器中 CSNCKM 位选择 CSN 在第一个SCK有效上升沿的之前一个或者两个SCK时钟周期拉低及在最后一个SCK有效上升沿之后

一个或者两个 SCK时钟周期拉高。


图 31-5. CSN 和 SCK 的行为（CSNCKM = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/b7c728b600f4316e223e16d691f3a5dcac093968475dd1a7ac0fc4348cbfff1d.jpg)


当 FIFO 在写操作时为空或者读操作时为满，SCK 会停止并且保持低电平直到 FIFO 可以再次工作。在这时，如果 CSN 为高电平，SCK会在 CSN 上升沿之后的半个 SCK 时钟周期拉高电平。

## 31.4. 操作模式

QSPI 可以工作在普通模式、读轮询模式和内存映射模式。在普通模式下，所有的操作都依赖于QSPI 寄存器。在读轮询模式下，定时读取并检查外部闪存存储器中的状态寄存器值。在内存映射模式下，外部闪存被映射到微控制器地址空间（范围从 0x9000 0000 到 0x9FFF FFFF），并作为内部存储器访问。

## 31.4.1. 普通模式

普通模式写操作是通过将 QSPI_TCFG 寄存器中的 FMOD[1:0]为“00”来选择的。待传输的数据写入 QSPI_DATA。通过将 QSPI_TCFG 寄存器中的 FMOD[1:0]设置为“01”，选择普通模式读操作，接收的数据从 QSPI_DATA 读取。

QSPI_DTLEN 寄存器中的 DTLEN[31:0]定义了待传输的字节数。如果 DTLEN 是 0xFFFF FFFF，则认为传输的字节数是未定义的，在传输字节数达到 QSPI_DCFG 寄存器中 FMSZ[4:0]规定的存储器大小边界时停止传输。如果 DTLEN 为 0xFFFF FFFF 且 FMSZ[4:0]被配置为 0x1F 时，闪存存储器容量为 4GB，传输会一直持续到发生中止请求或 QSPI 被禁用。

当传输数据的字节数达到 DTLEN 寄存器中设定的值时，传输完成标志 TC 会被置 1。如果 DTLEN为 0xFFFFFFFF，则发送 / 接收字节数等于 FMSZ[4:0]规定的外部存储器大小时，TC 会被置 1。如果 TCIE和 TC 都被置 1，则会产生中断，通过将 QSPI_STATC 寄存器的 TCC 位置 1 可以清除TC 位。

## 初始化一个命令序列

命令序列在根据通信需求配置好最后信息之后立即开始。

当没有地址并且没有数据时，在访问 QSPI_TCFG 寄存器之后立即开始命令序列。

当存在地址但没有数据时，在访问 QSPI_ADDR 寄存器之后立即开始命令序列。

当在普通模式写操作时需要地址并且有数据，在访问QSPI_DATA寄存器之后立即开始命令序列。

## FIFO

16 字节的 FIFO 用于传输数据。在普通模式写操作时，AHB 写访问方式与 FIFO 增加的字节数的关系如 31-5. AHB FIFO 所示。


表 31-5. AHB 写访问方式与 FIFO 增加的字节数的关系


<table><tr><td>AHB 写访问方式</td><td>FIFO 增加的字节数</td></tr><tr><td>32 位</td><td>4 字节</td></tr><tr><td>16 位</td><td>2 字节</td></tr><tr><td>8 位</td><td>1 字节</td></tr></table>

注意：当 AHB 写访问模式为 8 位或 16 位时，QSPI_DATA 寄存器中最低有效字节是有效的。

FIFO 阈值由 QSPI_CTL 寄存器中的 FTL[3:0]定义，在普通模式读操作时，当 FIFO 中的字节数等于者超过定义的阈值时，QSPI_STAT 寄存器中的 FIFO 阈值标志 FT 将置 1。在数据阶段完成后如果 FIFO 不为空，FT 也会被置 1。在普通模式写操作时，当 FIFO 的空字节数超过阈值时，FT会被置 1。

如果 FTIE和 FT 都被置 1，将产生中断。如果 QSPI DMA使能，DMA请求由 FT 产生，直到标志清除。

在普通模式读操作时，当 FIFO 变为满时，QSPI 暂时停止 SCK 以避免溢出。读序列不能恢复直到FIFO 中有大于等于 4 个字节剩余空间。

## 31.4.2. 读轮询模式

通过将 FMOD[1:0]配置为“10”可以来选择读轮询模式。在读轮询模式下，QSPI 周期性地启动一个读命令，其中最多包含 4 字节的数据。接收到的数据可以按位屏蔽，并与定义的数据内容进行比较，如果匹配发生，且 RPMFIE 位置 1，将生成一个中断。

读轮询访问序列的启动与普通模式读操作相同。在周期性间隔时 BUSY位保持高电平。

轮询匹配模式位 RPMM 控制比较匹配模式，如果 RPMM = 0，与模式被选择。在该模式下，只在所有的未屏蔽位都有匹配时，状态匹配标志 RPMF 将置 1。如果 RPMM = 1，或模式被选择。在该模式下，任何非屏蔽位只要有一位匹配，RPMF 将置 1。

在读轮询模式下，如果设置了 RPMS 位，当检测到匹配时，读轮询序列将停止，并在数据阶段结束时清除 BUSY标志。否则，周期序列将继续，直到 ABORT 位置 1 或 QSPI 被关闭。

在读轮询模式下，FIFO 是避开的，读取的状态字节存放在 QSPI_DATA 中，存储的状态字节不会被 MASK 控制域影响。如果有数据阶段，QSPI_DATA 中内容在数据阶段开始时更新。

如果 FT 位在数据阶段结束时被置位，此时认为外部闪存状态字节已经被读取，读取 QSPI_DATA清除 FT 位。

## 31.4.3. 内存映射模式

通过将 FMOD[1:0]配置为“11”，可以选择内存映射模式。在内存映射模式下，外部闪存被认为是内部存储器来访问，最大访问地址为 256MB，即使外部闪存大于 256MB。即使 FMSZ 定义的地址范围在 256MB 范围内，内存映射模式也不允许地址超过 FMSZ 定义的范围。否则，将生成一个错误。如果 AHB 主机是 CPU，会产生硬故障中断。如果 AHB 主机是 DMA，将产生一个传输错误，并且相应 DMA 通道会关闭。

在该模式下，支持字节、半字、字单次访问或突发访问。

内存映射模式支持顺序访问时的预取功能。QSPI 在访问数据之前会首先在下一个地址加载数据，如果下次访问确实是在下一个地址，那么访问速度会更快，因为数据已经被预取了。否则，将重新启动读取序列。在读取序列开始之前拉低 CSN。

当 FIFO 满时，SCK 停止输出，在此期间 CSN 保持低电平。如果 QSPI_CTL 寄存器中 TMOUTEN位置 1，当低电平的持续时间达到 QSPI_TMOUT 寄存器中指定的 SCK时钟周期数时，CSN 将被拉高。

在开始传输时，在 CSN 拉低之前 BUSY位会变为高电平，在发生超时、中止或者 QSPI 被关闭后变为低电平。

## 31.5. QSPI 配置

## 31.5.1. Flash 配置

QSPI_DCFG 寄存器的配置可以用来指定外部闪存存储器的特性，从而使 QSPI 可以持续工作。

QSPI_DCFG 寄存器中 FMSZ[4:0]定义了外部存储器大小，FMSZ+1 是外部存储器的地址位数。在普通模式下，flash 容量最大可达 4GB。

CSHC[2:0]定义了片选高电平时间，它规定了在两个命令序列之间保持高电平最少的 SCK 周期数。

## 31.5.2. IP 配置

QSPI_CTL 寄存器中的配置可以用来指定 QSPI IP 的特征。

QSPI_CTL 寄存器中 PSC[7:0]定义了时钟分频系数。

SSAMPLE 定义哪个 SCK 边沿用于采样数据。默认情况下，QSPI 在外部存储器驱动数据后的半个 SCK 周期采样数据。然而，因为外部信号的延迟，需要推迟采样数据。采样边沿可以使用SSAMPLE 移位半个 SCK 周期。

通过在 QSPI_STAT 寄存器中设置 DMAEN 位来启用 DMA 请求。在 QSPI_CTL 寄存器中设置FTL[3:0]位来配置 FIFO 阈值等级。

## 31.6. 只发送一次指令

将 QSPI_TCFG 寄存器中 SIOO 位置 1，可以使能只发送一次指令模式，该功能对所有模式有效。如果 SIOO 置 1，在访问 QSPI_TCFG 后该指令只发送一次，后续命令序列会跳过指令阶段，直到QSPI_TCFG 再次被访问。

## 31.7. 错误和中断

当 31-6. TERR AHB 中一个条件发生时，会产生 TERR 和 AHB 错误。


表 31-6. TERR 和 AHB 错误条件


<table><tr><td>错误名称</td><td>条件</td></tr><tr><td>TERR</td><td>1. 在普通模式或者读轮询模式下,超出FMSZ规定的地址范围,在QSPI_ADDR寄存器中编写了一个错误的地址。2. 在普通模式下,地址(ADDR)加数据长度(DTLEN)大于外部内存。</td></tr><tr><td>AHB错误</td><td>1. 在内存映射模式下,AHB主机执行超出范围访问,或QSPI被关闭。2. AHB主机正在访问内存映射空间,但内存映射模式未使能。</td></tr></table>


QSPI 中断事件和标志如 31-7. QSPI 所示。



表 31-7. QSPI 中断事件


<table><tr><td>中断事件</td><td>事件标志</td><td>中断使能位</td><td>清除方式</td></tr><tr><td>FIFO阈值中断</td><td>FT</td><td>FTIE</td><td>硬件清除</td></tr><tr><td>传输完成中断</td><td>TC</td><td>TCIE</td><td>QSPI_STATC寄存器中TCC位置1</td></tr><tr><td>传输错误中断</td><td>TERR</td><td>TERRIE</td><td>QSPI_STATC寄存器中TERRC位置1</td></tr><tr><td>超时中断</td><td>TMOUT</td><td>TMOUTIE</td><td>QSPI_STATC寄存器中TMOUTC位置1</td></tr><tr><td>状态匹配中断</td><td>RPMF</td><td>RPMFIE</td><td>QSPI_STATC寄存器中RPMFC位置1</td></tr></table>
