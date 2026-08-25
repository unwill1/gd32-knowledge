## 4.3. RCU 寄存器

RCU 基地址：0x4002 1000

## 4.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 XX83 X表示未定义

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>PLLSTB</td><td>PLLEN</td><td colspan="3">保留</td><td>HXTALSTBRST</td><td>CKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td colspan="6"></td><td>r</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC8MCALIB[7:0]</td><td colspan="5">IRC8MADJ[4:0]</td><td>保留</td><td>IRC8MSTB</td><td>IRC8MEN</td></tr><tr><td colspan="6"></td><td>r</td><td></td><td colspan="3"></td><td>rw</td><td></td><td></td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>HXTALSTBRST</td><td>HXTAL时钟稳定标志位复位由软件置位或复位0:HXTAL时钟稳定标志位不复位1:HXTAL时钟稳定标志位复位</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~48MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~48MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC8M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC8MEN的状态,自动使能IRC8M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位0:高速4~48MHz晶体振荡器被关闭1:高速4~48MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC8MCALIB[7:0]</td><td>内部8MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC8MADJ[4:0]</td><td>内部8MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC8MADJ[4:0]位域的当前值加上IRC8MCALIB[7:0]位域的值。最终调整值应该调整IRC8M到8MHz±1%</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC8MSTB</td><td>IRC8M内部8MHz RC振荡器稳定标志位硬件置‘1’来指示IRC8M振荡器时钟是否稳定待用0:IRC8M振荡器未稳定1:IRC8M振荡器已稳定</td></tr><tr><td>0</td><td>IRC8MEN</td><td>内部8MHz RC振荡器使能软件置位或复位,如果IRC8M时钟做为系统时钟时,该位不能被复位。当从深度睡眠或待机模式返回,或当CKMEN置位同时用作系统时钟的HXTAL振荡器发生故障时,该位由硬件置1来启动IRC8M振荡器。0:内部8MHz RC振荡器被关闭1:内部8MHz RC振荡器被打开</td></tr></table>

## 4.3.2. PLL 寄存器（RCU_PLL）

地址偏移：0x04

复位值：0x0000 0400

配置PLL时钟可参考下列公式：

CK_PLLVCOSRC = CK_PLLSRC / PLLPSC 

CK_PLLVCO = CK_PLLVCOSRC × PLLN 

CK_PLLP = CK_PLLVCO / PLLP 

CK_PLLQ = CK_PLLVCO / PLLQ 

CK_PLLR = CK_PLLVCO / PLLR 

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">PLL[4:0]</td><td colspan="4">PLLQ[3:0]</td><td>PLLSEL</td><td>PLLREN</td><td>PLLQEN</td><td>PLLPEN</td><td>保留</td><td colspan="2">PLLP[1:0]</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="8">PLLN[7:0]</td><td colspan="2">保留</td><td colspan="4">PLLPSC[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>PLL[4:0]</td><td>PLLR 输出频率的分频系数(PLL VCO 时钟做为输入)当 PLL 被关闭时由软件置位或清零。这些位域用做将 PLL VCO 时钟(CK_PLLVCO)分频生成 PLLQ 输出时钟(CK_PLLQ)。RCU_PLL 寄存器的 PLLN 位域对 CK_PLLVCO 时钟进行了描述。00000:保留00001:保留00010: CK_PLLQ = CK_PLLVCO / 200011: CK_PLLQ = CK_PLLVCO / 300100: CK_PLLQ = CK_PLLVCO / 4...11111: CK_PLLQ = CK_PLLVCO / 31</td></tr><tr><td>26:23</td><td>PLL[3:0]</td><td>PLLQ 输出频率的分频系数(PLL VCO 时钟做为输入)当 PLL 被关闭时由软件置位或清零。这些位域用做将 PLL VCO 时钟(CK_PLLVCO)分频生成 PLLQ 输出时钟(CK_PLLQ)。CK_PLLQ 时钟可以被用作 TRNG(48MHz)模块的时钟源。RCU_PLL 寄存器的 PLLN 位域对 CK_PLLVCO 时钟进行了描述。0000:保留0001:保留0010: CK_PLLQ = CK_PLLVCO / 20011: CK_PLLQ = CK_PLLVCO / 30100: CK_PLLQ = CK_PLLVCO / 41111: CK_PLLQ = CK_PLLVCO / 15</td></tr><tr><td>22</td><td>PLLSEL</td><td>PLL时钟源选择由软件置位或复位,控制PLL时钟源0: IRC8M时钟被选择为PLL时钟的时钟源1: HXTAL时钟被选择为PLL时钟的时钟源</td></tr><tr><td>21</td><td>PLLREN</td><td>PLLR 分频器输出使能由软件置位或复位。只有在PLLEN位为0时PLLREN位才可写。0: 禁止CK_PLLR输出1: 使能CK_PLLR输出</td></tr><tr><td>20</td><td>PLLQEN</td><td>PLLQ 分频器输出使能由软件置位或复位。只有在PLLEN位为0时PLLQEN位才可写。0: 禁止CK_PLLQ输出1: 使能CK_PLLQ输出</td></tr><tr><td>19</td><td>PLLPEN</td><td>PLLP 分频器输出使能由软件置位或复位。只有在PLLEN位为0时PLLPEN位才可写。0: 禁止CK_PLLP输出1: 使能CK_PLLP输出</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>PLLP[1:0]</td><td>PLLP 输出频率分频系数(PLL VCO 时钟做为输入)当 PLL 被关闭时由软件置位或清零。这些位域用做将 PLL VCO 时钟(CK_PLLVCO)分频生成 PLLP 输出时钟(CK_PLLP)。CK_PLLP 时钟可以被用作系统时钟(不超过 216MHz)。RCU_PLL 寄存器的 PLLN 位域对 CK_PLLVCO 时钟进行了描述。00: CK_PLLP = CK_PLLVCO / 201: CK_PLLP = CK_PLLVCO / 410: CK_PLLP = CK_PLLVCO / 611: CK_PLLP = CK_PLLVCO / 8</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:6</td><td>PLLN[8:0]</td><td>PLL VCO 时钟倍频因子当 PLL 被关闭时由软件置位或清零(仅支持全字/半字写操作)。这些位域用做将 PLL VCO 源时钟(CK_PLLVCOSRC)倍频生成 PLL VCO 输出时钟(CK_PLLVCO)。RCU_PLL 寄存器的 PLLPSC 位域对 CK_PLLVCOSRC 时钟进行了描述。注意: CK_PLLVCO 时钟频率范围必须在 96MHz 到 480MHz 之间PLLN 的值必须满足:<eq>8 \leq \text{PLLN} \leq 180</eq>000000000: 保留000000001: 保留000111111:保留</td></tr><tr><td></td><td></td><td>0001000: PLLN = 8</td></tr><tr><td></td><td></td><td>0001001: PLLN = 9</td></tr><tr><td></td><td></td><td>0001010: PLLN = 10</td></tr><tr><td></td><td></td><td>...</td></tr><tr><td></td><td></td><td>10110100: PLLN = 180</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>PLLPSC[5:0]</td><td>PLL VCO 源时钟分频器当PLL被关闭时由软件置位或清零。这些位域用做将PLL源时钟(CK_PLLSRC)分频生成PLL VCO源时钟(CK_PLLVCOSRC)。RCU_PLL寄存器的PLLSEL位对CK_PLLSRC时钟进行了描述。VCO源时钟频率范围必须在2MHz到16MHz之间</td></tr><tr><td></td><td></td><td>0000: CK_PLLSRC</td></tr><tr><td></td><td></td><td>0001: CK_PLLSRC / 2</td></tr><tr><td></td><td></td><td>0010: CK_PLLSRC / 3</td></tr><tr><td></td><td></td><td>0011: CK_PLLSRC / 4</td></tr><tr><td></td><td></td><td>...</td></tr><tr><td></td><td></td><td>1111: CK_PLLSRC / 16</td></tr></table>

