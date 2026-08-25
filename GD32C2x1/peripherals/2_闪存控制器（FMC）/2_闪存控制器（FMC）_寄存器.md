## 2.4. FMC 寄存器

FMC基地址：0x4002 2000

## 2.4.1. 等待状态寄存器（FMC_WS）

地址偏移：0x00

复位值：0x000X 0200 (X值为0b010x)，如果芯片从Bootloade启动，WSCNT会被配置为0b001

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>DBGEN</td><td>保留</td><td>MFPE</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ICRST</td><td>保留</td><td>ICEN</td><td>PFEN</td><td colspan="5">保留</td><td colspan="3">WSCNT[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>DBGEN</td><td>该位用于软件启用/禁用调试0:禁用调试。1:使能调试。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>MFPE</td><td>主闪存已编程或空标志该位用来表示主闪存的第一个位置是否已编程或者为空。0:主闪存已编程1:主闪存为空该位可以通过软件设置和清除</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11</td><td>ICRST</td><td>复位指令缓存区。该位仅在ICEN位置0时可写。0:无效果。1:复位指令缓存区。</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>ICEN</td><td>指令缓存区使能位0:失能指令缓存区。1:使能指令缓存区。</td></tr><tr><td>8</td><td>PFEN</td><td>预取功能使能位0:失能预取功能。1:使能预取功能。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2:0</td><td>WSCNT[2:0]</td><td>等待状态计数器软件置1和清0。000:不增加等待状态001:增加1个等待状态1其它:保留</td></tr></table>

## 2.4.2. 解锁寄存器（FMC_KEY）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL 解锁寄存器这些位仅能被软件写。写连续的解锁值到 KEY[31:0]可以解锁 FMC_CTL 寄存器。</td></tr></table>

## 2.4.3. 选项字节操作解锁寄存器（FMC_OBKEY）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_OBCTL 选项字节操作解锁寄存器这些位仅能被软件写写连续的解锁值到 OBKEY[31:0]解锁 FMC_OBCTL 寄存器。</td></tr></table>

## 2.4.4. 状态寄存器（FMC_STAT）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>FLASH_ECC_EN</td><td>BUSY</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OBERR</td><td>RPERR</td><td colspan="4">保留</td><td>FSTPERR</td><td>保留</td><td>PGSERR</td><td>PGMERR</td><td>PGAERR</td><td>WPERR</td><td>PGERR</td><td>保留</td><td>OPRERR</td><td>ENDF</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td colspan="4"></td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>FLASH_ECC_EN</td><td>当前Flash ECC使能状态:当Flash ECC被启用时,该位为1,否则为0。</td></tr><tr><td>16</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr><tr><td>15</td><td>OBERR</td><td>选项字节读取错误标志位当选项字节与其补充字节不匹配时,该位由硬件置位,并且该选项字节强制设置为0xFF。</td></tr><tr><td>14</td><td>RPERR</td><td>读保护错误标志位当访问的地址被DCRP或SCR保护时,该位由硬件置1。这个位可以通过写入1来清除。0:未发生读保护错误。1:发生读保护错误。</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>9</td><td>FSTPERR</td><td>快速编程错误标志位.当快速编程序列由于错误(对齐、大小、写保护或数据丢失)而中断时,该位由硬件置1。同时设置相应的错误位(PGAERR、PGMERR或WPERR)。该位可以通过写入1来清除。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>PGSERR</td><td>编程顺序错误标志位当编程操作没有将PG位预先置1就编程时,该位将由硬件置位。由于先前的编程错误导致PGERR,PGMERR,PGAERR或WPERR置1时,该位也置1。该位可以由软件写1清0。0:未发生编程顺序错误。1:发生编程顺序错误。</td></tr></table>

该寄存器可以按字节（8位）、半字（16位）和字（32位）访问。

<table><tr><td>6</td><td>PGMERR</td><td>编程大小不匹配错误标志位.当编程的大小为半字/字访问时,该位将由硬件置位。唯一正确的编程大小为双字。该位可以由软件写1清0。</td></tr><tr><td>5</td><td>PGAERR</td><td>编程对齐错误标志位当写入的数据非64位对齐时,即要编程的数据不能包含在同一64位闪存行中,该位将由硬件置位。该位可以由软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位当擦除/编程保护错误发生时,该位由硬件置位,软件写1清0。0:未发生擦除/编程保护错误。1:发生擦除/编程保护错误。</td></tr><tr><td>3</td><td>PGERR</td><td>编程错误标志位当要编程的闪存双字地址的数据不是0xFFFF FFFF FFFF FFFF时,该位由硬件置1,软件写1清0。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>OPRERR</td><td>操作失败错误标志位当闪存编程或擦除操作已完成且不成功时,并且使能了错误中断(ERRIE = 1),则该位将由硬件置1。该位可以由软件写1清0。</td></tr><tr><td>0</td><td>ENDF</td><td>操作结束标志位当闪存编程或擦除操作已完成并成功时,此位将被硬件置1。该位可以由软件写1清0。</td></tr></table>

## 2.4.5. 控制寄存器（FMC_CTL）

地址偏移：0x14

复位值：0xC000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td>OBLK</td><td>保留</td><td>SCR</td><td>OBRLD</td><td>RPERRIE</td><td>ERRIE</td><td>ENDIE</td><td colspan="5">保留</td><td>FSTPG</td><td>OBSTART</td><td>START</td></tr><tr><td>rs</td><td>rs</td><td></td><td>rs</td><td>rc_w1</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rs</td><td>rs</td><td>rs</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td colspan="6">PN[5:0]</td><td>MER</td><td>PER</td><td>PG</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>FMC_CTL 寄存器锁定标志位当正确的序列写入到 FMC_KEY 寄存器时,该位将由硬件清 0。该位可以由软件置 1。</td></tr><tr><td>30</td><td>OBLK</td><td>FMC_OBCTL 寄存器锁定标志位如果该位被置1,FMC_OBCTL寄存器中关于用户选项字节的所有位以及选项字节页都将被锁定。当正确的序列被写入到FMC_OBKEY寄存器时,该位被硬件清0。该位可由软件置1。</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28</td><td>SCR</td><td>安全用户区域使能位该位置1时锁定安全用户区域。当有安全用户区域时可以由软件置1,且该位只能写一次。0:失能安全用户区域。1:使能安全用户区域。该位只能通过软件置1,并通过系统复位清除。</td></tr><tr><td>27</td><td>OBRLD</td><td>选项字节重加载位该位可以由软件置1。0:无影响。1:强制选项字节重加载。注意:如果当OBLK置位时,该位无法写入。</td></tr><tr><td>26</td><td>RPERRIE</td><td>读保护错误中断使能位仅当LK被设置为0时,软件才能设置或清除该位。0:失能读保护错误中断。1:使能读保护错误中断。</td></tr><tr><td>25</td><td>ERRIE</td><td>操作错误中断使能位该位可以由软件置1或清0。0:失能操作失败错误中断。1:使能操作失败错误中断。</td></tr><tr><td>24</td><td>ENDIE</td><td>操作结束中断使能位该位可以由软件置1或清0。0:失能操作结束中断。1:使能操作结束中断。</td></tr><tr><td>23:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>FSTPG</td><td>主闪存快速编程命令位该位可以由软件置1或清0。0:失能快速编程1:使能快速编程</td></tr><tr><td>17</td><td>OBSTART</td><td>发送选项字节更改命令位该位由软件置1,只有当OBLK被设置为0时,才向FMC发送选项字节更改命令。当BUSY位被清除时,该位被硬件清除。</td></tr><tr><td>16</td><td>START</td><td>向FMC发送擦除命令位该位用于向FMC发送擦除命令。当BUSY位被清除时,该位被硬件清除。</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8:3</td><td>PN[5:0]</td><td>擦除页码选择位这些位用于选择要擦除的页码:000000:第0页。000001:第1页。...111111:第63页。</td></tr><tr><td>2</td><td>MER</td><td>主闪存批量擦除指令位该位可以由软件置1或清00:无作用。1:主闪存批量擦除指令。</td></tr><tr><td>1</td><td>PER</td><td>主闪存页擦除指令位该位可以由软件置1或清00:无作用。1:主闪存页擦除指令。</td></tr><tr><td>0</td><td>PG</td><td>主闪存编程命令位该位可以由软件置1或清00:失能主存储块编程命令。1:使能主存储块编程命令。</td></tr></table>

## 2.4.6. ECC 控制及状态寄存器（FMC_ECCCS）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>ECCINJEN</td><td colspan="5">保留</td><td colspan="2">ECCINJDATA[1:0]</td><td colspan="8">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ECCCORIE</td><td>ECCDETI E</td><td colspan="12">保留</td><td>ECCDET</td><td>ECCCOR</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>ECCINJEN</td><td>ECC 故障注入使能0: ECC 故障注入失能。1: ECC 故障注入使能。</td></tr><tr><td>30:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>ECCINJDATA[1:0]</td><td>当 ECCINJEN 为 1 时,通过设置该位域可以控制对闪存进行单个位或者双位错误故障注入。00:无错误故障注入</td></tr></table>

<table><tr><td></td><td></td><td>01: 单个位错误故障注入10: 单个位错误故障注入11: 双位错误故障注入注: 该位域只能用于向闪存数据的 bit0 和 bit1 注入错误。</td></tr><tr><td>23:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ECCORIE</td><td>纠正单个位中断使能0: 纠正单个位中断失能。1: 纠正单个位中断使能。</td></tr><tr><td>14</td><td>ECCDETIE</td><td>检测到双位错误中断使能。0: 检测到双位错误中断失能1: 检测到双位错误中断使能</td></tr><tr><td>13:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>ECCDET</td><td>检测到双位错误标志。当检测到双位错误时,该位置 1。该位写 1 清零。0: 未检测到 ECC 双位错误。1: 检测到 ECC 双位错误。</td></tr><tr><td>0</td><td>ECCOR</td><td>检测并纠正单个位错误标志该位写 1 清零。0: 未检测并纠正 ECC 单个位错误。1: 检测并纠正 ECC 单个位错误。</td></tr></table>

## 2.4.7. ECC 地址寄存器（FMC_ECCADDR）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCADDR[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ECCADDR[31:0]</td><td>ECC 错误地址(64 位对齐)。</td></tr></table>

## 2.4.8. 选项字节控制寄存器（FMC_OBCTL）

地址偏移：0x20

复位值：0xXXXX XXXX。

当FMC_CTL寄存器中的OBRLD位置位或系统重置时，从闪存中加载对应值到该寄存器。


该寄存器可以按字节（8位）、半字（16位）和字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="2">NRST_MDSEL[1:0]</td><td>nBOOT0</td><td>nBOOT1</td><td>SWBT0</td><td>保留</td><td>SRAM_ECCEN</td><td>HXTAL_REMAP</td><td>保留</td><td>nWWDG_HW</td><td colspan="2">保留</td><td>nFWDG_HW</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="2"></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td colspan="2">BORF_TH[1:0]</td><td colspan="2">BORR_TH[1:0]</td><td>BORST_EN</td><td colspan="8">SPC[7:0]</td></tr><tr><td></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="3"></td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>28:27</td><td>NRST_MDSEL[1:0]</td><td>NRST引脚模式选择位00:保留01:NRST引脚上的低电平可以复位系统,内部复位不能驱动NRST引脚。10:NRST引脚功能与普通GPIO相同,只有内部复位。11:NRST引脚配置为复位输入/输出模式。</td></tr><tr><td>26</td><td>nBOOT0</td><td>BOOT0选择位0:BOOT0为1。1:BOOT0为0。</td></tr><tr><td>25</td><td>nBOOT1</td><td>Boot1选择位0:BOOT1为1。1:BOOT1为0。与BOOT0共同决定启动模式。</td></tr><tr><td>24</td><td>SWBT0</td><td>软件BOOT0选择位0:BOOT0取决于PA14/BOOT0引脚。1:BOOT0取决于选项字节位nBOOT0。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22</td><td>SRAM_ECCEN</td><td>SRAMECC失能位0:使能SRAMECC。1:失能SRAMECC。</td></tr><tr><td>21</td><td>HXTAL_REMAP</td><td>HXTAL重映射0:使能重映射。1:失能重映射。当该位被设置为0时,HXTAL时钟源将从PF0-OSC_IN/PF1-OSC_OUT引脚重新映射到PC14-OSCX_IN/PC15-OSCX_OUT。因此,PC14-OSCX_IN/PC15-OSCX_OUT被LXTAL和HXTAL共享,两个时钟源不能同时使用</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19</td><td>nWWDG_HW</td><td>窗口看门狗配置位0: 硬件窗口看门狗。1: 软件窗口看门狗。</td></tr><tr><td>18:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>nFWDG_HW</td><td>独立看门狗配置位0: 硬件独立看门狗。1: 软件独立看门狗。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>nRST_STDBY</td><td>选项字节待机复位选择位0: 进入待机模式时产生复位1: 进入待机模式时不产生复位</td></tr><tr><td>13</td><td>nRST_DPSLP</td><td>选项字节深度睡眠复位选择位0: 进入深度睡眠模式时产生复位1: 进入深度睡眠模式时不产生复位</td></tr><tr><td>12:11</td><td>BORF_TH[1:0]</td><td>VDD供电下降时的BOR阈值VDD下降超过这个阈值会激活复位信号。00: BOR下降等级1, 阈值在2.0V左右01: BOR下降等级2, 阈值在2.2V左右10: BOR下降等级3, 阈值在2.5V左右11: BOR下降等级4, 阈值在2.8V左右注:BORR_TH低于BORF_TH的配置组合都属于非法配置。非法配置情况下,BORR_TH和BORF_TH被强制设置为默认值0b11</td></tr><tr><td>10:9</td><td>BORR_TH[1:0]</td><td>VDD供电上升时的BOR阈值VDD上升超过这个阈值会激活复位信号。00: BOR上升等级1, 阈值在2.1V左右01: BOR上升等级2, 阈值在2.3V左右10: BOR上升等级3, 阈值在2.6V左右11: BOR上升等级4, 阈值在2.9V左右注:BORR_TH低于BORF_TH的配置组合都属于非法配置。非法配置情况下,BORR_TH和BORF_TH被强制设置为默认值0b11</td></tr><tr><td>8</td><td>BORST_EN</td><td>电压波动复位使能位0: 电压波动复位失能, 上电复位由POR/PDR级别定义1: 电压波动复位使能, 阈值参考BORR_TH和BORF_TH</td></tr><tr><td>7:0</td><td>SPC[7:0]</td><td>安全保护等级选项字节状态位0xA5: 无安全保护。0xCC: 高安全保护等级, 芯片读保护启用。除0xA5或0xCC之外任何值: 低安全保护等级, 存储区保护启用。</td></tr></table>

## 2.4.9. DCRP0 起始地址寄存器（FMC_DCRP_SADDR0）

地址偏移：0x24

复位值：0x0000 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">DCRP0_SADDR[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:0</td><td>DCRP0_SADDR[6:0]</td><td>DCRP0 起始地址偏移DCRP0_SADDR 包含了 DCRP0 的第一个子页的地址偏移量。</td></tr></table>

## 2.4.10. DCRP0 结束地址寄存器（FMC_DCRP_EADDR0）

地址偏移：0x28

复位值：0xX000 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DCRP_E</td><td colspan="15"></td></tr><tr><td>REN</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">DCRP0_EADDR[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DCRP_EREN</td><td>DCRP 区域擦除使能位。0: 当FMC_OBCTL寄存器中SPC的等级从低保护等级降到无保护等级时, DCRP区域不擦除。1: 当 FMC_OBCTL 寄存器中 SPC 的等级从低保护等级降到无保护等级时, DCRP区域擦除。</td></tr><tr><td>30:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:0</td><td>DCRP0_EADDR[6:0]</td><td>DCRP0 结束地址偏移DCRP0_EADDR包含了DCRP0的最后一个子页的地址偏移量。</td></tr></table>

## 2.4.11. 擦除/编程保护区域 0寄存器（FMC_WP0）

地址偏移：0x2C

复位值：0x00XX 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP0_EADDR[5:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP0_SADDR[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21:16</td><td>WP0_EADDR[5:0]</td><td>擦除/编程保护区域0结束地址偏移WP0_EADDR包含擦除/编程保护区域0的最后一页</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:0</td><td>WP0_SADDR[5:0]</td><td>擦除/编程保护区域0起始地址偏移WP0_SADDR包含擦除/编程保护区域0的第一页</td></tr></table>

## 2.4.12. 擦除/编程保护区域 1寄存器（FMC_WP1）

地址偏移：0x30

复位值：0x00XX 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP1_EADDR[5:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP1_SADDR[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21:16</td><td>WP1_EADDR[5:0]</td><td>擦除/编程保护区域1结束地址偏移WP1_EADDR包含擦除/编程保护区域1的最后一页</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:0</td><td>WP1_SADDR[5:0]</td><td>擦除/编程保护区域1起始地址偏移WP1_SADDR包含擦除/编程保护区域1的第一页</td></tr></table>

## 2.4.13. DCRP1 起始地址寄存器（FMC_DCRP_SADDR1）

地址偏移：0x34

复位值：0x0000 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">DCRP1_SADDR[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:0</td><td>DCRP1_SADDR[6:0]</td><td>DCRP1 起始地址偏移DCRP1_SADDR包含了DCRP1的第一个子页的地址偏移量。</td></tr></table>

## 2.4.14. DCRP1 结束地址寄存器（FMC_DCRP_EADDR1）

地址偏移：0x38

复位值：0x0000 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">DCRP1_EADDR[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:0</td><td>DCRP1_EADDR[6:0]</td><td>DCRP1 结束地址偏移DCRP1_EADDR包含了DCRP1的最后一个子页的地址偏移量。</td></tr></table>

## 2.4.15. 安全用户区域寄存器（FMC_SCR）

地址偏移：0x80

复位值：0x000X 00XX

该寄存器只能按（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BOOTLK</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="7">SCR_PAGE_CNT[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>BOOTLK</td><td>该位置1时强制从用户闪存启动0:支持闪存,RAM和系统启动。1:只能从主闪存启动。</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:0</td><td>SCR_PAGE_CNT[6:0]</td><td>配置安全用户区域的页数安全用户区域从基地址0x0800 0000开始。大小为SCR_PAGE_CNT乘以页大小。注意:该区域仅当OB_SPC等级为无保护时才可以修改。</td></tr></table>

## 2.4.16. 产品 ID 寄存器（FMC_PID）

地址偏移：0x120

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留 ID 寄存器该寄存器为只读上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>
