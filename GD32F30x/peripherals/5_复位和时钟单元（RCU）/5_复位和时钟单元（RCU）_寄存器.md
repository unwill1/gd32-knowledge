## 5.3. RCU 寄存器

RCU 基地址：0x4002 1000

## 5.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83 x表示未定义

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>PLLSTB</td><td>PLLEN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td colspan="6"></td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MSTB</td><td>IRC8MEN</td></tr><tr><td colspan="6"></td><td>r</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~32MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~32MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位0:高速4~32MHz晶体振荡器被关闭1:高速4~32MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部8MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部8MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整IRC8M到8MHz±1%</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M内部8MHz RC振荡器稳定标志位硬件置‘1’来指示IRC8M振荡器时钟是否稳定待用0:IRC8M振荡器未稳定1:IRC8M振荡器已稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部8MHz RC振荡器使能软件置位或复位,如果IRC8M时钟做为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当CKMEN置位同时用作系统时钟的HXTAL振荡器发生故障时,该位由硬件置1来启动IRC8M振荡器。0:内部8MHz RC振荡器被关闭1:内部8MHz RC振荡器被打开</td></tr></table>

## 5.3.2. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>USBDPSC[2]</td><td>PLLMF[5]</td><td>保留</td><td>ADCPSC[2]</td><td>PLLMF[4]</td><td colspan="3">CKOUT0SEL[2:0]</td><td colspan="2">USBDPSC[1:0]</td><td colspan="4">PLLMF[3:0]</td><td>PREDV0</td><td>PLLSEL</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]</td><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>USBDPSC[2]</td><td>USBDPSC的第2位参考寄存器RCU_CFG0的22到23位</td></tr><tr><td>30</td><td>PLLMF[5]</td><td>PLLMF的第5位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>ADCPSC[2]</td><td>ADCPSC的第2位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>27</td><td>PLLMF[4]</td><td>PLLMF的第4位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>26:24</td><td>CKOUT0SEL[2:0]</td><td>CKOUT0时钟源选择由软件置位或清零0xx:无时钟输出100:选择系统时钟CK_SYS101:选择内部8M RC振荡器时钟110:选择高速晶体振荡器时钟(HXTAL)111:选择(CK_PLL/2)时钟</td></tr><tr><td>23:22</td><td>USBDPSC[1:0]</td><td>USBD的时钟分频系数由软件置位或清零。USBD的时钟必须为48MHz,当USBD时钟使能的时候,这些位无法修改。000:CK_USBD=CK_PLL/1.5001:CK_USBD=CK_PLL010:CK_USBD=CK_PLL/2.5011:CK_USBD=CK_PLL/2100:CK_USBD=CK_PLL/3101:CK_USBD=CK_PLL/3.511x:CK_USBD=CK_PLL/4</td></tr><tr><td>21:18</td><td>PLLMF[3:0]</td><td>PLL时钟倍频因子与寄存器RCU_CFG0的27,30位共同构成倍频因子,由软件置位或清零。注意:PLL输出时钟频率不能超过120MHz000000:(PLL源时钟x2)000001:(PLL源时钟x3)000010:(PLL源时钟x4)000011:(PLL源时钟x5)000100:(PLL源时钟x6)000101:(PLL源时钟x7)000110:(PLL源时钟x8)000111:(PLL源时钟x9)001000:(PLL源时钟x10)001001:(PLL源时钟x11)</td></tr></table>

001010: (PLL 源时钟 x 12)

001011: (PLL 源时钟 x 13)

001100: (PLL 源时钟 x 14)

001101: (PLL 源时钟 x 15)

001110: （PLL 源时钟 x 16）

001111: (PLL 源时钟 x 16)

010000: (PLL 源时钟 x 17)

010001: (PLL 源时钟 x 18)

010010: (PLL 源时钟 x 19)

010011: (PLL 源时钟 x 20)

010100: （PLL 源时钟 x 21）

010101: (PLL 源时钟 x 22)

010110: (PLL 源时钟 x 23)

010111: (PLL 源时钟 x 24)

011000: (PLL 源时钟 x 25)

011001: (PLL 源时钟 x 26)

011010: （PLL 源时钟 x 27）

011011: (PLL 源时钟 x 28)

011100: (PLL 源时钟 x 29)

011101: (PLL 源时钟 x 30)

011110: （PLL 源时钟 x 31）

011111: (PLL 源时钟 x 32)

100000: (PLL 源时钟 x 33)

100001: (PLL 源时钟 x 34)

... 

111110: (PLL 源时钟 x 63)

111111: (PLL 源时钟 x 63)

17 PREDV0 PREDV0 分频因子

由软件置位或清零，PLL 未使能时，可以修改这些位。

0: PREDV0 输入源时钟未分频

1: PREDV0 输入源时钟 2 分频

16 PLLSEL PLL时钟源选择

由软件置位或复位，控制 PLL 时钟源。

0: （IRC8M / 2）被选择为 PLL 时钟的时钟源

1: HXTAL 时钟或者 IRC48M 时钟（寄存器 RCU_CFG1 位 PLLPRESEL 决定）被选择为 PLL 时钟的时钟源

15:14 ADCPSC[1:0] ADC 的时钟分频系数

与寄存器RCU_CFG0的28位，寄存器RCU_CFG1的29位共同构成分频因子。

由软件置位或清零

0000: CK_ADC = CK_APB2 / 2 

0001: CK_ADC = CK_APB2 / 4 

0010: CK_ADC = CK_APB2 / 6 

0011: CK_ADC = CK_APB2 / 8 

0100: CK_ADC = CK_APB2 / 2 

0101: CK_ADC = CK_APB2 / 12 

0110: CK_ADC = CK_APB2 / 8 

0111: CK_ADC = CK_APB2 / 16 

1x00 : CK_ADC = CK_AHB / 5 

1x01 : CK_ADC = CK_AHB / 6 

1x10 : CK_ADC = CK_AHB / 10 

1x11 : CK_ADC = CK_AHB / 20 

13:11 APB2PSC[2:0] APB2 预分频选择

由软件置位或清零，控制 APB2 时钟分频因子。

0xx: 选择 CK_AHB 时钟不分频

100: 选择 CK_AHB 时钟 2 分频

101: 选择 CK_AHB 时钟 4 分频

110: 选择 CK_AHB 时钟 8 分频

111: 选择 CK_AHB 时钟 16 分频

10:8 APB1PSC[2:0] APB1 预分频选择

由软件置位或清零，控制 APB1 时钟分频因子。

0xx: 选择 CK_AHB 时钟不分频

100: 选择 CK_AHB 时钟 2 分频

101: 选择 CK_AHB 时钟 4 分频

110: 选择 CK_AHB 时钟 8 分频

111: 选择 CK_AHB 时钟 16 分频

7:4 AHBPSC[3:0] AHB预分频选择

由软件置位或清零，控制 AHB 时钟分频因子。

0xxx: 选择 CK_SYS 时钟不分频

1000: 选择 CK_SYS 时钟 2 分频

1001: 选择 CK_SYS 时钟 4 分频

1010: 选择 CK_SYS 时钟 8 分频

1011: 选择 CK_SYS 时钟 16 分频

1100: 选择 CK_SYS 时钟 64 分频

1101: 选择 CK_SYS 时钟 128 分频

1110: 选择 CK_SYS 时钟 256 分频

1111: 选择 CK_SYS 时钟 512 分频

3:2 SCSS[1:0] 系统时钟选择状态

由硬件置位或清零，标识当前系统时钟的时钟源。

