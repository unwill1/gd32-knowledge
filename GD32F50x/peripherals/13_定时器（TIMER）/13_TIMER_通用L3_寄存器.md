## 13.3.5. TIMERx 寄存器(x=15/16)

TIMER15 基地址：0x4001 5000

TIMER16 基地址：0x4000 1800

控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="2">CAM[1:0]</td><td>DIR</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置 CKDIV,规定定时器时钟(TIMER_CK)与死区时间和采样时钟(DTS)之间的分频系数,死区发生器和数字滤波器会用到 DTS 时间。00:<eq>f_{DTS}=f_{TIMER\_CK}</eq>01:<eq>f_{DTS}=f_{TIMER\_CK}/2</eq>10:<eq>f_{DTS}=f_{TIMER\_CK}/4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:5</td><td>CAM[1:0]</td><td>计数器对齐模式选择00:无中央对齐模式(边沿对齐模式)。DIR 位指定了计数方向。01:中央对齐向下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=3'b000),只有在向下计数时,通道的比较中断标志置 110:中央对齐向上计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=3'b000),只有在向上计数时,通道的比较中断标志置 111:中央对齐上下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),在向上和向下计数时,通道的比较中断标志都会置1当计数器使能以后,该位不能从0x00切换到非0x00状态。</td></tr><tr><td>4</td><td>DIR</td><td>方向0:向上计数1:向下计数当计数器配置为中央对齐模式时,该位为只读。</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0:更新事件发生后,计数器继续计数1:在下一次更新事件发生时,CEN硬件清零并且计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该为,选择更新事件源.0:使能后,下述任一事件产生更新中断或DMA请求:-UPG位被置1-计数器上溢或者下溢-从模式控制器产生的更新1:使能后只有计数器上溢才产生更新中断或DMA请求</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新该位用来使能或禁能更新事件的产生0:更新事件使能.当以下事件之一发生时,更新事件产生,具有缓存的寄存器被装入它们的预装载值:-UPG位被置1-计数器上溢或者下溢-从模式控制器产生一个更新事件1:更新事件禁能。带有缓存的寄存器保持原有值,如果UPG位被置1或者从模式控制器产生一个硬件复位事件,计数器和预分频器被重新初始化</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0:计数器禁能1:计数器使能在软件将CEN位置1后,外部时钟模式才能工作。触发模式可以自动地通过硬件设置CEN位。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CCUC[2:1]</td><td colspan="4">保留</td><td>MMC[3]</td><td colspan="9">保留</td></tr><tr><td colspan="5">rw</td><td colspan="11">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>ISO1</td><td>ISO0N</td><td>ISO0</td><td>TI0S</td><td colspan="3">MMC[2:0]</td><td>DMAS</td><td>CCUC[0]</td><td>保留</td><td>CCSE</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CCUC[2:1]</td><td>换相控制影子寄存器更新控制请参考 CCUC [0]的描述。</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>25</td><td>MMC[3]</td><td>主模式控制请参考 MMC[2:0]的描述。</td></tr><tr><td>24:11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10</td><td>ISO1</td><td>通道 1 的空闲状态输出参考 ISO0 位。</td></tr><tr><td>9</td><td>ISO0N</td><td>通道 0 的互补通道空闲状态输出0:当 POEN 复位,CH0_ON 输出低电平1:当 POEN 复位,CH0_ON 输出高电平此位只有在 TIMERx_CCHP0 寄存器的 PROT[1:0]位为 00 的时候可以被更改。</td></tr><tr><td>8</td><td>ISO0</td><td>通道 0 的空闲状态输出0:当 POEN 复位,CH0_O 输出低电平1:当 POEN 复位,CH0_O 输出高电平如果 CH0_ON 生效,一个死区时间后 CH0_O 输出改变。此位只有在 TIMERx_CCHP0 寄存器的 PROT[1:0]位为 00 的时候可以被更改。</td></tr><tr><td>7</td><td>TIOS</td><td>通道 0 触发输入选择0:选择 TIMERx_CH0 引脚作为通道 0 的触发输入1:选择 TIMERx_CH0,CH1 和 CH2 引脚异或的结果作为通道 0 的触发输入</td></tr><tr><td>6:4</td><td>MMC[2:0]</td><td>主模式控制这些位控制 TRGO 信号的选择,TRGO 信号由主定时器发给从定时器用于同步功能0000:复位。TIMERx_SWEVG 寄存器的 UPG 位被置 1 或从模式控制器产生复位触发一次 TRGO 脉冲,后一种情况下,TRGO 上的信号相对实际的复位会有一个延迟。0001:使能。此模式可用于同时启动多个定时器或控制在一段时间内使能从定时器。主模式控制器选择计数器使能信号作为触发输出 TRGO。当 CEN 控制位被置 1 或者暂停模式下触发输入为高电平时,计数器使能信号被置 1。在暂停模式下,计数器使能信号受控于触发输入,在触发输入和 TRGO 上会有一个延迟,除非选择了主/从模式。0010:更新。主模式控制器选择更新事件作为 TRGO。0011:捕获/比较脉冲.通道0在发生一次捕获或一次比较成功时,主模式控制器产生一个TRGO脉冲0100:比较。在这种模式下主模式控制器选择O0CPRE信号被用于作为触发输出TRGO0101:比较。在这种模式下主模式控制器选择O1CPRE信号被用于作为触发输出TRGO1000:保留1001:在这种模式下主模式控制器选择软同步事件信号(设置SWSYNCG位为1产生)作为触发输出TRGO。1010~1111:保留</td></tr><tr><td>3</td><td>DMAS</td><td>DMA请求源选择0:当通道捕获/比较事件发生时,发送通道CHx/MCHx的DMA请求.1:当更新事件发生,发送通道CHx/MCHx的DMA请求</td></tr><tr><td>2</td><td>CCUC[0]</td><td>换相控制影子寄存器更新控制当换相控制影子寄存器(CHxEN,MCHxEN和CHxCOMCTL位)使能(CCSE=1),这些影子寄存器更新控制如下:000:CMTG位被置1时,更新影子寄存器001:当CMTG位被置1或检测到TRGI上升沿时,影子寄存器更新100:当计数器上溢事件发生时,影子寄存器更新101:当计数器下溢事件发生时,影子寄存器更新110:当计数器上溢/下溢事件发生时,影子寄存器更新其他值:保留当通道没有互补输出时,此位无效。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>0</td><td>CCSE</td><td>换相控制影子使能0:影子寄存器CHxEN、MCHxEN和CHxCOMCTL位禁能.1:影子寄存器CHxEN、MCHxEN和CHxCOMCTL位使能.如果这些位已经被写入了,换相事件到来时这些位才被更新当通道没有互补输出时,此位无效</td></tr></table>

