# 29.10. OSPI 寄存器

OSPI0基地址：0x5200 5000

OSPI1基地址：0x5200 A000

# 29.10.1. 控制寄存器（OSPI_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">FMOD[1:0]</td><td colspan="4">保留</td><td>SPMOD</td><td>SPS</td><td colspan="2">保留</td><td>SMIE</td><td>FTIE</td><td>TCIE</td><td>TERRIE</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="5">FTL[4:0]</td><td colspan="5">保留</td><td>DMAEN</td><td>保留</td><td>OSPIEN</td></tr><tr><td colspan="3"></td><td colspan="5">rw</td><td colspan="5"></td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>FMOD[1:0]</td><td>功能模式00:间接写入模式。01:间接读取模式。10:状态轮询模式。11:内存映射模式。当DMAEN位为1,在更改该位域之前必须禁止相应通道的DMA控制器。</td></tr><tr><td>27:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>SPMOD</td><td>状态轮询匹配模式0:与模式,如果存储器返回的字节所有非屏蔽位都和匹配寄存器相应位匹配,状态匹配标志SM被置位。1:或模式,如果存储器返回的字节任何一个非屏蔽位都和匹配寄存器相应位匹配,状态匹配标志SM被置位。</td></tr><tr><td>22</td><td>SPS</td><td>状态轮询模式停止该位表明在产生匹配后停止状态轮询模式。0:保留1:在产生匹配后自动轮询停止。</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>SMIE</td><td>状态匹配中断使能0:禁用状态匹配中断。1:使能状态匹配中断。</td></tr><tr><td>18</td><td>FTIE</td><td>FIFO阈值中断使能0:禁用FIFO阈值中断。1:使能FIFO阈值中断。</td></tr><tr><td>17</td><td>TCIE</td><td>传输完成中断使能0:禁用传输完成中断。1:使能传输完成中断。</td></tr><tr><td>16</td><td>TERRIE</td><td>传输错误中断使能。0:禁用传输错误中断使能。1:使能传输错误中断使能。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>FTL[4:0]</td><td>FIFO阈值等级该位在间接模式下使用,FIFO中的字节数会触发FIFO阈值标志置位。间接模式写操作时(FMOD=00):0:如果有1个或者更多字节可以有效写入FIFO,FT置位。1:如果有2个或者更多字节可以有效写入FIFO,FT置位。...31:如果有32个字节可以有效写入FIFO,FT置位。间接模式读操作时(FMOD=01):0:如果有1个或者更多有效数据能从FIFO中读取,FT置位。1:如果有2个或者更多有效数据能从FIFO中读取,FT置位。...31:如果有32个有效数据能从FIFO中读取,FT置位。如果DMAEN为1,在改变FTL之前,DMA控制器的相应通道必须是禁用的。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>DMAEN</td><td>DMA使能间接模式下,可以使用DMA通过OSPI_DATA寄存器传输数据。当FT位置1时,DMA传输开始。0:DMA禁用。1:DMA使能。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>OSPIEN</td><td>使能OSPI0:禁用OSPI。1:使能OSPI。</td></tr></table>

