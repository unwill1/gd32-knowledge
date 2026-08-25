## 29.7. USBFS 寄存器

USBFS 基地址：0x5000 0000

## 29.7.1. 全局控制与状态寄存器组

## 全局 AHB 控制和状态寄存器 （USBFS_GAHBCS）

地址偏移：0x0008

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>PTXFTH</td><td>TXFTH</td><td colspan="6">保留</td><td>GINTEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>PTXFTH</td><td>周期性Tx FIFO阈值0:当周期性发送FIFO半空时,将触发PTXFEIF标志位1:当周期性发送FIFO全空时,将触发PTXFEIF标志位注意:只在主机模式下访问</td></tr><tr><td>7</td><td>TXFTH</td><td>Tx FIFO 阈值设备模式:0:当IN端点发送FIFO半空时,将触发TXFEIF标志位1:当IN端点发送FIFO全空时,将触发TXFEIF标志位主机模式:0:当非周期性发送FIFO半空时,将触发NPTXFEIF标志位1:当非周期性发送FIFO全空时,将触发NPTXFEIF标志位</td></tr><tr><td>6:10</td><td>保留GINTEN</td><td>必须保持复位值。全局中断使能</td></tr><tr><td></td><td></td><td>0: 全局中断不使能</td></tr><tr><td></td><td></td><td>1: 全局中断使能</td></tr><tr><td></td><td></td><td>注意: 在主机和设备模式下,均可访问</td></tr></table>

## 全局 USB 控制和状态寄存器 （USBFS_GUSBCS）

地址偏移：0x000C

复位值：0x0000 0880

该寄存器只能按字（32 位）访问

<table><tr><td>保留</td><td>FDM</td><td>FHM</td><td colspan="2">保留</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td></tr><tr><td>保留</td><td colspan="2">UTT[3:0]</td><td colspan="2">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>FDM</td><td>强制设备模式通过置位该控制位,可强制USB内核为设备模式0:正常模式1:设备模式设置该控制位后,应用必须等待至少25ms,让变化产生作用。注意:在设备和主机模式下,均可访问。</td></tr><tr><td>29</td><td>FHM</td><td>强制主机模式通过置位该控制位,可强制USB内核为主机模式0:正常模式1:主机模式设置该控制位后,应用必须等待至少25ms,让变化产生作用。注意:在设备和主机模式下,均可访问</td></tr><tr><td>28:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>UTT[3:0]</td><td>USB运转时间以物理时钟数来设定运转时间注意:仅在设备模式下访问</td></tr><tr><td>9:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>TOC[2:0]</td><td>超时校准当等待一个包时,USBFS需要使用USB2.0协议中需要的超时数值。应用可以使用TOC[2:0]增加该数值(以PHY时钟为单位)。PHY时钟频率为48MHz。</td></tr></table>

## 全局复位控制寄存器 （USBFS_GRSTCTL）

地址偏移：0x0010

复位值：0x8000 0000

应用通过该寄存器来复位内核的不同硬件特性。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="5">TXFNUM[4,0]</td><td>TXFF</td><td>RXFF</td><td>保留</td><td>HFCRST</td><td>HCSRST</td><td>CSRST</td></tr><tr><td colspan="5"></td><td colspan="5">rw</td><td>rs</td><td>rs</td><td></td><td>rs</td><td>rs</td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:6</td><td>TXFNUM[4:0]</td><td>Tx FIFO数目当本寄存器中TXFF控制位置位时,该标志位决定那个Tx FIFO会被冲刷主机模式:00000:仅非周期性Tx FIFO被冲刷00001:仅周期性Tx FIFO被冲刷1xxxx:周期性和非周期性Tx FIFO均被冲刷其他:没有数据被冲刷设备模式:00000:仅Tx FIFO被冲刷00001:仅Tx FIFO被冲刷00011:仅TxFIFO3被冲刷1XXXX:所有的TxFIFO均被冲刷其他:没有数据被冲刷</td></tr><tr><td>5</td><td>TXFF</td><td>TxFIFO冲刷控制位应用通过置位该控制位来冲刷TxFIFO数据,并且TXFNUM[4:0]决定冲刷的FIFO数目。当冲刷完成后,硬件自动清除该控制位。置位该控制位后,应用应该等待该控制位清除,并且,在此之前USBFS不应有其他操作。注意:在设备和主机模式下,均可访问</td></tr><tr><td>4</td><td>RXFF</td><td>RxFIFO冲刷控制位应用通过置位该控制位来冲刷RxFIFO数据。当冲刷完成后,硬件自动清除该控制位。置位该控制位后,应用应该等待该控制位清除,并且,在此之前USBFS不应有其他操作。注意:在设备和主机模式下,均可访问</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>HFCRST</td><td>主机帧计数器复位应用通过置位该控制位来复位USBFS内的帧计数器。该控制位置位后,接下来SOF的帧计数器将变为0。当复位操作完成后,硬件自动清除该控制位。置位该控制位后,应用应该等待该控制位清除,并且,在此之前USBFS不应有其他操作。注意:仅在主机模式下访问</td></tr><tr><td>1</td><td>HCSRST</td><td>HCLK软件复位应用通过置位该控制位来复位ABH时钟域电路在复位操作完成后,硬件自动清除该控制位。置位该控制位后,应用应该等待该控制位清除,并且,在此之前USBFS不应有其他操作。注意:在设备和主机模式下,均可访问</td></tr><tr><td>0</td><td>CSRST</td><td>USB内核软件复位复位AHB和USB时钟域电路,以及大多数的寄存器。</td></tr></table>

## 全局中断标志寄存器 （USBFS_GINTF）

地址偏移：0x0014

复位值：0x0400 0021

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WKUPIF</td><td>保留</td><td>DISCIF</td><td colspan="2">保留</td><td>PTXFEIF</td><td>HCIF</td><td>HPIF</td><td colspan="2">保留</td><td>PXNCIF/ISOONCIF</td><td>ISOINCIF</td><td>OEPIF</td><td>IEPIF</td><td colspan="2">保留</td></tr><tr><td colspan="2">rc_w1</td><td colspan="3">rc_w1</td><td>r</td><td>r</td><td>r</td><td colspan="2"></td><td>rc_w1</td><td>rc_w1</td><td>r</td><td>r</td><td colspan="2"></td></tr><tr><td colspan="2">15</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EOPFIF</td><td>ISOOPDIF</td><td>ENUMF</td><td>RST</td><td>SP</td><td>ESP</td><td colspan="2">保留</td><td>GONAK</td><td>GNPINAK</td><td>NPTXFEIF</td><td>RXFNEIF</td><td>SOF</td><td>保留</td><td>MFIF</td><td>COPM</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>rc_w1</td><td></td><td>rc_w1</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WKUPIF</td><td>唤醒中断标志位当在USB总线上检测到一个恢复信号(在设备模式下)或者一个远程唤醒信号(在主机模式下),硬件将置位该中断标志位。注意:在设备和主机模式下,均可访问</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DISCIF</td><td>断开中断标志位当设备断开后,将触发该标志位。注意:仅在主机模式下访问</td></tr><tr><td>28:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>PTXFEIF</td><td>周期性Tx FIFO空中断标志位当周期性发送FIFO半空或全空时,将触发该标志位。空阈值由USBFS_GAHBCS寄存器中周期性Tx FIFO空等级控制位(PTXFTH)决定。注意:仅在主机模式下访问</td></tr><tr><td>25</td><td>HCIF</td><td>主机通道中断标志位当在主机模式下其中一个通道挂起一个中断时,USBFS将置位该标志位。软件应该首先读取USBFS_HACHINT寄存器以获取通道号,然后读取相应的USBFS_HCHxINTF寄存器以获取产生中断的通道标志位。当产生通道中断的独立通道标志位被清除后,该中断标志位将自动清除。注意:仅在主机模式下访问</td></tr><tr><td>24</td><td>HPIF</td><td>主机端口中断标志位当USBFS在主机模式下检测到端口状态改变时,USB内核将置位该标志位。软件应该读取USBFS_HPCS寄存器以获取该中断源。当产生端口中断的标志被清除后,该中断标志位将自动清除。注意:仅在主机模式下访问</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>PXNCIF</td><td>周期性传输未完成中断标志位在当前帧内,当帧结束时,周期性传输未完成,USBFS将置位该标志位(主机模式)。</td></tr><tr><td></td><td>ISOONCIF</td><td>同步OUT传输未完成中断标志位在周期性帧结束时(由USBFS_DCFG寄存器的EOPFT控制位定义),如果仍有同步OUT端点未完成传输,USBFS将置位该标志位(设备模式)。</td></tr><tr><td>20</td><td>ISOINCIF</td><td>同步IN传输未完成中断标志位在周期性帧结束时(由USBFS_DCFG寄存器的EOPFT控制位定义),如果仍有同步IN端点未完成传输,USBFS将置位该标志位(设备模式)。注意:仅在设备模式下访问</td></tr><tr><td>19</td><td>OEPIF</td><td>OUT端点中断标志位当在设备模式下,其中一个OUT端点挂起一个中断时,USBFS将置位该中断标志位。软件应该首先读取USBFS_DAEPINT寄存器以获取设备号,然后读取相应的USBFS_DOEPxINTF寄存器以获取产生中断的端点标志位。当产生中断的相应端点标志位被清除后,该中断标志位被自动清除。注意:仅在设备模式下访问</td></tr><tr><td>18</td><td>IEPIF</td><td>IN端点中断标志位当在设备模式下,其中一个IN端点挂起一个中断时,USBFS将置位该标志位。软件应该首先读取USBFS_DAEPINT寄存器以获取设备号,然后读取相应的USBFS_DIEPxINTF寄存器以获取产生中断的端点标志位。当相应产生中断的端点标志位被清除后,该中断标志位被自动清除。</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>EOPFIF</td><td>周期性帧结束中断标志位当一帧内USB总线时间已经达到USBFS_DCFG寄存器中EOPFT控制位所定义的数值时,USBFS将置位该中断标志位。注意:仅在设备模式下访问</td></tr><tr><td>14</td><td>ISOOPDIF</td><td>同步OUT包丢失中断标志位如果USBFS接收到一个同步OUT包,但是Rx FIFO没有足够的空间来接收该OUT包,USBFS将置位该标志位。注意:仅在设备模式下访问</td></tr><tr><td>13</td><td>ENUMF</td><td>枚举完成中断标志位在速度枚举完成后,USBFS将置位该中断标志位。软件能够读取USBFS_DSTAT寄存器以获取当前设备速度。注意:仅在设备模式下访问</td></tr><tr><td>12</td><td>RST</td><td>USB复位中断标志位当USBFS在USB总线上检测到一个USB复位信号后,USBFS将置位该中断标志位。注意:仅在设备模式下访问</td></tr><tr><td>11</td><td>SP</td><td>USB挂起中断标志位当USBFS检测到USB总线空闲3ms并且进入挂起状态,USBFS将置位该中断标志位。注意:仅在设备模式下访问</td></tr><tr><td>10</td><td>ESP</td><td>早期挂起中断标志位当USBFS检测到USB总线空闲3ms时,USBFS将置位该中断标志位。</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>GONAK</td><td>全局OUT NAK有效标志位软件能够向USBFS_DCTL寄存器的SGONAK控制位写1,并且USBFS将会在SGONAK写入有效后,置位GONAK标志位。注意:仅在设备模式下可访问</td></tr><tr><td>6</td><td>GNPINAK</td><td>全局非周期性IN NAK有效标志位软件能够向USBFS_DCTL寄存器中的SGINAK控制位写1,并且USBFS将会在SGINAK写入有效后,置位GNPINAK标志位注意:仅在设备模式下可访问</td></tr><tr><td>5</td><td>NPTXFEIF</td><td>非周期性Tx FIFO空中断标志位当非周期性Tx FIFO为半空或全空时,将置位该中断标志位。该阈值由USBFS_GAHBCS寄存器中的非周期Tx FIFO空等级控制位(TXFTH)决定。注意:仅在主机模式下访问</td></tr><tr><td>4</td><td>RXFNEIF</td><td>Rx FIFO非空中断标志位当至少有一个包或状态条目在Rx FIFO中时,USBFS将置位该标志位。注意:在主机和设备模式下,均可访问</td></tr><tr><td>3</td><td>SOF</td><td>帧起始中断标志位主机模式:当准备在USB总线上发送一个SOF或保持有效信号,USBFS将置位该中断标志位。软件可以通过写1清除该中断标志位。设备模式:当USBFS接收到一个SOF令牌包后,USBFS置位该标志位。应用可以读取设备状态寄存器以获取当前帧号。软件可以通过写1清除该中断标志位。注意:在设备和主机模式下,均可访问</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>MFIF</td><td>模式错误中断标志位如果软件在设备模式下操作仅主机可访问的寄存器或者在主机模式下操作仅设备可访问的寄存器,USBFS将置位该中断标志位。这些错误操作不会产生作用。注意:在主机和设备模式下,均可访问</td></tr><tr><td>0</td><td>COPM</td><td>当前操作模式0:设备模式1:主机模式</td></tr></table>

