## 14.4.5. TIMERx 寄存器(x=15,16)

TIMER15 基地址：0x4001 4400

TIMER16 基地址：0x4001 4800

## 控制寄存器 0 (TIMERx_CTL0)

地址偏移：0x00

复位值: 0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="3">保留</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


该寄存器通过字访问(32位)


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置 CKDIV,规定定时器时钟(TIMER_CK)与死区时间和采样时钟(DTS)之间的分频系数,死区发生器和数字滤波器会用到 DTS 时间。00:fDTS=fTIMER_CK01:fDTS=fTIMER_CK/210:fDTS=fTIMER_CK/411:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0:更新事件发生后,计数器继续计数1:在下一次更新事件发生时,CEN 硬件清零并且计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该为,选择更新事件源.0:使能后,下述任一事件产生更新中断或 DMA 请求:-UPG 位被置 1-计数器溢出/下溢-从模式控制器产生的更新1:使能后只有计数器溢出/下溢才产生更新中断或 DMA 请求</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新.该位用来使能或禁能更新事件的产生.0:更新事件使能.当以下事件之一发生时,更新事件产生,具有缓存的寄存器被装入它们的预装载值:-UPG 位被置 1-计数器溢出/下溢-从模式控制器产生一个更新事件1:更新事件禁能.带有缓存的寄存器保持原有值,如果 UPG 位被置 1 或者从模式控制器产生一个硬件复位事件,计数器和预分频器被重新初始化</td></tr></table>

计数器使能

0：计数器禁能

1：计数器使能

在软件将 CEN位置 1 后，外部时钟、暂停模式和编码器模式才能工作。触发模式可以自动地通过硬件设置 CEN位。

控制寄存器 1 (TIMERx_CTL1)

地址偏移：0x04

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>ISO0N</td><td>ISO0</td><td colspan="4">保留</td><td>DMAS</td><td>CCUC</td><td>保留</td><td>CCSE</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>ISO0N</td><td>通道0的互补通道空闲状态输出0:当POEN复位,CH0_ON设置低电平.1:当POEN复位,CH0_ON设置高电平此位只有在TIMERx_CCHP寄存器的PROT[1:0]位为00的时候可以被更改.</td></tr><tr><td>8</td><td>ISO0</td><td>通道0的空闲状态输出0:当POEN复位,CH0_O设置低电平1:当POEN复位,CH0_O设置高电平如果CH0_ON生效,一个死区时间后CH0_O输出改变。此位只有在TIMERx_CCHP寄存器的PROT[1:0]位为00的时候可以被更改.</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>DMAS</td><td>DMA请求源选择0:当通道捕获/比较事件发生时,发送通道x的DMA请求.1:当更新事件发生,发送通道x的DMA请求</td></tr><tr><td>2</td><td>CCUC</td><td>换相控制影子寄存器更新控制当换相控制影子寄存器(CHxEN, CHxNEN和CHxCOMCTL位)使能(CCSE=1),这些影子寄存器更新控制如下:0:CMTG位被置1时更新影子寄存器1:当CMTG位被置1或检测到TRIGI上升沿时,影子寄存器更新当通道没有互补输出时,此位无效。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值.</td></tr></table>

0：影子寄存器 CHxEN, CHxNEN 和 CHxCOMCTL 位禁能.

1：影子寄存器 CHxEN, CHxNEN 和 CHxCOMCTL 位使能.

如果这些位已经被写入了，换相事件到来时这些位才被更新

当通道没有互补输出时，此位无效

## DMA 和中断使能寄存器 (TIMERx_DMAINTEN)

地址偏移：0x0C

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CH0DEN</td><td>UPDEN</td><td>BRK0IE</td><td>保留</td><td>CMTIE</td><td colspan="3">保留</td><td>CH0IE</td><td>UPIE</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>9</td><td>CHODEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>BRK0IE</td><td>中止中断使能0:禁止中止中断1:使能中止中断</td></tr><tr><td>5</td><td>CMTIE</td><td>换相更新中断使能0:禁止换相更新中断1:使能换相更新中断</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器 (TIMERx_INTF)

