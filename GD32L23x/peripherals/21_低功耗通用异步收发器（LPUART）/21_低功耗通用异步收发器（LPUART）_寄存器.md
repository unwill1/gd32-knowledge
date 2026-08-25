## 21.4. LPUART 寄存器

GD32L233xx 产品

LPUART0基地址：0x4000 8000

GD32L235xx 产品

LPUART0基地址：0x4000 8000

LPUART1基地址：0x4000 4800

## 21.4.1. LPUART 控制寄存器 0（LPUART_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>WL1</td><td colspan="2">保留</td><td colspan="5">DEA[4:0]</td><td colspan="5">DED[4:0]</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>AMIE</td><td>MEN</td><td>WLO</td><td>WM</td><td>PCEN</td><td>PM</td><td>PERRIE</td><td>TBEIE</td><td>TCIE</td><td>RBNEIE</td><td>IDLEIE</td><td>TEN</td><td>REN</td><td>UESM</td><td>UEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>WL1</td><td>字长该位与WL0位决定字长WL[1:0] = 00, 8数据位WL[1:0] = 01, 9数据位WL[1:0] = 10, 7数据位WL[1:0] = 11, 7数据位当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>27:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:21</td><td>DEA[4:0]</td><td>驱动使能置位时间这些数字用来定义DE(驱动使能)信号的置位与第一个字节的起始位之间的时间间隔。它通过LPUART CLK来表示。当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>20:16</td><td>DED[4:0]</td><td>驱动使能置低时间这些位用来定义一个发送信息最后一个字节的停止位与置低DE(驱动使能)信号之间的时间间隔。它通过LPUART CLK来表示。当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>AMIE</td><td>ADDR字符匹配中断使能0:ADDR字符匹配中断禁用1:ADDR字符匹配中断使能</td></tr><tr><td>13</td><td>MEN</td><td>静默模式使能0:静默模式禁用1:静默模式被使能</td></tr><tr><td>12</td><td>WLO</td><td>字长该位与WL1位决定字长WL[1:0] = 00,8数据位WL[1:0] = 01,9数据位WL[1:0] = 10,7数据位WL[1:0] = 11,7数据位当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>WM</td><td>从静默模式唤醒方法0:空闲线1:地址标记当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>10</td><td>PCEN</td><td>校验控制使能0:校验控制禁用1:校验控制被使能当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>9</td><td>PM</td><td>校验模式0:偶校验1:奇校验当LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>PERRIE</td><td>校验错误中断使能0:校验错误中断禁用1:当LPUART_STAT寄存器的PERR位置位时,将触发中断。</td></tr><tr><td>7</td><td>TBEIE</td><td>发送寄存器空中断使能0:中断禁止1:当LPUART_STAT寄存器的TBE位置位时,将触发中断。</td></tr><tr><td>6</td><td>TCIE</td><td>发送完成中断使能如果该位置1,LPUART_STAT寄存器中TC被置位时产生中断。0:发送完成中断禁用1:发送完成中断使能</td></tr><tr><td>5</td><td>RBNEIE</td><td>读数据缓冲区非空中断和过载错误中断使能0:读数据缓冲区非空中断和过载错误中断禁用1:当LPUART_STAT寄存器的ORERR或RBNE位置位时,将触发中断。</td></tr><tr><td>4</td><td>IDLEIE</td><td>IDLE线检测中断使能0: IDLE线检测中断禁用1: 当LPUART_STAT寄存器的IDLEF位置位时,将触发中断。</td></tr><tr><td>3</td><td>TEN</td><td>发送器使能0: 发送器关闭1: 发送器打开</td></tr><tr><td>2</td><td>REN</td><td>接收器使能0: 接收器关闭1: 接收器打开并且开始搜索起始位。</td></tr><tr><td>1</td><td>UESM</td><td>LPUART在深度睡眠模式下使能0: LPUART不能从深度睡眠模式唤醒MCU1: LPUART能从深度睡眠模式唤醒MCU。条件是LPUART的时钟源必须是IRC16M或LXTAL。</td></tr><tr><td>0</td><td>UEN</td><td>LPUART使能0: LPUART预分频器和输出禁用1: LPUART预分频器和输出被使能</td></tr></table>

