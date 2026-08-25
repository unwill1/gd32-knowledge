## 9.3. RCU 寄存器

RCU 基地址：0x4002 1000

## 9.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83 x 表示未定义

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>PLL1STB</td><td>PLL1EN</td><td>PLL0STB</td><td>PLL0EN</td><td colspan="4">保留</td><td>HCKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td colspan="4"></td><td>r</td><td>rw</td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MSTB</td><td>IRC8MEN</td></tr><tr><td colspan="8">r</td><td colspan="6">rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>PLL1STB</td><td>PLL1时钟稳定标志位硬件置1来表示PLL1输出时钟是否稳定待用0:PLL1未稳定1:PLL1已稳定</td></tr><tr><td>26</td><td>PLL1EN</td><td>PLL1使能软件置位或复位,当PLL1时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL1被关闭1:PLL1被打开</td></tr><tr><td>25</td><td>PLL0STB</td><td>PLL0时钟稳定标志位硬件置1来表示PLL0输出时钟是否稳定待用0:PLL0未稳定1:PLL0已稳定</td></tr><tr><td>24</td><td>PLL0EN</td><td>PLL0使能软件置位或复位,当PLL0时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL0被关闭</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>HCKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~40MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~40MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清HCKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式,HXTAL输出时钟等于输入时钟。</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:高速4~40MHz晶体振荡器被关闭1:高速4~40MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部8MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部8MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整IRC8M到8MHz±1%。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M内部8MHz RC振荡器稳定标志位硬件置‘1’来指示IRC8M振荡器时钟是否稳定待用0:IRC8M振荡器未稳定1:IRC8M振荡器已稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部8MHz RC振荡器使能软件置位或复位,如果IRC8M时钟做为系统时钟时,该位不能被复位。当从深度</td></tr></table>
睡眠或待机模式返回，或当 CKMEN 置位同时用作系统时钟的 HXTAL 振荡器发生故障时，该位由硬件置 1 来启动 IRC8M振荡器。

0：内部 8MHz RC 振荡器被关闭

1：内部 8MHz RC 振荡器被打开

## 9.3.2. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x0010 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>USBFSPSC[2]</td><td colspan="2">PLL0MF[5:4]</td><td>ADCPSC[2]</td><td>保留</td><td colspan="3">CKOUTSEL[2:0]</td><td colspan="2">USBFSPSC[1:0]</td><td colspan="4">PLL0MF[3:0]</td><td>PREDIVO_LSB</td><td>保留</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td></td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]</td><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>USBFSPSC[2]</td><td>USBFSPSC的第2位参考寄存器RCU_CFG0的22到23位</td></tr><tr><td>30:29</td><td>PLL0MF[5:4]</td><td>PLL0MF的第5位和第4位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>28</td><td>ADCPSC[2]</td><td>ADCPSC的第2位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>CKOUTSEL[2:0]</td><td>CKOUT时钟源选择由软件置位或清零000:选择系统时钟CK_SYS001:选择内部8MHz RC振荡器时钟010:选择高速晶体振荡器时钟(HXTAL)011:选择(CK_PLL0/2)时钟100:选择(CK_PLL1/2)时钟101:选择低速晶体振荡器时钟(LXTAL)110:选择内部48MHz RC振荡器时钟111:选择内部40KHz RC振荡器时钟</td></tr><tr><td>23:22</td><td>USBFSPSC[1:0]</td><td>USBFS的时钟分频系数由软件置位或清零。USBFS的时钟必须为48MHz,当USBFS时钟使能的时候,这些位无法修改</td></tr><tr><td></td><td></td><td>000: CK_USBFS = CK_PLL0 / 3</td></tr><tr><td></td><td></td><td>001: CK_USBFS = CK_PLL0 / 2</td></tr><tr><td></td><td></td><td>010: CK_USBFS = CK_PLL0 / 5</td></tr><tr><td></td><td></td><td>011: CK_USBFS = CK_PLL0 / 4</td></tr><tr><td></td><td></td><td>100: CK_USBFS = CK_PLL0 / 6</td></tr><tr><td></td><td></td><td>101: CK_USBFS = CK_PLL0 / 7</td></tr><tr><td></td><td></td><td>11x: CK_USBFS = CK_PLL0 / 8</td></tr><tr><td>21:18</td><td>PLL0MF[3:0]</td><td>PLL0时钟倍频因子与寄存器RCU_CFG0的29,30位共同构成倍频因子,由软件置位或清零注意:PLL0输出时钟频率不能超过200MHz(适用于GD32F502xx),PLL0输出时钟频率不能超过252MHz(适用于GD32F503xx),PLL0输出时钟频率不能超过280MHz(适用于GD32F505xx)。0000xx:保留000100:(PLL时钟源x4)000101:(PLL时钟源x5)000110:(PLL时钟源x6)...111111:(PLL时钟源x63)</td></tr><tr><td>17</td><td>PREDIV0_LSB</td><td>PREDIV0分频因子的最低位与寄存器RCU_CFG1位PREDIV0第0位相同,通过寄存器RCU_CFG1来改变PREDIV0的值,此位也会一同改。当PREDIV0的第1到3位未修改时,此位决定PREDIV0的输入时钟是否二分频。</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>ADCPSC[1:0]</td><td>ADC的时钟分频系数与寄存器RCU_CFG0的28位,寄存器RCU_CFG1的29位共同构成分频因子,由软件置位或清零。0000:CK_ADC=CK_APB2/20001:CK_ADC=CK_APB2/40010:CK_ADC=CK_APB2/60011:CK_ADC=CK_APB2/80100:CK_ADC=CK_APB2/20101:CK_ADC=CK_APB2/120110:CK_ADC=CK_APB2/80111:CK_ADC=CK_APB2/161000:CK_ADC=CK_AHB/31100:CK_ADC=CK_AHB/51x01:CK_ADC=CK_AHB/61x10:CK_ADC=CK_AHB/101x11: CK_ADC = CK_AHB / 20</td></tr><tr><td>13:11</td><td>APB2PSC[2:0]</td><td>APB2 预分频选择由软件置位或清零,控制 APB2 时钟分频因子。0xx: CK_APB2 = CK_AHB100: CK_APB2 = CK_AHB / 2101: CK_APB2 = CK_AHB / 4110: CK_APB2 = CK_AHB / 8111: CK_APB2 = CK_AHB / 16</td></tr><tr><td>10:8</td><td>APB1PSC[2:0]</td><td>APB1 预分频选择由软件置位或清零,控制 APB1 时钟分频因子。0xx: CK_APB1 = CK_AHB100: CK_APB1 = CK_AHB / 2101: CK_APB1 = CK_AHB / 4110: CK_APB1 = CK_AHB / 8111: CK_APB1 = CK_AHB / 16</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB 预分频选择由软件置位或清零,控制 AHB 时钟分频因子。0xxx: CK_AHB = CK_SYS1000: CK_AHB = CK_SYS / 21001: CK_AHB = CK_SYS / 41010: CK_AHB = CK_SYS / 81011: CK_AHB = CK_SYS / 161100: CK_AHB = CK_SYS / 641101: CK_AHB = CK_SYS / 1281110: CK_AHB = CK_SYS / 2561111: CK_AHB = CK_SYS / 512</td></tr><tr><td>3:2</td><td>SCSS[1:0]</td><td>系统时钟选择状态由硬件置位或清零,标识当前系统时钟的时钟源。00: 选择 CK_IRC8M 时钟作为 CK_SYS 时钟源01: 选择 CK_HXTAL 时钟作为 CK_SYS 时钟源10: 选择 CK_PLL0P 时钟作为 CK_SYS 时钟源11: 保留</td></tr><tr><td>1:0</td><td>SCS[1:0]</td><td>系统时钟选择由软件配置选择系统时钟源。由于 CK_SYS 的改变存在固有的延迟,因此软件应当读 SCSS 位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时,以及当 HXTAL 直接或间接作为系统时钟同时 HXTAL 时钟监视器检测到 HXTAL 故障时,强制选择 IRC8M 作为系统时钟。00: 选择 CK_IRC8M 时钟作为 CK_SYS 时钟源01: 选择 CK_HXTAL 时钟作为 CK_SYS 时钟源</td></tr></table>

