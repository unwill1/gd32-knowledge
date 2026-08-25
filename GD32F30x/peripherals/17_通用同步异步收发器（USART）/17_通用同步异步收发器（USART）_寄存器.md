## 17.4. USART 寄存器

USART0 基地址：0x4001 3800

USART1 基地址：0x4000 4400

USART2 基地址：0x4000 4800

UART3 基地址：0x4000 4C00

UART4 基地址：0x4000 5000

## 17.4.1. 状态寄存器 0（USART_STAT0）

地址偏移：0x00

复位值：0x0000 00C0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CTSF</td><td>LBDF</td><td>TBE</td><td>TC</td><td>RBNE</td><td>IDLEF</td><td>ORERR</td><td>NERR</td><td>FERR</td><td>PERR</td></tr></table>

<table><tr><td>rc_w0</td><td>rc_w0</td><td>r</td><td>rc_w0</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CTSF</td><td>CTS变化标志如果设置了USART_CTL2寄存器中CTSEN位,当nCTS输入变化时,该位由硬件置位。如果设置了USART_CTL2寄存器中CTSIE位,将产生中断。该位由软件清0。0:nCTS状态线没有变化。1:nCTS状态线发生变化。该位对UART3/4无效。</td></tr><tr><td>8</td><td>LBDF</td><td>LIN断开检测标志。寄存器USART_CTL1寄存器中LMEN置位,说明检测到LIN断开。如果USART_CTL1寄存器中LBDIE被置位时,将产生中断。该位由软件清0。0:没有检测到LIN断开字符。1:检测到LIN断开字符。</td></tr><tr><td>7</td><td>TBE</td><td>发送数据缓冲区空。上电复位或待发送数据已发送至移位寄存器后,该位置1。USART_CTL0寄存器中TBEIE被置位将产生中断。该位在软件将待发送数据写入USART_DATA时被清0。0:发送数据缓冲区不为空。1:发送数据缓冲区空。</td></tr><tr><td>6</td><td>TC</td><td>发送完成上电复位后,该位被置1。如果TBE置位,在当前数据发送完成时该位置1。USART_CTL0寄存器中TCIE被置位将产生中断。该位由软件清0。0:发送没有完成1:发送完成</td></tr><tr><td>5</td><td>RBNE</td><td>读数据缓冲区非空。当读数据缓冲区接收到来自移位寄存器的数据时,该位置1。当寄存器USART_CTL0的RBNEIE位被置位,将会有中断产生。软件可以通过对该位写0或读USART_DATA寄存器来将该位清0。0:读数据缓冲区为空。1:读数据缓冲区不为空。</td></tr><tr><td>4</td><td>IDLEF</td><td>空闲线检测标志。在一个帧时间内,在RX引脚检测到空闲状态,该位置1。当寄存器USART_CTL0的IDLEIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:未检测到空闲帧。1:检测到空闲帧。</td></tr><tr><td>3</td><td>ORERR</td><td>溢出错误在RBNE置位的情况下,如果USART_DATA寄存器接收到来自移位寄存器的数据,该位置1。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:没有检测到溢出错误。1:检测到溢出错误。</td></tr><tr><td>2</td><td>NERR</td><td>噪声错误标志在接收数据时,如果在RX引脚检测到噪声,该位被置位。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:没检测到噪声错误。1:检测到噪声错误。</td></tr><tr><td>1</td><td>FERR</td><td>帧错误接收数据期间,在停止位传输过程中,RX引脚检测到低电平,该位被置位。当寄存器USART_CTL2的ERRIE位被置位,将会有中断产生。软件先读USART_STAT0,再读USART_DATA可清除该位。0:未检测到帧错误。1:检测到帧错误。</td></tr><tr><td>0</td><td>PERR</td><td>校验错误当接收到的数据帧校验位与预期校验值不同时,该位置位。软件先读USART_STAT0,再读USART_DATA可清除该位。0:没检测到校验错误。1:检测到校验错误。</td></tr></table>

## 17.4.2. 数据寄存器（USART_DATA）

地址偏移：0x04

复位值：未定义

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">DATA[8:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>DATA[8:0]</td><td>发送或接收的数据值。软件可以通过写这些位来改变发送数据,或读这些位的值来获取接收数据。如果使能了奇偶校验,当发送数据被写入寄存器,数据的最高位(第7位或第8位取决于USART_CTL0寄存器的WL位)将被校验位取代。</td></tr></table>

## 17.4.3. 波特率寄存器（USART_BAUD）

地址偏移：0x08

复位值：0x0000 0000

使能USART（UEN=1）时，不能写该寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">INTDIV [11:0]</td><td colspan="4">FRADIV[3:0]</td></tr></table>


rw



rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:4</td><td>INTDIV[11:0]</td><td>波特率分频器的整数部分。</td></tr><tr><td>3:0</td><td>FRADIV [3:0]</td><td>波特率分频器的小数部分。</td></tr></table>

## 17.4.4. 控制寄存器 0（USART_CTL0）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>UEN</td><td>WL</td><td>WM</td><td>PCEN</td><td>PM</td><td>PERRIE</td><td>TBEIE</td><td>TCIE</td><td>RBNEIE</td><td>IDLEIE</td><td>TEN</td><td>REN</td><td>RWU</td><td>SBKCMD</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>UEN</td><td>USART使能0: USART禁用1: USART使能</td></tr><tr><td>12</td><td>WL</td><td>字长0: 8数据位1: 9数据位</td></tr><tr><td>11</td><td>WM</td><td>从静默模式唤醒方法0: 空闲线1: 地址匹配</td></tr><tr><td>10</td><td>PCEN</td><td>校验控制使能0: 校验控制禁用1: 校验控制被使能</td></tr><tr><td>9</td><td>PM</td><td>校验模式0: 偶校验1: 奇校验</td></tr><tr><td>8</td><td>PERRIE</td><td>校验错误中断使能。如果该位置1,USART_STAT0寄存器中PERR被置位时产生中断。0: 校验错误中断禁用。1: 校验错误中断使能。</td></tr><tr><td>7</td><td>TBEIE</td><td>发送缓冲区空中断使能。如果该位置1,USART_STAT0寄存器中TBE被置位时产生中断。0: 发送缓冲区空中断禁止。1: 发送缓冲区空中断使能。</td></tr><tr><td>6</td><td>TCIE</td><td>发送完成中断使能。如果该位置1,USART_STAT0寄存器中TC被置位时产生中断。0: 发送完成中断禁用。1: 发送完成中断使能。</td></tr><tr><td>5</td><td>RBNEIE</td><td>读数据缓冲区非空中断和过载错误中断使能。如果该位置1,USART_STAT0寄存器中RBNE或ORERR被置位时产生中断。0: 读数据缓冲区非空中断和过载错误中断禁用。</td></tr></table>

1：读数据缓冲区非空中断和过载错误中断使能。

4 IDLEIE IDLE线检测中断使能。

如果该位置1，USART_STAT0寄存器中IDLEF被置位时产生中断。

0：IDLE线检测中断禁用。

1：IDLE线检测中断禁用使能。

3 TEN 发送器使能

0：发送器禁用

1：发送器使能

2 REN 接收器使能

0：接收器禁用

1：接收器使能

1 RWU 接收器从静默模式中唤醒。

软件可以通过将该位置1使得USART进入静默模式，将该位清0唤醒USART。

空闲帧唤醒模式下(WM=0)，当检测到空闲帧时，该位由硬件清0。地址匹配模式下(WM=1)，当接收到一个地址匹配帧时，该位由硬件清0；或接收到一个地址非匹配帧时，由硬件置1。

0：接收器处于正常工作模式。

1：接收器处于静默模式。

0 SBKCMD 发送断开帧

软件通过发送断开帧将该位置1。

断开帧传输结束由硬件清0。

0：没有发送断开帧

1：发送断开帧

## 17.4.5. 控制寄存器 1（USART_CTL1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LMEN</td><td colspan="2">STB[1:0]</td><td>CKEN</td><td>CPL</td><td>CPH</td><td>CLEN</td><td>保留</td><td>LBDIE</td><td>LBLEN</td><td>保留</td><td></td><td colspan="3">ADDR[3:0]</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LMEN</td><td>LIN模式使能0: LIN模式禁用</td></tr></table>

1：LIN模式使能

13:12 STB[1:0] 

STOP位长

00：1停止位

01：0.5停止位

10：2停止位

11：1.5停止位

对于UART3/4，只有1位停止位和2位停止位是有效的。

11 CKEN 

CK 引脚使能

0：CK引脚禁用

1：CK引脚使能

该位对于UART3/4无效。

10 CPL 

时钟极性

该位用来设定在同步模式下CK引脚的极性。

0：CK引脚不对外发送时保持为低电平。

1：CK引脚不对外发送时保持为高电平。

该位对于UART3/4无效。

9 CPH 

时钟相位

该位用来设定在同步模式下CK引脚的相位。

0：在首个时钟边沿采样第一个数据。

1：在第二个时钟边沿采样第一个数据。

该位对于UART3/4无效。

8 CLEN 

CK信号长度

该位用来设定在同步模式下CK信号的长度。

0：8位数据帧中有7个CK脉冲，9位数据帧中有8个CK脉冲。

1：8位数据帧中有8个CK脉冲，9位数据帧中有9个CK脉冲。