# 29.10.2. 设备配置寄存器 0（OSPI_DCFG0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td colspan="3">DTYSEL[2:0]</td><td colspan="3">保留</td><td colspan="5">MESZ[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">CSHC[5:0]</td><td colspan="8">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>DTYSEL[2:0]</td><td>选择设备类型000: Micron模式,DTR 8数据位模式下按D0/D1排序。八线/四线/双线/单线模式下的常规SPI协议。001: Macronix模式,DTR 8数据位模式下按D1/D0排序。八线/四线/双线/单线模式下的常规SPI协议。010: 标准模式。011: Macronix RAM模式,DTR 8位数据模式下D1/D0排序。具有专用地址映射的八线/四线/双线/单线模式下的常规SPI协议。其它: 保留。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>MESZ[4:0]</td><td>存储器大小该位定义外部存储器大小,使用下列公式:存储器字节数 = <eq>2^{[MESZ+1]}</eq>。MESZ+1是存储器地址位数。间接模式下,存储器容量最大到4GB。在内存映射模式下,最大256MB。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>CSHC[5:0]</td><td>片选高电平周期数CSHC+1定义了在两个命令序列之间CSN保持高电平最少的SCK周期数。0: CSN保持高电平至少1个SCK周期。1: CSN保持高电平至少2个SCK周期。...63: CSN保持高电平至少64个SCK周期。</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 29.10.3. 设备配置寄存器 1（OSPI_DCFG1）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="3">WPSZ[2:0]</td><td></td></tr><tr><td colspan="12"></td><td colspan="3">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">PSC[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>WPSZ[2:0]</td><td>回卷大小000:外部存储器设备不支持回卷读取。001:保留。010:外部存储器设备支持16字节回卷大小。011:外部存储器设备支持32字节回卷大小。100:外部存储器设备支持64字节回卷大小。101:外部存储器设备支持128字节回卷大小。110:保留。111:保留。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>PSC[7:0]</td><td>该位域定义了从内核时钟分频产生OSPI时钟的分频因子(位域值+1)。0:<eq>F_{CLK} = F_{KERNEL}</eq>。1:<eq>F_{CLK} = F_{KERNEL} / 2</eq>。2:<eq>F_{CLK} = F_{KERNEL} / 3</eq>。...255:<eq>F_{CLK} = F_{KERNEL} / 256</eq>。对于奇数时钟分频因子,时钟的占空比没有50%,时钟信号保持低电平时间要比高电平时间少一个周期。</td></tr></table>

# 29.10.4. 状态寄存器（OSPI_STAT）

地址偏移：0x20

复位值：0x0000 0004

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">FL[5:0]</td><td colspan="2">保留</td><td>BUSY</td><td>保留</td><td>SM</td><td>FT</td><td>TC</td><td>TERR</td></tr><tr><td colspan="2"></td><td colspan="6">r</td><td colspan="2"></td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>FL[5:0]</td><td>FIFO等级该位域给出FIFO有效字节数。在状态轮询模式下,FL为0。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>BUSY</td><td>忙状态该位在命令传输时置1,在对存储器一次操作完成后并且FIFO为空时清0。</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>SM</td><td>状态匹配标志在状态轮询模式下,当接收到数据匹配期望值时置1,向SMC位写1清0。</td></tr><tr><td>2</td><td>FT</td><td>FIFO阈值标志在间接模式下,当FIFO阈值到达或者最后读操作时FIFO非空,该位置1。在状态轮询模式下,每次从外部存储器读取状态寄存器时置位,DATA寄存器被读取时清0。</td></tr><tr><td>1</td><td>TC</td><td>传输完成标志在间接模式下,当传输数据达到设置长度时,该位置1。通过对TCC位置1来清除。</td></tr><tr><td>0</td><td>TERR</td><td>传输错误标志在间接模式下,当无效地址被访问时该位置1,通过对TERRC位置1来清除。</td></tr></table>

# 29.10.5. 状态清除寄存器（OSPI_STATC）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>SMC</td><td>保留</td><td>TCC</td><td>TERRC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>SMC</td><td>清除状态匹配标志写1清除状态寄存器的SM标志。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TCC</td><td>清除传输完成标志写1清除状态寄存器的TC标志。</td></tr><tr><td>0</td><td>TERRC</td><td>清除传输错误标志写1清除状态寄存器的TERR标志。</td></tr></table>

# 29.10.6. 数据长度寄存器（OSPI_DTLEN）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DTLEN[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DTLEN[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DTLEN[31:0]</td><td>数据长度在间接模式和状态轮询模式下数据长度为DTLEN+1,对于状态轮询模式,DTLEN的值不大于3。在间接模式下全为1表明未定义长度,OSPI会持续通信直到MESZ设定的存储器容量大小。0x0000 0000:1个字节将要被传输。0x0000 0001:2个字节将要被传输。0x0000 0002:3个字节将要被传输。0x0000 0003:4个字节将要被传输。...0xFFFF FFFD:4,294,967,294 (4G-2)个字节将要被传输。0xFFFF FFFE:4,294,967,295 (4G-1)个字节将要被传输。0xFFFF FFFF:未定义长度 - 所有字节都会被传输直到存储器最后(由MESZ定义),如果MESZ为0x1F,无限读数据。内存映射模式下,该位无影响。</td></tr></table>