## 4.3.3. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="3">APB3PSC[2:0]</td><td colspan="3">CKOUTDIV[2:0]</td><td colspan="3">CKOUTSEL[2:0]</td><td colspan="5">保留</td></tr><tr><td colspan="2"></td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="2">保留</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="3">rw</td><td colspan="5">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:27</td><td>APB3PSC[2:0]</td><td>APB3 预分频选择由软件置位或清零,控制 APB3 时钟分频因子0xx: CK_APB3 = CK_AHB100: CK_APB3 = CK_AHB / 2</td></tr></table>

<table><tr><td rowspan="3"></td><td rowspan="3"></td><td>101: CK_APB3 = CK_AHB / 4</td></tr><tr><td>110: CK_APB3 = CK_AHB / 8</td></tr><tr><td>111: CK_APB3 = CK_AHB / 16</td></tr><tr><td>26:24</td><td>CKOUTDIV[2:0]</td><td>CK_OUT 分频器,来降低 CK_OUT 频率CK_OUT 的选择参考 RCU_CFG0 的 23:21 位。000: CK_OUT 不分频001: CK_OUT 2 分频010: CK_OUT 4 分频011: CK_OUT 8 分频100: CK_OUT 16 分频</td></tr><tr><td>23:21</td><td>CKOUTSEL[2:0]</td><td>CKOUT 时钟源选择由软件置位或清零000: 无时钟输出001: 保留010: 选择 CK_IRC32K 时钟011: 选择低速晶体振荡器时钟 (LXTAL)100: 选择系统时钟 CK_SYS101: 选择内部 8M RC 振荡器时钟110: 选择高速晶体振荡器时钟 (HXTAL)111: 选择 CK_PLLP 时钟</td></tr><tr><td>20:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>APB2PSC[2:0]</td><td>APB2 预分频选择由软件置位或清零,控制 APB2 时钟分频因子0xx: CK_APB2 = CK_AHB100: CK_APB2 = CK_AHB / 2101: CK_APB2 = CK_AHB / 4110: CK_APB2 = CK_AHB / 8111: CK_APB2 = CK_AHB / 16</td></tr><tr><td>12:10</td><td>APB1PSC[2:0]</td><td>APB1 预分频选择由软件置位或清零,控制 APB1 时钟分频因子.0xx: CK_APB1 = CK_AHB100: CK_APB1 = CK_AHB / 2101: CK_APB1 = CK_AHB / 4110: CK_APB1 = CK_AHB / 8111: CK_APB1 = CK_AHB / 16</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB 预分频选择</td></tr></table>

由软件置位或清零，控制 AHB 时钟 由软件置位或清零，控制AHB时钟分频因子

0xxx：CK_AHB = CK_SYS 1000：CK_AHB = CK_SYS / 2 1001：CK_AHB = CK_SYS / 4 1010：CK_AHB = CK_SYS / 8 1011：CK_AHB = CK_SYS / 16 1100：CK_AHB = CK_SYS / 64 1101：CK_AHB = CK_SYS / 128 1110：CK_AHB = CK_SYS / 256 1111：CK_AHB = CK_SYS / 512 

由硬件置位或清零，标识当前系统时钟的时钟源

00：选择 CK_IRC8M 时钟作为 CK_SYS 时钟源

01：选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10：保留

11：选择 CK_PLLP 时钟作为 CK_SYS 时钟源

由软件配置选择系统时钟源。由于 CK_SYS 的改变存在固有的延迟，因此软件应当读 SCSS 位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时，以及当 HXTAL 直接或间接作为系统时钟同时 HXTAL 时钟监视器检测到 HXTAL 故障时，强制选择 IRC8M作为系统时钟。

00：选择 CK_IRC8M 时钟作为 CK_SYS 时钟源

01：选择 CK_HXTAL 时钟作为 CK_SYS 时钟源

10：保留

11：选择 CK_PLL 时钟作为 CK_SYS 时钟源

## 4.3.4. 时钟中断寄存器（RCU_INT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>LCKMIC</td><td>LCKMIF</td><td colspan="3">保留</td><td>CKMIC</td><td colspan="2">保留</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC8MSTBIC</td><td>LXTALSTBIC</td><td>IRC32KSTBIC</td></tr><tr><td colspan="3"></td><td>w</td><td>r</td><td colspan="3"></td><td>w</td><td colspan="2"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC8MSTBIE</td><td>LXTALSTBIE</td><td>IRC32KSTBIE</td><td>CKMIF</td><td colspan="2">保留</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC8MSTBIF</td><td>LXTALSTBIF</td><td>IRC32KSTBIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>LCKMIC</td><td>LXTAL时钟阻塞中断清零软件写1复位LCKMIF标志位0:不复位LCKMIF标志位1:复位LCKMIF标志位</td></tr><tr><td>27</td><td>LCKMIF</td><td>LXTAL时钟阻塞中断标志位当LXTAL时钟被阻塞时由硬件置位软件置位LCKMIC位时清除该位0:时钟正常运行1:LXTAL时钟阻塞</td></tr><tr><td>26:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位.0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL时钟稳定中断清零软件写1复位PLLSTBIF标志位0:不复位PLLSTBIF标志位1:复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC8MSTBIC</td><td>IRC8M时钟稳定中断清零软件写1复位IRC8MSTBIF标志位0:不复位IRC8MSTBIF标志位1:复位IRC8MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0:不复位LXTALSTBIF标志位1:复位LXTALSTBIF标志位</td></tr></table>

<table><tr><td>16</td><td>IRC32KSTBIC</td><td>IRC32K时钟稳定中断清零软件写1复位IRC32KSTBIF标志位0:不复位IRC32KSTBIF标志位1:复位IRC32KSTBIF标志位</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置位和复位来使能/禁止PLL时钟稳定中断0:禁止PLL时钟稳定中断1:使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC8MSTBIE</td><td>IRC8M时钟稳定中断使能软件置位和复位来使能/禁止IRC8M时钟稳定中断0:禁止IRC8M时钟稳定中断1:使能IRC8M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC32KSTBIE</td><td>IRC32K时钟稳定中断使能软件置位和复位来使能/禁止IRC32K时钟稳定中断0:禁止IRC32K时钟稳定中断1:使能IRC32K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位.软件置位CKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1软件置位PLLSTBIC位时清除该位0:无PLL时钟稳定中断产生</td></tr></table>

<table><tr><td></td><td></td><td>1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~32MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC8MSTBIF</td><td>IRC8M时钟稳定中断标志位当内部8MHz RC振荡器时钟稳定且IRC8MSTBIE位被置1时由硬件置1软件置位IRC8MSTBIC位时清除该位0:无IRC8M时钟稳定中断产生1:产生IRC8M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC32KSTBIF</td><td>IRC32K时钟稳定中断标志位当内部32kHz RC振荡器时钟稳定且IRC32KSTBIE位被置1时由硬件置1软件置位IRC32KSTBIC位时清除该位0:无IRC32K时钟稳定中断产生1:产生IRC32K时钟稳定中断</td></tr></table>

## 4.3.5. AHB1 复位寄存器（RCU_AHB1RST）

地址偏移：0x010

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FFTRST</td><td colspan="7">保留</td><td>DMAMUXRST</td><td>DMA1RS T</td><td>DMA0RS T</td><td colspan="5">保留</td></tr><tr><td colspan="8">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CLARST</td><td colspan="2">保留</td><td>CRCRST</td><td colspan="12">保留</td></tr><tr><td>rw</td><td colspan="15">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FFTRST</td><td>FFT 复位由软件置位或复位0:无作用1:复位 FFT</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXRST</td><td>DMAMUX 复位由软件置位或复位0:无作用1:复位 DMAMUX</td></tr><tr><td>22</td><td>DMA1RST</td><td>DMA1 复位由软件置位或复位0:无作用1:复位 DMA1</td></tr><tr><td>21</td><td>DMA0RST</td><td>DMA0 复位由软件置位或复位0:无作用1:复位 DMA0</td></tr><tr><td>20:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CLARST</td><td>CLA 复位由软件置位或复位0:无作用1:复位 CLA</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCRST</td><td>CRC 复位由软件置位或复位0:无作用1:复位 CRC</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.6. AHB2 复位寄存器（RCU_AHB2RST）

