# 6.3. RCU 寄存器

RCU 基地址：0x5802 4400

# 6.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0xC000 8040

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IRC64MS TB</td><td>IRC64ME N</td><td>PLL2STB</td><td>PLL2EN</td><td>PLL1STB</td><td>PLL1EN</td><td>PLL0STB</td><td>PLL0EN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALB PS</td><td>HXTALST B</td><td>HXTALE N</td></tr><tr><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">IRC64MCALIB[8:0]</td><td colspan="7">IRC64MADJ[6:0]</td></tr><tr><td colspan="9">r</td><td colspan="7">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IRC64MSTB</td><td>内部64MHz RC振荡器稳定标志位硬件置‘1’来指示IRC64M振荡器时钟是否稳定待用0: IRC64M振荡器未稳定1: IRC64M 振荡器已稳定</td></tr><tr><td>30</td><td>IRC64MEN</td><td>内部64MHz RC振荡器使能软件置位或复位,如果IRC64M时钟作为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当CKMEN置位同时用作系统时钟的HXTAL振荡器发生故障时,该位由硬件置1来启动IRC64M振荡器。0: 内部64 MHz RC振荡器被关闭1: 内部 64 MHz RC 振荡器被打开</td></tr><tr><td>29</td><td>PLL2STB</td><td>PLL2 时钟稳定标志位硬件置1来表示PLL2输出时钟是否稳定待用0: PLL2未稳定1: PLL2 已稳定</td></tr><tr><td>28</td><td>PLL2EN</td><td>PLL2 使能软件置位或复位,当进入深度睡眠或待机模式时由硬件复位0: PLL2被关闭1: PLL2 被打开</td></tr><tr><td>27</td><td>PLL1STB</td><td>PLL1 时钟稳定标志位硬件置1来表示PLL1输出时钟是否稳定待用0: PLL1未稳定1: PLL1 已稳定</td></tr><tr><td>26</td><td>PLL1EN</td><td>PLL1 使能软件置位或复位,当进入深度睡眠或待机模式时由硬件复位0:PLL1被关闭1:PLL1被打开</td></tr><tr><td>25</td><td>PLL0STB</td><td>PLL0时钟稳定标志位硬件置1来表示PLL0输出时钟是否稳定待用0:PLL0未稳定1:PLL0已稳定</td></tr><tr><td>24</td><td>PLL0EN</td><td>PLL0使能软件置位或复位,当PLL0时钟作为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL0被关闭1:PLL0被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~50MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~50MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC64M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC64MEN的状态,自动使能IRC64M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTAL位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL0P时钟作为系统时钟时,其作为PLL0的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:高速4~50MHz晶体振荡器被关闭1:高速4~50MHz晶体振荡器被打开</td></tr><tr><td>15:7</td><td>IRC64MCALIB[8:0]</td><td>内部64MHz RC振荡器校准值上电时自动加载这些位</td></tr><tr><td>6:0</td><td>IRC64MADJ[6:0]</td><td>内部64MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC64MADJ[6:0]位域的当前值加上</td></tr></table>

IRC64MCALIB[8:0]位域的值。最终调整值应该调整 IRC64M 到 64 MHz ± 1%

# 6.3.2. PLL0 寄存器（RCU_PLL0）

地址偏移：0x04

复位值：0x0100 2020

配置PLL0时钟可参考下列公式：

CK_PLL0VCOSRC = CK_PLL0SRC / PLL0PSC
CK_PLL0VCO = CK_PLL0VCOSRC × (PLL0N + PLL0FRAN / 2 $^{13}$ )
CK_PLL0R = CK_PLL0VCO / PLL0R
CK_PLL0P = CK_PLL0VCO / PLL0P 

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLLSTBSRC</td><td colspan="7">PLL0R[6:0]</td><td>保留</td><td colspan="7">PLL0P[6:0]</td></tr><tr><td>w</td><td colspan="9">rw</td><td colspan="6">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="9">PLL0N[8:0]</td><td colspan="6">PLL0PSC[5:0]</td></tr><tr><td colspan="10">rw</td><td colspan="6">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLLSTBSRC</td><td>PLLs 稳定信号源0: 模拟信号1: 数字信号</td></tr><tr><td>30:24</td><td>PLL0R[6:0]</td><td>PLL0R 输出频率的分频系数(PLL0 VCO 时钟作为输入)当 PLL0 被关闭时由软件置位或清零。这些位域用做将 PLL0 VCO 时钟(CK_PLL0VCO)分频生成 PLL0R 输出时钟(CK_PLL0R)。RCU_PLL0 寄存器的 PLL0N 位域对 CK_PLL0VCO 时钟进行了描述。0000000: CK_PLL0R = CK_PLL0VCO0000001: CK_PLL0R = CK_PLL0VCO / 20000010: CK_PLL0R = CK_PLL0VCO / 3.0000011: CK_PLL0R = CK_PLL0VCO / 40000100: CK_PLL0R = CK_PLL0VCO / 5...1111111: CK_PLL0R = CK_PLL0VCO / 128</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:16</td><td>PLL0P[6:0]</td><td>PLL0P 输出频率分频系数(PLL0 VCO 时钟作为输入)当 PLL0 被关闭时由软件置位或清零。这些位域用做将 PLL0 VCO 时钟(CK_PLL0VCO)分频生成 PLL0P 输出时钟(CK_PLL0P)。CK_PLL0P 时钟可以被用作系统时钟(不超过 600MHz)。 RCU_PLL0 寄存器的 PLL0N 位域对 CK_PLL0VCO 时钟进行了描述。</td></tr></table>

0000000：CK_PLL0P = CK_PLL0VCO 

0000001：CK_PLL0P = CK_PLL0VCO / 2 

0000010：CK_PLL0P = CK_PLL0VCO / 3 

0000011：CK_PLL0P = CK_PLL0VCO / 4 

0000100：CK_PLL0P = CK_PLL0VCO / 5 

1111111：CK_PLL0P = CK_PLL0VCO / 128 

15 保留 必须保持复位值。

14:6 PLL0N[8:0] PLL0 VCO 时钟倍频因子

当 PLL0 被关闭时由软件置位或清零（仅支持全字/半字写操作）。这些位域用做将PLL0 VCO 源 时 钟 （ CK_PLL0VCOSRC ） 倍 频 生 成 PLL0 VCO 输 出 时 钟（CK_PLL0VCO）。RCU_PLL0 寄存器的 PLL0PSC 位域对 CK_PLL0VCOSRC 时钟进行了描述。

注意：CK_PLL0VCO 时钟频率范围必须在 150MHz 到 836MHz 之间

PLL0N 的值必须满足：

当 PLL0 小数锁存禁能时，PLL0N 的值必须满足：9 ≤ PLL0N ≤ 512

当 PLL0 小数锁存使能时，PLL0N 的值必须满足：12 ≤ PLL0N ≤ 508

000000000：保留

000000111：保留

000001000：PLL0N = 9 

001000000：PLL0N = 65 

001000001：PLL0N = 66 

111111111：PLL0N = 512 

5:0 PLL0PSC[5:0] PLL0 VCO 源时钟分频器

当PLL0被关闭时由软件置位或清零。这些位域用做将PLL0源时钟（CK_PLL0SRC）分频生成 PLL0 VCO 源时钟（CK_PLL0VCOSRC）。RCU_PLLALL 寄存器的 PLLSEL位对 CK_PLL0SRC 时钟进行了描述。

VCO源时钟频率范围必须在 1MHz 到16MHz 之间

000000：保留

000001：CK_PLL0SRC 

000010：CK_PLL0SRC / 2 

000011：CK_PLL0SRC / 3 

111111：CK_PLL0SRC / 63 

# 6.3.3. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x08

复位值：0x0000 0000


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">I2C0SEL[1:0]</td><td colspan="3">APB3PSC[2:0]</td><td colspan="3">APB4PSC[2:0]</td><td colspan="2">保留</td><td colspan="6">RTCDIV[5:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="6">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="2">保留</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="3">rw</td><td colspan="5">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>I2C0SEL[1:0]</td><td>I2C0时钟源选择由软件置位或复位,控制I2C0时钟源00:选择CK_APB1时钟作为I2C0源时钟01:选择CK_PLL2R时钟作为I2C0源时钟10:选择CK_IRC64MDIV时钟作为I2C0源时钟11:选择CK_LPIRC4M时钟作为I2C0源时钟</td></tr><tr><td>29:27</td><td>APB3PSC[2:0]</td><td>APB3预分频选择由软件置位或清零,控制APB3时钟分频因子0xx:选择CK_AHB时钟不分频100:选择CK_AHB时钟2分频101:选择CK_AHB时钟4分频110:选择CK_AHB时钟8分频111:选择CK_AHB时钟16分频</td></tr><tr><td>26:24</td><td>APB4PSC[2:0]</td><td>APB4预分频选择由软件置位或清零,控制APB4时钟分频因子0xx:选择CK_AHB时钟不分频100:选择CK_AHB时钟2分频101:选择CK_AHB时钟4分频110:选择CK_AHB时钟8分频111:选择CK_AHB时钟16分频</td></tr><tr><td>23:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:16</td><td>RTCDIV[5:0]</td><td>RTC时钟分频系数由软件置位或清零。这些位用作将HXTAL时钟分频生成RTC时钟(不超过1MHz)000000:无时钟000001:无时钟000010:CK_HXTAL/2000011:CK_HXTAL/3...111111:CK_HXTAL/63</td></tr><tr><td>15:13</td><td>APB2PSC[2:0]</td><td>APB2预分频选择由软件置位或清零,控制APB2时钟分频因子0xx:选择CK_AHB时钟不分频100:选择CK_AHB时钟2分频</td></tr></table>

101：选择 CK_AHB 时钟 4 分频

110：选择 CK_AHB 时钟 8 分频

111：选择 CK_AHB 时钟 16 分频

12:10 APB1PSC[2:0] 

APB1 预分频选择

由软件置位或清零，控制 APB1 时钟分频因子.

0xx：选择 CK_AHB 时钟不分频

100：选择 CK_AHB 时钟 2 分频

101：选择 CK_AHB 时钟 4 分频

110：选择 CK_AHB 时钟 8 分频

111：选择 CK_AHB 时钟 16 分频

9:8 保留

必须保持复位值。

7:4 AHBPSC[3:0] 

AHB / AXI 预分频选择

由软件置位或清零，控制 AHB / AXI 时钟分频因子.

