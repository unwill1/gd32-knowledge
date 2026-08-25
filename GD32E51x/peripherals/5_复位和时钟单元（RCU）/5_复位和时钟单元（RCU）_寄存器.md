## 5.3. RCU 寄存器

RCU 基地址：0x4002 1000

## 5.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83，x 表示未定义

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>PLLSTB</td><td>PLLEN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td colspan="6"></td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MSTB</td><td>IRC8MEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~32MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~32MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止 HXTAL 旁路模式1:使能 HXTAL 旁路模式 HXTAL 输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示 HXTAL 振荡器时钟是否稳定待用0:HXTAL 振荡器未稳定1:HXTAL 振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果 HXTAL 时钟作为系统时钟或者当 PLL 时钟做为系统时钟时,其做为 PLL 的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位0:高速 4~32 MHz 晶体振荡器被关闭1:高速 4~32 MHz 晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部 8MHz RC 振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部 8MHz RC 振荡器时钟调整值这些位由软件置位,最终调整值为 IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整 IRC8M 到 8MHz ± 1%</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M 内部 8MHz RC 振荡器稳定标志位硬件置‘1’来指示 IRC8M 振荡器时钟是否稳定待用0:IRC8M 振荡器未稳定1:IRC8M 振荡器已稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部 8MHz RC 振荡器使能软件置位或复位,如果 IRC8M 时钟做为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当 CKMEN 置位同时用作系统时钟的 HXTAL 振荡器发生故障时,该位由硬件置 1 来启动 IRC8M 振荡器。0:内部 8MHz RC 振荡器被关闭1:内部 8MHz RC 振荡器被打开</td></tr></table>

## 5.3.2. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>USBDPSC[2]</td><td>PLLMF[5]</td><td>保留</td><td>ADCPSC[2]</td><td>PLLMF[4]</td><td colspan="3">CKOUT0SEL[2:0]</td><td colspan="2">USBDPSC[1:0]</td><td colspan="4">PLLMF[3:0]</td><td>PREDV0</td><td>PLLSEL</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]rw</td><td colspan="3">APB2PSC[2:0]rw</td><td colspan="3">APB1PSC[2:0]rw</td><td colspan="4">AHBPSC[3:0]rw</td><td colspan="2">SCSS[1:0]r</td><td colspan="2">SCS[1:0]rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>USBDPSC[2]</td><td>USBDPSC的第2位参考寄存器RCU_CFG0的22到23位</td></tr><tr><td>30</td><td>PLLMF[5]</td><td>PLLMF的第5位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>ADCPSC[2]</td><td>ADCPSC的第2位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>27</td><td>PLLMF[4]</td><td>PLLMF的第4位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>26:24</td><td>CKOUT0SEL[2:0]</td><td>CKOUT0时钟源选择由软件置位或清零0xx:无时钟输出100:选择系统时钟CK_SYS101:选择内部8M RC振荡器时钟110:选择高速晶体振荡器时钟(HXTAL)111:选择(CK_PLL/2)时钟</td></tr><tr><td>23:22</td><td>USBDPSC[1:0]</td><td>USBD的时钟分频系数由软件置位或清零。USBD的时钟必须为48MHz,当USBD时钟使能的时候,这些位无法修改000:CK_USBD=CK_PLL/1.5001:CK_USBD=CK_PLL010:CK_USBD=CK_PLL/2.5011:CK_USBD=CK_PLL/2100:CK_USBD=CK_PLL/3101:CK_USBD=CK_PLL/3.511x:CK_USBD=CK_PLL/4</td></tr><tr><td>21:18</td><td>PLLMF[3:0]</td><td>PLL时钟倍频因子与寄存器RCU_CFG0的27,30位共同构成倍频因子,由软件置位或清零注意:PLL输出时钟频率不能超过180MHz000000:(PLL源时钟x2)000001:(PLL源时钟x3)000010:(PLL源时钟x4)000011:(PLL源时钟x5)000100:(PLL源时钟x6)000101:(PLL源时钟x7)000110:(PLL源时钟x8)000111:(PLL源时钟x9)001000:(PLL源时钟x10)001001: (PLL源时钟 x 11)</td></tr><tr><td rowspan="27"></td><td rowspan="27"></td><td>001010: (PLL源时钟 x 12)</td></tr><tr><td>001011: (PLL源时钟 x 13)</td></tr><tr><td>001100: (PLL源时钟 x 14)</td></tr><tr><td>001101: (PLL源时钟 x 15)</td></tr><tr><td>001110: (PLL源时钟 x 16)</td></tr><tr><td>001111: (PLL源时钟 x 16)</td></tr><tr><td>010000: (PLL源时钟 x 17)</td></tr><tr><td>010001: (PLL源时钟 x 18)</td></tr><tr><td>010010: (PLL源时钟 x 19)</td></tr><tr><td>010011: (PLL源时钟 x 20)</td></tr><tr><td>010100: (PLL源时钟 x 21)</td></tr><tr><td>010101: (PLL源时钟 x 22)</td></tr><tr><td>010110: (PLL源时钟 x 23)</td></tr><tr><td>010111: (PLL源时钟 x 24)</td></tr><tr><td>011000: (PLL源时钟 x 25)</td></tr><tr><td>011001: (PLL源时钟 x 26)</td></tr><tr><td>011010: (PLL源时钟 x 27)</td></tr><tr><td>011011: (PLL源时钟 x 28)</td></tr><tr><td>011100: (PLL源时钟 x 29)</td></tr><tr><td>011101: (PLL源时钟 x 30)</td></tr><tr><td>011110: (PLL源时钟 x 31)</td></tr><tr><td>011111: (PLL源时钟 x 32)</td></tr><tr><td>100000: (PLL源时钟 x 33)</td></tr><tr><td>100001: (PLL源时钟 x 34)</td></tr><tr><td>...</td></tr><tr><td>111110: (PLL源时钟 x 63)</td></tr><tr><td>111111: (PLL源时钟 x 64)</td></tr><tr><td>17</td><td>PREDV0</td><td>PREDV0 分频因子由软件置位或清零,PLL未使能时,可以修改这些位0: PREDV0 输入源时钟未分频1: PREDV0 输入源时钟 2 分频</td></tr><tr><td>16</td><td>PLLSEL</td><td>PLL时钟源选择由软件置位或复位,控制PLL时钟源0: (IRC8M/2)被选择为PLL时钟的时钟源1: HXTAL时钟或者IRC48M时钟(寄存器RCU_CFG1位PLLPRESEL决定)被选择为PLL时钟的时钟源</td></tr><tr><td>15:14</td><td>ADCPSC[1:0]</td><td>ADC的时钟分频系数与寄存器RCU_CFG0的28位,寄存器RCU_CFG1的29位共同构成分频因子,由软件置位或清零0000: CK_ADC = CK_APB2 / 20001: CK_ADC = CK_APB2 / 40010: CK_ADC = CK_APB2 / 6</td></tr></table>

<table><tr><td></td><td></td><td>0011: CK_ADC = CK_APB2 / 80100: CK_ADC = CK_APB2 / 20101: CK_ADC = CK_APB2 / 120110: CK_ADC = CK_APB2 / 80111: CK_ADC = CK_APB2 / 161x00: CK_ADC = CK_AHB / 51x01: CK_ADC = CK_AHB / 61x10: CK_ADC = CK_AHB / 101x11: CK_ADC = CK_AHB / 20</td></tr><tr><td>13:11</td><td>APB2PSC[2:0]</td><td>APB2 预分频选择由软件置位或清零,控制 APB2 时钟分频因子0xx: 选择 CK_AHB 时钟不分频100: 选择 CK_AHB 时钟 2 分频101: 选择 CK_AHB 时钟 4 分频110: 选择 CK_AHB 时钟 8 分频111: 选择 CK_AHB 时钟 16 分频</td></tr><tr><td>10:8</td><td>APB1PSC[2:0]</td><td>APB1 预分频选择由软件置位或清零,控制 APB1 时钟分频因子.0xx: 选择 CK_AHB 时钟不分频100: 选择 CK_AHB 时钟 2 分频101: 选择 CK_AHB 时钟 4 分频110: 选择 CK_AHB 时钟 8 分频111: 选择 CK_AHB 时钟 16 分频</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB 预分频选择由软件置位或清零,控制 AHB 时钟分频因子.0xxx: 选择 CK_SYS 时钟不分频1000: 选择 CK_SYS 时钟 2 分频1001: 选择 CK_SYS 时钟 4 分频1010: 选择 CK_SYS 时钟 8 分频1011: 选择 CK_SYS 时钟 16 分频1100: 选择 CK_SYS 时钟 64 分频1101: 选择 CK_SYS 时钟 128 分频1110: 选择 CK_SYS 时钟 256 分频1111: 选择 CK_SYS 时钟 512 分频</td></tr><tr><td>3:2</td><td>SCSS[1:0]</td><td>系统时钟选择状态由硬件置位或清零,标识当前系统时钟的时钟源00: 选择 CK_IRC8M 时钟作为 CK_SYS 时钟源01: 选择 CK_HXTAL 时钟作为 CK_SYS 时钟源10: 选择 CK_PLL 时钟作为 CK_SYS 时钟源11: 保留</td></tr><tr><td>1:0</td><td>SCS[1:0]</td><td>系统时钟选择由软件配置选择系统时钟源。由于 CK_SYS 的改变</td></tr></table>

读 SCSS 位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时，以及当 HXTAL 直接或间接作为系统时钟同时 HXTAL 时钟监视器检测到 HXTAL 故障时，强制选择 IRC8M作为系统时钟。

00：选择 CK_IRC8M 时钟作为 CK_SYS 时钟源

01：选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10：选择 CK_PLL 时钟作为 CK_SYS 时钟源

11：保留

## 5.3.3. 时钟中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td colspan="2">保留</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC40KSTBIC</td></tr><tr><td colspan="8"></td><td>w</td><td colspan="2"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC8MSTBIE</td><td>LXTALSTBIE</td><td>IRC40KSTBIE</td><td>CKMIF</td><td colspan="2">保留</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC8MSTBIF</td><td>LXTALSTBIF</td><td>IRC40KSTBIF</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL 时钟阻塞中断清零软件写 1 复位 CKMIF 标志位.0: 不复位 CKMIF 标志位1: 复位 CKMIF 标志位</td></tr><tr><td>22:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL 时钟稳定中断清零软件写 1 复位 PLLSTBIF 标志位0: 不复位 PLLSTBIF 标志位1: 复位 PLLSTBIF 标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL 时钟稳定中断清零软件写 1 复位 HXTALSTBIF 标志位0: 不复位 HXTALSTBIF 标志位1: 复位 HXTALSTBIF 标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M 时钟稳定中断清零软件写 1 复位 IRC8MSTBIF 标志位0: 不复位 IRC8MSTBIF 标志位</td></tr></table>

<table><tr><td></td><td></td><td>1: 复位 IRC8MSTBIF 标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL 时钟稳定中断清零软件写 1 复位 LXTALSTBIF 标志位0: 不复位 LXTALSTBIF 标志位1: 复位 LXTALSTBIF 标志位</td></tr><tr><td>16</td><td>IRC40KSTBIC</td><td>IRC40K 时钟稳定中断清零软件写 1 复位 IRC40KSTBIF 标志位0: 不复位 IRC40KSTBIF 标志位1: 复位 IRC40KSTBIF 标志位</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL 时钟稳定中断使能软件置位和复位来使能/禁止 PLL 时钟稳定中断0: 禁止 PLL 时钟稳定中断1: 使能 PLL 时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL 时钟稳定中断使能软件置位和复位来使能/禁止 HXTAL 时钟稳定中断0: 禁止 HXTAL 时钟稳定中断1: 使能 HXTAL 时钟稳定中断</td></tr><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M 时钟稳定中断使能软件置位和复位来使能/禁止 IRC8M 时钟稳定中断0: 禁止 IRC8M 时钟稳定中断1: 使能 IRC8M 时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL 时钟稳定中断使能软件置位和复位来使能/禁止 LXTAL 时钟稳定中断0: 禁止 LXTAL 时钟稳定中断1: 使能 LXTAL 时钟稳定中断</td></tr><tr><td>8</td><td>IRC40KSTBIE</td><td>IRC40K 时钟稳定中断使能软件置位和复位来使能/禁止 IRC40K 时钟稳定中断0: 禁止 IRC40K 时钟稳定中断1: 使能 IRC40K 时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL 时钟阻塞中断标志位当 HXTAL 时钟被阻塞时由硬件置位.软件置位 CKMIC 位时清除该位0: 时钟正常运行1: HXTAL 时钟阻塞</td></tr><tr><td>6:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL 时钟稳定中断标志位当 PLL 时钟稳定且 PLLSTBIE 位被置 1 时由硬件置 1 软件置位 PLLSTBIC 位时清除该位</td></tr></table>