## 21.4.2. LPUART 控制寄存器 1（LPUART_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ADDR[7:0]</td><td colspan="4">保留</td><td>MSBF</td><td>DINV</td><td>TINV</td><td>RINV</td></tr><tr><td colspan="12">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STRP</td><td>保留</td><td colspan="2">STB[1:0]</td><td colspan="7">保留</td><td>ADDM</td><td colspan="4">保留</td></tr><tr><td>rw</td><td colspan="7">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ADDR[7:0]</td><td>LPUART的节点地址这些位给出LPUART的节点地址。在多处理器通信并且静默模式或者深度睡眠模式期间,这些位用来唤醒进行地址标记的检测。接收到的最高位为1的数据帧将和这些位进行比较。当ADDM位被清零时,仅仅ADDR[3:0]被用来比较。在正常的接收期间,这些位也用来进行字符检测。所有接收到的字符(8位)与ADDR[7:0]的值进行比较,如果匹配,AMF标志将被置位。当接收器(REN=1)和LPUART(UEN=1)被使能时,该位域不能被改写。</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>MSBF</td><td>高位在前0:数据发送/接收,采用低位在前1:数据发送/接收,采用高位在前LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>18</td><td>DINV</td><td>数据位反转0:数据位信号值没有反转1:数据位信号值被反转LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>17</td><td>TINV</td><td>TX管脚电平反转0:TX管脚信号值没有反转1:TX管脚信号值被反转.LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>16</td><td>RINV</td><td>RX管脚电平反转0:RX管脚信号值没有反转.1:RX管脚信号值被反转LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>15</td><td>STRP</td><td>交换TX/RX管脚0:TX和RX管脚功能不被交换1:TX和RX管脚功能被交换当LPUART被使能(UEN=1)时,该位域不能改写。</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>STB[1:0]</td><td>STOP位长00~01:1停止位10~11:2停止位LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>ADDM</td><td>地址检测模式该位用来选择4位地址检测或全位地址检测。0:4位地址检测1:全位地址检测。在7位,8位和9位数据模式下,地址检测分别按6位,7位和8位地址(ADDR[5:0],ADDR[6:0]和ADDR[7:0])执行。LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 21.4.3. LPUART 控制寄存器 2（LPUART_CTL2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td colspan="8">保留</td><td>UCESM</td><td>WUIE</td><td>WUM[1:0]</td><td colspan="4">保留</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DEP</td><td>DEM</td><td>DDRE</td><td>OVRD</td><td>保留</td><td>CTSIE</td><td>CTSEN</td><td>RTSEN</td><td>DENT</td><td>DENR</td><td colspan="2">保留</td><td>HDEN</td><td colspan="2">保留</td><td>ERRIE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>UCESM</td><td>Deep-sleep模式下LPUART时钟使能0: Deep-sleep模式下LPUART时钟失能1: Deep-sleep模式下LPUART时钟使能</td></tr><tr><td>22</td><td>WUIE</td><td>从深度睡眠模式唤醒中断使能0: 从深度睡眠模式唤醒中断禁用1: 从深度睡眠模式唤醒中断被使能</td></tr><tr><td>21:20</td><td>WUM[1:0]</td><td>从深度睡眠模式唤醒模式这个位域指定什么事件可以置位LPUART_STAT寄存器中的WUF(从深度睡眠唤醒标志)标志。00: WUF在地址匹配的时候置位。如何实现地址匹配在ADDR和ADDM中定义。01: 保留10: WUF在检测到起始位时置位11: WUF在检测到RBNE时置位LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>DEP</td><td>驱动使能的极性选择模式0: DE信号高有效1: DE信号低有效LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>14</td><td>DEM</td><td>驱动使能模式用户使能该位以后,可以通过DE信号对外部收发器进行控制。DE信号是从RTS管脚输出的。0: DE功能禁用1: DE功能开启LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>13</td><td>DDRE</td><td>在接收错误时禁止DMA0: 在发生接收错误的情况下,不禁用DMA。所有的错误数据不会产生DMA请求,以确保错误的数据不会被传输,但是下一个接收到的正确的数据会被传输。RBNE位保持0以阻止过载错误,但是相应错误标志位会被置位。1: 在接收错误的情况下,DMA被关闭。DMA请求会被屏蔽,直到相应的标志位被清0。RBNE标志和相应的错误标志位会被置位。软件在清除错误标志前,必须首先关DMA请求(DMAR = 0)或清RBNE。LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>12</td><td>OVRD</td><td>溢出禁止0:溢出功能被使能。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将被置位,并且新数据将会丢失。1:溢出功能禁止。当接收到的数据在新数据到达前没有被读走,ORERR错误标志位将不会被置位,新数据会将LPUART_RDATA寄存器以前的内容覆盖。LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CTSIE</td><td>CTS中断使能0:CTS中断屏蔽1:当LPUART_STAT的CTS位置位时,会产生中断。</td></tr><tr><td>9</td><td>CTSEN</td><td>CTS使能0:CTS硬件流控禁用1:CTS硬件流控被使能LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>8</td><td>RTSEN</td><td>RTS使能0:RTS硬件流控禁用1:RTS硬件流控被使能,只有当接收缓冲区有空间的时候,才会请求下一个数据。LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>7</td><td>DENT</td><td>DMA发送使能0:关闭DMA发送模式1:开启DMA发送模式</td></tr><tr><td>6</td><td>DENR</td><td>DMA接收使能0:关闭DMA接收模式1:开启DMA接收模式</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>HDEN</td><td>半双工使能0:禁用半双工模式1:开启半双工模式LPUART被使能(UEN=1)时,该位域不能被改写。</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>ERRIE</td><td>多级缓存通信模式的错误中断使能0:禁用错误中断1:在多级缓存通信时,当LPUART_STAT寄存器的FERR位,ORERR位或NERR位被置位时,会产生中断。</td></tr></table>

