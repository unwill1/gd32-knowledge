## 28.4. EXMC 寄存器

## 28.4.1. NOR/PSRAM 控制器寄存器

## PSRAM/NOR Flash 控制寄存器 (EXMC_PNCTL)

偏移地址：0x00

复位值：0x0000 30DB（对于 region0）

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td>SYNCWR</td><td colspan="3">CPS[2:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ASYNCWAIT</td><td>保留</td><td>NRWTEN</td><td>WREN</td><td>NRWTCFG</td><td>WRAPEN</td><td>NRWTPOL</td><td>SBRSTEN</td><td>保留</td><td>NREN</td><td colspan="2">NRW[1:0]</td><td colspan="2">NRTP[1:0]</td><td>NRMUX</td><td>NRBKEN</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31:20</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>19</td><td colspan="4">SYNCWR</td><td colspan="11">选择写操作模式0:异步写操作1:同步写操作</td></tr><tr><td>18:16</td><td colspan="4">CPS[2:0]</td><td colspan="11">CRAM页大小000:页边界自动突发分割001:128字节010:256字节011:512字节100:1024字节其他:保留</td></tr><tr><td>15</td><td colspan="4">ASYNCWAIT</td><td colspan="11">异步等待功能使能位0:禁用异步等待功能1:使能异步等待功能</td></tr><tr><td>14</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>13</td><td colspan="4">NRWTEN</td><td colspan="11">NWAIT信号使能对于存储器的突发模式访问,该位使能/禁用等待状态插入NWAIT信号功能0:禁用NWAIT信号</td></tr></table>

## 1：使能NWAIT信号

<table><tr><td>12</td><td>WREN</td><td>写操作使能0:禁止EXMC对外部存储器的写操作,否则产生一个AHB错误1:允许EXMC对外部存储器的写操作(复位缺省值)</td></tr><tr><td>11</td><td>NRWTCFG</td><td>NWAIT信号配置,只在同步模式有效0:NWAIT信号在等待状态前的一个数据周期有效1:NWAIT信号在等待状态期间有效</td></tr><tr><td>10</td><td>WRAPEN</td><td>非对齐成组模式使能0:禁止非对齐成组操作1:允许非对齐成组操作</td></tr><tr><td>9</td><td>NRWTPOL</td><td>NWAIT信号极性0:NWAIT低电平有效1:NWAIT高电平有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>同步突发模式使能0:禁止同步突发模式1:使能同步突发模式</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>NREN</td><td>NOR闪存访问使能0:禁止NOR Flash访问1:允许NOR Flash访问</td></tr><tr><td>5:4</td><td>NRW[1:0]</td><td>存储器数据宽度00:8位01:16位(复位缺省值)10/11:保留</td></tr><tr><td>3:2</td><td>NRTP[1:0]</td><td>存储器类型00:保留01:PSRAM(CRAM)10:NOR Flash(region0复位之后的默认值)11:保留</td></tr><tr><td>1</td><td>NRMUX</td><td>数据线/地址线复用0:禁用地址/数据复用功能1:允许地址/数据复用功能</td></tr><tr><td>0</td><td>NRBKEN</td><td>存储块使能0:禁用对应的存储器块1:使能对应的存储器块</td></tr></table>

## PSRAM/NOR Flash 时序寄存器 (EXMC_PNTCFG)

偏移地址：0x04

复位值：0x0FFF FFFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">DLAT[3:0]</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">BUSLAT[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DSET[7:0]</td><td colspan="4">AHLD[3:0]</td><td colspan="4">ASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>DLAT[3:0]</td><td>NOR Flash数据延时,仅在同步模式有效0x0:第一数据的保持时间为2个EXMC_CLK时钟周期0x1:第一数据的保持时间为3个EXMC_CLK时钟周期......0xF:第一数据的保持时间为17个EXMC_CLK时钟周期</td></tr><tr><td>23:20</td><td>CKDIV[3:0]</td><td>同步模式时钟分频比,仅在同步模式有效0x0:保留0x1:EXMC_CLK周期=2个HCLK周期......0xF:EXMC_CLK周期=16个HCLK周期</td></tr><tr><td>19:16</td><td>BUSLAT[3:0]</td><td>总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间0x0:总线延迟=1个HCLK周期0x1:总线延迟=2个HCLK周期......0xF:总线延迟=16个HCLK周期</td></tr><tr><td>15:8</td><td>DSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=2个HCLK周期......0xFF:数据建立时间=256个HCLK周期</td></tr><tr><td>7:4</td><td>AHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在复用模式有效</td></tr></table>

<table><tr><td></td><td></td><td>0x0:保留</td></tr><tr><td></td><td></td><td>0x1:地址建立时间=2个HCLK</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>0xF:地址建立时间=16个HCLK</td></tr><tr><td>3:0</td><td>ASET[3:0]</td><td>异步地址建立时间</td></tr><tr><td></td><td></td><td>该位域设置地址建立时间</td></tr><tr><td></td><td></td><td>注意:该位域仅在NOR Flash的异步模式有效</td></tr><tr><td></td><td></td><td>0x0:地址建立时间=1个HCLK</td></tr><tr><td></td><td></td><td>......</td></tr><tr><td></td><td></td><td>0xF:地址建立时间=16个HCLK</td></tr></table>

## 28.4.2. NAND Flash 控制器寄存器

## NAND Flash 控制寄存器 (EXMC_NCTL)

偏移地址：0x60

复位值：0x0000 0018

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="3">ECCSZ[2:0]</td><td>ATR[3]</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">ATR[2:0]</td><td colspan="4">CTR[3:0]</td><td colspan="2">保留</td><td>ECCEN</td><td colspan="2">NDW[1:0]</td><td>NDTP</td><td>NDBKEN</td><td>NDWTEN</td><td>保留</td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2"></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:17</td><td>ECCSZ[2:0]</td><td>ECC块大小000: 256字节001: 512字节010: 1024字节011: 2048字节100: 4096字节101: 8192字节</td></tr><tr><td>16:13</td><td>ATR[3:0]</td><td>ALE至RE的延迟0x0: 1个HCLK......0xF: 16个HCLK</td></tr></table>

<table><tr><td>12:9</td><td>CTR[3:0]</td><td>CLE至RE的延迟0x0: 1个HCLK0x1: 2个HCLK......0xF: 16个HCLK</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>ECCEN</td><td>ECC使能0: 关闭ECC,并复位EXMC_NECCx1: 打开ECC</td></tr><tr><td>5:4</td><td>NDW[1:0]</td><td>外部存储器数据宽度00: 8位01: 16位其他: 保留</td></tr><tr><td>3</td><td>NDTP</td><td>外部存储器的类型0: 保留1: NAND Flash</td></tr><tr><td>2</td><td>NDBKEN</td><td>存储块使能0: 禁用对应的存储器块1: 使能对应的存储器块</td></tr><tr><td>1</td><td>NDWTEN</td><td>NWAIT信号使能位0: 关闭等待功能1: 使能等待功能</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## NAND Flash 状态寄存器 (EXMC_NSTAT)

偏移地址：0x64

复位值：0x0000 0042（对于 bank1）

该寄存器只能按字（32 位）访问。

该寄存器包含一个 FIFO 空状态位，该位主要用于 ECC。当写外部存储器时，FIFO 可以容纳来自AHB 访问的 2 个字，使得 AHB 总线可以暂时被释放而用于其他外设。ECC 计算是基于从 FIFO传递的数据。为了得到正确的 ECC 值，用户应该在 FIFO 空状态标志位为 1 时才去读 ECC 寄存器。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FFEPT</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FFEPT</td><td>FIFO空标志位0:FIFO非空1:FIFO空</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## NAND Flash 通用空间时序寄存器 (EXMC_NCTCFG)

偏移地址：0x68

复位值：0xFCFC FCFC

该寄存器只能按字（32 位）访问。

这些操作适用于以下类型的外部存储器的通用存储空间 16 位的 NAND Flash。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">COMHIZ[7:0]</td><td colspan="8">COMHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">COMWAIT[7:0]</td><td colspan="8">COMSET[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>COMHIZ[7:0]</td><td>通用空间数据总线的高阻时间定义在通用空间进行写操作后数据总线保持高阻态时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>COMHLD[7:0]</td><td>通用空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK......0xFE: 254个HCLK0xFF: 保留</td></tr></table>

<table><tr><td>15:8</td><td>COMWAIT[7:0]</td><td>通用空间的等待时间定义了保持命令的最小时间0x00:保留0x01:2个HCLK(加上NWAIT时钟周期)......0xFE:255个HCLK(加上NWAIT时钟周期)0xFF:保留</td></tr><tr><td>7:0</td><td>COMSET[7:0]</td><td>通用空间的建立时间定义地址信号的建立时间0x00:1个HCLK......0xFE:255个HCLK0xFF:保留</td></tr></table>

## NAND Flash 属性空间时序寄存器 (EXMC_NATCFG)

偏移地址：0x6C

复位值：0xFCFC FCFC

该寄存器只能按字（32 位）访问。

用于对 NAND Flash 属性存储空间的 8 位访问，适用于最后一个地址或命令写入访问，如果需要应用其他时序。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ATTHIZ[7:0]</td><td colspan="8">ATTHLD[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ATTWAIT[7:0]</td><td colspan="8">ATTSET[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ATTHIZ[7:0]</td><td>属性空间数据总线的高阻时间定义在属性空间进行写操作后数据总线保持高阻态时间0x00: 1个HCLK......0xFE: 255个HCLK0xFF: 保留</td></tr><tr><td>23:16</td><td>ATTHLD[7:0]</td><td>属性空间的保持时间在发送地址后的地址保持时间,在写操作时,也作为数据信号保持的时间0x00: 保留0x01: 1个HCLK</td></tr></table>

15:8 ATTWAIT[7:0] 属性空间的等待时间定义了保持命令的最小时间0x00：保留0x01：2个HCLK (加上NWAIT时钟周期)0xFE：255个HCLK (加上NWAIT时钟周期)0xFF：保留

7:0 ATTSET[7:0] 属性空间的建立时间定义地址信号的建立时间0x00：1个HCLK0xFE：255个HCLK0xFF：保留

## NAND Flash ECC 结果寄存器 (EXMC_NECC)

偏移地址：0x74

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECC[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td colspan="3">描述</td></tr><tr><td>31:0</td><td>ECC[31:0]</td><td colspan="3">ECC计算结果</td></tr><tr><td></td><td></td><td>ECCSZ[2:0]</td><td>NAND Flash 页大小</td><td>ECC 位</td></tr><tr><td></td><td></td><td>0b000</td><td>256</td><td>ECC[21:0]</td></tr><tr><td></td><td></td><td>0b001</td><td>512</td><td>ECC[23:0]</td></tr><tr><td></td><td></td><td>0b010</td><td>1024</td><td>ECC[25:0]</td></tr><tr><td></td><td></td><td>0b011</td><td>2048</td><td>ECC[27:0]</td></tr><tr><td></td><td></td><td>0b100</td><td>4096</td><td>ECC[29:0]</td></tr><tr><td></td><td></td><td>0b101</td><td>8192</td><td>ECC[31:0]</td></tr></table>

