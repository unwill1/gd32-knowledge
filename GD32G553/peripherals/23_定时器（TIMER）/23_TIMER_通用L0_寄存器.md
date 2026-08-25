## 23.2.5. TIMERx 寄存器（x = 1 / 2 / 3 / 4）

TIMER1基地址：0x4000 0000

TIMER2基地址：0x4000 0400

TIMER3基地址：0x4000 0800

TIMER4基地址：0x4000 0C00

## 控制寄存器 0（TIMERx_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ADMEN</td><td>UPIFBUEN</td><td>保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="2">CAM[1:0]</td><td>DIR</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ADMEN</td><td>微调模式使能0:微调模式禁能1:微调模式使能注意:该位只能在CEN位为0时修改。</td></tr><tr><td>11</td><td>UPIFBUEN</td><td>UPIF位备份使能0:备份禁能。UPIF位没有备份到TIMERx_CNT寄存器中的UPIFBU位1:备份使能。UPIF位备份到TIMERx_CNT寄存器中的UPIFBU位</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(CK_TIMER)与死区时间和采样时钟(DTS)之间的分频系数,死区发生器和数字滤波器会用到DTS时间。00:<eq>f_{DTS} = f_{CK\_TIMER}</eq>01:<eq>f_{DTS} = f_{CK\_TIMER} / 2</eq>10:<eq>f_{DTS} = f_{CK\_TIMER} / 4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:5</td><td>CAM[1:0]</td><td>计数器对齐模式选择00:无中央对齐模式(边沿对齐模式)。DIR 位指定了计数方向。01:中央对齐向下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),只有在向下计数时,通道的比较中断标志置 110:中央对齐向上计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),只有在向上计数时,通道的比较中断标志置 111:中央对齐上下计数置 1 模式。计数器在中央计数模式计数,通道被配置在输出模式(TIMERx_CHCTL0 寄存器中 CHxMS=00),在向上和向下计数时,通道的比较中断标志都会置 1当计数器使能以后,该位不能从 0x00 切换到非 0x00 状态。</td></tr><tr><td>4</td><td>DIR</td><td>方向0:向上计数1:向下计数当计数器配置为中央对齐模式或译码器模式时,该位为只读。</td></tr><tr><td>3</td><td>SPM</td><td>单脉冲模式0:更新事件发生后,计数器继续计数1:在下一次更新事件发生时,CEN 硬件清零并且计数器停止计数</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该位,选择更新事件源.0:使能后,下述任一事件产生更新中断或 DMA 请求:-UPG 位被置 1-计数器上溢/下溢-从模式控制器产生的更新1:使能后只有计数器上溢/下溢才产生更新中断或 DMA 请求。</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新.该位用来使能或禁能更新事件的产生。0:更新事件使能。当以下事件之一发生时,更新事件产生,具有缓存的寄存器被装入它们的预装载值:-UPG 位被置 1-计数器上溢/下溢-从模式控制器产生一个更新事件</td></tr><tr><td>0</td><td>CEN</td><td>计数器使能0: 计数器禁能1: 计数器使能在软件将 CEN 位置 1 后,外部时钟、暂停模式和译码器模式才能工作。触发模式可以自动地通过硬件设置 CEN 位。</td></tr></table>

## 控制寄存器 1（TIMERx_CTL1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>MMC0[3]</td><td colspan="9">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TIOS</td><td colspan="3">MMC0[2:0]</td><td>DMAS</td><td colspan="3">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>MMC0[3]</td><td>主模式控制 0请参考 MMC0[2:0]的描述。</td></tr><tr><td>24:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TIOS</td><td>通道 0 触发输入选择0:选择 TIMERx_CH0 引脚作为通道 0 的触发输入1:选择 TIMERx_CH0, CH1 和 CH2 引脚异或的结果作为通道 0 的触发输入</td></tr><tr><td>6:4</td><td>MMC0[2:0]</td><td>主模式控制 0这些位控制 TRGO0 信号的选择,TRGO0 信号由主定时器发给从定时器用于同步功能。0000:复位。TIMERx_SWEVG 寄存器的 UPG 位被置 1 或从模式控制器产生复位触发一次 TRGO0 脉冲,后一种情况下,TRGO0 上的信号相对实际的复位会有一个延迟。0001:使能。此模式可用于同时启动多个定时器或控制在一段时间内使能从定时器。主模式控制器选择计数器使能信号作为触发输出 TRGO0。当 CEN 控制位被置 1 或者暂停模式下触发输入为高电平时,计数器使能信号被置 1。在暂停模式下,计数器使能信号受控于触发输入,在触发输入和TRGO0上会有一个延迟,除非选择了主/从模式。0010:更新。主模式控制器选择更新事件作为TRGO0。0011:捕获/比较脉冲。通道0在发生一次捕获或一次比较成功时,主模式控制器产生一个TRGO0脉冲0100:比较。在这种模式下主模式控制器选择O0CPRE信号被用于作为触发输出TRGO00101:比较。在这种模式下主模式控制器选择O1CPRE信号被用于作为触发输出TRGO00110:比较。在这种模式下主模式控制器选择O2CPRE信号被用于作为触发输出TRGO00111:比较。在这种模式下主模式控制器选择O3CPRE信号被用于作为触发输出TRGO01000:译码器时钟输出。在这种模式下主模式控制器选择译码器时钟信号作为触发输出TRGO0。此值仅用于正交译码器模式0~4和译码器模式0~3。1001~1111:保留</td></tr><tr><td>3</td><td>DMAS</td><td>DMA请求源选择0:当通道捕获/比较事件发生时,发送通道CHx的DMA请求1:当更新事件发生,发送通道CHx的DMA请求</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 从模式配置寄存器（TIMERx_SMCFG）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>PRMRPSEL</td><td>DECMODS</td><td>DECMODEN</td><td colspan="8">保留</td></tr><tr><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="8"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ETP</td><td>SMC1</td><td colspan="2">ETPSC[1:0]</td><td colspan="4">ETFC[3:0]</td><td>MSM</td><td colspan="3">保留</td><td>OCRC</td><td colspan="3">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:27</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>26</td><td colspan="3">PRMRPSEL</td><td colspan="12">暂停+复位模式复位极性选择0:计数器在下降沿复位1: 计数器在上升沿复位</td></tr><tr><td>25</td><td colspan="3">DECMODS</td><td colspan="12">译码器模式更新源该位用于选择译码器模式的更新源。0: 模式修改后,通过 TIMER 的更新事件更新译码器模式1: 模式修改后,通过索引事件更新译码器模式</td></tr><tr><td>24</td><td colspan="3">DECMODEN</td><td colspan="12">译码器模式在线修改使能0: 译码器模式在线修改禁能1: 译码器模式在线修改使能该位置 1 时,译码器模式可以从一种模式修改为另一种模式。</td></tr><tr><td>23:16</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>15</td><td colspan="3">ETP</td><td colspan="12">外部触发极性该位指定 ETI 信号的极性0: ETI 高电平或上升沿有效1: ETI 低电平或下降沿有效</td></tr><tr><td>14</td><td colspan="3">SMC1</td><td colspan="12">从模式的一部分为了使能外部时钟模式 1 在外部时钟模式 1,计数器由 ETIFP 信号上的任意有效边沿驱动。0: 外部时钟模式 1 禁能1: 外部时钟模式 1 使能复位模式,暂停模式和事件模式可以与外部时钟模式 1 同时使用。但是 TSCFGy[4:0](y = 3,4,5)位域的值不能为 5'b01000。如果外部时钟模式 0 和外部时钟模式 1 同时被使能,外部时钟的输入是 ETIFP。注意:外部时钟模式 0 使能在 SYSCFG_TIMERxCFG1 寄存器中的 TSCFG6[4:0]位域。</td></tr><tr><td>13:12</td><td colspan="3">ETPSC[1:0]</td><td colspan="12">外部触发预分频外部触发信号 ETI 的频率不能超过 TIMER_CK 频率的 1/4。当输入较快的外部时钟时,可以使用预分频降低 ETIFP 的频率。00: 预分频禁能01: ETI 频率被 2 分频10: ETI 频率被 4 分频11: ETI 频率被 8 分频</td></tr><tr><td>11:8</td><td colspan="3">ETFC[3:0]</td><td colspan="12">外部触发滤波控制数字滤波器是一个事件计数器,它记录到 N 个事件后会产生一个输出的跳变。这些位定义了对 ETI 信号采样的频率和对 ETI 数字滤波的带宽。0000: 滤波器禁能 fsAMP=fdTS, N=10001: fsAMP=fCK_TIMER, N=20010: fsAMP=fCK_TIMER, N=40011: fsAMP=fCK_TIMER, N=8</td></tr></table>

