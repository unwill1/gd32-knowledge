## 22.1.4. TIMERx 寄存器（x=0,7）

TIMER0 基地址：0x4001 0000

TIMER7 基地址：0x4001 0400

## 控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="2">CAM[1:0]</td><td>DIR</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(CK_TIMER)与死区时间和数字滤波器采样时钟(DTS)之间的分频系数。00:$f_{DTS}=f_{CK\_TIMER}$01:$f_{DTS}=f_{CK\_TIMER}/2$10:$f_{DTS}=f_{CK\_TIMER}/4$11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器。1:使能 TIMERx_CAR 寄存器的影子寄存器。</td></tr><tr><td>6:5</td><td>CAM[1:0]</td><td>计数器对齐模式选择00:无中央对齐计数模式(边沿对齐模式)。DIR位指定了计数方向01:中央对齐向下计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),只有在向下计数时,CHxF位置110:中央对齐向上计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),只有在向上计数时,CHxF位置111:中央对齐上下计数置1模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0寄存器中CHxMS=00),在向上和向下计数时,CHxF位都会置1当计数器使能以后,该位不能从 0x00 切换到非 0x00</td></tr><tr><td>4</td><td>DIR</td><td>方向0:向上计数1:向下计数</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0: 单脉冲模式禁能。更新事件发生后,计数器继续计数1: 单脉冲模式使能。在下一次更新事件发生时,计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该位,选择更新事件源.0: 以下事件均会产生更新中断或DMA请求:UPG位被置1计数器溢出/下溢复位模式产生的更新1: 下列事件会产生更新中断或DMA请求:计数器溢出/下溢</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新.该位用来使能或禁能更新事件的产生0: 更新事件使能. 更新事件发生时,相应的影子寄存器被装入预装载值,以下事件均会产生更新事件:UPG位被置1计数器溢出/下溢复位模式产生的更新1: 更新事件禁能.注意:当该位被置1时,UPG位被置1或者复位模式不会产生更新事件,但是计数器和预分频器被重新初始化</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0: 计数器禁能。1: 计数器使能。在软件将CEN位置1后,外部时钟、暂停模式和译码器模式才能工作。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ISO3N</td><td>ISO3</td><td>ISO2N</td><td>ISO2</td><td>ISO1N</td><td>ISO1</td><td>ISO0N</td><td>ISO0</td><td>TI0S</td><td colspan="3">MMC[2:0]</td><td>DMAS</td><td>CCUC</td><td>保留</td><td>CCSE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ISO3N</td><td>通道3的互补通道空闲状态输出参考ISO0N位。</td></tr><tr><td>14</td><td>ISO3</td><td>通道3的空闲状态输出参考ISO0位。</td></tr><tr><td>13</td><td>ISO2N</td><td>通道2的互补通道空闲状态输出参考ISO0N位。</td></tr><tr><td>12</td><td>ISO2</td><td>通道2的空闲状态输出参考ISO0位。</td></tr><tr><td>11</td><td>ISO1N</td><td>通道1的互补通道空闲状态输出参考ISO0N位。</td></tr><tr><td>10</td><td>ISO1</td><td>通道1的空闲状态输出参考ISO0位。</td></tr><tr><td>9</td><td>ISO0N</td><td>通道0的互补通道空闲状态输出0:当POEN复位,CH0_ON设置低电平。1:当POEN复位,CH0_ON设置高电平。此位只有在TIMERx_CCHP寄存器的PROT[1:0]位为00的时候可以被更改。</td></tr><tr><td>8</td><td>ISO0</td><td>通道0的空闲状态输出0:当POEN复位,CH0_O设置低电平。1:当POEN复位,CH0_O设置高电平。如果CH0_ON生效,一个死区时间后CH0_O输出改变。此位只有在TIMERx_CCHP寄存器的PROT[1:0]位为00的时候可以被更改。</td></tr><tr><td>7</td><td>TI0S</td><td>通道0触发输入选择0:选择TIMERx_CH0引脚作为通道0的触发输入。1:选择TIMERx_CH0,CH1和CH2引脚异或的结果作为通道0的触发输入。</td></tr><tr><td>6:4</td><td>MMC[2:0]</td><td>主模式控制这些位控制TRGO信号的选择,TRGO信号由主定时器发给从定时器用于同步功能000:当产生一个定时器复位事件后,输出一个TRGO信号,定时器复位源为:主定时器产生一个复位事件TIMERx_SWEVG寄存器中UPG位置1001:当产生一个定时器使能事件后,输出一个TRGO信号,定时器使能源为:CEN位置1在暂停模式下,触发输入置1010:当产生一个定时器更新事件后,输出一个TRGO信号,更新事件源由UPDIS和UPS位决定011:当通道0在发生一次捕获或一次比较成功时,主模式控制器产生一个TRGO脉冲100:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O0CPRE101:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O1CPRE110:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O2CPRE111:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O3CPRE</td></tr><tr><td>3</td><td>DMAS</td><td>DMA请求源选择0:当通道捕获/比较事件发生时,发送通道x的DMA请求。1:当更新事件发生,发送通道x的DMA请求。</td></tr><tr><td>2</td><td>CCUC</td><td>换相控制影子寄存器更新控制当换相控制影子寄存器(CHxEN, CHxNEN和CHxCOMCTL位)使能(CCSE=1),这些影子寄存器更新控制如下:0:CMTG位被置1时更新影子寄存器。1:当CMTG位被置1或检测到TRIGI上升沿时,影子寄存器更新。当通道没有互补输出时,此位无效。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CCSE</td><td>换相控制影子使能0:影子寄存器CHxEN, CHxNEN和CHxCOMCTL位禁能。1:影子寄存器CHxEN, CHxNEN和CHxCOMCTL位使能。如果这些位已经被写入了,换相事件到来时这些位才被更新。当通道没有互补输出时,此位无效。</td></tr></table>