<table><tr><td></td><td></td><td>0:无PLL时钟稳定中断产生1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~32MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC40KSTBIF</td><td>IRC40K时钟稳定中断标志位当内部40kHz RC振荡器时钟稳定且IRC40KSTBIE位被置1时由硬件置1软件置位IRC40KSTBIC位时清除该位0:无IRC40K时钟稳定中断产生1:产生IRC40K时钟稳定中断</td></tr></table>

## 5.3.4. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMPRST</td><td>保留</td><td>SHRTIME RST</td><td>USART5 RST</td><td>保留</td><td>TIMER16 RST</td><td>TIMER15 RST</td><td>TIMER14 RST</td><td colspan="2">保留</td><td>TIMER10 RST</td><td>TIMER9 RST</td><td>TIMER8 RST</td><td colspan="3">保留</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2RS T</td><td>USART0 RST</td><td>TIMER7R ST</td><td>SPI0RST</td><td>TIMER0R ST</td><td>ADC1RS T</td><td>ADC0RS T</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td><td>AFRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMPRST</td><td>CMP 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>SHRTIMEREN</td><td>SHRTIMER 复位由软件置位或复位0:无作用1:复位 SHRTIMER</td></tr><tr><td>28</td><td>USART5EN</td><td>USART5 复位由软件置位或复位0:无作用1:复位 USART5</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TIMER16RST</td><td>TIMER16 复位由软件置位或复位0:无作用1:复位 TIMER16</td></tr><tr><td>25</td><td>TIMER15RST</td><td>TIMER15 复位由软件置位或复位0:无作用1:复位 TIMER15</td></tr><tr><td>24</td><td>TIMER14RST</td><td>TIMER14 复位由软件置位或复位0:无作用1:复位 TIMER14</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10RST</td><td>TIMER10 复位由软件置位或复位0:无作用1:复位 TIMER10</td></tr><tr><td>20</td><td>TIMER9RST</td><td>TIMER9 复位由软件置位或复位0:无作用1:复位 TIMER9</td></tr><tr><td>19</td><td>TIMER8RST</td><td>TIMER8 复位由软件置位或复位0:无作用1:复位 TIMER8</td></tr><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2RST</td><td>ADC2 复位</td></tr></table>

由软件置位或复位
0: 无作用
1: 复位所有 ADC2

14 USART0RST USART0 复位
由软件置位或复位
0: 无作用
1: 复位 USART0

13 TIMER7RST TIMER7 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER7

12 SPI0RST SPI0 复位
由软件置位或复位
0: 无作用
1: 复位 SPI0

11 TIMER0RST TIMER0 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER0

10 ADC1RST ADC1 复位
由软件置位或复位
0: 无作用
1: 复位所有 ADC1

9 ADC0RST ADC0 复位
由软件置位或复位
0: 无作用
1: 复位所有 ADC0

8 PGRST GPIO 端口 G 复位
由软件置位或复位
0: 无作用
1: 复位 GPIO 端口 G

7 PFRST GPIO 端口 F 复位
由软件置位或复位
0: 无作用
1: 复位 GPIO 端口 F

6 PERST GPIO 端口 E 复位
由软件置位或复位
0: 无作用
1: 复位 GPIO 端口 E

<table><tr><td>5</td><td>PDRST</td><td>GPIO端口D复位由软件置位或复位0:无作用1:复位GPIO端口D</td></tr><tr><td>4</td><td>PCRST</td><td>GPIO端口C复位由软件置位或复位0:无作用1:复位GPIO端口C</td></tr><tr><td>3</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>2</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFRST</td><td>复用功能I/O复位由软件置位或复位0:无作用1:复位复用功能I/O</td></tr></table>

## 5.3.5. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>DAC1RS T</td><td>DAC0RS T</td><td>PMURST</td><td>BKPIRST</td><td>CAN1RS T</td><td>CAN0RS T</td><td>I2C2RST</td><td>USBDRS T</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4R ST</td><td>UART3R ST</td><td>USART2 RST</td><td>USART1 RST</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGT RST</td><td colspan="2">保留</td><td>TIMER13 RST</td><td>TIMER12 RST</td><td>TIMER11 RST</td><td>TIMER6R ST</td><td>TIMER5R ST</td><td>TIMER4R ST</td><td>TIMER3R ST</td><td>TIMER2R ST</td><td>TIMER1R ST</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td></td><td></td><td>0:无作用1:复位 DAC1</td></tr><tr><td>29</td><td>DAC0RST</td><td>DAC0 复位由软件置位或复位0:无作用1:复位 DAC0</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>BKPIRST</td><td>BKPI 复位由软件置位或复位0:无作用1:复位 BKP</td></tr><tr><td>26</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>25</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>24</td><td>I2C2RST</td><td>I2C2 复位由软件置位或复位0:无作用1:复位 I2C2</td></tr><tr><td>23</td><td>USBDRST</td><td>USBD 复位由软件置位或复位0:无作用1:复位 USBD</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位</td></tr></table>

由软件置位或复位
0: 无作用
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

15 SPI2RST SPI2 复位
由软件置位或复位
0: 无作用
1: 复位 SPI2

14 SPI1RST SPI1 复位
由软件置位或复位
0: 无作用
1: 复位 SPI1

13:12 保留 必须保持复位值。

11 WWDGTRST WWDGT 复位
由软件置位或复位
0: 无作用
1: 复位 WWDGT

10:9 保留 必须保持复位值。

8 TIMER13RST TIMER13 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER13

7 TIMER12RST TIMER12 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER12

<table><tr><td>6</td><td>TIMER11RST</td><td>TIMER11 复位由软件置位或复位0:无作用1:复位 TIMER11</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 5.3.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移：0x14

复位值：0x0000 0014

注意：Bit4不能被清为0。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPIEN</td><td>TMUEN</td><td colspan="14">保留</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>SDIOEN</td><td>保留</td><td>EXMCEN</td><td>保留</td><td>CRCEN</td><td>保留</td><td>SRAMSPEN</td><td>DMA1EN</td><td>DMA0EN</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPIEN</td><td>SQPI时钟使能由软件置位或复位0:关闭 SQPI时钟1:开启 SQPI时钟</td></tr><tr><td>30</td><td>TMUEN</td><td>TMU时钟使能由软件置位或复位0:关闭 TMU时钟1:开启 TMU时钟</td></tr><tr><td>29:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>SDIOEN</td><td>SDIO时钟使能由软件置位或复位0:关闭 SDIO时钟1:开启 SDIO时钟</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EXMCEN</td><td>EXMC时钟使能由软件置位或复位0:关闭 EXMC时钟1:开启 EXMC时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0:关闭 CRC时钟1:开启 CRC时钟</td></tr><tr><td>5:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPEN</td><td>在睡眠模式下 SRAM时钟使能由软件置位或复位0:在睡眠模式下关闭 SRAM时钟1:在睡眠模式下开启 SRAM时钟</td></tr><tr><td>1</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭 DMA1时钟1:开启 DMA1时钟</td></tr><tr><td>0</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位</td></tr></table>

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

0：关闭 DMA0 时钟

1：开启 DMA0 时钟

## 5.3.7. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x18

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMPEM</td><td>保留</td><td>SHRTIME REN</td><td>USART5 EN</td><td>保留</td><td>TIMER16 EN</td><td>TIMER15 EN</td><td>TIMER14 EN</td><td colspan="2">保留</td><td>TIMER10 EN</td><td>TIMER9E N</td><td>TIMER8E N</td><td colspan="3">保留</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2EN</td><td>USART0 EN</td><td>TIMER7E N</td><td>SPI0EN</td><td>TIMER0E N</td><td>ADC1EN</td><td>ADC0EN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td><td>AFEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMPEN</td><td>CMP时钟使能由软件置位或复位0:关闭CMP时钟1:开启CMP时钟</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>SHRTIMEREN</td><td>SHRTIMER时钟使能由软件置位或复位0:关闭HPTIEMR时钟1:开启SHRTIMER时钟</td></tr><tr><td>28</td><td>USART5EN</td><td>USART5时钟使能由软件置位或复位0:关闭USART5时钟1:开启USART5时钟</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TIMER16EN</td><td>TIMER16时钟使能由软件置位或复位0:关闭TIMER16时钟1:开启TIMER16时钟</td></tr><tr><td>25</td><td>TIMER15EN</td><td>TIMER15时钟使能由软件置位或复位0:关闭TIMER15时钟1:开启TIMER15时钟</td></tr></table>

<table><tr><td>24</td><td>TIMER14EN</td><td>TIMER14时钟使能由软件置位或复位0:关闭 TIMER14时钟1:开启 TIMER14时钟</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10EN</td><td>TIMER10时钟使能由软件置位或复位0:关闭 TIMER10时钟1:开启 TIMER10时钟</td></tr><tr><td>20</td><td>TIMER9EN</td><td>TIMER9时钟使能由软件置位或复位0:关闭 TIMER9时钟1:开启 TIMER9时钟</td></tr><tr><td>19</td><td>TIMER8EN</td><td>TIMER8时钟使能由软件置位或复位0:关闭 TIMER8时钟1:开启 TIMER8时钟</td></tr><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭 ADC2时钟1:开启 ADC2时钟</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭 USART0时钟1:开启 USART0时钟</td></tr><tr><td>13</td><td>TIMER7EN</td><td>TIMER7复位由软件置位或复位0:无作用1:复位 TIMER7</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>TIMER0EN</td><td>TIMER0复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr><tr><td>10</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>9</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>8</td><td>PGEN</td><td>GPIO端口G时钟使能由软件置位或复位0:关闭GPIO端口G时钟1:开启GPIO端口G时钟</td></tr><tr><td>7</td><td>PFEN</td><td>GPIO端口F时钟使能由软件置位或复位0:关闭GPIO端口F时钟1:开启GPIO端口F时钟</td></tr><tr><td>6</td><td>PEEN</td><td>GPIO端口E时钟使能由软件置位或复位0:关闭GPIO端口E时钟1:开启GPIO端口E时钟</td></tr><tr><td>5</td><td>PDEN</td><td>GPIO端口D时钟使能由软件置位或复位0:关闭GPIO端口D时钟1:开启GPIO端口D时钟</td></tr><tr><td>4</td><td>PCEN</td><td>GPIO端口C时钟使能由软件置位或复位0:关闭GPIO端口C时钟1:开启GPIO端口C时钟</td></tr><tr><td>3</td><td>PBEN</td><td>GPIO端口B时钟使能由软件置位或复位0:关闭GPIO端口B时钟1:开启GPIO端口B时钟</td></tr><tr><td>2</td><td>PAEN</td><td>GPIO端口A时钟使能由软件置位或复位0:关闭GPIO端口A时钟1:开启GPIO端口A时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFEN</td><td>复用功能IO时钟使能由软件置位或复位0:关闭复用功能IO时钟</td></tr></table>

## 1：开启复用功能 IO 时钟