该位对于UART3/4无效。

7 保留

必须保持复位值。

6 LBDIE 

LIN断开信号检测中断使能。

如果该位置1，当USART_STAT0寄存器中LBDF被置位时将产生中断。

0：断开信号检测中断禁用。

1：断开信号检测中断使能。

5 LBLEN 

LIN断开帧长度

该位用来设定在断开帧长度。

0：10位

1：11位

4 保留

必须保持复位值。

3:0 ADDR[3:0] 

USART地址

地址匹配唤醒模式下(WM=1)，如果接收到的数据帧低四位与ADDR[3:0]值不相等，USART就会进入静默模式；如果接收到的数据帧低四位与ADDR[3:0]值相等，

USART就会被唤醒。

## 17.4.6. 控制寄存器 2（USART_CTL2）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>CTSIE</td><td>CTSEN</td><td>RTSEN</td><td>DENT</td><td>DENR</td><td>SCEN</td><td>NKEN</td><td>HDEN</td><td>IRLP</td><td>IREN</td><td>ERRIE</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CTSIE</td><td>CTS中断使能如果该位置1,当USART_STAT0寄存器中CTSF被置位时将产生中断。0:CTS中断禁用。1:CTS中断使能。该位对于UART3/4无效。</td></tr><tr><td>9</td><td>CTSEN</td><td>CTS使能该位用于使能CTS硬件流控制功能。0:CTS硬件流控制禁用。1:CTS硬件流控制使能。该位对于UART3/4无效。</td></tr><tr><td>8</td><td>RTSEN</td><td>RTS使能该位用于使能RTS硬件流控制功能。0:RTS硬件流控制禁用。1:RTS硬件流控制使能。该位对于UART3/4无效。</td></tr><tr><td>7</td><td>DENT</td><td>DMA发送使能0:DMA发送模式禁用。1:DMA发送模式使能。</td></tr><tr><td>6</td><td>DENR</td><td>DMA接收使能0:DMA接收模式禁用。1:DMA接收模式使能。</td></tr><tr><td>5</td><td>SCEN</td><td>智能卡模式使能该位用于使能智能卡模式。0:智能卡模式禁用。1:智能卡模式使能。该位对于UART3/4无效。</td></tr><tr><td>4</td><td>NKEN</td><td>在智能卡模式NACK使能。该位用于智能卡模式在奇偶校验错误发生时使能NACK发送。0:当出现校验错误时不发送NACK。1:当出现校验错误时发送NACK。该位对于UART3/4无效。</td></tr><tr><td>3</td><td>HDEN</td><td>半双工使能该位用于使能半双工模式。0:半双工模式禁用。1:半双工模式使能。</td></tr><tr><td>2</td><td>IRLP</td><td>IrDA低功耗模式该位用于为IrDA模式选择低功耗模式。0:正常模式1:低功耗模式</td></tr><tr><td>1</td><td>IREN</td><td>IrDA模式使能0:IrDA禁用1:IrDA使能</td></tr><tr><td>0</td><td>ERRIE</td><td>错误中断使能当DMA接收模式(DENR=1)使能时,如果该位被置1,USART_STAT0寄存器中FERR,ORERR,NERR被置位将产生中断。0:错误中断禁用。1:错误中断使能。</td></tr></table>

## 17.4.7. 保护时间和预分频器寄存器（USART_GP）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">GUAT[7:0]</td><td colspan="8">PSC[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>GUAT[7:0]</td><td>智能卡模式下的保护时间值。TC标志置位时间延时GUAT[7:0]个波特时钟周期。</td></tr></table>

该位对于UART3/4无效。

<table><tr><td>7:0</td><td>PSC[7:0]</td><td>使能USART IrDA低功耗模式,这些位用来设定将外设时钟(PCLK1/PCLK2)分频产生低功耗频率的分频系数。00000000:保留-不要写入该值。00000001:对源时钟1分频。...11111111:对源时钟255分频。在IrDA正常模式下,PSC只能设置成00000001。在智能卡模式下,PSC[4:0]用于设定外设时钟(APB1/APB2)生成智能卡时钟的分频系数。实际的分频系数为PSC[4:0]设定值的两倍。00000:保留-不要写入该值。00001:对源时钟2分频。00010:对源时钟4分频。...11111:对源时钟62分频。在智能卡模式下,PSC[7:5]保留。</td></tr></table>

## 17.4.8. 控制寄存器 3（USART_CTL3）

偏移地址：0x80

复位值：0x0000 0000

