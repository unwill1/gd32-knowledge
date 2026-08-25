## 23.4.5. TIMERx 寄存器（x = 15 / 16）

TIMER15 基地址：0x4001 4400

TIMER16 基地址：0x4001 4800

控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ADMEN</td><td>UPIFBUEN</td><td>保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="3">保留</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td></td><td colspan="2">rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ADMEN</td><td>微调模式使能0:微调模式禁能1:微调模式使能注意:该位只能在CEN位为0时修改。</td></tr><tr><td>11</td><td>UPIFBUEN</td><td>UPIF位备份使能0:备份禁能。UPIF位没有备份到TIMERx_CNT寄存器中的UPIFBU位1:备份使能。UPIF位备份到TIMERx_CNT寄存器中的UPIFBU位</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(TIMER_CK)与死区时间和采样时钟(DTS)之间的分频系数,死区发生器和数字滤波器会用到DTS时间。00:<eq>f_{DTS}=f_{TIMER\_CK}</eq>01:<eq>f_{DTS}=f_{TIMER\_CK}/2</eq>10:<eq>f_{DTS}=f_{TIMER\_CK}/4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能TIMERx_CAR寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0:更新事件发生后,计数器继续计数1:在下一次更新事件发生时,CEN 硬件清零并且计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该为,选择更新事件源.0:使能后,下述任一事件产生更新中断或DMA请求:-UPG位被置1-计数器上溢-从模式控制器产生的更新1:使能后只有计数器上溢才产生更新中断或DMA请求</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新该位用来使能或禁能更新事件的产生0:更新事件使能.当以下事件之一发生时,更新事件产生,具有缓存的寄存器被装入它们的预装载值:-UPG位被置1-计数器上溢-从模式控制器产生一个更新事件1:更新事件禁能。带有缓存的寄存器保持原有值,如果UPG位被置1或者从模式控制器产生一个硬件复位事件,计数器和预分频器被重新初始化</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0:计数器禁能1:计数器使能在软件将CEN位置1后,外部时钟、暂停模式和译码器模式才能工作。触发模式可以自动地通过硬件设置CEN位。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CCUC[2:1]</td><td colspan="14">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>ISO0N</td><td>ISO0</td><td colspan="4">保留</td><td>DMAS</td><td>CCUC[0]</td><td>保留</td><td>CCSE</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CCUC[2:1]</td><td>换相控制影子寄存器更新控制请参考 CCUC [0]的描述。</td></tr><tr><td>29:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>ISO0N</td><td>多模式通道 0 的互补通道空闲状态输出0:当 POEN 复位,MCH0_O 输出低电平1:当 POEN 复位,MCH0_O 输出高电平此位只有在 TIMERx_CCHP0 寄存器的 PROT [1:0]位为 00 的时候可以被更改。</td></tr><tr><td>8</td><td>ISO0</td><td>通道 0 的空闲状态输出0:当 POEN 复位,CH0_O 输出低电平1:当 POEN 复位,CH0_O 输出高电平如果 MCH0_O 生效,一个死区时间后 CH0_O 输出改变。此位只有在 TIMERx_CCHP0 寄存器的 PROT[1:0]位为 00 的时候可以被更改。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>DMAS</td><td>DMA请求源选择0:当通道捕获/比较事件发生时,发送通道 CHx / MCHx 的 DMA 请求1:当更新事件发生,发送通道 CHx / MCHx 的 DMA 请求</td></tr><tr><td>2</td><td>CCUC</td><td>换相控制影子寄存器更新控制当换相控制影子寄存器(CHxEN,MCHxEN 和 CHxCOMCTL 位)使能(CCSE = 1),这些影子寄存器更新控制如下:000:CMTG 位被置 1 时,更新影子寄存器001:保留100:当计数器上溢事件发生时,影子寄存器更新其他值:保留当通道没有互补输出时,此位无效。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CCSE</td><td>换相控制影子使能0:影子寄存器 CHxEN、MCHxEN 和 CHxCOMCTL 位禁能.1:影子寄存器 CHxEN、MCHxEN 和 CHxCOMCTL 位使能.如果这些位已经被写入了,换相事件到来时这些位才被更新当通道没有互补输出时,此位无效</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>MCH0DEN</td><td colspan="3">保留</td><td>MCH0IE</td><td colspan="4">保留</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CH0DEN</td><td>UPDEN</td><td>BRKIE</td><td>保留</td><td>CMTIE</td><td colspan="3">保留</td><td>CH0IE</td><td>UPIE</td></tr><tr><td colspan="7">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>MCH0DEN</td><td>多模式通道0比较/捕获DMA请求使能0:禁止多模式通道0比较/捕获DMA请求1:使能多模式通道0比较/捕获DMA请求注意:此DMA使能位仅用于多模式通道输入和输出独立模式(当MCH0MSEL[1:0]=2'b00时)。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>MCH0IE</td><td>多模式通道0比较/捕获中断使能0:禁止多模式通道0中断1:使能多模式通道0中断注意:此中断使能位仅用于多模式通道输入和输出独立模式(当MCH0MSEL[1:0]=2'b00时)。</td></tr><tr><td>19:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>BRKIE</td><td>中止中断使能0:禁止中止中断1:使能中止中断</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CMTIE</td><td>换相更新中断使能0:禁止换相更新中断1:使能换相更新中断</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>MCH0OF</td><td colspan="3">保留</td><td>MCH0IF</td><td colspan="4">保留</td></tr><tr><td colspan="10">rc_w0</td><td colspan="6">rc_w0</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CH0OF</td><td>保留</td><td>BRK0IF</td><td>保留</td><td>CMTIF</td><td colspan="3">保留</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="7">rc_w0</td><td>rc_w0</td><td colspan="6">rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>MCH0OF</td><td>多模式通道0捕获溢出标志当通道0被配置为输入模式时,在MCH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0。0:无捕获溢出中断发生1:捕获溢出中断发生</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>MCH0IF</td><td>多模式通道0比较/捕获中断标志此标志由硬件置1软件清0。当多模式通道0用于输入模式时,捕获事件发生时此标志位置1;当多模式通道0用于输出模式时,此标志位在一个比较事件发生时置1。当多模式通道0在输入模式下时,通过读TIMERx_MCH0CV寄存器可以清零该位。0:无多模式通道0中断发生1:多模式通道0中断发生</td></tr><tr><td>19:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0。0:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>BRK0IF</td><td>BREAK0中断标志位一旦BREAK0输入有效,由硬件对该位置1。如果BREAK0输入无效,则该位可由软件清0。0:无BREAK0事件产生1:BREAK0输入上检测到有效电平</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CMTIF</td><td>通道换相更新中断标志当通道换相更新事件发生时此标志位被硬件置1,此位由软件清0。0:无通道换相更新中断发生1:通道换相更新中断发生</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。当通道0在输入模式下时,通过读TIMERx_CH0CV寄存器可以清零该位。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在任何更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>MCH0G</td><td colspan="4">保留</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>BRK0G</td><td>保留</td><td>CMTG</td><td colspan="3">保留</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="8">w</td><td colspan="6">w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>MCH0G</td><td>多模式通道0互补捕获或比较事件发生该位由软件置1,用于在多模式通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,MCH0IF标志位被置1,若开启相应的中断和DMA,则发出相应的中断和DMA请求。此外,如果多模式通道0配置为输入模式,计数器的当前值被TIMERx_MCH0CV寄存器捕获,如果MCH0IF标志位已经为1,则MCH0OF标志位被置1。0:不产生多模式通道0捕获或比较事件1:发生多模式通道0捕获或比较事件</td></tr><tr><td>19:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>BRK0G</td><td>产生BREAK0事件该位由软件置1,用于产生一个BREAK0事件,由硬件自动清0。当此位被置1时,POEN位被清0且BRK0IF位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:不产生BREAK0事件1:产生BREAK0事件</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CMTG</td><td>通道换相更新事件发生此位由软件置1,由硬件自动清0.当此位被置1,通道捕获/比较控制寄存器(CHxEN、MCHxEN和CHxCOMCTL)的互补输出被更新(根据TIMERx_CTL1中CCSE值)。0:不产生通道控制更新事件1:产生通道控制更新事件</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,向上计数模式,计数器被清0,预分频计数器将同时被清除。0:无更新事件产生1:产生更新事件</td></tr></table>

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">保留</td><td rowspan="2">CH0MS[2]</td><td rowspan="2" colspan="13">保留</td><td>CH0COMCTL[3]</td></tr><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="8">保留</td><td>CH0COMCEN</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td colspan="2">保留</td><td rowspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="3">CH0CAPPSC[1:0]</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>CH0MS[2]</td><td>通道 0 I/O 模式选择参考 CH0MS[1:0]描述。</td></tr><tr><td>29:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CH0COMCTL[3]</td><td>通道 0 输出比较控制参见 CH0COMCTL[2:0]描述</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>CH0COMCEN</td><td>通道 0 输出比较清 0 使能当此位被置 1,当检测到 ETIFP 输入高电平时,O0CPRE 参考信号被清 0。0:禁止通道 0 输出比较清零1:使能通道 0 输出比较清零</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式CH0COMCTL[3]和CH0COMCTL[2:0]位域定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O的值。O0CPRE高电平有效,而CH0_O的有效电平取决于CHOP位。注意:当多模式通道0配置为输出模式,且MCH0MSEL[1:0]=2'b11时,CH0COMCTL[3]和CH0COMCTL[2:0]位域定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O、MCH0_O的值。O0CPRE高电平有效,CH0_O、MCH0_O的有效电平取决于CHOP、MCHOP位。0000:时基。输出比较寄存器TIMERx_CH0CV与计数器TIMERx_CNT间的比较对O0CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE翻转。0100:强制为低。强制O0CPRE为低电平0101:强制为高。强制O0CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为有效电平,否则为无效电平。1000~1111:保留注意:在PWM模式0或PWM模式1中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,O0CPRE电平才改变。当CH0和MCH0输出互补时,该位域预装载。若CCSE=1,则该位域只在通道换相事件发生时更新。当TIMERx_CCHP0寄存器的PROT[1:0]=11且CH0MS=000(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>CH0COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0输出比较影子寄存器1:使能通道0输出比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式当 TIMERx_CCHP0 寄存器的 PROT [1:0]=11 且 CH0MS =000 时此位不能被改变。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道 0 I/O 模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(当 MCH0MSEL[1:0] = 2'b00 时,TIMERx_CHCTL2 寄存器的 CH1EN 位清 0;当 MCH0MSEL[1:0] = 2'b01 或 2'b11 时,TIMERx_CHCTL2 寄存器的 CH0EN、MCH0EN 位清 0)时,CH0MS[2:0]才可写。000:通道 0 配置为输出001:通道 0 配置为输入,ISO 映射在 CI0FE0 上010:保留011:保留100:通道 0 配置为输入,ISO 映射在 MCI0FE0 上101~111:保留</td></tr></table>

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述。</td></tr><tr><td>29:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了CIO输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=20010:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=40011:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=80100:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=60101:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=80110:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=60111:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=81000:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=61001:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=81010:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=51011:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=61100:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=81101:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=51110:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=61111: fsAMP=fDTS/32, N=8</td></tr><tr><td>3:2</td><td>CH0CAPPSC[1:0]</td><td>通道0输入捕获预分频器这2位定义了通道0输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH0EN=0时,则预分频器复位。00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获01:每2个事件触发一次捕获10:每4个事件触发一次捕获11:每8个事件触发一次捕获</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道0模式选择与输出比较模式相同。</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>MCHOP</td><td>MCH0EN</td><td>CHOP</td><td>CH0EN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>MCH0P</td><td>多模式通道0捕获/比较极性当通道0配置为输出模式,且MCH0MSEL[1:0]=2'b11时,此位定义了多模式通道0输出信号MCH0_O的极性。0:多模式通道0高电平有效1:多模式通道0低电平有效当通道0配置为输入模式时,此位和CHOP联合使用,作为通道0的极性选择控制信号。当TIMERx_CCHP0寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr><tr><td>2</td><td>MCH0EN</td><td>多模式通道0捕获/比较使能当多模式通道0配置为输出模式时,将此位置1使能MCH0_O信号有效。当多模式通道0配置为输入模式时,将此位置1使能多模式通道0上的捕获事件。0:禁止多模式通道01:使能多模式通道0</td></tr><tr><td>1</td><td>CHOP</td><td>通道0捕获/比较极性当通道0配置为输出模式时,此位定义了输出信号极性。0:通道0高电平有效1:通道0低电平有效当通道0配置为输入模式时,此位定义了通道0输入信号的极性。[MCHOP, CHOP]用于选择通道0输入信号有效边沿或者捕获极性。00:把通道0输入信号的上升沿作为捕获或者从模式下触发的有效信号,且通道0输入信号不会被翻转。01:把通道0输入信号的下降沿作为捕获或者从模式下触发的有效信号,且通道0输入信号会被翻转。10:保留。11:把通道0输入信号的上升沿和下降沿都作为捕获或者从模式下触发的有效信号,且通道0输入信号不翻转。当TIMERxCCHP0寄存器的PROT [1:0]=11或10时此位不能被更改。</td></tr><tr><td>0</td><td>CHOEN</td><td>通道0捕获/比较使能当通道0配置为输出模式时,将此位置1使能CHO_O信号有效。当通道0配置为输入模式时,将此位置1使能通道0上的捕获事件。0:禁止通道01:使能通道0</td></tr></table>

