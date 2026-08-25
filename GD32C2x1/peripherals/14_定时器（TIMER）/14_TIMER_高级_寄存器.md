## 14.1.5. TIMERx 寄存器（x=0）

TIMER0基地址：0x4001 2C00

控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="2">CAM[1:0]</td><td>DIR</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(CK_TIMER)与死区时间和数字滤波器采样时钟(DTS)之间的分频系数。00:<eq>f_{DTS}=f_{CK\_TIMER}</eq>01:<eq>f_{DTS}=f_{CK\_TIMER}/2</eq>10:<eq>f_{DTS}=f_{CK\_TIMER}/4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:5</td><td>CAM[1:0]</td><td>计数器对齐模式选择00:无中央对齐模式(边沿对齐模式)。DIR 位指定了计数方向。01:中央对齐向下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),只有在向下计数时,通道的比较中断标志置 1。10:中央对齐向上计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),只有在向上计数时,通道的比较中断标志置 1。11:中央对齐上下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),在向上和向下计数时,通道的比较中断标志都会置 1当计数器使能以后,该位不能从 0x00 切换到非 0x00.</td></tr><tr><td>4</td><td>DIR</td><td>方向0:向上计数1:向下计数当计数器配置为中央对齐模式或正交译码器模式时,该位为只读。</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0:单脉冲模式禁能,更新事件发生后,计数器继续计数。1:单脉冲模式使能,在下一次更新事件发生时,计数器停止计数。</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该位,选择更新事件源。0:使能后,下述任一事件产生更新中断或DMA请求:-UPG位被置1;-计数器溢出/下溢;-复位模式产生的更新。1:使能后只有计数器溢出/下溢才产生更新中断或DMA请求</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新。该位用来使能或禁能更新事件的产生。0:更新事件使能。当以下事件之一发生时,更新事件产生,具有缓存的寄存器被装入它们的预装载值:-UPG位被置1;-计数器溢出/下溢;-复位模式产生一个更新事件。1:更新事件禁能。带有缓存的寄存器保持原有值,如果UPG位被置1或者复位模式产生一个硬件复位事件,计数器和预分频器被重新初始化。</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0:计数器禁能1:计数器使能在软件将CEN位置1后,外部时钟、暂停模式和正交译码器模式才能工作。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>ISO3</td><td>ISO2N</td><td>ISO2</td><td>ISO1N</td><td>ISO1</td><td>ISO0N</td><td>ISO0</td><td>TI0S</td><td colspan="3">MMC[2:0]</td><td>DMAS</td><td>CCUC</td><td>保留</td><td>CCSE</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:15</td><td colspan="3">保留</td><td colspan="12">必须保持复位值</td></tr><tr><td>14</td><td colspan="3">ISO3</td><td colspan="12">通道3的空闲状态输出参考 ISO0 位</td></tr><tr><td>13</td><td colspan="3">ISO2N</td><td colspan="12">通道 2 的互补通道空闲状态输出参考 ISO0N 位</td></tr><tr><td>12</td><td colspan="3">ISO2</td><td colspan="12">通道 2 的空闲状态输出参考 ISO0 位</td></tr><tr><td>11</td><td colspan="3">ISO1N</td><td colspan="12">通道 1 的互补通道空闲状态输出参考 ISO0N 位</td></tr><tr><td>10</td><td colspan="3">ISO1</td><td colspan="12">通道 1 的空闲状态输出参考 ISO0 位</td></tr><tr><td>9</td><td colspan="3">ISO0N</td><td colspan="12">通道 0 的互补通道空闲状态输出0:当 POEN 位复位时,CH0_ON 设置低电平1:当 POEN 位复位时,CH0_ON 设置高电平此位只有在 TIMERx_CCHP 寄存器的 PROT[1:0]位为 00 的时候可以被更改。</td></tr><tr><td>8</td><td colspan="3">ISO0</td><td colspan="12">通道 0 的空闲状态输出0:当 POEN 位复位时,CH0_O 设置低电平1:当 POEN 位复位时,CH0_O 设置高电平如果 CH0_ON 生效,一个死区时间后 CH0_O 输出改变。此位只有在 TIMERx_CCHP 寄存器的 PROT[1:0]位为 00 的时候可以被更改。</td></tr><tr><td>7</td><td colspan="3">TIOS</td><td colspan="12">通道 0 触发输入选择0:选择 TIMERx_CH0 引脚作为通道 0 的触发输入1:选择 TIMERx_CH0,TIMERx_CH1 和 TIMERx_CH2 引脚异或的结果作为通道 0 的触发输入</td></tr><tr><td>6:4</td><td colspan="3">MMC[2:0]</td><td colspan="12">主模式控制这些位控制 TRGO 信号的选择,TRGO 信号由主定时器发给从定时器用于同步功能。000:复位。TIMERx_SWEVG 寄存器的 UPG 位被置 1 或从模式控制器产生复位时,触发一次 TRGO 脉冲,后一种情况下,TRGO 上的信号相对实际的复位会有一个延迟。001:使能。此模式可用于同时启动多个定时器或控制在一段时间内使能从定时器。主模式控制器选择计数器使能信号作为触发输出 TRGO。当 CEN 控制位被置 1 或者暂停模式下触发输入为高电平时,计数器使能信号被置 1。在暂停模式下,计数器使能信号受控于触发输入,在触发输入和 TRGO 上会有一个延迟,除非选择了主/从模式。010:更新。主模式控制器选择更新事件作为 TRGO。011:捕获/比较脉冲。通道 0 在发生一次捕获或一次比较成功时,主模式控制器产生一个 TRGO 脉冲。100:比较。在这种模式下,主模式控制器选择 O0CPRE 信号作为触发输出 TRGO。101:比较。在这种模式下,主模式控制器选择 O1CPRE 信号作为触发输出 TRGO。110:比较。在这种模式下,主模式控制器选择 O2CPRE 信号作为触发输出 TRGO。111:比较。在这种模式下,主模式控制器选择 O3CPRE 信号作为触发输出 TRGO。</td></tr><tr><td>3</td><td colspan="3">DMAS</td><td colspan="12">DMA 请求源选择0:当通道捕获/比较事件发生时,发送通道x的DMA请求1:当更新事件发生,发送通道x的DMA请求</td></tr><tr><td>2</td><td colspan="3">CCUC</td><td colspan="12">换相控制影子寄存器更新控制当换相控制影子寄存器(CHxEN,CHxNEN和CHxCOMCTL位)使能(CCSE=1),这些影子寄存器更新控制如下:0:CMTG位被置1时,更新影子寄存器1:当CMTG位被置1或检测到TRIGI上升沿时,影子寄存器更新当通道没有互补输出时,此位无效。</td></tr><tr><td>1</td><td colspan="3">保留</td><td colspan="12">必须保持复位值</td></tr><tr><td>0</td><td colspan="3">CCSE</td><td colspan="12">换相控制影子使能0:影子寄存器(CHxEN,CHxNEN和CHxCOMCTL位)禁能1:影子寄存器(CHxEN,CHxNEN和CHxCOMCTL位)使能如果这些位已经被写入了,换相事件到来时这些位才被更新。当通道没有互补输出时,此位无效。</td></tr></table>