00: 选择 CK_IRC8M 时钟作为 CK_SYS 时钟源

01: 选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10: 选择 CK_PLL 时钟作为 CK_SYS 时钟源

11: 保留

1:0 SCS[1:0] 系统时钟选择

由软件配置选择系统时钟源。由于 CK_SYS 的改变存在固有的延迟，因此软件应当读 SCSS 位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时，以及当 HXTAL 直接或间接作为系统时钟同时 HXTAL 时钟监视器检测到 HXTAL 故障时，强制选择 IRC8M 作为系统时钟。

00: 选择 CK_IRC8M 时钟作为 CK_SYS 时钟源

01: 选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10: 选择 CK_PLL 时钟作为 CK_SYS 时钟源

11: 保留

## 5.3.3. 时钟中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td colspan="2">保留</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC40KSTBIC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC8MSTBIE</td><td>LXTALSTBIE</td><td>IRC40KSTBIE</td><td>CKMIF</td><td colspan="2">保留</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC8MSTBIF</td><td>LXTALSTBIF</td><td>IRC40KSTBIF</td></tr><tr><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL时钟稳定中断清零软件写1复位PLLSTBIF标志位0:不复位PLLSTBIF标志位1:复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M时钟稳定中断清零软件写1复位IRC8MSTBIF标志位0:不复位IRC8MSTBIF标志位1:复位IRC8MSTBIF标志位</td></tr></table>

<table><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0:不复位LXTALSTBIF标志位1:复位LXTALSTBIF标志位</td></tr><tr><td>16</td><td>IRC40KSTBIC</td><td>IRC40K时钟稳定中断清零软件写1复位IRC40KSTBIF标志位0:不复位IRC40KSTBIF标志位1:复位IRC40KSTBIF标志位</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置位和复位来使能/禁止PLL时钟稳定中断0:禁止PLL时钟稳定中断1:使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M时钟稳定中断使能软件置位和复位来使能/禁止IRC8M时钟稳定中断0:禁止IRC8M时钟稳定中断1:使能IRC8M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC40KSTBIE</td><td>IRC40K时钟稳定中断使能软件置位和复位来使能/禁止IRC40K时钟稳定中断0:禁止IRC40K时钟稳定中断1:使能IRC40K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位.软件置位CKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1软件置位PLLSTBIC位时清除该位0:无PLL时钟稳定中断产生</td></tr></table>

<table><tr><td></td><td></td><td>1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~16MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC40KSTBIF</td><td>IRC40K时钟稳定中断标志位当内部40kHz RC振荡器时钟稳定且IRC40KSTBIE位被置1时由硬件置1软件置位IRC40KSTBIC位时清除该位0:无IRC40K时钟稳定中断产生1:产生IRC40K时钟稳定中断</td></tr></table>

## 5.3.4. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>TIMER10RST</td><td>TIMER9RST</td><td>TIMER8RST</td><td colspan="3">保留</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2RS T</td><td>USART0 RST</td><td>TIMER7R ST</td><td>SPI0RST</td><td>TIMER0R ST</td><td>ADC1RS T</td><td>ADC0RS T</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td><td>AFRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10RST</td><td>TIMER10 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td></td><td></td><td>1: 复位 TIMER10</td></tr><tr><td>20</td><td>TIMER9RST</td><td>TIMER9 复位由软件置位或复位0: 无作用1: 复位 TIMER9</td></tr><tr><td>19</td><td>TIMER8RST</td><td>TIMER8 复位由软件置位或复位0: 无作用1: 复位 TIMER8</td></tr><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2RST</td><td>ADC2 复位由软件置位或复位0: 无作用1: 复位所有 ADC2</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0: 无作用1: 复位 USART0</td></tr><tr><td>13</td><td>TIMER7RST</td><td>TIMER7 复位由软件置位或复位0: 无作用1: 复位 TIMER7</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0: 无作用1: 复位 SPI0</td></tr><tr><td>11</td><td>TIMER0RST</td><td>TIMER0 复位由软件置位或复位0: 无作用1: 复位 TIMER0</td></tr><tr><td>10</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0: 无作用1: 复位所有 ADC1</td></tr><tr><td>9</td><td>ADC0RST</td><td>ADC0 复位由软件置位或复位0: 无作用1: 复位所有 ADC0</td></tr><tr><td>8</td><td>PGRST</td><td>GPIO 端口 G 复位由软件置位或复位0:无作用1:复位 GPIO 端口 G</td></tr><tr><td>7</td><td>PFRST</td><td>GPIO 端口 F 复位由软件置位或复位0:无作用1:复位 GPIO 端口 F</td></tr><tr><td>6</td><td>PERST</td><td>GPIO 端口 E 复位由软件置位或复位0:无作用1:复位 GPIO 端口 E</td></tr><tr><td>5</td><td>PDRST</td><td>GPIO 端口 D 复位由软件置位或复位0:无作用1:复位 GPIO 端口 D</td></tr><tr><td>4</td><td>PCRST</td><td>GPIO 端口 C 复位由软件置位或复位0:无作用1:复位 GPIO 端口 C</td></tr><tr><td>3</td><td>PBRST</td><td>GPIO 端口 B 复位由软件置位或复位0:无作用1:复位 GPIO 端口 B</td></tr><tr><td>2</td><td>PARST</td><td>GPIO 端口 A 复位由软件置位或复位0:无作用1:复位 GPIO 端口 A</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFRST</td><td>复用功能 I/O 复位由软件置位或复位0:无作用1:复位复用功能 I/O</td></tr></table>

## 5.3.5. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACRST</td><td>PMURST</td><td>BKPIRST</td><td>保留</td><td>CAN0RS T</td><td>保留</td><td>USBD</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4R ST</td><td>UART3R ST</td><td>USART2 RST</td><td>USART1 RST</td><td>保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGT RST</td><td colspan="2">保留</td><td>TIMER13 RST</td><td>TIMER12 RST</td><td>TIMER11 RST</td><td>TIMER6R ST</td><td>TIMER5R ST</td><td>TIMER4R ST</td><td>TIMER3R ST</td><td>TIMER2R ST</td><td>TIMER1R ST</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACRST</td><td>DAC 复位由软件置位或复位0:无作用1:复位 DAC</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>BKPIRST</td><td>BKPI 复位由软件置位或复位0:无作用1:复位 BKP</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>USBDRST</td><td>USBD 复位由软件置位或复位0:无作用1:复位 USBD</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td></td><td></td><td>1: 复位 I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0: 无作用1: 复位 UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0: 无作用1: 复位 UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0: 无作用1: 复位 USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0: 无作用1: 复位 USART1</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0: 无作用1: 复位 SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0: 无作用1: 复位 SPI1</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位0: 无作用1: 复位 WWDGT</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13RST</td><td>TIMER13 复位由软件置位或复位0: 无作用1: 复位 TIMER13</td></tr><tr><td>7</td><td>TIMER12RST</td><td>TIMER12 复位由软件置位或复位0:无作用1:复位 TIMER12</td></tr><tr><td>6</td><td>TIMER11RST</td><td>TIMER11 复位由软件置位或复位0:无作用1:复位 TIMER11</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 5.3.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移。0x14

