## 3.4. FMC 寄存器

FMC 基地址：0x4002 3C00

## 3.4.1. 解锁寄存器（FMC_KEY）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁 FMC_CTL寄存器。</td></tr></table>

## 3.4.2. 选项字节解锁寄存器（FMC_OBKEY）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_OBCTLx选项字节解锁寄存器这些位仅能被软件写写解锁值到OBKEY[31:0]解锁FMC_OBCTLx寄存器的选项字节命令</td></tr></table>

## 3.4.3. 状态寄存器（FMC_STAT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BUSY</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>RDCERR</td><td>PGSERR</td><td>PGMERR</td><td>PGAERR</td><td>WPERR</td><td>保留</td><td>LDECCDET</td><td>OPERR</td><td>END</td></tr><tr><td colspan="7"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BUSY</td><td>闪存忙标志位当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>RDCERR</td><td>CBUS读保护错误标志位在CBUS读保护扇区进行CBUS读操作时,该位由硬件置位。软件写1清0。</td></tr><tr><td>7</td><td>PGSERR</td><td>编程顺序错误标志位当FMC_CTL寄存器中PG位未置位时进行闪存编程,该位由硬件置位。软件写1清0。</td></tr><tr><td>6</td><td>PGMERR</td><td>编程类型不匹配错误标志位当编程写入数据类型(字/半字/字节访问)与FMC_CTL寄存器中PSZ位不匹配时,该位由硬件置位。软件写1清0。</td></tr><tr><td>5</td><td>PGAERR</td><td>编程对齐错误标志双字编程下当CBUS写数据或地址不对齐时,此位被硬件置1。软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>LDECCDET</td><td>加载代码时检测到双位ECC错误标志位检测到双位错误时硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>OPERR</td><td>闪存操作错误标志位该位由硬件置位,当FMC_CTL寄存器中ERRIE位被置位时闪存操作发生错误(当RDCERR/PGSERR/PGMERR/WPERR位被置位时表示错误发生)。软件写1清0。</td></tr><tr><td>0</td><td>END</td><td>操作结束标志位当操作执行成功,此位被硬件置1。软件写1清0。</td></tr></table>

## 3.4.4. 控制寄存器（FMC_CTL）

地址偏移：0x10

复位值：0x8000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td>RLBE</td><td>NWLDE</td><td colspan="2">保留</td><td>LDECCIE</td><td>ERRIE</td><td>ENDIE</td><td colspan="7">保留</td><td>START</td></tr><tr><td>rs</td><td>w</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="7"></td><td>rs</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MER1</td><td colspan="3">保留</td><td>SN[5]</td><td>DWPGE</td><td colspan="2">PSZ[1:0]</td><td colspan="5">SN[4:0]</td><td>MER0</td><td>SER</td><td>PG</td></tr><tr><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>FMC_CTL锁定当向FMC_KEY寄存器中写入正确的顺序,该位由硬件清除。软件置1。</td></tr><tr><td>30</td><td>RLBE</td><td>使能OTP2读锁定块。只能软件置1使能读锁定。软件一旦置1,读锁定块对应的数据块无法被读。复位后恢复复位值。</td></tr><tr><td>29</td><td>NWLDE</td><td>系统复位后使能零等待区加载。仅电源复位后恢复复位值。0:系统复位后不拷贝闪存内容到缓冲区。1:系统复位后拷贝闪存内容到缓冲区。JTAG调试下不支持。</td></tr><tr><td>28:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>LDECCIE</td><td>代码加载ECC错误中断使能位软件置1和清00:无硬件中断产生1:使能错误中断</td></tr><tr><td>25</td><td>ERRIE</td><td>错误中断使能位软件置1和清00:无硬件中断产生1:使能错误中断</td></tr><tr><td>24</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清00:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>START</td><td>发送擦除命令位该位由软件置位,发送擦除命令到FMC。该位当BUSY位清零时由硬件清零。</td></tr><tr><td>15</td><td>MER1</td><td>主存储闪存bank1整片擦除命令位软件置1和清00:无影响1:主存储闪存bank1整片擦除命令</td></tr></table>

