# 20.7. ADC 寄存器

ADC0 基地址： 0x4001 2400

ADC1 基地址:：0x4001 2800

ADC2 基地址:：0x4001 2C00

# 20.7.1. 状态寄存器（ADC_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WDE2</td><td>WDE1</td><td colspan="14">保留</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ROVF</td><td>STRC</td><td colspan="2">保留</td><td>EOC</td><td>WDE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WDE2</td><td>模拟看门狗2事件标志0:没有模拟看门狗2事件1:产生模拟看门狗2事件转换电压超过ADC_WDLT2和ADC_WDHT2寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>30</td><td>WDE1</td><td>模拟看门狗1事件标志0:没有模拟看门狗1事件1:产生模拟看门狗1事件转换电压超过ADC_WDLT1和ADC_WDHT1寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>29:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ROVF</td><td>常规序列数据寄存器溢出0:常规序列数据寄存器没有溢出1:常规序列数据寄存器溢出在单次或多次模式中,当常规序列数据寄存器溢出时,该位由硬件置位。只有在DMA使能或者转换结束模式被置1(EOCM=1)时,这个标志位才会置位。如果出现ROVF置位,则最后的常规序列数据会被丢失。软件写“0”清除。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0:转换没有开始1:转换开始</td></tr></table>

常规序列转换开始时硬件置位，软件写0清除。

3:2 保留 必须保持复位值。

1 EOC 常规序列转换结束标志

0：转换没有结束

1：转换结束

常规序列转换结束时硬件置位，软件写 0 或读 ADC_RDATA 寄存器清除。

0 WDE0 模拟看门狗 0 事件标志

0： 没有模拟看门狗0 事件

1： 产生模拟看门狗0 事件

转换电压超过 ADC_WDLT0和 ADC_WDHT0 寄存器设定的阈值时由硬件置 1，软件写 0 清除。

# 20.7.2. 控制寄存器 0（ADC_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WDE2IE</td><td>WDE1IE</td><td colspan="3">保留</td><td>ROVFIE</td><td colspan="2">DRES[1:0]</td><td>RWD0EN</td><td colspan="7">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="7"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM[2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WD0SC</td><td>SM</td><td>保留</td><td>WDE0IE</td><td>EOCIE</td><td colspan="5">WD0CHSEL[4:0]</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WDE2IE</td><td>WDE2 中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>30</td><td>WDE1IE</td><td>WDE1 中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>29:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>ROVFIE</td><td>常规序列溢出 ROVF 中断使能0: ROVF 中断失能1: ROVF 中断使能</td></tr><tr><td>25:24</td><td>DRES[1:0]</td><td>ADC0/1 数据分辨率00:14 位01:12 位10:10 位11:8 位</td></tr></table>

<table><tr><td></td><td></td><td>ADC2 数据分辨率00:12位01:10位10:8位11:6位</td></tr><tr><td>23</td><td>RWD0EN</td><td>常规序列看门狗 0 使能0:常规序列看门狗 0 禁止1:常规序列看门狗 0 使能</td></tr><tr><td>22:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成 DISNUM[2:0]+1</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0:间断运行模式禁止1:间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WD0SC</td><td>扫描模式下,模拟看门狗 0 在单通道配置0:模拟看门狗 0 在所有通道有效1:模拟看门狗 0 在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0:扫描运行模式禁止1:扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WDE0IE</td><td>WDE0 中断使能0:中断禁止1:中断使能</td></tr><tr><td>5</td><td>EOCIE</td><td>EOC 中断使能0:中断禁止1:中断使能</td></tr><tr><td>4:0</td><td>WDCHSEL[4:0]</td><td>模拟看门狗通道选择00000:ADC 通道 000001:ADC 通道 100010:ADC 通道 200011:ADC 通道 300100:ADC 通道 400101:ADC 通道 500110:ADC 通道 600111:ADC 通道 7</td></tr></table>

01000:ADC 通道 8

01001:ADC 通道 9

01010:ADC 通道 10

01011:ADC 通道 11

01100:ADC 通道 12

01101:ADC 通道 13

01110:ADC 通道 14

01111:ADC 通道 15

10000:ADC 通道 16

10001:ADC 通道 17

10010:ADC 通道 18

10000:ADC 通道 19

10001:ADC 通道 20

其他值保留。

注意：ADC0 模拟输入通道20内部连接至 DAC0_OUT0。ADC1 模拟输入通道

