## 14.6. DMA寄存器

DMA0 基地址：0x4002 6000

DMA1 基地址：0x4002 6400

## 14.6.1. 中断标志位寄存器 0（DMA_INTF0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FTFIF3</td><td>HTFIF3</td><td>TAEIF3</td><td>SDEIF3</td><td>保留</td><td>FEEIF3</td><td>FTFIF2</td><td>HTFIF2</td><td>TAEIF2</td><td>SDEIF2</td><td>保留</td><td>FEEIF2</td></tr><tr><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>FTFIF1</td><td>HTFIF1</td><td>TAEIF1</td><td>SDEIF1</td><td>保留</td><td>FEEIF1</td><td>FTFIF0</td><td>HTFIF0</td><td>TAEIF0</td><td>SDEIF0</td><td>保留</td><td>FEEIF0</td></tr><tr><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/21/11/5</td><td>FTFIFx</td><td>通道x的传输完成标志位(x=0...3)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x传输未完成1:通道x传输完成</td></tr><tr><td>26/20/10/4</td><td>HTFIFx</td><td>通道x的半传输完成标志位(x=0...3)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x半传输未完成1:通道x半传输完成</td></tr><tr><td>25/19/9/3</td><td>TAEIFx</td><td>通道x的传输错误标志位(x=0...3)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x未发生传输错误1:通道x发生传输错误</td></tr><tr><td>24/18/8/2</td><td>SDEIFx</td><td>通道x的单数据传输模式异常标志位(x=0...3)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x未发生单数据传输模式异常1:通道x发生单数据传输模式异常</td></tr><tr><td>23/17/7/1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22/16/6/0</td><td>FEEIFx</td><td>通道x的FIFO错误与FIFO异常标志位(x=0...3)硬件置位,软件写DMA_INTC0相应位为11清零。0:通道x未发生FIFO错误或FIFO异常</td></tr></table>

## 1：通道x发生FIFO错误或FIFO异常

## 14.6.2. 中断标志位寄存器 1（DMA_INTF1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FTFIF7</td><td>HTFIF7</td><td>TAEIF7</td><td>SDEIF7</td><td>保留</td><td>FEEIF7</td><td>FTFIF6</td><td>HTFIF6</td><td>TAEIF6</td><td>SDEIF6</td><td>保留</td><td>FEEIF6</td></tr><tr><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>FTFIF5</td><td>HTFIF5</td><td>TAEIF5</td><td>SDEIF5</td><td>保留</td><td>FEEIF5</td><td>FTFIF4</td><td>HTFIF4</td><td>TAEIF4</td><td>SDEIF4</td><td>保留</td><td>FEEIF4</td></tr><tr><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/21/11/5</td><td>FTFIFx</td><td>通道x的传输完成标志位(x=4...7)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x传输未完成1:通道x传输完成</td></tr><tr><td>26/20/10/4</td><td>HTFIFx</td><td>通道x的半传输完成标志位(x=4...7)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x半传输未完成1:通道x半传输完成</td></tr><tr><td>25/19/9/3</td><td>TAEIFx</td><td>通道x的传输错误标志位(x=4...7)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x未发生传输错误1:通道x发生传输错误</td></tr><tr><td>24/18/8/2</td><td>SDEIFx</td><td>通道x的单数据传输模式异常标志位(x=4...7)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x未发生单数据传输模式异常1:通道x发生单数据传输模式异常</td></tr><tr><td>23/17/7/1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22/16/6/0</td><td>FEEIFx</td><td>通道x的FIFO错误与FIFO异常标志位(x=4...7)硬件置位,软件写DMA_INTC0相应位为1清零。0:通道x未发生FIFO错误或FIFO异常1:通道x发生FIFO错误或FIFO异常</td></tr></table>

