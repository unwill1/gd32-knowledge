# 44.4. 比较器寄存器

CMP 基地址：0x5800 3800

# 44.4.1. 状态寄存器（CMP_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>CMP1IF</td><td>CMP0IF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CMP1O</td><td>CMP0O</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>CMP1IF</td><td>CMP1中断标志位0:无CMP1中断发生1:CMP1中断发生当CMP1输出置位时,该位由硬件置1。软件写1至CMP_IFC寄存器CMP1IC位清0。</td></tr><tr><td>16</td><td>CMP0IF</td><td>CMP0中断标志位0:无CMP0中断发生1:CMP0中断发生当CMP0输出置位时,该位由硬件置1。软件写1至CMP_IFC寄存器CMP0IC位清0。</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMP1O</td><td>CMP1 输出该位反映 CMP1 输出状态,是只读位0:同相输入端低于反相输入端,输出为低电平1:同相输入端高于反相输入端,输出为高电平</td></tr><tr><td>0</td><td>CMP0O</td><td>CMP0 输出该位反映 CMP0 输出状态,是只读位0:同相输入端低于反相输入端,输出为低电平1:同相输入端高于反相输入端,输出为高电平</td></tr></table>

# 44.4.2. 中断标志位清除寄存器（CMP_IFC）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>CMP1IC</td><td>CMP0IC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>CMP1IC</td><td>CMP1中断标志位清除0:无清除中断标志位发生1:清除中断标志位</td></tr><tr><td>16</td><td>CMP0IC</td><td>CMP0中断标志位清除0:无清除中断标志位发生1:清除中断标志位</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 44.4.3. 备用选择寄存器（CMP_SR）

地址偏移： 0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">AFSE[10:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>AFSE[10:0]</td><td>CMP 备用输出端口选择,它们连接在 GPIO。对于每一位,选择 0 为 CMP0_OUT 与相应的备用功能,选择 1 为 CMP1_OUT 与相应的备用功能。位 0: PA6位 1: PA8位 2: PB12</td></tr></table>

位 3: PE6

位 4: PE15

位 5: PG2

位 6: PG3

位 7: PG4

位 8: PK0

位 9: PK1

位 10：PK2

# 44.4.4. CMP0 控制状态寄存器（CMP0_CS）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP0LK</td><td colspan="3">保留</td><td colspan="4">CMP0BLK[3:0]</td><td colspan="3">保留</td><td>CMP0PSEL</td><td>保留</td><td colspan="3">CMP0MSEL[2:0]</td></tr><tr><td colspan="4">rw</td><td colspan="6">rw</td><td colspan="3">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">CMP0M[1:0]</td><td colspan="2">保留</td><td colspan="2">CMP0HST[1:0]</td><td>保留</td><td>CMP0INTEN</td><td colspan="2">保留</td><td>CMP0PL</td><td>CMP0SEN</td><td>CMP0BEN</td><td>CMP0EN</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP0LK</td><td>CMP0写保护该位可将CMP0的各控制位设为只读。该位只可通过软件置位一次,通过系统复位清除。0: CMP0_CS是可读可写位1: CMP0_CS和CMP_SR是只读位</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>CMP0BLK[3:0]</td><td>CMP0输出消隐源该位域用于选择哪个定时器输出控制比较器0的输出消隐。0000:无消隐0001:选择TIMER0_CH0输出比较信号为消隐源0010:选择TIMER1_CH2输出比较信号为消隐源0011:选择TIMER2_CH2输出比较信号为消隐源0100:选择TIMER2_CH3输出比较信号为消隐源0101:选择TIMER7_CH0输出比较信号为消隐源0110:选择TIMER14_CH0输出比较信号为消隐源其它:保留。</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>CMP0PSEL</td><td>CMP0_IP输入选择该位用于选择CMP0的CMP0_IP输入源。0: PB01: PB2</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>CMP0MSEL[2:0]</td><td>CMP0_IM输入选择该位域用于选择CMP0的CMP0_IM输入源。000: VREFINT/4001: VREFINT/2010: VREFINT*3/4011: VREFINT100: DAC0_OUT0101: DAC0_OUT1110: PB1111: PC4</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>CMP0M[1:0]</td><td>CMP0模式该位域用于控制CMP0的运行模式以调整速度和功耗。00: 高速/全功耗01/10: 中速/中功耗11: 超低速/超低功耗</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CMP0HST[1:0]</td><td>CMP0迟滞该位域用于控制迟滞水平00: 无迟滞01: 低迟滞10: 中迟滞11: 高迟滞</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CMP0INTEN</td><td>CMP0中断使能0: 禁能1: 使能</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CMP0PL</td><td>CMP0输出极性该位用于控制CMP0输出极性0: 输出是正相的1: 输出是反相的</td></tr><tr><td>2</td><td>CMP0SEN</td><td>电压定标器使能位该位可通过软件置位和清除,可使能VREFINT分频器的输出,被视为CMP反相输</td></tr></table>