16、通道 17 和通道 20 内部连接至电池、VREFINT输入、DAC0_OUT1。ADC2 模拟输入通道 17、通道 18、通道 19 和通道 20 内部连接至 VBAT、温度传感器、VREFINT输入和高精度温度传感器。

# 20.7.3. 控制寄存器 1（ADC_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TSVEN2</td><td>SWRCST</td><td colspan="2">ETMRC[1:0]</td><td>CALMOD</td><td>保留</td><td>VBATEN</td><td>INREFEN</td><td>TSVEN1</td><td colspan="7">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="7"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>HPDFCFG</td><td>DAL</td><td>EOCM</td><td>DDM</td><td>DMA</td><td>保留</td><td colspan="3">CALNUM[2:0]</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域



名称



描述


<table><tr><td>31</td><td>TSVEN2</td><td>在ADC2中,该位可由软件置位或清零。ADC2通道20(高精度温度传感器)使能。0:高精度温度传感器通道失能1:高精度温度传感器通道使能</td></tr><tr><td>30</td><td>SWRCST</td><td>软件触发常规序列启动转换该位置1开启常规序列转换。软件置位,软件清零,或转换开始后,立刻由硬件清零。</td></tr><tr><td>29:28</td><td>ETMRC[1:0]</td><td>常规序列外部触发模式00:常规序列外部触发失能01:常规序列外部触发上升沿使能10:常规序列外部触发下降沿使能11:常规序列外部触发双边沿使能</td></tr><tr><td>27</td><td>CALMOD</td><td>ADC校准模式(适用于ADC0/1)0:校准失调和失配1:校准失调</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>VBATEN</td><td>在ADC2中,该位可由软件置位或清零。使能ADC1的通道16(外部电池电压的1/4)使能ADC2的通道17(外部电池电压的1/4)0:外部电池电压的1/4失能1:外部电池电压的1/4使能</td></tr><tr><td>24</td><td>INREFEN</td><td>在ADC2中,该位可由软件置位或清零。使能ADC1的通道17(内部参考电压)使能ADC2的通道19(内部参考电压)0:内部参考电压失能1:内部参考电压使能</td></tr><tr><td>23</td><td>TSVEN1</td><td>在ADC2中,该位可由软件置位或清零。ADC2通道18(温度传感器)使能。0:温度传感器通道失能1:温度传感器通道使能</td></tr><tr><td>22:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>HPDFCFG</td><td>HPDF模式配置该位由软件置位或清零,使能或使能HPDF模式。仅在DMA=0时有效。0:HPDF模式失能1:HPDF模式使能</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0:最低有效位对齐1:最高有效位对齐</td></tr><tr><td>10</td><td>EOCM</td><td>转换结束模式0:只有在常规转换序列转换结束时,才将EOC置1。如果不设置DMA=1,则溢出检测失能。1:在每个常规序列转换结束时,将EOC置1。溢出检测自动使能。</td></tr><tr><td>9</td><td>DDM</td><td>DMA失能模式该位用于在单次ADC模式下配置DMA失能。0:DMA机制在DMA控制器的传输结束信号之后失能。1:当DMA=1,在每个常规序列转换结束时DMA机制产生一个DMA请求。</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0:DMA请求禁止1: DMA 请求使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CALNUM[2:0]</td><td>校准次数这些位定义了 ADC 的校准次数。000: 1 次001: 2 次010: 4 次011: 8 次100: 16 次101: 32 次(只针对 12 位 ADC)其它: 保留。</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位在校准寄存器初始化后该位可以软件置位和硬件清零。0: 校准寄存器初始化结束.1: 校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC 校准0: 校准结束1: 校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0: 禁止连续运行模式1: 使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启 ADC。该位从 0 变成 1 将唤醒 ADC。为了省电,当该位为 0 时,模拟子模块将会进入掉电模式。0: 失能 ADC,并进入掉电模式1: 使能 ADC</td></tr></table>

# 20.7.4. 看门狗高阈值寄存器 0（ADC_WDHT0）

地址偏移：0x1C

