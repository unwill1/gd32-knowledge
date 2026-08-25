## 29.8. SDIO 寄存器

SDIO 基地址：0x4001 2C00

## 29.8.1. 电源控制寄存器（SDIO_PWRCTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td colspan="2">PWRCTL[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>PWRCTL[1:0]</td><td>SDIO 电源控制位这些位控制 SDIO 状态,卡输入或输出。00: SDIO 电源关闭: SDIO CSM/DSM 复位到 IDLE,卡的时钟停止,没有命令/数据输出到卡01: 保留10: 保留11: SDIO 上电</td></tr></table>


注意：两次对该寄存器写访问之间，需要至少 3 个 SDIOCLK 和 2 个 PCLK2 时钟周期，用于同步寄存器到 SDIOCLK 时钟域。


## 29.8.2. 时钟控制寄存器（SDIO_CLKCTL）

地址偏移：0x04

复位值：0x0000 0000

该寄存器控制输出时钟 SDIO_CLK。

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DIV[8]</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>HWCLKEN</td><td>CLKEDGE</td><td colspan="2">BUSMODE[1:0]</td><td>CLKBYP</td><td>CLKPWRSAV</td><td>CLKEN</td><td colspan="8">DIV[7:0]</td></tr><tr><td></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td colspan="5">rw</td></tr></table>

<table><tr><td>31</td><td>DIV[8]</td><td>时钟分频系数的最高位这个域定义了输入时钟(SDIOCLK)与输出时钟间的分频系数的最高位,参考SDIO_CLKCTL寄存器的0到7位。</td></tr><tr><td>30:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>HWCLKEN</td><td>硬件时钟控制使能位如果该位置位,根据系统总线是否非常忙,硬件控制SDIO_CLK开/关。由于硬件可以在快要下溢/上溢时关闭SDIO_CLK,所以当该位被置位时不会有下溢/上溢错误。0:关闭硬件时钟控制1:开启硬件时钟控制</td></tr><tr><td>13</td><td>CLKEDGE</td><td>SDIO_CLK时钟边沿选择位0:选择SDIOCLK的上升沿产生SDIO_CLK1:选择SDIOCLK的下降沿产生SDIO_CLK</td></tr><tr><td>12:11</td><td>BUSMODE[1:0]</td><td>SDIO卡总线模式控制位00:1位SDIO卡总线模式01:4位SDIO卡总线模式10:8位SDIO卡总线模式</td></tr><tr><td>10</td><td>CLKBYP</td><td>旁路时钟使能位该位定义了SDIO_CLK直接来自于SDIOCLK或是SDIOCLK分频。0:无旁路,SDIO_CLK时钟参考SDIO_CLKCTL寄存器的DIV位域1:旁路时钟,SDIO_CLK时钟直接为SDIOCLK(SDIOCLK/1)</td></tr><tr><td>9</td><td>CLKPWRSAV</td><td>SDIO_CLK时钟动态开启/关闭以节省功耗该位在总线空闲的时候,控制SDIO_CLK时钟动态开启/关闭以节省功耗。0:SDIO_CLK时钟总是开启1:SDIO_CLK时钟在总线空闲时关闭</td></tr><tr><td>8</td><td>CLKEN</td><td>SDIO_CLK时钟输出使能位0:关闭SDIO_CLK1:开启SDIO_CLK</td></tr><tr><td>7:0</td><td>DIV[7:0]</td><td>时钟分频该个域和DIV[8]位定义了分频因子来向卡产生SDIO_CLK时钟。如果CLKBYP位为0,SDIO_CLK是由SDIOCLK分频得到,并且SDIO_CLK频率=SDIOCLK/(DIV[8:0]+2)。</td></tr><tr><td></td><td colspan="2">注意:两次对该寄存器写访问之间,需要至少3个SDIOCLK和2个PCLK2时钟周期,用于同步寄存器到SDIOCLK时钟域。</td></tr></table>

