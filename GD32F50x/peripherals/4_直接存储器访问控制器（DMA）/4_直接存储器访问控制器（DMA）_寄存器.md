## 4.5. DMA 寄存器

DMA0 基地址：0x4002 0000

DMA1 基地址：0x4002 0400

注意：DMA1 仅有五个通道（0 到 4 通道），所有相关寄存器中通道 5 和通道 6 相关标志位不适用于 DMA1。

## 4.5.1. 中断标志位寄存器 (DMA_INTF)

地址偏移：0x00

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>ERRIF6</td><td>HTFIF6</td><td>FTFIF6</td><td>GIF6</td><td>ERRIF5</td><td>HTFIF5</td><td>FTFIF5</td><td>GIF5</td><td>ERRIF4</td><td>HTFIF4</td><td>FTFIF4</td><td>GIF4</td></tr><tr><td colspan="4"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ERRIF3</td><td>HTFIF3</td><td>FTFIF3</td><td>GIF3</td><td>ERRIF2</td><td>HTFIF2</td><td>FTFIF2</td><td>GIF2</td><td>ERRIF1</td><td>HTFIF1</td><td>FTFIF1</td><td>GIF1</td><td>ERRIF0</td><td>HTFIF0</td><td>FTFIF0</td><td>GIF0</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/23/19/15/11/7/3</td><td>ERRIFx</td><td>通道x错误标志位(x=0...6)硬件置位,软件写DMA_INTC相应位为1清零0:通道x未发生传输错误1:通道x发生传输错误</td></tr><tr><td>26/22/18/14/10/6/2</td><td>HTFIFx</td><td>通道x半传输完成标志位(x=0...6)硬件置位,软件写DMA_INTC相应位为1清零0:通道x半传输未完成1:通道x半传输完成</td></tr><tr><td>25/21/17/13/9/5/1</td><td>FTFIFx</td><td>通道x传输完成标志位(x=0...6)硬件置位,软件写DMA_INTC相应位为1清零0:通道x传输未完成1:通道x传输完成</td></tr><tr><td>24/20/16/12/8/4/0</td><td>GIFx</td><td>通道x全局中断标志位(x=0...6)硬件置位,软件写DMA_INTC相应位为1清零0:通道xERRIF,HTFIF或FTFIF标志位未置位1:通道x至少发生ERRIF,HTFIF或FTFIF之一置位</td></tr></table>

## 4.5.2. 中断标志位清除寄存器 (DMA_INTC)

地址偏移：0x04

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>ERRIFC6</td><td>HTFIFC6</td><td>FTFIFC6</td><td>GIFC6</td><td>ERRIFC5</td><td>HTFIFC5</td><td>FTFIFC5</td><td>GIFC5</td><td>ERRIFC4</td><td>HTFIFC4</td><td>FTFIFC4</td><td>GIFC4</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ERRIFC3</td><td>HTFIFC3</td><td>FTFIFC3</td><td>GIFC3</td><td>ERRIFC2</td><td>HTFIC2</td><td>FTFIFC2</td><td>GIFC2</td><td>ERRIFC1</td><td>HTFIFC1</td><td>FTFIFC1</td><td>GIFC1</td><td>ERRIFC0</td><td>HTFIFC0</td><td>FTFIFC0</td><td>GIFC0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27/23/19/15/11/7/3</td><td>ERRIFCx</td><td>清除通道<eq>x(x=0...6)</eq>的错误标志位0:无影响1:清零DMA_INTF寄存器的ERRIFx位</td></tr><tr><td>26/22/18/14/10/6/2</td><td>HTFIFCx</td><td>清除通道<eq>x(x=0...6)</eq>的半传输完成标志位0:无影响1:清零DMA_INTF寄存器的HTFIFx位</td></tr><tr><td>25/21/17/13/9/5/1</td><td>FTFIFCx</td><td>清除通道<eq>x(x=0...6)</eq>的传输完成标志位0:无影响1:清零DMA_INTF寄存器的FTFIFx位</td></tr><tr><td>24/20/16/12/8/4/0</td><td>GIFCx</td><td>清除通道<eq>x(x=0...6)</eq>的全局中断标志位0:无影响1:清零DMA_INTF寄存器的GIFx,ERRIFx,HTFIFx和FTFIFx位</td></tr></table>

## 4.5.3. 通道 x 控制寄存器 (DMA_CHxCTL)

x = 0...6, x 为通道序号

