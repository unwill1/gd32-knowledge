## 2.4. FMC 寄存器

FMC 基地址：0x4002 2000

## 2.4.1. 等待状态寄存器(FMC_WS)

地址偏移：0x00

复位值：0x0004 0600

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>DBGEN</td><td colspan="2">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SLP_MDSEL</td><td>RUN_MDSEL</td><td>DCRST</td><td>ICRST</td><td>DCEN</td><td>ICEN</td><td>PFEN</td><td colspan="4">保留</td><td colspan="4">WSCNT[3: 0]</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>DBGEN</td><td>该位用于软件启用/禁用调试0:禁用调试。1:使能调试。</td></tr><tr><td>17:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>SLP_MDSEL</td><td>在睡眠模式下闪存的运行模式该位用于决定系统进入睡眠模式时,闪存进入掉电模式还是空闲模式0:当系统进入睡眠模式时,闪存仍为空闲模式。1:当系统进入睡眠模式时,闪存进入掉电模式。</td></tr><tr><td>13</td><td>RUN_MDSEL</td><td>在运行模式下闪存的运行模式当系统进入运行模式时,用于确定闪存进入掉电模式还是空闲模式。只有当代码在RAM中运行时,闪存才能置于掉电模式。当置位RUN_MDSEL时,闪存无法访问。这个位被FMC_RUNKEY写保护。0:当系统在运行模式下,闪存仍为空闲模式。1:当系统在运行模式下,闪存进入掉电模式。</td></tr><tr><td>12</td><td>DCRST</td><td>复位数据缓存区。该位仅可在DCEN位置0时可写。0:无效果。1:复位数据缓存区。</td></tr><tr><td>11</td><td>ICRST</td><td>复位指令缓存区。该位仅可在ICEN位置0时可写。0:无效果。1:复位指令缓存区。</td></tr><tr><td>10</td><td>DCEN</td><td>数据缓存区使能位0:失能数据缓存区。1:使能数据缓存区。</td></tr><tr><td>9</td><td>ICEN</td><td>指令缓存区使能位0:失能指令缓存区。1:使能指令缓存区。</td></tr><tr><td>8</td><td>PFEN</td><td>预取功能使能位0:失能预取功能。1:使能预取功能。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:0</td><td>WSCNT[3:0]</td><td>等待状态计数寄存器软件置1和清0。0000:不增加等待状态。0001:增加1个等待状态。0010:增加2个等待状态。0011:增加3个等待状态。0100:增加4个等待状态。...1111:增加15个等待状态。</td></tr></table>

## 2.4.2. 系统运行时闪存的运行模式解锁寄存器(FMC_RUNKEY)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RUN_KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RUN_KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RUN_KEY[31:0]</td><td>RUN_MDSEL 解锁寄存器</td></tr></table>

这些位仅能被软件写。

写解锁值到 RUN_KEY[31:0]来解锁在 FMC_WS 寄存器中的 RUN_MDSEL 位。

RUN_KEY1：0x04152637 

RUN_KEY2：0xFAFBFCFD 

## 2.4.3. 解锁寄存器(FMC_KEY)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL 解锁寄存器这些位仅能被软件写。写解锁值到 KEY[31:0]可以解锁 FMC_CTL 寄存器。</td></tr></table>

## 2.4.4. 选项字节操作解锁寄存器(FMC_OBKEY)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_CTL选项字节操作解锁寄存器这些位仅能被软件写写解锁值到OBKEY[31:0]解锁FMC_CTL寄存器的选项字节命令。</td></tr></table>

OBKEY1：0x0819 2A3B 

OBKEY2：0x4C5D 6E7F 

