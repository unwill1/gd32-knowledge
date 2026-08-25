## 2.4. FMC 寄存器

FMC基地址：0x4002 2000

## 2.4.1. 等待状态寄存器 (FMC_WS)

地址偏移：0x00

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">WSCNT[2:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>WSCNT[2:0]</td><td>等待状态计数寄存器软件置1和清0,FMC_WSEN寄存器的WSEN位被置1时WSCNT位有效。000:不增加等待状态001:增加1个等待状态010:增加2个等待状态011~111:保留</td></tr></table>

## 2.4.2. 解锁寄存器 (FMC_KEY0)

地址偏移：0x04

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL0解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁FMC_CTL0寄存器。</td></tr></table>

## 2.4.3. 选项字节操作解锁寄存器（FMC_OBKEY）

地址偏移：0x08

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY[31:0]</td><td>FMC_CTL0可选字节操作解锁寄存器这些位仅软件可写。写解锁值到OBKEY[31:0]解锁FMC_CTL0寄存器的可选字节命令。</td></tr></table>

## 2.4.4. 状态寄存器 0 (FMC_STAT0)

地址偏移：0x0C

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ENDF</td><td>WPERR</td><td>保留</td><td>PGERR</td><td>保留</td><td>BUSY</td></tr><tr><td colspan="10"></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td></td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ENDF</td><td>操作结束标志位操作成功执行后,此位被硬件置1,软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>PGERR</td><td>编程错误标志位当被编程区域状态不为0xFFFF时,对闪存编程,此位被硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志</td></tr></table>

当闪存操作正在进行时，此位被置1。当操作结束或者出错，此位被清0。

## 2.4.5. 控制寄存器 0 (FMC_CTL0)

地址偏移：0x10

复位值：0x0000 0080


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ENDIE</td><td>保留</td><td>ERRIE</td><td>OBWEN</td><td>保留</td><td>LK</td><td>START</td><td>OBER</td><td>OBPG</td><td>保留</td><td>MER</td><td>PER</td><td>PG</td></tr><tr><td colspan="3"></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rs</td><td>rs</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清0。0:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ERRIE</td><td>出错中断使能位软件置1和清0。0:无硬件中断产生1:使能出错中断</td></tr><tr><td>9</td><td>OBWEN</td><td>可选字节擦除/编程使能位当正确的序列写入FMC_OBKEY寄存器,此位由硬件置1。此位可以被软件清0。</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>FMC_CTL0寄存器锁定标志位当正确的序列写入FMC_KEY0寄存器,此位由硬件清0。此位可以由软件置1。</td></tr><tr><td>6</td><td>START</td><td>向FMC发送擦除命令位软件置1可以发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>5</td><td>OBER</td><td>可选字节擦除命令位软件置1和清0。0:无作用1:可选字节擦除命令</td></tr><tr><td>4</td><td>OBPG</td><td>可选字节编程命令位软件置1和清0。0:无作用</td></tr></table>

1: 可选字节编程命令

3 保留 必须保持复位值。

2 MER 主存储块整片擦除命令位软件置1和清0。

0: 无作用

1: 主存储块整片擦除命令

1 PER 主存储块页擦除命令位软件置1和清0。

0: 无作用

1: 主存储块页擦除命令

0 PG 主存储块编程命令位软件置1和清0。

0: 无作用

1: 主存储块编程命令

注意：当相应闪存操作完成后，该寄存器需处于复位状态。

## 2.4.6. 地址寄存器 0 (FMC_ADDR0)

地址偏移：0x14

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">W</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>


W 



位/位域 名称 描述


<table><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除或编程地址该位通过软件设置。ADDR 位是闪存擦除命令的地址。</td></tr></table>

## 2.4.7. 选项字节状态寄存器 (FMC_OBSTAT)

地址偏移：0x1C

复位值：0x0XXX XXXX


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">DATA[15:6]</td></tr></table>

<table><tr><td colspan="6">15 14 13 12 11 10</td><td colspan="6">9 8 7 6 5 4 3 2</td><td>1 0</td></tr><tr><td colspan="6">DATA[5:0]</td><td colspan="5">USER[7:0]</td><td>SPC</td><td>OBERR</td></tr><tr><td colspan="6">r</td><td colspan="5">r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:10</td><td>DATA[15:0]</td><td>系统复位后保存可选字节块的DATA[15:0]部分</td></tr><tr><td>9:2</td><td>USER[7:0]</td><td>系统复位后保存可选字节块的USER字节</td></tr><tr><td>1</td><td>SPC</td><td>安全保护状态0:未保护1:已保护</td></tr><tr><td>0</td><td>OBERR</td><td>可选字节读错误位当可选字节和它的补字节不匹配时此位由硬件置1,可选字节被强制设置为0xFF。</td></tr></table>

