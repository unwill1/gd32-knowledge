## 19.5. SHRTIMER 寄存器

SHRTIMER 基地址：0x4001 7400

寄存器进行分段寻址：

SHRTIMER Master_TIMER 寄存器基地址：0x4001 7400

SHRTIMER Slave_TIMER0 寄存器基地址：0x4001 7480

SHRTIMER Slave_TIMER1 寄存器基地址：0x4001 7500

SHRTIMER Slave_TIMER2 寄存器基地址：0x4001 7580

SHRTIMER Slave_TIMER3 寄存器基地址：0x4001 7600

SHRTIMER Slave_TIMER4 寄存器基地址：0x4001 7680

SHRTIMER 通用寄存器基地址：0x4001 7780

## 19.5.1. Master_TIMER 寄存器

SHRTIMER Master_TIMER 寄存器基地址：0x4001 7400

## Master_TIMER 控制寄存器 0 (SHRTIMER_MTCTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">UPSEL[1:0]</td><td>UPREP</td><td>保留</td><td>SHWEN</td><td colspan="2">DACTRGS[1:0]</td><td colspan="3">保留</td><td>ST4CEN</td><td>ST3CEN</td><td>ST2CEN</td><td>ST1CEN</td><td>ST0CEN</td><td>MTCEN</td></tr><tr><td colspan="2">rw</td><td>rw</td><td></td><td>rw</td><td colspan="2">rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">SYNOSRC[1:0]</td><td colspan="2">SYNOPLS[1:0]</td><td>SYNISTR T</td><td>SYNIRST</td><td colspan="2">SYNISRC[1:0]</td><td colspan="2">保留</td><td>HALFM</td><td>CNTRST M</td><td>CTNM</td><td colspan="3">CNTCKDIV[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>UPSEL[1:0]</td><td>更新事件选择该位域用于配置更新事件与DMA模式的关系。00: 更新事件产生与DMA模式无关。01: 在DMA模式下完成DMA传输时生成更新事件。10: 在DMA模式下DMA传输完成后,计数器翻转产生更新事件。仅适用于连续模式。11: 保留。</td></tr><tr><td>29</td><td>UPREP</td><td>重复事件生成更新事件该位用于使能重复事件生成更新事件。0: 重复事件生成更新事件禁能1: 重复事件生成更新事件使能注意:仅当UPSEL [1:0] = 2'b00或2'b01时才能设置UPREP。</td></tr><tr><td>28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27</td><td>SHWEN</td><td>影子寄存器使能0: 影子寄存器禁能1: 影子寄存器使能</td></tr><tr><td>26:25</td><td>DACTRGS[1:0]</td><td>DAC触发源发生更新事件时,定时器生成DAC触发事件。该位域用于配置哪个触发源触发事件。00: 不生成DAC触发事件01: 在SHRTIMER_DACTRIG0上生成DAC触发事件10: 在SHRTIMER_DACTRIG1上生成DAC触发事件11: 在SHRTIMER_DACTRIG2上生成DAC触发事件</td></tr><tr><td>24:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21</td><td>ST4CEN</td><td>Slave_TIMER4计数器使能0: Slave_TIMER4计数器禁能1: Slave_TIMER4计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>20</td><td>ST3CEN</td><td>Slave_TIMER3计数器使能0: Slave_TIMER3计数器禁能1: Slave_TIMER3计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>19</td><td>ST2CEN</td><td>Slave_TIMER2计数器使能0: Slave_TIMER2计数器禁能1: Slave_TIMER2计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>18</td><td>ST1CEN</td><td>Slave_TIMER1计数器使能0: Slave_TIMER1计数器禁能1: Slave_TIMER1计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>17</td><td>ST0CEN</td><td>Slave_TIMER0计数器使能0: Slave_TIMER0计数器禁能1: Slave_TIMER0计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>16</td><td>MTCEN</td><td>Master_TIMER计数器使能0: Master_TIMER计数器禁能1: Master_TIMER计数器使能注意:不得在小于8个tSHRTIMER_CK时钟周期内修改该位。</td></tr><tr><td>15:14</td><td>SYNOSRC[1:0]</td><td>同步输出源该位域用于配置发送到同步输出SHRTIMER_SCOUT上的事件。00:Master_TIMER启动事件。01:Master_TIMER比较0事件10:Slave_TIMER0复位和启动事件11:Slave_TIMER0比较0事件</td></tr><tr><td>13:12</td><td>SYNOPLS[1:0]</td><td>同步输出脉冲该位域用于配置同步输出SHRTIMER_SCOUT上的脉冲。00:脉冲生成禁能。SHRTIMER_SCOUT上无脉冲。01:保留。10:在SHRTIMER_SCOUT上产生正脉冲。它的长度是16个tSHRTIMER_CK个周期。11:在SHRTIMER_SCOUT上产生负脉冲。它的长度是16个tSHRTIMER_CK个周期。</td></tr><tr><td>11</td><td>SYNISTRT</td><td>同步输入启动计数器该位用于配置同步输入启动计数器。0:同步输入不能启动计数器。1:同步输入可以启动计数器。</td></tr><tr><td>10</td><td>SYNIRST</td><td>同步输入复位计数器该位用于配置同步输入复位计数器。0:同步输入不能复位计数器。1:同步输入可以复位计数器。</td></tr><tr><td>9:8</td><td>SYNISRC[1:0]</td><td>同步输入源该位域用于配置同步输入源。00:同步输入禁能。01:保留。10:内部信号:高级定时器TIMER0中的TIMER0_TRGO。11:外部信号:SHRTIMER_SCIN引脚上的正脉冲。注意:相应的计时器使能后,将无法修改此位字段</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>HALFM</td><td>半波模式该位置1时,SHRTIMER_MTCMP0V有效寄存器始终是计数器自动重载值(SHRTIMER_MTCAR)的一半。0:半波模式禁能。1:半波模式使能。</td></tr><tr><td>4</td><td>CNTRSTM</td><td>计数器复位模式该位用于定义单脉冲模式下计数器的行为。0:计数器只能计数到周期值后才能复位。1:可以随时复位计数器(运行或停止)。</td></tr><tr><td>3</td><td>CTNM</td><td>连续模式。0:单脉冲模式。当计数器达到SHRTIMER_MTCAR值时,它将由硬件停止。1:连续模式。计数器在达到SHRTIMER_MTCAR值时,翻转到0并连续计数。</td></tr><tr><td>2:0</td><td>CNTCKDIV[2:0]</td><td>计数器时钟分频该位域可以由软件配置,确定超高分辨率时钟(SHRTIMER_HPCK)和计数器时钟(SHRTIMER_PSCCK)的分频比。当SHRTIMER_MTACTL中的CNTCKDIV[3]为0时,<eq>f_{SHRTIMER\_PSCCK} = f_{SHRTIMER\_HPCK} / 2^{CNTCKDIV[2:0]+1}</eq>。当SHRTIMER_MTACTL中的CNTCKDIV[3]位为1,且CNTCKDIV[2:0]配置为3'b000时:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}</eq>0000:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 2</eq>0001:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 4</eq>0010:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 8</eq>0011:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 16</eq>0100:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 32</eq>0101:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 64</eq>0110:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 128</eq>0111:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 256</eq>1000:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}</eq>其他值保留。注意:一旦使能定时器,就不能修改CNTCKDIV[3:0]位域。</td></tr></table>

## Master_TIMER 中断标志寄存器(SHRTIMER_MTINTF)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>UPIF</td><td>SYNIIF</td><td>REPIF</td><td>CMP3IF</td><td>CMP2IF</td><td>CMP1IF</td><td>CMP0IF</td></tr><tr><td colspan="9"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>UPIF</td><td>更新中断标志发生更新事件时,此标志由硬件置位。0: 更新中断未发生1: 更新中断发生</td></tr><tr><td>5</td><td>SYNIIF</td><td>同步输入中断标志同步输入到来时,此标志由硬件置位。0: 同步输入未发生1: 同步输入发生</td></tr><tr><td>4</td><td>REPIF</td><td>重复中断标志</td></tr></table>

<table><tr><td></td><td></td><td>发生重复事件时,此标志由硬件置位。0: 重复中断未发生1: 重复中断发生</td></tr><tr><td>3</td><td>CMP3IF</td><td>比较3中断标志当发生比较3事件时,此标志由硬件置位。0: 比较3中断未发生1: 比较3中断发生</td></tr><tr><td>2</td><td>CMP2IF</td><td>比较2中断标志当发生比较2事件时,此标志由硬件置位。0: 比较2中断未发生1: 比较2中断发生</td></tr><tr><td>1</td><td>CMP1IF</td><td>比较1中断标志当发生比较3事件时,此标志由硬件置位。0: 比较1中断未发生1: 比较1中断发生</td></tr><tr><td>0</td><td>CMP0IF</td><td>比较0中断标志当发生比较0事件时,此标志由硬件置位。0: 比较0中断未发生1: 比较0中断发生</td></tr></table>

## Master_TIMER 中断标志清除寄存器(SHRTIMER_MTINTC)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>UPIFC</td><td>SYNIIFC</td><td>REPIFC</td><td>CMP3IFC</td><td>CMP2IFC</td><td>CMP1IFC</td><td>CMP0IFC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>UPIFC</td><td>更新中断标志清除0:没有影响1:清除更新中断标志</td></tr><tr><td>5</td><td>SYNIIFC</td><td>同步输入中断标志清除0:没有影响1:清除同步输入中断标志</td></tr><tr><td>4</td><td>REPIFC</td><td>重复中断标志清除0:没有影响1:清除重复中断标志</td></tr><tr><td>3</td><td>CMP3IFC</td><td>比较3中断标志清除0:没有影响1:清除比较3中断标志</td></tr><tr><td>2</td><td>CMP2IFC</td><td>比较2中断标志清除0:没有影响1:清除比较2中断标志</td></tr><tr><td>1</td><td>CMP1IFC</td><td>比较1中断标志清除0:没有影响1:清除比较1中断标志</td></tr><tr><td>0</td><td>CMP0IFC</td><td>比较0中断标志清除0:没有影响1:清除比较0中断标志</td></tr></table>

## Master_TIMER DMA 和中断使能寄存器 (SHRTIMER_MTDMAINTEN)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>UPDEN</td><td>SYNIDEN</td><td>REPDEN</td><td>CMP3DEN</td><td>CMP2DEN</td><td>CMP1DEN</td><td>CMP0DEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>UPIE</td><td>SYNIIE</td><td>REPIE</td><td>CMP3IE</td><td>CMP2IE</td><td>CMP1IE</td><td>CMP0IE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22</td><td>UPDEN</td><td>更新 DMA 请求使能0:禁能1:使能</td></tr><tr><td>21</td><td>SYNIDEN</td><td>同步输入 DMA 请求使能0:禁能1:使能</td></tr><tr><td>20</td><td>REPDEN</td><td>重复 DMA 请求使能0:禁能1:使能</td></tr></table>

<table><tr><td>19</td><td>CMP3DEN</td><td>比较3DMA请求使能0:禁能1:使能</td></tr><tr><td>18</td><td>CMP2DEN</td><td>比较2DMA请求使能0:禁能1:使能</td></tr><tr><td>17</td><td>CMP1DEN</td><td>比较1DMA请求使能0:禁能1:使能</td></tr><tr><td>16</td><td>CMP0DEN</td><td>比较0DMA请求使能0:禁能1:使能</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>UPIE</td><td>更新中断使能0:禁能1:使能</td></tr><tr><td>5</td><td>SYNIIE</td><td>同步输入中断使能0:禁能1:使能</td></tr><tr><td>4</td><td>REPIE</td><td>重复中断使能0:禁能1:使能</td></tr><tr><td>3</td><td>CMP3IE</td><td>比较3中断使能0:禁能1:使能</td></tr><tr><td>2</td><td>CMP2IE</td><td>比较2中断使能0:禁能1:使能</td></tr><tr><td>1</td><td>CMP1IE</td><td>比较1中断使能0:禁能1:使能</td></tr><tr><td>0</td><td>CMP0IE</td><td>比较0中断使能0:禁能1:使能</td></tr></table>

## Master_TIMER 计数器寄存器(SHRTIMER_MTCNT)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>当前计数器值。对该位域进行写操作可以更改计数器的值。仅当Master_TIMER停止(SHRTIMER_MTCTL0寄存器中的MTCEN=0)时,对其进行写操作才能更改计数器的值。注意:(1)计数器时钟分频系数小于64(CNTCKDIV[3:0]&lt;5)时,计数器的最低有效位无效,它们不能被写入,读出值为0。(2)如果写入该位域的值高于SHRTIMER_MPER寄存器值,则定时器的行为是不可预测的。</td></tr></table>

## Master_TIMER 计数器自动重载寄存器(SHRTIMER_MTCAR)

地址偏移：0x14

复位值：0x0000 FFDF

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值该位域定义了计数器的自动重载值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于(3*tSHRTIMER_CK)。例如:当CNTCKDIV [3:0]=4&#x27;b0000时,CARL [15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV [3:0]=4&#x27;b0000时,CARL [15:0]&lt;= 0xFFDF。</td></tr></table>

## Master_TIMER 重复计数寄存器(SHRTIMER_MTCREP)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>CREP[7:0]</td><td>重复计数器值该位域用于定义重复事件的发生率。当重复计数器递减计数到零时,连续模式下即将发生的翻转事件或复位事件将产生一个重复事件。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN = 0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。</td></tr></table>

## Master_TIMER 比较 0 寄存器(SHRTIMER_MTCMP0V)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP0VAL[15:0]</td><td>比较0值该位域用于配置与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于3个tSHRTIMER_CK。例如:当CNTCKDIV [3:0]=4&#x27;b0000时,CARL [15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV [3:0]</td></tr></table>

= 4’b0000 时，CARL [15:0] <= 0xFFDF。

## Master_TIMER 比较 1 寄存器(SHRTIMER_MTCMP1V)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP1VAL[15:0]</td><td>比较1值该位域用于配置与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于3个<eq>t_{SHRTIMER\_CK}</eq>。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&lt;=0xFFDF。</td></tr></table>

## Master_TIMER 比较 2 寄存器(SHRTIMER_MTCMP2V)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP2VAL[15:0]</td><td>比较2值该位域用于配置与计数器进行比较的值。</td></tr></table>

该寄存器具有影子寄存器。如果影子寄存器被禁能（SHWEN = 0），它将保存有效寄存器的内容；否则，它将保存影子寄存器的内容。

注意：

（1）最小值必须大于或等于 3 个 t<sub>SHRTIMER_CK</sub>。例如：当 CNTCKDIV [3:0] = 4’b0000时，CARL [15:0] > = 0x60。

（2）最大值必须小于或等于（0xFFFF –1*t<sub>SHRTIMER_CK</sub>）。例如：当 CNTCKDIV [3:0]= 4’b0000 时，CARL [15:0] <= 0xFFDF。

## Master_TIMER 比较 3 寄存器(SHRTIMER_MTCMP3V)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP3VAL[15:0]</td><td>比较3值该位域用于配置与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于3个<eq>t_{SHRTIMER\_CK}</eq>。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&lt;=0xFFDF。</td></tr></table>

## Master_TIMER 附加控制寄存器(SHRTIMER_MTACTL)

地址偏移：0x7C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>CNTCKDIV[3]</td><td colspan="3">保留</td></tr><tr><td colspan="12">位/位域</td><td>名称</td><td colspan="3">描述</td></tr><tr><td colspan="12">31:4</td><td>保留</td><td colspan="3">必须保持复位值</td></tr><tr><td colspan="12">3</td><td>CNTCKDIV[3]</td><td colspan="3">计数器时钟分频该位位域可以由软件配置,确定超高分辨率时钟(SHRTIMER_HPCK)和计数器时钟(SHRTIMER_PSCCK)的分频比。当SHRTIMER_MTACTL中的CNTCKDIV[3]为0时,<eq>f_{SHRTIMER\_PSCCK} = f_{SHRTIMER\_HPCK} / 2^{CNTCKDIV [2:0] + 1}</eq>。当SHRTIMER_MTACTL中的CNTCKDIV[3]位为1并且CNTCKDIV[2:0]只能配置为3'b000时:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}</eq>注意:一旦使能定时器,就不能修改CNTCKDIV[3:0]位域。</td></tr></table>

2:0 保留 必须保持复位值

## 19.5.2. Slave_TIMERx 寄存器(x=0..4)

SHRTIMER Slave_TIMER0 寄存器基地址：0x4001 7480

SHRTIMER Slave_TIMER1 寄存器基地址：0x4001 7500

SHRTIMER Slave_TIMER2 寄存器基地址：0x4001 7580

SHRTIMER Slave_TIMER3 寄存器基地址：0x4001 7600

SHRTIMER Slave_TIMER4 寄存器基地址：0x4001 7680

## Slave_TIMERx 控制寄存器 0 (SHRTIMER_STxCTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">UPSEL[3:0]</td><td>SHWEN</td><td colspan="2">DACTRGS[1:0]</td><td>UPBMT</td><td>UPBST4</td><td>UPBST3</td><td>UPBST2</td><td>UPBST1</td><td>UPBST0</td><td>UPRST</td><td>UPREP</td><td>保留</td></tr><tr><td></td><td colspan="3">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">DELCMP3M[1:0]</td><td colspan="2">DELCMP1M[1:0]</td><td>SYNISTR T</td><td>SYNIRST</td><td colspan="3">保留</td><td>BLNMEN</td><td>HALFM</td><td>CNTRST M</td><td>CTNM</td><td colspan="3">CNTCKDIV[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>UPSEL[3:0]</td><td>更新事件选择该位域用于配置更新事件与DMA模式的关系。0000: 更新事件的生成独立于DMA模式。0001: 在DMA模式下完成DMA传输时生成更新事件。0010: 在DMA模式下完成DMA传输后的更新事件,生成更新事件。0011:在STxUPIN0的上升沿生成更新事件。0100:在STxUPIN1的上升沿生成更新事件。0101:在STxUPIN2的上升沿生成更新事件。0110:在STxUPIN0的上升沿到来之后的更新事件,生成更新事件。0111:在STxUPIN1的上升沿到来之后的更新事件,生成更新事件。1000:在STxUPIN2的上升沿到来之后的更新事件,生成更新事件。其他值保留。注意:(1)在写入新值之前,必须先复位该位域。(2)当UPSEL[3:0]=4'b0001,4'b0011,4'b0100和4'b0101时,可以有多个并发更新源。例如,通过Master_TIMER(UPBMT=1)和DMA模式进行更新。</td></tr><tr><td>27</td><td>SHWEN</td><td>影子寄存器使能0:影子寄存器禁能1:影子寄存器使能</td></tr><tr><td>26:25</td><td>DACTRGS[1:0]</td><td>DAC触发源发生更新事件时,定时器生成DAC触发事件。该位域用于配置哪个触发源生成DAC触发事件。00:不生成DAC触发事件01:在SHRTIMER_DACTRIG0上生成DAC触发事件10:在SHRTIMER_DACTRIG1上生成DAC触发事件11:在SHRTIMER_DACTRIG2上生成DAC触发事件</td></tr><tr><td>24</td><td>UPBMT</td><td>通过Master_TIMER更新事件进行更新该位置1时,Slave_TIMERx(x=0..4)更新事件与Master_TIMER更新事件同步,且它们的有效寄存器由Master_TIMER更新事件进行更新。0:有效寄存器不由Master_TIMER更新。1:有效寄存器由Master_TIMER更新。</td></tr><tr><td>23</td><td>UPBST4</td><td>通过Slave_TIMER4更新事件进行更新该位置1时,Slave_TIMERx(x=0..3)更新事件与Slave_TIMER4更新事件同步,且它们的有效寄存器由Slave_TIMER4更新事件进行更新。0:有效寄存器不由Slave_TIMER4更新。1:有效寄存器由Slave_TIMER4更新。注意:Slave_TIMER4的寄存器中不存在此位。</td></tr><tr><td>22</td><td>UPBST3</td><td>通过Slave_TIMER3更新事件进行更新该位置1时,Slave_TIMERx(x=0,1,2,4)更新事件与Slave_TIMER3更新事件同步,且它们的有效寄存器由Slave_TIMER3更新事件进行更新。0:有效寄存器不由Slave_TIMER3更新。1:有效寄存器由Slave_TIMER3更新。注意:Slave_TIMER3的寄存器中不存在此位。</td></tr><tr><td>21</td><td>UPBST2</td><td>通过Slave_TIMER2更新事件进行更新该位置1时,Slave_TIMERx(x=0,1,3,4)更新事件与Slave_TIMER2更新事件同步,且它们的有效寄存器由Slave_TIMER2更新事件进行更新。0:有效寄存器不由 Slave_TIMER2 更新。1:有效寄存器由 Slave_TIMER2 更新。注意:Slave_TIMER2 的寄存器中不存在此位。</td></tr><tr><td>20</td><td>UPBST1</td><td>通过 Slave_TIMER1 更新事件进行更新该位置 1 时,Slave_TIMERx(x=0,2,3,4)更新事件与 Slave_TIMER1 更新事件同步,且它们的有效寄存器由 Slave_TIMER1 更新事件进行更新。0:有效寄存器不由 Slave_TIMER1 更新。1:有效寄存器由 Slave_TIMER1 更新。注意:Slave_TIMER1 的寄存器中不存在此位。</td></tr><tr><td>19</td><td>UPBST0</td><td>通过 Slave_TIMER0 更新事件进行更新该位置 1 时,Slave_TIMERx(x=0,2,3,4)更新事件与 Slave_TIMER0 更新事件同步,且它们的有效寄存器由 Slave_TIMER0 更新事件进行更新。0:有效寄存器不由 Slave_TIMER0 更新。1:有效寄存器由 Slave_TIMER0 更新。注意:Slave_TIMER0 的寄存器中不存在此位。</td></tr><tr><td>18</td><td>UPRST</td><td>更新事件由复位事件生成该位用于使能计数器复位事件或翻转事件生成更新事件。0:复位事件或翻转事件生成更新事件禁能1:复位事件或翻转事件生成更新事件使能</td></tr><tr><td>17</td><td>UPREP</td><td>更新事件由重复事件生成该位用于使能重复事件生成更新事件。0:重复事件生成更新事件禁能1:重复事件生成更新事件使能</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:14</td><td>DELCMP3M[1:0]</td><td>比较 3 延迟模式00:比较 3 延迟模式禁能。只要计数器值等于比较 3 有效寄存器值,就会发生比较匹配。01:比较 3 延迟模式 0。捕获 1 事件后,比较 3 的重新计算值为:(比较 3 有效寄存器值+捕获 1 值)。一旦计数器等于重新计算的值,就会发生比较匹配。10:比较 3 延迟模式 1。在捕获 1 事件或比较 0 事件之后,比较 3 的重新计算值是:(比较 3 有效寄存器值+捕获 1 值,或者比较 3 有效寄存器值+比较 0 值)。一旦计数器等于重新计算的值,就会发生比较匹配。11:比较 3 延迟模式 2。在捕获 1 事件或比较 2 事件之后,比较 3 的重新计算值为:(比较 3 有效寄存器值+捕获 1 的值,或比较 3 有效寄存器值+比较 2 的值)。一旦计数器等于重新计算的值,就会发生比较匹配。注意:一旦使能计数器(SHRTIMER_MTCTL0 寄存器中的 STxCEN=1),就不得修改此位域。</td></tr><tr><td>13:12</td><td>DELCMP1M[1:0]</td><td>比较 1 延迟模式00:比较 1 延迟模式禁能。只要计数器值等于比较 1 有效寄存器值,就会发生比较匹配。01:比较 1 延迟模式 0。捕获 0 事件后,比较 1 的重新计算值为:(比较 1 有效寄存器值+捕获0值)。一旦计数器等于重新计算的值,就会发生比较匹配。10:比较1延迟模式1。在捕获0事件或比较0事件之后,比较1的重新计算值是:(比较1有效寄存器值+捕获0值,或者比较1有效寄存器值+比较0值)。一旦计数器等于重新计算的值,就会发生比较匹配。11:比较1延迟模式2。在捕获0事件或比较2事件之后,比较1的重新计算值为:(比较1有效寄存器值+捕获0的值,或比较1有效寄存器值+比较2的值)。一旦计数器等于重新计算的值,就会发生比较匹配。注意:一旦使能计数器(SHRTIMER_MTCTL0寄存器中的STxCEN=1),就不得修改此位域。</td></tr><tr><td>11</td><td>SYNISTRT</td><td>同步输入启动计数器该位用于配置同步输入启动计数器。0:同步输入不能启动计数器。1:同步输入可以启动计数器。</td></tr><tr><td>10</td><td>SYNIRST</td><td>同步输入复位计数器该位用于配置同步输入复位计数器。0:同步输入不能复位计数器。1:同步输入可以复位计数器。</td></tr><tr><td>9:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>BLNMEN</td><td>均衡模式使能0:均衡模式禁能1:均衡模式使能注意:一旦使能计数器(SHRTIMER_MTCTL0寄存器中的STxCEN=1),就不得修改此位域。</td></tr><tr><td>5</td><td>HALFM</td><td>半波模式该位置1时,SHRTIMER_STxCMP0V有效寄存器始终是计数器自动重载值(SHRTIMER_STxCAR)的一半。0:半波模式禁能。1:半波模式使能。</td></tr><tr><td>4</td><td>CNTRSTM</td><td>计数器复位模式该位用于定义单脉冲模式下定时器计数器的行为。0:计数器只能计数到周期值后才能复位1:可以随时复位计数器(运行或停止)。</td></tr><tr><td>3</td><td>CTNM</td><td>连续模式。0:单脉冲模式。当计数器达到SHRTIMER_STxCAR值时,它将由硬件停止。1:连续模式。计数器在达到SHRTIMER_STxCAR值时,翻转到0并连续计数。</td></tr><tr><td>2:0</td><td>CNTCKDIV[2:0]</td><td>计数器时钟分频该位域可以由软件配置,确定超高分辨率时钟(SHRTIMER_HPCK)和计数器时钟(SHRTIMER_PSCCK)的分频比。当SHRTIMER_MTACTL中的CNTCKDIV[3]为0时,<eq>f_{SHRTIMER\_PSCCK} = f_{SHRTIMER\_HPCK}/2^{CNTCKDIV[2:0]+1}</eq>。</td></tr></table>

当 SHRTIMER_MTACTL 中的 CNTCKDIV [3]位为 1，且 CNTCKDIV[2:0]配置为 3'b000 时： $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}$ 0000: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 2$ 0001: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 4$ 0010: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 8$ 0011: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 16$ 0100: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 32$ 0101: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 64$ 0110: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 128$ 0111: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK} / 256$ 1000: $f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}$ 其他值保留。

注意：一旦使能定时器（SHRTIMER_MTCTL0 寄存器中的 STxCEN = 1），就不能修改 CNTCKDIV [3:0]位域。