地址偏移：0x014

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TMURST</td><td>TRNGRS T</td><td colspan="2">保留</td><td>CAURST</td><td>保留</td><td>FACRST</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PGRST</td><td>GPIO端口G复位由软件置位或复位0:无作用1:复位GPIO端口G</td></tr><tr><td>22</td><td>PFRST</td><td>GPIO端口F复位由软件置位或复位0:无作用1:复位GPIO端口F</td></tr><tr><td>21</td><td>PERST</td><td>GPIO端口E复位由软件置位或复位0:无作用1:复位GPIO端口E</td></tr><tr><td>20</td><td>PDRST</td><td>GPIO端口D复位由软件置位或复位0:无作用1:复位GPIO端口D</td></tr><tr><td>19</td><td>PCRST</td><td>GPIO端口C复位由软件置位或复位0:无作用1:复位GPIO端口C</td></tr><tr><td>18</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>17</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr></table>

<table><tr><td>16:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TMURST</td><td>TMU 复位由软件置位或复位0:无作用1:复位 TMU</td></tr><tr><td>6</td><td>TRNGRST</td><td>TRNG 复位由软件置位或复位0:无作用1:复位 TRNG</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CAURST</td><td>CAU 复位由软件置位或复位0:无作用1:复位 CAU</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>FACRST</td><td>FAC 复位由软件置位或复位0:无作用1:复位 FAC</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.7. AHB3 复位寄存器（RCU_AHB3RST）

地址偏移：0x018

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>QSPIRST</td><td>EXMCRST</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>QSPIRST</td><td>QSPI 复位由软件置位或复位0:无作用1:复位 QSPI</td></tr><tr><td>0</td><td>EXMCRST</td><td>EXMC 复位由软件置位或复位0:无作用1:复位 EXMC</td></tr></table>

## 4.3.8. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x20

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMURST</td><td colspan="3">保留</td><td>I2C3RST</td><td>I2C2RST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>USART2RST</td><td>USART1RST</td><td>保留</td></tr><tr><td colspan="3"></td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td colspan="2">保留</td><td>WWDGTRST</td><td>保留</td><td>LPTIMERRST</td><td colspan="3">保留</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3RST</td><td>I2C3 复位由软件置位或复位0:无作用1:复位 I2C3</td></tr><tr><td>23</td><td>I2C2RST</td><td>I2C2 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位I2C2</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用1:复位UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0:无作用1:复位UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0:无作用1:复位USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0:无作用1:复位USART1</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0:无作用1:复位SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0:无作用</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位0:无作用1:复位 WWDGT</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>LPTIMERRST</td><td>LPTIMER 复位由软件置位或复位0:无作用1:复位 LPTIMER</td></tr><tr><td>8:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6 复位由软件置位或复位0:无作用1:复位 TIMER6</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5 复位由软件置位或复位0:无作用1:复位 TIMER5</td></tr><tr><td>3</td><td>TIMER4RST</td><td>TIMER4 复位由软件置位或复位0:无作用1:复位 TIMER4</td></tr><tr><td>2</td><td>TIMER3RST</td><td>TIMER3 复位由软件置位或复位0:无作用1:复位 TIMER3</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2 复位由软件置位或复位0:无作用1:复位 TIMER2</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用</td></tr></table>

## 1：复位 TIMER1

## 4.3.9. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x24

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRIGSEL RST</td><td>保留</td><td>HRTIME RRST</td><td colspan="9">保留</td><td>HPDFRS T</td><td>TIMER16 RST</td><td>TIMER15 RST</td><td>TIMER14 RST</td></tr><tr><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TIMER19 RST</td><td>SYSCFG RST</td><td>保留</td><td>SPI0RST</td><td>保留</td><td>CAN2RS T</td><td>CAN1RS T</td><td>CAN0RS T</td><td colspan="3">保留</td><td>USART0 RST</td><td>CMPRST</td><td>VREFRS T</td><td>TIMER7R ST</td><td>TIMER0R ST</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRIGSELRST</td><td>TRIGSEL 复位由软件置位或复位0:无作用1:复位 TRIGSEL</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>HRTIMEREN</td><td>HRTIMER 复位由软件置位或复位0:无作用1:复位 HRTIMER</td></tr><tr><td>28:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>HPDFRST</td><td>HPDF 复位由软件置位或复位0:无作用1:复位 HPDF</td></tr><tr><td>18</td><td>TIMER16RST</td><td>TIMER16 复位由软件置位或复位0:无作用1:复位 TIMER16</td></tr><tr><td>17</td><td>TIMER15RST</td><td>TIMER15 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 TIMER15</td></tr><tr><td>16</td><td>TIMER14RST</td><td>TIMER14 复位由软件置位或复位0:无作用1:复位 TIMER14</td></tr><tr><td>15</td><td>TIMER19RST</td><td>TIMER19 复位由软件置位或复位0:无作用1:复位 TIMER19</td></tr><tr><td>14</td><td>SYSCFGRST</td><td>SYSCFG 复位由软件置位或复位0:无作用1:复位 SYSCFG</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CAN2RST</td><td>CAN2 复位由软件置位或复位0:无作用1:复位 CAN2</td></tr><tr><td>9</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>8</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>USART0RST</td><td>USART0 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位USART0</td></tr><tr><td>3</td><td>CMPRST</td><td>CMP复位由软件置位或复位0:无作用1:复位CMP</td></tr><tr><td>2</td><td>VREFRST</td><td>VREFR复位由软件置位或复位0:无作用1:复位VREFR</td></tr><tr><td>1</td><td>TIMER7RST</td><td>TIMER7复位由软件置位或复位0:无作用1:复位TIMER7</td></tr><tr><td>0</td><td>TIMER0RST</td><td>TIMER0复位由软件置位或复位0:无作用1:复位TIMER0</td></tr></table>

## 4.3.10. APB3 复位寄存器（RCU_APB3RST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>DAC3RS T</td><td>DAC2RS T</td><td>DAC1RS T</td><td>DAC0RS T</td><td>DACHOL DRST</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ADC3RS T</td><td>ADC2RS T</td><td>ADC1RS T</td><td>ADC0RS T</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>DAC3RST</td><td>DAC3 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 DAC3</td></tr><tr><td>19</td><td>DAC2RST</td><td>DAC2 复位由软件置位或复位0:无作用1:复位 DAC2</td></tr><tr><td>18</td><td>DAC1RST</td><td>DAC1 复位由软件置位或复位0:无作用1:复位 DAC1</td></tr><tr><td>17</td><td>DAC0RST</td><td>DAC0 复位由软件置位或复位0:无作用1:复位 DAC0</td></tr><tr><td>16</td><td>DACHOLDRST</td><td>DAC 保持时钟复位由软件置位或复位,DAC 保持时钟源为 IRC32K0:无作用1:复位 DAC 保持时钟</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>ADC3RST</td><td>ADC3 复位由软件置位或复位0:无作用1:复位 ADC3</td></tr><tr><td>10</td><td>ADC2RST</td><td>ADC2 复位由软件置位或复位0:无作用1:复位 ADC2</td></tr><tr><td>9</td><td>ADC1RST</td><td>ADC1 复位由软件置位或复位0:无作用1:复位 ADC1</td></tr><tr><td>8</td><td>ADC0RST</td><td>ADC0 复位由软件置位或复位0:无作用</td></tr></table>

1：复位 ADC0

7:0 保留 必须保持复位值。

## 4.3.11. AHB1 使能寄存器（RCU_AHB1EN）

