## 14.2.5. TIMERx 寄存器（x=2）

TIMER2基地址：0x4000 0400

控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="2">CAM[1:0]</td><td>DIR</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(CK_TIMER)与死区时间和数字滤波器采样时钟(DTS)之间的分频系数。00:<eq>f_{DTS}=f_{CK\_TIMER}</eq>01:<eq>f_{DTS}=f_{CK\_TIMER}/2</eq>10:<eq>f_{DTS}=f_{CK\_TIMER}/4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:5</td><td>CAM[1:0]</td><td>计数器对齐模式选择00:无中央对齐计数模式(边沿对齐模式)。DIR位指定了计数方向01:中央对齐向下计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),只有在向下计数时,CHxF位置110:中央对齐向上计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),只有在向上计数时,CHxF位置111:中央对齐上下计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),在向上和向下计数时,CHxF位都会置1当计数器使能以后,该位不能从0x00切换到非0x00。</td></tr><tr><td>4</td><td>DIR</td><td>方向0:向上计数1:向下计数当计数器配置为中央对齐计数模式或正交译码器模式时,该位只读。</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0: 单脉冲模式禁能。更新事件发生后,计数器继续计数1: 单脉冲模式使能。在下一次更新事件发生时,计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该位,选择更新事件源.0: 以下事件均会产生更新中断或DMA请求:UPG位被置1计数器溢出/下溢复位模式产生的更新1: 下列事件会产生更新中断或DMA请求:计数器溢出/下溢</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新.该位用来使能或禁能更新事件的产生0: 更新事件使能. 更新事件发生时,相应的影子寄存器被装入预装载值,以下事件均会产生更新事件:UPG位被置1计数器溢出/下溢复位模式产生的更新1: 更新事件禁能.注意:当该位被置1时,UPG位被置1或者复位模式不会产生更新事件,但是计数器和预分频器被重新初始化</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0: 计数器禁能1: 计数器使能在软件将CEN位置1后,外部时钟、暂停模式和正交译码器模式才能工作。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TIOS</td><td colspan="3">MMC[2:0]</td><td>DMAS</td><td colspan="3">保留.</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TIOS</td><td>通道0触发输入选择0:选择 TIMERx_CH0 引脚作为通道 0 的触发输入1:选择 TIMERx_CH0,CH1 和 CH2 引脚异或的结果作为通道 0 的触发输入</td></tr><tr><td>6:4</td><td>MMC[2:0]</td><td>主模式控制这些位控制TRGO信号的选择,TRGO信号由主定时器发给从定时器用于同步功能000:当产生一个定时器复位事件后,输出一个TRGO信号,定时器复位源为:主定时器产生一个复位事件TIMERx_SWEVG寄存器中UPG位置1001:当产生一个定时器使能事件后,输出一个TRGO信号,定时器使能源为:CEN位置1在暂停模式下,触发输入置1010:当产生一个定时器更新事件后,输出一个TRGO信号,更新事件源由UPDIS和UPS位决定011:当通道0在发生一次捕获或一次比较成功时,主模式控制器产生一个TRGO脉冲100:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O0CPRE101:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O1CPRE110:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O2CPRE111:当产生一次比较事件时,输出一个 TRGO 信号,比较事件源来自 O3CPRE</td></tr><tr><td>3</td><td>DMAS</td><td>DMA 请求源选择0:当通道捕获/比较事件发生时,发送通道 x 的 DMA 请求.1:当更新事件发生,发送通道 x 的 DMA 请求</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 从模式配置寄存器（TIMERx_SMCFG）

地址偏移：0x08

复位值： 0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ETP</td><td>SMC1</td><td colspan="2">ETPSC[1:0]</td><td colspan="4">ETFC[3:0]</td><td>MSM</td><td colspan="7">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15</td><td>ETP</td><td>外部触发极性该位指定 ETI 信号的极性0: ETI 高电平或上升沿有效.1: ETI 低电平或下降沿有效.</td></tr><tr><td>14</td><td>SMC1</td><td>SMC 的一部分为了使能外部时钟模式 1</td></tr></table>