0xxx：选择 CK_SYS 时钟不分频

1000：选择 CK_SYS 时钟 2 分频

1001：选择 CK_SYS 时钟 4 分频

1010：选择 CK_SYS 时钟 8 分频

1011：选择 CK_SYS 时钟 16 分频

1100：选择 CK_SYS 时钟 64 分频

1101：选择 CK_SYS 时钟 128 分频

1110：选择 CK_SYS 时钟 256 分频

1111：选择 CK_SYS 时钟 512 分频

3:2 SCSS[1:0] 

系统时钟选择状态

由硬件置位或清零，标识当前系统时钟的时钟源

00：选择 CK_IRC64MDIV 时钟作为 CK_SYS 时钟源

01：选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10：选择 CK_LPIRC4M 时钟作为 CK_SYS 时钟源

11：选择 CK_PLL0P 时钟作为 CK_SYS 时钟源

1:0 SCS[1:0] 

系统时钟选择

由软件配置选择系统时钟源。由于CK_SYS的改变存在固有的延迟，因此软件应当读SCSS位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时，以及当HXTAL直接或间接作为系统时钟同时HXTAL时钟监视器检测到HXTAL故障时，强制选择CK_IRC64MDIV作为系统时钟。

00：选择 CK_IRC64MDIV 时钟作为 CK_SYS 时钟源

01：选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10：选择 CK_LPIRC4M 时钟作为 CK_SYS 时钟源

11：选择 CK_PLL0P 时钟作为 CK_SYS 时钟源

# 6.3.4. 时钟中断寄存器（RCU_INT）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>LCKMIC</td><td>LCKMIF</td><td>LPIRC4MSTBIC</td><td>LPIRC4MSTBIE</td><td>LPIRC4MSTBIF</td><td>CKMIC</td><td>PLL2STBIC</td><td>PLL1STBIC</td><td>PLLOSTBIC</td><td>HXTALSTBIC</td><td>IRC64MSTBIC</td><td>LXTALSTBIC</td><td>IRC32KSTBIC</td></tr><tr><td colspan="3"></td><td>w</td><td>r</td><td>w</td><td>rw</td><td>r</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>PLL2STBIE</td><td>PLL1STBIE</td><td>PLL0STBIE</td><td>HXTALSTBIE</td><td>IRC64MSTBIE</td><td>LXTALSTBIE</td><td>IRC32KSTBIE</td><td>CKMIF</td><td>PLL2STBIF</td><td>PLL1STBIF</td><td>PLLOSTBIF</td><td>HXTALSTBIF</td><td>IRC64MSTBIF</td><td>LXTALSTBIF</td><td>IRC32KSTBIF</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>LCKMIC</td><td>LXTAL时钟阻塞中断清零软件写1复位LCKMIF标志位0:不复位LCKMIF标志位1:复位LCKMIF标志位</td></tr><tr><td>27</td><td>LCKMIF</td><td>LXTAL时钟阻塞中断标志位当LXTAL时钟被阻塞时由硬件置位软件置位LCKMIC位时清除该位0:时钟正常运行1:LXTAL时钟阻塞</td></tr><tr><td>26</td><td>LPIRC4MSTBIC</td><td>LPIRC4M时钟稳定中断清零软件写1复位LPIRC4MSTBIF标志位0:不复位LPIRC4MSTBIF标志位1:复位LPIRC4MSTBIF标志位</td></tr><tr><td>25</td><td>LPIRC4MSTBIE</td><td>LPIRC4M时钟稳定中断使能软件置位和复位来使能/禁止LPIRC4M时钟稳定中断0:禁止LPIRC4M时钟稳定中断1:使能LPIRC4M时钟稳定中断</td></tr><tr><td>24</td><td>LPIRC4MSTBIF</td><td>LPIRC4M时钟稳定中断标志位当内部64MHz RC振荡器时钟稳定且LPIRC4MSTBIE位被置1时由硬件置1软件置位LPIRC4MSTBIC位时清除该位0:无LPIRC4M时钟稳定中断产生1:产生LPIRC4M时钟稳定中断</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位.0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>PLL2STBIC</td><td>PLL2时钟稳定中断清零软件写1复位PLL2STBIF标志位0:不复位PLL2STBIF标志位</td></tr></table>

1：复位 PLL2STBIF 标志位

<table><tr><td>21</td><td>PLL1STBIC</td><td>PLL1 时钟稳定中断清零软件写 1 复位 PLL1STBIF 标志位0:不复位 PLL1STBIF 标志位1:复位 PLL1STBIF 标志位</td></tr></table>

<table><tr><td>20</td><td>PLL0STBIC</td><td>PLL0 时钟稳定中断清零软件写 1 复位 PLL0STBIF 标志位0: 不复位 PLL0STBIF 标志位1: 复位 PLL0STBIF 标志位</td></tr></table>

<table><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL 时钟稳定中断清零软件写 1 复位 HXTALSTBIF 标志位0: 不复位 HXTALSTBIF 标志位1: 复位 HXTALSTBIF 标志位</td></tr></table>

<table><tr><td>18</td><td>IRC64MSTBIC</td><td>IRC64M 时钟稳定中断清零软件写 1 复位 IRC64MSTBIF 标志位0:不复位 IRC64MSTBIF 标志位1:复位 IRC64MSTBIF 标志位</td></tr></table>

<table><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL 时钟稳定中断清零软件写 1 复位 LXTALSTBIF 标志位0: 不复位 LXTALSTBIF 标志位1: 复位 LXTALSTBIF 标志位</td></tr></table>

<table><tr><td>16</td><td>IRC32KSTBIC</td><td>IRC32K 时钟稳定中断清零软件写 1 复位 IRC32KSTBIF 标志位0: 不复位 IRC32KSTBIF 标志位1: 复位 IRC32KSTBIF 标志位</td></tr></table>

15 保留 必须保持复位值。

<table><tr><td>14</td><td>PLL2STBIE</td><td>PLL2 时钟稳定中断使能软件置位和复位来使能/禁止PLL2时钟稳定中断0:禁止 PLL2 时钟稳定中断1:使能 PLL2 时钟稳定中断</td></tr></table>

<table><tr><td>13</td><td>PLL1STBIE</td><td>PLL1 时钟稳定中断使能软件置位和复位来使能/禁止PLL1时钟稳定中断0:禁止 PLL1 时钟稳定中断1:使能 PLL1 时钟稳定中断</td></tr></table>

<table><tr><td>12</td><td>PLL0STBIE</td><td>PLL0 时钟稳定中断使能软件置位和复位来使能/禁止PLL0时钟稳定中断0:禁止 PLL0 时钟稳定中断1:使能 PLL0 时钟稳定中断</td></tr></table>

11 HXTALSTBIE HXTAL 时钟稳定中断使能

软件置位和复位来使能/禁止HXTAL时钟稳定中断

0：禁止HXTAL时钟稳定中断

1：使能 HXTAL 时钟稳定中断

10 IRC64MSTBIE 

IRC64M 时钟稳定中断使能

软件置位和复位来使能/禁止IRC64M时钟稳定中断

0：禁止IRC64M时钟稳定中断

1：使能 IRC64M 时钟稳定中断

9 LXTALSTBIE 

LXTAL 时钟稳定中断使能

软件置位和复位来使能/禁止LXTAL时钟稳定中断

0：禁止LXTAL时钟稳定中断

1：使能 LXTAL 时钟稳定中断

8 IRC32KSTBIE 

IRC32K 时钟稳定中断使能

软件置位和复位来使能/禁止IRC32K时钟稳定中断

0：禁止IRC32K时钟稳定中断

1：使能 IRC32K 时钟稳定中断

7 CKMIF 

HXTAL时钟阻塞中断标志位

当HXTAL时钟被阻塞时由硬件置位.

软件置位 CKMIC 位时清除该位

0：时钟正常运行

1：HXTAL 时钟阻塞

6 PLL2STBIF 

PLL2 时钟稳定中断标志位

当PLL2时钟稳定且PLL2STBIE位被置1时由硬件置1

软件置位 PLL2STBIC 位时清除该位

0：无PLL2时钟稳定中断产生

1：产生 PLL2 时钟稳定中断

5 PLL1STBIF 

PLL1 时钟稳定中断标志位

当PLL1时钟稳定且PLL1STBIE位被置1时由硬件置1

软件置位 PLL1STBIC 位时清除该位

0：无PLL1时钟稳定中断产生

1：产生 PLL1 时钟稳定中断

4 PLL0STBIF 

PLL0 时钟稳定中断标志位

当PLL0时钟稳定且PLL0STBIE位被置1时由硬件置1

软件置位 PLL0STBIC 位时清除该位

0：无PLL0时钟稳定中断产生

1：产生 PLL0 时钟稳定中断

3 HXTALSTBIF 

HXTAL 时钟稳定中断标志位

当高速4 ~ 50 MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1

软件置位 HXTALSTBIC 位时清除该位

0：无HXTAL时钟稳定中断产生

1：产生HXTAL时钟稳定中断

<table><tr><td>2</td><td>IRC64MSTBIF</td><td>IRC64M时钟稳定中断标志位当内部64MHz RC振荡器时钟稳定且IRC64MSTBIE位被置1时由硬件置1软件置位IRC64MSTBIC位时清除该位0:无IRC64M时钟稳定中断产生1:产生IRC64M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC32KSTBIF</td><td>IRC32K时钟稳定中断标志位当内部32kHz RC振荡器时钟稳定且IRC32KSTBIE位被置1时由硬件置1软件置位IRC32KSTBIC位时清除该位0:无IRC32K时钟稳定中断产生1:产生IRC32K时钟稳定中断</td></tr></table>

# 6.3.5. AHB1 复位寄存器（RCU_AHB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>USBHS1RST</td><td colspan="3">保留</td><td>ENET0RST</td><td>保留</td><td>DMAMUXRST</td><td>DMA1RS T</td><td>DMA0RS T</td><td colspan="5">保留</td></tr><tr><td colspan="2"></td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USBHS0RST</td><td colspan="13">保留</td><td>ENET1RST</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>USBHS1RST</td><td>USBHS1 复位由软件置位或复位0:无作用1:复位 USBHS1</td></tr><tr><td>28:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>ENET0RST</td><td>Ethernet0 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td></td><td></td><td>1: 复位ENET0</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXRST</td><td>DMAMUX复位由软件置位或复位0:无作用1:复位DMAMUX</td></tr><tr><td>22</td><td>DMA1RST</td><td>DMA1复位由软件置位或复位0:无作用1:复位DMA1</td></tr><tr><td>21</td><td>DMA0RST</td><td>DMA0复位由软件置位或复位0:无作用1:复位DMA0</td></tr><tr><td>20:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USBHS0RST</td><td>USBHS0复位由软件置位或复位0:无作用1:复位USBHS0</td></tr><tr><td>13:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>ENET1RST</td><td>Ethernet1复位由软件置位或复位0:无作用1:复位ENET1</td></tr></table>