## 29.8.3. 命令参数寄存器（SDIO_CMDAGMT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器定义了 32 位命令参数，这些参数将被用作于命令的一部分（位 39 到位 8）该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CMDAGMT[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMDAGMT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CMDAGMT[31:0]</td><td>SDIO 卡命令参数这个域定义了将被发送到卡的 SDIO 卡命令参数。这个域是命令消息的位[39:8]。如果命令消息包含一个参数,在发送命令时,这个域应该在写 SDIO_CMDCTL 寄存器前更新。</td></tr></table>

## 29.8.4. 命令控制寄存器（SDIO_CMDCTL）

地址偏移：0x0C

复位值：0x0000 0000

SDIO_CMDCTL 寄存器包含命令索引和其他命令控制位来控制命令状态机（CSM）。

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>ATAEN</td><td>NINTEN</td><td>ENCMDC</td><td>SUSPEND</td><td>CSMEN</td><td>WAITDEND</td><td>INTWAIT</td><td colspan="2">CMDRESP[1:0]</td><td colspan="6">CMDIDX[5:0]</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="6">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>ATAEN</td><td>CE-ATA 命令使能(仅用于 CE-ATA)如果该位置位,主机进入 CE-ATA 模式,并且 CSM 传输 CMD61。0: CE-ATA 失能1: CE-ATA 使能</td></tr><tr><td>13</td><td>NINTEN</td><td>无 CE-ATA 中断(仅用于 CE-ATA)该位定义了有无 CE-ATA 中断。该位仅用于 CE-ATA 卡的情况。0: CE-ATA 中断使能1: CE_ATA 中断失能</td></tr><tr><td>12</td><td>ENCMDC</td><td>使能命令完成信号(仅用于 CE-ATA)该位定义了在 CE-ATA 上有无命令完成信号。0: 无命令完成信号1: 有命令完成信号</td></tr><tr><td>11</td><td>SUSPEND</td><td>SD I/O 暂停命令(仅用于 SD I/O)该位定义了CSM是否发送了暂停命令。该位仅用于SDIO卡。0:无影响1:暂停命令</td></tr><tr><td>10</td><td>CSMEN</td><td>命令状态机(CSM)使能位0:命令状态机失能(停留在CS_Idle)1:命令状态机使能</td></tr><tr><td>9</td><td>WAITDEND</td><td>等待数据传输结束如果该位置位,命令状态机开始发送命令前需要等待数据传输结束。0:无影响1:等待数据传输结束</td></tr><tr><td>8</td><td>INTWAIT</td><td>中断等待超时该位定义了命令状态机在CS_Wait状态等待卡中断。如果该位被置位,无命令等待超时生成。0:无等待中断1:等待中断</td></tr><tr><td>7:6</td><td>CMDRESP[1:0]</td><td>命令响应类型位这些位定义了发送一个命令消息后的响应类型。00:无响应01:短响应10:无响应11:长响应</td></tr><tr><td>5:0</td><td>CMDIDX[5:0]</td><td>命令索引这个域定义了将被发送到SDIO卡的命令索引。</td></tr></table>

注意：两次对该寄存器写访问之间，需要至少 3 个 SDIOCLK 和 2 个 PCLK2 时钟周期，用于同步寄存器到 时钟域。

## 29.8.5. 命令索引响应寄存器（SDIO_RSPCMDIDX）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">RSPCMDIDX[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>RSPCMDIDX[5:0]</td><td>最后响应的命令索引</td></tr></table>

只读位域。这个域包含收到的最后命令响应的命令索引。如果响应没有命令索引（R3 的长响应和短响应），这个寄存器的内容是不未定义的。

## 29.8.6. 响应寄存器（SDIO_RESPx）（x=0...3）

地址偏移：0x14 + 4 * x

复位值：0x0000 0000

