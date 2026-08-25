## 19.5. LPTIMER 寄存器

GD32L233 系列芯片中：

LPTIMER 基地址：0x4000 9400

GD32L235 系列芯片中：

LPTIMER0 基地址：0x4000 9400

LPTIMER1 基地址：0x4000 7C00

## 19.5.1. 中断标志寄存器（LPTIMER_INTF）

地址偏移：0x00

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IN1EIF</td><td>IN0EIF</td><td>INRFOEIF</td><td>INHLOEIF</td><td>INHLCOIF</td><td>HLCMV UPIF</td><td colspan="10">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>DOWNIF</td><td>UPIF</td><td>CARUPIF</td><td>CMPV UPIF</td><td>ETED EVIF</td><td>CARMIF</td><td>CMPV MIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IN1EIF</td><td>LPTIMER_IN1 错误中断标志位当 LPTIMER_IN1 信号不在 LPTIMER_IN0 信号的两个连续上升沿之间发生跳变时,该标志位由硬件置 1。可以通过向 INTC 寄存器的 IN1EIC 位写入 1 来清除 IN1EIF 标志。注意:该标志位仅用于译码器模式 1。</td></tr><tr><td>30</td><td>IN0EIF</td><td>LPTIMER_IN0 错误中断标志位当 LPTIMER_IN0 信号不在 LPTIMER_IN1 信号的两个连续上升沿之间发生跳变时,该标志位由硬件置 1。可以通过向 INTC 寄存器的 IN0EIC 位写入 1 来清除 IN0EIF 标志。注意:该标志位仅用于译码器模式 1。</td></tr><tr><td>29</td><td>INRFOEIF</td><td>LPTIMER_IN0 和 LPTIMER_IN1 下降沿和上升沿重叠错误中断标志位当 LPTIMER_IN0 下降沿和 LPTIMER_IN1 上升沿同时发生或者 LPTIMER_IN0 上升沿和 LPTIMER_IN1 下降沿同时发生时,该标志位由硬件置 1。可以通过向 INTC 寄存器的 INRFOEIC 位写入 1 来清除 INRFOEIF 标志。注意:该标志位仅用于译码器模式 1。</td></tr><tr><td>28</td><td>INHLOEIF</td><td>LPTIMER_IN0 和 LPTIMER_IN1 高电平重叠错误中断标志位当 LPTIMER_IN0 和 LPTIMER_IN1 的高电平重叠时,该标志位由硬件置 1。可以通过向INTC寄存器的INHLOEIC位写入1来清除INHLOEIF标志。注意:该标志位仅用于译码器模式1。</td></tr><tr><td>27</td><td>INHLCOIF</td><td>LPTIMER_Inx(x=0,1)高电平计数器溢出中断标志位当LPTIMER_Inx的高电平计数器与外部输入高电平计数最大值寄存器(LPTIMER_INHLCMV)值相等时,该标志位由硬件置1。可以通过向INTC寄存器的INHLCOIC位写入1来清除INHLCOIF标志。</td></tr><tr><td>26</td><td>HLCMVUPIF</td><td>输入高电平计数最大值寄存器更新中断标志位当APB总线完成对LPTIMER_INHLCMV寄存器的写操作时,该标志位由硬件置1。可以通过向INTC寄存器的HLCMVUPIC位写入1来清除HLCMVUPIF标志。</td></tr><tr><td>25:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>DOWNIF</td><td>LPTIMER计数器由向上计数改为向下计数中断标志位在译码器0模式中,当计数器由向上计数改为向下计数时,该标志位由硬件置1。可以通过向INTC寄存器的DOWNIC位写入1来清除DOWNIF标志。</td></tr><tr><td>5</td><td>UPIF</td><td>LPTIMER计数器由向下计数改为向上计数中断标志位在译码器0模式中,当计数器由向下计数改为向上计数时,该标志位由硬件置1。可以通过向INTC寄存器的UPIC位写入1来清除UPIF标志。</td></tr><tr><td>4</td><td>CARUPIF</td><td>计数器自动重载寄存器更新中断标志位当APB总线完成对LPTIMER_CAR寄存器的写操作时,该标志位由硬件置1。可以通过向INTC寄存器的CARUPIC位写入1来清除CARUPIF标志。</td></tr><tr><td>3</td><td>CMPVUPIF</td><td>比较寄存器更新中断标志位当APB总线完成对LPTIMER_CMPV寄存器的写操作时,该标志位由硬件置1。可以通过向INTC寄存器的CMPVUPIC位写入1来清除CMPVUPIF标志。</td></tr><tr><td>2</td><td>ETEDEVIF</td><td>外部触发边沿事件中断标志位当外部触发的有效边沿发生时,该标志位由硬件置1。可以通过向INTC寄存器的ETEDEVIC位写入1来清除ETEDEVIF标志。注意:当外部触发的有效边沿发生在LPTIMER启动之后,该标志位不会置位。</td></tr><tr><td>1</td><td>CARMIF</td><td>计数器自动重载寄存器匹配中断标志位当LPTIMER_CNT的值与LPTIMER_CAR寄存器的值相等时,该标志位由硬件置1。可以通过向INTC寄存器的CARMIC位写入1来清除CARMIF标志。</td></tr><tr><td>0</td><td>CMPVMIF</td><td>比较寄存器匹配中断标志位当LPTIMER_CNT的值与LPTIMER_CMPV寄存器的值相等时,该标志位由硬件置1。可以通过向INTC寄存器的CMPVMIC位写入1来清除CMPVMIF标志。</td></tr></table>