# 6.3.6. AHB2 复位寄存器（RCU_AHB2RST）

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TMURST</td><td>TRNGRS T</td><td>保留</td><td>HAURST</td><td>CAURST</td><td>SDIO1RS T</td><td>FACRST</td><td>DCIRST</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TMURST</td><td>TMU 复位由软件置位或复位.0:无作用1:复位 TMU</td></tr><tr><td>6</td><td>TRNGRST</td><td>TRNG 复位由软件置位或复位0:无作用1:复位 TRNG</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>HAURST</td><td>HAU 复位由软件置位或复位0:无作用1:复位 HAU</td></tr><tr><td>3</td><td>CAURST</td><td>CAU 复位由软件置位或复位0:无作用1:复位 CAU</td></tr><tr><td>2</td><td>SDIO1RST</td><td>SDIO1 复位由软件置位或复位0:无作用1:复位 SDIO1</td></tr><tr><td>1</td><td>FACRST</td><td>FAC 复位由软件置位或复位0:无作用1:复位 FAC</td></tr><tr><td>0</td><td>DCIRST</td><td>DCI 复位由软件置位或复位0:无作用1:复位 DCI</td></tr></table>

# 6.3.7. AHB3 复位寄存器（RCU_AHB3RST）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>RTDEC1RST</td><td>RTDEC0RST</td><td>保留</td><td>OSPI1RS T</td><td>OSPI0RS T</td><td>OSPIMR ST</td><td>MDMARS T</td><td>SDIO0RS T</td><td>IPARST</td><td>EXMCRS T</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>RTDEC1RST</td><td>RTDEC1 复位由软件置位或复位0:无作用1:复位 RTDEC1</td></tr><tr><td>8</td><td>RTDEC0RST</td><td>RTDEC0 复位由软件置位或复位0:无作用1:复位 RTDEC0</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>OSPI1RST</td><td>OSPI1 复位由软件置位或复位0:无作用1:复位 OSPI1</td></tr><tr><td>5</td><td>OSPI0RST</td><td>OSPI0 复位由软件置位或复位0:无作用1:复位 OSPI0</td></tr><tr><td>4</td><td>OSPIMRST</td><td>OSPIM 复位由软件置位或复位0:无作用1:复位 OSPIM</td></tr><tr><td>3</td><td>MDMARST</td><td>MDMA 复位由软件置位或复位0:无作用1:复位 MDMA</td></tr><tr><td>2</td><td>SDIO0RST</td><td>SDIO0 复位由软件置位或复位0:无作用1:复位 SDIO0</td></tr><tr><td>1</td><td>IPARST</td><td>IPA 复位由软件置位或复位0:无作用</td></tr></table>

1：复位 IPA

<table><tr><td>0</td><td>EXMCRST</td><td>EXMC 复位由软件置位或复位0:无作用1:复位 EXMC</td></tr></table>

# 6.3.8. AHB4 复位寄存器（RCU_AHB4RST）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>HWSEMRST</td><td>CRCRST</td><td colspan="4">保留</td><td>PKRST</td><td>PJRST</td><td>PHRST</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td></tr><tr><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>HWSEMRST</td><td>HWSEM 复位由软件置位或复位0:无作用1:复位 HWSEM</td></tr><tr><td>14</td><td>CRCRST</td><td>CRC 复位由软件置位或复位0:无作用1:复位 CRC</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>PKRST</td><td>GPIO 端口 K 复位由软件置位或复位0:无作用1:复位 GPIO 端口 K</td></tr><tr><td>8</td><td>PJRST</td><td>GPIO 端口 J 复位由软件置位或复位0:无作用1:复位 GPIO 端口 J</td></tr><tr><td>7</td><td>PHRST</td><td>GPIO 端口 H 复位由软件置位或复位</td></tr></table>

0：无作用

1：复位 GPIO 端口 H

6 PGRST GPIO 端口 G 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 G

5 PFRST GPIO 端口 F 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 F

4 PERST GPIO 端口 E 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 E

3 PDRST GPIO 端口 D 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 D

2 PCRST GPIO 端口 C 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 C

1 PBRST GPIO 端口 B 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 B

0 PARST GPIO 端口 A 复位

由软件置位或复位

0：无作用

1：复位 GPIO 端口 A

# 6.3.9. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x20

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7RST</td><td>UART6RST</td><td>DACRST</td><td>DACHOLDRST</td><td>CTCRST</td><td colspan="2">保留</td><td>I2C3RST</td><td>I2C2RST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>USART2RST</td><td>USART1RST</td><td>MDIORS T</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td>RSPDIFRST</td><td>保留</td><td>TIMER51RST</td><td>TIMER50RST</td><td>TIMER31RST</td><td>TIMER30RST</td><td>TIMER23RST</td><td>TIMER22RST</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UART7RST</td><td>UART7 复位由软件置位或复位0:无作用1:复位 UART7</td></tr><tr><td>30</td><td>UART6RST</td><td>UART6 复位由软件置位或复位0:无作用1:复位 UART6</td></tr><tr><td>29</td><td>DACRST</td><td>DAC 复位由软件置位或复位0:无作用1:复位 DAC</td></tr><tr><td>28</td><td>DACHOLDRST</td><td>DAC 保持时钟复位由软件置位或复位,DAC 保持时钟源为 IRC32K0:无作用1:复位 DAC 保持时钟</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用1:复位 CTC</td></tr><tr><td>26:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3RST</td><td>I2C3 复位由软件置位或复位0:无作用1:复位 I2C3</td></tr><tr><td>23</td><td>I2C2RST</td><td>I2C2 复位由软件置位或复位0:无作用1:复位 I2C2</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr></table>

<table><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用1:复位 UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0:无作用1:复位 UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0:无作用1:复位 USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0:无作用1:复位 USART1</td></tr><tr><td>16</td><td>MDIORST</td><td>MDIO 复位由软件置位或复位0:无作用1:复位 MDIO</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0:无作用1:复位 SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0:无作用1:复位 SPI1</td></tr><tr><td>13</td><td>RSPDIFRST</td><td>RSPDIF 复位由软件置位或复位0:无作用1:复位 RSPDIF</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>TIMER51RST</td><td>TIMER51 复位由软件置位或复位</td></tr></table>

0：无作用

1：复位 TIMER51

10 TIMER50RST TIMER50 复位

由软件置位或复位

0：无作用

1：复位 TIMER50

9 TIMER31RST TIMER31 复位

由软件置位或复位

0：无作用

1：复位 TIMER31

8 TIMER30RST TIMER30 复位

由软件置位或复位

0：无作用

1：复位 TIMER30

7 TIMER23RST TIMER23 复位

由软件置位或复位

0：无作用

1：复位 TIMER23

6 TIMER6RST TIMER6 复位

由软件置位或复位

0：无作用

1：复位 TIMER6

5 TIMER6RST TIMER6 复位

由软件置位或复位

0：无作用

1：复位 TIMER6

4 TIMER5RST TIMER5 复位

由软件置位或复位

0：无作用

1：复位 TIMER5

3 TIMER4RST TIMER4 复位

由软件置位或复位

0：无作用

1：复位 TIMER4

2 TIMER3RST TIMER3 复位

由软件置位或复位

0：无作用

1：复位 TIMER3

1 TIMER2RST TIMER2 复位

由软件置位或复位

0：无作用

1：复位 TIMER2

<table><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

# 6.3.10. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x24

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRIGSEL RST</td><td>EDOUTR ST</td><td>TIMER44 RST</td><td>TIMER43 RST</td><td>TIMER42 RST</td><td>TIMER41 RST</td><td>TIMER40 RST</td><td>SAI2RST</td><td>SAI1RST</td><td>SAI0RST</td><td>SPI5RST</td><td>SPI4RST</td><td>HPDFRS T</td><td>TIMER16 RST</td><td>TIMER15 RST</td><td>TIMER14 RST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SPI3RST</td><td>SPI0RST</td><td>保留</td><td>ADC2RST</td><td>ADC1RST</td><td>ADC0RS T</td><td colspan="2">保留</td><td>USART5 RST</td><td>USART0 RST</td><td colspan="2">保留</td><td>TIMER7R ST</td><td>TIMER0R ST</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRIGSELRST</td><td>TRIGSEL 复位由软件置位或复位0:无作用1:复位 TRIGSEL</td></tr><tr><td>30</td><td>EDOUTRST</td><td>EDOUT 复位由软件置位或复位0:无作用1:复位 EDOUT</td></tr><tr><td>29</td><td>TIMER44RST</td><td>TIMER44 复位由软件置位或复位0:无作用1:复位 TIMER44</td></tr><tr><td>28</td><td>TIMER43RST</td><td>TIMER43 复位由软件置位或复位0:无作用1:复位 TIMER43</td></tr><tr><td>27</td><td>TIMER42RST</td><td>TIMER42 复位由软件置位或复位</td></tr></table>

0：无作用

1：复位 TIMER42

26 TIMER41RST TIMER41 复位

由软件置位或复位

0：无作用

1：复位 TIMER41

25 TIMER40RST TIMER40 复位

由软件置位或复位

0：无作用

1：复位 TIMER40

24 SAI2RST SAI2 复位

由软件置位或复位

0：无作用

1：复位 SAI2

23 SAI1RST SAI1 复位

由软件置位或复位

0：无作用

1：复位 SAI1

22 SAI0RST SAI0 复位

由软件置位或复位

0：无作用

1：复位 SAI0

21 SPI5RST SPI5 复位

由软件置位或复位

0：无作用

1：复位 SPI5

20 SPI4RST SPI4 复位

由软件置位或复位

0：无作用

1：复位 SPI4

19 HPDFRST HPDF 复位

由软件置位或复位

0：无作用

1：复位 HPDF

18 TIMER16RST TIMER16 复位

由软件置位或复位

0：无作用

1：复位 TIMER16