# 29.10.7. 地址寄存器（OSPI_ADDR）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 

ADDR[31:0] 

地址

发送到存储器的访问地址。

该位域当BUSY位为0时才能写入并且内存映射模式不被配置。

# 29.10.8. 数据寄存器（OSPI_DATA）

地址偏移：0x50

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>将要与存储器交互的数据。在间接模式下写操作时,在发送到存储器之前,写入到该寄存器数据会被存储到FIFO中。如果FIFO为满,写操作会停止直到FIFO有足够空间。在间接模式下读操作时,读该寄存器获取从存储器接收的数据。如果FIFO没有足够的字节数来满足读命令请求,并且BUSY位为1,那么读操作会被停止直到FIFO中有足够的数据或者传输已经完成。在状态轮询模式下,该寄存器包含从读取的最后数据。</td></tr></table>

# 29.10.9. 状态屏蔽寄存器（OSPI_STATMK）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MASK[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MASK [15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MASK[31:0]</td><td>状态屏蔽用来屏蔽接收的状态字节。对于第n位:</td></tr></table>

0：接收数据的第n位屏蔽，该位不参与匹配逻辑。

1：接收数据的第n位没有屏蔽，该位参与匹配逻辑。

# 29.10.10. 状态匹配寄存器（OSPI_STATMATCH）

