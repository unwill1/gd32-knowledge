## 30.4. SPI 寄存器

SPI0 基地址：0x4001 3000

SPI1 基地址：0x4000 3800

SPI2 基地址：0x4000 3C00

## 30.4.1. 控制寄存器 0（SPI_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BDEN</td><td>BDOEN</td><td>CRCEN</td><td>CRCNT</td><td>CRCL</td><td>RO</td><td>SWNSS EN</td><td>SWNSS</td><td>LF</td><td>SPIEN</td><td colspan="3">PSC[2:0]</td><td>MSTMOD</td><td>CKPL</td><td>CKPH</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>BDEN</td><td>双向数据模式使能0:2线单向传输模式。1:1线双向传输模式。数据在主机的MOSI引脚和从机的MISO引脚之间传输。</td></tr><tr><td>14</td><td>BDOEN</td><td>双向传输输出使能当BDEN置位时,该位决定了数据的传输方向。0:工作在只接收模式。1:工作在只发送模式。</td></tr><tr><td>13</td><td>CRCEN</td><td>CRC计算使能0:禁能CRC计算。1:使能CRC计算。</td></tr><tr><td>12</td><td>CRCNT</td><td>下一次传输CRC0:下一次传输值为数据。1:下一次传输值为CRC值。当数据传输由DMA管理时,CRC值由硬件传输,该位应该被清零。在全双工和只发送模式下,当最后一个数据写入SPI_DATA寄存器后应将该位置1。</td></tr><tr><td>11</td><td>CRCL</td><td>CRC长度0:8位CRC数据长度1:16位CRC数据长度</td></tr><tr><td>10</td><td>RO</td><td>只接收模式当BDEN清零时,该位决定了数据的传输方向。0:全双工模式1:只接收模式</td></tr><tr><td>9</td><td>SWNSSEN</td><td>NSS软件模式使能0:NSS硬件模式,NSS电平取决于NSS引脚。1:NSS软件模式,NSS电平取决于SWNSS位。该位在SPI TI模式下没有意义。</td></tr><tr><td>8</td><td>SWNSS</td><td>NSS软件模式下NSS引脚选择0:NSS引脚拉低。1:NSS引脚拉高。只有在SWNSSEN置位时,该位有效。该位在SPI TI模式下没有意义。</td></tr><tr><td>7</td><td>LF</td><td>最低有效位先发模式0:先发送最高有效位。1:先发送最低有效位。该位在SPI TI模式下没有意义。</td></tr><tr><td>6</td><td>SPIEN</td><td>SPI使能0:禁能SP1:使能SPI</td></tr><tr><td>5:3</td><td>PSC[2:0]</td><td>主时钟预分频选择000:PCLK/2001:PCLK/4010:PCLK/8011:PCLK/16100:PCLK/32101:PCLK/64110:PCLK/128111:PCLK/256当使用SPI0时,PCLK=PCLK2。当使用SPI1或者SPI2时,PCLK=PCLK1。</td></tr><tr><td>2</td><td>MSTMOD</td><td>主从模式使能0:从机模式1:主机模式</td></tr><tr><td>1</td><td>CKPL</td><td>时钟极性选择0:SPI为空闲状态时,CLK引脚拉低。1:SPI为空闲状态时,CLK引脚拉高。</td></tr><tr><td>0</td><td>CKPH</td><td>时钟相位选择0:在第一个时钟跳变沿采集第一个数据。1:在第二个时钟跳变沿采集第一个数据。</td></tr></table>

## 30.4.2. 控制寄存器 1（SPI_CTL1）

地址偏移：0x04

复位值：0x0000 0700


