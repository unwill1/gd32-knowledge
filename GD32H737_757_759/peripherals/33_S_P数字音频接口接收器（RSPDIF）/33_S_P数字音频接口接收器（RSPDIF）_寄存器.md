# 33.4. RSPDIF 寄存器

RSPDIF基地址：0x4000 4000

# 33.4.1. 控制寄存器（RSPDIF_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>BKSCKEN</td><td>SCKEN</td><td>保留</td><td colspan="3">RXCHSEL[2:0]</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>WFRXA</td><td colspan="2">MAXRT[1:0]</td><td>CFCHSEL</td><td>DMACBEN</td><td>PTNCPEN</td><td>CUNCPEN</td><td>VNCPEN</td><td>PNCPEN</td><td colspan="2">RXDF[1:0]</td><td>RXSTEOMEN</td><td>DMAREN</td><td colspan="2">RXCFG[1:0]</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>BKSCKEN</td><td>备份符号时钟使能位软件置1和清0。0: RSPDIF不生成备用符号时钟。1: 当SCKEN=1,RSPDIF生成一个备用符号时钟。请参考RSPDIF时钟管理如何编程该区域。</td></tr><tr><td>20</td><td>SCKEN</td><td>符号时钟使能位软件置1和清0。0: RSPDIF不生成符号时钟。1: RSPDIF生成一个符号时钟。请参考RSPDIF时钟管理如何编程该区域。</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>RXCHSEL[2:0]</td><td>RSPDIF输入通道选择000: 选择RSPDIF_CH0001: 选择RSPDIF_CH1010: 选择RSPDIF_CH2011: 选择RSPDIF_CH3100~111: 保留</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>WFRXA</td><td>等待选定的RSPDIF通道的4个有效转换信号软件置1和清0。0: 在启动同步进程之前,RSPDIF不等待选定的RSPDIF通道的有效转换信号。1:在启动同步进程之前,RSPDIF等待选定的RSPDIF通道的有效转换信号。</td></tr><tr><td>13:12</td><td>MAXRT[1:0]</td><td>RSPDIF同步阶段允许的最大重试次数00:不允许重试(仅一次机会)01:允许最多3次重试10:允许最多15次重试11:允许最多63次重试</td></tr><tr><td>11</td><td>CFCHSEL</td><td>控制流获取通道状态源选择软件置1和清0。0:从通道A获取通道状态1:从通道B获取通道状态</td></tr><tr><td>10</td><td>DMACBEN</td><td>控制流的控制缓冲区DMA使能位软件置1和清0。0:禁能控制流DMA模式。1:使能控制流DMA模式。当该位置位时,每当CBEN标志置位就会生成DMA请求。</td></tr><tr><td>9</td><td>PTNCPEN</td><td>报头类型位域不复制使能位软件置1和清0。0:将报头类型位域复制到RSPDIF_DATA中。1:不将报头类型位域复制到RSPDIF_DATA中,而是写0来替代。</td></tr><tr><td>8</td><td>CUNCPEN</td><td>通道信息位和用户信息位不复制使能位软件置1和清0。0:将通道信息位和用户信息位复制到RSPDIF_DATA中。1:不将通道信息位和用户信息位复制到RSPDIF_DATA中,而是写0来替代。</td></tr><tr><td>7</td><td>VNCPEN</td><td>有效位不复制使能位软件置1和清0。0:将有效位复制到RSPDIF_DATA中。1:不将有效位复制到RSPDIF_DATA中,而是写0来替代。</td></tr><tr><td>6</td><td>PNCPEN</td><td>奇偶校验位不复制使能位软件置1和清0。0:将奇偶校验位复制到RSPDIF_DATA中。1:不将奇偶校验位复制到RSPDIF_DATA中,而是写0来替代。</td></tr><tr><td>5:4</td><td>RXDF[1:0]</td><td>接收数据格式选择软件置1和清0。00:数据格式为RSPDIF_DATA_F0寄存器所描述的格式,音频数据右对齐(LSB)01:数据格式为RSPDIF_DATA_F1寄存器所描述的格式,音频数据左对齐(MSB)10:数据格式为RSPDIF_DATA_F2寄存器所描述的格式,将两个16位的音频数据打包为一个32位的数据11:保留</td></tr><tr><td>3</td><td>RXSTEOMEN</td><td>接收立体声模式使能位软件置1和清0。</td></tr></table>

0：单声道模式

1：立体声模式

这一比特位用于在溢出情况下，以处理不对齐的情况。

2 DMAREN 

数据流接收 DMA 使能位

软件置 1 和清 0。

0：禁能接收 DMA

