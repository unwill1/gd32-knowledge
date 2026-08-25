# 25.4. EXMC 寄存器

EXMC基地址：0xA000 0000

# 25.4.1. NOR/PSRAM 控制器寄存器

SRAM/NOR Flash 控制寄存器（EXMC_SNCTLx）（x=0, 1, 2, 3）

偏移地址：0x00 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0000 30DA

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>CCK</td><td>SYNCWR</td><td colspan="3">CPS[2:0]</td></tr><tr><td colspan="11"></td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ASYNC</td><td>EXMO</td><td>NRWT</td><td rowspan="2">WEN</td><td>NRWT</td><td rowspan="2">WRAPEN</td><td>NRWT</td><td>SBR</td><td rowspan="2">保留</td><td>NR</td><td rowspan="2" colspan="2">NRW[1:0]</td><td rowspan="2" colspan="2">NRTP[1:0]</td><td>NR</td><td>NRBK</td></tr><tr><td>WTEN</td><td>DEN</td><td>EN</td><td>CFG</td><td>POL</td><td>STEN</td><td>EN</td><td>MUX</td><td>EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>CCK</td><td>连续时钟配置0: EXMC_CLK只在同步模式产生1: EXMC_CLK无条件产生注意:该位只在EXMC_SNCTL0有效, EXMC_SNCTLx (x = 1, 2, 3)没有意义</td></tr><tr><td>19</td><td>SYNCWR</td><td>选择写操作模式0: 异步写操作1: 同步写操作</td></tr><tr><td>18:16</td><td>CPS[2:0]</td><td>CRAM页大小000: 页边界自动突发分割001: 128字节010: 256字节011: 512字节100: 1024字节其他: 保留</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>异步等待功能使能位0: 禁用异步等待功能1: 使能异步等待功能</td></tr><tr><td>14</td><td>EXMODEN</td><td>扩展模式使能0: 禁用扩展模式,即不使用EXMC_SNWTCFGx</td></tr></table>

1：使能扩展模式

13 NRWTEN 

NWAIT信号使能

对于存储器的突发模式访问，该位使能/禁用等待状态插入NWAIT信号功能

0：成组传输模式时，禁用NWAIT信号

1：成组传输模式时，使能NWAIT信号

12 WEN 

写操作使能

0：禁止EXMC对外部存储器的写操作，否则产生一个AHB错误

1：允许EXMC对外部存储器的写操作（复位缺省值）

11 NRWTCFG 

NWAIT信号配置，只在同步模式有效

0：NWAIT信号在等待状态前的一个数据周期有效

1：NWAIT信号在等待状态期间有效

10 WRAPEN 

非对齐成组模式使能

0：禁止非对齐成组操作

1：允许非对齐成组操作

9 NRWTPOL 

NWAIT信号极性

0：NWAIT低电平有效

1：NWAIT高电平有效

8 SBRSTEN 

同步突发模式使能

0：禁止同步突发模式

1：使能同步突发模式

7 保留

必须保持复位值。

6 NREN 

NOR闪存访问使能

0：禁止NOR Flash访问

1：允许NOR Flash访问

5:4 NRW[1:0] 

存储器数据宽度

00：8位

01：16位（复位缺省值）

10/11：保留

3:2 NRTP[1:0] 

存储器类型

00：SRAM、ROM 

01：PSRAM（CRAM） 

10：NOR Flash 

11：保留

1 NRMUX 

数据线/地址线复用

0：禁用地址/数据复用功能

1：允许地址/数据复用功能

0 NRBKEN 存储块使能

0：禁用对应的存储器块

1：使能对应的存储器块

# SRAM/NOR Flash 时序寄存器（EXMC_SNTCFGx）（x=0, 1, 2, 3）

