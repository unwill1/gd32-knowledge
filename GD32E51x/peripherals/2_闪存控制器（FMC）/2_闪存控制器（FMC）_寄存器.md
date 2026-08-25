## 2.4. FMC 寄存器

FMC 基地址：0x4002 2000

## 2.4.1. 等待状态寄存器（FMC_WS）

地址偏移：0x00

复位值：0x0000 0630

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>DCRST</td><td>ICRST</td><td>DCEN</td><td>ICEN</td><td colspan="4">保留</td><td>PFEN</td><td>保留</td><td colspan="3">WSCNT[2:0]</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td></td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>DCRST</td><td>复位 D-cache 高速缓存区。该位仅可在 DCEN 位置 0 时可写。0:无效果1:复位 D-cache 高速缓存区</td></tr><tr><td>11</td><td>ICRST</td><td>复位 I-cache 该位仅可在 ICEN 位置 0 时可写。0:无效果1:复位 I-cache 高速缓存区</td></tr><tr><td>10</td><td>DCEN</td><td>D-cache 高速缓存区使能位0:失能 D-cache 高速缓存区1:使能 D-cache 高速缓存区</td></tr><tr><td>9</td><td>ICEN</td><td>I-cache 高速缓存区使能位0:失能 I-cache 高速缓存区1:使能 I-cache 高速缓存区</td></tr><tr><td>8:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PFEN</td><td>预取功能使能位0:失能预取功能1:使能预取功能</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>WSCNT[2:0]</td><td>等待状态计数寄存器软件置 1 和清 0。000:不增加等待状态001:增加 1 个等待状态</td></tr></table>

010：增加2 个等待状态

011：增加3 个等待状态

100：增加4 个等待状态

101 ~ 111：保留

## 2.4.2. 解锁寄存器（FMC_KEY）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL 解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁 FMC_CTL寄存器。</td></tr></table>

## 2.4.3. 选项字节操作解锁寄存器（FMC_OBKEY）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_CTL选项字节操作解锁寄存器这些位仅能被软件写写解锁值到OBKEY[31:0]解锁FMC_CTL寄存器的选项字节命令。</td></tr></table>

## 2.4.4. 状态寄存器（FMC_STAT）

地址偏移：0x0C

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ENDF</td><td>WPERR</td><td>PGAERR</td><td>PGERR</td><td>保留</td><td>BUSY</td></tr><tr><td colspan="10"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>r</td></tr></table>

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ENDF</td><td>操作结束标志位操作成功执行后,此位被硬件置1。软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>PGAERR</td><td>编程对齐错误标志位当写数据不对齐时,此位被硬件置1。软件写1清0。</td></tr><tr><td>2</td><td>PGERR</td><td>编程错误标志位当被编程区域状态不为0xFFFF时,对闪存编程,此位被硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr></table>

## 2.4.5. 控制寄存器（FMC_CTL）

地址偏移：0x10

复位值：0x0000 0080


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ENDIE</td><td>保留</td><td>ERRIE</td><td>OBWEN</td><td>保留</td><td>LK</td><td>START</td><td>OBER</td><td>OBPG</td><td>保留</td><td>MER</td><td>PER</td><td>PG</td></tr><tr><td colspan="3"></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rs</td><td>rs</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清00:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ERRIE</td><td>出错中断使能位软件置1和清00:无硬件中断产生.1:使能出错中断</td></tr><tr><td>9</td><td>OBWEN</td><td>选项字节擦除/编程使能位当正确的序列写入FMC_OBKEY寄存器,此位由硬件置1。此位可以被软件清0。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>FMC_CTL0寄存器锁定标志位当正确的序列写入FMC_KEY0寄存器,此位由硬件清0。此位可以由软件置1。</td></tr><tr><td>6</td><td>START</td><td>向FMC发送擦除命令位软件置1可以发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>5</td><td>OBER</td><td>选项字节擦除命令位软件置1和清00:无作用1:选项字节擦除命令</td></tr><tr><td>4</td><td>OBPG</td><td>选项字节编程命令位软件置1和清00:无作用1:选项字节编程命令</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>MER</td><td>主存储块整片擦除命令位软件置1和清00:无作用1:主存储块整片擦除命令</td></tr><tr><td>1</td><td>PER</td><td>主存储块页擦除命令位软件置1和清00:无作用1:主存储块页擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清00:无作用1:主存储块编程命令</td></tr></table>


注意：当相应闪存操作完成后，该寄存器需处于复位状态。


## 2.4.6. 地址寄存器（FMC_ADDR）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">W</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除或编程地址该位通过软件设置。ADDR 位是闪存擦除/编程命令的地址</td></tr></table>