## 5.3.8. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>DAC1EN</td><td>DAC0EN</td><td>PMUEN</td><td>BKPIEN</td><td>CAN1EN</td><td>CAN0EN</td><td>I2C2EN</td><td>USBDEN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td colspan="2">保留</td><td>TIMER13EN</td><td>TIMER12EN</td><td>TIMER11EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>DAC1EN</td><td>DAC1时钟使能由软件置位或复位0:关闭 DAC1 时钟1:开启 DAC1 时钟</td></tr><tr><td>29</td><td>DAC0EN</td><td>DAC0时钟使能由软件置位或复位0:关闭 DAC0 时钟1:开启 DAC0 时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭 PMU 时钟1:开启 PMU 时钟</td></tr><tr><td>27</td><td>BKPIEN</td><td>BKP时钟使能由软件置位或复位0:关闭 BKP 时钟1:开启 BKP 时钟</td></tr><tr><td>26</td><td>CAN1EN</td><td>CAN1时钟使能由软件置位或复位0:关闭 CAN1 时钟1:开启 CAN1 时钟</td></tr><tr><td>25</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>24</td><td>I2C2EN</td><td>I2C2时钟使能由软件置位或复位0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>23</td><td>USBDEN</td><td>USBD时钟使能由软件置位或复位0:关闭USBD时钟1:开启USBD时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13EN</td><td>TIMER13时钟使能由软件置位或复位0:关闭TIMER13时钟1:开启TIMER13时钟</td></tr><tr><td>7</td><td>TIMER12EN</td><td>TIMER12时钟使能由软件置位或复位0:关闭TIMER12时钟1:开启TIMER12时钟</td></tr><tr><td>6</td><td>TIMER11EN</td><td>TIMER11时钟使能由软件置位或复位0:关闭TIMER11时钟1:开启TIMER11时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6时钟使能由软件置位或复位0:关闭TIMER6时钟1:开启TIMER6时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5时钟使能由软件置位或复位0:关闭TIMER5时钟1:开启TIMER5时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4时钟使能由软件置位或复位0:关闭TIMER4时钟1:开启TIMER4时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3时钟使能由软件置位或复位0:关闭TIMER3时钟1:开启TIMER3时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2时钟使能</td></tr></table>

## 5.3.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，只能由备份域复位进行复位

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的 LXTALEN、LXTALBPS、RTCSRC 和 RTCEN位仅在备份域复位后才清 0。只有在电源控制寄存器 0（PMU_CTL0）中的 BKPWEN 位置 1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源</td></tr></table>

<table><tr><td></td><td></td><td>10:选择CK_IRC40K时钟作为RTC的时钟源11:选择CK_HXTAL/128时钟作为RTC的时钟源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值。00:弱驱动能01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能由软件置位或复位0:关闭LXTAL时钟1:使能LXTAL时钟</td></tr></table>

## 5.3.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C00 0000，所有复位标志位仅在电源复位时被清零，RSTFC/IRC40KEN 在系统复位时被清零。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>BORRSTF</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC40KSTB</td><td>IRC40KEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位</td></tr></table>

<table><tr><td></td><td></td><td>向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>BORRSTF</td><td>欠压复位复位标志位欠压复位复位发生时由硬件置1向RSTFC位写1来清除该位0:无欠压复位复位发生1:发生欠压复位复位</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用1:清除所有复位标志位</td></tr><tr><td>23:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC40KSTB</td><td>IRC40K时钟稳定标志位该位由硬件置1指示IRC40K输出时钟是否稳定待用</td></tr></table>

0：IRC40K 时钟未稳定

1：IRC40K 已稳定

0 IRC40KEN IRC40K 使能

由软件置位和复位

0：关闭 IRC40K 时钟

1：开启 IRC40K 时钟

## 5.3.11. AHB 复位寄存器（RCU_AHBRST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPIRST</td><td>TMURST</td><td colspan="14">保留</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPIRST</td><td>SQPI 复位由软件置位或复位0:无作用1:复位 SQPI</td></tr><tr><td>30</td><td>TMURST</td><td>TMU 复位由软件置位或复位0:无作用1:复位 TMU</td></tr><tr><td>29:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.12. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>PLLPRES EL</td><td>ADCPSC[ 3]</td><td colspan="9">保留</td><td>SHRTIME RSEL</td><td colspan="3">保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>PLLPRESEL</td><td>PLL时钟源预选择由软件置位或复位,控制PLL时钟源0:HXTAL被选择为PLL时钟的时钟源1:CK_IRC48M被选择为PLL时钟的时钟源</td></tr><tr><td>29</td><td>ADCPSC[3]</td><td>ADCPSC的第3位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>28:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>SHRTIMERSEL</td><td>SHRTIMER时钟源选择由软件置位或复位,控制SHRTIMER时钟源0:APB2时钟被选择为SHRTIMER时钟的时钟源1:系统时钟被选择为SHRTIMER时钟的时钟源</td></tr><tr><td>18:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.13. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为1.0V001:在深度睡眠模式下内核电压为0.9V010:在深度睡眠模式下内核电压为0.8V011:在深度睡眠模式下内核电压为0.7V1xx:保留</td></tr></table>

## 5.3.14. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0x8000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">保留</td><td>IRC48MS TB</td><td>IRC48ME N</td></tr><tr><td colspan="14">r</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>CK48MS EL</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB [7:0]</td><td>内部 48MHz RC 振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部 48MHz RC 振荡器时钟稳定标志位硬件置‘1’来指示 IRC48M 振荡器时钟是否稳定待用0: IRC48M 未稳定1: IRC48M 已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部 48MHz RC 振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位0: 关闭 IRC48M 时钟1: 打开 IRC48M 时钟</td></tr><tr><td>15:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CK48MSEL</td><td>48MHz 时钟源选择由软件置位和复位。该位用于选择 IRC48M 时钟或 PLL48M 时钟作为 CK48M 时钟源。CK48M 时钟用于:0: 不选择 IRC48M 时钟(使用 CK_PLL/USBDPSC 时钟)1: 选择 IRC48M 时钟</td></tr></table>

## 5.3.15. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>保留</td><td>IRC48MSTBIC</td><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>IRC48MSTBIE</td><td colspan="7">保留</td><td>IRC48MSTBIF</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部 48 MHz RC 振荡器稳定中断清零软件写 1 复位 IRC48MSTBIF 标志位0: 不复位 IRC48MSTBIF 标志位1: 复位 IRC48MSTBIF 标志位</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部 48 MHz RC 振荡器稳定中断使能由软件置位和复位来使能/禁止 IRC48M 时钟稳定中断0: 禁止 IRC48M 时钟稳定中断1: 使能 IRC48M 时钟稳定中断</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M 时钟稳定中断标志位当内部 48 MHz RC 振荡器时钟稳定且 IRC48MSTBIE 位被置 1 时由硬件置 1 软件置位 IRC48MSTBIC 位时清除该位0: 无 IRC48M 时钟稳定中断产生1: 产生 IRC48M 时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 5.3.16. PLL 时钟扩频控制寄存器（RCU_PLLSSCTL）

地址偏移：0xD0

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

扩频调制仅适用于主 PLL 时钟

仅当 PLL 被禁止时，RCU_PLLSSCTL 寄存器才可写入

该寄存器用于配置 PLL 扩频时钟生成，需按照如下公式：

$$
\text { MODCNT } = \text { round } (f _ {\text { PLLIN }} / 4 / f _ {\text { mod }})
$$

MODSTEP = round（mdamp*PLLN*2<sup>15</sup>/（MODCNT*100）） 

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">I2C2SEL[1:0]</td><td colspan="2">保留</td><td colspan="2">USART5SEL[1:0]</td></tr></table>

f<sub>PLLIN</sub>表示 PLL 输入时钟频率，f<sub>mod</sub>表示扩频调制频率，mdamp 表示扩频调制振幅（按百分比表示），PLLN 表示 PLL 时钟频率倍频因子

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SSCGON</td><td>SS_TYPE</td><td colspan="2">保留</td><td colspan="12">MODSTEP[14:3]</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">MODSTEP[2:0]</td><td colspan="13">MODCNT[12:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SSCGON</td><td>PLL 扩频调制使能0:禁止扩频调制1:使能扩频调制</td></tr><tr><td>30</td><td>SS_TYPE</td><td>PLL 扩频调制类型选择0:选择中心扩频1:选择向下扩频</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:13</td><td>MODSTEP</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件:MODSTEP*MODCNT≤<eq>2^{15}</eq>-1</td></tr><tr><td>12:0</td><td>MODCNT</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件:MODSTEP*MODCNT≤<eq>2^{15}</eq>-1</td></tr></table>

## 5.3.17. 配置寄存器 2（RCU_CFG2）

地址偏移：0xD4

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>I2C2SEL[1:0]</td><td>I2C2时钟源选择由软件置1或清0。00:I2C2时钟源选择APB1时钟01:I2C2时钟源选择系统时钟1x: I2C2时钟源选择IRC8M</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>USART5SEL[1:0]</td><td>USART5时钟源选择由软件置1或清0。00: USART5时钟选择APB2时钟01: USART5时钟选择系统时钟10: USART5时钟选择LXTAL时钟11: USART5时钟选择IRC8M时钟</td></tr></table>

## 5.3.18. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTC RST</td><td colspan="11">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.19. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td>rw</td><td colspan="11"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC时钟使能由软件置位或复位0:关闭CTC时钟1:开启CTC时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 互联型产品的复位和时钟控制单元（RCU）

## 5.4. 复位控制单元（RCTL）

## 5.4.1. 简介

GD32E51x 复位控制包括三种控制方式：电源复位、系统复位和备份域复位。电源复位又称为冷复位，其复位除了备份域的所有系统。系统复位将复位除了 SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设 IP。备份域复位将复位备份区域。复位能够被外部信号、内部事件和复位发生器触发。后续章节将介绍关于这些复位的详细信息

## 5.4.2. 功能描述

## 电源复位

当发生以下任一事件时，产生电源复位：上电/掉电复位（POR/PDR 复位），从待机模式中返回后由内部复位发生器产生。电源复位复位所有的寄存器除了备份域。电源复位为低电平有效，当内部 LDO 电源基准准备好提供 1.1V 电压时，电源复位电平将变为无效。复位入口向量被固定在存储器映射的地址 0x0000_0004。

## 系统复位

当发生以下任一事件时，产生一个系统复位：

 上电复位（POWER_RSTn）

 外部引脚复位（NRST）

 窗口看门狗计数终止（WWDGT_RSTn）

 独立看门狗计数终止（FWDGT_RSTn）

 Cortex<sup>®</sup>-M33的中断应用和复位控制寄存器中的SYSRESETREQ位置‘1’（SW_RSTn）

■ 用 户 选 择 字 节 寄 存 器nRST_STDBY设置为0， 并 且 进 入 待 机 模 式 时 将 产 生 复 位（OB_STDBY_RSTn）

■ 用 户 选 择 字 节 寄 存 器 nRST_DPSLP 设 置 为 0 ， 并 且 进 入 深 度 睡 眠 模 式 时（OB_DPSLP_RSTn）

系统复位将复位除了 SW-DP控制器和备份域之外的其余部分，包括处理器内核和外设 IP。

系统复位脉冲发生器保证每一个复位源（外部或内部）都能有至少 20μs 的低电平脉冲延时。


图 5-5. 系统复位电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/a578d5158682c93f0923e276e0d241bd3622624f0b4318a340091969d804a238.jpg)


## 备份域复位

以下事件之一发生时，产生备份域复位：1、设置备份域控制寄存器中的 BKPRST 位为‘1’；2、备份域电源上电复位（在 VDD 和 VBAT 两者都掉电的前提下，VDD 或 VBAT 上电）。

## 5.5. 时钟控制单元（CCTL）

## 5.5.1. 简介

