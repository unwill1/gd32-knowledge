# 40.5. LPDTS 寄存器

LPDTS基地址：0x5800 6800

# 40.5.1. LPDTS 配置寄存器（LPDTS_CFG）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>REFSEL</td><td colspan="4">SPT[3:0]</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">ITSEL[3:0]</td><td colspan="3">保留</td><td>TRGS</td><td colspan="3">保留</td><td>TSEN</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="4">rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>REFSEL</td><td>参考时钟选择位0:高速参考时钟(PCLK)1:低速参考时钟(LXTAL)</td></tr><tr><td>19:16</td><td>SPT[3:0]</td><td>采样时间采样时间的增加有利于提高采样精度</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>ITSEL[3:0]</td><td>触发输入选择位设置此位能够选择温度测量的触发输入源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TRGS</td><td>频率测量触发选择位0:无软件触发1:当模块准备完成时软件触发频率测量</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>TSEN</td><td>使能LPDTS模块0:禁止LPDTS模块1:使能LPDTS模块</td></tr></table>

# 40.5.2. T0 传感器数据寄存器（LPDTS_SDATA）

地址偏移：0x08

复位值：0x000X XXXX

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">VAL[1:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FREQ[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>VAL[1:0]</td><td>采集温度值采集到的T0温度值0x00: 25 °C0x01: -40 °C其他: 保留</td></tr><tr><td>15:0</td><td>FREQ[15:0]</td><td>频率值当外界环境为T0时采集到的频率值注意: 采集单位设置为 0.1 kHz</td></tr></table>

# 40.5.3. 斜率数据寄存器（LPDTS_RDATA）

地址偏移：0x10

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RCVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RCVAL[15:0]</td><td>斜率值这些位定义了LPDTS模块的温度测量斜率值注意:采集单位设置为 1 Hz/°C</td></tr></table>

# 40.5.4. 中断阈值寄存器（LPDTS_IT）