该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>TXDMA_ODD</td><td>RXDMA_ODD</td><td>BYTEN</td><td colspan="4">DZ[3:0]</td><td>TBEIE</td><td>RBNEIE</td><td>ERRIE</td><td>TMOD</td><td>NSSP</td><td>NSSDRV</td><td>DMATEN</td><td>DMAREN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>TXDMA_ODD</td><td>DMA发送通道奇数字节在数据合并传输模式中,当通过DMA发送的数据总数为奇数时置位。仅在DMA功能开启且合并模式开启时(数据长度小于等于8位且对SPI_DATA写入访问是16位宽)有效。必须在SPI禁止时写入。0:通过DMA发送的数据总量为偶数个。1:通过DMA发送的数据总量为奇数个。</td></tr><tr><td>13</td><td>RXDMA_ODD</td><td>DMA接收通道奇数字节在数据合并传输模式中,当通过DMA接收的数据总数为奇数时置位。仅在DMA功能开启且合并模式开启时(数据长度小于等于8位且对SPI_DATA写入访问是16位宽)有效。必须在SPI禁止时写入。0:通过DMA接收的数据总量为偶数个。1:通过DMA接收的数据总量为奇数个。</td></tr><tr><td>12</td><td>BYTEN</td><td>字节访问使能该位用于指示对FIFO的访问宽度,并设置产生RBNE的RXFIFO的阈值。0:半字访问,且当RXLVL&gt;=2时,RBNE置位。1:字节访问,且当RXLVL&gt;=1时,RBNE置位。</td></tr><tr><td>11:8</td><td>DZ[3:0]</td><td>数据位宽这些位配置SPI传输数据的位宽:0000:强制为“0111”0001:强制为“0111”0010:强制为“0111”0011:4位0100:5位......1111:16位</td></tr><tr><td>7</td><td>TBEIE</td><td>发送缓冲区空中断使能0:禁能TBE中断1:使能TBE中断。当TBE置位时,产生中断。</td></tr><tr><td>6</td><td>RBNEIE</td><td>接收缓冲区非空中断使能0:禁能RBNE中断1:使能RBNE中断。当RBNE置位时,产生中断。</td></tr><tr><td>5</td><td>ERRIE</td><td>错误中断使能0:禁能错误中断1:使能错误中断。当CRCERR位,CONFERR位,FERR位,RXORERR位或者TXURERR位置1时,产生中断。</td></tr><tr><td>4</td><td>TMOD</td><td>SPI TI模式使能0:禁能SPI TI模式1:使能SPI TI模式</td></tr><tr><td>3</td><td>NSSP</td><td>SPI NSS脉冲模式使能0:禁能SPI NSS脉冲模式1:使能SPI NSS脉冲模式</td></tr><tr><td>2</td><td>NSSDRV</td><td>NSS输出使能0:禁能主机NSS输出1:使能主机NSS输出当SPI使能时,如果NSS引脚配置为输出模式,NSS引脚在主模式时被拉低。如果NSS引脚配置为输入模式,NSS引脚在主模式时被拉高,此时该位无效。</td></tr><tr><td>1</td><td>DMATEN</td><td>发送缓冲区DMA使能0:禁能发送缓冲区DMA1:使能发送缓冲区DMA。当SPI_STAT中的TBE置位时,将会在相应的DMA通道上产生一个DMA请求。</td></tr><tr><td>0</td><td>DMAREN</td><td>接收缓冲区DMA使能0:禁能接收缓冲区DMA1:使能接收缓冲区DMA。当SPI_STAT中的RBNE置位时,将会在相应的DMA通道上产生一个DMA请求。</td></tr></table>

## 30.4.3. 状态寄存器（SPI_STAT）

地址偏移：0x08

复位值：0x0000 0002

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="2">TXLVL[1:0]</td><td colspan="2">RXLVL[1:0]</td><td>FERR</td><td>TRANS</td><td>RXORERR</td><td>CONFERR</td><td>CRCERR</td><td colspan="2">保留</td><td>TBE</td><td>RBNE</td></tr><tr><td colspan="3"></td><td colspan="2">r</td><td colspan="2">r</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>rc_w0</td><td colspan="2"></td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:11</td><td>TXLVL[1:0]</td><td>发送FIFO状态00:空01:1/4满10:1/2满11:满注意:这里的FIFO状态是指FIFO当前实际的存储量。在这里,当FIFO存储量大于总存储量的1/2时认为FIFO已满。</td></tr><tr><td>10:98</td><td>RXLVL[1:0]FERR</td><td>接收FIFO状态00:空01:1/4满10:1/2满11:满这些位在打开了CRC计算功能时的SPI只接收模式下,不使用。注意:这里的FIFO状态是指FIFO当前实际的存储量。在这里,当FIFO存储量大于总存储量的1/2时认为FIFO已满。帧错误</td></tr><tr><td></td><td></td><td>SPI TI模式:</td></tr><tr><td></td><td></td><td>0:没有TI模式帧错误发生</td></tr><tr><td></td><td></td><td>1:TI模式帧错误发生</td></tr><tr><td></td><td></td><td>该位由硬件置位,可以通过写0清除。</td></tr><tr><td>7</td><td>TRANS</td><td>通信进行中标志</td></tr><tr><td></td><td></td><td>0:SPI空闲</td></tr><tr><td></td><td></td><td>1:SPI当前正在发送且/或接收数据。</td></tr><tr><td></td><td></td><td>该位由硬件置位和清除。</td></tr><tr><td>6</td><td>RXORERR</td><td>接收过载错误标志</td></tr><tr><td></td><td></td><td>0:没有接收过载错误发生</td></tr><tr><td></td><td></td><td>1:接收过载错误发生</td></tr><tr><td></td><td></td><td>该位由硬件置位,软件序列清零。软件序列为:先读SPI_DATA寄存器,然后读SPI_STAT寄存器。</td></tr><tr><td>5</td><td>CONFERR</td><td>SPI配置错误</td></tr><tr><td></td><td></td><td>0:无配置错误发生</td></tr><tr><td></td><td></td><td>1:配置错误发生(主机模式下,在硬件NSS模式时NSS引脚被拉低,或者软件NSS模式时SWNSS位为0,都会产生CONFERR错误。)</td></tr><tr><td></td><td></td><td>该位由硬件置位,软件序列清零。软件序列为:读或写SPI_STAT寄存器,然后写SPI_CTL0寄存器。</td></tr><tr><td></td><td></td><td>I2S模式下不使用该位。</td></tr><tr><td>4</td><td>CRCERR</td><td>SPI CRC错误标志</td></tr><tr><td></td><td></td><td>0:SPI_RCRC值等于最后接收到的CRC值。</td></tr><tr><td></td><td></td><td>1:SPI_RCRC值不等于最后接收到的CRC值该位由硬件置位,可以通过写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TBE</td><td>发送缓冲区空</td></tr><tr><td></td><td></td><td>0:发送缓冲区非空</td></tr><tr><td></td><td></td><td>1:发送缓冲区空</td></tr><tr><td>0</td><td>RBNE</td><td>接收缓冲区非空</td></tr><tr><td></td><td></td><td>0:接收缓冲区空</td></tr><tr><td></td><td></td><td>1:接收缓冲区非空</td></tr></table>

