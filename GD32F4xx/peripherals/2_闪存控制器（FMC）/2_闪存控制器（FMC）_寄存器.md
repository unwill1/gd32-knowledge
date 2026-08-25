## 2.4. FMC 寄存器

FMC 基地址：0x4002 3C00

## 2.4.1. 等待状态寄存器 (FMC_WS)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">WSCNT[3:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>WSCNT[3:0]</td><td>等待状态计数寄存器软件置1和清0。FMC_WSEN寄存器的WSEN位被置1时WSCNT位有效。0000:不增加等待状态0001:增加1个等待状态0010:增加2个等待状态...1111:增加15个等待状态</td></tr></table>

## 2.4.2. 解锁寄存器 (FMC_KEY)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL解锁寄存器这些位仅能被软件写。</td></tr></table>

写解锁值到KEY[31:0]可以解锁 FMC_CTL寄存器。

## 2.4.3. 选项字节解锁寄存器 (FMC_OBKEY)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>


W


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_OBCTLx选项字节解锁寄存器这些位仅能被软件写写解锁值到OBKEY[31:0]解锁FMC_OBCTLx寄存器的选项字节命令</td></tr></table>

## 2.4.4. 状态寄存器 (FMC_STAT)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BUSY</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>RDDERR</td><td>PGSERR</td><td>PGMERR</td><td>保留</td><td>WPERR</td><td colspan="2">保留</td><td>OPERR</td><td>END</td></tr><tr><td colspan="7"></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td colspan="2"></td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BUSY</td><td>闪存忙标志位当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>RDDERR</td><td>DBUS读保护错误标志位在DBUS读保护扇区进行DBUS读操作时,该位由硬件置位。软件写1清0。</td></tr><tr><td>7</td><td>PGSERR</td><td>编程顺序错误标志位当FMC_CTL寄存器中PG位未置位时进行闪存编程,该位由硬件置位。软件写1清0。</td></tr><tr><td>6</td><td>PGMERR</td><td>编程类型不匹配错误标志位当编程写入数据类型(字/半字/字节访问)与FMC_CTL寄存器中PSZ位不匹配时,该位由硬件置位。软件写1清0。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OPERR</td><td>闪存操作错误标志位该位由硬件置位,当FMC_CTL寄存器中ERRIE位被置位时闪存操作发生错误(当RDDERR/PGSERR/PGMERR/WPERR位被置位时表示错误发生)。软件写1清0。</td></tr><tr><td>0</td><td>END</td><td>操作结束标志位当操作执行成功,此位被硬件置1。软件写1清0。</td></tr></table>

## 2.4.5. 控制寄存器 (FMC_CTL)

地址偏移：0x10

复位值：0x8000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="5">保留</td><td>ERRIE</td><td>ENDIE</td><td colspan="7">保留</td><td>START</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rs</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MER1</td><td colspan="5">保留</td><td colspan="2">PSZ[1:0]</td><td colspan="5">SN[4:0]</td><td>MERO</td><td>SER</td><td>PG</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>FMC_CTL锁定当向FMC_KEY寄存器中写入正确的顺序,该位由硬件清除。软件置1。</td></tr><tr><td>30:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>ERRIE</td><td>错误中断使能位软件置1和清00:无硬件中断产生1:使能错误中断</td></tr><tr><td>24</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清00:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>START</td><td>发送擦除命令位该位由软件置位,发送擦除命令到FMC。该位当BUSY位清零时由硬件清零。</td></tr><tr><td>15</td><td>MER1</td><td>主存储闪存bank1整片擦除命令位软件置1和清00:无影响1:主存储闪存bank1整片擦除命令</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>PSZ[1:0]</td><td>编程大小位软件置1和清000:按字节编程访问01:按半字编程访问10/11:按字编程访问</td></tr><tr><td>7:3</td><td>SN[4:0]</td><td>选择擦除扇区号软件置1和清000000:选择扇区00001:选择扇区1...01011:选择扇区1101100:选择扇区2401101:选择扇区2501110:选择扇区2601111:选择扇区2710000:选择扇区1210001:选择扇区13...11011:选择扇区2311100~11111:保留</td></tr><tr><td>2</td><td>MER0</td><td>主存储块bank0整片擦除命令位软件置1和清00:无作用1:主存储块bank0整片擦除命令</td></tr><tr><td>1</td><td>SER</td><td>主存储块扇区擦除命令位软件置1和清00:无作用1:主存储块扇区擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清00:无作用</td></tr></table>

1: 主存储块编程命令

注意：当相应闪存操作完成后，该寄存器需处于复位状态。

## 2.4.6. 选项字节控制寄存器 0 (FMC_OBCTL0)

地址偏移：0x14