偏移地址：0x04 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">ASYNCMOD[1:0]</td><td colspan="4">DLAT[3:0]</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">BUSLAT[3:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DSET[7:0]</td><td colspan="4">AHLD[3:0]</td><td colspan="4">ASET[3:0]</td></tr><tr><td colspan="2"></td><td colspan="6">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>ASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式中使用00: 模式A01: 模式B10: 模式C11: 模式D</td></tr><tr><td>27:24</td><td>DLAT[3:0]</td><td>NOR Flash数据延时,仅在同步模式有效0x0: 第一数据的保持时间为2个EXMC_CLK时钟周期0x1: 第一数据的保持时间为3个EXMC_CLK时钟周期......0xF: 第一数据的保持时间为17个EXMC_CLK时钟周期</td></tr><tr><td>23:20</td><td>CKDIV[3:0]</td><td>同步模式时钟分频比,仅在同步模式有效0x0: 保留0x1: EXMC_CLK周期=2个HCLK周期......0xF: EXMC_CLK周期=16个HCLK周期</td></tr><tr><td>19:16</td><td>BUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间0x0: 总线延迟=0个HCLK周期0x1: 总线延迟=1个HCLK周期......0xF: 总线延迟=15个HCLK周期</td></tr><tr><td>15:8</td><td>DSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=1个HCLK周期......0xFF:数据建立时间=255个HCLK周期</td></tr><tr><td>7:4</td><td>AHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0:保留0x1:地址保持时间=1个HCLK......0xF:地址保持时间=15个HCLK</td></tr><tr><td>3:0</td><td>ASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在SRAM,ROM,NOR Flash的异步模式有效0x0:地址建立时间=0个HCLK......0xF:地址建立时间=15个HCLK</td></tr></table>

# SRAM/NOR Flash 写时序寄存器（EXMC_SNWTCFGx）（x=0, 1, 2, 3）

偏移地址：0x104 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0FFF FFFF

该寄存器仅在扩展模式使能（寄存器EXMC_SNCTL位EXMODEN置1）后有效。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">WASYNCMOD[1:0]</td><td colspan="8">保留</td><td colspan="4">WBUSLAT[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">WDSET[7:0]</td><td colspan="4">WAHLD[3:0]</td><td colspan="4">WASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>WASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式中使用00: 模式A01: 模式B10: 模式C11: 模式D</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>WBUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间0x0:总线延迟=0个HCLK周期0x1:总线延迟=1个HCLK周期......0xF:总线延迟=15个HCLK周期</td></tr><tr><td>15:8</td><td>WDSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=1个HCLK周期......0xFF:数据建立时间=255个HCLK周期</td></tr><tr><td>7:4</td><td>WAHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0:保留0x1:地址建立时间=1个HCLK......0xF:地址建立时间=15个HCLK</td></tr><tr><td>3:0</td><td>WASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在SRAM,ROM,NOR Flash的异步模式有效0x0:地址建立时间=0个HCLK......0xF:地址建立时间=15个HCLK</td></tr></table>

# 25.4.2. NAND Flash/PC Card 控制器寄存器

NAND Flash/PC Card 控制寄存器（EXMC_NPCTLx）（x=1, 2, 3）

偏移地址：0x40 + 0x20 * x（x = 1, 2, 3）

复位值：0x0000 0008

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="3">ECCSZ[2:0]</td><td>ATR[3]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">ATR[2:0]</td><td colspan="4">CTR[3:0]</td><td colspan="2">保留</td><td>ECCEN</td><td colspan="2">NDW[1:0]</td><td>NDTP</td><td>NDBKEN</td><td>NDWTEN</td><td>保留</td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:17</td><td>ECCSZ[2:0]</td><td>ECC块大小000: 256字节001: 512字节010: 1024字节011: 2048字节100: 4096字节101: 8192字节</td></tr><tr><td>16:13</td><td>ATR[3:0]</td><td>ALE至RE的延迟0x0: 1个HCLK......0xF: 16个HCLK</td></tr><tr><td>12:9</td><td>CTR[3:0]</td><td>CLE至RE的延迟0x0: 1个HCLK0x1: 2个HCLK......0xF: 16个HCLK</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>ECCEN</td><td>ECC使能0: 关闭ECC,并复位EXMC_NECCx1: 打开ECC</td></tr><tr><td>5:4</td><td>NDW[1:0]</td><td>外部存储器数据宽度00: 8位01: 16位其他: 保留注意: 对于PC/CF Card, 数据宽度必须选择16位</td></tr><tr><td>3</td><td>NDTP</td><td>外部存储器的类型0: PC Card, CF Card, PCMCIA1: NAND Flash</td></tr><tr><td>2</td><td>NDBKEN</td><td>存储块使能0: 禁用对应的存储器块1: 使能对应的存储器块</td></tr><tr><td>1</td><td>NDWTEN</td><td>NWAIT信号使能位0: 关闭等待功能1: 使能等待功能</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# NAND Flash/PC Card 中断使能寄存器（EXMC_NPINTENx）（x=1, 2, 3）

偏移地址：0x44 + 0x20 * x（x = 1, 2, 3）

复位值：0x0000 0042 （对于bank1和bank2） 0x0000 0040 （对于bank3）

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FFEPT</td><td>INTFEN</td><td>INTHEN</td><td>INTREN</td><td>INTFS</td><td>INTHS</td><td>INTRS</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FFEPT</td><td>FIFO空标志位0:FIFO非空1:FIFO空</td></tr><tr><td>5</td><td>INTFEN</td><td>中断下降沿检测使能0:禁用中断下降沿检测1:使能中断下降沿检测</td></tr><tr><td>4</td><td>INTHEN</td><td>中断高电平检测使能0:禁用中断高电平检测1:使能中断高电平检测</td></tr><tr><td>3</td><td>INTREN</td><td>中断上升沿中断检测使能0:禁用中断上升沿检测1:使能中断上升沿检测</td></tr><tr><td>2</td><td>INTFS</td><td>中断下降沿状态0:没有检测到中断下降沿1:检测到中断下降沿</td></tr><tr><td>1</td><td>INTHS</td><td>中断高电平状态0:没有检测到中断高电平1:检测到中断高电平</td></tr><tr><td>0</td><td>INTRS</td><td>中断上升沿状态0:没有检测到中断上升沿1:检测到中断上升沿</td></tr></table>

# NAND Flash/PC Card 通用空间时序寄存器（EXMC_NPCTCFGx）（x=1, 2, 3）

偏移地址：0x48 + 0x20 * x（x = 1, 2, 3）

复位值：0xFFFFFFFF

这些操作适用于以下类型的外部存储器的通用存储空间16位的PC Card，CF card和NANDFlash。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">COMHIZ[7:0]</td><td colspan="8">COMHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">COMWAIT[7:0]</td><td colspan="8">COMSET[7:0]</td></tr></table>


rw



rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>COMHIZ[7:0]</td><td>通用空间数据总线的高阻时间定义在通用空间进行写操作后数据总线保持高阻态时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>COMHLD[7:0]</td><td>通用空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr><tr><td>15:8</td><td>COMWAIT[7:0]</td><td>通用空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK(加上NWAIT时钟周期)......0xFE: 255个HCLK(加上NWAIT时钟周期)0xFF: 保留</td></tr><tr><td>7:0</td><td>COMSET[7:0]</td><td>通用空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr></table>

NAND Flash/PC Card 属性空间时序寄存器（EXMC_NPATCFGx）（x=1, 2, 3）

偏移地址：0x4C + 0x20 * x（x = 1, 2, 3）

复位值：0x FFFFFFFF

这些操作适用于以下类型的外部存储器的属性存储空间8位的PC Card和NAND Flash。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ATTHIZ[7:0]</td><td colspan="8">ATTHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ATTWAIT[7:0]</td><td colspan="8">ATTSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ATTHIZ[7:0]</td><td>属性空间数据总线的高阻时间定义在属性空间进行写操作后数据总线保持高阻态时间0x00: 0个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>ATTHLD[7:0]</td><td>属性空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr><tr><td>15:8</td><td>ATTWAIT[7:0]</td><td>属性空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK(加上NWAIT时钟周期)......0xFE: 255个HCLK(加上NWAIT时钟周期)0xFF: 保留</td></tr><tr><td>7:0</td><td>ATTSET[7:0]</td><td>属性空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr></table>

# PC Card I/O 空间时序寄存器（EXMC_PIOTCFG3）

偏移地址：0xB0

复位值：0x FFFFFFFF

<table><tr><td colspan="16">该寄存器只能按字(32位)访问。</td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IOHIZ[7:0]</td><td colspan="8">IOHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IOWAIT[7:0]</td><td colspan="8">IOSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IOHIZ[7:0]</td><td>I/O空间数据总线的高阻时间定义在IO空间进行写操作后数据总线保持高阻态时间0x00: 0个HCLK......0xFF: 255个HCLK</td></tr><tr><td>23:16</td><td>IOHLD[7:0]</td><td>I/O空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFF: 255个HCLK</td></tr><tr><td>15:8</td><td>IOWAIT[7:0]</td><td>I/O空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: 2个HCLK(加上NWAIT时钟周期)......0xFF: 256个HCLK(加上NWAIT时钟周期)</td></tr><tr><td>7:0</td><td>IOSET[7:0]</td><td>I/O空间的建立时间定义地址信号的建立时间0x00: 1个HCLK......0xFF: 256个HCLK</td></tr></table>

# NAND Flash ECC 结果寄存器（EXMC_NECCx）（x=1, 2）

偏移地址：0x54+0x20 * x（x =1, 2）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECC[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

ECC[15:0] 

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ECC[31:0]</td><td>ECC计算结果当ECCSZ[2:0] = 000,页大小为256字节,ECC计算结果存储在ECC[21:0]位域。当ECCSZ[2:0] = 001,页大小为512字节,ECC计算结果存储在ECC[23:0]位域。当ECCSZ[2:0] = 010,页大小为1024字节,ECC计算结果存储在ECC[25:0]位域。当ECCSZ[2:0] = 011,页大小为2048字节,ECC计算结果存储在ECC[27:0]位域。当ECCSZ[2:0] = 100,页大小为4096字节,ECC计算结果存储在ECC[29:0]位域。当ECCSZ[2:0] = 101,页大小为8192字节,ECC计算结果存储在ECC[31:0]位域。</td></tr></table>

# 25.4.3. SDRAM控制器寄存器

# SDRAM 控制寄存器（EXMC_SDCTLx）（x=0, 1）

偏移地址：0x140+4*x（x = 0, 1）

复位值：0x0000 02D0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="2">PIPED[1:0]</td><td>BRSTRD</td><td colspan="2">SDCLK[1:0]</td><td>WPEN</td><td colspan="2">CL[1:0]</td><td>NBK</td><td colspan="2">SDW[1:0]</td><td colspan="2">RAW[1:0]</td><td colspan="2">CAW[1:0]</td></tr><tr><td></td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>硬件强制清零</td></tr><tr><td>14:13</td><td>PIPED[1:0]</td><td>流水线读数据延迟这些位用于指定在CAS延迟之后再延迟多少个HCLK时钟周期才去读数据00:延迟0个HCLK周期01:延迟1个HCLK周期10:延迟2个HCLK周期11:保留注意:寄存器EXMC_SDCTL1相应位保留</td></tr><tr><td>12</td><td>BRSTRD</td><td>突发读开关当该位被置位时,会在CAS延迟期间预期处理下一个读命令,并将数据存储到读FIFO中。0:禁用突发读1:使能突发读</td></tr></table>


注意：寄存器EXMC_SDCTL1相应位保留


<table><tr><td>11:10</td><td>SDCLK[1:0]</td><td>SDRAM时钟配置这些位指定了两个SDRAM device的时钟周期。如果需要修改存储器时钟配置,首先需要将存储器时钟禁用,并且在修改配置后将存储器重新初始化。00: SDCLK存储器时钟禁用01: 保留10: SDCLK存储器周期为2个HCLK11: SDCLK存储器周期为3个HCLK注意: 寄存器EXMC_SDCTL1相应位保留</td></tr><tr><td>9</td><td>WPEN</td><td>写保护该位禁用写保护功能0: 禁用写保护,允许写访问1: 使能写保护,忽略写访问</td></tr><tr><td>8:7</td><td>CL[1:0]</td><td>CAS延迟这些位用于设定SDRAM CAS延迟多少个SDRAM存储器时钟周期单元00: 保留不使用01: 1个周期10: 2个周期11: 3个周期</td></tr><tr><td>6</td><td>NBK</td><td>内部Bank的个数该位指定内部Bank的个数0: 2个内部Banks1: 4个内部Banks</td></tr><tr><td>5:4</td><td>SDW[1:0]</td><td>SDRAM数据总线宽度该位指定SDRAM存储器数据总线宽度00: 8位01: 16位10: 32位11: 保留</td></tr><tr><td>3:2</td><td>RAW[1:0]</td><td>行地址位宽这些位用于指定行地址的比特宽度00: 11位01: 12位10: 13位11: 保留</td></tr><tr><td>1:0</td><td>CAW[1:0]</td><td>列地址位宽这些位用于指定列地址的比特宽度00: 8位01: 9位10: 10位</td></tr></table>

11：11位

# SDRAM 时序寄存器（EXMC_SDTCFGx）（x=0, 1）

偏移地址：0x148+4*x（x = 0, 1）

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">RCD[3:0]</td><td colspan="4">RPD[3:0]</td><td colspan="4">WRD[3:0]</td></tr><tr><td colspan="4"></td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">ARFD[3:0]</td><td colspan="4">RASD[3:0]</td><td colspan="4">XSRD[3:0]</td><td colspan="4">LMRD[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>RCD[3:0]</td><td>行到列的延迟这些位指定了使能命令与读/写命令之间延迟多少SDRAM时钟周期单元0x0: 1个周期0x1: 2个周期....0xF: 16个周期</td></tr><tr><td>23:20</td><td>RPD[3:0]</td><td>行预充电延迟这些位指定了预充电命令与下一个命令之间延迟多少SDRAM存储器时钟周期单元0x0: 1个周期0x1: 2个周期....0xF: 16个周期注意: 寄存器EXMC_SDTCFG1相应位保留,如果两个SDRAM存储器都被使用,RPD必须用较慢设备的时序来配置</td></tr><tr><td>19:16</td><td>WRD[3:0]</td><td>写恢复延迟这些位指定写命令和预充电命令之间延迟多少SDRAM存储器时钟周期单元0x0: 1个周期0x1: 2个周期....0xF: 16个周期注意: 寄存器EXMC_SDTCFG1相应位保留,如果两个SDRAM存储器都被使用,WRD必须用较慢设备的时序来配置</td></tr><tr><td>15:12</td><td>ARFD[3:0]</td><td>自动刷新延迟这些位指定两个连续的刷新命令之间的延迟,在同一个内部bank上两个使能命令之间的延迟,以及刷新命令和使能命令之间的延迟,延迟时间以SDRAM存储器时钟周期为单位0x0:1个周期0x1:2个周期....0xF:16个周期注意:寄存器EXMC_SDTCFG1相应位保留,如果两个SDRAM存储器都被使用,ARFD必须用较慢设备的时序来配置</td></tr><tr><td>11:8</td><td>RASD[3:0]</td><td>行地址选择延迟这些位指定了使能命令与预充电命令之间延迟多少SDRAM时钟周期单元,也指定了两个连续的自刷新命令之间的最小延迟0x0:1个周期0x1:2个周期....0xF:16个周期</td></tr><tr><td>7:4</td><td>XSRD[3:0]</td><td>退出自刷新延迟这些位指定了从自刷新命令到使能命令之间延迟多少个SDRAM存储器时钟周期单元0x0:1个周期0x1:2个周期....0xF:16个周期</td></tr><tr><td>3:0</td><td>LMRD[3:0]</td><td>加载模式寄存器延迟这些位指定加载模式寄存器命令与刷新或使能命令之间延迟多少SDRAM存储器时钟周期单元0x0:1个周期0x1:2个周期....0xF:16个周期</td></tr></table>

# SDRAM 命令寄存器（EXMC_SDCMD）

偏移地址：0x150

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">MRC[12:7]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">MRC[6:0]</td><td colspan="4">NARF[3:0]</td><td>DS0</td><td>DS1</td><td colspan="3">CMD[2:0]</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:9</td><td>MRC[12:0]</td><td>模式寄存器内容这些位指定SDRAM模式寄存器的内容,这些内容在CMD=&quot;100&quot;时进行编程</td></tr><tr><td>8:5</td><td>NARF[3:0]</td><td>连续的自动刷新个数这些位指定在CMD=&quot;011&quot;时,发出多少个连续自动刷新周期0x0:1个自动刷新周期0x1:2个自动刷新周期....0xE:15个自动刷新周期0xF:保留</td></tr><tr><td>4</td><td>DS0</td><td>选择SDRAM device 0该位指示SDRAM device 0是否被选择0:SDRAM device 0没有被选择1:SDRAM device 0被选择</td></tr><tr><td>3</td><td>DS1</td><td>选择SDRAM device 1该位指示SDRAM device 1是否被选择0:SDRAM device 1没有被选择1:SDRAM device 1被选择</td></tr><tr><td>2:0</td><td>CMD[2:0]</td><td>命令这些位指定发送到SDRAM设备上的命令000:正常操作模式001:时钟使能命令010:所有存储区预充电命令011:自动刷新命令100:加载模式寄存器命令101:自刷新命令110:掉电模式进入命令111:保留注意:发送命令时,至少需要选择一个设备(设备0或设备1)。如果两个设备同时使用,必须同时选择两个设备发送命令。</td></tr></table>

# SDRAM 自动刷新间隔寄存器（EXMC_SDARI）

偏移地址：0x154

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>REIE</td><td colspan="13">ARINTV[12:0]</td><td>REC</td></tr><tr><td></td><td>rw</td><td colspan="13">rw</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>REIE</td><td>刷新错误中断使能0: 中断禁止1: 状态寄存器RFE位置1发生中断</td></tr><tr><td>13:1</td><td>ARINTV[12:0]</td><td>自动刷新间隔这些位指定两个连续的自动刷新命令之间间隔多少存储器时钟周期单元ARFITV= (SDRAM刷新周期/行数) -20</td></tr><tr><td>0</td><td>REC</td><td>清除刷新错误标志该位置1会清除状态寄存器REIF位0: 没有效果1: 清除刷新错误标志</td></tr></table>

# SDRAM 状态寄存器（EXMC_SDSTAT）

偏移地址：0x158

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>NRDY</td><td colspan="2">STA1[1:0]</td><td colspan="2">STA0[1:0]</td><td>REIF</td></tr></table>

<table><tr><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>NRDY</td><td>非就绪状态该位指定SDRAM控制器是否已经准备接收一个新的命令0: SDRAM控制器准备好接收新命令1: SDRAM控制器没有准备好接收新命令</td></tr><tr><td>4:3</td><td>STA1[1:0]</td><td>device1 状态该位定义SDRAM device1的状态00: 正常状态01: 自刷新状态</td></tr><tr><td></td><td></td><td>10: 掉电状态</td></tr><tr><td>2:1</td><td>STA0[1:0]</td><td>device 0 状态</td></tr><tr><td></td><td></td><td>该位定义SDRAM device 0的状态</td></tr><tr><td></td><td></td><td>00: 正常状态</td></tr><tr><td></td><td></td><td>01: 自刷新状态</td></tr><tr><td></td><td></td><td>10: 掉电状态</td></tr><tr><td>0</td><td>REIF</td><td>刷新错误标志</td></tr><tr><td></td><td></td><td>0: 无刷新错误</td></tr><tr><td></td><td></td><td>1: 出现刷新错误。若中断使能位置1(REIE),则产生中断。</td></tr></table>

# SDRAM 读采样控制寄存器（EXMC_SDRSCTL）

偏移地址：0x180

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">SDSC[3:0]</td><td colspan="2">保留</td><td>SSCR</td><td>RSEN</td></tr><tr><td colspan="8"></td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>SDSC[3:0]</td><td>选择读数据的采样时钟的延迟单元0x0: 0个延迟单元0x1: 1个延迟单元......0xF: 15个延迟单元</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SSCR</td><td>选择读数据的采样周期0:除延迟之外,为读数据采样时钟增加0个额外的HCLK周期1:除延迟之外,为读数据采样时钟增加1个额外的HCLK周期</td></tr><tr><td>0</td><td>RSEN</td><td>读采样使能0:禁止读采样1:使能读采样</td></tr></table>

# 25.4.4. SQPI-PSRAM 控制器寄存器

# SPI 初始化寄存器（EXMC_SINIT）

偏移地址：0x310

复位值：0x1801 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>POL</td><td colspan="2">IDL[1:0]</td><td colspan="5">ADRBIT[4:0]</td><td colspan="6">保留</td><td colspan="2">CMDBIT[1:0]</td></tr><tr><td>rw</td><td colspan="2">rw</td><td colspan="11">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>POL</td><td>读数据时的采样极性0:上升沿时进行采样(缺省值)1:下降沿时进行采样</td></tr><tr><td>30:29</td><td>IDL[1:0]</td><td>SPI PSRAM ID长度00:64位01:32位10:16位11:8位</td></tr><tr><td>28:24</td><td>ADRBIT[4:0]</td><td>SPI PSRAM地址位数范围由1到26(缺省值为24)0x00:保留0x01:1位地址......0x1A:26位地址0x1B:保留......0x1F:保留</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>CMDBIT[1:0]</td><td>SPI PSRAM命令位数00:4位01:8位(缺省值)10:16位11:保留</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# SPI 读命令寄存器（EXMC_SRCMD）

偏移地址：0x320

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>RDID</td><td colspan="9">保留</td><td colspan="2">RMODE[1:0]</td><td colspan="4">RWAITCYCLE[3:0]</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RCMD[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>RDID</td><td>发送读SPI PSRAM ID的命令,命令码和模式分别通过RCMD和RMODE设置</td></tr><tr><td>30:22</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>21:20</td><td>RMODE[1:0]</td><td>SPI PSRAM读命令模式00:非SPI模式01:SPI模式10:SQPI模式11:QPI模式</td></tr><tr><td>19:16</td><td>RWAITCYCLE[3:0]</td><td>读数据时地址阶段结束后等待的周期数</td></tr><tr><td>15:0</td><td>RCMD[15:0]</td><td>SPI 读命令的命令码CMDBIT不同时,RCMD有效位不同:CMDBIT=00,RCMD[3:0]有效CMDBIT=01,RCMD[7:0]有效CMDBIT=10,RCMD[15:0]有效</td></tr></table>


注意：在向 RDID 位写 1 之前，你必须确保该位已被清除，RDID 置 1 之后，必须等待 RDID 被清除


# SPI 写命令寄存器（EXMC_SWCMD）

偏移地址：0x330

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SC</td><td colspan="9">保留</td><td colspan="2">WMODE[1:0]</td><td colspan="4">WWAITCYCLE[3:0]</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WCMD[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SC</td><td>发送SPI PSRAM没有地址和数据阶段的特殊命令,命令码和模式分别由WCMD和WMODE设置</td></tr><tr><td>30:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>WMODE[1:0]</td><td>SPI PSRAM写命令模式00:非SPI模式01:SPI模式10:SQPI模式11:QPI模式</td></tr><tr><td>19:16</td><td>WWAITCYCLE[3:0]</td><td>写数据时地址阶段结束后等待的周期数</td></tr><tr><td>15:0</td><td>WCMD[15:0]</td><td>SPI 写命令的命令码</td></tr></table>


注意：在向 SC 位写 1 之前，你必须确保该位已被清除，SC 置 1 之后，必须等待 SC 被清除


# SPI ID 低位寄存器（EXMC_SIDL）

偏移地址：0x340

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SIDL[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SIDL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SIDL[31:0]</td><td>ID低位数据当IDL=00或01时,SIDL[31:0]有效当IDL=10时,SIDL[15:0]有效当IDL=11时,SIDL[7:0]有效</td></tr></table>

# SPI ID 高位寄存器（EXMC_SIDH）

偏移地址：0x350

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SIDH[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

SIDH[15:0] 

rw 

位/位域

名称

描述

31:0 

SIDH[63:32] 

ID高位数据

仅在IDL=00时有效
