# 38.4. EXMC 寄存器

EXMC基地址：0x5200 4000

# 38.4.1. NOR/PSRAM 控制器寄存器

SRAM/NOR Flash 控制寄存器（EXMC_SNCTLx, x=0, 1, 2, 3）

地址偏移：0x00 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0000 30DA

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="2">BKREMAP[1:0]</td><td colspan="3">保留</td><td>CCK</td><td>SYNCWR</td><td colspan="3">CPS[2:0]</td></tr><tr><td colspan="11">rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ASYNCW TEN</td><td>EXMODE N</td><td>NRWTEN</td><td>WEN</td><td>NRWTCF G</td><td>保留</td><td>NRWTPOL</td><td>SBRSTE N</td><td>保留</td><td>NREN</td><td colspan="2">NRW[1:0]</td><td colspan="2">NRTP[1:0]</td><td>NRMUX</td><td>NRBKEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>BKREMAP[1:0]</td><td>Bank 重映射00: 默认映射01: NOR/PSRAM bank 和 SDRAM device0 交换10: 保留11: 保留注意: BKREMAP 位域只在 EXMC_SNCTL0 有效, EXMC_SNCTLx (x = 1, 2, 3)没有意义。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>CCK</td><td>连续时钟配置0: EXMC_CLK 只在同步模式产生1: EXMC_CLK 无条件产生注意: 该位只在 EXMC_SNCTL0 有效, EXMC_SNCTLx (x = 1, 2, 3)没有意义。当该位置为 1 时, 只有 EXMC_SNTCFG0 寄存器的 CKDIV[3:0]可以影响 EXMC_CLK 的输出。</td></tr><tr><td>19</td><td>SYNCWR</td><td>选择写操作模式0: 异步写操作1: 同步写操作</td></tr><tr><td>18:16</td><td>CPS[2:0]</td><td>CRAM 页大小000: 页边界自动突发分割</td></tr></table>

001：128 字节

010：256 字节

011：512 字节

100：1024 字节

其他：保留

15 ASYNCWTEN 异步等待功能使能位

0：禁用异步等待功能

1：使能异步等待功能

14 EXMODEN 扩展模式使能

0：禁用扩展模式，即不使用 EXMC_SNWTCFGx

1：使能扩展模式

13 NRWTEN NWAIT 信号使能

对于存储器的突发模式访问，该位使能/禁用等待状态插入 NWAIT 信号功能。

0：成组传输模式时，禁用 NWAIT 信号

1：成组传输模式时，使能 NWAIT 信号

12 WEN 写操作使能

0：禁止 EXMC 对外部存储器的写操作，否则产生一个 AXI错误

1：允许 EXMC 对外部存储器的写操作（复位缺省值）

11 NRWTCFG NWAIT 信号配置，只在同步模式有效

0：NWAIT 信号在等待状态前的一个数据周期有效

1：NWAIT 信号在等待状态期间有效

10 保留 必须保持复位值。

9 NRWTPOL NWAIT 信号极性

0：NWAIT 低电平有效

1：NWAIT 高电平有效

8 SBRSTEN 同步突发模式使能

0：禁止同步突发模式

1：使能同步突发模式

7 保留 必须保持复位值。

6 NREN NOR Flash 访问使能

0：禁止 NOR Flash 访问

1：允许 NOR Flash 访问

5:4 NRW[1:0] NOR 存储器数据宽度

00：8 位

01：16 位(复位缺省值)

10：32 位

11：保留

3:2 NRTP[1:0] NOR 存储器类型

00：SRAM、ROM 

01：PSRAM（CRAM） 

10：NOR Flash 

11：保留

1 NRMUX NOR 数据线/地址线复用

0：禁用地址/数据复用功能

1：允许地址/数据复用功能

0 NRBKEN NOR 存储块使能

0：禁用对应的存储器块

1：使能对应的存储器块

# SRAM/NOR Flash 时序配置寄存器（EXMC_SNTCFGx, x=0, 1, 2, 3）

