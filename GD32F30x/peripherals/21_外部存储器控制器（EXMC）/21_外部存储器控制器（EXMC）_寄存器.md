## 21.4. EXMC 寄存器

## 21.4.1. NOR/PSRAM 控制器寄存器

## SRAM/NOR Flash 控制寄存器 (EXMC_SNCTLx) (x=0, 1, 2, 3)

偏移地址：0x00 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0000 30DB （对于region0），0x0000 30D2（对于region1、region2和region3）

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td>SYNCWR</td><td colspan="3">CPS[2:0]</td></tr><tr><td colspan="12"></td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ASYNCWAIT</td><td>EXMODEN</td><td>NRWTEN</td><td>WREN</td><td>NRWTCFG</td><td>WRAPEN</td><td>NRWTPOL</td><td>SBRSTEN</td><td>保留</td><td>NREN</td><td colspan="2">NRW[1:0]</td><td colspan="2">NRTP[1:0]</td><td>NRMUX</td><td>NRBKEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>SYNCWR</td><td>选择写操作模式0:异步写操作1:同步写操作</td></tr><tr><td>18:16</td><td>CPS[2:0]</td><td>CRAM页大小000:页边界自动突发分割001:128字节010:256字节011:512字节100:1024字节其他:保留</td></tr><tr><td>15</td><td>ASYNCWAIT</td><td>异步等待功能使能位0:禁用异步等待功能1:使能异步等待功能</td></tr><tr><td>14</td><td>EXMODEN</td><td>扩展模式使能0:禁用扩展模式1:使能扩展模式</td></tr><tr><td>13</td><td>NRWTEN</td><td>NWAIT信号使能对于存储器的突发模式访问,该位使能/禁用等待状态插入NWAIT信号功能0:禁用NWAIT信号</td></tr></table>

1：使能NWAIT信号

12 WREN 写操作使能

0：禁止EXMC对外部存储器的写操作，否则产生一个AHB错误

1：允许EXMC对外部存储器的写操作（复位缺省值）

11 NRWTCFG NWAIT信号配置，只在同步模式有效

$0 { : }$ ：NWAIT信号在等待状态前的一个数据周期有效

1：NWAIT信号在等待状态期间有效

10 WRAPEN 非对齐成组模式使能

$0 { : }$ ：禁止非对齐成组操作

1：允许非对齐成组操作

9 NRWTPOL NWAIT信号极性

$0 { : }$ ：NWAIT低电平有效

1：NWAIT高电平有效

8 SBRSTEN 同步突发模式使能

$0 { : }$ 禁止同步突发模式

1：使能同步突发模式

7 保留 必须保持复位值。 必须保持复位值。

6 NREN NOR闪存访问使能

$0 { : }$ 禁止NOR Flash访问

1：允许NOR Flash访问

5:4 NRW[1:0] 存储器数据宽度

00：8位

01：16位(复位缺省值)

10/11：保留

3:2 NRTP[1:0] 存储器类型

00：SRAM(region1~region3复位之后的默认值)

01：PSRAM（CRAM） 

10：NOR Flash(region0复位之后的默认值)

11：保留

1 NRMUX 数据线/地址线复用

0：禁用地址/数据复用功能

1：允许地址/数据复用功能

0 NRBKEN 存储块使能

$0 { : }$ ：禁用对应的存储器块

1：使能对应的存储器块

SRAM/NOR Flash 时序寄存器 (EXMC_SNTCFGx) (x=0, 1, 2, 3)