地址偏移：0x030

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FFTEN</td><td colspan="7">保留</td><td>DMAMUX EN</td><td>DMA1EN</td><td>DMA0EN</td><td colspan="5">保留</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CLAEN</td><td colspan="2">保留</td><td>CRCEN</td><td colspan="12">保留</td></tr><tr><td>rw</td><td colspan="15">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FFTEN</td><td>FFT时钟使能由软件置位或复位0:关闭FFT时钟1:开启FFT时钟</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXEN</td><td>DMAMUX时钟使能由软件置位或复位0:关闭DMAMUX时钟1:开启DMAMUX时钟</td></tr><tr><td>22</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭DMA1时钟1:开启DMA1时钟</td></tr><tr><td>21</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr><tr><td>20:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CLAEN</td><td>CLA时钟使能由软件置位或复位0:关闭CLA时钟1:开启CLA时钟</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0:关闭CRC时钟1:开启CRC时钟</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.12. AHB2 使能寄存器（RCU_AHB2EN）

地址偏移：0x034

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>TMUEN</td><td>TRNGEN</td><td colspan="2">保留</td><td>CAUEN</td><td>保留</td><td>FACEN</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PGEN</td><td>GPIO端口G时钟使能由软件置位或复位0:关闭GPIO端口G时钟1:开启GPIO端口G时钟</td></tr><tr><td>22</td><td>PFEN</td><td>GPIO端口F时钟使能由软件置位或复位0:关闭GPIO端口F时钟1:开启GPIO端口F时钟</td></tr><tr><td>21</td><td>PEEN</td><td>GPIO端口E时钟使能由软件置位或复位0:关闭GPIO端口E时钟1:开启GPIO端口E时钟</td></tr></table>

<table><tr><td>20</td><td>PDEN</td><td>GPIO端口D时钟使能由软件置位或复位0:关闭GPIO端口D时钟1:开启GPIO端口D时钟</td></tr><tr><td>19</td><td>PCEN</td><td>GPIO端口C时钟使能由软件置位或复位0:关闭GPIO端口C时钟1:开启GPIO端口C时钟</td></tr><tr><td>18</td><td>PBEN</td><td>GPIO端口B时钟使能由软件置位或复位0:关闭GPIO端口B时钟1:开启GPIO端口B时钟</td></tr><tr><td>17</td><td>PAEN</td><td>GPIO端口A时钟使能由软件置位或复位0:关闭GPIO端口A时钟1:开启GPIO端口A时钟</td></tr><tr><td>16:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TMUEN</td><td>TMU时钟使能由软件置位或复位0:关闭TMU时钟1:开启TMU时钟</td></tr><tr><td>6</td><td>TRNGEN</td><td>TRNG时钟使能由软件置位或复位0:关闭TRNG时钟1:开启TRNG时钟</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CAUEN</td><td>CAU时钟使能由软件置位或复位0:关闭CAU时钟1:开启CAU时钟</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>FACEN</td><td>FAC时钟使能由软件置位或复位0:关闭FAC时钟1:开启FAC时钟</td></tr></table>

0 保留 必须保持复位值。

## 4.3.13. AHB3 使能寄存器（RCU_AHB3EN）

地址偏移：0x038

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>QSPIEN</td><td>EXMCEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>QSPIEN</td><td>QSPI 时钟使能由软件置位或复位0: 关闭 QSPI 时钟1: 开启 QSPI 时钟</td></tr><tr><td>0</td><td>EXMCEN</td><td>EXMC 时钟使能由软件置位或复位0: 关闭 EXMC 时钟1: 开启 EXMC 时钟</td></tr></table>

## 4.3.14. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x40

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMUEN</td><td colspan="3">保留</td><td>I2C3EN</td><td>I2C2EN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>保留</td></tr><tr><td colspan="7">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td>保留</td><td>LPTIMEREN</td><td colspan="3">保留</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3EN</td><td>I2C3时钟使能由软件置位或复位0:关闭I2C3时钟1:开启I2C3时钟</td></tr><tr><td>23</td><td>I2C2EN</td><td>I2C2时钟使能由软件置位或复位0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟</td></tr></table>

<table><tr><td></td><td></td><td>1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>LPTIMEREN</td><td>LPTIMER时钟使能由软件置位或复位0:关闭LPTIMER时钟1:开启LPTIMER时钟</td></tr><tr><td>8:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6时钟使能由软件置位或复位0:关闭TIMER6时钟1:开启TIMER6时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5时钟使能由软件置位或复位0:关闭TIMER5时钟1:开启TIMER5时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:关闭 TIMER4 时钟1:开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3 时钟使能由软件置位或复位0:关闭 TIMER3 时钟1:开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2 时钟使能由软件置位或复位0:关闭 TIMER2 时钟1:开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1 时钟使能由软件置位或复位0:关闭 TIMER1 时钟1:开启 TIMER1 时钟</td></tr></table>

## 4.3.15. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x44

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TRIGSEL EN</td><td>保留</td><td>HRTIME REN</td><td colspan="9">保留</td><td>HPDFEN</td><td>TIMER16 EN</td><td>TIMER15 EN</td><td>TIMER14 EN</td></tr><tr><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TIMER19 EN</td><td>SYSCFG EN</td><td>保留</td><td>SPI0EN</td><td>保留</td><td>CAN2EN</td><td>CAN1EN</td><td>CAN0EN</td><td colspan="3">保留</td><td>USART0 EN</td><td>CMPEN</td><td>VREFEN</td><td>TIMER7E N</td><td>TIMER0E N</td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRIGSELEN</td><td>TRIGSEL 时钟使能由软件置位或复位0: 关闭 TRIGSEL 时钟1: 开启 TRIGSEL 时钟</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>HRTIMEREN</td><td>HRTIMER 时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:关闭 HRTIMER 时钟1:开启 HRTIMER 时钟</td></tr><tr><td>28:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>HPDFEN</td><td>HPDF 时钟使能由软件置位或复位0:关闭 HPDF 时钟1:开启 HPDF 时钟</td></tr><tr><td>18</td><td>TIMER16EN</td><td>TIMER16 时钟使能由软件置位或复位0:关闭 TIMER16 时钟1:开启 TIMER16 时钟</td></tr><tr><td>17</td><td>TIMER15EN</td><td>TIMER14 时钟使能由软件置位或复位0:关闭 TIMER14 时钟1:开启 TIMER14 时钟</td></tr><tr><td>16</td><td>TIMER14EN</td><td>TIMER14 时钟使能由软件置位或复位0:关闭 TIMER14 时钟1:开启 TIMER14 时钟</td></tr><tr><td>15</td><td>TIMER19EN</td><td>TIMER19 时钟使能由软件置位或复位0:关闭 TIMER19 时钟1:开启 TIMER19 时钟</td></tr><tr><td>14</td><td>SYSCFGEN</td><td>SYSCFG 时钟使能由软件置位或复位0:关闭 SYSCFG 时钟1:开启 SYSCFG 时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0 时钟使能由软件置位或复位0:关闭 SPI0 时钟1:开启 SPI0 时钟</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CAN2EN</td><td>CAN2 时钟使能由软件置位或复位0:关闭CAN2时钟1:开启CAN2时钟</td></tr><tr><td>9</td><td>CAN1EN</td><td>CAN1时钟使能由软件置位或复位0:关闭CAN1时钟1:开启CAN1时钟</td></tr><tr><td>8</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>3</td><td>CMPEN</td><td>CMP时钟使能由软件置位或复位0:关闭CMP时钟1:开启CMP时钟</td></tr><tr><td>2</td><td>VREFEN</td><td>VREF时钟使能由软件置位或复位0:关闭VREF时钟1:开启VREF时钟</td></tr><tr><td>1</td><td>TIMER7EN</td><td>TIMER7时钟使能由软件置位或复位0:关闭TIMER7时钟1:开启TIMER7时钟</td></tr><tr><td>0</td><td>TIMER0EN</td><td>TIMER0时钟使能由软件置位或复位0:关闭TIMER0时钟1:开启TIMER0时钟</td></tr></table>

## 4.3.16. APB3 使能寄存器（RCU_APB3EN）