## 21.4.4. LPUART 波特率寄存器（LPUART_BAUD）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

当LPUART（UEN=1）被使能时，该寄存器不能被改写。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">BRR[19:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BRR[15:8]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:0</td><td>BRR[19:0]</td><td>LPUARTDIV的值注意:<eq>BRR[19:0] \geq 0x300</eq>并且(3x波特率)<eq>\leq LPUCLK \leq (4096x波特率)</eq>。</td></tr></table>

## 21.4.5. LPUART 请求寄存器（LPUART_CMD）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>RXFCMD</td><td>MMCMD</td><td colspan="2">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>RXFCMD</td><td>接收数据清空请求向该位写1来清除RBNE标志位,以丢弃未读的接收数据。</td></tr><tr><td>2</td><td>MMCMD</td><td>静默模式请求向该位写1使LPUART进入静默模式并且置位RWU标志位。</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 21.4.6. LPUART 状态寄存器（LPUART_STAT）

地址偏移：0x1C

复位值：0x0000 00C0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>REA</td><td>TEA</td><td>WUF</td><td>RWU</td><td>保留</td><td>AMF</td><td>BSY</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td>保留</td><td></td><td></td><td>CTS</td><td>CTSF</td><td>保留</td><td>TBE</td><td>TC</td><td>RBNE</td><td>IDLEF</td><td>ORERR</td><td>NERR</td><td>FERR</td><td>PERR</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>REA</td><td>接收使能通知标志这位反映了LPUART核心逻辑的接收使能状态,该位可以通过硬件设置。0:LPUART核心接收逻辑禁用1:LPUART核心接收逻辑被使能</td></tr><tr><td>21</td><td>TEA</td><td>发送使能通知标志该位反映了LPUART核心逻辑的发送使能状态,该位可以通过硬件设置。0:LPUART核心发送逻辑禁用1:LPUART核心发送逻辑被使能</td></tr><tr><td>20</td><td>WUF</td><td>从深度睡眠模式唤醒标志0:没有从深度睡眠模式唤醒1:已从深度睡眠模式唤醒,如果在LPUART_CTL2寄存器的WUFIE=1并且MCU处于深度睡眠模式,将引发一个中断。当检测到一个唤醒事件时,该位通过硬件置位,这个事件在WUM位域被定义。向LPUART_INTC寄存器中的WUC写1,该位被清0。当UESM被清0时,该位清0。</td></tr><tr><td>19</td><td>RWU</td><td>接收器从静默模式唤醒该位表示LPUART处于静默模式。0:接收器在工作状态1:接收器在静默状态当在唤醒和静默模式切换时,它通过硬件清0或者置1。静默模式控制(地址帧还是空闲帧)是用通过LPUART_CTL0寄存器的WM位选择。如果选择空闲信号唤醒,只能通过向LPUART_CMD寄存器的MMCMD位写1来将该位置位。</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>AMF</td><td>ADDR匹配标志0:ADDR和接收到的字符不匹配1:ADDR和接收到的字符匹配,如果LPUART_CTL0寄存器的AMIE=1,将引发一个中断。当接收到ADDR[7:0]中定义的字符时,硬件置位。通过向LPUART_INTC寄存器的AMC写1清0。</td></tr><tr><td>16</td><td>BSY</td><td>忙标志0:LPUART处于空闲1: LPUART正在接收</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CTS</td><td>CTS电平这个值等于nCTS输入引脚电平的反向拷贝。0: nCTS输入引脚高电平1: nCTS输入引脚低电平</td></tr><tr><td>9</td><td>CTSF</td><td>CTS变化标志0: nCTS状态线没有变化1: nCTS状态线发生变化,如果LPUART_CTL2寄存器的CTSIE位置位,将引发中断。当nCTS输入变化时,由硬件置位。通过向LPUART_INTC寄存器的CTSC位写1,清零该位。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TBE</td><td>发送数据寄存器空0: 数据没有发送到移位寄存器1: 数据发送到移位寄存器。如果LPUART_CTL0寄存器的TBEIE位置位,将会有中断产生。当LPUART_TDATA寄存器的内容已经被转移到移位寄存器时,由硬件置位。通过向LPUART_TDATA寄存器中写数据来清0。</td></tr><tr><td>6</td><td>TC</td><td>发送完成0: 发送没有完成1: 发送完成。如果LPUART_CTL0寄存器的TCIE被置位,将会有中断产生。如果一个包含数据的帧的发送完成且TBE被置位,该位由硬件置位。通过向LPUART_INTC寄存器的TCC位写1清0。</td></tr><tr><td>5</td><td>RBNE</td><td>读数据缓冲区非空0: 没有接收到数据1: 已接收到数据并且可以读取。当寄存器LPUART_CTL0的RBNEIE位被置位,将会有中断产生。当接收移位寄存器的内容已经被转移到寄存器LPUART_RDATA,由硬件置位。通过读LPUART_RDATA寄存器或向LPUART_CMD寄存器的RXFCMD位写1清0。</td></tr><tr><td>4</td><td>IDLEF</td><td>空闲线检测标志0: 没检测到空闲线1: 检测到空闲线。如果LPUART_CTL0寄存器的IDLEIE位置1,将会有中断产生。当检测到空闲线时,通过硬件置位。直到RBNE位置位,否则它不会被再次置位。向LPUART_INTC寄存器的IDLEC位写1清0。</td></tr><tr><td>3</td><td>ORERR</td><td>溢出错误0: 未检测到溢出错误1: 检测到溢出错误。在多级缓存通信中,如果寄存器LPUART_CTL0的RBNEIE位置位,将会引发中断。如果寄存器LPUART_CTL2的ERRIE位置位也会引发中断。在RBNE置位的情况下,如果接收移位寄存器的数据传递给LPUART_RDATA寄存器,将会由硬件置位。向LPUART_INTC寄存器的OREC位写1清0。</td></tr><tr><td>2</td><td>NERR</td><td>噪声错误标志0:未检测到噪声错误1:检测到噪声错误。在多级缓存通信中,如果寄存器LPUART_CTL2的ERRIE位置位,将会有中断产生。在接收帧的时候检测到噪声错误,将会由硬件置位。向寄存器LPUART_INTC的NEC位写1清0。</td></tr><tr><td>1</td><td>FERR</td><td>帧错误0:未检测到帧错误1:检测到帧错误或者断开字符。在多级缓存通信中,如果寄存器LPUART_CTL2的ERRIE位置位,将会有中断产生。当一个不同步,强噪声或者断开字符被检测到时,硬件置位。在智能卡模式下,当发送次数达到上限,仍然没有收到发送成功应答(卡一直响应NACKs),该位也将被置位。向LPUART_INTC寄存器的FEC位写1清0。</td></tr><tr><td>0</td><td>PERR</td><td>校验错误0:未检测到校验错误1:检测到校验错误,在多级缓存通信中,如果寄存器LPUART_CTL0的PERRIE位置位,将会有中断产生。当在接收模式的时候检测到校验错误,将会由硬件置位。向LPUART_INTC寄存器的PEC位写1清0。</td></tr></table>

