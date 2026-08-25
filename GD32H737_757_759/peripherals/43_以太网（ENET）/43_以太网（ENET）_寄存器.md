# 43.4. ENET 寄存器

ENET0基地址：0x4002 8000

ENET1基地址：0x4002 A000

# 43.4.1. MAC 配置寄存器（ENET_MAC_CFG）

地址偏移：0x0000

复位值：0x0000 8000

MAC配置寄存器是MAC的工作模式寄存器。它定义了接收和发送的工作模式。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>TFCD</td><td>保留</td><td>WDD</td><td>JBD</td><td colspan="2">保留</td><td colspan="3">IGBS[2:0]</td><td>CSD</td></tr><tr><td colspan="6"></td><td>rw</td><td></td><td>rw</td><td>rw</td><td colspan="2"></td><td></td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SPD</td><td>ROD</td><td>LBM</td><td>DPM</td><td>IPFCO</td><td>RTD</td><td>保留</td><td>APCD</td><td colspan="2">BOL[1:0]</td><td>DFC</td><td>TEN</td><td>REN</td><td colspan="2">保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>TFCD</td><td>类型帧CRC剥离位0:帧的帧校验序列(最后4字节)在转发之前不会被剥离1:帧的帧校验序列(最后4字节)在转发之前会被剥离注意:该位仅在帧的LT域大于0x0600时有效。</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>WDD</td><td>关闭看门狗该位表示已接收到了最大字节数的数据,超过的部分将被切断。0:MAC允许接收小于或等于2048字节的帧1:MAC关闭接收看门狗定时器,此时最多可接收16384字节的帧。</td></tr><tr><td>22</td><td>JBD</td><td>不检测Jabber该位表示发送帧最大允许的发送字节数,超过的部分将被截断。0:MAC允许的最大发送字节数为2048字节1:MAC关闭发送Jabber定时器,此时最多可发送16384字节的帧。</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:17</td><td>IGBS[2:0]</td><td>帧间间隙选择位这些位用于选择2个相邻发送帧之间的最短发送间隙。0x0:96位时间0x1:88位时间0x2:80位时间0x3:72位时间0x4:64位时间0x5:56位时间(半双工模式下不可用)0x6:48位时间(半双工模式下不可用)0x7:40位时间(半双工模式下不可用)</td></tr><tr><td>16</td><td>CSD</td><td>关闭载波侦听功能0: MAC载波信号错误时会报错,并终止发送。1: 在半双工模式下,MAC在发送帧过程中忽略MII的CRS信号,发送过程中载波丢失或者没有载波都不会报错。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SPD</td><td>快速以太网速度该位表示快速以太网模式下的速度:0: 10 Mbit/s1: 100 Mbit/s</td></tr><tr><td>13</td><td>ROD</td><td>关闭自接收功能该位在全双工模式下可忽略0: MAC在发送时接收所有来自PHY的数据包1: MAC在半双工模式下不接受帧</td></tr><tr><td>12</td><td>LBM</td><td>回环模式0: MAC在普通模式下工作1: MAC在MII的回环模式下工作</td></tr><tr><td>11</td><td>DPM</td><td>双工模式0: 半双工模式使能1: 全双工模式使能</td></tr><tr><td>10</td><td>IPFCO</td><td>IP帧数据校验和0: 禁止接收端TCP/UDP/ICMP报头的校验和检验功能1: 使能接收端的帧数据校验和检测功能</td></tr><tr><td>9</td><td>RTD</td><td>不尝试重试全双工模式下该位可被忽略0: MAC会在发生冲突后按照BOL位的设定重发高达16次1: 帧仅发送一次</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>APCD</td><td>自动填充/CRC剥离该位仅在非标签帧,且其长度域值小于等于1536时有效。0: MAC会转发所有接收到的帧,而不改变帧的内容。1: MAC会去除帧的填充字节和CRC域</td></tr><tr><td>6:5</td><td>BOL[1:0]</td><td>退后限制在全双工模式下这些位可被忽略在发生冲突后,MAC在重发当前帧之前需要延迟一段时间。这个延迟时间(dt)的时基单元称为时间间隙,一个时间间隙为512位时间。这个延迟时间(dt)是由下式计算得的随机整数值:<eq>0 \leq dt &lt; 2^{k}</eq>。0x0: k = min (n, 10)0x1: k = min (n, 8)0x2: k = min (n, 4)0x3: k = min (n, 1)其中n=重发次数。</td></tr><tr><td rowspan="4">4</td><td rowspan="4">DFC</td><td>顺延检验</td></tr><tr><td>在全双工模式下这些位可被忽略</td></tr><tr><td>0:禁止MAC顺延检验功能。MAC会延迟发送直到CRS信号失效。</td></tr><tr><td>1:MAC顺延检验功能使能。如果延迟超过24288位时间,则会发生过度顺延错误,并且MAC将中止发送。但如果在顺延时间内检测到有效的CRS(载波侦听)信号,则会将顺延计数器重置为0,重新启动顺延计时。</td></tr><tr><td rowspan="3">3</td><td rowspan="3">TEN</td><td>使能发送器</td></tr><tr><td>0:MAC关闭发送状态机,若当前帧正在发送则在完成发送后关闭。</td></tr><tr><td>1:MAC使能发送状态机</td></tr><tr><td rowspan="3">2</td><td rowspan="3">REN</td><td>使能接收器</td></tr><tr><td>0:MAC关闭接收状态机,若当前帧正在接收则在接收完成后关闭。</td></tr><tr><td>1:MAC使能接收状态机</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 43.4.2. MAC 帧过滤器寄存器（ENET_MAC_FRMF）