复位值。0x0000 0014

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>SDIOEN</td><td>保留</td><td>EXMCEN</td><td>保留</td><td>CRCEN</td><td>保留</td><td>FMCSPE N</td><td>保留</td><td>SRAMSP EN</td><td>DMA1EN</td><td>DMA0EN</td></tr><tr><td></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>SDIOEN</td><td>SDIO时钟使能由软件置位或复位0:关闭SDIO时钟1:开启SDIO时钟</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EXMCEN</td><td>EXMC时钟使能由软件置位或复位0:关闭EXMC时钟1:开启EXMC时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0:关闭CRC时钟1:开启CRC时钟</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCSPEN</td><td>在睡眠模式下FMC时钟使能由软件置位或复位0:在睡眠模式下关闭FMC时钟1:在睡眠模式下开启FMC时钟</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPEN</td><td>在睡眠模式下SRAM时钟使能由软件置位或复位0:在睡眠模式下关闭SRAM时钟1:在睡眠模式下开启SRAM时钟</td></tr><tr><td>1</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭DMA1时钟1:开启DMA1时钟</td></tr><tr><td>0</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr></table>

## 5.3.7. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>TIMER10EN</td><td>TIMER9EN</td><td>TIMER8EN</td><td colspan="3">保留</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2EN</td><td>USART0EN</td><td>TIMER7EN</td><td>SPI0EN</td><td>TIMER0EN</td><td>ADC1EN</td><td>ADC0EN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td><td>AFEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10EN</td><td>TIMER10时钟使能由软件置位或复位0:关闭 TIMER10 时钟1:开启 TIMER10 时钟</td></tr><tr><td>20</td><td>TIMER9EN</td><td>TIMER9时钟使能由软件置位或复位0:关闭 TIMER9 时钟1:开启 TIMER9 时钟</td></tr><tr><td>19</td><td>TIMER8EN</td><td>TIMER8时钟使能由软件置位或复位0:关闭 TIMER8 时钟1:开启 TIMER8 时钟</td></tr><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭 ADC2 时钟1:开启 ADC2 时钟</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭 USART0 时钟1:开启 USART0 时钟</td></tr><tr><td>13</td><td>TIMER7EN</td><td>TIMER7时钟使能由软件置位或复位0:关闭 TIMER7 时钟</td></tr></table>

<table><tr><td></td><td></td><td>1:开启 TIMER7 时钟</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0 时钟使能由软件置位或复位0:关闭 SPI0 时钟1:开启 SPI0 时钟</td></tr><tr><td>11</td><td>TIMER0EN</td><td>TIMER0 时钟使能由软件置位或复位0:关闭 TIMER0 时钟1:开启 TIMER0 时钟</td></tr><tr><td>10</td><td>ADC1EN</td><td>ADC1 时钟使能由软件置位或复位0:关闭 ADC1 时钟1:开启 ADC1 时钟</td></tr><tr><td>9</td><td>ADC0EN</td><td>ADC0 时钟使能由软件置位或复位0:关闭 ADC0 时钟1:开启 ADC0 时钟</td></tr><tr><td>8</td><td>PGEN</td><td>GPIO 端口 G 时钟使能由软件置位或复位0:关闭 GPIO 端口 G 时钟1:开启 GPIO 端口 G 时钟</td></tr><tr><td>7</td><td>PFEN</td><td>GPIO 端口 F 时钟使能由软件置位或复位0:关闭 GPIO 端口 F 时钟1:开启 GPIO 端口 F 时钟</td></tr><tr><td>6</td><td>PEEN</td><td>GPIO 端口 E 时钟使能由软件置位或复位0:关闭 GPIO 端口 E 时钟1:开启 GPIO 端口 E 时钟</td></tr><tr><td>5</td><td>PDEN</td><td>GPIO 端口 D 时钟使能由软件置位或复位0:关闭 GPIO 端口 D 时钟1:开启 GPIO 端口 D 时钟</td></tr><tr><td>4</td><td>PCEN</td><td>GPIO 端口 C 时钟使能由软件置位或复位0:关闭 GPIO 端口 C 时钟1:开启 GPIO 端口 C 时钟</td></tr><tr><td>3</td><td>PBEN</td><td>GPIO 端口 B 时钟使能由软件置位或复位0: 关闭 GPIO 端口 B 时钟1: 开启 GPIO 端口 B 时钟</td></tr><tr><td>2</td><td>PAEN</td><td>GPIO 端口 A 时钟使能由软件置位或复位0: 关闭 GPIO 端口 A 时钟1: 开启 GPIO 端口 A 时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFEN</td><td>复用功能 IO 时钟使能由软件置位或复位0: 关闭复用功能 IO 时钟1: 开启复用功能 IO 时钟</td></tr></table>

## 5.3.8. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACEN</td><td>PMUEN</td><td>BKPIEN</td><td>保留</td><td>CAN0EN</td><td>保留</td><td>USBDEN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td colspan="2">保留</td><td>TIMER13EN</td><td>TIMER12EN</td><td>TIMER11EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置位或复位0:关闭DAC时钟1:开启DAC时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>27</td><td>BKPIEN</td><td>BKP时钟使能由软件置位或复位0:关闭BKP时钟</td></tr></table>

<table><tr><td></td><td></td><td>1:开启BKP时钟</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>USBDEN</td><td>USBD时钟使能由软件置位或复位0:关闭USBD时钟1:开启USBD时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0: 关闭 SPI2 时钟1: 开启 SPI2 时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1 时钟使能由软件置位或复位0: 关闭 SPI1 时钟1: 开启 SPI1 时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT 时钟使能由软件置位或复位0: 关闭 WWDGT 时钟1: 开启 WWDGT 时钟</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13EN</td><td>TIMER13 时钟使能由软件置位或复位0: 关闭 TIMER13 时钟1: 开启 TIMER13 时钟</td></tr><tr><td>7</td><td>TIMER12EN</td><td>TIMER12 时钟使能由软件置位或复位0: 关闭 TIMER12 时钟1: 开启 TIMER12 时钟</td></tr><tr><td>6</td><td>TIMER11EN</td><td>TIMER11 时钟使能由软件置位或复位0: 关闭 TIMER11 时钟1: 开启 TIMER11 时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6 时钟使能由软件置位或复位0: 关闭 TIMER6 时钟1: 开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5 时钟使能由软件置位或复位0: 关闭 TIMER5 时钟1: 开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4 时钟使能由软件置位或复位0: 关闭 TIMER4 时钟1: 开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3 时钟使能由软件置位或复位0: 关闭 TIMER3 时钟</td></tr></table>

1: 开启 TIMER3 时钟

<table><tr><td>1</td><td>TIMER2EN</td><td>TIMER2 时钟使能由软件置位或复位0:关闭 TIMER2 时钟1:开启 TIMER2 时钟</td></tr></table>

<table><tr><td>0</td><td>TIMER1EN</td><td>TIMER1 时钟使能由软件置位或复位0:关闭 TIMER1 时钟1:开启 TIMER1 时钟</td></tr></table>

## 5.3.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，只能由备份域复位进行复位

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的LXTALEN、LXTALBPS、RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPDRST</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPDRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC40K时钟作为RTC的时钟源11:选择CK_HXTAL/128时钟作为RTC的时钟源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值00:弱驱动能力01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能由软件置位或复位0:关闭LXTAL时钟1:使能LXTAL时钟</td></tr></table>

## 5.3.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C00 0000，所有复位标志位仅在电源复位时被清零，RSTFC/IRC40KEN在系统复位时被清零。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>保留</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="10">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>IRC40KSTB</td><td>IRC40KEN</td></tr></table>

r rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用1:清除所有复位标志位</td></tr><tr><td>23:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC40KSTB</td><td>IRC40K时钟稳定标志位该位由硬件置1指示IRC40K输出时钟是否稳定待用</td></tr></table>

