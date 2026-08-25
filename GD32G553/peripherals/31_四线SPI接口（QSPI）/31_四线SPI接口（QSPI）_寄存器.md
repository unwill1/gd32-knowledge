## 31.8. QSPI 寄存器

QSPI 访问基地址：0xA000 1000

## 31.8.1. 控制寄存器（QSPI_CTL）

地址偏移：0x00

复位值：0x0000 0010

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">PSC[7:0]</td><td>RPMM</td><td>RPMS</td><td>保留</td><td>TMOUTIE</td><td>RPMFIE</td><td>FTIE</td><td>TCIE</td><td>TERRIE</td></tr><tr><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">OCKDV[3:0]</td><td colspan="4">FTL[3:0]</td><td colspan="2">保留</td><td>OCKDEN</td><td>SSAMPLE</td><td>TMOUTEN</td><td>DMAEN</td><td>ABORT</td><td>QSPIEN</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>w1s</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>PSC[7:0]</td><td>该位域定义了从AHB时钟分频产生QSPI时钟的分频因子。SCK和AHB之间的频率关系为:<eq>f_{SCK}=f_{AHB}/(PSC+1)</eq>.00000000:<eq>f_{SCK}=f_{AHB}</eq>00000001:<eq>f_{SCK}=f_{AHB}/2</eq>00000010:<eq>f_{SCK}=f_{AHB}/3</eq>...11111111:<eq>f_{SCK}=f_{AHB}/256</eq>对于奇数时钟分频因子,时钟的占空比没有50%,时钟信号保持低电平时间要比高电平时间少一个周期。该位只能在BUSY=0时才能修改。</td></tr><tr><td>23</td><td>RPMM</td><td>读轮询匹配模式该位表明在读轮询时采用什么方式定义产生匹配0:与模式,如果flash返回的字节所有非屏蔽位都和QSPI_STATMATCH寄存器相应位匹配,状态匹配标志RPMF被置位。1:或模式,如果flash返回的字节任何一个非屏蔽位都和QSPI_STATMATCH寄存器相应位匹配,状态匹配标志RPMF被置位。该位只能在BUSY=0时修改。</td></tr><tr><td>22</td><td>RPMS</td><td>读轮询模式停止该位表明在产生匹配后停止读轮询模式0:在ABORT置位或者禁能QSPI模块时读轮询停止。1:在产生匹配后读轮询停止。该位只能在BUSY=0时修改。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>TMOUTIE</td><td>超时中断使能0:中断禁能1:中断使能</td></tr><tr><td>19</td><td>RPMFIE</td><td>读轮询模式匹配中断使能0:中断禁能1:中断使能</td></tr><tr><td>18</td><td>FTIE</td><td>FIFO阈值中断使能0:中断禁能1:中断使能</td></tr><tr><td>17</td><td>TCIE</td><td>传输完成中断使能0:中断禁能1:中断使能</td></tr><tr><td>16</td><td>TERRIE</td><td>传输错误中断使能0:中断禁能1:中断使能</td></tr><tr><td>15:12</td><td>OCKDV[3:0]</td><td>输出时钟延时值该位域仅在OCKDEN使能时有效。输出时钟延迟功能仅在QSPI时钟不分频时生效。</td></tr><tr><td>11:8</td><td>FTL[3:0]</td><td>FIFO阈值等级该位在普通模式下使用,FIFO中的字节数会触发FIFO阈值标志被置位。普通模式写操作时(FMOD=00):0000:FT会被置位,如果有1个或者更多字节可以有效写入FIFO0001:FT会被置位,如果有2个或者更多字节可以有效写入FIFO...1111:FT会被置位,如果有16个字节可以有效写入FIFO普通模式读操作时(FMOD=01):0000:FT会被置位,如果有1个或者更多有效数据能从FIFO中读取0001:FT会被置位,如果有2个或者更多有效数据能从FIFO中读取...1111:FT会被置位,如果有16个有效数据能从FIFO中读取如果DMAEN为1,在改变FTL之前,DMA控制器的相应通道必须禁能。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>OCKDEN</td><td>向flash写数据时输出SCK延时使能0:SCK延时禁能1:SCK延时使能</td></tr><tr><td>4</td><td>SSAMPLE</td><td>采样延时默认情况下,QSPI在FLASH存储器驱动数据后二分之一个SCK时钟周期采样。考虑到外部信号的延迟,该位域可以配置为允许数据稍后对数据进行采样。0:不延时1:延时半个周期该位只能在BUSY=0时才能被修改。</td></tr><tr><td>3</td><td>TMOUTEN</td><td>超时计数器使能在内存映射模式(FMOD=11)下,如果将该位置1,且在TMOUTCYC[15:0]定义的时间之后,没有访问外部flash,片选(CSN)会释放。0:超时计数器失能,在内存映射模式下访问后片选(CSN)保持低电平1:超时计数器使能,在内存映射模式下,如果flash在超过TMOUTCYC[15:0]个周期后没有访问外部flash,片选(CSN)会释放。该位只能在BUSY=0时修改。</td></tr><tr><td>2</td><td>DMAEN</td><td>DMA使能普通模式下,可以使用DMA传输数据。当FT位置1时,DMA传输开始。0:DMA禁能1:DMA使能</td></tr><tr><td>1</td><td>ABORT</td><td>终止请求该位停止当前命令,终止请求完成后会自动清除。读轮询模式或者内存映射模式,如果将该位置1,RPMS位或者DMEN位被清除。0:无终止请求1:终止请求</td></tr><tr><td>0</td><td>QSPIEN</td><td>使能QSPI0:QSPI禁能1:QSPI使能</td></tr></table>

