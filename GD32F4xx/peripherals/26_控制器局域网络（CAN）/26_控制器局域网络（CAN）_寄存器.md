# 26.4. CAN 寄存器

CAN0基地址：0x4000 6400

CAN1基地址：0x4000 6800

# 26.4.1. 控制寄存器（CAN_CTL）

地址偏移：0x00

复位值：0x0001 0002


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>DFZ</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SWRST</td><td colspan="7">保留</td><td>TTC</td><td>ABOR</td><td>AWU</td><td>ARD</td><td>RFOD</td><td>TFO</td><td>SLPWMOD</td><td>IWMOD</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>DFZ</td><td>调试冻结如果DBG_CTL0寄存器中CANx_HOLD被置位,该位用来定义CAN控制器工作在调试冻结或正常工作状态。如果DBG_CTL0寄存器中CANx_HOLD被清零,该位无效。0:处于Debug时,CAN接收和发送正常工作1:处于Debug时,CAN接收和发送停止</td></tr><tr><td>15</td><td>SWRST</td><td>软件复位0:正常操作1:复位CAN并进入睡眠工作模式。该位会自动清0</td></tr><tr><td>14:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TTC</td><td>时间触发通信0:禁用时间触发通信1:使能时间触发通信</td></tr><tr><td>6</td><td>ABOR</td><td>自动离线恢复0:通过软件手动地从离线状态恢复1:通过硬件自动的从离线状态恢复</td></tr><tr><td>5</td><td>AWU</td><td>自动唤醒一旦自动唤醒后,CAN_CTL寄存器的SLPWMOD位将自动被清0。0:通过软件手动的从睡眠工作模式唤醒1: 通过硬件自动的从睡眠工作模式唤醒</td></tr><tr><td>4</td><td>ARD</td><td>自动重发禁止0: 使能自动重发1: 禁用自动重发</td></tr><tr><td>3</td><td>RFOD</td><td>禁用接收FIFO满时覆盖0: 使能接收FIFO满时覆盖。当接收FIFO满时,FIFO中的数据被新来的数据覆盖1: 禁用接收FIFO满时覆盖。当接收FIFO满时,新来的数据被丢弃,FIFO中的数据保持不变,不会被覆盖</td></tr><tr><td>2</td><td>TFO</td><td>发送FIFO顺序0: 标识符(Identifier)较小的帧先发送1: 所有等待发送的邮箱按照先进先出(FIFO)的顺序发送</td></tr><tr><td>1</td><td>SLPWMOD</td><td>睡眠工作模式如果软件将该位置1,CAN将会在当前发送或接收完成时进入睡眠工作模式。该位可由软件或者硬件清0。如果CAN_CTL寄存器中AWU被置位,当检测到CAN总线工作时,该位被清0。0: 禁用睡眠工作模式1: 使能睡眠工作模式</td></tr><tr><td>0</td><td>IWMOD</td><td>初始化工作模式0: 禁用初始化工作模式1: 使能初始化工作模式</td></tr></table>

# 26.4.2. 状态寄存器（CAN_STAT）

地址偏移：0x04

复位值：0x0000 0C02

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>RXL</td><td>LASTRX</td><td>RS</td><td>TS</td><td colspan="3">保留</td><td>SLPIF</td><td>WUIF</td><td>ERRIF</td><td>SLPWS</td><td>IWS</td></tr></table>