地址偏移：0x014

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">INTHT[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">INTLT[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>INTHT[15:0]</td><td>中断高阈值这些位定义了温度中断高阈值,当采集值高于此值时将产生中断。</td></tr><tr><td>15:0</td><td>INTLT[15:0]</td><td>中断低阈值这些位定义了温度中断低阈值,当采集值低于此值时将产生中断。</td></tr></table>

# 40.5.5. 温度值寄存器（LPDTS_DATA）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">COVAL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>COVAL[15:0]</td><td>计数器输出值</td></tr></table>

# 40.5.6. 温度传感器状态寄存器（LPDTS_STAT）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

保留

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TSRF</td><td colspan="8">保留</td><td>HTAIF</td><td>LTAIF</td><td>EMAIF</td><td>保留</td><td>HTIF</td><td>LTIF</td><td>EMIF</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>TSRF</td><td>温度传感器准备标志0: 温度传感器准备未完成1: 温度传感器准备完成</td></tr><tr><td>14:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>HTAIF</td><td>高阈值异步中断标志位当达到温度高阈值并且HTAIE位置位时,此位被硬件置位。当LPDTS_INTC寄存器中的HTAIC位置位时,此位被软件复位。0: 未产生高阈值异步中断1: 产生高阈值异步中断</td></tr><tr><td>5</td><td>LTAIF</td><td>低阈值异步中断标志位当达到温度低阈值并且LTAIE位置位时,此位被硬件置位。当LPDTS_INTC寄存器中的LTAIC位置位时,此位被软件复位。0: 未产生低阈值异步中断1: 产生低阈值异步中断</td></tr><tr><td>4</td><td>EMAIF</td><td>测量完成异步中断标志位当达到温度测量完成并且EMAIE位置位时,此位被硬件置位。当LPDTS_INTC寄存器中的EMAIC位置位时,此位被软件复位。0: 未产生温度测量完成异步中断1: 产生温度测量完成异步中断</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>HTIF</td><td>高阈值中断标志位当达到温度高阈值并且HTIE位置位时,此位被硬件置位(与PCLK同步)。当LPDTS_INTC寄存器中的HTIC位置位时,此位被软件复位。0: 未产生高阈值中断1: 产生高阈值中断</td></tr><tr><td>1</td><td>LTIF</td><td>低阈值中断标志位当达到温度低阈值并且LTIE位置位时,此位被硬件置位(与PCLK同步)。当LPDTS_INTC寄存器中的LTIC位置位时,此位被软件复位。0: 未产生低阈值中断1: 产生低阈值中断</td></tr><tr><td>0</td><td>EMIF</td><td>测量完成中断标志位</td></tr></table>

当达到温度测量完成并且EMIE位置位时，此位被硬件置位（与PCLK同步）。

当LPDTS_INTC寄存器中的EMIC位置位时，此位被软件复位。

0：未产生温度测量完成中断

1：产生温度测量完成中断

# 40.5.7. 中断使能寄存器（LPDTS_INTEN）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>HTAIE</td><td>LTAIE</td><td>EMAIE</td><td>保留</td><td>HTIE</td><td>LTIE</td><td>EMIE</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>HTAIE</td><td>高阈值异步中断使能位通过软件复位/置位来失能/使能高阈值异步中断(仅当REFSEL=1有效)0:失能高阈值异步中断1:使能高阈值异步中断</td></tr><tr><td>5</td><td>LTAIE</td><td>低阈值异步中断使能位通过软件复位/置位来失能/使能低阈值异步中断(仅当REFSEL=1有效)0:失能低阈值异步中断1:使能低阈值异步中断</td></tr><tr><td>4</td><td>EMAIE</td><td>测量完成异步中断使能位通过软件复位/置位来失能/使能测量完成异步中断(仅当REFSEL=1有效)0:失能测量完成异步中断1:使能测量完成异步中断</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>HTIE</td><td>高阈值中断使能位通过软件复位/置位来失能/使能高阈值中断(与PCLK同步)0:失能高阈值中断1:使能高阈值中断</td></tr><tr><td>1</td><td>LTIE</td><td>低阈值中断使能位通过软件复位/置位来失能/使能低阈值中断(与PCLK同步)0:失能低阈值中断1:使能低阈值中断</td></tr></table>

<table><tr><td>0</td><td>EMIE</td><td>测量完成中断使能位</td></tr><tr><td></td><td></td><td>通过软件复位/置位来失能/使能测量完成中断(与PCLK同步)</td></tr><tr><td></td><td></td><td>0: 失能测量完成中断</td></tr><tr><td></td><td></td><td>1: 使能测量完成中断</td></tr></table>

# 40.5.8. 中断标志清除寄存器（LPDTS_INTC）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>HTAIC</td><td>LTAIC</td><td>EMAIC</td><td>保留</td><td>HTIC</td><td>LTIC</td><td>EMIC</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>HTAIC</td><td>高阈值异步中断清除位通过软件置位来清除LPDTS_STAT寄存器中的HTAIF标志位</td></tr><tr><td>5</td><td>LTAIC</td><td>低阈值异步中断清除位通过软件置位来清除LPDTS_STAT寄存器中的LTAIF标志位</td></tr><tr><td>4</td><td>EMAIC</td><td>测量完成异步中断清除位通过软件置位来清除LPDTS_STAT寄存器中的EMAIF标志位</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>HTIC</td><td>高阈值中断清除位通过软件置位来清除LPDTS_STAT寄存器中的HTIF标志位</td></tr><tr><td>1</td><td>LTIC</td><td>低阈值中断清除位通过软件置位来清除LPDTS_STAT寄存器中的LTIF标志位</td></tr><tr><td>0</td><td>EMIC</td><td>测量完成中断清除位通过软件置位来清除LPDTS_STAT寄存器中的EMIF标志位</td></tr></table>

# 40.5.9. 选择寄存器（LPDTS_OP）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OP[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OP[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OP [31:0]</td><td>通用选项位</td></tr></table>