0100：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=6 

0101：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=8 

0110：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=6 

0111：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=8 

1000：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=6 

1001：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=8 

1010：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=5 

<table><tr><td>7</td><td>MSM</td><td>主-从模式该位被用来同步被选择的定时器同时开始计数。通过TRIGI和TRGO0,定时器被连接在一起,TRGO0用做启动事件。0:主从模式禁能1:主从模式使能</td></tr><tr><td>6:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>OCRC</td><td>OxCPRE清除源选择该位用于选择OxCPRE清除源。0:OCPRE_CLR_INT连接OCPRE_CLR输入1:OCPRE_CLR_INT连接到ETIF</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## DMA 和中断使能寄存器（TIMERx_DMAINTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDIE</td><td>CH2COMADDIE</td><td>CH1COMADDIE</td><td>CH0COMADDIE</td><td colspan="8">保留</td><td>INDERRIE</td><td>DIRTRANIE</td><td>DECDISIE</td><td>DECJIE</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>INDIE</td><td>TRGDEN</td><td>保留</td><td>CH3DEN</td><td>CH2DEN</td><td>CH1DEN</td><td>CH0DEN</td><td>UPDEN</td><td>保留</td><td>TRGIE</td><td>保留</td><td>CH3IE</td><td>CH2IE</td><td>CH1IE</td><td>CH0IE</td><td>UPIE</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>31</td><td>CH3COMADDIE</td><td>通道3附加比较中断使能0:禁止通道3附加比较中断1:使能通道3附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>30</td><td>CH2COMADDIE</td><td>通道2附加比较中断使能0:禁止通道2附加比较中断1:使能通道2附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>29</td><td>CH1COMADDIE</td><td>通道1附加比较中断使能0:禁止通道1附加比较中断1:使能通道1附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>28</td><td>CH0COMADDIE</td><td>通道0附加比较中断使能0:禁止通道0附加比较中断1:使能通道0附加比较中断注意:此中断使能位仅用于复合PWM模式。</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>INDERRIE</td><td>索引错误中断使能0:索引错误中断禁能1:索引错误中断使能</td></tr><tr><td>18</td><td>DIRTRANIE</td><td>计数方向变化中断使能0:计数方向变化中断禁能1:计数方向变化中断禁能</td></tr><tr><td>17</td><td>DECDISIE</td><td>正交译码器信号断线检测使能0:禁能1:使能注意:该位仅用于正交译码器信号断线检测使能(DECDISDEN=1)时。</td></tr><tr><td>16</td><td>DECJIE</td><td>正交译码器信号跳变(两个信号同时发生跳变)中断使能0:禁能1:使能注意:该位仅用于正交译码器信号同时跳变检测使能(DECJDEN=1)时。</td></tr><tr><td>15</td><td>INDIE</td><td>索引中断使能0:索引中断禁能1:索引中断使能</td></tr><tr><td>14</td><td>TRGDEN</td><td>触发DMA请求使能</td></tr></table>

<table><tr><td></td><td></td><td>0:禁止触发DMA请求1:使能触发DMA请求</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CH3DEN</td><td>通道3比较/捕获DMA请求使能0:禁止通道3比较/捕获DMA请求1:使能通道3比较/捕获DMA请求</td></tr><tr><td>11</td><td>CH2DEN</td><td>通道2比较/捕获DMA请求使能0:禁止通道2比较/捕获DMA请求1:使能通道2比较/捕获DMA请求</td></tr><tr><td>10</td><td>CH1DEN</td><td>通道1比较/捕获DMA请求使能0:禁止通道1比较/捕获DMA请求1:使能通道1比较/捕获DMA请求</td></tr><tr><td>9</td><td>CH0DEN</td><td>通道0比较/捕获DMA请求使能0:禁止通道0比较/捕获DMA请求1:使能通道0比较/捕获DMA请求</td></tr><tr><td>8</td><td>UPDEN</td><td>更新DMA请求使能0:禁止更新DMA请求1:使能更新DMA请求</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TRGIE</td><td>触发中断使能0:禁止触发中断1:使能触发中断</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>CH3IE</td><td>通道3比较/捕获中断使能0:禁止通道3中断1:使能通道3中断</td></tr><tr><td>3</td><td>CH2IE</td><td>通道2比较/捕获中断使能0:禁止通道2中断1:使能通道2中断</td></tr><tr><td>2</td><td>CH1IE</td><td>通道1比较/捕获中断使能0:禁止通道1中断1:使能通道1中断</td></tr><tr><td>1</td><td>CH0IE</td><td>通道0比较/捕获中断使能0:禁止通道0中断</td></tr></table>

1：使能通道 0 中断

更新中断使能

0：禁止更新中断

1：使能更新中断