地址偏移：0x04 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">ASYNCMOD[1:0]</td><td colspan="4">DLAT[3:0]</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">BUSLAT[3:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DSET[7:0]</td><td colspan="4">AHLD[3:0]</td><td colspan="4">ASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>ASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式(EXMC_SNCTLx 寄存器的 EXMODEN 位为 1)中使用。00: 模式 A01: 模式 B10: 模式 C11: 模式 D</td></tr><tr><td>27:24</td><td>DLAT[3:0]</td><td>NOR Flash 数据延时,仅在同步模式有效0x0: 第一数据的保持时间为 2 个 EXMC_CLK 时钟周期0x1: 第一数据的保持时间为 3 个 EXMC_CLK 时钟周期......0xF: 第一数据的保持时间为 17 个 EXMC_CLK 时钟周期</td></tr><tr><td>23:20</td><td>CKDIV[3:0]</td><td>同步模式时钟分频比,仅在同步模式有效0x0: 无 EXMC_CLK 时钟输出0x1: EXMC_CLK 周期 = 2 * CK_EXMC 周期......</td></tr></table>

0xF：EXMC_CLK 周期 = 16 * CK_EXMC 周期

<table><tr><td>19:16</td><td>BUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间。0x0:总线延迟=0*CK_EXMC周期0x1:总线延迟=1*CK_EXMC周期......0xF:总线延迟=15*CK_EXMC周期</td></tr><tr><td>15:8</td><td>DSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=1*CK_EXMC周期......0xFF:数据建立时间=255*CK_EXMC周期</td></tr><tr><td>7:4</td><td>AHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0:保留0x1:地址保持时间=1*CK_EXMC......0xF:地址保持时间=15*CK_EXMC</td></tr><tr><td>3:0</td><td>ASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在SRAM,ROM,NOR Flash的异步模式有效0x0:地址建立时间=0*CK_EXMC......0xF:地址建立时间=15*CK_EXMC</td></tr></table>

# SRAM/NOR Flash 写时序寄存器（(EXMC_SNWTCFGx, x=0, 1, 2, 3）

地址偏移：0x104 + 8 * x, (x = 0, 1, 2, 3)

复位值：0x0FFF FFFF

该寄存器仅在扩展模式使能（寄存器EXMC_SNCTLx位EXMODEN置1）后有效。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">WASYNMOD[1:0]</td><td colspan="8">保留</td><td colspan="4">WBUSLAT[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">WDSET[7:0]</td><td colspan="4">WAHLD[3:0]</td><td colspan="4">WASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

位/位域 名称 描述

31:30 保留 必须保持复位值。

<table><tr><td>29:28</td><td>WASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式(EXMC_SNCTLx 寄存器的 EXMODEN 位为 1)中使用。00: 模式 A01: 模式 B10: 模式 C11: 模式 D</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>WBUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间。0x0: 总线延迟 = 0 * CK_EXMC 周期0x1: 总线延迟 = 1 * CK_EXMC 周期......0xF: 总线延迟 = 15 * CK_EXMC 周期</td></tr><tr><td>15:8</td><td>WDSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00: 保留0x01: 数据建立时间 = 1 * CK_EXMC 周期......0xFF: 数据建立时间 = 255 * CK_EXMC 周期</td></tr><tr><td>7:4</td><td>WAHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式 D 与复用模式有效0x0: 保留0x1: 地址保持时间 = 1 * CK_EXMC......0xF: 地址保持时间 = 15 * CK_EXMC</td></tr><tr><td>3:0</td><td>WASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在 SRAM,ROM,NOR Flash 的异步模式有效0x0: 地址建立时间 = 0 * CK_EXMC0x1: 地址建立时间 = 1 * CK_EXMC......0xF: 地址建立时间 = 15 * CK_EXMC</td></tr></table>

# 38.4.2. NAND Flash 控制器寄存器

# NAND Flash 控制器寄存器（EXMC_NCTL）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="3">ECCSZ[2:0]</td><td>ART[3]</td><td></td></tr><tr><td colspan="11"></td><td colspan="3">rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">ATR[2:0]</td><td colspan="4">CTR[3:0]</td><td colspan="2">保留</td><td>ECCEN</td><td>NDW[1:0]</td><td>保留</td><td>NDBKEN</td><td>NDWTEN</td><td>保留</td><td></td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:17</td><td>ECCSZ[2:0]</td><td>ECC 块大小000: 256 字节001: 512 字节010: 1024 字节011: 2048 字节100: 4096 字节101: 8192 字节</td></tr><tr><td>16:13</td><td>ATR[3:0]</td><td>ALE 至 RE 延迟0x0: ALE 至 RE 延迟 = 1 * CK_EXMC......0xF: ALE 至 RE 延迟 = 16 * CK_EXMC</td></tr><tr><td>12:9</td><td>CTR[3:0]</td><td>CLE 至 RE 延迟0x0: CLE 至 RE 延迟 = 1 * CK_EXMC0x1: CLE 至 RE 延迟 = 2 * CK_EXMC......0xF: CLE 至 RE 延迟 = 16 * CK_EXMC</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>ECCEN</td><td>ECC 使能0: 关闭 ECC,并复位 EXMC_NECC1: 使能 ECC</td></tr><tr><td>5:4</td><td>NDW[1:0]</td><td>NAND 外部存储器宽度00: 8 位01: 16 位其他: 保留</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>NDBKEN</td><td>NAND 外部存储器使能0: 禁能对应的存储器块1: 使能对应的存储器块</td></tr><tr><td>1</td><td>NDWTEN</td><td>NWAIT 信号使能位0: 关闭等待功能1: 使能等待功能</td></tr></table>\
0 保留 必须保持复位值。

# NAND Flash 中断使能寄存器（EXMC_NINTEN）

地址偏移：0x84

复位值：0x0000 0042

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FFEPT</td><td>INTFEN</td><td>INTHEN</td><td>INTREN</td><td>INTFS</td><td>INTHS</td><td>INTRS</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FFEPT</td><td>FIFO空标志位0:FIFO非空1:FIFO空</td></tr><tr><td>5</td><td>INTFEN</td><td>中断下降沿检测使能0:禁用中断下降沿检测1:使能中断下降沿检测</td></tr><tr><td>4</td><td>INTHEN</td><td>中断高电平检测使能0:禁用中断高电平检测1:使能中断高电平检测</td></tr><tr><td>3</td><td>INTREN</td><td>中断上升沿中断检测使能0:禁用中断上升沿检测1:使能中断上升沿检测</td></tr><tr><td>2</td><td>INTFS</td><td>中断下降沿状态0:没有检测到中断下降沿1:检测到中断下降沿</td></tr><tr><td>1</td><td>INTHS</td><td>中断高电平状态0:没有检测到中断高电平1:检测到中断高电平</td></tr><tr><td>0</td><td>INTRS</td><td>中断上升沿状态0:没有检测到中断上升沿1:检测到中断上升沿</td></tr></table>

# NAND Flash 通用空间时序寄存器（EXMC_NCTCFG）

地址偏移：0x88

复位值：0xFFFF FFFF

这些操作适用于NAND Flash的外部存储器的通用存储空间。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">COMHIZ[7:0]</td><td colspan="8">COMHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">COMWAIT[7:0]</td><td colspan="8">COMSET[7:0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>COMHIZ[7:0]</td><td>通用空间数据总线的高阻时间定义在通用空间进行写操作后数据总线保持高阻态时间0x00: COMHIZ = 1 * CK_EXMC......0xFE: COMHIZ = 255 * CK_EXMC0xFF: 保留</td></tr><tr><td>23:16</td><td>COMHLD[7:0]</td><td>通用空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: COMHLD = 1 * CK_EXMC......0xFE: COMHLD = 254 * CK_EXMC0xFF: 保留</td></tr><tr><td>15:8</td><td>COMWAIT[7:0]</td><td>通用空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: COMWAIT = 2 * CK_EXMC(加上 NWAIT 时钟周期)......0xFE: COMWAIT = 255 * CK_EXMC(加上 NWAIT 时钟周期)0xFF: 保留</td></tr><tr><td>7:0</td><td>COMSET[7:0]</td><td>通用空间的建立时间定义地址信号的建立时间0x00: COMSET = 1 * CK_EXMC......0xFE: COMSET = 255 * CK_EXMC0xFF: 保留</td></tr></table>

# NAND Flash 属性空间时序寄存器（EXMC_NATCFG）

地址偏移：0x8C

复位值：0xFFFF FFFF

如果必须应用其他时序，对于最后地址的写访问，它被用于NAND Flash的属性存储空间的8位访问。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ATTHIZ[7:0]</td><td colspan="8">ATTHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ATTWAIT[7:0]</td><td colspan="8">ATTSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ATTHIZ[7:0]</td><td>属性空间数据总线的高阻时间定义在属性空间进行写操作后数据总线保持高阻态时间0x00: ATTHIZ = 0 * CK_EXMC......0xFE: ATTHIZ = 254 * CK_EXMC0xFF: 保留</td></tr><tr><td>23:16</td><td>ATTHLD[7:0]</td><td>属性空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: ATTHLD = 1 * CK_EXMC......0xFE: ATTHLD = 254 * CK_EXMC0xFF: 保留</td></tr><tr><td>15:8</td><td>ATTWAIT[7:0]</td><td>属性空间的等待时间定义了保持命令的最小时间0x00: 保留0x01: ATTWAIT = 2 * CK_EXMC(加上 NWAIT 时钟周期)......0xFE: ATTWAIT = 255 * CK_EXMC(加上 NWAIT 时钟周期)0xFF: ATTWAIT = 保留</td></tr><tr><td>7:0</td><td>ATTSET[7:0]</td><td>属性空间的建立时间定义地址信号的建立时间0x00: ATTSET = 1 * CK_EXMC......0xFE: ATTSET = 255 * CK_EXMC0xFF: 保留</td></tr></table>

# NAND Flash ECC 寄存器（EXMC_NECC）

地址偏移：0x94

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECC[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECC[15:0]</td></tr></table>


位/位域 名称 描述


<table><tr><td>ECCSZ[2:0]</td><td>NAND Flash 页大小</td><td>ECC位</td></tr><tr><td>0b000</td><td>256</td><td>ECC[21:0]</td></tr><tr><td>0b001</td><td>512</td><td>ECC[23:0]</td></tr><tr><td>0b010</td><td>1024</td><td>ECC[25:0]</td></tr><tr><td>0b011</td><td>2048</td><td>ECC[27:0]</td></tr><tr><td>0b100</td><td>4096</td><td>ECC[29:0]</td></tr><tr><td>0b101</td><td>8192</td><td>ECC[31:0]</td></tr></table>

# 38.4.3. SDRAM 控制器寄存器

# SDRAM 控制寄存器（EXMC_SDCTLx, x=0, 1）

地址偏移：0x140+4*x, (x = 0, 1)

复位值：0x0000 02D0

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SDCLK[2]</td><td colspan="2">PIPED[1:0]</td><td>BRSTRD</td><td colspan="2">SDCLK[1:0]</td><td>WPEN</td><td colspan="2">CL[1:0]</td><td>NBK</td><td colspan="2">SDW[1:0]</td><td colspan="2">RAW[1:0]</td><td colspan="2">CAW[1:0]</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:16</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>15</td><td>SDCLK[2]</td><td>参考 SDCLK[1:0]的描述</td></tr><tr><td>14:13</td><td>PIPED[1:0]</td><td>流水线读数据延迟这些位用于指定在 CAS 延迟之后再延迟多少个 CK_EXMC 时钟周期才去读数据00:延迟 0 个 CK_EXMC 周期01:延迟 1 个 CK_EXMC 周期10:延迟 2 个 CK_EXMC 周期11:保留</td></tr></table>

注意：寄存器 EXMC_SDCTL1 相应位保留

12 BRSTRD 突发读开关

当该位被置位时，会在 CAS 延迟期间预期处理下一个读命令，并将数据存储到读FIFO 中。

0：禁用突发读

1：使能突发读

注意：寄存器 EXMC_SDCTL1 相应位保留

11:10 SDCLK[1:0] SDRAM 时钟配置

这些位指定了两个 SDRAM device 的时钟周期。如果需要修改存储器时钟配置，首先需要将存储器时钟禁用，并且在修改配置后将存储器重新初始化。

000：SDCLK 存储器时钟禁用

001：保留

010：SDCLK 存储器周期 = 2 * CK_EXMC 周期

011：SDCLK 存储器周期 = 3 * CK_EXMC 周期

110：SDCLK 存储器周期 = 4 * CK_EXMC 周期

111：SDCLK 存储器周期 = 5 * CK_EXMC 周期

其他：保留

注意：寄存器 EXMC_SDCTL1 相应位保留

SDCLK[2]位不连续，位于第 15 位。

9 WPEN 写保护

该位禁用写保护功能

0：禁用写保护，允许写访问

1：使能写保护，忽略写访问

8:7 CL[1:0] CAS 延迟

这些位用于设定 SDRAM CAS延迟多少个 SDRAM 存储器时钟周期单元

00：保留不使用

01：1 个周期

10：2 个周期

11：3 个周期

6 NBK 内部 Bank 的个数

该位指定内部 Bank 的个数

0：2 个内部 Bank

1：4 个内部 Bank

5:4 SDW[1:0] SDRAM 数据总线宽度

该位指定 SDRAM 存储器数据总线宽度

00：8 位

01：16 位

10：32 位

11：保留

3:2 RAW[1:0] 行地址位宽

这些位用于指定行地址的比特宽度

00：11 位

01：12 位

10：13 位

11：保留

1:0 CAW[1:0] 

列地址位宽

这些位用于指定列地址的比特宽度

00：8 位

01：9 位

10：10 位

11：11 位

# SDRAM 时序配置寄存器（EXMC_SDTCFGx, x=0, 1）

地址偏移：0x148+4*x, (x = 0, 1)

复位值：0x0FFF FFFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">RCD[3:0]</td><td colspan="4">RPD[3:0]</td><td colspan="4">WRD[3:0]</td></tr><tr><td colspan="4"></td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">ARFD[3:0]</td><td colspan="4">RASD[3:0]</td><td colspan="4">XSRD[3:0]</td><td colspan="4">LMRD[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>27:24</td><td>RCD[3:0]</td><td>行到列的延迟这些位指定了使能命令与读/写命令之间延迟多少 SDRAM 时钟周期单元。0x0: 1个周期.0x1: 2个周期....0xF: 16个周期</td></tr><tr><td>23:20</td><td>RPD[3:0]</td><td>行预充电延迟这些位指定了预充电命令与下一个命令之间延迟多少 SDRAM 存储器时钟周期单元。0x0: 1个周期0x1: 2个周期....0xF: 16个周期注意: 寄存器 EXMC_SDTCFG1 相应位保留, 如果两个 SDRAM 存储器都被使用, RPD 必须用较慢设备的时序来配置。</td></tr><tr><td>19:16</td><td>WRD[3:0]</td><td>写恢复延迟这些位指定写命令和预充电命令之间延迟多少 SDRAM 存储器时钟周期单元。0x0: 1个周期</td></tr></table>

0x1：2 个周期

0xF：16 个周期

注意：寄存器 EXMC_SDTCFG1 相应位保留，如果两个 SDRAM 存储器都被使用，WRD 必须用较慢设备的时序来配置。

15:12 ARFD[3:0] 自动刷新延迟

这些位指定两个连续的刷新命令之间的延迟，在同一个内部 bank 上两个使能命令之间的延迟，以及刷新命令和使能命令之间的延迟，延迟时间以 SDRAM 存储器时钟周期为单位。

0x0：1 个周期

0x1：2 个周期

0xF：16 个周期

注意：寄存器 EXMC_SDTCFG1 相应位保留，如果两个 SDRAM 存储器都被使用，ARFD 必须用较慢设备的时序来配置。

11:8 RASD[3:0] 行地址选择延迟

这些位指定了使能命令与预充电命令之间延迟多少 SDRAM 时钟周期单元，也指定了两个连续的自刷新命令之间的最小延迟。

0x0：1 个周期

0x1：2 个周期

0xF：16 个周期

7:4 XSRD[3:0] 退出自刷新延迟

这些位指定了从自刷新命令到使能命令之间延迟多少个 SDRAM 存储器时钟周期单元。

0x0：1 个周期

0x1：2 个周期

0xF：16 个周期

3:0 LMRD[3:0] 加载模式寄存器延迟

这些位指定加载模式寄存器命令与刷新或使能命令之间延迟多少 SDRAM 存储器时钟周期单元。

0x0：1 个周期

0x1：2 个周期

0xF：16 个周期

# SDRAM 命令寄存器（EXMC_SDCMD）

地址偏移：0x150

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">MRC[12:7]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">MRC[6:0]</td><td colspan="4">NARF[3:0]</td><td>DS0</td><td>DS1</td><td colspan="3">CMD[2:0]</td></tr><tr><td colspan="7">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>21:9</td><td>MRC[12:0]</td><td>模式寄存器内容这些位指定 SDRAM 模式寄存器的内容,这些内容在 CMD = &#x27;100&#x27;时进行编程</td></tr><tr><td>8:5</td><td>NARF[3:0]</td><td>连续的自动刷新个数这些位指定在 CMD = &#x27;011&#x27;时,发出多少个连续自动刷新周期0x0: 1 个自动刷新周期0x1: 2 个自动刷新周期....0xE: 15 个自动刷新周期0xF: 保留</td></tr><tr><td>4</td><td>DS0</td><td>选择 SDRAM Device 0该位指示 SDRAM Device 0 是否被选择0: SDRAM Device 0 没有被选择1: SDRAM Device 0 被选择</td></tr><tr><td>3</td><td>DS1</td><td>选择 SDRAM Device 1该位指示 SDRAM Device 1 是否被选择0: SDRAM Device 1 没有被选择1: SDRAM Device 1 被选择</td></tr><tr><td>2:0</td><td>CMD[2:0]</td><td>命令这些位指定发送到 SDRAM 设备上的命令000: 正常操作模式001: 时钟使能命令010: 所有存储区预充电命令011: 自动刷新命令100: 加载模式寄存器命令101: 自刷新命令110: 掉电模式进入命令111: 保留注意: 发送命令时,至少需要选择一个设备(DS1 或 DS0)。如果两个设备同时使用,必须同时选择两个设备发送命令。</td></tr></table>

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>REIE</td><td colspan="13">ARINTV[12:0]</td><td>REC</td></tr><tr><td colspan="7">rw</td><td colspan="8">rw</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>14</td><td>REIE</td><td>刷新错误中断使能0: 中断禁止1: 状态寄存器 REIF 位置 1 发生中断</td></tr><tr><td>13:1</td><td>ARINTV[12:0]</td><td>自动刷新间隔这些位指定两个连续的自动刷新命令之间间隔多少存储器时钟周期单元。ARFITV = (SDRAM 刷新周期/行数) - 20</td></tr><tr><td>0</td><td>REC</td><td>清除刷新错误标志该位置 1 会清除状态寄存器 REIF 位。0: 没有效果1: 清除刷新错误标志</td></tr></table>

# SDRAM 状态寄存器（EXMC_SDSTAT）

地址偏移：0x158

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>NRDY</td><td colspan="2">STA1[1:0]</td><td colspan="2">STA0[1:0]</td><td>REIF</td></tr><tr><td colspan="10"></td><td>r</td><td colspan="2">r</td><td colspan="2">r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>5</td><td>NRDY</td><td>非就绪状态该位指定 SDRAM 控制器是否已经准备接收一个新的命令0: SDRAM 控制器准备好接收新命令1: SDRAM 控制器没有准备好接收新命令</td></tr><tr><td>4:3</td><td>STA1[1:0]</td><td>Device1 状态</td></tr></table>

该位定义 SDRAM Device1 的状态

00：正常状态

01：自刷新状态

10：掉电状态

2:1 STA0[1:0] 

Device 0 状态

该位定义 SDRAM Device0 的状态

00：正常状态

01：自刷新状态

10：掉电状态

0 REIF 

刷新错误标志

0：无刷新错误

1：出现刷新错误。若中断使能位置 1（RFEIE），则产生中断 REIE

# SDRAM 读采样控制寄存器（EXMC_SDRSCTL）

地址偏移：0x180

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">SDSC[3:0]</td><td colspan="2">保留</td><td>SSCR</td><td>RSEN</td></tr><tr><td colspan="8"></td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>7:4</td><td>SDSC[3:0]</td><td>选择读数据的采样时钟的延迟单元0x0: 0个延迟单元0x1: 1个延迟单元......0xF: 15个延迟单元</td></tr><tr><td>3:2</td><td>保留</td><td>硬件强制清零。</td></tr><tr><td>1</td><td>SSCR</td><td>选择读数据的采样周期0:除延迟之外,为读数据采样时钟增加0个额外的CK_EXMC周期1:除延迟之外,为读数据采样时钟增加1个额外的CK_EXMC周期</td></tr><tr><td>0</td><td>RSEN</td><td>读采样使能0:禁止读采样1:使能读采样</td></tr></table>