## Slave_TIMERx 中断标志寄存器 (SHRTIMER_STxINTF)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>CH1F</td><td>CH0F</td><td colspan="2">保留</td><td>BLNIF</td><td>CBLNF</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>DLYIIF</td><td>RSTIF</td><td>CH1ONAIF</td><td>CH1OAIF</td><td>CH0ONAIF</td><td>CH0OAIF</td><td>CAP1IF</td><td>CAP0IF</td><td>UPIF</td><td>保留</td><td>REPIF</td><td>CMP3IF</td><td>CMP2IF</td><td>CMP1IF</td><td>CMP0IF</td></tr><tr><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21</td><td>CH1F</td><td>通道1输出标志该位用于指示通道1的输出电平状态。0:通道1输出无效电平。1:通道1输出有效电平。</td></tr><tr><td>20</td><td>CH0F</td><td>通道0输出标志该位用于指示通道0的输出电平状态。0:通道0输出无效电平。1:通道0输出有效电平。</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>BLNIF</td><td>均衡空闲标志该位用于指示在进入均衡空闲状态时,哪个通道正在输出信号。0:当进入均衡空闲模式时,通道0输出CHOPRE信号,而通道1输出无效电平。1:当进入均衡空闲模式时,通道1输出CH1OPRE信号,而通道0输出无效电平。</td></tr><tr><td>16</td><td>CBLNF</td><td>当前的均衡状态标志该位仅在均衡模式下有效。该位用于指示当前正在输出信号的通道。0:通道0输出CHOPRE信号,通道1输出无效电平。1:通道1输出CH1OPRE信号,通道0输出无效电平。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>DLYIIF</td><td>延迟空闲模式进入中断标志进入延迟空闲或均衡空闲模式时,此标志由硬件置位。0:延迟空闲模式进入中断未发生1:延迟空闲模式进入中断发生</td></tr><tr><td>13</td><td>RSTIF</td><td>计数器复位中断标志计数器复位或翻转事件发生时,此标志由硬件置位。0:计数器复位或翻转事件中断未发生1:计数器复位或翻转事件中断发生</td></tr><tr><td>12</td><td>CH1ONAIF</td><td>通道1输出无效中断标志请参阅CH0ONAIF说明。</td></tr><tr><td>11</td><td>CH1OAIF</td><td>通道1输出有效中断标志请参阅CH0OAIF说明。</td></tr><tr><td>10</td><td>CH0ONAIF</td><td>通道0输出无效中断标志当通道0输出无效(COPRE从有效变为无效)发生时,该标志由硬件置位。0:通道0输出无效中断未发生1:通道0输出无效中断发生</td></tr><tr><td>9</td><td>CH0OAIF</td><td>通道0输出有效中断标志当通道0输出有效(COPRE从无效变为有效)发生时,该标志由硬件置位。0:通道0输出有效中断未发生1:通道0输出有效中断发生</td></tr><tr><td>8</td><td>CAP1IF</td><td>捕获1中断标志当捕获1事件发生,该标志由硬件置位。0:捕获1中断未发生1:捕获1中断发生</td></tr><tr><td>7</td><td>CAP0IF</td><td>捕获0中断标志当捕获0事件发生,该标志由硬件置位。0:捕获0中断未发生1:捕获0中断发生</td></tr><tr><td>6</td><td>UPIF</td><td>更新中断标志当更新事件发生,该标志由硬件置位。0:更新中断未发生</td></tr></table>

<table><tr><td></td><td></td><td>1: 更新中断发生</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4</td><td>REPIF</td><td>重复中断标志当重复事件发生时,此标志由硬件置位。0: 重复中断未发生1: 重复中断发生</td></tr><tr><td>3</td><td>CMP3IF</td><td>比较3中断标志当比较3事件发生,该标志由硬件置位。0: 比较3中断未发生1: 比较3中断发生</td></tr><tr><td>2</td><td>CMP2IF</td><td>比较2中断标志当比较2事件发生,该标志由硬件置位。0: 比较2中断未发生1: 比较2中断发生</td></tr><tr><td>1</td><td>CMP1IF</td><td>比较1中断标志当比较1事件发生,该标志由硬件置位。0: 比较1中断未发生1: 比较1中断发生</td></tr><tr><td>0</td><td>CMP0IF</td><td>比较0中断标志当比较2事件发生,该标志由硬件置位。0: 比较0中断未发生1: 比较0中断发生</td></tr></table>

## Slave_TIMERx 中断标志清除寄存器 (SHRTIMER_STxINTC)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>DLYIIFC</td><td>RSTIFC</td><td>CH1ONAIFC</td><td>CH1OAIFC</td><td>CH0ONAIFC</td><td>CH0OAIFC</td><td>CAP1IFC</td><td>CAP0IFC</td><td>UPIFC</td><td>保留</td><td>REPIFC</td><td>CMP3IFC</td><td>CMP2IFC</td><td>CMP1IFC</td><td>CMP0IFC</td></tr><tr><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>DLYIIFC</td><td>延迟空闲模式进入中断标志清除0:无效1: 清除延迟空闲模式进入中断标志(SHRTIMER_STxINTF 寄存器中的 DLYIIF 位)</td></tr><tr><td>13</td><td>RSTIFC</td><td>计数器复位中断标志清除0: 无效1: 清除计数器复位中断标志(SHRTIMER_STxINTF 寄存器中的 RSTIF 位)</td></tr><tr><td>12</td><td>CH1ONAIFC</td><td>通道 1 输出无效中断标志清除清除 SHRTIMER_STxINTF 寄存器中的 CH1ONAIF 位请参考 CH0ONAIFC 的描述</td></tr><tr><td>11</td><td>CH1OAIFC</td><td>通道 1 输出有效中断标志清除清除 SHRTIMER_STxINTF 寄存器中的 CH1OAIF 位请参考 CH0OAIFC 的描述</td></tr><tr><td>10</td><td>CH0ONAIFC</td><td>通道 0 输出无效中断标志清除0: 无效1: 清除通道 0 输出无效中断标志(SHRTIMER_STxINTF 寄存器中的 CH0ONAIF 位)</td></tr><tr><td>9</td><td>CH0OAIFC</td><td>通道 0 输出有效中断标志清除0: 无效1: 清除通道 0 输出有效中断标志(SHRTIMER_STxINTF 寄存器中的 CH0OAIF 位)</td></tr><tr><td>8</td><td>CAP1IFC</td><td>比较 1 捕获中断标志清除0: 无效1: 清除比较 1 捕获中断标志(SHRTIMER_STxINTF 寄存器中的 CAP1IF 位)</td></tr><tr><td>7</td><td>CAP0IFC</td><td>比较 0 捕获中断标志清除0: 无效1: 清除比较 0 捕获中断标志(SHRTIMER_STxINTF 寄存器中的 CAP0IF 位)</td></tr><tr><td>6</td><td>UPIFC</td><td>更新中断标志清除0: 无效1: 清除更新中断标志(SHRTIMER_STxINTF 寄存器中的 UPIF 位)</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4</td><td>REPIFC</td><td>重复中断标志清除0: 无效1: 清除重复中断标志(SHRTIMER_STxINTF 寄存器中的 REPIF 位)</td></tr><tr><td>3</td><td>CMP3IFC</td><td>比较 3 中断标志清除0: 无效1: 清除比较 3 中断标志(SHRTIMER_STxINTF 寄存器中的 CMP3IF 位)</td></tr><tr><td>2</td><td>CMP2IFC</td><td>比较 2 中断标志清除0: 无效1: 清除比较 2 中断标志(SHRTIMER_STxINTF 寄存器中的 CMP2IF 位)</td></tr><tr><td>1</td><td>CMP1IFC</td><td>比较 1 中断标志清除0: 无效</td></tr></table>

1：清除比较 1 中断标志（SHRTIMER_STxINTF 寄存器中的 CMP1IF 位）

0 CMP0IFC 比较 0 中断标志清除

0：无效

1：清除比较 0 中断标志（SHRTIMER_STxINTF 寄存器中的 CMP0IF 位）

## Slave_TIMERx DMA 和中断使能寄存器 (SHRTIMER_STxDMAINTEN)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>DLYIDEN</td><td>RSTDEN</td><td>CH1ONADEN</td><td>CH1OADEN</td><td>CH0ONADEN</td><td>CH0OADEN</td><td>CAP1DEN</td><td>CAP0DEN</td><td>UPDEN</td><td>保留</td><td>REPDEN</td><td>CMP3DEN</td><td>CMP2DEN</td><td>CMP1DEN</td><td>CMP0DEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>DLYIIE</td><td>RSTIE</td><td>CH1ONAIE</td><td>CH1OAIE</td><td>CH0ONAIE</td><td>CH0OAIE</td><td>CAP1IE</td><td>CAP0IE</td><td>UPIE</td><td>保留</td><td>REPIE</td><td>CMP3IE</td><td>CMP2IE</td><td>CMP1IE</td><td>CMP0IE</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>DLYIDEN</td><td>延迟空闲模式进入DMA请求使能0:禁能1:使能</td></tr><tr><td>29</td><td>RSTDEN</td><td>计数器复位DMA请求使能0:禁能1:使能</td></tr><tr><td>28</td><td>CH1ONADEN</td><td>通道1输出无效DMA请求使能请参考CH0ONADEN位描述。</td></tr><tr><td>27</td><td>CH1OADEN</td><td>通道1输出有效DMA请求使能请参考CH0OADEN位描述。</td></tr><tr><td>26</td><td>CH0ONADEN</td><td>通道0输出无效DMA请求使能0:禁能1:使能</td></tr><tr><td>25</td><td>CH0OADEN</td><td>通道0输出有效DMA请求使能0:禁能1:使能</td></tr><tr><td>24</td><td>CAP1DEN</td><td>捕获1DMA请求使能0:禁能</td></tr></table>

<table><tr><td>23</td><td>CAP0DEN</td><td>捕获0 DMA请求使能0:禁能1:使能</td></tr><tr><td>22</td><td>UPDEN</td><td>更新DMA请求使能0:禁能1:使能</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>REPDEN</td><td>重复DMA请求使能0:禁能1:使能</td></tr><tr><td>19</td><td>CMP3DEN</td><td>比较3 DMA请求使能0:禁能1:使能</td></tr><tr><td>18</td><td>CMP2DEN</td><td>比较2 DMA请求使能0:禁能1:使能</td></tr><tr><td>17</td><td>CMP1DEN</td><td>比较1 DMA请求使能0:禁能1:使能</td></tr><tr><td>16</td><td>CMP0DEN</td><td>比较0 DMA请求使能0:禁能1:使能</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>DLYIIE</td><td>延迟空闲模式进入中断使能0:禁能1:使能</td></tr><tr><td>13</td><td>RSTIE</td><td>计数器复位中断使能0:禁能1:使能</td></tr><tr><td>12</td><td>CH1ONAIE</td><td>通道1输出无效中断使能请参考CH0ONAIE位描述。</td></tr><tr><td>11</td><td>CH1OAIE</td><td>通道1输出有效中断使能请参考CH0OAIE位描述。</td></tr><tr><td>10</td><td>CH0ONAIE</td><td>通道0输出无效中断使能0:禁能1:使能</td></tr><tr><td>9</td><td>CH0OAIE</td><td>通道0输出有效中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>8</td><td>CAP1IE</td><td>捕获1中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>7</td><td>CAP0IE</td><td>捕获0中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>6</td><td>UPIE</td><td>更新中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4</td><td>REPIE</td><td>重复中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>3</td><td>CMP3IE</td><td>比较3中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>2</td><td>CMP2IE</td><td>比较2中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>1</td><td>CMP1IE</td><td>比较1中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr><tr><td>0</td><td>CMP0IE</td><td>比较0中断使能</td></tr><tr><td></td><td></td><td>0:禁能</td></tr><tr><td></td><td></td><td>1:使能</td></tr></table>

## Slave_TIMERx 计数器寄存器 (SHRTIMER_STxCNT)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>该位域用于配置当前计数器值。对该位域进行写操作可以更改计数器的值。仅当 Slave_TIMERx 停止(SHRTIMER_STxCTL0 寄存器中的 STxCEN = 0)时,才能对其进行写操作,更改计数器的值。注意:(1)计数器时钟分频系数小于 64(CNTCKDIV [3:0] &lt; 5)时,计数器的最低有效位无效,它们不能被写入,读出值为 0。(2)如果写入该位域的值高于 SHRTIMER_MPER 寄存器值,则定时器的行为是不可预测的。</td></tr></table>

## Slave_TIMERx 计数器自动重载寄存器 (SHRTIMER_STxCAR)

地址偏移：0x14

复位值：0x0000 FFDF

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值该位域定义计数器的自动重载值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于(3*tSHRTIMER_CK)。例如:当CNTCKDIV [3:0]=4&#x27;b0000时,CARL [15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV [3:0]=4&#x27;b0000时,CARL [15:0] &lt;= 0xFFDF。</td></tr></table>

## Slave_TIMERx 重复计数寄存器 (SHRTIMER_STxCREP)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>CREP[7:0]</td><td>重复计数器值该位域用于定义重复事件的发生率。当重复计数器递减计数到零时,连续模式下即将发生的翻转事件或复位事件将产生一个重复事件。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。</td></tr></table>

## Slave_TIMERx 比较 0 寄存器 (SHRTIMER_STxCMP0V)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP0VAL[15:0]</td><td>比较0值该位域包含要与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于3个<eq>t_{SHRTIMER\_CK}</eq>。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&lt;=0xFFDF。</td></tr></table>

## Slave_TIMERx 比较 0 复合寄存器 (SHRTIMER_STxCMP0CP)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">CREP[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>CREP[7:0]</td><td>计数器重复值该位域是SHRTIMER_STxCREP寄存器中CREP[7:0]的别名。</td></tr><tr><td>15:0</td><td>CMP0VAL[15:0]</td><td>比较0值该位域是SHRTIMER_STxCMP0V寄存器中CMP0VAL[15:0]的别名。</td></tr></table>

## Slave_TIMERx 比较 1 寄存器 (SHRTIMER_STxCMP1V)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP1VAL[15:0]</td><td>比较1值该位域包含要与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。延迟模式中,有效寄存器的值会重新进行计算。注意:(1)最小值必须大于或等于3个<eq>t_{SHRTIMER\_CK}</eq>。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&lt;=0xFFDF。</td></tr></table>

## Slave_TIMERx 比较 2 寄存器 (SHRTIMER_STxCMP2V)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP2VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP2VAL[15:0]</td><td>比较2值该位域包含要与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。注意:(1)最小值必须大于或等于3个<eq>t_{SHRTIMER\_CK}</eq>。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&gt; = 0x60。(2)最大值必须小于或等于(0xFFFF - 1*tSHRTIMER_CK)。例如:当CNTCKDIV[3:0]=4&#x27;b0000时,CARL[15:0]&lt;=0xFFDF。</td></tr></table>

## Slave_TIMERx 比较 3 寄存器 (SHRTIMER_STxCMP3V)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMP3VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CMP3VAL[15:0]</td><td>比较3值该位域包含要与计数器进行比较的值。该寄存器具有影子寄存器。如果影子寄存器被禁能(SHWEN=0),它将保存有效寄存器的内容;否则,它将保存影子寄存器的内容。</td></tr></table>

延迟模式中，有效寄存器的值会重新进行计算。

注意：

（1）最小值必须大于或等于 3 个 t<sub>SHRTIMER_CK</sub>。例如：当 CNTCKDIV [3:0] = 4’b0000时，CARL [15:0] > = 0x60。

（2）最大值必须小于或等于（0xFFFF –1*t<sub>SHRTIMER_CK</sub>）。例如：当 CNTCKDIV [3:0]= 4’b0000 时，CARL [15:0] <= 0xFFDF。

## Slave_TIMERx 捕获 0 寄存器 (SHRTIMER_STxCAP0V)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CAP0VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CAP0VAL[15:0]</td><td>捕获0值该位域保持上一个捕获事件发生时的计数器值,且该位域只读。注意:计数器时钟分频系数小于64(CNTCKDIV [3:0]&lt;5)时,计数器的最低有效位无效,它们不能被写入,读出值为0。</td></tr></table>

## Slave_TIMERx 捕获 1 寄存器 (SHRTIMER_STxCAP1V)

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CAP1VAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CAP1VAL[15:0]</td><td>捕获1值该位域保持上一个捕获事件发生时的计数器值,且该位域只读。</td></tr></table>

注意：计数器时钟分频系数小于 64（CNTCKDIV [3:0] <5）时，计数器的最低有效位无效，它们不能被写入，读出值为 0。

## Slave_TIMERx 死区控制寄存器 (SHRTIMER_STxDTCTL)

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DTFSVPROT</td><td>DTFSPROT</td><td colspan="4">保留</td><td>DTFS</td><td colspan="9">DTFCFG[8:0]</td></tr><tr><td>rwo</td><td>rwo</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DTRSVPROT</td><td>DTRSPROT</td><td colspan="4">DTGCKDIV[3:0]</td><td>DTRS</td><td colspan="9">DTRCFG[8:0]</td></tr><tr><td>rwo</td><td>rwo</td><td colspan="4">rw</td><td>rw</td><td colspan="9">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DTFSVPROT</td><td>死区下降沿(值和符号)保护该位域用于死区下降沿(值和符号)的写保护。0:保护禁能。DTFS位和DTFCFG[15:0]位域是可写的。1:保护使能。DTFS位和DTFCFG[15:0]位域是只读的。注意:(1)DTFCFG[15:9]位域在SHRTIMER_STxACTL寄存器中。(2)该位不进行预装载。</td></tr><tr><td>30</td><td>DTFSPROT</td><td>死区下降沿(符号)保护该位域用于死区下降沿(符号)的写保护。0:保护禁能。SHRTIMER_STxDTCTL寄存器中的DTFS位是可写的。1:保护使能。SHRTIMER_STxDTCTL寄存器中的DTFS位是只读的。注意:(1)该位不进行预装载。</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>25</td><td>DTFS</td><td>死区下降沿值的符号0:死区下降沿值的符号为正。1:死区下降沿值的符号为负。注意:当SHRTIMER_STxDTCTL寄存器中的DTFSPROT位或DTFSVPROT位置1时,无法修改此位。</td></tr><tr><td>24:16</td><td>DTFCFG[8:0]</td><td>死区下降沿值该位域用于配置跟随输出准备信号(OyPRE,y=0,1)下降沿之后的死区时间值。DTF值 = DTFCFG[15:0] x tSHRTIMER_DTGCK,其中,tSHRTIMER_DTGCK = 1/fSHRTIMER_DTGCK。写入该位域可以更改DTFCFG[15:0]位域的低9位。</td></tr></table>

注意：
（1）DTFCFG [15:9] 位域在 SHRTIMER_STxACTL 寄存器中。
（2）当 SHRTIMER_STxDTCTL 寄存器中的 DTFSVPROT 位置 1 时，无法修改此位域。

15 DTRSVPROT 死区上升沿（值和符号）保护
该位域用于死区上升沿（值和符号）的写保护。
0：保护禁能。DTRS 位和 DTRCFG [15:0] 位域是可写的。
1：保护使能。DTRS 位和 DTRCFG [15:0] 位域是只读的。
注意：
（1）DTRCFG [15:9] 位域在 SHRTIMER_STxACTL 寄存器中。
（2）该位不进行预装载。

14 DTRSPROT 死区上升沿（符号）保护
该位域用于死区上升沿（符号）的写保护。
0：保护禁能。SHRTIMER_STxDTCTL 寄存器中的 DTRS 位是可写的。
1：保护使能。SHRTIMER_STxDTCTL 寄存器中的 DTRS 位是只读的。
注意：
（1）该位不进行预装载。

13:10 DTGCKDIV[2:0] 死区时间发生器时钟分频
该位域可以通过软件配置，用于确定 SHRTIMER 时钟（SHRTIMER_CK）和死区时间发生器时钟（SHRTIMER_DTGCK）的分频系数。
DTGCKDIV[3] = 0 时， $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 2^{DTGCKDIV[2:0]}$ 。
DTGCKDIV[3] = 1 时， $f_{\text{SHRTIMER\_DTGCK}} = 2^{(DTGCKDIV[2:0]+4) * f_{\text{SHRTIMER\_CK}}}$ 。
0000： $f_{\text{SHRTIMER\_DTGCK}} = 8 * f_{\text{SHRTIMER\_CK}}$ 0001： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 2$ 0010： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 4$ 0011： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 8$ 0100： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 16$ 0101： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 32$ 0110： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 64$ 0111： $f_{\text{SHRTIMER\_DTGCK}} = (8 * f_{\text{SHRTIMER\_CK}}) / 128$ 1000： $f_{\text{SHRTIMER\_DTGCK}} = 16 * f_{\text{SHRTIMER\_CK}}$ 1001： $f_{\text{SHRTIMER\_DTGCK}} = 32 * f_{\text{SHRTIMER\_CK}}$ 1010： $f_{\text{SHRTIMER\_DTGCK}} = 64 * f_{\text{SHRTIMER\_CK}}$ 其他位保留。
注意：如果任何一个保护位（DTFSPROT，DTFSVPROT，DTRS PROT 和 DTRS VPROT）置位，则不能修改此位域。

9 DTRS 死区上升沿值的符号
0：死区上升沿值的符号为正。
1：死区上升沿值的符号为负。
注意：当 SHRTIMER_STxDTCTL 寄存器中的 DTRS PROT 位或 DTRS VPROT 位置 1 时，无法修改此位。

8:0 DTRCFG[8:0] 死区上升沿值

该位域用于配置跟随输出准备信号（OyPRE，y = 0,1）上升沿之后的死区时间值。DTR 值 = DTRCFG[15:0] x t<sub>SHRTIMER_DTGCK</sub> ， 其 中 ， t<sub>SHRTIMER_DTGCK</sub> = 1/f<sub>SHRTIMER_DTGCK</sub>。

写入该位域可以更改 DTRCFG[15:0]位域的低 9 位。

注意：

（1）DTRCFG [15:9]位域在 SHRTIMER_STxACTL 寄存器中。

（2）当 SHRTIMER_STxDTCTL 寄存器中的 DTRSVPROT 位置 1 时，无法修改此位域。

## Slave_TIMERx 通道 0 置位请求寄存器 (SHRTIMER_STxCH0SET)

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH0SUP</td><td>CH0SEXEV9</td><td>CH0SEXEV8</td><td>CH0SEXEV7</td><td>CH0SEXEV6</td><td>CH0SEXEV5</td><td>CH0SEXEV4</td><td>CH0SEXEV3</td><td>CH0SEXEV2</td><td>CH0SEXEV1</td><td>CH0SEXEV0</td><td>CH0SSTEV8</td><td>CH0SSTEV7</td><td>CH0SSTEV6</td><td>CH0SSTEV5</td><td>CH0SSTEV4</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH0SSTEV3</td><td>CH0SSTEV2</td><td>CH0SSTEV1</td><td>CH0SSTEV0</td><td>CH0SMTCMP3</td><td>CH0SMTCMP2</td><td>CH0SMTCMP1</td><td>CH0SMTCMP0</td><td>CH0SMTPER</td><td>CH0SCMP3</td><td>CH0SCMP2</td><td>CH0SCMP1</td><td>CH0SCMP0</td><td>CH0SPER</td><td>CH0SRT</td><td>CH0SSEV</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH0SUP</td><td>更新事件生成通道0置位请求该位置1时,更新事件可以产生置位请求。0:更新事件不生成置位请求。1:更新事件生成置位请求。</td></tr><tr><td>30</td><td>CHOSEXEV9</td><td>外部事件9生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>29</td><td>CHOSEXEV8</td><td>外部事件8生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>28</td><td>CHOSEXEV7</td><td>外部事件7生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>27</td><td>CHOSEXEV6</td><td>外部事件6生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>26</td><td>CHOSEXEV5</td><td>外部事件5生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>25</td><td>CHOSEXEV4</td><td>外部事件4生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>24</td><td>CH0SEXEV3</td><td>外部事件3生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>23</td><td>CH0SEXEV2</td><td>外部事件2生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>22</td><td>CH0SEXEV1</td><td>外部事件1生成通道0置位请求请参考CHOSEXEV0说明。</td></tr><tr><td>21</td><td>CH0SEXEV0</td><td>外部事件0生成通道0置位请求该位置1时,外部事件0可以产生置位请求。0:该事件不生成置位请求。1:该事件生成置位请求。</td></tr><tr><td>20</td><td>CH0SSTEV8</td><td>Slave_TIMERx互连事件8生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>19</td><td>CH0SSTEV7</td><td>Slave_TIMERx互连事件7生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>18</td><td>CH0SSTEV6</td><td>Slave_TIMERx互连事件6生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>17</td><td>CH0SSTEV5</td><td>Slave_TIMERx互连事件5生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>16</td><td>CH0SSTEV4</td><td>Slave_TIMERx互连事件4生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>15</td><td>CH0SSTEV3</td><td>Slave_TIMERx互连事件3生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>14</td><td>CH0SSTEV2</td><td>Slave_TIMERx互连事件2生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>13</td><td>CH0SSTEV1</td><td>Slave_TIMERx互连事件1生成通道0置位请求请参考CH0SSTEV0说明。</td></tr><tr><td>12</td><td>CH0SSTEV0</td><td>Slave_TIMERx互连事件0生成通道0置位请求该位置1时,Slave_TIMERx互连事件0可以产生置位请求。具体请参考表19-5.Slave_TIMER内部连接事件。0:该事件不生成置位请求。1:该事件生成置位请求。</td></tr><tr><td>11</td><td>CH0SMTCMP3</td><td>Master_TIMER比较3事件生成通道0置位请求该位置1时,Master_TIMER比较3事件可以产生置位请求。0:Master_TIMER比较3事件不生成置位请求。1:Master_TIMER比较3事件生成置位请求。</td></tr><tr><td>10</td><td>CH0SMTCMP2</td><td>Master_TIMER比较2事件生成通道0置位请求该位置1时,Master_TIMER比较2事件可以产生置位请求。0: Master_TIMER 比较 2 事件不生成置位请求。1: Master_TIMER 比较 2 事件生成置位请求。</td></tr><tr><td>9</td><td>CHOSMTCMP1</td><td>Master_TIMER 比较 1 事件生成通道 0 置位请求该位置 1 时,Master_TIMER 比较 1 事件可以产生置位请求。0: Master_TIMER 比较 1 事件不生成置位请求。1: Master_TIMER 比较 1 事件生成置位请求。</td></tr><tr><td>8</td><td>CHOSMTCMP0</td><td>Master_TIMER 比较 0 事件生成通道 0 置位请求该位置 1 时,Master_TIMER 比较 0 事件可以产生置位请求。0: Master_TIMER 比较 0 事件不生成置位请求。1: Master_TIMER 比较 0 事件生成置位请求。</td></tr><tr><td>7</td><td>CHOSMTPER</td><td>Master_TIMER 周期事件生成通道 0 置位请求连续模式下,Master_TIMER 计数器的翻转事件可以产生置位请求。在单脉冲模式下,Master_TIMER 计数器的复位事件可以产生置位请求。0: 该事件不生成置位请求。1: 该事件生成置位请求。</td></tr><tr><td>6</td><td>CHOSCMP3</td><td>Slave_TIMERx 比较 3 事件生成通道 0 置位请求该位置 1 时,Slave_TIMERx 比较 3 事件可以产生置位请求。0: Slave_TIMERx 比较 3 事件不生成置位请求。1: Slave_TIMERx 比较 3 事件生成置位请求。</td></tr><tr><td>5</td><td>CHOSCMP2</td><td>Slave_TIMERx 比较 2 事件生成通道 0 置位请求该位置 1 时,Slave_TIMERx 比较 2 事件可以产生置位请求。0: Slave_TIMERx 比较 2 事件不生成置位请求。1: Slave_TIMERx 比较 2 事件生成置位请求。</td></tr><tr><td>4</td><td>CHOSCMP1</td><td>Slave_TIMERx 比较 1 事件生成通道 0 置位请求该位置 1 时,Slave_TIMERx 比较 1 事件可以产生置位请求。0: Slave_TIMERx 比较 1 事件不生成置位请求。1: Slave_TIMERx 比较 1 事件以生成置位请求。</td></tr><tr><td>3</td><td>CHOSCMP0</td><td>Slave_TIMERx 比较 0 事件生成通道 0 置位请求该位置 1 时,Slave_TIMERx 比较 0 事件可以产生置位请求。0: Slave_TIMERx 比较 0 事件不生成置位请求。1: Slave_TIMERx 比较 0 事件生成置位请求。</td></tr><tr><td>2</td><td>CHOSPER</td><td>Slave_TIMERx 周期事件生成通道 0 置位请求该位置 1 时,Slave_TIMERx 周期事件可以产生置位请求。0: Slave_TIMERx 周期事件不生成置位请求。1: Slave_TIMERx 周期事件生成置位请求。</td></tr><tr><td>1</td><td>CHOSRST</td><td>Slave_TIMERx 复位事件生成通道 0 置位请求该位置 1 时,由软件和同步输入引起的 Slave_TIMERx 复位事件,生成通道 0 置位请求。0: 该事件不生成置位请求。1: 该事件生成置位请求。</td></tr></table>