在外部时钟模式 1，计数器由ETIF 信号上的任意有效边沿驱动

0：外部时钟模式 1 禁能

当从模式配置为复位模式，暂停模式和事件模式时，定时器仍然可以工作在外部时钟模式 1。但是 TRGS 必须不能为 3’b111。

13:12 ETPSC[1:0] 外部触发预分频外部触发信号 ETIFP 的频率不能超过 TIMER_CK 频率的1/4。当输入较快的外部时钟时，可以使用预分频降低 ETIFP 的频率。00：预分频禁能01：2 分频10：4 分频11：8 分频

外部触发信号可以通过数字滤波器进行滤波，该位域定义了数字滤波器的滤波能力。数字滤波器的基本原理是：以 f 频率连续采样外部触发信号，同时记录采样相同电平的次数。当该次数达到配置的滤波能力时，则认为是一个有效的电平信号。

<table><tr><td>EXTFC[3:0]</td><td>次数</td><td><eq>f_{SAMP}</eq></td></tr><tr><td>4&#x27;b0000</td><td colspan="2">Filter disabled.</td></tr><tr><td>4&#x27;b0001</td><td>2</td><td rowspan="3"><eq>f_{TIMER\_CK}</eq></td></tr><tr><td>4&#x27;b0010</td><td>4</td></tr><tr><td>4&#x27;b0011</td><td>8</td></tr><tr><td>4&#x27;b0100</td><td>6</td><td rowspan="2"><eq>f_{DTS\_CK}/2</eq></td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6</td><td rowspan="2"><eq>f_{DTS\_CK}/4</eq></td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6</td><td rowspan="2"><eq>f_{DTS\_CK}/8</eq></td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5</td><td rowspan="3"><eq>f_{DTS\_CK}/16</eq></td></tr><tr><td>4&#x27;b1011</td><td>6</td></tr><tr><td>4&#x27;b1100</td><td>8</td></tr><tr><td>4&#x27;b1101</td><td>5</td><td rowspan="3"><eq>f_{DTS\_CK}/32</eq></td></tr><tr><td>4&#x27;b1110</td><td>6</td></tr><tr><td>4&#x27;b1111</td><td>8</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>TRGDEN</td><td>保留</td><td>CH3DEN</td><td>CH2DEN</td><td>CH1DEN</td><td>CH0DEN</td><td>UPDEN</td><td>保留</td><td>TRGIE</td><td>保留</td><td>CH3IE</td><td>CH2IE</td><td>CH1IE</td><td>CHOIE</td><td>UPIE</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>14</td><td>TRGDEN</td><td>触发DMA请求使能0:禁止触发DMA请求1:使能触发DMA请求</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>12</td><td>CH3DEN</td><td>通道3比较/捕获DMA请求使能0:禁止通道3比较/捕获DMA请求1:使能通道3比较/捕获DMA请求</td></tr><tr><td>11</td><td>CH2DEN</td><td>通道2比较/捕获DMA请求使能0:禁止通道2比较/捕获DMA请求1:使能通道2比较/捕获DMA请求</td></tr><tr><td>10</td><td>CH1DEN</td><td>通道1比较/捕获DMA请求使能0:禁止通道1比较/捕获DMA请求1:使能通道1比较/捕获DMA请求</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>6</td><td>TRGIE</td><td>触发中断使能0:禁止触发中断1:使能触发中断</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>4</td><td>CH3IE</td><td>通道3比较/捕获中断使能0:禁止通道3中断1:使能通道3中断</td></tr><tr><td>3</td><td>CH2IE</td><td>通道2比较/捕获中断使能0:禁止通道2中断1:使能通道2中断</td></tr><tr><td>2</td><td>CH1IE</td><td>通道1比较/捕获中断使能0:禁止通道1中断1:使能通道1中断</td></tr><tr><td>1</td><td>CH0IE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CH3OF</td><td>CH2OF</td><td>CH1OF</td><td>CH0OF</td><td colspan="2">保留</td><td>TRGIF</td><td>保留</td><td>CH3IF</td><td>CH2IF</td><td>CH1IF</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="3"></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td colspan="2">.</td><td>rc_w0</td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>12</td><td>CH3OF</td><td>通道3捕获溢出标志参见CH0OF描述</td></tr><tr><td>11</td><td>CH2OF</td><td>通道2捕获溢出标志参见CH0OF描述</td></tr><tr><td>10</td><td>CH1OF</td><td>通道1捕获溢出标志参见CH0OF描述</td></tr><tr><td>98:7</td><td>CH0OF保留</td><td>通道1捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0.0:无捕获溢出中断发生必须保持复位值。.</td></tr><tr><td>6</td><td>TRGIF</td><td>触发中断标志当发生触发事件时,此标志会置1,此位由软件清0。当暂停模式使能时,触发输入的任意边沿都可以产生触发事件。否则,其它模式时,仅在触发输入端检测到有效边沿,产生触发事件。0:无触发事件产生1:触发中断产生</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>4</td><td>CH3IF</td><td>通道3比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>3</td><td>CH2IF</td><td>通道2比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>2</td><td>CH1IF</td><td>通道1比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在任何更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>TRGG</td><td>保留.</td><td>CH3G</td><td>CH2G</td><td>CH1G</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="9"></td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>6</td><td>TRGG</td><td>触发事件产生此位由软件置1,由硬件自动清0.当此位被置1,TIMERx_INTF寄存器的TRGIF标志位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:无触发事件产生1:产生触发事件</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>4</td><td>CH3G</td><td>通道3捕获或比较事件发生参见CH0G描述</td></tr><tr><td>3</td><td>CH2G</td><td>通道2捕获或比较事件发生参见CH0G描述</td></tr><tr><td>2</td><td>CH1G</td><td>通道1捕获或比较事件发生参见CH0G描述</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,如果选择了中央对齐或向上计数模式,计数器被清0。否则(向下计数模式)计数器将载入自动重载值,预分频计数器将同时被清除。0:无更新事件产生1:产生更新事件</td></tr></table>

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>CH1COMCTL[3]</td><td colspan="7">保留</td><td>CH0COMCTL[3]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH1COMCEN</td><td colspan="3">CH1COMCTL[2:0]</td><td>CH1COMSEN</td><td>CH1COMFEN</td><td rowspan="2" colspan="2">CH1MS[1:0]</td><td>CH0COMCEN</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH1CAPFLT[3:0]</td><td colspan="2">CH1CAPPSC[1:0]</td><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr><tr><td colspan="4">Rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

