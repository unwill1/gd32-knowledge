## 33.4. EXMC 寄存器

EXMC 基地址：0xA000 0000

## 33.4.1. NOR / PSRAM 控制器寄存器

SRAM / NOR Flash 控制寄存器（EXMC_SNCTLx）（x=0, 1, 2, 3）

偏移地址：0x00 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0000 30DA（Region 0）

复位值：0x0000 30D2（Region 1）

复位值：0x0000 30D2（Region 2）

复位值：0x0000 30D2（Region 3）

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="2">BLSET[1:0]</td><td>WFIFODIS</td><td>CCK</td><td>SYNCWR</td><td colspan="3">CPS[2:0]</td></tr><tr><td colspan="8"></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ASYNCWAIT</td><td>EXMODEN</td><td>NRWTEN</td><td>WEN</td><td>NRWTCFG</td><td>WRAPEN</td><td>NRWTPOL</td><td>SBRSTEN</td><td>保留</td><td>NREN</td><td colspan="2">NRW[1:0]</td><td colspan="2">NRTP[1:0]</td><td>NRMUX</td><td>NRBKEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:22</td><td>BLSET[1:0]</td><td>NBL(字节信号)建立时间00:NBL建立时间从NBL拉低到片选NE拉低为0个AHB时钟周期01:NBL建立时间从NBL拉低到片选NE拉低为1个AHB时钟周期10:NBL建立时间从NBL拉低到片选NE拉低为2个AHB时钟周期11:NBL建立时间从NBL拉低到片选NE拉低为3个AHB时钟周期</td></tr><tr><td>21</td><td>WFIFODIS</td><td>写FIFO禁能该位控制写FIFO功能。0:使能写FIFO(复位默认值)1:禁能写FIFO注意:WFIFODIS位在EXMC_SNCTLx(x=1..3)没有意义。只能在EXMC_SNCTL0寄存器中可以对其使能。</td></tr><tr><td>20</td><td>CCK</td><td>连续时钟配置0: EXMC_CLK只在同步模式产生1: EXMC_CLK无条件产生注意:该位只在EXMC_SNCTL0有效,EXMC_SNCTLx(x=1..3)没有意义。当设置此位时,只有EXMC_SNCTL0 CKDIV[3:0]分频因子可以影响EXMC_CLK输出。</td></tr><tr><td>19</td><td>SYNCWR</td><td>选择写操作模式0:异步写操作1:同步写操作</td></tr><tr><td>18:16</td><td>CPS[2:0]</td><td>CRAM页大小000:页边界自动突发分割001:128字节010:256字节011:512字节100:1024字节其他:保留</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>异步等待功能使能位0:禁用异步等待功能1:使能异步等待功能</td></tr><tr><td>14</td><td>EXMODEN</td><td>扩展模式使能0:禁用扩展模式,即不使用EXMC_SNWTCFGx1:使能扩展模式</td></tr><tr><td>13</td><td>NRWTEN</td><td>NWAIT信号使能对于存储器的突发模式访问,该位使能/禁用等待状态插入NWAIT信号功能0:成组传输模式时,禁用NWAIT信号1:成组传输模式时,使能NWAIT信号</td></tr><tr><td>12</td><td>WEN</td><td>写操作使能0:禁止EXMC对外部存储器的写操作,否则产生一个AHB错误1:允许EXMC对外部存储器的写操作(复位缺省值)</td></tr><tr><td>11</td><td>NRWTCFG</td><td>NWAIT信号配置,只在同步模式有效0:NWAIT信号在等待状态前的一个数据周期有效1:NWAIT信号在等待状态期间有效</td></tr><tr><td>10</td><td>WRAPEN</td><td>非对齐成组模式使能0:禁止非对齐成组操作1:允许非对齐成组操作</td></tr><tr><td>9</td><td>NRWTPOL</td><td>NWAIT信号极性0:NWAIT低电平有效1: NWAIT高电平有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>同步突发模式使能0: 禁止同步突发模式1: 使能同步突发模式</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>NREN</td><td>NOR闪存访问使能0: 禁止NOR Flash访问1: 允许NOR Flash访问</td></tr><tr><td>5:4</td><td>NRW[1:0]</td><td>存储器数据宽度00: 8位01: 16位(复位缺省值)10/11: 保留</td></tr><tr><td>3:2</td><td>NRTP[1:0]</td><td>存储器类型00: SRAM (Region1-Region3的复位缺省值)01: PSRAM (CRAM)10: NOR Flash (Region0的复位缺省值)11: 保留</td></tr><tr><td>1</td><td>NRMUX</td><td>数据线/地址线复用0: 禁用地址/数据复用功能1: 允许地址/数据复用功能</td></tr><tr><td>0</td><td>NRBKEN</td><td>存储块使能0: 禁用对应的存储器块1: 使能对应的存储器块</td></tr></table>

## SRAM / NOR Flash 时序寄存器（EXMC_SNTCFGx）（x=0, 1, 2, 3）