这些寄存器包含最后收到的卡响应的内容。

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RESPx[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RESPx[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RESPx[31:0]</td><td>卡状态。响应内容由表29-32. 不同响应类型对应的SDIO RESPx寄存器所示。</td></tr></table>


短响应为 32 位，长响应为 127 位（位 128 是结束位 0）。



表 29-32. 不同响应类型对应的 SDIO_RESPx 寄存器


<table><tr><td>寄存器</td><td>短响应</td><td>长响应</td></tr><tr><td>SDIO_RESP0</td><td>卡响应[31:0]</td><td>卡响应[127:96]</td></tr><tr><td>SDIO_RESP1</td><td>保留</td><td>卡响应[95:64]</td></tr><tr><td>SDIO_RESP2</td><td>保留</td><td>卡响应[63:32]</td></tr><tr><td>SDIO_RESP3</td><td>保留</td><td>卡响应[31:1],加上位 0</td></tr></table>

## 29.8.7. 数据超时寄存器（SDIO_DATATO）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATATO[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATATO[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATATO[31:0]</td><td>数据超时时间这些位定义了数据超时时间,由SDIO_CLK计数。当DSM进入WaitR或BUSY状态,该寄存器的值加载到内部计数器开始递减。DSM超时并进入空闲状态,当计数</td></tr></table>

器的值减至 0 时设置 DTTMOUT标志。

注意：当需要数据传输时，数据定时器寄存器和数据长度寄存器应在写数据控制寄存器前更新。

## 29.8.8. 数据长度寄存器（SDIO_DATALEN）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td colspan="9">DATALEN[24:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATALEN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:0</td><td>DATALEN[24:0]</td><td>数据传输长度该寄存器定义了需要传输的字节数。当数据传输开始时,数据计数器加载到这个寄存器并开始递减。</td></tr></table>

注意：如果选择了数据块传输，该寄存器的内容应该为块大小的倍数（参考 SDIO_DATACTL 寄存器）。当需要数据传输时，数据定时器寄存器和数据长度寄存器应在写数据控制寄存器前更新。

## 29.8.9. 数据控制寄存器（SDIO_DATACTL）

地址偏移：0x2C

复位值：0x0000 0000


该寄存器控制 DSM。该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>IOEN</td><td>RWTYPE</td><td>RWSTOP</td><td>RWEN</td><td colspan="4">BLKSZ[3:0]</td><td>DMAEN</td><td>TRANSMOD</td><td>DATADIR</td><td>DATAEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>IOEN</td><td>SD I/O 特定功能使能(仅用于 SD I/O)0:未使能 SD I/O 特定功能1:使能 SD I/O 特定功能</td></tr><tr><td>10</td><td>RWTYPE</td><td>读等待类型(仅用于 SD I/O)0:使用SDIO_DAT[2]控制读等待1:通过停止SDIO_CLK控制读等待</td></tr><tr><td>9</td><td>RWSTOP</td><td>读等待停止(仅用于SD I/O)0:无影响1:如果RWEN位被置位,停止读等待过程</td></tr><tr><td>8</td><td>RWEN</td><td>读等待模式使能(仅用于SD I/O)0:读等待模式失能1:读等待模式使能</td></tr><tr><td>7:4</td><td>BLKSZ[3:0]</td><td>数据块大小这些位定义了当数据传输是块传输时数据块的大小。0000:块大小=20=1字节0001:块大小=21=2字节0010:块大小=22=4字节0011:块大小=23=8字节0100:块大小=24=16字节0101:块大小=25=32字节0110:块大小=26=64字节0111:块大小=27=128字节1000:块大小=28=256字节1001:块大小=29=512字节1010:块大小=210=1024字节1011:块大小=211=2048字节1100:块大小=212=4096字节1101:块大小=213=8192字节1110:块大小=214=16384字节1111:保留</td></tr><tr><td>3</td><td>DMAEN</td><td>DMA使能位0:DMA失能1:DMA使能</td></tr><tr><td>2</td><td>TRANSMOD</td><td>数据传输模式0:块传输模式1:流传输或SDIO多字节传输模式</td></tr><tr><td>1</td><td>DATADIR</td><td>数据传输方向0:写数据到卡上1:从卡中读取数据</td></tr><tr><td>0</td><td>DATAEN</td><td>数据传输使能位写1到该位开启数据传输不管该位为0或1。如果RWEN置位,DSM进入到读等待状态,或者根据DATADIR位DSM进入WaitS或WaitR状态。开始一个新的数据传输,不需要清该位为0。</td></tr></table>

到 SDIOCLK 时钟域。

## 29.8.10. 数据计数寄存器（SDIO_DATACNT）

地址偏移：0x30

复位值：0x0000 0000

该寄存器为只读类型。当 DSM 从空闲状态进入 WaitR 或者 WaitS 时，该寄存器从数据长度寄存器（SDIO_DATALEN）加载数值。随着数据传输，数值不断递减直至为 0，随后 DSM 进入空闲状态并设置数据结束标志 DTEND。

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td colspan="9">DATACNT[24:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATACNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:0</td><td>DATACNT[24:0]</td><td>数据计数值</td></tr></table>


只读位域。当读取这些位时，返回待传输剩余数据的字节数。


## 29.8.11. 状态寄存器（SDIO_STAT）

地址偏移：0x34

复位值：0x0000 0000

该寄存器为只读类型。下面描述标志的类型：

位[23:22, 10:0]的标志只能通过向中断清除寄存器(SDIO_INTC)中相应的位写’1’清除。

位[21:11]的标志是根据硬件逻辑而发送变化的。

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>ATAEND</td><td>SDIOINT</td><td>RXDTVAL</td><td>TXDTVAL</td><td>RFE</td><td>TFE</td><td>RFF</td><td>TFF</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFH</td><td>TFH</td><td>RXRUN</td><td>TXRUN</td><td>CMDRUN</td><td>DTBLKE ND</td><td>STBITE</td><td>DTEND</td><td>CMDSEN D</td><td>CMDREC V</td><td>RXORE</td><td>TXURE</td><td>DTTMOUT</td><td>CMDTMO UT</td><td>DTCRCER RR</td><td>CCRCER R</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>ATAEND</td><td>CE-ATA 命令完成信号已接收(仅用于CMD61)</td></tr><tr><td>22</td><td>SDIOINT</td><td>SD I/O 中断已接收</td></tr><tr><td>21</td><td>RXDTVAL</td><td>接收 FIFO 中的数据有效</td></tr><tr><td>20</td><td>TXDTVAL</td><td>发送 FIFO 中的数据有效</td></tr><tr><td>19</td><td>RFE</td><td>接收 FIFO 为空</td></tr><tr><td>18</td><td>TFE</td><td>发送 FIFO 为空,当硬件流控制使能,并且 FIFO 中包含 2 个字时,TFE 信号变得有效。</td></tr><tr><td>17</td><td>RFF</td><td>接收 FIFO 为满,当硬件流控制使能,RFF 信号在 FIFO 差 2 个字就满时变得有效。</td></tr><tr><td>16</td><td>TFF</td><td>发送 FIFO 为满</td></tr><tr><td>15</td><td>RFH</td><td>接收 FIFO 半满:FIFO 中至少还有 8 个字可被读取</td></tr><tr><td>14</td><td>TFH</td><td>发送 FIFO 半空:至少还有 8 个字可被写入到 FIFO 中</td></tr><tr><td>13</td><td>RXRUN</td><td>正在接收数据</td></tr><tr><td>12</td><td>TXRUN</td><td>正在传输数据</td></tr><tr><td>11</td><td>CMDRUN</td><td>正在传输命令</td></tr><tr><td>10</td><td>DTBLKEND</td><td>数据块已发送/已接收(CRC 检测通过)</td></tr><tr><td>9</td><td>STBITE</td><td>总线上起始位错误</td></tr><tr><td>8</td><td>DTEND</td><td>数据结束(数据计数器,SDIO_DATACNT 为零)</td></tr><tr><td>7</td><td>CMDSEND</td><td>命令已发送(不需响应)</td></tr><tr><td>6</td><td>CMDRECV</td><td>命令响应已接收(CRC 检测通过)</td></tr><tr><td>5</td><td>RXORE</td><td>接收 FIFO 上溢错误发生</td></tr><tr><td>4</td><td>TXURE</td><td>发送 FIFO 下溢错误发生</td></tr><tr><td>3</td><td>DTTMOUT</td><td>数据超时,数据超时时间取决于 SDIO_DATATO 寄存器。</td></tr><tr><td>2</td><td>CMDTMOUT</td><td>命令响应超时,命令超时时间为 64 个 SDIO_CLK 时钟周期的固定值。</td></tr><tr><td>1</td><td>DTCRCERR</td><td>数据块已发送/已接收(CRC 检测失败)</td></tr><tr><td>0</td><td>CCRCERR</td><td>命令响应已接收(CRC 检测失败)</td></tr></table>

## 29.8.12. 中断清除寄存器（SDIO_INTC）

地址偏移：0x38

复位值：0x0000 0000

该寄存器为只读。对该寄存器的位写 1 可以清除 SDIO_STAT 寄存器中相应的状态位。该寄存器只能按字(32 位)访问

<table><tr><td colspan="7">保留</td><td>ATAENDC</td><td>SDIOINTC</td><td colspan="6">保留</td><td></td></tr><tr><td colspan="7"></td><td>w</td><td>w</td><td colspan="6"></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>DTBLKENDC</td><td>STBITEC</td><td>DTENDC</td><td>CMDSENDC</td><td>CMDRECVC</td><td>RXOREC</td><td>TXUREC</td><td>DTTMOUTC</td><td>CMDTMOUTC</td><td>DTCRERRC</td><td>CCRCERRC</td></tr><tr><td colspan="5"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>ATAENDC</td><td>ATAEND 标志清除位写 1 清除标志。</td></tr><tr><td>22</td><td>SDIOINTC</td><td>SDIOINT 标志清除位写 1 清除标志。</td></tr><tr><td>21:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>DTBLKENDC</td><td>DTBLKEND 标志清除位写 1 清除标志。</td></tr><tr><td>9</td><td>STBITEC</td><td>STBITE 标志清除位写 1 清除标志。</td></tr><tr><td>8</td><td>DTENDC</td><td>DTEND 标志清除位写 1 清除标志。</td></tr><tr><td>7</td><td>CMDSENDC</td><td>CMDSEND 标志清除位写 1 清除标志。</td></tr><tr><td>6</td><td>CMDRECVC</td><td>CMDRECV 标志清除位写 1 清除标志。</td></tr><tr><td>5</td><td>RXOREC</td><td>RXORE 标志清除位写 1 清除标志。</td></tr><tr><td>4</td><td>TXUREC</td><td>TXURE 标志清除位写 1 清除标志。</td></tr><tr><td>3</td><td>DTTMOUTC</td><td>DTTMOUT 标志清除位写 1 清除标志。</td></tr><tr><td>2</td><td>CMDTMOUTC</td><td>CMDTMOUT 标志清除位写 1 清除标志。</td></tr><tr><td>1</td><td>DTCRCERRC</td><td>DTCRCERR 标志清除位写 1 清除标志。</td></tr><tr><td>0</td><td>CCRCERRC</td><td>CCRCERR 标志清除位写 1 清除标志。</td></tr></table>

## 29.8.13. 中断使能寄存器（SDIO_INTEN）

地址偏移：0x3C

复位值：0x0000 0000


该寄存器使能 SDIO_STAT 寄存器中相应状态位的中断。该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>ATAENDIE</td><td>SDIOINTIE</td><td>RXDTVALIE</td><td>TXDTVALIE</td><td>RFEIE</td><td>TFEIE</td><td>RFFIE</td><td>TFFIE</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFHIE</td><td>TFHIE</td><td>RXRUNIE</td><td>TXRUNIE</td><td>CMDRUNIE</td><td>DTBLKENDIE</td><td>STBITEIE</td><td>DTENDIE</td><td>CMDSEN DIE</td><td>CMDREC VIE</td><td>RXOREIE</td><td>TXUREIE</td><td>DTTMOUTIE</td><td>CMDTMO UTIE</td><td>DTCRCE RRIE</td><td>CCRCER RIE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>ATAENDIE</td><td>CE-ATA命令完成信号已接收中断使能写1使能中断。</td></tr><tr><td>22</td><td>SDIOINTIE</td><td>SD I/O中断已接收中断使能写1使能中断。</td></tr><tr><td>21</td><td>RXDTVALIE</td><td>接收FIFO中的数据有效中断使能写1使能中断。</td></tr><tr><td>20</td><td>TXDTVALIE</td><td>发送FIFO中的数据有效中断使能写1使能中断。</td></tr><tr><td>19</td><td>RFEIE</td><td>接收FIFO空中断使能写1使能中断。</td></tr><tr><td>18</td><td>TFEIE</td><td>发送FIFO空中断使能写1使能中断。</td></tr><tr><td>17</td><td>RFFIE</td><td>接收FIFO满中断使能写1使能中断。</td></tr><tr><td>16</td><td>TFFIE</td><td>发送FIFO满中断使能写1使能中断。</td></tr><tr><td>15</td><td>RFHIE</td><td>接收FIFO半满中断使能写1使能中断。</td></tr><tr><td>14</td><td>TFHIE</td><td>发送FIFO半满中断使能写1使能中断。</td></tr><tr><td>13</td><td>RXRUNIE</td><td>正在接收数据中断使能写1使能中断。</td></tr><tr><td>12</td><td>TXRUNIE</td><td>正在传输数据中断使能</td></tr></table>

<table><tr><td>11</td><td>CMDRUNIE</td><td>正在传输命令中断使能写1使能中断。</td></tr><tr><td>10</td><td>DTBLKENDIE</td><td>数据块已发送/已接收中断使能写1使能中断。</td></tr><tr><td>9</td><td>STBITEIE</td><td>起始位错误中断使能写1使能中断。</td></tr><tr><td>8</td><td>DTENDIE</td><td>数据结束中断使能写1使能中断。</td></tr><tr><td>7</td><td>CMDSENDIE</td><td>命令已发送中断使能写1使能中断。</td></tr><tr><td>6</td><td>CMDRECVIE</td><td>命令响应已接收中断使能写1使能中断。</td></tr><tr><td>5</td><td>RXOREIE</td><td>接收FIFO上溢错误中断使能写1使能中断。</td></tr><tr><td>4</td><td>TXUREIE</td><td>发送FIFO下溢错误中断使能写1使能中断。</td></tr><tr><td>3</td><td>DTTMOUTIE</td><td>数据超时中断使能写1使能中断。</td></tr><tr><td>2</td><td>CMDTMOUTIE</td><td>命令响应超时中断使能写1使能中断。</td></tr><tr><td>1</td><td>DTCRCERRIE</td><td>数据CRC错误中断使能写1使能中断。</td></tr><tr><td>0</td><td>CCRCERRIE</td><td>命令响应CRC错误中断使能写1使能中断。</td></tr></table>

## 29.8.14. FIFO 计数寄存器（SDIO_FIFOCNT）

地址偏移：0x48

复位值：0x0000 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">FIFOCNT[23:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FIFOCNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>FIFOCNT[23:0]</td><td>FIFO计数器这些位定义了从FIFO中读取或写入到FIFO剩余的字数。当DATAEN置位时,它加载数据长度寄存器的值(如果SDIO_DATALEN是字对齐时,该值为SDIO_DATALEN[24:2];如果SDIO_DATALEN不是字对齐,该值为SDIO_DATALEN[24:2]+1),然后当写一个字到FIFO或从FIFO中读取一个字时,开始递减计数。</td></tr></table>

## 29.8.15. FIFO 数据寄存器（SDIO_FIFO）

地址偏移：0x80

复位值：0x0000 0000

该寄存器占用了 32 个 32 位的字，地址偏移从 0x80 到 0xFC。

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">FIFODT[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FIFODT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FIFODT[31:0]</td><td>接收FIFO数据或发送FIFO数据这些位为接收FIFO或发送FIFO的数据。读或写该寄存器相当于对FIFO读或写数据。</td></tr></table>