## 2.4.5. 状态寄存器(FMC_STAT)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BUSY</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OBERR</td><td>RPERR</td><td colspan="6">保留</td><td>PGSERR</td><td>PGMERR</td><td>PGAERR</td><td>WPERR</td><td>PGERR</td><td>保留</td><td>OPRERR</td><td>ENDF</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td colspan="6"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr><tr><td>15</td><td>OBERR</td><td>选项字节读取错误标志位当选项字节与其补充字节不匹配时,该位由硬件置位,并且该选项字节强制设置为0xFF。</td></tr><tr><td>14</td><td>RPERR</td><td>读保护错误标志位当通过CBUS访问的地址被DCRP或SCR保护时,该位由硬件置1。这个位可以通过写入1来清除。0:未发生读保护错误。1:发生读保护错误。</td></tr><tr><td>13:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>PGSERR</td><td>编程顺序错误标志位当编程操作没有将PG位先置1就编程时,该位由硬件置位。由于先前的编程错误导致PGERR,PGMERR,PGAERR或WPERR置1时,该位也置1。该位软件写1清0。0:未发生编程顺序错误。1:发生编程顺序错误。</td></tr><tr><td>6</td><td>PGMERR</td><td>程序大小与错误标志位不匹配。当编程大小为半字/字访问时,该位由硬件置位。唯一正确的编程大小是双字。该位软件写1清0。</td></tr><tr><td>5</td><td>PGAERR</td><td>编程对齐错误标志位当CBUS写入数据未64位对齐时,即要编程的数据不能包含在同一64位闪存行中,该位由硬件置位。该位软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位该位由硬件置位,软件写1清0。0:未发生擦除/编程保护错误。1:发生擦除/编程保护错误。</td></tr><tr><td>3</td><td>PGERR</td><td>编程错误标志位当要编程的闪存双字地址的数据不是0xFFFF FFFF FFFF FFFF时,该位由硬件置1,软件写1清0。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>OPRERR</td><td>操作失败错误标志位如果闪存编程或擦除操作完成不成功,并且使能了错误中断(ERRIE = 1),则该位由硬件置1,软件写1清0。</td></tr><tr><td>0</td><td>ENDF</td><td>操作结束标志位当操作执行成功且使能操作结束中断(ENDIE = 1),此位被硬件置1。软件写1清0。</td></tr></table>

## 2.4.6. 控制寄存器(FMC_CTL)

地址偏移：0x14

复位值：0xC000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td>OBLK</td><td>SCR1</td><td>SCR0</td><td>OBRLD</td><td>RPERRIE</td><td>ERRIE</td><td>ENDIE</td><td colspan="6">保留</td><td>OBSTAR T</td><td>START</td></tr><tr><td>rs</td><td>rs</td><td>rs</td><td>rs</td><td>rc_w1</td><td>rw</td><td>rw</td><td>rw</td><td colspan="6"></td><td>rs</td><td>rs</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MER1</td><td colspan="2">保留</td><td>BKSEL</td><td>保留</td><td colspan="8">PNSEL[7:0]</td><td>MERO</td><td>PER</td><td>PG</td></tr><tr><td colspan="3">rw</td><td colspan="5">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>FMC_CTL 寄存器锁定标志位当正确的序列写入 FMC_KEY 寄存器,此位由硬件清 0。此位可以由软件置 1。</td></tr><tr><td>30</td><td>OBLK</td><td>FMC_OBCTL 锁定标志位如果这个位被置1,FMC_OBCTL寄存器中关于用户选项字节的所有位以及选项字节页都将被锁定。当正确的序列被写入FMC_OBKEY寄存器时,该位被硬件清除。该位可通过软件设置。此位可以由软件置1。</td></tr><tr><td>29</td><td>SCR1</td><td>Bank1安全用户区域使能位该位置1时锁定bank1的安全用户区域。当退出安全用户区域时可以由软件设置,该位只能写一次。在DBS=0的情况下,该位不起作用。0:失能bank1的安全用户区域。1:使能bank1的安全用户区域。</td></tr><tr><td>28</td><td>SCR0</td><td>Bank0安全用户区域使能位该位置1时锁定bank0的安全用户区域。当退出安全用户区域时可以由软件设置,该位只能写一次。0:失能bank0的安全用户区域。1:使能bank0的安全用户区域。</td></tr><tr><td>27</td><td>OBRLD</td><td>选项字节重加载位此位可以由软件置1。0:完成选项字节重加载。1:强制选项字节重加载。注意:1.如果当OBLK置位时,该位无法写入。2.OBSTART置位时,该位无法写入,OBSTART和OBRLD两个同时写,两位都不生效。</td></tr><tr><td>26</td><td>RPERRIE</td><td>读保护错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能读保护错误中断。1:使能读保护错误中断。</td></tr><tr><td>25</td><td>ERRIE</td><td>操作失败错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能操作失败错误中断。1:使能操作失败错误中断。</td></tr><tr><td>24</td><td>ENDIE</td><td>操作结束中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能操作结束中断。1:使能操作结束中断。</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>OBSTART</td><td>发送选项字节更改命令位该位由软件置1,只有当OBLK设置为0时,才向FMC发送选项字节更改命令。当BUSY位被清除时,该位被硬件清除。</td></tr><tr><td>16</td><td>START</td><td>向FMC发送擦除命令位当LK设置为0时,该位才能被软件置1和清0。用于向FMC发送擦除命令。当BUSY位被清除时,该位被硬件清除。当MER0、MER1和PER位均清0,如果START位被置1,可能会出现不可预知的问题,而不会产生任何错误标志。应当禁止这种操作。</td></tr><tr><td>15</td><td>MER1</td><td>Bank1批量擦除选择位当LK设置为0时,该位才能被软件置1和清0。0:无作用。1:选择bank1批量擦除。</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>12</td><td>BKSEL</td><td>选择bank号来进行页擦除DBS=10:选择bank0进行页擦除。1:选择bank1进行页擦除。DBS=0保留,必须保持复位值。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>10:3</td><td>PNSEL[7:0]</td><td>擦除页码选择位这些位用于选择要擦除的页码:00000000:第0页。00000001:第1页。...11111111:第255页。</td></tr><tr><td>2</td><td>MER0</td><td>Bank0批量擦除选择位当LK设置为0时,该位才能被软件置1和清0。0:无作用。1:选择bank0批量擦除。</td></tr><tr><td>1</td><td>PER</td><td>页擦除命令位当LK设置为0时,该位才能被软件置1和清0。0:无作用。1:使能页擦除命令。</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清00:失能主存储块编程命令。1:使能主存储块编程命令。</td></tr></table>