## 从模式配置寄存器（TIMERx_SMCFG）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ETP</td><td>SMC1</td><td colspan="2">ETPSC[1:0]</td><td colspan="4">ETFC[3:0]</td><td>MSM</td><td colspan="7">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15</td><td>ETP</td><td>外部触发极性该位指定 ETI 信号的极性0: ETI 高电平或上升沿有效1: ETI 低电平或下降沿有效</td></tr><tr><td>14</td><td>SMC1</td><td>SMC 的一部分使能外部时钟模式 1在外部时钟模式 1,计数器由 ETIFP 信号上的任意有效边沿驱动0: 外部时钟模式 1 禁能1: 外部时钟模式 1 使能复位模式,暂停模式和事件模式可以与外部时钟模式 1 同时使用。但是不能将 TRGS 设为 3&#x27;b111。如果同时使能外部时钟模式 0 和外部时钟模式 1,外部时钟的输入是 ETIFP。</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2">注意:外部时钟模式0使能在寄存器的SMC位域。</td></tr><tr><td>13:12</td><td>ETPSC[1:0]</td><td colspan="2">外部触发预分频外部触发信号ETIFP的频率不能超过TIMER_CK频率的1/4。当输入较快的外部时钟时,可以使用预分频降低ETIFP的频率。00:预分频禁能01:ETIFP频率被2分频10:ETIFP频率被4分频11:ETIFP频率被8分频</td></tr><tr><td rowspan="18">11:8</td><td rowspan="18">ETFC[3:0]</td><td colspan="2">外部触发滤波控制外部触发信号可以通过数字滤波器进行滤波,该位域定义了数字滤波器的滤波能力。数字滤波器的基本原理是:以<eq>f_{SAMP}</eq>频率连续采样外部触发信号,同时记录采样相同电平的次数。当该次数达到配置的滤波能力时,则认为是一个有效的电平信号。</td></tr><tr><td>EXTFC[3:0]</td><td>次数<eq>f_{SAMP}</eq></td></tr><tr><td>4&#x27;b0000</td><td>Filter disabled.</td></tr><tr><td>4&#x27;b0001</td><td>2<eq>f_{TIMER\_CK}</eq></td></tr><tr><td>4&#x27;b0010</td><td>4</td></tr><tr><td>4&#x27;b0011</td><td>8</td></tr><tr><td>4&#x27;b0100</td><td>6<eq>f_{DTS\_CK}/2</eq></td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6<eq>f_{DTS\_CK}/4</eq></td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6<eq>f_{DTS\_CK}/8</eq></td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5<eq>f_{DTS\_CK}/16</eq></td></tr><tr><td>4&#x27;b1011</td><td>6</td></tr><tr><td>4&#x27;b1100</td><td>8</td></tr><tr><td>4&#x27;b1101</td><td>5<eq>f_{DTS\_CK}/32</eq></td></tr><tr><td>4&#x27;b1110</td><td>6</td></tr><tr><td>4&#x27;b1111</td><td>8</td></tr><tr><td>7</td><td>MSM</td><td colspan="2">主-从模式该位用来同步被选择的定时器同时开始计数。TRGI用做启动事件,通过TRGO,定时器被连接在一起。0:主从模式禁能1:主从模式使能</td></tr><tr><td>6:0</td><td>保留</td><td colspan="2">必须保持复位值.</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>TRGDEN</td><td>CMTDEN</td><td>CH3DEN</td><td>CH2DEN</td><td>CH1DEN</td><td>CH0DEN</td><td>UPDEN</td><td>BRKIE</td><td>TRGIE</td><td>CMTIE</td><td>CH3IE</td><td>CH2IE</td><td>CH1IE</td><td>CH0IE</td><td>UPIE</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>TRGDEN</td><td>触发DMA请求使能0:禁止触发DMA请求1:使能触发DMA请求</td></tr><tr><td>13</td><td>CMTDEN</td><td>换相DMA更新请求使能0:禁止换相DMA更新请求1:使能换相DMA更新请求</td></tr><tr><td>12</td><td>CH3DEN</td><td>通道3比较/捕获DMA请求使能0:禁止通道3比较/捕获DMA请求1:使能通道3比较/捕获DMA请求</td></tr><tr><td>11</td><td>CH2DEN</td><td>通道2比较/捕获DMA请求使能0:禁止通道2比较/捕获DMA请求1:使能通道2比较/捕获DMA请求</td></tr><tr><td>10</td><td>CH1DEN</td><td>通道1比较/捕获DMA请求使能0:禁止通道1比较/捕获DMA请求1:使能通道1比较/捕获DMA请求</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>BRKIE</td><td>中止中断使能0:禁止中止中断1:使能中止中断</td></tr><tr><td>6</td><td>TRGIE</td><td>触发中断使能0:禁止触发中断1:使能触发中断</td></tr><tr><td>5</td><td>CMTIE</td><td>换相更新中断使能0:禁止换相更新中断1:使能换相更新中断</td></tr></table>

rc_w0 