<table><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>SN[5]</td><td>参考SN[4:0].</td></tr><tr><td>10</td><td>DWPGE</td><td>使能双字编程0:非双字编程,参考PSZ[1:0]1:双字编程</td></tr><tr><td>9:8</td><td>PSZ[1:0]</td><td>编程大小位软件置1和清000:按字节编程访问01:按半字编程访问10/11:按字编程访问</td></tr><tr><td>7:3</td><td>SN[4:0]</td><td>选择擦除扇区号软件置1和清0000000:选择扇区0000001:选择扇区1...110100:选择扇区52110101:选择扇区53110110~111111:保留</td></tr><tr><td>2</td><td>MER0</td><td>主存储块bank0整片擦除命令位软件置1和清00:无作用1:主存储块bank0整片擦除命令</td></tr><tr><td>1</td><td>SER</td><td>主存储块扇区擦除命令位软件置1和清00:无作用1:主存储块扇区擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清00:无作用1:主存储块编程命令</td></tr></table>


注意：当相应闪存操作完成后，该寄存器需处于复位状态。


## 3.4.5. 选项字节控制寄存器 0（FMC_OBCTL0）

地址偏移：0x14

复位值：0xXXXX XXXX，初始值为 0x3FFF AAED。复位后装载选项字节中的值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DRP</td><td>保留</td><td>NWA</td><td>ECCEN</td><td colspan="12">WP0[11:0]</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="10">rw</td><td colspan="12"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td colspan="2"></td></tr><tr><td colspan="3"></td><td colspan="5">SPC[7:0]</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td>nWDG_HW</td><td>BB</td><td>BOR_TH[1:0]</td><td>OB_START</td><td colspan="2">OB_LK</td></tr><tr><td colspan="3"></td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rs</td><td colspan="2">rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DRP</td><td>CBUS读保护位0:WPx位用于每一个扇区的擦除/编程保护1:WPx位用于每一个扇区的擦除/编程和CBUS读保护</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>NWA</td><td>选择零等待区0:Bank11:Bank0</td></tr><tr><td>28</td><td>ECCEN</td><td>使能ECC0:失能ECC.1:使能ECC.</td></tr><tr><td>27:16</td><td>WP0[11:0]</td><td>当DRP为0时,每个扇区擦除/编程保护当DRP为1时,每个扇区擦除/编程和CBUS读保护。WP[0]作用于扇区0,WP[1]作用于扇区1,以此类推。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。1:当DRP为0时,无影响。当DRP为1时,擦除/编程和CBUS读保护。</td></tr><tr><td>15:8</td><td>SPC[7:0]</td><td>选项字节安全保护代码0xAA:无安全保护0xCC:安全保护高除0xAA或0xCC之外任何值:安全保护低</td></tr><tr><td>7</td><td>nRST_STDBY</td><td>选项字节待机复位值0:产生复位而不进入待机模式1:当进入待机模式时不产生复位</td></tr><tr><td>6</td><td>nRST_DPSLP</td><td>选项字节深度睡眠复位值0:产生复位而不进入深度睡眠模式1:当进入深度睡眠模式时不产生复位</td></tr><tr><td>5</td><td>nWDG_HW</td><td>选项字节看门狗值如果改变该位,需要系统复位生效0:硬件自由看门狗1:软件自由看门狗</td></tr><tr><td>4</td><td>BB</td><td>选项字节启动块值0:当配置从主存储块启动时,从bank0启动。1:当配置从主存储块启动时,从bank1启动,若bank1无启动程序,从bank0启</td></tr></table>

<table><tr><td></td><td></td><td>动。(如果bank0和bank1均无启动程序,芯片不处于高保护等级)</td></tr><tr><td>3:2</td><td>BOR_TH[1:0]</td><td>选项字节BOR阈值00:BOR阈值301:BOR阈值210:BOR阈值111:BOR关闭</td></tr><tr><td>1</td><td>OB_START</td><td>发送选项字节命令到FMC该位由软件设置。当BUSY位清0时由硬件清除该位。</td></tr><tr><td>0</td><td>OB_LK</td><td>FMC_OBCTLx锁定位当往FMC_OBKEY寄存器写值顺序正确时,该位由硬件清0。软件置位。</td></tr></table>

## 3.4.6. 选项字节控制寄存器 1（FMC_OBCTL1）

地址偏移：0x18

复位值：0xXXXX XXXX，初始值为 0x0FFF FFFF（复位后装载选项字节中的值）

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">WP1[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">WP1[19:12]</td><td colspan="8">WP0[19:12]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>WP1[11:0]</td><td>当DRP为0时,每个扇区擦除/编程保护。当DRP为1时,每个扇区擦除/编程和CBUS读保护。WP1[0]作用于扇区20,WP1[1]作用于扇区21,以此类推。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。1:当DRP为0时,无影响。当DRP为1时,擦除/编程和CBUS读保护。</td></tr><tr><td>15:8</td><td>WP1[19:12]</td><td>当DRP为0时,每个扇区擦除/编程保护。当DRP为1时,每个扇区擦除/编程和CBUS读保护。WP1[12]作用于扇区32,WP1[13]作用于扇区33,以此类推。特别指出,WP1[19]作用于扇区39~53。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。1:当DRP为0时,无影响。当DRP为1时,擦除/编程和CBUS读保护。</td></tr><tr><td>7:0</td><td>WP0[19:12]</td><td>当DRP为0时,每个扇区擦除/编程保护。当DRP为1时,每个扇区擦除/编程和CBUS读保护。WP0[12]作用于扇区12,WP0[13]作用于扇区13,以此类推。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。1:当DRP为0时,无影响。当DRP为1时,擦除/编程和CBUS读保护。</td></tr></table>

