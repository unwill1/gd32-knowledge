## 6.4. FMC 寄存器

FMC 基地址：0x4002 2000

## 6.4.1. 解锁寄存器 (FMC_KEY0)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL0解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁FMC_CTL0寄存器。</td></tr></table>

## 6.4.2. 选项字节操作解锁寄存器（FMC_OBKEY）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>选项字节操作解锁寄存器这些位仅软件可写。写解锁值到OBKEY[31:0]解锁FMC_OBCTLx (x = 0,1,2)寄存器的选项字节命令。</td></tr></table>

## 6.4.3. 状态寄存器 0 (FMC_STAT0)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ENDF</td><td>WPERR</td><td>保留</td><td>PGERR</td><td>保留</td><td>BUSY</td></tr><tr><td colspan="10"></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td></td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ENDF</td><td>操作结束标志位操作成功执行后,此位被硬件置1,软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>PGERR</td><td>编程错误标志位当被编程区域状态不为0xFFFF时,对闪存编程,此位被硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr></table>

## 6.4.4. 控制寄存器 0 (FMC_CTL0)

地址偏移：0x10

复位值：0x0000 0080

该寄存器只能按字(32 位)访问

注意：当相应闪存操作完成后，该寄存器需处于复位状态。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>NWLDE</td><td>PWDN</td><td colspan="14">Reserved</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">Reserved</td><td>RLBE</td><td>ENDIE</td><td>Reserved</td><td>ERRIE</td><td colspan="2">Reserved</td><td>LK</td><td>START</td><td colspan="3">Reserved</td><td>MER</td><td>PER</td><td>PG</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>NWLDE</td><td>在系统复位时使能零等待时间区域加载。零等待时间区域加载包括加载选项字节、一次性可编程(OTP)和主闪存代码区。该位由软件设置或清除,系统复位后不复位,上电复位后复位。0:系统复位后不拷贝闪存内容到缓冲区。1:系统复位后拷贝闪存内容到缓冲区。</td></tr><tr><td>30</td><td>PWDN</td><td>当没有操作时,闪存进入深度掉电模式。该位由软件设置或清除,系统复位后不复位,上电复位后复位。1:进入深度掉电模式0:不进入深度掉电模式注意:1、在省电模式下,闪存仅在PWDN位置为1时才会进入深度掉电模式。2、在使能CPU Cbus超时(CPUCBUSTO=1)且PWDN=1的情况下,闪存进入深度掉电模式后,访问闪存非零等待区(data区)会导致CBUS超时,引发Hardfault错误。3、在未使能CPU Cbus超时(CPUCBUSTO=0)且PWDN=1的情况下,闪存进入深度掉电模式后,访问闪存非零等待区(data区)会唤醒闪存,需要等待闪存唤醒时间,访问闪存零等待区(code区)不会唤醒闪存且无需等待。</td></tr><tr><td>29:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>RLBE</td><td>使能OTP2读锁定块。只能软件置1使能读锁定。软件一旦置1,读锁定块对应的数据块无法被读。复位后恢复复位值。</td></tr><tr><td>12</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清0。0:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ERRIE</td><td>出错中断使能位软件置1和清0。0:无硬件中断产生1:使能出错中断</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>FMC_CTL0寄存器锁定标志位当正确的序列写入FMC_KEY0寄存器,此位由硬件清0。此位可以由软件置1。</td></tr><tr><td>6</td><td>START</td><td>向FMC发送擦除命令位软件置1可以发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>5:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>MER</td><td>主存储块整片擦除命令位软件置1和清0。0:无作用1:主存储块整片擦除命令</td></tr><tr><td>1</td><td>PER</td><td>主存储块页擦除命令位软件置1和清0。0:无作用1:主存储块页擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清0。0:无作用1:主存储块编程命令</td></tr></table>

## 6.4.5. 地址寄存器 0 (FMC_ADDR0)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除地址该位通过软件设置。ADDR位是闪存擦除命令的地址。</td></tr></table>

## 6.4.6. 选项字节控制寄存器 0 (FMC_OBCTL0)

地址偏移：0x18

复位值：0x0XXX XXXX

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">SPC[7:0]</td><td colspan="6">保留</td><td>OB_START</td><td>OB_LK</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>SPC[7:0]</td><td>选项字节安全保护代码0xAA:无安全保护0xCC:安全保护高除0xAA或0xCC之外任何值:安全保护低</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OB_START</td><td>发送选项字节命令到FMC该位由软件设置。当BUSY位清0时由硬件清除该位。</td></tr><tr><td>0</td><td>OB_LK</td><td>FMC_OBCTL0/1/2锁定位当往FMC_OBKEY寄存器写值顺序正确时,该位由硬件清0。软件置位。</td></tr></table>

## 6.4.7. 选项字节控制寄存器 1 (FMC_OBCTL1)

地址偏移：0x1C

