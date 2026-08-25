## 14.7. ADC 寄存器

ADC0 基地址： 0x4001 2000

ADC1 基地址:：0x4001 2100

ADC2 基地址:：0x4001 2200

## 14.7.1. 状态寄存器 (ADC_STAT)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ROVF</td><td>STRC</td><td colspan="2">保留</td><td>EOC</td><td>WDE</td></tr><tr><td colspan="10"></td><td>rc_w0</td><td>rc_w0</td><td colspan="2"></td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ROVF</td><td>常规数据寄存器溢出0:常规数据寄存器没有溢出1:常规数据寄存器溢出在单次或多次模式中,当常规数据寄存器溢出时,该位由硬件置位。只有在DMA使能或者转换结束模式被置1(EOCM=1)时,这个标志位才会置位。如果出现ROVF置位,则最后的常规数据会被丢失。软件写‘0”清除。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0:转换没有开始1:转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC</td><td>常规序列转换结束标志0:常规序列转换没有结束1:常规序列转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr><tr><td>0</td><td>WDE</td><td>模拟看门狗事件标志0:没有模拟看门狗事件1:产生模拟看门狗事件</td></tr></table>

转换电压超过 ADC_WDLT 和ADC_WDHT 寄存器设定的阈值时由硬件置 1，软件写 0 清除。

## 14.7.2. 控制寄存器 0 (ADC_CTL0)