<table><tr><td>4</td><td>CH3IE</td><td>通道3比较/捕获中断使能0:禁止通道3中断1:使能通道3中断</td></tr><tr><td>3</td><td>CH2IE</td><td>通道2比较/捕获中断使能0:禁止通道2中断1:使能通道2中断</td></tr><tr><td>2</td><td>CH1IE</td><td>通道1比较/捕获中断使能0:禁止通道1中断1:使能通道1中断</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>CH4IF</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SYSBIF</td><td>CH3OF</td><td>CH2OF</td><td>CH1OF</td><td>CH0OF</td><td>BRK1IF</td><td>BRK0IF</td><td>TRGIF</td><td>CMTIF</td><td>CH3IF</td><td>CH2IF</td><td>CH1IF</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="2"></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>CH4IF</td><td>通道4比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>SYSBIF</td><td>系统源中止事件中断标志位当系统中止源有效时,该位由硬件置1,当系统源无效时,该位由软件清零。0:无系统中止事件中断发生1:系统中止事件中断发生注意:当该位置1时,在通道输出恢复前,该位必须由软件清零。</td></tr><tr><td>12</td><td>CH3OF</td><td>通道3捕获溢出标志参见CH0OF描述</td></tr><tr><td>11</td><td>CH2OF</td><td>通道2捕获溢出标志参见CH0OF描述</td></tr><tr><td>10</td><td>CH1OF</td><td>通道1捕获溢出标志参见CH0OF描述</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0。0:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8</td><td>BRK1IF</td><td>BREAK1中断标志位一旦BREAK1输入有效,由硬件对该位置‘1’。如果BREAK1输入无效,则该位可由软件清‘0’。0:无BREAK1事件产生1:BREAK1输入上检测到有效电平。当TIMERx_DMAINTEN寄存器中的BRKIE=1时,中断产生</td></tr><tr><td>7</td><td>BRK0IF</td><td>BREAK0中断标志位一旦BREAK0输入有效,由硬件对该位置‘1’。如果BREAK0输入无效,则该位可由软件清‘0’。0:无BREAK0事件产生1:BREAK0输入上检测到有效电平</td></tr><tr><td>6</td><td>TRGIF</td><td>触发中断标志当发生触发事件时,此标志会置1,此位由软件清0。当暂停模式使能时,触发输入的任意边沿都可以产生触发事件。否则,其它模式时,仅在触发输入端检测到有效边沿,产生触发事件。0:无触发事件产生1:触发中断产生</td></tr><tr><td>5</td><td>CMTIF</td><td>通道换相更新中断标志当通道换相更新事件发生时,此标志位被硬件置1,此位由软件清0。0:无通道换相更新中断发生1:通道换相更新中断发生</td></tr><tr><td>4</td><td>CH3IF</td><td>通道3比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>3</td><td>CH2IF</td><td>通道2比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>2</td><td>CH1IF</td><td>通道1比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1,软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>BRK1G</td><td>BRK0G</td><td>TRGG</td><td>CMTG</td><td>CH3G</td><td>CH2G</td><td>CH1G</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="7"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8</td><td>BRK1G</td><td>产生BREAK1事件该位由软件置1,用于产生一个BREAK1事件,由硬件自动清0。当此位被置1时,POEN位被清0且BRK1IF位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:不产生BREAK1事件1:产生 BREAK1 事件</td></tr><tr><td>7</td><td>BRK0G</td><td>产生BREAK0事件该位由软件置1,用于产生一个BREAK0事件,由硬件自动清0。当此位被置1时,POEN位被清0且BRK0IF位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:不产生 BREAK0 事件1:产生 BREAK0 事件</td></tr><tr><td>6</td><td>TRGG</td><td>触发事件产生此位由软件置1,由硬件自动清0。当此位被置1,TIMERx_INTF 寄存器的 TRGIF标志位被置1,若开启对应的中断和 DMA,则产生相应的中断和 DMA 传输。0:无触发事件产生1:产生触发事件</td></tr><tr><td>5</td><td>CMTG</td><td>通道换相更新事件发生此位由软件置1,由硬件自动清0。当此位被置1,根据CCSE位(TIMERx_CTL1寄存器中)的值,通道捕获/比较控制寄存器(CHxEN,CHxNEN和CHxCOMCTL)的互补输出被更新。0:不产生通道换相更新事件1:产生通道换相更新事件</td></tr><tr><td>4</td><td>CH3G</td><td>通道3捕获或比较事件发生参见CH0G描述</td></tr><tr><td>3</td><td>CH2G</td><td>通道2捕获或比较事件发生参见CH0G描述</td></tr><tr><td>2</td><td>CH1G</td><td>通道1捕获或比较事件发生参见CH0G描述</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被捕获到TIMERx_CH0CV寄存器,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,如果选择了中央对齐或向上计数模式,计数器被清0。否则(向下计数模式)计数器将载入自动重载值,预分频计数器将同时被清除。0:无更新事件产生1:产生更新事件</td></tr></table>

输出比较模式:

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>CH1COMCTL[3]</td><td colspan="7">保留</td><td>CH0COMCTL[3]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH1COM CEN</td><td colspan="3">CH1COMCTL[2:0]</td><td>CH1COM SEN</td><td>CH1COM FEN</td><td rowspan="2" colspan="2">CH1MS[1:0]</td><td>CH0COM CEN</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COM SEN</td><td>CH0COM FEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH1CAPFLT[3:0]</td><td colspan="2">CH1CAPPSC[1:0]</td><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>24</td><td>CH1COMCTL[3]</td><td>参见 CH1COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>16</td><td>CH0COMCTL[3]</td><td>参见 CH0COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH1COMCEN</td><td>通道 1 输出比较清 0 使能参见 CH0COMCEN 描述</td></tr><tr><td>14:12</td><td>CH1COMCTL[2:0]</td><td>通道 1 输出比较模式参见 CH0COMCTL 描述</td></tr><tr><td>11</td><td>CH1COMSEN</td><td>通道 1 输出比较影子寄存器使能参见 CH0COMSEN 描述</td></tr><tr><td>10</td><td>CH1COMFEN</td><td>通道 1 输出比较快速使能参见 CH0COMFEN 描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道 1 模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH1EN 位被清 0)时这些位才可以写。00:通道 1 配置为输出。01:通道 1 配置为输入,IS1 映射在 CI1FE1 上。10:通道 1 配置为输入,IS1 映射在 CI0FE1 上。11:通道 1 配置为输入,IS1 映射在 ITS 上,此模式仅工作在内部触发器输入被选中时(由 SYSCFG_TIMER0CFG)寄存器中的 TSCFGx[2:0] (x = 3,4,5,6,7)位域选择)。</td></tr><tr><td>7</td><td>CH0COMCEN</td><td>通道 0 输出比较清 0 使能当此位被置 1,当检测到 ETIFP 输入高电平时,O0CPRE 参考信号被清 00:禁止通道 0 输出比较清零1:使能通道 0 输出比较清零</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道 0 输出比较模式此位定义了 O0CPRE 的动作,而 O0CPRE 决定了 CH0_O、CH0_ON 的值。O0CPRE 高电平有效,而 CH0_O、CH0_ON 的有效电平取决于 CH0P、CH0NP 位。0000:时基。输出比较寄存器 TIMERx_CH0CV 与计数器 TIMERx_CNT 间的比较对 O0CPRE 不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 翻转。0100:强制为低。强制 O0CPRE 为低电平0101:强制为高。强制 O0CPRE 为高电平0110:PWM 模式 0。在向上计数时,一旦计数器值小于 TIMERx_CH0CV 时,O0CPRE 为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于 TIMERx_CH0CV</td></tr></table>

时，O0CPRE 为无效电平，否则为有效电平。

0111：PWM模式1。在向上计数时，一旦计数器值小于TIMERx_CH0CV时，O0CPRE为无效电平，否则为有效电平。在向下计数时，一旦计数器的值大于 TIMERx_CH0CV时，O0CPRE 为有效电平，否则为无效电平。

在 PWM 模式 0 或 PWM 模式 1 中，只有当比较结果改变了或者输出比较模式中从时基模式切换到 PWM 模式时，O0CPRE 电平才改变。

当 TIMERx_CCHP 寄存器的 PROT[1：0]=11 且 CH0MS =00（比较模式）时，此位不能被改变。

