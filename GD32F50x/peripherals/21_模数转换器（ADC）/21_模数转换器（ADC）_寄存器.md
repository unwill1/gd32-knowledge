## 21.7. ADC 寄存器

ADC0 基地址：0x4001 2400

ADC1 基地址：0x4001 2800

ADC2 基地址：0x4001 3C00

## 21.7.1. 状态寄存器（ADC_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>STRC</td><td>STIC</td><td>EOIC</td><td>EORC</td><td>WD0E</td></tr><tr><td colspan="11"></td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>STRC</td><td>常规序列转换开始标志0:常规序列转换没有开始1:常规序列转换开始常规序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>3</td><td>STIC</td><td>注入序列转换开始标志0:注入序列转换没有开始1:注入序列转换开始注入序列转换开始时硬件置位,软件写0清除。</td></tr><tr><td>2</td><td>EOIC</td><td>注入序列转换结束标志0:注入序列转换没有结束1:注入序列转换结束注入序列所有的通道转换结束时硬件置位,软件写0清除。</td></tr><tr><td>1</td><td>EORC</td><td>常规序列转换结束标志0:常规序列转换没有结束1:常规序列转换结束常规序列转换结束时硬件置位,软件写0或读ADC_RDATA寄存器清除。</td></tr></table>

1：产生模拟看门狗0事件

转换电压超过ADC_WD0LT和ADC_WD0HT寄存器设定的阈值时由硬件置1。

软件写 0 清除。

## 21.7.2. 控制寄存器 0（ADC_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>RWD0EN</td><td>IWD0EN</td><td colspan="2">保留</td><td colspan="4">SYNCM[3:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td colspan="2"></td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DISNUM[2:0]</td><td>DISIC</td><td>DISRC</td><td>ICA</td><td>WD0SC</td><td>SM</td><td>EOICIE</td><td>WD0EIE</td><td>EORCIE</td><td colspan="5">WD0CHSEL[4:0]</td></tr><tr><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>RWD0EN</td><td>常规序列模拟看门狗0使能0:常规序列模拟看门狗0禁能1:常规序列模拟看门狗0使能</td></tr><tr><td>22</td><td>IWD0EN</td><td>注入序列模拟看门狗0使能0:注入序列模拟看门狗0禁能1:注入序列模拟看门狗0使能</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:16</td><td>SYNCM[3:0]</td><td>同步模式选择这些位用于运行模式选择0000:独立模式0001:常规并行和注入并行组合模式0010:常规并行和注入交替触发组合模式0011:注入并行和常规快速交叉组合模式0100:注入并行和常规慢速交叉组合模式0101:注入并行模式0110:常规并行模式0111:常规快速交叉模式1000:常规慢速交叉模式1001:注入交替触发模式注意:1)这些位只用于ADC0;2)建议用户在任何配置之前关闭同步模式。</td></tr><tr><td>15:13</td><td>DISNUM[2:0]</td><td>间断模式下的转换数目触发后即将被转换的通道数目将变成DISNUM[2:0]+1</td></tr><tr><td>12</td><td>DISIC</td><td>注入序列间断模式0:注入序列间断运行模式禁能1:注入序列间断运行模式使能</td></tr><tr><td>11</td><td>DISRC</td><td>常规序列间断模式0:常规序列间断运行模式禁能1:常规序列间断运行模式使能</td></tr><tr><td>10</td><td>ICA</td><td>注入序列自动转换0:注入序列自动转换禁能1:注入序列自动转换使能</td></tr><tr><td>9</td><td>WD0SC</td><td>扫描模式下,模拟看门狗0在通道配置0:模拟看门狗0在所有通道有效1:模拟看门狗0在单通道有效</td></tr><tr><td>8</td><td>SM</td><td>扫描模式0:扫描运行模式禁能1:扫描运行模式使能</td></tr><tr><td>7</td><td>EOICIE</td><td>EOIC中断使能0:EOIC中断禁能1:EOIC中断使能</td></tr><tr><td>6</td><td>WD0EIE</td><td>WD0E中断使能0:WD0E中断禁能1:WD0E中断使能</td></tr><tr><td>5</td><td>EORCIE</td><td>EORC中断使能0:EORC中断禁能1:EORC中断使能</td></tr><tr><td>4:0</td><td>WD0CHSEL[4:0]</td><td>模拟看门狗0通道选择00000:ADC通道00001:ADC通道100010:ADC通道200011:ADC通道300100:ADC通道400101:ADC通道500110:ADC通道6</td></tr></table>

注意：ADC0 的模拟输入通道 16 和通道 17 分别连接到温度传感器和 V<sub>REFINT</sub>。