输出比较模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>24</td><td>CH1COMCTL[3]</td><td>参见 CH1COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>16</td><td>CH0COMCTL[3]</td><td>参见 CH0COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH1COMCEN</td><td>通道 1 输出比较清 0 使能参见 CH0COMCEN 描述</td></tr><tr><td>14:12</td><td>CH1COMCTL[2:0]</td><td>通道 1 输出比较模式参见 CH0COMCTL 描述</td></tr><tr><td>11</td><td>CH1COMSEN</td><td>通道 1 输出比较影子寄存器使能参见 CH0COMSEN 描述</td></tr><tr><td>10</td><td>CH1COMFEN</td><td>通道 1 输出比较快速使能参见 CH0COMFEN 描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道 1 模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH1EN 位被清 0)时这些位才可以写。00:通道 1 配置为输出01:通道 1 配置为输入,IS1 映射在 CI1FE1 上10:通道 1 配置为输入,IS1 映射在 CI0FE1 上11:通道 1 配置为输入,IS1 映射在 ITS 上,此模式仅工作在内部触发器输入被选中时(由 SYSCFG_TIMER2CFG)寄存器中的 TSCFGx[2:0] (x = 3,4,5,6,7)位域选择)。</td></tr><tr><td>7</td><td>CH0COMCEN</td><td>通道 0 输出比较清 0 使能当此位被置 1,当检测到 ETIFP 信号输入高电平时,O0CPRE 参考信号被清 00:禁止通道 0 输出比较清零1:使能通道 0 输出比较清零</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道 0 输出比较模式此位定义了 O0CPRE 的动作,而 O0CPRE 决定了 CH0_O、CH0_ON 的值。O0CPRE 高电平有效,而 CH0_O、CH0_ON 的有效电平取决于 CH0P、CH0NP 位。0000:时基。输出比较寄存器 TIMERx_CH0CV 与计数器 TIMERx_CNT 间的比较对 O0CPRE 不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时,强制 O0CPRE 翻转。0100:强制为低。强制 O0CPRE 为低电平0101:强制为高。强制 O0CPRE 为高电平0110:PWM 模式 0。在向上计数时,一旦计数器值小于 TIMERx_CH0CV 时,O0CPRE 为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于 TIMERx_CH0CV</td></tr></table>