## 从模式配置寄存器（TIMERx_SMCFG）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ETP</td><td>SMC1</td><td colspan="2">ETPSC[1:0]</td><td colspan="4">ETFC[3:0]</td><td>MSM</td><td colspan="3">TRGS[2:0]</td><td>保留</td><td colspan="3">SMC[2:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15</td><td>ETP</td><td>外部触发极性该位指定 ETI 信号的极性0: ETI 高电平或上升沿有效.1: ETI 低电平或下降沿有效.</td></tr><tr><td>14</td><td>SMC1</td><td>SMC 的一部分为了使能外部时钟模式 1在外部时钟模式 1,计数器由 ETIF 信号上的任意有效边沿驱动0: 外部时钟模式 1 禁能1: 外部时钟模式 1 使能当从模式配置为复位模式,暂停模式和事件模式时,定时器仍然可以工作在外部时钟模式 1。但是 TRGS 必须不能为 3&#x27;b111。如果外部时钟模式 0 和外部时钟模式 1 同时被被配置,外部时钟的输入是 ETIF</td></tr></table>

<table><tr><td>6:4</td><td>TRGS[2:0]</td><td>触发选择</td></tr><tr><td></td><td></td><td>该位域用来指定选择哪一个信号作为用来同步计数器的触发输入源</td></tr><tr><td></td><td></td><td>000: ITI0</td></tr><tr><td></td><td></td><td>001: ITI1</td></tr><tr><td></td><td></td><td>010: ITI2</td></tr><tr><td></td><td></td><td>011: ITI3</td></tr><tr><td></td><td></td><td>100: CI0F_ED</td></tr><tr><td></td><td></td><td>101: CI0FE0</td></tr><tr><td></td><td></td><td>110: CI1FE1</td></tr></table>

注意：外部时钟模式 0 使能在寄存器的 SMC[2:0]位域。

<table><tr><td>13:12</td><td>ETPSC[1:0]</td><td>外部触发预分频</td></tr><tr><td></td><td></td><td>外部触发信号 ETIFP 的频率不能超过 TIMER_CK 频率的 1/4。当输入较快的外部时钟时,可以使用预分频降低 ETIFP 的频率。</td></tr><tr><td></td><td></td><td>00: 预分频禁能</td></tr><tr><td></td><td></td><td>01: 2 分频</td></tr><tr><td></td><td></td><td>10: 4 分频</td></tr><tr><td></td><td></td><td>11: 8 分频</td></tr></table>

## 11:8 ETFC[3:0] 外部触发滤波控制

外部触发信号可以通过数字滤波器进行滤波，该位域定义了数字滤波器的滤波能力。数字滤波器的基本原理是：以 f 频率连续采样外部触发信号，同时记录采样相同电平的次数。当该次数达到配置的滤波能力时，则认为是一个有效的电平信号。

<table><tr><td>EXTFC[3:0]</td><td>次数</td><td>fSAMP</td></tr><tr><td>4&#x27;b0000</td><td colspan="2">Filter disabled.</td></tr><tr><td>4&#x27;b0001</td><td>2</td><td></td></tr><tr><td>4&#x27;b0010</td><td>4</td><td>fCK_TIMER</td></tr><tr><td>4&#x27;b0011</td><td>8</td><td></td></tr><tr><td>4&#x27;b0100</td><td>6</td><td rowspan="2">$f_{DTS\_CK}/2$</td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6</td><td rowspan="2">$f_{DTS\_CK}/4$</td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6</td><td rowspan="2">$f_{DTS\_CK}/8$</td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5</td><td></td></tr><tr><td>4&#x27;b1011</td><td>6</td><td>$f_{DTS\_CK}/16$</td></tr><tr><td>4&#x27;b1100</td><td>8</td><td></td></tr><tr><td>4&#x27;b1101</td><td>5</td><td></td></tr><tr><td>4&#x27;b1110</td><td>6</td><td>$f_{DTS\_CK}/32$</td></tr><tr><td>4&#x27;b1111</td><td>8</td><td></td></tr><tr><td colspan="3">主-从模式该位被用来同步被选择的定时器同时开始计数。通过接在一起,TRGO用做启动事件。0:主从模式禁能1:主从模式使能</td></tr></table>

<table><tr><td></td><td></td><td>111: ETIFP从模式被使能后这些位不能改</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2:0</td><td>SMC[2:0]</td><td>从模式控制000: 关闭从模式. 如果 CEN=1,则预分频器直接由内部时钟驱动001: 译码器模式 0. 根据 CI1FE1 的电平,计数器在 CI0FE0 的边沿向上/下计数010: 译码器模式 1. 根据 CI0FE0 的电平,计数器在 CI1FE1 的边沿向上/下计数011: 译码器模式 2. 根据另一个信号的输入电平,计数器在 CI0FE0 和 CI1FE1 的边沿向上/ 下计数100: 复位模式. 选中的触发输入的上升沿重新初始化计数器,并且产生更新事件101: 暂停模式. 当触发输入为高时,计数器的时钟开启。一旦触发输入变为低,则计数器时钟停止110: 事件模式.计数器在触发输入的上升沿启动。111: 外部时钟模式 0. 选中的触发输入的上升沿驱动计数器</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDIE</td><td>CH2COMADDIE</td><td>CH1COMADDIE</td><td>CH0COMADDIE</td><td colspan="12">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>TRGDEN</td><td>CMTDEN</td><td>CH3DEN</td><td>CH2DEN</td><td>CH1DEN</td><td>CH0DEN</td><td>UPDEN</td><td>BRKIE</td><td>TRGIE</td><td>CMTIE</td><td>CH3IE</td><td>CH2IE</td><td>CH1IE</td><td>CH0IE</td><td>UPIE</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3COMADDIE</td><td>通道3附加比较中断使能0:禁止通道3附加比较中断1:使能通道3附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>30</td><td>CH2COMADDIE</td><td>通道2附加比较中断使能0:禁止通道2附加比较中断1:使能通道2附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>29</td><td>CH1COMADDIE</td><td>通道1附加比较中断使能0:禁止通道1附加比较中断1:使能通道1附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr></table>