偏移地址：0x04 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0FFF FFFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">ASYNCMOD[1:0]</td><td colspan="4">DLAT[3:0]</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">BUSLAT[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DSET[7:0]位/位域</td><td colspan="4">AHLD[3:0]名称</td><td colspan="4">ASET[3:0]描述</td></tr><tr><td colspan="8">31:30</td><td colspan="4">保留</td><td colspan="4">必须保持复位值。</td></tr><tr><td colspan="8">29:28</td><td colspan="4">ASYNCMOD[1:0]</td><td colspan="4">异步访问模式该位只有在扩展模式中使用00: 模式A01: 模式B10: 模式C11: 模式D</td></tr><tr><td colspan="8">27:24</td><td colspan="4">DLAT[3:0]</td><td colspan="4">NOR Flash数据延时,仅在同步模式有效0x0: 首次突发访问的数据延迟时间为2个EXMC_CLK时钟周期0x1: 首次突发访问的数据延迟时间为3个EXMC_CLK时钟周期......0xE ~ 0xF: 首次突发访问的数据延迟时间为17个EXMC_CLK时钟周期</td></tr><tr><td colspan="8">23:20</td><td colspan="4">CKDIV[3:0]</td><td colspan="4">同步模式时钟分频比,仅在同步模式有效0x0: 保留0x1: EXMC_CLK周期=2个HCLK周期......0xF: EXMC_CLK周期=16个HCLK周期</td></tr><tr><td colspan="8">19:16</td><td colspan="4">BUSLAT[3:0]</td><td colspan="4">总线延迟时间在复用读模式中使用,避免总线冲突,是总线恢复到高阻态的最小时间0x0: 总线延迟=0个HCLK周期0x1: 总线延迟=1个HCLK周期......0xF: 总线延迟=15个HCLK周期</td></tr><tr><td colspan="8">15:8</td><td colspan="4">DSET[7:0]</td><td colspan="4">异步数据建立时间该位域仅在异步模式有效0x00: 保留0x01: 数据建立时间=1个HCLK周期......0xFF: 数据建立时间=255个HCLK周期</td></tr><tr><td colspan="8">7:4</td><td colspan="4">AHLD[3:0]</td><td colspan="4">异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0: 保留0x1: 地址保持时间=1个HCLK......0xF: 地址保持时间=15个HCLK</td></tr><tr><td colspan="8">3:0</td><td colspan="4">ASET[3:0]</td><td colspan="4">异步地址建立时间</td></tr></table>

该位域设置地址建立时间

注意：该位域仅在SRAM,ROM,NOR Flash的异步模式有效

0x0：地址建立时间= 0个HCLK

0xF：地址建立时间= 15个HCLK

## SRAM / NOR Flash 写时序寄存器（EXMC_SNWTCFGx）（x=0, 1, 2, 3）

偏移地址：0x104 + 8 * x（x = 0, 1, 2, 3）

复位值：0x0FFF FFFF

该寄存器仅在扩展模式使能（寄存器 EXMC_SNCTL 位 EXMODEN 置 1）后有效。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">WASYNCMOD[1:0]</td><td colspan="8">保留</td><td colspan="4">WBUSLAT[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">WDSET[7:0]</td><td colspan="4">WAHLD[3:0]</td><td colspan="4">WASET[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>WASYNCMOD[1:0]</td><td>异步访问模式该位只有在扩展模式中使用00: 模式A01: 模式B10: 模式C11: 模式D</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>WBUSLAT[3:0]</td><td>总线延迟时间在每个写事务结束时添加总线延迟,避免总线冲突,是总线恢复到高阻态的最小时间0x0: 总线延迟=0个HCLK周期0x1: 总线延迟=1个HCLK周期......0xF: 总线延迟=15个HCLK周期</td></tr><tr><td>15:8</td><td>WDSET[7:0]</td><td>异步数据建立时间该位域仅在异步模式有效0x00:保留0x01:数据建立时间=1个HCLK周期......0xFF:数据建立时间=255个HCLK周期</td></tr><tr><td>7:4</td><td>WAHLD[3:0]</td><td>异步地址保持时间该位域设置地址保持时间,仅在模式D与复用模式有效0x0:保留0x1:地址建立时间=1个HCLK......0xF:地址建立时间=15个HCLK</td></tr><tr><td>3:0</td><td>WASET[3:0]</td><td>异步地址建立时间该位域设置地址建立时间注意:该位域仅在SRAM,ROM,NOR Flash的异步模式有效0x0:地址建立时间=0个HCLK......0xF:地址建立时间=15个HCLK</td></tr></table>

## SRAM / NOR Flash 状态寄存器（EXMC_SNSTAT）

偏移地址：0x84

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FIFOEPT</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FIFOEPT</td><td>FIFO空标志0:FIFO非空1:FIFO空</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## SRAM / NOR Flash 数据延迟减少寄存器（EXMC_SNLATDECx）（x=0, 1, 2, 3）

偏移地址：0x300 + 4 * x（x = 0, 1, 2, 3）

复位值：0x0000 0000

该寄存器仅在同步模式时有效。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">LATDEC[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>LATDEC[2:0]</td><td>配置NOR Flash的数据延迟的减少值。仅在同步读访问时有效。该字段与DLAT一起用于调整读访问时间。同步读:000:首次突发访问的数据延迟为(DLAT + 3) EXMC_CLK001:首次突发访问的数据延迟为(DLAT + 2) EXMC_CLK010:首次突发访问的数据延迟为(DLAT + 1) EXMC_CLK011:首次突发访问的数据延迟为(DLAT + 0) EXMC_CLK100:首次突发访问的数据延迟为(DLAT - 1) EXMC_CLK101:首次突发访问的数据延迟为(DLAT - 2) EXMC_CLK110:首次突发访问的数据延迟为(DLAT - 3) EXMC_CLK111:首次突发访问的数据延迟为(DLAT - 4) EXMC_CLK注意:例如,如果读模式下的数据延迟需要配置为3个CLK,则DLAT[3:0]应为0b&#x27;0000,LATDEC[2:0]应为0b&#x27;010。</td></tr></table>