时，O0CPRE 为无效电平，否则为有效电平。

0111：PWM模式1。在向上计数时，一旦计数器值小于TIMERx_CH0CV时，O0CPRE为无效电平，否则为有效电平。在向下计数时，一旦计数器的值大于 TIMERx_CH0CV时，O0CPRE 为有效电平，否则为无效电平。

在 PWM 模式 0 或 PWM 模式 1 中，只有当比较结果改变了或者输出比较模式中从时基模式切换到 PWM模式时，O0CPRE 电平才改变。

当 TIMERx_CCHP 寄存器的 PROT[1：0]=11 且 CH0MS =00（比较模式）时，此位不能被改变。

1000: 可再次触发单脉冲模式 0。 O0CPRE 工作在 PWM 模式 0，向上计数时，O0CPRE 有效，当外部触发信号产生时，O0CPRE 无效，在下次更新事件产生后，O0CPRE 恢复有效。向下计数时，O0CPRE 无效，当外部触发信号产生时，O0CPRE有效，在下次更新事件产生后，O0CPRE 恢复无效。

1001: 可再次触发单脉冲模式 1。 O0CPRE 工作在 PWM 模式 1，向上计数时，O0CPRE 无效，当外部触发信号产生时，O0CPRE 有效，在下次更新事件产生后，

O0CPRE 恢复无效。向下计数时，O0CPRE 有效，当外部触发信号产生时，O0CPRE无效，在下次更新事件产生后，O0CPRE 恢复有效。

## 1010:保留

1011:保留

1100:复合 PWM0 模式。O0CPRE 工作在 PWM 模式 0，O0CPREC 输出结果是O0CPRE 和 O1CPRE 的逻辑“或”。

1101:复合 PWM1 模式。O0CPRE 工作在 PWM 模式 1，O0CPREC 输出结果是O0CPRE 和 O1CPRE 的逻辑“与”。

1110: 非对称PWM0 模式。O0CPRE工作在PWM模式0，在向上计数时，O0CPREC输出结果是 O0CPRE，向下计数时输出 O1CPRE。

1111 非对称 PWM1 模式。O0CPRE 工作在 PWM 模式 1，在向上计数时，O0CPREC输出结果是 O0CPRE，向下计数时输出 O1CPRE。

当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 且 CH0MS =000（比较模式）时，此位不能被改变。

当此位被置 1，TIMERx_CH0CV 寄存器的影子寄存器被使能，影子寄存器在每次更新事件时都会被更新。

仅在单脉冲模式下（SPM =1），可以在未确认影子寄存器的情况下使用 PWM模式当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 且 CH0MS =00 时此位不能被改变。

## CH0COMFEN 通道 0 输出比较快速使能


输入捕获模式:


00：通道 0 配置为输出

01：通道 0 配置为输入，IS0映射在 CI0FE0 上

10：通道 0 配置为输入，IS0映射在 CI1FE0 上

