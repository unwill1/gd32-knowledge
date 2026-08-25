# 41.6. EDOUT 寄存器

EDOUT 基地址：0x4001 8800

# 41.6.1. 控制寄存器（EDOUT_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>POL</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>POL</td><td>B相工作极性该位用于选择B相输出信号极性。如果EDOUT_ENABLE寄存器的EDOUTEN位为0,则该位的设置会反映在B相输出。否则,此位设置无效。0:工作极性为正向1:工作极性为反向</td></tr></table>

# 41.6.2. 使能寄存器（EDOUT_ENABLE）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EDOUTENrw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EDOUTEN</td><td>EDOUT 使能位</td></tr></table>

当该位设置为0 时，EDOUT_LCNT寄存器配置完成后，AB 相会立即输出相对应的状态，Z 相输出值为0。当该位设置为1 时，EDOUT 启动并输出AB 相和Z相信号。

0：禁止 EDOUT

1：使能 EDOUT

# 41.6.3. 位置寄存器（EDOUT_LOC）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LOCMAX[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>LOCMAX[15:0]</td><td>最大位置通过该位域设置一次旋转的最大位置。最大位置必须为4的倍数。如果最大位置为“4×M”,则在此寄存器中设置“4×M-1”。当EDOUT_ENABLE寄存器的EDOUTEN位从0更改为1时,该位域设置生效。0x0000~0x000E:保留0x000F:最大位置为16...0xyyyy:最大位置为0xyyyy+1</td></tr></table>

# 41.6.4. 输出计数器寄存器（EDOUT_OCNT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PDC[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">EDGC[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>PDC[15:0]</td><td>相位差该位域设置下一更新周期A相与B相信号之间的相位差。设定值的允许范围为2至65535,单位为<eq>T_{PCLK}</eq>。当EDGC位域设置为0时,将该位域设置为65535;当不为0时,将其设置为“更新周期/<eq>T_{PCLK}</eq>/EDGC的绝对值”(向下舍入)。当EDOUT运行时(即EDOUT_ENABLE寄存器的EDOUTEN位为1),请确保在下一个更新周期事件之前设置该位域。</td></tr><tr><td>15:0</td><td>EDGC[15:0]</td><td>边沿数量该位域设置下一更新周期的A相与B相信号的边沿数量。如果使用反方向旋转,需要设置为二进制补码表示的负值,值的允许范围为-32767(0x8001)到32767(0x7FFF)。该位域的绝对值不得大于“更新周期/(2*<eq>T_{PCLK}</eq>)”。当EDOUT运行时(即EDOUT_ENABLE寄存器中的EDOUTEN位为1),请确保在下一个更新周期事件之前设置该位域。</td></tr></table>

# 41.6.5. 位置计数寄存器（EDOUT_LCNT）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LOCCNT[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>LOCCNT[15:0]</td><td>当前位置该位域用在EDOUT停止时(即EDOUT_ENABLE寄存器的EDOUTEN位为0),设置当前位置(设置范围为0到LOCMAX)。当前位置设置完成后,A相和B相会立即输出相应状态。当EDOUT运行时(即EDOUT_ENABLE寄存器的EDOUTEN位为1),这些位反映出与A相和B相输出相关的位置变化。</td></tr></table>

# 41.6.6. Z 相配置寄存器（EDOUT_ZCR）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>ZOMD</td><td colspan="8">ZOWH[7:0]</td></tr><tr><td colspan="7"></td><td colspan="4">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ZOSP[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>ZOMD</td><td>Z相输出模式0:当前位置决定输出1:边沿序号决定输出</td></tr><tr><td>23:16</td><td>ZOWH[7:0]</td><td>Z相输出宽度</td></tr><tr><td>15:0</td><td>ZOSP[15:0]</td><td>Z相输出起始位置</td></tr></table>