10：选择 CK_PLL0P 时钟作为 CK_SYS 时钟源

11：保留

## 9.3.3. 时钟中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>LCKMIF</td><td>LCKMIC</td><td>HCKMIC</td><td>保留</td><td>PLL1STBIC</td><td>PLLOSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC40KSTBIC</td></tr><tr><td colspan="6"></td><td>r</td><td>w</td><td>w</td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>LCKMIE</td><td>保留</td><td>PLL1STBIE</td><td>PLL0STBIE</td><td>HXTALSTBIE</td><td>IRC8MSTBIE</td><td>LXTALSTBIE</td><td>IRC40KSTBIE</td><td>HCKMIF</td><td>保留</td><td>PLL1STBIF</td><td>PLLOSTBIF</td><td>HXTALSTBIF</td><td>IRC8MSTBIF</td><td>LXTALSTBIF</td><td>IRC40KSTBIF</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>LCKMIF</td><td>LXTAL 时钟阻塞中断标志位当 LXTAL 时钟被阻塞时由硬件置位软件置位 LCKMIC 位时清除该位0:时钟正常运行1:LXTAL 时钟阻塞</td></tr><tr><td>24</td><td>LCKMIC</td><td>LXTAL 时钟阻塞中断清零软件写 1 复位 LCKMIF 标志位0:不复位 LCKMIF 标志位1:复位 LCKMIF 标志位</td></tr><tr><td>23</td><td>HCKMIC</td><td>HXTAL 时钟阻塞中断清零软件写 1 复位 HCKMIF 标志位0:不复位 HCKMIF 标志位1:复位 HCKMIF 标志位</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>PLL1STBIC</td><td>PLL1 时钟稳定中断清零软件写 1 复位 PLL1STBIF 标志位0:不复位 PLL1STBIF 标志位1:复位 PLL1STBIF 标志位</td></tr></table>

<table><tr><td>20</td><td>PLL0STBIC</td><td>PLL0时钟稳定中断清零软件写1复位PLL0STBIF标志位0:不复位PLL0STBIF标志位1:复位PLL0STBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M时钟稳定中断清零软件写1复位IRC8MSTBIF标志位0:不复位IRC8MSTBIF标志位1:复位IRC8MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0:不复位LXTALSTBIF标志位1:复位LXTALSTBIF标志位</td></tr><tr><td>16</td><td>IRC40KSTBIC</td><td>IRC40K时钟稳定中断清零软件写1复位IRC40KSTBIF标志位0:不复位IRC40KSTBIF标志位1:复位IRC40KSTBIF标志位</td></tr><tr><td>15</td><td>LCKMIE</td><td>LXTAL时钟阻塞中断使能软件置位和复位来使能/禁止LXTAL时钟阻塞中断0:禁止LXTAL时钟阻塞中断1:使能LXTAL时钟阻塞中断</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>PLL1STBIE</td><td>PLL1时钟稳定中断使能软件置位和复位来使能/禁止PLL1时钟稳定中断0:禁止PLL1时钟稳定中断1:使能PLL1时钟稳定中断</td></tr><tr><td>12</td><td>PLL0STBIE</td><td>PLL0时钟稳定中断使能软件置位和复位来使能/禁止PLL0时钟稳定中断0:禁止PLL0时钟稳定中断1:使能PLL0时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0:禁止HXTAL时钟稳定中断</td></tr></table>

