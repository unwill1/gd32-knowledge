## 15.4. CMP 寄存器

CMP 基地址：0x4001 7C00

## 15.4.1. CMP1 控制状态寄存器（CMP1_CS）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP1LK</td><td>CMP1O</td><td colspan="7">保留</td><td>CMP1MSEL[3]</td><td>保留</td><td colspan="3">CMP1BLK[2:0]</td><td colspan="2">保留</td></tr><tr><td>rwo</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMP1PL</td><td>保留</td><td colspan="4">CMP1OSEL[3:0]</td><td colspan="3">保留</td><td colspan="3">CMP1MSEL[2:0]</td><td colspan="3">保留</td><td>CMP1EN</td></tr><tr><td colspan="2">rw</td><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP1LK</td><td>CMP1写保护该位可将CMP1的各控制位设为只读,该位可写一次,通过系统复位清除,可通过软件置位。0: CMP1_CS是可读可写位1: CMP1_CS是只读位</td></tr><tr><td>30</td><td>CMP1O</td><td>CMP1输出该位反映CMP1输出状态,是只读位。0:同相输入端低于反相输入端,输出为低电平。1:同相输入端高于反相输入端,输出为高电平。</td></tr><tr><td>29:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>CMP1MSEL[3]</td><td>CMP1MSEL位域的位3见CMP1_CS的6:4位。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>CMP1BLK[2:0]</td><td>CMP1输出消隐源该位域用于选择哪个定时器输出控制CMP1的输出消隐。000:无消隐001:保留010:选择TIMER1_CH2输出比较信号为消隐源011:选择TIMER2_CH2输出比较信号为消隐源100~111:保留</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CMP1PL</td><td>CMP1 输出极性该位用于控制 CMP1 输出极性。0:输出是正相的1:输出是反相的</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>CMP1OSEL[2:0]</td><td>CMP1 的输出选择该位域用于控制 CMP1 输出选择。0000:无选择0001:定时器 0 中止输入0010~0110:保留0111:定时器 0 通道 0 输入捕获1000:定时器 1 通道 3 输入捕获1001:保留1010:定时器 2 通道 0 输入捕获1011~1111:保留注意:使用定时器捕获比较器的输出信号时,建议先使能 CMP,再配置定时器通道</td></tr><tr><td>9:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CMP1MSEL[2:0]</td><td>CMP1_IM 输入选择该位域结合位 22,用于选择 CMP1 的输入端 CMP1_IM 的输入源0000:VREFINT/40001:VREFINT/20010:VREFINT*3/40011:VREFINT0100:PA40101:PA50110:PA20111:DAC0_OUT01000:DAC1_OUT01001:DAC0_OUT11010~1111:保留</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CMP1EN</td><td>CMP1 使能0:CMP1 禁能1:CMP1 使能</td></tr></table>