<table><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>RXL</td><td>RX 引脚电平</td></tr><tr><td>10</td><td>LASTRX</td><td>RX 引脚最近一次的采样值</td></tr><tr><td>9</td><td>RS</td><td>接收状态0: CAN当前不是接收器1: CAN当前是接收器</td></tr><tr><td>8</td><td>TS</td><td>发送状态0: CAN当前不是发送器1: CAN当前是发送器</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>SLPIF</td><td>进入睡眠工作模式的状态改变中断标志该位在进入睡眠工作模式时由硬件置位。当CAN不再处于睡眠工作模式时由硬件清零。该位也可以由软件写1清0。0: CAN没有进入睡眠工作模式1: CAN进入睡眠工作模式。如果相应的中断使能位为1,则发生中断</td></tr><tr><td>3</td><td>WUIF</td><td>从睡眠工作模式唤醒的状态改变中断标志该位在睡眠工作模式时检测到CAN总线上的活动时由硬件置位。该位由软件写1清0。0: 没有检测到唤醒信号1: 发现唤醒信号。如果相应的中断使能位为1,则发生中断</td></tr><tr><td>2</td><td>ERRIF</td><td>错误中断标志该位由以下事件置位。CAN_ERR寄存器中BOERR位和CAN_INTEN寄存器中BOIE位都置位。或CAN_ERR寄存器中PERR位和CAN_INTEN寄存器中PERRIE位都置位。或CAN_ERR寄存器中WERR位和CAN_INTEN寄存器中WERRIE位都置位。或CAN_ERR寄存器中ERRN位域的值不为0且CAN_INTEN寄存器中ERRNIE位置位。该位由软件写1清零。0: 没有错误1: 发生错误。如果相应的中断使能位为1,则发生中断</td></tr><tr><td>1</td><td>SLPWS</td><td>睡眠工作状态将CAN_CTL寄存器中SLPWMOD位置位进入睡眠工作模式后该位由硬件置位。当CAN由正常通信模式切换到睡眠工作模式,需等待当前发送过程或者接收过程完成。当CAN离开睡眠工作模式(清除CAN_CTL寄存器中SLPWMOD位或是在CAN_CTL寄存器中AWU置位时检测到CAN总线上的活动)时,该位由硬件清零。如果由睡眠工作模式切换到正常工作模式,该位在CAN接收到来自总线的连续11个隐性位后被清0。0: CAN没有处于睡眠工作状态1: CAN处于睡眠工作状态</td></tr><tr><td>0</td><td>IWS</td><td>初始化工作状态将CAN_CTL寄存器中IWMOD位置位进入初始化模式后该位由硬件置位。当CAN由正常通信模式切换到初始化工作模式,需等待当前发送过程或者接收过程完成。在清除CAN_CTL寄存器中IWMOD位离开初始化模式后,该位由硬件清0。如果由初始化工作模式切换到正常工作模式,该位在CAN接收到来自总线的连续11个隐性位后被清0。0: CAN没有处于初始化工作状态</td></tr></table>

1：CAN处于初始化工作状态

# 26.4.3. 发送状态寄存器（CAN_TSTAT）

地址偏移：0x08