## 中断标志寄存器（TIMERx_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDIF</td><td>CH2COMADDIF</td><td>CH1COMADDIF</td><td>CH0COMADDIF</td><td colspan="8">保留</td><td>INDERRIF</td><td>DIRTRANIF</td><td>DECDISIF</td><td>DECJIF</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>INDIF</td><td colspan="2">保留</td><td>CH3OF</td><td>CH2OF</td><td>CH1OF</td><td>CH0OF</td><td colspan="2">保留</td><td>TRGIF</td><td>保留</td><td>CH3IF</td><td>CH2IF</td><td>CH1IF</td><td>CH0IF</td><td>UPIF</td></tr><tr><td>rc_w0</td><td></td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td>rc_w0</td><td></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3COMADDIF</td><td>通道3附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>30</td><td>CH2COMADDIF</td><td>通道2附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>29</td><td>CH1COMADDIF</td><td>通道1附加比较中断标志参见CH0COMADDIF描述。</td></tr><tr><td>28</td><td>CH0COMADDIF</td><td>通道0附加比较中断标志此标志由硬件置1软件清0。当通道0用于输出模式时,此标志位在一个比较事件发生时被置1。0:无通道0中断发生1:通道0中断发生注意:此标志仅用于复合PWM模式。</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>INDERRIF</td><td>索引错误中断标志位此标志由硬件置1软件清0。0:无索引错误中断发生1:索引错误中断发生</td></tr><tr><td>18</td><td>DIRTRANIF</td><td>计数方向变化中断标志位译码器模式下,此标志在 TIMERx_CTL0 寄存器中的 DIR 位发生变化时由硬件置 1,并由软件清 0。0:无计数方向变化中断发生1:计数方向变化中断发生</td></tr><tr><td>17</td><td>DECDISIF</td><td>正交译码器信号断线中断标志位0:无正交译码器信号断线中断发生1:正交译码器信号断线中断发生注意:该位仅用于正交译码器信号断线检测使能(DECDISDEN =1)时。</td></tr><tr><td>16</td><td>DECJIF</td><td>正交译码器信号跳变(两个信号同时发生跳变)中断标志位0:无正交译码器信号跳变中断发生1:正交译码器信号跳变中断发生注意:该位仅用于正交译码器信号同时跳变检测使能(DECJDEN =1)时。</td></tr><tr><td>15</td><td>INDIF</td><td>索引中断标志位此标志由硬件置 1 软件清 0。0:无索引中断发生1:索引中断发生</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CH3OF</td><td>通道 3 捕获溢出标志参见 CH0OF 描述。</td></tr><tr><td>11</td><td>CH2OF</td><td>通道 2 捕获溢出标志参见 CH0OF 描述。</td></tr><tr><td>10</td><td>CH1OF</td><td>通道 1 捕获溢出标志参见 CH0OF 描述。</td></tr><tr><td>9</td><td>CH0OF</td><td>通道 1 捕获溢出标志当通道 0 被配置为输入模式时,在 CH0IF 标志位已经被置 1 后,捕获事件再次发生时,该标志位可以由硬件置 1。该标志位由软件清 0。0:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TRGIF</td><td>触发中断标志当发生触发事件时,此标志由硬件置 1。此位由软件清 0。当从模式控制器处于除暂停模式外的其它模式时,在 TRGI 输入端检测到有效边沿,产生触发事件。当从模式控制器处于暂停模式时,TRGI 的任意边沿都可以产生触发事件。0:无触发事件产生</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>CH3IF</td><td>通道3比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>3</td><td>CH2IF</td><td>通道2比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>2</td><td>CH1IF</td><td>通道1比较/捕获中断标志参见CH0IF描述。</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。当通道0在输入模式下时,通过读TIMERx_CH0CV寄存器可以清零该位。0:无通道0中断发生1:通道0中断发生</td></tr><tr><td>0</td><td>UPIF</td><td>更新中断标志此位在任何更新事件发生时由硬件置1,软件清0。0:无更新中断发生1:发生更新中断</td></tr></table>

## 软件事件产生寄存器（TIMERx_SWEVG）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3COMADDG</td><td>CH2COMADDG</td><td>CH1COMADDG</td><td>CH0COMADDG</td><td colspan="12">保留</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>TRGG</td><td>保留</td><td>CH3G</td><td>CH2G</td><td>CH1G</td><td>CH0G</td><td>UPG</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3COMADDG</td><td>通道3附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>30</td><td>CH2COMADDG</td><td>通道2附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>29</td><td>CH1COMADDG</td><td>通道1附加比较事件发生参见CH0COMADDG描述。</td></tr><tr><td>28</td><td>CH0COMADDG</td><td>通道0附加比较事件发生该位由软件置1,用于在通道0产生一个比较事件,由硬件自动清0。当此位被置1,CH0COMADDIF标志位被置1,若开启对应的中断和DMA,则发出相应的中断请求。0:不产生通道0附加比较事件1:发生通道0附加比较事件注意:此位仅用于复合PWM模式。</td></tr><tr><td>27:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TRGG</td><td>触发事件产生此位由软件置1,由硬件自动清0.当此位被置1,TIMERx_INTF寄存器的TRGIF标志位被置1,若开启对应的中断和DMA,则产生相应的中断和DMA传输。0:无触发事件产生1:产生触发事件</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>CH3G</td><td>通道3捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>3</td><td>CH2G</td><td>通道2捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>2</td><td>CH1G</td><td>通道1捕获或比较事件发生参见CH0G描述。</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1,如果选择了中央对齐或向上计数模式,计数器被清0。否则(向下计数模式)计数器将载入自动重载值,预分频计数器将同时被清除。</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">CH1MS[2]</td><td rowspan="2">CH0MS[2]</td><td>CH1COMADDSEN</td><td>CH0COMADDSEN</td><td>CH1ADDUPS</td><td>CH0ADDUPS</td><td rowspan="2">保留</td><td>CH1COMCTL[3]</td><td rowspan="2" colspan="7">保留</td><td>CH0COMCTL[3]</td></tr><tr><td>保留</td><td>保留</td><td>保留</td><td>保留</td><td>保留</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="9">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH1COMCEN</td><td colspan="3">CH1COMCTL[2:0]</td><td>CH1COMSEN</td><td>CH1COMFEN</td><td rowspan="2" colspan="2">CH1MS[1:0]</td><td>CH0COMCEN</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH1CAPFLT[3:0]</td><td colspan="2">CH1CAPPSC[1:0]</td><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

0：无更新事件产生

1：产生更新事件

## 通道控制寄存器 0（TIMERx_CHCTL0）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH1MS[2]</td><td>通道 1 I/O 模式选择参考 CH1MS[1:0]描述。</td></tr><tr><td>30</td><td>CH0MS[2]</td><td>通道 0 I/O 模式选择参考 CH0MS[1:0]描述。</td></tr><tr><td>29</td><td>CH1COMADDSEN</td><td>通道 1 附加输出比较影子寄存器使能参考 CH0COMADDSEN 描述。</td></tr><tr><td>28</td><td>CH0COMADDSEN</td><td>通道 0 附加输出比较影子寄存器使能当此位被置 1,TIMERx_CH0COMV_ADD 寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道 0 附加比较输出影子寄存器1:使能通道 0 附加比较输出影子寄存器仅在单脉冲模式下(TIMERx_CTL0 寄存器的 SPM=1),可以在未确认预装载寄存器情况下使用 PWM 模式。</td></tr><tr><td>27</td><td>CH1ADDUPS</td><td>通道1附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH1COMV_ADD寄存器1:在发生计数器计数值匹配 CH1VAL 值时,更新 TIMERx_CH1COMV_ADD 寄存器</td></tr><tr><td>26</td><td>CH0ADDUPS</td><td>通道0附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH0COMV_ADD寄存器1:在发生计数器计数值匹配CH0VAL值时,更新TIMERx_CH0COMV_ADD寄存器</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>CH1COMCTL[3]</td><td>通道1输出比较控制参见CH0COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CH0COMCTL[3]</td><td>通道0输出比较控制参见CH0COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH1COMCEN</td><td>通道1输出比较清0使能参见CH0COMCEN描述。</td></tr><tr><td>14:12</td><td>CH1COMCTL[2:0]</td><td>通道1输出比较模式参见CH0COMCTL描述。</td></tr><tr><td>11</td><td>CH1COMSEN</td><td>通道1输出比较影子寄存器使能参见CH0COMSEN描述。</td></tr><tr><td>10</td><td>CH1COMFEN</td><td>通道1输出比较快速使能参见CH0COMFEN描述</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择CH1MS[2:0]位域定义了通道的方向和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH1EN位被清0)时这些位才可以写。000:通道1配置为输出001:通道1配置为输入,IS1映射在CI1FE1上010:通道1配置为输入,IS1映射在CI0FE1上011:通道1配置为输入,IS1映射在ITS上,此模式仅工作在内部触发器输入被选中时(由SYSCFG_TIMERxCFG2(x=1..4)寄存器中的TSCFG15[4:0]位域选择)。100~111:保留</td></tr><tr><td>7</td><td>CH0COMCEN</td><td>通道0输出比较清0使能当此位被置1,当检测到ETIFP输入高电平时,O0CPRE参考信号被清0。0:禁止通道0输出比较清零1:使能通道0输出比较清零</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式CH0COMCTL[3]和CH0COMCTL[2:0]位域定义了输出准备信号O0CPRE的动作,而O0CPRE决定了CH0_O的值。O0CPRE高电平有效,而CH0_O的有效电平取决于CH0P位。</td></tr></table>

