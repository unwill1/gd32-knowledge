# 36.7. SDIO 寄存器

SDIO0 基地址：0x5200 7000

SDIO1 基地址：0x4802 2400

# 36.7.1. 电源控制寄存器（SDIO_PWRCTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>DIRPS</td><td>VSEN</td><td>VSSTART</td><td colspan="2">PWRCTL[1:0]</td></tr></table>


rw rw rw rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>DIRPS</td><td>命令和数据方向极性选择位只有在PWRCTL[1:0]清零状态时,才能写入该位。0:方向信号为低电平时,电压收发器驱动IOs作为输出1:方向信号为高电平时,电压收发器驱动IOs作为输出</td></tr><tr><td>3</td><td>VSEN</td><td>电压切换使能位该位用于在电压切换命令响应后停止SDIO_CLK。只有在CSMEN位清零的条件下,固件才能修改该位。0:在成功接收到命令响应后,SDIO_CLK时钟保持不变1:在成功接收到命令响应后,SDIO_CLK时钟停止</td></tr><tr><td>2</td><td>VSSTART</td><td>电压切换启动位该位用于启动电压切换的时序关键部分。0:电压切换没有激活也没有启动1:电压切换激活或启动</td></tr><tr><td>1:0</td><td>PWRCTL[1:0]</td><td>SDIO电源控制位该位域控制SDIO状态,卡输入或输出。该位域只能在SDIO断电状态下写入。00:复位之后(复位:SDIO被禁用,时钟停止,SDIO_CMD和SDIO_DAT处于高阻状态,且SDIO_CLK是低电平),如果写00,SDIO掉电(掉电:SDIO被禁用,时钟停止,SDIO_DAT、SDIO_CMD和SDIO_CLK都为高电平)01:保留(写01,寄存器值不变)10:掉电再上电(SDIO被禁用且卡的时钟停止,SDIO_DAT、SDIO_CMD和SDIO_CLK都为低电平)</td></tr></table>

11：SDIO 上电（上电后，使能 SDIO 有 74 个时钟周期的延迟，延迟期间任何写操作都被忽略，PWRCTL 寄存器保持 11）

# 36.7.2. 时钟控制寄存器（SDIO_CLKCTL）

地址偏移：0x04

复位值：0x0000 0000

该寄存器控制输出时钟 SDIO_CLK。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="2">RCLK[1:0]</td><td>BUSSP</td><td>DRSEL</td><td>HWEN</td><td>CLKEDGE</td></tr><tr><td colspan="10"></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">BUSMODE[1:0]</td><td>保留</td><td>CLKPWRSAV</td><td colspan="2">保留</td><td colspan="10">DIV[9:0]</td></tr><tr><td colspan="3">rw</td><td colspan="7">rw</td><td colspan="6">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>RCLK[1:0]</td><td>接收时钟选择位该位域只能在CMDSTA=0且DATSTA=0时写入。00:选择SDIO_IN_CLK时钟01:选择SDIO_CLKIN时钟10:选择SDIO_FB_CLK时钟11:保留(默认选择SDIO_IN_CLK时钟)</td></tr><tr><td>19</td><td>BUSSP</td><td>总线速度模式选择位该位只能在CMDSTA=0且DATSTA=0时写入。0:DS,HS,SDR12,SDR25总线模式1:SDR50,DDR50,SDR104总线模式</td></tr><tr><td>18</td><td>DRSEL</td><td>数据速率选择位该位只能在CMDSTA=0且DATSTA=0时写入。0:SDR模式被选择1:DDR模式被选择</td></tr><tr><td>17</td><td>HWEN</td><td>硬件流控制使能位如果该位置位,TFF和RFF寄存器的意义被改变。该位只能在CMDSTA=0且DATSTA=0时写入。0:硬件流控制被禁用1:硬件流控制被使能</td></tr><tr><td>16</td><td>CLKEDGE</td><td>命令和数据SDIO_CLK移相选择位该位只能在CMDSTA=0且DATSTA=0时写入。</td></tr></table>

当 DIV = 0 时，该位不起作用。数据和命令在 SDIO_CLK 的下降沿变化。

0：如果 DIV > 0 且在 SDR 模式，命令和数据在 SDIO_CLK 上升沿后的 CK_SDIO下降沿改变。SDIO_CLK 在 CK_SDIO 的上升沿产生。