<table><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M时钟稳定中断使能软件置位和复位来使能/禁止IRC8M时钟稳定中断0:禁止IRC8M时钟稳定中断1:使能IRC8M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC40KSTBIE</td><td>IRC40K时钟稳定中断使能软件置位和复位来使能/禁止IRC40K时钟稳定中断0:禁止IRC40K时钟稳定中断1:使能IRC40K时钟稳定中断</td></tr><tr><td>7</td><td>HCKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位软件置位HCKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>PLL1STBIF</td><td>PLL1时钟稳定中断标志位当PLL时钟稳定且PLL1STBIE位被置1时由硬件置1软件置位PLL1STBIC位时清除该位0:无PLL1时钟稳定中断产生1:产生PLL1时钟稳定中断</td></tr><tr><td>4</td><td>PLL0STBIF</td><td>PLL0时钟稳定中断标志位当PLL0时钟稳定且PLL0STBIE位被置1时由硬件置1软件置位PLL0STBIC位时清除该位0:无PLL0时钟稳定中断产生1:产生PLL0时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~40MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC40KSTBIF</td><td>IRC40K时钟稳定中断标志位当内部40kHz RC振荡器时钟稳定且IRC40KSTBIE位被置1时由硬件置1软件置位IRC40KSTBIC位时清除该位0:无IRC40K时钟稳定中断产生1:产生IRC40K时钟稳定中断</td></tr></table>

## 9.3.4. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CAN1RS T</td><td>CAN0RS T</td><td>SYSCFG RST</td><td>TRIGSEL RST</td><td colspan="3">保留</td><td>TIMER15 RST</td><td colspan="4">保留</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2RS T</td><td>USART0 RST</td><td>TIMER7R ST</td><td>SPI0RST</td><td>TIMER0R ST</td><td>ADC1RS T</td><td>ADC0RS T</td><td colspan="2">保留</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td><td>AFRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>26</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>25</td><td>SYSCFGRST</td><td>SYSCFG 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 SYSCFG</td></tr><tr><td>24</td><td>TRIGSELRST</td><td>TRIGSEL 复位由软件置位或复位0:无作用1:复位 TRIGSEL</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>TIMER15RST</td><td>TIMER15 复位由软件置位或复位0:无作用1:复位 TIMER15</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2RST</td><td>ADC2 复位由软件置位或复位0:无作用1:复位 ADC2</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0:无作用1:复位 USART0</td></tr><tr><td>13</td><td>TIMER7RST</td><td>TIMER7 复位由软件置位或复位0:无作用1:复位 TIMER7</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>TIMER0RST</td><td>TIMER0 复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr><tr><td>10</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0:无作用</td></tr><tr><td>9</td><td>ADC0RST</td><td>ADC0复位由软件置位或复位0:无作用1:复位所有ADC0</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>PERST</td><td>GPIO端口E复位由软件置位或复位0:无作用1:复位GPIO端口E</td></tr><tr><td>5</td><td>PDRST</td><td>GPIO端口D复位由软件置位或复位0:无作用1:复位GPIO端口D</td></tr><tr><td>4</td><td>PCRST</td><td>GPIO端口C复位由软件置位或复位0:无作用1:复位GPIO端口C</td></tr><tr><td>3</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>2</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFRST</td><td>复用功能I/O复位由软件置位或复位0:无作用1:复位复用功能I/O</td></tr></table>

## 9.3.5. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x10

复位值：0x0000 0000


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACRST</td><td>PMURST</td><td>BKPIRST</td><td colspan="3">保留</td><td>CMPRST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>USART2RST</td><td>USART1RST</td><td>保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGTRST</td><td colspan="4">保留</td><td>TIMER16RST</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACRST</td><td>DAC 复位由软件置位或复位0:无作用1:复位 DAC</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>BKPIRST</td><td>BKPI 复位由软件置位或复位0:无作用1:复位 BKP</td></tr><tr><td>26:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CMPRST</td><td>CMP 复位由软件置位或复位0:无作用1:复位 CMP</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr></table>

<table><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用1:复位 UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0:无作用1:复位 UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0:无作用1:复位 USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0:无作用1:复位 USART1</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0:无作用1:复位 SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0:无作用1:复位 SPI1</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位0:无作用1:复位 WWDGT</td></tr><tr><td>10:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TIMER16RST</td><td>TIMER16 复位由软件置位或复位0:无作用1:复位 TIMER16</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 9.3.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移：0x14

