## 35.4. FAC 寄存器

FAC 基地址：0x4802 4800

## 35.4.1. FAC X0 缓冲区配置寄存器（FAC_X0BCFG）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问，仅在FAC_PARACFG寄存器的EXE位为0时可修改。

## 35.4.2. FAC X1 缓冲区配置寄存器（FAC_X1BCFG）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">X1B_SIZE[7:0]</td><td colspan="8">X1B_ADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>X1B_SIZE[7:0]</td><td>X1 缓冲区分配大小当 FAC 正在运行(EXE=1)时,该位域不可改变。</td></tr><tr><td>7:0</td><td>X1B_ADDR[7:0]</td><td>X1 缓冲区基地址当 FAC 正在运行(EXE=1)时,该位域可进行改变,当改变滤波器系数值时,滤波器应该暂停,因为在滤波器计算过程中改变滤波器参数会影响输出结果。</td></tr></table>

## 35.4.3. FAC Y 缓冲区配置寄存器（FAC_YBCFG）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。该寄存器仅在FAC_PARACFG寄存器的EXE位为0时可修改。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="2">Y_WBEF[1:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">YB_SIZE[7:0]</td><td colspan="8">YB_ADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>Y_WBEF[1:0]</td><td>缓冲区水印区空标志如果缓冲区水印区可用空间的数目少于<eq>2^{Y\_WBEF}</eq>,标志位置位。00:阈值为101:阈值为210:阈值为411:阈值为8如果若干数据在一次中断中传输到缓冲区,设置阈值大于1。如果DMA读数据指令被使能,阈值应设置为1。</td></tr><tr><td>23:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>YB_SIZE[7:0]</td><td>Y缓冲区分配大小对于FIR滤波器,最小缓冲区大小为水印区阈值加1。</td></tr></table>

<table><tr><td></td><td colspan="2">对于IIR滤波器,最小缓冲区大小为水印区阈值与反馈抽头数目之和。</td></tr><tr><td>7:0</td><td>YB_ADDR[7:0]</td><td>Y缓冲区基地址。</td></tr></table>

## 35.4.4. FAC 参数配置寄存器（FAC_PARACFG）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>EXE</td><td colspan="7">FUN[6:0]</td><td colspan="8">IPR[7:0]</td></tr><tr><td>rw</td><td colspan="7">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IPQ[7:0]</td><td colspan="8">IPP[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>EXE</td><td>执行0: FAC停止运行1: FAC开始运行使能该位,FAC会执行FUN位域定义的功能,当产生软件复位时,FAC会停止任何正在进行的功能。该位由硬件复位以实现初始化功能。</td></tr><tr><td>30:24</td><td>FUN[6:0]</td><td>功能0000001:加载X0缓冲区0000010:加载X1缓冲区0000011:加载Y缓冲区0001000:FIR滤波器0001001:IIR滤波器其他:保留该位仅在FAC_PARACFG寄存器的EXE位为0时可修改。</td></tr><tr><td>23:16</td><td>IPR</td><td>输入参数IPR该位仅在FAC_PARACFG寄存器的EXE位为0时可修改。</td></tr><tr><td>15:8</td><td>IPQ</td><td>输入参数IPQ该位仅在FAC_PARACFG寄存器的EXE位为0时可修改。</td></tr><tr><td>7:0</td><td>IPP</td><td>输入参数IPP该位仅在FAC_PARACFG寄存器的EXE位为0时可修改。</td></tr></table>

