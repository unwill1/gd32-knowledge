## 20.1.4. USART 寄存器

USART0 基地址：0x4001 3800

USART1 基地址：0x4000 4400

USART2 基地址：0x4000 4800

UART3 基地址：0x4000 4C00

UART4 基地址：0x4000 5000

## 状态寄存器 0 （USART_STAT0）

地址偏移：0x00

复位值：0x0000 00C0

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CTSF</td><td>LBDF</td><td>TBE</td><td>TC</td><td>RBNE</td><td>IDLEF</td><td>ORERR</td><td>NERR</td><td>FERR</td><td>PERR</td></tr><tr><td colspan="6"></td><td>rc_w0</td><td>rc_w0</td><td>r</td><td>rc_w0</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CTSF</td><td>CTS变化标志。如果设置了USART_CTL2寄存器中CTSEN位,当nCTS输入变化时,该位由硬件置位。如果设置了USART_CTL2寄存器中CTSIE位,将产生中断。该位由软件清0。0:nCTS状态线没有变化。1:nCTS状态线发生变化。该位对UART3/4无效。</td></tr><tr><td>8</td><td>LBDF</td><td>LIN断开检测标志。寄存器USART_CTL1寄存器中LMEN置位,说明检测到LIN断开。如果USART_CTL1寄存器中LBDIE被置位时,将产生中断。该位由软件清0。0:没有检测到LIN断开字符。1:检测到LIN断开字符。</td></tr><tr><td>7</td><td>TBE</td><td>发送数据缓冲区空上电复位或待发送数据已发送至移位寄存器后,该位置1。USART_CTL0寄存器中TBEIE被置位将产生中断。该位在软件将待发送数据写入USART_DATA时被清0。0:发送数据缓冲区不为空。</td></tr></table>

1：发送数据缓冲区空。

<table><tr><td>6</td><td>TC</td><td>发送完成上电复位后,该位被置1。如果TBE置位,在当前数据发送完成时该位置1。USART_CTL0寄存器中TCIE被置位将产生中断。该位由软件清0。0:发送没有完成。1:发送完成。</td></tr><tr><td>5</td><td>RBNE</td><td>读数据缓冲区非空。当读数据缓冲区接收到来自移位寄存器的数据时,该位置1。当寄存器USART_CTL0的RBNEIE位被置位,将会有中断产生。软件可以通过对该位写0或读USART_DATA寄存器来将该位清0。0:读数据缓冲区为空。1:读数据缓冲区不为空。</td></tr><tr><td>4</td><td>IDLEF</td><td>空闲线检测标志。在一个帧时间内,在RX引脚检测到空闲状态,该位置1。当寄存器USART_CTL0的IDLEIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:未检测到空闲帧。1:检测到空闲帧。</td></tr><tr><td>3</td><td>ORERR</td><td>溢出错误。在RBNE置位的情况下,如果USART_DATA寄存器接收到来自移位寄存器的数据,该位置1。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:没有检测到溢出错误。1:检测到溢出错误。</td></tr><tr><td>2</td><td>NERR</td><td>噪声错误标志。将USART_CTL2寄存器中OSB清0,在接收数据时,如果在RX引脚检测到噪声,该位被置位。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:没检测到噪声错误。1:检测到噪声错误。</td></tr><tr><td>1</td><td>FERR</td><td>帧错误。接收数据期间,在停止位传输过程中,RX引脚检测到低电平,该位被置位。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:未检测到帧错误。1:检测到帧错误。</td></tr><tr><td>0</td><td>PERR</td><td>校验错误。当接收到的数据帧校验位与预期校验值不同时,该位置位。软件先读USART_STAT0,再读或者写USART_DATA可清除该位。0:没检测到校验错误。</td></tr></table>

1：检测到校验错误。

## 数据寄存器 （USART_DATA）

地址偏移：0x04

复位值：未定义

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">DATA[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>DATA[8:0]</td><td>发送或接收的数据值。软件可以通过写这些位来改变要发送的数据,或读这些位的值来获取接收到的数据。如果使能了奇偶校验,当发送数据被写入寄存器,数据的最高位(第7位或第8位取决于USART_CTL0寄存器的WL位)将被校验位取代。</td></tr></table>

## 波特率寄存器 （USART_BAUD）

地址偏移：0x08

复位值：0x0000 0000

使能 USART（UEN=1）时，不能写该寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">INTDIV [11:0]</td><td colspan="4">FRADIV[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:4</td><td>INTDIV[11:0]</td><td>波特率分频器的整数部分。</td></tr><tr><td>3:0</td><td>FRADIV [3:0]</td><td>波特率分频器的小数部分。</td></tr></table>