17 TIMER15RST TIMER15 复位

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 TIMER15</td></tr><tr><td>16</td><td>TIMER14RST</td><td>TIMER14 复位由软件置位或复位0:无作用1:复位 TIMER14</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>SPI3RST</td><td>SPI3 复位由软件置位或复位0:无作用1:复位 SPI3</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ADC2RST</td><td>ADC2 复位由软件置位或复位0:无作用1:复位所有 ADC2</td></tr><tr><td>9</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0:无作用1:复位所有 ADC1</td></tr><tr><td>8</td><td>ADC0RST</td><td>ADC0 复位由软件置位或复位0:无作用1:复位所有 ADC0</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5RST</td><td>USART5 复位由软件置位或复位0:无作用1:复位 USART5</td></tr><tr><td>4</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0:无作用1:复位 USART0</td></tr></table>

3:2 保留 必须保持复位值。

1 TIMER7RST TIMER7 复位由软件置位或复位

0：无作用

1：复位 TIMER7

0 TIMER0RST TIMER0 复位

由软件置位或复位

0：无作用

1：复位 TIMER0

# 6.3.11. APB3 复位寄存器（RCU_APB3RST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>WWDGTRST</td><td>TLIRST</td></tr></table>


rw rw 



位/位域 名称 描述


<table><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位0:无作用1:复位 WWDGT</td></tr></table>

<table><tr><td>0</td><td>TLIRST</td><td>TLI 复位</td></tr><tr><td></td><td></td><td>由软件置位或复位</td></tr><tr><td></td><td></td><td>0:无作用</td></tr><tr><td></td><td></td><td>1:复位 TLI</td></tr></table>

# 6.3.12. APB4 复位寄存器（RCU_APB4RST）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td></td><td>PMURST</td><td>LPDTSRST</td><td>VREFRS T</td><td>CMPRST</td><td>SYSCFG RST</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>3</td><td>LPDTSRST</td><td>LPDTS 复位由软件置位或复位0:无作用1:复位 LPDTS</td></tr><tr><td>2</td><td>VREFRST</td><td>VREF 复位由软件置位或复位0:无作用1:复位 VREF</td></tr><tr><td>1</td><td>CMPRST</td><td>CMP 复位由软件置位或复位0:无作用1:复位 CMP</td></tr><tr><td>0</td><td>SYSCFGRST</td><td>SYSCFG 复位由软件置位或复位0:无作用1:复位 SYSCFG</td></tr></table>

# 6.3.13. AHB1 使能寄存器（RCU_AHB1EN）

地址偏移：0x30

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>USBHS1ULPIEN</td><td>USBHS1EN</td><td>ENETOPTEN</td><td>ENETORXEN</td><td>ENETOTXEN</td><td>ENETOEN</td><td>保留</td><td>DMAMUXEN</td><td>DMA1EN</td><td>DMA0EN</td><td colspan="5">保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>USBHS0ULPIEN</td><td>USBHS0EN</td><td colspan="10">保留</td><td>ENET1PTPEN</td><td>ENET1RXEN</td><td>ENET1TXEN</td><td>ENET1EN</td></tr></table>

rw rw 

rw rw rw rw 


位/位域



名称



描述


<table><tr><td>31</td><td>保留</td><td>必须保持复位值.</td></tr><tr><td>30</td><td>USBHS1ULPIEN</td><td>USBHS1 ULPI 时钟使能由软件置位或复位0: 关闭 USBHS1 ULPI 时钟1: 开启 USBHS1 ULPI 时钟</td></tr><tr><td>29</td><td>USBH1SEN</td><td>USBHS1 时钟使能由软件置位或复位0: 关闭 USBHS1 时钟1: 开启 USBHS1 时钟</td></tr><tr><td>28</td><td>ENET0PTPEN</td><td>以太网 0 PTP 时钟使能由软件置位或复位0: 关闭以太网 0 PTP 时钟1: 开启以太网 0 PTP 时钟</td></tr><tr><td>27</td><td>ENET0RXEN</td><td>以太网 0 RX 时钟使能由软件置位或复位0: 关闭以太网 0 RX 时钟1: 开启以太网 0 RX 时钟</td></tr><tr><td>26</td><td>ENET0TXEN</td><td>以太网 0 TX 时钟使能由软件置位或复位0: 关闭以太网 0 TX 时钟1: 开启以太网 0 TX 时钟</td></tr><tr><td>25</td><td>ENE0TEN</td><td>以太网 0 时钟使能由软件置位或复位0: 关闭以太网 0 时钟1: 开启以太网 0 时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXEN</td><td>DMAMUX 时钟使能由软件置位或复位0: 关闭 DMAMUX 时钟1: 开启 DMAMUX 时钟</td></tr><tr><td>22</td><td>DMA1EN</td><td>DMA1 时钟使能由软件置位或复位0: 关闭 DMA1 时钟1: 开启 DMA1 时钟</td></tr><tr><td>21</td><td>DMA0EN</td><td>DMA0 时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr><tr><td>20:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>USBHS0ULPIEN</td><td>USBHS0 ULPI时钟使能由软件置位或复位0:关闭USBHS0 ULPI时钟1:开启USBHS0 ULPI时钟</td></tr><tr><td>14</td><td>USBH0SEN</td><td>USBHS0时钟使能由软件置位或复位0:关闭USBHS0时钟1:开启USBHS0时钟</td></tr><tr><td>13:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>ENET1PTPEN</td><td>以太网1PTP时钟使能由软件置位或复位0:关闭以太网1PTP时钟1:开启以太网1PTP时钟</td></tr><tr><td>2</td><td>ENET1RXEN</td><td>以太网1RX时钟使能由软件置位或复位0:关闭以太网1RX时钟1:开启以太网1RX时钟</td></tr><tr><td>1</td><td>ENET1TXEN</td><td>以太网1TX时钟使能由软件置位或复位0:关闭以太网1TX时钟1:开启以太网1TX时钟</td></tr><tr><td>0</td><td>ENE1TEN</td><td>以太网1时钟使能由软件置位或复位0:关闭以太网1时钟1:开启以太网1时钟</td></tr></table>

# 6.3.14. AHB2 使能寄存器（RCU_AHB2EN）

地址偏移：0x34

复位值：0x0000 0100

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>RAMECC</td><td>TMUEN</td><td>TRNGEN</td><td>保留</td><td>HAUEN</td><td>CAUEN</td><td>SDIO1EN</td><td>FACEN</td><td>DCIEN</td></tr><tr><td colspan="7"></td><td>MU1EN</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>RAMECCMU1EN</td><td>RAMECCMU1时钟使能由软件置位或复位0:关闭RAMECCMU1时钟1:开启RAMECCMU1时钟</td></tr><tr><td>7</td><td>TMUEN</td><td>TMU时钟使能由软件置位或复位0:关闭TMU时钟1:开启TMU时钟</td></tr><tr><td>6</td><td>TRNGEN</td><td>TRNG时钟使能由软件置位或复位0:关闭TRNG时钟1:开启TRNG时钟</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>HAUEN</td><td>HAU时钟使能由软件置位或复位0:关闭HAU时钟1:开启HAU时钟</td></tr><tr><td>3</td><td>CAUEN</td><td>CAU时钟使能由软件置位或复位0:关闭CAU时钟1:开启CAU时钟</td></tr><tr><td>2</td><td>SDIO1EN</td><td>SDIO1时钟使能由软件置位或复位0:关闭SDIO1时钟1:开启SDIO1时钟</td></tr><tr><td>1</td><td>FACEN</td><td>FAC时钟使能由软件置位或复位0:关闭FAC时钟1:开启FAC时钟</td></tr><tr><td>0</td><td>DCIEN</td><td>DCI时钟使能由软件置位或复位0:关闭DCI时钟1:开启DCI时钟</td></tr></table>

# 6.3.15. AHB3 使能寄存器（RCU_AHB3EN）

地址偏移：0x38

复位值：0x0000 8400

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CPUEN</td><td colspan="4">保留</td><td>RAMECC MU0EN</td><td>RTDEC1 EN</td><td>RTDEC0 EN</td><td>保留</td><td>OSPI1EN</td><td>OSPI0EN</td><td>OSPIME N</td><td>MDMAEN</td><td>SDIO0EN</td><td>IPAEN</td><td>EXMCEN</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CPUEN</td><td>CPU时钟使能由软件置位或复位0:关闭CPU时钟1:开启CPU时钟</td></tr><tr><td>14:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>RAMECCMU0EN</td><td>RAMECCMU0时钟使能由软件置位或复位0:关闭RAMECCMU0时钟1:开启RAMECCMU0时钟</td></tr><tr><td>9</td><td>RTDEC1EN</td><td>RTDEC1时钟使能由软件置位或复位0:关闭RTDEC1时钟1:开启RTDEC1时钟</td></tr><tr><td>8</td><td>RTDEC0EN</td><td>RTDEC0时钟使能由软件置位或复位0:关闭RTDEC0时钟1:开启RTDEC0时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>OSPI1EN</td><td>OSPI1时钟使能由软件置位或复位0:关闭OSPI1时钟1:开启OSPI1时钟</td></tr><tr><td>5</td><td>OSPI0EN</td><td>OSPI0时钟使能由软件置位或复位0:关闭OSPI0时钟</td></tr></table>

1：开启 OSPI0 时钟

4 OSPIMEN 

OSPIM 时钟使能

由软件置位或复位

0：关闭 OSPIM 时钟

1：开启 OSPIM 时钟

3 MDMAEN 

MDMA 时钟使能

由软件置位或复位

0：关闭 MDMA 时钟

1：开启 MDMA 时钟

2 SDIO0EN 

SDIO0 时钟使能

由软件置位或复位

0：关闭 SDIO0 时钟

1：开启 SDIO0 时钟

1 IPAEN 

IPAEN 时钟使能

由软件置位或复位

0：关闭 IPAEN 时钟

1：开启 IPAEN 时钟

0 EXMCEN 

EXMC 时钟使能

由软件置位或复位

0：关闭 EXMC 时钟

1：开启 EXMC 时钟

# 6.3.16. AHB4 使能寄存器（RCU_AHB4EN）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>HWSEME N</td><td>CRCEN</td><td>BKPSRA MEN</td><td colspan="3">保留</td><td>PKEN</td><td>PJEN</td><td>PHEN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

位/位域 名称

描述

31:16 保留

必须保持复位值。

15 HWSEMEN 

HWSEM 时钟使能

