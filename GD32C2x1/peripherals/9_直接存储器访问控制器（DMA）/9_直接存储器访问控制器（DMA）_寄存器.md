## 9.5. DMA 寄存器

DMA 基地址：0x4002 0000

## 9.5.1. 中断标志位寄存器（DMA_INTF）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ERRIF2</td><td>HTFIF2</td><td>FTFIF2</td><td>GIF2</td><td>ERRIF1</td><td>HTFIF1</td><td>FTFIF1</td><td>GIF1</td><td>ERRIF0</td><td>HTFIF0</td><td>FTFIF0</td><td>GIF0</td></tr><tr><td colspan="4"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11/7/3</td><td>ERRIFx</td><td>通道x错误标志位(x=0...2)硬件置位,软件写DMA_INTC相应位为1清零0:通道x未发生传输错误1:通道x发生传输错误</td></tr><tr><td>10/6/2</td><td>HTFIFx</td><td>通道x半传输完成标志位(x=0...2)硬件置位,软件写DMA_INTC相应位为1清零0:通道x半传输未完成1:通道x半传输完成</td></tr><tr><td>9/5/1</td><td>FTFIFx</td><td>通道x传输完成标志位(x=0...2)硬件置位,软件写DMA_INTC相应位为1清零0:通道x传输未完成1:通道x传输完成</td></tr><tr><td>8/4/0</td><td>GIFx</td><td>通道x全局中断标志位(x=0...2)硬件置位,软件写DMA_INTC相应位为1清零0:通道xERRIF,HTFIF或FTFIF标志位未置位1:通道x至少发生ERRIF,HTFIF或FTFIF之一置位</td></tr></table>

## 9.5.2. 中断标志位清除寄存器（DMA_INTC）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ERRIFC2</td><td>HTFIC2</td><td>FTFIFC2</td><td>GIFC2</td><td>ERRIFC1</td><td>HTFIFC1</td><td>FTFIFC1</td><td>GIFC1</td><td>ERRIFC0</td><td>HTFIFC0</td><td>FTFIFC0</td><td>GIFC0</td></tr><tr><td colspan="4"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11/7/3</td><td>ERRIFCx</td><td>清除通道x(x=0...2)的错误标志位0:无影响1:清零DMA_INTF寄存器的ERRIFx位</td></tr><tr><td>10/6/2</td><td>HTFIFCx</td><td>清除通道x(x=0...2)的半传输完成标志位0:无影响1:清零DMA_INTF寄存器的HTFIFx位</td></tr><tr><td>9/5/1</td><td>FTFIFCx</td><td>清除通道x(x=0...2)的传输完成标志位0:无影响1:清零DMA_INTF寄存器的FTFIFx位</td></tr><tr><td>8/4/0</td><td>GIFCx</td><td>清除通道x(x=0...2)的全局中断标志位0:无影响1:清零DMA_INTF寄存器的GIFx,ERRIFx,HTFIFx和FTFIFx位</td></tr></table>

## 9.5.3. 通道 x 控制寄存器（DMA_CHxCTL）

x = 0…2，x 为通道序号

地址偏移： $0 { \times } 0 8 + 0 { \times } 1 4 ^ { \star } \times$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>M2M</td><td colspan="2">PRIO[1:0]</td><td colspan="2">MWIDTH[1:0]</td><td colspan="2">PWIDTH[1:0]</td><td>MNAGA</td><td>PNAGA</td><td>CMEN</td><td>DIR</td><td>ERRIE</td><td>HTFIE</td><td>FTFIE</td><td>CHEN</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>M2M</td><td>存储器到存储器模式软件置位和清零0:禁止存储器到存储器模式1:使能存储器到存储器模式</td></tr></table>