## 19.5.2. 中断标志清除寄存器（LPTIMER_INTC）

地址偏移：0x04

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IN1EIC</td><td>INOEC</td><td>INRFOEC</td><td>INHLOEC</td><td>INHLCOIC</td><td>HLCMVUPIC</td><td colspan="10">保留</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>DOWNIC</td><td>UPIC</td><td>CARUPIC</td><td>CMPVUPIC</td><td>ETEDEVIC</td><td>CARMIC</td><td>CMPVMIC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IN1EIC</td><td>LPTIMER_IN1 错误中断标志清除位向该位写 1 来清除 IN1EIF 标志,写 0 无影响。</td></tr><tr><td>30</td><td>INOEIC</td><td>LPTIMER_IN0 错误中断标志清除位向该位写 1 来清除 IN0EIF 标志,写 0 无影响。</td></tr><tr><td>29</td><td>INRFOEIC</td><td>LPTIMER_IN0 和 LPTIMER_IN1 下降沿和上升沿重叠错误中断标志清除位向该位写 1 来清除 INRFOEIF 标志,写 0 无影响。</td></tr><tr><td>28</td><td>INHLOEIC</td><td>LPTIMER_IN0 和 LPTIMER_IN1 高电平重叠错误中断标志清除位向该位写 1 来清除 INHLOEIF 标志,写 0 无影响。</td></tr><tr><td>27</td><td>INHLCOIC</td><td>LPTIMER_Inx(x=0,1)高电平计数器溢出中断标志清除位向该位写 1 来清除 INHLCOIF 标志,写 0 无影响。</td></tr><tr><td>26</td><td>HLCMVUPIC</td><td>输入高电平计数最大值寄存器更新中断标志清除位向该位写 1 来清除 HLCMVUPIF 标志,写 0 无影响。</td></tr><tr><td>25:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>DOWNIC</td><td>LPTIMER计数器由向上计数改为向下计数中断标志清除位向该位写 1 来清除 DOWNIF 标志,写 0 无影响。</td></tr><tr><td>5</td><td>UPIC</td><td>LPTIMER计数器由向下计数改为向上计数中断标志清除位向该位写 1 来清除 UPIF 标志,写 0 无影响。</td></tr><tr><td>4</td><td>CARUPIC</td><td>计数器自动重载寄存器更新中断标志清除位向该位写 1 来清除 CARUPIF 标志,写 0 无影响。</td></tr><tr><td>3</td><td>CMPVUPIC</td><td>比较寄存器更新中断标志清除位向该位写 1 来清除 CMPVUPIF 标志,写 0 无影响。</td></tr><tr><td>2</td><td>ETEDEVIC</td><td>外部触发边沿事件中断标志清除位向该位写 1 来清除 ETEDEVIF 标志,写 0 无影响。</td></tr><tr><td>1</td><td>CARMIC</td><td>计数器自动重载寄存器匹配中断标志清除位向该位写 1 来清除 CARMIF 标志,写 0 无影响。</td></tr><tr><td>0</td><td>CMPVMIC</td><td>比较寄存器匹配中断标志清除位向该位写 1 来清除 CMPVMIF 标志,写 0 无影响。</td></tr></table>