UART3/4未使用该寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>MSBF</td><td>DINV</td><td>TINV</td><td>RINV</td><td colspan="2">保留</td><td>EBIE</td><td>RTIE</td><td colspan="3">SCRTNUM[2:0]</td><td>RTEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>MSBF</td><td>高位在前该位用于设定数据在发送或接收时的顺序。0:数据发送/接收,采用低位在前。1:数据发送/接收,采用高位在前。USART被使能(UEN=1)时,这一位不能被改写。</td></tr><tr><td>10</td><td>DINV</td><td>数据位反转该位用于设定在发送或接收时数据位的极性。0:数据位信号值没有反转。1:数据位信号值被反转。USART被使能 (UEN=1) 时,这一位不能被改写。</td></tr><tr><td>9</td><td>TINV</td><td>TX 引脚电平反转该位用于设定TX引脚极性。0: TX引脚信号值没有反转。1: TX引脚信号值被反转。USART被使能 (UEN=1) 时,这一位不能被改写。</td></tr><tr><td>8</td><td>RINV</td><td>RX引脚电平反转。该位用于设定RX引脚极性。0: RX引脚信号值没有反转。1: RX引脚信号值被反转。USART被使能 (UEN=1) 时,这一位不能被改写。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EBIE</td><td>块结束标志中断使能位。如果该位置1, USART_STAT1寄存器中EBF被置位时产生中断。0: 块中断禁用。1: 块中断使能。</td></tr><tr><td>4</td><td>RTIE</td><td>接收超时标志中断使能位。如果该位置1, USART_STAT1寄存器中RTF被置位时产生中断。0: 接收超时中断禁用。1: 接收超时中断使能。</td></tr><tr><td>3:1</td><td>SCRTNUM[2:0]</td><td>智能卡自动重试次数寄存器。在智能卡模式下,这些位用来设定在发送和接收时重试的次数。在发送模式下,一帧数据可以重发 SCRTNUM 次。如果一帧数据发送失败 SCRTNUM+1次,FERR 被置位。在接收模式下,USART接收一个数据帧可以执行 SCRTNUM+1 次。如果一个数据帧校验位不匹配事件产生 SCRTNUM+1 次,RBNE 位和 PERR 位被置位。当这些位被设置为 0x0 时,在发送模式下这些位将不会自动发送。</td></tr><tr><td>0</td><td>RTEN</td><td>接收器超时使能。该位用于使能USART接收超时。0: 接收器超时检测功能禁用。1: 接收器超时检测功能被使能。</td></tr></table>

## 17.4.9. 接收超时寄存器（USART_RT）

偏移地址：0x84

复位值：0x0000 0000

UART3/4未使用该寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">BL[7:0]</td><td colspan="8">RT[23:16]</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="9">rw</td><td colspan="6">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="16">RT[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>BL[7:0]</td><td>块长度这些位用于设定智能卡T=1的接收时,块的长度。它的值等于信息字节的长度+结束部分的长度(1-LEC/2-CRC)-1。这个值可以在块接收开始去设置(用于需要从块的序言提取块的长度的情形),这个值在每一个接收时钟周期只能设置一次。在智能卡模式下,当TBE=0时,块的长度计数器被清0。在其他模式下,当REN=0(禁用接收器)或者当USART_STAT1寄存器的EBF位被写0时,块的长度计数器被清0。</td></tr><tr><td>23:0</td><td>RT[23:0]</td><td>接收器超时阈值。该位域用于指定接收超时值,单位是波特时钟的时长。标准模式下,如果在最后一个字节接收后,在RT规定的时长内,没有检测到新的起始位,USART_STAT1寄存器中RTF标志被置位。在智能卡模式,这个值被用来实现CWT和BWT。在这种情况下,超时检测是从最后一个接收字节的起始位开始算的。这些位可以在工作时改写。假如一个新数据到来的时间比RT规定的晚,RTF标志会被置位。对于每个接收字符,这个值只能改写一次。</td></tr></table>

## 17.4.10. 状态寄存器 1（USART_STAT1）

偏移地址：0x88

复位值：0x0000 0000

UART3/4未使用该寄存器

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BSY</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>EBF</td><td>RTF</td><td colspan="11">保留</td></tr></table>


w0 w0


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BSY</td><td>忙标志USART接收一帧数据时被置位。0: USART接收通道空闲。1: USART接收通道忙。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>EBF</td><td>块结束标志该位在接收字节数(从块起始开始计数,包含序言)等于或者大于BLEN+4时被置位。USART_CTL3寄存器中EBIE被置位将产生中断。软件可以通过写0清除该位。0:块结束事件没有发生。1:块结束事件发生。</td></tr><tr><td>11</td><td>RTF</td><td>接收超时标志该位在RX引脚空闲时间已经超过RT值时被置位。USART_CTL3寄存器中RTIE被置位将产生中断。软件可以通过写0清除该位。0:接收器超时事件没有发生。1:接收器超时事件发生。</td></tr><tr><td>10:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