## 2.4.7. ECC 控制与状态寄存器(FMC_ECCCS)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>ECCDET0</td><td>ECCCOR0</td><td>ECCDET1</td><td>ECCCOR1</td><td colspan="3">保留</td><td>ECCCORIE</td><td>保留</td><td>SYS_ECC</td><td>BK_ECC</td><td colspan="2">保留</td><td colspan="3">ECCADDR[18:16]</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td></td><td></td><td>rw</td><td></td><td>r</td><td>r</td><td></td><td></td><td></td><td>r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>ECCDET0</td><td>检测到双位错误标志位DBS=0:当在LSB(bits63:0)检测到两个ECC错误时此位置位。软件写1清0。DBS=1:当检测到两个ECC错误时此位置位。软件写1清0。0:未检测到ECC双位错误。1:检测到ECC双位错误。</td></tr><tr><td>30</td><td>ECCCOR0</td><td>检测并纠正单个位错误标志DBS=0:当在LSB(bits63:0)检测并纠正单个ECC错误时此位置位。软件写1清0。DBS=1:当检测并纠正单个ECC错误时此位置位。软件写1清0。0:未检测并纠正ECC单个位错误。1:检测并纠正ECC单个位错误。</td></tr><tr><td>29</td><td>ECCDET1</td><td>检测到双位错误标志位DBS=0:当在MSB(bits127:64)检测到两个ECC错误时此位置位。软件写1清0。DBS=1:保留,必须保持复位值。0:未检测到ECC双位错误。1:检测到ECC双位错误。</td></tr><tr><td>28</td><td>ECCCOR1</td><td>检测并纠正单个位错误标志DBS=0:当在MSB(bits127:64)检测并纠正单个ECC错误时此位置位。软件写1清0。</td></tr></table>

<table><tr><td colspan="16">地址偏移:0x20复位值:0xXXXX XXXX该寄存器只能按字(32位)访问。</td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td></td><td></td><td>DBS=1:保留,必须保持复位值。0:未检测并纠正ECC单个位错误。1:检测并纠正ECC单个位错误。</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>24</td><td>ECCORIE</td><td>纠正单个位中断使能0:失能纠正单个位中断。1:使能纠正单个位中断。当ECCOR位置1时,此位使能时生成一个中断。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22</td><td>SYS_ECC</td><td>当检测到系统引导装载程序ECC纠错或双位ECC错误时,此位置1。0:未检测到系统引导装载程序中ECC纠错或双位ECC错误。1:检测到系统引导装载程序中ECC纠错或双ECC错误。</td></tr><tr><td>21</td><td>BK_ECC</td><td>ECC错误bank号DBS=1:表示ECC纠错或双ECC纠错发生在哪个bank。0:Bank 01:Bank 1DBS=0:如果SYS_ECC置1,表明系统引导装载程序ECC纠错或双ECC纠错发生在哪个bank。如果SYS_ECC为0,保留,必须保持复位值。</td></tr><tr><td>20:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18:0</td><td>ECCADDR[18:0]</td><td>ECC错误地址DBS=0表示在闪存中发生了ECC纠错或双位ECC错误的地址。DBS=1表示在某一bank中发生了ECC纠错或双位ECC错误的地址。</td></tr></table>

