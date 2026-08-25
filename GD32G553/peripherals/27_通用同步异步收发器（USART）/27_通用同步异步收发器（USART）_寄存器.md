## 27.4. USART 寄存器

USART0 基地址：0x4001 3800

USART1 基地址：0x4000 4400

USART2 基地址：0x4000 4800

UART3 基地址：0x4000 4C00

UART4 基地址：0x4000 5000

## 27.4.1. USART 控制寄存器 0（USART_CTL0）

地址偏移：0x00

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>AMIE1</td><td colspan="2">保留</td><td>WL1</td><td>EBIE</td><td>RTIE</td><td colspan="5">DEA[4:0]</td><td colspan="5">DED[4:0]</td></tr><tr><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2">OVSMOD</td><td rowspan="2">AMIE0</td><td rowspan="2">MEN</td><td rowspan="2">WLO</td><td rowspan="2">WM</td><td rowspan="2">PCEN</td><td rowspan="2">PM</td><td rowspan="2">PERRIE</td><td>TBEIE</td><td rowspan="2">TCIE</td><td>RBNEIE</td><td rowspan="2">IDLEIE</td><td rowspan="2">TEN</td><td rowspan="2">REN</td><td rowspan="2">UESM</td><td rowspan="2">UEN</td></tr><tr><td>TFNFIE</td><td>RFNEIE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>AMIE1</td><td>ADDR1中字符匹配中断使能0:ADDR1中字符匹配中断禁用1:ADDR1中字符匹配中断使能</td></tr><tr><td>30:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>WL1</td><td>字长1WL1与WL0位决定字长。00:8数据位01:9数据位10:7数据位11:10数据位当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>27</td><td>EBIE</td><td>块尾中断使能0:中断禁止1:中断使能在UART3 / UART4中,该位保留。</td></tr><tr><td>26</td><td>RTIE</td><td>接收超时中断使能0:中断禁止1:中断使能在UART3 / UART4中,该位保留。</td></tr><tr><td>25:21</td><td>DEA[4:0]</td><td>驱动使能置位时间这些数字用来定义DE(驱动使能)信号的置位与第一个字节的起始位之间的时间间隔。它以采样时间为单位(1/8或1/16位时间),可以通过OVSMOD位来配置。当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>20:16</td><td>DED[4:0]</td><td>驱动使能置低时间这些位用来定义一个发送信息最后一个字节的停止位与置低DE(驱动使能)信号之间的时间间隔。它以采样时间为单位(1/8或1/16位时间),可以通过OVSMOD位来配置。当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>15</td><td>OVSMOD</td><td>过采样模式0:16倍过采样1:8倍过采样在LIN,IrDA和智能卡模式,该位保持清0。当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>14</td><td>AMIE0</td><td>ADDR0中字符匹配中断使能0:ADDR0中字符匹配中断禁用1:ADDR0中字符匹配中断使能</td></tr><tr><td>13</td><td>MEN</td><td>静默模式使能0:静默模式禁用1:静默模式被使能</td></tr><tr><td>12</td><td>WL0</td><td>字长0WL1与WL0位决定字长。0:8数据位1:9数据位当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>WM</td><td>从静默模式唤醒方法0:空闲线1:地址标记当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>10</td><td>PCEN</td><td>校验控制使能</td></tr></table>

<table><tr><td></td><td></td><td>0:校验控制禁用1:校验控制被使能当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>9</td><td>PM</td><td>校验模式0:偶校验1:奇校验当USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>PERRIE</td><td>校验错误中断使能0:校验错误中断禁用1:当USART_STAT寄存器的PERR位置位时,将触发中断。</td></tr><tr><td rowspan="2">7</td><td>TBEIE</td><td>当FIFO禁用:发送寄存器空中断使能0:中断禁止1:当USART_STAT寄存器的TBE位置位时,将触发中断。</td></tr><tr><td>TFNFIE</td><td>当FIFO使能:发送FIFO非满中断使能0:中断禁止1:当USART_STAT寄存器的TFNF位置位时,将触发中断。</td></tr><tr><td>6</td><td>TCIE</td><td>发送完成中断使能如果该位置1,USART_STAT寄存器中TC被置位时产生中断。0:发送完成中断禁用1:发送完成中断使能</td></tr><tr><td rowspan="2">5</td><td>RBNEIE</td><td>当FIFO禁用:读数据缓冲区非空中断和过载错误中断使能0:读数据缓冲区非空中断和过载错误中断禁用1:当USART_STAT寄存器的ORERR或RBNE位置位时,将触发中断。</td></tr><tr><td>RFNEIE</td><td>当FIFO使能:接收FIFO非空中断使能和过载错误中断使能0:接收FIFO非空中断和过载错误中断禁用1:当USART_STAT寄存器的ORERR或RFNE位置位时,将触发中断。</td></tr><tr><td>4</td><td>IDLEIE</td><td>IDLE线检测中断使能0:IDLE线检测中断禁用1:当USART_STAT寄存器的IDLEF位置位时,将触发中断。</td></tr><tr><td>3</td><td>TEN</td><td>发送器使能0:发送器关闭</td></tr></table>