由软件置位或复位

0：关闭 HWSEM 时钟

1：开启 HWSEM 时钟

14 

CRCEN 

CRC 时钟使能

由软件置位或复位

0：关闭 CRC 时钟

1：开启 CRC 时钟

13 

BKPSRAMEN 

BKPSRAM 时钟使能

由软件置位或复位

0：关闭 BKPSRAM 时钟

1：开启 BKPSRAM 时钟

12:10 

保留

必须保持复位值。

9 

PKEN 

GPIO 端口 K 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 K 时钟

1：开启 GPIO 端口 K 时钟

8 

PJEN 

GPIO 端口 J 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 J 时钟

1：开启 GPIO 端口 J 时钟

7 

PHEN 

GPIO 端口 H 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 H 时钟

1：开启 GPIO 端口 H 时钟

6 

PGEN 

GPIO 端口 G时钟使能

由软件置位或复位

0：关闭 GPIO 端口 G 时钟

1：开启 GPIO 端口 G 时钟

5 

PFEN 

GPIO 端口 F 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 F 时钟

1：开启 GPIO 端口 F 时钟

4 

PEEN 

GPIO 端口 E 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 E 时钟

1：开启 GPIO 端口 E 时钟

3 

PDEN 

GPIO 端口 D 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 D 时钟

1：开启 GPIO 端口 D 时钟

PCEN 

GPIO 端口 C 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 C 时钟

1：开启 GPIO 端口 C 时钟

1 PBEN GPIO 端口 B 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 B 时钟

1：开启 GPIO 端口 B 时钟

0 PAEN GPIO 端口 A 时钟使能

由软件置位或复位

0：关闭 GPIO 端口 A 时钟

1：开启 GPIO 端口 A 时钟

# 6.3.17. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x40

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7EN</td><td>UART6EN</td><td>DACEN</td><td>DACHOLDEN</td><td>CTCEN</td><td colspan="2">保留</td><td>I2C3EN</td><td>I2C2EN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>MDIOEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td>RSPDIFEN</td><td>保留</td><td>TIMER51EN</td><td>TIMER50EN</td><td>TIMER31EN</td><td>TIMER30EN</td><td>TIMER23EN</td><td>TIMER22EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>UART7EN</td><td>UART7 时钟使能由软件置位或复位0: 关闭 UART7 时钟1: 开启 UART7 时钟</td></tr><tr><td>30</td><td>UART6EN</td><td>UART6 时钟使能由软件置位或复位0: 关闭 UART6 时钟1: 开启 UART6 时钟</td></tr><tr><td>29</td><td>DACEN</td><td>DAC 时钟使能由软件置位或复位0: 关闭 DAC 时钟1: 开启 DAC 时钟</td></tr><tr><td>28</td><td>DACHOLDEN</td><td>DAC 保持时钟使能由软件置位或复位,DAC 保持时钟源为 IRC32K</td></tr></table>

0：关闭 DAC保持时钟

1：开启 DAC保持时钟

27 CTCEN CTC 保持时钟使能

由软件置位或复位

0：关闭 CTC 保持时钟

1：开启 CTC 保持时钟

26:25 保留 必须保持复位值。

24 I2C3EN I2C3 时钟使能

由软件置位或复位

0：关闭 I2C3 时钟

1：开启 I2C3 时钟

23 I2C2EN I2C2 时钟使能

由软件置位或复位

0：关闭 I2C2 时钟

1：开启 I2C2 时钟

22 I2C1EN I2C1 时钟使能

由软件置位或复位

0：关闭 I2C1 时钟

1：开启 I2C1 时钟

21 I2C0EN I2C0 时钟使能

由软件置位或复位

0：关闭 I2C0 时钟

1：开启 I2C0 时钟

20 UART4EN UART4 时钟使能

由软件置位或复位

0：关闭 UART4 时钟

1：开启 UART4 时钟

19 UART3EN UART3 时钟使能

由软件置位或复位

0：关闭 UART3 时钟

1：开启 UART3 时钟

18 USART2EN USART2 时钟使能

由软件置位或复位

0：关闭 USART2 时钟

1：开启 USART2 时钟

17 USART1EN USART1 时钟使能

由软件置位或复位

0：关闭 USART1 时钟

1：开启 USART1 时钟

<table><tr><td>16</td><td>MDIOEN</td><td>MDIO时钟使能由软件置位或复位0:关闭MDIO时钟1:开启MDIO时钟</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13</td><td>RSPDIFEN</td><td>RSPDIF时钟使能由软件置位或复位0:关闭RSPDIF时钟1:开启RSPDIF时钟</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>TIMER51EN</td><td>TIMER51时钟使能由软件置位或复位0:关闭TIMER51时钟1:开启TIMER51时钟</td></tr><tr><td>10</td><td>TIMER51EN</td><td>TIMER51时钟使能由软件置位或复位0:关闭TIMER51时钟1:开启TIMER51时钟</td></tr><tr><td>9</td><td>TIMER31EN</td><td>TIMER31时钟使能由软件置位或复位0:关闭TIMER31时钟1:开启TIMER31时钟</td></tr><tr><td>8</td><td>TIMER30EN</td><td>TIMER30时钟使能由软件置位或复位0:关闭TIMER30时钟1:开启TIMER30时钟</td></tr><tr><td>7</td><td>TIMER23EN</td><td>TIMER23时钟使能由软件置位或复位0:关闭TIMER23时钟1:开启TIMER23时钟</td></tr><tr><td>6</td><td>TIMER22EN</td><td>TIMER22时钟使能由软件置位或复位0: 关闭 TIMER22 时钟1: 开启 TIMER22 时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6 时钟使能由软件置位或复位0: 关闭 TIMER6 时钟1: 开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5 时钟使能由软件置位或复位0: 关闭 TIMER5 时钟1: 开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4 时钟使能由软件置位或复位0: 关闭 TIMER4 时钟1: 开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3 时钟使能由软件置位或复位0: 关闭 TIMER3 时钟1: 开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2 时钟使能由软件置位或复位0: 关闭 TIMER2 时钟1: 开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1 时钟使能由软件置位或复位0: 关闭 TIMER1 时钟1: 开启 TIMER1 时钟</td></tr></table>

# 6.3.18. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x44

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRIGSEL EN</td><td>EDOUTEN</td><td>TIMER44EN</td><td>TIMER43EN</td><td>TIMER42EN</td><td>TIMER41EN</td><td>TIMER40EN</td><td>SAI2EN</td><td>SAI1EN</td><td>SAI0EN</td><td>SPI5EN</td><td>SPI4EN</td><td>HPDFEN</td><td>TIMER16EN</td><td>TIMER15EN</td><td>TIMER14EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SPI3EN</td><td>SPI0EN</td><td>保留</td><td>ADC2EN</td><td>ADC1EN</td><td>ADC0EN</td><td colspan="2">保留</td><td>USART5EN</td><td>USART0EN</td><td colspan="2">保留</td><td>TIMER7EN</td><td>TIMER0EN</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRIGSELEN</td><td>TRIGSEL时钟使能由软件置位或复位0:关闭 TRIGSEL 时钟1:开启 TRIGSEL 时钟</td></tr><tr><td>30</td><td>EDOUTEN</td><td>EDOUT时钟使能由软件置位或复位0:关闭 EDOUT 时钟1:开启 EDOUT 时钟</td></tr><tr><td>29</td><td>TIMER44EN</td><td>TIMER44时钟使能由软件置位或复位0:关闭 TIMER44 时钟1:开启 TIMER44 时钟</td></tr><tr><td>28</td><td>TIMER43EN</td><td>TIMER43时钟使能由软件置位或复位0:关闭 TIMER43 时钟1:开启 TIMER43 时钟</td></tr><tr><td>27</td><td>TIMER42EN</td><td>TIMER42时钟使能由软件置位或复位0:关闭 TIMER42 时钟1:开启 TIMER42 时钟</td></tr><tr><td>26</td><td>TIMER41EN</td><td>TIMER41时钟使能由软件置位或复位0:关闭 TIMER41 时钟1:开启 TIMER41 时钟</td></tr><tr><td>25</td><td>TIMER40EN</td><td>TIMER40时钟使能由软件置位或复位0:关闭 TIMER40 时钟1:开启 TIMER40 时钟</td></tr><tr><td>24</td><td>SAI2EN</td><td>SAI2时钟使能由软件置位或复位0:关闭 SAI2 时钟1:开启 SAI2 时钟</td></tr><tr><td>23</td><td>SAI1EN</td><td>SAI1时钟使能由软件置位或复位0:关闭 SAI1 时钟1:开启 SAI1 时钟</td></tr><tr><td>22</td><td>SAI0EN</td><td>SAI0时钟使能由软件置位或复位0:关闭 SAI0 时钟</td></tr></table>

1：开启 SAI0 时钟

21 SPI5EN SPI5 时钟使能

由软件置位或复位

0：关闭 SPI5 时钟

1：开启 SPI5 时钟

20 SPI4EN SPI4 时钟使能

由软件置位或复位

0：关闭 SPI4 时钟

1：开启 SPI4 时钟

19 HPDFEN HPDF 时钟使能

由软件置位或复位

0：关闭 HPDF 时钟

1：开启 HPDF 时钟

18 TIMER16EN TIMER16 时钟使能

由软件置位或复位

0：关闭 TIMER16 时钟

1：开启 TIMER16 时钟

17 TIMER15EN TIMER15 时钟使能

由软件置位或复位

0：关闭 TIMER15 时钟

1：开启 TIMER15 时钟

16 TIMER14EN TIMER14 时钟使能

由软件置位或复位

0：关闭 TIMER14 时钟

1：开启 TIMER14 时钟

15:14 保留 必须保持复位值。

13 SPI3EN SPI3 时钟使能

由软件置位或复位

0：关闭 SPI3 时钟

1：开启 SPI3 时钟

12 SPI0EN SPI0 时钟使能

由软件置位或复位

0：关闭 SPI0 时钟

1：开启 SPI0 时钟

11 保留 必须保持复位值。

10 ADC2EN ADC2 时钟使能

由软件置位或复位

0：关闭 ADC2 时钟

<table><tr><td></td><td></td><td>1:开启ADC2时钟</td></tr><tr><td>9</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>8</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5EN</td><td>USART5时钟使能由软件置位或复位0:关闭USART5时钟1:开启USART5时钟</td></tr><tr><td>4</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER7EN</td><td>TIMER7时钟使能由软件置位或复位0:关闭TIMER7时钟1:开启TIMER7时钟</td></tr><tr><td>0</td><td>TIMER0EN</td><td>TIMER0时钟使能由软件置位或复位0:关闭TIMER0时钟1:开启TIMER0时钟</td></tr></table>