地址偏移：0x48\
复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>DAC3EN</td><td>DAC2EN</td><td>DAC1EN</td><td>DAC0EN</td><td>DACHOL DEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ADC3EN</td><td>ADC2EN</td><td>ADC1EN</td><td>ADC0EN</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>DAC3EN</td><td>DAC3时钟使能由软件置位或复位0:关闭 DAC3 时钟1:开启 DAC3 时钟</td></tr><tr><td>19</td><td>DAC2EN</td><td>DAC2时钟使能由软件置位或复位0:关闭 DAC2 时钟1:开启 DAC2 时钟</td></tr><tr><td>18</td><td>DAC1EN</td><td>DAC1时钟使能由软件置位或复位0:关闭 DAC1 时钟1:开启 DAC1 时钟</td></tr><tr><td>17</td><td>DAC0EN</td><td>DAC0时钟使能由软件置位或复位0:关闭 DAC0 时钟1:开启 DAC0 时钟</td></tr><tr><td>16</td><td>DACHOLDEN</td><td>DAC保持时钟使能由软件置位或复位,DAC保持时钟源为 IRC32K。0:关闭 DAC 保持时钟1:开启 DAC 保持时钟</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>ADC3EN</td><td>ADC3时钟使能由软件置位或复位0:关闭 ADC3 时钟1:开启ADC3时钟</td></tr><tr><td>10</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭ADC2时钟1:开启ADC2时钟</td></tr><tr><td>9</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>8</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.17. AHB1 睡眠和深度睡眠使能寄存器（RCU_AHB1SPDPEN）

地址偏移：0x050

复位值：0x80EB 9100

注意：Bit8不能被清零。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FFTSPD PEN</td><td colspan="7">保留</td><td>DMAMUX SPDPEN</td><td>DMA1SP DPEN</td><td>DMA0SP DPEN</td><td>保留</td><td>TCMSRAMSPDPEN</td><td>保留</td><td>SRAM1SP DPEN</td><td>SRAM0SP DPEN</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CLASPD PEN</td><td colspan="2">保留</td><td>CRCSPD PEN</td><td colspan="12">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FFTSPDPEN</td><td>在睡眠和深度睡眠模式下 FFT 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 FFT 时钟1: 在睡眠和深度睡眠模式下开启 FFT 时钟</td></tr></table>

<table><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXSPDPEN</td><td>在睡眠和深度睡眠模式下 DMAMUX 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 DMAMUX 时钟1: 在睡眠和深度睡眠模式下开启 DMAMUX 时钟</td></tr><tr><td>22</td><td>DMA1SPDPEN</td><td>在睡眠和深度睡眠模式下 DMA1 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 DMA1 时钟1: 在睡眠和深度睡眠模式下开启 DMA1 时钟</td></tr><tr><td>21</td><td>DMA0SPDPEN</td><td>在睡眠和深度睡眠模式下 DMA0 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 DMA0 时钟1: 在睡眠和深度睡眠模式下开启 DMA0 时钟</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>TCMSRAMSPDPEN</td><td>在睡眠和深度睡眠模式下 TCMSRAM 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TCMSRAM 时钟1: 在睡眠和深度睡眠模式下开启 TCMSRAM 时钟</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SRAM1SPDPEN</td><td>在睡眠和深度睡眠模式下 SRAM1 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SRAM1 时钟1: 在睡眠和深度睡眠模式下开启 SRAM1 时钟</td></tr><tr><td>16</td><td>SRAM0SPDPEN</td><td>在睡眠和深度睡眠模式下 SRAM0 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SRAM0 时钟1: 在睡眠和深度睡眠模式下开启 SRAM0 时钟</td></tr><tr><td>15</td><td>CLASPDPEN</td><td>在睡眠和深度睡眠模式下 CLA 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 CLA 时钟1: 在睡眠和深度睡眠模式下开启 CLA 时钟</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCSPDPEN</td><td>在睡眠和深度睡眠模式下 CRC 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 CRC 时钟</td></tr></table>

1：在睡眠和深度睡眠模式下开启 CRC 时钟

11:0 保留 必须保持复位值。

## 4.3.18. AHB2 睡眠和深度睡眠使能寄存器（RCU_AHB2SPDPEN）

地址偏移：0x054

复位值：0x00FE 00CA

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>PGSPDPEN</td><td>PFSPDPEN</td><td>PESPDPEN</td><td>PDSPDPEN</td><td>PCSPDPEN</td><td>PBSPDPEN</td><td>PASPDPEN</td><td>保留</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>TMUSDPEN</td><td>TRNGSPD PEN</td><td colspan="2">保留</td><td>CAUSDPEN</td><td>保留</td><td>FACSPDPEN</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>PGSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 G 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 G 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 G 时钟</td></tr><tr><td>22</td><td>PFSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 F 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 F 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 F 时钟</td></tr><tr><td>21</td><td>PESPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 E 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 E 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 E 时钟</td></tr><tr><td>20</td><td>PDSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 D 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 D 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 D 时钟</td></tr><tr><td>19</td><td>PCSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 C 时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:在睡眠和深度睡眠模式下关闭 GPIO 端口 C 时钟1:在睡眠和深度睡眠模式下开启 GPIO 端口 C 时钟</td></tr><tr><td>18</td><td>PBSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 B 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 GPIO 端口 B 时钟1:在睡眠和深度睡眠模式下开启 GPIO 端口 B 时钟</td></tr><tr><td>17</td><td>PASPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 A 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 GPIO 端口 A 时钟1:在睡眠和深度睡眠模式下开启 GPIO 端口 A 时钟</td></tr><tr><td>16:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>TMUSPDPEN</td><td>在睡眠和深度睡眠模式下 TMU 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TMU 时钟1:在睡眠和深度睡眠模式下开启 TMU 时钟</td></tr><tr><td>6</td><td>TRNGSPDPEN</td><td>在睡眠和深度睡眠模式下 TRNG 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TRNG 时钟1:在睡眠和深度睡眠模式下开启 TRNG 时钟</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CAUSPDPEN</td><td>在睡眠和深度睡眠模式下 CAU 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 CAU 时钟1:在睡眠和深度睡眠模式下开启 CAU 时钟</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>FACSPDPEN</td><td>在睡眠和深度睡眠模式下 FAC 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 FAC 时钟1:在睡眠和深度睡眠模式下开启 FAC 时钟</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.19. AHB3 睡眠和深度睡眠使能寄存器（RCU_AHB3SPDPEN）

地址偏移：0x058

复位值：0x0000 0003

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>QSPISPD PEN</td><td>EXMCSP DPEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>QSPISPDPEN</td><td>在睡眠和深度睡眠模式下 QSPI 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 QSPI 时钟1: 在睡眠和深度睡眠模式下开启 QSPI 时钟</td></tr><tr><td>0</td><td>EXMCSPDPEN</td><td>在睡眠和深度睡眠模式下 EXMC 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 EXMC 时钟1: 在睡眠和深度睡眠模式下开启 EXMC 时钟</td></tr></table>

## 4.3.20. APB1 睡眠和深度睡眠使能寄存器（RCU_APB1SPDPEN）

地址偏移：0x60