<table><tr><td></td><td></td><td>1:发送器打开</td></tr><tr><td>2</td><td>REN</td><td>接收器使能0:接收器关闭1:接收器打开并且开始搜索起始位。</td></tr><tr><td>1</td><td>UESM</td><td>USART在深度睡眠模式下使能0:USART不能从深度睡眠模式唤醒MCU1:USART能从深度睡眠模式唤醒MCU。条件是USART的时钟源必须是CK_IRC8M或CK_LXTAL。在UART3 / UART4中,该位保留。</td></tr><tr><td>0</td><td>UEN</td><td>USART使能0:USART预分频器和输出禁用1:USART预分频器和输出被使能</td></tr></table>

## 27.4.2. USART 控制寄存器 1（USART_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ADDR0[7:0]</td><td>RTEN</td><td colspan="3">保留</td><td>MSBF</td><td>DINV</td><td>TINV</td><td>RINV</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STRP</td><td>LMEN</td><td colspan="2">STB[1:0]</td><td>CKEN</td><td>CPL</td><td>CPH</td><td>CLEN</td><td>保留</td><td>LBDIE</td><td>LBLEN</td><td>ADDM0</td><td colspan="3">保留</td><td>AMENO</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ADDR0[7:0]</td><td>USART的节点地址0这些位给出USART的节点地址0。在多处理器通信并且静默模式或者深度睡眠模式期间,这些位用来唤醒进行地址匹配的检测。接收到的最高位为1的数据帧将和这些位进行比较。当ADDM0位被清零时,仅仅ADDR0[3:0]被用来比较。在正常的接收期间,这些位也用来进行字符检测。所有接收到的字符(8位)与ADDR0[7:0]的值进行比较,如果匹配,AMF0标志将被置位。当接收器(REN=1)和USART(UEN=1)被使能时,该位域不能被改写。</td></tr><tr><td>23</td><td>RTEN</td><td>接收器超时使能0:接收器超时功能禁用1:接收器超时功能被使能</td></tr></table>

<table><tr><td></td><td></td><td>在UART3 / UART4中,该位保留。</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>MSBF</td><td>高位在前0:数据发送/接收,采用低位在前1:数据发送/接收,采用高位在前USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>18</td><td>DINV</td><td>数据位反转0:数据位信号值没有反转1:数据位信号值被反转USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>17</td><td>TINV</td><td>TX管脚电平反转0:TX管脚信号值没有反转1:TX管脚信号值被反转.USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>16</td><td>RINV</td><td>RX管脚电平反转0:RX管脚信号值没有反转.1:RX管脚信号值被反转USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>15</td><td>STRP</td><td>交换TX/RX管脚0:TX和RX管脚功能不被交换1:TX和RX管脚功能被交换当USART被使能(UEN=1)时,该位域不能改写。</td></tr><tr><td>14</td><td>LMEN</td><td>LIN模式使能0:LIN模式关闭1:LIN模式开启USART被使能(UEN=1)时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>13:12</td><td>STB[1:0]</td><td>STOP位长00:1停止位01:0.5停止位10:2停止位11:1.5停止位USART被使能(UEN=1)时,该位域不能被改写。注意:0.5停止位和1.5停止位不适用于UART3 / UART4。</td></tr><tr><td>11</td><td>CKEN</td><td>CK管脚使能0:CK管脚禁用</td></tr></table>

<table><tr><td></td><td></td><td>1: CK管脚被使能USART被使能 (UEN = 1)时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>10</td><td>CPL</td><td>时钟极性0: 在同步模式下,CK管脚不对外发送时保持为低电平1: 在同步模式下,CK管脚不对外发送时保持为高电平USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>9</td><td>CPH</td><td>时钟相位0: 在同步模式下,在首个时钟边沿采样第一个数据1: 在同步模式下,在第二个时钟边沿采样第一个数据USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>CLEN</td><td>CK长度0: 在同步模式下,最后一位(MSB)的时钟脉冲不输出到CK管脚1: 在同步模式下,最后一位(MSB)的时钟脉冲输出到CK管脚USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>LBDIE</td><td>LIN断开信号检测中断使能0: 断开信号检测中断禁用1: 当USART_STAT的LBDF位置位,将产生中断。在UART3 / UART4中,该位保留。</td></tr><tr><td>5</td><td>LBLEN</td><td>LIN断开帧长度0: 检测10位断开帧1: 检测11位断开帧USART被使能 (UEN = 1)时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>4</td><td>ADDM0</td><td>地址0检测模式该位用来选择4位地址检测或全位地址检测。0: 4位地址检测1: 全位地址检测。在7位,8位和9位数据模式下,地址检测分别按6位,7位和8位地址(ADDR0[5:0],ADDR0[6:0]和ADDR0[7:0])执行。USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AMENO</td><td>地址0匹配使能0: 地址0匹配模式禁用1: 地址0匹配模式使能</td></tr></table>