复位值：0x0000 0014


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td>DMAMUXEN</td><td>TRNGEN</td><td>HAUEN</td><td>CAUEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>USBFSEN</td><td colspan="3">保留</td><td>EXMCEN</td><td>保留</td><td>CRCEN</td><td>保留</td><td>FMCSPEN</td><td>保留</td><td>SRAMSPEN</td><td>DMA1EN</td><td>DMA0EN</td></tr><tr><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>DMAMUXEN</td><td>DMAMUX时钟使能由软件置位或复位0:关闭DMAMUX时钟1:开启DMAMUX时钟</td></tr><tr><td>18</td><td>TRNGEN</td><td>TRNG时钟使能由软件置位或复位0:关闭TRNG时钟1:开启TRNG时钟</td></tr><tr><td>17</td><td>HAUEN</td><td>HAU时钟使能由软件置位或复位0:关闭HAU时钟1:开启HAU时钟</td></tr><tr><td>16</td><td>CAUEN</td><td>CAU时钟使能由软件置位或复位0:关闭CAU时钟1:开启CAU时钟</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>USBFSEN</td><td>USBFS时钟使能由软件置位或复位0:关闭USBFS时钟1:开启USBFS时钟</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EXMCEN</td><td>EXMC时钟使能由软件置位或复位0:关闭EXMC时钟1:开启EXMC时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0:关闭CRC时钟1:开启CRC时钟</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCSPEN</td><td>在睡眠模式下FMC时钟使能由软件置位或复位0:在睡眠模式下关闭FMC时钟1:在睡眠模式下开启FMC时钟</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPEN</td><td>在睡眠模式下SRAM时钟使能由软件置位或复位0:在睡眠模式下关闭SRAM时钟1:在睡眠模式下开启SRAM时钟</td></tr><tr><td>1</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭DMA1时钟1:开启DMA1时钟</td></tr><tr><td>0</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr></table>

## 9.3.7. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CAN1EN</td><td>CAN0EN</td><td>SYSCFG EN</td><td>TRIGSEL EN</td><td colspan="3">保留</td><td>TIMER15 EN</td><td colspan="4">保留</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2EN</td><td>USART0 EN</td><td>TIMER7E N</td><td>SPI0EN</td><td>TIMER0EN</td><td>ADC1EN</td><td>ADC0EN</td><td colspan="2">保留</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td><td>AFEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:28</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>27</td><td colspan="3">CAN1EN</td><td colspan="12">CAN1时钟使能由软件置位或复位0:关闭CAN1时钟1:开启CAN1时钟</td></tr></table>

<table><tr><td>26</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>25</td><td>SYSCFGEN</td><td>SYSCFG时钟使能由软件置位或复位0:关闭SYSCFG时钟1:开启SYSCFG时钟</td></tr><tr><td>24</td><td>TRIGSELEN</td><td>TRIGSEL时钟使能由软件置位或复位0:关闭TRIGSEL时钟1:开启TRIGSEL时钟</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>TIMER15EN</td><td>TIMER15时钟使能由软件置位或复位0:关闭TIMER15时钟1:开启TIMER15时钟</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭ADC2时钟1:开启ADC2时钟</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>13</td><td>TIMER7EN</td><td>TIMER7复位由软件置位或复位0:无作用1:复位TIMER7</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0复位由软件置位或复位0:无作用1:复位SPI0</td></tr><tr><td>11</td><td>TIMER0EN</td><td>TIMER0复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr><tr><td>10</td><td>ADC1EN</td><td>ADC1 时钟使能由软件置位或复位0:关闭 ADC1 时钟1:开启 ADC1 时钟</td></tr><tr><td>9</td><td>ADC0EN</td><td>ADC0 时钟使能由软件置位或复位0:关闭 ADC0 时钟1:开启 ADC0 时钟</td></tr><tr><td>8:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>PEEN</td><td>GPIO 端口 E 时钟使能由软件置位或复位0:关闭 GPIO 端口 E 时钟1:开启 GPIO 端口 E 时钟</td></tr><tr><td>5</td><td>PDEN</td><td>GPIO 端口 D 时钟使能由软件置位或复位0:关闭 GPIO 端口 D 时钟1:开启 GPIO 端口 D 时钟</td></tr><tr><td>4</td><td>PCEN</td><td>GPIO 端口 C 时钟使能由软件置位或复位0:关闭 GPIO 端口 C 时钟1:开启 GPIO 端口 C 时钟</td></tr><tr><td>3</td><td>PBEN</td><td>GPIO 端口 B 时钟使能由软件置位或复位0:关闭 GPIO 端口 B 时钟1:开启 GPIO 端口 B 时钟</td></tr><tr><td>2</td><td>PAEN</td><td>GPIO 端口 A 时钟使能由软件置位或复位0:关闭 GPIO 端口 A 时钟1:开启 GPIO 端口 A 时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFEN</td><td>复用功能 IO 时钟使能由软件置位或复位0:关闭复用功能 IO 时钟1:开启复用功能 IO 时钟</td></tr></table>

## 9.3.8. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x1C

复位值：0x1000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DACEN</td><td>PMUEN</td><td>BKPIEN</td><td colspan="3">保留</td><td>CMPEN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td colspan="4">保留</td><td>TIMER16EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置位或复位0:关闭DAC时钟1:开启DAC时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>27</td><td>BKPIEN</td><td>BKP时钟使能由软件置位或复位0:关闭BKP时钟1:开启BKP时钟</td></tr><tr><td>26:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CMPEN</td><td>CMP时钟使能由软件置位或复位0:关闭CMP时钟1:开启CMP时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr></table>

<table><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>TIMER16EN</td><td>TIMER16时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0: 关闭 TIMER16 时钟1: 开启 TIMER16 时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6 时钟使能由软件置位或复位0: 关闭 TIMER6 时钟1: 开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5 时钟使能由软件置位或复位0: 关闭 TIMER5 时钟1: 开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4 时钟使能由软件置位或复位0: 关闭 TIMER4 时钟1: 开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3 时钟使能由软件置位或复位0: 关闭 TIMER3 时钟1: 开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2 时钟使能由软件置位或复位0: 关闭 TIMER2 时钟1: 开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1 时钟使能由软件置位或复位0: 关闭 TIMER1 时钟1: 开启 TIMER1 时钟</td></tr></table>