1000:可再次触发单脉冲模式 0。 O0CPRE 工作在 PWM 模式 0，向上计数时，O0CPRE 有效，当外部触发信号产生时，O0CPRE 无效，在下次更新事件产生后，O0CPRE 恢复有效。向下计数时，O0CPRE 无效，当外部触发信号产生时，O0CPRE有效，在下次更新事件产生后，O0CPRE 恢复无效。

1001: 可再次触发单脉冲模式 1。 O0CPRE 工作在 PWM 模式 1，向上计数时，O0CPRE 无效，当外部触发信号产生时，O0CPRE 有效，在下次更新事件产生后，

O0CPRE 恢复无效。向下计数时，O0CPRE 有效，当外部触发信号产生时，O0CPRE无效，在下次更新事件产生后，O0CPRE 恢复有效。

## 1010:保留

1011:保留

1100:复合 PWM0 模式。O0CPRE 工作在 PWM 模式 0，O0CPREC 输出结果是O0CPRE 和 O1CPRE 的逻辑“或”。

1101:复合 PWM1 模式。O0CPRE 工作在 PWM 模式 1，O0CPREC 输出结果是O0CPRE 和 O1CPRE 的逻辑“与”。

1110: 非对称PWM0模式。O0CPRE工作在PWM模式0，在向上计数时，O0CPREC输出结果是 O0CPRE，向下计数时输出 O1CPRE。

1111 非对称 PWM1 模式。O0CPRE 工作在 PWM 模式 1，在向上计数时，O0CPREC输出结果是 O0CPRE，向下计数时输出 O1CPRE。

当TIMERx_CCHP寄存器的PROT [1:0]=11且CH0MS =000（比较模式）时，此位不能被改变。

## CH0COMSEN 通道 0 输出比较影子寄存器使能

当此位被置 1，TIMERx_CH0CV 寄存器的影子寄存器被使能，影子寄存器在每次更新事件时都会被更新。

仅在单脉冲模式下（TIMERx_CTL0 寄存器的 SPM =1），可以在未确认预装载寄存器情况下使用 PWM 模式

## CH0COMFEN 通道 0 输出比较快速使能

当该位为 1 时，如果通道配置为 PWM 模式 0 或者 PWM 模式 1，会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配，CH0_O 被设置为比较电平而与比较结果无关。0：通道 0 输出比较快速禁能。仅比较结果输入作为有效边沿时会产生比较匹配，并将 CH0_O 设置为比较电平，激活 CH0_O 输出的最小延时为 5 个时钟周期。

1：通道 0 输出比较快速使能。触发输入信号的有效边沿和比较结果都会产生比较匹配，并将 CH0_O 设置为比较电平。当触发信号的输入作为有效边沿时，激活CH0_O 输出的最小延时为 3 个时钟周期。

## 1:0 CH0MS[1:0] 通道 0 I/O 模式选择

这 些 位 定 义 了 通 道 的 工 作 模 式 和 输 入 信 号 的 选 择 。 只 有 当 通 道 关 闭（TIMERx_CHCTL2 寄存器的 CH0EN 位被清 0）时，这些位才可写。

00：通道 0 配置为输出。

01：通道 0 配置为输入，IS0映射在 CI0FE0 上。

10：通道0 配置为输入，IS0映射在 CI1FE0 上。此模式仅工作在内部触发器输入被选中时（由 SYSCFG_TIMER0CFG）寄存器中的 TSCFGx[2:0] (x = 3,4,5,6,7)位域选择）。

输入捕获模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:12</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述</td></tr><tr><td>11:10</td><td>CH1CAPPSC[1:0]</td><td>通道1输入捕获预分频器参见CH0CAPPSC描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择与输出模式相同</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制数字滤波器由一个事件计数器组成,N个输入事件后会产生一个输出的跳变。这些位定义了CI0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=1。0001:<eq>f_{SAMP} = f_{PCLK}</eq>,N=2。0010:<eq>f_{SAMP} = f_{PCLK}</eq>,N=4。0011:<eq>f_{SAMP} = f_{PCLK}</eq>,N=8。0100:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=6。0101:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=8。0110:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=6。0111:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=8。1000:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=6。1001:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=8。1010:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=5。1011:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=6。1100:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=8。1101:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=5。1110:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=6。1111:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=8。</td></tr></table>

这2位定义了通道0输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH0EN=0时，则预分频器复位。

00：无预分频器，捕获输入口上检测到的每一个边沿都触发一次捕获。

01：每 2 个事件触发一次捕获。

10：每 4 个事件触发一次捕获。

11：每 8 个事件触发一次捕获。

1:0 CH0MS[1:0] 通道 0 模式选择

与输出比较模式相同

## 通道控制寄存器 1（TIMERx_CHCTL1）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>CH3COMCTL[3]</td><td colspan="7">保留</td><td>CH2COMCTL[3]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3COM CEN</td><td colspan="3">CH3COMCTL[2:0]</td><td>CH3COM SEN</td><td>CH3COM FEN</td><td rowspan="2" colspan="2">CH3MS[1:0]</td><td>CH2COM CEN</td><td colspan="3">CH2COMCTL[2:0]</td><td>CH2COM SEN</td><td>CH2COM FEN</td><td rowspan="2" colspan="2">CH2MS[1:0]</td></tr><tr><td colspan="4">CH3CAPFLT[3:0]</td><td colspan="2">CH3CAPPSC[1:0]</td><td colspan="4">CH2CAPFLT[3:0]</td><td colspan="2">CH2CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