1：使能接收 DMA

当设置此位时，每当 RBNE 置位时，就生成接收 DMA 请求。

1:0 RXCFG[1:0] 

RSPDIF 配置

00：禁用 RSPDIF

01：只使能 RSPDIF 同步

10：保留

11：使能 RSPDIF

# 33.4.2. 中断使能寄存器（RSPDIF_INTEN）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>RXDCERRIE</td><td>SYNDOIE</td><td>SYNDBIE</td><td>RXORERRIE</td><td>PERRIE</td><td>CBNEIE</td><td>RBNEIE</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

位/位域 名称

描述

31:7 保留

必须保持复位值。

6 RXDCERRIE 

RSPDIF 数据解码错误中断使能

软件置 1 和清 0。

0：禁能中断

1：使能中断

当该位置位时，如果RSPDIF_STAT寄存器中的SYNERR或TMOUTERR或FRERR置位，就会产生 RSPDIF 数据解码错误中断。

5 SYNDOIE 

同步完成中断使能

软件置 1 和清 0。

0：禁能中断

1：使能中断

当该位置位时，如果 RSPDIF_STAT 寄存器中的 SYNDO 位置位，就会产生同步完成中断。

<table><tr><td>4</td><td>SYNDBIE</td><td>同步块检测中断使能软件置1和清0。0:禁能中断1:使能中断当该位置位时,如果RSPDIF_STAT寄存器中的SYNDB位置位,就会产生同步块检测中断。</td></tr><tr><td>3</td><td>RXORERRIE</td><td>接收上溢错误中断使能软件置1和清0。0:禁能中断1:使能中断当该位置位时,如果RSPDIF_STAT寄存器中的RXORERR位置位,就会产生接收上溢错误中断。</td></tr><tr><td>2</td><td>PERRIE</td><td>校验错误中断使能软件置1和清0。0:禁能中断1:使能中断当该位置位时,如果RSPDIF_STAT寄存器中的PERR位置位,就会产生校验错误中断。</td></tr><tr><td>1</td><td>CBNEIE</td><td>RSPDIF_CHSTAT寄存器非空中断使能软件置1和清0。0:禁能中断1:使能中断当该位置位时,如果RSPDIF_STAT寄存器中的CBNE位置位,就会产生控制流接收寄存器非空中断。</td></tr><tr><td>0</td><td>RBNEIE</td><td>RSPDIF_DATA寄存器非空中断使能软件置1和清0。0:禁能中断1:使能中断当该位置位时,如果RSPDIF_STAT寄存器中的RBNE位置位,就会产生接收数据寄存器非空中断。</td></tr></table>