## 14.6.3. 中断标志位清除寄存器（DMA_INTC0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FTFIFC3</td><td>HTFIFC3</td><td>TAEIFC3</td><td>SDEIFC3</td><td>保留</td><td>FEEIFC3</td><td>FTFIFC2</td><td>HTFIFC2</td><td>TAEIFC2</td><td>SDEIFC2</td><td>保留</td><td>FEEIFC2</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>FTFIFC1</td><td>HTFIFC1</td><td>TAEIFC1</td><td>SDEIFC1</td><td>保留</td><td>FEEIFC1</td><td>FTFIFC0</td><td>HTFIFC0</td><td>TAEIFC0</td><td>SDEIFC0</td><td>保留</td><td>FEEIFC0</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/21/11/5</td><td>FTFIFCx</td><td>通道x的传输完成标志清除位(x=0...3)0:无影响1:清除传输完成标志位</td></tr><tr><td>26/20/10/4</td><td>HTFIFCx</td><td>通道x的半传输完成标志清除位(x=0...3)0:无影响1:清除半传输完成标志位</td></tr><tr><td>25/19/9/3</td><td>TAEIFCx</td><td>通道x的传输错误标志清除位(x=0...3)0:无影响1:清除传输错误标志位</td></tr><tr><td>24/18/8/2</td><td>SDEIFCx</td><td>通道x的单数据传输模式异常标志清除位(x=0...3)0:无影响1:清除单数据传输模式异常标志位</td></tr><tr><td>23/17/7/1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22/16/6/0</td><td>FEEIFCx</td><td>通道x的FIFO错误与FIFO异常标志清除位(x=0...3)0:无影响1:清除FIFO错误与FIFO异常标志位</td></tr></table>

## 14.6.4. 中断标志位清除寄存器 1（DMA_INTC1）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>FTFIFC7</td><td>HTFIFC7</td><td>TAEIFC7</td><td>SDEIFC7</td><td>保留</td><td>FEEIFC7</td><td>FTFIFC6</td><td>HTFIFC6</td><td>TAEIFC6</td><td>SDEIFC6</td><td>保留</td><td>FEEIFC6</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>FTFIFC5</td><td>HTFIFC5</td><td>TAEIFC5</td><td>SDEIFC5</td><td>保留</td><td>FEEIFC5</td><td>FTFIFC4</td><td>HTFIFC4</td><td>TAEIFC4</td><td>SDEIFC4</td><td>保留</td><td>FEEIFC4</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td></td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/21/11/5</td><td>FTFIFCx</td><td>通道x的传输完成标志清除位(x=4...7)0:无影响1:清除传输完成标志位</td></tr><tr><td>26/20/10/4</td><td>HTFIFCx</td><td>通道x的半传输完成标志清除位(x=4...7)0:无影响1:清除半传输完成标志位</td></tr><tr><td>25/19/9/3</td><td>TAEIFCx</td><td>通道x的传输错误标志清除位(x=4...7)0:无影响1:清除传输错误标志位</td></tr><tr><td>24/18/8/2</td><td>SDEIFCx</td><td>通道x的单数据传输模式异常标志清除位(x=4...7)0:无影响1:清除单数据传输模式异常标志位</td></tr><tr><td>23/17/7/1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22/16/6/0</td><td>FEEIFCx</td><td>通道x的FIFO错误与FIFO异常标志清除位(x=4...7)0:无影响1:清除FIFO错误与FIFO异常标志位</td></tr></table>

## 14.6.5. 通道 x 控制寄存器（DMA_CHxCTL）

x = 0..7,x为通道编号

地址偏移：0x10 + 0x18*x

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="3">PERIEN[2:0]</td><td colspan="2">MBURST[1:0]</td><td colspan="2">PBURST[1:0]</td><td>保留</td><td>MBS</td><td>SBMEN</td><td colspan="2">PRIO[1:0]</td></tr><tr><td colspan="4"></td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td></td><td>rw</td><td>rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PAIF</td><td colspan="2">MWIDTH[1:0]</td><td colspan="2">PWIDTH[1:0]</td><td>MNAGA</td><td>PNAGA</td><td>CMEN</td><td colspan="2">TM[1:0]</td><td>TFCS</td><td>FTFIE</td><td>HTFIE</td><td>TAEIE</td><td>SDEIE</td><td>CHEN</td></tr><tr><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:25</td><td>PERIEN[2:0]</td><td>外设使能软件置1与清0</td></tr></table>

000: 使能外设0
001: 使能外设1
010: 使能外设2
011: 使能外设3
100: 使能外设4
101: 使能外设5
110: 使能外设6
111: 使能外设7
CHEN为1时不可写入