## 控制寄存器 0 （USART_CTL0）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OVSMOD</td><td>保留</td><td>UEN</td><td>WL</td><td>WM</td><td>PCEN</td><td>PM</td><td>PERRIE</td><td>TBEIE</td><td>TCIE</td><td>RBNEIE</td><td>IDLEIE</td><td>TEN</td><td>REN</td><td>RWU</td><td>SBKCMD</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>OVSMOD</td><td>采样模式0: 16倍采样1: 8倍采样如果SCEN=1, IREN=1或者LMEN=1, OVSMOD由硬件强制为0。</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>UEN</td><td>USART使能0: USART禁用1: USART使能</td></tr><tr><td>12</td><td>WL</td><td>字长0: 8数据位1: 9数据位</td></tr><tr><td>11</td><td>WM</td><td>从静默模式唤醒方法。0: 空闲线1: 地址掩码</td></tr><tr><td>10</td><td>PCEN</td><td>校验控制使能。0: 校验控制禁用。1: 校验控制使能。</td></tr><tr><td>9</td><td>PM</td><td>校验模式0: 偶校验1: 奇校验</td></tr><tr><td>8</td><td>PERRIE</td><td>校验错误中断使能。如果该位置1, USART_STAT0寄存器中PERR被置位时产生中断。0: 校验错误中断禁用。1: 校验错误中断使能。</td></tr><tr><td>7</td><td>TBEIE</td><td>发送缓冲区空中断使能。如果该位置1,USART_STAT0寄存器中TBE被置位时产生中断。0:发送缓冲区空中断禁止。1:发送缓冲区空中断使能。</td></tr><tr><td>6</td><td>TCIE</td><td>发送完成中断使能。如果该位置1,USART_STAT0寄存器中TC被置位时产生中断。0:发送完成中断禁用。1:发送完成中断使能。</td></tr><tr><td>5</td><td>RBNEIE</td><td>读数据缓冲区非空中断和过载错误中断使能。如果该位置1,USART_STAT0寄存器中RBNE或ORERR被置位时产生中断。0:读数据缓冲区非空中断和过载错误中断禁用。1:读数据缓冲区非空中断和过载错误中断使能。</td></tr><tr><td>4</td><td>IDLEIE</td><td>IDLE线检测中断使能。如果该位置1,USART_STAT0寄存器中IDLEF被置位时产生中断。0:IDLE线检测中断禁用。1:IDLE线检测中断使能。</td></tr><tr><td>3</td><td>TEN</td><td>发送器使能。0:发送器禁用。1:发送器使能。</td></tr><tr><td>2</td><td>REN</td><td>接收器使能。0:接收器禁用。1:接收器使能。</td></tr><tr><td>1</td><td>RWU</td><td>接收器从静默模式中唤醒。软件可以通过将该位置1使得USART进入静默模式,将该位清0唤醒USART。空闲帧唤醒模式下(WM=0),当检测到空闲帧时,该位由硬件清0。地址掩码模式下(WM=1),当接收到一个地址匹配帧时,该位由硬件清0;或接收到一个地址非匹配帧时,由硬件置1。0:接收器处于正常工作模式。1:接收器处于静默模式。</td></tr><tr><td>0</td><td>SBKCMD</td><td>发送断开帧。软件通过发送断开帧将该位置1。断开帧传输结束由硬件清0。0:没有发送断开帧。1:发送断开帧。</td></tr></table>

## 控制寄存器 1 （USART_CTL1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LMEN</td><td colspan="2">STB[1:0]</td><td>CKEN</td><td>CPL</td><td>CPH</td><td>CLEN</td><td>保留</td><td>LBDIE</td><td>LBLEN</td><td>保留</td><td></td><td colspan="3">ADDR[3:0]</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LMEN</td><td>LIN模式使能。0: LIN模式禁用。1: LIN模式使能。</td></tr><tr><td>13:12</td><td>STB[1:0]</td><td>STOP位长00: 1停止位01: 0.5停止位10: 2停止位11: 1.5停止位对于UART3/4,只有1位停止位和两位停止位是有效的。</td></tr><tr><td>11</td><td>CKEN</td><td>CK引脚使能0: CK引脚禁用1: CK引脚使能该位对于UART3/4无效。</td></tr><tr><td>10</td><td>CPL</td><td>时钟极性该位用来设定在同步模式下CK引脚的极性。0: CK引脚不对外发送时保持为低电平。1: CK引脚不对外发送时保持为高电。该位对于UART3/4无效。</td></tr><tr><td>9</td><td>CPH</td><td>时钟相位该位用来设定在同步模式下CK引脚的相位。0: 在首个时钟边沿采样第一个数据1: 在第二个时钟边沿采样第一个数据该位对于UART3/4无效。</td></tr><tr><td>8</td><td>CLEN</td><td>CK信号长度。该位用来设定在同步模式下CK信号的长度。0: 8位数据帧中有7个CK脉冲,9位数据帧中有8个CK脉冲。1: 8位数据帧中有8个CK脉冲,9位数据帧中有9个CK脉冲。该位对于UART3/4无效。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>LBDIE</td><td>LIN断开信号检测中断使能。如果该位置1,当USART_STAT0寄存器中LBDF被置位时将产生中断。0: 断开信号检测中断禁用。1:断开信号检测中断使能。</td></tr><tr><td>5</td><td>LBLEN</td><td>LIN 断开帧长度该位用来设定在断开帧长度。0:10 位1:11 位</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>ADDR[3:0]</td><td>USART 地址地址掩码唤醒模式下(WM=1),如果接收到的数据帧低四位与 ADDR[3:0]值不相等,USART 就会进入静默模式;如果接收到的数据帧低四位与 ADDR[3:0]值相等,USART 就会被唤醒。</td></tr></table>