## 27.4.3. USART 控制寄存器 2（USART_CTL2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ADDR1[7:0]</td><td>ADDM1</td><td>WUIE</td><td colspan="2">WUM[1:0]</td><td colspan="3">SCRTNUM[2:0]</td><td>AMEN1</td></tr><tr><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DEP</td><td>DEM</td><td>DDRE</td><td>OVRD</td><td>OSB</td><td>CTSIE</td><td>CTSEN</td><td>RTSEN</td><td>DENT</td><td>DENR</td><td>SCEN</td><td>NKEN</td><td>HDEN</td><td>IRLP</td><td>IREN</td><td>ERRIE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ADDR1[7:0]</td><td>USART的节点地址1这些位给出USART的节点地址1。在多处理器通信并且静默模式或者深度睡眠模式期间,这些位用来唤醒进行地址标记的检测。接收到的最高位为1的数据帧将和这些位进行比较。当ADDM1位被清零时,仅仅ADDR1[3:0]被用来比较。在正常的接收期间,这些位也用来进行字符检测。所有接收到的字符(8位)与ADDR1[7:0]的值进行比较,如果匹配,AMF1标志将被置位。当接收器(REN=1)和USART(UEN=1)被使能时,该位域不能被改写。</td></tr><tr><td>23</td><td>ADDM1</td><td>地址1检测模式该位用来选择4位地址检测或全位地址检测。0:4位地址检测1:全位地址检测。在7位,8位和9位数据模式下,地址检测分别按6位,7位和8位地址(ADDR1[5:0],ADDR1[6:0]和ADDR1[7:0])执行。USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>22</td><td>WUIE</td><td>从深度睡眠模式唤醒中断使能0:从深度睡眠模式唤醒中断禁用1:从深度睡眠模式唤醒中断被使能在UART3 / UART4,该位保留。</td></tr><tr><td>21:20</td><td>WUM[1:0]</td><td>从深度睡眠模式唤醒模式这个位域指定什么事件可以置位USART_STAT寄存器中的WUF(从深度睡眠唤醒标志)标志。00:WUF在地址匹配的时候置位。如何实现地址匹配在ADDR和ADDM中定义。01:保留10:WUF在检测到起始位时置位11:WUF在检测到RBNE时置位USART被使能 (UEN = 1)时,该位域不能被改写。在UART3 / UART4,该位保留。</td></tr><tr><td>19:17</td><td>SCRTNUM[2:0]</td><td>智能卡自动重试数目在智能卡模式下,这些位用来指定在发送和接收时重试的次数。在发送模式下,它指的是在产生发送错误(FERR位置位)之前自动重试的发送次数。在接收模式下,它指的是在产生接收错误(RBNE位和PERR位置位)之前自动重试的接收次数。当这些位被设置为0x0时,在发送模式下这些位将不会自动发送。USART被使能 (UEN = 1)时,该位域被清零,并停止重发。在UART3 / UART4中,该位保留。</td></tr><tr><td>16</td><td>AMEN1</td><td>地址1匹配使能0: 地址1匹配模式禁用1: 地址1匹配模式使能</td></tr><tr><td>15</td><td>DEP</td><td>驱动使能的极性选择模式0: DE信号高有效1: DE信号低有效USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>14</td><td>DEM</td><td>驱动使能模式用户使能该位以后,可以通过DE信号对外部收发器进行控制。DE信号是从RTS管脚输出的。0: DE功能禁用1: DE功能开启USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>13</td><td>DDRE</td><td>在接收错误时屏蔽DMA请求0: 在发生接收错误的情况下,不禁用DMA。所有的错误数据不会产生DMA请求,以确保错误的数据不会被传输,但是下一个接收到的正确的数据会被传输。在发生接收错误时,RBNE位保持0以阻止过载错误,但是相应错误标志位会被置位。这种模式可用于智能卡模式。1: 在接收错误的情况下,DMA请求会被屏蔽,直到相应的标志位被清0。RBNE标志和相应的错误标志位会被置位。软件在清除错误标志前,必须首先失能DMA接收(DENR = 0)或清RBNE。USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>12</td><td>OVRD</td><td>溢出禁止0: 溢出功能被使能。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将被置位,并且新数据将会丢失。1: 溢出功能禁止。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将不会被置位,新数据会将USART_RDATA寄存器以前的内容覆盖。USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>OSB</td><td>单次采样方式0:三次采样方法1:一次采样方法USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>10</td><td>CTSIE</td><td>CTS中断使能0:CTS中断屏蔽1:当USART_STAT的CTS位置位时,会产生中断。</td></tr><tr><td>9</td><td>CTSEN</td><td>CTS使能0:CTS硬件流控禁用1:CTS硬件流控被使能USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>RTSEN</td><td>RTS使能0:RTS硬件流控禁用1:RTS硬件流控被使能,只有当接收缓冲区有空间的时候,才会请求下一个数据。USART被使能 (UEN = 1)时,该位域不能被改写。</td></tr><tr><td>7</td><td>DENT</td><td>DMA发送使能0:关闭DMA发送模式1:开启DMA发送模式</td></tr><tr><td>6</td><td>DENR</td><td>DMA接收使能0:关闭DMA接收模式1:开启DMA接收模式</td></tr><tr><td>5</td><td>SCEN</td><td>智能卡模式使能0:智能卡模式禁用1:智能卡模式使能USART被使能 (UEN = 1)时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>4</td><td>NKEN</td><td>智能卡模式NACK使能0:当出现校验错误时不发送NACK1:当出现校验错误时发送NACKUSART被使能 (UEN = 1)时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>3</td><td>HDEN</td><td>半双工使能0:禁用半双工模式1:开启半双工模式</td></tr><tr><td>2</td><td>IRLP</td><td>IrDA低功耗模式0: 正常模式1: 低功耗模式USART被使能 (UEN = 1) 时,该位域不能被改写。</td></tr><tr><td>1</td><td>IREN</td><td>IrDA模式使能0: IrDA禁用1: IrDA被使能USART被使能 (UEN = 1) 时,该位域不能被改写。在UART3 / UART4中,该位保留。</td></tr><tr><td>0</td><td>ERRIE</td><td>多级缓存通信模式的错误中断使能0: 禁用错误中断1: 在多级缓存通信时,当USART_STAT寄存器的FERR位,ORERR位或NERR位被置位时,会产生中断。</td></tr></table>