如果 DIV > 0 且在 DDR 模式，命令在 SDIO_CLK 上升沿后的 CK_SDIO 下降沿改变。数据在 SDIO_CLK 上升沿后的 CK_SDIO 下降沿改变。SDIO_CLK 在 CK_SDIO的上升沿产生。

1：如果 DIV > 0 且在 SDR 模式，命令和数据在 SDIO_CLK 下降沿后的 CK_SDIO下降沿改变。SDIO_CLK 在 CK_SDIO 的上升沿产生。

如果 DIV > 0 且在 DDR 模式，命令在 SDIO_CLK 下降沿后的 CK_SDIO 上升沿改变。数据在 SDIO_CLK 边沿后的 CK_SDIO 下降沿改变。SDIO_CLK 在 CK_SDIO的上升沿产生。

15:14 BUSMODE[1:0] SDIO卡总线模式控制位

该位域只能在 CMDSTA = 0 且 DATSTA = 0 时写入。

00：选择 1 位总线模式（默认选择且只能 SDR 模式），SDIO_DAT0

01：选择 4 位总线模式，SDIO_DAT[3：0]

10：选择 8 位总线模式，SDIO_DAT[7：0]

11：保留

13 保留 必须保持复位值。

12 CLKPWRSAV SDIO_CLK 时钟动态开启/关闭以节省功耗

该位在总线空闲的时候，控制 SDIO_CLK 时钟动态开启/关闭以节省功耗。

该位只能在 CMDSTA = 0 且 DATSTA = 0 时写入。

0：SDIO_CLK 时钟总是开启

1：SDIO_CLK 时钟在总线空闲时关闭

11:10 保留 必须保持复位值。

9:0 DIV[9:0] 时钟分频

该位域只能在 CMDSTA = 0 且 DATSTA = 0 时写入。

该位域定义了分频因子来向卡产生 SDIO_CLK 时钟。SDIO_CLK 是由 CK_SDIO 分频得到，并且 SDIO_CLK 频率= CK_SDIO / （DIV[9:0] * 2）

0x000：SDIO_CLK = CK_SDIO / 1（不支持 DDR 模式）

0x001：SDIO_CLK = CK_SDIO / 2 

0x002：SDIO_CLK = CK_SDIO / 4 

0x3FF：SDIO_CLK = CK_SDIO / 2046 

注意：SD 卡、SD I/O 卡或 e•MMC 卡在卡识别模式时，SDIO_CLK 频率必须不大于 400kHz。

如果 RCA 已经被分配给所有的卡时，可以改变时钟频率到最大的卡总线频率。

在两次对该寄存器的写访问之间，至少需要 7 个 HCLK 周期，用于同步寄存器到 SDIO_CLK 时钟域。

# 36.7.3. 命令参数寄存器（SDIO_CMDAGMT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器定义了 32 位命令参数，这些参数将被用作为命令的一部分（位 39 到位 8）。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CMDAGMT[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMDAGMT[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CMDAGMT[31:0]</td><td>SDIO 卡命令参数该位域定义了将被发送到卡的 SDIO 卡命令参数。这个域是命令消息的位[39:8]。如果命令消息包含一个参数,在发送命令时,这个域应该在写 SDIO_CMDCTL 寄存器前更新。只有在 CSMEN 位清零时,该位才能被固件写入。</td></tr></table>

# 36.7.4. 命令控制寄存器（SDIO_CMDCTL）

地址偏移：0x0C

复位值：0x0000 0000