<table><tr><td>28</td><td>CH0COMADDIE</td><td>通道0附加比较中断使能0:禁止通道0附加比较中断1:使能通道0附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>27:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>TRGDEN</td><td>触发DMA请求使能0:禁止触发DMA请求1:使能触发DMA请求</td></tr><tr><td>13</td><td>CMTDEN</td><td>换相DMA更新请求使能0:禁止换相DMA更新请求1:使能换相DMA更新请求</td></tr><tr><td>12</td><td>CH3DEN</td><td>通道3比较/捕获DMA请求使能0:禁止通道3比较/捕获DMA请求1:使能通道3比较/捕获DMA请求</td></tr><tr><td>11</td><td>CH2DEN</td><td>通道2比较/捕获DMA请求使能0:禁止通道2比较/捕获DMA请求1:使能通道2比较/捕获DMA请求</td></tr><tr><td>10</td><td>CH1DEN</td><td>通道1比较/捕获DMA请求使能0:禁止通道1比较/捕获DMA请求1:使能通道1比较/捕获DMA请求</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>BRKIE</td><td>中止中断使能0:禁止中止中断1:使能中止中断</td></tr><tr><td>6</td><td>TRGIE</td><td>触发中断使能0:禁止触发中断1:使能触发中断</td></tr><tr><td>5</td><td>CMTIE</td><td>换相更新中断使能0:禁止换相更新中断1:使能换相更新中断</td></tr><tr><td>4</td><td>CH3IE</td><td>通道3比较/捕获中断使能0:禁止通道3中断1:使能通道3中断</td></tr></table>

<table><tr><td>3</td><td>CH2IE</td><td>通道2比较/捕获中断使能0:禁止通道2中断1:使能通道2中断</td></tr><tr><td>2</td><td>CH1IE</td><td>通道1比较/捕获中断使能0:禁止通道1中断1:使能通道1中断</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDIF</td><td>CH2COMADDIF</td><td>CH1COMADDIF</td><td>CH0COMADDIF</td><td colspan="12">保留</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CH3OF</td><td>CH2OF</td><td>CH1OF</td><td>CH0OF</td><td>保留</td><td>BRKIF</td><td>TRGIF</td><td>CMTIF</td><td>CH3IF</td><td>CH2IF</td><td>CH1IF</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="3"></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3COMADDIF</td><td>通道3附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>30</td><td>CH2COMADDIF</td><td>通道2附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>29</td><td>CH1COMADDIF</td><td>通道1附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>28</td><td>CH0COMADDIF</td><td>通道0附加比较中断标志此标志由硬件置1软件清0。当通道0用于输出模式时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生注意:此标志仅用于复合PWM模式。</td></tr><tr><td>27:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CH3OF</td><td>通道3捕获溢出标志参见CH0OF描述。</td></tr><tr><td>11</td><td>CH2OF</td><td>通道2捕获溢出标志参见CH0OF描述。</td></tr><tr><td>10</td><td>CH1OF</td><td>通道1捕获溢出标志参见CH0OF描述。</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0。0:无捕获溢出中断发生。1:发生了捕获溢出中断。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>BRKIF</td><td>中止中断标志位当中止输入有效时,由硬件对该位置‘1’。当中止输入无效时,则该位可由软件清‘0’。0:无中止事件产生。1:中止输入上检测到有效电平。</td></tr><tr><td>6</td><td>TRGIF</td><td>触发中断标志当发生触发事件时,此标志会置1,此位由软件清0。当暂停模式使能时,触发输入的任意边沿都可以产生触发事件。否则,其它模式时,仅在触发输入端检测到有效边沿,产生触发事件。0:无触发事件产生。1:触发中断产生。</td></tr><tr><td>5</td><td>CMTIF</td><td>通道换相更新中断标志当通道换相更新事件发生时此标志位被硬件置1,此位由软件清0。0:无通道换相更新中断发生。1:通道换相更新中断发生。</td></tr><tr><td>4</td><td>CH3IF</td><td>通道3比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>3</td><td>CH2IF</td><td>通道2比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>2</td><td>CH1IF</td><td>通道1比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。当通道0在输入模式下时,读TIMERx_CH0CV会将此标志清0。0:无通道0中断发生。</td></tr></table>

1：通道 0 中断发生。

更新中断标志

此位在任何更新事件发生时由硬件置 1，软件清 0。

0：无更新中断发生。