0000：时基。输出比较寄存器 TIMERx_CH0CV 与计数器 TIMERx_CNT 间的比较对O0CPRE 不起作用

0001：匹配时设置为高。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时，强制 O0CPRE 为高。

0010：匹配时设置为低。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时，强制 O0CPRE 为低。

0011：匹配时翻转。当计数器的值与捕获/比较值寄存器 TIMERx_CH0CV 相同时，强制 O0CPRE 翻转。

0100：强制为低。强制 O0CPRE 为低电平

0101：强制为高。强制 O0CPRE 为高电平

0110：PWM模式0。在向上计数时，一旦计数器值小于TIMERx_CH0CV时，O0CPRE为有效电平，否则为无效电平。在向下计数时，一旦计数器的值大于 TIMERx_CH0CV时，O0CPRE 为无效电平，否则为有效电平。

0111：PWM模式1。在向上计数时，一旦计数器值小于TIMERx_CH0CV时，O0CPRE为无效电平，否则为有效电平。在向下计数时，一旦计数器的值大于 TIMERx_CH0CV时，O0CPRE 为有效电平，否则为无效电平。

1000：可延时的单脉冲模式0。O0CPRE的输出情况类似与PWM模式0。在向上计数模式时，O0CPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平；在向下计数模式时，O0CPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平。

1001：可延时的单脉冲模式1。O0CPRE的输出情况类似与PWM模式1。在向上计数模式时，O0CPRE先输出无效电平，当外部触发事件发生时，立即输出有效电平，当下一次更新事件发生时，再变成无效电平；在向下计数模式时，O0CPRE先输出有效电平，当外部触发事件发生时，立即输出无效电平，当下一次更新事件发生时，再变成有效电平。

1010 / 1011 / 1100 / 1101 / 1110 / 1111：保留

注意：在复合 PWM 模式下（CH0CPWMEN = 1’b1 和 CH0MS = 3’b000），通道 0的 PWM 输出信号由 TIMERx_CH0CV 和 TIMERx_CH0COMV_ADD 寄存器共同确定。详细信息请参考 PWM 。

在 PWM 模式 1 或 PWM 模式 2 中，只有当比较结果改变了或者输出比较模式中从时基模式切换到 PWM模式时，O0CPRE 电平才改变。

通道 0 输出比较影子寄存器使能

<table><tr><td>2</td><td>CH0COMFEN</td><td>通道0输出比较快速使能当该位为1时,如果通道配置为PWM模式0或者PWM模式1,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH0_O被设置为比较电平而与比较结果无关。0:通道0输出比较快速禁能。当触发器的输入有一个有效沿时,激活CH0_O输出的最小延时为5个时钟周期1:通道0输出比较快速使能。当触发器的输入有一个有效沿时,激活CH0_O输出的最小延时为3个时钟周期</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道0I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH0EN位被清0)时,CH0MS[2:0]位才可以写。000:通道0配置为输出001:通道0配置为输入,ISO映射在CI0FE0上010:通道0配置为输入,ISO映射在CI1FE0上011:通道0配置为输入,ISO映射在ITS上。此模式仅工作在内部触发输入被选中时(由SYSCFG_TIMERxCFG2(x=1..4)寄存器中的TSCFG15[4:0]位域选择)。100~111:保留</td></tr></table>

## 输入捕获模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH1MS[2]</td><td>通道1模式选择与输出模式相同。</td></tr><tr><td>30</td><td>CH0MS[2]</td><td>通道0模式选择与输出模式相同。</td></tr><tr><td>29:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>CH1CAPFLT[3:0]</td><td>通道1输入捕获滤波控制参见CH0CAPFLT描述。</td></tr><tr><td>11:10</td><td>CH1CAPPSC[1:0]</td><td>通道1输入捕获预分频器参见CH0CAPPSC描述。</td></tr><tr><td>9:8</td><td>CH1MS[1:0]</td><td>通道1模式选择与输出模式相同。</td></tr><tr><td>7:4</td><td>CH0CAPFLT[3:0]</td><td>通道0输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了CI0输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=20010:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=4</td></tr></table>

0011：f<sub>SAMP</sub> = f<sub>CK_TIMER</sub>，N=8 

0100：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=6 

0101：f<sub>SAMP</sub>=f<sub>DTS</sub>/2，N=8 

0110：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=6 

0111：f<sub>SAMP</sub>=f<sub>DTS</sub>/4，N=8 

1000：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=6 

1001：f<sub>SAMP</sub>=f<sub>DTS</sub>/8，N=8 

1010：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=5 

1011：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=6 

1100：f<sub>SAMP</sub>=f<sub>DTS</sub>/16，N=8 

1101：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=5 

1110：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=6 

1111：f<sub>SAMP</sub>=f<sub>DTS</sub>/32，N=8 

## 3:2 CH0CAPPSC[1:0] 通道 0 输入捕获预分频器

这 2 位定义了通道0 输入的预分频系数。当 TIMERx_CHCTL2 寄存器中的CH0EN =0 时，则预分频器复位。

00：无预分频器，捕获输入口上检测到的每一个边沿都触发一次捕获

01：每 2 个事件触发一次捕获

10：每 4 个事件触发一次捕获

11：每 8 个事件触发一次捕获

与输出比较模式相同。

## 通道控制寄存器 1（TIMERx_CHCTL1）

地址偏移：0x1C

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">CH3MS[2]</td><td rowspan="2">CH2MS[2]</td><td>CH3COMADDSEN</td><td>CH2COMADDSEN</td><td>CH3ADDUPS</td><td>CH2ADDUPS</td><td rowspan="2">保留</td><td>CH3COMCTL[3]</td><td rowspan="2" colspan="7">保留</td><td>CH2COMCTL[3]</td></tr><tr><td>保留</td><td>保留</td><td>保留</td><td>保留</td><td>保留</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="9">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3COMCEN</td><td colspan="3">CH3COMCTL[2:0]</td><td>CH3COMSEN</td><td>CH3COMFEN</td><td rowspan="2" colspan="2">CH3MS[1:0]</td><td>CH2COMCEN</td><td colspan="3">CH2COMCTL[2:0]</td><td>CH2COMSEN</td><td>CH2COMFEN</td><td rowspan="2" colspan="2">CH2MS[1:0]</td></tr><tr><td colspan="4">CH3CAPFLT[3:0]</td><td colspan="2">CH3CAPPSC[1:0]</td><td colspan="4">CH2CAPFLT[3:0]</td><td colspan="2">CH2CAPPSC[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