## 9.3.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，只能由备份域复位进行复位。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的 LXTALEN、LXTALBPS、RTCSRC 和 RTCEN 位仅在备份域复位后才清 0。只有在电源控制寄存器（PMU_CTL）中的 BKPWEN 位置 1 后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>保留</td><td>BKPRST</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td>LXTALRD YRST</td><td>LCKMD</td><td>LCKMEN</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALST B</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="2">rw</td><td>w</td><td>r</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC40K时钟作为RTC的时钟源11:选择CK_HXTAL/128时钟作为RTC的时钟源</td></tr><tr><td>7</td><td>LXTALRDYRST</td><td>LXTAL就绪复位0:LXTAL就绪时不复位1:LXTAL就绪时复位</td></tr><tr><td>6</td><td>LCKMD</td><td>LXTAL时钟故障检测由硬件置位,当外部32KHz振荡器(LXTAL)上的时钟安全系统检测到故障。当LCKMEN或LXTALEN关闭时,该位清零。0:LXTAL(32KHz振荡器)上未检测到故障1:在LXTAL(32KHz振荡器)上检测到故障</td></tr><tr><td>5</td><td>LCKMEN</td><td>LXTAL时钟监视器使能0:禁止LXTAL时钟监视器1:使能LXTAL时钟监视器通过软件设置,启用LXTAL(32KHz振荡器)上的时钟安全系统。LCKMEN必须在LXTAL已启用(LXTALEN位已启用)和就绪(LXTALSTB标志由硬件设置)。注意:一旦该位被置位,该位可以通过备份域复位清除或者在检测到LXTAL时钟故障后(LCKMD=1)通过复位LCKMEN清除。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值00:弱驱动能力01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能由软件置位或复位0:关闭LXTAL时钟1:使能LXTAL时钟</td></tr></table>

## 9.3.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C00 0000, 所有复位标志位仅在电源复位时被清零，RSTFC/IRC40KEN 在系统复位时被清零。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>保留</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="10">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC40KSTB</td><td>IRC40KEN</td></tr><tr><td colspan="14">位/位域</td><td>名称</td><td>描述</td></tr><tr><td colspan="14">31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td colspan="14">30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td colspan="14">29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td colspan="14">28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td colspan="14">27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td colspan="14">26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td colspan="14">25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td colspan="14">24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用1:清除所有复位标志位</td></tr></table>

<table><tr><td>23:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC40KSTB</td><td>IRC40K时钟稳定标志位该位由硬件置1指示IRC40K输出时钟是否稳定待用0:IRC40K时钟未稳定1:IRC40K已稳定</td></tr><tr><td>0</td><td>IRC40KEN</td><td>IRC40K使能由软件置位和复位0:关闭IRC40K时钟1:开启IRC40K时钟</td></tr></table>

## 9.3.11. AHB 复位寄存器（RCU_AHBRST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td>DMA1RS T</td><td>DMA0RS T</td><td>DMAMUX RST</td><td>TRNGRS T</td><td>HAURST</td><td>CAURST</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>USBFSR ST</td><td colspan="12">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>DMA1RST</td><td>DMA1 复位由软件置位或复位0:无作用1:复位 DMA1</td></tr><tr><td>20</td><td>DMA0RST</td><td>DMA0 复位由软件置位或复位0:无作用1:复位 DMA0</td></tr><tr><td>19</td><td>DMAMUXRST</td><td>DMAMUX 复位由软件置位或复位0:无作用</td></tr><tr><td>18</td><td>TRNGRST</td><td>TRNG 复位由软件置位或复位0:无作用1:复位 TRNG</td></tr><tr><td>17</td><td>HAURST</td><td>HAU 复位由软件置位或复位0:无作用1:复位 HAU</td></tr><tr><td>16</td><td>CAURST</td><td>CAU 复位由软件置位或复位0:无作用1:复位 CAU</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>USBFSRST</td><td>USBFS 复位由软件置位或复位0:无作用1:复位 USBFS</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 9.3.12. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0400

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>ADCPSC[3]</td><td colspan="5">IRC40KCALIB[4:0]</td><td colspan="2">保留</td><td colspan="2">PLL0SEL[1:0]</td><td>HXTALRDYRST</td><td>I2S2SEL</td><td>I2S1SEL</td><td>PLL1SEL</td></tr><tr><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>r</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td></td><td colspan="5">PLL1MF[5:0]</td><td colspan="4">PREDIV1[3:0]</td><td colspan="4">PREDIV0[3:0]</td></tr><tr><td colspan="2"></td><td></td><td colspan="5">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>ADCPSC[3]</td><td>ADCPSC的第3位</td></tr></table>

<table><tr><td></td><td></td><td>参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>28:24</td><td>IRC40KCALIB[4:0]</td><td>内部40KHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>PLL0SEL[1:0]</td><td>PLL0时钟源选择通过软件置位和复位控制PLL0时钟源。00:选择IRC8M时钟作为PLL0的时钟源01:选择IRC48M时钟作为PLL0的时钟源10:选择HXTAL时钟作为PLL0的时钟源11:选择CK_PLL1时钟作为PLL0的时钟源</td></tr><tr><td>19</td><td>HXTALRDYRST</td><td>HXTAL就绪复位0:HXTAL就绪不复位1:HXTAL就绪复位</td></tr><tr><td>18</td><td>I2S2SEL</td><td>I2S2时钟源选择由软件置位或复位,控制I2S2时钟源。0:系统时钟被选择为I2S2时钟的时钟源1:CK_PLL1被选择为I2S2时钟的时钟源</td></tr><tr><td>17</td><td>I2S1SEL</td><td>I2S1时钟源选择由软件置位或复位,控制I2S1时钟源。0:系统时钟被选择为I2S1时钟的时钟源1:CK_PLL1被选择为I2S1时钟的时钟源</td></tr><tr><td>16</td><td>PLL1SEL</td><td>PLL1时钟源选择通过软件置位和复位控制PLL1时钟源。0:选择HXTAL时钟作为PLL1的时钟源1:选择IRC48M时钟作为PLL1的时钟源</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>PLL1MF[3:0]</td><td>PLL1时钟倍频因子由软件置位或清零0000xx:保留000100:(PLL1源时钟x4)000101:(PLL1源时钟x5)...111111:(PLL1源时钟x63)</td></tr><tr><td>7:4</td><td>PREDIV1[3:0]</td><td>PREDIV1分频因子由软件置位或清零,PLL1未使能时,可以修改这些位。</td></tr></table>