## 输出比较模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>24</td><td>CH3COMCTL[3]</td><td>参见 CH3COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>16</td><td>CH2COMCTL[3]</td><td>参见 CH2COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH3COMCEN</td><td>通道 3 输出比较清 0 使能参见 CH0COMCEN 描述</td></tr><tr><td>14:12</td><td>CH3COMCTL[2:0]</td><td>通道 3 输出比较模式参见 CH0COMCTL 描述</td></tr><tr><td>11</td><td>CH3COMSEN</td><td>通道 3 输出比较影子寄存器使能参见 CH0COMSEN 描述</td></tr><tr><td>10</td><td>CH3COMFEN</td><td>通道 3 输出比较快速使能参见 CH0COMSEN 描述</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道 3 模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的CH3EN位被清0)时这些位才可以写。00:通道3配置为输出。01:通道3配置为输入,IS3映射在CI3FE3上。10:通道3配置为输入,IS3映射在CI2FE3上。11:通道3配置为输入,IS3映射在ITS上,此模式仅工作在内部触发器输入被选中时(由SYSCFG_TIMER0CFG)寄存器中的TSCFGx[2:0](x=3,4,5,6,7)位域选择)。</td></tr><tr><td>7</td><td>CH2COMCEN</td><td>通道2输出比较清0使能当此位被置1,当检测到ETIF输入高电平时,O2CPRE参考信号被清00:使能通道2输出比较清零1:禁止通道2输出比较清零</td></tr><tr><td>6:4</td><td>CH2COMCTL[2:0]</td><td>通道2输出比较模式此位定义了O2CPRE的动作,而O2CPRE决定了CH2_O、CH2_ON的值。O2CPRE高电平有效,而CH2_O、CH2_ON的有效电平取决于CH2P、CH2NP位。0000:时基。输出比较寄存器TIMERx_CH2CV与计数器TIMERx_CNT间的比较对O2CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE翻转。0100:强制为低。强制O2CPRE为低电平0101:强制为高。强制O2CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为有效电平,否则为无效电平。在PWM模式0或PWM模式1中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,CxCOMR电平才改变。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH2MS=00(比较模式)时此位不能被改变。1000:可再次触发单脉冲模式0。O2CPRE工作在PWM模式0,向上计数时,O2CPRE有效,当外部触发信号产生时,O2CPRE无效,在下次更新事件产生后,O2CPRE恢复有效。向下计数时,O2CPRE无效,当外部触发信号产生时,O2CPRE有效,在下次更新事件产生后,O2CPRE恢复无效。1001:可再次触发单脉冲模式1。O2CPRE工作在PWM模式1,向上计数时,O2CPRE无效,当外部触发信号产生时,O2CPRE有效,在下次更新事件产生后,O2CPRE恢复无效。向下计数时,O2CPRE有效,当外部触发信号产生时,O2CPRE无效,在下次更新事件产生后,O2CPRE恢复有效。1010:保留1011:保留1100:复合 PWM0 模式。O2CPRE 工作在 PWM 模式 0,O2CPREC 输出结果是 O2CPRE 和 O3CPRE 的逻辑“或”。1101:复合 PWM1 模式。O2CPRE 工作在 PWM 模式 1,O2CPREC 输出结果是 O2CPRE 和 O3CPRE 的逻辑“与”。1110:非对称 PWM0 模式。O2CPRE 工作在 PWM 模式 0,在向上计数时,O2CPREC 输出结果是 O2CPRE,向下计数时输出 O3CPRE。1111 非对称 PWM1 模式。O2CPRE 工作在 PWM 模式 1,在向上计数时,O2CPREC 输出结果是 O2CPRE,向下计数时输出 O3CPRE。当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 且 CH2MS =000(比较模式)时,此位不能被改变。</td></tr><tr><td>3</td><td>CH2COMSEN</td><td>通道 2 出比较影子寄存器使能当此位被置 1,TIMERx_CH2CV 寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道 2 输出/比较影子寄存器1:使能通道 2 输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0 寄存器的 SPM=1),可以在未确认预装载寄存器情况下使用 PWM 模式当 TIMERx_CCHP 寄存器的 PROT[1:0]=11 且 CH2MS =00 时此位不能被改变。</td></tr><tr><td>2</td><td>CH2COMFEN</td><td>通道 2 输出比较快速使能当该位为 1 时,如果通道配置为 PWM 模式 0 或者 PWM 模式 1,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH2_O 被设置为比较电平而与比较结果无关。0:通道 2 输出比较快速禁能。仅比较结果输入作为有效边沿时会产生比较匹配,并将 CH2_O 设置为比较电平,激活 CH2_O 输出的最小延时为 5 个时钟周期。1:通道 2 输出比较快速使能。触发输入信号的有效边沿和比较结果都会产生比较匹配,并将 CH2_O 设置为比较电平。当触发信号的输入作为有效边沿时,激活 CH2_O 输出的最小延时为 3 个时钟周期。</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td>通道 2 I/O 模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH2EN 位被清 0)时这些位才可写。00:通道 2 配置为输出。01:通道 2 配置为输入,IS2 映射在 CI2FE2 上。10:通道 2 配置为输入,IS2 映射在 CI3FE2 上。11:通道 2 配置为输入,IS2 映射在 ITS 上,此模式仅工作在内部触发器输入被选中时(由 SYSCFG_TIMER0CFG)寄存器中的 TSCFGx[2:0](x = 3,4,5,6,7)位域选择)。</td></tr></table>

输入捕获模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:12</td><td>CH3CAPFLT[3:0]</td><td>通道3输入捕获滤波控制参见CH0CAPFLT描述</td></tr><tr><td>11:10</td><td>CH3CAPPSC[1:0]</td><td>通道3输入捕获预分频器参见CH0CAPPSC描述</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择与输出模式相同</td></tr><tr><td>7:4</td><td>CH2CAPFLT[3:0]</td><td>通道2输入捕获滤波控制数字滤波器由一个事件计数器组成,N个输入事件后会产生一个输出的跳变。这些位定义了CI2输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=1。0001:<eq>f_{SAMP} = f_{PCLK}</eq>,N=2。0010:<eq>f_{SAMP} = f_{PCLK}</eq>,N=4。0011:<eq>f_{SAMP} = f_{PCLK}</eq>,N=8。0100:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=6。0101:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=8。0110:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=6。0111:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=8。1000:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=6。1001:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=8。1010:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=5。1011:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=6。1100:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=8。1101:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=5。1110:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=6。1111:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=8。</td></tr><tr><td>3:2</td><td>CH2CAPPSC[1:0]</td><td>通道2输入捕获预分频器这2位定义了通道2输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH2EN=0时,则预分频器复位。00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获。01:每2个事件触发一次捕获。10:每4个事件触发一次捕获。11:每8个事件触发一次捕获。</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td>通道2模式选择与输出比较模式相同</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>CH4P</td><td>CH4EN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3NP</td><td>保留</td><td>CH3P</td><td>CH3EN</td><td>CH2NP</td><td>CH2NEN</td><td>CH2P</td><td>CH2EN</td><td>CH1NP</td><td>CH1NEN</td><td>CH1P</td><td>CH1EN</td><td>CH0NP</td><td>CH0NEN</td><td>CH0P</td><td>CH0EN</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>CH4P</td><td>通道4极性参考CHOP描述</td></tr><tr><td>16</td><td>CH4EN</td><td>通道4使能参考CH0EN描述</td></tr><tr><td>15</td><td>CH3NP</td><td>通道3互补输出极性参考CH0NP描述</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>CH3P</td><td>通道3极性参考CHOP描述</td></tr><tr><td>12</td><td>CH3EN</td><td>通道3使能参考CH0EN描述</td></tr><tr><td>11</td><td>CH2NP</td><td>通道2互补输出极性参考CH0NP描述</td></tr><tr><td>10</td><td>CH2NEN</td><td>通道2互补输出使能参考CH0NEN描述</td></tr><tr><td>9</td><td>CH2P</td><td>通道2极性参考CHOP描述</td></tr><tr><td>8</td><td>CH2EN</td><td>通道2使能参考CH0EN描述</td></tr><tr><td>7</td><td>CH1NP</td><td>通道1互补输出极性参考CH0NP描述</td></tr><tr><td>6</td><td>CH1NEN</td><td>通道1互补输出使能参考CH0NEN描述</td></tr><tr><td>5</td><td>CH1P</td><td>通道1极性参考CHOP描述</td></tr><tr><td>4</td><td>CH1EN</td><td>通道1使能参考CH0EN描述</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,此位定义了互补输出信号的极性。0:通道0高电平有效1:通道0低电平有效当通道0配置为输入模式时,此位和CHOP联合使用,作为输入信号CI0的极性选择控制信号。当 TIMERx_CCHP 寄存器的 PROT[1: 0]=11 或 10 时此位不能被更改。</td></tr><tr><td>2</td><td>CHONEN</td><td>通道 0 互补输出使能当通道 0 配置为输出模式时,将此位置 1 使能通道 0 的互补输出。0:禁止通道 0 互补输出1:使能通道 0 互补输出</td></tr><tr><td>1</td><td>CHOP</td><td>通道 0 极性当通道 0 配置为输出模式时,此位定义了输出信号极性。0:通道 0 高电平有效1:通道 0 低电平有效当通道 0 配置为输入模式时,此位定义了 CI0 信号极性。CHOP 将选择 CI0FE0 或者 CI1FE0 的有效边沿或者捕获极性。CHOP=0:把 CixFE0 的上升沿作为捕获或者从模式下触发的有效信号,并且 CixFE0 不会被翻转。CHOP=1:把 CixFE0 的下降沿作为捕获或者从模式下触发的有效信号,并且 CixFE0 会被翻转。当 TIMERx_CCHP 寄存器的 PROT[1: 0]=11 或 10 时此位不能被更改。</td></tr><tr><td>0</td><td>CHOEN</td><td>通道 0 捕获/比较使能当通道 0 配置为输出模式时,将此位置 1 使能 CHO_O 信号有效。当通道 0 配置为输入模式时,将此位置 1 使能通道 0 上的捕获事件。0:禁止通道 01:使能通道 0</td></tr></table>

