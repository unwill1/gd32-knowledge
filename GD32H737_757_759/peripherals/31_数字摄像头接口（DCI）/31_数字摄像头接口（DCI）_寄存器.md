# 31.7. DCI 寄存器

DCI基地址：0x4802 0000

# 31.7.1. 控制寄存器（DCI_CTL）

偏移地址：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>EVSEN</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>AECEN</td><td>DCIEN</td><td>CCMOD</td><td>CCEN</td><td colspan="2">DCIF[1:0]</td><td colspan="2">FR[1:0]</td><td>VPS</td><td>HPS</td><td>CKS</td><td>ESM</td><td>JM</td><td>WDEN</td><td>SNAP</td><td>CAP</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>EVSEN</td><td>外部 Vsync 使能0:禁用外部 Vsync 模式1:使能外部 Vsync 模式仅适用于 CCIR 逐行扫描模式</td></tr><tr><td>15</td><td>AECEN</td><td>自动纠错使能,1bit 纠错0:禁能自动纠错1:使能自动纠错仅适用于 CCIR 隔行扫描模式</td></tr><tr><td>14</td><td>DCIEN</td><td>DCI 使能0:DCI 禁止1:DCI 使能</td></tr><tr><td>13</td><td>CCMOD</td><td>CCIR 模式选择0:CCIR 逐行模式1:CCIR 隔行模式</td></tr><tr><td>12</td><td>CCEN</td><td>CCIR 使能0:禁能 CCIR1:使能 CCIR</td></tr><tr><td>11:10</td><td>DCIF[1:0]</td><td>DCI 数据格式00:每个像素时钟捕获8位数据01:每个像素时钟捕获10位数据10:每个像素时钟捕获12位数据</td></tr></table>

11：每个像素时钟捕获 14 位数据

<table><tr><td>9:8</td><td>FR[1:0]</td><td>帧频率在连续捕获模式,FR定义帧捕获频率00:捕获所有帧01:每隔一帧捕获一次10:每隔三帧捕获一次11:保留</td></tr><tr><td>7</td><td>VPS</td><td>垂直同步极性选择0:消隐期间低电平1:消隐期间高电平</td></tr><tr><td>6</td><td>HPS</td><td>水平同步极性选择0:消隐期间低电平1:消隐期间高电平</td></tr><tr><td>5</td><td>CKS</td><td>时钟极性选择0:下降沿捕获1:上升沿捕获</td></tr><tr><td>4</td><td>ESM</td><td>内嵌码同步模式0:禁止内嵌码同步模式1:使能内嵌码同步模式</td></tr><tr><td>3</td><td>JM</td><td>JPEG子模式0:禁止JPEG子模式1:使能JPEG子模式</td></tr><tr><td>2</td><td>WDEN</td><td>窗口使能0:禁止窗口功能1:使能窗口功能</td></tr><tr><td>1</td><td>SNAP</td><td>快照模式0:连续捕获模式1:快照模式</td></tr><tr><td>0</td><td>CAP</td><td>使能捕获0:禁止帧捕获1:使能帧捕获</td></tr></table>

# 31.7.2. 状态寄存器 0（DCI_STAT0）

地址偏移：0x04

复位值：0x0000 0003

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>FV</td><td>VS</td><td>HS</td></tr><tr><td colspan="13"></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>FV</td><td>FIFO 有效0: FIFO 没有有效像素数据1: FIFO 中像素数据有效</td></tr><tr><td>1</td><td>VS</td><td>VS 引脚状态0: 不在垂直消隐期间1: 处于垂直消隐期间</td></tr><tr><td>0</td><td>HS</td><td>HS 引脚状态0: 不在水平消隐期间1: 处于水平消隐期间</td></tr></table>

# 31.7.3. 状态寄存器 1（DCI_STAT1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CCEF</td><td>COFF</td><td>F1F</td><td>F0F</td><td>ELF</td><td>VSF</td><td>ESEF</td><td>OVRF</td><td>EFF</td></tr><tr><td colspan="7"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CCEF</td><td>CCIR 错误标志0:没有错误出现1:在 SVA 或 EVA 码上检测到错误仅适用于 CCIR 隔行扫描模式</td></tr><tr><td>7</td><td>COFF</td><td>CCIR 场改变标志0:没有场的改变事件出现1:场发生了改变</td></tr></table>