## 27.4.4. USART 波特率寄存器（USART_BAUD）

地址偏移：0x0C

复位值：0x0000 0000

当USART（UEN = 1）被使能时，该寄存器不能被改写。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">BRR [15:4]</td><td colspan="4">BRR[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:4</td><td>BRR[15:4]</td><td>波特率分频系数的整数部分INTDIV = BRR[15:4]</td></tr><tr><td>3:0</td><td>BRR[3:0]</td><td>波特率分频系数的小数部分如果OVSMOD = 0, FRADIV = BRR [3:0];如果OVSMOD = 1, FRADIV = BRR [2:0], BRR [3]必须被置0。</td></tr></table>

## 27.4.5. USART 保护时间和预分频器寄存器（USART_GP）

地址偏移：0x10

复位值：0x0000 0000

USART被使能（UEN = 1）时，该寄存器不能被改写。

在UART3 / UART4中，该寄存器保留。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">GUAT[7:0]</td><td colspan="8">PSC[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>GUAT[7:0]</td><td>在智能卡模式下的保护时间值USART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>7:0</td><td>PSC[7:0]</td><td>预分频器值在红外低功耗模式下,对系统时钟进行分频已获得低功耗模式下的频率。寄存器的值是分频系数00000000:保留-不设置这个值00000001:1分频00000010:2分频...在IrDA正常模式下的分频值00000001:仅能设为这个值在智能卡模式下,对系统时钟进行分频的值存于PSC[4:0]位域中。PSC[7:5]位保持为复位值。分频系数是寄存器中值的两倍。00000:保留-不设置这个值00001:2分频00010:4分频00011:6分频...USART被使能(UEN=1)时,该位域不能被改写。</td></tr></table>

## 27.4.6. USART 接收超时寄存器（USART_RT）

地址偏移：0x14

复位值：0x0000 0000

在UART3 / UART4中，该寄存器保留。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">BL[7:0]</td><td colspan="8">RT[23:16]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>BL[7:0]</td><td>块长度这些位给出了智能卡T=1的接收时块的长度。它的值等于信息字节的长度+结束部分的长度(1-LEC/2-CRC)-1。这个值可以在块接收开始时设置(用于需要从块的序言提取块的长度的情形),这个只在每一个接收时钟周期只能设置一次。在智能卡模式下,当TBE=0时,块的长度计数器被清0。在其他模式下,当REN=0(禁用接收器)并且/或者当EBC位被写1时块的长度计数器被清0。</td></tr><tr><td>23:0</td><td>RT[23:0]</td><td>接收器超时门限该位域指定接收超时值,单位是波特时钟的时长标准模式下,如果在最后一个字节接收后,在RT规定的时长内,没有检测到新的起始位,RTF标志被置位。在智能卡模式,这个值被用来实现CWT和BWT。在这种情况下,超时检测是从最后一个接收字节的起始位开始。这些位可以在工作时改写。假如一个新数据到来的时间比RT规定的晚,RTF标志会被置位。对于每个接收字符,这个值只能改写一次。注意:当16倍过采样时,RT[23:0]不能被配置为0xFFFFF。</td></tr></table>

## 27.4.7. USART 请求寄存器（USART_CMD）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>TXFCMD</td><td>RXFCMD</td><td>MMCMD</td><td>SBKCMD</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TXFCMD</td><td>发送数据清空请求向该位写1去置位TBE标志位,以取消发送数据。</td></tr><tr><td>3</td><td>RXFCMD</td><td>接收数据清空请求向该位写1来清除RBNE标志位,以丢弃未读的接收数据。</td></tr><tr><td>2</td><td>MMCMD</td><td>静默模式请求向该位写1使USART进入静默模式并且置位RWU标志位。</td></tr><tr><td>1</td><td>SBKCMD</td><td>发送断开帧请求向该位写1置位SBF标志并使USART在空闲时发送一个断开帧。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 27.4.8. USART 状态寄存器（USART_STAT）

地址偏移：0x1C