## 控制寄存器 2 （USART_CTL2）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>OSB</td><td>CTSIE</td><td>CTSEN</td><td>RTSEN</td><td>DENT</td><td>DENR</td><td>SCEN</td><td>NKEN</td><td>HDEN</td><td>IRLP</td><td>IREN</td><td>ERRIE</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>OSB</td><td>一个数据位采样一次的方法。该位用于选择采样方法。当该位被置位时,USART 对一个数据位取一个采样点,而不是一个数据位取三个采样点。当使用该方法时,噪声错误标志(NERR)需禁用。0:三次采样方法。1:一次采样方法。</td></tr><tr><td>10</td><td>CTSIE</td><td>CTS 中断使能。如果该位置 1,当 USART_STAT0 寄存器中 CTSF 被置位时将产生中断。0:CTS 中断禁用。1:CTS 中断使能。该位对于 UART3/4 无效。</td></tr><tr><td>9</td><td>CTSEN</td><td>CTS 使能该位用于使能 CTS 硬件流控制功能。0:CTS 硬件流控制禁用。1:CTS 硬件流控制使能。该位对于 UART3/4 无效。</td></tr><tr><td>8</td><td>RTSEN</td><td>RTS使能该位用于使能RTS硬件流控制功能。0:RTS硬件流控制禁用。1:RTS硬件流控制使能。该位对于UART3/4无效。</td></tr><tr><td>7</td><td>DENT</td><td>DMA发送使能0:DMA发送模式禁用。1:DMA发送模式使能。</td></tr><tr><td>6</td><td>DENR</td><td>DMA接收使能0:DMA接收模式禁用。1:DMA接收模式使能。</td></tr><tr><td>5</td><td>SCEN</td><td>智能卡模式使能该位用于使能智能卡模式。0:智能卡模式禁用。1:智能卡模式使能。该位对于UART3/4无效。</td></tr><tr><td>4</td><td>NKEN</td><td>在智能卡模式NACK使能。该位用于智能卡模式在奇偶校验错误发生时使能NACK发送。0:当出现校验错误时不发送NACK。1:当出现校验错误时发送NACK。该位对于UART3/4无效。</td></tr><tr><td>3</td><td>HDEN</td><td>半双工使能该位用于使能半双工模式。0:半双工模式禁用1:半双工模式使能</td></tr><tr><td>2</td><td>IRLP</td><td>IrDA低功耗模式。该位用于为IrDA模式选择低功耗模式。0:正常模式1:低功耗模式</td></tr><tr><td>1</td><td>IREN</td><td>IrDA模式使能0:IrDA禁用1:IrDA使能</td></tr><tr><td>0</td><td>ERRIE</td><td>错误中断使能。当DMA接收模式(DENR=1)使能时,如果该位被置1,USART_STAT0寄存器中FERR,ORERR,NERR被置位将产生中断。0:错误中断禁用。1:错误中断使能。</td></tr></table>

## 保护时间和预分频器寄存器 （USART_GP）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">GUAT[7:0]</td><td colspan="8">PSC[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>GUAT[7:0]</td><td>智能卡模式下的保护时间值。TC标志置位时间延时GUAT[7:0]个波特时钟周期。该位对于UART3/4无效。</td></tr><tr><td>7:0</td><td>PSC[7:0]</td><td>使能USART IrDA低功耗模式,这些位用来设定将外设时钟(PCLK1/PCLK2)分频产生低功耗频率的分频系数。00000000:保留-不要写入该值。00000001:对源时钟1分频。...11111111:对源时钟255分频。在IrDA正常模式下,PSC只能设置成00000001。在智能卡模式下,PSC[4:0]用于设定外设时钟(APB1/APB2)生成智能卡时钟的分频系数。实际的分频系数为PSC[4:0]设定值的两倍。00000:保留-不要写入该值。00001:对源时钟2分频。00010:对源时钟4分频。...11111:对源时钟62分频。在智能卡模式下,PSC[7:5]保留。</td></tr></table>

控制寄存器 3 （USART_CTL3）

偏移地址：0x80

复位值：0x0000 0000

UART3/4 未使用该寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>MSBF</td><td>DINV</td><td>TINV</td><td>RINV</td><td colspan="2">保留</td><td>EBIE</td><td>RTIE</td><td colspan="3">SCRTNUM[2:0]</td><td>RTEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>MSBF</td><td>高位在前该位用于设定数据在发送或接收时的顺序。0:数据发送/接收,采用低位在前。1:数据发送/接收,采用高位在前。USART被使能(UEN=1)时,这一位不能被改写。</td></tr><tr><td>10</td><td>DINV</td><td>数据位反转该位用于设定在发送或接收时数据位的极性。0:数据位信号值没有反转。1:数据位信号值被反转。USART被使能(UEN=1)时,这一位不能被改写。</td></tr><tr><td>9</td><td>TINV</td><td>TX引脚电平反转。该位用于设定TX引脚极性。0:TX引脚信号值没有反转。1:TX引脚信号值被反转。USART被使能(UEN=1)时,这一位不能被改写。</td></tr><tr><td>8</td><td>RINV</td><td>RX引脚电平反转。该位用于设定RX引脚极性。0:RX引脚信号值没有反转。1:RX引脚信号值被反转。USART被使能(UEN=1)时,这一位不能被改写。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EBIE</td><td>块结束标志中断使能位如果该位置1,USART_STAT1寄存器中EBF被置位时产生中断。0:块中断禁用。1:块中断使能。</td></tr><tr><td>4</td><td>RTIE</td><td>接收超时标志中断使能位。如果该位置1,USART_STAT1寄存器中RTF被置位时产生中断。0:接收超时中断禁用。1:接收超时中断使能。</td></tr><tr><td>3:1</td><td>SCRTNUM[2:0]</td><td>智能卡自动重试次数寄存器。在智能卡模式下,这些位用来设定在发送和接收时重试的次数。在发送模式下,一帧数据可以重发SCRTNUM次。如果一帧数据发送失败SCRTNUM+1次,FERR被置位。在接收模式下,USART接收一个数据帧可以执行SCRTNUM+1次。如果一个数据</td></tr></table>

帧校验位不匹配事件产生 SCRTNUM+1 次，RBNE 位和 PERR 位被置位。当这些位被设置为 0x0 时，在发送模式下这些位将不会自动发送。

0 RTEN 接收器超时使能。

该位用于使能 USART接收超时。

0：接收器超时检测功能禁用。

1：接收器超时检测功能使能。

## 接收超时寄存器 （USART_RT）

偏移地址：0x84

复位值：0x0000 0000

UART3/4未使用该寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">BL[7:0]</td><td colspan="8">RT[23:16]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>BL[7:0]</td><td>块长度这些位用于设定智能卡 T=1 的接收时,块的长度。它的值等于信息字节的长度+结束部分的长度(1-LEC/2-CRC) - 1。这个值可以在块接收开始去设置(用于需要从块的序言提取块的长度的情形),这个值在每一个接收时钟周期只能设置一次。在智能卡模式下,当 TBE=0 时,块的长度计数器被清 0。在其他模式下,当 REN=0 (禁用接收器)或者当 USART_STAT1 寄存器的 EBF 位被写 0 时,块的长度计数器被清 0。</td></tr><tr><td>23:0</td><td>RT[23:0]</td><td>接收器超时阈值。该位域用于指定接收超时值,单位是波特时钟的时长。标准模式下,如果在最后一个字节接收后,在 RT 规定的时长内,没有检测到新的起始位,USART_STAT1 寄存器中 RTF 标志被置位。在智能卡模式,这个值被用来实现 CWT 和 BWT。在这种情况下,超时检测是从最后一个接收字节的起始位开始算的。这些位可以在工作时改写。假如一个新数据到来的时间比 RT 规定的晚,RTF 标志会被置位。对于每个接收字符,这个值只能改写一次。注意:当 16 倍过采样时,RT[23:0]不能被配置为 0xFFFFFFF。</td></tr></table>