注意：在主机和设备模式下，均可访问

全局中断使能寄存器 （USBFS_GINTEN）

地址偏移：0x0018

复位值：0x0000 0000

这个寄存器同全局中断标志寄存器（USBFS_GINTF）一起工作来中断应用程序。当中断使能位被禁止后，相应的中断就不会产生。然而，相应的全局中断标志位依然会被置位。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WKUPIE</td><td>保留</td><td>DISCIE</td><td colspan="2">保留.</td><td>PTXFEIE</td><td>HCIE</td><td>HPIE</td><td colspan="2">保留</td><td>PXNCIE/ISOONCIE</td><td>ISOINCIE</td><td>OEPIE</td><td>IEPIE</td><td colspan="2">保留</td></tr><tr><td>rw</td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>r</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EOPFIE</td><td>ISOOPDIE</td><td>ENUMFIE</td><td>RSTIE</td><td>SPIE</td><td>ESPIE</td><td colspan="2">保留</td><td>GONAKIE</td><td>GNPINAKIE</td><td>NPTXFEIE</td><td>RXFNEIE</td><td>SOFIE</td><td>保留</td><td>MFIE</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WKUPIE</td><td>唤醒中断使能0:禁用唤醒中断1:使能唤醒中断注意:在主机和设备模式下,均可访问</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DISCIE</td><td>断开中断使能0:禁用断开中断1:使能断开中断注意:仅在设备模式下使用</td></tr><tr><td>28:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>PTXFEIE</td><td>周期性Tx FIFO空中断使能0:禁用周期性Tx FIFO空中断1:使能周期性Tx FIFO空中断注意:仅在主机模式下访问</td></tr><tr><td>25</td><td>HCIE</td><td>主机通道中断使能</td></tr></table>

<table><tr><td></td><td></td><td>0:禁用主机通道中断1:使能主机通道中断注意:仅在主机模式下访问</td></tr><tr><td>24</td><td>HPIE</td><td>主机端口中断使能0:禁止主机端口中断1:使能主机端口中断注意:仅在主机模式下访问</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>PXNCIE</td><td>周期性传输未完成中断使能0:禁止周期性未完成传输中断1:使能周期性未完成传输中断注意:仅在主机模式下访问</td></tr><tr><td></td><td>ISOONCIE</td><td>同步OUT传输未完成中断使能0:禁止同步OUT传输未完成中断1:使能同步OUT传输未完成中断注意:仅在设备模式下访问</td></tr><tr><td>20</td><td>ISOINCIE</td><td>同步IN传输未完成中断使能0:禁止同步IN传输未完成中断1:使能同步IN传输未完成中断注意:仅在设备模式下访问</td></tr><tr><td>19</td><td>OEPIE</td><td>OUT端点中断使能0:禁止OUT端点中断1:使能OUT端点中断注意:仅在设备模式下访问</td></tr><tr><td>18</td><td>IEPIE</td><td>IN端点中断使能0:禁止IN端点中断1:使能IN端点中断注意:仅在设备模式下访问</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>EOPFIE</td><td>周期性帧结束中断使能0:禁止周期性帧结束中断1:使能周期性帧结束中断注意:仅在设备模式下访问</td></tr><tr><td>14</td><td>ISOOPDIE</td><td>同步OUT包丢失中断使能0:禁止同步OUT包丢失中断1:使能同步OUT包丢失中断</td></tr></table>

<table><tr><td></td><td></td><td>注意:仅在设备模式下访问</td></tr><tr><td>13</td><td>ENUMFIE</td><td>枚举完成中断使能0:禁止枚举完成中断1:使能枚举完成中断注意:仅在设备模式下访问</td></tr><tr><td>12</td><td>RSTIE</td><td>USB复位中断使能0:禁止USB复位中断1:使能USB复位中断注意:仅在设备模式下访问</td></tr><tr><td>11</td><td>SPIE</td><td>USB挂起中断使能0:禁止USB挂起中断1:使能USB挂起中断注意:仅在设备模式下访问</td></tr><tr><td>10</td><td>ESPIE</td><td>早期挂起中断使能0:禁止早期挂起中断1:使能早期挂起中断注意:仅在设备模式下访问</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>GONAKIE</td><td>全局OUT NAK有效中断使能0:禁止全局OUT NAK有效中断1:使能全局OUT NAK有效中断注意:仅在设备模式下访问</td></tr><tr><td>6</td><td>GNPINAKIE</td><td>全局非周期性IN NAK有效中断使能0:禁止全局非周期性IN NAK有效中断1:使能全局非周期性IN NAK有效中断注意:仅在设备模式下访问</td></tr><tr><td>5</td><td>NPTXFEIE</td><td>非周期性发送FIFO空中断使能0:禁止非周期性发送FIFO空中断1:使能非周期性发送FIFO空中断注意:仅在主机模式下访问</td></tr><tr><td>4</td><td>RXFNEIE</td><td>接收FIFO非空中断使能0:禁止接收FIFO非空中断1:使能接收FIFO非空中断注意:在设备模式与主机模式下,均可访问</td></tr><tr><td>3</td><td>SOFIE</td><td>帧首中断使能0:禁止帧首中断</td></tr></table>

<table><tr><td></td><td></td><td>1:使能帧首中断注意:在设备模式下与主机模式下,均可访问</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>MFIE</td><td>模式错误中断使能0:禁止模式错误中断1:使能模式错误中断注意:在设备模式下与主机模式下,均可访问</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 全局接收状态读取/接收状态读取和弹出寄存器（USBFS_GRSTATR/USBFS_GRSTATP）

读地址偏移：0x001C

弹出地址偏移：0x0020

复位值：0x0000 0000

对接收状态读寄存器的读操作，将返回接收 FIFO 中顶部的条目。对接收状态读取和弹出寄存器的读操作，将额外的弹出 Rx FIFO 的顶部条目。