1：发生更新中断。

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDG</td><td>CH2COMADDG</td><td>CH1COMADDG</td><td>CH0COMADDG</td><td colspan="12">保留</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>BRKG</td><td>TRGG</td><td>CMTG</td><td>CH3G</td><td>CH2G</td><td>CH1G</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="8"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3COMADDG</td><td>通道3附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>30</td><td>CH2COMADDG</td><td>通道2附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>29</td><td>CH1COMADDG</td><td>通道1附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>28</td><td>CH0COMADDG</td><td>通道0附加比较事件发生该位由软件置1,用于在通道0产生一个比较事件,由硬件自动清0。当此位被置1,CH0COMADDIF标志位被置1,若开启对应的中断和DMA,则发出相应的中断请求。0:不产生通道0附加比较事件1:发生通道0附加比较事件注意:此位仅用于复合PWM模式。</td></tr><tr><td>27:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>BRKG</td><td>产生中止事件该位由软件置1,用于产生一个中止事件,由硬件自动清0。当此位被置1时,POEN位被清0且BRKIF位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:不产生中止事件。1:产生中止事件。</td></tr><tr><td>6</td><td>TRGG</td><td>触发事件产生此位由软件置1,由硬件自动清0.当此位被置1,TIMERx_INTF寄存器的TRGIF标志位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:无触发事件产生。1:产生触发事件。</td></tr><tr><td>5</td><td>CMTG</td><td>通道换相更新事件发生此位由软件置1,由硬件自动清0.当此位被置1,通道捕获/比较控制寄存器(CHxEN,CHxNEN和CHxCOMCTL)的互补输出被更新。0:不产生通道控制更新事件。1:产生通道控制更新事件。</td></tr><tr><td>4</td><td>CH3G</td><td>通道3捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>3</td><td>CH2G</td><td>通道2捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>2</td><td>CH1G</td><td>通道1捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件。1:发生通道0捕获或比较事件。</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,如果选择了中央对齐或向上计数模式,计数器被清0。否则(向下计数模式)计数器将载入自动重载值,预分频计数器将同时被清除。0:无更新事件产生。1:产生更新事件。</td></tr></table>

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1COMADDSEN</td><td>CH0COMADDSEN</td><td colspan="12">保留</td></tr><tr><td colspan="16">保留</td></tr><tr><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>CH1COMCEN</td><td>CH1COMCTL[2:0]</td><td>CH1COMSEN</td><td>CH1COMFEN</td><td rowspan="2">CH1MS[1:0]</td><td>CH0COMCEN</td><td>CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2">CH0MS[1:0]</td></tr><tr><td colspan="2">CH1CAPFLT[3:0]</td><td colspan="2">CH1CAPPSC[1:0]</td><td colspan="2">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td></tr></table>


输出比较模式：


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>CH1COMADDSEN</td><td>通道1附加输出比较影子寄存器使能参考CH0COMADDSEN描述。</td></tr><tr><td>28</td><td>CH0COMADDSEN</td><td>通道0附加输出比较影子寄存器使能当此位被置1,TIMERx_CH0COMV_ADD寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0附加比较输出影子寄存器1:使能通道0附加比较输出影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=000时此位不能被改变。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CH1COMCEN</td><td>通道1输出比较清0使能参见CH0COMCEN描述。</td></tr><tr><td>14:12</td><td>CH1COMCTL[2:0]</td><td>通道1输出比较模式参见CH0COMCTL描述。</td></tr><tr><td>11</td><td>CH1COMSEN</td><td>通道1输出比较影子寄存器使能参见CH0COMSEN描述。</td></tr><tr><td>10</td><td>CH1COMFEN</td><td>通道1输出比较快速使能参见CH0COMFEN描述。</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH1EN位被清0)时这些位才可以写。00:通道1配置为输出01:通道1配置为输入,IS1映射在CI1FE1上10:通道1配置为输入,IS1映射在CI0FE1上11:通道1配置为输入,IS1映射在ITS上注意:当CH1MS[1:0]=11时,需要通过TRGS位(位于TIMERx_SMCFG寄存器)选择内部触发输入。</td></tr><tr><td>7</td><td>CH0COMCEN</td><td>通道0输出比较清0使能当此位被置1,当检测到ETIFP信号输入高电平时,O0CPRE参考信号被清00:禁止通道0输出比较清零1:使能通道0输出比较清零</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式此位定义了输出准备信号O0CPRE的输出比较模式,而O0CPRE决定了CH0_O、CH0_ON的值。另外,O0CPRE高电平有效,而CH0_O、CH0_ON通道的极性取决于CH0P、CH0NP位。000:时基。输出比较寄存器TIMERx_CH0CV与计数器TIMERx_CNT间的比较对O0CPRE不起作用001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为高。010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为低。011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE翻转。100:强制为低。强制O0CPRE为低电平101:强制为高。强制O0CPRE为高电平110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为高电平,否则为低电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为低电平,否则为高电平。111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为低电平,否则为高电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为高电平,否则为低电平。注意:在复合PWM模式下(CH0CPWMEN=1'b1和CH0MS=3'b000),通道0的PWM输出信号由TIMERx_CH0CV和TIMERx_CH0COMV_ADD寄存器共同确定。详细信息请参考复合PWM模式。如果配置在PWM模式下,只有当输出比较模式从时基模式变为PWM模式或者比较结果改变时,O0CPRE电平才改变。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=00(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>CH0COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0输出/比较影子寄存器1:使能通道0输出/比较影子寄存器仅在单脉冲模式下(SPM=1),可以在未确认影子寄存器的情况下使用PWM模式当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=00时此位不能被改变。</td></tr><tr><td>2</td><td>CH0COMFEN</td><td>通道0输出比较快速使能当该位为1时,如果通道配置为PWM0模式或者PWM1模式,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH0_O被设置为比较电平而与比较结果无关。0:禁止通道0输出比较快速.1:使能通道0输出比较快速。</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道0I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH0EN位被清0)时这些位才可写。</td></tr></table>

