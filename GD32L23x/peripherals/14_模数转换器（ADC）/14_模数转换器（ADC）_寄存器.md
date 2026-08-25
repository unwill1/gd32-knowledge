## 14.5. ADC 寄存器

ADC基地址：0x4001 2400

## 14.5.1. 状态寄存器（ADC_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td>STRC</td><td>保留</td><td></td><td>EOC</td><td>WDE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w0</td><td></td><td></td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0:转换没有开始1:转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC</td><td>常规序列转换结束标志0:转换没有结束1:转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr><tr><td>0</td><td>WDE</td><td>模拟看门狗事件标志0:没有模拟看门狗事件1:产生模拟看门狗事件转换电压超过ADC_WDLT和ADC_WDHT寄存器中设定的阈值时由硬件置1,软件写0清除。</td></tr></table>

## 14.5.2. 控制寄存器 0（ADC_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="2">DRES [1:0]rw</td><td>RWDENrw</td><td colspan="7">保留rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM [2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WDSC</td><td>SM</td><td>保留</td><td>WDEIE</td><td>EOCIE</td><td colspan="5">WDCHSEL [4:0]</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>DRES [1:0]</td><td>ADC分辨率00: 12位01: 10位10: 8位11: 6位</td></tr><tr><td>23</td><td>RWDEN</td><td>常规序列模拟看门狗使能0: 常规序列模拟看门狗禁能1: 常规序列模拟看门狗使能</td></tr><tr><td>22:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0: 间断运行模式禁能1: 间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WDSC</td><td>扫描模式下,模拟看门狗在单通道有效0: 模拟看门狗在所有通道有效1: 模拟看门狗在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0: 扫描运行模式禁能1: 扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WDEIE</td><td>WDE中断使能0: 中断禁能1: 中断使能</td></tr><tr><td>5</td><td>EOCIE</td><td>EOC中断使能0: 中断禁能1: 中断使能</td></tr><tr><td>4:0</td><td>WDCHSEL[4:0]</td><td>模拟看门狗通道选择00000: ADC通道0</td></tr></table>

00001：ADC通道1

00010：ADC通道2

10000：ADC通道16

10001：ADC通道17

10010：ADC通道18

10011：ADC通道19

注意：ADC的模拟输入通道16、通道17、通道18和通道19内部分别连接到温度传感器、V<sub>REFINT</sub>、V<sub>BAT</sub>和V<sub>SLCD</sub>。

## 14.5.3. 控制寄存器 1（ADC_CTL1）

GD32L233xx 产品

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>VSLCDEN</td><td>VBATEN</td><td>INREFEN</td><td>TSVEN</td><td>SWRCST</td><td>保留</td><td>ETERC</td><td colspan="3">ETSRC [2:0]</td><td>保留</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td colspan="2">保留</td><td>DMA</td><td colspan="4">保留</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td colspan="4"></td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>VSLCDEN</td><td>ADC的通道19(1/3的<eq>V_{SLCD}</eq>电压)使能0:ADC的通道19禁能1:ADC的通道19使能</td></tr><tr><td>25</td><td>VBATEN</td><td>ADC的通道18(1/3外部电池电压)使能0:ADC的通道18禁能1:ADC的通道18使能</td></tr><tr><td>24</td><td>INREFEN</td><td>ADC的通道17(内部参考电压)使能0:ADC的通道17禁能1:ADC的通道17使能</td></tr><tr><td>23</td><td>TSVEN</td><td>ADC的通道16(温度传感器)使能0:ADC的通道16禁能1:ADC的通道16使能</td></tr><tr><td>22</td><td>SWRCST</td><td>软件触发常规序列转换开始如果ETSRC是111,该位置‘1’开启常规序列转换。该位由软件置位,软件清零或转换开始由硬件清零。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ETERC</td><td>常规序列外部触发使能0:常规序列外部触发禁能1:常规序列外部触发使能</td></tr><tr><td>19:17</td><td>ETSRC [2:0]</td><td>常规序列通道外部触发选择000:TIMER8 CH0001:TIMER8 CH1010:保留011:TIMER1 CH1100:TIMER2 TRGO101:TIMER11 CH0110:中断线1111:软件触发SWRCST</td></tr><tr><td>16:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0:最低有效位对齐1:最高有效位对齐</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0:DMA请求禁能1:DMA请求使能</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位软件置位,在校准寄存器初始化后,该位硬件清零。0:校准寄存器初始化结束.1:校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC校准0:校准结束1:校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0:禁能连续运行模式1:使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启ADC。该位从‘0’变成‘1’将在稳定时间结束后唤醒ADC。当该位被置位以后,不改变寄存器的其他位仅仅对该位写‘1’,将开启转换。0:禁能ADC并掉电1:使能ADC</td></tr></table>