## 输出比较模式：

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3MS[2]</td><td>通道3 I/O模式选择参考CH3MS[1:0]描述。</td></tr><tr><td>30</td><td>CH2MS[2]</td><td>通道2 I/O模式选择参考CH2MS[1:0]描述。</td></tr><tr><td>29</td><td>CH3COMADDSEN</td><td>通道3附加输出比较影子寄存器使能参考CH2COMADDSEN描述。</td></tr><tr><td>28</td><td>CH2COMADDSEN</td><td>通道2附加输出比较影子寄存器使能当此位被置1,TIMERx_CH2COMV_ADD寄存器的影子寄存器使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道2附加输出/比较影子寄存器1:使能通道2附加输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。</td></tr><tr><td>27</td><td>CH3ADDUPS</td><td>通道3附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH3COMV_ADD寄存器1:在发生计数器计数值匹配CH3VAL值时,更新TIMERx_CH3COMV_ADD寄存器</td></tr><tr><td>26</td><td>CH2ADDUPS</td><td>通道2附加寄存器更新源0:在发生更新事件时,更新TIMERx_CH2COMV_ADD寄存器1:在发生计数器计数值匹配CH2VAL值时,更新TIMERx_CH2COMV_ADD寄存器</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>CH3COMCTL[3]</td><td>通道3输出比较控制请参考CH2COMCTL[2:0]描述</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CH2COMCTL[3]</td><td>通道2输出比较控制请参考CH2COMCTL[2:0]描述</td></tr><tr><td>15</td><td>CH3COMCEN</td><td>通道3输出比较清0使能参见CH0COMCEN描述。</td></tr><tr><td>14:12</td><td>CH3COMCTL[2:0]</td><td>通道3输出比较模式参见CH0COMCTL描述。</td></tr><tr><td>11</td><td>CH3COMSEN</td><td>通道3输出比较影子寄存器使能参见CH0COMSEN描述。</td></tr><tr><td>10</td><td>CH3COMFEN</td><td>通道3输出比较快速使能参见 CH2COMFEN 描述</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2 寄存器的 CH3EN 位被清0)时这些位才可以写。000:通道3配置为输出001:通道3配置为输入,IS3映射在 CI3FE3 上010:通道3配置为输入,IS3映射在 CI2FE3 上011:通道3配置为输入,IS3映射在 ITS上,此模式仅工作在内部触发器输入被选中时(由SYSCFG_TIMERxCFG2(x=1..4)寄存器中的TSCFG15[4:0]位域选择)。100~111:保留</td></tr><tr><td>7</td><td>CH2COMCEN</td><td>通道2输出比较清0使能当此位被置1,当检测到ETIF输入高电平时,O2CPRE参考信号被清00:使能通道2输出比较清零1:禁止通道2输出比较清零</td></tr><tr><td>6:4</td><td>CH2COMCTL[2:0]</td><td>通道2输出比较模式此位定义了输出准备信号O2CPRE的动作,而O2CPRE决定了CH2_O的值。O2CPRE高电平有效,而CH2_O的有效电平取决于CH2P位。0000:时基。输出比较寄存器TIMERx_CH2CV与计数器TIMERx_CNT间的比较对O2CPRE不起作用0001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为高。0010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE为低。0011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH2CV相同时,强制O2CPRE翻转。0100:强制为低。强制O2CPRE为低电平0101:强制为高。强制O2CPRE为高电平0110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为有效电平,否则为无效电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为无效电平,否则为有效电平。0111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH2CV时,O2CPRE为无效电平,否则为有效电平。在向下计数时,一旦计数器的值大于TIMERx_CH2CV时,O2CPRE为有效电平,否则为无效电平。1000:可延时的单脉冲模式0。O2CPRE的输出情况类似与PWM模式0。在向上计数模式时,O2CPRE先输出有效电平,当外部触发事件发生时,立即输出无效电平,当下一次更新事件发生时,再变成有效电平;在向下计数模式时,O2CPRE先输出无效电平,当外部触发事件发生时,立即输出有效电平,当下一次更新事件发生时,再变成无效电平。1001:可延时的单脉冲模式1。O2CPRE的输出情况类似与PWM模式1。在向上计数模式时,O2CPRE先输出无效电平,当外部触发事件发生时,立即输出有效电平,当下一次更新事件发生时,再变成无效电平;在向下计数模式时,O2CPRE先输出有效电平,当外部触发事件发生时,立即输出无效电平,当下一次更新事件发生时,再变成有效电平。1010:可编程的脉冲输出。当计数器计数值与输出比较寄存器TIMERx_CH2CV匹配时,CH2_O上输出可编程的脉冲。脉冲由TIMERx_DECCTL寄存器中的OPPSC[2:0]和OPWID[7:0]位域配置。1011:输出DIR位。O2CPRE信号表示DIR位(在TIMERx_CTL0寄存器中)的值。1100/1101/1110/1111:保留注意:在复合PWM模式下(CH2CPWMEN=1'b1和CH2MS=3'b000),通道2的PWM输出信号由TIMERx_CH2CV和TIMERx_CH2COMV_ADD寄存器共同确定。详细信息请参考复合PWM模式。在PWM模式1或PWM模式2中,只有当比较结果改变了或者输出比较模式中从时基模式切换到PWM模式时,O2CPRE电平才改变。</td></tr><tr><td>3</td><td>CH2COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH2CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道2输出/比较影子寄存器1:使能通道2输出/比较影子寄存器仅在单脉冲模式下(TIMERx_CTL0寄存器的SPM=1),可以在未确认预装载寄存器情况下使用PWM模式。</td></tr><tr><td>2</td><td>CH2COMFEN</td><td>通道2输出比较快速使能当该位为1时,如果通道配置为PWM模式0或者PWM模式1,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH2_O被设置为比较电平而与比较结果无关。0:通道2输出比较快速禁能。当触发器的输入有一个有效沿时,激活CH2_O输出的最小延时为5个时钟周期1:通道2输出比较快速使能。当触发器的输入有一个有效沿时,激活CH2_O输出的最小延时为3个时钟周期</td></tr><tr><td>1:0</td><td>CH2MS[1:0]</td><td>通道2I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭(TIMERx_CHCTL2寄存器的CH2EN位被清0)时这些位才可写。000:通道2配置为输出001:通道2配置为输入,IS2映射在CI2FE2上010:通道2配置为输入,IS2映射在CI3FE2上011:通道2配置为输入,IS2映射在ITS上。此模式仅工作在内部触发输入被选中时(由SYSCFG_TIMERxCFG2(x=1..4)寄存器中的TSCFG15[4:0]位域选择)。</td></tr></table>


输入捕获模式：


100~111：保留

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3MS[2]</td><td>通道3模式选择与输出模式相同。</td></tr><tr><td>30</td><td>CH2MS[2]</td><td>通道2模式选择与输出模式相同。</td></tr><tr><td>29:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>CH3CAPFLT[3:0]</td><td>通道3输入捕获滤波控制参见CH0CAPFLT描述。</td></tr><tr><td>11:10</td><td>CH3CAPPSC[1:0]</td><td>通道3输入捕获预分频器参见CH0CAPPSC描述。</td></tr><tr><td>9:8</td><td>CH3MS[1:0]</td><td>通道3模式选择与输出模式相同。</td></tr><tr><td>7:4</td><td>CH2CAPFLT[3:0]</td><td>通道2输入捕获滤波控制数字滤波器由一个事件计数器组成,它记录N个输入事件后会产生一个输出的跳变。这些位定义了CI2输入信号的采样频率和数字滤波器的长度。0000:无滤波器,<eq>f_{SAMP} = f_{DTS}</eq>,N=10001:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=20010:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=40011:<eq>f_{SAMP} = f_{CK\_TIMER}</eq>,N=80100:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=60101:<eq>f_{SAMP} = f_{DTS}/2</eq>,N=80110:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=60111:<eq>f_{SAMP} = f_{DTS}/4</eq>,N=81000:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=61001:<eq>f_{SAMP} = f_{DTS}/8</eq>,N=81010:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=51011:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=61100:<eq>f_{SAMP} = f_{DTS}/16</eq>,N=81101:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=51110:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=61111:<eq>f_{SAMP} = f_{DTS}/32</eq>,N=8</td></tr></table>