时钟控制单元提供了一系列频率的时钟功能，包括一个内部 8M RC 振荡器时钟（IRC8M）、一个内部 48M RC 振荡器时钟（IRC48M）、一个外部高速晶体振荡器时钟（HXTAL）、一个内部 40K RC 振荡器时钟（IRC40K）、一个外部低速晶体振荡器时钟（LXTAL）、四个锁相环（PLL）、一个 HXTAL 时钟监视器、时钟预分频器、时钟多路复用器和时钟门控电路。

AHB、APB 和 Cortex®-M33 时钟都源自系统时钟（CK_SYS），系统时钟的时钟源可以选择IRC8M、HXTAL 或 PLL。系统时钟的最大运行时钟频率可以达到 180MHz。


图 5-6. 时钟树


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/4837516dd22dad57b0d0d4a88e8fe1c6e812c6f777760d96e09c01d57167f746.jpg)


预分频器可以配置 AHB、APB2 和 APB1 域的时钟频率。AHB、APB2、APB1 域的最高时钟频率分别为 180MHz、180MHz、90MHz。RCU 通过 AHB 时钟（HCLK）8 分频后作为 Cortex<sup>®</sup>系统定时器（SysTick）的外部时钟。通过对 SysTick 控制和状态寄存器的设置，可选择上述时钟或 AHB（HCLK）时钟作为 SysTick 时钟。

ADC 时钟由 APB2 时钟经 2、4、6、8、12、16 分频或由 AHB 时钟经 5、6、10、20 分频获得，它们是通过设置 RCU_CFG0 和 RCU_CFG1 寄存器的 ADCPSC 位来选择。USART5 时钟由 IRC8M 或 LXTAL 或 CK_SYS 或 APB2 时钟提供，通过配置 RCU_CFG2 寄存器的USART5SEL 位来选择。I2C2 的时钟由 IRC8M 或 CK_SYS 或 APB1 时钟提供，通过配置RCU_CFG2 寄存器的 I2C2SEL 位来选择。

SDIO, EXMC 的时钟由 CK_AHB 提供。

TIMER 时钟由 CK_APB1 和 CK_APB2 时钟分频获得，如果 APBx（x=0,1）的分频系数不为1，则 TIMER 时钟为 CK_APBx（x = 0,1）的两倍。

PLLUSB 时 钟 由 HXTAL 或 IRC48M 提 供 。 通 过 配 置 RCC_ADDCFG 寄 存 器 的PLLUSBPRESEL 来选择。PLLUSB 时钟工作的最大频率为 480Mhz

USBHS 的时钟由外部 PHY 时钟或内部时钟提供。通过配置 USBHS_GUSBCS 寄存器的EMBHY 位来选择。

CTC 时钟由 IRC48M 时钟提供，通过 CTC 单元，可以实现 IRC48M 时钟精度的自动调整。

I2S 的时钟由 CK_SYS 或 PLL2*2 提供，通过配置 RCU_CFG1 寄存器的 I2SxSEL 来选择。

通过配置 AFIO_PCF0 寄存器的 ENET_PHY_SEL 位，以太网 TX/RX 时钟可以选择由外部引脚（ENET_TX_CLK/ENET_RX_CLK）输入时钟提供。

通过配置 RCU_BDCTL 寄存器的 RTCSRC 位，RTC 时钟可以选择由 LXTAL 时钟、IRC40K时钟或 HXTAL 时钟的 128 分频提供。RTC 时钟选择 HXTAL 时钟的 128 分频做为时钟源后，当 1.1V 内核电压域掉电时，时钟将停止。RTC 时钟选择 IRC40K 时钟做为时钟源后，当 V掉电时，时钟将停止。RTC 时钟选择 LXTAL 时钟做为时钟源后，当 V 和 V 都掉电时，时钟将停止。

当 FWDGT 启动时，FWDGT 时钟被强制选择由 IRC40K 时钟做为时钟源。

当 FMC 启动时，FMC 时钟被强制选择由 IRC8M 时钟作为时钟源。

SHRTIMER时钟由CK_APB2或CK_SYS提供。通过配置RCU_CFG1寄存器的SHRTIMERSEL位来选择。

如 果 用 户 不 需 要 使 用SHRTIMER高 分 辨 率 模 式 ， 可 以 保 持RCU_CFG1寄 存 器 中 的SHRTIMERSEL位清零，在这种情况下，SHRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值必须大于或等于5（预分频比大于或等于64）。

如果用户需要使用SHRTIMER高分辨率模式，必须在系统时钟源选择为PLL时，通过配置RCU_CFG1 寄 存 器 中 的 SHRTIMERSEL 位 为 1 ， 选 择 CK_SYS 为 时 钟 源 ， 此 时SHRTIMER_MTCTL0寄存器中的CNTCKDIV[2:0]值可以配置为任何可选值。

注意：在高分辨率配置中，必须配置 AHB 和 APB2 预分频器（RCU_CFG0 寄存器中的AHBPSC[3:0]和 APB2PSC[2:0]位），将系统时钟 CK_SYS 与 APB2 时钟 PCLK2 之间的比率为 1，2 或 4。

## 5.5.2. 主要特性

 4到32MHz外部高速晶体振荡器（HXTAL）；

 内部8MHz RC振荡器（IRC8M）；

 内部48MHz RC振荡器；

 32768 Hz外部低速晶体振荡器（LXTAL）；

 内部40KHz RC振荡器（IRC40K）；

 PLL时钟源可选HXTAL、IRC8M或IRC48M；

 HXTAL时钟监视器。

## 5.5.3. 功能描述

外部高速晶体振荡时钟（HXTAL）

4 到 32M 的外部高速晶体振荡器可为系统时钟提供更为精确时钟源。带有特定频率的晶体必须靠近两个 HXTAL 的引脚连接。和晶体连接的外部电阻和电容必须根据所选择的振荡器来调整。


图 5-7. HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/b436faa2c997e4be5fcb1a3e57a8ebb3b1188b9a5479a4e8e8366e47a7e6f984.jpg)


HXTAL 晶体振荡器可以通过设置控制寄存器 RCU_CTL 的 HXTALEN 位来启动或关闭，在控制寄存器 RCU_CTL 中的 HXTALSTB位用来指示外部高速振荡器是否已稳定。在启动时，直到这一位被硬件置‘1’，时钟才被释放出来。这个特定的延迟时间被称为振荡器的启动时间。当 HXTAL 时钟稳定后，如果在中断寄存器 RCU_INT 中的相应中断使能位 HXTALSTBIE 位被置‘1’，将会产生相应中断。此时，HXTAL 时钟可以被直接用作系统时钟源或者 PLL 输入时钟。

将控制寄存器RCU_CTL的HXTALBPS和HXTALEN位置‘1’可以设置外部时钟旁路模式。旁路输入时，信号接至 OSCIN，OSCOUT 保持悬空状态，如 5-8. HXTAL所示。此时，CK_HXTAL 等于驱动 OSCIN 管脚的外部时钟。


图 5-8. 旁路模式下 HXTAL 时钟源


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/413c0cce3cd1f9a87202c82585034bc3f58b812b236d4bfaad68cd3308abbb1a.jpg)


## 内部 8M RC 振荡器时钟（IRC8M）

内部 8MHz RC 振荡器时钟，简称 IRC8M 时钟，拥有 8MHz的固定频率，设备上电后 CPU 默认选择其做为系统时钟源。IRC8M RC 振荡器能够在不需要任何外部器件的条件下为用户提供更低成本类型的时钟源。IRC8M RC 振荡器可以通过设置控制寄存器（RCU_CTL）中的IRC8MEN 位被启动和关闭。控制寄存器 RCU_CTL 中的 IRC8MSTB 位用来指示 IRC8M 内部RC 振荡器是否稳定。IRC8M 振荡器的启动时间比 HXTAL 晶体振荡器要更短。如果中断寄存器 RCU_INT 中的相应中断使能位 IRC8MSTBIE 被置‘1’，在 IRC8M 稳定以后，将产生一个中断。IRC8M 时钟也可用作系统时钟源或 PLL 输入时钟。

工厂会校准 IRC8M 时钟频率的精度，但是它的精度仍然比 HXTAL 时钟要差。用户可以根据需求、环境条件和成本决定选择哪个时钟作为系统时钟源。

如果 HXTAL 或者 PLL 被选择为系统时钟源，为了最大程度减小系统从深度睡眠模式恢复的时间，当系统从深度睡眠模式初始唤醒时，硬件会强制 IRC8M 时钟作为系统时钟。

## 内部 48M RC 振荡器时钟（IRC48M）

内部 48MHz RC 振荡器时钟，简称 IRC48M 时钟，拥有 48MHz 的固定频率，当使用PLLUSB/USBHS 模块时，IRC48M 振荡器在不需要任何外部器件的条件下为用户提供了一种成本更低的时钟源选择。IRC48M RC 振荡器可以通过设置 RCU_ADDCTL 寄存器中的IRC48MEN位被启动和关闭。RCU_ADDCTL寄存器中的IRC48MSTB位用来指示内部48MHzRC 振荡器是否稳定。如果 RCU_ADDINT 寄存器中的相应中断使能位 IRC48MSTBIE 被置‘1’，在 IRC48M 稳定以后，将产生一个中断。IRC48M 时钟可做为 PLLUSB/USBHS 的系统时钟。

工厂会校准 IRC48M 时钟频率的精度，但是它的精度仍然不够精准。因为 USB 模块需要的时钟频率必须满足 48MHz（500ppm）。CTC 单元提供了一种硬件自动执行动态调整的功能将IRC48M 时钟调整到需要的频率。

## 锁相环（PLL）

CL 系列的芯片，内部有四个锁相环，PLL，PLL1，PLL2 和 PLLUSB。

PLL 可以通过设置 RCU_CTL 寄存器中的 PLLEN 位被启动和关闭。RCU_CTL 寄存器中的PLLSTB位用来指示PLL时钟是否稳定。如果RCU_INT寄存器中的相应中断使能位PLLSTBIE被置‘1’，在 PLL 稳定以后，将产生一个中断。

PLL1 可以通过设置 RCU_CTL 寄存器中的 PLL1EN 位被启动和关闭。RCU_CTL 寄存器中的PLL1STB 位用来指示 PLL1 时钟是否稳定。如果 RCU_INT 寄存器中的相应中断使能位PLL1STBIE 被置‘1’，在 PLL1 稳定以后，将产生一个中断。

PLL2 可以通过设置 RCU_CTL 寄存器中的 PLL2EN 位被启动和关闭。RCU_CTL 寄存器中的PLL2STB 位用来指示 PLL2 时钟是否稳定。如果 RCU_INT 寄存器中的相应中断使能位PLL2STBIE 被置‘1’，在 PLL2 稳定以后，将产生一个中断。

PLLUSB 可 以 通 过 设 置 RCU_ADDCTL 寄 存 器 中 的 PLLUSBEN 位 被 启 动 和 关 闭。RCU_ADDCTL 寄 存 器 中 的 PLLUSBSTB 位 来 指 示 PLLUSB 时 钟 是 否 稳 定 。 如 果RCU_ADDINT寄存器中的相应中断使能位PLLUSBSTBIE被置‘1’，在PLLUSB稳定以后，将产生一个中断。

当进入 Deepsleep/Standby 模式或者 HXTAL 监视器检测到时钟阻塞时（HXTAL 做为锁相环的输入时钟），四个 PLL 将被关闭。

## 外部低速晶体振荡器时钟（LXTAL）

LXTAL 是一个频率为 32.768kHz 的外部低速晶体或陶瓷谐振器。它为实时时钟电路提供一个低功耗且高精准的时钟源。LXTAL 振荡器可以通过设置备份域控制寄存器（RCU_BDCTL）中的 LXTALEN 位被启动和关闭。备份域控制寄存器 RCU_BDCTL 中的 LXTALSTB 位用来指示LXTAL 时钟是否稳定。如果中断寄存器 RCU_INT 中的相应中断使能位 LXTALSTBIE 被置‘1’，在 LXTAL 稳定以后，将产生一个中断。