## 3.4.7. 页擦除配置寄存器（FMC_PECFG）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PE_EN</td><td colspan="2">保留</td><td colspan="13">PE_ADDR[28:16]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PE_ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PE_EN</td><td>页擦除功能使能位0:禁能页擦除1:使能页擦除</td></tr><tr><td>30:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:0</td><td>PE_ADDR[28:0]</td><td>待擦除页地址(4K字节对齐)</td></tr></table>

## 3.4.8. 页擦除功能解锁寄存器（FMC_PEKEY）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PE_KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PE_KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PE_KEY[31:0]</td><td>FMC_PECFG解锁寄存器这些位仅能被软件写。写解锁值0xA9B8C7D6到PE_KEY[31:0]可以解锁FMC_PECFG寄存器。</td></tr></table>

## 3.4.9. OTP1 配置寄存器（FMC_OTP1CFG）

地址偏移：0x28

复位值：0x0000 FFFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">Reserved</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OPT1REN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>OTP1REN[15:0]</td><td>使能OTP1读OTP1REN[x]决定OTP1数据块x是否可读,x=0..15。0:数据块不可读1:数据块可读软件可写0,但仅复位后设为1。</td></tr></table>

## 3.4.10. 代码加载 ECC 错误地址 0（FMC_LDECCADDR0）

地址偏移：0x2C

复位值：0xFFFF FFFF。复位后加载闪存数据。如果无 ECC 错误，默认值为 0xFFFF FFFF。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">LDECCADDR0[31:16]</td></tr><tr><td colspan="16">rs_r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LDECCADDR0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>LDECCADDR0[31:0]</td><td>当从主闪存 / bootloader / OTP1中加载代码时,表示ECC双位检测错误基地址(64位对齐)。64位的任意位置可能出错。</td></tr></table>

## 3.4.11. 代码加载 ECC 错误地址 1（FMC_LDECCADDR1）

地址偏移：0x30

复位值：0xFFFF FFFF。复位后加载闪存数据。如果无 ECC 错误，默认值为 0xFFFF FFFF。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">LDECCADDR1[31:16]</td></tr><tr><td colspan="16">rs_r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LDECCADDR1[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>LDECCADDR1[31:0]</td><td>当从主闪存 / bootloader / OTP1中加载代码时,表示ECC双位检测错误基地址(64位对齐)。64位的任意位置可能出错。</td></tr></table>

## 3.4.12. 代码加载 ECC 错误地址 2（FMC_LDECCADDR2）

地址偏移：0x34

复位值：0xFFFF FFFF。复位后加载闪存数据。如果无 ECC 错误，默认值为 0xFFFF FFFF。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">LDECCADDR2[31:16]</td></tr><tr><td colspan="16">rs_r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LDECCADDR2[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>LDECCADDR2[31:0]</td><td>当从主闪存 / bootloader / OTP1中加载代码时,表示ECC双位检测错误基地址(64位对齐)。64位的任意位置可能出错。</td></tr></table>

## 3.4.13. 选项字节状态寄存器（FMC_OBSTAT）

地址偏移：0x40

复位值：0x0000 0000.

该寄存器只能按字（32 位）访问。

<table><tr><td colspan="16">Reserved</td></tr><tr><td colspan="13">Reserved</td><td>SPCH</td><td>SPCL</td><td>Reserved</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SPCH</td><td>芯片当前安全保护为高等级时为1。</td></tr><tr><td>1</td><td>SPCL</td><td>芯片当前安全保护为低等级时为1。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 3.4.14. 产品 ID 寄存器（FMC_PID）

地址偏移：0x100

复位值：0xXXXX XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留ID寄存器该寄存器为只读</td></tr></table>


上电后这些位始终不会改变，该寄存器在生产过程中被一次性编程。


## 3.4.15. 熔丝控制和状态寄存器（EFUSE_CS）

