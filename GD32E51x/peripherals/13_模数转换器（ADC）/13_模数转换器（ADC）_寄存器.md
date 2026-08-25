## 13.7. ADC 寄存器

ADC0 基地址：0x4001 2400

ADC1 基地址：0x4001 2800

ADC2 基地址：0x4001 3C00

## 13.7.1. 状态寄存器（ADC_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WDE2</td><td>WDE1</td><td colspan="14">保留</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>STRC</td><td colspan="2">保留</td><td>EOC</td><td>WDE0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WDE2</td><td>模拟看门狗2事件标志0: 模拟看门狗2事件没有发生1: 模拟看门狗2事件发生转换电压超过ADC_WDLT2寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>30</td><td>WDE1</td><td>模拟看门狗1事件标志0: 模拟看门狗1事件没有发生1: 模拟看门狗1事件发生转换电压超过ADC_WDLT1寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>29:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0: 转换没有开始1: 转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC</td><td>常规序列转换结束标志0: 转换没有结束1: 转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr><tr><td>0</td><td>WDE0</td><td>模拟看门狗0事件标志0: 模拟看门狗0事件没有发生</td></tr></table>

1：模拟看门狗0事件发生

转换电压超过ADC_WDLT0和ADC_WDHT0寄存器设定的阈值时由硬件置1，软件写0清除。

## 13.7.2. 控制寄存器 0（ADC_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WDE2IE</td><td>WDE1IE</td><td colspan="6">保留</td><td>RWD0EN</td><td colspan="3">保留</td><td colspan="4">SYNCM[3:0]</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM[2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WD0SC</td><td>SM</td><td>保留</td><td>WDE0IE</td><td>EOCIE</td><td></td><td colspan="4">WD0CHSEL[4:0]</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>WDE2IE</td><td>WDE2中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>30</td><td>WDE1IE</td><td>WDE1中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>29:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23</td><td>RWD0EN</td><td>常规序列模拟看门狗0使能0: 模拟看门狗0禁止1: 模拟看门狗0使能</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>SYNCM[3:0]</td><td>同步模式选择这些位用于运行模式选择。0000: 独立模式0110: 常规并行模式0111: 常规快速交叉模式1000: 常规慢速交叉模式注意: 1)这些位只用于ADC0; 2)建议用户在任何配置之前关闭同步模式。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式</td></tr></table>

<table><tr><td></td><td></td><td>0:常规序列间断运行模式禁止1:常规序列间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WD0SC</td><td>扫描运行模式下,模拟看门狗0在通道的配置0:模拟看门狗0在所有通道有效1:模拟看门狗0在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0:扫描运行模式禁止1:扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WDE0IE</td><td>WDE0中断使能0:中断禁止1:中断使能</td></tr><tr><td>5</td><td>EOCIE</td><td>EOC中断使能0:EOC中断禁止1:EOC中断使能</td></tr><tr><td>4:0</td><td>WD0CHSEL[4:0]</td><td>模拟看门狗0通道选择00000:ADC通道000001:ADC通道100010:ADC通道200011:ADC通道300100:ADC通道400101:ADC通道500110:ADC通道600111:ADC通道701000:ADC通道801001:ADC通道901010:ADC通道1001011:ADC通道1101100:ADC通道1201101:ADC通道1301110:ADC通道1401111:ADC通道1510000:ADC通道1610001:ADC通道17其他值保留。</td></tr></table>

注意：ADC0的模拟输入通道16和通道17分别连接到温度传感器和V 。ADC1的模拟输入通道16和通道17内部都连接到V 。ADC2的模拟输入通道16和通道17内部都连接到V<sub>SSA</sub>。

