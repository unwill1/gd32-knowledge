## 23.4. 比较器寄存器

CMP 基地址：0x4000 7800

## 23.4.1. 状态寄存器（CMP_STAT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td colspan="15">Reserved</td><td>CMP0IF</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15"></td><td>CMP0O</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CMP0IF</td><td>CMP0中断标志位0:无CMP0中断发生1: CMP0中断发生当CMP0输出置位时,该位由硬件置1。软件写1至CMP_IFC寄存器CMP0IC位清0。</td></tr><tr><td>15:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CMP0O</td><td>CMP0 输出该位反映 CMP0 输出状态,是只读位0:正相输入端低于反相输入端,输出为低电平1:正相输入端高于反相输入端,输出为高电平</td></tr></table>

## 23.4.2. 中断标志位清除寄存器（CMP_IFC）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td colspan="15">Reserved</td><td>CMP0IC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>Reserved</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>CMP0IC</td><td>CMP0中断标志位清除0:无清除中断标志位发生1:清除中断标志位</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 23.4.3. CMP0 控制状态寄存器（CMP0_CS）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMP0LK</td><td>CMP0DF SNUM</td><td colspan="2">CMP0DFSCDIV[1:0]</td><td colspan="4">CMP0BLK[3:0]</td><td colspan="4">保留</td><td colspan="4">CMP0MSEL[3:0]</td></tr><tr><td>rwo</td><td>rw</td><td colspan="2">rw</td><td colspan="8">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CMP0HST[1:0]</td><td>保留</td><td>CMP0INT EN</td><td colspan="2">保留</td><td>CMP0PL</td><td>CMP0SE N</td><td>CMP0BE N</td><td>CMP0EN</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMP0LK</td><td>CMP0写保护该位可将CMP0的各控制位设为只读。该位只可通过软件置位一次,通过系统复位清除。0: CMP0_CS是可读可写位1: CMP0_CS是只读位</td></tr><tr><td>30</td><td>CMP0DFSNUM</td><td>CMP0数字滤波采样次数0:同一值采样2次,输出发生变化。1:同一值采样3次,输出发生变化</td></tr><tr><td>29:28</td><td>CMP0DFSCDIV[1:0]</td><td>CMP0数字滤波采样时钟分频该位被用于选择数字滤波的采样频率。00:未使用数字滤波器01:采样频率为<eq>f_{PCLK} / 8</eq>。10:采样频率为<eq>f_{PCLK} / 16</eq>。</td></tr></table>

<table><tr><td>27:24</td><td>CMP0BLK[3:0]</td><td>CMP0输出消隐源该位域用于选择哪个定时器输出控制比较器0的输出消隐。0000:无消隐0001:选择TIMER0_CH0输出比较信号为消隐源0010:选择TIMER1_CH2输出比较信号为消隐源0011:选择TIMER2_CH2输出比较信号为消隐源0100:选择TIMER2_CH3输出比较信号为消隐源0101:选择TIMER7_CH0输出比较信号为消隐源0110:选择TIMER15_CH0输出比较信号为消隐源其它:保留。</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>CMP0MSEL[3:0]</td><td>CMP0_IM输入选择该位域用来选择CMP0的CMP0_IM输入源选择。0000:<eq>V_{REFINT}</eq> / 40001:<eq>V_{REFINT}</eq> / 20010:<eq>V_{REFINT}</eq>*3 / 40011:<eq>V_{REFINT}</eq>0100:PA40101:PA50110:PA20111:DAC_OUT0其它:保留。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CMP0HST[1:0]</td><td>CMP0迟滞该位域用于控制迟滞水平00:无迟滞01:低迟滞10:中迟滞11:高迟滞</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CMP0INTEN</td><td>CMP0中断使能0:禁能1:使能</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CMP0PL</td><td>CMP0输出极性该位是用来控制CMP0输出极性</td></tr></table>

<table><tr><td></td><td></td><td>0: 输出是正相的1: 输出是反相的</td></tr><tr><td>2</td><td>CMP0SEN</td><td>电压定标器使能位当CMP0使能时,该位必须置位0: 如果CMP0_CS的CMP0SEN位也复位,则禁用<eq>V_{REFINT}</eq>电压定标器1: 启用电压定标器</td></tr><tr><td>1</td><td>CMP0BEN</td><td>定标器使能位0: 如果CMP0_CS的CMP0BEN位也复位,则禁用定标器电阻桥1: 启用定标器电阻桥</td></tr><tr><td>0</td><td>CMP0EN</td><td>CMP0使能0: CMP0禁能1: CMP0使能</td></tr></table>
