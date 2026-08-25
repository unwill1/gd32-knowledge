## 18.4. CMP 寄存器

CMP 基地址：0x4001 7C00

## 18.4.1. CMP0 控制状态寄存器（CMP0_CS）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP0LK</td><td>CMP00</td><td colspan="6">保留</td><td>CMP0SEN</td><td>CMP0BEN</td><td>保留</td><td colspan="3">CMP0BLK[2:0]</td><td colspan="2">CMP0HST[1:0]</td></tr><tr><td>rwo</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMP0PL</td><td colspan="3">保留</td><td>CMP0SW</td><td colspan="4">保留</td><td colspan="3">CMP0MSEL[2:0]</td><td colspan="2">CMP0M[1:0]</td><td>保留</td><td>CMP0EN</td></tr><tr><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP0LK</td><td>CMP0写保护该位可将CMP0的各控制位设为只读,该位可写一次,通过系统复位清除,可通过软件置位。0: CMP0_CS[31:0]是可读可写位1: CMP0_CS[31:0]是只读位</td></tr><tr><td>30</td><td>CMP0O</td><td>CMP0输出该位反映CMP0输出状态,是只读位。0:同相输入端低于反相输入端,输出为低电平。1:同相输入端高于反相输入端,输出为高电平。</td></tr><tr><td>29:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CMP0SEN</td><td>电压标量使能位该位可通过软件置位和清除,可使能<eq>V_{REFINT}</eq>分频器的输出,被视为反相输入端。0:在CMP1_CS寄存器CMP1SEN位为0的情景下,除能带隙标量。1:使能带隙标量</td></tr><tr><td>22</td><td>CMP0BEN</td><td>标量桥接使能位0:在CMP1_CS寄存器CMP1BEN位为0的情景下,除能标量电阻桥接功能。1:使能标量电阻桥接功能</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>CMP0BLK[2:0]</td><td>CMP0输出消隐源该位域用于选择哪个定时器输出控制CMP0的输出消隐。000:无消隐001:选择TIMER0_CH1输出比较信号为消隐源010:选择TIMER2_CH1输出比较信号为消隐源</td></tr></table>

<table><tr><td rowspan="4"></td><td rowspan="4"></td><td>011:保留</td></tr><tr><td>100:选择TIMER13_CH0输出比较信号为消隐源</td></tr><tr><td>101:选择TIMER15_CH0输出比较信号为消隐源</td></tr><tr><td>110~111:保留</td></tr><tr><td rowspan="6">17:16</td><td rowspan="6">CMP0HST[1:0]</td><td>CMP0迟滞</td></tr><tr><td>该位域用于控制迟滞水平。</td></tr><tr><td>00:无迟滞</td></tr><tr><td>01:低迟滞</td></tr><tr><td>10:中迟滞</td></tr><tr><td>11:高迟滞</td></tr><tr><td rowspan="4">15</td><td rowspan="4">CMP0PL</td><td>CMP0输出极性</td></tr><tr><td>该位用于控制输出极性。</td></tr><tr><td>0:输出是正相的</td></tr><tr><td>1:输出是反相的</td></tr><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td rowspan="4">11</td><td rowspan="4">CMP0SW</td><td>CMP0开关模式</td></tr><tr><td>该位用于开关CMP0同相输入端PA1与PB2之间的连接。</td></tr><tr><td>0:开关模式禁能</td></tr><tr><td>1:开关模式使能</td></tr><tr><td>10:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td rowspan="10">6:4</td><td rowspan="10">CMP0MSEL[2:0]</td><td>CMP0_IM输入选择</td></tr><tr><td>该位域用于选择CMP0的输入端CMP0_IM的输入源。</td></tr><tr><td>000:VREFINT/4</td></tr><tr><td>001:VREFINT/2</td></tr><tr><td>010:VREFINT*3/4</td></tr><tr><td>011:VREFINT</td></tr><tr><td>100:PB2</td></tr><tr><td>101:PA0</td></tr><tr><td>110:PB1</td></tr><tr><td>111:VSSA</td></tr><tr><td rowspan="6">3:2</td><td rowspan="6">CMP0M[1:0]</td><td>CMP0模式</td></tr><tr><td>该位域用于控制CMP0的运行模式以调整速度和功耗。</td></tr><tr><td>00:高速/全功耗</td></tr><tr><td>01:中速/中功耗</td></tr><tr><td>10:低速/低功耗</td></tr><tr><td>11:超低速/超低功耗</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td rowspan="2">0</td><td rowspan="2">CMP0EN</td><td>CMP0使能</td></tr><tr><td>0: CMP0禁能</td></tr></table>