仅适用于 CCIR 隔行扫描模式

6 F1F CCIR 场 1

0：当前不是场 1

1：当前是场 1

仅适用于 CCIR 隔行扫描模式（在当前场不匹配时自动清除）

5 F0F CCIR 场 0

0：当前不是场 0

1：当前是场 0

仅适用于 CCIR 隔行扫描模式（在当前场不匹配时自动清除）

4 ELF 行结束标志

0：没有行结束标志

1：DCI 捕获到一行

3 VSF 垂直同步标志

0：没有垂直同步标志

1：检测到垂直同步消隐

2 ESEF 内嵌码同步错误标志

0：没有内嵌码同步错误标志

1：检测到内嵌码同步错误

1 OVRF FIFO 溢出标志

0：没有 FIFO 溢出

1：发生 FIFO 溢出

0 EFF 帧结束标志

0：没有帧结束标志

1：帧被 DCI 捕获

# 31.7.4. 中断使能寄存器（DCI_INTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CCEIE</td><td>COFIE</td><td>F1IE</td><td>F0IE</td><td>ELIE</td><td>VSIE</td><td>ESEIE</td><td>OVRIE</td><td>EFIE</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

位/位域 名称 描述

31:9 保留 必须保持复位值。

<table><tr><td>8</td><td>CCEIE</td><td>CCIR 错误中断使能0: CCIR 错误标志不会产生中断1: CCIR 错误标志会产生中断</td></tr><tr><td>7</td><td>COFIE</td><td>场中断使能的 CCIR 变化0: CCIR 场标志变化不会产生中断1: CCIR 场标志变化将产生中断</td></tr><tr><td>6</td><td>F1IE</td><td>CCIR 场 1 中断使能0: CCIR 场 1 标志不会产生中断1: CCIR 场 1 标志将产生中断</td></tr><tr><td>5</td><td>FOIE</td><td>CCIR 场 0 中断使能0: CCIR 场 0 不会产生中断1: CCIR 场 0 标志将产生中断</td></tr><tr><td>4</td><td>ELIE</td><td>行结束中断使能0: 行结束标志不产生中断1: 行结束标志产生中断</td></tr><tr><td>3</td><td>VSIE</td><td>垂直同步中断使能0: 垂直同步标志不产生中断1: 垂直同步标志产生中断</td></tr><tr><td>2</td><td>ESEIE</td><td>内嵌码同步错误中断使能0: 内嵌码同步错误标志不产生中断1: 内嵌码同步错误标志产生中断</td></tr><tr><td>1</td><td>OVRIE</td><td>FIFO 溢出中断使能0: FIFO 溢出不产生中断1: FIFO 溢出产生中断</td></tr><tr><td>0</td><td>EFIE</td><td>帧结束中断使能0: 帧结束标志不产生中断1: 帧结束标志产生中断</td></tr></table>

# 31.7.5. 中断标志寄存器（DCI_INTF）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CCEIF</td><td>COFIF</td><td>F1IF</td><td>F0IF</td><td>ELIF</td><td>VSIF</td><td>ESEIF</td><td>OVRIF</td><td>EFIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CCEIF</td><td>CCIR 错误中断标志仅适用于 CCIR 隔行扫描模式,在 SVA 或 EVA 代码上发现错误。</td></tr><tr><td>7</td><td>COFIF</td><td>场中断标志的 CCIR 变化仅适用于 CCIR 隔行扫描模式</td></tr><tr><td>6</td><td>F1IF</td><td>CCIR 场 1 中断标志仅适用于 CCIR 隔行扫描模式(当前场不匹配时自动清零)</td></tr><tr><td>5</td><td>F0IF</td><td>CCIR 场 0 中断标志仅适用于 CCIR 隔行扫描模式(当前场不匹配时自动清零)</td></tr><tr><td>4</td><td>ELIF</td><td>行结束中断标志</td></tr><tr><td>3</td><td>VSMF</td><td>垂直同步中断标志</td></tr><tr><td>2</td><td>ESEMF</td><td>内嵌码同步错误中断标志</td></tr><tr><td>1</td><td>OVRMF</td><td>FIFO 溢出中断标志</td></tr><tr><td>0</td><td>EFMF</td><td>帧结束中断标志</td></tr></table>

