## 25.5. SPI/I2S 寄存器

SPI0 基地址：0x4001 3000

SPI1/I2S1 基地址：0x4000 3800

SPI2/I2S2 基地址：0x4000 3C00

## 25.5.1. 控制寄存器 0 (SPI_CTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

该寄存器在 I2S 模式下没有意义。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BDEN</td><td>BDOEN</td><td>CRCEN</td><td>CRCNT</td><td>FF16</td><td>RO</td><td>SWNSS EN</td><td>SWNSS</td><td>LF</td><td>SPIEN</td><td colspan="3">PSC [2:0]</td><td>MSTMOD</td><td>CKPL</td><td>CKPH</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>BDEN</td><td>双向数据模式0:2线单向传输模式1:1线双向传输模式。数据在主机的MOSI引脚和从机的MISO引脚之间传输。</td></tr><tr><td>14</td><td>BDOEN</td><td>双向传输输出使能当BDEN置位时,该位决定了数据的传输方向。0:工作在只接收模式1:工作在只发送模式</td></tr><tr><td>13</td><td>CRCEN</td><td>CRC计算使能0:CRC计算禁止1:CRC计算使能</td></tr><tr><td>12</td><td>CRCNT</td><td>下一次传输CRC0:下一次传输值为数据1:下一次传输值为CRC值(TCR)当数据传输由DMA管理时,CRC值由硬件传输,该位应该被清零。在全双工和只发送模式下,当最后一个数据写入SPI_DATA寄存器后应将该位置1。在只接收模式下,在接收完倒数第二个数据后应将该位置1。</td></tr><tr><td>11</td><td>FF16</td><td>数据帧格式0:8位数据帧格式1:16位数据帧格式</td></tr><tr><td>10</td><td>RO</td><td>只接收模式当BDEN清零时,该位决定了数据的传输方向。0:全双工模式1:只接收模式</td></tr><tr><td>9</td><td>SWNSSEN</td><td>NSS软件模式选择0:NSS硬件模式,NSS电平取决于NSS引脚1:NSS软件模式,NSS电平取决于SWNSS位该位在SPI TI模式下没有意义。</td></tr><tr><td>8</td><td>SWNSS</td><td>NSS软件模式下NSS引脚选择0:NSS引脚拉低1:NSS引脚拉高只有在SWNSSEN置位时,该位有效。该位在SPI TI模式下没有意义。</td></tr><tr><td>7</td><td>LF</td><td>最低有效位先发模式0:先发送最高有效位1:先发送最低有效位该位在SPI TI模式下没有意义。</td></tr><tr><td>6</td><td>SPIEN</td><td>SPI使能0:SPI设备禁止1:SPI设备使能</td></tr><tr><td>5:3</td><td>PSC[2:0]</td><td>主时钟预分频选择000:PCLK/2 100:PCLK/32001:PCLK/4 101:PCLK/64010:PCLK/8 110:PCLK/128011:PCLK/16 111:PCLK/256当使用SPI0时,PCLK=PCLK2,当使用SPI1和SPI2时,PCLK=PCLK1。</td></tr><tr><td>2</td><td>MSTMOD</td><td>主从模式使能0:从机模式1:主机模式</td></tr><tr><td>1</td><td>CKPL</td><td>时钟极性选择0:SPI为空闲状态时,CLK引脚拉低</td></tr></table>

<table><tr><td>0</td><td>CKPH</td><td>时钟相位选择</td></tr><tr><td></td><td></td><td>0:在第一个时钟跳变沿采集第一个数据</td></tr><tr><td></td><td></td><td>1:在第二个时钟跳变沿时钟跳变沿采集第一个数据</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TBEIE</td><td>RBNEIE</td><td>ERRIE</td><td>TMOD</td><td>NSSP</td><td>NSSDRV</td><td>DMATEN</td><td>DMAREN</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

## 1：SPI 为空闲状态时，CLK 引脚拉高

## 25.5.2. 控制寄存器 1 (SPI_CTL1)

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TBEIE</td><td>发送缓冲区空中断使能0:TBE中断禁止1:TBE中断使能。当TBE置位时,产生中断。</td></tr><tr><td>6</td><td>RBNEIE</td><td>接收缓冲区非空中断使能0:RBNE中断禁止.1:RBNE中断使能。当RBNE置位时,产生中断。</td></tr><tr><td>5</td><td>ERRIE</td><td>错误中断使能0:错误中断禁止1:错误中断使能。当CRCERR位,CONFERR位,RXORERR位或者TXURERR位置1时,产生中断。</td></tr><tr><td>4</td><td>TMOD</td><td>SPI TI模式使能0:SPI TI模式禁止1:SPI TI模式使能</td></tr><tr><td>3</td><td>NSSP</td><td>SPINSS脉冲模式使能0:SPINSS脉冲模式禁止1:SPINSS脉冲模式使能</td></tr><tr><td>2</td><td>NSSDRV</td><td>NSS输出使能0:NSS输出禁止</td></tr></table>

