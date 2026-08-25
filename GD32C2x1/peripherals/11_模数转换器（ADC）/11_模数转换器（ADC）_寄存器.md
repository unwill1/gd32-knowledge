## 11.6. ADC 寄存器

ADC 基地址：0x4001 2400

## 11.6.1. 状态寄存器（ADC_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WD2E</td><td>WD1E</td><td colspan="14">保留</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>STRC</td><td colspan="2">保留</td><td>EOC</td><td>WD0E</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31</td><td>WD2E</td><td>模拟看门狗2事件标志0:没有模拟看门狗2事件1:模拟看门狗2事件发生转换电压超过ADC_WD2HT和ADC_WD2LT寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>30</td><td>WD1E</td><td>模拟看门狗1事件标志0:没有模拟看门狗1事件1:模拟看门狗1事件发生转换电压超过ADC_WD1HT和ADC_WD1LT寄存器设定的阈值时由硬件置1,软件写0清除。</td></tr><tr><td>29:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0:常规序列转换没有开始1:常规序列转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>EOC</td><td>序列转换结束标志0:序列转换没有结束1:序列转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr><tr><td>0</td><td>WD0E</td><td>模拟看门狗事件0标志0:没有模拟看门狗0事件1:模拟看门狗0事件发生</td></tr></table>

转换电压超过 ADC_WD0LT和 ADC_WD0HT 寄存器设定的阈值时由硬件置 1，软件写 0 清除。

## 11.6.2. 控制寄存器 0（ADC_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>WD2EIE</td><td>WD1EIE</td><td colspan="4">保留</td><td colspan="2">DRES [1:0]</td><td>RWD0EN</td><td colspan="7">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="4"></td><td colspan="2">rw</td><td>rw</td><td colspan="7"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM [2:0]</td><td>保留</td><td>DISRC</td><td>保留</td><td>WD0SC</td><td>SM</td><td>保留</td><td>WD0EIE</td><td>EOCIE</td><td>保留</td><td colspan="4">WD0CHSEL[3:0]</td></tr><tr><td colspan="3">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31</td><td>WD2EIE</td><td>WD2E中断使能0: WD2E中断禁能1: WD2E中断使能</td></tr><tr><td>30</td><td>WD1EIE</td><td>WD1E中断使能0: WD1E中断禁能1: WD1E中断使能</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>DRES[1:0]</td><td>ADC分辨率00: 12位01: 10位10: 8位11: 6位</td></tr><tr><td>23</td><td>RWD0EN</td><td>常规序列模拟看门狗0使能0: 常规序列模拟看门狗0禁能1: 常规序列模拟看门狗0使能</td></tr><tr><td>22:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0: 常规序列间断运行模式禁能1: 常规序列间断运行模式使能</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WD0SC</td><td>扫描模式下,模拟看门狗0在单个通道配置0:模拟看门狗0在所有通道有效1:模拟看门狗0在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0:扫描运行模式禁能1:扫描运行模式使能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WD0EIE</td><td>WD0E中断使能0:WD0E中断禁能1:WD0E中断使能</td></tr><tr><td>5</td><td>EOCIE</td><td>EOC中断使能0:EOC中断禁能1:EOC中断使能</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>WD0CHSEL[3:0]</td><td>模拟看门狗0通道选择0000:ADC通道00001:ADC通道10010:ADC通道20011:ADC通道30100:ADC通道40101:ADC通道50110:ADC通道60111:ADC通道71000:ADC通道81001:ADC通道91010:ADC通道101011:ADC通道111100:ADC通道121101:ADC通道131110:ADC通道141111:ADC通道15注意:1. ADC模拟输入通道13、14和15分别连接到温度传感器、<eq>V_{REFINT}</eq>和<eq>V_{REFP}</eq>模拟输入。</td></tr></table>

## 11.6.3. 控制寄存器 1（ADC_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>INREFEN</td><td>TSVEN</td><td>SWRCST</td><td>保留</td><td>ETERC</td><td colspan="3">ETSRC [2:0]</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>DAL</td><td colspan="2">保留</td><td>DMA</td><td></td><td colspan="5">保留</td><td>CTN</td><td>ADCON</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>INREFEN</td><td>内部参考电压通道(<eq>V_{REFINT}</eq>)使能0: 内部参考电压通道禁能1: 内部参考电压通道使能连接到ADC模拟输入通道14</td></tr><tr><td>23</td><td>TSVEN</td><td>温度传感器输出电压通道使能0: 温度传感器输出电压通道禁能1: 温度传感器输出电压通道使能连接到ADC模拟输入通道13</td></tr><tr><td>22</td><td>SWRCST</td><td>常规序列软件启动转换如果ETSRC是111,该位置‘1’开启常规序列转换。软件置位,软件清零,或转换开始后,由硬件清零。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ETERC</td><td>常规序列外部触发使能0: 常规序列外部触发禁能1: 常规序列外部触发使能</td></tr><tr><td>19:17</td><td>ETSRC[2:0]</td><td>常规序列外部触发选择000: 定时器2CH1001: 定时器0CH2010: 定时器0CH1011: 定时器2TRGO100: 定时器0CH0101: 定时器2CH0110: 中断线1111: 软件触发</td></tr><tr><td>16:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0: 最低有效位对齐1: 最高有效位对齐</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>DMA</td><td>DMA请求使能0: DMA 请求禁能1: DMA 请求使能</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0: 禁能连续运行模式1: 使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启 ADC该位从‘0’变成‘1’将在稳定时间结束后唤醒 ADC。当该位被置位以后,不改变寄存器的其他位仅仅对该位写‘1’,将开启转换。0: 禁能 ADC 关闭电源1: 使能 ADC</td></tr></table>