<table><tr><td></td><td></td><td>注意:该位置1时,其他的定时器复位事件不会影响输出。</td></tr><tr><td>0</td><td>CHOSSEV</td><td>软件事件生成通道0置位请求</td></tr><tr><td></td><td></td><td>该位由软件置1,由硬件自动清除。该位置1时,生成通道0置位请求。</td></tr><tr><td></td><td></td><td>0:该事件不生成置位请求</td></tr><tr><td></td><td></td><td>1:该事件生成置位请求</td></tr><tr><td></td><td></td><td>注意:该位不进行预装载。</td></tr></table>

## Slave_TIMERx 通道 0 复位请求寄存器 (SHRTIMER_STxCH0RST)

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH0RSUP</td><td>CH0RSEXEV9</td><td>CH0RSEXEV8</td><td>CH0RSEXEV7</td><td>CH0RSEXEV6</td><td>CH0RSEXEV5</td><td>CH0RSEXEV4</td><td>CH0RSEXEV3</td><td>CH0RSEXEV2</td><td>CH0RSEXEV1</td><td>CH0RSEXEV0</td><td>CH0RSSTEV8</td><td>CH0RSSTEV7</td><td>CH0RSSTEV6</td><td>CH0RSSTEV5</td><td>CH0RSSTEV4</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH0RSSTEV3</td><td>CH0RSSTEV2</td><td>CH0RSSTEV1</td><td>CH0RSSTEV0</td><td>CH0RSMTCMP3</td><td>CH0RSMTCMP2</td><td>CH0RSMTCMP1</td><td>CH0RSMTCMP0</td><td>CH0RSMTPER</td><td>CH0RSCMP3</td><td>CH0RSCMP2</td><td>CH0RSCMP1</td><td>CH0RSCMP0</td><td>CH0RSPER</td><td>CH0RSRST</td><td>CH0RSSEV</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH0RSUP</td><td>更新事件生成通道0复位请求该位置1时,更新事件可以产生复位请求。0:更新事件不生成复位请求。1:更新事件生成复位请求。</td></tr><tr><td>30</td><td>CH0RSEXEV9</td><td>外部事件9生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>29</td><td>CH0RSEXEV8</td><td>外部事件8生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>28</td><td>CH0RSEXEV7</td><td>外部事件7生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>27</td><td>CH0RSEXEV6</td><td>外部事件6生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>26</td><td>CH0RSEXEV5</td><td>外部事件5生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>25</td><td>CH0RSEXEV4</td><td>外部事件4生成通道0复位请求请参考CH0RSEXEV0说明。</td></tr><tr><td>24</td><td>CH0RSEXEV3</td><td>外部事件3生成通道0复位请求请参考 CHORSEXEV0 说明。</td></tr><tr><td>23</td><td>CHORSEXEV2</td><td>外部事件 2 生成通道 0 复位请求请参考 CHORSEXEV0 说明。</td></tr><tr><td>22</td><td>CHORSEXEV1</td><td>外部事件 1 生成通道 0 复位请求请参考 CHORSEXEV0 说明。</td></tr><tr><td>21</td><td>CHORSEXEV0</td><td>外部事件 0 生成通道 0 复位请求当该位置 1 时,外部事件 0 可以产生复位请求。0:该事件不生成复位请求。1:该事件生成复位请求。</td></tr><tr><td>20</td><td>CHORSSTEV8</td><td>Slave_TIMERx 互连事件 8 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>19</td><td>CHORSSTEV7</td><td>Slave_TIMERx 互连事件 7 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>18</td><td>CHORSSTEV6</td><td>Slave_TIMERx 互连事件 6 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>17</td><td>CHORSSTEV5</td><td>Slave_TIMERx 互连事件 5 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>16</td><td>CHORSSTEV4</td><td>Slave_TIMERx 互连事件 4 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>15</td><td>CHORSSTEV3</td><td>Slave_TIMERx 互连事件 3 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>14</td><td>CHORSSTEV2</td><td>Slave_TIMERx 互连事件 2 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>13</td><td>CHORSSTEV1</td><td>Slave_TIMERx 互连事件 1 生成通道 0 复位请求请参考 CHORSSTEV0 说明。</td></tr><tr><td>12</td><td>CHORSSTEV0</td><td>Slave_TIMERx 互连事件 0 生成通道 0 复位请求该位置 1 时,Slave_TIMERx 互连事件 0 可以产生复位请求。具体请参考表19-5.Slave_TIMER 内部连接事件。0:该事件不生成复位请求。1:该事件生成复位请求。</td></tr><tr><td>11</td><td>CHORSMTCMP3</td><td>Master_TIMER 比较 3 事件生成通道 0 复位请求该位置 1 时,Master_TIMER 比较 3 事件可以产生复位请求。0:Master_TIMER 比较 3 事件不生成复位请求。1:Master_TIMER 比较 3 事件生成复位请求。</td></tr><tr><td>10</td><td>CHORSMTCMP2</td><td>Master_TIMER 比较 2 事件生成通道 0 复位请求该位置 1 时,Master_TIMER 比较 2 事件可以产生复位请求。0:Master_TIMER 比较 2 事件不生成复位请求。1: Master_TIMER 比较 2 事件生成复位请求。</td></tr><tr><td>9</td><td>CH0RSMTCMP1</td><td>Master_TIMER 比较 1 事件生成通道 0 复位请求该位置 1 时,Master_TIMER 比较 1 事件可以产生复位请求。0: Master_TIMER 比较 1 事件不生成复位请求。1: Master_TIMER 比较 1 事件生成复位请求。</td></tr><tr><td>8</td><td>CH0RSMTCMP0</td><td>Master_TIMER 比较 0 事件生成通道 0 复位请求该位置 1 时,Master_TIMER 比较 0 事件可以产生复位请求。0: Master_TIMER 比较 0 事件不生成复位请求。1: Master_TIMER 比较 0 事件生成复位请求。</td></tr><tr><td>7</td><td>CH0RSMTPER</td><td>Master_TIMER 周期事件生成通道 0 复位请求连续模式下,Master_TIMER 计数器翻转事件可以产生复位请求。在单脉冲模式下,Master_TIMER 计数器复位事件可以产生复位请求。0: 该事件不生成复位请求。1: 该事件生成复位请求。</td></tr><tr><td>6</td><td>CH0RSCMP3</td><td>Slave_TIMERx 比较 3 事件生成通道 0 复位请求该位置 1 时,Slave_TIMERx 比较 3 事件可以产生复位请求。0: Slave_TIMERx 比较 3 事件不生成复位请求。1: Slave_TIMERx 比较 3 事件生成复位请求。</td></tr><tr><td>5</td><td>CH0RSCMP2</td><td>Slave_TIMERx 比较 2 事件生成通道 0 复位请求该位置 1 时,Slave_TIMERx 比较 2 事件可以产生复位请求。0: Slave_TIMERx 比较 2 事件不生成复位请求。1: Slave_TIMERx 比较 2 事件生成复位请求。</td></tr><tr><td>4</td><td>CH0RSCMP1</td><td>Slave_TIMERx 比较 1 事件生成通道 0 复位请求该位置 1 时,Slave_TIMERx 比较 1 事件可以产生复位请求。0: Slave_TIMERx 比较 1 事件不生成复位请求。1: Slave_TIMERx 比较 1 事件生成复位请求。</td></tr><tr><td>3</td><td>CH0RSCMP0</td><td>Slave_TIMERx 比较 0 事件生成通道 0 复位请求该位置 1 时,Slave_TIMERx 比较 0 事件可以产生复位请求。0: Slave_TIMERx 比较 0 事件不生成复位请求。1: Slave_TIMERx 比较 0 事件生成复位请求。</td></tr><tr><td>2</td><td>CH0RSPER</td><td>Slave_TIMERx 周期事件生成通道 0 复位请求该位置 1 时,Slave_TIMERx 周期事件可以产生复位请求。0: Slave_TIMERx 周期事件不生成复位请求。1: Slave_TIMERx 周期事件生成复位请求。</td></tr><tr><td>1</td><td>CH0RSRST</td><td>Slave_TIMERx 复位事件生成通道 0 复位请求该位置 1 时,由软件和同步输入引起的 Slave_TIMERx 复位事件,生成通道 0 复位请求。0: 该事件不生成复位请求。1: 该事件生成复位请求。</td></tr></table>

<table><tr><td></td><td></td><td>注意:该位置1时,其他的定时器复位事件不会影响输出。</td></tr><tr><td>0</td><td>CH0RSSEV</td><td>软件事件生成通道0复位请求该位由软件置1,由硬件自动清除。该位置1时,生成通道0复位请求。0:该事件不生成复位请求1:该事件生成复位请求注意:该位不进行预装载。</td></tr></table>

## Slave_TIMERx 通道 1 置位请求寄存器 (SHRTIMER_STxCH1SET)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH1SUP</td><td>CH1SEXEV9</td><td>CH1SEXEV8</td><td>CH1SEXEV7</td><td>CH1SEXEV6</td><td>CH1SEXEV5</td><td>CH1SEXEV4</td><td>CH1SEXEV3</td><td>CH1SEXEV2</td><td>CH1SEXEV1</td><td>CH1SEXEV0</td><td>CH1SSTEV8</td><td>CH1SSTEV7</td><td>CH1SSTEV6</td><td>CH1SSTEV5</td><td>CH1SSTEV4</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH1SSTEV3</td><td>CH1SSTEV2</td><td>CH1SSTEV1</td><td>CH1SSTEV0</td><td>CH1SMTCMP3</td><td>CH1SMTCMP2</td><td>CH1SMTCMP1</td><td>CH1SMTCMP0</td><td>CH1SMTPER</td><td>CH1SCMP3</td><td>CH1SCMP2</td><td>CH1SCMP1</td><td>CH1SCMP0</td><td>CH1SPER</td><td>CH1SRT</td><td>CH1SSEV</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH1SUP</td><td>更新事件生成通道1置位请求该位置1时,更新事件可以产生置位请求。0:更新事件不生成置位请求。1:更新事件生成置位请求。</td></tr><tr><td>30</td><td>CH1SEXEV9</td><td>外部事件9生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>29</td><td>CH1SEXEV8</td><td>外部事件8生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>28</td><td>CH1SEXEV7</td><td>外部事件7生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>27</td><td>CH1SEXEV6</td><td>外部事件6生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>26</td><td>CH1SEXEV5</td><td>外部事件6生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>25</td><td>CH1SEXEV4</td><td>外部事件4生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>24</td><td>CH1SEXEV3</td><td>外部事件3生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>23</td><td>CH1SEXEV2</td><td>外部事件2生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>22</td><td>CH1SEXEV1</td><td>外部事件1生成通道1置位请求请参考CH1SEXEV0说明。</td></tr><tr><td>21</td><td>CH1SEXEV0</td><td>外部事件0生成通道1置位请求当该位置1时,外部事件1可以产生置位请求。0:该事件不生成置位请求。1:该事件生成置位请求。</td></tr><tr><td>20</td><td>CH1SSTEV8</td><td>Slave_TIMERx互连事件8生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>19</td><td>CH1SSTEV7</td><td>Slave_TIMERx互连事件7生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>18</td><td>CH1SSTEV6</td><td>Slave_TIMERx互连事件6生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>17</td><td>CH1SSTEV5</td><td>Slave_TIMERx互连事件5生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>16</td><td>CH1SSTEV4</td><td>Slave_TIMERx互连事件4生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>15</td><td>CH1SSTEV3</td><td>Slave_TIMERx互连事件3生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>14</td><td>CH1SSTEV2</td><td>Slave_TIMERx互连事件2生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>13</td><td>CH1SSTEV1</td><td>Slave_TIMERx互连事件1生成通道1置位请求请参考CH1SSTEV0说明。</td></tr><tr><td>12</td><td>CH1SSTEV0</td><td>Slave_TIMERx互连事件0生成通道1置位请求该位置1时,Slave_TIMERx互连事件0可以产生置位请求。具体请参考表19-5.Slave_TIMER内部连接事件。0:该事件不生成置位请求。1:该事件生成置位请求。</td></tr><tr><td>11</td><td>CH1SMTCMP3</td><td>Master_TIMER比较3事件生成通道1置位请求该位置1时,Master_TIMER比较3事件可以产生置位请求。0:Master_TIMER比较3事件不生成置位请求。1:Master_TIMER比较3事件生成置位请求。</td></tr><tr><td>10</td><td>CH1SMTCMP2</td><td>Master_TIMER比较2事件生成通道1置位请求该位置1时,Master_TIMER比较2事件可以产生置位请求。0:Master_TIMER比较2事件不生成置位请求。1: Master_TIMER 比较 2 事件生成置位请求。</td></tr><tr><td>9</td><td>CH1SMTCMP1</td><td>Master_TIMER 比较 1 事件生成通道 1 置位请求该位置 1 时,Master_TIMER 比较 1 事件可以产生置位请求。0: Master_TIMER 比较 1 事件不生成置位请求。1: Master_TIMER 比较 1 事件生成置位请求。</td></tr><tr><td>8</td><td>CH1SMTCMP0</td><td>Master_TIMER 比较 0 事件生成通道 1 置位请求该位置 1 时,Master_TIMER 比较 0 事件可以产生置位请求。0: Master_TIMER 比较 0 事件不生成置位请求。1: Master_TIMER 比较 0 事件生成置位请求。</td></tr><tr><td>7</td><td>CH1SMTPER</td><td>Master_TIMER 周期事件生成通道 1 置位请求连续模式下,Master_TIMER 计数器翻转事件可以产生置位请求。在单脉冲模式下,Master_TIMER 计数器复位事件可以产生置位请求。0: 该事件不生成置位请求。1: 该事件生成置位请求。</td></tr><tr><td>6</td><td>CH1SCMP3</td><td>Slave_TIMERx 比较 3 事件生成通道 1 置位请求该位置 1 时,Slave_TIMERx 比较 3 事件可以产生置位请求。0: Slave_TIMERx 比较 3 事件不生成置位请求。1: Slave_TIMERx 比较 3 事件生成置位请求。</td></tr><tr><td>5</td><td>CH1SCMP2</td><td>Slave_TIMERx 比较 2 事件生成通道 1 置位请求该位置 1 时,Slave_TIMERx 比较 2 事件可以产生置位请求。0: Slave_TIMERx 比较 2 事件不生成置位请求。1: Slave_TIMERx 比较 2 事件生成置位请求。</td></tr><tr><td>4</td><td>CH1SCMP1</td><td>Slave_TIMERx 比较 1 事件生成通道 1 置位请求该位置 1 时,Slave_TIMERx 比较 1 事件可以产生置位请求。0: Slave_TIMERx 比较 1 事件不生成置位请求。1: Slave_TIMERx 比较 1 事件生成置位请求。</td></tr><tr><td>3</td><td>CH1SCMP0</td><td>Slave_TIMERx 比较 0 事件生成通道 1 置位请求该位置 1 时,Slave_TIMERx 比较 0 事件可以产生置位请求。0: Slave_TIMERx 比较 0 事件不生成置位请求。1: Slave_TIMERx 比较 0 事件生成置位请求。</td></tr><tr><td>2</td><td>CH1SPER</td><td>Slave_TIMERx 周期事件生成通道 1 置位请求该位置 1 时,Slave_TIMERx 周期事件可以产生置位请求。0: Slave_TIMERx 周期事件不生成置位请求。1: Slave_TIMERx 周期事件生成置位请求。</td></tr><tr><td>1</td><td>CH1SRST</td><td>Slave_TIMERx 复位事件生成通道 1 置位请求该位置 1 时,由软件和同步输入引起的 Slave_TIMERx 复位事件,生成通道 1 置位请求。0: 该事件不生成置位请求。1: 该事件生成置位请求。</td></tr></table>

<table><tr><td></td><td></td><td>注意:该位置1时,其他的定时器复位事件不会影响输出。</td></tr><tr><td>0</td><td>CH1SSEV</td><td>软件事件生成通道1置位请求该位由软件置1,由硬件自动清除。该位置1时,生成通道1置位请求。0:该事件不生成置位请求1:该事件生成置位请求注意:该位不进行预装载。</td></tr></table>

## Slave_TIMERx 通道 1 复位请求寄存器 (SHRTIMER_STxCH1RST)

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CH1RSUP</td><td>CH1RSEXEV9</td><td>CH1RSEXEV8</td><td>CH1RSEXEV7</td><td>CH1RSEXEV6</td><td>CH1RSEXEV5</td><td>CH1RSEXEV4</td><td>CH1RSEXEV3</td><td>CH1RSEXEV2</td><td>CH1RSEXEV1</td><td>CH1RSEXEV0</td><td>CH1RSSTEV8</td><td>CH1RSSTEV7</td><td>CH1RSSTEV6</td><td>CH1RSSTEV5</td><td>CH1RSSTEV4</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CH1RSSTEV3</td><td>CH1RSSTEV2</td><td>CH1RSSTEV1</td><td>CH1RSSTEV0</td><td>CH1RSMTCMP3</td><td>CH1RSMTCMP2</td><td>CH1RSMTCMP1</td><td>CH1RSMTCMP0</td><td>CH1RSMTPER</td><td>CH1RSCMP3</td><td>CH1RSCMP2</td><td>CH1RSCMP1</td><td>CH1RSCMP0</td><td>CH1RSPER</td><td>CH1RSRST</td><td>CH1RSSEV</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CH1RSUP</td><td>更新事件生成通道1复位请求该位置1时,更新事件可以产生复位请求。0:更新事件不生成复位请求。1:更新事件生成复位请求。</td></tr><tr><td>30</td><td>CH1RSEXEV9</td><td>外部事件9生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>29</td><td>CH1RSEXEV8</td><td>外部事件8生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>28</td><td>CH1RSEXEV7</td><td>外部事件9生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>27</td><td>CH1RSEXEV6</td><td>外部事件6生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>26</td><td>CH1RSEXEV5</td><td>外部事件5生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>25</td><td>CH1RSEXEV4</td><td>外部事件4生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>24</td><td>CH1RSEXEV3</td><td>外部事件3生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>23</td><td>CH1RSEXEV2</td><td>外部事件2生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>22</td><td>CH1RSEXEV1</td><td>外部事件1生成通道1复位请求请参考CH1RSEXEV0说明。</td></tr><tr><td>21</td><td>CH1RSEXEV0</td><td>外部事件0生成通道1复位请求当该位置1时,外部事件0可以产生复位请求。0:该事件不生成复位请求。1:该事件生成复位请求。</td></tr><tr><td>20</td><td>CH1RSSTEV8</td><td>Slave_TIMERx互连事件8生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>19</td><td>CH1RSSTEV7</td><td>Slave_TIMERx互连事件7生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>18</td><td>CH1RSSTEV6</td><td>Slave_TIMERx互连事件6生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>17</td><td>CH1RSSTEV5</td><td>Slave_TIMERx互连事件5生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>16</td><td>CH1RSSTEV4</td><td>Slave_TIMERx互连事件4生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>15</td><td>CH1RSSTEV3</td><td>Slave_TIMERx互连事件3生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>14</td><td>CH1RSSTEV2</td><td>Slave_TIMERx互连事件2生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>13</td><td>CH1RSSTEV1</td><td>Slave_TIMERx互连事件1生成通道1复位请求请参考CH1RSSTEV0说明。</td></tr><tr><td>12</td><td>CH1RSSTEV0</td><td>Slave_TIMERx互连事件0生成通道1复位请求该位置1时,Slave_TIMERx互连事件1可以产生复位请求。具体请参考表19-5.Slave_TIMER内部连接事件。0:该事件不生成复位请求。1:该事件生成复位请求。</td></tr><tr><td>11</td><td>CH1RSMTCMP3</td><td>Master_TIMER比较3事件生成通道1复位请求该位置1时,Master_TIMER比较3事件可以产生复位请求。0:Master_TIMER比较3事件不生成复位请求。1:Master_TIMER比较3事件生成复位请求。</td></tr><tr><td>10</td><td>CH1RSMTCMP2</td><td>Master_TIMER比较2事件生成通道1复位请求该位置1时,Master_TIMER比较2事件可以产生复位请求。0:Master_TIMER比较2事件不生成复位请求。1: Master_TIMER 比较 2 事件生成复位请求。</td></tr><tr><td>9</td><td>CH1RSMTCMP1</td><td>Master_TIMER 比较 1 事件生成通道 1 复位请求该位置 1 时,Master_TIMER 比较 1 事件可以产生复位请求。0: Master_TIMER 比较 1 事件不生成复位请求。1: Master_TIMER 比较 1 事件生成复位请求。</td></tr><tr><td>8</td><td>CH1RSMTCMP0</td><td>Master_TIMER 比较 0 事件生成通道 1 复位请求该位置 1 时,Master_TIMER 比较 0 事件可以产生复位请求。0: Master_TIMER 比较 0 事件不生成复位请求。1: Master_TIMER 比较 0 事件生成复位请求。</td></tr><tr><td>7</td><td>CH1RSMTPER</td><td>Master_TIMER 周期事件生成通道 1 复位请求连续模式下,Master_TIMER 计数器翻转事件可以产生复位请求。在单脉冲模式下,Master_TIMER 计数器复位事件可以产生复位请求。0: 该事件不生成复位请求。1: 该事件生成复位请求。</td></tr><tr><td>6</td><td>CH1RSCMP3</td><td>Slave_TIMERx 比较 3 事件生成通道 1 复位请求该位置 1 时,Slave_TIMERx 比较 3 事件可以产生复位请求。0: Slave_TIMERx 比较 3 事件不生成复位请求。1: Slave_TIMERx 比较 3 事件生成复位请求。</td></tr><tr><td>5</td><td>CH1RSCMP2</td><td>Slave_TIMERx 比较 2 事件生成通道 1 复位请求该位置 1 时,Slave_TIMERx 比较 2 事件可以产生复位请求。0: Slave_TIMERx 比较 2 事件不生成复位请求。1: Slave_TIMERx 比较 2 事件生成复位请求。</td></tr><tr><td>4</td><td>CH1RSCMP1</td><td>Slave_TIMERx 比较 1 事件生成通道 1 复位请求该位置 1 时,Slave_TIMERx 比较 1 事件可以产生复位请求。0: Slave_TIMERx 比较 1 事件不生成复位请求。1: Slave_TIMERx 比较 1 事件生成复位请求。</td></tr><tr><td>3</td><td>CH1RSCMP0</td><td>Slave_TIMERx 比较 0 事件生成通道 1 复位请求该位置 1 时,Slave_TIMERx 比较 0 事件可以产生复位请求。0: Slave_TIMERx 比较 0 事件不生成复位请求。1: Slave_TIMERx 比较 0 事件生成复位请求。</td></tr><tr><td>2</td><td>CH1RSPER</td><td>Slave_TIMERx 周期事件生成通道 1 复位请求该位置 1 时,Slave_TIMERx 周期事件可以产生复位请求。0: Slave_TIMERx 周期事件不生成复位请求。1: Slave_TIMERx 周期事件生成复位请求。</td></tr><tr><td>1</td><td>CH1RSRST</td><td>Slave_TIMERx 复位事件生成通道 1 复位请求该位置 1 时,由软件和同步输入引起的 Slave_TIMERx 复位事件,生成通道 1 复位请求。0: 该事件不生成复位请求。1: 该事件生成复位请求。</td></tr></table>

<table><tr><td></td><td></td><td>注意:该位置1时,其他的定时器复位事件不会影响输出。</td></tr><tr><td>0</td><td>CH1RSSEV</td><td>软件事件生成通道1复位请求该位由软件置1,由硬件自动清除。该位置1时,生成通道1复位请求。0:该事件不生成复位请求1:该事件生成复位请求注意:该位不进行预装载。</td></tr></table>

## Slave_TIMERx 外部事件滤波配置寄存器 0 (SHRTIMER_STxEXEVFCFG0)

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="4">EXEV4FM[3:0]</td><td>EXEV4M EEN</td><td>保留</td><td colspan="4">EXEV3FM[3:0]</td><td>EXEV3M EEN</td><td>保留</td><td>EXEV2F M[3]</td></tr><tr><td colspan="3"></td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>EXEV2FM[2:0]</td><td>EXEV0M EEN</td><td>保留</td><td>EXEV1FM[3:0]</td><td>EXEV1M EEN</td><td>保留</td><td>EXEV0FM[3:0]</td><td>EXEV0M EEN</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28:25</td><td>EXEV4FM[3:0]</td><td>外部事件 4 滤波模式请参考 EXEV0FM [3:0]的描述。</td></tr><tr><td>24</td><td>EXEV4MEEN</td><td>外部事件 4 存储功能使能请参考 EXEV0MEEN 的描述。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:19</td><td>EXEV3FM[3:0]</td><td>外部事件 3 滤波模式请参考 EXEV0FM [3:0]的描述。</td></tr><tr><td>18</td><td>EXEV3MEEN</td><td>外部事件 3 存储功能使能请参考 EXEV0MEEN 的描述。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16:13</td><td>EXEV2FM[3:0]</td><td>外部事件 2 滤波模式请参考 EXEV0FM [3:0]的描述。</td></tr><tr><td>12</td><td>EXEV2MEEN</td><td>外部事件 2 存储功能使能请参考 EXEV0MEEN 的描述。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10:7</td><td>EXEV1FM[3:0]</td><td>外部事件1滤波模式请参考EXEV0FM[3:0]的描述。</td></tr><tr><td>6</td><td>EXEV1MEEN</td><td>外部事件1存储功能使能请参考EXEV0MEEN的描述。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:1</td><td>EXEV0FM[3:0]</td><td>外部事件0滤波模式在消隐模式下,如果外部事件在消隐期间发生,则将其忽略。在窗口模式下,仅当外部事件发生在给定的时间窗口内时,才考虑该外部事件。0000:滤波模式禁能。0001:消隐模式。消隐时间是从计数器复位到SHRTIMER_STxCMP0V比较事件发生持续的时间。0010:消隐模式。消隐时间是从计数器复位到SHRTIMER_STxCMP1V比较事件发生持续的时间。0011:消隐模式。消隐时间是从计数器复位到SHRTIMER_STxCMP2V比较事件发生持续的时间。0100:消隐模式。消隐时间是从计数器复位到SHRTIMER_STxCMP3V比较事件发生持续的时间。0101:消隐模式。消隐时间为其他Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC0。0110:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC1。0111:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC2。1000:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC3。1001:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC4。1010:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC5。1011:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC6。1100:消隐模式。消隐时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STBLKSRC7。1101:窗口模式。窗口时间是从计数器复位到SHRTIMER_STxCMP1V比较事件发生持续的时间。1110:窗口模式。窗口时间是从计数器复位到SHRTIMER_STxCMP2V比较事件发生持续的时间。1111:窗口模式。窗口时间为其他 Slave_TIMERy(除了 Slave_TIMERx):STWDSRC。</td></tr></table>

## 注意：

（1）一旦计数器使能（STxCEN 位置 1），不得修改该位域。

（2）用于滤波的比较寄存器的值必须大于 0。