将备份域控制寄存器 RCU_BDCTL 的 LXTALBPS 和 LXTALEN 位置‘1’可以选择外部时钟旁路模式。CK_LXTAL 与连到 OSC32IN 脚上外部时钟信号一致。

## 内部 40K RC 振荡器时钟（IRC40K）

IRC40K 内部 RC 振荡器时钟担当一个低功耗时钟源的角色，不需要外部器件，它的时钟频率大约 40kHz，为独立看门狗和实时时钟电路提供时钟。IRC40K RC 振荡器可以通过设置复位源/时钟寄存器 RCU_RSTSCK 中的 IRC40KEN 位被启动和关闭。复位源/时钟寄存器RCU_RSTSCK 中的 IRC40KSTB 位用来指示 IRC40K 时钟是否已稳定。如果复位源/时钟寄存器 RCU_RSTSCK 中的相应中断使能位 IRC40KSTBIE 被置‘1’，在 IRC40K 稳定以后，将产生一个中断。

TIMER4_CH3 可以捕获 IRC40K 的时钟，进而对 RTC 和 FWDGT 的计数器进行校准，详细的信息可以参考 AFIO_PCF0 寄存器的位 TIMER4CH3_IREMAP。

## 系统时钟（CK_SYS）选择

系统复位后，IRC8M 时钟默认做为 CK_SYS 的时钟源，改变配置寄存器 0（RCU_CFG0）中的系统时钟变换位 SCS可以切换系统时钟源为 HXTAL 或 CK_PLL。当 SCS 的值被改变，系统时钟将使用原来的时钟源继续运行直到转换的目标时钟源稳定。当一个时钟源被直接或通过PLL间接作为系统时钟时，它将不能被停止。

## HXTAL 时钟监视器（CKM）

设置控制寄存器 RCU_CTL 中的 HXTAL 时钟监视使能位 CKMEN，HXTAL 可以使能时钟监视功能。该功能必须在 HXTAL 启动延迟完毕后使能，在 HXTAL 停止后禁止。一旦监测到HXTAL 故障，HXTAL 将自动被禁止，中断寄存器 RCU_INT 中的 HXTAL 时钟阻塞中断标志位 CKMIF 将被置‘1’，产生 HXTAL 故障事件。这个故障引发的中断和 Cortex®-M33 的不可屏蔽中断 NMI 相连。如果 HXTAL 被选作系统，PLL 或是 RTC 的时钟源，HXTAL 故障将促使选择 IRC8M 为系统时钟源，PLL 将被自动禁止，RTC 的时钟源需要重新配置。

## 时钟输出功能

时钟输出功能输出从 0.09375MHz 到 180MHz 的时钟。通过设置时钟配置寄存器 0（RCU_CFG0）中的 CK_OUT0 时钟源选择位域 CKOUT0SEL 能够选择不同的时钟信号。相应的 GPIO 引脚应该被配置成备用功能 I/O（AFIO）模式来输出选择的时钟信号。


表 5-3. 时钟输出 0 的时钟源选择


<table><tr><td>时钟输出 0 的时钟源选择位域</td><td>时钟源</td></tr><tr><td>00xx</td><td>NO CLK</td></tr><tr><td>0100</td><td>CK_SYS</td></tr><tr><td>0101</td><td>CK_IRC8M</td></tr><tr><td>0110</td><td>CK_HXTAL</td></tr><tr><td>0111</td><td>CK_PLL/2</td></tr><tr><td>1000</td><td>CK_PLL1</td></tr><tr><td>1001</td><td>CK_PLL2/2</td></tr><tr><td>1010</td><td>EXT1</td></tr><tr><td>1011</td><td>CK_PLL2</td></tr><tr><td>1100</td><td>CK_IRC48M</td></tr><tr><td>1101</td><td>CK_IRC48M/8</td></tr><tr><td>1110</td><td>CK_PLLUSB/32</td></tr></table>

## 电压控制

深度睡眠模式电压寄存器（RCU_DSV）中的 DSLPVS[2:0]位域可以控制 1.1V 域在深度睡眠模式下的电压。


表 5-4. 深度睡眠模式下 1.1V域电压选择


<table><tr><td>DSLPVS[2:0]</td><td>深度睡眠模式电压(V)</td></tr><tr><td>000</td><td>1.0</td></tr><tr><td>001</td><td>0.9</td></tr><tr><td>010</td><td>0.8</td></tr><tr><td>011</td><td>0.7</td></tr></table>

## 5.6. RCU 寄存器

RCU 基地址：0x4002 1000

## 5.6.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83 x 表示未定义

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>PLL2STB</td><td>PLL2EN</td><td>PLL1STB</td><td>PLL1EN</td><td>PLLSTB</td><td>PLL EN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALB PS</td><td>HXTALST B</td><td>HXTALE N</td></tr><tr><td colspan="2"></td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MST B</td><td>IRC8MEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>PLL2STB</td><td>PLL2时钟稳定标志位硬件置1来表示PLL2输出时钟是否稳定待用0:PLL2未稳定1:PLL2已稳定</td></tr><tr><td>28</td><td>PLL2EN</td><td>PLL2使能软件置位或复位,当PLL2时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL2被关闭1:PLL2被打开</td></tr><tr><td>27</td><td>PLL1STB</td><td>PLL1时钟稳定标志位硬件置1来表示PLL1输出时钟是否稳定待用0:PLL1未稳定1:PLL1已稳定</td></tr><tr><td>26</td><td>PLL1EN</td><td>PLL1使能软件置位或复位,当PLL1时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL1被关闭1:PLL1被打开</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~32MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~32MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位0:高速4~32MHz晶体振荡器被关闭1:高速4~32MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部8MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部8MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整IRC8M到8MHz±1%</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M内部8MHz RC振荡器稳定标志位硬件置‘1’来指示IRC8M振荡器时钟是否稳定待用0:IRC8M振荡器未稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部 8MHz RC 振荡器使能软件置位或复位,如果 IRC8M 时钟做为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当 CKMEN 置位同时用作系统时钟的 HXTAL 振荡器发生故障时,该位由硬件置 1 来启动 IRC8M 振荡器。0: 内部 8MHz RC 振荡器被关闭1: 内部 8MHz RC 振荡器被打开</td></tr></table>

## 5.6.2. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>USBHSPSC[2]</td><td colspan="2">PLLMF[5:4]</td><td>ADCPSC[2]</td><td colspan="4">CKOUT0SEL[3:0]</td><td colspan="2">USBHSPSC[1:0]</td><td colspan="4">PLLMF[3:0]</td><td>PREDV0_LSB</td><td>PLLSEL</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]</td><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>USBHSPSC[2]</td><td>USBHSPSC的第2位参考寄存器RCU_CFG0的22到23位</td></tr><tr><td>30:29</td><td>PLLMF[5:4]</td><td>PLLMF的第5位和第4位参考寄存器RCU_CFG0的18到21位</td></tr><tr><td>28</td><td>ADCPSC[2]</td><td>ADCPSC的第2位参考寄存器RCU_CFG0的14到15位</td></tr><tr><td>27:24</td><td>CKOUT0SEL[3:0]</td><td>CKOUT0时钟源选择由软件置位或清零00xx:无时钟输出0100:选择系统时钟CK_SYS0101:选择内部8M RC振荡器时钟0110:选择高速晶体振荡器时钟(HXTAL)0111:选择(CK_PLL/2)时钟1000:选择CK_PLL1时钟1001:选择(CK_PLL2/2)时钟1010:选择提供给ENET的EXT1时钟1011:选择CK_PLL2时钟1100:选择CK_IRC48M时钟1101:选择(CK_IRC48M/8)时钟1110: 选择(CK_PLLUSB/32)时钟</td></tr><tr><td>23:22</td><td>USBHSPSC[1:0]</td><td>USBHS的时钟分频系数由软件置位或清零。USBHS的时钟必须为48MHz,当USBHS时钟使能的时候,这些位无法修改000: CK_USBHS= CK_PLL / 1.5001: CK_USBHS= CK_PLL010: CK_USBHS= CK_PLL / 2.5011: CK_USBHS= CK_PLL / 2100: CK_USBHS= CK_PLL / 3101: CK_USBHS= CK_PLL / 3.511x: CK_USBHS= CK_PLL / 4</td></tr><tr><td>21:18</td><td>PLLMF[3:0]</td><td>PLL时钟倍频因子与寄存器RCU_CFG0的29,30位共同构成倍频因子,由软件置位或清零注意:PLL输出时钟频率不能超过180MHz000000:(PLL源时钟 x 2)000001:(PLL源时钟 x 3)000010:(PLL源时钟 x 4)000011:(PLL源时钟 x 5)000100:(PLL源时钟 x 6)000101:(PLL源时钟 x 7)000110:(PLL源时钟 x 8)000111:(PLL源时钟 x 9)001000:(PLL源时钟 x 10)001001:(PLL源时钟 x 11)001010:(PLL源时钟 x 12)001011:(PLL源时钟 x 13)001100:(PLL源时钟 x 14)001101:(PLL源时钟 x 6.5)001110:(PLL源时钟 x 16)001111:(PLL源时钟 x 16)010000:(PLL源时钟 x 17)010001:(PLL源时钟 x 18)010010:(PLL源时钟 x 19)010011:(PLL源时钟 x 20)010100:(PLL源时钟 x 21)010101:(PLL源时钟 x 22)010110:(PLL源时钟 x 23)010111:(PLL源时钟 x 24)011000:(PLL源时钟 x 25)011001:(PLL源时钟 x 26)011010:(PLL源时钟 x 27)011011:(PLL源时钟 x 28)011100:(PLL源时钟 x 29)011101: (PLL源时钟 x30)011110: (PLL源时钟 x31)011111: (PLL源时钟 x32)100000: (PLL源时钟 x33)100001: (PLL源时钟 x34)...111110: (PLL源时钟 x63)111111: (PLL源时钟 x64)</td></tr><tr><td>17</td><td>PREDV0_LSB</td><td>PREDV0分频因子的最低位与寄存器RCU_CFG1位PREDV0第0位相同,通过寄存器RCU_CFG1来改变PREDV0的值,此位也会一同改。当PREDV0的第1到3位未修改时,此位决定PREDV0的输入时钟是否二分频。</td></tr><tr><td>16</td><td>PLLSEL</td><td>PLL时钟源选择由软件置位或复位,控制PLL时钟源0:(IRC8M/2)被选择为PLL时钟的时钟源1:HXTAL时钟或者IRC48M时钟(寄存器RCU_CFG1位PLLPRESEL决定)被选择为PLL时钟的时钟源</td></tr><tr><td>15:14</td><td>ADCPSC[1:0]</td><td>ADC的时钟分频系数与寄存器RCU_CFG0的28位,寄存器RCU_CFG1的29位共同构成分频因子,由软件置位或清零0000: CK_ADC = CK_APB2 / 20001: CK_ADC = CK_APB2 / 40010: CK_ADC = CK_APB2 / 60011: CK_ADC = CK_APB2 / 80100: CK_ADC = CK_APB2 / 20101: CK_ADC = CK_APB2 / 120110: CK_ADC = CK_APB2 / 80111: CK_ADC = CK_APB2 / 161x00: CK_ADC = CK_AHB / 51x01: CK_ADC = CK_AHB / 61x10: CK_ADC = CK_AHB / 101x11: CK_ADC = CK_AHB / 20</td></tr><tr><td>13:11</td><td>APB2PSC[2:0]</td><td>APB2预分频选择由软件置位或清零,控制APB2时钟分频因子0xx: CK_APB2 = CK_AHB100: CK_APB2 = CK_AHB / 2101: CK_APB2 = CK_AHB / 4110: CK_APB2 = CK_AHB / 8111: CK_APB2 = CK_AHB / 16</td></tr><tr><td>10:8</td><td>APB1PSC[2:0]</td><td>APB1预分频选择由软件置位或清零,控制APB1时钟分频因子.0xx: CK_APB1 = CK_AHB</td></tr></table>