复位值：0x11FE CA3F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMUSPD PEN</td><td colspan="3">保留</td><td>I2C3SPD PEN</td><td>I2C2SPD PEN</td><td>I2C1SPD PEN</td><td>I2C0SPD PEN</td><td>UART4S PDPEN</td><td>UART3S PDPEN</td><td>USART2 SPDPEN</td><td>USART1 SPDPEN</td><td>保留</td></tr><tr><td colspan="7">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2SPD PEN</td><td>SPI1SPD PEN</td><td colspan="2">保留</td><td>WWDGT SPDPEN</td><td>保留</td><td>LPTIMER SPDPEN</td><td colspan="3">保留</td><td>TIMER6S PDPEN</td><td>TIMER5S PDPEN</td><td>TIMER4S PDPEN</td><td>TIMER3S PDPEN</td><td>TIMER2S PDPEN</td><td>TIMER1S PDPEN</td></tr><tr><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMUSPDPEN</td><td>在睡眠和深度睡眠模式下 PMU 时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:在睡眠和深度睡眠模式下关闭PMU时钟1:在睡眠和深度睡眠模式下开启PMU时钟</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3SPDPEN</td><td>在睡眠和深度睡眠模式下I2C3时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭I2C3时钟1:在睡眠和深度睡眠模式下开启I2C3时钟</td></tr><tr><td>23</td><td>I2C2SPDPEN</td><td>在睡眠和深度睡眠模式下I2C2时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭I2C2时钟1:在睡眠和深度睡眠模式下开启I2C2时钟</td></tr><tr><td>22</td><td>I2C1SPDPEN</td><td>在睡眠和深度睡眠模式下I2C1时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭I2C1时钟1:在睡眠和深度睡眠模式下开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0SPDPEN</td><td>在睡眠和深度睡眠模式下I2C0时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭I2C0时钟1:在睡眠和深度睡眠模式下开启I2C0时钟</td></tr><tr><td>20</td><td>UART4SPDPEN</td><td>在睡眠和深度睡眠模式下UART4时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭UART4时钟1:在睡眠和深度睡眠模式下开启UART4时钟</td></tr><tr><td>19</td><td>UART3SPDPEN</td><td>在睡眠和深度睡眠模式下UART3时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭UART3时钟1:在睡眠和深度睡眠模式下开启UART3时钟</td></tr><tr><td>18</td><td>USART2SPDPEN</td><td>在睡眠和深度睡眠模式下USART2时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭USART2时钟1:在睡眠和深度睡眠模式下开启USART2时钟</td></tr><tr><td>17</td><td>USART1SPDPEN</td><td>在睡眠和深度睡眠模式下USART1时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭USART1时钟1:在睡眠和深度睡眠模式下开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2SPDPEN</td><td>在睡眠和深度睡眠模式下 SPI2 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SPI2 时钟1: 在睡眠和深度睡眠模式下开启 SPI2 时钟</td></tr><tr><td>14</td><td>SPI1SPDPEN</td><td>在睡眠和深度睡眠模式下 SPI1 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SPI1 时钟1: 在睡眠和深度睡眠模式下开启 SPI1 时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTSPDPEN</td><td>在睡眠和深度睡眠模式下 WWDGT 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 WWDGT 时钟1: 在睡眠和深度睡眠模式下开启 WWDGT 时钟</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>LPTIMERSPDPEN</td><td>在睡眠和深度睡眠模式下 LPTIMER 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 LPTIMER 时钟1: 在睡眠和深度睡眠模式下开启 LPTIMER 时钟</td></tr><tr><td>8:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER6 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER6 时钟1: 在睡眠和深度睡眠模式下开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER5 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER5 时钟1: 在睡眠和深度睡眠模式下开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER4 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER4 时钟1: 在睡眠和深度睡眠模式下开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER3 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER3 时钟</td></tr></table>

<table><tr><td></td><td></td><td>1:在睡眠和深度睡眠模式下开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER2 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TIMER2 时钟1:在睡眠和深度睡眠模式下开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER1 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TIMER1 时钟1:在睡眠和深度睡眠模式下开启 TIMER1 时钟</td></tr></table>

## 4.3.21. APB2 睡眠和深度睡眠使能寄存器（RCU_APB2SPDPEN）

地址偏移：0x64

复位值：0xA00F D71F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td><td></td></tr><tr><td>TRIGSELSPDPEN</td><td>保留</td><td>HRTIMERSPDPEN</td><td colspan="9">保留</td><td>HPDFSPDPEN</td><td>TIMER16SPDPEN</td><td>TIMER15SPDPEN</td><td>TIMER14SPDPEN</td><td></td></tr><tr><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td></td></tr><tr><td>TIMER19SPDPEN</td><td>SYSCFGSPDPEN</td><td>保留</td><td>SPI0SPDPEN</td><td>保留</td><td>CAN2SPDPEN</td><td>CAN1SPDPEN</td><td>CAN0SPDPEN</td><td colspan="3">保留</td><td>USART0SPDPEN</td><td>CMPSPDPEN</td><td>VREFSPDPEN</td><td>TIMER7SPDPEN</td><td>TIMER0SPDPEN</td><td></td></tr><tr><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TRIGSELSPDPEN</td><td>在睡眠和深度睡眠模式下 TRIGSEL 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TRIGSEL 时钟1: 在睡眠和深度睡眠模式下开启 TRIGSEL 时钟</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>HRTIMERSPDPEN</td><td>在睡眠和深度睡眠模式下 HRTIMER 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 HRTIMER 时钟1: 在睡眠和深度睡眠模式下开启 HRTIMER 时钟</td></tr><tr><td>28:20</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>19</td><td>HPDFSPDPEN</td><td>在睡眠和深度睡眠模式下 HPDF 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 HPDF 时钟1: 在睡眠和深度睡眠模式下开启 HPDF 时钟</td></tr><tr><td>18</td><td>TIMER16SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER16 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER16 时钟1: 在睡眠和深度睡眠模式下开启 TIMER16 时钟</td></tr><tr><td>17</td><td>TIMER15SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER15 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER15 时钟1: 在睡眠和深度睡眠模式下开启 TIMER15 时钟</td></tr><tr><td>16</td><td>TIMER14SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER14 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER14 时钟1: 在睡眠和深度睡眠模式下开启 TIMER14 时钟</td></tr><tr><td>15</td><td>TIMER19SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER19 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER19 时钟1: 在睡眠和深度睡眠模式下开启 TIMER19 时钟</td></tr><tr><td>14</td><td>SYSCFGSPDPEN</td><td>在睡眠和深度睡眠模式下 SYSCFG 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SYSCFG 时钟1: 在睡眠和深度睡眠模式下开启 SYSCFG 时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0SPDPEN</td><td>在睡眠和深度睡眠模式下 SPI0 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SPI0 时钟1: 在睡眠和深度睡眠模式下开启 SPI0 时钟</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>CAN2SPDPEN</td><td>在睡眠和深度睡眠模式下 CAN2 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 CAN2 时钟1: 在睡眠和深度睡眠模式下开启 CAN2 时钟</td></tr><tr><td>9</td><td>CAN1SPDPEN</td><td>在睡眠和深度睡眠模式下 CAN1 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭CAN1时钟1:在睡眠和深度睡眠模式下开启CAN1时钟</td></tr><tr><td>8</td><td>CAN0SPDPEN</td><td>在睡眠和深度睡眠模式下CAN0时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭CAN0时钟1:在睡眠和深度睡眠模式下开启CAN0时钟</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>USART0SPDPEN</td><td>在睡眠和深度睡眠模式下USART0时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭USART0时钟1:在睡眠和深度睡眠模式下开启USART0时钟</td></tr><tr><td>3</td><td>CMPSPDPEN</td><td>在睡眠和深度睡眠模式下CMP时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭CMP时钟1:在睡眠和深度睡眠模式下开启CMP时钟</td></tr><tr><td>2</td><td>VREFSPDPEN</td><td>在睡眠和深度睡眠模式下VREF时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭VREF时钟1:在睡眠和深度睡眠模式下开启VREF时钟</td></tr><tr><td>1</td><td>TIMER7SPDPEN</td><td>在睡眠和深度睡眠模式下TIMER7时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭TIMER7时钟1:在睡眠和深度睡眠模式下开启TIMER7时钟</td></tr><tr><td>0</td><td>TIMER0SPDPEN</td><td>在睡眠和深度睡眠模式下TIMER0时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭TIMER0时钟1:在睡眠和深度睡眠模式下开启TIMER0时钟</td></tr></table>

## 4.3.22. APB3 睡眠和深度睡眠使能寄存器（RCU_APB3SPDPEN）

地址偏移：0x68