1：NSS 输出使能。

<table><tr><td></td><td></td><td>1: NSS 输出使能。当 SPI 使能时,如果 NSS 引脚配置为输出模式,NSS 引脚在主模式时被拉低。如果 NSS 引脚配置为输入模式,NSS 引脚在主模式时被拉高,此时该位无效。</td></tr><tr><td>1</td><td>DMATEN</td><td>发送缓冲区 DMA 使能0: 发送缓冲区 DMA 禁止1: 发送缓冲区 DMA 使能。当 SPI_STAT 中的 TBE 置位时,将会在相应的 DMA通道上产生一个 DMA 请求。</td></tr><tr><td>0</td><td>DMAREN</td><td>接收缓冲区 DMA 使能0: 接收缓冲区 DMA 禁止1: 接收缓冲区 DMA 使能。当 SPI_STAT 中的 RBNE 置位时,将会在相应的 DMA通道上产生一个 DMA 请求。</td></tr></table>

## 25.5.3. 状态寄存器 (SPI_STAT)

地址偏移：0x08

复位值：0x0002

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>FERR</td><td>TRANS</td><td>RXORERR</td><td>CONFERR</td><td>CRCERR</td><td>TXURERR</td><td>I2SCH</td><td>TBE</td><td>RBNE</td></tr><tr><td colspan="7"></td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>FERR</td><td>帧错误SPI TI 模式:0:没有 TI 模式帧错误发生1:TI 模式帧错误发生I2S 模式:0:没有 I2S 帧错误发生1:I2S 帧错误发生该位由硬件置位,可以通过写 0 清除。</td></tr><tr><td>7</td><td>TRANS</td><td>通信进行中标志0:SPI 或 I2S 空闲1:SPI 或 I2S 当前正在发送或接收数据</td></tr><tr><td>6</td><td>RXORERR</td><td>接收过载错误标志0:没有接收过载错误发生1:接收过载错误发生该位由硬件置位,软件序列清零。软件序列为:先读SPI_DATA寄存器,然后读SPI_STAT寄存器。</td></tr><tr><td>5</td><td>CONFERR</td><td>SPI配置错误0:无配置错误发生1:配置错误发生(主机模式下,在硬件NSS模式时NSS引脚被拉低,或者软件NSS模式时SWNSS位为0,都会产生CONFERR错误)该位由硬件置位,软件序列清零。软件序列为:先读或写SPI_STAT寄存器,然后写SPI_CTL0寄存器。I2S模式下不使用该位。</td></tr><tr><td>4</td><td>CRCERR</td><td>SPI CRC错误标志0:SPI_RCRC值等于最后接收到的CRC值1:SPI_RCRC值不等于最后接收到的CRC值该位由硬件置位,可以通过写0清除。I2S模式下不使用该位。</td></tr><tr><td>3</td><td>TXURERR</td><td>发送欠载错误标志0:无发送欠载错误发生1:发送欠载错误发生该位由硬件置位,通过读SPI_STAT寄存器清除。SPI模式下不使用该位。</td></tr><tr><td>2</td><td>I2SCH</td><td>I2S通道标志0:下一个将要发送或接收的数据属于左通道1:下一个要发送或接收的数据属于右通道该位由硬件置位和清除。SPI模式下该位无用,I2S PCM模式下该位没有意义。</td></tr><tr><td>1</td><td>TBE</td><td>发送缓冲区空0:发送缓冲区非空1:发送缓冲区空</td></tr><tr><td>0</td><td>RBNE</td><td>接收缓冲区非空0:接收缓冲区空1:接收缓冲区非空</td></tr></table>

## 25.5.4. 数据寄存器 (SPI_DATA)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SPI_DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SPI_DATA[15:0]</td><td>数据传输寄存器值硬件有两个缓冲区:发送缓冲区和接收缓冲区。向 SPI_DATA 写数据将会把数据存入发送缓冲区,从 SPI_DATA 读数据,将从接收缓冲区获得数据。当数据帧格式为 8 位时,SPI_DATA[15:8]强制为 0,SPI_DATA[7:0]用来发送和接收数据,发送和接收缓冲区都是 8 位。如果数据帧格式为 16 位,SPI_DATA[15:0]用于发送和接收数据,发送和接收缓冲区也是 16 位。</td></tr></table>

## 25.5.5. CRC 多项式寄存器 (SPI_CRCPOLY)

地址偏移：0x10