0：外部事件 0 存储功能禁能。

1：外部事件 0 存储功能使能。一旦消隐周期或窗口周期完成，便会产生存储事件。注意：

（1）一旦计数器使能（STxCEN 位置 1），不得修改该位域。

（2）该位置 1 时，可以在窗口模式下生成超时事件。

## Slave_TIMERx 外部事件滤波配置寄存器 1 (SHRTIMER_STxEXEVFCFG1)

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="4">EXEV9FM[3:0]</td><td>EXEV9M EEN</td><td>保留</td><td colspan="4">EXEV8FM[3:0]</td><td>EXEV8M EEN</td><td>保留</td><td>EXEV7F M[3]</td></tr><tr><td colspan="7">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">EXEV7FM[2:0]</td><td>EXEV7M EEN</td><td>保留</td><td colspan="4">EXEV6FM[3:0]</td><td>EXEV6M EEN</td><td>保留</td><td colspan="4">EXEV5FM[3:0]</td><td>EXEV5M EEN</td></tr><tr><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28:25</td><td>EXEV9FM[3:0]</td><td>外部事件9滤波模式请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0FM [3:0]的描述。</td></tr><tr><td>24</td><td>EXEV9MEEN</td><td>外部事件9存储功能使能请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0MEEN的描述。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:19</td><td>EXEV8FM[3:0]</td><td>外部事件8滤波模式请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0FM [3:0]的描述。</td></tr><tr><td>18</td><td>EXEV8MEEN</td><td>外部事件8存储功能使能请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0MEEN的描述。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16:13</td><td>EXEV7FM[3:0]</td><td>外部事件7滤波模式请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0FM [3:0]的描述。</td></tr><tr><td>12</td><td>EXEV7MEEN</td><td>外部事件7存储功能使能请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0MEEN的描述。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10:7</td><td>EXEV6FM[3:0]</td><td>外部事件6滤波模式请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0FM[3:0]的描述。</td></tr><tr><td>6</td><td>EXEV6MEEN</td><td>外部事件6存储功能使能请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0MEEN的描述。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:1</td><td>EXEV5FM[3:0]</td><td>外部事件5滤波模式请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0FM[3:0]的描述。</td></tr><tr><td>0</td><td>EXEV5MEEN</td><td>外部事件5存储功能使能请参考SHRTIMER_STxEXEVFCFG0寄存器中的EXEV0MEEN的描述。</td></tr></table>

## Slave_TIMERx 计数器复位寄存器(SHRTIMER_STxCNTRST)

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

## For Slave_TIMER0

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>ST4CMP3RST</td><td>ST4CMP1RST</td><td>ST4CMP0RST</td><td>ST3CMP3RST</td><td>ST3CMP1RST</td><td>ST3CMP0RST</td><td>ST2CMP3RST</td><td>ST2CMP1RST</td><td>ST2CMP0RST</td><td>ST1CMP3RST</td><td>ST1CMP1RST</td><td>ST1CMP0RST</td><td>EXEV9RST</td><td>EXEV8RST</td><td>EXEV7RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV6RST</td><td>EXEV5RST</td><td>EXEV4RST</td><td>EXEV3RST</td><td>EXEV2RST</td><td>EXEV1RST</td><td>EXEV0RST</td><td>MTCMP3RST</td><td>MTCMP2RST</td><td>MTCMP1RST</td><td>MTCMP0RST</td><td>MTPERRST</td><td>CMP3RS T</td><td>CMP1RS T</td><td>UPRST</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>ST4CMP3RST</td><td>Slave_TIMER4 比较 3 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>29</td><td>ST4CMP1RST</td><td>Slave_TIMER4 比较 1 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>28</td><td>ST4CMP0RST</td><td>Slave_TIMER4 比较 0 事件复位计数器该位用于配置 Slave_TIMER4 比较 0 事件复位计数器。0: Slave_TIMER4 比较 0 事件不复位计数器。1: Slave_TIMER4 比较 0 事件复位计数器。</td></tr><tr><td>27</td><td>ST3CMP3RST</td><td>Slave_TIMER3 比较 3 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>26</td><td>ST3CMP1RST</td><td>Slave_TIMER3 比较 1 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr></table>

<table><tr><td>25</td><td>ST3CMP0RST</td><td>Slave_TIMER3 比较 0 事件复位计数器该位用于配置 Slave_TIMER3 比较 0 事件复位计数器。0: Slave_TIMER3 比较 0 事件不复位计数器。1: Slave_TIMER3 比较 0 事件复位计数器。</td></tr><tr><td>24</td><td>ST2CMP3RST</td><td>Slave_TIMER2 比较 3 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>23</td><td>ST2CMP1RST</td><td>Slave_TIMER2 比较 1 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>22</td><td>ST2CMP0RST</td><td>Slave_TIMER2 比较 0 事件复位计数器该位用于配置 Slave_TIMER2 比较 0 事件复位计数器。0: Slave_TIMER2 比较 0 事件不复位计数器。1: Slave_TIMER2 比较 0 事件复位计数器。</td></tr><tr><td>21</td><td>ST1CMP3RST</td><td>Slave_TIMER1 比较 3 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>20</td><td>ST1CMP1RST</td><td>Slave_TIMER1 比较 1 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>19</td><td>ST1CMP0RST</td><td>Slave_TIMER1 比较 0 事件复位计数器该位用于配置 Slave_TIMER1 比较 0 事件复位计数器。0: Slave_TIMER1 比较 0 事件不复位计数器。1: Slave_TIMER1 比较 0 事件复位计数器。</td></tr><tr><td>18</td><td>EXEV9RST</td><td>外部事件 9 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>17</td><td>EXEV8RST</td><td>外部事件 8 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>16</td><td>EXEV7RST</td><td>外部事件 7 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>15</td><td>EXEV6RST</td><td>外部事件 6 复位计数器请参考 EXEV0RST 说明。.</td></tr><tr><td>14</td><td>EXEV5RST</td><td>外部事件 5 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>13</td><td>EXEV4RST</td><td>外部事件 4 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>12</td><td>EXEV3RST</td><td>外部事件 3 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>11</td><td>EXEV2RST</td><td>外部事件 2 复位计数器请参考 EXEV0RST 说明。</td></tr></table>

<table><tr><td>10</td><td>EXEV1RST</td><td>外部事件1复位计数器请参考EXEV0RST说明。</td></tr><tr><td>9</td><td>EXEV0RST</td><td>外部事件0复位计数器0:外部事件0不复位计数器。1:外部事件0复位计数器。</td></tr><tr><td>8</td><td>MTCMP3RST</td><td>Master_TIMER比较3事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>7</td><td>MTCMP2RST</td><td>Master_TIMER比较2事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>6</td><td>MTCMP1RST</td><td>Master_TIMER比较1事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>5</td><td>MTCMP0RST</td><td>Master_TIMER比较0事件复位计数器该位用于配置Master_TIMER比较0事件复位计数器。0:Master_TIMER比较0事件不复位计数器。1:Master_TIMER比较0事件复位计数器。</td></tr><tr><td>4</td><td>MTPERRST</td><td>Master_TIMER周期事件复位计数器该位用于配置Master_TIMER周期事件复位计数器。0:Master_TIMER周期事件不复位计数器。1:Master_TIMER周期事件复位计数器。</td></tr><tr><td>3</td><td>CMP3RST</td><td>Slave_TIMER0比较3事件复位计数器请参考CMP1RST说明。</td></tr><tr><td>2</td><td>CMP1RST</td><td>Slave_TIMER0比较1事件复位计数器该位用于配置比较1事件复位计数器。0:比较1事件不复位计数器。1:比较1事件复位计数器。</td></tr><tr><td>1</td><td>UPRST</td><td>Slave_TIMER0更新事件复位计数器该位用于配置更新事件复位计数器。0:更新事件不复位计数器。1:更新事件复位计数器。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>


For Slave_TIMER1


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>ST4CMP3RST</td><td>ST4CMP1RST</td><td>ST4CMP0RST</td><td>ST3CMP3RST</td><td>ST3CMP1RST</td><td>ST3CMP0RST</td><td>ST2CMP3RST</td><td>ST2CMP1RST</td><td>ST2CMP0RST</td><td>ST0CMP3RST</td><td>ST0CMP1RST</td><td>ST0CMP0RST</td><td>EXEV9RST</td><td>EXEV8RST</td><td>EXEV7RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV6RST</td><td>EXEV5RST</td><td>EXEV4RST</td><td>EXEV3RST</td><td>EXEV2RST</td><td>EXEV1RST</td><td>EXEV0RST</td><td>MTCMP3RST</td><td>MTCMP2RST</td><td>MTCMP1RST</td><td>MTCMP0RST</td><td>MTPERRST</td><td>CMP3RS T</td><td>CMP1RS T</td><td>UPRST</td><td>保留</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>ST4CMP3RST</td><td>Slave_TIMER4 比较 3 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>29</td><td>ST4CMP1RST</td><td>Slave_TIMER4 比较 1 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>28</td><td>ST4CMP0RST</td><td>Slave_TIMER4 比较 0 事件复位计数器该位用于配置 Slave_TIMER4 比较 0 事件复位计数器。0: Slave_TIMER4 比较 0 事件不复位计数器1: Slave_TIMER4 比较 0 事件复位计数器</td></tr><tr><td>27</td><td>ST3CMP3RST</td><td>Slave_TIMER3 比较 3 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>26</td><td>ST3CMP1RST</td><td>Slave_TIMER3 比较 1 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>25</td><td>ST3CMP0RST</td><td>Slave_TIMER3 比较 0 事件复位计数器该位用于配置 Slave_TIMER3 比较 0 事件复位计数器。0: Slave_TIMER3 比较 0 事件不复位计数器1: Slave_TIMER3 比较 0 事件复位计数器</td></tr><tr><td>24</td><td>ST2CMP3RST</td><td>Slave_TIMER2 比较 3 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>23</td><td>ST2CMP1RST</td><td>Slave_TIMER2 比较 1 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>22</td><td>ST2CMP0RST</td><td>Slave_TIMER2 比较 0 事件复位计数器该位用于配置 Slave_TIMER2 比较 0 事件复位计数器。0: Slave_TIMER2 比较 0 事件不复位计数器1: Slave_TIMER2 比较 0 事件复位计数器</td></tr><tr><td>21</td><td>ST0CMP3RST</td><td>Slave_TIMER0 比较 3 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>20</td><td>ST0CMP1RST</td><td>Slave_TIMER0 比较 1 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>19</td><td>ST0CMP0RST</td><td>Slave_TIMER0 比较 0 事件复位计数器该位用于配置 Slave_TIMER0 比较 0 事件复位计数器。0: Slave_TIMER0 比较 0 事件不复位计数器1: Slave_TIMER0 比较 0 事件复位计数器</td></tr><tr><td>18</td><td>EXEV9RST</td><td>外部事件 9 复位计数器</td></tr></table>

<table><tr><td></td><td></td><td>请参考 EXEV0RST 说明。</td></tr><tr><td>17</td><td>EXEV8RST</td><td>外部事件 8 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>16</td><td>EXEV7RST</td><td>外部事件 7 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>15</td><td>EXEV6RST</td><td>外部事件 6 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>14</td><td>EXEV5RST</td><td>外部事件 5 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>13</td><td>EXEV4RST</td><td>外部事件 4 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>12</td><td>EXEV3RST</td><td>外部事件 3 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>11</td><td>EXEV2RST</td><td>外部事件 2 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>10</td><td>EXEV1RST</td><td>外部事件 1 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>9</td><td>EXEV0RST</td><td>外部事件 0 复位计数器0: 外部事件 0 不复位计数器1: 外部事件 0 复位计数器</td></tr><tr><td>8</td><td>MTCMP3RST</td><td>Master_TIMER 比较 3 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>7</td><td>MTCMP2RST</td><td>Master_TIMER 比较 2 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>6</td><td>MTCMP1RST</td><td>Master_TIMER 比较 1 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>5</td><td>MTCMP0RST</td><td>Master_TIMER 比较 0 事件复位计数器该位用于配置 Master_TIMER 比较 0 事件复位计数器。0: Master_TIMER 比较 0 事件不复位计数器1: Master_TIMER 比较 0 事件复位计数器</td></tr><tr><td>4</td><td>MTPERRST</td><td>Master_TIMER 周期事件复位计数器该位用于配置 Master_TIMER 周期事件复位计数器。0: Master_TIMER 周期事件不复位计数器1: Master_TIMER 周期事件复位计数器</td></tr><tr><td>3</td><td>CMP3RST</td><td>Slave_TIMER1 比较 3 事件复位计数器请参考 CMP1RST 说明。</td></tr></table>

<table><tr><td>2</td><td>CMP1RST</td><td>Slave_TIMER1 比较 1 事件复位计数器该位用于配置比较 1 事件复位计数器。0: 比较 1 事件不复位计数器1: 比较 1 事件复位计数器</td></tr><tr><td>1</td><td>UPRST</td><td>Slave_TIMER1 更新事件复位计数器该位用于配置更新事件复位计数器。0: 更新事件不复位计数器1: 更新事件复位计数器</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>


For Slave_TIMER2


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>ST4CMP3RST</td><td>ST4CMP1RST</td><td>ST4CMP0RST</td><td>ST3CMP3RST</td><td>ST3CMP1RST</td><td>ST3CMP0RST</td><td>ST1CMP3RST</td><td>ST1CMP1RST</td><td>ST1CMP0RST</td><td>ST0CMP3RST</td><td>ST0CMP1RST</td><td>ST0CMP0RST</td><td>EXEV9RST</td><td>EXEV8RST</td><td>EXEV7RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV6RST</td><td>EXEV5RST</td><td>EXEV4RST</td><td>EXEV3RST</td><td>EXEV2RST</td><td>EXEV1RST</td><td>EXEV0RST</td><td>MTCMP3RST</td><td>MTCMP2RST</td><td>MTCMP1RST</td><td>MTCMP0RST</td><td>MTPERRST</td><td>CMP3RS T</td><td>CMP1RS T</td><td>UPRST</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>ST4CMP3RST</td><td>Slave_TIMER4 比较 3 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>29</td><td>ST4CMP1RST</td><td>Slave_TIMER4 比较 1 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>28</td><td>ST4CMP0RST</td><td>Slave_TIMER4 比较 0 事件复位计数器该位用于配置 Slave_TIMER4 比较 0 事件复位计数器。0: Slave_TIMER4 比较 0 事件不复位计数器1: Slave_TIMER4 比较 0 事件复位计数器</td></tr><tr><td>27</td><td>ST3CMP3RST</td><td>Slave_TIMER3 比较 3 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>26</td><td>ST3CMP1RST</td><td>Slave_TIMER3 比较 1 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>25</td><td>ST3CMP0RST</td><td>Slave_TIMER3 比较 0 事件复位计数器该位用于配置 Slave_TIMER3 比较 0 事件复位计数器。0: Slave_TIMER3 比较 0 事件不复位计数器1: Slave_TIMER3 比较 0 事件复位计数器</td></tr></table>

<table><tr><td>24</td><td>ST1CMP3RST</td><td>Slave_TIMER1 比较 3 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>23</td><td>ST1CMP1RST</td><td>Slave_TIMER1 比较 1 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>22</td><td>ST1CMP0RST</td><td>Slave_TIMER1 比较 0 事件复位计数器该位用于配置 Slave_TIMER1 比较 0 事件复位计数器。0: Slave_TIMER1 比较 0 事件不复位计数器1: Slave_TIMER1 比较 0 事件复位计数器</td></tr><tr><td>21</td><td>ST0CMP3RST</td><td>Slave_TIMER0 比较 3 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>20</td><td>ST0CMP1RST</td><td>Slave_TIMER0 比较 1 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>19</td><td>ST0CMP0RST</td><td>Slave_TIMER0 比较 0 事件复位计数器该位用于配置 Slave_TIMER0 比较 0 事件复位计数器。0: Slave_TIMER0 比较 0 事件不复位计数器1: Slave_TIMER0 比较 0 事件复位计数器</td></tr><tr><td>18</td><td>EXEV9RST</td><td>外部事件 9 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>17</td><td>EXEV8RST</td><td>外部事件 8 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>16</td><td>EXEV7RST</td><td>外部事件 7 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>15</td><td>EXEV6RST</td><td>外部事件 6 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>14</td><td>EXEV5RST</td><td>外部事件 5 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>13</td><td>EXEV4RST</td><td>外部事件 4 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>12</td><td>EXEV3RST</td><td>外部事件 3 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>11</td><td>EXEV2RST</td><td>外部事件 2 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>10</td><td>EXEV1RST</td><td>外部事件 1 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>9</td><td>EXEV0RST</td><td>外部事件 0 复位计数器0: 外部事件 0 不复位计数器</td></tr></table>

<table><tr><td></td><td></td><td>1: 外部事件0复位计数器</td></tr><tr><td>8</td><td>MTCMP3RST</td><td>Master_TIMER比较3事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>7</td><td>MTCMP2RST</td><td>Master_TIMER比较2事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>6</td><td>MTCMP1RST</td><td>Master_TIMER比较1事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>5</td><td>MTCMP0RST</td><td>Master_TIMER比较0事件复位计数器该位用于配置Master_TIMER比较0事件复位计数器。0: Master_TIMER比较0事件不复位计数器。1: Master_TIMER比较0事件复位计数器。</td></tr><tr><td>4</td><td>MTPERRST</td><td>Master_TIMER周期事件复位计数器该位用于配置Master_TIMER周期事件复位计数器。0: Master_TIMER周期事件不复位计数器。1: Master_TIMER周期事件复位计数器。</td></tr><tr><td>3</td><td>CMP3RST</td><td>Slave_TIMER2比较3事件复位计数器请参考CMP1RST说明。</td></tr><tr><td>2</td><td>CMP1RST</td><td>Slave_TIMER2比较1事件复位计数器该位用于配置比较1事件复位计数器。0: 比较1事件不复位计数器。1: 比较1事件复位计数器。</td></tr><tr><td>1</td><td>UPRST</td><td>Slave_TIMER2更新事件复位计数器该位用于配置更新事件复位计数器。0: 更新事件不复位计数器1: 更新事件复位计数器</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>


For Slave_TIMER3


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>ST4CMP3RST</td><td>ST4CMP1RST</td><td>ST4CMP0RST</td><td>ST2CMP3RST</td><td>ST2CMP1RST</td><td>ST2CMP0RST</td><td>ST1CMP3RST</td><td>ST1CMP1RST</td><td>ST1CMP0RST</td><td>ST0CMP3RST</td><td>ST0CMP1RST</td><td>ST0CMP0RST</td><td>EXEV9RST</td><td>EXEV8RST</td><td>EXEV7RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV6RST</td><td>EXEV5RST</td><td>EXEV4RST</td><td>EXEV3RST</td><td>EXEV2RST</td><td>EXEV1RST</td><td>EXEV0RST</td><td>MTCMP3RST</td><td>MTCMP2RST</td><td>MTCMP1RST</td><td>MTCMP0RST</td><td>MTPERRST</td><td>CMP3RS T</td><td>CMP1RS T</td><td>UPRST</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>ST4CMP3RST</td><td>Slave_TIMER4 比较 3 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>29</td><td>ST4CMP1RST</td><td>Slave_TIMER4 比较 1 事件复位计数器请参考 ST4CMP0RST 说明。</td></tr><tr><td>28</td><td>ST4CMP0RST</td><td>Slave_TIMER4 比较 0 事件复位计数器该位用于配置 Slave_TIMER4 比较 0 事件复位计数器。0: Slave_TIMER4 比较 0 事件不复位计数器。1: Slave_TIMER4 比较 0 事件复位计数器。</td></tr><tr><td>27</td><td>ST2CMP3RST</td><td>Slave_TIMER2 比较 3 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>26</td><td>ST2CMP1RST</td><td>Slave_TIMER2 比较 1 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>25</td><td>ST2CMP0RST</td><td>Slave_TIMER2 比较 0 事件复位计数器该位用于配置 Slave_TIMER2 比较 0 事件复位计数器。0: Slave_TIMER2 比较 0 事件不复位计数器。1: Slave_TIMER2 比较 0 事件复位计数器。</td></tr><tr><td>24</td><td>ST1CMP3RST</td><td>Slave_TIMER1 比较 3 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>23</td><td>ST1CMP1RST</td><td>Slave_TIMER1 比较 1 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>22</td><td>ST1CMP0RST</td><td>Slave_TIMER1 比较 0 事件复位计数器该位用于配置 Slave_TIMER1 比较 0 事件复位计数器。0: Slave_TIMER2 比较 0 事件不复位计数器。1: Slave_TIMER1 比较 0 事件复位计数器。</td></tr><tr><td>21</td><td>ST0CMP3RST</td><td>Slave_TIMER0 比较 3 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>20</td><td>ST0CMP1RST</td><td>Slave_TIMER0 比较 1 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>19</td><td>ST0CMP0RST</td><td>Slave_TIMER0 比较 0 事件复位计数器该位用于配置 Slave_TIMER0 比较 0 事件复位计数器。0: Slave_TIMER0 比较 0 事件不复位计数器。1: Slave_TIMER0 比较 0 事件复位计数器。</td></tr><tr><td>18</td><td>EXEV9RST</td><td>外部事件 9 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>17</td><td>EXEV8RST</td><td>外部事件 8 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>16</td><td>EXEV7RST</td><td>外部事件7复位计数器请参考EXEV0RST说明。</td></tr><tr><td>15</td><td>EXEV6RST</td><td>外部事件6复位计数器请参考EXEV0RST说明。</td></tr><tr><td>14</td><td>EXEV5RST</td><td>外部事件5复位计数器请参考EXEV0RST说明。</td></tr><tr><td>13</td><td>EXEV4RST</td><td>外部事件4复位计数器请参考EXEV0RST说明。</td></tr><tr><td>12</td><td>EXEV3RST</td><td>外部事件3复位计数器请参考EXEV0RST说明。</td></tr><tr><td>11</td><td>EXEV2RST</td><td>外部事件2复位计数器请参考EXEV0RST说明。</td></tr><tr><td>10</td><td>EXEV1RST</td><td>外部事件1复位计数器请参考EXEV0RST说明。</td></tr><tr><td>9</td><td>EXEV0RST</td><td>外部事件0复位计数器该位用于配置外部事件0复位计数器。0:外部事件0不复位计数器。1:外部事件0复位计数器。</td></tr><tr><td>8</td><td>MTCMP3RST</td><td>Master_TIMER比较3事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>7</td><td>MTCMP2RST</td><td>Master_TIMER比较2事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>6</td><td>MTCMP1RST</td><td>Master_TIMER比较1事件复位计数器请参考MTCMP0RST说明。</td></tr><tr><td>5</td><td>MTCMP0RST</td><td>Master_TIMER比较0事件复位计数器该位用于配置Master_TIMER比较0事件复位计数器。0:Master_TIMER比较0事件不复位计数器。1:Master_TIMER比较0事件复位计数器。</td></tr><tr><td>4</td><td>MTPERRST</td><td>Master_TIMER周期事件复位计数器该位用于配置Master_TIMER周期事件复位计数器。0:Master_TIMER周期事件不复位计数器。1:Master_TIMER周期事件复位计数器。</td></tr><tr><td>3</td><td>CMP3RST</td><td>Slave_TIMER3比较3事件复位计数器请参考CMP1RST说明。</td></tr><tr><td>2</td><td>CMP1RST</td><td>Slave_TIMER3比较1事件复位计数器该位用于配置比较1事件复位计数器。0:比较1事件不复位计数器。</td></tr></table>

<table><tr><td></td><td></td><td>1: 比较 1 事件复位计数器。</td></tr><tr><td>1</td><td>UPRST</td><td>Slave_TIMER3 更新事件复位计数器该位用于配置更新事件复位计数器。0: 更新事件不复位计数器。1: 更新事件复位计数器。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>


For Slave_TIMER4


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>ST3CMP3RST</td><td>ST3CMP1RST</td><td>ST3CMP0RST</td><td>ST2CMP3RST</td><td>ST2CMP1RST</td><td>ST2CMP0RST</td><td>ST1CMP3RST</td><td>ST1CMP1RST</td><td>ST1CMP0RST</td><td>ST0CMP3RST</td><td>ST0CMP1RST</td><td>ST0CMP0RST</td><td>EXEV9RST</td><td>EXEV8RST</td><td>EXEV7RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV6RST</td><td>EXEV5RST</td><td>EXEV4RST</td><td>EXEV3RST</td><td>EXEV2RST</td><td>EXEV1RST</td><td>EXEV0RST</td><td>MTCMP3RST</td><td>MTCMP2RST</td><td>MTCMP1RST</td><td>MTCMP0RST</td><td>MTPERRST</td><td>CMP3RS T</td><td>CMP1RS T</td><td>UPRST</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>30</td><td>ST3CMP3RST</td><td>Slave_TIMER3 比较 3 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>29</td><td>ST3CMP1RST</td><td>Slave_TIMER3 比较 1 事件复位计数器请参考 ST3CMP0RST 说明。</td></tr><tr><td>28</td><td>ST3CMP0RST</td><td>Slave_TIMER3 比较 0 事件复位计数器该位用于配置 Slave_TIMER3 比较 0 事件复位计数器。0: Slave_TIMER3 比较 0 事件不复位计数器。1: Slave_TIMER3 比较 0 事件复位计数器。</td></tr><tr><td>27</td><td>ST2CMP3RST</td><td>Slave_TIMER2 比较 3 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>26</td><td>ST2CMP1RST</td><td>Slave_TIMER2 比较 1 事件复位计数器请参考 ST2CMP0RST 说明。</td></tr><tr><td>25</td><td>ST2CMP0RST</td><td>Slave_TIMER2 比较 0 事件复位计数器该位用于配置 Slave_TIMER2 比较 0 事件复位计数器。0: Slave_TIMER2 比较 0 事件不复位计数器。1: Slave_TIMER2 比较 0 事件复位计数器。</td></tr><tr><td>24</td><td>ST1CMP3RST</td><td>Slave_TIMER1 比较 3 事件复位计数器请参考 ST1CMP0RST 说明。</td></tr><tr><td>23</td><td>ST1CMP1RST</td><td>Slave_TIMER1 比较 1 事件复位计数器</td></tr><tr><td>22</td><td>ST1CMP0RST</td><td>Slave_TIMER1 比较 0 事件复位计数器该位用于配置 Slave_TIMER1 比较 0 事件复位计数器。0: Slave_TIMER1 比较 0 事件不复位计数器。1: Slave_TIMER1 比较 0 事件复位计数器。</td></tr><tr><td>21</td><td>ST0CMP3RST</td><td>Slave_TIMER0 比较 3 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>20</td><td>ST0CMP1RST</td><td>Slave_TIMER0 比较 1 事件复位计数器请参考 ST0CMP0RST 说明。</td></tr><tr><td>19</td><td>ST0CMP0RST</td><td>Slave_TIMER0 比较 0 事件复位计数器该位用于配置 Slave_TIMER0 比较 0 事件复位计数器。0: Slave_TIMER0 比较 0 事件不复位计数器。1: Slave_TIMER0 比较 0 事件复位计数器。</td></tr><tr><td>18</td><td>EXEV9RST</td><td>外部事件 9 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>17</td><td>EXEV8RST</td><td>外部事件 8 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>16</td><td>EXEV7RST</td><td>外部事件 7 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>15</td><td>EXEV6RST</td><td>外部事件 6 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>14</td><td>EXEV5RST</td><td>外部事件 5 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>13</td><td>EXEV4RST</td><td>外部事件 4 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>12</td><td>EXEV3RST</td><td>外部事件 3 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>11</td><td>EXEV2RST</td><td>外部事件 2 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>10</td><td>EXEV1RST</td><td>外部事件 1 复位计数器请参考 EXEV0RST 说明。</td></tr><tr><td>9</td><td>EXEV0RST</td><td>外部事件 0 复位计数器0: 外部事件 0 不复位计数器1: 外部事件 0 复位计数器</td></tr><tr><td>8</td><td>MTCMP3RST</td><td>Master_TIMER 比较 3 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>7</td><td>MTCMP2RST</td><td>Master_TIMER 比较 2 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>6</td><td>MTCMP1RST</td><td>Master_TIMER 比较 1 事件复位计数器请参考 MTCMP0RST 说明。</td></tr><tr><td>5</td><td>MTCMP0RST</td><td>Master_TIMER 比较 0 事件复位计数器该位用于配置 Master_TIMER 比较 0 事件复位计数器。0: Master_TIMER 比较 0 事件不复位计数器。1: Master_TIMER 比较 0 事件复位计数器。</td></tr><tr><td>4</td><td>MTPERRST</td><td>Master_TIMER 周期事件复位计数器该位用于配置 Master_TIMER 周期事件复位计数器。0: Master_TIMER 周期事件不复位计数器。1: Master_TIMER 周期事件复位计数器。</td></tr><tr><td>3</td><td>CMP3RST</td><td>Slave_TIMER4 比较 3 事件复位计数器请参考 CMP1RST 说明。</td></tr><tr><td>2</td><td>CMP1RST</td><td>Slave_TIMER4 比较 1 事件复位计数器该位用于配置比较 1 事件复位计数器。0: 比较 1 事件不复位计数器。1: 比较 1 事件复位计数器。</td></tr><tr><td>1</td><td>UPRST</td><td>Slave_TIMER4 更新事件复位计数器该位用于配置更新事件复位计数器。0: 更新事件不复位计数器。1: 更新事件复位计数器。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## Slave_TIMERx 载波控制寄存器 (SHRTIMER_STxCSCTL)

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="4">CSFSTPW[3:0]</td><td colspan="3">CSDTY[2:0]</td><td colspan="4">CSPRD[3:0]</td></tr><tr><td colspan="5"></td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10:7</td><td>CSFSTPW[3:0]</td><td>第一个载波信号的脉冲宽度该位域定义了在通道输出准备信号(CHxOPRE)上升沿之后的第一个载波信号的脉</td></tr></table>