复位值：0xXXXX XXXX，初始值为0x2FFF AAED。复位后装载选项字节中的值。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DRP</td><td>DBS</td><td colspan="2">保留</td><td colspan="12">WP0[11:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="14">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">SPC[7:0]</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td>nWDG_HW</td><td>BB</td><td colspan="2">BOR_TH[1:0]</td><td>OB_START</td><td>OB_LK</td></tr><tr><td colspan="2"></td><td colspan="6">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rs</td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DRP</td><td>DBUS读保护位0:WPx位用于每一个扇区的擦除/编程保护1:WPx位用于每一个扇区的擦除/编程和DBUS读保护注意:该功能位仅对GD32F450xx、GD32F470xx系列有效</td></tr><tr><td>30</td><td>DBS</td><td>当闪存大小为1M字节时,选择设置为双块还是单块0:当内存大小为1M字节时,设置为单块1:当内存大小为1M字节时,设置为双块注意:该功能位仅对GD32F450xx、GD32F470xx 1M闪存系列有效。</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>WP0[11:0]</td><td>当DRP为0时,每个扇区擦除/编程保护当DRP为1时,每个扇区擦除/编程和DBUS读保护。WP[0]作用于扇区0,WP[1]作用于扇区1,以此类推。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。1:当DRP为0时,无影响。当DRP为1时,擦除/编程和DBUS读保护。</td></tr><tr><td>15:8</td><td>SPC[7::0]</td><td>选项字节安全保护代码0xAA:无安全保护0xCC:安全保护高除0xAA或0xCC之外任何值:安全保护低</td></tr><tr><td>7</td><td>nRST_STDBY</td><td>选项字节待机复位值0:产生复位而不进入待机模式1:当进入待机模式时不产生复位</td></tr><tr><td>6</td><td>nRST_DPSLP</td><td>选项字节深度睡眠复位值0:产生复位而不进入深度睡眠模式1:当进入深度睡眠模式时不产生复位</td></tr><tr><td>5</td><td>nWDG_HW</td><td>选项字节看门狗值如果改变该位,需要系统复位生效0:硬件自由看门狗1:软件自由看门狗</td></tr><tr><td>4</td><td>BB</td><td>选项字节启动块值0:当配置从主存储块启动时,从bank0启动。1:当配置从主存储块启动时,从bank1启动,若bank1无启动程序,从bank0启动。(如果bank0和bank1均无启动程序,芯片不处于高保护等级)注意:该功能位仅对GD32F450xx、GD32F470xx具有双BANK闪存系列有效(通过DBS=1除外)</td></tr><tr><td>3:2</td><td>BOR_TH[1:0]</td><td>选项字节BOR阈值00:BOR阈值301:BOR阈值210:BOR阈值111:BOR关闭</td></tr><tr><td>1</td><td>OB_START</td><td>发送选项字节命令到FMC该位由软件设置。当BUSY位清0时由硬件清除该位。</td></tr><tr><td>0</td><td>OB_LK</td><td>FMC_OBCTLx锁定位当往FMC_OBKEY寄存器写值顺序正确时,该位由硬件清0。软件置位。</td></tr></table>

## 2.4.7. 选项字节控制寄存器 1 (FMC_OBCTL1)

地址偏移：0x18

复位值：0xXXXX XXXX，初始值为0x0FFF 0000（复位后装载选项字节中的值）

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">WP1[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>WP1[11:0]</td><td>当DRP为0时,每个扇区擦除/编程保护。当DRP为1时,每个扇区擦除/编程和DBUS读保护。WP1[0]作用于扇区12,WP1[1]作用于扇区13,以此类推。特别指出,WP1[11]作用于扇区23~27。0:当DRP为0时,擦除/编程保护。当DRP为1时,无影响。</td></tr></table>

1: 当DRP为0时，无影响。当DRP为1时，擦除/编程和DBUS读保护。

15:0 保留 必须保持复位值。

## 2.4.8. 页擦除配置寄存器 (FMC_PECFG)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PE_EN</td><td colspan="2">保留</td><td colspan="13">PE_ADDR[28:16]</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PE_ADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PE_EN</td><td>页擦除功能使能位0:禁能页擦除1:使能页擦除</td></tr><tr><td>30:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:0</td><td>PE_ADDR[28:0]</td><td>待擦除页地址(4K字节对齐)</td></tr></table>

## 2.4.9. 页擦除功能解锁寄存器 (FMC_PEKEY)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PE_KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PE_KEY[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PE_KEY[31:0]</td><td>FMC_PECFG解锁寄存器这些位仅能被软件写。写解锁值0xA9B8C7D6到PE_KEY[31:0]可以解锁FMC_PECFG寄存器。</td></tr></table>

## 2.4.10. 等待状态使能寄存器 (FMC_WSEN)

地址偏移：0xFC

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>WSEN</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>WSEN</td><td>闪存等待状态使能软件写1和清0。该位由FMC_KEY寄存器保护。往FMC_KEY寄存器中写入0x45670123和0XCDEF89AB来解锁该位。0:读取闪存时,无等待状态1:读取闪存时,有等待状态</td></tr></table>

## 2.4.11. 产品 ID 寄存器 (FMC_PID)

地址偏移：0x100

复位值：0xXXXX XXXX

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留ID寄存器</td></tr><tr><td></td><td></td><td>该寄存器为只读</td></tr><tr><td></td><td></td><td>上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>