## 11.6.4. 采样时间寄存器 0（ADC_SAMPT0）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">SPT15[2:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间000:通道采样时间为2.5周期001:通道采样时间为3.5周期010:通道采样时间为7.5周期011:通道采样时间为12.5周期100:通道采样时间为19.5周期101:通道采样时间为39.5周期110:通道采样时间为79.5周期</td></tr></table>

111：通道采样时间为 160.5周期

## 11.6.5. 采样时间寄存器 1（ADC_SAMPT1）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT5[0]</td><td colspan="3">SPT4[2:0]</td><td colspan="3">SPT3[2:0]</td><td colspan="3">SPT2[2:0]</td><td colspan="3">SPT1[2:0]</td><td colspan="3">SPT0[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT1[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为2.5周期001:通道采样时间为3.5周期010:通道采样时间为7.5周期011:通道采样时间为12.5周期100:通道采样时间为19.5周期101:通道采样时间为39.5周期110:通道采样时间为79.5周期111:通道采样时间为160.5周期</td></tr></table>

## 11.6.6. 看门狗 0高阈值寄存器（ADC_WD0HT）

地址偏移：0x24

复位值：0x0000 0FFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WD0HT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WD0HT[11:0]</td><td>模拟看门狗 0 高侧阈值这些位定义了模拟看门狗 0 的高阈值。</td></tr></table>

## 11.6.7. 看门狗 0低阈值寄存器（ADC_WD0LT）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WDOLT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WDOLT[11:0]</td><td>模拟看门狗 0 低侧阈值这些位定义了模拟看门狗 0 的低阈值。</td></tr></table>

## 11.6.8. 常规序列寄存器 0（ADC_RSQ0）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td>保留</td><td colspan="3">RSQ15[3:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td>保留</td><td colspan="4">RSQ14[3:0]</td><td>保留</td><td colspan="4">RSQ13[3:0]</td><td>保留</td><td colspan="4">RSQ12[3:0]</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RL[3:0]</td><td>常规序列长度常规转换序列中的总的通道数目为 RL[3:0]+1。</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:15</td><td>RSQ15[3:0]</td><td>参考 RSQ0[3:0]的描述</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>RSQ14[3:0]</td><td>参考 RSQ0[3:0]的描述</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:5</td><td>RSQ13[3:0]</td><td>参考 RSQ0[3:0]的描述</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>RSQ12[3:0]</td><td>参考 RSQ0[3:0]的描述</td></tr></table>

## 11.6.9. 常规序列寄存器 1（ADC_RSQ1）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="4">RSQ11[3:0]</td><td>保留</td><td colspan="4">RSQ10[3:0]</td><td>保留</td><td colspan="3">RSQ9[3:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ9[0]</td><td>保留</td><td colspan="4">RSQ8[3:0]</td><td>保留</td><td colspan="4">RSQ7[3:0]</td><td>保留</td><td colspan="4">RSQ6[3:0]</td></tr><tr><td colspan="2">rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:25</td><td>RSQ11[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RSQ10[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:15</td><td>RSQ9[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>RSQ8[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:5</td><td>RSQ7[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>RSQ6[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr></table>

## 11.6.10. 常规序列寄存器 2（ADC_RSQ2）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="4">RSQ5[3:0]</td><td>保留</td><td colspan="4">RSQ4[3:0]</td><td>保留</td><td colspan="3">RSQ3[3:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td>保留</td><td colspan="4">RSQ2[3:0]</td><td>保留</td><td colspan="4">RSQ1[3:0]</td><td>保留</td><td colspan="4">RSQ0[3:0]</td></tr><tr><td colspan="2">rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ5[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>RSQ4[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:15</td><td>RSQ3[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>RSQ2[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:5</td><td>RSQ1[3:0]</td><td>参考RSQ0[3:0]的描述</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>RSQ0[3:0]</td><td>通道编号写入这些位来选择常规序列的第n个转换的通道(通道编号为0..15)</td></tr></table>