复位值：0x1C00 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TMLS2</td><td>TMLS1</td><td>TMLS0</td><td>TME2</td><td>TME1</td><td>TME0</td><td colspan="2">NUM[1:0]</td><td>MST2</td><td colspan="3">保留</td><td>MTE2</td><td>MAL2</td><td>MTFNER R2</td><td>MTF2</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="2">r</td><td>rs</td><td colspan="3"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MST1</td><td colspan="3">保留</td><td>MTE1</td><td>MAL1</td><td>MTFNER R1</td><td>MTF1</td><td>MST0</td><td colspan="3">保留</td><td>MTE0</td><td>MAL0</td><td>MTFNER R0</td><td>MTF0</td></tr><tr><td>rs</td><td colspan="3"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rs</td><td colspan="3"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TMLS2</td><td>在发送FIFO中邮箱2最后发送该位为1表明,当有2个及其以上帧等待发送时,发送邮箱2具有最后的发送顺序。</td></tr><tr><td>30</td><td>TMLS1</td><td>在发送FIFO中邮箱1最后发送该位为1表明,当有2个及其以上帧等待发送时,发送邮箱1具有最后的发送顺序。</td></tr><tr><td>29</td><td>TMLS0</td><td>在发送FIFO中邮箱0最后发送该位为1表明,当有2个及其以上帧等待发送时,发送邮箱0具有最后的发送顺序。</td></tr><tr><td>28</td><td>TME2</td><td>发送邮箱2空0:发送邮箱2不为空1:发送邮箱2空</td></tr><tr><td>27</td><td>TME1</td><td>发送邮箱1空0:发送邮箱1不为空1:发送邮箱1空</td></tr><tr><td>26</td><td>TME0</td><td>发送邮箱0空0:发送邮箱0不为空1:发送邮箱0空</td></tr><tr><td>25:24</td><td>NUM[1:0]</td><td>当发送FIFO不满时,NUM表示下一个将要发送的邮箱号。当发送FIFO满时,NUM表示最后一个将要发送的邮箱号。</td></tr><tr><td>23</td><td>MST2</td><td>邮箱2停止发送将其置1,将停止邮箱2的发送过程。当邮箱2变为empty状态时,该位被硬件自动清0。</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>MTE2</td><td>邮箱2发送错误当发生发送错误时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF2写1清0。也可以在下一次发送开始时由硬件清0。当发生错误时该位被置1。</td></tr><tr><td>18</td><td>MAL2</td><td>邮箱2仲裁失败当发生仲裁失败时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF2写1清0。也可以在下一次发送开始时由硬件清0。当发生仲裁失败时该位被置1。</td></tr><tr><td>17</td><td>MTFNERR2</td><td>邮箱2无错发送完成当发送结束并且没有错误产生时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF2写1清0。也可以在无错传输结束时由硬件清0。0:传输结束时发生了错误1:传输结束且没有错误</td></tr><tr><td>16</td><td>MTF2</td><td>邮箱2发送完成当发送完成或被中止时,该位由硬件置1。由软件写1清0,或当CAN_TMI2寄存器的TEN被置位时清0。0:发送邮箱2正在发送1:发送邮箱2完成发送</td></tr><tr><td>15</td><td>MST1</td><td>邮箱1停止发送将其置1,将停止邮箱1的发送过程。当邮箱1变为empty状态时,该位被硬件自动清0。</td></tr><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>MTE1</td><td>邮箱1发送错误当发生发送错误时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF1写1清0。也可以在下一次发送开始时由硬件清0。当发生错误时该位被置1。</td></tr><tr><td>10</td><td>MAL1</td><td>邮箱1仲裁失败当发生仲裁失败时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF1写1清0。也可以在下一次发送开始时由硬件清0。当发生仲裁失败时该位被置1。</td></tr><tr><td>9</td><td>MTFNERR1</td><td>邮箱1无错发送完成当发送结束并且没有错误产生时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF1写1清0。也可以在无错传输结束时由硬件清0。0:传输结束时发生了错误1:传输结束且没有错误</td></tr><tr><td>8</td><td>MTF1</td><td>邮箱1发送完成当发送完成或被中止时,该位由硬件置1。由软件写1清0,或当CAN_TMI1寄存器的TEN被置位时清0。0:发送邮箱1正在发送1:发送邮箱1完成发送</td></tr><tr><td>7</td><td>MST0</td><td>邮箱0停止发送将其置1,将停止邮箱0的发送过程。当邮箱0变为emtpy状态时,该位被硬件自动清0。</td></tr><tr><td>6:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>MTE0</td><td>邮箱0发送错误当发生发送错误时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF0写1清0。也可以在下一次发送开始时由硬件清0。当发生错误时该位被置1。</td></tr><tr><td>2</td><td>MAL0</td><td>邮箱0仲裁失败当发生仲裁失败时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF0写1清0。也可以在下一次发送开始时由硬件清0。当发生仲裁失败时该位被置1。</td></tr><tr><td>1</td><td>MTFNERR0</td><td>邮箱0无错发送完成当发送结束并且没有错误产生时,该位由硬件置1。由软件写1清0或对CAN_TSTAT寄存器中MTF0写1清0。也可以在无错传输结束时由硬件清0。0:传输结束时发生了错误1:传输结束且没有错误</td></tr><tr><td>0</td><td>MTF0</td><td>邮箱0发送完成当发送完成或被中止时,该位由硬件置1。由软件写1清0,或当CAN_TMI0寄存器的TEN被置位时清0。0:发送邮箱0正在发送1:发送邮箱0完成发送</td></tr></table>