## 计数器寄存器（TIMERx_CNT）

地址偏移：0x24

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UPIFBU</td><td colspan="15">保留</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UPIFBU</td><td>UPIF位备份该位只读,是 TIMERx_INTF 寄存器的 UPIF 位的备份值。当 UPIFBUEN = 1 时,该位有效,若 UPIFBUEN =0,该位保留,读取该位值为零。</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。当 PWMADMEN = 0 时,该位域表示当前计数器的值。写操作该位域可以改变计数器的值。当 PWMADMEN = 1 时,该位域仅用于表示计数器值的整数部分,不包含小数部分。</td></tr></table>

预分频寄存器（TIMERx_PSC）

地址偏移： 0x28

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值</td></tr><tr><td></td><td></td><td>计数器时钟等于PSC时钟除以(PSC+1),每次当更新事件产生时,PSC的值被装入当前预分频寄存器。</td></tr></table>

计数器自动重载寄存器（TIMERx_CAR）

地址偏移：0x2C

复位值：0x0000 FFFF

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CARL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CARL[19:16]</td><td>计数器自动重载值(16位至19位)当PWMADMEN=0时,CARL[19:16]位域值0000。当PWMADMEN=1时,CARL[19:16]位域用于表示自动重载值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值(0位至15位)这些位定义了计数器的自动重载值。当PWMADMEN=0时,CARL[15:0]位域用于表示计数器的自动重载值。当PWMADMEN=1时,CARL[15:0]位域用于表示自动重载值的整数部分。</td></tr></table>