## 13.7.3. 控制寄存器 1（ADC_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>ETSRC[3]</td><td colspan="7">保留</td><td>TSVREN</td><td>SWRCST</td><td>保留</td><td>ETERC</td><td colspan="3">ETSRC[2: 0]</td><td>保留.</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td colspan="2">保留.</td><td>DMA</td><td>保留</td><td colspan="3">CALNUM[2:0]</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>ETSRC[3]</td><td>常规序列外部触发选择,具体请参考ETSRC[2:0]的描述。</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TSVREN</td><td>ADC0的通道16和17使能0: ADC0的通道16和17禁止1: ADC0的通道16和17使能</td></tr><tr><td>22</td><td>SWRCST</td><td>常规序列转换开始如果ETSRC是111,该位置“1”开启常规序列转换。软件置位,软件清零,或转换开始后,由硬件清零。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ETERC</td><td>常规序列外部触发使能0: 外部触发禁止1: 外部触发使能</td></tr><tr><td>19:17</td><td>ETSRC[2:0]</td><td>常规序列外部触发选择ETSRC[2:0]与ETSRC[3]共同确定常规序列外部触发源。对于ADC0与ADC1:0000: TIMER0_CH0001: TIMER_CH10010: TIMER0_CH20011: TIMER1_CH10100: TIMER2_TRGO0101: TIMER3_CH30110: 中断线11/ TIMER7_TRGO0111: 软件触发1000: SHRTIMER_ADCTRIG01001: SHRTIMER_ADCTRIG2其他值保留。对于ADC2:0000: TIMER2_CH00001: TIMER1_CH20010: TIMER0_CH20011: TIMER7_CH00100: TIMER7_TRGO0101: TIMER4_CH00110: TIMER4_CH20111: SWRCST1xxx: 保留</td></tr><tr><td>16:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0: 最低有效位(LSB)对齐1: 最高有效位(MSB)对齐</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0: DMA请求禁止1: DMA请求使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CALNUM[2:0]</td><td>校准次数这些位用于配置ADC的校准次数。000: 1次001: 2次010: 4次011: 8次100: 16次101: 32次其他值保留。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位软件置位,在校准寄存器初始化后该位硬件清零。0: 校准寄存器初始化结束.1: 校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC校准0: 校准结束1: 校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0: 禁止连续运行模式1: 使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启ADC。该位从“0”变成“1”将在稳定时间结束后唤醒ADC。该位置1后,不改变寄存器的其他位仅对该位写1,将开启转换。</td></tr></table>

0：禁能ADC并掉电

1：使能ADC

## 13.7.4. 采样时间寄存器 0（ADC_SAMPT0）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="3">SPT17[2:0]</td><td colspan="3">SPT16[2:0]</td><td colspan="2">SPT15[2:1]</td></tr><tr><td colspan="11">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:21</td><td>SPT17[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT16[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考SPT10[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间000:通道采样时间为1.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 13.7.5. 采样时间寄存器 1（ADC_SAMPT1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT5[0]</td><td colspan="3">SPT4[2:0]</td><td colspan="3">SPT3[2:0]</td><td colspan="3">SPT2[2:0]</td><td colspan="3">SPT1[2:0]</td><td colspan="3">SPT0[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT1[2:0]</td><td>参考SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为1.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 13.7.6. 看门狗 0高阈值寄存器（ADC_WDHT0）

地址偏移：0x24