## 31.8.2. 设备配置寄存器（QSPI_DCFG）

地址偏移：0x04

复位值：0x001F 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>CSNCKM</td><td colspan="9">保留</td><td colspan="5">FMSZ[4:0]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="3">CSHC[2:0]</td><td colspan="2">保留</td><td>DLYSCEN</td><td>RCKSEL</td><td colspan="3">RXSFT[2:0]</td><td>CKMOD</td></tr><tr><td colspan="5"></td><td colspan="3">rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>CSNCKM</td><td>选择CSN在第一个SCK有效上升沿的之前一个还是两个SCK时钟周期拉低和在最后一个SCK有效上升沿之后一个还是两个SCK时钟周期拉高。0:1个SCK周期1:2个SCK周期</td></tr><tr><td>29:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>FMSZ[4:0]</td><td>flash存储器大小该位域定义外部存储器大小:Flash存储器字节数为<eq>2^{[FMSZ+1]}</eq>FMSZ+1是flash存储器地址位数。普通模式下,flash存储器容量最大到4GB。在内存映射模式下,最大256MB。该位只能在BUSY=0时修改。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:8</td><td>CSHC[2:0]</td><td>片选高电平周期数CSHC+1定义了在两个命令序列之间保持高电平最少的SCK周期数000:CSN保持高电平至少1个SCK周期001:CSN保持高电平至少2个SCK周期...111:CSN保持高电平至少8个SCK周期该位只能在BUSY=0时修改。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>DLYSCEN</td><td>延迟扫描功能使能0:禁能1:使能注意:该位仅在RCKSEL=0时生效。该位使能SCK相位微调功能,通过CPDM模块实现。CPDM调整时钟完成后,需再设置DLYSCEN=0。</td></tr><tr><td>4</td><td>RCKSEL</td><td>接收时钟选择0:SCK1:DQS选择接收时钟源为QSPI内部产生的SCK还是外部设备提供的DQS。当选择DQS时钟时,也可以使用CPDM进行时钟调整,而且不需要将DLYSCEN位置位。</td></tr><tr><td>3:1</td><td>RXSFT[2:0]</td><td>接收移位步长,数据延长超过0.5个周期时。</td></tr><tr><td></td><td></td><td>000:不延迟</td></tr><tr><td></td><td></td><td>001:1个周期</td></tr><tr><td></td><td></td><td>010:2个周期</td></tr><tr><td></td><td></td><td>011:3个周期</td></tr><tr><td></td><td></td><td>100:4个周期</td></tr><tr><td></td><td></td><td>101:5个周期</td></tr><tr><td></td><td></td><td>110:6个周期</td></tr><tr><td></td><td></td><td>111:7个周期</td></tr><tr><td></td><td></td><td>该位域可和SSAMPLE位一起调整接收采样点。</td></tr><tr><td>0</td><td>CKMOD</td><td>该位表明QSPI空闲时SCK电平</td></tr><tr><td></td><td></td><td>0:当CSN为高时,SCK保持低电平</td></tr><tr><td></td><td></td><td>1:当CSN为高时,SCK保持高电平</td></tr><tr><td></td><td></td><td>该位只能在BUSY=0时修改。</td></tr></table>

## 31.8.3. 状态寄存器（QSPI_STAT）

地址偏移：0x08