## 21.4.7. LPUART 中断标志清除寄存器（LPUART_INTC）

地址偏移：0x20

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>WUC</td><td colspan="2">保留</td><td>AMC</td><td>保留</td></tr><tr><td colspan="14">w</td><td>w</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CTSC</td><td colspan="2">保留</td><td>TCC</td><td>保留</td><td>IDLEC</td><td>OREC</td><td>NEC</td><td>FEC</td><td>PEC</td></tr><tr><td colspan="9">w</td><td colspan="2">w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>WUC</td><td>从深度睡眠模式唤醒标志的清除向该位写1清除LPUART_STAT寄存器的WUF位。</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>AMC</td><td>ADDR匹配标志清除</td></tr></table>

<table><tr><td></td><td></td><td>向该位写1清除LPUART_STAT寄存器的AMF位。</td></tr><tr><td>16:110</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CTSC</td><td>CTS变化标志清除向该位写1清除LPUART_STAT寄存器的CTSF位。</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TCC</td><td>发送完成标志清除向该位写1清除LPUART_STAT寄存器的TC位。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>IDLEC</td><td>空闲线检测标志清除向该位写1清除LPUART_STAT寄存器的IDLEF位。</td></tr><tr><td>3</td><td>OREC</td><td>溢出标志清除向该位写1清除LPUART_STAT寄存器的ORERR位。</td></tr><tr><td>2</td><td>NEC</td><td>噪声检测清除向该位写1清除LPUART_STAT寄存器的NERR位。</td></tr><tr><td>1</td><td>FEC</td><td>帧格式错误标志清除向该位写1清除LPUART_STAT寄存器的FERR位。</td></tr><tr><td>0</td><td>PEC</td><td>校验错误标志清除向该位写1清除LPUART_STAT寄存器的PERR位。</td></tr></table>