## GD32L235xx 产品

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>VSLCDEN</td><td>VBATEN</td><td>INREFEN</td><td>TSVEN</td><td>SWRCST</td><td>保留</td><td>ETERC</td><td colspan="3">ETSRC [2:0]</td><td>保留</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td colspan="2">保留</td><td>DMA</td><td>保留</td><td colspan="3">CALNUM[2:0]</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td colspan="4"></td><td>rw</td><td colspan="2"></td><td>rw</td><td></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>VSLCDEN</td><td>ADC的通道19(1/3的<eq>V_{SLCD}</eq>电压)使能0: ADC的通道19禁能1: ADC的通道19使能</td></tr><tr><td>25</td><td>VBATEN</td><td>ADC的通道18(1/3外部电池电压)使能0: ADC的通道18禁能1: ADC的通道18使能</td></tr><tr><td>24</td><td>INREFEN</td><td>ADC的通道17(内部参考电压)使能0: ADC的通道17禁能1: ADC的通道17使能</td></tr><tr><td>23</td><td>TSVEN</td><td>ADC的通道16(温度传感器)使能0: ADC的通道16禁能1: ADC的通道16使能</td></tr><tr><td>22</td><td>SWRCST</td><td>软件触发常规序列转换开始如果ETSRC是111,该位置‘1’开启常规序列转换。该位由软件置位,软件清零或转换开始由硬件清零。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ETERC</td><td>常规序列外部触发使能0: 常规序列外部触发禁能1: 常规序列外部触发使能</td></tr><tr><td>19:17</td><td>ETSRC [2:0]</td><td>常规序列通道外部触发选择000: TIMER8 CH0001: TIMER8 CH1010: TIMER0_CH2011: TIMER1 CH1100: TIMER2 TRGO101: TIMER11 CH0110: 中断线1111: 软件触发SWRCST</td></tr><tr><td>16:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0: 最低有效位对齐1: 最高有效位对齐</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0: DMA请求禁能1: DMA请求使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CALNUM[2:0]</td><td>校准次数这些位用于配置ADC的校准次数。000: 1次001: 2次010: 4次011: 8次100: 16次101: 32次其他值保留。</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位软件置位,在校准寄存器初始化后,该位硬件清零。0: 校准寄存器初始化结束.1: 校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC校准0: 校准结束1: 校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0: 禁能连续运行模式1: 使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启ADC。该位从‘0’变成‘1’将在稳定时间结束后唤醒ADC。当该位被置位以后,不改变寄存器的其他位仅仅对该位写‘1’,将开启转换。0: 禁能ADC并掉电1: 使能ADC</td></tr></table>

## 14.5.4. 采样时间寄存器 0（ADC_SAMPT0）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT19[2:0]</td><td colspan="3">SPT18[2:0]</td><td colspan="3">SPT17[2:0]</td><td colspan="3">SPT16[2:0]</td><td colspan="2">SPT15[2:0]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT19[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>26:24</td><td>SPT18[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>23:21</td><td>SPT17[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>20:18</td><td>SPT16[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考SPT10[2:0]的描述。</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间000:通道采样时间为2.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 14.5.5. 采样时间寄存器 1（ADC_SAMPT1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>SPT5[0]</td><td>SPT4[2:0]</td><td>SPT3[2:0]</td><td>SPT2[2:0]</td><td>SPT1[2:0]</td><td>SPT0[2:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT1[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为2.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 14.5.6. 看门狗高阈值寄存器（ADC_WDHT）

地址偏移：0x24