0: IRC40K 时钟未稳定

1: IRC40K 已稳定

<table><tr><td>0</td><td>IRC40KEN</td><td>IRC40K 使能由软件置位和复位0:关闭 IRC40K 时钟1:开启 IRC40K 时钟</td></tr></table>

## 5.3.11. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>PLLPRES EL</td><td>ADCPSC[3]</td><td colspan="13">保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>PLLPRESET</td><td>PLL时钟源预选择由软件置位或复位,控制PLL时钟源0:HXTAL被选择为PLL时钟的时钟源1:CK_IRC48M被选择为PLL时钟的时钟源</td></tr><tr><td>29</td><td>ADCPSC[3]</td><td>ADCPSC的第3位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>28:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.12. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为缺省值001:在深度睡眠模式下内核电压为(缺省值-0.1)V(不建议客户使用)010:在深度睡眠模式下内核电压为(缺省值-0.2)V(不建议客户使用)011:在深度睡眠模式下内核电压为(缺省值-0.3)V(不建议客户使用)1xx:保留</td></tr></table>

## 5.3.13. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0x8000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">保留</td><td>IRC48MS TB</td><td>IRC48ME N</td></tr><tr><td colspan="14">r</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>CK48MS EL</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB [7:0]</td><td>内部 48MHz RC 振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部 48MHz RC 振荡器时钟稳定标志位硬件置‘1’来指示 IRC48M 振荡器时钟是否稳定待用0: IRC48M 未稳定1: IRC48M 已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部 48MHz RC 振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位0: 关闭 IRC48M 时钟1: 打开 IRC48M 时钟</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CK48MSEL</td><td>48MHz时钟源选择由软件置位和复位。该位用于选择IRC48M时钟或PLL48M时钟作为CK48M时钟源。CK48M时钟用于:0:不选择IRC48M时钟(使用CK_PLL/USBDPSC时钟)1:选择IRC48M时钟</td></tr></table>

## 5.3.14. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>IRC48MSTBIC</td><td colspan="6">保留</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>IRC48MSTBIE</td><td colspan="7">保留</td><td>IRC48MSTBIF</td><td colspan="6">保留</td></tr><tr><td colspan="9">rw</td><td colspan="7">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部 48 MHz RC 振荡器稳定中断清零软件写 1 复位 IRC48MSTBIF 标志位0: 不复位 IRC48MSTBIF 标志位1: 复位 IRC48MSTBIF 标志位</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部 48 MHz RC 振荡器稳定中断使能由软件置位和复位来使能/禁止 IRC48M 时钟稳定中断0: 禁止 IRC48M 时钟稳定中断1: 使能 IRC48M 时钟稳定中断</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M 时钟稳定中断标志位当内部 48 MHz RC 振荡器时钟稳定且 IRC48MSTBIE 位被置 1 时由硬件置 1 软件置位 IRC48MSTBIC 位时清除该位0: 无 IRC48M 时钟稳定中断产生1: 产生 IRC48M 时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.15. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTC RST</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.16. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC 时钟使能由软件置位或复位0: 关闭 CTC 时钟1: 开启 CTC 时钟</td></tr></table>

26:0 

保留

必须保持复位值

## 互联型产品的复位和时钟控制单元（RCU）

## 5.6. RCU 寄存器

RCU 基地址：0x4002 1000

## 5.6.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83 x表示未定义

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>PLL2STB</td><td>PLL2EN</td><td>PLL1STB</td><td>PLL1EN</td><td>PLLSTB</td><td>PLL EN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALB PS</td><td>HXTALST B</td><td>HXTALE N</td></tr><tr><td colspan="2"></td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MST B</td><td>IRC8MEN</td></tr><tr><td colspan="2"></td><td colspan="6">r</td><td colspan="6">rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>PLL2STB</td><td>PLL2时钟稳定标志位硬件置1来表示PLL2输出时钟是否稳定待用0:PLL2未稳定1:PLL2已稳定</td></tr><tr><td>28</td><td>PLL2EN</td><td>PLL2使能软件置位或复位,当PLL2时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL2被关闭1:PLL2被打开</td></tr><tr><td>27</td><td>PLL1STB</td><td>PLL1时钟稳定标志位硬件置1来表示PLL1输出时钟是否稳定待用0:PLL1未稳定1:PLL1已稳定</td></tr><tr><td>26</td><td>PLL1EN</td><td>PLL1使能软件置位或复位,当PLL1时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL1被关闭1:PLL1被打开</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速3~25MHz晶体振荡器(HXTAL)时钟监视器1:使能高速3~25MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:高速3~25MHz晶体振荡器被关闭1:高速3~25MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部8MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部8MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整IRC8M到8MHz±1%。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M内部8MHz RC振荡器稳定标志位硬件置‘1’来指示IRC8M振荡器时钟是否稳定待用0:IRC8M振荡器未稳定1:IRC8M振荡器已稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部 8MHz RC 振荡器使能软件置位或复位,如果 IRC8M 时钟做为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当 CKMEN 置位同时用作系统时钟的 HXTAL 振荡器发生故障时,该位由硬件置 1 来启动 IRC8M 振荡器。0: 内部 8MHz RC 振荡器被关闭1: 内部 8MHz RC 振荡器被打开</td></tr></table>

## 5.6.2. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>USBFSPSC[2]</td><td colspan="2">PLLMF[5:4]</td><td>ADCPSC[2]</td><td colspan="4">CKOUT0SEL[3:0]</td><td colspan="2">USBFSPSC[1:0]</td><td colspan="4">PLLMF[3:0]</td><td>PREDV0_LSB</td><td>PLLSEL</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]</td><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>USBFSPSC[2]</td><td>USBFSPSC的第2位参考寄存器RCU_CFG0的22到23位</td></tr><tr><td>30:29</td><td>PLLMF[5:4]</td><td>PLLMF的第5位和第4位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>28</td><td>ADCPSC[2]</td><td>ADCPSC的第2位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>27:24</td><td>CKOUT0SEL[3:0]</td><td>CKOUT0时钟源选择由软件置位或清零00xx:无时钟输出0100:选择系统时钟CK_SYS0101:选择内部8M RC振荡器时钟0110:选择高速晶体振荡器时钟(HXTAL)0111:选择(CK_PLL/2)时钟1000:选择CK_PLL1时钟1001:选择(CK_PLL2/2)时钟1010:选择提供给ENET的EXT1时钟1011:选择CK_PLL2时钟</td></tr><tr><td>23:22</td><td>USBFSPSC[1:0]</td><td>USBFS的时钟分频系数由软件置位或清零。USBFS的时钟必须为48MHz,当USBFS时钟使能的时候,这些位无法修改</td></tr></table>

000: CK_USBFS = CK_PLL / 1.5 

001: CK_USBFS = CK_PLL 

010: CK_USBFS = CK_PLL / 2.5 

011: CK_USBFS = CK_PLL / 2 

100: CK_USBFS = CK_PLL / 3 

101: CK_USBFS = CK_PLL / 3.5 

11x: CK_USBFS = CK_PLL / 4 

21:18 PLLMF[3:0] 

PLL 时钟倍频因子

与寄存器RCU_CFG0的29,30位共同构成倍频因子，由软件置位或清零注意：PLL输出时钟频率不能超过120MHz

000000: (PLL 时钟源 x2)

000001: (PLL 时钟源 x3)

000010: (PLL 时钟源 x4)

000011: (PLL 时钟源 x5)