# 26.4.4. 接收 FIFO0 寄存器（CAN_RFIFO0）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>RFD0</td><td>RFO0</td><td>RFF0</td><td>保留</td><td colspan="2">RFL0[1:0]</td></tr><tr><td colspan="10"></td><td>rs</td><td>rc_w1</td><td>rc_w1</td><td></td><td colspan="2">r</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>RFD0</td><td>释放一次FIFO0中的数据该位被置1,将释放FIFO0中的一帧数据。FIFO释放相应的数据空间后,该位被清0。</td></tr><tr><td>4</td><td>RFO0</td><td>接收FIFO0溢出当接收FIFO0溢出时被置位,由软件写1清0。0:接收FIFO0没有溢出1:接收FIFO0溢出</td></tr><tr><td>3</td><td>RFF0</td><td>接收FIFO0满当接收FIFO0满时被置位,由软件写1清0。0:接收FIFO0不满1:接收FIFO0满</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>RFL0[1:0]</td><td>接收FIFO0中帧的数量</td></tr></table>

# 26.4.5. 接收 FIFO1 寄存器（CAN_RFIFO1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>RFD1</td><td>RFO1</td><td>RFF1</td><td>保留</td><td colspan="2">RFL1[1:0]</td></tr><tr><td colspan="10"></td><td>rs</td><td>rc_w1</td><td>rc_w1</td><td></td><td colspan="2">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>RFD1</td><td>释放一次FIFO1中的数据该位被置1,将释放FIFO1中的一帧数据。FIFO释放相应的数据空间后,该位被清0。</td></tr><tr><td>4</td><td>RFO1</td><td>接收FIFO1溢出当接收FIFO1溢出时被置位,由软件写1清0。0:接收FIFO1没有溢出1:接收FIFO1溢出</td></tr><tr><td>3</td><td>RFF1</td><td>接收FIFO1满当接收FIFO1满时被置位,由软件写1清0。0:接收FIFO1不满</td></tr></table>

1：接收 FIFO1 满

2 保留 必须保持复位值。

1:0 RFL1[1:0] 接收 FIFO1 中帧的数量

# 26.4.6. 中断使能寄存器 (CAN_INTEN)

地址偏移：0x14

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>SLPWIE</td><td>WIE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ERRIE</td><td colspan="3">保留</td><td>ERRNIE</td><td>BOIE</td><td>PERRIE</td><td>WERRIE</td><td>保留</td><td>RFOIE1</td><td>RFFIE1</td><td>RFNEIE1</td><td>RFOIE0</td><td>RFFIE0</td><td>RFNEIE0</td><td>TMEIE</td></tr><tr><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SLPWIE</td><td>睡眠中断使能0:禁用睡眠中断1:使能睡眠中断</td></tr><tr><td>16</td><td>WIE</td><td>唤醒中断使能0:禁用唤醒中断1:使能唤醒中断</td></tr><tr><td>15</td><td>ERRIE</td><td>错误中断使能0:禁用错误中断1:使能错误中断</td></tr><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>ERRNIE</td><td>错误种类中断使能0:禁用错误种类中断1:使能错误种类中断</td></tr><tr><td>10</td><td>BOIE</td><td>离线中断使能0:禁用离线中断1:使能离线中断</td></tr><tr><td>9</td><td>PERRIE</td><td>被动错误中断使能0:禁用被动错误1:使能被动错误</td></tr><tr><td>8</td><td>WERRIE</td><td>警告错误中断使能</td></tr></table>