地址偏移：0x200

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td colspan="4">Reserved</td><td>OVBERIC</td><td>RDIC</td><td>PGIC</td><td>Reserved</td><td>OVBERIE</td><td>RDIE</td><td>PGIE</td><td>Reserved</td><td>OVBERIF</td><td>RDIF</td><td>PGIF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td colspan="8">Reserved</td><td>EFBYP</td><td>EFRW</td><td>EFSTR</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>OVBERIC</td><td>越界错误中断标志清除位0:无影响1:清除越界错误标志位</td></tr><tr><td>25</td><td>RDIC</td><td>读操作完成中断标志清除位0:无影响1:清除读操作完成中断标志位</td></tr><tr><td>24</td><td>PGIC</td><td>写操作完成中断标志清除位0:无影响1:清除写操作完成中断标志位</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>OVBERIE</td><td>越界错误中断使能位0:失能越界错误中断1:使能越界错误中断</td></tr><tr><td>21</td><td>RDIE</td><td>读操作完成中断使能位0:失能读操作完成中断1:使能读操作完成中断</td></tr><tr><td>20</td><td>PGIE</td><td>写操作完成中断使能位0:失能写操作完成中断1:使能写操作完成中断</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>OVBERIF</td><td>越界错误标志位0:未发生越界错误1:发生越界错误</td></tr><tr><td>17</td><td>RDIF</td><td>读操作完成标志位0:读操作未完成1:读操作完成</td></tr><tr><td>16</td><td>PGIF</td><td>写操作完成标志位0:写操作未完成1:写操作完成</td></tr><tr><td>15:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>EFBYP</td><td>EFUSE内部LDO旁路。该位仅EFSTR为0时可置位。如果需要置位该位,用户需要确保EFSTR置位前外部供电稳定。编程时电压需要在2.25V~2.75V范围内,典型值为2.5V。.0:EFUSE编程使用内部LDO供电1:EFUSE编程使用外部VEFUSE管脚供电</td></tr><tr><td>1</td><td>EFRW</td><td>熔丝读写操作选择位0:读熔丝内容1:写熔丝内容当EFSTR为1时该位不可写。</td></tr><tr><td>0</td><td>EFSTR</td><td>发送熔丝读/写操作命令位该位由软件置1,硬件清00:无影响1:开始读/写操作</td></tr></table>

## 3.4.16. 熔丝地址寄存器（EFUSE_ADDR）

地址偏移：0x204

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">Reserved</td></tr></table>

<table><tr><td>Reserved</td><td>EFSIZE[4:0]</td><td>Reserved</td><td>EFADDR[4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>EFSIZE[4:0]</td><td>读/写熔丝数据大小</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>EFADDR[4:0]</td><td>读/写熔丝数据起始地址</td></tr></table>


注意：当 EFUSE_CS 寄存器中的 EFSTR 位为 1 时，该寄存器不可写


## 3.4.17. 熔丝控制寄存器（EFUSE_CTL）

地址偏移：0x208

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">Reserved</td></tr></table>

<table><tr><td colspan="7">Reserved</td><td>LK</td><td>UDLK</td><td>Reserved</td><td>BTFOSEL</td><td>NBTSB</td><td>NDBG</td><td>EFSPC</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>EFUSE_CTL 寄存器锁定位0:解锁 EFUSE_CTL 寄存器1:锁定 EFUSE_CTL 寄存器</td></tr><tr><td>6</td><td>UDLK</td><td>EFUSE_USER_DATA寄存器锁定位0:解锁EFUSE_USER_DATA寄存器1:锁定 EFUSE_USER_DATA 寄存器</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>BTFOSEL</td><td>选择从主闪存或 OTP1 启动。NBTSB=1 或 BOOT0=0 时该位有效。0:从主闪存启动1:从 OTP1 启动</td></tr><tr><td>2</td><td>NBTSB</td><td>禁止从 SRAM 或 bootloader 中启动0:能够从 SRAM 或 bootloader 中启动1:禁止从 SRAM 或 bootloader 中启动</td></tr><tr><td>1</td><td>NDBG</td><td>设置调试权限0:无影响1:不可调试</td></tr><tr><td>0</td><td>EFSPC</td><td>EFUSE 安全保护,禁止 SPC 从无保护更改为等级低0:无保护1:禁止 SPC 等级低</td></tr></table>

## 3.4.18. 熔丝用户数据寄存器（EFUSE_USER_DATA）

地址偏移：0x20C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td colspan="16">Reserved</td></tr><tr><td colspan="8">Reserved</td><td colspan="8">USERDATA[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>USERDATA[7:0]</td><td>熔丝中用户自定义数据字段</td></tr></table>