由软件配置选择系统时钟源。由于 CK_SYS 的改变存在固有的延迟，因此软件应当读 SCSS 位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时，以及当 HXTAL 直接或间接作为系统时钟同时 HXTAL 时钟监视器检测到 HXTAL 故障时，强制选择 IRC8M作为系统时钟。

10：选择 CK_PLL 时钟作为 CK_SYS 时钟源

## 5.6.3. 时钟中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td>PLL2STBIC</td><td>PLL1STBIC</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC40KSTBIC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>PLL2</td><td>PLL1</td><td>PLL</td><td>HXTAL</td><td>IRC8M</td><td>LXTAL</td><td>IRC40K</td><td>CKMIF</td><td>PLL2</td><td>PLL1</td><td>PLL</td><td>HXTAL</td><td>IRC8M</td><td>LXTAL</td><td>IRC40K</td></tr></table>

<table><tr><td></td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td>STBIE</td><td></td><td>STBIF</td><td>STBIF</td><td>STBIF</td><td>STBIF</td><td>STBIF</td><td>STBIF</td><td>STBIF</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位.0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>PLL2STBIC</td><td>PLL2时钟稳定中断清零软件写1复位PLL2STBIF标志位0:不复位PLL2STBIF标志位1:复位PLL2STBIF标志位</td></tr><tr><td>21</td><td>PLL1STBIC</td><td>PLL1时钟稳定中断清零软件写1复位PLL1STBIF标志位0:不复位PLL1STBIF标志位1:复位PLL1STBIF标志位</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL时钟稳定中断清零软件写1复位PLLSTBIF标志位0:不复位PLLSTBIF标志位1:复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M时钟稳定中断清零软件写1复位IRC8MSTBIF标志位0:不复位IRC8MSTBIF标志位1:复位IRC8MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0:不复位LXTALSTBIF标志位1:复位LXTALSTBIF标志位</td></tr><tr><td>16</td><td>IRC40KSTBIC</td><td>IRC40K时钟稳定中断清零软件写1复位IRC40KSTBIF标志位0:不复位IRC40KSTBIF标志位1:复位IRC40KSTBIF标志位</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>PLL2STBIE</td><td>PLL2时钟稳定中断使能</td></tr></table>

<table><tr><td></td><td></td><td>软件置位和复位来使能/禁止PLL2时钟稳定中断0:禁止PLL2时钟稳定中断1:使能PLL2时钟稳定中断</td></tr><tr><td>13</td><td>PLL1STBIE</td><td>PLL1时钟稳定中断使能软件置位和复位来使能/禁止PLL1时钟稳定中断0:禁止PLL1时钟稳定中断1:使能PLL1时钟稳定中断</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置位和复位来使能/禁止PLL时钟稳定中断0:禁止PLL时钟稳定中断1:使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M时钟稳定中断使能软件置位和复位来使能/禁止IRC8M时钟稳定中断0:禁止IRC8M时钟稳定中断1:使能IRC8M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC40KSTBIE</td><td>IRC40K时钟稳定中断使能软件置位和复位来使能/禁止IRC40K时钟稳定中断0:禁止IRC40K时钟稳定中断1:使能IRC40K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位.软件置位CKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6</td><td>PLL2STBIF</td><td>PLL2时钟稳定中断标志位当PLL时钟稳定且PLL2STBIE位被置1时由硬件置1软件置位PLL2STBIC位时清除该位0:无PLL2时钟稳定中断产生1:产生PLL2时钟稳定中断</td></tr><tr><td>5</td><td>PLL1STBIF</td><td>PLL1时钟稳定中断标志位当PLL时钟稳定且PLL1STBIE位被置1时由硬件置1软件置位PLL1STBIC位时清除该位</td></tr></table>

<table><tr><td></td><td></td><td>0:无PLL1时钟稳定中断产生1:产生PLL1时钟稳定中断</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1软件置位PLLSTBIC位时清除该位0:无PLL时钟稳定中断产生1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~32MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC40KSTBIF</td><td>IRC40K时钟稳定中断标志位当内部40kHz RC振荡器时钟稳定且IRC40KSTBIE位被置1时由硬件置1软件置位IRC40KSTBIC位时清除该位0:无IRC40K时钟稳定中断产生1:产生IRC40K时钟稳定中断</td></tr></table>

## 5.6.4. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMPRST</td><td>保留</td><td>SHRTIME RRST</td><td>USART5 RST</td><td>保留</td><td>TIMER16 RST</td><td>TIMER15 RST</td><td>TIMER14 RST</td><td colspan="2">保留</td><td>TIMER10 RST</td><td>TIMER9 RST</td><td>TIMER8 RST</td><td colspan="3">保留</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2RS T</td><td>USART0 RST</td><td>TIMER7R ST</td><td>SPI0RST</td><td>TIMER0R ST</td><td>ADC1RS T</td><td>ADC0RS T</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td><td>AFRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMPRST</td><td>CMP 复位由软件置位或复位0:无作用1:复位 CMP</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>SHRTIMEREN</td><td>SHRTIMER 复位由软件置位或复位0:无作用1:复位 SHRTIMER</td></tr><tr><td>28</td><td>USART5EN</td><td>USART5 复位由软件置位或复位0:无作用1:复位 USART5</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TIMER16RST</td><td>TIMER16 复位由软件置位或复位0:无作用1:复位 TIMER16</td></tr><tr><td>25</td><td>TIMER15RST</td><td>TIMER15 复位由软件置位或复位0:无作用1:复位 TIMER15</td></tr><tr><td>24</td><td>TIMER14RST</td><td>TIMER14 复位由软件置位或复位0:无作用1:复位 TIMER14</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10RST</td><td>TIMER10 复位由软件置位或复位0:无作用1:复位 TIMER10</td></tr><tr><td>20</td><td>TIMER9RST</td><td>TIMER9 复位由软件置位或复位0:无作用1:复位 TIMER9</td></tr><tr><td>19</td><td>TIMER8RST</td><td>TIMER8 复位由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:无作用1:复位 TIMER8</td></tr><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2RST</td><td>ADC2 复位由软件置位或复位0:无作用1:复位 ADC2</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0:无作用1:复位 USART0</td></tr><tr><td>13</td><td>TIMER7RST</td><td>TIMER7 复位由软件置位或复位0:无作用1:复位 TIMER7</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>TIMER0RST</td><td>TIMER0 复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr><tr><td>10</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0:无作用1:复位 ADC1</td></tr><tr><td>9</td><td>ADC0RST</td><td>ADC0 复位由软件置位或复位0:无作用1:复位 ADC0</td></tr><tr><td>8</td><td>PGRST</td><td>GPIO 端口 G 复位由软件置位或复位0:无作用1:复位 GPIO 端口 G</td></tr><tr><td>7</td><td>PFRST</td><td>GPIO 端口 F 复位由软件置位或复位0:无作用1:复位 GPIO 端口 F</td></tr><tr><td>6</td><td>PERST</td><td>GPIO端口E复位由软件置位或复位0:无作用1:复位GPIO端口E</td></tr><tr><td>5</td><td>PDRST</td><td>GPIO端口D复位由软件置位或复位0:无作用1:复位GPIO端口D</td></tr><tr><td>4</td><td>PCRST</td><td>GPIO端口C复位由软件置位或复位0:无作用1:复位GPIO端口C</td></tr><tr><td>3</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>2</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFRST</td><td>复用功能I/O复位由软件置位或复位0:无作用1:复位复用功能I/O</td></tr></table>

## 5.6.5. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>DAC1RST</td><td>DAC0RST</td><td>PMURST</td><td>BKPIRST</td><td>CAN1RST</td><td>CAN0RST</td><td>I2C2RST</td><td>保留</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>USART2RST</td><td>USART1RST</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGTRST</td><td colspan="2">保留</td><td>TIMER13RST</td><td>TIMER12RST</td><td>TIMER11RST</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>DAC1RST</td><td>DAC1 复位由软件置位或复位0:无作用1:复位 DAC0</td></tr><tr><td>29</td><td>DAC0RST</td><td>DAC0 复位由软件置位或复位0:无作用1:复位 DAC0</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>BKPIRST</td><td>BKPI 复位由软件置位或复位0:无作用1:复位 BKP</td></tr><tr><td>26</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>25</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>24</td><td>I2C2RST</td><td>I2C2 复位由软件置位或复位0:无作用1:复位 I2C2</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr></table>

<table><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用1:复位 UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0:无作用1:复位 UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0:无作用1:复位 USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0:无作用1:复位 USART1</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0:无作用1:复位 SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0:无作用1:复位 SPI1</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位0:无作用1:复位 WWDGT</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13RST</td><td>TIMER13 复位由软件置位或复位0:无作用1:复位 TIMER13</td></tr><tr><td>7</td><td>TIMER12RST</td><td>TIMER12 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td>6</td><td>TIMER11RST</td><td>TIMER11 复位由软件置位或复位0:无作用1:复位 TIMER11</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 5.6.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移：0x14

复位值：0x0000 0014

注意：Bit4不能被清为0。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPIEN</td><td>TMUEN</td><td colspan="13">保留</td><td>ENETRXEN</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ENETTX EN</td><td>ENETEN</td><td>ULPIEN</td><td>USBHSE N</td><td>保留</td><td>SDIOEN</td><td>保留</td><td>EXMCEN</td><td>保留</td><td>CRCEN</td><td colspan="3">保留</td><td>SRAMSP EN</td><td>DMA1EN</td><td>DMA0EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPIEN</td><td>SQPI时钟使能由软件置位或复位0:关闭SQPI时钟1:开启SQPI时钟</td></tr><tr><td>30</td><td>TMUEN</td><td>TMU时钟使能由软件置位或复位0:关闭TMU时钟1:开启TMU时钟</td></tr><tr><td>29:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>ENETRXEN</td><td>以太网RX时钟使能由软件置位或复位0:关闭以太网RX时钟1:开启以太网RX时钟</td></tr><tr><td>15</td><td>ENETTXEN</td><td>以太网TX时钟使能由软件置位或复位0:关闭以太网TX时钟1:开启以太网TX时钟</td></tr><tr><td>14</td><td>ENETEN</td><td>以太网时钟使能由软件置位或复位0:关闭以太网时钟1:开启以太网时钟</td></tr><tr><td>13</td><td>ULPIEN</td><td>ULPI时钟使能由软件置位或复位0:关闭ULPI时钟1:开启ULPI时钟</td></tr><tr><td>12</td><td>USBHSEN</td><td>USBHS时钟使能由软件置位或复位0:关闭USBHS时钟1:开启USBHS时钟</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>SDIOEN</td><td>SDIO时钟使能由软件置位或复位0:关闭SDIO时钟</td></tr></table>

<table><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>EXMCEN</td><td>EXMC时钟使能由软件置位或复位0:关闭EXMC时钟1:开启EXMC时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0:关闭CRC时钟1:开启CRC时钟</td></tr><tr><td>5:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPEN</td><td>在睡眠模式下SRAM时钟使能由软件置位或复位0:在睡眠模式下关闭SRAM时钟1:在睡眠模式下开启SRAM时钟</td></tr><tr><td>1</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭DMA1时钟1:开启DMA1时钟</td></tr><tr><td>0</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr></table>