状态寄存器 1 （USART_STAT1）

偏移地址：0x88

复位值：0x0000 0000

UART3/4 未使用该寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BSY</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>EBF</td><td>RTF</td><td colspan="11">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BSY</td><td>忙标志USART接收一帧数据时被置位。0:USART接收通道空闲。1:USART接收通道忙。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>EBF</td><td>块结束标志。该位在接收字节数(从块开始开始计数,包含序言)等于或者大于BLEN+4时被置位。USART_CTL3寄存器中EBIE被置位将产生中断。软件可以通过写0清除该位。0:块结束事件没有发生。1:块结束事件发生。</td></tr><tr><td>11</td><td>RTF</td><td>接收超时标志。该位在RX引脚空闲时间已经超过RT值时被置位。USART_CTL3寄存器中RTIE被置位将产生中断。软件可以通过写0清除该位。0:接收器超时事件没有发生。1:接收器超时事件发生。</td></tr><tr><td>10:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

GD 控制寄存器 （USART_GDCTL）

偏移地址：0xD0

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>CDIE</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>CD</td><td>保留</td><td>CDEN</td><td></td></tr><tr><td colspan="3">w0c</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>由硬件强制为0。</td></tr><tr><td>16</td><td>CDIE</td><td>冲突检测中断使能。0: 冲突检测中断禁用。1: 冲突检测中断使能。</td></tr><tr><td>15:9</td><td>保留</td><td>由硬件强制为0。</td></tr><tr><td>8</td><td>CD</td><td>冲突检测状态。0: 未检测到冲突。1: 半双工模式下检测到冲突。</td></tr><tr><td>7:2</td><td>保留</td><td>由硬件强制为0。</td></tr><tr><td>1</td><td>CDEN</td><td>冲突检测使能。0: 禁用1: 使能</td></tr><tr><td>0</td><td>保留</td><td>由硬件强制为0。</td></tr></table>

## 20.2.4. USART 寄存器

USART5基地址：0x4001 7000

USART 控制寄存器 0 （USART_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>EBIE</td><td>RTIE</td><td colspan="10">保留</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="10"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OVSMOD</td><td>AMIE</td><td>MEN</td><td>WL</td><td>WM</td><td>PCEN</td><td>PM</td><td>PERRIE</td><td>TBEIE</td><td>TCIE</td><td>RBNEIE</td><td>IDLEIE</td><td>TEN</td><td>REN</td><td>UESM</td><td>UEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>EBIE</td><td>块尾中断使能。0: 中断禁止1: 中断使能</td></tr><tr><td>26</td><td>RTIE</td><td>接收超时中断使能。0: 中断禁止1: 中断使能</td></tr><tr><td>25:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>OVSMOD</td><td>过采样模式。0: 16倍过采样。1: 8倍过采样。在LIN, IrDA和智能卡模式,该位保持清0。当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>14</td><td>AMIE</td><td>ADDR字符匹配中断使能。0: ADDR字符匹配中断禁用。1: ADDR字符匹配中断使能。</td></tr><tr><td>13</td><td>MEN</td><td>静默模式使能。0: 静默模式禁用。1: 静默模式被使能。</td></tr><tr><td>12</td><td>WL</td><td>字长0: 8数据位1: 9数据位当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>WM</td><td>从静默模式唤醒方法。0:空闲线1:地址标记当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>10</td><td>PCEN</td><td>校验控制使能。0:校验控制禁用。1:校验控制被使能。当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>9</td><td>PM</td><td>校验模式0:偶校验1:奇校验当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>PERRIE</td><td>校验错误中断使能。0:校验错误中断禁用。1:当USART_STAT寄存器的PERR位置位时,将触发中断。</td></tr><tr><td>7</td><td>TBEIE</td><td>发送寄存器空中断使能。0:中断禁止。1:当USART_STAT寄存器的TBE位置位时,将触发中断。</td></tr><tr><td>6</td><td>TCIE</td><td>发送完成中断使能。如果该位置1,USART_STAT寄存器中TC被置位时产生中断。0:发送完成中断禁用。1:发送完成中断使能。</td></tr><tr><td>5</td><td>RBNEIE</td><td>读数据缓冲区非空中断和过载错误中断使能。0:读数据缓冲区非空中断和过载错误中断禁用。1:当USART_STAT寄存器的ORERR或RBNE位置位时,将触发中断。</td></tr><tr><td>4</td><td>IDLEIE</td><td>IDLE线检测中断使能。0:IDLE线检测中断禁用。1:当USART_STAT寄存器的IDLEF位置位时,将触发中断。</td></tr><tr><td>3</td><td>TEN</td><td>发送器使能。0:发送器关闭。1:发送器打开。</td></tr><tr><td>2</td><td>REN</td><td>接收器使能。0:接收器关闭。1:接收器打开并且开始搜索起始位。</td></tr><tr><td>1</td><td>UESM</td><td>USART在深度睡眠模式下使能。0:USART不能从深度睡眠模式唤醒MCU。1:USART能从深度睡眠模式唤醒MCU。条件是USART的时钟源必须是IRC8M或LXTAL。</td></tr><tr><td>0</td><td>UEN</td><td>USART使能。</td></tr></table>

0：USART预分频器和输出禁用。