地址偏移：0x04

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>ROVFIE</td><td colspan="2">DRES[1:0]</td><td>RWDEN</td><td colspan="7">保留</td></tr><tr><td colspan="5"></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="7"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM[2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WDSC</td><td>SM</td><td>保留</td><td>WDEIE</td><td>EOCIE</td><td colspan="5">WDCHSEL[4:0]</td></tr><tr><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>ROVFIE</td><td>ROVF中断使能0: ROVF中断失能1: ROVF中断使能</td></tr><tr><td>25:24</td><td>DRES[1:0]</td><td>ADC数据分辨率00: 12位01: 10位10: 8位11: 6位</td></tr><tr><td>23</td><td>RWDEN</td><td>常规序列看门狗使能0: 常规序列看门狗禁止1: 常规序列看门狗使能</td></tr><tr><td>22:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0: 间断运行模式禁止1: 间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WDSC</td><td>扫描模式下,模拟看门狗在单通道有效0: 模拟看门狗在所有通道有效1: 模拟看门狗在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0: 扫描运行模式禁止1: 扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WDEIE</td><td>WDE 中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>5</td><td>EOCIE</td><td>EOC 中断使能0: 中断禁止1: 中断使能</td></tr><tr><td>4:0</td><td>WDCHSEL[4:0]</td><td>模拟看门狗通道选择00000: ADC 通道 00001: ADC 通道 100010: ADC 通道 200011: ADC 通道 300100: ADC 通道 400101: ADC 通道 500110: ADC 通道 600111: ADC 通道 701000: ADC 通道 801001: ADC 通道 901010: ADC 通道 1001011: ADC 通道 1101100: ADC 通道 1201101: ADC 通道 1301110: ADC 通道 1401111: ADC 通道 1510000: ADC 通道 1610001: ADC 通道 1710010: ADC 通道 18其他值保留。</td></tr></table>


注意： ADC0 的模拟输入通道 16，通道 17 和通道 18 分别连接到温度传感器，V 和 V 模拟输入。 ADC1 的模拟输入通道 16，通道 17 和通道18 内部都连接到 VSSA。 ADC2 的模拟输入通道 16，通道 17 和通道18 内部都连接到 VSSA。


## 14.7.3. 控制寄存器 1 (ADC_CTL1)

地址偏移：0x08

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>SWRCST</td><td colspan="2">ETMRC[1:0]</td><td colspan="4">ETSRC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td>EOCM</td><td>DDM</td><td>DMA</td><td colspan="4">保留</td><td>RSTCLB</td><td>CLB</td><td>CTN</td><td>ADCON</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>SWRCST</td><td>常规序列软件启动转换该位置1开启常规序列转换。软件置位,软件清零,或转换开始后,立刻由硬件清零。</td></tr><tr><td>29:28</td><td>ETMRC[1:0]</td><td>常规序列外部触发模式00:常规序列外部触发失能01:常规序列外部触发上升沿使能01:常规序列外部触发下降沿使能11:常规序列外部触发双边沿使能</td></tr><tr><td>27:24</td><td>ETSRC[3:0]</td><td>常规序列的外部触发选择0000:定时器0通道00001:定时器0通道10010:定时器0通道20011:定时器1通道10100:定时器1通道20101:定时器1通道30110:定时器1TRGO0111:定时器2通道01000:定时器2TRGO1001:定时器3通道31010:定时器4通道01011:定时器4通道11100:定时器4通道21101:定时器7通道01110:定时器7TRGO1111:EXTI外部中断线11</td></tr><tr><td>23:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0:最低有效位对齐1:最高有效位对齐</td></tr><tr><td>10</td><td>EOCM</td><td>转换结束模式0:只有在常规转换序列转换结束时,才将EOC置1。如果不设置DMA=1,则溢出检测失能。1:在每个常规转换结束时,将EOC置1。溢出检测自动使能。</td></tr><tr><td>9</td><td>DDM</td><td>DMA失能模式该位用于在单次ADC模式下配置DMA失能。0:DMA机制在DMA控制器的传输结束信号之后失能。1:当DMA=1,在每个常规转换结束时DMA机制产生一个DMA请求。</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0:DMA请求禁止1:DMA请求使能</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>RSTCLB</td><td>校准复位在校准寄存器初始化后该位可以软件置位和硬件清零。0:校准寄存器初始化结束.1:校准寄存器初始化开始</td></tr><tr><td>2</td><td>CLB</td><td>ADC校准0:校准结束1:校准开始</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0:禁止连续运行模式1:使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启ADC。该位从0变成1将唤醒ADC。为了省电,当该位为0时,模拟子模块将会进入掉电模式。0:失能ADC,并进入掉电模式1:使能ADC</td></tr></table>

## 14.7.4. 采样时间寄存器 0 (ADC_SAMPT0)

地址偏移：0x0C

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td colspan="3">SPT18[2:0]</td><td colspan="3">SPT17[2:0]</td><td colspan="3">SPT16[2:0]</td><td colspan="2">SPT15[2:1]</td></tr><tr><td colspan="5"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">说明</td></tr></table>

<table><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>SPT18[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT17[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT16[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间000:通道采样时间为 3个周期001:通道采样时间为 15个周期010:通道采样时间为 28个周期011:通道采样时间为 56个周期100:通道采样时间为 84个周期101:通道采样时间为 112个周期110:通道采样时间为 144个周期111:通道采样时间为 480个周期</td></tr></table>

## 14.7.5. 采样时间寄存器 1 (ADC_SAMPT1)

地址偏移：0x10

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT5[0]</td><td colspan="3">SPT4[2:0]</td><td colspan="3">SPT3[2:0]</td><td colspan="3">SPT2[2:0]</td><td colspan="3">SPT1[2:0]</td><td colspan="3">SPT0[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr></table>

<table><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为 3个周期001:通道采样时间为 15个周期010:通道采样时间为 28个周期011:通道采样时间为 56个周期100:通道采样时间为 84个周期101:通道采样时间为 112个周期110:通道采样时间为 144个周期111:通道采样时间为 480个周期</td></tr></table>

## 14.7.6. 看门狗高阈值寄存器 (ADC_WDHT)

地址偏移：0x24

复位值：0x0000 0FFF

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDHT[11:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WDHT[11:0]</td><td>模拟看门狗高侧阈值这些位定义了模拟看门狗的高侧阈值。</td></tr></table>

## 14.7.7. 看门狗低阈值寄存器 (ADC_WDLT)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDLT[11:0]</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">说明</td></tr><tr><td>31:12</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>11:0</td><td colspan="3">WDLT[11:0]</td><td colspan="12">模拟看门狗低侧阈值这些位定义了模拟看门狗的低侧阈值。</td></tr></table>

## 14.7.8. 常规序列寄存器 0 (ADC_RSQ0)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td colspan="4">RSQ15[4:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td colspan="5">RSQ14[4:0]</td><td colspan="5">RSQ13[4:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规序列长度常规序列中的总的通道数目为 RL[3:0]+1。</td></tr><tr><td>19:15</td><td>RSQ15[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ14[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ13[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ12[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr></table>

## 14.7.9. 常规序列寄存器 1 (ADC_RSQ1)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td colspan="2">16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ11[4:0]rw</td><td colspan="5">RSQ10[4:0]rw</td><td colspan="5">RSQ9[4:1]rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td></td></tr><tr><td>RSQ9[0]</td><td colspan="5">RSQ8[4:0]</td><td colspan="5">RSQ7[4:0]</td><td colspan="5">RSQ6[4:0]</td><td></td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ11[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ10[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ9[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ8[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ7[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ6[4:0]</td><td>参考 RSQ0[4:0]的描述</td></tr></table>

## 14.7.10. 常规序列寄存器 2 (ADC_RSQ2)

地址偏移：0x34

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ5[4:0]</td><td colspan="5">RSQ4[4:0]</td><td colspan="4">RSQ3[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td colspan="5">RSQ2[4:0]</td><td colspan="5">RSQ1[4:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ5[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ4[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ3[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ2[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ1[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ0[4:0]</td><td>通道编号(0..18)写入这些位来选择常规通道的第n个转换的通道</td></tr></table>

## 14.7.11. 常规数据寄存器 (ADC_RDATA)

地址偏移：0x4C

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道数据这些位包含了常规通道的转换结果,只读。</td></tr></table>

## 14.7.12. 过采样控制寄存器 (ADC_OVSAMPCTL)

地址偏移：0x80

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>TOVS</td><td colspan="4">OVSS[3:0]</td><td colspan="3">OVSR[2:0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="6"></td><td>rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>过采样触发该位通过软件置位和清除。0:在一次触发后连续执行过采样通道的所有转换1:对于过采样通道的每次转换都需要一次触发,触发次数由过采样率(OVSR[2:0])决定。注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过采样移位该位通过软件置位和清除。0000:不移位0001:移1位</td></tr><tr><td rowspan="9"></td><td rowspan="9"></td><td>0010:移2位</td></tr><tr><td>0011:移3位</td></tr><tr><td>0100:移4位</td></tr><tr><td>0101:移5位</td></tr><tr><td>0110:移6位</td></tr><tr><td>0111:移7位</td></tr><tr><td>1000:移8位</td></tr><tr><td>其余值都保留</td></tr><tr><td>注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td rowspan="10">4:2</td><td rowspan="10">OVSR[2:0]</td><td>过采样率这些位定义了过采样率的大小。</td></tr><tr><td>000:2x</td></tr><tr><td>001:4x</td></tr><tr><td>010:8x</td></tr><tr><td>011:16x</td></tr><tr><td>100:32x</td></tr><tr><td>101:64x</td></tr><tr><td>110:128x</td></tr><tr><td>111:256x</td></tr><tr><td>注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td rowspan="4">0</td><td rowspan="4">OVSEN</td><td>过采样使能该位通过软件置位和清除。</td></tr><tr><td>0:过采样失能</td></tr><tr><td>1:过采样使能</td></tr><tr><td>注意:只有在ADCON=0的时候才允许通过软件对该位进行写(确保没有转换正在执行)。</td></tr></table>

## 14.7.13. 摘要状态寄存器 (ADC_SSTAT)

地址偏移：0x300

复位值：0x0000 0000

该寄存器只能按字（32位）访问

该寄存器是只读的，提供了3个ADC状态的摘要。这个寄存器在ADC1和ADC2中不可用。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td>ROVF2</td><td>STRC2</td><td>保留</td><td></td><td>EOC2</td><td>WDE2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td></td><td></td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>ROVF1</td><td>STRC1</td><td>保留</td><td>EOC1</td><td>WDE1</td><td>保留</td><td>ROVF0</td><td>STRC0</td><td>保留</td><td>EOC0</td><td>WDE0</td></tr><tr><td></td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td></td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>ROVF2</td><td>该位是 ADC2 的 ROVF 的镜像</td></tr><tr><td>20</td><td>STRC2</td><td>该位是 ADC2 的 STRC 的镜像</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>EOC2</td><td>该位是 ADC2 的 EOC 的镜像</td></tr><tr><td>16</td><td>WDE2</td><td>该位是 ADC2 的 WDE 的镜像</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>ROVF1</td><td>该位是 ADC1 的 ROVF 的镜像</td></tr><tr><td>12</td><td>STRC1</td><td>该位是 ADC1 的 STRC 的镜像</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EOC1</td><td>该位是 ADC1 的 EOC 的镜像</td></tr><tr><td>8</td><td>WDE1</td><td>该位是 ADC1 的 WDE 的镜像</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ROVF0</td><td>该位是 ADC0 的 ROVF 的镜像</td></tr><tr><td>4</td><td>STRC0</td><td>该位是 ADC0 的 STRC 的镜像</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC0</td><td>该位是 ADC0 的 EOC 的镜像</td></tr><tr><td>0</td><td>WDE0</td><td>该位是 ADC0 的 WDE 的镜像</td></tr></table>

## 14.7.14. 同步控制寄存器 (ADC_SYNCCTL)

地址偏移：0x304

复位值：0x0000 0000

该寄存器只能按字（32位）访问

这个寄存器在ADC1和ADC2中不可用

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>TSVREN</td><td>VBATEN</td><td colspan="3">保留</td><td colspan="3">ADCCK[2:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td colspan="3"></td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">SYNCDMA[1:0]</td><td>SYNCDDM</td><td>保留</td><td colspan="4">SYNCDLY[3:0]</td><td colspan="3">保留</td><td colspan="5">SYNCM[4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TSVREN</td><td>使能ADC0的通道16(温度传感器)和通道17(内部参考电压)。0: ADC0的通道16和通道17失能1: ADC0的通道16和通道17使能</td></tr><tr><td>22</td><td>VBATEN</td><td>使能ADC0的通道18(外部电池电压的1/4)0: ADC0的通道18失能1: ADC0的通道18使能</td></tr><tr><td>21:19</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>18:16</td><td>ADCCK[2:0]</td><td>ADC时钟这些位配置所有ADC的时钟000: PCLK2 2分频001: PCLK2 4分频010: PCLK2 6分频011: PCLK2 8分频100: HCLK 5分频101: HCLK 6分频110: HCLK 10分频111: HCLK 20分频</td></tr><tr><td>15:14</td><td>SYNCDMA[1:0]</td><td>ADC同步DMA模式选择00: ADC同步DMA失能:01: ADC同步DMA模式010: ADC同步DMA模式111: 保留</td></tr><tr><td>13</td><td>SYNCDDM</td><td>ADC同步DMA使能模式该位配置ADC同步模式时DMA失能模式0: 当检测到来自DMA控制器的传输结束信号后,DMA机制失能1: 当SYNCDMA不为00时,根据SYNCDMA位来产生DMA请求。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>SYNCDLY[3:0]</td><td>ADC同步延迟在ADC同步模式中,这些位用于配置两个采样阶段之间的延迟为(5+SYNCDLY)ADC时钟周期。</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>SYNCM[4:0]</td><td>ADC同步模式当ADC同步模式已经使能,如果要将同步模式修改为其他值,必须先将这些位设置为0000000000: ADC同步模式失能。所有的ADC都独立工作。</td></tr></table>

00110：ADC0 和 ADC1 工作在常规并行模式。ADC2 独立工作。

00111：ADC0 和 ADC1 工作在常规跟随模式。ADC2 独立工作。

10110：所有的 ADC 都工作在常规并行模式。

10111：所有的 ADC 都工作在常规跟随模式。

其他值保留。

## 14.7.15. 同步常规数据寄存器 (ADC_SYNCDATA)

地址偏移：0x308

复位值：0x0000 0000

该寄存器只能按字（32位）访问

这个寄存器在ADC1和ADC2中不可用。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SYNCDATA1[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SYNCDATA0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>Fields</td><td>说明</td></tr><tr><td>31:16</td><td>SYNCDATA1[15:0]</td><td>ADC 同步模式中,常规数据 2</td></tr><tr><td>15:0</td><td>SYNCDATA0[15:0]</td><td>ADC 同步模式中,常规数据 1</td></tr></table>
