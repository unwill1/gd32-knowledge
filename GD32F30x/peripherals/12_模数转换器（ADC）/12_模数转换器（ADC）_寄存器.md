## 12.7. ADC 寄存器

ADC0 基地址：0x4001 2400

ADC1 基地址：0x4001 2800

ADC2 基地址：0x4001 3C00

## 12.7.1. 状态寄存器 (ADC_STAT)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>STRC</td><td colspan="2">保留</td><td>EOC</td><td>WDE</td></tr><tr><td colspan="11"></td><td colspan="3">rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0: 转换没有开始1: 转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC</td><td>常规序列转换结束标志0: 转换没有结束1: 转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr><tr><td>0</td><td>WDE</td><td>模拟看门狗事件标志0: 没有模拟看门狗事件1: 产生模拟看门狗事件转换电压超过ADC_WDLT和ADC_WDHT寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr></table>

## 12.7.2. 控制寄存器 0 (ADC_CTL0)

地址偏移：0x04

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>RWDEN</td><td colspan="3">保留</td><td colspan="4">SYNCM[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM[2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WDSC</td><td>SM</td><td>保留</td><td>WDEIE</td><td>EOCIE</td><td colspan="5">WDCHSEL[4:0]</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>RWDEN</td><td>常规序列看门狗使能0:常规序列看门狗禁止1:常规序列看门狗使能</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:16</td><td>SYNCM[3:0]</td><td>同步模式选择这些位用于运行模式选择0000:独立模式0001~0101:保留0110:常规并行模式0111:常规快速交叉模式1000:常规慢速交叉模式1001~1111:保留注意:1)这些位只用于ADC0;2)建议用户在任何配置之前关闭同步模式。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0:间断运行模式禁止1:间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WDSC</td><td>扫描模式下,模拟看门狗在通道配置0:模拟看门狗在所有通道有效1:模拟看门狗在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0:扫描运行模式禁止1:扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WDEIE</td><td>WDE中断使能</td></tr></table>

0：中断禁止

1：中断使能

5 EOCIE EOC 中断使能

0：中断禁止

1：中断使能

4:0 WDCHSEL[4:0] 模拟看门狗通道选择

00000: ADC 通道 0

00001: ADC 通道 1

00010: ADC 通道 2

00011: ADC 通道 3

00100: ADC 通道 4

00101: ADC 通道 5

00110: ADC 通道 6

00111: ADC 通道 7

01000: ADC 通道 8

01001: ADC 通道 9

01010: ADC 通道 10

01011: ADC 通道 11

01100: ADC 通道 12

01101: ADC 通道 13

01110: ADC 通道 14

01111: ADC 通道 15

10000: ADC 通道 16

10001: ADC 通道 17

其他值保留。

注意： ADC0 的模拟输入通道 16 和通道17 分别连接到温度传感器和 VREFINT。

ADC1 的模拟输入通道 16 和通道 17 内部都连接到 VSSA。 ADC2 的模拟输入通道

16 和通道 17 内部都连接到 VSSA。

## 12.7.3. 控制寄存器 1 (ADC_CTL1)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>TSVREN</td><td>SWRCST</td><td>保留</td><td>ETERC</td><td colspan="3">ETSRC[2: 0]</td><td>保留.</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td colspan="2">保留.</td><td>DMA</td><td colspan="4">保留</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

位/位域 名称 说明

<table><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TSVREN</td><td>ADC0的通道16和17使能0: ADC0的通道16和17禁止1: ADC0的通道16和17使能</td></tr><tr><td>22</td><td>SWRCST</td><td>软件触发常规序列转换开始如果ETSRC是111,该位置‘1’开启常规序列转换。软件置位,软件清零,或转换开始后,由硬件清零。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ETERC</td><td>常规序列外部触发使能0:常规序列外部触发禁止1:常规序列外部触发使能</td></tr><tr><td>19:17</td><td>ETSRC[2:0]</td><td>常规序列外部触发选择对于ADC0与ADC1:000:定时器0CH0001:定时器0CH1010:定时器0CH2011:定时器1CH1100:定时器2TRGO101:定时器3CH3110:中断线11/定时器7TRGO111:软件触发对于ADC2:000:定时器2CH0001:定时器1CH2010:定时器0CH2011:定时器7CH0100:定时器7TRGO101:定时器4CH0110:定时器4CH2111:软件触发</td></tr><tr><td>16:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0:最低有效位对齐1:最高有效位对齐</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0:DMA请求禁止1:DMA请求使能</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位软件置位,在校准寄存器初始化后该位硬件清零。0:校准寄存器初始化结束.1:校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC 校准0:校准结束1:校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0:禁止连续运行模式1:使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启 ADC。该位从‘0’变成‘1’将在稳定时间结束后唤醒 ADC。当该位被置位以后,不改变寄存器的其他位仅仅对该位写‘1’,将开启转换。0:禁止 ADC 关闭电源1:使能 ADC</td></tr></table>