## 5.6.7. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CMPEN</td><td>保留</td><td>SHRTIME REN</td><td>USART5 EN</td><td>保留</td><td>TIMER16 EN</td><td>TIMER15 EN</td><td>TIMER14 EN</td><td colspan="2">保留</td><td>TIMER10 EN</td><td>TIMER9E N</td><td>TIMER8E N</td><td colspan="3">保留</td></tr><tr><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ADC2EN</td><td>USART0 EN</td><td>TIMER7E N</td><td>SPI0EN</td><td>TIMER0E N</td><td>ADC1EN</td><td>ADC0EN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td><td>AFEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CMPEN</td><td>CMP时钟使能由软件置位或复位0:关闭CMP时钟1:开启CMP时钟</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>SHRTIMEREN</td><td>SHRTIMER时钟使能由软件置位或复位0:关闭SHRTIMER时钟1:开启SHRTIMER时钟</td></tr><tr><td>28</td><td>USART5EN</td><td>USART5时钟使能由软件置位或复位0:关闭USART5时钟1:开启USART5时钟</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TIMER16EN</td><td>TIMER16时钟使能由软件置位或复位0:关闭TIMER16时钟1:开启TIMER16时钟</td></tr><tr><td>25</td><td>TIMER15EN</td><td>TIMER15时钟使能由软件置位或复位0:关闭TIMER15时钟1:开启TIMER15时钟</td></tr><tr><td>24</td><td>TIMER14EN</td><td>TIMER14时钟使能由软件置位或复位0:关闭TIMER14时钟1:开启TIMER14时钟</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER10EN</td><td>TIMER10时钟使能由软件置位或复位0:关闭TIMER10时钟1:开启TIMER10时钟</td></tr><tr><td>20</td><td>TIMER9EN</td><td>TIMER9时钟使能由软件置位或复位0:关闭TIMER9时钟1:开启TIMER9时钟</td></tr><tr><td>19</td><td>TIMER8EN</td><td>TIMER8时钟使能由软件置位或复位0:关闭TIMER8时钟</td></tr></table>

<table><tr><td>18:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭ADC2时钟1:开启ADC2时钟</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>13</td><td>TIMER7EN</td><td>TIMER7时钟使能由软件置位或复位0:关闭TIMER7时钟1:开启TIMER7时钟</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0时钟使能由软件置位或复位0:关闭SPI0时钟1:开启SPI0时钟</td></tr><tr><td>11</td><td>TIMER0EN</td><td>TIMER0时钟使能由软件置位或复位0:关闭TIMER0时钟1:开启TIMER0时钟</td></tr><tr><td>10</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>9</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>8</td><td>PGEN</td><td>GPIO端口G时钟使能由软件置位或复位0:关闭GPIO端口G时钟1:开启GPIO端口G时钟</td></tr><tr><td>7</td><td>PFEN</td><td>GPIO端口F时钟使能由软件置位或复位0:关闭GPIO端口F时钟1:开启GPIO端口F时钟</td></tr><tr><td>6</td><td>PEEN</td><td>GPIO端口E时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0: 关闭 GPIO 端口 E 时钟1: 开启 GPIO 端口 E 时钟</td></tr><tr><td>5</td><td>PDEN</td><td>GPIO 端口 D 时钟使能由软件置位或复位0: 关闭 GPIO 端口 D 时钟1: 开启 GPIO 端口 D 时钟</td></tr><tr><td>4</td><td>PCEN</td><td>GPIO 端口 C 时钟使能由软件置位或复位0: 关闭 GPIO 端口 C 时钟1: 开启 GPIO 端口 C 时钟</td></tr><tr><td>3</td><td>PBEN</td><td>GPIO 端口 B 时钟使能由软件置位或复位0: 关闭 GPIO 端口 B 时钟1: 开启 GPIO 端口 B 时钟</td></tr><tr><td>2</td><td>PAEN</td><td>GPIO 端口 A 时钟使能由软件置位或复位0: 关闭 GPIO 端口 A 时钟1: 开启 GPIO 端口 A 时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AFEN</td><td>复用功能 IO 时钟使能由软件置位或复位0: 关闭复用功能 IO 时钟1: 开启复用功能 IO 时钟</td></tr></table>

## 5.6.8. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>DAC1EN</td><td>DAC0EN</td><td>PMUEN</td><td>BKPIEN</td><td>CAN1EN</td><td>CAN0EN</td><td>I2C2EN</td><td>保留</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td colspan="2">保留</td><td>TIMER13EN</td><td>TIMER12EN</td><td>TIMER11EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>DAC1EN</td><td>DAC1时钟使能由软件置位或复位0:关闭DAC1时钟1:开启DAC1时钟</td></tr><tr><td>29</td><td>DAC0EN</td><td>DAC0时钟使能由软件置位或复位0:关闭DAC0时钟1:开启DAC0时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>27</td><td>BKPIEN</td><td>BKP时钟使能由软件置位或复位0:关闭BKP时钟1:开启BKP时钟</td></tr><tr><td>26</td><td>CAN1EN</td><td>CAN1时钟使能由软件置位或复位0:关闭CAN1时钟1:开启CAN1时钟</td></tr><tr><td>25</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>24</td><td>I2C2EN</td><td>I2C2时钟使能由软件置位或复位0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13EN</td><td>TIMER13时钟使能由软件置位或复位0:关闭TIMER13时钟1:开启TIMER13时钟</td></tr><tr><td>7</td><td>TIMER12EN</td><td>TIMER12时钟使能由软件置位或复位0:关闭TIMER12时钟1:开启TIMER12时钟</td></tr></table>

<table><tr><td>6</td><td>TIMER11EN</td><td>TIMER11时钟使能由软件置位或复位0:关闭 TIMER11 时钟1:开启 TIMER11 时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6时钟使能由软件置位或复位0:关闭 TIMER6 时钟1:开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5时钟使能由软件置位或复位0:关闭 TIMER5 时钟1:开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4时钟使能由软件置位或复位0:关闭 TIMER4 时钟1:开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3时钟使能由软件置位或复位0:关闭 TIMER3 时钟1:开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2时钟使能由软件置位或复位0:关闭 TIMER2 时钟1:开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1时钟使能由软件置位或复位0:关闭 TIMER1 时钟1:开启 TIMER1 时钟</td></tr></table>

## 5.6.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，只能由备份域复位进行复位

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的 LXTALEN、LXTALBPS、RTCSRC 和 RTCEN位仅在备份域复位后才清 0。只有在电源控制寄存器（PMU_CTL）中的 BKPWEN 位置 1 后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC40K时钟作为RTC的时钟源11:选择CK_HXTAL/128时钟作为RTC的时钟源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值00:弱驱动能力01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能</td></tr></table>

由软件置位或复位0：关闭 LXTAL 时钟1：使能 LXTAL 时钟

## 5.6.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C00 0000，所有复位标志位仅在电源复位时被清零，RSTFC / IRC40KEN 在系统复位时被清零。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>BORRSTF</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC40KSTB</td><td>IRC40KEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位</td></tr></table>

<table><tr><td></td><td></td><td>电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>BORRSTF</td><td>欠压复位复位标志位欠压复位复位发生时由硬件置1向RSTFC位写1来清除该位0:无欠压复位复位发生1:发生欠压复位复位</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用1:清除所有复位标志位</td></tr><tr><td>23:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC40KSTB</td><td>IRC40K时钟稳定标志位该位由硬件置1指示IRC40K输出时钟是否稳定待用0:IRC40K时钟未稳定1:IRC40K已稳定</td></tr><tr><td>0</td><td>IRC40KEN</td><td>IRC40K使能由软件置位和复位0:关闭IRC40K时钟1:开启IRC40K时钟</td></tr></table>

## 5.6.11. AHB 复位寄存器（RCU_AHBRST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPIRST</td><td>TMURST</td><td colspan="14">保留</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>ENETRS T</td><td>保留</td><td>USBHSR ST</td><td colspan="12">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPIRST</td><td>SQPI 复位由软件置位或复位0:无作用1:复位 SQPI</td></tr><tr><td>30</td><td>TMURST</td><td>TMU 复位由软件置位或复位0:无作用1:复位 TMU</td></tr><tr><td>29:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>ENETRST</td><td>ENET 复位由软件置位或复位0:无作用1:复位 ENET</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>USBHSRST</td><td>USBHS 复位由软件置位或复位0:无作用1:复位 USBHS</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.12. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLL2MF[4]</td><td>PLLREPS EL</td><td>ADCPSC[3]</td><td>PLL2MF[5]</td><td colspan="8">保留</td><td>SHRTIME RSEL</td><td>I2S2SEL</td><td>I2S1SEL</td><td>PREDV0 SEL</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">PLL2MF[3:0]</td><td colspan="4">PLL1MF[3:0]</td><td colspan="4">PREDV1[3:0]</td><td colspan="4">PREDV0[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLL2MF[4]</td><td>PLL2MF的第4位参考寄存器RCU_CFG1的12到15位</td></tr><tr><td>30</td><td>PLLPRESEL</td><td>PLL时钟源预选择由软件置位或复位,控制PLL时钟源0: HXTAL 被选择为 PLL 时钟的时钟源1: CK_IRC48M 被选择为 PLL 时钟的时钟源</td></tr><tr><td>29</td><td>ADCPSC[3]</td><td>ADCPSC 的第 3 位参考寄存器 RCU_CFG0 的 14 到 15 位</td></tr><tr><td>28</td><td>PLL2MF[5]</td><td>PLL2MF 的第 5 位参考寄存器 RCU_CFG1 的 12 到 15 位</td></tr><tr><td>27:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>SHRTIMERSEL</td><td>SHRTIMER 时钟源选择由软件置位或复位,控制 SHRTIMER 时钟源0: APB2 时钟被选择为 SHRTIMER 时钟的时钟源1: 系统时钟被选择为 SHRTIMER 时钟的时钟源</td></tr><tr><td>18</td><td>I2S2SEL</td><td>I2S2 时钟源选择由软件置位或复位,控制 I2S2 时钟源0: 系统时钟被选择为 I2S2 时钟的时钟源1: (CK_PLL2 x 2) 被选择为 I2S2 时钟的时钟源</td></tr><tr><td>17</td><td>I2S1SEL</td><td>I2S1 时钟源选择由软件置位或复位,控制 I2S1 时钟源0: 系统时钟被选择为 I2S1 时钟的时钟源1: (CK_PLL2 x 2) 被选择为 I2S1 时钟的时钟源</td></tr><tr><td>16</td><td>PREDV0SEL</td><td>PREDV0 时钟源选择由软件置位或复位0: HXTAL 或 IRC48M 被选择为 PREDV0 的时钟源1: CK_PLL1 被选择为 PREDV0 的时钟源</td></tr><tr><td>15:12</td><td>PLL2MF[3:0]</td><td>PLL2 时钟倍频因子与寄存器 RCU_CFG1 的 31 位和 28 位共同构成倍频因子,由软件置位或清零000xx: 保留0010x: 保留0110: (PLL2 时钟源 x 8)0111: (PLL2 时钟源 x 9)1000: (PLL2 时钟源 x 10)1001: (PLL2 时钟源 x 11)1010: (PLL2 时钟源 x 12)1011: (PLL2 时钟源 x 13)1100: (PLL2 时钟源 x 14)1101: 保留1110: (PLL2 时钟源 x 16)1111: (PLL2 时钟源 x 20)10000: (PLL2 时钟源 x 18)...10110: (PLL2 时钟源 x 24)</td></tr></table>