复位值：0x0000 00C0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>REA</td><td>TEA</td><td>WUF</td><td>RWU</td><td>SBF</td><td>AMF0</td><td>BSY</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="2">保留</td><td rowspan="2">AMF1</td><td rowspan="2">EBF</td><td rowspan="2">RTF</td><td rowspan="2">CTS</td><td rowspan="2">CTSF</td><td rowspan="2">LBDF</td><td>TBE</td><td rowspan="2">TC</td><td>RBNE</td><td rowspan="2">IDLEF</td><td rowspan="2">ORERR</td><td rowspan="2">NERR</td><td rowspan="2">FERR</td><td rowspan="2">PERR</td></tr><tr><td>TFNF</td><td>RFNE</td></tr><tr><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>REA</td><td>接收使能通知标志这位反映了USART核心逻辑的接收使能状态,该位可以通过硬件设置。0: USART核心接收逻辑禁用1: USART核心接收逻辑被使能</td></tr><tr><td>21</td><td>TEA</td><td>发送使能通知标志该位反映了USART核心逻辑的发送使能状态,该位可以通过硬件设置。0: USART核心发送逻辑禁用1: USART核心发送逻辑被使能在UART3/UART4中,该位保留。</td></tr><tr><td>20</td><td>WUF</td><td>从深度睡眠模式唤醒标志0: 没有从深度睡眠模式唤醒1: 已从深度睡眠模式唤醒,如果在USART_CTL2寄存器的WUFIE = 1并且MCU处于深度睡眠模式,将引发一个中断。当检测到一个唤醒事件时,该位通过硬件置位,这个事件在WUM位域被定义。向USART_INTC寄存器中的WUC写1,该位被清0。当UESM被清0时,该位清0。在UART3 / UART4中,该位保留。</td></tr><tr><td>19</td><td>RWU</td><td>接收器从静默模式唤醒该位表示USART处于静默模式。0: 接收器在工作状态1: 接收器在静默状态当在唤醒和静默模式切换时,它通过硬件清0或者置1。静默模式控制(地址帧还是空闲帧)是用通过USART_CTL0寄存器的WM位选择。如果选择空闲信号唤醒,只能通过向USART_CMD寄存器的MMCMD位写1来将该位置位。</td></tr><tr><td>18</td><td>SBF</td><td>断开信号发送标识0: 没发送断开字符1: 将要发送断开字符该位表示一个断开发送信号被请求。通过向USART_CMD寄存器的SBKCMD写1来置位。在断开帧的停止位发送期间,硬件清0。</td></tr><tr><td>17</td><td>AMF0</td><td>ADDR0中字符匹配标志0: ADDR0中字符和接收到的字符不匹配1: ADDR0中字符和接收到的字符匹配,如果USART_CTL0寄存器的AMIE0 = 1,将引发一个中断。当接收到ADDR0[7:0]中定义的字符时,硬件置位。通过向USART_INTC寄存器的AMC0写1清0。</td></tr><tr><td>16</td><td>BSY</td><td>忙标志0: USART处于空闲1: USART正在接收</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>AMF1</td><td>ADDR1中字符匹配标志0: ADDR1中字符和接收到的字符不匹配1: ADDR1中字符和接收到的字符匹配,如果USART_CTL0寄存器的AMIE1=1,将引发一个中断。当接收到ADDR1[7:0]中定义的字符时,硬件置位。通过向USART_INTC寄存器的AMC1写1清0。</td></tr><tr><td>12</td><td>EBF</td><td>块结束标志0: 块没有结束1: 块结束已到(足够的字节数),如果USART_CTL1寄存器的EBIE=1,将引发一个中断。当接收到的字节数(从块开始,包括序言部分)等于或大于BLEN+4,硬件置位。通过向USART_INTC寄存器的EBC写1清0。在UART3 / UART4中,该位保留。</td></tr><tr><td>11</td><td>RTF</td><td>接收超时标志0: 尚未超时1: 已经超时,如果USART_CTL1寄存器的RTIE被置位,将会引发中断。如果空闲的时间已经超过了在USART_RT寄存器中设定的RT值,通过硬件置1。通过向USART_INTC寄存器的RTC位写1清0。在智能卡模式,这个超时相当于CWT或BWT计时。在UART3 / UART4中,该位保留。</td></tr><tr><td>10</td><td>CTS</td><td>CTS电平这个值等于nCTS输入引脚电平的反向拷贝。0: nCTS输入引脚高电平1: nCTS输入引脚低电平</td></tr><tr><td>9</td><td>CTSF</td><td>CTS变化标志0: nCTS状态线没有变化1: nCTS状态线发生变化 如果USART_CTL2寄存器的CTSIE位置位,将引发中断。当nCTS输入变化时,由硬件置位。通过向USART_INTC寄存器的CTSC位写1,清零该位。</td></tr><tr><td>8</td><td>LBDF</td><td>LIN断开检测标志0: 没有检测到LIN断开字符1: 检测到LIN断开字符。当USART_CTL1寄存器的LBDIE位被置位时,将会有中断产生。当LIN断开帧被检测到的时候,硬件置位。通过向USART_INTC寄存器的LBDC位写1,清零该位。在UART3 / UART4中,该位保留。</td></tr><tr><td rowspan="2">7</td><td>TBE</td><td>当FIFO模式禁用:发送数据寄存器空0:数据没有发送到移位寄存器1:数据发送到移位寄存器。如果USART_CTL0寄存器的TBEIE位置位,将会有中断产生。当USART_TDATA寄存器的内容已经被转移到移位寄存器或者向USART_CMD寄存器的TXFCMD位写1时,由硬件置位。通过向USART_TDATA寄存器中写数据来清0。</td></tr><tr><td>TFNF</td><td>当FIFO模式使能:传输FIFO非满0:传输FIFO满1:传输FIFO非满。如果USART_CTL0寄存器的TFNFIE位置位,将会有中断产生。当发送FIFO非满时,由硬件置位。当FIFO满时,由硬件置1。注意:在TXCMD置位期间,TFNF保持复位直到发送FIFO空。</td></tr><tr><td>6</td><td>TC</td><td>发送完成0:发送没有完成1:发送完成。如果USART_CTL0寄存器的TCIE被置位,将会有中断产生。如果一个包含数据的帧的发送完成且TBE或USART_FCS寄存器中TFE位被置位,该位由硬件置位。通过向USART_INTC寄存器的TCC位写1清0。注意:当TEN清零时,TC位被立即置位,传输结束。</td></tr><tr><td rowspan="2">5</td><td>RBNE</td><td>当FIFO模式禁用:读数据缓冲区非空0:没有接收到数据1:已接收到数据并且可以读取。当寄存器USART_CTL0的RBNEIE位被置位,将会有中断产生。当接收移位寄存器的内容已经被转移到寄存器USART_RDATA,由硬件置位。通过读USART。</td></tr><tr><td>RFNE</td><td>当FIFO模式使能:接收FIFO非空0:接收FIFO为空1:接收FIFO非空。当寄存器USART_CTL0的RFNEIE位被置位,将会有中断产生。当接收FIFO非空时,由硬件置位。当接收FIFO为空时,由硬件清零。该位也可以通过RXFCMD置位来清零。</td></tr><tr><td>4</td><td>IDLEF</td><td>空闲线检测标志0: 没检测到空闲线1: 检测到空闲线。如果USART_CTL0寄存器的IDLEIE位置1,将会有中断产生。当检测到空闲线时,通过硬件置位。直到RBNE位置位,否则它不会被再次置位。向USART_INTC寄存器的IDLEC位写1清0。</td></tr><tr><td>3</td><td>ORERR</td><td>溢出错误0: 未检测到溢出错误1: 检测到溢出错误。在多级缓存通信中,如果寄存器USART_CTL0的RBNEIE或RFNEIE位置位,将会引发中断。如果寄存器USART_CTL2的ERRIE位置位也会引发中断。在RBNE或RFF置位的情况下,如果接收移位寄存器的数据传递给USART_RDATA寄存器,将会由硬件置位。向USART_INTC寄存器的OREC位写1清0。</td></tr><tr><td>2</td><td>NERR</td><td>噪声错误标志0: 未检测到噪声错误1: 检测到噪声错误。在多级缓存通信中,如果寄存器USART_CTL2的ERRIE位置位,将会有中断产生。在接收帧的时候检测到噪声错误,将会由硬件置位。向寄存器USART_INTC的NEC位写1清0。注意:当该位与RBNE位或RFNE位同时置位时,将不会产生中断。当FIFO使能时,噪声错误与USART_RDATA中的数据有关。</td></tr><tr><td>1</td><td>FERR</td><td>帧错误0: 未检测到帧错误1: 检测到帧错误或者断开字符。在多级缓存通信中,如果寄存器USART_CTL2的ERRIE位置位,将会有中断产生。当一个不同步,强噪声或者断开字符被检测到时,硬件置位。在智能卡模式下,当发送次数达到上限,仍然没有收到发送成功应答(卡一直响应NACKs),该位也将被置位。向USART_INTC寄存器的FEC位写1清0。注意:当FIFO使能时,噪声错误与USART_RDATA中的数据有关。</td></tr><tr><td>0</td><td>PERR</td><td>校验错误0: 未检测到校验错误1: 检测到校验错误,在多级缓存通信中,如果寄存器USART_CTL0的PERRIE位置位,将会有中断产生。当在接收模式的时候检测到校验错误,将会由硬件置位。向USART_INTC寄存器的PEC位写1清0。注意:当FIFO使能时,噪声错误与USART_RDATA中的数据有关。</td></tr></table>