地址偏移：0x10

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">SYSBIF</td><td colspan="2">保留</td><td>CH0OF</td><td>保留.</td><td>BRK0IF</td><td>保留</td><td>CMTIF</td><td colspan="3">保留.</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="2"></td><td colspan="2">rc_w0</td><td colspan="2"></td><td colspan="2">rc_w0</td><td colspan="2">rc_w0</td><td colspan="4">rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>13</td><td>SYSBIF</td><td>系统源中止事件中断标志位当系统中止源有效时,该位由硬件置1,当系统源无效时,该位由软件清零。0:无系统中止事件中断发生1:系统中止事件中断发生注意:当该位置1时,在通道输出恢复前,该位必须由软件清零。</td></tr><tr><td>12:10</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0.0:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7</td><td>BRK0IF</td><td>中止0中断标志位一旦中止输入有效,由硬件对该位置‘1’。如果中止输入无效,则该位可由软件清‘0’。0:无中止事件产生1:中止输入上检测到有效电平</td></tr><tr><td>5</td><td>CMTIF</td><td>通道换相更新中断标志当通道换相更新事件发生时此标志位被硬件置1,此位由软件清0。0:无通道换相更新中断发生1:通道换相更新中断发生</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在任何更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器 (TIMERx_SWEVG)

地址偏移：0x14

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>BRK0G</td><td>保留</td><td>CMTG</td><td colspan="3">保留</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="8"></td><td>w</td><td colspan="5">w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7</td><td>BRKG</td><td>产生中止0事件该位由软件置1,用于产生一个中止事件,由硬件自动清0。当此位被置1时,POEN位被清0且BRKIF位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:不产生中止事件1:产生中止事件</td></tr><tr><td>5</td><td>CMTG</td><td>通道换相更新事件发生此位由软件置1,由硬件自动清0.当此位被置1,通道捕获/比较控制寄存器(CHxEN, CHxNEN 和 CHxCOMCTL)的互补输出被更新(根据 TIMERx_CTL1 中CCSE 值)。0:不产生通道控制更新事件1:产生通道控制更新事件</td></tr><tr><td>4:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,如果选择了中央对齐或向上计数模式,计数器被清0。否则(向下计数模式)计数器将载入自动重载值,预分频计数器将同时被清除。0:无更新事件产生1:产生更新事件</td></tr></table>

## 通道控制寄存器 0 (TIMERx_CHCTL0)

地址偏移：0x18

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="8">保留</td><td>保留</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式此位定义了输出参考信号O0CPRE的动作,而O0CPRE决定了CH0_O、CH0_ON的值。O0CPRE高电平有效,而CH0_O、CH0_ON的有效电平取决于CH0P、CH0NP位。000:时基。输出比较寄存器TIMERx_CH0CV与计数器TIMERx_CNT间的比较对O0CPRE不起作用001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为高。010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为低。011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE翻转。100:强制为低。强制O0CPRE为低电平101:强制为高。强制O0CPRE为高电平110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为无效电平,否则为有效电平。111: PWM 模式 1。在向上计数时,一旦计数器值小于 TIMERx_CH0CV 时,O0CPRE 为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于 TIMERx_CH0CV 时,O0CPRE 为有效电平,否则为无效电平。在 PWM 模式 0 或 PWM 模式 1 中,只有当比较结果改变了或者输出比较模式中从时基模式切换到 PWM 模式时,O0CPRE 电平才改变。当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 且 CH0MS =00(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>CH0COMSEN</td><td>通道 0 输出比较影子寄存器使能当此位被置 1,TIMERx_CH0CV 寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道 0 输出/比较影子寄存器1:使能通道 0 输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0 寄存器的 SPM =1),可以在未确认预装载寄存器情况下使用 PWM 模式当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 且 CH0MS =00 时此位不能被改变。</td></tr><tr><td>2</td><td>CH0COMFEN</td><td>通道 0 输出比较快速使能当该位为 1 时,如果通道配置为 PWM0 模式或者 PWM1 模式,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH0_O 被设置为比较电平而与比较结果无关。0:禁止通道 0 输出比较快速. 当触发器的输入有一个有效沿时,激活 CH0_O 输出的最小延时为 5 个时钟周期1:使能通道 0 输出比较快速。当触发器的输入有一个有效沿时,激活 CH0_O 输出的最小延时为 3 个时钟周期</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道 0 I/O 模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH0EN 位被清 0)时这些位才可写。00:通道 0 配置为输出01:通道 0 配置为输入,ISO 映射在 CI0FE0 上10:保留11:保留</td></tr></table>

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了CI0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,fSAMP=fDTS,N=10001:fSAMP=fPCLK,N=20010:fSAMP=fPCLK,N=40011:fSAMP=fPCLK,N=80100:fSAMP=fDTS/2,N=6</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留.</td><td>CH0NP</td><td>CH0NEN</td><td>CH0P</td><td>CH0EN</td></tr><tr><td colspan="12"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td></td><td></td><td>0101: fSAMP=fDTS/2, N=8</td></tr><tr><td></td><td></td><td>0110: fSAMP=fDTS/4, N=6</td></tr><tr><td></td><td></td><td>0111: fSAMP=fDTS/4, N=8</td></tr><tr><td></td><td></td><td>1000: fSAMP=fDTS/8, N=6</td></tr><tr><td></td><td></td><td>1001: fSAMP=fDTS/8, N=8</td></tr><tr><td></td><td></td><td>1010: fSAMP=fDTS/16, N=5</td></tr><tr><td></td><td></td><td>1011: fSAMP=fDTS/16, N=6</td></tr><tr><td></td><td></td><td>1100: fSAMP=fDTS/16, N=8</td></tr><tr><td></td><td></td><td>1101: fSAMP=fDTS/32, N=5</td></tr><tr><td></td><td></td><td>1110: fSAMP=fDTS/32, N=6</td></tr><tr><td></td><td></td><td>1111: fSAMP=fDTS/32, N=8</td></tr><tr><td>3:2</td><td>CH0CAPPSC[1:0]</td><td>通道0输入捕获预分频器这2位定义了通道0输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH0EN=0时,则预分频器复位。00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获01:每2个事件触发一次捕获10:每4个事件触发一次捕获11:每8个事件触发一次捕获</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道0模式选择与输出比较模式相同</td></tr></table>