<table><tr><td>0000:</td><td>PREDIV1 输入源时钟未分频</td></tr><tr><td>0001:</td><td>PREDIV1 输入源时钟 2 分频</td></tr><tr><td>0010:</td><td>PREDIV1 输入源时钟 3 分频</td></tr><tr><td>0011:</td><td>PREDIV1 输入源时钟 4 分频</td></tr><tr><td>0100:</td><td>PREDIV1 输入源时钟 5 分频</td></tr><tr><td>0101:</td><td>PREDIV1 输入源时钟 6 分频</td></tr><tr><td>0110:</td><td>PREDIV1 输入源时钟 7 分频</td></tr><tr><td>0111:</td><td>PREDIV1 输入源时钟 8 分频</td></tr><tr><td>1000:</td><td>PREDIV1 输入源时钟 9 分频</td></tr><tr><td>1001:</td><td>PREDIV1 输入源时钟 10 分频</td></tr><tr><td>1010:</td><td>PREDIV1 输入源时钟 11 分频</td></tr><tr><td>1011:</td><td>PREDIV1 输入源时钟 12 分频</td></tr><tr><td>1100:</td><td>PREDIV1 输入源时钟 13 分频</td></tr><tr><td>1101:</td><td>PREDIV1 输入源时钟 14 分频</td></tr><tr><td>1110:</td><td>PREDIV1 输入源时钟 15 分频</td></tr><tr><td>1111:</td><td>PREDIV1 输入源时钟 16 分频</td></tr></table>

<table><tr><td>注意: PREDV0 的第 0 位与 RCU_CFG 寄存器的 17 位, PREDV0 的第 0 位也</td></tr><tr><td>0000: PREDIV0 输入源时钟未分频</td></tr><tr><td>0001: PREDIV0 输入源时钟 2 分频</td></tr><tr><td>0010: PREDIV0 输入源时钟 3 分频</td></tr><tr><td>0011: PREDIV0 输入源时钟 4 分频</td></tr><tr><td>0100: PREDIV0 输入源时钟 5 分频</td></tr><tr><td>0101: PREDIV0 输入源时钟 6 分频</td></tr><tr><td>0110: PREDIV0 输入源时钟 7 分频</td></tr><tr><td>0111: PREDIV0 输入源时钟 8 分频</td></tr><tr><td>1000: PREDIV0 输入源时钟 9 分频</td></tr><tr><td>1001: PREDIV0 输入源时钟 10 分频</td></tr><tr><td>1010: PREDIV0 输入源时钟 11 分频</td></tr><tr><td>1011: PREDIV0 输入源时钟 12 分频</td></tr><tr><td>1100: PREDIV0 输入源时钟 13 分频</td></tr><tr><td>1101: PREDIV0 输入源时钟 14 分频</td></tr><tr><td>1110: PREDIV0 输入源时钟 15 分频</td></tr><tr><td>1111: PREDIV0 输入源时钟 16 分频</td></tr></table>

## 9.3.13. PLL 带宽配置寄存器（RCU_PLLBWCFG）

地址偏移：0x30

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">PLL1_BW_CFG[3:0]</td><td colspan="4">保留</td><td colspan="4">PLL0_BW_CFG[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>PLL1_BW_CFG[3:0]</td><td>PLL1 带宽配置Bit[2]和 Bit[0]在进入 PLL1 模拟接口之前取反</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>PLL0_BW_CFG[3:0]</td><td>PLL0 带宽配置Bit[2]和 Bit[0]在进入 PLL0 模拟接口之前取反</td></tr></table>

## 9.3.14. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x34

复位值：0x000A 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">SWDLY[4:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>SWDLY[4:0]</td><td>切换延迟时间当进入深度睡眠模式时,切换到IRC8M时钟,需等待SWDLY个IRC8M时钟周期,然后进入深度睡眠模式。默认为10个IRC8M时钟。注意:不要配置为0,因为它是一个序列。</td></tr><tr><td>15:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为缺省值001:在深度睡眠模式下内核电压为(缺省值-0.05)V010:在深度睡眠模式下内核电压为(缺省值-0.1)V011:在深度睡眠模式下内核电压为(缺省值-0.15)V100:在深度睡眠模式下内核电压为(缺省值-0.2)V101:在深度睡眠模式下内核电压为(缺省值-0.25)V110:在深度睡眠模式下内核电压为(缺省值-0.3)V(不建议客户使用)111:在深度睡眠模式下内核电压为(缺省值-0.35)V(不建议客户使用)</td></tr></table>

## 9.3.15. 时钟频率监视器配置寄存器 0（RCU_CKFMCFG0）