## 2.4.7. ECC 控制及状态寄存器（FMC_ECCCS）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCADDR[15:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ECCORIE</td><td>ECCDETIE</td><td colspan="7">保留</td><td>OBECCDET</td><td>OB_ECC</td><td>OTP_ECC</td><td>MF_ECC</td><td>SYS_ECC</td><td>ECCDET</td><td>ECCOR</td></tr><tr><td>rw</td><td>rw</td><td colspan="7"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>ECCADDR[15:0]</td><td>检测到 ECC 错误的双字的偏移地址。错误地址 = 基地址 + ECCADDR[15:0]*8,基地址可以是主闪存,system区,选项字节以及 OTP 的起始地址。主闪存:0 ~ 0x3FFF(128K/8 - 1)选项字节:0 ~ 0x01(16/8 - 1)OTP:0 ~ 0x3F(512/8 - 1)系统存储区域:0 ~ 0x4FF(10K/8 - 1)</td></tr><tr><td>15</td><td>ECCCORIE</td><td>纠正单个位中断使能0:纠正单个位中断失能。1:纠正单个位中断使能。</td></tr><tr><td>14</td><td>ECCDETIE</td><td>检测到双位错误中断使能。</td></tr><tr><td></td><td></td><td>0: 检测到双位错误中断失能1: 检测到双位错误中断使能</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>OBECCDET</td><td>检测到选项字节双位错误标志当加载选项字节到寄存器时检测到ECC错误,该位置1。该位写1清零。0: 在加载选项字节到寄存器时未检测到双位ECC错误1: 在加载选项字节到寄存器时检测到双位ECC错误</td></tr><tr><td>5</td><td>OB_ECC</td><td>如果在读取选项字节时检测到ECC错误,该位置1。ECCADDR会记录出错的选项字节偏移地址。ECCDET位和ECCCOR位表示是可纠正的单个位错误还是不可纠正的双位错误。该位写1清零。0: 在读取选项字节时未检测到ECC错误1: 在读取选项字节时检测到ECC错误</td></tr><tr><td>4</td><td>OTP_ECC</td><td>如果在OTP中检测到ECC错误,该位置1。ECCADDR会记录出错的OTP偏移地址。ECCDET位和ECCCOR位表示是可纠正的单个位错误还是不可纠正的双位错误。该位写1清零。0: 在OTP中未检测到ECC错误。1: 在OTP中检测到ECC错误。</td></tr><tr><td>3</td><td>MF_ECC</td><td>如果在主闪存中检测到ECC错误,该位置1。ECCADDR会记录出错的主闪存偏移地址。ECCDET位和ECCCOR位表示是可纠正的单个位错误还是不可纠正的双位错误。该位写1清零。0: 在主闪存中未检测到ECC错误。1: 在主闪存中检测到ECC错误。</td></tr><tr><td>2</td><td>SYS_ECC</td><td>如果在系统存储中检测到ECC错误,该位置1。ECCADDR会记录出错的系统存储偏移地址。ECCDET位和ECCCOR位表示是可纠正的单个位错误还是不可纠正的双位错误。该位写1清零。0: 在系统存储中未检测到ECC错误。1: 在系统存储中检测到ECC错误。</td></tr><tr><td>1</td><td>ECCDET</td><td>检测到双位错误标志。当检测到双位错误时,该位置1。该位写1清零。0: 未检测到ECC双位错误。1: 检测到ECC双位错误。</td></tr><tr><td>0</td><td>ECCOR</td><td>检测并纠正单个位错误标志该位写1清零。0: 未检测并纠正ECC单个位错误。1: 检测并纠正ECC单个位错误。</td></tr></table>

## 2.4.8. 选项字节状态寄存器（FMC_OBSTAT）

地址偏移：0x1C

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WP[31:0]</td><td>系统复位后保存选项字节块的WP[31:0]部分</td></tr><tr><td>2.4.10.</td><td colspan="2">产品ID寄存器(FMC_PID)</td></tr><tr><td></td><td colspan="2">地址偏移:0x100</td></tr><tr><td></td><td colspan="2">复位值:0xXXXX XXXX</td></tr><tr><td></td><td colspan="2">该寄存器只能按字(32位)访问。</td></tr><tr><td>31</td><td>30</td><td>29 28 27 26 25 24 23 22 21 20 19 18 17 16</td></tr></table>

复位值：0x0XXX XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">DATA[15:6]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">DATA[5:0]</td><td colspan="8">USER[7:0]</td><td>SPC</td><td>OBERR</td></tr><tr><td colspan="6">r</td><td colspan="8">r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:10</td><td>DATA[15:0]</td><td>系统复位后保存选项字节的 DATA[15:0]部分</td></tr><tr><td>9:2</td><td>USER[7:0]</td><td>系统复位后保存选项字节块的 USER 字节</td></tr><tr><td>1</td><td>SPC</td><td>安全保护状态0:未保护1:已保护</td></tr><tr><td>0</td><td>OBERR</td><td>选项字节读错误位当选项字节和它的补字节不匹配时此位由硬件置 1,选项字节被强制设置为 0xFF。</td></tr></table>

## 2.4.9. 擦除/编程保护寄存器（FMC_WP）

地址偏移：0x20

复位值：0xXXXX XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WP[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WP[15:0]</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留ID寄存器该寄存器为只读上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>