## 11.6.11. 常规数据寄存器（ADC_RDATA）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道数据这些位包含了常规通道的转换结果,只读。</td></tr></table>

## 11.6.12. 看门狗 1 通道选择寄存器（ADC_WD1SR）

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD1CS[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>AWD1CS[15:0]</td><td>模拟看门狗1通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗1保护的输入通道。AWD1CS[n] = 0: ADC模拟输入通道n不由模拟看门狗1保护。AWD1CS[n] = 1: ADC模拟输入通道n由模拟看门狗1保护。当AWD1CS[15:0] = 000..0,模拟看门狗1禁能。注意:1)通过AWD1CS位域配置的模拟看门狗1功能的通道,必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道;2)ADC模拟输入通道13、14和15分别连接到温度传感器、VREFINT和VREFP模拟输入。</td></tr></table>

## 11.6.13. 看门狗 2 通道选择寄存器（ADC_WD2SR）

地址偏移：0x54

复位值：0x00000000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AWD2CS[15:0]</td></tr></table>

<table><tr><td>Bits</td><td>Fields</td><td>Descriptions</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>AWD2CS[15:0]</td><td>模拟看门狗2通道选择这些位由软件置位和复位,它们使能并选择要由模拟看门狗2保护的输入通道。AWD2CS[n] = 0: ADC模拟输入通道n不由模拟看门狗2保护。AWD2CS[n] = 1: ADC模拟输入通道n由模拟看门狗2保护。当AWD2CS[15:0] = 000..0,模拟看门狗2禁能。注意:1)通过AWD2CS位域配置的模拟看门狗2功能的通道,必须是ADC_RSQn寄存器和ADC_ISQ寄存器中配置的通道;2)ADC模拟输入通道13、14和15分别连接到温度传感器、<eq>V_{REFINT}</eq>和<eq>V_{REFP}</eq>模拟输入。</td></tr></table>

## 11.6.14. 看门狗 1 高阈值寄存器（ADC_WD1HT）

地址偏移：0x58

复位值：0x0000 0FFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WD1HT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WD1HT[11:0]</td><td>模拟看门狗1高侧阈值这些位定义了模拟看门狗1的高阈值。</td></tr></table>

## 11.6.15. 看门狗 1 低阈值寄存器（ADC_WD1LT）

地址偏移：0x5C

复位值：0x0000 0000

<table><tr><td colspan="16">该寄存器只能按字(32位)访问。</td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WD1LT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WD1LT[11:0]</td><td>模拟看门狗1低侧阈值</td></tr></table>

## 11.6.16. 看门狗 2 高阈值寄存器（ADC_WD2HT）

地址偏移：0x60

复位值：0x0000 0FFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WD2HT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WD2HT[11:0]</td><td>模拟看门狗2高侧阈值这些位定义了模拟看门狗2的高阈值。</td></tr></table>

## 11.6.17. 看门狗 2 低阈值寄存器（ADC_WD2LT）

地址偏移：0x64

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WD2LT[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WD2LT[11:0]</td><td>模拟看门狗2低侧阈值这些位定义了模拟看门狗2的低阈值。</td></tr></table>

## 11.6.18. 过采样控制寄存器（ADC_OVSAMPCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>TOVS</td><td colspan="4">OVSS[3:0]</td><td colspan="3">OVSR[2:0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="6"></td><td>rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>过采样触发该位通过软件置位和清除。0: 在一次触发后连续执行过采样通道的所有转换1: 对于过采样通道的每次转换都需要一次触发,触发次数由过采样率(OVSR[2:0])决定。注意:只有在ADCON=0的时候才允许通过软件对该位进行写操作(确保没有转换正在执行)。</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过采样移位该位通过软件置位和清除。0000: 不移位0001: 移1位0010: 移2位0011: 移3位0100: 移4位0101: 移5位0110: 移6位0111: 移7位1000: 移8位其余值都保留注意:只有在ADCON=0的时候才允许通过软件对该位进行写操作(确保没有转换正在执行)。</td></tr><tr><td>4:2</td><td>OVSR[2:0]</td><td>过采样率这些位定义了过采样率的大小.000: 2x001: 4x010: 8x011: 16x100: 32x</td></tr></table>

101：64x 

110：128x 

111：256x 

注意：只有在 ADCON=0 的时候才允许通过软件对该位进行写操作（确保没有转换正在执行）。

1 保留 必须保持复位值。

0 OVSEN 过采样使能

该位通过软件置位和清除。

0：过采样禁能

1：过采样使能

注意：只有在 ADCON=0 的时候才允许通过软件对该位进行写（确保没有转换正在执行）。