## 27.4.9. USART 中断标志清除寄存器（USART_INTC）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>WUC</td><td colspan="2">保留</td><td>AMC0</td><td>AMC1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>EBC</td><td>RTC</td><td>保留</td><td>CTSC</td><td>LBDC</td><td>保留</td><td>TCC</td><td>保留</td><td>IDLEC</td><td>OREC</td><td>NEC</td><td>FEC</td><td>PEC</td></tr><tr><td></td><td></td><td></td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td></td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>WUC</td><td>从深度睡眠模式唤醒标志的清除向该位写1清除USART_STAT寄存器的WUF位。在UART3 / UART4中,该位保留。</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>AMC0</td><td>ADDR0中字符匹配标志清除向该位写1清除USART_STAT寄存器的AMF0位。</td></tr><tr><td>16</td><td>AMC1</td><td>ADDR1中字符匹配标志清除向该位写1清除USART_STAT寄存器的AMF1位。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>EBC</td><td>块结束标志清除向该位写1清除USART_STAT寄存器的EBF位。在UART3 / UART4中,该位保留。</td></tr><tr><td>11</td><td>RTC</td><td>接收超时标志清除向该位写1清除USART_STAT寄存器的RTF标志。在UART3 / UART4中,该位保留。</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CTSC</td><td>CTS变化标志清除向该位写1清除USART_STAT寄存器的CTSF位。</td></tr><tr><td>8</td><td>LBDC</td><td>LIN断开字符检测标志清除向该位写1清除USART_STAT寄存器的LBDF标志位。</td></tr></table>