复位值：0x0000 0004

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="5">FL[4:0]</td><td colspan="2">保留</td><td>BUSY</td><td>TMOUT</td><td>RPMF</td><td>FT</td><td>TC</td><td>TERR</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>FL[4:0]</td><td>FIFO等级该位域给出FIFO在普通模式下存储的有效字节数。在内存映射模式和读轮询模式下,FL为0。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>BUSY</td><td>忙状态flash该位在命令传输时设置。在普通模式下,当一次操作完成后,该位将被清除。如果在普通读模式下,FIFO也必须为空。</td></tr><tr><td>4</td><td>TMOUT</td><td>超时标志当TMOUTEN被设置并且在TMOUTCYC[15:0]个周期之后没有访问闪存时,该位置1。</td></tr><tr><td>3</td><td>RPMF</td><td>读轮询匹配标志在读轮询模式下,当接收到数据匹配QSPI_STATMATCH寄存器中期望值时,该位置1。</td></tr><tr><td>2</td><td>FT</td><td>FIFO阈值标志在普通模式下,当FIFO阈值到达或者最后一次读操作时FIFO非空,该位置1。在阈值条件不再满足时由硬件清0。在读轮询模式下,每次从外部flash读取状态寄存器时置位,DATA寄存器被读取时清0。</td></tr><tr><td>1</td><td>TC</td><td>传输完成标志在普通模式下,当QSPI_DTLEN寄存器中已编程的数据长度以普通模式或终止操作完成时,该位置1。</td></tr><tr><td>0</td><td>TERR</td><td>传输错误标志在普通模式下,当访问了无效地址时,该位置1。</td></tr></table>

## 31.8.4. 状态清除寄存器（QSPI_STATC）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>TMOUTC</td><td>RPMFC</td><td>保留</td><td>TCC</td><td>TERRC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td></td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TMOUTC</td><td>清除超时标志对该位写1清除QSPI_STAT寄存器的TMOUT标志。</td></tr><tr><td>3</td><td>RPMFC</td><td>清除读轮询匹配标志对该位写1清除QSPI_STAT寄存器的RPMF标志。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>1</td><td>TCC</td><td>清除传输完成标志对该位写1清除QSPI_STAT寄存器的TC标志。</td></tr><tr><td>0</td><td>TERRC</td><td>清除传输错误标志对该位写1清除QSPI_STAT寄存器的TERR标志。</td></tr></table>

## 31.8.5. 数据长度寄存器（QSPI_DTLEN）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DTLEN[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DTLEN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DTLEN[31:0]</td><td>数据长度该位域指定在普通模式和读轮询模式下要传输的数据的个数n(值+1)。在读轮询模式下,该位域的值应该是一个不大于3(表示4字节)的值。在普通模式下,如果该位域配置为0xFFFF FFFF,表示未定义的长度,QSPI将继续传输数据,直到QSPI_DCFG寄存器中的FMSZ[4:0]定义内存地址结束。0x0000 0000:待传输字节数为10x0000 0001:待传输字节数为20x0000 0002:待传输字节数为30x0000 0003:待传输字节数为4...0xFFFF FFFD:待传输字节数为4,294,967,294 (4G-2)0xFFFF FFFE:待传输字节数为4,294,967,295 (4G-1)0xFFFF FFFF:未定义长度,QSPI_DCFG寄存器中由FMSZ[4:0]定义的所有字节,直到内存结束都将被传输。如果FMSZ[4:0]为0x1F,将无限地继续读取。内存映射模式下,该位无影响。该位只能在BUSY = 0时修改。</td></tr></table>

## 31.8.6. 传输配置寄存器（QSPI_TCFG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DDREN</td><td>DDRHEN</td><td>保留</td><td>SIOO</td><td colspan="2">FMOD</td><td colspan="2">DATAMOD[1:0]</td><td>保留</td><td colspan="5">DUMYC[4:0]</td><td colspan="2">ALTESZ[1:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td></td><td></td><td colspan="4">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ALTEMOD[1:0]</td><td colspan="2">ADDRSZ[1:0]</td><td colspan="2">ADDRMOD[1:0]</td><td colspan="2">IMOD[1:0]</td><td colspan="8">INSTRUCTION[7:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td></td><td></td><td colspan="4">rw</td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DDREN</td><td>双倍传输速率模式使能0:禁能1:使能</td></tr><tr><td>30</td><td>DDRHEN</td><td>DDR输出保持使能在 DDR 模式下,延迟1/4个QSPI输出时钟周期再输出数据0:禁能1:使能在 QSPI 分频时使用。</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>SIOO</td><td>只发送一次指令模式当IMOD = 00时,该位没有影响。0:每次命令序列都发送指令1:命令序列第一次时发送指令该位只能在BUSY = 0时修改。</td></tr><tr><td>27::26</td><td>FMOD[1:0]</td><td>工作状态00:普通模式写操作01:普通模式读操作10:读轮询模式11:内存映射模式如果DMAEN位置1,在改变FMOD位域之前,DMA控制器的相应通道必须关闭。该位域只能在BUSY = 0时修改。</td></tr><tr><td>25:24</td><td>DATAMOD[1:0]</td><td>数据模式该位定义数据阶段的操作模式。00:无数据01:单线传输数据10:双线传输数据11:四线传输数据</td></tr></table>