复位值：0x001F 0F00

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>保留</td><td>DAC3SPDPEN</td><td>DAC2SPDPEN</td><td>DAC1SPDPEN</td><td>DAC0SPDPEN</td><td>DACHOLDSPDPEN</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>ADC3SPDPEN</td><td>ADC2SPDPEN</td><td>ADC1SPDPEN</td><td>ADC0SPDPEN</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>DAC3SPDPEN</td><td>在睡眠和深度睡眠模式下 DAC3 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 DAC3 时钟1:在睡眠和深度睡眠模式下开启 DAC3 时钟</td></tr><tr><td>19</td><td>DAC2SPDPEN</td><td>在睡眠和深度睡眠模式下 DAC2 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 DAC2 时钟1:在睡眠和深度睡眠模式下开启 DAC2 时钟</td></tr><tr><td>18</td><td>DAC1SPDPEN</td><td>在睡眠和深度睡眠模式下 DAC1 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 DAC1 时钟1:在睡眠和深度睡眠模式下开启 DAC1 时钟</td></tr><tr><td>17</td><td>DAC0SPDPEN</td><td>在睡眠和深度睡眠模式下 DAC0 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 DAC0 时钟1:在睡眠和深度睡眠模式下开启 DAC0 时钟</td></tr><tr><td>16</td><td>DACHOLDSPDPEN</td><td>在睡眠和深度睡眠模式下 DAC 保持时钟使能由软件置位或复位,DAC 保持时钟源为 IRC32K0:在睡眠模式下关闭 DAC 保持时钟1:在睡眠模式下开启 DAC 保持时钟</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>ADC3SPDPEN</td><td>在睡眠和深度睡眠模式下 ADC3 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 ADC3 时钟1:在睡眠和深度睡眠模式下开启 ADC3 时钟</td></tr><tr><td>10</td><td>ADC2SPDPEN</td><td>在睡眠和深度睡眠模式下 ADC2 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 ADC2 时钟1: 在睡眠和深度睡眠模式下开启 ADC2 时钟</td></tr><tr><td>9</td><td>ADC1SPDPEN</td><td>在睡眠和深度睡眠模式下 ADC1 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 ADC1 时钟1: 在睡眠和深度睡眠模式下开启 ADC1 时钟</td></tr><tr><td>8</td><td>ADC0SPDPEN</td><td>在睡眠和深度睡眠模式下 ADC0 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 ADC0 时钟1: 在睡眠和深度睡眠模式下开启 ADC0 时钟</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.23. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x70

复位值：0x0000 0018，只能由备份域复位进行复位

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

注意：备份域控制寄存器（RCU_BDCTL）的LXTALEN、LXTALBPS、RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>LSCKOUTSEL</td><td>LSCKOUTEN</td><td colspan="7">保留</td><td>BKPRST</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td colspan="7"></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td>LXTALSTBRST</td><td>LCKMD</td><td>LCKMEN</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31:26</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>25</td><td colspan="4">LSCKOUTSEL</td><td colspan="11">低速时钟输出选择0: IRC32K1: LXTAL</td></tr><tr><td>24</td><td colspan="4">LSCKOUTEN</td><td colspan="11">低速时钟输出使能0:低速时钟输出失能1:低速时钟输出使能</td></tr><tr><td>23:17</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>16</td><td colspan="4">BKPRST</td><td colspan="11">备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td colspan="4">RTCEN</td><td colspan="11">RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>9:8</td><td colspan="4">RTCSRC[1:0]</td><td colspan="11">RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC32K时钟作为RTC的时钟源11:选择CK_HXTAL/32时钟作为RTC的时钟源</td></tr><tr><td>7</td><td colspan="4">LXTALSTBRST</td><td colspan="11">低速晶体振荡器稳定标志位复位0:低速晶体振荡器稳定标志位不复位1:低速晶体振荡器稳定标志位复位</td></tr><tr><td>6</td><td colspan="4">LCKMD</td><td colspan="11">LXTAL时钟故障检测由硬件置位,当外部32kHz振荡器(LXTAL)上的时钟安全系统检测到故障。当LCKMEN或LXTALEN关闭时,该位清零。0:LXTAL(32kHz振荡器)上未检测到故障1:在LXTAL(32kHz振荡器)上检测到故障</td></tr><tr><td>5</td><td colspan="4">LCKMEN</td><td colspan="11">LXTAL时钟监视器使能0:禁止LXTAL时1:使能LXTAL时钟监视器通过软件设置,启用LXTAL(32kHz振荡器)上的时钟安全系统。LXTALEN必须在LXTAL已启用(LXTALEN位已启用)和就绪(LXTALSTB标志由硬件设置)。注意:一旦该位被置位,该位可以通过备份域复位清除或者在检测到LXTAL时钟故障后(LCKMD=1)通过复位LCKMEN清除。钟监视器</td></tr><tr><td>4:3</td><td colspan="4">LXTALDRI[1:0]</td><td colspan="11">LXTAL 驱动能力由软件置位或复位。当备份域复位时将复位该值00:禁止01:低驱动能力10:中驱动能力11:高驱动能力(复位后的缺省值)注意:LXTALDRI 位在旁路模式下无效</td></tr><tr><td>2</td><td colspan="4">LXTALBPS</td><td colspan="11">LXTAL 旁路模式使能由软件置位或复位0:禁止 LXTAL 旁路模式1:使能 LXTAL 旁路模式</td></tr><tr><td>1</td><td colspan="4">LXTALSTB</td><td colspan="11">低速晶体振荡器稳定标志位硬件置‘1’来指示 LXTAL 振荡器时钟是否稳定待用0:LXTAL 未稳定1:LXTAL 已稳定</td></tr><tr><td>0</td><td colspan="4">LXTALEN</td><td colspan="11">LXTAL 时钟使能由软件置位或复位0:关闭 LXTAL 时钟1:使能 LXTAL 时钟</td></tr></table>

## 4.3.24. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x74

复位值：0x0E00 0000，所有复位标志位仅在电源复位时被清零，RSTFC / IRC32KEN在系统复位时被清零。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>BORRSTF</td><td>RSTFC</td><td>OBLRST</td><td colspan="7">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>rw</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC32KSTB</td><td>IRC32KEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位</td></tr></table>

<table><tr><td></td><td></td><td>向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>BORRSTF</td><td>欠压复位复位标志位欠压复位复位发生时由硬件置1向RSTFC位写1来清除该位0:无欠压复位复位发生1:发生欠压复位复位</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用</td></tr></table>

<table><tr><td></td><td></td><td>1: 清除所有复位标志位</td></tr><tr><td>23</td><td>OBLRSTF</td><td>选项字节重载复位标志位选项字节重载复位发生时由硬件置1向RSTFC位写1来清除该位0: 无选项字节重载复位复位发生1: 发生选项字节重载复位</td></tr><tr><td>22:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC32KSTB</td><td>IRC32K时钟稳定标志位该位由硬件置1指示IRC32K输出时钟是否稳定待用0: IRC32K时钟未稳定1: IRC32K已稳定</td></tr><tr><td>0</td><td>IRC32KEN</td><td>IRC32K使能由软件置位和复位0: 关闭IRC32K时钟1: 开启IRC32K时钟</td></tr></table>

## 4.3.25. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x8C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>HPDFSEL</td><td colspan="2">HPDFAUDIOSEL[1:0]</td><td colspan="7">保留</td><td colspan="2">USART2SEL[1:0]</td><td colspan="2">USART1SEL[1:0]</td><td colspan="2">保留</td></tr><tr><td>rw</td><td colspan="9">rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">CAN2SEL[1:0]</td><td colspan="2">CAN1SEL[1:0]</td><td colspan="2">CAN0SEL[1:0]</td><td colspan="6">保留</td><td colspan="2">USART0SEL[1:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="6"></td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>HPDFSEL</td><td>HPDF 时钟源选择由软件置位或复位,控制 HPDF 时钟源0: CK_APB2 被选择为 HPDF 时钟的时钟源1: CK_AHB 被选择为 HPDF 时钟的时钟源</td></tr><tr><td>30:29</td><td>HPDFAUDIOSEL[1:0]</td><td>HPDF AUDIO 时钟源预选择由软件置位或复位,控制 HPDF AUDIO 时钟源00: CK_PLLQ 被选择为 HPDF AUDIO 时钟的时钟源</td></tr></table>