地址偏移：0x0004

复位值：0x0000 0000

MAC帧过滤器寄存器包含了接收帧的过滤模式位。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FAR</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>HPFLT</td><td>SAFLT</td><td>SAIFLT</td><td colspan="2">PCFRM[1:0]</td><td>BFRMD</td><td>MFD</td><td>DAIFLT</td><td>HMF</td><td>HUF</td><td>PM</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FAR</td><td>接收所有帧该位控制帧过滤器功能。0:只有通过了地址过滤器的接收帧才会被转发给应用程序1:所有接收到的帧都会被转发给应用程序,但过滤的结果会反映在更新接收描述符状态信息的相应标志位。</td></tr><tr><td>30:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>HPFLT</td><td>HASH或者完美过滤0:如果HMF位或者HUF位置'1',符合HASH过滤器的帧才能通过接收地址过滤。1:如果HMF位或者HUF位置'1',接收帧通过HASH过滤器或者完美过滤器中任一种,就认为通过接收地址过滤。</td></tr><tr><td>9</td><td>SAFLT</td><td>源地址过滤器除了目标地址过滤之外,使能源地址过滤器。过滤器将接收帧的源地址域值与使能的源地址寄存器中配置的值进行比较。如果源地址值相匹配,则接收描述符中的源地址匹配状态位将置位。0:源地址过滤器关闭1:源地址过滤器使能</td></tr><tr><td>8</td><td>SAIFLT</td><td>源地址过滤结果逆转该位将源地址比较结果逆转。0:仅在源地址过滤器结果逆转1:使能源地址过滤器结果逆转,所有源地址符合源地址寄存器的帧会被标记为未通过源地址过滤。</td></tr><tr><td>7:6</td><td>PCFRM[1:0]</td><td>控制帧转发位这些位用于设置所有控制帧的转发条件(包括单播和多播暂停帧)。对于是否处理暂停控制帧,只取决于RFCEN位(ENET_MAC_FCTL[2])的值。0x0:MAC不转发任何控制帧给应用程序0x1:MAC转发除了暂停帧以外的其他控制帧给应用程序0x2:MAC转发所有的控制帧给应用程序,即使是没通过地址过滤器的控制帧。0x3:MAC转发通过地址过滤器的控制帧给应用程序</td></tr><tr><td>5</td><td>BFRMD</td><td>不接收广播帧0:过滤器接收所有广播帧1:过滤器不接收所有广播帧</td></tr><tr><td>4</td><td>MFD</td><td>关闭多播过滤器0:是否对多播帧进行过滤,取决于HMF位的取值。1:所有的带多播目标地址的帧(帧的目标地址域中第一位为'1',但不是所有位都为'1')都能通过过滤器。</td></tr><tr><td>3</td><td>DAIFLT</td><td>目标地址过滤结果逆转该位将目标地址过滤结果逆转。0:禁用目标地址过滤结果逆转1:使能目标地址过滤结果逆转</td></tr><tr><td>2</td><td>HMF</td><td>多播HASH过滤器0:MAC会将接收到的多播帧的目标地址域和目标地址寄存器的设定值比较1:MAC根据HASH列表对接收到的多播帧进行目标地址过滤</td></tr><tr><td>1</td><td>HUF</td><td>单播HASH过滤器0:MAC会将接收到的单播帧目标地址域和目标地址寄存器的设定值比较1:MAC根据HASH列表对接收到的单播帧进行目标地址过滤</td></tr><tr><td>0</td><td>PM</td><td>混杂模式该位使地址过滤器无效,这意味着所有帧均可通过过滤器,同时接收描述符中状态信息的目标地址/源地址错误位总是为'0'。0:禁用混杂模式1:使能混杂模式</td></tr></table>

# 43.4.3. MAC hash 列表高寄存器（ENET_MAC_HLH）

