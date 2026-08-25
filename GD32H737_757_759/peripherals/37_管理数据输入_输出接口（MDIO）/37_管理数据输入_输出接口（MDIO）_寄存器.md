# 37.5. MDIO 寄存器

MDIO 基地址：0x4000 D800

# 37.5.1. 控制寄存器（MDIO_CTL）

地址偏移：0x00

复位值：0x0000 XXXX

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>PHYB</td><td>SWRST</td></tr></table>

rw w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>PHYB</td><td>MDIO PHY 位长度0: MDIO PHY 为5位1: MDIO PHY 为3位,未使用的PHY 位被忽略。</td></tr><tr><td>0</td><td>SWRST</td><td>写1以复位MDIO模块。寄存器不会被复位。硬件自动清零该位。</td></tr></table>

# 37.5.2. 接收帧信息寄存器（MDIO_RFRM）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">RTA[1:0]</td><td colspan="5">RDEV[4:0]</td><td colspan="5">RPHY[4:0]</td><td colspan="2">ROP[1:0]</td></tr><tr><td colspan="2"></td><td colspan="2">r</td><td colspan="5">r</td><td colspan="5">r</td><td colspan="2">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>RTA[1:0]</td><td>接收到的帧 TA 位信息(只支持写数据帧或者写地址帧的 TA 位)</td></tr><tr><td>11:7</td><td>RDEV[4:0]</td><td>接收到的帧 DEVADD 位信息</td></tr></table>

6:2 RPHY[4:0] 接收到的帧 PHYADR 位信息

1:0 ROP[1:0] 接收到的帧 OP 位信息

00：写地址帧

01：写数据帧

10：读后增量地址帧

11：读数据帧

# 37.5.3. 数据接收寄存器（MDIO_RDATA）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>接收到的帧 DATA 位数据</td></tr></table>

# 37.5.4. 地址接收寄存器（MDIO_RADDR）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RADDR[15:0]</td><td>接收到的帧 ADDRESS 位数据</td></tr></table>

# 37.5.5. 数据发送寄存器（MDIO_TDATA）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TDATA[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>TDATA[15:0]</td><td>数据由后一个读数据帧或者读后增量地址帧发送。在一个读数据帧或者读后增量地址帧之前,主机发送一个写地址帧来指定要读取的数据。在这个地址帧之后,用户软件必须在读数据帧或者读后增量地址帧到来之前将要求的数据放置到 TDATA[15:0]位。最迟在读操作帧的 TA 位的前 3 个 MDIO 时钟周期之前,需完成这个动作。</td></tr></table>

# 37.5.6. 配置寄存器（MDIO_CFG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="5">EDEVADD[4:0]</td><td colspan="5">EPHYSEL[4:0]</td><td colspan="5">PHYSW[4:0]</td></tr><tr><td></td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:10</td><td>EDEVADD[4:0]</td><td>期望的 DEVADD 值。通常为 01。</td></tr><tr><td>9:5</td><td>EPHYSEL[4:0]</td><td>选择期望的 PHYADR,对于 5 位 EPHYSEL 中的每一位 x:0:设置期望的 PHYADR.x =PHYPIN[4:0].x1:设置期望的 PHYADR.x = PHYSW[4:0].x</td></tr><tr><td>4:0</td><td>PHYSW[4:0]</td><td>软件配置的 PHYADR。根据 EPHYSEL[4:0]位域值选择 PHYADR。</td></tr></table>

# 37.5.7. 状态寄存器（MDIO_STAT）

地址偏移：0x18

复位值：0x0000 1000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>RBNE</td><td>保留</td><td>OVR</td><td>UDR</td><td>TO</td><td>TANM</td><td>PHYNM</td><td>PHYM</td><td>DEVNM</td><td>DEVM</td><td>RDFRM</td><td>RDINCFRM</td><td>ADDRFRM</td><td>WRFRM</td></tr><tr><td colspan="2"></td><td>r</td><td></td><td>r</td><td>r</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td><td>rc</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>RBNE</td><td>数据接收缓冲区非空标志。已接收到数据并可以读取。读 MDIO_RDATA 寄存器清零该位。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>OVR</td><td>数据接收上溢标志。在 RBNE 位置位的情况下,如果接收移位寄存器的数据传递给 MDIO_RDATA 寄存器,将会由硬件置位。读 MDIO_RDATA 寄存器清零该位。</td></tr><tr><td>10</td><td>UDR</td><td>数据发送下溢标志。在数据发送缓冲区为空的情况下,如果在读数据帧的 TA 位的前 3 个 MDIO 时钟周期之前没有将数据写到 MDIO_TDATA 寄存器,将会由硬件置位。写 MDIO_TDATA 寄存器清零该位。</td></tr><tr><td>9</td><td>TO</td><td>超时标志。在一个完整的帧的两个位之间的时间,包括前导码到数据部分,如果已达到设置的超时时间,仍没有收到新的位或者准备的数据位未发送出去,将会由硬件置位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>8</td><td>TANM</td><td>在写地址/写数据帧的 TA 最后一位接收完时,如果接收到的 TA,与期望的‘10’不匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>7</td><td>PHYNM</td><td>在帧的 PHYADR 最后一位接收完时,如果接收到的 PHYADR 与配置的期望 PHYADR 不匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>6</td><td>PHYM</td><td>在帧的 PHYADR 最后一位接收完时,如果接收到的 PHYADR 与配置的期望 PHYADR 相匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>5</td><td>DEVNM</td><td>在帧的 DEVADD 最后一位接收完时,如果接收到的 DEVADD 与配置的期望 DEVADD 不匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>4</td><td>DEVM</td><td>在帧的 DEVADD 最后一位接收完时,如果接收到的 DEVADD 与配置的期望 DEVADD 相匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>3</td><td>RDFRM</td><td>在读数据帧的最后一位(帧 DATA 位发送完成之后)接收完时,如果接收到的 DEVADD 和 PHYADR,与配置的期望 DEVADD 和期望 PHYADR 相匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>2</td><td>RDINCFRM</td><td>在读后增量地址帧的最后一位(帧 DATA 位发送完成之后)接收完时,如果接收到的 DEVADD 和 PHYADR,与配置的期望 DEVADD 和期望 PHYADR 相匹配,则置位该位。读 MDIO_STAT 寄存器清零该位。</td></tr><tr><td>1</td><td>ADDRFRM</td><td>在地址帧的最后一位接收完时,如果接收到的 DEVADD 和 PHYADR,与配置的期</td></tr></table>