入端。

0：如果 CMP1_CS 的 CMP1SEN 位也复位，则禁用 VREFINT电压定标器

1：启用电压定标器

1 CMP0BEN 定标器使能位

0：如果 CMP1_CS 的 CMP1BEN 位也复位，则禁用定标器电阻桥

1：启用定标器电阻桥

0 CMP0EN CMP0 使能

0：CMP0 禁能

1：CMP0 使能

# 44.4.5. CMP1 控制状态寄存器（CMP1_CS）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP1LK</td><td colspan="3">保留</td><td colspan="4">CMP1BLK[3:0]</td><td colspan="3">保留</td><td>CMP1PSEL</td><td>保留</td><td colspan="3">CMP1MSEL[2:0]</td></tr><tr><td colspan="4">rw</td><td colspan="7">rw</td><td colspan="2">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">CMP1M[1:0]</td><td colspan="2">保留</td><td colspan="2">CMP1HST[1:0]</td><td>保留</td><td>CMP1INTEN</td><td>保留</td><td>WNDEN</td><td>CMP1PL</td><td>CMP1SEN</td><td>CMP1BEN</td><td>CMP1EN</td></tr><tr><td colspan="2"></td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>CMP1LK</td><td>CMP1写保护该位可将CMP1的各控制位设为只读。该位只可通过软件置位一次,通过系统复位清除。0: CMP1_CS是可读可写位1: CMP1_CS和CMP_SR是只读位</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>CMP1BLK[3:0]</td><td>CMP1输出消隐源该位域用于选择哪个定时器输出控制比较器0的输出消隐。0000:无消隐0001:选择TIMER0_CH0输出比较信号为消隐源0010:选择TIMER1_CH2输出比较信号为消隐源0011:选择TIMER2_CH2输出比较信号为消隐源0100:选择TIMER2_CH3输出比较信号为消隐源0101:选择TIMER7_CH0输出比较信号为消隐源0110:选择TIMER14_CH0输出比较信号为消隐源其它:保留。</td></tr></table>

23:21 保留 必须保持复位值。

20 CMP1PSEL CMP1_IP 输入选择

该位用于选择 CMP1 的 CMP1_IP 输入源。

0：PE9 

1：PE11 

19 保留 必须保持复位值。

18:16 CMP1MSEL[2:0] CMP1_IM 输入选择

该位域用于选择 CMP1 的 CMP1_IM 输入源。

000：VREFINT / 4 

001：VREFINT / 2 

010：VREFINT * 3 / 4 

011：VREFINT 

100：DAC0_OUT0 

101：DAC0_OUT1 

110：PE10 

111：PE7 

15:14 保留 必须保持复位值。

13:12 CMP1M[1:0] CMP1 模式

该位域用于控制 CMP1 的运行模式以调整速度和功耗。

00：高速 / 全功耗

01 / 10：中速 / 中功耗

11：超低速 / 超低功耗

11:10 保留 必须保持复位值。

9:8 CMP1HST[1:0] CMP1 迟滞

该位域用于控制迟滞水平

00：无迟滞

01：低迟滞

10：中迟滞

11：高迟滞

7 保留 必须保持复位值。

6 CMP1INTEN CMP1中断使能

0：禁能

1：使能

5 保留 必须保持复位值。

4 WNDEN 窗口模式使能

该位用来选择 CMP1_IP 输入源。

0：CMP1_IP 连接到 CMP1 的同相输入端

1：CMP1_IP连接到CMP0_IP

<table><tr><td>3</td><td>CMP1PL</td><td>CMP1 输出极性该位用于控制 CMP1 输出极性0:输出是正相的1:输出是反相的</td></tr><tr><td>2</td><td>CMP1SEN</td><td>电压定标器使能位该位可通过软件置位和清除,可使能 VREFINT 分频器的输出,被视为 CMP 反相输入端。0:如果 CMP0_CS 的 CMP0SEN 位也复位,则禁用 VREFINT 电压定标器1:启用电压定标器</td></tr><tr><td>1</td><td>CMP1BEN</td><td>定标器使能位0:如果 CMP0_CS 的 CMP0BEN 位也复位,则禁用定标器电阻桥1:启用定标器电阻桥</td></tr><tr><td>0</td><td>CMP1EN</td><td>CMP1 使能0:CMP1 禁能1:CMP1 使能</td></tr></table>