## 30.4.4. 数据寄存器（SPI_DATA）

地址偏移：0x0C

复位值：0x0000 0000

<table><tr><td colspan="15">该寄存器可以按字节(8位)或半字(16位)或字(32位)访问。</td><td></td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SPI_DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SPI_DATA[15:0]</td><td>数据传输寄存器值对于SPI,硬件有两个FIFO:TXFIFO和RXFIFO。向SPI_DATA写数据将会把数据存入发送FIFO,从SPI_DATA读数据,将从接收FIFO获得数据。注意:对于SPI,实际上硬件只根据配置好的BYTEN这一位来判断每一次访问SPI_DATA的位宽,与软件当前操作所使用的位宽无关。</td></tr></table>

## 30.4.5. CRC 多项式寄存器（SPI_CRCPOLY）

地址偏移：0x10

复位值：0x0000 0007

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CRCPOLY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CRCPOLY[15:0]</td><td>CRC多项式寄存器值该值包含了CRC多项式,用于CRC计算,默认值为0007h。</td></tr></table>

## 30.4.6. 接收 CRC 寄存器（SPI_RCRC）

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RCRC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RCRC[15:0]</td><td>接收CRC寄存器值当SPI_CTL0中的CRCEN置位时,硬件计算接收数据的CRC值,并保存到RCRC寄存器中。对于SPI,只有当数据长度为8位或16位时,CRC有效。当CRC长度设置为8位并且数据长度等于8位时,CRC计算基于CRC8标准进行,并将值保存在RCRC[7:0]中,否则CRC计算基于CRC16标准进行,并将值保存在RCRC[15:0]中。硬件在接收到每个数据位后都会计算CRC值,当TRANS置位时,读该寄存器将返回一个中间值。当SPI_CTL0寄存器中的CRCEN位或RCU复位寄存器中的SPIxRST位置位时,该寄存器复位。</td></tr></table>

## 30.4.7. 发送 CRC 寄存器（SPI_TCRC）

地址偏移：0x18

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TCRC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>TCRC[15:0]</td><td>发送CRC寄存器值当SPI_CTL0中的CRCEN置位时,硬件计算发送数据的CRC值,并保存到TCRC寄存器中。对于SPI,只有当数据长度为8位或16位时,CRC有效。当CRC长度设置为8位并且数据长度等于8位时,CRC计算基于CRC8标准进行,并将值保存在TCRC[7:0]中,否则CRC计算基于CRC16标准进行,并将值保存在TCRC[15:0]中。</td></tr></table>

硬件在发送出每个数据位后都会计算CRC值，当TRANS置位时，读该寄存器将返回一个中间值。不同的数据帧格式（SPI_CTL0中的LF位决定）将会得到不同的CRC值。当SPI_CTL0寄存器中的CRCEN位或RCU复位寄存器中的SPIxRST位置位时，该寄存器复位。

## 30.4.8. SPI0 四线 SPI 控制寄存器（SPI_QCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器可以按字节（8位）或半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>QRD</td><td>QMOD</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>QRD</td><td>四线SPI模式读选择0: SPI四线模式写操作1: SPI四线模式读操作该位仅能在SPI未通信时配置(TRANS位清零)。该位仅适用于SPI0。</td></tr><tr><td>0</td><td>QMOD</td><td>四线SPI模式使能0: SPI工作在单路模式1: SPI工作在四线模式该位仅能在SPI未通信时配置(TRANS位清零)。该位仅适用于SPI0。</td></tr></table>