地址偏移：0x88

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MATCH[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MATCH[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MATCH[31:0]</td><td>状态匹配与屏蔽状态寄存器比较进行匹配的值。</td></tr></table>

# 29.10.11. 间隔寄存器（OSPI_INTERVAL）

地址偏移：0x90

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INTERVAL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>INTERVAL[15:0]</td><td>间隔周期状态轮询模式下两次读命令之间的SCK周期数。</td></tr></table>

# 29.10.12. 传输配置寄存器（OSPI_TCFG）

地址偏移：0x100

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>DADTR</td><td colspan="3">DATAMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">ALTESZ[1:0]</td><td>ABDTR</td><td colspan="3">ALTEMOD[2:0]</td></tr><tr><td colspan="4"></td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">ADDRSZ[1:0]</td><td>ADDRDTR</td><td colspan="3">ADDRMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">INSSZ[1:0]</td><td>保留</td><td colspan="3">IMOD[2:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>DADTR</td><td>数据双倍传输速率0: 数据阶段禁用DTR。1: 数据阶段使能DTR。注: 仅支持GD25LX512ME。</td></tr><tr><td>26:24</td><td>DATAMOD[2:0]</td><td>数据模式该位定义数据阶段的操作模式。000: 无数据。001: 单线传输数据。010: 双线传输数据。011: 四线传输数据。100: 八线传输数据。101: 保留。110: 保留。111: 保留。</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>ALTESZ[1:0]</td><td>交替字节大小该位域定义交替字节大小。00: 8位交替字节。01: 16位交替字节。10: 24位交替字节。11: 32位交替字节。</td></tr><tr><td>19</td><td>ABDTR</td><td>交替字节双倍传输速率0: 交替字节阶段禁用DTR。1: 交替字节阶段使能DTR。注: 仅支持GD25LX512ME。</td></tr><tr><td>18:16</td><td>ALTEMOD[2:0]</td><td>交替字节模式该位定义交替字节阶段的操作模式:000: 无交替字节。001: 单线传输交替字节。010: 双线传输交替字节。</td></tr></table>

011：四线传输交替字节。

100：八线传输交替字节。

101：保留。

110：保留。

111：保留。

15:14 保留 必须保持复位值。

13:12 ADDRSZ[1:0] 地址大小

该位域定义地址大小。

00：8位地址。

01：16位地址。

10：24位地址。

11：32位地址。

11 ADDRDTR 地址双倍传输速率

0：地址阶段禁用DTR模式。

1：地址阶段使能DTR模式。

注：仅支持GD25LX512ME。

10:8 ADDRMOD[2:0] 地址模式

该位定义地址阶段的操作模式：

000：无地址。

001：单线传输地址。

010：双线传输地址。

011：四线传输地址。

100：八线传输地址。

101：保留。

110：保留。

111：保留。

7:6 保留 必须保持复位值。

5:4 INSSZ[1:0] 指令大小

该位域定义指令大小。

00：8位指令。

01：16位指令。

10：24位指令。

11：32位指令。

3 保留 必须保持复位值。

2:0 IMOD[2:0] 命令模式

该位定义指令阶段的操作模式：

000：无指令。

001：单线传输指令。

010：双线传输指令。

011：四线传输指令。

100：八线传输指令。

101：保留。

110：保留。

111：保留。

# 29.10.13. 时序配置寄存器（OSPI_TIMCFG）

地址偏移：0x108

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>SSAMPLE</td><td colspan="2">保留</td><td>DEHQC</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">DUMYC[4:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>SSAMPLE</td><td>采样移位默认情况下,OSPI在外部存储器驱动数据后二分之一个SCK时钟周期采样。该位允许外部信号延迟的原因采样延迟。0:不移位。1:移位二分之一个周期。注:当通信速率大于40M,SSAMPLE必须设置为1。</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>DEHQC</td><td>延迟保持1/4周期0:不延迟保持。1:延迟保持1/4周期。</td></tr><tr><td>26:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DUMYC[4:0]</td><td>空指令周期数该位域定义空指令阶段持续时间。</td></tr></table>

# 29.10.14. 指令寄存器（OSPI_INS）

地址偏移：0x110

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">INSTRUCTION[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INSTRUCTION[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>INSTRUCTION[31:0]</td><td>指令发送到外部存储器的命令信息。</td></tr></table>

# 29.10.15. 交替字节寄存器（OSPI_ALTE）

地址偏移：0x120

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ALTE[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALTE[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ALTE[31:0]</td><td>交替字节发送给外部存储器的选项字节。</td></tr></table>

# 29.10.16. 回卷传输配置寄存器（OSPI_WPTCFG）

地址偏移：0x140

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>DADTR</td><td colspan="3">DATAMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">ALTESZ[1:0]</td><td>ABDTR</td><td colspan="3">ALTEMOD[1:0]</td></tr><tr><td colspan="4"></td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">ADDRSZ[1:0]</td><td>ADDRDTR</td><td colspan="3">ADDRMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">INSSZ[1:0]</td><td>保留</td><td colspan="3">IMOD[2:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>27</td><td>DADTR</td><td>数据双倍传输速率</td></tr><tr><td></td><td></td><td>0: 数据阶段禁用DTR。</td></tr><tr><td></td><td></td><td>1: 数据阶段使能DTR。</td></tr><tr><td></td><td></td><td>注: 仅支持GD25LX512ME。</td></tr></table>

<table><tr><td>26:24</td><td>DATAMOD[2:0]</td><td>数据模式</td></tr><tr><td></td><td></td><td>该位定义数据阶段的操作模式。</td></tr><tr><td></td><td></td><td>000:无数据。</td></tr><tr><td></td><td></td><td>001:单线传输数据。</td></tr><tr><td></td><td></td><td>010:双线传输数据。</td></tr><tr><td></td><td></td><td>011:四线传输数据。</td></tr><tr><td></td><td></td><td>100:八线传输数据。</td></tr><tr><td></td><td></td><td>101:保留。</td></tr><tr><td></td><td></td><td>110:保留。</td></tr><tr><td></td><td></td><td>111:保留。</td></tr></table>

<table><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>21:20</td><td>ALTESZ[1:0]</td><td>交替字节大小</td></tr><tr><td></td><td></td><td>该位域定义交替字节大小。</td></tr><tr><td></td><td></td><td>00:8位交替字节。</td></tr><tr><td></td><td></td><td>01:16位交替字节。</td></tr><tr><td></td><td></td><td>10:24位交替字节。</td></tr><tr><td></td><td></td><td>11:32位交替字节。</td></tr></table>

<table><tr><td>19</td><td>ABDTR</td><td>交替字节双倍传输速率</td></tr><tr><td></td><td></td><td>0:交替字节阶段禁用DTR。</td></tr><tr><td></td><td></td><td>1:交替字节阶段使能DTR。</td></tr><tr><td></td><td></td><td>注:仅支持GD25LX512ME。</td></tr></table>

<table><tr><td>18:16</td><td>ALTEMOD[2:0]</td><td>交替字节模式</td></tr><tr><td></td><td></td><td>该位定义交替字节阶段的操作模式:</td></tr><tr><td></td><td></td><td>000:无交替字节。</td></tr><tr><td></td><td></td><td>001:单线传输交替字节。</td></tr><tr><td></td><td></td><td>010:双线传输交替字节。</td></tr><tr><td></td><td></td><td>011:四线传输交替字节。</td></tr><tr><td></td><td></td><td>100:八线传输交替字节。</td></tr><tr><td></td><td></td><td>101:保留。</td></tr><tr><td></td><td></td><td>110:保留。</td></tr><tr><td></td><td></td><td>111:保留。</td></tr></table>

<table><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>13:12</td><td>ADDRSZ[1:0]</td><td>地址大小</td></tr><tr><td></td><td></td><td>该位域定义地址大小。</td></tr><tr><td></td><td></td><td>00:8位地址。</td></tr><tr><td></td><td></td><td>01:16位地址。</td></tr><tr><td></td><td></td><td>10:24位地址。</td></tr></table>

11：32位地址。

<table><tr><td>11</td><td>ADDRDTR</td><td>地址双倍传输速率</td></tr><tr><td></td><td></td><td>0: 地址阶段禁用DTR模式。</td></tr><tr><td></td><td></td><td>1: 地址阶段使能DTR模式。</td></tr><tr><td></td><td></td><td>注: 仅支持GD25LX512ME。</td></tr></table>

<table><tr><td>10:8</td><td>ADDRMOD[2:0]</td><td>地址模式</td></tr><tr><td></td><td></td><td>该位定义地址阶段的操作模式:</td></tr><tr><td></td><td></td><td>000:无地址。</td></tr><tr><td></td><td></td><td>001:单线传输地址。</td></tr><tr><td></td><td></td><td>010:双线传输地址。</td></tr><tr><td></td><td></td><td>011:四线传输地址。</td></tr><tr><td></td><td></td><td>100:八线传输地址。</td></tr><tr><td></td><td></td><td>101:保留。</td></tr><tr><td></td><td></td><td>110:保留。</td></tr><tr><td></td><td></td><td>111:保留。</td></tr></table>

7:6 保留 必须保持复位值。

<table><tr><td>5:4</td><td>INSSZ[1:0]</td><td>指令大小</td></tr><tr><td></td><td></td><td>该位域定义指令大小。</td></tr><tr><td></td><td></td><td>00:8位指令。</td></tr><tr><td></td><td></td><td>01:16位指令。</td></tr><tr><td></td><td></td><td>10:24位指令。</td></tr><tr><td></td><td></td><td>11:32位指令。</td></tr></table>

3 保留 必须保持复位值。

<table><tr><td>2:0</td><td>IMOD[1:0]</td><td>命令模式</td></tr><tr><td></td><td></td><td>该位定义指令阶段的操作模式:</td></tr><tr><td></td><td></td><td>000:无指令。</td></tr><tr><td></td><td></td><td>001:单线传输指令。</td></tr><tr><td></td><td></td><td>010:双线传输指令。</td></tr><tr><td></td><td></td><td>011:四线传输指令。</td></tr><tr><td></td><td></td><td>100:八线传输指令。</td></tr><tr><td></td><td></td><td>101:保留。</td></tr><tr><td></td><td></td><td>110:保留。</td></tr><tr><td></td><td></td><td>111:保留。</td></tr></table>

# 29.10.17. 回卷时序配置寄存器（OSPI_WPTIMCFG）

地址偏移：0x148

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>SSAMPLE</td><td>保留</td><td>DEHQC</td><td colspan="11">保留</td><td></td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">DUMYC[4:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>SSAMPLE</td><td>采样移位默认情况下,OSPI在外部存储器驱动数据后二分之一个SCK时钟周期采样。该位允许外部信号延迟的原因采样推迟。0:不移位。1:移位二分之一个周期。</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>DEHQC</td><td>延迟保持1/4周期0:不延迟保持。1:延迟保持1/4周期。</td></tr><tr><td>27:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DUMYC[4:0]</td><td>空指令周期数该位域定义空指令阶段持续时间。</td></tr></table>

# 29.10.18. 回卷指令寄存器（OSPI_WPINS）

地址偏移：0x150

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">INSTRUCTION[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INSTRUCTION[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 INSTRUCTION[31:0] 指令

发送到外部存储器的命令信息。

# 29.10.19. 回卷交替字节寄存器（OSPI_WPALTE）

地址偏移：0x160

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ALTE[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALTE[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ALTE[31:0]</td><td>交替字节发送给外部存储器的可选数据。</td></tr></table>

# 29.10.20. 写入传输配置寄存器（OSPI_WTCFG）

地址偏移：0x180

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>DADTR</td><td colspan="3">DATAMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">ALTESZ[1:0]</td><td>ABDTR</td><td colspan="3">ALTEMOD[1:0]</td></tr><tr><td colspan="4"></td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">ADDRSZ[1:0]</td><td>ADDRDTR</td><td colspan="3">ADDRMOD[2:0]</td><td colspan="2">保留</td><td colspan="2">INSSZ[1:0]</td><td>保留</td><td colspan="3">IMOD[2:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="2"></td><td colspan="2">rw</td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>DADTR</td><td>数据双倍传输速率0: 数据阶段禁用DTR。1: 数据阶段使能DTR。注: 仅支持GD25LX512ME。</td></tr><tr><td>26:24</td><td>DATAMOD[2:0]</td><td>数据模式该位定义数据阶段的操作模式。000: 无数据。001: 单线传输数据。010: 双线传输数据。011: 四线传输数据。100: 八线传输数据。101: 保留。110: 保留。</td></tr></table>

111：保留。

23:22 保留 必须保持复位值。

21:20 ALTESZ[1:0] 交替字节大小该位域定义交替字节大小。

00：8位交替字节。

01：16位交替字节。

10：24位交替字节。

11：32位交替字节。

19 ABDTR 交替字节双倍传输速率

0：交替字节阶段禁用DTR。

1：交替字节阶段使能DTR。

注：仅支持GD25LX512ME。

18:16 ALTEMOD[2:0] 交替字节模式

该位定义交替字节阶段的操作模式：

000：无交替字节。

001：单线传输交替字节。

010：双线传输交替字节。

011：四线传输交替字节。

100：八线传输交替字节。

101：保留。

110：保留。

111：保留。

15:14 保留 必须保持复位值。

13:12 ADDRSZ[1:0] 地址大小

该位域定义地址大小。

00：8位地址。

01：16位地址。

10：24位地址。

11：32位地址。

11 ADDRDTR 地址双倍传输速率

0：地址阶段禁用DTR模式。

1：地址阶段使能DTR模式。

注：仅支持GD25LX512ME。

10:8 ADDRMOD[2:0] 地址模式

该位定义地址阶段的操作模式：

000：无地址。

001：单线传输地址。

010：双线传输地址。

011：四线传输地址。

100：八线传输地址。

101：保留。

110：保留。

111：保留。

7:6 保留 必须保持复位值。

5:4 INSSZ[1:0] 指令大小

该位域定义指令大小。

00：8位指令。

01：16位指令。

10：24位指令。

11：32位指令。

3 保留 必须保持复位值。

2:0 IMOD[1:0] 命令模式

该位定义指令阶段的操作模式：

000：无指令。

001：单线传输指令。

010：双线传输指令。

011：四线传输指令。

100：八线传输指令。

101：保留。

110：保留。

111：保留。

# 29.10.21. 写入时序配置寄存器（OSPI_WTIMCFG）

地址偏移：0x188

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">DUMYC[4:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DUMYC[4:0]</td><td>空指令周期数该位域定义空指令阶段持续时间。</td></tr></table>

# 29.10.22. 写入指令寄存器（OSPI_WINS）

地址偏移：0x190

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">INSTRUCTION[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INSTRUCTION[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 INSTRUCTION[31:0] 指令

发送到外部存储器的命令信息。

# 29.10.23. 写入交替字节寄存器（OSPI_WALTE）

地址偏移：0x1A0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当BUSY位为1，该寄存器不可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ALTE[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALTE[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 ALTE[31:0] 交替字节

发送给外部存储器的可选数据。