在主机模式和设备模式下，Rx FIFO 中的条目具有不同的含义。当全局中断标志寄存器（USBFS_GINTF）中的接收 FIFO 非空中断标志位（RXFNEIF）置位后，软件应该读取该寄存器。

该寄存器只能按字(32 位)访问

主机模式：

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11"></td><td colspan="4">RPOKST[3:0]</td><td>DPID</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DPID</td><td colspan="5"></td><td colspan="6">BCOUNT[10:0]</td><td colspan="4">CNUM[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:17</td><td>RPCKST[3:0]</td><td>接收包状态0010:接收到IN数据包0011: IN传输完成(如果取出,触发一个中断)</td></tr><tr><td></td><td></td><td>0101: 数据翻转错误(如果取出,触发一个中断)</td></tr><tr><td></td><td></td><td>0111: 通道中止(如果取出,触发一个中断)</td></tr><tr><td></td><td></td><td>其他: 保留</td></tr><tr><td>16:15</td><td>DPID[1:0]</td><td>数据PID</td></tr><tr><td></td><td></td><td>接收包的数据PID</td></tr><tr><td></td><td></td><td>00: DATA0</td></tr><tr><td></td><td></td><td>10: DATA1</td></tr><tr><td></td><td></td><td>其他: 保留</td></tr><tr><td>14:4</td><td>BCOUNT[10:0]</td><td>字节数</td></tr><tr><td></td><td></td><td>接收IN数据包字节数。</td></tr><tr><td>3:0</td><td>CNUM[3:0]</td><td>通道数</td></tr><tr><td></td><td></td><td>当前接收包所属通道编号。</td></tr></table>

设备模式：

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11"></td><td colspan="4">RPOKST[3:0]</td><td>DPID</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DPID</td><td colspan="12">BCOUNT[10:0]</td><td colspan="3">EPNUM[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:17</td><td>RPCKST[3:0]</td><td>接收包状态0001:全局OUT NAK(产生一个中断)0010:接收到OUT数据包0011:OUT传输完成(产生一个中断)0100:SETUP传输完成(产生一个中断)0110:接收到SETUP数据包其他:保留</td></tr><tr><td>16:15</td><td>DPID[1:0]</td><td>数据PID接收到OUT数据包的数据PID00: DATA010: DATA1其他: 保留</td></tr><tr><td>14:4</td><td>BCOUNT[10:0]</td><td>字节数接收数据包的字节数</td></tr><tr><td>3:0</td><td>EPNUM[3:0]</td><td>端点号当前接收包所属端点编号</td></tr></table>

## 全局接收 FIFO 长度寄存器 （USBFS_GRFLEN）

地址偏移：0x0024

复位值：0x0000 0200

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RXFD[15:0]</td><td>Rx FIFO 深度以32位字计数<eq>17 \leq RXFD \leq 256</eq></td></tr><tr><td></td><td colspan="2">主机非周期性发送 FIFO 长度寄存器/设备 IN 端点 0 发送 FIFO 长度寄存器(USBFS_HNPTFLEN_DIEP0TFLEN)</td></tr><tr><td></td><td colspan="2">地址偏移:0x0028复位值:0x0200 0200</td></tr><tr><td></td><td colspan="2">该寄存器只能按字(32位)访问</td></tr><tr><td>31</td><td>30IEPOTXFD[15.0]</td><td>29 28 27 26 25 24 23 22 21 20 19 18 17 16HNPTXFD/</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IEPOTXRSAR[15:0]</td><td>HNPTXRSAR/</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 主机模式下：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>HNPTXFD[15:0]</td><td>主机非周期性Tx FIFO深度以32位字计数<eq>17 \leqslant</eq>HNPTXFD<eq>\leqslant</eq><eq>256</eq></td></tr><tr><td>15:0</td><td>HNPTXRSAR[15:0]</td><td>主机非周期性Tx RAM起始地址非周期性发送FIFO RAM的起始地址</td></tr></table>

## 设备模式下：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>IEP0TXFD[15:0]</td><td>输入端点0 Tx FIFO深度以32位字计数<eq>17 \leqslant</eq>IEP0TXFD<eq>\leqslant</eq>140</td></tr><tr><td>15:0</td><td>IEP0TXRSAR[15:0]</td><td>输入端点0 TX RAM起始地址端点0发送FIFO RAM的起始地址</td></tr></table>

## 主机非周期性发送 FIFO/队列状态寄存器 （USBFS_HNPTFQSTAT）

地址偏移：0x002C

复位值：0x0008 0200

该寄存器反映了非周期性 Tx FIFO 和请求队列的当前状态。

请求队列包括在主机模式下的 IN、OUT 或其他请求条目。

注意：在设备模式下，该寄存器不可用。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="7">NPTXRQTOP[6:0]</td><td colspan="8">NPTXRQS[7:0]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">NPTXFS[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:24</td><td>NPTXRQTOP[6:0]</td><td>非周期性发送请求队列的顶部条目在非周期性传输请求队列中的条目。位30:27:通道号位26:25:-00:IN/OUT令牌-01:0长度OUT包-11:通道中止请求位24:结束标志位,表明所选通道的最后一个条目</td></tr><tr><td>23:16</td><td>NPTXRQS[7:0]</td><td>非周期性发送请求队列空间非周期性请求队列的剩余空间0:请求队列空1:1个条目2:2个条目...n:n个条目(0≤n≤8)其他:保留</td></tr><tr><td>15:0</td><td>NPTXFS[15:0]</td><td>非周期性Tx FIFO空间非周期性发送FIFO剩余空间以32位字计数0:非周期性Tx FIFO为空1:1个字2:2个字...n:n个字(0≤n≤NPTXFD)其他:保留</td></tr><tr><td></td><td colspan="2">全局内核配置寄存器 (USBFS_GCCFG)地址偏移:0x0038复位值:0x0000 0000该寄存器只能按字(32位)访问</td></tr><tr><td>31</td><td>30</td><td>29 28 27 26 25 24 23 22 21 20 19 18 17 16</td></tr></table>

<table><tr><td></td><td colspan="10">保留</td><td>SOFOEN</td><td colspan="3">保留</td><td>PWRON</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>SOFOEN</td><td>SOF输出使能0:SOF脉冲输出禁止1:SOF脉冲输出使能</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>PWRON</td><td>上电该控制位为内部嵌入式全速PHY的电源开关0:嵌入式全速PHY掉电1:嵌入式全速PHY上电</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 内核 ID 寄存器 （USBFS_CID）

地址偏移：0x003C

复位值：0x0000 1000

该寄存器包含产品 ID

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">[15:0] HPTXFD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">r/rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">[15:0] HPTXFSAR</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>CID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CID[31:0]</td><td>内核ID软件能够写入或读取该域值,并利用该域值为应用产生一个唯一ID。</td></tr></table>

## 主机周期性发送 FIFO 长度寄存器 （USBFS_HPTFLEN）

地址偏移：0x0100

复位值：0x0200 0600

该寄存器只能按字（32 位）访问

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>HPTXFD[15:0]</td><td>主机周期性Tx FIFO深度以32位字计数<eq>1 \leqslant \text{HPTXFD} \leqslant 1024</eq></td></tr><tr><td>15:0</td><td>HPTXFSAR[15:0]</td><td>主机周期性Tx RAM起始地址主机周期性发送FIFO RAM起始地址</td></tr></table>

## 设备 IN 端点发送 FIFO 长度寄存器 （USBFS_DIEPxTFLEN） （x = 1..3，其中 x 是FIFO 编号）

地址偏移：0x0104 + （FIFO 编号 – 1） × 0x04