<table><tr><td></td><td></td><td>CHEN位为1时,该位不能被配置</td></tr><tr><td rowspan="7">13:12</td><td rowspan="7">PRIO[1:0]</td><td>软件优先级</td></tr><tr><td>软件置位和清零</td></tr><tr><td>00:低</td></tr><tr><td>01:中</td></tr><tr><td>10:高</td></tr><tr><td>11:极高</td></tr><tr><td>CHEN位为1时,该位域不能被配置</td></tr><tr><td rowspan="7">11:10</td><td rowspan="7">MWIDTH[1:0]</td><td>存储器的传输数据宽度</td></tr><tr><td>软件置位和清零</td></tr><tr><td>00:8-bit</td></tr><tr><td>01:16-bit</td></tr><tr><td>10:32-bit</td></tr><tr><td>11:保留</td></tr><tr><td>CHEN位为1时,该位域不能被配置</td></tr><tr><td rowspan="7">9:8</td><td rowspan="7">PWIDTH[1:0]</td><td>外设的传输数据宽度</td></tr><tr><td>软件置位和清零</td></tr><tr><td>00:8-bit</td></tr><tr><td>01:16-bit</td></tr><tr><td>10:32-bit</td></tr><tr><td>11:保留</td></tr><tr><td>CHEN位为1时,该位域不能被配置</td></tr><tr><td rowspan="5">7</td><td rowspan="5">MNAGA</td><td>存储器的地址生成算法</td></tr><tr><td>软件置位和清零</td></tr><tr><td>0:固定地址模式</td></tr><tr><td>1:增量地址模式</td></tr><tr><td>CHEN位为1时,该位不能被配置</td></tr><tr><td rowspan="5">6</td><td rowspan="5">PNAGA</td><td>外设的地址生成算法</td></tr><tr><td>软件置位和清零</td></tr><tr><td>0:固定地址模式</td></tr><tr><td>1:增量地址模式</td></tr><tr><td>CHEN位为1时,该位不能被配置</td></tr><tr><td rowspan="5">5</td><td rowspan="5">CMEN</td><td>循环模式使能</td></tr><tr><td>软件置位和清零</td></tr><tr><td>0:禁止循环模式</td></tr><tr><td>1:使能循环模式</td></tr><tr><td>CHEN位为1时,该位不能被配置</td></tr><tr><td rowspan="4">4</td><td rowspan="4">DIR</td><td>传输方向</td></tr><tr><td>软件置位和清零</td></tr><tr><td>0:从外设读出并写入存储器</td></tr><tr><td>1:从存储器读出并写入外设</td></tr></table>

<table><tr><td></td><td></td><td>CHEN位为1时,该位不能被配置</td></tr><tr><td>3</td><td>ERRIE</td><td>通道错误中断使能位软件置位和清零0:禁止通道错误中断1:使能通道错误中断</td></tr><tr><td>2</td><td>HTFIE</td><td>通道半传输完成中断使能位软件置位和清零0:禁止通道半传输完成中断1:使能通道半传输完成中断</td></tr><tr><td>1</td><td>FTFIE</td><td>通道传输完成中断使能位软件置位和清零0:禁止通道传输完成中断1:使能通道传输完成中断</td></tr><tr><td>0</td><td>CHEN</td><td>通道使能软件置位和清零0:禁止该通道1:使能该通道</td></tr></table>

## 9.5.4. 通道 x 计数寄存器（DMA_CHxCNT）

x = 0…2，x 为通道序号

地址偏移：0x0C + 0x14 * x

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>传输计数CHEN位为1时,该位域不能被配置该寄存器表明还有多少数据等待被传输。一旦通道使能,该寄存器为只读的,并在每个DMA传输之后值减1。如果该寄存器的值为0,无论通道开启与否,都不会有数据传输。如果该通道工作在循环模式下,一旦通道的传输任务完成,该寄存器会被自动重装载为初始设置值。</td></tr></table>

## 9.5.5. 通道 x 外设基地址寄存器（DMA_CHxPADDR）

$\times = 0 . . . 2 $ ，x 为通道序号

地址偏移： $0 { \times } 1 0 + 0 { \times } 1 4 ^ { \star } \times$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PADDR[31:0]</td><td>外设基地址CHEN位为1时,该位域不能被配置当PWIDTH位域的值为01(16-bit),PADDR[0]被忽略,访问自动与16位地址对齐。当PWIDTH位域的值为10(32-bit),PADDR[1:0]被忽略,访问自动与32位地址对齐。</td></tr></table>

## 9.5.6. 通道 x 存储器基地址寄存器（DMA_CHxMADDR）

x = 0…2，x 为通道序号

地址偏移： $0 { \times } 1 4 + 0 { \times } 1 4 ^ { \star } \times$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MADDR[31:0]</td><td>存储器基地址CHEN位为1时,该位域不能被配置当MWIDTH位域的值为01(16-bit)时,MADDR[0]被忽略,访问自动与16位地址对齐。当MWIDTH位域的值为10(32-bit)时,MADDR[1:0]被忽略,访问自动与32位地址对齐。</td></tr></table>