## 19.5.3. 中断使能寄存器（LPTIMER_INTEN）

地址偏移：0x08

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IN1EIE</td><td>INOIE</td><td>INRFOEIE</td><td>INHLOEIE</td><td>INHLCOIE</td><td>HLCMV UPIE</td><td colspan="10">保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="10"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>DOWNIE</td><td>UPIE</td><td>CARUPIE</td><td>CMPV UPIE</td><td>ETED EVIE</td><td>CARMIE</td><td>CMPV MIE</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IN1EIE</td><td>LPTIMER_IN1 错误中断使能位0:禁止 LPTIMER_IN1 错误中断1:使能 LPTIMER_IN1 错误中断只有在 LPTIMER 禁能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>30</td><td>INOEIE</td><td>LPTIMER_IN0 错误中断使能位0:禁止 LPTIMER_IN0 错误中断1:使能 LPTIMER_IN0 错误中断只有在 LPTIMER 禁能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>29</td><td>INRFOEIE</td><td>LPTIMER_IN0 和 LPTIMER_IN1 下降沿和上升沿重叠错误中断使能位0:禁止 LPTIMER_IN0 和 LPTIMER_IN1 下降沿和上升沿重叠错误中断1:使能 LPTIMER_IN0 和 LPTIMER_IN1 下降沿和上升沿重叠错误中断只有在 LPTIMER 禁能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>28</td><td>INHLOEIE</td><td>LPTIMER_IN0 和 LPTIMER_IN1 高电平重叠错误中断使能位0:禁止 LPTIMER_IN0 和 LPTIMER_IN1 高电平重叠错误中断1:使能 LPTIMER_IN0 和 LPTIMER_IN1 高电平重叠错误中断只有在 LPTIMER 禁能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>27</td><td>INHLCOIE</td><td>LPTIMER_Inx(x=0,1)高电平计数器溢出中断使能位0:禁止 LPTIMER_Inx(x=0,1)高电平计数器溢出中断1:使能 LPTIMER_Inx(x=0,1)高电平计数器溢出中断只有在 LPTIMER 的外部输入高电平计数器禁能时,才能修改该位(LPTIMER_CTL1 寄存器中的 INHLCEN 位为 0)。</td></tr><tr><td>26</td><td>HLCMVUPIE</td><td>输入高电平计数最大值寄存器更新中断使能位0:禁止输入高电平计数最大值寄存器更新中断1:使能输入高电平计数最大值寄存器更新中断只有在LPTIMER的外部输入高电平计数器禁能时,才能修改该位(LPTIMER_CTL1寄存器中的INHLCEN位为0)。</td></tr><tr><td>25:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>DOWNIE</td><td>LPTIMER计数器由向上计数改为向下计数中断使能位0:禁止计数器由向上计数改为向下计数中断1:使能计数器由向上计数改为向下计数中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>5</td><td>UPIE</td><td>LPTIMER计数器由向下计数改为向上计数中断使能位0:禁止计数器由向下计数改为向上计数中断1:使能计数器由向下计数改为向上计数中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>4</td><td>CARUPIE</td><td>计数器自动重载寄存器更新中断使能位0:禁止计数器自动重载寄存器更新中断1:使能计数器自动重载寄存器更新中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>3</td><td>CMPVUPIE</td><td>比较寄存器更新中断使能位0:禁止比较寄存器更新中断1:使能比较寄存器更新中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>2</td><td>ETEDEVIE</td><td>外部触发边沿事件中断使能位0:禁止外部触发边沿事件中断1:使能外部触发边沿事件中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>1</td><td>CARMIE</td><td>计数器自动重载寄存器匹配中断使能位0:禁止计数器自动重载寄存器匹配中断1:使能计数器自动重载寄存器匹配中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>0</td><td>CMPVMIE</td><td>比较寄存器匹配中断使能位0:禁止比较寄存器匹配中断1:使能比较寄存器匹配中断只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr></table>