地址偏移：0x40

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>IRC8MCKFFIE</td><td>IRC8MCKFFC</td><td>IRC8MCKFFF</td><td colspan="2">IRC8MCKFMC[1:0]</td><td>IRC8MCKFMEN</td></tr><tr><td colspan="10"></td><td>rw</td><td>w</td><td>r</td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>IRC8MCKFFIE</td><td>IRC8M时钟频率故障中断使能该位由软件置位和复位。0:关闭IRC8M时钟频率故障中断1:使能IRC8M时钟频率故障中断</td></tr><tr><td>4</td><td>IRC8MCKFFC</td><td>IRC8M时钟频率故障标志清除用软件编写1复位IRC8MCKFFF标志,并在IRC8MCKFFF被清除后由硬件自动复位。0:不复位IRC8MCKFFF标志1:复位IRC8MCKFFF标志位</td></tr><tr><td>3</td><td>IRC8MCKFFF</td><td>IRC8M时钟频率故障标志该位表示IRC8M时钟频率是否超出监控范围。0:IRC8M时钟频率未超出监控范围1:IRC8M时钟频率超出监控范围</td></tr><tr><td>2:1</td><td>IRC8MCKFMC[1:0]</td><td>IRC8M时钟频率监视器配置该位由软件设置和复位。00:时钟频率监控范围为<eq>8\mathrm{M}\mathrm{{Hz}} \pm 5\%</eq>01:时钟频率监控范围为<eq>8\mathrm{M}\mathrm{{Hz}} \pm {10}\%</eq>10:时钟频率监控范围为<eq>8\mathrm{M}\mathrm{{Hz}} \pm {15}\%</eq>11:时钟频率监控范围为<eq>8\mathrm{M}\mathrm{{Hz}} \pm {20}\%</eq></td></tr><tr><td>0</td><td>IRC8MCKFMEN</td><td>IRC8M时钟频率监控使能该位由软件设置和复位。0:关闭内部8M RC振荡器(IRC8M)时钟频率监视器1:使能内部8M RC振荡器(IRC8M)时钟频率监控器</td></tr></table>

## 9.3.16. 时钟频率监视器配置寄存器 1（RCU_CKFMCFG1）

地址偏移：0x44

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>HXTALCKFFC</td><td>HXTALCKFFF</td><td colspan="4">保留</td><td colspan="10">HXTALCKFFIE HXTALCKFMIN[11:0]</td></tr><tr><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">HXTALCKFMIN[11:0]</td><td colspan="12">HXTALCKFMAX[11:0]</td><td>HXTALCKFMEN</td></tr><tr><td colspan="6">rw</td><td colspan="9">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>HXTALCKFFC</td><td>HXTAL时钟频率故障标志清除用软件写1复位HXTALCKFFF标志,并在HXTALCKFFF被清除后由硬件自动复位。0:不复位HXTALCKFFF标志1:复位HXTALCKFFF标志位</td></tr><tr><td>30</td><td>HXTALCKFFF</td><td>HXTAL时钟频率故障标志该位表示HXTAL时钟频率是否超出监控范围。0:HXTAL时钟频率未超出监控范围1:HXTAL时钟频率超出监控范围</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>HXTALCKFFIE</td><td>HXTAL时钟频率故障中断使能该位由软件置位和复位。0:关闭HXTAL时钟频率故障中断</td></tr></table>

<table><tr><td></td><td></td><td>1:使能HXTAL时钟频率故障中断</td></tr><tr><td>24:13</td><td>HXTALCKFMIN[11:0]</td><td>HXTAL时钟频率监视器配置最小值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为1000个IRC48M时钟周期。</td></tr><tr><td>12:1</td><td>HXTALCKFMAX[11:0]</td><td>HXTAL时钟频率监视器配置最大值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为1000个IRC48M时钟周期。</td></tr><tr><td>0</td><td>HXTALCKFMEN</td><td>HXTAL时钟频率监控使能该位由软件设置和复位。0:关闭HXTAL时钟频率监视器1:使能HXTAL时钟频率监控器</td></tr></table>

## 9.3.17. 时钟频率监视器配置寄存器 2（RCU_CKFMCFG2）

地址偏移：0x48

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLL0PCKFFC</td><td>PLL0PCKFFF</td><td colspan="6">保留</td><td>PLL0PCKFFIE</td><td>保留</td><td colspan="6">PLL0PCKFMIN[9:0]</td></tr><tr><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">PLL0PCKFMIN[9:0]</td><td>保留</td><td colspan="10">PLL0PCKFMAX[9:0]</td><td>PLL0PCKFMEN</td></tr><tr><td colspan="8">rw</td><td colspan="7">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLL0PCKFFC</td><td>PLL0P时钟频率故障标志清除用软件写1复位PLL0PCKFFF标志,并在PLL0PCKFFF被清除后由硬件自动复位。0:不复位PLL0PCKFFF标志1:复位PLL0PCKFFF标志位</td></tr><tr><td>30</td><td>PLL0PCKFFF</td><td>PLL0P时钟频率故障标志该位表示PLL0P时钟频率是否超出监控范围。0:PLL0P时钟频率未超出监控范围1:PLL0P时钟频率超出监控范围</td></tr><tr><td>29:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PLL0PCKFFIE</td><td>PLL0P时钟频率故障中断使能该位由软件置位和复位。0: 关闭PLL0P时钟频率故障中断1: 使能PLL0P时钟频率故障中断</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:12</td><td>PLL0PCKFMIN[9:0]</td><td>PLL0P时钟频率监视器配置最小值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为100个IRC48M时钟周期。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:1</td><td>PLL0PCKFMAX[9:0]</td><td>PLL0P时钟频率监视器配置最大值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为100个IRC48M时钟周期。</td></tr><tr><td>0</td><td>PLL0PCKFMEN</td><td>PLL0P时钟频率监控使能该位由软件设置和复位。0: 关闭PLL0P时钟频率监视器1: 使能PLL0P时钟频率监控器</td></tr></table>