## 通道控制寄存器 2 (TIMERx_CHCTL2)

地址偏移：0x20

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,此位定义了互补输出信号的极性。0:通道0高电平有效1:通道0低电平有效当通道0配置为输入模式时,此位和CH0P联合使用,作为输入信号CI0的极性选择控制信号。当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 或 10 时此位不能被更改。</td></tr><tr><td>2</td><td>CH0NEN</td><td>通道 0 互补输出使能当通道 0 配置为输出模式时,将此位置 1 使能通道 0 的互补输出。0:禁止通道 0 互补输出1:使能通道 0 互补输出</td></tr><tr><td>1</td><td>CH0P</td><td>通道 0 极性当通道 0 配置为输出模式时,此位定义了输出信号极性。0:通道 0 高电平有效1:通道 0 低电平有效当通道 0 配置为输入模式时,此位定义了 CI0 信号极性[CH0NP, CH0P] 将选择 CI0FE0 或者 CI1FE0 的有效边沿或者捕获极性[CH0NP==0, CH0P==0]:把 CIxFEO 的上升沿作为捕获或者从模式下触发的有效信号,并且 CIxFEO 不会被翻转。[CH0NP==0, CH0P==1]:把 CIxFEO 的下降沿作为捕获或者从模式下触发的有效信号,并且 CIxFEO 会被翻转。[CH0NP==1, CH0P==0]:保留。[CH0NP==1, CH0P==1]:把 CIxFEO 的上升沿和下降沿都作为捕获或者从模式下触发的有效信号,并且 CIxFEO 不会被翻转。当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 或 10 时此位不能被更改。</td></tr><tr><td>0</td><td>CH0EN</td><td>通道 0 捕获/比较使能当通道 0 配置为输出模式时,将此位置 1 使能 CH0_O 信号有效。当通道 0 配置为输入模式时,将此位置 1 使能通道 0 上的捕获事件。0:禁止通道 01:使能通道 0</td></tr></table>

## 计数器寄存器 (TIMERx_CNT)

地址偏移：0x24

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>


重复计数寄存器 (TIMERx_CREP)


## 预分频寄存器 (TIMERx_PSC)

地址偏移： 0x28

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值</td></tr><tr><td></td><td></td><td>计数器时钟等于 PSC 时钟除以 (PSC+1),每次当更新事件产生时,PSC 的值被装入当前预分频寄存器。</td></tr></table>

## 计数器自动重载寄存器 (TIMERx_CAR)

地址偏移：0x2C

复位值: 0x0000 FFFF

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。</td></tr></table>


地址偏移：0x30



复位值: 0x0000 0000



该寄存器通过字访问(32位)


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CREP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>15:0</td><td>CREP[15:0]</td><td>重复计数器的值这些位定义了更新事件的产生速率。重复计数器计数值减为0时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。</td></tr></table>

## 通道 0 捕获/比较寄存器 (TIMERx_CH0CV)