000100: (PLL 时钟源 x6)

000101: (PLL 时钟源 x7)

000110: (PLL 时钟源 x8)

000111: (PLL 时钟源 x9)

001000: (PLL 时钟源 x 10)

001001: (PLL 时钟源 x11)

001010: （PLL 时钟源 x 12）

001011: (PLL 时钟源 x 13)

001100: (PLL 时钟源 x 14)

001101: (PLL 时钟源 x6.5)

001110: （PLL 时钟源 x 16）

001111: (PLL 时钟源 x 16)

010000: (PLL 时钟源 x 17)

010001: (PLL 时钟源 x 18)

010010: (PLL 时钟源 x 19)

010011: (PLL 时钟源 x20)

010100: (PLL 时钟源 x21)

010101: (PLL 时钟源 x22)

010110: （PLL 时钟源 x23）

010111: (PLL 时钟源 x24)

011000: (PLL 时钟源 x25)

011001: （PLL 时钟源 x26）

011010: (PLL 时钟源 x27)

011011: (PLL 时钟源 x28)

011100: (PLL 时钟源 x 29)

011101: (PLL 时钟源 x 30)

011110: (PLL 时钟源 x31)

011111: (PLL 时钟源 x 32)

100000: (PLL 时钟源 x 33)

100001: (PLL 时钟源 x 34)

<table><tr><td></td><td></td><td>...111110: (PLL时钟源x63)111111: (PLL时钟源x63)</td></tr><tr><td>17</td><td>PREDV0_LSB</td><td>PREDV0分频因子的最低位与寄存器RCU_CFG1位PREDV0第0位相同,通过寄存器RCU_CFG1来改变PREDV0的值,此位也会一同改。当PREDV0的第1到3位未修改时,此位决定PREDV0的输入时钟是否二分频。</td></tr><tr><td>16</td><td>PLLSEL</td><td>PLL时钟源选择由软件置位或复位,控制PLL时钟源。0:(IRC8M/2)被选择为PLL时钟的时钟源1:HXTAL时钟或者IRC48M时钟(寄存器RCU_CFG1位PLLPRESEL决定)被选择为PLL时钟的时钟源</td></tr><tr><td>15:14</td><td>ADCPSC[1:0]</td><td>ADC的时钟分频系数与寄存器RCU_CFG0的28位,寄存器RCU_CFG1的29位共同构成分频因子,由软件置位或清零。0000: CK_ADC = CK_APB2 / 20001: CK_ADC = CK_APB2 / 40010: CK_ADC = CK_APB2 / 60011: CK_ADC = CK_APB2 / 80100: CK_ADC = CK_APB2 / 20101: CK_ADC = CK_APB2 / 120110: CK_ADC = CK_APB2 / 80111: CK_ADC = CK_APB2 / 161x00: CK_ADC = CK_AHB / 51x01: CK_ADC = CK_AHB / 61x10: CK_ADC = CK_AHB / 101x11: CK_ADC = CK_AHB / 20</td></tr><tr><td>13:11</td><td>APB2PSC[2:0]</td><td>APB2预分频选择由软件置位或清零,控制APB2时钟分频因子。0xx: CK_APB2 = CK_AHB100: CK_APB2 = CK_AHB / 2101: CK_APB2 = CK_AHB / 4110: CK_APB2 = CK_AHB / 8111: CK_APB2 = CK_AHB / 16</td></tr><tr><td>10:8</td><td>APB1PSC[2:0]</td><td>APB1预分频选择由软件置位或清零,控制APB1时钟分频因子。0xx: CK_APB1 = CK_AHB100: CK_APB1 = CK_AHB / 2101: CK_APB1 = CK_AHB / 4110: CK_APB1 = CK_AHB / 8111: CK_APB1 = CK_AHB / 16</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB预分频选择由软件置位或清零,控制AHB时钟分频因子。0xxx: CK_AHB = CK_SYS1000: CK_AHB = CK_SYS / 21001: CK_AHB = CK_SYS / 41010: CK_AHB = CK_SYS / 81011: CK_AHB = CK_SYS / 161100: CK_AHB = CK_SYS / 641101: CK_AHB = CK_SYS / 1281110: CK_AHB = CK_SYS / 2561111: CK_AHB = CK_SYS / 512</td></tr><tr><td>3:2</td><td>SCSS[1:0]</td><td>系统时钟选择状态由硬件置位或清零,标识当前系统时钟的时钟源。00: 选择CK_IRC8M时钟作为CK_SYS时钟源01: 选择CK_HXTAL时钟作为CK_SYS时钟源10: 选择CK_PLL时钟作为CK_SYS时钟源11: 保留</td></tr><tr><td>1:0</td><td>SCS[1:0]</td><td>系统时钟选择由软件配置选择系统时钟源。由于CK_SYS的改变存在固有的延迟,因此软件应当读SCSS位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时,以及当HXTAL直接或间接作为系统时钟同时HXTAL时钟监视器检测到HXTAL故障时,强制选择IRC8M作为系统时钟。00: 选择CK_IRC8M时钟作为CK_SYS时钟源01: 选择CK_HXTAL时钟作为CK_SYS时钟源10: 选择CK_PLL时钟作为CK_SYS时钟源11: 保留</td></tr></table>

## 5.6.3. 时钟中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td>PLL2STBIC</td><td>PLL1STBIC</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC40KSTBIC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>PLL2STBIE</td><td>PLL1STBIE</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC8MSTBIE</td><td>LXTALSTBIE</td><td>IRC40KSTBIE</td><td>CKMIF</td><td>PLL2STBIF</td><td>PLL1STBIF</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC8MSTBIF</td><td>LXTALSTBIF</td><td>IRC40KSTBIF</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>PLL2STBIC</td><td>PLL2时钟稳定中断清零软件写1复位PLL2STBIF标志位0:不复位PLL2STBIF标志位1:复位PLL2STBIF标志位</td></tr><tr><td>21</td><td>PLL1STBIC</td><td>PLL1时钟稳定中断清零软件写1复位PLL1STBIF标志位0:不复位PLL1STBIF标志位1:复位PLL1STBIF标志位</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL时钟稳定中断清零软件写1复位PLLSTBIF标志位0:不复位PLLSTBIF标志位1:复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M时钟稳定中断清零软件写1复位IRC8MSTBIF标志位0:不复位IRC8MSTBIF标志位1:复位IRC8MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0:不复位LXTALSTBIF标志位1:复位LXTALSTBIF标志位</td></tr><tr><td>16</td><td>IRC40KSTBIC</td><td>IRC40K时钟稳定中断清零软件写1复位IRC40KSTBIF标志位0:不复位IRC40KSTBIF标志位1:复位IRC40KSTBIF标志位</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>PLL2STBIE</td><td>PLL2时钟稳定中断使能软件置位和复位来使能/禁止PLL2时钟稳定中断0:禁止PLL2时钟稳定中断1:使能PLL2时钟稳定中断</td></tr><tr><td>13</td><td>PLL1STBIE</td><td>PLL1时钟稳定中断使能软件置位和复位来使能/禁止PLL1时钟稳定中断0:禁止PLL1时钟稳定中断1:使能PLL1时钟稳定中断</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置位和复位来使能/禁止PLL时钟稳定中断0:禁止PLL时钟稳定中断1:使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M时钟稳定中断使能软件置位和复位来使能/禁止IRC8M时钟稳定中断0:禁止IRC8M时钟稳定中断1:使能IRC8M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC40KSTBIE</td><td>IRC40K时钟稳定中断使能软件置位和复位来使能/禁止IRC40K时钟稳定中断0:禁止IRC40K时钟稳定中断1:使能IRC40K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位软件置位CKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6</td><td>PLL2STBIF</td><td>PLL2时钟稳定中断标志位当PLL时钟稳定且PLL2STBIE位被置1时由硬件置1软件置位PLL2STBIC位时清除该位0:无PLL2时钟稳定中断产生1:产生PLL2时钟稳定中断</td></tr><tr><td>5</td><td>PLL1STBIF</td><td>PLL1时钟稳定中断标志位当PLL时钟稳定且PLL1STBIE位被置1时由硬件置1软件置位PLL1STBIC位时清除该位0:无PLL1时钟稳定中断产生1:产生PLL1时钟稳定中断</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1</td></tr></table>