偏移地址：0x04 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">ASYNCMOD[1:0]</td><td colspan="4">DLAT[3:0]</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">BUSLAT[3:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DSET[7:0]</td><td colspan="4">AHLD[3:0]</td><td colspan="4">ASET[3:0]</td></tr><tr><td colspan="2"></td><td colspan="6">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>ASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式中使用00: 模式A01: 模式B10: 模式C11: 模式D</td></tr><tr><td>27:24</td><td>DLAT[3:0]</td><td>NOR Flash数据延时,仅在同步模式有效0x0: 第一数据的保持时间为2个EXMC_CLK时钟周期0x1: 第一数据的保持时间为3个EXMC_CLK时钟周期......0xF: 第一数据的保持时间为17个EXMC_CLK时钟周期</td></tr><tr><td>23:20</td><td>CKDIV[3:0]</td><td>同步模式时钟分频比,仅在同步模式有效0x0: 保留0x1: EXMC_CLK周期=2个HCLK周期......0xF: EXMC_CLK周期=16个HCLK周期</td></tr><tr><td>19:16</td><td>BUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间0x0: 总线延迟=1个HCLK周期0x1: 总线延迟=2个HCLK周期......0xF: 总线延迟=16个HCLK周期</td></tr><tr><td>15:8</td><td>DSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00: 保留0x01: 数据建立时间=2个HCLK周期......0xFF: 数据建立时间=256个HCLK周期</td></tr><tr><td>7:4</td><td>AHLD[3:0]</td><td>异步地址保持时间</td></tr></table>

该位域设置地址保持时间，仅在模式D与复用模式有效

0x0：保留

0x1：地址建立时间=2个HCLK

0xF：地址建立时间=16个HCLK

3:0 

ASET[3:0] 

异步地址建立时间

该位域设置地址建立时间

注意：该位域仅在SRAM,ROM,NOR Flash的异步模式有效

0x0：地址建立时间= 1个HCLK

0xF：地址建立时间= 16个HCLK

## SRAM/NOR Flash 写时序寄存器 (EXMC_SNWTCFGx) (x=0, 1, 2, 3)

偏移地址：0x104 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

该寄存器仅在扩展模式使能（寄存器EXMC_SNCTL位EXMODEN置1）后有效。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">WASYNCMOD[1:0]</td><td colspan="8">保留</td><td colspan="4">WBUSLAT[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">WDSET[7:0]</td><td colspan="4">WAHLD[3:0]</td><td colspan="4">WASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

位/位域

名称

描述

31:30 

保留

必须保持复位值。

29:28 

WASYNCMOD[1:0] 

异步访问模式

该位只有在扩展模式中使用

00：模式A

01：模式B

10：模式C

11：模式D

27:20 

保留

必须保持复位值。

19:16 

WBUSLAT[3:0] 

总线延迟时间

在每次写传输结束的时候增加总线延时时间来满足连续传输之间的最小时间。

0x0：总线延迟=1个HCLK周期

0x1：总线延迟=2个HCLK周期

0xF：总线延迟=16个HCLK周期

<table><tr><td>15:8</td><td>WDSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=2个HCLK周期......0xFF:数据建立时间=256个HCLK周期</td></tr><tr><td>7:4</td><td>WAHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0:保留0x1:地址建立时间=2个HCLK......0xF:地址建立时间=16个HCLK</td></tr><tr><td>3:0</td><td>WASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在SRAM,ROM,NOR Flash的异步模式有效0x0:地址建立时间=1个HCLK0x1:地址建立时间=2个HCLK......0xF:地址建立时间=16个HCLK</td></tr></table>

## 21.4.2. NAND Flash/PC Card 控制器寄存器

## NAND Flash/PC Card 控制寄存器 (EXMC_NPCTLx) (x=1, 2, 3)

偏移地址：0x40 + 0x20 * x, (x = 1, 2, 3)

复位值：0x0000 0018

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="3">ECCSZ[2:0]</td><td>ATR[3]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">ATR[2:0]</td><td colspan="4">CTR[3:0]</td><td colspan="2">保留</td><td>ECCEN</td><td colspan="2">NDW[1:0]</td><td>NDTP</td><td>NDBKEN</td><td>NDWTEN</td><td>保留</td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:17</td><td>ECCSZ[2:0]</td><td>ECC块大小000: 256字节001: 512字节010: 1024字节011: 2048字节</td></tr></table>

<table><tr><td></td><td></td><td>100: 4096字节</td></tr><tr><td></td><td></td><td>101: 8192字节</td></tr><tr><td>16:13</td><td>ATR[3:0]</td><td>ALE至RE的延迟</td></tr><tr><td></td><td></td><td>0x0: 1个HCLK</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>0xF: 16个HCLK</td></tr><tr><td>12:9</td><td>CTR[3:0]</td><td>CLE至RE的延迟</td></tr><tr><td></td><td></td><td>0x0: 1个HCLK</td></tr><tr><td></td><td></td><td>0x1: 2个HCLK</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>0xF: 16个HCLK</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>ECCEN</td><td>ECC使能</td></tr><tr><td></td><td></td><td>0: 关闭ECC,并复位EXMC_NECCx</td></tr><tr><td></td><td></td><td>1: 打开ECC</td></tr><tr><td>5:4</td><td>NDW[1:0]</td><td>外部存储器数据宽度</td></tr><tr><td></td><td></td><td>00: 8位</td></tr><tr><td></td><td></td><td>01: 16位</td></tr><tr><td></td><td></td><td>其他: 保留</td></tr><tr><td></td><td></td><td>注意: 对于PC/CF Card, 数据宽度必须选择16位</td></tr><tr><td>3</td><td>NDTP</td><td>外部存储器的类型</td></tr><tr><td></td><td></td><td>0: PC Card, CF Card, PCMCIA</td></tr><tr><td></td><td></td><td>1: NAND Flash</td></tr><tr><td>2</td><td>NDBKEN</td><td>存储块使能</td></tr><tr><td></td><td></td><td>0: 禁用对应的存储器块</td></tr><tr><td></td><td></td><td>1: 使能对应的存储器块</td></tr><tr><td>1</td><td>NDWTEN</td><td>NWAIT信号使能位</td></tr><tr><td></td><td></td><td>0: 关闭等待功能</td></tr><tr><td></td><td></td><td>1: 使能等待功能</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## NAND Flash/PC Card 中断使能寄存器 (EXMC_NPINTENx) (x=1, 2, 3)

偏移地址：0x44 + 0x20 * x, (x = 1, 2, 3)

复位值：0x0000 0042（对于bank1和bank2），0x0000 0043（对于bank3）

该寄存器只能按字（32位）访问。

除了中断控制比特位，该寄存器还包含一个FIFO空状态位，该位主要用于ECC。当写外部存储器时，FIFO可以容纳来自AHB访问的2个字，使得AHB总线可以暂时被释放而用于其他外设。ECC计算是基于从FIFO传递的数据。为了得到正确的ECC值，用户应该在FIFO空状态标志位

为1时才去读ECC寄存器。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FFEPT</td><td>INTFEN</td><td>INTHEN</td><td>INTREN</td><td>INTFS</td><td>INTHS</td><td>INTRS</td></tr><tr><td colspan="9"></td><td>r</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FFEPT</td><td>FIFO空标志位0:FIFO非空1:FIFO空</td></tr><tr><td>5</td><td>INTFEN</td><td>中断下降沿检测使能0:禁用中断下降沿检测1:使能中断下降沿检测</td></tr><tr><td>4</td><td>INTHEN</td><td>中断高电平检测使能0:禁用中断高电平检测1:使能中断高电平检测</td></tr><tr><td>3</td><td>INTREN</td><td>中断上升沿中断检测使能0:禁用中断上升沿检测1:使能中断上升沿检测</td></tr><tr><td>2</td><td>INTFS</td><td>中断下降沿状态0:没有检测到中断下降沿1:检测到中断下降沿</td></tr><tr><td>1</td><td>INTHS</td><td>中断高电平状态0:没有检测到中断高电平1:检测到中断高电平</td></tr><tr><td>0</td><td>INTRS</td><td>中断上升沿状态0:没有检测到中断上升沿1:检测到中断上升沿</td></tr></table>

## NAND Flash/PC Card 通用空间时序寄存器 (EXMC_NPCTCFGx) (x=1, 2, 3)

偏移地址：0x48 + 0x20 * x, (x = 1, 2, 3)

复位值：0xFCFC FCFC

该寄存器只能按字（32位）访问。

这些操作适用于以下类型的外部存储器的通用存储空间16位的PC Card，CF card和NANDFlash。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">COMHIZ[7:0]</td><td colspan="8">COMHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">COMWAIT[7:0]</td><td colspan="8">COMSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>COMHIZ[7:0]</td><td>通用空间数据总线的高阻时间定义在通用空间进行写操作后数据总线保持高阻态时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>COMHLD[7:0]</td><td>通用空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr><tr><td>15:8</td><td>COMWAIT[7:0]</td><td>通用空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK (加上NWAIT时钟周期)......0xFE: 255个HCLK (加上NWAIT时钟周期)0xFF: 保留</td></tr><tr><td>7:0</td><td>COMSET[7:0]</td><td>通用空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr></table>

## NAND Flash/PC Card 属性空间时序寄存器 (EXMC_NPATCFGx) (x=1, 2, 3)

偏移地址：0x4C + 0x20 * x, (x = 1, 2, 3)

复位值：0xFCFC FCFC

该寄存器只能按字（32位）访问。

用于8位访问PC卡的属性空间，或是用另一种时序来对Nand Flash的最后地址进行写操作。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ATTHIZ[7:0]</td><td colspan="8">ATTHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ATTWAIT[7:0]</td><td colspan="8">ATTSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ATTHIZ[7:0]</td><td>属性空间数据总线的高阻时间定义在属性空间进行写操作后数据总线保持高阻态时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>ATTHLD[7:0]</td><td>属性空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr><tr><td>15:8</td><td>ATTWAIT[7:0]</td><td>属性空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK (加上NWAIT时钟周期)......0xFE: 255个HCLK (加上NWAIT时钟周期)0xFF: 保留</td></tr><tr><td>7:0</td><td>ATTSET[7:0]</td><td>属性空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr></table>

## PC Card I/O 空间时序寄存器 (EXMC_PIOTCFG3)

偏移地址：0xB0

复位值：0xFCFC FCFC

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IOHIZ[7:0]</td><td colspan="8">IOHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IOWAIT[7:0]</td><td colspan="8">IOSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IOHIZ[7:0]</td><td>I/O空间数据总线的高阻时间定义在IO空间进行写操作后数据总线保持高阻态时间0x00: 0个HCLK......0xFF: 255个HCLK</td></tr><tr><td>23:16</td><td>IOHLD[7:0]</td><td>I/O空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFF: 255个HCLK</td></tr><tr><td>15:8</td><td>IOWAIT[7:0]</td><td>I/O空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK (加上NWAIT时钟周期)......0xFF: 256个HCLK (加上NWAIT时钟周期)</td></tr><tr><td>7:0</td><td>IOSET[7:0]</td><td>I/O空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFF: 256个HCLK</td></tr></table>

## NAND Flash ECC 结果寄存器 (EXMC_NECCx) (x=1, 2)

偏移地址：0x54+0x20 * x, (x =1, 2 )

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECC[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECC[15:0]</td></tr></table>

位/位域 名称 描述

31:0 

ECC[31:0] 

ECC计算结果

<table><tr><td>ECCSZ[2:0]</td><td>NAND Flash 页大小</td><td>ECC 位</td></tr><tr><td>0b000</td><td>256</td><td>ECC[21:0]</td></tr><tr><td>0b001</td><td>512</td><td>ECC[23:0]</td></tr><tr><td>0b010</td><td>1024</td><td>ECC[25:0]</td></tr><tr><td>0b011</td><td>2048</td><td>ECC[27:0]</td></tr><tr><td>0b100</td><td>4096</td><td>ECC[29:0]</td></tr><tr><td>0b101</td><td>8192</td><td>ECC[31:0]</td></tr></table>