## 19.5.4. 控制寄存器 0（LPTIMER_CTL0）

地址偏移：0x0C

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>DECMSEL</td><td>DECMEN</td><td>CNTMEN</td><td>SHWEN</td><td>OPSEL</td><td>OMSEL</td><td>TIMEOUT</td><td colspan="2">ETMEN[1:0]</td><td>保留</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">ETSEL[2:0]</td><td>保留</td><td colspan="3">PSC[2:0]</td><td>保留</td><td colspan="2">TFLT [1:0]</td><td>保留</td><td colspan="2">ECKFLT[1:0]</td><td colspan="2">CKPSEL[1:0]</td><td>CKSSEL</td></tr><tr><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>DECMSEL</td><td>译码器模式选择0: 译码器模式01: 译码器模式1只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>24</td><td>DECMEN</td><td>译码器模式使能0: 译码器模式禁能1: 译码器模式使能只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>23</td><td>CNTMEN</td><td>计数器模式选择该位用于选择LPTIMER计数器的时钟源。0: 计数器在内部时钟每一个脉冲都计数1: 计数器在LPTIMER_IN0引脚上的每一个有效脉冲计数只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>22</td><td>SHWEN</td><td>LPTIMER_CAR和LPTIMER_CMPV影子寄存器使能0: 影子寄存器禁能。在每一次APB写操作之后,这两个寄存器立即更新1: 影子寄存器使能。这两个寄存器在LPTIME周期结束之后更新只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>21</td><td>OPSEL</td><td>输出极性选择该位用于控制LPTIMER输出的极性。0: 输出同相。向上计数时,当计数器值与LPTIMER_CMPV的值匹配,输出高电平;当计数器值与LPTIMER_CAR的值匹配,输出低电平。1: 输出反相。向上计数时,当计数器值与LPTIMER_CMPV的值匹配,输出低电平;当计数器值与LPTIMER_CAR的值匹配,输出高电平。只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>20</td><td>OMSEL</td><td>输出模式选择该位用于控制LPTIMER的输出模式。0: PWM模式或单脉冲模式(CTNMST位选择PWM模式,SMST位选择单脉冲模式)1: 置位模式只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>19</td><td>TIMEOUT</td><td>超时模式使能该位用于控制LPTIMER的超时模式。0: LPTIMER启动后,新的触发事件会被忽略1: LPTIMER启动后,新的触发事件会复位和重新启动LPTIMER只有在LPTIMER禁能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>18:17</td><td>ETMEN[1:0]</td><td>外部触发模式使能该位域用于配置LPTIMER的外部触发模式。00: 外部触发禁能(软件触发)01: 外部触发上升沿有效10: 外部触发下降沿有效11: 外部触发上升沿和下降沿都有效只有在LPTIMER禁能时,才能修改该位域(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>ETSEL[2:0]</td><td>外部触发选择该位域用于选择LPTIMER的外部触发源000: ETI0(GPIO)001: ETI1(RTC闹钟0)010: ETI2(RTC闹钟1)011: ETI3(RTC_TAMP0)100: ETI4(RTC_TAMP1)101: ETI5(RTC_TAMP2)110: ETI6(CMP0_OUT)111: ETI7(CMP1_OUT)只有在LPTIMER禁能时,才能修改该位域(LPTIMER_CTL1寄存器中的LPTEN位为0)。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:9</td><td>PSC[2:0]</td><td>时钟预分频器选择该位域用于配置预分频器,将LPTIMER的时钟LPTIMER_CK分频到计数器时钟PSC_CLK。000: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK}</eq>001: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 2</eq>010: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 4</eq>011: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 8</eq>100: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 16</eq>101: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 32</eq>110: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 64</eq>111: <eq>f_{PSC\_CLK} = f_{LPTIMER\_CK} / 128</eq>只有在 LPTIMER 禁能时,才能修改该位域(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:6</td><td>TFLT[1:0]</td><td>触发滤波该位域用于配置触发的数字滤波器,使用该功能时,必须使用内部时钟源。00:无滤波器,触发信号的每个有效电平都有效01:触发信号的有效电平变化必须保持 2 个时钟周期10:触发信号的有效电平变化必须保持 4 个时钟周期11:触发信号的有效电平变化必须保持 8 个时钟周期只有在 LPTIMER 禁能时,才能修改该位域(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>ECKFLT[1:0]</td><td>外部时钟滤波该位域用于配置外部时钟的数字滤波器,使用该功能时,必须使用内部时钟源。00:无滤波器,外部时钟的每个有效电平变化都有效01:外部时钟的有效电平变化必须保持 2 个时钟周期10:外部时钟的有效电平变化必须保持 4 个时钟周期11:外部时钟的有效电平变化必须保持 8 个时钟周期只有在 LPTIMER 禁能时,才能修改该位域(LPTIMER_CTL1 寄存器中的 LPTEN 位为 0)。</td></tr><tr><td>2:1</td><td>CKPSEL[1:0]</td><td>时钟极性选择当 LPTIMER 使用外部时钟源时,该位域用于配置计数器计数的有效边沿。00:上升沿计数若 LPTIMER 配置为译码器模式 0 (DECMEN=1,DECMSEL=0),译码器的上升沿计数模式有效;若 LPTIMER 配置为译码器模式 1 (DECMEN=1,DECMSEL=1),LPTIMER_IN0 和 LPTIMER_IN1 的输入同相;若 LPTIMER 外部输入高电平计数器使能 (INHLCEN=1),LPTIMER_IN0 和 LPTIMER_IN1 的输入同相。01:下降沿计数若 LPTIMER 配置为译码器模式 0 (DECMEN=1,DECMSEL=0),译码器的下降沿计数模式有效;若 LPTIMER 配置为译码器模式 1 (DECMEN=1,DECMSEL=1),LPTIMER_IN0 和 LPTIMER_IN1 的输入反相;若 LPTIMER 外部输入高电平计数器使能 (INHLCEN=1),LPTIMER_IN0 和</td></tr></table>