复位值：0x0XXX XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">DATA[15:6]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">DATA[5:0]</td><td colspan="8">USER[7:0]</td><td>保留</td><td>OBERR</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:10</td><td>DATA[15:0]</td><td>系统复位后保存选项字节块的DATA[15:0]部分</td></tr><tr><td>9:2</td><td>USER[7:0]</td><td>系统复位后保存选项字节块的USER字节</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>OBERR</td><td>选项字节读错误位当选项字节和它的补字节不匹配时此位由硬件置1,选项字节被强制设置为0xFF。</td></tr></table>

## 6.4.8. 选项字节控制寄存器 2 (FMC_OBCTL2)

地址偏移：0x20

复位值：0xXXXX XXXX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WP[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WP[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WP[31:0]</td><td>系统复位后保存选项字节块的WP[31:0]部分。</td></tr></table>

## 6.4.9. OTP1 配置寄存器 (FMC_OTP1CFG)

地址偏移：0x24

复位值：0x0000 FFFF.

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OTP1REN[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>OTP1REN[15:0]</td><td>使能OTP1读OTP1REN[x]决定OTP1数据块x是否可读,x=0..15。0:数据块不可读1:数据块可读</td></tr></table>

软件可写0，但仅复位后设为1。

## 6.4.10. 选项字节状态寄存器 (FMC_OBSTAT)

地址偏移：0x40

复位值：0x0000 0000.

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>SPCH</td><td>SPCL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SPCH</td><td>芯片当前安全保护为高等级时为1。</td></tr><tr><td>0</td><td>SPCL</td><td>芯片当前安全保护为低等级时为1。</td></tr></table>

## 6.4.11. 解锁寄存器 1 (FMC_KEY1)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL1解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁FMC_CTL1寄存器。</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ENDIE</td><td>保留</td><td>ERRIE</td><td colspan="2">保留</td><td>LK</td><td>START</td><td colspan="3">保留</td><td>MER</td><td>PER</td><td>PG</td></tr></table>

## 6.4.12. 状态寄存器 1 (FMC_STAT1)

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ENDF</td><td>WPERR</td><td>保留</td><td>PGERR</td><td>保留</td><td>BUSY</td></tr><tr><td colspan="10"></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td></td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ENDF</td><td>操作结束标志位操作成功执行后,此位被硬件置1。软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>PGERR</td><td>编程错误标志位当被编程区域状态不为0xFFFF时,对闪存编程,此位被硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr></table>

## 6.4.13. 控制寄存器 1 (FMC_CTL1)

地址偏移：0x50

复位值：0x0000 0080

该寄存器只能按字(32 位)访问。

注意：当相应闪存操作完成后，该寄存器需处于复位状态。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清0。0:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ERRIE</td><td>出错中断使能位软件置1和清0。0:无硬件中断产生1:使能出错中断</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>FMC_CTL1寄存器锁定标志位当正确的序列写入FMC_KEY1寄存器,此位由硬件清0。此位可以由软件置1。</td></tr><tr><td>6</td><td>START</td><td>发送擦除命令到FMC位软件置1可以发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>5:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>MER</td><td>主存储块整片擦除命令位软件置1和清0。0:无作用1:主存储块整片擦除命令</td></tr><tr><td>1</td><td>PER</td><td>主存储块页擦除命令位软件置1和清0。0:无作用1:主存储块页擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清0。0:无作用1:主存储块编程命令</td></tr></table>

## 6.4.14. 地址寄存器 1 (FMC_ADDR1)

地址偏移：0x54

复位值：0x0000 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除地址该位通过软件设置。ADDR位是闪存擦除命令的地址</td></tr></table>

## 6.4.15. OTP3 状态寄存器 (FMC_OTP3_STAT)

地址偏移：0x60

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>BTFOSEL_LK</td><td>NBTSB_LK</td><td>NDBG_LK</td><td>保留</td><td>BTFOSEL</td><td>NBTSB</td><td>NDBG</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>BTFOSEL_LK</td><td>BTFOSEL 锁状态0:未锁定1:锁定</td></tr><tr><td>5</td><td>NBTSB_LK</td><td>NBTSB 锁状态0:未锁定1:锁定</td></tr><tr><td>4</td><td>NDBG_LK</td><td>NDBG 锁状态0:未锁定1:锁定</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>BTFOSEL</td><td>选择从主闪存或 OTP1 启动。NBTSB=1 或 BOOT0=0 时该位有效。0:从主闪存启动1:从 OTP1 启动</td></tr><tr><td>1</td><td>NBTSB</td><td>禁止从 SRAM 或 bootloader 中启动0:能够从 SRAM 或 bootloader 中启动1:禁止从 SRAM 或 bootloader 中启动</td></tr><tr><td>0</td><td>NDBG</td><td>设置调试权限0:无影响1:不可调试</td></tr></table>

## 6.4.16. 产品 ID 寄存器 (FMC_PIDx, x=0...1)

地址偏移：0x100 + 0x4 * x

复位值：0xXXXX XXXX


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留ID寄存器该寄存器为只读。上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>