11：通道 0 配置为输入，IS0 映射在 ITS 上，此模式仅工作在内部触发器输入被选中时（由 SYSCFG_TIMER2CFG）寄存器中的 TSCFGx[2:0] (x = 3,4,5,6,7)位域选择）。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td><td></td><td></td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td><td></td><td></td></tr><tr><td>15:12</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述</td><td></td><td></td></tr><tr><td>11:10</td><td>CH1CAPPSC[1:0]</td><td>通道1输入捕获预分频器参见CH0CAPPSC描述</td><td></td><td></td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择与输出模式相同</td><td></td><td></td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制CI0输入信号可以通过数字滤波器进行滤波,该位域配置滤波参数。数字滤波器的基本原理:根据<eq>f_{SAMP}</eq>对CI0输入信号进行连续采样,并记录信号相同电平的次数。达到该位配置的滤波参数后,认为是有效电平。滤波器参数配置如下:</td><td></td><td></td></tr><tr><td rowspan="17" colspan="2"></td><td>CH0CAPFLT [3:0]</td><td>采样次数<eq>f_{SAMP}</eq></td><td></td></tr><tr><td>4&#x27;b0000</td><td>无滤波器</td><td></td></tr><tr><td>4&#x27;b0001</td><td>2<eq>f_{CK\_TIMER}</eq></td><td rowspan="15"></td></tr><tr><td>4&#x27;b0010</td><td>4</td></tr><tr><td>4&#x27;b0011</td><td>8</td></tr><tr><td>4&#x27;b0100</td><td>6<eq>f_{DTS}/2</eq></td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6<eq>f_{DTS}/4</eq></td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6<eq>f_{DTS}/8</eq></td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5<eq>f_{DTS}/16</eq></td></tr><tr><td>4&#x27;b1011</td><td>6</td></tr><tr><td>4&#x27;b1100</td><td>8</td></tr><tr><td>4&#x27;b1101</td><td>5<eq>f_{DTS}/32</eq></td></tr><tr><td>4&#x27;b1110</td><td>6</td></tr><tr><td>4&#x27;b1111</td><td>8</td></tr><tr><td>3:2</td><td>CH0CAPPSC[1:0]</td><td colspan="2">通道0输入捕获预分频器这2位定义了通道0输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH0EN</td><td></td></tr></table>

这 2 位定义了通道 0 输入的预分频系数。当 TIMERx_CHCTL2 寄存器中的 CH0EN=0 时，则预分频器复位。

00：无预分频器，捕获输入口上检测到的每一个边沿都触发一次捕获

01：每 2 个事件触发一次捕获

10：每 4 个事件触发一次捕获

11：每 8 个事件触发一次捕获

1:0 CH0MS[1:0] 通道 0 模式选择

## 通道控制寄存器 1（TIMERx_CHCTL1）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>CH3COMCTL[3]</td><td colspan="7">保留</td><td>CH2COMCTL[3]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3COM CEN</td><td colspan="3">CH3COMCTL[2:0]</td><td>CH3COM SEN</td><td>CH3COM FEN</td><td rowspan="2" colspan="2">CH3MS[1:0]</td><td>CH2COM CEN</td><td colspan="3">CH2COMCTL[2:0]</td><td>CH2COM SEN</td><td>CH2COM FEN</td><td rowspan="2" colspan="2">CH2MS[1:0]</td></tr><tr><td colspan="4">CH3CAPFLT[3:0]</td><td colspan="2">CH3CAPPSC[1:0]</td><td colspan="4">CH2CAPFLT[3:0]</td><td colspan="2">CH2CAPPSC[1:0]</td></tr><tr><td colspan="4">Rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

## 输出比较模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>24</td><td>CH3COMCTL[3]</td><td>参见 CH3COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>16</td><td>CH2COMCTL[3]</td><td>参见 CH2COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH3COMCEN</td><td>通道 3 输出比较清 0 使能参见 CH0COMCEN 描述</td></tr><tr><td>14:12</td><td>CH3COMCTL[2:0]</td><td>通道 3 输出比较模式参见 CH0COMCTL 描述</td></tr><tr><td>11</td><td>CH3COMSEN</td><td>通道 3 输出比较影子寄存器使能参见 CH0COMSEN 描述</td></tr><tr><td>10</td><td>CH3COMFEN</td><td>通道 3 输出比较快速使能参见 CH0COMFEN 描述</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道 3 模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH3EN 位被清 0)时这些位才可以写。00:通道 3 配置为输出01:通道 3 配置为输入,IS3 映射在 CI3FE3 上</td></tr></table>