# 33.4.3. 状态寄存器（RSPDIF_STAT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="15">CKCNT5[14:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>TMOUTE</td><td>SYNERR</td><td>FRERR</td><td>SYNDO</td><td>SYNDB</td><td>RXORER</td><td>PERR</td><td>CBNE</td><td>RBNE</td></tr><tr><td colspan="7"></td><td>RR</td><td></td><td></td><td></td><td></td><td>R</td><td></td><td></td><td></td></tr><tr><td colspan="7"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:16</td><td>CKCNT5[14:0]</td><td>使用rspdif_ck计数的5个符号的连续时间的时钟周期数该值可用于估算S/PDIF符号率。其精度受rspdif_ck的频率限制。例如,如果rspdif_ck固定为84 MHz,则CKCNT5=147d。S/PDIF数据流的采样率估算值为:<eq>F_s = 5 \times rspdif\_ck / (CKCNT5 \times 64) \sim 44.6 \text{ kHz}</eq>,因此最接近的标准采样率为44.1 kHz。请注意,当SYNDO变为高电平时,硬件更新CKCNT5,并且每帧数据更新时CKCNT5都更新。</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TMOUTERR</td><td>超时错误0:未检测到超时错误1:检测到超时错误当计数器TWCNT值达到最大值时,该位由硬件置1。它表示两次转换之间的时间间隔过长。这通常意味着RSPDIF_CH上没有有效信号。如果RSPDIF_INTEN寄存器中RXDCERRIE=1,则会生成中断。该标志通过将RXCFG[1:0]写为0来清零。</td></tr><tr><td>7</td><td>SYNERR</td><td>同步错误0:未检测到同步错误1:检测到同步错误当由于MAXRT重试次数方面的原因同步失败时,该位由硬件置1。如果RSPDIF_INTEN寄存器中RXDCERRIE=1,则会生成中断。该标志通过将RXCFG[1:0]写0来清零。</td></tr><tr><td>6</td><td>FRERR</td><td>帧错误0:未检测到曼彻斯特编码错误1:检测到曼彻斯特编码错误当在接收数据期间发生错误时,该位由硬件置1。报头未出现在预期位置,短转换未按对分组。仅当同步完成时(SYNDO=1),该位才能由硬件置1。如果RSPDIF_INTEN寄存器中RXDCERRIE=1,则会生成中断。该标志通过将RXCFG[1:0]写为0来清零。</td></tr><tr><td>5</td><td>SYNDO</td><td>同步完成0:同步挂起1:同步完成当同步阶段完成时,该位由硬件置1。如果RSPDIF_INTEN寄存器中SYNDOIE=1,则会生成中断。置位RSPDIF_STATC寄存器中SYNDOC位,即可将该标志清零。</td></tr><tr><td>4</td><td>SYNDB</td><td>已检测到同步块0:未检测到“B”报头1:已检测到“B”报头当检测到“B”报头时,该位由硬件置1。如果RSPDIF_INTEN寄存器中SYNDBIE=1,则会生成中断。置位RSPDIF_STATC寄存器中SYNDBC位,即可将该标志清零。</td></tr><tr><td>3</td><td>RXORERR</td><td>接收上溢错误0:无上溢错误1:检测到上溢错误在RBNE=1且RSPDIF_DATA和RX缓存均已满的情况下,RSPDIF仍在接收数据时,该位由硬件置1。如果RSPDIF_INTEN寄存器中RXORERRIE=1,则会生成中断。置位RSPDIF_STATC寄存器中RXORERRC位,即可将该标志清零。注意:当该位置1时,RSPDIF_DATA寄存器的内容不会丢失,但最后接收的数据会丢失。</td></tr><tr><td>2</td><td>PERR</td><td>校验错误0:无奇偶校验错误1:奇偶校验错误当所接收子帧的数据和状态位中包含奇数个0和1时,该位由硬件置1。如果RSPDIF_INTEN寄存器中PERRIE=1,则会生成中断。置位RSPDIF_STATC寄存器中PERRC位,即可将该标志清零。</td></tr><tr><td>1</td><td>CBNE</td><td>RSPDIF_CHSTAT寄存器非空0:RSPDIF_CHSTAT寄存器中无控制流数据1:RSPDIF_CHSTAT寄存器中有控制流数据当RSPDIF_CHSTAT寄存器中有控制流数据时,该位由硬件置1。如果RSPDIF_INTEN寄存器中CBNEIE=1,则会生成中断。当读取RSPDIF_CHSTAT寄存器时,该标志清零。</td></tr><tr><td>0</td><td>RBNE</td><td>RX缓存非空0:未接收到数据1:已接收到数据当有效数据进入RX缓存时,该位由硬件置1。如果RSPDIF_INTEN寄存器中RBNEIE=1,则会生成中断。可通过读取RSPDIF_DATA寄存器清零该标志。</td></tr></table>

# 33.4.4. 状态清除寄存器（RSPDIF_STATC）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYNDO</td><td>SYNDBC</td><td>RXORER</td><td>PERRC</td><td colspan="2">保留</td></tr><tr><td colspan="10"></td><td>C</td><td></td><td>RC</td><td></td><td colspan="2"></td></tr><tr><td colspan="10"></td><td>w</td><td>w</td><td>w</td><td>w</td><td colspan="2"></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>SYNDOC</td><td>清除同步完成标志将该位置1,清除RSPDIF_STAT寄存器中SYNDO标志。</td></tr><tr><td>4</td><td>SYNDBC</td><td>清除已检测到同步块标志将该位置1,清除RSPDIF_STAT寄存器中SYNDB标志。</td></tr><tr><td>3</td><td>RXORERRC</td><td>清除接收上溢错误标志将该位置1,清除RSPDIF_STAT寄存器中RXORERR标志。</td></tr><tr><td>2</td><td>PERRC</td><td>清除校验错误标志将该位置1,清除RSPDIF_STAT寄存器中PERR标志。</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 33.4.5. 接收数据寄存器（RSPDIF_DATA）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

根据 RXDF[1:0]值，接收数据寄存器有三种不同格式。

当 RXDF[1:0]= 2’b00，格式如下：


接收数据寄存器格式 0（RSPDIF_DATA_F0）


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">PREF[1:0]</td><td>C</td><td>U</td><td>V</td><td>P</td><td colspan="8">DATA[23:16]</td></tr><tr><td colspan="2"></td><td colspan="2">r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="3"></td><td colspan="5">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>PREF[1:0]</td><td>报头类型位这些位表示接收到的报头类型。00:未使用01:接收到报头B10:接收到报头M11:接收到报头W</td></tr></table>