## 从模式配置寄存器（TIMERx_SMCFG）

地址偏移：0x08

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>MSM</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>MSM</td><td>主-从模式该位被用来同步被选择的定时器同时开始计数。通过TRIGI和TRGO,定时器被连接在一起,TRGO用做启动事件。0:主从模式禁能1:主从模式使能</td></tr><tr><td>6:0</td><td>保留</td><td>必须保持复位值.</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1COMADDIE</td><td>CH0COMADDIE</td><td colspan="3">保留</td><td>MCH0DEN</td><td colspan="3">保留</td><td>MCH0IE</td><td colspan="4">保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>TRGDEN</td><td>CMTDEN</td><td colspan="2">保留</td><td>CH1DEN</td><td>CH0DEN</td><td>UPDEN</td><td>BRKIE</td><td>TRGIE</td><td>CMTIE</td><td colspan="2">保留</td><td>CH1IE</td><td>CH0IE</td><td>UPIE</td></tr><tr><td></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29</td><td>CH1COMADDIE</td><td>通道1附加比较中断使能0:禁止通道1附加比较中断1:使能通道1附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>28</td><td>CH0COMADDIE</td><td>通道0附加比较中断使能0:禁止通道0附加比较中断1:使能通道0附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>24</td><td>MCH0DEN</td><td>多模式通道0比较/捕获DMA请求使能0:禁止多模式通道0比较/捕获DMA请求1:使能多模式通道0比较/捕获DMA请求注意:此DMA使能位仅用于多模式通道输入和输出独立模式(当MCH0MSEL[1:0]=2b'00时)。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>20</td><td>MCH0IE</td><td>多模式通道0比较/捕获中断使能0:禁止多模式通道0中断1:使能多模式通道0中断注意:此中断使能位仅用于多模式通道输入和输出独立模式(当MCH0MSEL[1:0]=2b'00时)。</td></tr><tr><td>19:15</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>14</td><td>TRGDEN</td><td>触发DMA请求使能0:禁止触发DMA请求1:使能触发DMA请求</td></tr><tr><td>13</td><td>CMTDEN</td><td>换相DMA更新请求使能0:禁止换相DMA更新请求1:使能换相DMA更新请求</td></tr><tr><td>12:11</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>10</td><td>CH1DEN</td><td>通道1比较/捕获DMA请求使能0:禁止通道1比较/捕获DMA请求1:使能通道1比较/捕获DMA请求</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>BRKIE</td><td>中止中断使能0:禁止中止中断1:使能中止中断</td></tr><tr><td>6</td><td>TRGIE</td><td>触发中断使能0:禁止触发中断1:使能触发中断</td></tr><tr><td>5</td><td>CMTIE</td><td>换相更新中断使能0:禁止换相更新中断1:使能换相更新中断</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>2</td><td>CH1IE</td><td>通道1比较/捕获中断使能0:禁止通道1中断1:使能通道1中断</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1COMADDIF</td><td>CH0COMADDIF</td><td colspan="3">保留</td><td>MCH0OF</td><td colspan="3">保留</td><td>MCH0IF</td><td colspan="4">保留</td></tr><tr><td colspan="2"></td><td>rc_w0</td><td>rc_w0</td><td colspan="3"></td><td>rc_w0</td><td colspan="3"></td><td>rc_w0</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>CH1OF</td><td>CH0OF</td><td>保留</td><td>BRKIF</td><td>TRGIF</td><td>CMTIF</td><td colspan="2">保留</td><td>CH1IF</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="5"></td><td>rc_w0</td><td>rc_w0</td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td colspan="2"></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29</td><td>CH1COMADDIF</td><td>通道1附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>28</td><td>CH0COMADDIF</td><td>通道0附加比较中断标志此标志由硬件置1软件清0。当通道0用于输出模式时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生注意:此标志仅用于复合PWM模式。</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>24</td><td>MCH0OF</td><td>多模式通道0捕获溢出标志当通道0被配置为输入模式时,在MCH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0。0:无捕获溢出中断发生1:捕获溢出中断发生</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>MCH0IF</td><td>多模式通道0比较/捕获中断标志此标志由硬件置1软件清0。当多模式通道0用于输入模式时,捕获事件发生时此标志位置1;当多模式通道0用于输出模式时,此标志位在一个比较事件发生时置1。当多模式通道0在输入模式下时,通过读TIMERx_MCH0CV寄存器可以清零该位。0:无多模式通道0中断发生1:多模式通道0中断发生</td></tr><tr><td>19:11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10</td><td>CH1OF</td><td>通道1捕获溢出标志参见CH0OF描述</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清00:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7</td><td>BRKIF</td><td>BREAK中断标志位一旦BREAK输入有效,由硬件对该位置‘1’。如果BREAK输入无效,则该位可由软件清‘0’。0:无BREAK事件产生1:BREAK输入上检测到有效电平</td></tr><tr><td>6</td><td>TRGIF</td><td>触发中断标志当发生触发事件时,此标志由硬件置1。此位由软件清0。当从模式控制器处于除暂停模式外的其它模式时,在触发输入端检测到有效边沿,产生触发事件。当从模式控制器处于暂停模式时,触发输入的任意边沿都可以产生触发事件。0:无触发事件产生1:触发中断产生</td></tr><tr><td>5</td><td>CMTIF</td><td>通道换相更新中断标志当通道换相更新事件发生时此标志位被硬件置1,此位由软件清0。0:无通道换相更新中断发生1:通道换相更新中断发生</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>2</td><td>CH1IF</td><td>通道1比较/捕获中断标志参见CH0IF描述</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。当通道0在输入模式下时,通过读TIMERx_CH0CV寄存器可以清零该位。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在任何更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1COMADDG</td><td>CH0COMADDG</td><td colspan="7">保留</td><td>MCH0G</td><td colspan="4">保留</td></tr><tr><td colspan="2"></td><td>w</td><td>w</td><td colspan="7"></td><td colspan="5">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>BRKG</td><td>TRGG</td><td>CMTG</td><td colspan="2">保留</td><td>CH1G</td><td>CH0G</td><td>UPG</td></tr><tr><td colspan="8"></td><td>w</td><td>w</td><td>w</td><td colspan="2"></td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29</td><td>CH1COMADDG</td><td>通道1附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>28</td><td>CH0COMADDG</td><td>通道0附加比较事件发生该位由软件置1,用于在通道0产生一个比较事件,由硬件自动清0。当此位被置1,CH0COMADDIF标志位被置1,若开启对应的中断和DMA,则发出相应的中断请求。0:不产生通道0附加比较事件1:发生通道0附加比较事件注意:此位仅用于复合 PWM 模式。</td></tr><tr><td>27:21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>MCH0G</td><td>多模式通道 0 互补捕获或比较事件发生该位由软件置 1,用于在多模式通道 0 产生一个捕获/比较事件,由硬件自动清 0。当此位被置 1,MCH0IF 标志位被置 1,若开启相应的中断和 DMA,则发出相应的中断和 DMA 请求。此外,如果多模式通道 0 配置为输入模式,计数器的当前值被 TIMERx_MCH0CV 寄存器捕获,如果 MCH0IF 标志位已经为 1,则 MCH0OF 标志位被置 1。0:不产生多模式通道 0 捕获或比较事件1:发生多模式通道 0 捕获或比较事件</td></tr><tr><td>19:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>BRKG</td><td>产生 BREAK 事件该位由软件置 1,用于产生一个 BREAK 事件,由硬件自动清 0。当此位被置 1时,POEN 位被清 0 且 BRKIF 位被置 1,若开启对应的中断和 DMA,则产生相应的中断和 DMA 传输。0:不产生 BREAK 事件1:产生 BREAK 事件</td></tr><tr><td>6</td><td>TRGG</td><td>触发事件产生此位由软件置 1,由硬件自动清 0. 当此位被置 1,TIMERx_INTF 寄存器的 TRGIF标志位被置 1,若开启对应的中断和 DMA,则产生相应的中断和 DMA 传输。0:无触发事件产生1:产生触发事件</td></tr><tr><td>5</td><td>CMTG</td><td>通道换相更新事件发生此位由软件置 1,由硬件自动清 0. 当此位被置 1,通道捕获/比较控制寄存器(CHxEN、MCHxEN 和 CHxCOMCTL)的互补输出被更新(根据 TIMERx_CTL1 中 CCSE 值)。0:不产生通道控制更新事件1:产生通道控制更新事件</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>2</td><td>CH1G</td><td>通道 1 捕获或比较事件发生参见 CH0G 描述。</td></tr><tr><td>1</td><td>CH0G</td><td>通道 0 捕获或比较事件发生该位由软件置 1,用于在通道 0 产生一个捕获/比较事件,由硬件自动清 0。当此位被置 1,CH0IF 标志位被置 1,若开启对应的中断和 DMA,则发出相应的中断和 DMA 请求。此外,如果通道 0 配置为输入模式,计数器的当前值被 TIMERx_CH0CV 寄存器捕获,如果 CH0IF 标志位已经为 1,则 CH0OF 标志位被置 1。</td></tr></table>