```txt
冲宽度。
tCSFSTPW = (CSFSTPW[3:0]+1) x tSHRTIMER_CSGCK, tSHRTIMER_CSGCK = 16 x tSHRTIMER_CK.
0000: tCSFSTPW = tSHRTIMER_CSGCK
0001: tCSFSTPW = 2*tSHRTIMER_CSGCK
...
1110: tCSFSTPW = 15*tSHRTIMER_CSGCK
1111: tCSFSTPW = 16*tSHRTIMER_CSGCK

6:4 CSDTY[2:0] 载波信号占空比
该位域定义了载波信号（第一个脉冲除外）的占空比为CSDTY [2:0] / 8。
000: 0%（仅出现第一个脉冲）。
001: 12.5%
010: 25.0%
011: 37.5%
100: 50.0%
101: 62.5%
110: 75.0%
111: 87.5%

3:0 CSPRD[3:0] 载波信号周期
该位域定义了载波信号的周期（第一个脉冲除外）。
tCSPRD = (CSPRD[3:0]+1) x tSHRTIMER_CSGCK, tSHRTIMER_CSGCK = 16 x tSHRTIMER_CK.
0000: 16 x tSHRTIMER_CK
0001: 32 x tSHRTIMER_CK
...
1111: 256 x tSHRTIMER_CK
```

## Slave_TIMERx 捕获 0 触发寄存器 (SHRTIMER_STxCAP0TRG)

地址偏移：0x5C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CP0BST4CMP1</td><td>CP0BST4CMP0</td><td>CP0BST4NA</td><td>CP0BST4A</td><td>CP0BST3CMP1</td><td>CP0BST3CMP0</td><td>CP0BST3NA</td><td>CP0BST3A</td><td>CP0BST2MP1</td><td>CP0BST2CMP0</td><td>CP0BST2NA</td><td>CP0BST2A</td><td>CP0BST1CMP1</td><td>CP0BST1CMP0</td><td>CP0BST1NA</td><td>CP0BST1A</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CP0BST0CMP1</td><td>CP0BST0CMP0</td><td>CP0BST0NA</td><td>CP0BST0A</td><td>CP0BEXEV9</td><td>CP0BEXEV8</td><td>CP0BEXEV7</td><td>CP0BEXEV6</td><td>CP0BEXEV5</td><td>CP0BEXEV4</td><td>CP0BEXEV3</td><td>CP0BEXEV2</td><td>CP0BEXEV1</td><td>CP0BEXEV0</td><td>CP0BUP</td><td>CP0BSW</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CP0BST4CMP1</td><td>Slave_TIMER4 的比较 1 事件触发捕获 0该位仅在 Slave_TIMER4 的寄存器中保留。</td></tr></table>

<table><tr><td></td><td></td><td>请参考 CP0BST0CMP1 描述。</td></tr><tr><td>30</td><td>CP0BST4CMP0</td><td>Slave_TIMER4 的比较 0 事件触发捕获 0该位仅在 Slave_TIMER4 的寄存器中保留。请参考 CP0BST0CMP0 描述。</td></tr><tr><td>29</td><td>CP0BST4NA</td><td>ST4CH0_O 输出有效到无效的变化触发捕获 0该位仅在 Slave_TIMER4 的寄存器中保留。请参考 CP0BST0NA 描述。</td></tr><tr><td>28</td><td>CP0BST4A</td><td>ST4CH0_O 输出无效到有效的变化触发捕获 0该位仅在 Slave_TIMER4 的寄存器中保留。请参考 CP0BST0A 描述。</td></tr><tr><td>27</td><td>CP0BST3CMP1</td><td>Slave_TIMER3 的比较 1 事件触发捕获 0该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP0BST0CMP1 描述。</td></tr><tr><td>26</td><td>CP0BST3CMP0</td><td>Slave_TIMER3 的比较 0 事件触发捕获 0该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP0BST0CMP0 描述。</td></tr><tr><td>25</td><td>CP0BST3NA</td><td>ST3CH0_O 输出有效到无效的变化触发捕获 0该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP0BST0NA 描述。</td></tr><tr><td>24</td><td>CP0BST3A</td><td>ST3CH0_O 输出无效到有效的变化触发捕获 0该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP0BST0A 描述。</td></tr><tr><td>23</td><td>CP0BST2CMP1</td><td>Slave_TIMER2 的比较 1 事件触发捕获 0该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP0BST0CMP1 描述。</td></tr><tr><td>22</td><td>CP0BST2CMP0</td><td>Slave_TIMER2 的比较 0 事件触发捕获 0该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP0BST0CMP0 描述。</td></tr><tr><td>21</td><td>CP0BST2NA</td><td>ST2CH0_O 输出有效到无效的变化触发捕获 0该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP0BST0NA 描述。</td></tr><tr><td>20</td><td>CP0BST2A</td><td>ST2CH0_O 输出无效到有效的变化触发捕获 0该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP0BST0A 描述。</td></tr><tr><td>19</td><td>CP0BST1CMP1</td><td>Slave_TIMER1 的比较 1 事件触发捕获 0该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP0BST0CMP1 描述。</td></tr><tr><td>18</td><td>CP0BST1CMP0</td><td>Slave_TIMER1 的比较 0 事件触发捕获 0</td></tr></table>

<table><tr><td></td><td></td><td>该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP0BST0CMP0 描述。</td></tr><tr><td>17</td><td>CP0BST1NA</td><td>ST1CH0_O 输出有效到无效的变化触发捕获 0该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP0BST0NA 描述。</td></tr><tr><td>16</td><td>CP0BST1A</td><td>ST1CH0_O 输出无效到有效的变化触发捕获 0该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP0BST0A 描述。</td></tr><tr><td>15</td><td>CP0BST0CMP1</td><td>Slave_TIMER0 的比较 1 事件触发捕获 0该位仅在 Slave_TIMER0 的寄存器中保留。0: Slave_TIMER0 的比较 1 事件不触发捕获 0。1: Slave_TIMER0 的比较 1 事件触发捕获 0。</td></tr><tr><td>14</td><td>CP0BST0CMP0</td><td>Slave_TIMER0 的比较 0 事件触发捕获 0该位仅在 Slave_TIMER0 的寄存器中保留。0: Slave_TIMER0 的比较 0 事件不触发捕获 0。1: Slave_TIMER0 的比较 0 事件触发捕获 0。</td></tr><tr><td>13</td><td>CP0BST0NA</td><td>ST0CH0_O 输出有效到无效的变化触发捕获 0当 Slave_TIMER0 通道 0 的输出从有效电平转换为无效电平时,捕获 0 由 ST0CH0_O 触发。该位仅在 Slave_TIMER0 中保留。0: ST0CH0_O 输出有效到无效的变化不触发捕获 0。1: ST0CH0_O 输出有效到无效的变化触发捕获 0。</td></tr><tr><td>12</td><td>CP0BST0A</td><td>ST0CH0_O 输出无效到有效的变化触发捕获 0当 Slave_TIMER0 通道 0 的输出从无效电平转换为有效电平时,捕获 0 由 ST0CH0_O 触发。该位仅在 Slave_TIMER0 中保留。0: ST0CH0_O 输出无效到有效的变化不触发捕获 0。1: ST0CH0_O 输出无效到有效的变化触发捕获 0。</td></tr><tr><td>11</td><td>CP0BEXEV9</td><td>外部事件 9 触发捕获 0请参考 CP0BEXEV0 描述。</td></tr><tr><td>10</td><td>CP0BEXEV8</td><td>外部事件 8 触发捕获 0请参考 CP0BEXEV0 描述。</td></tr><tr><td>9</td><td>CP0BEXEV7</td><td>外部事件 7 触发捕获 0请参考 CP0BEXEV0 描述。</td></tr><tr><td>8</td><td>CP0BEXEV6</td><td>外部事件 6 触发捕获 0请参考 CP0BEXEV0 描述。</td></tr><tr><td>7</td><td>CP0BEXEV5</td><td>外部事件 5 触发捕获 0请参考 CP0BEXEV0 描述。</td></tr><tr><td>6</td><td>CP0BEXEV4</td><td>外部事件4触发捕获0请参考CP0BEXEV0描述。</td></tr><tr><td>5</td><td>CP0BEXEV3</td><td>外部事件3触发捕获0请参考CP0BEXEV0描述。</td></tr><tr><td>4</td><td>CP0BEXEV2</td><td>外部事件2触发捕获0请参考CP0BEXEV0描述。</td></tr><tr><td>3</td><td>CP0BEXEV1</td><td>外部事件1触发捕获0请参考CP0BEXEV0描述。</td></tr><tr><td>2</td><td>CP0BEXEV0</td><td>外部事件0触发捕获0当该位置1时,外部事件0触发捕获0。0:外部事件0不触发捕获01:外部事件0触发捕获0</td></tr><tr><td>1</td><td>CP0BUP</td><td>更新事件触发捕获0当该位置1时,更新事件触发捕获0。0:更新事件不触发捕获01:更新事件触发捕获0</td></tr><tr><td>0</td><td>CP0BSW</td><td>软件触发捕获0该位由软件置1,硬件自动清零。该位置1时,软件触发捕获0。0:软件不触发捕获01:软件触发捕获0</td></tr></table>

## Slave_TIMERx 捕获 1 触发寄存器 (SHRTIMER_STxCAP1TRG)

地址偏移：0x60

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CP1BST4CMP1</td><td>CP1BST4CMP0</td><td>CP1BST4NA</td><td>CP1BST4A</td><td>CP1BST3CMP1</td><td>CP1BST3CMP0</td><td>CP1BST3NA</td><td>CP1BST3A</td><td>CP1BST2MP1</td><td>CP1BST2CMP0</td><td>CP1BST2NA</td><td>CP1BST2A</td><td>CP1BST1CMP1</td><td>CP1BST1CMP0</td><td>CP1BST1NA</td><td>CP1BST1A</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CP1BST0CMP1</td><td>CP1BST0CMP0</td><td>CP1BST0NA</td><td>CP1BST0A</td><td>CP1BEXEV9</td><td>CP1BEXEV8</td><td>CP1BEXEV7</td><td>CP1BEXEV6</td><td>CP1BEXEV5</td><td>CP1BEXEV4</td><td>CP1BEXEV3</td><td>CP1BEXEV2</td><td>CP1BEXEV1</td><td>CP1BEXEV0</td><td>CP1BUP</td><td>CP1BSW</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td></td><td></td><td>该位仅在 Slave_TIMER4 的寄存器中保留。请参考 CP1BST0CMP0 描述。</td></tr><tr><td>29</td><td>CP1BST4NA</td><td>ST4CH0_O 输出有效到无效的变化触发捕获 1 该位仅在 Slave_TIMER4 的寄存器中。请参考 CP1BST0NA 描述。</td></tr><tr><td>28</td><td>CP1BST4A</td><td>ST4CH0_O 输出无效到有效的变化触发捕获 1 该位仅在 Slave_TIMER4 的寄存器中保留。请参考 CP1BST0A 描述。</td></tr><tr><td>27</td><td>CP1BST3CMP1</td><td>Slave_TIMER3 的比较 1 事件触发捕获 1 该位仅存在于 Slave_TIMER3 的寄存器中保留。请参考 CP1BST0CMP1 描述。</td></tr><tr><td>26</td><td>CP1BST3CMP0</td><td>Slave_TIMER3 的比较 0 事件触发捕获 1 该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP1BST0CMP0 描述。</td></tr><tr><td>25</td><td>CP1BST3NA</td><td>ST3CH0_O 输出有效到无效的变化触发捕获 1 该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP1BST0NA 描述。</td></tr><tr><td>24</td><td>CP1BST3A</td><td>ST3CH0_O 输出无效到有效的变化触发捕获 1 该位仅在 Slave_TIMER3 的寄存器中保留。请参考 CP1BST0A 描述。</td></tr><tr><td>23</td><td>CP1BST2CMP1</td><td>Slave_TIMER2 的比较 1 事件触发捕获 1 该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP1BST0CMP1 描述。</td></tr><tr><td>22</td><td>CP1BST2CMP0</td><td>Slave_TIMER2 的比较 0 事件触发捕获 1 该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP1BST0CMP0 描述。</td></tr><tr><td>21</td><td>CP1BST2NA</td><td>ST2CH0_O 输出有效到无效的变化触发捕获 1 该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP1BST0NA 描述。</td></tr><tr><td>20</td><td>CP1BST2A</td><td>ST2CH0_O 输出无效到有效的变化触发捕获 1 该位仅在 Slave_TIMER2 的寄存器中保留。请参考 CP1BST0A 描述。</td></tr><tr><td>19</td><td>CP1BST1CMP1</td><td>Slave_TIMER1 的比较 1 事件触发捕获 1 该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP1BST0CMP1 描述。</td></tr><tr><td>18</td><td>CP1BST1CMP0</td><td>Slave_TIMER1 的比较 0 事件触发捕获 1 该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP1BST0CMP0 描述。</td></tr></table>

<table><tr><td>17</td><td>CP1BST1NA</td><td>ST1CH0_O输出有效到无效的变化触发捕获1该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP1BST0NA 描述。</td></tr><tr><td>16</td><td>CP1BST1A</td><td>ST1CH0_O输出无效到有效的变化触发捕获1该位仅在 Slave_TIMER1 的寄存器中保留。请参考 CP1BST0A 描述。</td></tr><tr><td>15</td><td>CP1BST0CMP1</td><td>Slave_TIMER0 的比较 1 事件触发捕获 1该位仅在 Slave_TIMER0 的寄存器中保留。0: Slave_TIMER0 的比较 1 事件不触发捕获 1。1: Slave_TIMER0 的比较 1 事件触发捕获 1。</td></tr><tr><td>14</td><td>CP1BST0CMP0</td><td>Slave_TIMER0 的比较 0 事件触发捕获 1该位仅在 Slave_TIMER0 的寄存器中保留。0: Slave_TIMER0 的比较 0 事件不触发捕获 1。1: Slave_TIMER0 的比较 0 事件触发捕获 1。</td></tr><tr><td>13</td><td>CP1BST0NA</td><td>ST0CH0_O 输出有效到无效的变化触发捕获 1当 Slave_TIMER0 通道 0 的输出从有效电平转换为无效电平时,捕获 1 由 ST0CH0_O 触发。该位仅在 Slave_TIMER0 中保留。0: ST0CH0_O 输出有效到无效的变化不触发捕获 1。1: ST0CH0_O 输出有效到无效的变化触发捕获 1。</td></tr><tr><td>12</td><td>CP1BST0A</td><td>ST0CH0_O 输出无效到有效的变化触发捕获 1当 Slave_TIMER0 通道 0 的输出从无效电平转换为有效电平时,捕获 1 由 ST0CH0_O 触发。该位仅在 Slave_TIMER0 中保留。0: ST0CH0_O 输出无效到有效的变化不触发捕获 1。1: ST0CH0_O 输出无效到有效的变化触发捕获 1。</td></tr><tr><td>11</td><td>CP1BEXEV9</td><td>外部事件 9 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>10</td><td>CP1BEXEV8</td><td>外部事件 8 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>9</td><td>CP1BEXEV7</td><td>外部事件 7 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>8</td><td>CP1BEXEV6</td><td>外部事件 6 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>7</td><td>CP1BEXEV5</td><td>外部事件 5 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>6</td><td>CP1BEXEV4</td><td>外部事件 4 触发捕获 1请参考 CP1BEXEV0 描述。</td></tr><tr><td>5</td><td>CP1BEXEV3</td><td>外部事件3触发捕获1请参考CP1BEXEV0描述。</td></tr><tr><td>4</td><td>CP1BEXEV2</td><td>外部事件2触发捕获1请参考CP1BEXEV0描述。</td></tr><tr><td>3</td><td>CP1BEXEV1</td><td>外部事件1触发捕获1请参考CP1BEXEV0描述。</td></tr><tr><td>2</td><td>CP1BEXEV0</td><td>外部事件0触发捕获1当该位置1时,外部事件0触发捕获1。0:外部事件0不触发捕获11:外部事件0触发捕获1</td></tr><tr><td>1</td><td>CP1BUP</td><td>更新事件触发捕获1当该位置1时,更新事件触发捕获1。0:更新事件不触发捕获11:更新事件触发捕获1</td></tr><tr><td>0</td><td>CP1BSW</td><td>软件触发捕获1该位由软件置1,硬件自动清零。该位置1时,软件触发捕获1。0:软件不触发捕获11:软件触发捕获1</td></tr></table>

## Slave_TIMERx 通道输出控制寄存器 (SHRTIMER_STxCHOCTL)

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>BMCH1DTI</td><td>CH1CSEN</td><td colspan="2">CH1FLTOS[1:0]</td><td>ISO1</td><td>BMCH1IEN</td><td>CH1P</td><td>保留</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>DLYISCH[2:0]</td><td>DLYISME N</td><td>DTEN</td><td>BMCH1D TI</td><td>CHOCSE N</td><td>CHOFLTOS[1:0]</td><td>ISO0</td><td>BMCH0IE N</td><td>CHOP</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23</td><td>BMCH1DTI</td><td>突发模式中通道1的死区时间在突发模式下,可以在输出进入空闲状态之前插入死区时间。0:输出立即为空闲状态。1:输出在进入空闲状态之前插入死区时间。注意:(1)一旦计数器使能(STxCEN位置1),就不得修改该位。(2)仅在突发模式的空闲模式下,输出空闲状态之一为有效状态(<eq>ISOy = 1</eq>,<eq>y = 0.1</eq>),且死区时间值为正(DTFSPROT位/DTRSPROT位为0)时,才可以设置此位)。</td></tr><tr><td>22</td><td>CH1CSEN</td><td>通道1载波信号模式使能0:通道1载波信号模式禁能。1:通道1载波信号模式使能。注意:一旦计数器使能(STxCEN位置1),就不得修改该位。</td></tr><tr><td>21:20</td><td>CH1FLTOS[1:0]</td><td>通道1故障输出状态该位域配置了故障事件发生时,通道1的输出状态。00:没有影响。发生故障事件时,输出处于运行模式。01:输出为有效电平。10:输出无效电平。11:输出为高阻状态。注意:如果SHRTIMER_STxFLTCTL寄存器中的FLTyEN(<eq>y=0..4</eq>)位置1,或输出处于故障状态,,一旦计数器使能(将STxCEN位置1),就不能修改该位域。</td></tr><tr><td>19</td><td>ISO1</td><td>通道1输出空闲状态0:通道1输出空闲状态为无效电平。1:通道1输出空闲状态为有效电平。注意:必须在SHRTIMER控制输出前,配置该位。</td></tr><tr><td>18</td><td>BMCH1IEN</td><td>在突发模式中使能通道1空闲状态该位用于配置在突发模式下,通道1输出空闲状态。0:通道1输出不受突发模式影响。1:在突发模式下,通道1的输出可以为空闲状态。注意:该位已预加载,可以在运行时更改,但在突发模式下不得更改。</td></tr><tr><td>17</td><td>CH1P</td><td>通道1输出极性该位确定通道1输出信号的极性。0:通道1高电平有效。1:通道1低电平有效。注意:一旦计数器使能(STxCEN位置1),就不得修改该位。</td></tr><tr><td>16:13</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>12:10</td><td>DLYISCH[2:0]</td><td>延迟空闲的源和通道该位域配置了延迟空闲模式(DLYISMEN=1)使能时的源和通道。在SHRTIMER_STyCHOCTL(<eq>y=0,1,2</eq>)寄存器中:000:外部事件5到来时,通道0输出延迟的空闲状态。001:外部事件5到来时,通道1输出延迟的空闲状态。010:外部事件5到来时,通道0和通道1输出延迟的空闲状态。011:在均衡模式下,外部事件5到来时,通道0和通道1输出均衡空闲状态(SHRTIMER_STyCTL0(<eq>y=0,1,2</eq>)寄存器中的BLNMEN=1)。100:外部事件6到来时,通道0输出延迟的空闲状态。101:外部事件6到来时,通道1输出延迟的空闲状态。110:外部事件6到来时,通道0和通道1输出延迟的空闲状态。111:在均衡模式下,外部事件6到来时,通道0和通道1输出均衡空闲状态(SHRTIMER_STyCTL0(y=0,1,2)寄存器中的BLNMEN=1)。在SHRTIMER_STyCHOCTL(y=3,4)寄存器中:000:外部事件7到来时,通道0输出延迟的空闲状态。001:外部事件7到来时,通道1输出延迟的空闲状态。010:外部事件7到来时,通道0和通道1输出延迟的空闲状态。011:在均衡模式下,外部事件7到来时,通道0和通道1输出均衡空闲状态(SHRTIMER_STyCTL0(y=3,4)寄存器中的BLNMEN=1)。100:外部事件8到来时,通道0输出延迟的空闲状态。101:外部事件8到来时,通道1输出延迟的空闲状态。110:外部事件8到来时,通道0和通道1输出延迟的空闲状态。111:在均衡模式下,外部事件8到来时,通道0和通道1输出均衡空闲状态(SHRTIMER_STyCTL0(y=3,4)寄存器中的BLNMEN=1)。注意:一旦延迟空闲模式(DLYISMEN位置1)使能,就不得修改此位域。</td></tr><tr><td>9</td><td>DLYISMEN</td><td>延迟空闲模式使能0:延迟空闲模式禁能1:延迟空闲模式使能注意:一旦计数器使能(STxCEN位置1),就不得修改该位</td></tr><tr><td>8</td><td>DTEN</td><td>死区时间使能0:通道0和通道1的输出是独立的。1:通道0和通道1的输出是互补的,在通道0和通道1的输出之间插入死区时间。注意:一旦计数器使能(STxCEN位置1),或其输出被其他定时器使能和控制,就不得修改该位。</td></tr><tr><td>7</td><td>BMCH0DTI</td><td>突发模式中通道0的死区时间在突发模式下,可以在输出进入空闲状态之前插入死区时间。0:输出立即为空闲状态。1:输出在进入空闲状态之前插入死区时间。注意:(1)一旦计数器使能(STxCEN位置1),就不得修改该位。(2)仅在突发模式的空闲模式下,输出空闲状态之一为有效状态(ISOy=1,y=0,1),且死区时间值为正(DTFSPROT位/DTRSPROT位为0)时,才可以设置此位)。</td></tr><tr><td>6</td><td>CH0CSEN</td><td>通道0载波信号模式使能0:通道0载波信号模式禁能。1:通道0载波信号模式使能。注意:一旦计数器使能(STxCEN位置1),就不得修改该位。</td></tr><tr><td>5:4</td><td>CH0FLTOS[1:0]</td><td>通道0故障输出状态该位域配置了在故障事件发生时,通道0的输出状态。00:没有影响。发生故障事件时,输出处于运行模式。01:输出为有效电平。10:输出无效电平。11:输出为高阻状态。注意:如果SHRTIMER_STxFLTCTL寄存器中的FLTyEN(y=0..4)位置1,或输出处于故障状态,一旦计数器使能(将STxCEN位置1),就不能修改该位域。</td></tr><tr><td>3</td><td>ISO0</td><td>通道0输出空闲状态0:通道0输出空闲状态为无效电平。1:通道0输出空闲状态为有效电平。注意:必须在SHRTIMER控制输出前,配置该位。</td></tr><tr><td>2</td><td>BMCH0IEN</td><td>在突发模式中使能通道0空闲状态该位用于配置在突发模式下,通道0输出空闲状态0:通道0输出不受突发模式影响。1:在突发模式下,通道0的输出可以为空闲状态。注意:该位已预加载,可以在运行时更改,但在突发模式下不得更改。</td></tr><tr><td>1</td><td>CHOP</td><td>通道0输出极性该位确定通道0输出信号的极性。0:通道0高电平有效1:通道0低电平有效注意:一旦计数器使能(STxCEN位置1),就不得修改该位。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## Slave_TIMERx 故障控制寄存器 (SHRTIMER_STxFLTCTL)

地址偏移：0x68

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FLTENPROT</td><td colspan="15">保留</td></tr><tr><td>rwo15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>FLT4EN</td><td>FLT3EN</td><td>FLT2EN</td><td>FLT1EN</td><td>FLT0EN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FLTENPROT</td><td>故障保护使能该位用于使能写保护,该位只能写一次,当它置1时,只能通过系统复位清零。0: 故障保护禁能。<eq>FLTyEN (y=0..4)</eq>可以写操作。1: 故障保护使能。<eq>FLTyEN (y=0..4)</eq>为只读。</td></tr><tr><td>30:5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4</td><td>FLT4EN</td><td>故障4使能0: 故障4禁能1: 故障4使能</td></tr><tr><td>3</td><td>FLT3EN</td><td>故障3使能0: 故障3禁能1: 故障3使能</td></tr><tr><td>2</td><td>FLT2EN</td><td>故障2使能0: 故障2禁能1: 故障2使能</td></tr><tr><td>1</td><td>FLT1EN</td><td>故障1使能0: 故障1禁能1: 故障1使能</td></tr><tr><td>0</td><td>FLT0EN</td><td>故障0使能0: 故障0禁能1: 故障0使能</td></tr></table>

## Slave_TIMERx 附加控制寄存器 (SHRTIMER_STxACTL)