复位值：0x00FF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDHT0[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDHT0[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr></table>

23:0 WDHT0[23:0] 模拟看门狗 0 高侧阈值，对于 ADC0/1 位 WDHT0 [23:0]，对于 ADC2 位 WDHT0[11:0]。

这些位定义了模拟看门狗 0 的高侧阈值。

# 20.7.5. 看门狗低阈值寄存器 0（ADC_WDLT0）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDLT0[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDLT0[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>WDLT0[23:0]</td><td>模拟看门狗 0 低侧阈值,对于 ADC0/1 位 WDLT0 [23:0],对于 ADC2 位 WDLT0 [11:0]。这些位定义了模拟看门狗 0 的低侧阈值。</td></tr></table>

# 20.7.6. 常规序列寄存器 0（ADC_RSQ0）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td colspan="4">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP15[9:0]</td><td colspan="5">RSQ15[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规通道序列长度常规通道转换序列中的总的通道数目为 RL[3:0]+1。</td></tr><tr><td>19:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP15[9:0]</td><td>常规通道采样时间</td></tr></table>

10’d0：ADC0/1 为 3.5 周期，ADC2 为 2.5 周期

10’d1：ADC0/1 为 4.5 周期，ADC2 为 3.5 周期

10’d2：ADC0/1 为 5.5 周期，ADC2 为 4.5 周期

10’d3：ADC0/1 为 6.5 周期，ADC2 为 5.5 周期

10’d4：ADC0/1 为 7.5 周期，ADC2 为 6.5 周期

10’d638：ADC0/1 为 641.5 周期，ADC2 为 640.5 周期

10’d639：只有 ADC0/1 为 642.5 周期

10’d807：只有 ADC0/1 为 810.5 周期

其余位保留

4:0 RSQ15[4:0] 参考 RSQ0[4:0]描述

# 20.7.7. 常规序列寄存器 1（ADC_RSQ1）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP14[9:0]</td><td colspan="5">RSQ14[4:0]</td></tr><tr><td></td><td colspan="10">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP13[9:0]</td><td colspan="5">RSQ13[4:0]</td></tr><tr><td></td><td colspan="10">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP14[9:0]</td><td>常规通道采样时间10&#x27;d0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10&#x27;d1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10&#x27;d2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10&#x27;d3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10&#x27;d4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10&#x27;d638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10&#x27;d639: 只有 ADC0/1 为 642.5 周期......10&#x27;d807: 只有 ADC0/1 为 810.5 周期其余位保留</td></tr><tr><td>20:16</td><td>RSQ14[4:0]</td><td>参考 RSQ0[4:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>14:5</td><td>RSMP13[9:0]</td><td>常规通道采样时间</td></tr><tr><td></td><td></td><td>10&#x27;d0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期</td></tr><tr><td></td><td></td><td>10&#x27;d1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期</td></tr><tr><td></td><td></td><td>10&#x27;d2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期</td></tr><tr><td></td><td></td><td>10&#x27;d3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期</td></tr><tr><td></td><td></td><td>10&#x27;d4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>10&#x27;d638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期</td></tr><tr><td></td><td></td><td>10&#x27;d639: 只有 ADC0/1 为 642.5 周期</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>10&#x27;d807: 只有 ADC0/1 为 810.5 周期</td></tr><tr><td></td><td></td><td>其余位保留</td></tr><tr><td>4:0</td><td>RSQ13[4:0]</td><td>参考 RSQ0[4:0]描述</td></tr></table>

# 20.7.8. 常规序列寄存器 2（ADC_RSQ2）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP12[9:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP11[9:0]</td><td colspan="5">RSQ11[4:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP12[9:0]</td><td>常规通道采样时间10'd0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10'd1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10'd2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10'd3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10'd4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10'd638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10'd639: 只有 ADC0/1 为 642.5 周期......10'd807: 只有 ADC0/1 为 810.5 周期其余位保留</td></tr><tr><td>20:16</td><td>RSQ12[4:0]</td><td>参考 RSQ0[4:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP11[9:0]</td><td>常规通道采样时间10'd0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10'd1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10'd2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10'd3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10'd4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10'd638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10'd639: 只有 ADC0/1 为 642.5 周期......10'd807: 只有 ADC0/1 为 810.5 周期其余位保留</td></tr><tr><td>4:0</td><td>RSQ11[4:0]</td><td>参考 RSQ0[4:0]描述</td></tr></table>

# 20.7.9. 常规序列寄存器 3（ADC_RSQ3）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP10[9:0]</td><td colspan="5">RSQ10[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP9[9:0]</td><td colspan="5">RSQ9[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP10[9:0]</td><td>常规通道采样时间10'd0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10'd1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10'd2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10'd3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10'd4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10'd638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10'd639: 只有 ADC0/1 为 642.5 周期......10'd807: 只有 ADC0/1 为 810.5 周期其余位保留</td></tr><tr><td>20:16</td><td>RSQ10[4:0]</td><td>参考RSQ0[4:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP9[9:0]</td><td>常规通道采样时间10'd0: ADC0/1为3.5周期,ADC2为2.5周期10'd1: ADC0/1为4.5周期,ADC2为3.5周期10'd2: ADC0/1为5.5周期,ADC2为4.5周期10'd3: ADC0/1为6.5周期,ADC2为5.5周期10'd4: ADC0/1为7.5周期,ADC2为6.5周期......10'd638: ADC0/1为641.5周期,ADC2为640.5周期10'd639: 只有ADC0/1为642.5周期......10'd807: 只有ADC0/1为810.5周期其余位保留</td></tr><tr><td>4:0</td><td>RSQ9[4:0]</td><td>参考RSQ0[4:0]描述</td></tr></table>

# 20.7.10. 常规序列寄存器 4（ADC_RSQ4）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP8[9:0]</td><td colspan="5">RSQ8[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP7[9:0]</td><td colspan="5">RSQ7[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP8[9:0]</td><td>常规通道采样时间10&#x27;d0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10&#x27;d1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10&#x27;d2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10&#x27;d3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10&#x27;d4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10&#x27;d638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10&#x27;d639: 只有 ADC0/1 为 642.5 周期......10&#x27;d807: 只有 ADC0/1 为 810.5 周期</td></tr></table>

其余位保留

20:16 RSQ8[4:0] 参考 RSQ0[4:0]描述

15 保留 必须保持复位值。

14:5 RSMP7[9:0] 常规通道采样时间

10’d0：ADC0/1 为 3.5 周期，ADC2 为 2.5 周期

10’d1：ADC0/1 为 4.5 周期，ADC2 为 3.5 周期

10’d2：ADC0/1 为 5.5 周期，ADC2 为 4.5 周期

10’d3：ADC0/1 为 6.5 周期，ADC2 为 5.5 周期

10’d4：ADC0/1 为 7.5 周期，ADC2 为 6.5 周期

10’d638：ADC0/1 为 641.5 周期，ADC2 为 640.5 周期

10’d639：只有 ADC0/1 为 642.5 周期

10’d807：只有 ADC0/1 为 810.5 周期

其余位保留

4:0 RSQ7[4:0] 参考 RSQ0[4:0]描述

# 20.7.11. 常规序列寄存器 5（ADC_RSQ5）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP6[9:0]</td><td colspan="5">RSQ6[4:0]</td></tr><tr><td></td><td colspan="10">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP5[9:0]</td><td colspan="5">RSQ5[4:0]</td></tr><tr><td></td><td colspan="10">rw</td><td colspan="5">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP6[9:0]</td><td>常规通道采样时间<eq>10&#x27;d0</eq>:ADC0/1为3.5周期,ADC2为2.5周期<eq>10&#x27;d1</eq>:ADC0/1为4.5周期,ADC2为3.5周期<eq>10&#x27;d2</eq>:ADC0/1为5.5周期,ADC2为4.5周期<eq>10&#x27;d3</eq>:ADC0/1为6.5周期,ADC2为5.5周期<eq>10&#x27;d4</eq>:ADC0/1为7.5周期,ADC2为6.5周期......<eq>10&#x27;d638</eq>:ADC0/1为641.5周期,ADC2为640.5周期<eq>10&#x27;d639</eq>:只有ADC0/1为642.5周期......</td></tr></table>

10’d807：只有 ADC0/1 为 810.5 周期

其余位保留

20:16 RSQ6[4:0] 参考 RSQ0[4:0]描述

15 保留 必须保持复位值。

14:5 RSMP5[9:0] 常规通道采样时间

10’d0：ADC0/1 为 3.5 周期，ADC2 为 2.5 周期

10’d1：ADC0/1 为 4.5 周期，ADC2 为 3.5 周期

10’d2：ADC0/1 为 5.5 周期，ADC2 为 4.5 周期

10’d3：ADC0/1 为 6.5 周期，ADC2 为 5.5 周期

10’d4：ADC0/1 为 7.5 周期，ADC2 为 6.5 周期

10’d638：ADC0/1 为 641.5 周期，ADC2 为 640.5 周期

10’d639：只有 ADC0/1 为 642.5 周期

10’d807：只有 ADC0/1 为 810.5 周期

其余位保留

4:0 RSQ5[4:0] 参考 RSQ0[4:0]描述

# 20.7.12. 常规序列寄存器 6（ADC_RSQ6）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP4[9:0]</td><td colspan="5">RSQ4[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP3[9:0]</td><td colspan="5">RSQ3[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP4[9:0]</td><td>常规通道采样时间10'd0: ADC0/1 为 3.5 周期,ADC2 为 2.5 周期10'd1: ADC0/1 为 4.5 周期,ADC2 为 3.5 周期10'd2: ADC0/1 为 5.5 周期,ADC2 为 4.5 周期10'd3: ADC0/1 为 6.5 周期,ADC2 为 5.5 周期10'd4: ADC0/1 为 7.5 周期,ADC2 为 6.5 周期......10'd638: ADC0/1 为 641.5 周期,ADC2 为 640.5 周期10'd639: 只有 ADC0/1 为 642.5 周期......10'd807:只有ADC0/1为810.5周期其余位保留</td></tr><tr><td>20:16</td><td>RSQ4[4:0]</td><td>参考RSQ0[4:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP3[9:0]</td><td>常规通道采样时间10'd0:ADC0/1为3.5周期,ADC2为2.5周期10'd1:ADC0/1为4.5周期,ADC2为3.5周期10'd2:ADC0/1为5.5周期,ADC2为4.5周期10'd3:ADC0/1为6.5周期,ADC2为5.5周期10'd4:ADC0/1为7.5周期,ADC2为6.5周期......10'd638:ADC0/1为641.5周期,ADC2为640.5周期10'd639:只有ADC0/1为642.5周期......10'd807:只有ADC0/1为810.5周期其余位保留</td></tr><tr><td>4:0</td><td>RSQ3[4:0]</td><td>参考RSQ0[4:0]描述</td></tr></table>

# 20.7.13. 常规序列寄存器 7（ADC_RSQ7）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="10">RSMP2[9:0]</td><td colspan="5">RSQ2[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP1[9:0]</td><td colspan="5">RSQ1[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:21</td><td>RSMP2[9:0]</td><td>常规通道采样时间<eq>10&#x27;d0</eq>:ADC0/1为3.5周期,ADC2为2.5周期<eq>10&#x27;d1</eq>:ADC0/1为4.5周期,ADC2为3.5周期<eq>10&#x27;d2</eq>:ADC0/1为5.5周期,ADC2为4.5周期<eq>10&#x27;d3</eq>:ADC0/1为6.5周期,ADC2为5.5周期<eq>10&#x27;d4</eq>:ADC0/1为7.5周期,ADC2为6.5周期......<eq>10&#x27;d638</eq>:ADC0/1为641.5周期,ADC2为640.5周期</td></tr></table>

<table><tr><td></td><td></td><td>10&#x27;d639:只有ADC0/1为642.5周期......10&#x27;d807:只有ADC0/1为810.5周期其余位保留</td></tr><tr><td>20:16</td><td>RSQ2[4:0]</td><td>参考RSQ0[4:0]描述</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP1[9:0]</td><td>常规通道采样时间10&#x27;d0:ADC0/1为3.5周期,ADC2为2.5周期10&#x27;d1:ADC0/1为4.5周期,ADC2为3.5周期10&#x27;d2:ADC0/1为5.5周期,ADC2为4.5周期10&#x27;d3:ADC0/1为6.5周期,ADC2为5.5周期10&#x27;d4:ADC0/1为7.5周期,ADC2为6.5周期......10&#x27;d638:ADC0/1为641.5周期,ADC2为640.5周期10&#x27;d639:只有ADC0/1为642.5周期......10&#x27;d807:只有ADC0/1为810.5周期其余位保留</td></tr><tr><td>4:0</td><td>RSQ1[4:0]</td><td>参考RSQ0[4:0]描述</td></tr></table>

# 20.7.14. 常规序列寄存器 8（ADC_RSQ8）

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="10">RSMP0[9:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td></td><td colspan="10">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:5</td><td>RSMP0[9:0]</td><td>常规通道采样时间<eq>10&#x27;d0</eq>:ADC0/1为3.5周期,ADC2为2.5周期<eq>10&#x27;d1</eq>:ADC0/1为4.5周期,ADC2为3.5周期<eq>10&#x27;d2</eq>:ADC0/1为5.5周期,ADC2为4.5周期<eq>10&#x27;d3</eq>:ADC0/1为6.5周期,ADC2为5.5周期<eq>10&#x27;d4</eq>:ADC0/1为7.5周期,ADC2为6.5周期......<eq>10&#x27;d638</eq>:ADC0/1为641.5周期,ADC2为640.5周期</td></tr></table>

10’d639：只有 ADC0/1 为 642.5 周期

10’d807：只有 ADC0/1 为 810.5 周期

其余位保留

4:0 RSQ0[4:0] 

通道编号（0..20）写入这些位来选择常规通道的第 n 个转换的通道。

# 20.7.15. 常规数据寄存器（ADC_RDATA）

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RDATA[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>


r


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RDATA[31:0]</td><td>常规通道数据,对于ADC0/1,RDATA为[31:0],对于ADC2,RDATA为[15:0]。这些位包含了常规通道的转换结果,只读。</td></tr></table>

# 20.7.16. 过采样控制寄存器（ADC_OVSAMPCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">OVSR[9:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>TOVS</td><td colspan="4">OVSS[3:0]</td><td colspan="4">保留</td><td>OVSEN</td></tr><tr><td colspan="6">rw</td><td colspan="9">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:16</td><td>OVSR[9:0]</td><td>过采样率这些位定义了过采样率的大小,ADC0/1为1x~1024x,ADC2为1x~256x。10'd0: 1x(无过采样)10'd1: 2x10'd2: 3x......10'd1023: 1024x注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>过采样触发该位通过软件置位和清除。0: 在一次触发后连续执行过采样通道的所有转换1: 对于过采样通道的每次转换都需要一次触发,触发次数由过采样率(OVSR[9:0])决定。注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过采样移位该位通过软件置位和清除,对于ADC0/1,OVSS范围0000~1111,对于ADC2,OVSS范围0000~1000。0000: 不移位0001: 移1位0010: 移2位0011: 移3位0100: 移4位0101: 移5位0110: 移6位0111: 移7位1000: 移8位1001: 移9位1010: 移10位1011: 移11位其余位保留注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td>4:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>OVSEN</td><td>过采样使能该位通过软件置位和清除。0: 过采样失能1: 过采样使能注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr></table>

# 20.7.17. 看门狗 1 通道选择寄存器（ADC_WD1SR）

地址偏移：0xA0

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">AWD1CS[20:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD1CS[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:0</td><td>AWD1CS[20:0]</td><td>模拟看门狗1通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗1保护的输入通道。AWD1CS[n] = 0: ADC模拟输入通道n不由模拟看门狗1保护。AWD1CS[n] = 1: ADC模拟输入通道n由模拟看门狗1保护。当AWD1CH[20:0] = 000..0,模拟看门狗1禁能。</td></tr></table>

# 注意：

1）通过AWD1CS位域配置的模拟看门狗1功能的通道，必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道；

2）只有在ADC禁能（ADCON=0）时，才能软件写这些位。

# 20.7.18. 看门狗 2 通道选择寄存器（ADC_WD2SR）

地址偏移：0xA4

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">AWD2CS[20:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD2CS[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:0</td><td>AWD2CS[20:0]</td><td>模拟看门狗2通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗2保护的输入通道。AWD2CS[n] = 0: ADC模拟输入通道n不由模拟看门狗2保护。AWD2CS[n] = 1: ADC模拟输入通道n由模拟看门狗2保护。当AWD2CH[20:0] = 000..0,模拟看门狗2禁能。</td></tr></table>

# 注意：

1) 通过AWD2CS位域配置模拟看门狗2功能的通道，必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道；

2) 只有在ADC禁能（ADCON=0）时，才能软件写这些位。

# 20.7.19. 看门狗 1 高阈值寄存器（ADC_WDHT1）

地址偏移：0xA8

复位值：0x00FF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDHT1[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDHT1[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>WDHT1[23:0]</td><td>模拟看门狗1高侧阈值,ADC0/1为WDHT1[23:0],ADC2为WDHT1[7:0]。这些位定义了模拟看门狗1的高侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

# 20.7.20. 看门狗 1 低阈值寄存器（ADC_WDLT1）

地址偏移：0xA8

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDLT1[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDLT1[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>WDLT1[23:0]</td><td>模拟看门狗1低侧阈值,ADC0/1为WDLT1[23:0],ADC2为WDLT1[7:0]。这些位定义了模拟看门狗1的低侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

# 20.7.21. 看门狗 2 高阈值寄存器（ADC_WDHT2）

地址偏移：0xB0

复位值：0x00FF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDHT2[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDHT2[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>WDHT2[23:0]</td><td>模拟看门狗2高侧阈值,ADC0/1为WDHT2[23:0],ADC2为WDHT2[7:0]。这些位定义了模拟看门狗2的高侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

# 20.7.22. 看门狗 2 低阈值寄存器（ADC_WDLT2）

地址偏移：0xB4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDLT2[23:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDLT2[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>WDLT2[23:0]</td><td>模拟看门狗2低侧阈值,ADC0/1为WDLT2[23:0],ADC2为WDLT2[7:0]。这些位定义了模拟看门狗2的低侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

# 20.7.23. 差分模式控制寄存器（ADC_DIFCTL）

地址偏移：0xB8

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">DIFCTL[21:16]</td></tr></table>\
<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DIFCTL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:0</td><td>DIFCTL[21:0]</td><td>差分模式通道21..0。</td></tr></table>

这些位用于配置通道用于单端输入模式还是差分模式。

DIFCTL[n] = 0：ADC模拟输入通道n配置为单端模式。

DIFCTL[n] = 1：ADC模拟输入通道n配置为差分模式。

注意：只有在ADC禁能（ADCON=0）时，才能软件写这些位。

# 20.7.24. 摘要状态寄存器（ADC_SSTAT）

地址偏移：0x300

复位值：0x0000 0000

该寄存器是只读的，提供了3个ADC状态的摘要。这个寄存器在ADC1和ADC2中不可用。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>ADC2_ROVF</td><td>ADC2_STRC</td><td colspan="2">保留</td><td>ADC2_EOC</td><td>ADC2_WDE2</td><td>ADC2_WDE1</td><td>ADC2_WDE0</td></tr><tr><td colspan="8"></td><td>r</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC1_ROVF</td><td>ADC1_STRC</td><td colspan="2">保留</td><td>ADC1_EOC</td><td>ADC1_WDE2</td><td>ADC1_WDE1</td><td>ADC1_WDE0</td><td>ADC0_ROVF</td><td>ADC0_STRC</td><td colspan="2">保留</td><td>ADC0_EOC</td><td>ADC0_WDE2</td><td>ADC0_WDE1</td><td>ADC0_WDE0</td></tr><tr><td>r</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>ADC2_ROVF</td><td>该位是 ADC2 的 ROVF 的镜像</td></tr><tr><td>22</td><td>ADC2_STRC</td><td>该位是 ADC2 的 STRC 的镜像</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>ADC2_EOC</td><td>该位是 ADC2 的 EOC 的镜像</td></tr><tr><td>18</td><td>ADC2_WDE2</td><td>该位是 ADC2 的 WDE2 的镜像</td></tr><tr><td>17</td><td>ADC2_WDE1</td><td>该位是 ADC2 的 WDE1 的镜像</td></tr><tr><td>16</td><td>ADC2_WDE0</td><td>该位是 ADC2 的 WDE0 的镜像</td></tr><tr><td>15</td><td>ADC1_ROVF</td><td>该位是 ADC1 的 ROVF 的镜像</td></tr></table>

<table><tr><td>14</td><td>ADC1_STRC</td><td>该位是 ADC1 的 STRC 的镜像</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>ADC1_EOC</td><td>该位是 ADC1 的 EOC 的镜像</td></tr><tr><td>10</td><td>ADC1_WDE2</td><td>该位是 ADC1 的 WDE2 的镜像</td></tr><tr><td>9</td><td>ADC1_WDE1</td><td>该位是 ADC1 的 WDE1 的镜像</td></tr><tr><td>8</td><td>ADC1_WDE0</td><td>该位是 ADC1 的 WDE0 的镜像</td></tr><tr><td>7</td><td>ADC0_ROVF</td><td>该位是 ADC0 的 ROVF 的镜像</td></tr><tr><td>6</td><td>ADC0_STRC</td><td>该位是 ADC0 的 STRC 的镜像</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>ADC0_EOC</td><td>该位是 ADC0 的 EOC 的镜像</td></tr><tr><td>2</td><td>ADC0_WDE2</td><td>该位是 ADC0 的 WDE2 的镜像</td></tr><tr><td>1</td><td>ADC0_WDE1</td><td>该位是 ADC0 的 WDE1 的镜像</td></tr><tr><td>0</td><td>ADC0_WDE0</td><td>该位是 ADC0 的 WDE0 的镜像</td></tr></table>

# 20.7.25. 同步控制寄存器（ADC_SYNCCTL）

地址偏移：0x304

复位值：0x0000 0000

这个寄存器在ADC1中不可用。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">ADCCK[3:0]</td><td colspan="4">ADCSCK[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">SYNCDMA[1:0]</td><td colspan="2">SYNCDDM</td><td>保留</td><td colspan="3">SYNCDLY[3:0]</td><td colspan="4">保留</td><td colspan="4">SYNCM[3:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="8">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>ADCCK[3:0]</td><td>ADC时钟分频这些位配置所有ADC的时钟,可以通过软件设置频率。0000:ADC时钟1分频0001:ADC时钟2分频0010:ADC时钟4分频0011:ADC时钟6分频0100:ADC时钟8分频</td></tr></table>

<table><tr><td></td><td></td><td>0101: ADC时钟10分频0110: ADC时钟12分频0111: ADC时钟16分频1000: ADC时钟32分频1001: ADC时钟64分频1010: ADC时钟128分频1011: ADC时钟256分频其它值保留。</td></tr><tr><td>19:16</td><td>ADCSCK[3:0]</td><td>ADC同步时钟配置这些位配置所有ADC的时钟,可以通过软件设置ADC同步时钟模式。0000: CLK_ADC(异步时钟模式)1000: HCLK 2分频(同步时钟模式)1001: HCLK 4分频(同步时钟模式)1010: HCLK 6分频(同步时钟模式)1011: HCLK 8分频(同步时钟模式)1100: HCLK 10分频(同步时钟模式)1101: HCLK 12分频(同步时钟模式)1110: HCLK 14分频(同步时钟模式)1111: HCLK 16分频(同步时钟模式)其它值保留。</td></tr><tr><td>15:14</td><td>SYNCDMA[1:0]</td><td>ADC同步DMA模式选择00: ADC同步DMA失能:01: ADC同步DMA模式010: ADC同步DMA模式111: 保留</td></tr><tr><td>13</td><td>SYNCDDM</td><td>ADC同步DMA使能模式该位配置ADC同步模式时DMA失能模式0: 当检测到来自DMA控制器的传输结束信号后,DMA机制失能1: 当SYNCDMA不为00时,根据SYNCDMA位来产生DMA请求。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>SYNCDLY[3:0]</td><td>ADC同步延迟在ADC同步模式中,这些位用于配置两个采样阶段之间的延迟为(5+SYNCDLY)ADC时钟周期。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>SYNCM[3:0]</td><td>ADC同步模式当ADC同步模式已经使能,如果要将同步模式修改为其他值,必须先将这些位设置为000000000: ADC同步模式失能。所有的ADC都独立工作。0110: ADC0和ADC1工作在常规并行模式。0111: ADC0和ADC1工作在常规跟随模式。</td></tr></table>

其它值保留。

# 20.7.26. 同步常规数据寄存器 0（ADC_SYNCDATA0）

地址偏移：0x308

复位值：0x0000 0000

这个寄存器在ADC1和ADC2中不可用。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SYNCDATA1[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SYNCDATA0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>SYNCDATA1[15:0]</td><td>ADC 同步模式中,常规数据 1,且 SYNCDMA[1:0]=2&#x27;b 10。</td></tr><tr><td>15:0</td><td>SYNCDATA0[15:0]</td><td>ADC 同步模式中,常规数据 0,且 SYNCDMA[1:0]=2&#x27;b 10。</td></tr></table>

# 20.7.27. 同步常规数据寄存器 1（ADC_SYNCDATA1）

地址偏移：0x30C

复位值：0x0000 0000

这个寄存器在ADC1和ADC2中不可用。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SYNCDATA[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SYNCDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SYNCDATA[31:0]</td><td>当 SYNCDMA[1:0]=2&#x27;b01 时,依次从 ADC 的常规数据(主/从)中选择。</td></tr></table>