# 6.3.19. APB3 使能寄存器（RCU_APB3EN）

地址偏移：0x48

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>WWDGTEN</td><td>TLIEN</td></tr></table>

rw rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>0</td><td>TLIEN</td><td>TLI时钟使能由软件置位或复位0:关闭TLI时钟1:开启TLI时钟</td></tr></table>

# 6.3.20. APB4 使能寄存器（RCU_APB4EN）

地址偏移：0x4C

复位值：0x0000 0010

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>PMUEN</td><td>LPDTSEN</td><td>VREFEN</td><td>CMPEN</td><td>SYSCFGEN</td></tr><tr><td colspan="11"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>4</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>3</td><td>LPDTSEN</td><td>LPDTS时钟使能由软件置位或复位0:关闭LPDTS时钟1:开启LPDTS时钟</td></tr><tr><td>2</td><td>VREFEN</td><td>VREF时钟使能由软件置位或复位0:关闭VREF时钟1:开启VREF时钟</td></tr></table>

<table><tr><td>1</td><td>CMPEN</td><td>CMP 时钟使能由软件置位或复位0: 关闭 CMP 时钟1: 开启 CMP 时钟</td></tr><tr><td>0</td><td>SYSCFGEN</td><td>SYSCFG 时钟使能由软件置位或复位0: 关闭 SYSCFG 时钟1: 开启 SYSCFG 时钟</td></tr></table>

# 6.3.21. AHB1 睡眠模式使能寄存器（RCU_AHB1SPEN）

地址偏移：0x50

复位值：0x7EE3 C00F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>USBHS1 ULPISPEN</td><td>USBHS1 SPEN</td><td>ENETOPT PSPEN</td><td>ENETOR XSPEN</td><td>ENETOTX SPEN</td><td>ENETOS PEN</td><td>保留</td><td>DMAMUX SPEN</td><td>DMA1SP EN</td><td>DMA0SP EN</td><td colspan="3">保留</td><td>SRAM1S PEN</td><td>SRAM0SP EN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>USBHS0 ULPISPEN</td><td>USBHS0SPEN</td><td colspan="10">保留</td><td>ENET1PT PSPEN</td><td>ENET1R XSPEN</td><td>ENET1TX SPEN</td><td>ENET1S PEN</td></tr><tr><td>rw</td><td>rw</td><td colspan="10"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>USBHS1ULPISPEN</td><td>在睡眠模式下 USBHS1 ULPI 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USBHS1 ULPI 时钟1: 在睡眠模式下开启 USBHS1 ULPI 时钟</td></tr><tr><td>29</td><td>USBHS1SPEN</td><td>在睡眠模式下 USBHS1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USBHS1 时钟1: 在睡眠模式下开启 USBHS1 时钟</td></tr><tr><td>28</td><td>ENET0PTPSPEN</td><td>在睡眠模式下以太网 0 PTP 时钟使能由软件置位或复位0: 在睡眠模式下关闭以太网 0 PTP 时钟1: 在睡眠模式下开启以太网 0 PTP 时钟</td></tr><tr><td>27</td><td>ENET0RXSPEN</td><td>在睡眠模式下以太网 0 RX 时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:在睡眠模式下关闭以太网0RX时钟1:在睡眠模式下开启以太网0RX时钟</td></tr><tr><td>26</td><td>ENET0TXSPEN</td><td>在睡眠模式下以太网0TX时钟使能由软件置位或复位0:在睡眠模式下关闭以太网0TX时钟1:在睡眠模式下开启以太网0TX时钟</td></tr><tr><td>25</td><td>ENET0SPEN</td><td>在睡眠模式下以太网0时钟使能由软件置位或复位0:在睡眠模式下关闭以太网0时钟1:在睡眠模式下开启以太网0时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXSPEN</td><td>在睡眠模式下DMAMUX时钟使能由软件置位或复位0:在睡眠模式下关闭DMAMUX时钟1:在睡眠模式下开启DMAMUX时钟</td></tr><tr><td>22</td><td>DMA1SPEN</td><td>在睡眠模式下DMA1时钟使能由软件置位或复位0:在睡眠模式下关闭DMA1时钟1:在睡眠模式下开启DMA1时钟</td></tr><tr><td>21</td><td>DMA0SPEN</td><td>在睡眠模式下DMA0时钟使能由软件置位或复位0:在睡眠模式下关闭DMA0时钟1:在睡眠模式下开启DMA0时钟</td></tr><tr><td>20:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SRAM1SPEN</td><td>在睡眠模式下SRAM1时钟使能由软件置位或复位0:在睡眠模式下关闭SRAM1时钟1:在睡眠模式下开启SRAM1时钟</td></tr><tr><td>16</td><td>SRAM0SPEN</td><td>在睡眠模式下SRAM0时钟使能由软件置位或复位0:在睡眠模式下关闭SRAM0时钟1:在睡眠模式下开启SRAM0时钟</td></tr><tr><td>15</td><td>USBHS0ULPISPEN</td><td>在睡眠模式下USBHS0ULPI时钟使能由软件置位或复位0:在睡眠模式下关闭USBHS0ULPI时钟1:在睡眠模式下开启USBHS0ULPI时钟</td></tr><tr><td>14</td><td>USBHS0SPEN</td><td>在睡眠模式下USBHS0时钟使能由软件置位或复位0:在睡眠模式下关闭USBHS0时钟1:在睡眠模式下开启USBHS0时钟</td></tr><tr><td>13:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>ENET1PTPSPEN</td><td>在睡眠模式下以太网1 PTP时钟使能由软件置位或复位0:在睡眠模式下关闭以太网1 PTP时钟1:在睡眠模式下开启以太网1 PTP时钟</td></tr><tr><td>2</td><td>ENET1RXSPEN</td><td>在睡眠模式下以太网1 RX时钟使能由软件置位或复位0:在睡眠模式下关闭以太网1 RX时钟1:在睡眠模式下开启以太网1 RX时钟</td></tr><tr><td>1</td><td>ENET1TXSPEN</td><td>在睡眠模式下以太网1 TX时钟使能由软件置位或复位0:在睡眠模式下关闭以太网1 TX时钟1:在睡眠模式下开启以太网1 TX时钟</td></tr><tr><td>0</td><td>ENET1SPEN</td><td>在睡眠模式下以太网1时钟使能由软件置位或复位0:在睡眠模式下关闭以太网1时钟1:在睡眠模式下开启以太网1时钟</td></tr></table>

# 6.3.22. AHB2 睡眠模式使能寄存器（RCU_AHB2SPEN）

地址偏移：0x54

复位值：0x0000 01DF

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>RAMECC MU1SPEN</td><td>TMUSPEN</td><td>TRNGSPEN</td><td>保留</td><td>HAUSPEN</td><td>CAUSPEN</td><td>SDIO1SPEN</td><td>FACSPEN</td><td>DCISPEN</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>RAMECCMU1SPEN</td><td>在睡眠模式下 RAMECCMU1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 RAMECCMU1 时钟1: 在睡眠模式下开启 RAMECCMU1 时钟</td></tr><tr><td>7</td><td>TMUSPEN</td><td>在睡眠模式下 TMU 时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:在睡眠模式下关闭TMU时钟1:在睡眠模式下开启TMU时钟</td></tr><tr><td>6</td><td>TRNGSPEN</td><td>在睡眠模式下TRNG时钟使能由软件置位或复位0:在睡眠模式下关闭TRNG时钟1:在睡眠模式下开启TRNG时钟</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>HAUSPEN</td><td>在睡眠模式下HAU时钟使能由软件置位或复位0:在睡眠模式下关闭HAU时钟1:在睡眠模式下开启HAU时钟</td></tr><tr><td>3</td><td>CAUSPEN</td><td>在睡眠模式下CAU时钟使能由软件置位或复位0:在睡眠模式下关闭CAU时钟1:在睡眠模式下开启CAU时钟</td></tr><tr><td>2</td><td>SDIO1SPEN</td><td>在睡眠模式下SDIO1时钟使能由软件置位或复位0:在睡眠模式下关闭SDIO1时钟1:在睡眠模式下开启SDIO1时钟</td></tr><tr><td>1</td><td>FACSPEN</td><td>在睡眠模式下FAC时钟使能由软件置位或复位0:在睡眠模式下关闭FAC时钟1:在睡眠模式下开启FAC时钟</td></tr><tr><td>0</td><td>DCISPEN</td><td>在睡眠模式下DCI时钟使能由软件置位或复位0:在睡眠模式下关闭DCI时钟1:在睡眠模式下开启DCI时钟</td></tr></table>

# 6.3.23. AHB3 睡眠模式使能寄存器（RCU_AHB3SPEN）

地址偏移：0x58

复位值：0x0000 C77F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FMCSPEN</td><td>AXISRAMSPEN</td><td colspan="3">保留</td><td>RAMECCMU0SPEN</td><td>RTDEC1SPEN</td><td>RTDEC0SPEN</td><td>保留</td><td>OSPI1SPEN</td><td>OSPI0SPEN</td><td>OSPIMSPEN</td><td>MDMASPEN</td><td>SDIO0SPEN</td><td>IPASPEN</td><td>EXMCSPEN</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>FMCSPEN</td><td>在睡眠模式下 FMC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 FMC 时钟1: 在睡眠模式下开启 FMC 时钟</td></tr><tr><td>14</td><td>AXISRAMSPEN</td><td>在睡眠模式下 AXI SRAM 时钟使能由软件置位或复位0: 在睡眠模式下关闭 AXI SRAM 时钟1: 在睡眠模式下开启 AXI SRAM 时钟</td></tr><tr><td>13:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>RAMECCMU0SPEN</td><td>在睡眠模式下 RAMECCMU0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 RAMECCMU0 时钟1: 在睡眠模式下开启 RAMECCMU0 时钟</td></tr><tr><td>9</td><td>RTDEC1SPEN</td><td>在睡眠模式下 RTDEC1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 RTDEC1 时钟1: 在睡眠模式下开启 RTDEC1 时钟</td></tr><tr><td>8</td><td>RTDEC0SPEN</td><td>在睡眠模式下 RTDEC0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 RTDEC0 时钟1: 在睡眠模式下开启 RTDEC0 时钟</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>OSPI1SPEN</td><td>在睡眠模式下 OSPI1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 OSPI1 时钟1: 在睡眠模式下开启 OSPI1 时钟</td></tr><tr><td>5</td><td>OSPI0SPEN</td><td>在睡眠模式下 OSPI0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 OSPI0 时钟1: 在睡眠模式下开启 OSPI0 时钟</td></tr><tr><td>4</td><td>OSPIMSPEN</td><td>在睡眠模式下 OSPIM 时钟使能由软件置位或复位0: 在睡眠模式下关闭 OSPIM 时钟1: 在睡眠模式下开启 OSPIM 时钟</td></tr><tr><td>3</td><td>MDMASPEN</td><td>在睡眠模式下 MDMA 时钟使能由软件置位或复位</td></tr></table>