1：USART预分频器和输出被使能。

## USART 控制寄存器 1 （USART_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ADDR[7:0]</td><td>RTEN</td><td colspan="3">保留</td><td>MSBF</td><td>DINV</td><td>TINV</td><td>RINV</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STRP</td><td>LMEN</td><td colspan="2">STB[1:0]</td><td>CKEN</td><td>CPL</td><td>CPH</td><td>CLEN</td><td>保留</td><td>LBDIE</td><td>LBLEN</td><td>ADDM</td><td colspan="4">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ADDR[7:0]</td><td>USART的节点地址。这些位给出USART的节点地址。在多处理器通信并且静默模式或者深度睡眠模式期间,这些位用来唤醒进行地址标记的检测。接收到的最高位为1的数据帧将和这些位进行比较。当ADDM位被清零时,仅仅ADDR[3:0]被用来比较。在正常的接收期间,这些位也用来进行字符检测。所有接收到的字符(8位)与ADDR[7:0]的值进行比较,如果匹配,AMF标志将被置位。当接收器(REN=1)和USART(UEN=1)被使能时,该位域不能被改写。</td></tr><tr><td>23</td><td>RTEN</td><td>接收器超时使能。0:接收器超时功能禁用。1:接收器超时功能被使能。</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>MSBF</td><td>高位在前0:数据发送/接收,采用低位在前。1:数据发送/接收,采用高位在前。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>18</td><td>DINV</td><td>数据位反转。0:数据位信号值没有反转。1:数据位信号值被反转。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>17</td><td>TINV</td><td>TX管脚电平反转。0:TX管脚信号值没有反转。1:TX管脚信号值被反转。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>16</td><td>RINV</td><td>RX管脚电平反转。</td></tr></table>

<table><tr><td></td><td></td><td>0: RX管脚信号值没有反转。1: RX管脚信号值被反转。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>15</td><td>STRP</td><td>交换 TX/RX 管脚。0: TX 和 RX 管脚功能不被交换。1: TX 和 RX 管脚功能被交换。当 USART 被使能 (UEN=1) 时,该位域不能改写。</td></tr><tr><td>14</td><td>LMEN</td><td>LIN 模式使能。0: LIN 模式关闭。1: LIN 模式开启。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>13:12</td><td>STB[1:0]</td><td>STOP 位长00: 1 停止位01: 0.5 停止位10: 2 停止位11: 1.5 停止位USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>11</td><td>CKEN</td><td>CK 管脚使能。0: CK 管脚禁用。1: CK 管脚被使能。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>10</td><td>CPL</td><td>时钟极性0: 在同步模式下,CK 管脚不对外发送时保持为低电平。1: 在同步模式下,CK 管脚不对外发送时保持为高电平。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>9</td><td>CPH</td><td>时钟相位0: 在同步模式下,在首个时钟边沿采样第一个数据。1: 在同步模式下,在第二个时钟边沿采样第一个数据。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>8</td><td>CLEN</td><td>CK 长度0: 在同步模式下,最后一位(MSB)的时钟脉冲不输出到 CK 管脚。1: 在同步模式下,最后一位(MSB)的时钟脉冲输出到 CK 管脚。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>LBDIE</td><td>LIN 断开信号检测中断使能。0: 断开信号检测中断禁用。1: 当 USART_STAT 的 LBDF 位置位,将产生中断。</td></tr><tr><td>5</td><td>LBDL</td><td>LIN 断开帧长度。0: 检测 10 位断开帧。</td></tr></table>

<table><tr><td></td><td></td><td>1: 检测 11 位断开帧。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>4</td><td>ADDM</td><td>地址检测模式。该位用来选择 4 位地址检测或全位地址检测。0: 4 位地址检测。1: 全位地址检测。在 7 位,8 位和 9 位数据模式下,地址检测分别按 6 位,7 位和 8 位地址(ADDR[5:0], ADDR[6:0] 和 ADDR[7:0])执行。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## USART 控制寄存器 2 （USART_CTL2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>WUIE</td><td colspan="2">WUM[1:0]</td><td colspan="3">SCRTNUM[2:0]</td><td>保留</td></tr><tr><td colspan="9"></td><td>rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>DDRE</td><td>OVRD</td><td>OSB</td><td colspan="3">保留</td><td>DENT</td><td>DENR</td><td>SCEN</td><td>NKEN</td><td>HDEN</td><td>IRLP</td><td>IREN</td><td>ERRIE</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>WUIE</td><td>从深度睡眠模式唤醒中断使能。0:从深度睡眠模式唤醒中断禁用。1:从深度睡眠模式唤醒中断被使能。</td></tr><tr><td>21:20</td><td>WUM[1:0]</td><td>从深度睡眠模式唤醒模式这个位域指定什么事件可以置位USART_STAT寄存器中的WUF(从深度睡眠唤醒标志)标志。00:WUF在地址匹配的时候置位。如何实现地址匹配在ADDR和ADDM中定义。01:保留10:WUF在检测到起始位时置位。11:WUF在检测到RBNE时置位。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>19:17</td><td>SCRTNUM[2:0]</td><td>智能卡自动重试数目。在智能卡模式下,这些位用来指定在发送和接收时重试的次数。在发送模式下,它指的是在产生发送错误(FERR位置位)之前自动重试的发送次数。在接收模式下,它指的是在产生接收错误(RBNE位和PERR位置位)之前自动重试的接收次数。当这些位被设置为0x0时,在发送模式下这些位将不会自动发送。</td></tr><tr><td>16:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>DDRE</td><td>在接收错误时屏蔽DMA请求0:在发生接收错误的情况下,不禁用DMA。所有的错误数据不会产生DMA请求,以确保错误的数据不会被传输,但是下一个接收到的正确的数据会被传输。在发生接收错误时,RBNE位保持0以阻止过载错误,但是相应错误标志位会被置位。这种模式可用于智能卡模式。1:在接收错误的情况下,DMA请求会被屏蔽,直到相应的标志位被清0。RBNE标志和相应的错误标志位会被置位。软件在清除错误标志前,必须首先失能DMA接收(DMAR=0)或清RBNE。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>12</td><td>OVRD</td><td>溢出禁止0:溢出功能被使能。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将被置位,并且新数据将会丢失。1:溢出功能禁止。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将不会被置位,新数据会将USART_RDATA寄存器以前的内容覆盖。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>OSB</td><td>单次采样方式。0:三次采样方法。1:一次采样方法。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>10:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>DENT</td><td>DMA发送使能。0:关闭DMA发送模式。1:开启DMA发送模式</td></tr><tr><td>6</td><td>DENR</td><td>DMA接收使能。0:关闭DMA接收模式。1:开启DMA接收模式。</td></tr><tr><td>5</td><td>SCEN</td><td>智能卡模式使能。0:智能卡模式禁用。1:智能卡模式使能。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>4</td><td>NKEN</td><td>智能卡模式NACK使能。0:当出现校验错误时不发送NACK。1:当出现校验错误时发送NACK。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>3</td><td>HDEN</td><td>半双工使能0:禁用半双工模式。1:开启半双工模式。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>2</td><td>IRLP</td><td>IrDA 低功耗模式0: 正常模式1: 低功耗模式USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>1</td><td>IREN</td><td>IrDA 模式使能0: IrDA 禁用1: IrDA 被使能USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>0</td><td>ERRIE</td><td>多级缓存通信模式的错误中断使能0: 禁用错误中断。1: 在多级缓存通信时,当 USART_STAT 寄存器的 FERR 位,ORERR 位或 NERR 位被置位时,会产生中断。</td></tr></table>