<table><tr><td></td><td></td><td>0:禁用警告错误中断1:使能警告错误中断</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>RFOIE1</td><td>接收FIFO1溢出中断使能0:禁用接收FIFO1溢出中断1:使能接收FIFO1溢出中断</td></tr><tr><td>5</td><td>RFFIE1</td><td>接收FIFO1满中断使能0:禁用接收FIFO1满中断1:使能接收FIFO1满中断</td></tr><tr><td>4</td><td>RFNEIE1</td><td>接收FIFO1非空中断使能0:禁用接收FIFO1非空中断1:使能接收FIFO1非空中断</td></tr><tr><td>3</td><td>RFOIE0</td><td>接收FIFO0溢出中断使能0:禁用接收FIFO0溢出中断1:使能接收FIFO0溢出中断</td></tr><tr><td>2</td><td>RFFIE0</td><td>接收FIFO0满中断使能0:禁用接收FIFO0满中断1:使能接收FIFO0满中断</td></tr><tr><td>1</td><td>RFNEIE0</td><td>接收FIFO0非空中断使能0:禁用接收FIFO0非空中断1:使能接收FIFO0非空中断</td></tr><tr><td>0</td><td>TMEIE</td><td>发送邮箱空中断使能0:禁用发送邮箱空中断1:使能发送邮箱空中断</td></tr></table>

# 26.4.7. 错误寄存器（CAN_ERR）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">RECNT[7:0]</td><td colspan="8">TECNT[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="3">ERRN[2:0]</td><td>保留</td><td>BOERR</td><td>PERR</td><td>WERR</td></tr><tr><td colspan="8"></td><td colspan="5">rw</td><td>r</td><td>r</td><td>r</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:24</td><td>RECNT[7:0]</td><td>接收错误计数值</td></tr><tr><td>23:16</td><td>TECNT[7:0]</td><td>发送错误计数值</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>ERRN[2:0]</td><td>错误种类ERRN由硬件更新,可以反映位传输过程中的错误情况。当位传输成功没有错误时,ERRN为0。软件可以设置ERRN为0b111。000:无错误001:填充错误010:格式错误011:ACK错误100:位隐性错101:位显性错误110:CRC错误111:软件设置值</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>BOERR</td><td>离线错误当TEC上溢(超过255)时,CAN总线控制器进入离线状态,该位被置1。</td></tr><tr><td>1</td><td>PERR</td><td>被动错误当TECNT或者RECNT大于127时,该位由硬件置1。</td></tr><tr><td>0</td><td>WERR</td><td>警告错误当TECNT或RECNT大于等于96时,该位由硬件置1。</td></tr></table>

# 26.4.8. 位时序寄存器（CAN_BT）

地址偏移：0x1C

复位值：0x0123 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SCMOD</td><td>LCMOD</td><td colspan="4">保留</td><td colspan="2">SJW[1:0]</td><td>保留</td><td colspan="3">BS2[2:0]</td><td colspan="4">BS1[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="4"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">BAUDPSC[9:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SCMOD</td><td>静默通信模式0:禁用静默通信模式1:使能静默通信模式</td></tr><tr><td>30</td><td>LCMOD</td><td>回环通信模式</td></tr></table>

0：禁用回环通信模式

1：使能回环通信模式

29:26 保留 必须保持复位值。

25:24 SJW[1:0] 再同步补偿宽度

再同步补偿占用的时间单元数量= SJW[1:0]+1

23 保留 必须保持复位值。

22:20 BS2[2:0] 位段 2

位段 2 占用的时间单元数量=BS2[2:0]+1

19:16 BS1[3:0] 位段 1

位段 1 占用的时间单元数量=BS1[3:0]+1

15:10 保留 必须保持复位值。

9:0 BAUDPSC[9:0] 波特率分频系数

# 26.4.9. 发送邮箱标识符寄存器（CAN_TMIx）（x = 0...2）

地址偏移：0x180，0x190，0x1A0

复位值：0xXXXX XXXX（bit0 = 0）


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">SFID[10:0]/EFID[28:18]</td><td colspan="5">EFID[17:13]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">EFID[12:0]</td><td>FF</td><td>FT</td><td>TEN</td></tr><tr><td colspan="13">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:21</td><td>SFID[10:0]/EFID[28:1]</td><td>标识符</td></tr><tr><td></td><td>8]</td><td>SFID[10:0]:标准格式帧标识符</td></tr><tr><td></td><td></td><td>EFID[28:18]:扩展格式帧标识符</td></tr><tr><td>20:16</td><td>EFID[17:13]</td><td>标识符</td></tr><tr><td></td><td></td><td>EFID[17:13]:扩展格式帧标识符</td></tr><tr><td>15:3</td><td>EFID[12:0]</td><td>标识符</td></tr><tr><td></td><td></td><td>EFID[12:0]:扩展格式帧标识符</td></tr><tr><td>2</td><td>FF</td><td>帧格式</td></tr><tr><td></td><td></td><td>0:标准格式帧</td></tr><tr><td></td><td></td><td>1:扩展格式帧</td></tr><tr><td>1</td><td>FT</td><td>帧种类</td></tr></table>