LPTIMER_IN1 的输入反相。

## 10：双边沿计数

当外部时钟的双边沿都能有效计数时，LPTIMER 必须使用内部时钟源，并且内部时钟源的频率最少是外部时钟源频率的 4 倍。

若 LPTIMER 配置为译码器模式 0（DECMEN=1，DECMSEL=0），译码器的双边沿计数模式有效；

LPTIMER 不能配置为译码器模式 1；

若 LPTIMER 外部输入高电平计数器使能（INHLCEN=1），LPTIMER_IN0 和LPTIMER_IN1 的输入同相。

11：保留

只有在 LPTIMER 禁能时，才能修改该位域（LPTIMER_CTL1 寄存器中的 LPTEN 位为 0）。

## 0 CKSSEL 时钟源选择

该位用于选择 LPTIMER 的时钟源。

0：LPTIMER 使用内部时钟源

1：LPTIMER 使用外部时钟源（LPTIMER_IN0）

只有在 LPTIMER 禁能时，才能修改该位（LPTIMER_CTL1 寄存器中的 LPTEN 位为 0）。

注意：当 DECMEN 位置 1 使能译码器模式时，CKSSEL 会自动清零。

## 19.5.5. 控制寄存器 1（LPTIMER_CTL1）

地址偏移：0x10

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>INHLCEN</td><td>LPTENF</td><td colspan="14">保留</td></tr><tr><td>rw</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>CTNMST</td><td>SMST</td><td>LPTEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>INHLCEN</td><td>LPTIMER 外部输入高电平计数器使能0:禁能1:使能</td></tr><tr><td>30</td><td>LPTENF</td><td>LPTIMER 从 LPTIMER 内核使能标志位该位由硬件置位和清零。0:LPTIMER 禁能1:LPTIMER 使能</td></tr><tr><td>29:32</td><td>保留CTNMST</td><td>必须保持复位值。LPTIMER 以连续计数模式启动该位由软件置位和硬件清零。只有在 LPTIMER 使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 1)。</td></tr><tr><td>1</td><td>SMST</td><td>LPTIMER 以单次计数模式启动该位由软件置位和硬件清零。只有在 LPTIMER 使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 1)。</td></tr><tr><td>0</td><td>LPTEN</td><td>LPTIMER 使能该位由软件置位和清零。0: LPTIMER 禁能1: LPTIMER 使能</td></tr></table>