## 21.4.8. LPUART 数据接收寄存器（LPUART_RDATA）

地址偏移：0x24

复位值：未定义

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">RDATA[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>RDATA[8:0]</td><td>接收数据的值包含接收到的数据字节如果接收到的数据打开了奇偶校验位(LPUART_CTL0寄存器的PCEN置1),那么接收到的数据的最高位(第7位或8位,取决于数据的长度)是奇偶校验位。</td></tr></table>

## 21.4.9. LPUART 数据发送寄存器（LPUART_TDATA）

地址偏移：0x28

复位值：未定义

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">TDATA[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>TDATA[8:0]</td><td>发送数据的值包含发送的数据字节如果发送到的数据打开了奇偶校验位(LPUART_CTL0寄存器的PCEN置1),那么发送的数据的最高位(第7位或8位取决于数据的长度)将会被奇偶校验位替代。只有当LPUART_STAT寄存器的TBE位被置位时,这个寄存器才可以改写。</td></tr></table>

## 21.4.10. LPUART 兼容性控制寄存器（LPUART_CHC）

地址偏移：0xC0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>EPERR</td><td colspan="7">保留</td><td>HCM</td></tr><tr><td colspan="15">rc_w0</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EPERR</td><td>校验错误超前检测标志。在RBNE置位前,校验位被检测到时该标志置位。软件写0可以清除该位。0:没有检测到校验错误1:检测到校验错误</td></tr><tr><td>7:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>HCM</td><td>硬件流控制兼容性模式</td></tr></table>

## 0：nRTS信号等于RBNE状态寄存器

1：当最后一个数据位（PCE置位时的奇偶位）被采样时，nRTS信号置位