望 DEVADD 和期望 PHYADR 相匹配，则置位该位。读 MDIO_STAT 寄存器清零该位。

0 WRFRM 

在写数据帧的最后一位接收完时，如果接收到的 DEVADD 和 PHYADR，与配置的期望 DEVADD 和期望 PHYADR 相匹配，则置位该位。读 MDIO_STAT 寄存器清零该位。

# 37.5.8. 中断使能寄存器 (MDIO_INTEN)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>120</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>RBNEIE</td><td>保留</td><td>OVRIE</td><td>UDRIE</td><td>TOIE</td><td>TANMIE</td><td>PHYNMI E</td><td>PHYMIE</td><td>DEVNMI E</td><td>DEVMIE</td><td>RDFRMIE</td><td>RDINCFR MIE</td><td>ADDRFR MIE</td><td>WRFRMI E</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称



描述


<table><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>RBNEIE</td><td>若置位该位,则当 MDIO_STAT 中的 RBNE 位变为有效时产生中断请求。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>OVRIE</td><td>若置位该位,则当 MDIO_STAT 中的 OVR 位变为有效时产生中断请求。</td></tr><tr><td>10</td><td>UDRIE</td><td>若置位该位,则当 MDIO_STAT 中的 UDR 位变为有效时产生中断请求。</td></tr><tr><td>9</td><td>TOIE</td><td>若置位该位,则当 MDIO_STAT 中的 TO 位变为有效时产生中断请求。</td></tr><tr><td>8</td><td>TANMIE</td><td>若置位该位,则当 MDIO_STAT 中的 TANM 位变为有效时产生中断请求。</td></tr><tr><td>7</td><td>PHYNMIE</td><td>若置位该位,则当 MDIO_STAT 中的 PHYNM 位变为有效时产生中断请求。</td></tr><tr><td>6</td><td>PHYMIE</td><td>若置位该位,则当 MDIO_STAT 中的 PHYM 位变为有效时产生中断请求。</td></tr><tr><td>5</td><td>DEVNMIE</td><td>若置位该位,则当 MDIO_STAT 中的 DEVNM 位变为有效时产生中断请求。</td></tr><tr><td>4</td><td>DEVMIE</td><td>若置位该位,则当 MDIO_STAT 中的 DEVM 位变为有效时产生中断请求。</td></tr><tr><td>3</td><td>RDFRMIE</td><td>若置位该位,则当 MDIO_STAT 中的 RDFRM 位变为有效时产生中断请求。</td></tr><tr><td>2</td><td>RDINCFRMIE</td><td>若置位该位,则当 MDIO_STAT 中的 RDINCFRM 位变为有效时产生中断请求。</td></tr><tr><td>1</td><td>ADDRFRMIE</td><td>若置位该位,则当 MDIO_STAT 中的 ADDRFRM 位变为有效时产生中断请求。</td></tr><tr><td>0</td><td>WRFRMIE</td><td>若置位该位,则当 MDIO_STAT 中的 WRFRM 位变为有效时产生中断请求。</td></tr></table>

# 37.5.9. 引脚数值寄存器（MDIO_PIN）

地址偏移：0x20

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>120</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">PHYPIN[4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>PHYPIN[4:0]</td><td>读取的硬件引脚 MDIO_Ax(x=0...4)的数值</td></tr></table>

# 37.5.10. 超时寄存器（MDIO_TO）

地址偏移：0x24

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>120</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>TOCNT[15]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">TOCNT[14:0]</td><td>TOEN</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16:1</td><td>TOCNT[15:0]</td><td>MDIO 超时=TOCNT[15:0]*PCLK1</td></tr><tr><td>0</td><td>TOEN</td><td>使能超时0:超时失能1:超时使能</td></tr></table>