## 计数器寄存器（TIMERx_CNT）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>

## 预分频寄存器（TIMERx_PSC）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值计数器时钟等于 PSC 时钟除以(PSC+1),每次当更新事件产生时,PSC 的值被装入当前预分频寄存器。</td></tr></table>

## 计数器自动重载寄存器（TIMERx_CAR）

地址偏移：0x2C

复位值：0x0000 FFFF

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。</td></tr></table>

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>CREP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CREP[15:0]</td><td>重复计数器的值这些位定义了更新事件的产生速率。重复计数器计数值减为0时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。</td></tr></table>

## 通道 0 捕获/比较寄存器（TIMERx_CH0CV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值,并且本寄存器为只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 1 捕获/比较寄存器（TIMERx_CH1CV）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CH1VAL[15:0]</td><td>通道1的捕获或比较值当通道1配置为输入模式时,这些位决定了上次捕获事件的计数器值,并且本寄存器为只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 2 捕获/比较寄存器（TIMERx_CH2CV）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CH2VAL[15:0]</td><td>通道2的捕获或比较值当通道2配置为输入模式时,这些位决定了上次捕获事件的计数器值,并且本寄存器为只读。当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 3 捕获/比较寄存器（TIMERx_CH3CV）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3VAL[15:0]</td></tr></table>

<table><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CH3VAL[15:0]</td><td>通道3的捕获或比较值当通道3配置为输入模式时,这些位决定了上次捕获事件的计数器值,并且本寄存器为只读。当通道3配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 互补通道保护寄存器（TIMERx_CCHP）

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>BRK1P</td><td>BRK1EN</td><td colspan="4">BRK1F[3:0]</td><td colspan="4">BRK0F[3:0]</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>POEN</td><td>OAEN</td><td>BRK0P</td><td>BRK0EN</td><td>ROS</td><td>IOS</td><td colspan="2">PROT[1:0]</td><td colspan="8">DTCFG[7:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>25</td><td>BRK1P</td><td>BREAK1输入信号极性该位用于配置BREAK1输入信号的极性0: BREAK1输入信号低电平有效1: BREAK1输入信号高电平有效此位只有在TIMERx_CCHP寄存器的PROT [1:0] =00时才可修改。注意:对该位的每一次写操作,需要延时1个APB时钟才有效。</td></tr><tr><td>24</td><td>BRK1EN</td><td>BREAK1输入信号使能该位置1时,使能BREAK1输入信号。0: BREAK1输入禁能1: BREAK1输入使能此位只有在TIMERx_CCHP寄存器的PROT [1:0] =00时才可修改。注意:1)对该位的每一次写操作,需要延时1个APB时钟才有效。2)该位仅用于ROS=1且IOS=1时</td></tr><tr><td>23:20</td><td>BRK1F[3:0]</td><td>BREAK1输入信号滤波数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了BREAK1输入信号的采样频率和数字滤波器的长度。0000:无滤波器,BREAK1异步有效,N=10001:fSAMP=fCK_TIMER,N=20010:fSAMP=fCK_TIMER,N=4</td></tr></table>

$$
0 0 1 1: \mathrm{fSAMP} = \mathrm {fCK\_TIMER}, N = 8
$$

$$
0 1 0 0: \mathrm{fSAMP} = \mathrm{fDTS} / 2, \mathrm{N} = 6
$$

$$
0 1 0 1: \mathrm{fSAMP} = \mathrm{fDTS} / 2, \mathrm{N} = 8
$$

$$
0 1 1 0: \mathrm{fSAMP} = \mathrm{fDTS} / 4, \mathrm{N} = 6
$$

$$
0 1 1 1: \mathrm{fSAMP} = \mathrm{fDTS} / 4, \mathrm{N} = 8
$$

$$
1 0 0 0: \mathrm{fSAMP} = \mathrm{fDTS/8}, \mathrm{N=6}
$$

$$
1 0 0 1: \mathrm{fSAMP} = \mathrm{fDTS} / 8, \mathrm{N} = 8
$$

$$
1 0 1 0: \mathrm{fSAMP} = \mathrm{fDTS} / 1 6, \mathrm{N} = 5
$$

$$
1 0 1 1: \mathrm{fSAMP} = \mathrm{fDTS/16}, \mathrm{N=6}
$$

$$
1 1 0 0: \mathrm{fSAMP} = \mathrm{fDTS} / 1 6, \mathrm{N} = 8
$$

$$
1 1 0 1: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 5
$$

$$
1 1 1 0: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 6
$$

$$
1 1 1 1: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 8
$$

$$
0 1 0 1: \mathrm{fSAMP} = \mathrm{fDTS} / 2, \mathrm{N} = 8
$$

$$
0 1 1 0: \mathrm{fSAMP} = \mathrm{fDTS} / 4, \mathrm{N} = 6
$$