<table><tr><td></td><td></td><td>软件置位PLLSTBIC位时清除该位0:无PLL时钟稳定中断产生1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速3~25MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC40KSTBIF</td><td>IRC40K时钟稳定中断标志位当内部40kHz RC振荡器时钟稳定且IRC40KSTBIE位被置1时由硬件置1软件置位IRC40KSTBIC位时清除该位0:无IRC40K时钟稳定中断产生1:产生IRC40K时钟稳定中断</td></tr></table>

## 5.6.4. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>TIMER10RST</td><td>TIMER9RST</td><td>TIMER8RST</td><td colspan="3">保留</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0RST</td><td>TIMER7RST</td><td>SPI0RST</td><td>TIMER0RST</td><td>ADC1RS T</td><td>ADC0RS T</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td><td>AFRST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10RST</td><td>TIMER10 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 TIMER10</td></tr><tr><td>20</td><td>TIMER9RST</td><td>TIMER9 复位由软件置位或复位0:无作用1:复位 TIMER9</td></tr><tr><td>19</td><td>TIMER8RST</td><td>TIMER8 复位由软件置位或复位0:无作用1:复位 TIMER8</td></tr><tr><td>18:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0:无作用1:复位 USART0</td></tr><tr><td>13</td><td>TIMER7RST</td><td>TIMER7 复位由软件置位或复位0:无作用1:复位 TIMER7</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>TIMER0RST</td><td>TIMER0 复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr><tr><td>10</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0:无作用1:复位所有 ADC1</td></tr><tr><td>9</td><td>ADC0RST</td><td>ADC0 复位由软件置位或复位0:无作用1:复位所有 ADC0</td></tr><tr><td>8</td><td>PGRST</td><td>GPIO 端口 G 复位由软件置位或复位0:无作用</td></tr><tr><td></td><td></td><td>1: 复位 GPIO 端口 G</td></tr><tr><td>7</td><td>PFRST</td><td>GPIO 端口 F 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 F</td></tr><tr><td>6</td><td>PERST</td><td>GPIO 端口 E 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 E</td></tr><tr><td>5</td><td>PDRST</td><td>GPIO 端口 D 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 D</td></tr><tr><td>4</td><td>PCRST</td><td>GPIO 端口 C 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 C</td></tr><tr><td>3</td><td>PBRST</td><td>GPIO 端口 B 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 B</td></tr><tr><td>2</td><td>PARST</td><td>GPIO 端口 A 复位由软件置位或复位0: 无作用1: 复位 GPIO 端口 A</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFRST</td><td>复用功能 I/O 复位由软件置位或复位0: 无作用1: 复位复用功能 I/O</td></tr></table>

## 5.6.5. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACRSTrw</td><td>PMURSTrw</td><td>BKPIRSTrw</td><td>CAN1RS Trw</td><td>CAN0RS Trw</td><td colspan="2">保留</td><td>I2C1RSTrw</td><td>I2C0RSTrw</td><td>UART4R STrw</td><td>UART3R STrw</td><td>USART2 RSTrw</td><td>USART1 RSTrw</td><td>保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGTRST</td><td colspan="2">保留</td><td>TIMER13RST</td><td>TIMER12RST</td><td>TIMER11RST</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACRST</td><td>DAC 复位由软件置位或复位0:无作用1:复位 DAC</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>BKPIRST</td><td>BKPI 复位由软件置位或复位0:无作用1:复位 BKP</td></tr><tr><td>26</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>25</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>24:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用</td></tr></table>

1: 复位 UART4

19 UART3RST UART3 复位

由软件置位或复位

0: 无作用

1: 复位 UART3

18 USART2RST USART2 复位

由软件置位或复位

0: 无作用

1: 复位 USART2

17 USART1RST USART1 复位

由软件置位或复位

0: 无作用

1: 复位 USART1

16 保留 必须保持复位值。

15 SPI2RST SPI2复位

由软件置位或复位

0: 无作用

1: 复位 SPI2

14 SPI1RST SPI1复位

由软件置位或复位

0: 无作用

1: 复位 SPI1

13:12 保留 必须保持复位值。

11 WWDGTRST WWDGT 复位

由软件置位或复位

0: 无作用

1: 复位 WWDGT

10:9 保留 必须保持复位值。

8 TIMER13RST TIMER13复位

由软件置位或复位

0: 无作用

1: 复位 TIMER13

7 TIMER12RST TIMER12 复位

由软件置位或复位

0: 无作用

1: 复位 TIMER12

6 TIMER11RST TIMER11 复位

由软件置位或复位

<table><tr><td></td><td></td><td>0:无作用1:复位 TIMER11</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 5.6.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移：0x14

复位值：0x0000 0014

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>ENETRXEN</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ENETTXEN</td><td>ENETEN</td><td>保留</td><td>USBFSEN</td><td colspan="3">保留</td><td>EXMCEN</td><td>保留</td><td>CRCEN</td><td>保留</td><td>FMCSPEN</td><td>保留</td><td>SRAMSPEN</td><td>DMA1EN</td><td>DMA0EN</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>ENETRXEN</td><td>以太网 RX 时钟使能由软件置位或复位0:关闭以太网 RX 时钟1:开启以太网 RX 时钟</td></tr><tr><td>15</td><td>ENETTXEN</td><td>以太网 TX 时钟使能由软件置位或复位0:关闭以太网 TX 时钟1:开启以太网 TX 时钟</td></tr><tr><td>14</td><td>ENETEN</td><td>以太网时钟使能由软件置位或复位0:关闭以太网时钟1:开启以太网时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>USBFSEN</td><td>USBFS 时钟使能由软件置位或复位0:关闭 USBFS 时钟1:开启 USBFS 时钟</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EXMCEN</td><td>EXMC 时钟使能由软件置位或复位0:关闭 EXMC 时钟1:开启 EXMC 时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC 时钟使能由软件置位或复位0:关闭 CRC 时钟1:开启 CRC 时钟</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCSPEN</td><td>在睡眠模式下 FMC 时钟使能由软件置位或复位0:在睡眠模式下关闭 FMC 时钟1:在睡眠模式下开启 FMC 时钟</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPEN</td><td>在睡眠模式下 SRAM 时钟使能由软件置位或复位0:在睡眠模式下关闭 SRAM 时钟</td></tr></table>

1: 在睡眠模式下开启 SRAM 时钟

1 DMA1EN DMA1 时钟使能

由软件置位或复位

0: 关闭 DMA1 时钟

1: 开启 DMA1 时钟

0 DMA0EN DMA0 时钟使能

DMA0 时钟使能

由软件置位或复位

0: 关闭 DMA0 时钟

1: 开启 DMA0 时钟