## 9.3.18. 时钟频率监视器配置寄存器 3（RCU_CKFMCFG3）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLL1CKFFC</td><td>PLL1CKFFF</td><td colspan="6">保留</td><td>PLL1CKFFIE</td><td>保留</td><td colspan="6">PLL1CKFMIN[9:0]</td></tr><tr><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">PLL1CKFMIN[9:0]</td><td>保留</td><td colspan="10">PLL1CKFMAX[9:0]</td><td>PLL1CKFMEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLL1CKFFC</td><td>PLL1时钟频率故障标志清除用软件写1复位PLL1CKFFF标志,并在PLL1CKFFF被清除后由硬件自动复位。0:不复位PLL1CKFFF标志1:复位PLL1CKFFF标志位</td></tr><tr><td>30</td><td>PLL1CKFFF</td><td>PLL1时钟频率故障标志该位表示PLL1时钟频率是否超出监控范围。0:PLL1时钟频率未超出监控范围1:PLL1时钟频率超出监控范围</td></tr><tr><td>29:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PLL1CKFFIE</td><td>PLL1时钟频率故障中断使能该位由软件置位和复位。0:关闭PLL1时钟频率故障中断1:使能PLL1时钟频率故障中断</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:12</td><td>PLL1CKFMIN[9:0]</td><td>PLL1时钟频率监视器配置最小值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为100个IRC48M时钟周期。</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:1</td><td>PLL1CKFMAX[9:0]</td><td>PLL1时钟频率监视器配置最大值该位由软件设置和复位。参考时钟为IRC48M,监控窗口为100个IRC48M时钟周期。</td></tr><tr><td>0</td><td>PLL1CKFMEN</td><td>PLL1时钟频率监控使能该位由软件设置和复位。0:关闭PLL1时钟频率监视器1:使能PLL1时钟频率监控器</td></tr></table>

## 9.3.19. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0x8000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td>保留</td><td colspan="5">I2S2DIV[4:0]</td><td>IRC48MS TB</td><td>IRC48ME N</td></tr><tr><td colspan="8">r</td><td colspan="6">rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">FMCDIV[3:0]</td><td colspan="4">PLL0DIV[3:0]</td><td colspan="5">I2S1DIV[4:0]</td><td colspan="2">FMCSEL[1:0]</td><td>CK48MS EL</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB[7:0]</td><td>内部48MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:18</td><td>I2S2DIV[4:0]</td><td>I2S2分频因子分频因子为I2S2DIV +1。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部48MHz RC振荡器时钟稳定标志位硬件置‘1’来指示IRC48M振荡器时钟是否稳定待用0: IRC48M未稳定1: IRC48M已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部48MHz RC 振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位。0: 关闭IRC48M时钟1: 打开IRC48M时钟</td></tr><tr><td>15:12</td><td>FMCDIV[3:0]</td><td>FMC分频因子分频因子为FMCDIV +1。注意: 在整个芯片的生命周期中,需确保FMC接口时钟大于等于CK_AHB时钟,但不超过CK_AHB时钟的7倍,否则可能发生不可预知的问题。</td></tr><tr><td>11:8</td><td>PLL0DIV[3:0]</td><td>PLL0分频因子分频因子为PLL0DIV +1。</td></tr><tr><td>7:3</td><td>I2S1DIV[4:0]</td><td>I2S1分频因子分频因子为I2S1DIV +1。</td></tr><tr><td>2:1</td><td>FMCSEL[1:0]</td><td>FMC时钟源选择通过软件置位和复位控制FMC时钟源00: 选择CK_AHB作为FMC时钟源01: 选择CK_SYS作为FMC时钟源10: 选择CK_PLL0作为FMC时钟源11: 选择CK_PLL1作为FMC时钟源注意: 在整个芯片的生命周期中,需确保FMC接口时钟大于等于CK_AHB时钟,但不超过CK_AHB时钟的7倍,否则可能发生不可预知的问题。</td></tr><tr><td>0</td><td>CK48MSEL</td><td>48MHz时钟源选择由软件置位和复位。该位用于选择IRC48M时钟或PLL48M时钟作为CK48M时钟源。CK48M时钟用于:0: 不选择IRC48M时钟(使用CK_PLL/USBFSPSC时钟)1: 选择IRC48M时钟</td></tr></table>

## 9.3.20. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>IRC48MS TBIC</td><td colspan="6">保留</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>IRC48MS TBIE</td><td colspan="7">保留</td><td>IRC48MS TBIF</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部 48 MHz RC 振荡器稳定中断清零软件写 1 复位 IRC48MSTBIF 标志位0:不复位 IRC48MSTBIF 标志位1:复位 IRC48MSTBIF 标志位</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部 48 MHz RC 振荡器稳定中断使能由软件置位和复位来使能/禁止 IRC48M 时钟稳定中断0:禁止 IRC48M 时钟稳定中断1:使能 IRC48M 时钟稳定中断</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M 时钟稳定中断标志位当内部 48 MHz RC 振荡器时钟稳定且 IRC48MSTBIE 位被置 1 时由硬件置 1 软件置位 IRC48MSTBIC 位时清除该位0:无 IRC48M 时钟稳定中断产生1:产生 IRC48M 时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 9.3.21. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTCRST</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 9.3.22. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC时钟使能由软件置位或复位0:关闭CTC时钟1:开启CTC时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 9.3.23. 上锁寄存器（RCU_LOCK）

地址偏移：0x100

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LOCK</td><td colspan="15">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LOCK</td><td>RCU 寄存器上锁位该位由软件置位和复位。0: RCU 寄存器可配置1: RCU 寄存器不可配置,只能读注意:当 LOCK = 1,写 RCU 寄存器时,会产生 HardFault 异常。</td></tr><tr><td>30:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