复位值：0x0000 0007

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CRCPOLY [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CRCPOLY [15:0]</td><td>CRC 多项式寄存器值该值包含了 CRC 多项式,用于 CRC 计算,默认值为 0007h。</td></tr></table>

## 25.5.6. 接收 CRC 寄存器 (SPI_RCRC)

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RCRC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RCRC[15:0]</td><td>接收 CRC 寄存器值当 SPI_CTL0 中的 CRCEN 置位时,硬件计算接收数据的 CRC 值,并保存到 RCR 寄存器中。如果是 8 位数据帧格式,CRC 计算基于 CRC8 标准进行,保存数据到 RCRC [7:0]。如果是 16 位数据帧格式,CRC 计算基于 CRC16 标准进行,保存数据到 RCRC [15:0]。硬件在接收到每个数据位后都会计算 CRC 值,当 TRANS 置位时,读该寄存器将返回一个中间值。当 SPI_CTL0 寄存器中的 CRCEN 位和 SPIEN 位清零时,该寄存器复位。</td></tr></table>

## 25.5.7. 发送 CRC 寄存器 (SPI_TCRC)

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TCRC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>TCRC[15:0]</td><td>发送 CRC 寄存器值当 SPI_CTL0 中的 CRCEN 置位时,硬件计算发送数据的 CRC 值,并保存到 TCR</td></tr></table>

寄存器中。如果是 8 位数据帧格式，CRC 计算基于 CRC8 标准进行，保存数据到TCRC[7:0]。如果是 16 位数据帧格式，CRC 计算基于 CRC16 标准进行，保存数据到 TCRC[15:0]。

硬件在发送出每个数据位后都会计算 CRC 值，当 TRANS 置位时，读该寄存器将返回一个中间值。不同的数据帧格式（SPI_CTL0 中的 LF 位决定）将会得到不同的CRC 值。

当 SPI_CTL0 寄存器中的 CRCEN 位和 SPIEN 位清零时，该寄存器复位。

## 25.5.8. I2S 控制寄存器 (SPI_I2SCTL)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>I2SSEL</td><td>I2SEN</td><td colspan="2">I2SOPMOD[1:0]</td><td>PCMS MOD</td><td>保留</td><td colspan="2">I2SSTD[1:0]</td><td>CKPL</td><td colspan="2">DTLEN[1:0]</td><td>CHLEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>I2SSEL</td><td>I2S 模式选择0: SPI 模式1: I2S 模式当 SPI 模式或 I2S 模式关闭时配置该位。</td></tr><tr><td>10</td><td>I2SEN</td><td>I2S 使能0: I2S 禁止1: I2S 使能SPI 模式不使用该位。</td></tr><tr><td>9:8</td><td>I2SOPMOD[1:0]</td><td>I2S 运行模式00: 从机发送模式01: 从机接收模式10: 主机发送模式11: 主机接收模式当 I2S 模式关闭时配置该位。SPI 模式不使用该位。</td></tr><tr><td>7</td><td>PCMSMOD</td><td>PCM 帧同步模式</td></tr></table>

0：短帧同步

1：长帧同步

只有在 PCM标准下，该位才有意义。

当 I2S 模式关闭时配置该位。SPI 模式不使用该位。

6 保留 必须保持复位值。

5:4 I2SSTD[1:0] I2S 标准选择

当 I2S 模式关闭时配置该位。SPI 模式不使用该位。

3 CKPL 空闲状态时钟极性0：I2S_CK 空闲状态为低电平1：I2S_CK 空闲状态为高电平当 I2S 模式关闭时配置该位。SPI 模式不使用该位。

2:1 DTLEN[1:0] 数据长度

当 I2S 模式关闭时配置该位。SPI 模式不使用该位。

0 CHLEN 通道长度

当 I2S 模式关闭时配置该位。SPI 模式不使用该位。

## 25.5.9. I2S 时钟预分频寄存器 (SPI_I2SPSC)

地址偏移：0x20

复位值：0x0000 0002

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>MCKOEN</td><td>OF</td><td colspan="8">DIV[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>MCKOEN</td><td>I2S_MCK输出使能0:I2S_MCK输出禁止1:I2S_MCK输出使能当I2S模式关闭时配置该位。SPI模式不使用该位。</td></tr><tr><td>8</td><td>OF</td><td>预分频器的奇系数0:实际分频系数为DIV*21:实际分频系数为DIV*2+1当I2S模式关闭时配置该位。SPI模式下不使用该位。</td></tr><tr><td>7:0</td><td>DIV[7:0]</td><td>预分频器的分频系数实际分频系数是DIV*2+OF。DIV不能为0.当I2S模式关闭时配置该位。SPI模式下不使用该位。</td></tr></table>

## 25.5.10. SPI0 四路 SPI 控制寄存器 (SPI_QCTL)

地址偏移：0x80

复位值：0x0000 0000

该寄存器可以按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>QRD</td><td>QMOD</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>QRD</td><td>四路SPI模式读选择0: SPI四路模式写操作1: SPI四路模式读操作该位仅能在SPI未通信时配置(TRANS位清零)。该位仅适用于SPI0。</td></tr><tr><td>0</td><td>QMOD</td><td>四路SPI模式使能0: SPI工作在单路模式</td></tr></table>

## 1：SPI 工作在四路模式

该位仅能在 SPI 未通信时配置（TRANS 位清零）。

该位仅适用于 SPI0。

