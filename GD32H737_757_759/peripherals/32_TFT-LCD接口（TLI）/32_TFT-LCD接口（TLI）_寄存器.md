# 32.7. TLI 寄存器

TLI基地址：0x5000 1000

# 32.7.1. 同步脉冲宽度寄存器（TLI_SPSZ）

偏移地址：0x08

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">HPSZ[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">VPSZ[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>HPSZ[11:0]</td><td>水平同步脉冲宽度HPSZ值应该配置成水平同步脉冲像素的个数减1。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>VPSZ[11:0]</td><td>垂直同步脉冲宽度VPSZ值应该配置成垂直同步脉冲像素的个数减1。</td></tr></table>

# 32.7.2. 后沿宽度寄存器（TLI_BPSZ）

偏移地址：0x0C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">HBPSZ[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">VBPSZ[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>HBPSZ[11:0]</td><td>水平后沿加同步脉冲的宽度HBPSZ值应该配置成水平后沿像素个数加同步脉冲像素个数减1。</td></tr></table>

15:12 保留 必须保持复位值。

11:0 VBPSZ[11:0] 垂直后沿加同步脉冲的宽度

VBPSZ 值应该配置成垂直后沿像素个数加同步脉冲像素个数减 1。

# 32.7.3. 有效宽度寄存器（TLI_ASZ）

偏移地址：0x10

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">HASZ[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">VASZ[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>HASZ[11:0]</td><td>水平有效宽度加后沿像素和水平同步像素宽度 HASZ值应该配置成水平有效宽度加后沿像素和水平同步像素个数减1。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>VASZ[11:0]</td><td>垂直有效宽度加后沿像素和垂直同步像素宽度 VASZ值应该配置成垂直有效宽度加后沿像素和垂直同步像素个数减1。</td></tr></table>

# 32.7.4. 总宽度寄存器（TLI_TSZ）

偏移地址：0x14

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">HTSZ[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">VTSZ[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>HTSZ[11:0]</td><td>显示器的水平总宽度,包括有效宽度,后沿,同步脉冲和前沿HTSZ值应该配置成水平有效宽度像素的个数加后沿像素,前沿像素和同步脉冲像素</td></tr></table>


减 1。


<table><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>VTSZ[11:0]</td><td>显示器的垂直总宽度,包括有效宽度,后沿,同步脉冲和前沿VTSZ值应该配置成垂直有效宽度像素的个数加后沿像素,前沿像素和同步脉冲像素减1。</td></tr></table>

# 32.7.5. 控制寄存器（TLI_CTL）

偏移地址：0x18

复位值：0x0000 2220


该寄存器只能按字(32位)访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>HPPS</td><td>VPPS</td><td>DEPS</td><td>CLKPS</td><td colspan="11">保留</td><td>DFEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">RDB[2:0]</td><td>保留</td><td colspan="3">GDB[2:0]</td><td>保留</td><td colspan="3">BDB[2:0]</td><td colspan="3">保留</td><td>TLIEN</td></tr><tr><td></td><td colspan="3">r</td><td colspan="4">r</td><td colspan="7">r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>HPPS</td><td>水平脉冲极性选择0: 水平同步脉冲低电平有效1: 水平同步脉冲高电平有效</td></tr><tr><td>30</td><td>VPPS</td><td>垂直脉冲极性选择0: 垂直同步脉冲低电平有效1: 垂直同步脉冲高电平有效</td></tr><tr><td>29</td><td>DEPS</td><td>非数据使能极性选择0: 非数据使能低电平有效1: 非数据使能高电平有效</td></tr><tr><td>28</td><td>CLKPS</td><td>像素时钟极性选择0: 像素时钟是 TLI 时钟1: 像素时钟是 TLI 时钟翻转</td></tr><tr><td>27:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>DFEN</td><td>抖动功能使能0: 禁止抖动功能1: 使能抖动功能</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>RDB[2:0]</td><td>红色通道抖动位数固定为 2, 只读</td></tr></table>

<table><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:8</td><td>GDB[2:0]</td><td>绿色通道抖动位数固定为2,只读</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>BDB[2:0]</td><td>绿色通道抖动位数固定为2,只读</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>TLIEN</td><td>TLI使能位0:禁止TLI1:使能TLI</td></tr></table>

# 32.7.6. 重载层配置寄存器（TLI_RL）

偏移地址：0x24

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>FBR</td><td>RQR</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>FBR</td><td>帧消隐重载请求此位通过软件置位,在重载之后由硬件清除。0:禁止重载1:层配置将在帧消隐时被重载进入真正寄存器。</td></tr><tr><td>0</td><td>RQR</td><td>立即重载请求此位通过软件置位,在重载之后由硬件清除。0:禁止重载1:层配置将在该位置位之后被重载进入真正寄存器。</td></tr></table>

# 32.7.7. 背景色配置寄存器（TLI_BGC）

偏移地址：0x2C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">BVR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">BVG[7:0]</td><td colspan="8">BVB[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>BVR[7:0]</td><td>背景红色值</td></tr><tr><td>15:8</td><td>BVG[7:0]</td><td>背景绿色值</td></tr><tr><td>7:0</td><td>BVB[7:0]</td><td>背景蓝色值</td></tr></table>

# 32.7.8. 中断使能寄存器（TLI_INTEN）

偏移地址：0x34

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>LCRIE</td><td>TEIE</td><td>FEIE</td><td>LMIE</td></tr><tr><td colspan="12"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>LCRIE</td><td>层配置重载中断使能0: 层配置重载标志将不产生中断1: 层配置重载标志将产生中断</td></tr><tr><td>2</td><td>TEIE</td><td>传输错误中断使能0: 传输错误标志将不产生中断1: 传输错误标志将产生中断</td></tr><tr><td>1</td><td>FEIE</td><td>FIFO 错误中断使能0: FIFO 错误标志将不产生中断1: FIFO 错误标志将产生中断</td></tr><tr><td>0</td><td>LMIE</td><td>行标记中断使能0: 行标记标志将不产生中断1: 行标记标志将产生中断</td></tr></table>

# 32.7.9. 中断标志寄存器（TLI_INTF）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>LCRF</td><td>TEF</td><td>FEF</td><td>LMF</td></tr></table>


r 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>LCRF</td><td>层配置重载标志0:无层配置重载标志出现1:由 TLI_RL 寄存器的 FBR 位置位触发了层配置重载</td></tr><tr><td>2</td><td>TEF</td><td>传输错误标志0:无传输错误1:一个传输错误在 AXI 总线上出现</td></tr><tr><td>1</td><td>FEF</td><td>FIFO 错误标志0:无 FIFO 错误标志1:出现 FIFO 下溢错误</td></tr><tr><td>0</td><td>LMF</td><td>行标记标志0:没有行标记标志1:行数达到 TLI_LM 寄存器中设置的特定值</td></tr></table>

# 32.7.10. 中断标志清除寄存器（TLI_INTC）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>LCRC</td><td>TEC</td><td>FEC</td><td>LMC</td></tr></table>


w w w w 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>LCRC</td><td>层配置重载标志清除写1清除层配置重载标志</td></tr><tr><td>2</td><td>TEC</td><td>传输错误标志清除写1清除传输错误标志</td></tr><tr><td>1</td><td>FEC</td><td>FIFO错误标志清除写1清除FIFO错误标志</td></tr><tr><td>0</td><td>LMC</td><td>行标记标志清除写1清除行标记标志</td></tr></table>

# 32.7.11. 行标记寄存器（TLI_LM）

地址偏移: 0x40

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">LM[10:0]</td></tr><tr><td colspan="16">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>LM[10:0]</td><td>行标记值当行数到达该值,TLI_INTF 寄存器的 LMF 位将置位。</td></tr></table>

# 32.7.12. 当前像素位置寄存器（TLI_CPPOS）

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">HPOS[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">VPOS[15:0]</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:16</td><td>HPOS[15:0]</td><td>水平位置</td></tr><tr><td></td><td></td><td>当前显示的像素的水平位置</td></tr><tr><td>15:0</td><td>VPOS[15:0]</td><td>垂直位置</td></tr><tr><td></td><td></td><td>当前显示的像素的垂直位置</td></tr></table>

# 32.7.13. 状态寄存器（TLI_STAT）

地址偏移：0x48

复位值：0x0000 000F

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>HS</td><td>VS</td><td>HDE</td><td>VDE</td></tr></table>


r 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>HS</td><td>TLI当前的HS状态</td></tr><tr><td>2</td><td>VS</td><td>TLI当前的VS状态</td></tr><tr><td>1</td><td>HDE</td><td>当前的HDE状态0: TLI_CPPOS寄存器HPOS并未位于TLI_BPSZ寄存器HBPSZ与TLI_ASZ寄存器HASZ之间1: TLI_CPPOS寄存器HPOS位于TLI_BPSZ寄存器HBPSZ与TLI_ASZ寄存器HASZ之间</td></tr><tr><td>0</td><td>VDE</td><td>当前的VDE状态0: TLI_CPPOS寄存器VPOS并未位于TLI_BPSZ寄存器VBPSZ与TLI_ASZ寄存器HASZ之间1: TLI_CPPOS寄存器VPOS位于TLI_BPSZ寄存器VBPSZ与TLI_ASZ寄存器VASZ之间</td></tr></table>

# 32.7.14. 第 x 层控制寄存器（TLI_LxCTL）（x = 0, 1）

地址偏移：0x84 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td>LUTEN</td><td>保留</td><td></td><td>CKEYEN</td><td>LEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>LUTEN</td><td>LUT使能0:禁止 LUT1:使能 LUT</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CKEYEN</td><td>色键使能0:禁止色键功能1:使能色键功能</td></tr><tr><td>0</td><td>LEN</td><td>层使能0:禁止层1:使能层</td></tr></table>

# 32.7.15. 第 x 层水平位置参数寄存器 $\left( \mathbf { \bar { T } L } \mathbf { l } \underline { { \mathbf { \Pi } } } \ll \mathbf { L } \mathbf { \times } \mathbf { H } \mathbf { P } \mathbf { O } \pmb { \mathbb { S } } \right) \ \left( \mathbf { \ x { x } } = \mathbf { 0 } , \mathbf { 1 } \right)$

偏移地址：0x88 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">WRP[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WLP[11:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>WRP[11:0]</td><td>窗口右侧位置</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WLP[11:0]</td><td>窗口左侧位置</td></tr></table>

# 32.7.16. 第 x 层垂直位置参数寄存器 $\left( \mathbf { \mathsf { T L } } \mathbf { \mathsf { L } } \mathbf { \mathsf { L X } } \mathbf { \mathsf { V P O S } } \right) \left( \mathbf { \mathsf { x } } = \mathbf { 0 } , \mathbf { 1 } \right)$

地址偏移：0x8C + 0x80 * x

复位值：0x0000 0000


该寄存器只能按字(32位)访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">WBP[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WTP[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:16</td><td>WBP[11:0]</td><td>窗口底部位置</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WTP[11:0]</td><td>窗口顶部位置</td></tr></table>

# 32.7.17. 第 x 层色键值寄存器（TLI_LxCKEY）（x = 0, 1）

地址偏移：0x90 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">CKEYR[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">CKEYG[7:0]</td><td colspan="8">CKEYB[7:0]</td></tr><tr><td colspan="8">Rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>CKEYR [7:0]</td><td>色键红色值</td></tr><tr><td>15:8</td><td>CKEYG [7:0]</td><td>色键绿色值</td></tr><tr><td>7:0</td><td>CKEYB [7:0]</td><td>色键蓝色值</td></tr></table>

注意：如果某层的像素RGB等于TLI_LxCKEY寄存器定义的值，该像素RGB值复位为0。这意味着这些像素对其它层来说是透明的。

# 32.7.18. 第 x 层像素格式寄存器（TLI_LxPPF）（x = 0, 1）

地址偏移：0x94 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">PPF[2:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>PPF[2:0]</td><td>像素格式这些位配置像素格式000: ARGB8888001: RGB888010: RGB565011: ARGB1555100: ARGB4444101: L8110: AL44111: AL88</td></tr></table>

# 32.7.19. 第 x 层恒定 Alpha 寄存器 $( \mathbf { T L } | \mathbf { \Delta } \mathbf { \_ } \mathbf { L x S A } ) \mathbf { \Delta } ( \mathbf { x } = \mathbf { 0 } , 1 )$

地址偏移： $0 { \times } 9 8 + 0 { \times } 8 0 ^ { \star } \times$ 

复位值：0x0000 00FF

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">SA[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>SA[7:0]</td><td>恒定 Alpha可用于计算混合因子。</td></tr></table>

# 32.7.20. 第 x 层默认颜色寄存器（TLI_LxDC）（x = 0, 1）

地址偏移：0x9C + 0x80 * x

复位：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DCA[7:0]</td><td colspan="8">DCR[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DCG[7:0]</td><td colspan="8">DCB[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DCA[7:0]</td><td>默认颜色 ALPHA</td></tr><tr><td>23:16</td><td>DCR[7:0]</td><td>默认颜色红色</td></tr><tr><td>15:8</td><td>DCG[7:0]</td><td>默认颜色绿色</td></tr><tr><td>7:0</td><td>DCB[7:0]</td><td>默认颜色蓝色</td></tr></table>


注意：当该层被禁止或TLI_LxHPOS和TLI_LxVPOS定义的窗口之外，默认颜色值生效。


# 32.7.21. 第 x 层混合寄存器（TLI_LxBLEND）（x = 0, 1）

地址偏移：0xA0 + 0x80 * x

复位值：0x0000 0607

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="3">ACF1[2:0]</td><td colspan="5">保留</td><td colspan="3">ACF2[2:0]</td></tr><tr><td colspan="13">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:8</td><td>ACF1[2:0]</td><td>Alpha 混合因子 1 计算方法000:保留001:保留010:保留011:保留100:归一化的恒定 Alpha101:保留110:归一化的像素 Alpha 乘以归一化的恒定 Alpha111:保留</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>ACF2[2:0]</td><td>Alpha 混合因子 2 计算方法000:保留</td></tr></table>

001：保留

010：保留

011：保留

100：保留

101：1-归一化的恒定 Alpha

110：保留

111：1-归一化的像素 Alpha 乘以归一化的恒定 Alpha

# 32.7.22. 第 x 层帧基地址寄存器（TLI_LxFBADDR）（x = 0, 1）

地址偏移： $0 \times \mathsf { A C } + 0 \times 8 0 \sp \star \mathsf { x }$ 

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">FBADD[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FBADD[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FBADD[31:0]</td><td>帧缓冲区基地址</td></tr><tr><td></td><td></td><td>帧缓冲区基地址</td></tr></table>

# 32.7.23. 第 x 层行长度寄存器（TLI_LxFLLEN）（x = 0, 1）

地址偏移：0xB0 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="14">STDOFF[13:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">FLL[13:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:16</td><td>STDOFF[13:0]</td><td>步幅偏移这个值定义了从某行起始处到下一行起始处之间的字节数</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>13:0</td><td>FLL[13:0]</td><td>行长度</td></tr><tr><td></td><td></td><td>这个值为一行的字节数+7</td></tr></table>

# 32.7.24. 第 x 层总行数寄存器（TLI_LxFTLN）（x = 0, 1）

地址偏移：0xB4 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">FTLN[10:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>FTLN[10:0]</td><td>总行数这个值定义了一帧行数</td></tr></table>

# 32.7.25. 第 x 层颜色查找表寄存器（TLI_LxLUT）（x = 0, 1）

地址偏移：0xC4 + 0x80 * x

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">TADD [7:0]</td><td colspan="8">TR[7:0]</td></tr><tr><td colspan="8">w</td><td colspan="8">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">TG[7:0]</td><td colspan="8">TB[7:0]</td></tr><tr><td colspan="8">w</td><td colspan="8">w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>TADD[7:0]</td><td>颜色查找表写地址颜色查找表位于该地址的节点的值,将由写入的TR,TG和TB值更新。</td></tr><tr><td>23:16</td><td>TR[7:0]</td><td>LUT节点的红色值</td></tr><tr><td>15:8</td><td>TG[7:0]</td><td>LUT节点的绿色值</td></tr><tr><td>7:0</td><td>TB[7:0]</td><td>LUT节点的蓝色值</td></tr></table>