10：通道 3 配置为输入，IS3映射在 CI2FE3 上11：通道 3 配置为输入，IS3 映射在 ITS 上，此模式仅工作在内部触发器输入被选中时（由 SYSCFG_TIMER2CFG）寄存器中的 TSCFGx[2:0] (x = 3,4,5,6,7)位域选择）。

7 CH2COMCEN 通道 2 输出比较清0 使能当此位被置 1，当检测到 ETIFP 输入高电平时，O2CPRE 参考信号被清 00：使能通道 2 输出比较清零1：禁止通道 2 输出比较清零

## 6:4 CH2COMCTL[2:0] 通道 2 输出比较模式

此位定义了 O2CPRE 的动作，而 O2CPRE 决定了 CH2_O、CH2_ON 的值。O2CPRE高电平有效，而 CH2_O、CH2_ON 的有效电平取决于 CH2P、CH2NP 位。0000：时基。输出比较寄存器 TIMERx_CH2CV 与计数器 TIMERx_CNT 间的比较对O2CPRE 不起作用0001：匹配时设置为高。当计数器的值与捕获/比较值寄存器 TIMERx_CH2CV 相同时，强制 O2CPRE 为高。0010：匹配时设置为低。当计数器的值与捕获/比较值寄存器 TIMERx_CH2CV 相同时，强制 O2CPRE 为低。0011：匹配时翻转。当计数器的值与捕获/比较值寄存器 TIMERx_CH2CV 相同时，强制 O2CPRE 翻转。0100：强制为低。强制 O2CPRE 为低电平0101：强制为高。强制 O2CPRE 为高电平

1000:可再次触发单脉冲模式 0。 O2CPRE 工作在 PWM 模式 0，向上计数时，O2CPRE 有效，当外部触发信号产生时，O2CPRE 无效，在下次更新事件产生后，O2CPRE 恢复有效。向下计数时，O2CPRE 无效，当外部触发信号产生时，O2CPRE有效，在下次更新事件产生后，O2CPRE 恢复无效。

1001: 可再次触发单脉冲模式 1。 O2CPRE 工作在 PWM 模式 1，向上计数时，O2CPRE 无效，当外部触发信号产生时，O2CPRE 有效，在下次更新事件产生后，O2CPRE 恢复无效。向下计数时，O2CPRE 有效，当外部触发信号产生时，O2CPRE无效，在下次更新事件产生后，O2CPRE 恢复有效。

1010:保留

1011:保留

1100:复合 PWM0 模式。O2CPRE 工作在 PWM 模式 0，O2CPREC 输出结果是O2CPRE 和 O3CPRE 的逻辑“或”。

1101:复合 PWM1 模式。O2CPRE 工作在 PWM 模式 1，O2CPREC 输出结果是