复位值：0x0000 0FFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDHT0[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>WDHT0[11:0]</td><td>模拟看门狗0高侧阈值这些位定义了模拟看门狗0的高侧阈值。</td></tr></table>

## 13.7.7. 看门狗 0 低阈值寄存器（ADC_WDLT0）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDLT0[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>WDLT0[11:0]</td><td>模拟看门狗0低侧阈值这些位定义了模拟看门狗0的低侧阈值。</td></tr></table>

## 13.7.8. 常规序列寄存器 0（ADC_RSQ0）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td colspan="4">RSQ15[4:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td colspan="5">RSQ14[4:0]</td><td colspan="5">RSQ13[4:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规序列长度</td></tr><tr><td></td><td></td><td>常规通道转换序列中的总的通道数目为RL[3:0]+1。</td></tr><tr><td>19:15</td><td>RSQ15[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ14[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ13[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ12[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

## 13.7.9. 常规序列寄存器 1（ADC_RSQ1）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ11[4:0]</td><td colspan="5">RSQ10[4:0]</td><td colspan="4">RSQ9[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ9[0]</td><td colspan="5">RSQ8[4:0]</td><td colspan="5">RSQ7[4:0]</td><td colspan="5">RSQ6[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ11[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ10[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ9[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ8[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ7[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ6[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

## 13.7.10. 常规序列寄存器 2（ADC_RSQ2）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ5[4:0]</td><td colspan="5">RSQ4[4:0]</td><td colspan="4">RSQ3[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td colspan="5">RSQ2[4:0]</td><td colspan="5">RSQ1[4:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29:25</td><td>RSQ5[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ4[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ3[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ2[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ1[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ0[4:0]</td><td>通道编号(0..17)写入这些位来选择常规通道的第n个转换的通道。</td></tr></table>

## 13.7.11. 常规数据寄存器（ADC_RDATA）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADC1RDTR[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>ADC1RDTR[15:0]</td><td>ADC1常规通道数据ADC0:在同步模式下,这些位包含着ADC1的常规通道数据。这些位只在ADC0中使用。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道数据这些位包含了常规通道的转换结果,只读。</td></tr></table>

## 13.7.12. 过采样控制寄存器（ADC_OVSAMPCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">DRES[1:0]</td><td colspan="2">保留</td><td>TOVS</td><td colspan="4">OVSS[3:0]</td><td colspan="3">OVSR[2:0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>DRES[1:0]</td><td>ADC分辨率00: 12位01: 10位10: 8位11: 6位</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>TOVS</td><td>触发过滤采样该位通过软件设置和清除。0: 在一个触发之后,对一个通道连续进行过采样转换1: 在一个触发之后,对一个通道只进行一次过采样转换注意:当ADCON=0时,才允许软件写该位(确定没有转换正在进行)。</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过滤采样移位该位通过软件设置和清除。0000: 不移位0001: 移1位0010: 移2位0011: 移3位0100: 移4位0101: 移5位0110: 移6位0111: 移7位1000: 移8位其他保留注意:当ADCON=0时,才允许软件写该位(确定没有转换正在进行)。</td></tr><tr><td>4:2</td><td>OVR[2:0]</td><td>过采样率这些位定义了过采样率的大小。000: 2x001: 4x010: 8x011: 16x100: 32x101: 64x110: 128x111: 256x注意:当ADCON=0时,才允许软件写该位(确定没有转换正在进行)。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>0</td><td>OVSEN</td><td>过滤采样使能该位通过软件和设置和清除。</td></tr></table>

0：过滤采样失能

1：过滤采样使能

注意：当ADCON= 0时，才允许软件写该位（确定没有转换正在进行）。

## 13.7.13. 看门狗 1 通道选择寄存器（ADC_WD1SR）

地址偏移：0xA0

复位值：0x00000000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">AWD1CS[17:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD1CS[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:0</td><td>AWD1CS[17:0]</td><td>模拟看门狗1通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗1保护的输入通道。AWD1CS[n] = 0: ADC模拟输入通道n不由模拟看门狗1保护。AWD1CS[n] = 1: ADC模拟输入通道n由模拟看门狗1保护。当AWD1CH[17:0] = 000..0,模拟看门狗1禁能。注意:1)通过AWD1CS位域配置的模拟看门狗1功能的通道,必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道;2)只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

## 13.7.14. 看门狗 2 通道选择寄存器（ADC_WD2SR）

地址偏移：0xA4

复位值：0x00000000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">AWD2CS[17:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD2CS[15:0]</td></tr></table>

<table><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:0</td><td>AWD2CS[17:0]</td><td>模拟看门狗2通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗2保护的输入通道。AWD2CS[n] = 0: ADC模拟输入通道n不由模拟看门狗2保护。AWD2CS[n] = 1: ADC模拟输入通道n由模拟看门狗2保护。当AWD2CH[17:0] = 000..0,模拟看门狗2禁能。注意:1) 通过AWD2CS位域配置模拟看门狗2功能的通道,必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道;2) 只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

## 13.7.15. 看门狗 1 阈值寄存器（ADC_WDT1）

地址偏移：0xA8

复位值：0x00FF 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDHT1[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDLT1[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>WDHT1[7:0]</td><td>模拟看门狗1高侧阈值这些位定义了模拟看门狗1的高侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>WDLT1[7:0]</td><td>模拟看门狗1低侧阈值这些位定义了模拟看门狗1的低侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

## 13.7.16. 看门狗 2 阈值寄存器（ADC_WDT2）

地址偏移：0xAC

复位值：0x00FF 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDHT2[7:0]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">WDLT2[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>WDHT2[7:0]</td><td>模拟看门狗2高阈值这些位定义了模拟看门狗2的高阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>WDLT2[7:0]</td><td>模拟看门狗2低侧阈值这些位定义了模拟看门狗2的低侧阈值。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>

## 13.7.17. 差分模式控制寄存器（ADC_DIFCTL）

地址偏移：0xB0

复位值：0x00000000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">DIFCTL[17:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DIFCTL[15]</td><td colspan="15">DIFCTL[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:15</td><td>DIFCTL[17:15]</td><td>差分模式通道17..15。这些位只读,通道17..15被强制为单端输入模式(连接到单端I/O端口或内部通道)。</td></tr><tr><td>14:0</td><td>DIFCTL[14:0]</td><td>差分模式通道14..0。这些位用于配置通道用于单端输入模式还是差分模式。DIFCTL[n] = 0: ADC模拟输入通道n配置为单端模式。DIFCTL[n] = 1: ADC模拟输入通道n配置为差分模式。注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr></table>