$$
0 1 1 1: \mathrm{fSAMP} = \mathrm{fDTS} / 4, \mathrm{N} = 8
$$

$$
1 0 0 1: \mathrm{fSAMP} = \mathrm{fDTS/8}, \mathrm{N=8}
$$

$$
1 1 0 0: \mathrm{fSAMP} = \mathrm{fDTS} / 1 6, \mathrm{N} = 8
$$

$$
1 1 0 1: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 5
$$

$$
1 1 1 0: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 6
$$

$$
1 1 1 1: \mathrm{fSAMP} = \mathrm{fDTS} / 3 2, \mathrm{N} = 8
$$

<table><tr><td></td><td></td><td>1:使能通道输出注意:仅当CHxMS[1:0]=2'b00时该位有效。</td></tr><tr><td>14</td><td>OAEN</td><td>自动输出使能0:POEN位只能使用软件方式置1。1:如果中止输入无效,下一次更新事件发生时,POEN位将会置1。此位只有在TIMERxCCHP寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>13</td><td>BRKOP</td><td>BREAK0输入信号极性该位用于配置BREAK0输入信号的极性0:BREAK0输入信号低电平有效1:BREAK0输入信号高电平有效此位只有在TIMERxCCHP寄存器的PROT[1:0]=00时才可修改。注意:对该位的每一次写操作,需要延时1个APB时钟才有效。</td></tr><tr><td>12</td><td>BRK0EN</td><td>BREAK0输入信号使能该位置0时,使能BREAK0输入信号。0:BREAK0输入禁能1:BREAK0输入使能此位只有在TIMERxCCHP寄存器的PROT[1:0]=00时才可修改。注意:1)对该位的每一次写操作,需要延时1个APB时钟才有效。2)该位仅用于ROS=1且IOS=1时</td></tr><tr><td>11</td><td>ROS</td><td>运行模式下“关闭状态”使能当POEN位被置1(运行模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。0:输出“关闭状态”禁能。当CHxEN或者CHxNEN位被清零,对应通道为输出“禁能状态”。1:输出“关闭状态”使能。当CHxEN或者CHxNEN位被清零,对应通道为输出“关闭状态”。此位在TIMERxCCHP寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>10</td><td>IOS</td><td>空闲模式下“关闭状态”使能当POEN位被清0(空闲模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。0:输出“关闭状态”禁能。当CHxEN和CHxNEN位均被清零,对应通道为输出“禁能状态”。1:输出“关闭状态”使能。不论CHxEN和CHxNEN位的值,对应通道为输出“关闭状态”。此位在TIMERxCCHP寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>9:8</td><td>PROT[1:0]</td><td>互补寄存器保护控制这两位定义了寄存器的写保护特性。00:禁能保护模式,无写保护01:PROT模式0。TIMERxCTL1寄存器中ISOx/ISOxN位,TIMERxCCHP寄存器中BRKEN/BRKP/OAEN/DTCFG位写保护10:PROT模式1。除了PROT模式0下的寄存器写保护外,还有TIMERx_CHCTL2寄存器中 CHxP/CHxNP 位(如果相应通道配置为输出模式),TIMERx_CCHP 寄存器中 ROS/IOS 位。11: PROT 模式 2。除了 PROT 模式 1 下的寄存器写保护外,还有 TIMERx_CHCTLR0/1 中 CHxCOMCTL/ CHxCOMSEN 位(如果相关通道配置为输出模式)写保护。系统复位后这两位只能被写一次,一旦 TIMERx_CCHP 寄存器被写入,这两位被写保护。</td></tr><tr><td>7:0</td><td>DTCFG[7:0]</td><td>死区时间配置这些位定义了插入互补输出之间的死区持续时间。DTCFG 值和死区时间的关系如下:DTCFG[7:5] = 3'b0xx:DT value = DTCFG[7:0] * <eq>t_{DT}</eq>,<eq>t_{DT} = t_{DTS}</eq>。DTCFG[7:5] = 3'b10x:DT value = (64+DTCFG[5:0]) * <eq>t_{DT}</eq>,<eq>t_{DT} = t_{DTS}</eq>*2。DTCFG[7:5] = 3'b110:DT value = (32+DTCFG[4:0]) * <eq>t_{DT}</eq>,<eq>t_{DT} = t_{DTS}</eq>*8。DTCFG[7:5] = 3'b111:DT value = (32+DTCFG[4:0]) * <eq>t_{DT}</eq>,<eq>t_{DT} = t_{DTS}</eq>*16。此位只有在 TIMERx_CCHP 寄存器的 PROT[1:0]=00 时才可修改。</td></tr></table>

## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="5">DMATC[4:0]</td><td colspan="3">保留</td><td colspan="5">DMATA [4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>12:8</td><td>DMATC[4:0]</td><td>DMA传输计数该位域定义了DMA访问(读/写)TIMERx_DMATB寄存器的次数。5&#x27;b00000:1次传输5&#x27;b00001:2次传输...5&#x27;b10001:18次传输</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:0</td><td>DMATA[4:0]</td><td>DMA传输起始地址该位域定义了DMA访问TIMERx_DMATB寄存器的第一个地址。当第一次访问TIMERx_DMATB寄存器时,实际访问的就是该位域指定的地址。第二次访问TIMERx_DMATB时,将访问(起始地址+0x4)。</td></tr></table>

5’b00000：TIMERx_CTL0 

5’b00001：TIMERx_CTL1 

5’b10010：TIMERx_DMACFG 