0：在睡眠模式下关闭 MDMA时钟

1：在睡眠模式下开启 MDMA时钟

<table><tr><td>2</td><td>SDIO0SPEN</td><td>在睡眠模式下 SDIO0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SDIO0 时钟1: 在睡眠模式下开启 SDIO0 时钟</td></tr><tr><td>1</td><td>IPASPEN</td><td>在睡眠模式下 IPA 时钟使能由软件置位或复位0: 在睡眠模式下关闭 IPA 时钟1: 在睡眠模式下开启 IPA 时钟</td></tr><tr><td>0</td><td>EXMCSPEN</td><td>在睡眠模式下 EXMC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 EXMC 时钟1: 在睡眠模式下开启 EXMC 时钟</td></tr></table>

# 6.3.24. AHB4 睡眠模式使能寄存器（RCU_AHB4SPEN）

地址偏移：0x5C

复位值：0x0000 63FF

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>CRCSPEN</td><td>BKPSRAM SPEN</td><td colspan="3">保留</td><td>PKSPEN</td><td>PJSPEN</td><td>PHSPEN</td><td>PGSPEN</td><td>PFSPEN</td><td>PESPEN</td><td>PDSPEN</td><td>PCSPEN</td><td>PBSPEN</td><td>PASPEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>CRCSPEN</td><td>在睡眠模式下 CRC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 CRC 时钟1: 在睡眠模式下开启 CRC 时钟</td></tr><tr><td>13</td><td>BKPSRAMSPEN</td><td>在睡眠模式下备份域 SRAM 时钟使能由软件置位或复位0: 在睡眠模式下关闭备份域 SRAM 时钟1: 在睡眠模式下开启备份域 SRAM 时钟</td></tr><tr><td>12:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>PKSPEN</td><td>在睡眠模式下 GPIO 端口 K 时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 K 时钟1:在睡眠模式下开启 GPIO 端口 K 时钟</td></tr><tr><td>8</td><td>PJSPEN</td><td>在睡眠模式下 GPIO 端口 J 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 J 时钟1:在睡眠模式下开启 GPIO 端口 J 时钟</td></tr><tr><td>7</td><td>PHSPEN</td><td>在睡眠模式下 GPIO 端口 H 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 H 时钟1:在睡眠模式下开启 GPIO 端口 H 时钟</td></tr><tr><td>6</td><td>PGSPEN</td><td>在睡眠模式下 GPIO 端口 G 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 G 时钟1:在睡眠模式下开启 GPIO 端口 G 时钟</td></tr><tr><td>5</td><td>PFSPEN</td><td>在睡眠模式下 GPIO 端口 F 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 F 时钟1:在睡眠模式下开启 GPIO 端口 F 时钟</td></tr><tr><td>4</td><td>PEEN</td><td>在睡眠模式下 GPIO 端口 E 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 E 时钟1:在睡眠模式下开启 GPIO 端口 E 时钟</td></tr><tr><td>3</td><td>PDSPEN</td><td>在睡眠模式下 GPIO 端口 D 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 D 时钟1:在睡眠模式下开启 GPIO 端口 D 时钟</td></tr><tr><td>2</td><td>PCSPEN</td><td>在睡眠模式下 GPIO 端口 C 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 C 时钟1:在睡眠模式下开启 GPIO 端口 C 时钟</td></tr><tr><td>1</td><td>PBSPEN</td><td>在睡眠模式下 GPIO 端口 B 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 B 时钟1:在睡眠模式下开启 GPIO 端口 B 时钟</td></tr><tr><td>0</td><td>PASPEN</td><td>在睡眠模式下 GPIO 端口 A 时钟使能由软件置位或复位0:在睡眠模式下关闭 GPIO 端口 A 时钟1:在睡眠模式下开启 GPIO 端口 A 时钟</td></tr></table>

# 6.3.25. APB1 睡眠模式使能寄存器（RCU_APB1SPEN）

地址偏移：0x60

复位值：0xF9FF EFFF

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7SPEN</td><td>UART6SPEN</td><td>DACSPEN</td><td>DACHOLDSPEN</td><td>CTCSPEN</td><td colspan="2">保留</td><td>I2C3SPEN</td><td>I2C2SPEN</td><td>I2C1SPEN</td><td>I2C0SPEN</td><td>UART4SPEN</td><td>UART3SPEN</td><td>USART2SPEN</td><td>USART1SPEN</td><td>MDIOSPEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2SPEN</td><td>SPI1SPEN</td><td>RSPDIFSPEN</td><td>保留</td><td>TIMER51SPEN</td><td>TIMER50SPEN</td><td>TIMER31SPEN</td><td>TIMER30SPEN</td><td>TIMER23SPEN</td><td>TIMER22SPEN</td><td>TIMER6SPEN</td><td>TIMER5SPEN</td><td>TIMER4SPEN</td><td>TIMER3SPEN</td><td>TIMER2SPEN</td><td>TIMER1SPEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UART7SPEN</td><td>在睡眠模式下 UART7 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART7 时钟1: 在睡眠模式下开启 UART7 时钟</td></tr><tr><td>30</td><td>UART6SPEN</td><td>在睡眠模式下 UART6 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART6 时钟1: 在睡眠模式下开启 UART6 时钟</td></tr><tr><td>29</td><td>DACSPEN</td><td>在睡眠模式下 DAC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 DAC 时钟1: 在睡眠模式下开启 DAC 时钟</td></tr><tr><td>28</td><td>DACHOLDSPEN</td><td>在睡眠模式下 DAC 保持时钟使能由软件置位或复位,DAC 保持时钟源为 IRC32K0: 在睡眠模式下关闭 DAC 保持时钟1: 在睡眠模式下开启 DAC 保持时钟</td></tr><tr><td>27</td><td>CTCSPEN</td><td>在睡眠模式下 CTC 保持时钟使能由软件置位或复位0: 在睡眠模式下关闭 CTC 保持时钟1: 在睡眠模式下开启 CTC 保持时钟</td></tr><tr><td>26:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3SPEN</td><td>在睡眠模式下 I2C3 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C3 时钟1: 在睡眠模式下开启 I2C3 时钟</td></tr></table>

<table><tr><td>23</td><td>I2C2SPEN</td><td>在睡眠模式下 I2C2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C2 时钟1: 在睡眠模式下开启 I2C2 时钟</td></tr><tr><td>22</td><td>I2C1SPEN</td><td>在睡眠模式下 I2C1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C1 时钟1: 在睡眠模式下开启 I2C1 时钟</td></tr><tr><td>21</td><td>I2C0SPEN</td><td>在睡眠模式下 I2C0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C0 时钟1: 在睡眠模式下开启 I2C0 时钟</td></tr><tr><td>20</td><td>UART4SPEN</td><td>在睡眠模式下 UART4 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART4 时钟1: 在睡眠模式下开启 UART4 时钟</td></tr><tr><td>19</td><td>UART3SPEN</td><td>在睡眠模式下 UART3 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART3 时钟1: 在睡眠模式下开启 UART3 时钟</td></tr><tr><td>18</td><td>USART2SPEN</td><td>在睡眠模式下 USART2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART2 时钟1: 在睡眠模式下开启 USART2 时钟</td></tr><tr><td>17</td><td>USART1SPEN</td><td>在睡眠模式下 USART1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART1 时钟1: 在睡眠模式下开启 USART1 时钟</td></tr><tr><td>16</td><td>MDIOSPEN</td><td>在睡眠模式下 MDIO 时钟使能由软件置位或复位0: 在睡眠模式下关闭 MDIO 时钟1: 在睡眠模式下开启 MDIO 时钟</td></tr><tr><td>15</td><td>SPI2SPEN</td><td>在睡眠模式下 SPI2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI2 时钟1: 在睡眠模式下开启 SPI2 时钟</td></tr><tr><td>14</td><td>SPI1SPEN</td><td>在睡眠模式下 SPI1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI1 时钟1:在睡眠模式下开启SPI1时钟</td></tr><tr><td>13</td><td>RSPDIFSPEN</td><td>在睡眠模式下RSPDIF时钟使能由软件置位或复位0:在睡眠模式下关闭RSPDIF时钟1:在睡眠模式下开启RSPDIF时钟</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>TIMER51SPEN</td><td>在睡眠模式下TIMER51时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER51时钟1:在睡眠模式下开启TIMER51时钟</td></tr><tr><td>10</td><td>TIMER50SPEN</td><td>在睡眠模式下TIMER50时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER50时钟1:在睡眠模式下开启TIMER50时钟</td></tr><tr><td>9</td><td>TIMER31SPEN</td><td>在睡眠模式下TIMER31时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER31时钟1:在睡眠模式下开启TIMER31时钟</td></tr><tr><td>8</td><td>TIMER30SPEN</td><td>在睡眠模式下TIMER30时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER30时钟1:在睡眠模式下开启TIMER30时钟</td></tr><tr><td>7</td><td>TIMER23SPEN</td><td>在睡眠模式下TIMER23时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER23时钟1:在睡眠模式下开启TIMER23时钟</td></tr><tr><td>6</td><td>TIMER22SPEN</td><td>在睡眠模式下TIMER22时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER22时钟1:在睡眠模式下开启TIMER22时钟</td></tr><tr><td>5</td><td>TIMER6SPEN</td><td>在睡眠模式下TIMER6时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER6时钟1:在睡眠模式下开启TIMER6时钟</td></tr><tr><td>4</td><td>TIMER5SPEN</td><td>在睡眠模式下TIMER5时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER5时钟1:在睡眠模式下开启TIMER5时钟</td></tr><tr><td>3</td><td>TIMER4SPEN</td><td>在睡眠模式下TIMER4时钟使能</td></tr></table>