<table><tr><td></td><td></td><td>O2CPRE和O3CPRE的逻辑“与”。1110:非对称PWM0模式。O2CPRE工作在PWM模式0,在向上计数时,O2CPREC输出结果是O2CPRE,向下计数时输出O3CPRE。1111非对称PWM1模式。O2CPRE工作在PWM模式1,在向上计数时,O2CPREC输出结果是O2CPRE,向下计数时输出O3CPRE。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH2MS=000(比较模式)时,此位不能被改变。</td></tr><tr><td>3</td><td>CH2COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH2CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道2输出/比较影子寄存器1:使能通道2输出/比较影子寄存器仅在单脉冲模式下(SPM=1),可以在未确认影子寄存器情况下使用PWM模式当TIMERx_CCHP寄存器的PROT[1:0]=11且CH2MS=00时此位不能被改变。</td></tr><tr><td>2</td><td>CH2COMFEN</td><td>通道2输出比较快速使能当该位为1时,如果通道配置为PWM0模式或者PWM1模式,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH2_O被设置为比较电平而与比较结果无关。0:通道2输出比较快速禁能。仅比较结果输入作为有效边沿时会产生比较匹配,并将CH2_O设置为比较电平,激活CH2_O输出的最小延时为5个时钟周期。1:通道2输出比较快速使能。触发输入信号的有效边沿和比较结果都会产生比较匹配,并将CH2_O设置为比较电平。当触发信号的输入作为有效边沿时,激活CH2_O输出的最小延时为3个时钟周期。</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td>通道2I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH2EN位被清0)时这些位才可写。00:通道2配置为输出01:通道2配置为输入,IS2映射在CI2FE2上10:通道2配置为输入,IS2映射在CI3FE2上11:通道2配置为输入,IS2映射在ITS上,此模式仅工作在内部触发器输入被选中时(由SYSCFG_TIMER2CFG)寄存器中的TSCFGx[2:0](x=3,4,5,6,7)位域选择)。</td></tr></table>

输入捕获模式:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>CH3CAPFLT[3:0]</td><td>通道3输入捕获滤波控制参见CH0CAPFLT描述</td></tr><tr><td>11:10</td><td>CH3CAPPSC[1:0]</td><td>通道3输入捕获预分频器参见CH0CAPPSC描述</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择</td></tr></table>

## 与输出模式相同

<table><tr><td rowspan="18">7:4</td><td rowspan="18">CH2CAPFLT[3:0]</td><td colspan="3">通道2输入捕获滤波控制CI2输入信号可以通过数字滤波器进行滤波,该位域配置滤波参数。数字滤波器的基本原理:根据<eq>f_{SAMP}</eq>对CI2输入信号进行连续采样,并记录信号相同电平的次数。达到该位配置的滤波参数后,认为是有效电平。滤波器参数配置如下:</td></tr><tr><td>CH2CAPFLT [3:0]</td><td>采样次数</td><td><eq>f_{SAMP}</eq></td></tr><tr><td>4&#x27;b0000</td><td colspan="2">无滤波器</td></tr><tr><td>4&#x27;b0001</td><td>2</td><td rowspan="3"><eq>f_{CK\_TIMER}</eq></td></tr><tr><td>4&#x27;b0010</td><td>4</td></tr><tr><td>4&#x27;b0011</td><td>8</td></tr><tr><td>4&#x27;b0100</td><td>6</td><td rowspan="2"><eq>f_{DTS}/2</eq></td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6</td><td rowspan="2"><eq>f_{DTS}/4</eq></td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6</td><td rowspan="2"><eq>f_{DTS}/8</eq></td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5</td><td rowspan="3"><eq>f_{DTS}/16</eq></td></tr><tr><td>4&#x27;b1011</td><td>6</td></tr><tr><td>4&#x27;b1100</td><td>8</td></tr><tr><td>4&#x27;b1101</td><td>5</td><td rowspan="3"><eq>f_{DTS}/32</eq></td></tr><tr><td>4&#x27;b1110</td><td>6</td></tr><tr><td>4&#x27;b1111</td><td>8</td></tr><tr><td>3:2</td><td>CH2CAPPSC[1:0]</td><td colspan="3">通道2输入捕获预分频器这2位定义了通道2输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH2EN=0时,则预分频器复位。00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获01:每2个事件触发一次捕获10:每4个事件触发一次捕获11:每8个事件触发一次捕获</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td colspan="3">通道2模式选择与输出比较模式相同</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3NP</td><td>保留</td><td>CH3P</td><td>CH3EN</td><td>CH2NP</td><td>保留</td><td>CH2P</td><td>CH2EN</td><td>CH1NP</td><td>保留</td><td>CH1P</td><td>CH1EN</td><td>CH0NP</td><td>保留</td><td>CH0P</td><td>CH0EN</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CH3NP</td><td>通道3互补输出极性参考CH0NP描述</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>CH3P</td><td>通道3极性参考CH0P描述</td></tr><tr><td>12</td><td>CH3EN</td><td>通道3使能参考CH0EN描述</td></tr><tr><td>11</td><td>CH2NP</td><td>通道2互补输出极性参考CH0NP描述</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CH2P</td><td>通道2极性参考CH0P描述</td></tr><tr><td>8</td><td>CH2EN</td><td>通道2使能参考CH0EN描述</td></tr><tr><td>7</td><td>CH1NP</td><td>通道1互补输出极性参考CH0NP描述</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CH1P</td><td>通道1极性参考CH0P描述</td></tr><tr><td>4</td><td>CH1EN</td><td>通道1使能参考CH0EN描述</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,该位保持0。当通道0配置为输入模式时,此位和CH0P联合使用,作为输入信号CI0的极性选择控制信号。当TIMERxCCHP寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0P</td><td>通道0极性当通道0配置为输出模式时,此位定义了输出信号极性。0:通道0高电平为有效电平1:通道0低电平为有效电平当通道0配置为输入模式时,此位定义了CI0信号极性</td></tr></table>