## 35.4.5. FAC 控制寄存器（FAC_CTL）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>RST</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CPEN</td><td>FLTEN</td><td colspan="4">保留</td><td>DWEN</td><td>DREN</td><td colspan="2">保留</td><td>GSTEIE</td><td>STEIE</td><td>UFEIE</td><td>OFEIE</td><td>WIE</td><td>RIE</td></tr><tr><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>RST</td><td>复位 FAC 单元0:除能复位1:使能复位当 RST=1 时,写指针、读指针、EXE 位、FAC_STAT 寄存器、FAC_PARACFG 寄存器会产生复位。</td></tr><tr><td>15</td><td>CPEN</td><td>限幅使能0:限幅禁能,累加器超出范围的值被截断。1:限幅使能,累加器超出范围的值被限幅到最大正值或最小负值。</td></tr><tr><td>14</td><td>FLTEN</td><td>浮点格式使能0:输入数据和结果支持定点有符号整数格式q1.15。1:输入数据和结果支持32位单精度浮点格式。该位仅在FAC_PARACFG寄存器的EXE位为0时可修改。</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>DWEN</td><td>DMA 写通道使能0:未产生DMA请求1:在 X0 缓冲区未满的情况下,产生 DMA 请求该位仅在 FAC_PARACFG 寄存器的 EXE 位为 0 时可修改。</td></tr><tr><td>8</td><td>DREN</td><td>DMA 读通道使能0:未产生DMA请求1:在 Y 缓冲区未空的情况下,产生 DMA 请求该位仅在 FAC_PARACFG 寄存器的 EXE 位为 0 时可修改。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>GSTEIE</td><td>增益饱和错误中断使能0:未产生中断.1:如果GSTEF标志置1,产生中断请求软件置位和复位该位</td></tr><tr><td>4</td><td>STEIE</td><td>饱和错误中断使能0:未产生中断.1:如果STEF标志置1,产生中断请求软件置位和复位该位。</td></tr><tr><td>3</td><td>UFEIE</td><td>下溢错误中断使能0:未产生中断.1:如果UFEF标志置1,产生中断请求软件置位和复位该位。</td></tr><tr><td>2</td><td>OFEIE</td><td>上溢错误中断使能0:未产生中断1:如果OFEF标志置1,产生中断请求软件置位和复位该位。</td></tr><tr><td>1</td><td>WIE</td><td>写中断使能0:未产生中断.1:如果X0BFF标志置1,产生中断请求软件置位和复位该位。</td></tr><tr><td>0</td><td>RIE</td><td>读中断使能0:未产生中断.1:如果YBEF标志置1,产生中断请求软件置位和复位该位。</td></tr></table>

## 35.4.6. FAC 状态寄存器（FAC_STAT）

地址偏移：0x14

复位值：0x0000 0001

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>GSTEF</td><td>STEF</td><td>UFEF</td><td>OFEF</td><td colspan="6">保留</td><td>X0BFF</td><td>YBEF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>GSTEF</td><td>增益饱和错误标志,在增益后超过范围时置位。0:未检测到增益饱和错误1:增益饱和错误被检测</td></tr><tr><td>10</td><td>STEF</td><td>饱和错误标志0:未检测到饱和错误1:饱和错误被检测当累积结果超出范围时发生饱和。</td></tr><tr><td>9</td><td>UFEF</td><td>下溢错误标志0:未检测到下溢错误1:检测到下溢错误当Y缓冲区中没有可用有效数据时,从FAC_RDATA读取数据时发生下溢错误。</td></tr><tr><td>8</td><td>OFEF</td><td>上溢错误标志0:未检测到上溢错误1:检测到上溢错误当X1缓冲区中没有空闲空间时,向FAC_WDATA写数据时会产生上溢错误。</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>X0BFF</td><td>X0缓冲区满标志0:X0缓冲区未满1:X0缓冲区已满硬件或复位会置位或复位该标志。</td></tr><tr><td>0</td><td>YBEF</td><td>Y缓冲区空标志0:Y缓冲区未空1:Y缓冲区已空硬件或复位会置位或复位该标志。</td></tr></table>

## 35.4.7. FAC 写数据寄存器（FAC_WDATA）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WDATA</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>WDATA</td></tr></table>

当FLTEN为1时，浮点数据被选择

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WDATA[31:0]</td><td>写数据当对寄存器执行写命令时,写数据被传送到写指针指向的地址偏移,每次写入数据完成后,指针地址递增。</td></tr></table>


当FLTEN为0时，定点数据被选择


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>WDATA[15:0]</td><td>写数据当对寄存器执行写命令时,写数据被传送到写指针指向的地址偏移,每次写入数据完成后,指针地址递增。</td></tr></table>

## 35.4.8. FAC 读数据寄存器（FAC_RDATA）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RDATA</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RDATA</td></tr></table>

## 当FLTEN为1时，浮点数据被选择

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RDATA[31:0]</td><td>读数据当对寄存器执行读命令时,读指针指向的Y缓冲区的内容就是读到的数据,每次读数据完成时,读指针递增。</td></tr></table>

当FLTEN为0时，定点数据被选择

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>RDATA[15:0]</td><td>读数据当对寄存器执行读命令时,读指针指向的Y缓冲区的内容就是读到的数据,每次读数据完成时,读指针递增。</td></tr></table>
