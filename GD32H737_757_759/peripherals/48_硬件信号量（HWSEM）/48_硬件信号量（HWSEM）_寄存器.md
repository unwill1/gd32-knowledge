# 48.4. HWSEM 寄存器

HWSEM基地址：0x5802 6400

# 48.4.1. 控制寄存器（HWSEM_CTLx）（x=0…31）

地址偏移：0x00 + 0x4 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">MID[3:0]</td><td colspan="8">PID[7:0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>锁定信号0:当MID[3:0]和PID[7:0]与信号量信息匹配时,解锁信号量1:尝试锁定信号量</td></tr><tr><td>30:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>MID[3:0]</td><td>AHB总线主控ID软件写入,只有当信号量未锁定,并且要写入的MID[3:0]值与写锁定操作的AHB总线主控相匹配时,要写入的MID[3:0]值才会写入该位域。在写解锁操作中,当要写入的MID[3:0]值与写解锁操作的AHB总线主控相匹配时,该位域将清零。</td></tr><tr><td>7:0</td><td>PID[7:0]</td><td>进程ID软件写入,只有当信号量未锁定时,才可通过写锁定操作将PID[7:0]值写入该位域。在写解锁操作中,该位域将被清零。</td></tr></table>

# 48.4.2. 读锁定寄存器（HWSEM_RLKx）（x=0...31）

地址偏移：0x80 + 0x4 * x

复位值：0x0000 0000

HWSEM_RLKx（x=0...31）访问的物理地址与HWSEM_LKx（x=0...31）寄存器相同。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>MID[3:0]</td><td>PID[7:0]</td></tr><tr><td colspan="2">r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>读操作锁定信号当通过匹配的AHB总线主控读该位时,将始终返回1,如果信号量在读操作之前是解锁状态,则此时信号量会被硬件读锁定,如果信号量在读操作之前是锁定状态,则此时该位不变。0:信号量未锁定1:信号量已锁定</td></tr><tr><td>30:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>MID[3:0]</td><td>总线主控ID当通过匹配的AHB总线主控读该位域时,如果信号量在读操作之前是解锁状态,则此时AHB总线主控ID将被写入该位域,如果信号量在读操作之前是锁定状态,则此时将返回锁定该信号量的MID[3:0]。</td></tr><tr><td>7:0</td><td>PID[7:0]</td><td>进程ID当通过匹配的AHB总线主控读该位域时,如果信号量在读操作之前是解锁状态,则此时该位域将被写为0且读为0,如果信号量在读操作之前是锁定状态,则此时将返回锁定该信号量的PID[7:0]。</td></tr></table>

# 48.4.3. 中断使能寄存器（HWSEM_INTEN）

地址偏移：0x100

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SIE31</td><td>SIE30</td><td>SIE29</td><td>SIE28</td><td>SIE27</td><td>SIE26</td><td>SIE25</td><td>SIE24</td><td>SIE23</td><td>SIE22</td><td>SIE21</td><td>SIE20</td><td>SIE19</td><td>SIE18</td><td>SIE17</td><td>SIE16</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SIE15</td><td>SIE14</td><td>SIE13</td><td>SIE12</td><td>SIE11</td><td>SIE10</td><td>SIE9</td><td>SIE8</td><td>SIE7</td><td>SIE6</td><td>SIE5</td><td>SIE4</td><td>SIE3</td><td>SIE2</td><td>SIE1</td><td>SIE0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SIEx</td><td>信号量中断使能位0:禁能信号量中断1:使能信号量中断</td></tr></table>

# 48.4.4. 中断状态清除寄存器（HWSEM_INTC）

地址偏移：0x104

复位值：0x0000 0000


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SIFC31</td><td>SIFC30</td><td>SIFC29</td><td>SIFC28</td><td>SIFC27</td><td>SIFC26</td><td>SIFC25</td><td>SIFC24</td><td>SIFC23</td><td>SIFC22</td><td>SIFC21</td><td>SIFC20</td><td>SIFC19</td><td>SIFC18</td><td>SIFC17</td><td>SIFC16</td></tr><tr><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SIFC15</td><td>SIFC14</td><td>SIFC13</td><td>SIFC12</td><td>SIFC11</td><td>SIFC10</td><td>SIFC9</td><td>SIFC8</td><td>SIFC7</td><td>SIFC6</td><td>SIFC5</td><td>SIFC4</td><td>SIFC3</td><td>SIFC2</td><td>SIFC1</td><td>SIFC0</td></tr><tr><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td><td>w1</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:0</td><td>SIFCx</td><td>信号量中断标志清除位软件写入,始终读为0。0:无影响1:清除信号量标志和中断标志</td></tr></table>

# 48.4.5. 状态寄存器（HWSEM_STAT）

地址偏移：0x108

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SF31</td><td>SF30</td><td>SF29</td><td>SF28</td><td>SF27</td><td>SF26</td><td>SF25</td><td>SF24</td><td>SF23</td><td>SF22</td><td>SF21</td><td>SF20</td><td>SF19</td><td>SF18</td><td>SF17</td><td>SF16</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SF15</td><td>SF14</td><td>SF13</td><td>SF12</td><td>SF11</td><td>SF10</td><td>SF9</td><td>SF8</td><td>SF7</td><td>SF6</td><td>SF5</td><td>SF4</td><td>SF3</td><td>SF2</td><td>SF1</td><td>SF0</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:0</td><td>SFx</td><td>信号量标志</td></tr><tr><td></td><td></td><td>硬件置位,软件置位HWSEM_INTC寄存器的SIFCx位来清零该位。</td></tr><tr><td></td><td></td><td>0:无信号量解锁事件发生</td></tr><tr><td></td><td></td><td>1:发生了一个信号量解锁事件</td></tr></table>

# 48.4.6. 中断状态寄存器（HWSEM_INTF）

地址偏移：0x10C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SIF31</td><td>SIF30</td><td>SIF29</td><td>SIF28</td><td>SIF27</td><td>SIF26</td><td>SIF25</td><td>SIF24</td><td>SIF23</td><td>SIF22</td><td>SIF21</td><td>SIF20</td><td>SIF19</td><td>SIF18</td><td>SIF17</td><td>SIF16</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SIF15</td><td>SIF14</td><td>SIF13</td><td>SIF12</td><td>SIF11</td><td>SIF10</td><td>SIF9</td><td>SIF8</td><td>SIF7</td><td>SIF6</td><td>SIF5</td><td>SIF4</td><td>SIF3</td><td>SIF2</td><td>SIF1</td><td>SIF0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SIFx</td><td>信号量中断标志位硬件置位,软件置位HWSEM_INTC寄存器的SIFCx位来清零该位。0:没有中断挂起1:有一个中断挂起</td></tr></table>

# 48.4.7. 解锁寄存器（HWSEM_UNLK）

地址偏移：0x140

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">MID[3:0]</td><td colspan="8">保留</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>KEY[15:0]</td><td>清零密钥只写,读为0。只有当该位域值与HWSEM_KEY寄存器的KEY[15:0]值相匹配时,才可解锁所有与该寄存器的MID[3:0]相匹配的信号量。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>MID[3:0]</td><td>要清零的信号量总线主控ID只写,读为0。指示将要解锁被该位域值的总线主控ID占有的所有信号量。</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 48.4.8. 键值寄存器（HWSEM_KEY）

地址偏移：0x144

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>KEY[15:0]</td><td>解锁键值,用于解锁某个总线主控ID占有的所有信号量。</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