## USART 波特率寄存器 （USART_ BAUD）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当USART（UEN=1）被使能时，该寄存器不能被改写。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">BRR [15:4]</td><td colspan="4">BRR[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:4</td><td>BRR[15:4]</td><td>波特率分频系数的整数部分。INTDIV = BRR[15:4]</td></tr><tr><td>3:0</td><td>BRR[3:0]</td><td>波特率分频系数的小数部分。如果 OVSMOD = 0, FRADIV = BRR [3:0]。如果 OVSMOD = 1, FRADIV = BRR [2:0], BRR [3]必须被置 0。</td></tr></table>

## USART保护时间和预分频器寄存器 （USART_GP）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

USART被使能（UEN=1）时，该寄存器不能被改写。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">GUAT[7:0]</td><td colspan="8">PSC[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>GUAT[7:0]</td><td>在智能卡模式下的保护时间值。USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr><tr><td>7:0</td><td>PSC[7:0]</td><td>预分频器值在红外低功耗模式下,对系统时钟进行分频已获得低功耗模式下的频率。寄存器的值是分频系数。00000000: 保留 - 不设置这个值00000001: 1 分频00000010: 2 分频...在 IrDA 正常模式下的分频值00000001: 仅能设为这个值在智能卡模式下,对系统时钟进行分频的值存于 PSC[4:0]位域中。PSC[7:5]位保持为复位值。分频系数是寄存器中值的两倍。00000: 保留 -不设置这个值00001: 2 分频00010: 4 分频00011: 6 分频...USART 被使能 (UEN=1) 时,该位域不能被改写。</td></tr></table>

## USART 接收超时寄存器 （USART_RT）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">BL[7:0]</td><td colspan="8">RT[23:16]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>BL[7:0]</td><td>块长度这些位给出了智能卡T=1的接收时块的长度。它的值等于信息字节的长度+结束部分的长度(1-LEC/2-CRC)-1。这个值可以在块接收开始时设置(用于需要从块的序言提取块的长度的情形),这个只在每一个接收时钟周期只能设置一次。在智能卡模式下,当TBE=0时,块的长度计数器被清0。在其他模式下,当REN=0(禁用接收器)并且/或者当EBC位被写1时块的长度计数器被清0。</td></tr><tr><td>23:0</td><td>RT[23:0]</td><td>接收器超时门限。该位域指定接收超时值,单位是波特时钟的时长。标准模式下,如果在最后一个字节接收后,在RT规定的时长内,没有检测到新的起始位,RTF标志被置位。在智能卡模式,这个值被用来实现CWT和BWT。在这种情况下,超时检测是从最后一个接收字节的起始位开始。这些位可以在工作时改写。假如一个新数据到来的时间比RT规定的晚,RTF标志会被置位。对于每个接收字符,这个值只能改写一次。注意:当16倍过采样时,RT[23:0]不能被配置为0xFFFFF。</td></tr></table>

## USART 请求寄存器 （USART_CMD）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>TXFCMD</td><td>RXFCMD</td><td>MMCMD</td><td>SBKCMD</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TXFCMD</td><td>发送数据清空请求。向该位写1去置位TBE标志位,以取消发送数据。</td></tr><tr><td>3</td><td>RXFCMD</td><td>接收数据清空请求。向该位写1来清除RBNE标志位,以丢弃未读的接收数据。</td></tr><tr><td>2</td><td>MMCMD</td><td>静默模式请求。向该位写1使USART进入静默模式并且置位RWU标志位。</td></tr><tr><td>1</td><td>SBKCMD</td><td>发送断开帧请求。向该位写1置位SBKF标志并使USART在空闲时发送一个断开帧。</td></tr></table>

必须保持复位值。

## USART 状态寄存器 （USART_STAT）

地址偏移：0x1C