<table><tr><td></td><td></td><td>在UART3 / UART4中,该位保留。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TCC</td><td>发送完成标志清除向该位写1清除USART_STAT寄存器的TC位。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>IDLEC</td><td>空闲线检测标志清除向该位写1清除USART_STAT寄存器的IDLEF位。</td></tr><tr><td>3</td><td>OREC</td><td>溢出标志清除向该位写1清除USART_STAT寄存器的ORERR位。</td></tr><tr><td>2</td><td>NEC</td><td>噪声检测清除向该位写1清除USART_STAT寄存器的NERR位。</td></tr><tr><td>1</td><td>FEC</td><td>帧格式错误标志清除向该位写1清除USART_STAT寄存器的FERR位。</td></tr><tr><td>0</td><td>PEC</td><td>校验错误标志清除向该位写1清除USART_STAT寄存器的PERR位。</td></tr></table>

## 27.4.10. USART 数据接收寄存器（USART_RDATA）

地址偏移：0x24

复位值：未定义

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">RDATA[9:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>RDATA[9:0]</td><td>接收数据的值包含接收到的数据字节如果接收到的数据打开了奇偶校验位(USART_CTL0寄存器的PCEN置1),那么接收到的数据的最高位(第6位、7位、8位或9位,取决于数据的长度)是奇偶校验位。</td></tr></table>

## 27.4.11. USART 数据发送寄存器（USART_TDATA）

地址偏移：0x28