总之：起始地址 = TIMERx_CTL0 + DMATA*4

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>DMATB[15:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,从(起始地址)到(起始地址+传输次数*4)地址范围内的寄存器会被访问。传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

## 通道控制寄存器 1（TIMERx_CHCTL3）

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>CH4COMCTL[3]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>CH4COMCEN</td><td colspan="3">CH4COMCTL[2:0]</td><td>CH4COMSEN</td><td>CH4COMFEN</td><td colspan="2">保留</td></tr><tr><td colspan="8"></td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td colspan="2"></td></tr></table>

输出比较模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>16</td><td>CH4COMCTL[3]</td><td>通道4输出比较模式参见CH4COMCTL[2:0]描述</td></tr><tr><td>25:8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7</td><td>CH4COMCEN</td><td>通道4输出比较清0使能参见CH0COMCEN描述</td></tr><tr><td>6:4</td><td>CH4COMCTL[2:0]</td><td>通道2输出比较模式此位定义了O4CPRE的动作,而O4CPRE决定了CH4_O的值。O4CPRE高电平有效,而CH4_O的有效电平取决于CH4P位。0000:时基。输出比较寄存器TIMERx_CH4CV与计数器TIMERx_CNT间的比较对O4CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH4CV相同时,强制O4CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH4CV相同时,强制O4CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH4CV相同时,强制O4CPRE翻转。0100:强制为低。强制O4CPRE为低电平0101:强制为高。强制O4CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH4CV时,O4CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH4CV时,O4CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH4CV时,O4CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_CH4CV时,O4CPRE为有效电平,否则为无效电平。在PWM模式0或PWM模式1中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,CxCOMR电平才改变。1000:可再次触发模式0。O4CPRE工作在PWM模式0,向上计数时,O4CPRE有效,当外部触发信号产生时,O4CPRE无效,在下次更新事件产生后,O4CPRE恢复有效。向下计数时,O4CPRE无效,当外部触发信号产生时,O4CPRE有效,在下次更新事件产生后,O4CPRE恢复无效。1001:可再次触发模式1。O4CPRE工作在PWM模式1,向上计数时,O4CPRE无效,当外部触发信号产生时,O4CPRE有效,在下次更新事件产生后,O4CPRE恢复无效。向下计数时,O4CPRE有效,当外部触发信号产生时,O4CPRE无效,在下次更新事件产生后,O4CPRE恢复有效。其他:保留当TIMERx_CCHP寄存器的PROT[1:0]=11,此位不能被改变。</td></tr><tr><td>3</td><td>CH4COMSEN</td><td>通道4出比较影子寄存器使能当此位被置1,TIMERx_CH4CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道4输出/比较影子寄存器1:使能通道4输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用 PWM 模式当 TIMERx_CCHP 寄存器的 PROT[1: 0]=11。</td></tr><tr><td>2</td><td>CH4COMFEN</td><td>通道 4 输出比较快速使能当该位为 1 时,如果通道配置为 PWM 模式 0 或者 PWM 模式 1,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,<eq>CH4\_O</eq> 被设置为比较电平而与比较结果无关。0:通道 0 输出比较快速禁能。仅比较结果输入作为有效边沿时会产生比较匹配,并将 <eq>CH0\_O</eq> 设置为比较电平,激活 <eq>CH0\_O</eq> 输出的最小延时为 5 个时钟周期。1:通道 0 输出比较快速使能。触发输入信号的有效边沿和比较结果都会产生比较匹配,并将 <eq>CH0\_O</eq> 设置为比较电平。当触发信号的输入作为有效边沿时,激活 <eq>CH0\_O</eq> 输出的最小延时为 3 个时钟周期。</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值.</td></tr></table>

## 通道 4 捕获/比较寄存器（TIMERx_CH4CV）

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CCH4CH2</td><td>CCH4CH1</td><td>CCH4CH0</td><td colspan="13">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH4VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CCH4CH2</td><td>组合通道 4 和通道 20: O4CPRE 和 O2CPREF 独立输出1: O2CPREF 输出为 O2CPREF 和 O4CPRE 的逻辑“与”该位域可立即生效或者在下一次更新事件发生时生效(当 TIMERx_CHCTL1 中的比较影子寄存器使能)。</td></tr><tr><td>30</td><td>CCH4CH1</td><td>组合通道 4 和通道 10: O4CPRE 和 O1CPREF 独立输出1: O1CPREF 输出为 O1CPREF 和 O4CPRE 的逻辑“与”该位域可立即生效或者在下一次更新事件发生时生效(当 TIMERx_CHCTL1 中的比较影子寄存器使能)。</td></tr><tr><td>29</td><td>CCH4CH0</td><td>组合通道 4 和通道 00: O4CPRE 和 O0CPREF 独立输出1: O0CPREF 输出为 O0CPREF 和 O4CPRE 的逻辑“与”该位域可立即生效或者在下一次更新事件发生时生效(当 TIMERx_CHCTL1 中的比较影子寄存器使能)。</td></tr><tr><td>28:16</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CH4VAL[15:0]</td><td>通道4的捕获比较值这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 附加通道控制寄存器 0（TIMER0_AFCTL0）

地址偏移：0x60

复位值：0x0000 0001

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">ETISEL[3:2]</td></tr></table>

<table><tr><td>15 14</td><td>13 12 11 10</td><td>9</td><td>8 7 6 5 4 3 2 1</td><td>0</td></tr><tr><td>ETISEL[1:0]</td><td>保留</td><td>BRK0INP</td><td>保留</td><td>BRK0INE N</td></tr><tr><td>rw</td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>17:14</td><td>ETISEL</td><td>ETI 触发源选择该位域选择 ETI 的触发源0000: ETI 保留模式0011: ADC_WD0_OUT0100: ADC_WD1_OUT0101: ADC_WD2_OUT其他: 保留当 TIMERx_CCHP 寄存器的 PROT [1:0]=01,此位不能被改变。</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>9</td><td>BRK0INP</td><td>BREAK0备用输入极性该位用于配置BRKIN0输入极性,具体极性是由该位和BRK0P位共同确定。0: BRKIN0输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1: BRKIN0输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP寄存器的PROT [1:0]=00时才可修改。</td></tr><tr><td>8:1</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>0</td><td>BRK0INEN</td><td>BREAK0备用输入使能0: BRKIN0输入禁能1: BRKIN0输入使能</td></tr></table>

此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0] =00 时才可修改。

## 附加通道控制寄存器 1（TIMER0_AFCTL1）

地址偏移：0x64

复位值：0x0000 0001

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>BRK1INP</td><td colspan="8">保留</td><td>BRK1INE N</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>9</td><td>BRK1INP</td><td>BRKIN1备用功能输入极性该位用于配置BRKIN1输入极性,具体极性是由该位和BRKOP位共同确定。0: BRKIN1输入信号不反相(BRKOP=0,输入信号低有效;BRKOP=1,输入信号高有效)1: BRKIN1输入信号反相(BRKOP=0,输入信号高有效;BRKOP=1,输入信号低有效)此位只有在TIMERx_CCHP寄存器的PROT [1:0] =00时才可修改。</td></tr><tr><td>8:1</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>0</td><td>BRK1INEN</td><td>BRKIN1备用输入使能0: BRKIN1输入禁能1: BRKIN1输入使能此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0] =00 时才可修改。</td></tr></table>

输入选择寄存器（TIMERx_INSEL）

地址偏移：0x68

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">CI1_SEL[3:0]</td><td colspan="4">保留</td><td colspan="4">CI0_SEL[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>11:8</td><td>CI1_SEL[3:0]</td><td>TIMER0_CH1输入选择0000: TIMER0_CH1输入捕获0001: 比较器1输出其他: 保留</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:0</td><td>CI0_SEL[3:0]</td><td>TIMER0_CH0输入选择0000: TIMER0_CH0输入捕获0001: 比较器0输出其他: 保留</td></tr></table>

配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>OUTSEL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效。0:无影响。</td></tr><tr><td>0</td><td>OUTSEL</td><td>输出值选择位此位由软件写1或清0。1:如果POEN位与IOS位均为0,则输出无效。0:无影响。</td></tr></table>