地址偏移：0x34

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

互补通道保护寄存器 (TIMERx_CCHP)

地址偏移：0x44

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">BRKOF[3:0]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>POEN</td><td>OAEN</td><td>BRKP</td><td>BRKEN</td><td>ROS</td><td>IOS</td><td colspan="2">PROT[1:0]</td><td colspan="8">DTCFG[7:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:16</td><td>BRK0F[3:0]</td><td>BREAK0输入信号滤波数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了BREAK0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,BREAK0异步有效,N=10001:fSAMP=fCK_TIMER,N=20010:fSAMP=fCK_TIMER,N=40011:fSAMP=fCK_TIMER,N=80100:fSAMP=fDTS/2,N=60101:fSAMP=fDTS/2,N=80110:fSAMP=fDTS/4,N=60111:fSAMP=fDTS/4,N=81000:fSAMP=fDTS/8,N=61001:fSAMP=fDTS/8,N=81010:fSAMP=fDTS/16,N=51011:fSAMP=fDTS/16,N=61100:fSAMP=fDTS/16,N=81101:fSAMP=fDTS/32,N=51110:fSAMP=fDTS/32,N=61111:fSAMP=fDTS/32,N=8此位只有在TIMERx_CCHP寄存器的PROT [1:0]=00时才可修改。</td></tr><tr><td>15</td><td>POEN</td><td>所有的通道输出使能根据OAEN位,该位可以软件设置或者硬件自动设置。一旦中止输入有效,该位被硬件异步清0。如果一个通道配置为输出模式,如果设置了相应的使能位(TIMERx_CHCTL2寄存器的CHxEN,CHxNEN位),则开启CHx_O和CHx_ON输出。0:禁止通道输出或强制为空闲状态1:使能通道输出</td></tr><tr><td>14</td><td>OAEN</td><td>自动输出使能此位定义了POEN位是否可以被硬件自动置1。0:POEN位不能被硬件置11:如果中止输入无效,下一次更新事件发生时,POEN位能被硬件自动置1此位只有在TIMERx_CCHP寄存器的PROT [1:0]=00时才可修改。</td></tr><tr><td>13</td><td>BRKP</td><td>中止极性此位定义了中止输入信号BKIN的极性。0:中止输入低电平有效1:中止输入高电平有效</td></tr><tr><td>12</td><td>BRKEN</td><td>中止使能此位置1使能中止事件和CCS时钟失败事件输入。0:禁能中止输入</td></tr></table>

## 1：使能中止输入

<table><tr><td></td><td></td><td>此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0] =00 时才可修改。.</td></tr><tr><td>11</td><td>ROS</td><td>运行模式下“关闭状态”配置当 POEN 位被置 1,此位定义了通道(带有互补输出且配置为输出模式)的输出状态。0: 当 POEN 位被置 1,通道输出信号 (CHx_O/ CHx_ON)被禁止1: 当 POEN 位被置 1,通道输出信号 (CHx_O / CHx_ON)被使能,和 TIMER0_CHCTL2 寄存器 CHxEN/CHxNEN 位有关此位在 TIMERx_CCHP 寄存器的 PROT [1:0]=10 或 11 时不能被更改。</td></tr><tr><td>10</td><td>IOS</td><td>空闲模式下“关闭状态”配置当 POEN 位被清 0,此位定义了已经配置为输出模式的通道的输出状态。0: 当 POEN 位被清 0,通道输出信号(CHx_O/ CHx_ON)被禁止1: 当 POEN 位被清 0,通道输出信号(CHx_O/ CHx_ON)被使能,和 TIMERx_CHCTL2 寄存器 CHxEN/CHxNEN 位有关此位在 TIMERx_CCHP 寄存器的 PROT [1:0]=10 或 11 时不能被更改。.</td></tr><tr><td>9:8</td><td>PROT[1:0]</td><td>互补寄存器保护控制这两位定义了寄存器的写保护特性。00: 禁能保护模式。无写保护。01: PROT 模式 0。TIMERx_CTL1 寄存器中 ISOx/ISOxN 位,TIMERx_CCHP 寄存器中 BRKEN/BRKP/OAEN/DTCFG 位写保护10: PROT 模式 1。除了 PROT 模式 0 下的寄存器写保护外,还有 TIMERx_CHCTL2 寄存器中 CHxP/CHxNP 位(如果相应通道配置为输出模式), TIMERx_CCHP 寄存器中 ROS/IOS 位。11: PROT 模式 2。除了 PROT 模式 1 下的寄存器写保护外,还有 TIMERx_CHCTLR0/1 中 CHxCOMCTL/ CHxCOMSEN 位(如果相关通道配置为输出模式)写保护。系统复位后这两位只能被写一次,一旦 TIMERx_CCHP 寄存器被写入,这两位被写保护</td></tr><tr><td>7:0</td><td>DTCFG[7:0]</td><td>死区时间控制这些位定义了插入互补输出之间的死区持续时间。DTCFG 值和死区时间的关系如下:DTCFG [7:5] =3&#x27;b0xx: DTvalue =DTCFG [7:0]x tDT, tDT=tDTS.DTCFG [7:5] =3&#x27;b 10x: DTvalue = (64+DTCFG [5:0])xtDT, tDT =tDTS*2.DTCFG [7:5] =3&#x27;b 110: DTvalue = (32+DTCFG [4:0])xtDT, tDT=tDTS*8.DTCFG [7:5] =3&#x27;b 111: DTvalue = (32+DTCFG [4:0])xtDT, tDT =tDTS*16.此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0]=00 时才可修改。</td></tr></table>