## 2.4.8. 擦除/编程保护寄存器 (FMC_WP)

地址偏移：0x20

复位值：0xXXXX XXXX

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WP[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WP[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WP[31:0]</td><td>系统复位后保存可选字节块的WP[31:0]部分。</td></tr></table>

## 2.4.9. 解锁寄存器 1 (FMC_KEY1)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字(32位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

W 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL1解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁 FMC_CTL1寄存器。</td></tr></table>

## 2.4.10. 状态寄存器 1 (FMC_STAT1)

地址偏移：0x4C

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ENDF</td><td>WPERR</td><td>保留</td><td>PGERR</td><td>保留</td><td>BUSY</td></tr><tr><td colspan="10"></td><td>rc_w1</td><td>rc_w1</td><td></td><td>rc_w1</td><td></td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ENDF</td><td>操作结束标志位操作成功执行后,此位被硬件置1。软件写1清0。</td></tr><tr><td>4</td><td>WPERR</td><td>擦除/编程保护错误标志位在受保护的页上擦除/编程操作时,此位被硬件置1。软件写1清0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>PGERR</td><td>编程错误标志位当被编程区域状态不为0xFFFF时,对闪存编程,此位被硬件置1。软件写1清0。</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr></table>

## 2.4.11. 控制寄存器 1 (FMC_CTL1)

地址偏移：0x50

复位值：0x0000 0080


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ENDIE</td><td>保留</td><td>ERRIE</td><td colspan="2">保留</td><td>LK</td><td>START</td><td colspan="3">保留</td><td>MER</td><td>PER</td><td>PG</td></tr><tr><td colspan="3"></td><td>rw</td><td></td><td>rw</td><td colspan="2"></td><td>rs</td><td>rs</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ENDIE</td><td>操作结束中断使能位软件置1和清0。0:无硬件中断产生1:使能操作结束中断</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ERRIE</td><td>出错中断使能位软件置1和清0。0:无硬件中断产生1:使能出错中断</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>LK</td><td>FMC_CTL1寄存器锁定标志位当正确的序列写入FMC_KEY1寄存器,此位由硬件清0。此位可以由软件置1。</td></tr><tr><td>6</td><td>START</td><td>发送擦除命令到FMC位软件置1可以发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>5:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>MER</td><td>主存储块整片擦除命令位软件置1和清0。0:无作用1:主存储块整片擦除命令</td></tr><tr><td>1</td><td>PER</td><td>主存储块页擦除命令位软件置1和清0。0:无作用1:主存储块页擦除命令</td></tr><tr><td>0</td><td>PG</td><td>主存储块编程命令位软件置1和清0。0:无作用1:主存储块编程命令</td></tr></table>


注意：当相应闪存操作完成后，该寄存器需处于复位状态。


## 2.4.12. 地址寄存器 1 (FMC_ADDR1)

地址偏移：0x54

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">W</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>


W


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除或编程地址该位通过软件设置。ADDR 位是闪存擦除命令的地址</td></tr></table>

## 2.4.13. 等待状态使能寄存器 (FMC_WSEN)

地址偏移：0xFC

复位值：0x0000 0000


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>BPEN</td><td>WSEN</td></tr></table>


rw    rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>BPEN</td><td>FMC位编程功能使能寄存器此位由软件置1和清0。0:无效,写操作必须检测闪存操作页全为FF1:写操作不需要检测闪存操作页全为FF,FMC可以按位编程,写入数据和存储在闪存中数据进行逻辑与操作</td></tr><tr><td>0</td><td>WSEN</td><td>FMC等待状态使能寄存器此位由软件置1和清0。此位也被FMC_KEYx寄存器保护。需要写0x45670123和0xCDEF89AB到FMC_KEYx寄存器。0:从闪存取指无等待状态1:从闪存取指增加等待状态</td></tr></table>

## 2.4.14. 产品 ID 寄存器 (FMC_PID)

地址偏移：0x100

复位值：0xXXXX XXXX


该寄存器只能按字(32位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留ID寄存器该寄存器为只读。上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>