复位值：0x0200 0400 + （FIFO 编号 – 1） × 0x200


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IEPTXFD[15.0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">IEPTXRSAR</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>IEPTXFD[15:0]</td><td>IN端点Tx FIFO深度以32位字计数<eq>1 \leqslant \text{HPTXFD} \leqslant 1024</eq></td></tr><tr><td>15:0</td><td>IEPTXRSAR[15:0]</td><td>IN端点FIFOx Tx RAM起始地址以32位字为单位的IN端点发送FIFOx起始地址</td></tr></table>

## 29.7.2. 主机控制和状态寄存器组

主机帧间隔寄存器 （USBFS_HFT）

地址偏移：0x0404

复位值：0x0000 BB80

当 USBFS 控制器正在枚举中时，该寄存器为当前枚举速度设置帧间隔。帧间隔的修改将在下一帧生效。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>FRI[17:5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>FRI[15:0]</td><td>帧间隔该值描述了以PHY时钟为单位的帧周期。每次端口复位操作后,端口被使能,USBFS根据当前速度,采用一个固有值,并且软件可以向该位域写值以改变该固有值。该值需要采用以下描述的频率来进行计算:全速:48MHz低速:6MHz</td></tr></table>

## 主机帧信息保持寄存器 （USBFS_HFINFR）

地址偏移：0x0408

复位值：0xBB80 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>FRNUM[15:0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>FRT[15:0]</td><td>帧剩余时间该位域以PHY时钟为单位反映了当前帧剩余时间。</td></tr><tr><td>15:0</td><td>FRNUM[15:0]</td><td>帧号该位域反映了当前帧的帧号,当其增加到0x3FFF后,其值变为0。</td></tr></table>

## 主机周期性发送 FIFO/队列状态寄存器 （USBFS_HPTFQSTAT）

地址偏移：0x0410

复位值：0x0008 0200

该寄存器反映了主机周期性 Tx FIFO 和请求队列的当前状态。请求队列包括在主机模式下的 IN、OUT 或其他请求条目。


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td>PTXREQ[7:0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>PTXREQS[7:0]</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>PTXFS[15:0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>PTXREQT[7:0]</td><td>周期性Tx 请求队列的顶部条目在周期性发送请求队列中的条目位30:27:通道号位26:25:-00:IN/OUT 令牌-01:0长度OUT包-11:通道中止请求位24:中止标志,指示所选通道的最后一个条目</td></tr><tr><td>23:16</td><td>PTXREQS[7:0]</td><td>周期性发送请求队列空间周期性发送请求队列剩余空间0:请求队列为空1:1个条目2:2个条目...n:n个条目(0≤n≤8)其他:保留</td></tr><tr><td>15:0</td><td>PTXFS[15:0]</td><td>周期性发送FIFO空间周期性发送FIFO剩余空间以32位字计数</td></tr></table>

0：周期性发送FIFO为空

1：1个字

2：2个字

n：n个字（0≤n≤PTXFD)）

其他：保留

## 主机所有通道中断寄存器 （USBFS_HACHINT）

地址偏移：0x0414

复位值：0x0000 0000

当触发一个通道中断时，USBFS在该寄存器中置位相应的位，并且软件可以读取该寄存器以获取产生中断的通道。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">HACHINT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>HACHINT[7:0]</td><td>主机所有通道中断每一位表示一个通道:位0代表通道0,位7表示通道7</td></tr></table>

主机所有通道中断使能寄存器 （USBFS_HACHINTEN）

地址偏移：0x0418

复位值：0x0000 0000

软件可以使用该寄存器使能或禁用一个通道的中断。只有该寄存器中相应通道的中断使能控制位被置位，USBFS_GINTF 寄存器中的通道中断标志位 HCIF 标志位才可产生。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CINTEN[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>CINTEN</td><td>通道中断使能0:禁用通道n中断1:使能通道n中断每一位表示一个通道:位0代表通道0,位7代表通道7</td></tr></table>

地址偏移：0x0440

复位值：0x0000 0000

该寄存器控制端口行为，并且也包含一些反映端口状态的标志位。如果本寄存器中的 PRST、PEDC和 PCD 标志位被 USBFS 置位的话，USBFS_GINTF 寄存器中的 HPIF 标志位会被置位。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>PS[1:0]</td><td></td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>PP</td><td colspan="2">PLST[1:0]</td><td>保留</td><td>PRST</td><td>PSP</td><td>PREM</td><td colspan="2">保留</td><td>PEDC</td><td>PE</td><td>PCD</td><td>PCST</td></tr><tr><td></td><td></td><td></td><td>rw</td><td colspan="2">r</td><td></td><td>rw</td><td>rs</td><td>rw</td><td></td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>r</td></tr><tr><td>位/位域</td><td colspan="2">名称</td><td colspan="13">描述</td></tr><tr><td>31:19</td><td colspan="2">保留</td><td colspan="13">必须保持复位值。</td></tr><tr><td>18:17</td><td colspan="2">PS[1:0]</td><td colspan="13">端口速度反映连接到该端口的设备的枚举速度。01:全速10:低速其他:保留</td></tr><tr><td>16:13</td><td colspan="2">保留</td><td colspan="13">必须保持复位值。</td></tr><tr><td>12</td><td colspan="2">PP</td><td colspan="13">端口供电在端口被使用后,该控制位应该被置位。由于USBFS不具有电源供应能力,它只能使用该控制位以获取该端口是否在供电状态。软件应该在设置该控制位之前,保证在VBUS引脚上具有电源供应。0:端口掉电1:端口供电</td></tr><tr><td>11:10</td><td colspan="2">PLST[1:0]</td><td colspan="13">端口线状态反映USB数据线当前状态位10:DP线状态位11:DM线状态</td></tr><tr><td>9</td><td colspan="2">保留</td><td colspan="13">必须保持复位值。</td></tr><tr><td>8</td><td colspan="2">PRST</td><td colspan="13">端口复位应用通过设置该控制位以在USB端口上启动一个复位信号。当应用希望停止复位信号时,应用应该清除该控制位。0:端口不在复位状态1:端口处于复位状态</td></tr><tr><td>7</td><td colspan="2">PSP</td><td colspan="13">端口挂起应用设置该控制位来将端口进入挂起状态。当该控制位被置位后,端口停止发送SOF令牌包。该控制位只能够通过以下操作清除。- 应用置位该寄存器中的PRST控制位- 置位该寄存器中的PREM控制位- 检测到一个远程唤醒信号- 检测到一个设备断开0:端口不在挂起状态1:端口处于挂起状态</td></tr><tr><td>6</td><td colspan="2">PREM</td><td colspan="13">端口恢复应用通过置位该控制位以在USB端口上启动一个恢复信号。当应用希望停止恢复信号时,应用可以清除该控制位。0:无恢复驱动1: 恢复驱动</td></tr><tr><td>5:4</td><td colspan="2">保留</td><td colspan="13">必须保持复位值。</td></tr><tr><td>3</td><td colspan="2">PEDC</td><td colspan="13">端口使能/禁止更改当该寄存器中的位2端口使能控制位更改时,USB内核置位该标志位。</td></tr><tr><td>2</td><td colspan="2">PE</td><td colspan="13">端口使能当USB复位信号完成后,USBFS自动置位该位,并且该位不可由软件置位。该位可通过以下事件清除:- 一个断开状态- 软件清除该位0: 端口禁止1: 端口使能</td></tr><tr><td>1</td><td colspan="2">PCD</td><td colspan="13">端口连接检测当检测到设备连接时,USBFS置位该标志位。可通过向该位写1清除该标志位。</td></tr><tr><td>0</td><td colspan="2">PCST</td><td colspan="13">端口连接状态0: 设备没有连接到该端口1: 设备连接到该端口</td></tr></table>

## 主机通道 x 控制寄存器 （USBFS_HCHxCTL） （x = 0…7，其中 x 是通道编号）

地址偏移：0x0500 +（通道编号 × 0x20）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CEN</td><td>CDIS</td><td>ODDFRM</td><td></td><td></td><td colspan="5">DAR[6:0]</td><td colspan="2">保留</td><td colspan="2">EPTYPE[1:0]</td><td>LSD</td><td>保留</td></tr><tr><td>rs</td><td>rs</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EPDIR</td><td></td><td colspan="3">EPNUM[3:0]</td><td colspan="11">MPL[10:0]</td></tr><tr><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CEN</td><td>通道使能由应用设置,并且由USBFS清除0:通道禁止1:通道使能软件应该遵循操作指南来禁用或者使能一个通道</td></tr><tr><td>30</td><td>CDIS</td><td>通道禁止软件可以置位该控制位,来从处理事务中禁用该通道。软件应该遵循操作指南来禁用或者使能一个通道。</td></tr><tr><td>29</td><td>ODDFRM</td><td>奇偶帧控制对于周期性传输(中断或同步传输),该位控制将要处理的通道事务为奇数帧还是偶数帧。</td></tr><tr><td>28:22</td><td>DAR[1:0]</td><td>设备地址与该通道通信的USB设备地址。</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>EPTYPE</td><td>端点类型与该通道通信的端点的传输类型00:控制01:同步10:批量11:中断</td></tr><tr><td>17</td><td>LSD</td><td>低速设备与该通道通信的设备是一个低速设备。</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>EPDIR</td><td>端点方向与该通道通信的端点的传输方向0:OUT1:IN</td></tr><tr><td>14:11</td><td>EPNUM[3:0]</td><td>端点号与该通道通信的端点号</td></tr><tr><td>10:0</td><td>MPL[10:0]</td><td>最大包长目标端点的最大包长</td></tr></table>

主机通道 x 中断标志寄存器 （USBFS_HCHxINTF） （x = 0…7，其中 x 是通道编号）

地址偏移：0x0508 +（通道编号 × 0x20）

复位值：0x0000 0000

该寄存器包含一个通道的状态和事件，当软件获取一个通道中断时，软件需要为相应通道读取该寄存器以获取产生中断的中断源。该寄存器中的标志位均由硬件置位，并且写 1 清除。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>DTER</td><td>REQOVR</td><td>BBER</td><td>USBER</td><td>保留</td><td>ACK</td><td>NAK</td><td>STALL</td><td>保留</td><td>CH</td><td>TF</td></tr><tr><td colspan="5"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>DTER</td><td>数据切换错误IN事务获取一个数据包,但是该包的PID和USBFS_HCHxLEN寄存器中的DPID[1:0]控制位不匹配。</td></tr><tr><td>9</td><td>REQOVR</td><td>请求队列上溢当软件启动新的传输时,请求队列上溢。</td></tr><tr><td>8</td><td>BBER</td><td>串扰错误USB总线上发生一个串扰事件。产生串扰事件的典型原因是端点发送了一个数据包,但是数据包长度超过了端点的最大包长。</td></tr><tr><td>7</td><td>USBER</td><td>USB总线错误当在接收一个数据包的过程中,发生以下事件时,将置位USB总线错误标志位:接收包有一个错误的CRC域在USB总线上检测到填充错误当等待一个响应包时,超时</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ACK</td><td>ACK接收或者发送一个ACK响应包</td></tr><tr><td>4</td><td>NAK</td><td>NAK接收到一个NAK响应包</td></tr><tr><td>3</td><td>STALL</td><td>STALL接收到一个STALL响应包</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH</td><td>通道中止</td></tr><tr><td></td><td></td><td>通道被当前请求所禁用,在当前请求处理的过程中,并不响应其他请求处理。</td></tr><tr><td>0</td><td>TF</td><td>发送完成</td></tr><tr><td></td><td></td><td>该通道所有的事务成功完成并且无错误发生。</td></tr><tr><td></td><td></td><td>对于IN通道,在USBFS_HCHxLEN寄存器的PCNT位减到0后,该标志位被置位。</td></tr><tr><td></td><td></td><td>对于OUT通道,当软件从RxFIFO中读取和取出一个TF状态条目时,该标志位被置位。</td></tr></table>

## 主机通道 x 中断使能寄存器 （USBFS_HCHxINTEN）（x = 0…7，其中 x 是通道编号）

地址偏移：0x050C +（通道编号 × 0x20）

复位值：0x0000 0000

该寄存器包含 USBFS_HCHxINTF 寄存器内中断标志位的中断使能位。如果该寄存器的某位被软件置位，USBFS_HCHxINTF 寄存器内的相应位能够触发一个通道中断。该寄存器内的位可由软件置位和清除。

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>DTERIE</td><td>REQOVRIE</td><td>BBERIE</td><td>USBERIE</td><td>保留</td><td>ACKIE</td><td>NAKIE</td><td>STALLIE</td><td>保留</td><td>CHIE</td><td>TFIE</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>DTERIE</td><td>数据切换错误中断使能0:禁用数据切换错误中断1:使能数据切换错误中断</td></tr><tr><td>9</td><td>REQOVRIE</td><td>请求队列上溢中断使能0:禁用请求队列上溢中断1:使能请求队列上溢中断</td></tr><tr><td>8</td><td>BBERIE</td><td>串扰错误中断使能0:禁用串扰错误中断1:使能串扰错误中断</td></tr><tr><td>7</td><td>USBERIE</td><td>USB总线错误中断使能0:禁用USB总线错误中断1:使能USB总线错误中断</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ACKIE</td><td>ACK中断使能0:禁用ACK中断1:使能ACK中断</td></tr><tr><td>4</td><td>NAKIE</td><td>NAK中断使能0:禁用NAK中断1:使能NAK中断</td></tr><tr><td>3</td><td>STALLIE</td><td>STALL中断使能0:禁用STALL中断1:使能STALL中断</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHIE</td><td>通道中止中断使能0:禁用通道中止中断1:使能通道中止中断</td></tr><tr><td>0</td><td>TFIE</td><td>传输完成中断使能0:禁用传输完成中断1:使能传输完成中断</td></tr></table>

## 主机通道 x 长度寄存器 （USBFS_HCHxLEN） （x = 0…7，其中 x 是通道编号）

地址偏移：0x0510 +（通道编号 × 0x20）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="2">DPID[1:0]</td><td colspan="3"></td><td colspan="7">PCNT[9:0]</td><td colspan="3">TLEN[18:16]</td></tr><tr><td></td><td colspan="2">rw</td><td colspan="3"></td><td colspan="7">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>TLEN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:29</td><td>DPID[1:0]</td><td>数据PID软件应该在传输起始之前写该段位域。对于OUT传输,该位域包含第一个传输包的数据PID。对于IN传输,该位域包含第一个接收包的数据PID,并且如果数据PID不匹配的话,将会触发DTER标志位。在传输开始之后,USBFS遵循USB协议自动改变和切换该位域。00:DATA010:DATA11:SETUP(仅对于控制传输)01:保留</td></tr><tr><td>28:19</td><td>PCNT[9:0]</td><td>包计数在一个传输中希望发送(OUT)或接收(IN)的数据包个数。软件应该在通道使能之前写该位域。在传输启动之后,该位域在USBFS正确传输每个数据包后,自动减少。</td></tr><tr><td>18:0</td><td>TLEN[18:0]</td><td>传输长度一次传输的总数据字节数。对于OUT传输,该位域为OUT传输中期望发送的所有数据包总数据字节数。软件应该在通道使能之前写该位域。当软件或DMA正确向通道的数据FIFO中写入一个包时,该位域以包中字节大小进行减少。对于IN传输,每次软件或DMA从RxFIFO中读取一个包后,该位域也以包中字节大小进行减少。</td></tr></table>

## 29.7.3. 设备控制和状态寄存器组

## 设备配置寄存器 （USBFS_DCFG）

地址偏移：0x0800

复位值：0x0000 0003

在上电、枚举或执行某些控制命令后，该寄存器配置内核为设备模式。在设备初始化后，不可以改变该寄存器值。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="2">EOPF[1:0]</td><td colspan="7">DAR[6:0]</td><td>保留</td><td>NZLSOH</td><td colspan="2">DS[1:0]</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td colspan="7">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>12:11</td><td>EOPFT[1:0]</td><td>周期性帧尾时间该域定义周期性帧时间的帧尾标志触发的时间点00:80%的帧时间01:85%的帧时间10:90%的帧时间11:95%的帧时间</td></tr><tr><td>10:4</td><td>DAR[6:0]</td><td>设备地址该位定义USB设备地址,USBFS采用该位匹配接收的设备令牌地址域,在接收到来自主机的设置地址的命令后,软件设置该域</td></tr><tr><td>3</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>2</td><td>NZLSOH</td><td>非零长度OUT状态阶段握手在控制传输的OUT状态阶段,当USB设备接收到一个非零长度数据包时,该域控制控制USBFS是接收该包,还是用STALL握手信号拒绝该包。0:把该包视为正常包,根据设备OUT端点控制寄存器的NAKS和STALL位,回复握手相应握手包1:发送STALL握手,不保存接收到的OUT数据包</td></tr><tr><td>1:0</td><td>DS[1:0]</td><td>设备速度该域控制设备连入主机后的设备速度11:全速其他:保留</td></tr></table>

## 设备控制寄存器 (USBFS_DCTL)

地址偏移：0x0804

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">保留</td><td>POIF</td><td>CGONAK</td><td>SGONAK</td><td>CGINAK</td><td>SGINAK</td><td rowspan="2">保留</td><td>GONS</td><td>GINS</td><td>SD</td><td rowspan="2">RWKUP</td><td rowspan="2">rw</td></tr><tr><td>rw</td><td>w</td><td>w</td><td>w</td><td>w</td><td>r</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>11</td><td>POIF</td><td>上电初始化完成软件通过设置该位,通知USBFS寄存器在从掉电模式下唤醒,然后完成初始化。</td></tr><tr><td>10</td><td>CGONAK</td><td>清零全局OUT NAK软件设置该位从而清零该寄存器的GONS位</td></tr><tr><td>9</td><td>SGONAK</td><td>设置全局OUT NAK软件设置该位从而实现该寄存器的位GONS置位。当GONS位为零,设置该位会引起USBFS_GINTF寄存器的GONAK标志触发,软件应该在再写该位前清除GONAK标志。</td></tr><tr><td>8</td><td>CGINAK</td><td>清零全局IN NAK软件设置该位从而清零该寄存器的GINS位</td></tr><tr><td>7</td><td>SGINAK</td><td>设置全局IN NAK软件设置该位从而实现该寄存器的位GINS置位当GINS位为零,设置该位会引起USBFS_GINTF寄存器的GINAK标志触发,软件应该在再写该位前清除GINAK标志。</td></tr><tr><td>6:4</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>3</td><td>GONS</td><td>全局OUT NAK状态0: USBFS回复OUT事务的握手信号以及是否保存OUT数据包由Rx FIFO状态、端点的NAKS、STALL位确定。1: USBFS回复OUT事务NAK握手信号,不保存接收的OUT数据包。</td></tr><tr><td>2</td><td>GINS</td><td>全局IN NAK状态0: USBFS回复IN事务的握手信号由Tx FIFO状态、端点的NAKS、STALL位确定。1: USBFS通常回复IN事务NAK握手信号</td></tr><tr><td>1</td><td>SD</td><td>软断开软件可实现USB总线上的软断开,在置1该位后,关掉DP线上的上拉电阻,从而引起主机检测设备的断开。0: 没有软断开生成1: 生成软断开</td></tr><tr><td>0</td><td>RWKUP</td><td>远程唤醒在挂起状态,软件可通过该位来生成一个远程唤醒信号来通知主机恢复USB总线0: 没有远程唤醒信号生成1: 生成远程唤醒信号</td></tr></table>

## 设备状态寄存器 （USBFS_DSTAT）

地址偏移：0x0808

复位值：0x0000 0000

该寄存器包含设备模式下的 USBFS的状态和信息。


该寄存器采用字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">FNRSOF[138]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td>FNRSOF[7:0]</td><td></td><td></td><td></td><td></td><td colspan="5">保留</td><td colspan="2">ES[1:0]</td><td>SPST</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>21:8</td><td>FNRSOF[13:0]</td><td>所接收的SOF帧编号USBFS会在接收到一个SOF令牌后更新该域。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>2:1</td><td>ES[1:0]</td><td>枚举速度该域指示所枚举的设备速度,在寄存器USBFS_GINTF的ENUMF标志触发后,软件可以读取该域。</td></tr><tr><td></td><td></td><td>01:全速</td></tr><tr><td></td><td></td><td>其他:保留</td></tr><tr><td>0</td><td>SPST</td><td>挂起状态</td></tr><tr><td></td><td></td><td>该位指示设备是否处于挂起状态。</td></tr><tr><td></td><td></td><td>0:设备不在挂起状态</td></tr><tr><td></td><td></td><td>1:设备在挂起状态</td></tr></table>

## 设备 IN 端点通用中断使能寄存器 （USBFS_DIEPINTEN）

地址偏移：0x810

复位值：0x0000 0000

该寄存器包含寄存器 USBFS_DIEPxINTF 中的标志的中断使能位，如果软件置 1 某位，其在寄存器 USBFS_DIEPxINTF 中对应的位可以触发一个寄存器 USBFS_DAEPINT 端点中断。该位可以通过软件置位和清零。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>IEPNEEN</td><td>保留</td><td>EPTXFUDEN</td><td>CITOEN</td><td>保留</td><td>EPDISEN</td><td>TFEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>6</td><td>IEPNEEN</td><td>IN端点NAK有效中断使能位0:除能中断1:使能中断</td></tr><tr><td>5</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>4</td><td>EPTXFUDEN</td><td>端点Tx FIFO下溢中断使能位0:除能中断1:使能中断</td></tr><tr><td>3</td><td>CITOEN</td><td>控制IN事务超时中断使能位0:除能中断1:使能中断</td></tr><tr><td>2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1</td><td>EPDISEN</td><td>端点除能中断使能位0:除能中断1:使能中断</td></tr><tr><td>0</td><td>TFEN</td><td>传输完成中断使能位0:除能中断1:使能中断</td></tr></table>

## 设备 OUT 端点通用中断使能寄存器 （USBFS_DOEPINTEN）

地址偏移：0x0814

复位值：0x0000 0000

该寄存器包含寄存器 USBFS_DOEPxINTF 中的标志的中断使能位，如果软件置 1 某位，其在寄存器 USBFS_DOEPxINTF 中对应的位可以触发一个寄存器 USBFS_DAEPINT 端点中断。该位可以通过软件置位和清零。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>BTBSTPEN</td><td>保留</td><td>EPRXFOVREN</td><td>STPFEN</td><td>保留</td><td>EPDISEN</td><td>TFEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>6</td><td>BTBSTPEN</td><td>连续SETUP包中断使能位(仅适用于控制OUT端点)0:除能中断1:使能中断</td></tr><tr><td>5</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>4</td><td>EPRXFOVREN</td><td>端点Rx FIFO上溢中断使能位0:除能中断1:使能中断</td></tr><tr><td>3</td><td>STPFEN</td><td>SETUP阶段完成中断使能位(仅适用于控制OUT端点)0:除能中断1:使能中断</td></tr><tr><td>2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1</td><td>EPDISEN</td><td>端点除能中断使能位0:除能中断1:使能中断</td></tr><tr><td>0</td><td>TFEN</td><td>传输完成中断使能位0:除能中断1:使能中断</td></tr></table>

## 设备端点中断寄存器 （USBFS_DAEPINT）

地址偏移：0x0818

复位值：0x0000 0000

当一个端点的中断被触发，USBFS置 1 该寄存器的相应位，软件可通过该寄存器知道在本次中断中的端点号。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12"></td><td colspan="4">OEPITB[3:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">IEPTB[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保留为复位值。</td></tr></table>

<table><tr><td>19:16</td><td>OEPITB[3:0]</td><td>设备OUT端点中断位每个位代表一个OUT端点:Bit16代表OUT端点0,Bit19代表OUT端点3</td></tr><tr><td>15:4</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>3:0</td><td>IEPITB[3:0]</td><td>设备IN端点中断位每个位代表一个IN端点:Bit0代表IN端点0,Bit3代表IN端点3</td></tr></table>

## 设备端点中断使能寄存器 （USBFS_DAEPINTEN）

地址偏移：0x081C

复位值：0x0000 0000

该寄存器可通过软件使能或除能端点的中断，只有当端点在该寄存器中相应位被置 1 才能触发寄存器 USBFS_GINTF 的端点中断标志 OEPIF 或 IEPIF。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12"></td><td colspan="4">OEPIE[3:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">IEPIE[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>19:16</td><td>OEPIE[3:0]</td><td>OUT端点中断使能位0:除能OUT端点n中断1:使能OUT端点n中断每个位代表一个OUT端点:Bit16对应OUT端点0,Bit19对应OUT端点3</td></tr><tr><td>15:4</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>3:0</td><td>IEPIE[3:0]</td><td>IN端点中断使能位0:除能IN端点n中断1:使能IN端点n中断每个位代表一个IN端点:Bit0对应IN端点0,Bit3对应IN端点3</td></tr></table>

## 设备 IN 端点 FIFO 空中断使能寄存器 （USBFS_DIEPFEINTEN）

地址偏移：0x0834

复位值：0x0000 0000

该寄存器包含 IN 端点 Tx FIFO 空中断的使能位

寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">IEPTXFEIE[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>3:0</td><td>IEPTXFEIE[3:0]</td><td>IN端点Tx FIFO空中断的使能位该域控制着USBFS_DIEPxINTF寄存器的TXFE位能否生成一个寄存器USBFS_DAEPINT的端点中断位Bit0对应IN端点0,Bit5对应IN端点50:除能FIFO空中断1:使能FIFO空中断</td></tr></table>

## 设备 IN 端点 0 控制寄存器 （USBFS_DIEP0CTL）

地址偏移：0x0900

复位值：0x0000 8000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>EPEN</td><td>EPD</td><td colspan="2">保留</td><td>SNAK</td><td>CNAK</td><td colspan="4">TXFNUM[3.0]</td><td>STALL</td><td>保留</td><td colspan="2">EPTYPE[1.0]</td><td>NAKS</td><td>保留</td></tr><tr><td>rs</td><td>rs</td><td></td><td></td><td>w</td><td>w</td><td colspan="4">rw</td><td>rs</td><td></td><td colspan="2">r</td><td>r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>EPACT</td><td>保留</td><td>MPL[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>EPEN</td><td>端点使能软件置位、USBFS清零0:端点除能1:端点使能软件应该按照操作指南使能或除能端点</td></tr><tr><td>30</td><td>EPD</td><td>端点除能软件可通过置位该位从而除能端点,软件应该按照操作指南使能或除能端点。</td></tr><tr><td>29:28</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>27</td><td>SNAK</td><td>置位NAK软件置位该位来设置该寄存器的NAKS位</td></tr><tr><td>26</td><td>CNAK</td><td>清零NAK软件置位该位来清零该寄存器的NAKS位</td></tr><tr><td>25:22</td><td>TXFNUM[3:0]</td><td>Tx FIFO编号定义IN端点0的Tx FIFO编号</td></tr><tr><td>21</td><td>STALL</td><td>STALL握手当接收IN令牌时,软件可以通过置1该位发送STALL握手包,对于相应的OUT端点0,在接收SETUP令牌后,USBFS清除此位。该位比该寄存器的NAKS位和寄存器USBFS_DCTL的GINS位优先级要高,如果STALL和NAKS位都被置位,STALL位生效。</td></tr><tr><td>20</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>19:18</td><td>EPTYPE[1:0]</td><td>端点类型该域固定为'00',控制端点。</td></tr><tr><td>17</td><td>NAKS</td><td>NAK状态当该寄存器的STALL位和寄存器USBFS_DCTL的位GINS被清零,该位控制USBFS的NAK状态。0:根据端点Tx FIFO的状态,USBFS发送数据或握手包1:USBFS总为IN令牌发送NAK握手包该位是只读位,可以通过该寄存器的位CNAK和位SNAK控制该位</td></tr><tr><td>16</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>15</td><td>EPACT</td><td>端点激活对于端点0来说,该域固定为‘1’</td></tr><tr><td>14:2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1:0</td><td>MPL[1:0]</td><td>最大包长域定义了控制数据包的最大包长,如USB 2.0协议所描述,对控制传输而言,有四种包长度:00:64字节01:32字节10:16字节11:8字节</td></tr></table>

## 设备 IN 端点 x 控制寄存器 （USBFS_DIEPxCTL） （x = 1..3，x 是端点编号）

地址偏移：0x0900 + (端点编号 × 0x20)

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>EPEN</td><td>EPD</td><td>SODFRM/SD1 PID</td><td>SDPID/SEVENFRM</td><td>SNAK</td><td>CNAK</td><td colspan="4">TXFNUM[3:0]</td><td>STALL</td><td>保留</td><td colspan="2">EPTYPE[1:0]</td><td>NAKS</td><td>EOFRMDPID</td></tr><tr><td>rs</td><td>rs</td><td>w</td><td>w</td><td>w</td><td>w</td><td colspan="4">rw</td><td colspan="2">rw/rs</td><td colspan="2">rw</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EPACT</td><td colspan="4">保留</td><td colspan="11">MPL[10:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>EPEN</td><td>端点使能软件置位,USBFS清零0:端点除能1:端点使能软件应该按照操作指南使能或除能端点</td></tr><tr><td>30</td><td>EPD</td><td>端点除能软件可通过置位该位从而除能端点,软件应该按照操作指南使能或除能端点。</td></tr><tr><td>29</td><td>SODDFRMSD1PID</td><td>设置奇数帧(适用于同步IN端点)软件通过置1该位置1该寄存器的EOFRM位设置DATA1 PID(适用于中断和大容量IN端点)软件可通过置1该位置1该寄存器的DPID位</td></tr><tr><td rowspan="2">28</td><td>SEVENFRM</td><td>设置偶数帧(适用于同步IN端点)软件通过置1该位清零该寄存器的EOFRM位</td></tr><tr><td>SD0PID</td><td>设置DATA1(适用于中断和大容量IN端点)软件可通过置1该位清零该寄存器的DPID位</td></tr><tr><td>27</td><td>SNAK</td><td>设置NAK软件置1该位置1该寄存器的NAKS位</td></tr><tr><td>26</td><td>CNAK</td><td>清零NAK软件置1该位清零该寄存器的NAKS位</td></tr><tr><td>25:22</td><td>TXFNUM[3:0]</td><td>Tx FIFO编号该位定义了IN端点的Tx FIFO编号</td></tr><tr><td>21</td><td>STALL</td><td>STALL握手当接收IN令牌时,软件可以通过置1该位发送STALL握手包。该位比该寄存器的NAKS位和寄存器USBFS_DCTL的GINS位优先级要高,如果STALL和NAKS位都被置位,STALL位生效。对于控制IN端点:当对应的OUT端点接收到SETUP令牌时,只有USBFS可以清零此位,软件不可清除此位。对于中断或大容量IN端点:只有软件可以清零此位。</td></tr><tr><td>20</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>19:18</td><td>EPTYPE[1:0]</td><td>端点类型该域定义端点的传输类型:00:控制01:同步10:大容量11:中断</td></tr><tr><td>17</td><td>NAKS</td><td>NAK状态当该寄存器的STALL位和寄存器USBFS_DCTL的位GINS被清零,该位控制USBFS的NAK状态:0:根据端点Tx FIFO的状态,USBFS发送数据或握手包1:USBFS总为IN令牌发送NAK握手包该位是只读位,可以通过该寄存器的位CNAK和位SNAK控制该位</td></tr><tr><td>16</td><td>EOFRM</td><td>奇偶帧(适用于同步IN端点)对于同步传输,软件通过使用该位控制USBFS只在奇数帧或偶数帧为IN事务发送数据包,如果当前帧号的奇偶性不匹配该位,USBFS回复一个零长度的包:0:只在偶数帧发送数据1:只在奇数帧发送数据</td></tr><tr><td></td><td>DPID</td><td>端点数据PID(适用于中断或大容量IN端点)在端点或大容量传输中,有数据PID翻转机制,在传输开始之前,软件通过设定SD0PID来设置此位,按照USB协议中描述的数据PID翻转机制,USBFS在传输过程中保持该位。0:数据包的PID是DATA01:数据包的PID是DATA1</td></tr><tr><td>15</td><td>EPACT</td><td>端点激活该位控制端点是否激活,当端点没有激活,忽略任何令牌,不做任何回复。</td></tr><tr><td>14:11</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>10:0</td><td>MPL[10:0]</td><td>该域定义最大包长</td></tr></table>

## 设备 OUT 端点 0 控制寄存器 （USBFS_DOEP0CTL）

地址偏移: 0x0B00

复位值: 0x0000 8000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>EPEN</td><td>EPD</td><td colspan="2">保留</td><td>SNAK</td><td>CNAK</td><td colspan="4">保留</td><td>STALL</td><td>SNOOP</td><td colspan="2">EPTYPE[1:0]</td><td>NAKS</td><td>保留</td></tr><tr><td>rs</td><td>r</td><td></td><td></td><td>w</td><td>w</td><td></td><td></td><td></td><td></td><td>rs</td><td>rw</td><td>r</td><td></td><td>r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EPACT</td><td colspan="13">保留</td><td colspan="2">MPL[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>EPEN</td><td>端点使能软件置位,USBFS清零0: 端点除能1: 端点使能软件应该按照操作指南使能或除能端点。</td></tr><tr><td>30</td><td>EPD</td><td>端点除能对于OUT端点0,该位固定为0</td></tr><tr><td>29:28</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>27</td><td>SNAK</td><td>设置NAK软件置1该位置1该寄存器的NAKS位</td></tr><tr><td>26</td><td>CNAK</td><td>清零NAK软件置1该位清零该寄存器的NAKS位</td></tr><tr><td>25:22</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>21</td><td>STALL</td><td>STALL握手在OUT事务中,软件可以通过置1该位发送STALL握手包,对于OUT端点0,在接收SETUP令牌后,USBFS清除此位。该位比该寄存器的NAKS位和寄存器USBFS_DCTL的GINS位优先级要高,即如果STALL和NAKS位都被置位,STALL位生效。</td></tr><tr><td>20</td><td>SNOOP</td><td>调查模式该位控制OUT端点的调查模式,在调查模式中,USBFS不再检查接收数据包的CRC值0:调查模式除能1:调查模式使能</td></tr><tr><td>19:18</td><td>EPTYPE[1:0]</td><td>端点类型对于控制端点,该位固定为"00"</td></tr><tr><td>17</td><td>NAKS</td><td>NAK状态当该寄存器的STALL位和寄存器USBFS_DCTL的位GINS被清零,该位控制USBFS的NAK状态:0:根据端点Rx FIFO的状态,USBFS发送数据或握手包1:USBFS为OUT事务发NAK握手包该位是只读位,通过该寄存器的CNAK和SNAK位控制该位</td></tr><tr><td>16</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>15</td><td>EPACT</td><td>端点激活对于端点0,该域固定为1</td></tr><tr><td>14:2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1:0</td><td>MPL[1:0]</td><td>最大包长该位是只读位,其数值来自于寄存器USBFS_DIEP0CTL的位MPL:00:64字节</td></tr></table>

01：32字节

10：16字节

11：8字节

设备 OUT 端点 x 控制寄存器 （USBFS_DOEPxCTL） （x= 1..3，x 是端点编号）

地址偏移：0x0B00 + （端点编号 × 0x20）

复位值：0x0000 0000

软件用该寄存器控制 OUT 端点 0 以外的每个逻辑 OUT 端点

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>EPEN</td><td>EPD</td><td>SODDFRM/SD1PID</td><td>SEVENFRM/SD0PID</td><td>SNAK</td><td>CNAK</td><td colspan="4">保留</td><td>STALL</td><td>SNOOP</td><td colspan="2">EPTYPE[1:0]</td><td>NAKS</td><td>EOFRM/DPID</td></tr><tr><td>rs</td><td>rs</td><td>w</td><td>w</td><td>w</td><td>w</td><td colspan="4"></td><td>rw/rs</td><td>rw</td><td colspan="2">rw</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EPACT</td><td colspan="4">保留</td><td colspan="11">MPL[10:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>EPEN</td><td>端点使能软件置位,USBFS清零0:端点除能1:端点使能软件应该按照操作指南使能或除能端点。</td></tr><tr><td>30</td><td>EPD</td><td>端点除能软件通过置1该位除能端点,软件应该按照操作指南使能或除能端点。</td></tr><tr><td rowspan="2">29</td><td>SODDFRM</td><td>设置奇数帧(适用于同步OUT端点)该位只针对同步OUT端点有效软件置1该位来置位该寄存器的EOFRM位</td></tr><tr><td>SD1PID</td><td>设置DATA1 PID(适用于中断和大容量OUT端点)软件置1该位来置位该寄存器的DPID位</td></tr><tr><td>28</td><td>SEVENFRMSD0PID</td><td>设置偶数帧(适用于同步OUT端点)软件置1该位来清零该寄存器的EOFRM位设置DATA0 PID(适用于中断和大容量OUT端点)软件置1该位来清零该寄存器的DPID位</td></tr><tr><td>27</td><td>SNAK</td><td>设置NAK软件置1该位从而置1该寄存器的NAKS位</td></tr><tr><td>26</td><td>CNAK</td><td>清零NAK软件置1该位从而清零该寄存器的NAKS位</td></tr><tr><td>25:22</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>21</td><td>STALL</td><td>STALL握手在OUT事务中,软件可以通过置1该位发送STALL握手包。该位比该寄存器的NAKS位和寄存器USBFS_DCTL的GINS位优先级要高,如果STALL和NAKS位都被置位,STALL位生效。对于控制OUT端点:当OUT端点接收SETUP令牌时,只有USBFS可以清零该位,软件不可清零此位。对于中断或大容量OUT端点只有软件可以清零该位</td></tr><tr><td>20</td><td>SNOOP</td><td>调查模式该位控制OUT端点的调查模式,在调查模式中,USBFS不再检查接收数据包的CRC值0:调查模式除能1:调查模式使能</td></tr><tr><td>19:18</td><td>EPTYPE[1:0]</td><td>端点类型该域定义端点的传输类型00:控制01:同步10:大容量11:中断</td></tr><tr><td>17</td><td>NAKS</td><td>NAK状态当该寄存器的STALL位和寄存器USBFS_DCTL的位GONS被清零,该位控制USBFS的NAK状态:0:根据端点的Rx FIFO的状态,发送握手包1:USBFS为OUT事务发送NAK握手该位是只读位,通过该寄存器的CNAK和SNAK位控制该位</td></tr><tr><td>16</td><td>EOFRMDPID</td><td>奇偶帧(适用于同步OUT端点)对于同步传输,软件通过使用该位控制USBFS只在奇数帧或偶数帧发送数据包给OUT事务,如果当前帧号的奇偶性不匹配该位,USBFS不保存数据包0:只在偶数帧发送数据1:只在奇数帧发送数据端点数据PID(适用于中断或大容量端点)在端点或大容量传输中,有数据PID翻转机制,在传输开始之前,软件通过设定SD0PID来设置此位,按照USB协议中描述的数据PID翻转机制,USBFS在传输过程中保持该位。0:数据包PID是DATA01:数据包PID是DATA1</td></tr><tr><td>15</td><td>EPACT</td><td>端点激活位控制端点是否激活,当端点没有激活,忽略任何令牌,不做任何回复</td></tr><tr><td>14:11</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>10:0</td><td>MPL[10:0]</td><td>该位定义最大包长</td></tr></table>

## 设备 IN 端点 x 中断标志寄存器 （USBFS_DIEPxINTF） （x = 0..3，x 是端点编号）

地址偏移：0x0908 + （端点编号 × 0x20）

复位值：0x0000 0080

该寄存器包含 IN 端点的状态和事件，当获得一个 IN 端点的中断时，应该读取该端点的中断标志寄存器，从而获知中断源。该寄存器的标志位通常硬件置位，除了 TXFE 位，各位写 1 清零。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>TXFE</td><td>IEPNE</td><td>保留</td><td>EPTXFUD</td><td>CITO</td><td>保留</td><td>EPDIS</td><td>TF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>7</td><td>TXFE</td><td>发送FIFO空端点的Tx FIFO达到寄存器USBFS_GAHBCS的位TXFTH定义的空阈值。</td></tr><tr><td>6</td><td>IEPNE</td><td>IN端点NAK有效寄存器USBFS_DIEPxCTL的位SNAK的设置生效,该位可以通过写1清零或设置CNAK位</td></tr><tr><td>5</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>4</td><td>EPTXFUD</td><td>端点Tx FIFO下溢如果当IN令牌被接收后,Tx FIFO没有包数据,该标志被触发。</td></tr><tr><td>3</td><td>CITO</td><td>控制IN事务超时中断在控制IN事务中,如果设备等待的握手包超时,该标志位被触发</td></tr><tr><td>2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1</td><td>EPDIS</td><td>端点除能端点除能时,该标志位被触发</td></tr><tr><td>0</td><td>TF</td><td>传输完成当该端点的所有IN事务完成,该标志位被触发。</td></tr></table>

## 设备 OUT 端点 x 中断标志寄存器 （USBFS_DOEPxINTF）（x = 0..3，x 是端点编号）

地址偏移：0x0B08 + （端点编号 × 0x20）

复位值：0x0000 0000

该寄存器包含 OUT 端点的状态和事件，当获得一个 OUT 端点的中断时，应该读取该端点的中断标志寄存器，从而获知中断源。该寄存器的标志位通常硬件置位，各位写 1 清零。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td>BTBSTP</td><td>保留</td><td>EPRXFOVR</td><td>STPF</td><td>保留</td><td>EPDIS</td><td>TF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w1/rw</td><td></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>6</td><td>BTBSTP</td><td>连续SETUP包(适用于控制OUT端点)当一个控制OUT端点接收超过连续3个SETUP包时,该标志被触发。</td></tr><tr><td>5</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>4</td><td>EPRXFOVR</td><td>端点Rx FIFO上溢当OUT令牌被接收时,如果OUT端点的Rx FIFO没有足够的空间存放数据包,该位被触发。在这种情况下,USBFS不能接收OUT数据包,发送一个NAK握手包。</td></tr><tr><td>3</td><td>STPF</td><td>SETUP阶段完成(适用于控制OUT端点)当一个SETUP阶段完成,也就是USBFS在一个setup令牌后接收了一个IN或OUT令牌,该位被置位。</td></tr><tr><td>2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1</td><td>EPDIS</td><td>端点除能端点除能时,该标志位被触发</td></tr><tr><td>0</td><td>TF</td><td>传输完成当该端点的所有OUT事务完成,该标志位被触发</td></tr></table>

## 设备 IN 端点 0 传输长度寄存器 （USBFS_DIEP0LEN）

地址偏移：0x0910

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11"></td><td colspan="2">PCNT[1:0]</td><td colspan="3">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">TLEN[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>20:19</td><td>PCNT[1:0]</td><td>包数传输中被发送的数据包数量在端点使能之前,软件设置该位,在传输开始后,该域在每次数据包成功发送后自动减少。</td></tr><tr><td>18:7</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>6:0</td><td>TLEN[6:0]</td><td>传输长度</td></tr></table>

一次传输的数据总字节数

该域是IN传输中需要发送的包数据的总字节数，在端点使能之前，软件设置该位，在软件或DMA成功地将包数据写入端点的Tx FIFO中，该域减少与包数据大小相同的数值。

## 设备 OUT 端点 0 传输长度寄存器 （USBFS_DOEP0LEN）

地址偏移：0x0B10

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="2">STPCNT[1:0]</td><td colspan="9">保留</td><td>PCNT</td><td colspan="3">保留</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">TLEN[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>30:29</td><td>STPCNT[1:0]</td><td>SETUP包计数该域定义端点可以接受的最大连续SETUP包数量在SETUP传输之前,设置该域,每当连续SETUP包接收到时,该域值减1,当该域达到0时,寄存器USBFS_DOEP0INTF的BTBSTP标志被触发。00:0个包01:1个包10:2个包11:3个包</td></tr><tr><td>28:20</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>19</td><td>PCNT</td><td>包计数一次传输中应该接收到包数量。在端点使能前,软件设置该位,在传输开始后,每当数据包接收到后,该域数值自动减少。</td></tr><tr><td>18:7</td><td>保留</td><td>必须保留为复位值。</td></tr></table>

复位值：0x0000 0000

<table><tr><td>6:0</td><td>TLEN[6:0]</td><td>传输长度传输中数据总字数。该域是OUT传输中需要接收的包数据的总字节数,在端点使能之前,软件设置该位,在软件或DMA成功地将包数据读取端点的Rx FIFO中,该域减少与包数据大小相同的数值。</td></tr></table>

设备 IN 端点 x 传输长度寄存器 （USBFS_DIEPxLEN） （x = 1..3，x 是端点编号）

地址偏移：0x910 + （端点编号 × 0x20）

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="10">PCNT[9:0]</td><td colspan="3">TLEN[18:16]</td></tr><tr><td colspan="13">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TLEN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>28:19</td><td>PCNT[9:0]</td><td>包数量传输中被发送的数据包数量在端点使能之前,软件设置该位,在传输开始后,该域在每次数据包成功发送后自动减少。</td></tr><tr><td>18:0</td><td>TLEN[18:0]</td><td>传输长度传输的数据总字节数该域是IN传输中需要发送的包数据的总字节数,在端点使能之前,软件设置该位,在软件或DMA成功地将包数据写入端点的Tx FIFO中,该域减少与包数据大小相同的数值。</td></tr></table>

设备 OUT 端点 x 传输长度寄存器 （USBFS_DOEPxLEN） （x = 1..3，x 是端点编号）

地址偏移：0x0B10 + （x × 0x20）


该寄存器采用字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>T[1:0]</td><td>RXDPID/STPCN</td><td></td><td></td><td></td><td></td><td>PCNT[9:0]</td><td></td><td></td><td></td><td></td><td></td><td>TLEN[18:16]</td><td></td><td></td></tr><tr><td colspan="7">r/rw</td><td colspan="6">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TLEN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td rowspan="2">30:29</td><td>RXDPID[1:0]</td><td>接收数据PID(适用于同步OUT端点)该域保存该端点该数据包所接受的最后一个数据包的PID00:DATA010:DATA1其他:保留SETUP包数(适用于控制OUT端点)</td></tr><tr><td>STPCNT[1:0]</td><td>该位定义该端点可以接受连续SETUP最大包数在SETUP传输之前,设置该域,每当连续SETUP包接收到时,该域值减1,当该域达到0时,寄存器USBFS_DOEP0INTF的BTBSTP标志被触发。00:0个包01:1个包10:2个包11:3个包</td></tr><tr><td>28:19</td><td>PCNT[9:0]</td><td>包数传输中应该接收到包数量在端点使能前,软件设置该位,在传输开始后,每当数据包接收到后,该域数值自动减少。</td></tr><tr><td>18:0</td><td>TLEN[18:0]</td><td>传输长度传输中数据总字数该域是IN传输中需要接收的包数据的总字节数,在端点使能之前,软件设置该位,在软件或DMA成功地将包数据读取端点的Rx FIFO中,该域减少与包数据大小相同的数值。</td></tr></table>

## 设备 IN 端点 x 发送 FIFO 状态寄存器 （USBFS_DIEPxTFSTAT） （x = 0..3，x 是端点编号）

地址偏移：0x0918 + （端点编号 × 0x20）

复位值：0x0000 0200

该寄存器包含每个端点的 Tx FIFO 的信息。

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IEPTFS[15,0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>15:0</td><td>IEPTFS[15:0]</td><td>IN端点的Tx FIFO可用空间IN端点的Tx FIFO可用空间用32位字为单位0:FIFO是满的1:1字可用...n:n字可用</td></tr></table>

## 29.7.4. 电源和时钟控制寄存器 （USBFS_PWRCLKCTL）

地址偏移：0x0E00

复位值：0x0000 0000

该寄存器采用字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14"></td><td>SHCLK</td><td>SUDLK</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保留为复位值。</td></tr><tr><td>1</td><td>SHCLK</td><td>停止HCLK停止HCLK,节省电量0:HCLK未停止1:HCLK停止</td></tr><tr><td>0</td><td>SUCLK</td><td>停止USB时钟停止USB时钟,节省电量0:USB时钟未停止1:USB时钟停止</td></tr></table>