## 19.5.6. 比较寄存器（LPTIMER_CMPV）

GD32L233xx 芯片

地址偏移：0x14

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CMPVAL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMPVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CMPVAL[31:0]</td><td>比较值这些位定义了计数器的比较值。只有在 LPTIMER 使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 1)。</td></tr></table>

GD32L235xx 芯片

地址偏移：0x14

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>CMPVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CMPVAL[15:0]</td><td>比较值这些位定义了计数器的比较值。只有在LPTIMER使能时,才能修改该位(LPTIMER_CTL1寄存器中的LPTEN位为1)。</td></tr></table>

## 19.5.7. 计数器自动重载寄存器（LPTIMER_CAR）

GD32L233xx 芯片

地址偏移：0x18

复位值：0x0001

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CARL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CARL[31:0]</td><td>计数器自动重载寄存器值这些位定义了计数器的自动重载值。只有在 LPTIMER 使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 1)。</td></tr><tr><td></td><td colspan="2">GD32L235xx 芯片地址偏移:0x18复位值:0x0001</td></tr></table>

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>

<table><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载寄存器值这些位定义了计数器的自动重载值。只有在 LPTIMER 使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 LPTEN 位为 1)。</td></tr></table>

## 19.5.8. 计数器寄存器（LPTIMER_CNT）

GD32L233xx 芯片

地址偏移：0x1C

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">CNT[31:16]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">CNT[15:0]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CNT[31:0]</td><td>计数器值注意:当LPTIMER使用异步时钟时,对LPTIMER_CNT寄存器的读操作可能会返回不可靠的值。因此,需要执行两个连续的读操作,并且确认两次的读取值是否相同。</td></tr></table>

GD32L235xx 芯片

地址偏移：0x1C

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>计数器值</td></tr><tr><td></td><td></td><td>注意:当LPTIMER使用异步时钟时,对LPTIMER_CNT寄存器的读操作可能会返回不可靠的值。因此,需要执行两个连续的读操作,并且确认两次的读取值是否相同。</td></tr></table>

## 19.5.9. 外部输入映射寄存器（LPTIMER_EIRMP）

地址偏移：0x20

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IN1_RMP</td><td>INO_RMP</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IN1_RMP</td><td>外部输入 LPTIMER_IN1 映射0: 外部输入引脚 1 映射到 GPIO1: 外部输入引脚 1 映射到 CMP1_OUT</td></tr><tr><td>0</td><td>IN0_RMP</td><td>外部输入 LPTIMER_IN0 映射0: 外部输入引脚 0 映射到 GPIO1: 外部输入引脚 0 映射到 CMP0_OUT</td></tr></table>

## 19.5.10. 输入高电平计数最大值寄存器（LPTIMER_INHLCMV）

地址偏移：0X24

复位值：0x0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">INHLCMVAL [25:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INHLCMVAL [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:0</td><td>INHLCMVAL</td><td>输入高电平计数最大值只有在 LPTIMER 的外部输入高电平计数器使能时,才能修改该位(LPTIMER_CTL1 寄存器中的 INHLCEN 位为 1)。</td></tr></table>