0：数据帧

1：遥控帧

<table><tr><td>0</td><td>TEN</td><td>发送使能</td></tr><tr><td></td><td></td><td>当应用程序想要发送数据时,该位被置1将启动发送过程。当发送结束,发送邮箱为空时,该位由硬件清0。</td></tr><tr><td></td><td></td><td>0:禁用发送</td></tr><tr><td></td><td></td><td>1:使能发送</td></tr></table>

# 26.4.10. 发送邮箱属性寄存器（CAN_TMPx）（x = 0...2）

地址偏移：0x184，0x194，0x1A4

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">TS[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>TSEN</td><td colspan="4">保留</td><td colspan="4">DLENC[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>TS[15:0]</td><td>时间戳发送时间戳</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TSEN</td><td>时间戳使能0:禁用时间戳1:使能时间戳。时间戳 TS[15:0]将放在寄存器 CAN_TMDATA1 的 DATA6 和 DATA7 中只有当寄存器 CAN_CTL 中的 TTC 为 1 时,该位才有效。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>DLENC[3:0]</td><td>数据长度,DLENC[3:0]表示帧内数据长度。</td></tr></table>

# 26.4.11. 发送邮箱 data0 寄存器（CAN_TMDATA0x）（x = 0...2）

地址偏移：0x188，0x198，0x1A8

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB3[7:0]rw</td><td colspan="8">DB2[7:0]rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB1[7:0]</td><td colspan="8">DB0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB3[7:0]</td><td>字节 3</td></tr><tr><td>23:16</td><td>DB2[7:0]</td><td>字节 2</td></tr><tr><td>15:8</td><td>DB1[7:0]</td><td>字节 1</td></tr><tr><td>7:0</td><td>DB0[7:0]</td><td>字节 0</td></tr></table>

# 26.4.12. 发送邮箱 data1 寄存器（CAN_TMDATA1x）（x = 0...2）

地址偏移：0x18C，0x19C，0x1AC

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">DB7[7:0]</td><td colspan="9">DB6[7:0]</td></tr><tr><td colspan="7">rw</td><td colspan="9">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">DB5[7:0]</td><td colspan="9">DB4[7:0]</td></tr><tr><td colspan="7">rw</td><td colspan="9">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB7[7:0]</td><td>字节 7</td></tr><tr><td>23:16</td><td>DB6[7:0]</td><td>字节 6</td></tr><tr><td>15:8</td><td>DB5[7:0]</td><td>字节 5</td></tr><tr><td>7:0</td><td>DB4[7:0]</td><td>字节 4</td></tr></table>

# 26.4.13. 接收 FIFO 邮箱标识符寄存器（CAN_RFIFOMIx）（x = 0,1）

地址偏移：0x1B0，0x1C0

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">SFID[10:0]/EFID[28:18]</td><td colspan="5">EFID[17:13]</td></tr><tr><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>EFID[12:0]</td><td>FF</td><td>FT</td><td>保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td></td></tr></table>

