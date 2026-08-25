## 29.5. CAN 寄存器

CAN0基地址：0x4001 A000

CAN1基地址：0x4001 B000

CAN2基地址：0x4001 C000

## 29.5.1. 控制寄存器 0（CAN_CTL0）

地址偏移：0x00

复位值：0x5900 000F

该寄存器中除了位30，28，25，19之外的其他位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器中除了位31，27，24，20之外的其他位都会被CAN_CTL0寄存器中的软件复位SWRST位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CANDIS</td><td>INAMOD</td><td>RFEN</td><td>HALT</td><td>NRDY</td><td>保留</td><td>SWRST</td><td>INAS</td><td colspan="2">保留</td><td>WERREN</td><td>LPS</td><td>PNEN</td><td>PNS</td><td>SRDIS</td><td>RPFQEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td></td><td>rw</td><td>r</td><td colspan="2"></td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DMAEN</td><td>PNMOD</td><td>LAPRIOEN</td><td>MST</td><td>FDEN</td><td>保留</td><td colspan="2">FS[1:0]</td><td colspan="3">保留</td><td colspan="5">MSZ[4:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="2">rw</td><td colspan="4"></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CANDIS</td><td>CAN禁能该位不会被CAN_CTL0寄存器中的软件复位SWRST位影响。0:使能CAN模块1:禁能CAN模块</td></tr><tr><td>30</td><td>INAMOD</td><td>暂停模式使能0:禁能暂停模式1:使能暂停模式</td></tr><tr><td>29</td><td>RFEN</td><td>Rx FIFO使能0:禁能Rx FIFO1:使能Rx FIFO</td></tr><tr><td>28</td><td>HALT</td><td>暂停CAN1:当CAN_CTL0寄存器的INAMOD位置位时进入暂停模式</td></tr><tr><td>27</td><td>NRDY</td><td>未准备好该位指示了协议控制器的时钟是否被禁用。当在暂停模式下,或在CAN_Disable模式下,协议控制器的时钟被禁用,CAN模块未准备好。0:CAN模块已准备好1:CAN模块未准备好</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>SWRST</td><td>软件复位当该位置位时,CAN内部状态机和CAN寄存器将被复位。该位在软件复位完成后将由硬件自动清零。当CAN_CTL0寄存器的LPS位置位时,软件复位不起作用。0:无作用1:软件复位</td></tr><tr><td>24</td><td>INAS</td><td>暂停模式状态0:不处于暂停模式1:处于暂停模式</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>WERREN</td><td>错误警告使能当该位置位时,CAN_ERR1寄存器中的警告中断标志TWERRIF和RWERRIF位将被使能,分别用于反映CAN_ERR1寄存器中的TWERRF和RWERRF位状态切换。0:禁能Tx和Rx错误警告1:使能Tx和Rx错误警告</td></tr><tr><td>20</td><td>LPS</td><td>低功耗状态0:不处于低功耗状态1:处于低功耗状态</td></tr><tr><td>19</td><td>PNEN</td><td>虚拟联网模式使能0:禁能虚拟联网模式1:使能虚拟联网模式</td></tr><tr><td>18</td><td>PNS</td><td>虚拟联网状态0:不处于虚拟联网状态1:处于虚拟联网状态</td></tr><tr><td>17</td><td>SRDIS</td><td>自接收禁能0:使能自接收1:禁能自接收</td></tr><tr><td>16</td><td>RPFQEN</td><td>接收私有过滤使能&amp;接收邮箱队列使能0:禁能接收私有过滤&amp;禁能接收邮箱队列1:使能接收私有过滤&amp;使能接收邮箱队列</td></tr><tr><td>15</td><td>DMAEN</td><td>DMA使能0:禁能Rx FIFO的DMA功能1:使能 Rx FIFO 的 DMA 功能</td></tr><tr><td>14</td><td>PNMOD</td><td>虚拟联网模式选择0:不选择虚拟联网模式1:选择虚拟联网模式</td></tr><tr><td>13</td><td>LAPRIOEN</td><td>本地仲裁优先级使能0:禁能本地仲裁优先级1:使能本地仲裁优先级</td></tr><tr><td>12</td><td>MST</td><td>邮箱中止发送0:禁能发送中止1:使能发送中止</td></tr><tr><td>11</td><td>FDEN</td><td>CAN FD模式使能0:禁能CAN FD模式1:使能CAN FD模式</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>FS[1:0]</td><td>格式选择该位域定义了Rx FIFO标识符过滤表元素的格式。00:格式A:每个标识符过滤表元素包含一个完整标识符(标准格式和扩展格式)01:格式B:每个标识符过滤表元素包含两个完整标准格式标识符或者两个扩展格式标识符其中14位10:格式C:每个标识符过滤表元素包含四个标准格式标识符其中8位或者四个扩展格式标识符其中8位11:格式D:不接受所有帧</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>MSZ[4:0]</td><td>内存大小该位域定义了帧发送和接收使用的最大内存大小。这个内存大小以4字(等于8字节数据段时的邮箱描述符大小)为单位计算,包含了邮箱和Rx FIFO占用的空间。在配置该位域之前,必须将CAN_STAT寄存器中的所有置位标志位都处理服务。00000:1单位00001:2单位</td></tr></table>

11111：32单位

## 29.5.2. 控制寄存器 1（CAN_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器中位 12，7，5，4，3 只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器中所有位都不会被 CAN_CTL0寄存器中的软件复位 SWRST 位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BOIE</td><td>ERRSIE</td><td>保留</td><td>LSCMOD</td><td>TWERRIE</td><td>RWERRIE</td><td>保留</td><td>BSSSEL</td><td>BSPMOD</td><td>ABORDIS</td><td>TSYNC</td><td>MTO</td><td>MMOD</td><td colspan="3">保留</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>BOIE</td><td>离线中断使能0:禁能离线中断1:使能离线中断</td></tr><tr><td>14</td><td>ERRSIE</td><td>错误汇总中断使能0:禁能错误汇总中断1:使能错误汇总中断</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>LSCMOD</td><td>回环静默模式0:禁能回环静默模式1:使能回环静默模式注意:在该模式下,不能置位CAN_CTL0寄存器的SRDIS位,和CAN_FDCTL寄存器的TDCEN位。</td></tr><tr><td>11</td><td>TWERRIE</td><td>发送错误警告中断使能只有当CAN_CTL0寄存器的WERREN位置位时才可写该位。当CAN_CTL0寄存器的WERREN位为0时,该位读为0。0:禁能发送错误警告中断1:使能发送错误警告中断</td></tr><tr><td>10</td><td>RWERRIE</td><td>接收错误警告中断使能只有当CAN_CTL0寄存器的WERREN位置位时才可写该位。当CAN_CTL0寄存器的WERREN位为0时,该位读为0。0:禁能接收错误警告中断1:使能接收错误警告中断</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BSSSEL</td><td>位采样同步选择0:CAN总线采样的两阶段同步1:CAN总线采样单级同步</td></tr><tr><td>7</td><td>BSPMOD</td><td>位采样模式0:接收位使用1个采样点1:接收位使用3个采样点</td></tr><tr><td>6</td><td>ABORDIS</td><td>自动离线恢复不使能0:使能自动离线恢复1:不使能自动离线恢复</td></tr><tr><td>5</td><td>TSYNC</td><td>时间同步使能0:禁能时间同步1:使能时间同步</td></tr><tr><td>4</td><td>MTO</td><td>邮箱发送顺序0:高优先级的邮箱先发送1:低邮箱编号的邮箱先发送</td></tr><tr><td>3</td><td>MMOD</td><td>监听模式0:禁能监听模式1:使能监听模式</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 29.5.3. 计数器寄存器（CAN_TIMER）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>计数器值</td></tr></table>


该位域包含用于产生时间戳的内部计数器值。


## 29.5.4. 接收邮箱公有过滤寄存器（CAN_RMPUBF）

地址偏移：0x10

复位值：0xXXXX XXXX

该寄存器位于 RAM。

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MFD31</td><td>MFD30</td><td>MFD29</td><td>MFD28</td><td>MFD27</td><td>MFD26</td><td>MFD25</td><td>MFD24</td><td>MFD23</td><td>MFD22</td><td>MFD21</td><td>MFD20</td><td>MFD19</td><td>MFD18</td><td>MFD17</td><td>MFD16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MFD15</td><td>MFD14</td><td>MFD13</td><td>MFD12</td><td>MFD11</td><td>MFD10</td><td>MFD9</td><td>MFD8</td><td>MFD7</td><td>MFD6</td><td>MFD5</td><td>MFD4</td><td>MFD3</td><td>MFD2</td><td>MFD1</td><td>MFD0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td rowspan="7">31:0</td><td rowspan="7">MFDx</td><td>邮箱过滤数据</td></tr><tr><td>MFD31 位用于过滤邮箱描述符的 RTR 域。</td></tr><tr><td>MFD30 位用于过滤邮箱描述符的 IDE 域。</td></tr><tr><td>MFDx(x = 0..28)用于过滤邮箱描述符的 ID 域。</td></tr><tr><td>0:不关心该位</td></tr><tr><td>1:参与比较</td></tr><tr><td>注:对于标准帧,MDF18~MFD28 位域用于过滤邮箱描述符 ID 字段。</td></tr></table>

## 29.5.5. 错误寄存器 0（CAN_ERR0）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器的所有位都只读，除了在暂停模式之外。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">REFCNT[7:0]</td><td colspan="8">TEFCNT[7:0]</td></tr><tr><td colspan="8">rw0</td><td colspan="8">rw0</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">RECNT[7:0]</td><td colspan="8">TECNT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>REFCNT[7:0]</td><td>FD 帧 BRS 位为隐性位时数据阶段的接收错误计数器该位域在暂停模式下只可写为0。</td></tr><tr><td>23:16</td><td>TEFCNT[7:0]</td><td>FD 帧 BRS 位为隐性位时数据阶段的发送错误计数器该位域在暂停模式下只可写为0。</td></tr><tr><td>15:8</td><td>RECNT[7:0]</td><td>CAN 协议定义的接收错误计数器</td></tr><tr><td>7:0</td><td>TECNT[7:0]</td><td>CAN 协议定义的发送错误计数器</td></tr></table>

## 29.5.6. 错误寄存器 1（CAN_ERR1）

地址偏移：0x20

复位值：0x0004 0009

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BRFERR</td><td>BDFERR</td><td>保留</td><td>CRCFERR</td><td>FMFERR</td><td>STFFERR</td><td colspan="4">保留</td><td>ERROVR</td><td>ERRFSF</td><td>BORF</td><td>SYN</td><td>TWERRIF</td><td>RWERRIF</td></tr><tr><td>rc</td><td>rc</td><td></td><td>rc</td><td>rc</td><td>rc</td><td colspan="4"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>r</td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BRERR</td><td>BDERR</td><td>ACKERR</td><td>CRCERR</td><td>FMERR</td><td>STFERR</td><td>TWERRF</td><td>RWERRF</td><td>IDLEF</td><td>TS</td><td colspan="2">ERRSI[1:0]</td><td>RS</td><td>BOF</td><td>ERRSF</td><td>保留</td></tr><tr><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="2">r</td><td>r</td><td>rc_w1</td><td>rc_w1</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BRFERR</td><td>FD帧BRS位为隐性位时数据阶段的位隐性错误0:没有发生错误1:至少有一个位发送为隐性位,接收为显性位</td></tr><tr><td>30</td><td>BDFERR</td><td>FD帧BRS位为隐性位时数据阶段的位显性错误0:没有发生错误1:至少有一个位发送为显性位,接收为隐性位</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>CRCFERR</td><td>FD帧BRS位为隐性位时数据阶段的CRC错误0: 没有发生错误1: 发生了一个CRC错误</td></tr><tr><td>27</td><td>FMFERR</td><td>FD帧BRS位为隐性位时数据阶段的格式错误0: 没有发生错误1: 发生了一个格式错误</td></tr><tr><td>26</td><td>STFFERR</td><td>FD帧BRS位为隐性位时数据阶段的填充错误0: 没有发生错误1: 发生了一个填充错误</td></tr><tr><td>25:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>ERROVR</td><td>错误溢出该位表示在某一个错误标志位已经置位的情况下,又检测到了一个错误。0: 没有发生错误溢出1: 发生了错误溢出</td></tr><tr><td>20</td><td>ERRFSF</td><td>FD帧BRS位为隐性位时数据阶段的错误汇总标志该位是下列位的逻辑或:CAN_ERR1[31]: 位隐性错误CAN_ERR1[30]: 位显性错误CAN_ERR1[28]: CRC错误CAN_ERR1[27]: 格式错误CAN_ERR1[26]: 填充错误</td></tr><tr><td>19</td><td>BORF</td><td>离线恢复标志当检测到CAN总线上总线恢复序列时,该位置位,指示CAN节点可以从离线状态恢复。0: 没有事件发生1: 发生了离线恢复序列事件</td></tr><tr><td>18</td><td>SYN</td><td>同步标志0: 未与CAN总线同步1: 与CAN总线同步</td></tr><tr><td>17</td><td>TWERRIF</td><td>发生错误警告中断标志该位在离线状态时不使用。0: 没有事件发生1: CAN_ERR1寄存器的TWERRF位从0变为1</td></tr><tr><td>16</td><td>RWERRIF</td><td>接收错误警告中断标志该位在退出虚拟联网模式时将更新。0: 没有事件发生1: CAN_ERR1 寄存器的 RWERRF 位从 0 变为 1</td></tr><tr><td>15</td><td>BRERR</td><td>所有格式帧的位隐性错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 至少有一个位发送为隐性位,接收为显性位</td></tr><tr><td>14</td><td>BDERR</td><td>所有格式帧的位显性错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 至少有一个位发送为显性位,接收为隐性位</td></tr><tr><td>13</td><td>ACKERR</td><td>ACK错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 发生了一个 ACK 错误</td></tr><tr><td>12</td><td>CRCERR</td><td>CRC错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 发生了一个 CRC 错误</td></tr><tr><td>11</td><td>FMERR</td><td>格式错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 发生了一个格式错误</td></tr><tr><td>10</td><td>STFERR</td><td>填充错误该位在退出虚拟联网模式时将更新。0: 没有发生错误1: 发生了一个填充错误</td></tr><tr><td>9</td><td>TWERRF</td><td>发送错误警告标志0: 没有事件发生1: CAN_ERR0 寄存器的 TECNT[7:0]值大于等于 96</td></tr><tr><td>8</td><td>RWERRF</td><td>接收错误警告标志该位在退出虚拟联网模式时将更新。0: 没有事件发生1: CAN_ERR0 寄存器的 RECNT[7:0]值大于等于 96</td></tr><tr><td>7</td><td>IDLEF</td><td>空闲标志0: 没有事件发生1: 处于总线空闲状态</td></tr><tr><td>6</td><td>TS</td><td>发送状态0: CAN节点不处于发送状态1: CAN节点处于发送状态</td></tr><tr><td>5:4</td><td>ERRSI[1:0]</td><td>错误状态指示当CAN_CTL1寄存器的MMOD位,和CAN_CTL0寄存器的SWRST位都置位时,该位会复位一个CAN位时间,然后变为监听模式时的0b01值。00: 主动错误01: 被动错误1x: 离线</td></tr><tr><td>3</td><td>RS</td><td>接收状态0: CAN节点不处于接收状态1: CAN节点处于接收状态</td></tr><tr><td>2</td><td>BOF</td><td>离线标志0: 没有事件发生1: 处于离线状态</td></tr><tr><td>1</td><td>ERRSF</td><td>错误汇总标志该位是下列位的逻辑或:CAN_ERR1[15]: 位隐性错误CAN_ERR1[14]: 位显性错误CAN_ERR1[13]: ACK错误CAN_ERR1[12]: CRC错误CAN_ERR1[11]: 格式错误CAN_ERR1[10]: 填充错误</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 29.5.7. 中断使能寄存器（CAN_INTEN）

地址偏移：0x28

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MIE31</td><td>MIE30</td><td>MIE29</td><td>MIE28</td><td>MIE27</td><td>MIE26</td><td>MIE25</td><td>MIE24</td><td>MIE23</td><td>MIE22</td><td>MIE21</td><td>MIE20</td><td>MIE19</td><td>MIE18</td><td>MIE17</td><td>MIE16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MIE15</td><td>MIE14</td><td>MIE13</td><td>MIE12</td><td>MIE11</td><td>MIE10</td><td>MIE9</td><td>MIE8</td><td>MIE7</td><td>MIE6</td><td>MIE5</td><td>MIE4</td><td>MIE3</td><td>MIE2</td><td>MIE1</td><td>MIE0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>31:0</td><td>MIEx</td><td>消息发送和接收中断使能当RxFIFO禁能时,这些位用于邮箱编号x(参考邮箱编号)的中断配置。当RxFIFO使能时,MIE5到MIE7都用于RxFIFO的中断配置,邮箱的中断配置位为位x对应于邮箱编号x(参考邮箱编号)。0:禁能相应中断1:使能相应中断</td></tr></table>

## 29.5.8. 状态寄存器（CAN_STAT）

地址偏移：0x30

复位值：0x0000 0000

当 CAN_CTL0 寄存器的 RFEN 位的配置改变时，该寄存器的位 1 到位 7 都会被清零。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MS31</td><td>MS30</td><td>MS29</td><td>MS28</td><td>MS27</td><td>MS26</td><td>MS25</td><td>MS24</td><td>MS23</td><td>MS22</td><td>MS21</td><td>MS20</td><td>MS19</td><td>MS18</td><td>MS17</td><td>MS16</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MS15</td><td>MS14</td><td>MS13</td><td>MS12</td><td>MS11</td><td>MS10</td><td>MS9</td><td>MS8</td><td>MS7_RFO</td><td>MS6_RFW</td><td>MS5_RFNE</td><td>MS4_RES</td><td>MS3_RES</td><td>MS2_RES</td><td>MS1_RES</td><td>MS0_RFC</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>MSx</td><td>邮箱x状态x是邮箱编号,参考邮箱编号。0: 邮箱描述符没有发生消息的成功发送或接收1: 邮箱描述符发生了一次消息的成功发送或接收</td></tr><tr><td>7</td><td>MS7_RFO</td><td>邮箱7状态/RxFIFO溢出0: 当RxFIFO禁能时,邮箱7描述符没有发生消息的成功发送或接收/当RxFIFO使能时,RxFIFO没有发生溢出。1: 当RxFIFO禁能时,邮箱7描述符发生了一次消息的成功发送或接收/当RxFIFO使能时,RxFIFO发生了溢出。</td></tr><tr><td>6</td><td>MS6_RFW</td><td>邮箱6状态/RxFIFO警告0: 当RxFIFO禁能时,邮箱6描述符没有发生消息的成功发送或接收/当RxFIFO使能时,RxFIFO没有发生快满了的警告。1: 当RxFIFO禁能时,邮箱6描述符发生了一次消息的成功发送或接收/当RxFIFO使能时,RxFIFO发生快满了的警告。</td></tr><tr><td>5</td><td>MS5_RFNE</td><td>邮箱5状态/RxFIFO非空0: 当RxFIFO禁能时,邮箱5描述符没有发生消息的成功发送或接收/当RxFIFO使能时,Rx FIFO为主。1:当Rx FIFO禁能时,邮箱5描述符发生了一次消息的成功发送或接收/当RxFIFO使能时,Rx FIFO非空。</td></tr><tr><td>4</td><td>MS4_RES</td><td>邮箱4状态/保留与MS1_RES描述类似。</td></tr><tr><td>3</td><td>MS3_RES</td><td>邮箱3状态/保留与MS1_RES描述类似。</td></tr><tr><td>2</td><td>MS2_RES</td><td>邮箱2状态/保留与MS1_RES描述类似。</td></tr><tr><td>1</td><td>MS1_RES</td><td>邮箱1状态/保留0:当Rx FIFO禁能时,邮箱1描述符没有发生消息的成功发送或接收/当Rx FIFO使能时,该位保留。1:当Rx FIFO禁能时,邮箱1描述符发生了一次消息的成功发送或接收/当RxFIFO使能时,该位保留。</td></tr><tr><td>0</td><td>MS0_RFC</td><td>邮箱0状态/清Rx FIFO位0:当Rx FIFO禁能时,邮箱0描述符没有发生消息的成功发送或接收/当Rx FIFO使能时,不起作用。1:当Rx FIFO禁能时,邮箱0描述符发生了一次消息的成功发送或接收/当RxFIFO使能时,清Rx FIFO,该位只允许在暂停模式下写入,参考清FIFO。</td></tr></table>

## 29.5.9. 控制寄存器 2（CAN_CTL2）

地址偏移：0x34

复位值：0x00A0 0000

该寄存器中除了位 31，30 之外的其他位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。该寄存器中所有位都不会被 CAN_CTL0寄存器中的软件复位 SWRST 位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>ERRFSIE</td><td>BORIE</td><td colspan="2">保留</td><td colspan="4">RFFN[3:0]</td><td colspan="5">ASD[4:0]</td><td>RFO</td><td>RRFRMS</td><td>IDERTR_RMF</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td colspan="4">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ITSRC</td><td>PREEN</td><td>保留</td><td>ISO</td><td>EFDIS</td><td colspan="11">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="12"></td></tr></table>

<table><tr><td>31</td><td>ERRFSIE</td><td>FD帧BRS位为隐性位时数据阶段的错误汇总中断使能0:禁能FD帧BRS位为隐性位时数据阶段的错误汇总中断1:使能 FD 帧 BRS 位为隐性位时数据阶段的错误汇总中断</td></tr><tr><td>30</td><td>BORIE</td><td>离线恢复中断使能0:禁能离线恢复中断1:使能离线恢复中断</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>RFFN[3:0]</td><td>Rx FIFO过滤器数目</td></tr></table>


表 29-12. Rx FIFO 标识符过滤表元素数目


<table><tr><td>RFFN[3:0]</td><td>Rx FIFO标识符过滤表元素数目</td><td>Rx FIFO占用的空间</td><td>可用的邮箱</td></tr><tr><td>0000</td><td>8</td><td>邮箱描述符0 - 7</td><td>邮箱8 - 31</td></tr><tr><td>0001</td><td>16</td><td>邮箱描述符0 - 9</td><td>邮箱10 - 31</td></tr><tr><td>0002</td><td>24</td><td>邮箱描述符0 - 11</td><td>邮箱12 - 31</td></tr><tr><td>0003</td><td>32</td><td>邮箱描述符0 - 13</td><td>邮箱14 - 31</td></tr><tr><td>0004</td><td>40</td><td>邮箱描述符0 - 15</td><td>邮箱16 - 31</td></tr><tr><td>0005</td><td>48</td><td>邮箱描述符0 - 17</td><td>邮箱18 - 31</td></tr><tr><td>0006</td><td>56</td><td>邮箱描述符0 – 19</td><td>邮箱20 - 31</td></tr><tr><td>0007</td><td>64</td><td>邮箱描述符0 – 21</td><td>邮箱22 - 31</td></tr><tr><td>0008</td><td>72</td><td>邮箱描述符0 – 23</td><td>邮箱24 - 31</td></tr><tr><td>0009</td><td>80</td><td>邮箱描述符0 – 25</td><td>邮箱26 - 31</td></tr><tr><td>000A</td><td>88</td><td>邮箱描述符0 – 27</td><td>邮箱28 - 31</td></tr><tr><td>000B</td><td>96</td><td>邮箱描述符0 – 29</td><td>邮箱30 - 31</td></tr><tr><td>000C</td><td>104</td><td>邮箱描述符0 – 31</td><td>无</td></tr><tr><td>其他</td><td>104</td><td>邮箱描述符0 - 31</td><td>无</td></tr></table>

<table><tr><td></td><td></td><td>配置该位域时,需注意不要使Rx FIFO占用的内存空间超过由CAN_CTL0寄存器MSZ[4:0]位域配置的可用的内存空间大小,否则超过的部分将不起作用。</td></tr><tr><td>23:19</td><td>ASD[4:0]</td><td>仲裁启动延迟该位域定义了在发送仲裁过程启动之前需要延迟多少个CAN位时间。</td></tr><tr><td>18</td><td>RFO</td><td>接收过滤顺序0:先过滤比较Rx FIFO1:先过滤比较邮箱</td></tr><tr><td>17</td><td>RRFRMS</td><td>远程请求帧存储0:当找到了CODE为RANSWER的并且ID相匹配的邮箱,则产生一个远程应答帧。1:当找到了CODE为RANSWER的并且ID相匹配的邮箱,则将这个远程请求帧如同数据帧一样存储起来,而不自动发送远程应答帧。</td></tr><tr><td>16</td><td>IDERTR_RMF</td><td>邮箱接收时IDE和RTR域的过滤类型该位定义了接收邮箱描述符中IDE和RTR域与接收的位的匹配类型。0:总是比较IDE域,从不比较RTR域。忽略相关过滤寄存器中的过滤数据配置。1:过滤比较IDE和RTR域,使用相关过滤寄存器中的过滤数据配置。</td></tr><tr><td>15</td><td>ITSRC</td><td>内部计数器时钟源0:CAN波特率1:TRIGSEL输出的外部触发CANx_EX_TIME_TICK</td></tr><tr><td>14</td><td>PREEN</td><td>CAN规范中的协议异常检测使能0:禁能协议异常检测1:使能协议异常检测</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ISO</td><td>ISO CAN FD0:使用非ISO CAN FD协议1:使用ISO CAN FD协议</td></tr><tr><td>11</td><td>EFDIS</td><td>边沿过滤禁能0:使能边沿过滤1:禁能边沿过滤</td></tr><tr><td>10:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 29.5.10. 常规帧 CRC 寄存器（CAN_CRCC）

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">ANTM[4:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">CRCTC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>ANTM[4:0]</td><td>发送 CRCTC[14:0]值的相关联的邮箱的编号</td></tr></table>

该位域包含发送了 CRC 值为 CRCTC[14:0]的邮箱的编号。

15 保留 必须保持复位值。

14:0 CRCTC[14:0] 发送的常规帧CRC计算值

## 29.5.11. 接收 FIFO 共有过滤寄存器（CAN_RFIFOPUBF）

地址偏移：0x48

复位值：0xXXXX XXXX

该寄存器位域 RAM 区域。

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FFD31</td><td>FFD30</td><td>FFD29</td><td>FFD27</td><td>FFD27</td><td>FFD26</td><td>FFD25</td><td>FFD24</td><td>FFD23</td><td>FFD22</td><td>FFD21</td><td>FFD20</td><td>FFD19</td><td>FFD18</td><td>FFD17</td><td>FFD16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FFD15</td><td>FFD14</td><td>FFD13</td><td>FFD12</td><td>FFD11</td><td>FFD10</td><td>FFD9</td><td>FFD8</td><td>FFD7</td><td>FFD6</td><td>FFD5</td><td>FFD4</td><td>FFD3</td><td>FFD2</td><td>FFD1</td><td>FFD0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FFDx</td><td>Rx FIFO 过滤数据该位用于相应的标识符过滤表元素中各个位的过滤,过滤表元素中的保留位除外。0:不关心该位1:参与比较</td></tr></table>

## 29.5.12. 接收 FIFO 标识符过滤元素匹配序号寄存器（CAN_RFIFOIFMN）

地址偏移：0x4C

复位值：0xXXXX XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">IDFMN[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>IDFMN[8:0]</td><td>标识符过滤元素匹配序号只有当CAN_STAT寄存器的MS5_RFNE位置位时,该位域才有效。该位域表示在接收FIFO输出中的消息是与哪个标识符过滤元素相匹配。如果有超过一个相匹配的标识符过滤元素,则该位域指示最小序号的匹配的标识符过滤元素。</td></tr></table>

## 29.5.13. 位时间寄存器（CAN_BT）

地址偏移：0x50

复位值：0x0100 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器中所有位都不会被 CAN_CTL0寄存器中的软件复位 SWRST 位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">BAUDPSC[9:0]</td><td colspan="5">SJW[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">PTS[5:0]</td><td colspan="5">PBS1[4:0]</td><td colspan="5">PBS2[4:0]</td></tr><tr><td colspan="6">rw</td><td colspan="5">rwr</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>BAUDPSC[9:0]</td><td>波特率分频系数CAN波特率分配系数= BAUDPSC[9:0] + 1。</td></tr><tr><td>20:16</td><td>SJW[4:0]</td><td>再同步补偿宽度再同步补偿占用的时间单元数量 = SJW[4:0] + 1</td></tr><tr><td>15:10</td><td>PTS[5:0]</td><td>传播时间段传播时间段占用的时间单元数量 = PTS[5:0] + 1</td></tr><tr><td>9:5</td><td>PBS1[4:0]</td><td>相位缓冲段1相位缓冲段1占用的时间单元数量 = PBS1[4:0] + 1</td></tr><tr><td>4:0</td><td>PBS2[4:0]</td><td>相位缓冲段2相位缓冲段2占用的时间单元数量 = PBS2[4:0] + 1</td></tr></table>

## 29.5.14. 接收 FIFO/邮箱私有过滤 x 寄存器（CAN_RFIFOMPFx）（x=0..31）

地址偏移：0x880 + 4 * x

复位值：0xXXXX XXXX

该寄存器位于 RAM 区域。

这些寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

这些寄存器中所有位都不会被 CAN_CTL0 寄存器中的软件复位 SWRST 位复位。

这些寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FMFD31</td><td>FMFD30</td><td>FMFD29</td><td>FMFD27</td><td>FMFD27</td><td>FMFD26</td><td>FMFD25</td><td>FMFD24</td><td>FMFD23</td><td>FMFD22</td><td>FMFD21</td><td>FMFD20</td><td>FMFD19</td><td>FMFD18</td><td>FMFD17</td><td>FMFD16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FMFD15</td><td>FMFD14</td><td>FMFD13</td><td>FMFD12</td><td>FMFD11</td><td>FMFD10</td><td>FMFD9</td><td>FMFD8</td><td>FMFD7</td><td>FMFD6</td><td>FMFD5</td><td>FMFD4</td><td>FMFD3</td><td>FMFD2</td><td>FMFD1</td><td>FMFD0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FMFDx</td><td>FIFO / 邮箱过滤数据当用作邮箱过滤时,参考CAN_RMPUBF寄存器的MFDx位。当用作Rx FIFO 过滤时,参考 CAN_RFIFOPUBF 寄存器的 FFDx 位。0:不关心该位1:参与比较</td></tr></table>

## 29.5.15. 虚拟联网模式控制寄存器 0（CAN_PN_CTL0）

地址偏移：0xB00

复位值：0x0000 0100

该寄存器中除了位 17，16 之外的其他位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>WTOIE</td><td>WMIE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">NMM[7:0]</td><td colspan="2">保留</td><td colspan="2">DATAFT[1:0]</td><td colspan="2">IDFT[1:0]</td><td colspan="2">FFT[1:0]</td></tr><tr><td></td><td></td><td></td><td colspan="7">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:18</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>17</td><td colspan="3">WTOIE</td><td colspan="12">超时唤醒中断使能0:禁能超时唤醒中断1:使能超时唤醒中断</td></tr><tr><td>16</td><td colspan="3">WMIE</td><td colspan="12">匹配唤醒中断使能0:禁能匹配唤醒中断1:使能匹配唤醒中断</td></tr><tr><td>15:8</td><td colspan="3">NMM[7:0]</td><td colspan="12">消息匹配次数事件计数器用于唤醒帧过滤,在检测到N次匹配事件后,会产生一个事件输出。00000001:N=100000010:N=2......11111111:N=255</td></tr><tr><td>7:6</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>5:4</td><td colspan="3">DATAFT[1:0]</td><td colspan="12">在虚拟联网模式下DATA域的过滤类型00:只有当帧的DATA域与相应的期望数据寄存器中DATA位域一致时,认为这是一个DATA匹配的帧01:只有当帧的DATA域大于等于相应的期望数据寄存器中DATA下限值时,认为这是一个DATA匹配的帧10:只有当帧的DATA域小于等于相应的期望数据寄存器中DATA上限值时,认为这是一个DATA匹配的帧11:只有当帧的DATA域大于等于相应的期望数据寄存器中DATA下限值,并且小于等于相应的期望数据寄存器中DATA上限值时,认为这是一个DATA匹配的帧</td></tr><tr><td>3:2</td><td colspan="3">IDFT[1:0]</td><td colspan="12">在虚拟联网模式下ID域的过滤类型00:只有当帧的ID域与相应的期望标识符寄存器中ID位域一致时,认为这是一个ID匹配的帧01:只有当帧的ID域大于等于相应的期望标识符寄存器中ID下限值时,认为这是一个ID匹配的帧10:只有当帧的ID域小于等于相应的期望标识符寄存器中ID上限值时,认为这是一个ID匹配的帧11:只有当帧的ID域大于等于相应的期望标识符寄存器中ID下限值时,并且小于等于相应的期望标识符寄存器中ID上限值时,认为这是一个ID匹配的帧</td></tr><tr><td>1:0</td><td colspan="3">FFT[1:0]</td><td colspan="12">在虚拟联网模式下帧的过滤类型00:除了DATA,DLC域之外的其他域都需要过滤比较01:所有域都需要过滤比较10:除了DATA,DLC域之外的其他域都需要过滤比较NMM[7:0]次数</td></tr></table>

11：所有域都需要过滤比较 NMM[7:0]次数

## 29.5.16. 虚拟联网模式超时寄存器（CAN_PN_TO）

地址偏移：0xB04

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WTO[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>WTO[15:0]</td><td>超时唤醒</td></tr></table>


该超时值按照CAN位时间的64倍进行计数。默认关闭超时唤醒。


## 29.5.17. 虚拟联网模式状态寄存器（CAN_PN_STAT）

地址偏移：0xB08

复位值：0x0000 0080

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>WTOS</td><td>WMS</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">MMCNT[7:0]</td><td>MMCNTS</td><td colspan="7">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>WTOS</td><td>超时唤醒标志状态0:没有发生超时唤醒事件1:发生了超时唤醒事件</td></tr><tr><td>16</td><td>WMS</td><td>匹配唤醒标志状态0:没有发生匹配唤醒事件1:发生了匹配唤醒事件</td></tr><tr><td>15:8</td><td>MMCNT[7:0]</td><td>在虚拟联网模式下的帧匹配计数该位域指示了在虚拟联网模式下的匹配的帧的计数值。该位域在进入虚拟联网模式时由CAN模块复位,并且受软件复位的影响。</td></tr><tr><td>7</td><td>MMCNTS</td><td>帧匹配计数状态当该位置位时,指示MMCNT[7:0]值有效。0:帧匹配计数MMCNT[7:0]正在更新1:帧匹配计数MMCNT[7:0]有效</td></tr><tr><td>6:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 29.5.18. 虚拟联网模式期望标识符 0 寄存器（CAN_PN_EID0）

地址偏移：0xB0C

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>EIDE</td><td>ERTR</td><td colspan="13">EID_ELT[28:16]</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">EID_ELT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>EIDE</td><td>在虚拟联网模式下的期望IDE0: 标准格式1: 扩展格式</td></tr><tr><td>29</td><td>ERTR</td><td>在虚拟联网模式下的期望RTR0: 数据帧1: 远程帧</td></tr><tr><td>28:0</td><td>EIDF_EL[28:0]</td><td>在虚拟联网模式下的期望ID / 期望的ID下限值</td></tr></table>

当CAN_PN_CTL0寄存器的IDFT[1:0]位域为0 / 1 / 2时，该位域用作期望ID，当IDFT[1:0]位域为3时，该位域用作期望的ID下限值。

对于扩展格式帧，使用所有的29位。

对于标准格式帧，使用位18到28。

## 29.5.19. 虚拟联网模式期望 DLC 寄存器（CAN_PN_EDLC）

地址偏移：0xB10

复位值：0x0000 0008

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">DLCELT[3:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">DLCEHT[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>DLCELT[3:0]</td><td>在虚拟联网模式下的期望DLC下限值</td></tr><tr><td>15:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>DLCEHT[3:0]</td><td>在虚拟联网模式下的期望DLC上限值</td></tr></table>

## 29.5.20. 虚拟联网模式期望数据低字 0 寄存器（CAN_PN_EDL0）

地址偏移：0xB14

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB0ELT[7:0]</td><td colspan="8">DB1ELT[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB2ELT[7:0]</td><td colspan="8">DB3ELT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB0ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 0 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>23:16</td><td>DB1ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 1 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>15:8</td><td>DB2ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 2 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>7:0</td><td>DB3ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 3 下限值当 CAN_PN_CTL0 寄存器的 DATAFT[1:0]位域为 0 / 1 / 2 时,该位域用作期望的 DATA,当 DATAFT[1:0]位域为 3 时,该位域用作期望的 DATA 下限值。</td></tr></table>

## 29.5.21. 虚拟联网模式期望数据低字 1 寄存器（CAN_PN_EDL1）

地址偏移：0xB18

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB4ELT[7:0]</td><td colspan="8">DB5ELT[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB6ELT[7:0]</td><td colspan="8">DB7ELT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB4ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 4 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>23:16</td><td>DB5ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 5 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>15:8</td><td>DB6ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 6 下限值参考 DB3ELT[7:0]描述。</td></tr><tr><td>7:0</td><td>DB7ELT[7:0]</td><td>在虚拟联网模式下的期望数据字节 7 下限值参考 DB3ELT[7:0]描述。</td></tr></table>

## 29.5.22. 虚拟联网模式标识符过滤器 / 期望标识符 1 寄存器（CAN_PN_IFEID1）

地址偏移：0x B1C

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>IDEFD</td><td>RTRFD</td><td colspan="13">IDFD_EHT[28:16]</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDFD_EHT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>IDEFD</td><td>在虚拟联网模式下的 IDE 过滤数据0:不关心该位1:参与比较</td></tr><tr><td>29</td><td>RTRFD</td><td>在虚拟联网模式下的 RTR 过滤数据0:不关心该位1:参与比较</td></tr><tr><td>28:0</td><td>IDFD_EHT[28:0]</td><td>在虚拟联网模式下的ID过滤数据 / 期望的ID上限值ID过滤数据(当CAN_PN_CTL0寄存器的IDFT[1:0]位域为0时):0:不关心该位1:参与比较ID期望上限值(当IDFT[1:0]位域为3时)。保留(当IDFT[1:0]位域为1或者2时)。对于扩展格式帧,使用所有29位。对于标准格式帧,使用位18到28。</td></tr></table>

## 29.5.23. 虚拟联网模式数据 0 过滤器 / 期望数据高字 0 寄存器（CAN_PN_DF0EDH0）

地址偏移：0xB20

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB0FD_EHT[7:0]</td><td colspan="8">DB1FD_EHT[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB2FD_EHT[7:0]</td><td colspan="8">DB3FD_EHT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB0FD_EHT[7:0]</td><td>在虚拟联网模式下的数据字节0过滤数据 / 数据字节0期望上限值参考DB3FD_EHT[7:0]描述。</td></tr><tr><td>23:16</td><td>DB1FD_EHT[7:0]</td><td>在虚拟联网模式下的数据字节1过滤数据 / 数据字节1期望上限值参考DB3FD_EHT[7:0]描述。</td></tr><tr><td>15:8</td><td>DB2FD_EHT[7:0]</td><td>在虚拟联网模式下的数据字节2过滤数据 / 数据字节2期望上限值参考DB3FD_EHT[7:0]描述。</td></tr><tr><td>7:0</td><td>DB3FD_EHT[7:0]</td><td>在虚拟联网模式下的数据字节3过滤数据 / 数据字节3期望上限值数据字节3过滤数据(当CAN_PN_CTL0寄存器的DATAFT[1:0]位域为0时):0:不关心该位1:参与比较数据字节3期望上限值(当DATAFT[1:0]位域为3时)。保留(当DATAFT[1:0]位域为1或者2时)。</td></tr></table>

## 29.5.24. 虚拟联网模式数据 1 过滤器 / 期望数据高字 1 寄存器（CAN_PN_DF1EDH1）

地址偏移：0xB24

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB4FD_HTF[7:0]</td><td colspan="8">DB5FD_HTF[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB6FD_HTF[7:0]</td><td colspan="8">DB7FD_HTF[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB4FD_HTF[7:0]</td><td>在虚拟联网模式下的数据字节4过滤数据 / 数据字节4期望上限值参考DB3FD_EHT[7:0]描述。</td></tr></table>

<table><tr><td>23:16</td><td>DB5FD_HTF[7:0]</td><td>在虚拟联网模式下的数据字节5过滤数据 / 数据字节5期望上限值参考DB3FD_EHT[7:0]描述。</td></tr><tr><td>15:8</td><td>DB6FD_HTF[7:0]</td><td>在虚拟联网模式下的数据字节6过滤数据 / 数据字节6期望上限值参考DB3FD_EHT[7:0]描述。</td></tr><tr><td>7:0</td><td>DB7FD_HTF[7:0]</td><td>在虚拟联网模式下的数据字节7过滤数据 / 数据字节7期望上限值参考DB3FD_EHT[7:0]描述。</td></tr></table>

## 29.5.25. 虚拟联网模式接收唤醒邮箱x控制状态信息寄存器（CAN_PN_RWMxCS）（x=0..3）

地址偏移：0xB40 + 16 * x

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>RSRR</td><td>RIDE</td><td>RRTR</td><td colspan="4">RDLC[3:0]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>RSRR</td><td>接收到的SRR位</td></tr><tr><td>21</td><td>RIDE</td><td>接收到的IDE位0:帧为标准格式1:帧为扩展格式</td></tr><tr><td>20</td><td>RRTR</td><td>接收到的RTR位0:帧为数据帧1:帧为远程帧</td></tr><tr><td>19:16</td><td>RDLC[3:0]</td><td>接收到的DLC域该位域指示了有效的数据字节长度。</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 29.5.26. 虚拟联网模式接收唤醒邮箱 x 标识符寄存器（CAN_PN_RWMxI）（x=0..3）

地址偏移：0xB44 + 16 * x

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="13">RID[28:16]</td></tr><tr><td colspan="9"></td><td colspan="7">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:0</td><td>RID[28:16]</td><td>接收到的ID域对于扩展格式帧,使用这29位用于ID存储。对于标准格式帧,使用位18到位28用于ID存储。</td></tr></table>

## 29.5.27. 虚拟联网模式接收唤醒邮箱 x 数据 0 寄存器（CAN_PN_RWMxD0）（x=0..3）

地址偏移：0xB48 + 16 * x

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">RDB0[7:0]</td><td colspan="8">RDB1[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">RDB2[7:0]</td><td colspan="8">RDB3[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>RDB0[7:0]</td><td>接收到的数据字节0</td></tr><tr><td>23:16</td><td>RDB1[7:0]</td><td>接收到的数据字节1</td></tr><tr><td>15:8</td><td>RDB2[7:0]</td><td>接收到的数据字节2</td></tr><tr><td>7:0</td><td>RDB3[7:0]</td><td>接收到的数据字节3</td></tr></table>

## 29.5.28. 虚拟联网模式接收唤醒邮箱 x 数据 1 寄存器（CAN_PN_RWMxD1）（x=0..3）

地址偏移：0xB4C + 16 * x

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">RDB4[7:0]</td><td colspan="8">RDB5[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">RDB6[7:0]</td><td colspan="8">RDB7[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>RDB4[7:0]</td><td>接收到的数据字节 4</td></tr><tr><td>23:16</td><td>RDB5[7:0]</td><td>接收到的数据字节 5</td></tr><tr><td>15:8</td><td>RDB6[7:0]</td><td>接收到的数据字节 6</td></tr><tr><td>7:0</td><td>RDB7[7:0]</td><td>接收到的数据字节 7</td></tr></table>

## 29.5.29. FD 控制寄存器（CAN_FDCTL）

地址偏移：0xC00

复位值：0x8000 0101

该寄存器中位 17:16，15，12:8 只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器不会被 CAN_CTL0 寄存器中的软件复位 SWRST 位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BRSEN</td><td colspan="13">保留</td><td colspan="2">MDSZ[1:0]</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TDCEN</td><td>TDCS</td><td>保留</td><td colspan="5">TDCO[4:0]</td><td colspan="2">保留</td><td colspan="6">TDCV[5:0]</td></tr><tr><td>rw</td><td>rc_w1</td><td colspan="8">rw</td><td colspan="6">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BRSEN</td><td>数据阶段波特率切换使能0:不切换波特率1:当发送邮箱中的BRS位为隐形位'1'时,位速率需要在数据阶段从正常波特率切换到预先设置的数据波特率。</td></tr><tr><td>30:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>MDSZ[1:0]</td><td>邮箱数据大小00:每个邮箱8个字节数据01:每个邮箱16个字节数据10:每个邮箱32个字节数据</td></tr><tr><td></td><td></td><td>11:每个邮箱64个字节数据</td></tr><tr><td>15</td><td>TDCEN</td><td>传输延迟补偿使能注意:在回环静默模式下必须关闭传输延迟补偿功能。0:禁能传输延迟补偿1:使能传输延迟补偿</td></tr><tr><td>14</td><td>TDCS</td><td>传输延迟补偿状态当该位置位时,表示传输延迟超出补偿了补偿范围,无法正确地补偿传输延迟用于位校验。0:传输延迟在补偿范围内1:传输延迟超出补偿范围</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>TDCO[4:0]</td><td>传输延迟补偿偏置这些位被用于设置当FD帧BRS位为隐性位时的次级采样点(SSP)基于测量的补偿时间的偏移,测量的补偿时间是由硬件计算信号从CAN_TX发出到从CAN_RX接收到的过程的延迟时间得出的。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>TDCV[5:0]</td><td>传输延迟补偿值该位域由硬件设置,显示当前测量的传输延迟值与传输延迟补偿偏置之和。</td></tr></table>

## 29.5.30. FD 位时间寄存器（CAN_FDBT）

地址偏移：0xC04

复位值：0x0000 0000

该寄存器中所有位都只可在暂停模式下配置，它们在其他模式下被硬件锁定。

该寄存器不会被 CAN_CTL0 寄存器中的软件复位 SWRST 位复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="10">DBAUDPSC[9:0]</td><td>保留</td><td colspan="3">DSJW[2:0]</td></tr><tr><td colspan="13">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="5">DPTS[4:0]</td><td colspan="2">保留</td><td colspan="3">DPBS1[2:0]</td><td colspan="2">保留</td><td colspan="3">DPBS2[2:0]</td></tr><tr><td colspan="6">rw</td><td colspan="6">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:20</td><td>DBAUDPSC[9:0]</td><td>数据位时间的波特率分频系数CAN数据位时间的波特率分配系数= DBAUDPSC[9:0] + 1。</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>DSJW[2:0]</td><td>数据位时间的再同步补偿宽度再同步补偿占用的时间单元数量 = DSJW[2:0] + 1</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:10</td><td>DPTS[4:0]</td><td>数据位时间的传播时间段传播时间段占用的时间单元数量 = DPTS[4:0]</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:5</td><td>DPBS1[2:0]</td><td>数据位时间的相位缓冲段1相位缓冲段 1 占用的时间单元数量 = DPBS1[2:0] + 1</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DPBS2[2:0]</td><td>数据位时间的相位缓冲段 2相位缓冲段 2 占用的时间单元数量 = DPBS2[2:0] + 1</td></tr></table>

## 29.5.31. 常规帧和 FD 帧 CRC 寄存器（CAN_CRCCFD）

地址偏移：0xC08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="5">ANTM[4:0]</td><td colspan="3">保留</td><td colspan="5">CRCTCI[20:16]</td></tr><tr><td colspan="3"></td><td colspan="8">r</td><td colspan="5">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CRCTCI[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:24</td><td>ANTM[4:0]</td><td>发送 CRCTCI[20:0]值的相关联的邮箱的编号该位域包含发送常规帧或者 FD 帧时,CRC 值为 CRCTCI[20:0]的邮箱的编号。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:0</td><td>CRCTCI[20:0]</td><td>发送的常规帧 / FD帧的CRC计算值对于CRC_15,使用位0到位14,其他位为0,并且该位域值与CAN_CRCC寄存器中的CRCTC[14:0]值相同。对于CRC_17,使用位0到位16,其他位为0。对于CRC_21,使用所有的21位。</td></tr></table>