SDIO_CMDCTL 寄存器包含命令索引和其他命令控制位来控制命令状态机（CSM）。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>CMDSR</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BOOTMO DEN</td><td>BOOTMO D</td><td>HOLD</td><td>CSMEN</td><td>WAITDE ND</td><td>INTWAIT</td><td colspan="2">CMDRESP[1:0]</td><td>TRSTOP</td><td>TREN</td><td colspan="6">CMDIDX[5:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CMDSR</td><td>将命令视为挂起或恢复命令并发出中断周期开始/结束位。只有在 CSMEN 位清零时,该位才能被固件写入。0:无作用1:如果 TREN = 0,CSM 将命令视为挂起命令;如果 TREN = 1,CSM 将命令视为复位命令</td></tr><tr><td>15</td><td>BOOTMODEN</td><td>引导模式使能位0:禁用引导模式1:使能引导模式</td></tr><tr><td>14</td><td>BOOTMODE</td><td>引导模式选择位只有在 CSMEN 位清零时,该位才能被固件写入。</td></tr></table>

0：正常引导模式

1：备用引导模式

13 HOLD 保持 DSM 发送和接收新的数据块该位置位时，DSM 不会从 DS_WaitS 状态切换到 DS_Send 状态，或者从 DS_WaitR状态切换到 DS_Receive 状态。

只有在 CSMEN 位清零时，该位才能被固件写入。

0：无影响

1：保持在数据传输或接收的状态

12 CSMEN 命令状态机（CSM）使能位该位固件写入，硬件清零。

0：命令状态机失能（停留在 CS_Idle 状态）

1：命令状态机使能

11 WAITDEND 等待数据传输结束如果该位置位，命令状态机开始发送命令前需要等待数据传输结束。

0：无影响

1：等待数据传输结束

10 INTWAIT 等待中断请求如果在 Wait 状态下清零该位，将导致中断模式中止。

0：无影响

1：在命令响应时，禁止命令超时，并等待卡中断请求。

9:8 CMDRESP[1:0] 命令响应类型位这些位定义了发送一个命令消息后的响应类型。只有在 CSMEN 位清零时，该位域才能被固件写入。

00：无响应

01：短响应

10：短响应（无 CRC）

11：长响应

7 TRSTOP 数据传输停止命令模式使能位传输停止命令模式（CSM 将命令当做数据停止传输的命令）只有在 CSMEN 位清零时，该位才能被固件写入。

0：无影响

1：当发送命令时，使能传输停止命令模式且 CSM 将向 DSM发中止信号

6 TREN 数据传输命令模式使能位传输命令模式（CSM 将命令当做数据传输的命令）只有在 CSMEN 位清零时，该位才能被固件写入。

0：无影响

1：如果命令被发送，使能传输命令模式且 DSM 数据传输并且中断周期结束

5:0 CMDIDX[5:0] 命令索引只有在 CSMEN 位清零时，该位才能被固件写入。该位域定义了将被发送到 SDIO卡的命令索引。

注意：两次对该寄存器写访问之间，至少需要 7 个 HCLK 时钟周期，用于将寄存器同步到 SDIO_CLK 时钟域。

e•MMC 可以发送两种响应:短响应，48 位，或长响应，136位。

SD 卡和 SD I/O 卡只能发送短响应，参数可以根据响应的类型而变化：软件根据发送命令来区分响应的类型。

# 36.7.5. 命令索引响应寄存器（SDIO_RSPCMDIDX）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">RSPCMDIDX[5:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>RSPCMDIDX[5:0]</td><td>最后响应的命令索引只读位域。这个域包含收到的最后命令响应的命令索引。如果响应没有命令索引(R3的长响应和短响应),这个寄存器的内容是未定义的。</td></tr></table>

# 36.7.6. 响应寄存器（SDIO_RESPx x = 0..3）

地址偏移：0x14+（4*x）, x = 0..3

复位值：0x0000 0000

这些寄存器包含最后收到的卡响应的内容。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RESPx[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RESPx[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RESPx[31:0]</td><td>卡状态。响应内容由表 36-41. 不同响应类型对应的 SDIO_RESPx 寄存器所示。</td></tr></table>

短响应为 32 位，长响应为 127 位（位 128 是结束位 0）。


表 36-41. 不同响应类型对应的 SDIO_RESPx 寄存器


<table><tr><td>寄存器</td><td>短响应</td><td>长响应</td></tr><tr><td>SDIO_RESP0</td><td>卡响应 [31:0]</td><td>卡响应 [127:96]</td></tr><tr><td>SDIO_RESP1</td><td>保留</td><td>卡响应 [95:64]</td></tr><tr><td>SDIO_RESP2</td><td>保留</td><td>卡响应 [63:32]</td></tr><tr><td>SDIO_RESP3</td><td>保留</td><td>卡响应 [31:1],加上位 0</td></tr></table>

# 36.7.7. 数据超时寄存器（SDIO_DATATO）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATATO[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATATO[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATATO[31:0]</td><td>数据超时时间这些位定义了数据超时时间,由SDIO_CLK计数。当DSM进入WaitR或BUSY状态,该寄存器的值加载到内部计数器开始递减。DSM超时并进入空闲状态,当计数器的值减至0时设置DTTMOUT标志。该域只能在CMDSTA=0且DATSTA=0时写入。</td></tr></table>


注意：当需要数据传输时，数据超时器寄存器和数据长度寄存器应在写数据控制寄存器前更新。


# 36.7.8. 数据长度寄存器（SDIO_DATALEN）

地址偏移：0x28

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td colspan="9">DATALEN[24:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATALEN[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:0</td><td>DATALEN[24:0]</td><td>数据传输长度</td></tr></table>

该寄存器定义了需要传输的字节数。当数据传输开始时，这个寄存器的值将加载到数据计数器并开始递减。

只有在 CMDSTA=0 时，该位才能写入。

当 DATALEN 为 0 时，无数据传输。当有 CSMEN 和 TREN=1 的请求时，也没有命令传输。DATAEN 和 CSMEN 被清零。

注意：如果选择了数据块传输，该寄存器的内容应该为块大小的倍数（参考 SDIO_DATACTL 寄存器）。

当需要数据传输时，数据计时器寄存器和数据长度寄存器应在写数据控制寄存器前更新。

对于多字节传输，数据长度寄存器中的取值必须在 1 到 512之间。

# 36.7.9. 数据控制寄存器（SDIO_DATACTL）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器控制 DSM。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>FIFORES T</td><td>ACKEN</td><td colspan="5">保留</td><td colspan="4">BLKSZ[3:0]</td><td colspan="2">TRANSMOD[1:0]</td><td>DATADIR</td><td>DATAEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td colspan="5"></td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>FIFOREST</td><td>FIFO 复位,刷新所有的数据该位只有在 IDMAEN=0 且 DATSTA=1 时,才能被固件写入。当 DATSTA=0 时,该位被硬件自动清零。如果有传输错误或传输保持时,该位才有效。0:无影响1:刷新所有剩余的数据并复位 FIFO 指针</td></tr><tr><td>12</td><td>ACKEN</td><td>引导确认使能位该位只有在 DATSTA 位清零时,才能被固件写入。0:引导确认禁用1:引导确认使能</td></tr><tr><td>11:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>BLKSZ[3:0]</td><td>数据块大小这些位定义了当数据传输是块传输时数据块的大小。该位只有在 DATSTA 位清零时,才能被固件写入。0000:块大小 = <eq>2^{0}</eq> = 1 字节0001:块大小 = <eq>2^{1}</eq> = 2 字节0010:块大小 = <eq>2^{2}</eq> = 4 字节</td></tr></table>

0011：块大小 = 23 = 8 字节

0100：块大小 = 24 = 16 字节

0101：块大小 = 25 = 32 字节

0110：块大小 = 26 = 64 字节

0111：块大小 = 27 = 128 字节

1000：块大小 = 28 = 256 字节

1001：块大小 = 29 = 512 字节

1010：块大小 = 210 = 1024 字节

1011：块大小 = 211 = 2048 字节

1100：块大小 = 212 = 4096 字节

1101：块大小 = 213 = 8192 字节

1110：块大小 = 214 = 16384 字节

1111：保留

注意：当 DATALEN 不是 BLKSZ 的倍数时，传输的数据将在 BLKSZ 的倍数处截断。

3:2 TRANSMOD[1:0] 数据传输模式

该位域只有在 DATSTA 位清零时，才能被固件写入。

00：块传输模式

01：多字节传输模式（只适用于 SD/SD I/O卡）

10：流传输（只适用于 e•MMC 卡）

11：需要 CMD12 终止传输（开放终点）

1 DATADIR 数据传输方向

该位只有在 DATSTA 位清零时，才能被固件写入。

0：写数据到卡上

1：从卡中读取数据

0 DATAEN 数据传输使能位

数据传输命令未使用时，该位才被用于数据传输。

该位只有在 DATSTA 位清零时，才能被固件写入。该位在数据传输完成时，硬件自动清零。

0：无影响

1：启动数据传输，无 CSM 参与。

# 36.7.10. 数据计数寄存器（SDIO_DATACNT）

地址偏移：0x30

复位值：0x0000 0000

该寄存器为只读类型。当 DSM 从空闲状态进入 DS_WaitR 或者 DS_WaitS 时，该寄存器从数据长度寄存器（SDIO_DATALEN）加载数值。随着数据传输，数值不断递减直至为 0，随后DSM 进入空闲状态并设置数据结束标志 DTEND。

该寄存器只能按字（32位）访问。

31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 

<table><tr><td colspan="7">保留</td><td colspan="8">DATACNT[24:16]</td><td></td></tr><tr><td colspan="7"></td><td colspan="8">r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">DATACNT[15:0]</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:0</td><td>DATACNT[24:0]</td><td>数据计数值只读位域。当读取这些位时,返回待传输剩余数据的字节数。</td></tr></table>


注意：该寄存器只在数据传输完成或保持时读取。在错误事件后读取该值时，读取的数据计数值可能与实际传输的数据字节数不相等。


# 36.7.11. 状态寄存器（SDIO_STAT）

地址偏移：0x34

复位值：0x0000 0000

该寄存器为只读类型。下面描述标志的类型：

位[28:21, 11:0]的标志只能通过向中断清除寄存器（SDIO_INTC）中相应的位写’1’清除。

位[20:12]的标志是根据硬件逻辑而发送变化的。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>IDMAEND</td><td>IDMAERR</td><td>CLKSTOP</td><td>VSEND</td><td>ACKTO</td><td>ACKFAIL</td><td>SDIOINT</td><td>DAT0BSYEND</td><td>DAT0BSY</td><td>RFE</td><td>TFE</td><td>RFF</td><td>TFF</td></tr><tr><td colspan="3"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFH</td><td>TFH</td><td>DATSTA</td><td>CMDSTA</td><td>DATABOR</td><td>DTBLKEND</td><td>DATHOLD</td><td>DTEND</td><td>CMDSEND</td><td>CMDRECV</td><td>RXORE</td><td>TXURE</td><td>DTTMOUT</td><td>CMDTMOUT</td><td>DTCRCERR</td><td>CCRCERR</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>IDMAEND</td><td>IDMA传输结束</td></tr><tr><td>27</td><td>IDMAERR</td><td>IDMA传输错误</td></tr><tr><td>26</td><td>CLKSTOP</td><td>电压切换期间SDIO_CLK停止</td></tr><tr><td>25</td><td>VSEND</td><td>电压切换时关键时序完成</td></tr><tr><td>24</td><td>ACKTO</td><td>引导确认超时</td></tr><tr><td>23</td><td>ACKFAIL</td><td>引导确认接收且检查错误</td></tr></table>

<table><tr><td>22</td><td>SDIOINT</td><td>SD I/O 中断已接收</td></tr><tr><td>21</td><td>DAT0BSYEND</td><td>DAT0 线繁忙到准备好</td></tr><tr><td>20</td><td>DAT0BSY</td><td>DAT0 线繁忙硬件状态标志,不会产生中断。</td></tr><tr><td>19</td><td>RFE</td><td>接收 FIFO 为空硬件状态标志,不会产生中断。</td></tr><tr><td>18</td><td>TFE</td><td>发送 FIFO 为空该位在 FIFO 变满时清零。</td></tr><tr><td>17</td><td>RFF</td><td>接收 FIFO 为满该位在 FIFO 变空时清零。</td></tr><tr><td>16</td><td>TFF</td><td>发送 FIFO 为满硬件状态标志,不会产生中断。该位在 FIFO 变空时清零。</td></tr><tr><td>15</td><td>RFH</td><td>接收 FIFO 半满:FIFO 中至少还有一半数目的字可以被读取当 FIFO 中有(half+1)个空字时,该位被清零。</td></tr><tr><td>14</td><td>TFH</td><td>发送 FIFO 半空:至少还有一半数目的字可以被写到 FIFO 中当 FIFO 中的数据变为(half+1)个时,该位被清零。</td></tr><tr><td>13</td><td>DATSTA</td><td>数据通道激活状态该位只是硬件状态标志,不产生中断。</td></tr><tr><td>12</td><td>CMDSTA</td><td>命令通道激活状态该位只是硬件状态标志位,不产生中断。</td></tr><tr><td>11</td><td>DATABOR</td><td>数据传输被 CMD12 中止</td></tr><tr><td>10</td><td>DTBLKEND</td><td>数据块已发送/已接收(CRC 检测通过)</td></tr><tr><td>9</td><td>DATHOLD</td><td>数据传输保持</td></tr><tr><td>8</td><td>DTEND</td><td>数据结束(数据计数器,SDIO_DATACNT 为零)</td></tr><tr><td>7</td><td>CMDSEND</td><td>命令已发送(不需响应)</td></tr><tr><td>6</td><td>CMDRECV</td><td>命令响应已接收(CRC 检测通过)</td></tr><tr><td>5</td><td>RXORE</td><td>接收 FIFO 上溢错误发生</td></tr><tr><td>4</td><td>TXURE</td><td>发送 FIFO 下溢错误发生</td></tr><tr><td>3</td><td>DTTMOUT</td><td>数据超时,数据超时时间取决于 SDIO_DATATO 寄存器。</td></tr><tr><td>2</td><td>CMDTMOUT</td><td>命令响应超时,命令超时时间为 64 个 SDIO_CLK 时钟周期的固定值。</td></tr><tr><td>1</td><td>DTCRCERR</td><td>数据块已发送/已接收(CRC 检测失败)</td></tr><tr><td>0</td><td>CCRCERR</td><td>命令响应已接收(CRC 检测失败)</td></tr></table>

注意：如果使用 IDMA模式，FIFO 中断不能够被使能。

# 36.7.12. 中断清除寄存器（SDIO_INTC）

地址偏移：0x38

复位值：0x0000 0000

该寄存器为只读。对该寄存器的位写 1 可以清除 SDIO_STAT 寄存器中相应的状态位。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>IDMAENDC</td><td>IDMAERRC</td><td>CLKSTOPC</td><td>VSENDC</td><td>ACKTOC</td><td>ACKFAILC</td><td>SDIOINTC</td><td>DAT0BSYENDC</td><td colspan="5">保留</td></tr><tr><td colspan="3"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>DATABORC</td><td>DTBLKE NDC</td><td>DATHOL DC</td><td>DTENDC</td><td>CMDSEN DC</td><td>CMDREC VC</td><td>RXOREC</td><td>TXUREC</td><td>DTTMOUTC</td><td>CMDTMO UTC</td><td>DTCRCE RRC</td><td>CCRCER RC</td><td></td></tr><tr><td colspan="3"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>IDMAENDC</td><td>IDMAEND 标志清楚位写 1 清除标志。</td></tr><tr><td>27</td><td>IDMAERRC</td><td>IDMAERR 标志清楚位写 1 清除标志。</td></tr><tr><td>26</td><td>CLKSTOPC</td><td>CLKSTOP 标志清楚位写 1 清除标志。</td></tr><tr><td>25</td><td>VSENDC</td><td>VSEND 标志清楚位写 1 清除标志。</td></tr><tr><td>24</td><td>ACKTOC</td><td>ACKTO 标志清楚位写 1 清除标志。</td></tr><tr><td>23</td><td>ACKFAILC</td><td>ACKFAIL 标志清除位写 1 清除标志。</td></tr><tr><td>22</td><td>SDIOINTC</td><td>SDIOINT 标志清除位写 1 清除标志。</td></tr><tr><td>21</td><td>DAT0BSYENDC</td><td>DAT0BSYEND 标志清除位写 1 清除标志。</td></tr><tr><td>20:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DATABORC</td><td>DATABOR 标志清除位写 1 清除标志。</td></tr></table>

<table><tr><td>10</td><td>DTBLKENDC</td><td>DTBLKEND 标志清除位写 1 清除标志。</td></tr><tr><td>9</td><td>DATHOLDC</td><td>DATHOLD 标志清除位写 1 清除标志。</td></tr><tr><td>8</td><td>DTENDC</td><td>DTEND 标志清除位写 1 清除标志。</td></tr><tr><td>7</td><td>CMDSENDC</td><td>CMDSEND 标志清除位写 1 清除标志。</td></tr><tr><td>6</td><td>CMDRECVC</td><td>CMDRECV 标志清除位写 1 清除标志。</td></tr><tr><td>5</td><td>RXOREC</td><td>RXORE 标志清除位写 1 清除标志。</td></tr><tr><td>4</td><td>TXUREC</td><td>TXURE 标志清除位写 1 清除标志。</td></tr><tr><td>3</td><td>DTTMOUTC</td><td>DTTMOUT 标志清除位写 1 清除标志。</td></tr><tr><td>2</td><td>CMDTMOUTC</td><td>CMDTMOUT 标志清除位写 1 清除标志。</td></tr><tr><td>1</td><td>DTCRCERRC</td><td>DTCRCERR 标志清除位写 1 清除标志。</td></tr><tr><td>0</td><td>CCRCERRC</td><td>CCRCERR 标志清除位写 1 清除标志。</td></tr></table>

# 36.7.13. 中断使能寄存器（SDIO_INTEN）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器使能 SDIO_STAT 寄存器中相应状态位的中断。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>IDMAENDIE</td><td>IDMAERRIE</td><td>CLKSTOPIE</td><td>VSENDIE</td><td>ACKTOIE</td><td>ACKFAILIE</td><td>SDIOINTIE</td><td>DAT0BSYENDIE</td><td colspan="2">保留</td><td>TFEIE</td><td>RFFIE</td><td>保留</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFHIE</td><td>TFHIE</td><td colspan="2">保留</td><td>DATABORIE</td><td>DTBLKE NDIE</td><td>DATHOLDIE</td><td>DTENDIE</td><td>CMDSEN DIE</td><td>CMDREC VIE</td><td>RXOREIE</td><td>TXUREIE</td><td>DTTMOUTIE</td><td>CMDTMO UTIE</td><td>DTCRCE RRIE</td><td>CCRCER RIE</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28</td><td>IDMAENDIE</td><td>IDMA传输结束中断使能写1使能中断。</td></tr><tr><td>27</td><td>IDMAERRIE</td><td>IDMA传输错误中断使能写1使能中断。</td></tr><tr><td>26</td><td>CLKSTOPIE</td><td>电压切换时钟停止中断使能写1使能中断。</td></tr><tr><td>25</td><td>VSENDIE</td><td>电压切换关键时序结束中断使能写1使能中断。</td></tr><tr><td>24</td><td>ACKTOIE</td><td>引导确认超时使能写1使能中断。</td></tr><tr><td>23</td><td>ACKFAILIE</td><td>引导确认接收和检验失败中断使能写1使能中断。</td></tr><tr><td>22</td><td>SDIOINTIE</td><td>SD I/O中断已接收中断使能写1使能中断。</td></tr><tr><td>21</td><td>DAT0BSYENDIE</td><td>DAT0线繁忙结束中断使能写1使能中断。</td></tr><tr><td>20:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>TFEIE</td><td>发送FIFO空中断使能写1使能中断。</td></tr><tr><td>17</td><td>RFFIE</td><td>接收FIFO满中断使能写1使能中断。</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15</td><td>RFHIE</td><td>接收FIFO半满中断使能写1使能中断。</td></tr><tr><td>14</td><td>TFHIE</td><td>发送FIFO半空中断使能写1使能中断。</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11</td><td>DATABORIE</td><td>数据传输中止中断使能写1使能中断。</td></tr><tr><td>10</td><td>DTBLKENDIE</td><td>数据块已发送/已接收中断使能写1使能中断。</td></tr><tr><td>9</td><td>DATHOLDIE</td><td>数据保持中断使能写1使能中断。</td></tr></table>

<table><tr><td>8</td><td>DTENDIE</td><td>数据结束中断使能写1使能中断。</td></tr><tr><td>7</td><td>CMDSENDIE</td><td>命令已发送中断使能写1使能中断。</td></tr><tr><td>6</td><td>CMDRECVIE</td><td>命令响应已接收中断使能写1使能中断。</td></tr><tr><td>5</td><td>RXOREIE</td><td>接收FIFO上溢错误中断使能写1使能中断。</td></tr><tr><td>4</td><td>TXUREIE</td><td>发送FIFO下溢错误中断使能写1使能中断。</td></tr><tr><td>3</td><td>DTTMOUTIE</td><td>数据超时中断使能写1使能中断。</td></tr><tr><td>2</td><td>CMDTMOUTIE</td><td>命令响应超时中断使能写1使能中断。</td></tr><tr><td>1</td><td>DTCRCERRIE</td><td>数据CRC错误中断使能写1使能中断。</td></tr><tr><td>0</td><td>CCRCERRIE</td><td>命令响应CRC错误中断使能写1使能中断。</td></tr></table>

# 36.7.14. ACK 超时寄存器（SDIO_ACKTO）

地址偏移：0x40

复位值：0x0000 0000

当DSM进入WaitAck状态时，该寄存器的值将装载到计数器中，用于计数引导确认是否超时。如果计数器计数到0时，ACK超时状态标志会置位。

数据传输时，必须先设置SDIO_ACKTO寄存器，然后再设置SDIO_DATACTL寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td colspan="9">ACKTO[24:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ACKTO[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:0</td><td>ACKTO[24:0]</td><td>引导确认超时时间</td></tr></table>

只有在 CSMEN 位清零时，该位才能被固件写入。

# 36.7.15. FIFO 数据寄存器（SDIO_FIFO）

地址偏移：0x80

复位值：0x0000 0000

该寄存器占用了 16 个 32 位的字，地址偏移从 0x80 到 0xBC。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">FIFODT[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FIFODT[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FIFODT[31:0]</td><td>接收FIFO数据或发送FIFO数据这些位为接收FIFO或发送FIFO的数据。读或写该寄存器相当于对FIFO读或写数据。只有在DATSTA位置位时,该位才能被固件写入。</td></tr></table>

# 36.7.16. 内部 DMA（IDMA）控制寄存器（SDIO_IDMACTL）

地址偏移：0x50

复位值：0x0000 0000

该寄存器作为发送或接收 FIFO 只能按字（32 位）进行访问。

FIFO 包含 32 个连续地址作为 32 个入口。允许 CPU 使用该寄存器存储/装载多操作命令去写/读 FIFO。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>BUFSEL</td><td>BUFMOD</td><td>IDMAEN</td></tr></table>


rw rw rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>BUFSEL</td><td>IDMA 双缓冲区选择位只有在 DATSTA 位清零时,该位才能被固件写入。0: IDMA 使能时,使用缓冲区 0,禁止固件对 IDMAADDR0 进行写访问1: IDMA 使能时,使用缓冲区 1,禁止固件对 IDMAADDR1 进行写访问</td></tr></table>

<table><tr><td>1</td><td>BUFMOD</td><td>双缓冲区模式使能位只有在 DATSTA 位清零时,该位才能被固件写入。0:单缓冲区模式1:双缓冲区模式</td></tr><tr><td>0</td><td>IDMAEN</td><td>FIFO 内部 DMA 使能位只有在 DATSTA 位清零时,该位才能被固件写入。0: IDMA 禁用1: IDMA 使能</td></tr></table>

# 36.7.17. 内部 DMA（IDMA）缓冲大小寄存器（SDIO_IDMASIZE）

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

该寄存器包含双缓冲区模式下的缓冲区大小。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="8">IDMASIZE[7:0]</td><td colspan="5">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:5</td><td>IDMASIZE[7:0]</td><td>每个缓冲区的字节数IDMA区大小 = IDMASIZE[7:0]*8 字0x00:缓冲区大小 = 0 字0x01:缓冲区大小 = 8 字0x02:缓冲区大小 = 16 字......0xFF:缓冲区大小 = 2040 字</td></tr><tr><td>4:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 36.7.18. IDMA 缓冲区 0 基地址寄存器（SDIO_IDMAADDR0）

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

该寄存器包含单缓冲区配置下缓冲区的基地址，和双缓冲区配置的缓冲区 0 的基地址。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">IDMAADDR0[31:16]</td><td></td></tr><tr><td colspan="15">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">IDMAADDR0[15:0]</td><td></td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDMAADDR0[31:0]</td><td>地址是4的倍数。IDMAADDR0[1:0]总是0且只能被读。只有在DATSTA位清零时,该位域才能被固件写入。当DATSTA和BUFSEL都为1时,可以通过固件动态写入。</td></tr></table>

# 36.7.19. IDMA 缓冲区 1 基地址寄存器（SDIO_IDMAADDR1）

地址偏移：0x5C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

该寄存器包含双缓冲区配置的缓冲区 1 的基地址。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDMAADDR1[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDMAADDR1[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDMAADDR1[31:0]</td><td>地址是4的倍数。IDMAADDR1[1:0]总是0且只能被读。只有在DATSTA位清零时,该位域才能被固件写入。当DATSTA为1且BUFSEL都为0时,可以通过固件动态写入。</td></tr></table>