## 5.6.7. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>TIMER10EN</td><td>TIMER9EN</td><td>TIMER8EN</td><td colspan="3">保留</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0EN</td><td>TIMER7EN</td><td>SPI0EN</td><td>TIMER0EN</td><td>ADC1EN</td><td>ADC0EN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td><td>AFEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10EN</td><td>TIMER10时钟使能由软件置位或复位0:关闭 TIMER10 时钟1:开启 TIMER10 时钟</td></tr><tr><td>20</td><td>TIMER9EN</td><td>TIMER9时钟使能由软件置位或复位0:关闭 TIMER9 时钟1:开启 TIMER9 时钟</td></tr><tr><td>19</td><td>TIMER8EN</td><td>TIMER8时钟使能由软件置位或复位0:关闭 TIMER8 时钟1:开启 TIMER8 时钟</td></tr><tr><td>18:15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>13</td><td>TIMER7EN</td><td>TIMER7复位由软件置位或复位0:无作用1:复位TIMER7</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0复位由软件置位或复位0:无作用1:复位SPI0</td></tr><tr><td>11</td><td>TIMER0EN</td><td>TIMER0复位由软件置位或复位0:无作用1:复位TIMER0</td></tr><tr><td>10</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>9</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>8</td><td>PGEN</td><td>GPIO端口G时钟使能由软件置位或复位0:关闭GPIO端口G时钟1:开启GPIO端口G时钟</td></tr><tr><td>7</td><td>PFEN</td><td>GPIO端口F时钟使能由软件置位或复位0:关闭GPIO端口F时钟1:开启GPIO端口F时钟</td></tr><tr><td>6</td><td>PEEN</td><td>GPIO端口E时钟使能由软件置位或复位0:关闭GPIO端口E时钟1:开启GPIO端口E时钟</td></tr><tr><td>5</td><td>PDEN</td><td>GPIO端口D时钟使能由软件置位或复位0:关闭GPIO端口D时钟1:开启GPIO端口D时钟</td></tr><tr><td>4</td><td>PCEN</td><td>GPIO端口C时钟使能由软件置位或复位0:关闭GPIO端口C时钟1:开启GPIO端口C时钟</td></tr><tr><td>3</td><td>PBEN</td><td>GPIO端口B时钟使能由软件置位或复位0:关闭GPIO端口B时钟1:开启GPIO端口B时钟</td></tr><tr><td>2</td><td>PAEN</td><td>GPIO端口A时钟使能由软件置位或复位0:关闭GPIO端口A时钟1:开启GPIO端口A时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFEN</td><td>复用功能IO时钟使能由软件置位或复位0:关闭复用功能IO时钟1:开启复用功能IO时钟</td></tr></table>

## 5.6.8. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACEN</td><td>PMUEN</td><td>BKPIEN</td><td>CAN1EN</td><td>CAN0EN</td><td colspan="2">保留</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td colspan="2">保留</td><td>TIMER13EN</td><td>TIMER12EN</td><td>TIMER11EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置位或复位0:关闭DAC时钟1:开启DAC时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0: 关闭 PMU 时钟1: 开启 PMU 时钟</td></tr><tr><td>27</td><td>BKPIEN</td><td>BKP 时钟使能由软件置位或复位0: 关闭 BKP 时钟1: 开启 BKP 时钟</td></tr><tr><td>26</td><td>CAN1EN</td><td>CAN1 时钟使能由软件置位或复位0: 关闭 CAN1 时钟1: 开启 CAN1 时钟</td></tr><tr><td>25</td><td>CAN0EN</td><td>CAN0 时钟使能由软件置位或复位0: 关闭 CAN0 时钟1: 开启 CAN0 时钟</td></tr><tr><td>24:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1 时钟使能由软件置位或复位0: 关闭 I2C1 时钟1: 开启 I2C1 时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0 时钟使能由软件置位或复位0: 关闭 I2C0 时钟1: 开启 I2C0 时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4 时钟使能由软件置位或复位0: 关闭 UART4 时钟1: 开启 UART4 时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3 时钟使能由软件置位或复位0: 关闭 UART3 时钟1: 开启 UART3 时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2 时钟使能由软件置位或复位0: 关闭 USART2 时钟1: 开启 USART2 时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1 时钟使能由软件置位或复位0: 关闭 USART1 时钟1: 开启 USART1 时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13EN</td><td>TIMER13时钟使能由软件置位或复位0:关闭TIMER13时钟1:开启TIMER13时钟</td></tr><tr><td>7</td><td>TIMER12EN</td><td>TIMER12时钟使能由软件置位或复位0:关闭TIMER12时钟1:开启TIMER12时钟</td></tr><tr><td>6</td><td>TIMER11EN</td><td>TIMER11时钟使能由软件置位或复位0:关闭TIMER11时钟1:开启TIMER11时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6时钟使能由软件置位或复位0:关闭TIMER6时钟1:开启TIMER6时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5时钟使能由软件置位或复位0:关闭TIMER5时钟1:开启TIMER5时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4时钟使能由软件置位或复位0:关闭TIMER4时钟1:开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3 时钟使能由软件置位或复位0:关闭 TIMER3 时钟1:开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2 时钟使能由软件置位或复位0:关闭 TIMER2 时钟1:开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1 时钟使能由软件置位或复位0:关闭 TIMER1 时钟1:开启 TIMER1 时钟</td></tr></table>

## 5.6.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，只能由备份域复位进行复位。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的LXTALEN、LXTALBPS、RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC40K时钟作为RTC的时钟源11:选择CK_HXTAL/128时钟作为RTC的时钟源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值00:弱驱动能力01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能由软件置位或复位0:关闭LXTAL时钟1:使能LXTAL时钟</td></tr></table>

## 5.6.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C00 0000，所有复位标志位仅在电源复位时被清零，RSTFC/IRC40KEN在系统复位时被清零。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>保留</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="10">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC40KSTB</td><td>IRC40KEN</td></tr></table>

r rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用</td></tr></table>

1: 清除所有复位标志位

23:2 保留 必须保持复位值。

1 IRC40KSTB IRC40K 时钟稳定标志位
该位由硬件置 1 指示 IRC40K 输出时钟是否稳定待用

0: IRC40K 时钟未稳定

1: IRC40K 已稳定

0 IRC40KEN IRC40K 使能

由软件置位和复位

0: 关闭 IRC40K 时钟

1: 开启 IRC40K 时钟

## 5.6.11. AHB 复位寄存器（RCU_AHBRST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>ENETRS T</td><td>保留</td><td>USBFSR ST</td><td colspan="12">保留</td></tr></table>


rw    rw 



位/位域 名称 描述