## 1：CMP0 使能

## 18.4.2. CMP1 控制状态寄存器（CMP1_CS）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP1LK</td><td>CMP1O</td><td colspan="6">保留</td><td>CMP1SEN</td><td>CMP1BEN</td><td>保留</td><td colspan="3">CMP1BLK[2:0]</td><td colspan="2">CMP1HST[1:0]</td></tr><tr><td>rwo</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMP1PL</td><td colspan="3">保留</td><td>CMP1SW</td><td colspan="4">保留</td><td colspan="3">CMP1MSEL[2:0]</td><td colspan="2">CMP1M[1:0]</td><td>保留</td><td>CMP1EN</td></tr><tr><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP1LK</td><td>CMP1写保护该位可将CMP1的各控制位设为只读,该位可写一次,通过系统复位清除,可通过软件置位。0: CMP1_CS[31:0]是可读可写位1: CMP1_CS[31:0]是只读位</td></tr><tr><td>30</td><td>CMP1O</td><td>CMP1输出该位反映CMP1输出状态,是只读位。0: 同相输入端低于反相输入端,输出为低电平。1: 同相输入端高于反相输入端,输出为高电平。</td></tr><tr><td>29:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CMP1SEN</td><td>电压标量使能位该位可通过软件置位和清除,可使能<eq>V_{REFINT}</eq>分频器的输出,被视为反相输入端。0: 在CMP0_CS寄存器CMP0SEN位为0的情景下,除能带隙标量。1: 使能带隙标量</td></tr><tr><td>22</td><td>CMP1BEN</td><td>标量桥接使能位0: 在CMP0_CS寄存器CMP0BEN位为0的情景下,除能标量电阻桥接功能。1: 使能标量电阻桥接功能</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>CMP1BLK[2:0]</td><td>CMP1输出消隐源该位域用于选择哪个定时器输出控制CMP1的输出消隐。000: 无消隐001: 选择TIMER0_CH1输出比较信号为消隐源010: 选择TIMER2_CH1输出比较信号为消隐源011: 保留100: 选择TIMER13_CH0输出比较信号为消隐源</td></tr></table>

<table><tr><td></td><td></td><td>101:选择TIMER15_CH0输出比较信号为消隐源110~111:保留</td></tr><tr><td>17:16</td><td>CMP1HST[1:0]</td><td>CMP1迟滞该位域用于控制迟滞水平。00:无迟滞01:低迟滞10:中迟滞11:高迟滞</td></tr><tr><td>15</td><td>CMP1PL</td><td>CMP1输出极性该位用于控制输出极性。0:输出是正相的1:输出是反相的</td></tr><tr><td>14:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>CMP1SW</td><td>CMP1开关模式该位用于开关CMP1同相输入端PA3与PB6之间的连接。0:开关模式禁能1:开关模式使能</td></tr><tr><td>10:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CMP1MSEL[2:0]</td><td>CMP1_IM输入选择该位域用于选择CMP1的输入端CMP1_IM的输入源。000:<eq>V_{REFINT}</eq>/4001:<eq>V_{REFINT}</eq>/2010:<eq>V_{REFINT}</eq>*3/4011:<eq>V_{REFINT}</eq>100:PB6101:PA2110:PB3111:PB4</td></tr><tr><td>3:2</td><td>CMP1PM[1:0]</td><td>CMP1模式该位域用于控制CMP1的运行模式以调整速度和功耗。00:高速/全功耗01:中速/中功耗10:低速/低功耗11:超低速/超低功耗</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CMP1EN</td><td>CMP1使能0:CMP1禁能1:CMP1使能</td></tr></table>