地址偏移： $0 { \times } 0 8 + 0 { \times } 1 4 \times \mathsf { x }$ 

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>M2M</td><td colspan="2">PRIO[1:0]</td><td colspan="2">MWIDTH[1:0]</td><td colspan="2">PWIDTH[1:0]</td><td>MNAGA</td><td>PNAGA</td><td>CMEN</td><td>DIR</td><td>ERRIE</td><td>HTFIE</td><td>FTFIE</td><td>CHEN</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>M2M</td><td>存储器到存储器模式软件置位和清零0:禁止存储器到存储器模式1:使能存储器到存储器模式CHEN位为1时,该位不能被配置</td></tr><tr><td>13:12</td><td>PRIO[1:0]</td><td>软件优先级软件置位和清零00:低01:中10:高11:极高CHEN位为1时,该位域不能被配置</td></tr><tr><td>11:10</td><td>MWIDTH[1:0]</td><td>存储器的传输数据宽度软件置位和清零00:8-bit01:16-bit10:32-bit11:保留CHEN位为1时,该位域不能被配置</td></tr><tr><td>9:8</td><td>PWIDTH[1:0]</td><td>外设的传输数据宽度软件置位和清零00:8-bit01:16-bit10:32-bit11:保留CHEN位为1时,该位域不能被配置</td></tr><tr><td>7</td><td>MNAGA</td><td>存储器的地址生成算法软件置位和清零0:固定地址模式1:增量地址模式CHEN位为1时,该位不能被配置</td></tr><tr><td>6</td><td>PNAGA</td><td>外设的地址生成算法软件置位和清零0:固定地址模式1:增量地址模式</td></tr></table>

<table><tr><td></td><td></td><td>CHEN位为1时,该位不能被配置</td></tr><tr><td>5</td><td>CMEN</td><td>循环模式使能软件置位和清零0:禁止循环模式1:使能循环模式CHEN位为1时,该位不能被配置</td></tr><tr><td>4</td><td>DIR</td><td>传输方向软件置位和清零0:从外设读出并写入存储器1:从存储器读出并写入外设CHEN位为1时,该位不能被配置</td></tr><tr><td>3</td><td>ERRIE</td><td>通道错误中断使能位软件置位和清零0:禁止通道错误中断1:使能通道错误中断</td></tr><tr><td>2</td><td>HTFIE</td><td>通道半传输完成中断使能位软件置位和清零0:禁止通道半传输完成中断1:使能通道半传输完成中断</td></tr><tr><td>1</td><td>FTFIE</td><td>通道传输完成中断使能位软件置位和清零0:禁止通道传输完成中断1:使能通道传输完成中断</td></tr><tr><td>0</td><td>CHEN</td><td>通道使能软件置位和清零0:禁止该通道1:使能该通道</td></tr></table>

## 4.5.4. 通道 x 计数寄存器 (DMA_CHxCNT)

x = 0...6, x 为通道序号

地址偏移：0x0C + 0x14 × x

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>传输计数CHEN位为1时,该位域不能被配置该寄存器表明还有多少数据等待被传输。一旦通道使能,该寄存器为只读的,并在每个DMA传输之后值减1。如果该寄存器的值为0,无论通道开启与否,都不会有数据传输。如果该通道工作在循环模式下,一旦通道的传输任务完成,该寄存器会被自动重装载为初始设置值。</td></tr></table>

## 4.5.5. 通道 x 外设基地址寄存器 (DMA_CHxPADDR)

<table><tr><td colspan="15">x = 0...6, x为通道序号地址偏移: 0x10 + 0x14 × x复位值: 0x0000 0000</td><td></td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">PADDR[31:16]</td><td></td></tr><tr><td colspan="15">rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">PADDR[15:0]</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PADDR[31:0]</td><td>外设基地址CHEN位为1时,该位域不能被配置当PWIDTH位域的值为01(16-bit),PADDR[0]被忽略,访问自动与16位地址对齐。当PWIDTH位域的值为10(32-bit),PADDR[1:0]被忽略,访问自动与32位地址对齐。</td></tr></table>

## 4.5.6. 通道 x 存储器基地址寄存器 (DMA_CHxMADDR)

<table><tr><td colspan="16">x = 0...6, x为通道序号地址偏移: 0x14 + 0x14 × x复位值: 0x0000 0000</td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>MADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MADDR[31:0]</td><td>存储器基地址CHEN位为1时,该位域不能被配置当MWIDTH位域的值为01 (16-bit)时,MADDR [0]被忽略,访问自动与16位地址对齐。当MWIDTH位域的值为10 (32-bit)时,MADDR [1:0]被忽略,访问自动与32位地址对齐。</td></tr></table>