复位值：0x0000 00C0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>REA</td><td>TEA</td><td>WUF</td><td>RWU</td><td>SBF</td><td>AMF</td><td>BSY</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>EBF</td><td>RTF</td><td colspan="2">保留</td><td>LBDF</td><td>TBE</td><td>TC</td><td>RBNE</td><td>IDLEF</td><td>ORERR</td><td>NERR</td><td>FERR</td><td>PERR</td></tr><tr><td></td><td></td><td></td><td>r</td><td>r</td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>REA</td><td>接收使能通知标志。这位反映了USART核心逻辑的接收使能状态,该位可以通过硬件设置。0:USART核心接收逻辑禁用。1:USART核心接收逻辑被使能。</td></tr><tr><td>21</td><td>TEA</td><td>发送使能通知标志。该位反映了USART核心逻辑的发送使能状态,该位可以通过硬件设置。0:USART核心发送逻辑禁用。1:USART核心发送逻辑被使能。</td></tr><tr><td>20</td><td>WUF</td><td>从深度睡眠模式唤醒标志。0:没有从深度睡眠模式唤醒。1:已从深度睡眠模式唤醒,如果在USART_CTL2寄存器的WUFIE=1并且MCU处于深度睡眠模式,将引发一个中断。当检测到一个唤醒事件时,该位通过硬件置位,这个事件在WUM位域被定义。向USART_INTC寄存器中的WUC写1,该位被清0。当UESM被清0时,该位清0。</td></tr><tr><td>19</td><td>RWU</td><td>接收器从静默模式唤醒。该位表示USART处于静默模式。0:接收器在工作状态。1:接收器在静默状态。当在唤醒和静默模式切换时,它通过硬件清0或者置1。静默模式控制(地址帧还是空闲帧)是用通过USART_CTL0寄存器的WAKE位选择。如果选择空闲信号唤醒,只能通过向USART_CMD寄存器的MMCMD位写1来将该位置位。</td></tr><tr><td>18</td><td>SBF</td><td>断开信号发送标识。0:没发送断开字符。1:将要发送断开字符。该位表示一个断开发送信号被请求。通过向USART_CMD寄存器的SBKCMD写1来置位。在断开帧的停止位发送期间,硬件清0。</td></tr><tr><td>17</td><td>AMF</td><td>ADDR匹配标志。0:ADDR和接收到的字符不匹配。1:ADDR和接收到的字符匹配,如果USART_CTL0寄存器的AMIE=1,将引发一个中断。当接收到ADDR[7:0]中定义的字符时,硬件置位。通过向USART_INTC寄存器的AMC写1清0。</td></tr><tr><td>16</td><td>BSY</td><td>忙标志0:USART处于空闲。1:USART正在接收。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>EBF</td><td>块结束标志0:块没有结束。1:块结束已到(足够的字节数),如果USART_CTL1寄存器的EBIE=1,将引发一个中断。当接收到的字节数(从块开始,包括序言部分)等于或大于BLEN+4,硬件置位。通过向USART_INTC寄存器的EBC写1清0。</td></tr><tr><td>11</td><td>RTF</td><td>接收超时标志。0:尚未超时。1:已经超时,如果USART_CTL1寄存器的RTIE被置位,将会引发中断。如果空闲的时间已经超过了在USART_RT寄存器中设定的RT值,通过硬件置1。通过向USART_INTC寄存器的RTC位写1清0。在智能卡模式,这个超时相当于CWT或BWT计时。</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>LBDF</td><td>LIN断开检测标志。0:没有检测到LIN断开字符。1:检测到LIN断开字符。当USART_CTL1寄存器的LBDIE位被置位时,将会有中断产生。当LIN断开帧被检测到的时候,硬件置位。通过向USART_INTC寄存器的LBDC位写1,清零该位。</td></tr><tr><td>7</td><td>TBE</td><td>发送数据寄存器空。0:数据没有发送到移位寄存器。1:数据发送到移位寄存器。如果USART_CTL0寄存器的TBEIE位置位,将会有中断产生。当USART_TDATA寄存器的内容已经被转移到移位寄存器或者向USART_CMD寄存器的TXFCMD位写1时,由硬件置位。通过向USART_TDATA寄存器中写数据来清0。</td></tr><tr><td>6</td><td>TC</td><td>发送完成0: 发送没有完成。1: 发送完成。如果USART_CTL0寄存器的TCIE被置位,将会有中断产生。如果一个包含数据的帧的发送完成且TBE被置位,该位由硬件置位。通过向USART_INTC寄存器的TCC位写1清0。</td></tr><tr><td>5</td><td>RBNE</td><td>读数据缓冲区非空。0: 没有接收到数据。1: 已接收到数据并且可以读取。当寄存器USART_CTL0的RBNEIE位被置位,将会有中断产生。当接收移位寄存器的内容已经被转移到寄存器USART_RDATA,由硬件置位。通过读USART_RDATA寄存器或向USART_CMD寄存器的RXFCMD位写1清0。</td></tr><tr><td>4</td><td>IDLEF</td><td>空闲线检测标志。0: 没检测到空闲线。1: 检测到空闲线。如果USART_CTL0寄存器的IDLEIE位置1,将会有中断产生。当检测到空闲线时,通过硬件置位。直到RBNE位置位,否则它不会被再次置位。向USART_INTC寄存器的IDLEC位写1清0。</td></tr><tr><td>3</td><td>ORERR</td><td>溢出错误0: 未检测到溢出错误。1: 检测到溢出错误。在多级缓存通信中,如果寄存器USART_CTL0的RBNEIE位置位,将会引发中断。如果寄存器USART_CTL2的ERRIE位置位也会引发中断。在RBNE置位的情况下,如果接收移位寄存器的数据传递给USART_RDATA寄存器,将会由硬件置位。向USART_INTC寄存器的OREC位写1清0。</td></tr><tr><td>2</td><td>NERR</td><td>噪声错误标志。0: 未检测到噪声错误。1: 检测到噪声错误。在多级缓存通信中,如果寄存器USART_CTL2的ERRIE位置位,将会有中断产生。在接收帧的时候检测到噪声错误,将会由硬件置位。向寄存器USART_INTC的NEC位写1清0。</td></tr><tr><td>1</td><td>FERR</td><td>帧错误0: 未检测到帧错误。1: 检测到帧错误或者断开字符。在多级缓存通信中,如果寄存器USART_CTL2的ERRIE位置位,将会有中断产生。当一个不同步,强噪声或者断开字符被检测到时,硬件置位。在智能卡模式下,当发送次数达到上限,仍然没有收到发送成功应答(卡一直响应NACKs),该位也将被置位。向USART_INTC寄存器的FEC位写1清0。</td></tr><tr><td>0</td><td>PERR</td><td>校验错误0: 未检测到校验错误。1: 检测到校验错误,在多级缓存通信中,如果寄存器USART_CTL0的PERRIE位置位,将会有中断产生。</td></tr></table>