00：通道 0 配置为输出

01：通道 0 配置为输入，IS0映射在 CI0FE0 上

10：通道 0 配置为输入，IS0映射在 CI1FE0 上

11：通道 0 配置为输入，IS0映射在 ITS 上

注意：当 CH0MS[1:0]=11 时，需要通过 TRGS 位（位于 TIMERx_SMCFG 寄存器）选择内部触发输入

输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述。</td></tr><tr><td>11:10</td><td>CH1CAPPSC[1:0]</td><td>通道1输入捕获预分频器参见CH0CAPPSC描述。</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择与输出模式相同。</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制CI0输入信号可以通过数字滤波器进行滤波,该位域配置滤波参数。数字滤波器的基本原理:根据$f_{SAMP}$对CI0输入信号进行连续采样,并记录信号相同电平的次数。达到该位配置的滤波参数后,认为是有效电平。滤波器参数配置如下:</td></tr></table>

<table><tr><td>CHOCAPFLT [3:0]</td><td>采样次数</td><td>fSAMP</td></tr><tr><td>4&#x27;b0000</td><td></td><td>无滤波器</td></tr><tr><td>4&#x27;b0001</td><td>2</td><td></td></tr><tr><td>4&#x27;b0010</td><td>4</td><td>fCK_TIMER</td></tr><tr><td>4&#x27;b0011</td><td>8</td><td></td></tr><tr><td>4&#x27;b0100</td><td>6</td><td rowspan="2">$f_{DTS}/2$</td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6</td><td rowspan="2">$f_{DTS}/4$</td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6</td><td rowspan="2">$f_{DTS}/8$</td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5</td><td></td></tr><tr><td>4&#x27;b1011</td><td>6</td><td>$f_{DTS}/16$</td></tr><tr><td>4&#x27;b1100</td><td>8</td><td></td></tr><tr><td>4&#x27;b1101</td><td>5</td><td></td></tr><tr><td>4&#x27;b1110</td><td>6</td><td>$f_{DTS}/32$</td></tr><tr><td>4&#x27;b1111</td><td>8</td><td></td></tr></table>

这 2 位定义了通道 0 输入的预分频系数。当 TIMERx_CHCTL2 寄存器中的 CH0EN=0 时，则预分频器复位。

00：无预分频器，捕获输入口上检测到的每一个边沿都触发一次捕获。

01：每 2 个事件触发一次捕获。

10：每 4 个事件触发一次捕获。

11：每 8 个事件触发一次捕获。

1:0 CH0MS[1:0] 通道 0 模式选择

与输出比较模式相同。

## 通道控制寄存器 1（TIMERx_CHCTL1）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1COMADDSEN</td><td>CH0COMADDSEN</td><td colspan="12">保留</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3COM CEN</td><td colspan="3">CH3COMCTL[2:0]</td><td>CH3COM SEN</td><td>CH3COM FEN</td><td rowspan="2" colspan="2">CH3MS[1:0]</td><td>CH2COM CEN</td><td colspan="3">CH2COMCTL[2:0]</td><td>CH2COM SEN</td><td>CH2COM FEN</td><td rowspan="2" colspan="2">CH2MS[1:0]</td></tr><tr><td colspan="4">CH3CAPFLT[3:0]</td><td colspan="2">CH3CAPPSC[1:0]</td><td colspan="4">CH2CAPFLT[3:0]</td><td colspan="2">CH2CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>CH1COMADDSEN</td><td>通道1附加输出比较影子寄存器使能参考CH0COMADDSEN描述。</td></tr><tr><td>28</td><td>CH0COMADDSEN</td><td>通道0附加输出比较影子寄存器使能当此位被置1,TIMERx_CH0COMV_ADD寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0附加比较输出影子寄存器1:使能通道0附加比较输出影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=000时此位不能被改变。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CH3COMCEN</td><td>通道3输出比较清0使能参见CH0COMCEN描述。</td></tr><tr><td>14:12</td><td>CH3COMCTL[2:0]</td><td>通道3输出比较模式参见CH0COMCTL描述。</td></tr><tr><td>11</td><td>CH3COMSEN</td><td>通道3输出比较影子寄存器使能参见CH0COMSEN描述。</td></tr><tr><td>10</td><td>CH3COMFEN</td><td>通道3输出比较快速使能参见CH0COMFEN描述。</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择这些位定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH3EN位被清0)时这些位才可以写。00:通道3配置为输出01:通道3配置为输入,IS3映射在CI3FE3上10:通道3配置为输入,IS3映射在CI2FE3上11:通道3配置为输入,IS3映射在ITS上注意:当CH3MS[1:0]=11时,需要通过TRGS位(位于TIMERx_SMCFG寄存器)选择内部触发输入</td></tr><tr><td>7</td><td>CH2COMCEN</td><td>通道2输出比较清0使能当此位被置1,当检测到ETIFP输入高电平时,O2CPRE参考信号被清00:使能通道2输出比较清零1:禁止通道2输出比较清零</td></tr><tr><td>6:4</td><td>CH2COMCTL[2:0]</td><td>通道2输出比较模式此位定义了输出准备信号O2CPRE的输出比较模式,而O2CPRE决定了CH2_O、CH2_ON的值。另外,O2CPRE高电平有效,而CH2_O、CH2_ON通道的极性取决于CH2P、CH2NP位。000:时基。输出比较寄存器TIMERx_CH2CV与计数器TIMERx_CNT间的比较对O2CPRE不起作用001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为高。010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为低。011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE翻转。100:强制为低。强制O2CPRE为低电平101:强制为高。强制O2CPRE为高电平110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为高电平,否则为低电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为低电平,否则为高电平。111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为低电平,否则为高电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为高电平,否则为低电平。注意:在复合PWM模式下(CH2CPWMEN=1'b1和CH2MS=3'b000),通道2的PWM输出信号由TIMERx_CH2CV和TIMERx_CH2COMV_ADD寄存器共同确定。详细信息请参考复合PWM模式。如果配置在PWM模式下,只有当输出比较模式从时基模式变为PWM模式或者比较结果改变时,O2CPRE电平才改变。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH2MS=00(比较模式)时此位不</td></tr></table>