24:23 MBURST[1:0] 存储器突发类型
软件置1与清0
00: 单一传输
01: INCR4 (4拍增量突发传输)
10: INCR8 (8拍增量突发传输)
11: INCR16 (16拍增量突发传输)
CHEN为1时不可写入
如果寄存器DMA_CHxFCTL的MDMEN位为0，在使能通道后（CHEN置1），该位域会被硬件强制清零

22:21 PBURST[1:0] 外设突发类型
软件置1与清0
00: 单一传输
01: INCR4 (4拍增量突发传输)
10: INCR8 (8拍增量突发传输)
11: INCR16 (16拍增量突发传输)
CHEN为1时不可写入
如果寄存器DMA_CHxFCTL的MDMEN位为0，在使能通道后（CHEN置1），该位域会被硬件限制清零

20 保留 必须保持复位值。

19 MBS 存储器缓冲选择
硬件置1清0，软件置1清0
0: 存储器0作为存储器传输区域
1: 存储器1作为存储器传输区域
CHEN为1时不可写入
在每次传输完成时，硬件会自动更新该位，以此来表明DMA正在使用哪个存储区

18 SBMEN 存储切换模式使能
软件置1与清0
0: 关闭存储切换模式
1: 打开存储切换模式
CHEN为1时不可写入

17:16 PRIO[1:0] 软件优先级
软件置1与清0

00: 低
01: 中
10: 高
11: 超高
CHEN为1时不可写入

15 PAIF 外设地址增量固定
软件置1与清0
0: 外设地址增量由PWIDTH决定
1: 外设地址增量固定为4
CHEN为1时不可写入
如果PNAGA设置为0, 该位无影响
如果寄存器DMA_CHxFCTL的MDMEN位为'0'或者PBURST不为'00', 在使能通道后 (CHEN置1), 该位域会被硬件强制清零

14:13 MWIDTH[1:0] 存储器传输宽度
软件置1与清0
00: 8位
01: 16位
10: 32位
11: 保留
CHEN为1时不可写入
如果寄存器DMA_CHxFCTL的MDMEN位为'0', 在使能通道后 (CHEN置1), 该位域会被硬件强制与PWIDTH相等。

12:11 PWIDTH[1:0] 外设传输宽度
软件置1与清0
00: 8位
01: 16位
10: 32位
11: 保留
CHEN为1时不可写入

10 MNAGA 存储器地址生成算法
软件置1与清0
0: 固定地址模式
1: 增量地址模式
CHEN为1时不可写入

9 PNAGA 外设地址生成算法
软件置1与清0
0: 固定地址模式
1: 增量地址模式
CHEN为1时不可写入

8 CMEN 循环模式
软件置1与清0软件清0操作后，读该位仍为1代表还有正在进行的数据传输，软件查询该位可以确定DMA通道是否空闲，可以进行新的数据传输。

<table><tr><td></td><td></td><td>0:关闭循环模式1:打开循环模式CHEN为1时不可写入如果TFCS为‘1’,在使能通道后(CHEN置1),该位被自动清0如果SBMEN为‘1’,在使能通道后(CHEN置1),该位被自动置1</td></tr><tr><td>7:6</td><td>TM[1:0]</td><td>传输方式软件置1与清000:读外设写存储器01:读存储器写外设10:读存储器写存储器11:保留CHEN为1时不可写入</td></tr><tr><td>5</td><td>TFCS</td><td>传输控制器选择软件置1与清00:DMA作为传输控制器1:外设作为传输控制器CHEN为1时不可写入</td></tr><tr><td>4</td><td>FTFIE</td><td>传输完成中断使能位软件置1与清00:传输完成中断禁止1:传输完成中断使能</td></tr><tr><td>3</td><td>HTFIE</td><td>半传输完成中断使能位软件置1与清00:半传输完成中断禁止1:半传输完成中断使能</td></tr><tr><td>2</td><td>TAEIE</td><td>传输错误中断使能位软件置1与清00:传输错误中断禁止1:传输错误中断使能</td></tr><tr><td>1</td><td>SDEIE</td><td>单数据传输模式异常中断使能位软件置1与清00:单数据传输模式异常中断禁止1:单数据传输模式异常中断使能</td></tr><tr><td>0</td><td>CHEN</td><td>通道使能软件置1,硬件清00:通道禁止1:通道使能该位置1,DMA传输开始。发生以下情况该位会被自动清0:■ 数据传输完成- 发生FIFO配置错误或者传输错误</td></tr></table>