## 21.7.3. 控制寄存器 1（ADC_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>TSVEN</td><td>INREFEN</td><td>SWRCST</td><td>SWICST</td><td>Reserved</td><td colspan="2">ETMRC[1:0]</td><td colspan="2">保留</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="2">rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="2">ETMIC[1:0]</td><td>保留</td><td>DAL</td><td colspan="2">保留</td><td>RDMA</td><td>IDMA</td><td colspan="5">保留</td><td>CTN</td><td>ADCON</td></tr><tr><td></td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="5"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>TSVEN</td><td>ADC0的通道16(温度传感器)使能0: ADC0的通道16禁能1: ADC0的通道16使能</td></tr><tr><td>23</td><td>INREFEN</td><td>ADC0的通道17(内部参考电压<eq>V_{REFINT}</eq>)使能0: ADC0的通道17禁能1: ADC0的通道17使能</td></tr><tr><td>22</td><td>SWRCST</td><td>常规序列软件启动转换如果ETMRC是11,该位置‘1’开启常规序列转换。软件置位,软件清零,或转换开始后,由硬件清零。</td></tr><tr><td>21</td><td>SWICST</td><td>注入序列软件启动转换如果ETMIC是11,该位置‘1’开启注入序列转换。软件置位,软件清零,或转换开始后,由硬件清零。</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19: 18</td><td>ETMRC[1:0]</td><td>常规序列外部触发模式00,01,10: 常规序列外部触发上升沿使能11: 常规序列外部触发禁能</td></tr><tr><td>17: 15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14: 13</td><td>ETMIC[1:0]</td><td>注入序列外部触发模式00,01,10: 注入序列外部触发上升沿使能11: 注入序列外部触发禁能</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>DAL</td><td>数据对齐0: 最低有效位对齐1: 最高有效位对齐</td></tr><tr><td>10: 9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>RDMA</td><td>常规序列的DMA请求使能0: DMA请求禁止1: DMA请求使能</td></tr><tr><td>7</td><td>IDMA</td><td>注入序列的DMA请求使能0: DMA请求禁止1: DMA请求使能</td></tr><tr><td>6: 2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CTN</td><td>连续模式0: 禁能连续运行模式1: 使能连续运行模式</td></tr><tr><td>0</td><td>ADCON</td><td>开启ADC该位从‘0’变成‘1’将在稳定时间结束后唤醒ADC。当该位被置位以后,不改变寄存器的其他位仅仅对该位写‘1’,将开启转换。0: 禁能ADC关闭电源1: 使能ADC</td></tr></table>

## 21.7.4. 采样时间寄存器 0（ADC_SAMPT0）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="3">SPT17[2:0]</td><td colspan="3">SPT16[2:0]</td><td colspan="2">SPT15[2:1]</td></tr><tr><td colspan="11">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPT15[0]</td><td colspan="3">SPT14[2:0]</td><td colspan="3">SPT13[2:0]</td><td colspan="3">SPT12[2:0]</td><td colspan="3">SPT11[2:0]</td><td colspan="3">SPT10[2:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:21</td><td>SPT17[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT16[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT15[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT14[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT13[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT12[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT11[2:0]</td><td>参考 SPT10[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT10[2:0]</td><td>通道采样时间000:通道采样时间为1.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 21.7.5. 采样时间寄存器 1（ADC_SAMPT1）

地址偏移：0x10

复位值：0x0000 0000


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">SPT9[2:0]</td><td colspan="3">SPT8[2:0]</td><td colspan="3">SPT7[2:0]</td><td colspan="3">SPT6[2:0]</td><td colspan="2">SPT5[2:1]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>SPT5[0]</td><td>SPT4[2:0]</td><td>SPT3[2:0]</td><td>SPT2[2:0]</td><td>SPT1[2:0]</td><td>SPT0[2:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>SPT9[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>26:24</td><td>SPT8[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>23:21</td><td>SPT7[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>20:18</td><td>SPT6[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>17:15</td><td>SPT5[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>14:12</td><td>SPT4[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>11:9</td><td>SPT3[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>8:6</td><td>SPT2[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>5:3</td><td>SPT1[2:0]</td><td>参考 SPT0[2:0]的描述</td></tr><tr><td>2:0</td><td>SPT0[2:0]</td><td>通道采样时间000:通道采样时间为1.5周期001:通道采样时间为7.5周期010:通道采样时间为13.5周期011:通道采样时间为28.5周期100:通道采样时间为41.5周期101:通道采样时间为55.5周期110:通道采样时间为71.5周期111:通道采样时间为239.5周期</td></tr></table>

## 21.7.6. 注入通道数据偏移寄存器 x（ADC_IOFFx）（x=0..3）

地址偏移：0x14-0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">IOFF[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>IOFF[11:0]</td><td>注入通道x的数据偏移当转换注入通道时,这些位定义了用于从原始转换数据中减去的数值。转换的结果可以在ADC_IDATA寄存器中读出。</td></tr></table>