当在接收模式的时候检测到校验错误，将会由硬件置位。

向 USART_INTC 寄存器的 PEC 位写 1 清 0。

## USART 中断标志清除寄存器 （USART_INTC）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td>WUC</td><td>保留</td><td></td><td>AMC</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td>w</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>EBC</td><td>RTC</td><td colspan="2">保留</td><td>LBDC</td><td>保留</td><td>TCC</td><td>保留</td><td>IDLEC</td><td>OREC</td><td>NEC</td><td>FEC</td><td>PEC</td></tr><tr><td></td><td></td><td></td><td>w</td><td>w</td><td></td><td></td><td>w</td><td></td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>WUC</td><td>从深度睡眠模式唤醒标志的清除。向该位写1清除USART_STAT寄存器的WUF位。</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>AMC</td><td>ADDR匹配标志清除。向该位写1清除USART_STAT寄存器的AMF位。</td></tr><tr><td>16:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>EBC</td><td>块结束标志清除。向该位写1清除USART_STAT寄存器的EBF位。</td></tr><tr><td>11</td><td>RTC</td><td>接收超时标志清除。向该位写1清除USART_STAT寄存器的RTF标志。</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>LBDC</td><td>LIN断开字符检测标志清除。向该位写1清除USART_STAT寄存器的LBDF标志位。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TCC</td><td>发送完成标志清除。向该位写1清除USART_STAT寄存器的TC位。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>IDLEC</td><td>空闲线检测标志清除。向该位写1清除USART_STAT寄存器的IDLEF位。</td></tr><tr><td>3</td><td>OREC</td><td>溢出标志清除。向该位写1清除USART_STAT寄存器的ORERR位。</td></tr><tr><td>2</td><td>NEC</td><td>噪声检测清除。向该位写1清除USART_STAT寄存器的NERR位。</td></tr><tr><td>1</td><td>FEC</td><td>帧格式错误标志清除。向该位写1清除USART_STAT寄存器的FERR位。</td></tr><tr><td>0</td><td>PEC</td><td>校验错误标志清除。向该位写1清除USART_STAT寄存器的PERR位。</td></tr></table>

## USART 数据接收寄存器 （USART_RDATA）

地址偏移：0x24

复位值：未定义

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">RDATA[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>RDATA[8:0]</td><td>接收数据的值。包含接收到的数据字节。如果接收到的数据打开了奇偶校验位(USART_CTL0 寄存器的 PCEN 置 1),那么接收到的数据的最高位(第 7 位或 8 位,取决于数据的长度)是奇偶校验位。</td></tr></table>

## USART 数据发送寄存器 （USART_TDATA）

地址偏移：0x28

复位值：未定义

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">TDATA[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr></table>

8:0 TDATA[8:0] 发送数据的值。

包含发送的数据字节。

如果发送到的数据打开了奇偶校验位（USART_CTL0 寄存器的 PCEN置 1），那么发送的数据的最高位（第 7 位或 8 位取决于数据的长度）将会被奇偶校验位替代。只有当 USART_STAT寄存器的 TBE 位被置位时，这个寄存器才可以改写。

## USART 兼容性控制寄存器 （USART_CHC）

地址偏移：0xC0

复位值： 0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>EPERR</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EPERR</td><td>校验错误超前检测标志。在 RBNE 置位前,校验位被检测到时该标志置位。软件写 0 可以清除该位。0:没有检测到校验错误。1:检测到校验错误。</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## USART 接收 FIFO 控制和状态寄存器 （USART_RFCS）

地址偏移：0xD0

复位值：0x0000 0400

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFFINT</td><td colspan="3">RFCNT[2:0]</td><td>RFF</td><td>RFE</td><td>RFFIE</td><td>RFEN</td><td colspan="7">保留</td><td>ELNACK</td></tr><tr><td>r_w0</td><td colspan="3">r</td><td>r</td><td>r</td><td>rw</td><td>rw</td><td colspan="7"></td><td>rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:16</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>15</td><td colspan="3">RFFINT</td><td colspan="12">接收FIFO满中断标志。</td></tr><tr><td>14:12</td><td colspan="3">RFCNT[2:0]</td><td colspan="12">接收FIFO计数值。</td></tr><tr><td>11</td><td colspan="3">RFF</td><td colspan="12">接收FIFO满标志。0:接收FIFO不为满。1:接收FIFO满。</td></tr><tr><td>10</td><td colspan="3">RFE</td><td colspan="12">接收FIFO空标志。0:接收FIFO不为空。1:接收FIFO空。</td></tr><tr><td>9</td><td colspan="3">RFFIE</td><td colspan="12">接收FIFO满中断使能。0:禁止接收FIFO满中断。1:使能接收FIFO满中断。</td></tr><tr><td>8</td><td colspan="3">RFEN</td><td colspan="12">接收FIFO使能。当UESM=1,该位置位。0:禁止使用接收FIFO。1:使能接收FIFO。</td></tr><tr><td>7:1</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>0</td><td colspan="3">ELNACK</td><td colspan="12">若选择了智能卡模式,提前NACK。如果检测到校验位错误,NACK脉冲提前1/16位的时间。0:若选择了智能卡模式,禁止提前NACK。1:若选择了智能卡模式,使能提前NACK。</td></tr></table>