复位值：0x0000 0FFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDHT [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>11:0</td><td>WDHT [11:0]</td><td>模拟看门狗高侧阈值这些位定义了模拟看门狗的高侧阈值。</td></tr></table>

## 14.5.7. 看门狗低阈值寄存器（ADC_WDLT）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDLT [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WDLT [11:0]</td><td>模拟看门狗低侧阈值这些位定义了模拟看门狗的低侧阈值。</td></tr></table>

## 14.5.8. 常规序列寄存器 0（ADC_RSQ0）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL [3:0]</td><td colspan="4">RSQ15[4:1]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td colspan="5">RSQ14[4:0]</td><td colspan="5">RSQ13[4:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规序列长度常规序列的总通道数目为<eq>RL[3:0]+1</eq>。</td></tr><tr><td>19:15</td><td>RSQ15[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ14[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ13[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

4:0 RSQ12[4:0] 参考RSQ0[4:0]的描述

## 14.5.9. 常规序列寄存器 1（ADC_RSQ1）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ11[4:0]</td><td colspan="5">RSQ10[4:0]</td><td colspan="4">RSQ9[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ9[0]</td><td colspan="5">RSQ8[4:0]</td><td colspan="5">RSQ7[4:0]</td><td colspan="5">RSQ6[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">Rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ11[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ10[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ9[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ8[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ7[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ6[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

## 14.5.10. 常规序列寄存器 2（ADC_RSQ2）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ5[4:0]</td><td colspan="5">RSQ4[4:0]</td><td colspan="4">RSQ3[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td colspan="5">RSQ2[4:0]</td><td colspan="5">RSQ1[4:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">Rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ5[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

这些位包含了常规通道的转换结果，只读。

<table><tr><td>24:20</td><td>RSQ4[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ3[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ2[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ1[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ0[4:0]</td><td>通道编号(0..19)写入这些位来选择常规序列的第n个转换的通道</td></tr></table>

## 14.5.11. 常规数据寄存器（ADC_RDATA）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道转换数据</td></tr></table>

## 14.5.12. 过采样控制寄存器（ADC_OVSAMPCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>TOVS</td><td colspan="4">OVSS [3:0]</td><td colspan="3">OVSR [2:0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="6"></td><td>rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>过采样触发该位通过软件设置和清除。0:在一个触发后,连续执行过采样通道的所有转换</td></tr></table>

1：对于过采样通道的每次转换都需要一次触发，触发次数由过采样率（OVSR[2:0]）决定

注意：当ADCON= 0时软件才允许写该位（确定没有转换正在进行）。

注意：只有在ADCON=0的时候，才允许通过软件对该位进行写操作（确保没有转换正在进行）。

注意：只有在ADCON=0的时候，才允许通过软件对该位进行写操作（确保没有转换正在执行）。

注意：只有在ADCON=0的时候，才允许通过软件对该位进行写操作（确保没有转换正在执行）。

## 14.5.13. 充电控制寄存器（ADC_CCTL）

地址偏移：0x C0

复位值：0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>CHARGE</td></tr><tr><td colspan="16">ro</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">CCNT [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CHARGE</td><td>ADC充电状态0:无充电1:正在充电中该位由硬件置位和清零。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>CCNT [11:0]</td><td>ADC充电脉冲宽度计数器该位用于控制ADC充电脉冲的宽度,CCNT值与脉冲宽度的关系如下:脉冲宽度 = 5us = CCNT [11:0] * tPCLK2。注意:只有在ADCON =0(确定没有转换正在进行)时,才能软件写该位。</td></tr></table>

## 14.5.14. 差分模式控制寄存器（ADC_DIFCTL）

仅适用于 GD32L235xx 产品

地址偏移：0xC4

复位值：0x00000000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">DIFCTL[19:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DIFCTL[15]</td><td colspan="15">DIFCTL[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:15</td><td>DIFCTL[19:15]</td><td>差分模式通道19..15。这些位只读,通道19..15被强制为单端输入模式(连接到单端I/O端口或内部通道)。</td></tr><tr><td>14:0</td><td>DIFCTL[14:0]</td><td>差分模式通道14..0。这些位用于配置通道用于单端输入模式还是差分模式。DIFCTL[n] = 0: ADC模拟输入通道n配置为单端模式。</td></tr></table>

DIFCTL[n] = 1：ADC模拟输入通道n配置为差分模式。

注意：只有在ADC禁能（ADCON=0）时，才能软件写这些位。