能被改变。

<table><tr><td>3</td><td>CH2COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH2CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道2输出/比较影子寄存器1:使能通道2输出/比较影子寄存器仅在单脉冲模式下(SPM=1),可以在未确认影子寄存器情况下使用PWM模式当TIMERx_CCHP寄存器的PROT[1:0]=11且CH2MS=00时此位不能被改变。</td></tr><tr><td>2</td><td>CH2COMFEN</td><td>通道2输出比较快速使能当该位为1时,如果通道配置为PWM0模式或者PWM1模式,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH2_O被设置为比较电平而与比较结果无关。0:禁止通道2输出比较快速.1:使能通道2输出比较快速。</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td>通道2I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH2EN位被清0)时这些位才可写。00:通道2配置为输出01:通道2配置为输入,IS2映射在CI2FE2上10:通道2配置为输入,IS2映射在CI3FE2上11:通道2配置为输入,IS2映射在ITS上.注意:当CH2MS[1:0]=11时,需要通过TRGS位(位于TIMERx_SMCFG寄存器)选择内部触发输入</td></tr></table>

输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>CH3CAPFLT[3:0]</td><td>通道3输入捕获滤波控制参见CH0CAPFLT描述。</td></tr><tr><td>11:10</td><td>CH3CAPPSC[1:0]</td><td>通道3输入捕获预分频器参见CH0CAPPSC描述。</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择与输出模式相同。</td></tr><tr><td>7:4</td><td>CH2CAPFLT[3:0]</td><td>通道2输入捕获滤波控制CI2输入信号可以通过数字滤波器进行滤波,该位域配置滤波参数。数字滤波器的基本原理:根据$f_{SAMP}$对CI2输入信号进行连续采样,并记录信号相同电平的次数。达到该位配置的滤波参数后,认为是有效电平。滤波器参数配置如下:</td></tr><tr><td colspan="2"></td><td>CH2CAPFLT [3:0] 采样次数 $f_{SAMP}$4&#x27;b0000 无滤波器</td></tr></table>

<table><tr><td></td><td></td><td>4&#x27;b0001</td><td>2</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b0010</td><td>4</td><td>fCK_TIMER</td></tr><tr><td></td><td></td><td>4&#x27;b0011</td><td>8</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b0100</td><td>6</td><td>fDTS/2</td></tr><tr><td></td><td></td><td>4&#x27;b0101</td><td>8</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b0110</td><td>6</td><td>fDTS/4</td></tr><tr><td></td><td></td><td>4&#x27;b0111</td><td>8</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b1000</td><td>6</td><td>fDTS/8</td></tr><tr><td></td><td></td><td>4&#x27;b1001</td><td>8</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b1010</td><td>5</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b1011</td><td>6</td><td>fDTS/16</td></tr><tr><td></td><td></td><td>4&#x27;b1100</td><td>8</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b1101</td><td>5</td><td></td></tr><tr><td></td><td></td><td>4&#x27;b1110</td><td>6</td><td>fDTS/32</td></tr><tr><td></td><td></td><td>4&#x27;b1111</td><td>8</td><td></td></tr><tr><td rowspan="6">3:2</td><td rowspan="6">CH2CAPPSC[1:0]</td><td colspan="3">通道2输入捕获预分频器</td></tr><tr><td colspan="3">这2位定义了通道2输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH2E=0时,则预分频器复位。</td></tr><tr><td colspan="3">00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获。</td></tr><tr><td colspan="3">01:每2个事件触发一次捕获。</td></tr><tr><td colspan="3">10:每4个事件触发一次捕获。</td></tr><tr><td colspan="3">11:每8个事件触发一次捕获。</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td colspan="3">通道2模式选择与输出比较模式相同。</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3NP</td><td>CH3NEN</td><td>CH3P</td><td>CH3EN</td><td>CH2NP</td><td>CH2NEN</td><td>CH2P</td><td>CH2EN</td><td>CH1NP</td><td>CH1NEN</td><td>CH1P</td><td>CH1EN</td><td>CH0NP</td><td>CH0NEN</td><td>CH0P</td><td>CH0EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>Bits</td><td>Fields</td><td>Descriptions</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CH3NP</td><td>通道 3 互补输出极性参考 CH0NP 描述。</td></tr><tr><td>14</td><td>CH3NEN</td><td>通道 3 互补输出使能</td></tr><tr><td>13</td><td>CH3P</td><td>通道3极性参考CHOP描述。</td></tr><tr><td>12</td><td>CH3EN</td><td>通道3使能参考CH0EN描述。</td></tr><tr><td>11</td><td>CH2NP</td><td>通道2互补输出极性参考CH0NP描述。</td></tr><tr><td>10</td><td>CH2NEN</td><td>通道2互补输出使能参考CH0NEN描述。</td></tr><tr><td>9</td><td>CH2P</td><td>通道2极性参考CHOP描述。</td></tr><tr><td>8</td><td>CH2EN</td><td>通道2使能参考CH0EN描述。</td></tr><tr><td>7</td><td>CH1NP</td><td>通道1互补输出极性参考CH0NP描述。</td></tr><tr><td>6</td><td>CH1NEN</td><td>通道1互补输出使能参考CH0NEN描述。</td></tr><tr><td>5</td><td>CH1P</td><td>通道1极性参考CHOP描述。</td></tr><tr><td>4</td><td>CH1EN</td><td>通道1使能参考CH0EN描述。</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,此位定义了互补输出信号的极性。0:通道0互补输出高电平为有效电平1:通道0互补输出低电平为有效电平当通道0配置为输入模式时,此位和CHOP联合使用,作为输入信号CI0的极性选择控制信号。当TIMERxCCHP寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr><tr><td>2</td><td>CH0NEN</td><td>通道0互补输出使能当通道0配置为输出模式时,将此位置1使能通道0的互补输出。0:禁止通道0互补输出。1:使能通道0互补输出。</td></tr><tr><td>1</td><td>CHOP</td><td>通道0极性当通道0配置为输出模式时,此位定义了输出信号极性。0:通道0高电平为有效电平1:通道0低电平为有效电平当通道0配置为输入模式时,此位定义了CI0信号极性。[CH0NP, CHOP]将选择CI0FE0或者CI1FE0的有效边沿或者捕获极性。</td></tr></table>