地址偏移：0x7C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">DTFCFG[15:9]</td><td colspan="9">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">DTRCFG[15:9]</td><td colspan="5">保留</td><td>CNTCKDIV[3]</td><td colspan="3">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>DTFCFG[15:9]</td><td>下降沿死区值配置该位域用于配置跟随输出准备信号(OyPRE,y=0,1)下降沿之后的死区时间值。DTF 值 = DTFCFG [15:0] x tSHRTIMER_DTGCK,其中,tSHRTIMER_DTGCK= 1/fSHRTIMER_DTGCK。写入该位域可以更改 DTFCFG [15:0]位域的高7位。注意:(1)当SHRTIMER_STxDTCTL 寄存器中的 DTFSVPROT 位置1时,无法修改此位域。(2)该位是预装载的。</td></tr><tr><td>24:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:9</td><td>DTRCFG[15:9]</td><td>上升沿死区值配置该位域用于配置跟随输出准备信号(OyPRE,y=0,1)上升沿之后的死区时间值。DTR 值=DTRCFG[15:0] x tSHRTIMER_DTGCK,其中,tSHRTIMER_DTGCK= 1/fSHRTIMER_DTGCK。写入该位域可以更改 DTRCFG[15:0]位域的高7位。注意:(1)当SHRTIMER_STxDTCTL寄存器中的DTRSVPROT位置1时,无法修改此位域。(2)该位是预装载的。</td></tr><tr><td>8:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>CNTCKDIV[3]</td><td>计数器时钟分频该位位域由软件配置,确定超高分辨率时钟(SHRTIMER_HPCK)和计数器时钟(SHRTIMER_PSCCK)的分频比。当SHRTIMER_MTACTL中的CNTCKDIV[3]为0时,<eq>f_{SHRTIMER\_PSCCK} = f_{SHRTIMER\_HPCK} / 2^{CNTCKDIV [2:0] + 1}</eq>。当SHRTIMER_MTACTL中的CNTCKDIV[3]位为1且CNTCKDIV[2:0]配置为3'b000时:<eq>f_{SHRTIMER\_PSSCK} = f_{SHRTIMER\_HPCK}</eq>注意:一旦使能定时器,就不能修改CNTCKDIV[3:0]位域。</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 19.5.3. 通用寄存器

SHRTIMER 通用寄存器基地址：0x4001 7780

## SHRTIMER 控制寄存器 0 (SHRTIMER_CTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="3">ADTG3USRC[2:0]</td><td colspan="3">ADTG2USRC [2:0]</td><td colspan="3">ADTG1USRC [2:0]</td><td colspan="3">ADTG0USRC [2:0]</td></tr><tr><td colspan="4"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ST4UPDI S</td><td>ST3UPDI S</td><td>ST2UPDI S</td><td>ST1UPDI S</td><td>ST0UPDI S</td><td>MTUPDI S</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27:25</td><td>ADTG3USRC[2:0]</td><td>SHRTIMER_ADCTRIG3 更新源该位域可以由软件配置,配置 SHRTIMER_ADCTRIGS3 寄存器的更新源。000:Master_TIMER 更新事件001:Slaver_TIMER0 更新事件010:Slaver_TIMER1 更新事件011:Slaver_TIMER2 更新事件100:Slaver_TIMER3 更新事件101:Slaver_TIMER4 更新事件其他值保留。</td></tr><tr><td>24:22</td><td>ADTG2USRC[2:0]</td><td>SHRTIMER_ADCTRIG2 更新源该位域可以由软件配置,配置SHRTIMER_ADCTRIGS2寄存器的更新源。000:Master_TIMER更新事件001:Slaver_TIMER0更新事件010:Slaver_TIMER1更新事件011:Slaver_TIMER2更新事件100:Slaver_TIMER3更新事件101:Slaver_TIMER4更新事件其他值保留。</td></tr><tr><td>21:19</td><td>ADTG1USRC[2:0]</td><td>SHRTIMER_ADCTRIG1 更新源该位域可以由软件配置,配置SHRTIMER_ADCTRIGS1寄存器的更新源。000:Master_TIMER更新事件001:Slaver_TIMER0更新事件010:Slaver_TIMER1更新事件011:Slaver_TIMER2更新事件100:Slaver_TIMER3更新事件101:Slaver_TIMER4更新事件其他值保留。</td></tr><tr><td>18:16</td><td>ADTG0USRC[2:0]</td><td>SHRTIMER_ADCTRIG0 更新源该位域可以由软件配置,配置SHRTIMER_ADCTRIGS0寄存器的更新源。000:Master_TIMER更新事件001:Slaver_TIMER0更新事件010:Slaver_TIMER1更新事件011:Slaver_TIMER2更新事件100:Slaver_TIMER3更新事件101:Slaver_TIMER4更新事件其他值保留。</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>ST4UPDIS</td><td>Slave_TIMER4更新事件禁能该位用于使能或禁能更新事件的生成。0:更新事件使能。1:更新事件禁能。</td></tr><tr><td>4</td><td>ST3UPDIS</td><td>Slave_TIMER3更新事件禁能该位用于使能或禁能更新事件的生成。0:更新事件使能。1:更新事件禁能。</td></tr><tr><td>3</td><td>ST2UPDIS</td><td>Slave_TIMER2更新事件禁能该位用于使能或禁能更新事件的生成。0:更新事件使能。1: 更新事件禁能。</td></tr><tr><td>2</td><td>ST1UPDIS</td><td>Slave_TIMER1 更新事件禁能该位用于使能或禁能更新事件的生成。0: 更新事件使能。1: 更新事件禁能。</td></tr><tr><td>1</td><td>ST0UPDIS</td><td>Slave_TIMER0 更新事件禁能该位用于使能或禁能更新事件的生成。0: 更新事件使能。1: 更新事件禁能。</td></tr><tr><td>0</td><td>MTUPDIS</td><td>Master_TIMER 更新事件禁能该位用于使能或禁能更新事件的生成。0: 更新事件使能。1: 更新事件禁能。</td></tr></table>

## SHRTIMER 控制寄存器 1 (SHRTIMER_CTL1)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>ST4SRST</td><td>ST3SRST</td><td>ST2SRST</td><td>ST1SRST</td><td>ST0SRST</td><td>MTSRST</td><td colspan="2">保留</td><td>ST4SUP</td><td>ST3SUP</td><td>ST2SUP</td><td>ST1SUP</td><td>ST0SUP</td><td>MTSUP</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>ST4SRST</td><td>Slave_TIMER4 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>12</td><td>ST3SRST</td><td>Slave_TIMER3 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>11</td><td>ST2SRST</td><td>Slave_TIMER2 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>10</td><td>ST1SRST</td><td>Slave_TIMER1 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>9</td><td>ST0SRST</td><td>Slave_TIMER0 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>8</td><td>MTSRST</td><td>Master_TIMER 软件复位该位可由软件置位,硬件自动清除。该位置 1 时,计数器复位。0:无影响。1:计数器复位。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>ST4SUP</td><td>Slave_TIMER4 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄存器,并且所有挂起的更新请求都被取消。0:无影响。1:更新生成。</td></tr><tr><td>4</td><td>ST3SUP</td><td>Slave_TIMER3 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄存器,并且所有挂起的更新请求都被取消。0:无影响。1:更新生成。</td></tr><tr><td>3</td><td>ST2SUP</td><td>Slave_TIMER2 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄存器,并且所有挂起的更新请求都被取消。0:无影响。1:更新生成。</td></tr><tr><td>2</td><td>ST1SUP</td><td>Slave_TIMER1 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄存器,并且所有挂起的更新请求都被取消。0:无影响。1:更新生成。</td></tr><tr><td>1</td><td>ST0SUP</td><td>Slave_TIMER0 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄存器,并且所有挂起的更新请求都被取消。0:无影响。1:更新生成。</td></tr><tr><td>0</td><td>MTSUP</td><td>Master_TIMER 软件更新该位可由软件置位,硬件自动清除。该位置 1 时,影子寄存器的内容被传送到有效寄</td></tr></table>

存器，并且所有挂起的更新请求都被取消。

0：无影响。

1：更新生成。

## SHRTIMER 中断标志寄存器 (SHRTIMER_INTF)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>BMPERIF</td><td>DLLCALIF</td></tr><tr><td colspan="16">r r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYSFLTIF</td><td>FLT4IF</td><td>FLT3IF</td><td>FLT2IF</td><td>FLT1IF</td><td>FLT0IF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>BMPERIF</td><td>突发模式周期中断标志突发模式的周期时间到达时,该位由硬件置位。可以通过软件写1清零。0:突发模式周期中断未发生1:突发模式周期中断发生</td></tr><tr><td>16</td><td>DLLCALIF</td><td>DLL校准完成中断标志DLL校准完成后,此标志由硬件置1。可以通过软件写1清零。0: DLL校准完成中断未发生1: DLL校准完成中断发生</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>SYSFLTIF</td><td>系统故障中断标志系统故障发生时,此标志由硬件置1。可以通过软件写1清零。0:系统故障中断未发生1:系统故障中断发生</td></tr><tr><td>4</td><td>FLT4IF</td><td>故障4中断标志请参考FLTOIF描述。</td></tr><tr><td>3</td><td>FLT3IF</td><td>故障3中断标志请参考FLTOIF描述。</td></tr><tr><td>2</td><td>FLT2IF</td><td>故障2中断标志请参考FLTOIF描述。</td></tr><tr><td>1</td><td>FLT1IF</td><td>故障1中断标志</td></tr></table>

<table><tr><td></td><td></td><td>请参考 FLTOIF 描述。</td></tr><tr><td>0</td><td>FLTOIF</td><td>故障 0 中断标志故障 0 发生时,此标志由硬件置 1 。可以通过软件写 1 清零。0: 故障 0 中断未发生1: 故障 0 中断发生</td></tr></table>

## SHRTIMER 中断标志清除寄存器 (SHRTIMER_INTC)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>BMPER IFC</td><td>DLLCAL IFC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYSFLT IFC</td><td>FLT4IFC</td><td>FLT3IFC</td><td>FLT2IFC</td><td>FLT1IFC</td><td>FLT0IFC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>BMPERIFC</td><td>突发模式周期中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的BMPERIF位。0:无影响1:突发模式周期中断标志清除</td></tr><tr><td>16</td><td>DLLCALIFC</td><td>DLL校准完成中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的DLLCALIF位。0:无影响1: DLL校准完成中断标志清除</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>SYSFLTIFC</td><td>系统故障中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的SYSFLTIF位。0:无影响1:系统故障中断标志清除</td></tr><tr><td>4</td><td>FLT4IFC</td><td>故障4中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的FLT4IF位。0:无影响1:故障4中断标志清除</td></tr><tr><td>3</td><td>FLT3IFC</td><td>故障3中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的FLT3IF位。0:无影响1:故障3中断标志清除</td></tr><tr><td>2</td><td>FLT2IFC</td><td>故障2中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的FLT2IF位。0:无影响1:故障2中断标志清除</td></tr><tr><td>1</td><td>FLT1IFC</td><td>故障1中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的FLT1IF位。0:无影响1:故障1中断标志清除</td></tr><tr><td>0</td><td>FLT0IFC</td><td>故障0中断标志清除该位软件写1可以清零SHRTIMER_INTF寄存器中的FLT0IF位。0:无影响1:故障0中断标志清除</td></tr></table>

## SHRTIMER 中断使能寄存器 (SHRTIMER_INTEN)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>BMPERIE</td><td>DLLCALI E</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYSFLTI E</td><td>FLT4IE</td><td>FLT3IE</td><td>FLT2IE</td><td>FLT1IE</td><td>FLT0IE</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>BMPERIE</td><td>突发模式周期中断使能0:禁能1:使能</td></tr><tr><td>16</td><td>DLLCALIE</td><td>DLL 校准完成中断使能0:禁能1:使能</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>SYSFLTIE</td><td>系统故障中断使能0: 禁能1: 使能</td></tr><tr><td>4</td><td>FLT4IE</td><td>故障 4 中断使能请参考 FLT0IE 描述</td></tr><tr><td>3</td><td>FLT3IE</td><td>故障 3 中断使能请参考 FTOIE 描述</td></tr><tr><td>2</td><td>FLT2IE</td><td>故障 2 中断使能请参考 FTOIE 描述</td></tr><tr><td>1</td><td>FLT1IE</td><td>故障 1 中断使能请参考 FTOIE 描述</td></tr><tr><td>0</td><td>FLT0IE</td><td>故障 0 中断使能0: 禁能1: 使能</td></tr></table>

## SHRTIMER 通道输出使能寄存器 (SHRTIMER_CHOUTEN)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>ST4CH1EN</td><td>ST4CH0EN</td><td>ST3CH1EN</td><td>ST3CH0EN</td><td>ST2CH1EN</td><td>ST2CH0EN</td><td>ST1CH1EN</td><td>ST1CH0EN</td><td>ST0CH1EN</td><td>ST0CH0EN</td></tr><tr><td colspan="6"></td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>ST4CH1EN</td><td>Slave_TIMER4通道1输出(ST4CH1_O)使能请参考ST0CH0EN描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF寄存器中的ST4CH1DISF位配置。</td></tr><tr><td>8</td><td>ST4CH0EN</td><td>Slave_TIMER4通道0输出(ST4CH0_O)使能请参考ST0CH0EN描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF寄存器中的ST4CH0DISF位配置。</td></tr><tr><td>7</td><td>ST3CH1EN</td><td>Slave_TIMER3通道1输出(ST3CH1_O)使能请参考ST0CH0EN描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF寄存器中的ST3CH1DISF 位配置。</td></tr><tr><td>6</td><td>ST3CH0EN</td><td>Slave_TIMER3 通道 0 输出(ST3CH0_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST3CH0DISF 位配置。</td></tr><tr><td>5</td><td>ST2CH1EN</td><td>Slave_TIMER2 通道 1 输出(ST2CH1_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST2CH1DISF 位配置。</td></tr><tr><td>4</td><td>ST2CH0EN</td><td>Slave_TIMER2 通道 0 输出(ST2CH0_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST2CH0DISF 位配置。</td></tr><tr><td>3</td><td>ST1CH1EN</td><td>Slave_TIMER1 通道 1 输出(ST1CH1_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST1CH1DISF 位配置。</td></tr><tr><td>2</td><td>ST1CH0EN</td><td>Slave_TIMER1 通道 0 输出(ST1CH0_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST1CH0DISF 位配置。</td></tr><tr><td>1</td><td>ST0CH1EN</td><td>Slave_TIMER0 通道 1 输出(ST0CH1_O)使能请参考 ST0CH0EN 描述。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST0CH1DISF 位配置。</td></tr><tr><td>0</td><td>ST0CH0EN</td><td>Slave_TIMER0 通道 0 输出(ST0CH0_O)使能该位写 1 使能输出,写 0 无影响。故障输入有效时,该位由硬件异步清除。读该位内容,将返回输出使能或禁能的状态。0: Slave_TIMER0 通道 0 输出 ST0CH0_O 禁能。输出处于故障状态或空闲状态。1: Slave_TIMER0 通道 0 输出 ST0CH0_O 使能。注意:禁能状态对应空闲和故障状态,由SHRTIMER_CHOUTDISF 寄存器中的 ST0CH0DISF 位配置。</td></tr></table>

## SHRTIMER 通道输出禁能寄存器 (SHRTIMER_CHOUTDIS)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>ST4CH1DIS</td><td>ST4CH0DIS</td><td>ST3CH1DIS</td><td>ST3CH0DIS</td><td>ST2CH1DIS</td><td>ST2CH0DIS</td><td>ST1CH1DIS</td><td>ST1CH0DIS</td><td>ST0CH1DIS</td><td>ST0CH0DIS</td></tr><tr><td colspan="6"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>ST4CH1DIS</td><td>Slave_TIMER4通道1输出(ST4CH1_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>8</td><td>ST4CH0DIS</td><td>Slave_TIMER4通道0输出(ST4CH0_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>7</td><td>ST3CH1DIS</td><td>Slave_TIMER3通道1输出(ST3CH1_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>6</td><td>ST3CH0DIS</td><td>Slave_TIMER3通道0输出(ST3CH0_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>5</td><td>ST2CH1DIS</td><td>Slave_TIMER2通道1输出(ST2CH1_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>4</td><td>ST2CH0DIS</td><td>Slave_TIMER2通道0输出(ST2CH0_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>3</td><td>ST1CH1DIS</td><td>Slave_TIMER1通道1输出(ST1CH1_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>2</td><td>ST1CH0DIS</td><td>Slave_TIMER1通道0输出(ST1CH0_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>1</td><td>ST0CH1DIS</td><td>Slave_TIMER0通道1输出(ST0CH1_O)禁能请参考ST0CH0DIS描述。</td></tr><tr><td>0</td><td>ST0CH0DIS</td><td>Slave_TIMER1通道0输出(ST1CH0_O)禁能该位写1禁能输出,通道0进入空闲状态。写0无影响。0:无影响。1:Slave_TIMER1通道0输出ST0CH0_O禁能。输出从故障状态或运行状态进入空闲状态。</td></tr></table>