地址偏移：0x0008

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">HLH[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">HLH[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>HLH[31:0]</td><td>HASH列表高位这些位是HASH列表的高32位。</td></tr></table>

# 43.4.4. MAC hash 列表低寄存器（ENET_MAC_HLL）

地址偏移：0x000C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">HLL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">HLL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>HLL[31:0]</td><td>HASH列表低位这些位是HASH列表的低32位。</td></tr></table>

# 43.4.5. MAC PHY 控制寄存器（ENET_MAC_PHY_CTL）

地址偏移：0x0010

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">PA[4:0]</td><td colspan="5">PR[4:0]</td><td>保留</td><td colspan="3">CLR[2:0]</td><td>PW</td><td>PB</td></tr><tr><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="3">rw</td><td>rw</td><td colspan="2">rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:11</td><td>PA[4:0]</td><td>PHY地址这些位选择想要访问的PHY地址。</td></tr><tr><td>10:6</td><td>PR[4:0]</td><td>PHY寄存器这些位选择想要访问的PHY寄存器。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:2</td><td>CLR[2:0]</td><td>时钟范围根据HCLK的频率来决定MDC的时钟分频系数。0x0:HCLK/42(HCLK范围:60-100 MHz)0x1:HCLK/62(HCLK范围:100-150 MHz)0x2:HCLK/16(HCLK范围:20-35 MHz)0x3:HCLK/26(HCLK范围:35-60 MHz)0x4:HCLK/102(HCLK范围:150-250 MHz)0x5:HCLK/124(HCLK范围:250-300 MHz)0x6:HCLK/142(HCLK范围:300-350 MHz)其他:保留</td></tr><tr><td>1</td><td>PW</td><td>PHY写该位指示了PHY的操作模式。0:对PHY进行读操作1:对PHY进行写操作</td></tr><tr><td>0</td><td>PB</td><td>PHY忙该位指示了对PHY操作的状态。由应用程序置&#x27;1&#x27;后开始对PHY的进行读或者写操作,并需等到该位在操作完成后由硬件清&#x27;0&#x27;。在写ENET_MAC_PHY_CTL寄存器和读ENET_MAC_PHY_DATA寄存器之前,该位应当为&#x27;0&#x27;。</td></tr></table>

# 43.4.6. MAC PHY 数据寄存器（ENET_MAC_PHY_DATA）

地址偏移：0x0014

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PD[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>PD[15:0]</td><td>PHY数据位对于读操作,这些位为从PHY中读取的数据。对于写操作,这些位为将要写到PHY中</td></tr></table>

的数据。

# 43.4.7. MAC 流控寄存器（ENET_MAC_FCTL）

地址偏移：0x0018

复位值：0x0000 0000

该寄存器用于配置控制帧的生成和接收。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td colspan="15">PTM[15:0]</td><td></td></tr><tr><td colspan="15">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>DZQP</td><td>保留</td><td colspan="2">PLTS[1:0]</td><td>UPFDT</td><td>RFCEN</td><td>TFCEN</td><td>FLCB/BK PA</td></tr><tr><td colspan="8"></td><td>rw</td><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>PTM[15:0]</td><td>暂停时间这些位用来设置暂停控制帧时间域的值。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>DZQP</td><td>关闭零时间片暂停功能0:打开零时间片暂停控制帧自动生成功能1:关闭零时间片暂停控制帧的自动生成</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>PLTS[1:0]</td><td>暂停低阈值这些位设置了自动重发暂停帧的定时器阈值。这个阈值应当大于0,小于位[31:16]定义的暂停时间。低阈值的计算公式为PTM-PLTS。例如,PTM=0x80(128个时间间隙),PLTS=0x1(28个时间间隙),那么在第一个暂停帧发出100(128-28)个时间间隙后,将自动重发第二个暂停帧。0x0:暂停时间-4个时间间隙0x1:暂停时间-28个时间间隙0x2:暂停时间-144个时间间隙0x3:暂停时间-256个时间间隙注意:一个时间间隙是指MII接口发送512位(64字节)数据所需要的时间。</td></tr><tr><td>3</td><td>UPFDT</td><td>单播暂停帧检测0:MAC只接收符合IEEE802.3规范定义的唯一多播地址的暂停帧1:除了唯一多播地址的暂停帧,MAC同时还会使用MAC0地址(ENET_MAC_ADDR0H寄存器和ENET_MAC_ADDR0L寄存器)来检测暂停帧。</td></tr><tr><td>2</td><td>RFCEN</td><td>接收流控使能位0:MAC不解析暂停帧1:MAC解析并处理接收到的暂停帧。MAC关闭发送器一段指定的时间(接收帧中的</td></tr></table>

暂停时间域值）。