[CH0NP==0, CH0P==0]：把 CIxFE0 的上升沿作为捕获或者从模式下触发的有效信号，并且 CIxFE0 不会被翻转。

[CH0NP==0, CH0P==1]：把 CIxFE0 的下降沿作为捕获或者从模式下触发的有效信号，并且 CIxFE0 会被翻转。

[CH0NP==1, CH0P==0]：保留。

[CH0NP==1, CH0P==1]：把 CIxFE0 的上升沿和下降沿都作为捕获或者从模式下触发的有效信号，并且 CIxFE0 不会被翻转。

当 TIMERx_CCHP 寄存器的 PROT [1:0]=11 或 10 时此位不能被更改。

当通道 0 配置为输出模式时，将此位置 1 使能 CH0_O 信号有效。当通道 0 配置为输入模式时，将此位置 1 使能通道 0 上的捕获事件。

$0 { : }$ 禁止通道 0。

1：使能通道 0。

## 计数器寄存器（TIMERx_CNT）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>

## 预分频寄存器（TIMERx_PSC）

地址偏移： 0x28

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

## 重复计数寄存器（TIMERx_CREP）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>CREP[7:0]</td><td>重复计数器的值这些位定义了更新事件的产生速率。重复计数器计数值减为0时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。</td></tr></table>

通道 2 捕获/比较寄存器（TIMERx_CH2CV）

## 通道 0 捕获/比较寄存器（TIMERx_CH0CV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 1 捕获/比较寄存器（TIMERx_CH1CV）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH1VAL[15:0]</td><td>通道1的捕获或比较值当通道1配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>


地址偏移：0x3C


复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH2VAL[15:0]</td><td>通道2的捕获或比较值当通道2配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 3 捕获/比较寄存器（TIMERx_CH3CV）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH3VAL[15:0]</td><td>通道3的捕获或比较值当通道3配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道3配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

互补通道保护寄存器（TIMERx_CCHP）

地址偏移：0x44