## 15.4.2. CMP3 控制状态寄存器（CMP3_CS）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP3LK</td><td>CMP3O</td><td colspan="7">保留</td><td>CMP3MSEL[3]</td><td>保留</td><td colspan="3">CMP3BLK[2:0]</td><td colspan="2">保留</td></tr><tr><td>rwo</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMP3PL</td><td>保留</td><td colspan="4">CMP3OSEL[3:0]</td><td colspan="3">保留</td><td colspan="3">CMP3MSEL[2:0]</td><td colspan="3">保留</td><td>CMP3EN</td></tr><tr><td colspan="2">rw</td><td colspan="7">rw</td><td colspan="5">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP3LK</td><td>CMP3写保护该位可将CMP3的各控制位设为只读,该位可写一次,通过系统复位清除,可通过软件置位。0: CMP3_CS是可读可写位1: CMP3_CS是只读位</td></tr><tr><td>30</td><td>CMP3O</td><td>CMP3输出该位反映CMP3输出状态,是只读位。0:同相输入端低于反相输入端,输出为低电平。1:同相输入端高于反相输入端,输出为高电平。</td></tr><tr><td>29:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>CMP3MSEL[3]</td><td>CMP3MSEL位域的位3见CMP3_CS的6:4位。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>CMP3BLK[2:0]</td><td>CMP3输出消隐源该位域用于选择哪个定时器输出控制CMP3的输出消隐。000:无消隐001:选择TIMER2_CH3输出比较信号为消隐源010~111:保留</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CMP3PL</td><td>CMP3输出极性该位用于控制CMP3输出极性。0:输出是正相的1:输出是反相的</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>CMP3OSEL[2:0]</td><td>CMP3的输出选择该位域用于控制CMP3输出选择。0000:无选择0001:定时器0中止输入0010~0101:保留0110:定时器2通道2输入捕获0111:保留1000:定时器14通道1输入捕获1001~1111:保留注意:使用定时器捕获比较器的输出信号时,建议先使能CMP,再配置定时器通道</td></tr><tr><td>9:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CMP3MSEL[2:0]</td><td>CMP3_IM输入选择该位域结合位22,用于选择CMP3的输入端CMP3_IM的输入源。0000:VREFINT/40001:VREFINT/20010:VREFINT*3/40011:VREFINT0100:PA40101:PA50110:DAC0_OUT00111:PB21000:DAC1_OUT01001:DAC0_OUT11010~1111:保留</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CMP3EN</td><td>CMP3使能0:CMP3禁能1:CMP3使能</td></tr></table>

## 15.4.3. CMP5 控制状态寄存器（CMP5_CS）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP5LK</td><td>CMP5O</td><td colspan="7">保留</td><td>CMP5MSEL[3]</td><td>保留</td><td colspan="3">CMP5BLK[2:0]</td><td colspan="2">保留</td></tr><tr><td>rwo</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMP5PL</td><td>保留</td><td colspan="4">CMP5OSEL[3:0]</td><td colspan="3">保留</td><td colspan="3">CMP5MSEL[2:0]</td><td colspan="3">保留</td><td>CMP5EN</td></tr><tr><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP5LK</td><td>CMP5写保护该位可将CMP5的各控制位设为只读,该位可写一次,通过系统复位清除,可通过软件置位。0: CMP5_CS是可读可写位1: CMP5_CS是只读位</td></tr><tr><td>30</td><td>CMP5O</td><td>CMP5 输出该位反映 CMP5 输出状态,是只读位。0:同相输入端低于反相输入端,输出为低电平。1:同相输入端高于反相输入端,输出为高电平。</td></tr><tr><td>29:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>CMP5MSEL[3]</td><td>CMP5MSEL 位域的位 3见 CMP5_CS 的 6:4 位</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>CMP5BLK[2:0]</td><td>CMP5 输出消隐源该位域用于选择哪个定时器输出 CMP5 的输出消隐。000:无消隐001:保留010:保留011:选择 TIMER1_CH3 输出比较信号为消隐源100~111:保留</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CMP5PL</td><td>CMP5 输出极性该位用于控制 CMP5 输出极性。0:输出是正相的1:输出是反相的</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:10</td><td>CMP5OSEL[2:0]</td><td>CMP5 的输出选择该位域用于控制 CMP5 输出选择。0000:无选择0001:定时器 0 中止输入0010~0101:保留0110:定时器 1 通道 1 输入捕获0111~1001:保留1010:定时器 15 通道 0 输入捕获1011~1111:保留注意:使用定时器捕获比较器的输出信号时,建议先使能 CMP,再配置定时器通道</td></tr><tr><td>9:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CMP5MSEL[2:0]</td><td>CMP5_IM 输入选择该位域结合位 22,用于选择 CMP5 的输入端 CMP5_IM 的输入源。0000:<eq>V_{REFINT}</eq>/ 40001:<eq>V_{REFINT}</eq>/ 20010:<eq>V_{REFINT}</eq>* 3 / 40011:<eq>V_{REFINT}</eq>0100:PA40101: PA50110: DAC0_OUT00111: PB151000: DAC1_OUT01001: DAC0_OUT11010~1111: 保留</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CMP5EN</td><td>CMP5 使能0: CMP5 禁能1: CMP5 使能</td></tr></table>