<table><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>ENETRST</td><td>ENET 复位由软件置位或复位0:无作用1:复位 ENET</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>USBFSRST</td><td>USBFS 复位由软件置位或复位0:无作用1:复位 USBFS</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.12. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLL2MF[4]</td><td>PLLREPS EL</td><td>ADCPSC[3]</td><td colspan="10">保留</td><td>I2S2SEL</td><td>I2S1SEL</td><td>PREDV0 SEL</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">PLL2MF[3:0]</td><td colspan="4">PLL1MF[3:0]</td><td colspan="4">PREDV1[3:0]</td><td colspan="4">PREDV0[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLL2MF[4]</td><td>PLL2MF的第4位参考寄存器RCU_CFG1的12到15位</td></tr><tr><td>30</td><td>PLLPRESET</td><td>PLL时钟源预选择由软件置位或复位,控制PLL时钟源。0:HXTAL被选择为PLL时钟的时钟源1:CK_IRC48M被选择为PLL时钟的时钟源</td></tr><tr><td>29</td><td>ADCPSC[3]</td><td>ADCPSC的第3位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>28:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>I2S2SEL</td><td>I2S2时钟源选择由软件置位或复位,控制I2S2时钟源。0:系统时钟被选择为I2S2时钟的时钟源1:(CK_PLL2 x 2)被选择为I2S2时钟的时钟源</td></tr><tr><td>17</td><td>I2S1SEL</td><td>I2S1时钟源选择由软件置位或复位,控制I2S1时钟源。0:系统时钟被选择为I2S1时钟的时钟源1:(CK_PLL2 x 2)被选择为I2S1时钟的时钟源</td></tr><tr><td>16</td><td>PREDV0SEL</td><td>PREDV0时钟源选择由软件置位或复位0:HXTAL或IRC48M被选择为PREDV0的时钟源1:CK_PLL1被选择为PREDV0的时钟源</td></tr><tr><td>15:12</td><td>PLL2MF[3:0]</td><td>PLL2时钟倍频因子与寄存器RCU_CFG1的31位共同构成倍频因子,由软件置位或清零。000xx:保留0010x:保留00110:(PLL2源时钟x8)00111:(PLL2源时钟x9)01000:(PLL2源时钟x10)01001:(PLL2源时钟x11)</td></tr></table>

01010: (PLL2 源时钟 x 12)

01011: (PLL2 源时钟 x 13)

01100: (PLL2 源时钟 x 14)

01101: (PLL2 源时钟 x 15)

01110: (PLL2 源时钟 x 16)

01111: (PLL2 源时钟 x 20)

10000: (PLL2 源时钟 x 18)

10001: (PLL2 源时钟 x 19)

10010: (PLL2 源时钟 x 20)

10011: (PLL2 源时钟 x 21)

10100: (PLL2 源时钟 x 22)

10101: (PLL2 源时钟 x 23)

10110: (PLL2 源时钟 x 24)

10111: (PLL2 源时钟 x 25)

11000: (PLL2 源时钟 x 26)

11001: (PLL2 源时钟 x 27)

11010: (PLL2 源时钟 x 28)

11011: (PLL2 源时钟 x 29)

11100: (PLL2 源时钟 x 30)

11101: (PLL2 源时钟 x 31)

11110: (PLL2 源时钟 x 32)

11111: (PLL2 源时钟 x 40)

11:8 PLL1MF[3:0] PLL1时钟倍频因子

由软件置位或清零

00xx: 保留

010x: 保留

0110: (PLL1 源时钟 x 8)

0111: (PLL1 源时钟 x 9)

1000: (PLL1 源时钟 x 10)

1001: (PLL1 源时钟 x 11)

1010: (PLL1 源时钟 x 12)

1011: (PLL1 源时钟 x 13)

1100: (PLL1 源时钟 x 14)

1101: (PLL1 源时钟 x 15)

1110: (PLL1 源时钟 x 16)

1111: (PLL1 源时钟 x 20)

7:4 PREDV1[3:0] PREDV1 分频因子

由软件置位或清零，PLL1 和 PLL2 未使能时，可以修改这些位。

0000: PREDV1 输入源时钟未分频

0001: PREDV1 输入源时钟 2 分频

0010: PREDV1 输入源时钟 3 分频

0011: PREDV1 输入源时钟 4 分频

0100: PREDV1 输入源时钟 5 分频

<table><tr><td></td><td></td><td>0101: PREDV1 输入源时钟 6 分频0110: PREDV1 输入源时钟 7 分频0111: PREDV1 输入源时钟 8 分频1000: PREDV1 输入源时钟 9 分频1001: PREDV1 输入源时钟 10 分频1010: PREDV1 输入源时钟 11 分频1011: PREDV1 输入源时钟 12 分频1100: PREDV1 输入源时钟 13 分频1101: PREDV2 输入源时钟 14 分频1110: PREDV2 输入源时钟 15 分频1111: PREDV2 输入源时钟 16 分频</td></tr><tr><td>3:0</td><td>PREDV0[3:0]</td><td>PREDV0 分频因子由软件置位或清零,PLL 未使能时,可以修改这些位。注意:PREDV0 的第 0 位与 RCU_CFG0 寄存器的 17 位相同,修改 RCU_CFG0 寄存器的 17 位,PREDV0 的第 0 位也会进行相同的修改。0000: PREDV0 输入源时钟未分频0001: PREDV0 输入源时钟 2 分频0010: PREDV0 输入源时钟 3 分频0011: PREDV0 输入源时钟 4 分频0100: PREDV0 输入源时钟 5 分频0101: PREDV0 输入源时钟 6 分频0110: PREDV0 输入源时钟 7 分频0111: PREDV0 输入源时钟 8 分频1000: PREDV0 输入源时钟 9 分频1001: PREDV0 输入源时钟 10 分频1010: PREDV0 输入源时钟 11 分频1011: PREDV0 输入源时钟 12 分频1100: PREDV0 输入源时钟 13 分频1101: PREDV0 输入源时钟 14 分频1110: PREDV0 输入源时钟 15 分频1111: PREDV0 输入源时钟 16 分频</td></tr></table>

## 5.6.13. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为缺省值001:在深度睡眠模式下内核电压为(缺省值-0.1)V(不建议客户使用)010:在深度睡眠模式下内核电压为(缺省值-0.2)V(不建议客户使用)011:在深度睡眠模式下内核电压为(缺省值-0.3)V(不建议客户使用)1xx:保留</td></tr></table>

## 5.6.14. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0x8000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">保留</td><td>IRC48MSTB</td><td>IRC48MEN</td></tr><tr><td colspan="14">r</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>CK48MSEL</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB[7:0]</td><td>内部48MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部48MHz RC振荡器时钟稳定标志位硬件置‘1’来指示IRC48M振荡器时钟是否稳定待用0: IRC48M未稳定1: IRC48M已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部48MHz RC 振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位。0: 关闭IRC48M时钟1: 打开IRC48M时钟</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CK48MSEL</td><td>48MHz时钟源选择由软件置位和复位。该位用于选择IRC48M时钟或PLL48M时钟作为CK48M时钟源。</td></tr></table>

CK48M时钟用于:

0: 不选择IRC48M时钟（使用CK_PLL/USBFSPSC时钟）

1: 选择IRC48M时钟

## 5.6.15. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>IRC48MSTBIC</td><td colspan="6">保留</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>IRC48MSTBIE</td><td colspan="7">保留</td><td>IRC48MSTBIF</td><td colspan="6">保留</td></tr><tr><td colspan="9">rw</td><td colspan="7">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部 48 MHz RC 振荡器稳定中断清零软件写 1 复位 IRC48MSTBIF 标志位0:不复位 IRC48MSTBIF 标志位1:复位 IRC48MSTBIF 标志位</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部 48 MHz RC 振荡器稳定中断使能由软件置位和复位来使能/禁止 IRC48M 时钟稳定中断0:禁止 IRC48M 时钟稳定中断1:使能 IRC48M 时钟稳定中断</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M 时钟稳定中断标志位当内部 48 MHz RC 振荡器时钟稳定且 IRC48MSTBIE 位被置 1 时由硬件置 1 软件置位 IRC48MSTBIC 位时清除该位0:无 IRC48M 时钟稳定中断产生1:产生 IRC48M 时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.16. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTC RST</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.17. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC时钟使能由软件置位或复位0:关闭CTC时钟1:开启CTC时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