## 2.4.8. 选项字节控制寄存器(FMC_OBCTL)

<table><tr><td colspan="2">保留</td><td colspan="2">NRST_MDSEL[1:0]</td><td>nBOOT0</td><td>nSWBT0</td><td>TCMSRAM_ERS</td><td>SRAM_ECCEN</td><td>nBOOT1</td><td>DBS</td><td>保留</td><td>BB</td><td>保留</td><td>FWDGSPD_STDBY</td><td>FWDGSPD_DPSLP</td><td>nFWDG_HW</td></tr><tr><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FMC_SWP</td><td>保留</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td colspan="2">保留</td><td colspan="2">BOR_TH[1:0]</td><td colspan="8">SPC[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29:28</td><td>NRST_MDSEL[1:0]</td><td>NRST引脚模式选择位.00: NRST引脚配置为复位输入/输出模式。01: NRST引脚上的低电平可以复位系统,内部复位不能驱动NRST引脚。10: NRST引脚功能与普通GPIO相同,只有内部复位。11: NRST引脚配置为复位输入/输出模式。</td></tr><tr><td>27</td><td>nBOOT0</td><td>BOOT0选择位0: BOOT0为1。1: BOOT0为0。</td></tr><tr><td>26</td><td>nSWBT0</td><td>软件BOOT0失能位0: BOOT0取决于选项字节位nBOOT0。1: BOOT0取决于PB8/BOOT0引脚。</td></tr><tr><td>25</td><td>TCMSRAM_ERS</td><td>当系统复位时TCM SRAM擦除失能位0: 系统复位时擦除TCM SRAM。1: 系统复位时不擦除TCM SRAM。</td></tr><tr><td>24</td><td>SRAM_ECCEN</td><td>SRAM与TCM SRAM ECC失能位0: 使能SRAM与TCM SRAM ECC。1: 失能SRAM与TCM SRAM ECC。</td></tr><tr><td>23</td><td>nBOOT1</td><td>Boot1选择位0: BOOT1为1。1: BOOT1为0。与BOOT0共同决定启动模式。</td></tr><tr><td>22</td><td>DBS</td><td>单双bank模式选择位0: 选择单bank模式,128位读取位宽。1: 选择双bank模式,64位读取位宽。该位只能在禁用DCRP时写入。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>20</td><td>BB</td><td>Boot启动bank选择位0:当配置为从主闪存启动时,从bank0启动。1:当配置为从主内存启动时,从bank1启动,若bank1为空则从bank0启动。(或者当bank0,bank1均空且SPC等级不为高时从bootloader启动)。注意:在该位置1前必须先将FMC_SWP位置1。</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>FWDGSPD_STDBY</td><td>当系统处于待机模式时独立看门狗的运行状态0:当系统处于待机模式时独立看门狗暂停运行。1:当系统处于待机模式时独立看门狗继续运行。</td></tr><tr><td>17</td><td>FWDGSPD_DPSLP</td><td>当系统处于深度睡眠模式时独立看门狗的运行状态0:当系统处于深度睡眠模式时独立看门狗暂停运行。1:当系统处于深度睡眠模式时独立看门狗继续运行。</td></tr><tr><td>16</td><td>nFWDG_HW</td><td>软件独立看门狗配置位0:硬件独立看门狗。1:软件独立看门狗。</td></tr><tr><td>15</td><td>FMC_SWP</td><td>FMC存储器映射切换。这些位控制主FLASH存储器的Bank0和Bank1的地址映射切换功能。0:主FLASH存储器的Bank0被映射到地址0x0804 0000,主FLASH存储器的Bank1被映射到地址0x0800 00001:主FLASH存储器的Bank0映射到地址0x0800 0000,主FLASH存储器的Bank1映射到地址0x0804 0000注意:以上地址取决于具体芯片系列的扇区大小。使能BB位后该位不能置0。</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>nRST_STDBY</td><td>选项字节待机复位选择位0:当系统进入待机模式时复位。1:当系统进入待机模式时不复位。</td></tr><tr><td>12</td><td>nRST_DPSLP</td><td>选项字节深度睡眠复位选择位0:当系统进入深度睡眠模式时复位。1:当系统进入深度睡眠模式时不复位。</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9:8</td><td>BOR_TH[1:0]</td><td>选项字节BOR阈值00:BOR功能关闭。01:BOR阈值1。阈值约2.2V。10:BOR阈值2。阈值约2.5V。</td></tr></table>

11：BOR阈值3。阈值约2.8 V。

0xAA：无安全保护。

0xCC：高安全保护。

除 0xAA 或 0xCC 之外任何值：低安全保护。

## 2.4.9. DCRP0 起始地址(FMC_DCRP_SADDR0)

地址偏移：0x24

复位值：0xFFFF XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">DCRP0_SADDR [14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14:0</td><td>DCRP0_SADDR[14:0]</td><td>Bank0 仅执行区域起始地址DBS=1:DCRP0_SADDR包含bank0的仅执行区域起始地址。DBS=0:DCRP0_SADDR包含整个闪存的第1个仅执行区域起始地址。</td></tr></table>

## 2.4.10. DCRP0 结束地址(FMC_DCRP_EADDR0)

地址偏移：0x28

复位值：0xX0FF XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DCRP_E</td><td colspan="15"></td></tr><tr><td>REN</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">DCRP0_EADDR [14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DCRP_EREN</td><td>DCRP 区域配置擦除使能位。该位只能置 1。此位仅能在当 SPC 等级从低保护等级降到无保护等级时清除。0: 当SPC等级从低保护等级降到无保护等级时, DCRP区域不擦除。1: 当 SPC 等级从低保护等级降到无保护等级时, DCRP 区域擦除。</td></tr><tr><td>30:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14:0</td><td>DCRP0_EADDR[14:0]</td><td>Bank0 仅执行区域结束地址DBS=1:DCRP0_EADDR包含bank0的仅执行区域结束地址。DBS=0:DCRP0_EADDR 包含整个闪存的第 1 个仅执行区域结束地址。</td></tr></table>

## 2.4.11. Bank0 擦除/编程保护区域 0 寄存器(FMC_BK0WP0)

地址偏移：0x2C

复位值：0xFEXX FEXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK0WP0_EADDR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK0WP0_SADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>BK0WP0_EADDR[7:0]</td><td>第1个编程/保护区域尾页DBS=1:BK0WP0_EADDR[7:0]包含在bank0的第1个WP区域的尾页。DBS=0:BK0WP0_EADDR[7:0]包含在主存储闪存的第1个WP区域的尾页。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>BK0WP0_SADDR[7:0]</td><td>第1个编程/保护区域首页DBS=1:BK0WP0_SADDR[7:0]包含在bank0的第1个WP区域的首页。DBS=0:</td></tr></table>

BK0WP0_SADDR[7:0]包含在主存储闪存的第1个WP区域的首页。

## 2.4.12. Bank0 擦除/编程保护区域 1 寄存器(FMC_BK0WP1)

地址偏移：0x30

复位值：0xFEXX FEXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK0WP1_EADDR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK0WP1_SADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>BK0WP1_EADDR[7: 0]</td><td>第2个编程/保护区域尾页DBS=1:BK0WP1_EADDR[7:0]包含在bank0的第2个WP区域的尾页。DBS=0:BK0WP1_EADDR[7:0]包含在主存储闪存的第2个WP区域的尾页。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>BK0WP1_SADDR[7: 0]</td><td>第2个编程/保护区域首页DBS=1:BK0WP1_SADDR[7:0]包含在bank0的第2个WP区域的首页。DBS=0:BK0WP1_SADDR[7:0]包含在主存储闪存的第2个WP区域的首页。</td></tr></table>

## 2.4.13. DCRP1 起始地址(FMC_DCRP_SADDR1)

地址偏移：0x44

复位值：0xFFFF XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">2.4.15. Bank1 擦除/编程保护区域 0 寄存器(FMC_BK1WP0)</td><td></td></tr><tr><td></td><td></td><td colspan="13">地址偏移: 0x4C复位值: 0xFEXX FEXX该寄存器只能按字(32位)访问。</td><td></td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>保留</td><td>DCRP1_SADDR [14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14:0</td><td>DCRP1_SADDR[14:0]</td><td>Bank1 仅执行区域起始地址DBS=1:DCRP1_SADDR包含bank1的仅执行区域起始地址。DBS=0:DCRP1_SADDR包含整个闪存的第2个仅执行区域起始地址。</td></tr></table>

## 2.4.14. DCRP1 结束地址(FMC_DCRP_EADDR1)

地址偏移：0x48

复位值：0x00FF XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">DCRP1_EADDR [14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14:0</td><td>DCRP1_EADDR[14:0]</td><td>Bank1 仅执行区域结束地址DBS=1:DCRP1_EADDR包含bank1的仅执行区域结束地址。DBS=0:DCRP1_EADDR 包含整个闪存的第2个仅执行区域结束地址。</td></tr></table>

<table><tr><td colspan="8">保留</td><td colspan="8">BK1WP0_EADDR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK1WP0_SADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>BK1WP0_EADDR[7: 0]</td><td>第3个编程/保护区域尾页DBS=1:BK1WP0_EADDR[7:0]包含在bank1的第1个WP区域的尾页。DBS=0:BK1WP0_EADDR[7:0]包含在主存储闪存的第3个WP区域的尾页。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>BK1WP0_SADDR[7: 0]</td><td>第3个编程/保护区域首页DBS=1:BK1WP0_SADDR[7:0]包含在bank1的第1个WP区域的首页。DBS=0:BK1WP0_SADDR[7:0]包含在主存储闪存的第3个WP区域的首页。</td></tr></table>

## 2.4.16. Bank1 擦除/编程保护区域 1 寄存器(FMC_BK1WP1)

地址偏移：0x50

复位值：0xFEXX FEXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK1WP1_EADDR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">BK1WP1_SADDR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>BK1WP1_EADDR[7:0]</td><td>第4个编程/保护区域尾页DBS=1:BK1WP1_EADDR[7:0]包含在bank1的第2个WP区域的尾页。</td></tr></table>

<table><tr><td></td><td></td><td>DBS=0:</td></tr><tr><td></td><td></td><td>BK1WP1_EADDR[7:0]包含在主存储闪存的第4个WP区域的尾页。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td rowspan="3">7:0</td><td rowspan="3">BK1WP1_SADDR[7:0]</td><td>第4个编程/保护区域首页DBS=1:</td></tr><tr><td>BK1WP1_SADDR[7:0]包含在bank1的第2个WP区域的首页。DBS=0:</td></tr><tr><td>BK1WP1_SADDR[7:0]包含在主存储闪存的第4个WP区域的首页。</td></tr></table>

## 2.4.17. Bank0 安全用户区域寄存器(FMC_BK0SCR)

地址偏移：0x70

复位值：0xFF0X FXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BOOTLK</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">SCR_PAGE_CNT0[8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>BOOTLK</td><td>该位置1时强制从用户闪存启动0:支持闪存,RAM和系统启动。1:只能从主闪存启动。</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8:0</td><td>SCR_PAGE_CNT0[8:0]</td><td>配置bank0安全用户区域的页数安全用户区域从bank0基地址开始。内存大小为SCR_PAGE_CNT0乘以页面大小。该区域仅当SPC等级为无保护时可以修改。</td></tr></table>

## 2.4.18. Bank1 安全用户区域寄存器(FMC_BK1SCR)

地址偏移：0x74

复位值：0xFF00 FXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="9">SCR_PAGE_CNT1 [8:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8:0</td><td>SCR_PAGE_CNT1[8:0]</td><td>配置bank1安全用户区域的页数安全用户区域bank1基地址开始。内存大小为SCR_PAGE_CNT1乘以页面大小。该区域仅当SPC等级为无保护时可以修改。</td></tr></table>

## 2.4.19. 产品 ID 寄存器(FMC_PID)

地址偏移：0x100

复位值：0xXXXX XXXX

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品 ID 寄存器该寄存器为只读该寄存器在生产过程中被一次性编程。</td></tr></table>