<table><tr><td rowspan="13"></td><td rowspan="13"></td><td>10111: (PLL2时钟源x25)</td></tr><tr><td>11000: (PLL2时钟源x26)</td></tr><tr><td>11001: (PLL2时钟源x27)</td></tr><tr><td>11010: (PLL2时钟源x28)</td></tr><tr><td>11011: (PLL2时钟源x29)</td></tr><tr><td>11100: (PLL2时钟源x30)</td></tr><tr><td>11101: (PLL2时钟源x31)</td></tr><tr><td>11110: (PLL2时钟源x32)</td></tr><tr><td>11111: (PLL2时钟源x40)</td></tr><tr><td>100000: (PLL2时钟源x34)</td></tr><tr><td>...</td></tr><tr><td>111110: (PLL2时钟源x64)</td></tr><tr><td>111111: (PLL2时钟源x80)</td></tr><tr><td>11:8</td><td>PLL1MF[3:0]</td><td>PLL1时钟倍频因子由软件置位或清零00xx:保留010x:保留0110: (PLL1源时钟x8)0111: (PLL1源时钟x9)1000: (PLL1源时钟x10)1001: (PLL1源时钟x11)1010: (PLL1源时钟x12)1011: (PLL1源时钟x13)1100: (PLL1源时钟x14)1101: (PLL1源时钟x15)1110: (PLL1源时钟x16)1111: (PLL1源时钟x20)</td></tr><tr><td>7:4</td><td>PREDV1[3:0]</td><td>PREDV1分频因子由软件置位或清零,PLL1和PLL2未使能时,可以修改这些位0000: PREDV1输入源时钟未分频0001: PREDV1输入源时钟2分频0010: PREDV1输入源时钟3分频0011: PREDV1输入源时钟4分频0100: PREDV1输入源时钟5分频0101: PREDV1输入源时钟6分频0110: PREDV1输入源时钟7分频0111: PREDV1输入源时钟8分频1000: PREDV1输入源时钟9分频1001: PREDV1输入源时钟10分频1010: PREDV1输入源时钟11分频1011: PREDV1输入源时钟12分频1100: PREDV1输入源时钟13分频1101: PREDV2输入源时钟14分频</td></tr></table>

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td>1110: PREDV2 输入源时钟 15 分频</td></tr><tr><td>1111: PREDV2 输入源时钟 16 分频</td></tr><tr><td>3:0</td><td>PREDV0[3:0]</td><td>PREDV0 分频因子由软件置位或清零,PLL 未使能时,可以修改这些位注意:PREDV0 的第 0 位与 RCU_CFG0 寄存器的 17 位相同,修改 RCU_CFG0 寄存器的 17 位,PREDV0 的第 0 位也会进行相同的修改0000: PREDV0 输入源时钟未分频0001: PREDV0 输入源时钟 2 分频0010: PREDV0 输入源时钟 3 分频0011: PREDV0 输入源时钟 4 分频0100: PREDV0 输入源时钟 5 分频0101: PREDV0 输入源时钟 6 分频0110: PREDV0 输入源时钟 7 分频0111: PREDV0 输入源时钟 8 分频1000: PREDV0 输入源时钟 9 分频1001: PREDV0 输入源时钟 10 分频1010: PREDV0 输入源时钟 11 分频1011: PREDV0 输入源时钟 12 分频1100: PREDV0 输入源时钟 13 分频1101: PREDV0 输入源时钟 14 分频1110: PREDV0 输入源时钟 15 分频1111: PREDV0 输入源时钟 16 分频</td></tr></table>

## 5.6.13. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为1.0V001:在深度睡眠模式下内核电压为0.9V010:在深度睡眠模式下内核电压为0.8V</td></tr></table>

1xx：保留

## 5.6.14. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0x8000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">保留</td><td>IRC48MS TB</td><td>IRC48ME N</td></tr><tr><td colspan="14">r</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PLLUSBS TB</td><td>PLLUSBEN</td><td colspan="7">保留</td><td>USBSWEN</td><td colspan="3">USBHSDV[2:0]</td><td>USBHSS EL</td><td colspan="2">CK48MSEL[1:0]</td></tr><tr><td>r</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB[7:0]</td><td>内部48MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部48MHz RC振荡器时钟稳定标志位硬件置‘1’来指示IRC48M振荡器时钟是否稳定待用0: IRC48M未稳定1: IRC48M已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部48MHz RC 振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位0: 关闭IRC48M时钟1: 打开IRC48M时钟</td></tr><tr><td>15</td><td>PLLUSBSTB</td><td>PLLUSB时钟稳定标志位硬件置‘1’来指示PLLUSB时钟是否稳定待用0: PLLUSB时钟未稳定1: PLLUSB时钟已稳定</td></tr><tr><td>14</td><td>PLLUSBEN</td><td>PLLUSB使能由软件置位和复位。0: 关闭PLLUSB时钟1: 打开PLLUSB时钟</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>USBSWEN</td><td>USB时钟源选择使能1: 使用USBSW选择USB时钟</td></tr><tr><td>5:3</td><td>USBHSDV[2:0]</td><td>USBHS时钟分频因子由软件置位或清零。000: USBHSDV输入源时钟2分频001: USBHSDV输入源时钟4分频...111: USBHSDV输入源时钟16分频</td></tr><tr><td>2</td><td>USBHSSEL</td><td>USBHS时钟源选择由软件置位和复位。0: 选择48M时钟作为USBHS时钟源1: 选择60M时钟作为USBHS时钟源</td></tr><tr><td>1:0</td><td>CK48MSEL</td><td>48MHz时钟源选择由软件置位和复位。00: 选择CK_PLL / USBHSPSC时钟为48M时钟源01: 选择IRC48M时钟为48M时钟源11: 选择PLLUSB/USBHSDV为48M时钟源11: 选择PLL2位48M时钟源</td></tr></table>

## 5.6.15. 附加时钟配置寄存器（RCU_ADDCFG）

地址偏移： 0XC4

复位值：0x0000 0000


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td colspan="7">PLLUSBMF[6:0]</td><td>PLLUSBPREDVSEL</td><td>PLLUSBPRESEL</td></tr><tr><td colspan="14">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">PLLUSBPREDV [3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24:18</td><td>PLLUSBMF[6:0]</td><td>PLLUSB时钟倍频因子注意:PLLUSB输出时钟频率不能超过480MHz0010000:CK_PLLUSB = CK_PLLUSBSRC x 160010001:CK_PLLUSB = CK_PLLUSBSRC x 170010010:CK_PLLUSB = CK_PLLUSBSRC x 180010011:CK_PLLUSB = CK_PLLUSBSRC x 19</td></tr></table>

17 PLLUSBPREDVSELPLLUSBPREDV输入时钟源选择由软件置位和复位。0：PLLUSBSRC输出为PLLUSBPREDV输入时钟源1：PLL1时钟为PLLUSBPREDV输入源时钟

3:0 PLLUSBPREDV[3:0]PLLUSBPREDV的时钟分频系数由软件置位和复位。0000：保留0001：PLLUSBPREDV 输入源时钟未分频0010：PLLUSBPREDV 输入源时钟 2 分频0011：PLLUSBPREDV 输入源时钟 3 分频0100：PLLUSBPREDV 输入源时钟 4 分频0101：PLLUSBPREDV 输入源时钟 5 分频0110：PLLUSBPREDV 输入源时钟 6 分频0111：PLLUSBPREDV 输入源时钟 7 分频1000：PLLUSBPREDV 输入源时钟 8 分频1001：PLLUSBPREDV 输入源时钟 9 分频1010：PLLUSBPREDV 输入源时钟 10 分频1011：PLLUSBPREDV 输入源时钟 11 分频1100：PLLUSBPREDV 输入源时钟 12 分频1101：PLLUSBPREDV 输入源时钟 13 分频1110：PLLUSBPREDV 输入源时钟 14 分频1111：PLLUSBPREDV 输入源时钟15分频

## 5.6.16. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>PLLUSBSTBIC</td><td>IRC48MSTBIC</td><td colspan="6">保留</td></tr><tr><td colspan="16">w w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PLLUSBSTBIE</td><td>IRC48MSTBIE</td><td colspan="6">保留</td><td>PLLUSBSTBIF</td><td>IRC48MSTBIF</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PLLUSBSTBIC</td><td>PLLUSB 稳定中断清零软件写 1 复位 PLLUSBSTBIF 标志位0: 不复位 PLLUSBSTBIF 标志位1: 复位 PLLUSBSTBIF 标志位</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部 48 MHz RC 振荡器稳定中断清零软件写 1 复位 IRC48MSTBIF 标志位0: 不复位 IRC48MSTBIF 标志位1: 复位 IRC48MSTBIF 标志位</td></tr><tr><td>21:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>PLLUSBSTBIE</td><td>PLLUSB 稳定中断使能由软件置位和复位来使能/禁止 PLLUSB 时钟稳定中断0: 禁止 PLLUSB 时钟稳定中断1: 使能 PLLUSB 时钟稳定中断</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部 48 MHz RC 振荡器稳定中断使能由软件置位和复位来使能/禁止 IRC48M 时钟稳定中断0: 禁止 IRC48M 时钟稳定中断1: 使能 IRC48M 时钟稳定中断</td></tr><tr><td>13:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>PLLUSBSTBIF</td><td>PLLUSB 时钟稳定中断标志位当 PLLUSB 时钟稳定且 PLLUSB 位被置 1 时由硬件置 1软件置位 PLLUSB 位时清除该位0: 无 PLLUSB 时钟稳定中断产生1: 产生 PLLUSB 时钟稳定中断</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M 时钟稳定中断标志位当内部 48 MHz RC 振荡器时钟稳定且 IRC48MSTBIE 位被置 1 时由硬件置 1软件置位 IRC48MSTBIC 位时清除该位0: 无 IRC48M 时钟稳定中断产生1: 产生 IRC48M 时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.17. PLL 时钟扩频控制寄存器（RCU_PLLSSCTL）

地址偏移：0xD0

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

扩频调制仅适用于主 PLL 时钟

仅当 PLL 被禁止时，RCU_PLLSSCTL 寄存器才可写入

该寄存器用于配置 PLL 扩频时钟生成，需按照如下公式：

$$
\text { MODCNT } = \text { round } (f _ {\text { PLLIN }} / 4 / f _ {\text { mod }})
$$

$$
\text { MODSTEP } = \text { round } (\text { mdamp } * \text { PLLN } * 2 ^ {1 5} / (\text { MODCNT } * 1 0 0))
$$

f<sub>PLLIN</sub>表示 PLL 输入时钟频率，f<sub>mod</sub>表示扩频调制频率，mdamp 表示扩频调制振幅（按百分比表示），PLLN 表示 PLL时钟频率倍频因子

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SSCGON</td><td>SS_TYPE</td><td colspan="2">保留</td><td colspan="12">MODSTEP[14:3]</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">MODSTEP[2:0]</td><td colspan="13">MODCNT[12:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SSCGON</td><td>PLL 扩频调制使能0:禁止扩频调制1:使能扩频调制</td></tr><tr><td>30</td><td>SS_TYPE</td><td>PLL 扩频调制类型选择0:选择中心扩频1:选择向下扩频</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:13</td><td>MODSTEP</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件: MODSTEP*MODCNT≤<eq>2^{15}</eq>-1</td></tr><tr><td>12:0</td><td>MODCNT</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件: MODSTEP*MODCNT≤<eq>2^{15}</eq>-1</td></tr></table>

## 5.6.18. 配置寄存器 2（RCU_CFG2）

地址偏移：0XD4

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">I2C2SEL[1:0]</td><td colspan="2">保留</td><td colspan="2">USART5SEL[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>I2C2SEL[1:0]</td><td>I2C2时钟源选择由软件置1或清0。00:I2C2时钟源选择APB1时钟01:I2C2时钟源选择系统时钟1x:I2C2时钟源选择IRC8M</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>USART5SEL[1:0]</td><td>USART5时钟源选择由软件置1或清0。00:USART5时钟选择APB2时钟01:USART5时钟选择系统时钟10:USART5时钟选择LXTAL时钟11:USART5时钟选择IRC8M时钟</td></tr></table>

## 5.6.19. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CAN2RS T</td><td colspan="3">保留</td><td>CTC RST</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CAN2RST</td><td>CAN2 复位由软件置位或复位0:无作用1:复位 CAN2</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.6.20. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CAN2EN</td><td colspan="3">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CAN2EN</td><td>CAN2 时钟使能由软件置位或复位0: 关闭 CAN2 时钟1: 开启 CAN2 时钟</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC 时钟使能由软件置位或复位0: 关闭 CTC 时钟1: 开启 CTC 时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