<table><tr><td>位</td><td>区域</td><td>说明</td></tr><tr><td rowspan="2">31:21</td><td>SFID[10:0]/EFID[28:1]</td><td>标识符</td></tr><tr><td>8]</td><td>SFID[10:0]:标准格式帧标识符EFID[28:18]:扩展格式帧标识符</td></tr><tr><td>20:16</td><td>EFID[17:13]</td><td>标识符EFID[17:13]:扩展格式帧标识符</td></tr><tr><td>15:3</td><td>EFID[12:0]</td><td>标识符EFID[12:0]:扩展格式帧标识符</td></tr><tr><td>2</td><td>FF</td><td>帧格式0:标准格式帧1:扩展格式帧</td></tr><tr><td>1</td><td>FT</td><td>帧种类0:数据帧1:遥控帧</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 26.4.14. 接收 FIFO 邮箱属性寄存器（CAN_RFIFOMPx）（x = 0,1）

地址偏移：0x1B4，0x1C4

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">TS[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">FI[7:0]</td><td colspan="4">保留</td><td colspan="4">DLENC[3:0]</td></tr><tr><td colspan="12">r</td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>TS[15:0]</td><td>时间戳接收时间戳</td></tr><tr><td>15:8</td><td>FI[7:0]</td><td>过滤索引帧通过过滤器时的过滤序号</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>DLENC[3:0]</td><td>数据长度</td></tr></table>

DLENC[3:0]表示帧内数据长度。

# 26.4.15. 接收 FIFO 邮箱 data0 寄存器（CAN_RFIFOMDATA0x）（x=0,1）