复位值：未定义

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TDATA[9:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TDATA[9:0]</td><td>发送数据的值包含发送的数据字节如果发送到的数据打开了奇偶校验位(USART_CTL0寄存器的PCEN置1),那么发送的数据的最高位(第6位、7位、8位或9位取决于数据的长度)将会被奇偶校验位替代。只有当USART_STAT寄存器的TBE位被置位时,这个寄存器才可以改写。</td></tr></table>

## 27.4.12. USART 兼容性控制寄存器（USART_CHC）

地址偏移：0xC0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>EPERR</td><td colspan="7">保留</td><td>HCM</td></tr><tr><td colspan="15">rc_w0</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EPERR</td><td>校验错误超前检测标志。在RBNE置位前，校验位被检测到时该标志置位。软件写0可以清除该位。</td></tr><tr><td></td><td></td><td>0: 没有检测到校验错误</td></tr><tr><td></td><td></td><td>1: 检测到校验错误</td></tr><tr><td>7:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>HCM</td><td>硬件流控制兼容性模式</td></tr><tr><td></td><td></td><td>0: nRTS信号等于RBNE状态寄存器</td></tr><tr><td></td><td></td><td>1: 当最后一个数据位(PCE置位时的奇偶位)被采样时,nRTS信号置位</td></tr></table>

## 27.4.13. USART FIFO 控制和状态寄存器（USART_FCS）

地址偏移：0xD0

复位值：0x0300 0400

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TFEIE</td><td>保留</td><td>TFTIE</td><td>保留</td><td>RFTIE</td><td>TFEC</td><td>TFTIF</td><td>TFEIF</td><td>保留</td><td>RFTIF</td><td colspan="3">TFTCFG[2:0]</td><td colspan="3">RFTCFG[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td></td><td>rc_w0</td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RFFIF</td><td colspan="3">RFCNT[2:0]</td><td>RFF</td><td>RFE</td><td>RFFIE</td><td>FEN</td><td>TFF</td><td>TFE</td><td>TFT</td><td>RFT</td><td>保留</td><td colspan="2">RFCNT[4:3]</td><td>ELNACK</td></tr><tr><td>rc_w0</td><td colspan="3">r</td><td>r</td><td>r</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td colspan="2">r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TFEIE</td><td>发送FIFO空中断使能如果该位置位,当TFE位置位时,中断发生。0:禁止发送FIFO空中断1:使能发送FIFO空中断</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>TFTIE</td><td>发送FIFO到达阈值中断使能如果该位置位,当发送FIFO中的可用空间到达TFTCFG[2:0]配置的阈值时,中断发生。0:禁止发送FIFO到达阈值中断1:使能发送FIFO到达阈值中断</td></tr><tr><td>28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>RFTIE</td><td>接收FIFO到达阈值中断使能如果该位置位,当发送FIFO到达RFTCFG[2:0]配置的阈值时,中断发生。0:禁止接收FIFO到达阈值中断1:使能接收FIFO到达阈值中断</td></tr><tr><td>26</td><td>TFEC</td><td>发送FIFO空标志清除写1清除TFE标志</td></tr><tr><td>25</td><td>TFTIF</td><td>发送FIFO到达阈值中断标志当TFTIE位置位时,该位有效。0:发送FIFO中的可用空间未到达可编程阈值1:发送FIFO中的可用空间到达可编程阈值中断标志。当TFTIE置位时,中断发生。当发送FIFO中的可用空间TFTCFG[2:0]配置的阈值时,由硬件置位。</td></tr><tr><td>24</td><td>TFEIF</td><td>发送FIFO空中断标志当TFEIE置位时,该位有效。0:发送FIF非空1:发送FIFO为空中断标志</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>RFTIF</td><td>接收FIFO到达阈值中断标志当RFTIE位置位时,该位有效。0:接收FIFO到达可编程阈值1:接收FIFO到达可编程阈值中断标志</td></tr><tr><td>21:19</td><td>TFTCFG[2:0]</td><td>发送FIFO阈值配置000:发送FIFO到达FIFO深度的1/8001:发送FIFO到达FIFO深度的1/4010:发送FIFO到达FIFO深度的1/2011:发送FIFO到达FIFO深度的3/4100:发送FIFO到达FIFO深度的7/8101:发送FIFO为空11x:保留</td></tr><tr><td>18:16</td><td>RFTCFG[2:0]</td><td>接收FIFO阈值配置000:接收FIFO到达FIFO深度的1/8001:接收FIFO到达FIFO深度的1/4010:接收FIFO到达FIFO深度的1/2011:接收FIFO到达FIFO深度的3/4100:接收FIFO到达FIFO深度的7/8101:接收FIFO为满11x:保留</td></tr><tr><td>15</td><td>RFFIF</td><td>接收FIFO满中断标志当RFFIE置位时,该位有效。0:接收FIFO非满</td></tr><tr><td>14:12</td><td>RFCNT[2:0]</td><td>接收FIFO计数值该位域与RFCNT[4:3]位域决定接收FIFO计数值。</td></tr><tr><td>11</td><td>RFF</td><td>接收FIFO满标志0:接收FIFO不为满1:接收FIFO满。当RFFIE置位时,中断发生。当接收数据个数为RXFIFO大小加1时,由硬件置1。</td></tr><tr><td>10</td><td>RFE</td><td>接收FIFO空标志0:接收FIFO不为空1:接收FIFO空</td></tr><tr><td>9</td><td>RFFIE</td><td>接收FIFO满中断使能如果该位置位,当RFF位置位时,中断发生。0:禁止接收FIFO满中断1:使能接收FIFO满中断</td></tr><tr><td>8</td><td>FEN</td><td>FIFO使能0:禁止使用FIFO1:使能FIFO当USART被使能(UEN=1)时,该位域不能被改写。注意:当接收或发送数据未完成时,不要改变该位。当UEN位清零且不改变该位,在重配UEN位时,如果之前FIFO的值不在需要,需要先刷新FIFO。</td></tr><tr><td>7</td><td>TFF</td><td>发送FIFO满标志0:发送FIFO不为满1:发送FIFO满。</td></tr><tr><td>6</td><td>TFE</td><td>发送FIFO空标志0:发送FIFO不为空1:发送FIFO空。当TFEIE置位时,中断发生。当发送FIFO为空时,由硬件置位。当发送FIFO中只少有一个数据时,由硬件清0。向USART_CMD寄存器的TXFCMD位写1时,由硬件置位</td></tr><tr><td>5</td><td>TFT</td><td>发送FIFO阈值标志0:发送FIFO中的可用空间到达可编程阈值1:发送FIFO中的可用空间未到达可编程阈值。当发送FIFO中的可用空间到达TFTCFG[2:0]配置的阈值时,由硬件复位。</td></tr><tr><td>4</td><td>RFT</td><td>接收FIFO阈值标志0:接收FIFO未到达可编程阈值1:接收FIFO到达可编程阈值。当RFTIE置位时,中断发生。当接收FIFO到达RFTCFG[2:0]配置的阈值时,由硬件置1。这意味着接收FIFO中有RFTCFG[2:0] -1个数据,USART_RDATA寄存器中有一个数据。注意:当RTFCFG[2:0]=0b101且接收到16个数据时,RFT被置位。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:1</td><td>RFCNT[4:3]</td><td>接收FIFO计数值该位域与RFCNT[2:0]位域决定接收FIFO计数值。</td></tr><tr><td>0</td><td>ELNACK</td><td>若选择了智能卡模式,提前NACK如果检测到校验位错误,NACK脉冲提前1/16位的时间。0:若选择了智能卡模式,禁止提前NACK1:若选择了智能卡模式,使能提前NACK在UART3 / UART4中,该位保留。</td></tr></table>