## 12.7.4. 采样时间寄存器 0 (ADC_SAMPT0)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="3">SPT17[2:0]</td><td colspan="3">SPT16[2:0]</td><td colspan="2">SPT15[2:1]</td></tr><tr><td colspan="11">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:21</td><td>SPT17[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT16[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间</td></tr></table>

000：通道采样时间为1.5周期

001：通道采样时间为7.5周期

010：通道采样时间为13.5周期

011：通道采样时间为28.5周期

100：通道采样时间为41.5周期

101：通道采样时间为55.5周期

110：通道采样时间为71.5周期

111：通道采样时间为 239.5周期

## 12.7.5. 采样时间寄存器 1 (ADC_SAMPT1)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT5[0]</td><td colspan="3">SPT4[2:0]</td><td colspan="3">SPT3[2:0]</td><td colspan="3">SPT2[2:0]</td><td colspan="3">SPT1[2:0]</td><td colspan="3">SPT0[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为1.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期</td></tr></table>

101：通道采样时间为55.5周期

110：通道采样时间为71.5周期

111：通道采样时间为 239.5周期

## 12.7.6. 看门狗高阈值寄存器 (ADC_WDHT)

地址偏移：0x24

复位值：0x0000 0FFF

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDHT[11:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WDHT[11:0]</td><td>模拟看门狗高侧阈值这些位定义了模拟看门狗的高侧阈值。</td></tr></table>

## 12.7.7. 看门狗低阈值寄存器 (ADC_WDLT)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDLT[11:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WDLT[11:0]</td><td>模拟看门狗低侧阈值这些位定义了模拟看门狗的低侧阈值。</td></tr></table>

## 12.7.8. 常规序列寄存器 0 (ADC_RSQ0)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td colspan="4">RSQ15[4:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td colspan="5">RSQ14[4:0]</td><td colspan="5">RSQ13[4:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规序列长度常规通道转换序列中的总的通道数目为 RL[3:0]+1。</td></tr><tr><td>19:15</td><td>RSQ15[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ14[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ13[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ12[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr></table>

## 12.7.9. 常规序列寄存器 1 (ADC_RSQ1)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ11[4:0]</td><td colspan="5">RSQ10[4:0]</td><td colspan="4">RSQ9[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ9[0]</td><td colspan="5">RSQ8[4:0]</td><td colspan="5">RSQ7[4:0]</td><td colspan="5">RSQ6[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ11[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ10[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr></table>

<table><tr><td>19:15</td><td>RSQ9[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ8[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ7[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ6[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr></table>

## 12.7.10. 常规序列寄存器 2 (ADC_RSQ2)

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ5[4:0]</td><td colspan="5">RSQ4[4:0]</td><td colspan="4">RSQ3[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td colspan="5">RSQ2[4:0]</td><td colspan="5">RSQ1[4:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ5[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ4[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ3[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ2[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ1[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ0[4:0]</td><td>通道编号(0..17)写入这些位来选择常规通道的第 n 个转换的通道</td></tr></table>

## 12.7.11. 常规数据寄存器 (ADC_RDATA)

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADC1RDTR[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>ADC1RDTR[15:0]</td><td>ADC1 常规通道数据在同步模式下,这些位包含着 ADC1 的常规通道数据这些位只在 ADC0 中使用。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道数据这些位包含了常规通道的转换结果,只读。</td></tr></table>

## 12.7.12. 过采样控制寄存器 (ADC_OVSAMPCTL)

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">DRES[1:0]</td><td colspan="2">保留</td><td>TOVS</td><td colspan="4">OVSS[3:0]</td><td colspan="3">OVSR[2:0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="2"></td><td colspan="4">Rw</td><td>rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>DRES[1:0]</td><td>ADC分辨率00:12位01:10位10:8位11:6位</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>触发过滤采样该位通过软件设置和清除.0:所有的过滤采样连续转换完成一个触发后1:对于过采样通道的每次转换都需要一次触发,触发次数由过采样率(OVSR[2:0])决定。注意:当ADCON=0时软件才允许写该位(确定没有转换正在进行).</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过滤采样移位该位通过软件设置和清除.0000:不移位0001:移1位0010:移2位</td></tr></table>

0011：移 3 位

0100：移 4 位

0101：移 5 位

0110：移 6 位

0111：移 7 位

1000：移 8 位

其他保留

注意:当 ADCON=0 时软件才允许写该位(确定没有转换正在进行).

4:2 OVSR[2:0] 过采样率

这些位定义了过采样率的大小.

000：2x 

001：4x 

010：8x 

011：16x 

100：32x 

101：64x 

110：128x 

111：256x 

注意:当 ADCON=0 时软件才允许写该位(确定没有转换正在进行)

1 保留 必须保持复位值。

0 OVSEN 过滤采样使能

该位通过软件和设置和清除

0：过滤采样失能

1：过滤采样使能

注意:当 ADCON=0 时软件才允许写该位(确定没有转换正在进行)