由软件置位或复位

0：在睡眠模式下关闭 TIMER4 时钟

1：在睡眠模式下开启 TIMER4 时钟

2 TIMER3SPEN 

在睡眠模式下TIMER3时钟使能由软件置位或复位

0：在睡眠模式下关闭 TIMER3 时钟

1：在睡眠模式下开启 TIMER3 时钟

1 TIMER2SPEN 

在睡眠模式下TIMER2时钟使能由软件置位或复位

0：在睡眠模式下关闭 TIMER2 时钟

1：在睡眠模式下开启 TIMER2 时钟

0 TIMER1SPEN 

在睡眠模式下TIMER1时钟使能由软件置位或复位

0：在睡眠模式下关闭 TIMER1 时钟

1：在睡眠模式下开启 TIMER1 时钟

# 6.3.26. APB2 睡眠模式使能寄存器（RCU_APB2SPEN）

地址偏移：0x64

复位值：0xFFFF 3733

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRIGSELSPEN</td><td>EDOUTSPEN</td><td>TIMER44SPEN</td><td>TIMER43SPEN</td><td>TIMER42SPEN</td><td>TIMER41SPEN</td><td>TIMER40SPEN</td><td>SAI2SPEN</td><td>SAI1SPEN</td><td>SAI0SPEN</td><td>SPI5SPEN</td><td>SPI4SPEN</td><td>HPDFSPEN</td><td>TIMER16SPEN</td><td>TIMER15SPEN</td><td>TIMER14SPEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SPI3SPEN</td><td>SPI0SPEN</td><td>保留</td><td>ADC2SPEN</td><td>ADC1SPEN</td><td>ADC0SPEN</td><td colspan="2">保留</td><td>USART5SPEN</td><td>USART0SPEN</td><td colspan="2">保留</td><td>TIMER7SPEN</td><td>TIMER0SPEN</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>TRIGSELSPEN</td><td>在睡眠模式下 TRIGSEL 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TRIGSEL 时钟1: 在睡眠模式下开启 TRIGSEL 时钟</td></tr><tr><td>30</td><td>EDOUTSPEN</td><td>在睡眠模式下 EDOUT 时钟使能由软件置位或复位0: 在睡眠模式下关闭 EDOUT 时钟1: 在睡眠模式下开启 EDOUT 时钟</td></tr><tr><td>29</td><td>TIMER44SPEN</td><td>在睡眠模式下 TIMER44 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER44 时钟1:在睡眠模式下开启 TIMER44 时钟</td></tr><tr><td>28</td><td>TIMER43SPEN</td><td>在睡眠模式下 TIMER43 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER43 时钟1:在睡眠模式下开启 TIMER43 时钟</td></tr><tr><td>27</td><td>TIMER42SPEN</td><td>在睡眠模式下 TIMER42 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER42 时钟1:在睡眠模式下开启 TIMER42 时钟</td></tr><tr><td>26</td><td>TIMER41SPEN</td><td>在睡眠模式下 TIMER41 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER41 时钟1:在睡眠模式下开启 TIMER41 时钟</td></tr><tr><td>25</td><td>TIMER40SPEN</td><td>在睡眠模式下 TIMER40 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER40 时钟1:在睡眠模式下开启 TIMER40 时钟</td></tr><tr><td>24</td><td>SAI2SPEN</td><td>在睡眠模式下 SAI2 时钟使能由软件置位或复位0:在睡眠模式下关闭 SAI2 时钟1:在睡眠模式下开启 SAI2 时钟</td></tr><tr><td>23</td><td>SAI1SPEN</td><td>在睡眠模式下 SAI1 时钟使能由软件置位或复位0:在睡眠模式下关闭 SAI1 时钟1:在睡眠模式下开启 SAI1 时钟</td></tr><tr><td>22</td><td>SAI0SPEN</td><td>在睡眠模式下 SAI0 时钟使能由软件置位或复位0:在睡眠模式下关闭 SAI0 时钟1:在睡眠模式下开启 SAI0 时钟</td></tr><tr><td>21</td><td>SPI5SPEN</td><td>在睡眠模式下 SPI5 时钟使能由软件置位或复位0:在睡眠模式下关闭 SPI5 时钟1:在睡眠模式下开启 SPI5 时钟</td></tr><tr><td>20</td><td>SPI4SPEN</td><td>在睡眠模式下 SPI4 时钟使能由软件置位或复位0:在睡眠模式下关闭 SPI4 时钟1:在睡眠模式下开启 SPI4 时钟</td></tr><tr><td>19</td><td>HPDFSPEN</td><td>在睡眠模式下 HPDF 时钟使能由软件置位或复位0:在睡眠模式下关闭HPDF时钟1:在睡眠模式下开启HPDF时钟</td></tr><tr><td>18</td><td>TIMER16SPEN</td><td>在睡眠模式下TIMER16时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER16时钟1:在睡眠模式下开启TIMER16时钟</td></tr><tr><td>17</td><td>TIMER15SPEN</td><td>在睡眠模式下TIMER15时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER15时钟1:在睡眠模式下开启TIMER15时钟</td></tr><tr><td>16</td><td>TIMER14SPEN</td><td>在睡眠模式下TIMER14时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER14时钟1:在睡眠模式下开启TIMER14时钟</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>SPI3SPEN</td><td>在睡眠模式下SPI3时钟使能由软件置位或复位0:在睡眠模式下关闭SPI3时钟1:在睡眠模式下开启SPI3时钟</td></tr><tr><td>12</td><td>SPI0SPEN</td><td>在睡眠模式下SPI0时钟使能由软件置位或复位0:在睡眠模式下关闭SPI0时钟1:在睡眠模式下开启SPI0时钟</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>ADC2SPEN</td><td>在睡眠模式下ADC2时钟使能由软件置位或复位0:在睡眠模式下关闭ADC2时钟1:在睡眠模式下开启ADC2时钟</td></tr><tr><td>9</td><td>ADC1SPEN</td><td>在睡眠模式下ADC1时钟使能由软件置位或复位0:在睡眠模式下关闭ADC1时钟1:在睡眠模式下开启ADC1时钟</td></tr><tr><td>8</td><td>ADC0SPEN</td><td>在睡眠模式下ADC0时钟使能由软件置位或复位0:在睡眠模式下关闭ADC0时钟1:在睡眠模式下开启ADC0时钟</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5SPEN</td><td>在睡眠模式下 USART5 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART5 时钟1: 在睡眠模式下开启 USART5 时钟</td></tr><tr><td>4</td><td>USART0SPEN</td><td>在睡眠模式下 USART0 时钟使能由软件置位或复位0: 关闭在睡眠模式下 USART0 时钟1: 开启在睡眠模式下 USART0 时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER7SPEN</td><td>在睡眠模式下 TIMER7 时钟使能由软件置位或复位0: 关闭在睡眠模式下 TIMER7 时钟1: 开启在睡眠模式下 TIMER7 时钟</td></tr><tr><td>0</td><td>TIMER0SPEN</td><td>在睡眠模式下 TIMER0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TIMER0 时钟1: 在睡眠模式下开启 TIMER0 时钟</td></tr></table>

# 6.3.27. APB3 睡眠模式使能寄存器（RCU_APB3SPEN）

地址偏移：0x68

复位值：0x0000 0003

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>WWDGT SPEN</td><td>TLISPEN</td></tr><tr><td colspan="14"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>WWDGTSPEN</td><td>在睡眠模式下 WWDGT 时钟使能由软件置位或复位0:关闭在睡眠模式下 WWDGT 时钟1:开启在睡眠模式下 WWDGT 时钟</td></tr><tr><td>0</td><td>TLISPEN</td><td>在睡眠模式下 TLI 时钟使能由软件置位或复位0:在睡眠模式下关闭 TLI 时钟</td></tr></table>

1：在睡眠模式下开启 TLI 时钟

# 6.3.28. APB4 睡眠模式使能寄存器（RCU_APB4SPEN）

地址偏移：0x6C

复位值：0x0000 001F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>PMUSPEN</td><td>LPDTSSPEN</td><td>VREFSPEN</td><td>CMPSPEN</td><td>SYSCFGSPEN</td></tr><tr><td colspan="11"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PMUSPEN</td><td>在睡眠模式下 PMU 时钟使能由软件置位或复位0: 在睡眠模式下关闭 PMU 时钟1: 在睡眠模式下开启 PMU 时钟</td></tr><tr><td>3</td><td>LPDTSSPEN</td><td>在睡眠模式下 LPDTS 时钟使能由软件置位或复位0: 关闭在睡眠模式下 LPDTS 时钟1: 开启在睡眠模式下 LPDTS 时钟</td></tr><tr><td>2</td><td>VREFSPEN</td><td>在睡眠模式下 VREF 时钟使能由软件置位或复位0: 关闭在睡眠模式下 VREF 时钟1: 开启在睡眠模式下 VREF 时钟</td></tr><tr><td>1</td><td>CMPSPEN</td><td>在睡眠模式下 CMP 时钟使能由软件置位或复位0: 关闭在睡眠模式下 CMP 时钟1: 开启在睡眠模式下 CMP 时钟</td></tr><tr><td>0</td><td>SYSCFGSPEN</td><td>在睡眠模式下 SYSCFG 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SYSCFG 时钟1: 在睡眠模式下开启 SYSCFG 时钟</td></tr></table>

# 6.3.29. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x70

复位值：0x0000 0018，只能由备份域复位进行复位

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的LXTALEN、LXTALBPS、RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td>保留</td><td>LCKMD</td><td>LCKMEN</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="3">rw</td><td>r</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC32K时钟作为RTC的时钟源11:选择CK_HXTAL/RTCDIV时钟作为RTC的时钟源,请参考RCU_CFG0寄存器的RTCDIV位域。</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>LCKMD</td><td>LXTAL时钟故障检测由硬件置位,当外部32 kHz振荡器(LXTAL)上的时钟安全系统检测到故障。当LCKMEN或LXTALEN关闭时,该位清零。0:LXTAL(32 kHz振荡器)上未检测到故障1:在LXTAL(32 kHz振荡器)上检测到故障</td></tr><tr><td>5</td><td>LCKMEN</td><td>LXTAL时钟监视器使能0:禁止LXTAL时钟监视器</td></tr></table>