请注意，如果 PTNCPEN = 1，该位域将强制被设置为零。

27 C 通道状态位

请注意，如果 CUNCPEN = 1，该位域将强制被设置为零。

26 U 用户位

请注意，如果 CUNCPEN = 1，该位域将强制被设置为零。

25 V 有效位

请注意，如果 VNCPEN = 1，该位域将强制被设置为零。

24 P 校验位

请注意，如果 PNCPEN = 1，该位域将强制被设置为零。

23:0 DATA[23:0] 数据位

包含 24 个接收到的数据位，数据右对齐。

当 RXDF[1:0]= 2’b01，格式如下：


接收数据寄存器格式 1（RSPDIF_DATA_F1）


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA [23:8]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DATA [7:0]</td><td colspan="2">保留</td><td colspan="2">PREF[1:0]</td><td>C</td><td>U</td><td>V</td><td>P</td></tr><tr><td colspan="10">r</td><td colspan="2">r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:8</td><td>DATA[23:0]</td><td>数据位包含24个接收到的数据位,数据左右对齐。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>PREF[1:0]</td><td>报头类型位域这些位表示接收到的报头类型。00:未使用01:接收到报头B10:接收到报头M11:接收到报头W请注意,如果PTNCPEN=1,该位域将强制被设置为零。</td></tr><tr><td>3</td><td>C</td><td>通道状态位请注意,如果CUNCPEN=1,该位域将强制被设置为零。</td></tr><tr><td>2</td><td>U</td><td>用户位请注意,如果CUNCPEN=1,该位域将强制被设置为零。</td></tr><tr><td>1</td><td>V</td><td>有效位</td></tr></table>

请注意，如果 VNCPEN = 1，该位域将强制被设置为零。

0 P 校验位

请注意，如果 PNCPEN = 1，该位域将强制被设置为零。

当 RXDF[1:0]=2’b10，格式如下：


接收数据寄存器格式 2（RSPDIF_DATA_F2）


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA2[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA1[15:0]</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:16</td><td>DATA2[15:0]</td><td>当为立体声模式时,包含通道A数据。当为单声道模式时,包含的为最老的数据。</td></tr><tr><td>15:0</td><td>DATA1[15:0]</td><td>当为立体声模式时,包含通道B数据。当为单声道模式时,包含的为最新的数据。</td></tr></table>

# 33.4.6. 接收通道状态寄存器（RSPDIF_CHSTAT）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>SOB</td><td colspan="8">CHS[7:0]</td></tr><tr><td colspan="10">r</td><td colspan="6">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">USER[15:0]</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>SOB</td><td>块起始该位表示位 CHS[0]是否对应于新块的第一位0:CHS[0]不是新块的第一位1:CHS[0]是新块的第一位</td></tr><tr><td>23:16</td><td>CHS[7:0]</td><td>通道状态信息CHS[0]是最早的值。</td></tr></table>

<table><tr><td>15:0</td><td>USER[15:0]</td><td>用户数据信息位</td></tr><tr><td></td><td></td><td>USER[0]是最早的值,来自通道A,USER[1]来自通道B。因此,n为偶数时,USER[n]位来自通道A,否则来自通道B。</td></tr></table>

# 33.4.7. 接收阈值寄存器（RSPDIF_DTH）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="13">THLO[12:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="13">THHI[12:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:16</td><td>THLO[12:0]</td><td>阈值下限<eq>THLO = 1.5 \times UI / T_{rspdif\_ck}</eq>该位域包含当前阈值下限的估算值。该值可用于估算接收数据流的采样率。THLO的精度受限于 <eq>rspdif\_ck</eq> 的周期。采样率按如下公式估算:采样率 = [2 x THLO x <eq>T_{rspdif\_ck}</eq>+/- <eq>T_{rspdif\_ck}</eq>] x 2/3请注意,当SYNDO变为高电平时,THLO将由硬件更新,随后每帧都更新。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:0</td><td>THHI[12:0]</td><td>阈值上限<eq>THHI = 2.5 \times UI / T_{rspdif\_ck}</eq>该位域包含当前阈值上限的估算值。该值可用于估算接收数据流的采样率。THHI的精度受限于 <eq>rspdif\_ck</eq> 的周期。采样率按如下公式估算:采样率= [2 x THHI x <eq>T_{rspdif\_ck}</eq>+/- <eq>T_{rspdif\_ck}</eq>] x 2/5请注意,当SYNDO变为高电平时,THHI将由硬件更新,随后每帧都更新。</td></tr></table>