# 31.7.6. 中断标志清除寄存器（DCI_INTC）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CCEFC</td><td>COFFC</td><td>F1IF</td><td>F0IF</td><td>ELFC</td><td>VSFC</td><td>ESEFC</td><td>OVRFC</td><td>EFFC</td></tr><tr><td colspan="7"></td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CCEFC</td><td>CCIR 错误标志清除写 1 清除 CCIR 错误标志</td></tr><tr><td>7</td><td>COFFC</td><td>CCIR 场转换标志清除写 1 清除 CCIR 场转换标志</td></tr><tr><td>6</td><td>F1FC</td><td>CCIR 场 1 中断标志清除</td></tr></table>

写 1 清除 CCIR 场1 中断标志

<table><tr><td>5</td><td>F0FC</td><td>CCIR场0中断标志写1清除CCIR场0中断标志</td></tr><tr><td>4</td><td>ELFC</td><td>行结束中断标志清除写1清除行结束中断标志</td></tr><tr><td>3</td><td>VSFC</td><td>垂直同步标志清除写1清除垂直同步标志</td></tr><tr><td>2</td><td>ESEFC</td><td>内嵌码同步错误标志清除写1清除内嵌码同步错误标志</td></tr><tr><td>1</td><td>OVRFC</td><td>FIFO溢出标志清除写1清除FIFO溢出标志</td></tr><tr><td>0</td><td>EFFC</td><td>帧结束中断标志清除写1清除帧结束中断标志</td></tr></table>

# 31.7.7. 同步码寄存器（DCI_SC）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">FE[7:0]</td><td colspan="8">LE[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">LS[7:0]</td><td colspan="8">FS[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>FE[7:0]</td><td>内嵌同步模式的帧结束码</td></tr><tr><td>23:16</td><td>LE[7:0]</td><td>内嵌同步模式的行结束码</td></tr><tr><td>15:8</td><td>LS[7:0]</td><td>内嵌同步模式的行开始码</td></tr><tr><td>7:0</td><td>FS[7:0]</td><td>内嵌同步模式的帧开始码</td></tr></table>

# 31.7.8. 同步码屏蔽寄存器（DCI_SCUMSK）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">FEM[7:0]</td><td colspan="8">LEM[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">LSM[7:0]</td><td colspan="8">FSM[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>FEM[7:0]</td><td>内嵌码同步模式下非屏蔽帧结束码</td></tr><tr><td>23:16</td><td>LEM[7:0]</td><td>内嵌码同步模式下非屏蔽行结束码</td></tr><tr><td>15:8</td><td>LSM[7:0]</td><td>内嵌码同步模式下非屏蔽行开始码</td></tr><tr><td>7:0</td><td>FSM[7:0]</td><td>内嵌码同步模式下非屏蔽帧开始码</td></tr></table>

# 31.7.9. 剪裁窗口开始位置寄存器（DCI_CWSPOS）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="13">WVSP[12:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">WHSP[13:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:16</td><td>WVSP[12:0]</td><td>窗口垂直开始位置值为0表示着第一行,以此类推</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:0</td><td>WHSP[13:0]</td><td>窗口水平开始位置值为0表示着第一个像素时钟,以此类推</td></tr></table>

# 31.7.10. 剪裁窗口大小寄存器（DCI_CWSZ）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="14">WVSZ[13:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">WHSZ[13:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29:16</td><td>WVSZ[13:0]</td><td>窗口垂直大小WVSZ=X表示X+1行</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13:0</td><td>WHSZ[13:0]</td><td>窗口水平大小WHSZ=X表示某一行有X+1个像素时钟</td></tr></table>

# 31.7.11. 数据寄存器（DCI_DATA）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DT3[7:0]</td><td colspan="8">DT2[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DT1[7:0]</td><td colspan="8">DT0[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DT3[7:0]</td><td>像素字节 3</td></tr><tr><td>23:16</td><td>DT2[7:0]</td><td>像素字节 2</td></tr><tr><td>15:8</td><td>DT1[7:0]</td><td>像素字节 1</td></tr><tr><td>7:0</td><td>DT0[7:0]</td><td>像素字节 0</td></tr></table>