## 重复计数寄存器 0（TIMERx_CREP0）

地址偏移：0x30

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>CREP0[7:0]</td><td>重复计数器值 0这些位定义了更新事件的产生速率。重复计数器计数值减为 0 时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。注意:当 TIMERx_CFG 寄存器中的 CREPSEL =0 时,使用该位。</td></tr></table>

## 通道 0 捕获/比较寄存器（TIMERx_CH0CV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CH0VAL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>31:28</td><td>CH0VAL[19:16]</td><td>通道0的捕获或比较值(16位到19位)当通道0配置为输入模式时,CH0VAL[19:16]位域值为0000。当通道0配置为输出模式时,该位域包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH0VAL[19:16]位域值为0000。当PWMADMEN=1时,CH0VAL[19:16]位域用于表示比较值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值(0位至15位)当通道0配置为输入模式时,CH0VAL[15:0]决定了上次捕获事件的计数器值,且该位域只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH0VAL[15:0]位域值表示比较值。当PWMADMEN=1时,CH0VAL[15:0]位域用于表示比较值的整数部分。</td></tr></table>

## 互补通道保护寄存器 0（TIMERx_CCHP0）

地址偏移：0x44

复位值：0x0000 0000

该寄存器通过字访问（32位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>BRK0LK</td><td>保留</td><td>BRK0REL</td><td colspan="6">保留</td><td colspan="4">BRK0F[3:0]</td></tr><tr><td></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="7">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>POEN</td><td>OAEN</td><td>BRK0P</td><td>BRK0EN</td><td>ROS</td><td>IOS</td><td colspan="2">PROT[1:0]</td><td colspan="8">DTCFG[7:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>BRK0LK</td><td>BREAK0输入锁存0:BREAK0输入为输入模式1:BREAK0输入为锁存模式当BRK0LK置1时,BREAK0输入配置为开漏输出模式。任何有效的BREAK0事件都会拉低BREAK0输入引脚电平,用于向外部设备提示有内部BREAK0事件发生。此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。注意:对该位的每一次写操作,需要延时1个APB时钟才有效。</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>BRK0REL</td><td>BREAK0输入释放当BREAK0输入无效时,该位由硬件清零。0: BREAK0输入锁存1: BREAK0输入释放当软件将该位置1时,将释放锁存输出控制(高阻态的开漏模式)。当BREAK0事件无效时,该位由硬件清零。注意:对该位的每一次写操作,需要延时1个APB时钟才有效。</td></tr><tr><td>25:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>BRK0F[3:0]</td><td>BREAK0输入信号滤波数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了BREAK0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,BREAK0异步有效,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}, N=2</eq>0010:<eq>f_{SAMP} = f_{CK\_TIMER}, N=4</eq>0011:<eq>f_{SAMP} = f_{CK\_TIMER}, N=8</eq>0100:<eq>f_{SAMP} = f_{DTS}/2, N=6</eq>0101:<eq>f_{SAMP} = f_{DTS}/2, N=8</eq>0110:<eq>f_{SAMP} = f_{DTS}/4, N=6</eq>0111:<eq>f_{SAMP} = f_{DTS}/4, N=8</eq>1000:<eq>f_{SAMP} = f_{DTS}/8, N=6</eq>1001:<eq>f_{SAMP} = f_{DTS}/8, N=8</eq>1010:<eq>f_{SAMP} = f_{DTS}/16, N=5</eq>1011:<eq>f_{SAMP} = f_{DTS}/16, N=6</eq>1100:<eq>f_{SAMP} = f_{DTS}/16, N=8</eq>1101:<eq>f_{SAMP} = f_{DTS}/32, N=5</eq>1110:<eq>f_{SAMP} = f_{DTS}/32, N=6</eq>1111:<eq>f_{SAMP} = f_{DTS}/32, N=8</eq>此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>15</td><td>POEN</td><td>所有的通道输出使能根据OAEN位,该位可以软件设置或者硬件自动设置。一旦中止输入有效,该位被硬件异步清0。如果一个通道配置为输出模式,如果设置了相应的使能位(TIMERx_CHCTL2寄存器的CHxEN, CHxNEN位),则开启CHx_O和MCHx_O输出。0:禁止通道输出或强制为空闲状态1:使能通道输出</td></tr><tr><td>14</td><td>OAEN</td><td>自动输出使能此位定义了POEN位是否可以被硬件自动置1。0: POEN位不能被硬件置11: 如果中止输入无效,下一次更新事件发生时,POEN位能被硬件自动置1此位只有在TIMERx_CCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>13</td><td>BRK0P</td><td>BREAK0输入信号极性此位定义了BREAK0输入的极性。0: BREAK0输入低电平有效1: BREAK0输入高电平有效此位只有在TIMERx_CCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>12</td><td>BRK0EN</td><td>BREAK0输入信号使能此位置1使能BREAK0输入信号。0: BREAK0输入禁能1: BREAK0输入使能此位只有在TIMERx_CCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>11</td><td>ROS</td><td>运行模式下“关闭状态”使能当POEN位被置1(运行模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表23-22.由参数控制的互补输出表(MCHxMSEL=2'b11)。0: 输出“关闭状态”禁能。当CHxEN或者CHxNEN位被清零,对应通道为输出“禁能状态”。1: 输出“关闭状态”使能。当CHxEN或者CHxNEN位被清零,对应通道为输出“关闭状态”。此位在TIMERx_CCHP0寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>10</td><td>IOS</td><td>空闲模式下“关闭状态”使能当POEN位被清0(空闲模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表23-22.由参数控制的互补输出表(MCHxMSEL=2'b11)。0: 输出“关闭状态”禁能。当CHxEN和CHxNEN位均被清零,对应通道为输出“禁能状态”。1: 输出“关闭状态”使能。不论CHxEN和CHxNEN位的值,对应通道为输出“关闭状态”。此位在TIMERx_CCHP0寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>9:8</td><td>PROT[1:0]</td><td>互补寄存器保护控制这两位定义了寄存器的写保护特性。00: 禁能保护模式。无写保护01: PROT模式0。TIMERx_CTL1寄存器中ISOx/ISOxN位,TIMERx_CCHP0寄存器中BRK0EN/BRK0P/OAEN/DTCFG位写保护10: PROT模式1。除了PROT模式0下的寄存器写保护外,还有TIMERx_CHCTL2寄存器中CHxP/MCHxP位(如果相应通道配置为输出模式),TIMERx_CCHP0寄</td></tr></table>

存器中 ROS / IOS 位。

<table><tr><td>7:0</td><td>DTCFG[7:0]</td><td>死区时间控制这些位定义了插入互补输出之间的死区持续时间。DTCFG值和死区时间的关系如下:DTCFG [7:5] = 3&#x27;b0xx: DTvalue = DTCFG [7:0] x tDT, tDT = tDTSDTCFG [7:5] = 3&#x27;b 10x: DTvalue = (64+DTCFG [5:0]) x tDT, tDT = tDTS * 2DTCFG [7:5] = 3&#x27;b 110: DTvalue = (32+DTCFG [4:0]) x tDT, tDT = tDTS * 8DTCFG [7:5] = 3&#x27;b 111: DTvalue = (32+DTCFG [4:0]) x tDT, tDT = tDTS * 16此位只有在 TIMERx_CCHP0 寄存器的 PROT [1:0] = 00 时才可修改。</td></tr></table>

## 多模式通道控制寄存器 0（TIMERx_MCHCTL0）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">保留</td><td rowspan="2">MCH0MS[2]</td><td rowspan="2" colspan="13">保留</td><td>MCH0COMCTL[3]</td></tr><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="8">保留</td><td>MCH0COMCEN</td><td colspan="3">MCH0COMCTL[2:0]</td><td>MCH0COMSEN</td><td>MCH0COMFEN</td><td rowspan="2" colspan="2">MCH0MS[1:0]</td></tr><tr><td colspan="4">MCH0CAPFLT[3:0]</td><td colspan="2">MCH0CAPPSC[1:0]</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>MCH0MS[2]</td><td>多模式通道 0 I/O 模式选择参考MCH0MS[1:0]描述。</td></tr><tr><td>29:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>MCH0COMCTL[3]</td><td>多模式通道0输出比较控制请参考MCH0COMCTL[2:0]描述。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>MCH0COMCEN</td><td>多模式通道0输出比较清0使能当此位被置1,当检测到ETIFP输入高电平时,MO0CPRE参考信号被清0。0:多模式通道0输出比较清零禁止1:多模式通道0输出比较清零使能</td></tr><tr><td>6:4</td><td>MCH0COMCTL[2:0]</td><td>多模式通道0输出比较控制当多模式通道0配置为输出模式,并且MCH0MSEL[1:0]=2'b00,MCH0COMCTL[3]和MCH0COMCTL[2:0]位域定义了输出准备信号MO0CPRE的动作,而MO0CPRE决定了MCH0_O的值。MO0CPRE高电平有效,而MCH0_O的有效电平取决于MCH0FP[1:0]位。注意:当多模式通道0配置为输出模式,且MCH0MSEL[1:0]=2'b11时,CH0COMCTL[2:0]位定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O、MCH0_O的值。O0CPRE高电平有效,CH0_O、MCH0_O的有效电平取决于CH0P、MCH0P位。0000:时基。输出比较寄存器TIMERx_MCH0CV与计数器TIMERx_CNT间的比较对MO0CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE翻转。0100:强制为低。强制MO0CPRE为低电平0101:强制为高。强制MO0CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_MCH0CV时,MO0CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_MCH0CV时,MO0CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_MCH0CV时,MO0CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_MCH0CV时,MO0CPRE为有效电平,否则为无效电平。1000~1111:保留</td></tr></table>

## 注意：

在 PWM 模式 1 或 PWM 模式 2 中，只有当比较结果改变了或者输出比较模式中从时基模式切换到 PWM模式时，MO0CPRE 电平才改变。

当 CH0 和 MCH0 输出互补时，该位域预装载。若 CCSE = 1，则该位域只在通道换

<table><tr><td></td><td></td><td>相事件发生时更新。当TIMERx_CCHP0寄存器的PROT[1:0] = 11且MCH0MS = 000(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>MCH0COMSEN</td><td>多模式通道0输出比较影子寄存器使能当此位被置1,TIMERx_MCH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止多模式通道0输出/比较影子寄存器1:使能多模式通道0输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。当TIMERx_CCHP0寄存器的PROT [1:0] = 11且CH0MS = 00时此位不能被改变。</td></tr><tr><td>2</td><td>MCH0COMFEN</td><td>多模式通道0输出比较快速使能当该位为1时,如果通道配置为PWM模式0或者PWM模式1,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,MCH0_O被设置为比较电平而与比较结果无关。0:多模式通道0输出比较快速禁能。当触发器的输入有一个有效沿时,激活MCH0_O输出的最小延时为5个时钟周期1:多模式通道0输出比较快速使能。当触发器的输入有一个有效沿时,激活MCH0_O输出的最小延时为3个时钟周期</td></tr><tr><td>1:0</td><td>MCH0MS[1:0]</td><td>多模式通道0I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的MCH0EN位清0)时,MCH0MS[2:0]才可写。000:多模式通道0配置为输出001:多模式通道0配置为输入,MIS0映射在MCIOFEM0上010:保留011:保留100:多模式通道0配置为输入,MIS0映射在CI0FEM0上。101~111:保留</td></tr></table>

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>MCH0MS[2]</td><td>多模式通道 0 I/O 模式选择参考MCH0MS[1:0]描述。</td></tr><tr><td>29:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>MCH0CAPFLT[3:0]</td><td>通道 0 输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录 N 个输入事件后会产生一个输出的跳变。</td></tr></table>

这些位定义了 MCI0 输入信号的采样频率和数字滤波器的长度。

0000：无滤波器，f<sub>SAMP</sub>= f<sub>DTS</sub>，N=10001：f<sub>SAMP</sub> = f<sub>CK_TIMER</sub>，N=20010：f<sub>SAMP</sub> = f<sub>CK_TIMER</sub>，N=40011：f<sub>SAMP</sub> = f<sub>CK_TIMER</sub>，N=80100：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=60101：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=80110：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=60111：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=81000：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=61001：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=81010：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=51011：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=61100：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=81101：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=51110：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=61111：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=8

## 3:2 MCH0CAPPSC[1:0] 多模式通道 0 输入捕获预分频器

## 多模式通道控制寄存器 2（TIMERx_MCHCTL2）

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>MCH0FP[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>MCH0FP[1:0]</td><td>多模式通道0捕获/比较独立极性控制当多模式通道0配置为输出模式时,且MCH0MSEL[1:0]=2&#x27;b00,此位定义了输出信号极性。00:多模式通道0高电平有效01:多模式通道0低电平有效10:保留11:保留当通道0配置为输入模式时,此位定义了多模式通道0输入信号的极性。MCH0FP[1:0]将选择多模式通道0输入信号的有效边沿或者捕获极性。00:把多模式通道0输入信号的上升沿作为捕获或者从模式下触发的有效信号,且多模式通道0输入信号不会被翻转。01:把多模式通道0输入信号的下降沿作为捕获或者从模式下触发的有效信号,且多模式通道0输入信号会被翻转。10:保留。11:把多模式通道0输入信号的上升沿或下降沿作为捕获或者从模式下触发的有效信号,并且多模式通道0输入信号不会被翻转。当TIMERxCCHP0寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr></table>

## 多模式通道 0 捕获/比较寄存器（TIMERx_MCH0CV）

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MCH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>MCH0VAL[15:0]</td><td>多模式通道0的捕获或比较值当多模式通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值,且本寄存器为只读。当多模式通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相</td></tr></table>

应影子寄存器后，影子寄存器值随每次更新事件更新。

## 控制寄存器 2（TIMERx_CTL2）

地址偏移：0x74

复位值：0x0030 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="2">MCH0MSEL[1:0]</td><td colspan="4">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>MCH0MSEL[1:0]</td><td>多模式通道0模式选择00:独立模式,MCH0 独立于CH001:保留10:保留11:互补模式,只有CH0可用于输入,MCH0输出与CH0输出互补</td></tr><tr><td>19:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## TIMERx 备用功能控制寄存器 0（TIMERx_AFCTL0）

地址偏移：0x8C

复位值：0x0000 0001


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>BRK0CMP3P</td><td>BRK0CMP2P</td><td>BRK0CMP1P</td><td>BRK0CMP0P</td><td colspan="8">保留</td><td>BRK0IN0P</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="8"></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BRK0CMP6EN</td><td>BRK0CMP5EN</td><td>BRK0CMP4EN</td><td>BRK0CMP3EN</td><td>BRK0CMP2EN</td><td>BRK0CMP1EN</td><td>BRK0CMP0EN</td><td>BRK0HPDFEN</td><td>BRK0CMP7EN</td><td colspan="6">保留</td><td>BRK0IN0EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="6"></td><td>rw</td></tr></table>

<table><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>BRK0CMP3P</td><td>BREAK0 CMP3输入极性该位用于配置CMP3输入极性,具体极性是由该位和BRK0P位共同确定。0:CMP3输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:CMP3输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>27</td><td>BRK0CMP2P</td><td>BREAK0 CMP2输入极性该位用于配置CMP2输入极性,具体极性是由该位和BRK0P位共同确定。0:CMP2输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:CMP2输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>26</td><td>BRK0CMP1P</td><td>BREAK0 CMP1输入极性该位用于配置CMP1输入极性,具体极性是由该位和BRK0P位共同确定。0:CMP1输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:CMP1输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>25</td><td>BRK0CMP0P</td><td>BREAK0 CMP0输入极性0:CMP0输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:CMP输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>24:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BRK0IN0P</td><td>BREAK0 BRKIN0备用输入极性该位用于配置BRKIN0输入极性,具体极性是由该位和BRK0P位共同确定。0:BRKIN0输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:BRKIN0输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>15</td><td>BRK0CMP6EN</td><td>BREAK0 CMP6输入使能0: CMP6输入禁能1: CMP6输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>14</td><td>BRK0CMP5EN</td><td>BREAK0 CMP5输入使能0: CMP5输入禁能1: CMP5输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>13</td><td>BRK0CMP4EN</td><td>BREAK0 CMP4输入使能0: CMP4输入禁能1: CMP4输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>12</td><td>BRK0CMP3EN</td><td>BREAK0 CMP3输入使能0: CMP3输入禁能1: CMP3输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>11</td><td>BRK0CMP2EN</td><td>BREAK0 CMP2输入使能0: CMP2输入禁能1: CMP2输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>10</td><td>BRK0CMP1EN</td><td>BREAK0 CMP1输入使能0: CMP1输入禁能1: CMP1输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>9</td><td>BRK0CMP0EN</td><td>BREAK0 CMP0输入使能0: CMP0输入禁能1: CMP0输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>8</td><td>BRK0HPDFEN</td><td>BREAK0 HPDF输入使能0: HPDF输入禁能1: HPDF输入使能注意: HPDF输入对于TIMER15(HPDF_BREAK[1])和TIMER16(HPDF_BREAK[2])是不同的。此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>7</td><td>BRK0CMP7EN</td><td>BREAK0 CMP7输入使能0: CMP7输入禁能</td></tr><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:19</td><td>OCRINSEL[2:0]</td><td>OCPRE_CLR输入选择000: OCPRE_CLR0001: OCPRE_CLR1...111: OCPRE_CLR7</td></tr><tr><td colspan="2" rowspan="9"></td><td>OCPRE_CLR 输入选择 TIMER15 / 16</td></tr><tr><td>OCPRE_CLR0 CMP0_OUT</td></tr><tr><td>OCPRE_CLR1 CMP1_OUT</td></tr><tr><td>OCPRE_CLR2 CMP2_OUT</td></tr><tr><td>OCPRE_CLR3 CMP3_OUT</td></tr><tr><td>OCPRE_CLR4 CMP4_OUT</td></tr><tr><td>OCPRE_CLR5 CMP5_OUT</td></tr><tr><td>OCPRE_CLR6 CMP6_OUT</td></tr><tr><td>OCPRE_CLR7 CMP7_OUT</td></tr></table>

<table><tr><td></td><td></td><td>1: CMP7输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>6:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BRK0IN0EN</td><td>BREAK0 BRKIN0备用输入使能0: BRKIN0输入禁能1: BRKIN0输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr></table>

## 备用功能控制寄存器 1（TIMERx_AFCTL1）

地址偏移：0x90

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="3">OCRINSEL[2:0]</td><td colspan="3">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>


此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。


保留

必须保持复位值。

## 重复计数寄存器 1（TIMERx_CREP1）

地址偏移：0x98

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CREP1[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CREP1[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CREP1[31:0]</td><td>重复计数器的值 1该位域为 32 位,只读。这些位定义了更新事件的产生速率。重复计数器计数值减为 0 时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。注意:当TIMERx_CFG寄存器中的CREPSEL=1时,使用该位域。</td></tr></table>

互补通道保护寄存器 1（TIMERx_CCHP1）

地址偏移：0x09C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>DTMODE N</td><td>DTDIFEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">DTFCFG[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>DTMODEN</td><td>死区时间在线修改功能使能0:死区时间在线修改功能禁能1:死区时间在线修改功能使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。注意:如果在CEN=1时将该位置1,则在上次更新事件之后写入的任何值(在DTCFG[7:0]位域和DTCFG[7:0]位域)都是无效的,只使用前一次的值。</td></tr><tr><td>16</td><td>DTDIFEN</td><td>死区时间不同配置使能0:上升沿和下降沿的死区时间(在 TIMERx_CCHP1 寄存器的 DTCFG[7:0]位域配置)相同。1:上升沿的死区时间由 TIMERx_CCHP1 寄存器的 DTCFG[7:0]位域配置;下降沿的死区时间由 TIMERx_CCHP1 寄存器的 DTFCFG[7:0]位域配置。此位只有在TIMERx_CCHP0寄存器的PROT [1:0] = 00时才可修改。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>DTFCFG[7:0]</td><td>下降沿死区时间控制该位域控制 OxCPRE 信号下降沿的死区时间值,该死区时间在输出转换之前插入。DTCFG 值与死区时间的关系如下:DTCFG [7:5] = 3'b0xx: DTvalue = DTCFG [7:0] x tDT, tDT = tDTSDTCFG [7:5] = 3'b 10x: DTvalue = (64+DTCFG [5:0]) x tDT, tDT = tDTS * 2DTCFG [7:5] = 3'b 110: DTvalue = (32+DTCFG [4:0]) x tDT, tDT = tDTS * 8DTCFG [7:5] = 3'b 111: DTvalue = (32+DTCFG [4:0]) x tDT, tDT = tDTS * 16此位只有在 TIMERx_CCHP0 寄存器的 PROT [1:0]=00 时才可修改</td></tr></table>

## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">DMATC[5:0]</td><td colspan="2">保留</td><td colspan="6">DMATA [5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>DMATC [5:0]</td><td>DMA 传输计数该位域定义了 DMA 访问(读/写)TIMERx_DMATB 寄存器的次数。6'b000000:传输1次6'b000001:传输2次6'b111000: 传输57次</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>DMATA [5:0]</td><td>DMA传输起始地址该位域定义了DMA访问TIMERxDMAVB寄存器的第一个地址。当通过TIMERxDMA第一次访问时,访问的就是该位域指定的地址。第二次访问TIMERx_DMATB时,将访问起始地址+0x4。6'b0_0000: TIMERx_CTL06'b0_0001: TIMERx_CTL1...总之:起始地址 = TIMERx_CTL0 + DMATA*4</td></tr></table>

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DMATB[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DMATB [31:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>CCUSEL</td><td>CREPSEL</td><td>CHVSEL</td><td>OUTSEL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CCUSEL</td><td>换相控制影子寄存器更新选择只有当CCUC[2:0]位域配置为100,101和110时,该位才有效。0:当计数器产生一个上溢/下溢事件时,影子寄存器才更新1:当重复计数器值为0,且计数器产生一个上溢/下溢事件时,影子寄存器才更新</td></tr><tr><td>2</td><td>CREPSEL</td><td>计数器重复寄存器选择该位用于选择重复计数寄存器。0:更新事件的速率由TIMERx_CREPO寄存器确定1:更新事件的速率由 TIMERx_CREP1 寄存器确定</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写 1 或清 0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>OUTSEL</td><td>输出值选择位此位由软件写 1 或清 0。1:如果 POEN 位与 IOS 位均为 0,则输出无效0:无影响</td></tr></table>