[CH0NP， CH0P] 将选择 CI0FE0 或者 CI1FE0 的有效边沿或者捕获极性

[CH0NP==0， CH0P==0]：把 CixFE0 的上升沿作为捕获或者从模式下触发的有效信号，并且 CixFE0 不会被翻转。

[CH0NP==0， CH0P==1]：把 CixFE0 的下降沿作为捕获或者从模式下触发的有效信号，并且 CixFE0 会被翻转。

$$
[ \mathrm{CH0NP} = = 1, \quad \mathrm{CH0P} = = 0 ]: \text {保留。}
$$

[CH0NP==1， CH0P==1]：把 CixFE0 的上升沿和下降沿都作为捕获或者从模式下触发的有效信号，并且 CixFE0 不会被翻转。

当 $\mathsf { T I M E R x \_ C C H P }$ 寄存器的 PROT [1:0]=11 或 10 时此位不能被更改。

当通道 0 配置为输出模式时，将此位置 1 使能 CH0_O 信号有效。当通道 0 配置为输入模式时，将此位置 1 使能通道 0 上的捕获事件。

1：使能通道 0

## 计数器寄存器（TIMERx_CNT）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>

## 预分频寄存器（TIMERx_PSC）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值计数器时钟等于 TIMER_CK 时钟除以(PSC+1),每次当更新事件产生时,PSC 的值被装入到对应的影子寄存器。</td></tr></table>

## 计数器自动重载寄存器（TIMERx_CAR）

地址偏移：0x2C

复位值：0x0000 FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。</td></tr></table>

## 通道 0 捕获/比较值寄存器（TIMERx_CH0CV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄</td></tr></table>

存器后，影子寄存器值随每次更新事件更新。

## 通道 1 捕获/比较值寄存器（TIMERx_CH1CV）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH1VAL[15:0]</td><td>通道1的捕获或比较值当通道1配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 2 捕获/比较值寄存器（TIMERx_CH2CV）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH2VAL[15:0]</td><td>通道2的捕获或比较值当通道2配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 3 捕获/比较值寄存器（TIMERx_CH3CV）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH3VAL[15:0]</td><td>通道3的捕获或比较值当通道3配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道3配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="5">DMATC[4:0]</td><td colspan="3">保留</td><td colspan="5">DMATA [4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>12:8</td><td>DMATC [4:0]</td><td>DMA传输计数该位域定义了DMA访问(读写)TIMERx_DMATB寄存器的数量n,n=(DMATC[4:0]+1).DMATC [4:0]从5&#x27;b0_0000到5&#x27;b1_0001.</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DMATA [4:0]</td><td>DMA传输起始地址该位域定义了DMA访问TIMERx_DMATB寄存器的第一个地址。当通过TIMERx_DMA第一次访问时,访问的就是该位域指定的地址。第二次访问</td></tr></table>

TIMERx_DMATB 时，将访问起始地址+0x4。

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>15:0</td><td>DMATB [15:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