## DMA 配置寄存器 (TIMERx_DMACFG)

地址偏移：0x48

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="5">DMATC[4:0]</td><td colspan="3">保留</td><td colspan="5">DMATA [4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>12:8</td><td>DMATC [4:0]</td><td>DMA 传输计数该位域定义了 DMA 访问(读写)TIMERx_DMATB 寄存器的数量</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:0</td><td>DMATA [4:0]</td><td>DMA 传输起始地址该位域定义了 DMA 访问 TIMERx_DMATB 寄存器的第一个地址。当通过 TIMERx_DMA 第一次访问时,访问的就是该位域指定的地址。第二次访问 TIMERx_DMATB 时,将访问起始地址+0x4。5&#x27;b0_0000: TIMERx_CTL05&#x27;b0_0001: TIMERx_CTL1...总之:起始地址 = TIMERx_CTL0 + DMATA*4</td></tr></table>

## DMA 发送缓冲区寄存器 (TIMERx_DMATB)

地址偏移：0x4C

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>DMATB [15:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

## 附加通道控制寄存器 0（TIMER0_AFCTL0）

地址偏移：0x60

复位值：0x0000 0001

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>BRK0IN0P</td><td colspan="8">保留</td><td>BRK0IN0EN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>9</td><td>BRK0IN0P</td><td>BREAK0 BRKIN0备用输入极性该位用于配置BRKIN0输入极性,具体极性是由该位和BRK0P位共同确定。0:BRKIN0输入信号不反相(BRK0P=0,输入信号低有效;BRK0P=1,输入信号高有效)1:BRKIN0输入信号反相(BRK0P=0,输入信号高有效;BRK0P=1,输入信号低有效)此位只有在TIMERx_CCHP寄存器的PROT [1:0]=00时才可修改。</td></tr><tr><td>8:1</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>0</td><td>BRK0IN0EN</td><td>BREAK0 BRKIN0备用输入使能0:BRKIN0输入禁能1:BRKIN0输入使能此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0]=00 时才可修改。</td></tr></table>

输入选择寄存器（TIMERx_INSEL）

地址偏移：0x68

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">CIO_SEL[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>3:0</td><td>CIO_SEL[3:0]</td><td>TIMERx_CH0输入选择</td></tr><tr><td></td><td></td><td>0000: 通道0输入连接到TIMERx_CH0</td></tr><tr><td></td><td></td><td>0001: 通道0输入连接到IRC32 对于TIMER16保留</td></tr><tr><td></td><td></td><td>0010: 对于TIMER15保留,通道0输入连接到HXTAL/32</td></tr><tr><td></td><td></td><td>0011: 对于TIMER15保留,对于TIMER16通道0输入连接到CKOUTSEL0</td></tr><tr><td></td><td></td><td>0100: 通道0输入连接到CKOUTSEL1</td></tr><tr><td></td><td></td><td>其他: 保留</td></tr></table>

## 配置寄存器 (TIMERx_CFG)

地址偏移：0xFC

复位值: 0x0000 0000

该寄存器通过字访问(32位)

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>OUTSEL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>OUTSEL</td><td>输出值选择位此位由软件写1或清0。1:如果POEN位与IOS位均为0,则输出无效0:无影响</td></tr></table>