复位值： 0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>POEN</td><td>OAEN</td><td>BRKP</td><td>BRKEN</td><td>ROS</td><td>IOS</td><td colspan="2">PROT[1:0]</td><td colspan="8">DTCFG[7:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15</td><td>POEN</td><td>所有的通道输出使能该位通过以下方式置1:-写1置位-如果OAEN=1,则在下一次更新事件发生时置1.该位通过以下方式清0:-写0清0-有效的中止输入(异步)如果一个通道配置为输出模式,如果设置了相应的使能位(TIMERx_CHCTL2寄存器的CHxEN, CHxNEN位),则开启CHx_O和CHx_ON输出。0:禁止通道输出1:使能通道输出注意:仅当CHxMS[1:0]=2&#x27;b00时该位有效</td></tr><tr><td>14</td><td>OAEN</td><td>自动输出使能0:POEN位只能使用软件方式置11:如果中止输入无效,下一次更新事件发生时,POEN位置1此位只有在TIMERx_CCHP寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>13</td><td>BRKP</td><td>中止极性此位定义了中止输入信号BRKIN的极性。0:中止输入低电平有效1:中止输入高电平有效</td></tr><tr><td>12</td><td>BRKEN</td><td>中止使能此位置1使能中止事件和CKM时钟失败事件输入。0:禁能中止输入1:使能中止输入此位只有在TIMERx_CCHP寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>11</td><td>ROS</td><td>运行模式下“关闭状态”使能当POEN位被置1(运行模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表22-5。0:输出“关闭状态”禁能。当CHxEN或者CHxNEN位被清零,对应通道为输出“禁能状态”。1:输出“关闭状态”使能。当CHxEN或者CHxNEN位被清零,对应通道为输出“关闭状态”。</td></tr></table>

此位在 TIMERx_CCHP 寄存器的 PROT [1:0]=10 或 11 时不能被更改。

<table><tr><td>10</td><td>IOS</td><td>空闲模式下“关闭状态”使能当 POEN 位被清 0(空闲模式),此位可以被置 1 来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表22-6。0:输出“关闭状态”禁能。当 CHxEN 和 CHxNEN 位均被清零,对应通道为输出“禁能状态”。1:输出“关闭状态”使能。不论 CHxEN 和 CHxNEN 位的值,对应通道为输出“关闭状态”。此位在 TIMERx_CCHP 寄存器的 PROT [1:0]=10 或 11 时不能被更改。</td></tr></table>

<table><tr><td>9:8</td><td>PROT[1:0]</td><td>互补寄存器保护控制这两位定义了寄存器的写保护特性。00:禁能保护模式。无写保护。01:PROT 模式 0。TIMERx_CTL1 寄存器中 ISOx/ISOxN 位,TIMERx_CCHP 寄存器中 BRKEN/BRKP/OAEN/DTCFG 位写保护。10:PROT 模式 1。除了 PROT 模式 0 下的寄存器写保护外,还有 TIMERx_CHCTL2 寄存器中 CHxP/CHxNP 位(如果相应通道配置为输出模式),TIMERx_CCHP 寄存器中 ROS/IOS 位写保护。11:PROT 模式 2。除了 PROT 模式 1 下的寄存器写保护外,还有 TIMERx_CHCTLR0/1 中 CHxCOMCTL/CHxCOMSEN 位(如果相关通道配置为输出模式)写保护。系统复位后这两位只能被写一次,一旦 TIMERx_CCHP 寄存器被写入,这两位被写保护。</td></tr></table>

DTCFG值和死区时间的关系如下：

<table><tr><td>DTCFG[7:5]</td><td>The duration of dead-time</td></tr><tr><td>3&#x27;b0xx</td><td>DTCFG[7:0] * $t_{DTS\_CK}$</td></tr><tr><td>3&#x27;b10x</td><td>(64+ DTCFG[5:0]) * $t_{DTS\_CK}$*2</td></tr><tr><td>3&#x27;b110</td><td>(32+ DTCFG[4:0]) * $t_{DTS\_CK}$*8</td></tr><tr><td>3&#x27;b111</td><td>(32+ DTCFG[4:0]) * $t_{DTS\_CK}$*16</td></tr></table>


注意：



1. tDTS_CK 是 DTS_CK 的周期，由 TIMERx_CTL0 中的 CKDIC[1:0]定义。



2. 此位只有在 TIMERx_CCHP 寄存器的 PROT [1:0]=00 时才可修改。


## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>DMATC[4:0]</td><td>保留</td><td>DMATA [4:0]</td></tr><tr><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>DMATC [4:0]</td><td>DMA传输计数该位域定义了DMA访问(读写)TIMERx_DMATB寄存器的数量n,n=(DMATC[4:0]+1).DMATC [4:0]从5&#x27;b0_0000到5&#x27;b1_0001.</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DMATA [4:0]</td><td>DMA传输起始地址该位域定义了DMA访问TIMERx_DMATB寄存器的第一个地址。当通过TIMERx_DMA第一次访问时,访问的就是该位域指定的地址。第二次访问TIMERx_DMATB时,将访问起始地址+0x4。</td></tr></table>

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>DMATB [15:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问。传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

## 通道 0 附加比较寄存器（TIMERx_CH0COMV_ADD）

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH0COMVAL_ADD[15:0]</td><td>通道0附加比较值当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>


通道 1 附加比较寄存器（TIMERx_CH1COMV_ADD）



地址偏移：0x68



复位值：0x0000 0000



该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH1COMVAL_ADD[15:0]</td><td>通道1附加比较值当通道1附加配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>

## 通道 2 附加比较寄存器（TIMERx_CH2COMV_ADD）

地址偏移：0x6C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr></table>

CH2COMVAL_ADD 通道2附加比较值

当通道2附加配置为输出模式时，这些位包含了即将和计数器比较的值。使能相应影子寄存器后，影子寄存器值随每次更新事件更新。

注意：该寄存器仅用于复合PWM模式（当CH0CPWMEN=1时）。

## 通道 3 附加比较寄存器（TIMERx_CH3COMV_ADD）

地址偏移：0x70

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH3COMVAL_ADD[15:0]</td><td>通道3附加比较值当通道3附加配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>

## 控制寄存器 2（TIMERx_CTL2）

地址偏移：0x74

复位值：0x0FF0 00FF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3C PWMEN</td><td>CH2C PWMEN</td><td>CH1C PWMEN</td><td>CH0C PWMEN</td><td colspan="12">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3CPWMEN</td><td>通道 3 复合 PWM 模式使能0:通道 3 复合 PWM 模式禁能1:通道 3 复合 PWM 模式使能</td></tr><tr><td>30</td><td>CH2CPWMEN</td><td>通道 2 复合 PWM 模式使能0: 通道2复合PWM模式禁能1: 通道2复合PWM模式使能</td></tr><tr><td>29</td><td>CH1CPWMEN</td><td>通道1复合PWM模式使能0: 通道1复合PWM模式禁能1: 通道1复合PWM模式使能</td></tr><tr><td>28</td><td>CH0CPWMEN</td><td>通道0复合PWM模式使能0: 通道0复合PWM模式禁能1: 通道0复合PWM模式使能</td></tr><tr><td>27:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>OUTSEL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效。0:无影响。</td></tr><tr><td>0</td><td>OUTSEL</td><td>输出值选择位此位由软件写1或清0。1:如果POEN位与IOS位均为0,则输出无效。0:无影响。</td></tr></table>