## 21.7.7. 看门狗高阈值寄存器（ADC_WD0HT）

地址偏移：0x24

复位值：0x000F FFFF

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">WD0HT[19:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WD0HT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:0</td><td>WD0HT[19:0]</td><td>模拟看门狗 0 高侧阈值这些位定义了模拟看门狗 0 的高阈值。</td></tr></table>

## 21.7.8. 看门狗低阈值寄存器（ADC_WD0LT）

地址偏移：0x28

复位值：0x000F FFFF

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="4">WDOLT[19:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WDOLT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">RL[3:0]</td><td colspan="4">RSQ15[4:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ15[0]</td><td colspan="5">RSQ14[4:0]</td><td colspan="5">RSQ13[4:0]</td><td colspan="5">RSQ12[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">说明</td></tr><tr><td>31:24</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>23:20</td><td colspan="4">RL[3:0]</td><td colspan="11">常规序列长度常规转换序列中的总的通道数目为RL[3:0]+1。</td></tr><tr><td>19:15</td><td colspan="4">RSQ15[4:0]</td><td colspan="11">参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td colspan="4">RSQ14[4:0]</td><td colspan="11">参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td colspan="4">RSQ13[4:0]</td><td colspan="11">参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td colspan="4">RSQ12[4:0]</td><td colspan="11">参考RSQ0[4:0]的描述</td></tr></table>

19:0 WD0LT[19:0] 模拟看门狗 0 低侧阈值

这些位定义了模拟看门狗 0 的低阈值。

## 21.7.9. 常规序列寄存器 0（ADC_RSQ0）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

## 21.7.10. 常规序列寄存器 1（ADC_RSQ1）

地址偏移：0x30

复位值：0x0000 0000


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ11[4:0]</td><td colspan="5">RSQ10[4:0]</td><td colspan="4">RSQ9[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ9[0]</td><td colspan="5">RSQ8[4:0]</td><td colspan="5">RSQ7[4:0]</td><td colspan="5">RSQ6[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>位/位域</td><td>名称</td><td colspan="14">说明</td></tr><tr><td>31:30</td><td>保留</td><td colspan="14">必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ11[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ10[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ9[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ8[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ7[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ6[4:0]</td><td colspan="14">参考RSQ0[4:0]的描述</td></tr></table>

## 21.7.11. 常规序列寄存器 2（ADC_RSQ2）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="5">RSQ5[4:0]</td><td colspan="5">RSQ4[4:0]</td><td colspan="4">RSQ3[4:1]</td></tr><tr><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RSQ3[0]</td><td colspan="5">RSQ2[4:0]</td><td colspan="5">RSQ1[4:0]</td><td colspan="5">RSQ0[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:25</td><td>RSQ5[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>24:20</td><td>RSQ4[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>19:15</td><td>RSQ3[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>RSQ2[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>RSQ1[4:0]</td><td>参考RSQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>RSQ0[4:0]</td><td>通道编号(0..17)写入这些位来选择常规序列的第n个转换的通道</td></tr></table>

## 21.7.12. 注入序列寄存器（ADC_ISQ）

地址偏移：0x38

复位值：0x0000 0000


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="2">IL[1:0]</td><td colspan="4">ISQ3[4:1]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ISQ3[0]</td><td colspan="5">ISQ2[4:0]</td><td colspan="5">ISQ1[4:0]</td><td colspan="5">ISQ0[4:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>IL[1:0]</td><td>注入序列长度注入序列总的通道数目为 IL[1:0]+1。</td></tr><tr><td>19:15</td><td>ISQ3[4:0]</td><td>参考 ISQ0[4:0]的描述</td></tr><tr><td>14:10</td><td>ISQ2[4:0]</td><td>参考 ISQ0[4:0]的描述</td></tr><tr><td>9:5</td><td>ISQ1[4:0]</td><td>参考 ISQ0[4:0]的描述</td></tr><tr><td>4:0</td><td>ISQ0[4:0]</td><td>通道编号(0..17)写入这些位来选择注入序列的第 n 个转换的通道和常规序列不同的是,如果 IL[1:0]长度不足 4,注入通道转换从(4-IL[1:0]-1)开始。</td></tr><tr><td></td><td></td><td>IL 注入通道转换顺序</td></tr><tr><td></td><td></td><td>3 ISQ0 &gt;&gt; ISQ1 &gt;&gt; ISQ2 &gt;&gt; ISQ3</td></tr><tr><td></td><td></td><td>2 ISQ1 &gt;&gt; ISQ2 &gt;&gt; ISQ3</td></tr><tr><td></td><td></td><td>1 ISQ2 &gt;&gt; ISQ3</td></tr><tr><td></td><td></td><td>0 ISQ3</td></tr></table>

## 21.7.13. 锁存数据寄存器 x（ADC_LDATAx）（x= 0..3）

地址偏移：0x3C + 0x04 * x (x=0..3)

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LDATAn [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>LDATAn[15:0]</td><td>注入或者常规序列第n个转换数据这些位包含了注入或者常规序列第n个转换数据,只读。</td></tr></table>

## 21.7.14. 常规数据寄存器（ADC_RDATA）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADC1RDATA[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>ADC1RDTR[15:0]</td><td>ADC1常规通道数据在ADC0中:在同步模式下,这些位包含着ADC1的常规通道数据。在ADC1中:这些位保留。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>常规通道数据这些位包含了常规通道的转换结果,只读。</td></tr></table>

## 21.7.15. 注入数据寄存器（ADC_IDATA）

地址偏移：0x50

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>IDATA[15:0]</td><td>注入通道转换的数据</td></tr></table>

这些位包含了注入通道的转换结果，只读。

## 21.7.16. 锁存数据控制寄存器（ADC_LDCTL）

地址偏移：0x54

复位值：0x0001 0203

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SEQSEL0</td><td colspan="3">保留</td><td colspan="4">COVSEL0[3:0]</td><td>SEQSEL1</td><td colspan="3">保留</td><td colspan="4">COVSEL1[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SEQSEL2</td><td colspan="3">保留</td><td colspan="4">COVSEL2[3:0]</td><td>SEQSEL3</td><td colspan="3">保留</td><td colspan="4">COVSEL3[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SEQSEL0</td><td>ADC_LDATA0寄存器序列源选择0:选择注入序列1:选择常规序列注意:只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>COVSEL0[3:0]</td><td>ADC_LDATA0寄存器转换源选择当ADC_LDATA0寄存器用于序列转换时,可以选择将注入序列(SEQSEL0=0)或者常规序列(SEQSEL0=1)的第n个转换的数据存储在ADC_LDATA0寄存器中。0000:序列第0个转换0001:序列第1个转换0010:序列第2个转换...1111:序列第15个转换其他值保留。注意:在注入序列(SEQSEL0=0)中,只能为4&#x27;b0000、4&#x27;b0001、4&#x27;b0010和4&#x27;b0011,默认值为4&#x27;b0000。只有在ADC禁能(ADCON=0)时,才能软件写这些位。</td></tr><tr><td>23</td><td>SEQSEL1</td><td>参考SEQSEL0描述。</td></tr><tr><td>22:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>COVSEL1[3:0]</td><td>参考COVSEL0[3:0]描述。</td></tr><tr><td>15</td><td>SEQSEL2</td><td>参考SEQSEL0描述。</td></tr></table>

<table><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>COVSEL2[3:0]</td><td>参考COVSEL0[3:0]描述。</td></tr><tr><td>7</td><td>SEQSEL3</td><td>参考SEQSEL0描述。</td></tr><tr><td>6:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>COVSEL3[3:0]</td><td>参考COVSEL0[3:0]描述。</td></tr></table>

## 21.7.17. 过采样控制寄存器（ADC_OVSAMPCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">DRES[1: 0]</td><td colspan="2">保留</td><td>TOVS</td><td colspan="4">OVSS[3: 0]</td><td colspan="3">OVR[2: 0]</td><td>保留</td><td>OVSEN</td></tr><tr><td colspan="2"></td><td colspan="2">Rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>DRES[1:0]</td><td>ADC分辨率00:12位01:10位10:8位11:6位</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TOVS</td><td>过采样触发该位通过软件置位和清除。0:在一次触发后连续执行过采样通道的所有转换1:对于过采样通道的每次转换都需要一次触发,触发次数由过采样率(OVSR[2:0])决定。注意:只有在ADCON=0的时候才允许通过软件对该位进行写操作(确保没有转换正在执行)。</td></tr><tr><td>8:5</td><td>OVSS[3:0]</td><td>过采样移位该位通过软件置位和清除。0000:不移位</td></tr></table>

0001：移 1 位0010：移 2 位0011：移 3 位0100：移 4 位0101：移 5 位0110：移 6 位0111：移 7 位1000：移 8 位

注意：只有在 ADCON=0 的时候才允许通过软件对该位进行写操作（确保没有转换正在执行）。

过采样率这些位定义000：2x001：4x010：8x011：16x100：32x101：64x110：128x111：256x

注意：只有在 ADCON=0 的时候才允许通过软件对该位进行写操作（确保没有转换正在执行）。

1 保留 必须保持复位值。

该位通过软件置位和清除。

注意：只有在 ADCON=0 的时候才允许通过软件对该位进行写（确保没有转换正在执行）。