## 通道控制寄存器 2（TIMERx_CHCTL2）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH3NP</td><td>保留</td><td>CH3P</td><td>CH3EN</td><td>CH2NP</td><td>保留</td><td>CH2P</td><td>CH2EN</td><td>CH1NP</td><td>保留</td><td>CH1P</td><td>CH1EN</td><td>CH0NP</td><td>保留</td><td>CH0P</td><td>CH0EN</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CH3NP</td><td>通道3互补输出极性参考CH0NP描述。</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>CH3P</td><td>通道3极性参考CH0P描述。</td></tr><tr><td>12</td><td>CH3EN</td><td>通道3使能参考CH0EN描述。</td></tr><tr><td>11</td><td>CH2NP</td><td>通道2互补输出极性参考CH0NP描述。</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CH2P</td><td>通道2极性参考CH0P描述。</td></tr><tr><td>8</td><td>CH2EN</td><td>通道2使能参考CH0EN描述。</td></tr><tr><td>7</td><td>CH1NP</td><td>通道1互补输出极性参考CH0NP描述。</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CH1P</td><td>通道1极性参考CH0P描述。</td></tr><tr><td>4</td><td>CH1EN</td><td>通道1使能参考CH0EN描述。</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,该位必须保持复位值。当通道0配置为输入模式时,此位和CH0P联合使用,作为输入信号CI0的极性选择控制信号。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0P</td><td>通道0极性当通道0配置为输出模式时,此位定义了输出信号极性。0:通道0高电平有效1:通道0低电平有效当通道0配置为输入模式时,此位定义了通道0输入信号极性。[CH0NP,CH0P]将选择CI0FE0或者CI1FE0的有效边沿或者捕获极性。00:把CIxFE0的上升沿作为捕获或者从模式下触发的有效信号,并且CIxFE0不会被翻转。01:把CIxFE0的下降沿作为捕获或者从模式下触发的有效信号,并且CIxFE0会被翻转。10:保留。11:把CIxFE0的上升沿和下降沿都作为捕获或者从模式下触发的有效信号,并且CIxFE0不会被翻转。</td></tr><tr><td>0</td><td>CH0EN</td><td>通道0捕获/比较使能当通道0配置为输出模式时,将此位置1使能CH0_O信号有效。当通道0配置为输入模式时,将此位置1使能通道0上的捕获事件。0:禁止通道01:使能通道0</td></tr></table>

## 计数器寄存器（TIMERx_CNT）（TIMERx, x = 2, 3）

地址偏移：0x24

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UPIFBU</td><td colspan="15">保留</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UPIFBU</td><td>UPIF位备份该位只读,是 TIMERx_INTF 寄存器的 UPIF 位的备份值。当 UPIFBUEN = 1 时,该位有效,若 UPIFBUEN =0,该位保留,读取该位值为零。</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。当 PWMADMEN = 0 时,该位域表示当前计数器的值。写操作该位域可以改变计数器的值。当 PWMADMEN = 1 时,该位域仅用于表示计数器值的整数部分,不包含小数部分。</td></tr></table>

计数器寄存器（TIMERx_CNT）（TIMERx, x = 1, 4）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CNT[31]</td><td rowspan="2" colspan="15">CNT[30:16]</td></tr><tr><td>UPIFBU</td></tr><tr><td>rw /r</td><td colspan="15">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