## 14.6.6. 通道 x 计数寄存器（DMA_CHxCNT）

$\mathsf { x } = 0 . . . 7 , \mathsf { x }$ 为通道编号

地址偏移： $0 { \times } 1 4 + 0 { \times } 1 8 ^ { \star } { \times }$ 

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>传输计数在使能通道后(CHEN置1),该位域不可写。传输过程中,CNT代表剩余未发的数据量。外设每传输一次数据,CNT减1。如果寄存器DMA_CHxCTL的CMEN位或SBMEN位置1,在每次传输完成时,CNT会由硬件自动重新装载。</td></tr></table>

## 14.6.7. 通道 x 外设基地址寄存器（DMA_CHxPADDR）

$\mathsf { x } = 0 . . . 7 , \mathsf { x }$ 为通道编号

地址偏移： $0 \times 1 8 + 0 \times 1 8 ^ { \star } \mathsf { x }$ 

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PADDR[31:0]</td><td>外设基地址在使能通道后(CHEN置1),该位域不可写。当PWIDTH位‘01’,最低位被忽略,自动半字对齐当PWIDTH位‘10’,最低位两位被忽略,自动字对齐</td></tr></table>

注意：若寄存器DMA_CHxCTL的PAIF位置1，该位域必须配置为4字节对齐。

## 14.6.8. 通道 x 存储器 0 基地址寄存器（DMA_CHxM0ADDR）

$\mathsf { x } = 0 . . . 7 , \mathsf { x }$ 为通道编号

地址偏移：0x1C + 0x18*x

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">M0ADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">M0ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>M0ADDR[31:0]</td><td>存储器0基地址若寄存器DMA_CHxCTL位MBS为0,该位域定义DMA传输过程中存储器的基地址如果寄存器DMA_CHxCTL的CHEN位置1且MBS位为0时,该位域不可写当MWIDTH位‘01’,最低位被忽略,自动半字对齐当MWIDTH位‘10’,最低位两位被忽略,自动字对齐</td></tr></table>

## 14.6.9. 通道 x 存储器 1 基地址寄存器（DMA_CHxM1ADDR）

x = 0...7,x为通道编号

地址偏移：0x20 + 0x18*x

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">M1ADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">M1ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>M1ADDR[31:0]</td><td>存储器1基地址若寄存器DMA_CHxCTL位MBS为1,该位域定义DMA传输过程中存储器的基地址如果寄存器DMA_CHxCTL的CHEN位置1且MBS为1时,该位域不可写当MWIDTH位‘01’,最低位被忽略,自动半字对齐当MWIDTH位‘10’,最低位两位被忽略,自动字对齐</td></tr></table>

## 14.6.10. 通道 xFIFO 控制寄存器（DMA_CHxFCTL）

x = 0...7,x为通道编号

地址偏移：0x24 + 0x18*x

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>FEEIE</td><td>保留</td><td colspan="3">FCNT[2:0]</td><td>MDMEN</td><td colspan="2">FCCV[1:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td></td><td colspan="3">r</td><td>rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>FEEIE</td><td>FIFO错误和异常中断使能位软件置1与清00:FIFO错误和异常中断禁止1:FIFO错误和异常中断使能</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:3</td><td>FCNT[2:0]</td><td>FIFO计数器硬件置位和清零000:FIFO非空并且数据少于1个字001:FIFO数据多于1个字少于2个字010:FIFO数据多于2个字少于3个字011:FIFO数据多于3个字少于4个字100:FIFO空101:FIFO满110~111:保留该位域表明在数据传输过程FIFO中的数据量。若MDMEN为0,则该位域无意义。</td></tr><tr><td>2</td><td>MDMEN</td><td>多数据传输模式使能软件置位与清除0:关闭多数据传输模式1:打开多数据传输模式CHEN为1时不可写入如果寄存器DMA_CHxCTL的TM位域为‘10’,在通道使能后,该位由硬件强制置1.</td></tr><tr><td>1:0</td><td>FCCV[1:0]</td><td>FIFO计数器临界值软件置位与清除00:1个字01:2个字10:3个字</td></tr></table>

## 11：4个字

在通道使能后，该位域不可写。若MDMEN为‘0’，该位域无实际意义。