<table><tr><td></td><td></td><td>01:外部 HPDF_CKIN 引脚被选择为 HPDF AUDIO 时时钟的时钟源10:IRC8M 被选择为 HPDF AUDIO 时时钟的时钟源11:保留</td></tr><tr><td>28:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:20</td><td>USART2SEL[1:0]</td><td>USART2 时钟源预选择由软件置位或复位,控制 USART2 时钟源00:CK_APB1 被选择为 USART2 时钟的时钟源01:CK_SYS 被选择为 USART2 时时钟的时钟源10:CK_LXTAL 被选择为 USART2 时时钟的时钟源11:CK_IRC8M 被选择为 USART2 时时钟的时钟源</td></tr><tr><td>19:18</td><td>USART1SEL[1:0]</td><td>USART1 时钟源预选择由软件置位或复位,控制 USART1 时钟源00:CK_APB1 被选择为 USART1 时钟的时钟源01:CK_SYS 被选择为 USART1 时时钟的时钟源10:CK_LXTAL 被选择为 USART1 时时钟的时钟源11:CK_IRC8M 被选择为 USART1 时时钟的时钟源</td></tr><tr><td>17:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>CAN2SEL[1:0]</td><td>CAN2 时钟源预选择由软件置位或复位,控制 CAN2 时钟源00:CK_IRC8M 被选择为 CAN2 时钟的时钟源01:CK_APB2 被选择为 CAN2 时时钟的时钟源10:CK_PLLQ 被选择为 CAN2 时时钟的时钟源11:CK_HXTAL 被选择为 CAN2 时时钟的时钟源</td></tr><tr><td>11:10</td><td>CAN1SEL[1:0]</td><td>CAN1 时钟源预选择由软件置位或复位,控制 CAN1 时钟源00:CK_IRC8M 被选择为 CAN1 时钟的时钟源01:CK_APB2 被选择为 CAN1 时时钟的时钟源10:CK_PLLQ 被选择为 CAN1 时时钟的时钟源11:CK_HXTAL 被选择为 CAN1 时时钟的时钟源</td></tr><tr><td>9:8</td><td>CAN0SEL[1:0]</td><td>CAN0 时钟源预选择由软件置位或复位,控制 CAN0 时钟源00:CK_IRC8M 被选择为 CAN0 时钟的时钟源01:CK_APB2 被选择为 CAN0 时时钟的时钟源10:CK_PLLQ 被选择为 CAN0 时时钟的时钟源11:CK_HXTAL 被选择为 CAN0 时时钟的时钟源</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>1:0</td><td>USART0SEL[1:0]</td><td>USART0 时钟源预选择由软件置位或复位,控制 USART0 时钟源00: CK_APB2 被选择为 USART0 时钟的时钟源01: CK_SYS 被选择为 USART0 时时钟的时钟源10: CK_LXTAL 被选择为 USART0 时时钟的时钟源11: CK_IRC8M 被选择为 USART0 时时钟的时钟源</td></tr></table>

## 4.3.26. 时钟配置寄存器 2（RCU_CFG2）

地址偏移：0x90

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="2">ADC3SEL[1:0]</td><td colspan="2">ADC0_1_2SEL[1:0]</td><td colspan="6">保留</td><td>HRTIMERSEL</td><td>保留</td><td colspan="2">QSPISEL[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="8">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">TRNGPSC[3:0]</td><td>保留</td><td colspan="2">LPTIMERSEL[1:0]</td><td>保留</td><td colspan="2">I2C3SEL[1:0]</td><td colspan="2">I2C2SEL[1:0]</td><td colspan="2">I2C1SEL[1:0]</td><td colspan="2">I2C0SEL[1:0]</td></tr><tr><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>ADC3SEL[1:0]</td><td>ADC3时钟源预选择由软件置位或复位,控制ADC3时钟源00:保留01:CK_PLLR被选择为ADC3时时钟的时钟源10:CK_SYS被选择为ADC3时时钟的时钟源11:保留</td></tr><tr><td>27:26</td><td>ADC0_1_2SEL[1:0]</td><td>ADC0/1/2时钟源预选择由软件置位或复位,控制ADC0/1/2时钟源00:保留01:CK_PLLR被选择为ADC0/1/2时时钟的时钟源10:CK_SYS被选择为ADC0/1/2时时钟的时钟源11:保留</td></tr><tr><td>25:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>HRTIMERSEL</td><td>HRTIMER时钟源预选择由软件置位或复位,控制HRTIMER时钟源</td></tr></table>

<table><tr><td></td><td></td><td>0: CK_APB2 被选择为 HRTIMER 时时钟的时钟源1: CK_SYS 被选择为 HRTIMER 时时钟的时钟源</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>QSPISEL[1:0]</td><td>QSPI 时钟源预选择由软件置位或复位,控制 QSPI 时钟源00: CK_SYS 被选择为 QSPI 时钟的时钟源01: CK_IRC8M 被选择为 QSPI 时时钟的时钟源10: CK_PLLQ 被选择为 QSPI 时时钟的时钟源11: CK_PLLR 被选择为 QSPI 时时钟的时钟源</td></tr><tr><td>15:12</td><td>TRNGPSC[3:0]</td><td>TRNG 分频选择由软件置位或复位,控制 TRNG 时钟分频0000: 保留0001: 保留0010: CK_PLLQ / 20011: CK_PLLQ / 30100: CK_PLLQ / 4...1111: CK_PLLQ / 15</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:9</td><td>LPTIMERSEL[1:0]</td><td>LPTIMER 时钟源预选择由软件置位或复位,控制 LPTIMER 时钟源00: CK_APB1 被选择为 LPTIMER 时钟的时钟源01: CK_IRC32K 被选择为 LPTIMER 时时钟的时钟源10: CK_LXTAL 被选择为 LPTIMER 时时钟的时钟源11: CK_IRC8M 被选择为 LPTIMER 时时钟的时钟源</td></tr><tr><td>8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:6</td><td>I2C3SEL[1:0]</td><td>I2C3 时钟源预选择由软件置位或复位,控制 I2C3 时钟源00: CK_APB1 被选择为 I2C3 时钟的时钟源01: CK_SYS 被选择为 I2C3 时时钟的时钟源10: CK_IRC8M 被选择为 I2C3 时时钟的时钟源11: 保留</td></tr><tr><td>5:4</td><td>I2C2SEL[1:0]</td><td>I2C2 时钟源预选择由软件置位或复位,控制 I2C2 时钟源00: CK_APB1 被选择为 I2C2 时钟的时钟源01: CK_SYS 被选择为 I2C2 时时钟的时钟源</td></tr></table>

<table><tr><td></td><td></td><td>10: CK_IRC8M 被选择为 I2C2 时时钟的时钟源11: 保留</td></tr><tr><td>3:2</td><td>I2C1SEL[1:0]</td><td>I2C1 时钟源预选择由软件置位或复位,控制 I2C1 时钟源00: CK_APB1 被选择为 I2C1 时钟的时钟源01: CK_SYS 被选择为 I2C1 时时钟的时钟源10: CK_IRC8M 被选择为 I2C1 时时钟的时钟源11: 保留</td></tr><tr><td>1:0</td><td>I2C0SEL[1:0]</td><td>I2C0 时钟源预选择由软件置位或复位,控制 I2C0 时钟源00: CK_APB1 被选择为 I2C0 时钟的时钟源01: CK_SYS 被选择为 I2C0 时时钟的时钟源10: CK_IRC8M 被选择为 I2C0 时时钟的时钟源11: 保留</td></tr></table>