## UPIFBUEN = 0:

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CNT[31:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。当 PWMADMEN = 0 时,该位域表示当前计数器的值。写操作该位域可以改变计数器的值。当PWMADMEN = 1时,该位域仅用于表示计数器值的整数部分,不包含小数部分。</td></tr></table>


UPIFBUEN = 1: 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UPIFBU</td><td>UPIF位备份该位只读,是TIMERx_INTF寄存器的UPIF位的备份值。当UPIFBUEN = 1时,该位有效,若UPIFBUEN =0,该位保留,读取该位值为零。</td></tr><tr><td>30</td><td>CNT[30:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。当PWMADMEN = 0时,该位域表示当前计数器的值。写操作该位域可以改变计数器的值。当PWMADMEN = 1时,该位域仅用于表示计数器值的整数部分,不包含小数部分。</td></tr></table>

## 预分频寄存器（TIMERx_PSC）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值计数器时钟等于PSC时钟除以(PSC+1),每次当更新事件产生时,PSC的值被装入当前预分频寄存器。</td></tr></table>

## 计数器自动重载寄存器（TIMERx_CAR）（TIMERx, x = 2, 3）

地址偏移：0x2C

复位值：0x FFFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CARL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CARL[19:16]</td><td>计数器自动重载值(16位至19位)当PWMADMEN=0时,CARL[19:16]位域值0000。当PWMADMEN=1时,CARL[19:16]位域用于表示自动重载值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值(0位至15位)这些位定义了计数器的自动重载值。当PWMADMEN=0时,CARL[15:0]位域用于表示计数器的自动重载值。当PWMADMEN=1时,CARL[15:0]位域用于表示自动重载值的整数部分。</td></tr></table>

## 计数器自动重载寄存器（TIMERx_CAR）（TIMERx, x = 1, 4）

地址偏移：0x2C

复位值：0x FFFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CARL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CARL[31:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。当PWMADMEN=0时,CARL[31:0]位域用于表示计数器的自动重载值。当PWMADMEN=1时,CARL[27:0]位域用于表示自动重载值的整数部分,CARL[31:28]位域用于表示自动重载值的整数部分。</td></tr></table>

## 通道 0 捕获/比较值寄存器（TIMERx_CH0CV）（TIMERx, x = 2, 3）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CHOVAL[19:16]</td><td colspan="12">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CH0VAL[19:16]</td><td>通道0的捕获或比较值(16位到19位)当通道0配置为输入模式时,CH0VAL[19:16]位域值为0000。当通道0配置为输出模式时,该位域包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH0VAL[19:16]位域值为0000。当PWMADMEN=1时,CH0VAL[19:16]用于表示比较值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道0的捕获或比较值(0位至15位)当通道0配置为输入模式时,CH0VAL[15:0]决定了上次捕获事件的计数器值,且该位域只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH0VAL[15:0]位域值表示比较值。当PWMADMEN=1时,CH0VAL[15:0]用于表示比较值的整数部分。</td></tr></table>

## 通道 0 捕获/比较值寄存器（TIMERx_CH0CV）（TIMERx, x = 1, 4）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH0VAL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CH0VAL[31:0]</td><td>通道0的捕获或比较值当通道0配置为输入模式时,CH0VAL[31:28]位域值为0000,CH0VAL[27:0]位域表示上次捕获事件的计数器值,且该位域只读。当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

当 PWMADMEN = 0 时，CH0VAL[31:0]位域值表示计数器的比较值。

当 PWMADMEN = 1 时，CH0VAL[27:0]位域用于表示比较值的整数部分，CH0VAL[31:28]用于表示比较值的小数部分。

## 通道 1 捕获/比较值寄存器（TIMERx_CH1CV）（TIMERx, x = 2, 3）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CH1VAL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CH1VAL[19:16]</td><td>通道1的捕获或比较值(16位到19位)当通道1配置为输入模式时,CH1VAL[19:16]位域值为0000。当通道1配置为输出模式时,该位域包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH1VAL[19:16]位域值为0000。当PWMADMEN=1时,CH1VAL[19:16]用于表示比较值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH1VAL[15:0]</td><td>通道1的捕获或比较值(0位至15位)当通道1配置为输入模式时,CH1VAL[15:0]决定了上次捕获事件的计数器值,且该位域只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH1VAL[15:0]位域值表示比较值。当PWMADMEN=1时,CH1VAL[15:0]用于表示比较值的整数部分。</td></tr></table>

通道 1 捕获/比较值寄存器（TIMERx_CH1CV）（TIMERx, x = 1, 4）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH1VAL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CH1VAL[31:0]</td><td>通道1的捕获或比较值当通道1配置为输入模式时,CH1VAL[31:28]位域值为0000,CH1VAL[27:0]位域表示上次捕获事件的计数器值,且该位域只读。当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH1VAL[31:0]位域值表示计数器的比较值。当PWMADMEN=1时,CH1VAL[27:0]位域用于表示比较值的整数部分,CH1VAL[31:28]用于表示比较值的小数部分。</td></tr></table>

## 通道 2 捕获/比较值寄存器（TIMERx_CH2CV）（TIMERx, x = 2, 3）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CH2VAL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CH2VAL[19:16]</td><td>通道2的捕获或比较值(16位到19位)当通道2配置为输入模式时,CH2VAL[19:16]位域值为0000。当通道2配置为输出模式时,该位域包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH2VAL[19:16]位域值为0000。当PWMADMEN=1时,CH2VAL[19:16]用于表示比较值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH2VAL[15:0]</td><td>通道2的捕获或比较值(0位至15位)当通道2配置为输入模式时,CH2VAL[15:0]决定了上次捕获事件的计数器值,且该</td></tr></table>## 通道 2 捕获/比较值寄存器（TIMERx_CH2CV）（TIMERx, x = 1, 4）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH2VAL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CH2VAL[31:0]</td><td>通道2的捕获或比较值当通道2配置为输入模式时,CH2VAL[31:28]位域值为0000,CH2VAL[27:0]位域表示上次捕获事件的计数器值,且该位域只读。当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH2VAL[31:0]位域值表示计数器的比较值。当PWMADMEN=1时,CH2VAL[27:0]位域用于表示比较值的整数部分,CH2VAL[31:28]用于表示比较值的小数部分。</td></tr></table>

## 通道 3 捕获/比较值寄存器（TIMERx_CH3CV）（TIMERx, x = 2, 3）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">CH3VAL[19:16]</td><td colspan="12">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>CH3VAL[19:16]</td><td>通道3的捕获或比较值(16位到19位)当通道3配置为输入模式时,CH3VAL[19:16]位域值为0000。当通道3配置为输出模式时,该位域包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH3VAL[19:16]位域值为0000。当PWMADMEN=1时,CH3VAL[19:16]用于表示比较值的小数部分。</td></tr><tr><td>27:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CH3VAL[15:0]</td><td>通道3的捕获或比较值(0位至15位)当通道3配置为输入模式时,CH3VAL[15:0]决定了上次捕获事件的计数器值,且该位域只读。当通道3配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH3VAL[15:0]位域值表示比较值。当PWMADMEN=1时,CH3VAL[15:0]用于表示比较值的整数部分。</td></tr></table>

## 通道 3 捕获/比较值寄存器（TIMERx_CH3CV）（TIMERx, x = 1, 4）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH3VAL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CH3VAL[31:0]</td><td>通道3的捕获或比较值当通道3配置为输入模式时,CH3VAL[31:28]位域值为0000,CH3VAL[27:0]位域表示上次捕获事件的计数器值,且该位域只读。当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应的影子寄存器后,影子寄存器值随每次更新事件更新。当PWMADMEN=0时,CH3VAL[31:0]位域值表示计数器的比较值。当PWMADMEN=1时,CH3VAL[27:0]位域用于表示比较值的整数部分,CH3VAL[31:28]用于表示比较值的小数部分。</td></tr></table>

## 通道 0 附加比较寄存器（TIMERx_CH0COMV_ADD）

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH0COMVAL_ADD[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>CH0COMVAL_ADD[31:16]</td><td>通道0附加比较值(位16到位31)该位域仅用于TIMER1/4。</td></tr><tr><td>15:0</td><td>CH0COMVAL_ADD[15:0]</td><td>通道0附加比较值(位0到位15)当通道0配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>

## 通道 1 附加比较寄存器（TIMERx_CH1COMV_ADD）

地址偏移：0x68

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH1COMVAL_ADD[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH1COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>CH1COMVAL_ADD[31:16]</td><td>通道1附加比较值(位16到位31)该位域仅用于TIMER1/4。</td></tr><tr><td>15:0</td><td>CH1COMVAL_ADD[15:0]</td><td>通道1附加比较值(位0到位15)当通道1配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

注意：该寄存器仅用于复合PWM模式（当CH0CPWMEN=1时）。

## 通道 2 附加比较寄存器（TIMERx_CH2COMV_ADD）

地址偏移：0x6C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH2COMVAL_ADD[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH2COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>CH2COMVAL_ADD[31:16]</td><td>通道2附加比较值(位16到位31)该位域仅用于TIMER1/4。</td></tr><tr><td>15:0</td><td>CH2COMVAL_ADD[15:0]</td><td>通道2附加比较值(位0到位15)当通道2配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。注意:该寄存器仅用于复合PWM模式(当CH0CPWMEN=1时)。</td></tr></table>


通道 3 附加比较寄存器（TIMERx_CH3COMV_ADD）



地址偏移：0x70



复位值：0x0000 0000



该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CH3COMVAL_ADD[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH3COMVAL_ADD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>CH3COMVAL_ADD[31:16]</td><td>通道3附加比较值(位16到位31)该位域仅用于TIMER1/4。</td></tr><tr><td>15:0</td><td>CH3COMVAL_ADD</td><td>通道3附加比较值(位0到位15)</td></tr></table>

[15:0] 

当通道3配置为输出模式时，这些位包含了即将和计数器比较的值。使能相应影子寄存器后，影子寄存器值随每次更新事件更新。

注意：该寄存器仅用于复合PWM模式（当CH0CPWMEN=1时）。

控制寄存器 2（TIMERx_CTL2）

地址偏移：0x74

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH3C PWMEN</td><td>CH2C PWMEN</td><td>CH1C PWMEN</td><td>CH0C PWMEN</td><td colspan="8">保留</td><td>DECDISDEN</td><td>DECJDEN</td><td colspan="2">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CH3OMPSEL[1:0]</td><td colspan="2">CH2OMPSEL[1:0]</td><td colspan="2">CH1OMPSEL[1:0]</td><td colspan="2">CH0OMPSEL[1:0]</td><td colspan="8">保留</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH3CPWMEN</td><td>通道3复合PWM模式使能0:通道3复合PWM模式禁能1:通道3复合PWM模式使能</td></tr><tr><td>30</td><td>CH2CPWMEN</td><td>通道2复合PWM模式使能0:通道2复合PWM模式禁能1:通道2复合PWM模式使能</td></tr><tr><td>29</td><td>CH1CPWMEN</td><td>通道1复合PWM模式使能0:通道1复合PWM模式禁能1:通道1复合PWM模式使能</td></tr><tr><td>28</td><td>CH0CPWMEN</td><td>通道0复合PWM模式使能0:通道0复合PWM模式禁能1:通道0复合PWM模式使能</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>DECDISDEN</td><td>正交译码器信号断线检测使能0:正交译码器信号断线检测禁能1:正交译码器信号断线检测使能</td></tr><tr><td>18</td><td>DECJDEN</td><td>正交译码器信号跳变(两个信号同时发生跳变沿)检测使能0:正交译码器信号跳变(两个信号同时发生跳变沿)检测禁能1:正交译码器信号跳变(两个信号同时发生跳变沿)检测使能</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>CH3OMPSEL[1:0]</td><td>通道3输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O3CPRE(用来驱动CH3_O信号)。00:O3CPRE信号根据CH3COMCTL[2:0]位的配置输出。01:只有在计数器向上计数,匹配事件发生时,O3CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O3CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或向下计数,匹配事件发生时,O3CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。</td></tr><tr><td>13:12</td><td>CH2OMPSEL[1:0]</td><td>通道2输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O2CPRE(用来驱动CH2_O信号)。00:O2CPRE信号根据CH2COMCTL[2:0]位的配置正常输出。01:只有在计数器向上计数,匹配事件发生时,O2CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O2CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或者向下计数,匹配事件发生时,O2CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。</td></tr><tr><td>11:10</td><td>CH1OMPSEL[1:0]</td><td>通道1输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O1CPRE(用来驱动CH1_O信号)。00:O1CPRE信号根据CH1COMCTL[2:0]位的配置正常输出。01:只有在计数器向上计数,匹配事件发生时,O1CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O1CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或者向下计数,匹配事件发生时,O1CPRE信号输出一个脉冲,且脉冲宽度是一个CK_TIMER时钟周期。</td></tr><tr><td>9:8</td><td>CH0OMPSEL[1:0]</td><td>通道0输出匹配脉冲选择当匹配事件发生时,该位用于选择准备输出信号O0CPRE(用来驱动CH0_O信号)。00:O0CPRE信号根据CH0COMCTL[2:0]位的配置正常输出。01:只有在计数器向上计数,匹配事件发生时,O0CPRE信号输出一个脉冲,并且脉冲宽度是一个CK_TIMER时钟周期。10:只有在计数器向下计数,匹配事件发生时,O0CPRE信号输出一个脉冲,脉冲宽度是一个CK_TIMER时钟周期。11:在计数器向上计数或者向下计数,匹配事件发生时,O0CPRE信号输出一个脉</td></tr></table>

冲，脉冲宽度是一个 CK_TIMER 时钟周期。

7:0 保留 必须保持复位值。

备用功能控制寄存器 1（TIMERx_AFCTL1）

地址偏移：0x90

复位值：0x0000 0007

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="3">OCRINSEL[2:0]</td><td colspan="3">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td colspan="3">描述</td></tr><tr><td>31:22</td><td>保留</td><td colspan="3">必须保持复位值。</td></tr><tr><td rowspan="14">21:19</td><td rowspan="14">OCRINSEL[2:0]</td><td colspan="3">OCPRE_CLR输入选择</td></tr><tr><td colspan="3">000: OCPRE_CLR0</td></tr><tr><td colspan="3">001: OCPRE_CLR1</td></tr><tr><td colspan="3">...</td></tr><tr><td colspan="3">111: OCPRE_CLR7</td></tr><tr><td>OCPRE_CLR 输入选择</td><td>TIMER1 / 2</td><td>TIMER3 / 4</td></tr><tr><td>OCPRE_CLR0</td><td>CMP0_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR1</td><td>CMP1_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR2</td><td>CMP2_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR3</td><td>CMP3_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR4</td><td>CMP4_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR5</td><td>CMP5_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR6</td><td>CMP6_OUT</td><td>保留</td></tr><tr><td>OCPRE_CLR7</td><td>CMP7_OUT</td><td>保留</td></tr><tr><td>18:0</td><td>保留</td><td colspan="3">必须保持复位值。</td></tr></table>

看门狗计数器周期寄存器（TIMERx_WDGPER）

地址偏移：0x94

复位值：0xFFFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WDGPER[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDGPER[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WDGPER[31:0]</td><td>看门狗计数器周期值这些位用于配置两个看门狗的计数器周期。当看门狗计数器连续计数到该值时,计数器计数超时且中断标志位DECDISIF位置位。若DECDISIE=1,则相应的中断产生。注意:该寄存器位仅用于正交译码器信号断线检测功能(DECDISDEN=1)使能。</td></tr></table>

## 译码器控制寄存器（TIMERx_DECCTL）

地址偏移：0xA0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td colspan="3">OPPSC[2:0]</td><td colspan="8">OPWID[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="2">INDP[1:0]</td><td>FINDRST</td><td colspan="2">保留</td><td colspan="2">INDRSTDIR[1:0]</td><td>INDRSTE N</td></tr><tr><td colspan="8"></td><td colspan="2">rw</td><td>rw</td><td colspan="2"></td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>OPPSC[2:0]</td><td>输出脉冲预分频该位域用于配置脉冲发生器的时钟分频系数。<eq>t_{opclk} = (2^{(OPPSC [2:0])}) \times t_{CK\_TIMER}</eq></td></tr><tr><td>23:16</td><td>OPWID[7:0]</td><td>输出脉冲宽度该位域用于配置脉冲的宽度<eq>t_{opw} = OPWID [7:0] \times t_{opclk}</eq></td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:6</td><td>INDP[1:0]</td><td>索引定位在正交解码器模式0~4中,该位域表示索引事件将在哪种类型的AB输入中复位计数00: 当AB相输入为00时,索引事件复位计数器01: 当AB相输入为01时,索引事件复位计数器10: 当AB相输入为10时,索引事件复位计数器11: 当AB相输入为11时,索引事件复位计数器在译码器模式0~3中,该位域表示索引事件将在哪种类型的AB输入中复位计数器:x0: 当时钟信号为低电平时,索引事件复位计数器x1: 当时钟信号为高电平时,索引事件复位计数器注意:在译码器模式0~3中,INDP[1]无效。</td></tr><tr><td>5</td><td>FINDRST</td><td>第一个索引信号复位计数器0: 所有的索引信号都可以复位计数器1: 只有第一个索引信号有效,可以复位计数器</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:1</td><td>INDRSTDIR[1:0]</td><td>索引信号复位计数器时的计数方向该位域用于配置计数器的计数方向和索引00: 当计数器向上和向下计数时,索引信号复位计数器01: 仅在计数器向上计数时,索引信号复位计数器10: 仅在计数器向下计数时,索引信号复位计数器11: 保留注意:仅在INDRSTEN=0时,可以修改INDRSTDIR[1:0]位域。</td></tr><tr><td>0</td><td>INDRSTEN</td><td>索引信号复位使能0: 索引信号复位计数器禁能1: 索引信号复位计数器使能</td></tr></table>

## DMA 配置寄存器（TIMERx_DMACFG）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">DMATC[5:0]</td><td colspan="2">保留</td><td colspan="6">DMATA[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>DMATC [5:0]</td><td>DMA 传输计数该位域定义了 DMA 访问(读写)TIMERx_DMATB 寄存器的数量。6'b000000:传输1次6'b000001:传输2次...6'b111000:传输57次</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>DMATA [5:0]</td><td>DMA 传输起始地址该位域定义了 DMA 访问 TIMERx_DMATB 寄存器的第一个地址。当通过 TIMERx_DMA 第一次访问时,访问的就是该位域指定的地址。第二次访问 TIMERx_DMATB 时,将访问起始地址+0x4。6'b000000: TIMERx_CTL06'b000001: TIMERx_CTL1...总之:起始地址 = TIMERx_CTL0 + DMATA*4。</td></tr></table>

## DMA 发送缓冲区寄存器（TIMERx_DMATB）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DMATB[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DMATB [31:0]</td><td>DMA 发送缓冲对这个寄存器的读或写,(起始地址+传输次数*4)地址范围内的寄存器会被访问传输次数由硬件计算,范围为 0 到 DMATC。</td></tr></table>

## 配置寄存器（TIMERx_CFG）

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