SHRTIMER 通道输出禁能标志寄存器 (SHRTIMER_CHOUTDISF)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>ST4CH1DISF</td><td>ST4CH0DISF</td><td>ST3CH1DISF</td><td>ST3CH0DISF</td><td>ST2CH1DISF</td><td>ST2CH0DISF</td><td>ST1CH1DISF</td><td>ST1CH0DISF</td><td>ST0CH1DISF</td><td>ST0CH0DISF</td></tr><tr><td colspan="6"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>ST4CH1DISF</td><td>Slave_TIMER4 通道 1 输出(ST4CH1_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>8</td><td>ST4CH0DISF</td><td>Slave_TIMER4 通道 0 输出(ST4CH0_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>7</td><td>ST3CH1DISF</td><td>Slave_TIMER3 通道 1 输出(ST3CH1_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>6</td><td>ST3CH0DISF</td><td>Slave_TIMER3 通道 0 输出(ST3CH0_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>5</td><td>ST2CH1DISF</td><td>Slave_TIMER2 通道 1 输出(ST2CH1_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>4</td><td>ST2CH0DISF</td><td>Slave_TIMER2 通道 0 输出(ST2CH0_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>3</td><td>ST1CH1DISF</td><td>Slave_TIMER1 通道 1 输出(ST1CH1_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>2</td><td>ST1CH0DISF</td><td>Slave_TIMER1 通道 0 输出(ST1CH0_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>1</td><td>ST0CH1DISF</td><td>Slave_TIMER0 通道 1 输出(ST0CH1_O)禁能标志请参考 ST0CH0DISF 描述。</td></tr><tr><td>0</td><td>ST0CH0DISF</td><td>Slave_TIMER0 通道 0 输出(ST0CH0_O)禁能标志读该位内容,将返回通道 0 输出禁能状态。输出使能时无效。0:空闲状态下,Slave_TIMER0 通道 0 输出 ST0CH0_O 禁能。1:故障状态下,Slave_TIMER0 通道 0 输出 ST0CH0_O 禁能。</td></tr></table>

SHRTIMER 突发模式控制寄存器 (SHRTIMER_BMCTL)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BMOPTF</td><td colspan="9">保留</td><td>BMST4</td><td>BMST3</td><td>BMST2</td><td>BMST1</td><td>BMST0</td><td>BMMT</td></tr><tr><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>BMSE</td><td colspan="4">BMPSC[3:0]</td><td colspan="4">BMCLKS[3:0]</td><td>BMCTN</td><td>BMEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BMOPTF</td><td>突发模式运行标志突发模式正在运行时,该标志位由硬件置位。该位写0将停止突发模式。0:常规运行,突发模式不起作用。1:突发模式正在进行。</td></tr><tr><td>30:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21</td><td>BMST4</td><td>Slave_TIMER4 突发模式0: Slave_TIMER4 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Slave_TIMER4 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。注意:(1)突发模式使能时,无法更改此位。(2)当均衡空闲模式有效(SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH [2:0] = 3'bx11)时,不能将此位置位。</td></tr><tr><td>20</td><td>BMST3</td><td>Slave_TIMER3 突发模式0: Slave_TIMER3 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Slave_TIMER3 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。注意:(1)突发模式使能时,无法更改此位。(2)当均衡空闲模式有效(SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH [2:0] = 3'bx11)时,不能将此位置位。</td></tr><tr><td>19</td><td>BMST2</td><td>Slave_TIMER2 突发模式0: Slave_TIMER2 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Slave_TIMER2 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。注意:(1)突发模式使能时,无法更改此位。(2)当均衡空闲模式有效(SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH [2:0] = 3'bx11)时,不能将此位置位。</td></tr><tr><td>18</td><td>BMST1</td><td>Slave_TIMER1 突发模式0: Slave_TIMER1 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Slave_TIMER1 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。注意:(1)突发模式使能时,无法更改此位。(2)当均衡空闲模式有效(SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH [2:0] = 3'bx11)时,不能将此位置位。</td></tr><tr><td>17</td><td>BMST0</td><td>Slave_TIMER0 突发模式0: Slave_TIMER0 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Slave_TIMER0 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。注意:(1)突发模式使能时,无法更改此位。(2)当均衡空闲模式有效(SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH [2:0] = 3'bx11)时,不能将此位置位。</td></tr><tr><td>16</td><td>BMMT</td><td>Master_TIMER 突发模式0: Master_TIMER 计数器时钟(SHRTIMER_PSCCK)保持,且计数器正常运行。1: Master_TIMER 计数器时钟(SHRTIMER_PSCCK)停止,且计数器复位。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10</td><td>BMSE</td><td>突发模式影子寄存器使能0: SHRTIMER_BMCMPV 和 SHRTIMER_BMCAR 寄存器的影子寄存器禁能。1: SHRTIMER_BMCMPV 和 SHRTIMER_BMCAR 寄存器的影子寄存器使能。注意:突发模式使能时不能更改此位。</td></tr><tr><td>9:6</td><td>BMPSC[3:0]</td><td>突发模式时钟分频该位域可以由软件配置,当SHRTIMER_BMCTL 寄存器中的 BMCLKS [3:0] = 4'b1010 时,确定超高分辨率时钟(SHRTIMER_HPCK)和突发模式计数器时钟(SHRTIMER_BMCNTCK)的分频比.<eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/2^{BMPSC[3:0]}</eq>0000: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}</eq>0001: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/2</eq>0010: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/4</eq>0011: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/8</eq>0100: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/16</eq>0101: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/32</eq>0110: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/64</eq>0111: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/128</eq>1000: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/256</eq>1001: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/512</eq>1010: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/1024</eq>1011: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/2048</eq>1100: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/4096</eq>1101: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/8192</eq>1110: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/16384</eq>1111: <eq>f_{SHRTIMER\_BMCNTCK} = f_{SHRTIMER\_CK}/32768</eq>注意:突发模式使能时,该位不能修改。</td></tr><tr><td></td><td></td><td>0011: Slave_TIMER2 计数器复位/翻转事件。0100: Slave_TIMER3 计数器复位/翻转事件。0101: Slave_TIMER4 计数器复位/翻转事件。0110: 芯片内部信号 0, BMCLK0。0111: 芯片内部信号 1, BMCLK1。1000: 芯片内部信号 2, BMCLK2。1001: 芯片内部信号 3, BMCLK3。1010: FSHRTIMER_CK时钟预分频(根据 BMPRSC [3:0]设置)。其他值保留。注意:(1)突发模式使能时,无法更改此位(2)BMCLKy (y = 0..3):请参考表19-14. 突发模式的芯片内部信号。</td></tr><tr><td>1</td><td>BMCTN</td><td>突发模式下的连续模式0: 单脉冲模式。BM计数器达到SHRTIMER_BMCAR值时,由硬件停止。1: 连续模式。BM计数器达到SHRTIMER_BMCAR值时,翻转到零并连续计数。</td></tr><tr><td>0</td><td>BMEN</td><td>突发模式使能该位置1时,突发模式控制器已准备好接收突发模式启动触发。该位写0将终止突发模式。0: 突发模式禁能。1: 突发模式使能。</td></tr></table>

## SHRTIMER 突发模式启动触发寄存器 (SHRTIMER_BMSTRG)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CISGN</td><td>EXEV7</td><td>EXEV6</td><td>ST3EXEV7</td><td>ST0EXEV6</td><td>ST4CMP1</td><td>ST4CMP0</td><td>ST4REP</td><td>ST4RST</td><td>ST3CMP1</td><td>ST3CMP0</td><td>ST3REP</td><td>ST3RST</td><td>ST2CMP1</td><td>ST2CMP0</td><td>ST2REP</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ST2RST</td><td>ST1CMP1</td><td>ST1CMP0</td><td>ST1REP</td><td>ST1RST</td><td>ST0CMP1</td><td>ST0CMP0</td><td>ST0REP</td><td>ST0RST</td><td>MTCMP3</td><td>MTCMP2</td><td>MTCMP1</td><td>MTCMP0</td><td>MTREP</td><td>MTRST</td><td>SWTRG</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CISGN</td><td>芯片内部信号触发突发模式芯片内部信号(TIMER6_TRGO)启动突发模式。0:对突发模式无影响。1:芯片内部信号启动突发模式。</td></tr><tr><td>30</td><td>EXEV7</td><td>外部事件7触发突发模式外部事件7启动突发模式。</td></tr></table>

<table><tr><td></td><td></td><td>0:对突发模式无影响。1:外部事件7启动突发模式。</td></tr><tr><td>29</td><td>EXEV6</td><td>外部事件6触发突发模式外部事件6启动突发模式。0:对突发模式无影响。1:外部事件6启动突发模式。</td></tr><tr><td>28</td><td>ST3EXEV7</td><td>外部事件7之后的Slave_TIMER3周期事件触发突发模式0:对突发模式无影响。1:外部事件7之后的Slave_TIMER3周期事件启动突发模式</td></tr><tr><td>27</td><td>ST0EXEV6</td><td>外部事件6之后的Slave_TIMER0周期事件触发突发模式0:对突发模式无影响。1:外部事件6之后的Slave_TIMER0周期事件启动突发模式</td></tr><tr><td>26</td><td>ST4CMP1</td><td>Slave_TIMER4比较1事件触发突发模式。请参考MTCMP1模式。</td></tr><tr><td>25</td><td>ST4CMP0</td><td>Slave_TIMER4比较0事件触发突发模式。请参考MTCMP0模式。</td></tr><tr><td>24</td><td>ST4REP</td><td>Slave_TIMER4重复事件触发突发模式。请参考MTREP模式。</td></tr><tr><td>23</td><td>ST4RST</td><td>Slave_TIMER4复位事件触发突发模式。请参考MTRST模式。</td></tr><tr><td>22</td><td>ST3CMP1</td><td>Slave_TIMER3比较1事件触发突发模式。请参考MTCMP1模式。</td></tr><tr><td>21</td><td>ST3CMP0</td><td>Slave_TIMER3比较0事件触发突发模式。请参考MTCMP0模式。</td></tr><tr><td>20</td><td>ST3REP</td><td>Slave_TIMER3重复事件触发突发模式。请参考MTREP模式。</td></tr><tr><td>19</td><td>ST3RST</td><td>Slave_TIMER3复位事件触发突发模式。请参考MTRST模式。</td></tr><tr><td>18</td><td>ST2CMP1</td><td>Slave_TIMER2比较1事件触发突发模式。请参考MTCMP1模式。</td></tr><tr><td>17</td><td>ST2CMP0</td><td>Slave_TIMER2比较0事件触发突发模式。请参考MTCMP0模式。</td></tr><tr><td>16</td><td>ST2REP</td><td>Slave_TIMER2重复事件触发突发模式。请参考MTREP模式。</td></tr><tr><td>15</td><td>ST2RST</td><td>Slave_TIMER2复位事件触发突发模式。请参考MTRST模式。</td></tr></table>

<table><tr><td>14</td><td>ST1CMP1</td><td>Slave_TIMER1 比较 1 事件触发突发模式。请参考 MTCMP1 模式。</td></tr><tr><td>13</td><td>ST1CMP0</td><td>Slave_TIMER1 比较 0 事件触发突发模式。请参考 MTCMP0 模式。</td></tr><tr><td>12</td><td>ST1REP</td><td>Slave_TIMER1 重复事件触发突发模式。请参考 MTREP 模式。</td></tr><tr><td>11</td><td>ST1RST</td><td>Slave_TIMER1 复位事件触发突发模式。请参考 MTRST 模式。</td></tr><tr><td>10</td><td>ST0CMP1</td><td>Slave_TIMER0 比较 1 事件触发突发模式。请参考 MTCMP1 模式。</td></tr><tr><td>9</td><td>ST0CMP0</td><td>Slave_TIMER0 比较 0 事件触发突发模式。请参考 MTCMP0 模式。</td></tr><tr><td>8</td><td>ST0REP</td><td>Slave_TIMER0 重复事件触发突发模式。请参考 MTREP 模式。</td></tr><tr><td>7</td><td>ST0RST</td><td>Slave_TIMER0 复位事件触发突发模式。请参考 MTRST 模式。</td></tr><tr><td>6</td><td>MTCMP3</td><td>Master_TIMER 比较 3 事件触发突发模式。请参考 MTCMP0 模式。</td></tr><tr><td>5</td><td>MTCMP2</td><td>Master_TIMER 比较 2 事件触发突发模式。请参考 MTCMP0 模式。</td></tr><tr><td>4</td><td>MTCMP1</td><td>Master_TIMER 比较 1 事件触发突发模式。请参考 MTCMP0 模式。</td></tr><tr><td>3</td><td>MTCMP0</td><td>Master_TIMER 比较 0 事件触发突发模式。0:对突发模式无影响。1:Master_TIMER 比较 0 事件启动突发模式。</td></tr><tr><td>2</td><td>MTREP</td><td>Master_TIMER 重复事件触发突发模式。0:对突发模式无影响。1:Master_TIMER 重复事件启动突发模式。</td></tr><tr><td>1</td><td>MTRST</td><td>Master_TIMER 复位事件触发突发模式。0:对突发模式无影响。1:Master_TIMER 复位事件启动突发模式。</td></tr><tr><td>0</td><td>SWTRG</td><td>软件触发突发模式该位由软件置 1 ,硬件自动清零。该位置 1 时,触发突发模式。如果突发模式未使能,则该位无效(SHRTIMER_BMCTL 寄存器中的 BMEN 位复位)。0:对突发模式无影响。1:软件触发启动突发模式。注意:如果突发模式未使能(BMEN 位复位),则此位无效。</td></tr></table>

## SHRTIMER 突发模式比较值寄存器 (SHRTIMER_BMCMPV)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BMCMPVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>BMCMPVAL[15:0]</td><td>突发模式比较值该位域包含了与BM计数器进行比较的值,并定义了空闲的持续时间。该寄存器有影子寄存器,可以进行预装载。注意:当预分频系数为0,<eq>f_{SHRTIMER\_CK}</eq>时钟直接作为突发模式时钟源(BMCLKS [3:0] = 4&#x27;b1010和BMPSC [3:0] = 4)时,BMCMPVAL[15:0]不能设置为0x0000。</td></tr></table>

## SHRTIMER 突发模式计数器自动重载寄存器 (SHRTIMER_BMCAR)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BMCARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>BMCARL[15:0]</td><td>突发模式计数器自动重载值该位域配置了BM计数器的自动重载值,并定义了突发模式的周期,该周期是空闲状态和运行状态持续的时间之和。该寄存器具有影子寄存器,可以进行预加载。注意:突发模式使能时,该位域不能为零。</td></tr></table>

## SHRTIMER 外部事件配置寄存器 0 (SHRTIMER_EXEVCFG0)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="2">EXEV4EG[1:0]</td><td>EXEV4P</td><td colspan="2">EXEV4SRC[1:0]</td><td>保留</td><td colspan="2">EXEV3EG[1:0]</td><td>EXEV3P</td><td colspan="2">EXEV3SRC[1:0]</td><td>保留</td><td>EXEV2EG[1]</td></tr><tr><td colspan="5">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV2EG[0]</td><td>EXEV2P</td><td colspan="2">EXEV2SRC[1:0]</td><td>保留</td><td colspan="2">EXEV1EG[1:0]</td><td>EXEV1P</td><td colspan="2">EXEV1SRC[1:0]</td><td>保留</td><td colspan="2">EXEV0EG[1:0]</td><td>EXEV0P</td><td colspan="2">EXEV0SRC[1:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28:27</td><td>EXEV4EG[1:0]</td><td>外部事件 4 有效沿请参考 EXEV0EG [1:0]说明。</td></tr><tr><td>26</td><td>EXEV4P</td><td>外部事件 4 极性请参考 EXEV0P 说明。</td></tr><tr><td>25:24</td><td>EXEV4SRC[1:0]</td><td>外部事件 4 的源请参考 EXEV0SRC[1:0]说明。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:21</td><td>EXEV3EG[1:0]</td><td>外部事件 3 有效沿请参考 EXEV0EG [1:0]说明。</td></tr><tr><td>20</td><td>EXEV3P</td><td>外部事件 3 极性请参考 EXEV0P 说明。</td></tr><tr><td>19:18</td><td>EXEV3SRC[1:0]</td><td>外部事件 3 的源请参考 EXEV0SRC[1:0]说明。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16:15</td><td>EXEV2EG[1:0]</td><td>外部事件 2 有效沿请参考 EXEV0EG [1:0]说明。</td></tr><tr><td>14</td><td>EXEV2P</td><td>外部事件 2 极性请参考 EXEV0P 说明。</td></tr><tr><td>13:12</td><td>EXEV2SRC[1:0]</td><td>外部事件 2 的源请参考 EXEV0SRC[1:0]说明。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值</td></tr></table>

<table><tr><td>10:9</td><td>EXEV1EG[1:0]</td><td>外部事件1有效沿请参考EXEV0EG [1:0]说明。</td></tr><tr><td>8</td><td>EXEV1P</td><td>外部事件1极性请参考EXEV0P说明。</td></tr><tr><td>7:6</td><td>EXEV1SRC[1:0]</td><td>外部事件1的源请参考EXEV0SRC[1:0]说明。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:3</td><td>EXEV0EG[1:0]</td><td>外部事件0有效沿该位域配置了外部事件0的有效沿。00:电平有效。有效电平由EXEV0P位定义。01:上升沿有效,EXEV0P位无效。10:下降沿有效,EXEV0P位无效11:上升沿和下降沿均有效,EXEV0P位无效。</td></tr><tr><td>2</td><td>EXEV0P</td><td>外部事件0的极性当EXEV0EG [1:0] = 2&#x27;b00时,该位确定了外部事件0的有效电平。0:外部事件0高电平有效。1:外部事件0低电平有效。注意:一旦Slave_TIMERx使能,就不能更改该位。</td></tr><tr><td>1:0</td><td>EXEV0SRC[1:0]</td><td>外部事件0的源00:外部事件0的源为EXEV0SRC 0。01:外部事件0的源为EXEV0SRC 1。10:外部事件0的源为EXEV0SRC 2。11:外部事件0的源为EXEV0SRC 3。注意:一旦Slave_TIMERx使能,就不能更改该位。</td></tr></table>

## SHRTIMER 外部事件配置寄存器 1 (SHRTIMER_EXEVCFG1)

地址偏移：0x34

复位值：0x0000 0000


该寄存器只能进行字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="2">EXEV9EG[1:0]</td><td>EXEV9P</td><td colspan="2">EXEV9SRC[1:0]</td><td>保留</td><td colspan="2">EXEV8EG[1:0]</td><td>EXEV8P</td><td colspan="2">EXEV8SRC[1:0]</td><td>保留</td><td>EXEV7EG[1]</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>EXEV7EG[0]</td><td>EXEV7P</td><td colspan="2">EXEV7SRC[1:0]</td><td>保留</td><td colspan="2">EXEV6EG[1:0]</td><td>EXEV6P</td><td colspan="2">EXEV6SRC[1:0]</td><td>保留</td><td colspan="2">EXEV5EG[1:0]</td><td>EXEV5P</td><td colspan="2">EXEV5SRC[1:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28:27</td><td>EXEV9EG[1:0]</td><td>外部事件9有效沿请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0EG[1:0]位域说明。</td></tr><tr><td>26</td><td>EXEV9P</td><td>外部事件9极性请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0P位说明。</td></tr><tr><td>25:24</td><td>EXEV9SRC[1:0]</td><td>外部事件9的源请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0SRC[1:0]位域说明。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:21</td><td>EXEV8EG[1:0]</td><td>外部事件8有效沿请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0EG[1:0]位域说明。</td></tr><tr><td>20</td><td>EXEV8P</td><td>外部事件8极性请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0P位说明。</td></tr><tr><td>19:18</td><td>EXEV8SRC[1:0]</td><td>外部事件8的源请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0SRC[1:0]位域说明。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16:15</td><td>EXEV7EG[1:0]</td><td>外部事件7有效沿请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0EG[1:0]位域说明。</td></tr><tr><td>14</td><td>EXEV7P</td><td>外部事件7极性请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0P位说明。</td></tr><tr><td>13:12</td><td>EXEV7SRC[1:0]</td><td>外部事件7的源请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0SRC[1:0]位域说明。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10:9</td><td>EXEV6EG[1:0]</td><td>外部事件6有效沿请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0EG[1:0]位域说明。</td></tr><tr><td>8</td><td>EXEV6P</td><td>外部事件6极性请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0P位说明。</td></tr><tr><td>7:6</td><td>EXEV6SRC[1:0]</td><td>外部事件6的源请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0SRC[1:0]位域说明。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4:3</td><td>EXEV5EG[1:0]</td><td>外部事件5有效沿请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0EG[1:0]位域说明。</td></tr><tr><td>2</td><td>EXEV5P</td><td>外部事件5极性请参考SHRTIMER_EXEVCFG0寄存器中的EXEV0P位说明。</td></tr><tr><td>1:0</td><td>EXEV5SRC[1:0]</td><td>外部事件5的源</td></tr></table>

请参考 SHRTIMER_EXEVCFG0 寄存器中的 EXEV0SRC[1:0]位域说明。

## SHRTIMER 外部事件数字滤波控制寄存器 (SHRTIMER_EXEVDFCTL)

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">EXEVFDIV[1:0]</td><td colspan="2">保留</td><td colspan="4">EXEV9FC[3:0]</td><td colspan="2">保留</td><td colspan="4">EXEV8FC[3:0]</td><td colspan="2">保留</td></tr><tr><td colspan="4">rw</td><td colspan="6">rw</td><td colspan="6">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXEV7FC[3:0]</td><td colspan="2">保留</td><td colspan="4">EXEV6FC[3:0]</td><td colspan="2">保留</td><td colspan="4">EXEV5FC[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="6">rw</td><td colspan="6">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>EXEVFDIV[1:0]</td><td>外部事件数字滤波器时钟分频该位域由软件配置,确定SHRTIMER时钟(SHRTIMER_CK)和外部事件数字滤波器时钟(SHRTIMER_EXEVFCK)之间的分频比。<eq>f_{SHRTIMER\_EXEVFCK} = f_{SHRTIMER\_CK}/2^{EXEVFDIV[2:0]}</eq>。00:<eq>f_{SHRTIMER\_EXEVFCK} = f_{SHRTIMER\_CK}</eq>。01:<eq>f_{SHRTIMER\_EXEVFCK} = f_{SHRTIMER\_CK}/2</eq>。10:<eq>f_{SHRTIMER\_EXEVFCK} = f_{SHRTIMER\_CK}/4</eq>。11:<eq>f_{SHRTIMER\_EXEVFCK} = f_{SHRTIMER\_CK}/8</eq>。</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27:24</td><td>EXEV9FC[3:0]</td><td>外部事件9滤波控制请参考EXEV5FC [3:0]说明。</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21:18</td><td>EXEV8FC[3:0]</td><td>外部事件8滤波控制请参考EXEV5FC [3:0]说明。</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:12</td><td>EXEV7FC[3:0]</td><td>外部事件7滤波控制请参考EXEV5FC [3:0]说明。</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9:6</td><td>EXEV6FC[3:0]</td><td>外部事件5滤波控制请参考EXEV5FC [3:0]说明。</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:0</td><td>EXEV5FC[3:0]</td><td>外部事件5滤波控制在数字滤波器中使用事件计数器,N次输入事件后,输出才会发生转变。该位域用于确定采样外部事件的频率(<eq>f_{SAMP}</eq>)以及应用于外部事件的数字滤波器的长度。</td></tr></table>

<table><tr><td>0000:无滤波。</td></tr><tr><td>0001:fSAMP=fSHRTIMER_CK,N=2。</td></tr><tr><td>0010:fSAMP=fSHRTIMER_CK,N=4。</td></tr><tr><td>0011:fSAMP=fSHRTIMER_CK,N=8。</td></tr><tr><td>0100:fSAMP=fSHRTIMER_EXEVFCK/2,N=6。</td></tr><tr><td>0101:fSAMP=fSHRTIMER_EXEVFCK/2,N=8。</td></tr><tr><td>0110:fSAMP=fSHRTIMER_EXEVFCK/4,N=6。</td></tr><tr><td>0111:fSAMP=fSHRTIMER_EXEVFCK/4,N=8。</td></tr><tr><td>1000:fSAMP=fSHRTIMER_EXEVFCK/8,N=6。</td></tr><tr><td>1001:fSAMP=fSHRTIMER_EXEVFCK/8,N=8。</td></tr><tr><td>1010:fSAMP=fSHRTIMER_EXEVFCK/16,N=5。</td></tr><tr><td>1011:fSAMP=fSHRTIMER_EXEVFCK/16,N=6。</td></tr><tr><td>1100:fSAMP=fSHRTIMER_EXEVFCK/16,N=8。</td></tr><tr><td>1101:fSAMP=fSHRTIMER_EXEVFCK/32,N=5。</td></tr><tr><td>1110:fSAMP=fSHRTIMER_EXEVFCK/32,N=6。</td></tr><tr><td>1111:fSAMP=fSHRTIMER_EXEVFCK/32,N=8。</td></tr></table>

## SHRTIMER ADC 触发源 0 寄存器 (SHRTIMER_ADCTRIGS0)

地址偏移：0x3C

复位值：0x0000 0000


该寄存器只能进行字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRG0ST4PER</td><td>TRG0ST4C3</td><td>TRG0ST4C2</td><td>TRG0ST4C1</td><td>TRG0ST3PER</td><td>TRG0ST3C3</td><td>TRG0ST3C2</td><td>TRG0ST3C1</td><td>TRG0ST2PER</td><td>TRG0ST2C3</td><td>TRG0ST2C2</td><td>TRG0ST2C1</td><td>TRG0ST1RST</td><td>TRG0ST1PER</td><td>TRG0ST1C3</td><td>TRG0ST1C2</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TRG0ST1C1</td><td>TRG0ST0RST</td><td>TRG0ST0PER</td><td>TRG0ST0C3</td><td>TRG0ST0C2</td><td>TRG0ST0C1</td><td>TRG0EXEV4</td><td>TRG0EXEV3</td><td>TRG0EXEV2</td><td>TRG0EXEV1</td><td>TRG0EXEV0</td><td>TRG0MTPER</td><td>TRG0MTC3</td><td>TRG0MTC2</td><td>TRG0MTC1</td><td>TRG0MTC0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRG0ST4PER</td><td>Slave_TIMER4周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周期事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4周期事件生成ADC触发事件。</td></tr><tr><td>30</td><td>TRG0ST4C3</td><td>Slave_TIMER4比较3事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST4C1 描述。</td></tr><tr><td>29</td><td>TRG0ST4C2</td><td>Slave_TIMER4比较2事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST4C1 描述。</td></tr><tr><td>28</td><td>TRG0ST4C1</td><td>Slave_TIMER4比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4比较1事件生成ADC触发事件。</td></tr><tr><td>27</td><td>TRG0ST3PER</td><td>Slave_TIMER3周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周期事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3周期事件生成ADC触发事件。</td></tr><tr><td>26</td><td>TRG0ST3C3</td><td>Slave_TIMER3比较3事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST3C1 描述。</td></tr><tr><td>25</td><td>TRG0ST3C2</td><td>Slave_TIMER3比较2事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST3C1 描述。</td></tr><tr><td>24</td><td>TRG0ST3C1</td><td>Slave_TIMER3比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3比较1事件生成ADC触发事件。</td></tr><tr><td>23</td><td>TRG0ST2PER</td><td>Slave_TIMER2周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周期事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2周期事件生成ADC触发事件。</td></tr><tr><td>22</td><td>TRG0ST2C3</td><td>Slave_TIMER3比较3事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST2C1 描述。</td></tr><tr><td>21</td><td>TRG0ST2C2</td><td>Slave_TIMER3比较2事件生成SHRTIMER_ADCTRIG0请参考 TRG0ST2C1 描述。</td></tr><tr><td>20</td><td>TRG0ST2C1</td><td>Slave_TIMER2比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件是否生成ADC触发事件。0:SHRTIMER Slave_TIMER2比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2比较1事件生成ADC触发事件。</td></tr><tr><td>19</td><td>TRG0ST1RST</td><td>Slave_TIMER1复位事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置生成ADC触发事件。0:SHRTIMER Slave_TIMER1复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1复位事件生成ADC触发事件。</td></tr><tr><td>18</td><td>TRG0ST1PER</td><td>Slave_TIMER1周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周</td></tr></table>
<table><tr><td></td><td></td><td>期事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1周期事件生成ADC触发事件。</td></tr><tr><td>17</td><td>TRG0ST1C3</td><td>Slave_TIMER1比较3事件生成SHRTIMER_ADCTRIG0请参考 TRG0ST1C1 描述。</td></tr><tr><td>16</td><td>TRG0ST1C2</td><td>Slave_TIMER1比较2事件生成SHRTIMER_ADCTRIG0请参考 TRG0ST1C1 描述。</td></tr><tr><td>15</td><td>TRG0ST1C1</td><td>Slave_TIMER1比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1比较1事件生成ADC触发事件。</td></tr><tr><td>14</td><td>TRG0ST0RST</td><td>Slave_TIMER0复位事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置事件是否生成ADC触发事件。0:SHRTIMER Slave_TIMER0复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0复位事件生成ADC触发事件。</td></tr><tr><td>13</td><td>TRG0ST0PER</td><td>Slave_TIMER0周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周期事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0周期事件生成ADC触发事件。</td></tr><tr><td>12</td><td>TRG0ST0C3</td><td>Slave_TIMER0比较3事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST0C1 描述。</td></tr><tr><td>11</td><td>TRG0ST0C2</td><td>Slave_TIMER0比较2事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0ST0C1 描述。</td></tr><tr><td>10</td><td>TRG0ST0C1</td><td>Slave_TIMER0比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0比较1事件生成ADC触发事件。</td></tr><tr><td>9</td><td>TRG0EXEV4</td><td>外部事件4生成生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0EXEV0 描述。</td></tr><tr><td>8</td><td>TRG0EXEV3</td><td>外部事件3生成生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0EXEV0 描述。</td></tr><tr><td>7</td><td>TRG0EXEV2</td><td>外部事件2生成生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考 TRG0EXEV0 描述。</td></tr><tr><td>6</td><td>TRG0EXEV1</td><td>外部事件1生成生成SHRTIMER_ADCTRIG0上的ADC触发事件</td></tr><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRG1ST4RST</td><td>Slave_TIMER4复位事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事</td></tr></table>

<table><tr><td></td><td></td><td>请参考TRG0EXEV0描述。</td></tr><tr><td>5</td><td>TRG0EXEV0</td><td>外部事件0生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:外部事件0(EXEV0C)不生成ADC触发事件。1:外部事件0(EXEV0C)生成ADC触发事件。</td></tr><tr><td>4</td><td>TRG0MTPER</td><td>Master_TIMER周期事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置周期事件生成ADC触发事件。0:SHRTIMER Master_TIMER周期事件不生成ADC触发事件。1:SHRTIMER Master_TIMER周期事件生成ADC触发事件。</td></tr><tr><td>3</td><td>TRG0MTC3</td><td>Master_TIMER比较3事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考TRG0MTC0描述。</td></tr><tr><td>2</td><td>TRG0MTC2</td><td>Master_TIMER比较2事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考TRG0MTC0描述。</td></tr><tr><td>1</td><td>TRG0MTC1</td><td>Master_TIMER比较1事件生成SHRTIMER_ADCTRIG0上的ADC触发事件请参考TRG0MTC0描述。</td></tr><tr><td>0</td><td>TRG0MTC0</td><td>Master_TIMER比较0事件生成SHRTIMER_ADCTRIG0上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG0上生成ADC触发事件。该位用于配置比较1事件生成ADC触发事件。0:SHRTIMER Master_TIMER比较0事件不生成ADC触发事件。1:SHRTIMER Master_TIMER比较0事件生成ADC触发事件。</td></tr></table>

## SHRTIMER ADC 触发源 1 寄存器 (SHRTIMER_ADCTRIGS1)

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRG1ST4RST</td><td>TRG1ST4C3</td><td>TRG1ST4C2</td><td>TRG1ST4C1</td><td>TRG1ST3RST</td><td>TRG1ST3PER</td><td>TRG1ST3C3</td><td>TRG1ST3C2</td><td>TRG1ST3C1</td><td>TRG1ST2RST</td><td>TRG1ST2PER</td><td>TRG1ST2C3</td><td>TRG1ST2C2</td><td>TRG1ST2C1</td><td>TRG1ST1PER</td><td>TRG1ST1C3</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TRG1ST1C2</td><td>TRG1ST1C1</td><td>TRG1ST0PER</td><td>TRG1ST0C3</td><td>TRG1ST0C2</td><td>TRG1ST0C1</td><td>TRG1EXEV9</td><td>TRG1EXEV8</td><td>TRG1EXEV7</td><td>TRG1EXEV6</td><td>TRG1EXEV5</td><td>TRG1MTPER</td><td>TRG1MTC3</td><td>TRG1MTC2</td><td>TRG1MTC1</td><td>TRG1MTC0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td></td><td></td><td>件生成ADC触发事件。0:SHRTIMER Slave_TIMER4复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4复位事件生成ADC触发事件。</td></tr><tr><td>30</td><td>TRG1ST4C3</td><td>Slave_TIMER4比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST4C1 描述。</td></tr><tr><td>29</td><td>TRG1ST4C2</td><td>Slave_TIMER4比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST4C1 描述。</td></tr><tr><td>28</td><td>TRG1ST4C1</td><td>Slave_TIMER4比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于确定事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4比较1事件生成ADC触发事件。</td></tr><tr><td>27</td><td>TRG1ST3RST</td><td>Slave_TIMER3复位事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3复位事件生成ADC触发事件。</td></tr><tr><td>26</td><td>TRG1ST3PER</td><td>Slave_TIMER3周期事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3周期事件生成ADC触发事件。</td></tr><tr><td>25</td><td>TRG1ST3C3</td><td>Slave_TIMER3比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST3C1 描述。</td></tr><tr><td>24</td><td>TRG1ST3C2</td><td>Slave_TIMER3比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST3C1 描述。</td></tr><tr><td>23</td><td>TRG1ST3C1</td><td>Slave_TIMER3比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3比较1事件生成ADC触发事件。</td></tr><tr><td>22</td><td>TRG1ST2RST</td><td>Slave_TIMER2复位事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2复位事件生成ADC触发事件。</td></tr><tr><td>21</td><td>TRG1ST2PER</td><td>Slave_TIMER2周期事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER2周期事件不生成ADC触发事件。1: SHRTIMER Slave_TIMER2周期事件生成ADC触发事件。</td></tr><tr><td>20</td><td>TRG1ST2C3</td><td>Slave_TIMER2比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST2C1 描述。</td></tr><tr><td>19</td><td>TRG1ST2C2</td><td>Slave_TIMER2比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST2C1 描述。</td></tr><tr><td>18</td><td>TRG1ST2C1</td><td>Slave_TIMER2比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER2比较1事件不生成ADC触发事件。1: SHRTIMER Slave_TIMER2比较1事件生成ADC触发事件。</td></tr><tr><td>17</td><td>TRG1ST1PER</td><td>Slave_TIMER1周期事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER1周期事件不生成ADC触发事件。1: SHRTIMER Slave_TIMER1周期事件生成ADC触发事件。</td></tr><tr><td>16</td><td>TRG1ST1C3</td><td>Slave_TIMER1比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST1C1 描述。</td></tr><tr><td>15</td><td>TRG1ST1C2</td><td>Slave_TIMER1比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST1C1 描述。</td></tr><tr><td>14</td><td>TRG1ST1C1</td><td>Slave_TIMER1比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER1比较1事件不生成ADC触发事件。1: SHRTIMER Slave_TIMER1比较1事件生成ADC触发事件。</td></tr><tr><td>13</td><td>TRG1ST0PER</td><td>Slave_TIMER0周期事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER0周期事件不生成ADC触发事件。1: SHRTIMER Slave_TIMER0周期事件生成ADC触发事件。</td></tr><tr><td>12</td><td>TRG1ST0C3</td><td>Slave_TIMER0比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST0C1 描述。</td></tr><tr><td>11</td><td>TRG1ST0C2</td><td>Slave_TIMER0比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1ST0C1 描述。</td></tr><tr><td>10</td><td>TRG1ST0C1</td><td>Slave_TIMER0比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0: SHRTIMER Slave_TIMER0比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0比较1事件生成ADC触发事件。</td></tr><tr><td>9</td><td>TRG1EXEV9</td><td>外部事件9事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1EXEV5 描述。</td></tr><tr><td>8</td><td>TRG1EXEV8</td><td>外部事件8事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1EXEV5 描述。</td></tr><tr><td>7</td><td>TRG1EXEV7</td><td>外部事件7事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1EXEV5 描述。</td></tr><tr><td>6</td><td>TRG1EXEV6</td><td>外部事件6事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考 TRG1EXEV5 描述。</td></tr><tr><td>5</td><td>TRG1EXEV5</td><td>外部事件5生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:外部事件5(EXEV5C)不生成ADC触发事件。1:外部事件5(EXEV5C)生成ADC触发事件。</td></tr><tr><td>4</td><td>TRG1MTPER</td><td>Master_TIMER周期事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Master_TIMER周期事件不生成ADC触发事件。1:SHRTIMER Master_TIMER周期事件生成ADC触发事件。</td></tr><tr><td>3</td><td>TRG1MTC3</td><td>Master_TIMER比较3事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考TRG1MTC0描述。</td></tr><tr><td>2</td><td>TRG1MTC2</td><td>Master_TIMER比较2事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考TRG1MTC0描述。</td></tr><tr><td>1</td><td>TRG1MTC1</td><td>Master_TIMER比较1事件生成SHRTIMER_ADCTRIG1上的ADC触发事件请参考TRG1MTC0描述。</td></tr><tr><td>0</td><td>TRG1MTC0</td><td>Master_TIMER比较0事件生成SHRTIMER_ADCTRIG1上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG1上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Master_TIMER比较0事件不生成ADC触发事件。1:SHRTIMER Master_TIMER比较0事件生成ADC触发事件。</td></tr></table>

## SHRTIMER ADC 触发源 2 寄存器 (SHRTIMER_ADCTRIGS2)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRG2ST4PER</td><td>TRG2ST4C3</td><td>TRG2ST4C2</td><td>TRG2ST4C1</td><td>TRG2ST3PER</td><td>TRG2ST3C3</td><td>TRG2ST3C2</td><td>TRG2ST3C1</td><td>TRG2ST2PER</td><td>TRG2ST2C3</td><td>TRG2ST2C2</td><td>TRG2ST2C1</td><td>TRG2ST1RST</td><td>TRG2ST1PER</td><td>TRG2ST1C3</td><td>TRG2ST1C2</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TRG2ST1C1</td><td>TRG2ST0RST</td><td>TRG2ST0PER</td><td>TRG2ST0C3</td><td>TRG2ST0C2</td><td>TRG2ST0C1</td><td>TRG2EXEV4</td><td>TRG2EXEV3</td><td>TRG2EXEV2</td><td>TRG2EXEV1</td><td>TRG2EXEV0</td><td>TRG2MTPER</td><td>TRG2MTC3</td><td>TRG2MTC2</td><td>TRG2MTC1</td><td>TRG2MTC0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRG2ST4PER</td><td>Slave_TIMER4周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4周期事件生成ADC触发事件。</td></tr><tr><td>30</td><td>TRG2ST4C3</td><td>Slave_TIMER4比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST4C1 描述。</td></tr><tr><td>29</td><td>TRG2ST4C2</td><td>Slave_TIMER4比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST4C1 描述。</td></tr><tr><td>28</td><td>TRG2ST4C1</td><td>Slave_TIMER4比较1事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4比较1事件生成ADC触发事件。</td></tr><tr><td>27</td><td>TRG2ST3PER</td><td>Slave_TIMER3周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3周期事件生成ADC触发事件。</td></tr><tr><td>26</td><td>TRG2ST3C3</td><td>Slave_TIMER3比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST3C1 描述。</td></tr><tr><td>25</td><td>TRG2ST3C2</td><td>Slave_TIMER3比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST3C1 描述。</td></tr><tr><td>24</td><td>TRG2ST3C1</td><td>Slave_TIMER3比较1事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3比较1事件生成ADC触发事件。</td></tr><tr><td>23</td><td>TRG2ST2PER</td><td>Slave_TIMER2周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2周期事件生成ADC触发事件。</td></tr><tr><td>22</td><td>TRG2ST2C3</td><td>Slave_TIMER2比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST2C1 描述。</td></tr><tr><td>21</td><td>TRG2ST2C2</td><td>Slave_TIMER2比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST2C1 描述。</td></tr><tr><td>20</td><td>TRG2ST2C1</td><td>Slave_TIMER2比较1事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2比较1事件生成ADC触发事件。</td></tr><tr><td>19</td><td>TRG2ST1RST</td><td>Slave_TIMER1复位事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1复位事件生成ADC触发事件。</td></tr><tr><td>18</td><td>TRG2ST1PER</td><td>Slave_TIMER1周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1周期事件生成ADC触发事件。</td></tr><tr><td>17</td><td>TRG2ST1C3</td><td>Slave_TIMER1比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST1C1 描述。</td></tr><tr><td>16</td><td>TRG2ST1C2</td><td>Slave_TIMER1比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST1C1 描述。</td></tr><tr><td>15</td><td>TRG2ST1C1</td><td>Slave_TIMER1比较1事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1比较1事件生成ADC触发事件。</td></tr><tr><td>14</td><td>TRG2ST0RST</td><td>Slave_TIMER0复位事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0复位事件生成ADC触发事件。</td></tr><tr><td>13</td><td>TRG2ST0PER</td><td>Slave_TIMER0周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0周期事件上生成ADC触发事件。1:SHRTIMER Slave_TIMER0周期事件上成ADC触发事件。</td></tr><tr><td>12</td><td>TRG2ST0C3</td><td>Slave_TIMER0比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST0C1 描述。</td></tr><tr><td>11</td><td>TRG2ST0C2</td><td>Slave_TIMER0比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2ST0C1 描述。</td></tr><tr><td>10</td><td>TRG2ST0C1</td><td>Slave_TIMER0比较1事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0比较1事件生成ADC触发事件。</td></tr><tr><td>9</td><td>TRG2EXEV4</td><td>外部事件4生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2EXEV0 描述。</td></tr><tr><td>8</td><td>TRG2EXEV3</td><td>外部事件3生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2EXEV0 描述。</td></tr><tr><td>7</td><td>TRG2EXEV2</td><td>外部事件2生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2EXEV0 描述。</td></tr><tr><td>6</td><td>TRG2EXEV1</td><td>外部事件1生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考 TRG2EXEV0 描述。</td></tr><tr><td>5</td><td>TRG2EXEV0</td><td>外部事件0生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:外部事件0(EXEV0C)不生成ADC触发事件。1:外部事件0(EXEV0C)生成ADC触发事件。</td></tr><tr><td>4</td><td>TRG2MTPER</td><td>Master_TIMER周期事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Master_TIMER周期事件不生成ADC触发事件。1:SHRTIMER Master_TIMER周期事件生成ADC触发事件。</td></tr><tr><td>3</td><td>TRG2MTC3</td><td>Master_TIMER比较3事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考TRG2MTC0描述。</td></tr><tr><td>2</td><td>TRG2MTC2</td><td>Master_TIMER比较2事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考TRG2MTC0描述。</td></tr><tr><td>1</td><td>TRG2MTC1</td><td>Master_TIMER比较31事件生成SHRTIMER_ADCTRIG2上的ADC触发事件请参考TRG2MTC0描述。</td></tr><tr><td>0</td><td>TRG2MTC0</td><td>Master_TIMER比较0事件生成SHRTIMER_ADCTRIG2上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG2上生成ADC触发事件。该位用于配置事件生成ADC触发事件。</td></tr></table>

0：SHRTIMER Master_TIMER比较0事件不生成ADC触发事件。

1：SHRTIMER Master_TIMER比较0事件生成ADC触发事件。

## SHRTIMER ADC 触发源 3 寄存器 (SHRTIMER_ADCTRIGS3)

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRG3ST4RST</td><td>TRG3ST4C3</td><td>TRG3ST4C2</td><td>TRG3ST4C1</td><td>TRG3ST3RST</td><td>TRG3ST3PER</td><td>TRG3ST3C3</td><td>TRG3ST3C2</td><td>TRG3ST3C1</td><td>TRG3ST2RST</td><td>TRG3ST2PER</td><td>TRG3ST2C3</td><td>TRG3ST2C2</td><td>TRG3ST2C1</td><td>TRG3ST1PER</td><td>TRG3ST1C3</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TRG3ST1C2</td><td>TRG3ST1C1</td><td>TRG3ST0PER</td><td>TRG3ST0C3</td><td>TRG3ST0C2</td><td>TRG3ST0C1</td><td>TRG3EXEV9</td><td>TRG3EXEV8</td><td>TRG3EXEV7</td><td>TRG3EXEV6</td><td>TRG3EXEV5</td><td>TRG3MTPER</td><td>TRG3MTC3</td><td>TRG3MTC2</td><td>TRG3MTC1</td><td>TRG3MTC0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRG3ST4RST</td><td>Slave_TIMER4复位事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4复位事件生成ADC触发事件。</td></tr><tr><td>30</td><td>TRG3ST4C3</td><td>Slave_TIMER4比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST4C1 描述。</td></tr><tr><td>29</td><td>TRG3ST4C2</td><td>Slave_TIMER4比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST4C1 描述。</td></tr><tr><td>28</td><td>TRG3ST4C1</td><td>Slave_TIMER4比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER4比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER4比较1事件生成ADC触发事件。</td></tr><tr><td>27</td><td>TRG3ST3RST</td><td>Slave_TIMER3复位事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3复位事件生成ADC触发事件。</td></tr><tr><td>26</td><td>TRG3ST3PER</td><td>Slave_TIMER3周期事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3周期事件生成ADC触发事件。</td></tr><tr><td>25</td><td>TRG3ST3C3</td><td>Slave_TIMER3比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST3C1 描述。</td></tr><tr><td>24</td><td>TRG3ST3C2</td><td>Slave_TIMER3比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST3C1 描述。</td></tr><tr><td>23</td><td>TRG3ST3C1</td><td>Slave_TIMER3比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER3比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER3比较1事件生成ADC触发事件。</td></tr><tr><td>22</td><td>TRG3ST2RST</td><td>Slave_TIMER2复位事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2复位事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2复位事件生成ADC触发事件。</td></tr><tr><td>21</td><td>TRG3ST2PER</td><td>Slave_TIMER2周期事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2周期事件生成ADC触发事件。</td></tr><tr><td>20</td><td>TRG3ST2C3</td><td>Slave_TIMER2比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST2C1 描述。</td></tr><tr><td>19</td><td>TRG3ST2C2</td><td>Slave_TIMER2比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST2C1 描述。</td></tr><tr><td>18</td><td>TRG3ST2C1</td><td>Slave_TIMER2比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER2比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER2比较1事件生成ADC触发事件。</td></tr><tr><td>17</td><td>TRG3ST1PER</td><td>Slave_TIMER1周期事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1周期事件生成ADC触发事件。</td></tr><tr><td>16</td><td>TRG3ST1C3</td><td>Slave_TIMER1比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST1C1 描述。</td></tr><tr><td>15</td><td>TRG3ST1C2</td><td>Slave_TIMER1比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST1C1 描述。</td></tr><tr><td>14</td><td>TRG3ST1C1</td><td>Slave_TIMER1比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER1比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER1比较1事件生成ADC触发事件。</td></tr><tr><td>13</td><td>TRG3ST0PER</td><td>Slave_TIMER0周期事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0周期事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0周期事件生成ADC触发事件。</td></tr><tr><td>12</td><td>TRG3ST0C3</td><td>Slave_TIMER0比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST0C1 描述。</td></tr><tr><td>11</td><td>TRG3ST0C2</td><td>Slave_TIMER0比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3ST0C1 描述。</td></tr><tr><td>10</td><td>TRG3ST0C1</td><td>Slave_TIMER0比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Slave_TIMER0比较1事件不生成ADC触发事件。1:SHRTIMER Slave_TIMER0比较1事件生成ADC触发事件。</td></tr><tr><td>9</td><td>TRG3EXEV9</td><td>外部事件9事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3EXEV5 描述。</td></tr><tr><td>8</td><td>TRG3EXEV8</td><td>外部事件8事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3EXEV5 描述。</td></tr><tr><td>7</td><td>TRG3EXEV7</td><td>外部事件7事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3EXEV5 描述。</td></tr><tr><td>6</td><td>TRG3EXEV6</td><td>外部事件6事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考 TRG3EXEV5 描述。</td></tr><tr><td>5</td><td>TRG3EXEV5</td><td>外部事件5生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:外部事件5(EXEV5C)不生成ADC触发事件。1:外部事件5(EXEV5C)生成ADC触发事件。</td></tr><tr><td>4</td><td>TRG3MTPER</td><td>Master_TIMER周期事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Master_TIMER周期事件不生成ADC触发事件。1:SHRTIMER Master_TIMER周期事件生成ADC触发事件。</td></tr><tr><td>3</td><td>TRG3MTC3</td><td>Master_TIMER比较3事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考TRG3MTC0描述。</td></tr><tr><td>2</td><td>TRG3MTC2</td><td>Master_TIMER比较2事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考TRG3MTC0描述。</td></tr><tr><td>1</td><td>TRG3MTC1</td><td>Master_TIMER比较1事件生成SHRTIMER_ADCTRIG3上的ADC触发事件请参考TRG3MTC0描述。</td></tr><tr><td>0</td><td>TRG3MTC0</td><td>Master_TIMER比较0事件生成SHRTIMER_ADCTRIG3上的ADC触发事件SHRTIMER可以在SHRTIMER_ADCTRIG3上生成ADC触发事件。该位用于配置事件生成ADC触发事件。0:SHRTIMER Master_TIMER比较0事件不生成ADC触发事件。1:SHRTIMER Master_TIMER比较0事件生成ADC触发事件。</td></tr></table>

## SHRTIMER DLL 校准控制寄存器 (SHRTIMER_DLLCCTL)

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="2">CLBPER[1:0]</td><td>CLBPEREN</td><td>CLBSTRT</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:2</td><td>CLBPER[1:0]</td><td>DLL 校准周期该位域定义了 DLL 校准周期的长度。00: 1048576 * tSHRTIMER_CK01: 131072 * tSHRTIMER_CK10: 16384 * tSHRTIMER_CK11: 2048 * tSHRTIMER_CK</td></tr><tr><td>1</td><td>CLBPEREN</td><td>DLL 定期校准使能该位用于使能定期的 DLL 校准。CLBPER [1:0]位域用于设置校准周期。0: DLL 定期校准禁能。1: DLL 定期校准使能。注意:不能同时设置 CLBPEREN 位和 CLBSTRT 位。</td></tr></table>

当 CLBPEREN = 0 时，向该位写入 1 将启动 DLL 校准。该位只能进行写操作。

0：无效。

1：DLL 校准开始。

注意：不能同时设置 CLBPEREN 位和 CLBSTRT 位。

## SHRTIMER 故障输入配置寄存器 0 (SHRTIMER_FLTINCFG0)

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FLT3INPROT</td><td></td><td colspan="3">FLT3INFC[3:0]</td><td>FLT3INSRC</td><td>FLT3INP</td><td>FLT3INEN</td><td>FLT2INPROT</td><td></td><td colspan="3">FLT2INFC[3:0]</td><td>FLT2INSRC</td><td>FLT2INP</td><td>FLT2INEN</td></tr><tr><td>rwo</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rwo</td><td></td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FLT1INPROT</td><td></td><td colspan="3">FLT1INFC[3:0]</td><td>FLT1INSRC</td><td>FLT1INP</td><td>FLT1INEN</td><td>FLT0INPROT</td><td></td><td colspan="3">FLT0INFC[3:0]</td><td>FLT0INSRC</td><td>FLT0INP</td><td>FLT0INEN</td></tr><tr><td>rwo</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rwo</td><td></td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FLT3INPROT</td><td>保护故障3输入配置请参考 FLT0INPROT 描述。</td></tr><tr><td>30:27</td><td>FLT3INFC[3:0]</td><td>故障3输入滤波配置请参考 FLT0INFC[3:0]描述。</td></tr><tr><td>26</td><td>FLT3INSRC</td><td>故障3输入源请参考 FLT0INSRC 描述。</td></tr><tr><td>25</td><td>FLT3INP</td><td>故障3输入极性请参考 FLT0INP 描述。</td></tr><tr><td>24</td><td>FLT3INEN</td><td>故障3输入使能请参考 FLT0INEN 描述。</td></tr><tr><td>23</td><td>FLT2INPROT</td><td>保护故障2输入配置请参考 FLT0INPROT 描述。</td></tr><tr><td>22:19</td><td>FLT2INFC[3:0]</td><td>故障3输入滤波控制请参考 FLT0INFC[3:0]描述。</td></tr><tr><td>18</td><td>FLT2INSRC</td><td>故障2输入源请参考 FLT0INSRC 描述。</td></tr><tr><td>17</td><td>FLT2INP</td><td>故障2输入极性请参考 FLT0INP 描述。</td></tr><tr><td>16</td><td>FLT2INEN</td><td>故障 2 输入使能请参考 FLT0INEN 描述。</td></tr><tr><td>15</td><td>FLT1INPROT</td><td>保护故障 1 输入配置请参考 FLT0INPROT 描述。</td></tr><tr><td>14:11</td><td>FLT1INFC[3:0]</td><td>故障 1 输入滤波控制请参考 FLT0INFC[3:0]描述。</td></tr><tr><td>10</td><td>FLT1INSRC</td><td>故障 1 输入源请参考 FLT0INSRC 描述。</td></tr><tr><td>9</td><td>FLT1INP</td><td>故障 1 输入极性请参考 FLT0INP 描述。</td></tr><tr><td>8</td><td>FLT1INEN</td><td>故障 1 输入使能请参考 FLT0INEN 描述。</td></tr><tr><td>7</td><td>FLT0INPROT</td><td>保护故障 0 输入配置该位域用于配置故障 0 输入配置的写保护功能。该位写一次有效。一旦由软件置位,只能通过系统复位将其清除。0:保护禁能。FLT0INEN, FLT0INP, FLT0INSRC 和 FLT0INFC [3:0]是可写的。1:保护使能。FLT0INEN, FLT0INP, FLT0INSRC 和 FLT0INFC [3:0]是只读的。</td></tr><tr><td>6:3</td><td>FLT0INFC[3:0]</td><td>故障 0 输入滤波控制在数字滤波器中使用事件计数器,N 次输入事件后,输出才会发生转变。该位域用于确定采样外部事件的频率(<eq>f_{SAMP}</eq>)以及应用于外部事件的数字滤波器的长度。0000:无滤波。0001:<eq>f_{SAMP} = f_{SHRTIMER\_CK}</eq>, N=2.0010:<eq>f_{SAMP} = f_{SHRTIMER\_CK}</eq>, N=4.0011:<eq>f_{SAMP} = f_{SHRTIMER\_CK}</eq>, N=8.0100:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/2, N=6.0101:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/2, N=8.0110:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/4, N=6.0111:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/4, N=8.1000:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/8, N=6.1001:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/8, N=8.1010:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/16, N=5.1011:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/16, N=6.1100:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/16, N=8.1101:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/32, N=5.1110:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/32, N=6.1111:<eq>f_{SAMP} = f_{SHRTIMER\_FLTFCK}</eq>/32, N=8.注意:(1)仅当 FLT0INEN 位复位时,才能对该位进行写操作。(2)当 FLT0INPROT 位配置时,不能修改该位域。</td></tr></table>

<table><tr><td>2</td><td>FLTOINSRC</td><td>故障0输入源0: 故障0的输入源是芯片外部引脚。1: 故障0的输入源是芯片内部信号(如比较器)。注意: 仅当FLTOINEN位复位时,才能对该位进行写操作。</td></tr><tr><td>1</td><td>FLTOINP</td><td>故障0输入极性该位用于配置故障0的输入极性。0: 故障0输入为低电平有效。1: 故障0输入为高电平有效。</td></tr><tr><td>0</td><td>FLTOINEN</td><td>故障0输入使能该位置1时,使能故障0输入。0: 故障0输入禁能。1: 故障0输入使能。</td></tr></table>

## SHRTIMER 故障输入配置寄存器 1 (SHRTIMER_FLTINCFG1)

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="2">FLTFDIV[2:0]</td><td colspan="8">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>FLT4INPROT</td><td colspan="4">FLT4INFC[3:0]</td><td>FLT4INSRC</td><td>FLT4INP</td><td>FLT4INEN</td></tr><tr><td colspan="8"></td><td>rwo</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>25:24</td><td>FLTFDIV[2:0]</td><td>故障输入数字滤波器时钟分频该位域可由软件配置,以确定SHRTIMER时钟(SHRTIMER_CK)和故障输入数字滤波器时钟(SHRTIMER_FLTFCK)之间的分频比。<eq>f_{SHRTIMER_FLTFCK} = f_{SHRTIMER_CK}/2^{FLTFDIV[2:0]}</eq>。00:<eq>f_{SHRTIMER_FLTFCK} = f_{SHRTIMER_CK}</eq>。01:<eq>f_{SHRTIMER_FLTFCK} = f_{SHRTIMER_CK}/2</eq>。10:<eq>f_{SHRTIMER_FLTFCK} = f_{SHRTIMER_CK}/4</eq>。11:<eq>f_{SHRTIMER_FLTFCK} = f_{SHRTIMER_CK}/8</eq>。注意:必须在设置FLTyINEN(y=0..4)之前配置该位。</td></tr><tr><td>23:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>FLT4INPROT</td><td>保护故障4输入配置请参考SHRTIMER_FLTINCFG0寄存器中的FLT0INPROT位描述。</td></tr><tr><td>6:3</td><td>FLT4INFC[3:0]</td><td>故障4输入滤波控制</td></tr></table>

<table><tr><td></td><td></td><td>请参考SHRTIMER_FLTINCFG0寄存器中的FLT0INFC[3:0]位域描述。</td></tr><tr><td>2</td><td>FLT4INSRC</td><td>故障4输入源请参考SHRTIMER_FLTINCFG0寄存器中的FLT0INSRC位描述。</td></tr><tr><td>1</td><td>FLT4INP</td><td>故障4输入极性请参考SHRTIMER_FLTINCFG0寄存器中的FLT0INP位描述。</td></tr><tr><td>0</td><td>FLT4INEN</td><td>故障4输入使能请参考SHRTIMER_FLTINCFG0寄存器中的FLT0INEN位描述。</td></tr></table>

## SHRTIMER DMA 更新 Master_TIMER 寄存器 (SHRTIMER_DMAUPMTR)

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MTACTL</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>MTCMP3V</td><td>MTCMP2V</td><td>MTCMP1V</td><td>MTCMP0V</td><td>MTCREP</td><td>MTCAR</td><td>MTCNT</td><td>MTDMAINTEN</td><td>MTINTC</td><td>MTCTL0</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MTACTL</td><td>通过 DMA 模式更新 SHRTIMER_MTACTL 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>30:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>MTCMP3V</td><td>通过 DMA 模式更新 SHRTIMER_MTCMP3V 寄存器请参考MTCTL0描述。</td></tr><tr><td>8</td><td>MTCMP2V</td><td>通过 DMA 模式更新 SHRTIMER_MTCMP2V 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>7</td><td>MTCMP1V</td><td>通过 DMA 模式更新 SHRTIMER_MTCMP1V 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>6</td><td>MTCMP0V</td><td>通过 DMA 模式更新 SHRTIMER_MTCMP0V 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>5</td><td>MTCREP</td><td>通过 DMA 模式更新 SHRTIMER_MTCREP 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>4</td><td>MTCAR</td><td>通过 DMA 模式更新 SHRTIMER_MTCAR 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>3</td><td>MTCNT</td><td>通过 DMA 模式更新 SHRTIMER_MTCNT 寄存器</td></tr></table>

<table><tr><td></td><td></td><td>请参考 MTCTL0 描述。</td></tr><tr><td>2</td><td>MTDMAINTEN</td><td>通过 DMA 模式更新 SHRTIMER_MTDMAINTEN 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>1</td><td>MTINTC</td><td>通过 DMA 模式更新 SHRTIMER_MTINTC 寄存器请参考 MTCTL0 描述。</td></tr><tr><td>0</td><td>MTCTL0</td><td>通过 DMA 模式更新 SHRTIMER_MTCTL0 寄存器该位用于配置通过 DMA 模式更新 SHRTIMER_MTCTL0 寄存器。0: DMA 模式不能更新 SHRTIMER_MTCTL0 寄存器。1: 通过 DMA 模式更新 SHRTIMER_MTCTL0 寄存器。</td></tr></table>

## SHRTIMER DMA 更新 Slavex_TIMER 寄存器 (SHRTIMER_DMAUPSTxR)(x=0..4)

地址偏移：0x5C + x * 0x4,(x=0..4)

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>STxACTL</td><td colspan="10">保留</td><td>STxFLTCTL</td><td>STxCHOCTL</td><td>STxCSCTL</td><td>STxCNTRST</td><td>STxEXEVFCFG1</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STxEXEVFCFG0</td><td>STxCH1RST</td><td>STxCH1SET</td><td>STxCH0RST</td><td>STxCH0SET</td><td>STxDTCTL</td><td>STxCMP3V</td><td>STxCMP2V</td><td>STxCMP1V</td><td>STxCMP0V</td><td>STxCREP</td><td>STxCAR</td><td>STxCNT</td><td>STxDMAINTEN</td><td>STxINTC</td><td>STxCTL0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>STxACTL</td><td>通过 DMA 模式更新 SHRTIMER_STxACTL 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>30:21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>STxFLTCTL</td><td>通过 DMA 模式更新 SHRTIMER_STxFLTCTL 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>19</td><td>STxCHOCTL</td><td>通过 DMA 模式更新 SHRTIMER_STxCHOCTL 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>18</td><td>STxCSCTL</td><td>通过 DMA 模式更新 SHRTIMER_STxCSCTL 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>17</td><td>STxCNTRST</td><td>通过 DMA 模式更新 SHRTIMER_STxCNTRST 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>16</td><td>STxEXEVFCFG1</td><td>通过 DMA 模式更新 SHRTIMER_STxEXEVFCFG1 寄存器请参考 STxCTL0 描述。</td></tr><tr><td>15</td><td>STxEXEVFCFG0</td><td>通过 DMA 模式更新 SHRTIMER_STxEXEVFCFG0 寄存器请参考STxCTL0描述。</td></tr><tr><td>14</td><td>STxCH1RST</td><td>通过DMA模式更新SHRTIMER_STxCH1RST寄存器请参考STxCTL0描述。</td></tr><tr><td>13</td><td>STxCH1SET</td><td>通过DMA模式更新SHRTIMER_STxCH1SET寄存器请参考STxCTL0描述。</td></tr><tr><td>12</td><td>STxCH0RST</td><td>通过DMA模式更新SHRTIMER_STxCH0RST寄存器请参考STxCTL0描述。</td></tr><tr><td>11</td><td>STxCH0SET</td><td>通过DMA模式更新SHRTIMER_STxCH0SET寄存器请参考STxCTL0描述。</td></tr><tr><td>10</td><td>STxDTCTL</td><td>通过DMA模式更新SHRTIMER_STxCHOCTL寄存器请参考STxCTL0描述。</td></tr><tr><td>9</td><td>STxCMP3V</td><td>通过DMA模式更新SHRTIMER_STxDTCTL寄存器请参考STxCTL0描述。</td></tr><tr><td>8</td><td>STxCMP2V</td><td>通过DMA模式更新SHRTIMER_STxCMP2V寄存器请参考STxCTL0描述。</td></tr><tr><td>7</td><td>STxCMP1V</td><td>通过DMA模式更新SHRTIMER_STxCMP1V寄存器请参考STxCTL0描述。</td></tr><tr><td>6</td><td>STxCMP0V</td><td>通过DMA模式更新SHRTIMER_STxCMP0V寄存器请参考STxCTL0描述。</td></tr><tr><td>5</td><td>STxCREP</td><td>通过DMA模式更新SHRTIMER_STxCREP寄存器请参考STxCTL0描述。</td></tr><tr><td>4</td><td>STxCAR</td><td>通过DMA模式更新SHRTIMER_STxCAR寄存器请参考STxCTL0描述。</td></tr><tr><td>3</td><td>STxCNT</td><td>通过DMA模式更新SHRTIMER_STxCNT寄存器请参考STxCTL0描述。</td></tr><tr><td>2</td><td>STxDMAINTEN</td><td>通过DMA模式更新SHRTIMER_STxDMAINTEN寄存器请参考STxCTL0描述。</td></tr><tr><td>1</td><td>STxINTC</td><td>通过DMA模式更新SHRTIMER_STxINTC寄存器请参考STxCTL0描述。</td></tr><tr><td>0</td><td>STxCTL0</td><td>通过DMA模式更新SHRTIMER_STxCTL0寄存器该位用于配置DMA模式更新SHRTIMER_STxCTL0寄存器。0: DMA模式不能更新SHRTIMER_STxCTL0寄存器。1: 通过DMA模式更新SHRTIMER_STxCTL0寄存器。</td></tr></table>

## SHRTIMER DMA 传输缓冲寄存器 (SHRTIMER_DMATB)

地址偏移：0x70

复位值：0x0000 0000

该寄存器只能进行字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DMATB[31:16]</td></tr><tr><td colspan="16">wo</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMATB[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DMATB[31:16]</td><td>DMA 传输缓冲区对该寄存器进行写操作时,实际访问的寄存器是SHRTIMER_DMAUPMTR 寄存器和SHRTIMER_DMAUPSTxR(x=0..4)寄存器中使能的寄存器。寄存器指针的增量由硬件计算。</td></tr></table>