地址偏移：0x1B8，0x1C8

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB3[7:0]</td><td colspan="8">DB2[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB1[7:0]</td><td colspan="8">DB0[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB3[7:0]</td><td>字节 3</td></tr><tr><td>23:16</td><td>DB2[7:0]</td><td>字节 2</td></tr><tr><td>15:8</td><td>DB1[7:0]</td><td>字节 1</td></tr><tr><td>7:0</td><td>DB0[7:0]</td><td>字节 0</td></tr></table>

# 26.4.16. 接收 FIFO 邮箱 data1 寄存器（CAN_RFIFOMDATA1x）（x=0,1）

地址偏移：0x1BC，0x1CC

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DB7[7:0]</td><td colspan="8">DB6[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">R</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DB5[7:0]</td><td colspan="8">DB4[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DB7[7:0]</td><td>字节 7</td></tr><tr><td>23:16</td><td>DB6[7:0]</td><td>字节 6</td></tr><tr><td>15:8</td><td>DB5[7:0]</td><td>字节 5</td></tr><tr><td>7:0</td><td>DB4[7:0]</td><td>字节 4</td></tr></table>

# 26.4.17. 过滤器控制寄存器（CAN_FCTL）（仅 CAN0 可用）

地址偏移：0x200

复位值：0x2A1C 0E01


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">HBC1F[5:0]</td><td colspan="7">保留</td><td>FLD</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>HBC1F[5:0]</td><td>CAN1 过滤器单元起始位置这些位用来定义 CAN1 过滤器起始位置。CAN0 可以用编号为 0~HBC1F-1 过滤器,CAN1 可以用编号为 HBC1F~27 过滤器。当这些位的值为 0,CAN0 将没有过滤器可以使用。当这些位的值为 28 时,CAN1 将没有过滤器可以使用。</td></tr><tr><td>7:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>FLD</td><td>过滤器锁禁用0:使能过滤器锁1:禁用过滤器锁</td></tr></table>

# 26.4.18. 过滤器模式配置寄存器（CAN_FMCFG）（仅 CAN0 可用）

地址偏移：0x204

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FMOD27</td><td>FMOD26</td><td>FMOD25</td><td>FMOD24</td><td>FMOD23</td><td>FMOD22</td><td>FMOD21</td><td>FMOD20</td><td>FMOD19</td><td>FMOD18</td><td>FMOD17</td><td>FMOD16</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FMOD15</td><td>FMOD14</td><td>FMOD13</td><td>FMOD12</td><td>FMOD11</td><td>FMOD10</td><td>FMOD9</td><td>FMOD8</td><td>FMOD7</td><td>FMOD6</td><td>FMOD5</td><td>FMOD4</td><td>FMOD3</td><td>FMOD2</td><td>FMOD1</td><td>FMOD0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:0</td><td>FMODx</td><td>过滤器模式0:掩码模式</td></tr></table>

1：列表模式

# 26.4.19. 过滤器位宽配置寄存器（CAN_FSCFG）（仅 CAN0 可用）

地址偏移：0x20C

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FS27</td><td>FS26</td><td>FS25</td><td>FS24</td><td>FS23</td><td>FS22</td><td>FS21</td><td>FS20</td><td>FS19</td><td>FS18</td><td>FS17</td><td>FS16</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FS15</td><td>FS14</td><td>FS13</td><td>FS12</td><td>FS11</td><td>FS10</td><td>FS9</td><td>FS8</td><td>FS7</td><td>FS6</td><td>FS5</td><td>FS4</td><td>FS3</td><td>FS2</td><td>FS1</td><td>FS0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:0</td><td>FSx</td><td>过滤器位宽0: 16-bit 位宽1: 32-bit 位宽</td></tr></table>

# 26.4.20. 过滤器关联 FIFO 寄存器（CAN_FAFIFO）（仅 CAN0 可用）

地址偏移：0x214

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FAF27</td><td>FAF26</td><td>FAF25</td><td>FAF24</td><td>FAF23</td><td>FAF22</td><td>FAF21</td><td>FAF20</td><td>FAF19</td><td>FAF18</td><td>FAF17</td><td>FAF16</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>Rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FAF15</td><td>FAF14</td><td>FAF13</td><td>FAF12</td><td>FAF11</td><td>FAF10</td><td>FAF9</td><td>FAF8</td><td>FAF7</td><td>FAF6</td><td>FAF5</td><td>FAF4</td><td>FAF3</td><td>FAF2</td><td>FAF1</td><td>FAF0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>Rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:0</td><td>FAFx</td><td>过滤器关联FIFO0: 关联FIFO01: 关联FIFO1</td></tr></table>

# 26.4.21. 过滤器激活寄存器（CAN_FW）（仅 CAN0 可用）

地址偏移：0x21C

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FW27</td><td>FW26</td><td>FW25</td><td>FW24</td><td>FW23</td><td>FW22</td><td>FW21</td><td>FW20</td><td>FW19</td><td>FW18</td><td>FW17</td><td>FW16</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FW15</td><td>FW14</td><td>FW13</td><td>FW12</td><td>FW11</td><td>FW10</td><td>FW9</td><td>FW8</td><td>FW7</td><td>FW6</td><td>FW5</td><td>FW4</td><td>FW3</td><td>FW2</td><td>FW1</td><td>FW0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:0</td><td>FWx</td><td>过滤器激活0:没有激活1:激活工作</td></tr></table>

# 26.4.22. 过滤器（x）数据（y）寄存器（CAN_FxDATAy）（x = 0...27, y = 0,1）（仅 CAN0可用）

地址偏移： $0 \times 2 4 0 + 8 \times { \mathsf { x } } + 4 \ { \mathsf { \Pi } } ^ { \star } \lor , \quad ( { \mathsf { x } } = 0 . . 2 7 , \lor = 0 , 1 )$ 

复位值：0xXXXX XXXX


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FD31</td><td>FD30</td><td>FD29</td><td>FD28</td><td>FD27</td><td>FD26</td><td>FD25</td><td>FD24</td><td>FD23</td><td>FD22</td><td>FD21</td><td>FD20</td><td>FD19</td><td>FD18</td><td>FD17</td><td>FD16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FD15</td><td>FD14</td><td>FD13</td><td>FD12</td><td>FD11</td><td>FD10</td><td>FD9</td><td>FD8</td><td>FD7</td><td>FD6</td><td>FD5</td><td>FD4</td><td>FD3</td><td>FD2</td><td>FD1</td><td>FD0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FDx</td><td>过滤器数据掩码模式下:0:标识符的 Bit(x)不需参与比较1:标识符的 Bit(x)需要参与比较列表模式下:0:标识符的 Bit(x)必须为 01:标识符的 Bit(x)必须为 1</td></tr></table>