<table><tr><td></td><td></td><td>该位同时决定空闲阶段操作模式该位域只能在BUSY=0时修改。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:18</td><td>DUMYC[4:0]</td><td>空指令周期数该位域定义空闲阶段持续时间。该位域只能在BUSY=0时修改。</td></tr><tr><td>17:16</td><td>ALTESZ[1:0]</td><td>交替字节大小00:8位交替字节01:16位交替字节10:24位交替字节11:32位交替字节该位域只能在BUSY=0时修改。</td></tr><tr><td>15:14</td><td>ALTEMOD[1:0]</td><td>交替字节模式00:无交替字节01:单线传输交替字节10:双线传输交替字节11:四线传输交替字节该位域只能在BUSY=0时修改。</td></tr><tr><td>13:12</td><td>ADDRSZ[1:0]</td><td>地址大小00:8位地址01:16位地址10:24位地址11:32位地址该位域只能在BUSY=0时修改。</td></tr><tr><td>11:10</td><td>ADDRMOD[1:0]</td><td>地址模式00:无地址01:单线传输地址10:双线传输地址11:四线传输地址该位域只能在BUSY=0时修改。</td></tr><tr><td>9:8</td><td>IMOD[1:0]</td><td>命令模式00:无指令01:单线传输指令10:双线传输指令11:四线传输指令该位域只能在BUSY=0时修改。</td></tr></table>

7:0 

INSTRUCTION[7:0] 指令

发送到flash存储器的命令信息。

该位域只能在BUSY = 0时修改。

## 31.8.7. 地址寄存器（QSPI_ADDR）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR [31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR [31:0]</td><td>地址发送到flash存储器的访问地址。当BUSY=0或在内存映射模式下,对该位域写入值将被忽略。</td></tr></table>

## 31.8.8. 交替字节寄存器（QSPI_ALTE）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ALTE[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALTE [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ALTE [31:0]</td><td>交替字节紧随地址之后,发送给flash存储器的可选数据。该位只能在BUSY = 0时修改。</td></tr></table>

## 31.8.9. 数据寄存器（QSPI_DATA）

地址偏移：0x20

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>将要与flash存储器交互的数据。在普通模式下写操作时,在发送到flash存储器之前,写入到该寄存器数据会被存储到FIFO中。如果FIFO为满,写操作会停止直到FIFO有足够空间。在普通模式下读操作时,读该寄存器获取从flash存储器接收的数据。如果FIFO没有足够的字节数来满足读命令请求,并且BUSY位为1,那么读操作会被停止直到FIFO中有足够的数据或者传输已经完成。在读轮询模式下,该寄存器包含从flash读取的最后数据。</td></tr></table>

## 31.8.10. 状态屏蔽寄存器（QSPI_STATMK）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MASK[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MASK [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MASK[31:0]</td><td>读轮询模式下状态屏蔽读轮询模式下从flash接收的状态字节掩码。对于MASK[31:0]第n位:0:接收数据的第n位不参与匹配1:接收数据的第n位参与匹配</td></tr></table>

该位域只能在BUSY = 0时修改。

## 31.8.11. 状态匹配寄存器（QSPI_STATMATCH）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MATCH[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MATCH[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MATCH[31:0]</td><td>读轮询模式下状态匹配与QSPI_STATMK寄存器中值进行比较匹配的期望值。该位域只能在BUSY = 0时修改。</td></tr></table>

## 31.8.12. 间隔寄存器（QSPI_INTERVAL）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INTERVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>INTERVAL[15:0]</td><td>间隔周期读轮询模式下两次读命令之间的SCK周期数。该位域只能在BUSY = 0时修改。</td></tr></table>

## 31.8.13. 超时寄存器（QSPI_TMOUT）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TMOUTCYC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>TMOUTCYC[15:0]</td><td>超时周期当内存映射模式,FIFO满时,该位域表明在下次访问到来时片选保持低电平的SCK周期数。该位域只能在BUSY=0时修改。注意:该位域不能设置为0,如果超时功能打开。</td></tr></table>

## 31.8.14. FIFO 刷新寄存器（QSPI_FLUSH）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>FLUSH</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>FLUSH</td><td>用于刷新所有内部FIFO</td></tr></table>