0：不产生通道 0 捕获或比较事件

1：发生通道 0 捕获或比较事件

此位由软件置 1，被硬件自动清 0。当此位被置 1，向上计数模式，计数器被清 0，

预分频计数器将同时被清除。

0：无更新事件产生

1：产生更新事件

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">CH1MS[2]</td><td rowspan="2">CH0MS[2]</td><td>CH1COMADDSEN</td><td>CH0COMADDSEN</td><td>CH1ADDUPS</td><td>CH0ADDUPS</td><td rowspan="2">保留</td><td>CH1COMCTL[3]</td><td rowspan="2" colspan="7">保留</td><td>CH0COMCTL[3]</td></tr><tr><td colspan="4">保留</td><td>保留</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="9">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">CH1COMCTL[2:0]</td><td>CH1COMSEN</td><td>CH1COMFEN</td><td rowspan="2" colspan="2">CH1MS[1:0]</td><td>保留</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH1CAPFLT[3:0]</td><td colspan="2">CH1CAPPSC[1:0]</td><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH1MS[2]</td><td>通道 1 I/O 模式选择参考 CH1MS[1:0]描述。</td></tr><tr><td>30</td><td>CH0MS[2]</td><td>通道 0 I/O 模式选择参考 CH0MS[1:0]描述。</td></tr><tr><td>29</td><td>CH1COMADDSEN</td><td>通道 1 附加输出比较影子寄存器使能参考 CH0COMADDSEN 描述。</td></tr><tr><td>28</td><td>CH0COMADDSEN</td><td>通道 0 附加输出比较影子寄存器使能当此位被置 1,TIMERx_CH0COMV_ADD 寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:通道 0 附加比较输出影子寄存器禁能1:通道 0 附加比较输出影子寄存器使能仅在单脉冲模式下(TIMERx_CTL0 寄存器的 SPM =1),可以在未确认预装载寄存器情况下使用 PWM 模式。当 TIMERx_CCHP0 寄存器的 PROT [1:0]=11 且 CH0MS =000 时此位不能被改</td></tr><tr><td>27</td><td>CH1ADDUPS</td><td>通道1附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH1COMV_ADD寄存器1:在发生计数器计数值匹配CH1VAL值时,更新TIMERx_CH1COMV_ADD寄存器</td></tr><tr><td>26</td><td>CH0ADDUPS</td><td>通道0附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH0COMV_ADD寄存器1:在发生计数器计数值匹配CH0VAL值时,更新TIMERx_CH0COMV_ADD寄存器</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>24</td><td>CH1COMCTL[3]</td><td>通道1输出比较控制参见CH0COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>CH0COMCTL[3]</td><td>通道0输出比较控制参见CH0COMCTL[2:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14:12</td><td>CH1COMCTL[2:0]</td><td>通道1输出比较模式参见CH0COMCTL描述</td></tr><tr><td>11</td><td>CH1COMSEN</td><td>通道1输出比较影子寄存器使能参见CH0COMSEN描述</td></tr><tr><td>10</td><td>CH1COMFEN</td><td>通道1输出比较快速使能参见CH0COMFEN描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择CH1MS[2:0]位域定义了通道的方向和输入信号的选择。只有当通道关闭(当MCH1MSEL[1:0]=2b'00时,TIMERx_CHCTL2寄存器的CH1EN位清0;当MCH1MSEL[1:0]=2b'01或2b'11时,TIMERx_CHCTL2寄存器的CH1EN、MCH1EN位清0)时,这些位才可以写。000:通道1配置为输出001:通道1配置为输入,IS1映射在CI1FE1上010:通道1配置为输入,IS1映射在CI0FE1上011:通道1配置为输入,IS1映射在ITS上,此模式仅工作在内部触发器输入被选中时(由SYSCFG_TIMERxCFG2(x=15,16)寄存器中的TSCFG15[4:0]位域选择)。100~111:保留</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式CH0COMCTL[3]和CH0COMCTL[2:0]位域定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O和MCH0_O的值。O0CPRE高电平有效,而CH0_O和MCH0_O的有效电平取决于CH0P和MCH0P位。注意:当多模式通道0配置为输出模式,且MCH0MSEL[1:0]=2b'11时,CH0COMCTL[3]和CH0COMCTL[2:0]位域定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O、MCH0_O的值。O0CPRE高电平有效,CH0_O、MCH0_O的有效电平取决于CH0P、MCH0P位。0000:时基。输出比较寄存器TIMERx_CH0CV与计数器TIMERx_CNT间的比较对O0CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE翻转。0100:强制为低。强制O0CPRE为低电平0101:强制为高。强制O0CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为有效电平,否则为无效电平。1000~1111:保留注意:在复合PWM模式下(CH0CPWMEN=1'b1和CH0MS=3'b000),通道0的PWM输出信号由TIMERx_CH0CV和TIMERx_CH0COMV_ADD寄存器共同确定。详细信息请参考复合PWM模式。在PWM模式0或PWM模式1中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,O0CPRE电平才改变。当CH0和MCH0输出互补时,该位域预装载。若CCSE=1,则该位域只在通道换相事件发生时更新。当TIMERx_CCHP0寄存器的PROT[1:0]=11且CH0MS=000(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>CH0COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0输出/比较影子寄存器1:使能通道0输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式</td></tr></table>

当 TIMERx_CCHP0 寄存器的 PROT [1:0]=11 且 CH0MS =000 时此位不能被改变。

## 1:0 CH0MS[1:0] 通道 0 I/O 模式选择

000：通道0 配置为输出

001：通道 0 配置为输入，IS0 映射在 CI0FE0 上

010：通道 0 配置为输入，IS0 映射在 CI1FE0 上

011：通道0 配置为输入，IS0映射在 ITS 上。此模式仅工作在内部触发输入被选中时（由 SYSCFG_TIMERxCFG2(x=15,16)寄存器中的 TSCFG15[4:0]位域选择）。

100：通道 0 配置为输入，IS0 映射在 MCI0FE0 上

101~111：保留

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:12</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述</td></tr><tr><td>11:10</td><td>CH1CAPPSC[1:0]</td><td>通道1输入捕获预分频器参见CH0CAPPSC描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择与输出模式相同</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了CI0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=20010:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=40011:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=80100:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=6</td></tr></table>

<table><tr><td>0101: fSAMP=fDTS/2, N=8</td></tr><tr><td>0110: fSAMP=fDTS/4, N=6</td></tr><tr><td>0111: fSAMP=fDTS/4, N=8</td></tr><tr><td>1000: fSAMP=fDTS/8, N=6</td></tr><tr><td>1001: fSAMP=fDTS/8, N=8</td></tr><tr><td>1010: fSAMP=fDTS/16, N=5</td></tr><tr><td>1011: fSAMP=fDTS/16, N=6</td></tr><tr><td>1100: fSAMP=fDTS/16, N=8</td></tr><tr><td>1101: fSAMP=fDTS/32, N=5</td></tr><tr><td>1110: fSAMP=fDTS/32, N=6</td></tr><tr><td>1111: fSAMP=fDTS/32, N=8</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000


该寄存器可以按半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留.</td><td>CH1PERFOREN</td><td>CH0PERFOREN</td><td colspan="12">保留.</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留.</td><td>MCH1P</td><td>保留</td><td>CH1P</td><td>CH1EN</td><td>MCH0P</td><td>MCH0EN</td><td>CH0P</td><td>CH0EN</td></tr><tr><td colspan="8"></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29</td><td>CH1PERFOREN</td><td>Channel 1在复合PWM模式下,周期点匹配时刻O1CPRE电平值设置。参考 CH0PERFOREN 描述。</td></tr><tr><td>28</td><td>CH0PERFOREN</td><td>Channel 0在复合PWM模式下,周期点匹配时刻O0CPRE电平值设置。</td></tr></table>

## 0：禁能

<table><tr><td></td><td></td><td>1: 复合PWM0模式下,周期点匹配时刻电平值强制拉高,复合PWM1模式下,周期点匹配时刻电平值强制拉低。注意:中央对齐模式下,周期点为计数器下溢时刻;边沿对齐模式下,周期点为计数器溢出时刻。</td></tr><tr><td>27:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>MCH1P</td><td>多模式通道1捕获/比较极性参考MCHOP描述。</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>CH1P</td><td>通道1捕获/比较极性参考CHOP描述。</td></tr><tr><td>4</td><td>CH1EN</td><td>通道1捕获/比较使能参考CH0EN描述。</td></tr><tr><td>3</td><td>MCHOP</td><td>多模式通道0捕获/比较极性当通道0配置为输出模式,且MCH0MSEL[1:0] = 2b&#x27;11时,此位定义了多模式通道0输出信号MCH0_O的极性。0: 多模式通道0高电平有效1: 多模式通道0低电平有效当通道0配置为输入模式时,此位和CHOP联合使用,作为通道0的极性选择控制信号。当TIMERx_CCHP0寄存器的PROT [1:0]=11或10时此位不能被更改。</td></tr><tr><td>2</td><td>MCH0EN</td><td>多模式通道0捕获/比较使能当多模式通道0配置为输出模式时,将此位置1使能MCH0_O信号有效。当多模式通道0配置为输入模式时,将此位置1使能多模式通道0上的捕获事件。0: 禁止多模式通道01: 使能多模式通道0</td></tr><tr><td>1</td><td>CHOP</td><td>通道0捕获/比较极性当通道0配置为输出模式时,此位定义了输出信号极性。0: 通道0高电平有效1: 通道0低电平有效当通道0配置为输入模式时,此位定义了通道0输入信号的极性。[MCHOP, CHOP]用于选择通道0输入信号信号有效边沿或者捕获极性。00: 把通道0输入信号的上升沿作为捕获或者从模式下触发的有效信号,且通道0输入信号不会被翻转。01: 把通道0输入信号的下降沿作为捕获或者从模式下触发的有效信号,且通道0输入信号会被翻转。10: 保留。</td></tr></table>

11：把通道 0 输入信号的上升沿和下降沿都作为捕获或者从模式下触发的有效信号，且通道 0 输入信号不翻转。

当 TIMERx_CCHP0 寄存器的 PROT [1:0]=11 或 10 时此位不能被更改。

当通道 0 配置为输出模式时，将此位置 1 使能 CH0_O 信号有效。当通道 0 配置为输入模式时，将此位置 1 使能通道 0 上的捕获事件。

## 计数器寄存器（TIMERx_CNT）

地址偏移：0x24

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>

## 预分频寄存器（TIMERx_PSC）

地址偏移：0x28

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值</td></tr><tr><td></td><td></td><td>计数器时钟等于 PSC 时钟除以(PSC+1),每次当更新事件产生时,PSC 的值被装入当前预分频寄存器。</td></tr></table>

## 计数器自动重载寄存器（TIMERx_CAR）

地址偏移：0x2C

复位值：0x0000 FFFF

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。</td></tr></table>

## 重复计数寄存器 0（TIMERx_CREP0）

地址偏移：0x30

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>7:0</td><td>CREP0[7:0]</td><td>重复计数器的值 0这些位定义了更新事件的产生速率。重复计数器计数值减为 0 时产生更新事件。影子寄存器的更新速率也会受这些位影响(前提是影子寄存器被使能)。注意:当 TIMERx_CFG 寄存器中的 CREPSEL =0 时,使用该位。</td></tr></table>

## 通道 0 捕获/比较寄存器（TIMERx_CH0CV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 1 捕获/比较寄存器（TIMERx_CH1CV）

地址偏移：0x38

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH1VAL[15:0]</td><td>通道1的捕获或比较值当通道1配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 互补通道保护寄存器 0（TIMERx_CCHP0）

地址偏移：0x44

复位值：0x0000 0000

该寄存器通过字访问（32 位）。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">BRKF[3:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>POEN</td><td>OAEN</td><td>BRKP</td><td>BRKEN</td><td>ROS</td><td>IOS</td><td colspan="2">PROT[1:0]</td><td colspan="8">DTCFG[7:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:16</td><td>BRKF[3:0]</td><td>BREAK输入信号滤波数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了BREAK输入信号的采样频率和数字滤波器的长度。0000:无滤波器,BREAK异步有效,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}, N=2</eq>0010:<eq>f_{SAMP} = f_{CK\_TIMER}, N=4</eq>0011:<eq>f_{SAMP} = f_{CK\_TIMER}, N=8</eq>0100:<eq>f_{SAMP} = f_{DTS}/2, N=6</eq>0101:<eq>f_{SAMP} = f_{DTS}/2, N=8</eq>0110:<eq>f_{SAMP} = f_{DTS}/4, N=6</eq>0111:<eq>f_{SAMP} = f_{DTS}/4, N=8</eq>1000:<eq>f_{SAMP} = f_{DTS}/8, N=6</eq>1001:<eq>f_{SAMP} = f_{DTS}/8, N=8</eq>1010:<eq>f_{SAMP} = f_{DTS}/16, N=5</eq>1011:<eq>f_{SAMP} = f_{DTS}/16, N=6</eq>1100:<eq>f_{SAMP} = f_{DTS}/16, N=8</eq>1101:<eq>f_{SAMP} = f_{DTS}/32, N=5</eq>1110:<eq>f_{SAMP} = f_{DTS}/32, N=6</eq>1111:<eq>f_{SAMP} = f_{DTS}/32, N=8</eq>此位只有在TIMERx_CCHP0寄存器的PROT [1:0]=00时才可修改。</td></tr><tr><td>15</td><td>POEN</td><td>所有的通道输出使能根据OAEN位,该位可以软件设置或者硬件自动设置。一旦中止输入有效,该位被硬件异步清0。如果一个通道配置为输出模式,如果设置了相应的使能位(TIMERx_CHCTL2寄存器的CHxEN,MCHxEN位),则开启CHx_O和MCHx_O输出。0:禁止通道输出或强制为空闲状态</td></tr></table>

## 1：使能通道输出

<table><tr><td>14</td><td>OAEN</td><td>自动输出使能此位定义了POEN位是否可以被硬件自动置1。0: POEN位不能被硬件置11: 如果中止输入无效,下一次更新事件发生时,POEN位能被硬件自动置1此位只有在TIMERxCCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>13</td><td>BRKP</td><td>BREAK输入信号极性此位定义了BREAK输入的极性。0: BREAK输入低电平有效1: BREAK输入高电平有效此位只有在TIMERxCCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>12</td><td>BRKEN</td><td>BREAK输入信号使能此位置1使能BREAK输入信号。0: BREAK输入禁能1: BREAK输入使能此位只有在TIMERxCCHP0寄存器的PROT[1:0]=00时才可修改。</td></tr><tr><td>11</td><td>ROS</td><td>运行模式下“关闭状态”使能当POEN位被置1(运行模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表13-13.由参数控制的互补输出表(MCHxMSEL=2'b11)。0: 输出“关闭状态”禁能。当CHxEN或者MCHxEN位被清零,对应通道为输出“禁能状态”。1: 输出“关闭状态”使能。当CHxEN或者MCHxEN位被清零,对应通道为输出“关闭状态”。此位在TIMERxCCHP0寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>10</td><td>IOS</td><td>空闲模式下“关闭状态”使能当POEN位被清0(空闲模式),此位可以被置1来使能通道(带有互补输出且配置为输出模式)的输出“关闭状态”。参见表13-13.由参数控制的互补输出表(MCHxMSEL=2'b11)。0: 输出“关闭状态”禁能。当CHxEN和MCHxEN位均被清零,对应通道为输出“禁能状态”。1: 输出“关闭状态”使能。不论CHxEN和MCHxEN位的值,对应通道为输出“关闭状态”。此位在TIMERxCCHP0寄存器的PROT[1:0]=10或11时不能被更改。</td></tr><tr><td>9:8</td><td>PROT[1:0]</td><td>互补寄存器保护控制这两位定义了寄存器的写保护特性。00: 禁能保护模式。无写保护。01: PROT模式0。TIMERxCTL1寄存器中ISOx/ISOxN位,TIMERxCCHP0寄存器中BRKEN/BRKP/OAEN/DTCFG位写保护10:PROT模式1。除了PROT模式0下的寄存器写保护外,还有TIMERx_CHCTL2寄存器中CHxP/MCHxP位(如果相应通道配置为输出模式),TIMERx_CCHP0寄存器中ROS/IOS位。11:PROT模式2。除了PROT模式1下的寄存器写保护外,还有TIMERx_CHCTLR0/1中CHxCOMCTL/CHxCOMSEN位(如果相关通道配置为输出模式)写保护。11:PROT模式2。除了PROT模式1下的寄存器写保护外,还有TIMERx_CHCTLR0及TIMERx_MCHCTL0寄存器中CHxCOMCTL/CHxCOMSEN/CHxCOMADDSEN/MCHxCOMCTL/MCHxCOMSEN位(如果相关通道配置为输出模式)写保护。系统复位后这两位只能被写一次,一旦TIMERx_CCHP0寄存器被写入,这两位被写保护</td></tr><tr><td>7:0</td><td>DTCFG[7:0]</td><td>死区时间控制这些位定义了插入互补输出之间的死区持续时间。DTCFG值和死区时间的关系如下:DTCFG [7:5] =3'b0xx: DTvalue =DTCFG [7:0]x tDT, tDT=tDTS.DTCFG [7:5] =3'b 10x: DTvalue = (64+DTCFG [5:0]) xtDT, tDT=tDTS*2.DTCFG [7:5] =3'b 110: DTvalue = (32+DTCFG [4:0]) xtDT, tDT=tDTS*8.DTCFG [7:5] =3'b 111: DTvalue = (32+DTCFG [4:0]) xtDT, tDT=tDTS*16.此位只有在TIMERx_CCHP0寄存器的PROT [1:0]=00时才可修改。</td></tr></table>

## 多模式通道控制寄存器 0（TIMERx_MCHCTL0）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">保留</td><td rowspan="2">MCH0MS[2]</td><td rowspan="2" colspan="13">保留</td><td>MCH0COMCTL[3]</td></tr><tr><td>保留</td></tr></table>

<table><tr><td>15 14 13 12 11 10 9 8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2">保留</td><td>保留</td><td colspan="3">MCH0COMCTL[2:0]</td><td>MCH0COMSEN</td><td>MCH0COMFEN</td><td rowspan="2" colspan="2">MCH0MS[1:0]</td></tr><tr><td colspan="4">MCH0CAPFLT[3:0]</td><td colspan="2">MCH0CAPPSC[1:0]</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>MCH0MS[2]</td><td>多模式通道0I/O模式选择参考MCH0MS[1:0]描述。</td></tr><tr><td>29:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>MCH0COMCTL[3]</td><td>多模式通道0输出比较控制请参考MCH0COMCTL[2:0]描述。</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>MCH0COMCTL[2:0]</td><td>多模式通道0输出比较控制当多模式通道0配置为输出模式,并且MCH0MSEL[1:0]=2b'00,MCH0COMCTL[3]和MCH0COMCTL[2:0]位域定义了输出准备信号MO0CPRE的动作,而MO0CPRE决定了MCH0_O的值。MO0CPRE高电平有效,而MCH0_O的有效电平取决于MCH0FP[1:0]位。注意:当多模式通道0配置为输出模式,且MCH0MSEL[1:0]=2b'11时,CH0COMCTL[2:0]位定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O、MCH0_O的值。O0CPRE高电平有效,CH0_O、MCH0_O的有效电平取决于CH0P、MCH0P位。0000:时基。输出比较寄存器TIMERx_MCH0CV与计数器TIMERx_CNT间的比较对MO0CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_MCH0CV相同时,强制MO0CPRE翻转。0100:强制为低。强制MO0CPRE为低电平0101:强制为高。强制MO0CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_MCH0CV时,MO0CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_MCH0CV时,MO0CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_MCH0CV时,MO0CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_MCH0CV时,MO0CPRE为有效电平,否则为无效电平。1000~1111:保留在PWM模式0或PWM模式1中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,MO0CPRE电平才改变。当CH0和MCH0输出互补时,该位域预装载。若CCSE=1,则该位域只在通道换相事件发生时更新。当TIMERx_CCHP0寄存器的PROT[1:0]=11且MCH0MS=000(比较模式)时此位不</td></tr></table>

能被改变。

<table><tr><td>3</td><td>MCH0COMSEN</td><td>多模式通道0输出比较影子寄存器使能当此位被置1,TIMERx_MCH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止多模式通道0输出/比较影子寄存器1:使能多模式通道0输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。当TIMERx_CCHP0寄存器的PROT[1:0]=11且CH0MS=00时此位不能被改变。</td></tr><tr><td>2</td><td>MCH0COMFEN</td><td>多模式通道0输出比较快速使能0:多模式通道0输出比较快速禁能。仅比较结果输入作为有效边沿时会产生比较匹配,并将MCHO_O设置为比较电平,激活MCHO_O输出的最小延时为5个时钟周期。1:多模式通道0输出比较快速使能。触发输入信号的有效边沿和比较结果都会产生比较匹配,并将MCHO_O设置为比较电平。当触发信号的输入作为有效边沿时,激活MCHO_O输出的最小延时为3个时钟周期。</td></tr><tr><td>1:0</td><td>MCH0MS[1:0]</td><td>多模式通道0I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当MCH0MSEL[1:0]=2b&#x27;00时,TIMERx_CHCTL2寄存器的MCHOEN位清0)时,MCH0MS[2:0]才可写。000:多模式通道0配置为输出001:多模式通道0配置为输入,MISO映射在MCIOFEM0上010:保留011:多模式通道0配置为输入,MISO映射在ITS上。此模式仅工作在内部触发输入被选中时(由SYSCFG_TIMERxCFG2(x=14,40,41,42,43,44)寄存器中的TSCFG15[4:0]位域选择)。100:多模式通道0配置为输入,MISO映射在CI0FEM0上。101~111:保留</td></tr></table>

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>MCH0MS[2]</td><td>多模式通道 0 I/O 模式选择参考MCH0MS[1:0]描述。</td></tr><tr><td>29:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:4</td><td>MCH0CAPFLT[3:0]</td><td>通道 0 输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录 N 个输入事件后会产生一个输出的跳变。这些位定义了 MCI0 输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=1</td></tr></table>

## 多模式通道控制寄存器 2（TIMERx_MCHCTL2）

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td colspan="2">MCH0FP[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1:0</td><td>MCH0FP[1:0]</td><td>多模式通道0捕获/比较独立极性控制当多模式通道0配置为输出模式时,且MCH0MSEL[1:0]=2b'00,此位定义了输出信号极性。00:多模式通道0高电平有效01:多模式通道0低电平有效10:保留11:保留当通道0配置为输入模式时,此位定义了多模式通道0输入信号的极性。MCH0FP[1:0]将选择多模式通道0输入信号的有效边沿或者捕获极性。00:把多模式通道0输入信号的上升沿作为捕获或者从模式下触发的有效信号,且多模式通道0输入信号不会被翻转。01:把多模式通道0输入信号的下降沿作为捕获或者从模式下触发的有效信号,且多模式通道0输入信号会被翻转。10:保留。11:把多模式通道0输入信号的上升沿或下降沿作为捕获或者从模式下触发的有效信号,并且多模式通道0输入信号不会被翻转。当TIMERx_CCHP0寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr></table>

## 多模式通道 0 捕获/比较寄存器（TIMERx_MCH0CV）

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MCH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>MCH0VAL[15:0]</td><td>多模式通道0的捕获或比较值当多模式通道0配置为输入模式时,这些位决定了上次捕获事件的计数器值,且本寄存器为只读。当多模式通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 通道 0 附加比较寄存器（TIMERx_CH0COMV_ADD）

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH0COMVAL_ADD[15:0]</td><td>通道0附加比较值当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>

## 通道 1 附加比较寄存器（TIMERx_CH1COMV_ADD）

地址偏移：0x68

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CH1COMVAL_ADD[15:0]</td><td>通道1附加比较值当通道1附加配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>

## 控制寄存器 2（TIMERx_CTL2）

地址偏移：0x74

复位值：0x0030 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>CH1C PWMEN</td><td>CH0C PWMEN</td><td colspan="6">保留</td><td colspan="2">MCH0MSEL[1:0]</td><td colspan="4">保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="6"></td><td colspan="2">rw</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="2">CH1OMPSEL[1:0]</td><td colspan="2">CH0OMPSEL[1:0]</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29</td><td>CH1CPWMEN</td><td>通道1复合PWM模式使能0:通道1复合PWM模式禁能1:通道1复合PWM模式使能</td></tr><tr><td>28</td><td>CH0CPWMEN</td><td>通道0复合PWM模式使能0:通道0复合PWM模式禁能1:通道0复合PWM模式使能</td></tr><tr><td>27:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21:20</td><td>MCH0MSEL[1:0]</td><td>多模式通道0模式选择00:独立模式,MCH0独立于CH001:保留10:保留11:互补模式,只有CH0可用于输入,MCH0输出与CH0输出互补</td></tr><tr><td>19:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:10</td><td>CH1OMPSEL[1:0]</td><td>通道1输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O1CPRE(用来驱动CH1_O信号)。00:O1CPRE信号根据CH1COMCTL[2:0]位的配置正常输出。01:只有在计数器向上计数,匹配事件发生时,O1CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O1CPRE信号输出一个脉冲,脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或者向下计数,匹配事件发生时,O1CPRE信号输出一个脉冲,脉冲宽度是一个CK_TIMER时钟周期。</td></tr><tr><td>9:8</td><td>CH0OMPSEL[1:0]</td><td>通道0输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O0CPRE(用来驱动CH0_O信号)。00:O0CPRE信号根据CH0COMCTL[2:0]位的配置正常输出。01:只有在计数器向上计数,匹配事件发生时,O0CPRE信号输出一个脉冲,并且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O0CPRE信号输出一个脉冲,脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或者向下计数,匹配事件发生时,O0CPRE信号输出一个脉冲,脉冲宽度是一个CK_TIMER时钟周期。</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## TIMERx 备用功能控制寄存器 0（TIMERx_AFCTL0）

地址偏移：0x8C

复位值：0x0000 0001

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>BRKCMP0P</td><td colspan="8">保留</td><td>BRKIN0P</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>BRKCMP0EN</td><td colspan="8">保留</td><td>BRKIN0EN</td></tr><tr><td colspan="7">rw</td><td colspan="8">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>BRKCMP0P</td><td>BREAK CMP0输入极性0: CMP0输入信号不反相(BRKP =0,输入信号低有效;BRKP =1,输入信号高有效)1: CMP输入信号反相(BRKP =0,输入信号高有效;BRKP =1,输入信号低有效)此位只有在TIMERx_CCHP0寄存器的PROT [1:0] =00时才可修改。</td></tr><tr><td>24:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BRKIN0P</td><td>BREAK BRKIN0备用输入极性该位用于配置BRKIN0输入极性,具体极性是由该位和BRKP位共同确定。0: BRKIN0输入信号不反相(BRKP =0,输入信号低有效;BRKP =1,输入信号高有效)1: BRKIN0输入信号反相(BRKP =0,输入信号高有效;BRKP =1,输入信号低有效)</td></tr></table>

<table><tr><td></td><td></td><td>此位只有在TIMERx_CCHP0寄存器的PROT [1:0] =00时才可修改。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>BRKCMP0EN</td><td>BREAK CMP0输入使能0: CMP0输入禁能1: CMP0输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] =00时才可修改。</td></tr><tr><td>8:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BRKIN0EN</td><td>BREAK BRKIN0备用输入使能0: BRKIN0输入禁能1: BRKIN0输入使能此位只有在TIMERx_CCHP0寄存器的PROT [1:0] =00时才可修改。</td></tr></table>

## 计数器初值控制寄存器(TIMERx_CINITCTL)

地址偏移：0xA4

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>SWSYNCG</td><td>CINITDIR</td><td>CINITVEN</td></tr><tr><td colspan="13"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SWSYNCG</td><td>软件同步事件产生该位由软件置位,硬件自动清零,对该位进行读操作,读取值均为0。0:无效1:产生软件更新事件</td></tr><tr><td>1</td><td>CINITDIR</td><td>计数器初始计数方向0:同步事件发生时,计数器向下计数1:同步事件发生时,计数器向上计数当同步事件发生,且计数器从TIMERx_CINITV寄存器加载计数器初始值后,该位表明了此时计数器的计数初始方向。注意:该位仅用于CAM[1:0]≠00的情况。</td></tr></table>

0 CINITVEN 计数器初值寄存器使能

0：计数器初值寄存器禁能。计数器寄存器不从计数器初值寄存器加载初值。

1：计数器初值寄存器使能。当同步事件发生（通过软件将SWSYNCG位置1产生软件同步事件，输入引脚输入硬件同步事件）时，计数器寄存器可以从计数器初值寄存器加载初值。

计数器初值寄存器(TIMERx_CINITV)

地址偏移：0xA8

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CINITVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CINITVAL[15:0]</td><td>计数器初始值该位域用于表示计数器的初始值。CINITVEN位为0时,计数器的寄存器不能加载在CINITVAL[15:0]位域中设置的初始值。CINITVEN位为1时,当同步事件发生时,计数器的寄存器可以加载在CINITVAL[15:0]位域中设置的初始值。</td></tr></table>

## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">DMATC[5:0]</td><td colspan="2">保留</td><td colspan="6">DMATA [5:0]</td></tr></table>

<table><tr><td>31:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13:8</td><td>DMATC [5:0]</td><td>DMA传输计数该位域定义了DMA访问(读/写)TIMERx_DMATB寄存器的次数。6&#x27;b000000:传输1次6&#x27;b000001:传输2次...6&#x27;b111111:传输63次</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:0</td><td>DMATA [5:0]</td><td>DMA传输起始地址该位域定义了DMA访问TIMERx_DMAVB寄存器的第一个地址。当通过TIMERx_DMA第一次访问时,访问的就是该位域指定的地址。第二次访问TIMERx_DMATB时,将访问起始地址+0x4。6&#x27;b0_0000:TIMERx_CTL06&#x27;b0_0001:TIMERx_CTL1...总之:起始地址 = TIMERx_CTL0 + DMATA*4</td></tr></table>

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DMATB[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DMATB [31:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>CCUSEL</td><td>保留</td><td>CHVSEL</td><td>OUTSEL</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>CCUSEL</td><td>换相控制影子寄存器更新选择只有当CCUC[2:0]位域配置为100,101和110时,该位才有效。0:当计数器产生一个上溢/下溢事件时,影子寄存器才更新1:当重复计数器值为0,且计数器产生一个上溢/下溢事件时,影子寄存器才更新</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>OUTSEL</td><td>输出值选择位此位由软件写1或清0。1:如果POEN位与IOS位均为0,则输出无效0:无影响</td></tr></table>

