## 5.3. RCU 寄存器

RCU基地址：0x4002 3800

## 5.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 xx83 x表示未定义

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>PLLSAIS TB</td><td>PLLSAIEN</td><td>PLLI2SSTB</td><td>PLLI2SEN</td><td>PLLSTB</td><td>PLLEN</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td colspan="2"></td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC16MCALIB[7:0]</td><td colspan="5">IRC16MADJ[4:0]</td><td>保留</td><td>IRC16MSTB</td><td>IRC16MEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>Must be kept at reset value.</td></tr><tr><td>29</td><td>PLLSAISTB</td><td>PLLSAI时钟稳定标志位硬件置1来表示PLLSAI输出时钟是否稳定待用0:PLLSAI未稳定1:PLLSAI已稳定</td></tr><tr><td>28</td><td>PLLSAIEN</td><td>PLLSAI使能软件置位或复位,当进入深度睡眠或待机模式时由硬件复位。0:PLLSAI被关闭1:PLLSAI被打开</td></tr><tr><td>27</td><td>PLLI2SSTB</td><td>PLLI2S时钟稳定标志位硬件置1来表示PLLI2S输出时钟是否稳定待用0:PLL12S未稳定1:PLL12S已稳定</td></tr><tr><td>26</td><td>PLLI2SEN</td><td>PLLI2S使能软件置位或复位,当进入深度睡眠或待机模式时由硬件复位。0:PLL12S被关闭1:PLL12S被打开</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置1来表示PLL输出时钟是否稳定待用0:PLL未稳定1:PLL已稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位,当PLL时钟做为系统时钟时该位不能被复位。当进入深度睡眠或待机模式时由硬件复位。0:PLL被关闭1:PLL被打开</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视器使能0:禁止高速4~32MHz晶体振荡器(HXTAL)时钟监视器1:使能高速4~32MHz晶体振荡器(HXTAL)时钟监视器当硬件检测到HXTAL时钟被阻塞在低或高状态时,内部硬件自动切换系统时钟到IRC16M时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC16MEN的状态,自动使能IRC16M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>高速晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTAL位为0时HXTALBPS位才可写0:禁止HXTAL旁路模式1:使能HXTAL旁路模式HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>高速晶体振荡器(HXTAL)时钟稳定标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>高速晶体振荡器(HXTAL)使能软件置位或复位,如果HXTAL时钟作为系统时钟或者当PLL时钟做为系统时钟时,其做为PLL的输入时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:高速4~32MHz晶体振荡器被关闭1:高速4~32MHz晶体振荡器被打开</td></tr><tr><td>15:8</td><td>IRC16MCALIB[7:0]</td><td>内部16MHz RC振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC16MADJ[4:0]</td><td>内部16MHz RC振荡器时钟调整值这些位由软件置位,最终调整值为IRC16MADJ[4:0]位域的当前值加上IRC16MCALIB[7:0]位域的值。最终调整值应该调整IRC16M到16MHz±1%。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC16MSTB</td><td>IRC16M内部16MHz RC振荡器稳定标志位硬件置‘1’来指示IRC16M振荡器时钟是否稳定待用0:IRC16M振荡器未稳定1:IRC16M振荡器已稳定</td></tr><tr><td>0</td><td>IRC16MEN</td><td>内部16MHz RC振荡器使能软件置位或复位,如果IRC16M时钟做为系统时钟时,该位不能被复位。当从深度睡</td></tr></table>

眠或待机模式返回，或当CKMEN置位同时用作系统时钟的HXTAL振荡器发生故障时，该位由硬件置1来启动IRC16M振荡器。

0：内部16 MHz RC振荡器被关闭

1：内部 16 MHz RC 振荡器被打开

## 5.3.2. PLL 寄存器（RCU_PLL）

地址偏移：0x04

复位值：0x2400 3010

配置PLL时钟可参考下列公式：

CK_PLLVCOSRC = CK_PLLSRC / PLLPSC 

CK_PLLVCO = CK_PLLVCOSRC × PLLN 

CK_PLLP = CK_PLLVCO / PLLP 

CK_PLLQ = CK_PLLVCO / PLLQ 

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">PLLQ[3:0]</td><td>保留</td><td>PLLSEL</td><td colspan="4">保留</td><td colspan="2">PLLP[1:0]</td></tr><tr><td colspan="8">rw</td><td colspan="6">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="9">PLLN[8:0]</td><td colspan="6">PLLPSC[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>PLLQ[3:0]</td><td>PLLQ输出频率的分频系数(PLL VCO时钟做为输入)当PLL被关闭时由软件置位或清零。这些位域用做将PLL VCO时钟(CK_PLLVCO)分频生成PLLQ输出时钟(CK_PLLQ)。CK_PLLQ时钟可以被用作UBSFS/USBHS(48MHz)、TRNG(48MHz)或SDIO(≤48MHz)模块的时钟源。RCU_PLL寄存器的PLLN位域对CK_PLLVCO时钟进行了描述。0000:保留0001:保留0010:CK_PLLQ=CK_PLLVCO/20011:CK_PLLQ=CK_PLLVCO/30100:CK_PLLQ=CK_PLLVCO/4...1111:CK_PLLQ=CK_PLLVCO/15</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PLLSEL</td><td>PLL时钟源选择由软件置位或复位,控制PLL时钟源0:IRC16M时钟被选择为PLL、PLLSAI、PLLI2S时钟的时钟源1:HXTAL时钟被选择为PLL、PLLSAI、PLLI2S时钟的时钟源</td></tr><tr><td>21:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>PLLP[1:0]</td><td>PLLP输出频率分频系数(PLL VCO时钟做为输入)当PLL被关闭时由软件置位或清零。这些位域用做将PLL VCO时钟(CK_PLLVCO)分频生成PLLP输出时钟(CK_PLLP)。CK_PLLP时钟可以被用作系统时钟(不超过200MHz)。RCU_PLL寄存器的PLLN位域对CK_PLLVCO时钟进行了描述。00: CK_PLLP = CK_PLLVCO / 201: CK_PLLP = CK_PLLVCO / 410: CK_PLLP = CK_PLLVCO / 611: CK_PLLP = CK_PLLVCO / 8</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:6</td><td>PLLN[8:0]</td><td>PLL VCO时钟倍频因子当PLL被关闭时由软件置位或清零(仅支持全字/半字写操作)。这些位域用做将PLL VCO源时钟(CK_PLLVCOSRC)倍频生成PLL VCO输出时钟(CK_PLLVCO)。RCU_PLL寄存器的PLLPSC位域对CK_PLLVCOSRC时钟进行了描述。注意:CK_PLLVCO时钟频率范围必须在100MHz到500MHz之间PLLN的值必须满足:64≤PLL≤500(当RCU_PLLSCTL寄存器的SSCGON=0)69≤PLL≤500(当RCU_PLLSCTL寄存器的SSCGON=1/SS_TYPE=0)71≤PLL≤500(当RCU_PLLSCTL寄存器的SSCGON=1/SS_TYPE=1)000000000:保留000000001:保留...000111111:保留001000000: CK_PLLVCO = CK_PLLVCOSRC x 64001000001: CK_PLLVCO = CK_PLLVCOSRC x 65...111110100: CK_PLLVCO = CK_PLLVCOSRC x 500111110101:保留...111111111:保留</td></tr><tr><td>5:0</td><td>PLLPSC[5:0]</td><td>PLL VCO源时钟分频器当PLL被关闭时由软件置位或清零。这些位域用做将PLL源时钟(CK_PLLSRC)分频生成PLL VCO源时钟(CK_PLLVCOSRC)、PLLSAI VCO源时钟(CK_PLLSAIVCOSRC)和PLLI2S VCO源时钟(CK_PLLI2SVCOSRC)。RCU_PLL寄存器的PLLSEL位对CK_PLLSRC时钟进行了描述。VCO源时钟频率范围必须在1MHz到2MHz之间000000:保留.000001:保留000010: CK_PLLSRC / 2000011: CK_PLLSRC / 3...111111: CK_PLLSRC / 63</td></tr></table>

## 5.3.3. 时钟配置寄存器 0（RCU_CFG0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CKOUT1SEL[1:0]</td><td colspan="3">CKOUT1DIV[2:0]</td><td colspan="3">CKOUT0DIV[2:0]</td><td>I2SSEL</td><td colspan="2">CKOUT0SEL[1:0]</td><td colspan="5">RTCDIV[4:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="2">保留</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="6">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CKOUT1SEL[1:0]</td><td>CKOUT1时钟源选择由软件置位或清零00:选择系统时钟01:选择CK_PLLI2SR时钟10:选择高速晶体振荡器时钟(HXTAL)11:选择CK_PLLP时钟</td></tr><tr><td>29:27</td><td>CKOUT1DIV[2:0]</td><td>CK_OUT1分频器,来降低CK_OUT1频率CK_OUT1时钟源的选择参考RCU_CFG0寄存器的31:30位0xx:CK_OUT1不分频100:CK_OUT1被2分频101:CK_OUT1被3分频110:CK_OUT1被4分频111:CK_OUT1被5分频</td></tr><tr><td>26:24</td><td>CKOUT0DIV[2:0]</td><td>CK_OUT0分频器,来降低CK_OUT0频率CK_OUT0时钟源的选择参考RCU_CFG0寄存器的22:21位0xx:CK_OUT0不分频100:CK_OUT0被2分频101:CK_OUT0被3分频110:CK_OUT0被4分频111:CK_OUT0被5分频</td></tr><tr><td>23</td><td>I2SSEL</td><td>I2S时钟源选择由软件置位或复位,控制I2S时钟源0:选择CK_PLLI2SR时钟作为I2S源时钟1:选择外部I2S_CKIN引脚输入信号作为I2S源时钟</td></tr><tr><td>22:21</td><td>CKOUT0SEL[1:0]</td><td>CKOUT0时钟源选择由软件置位或清零00:选择内部16M RC振荡器时钟01:选择低速晶体振荡器时钟(LXTAL)10:选择高速晶体振荡器时钟(HXTAL)11:选择CK_PLLP时钟</td></tr><tr><td>20:16</td><td>RTCDIV[4:0]</td><td>RTC时钟分频系数由软件置位或清零。这些位用作将HXTAL时钟分频生成RTC时钟(不超过1MHz)00000:无时钟00001:无时钟00010:CK_HXTAL/200011:CK_HXTAL/3...11111:CK_HXTAL/31</td></tr><tr><td>15:13</td><td>APB2PSC[2:0]</td><td>APB2预分频选择由软件置位或清零,控制APB2时钟分频因子。0xx:选择CK_AHB时钟不分频100:选择CK_AHB时钟2分频101:选择CK_AHB时钟4分频110:选择CK_AHB时钟8分频111:选择CK_AHB时钟16分频</td></tr><tr><td>12:10</td><td>APB1PSC[2:0]</td><td>APB1预分频选择由软件置位或清零,控制APB1时钟分频因子。0xx:选择CK_AHB时钟不分频100:选择CK_AHB时钟2分频101:选择CK_AHB时钟4分频110:选择CK_AHB时钟8分频111:选择CK_AHB时钟16分频</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB预分频选择由软件置位或清零,控制AHB时钟分频因子。0xxx:选择CK_SYS时钟不分频1000:选择CK_SYS时钟2分频1001:选择CK_SYS时钟4分频1010:选择CK_SYS时钟8分频1011:选择CK_SYS时钟16分频1100:选择CK_SYS时钟64分频1101:选择CK_SYS时钟128分频1110:选择CK_SYS时钟256分频1111:选择CK_SYS时钟512分频</td></tr><tr><td>3:2</td><td>SCSS[1:0]</td><td>系统时钟选择状态由硬件置位或清零,标识当前系统时钟的时钟源。00:选择CK_IRC16M时钟作为CK_SYS时钟源01:选择CK_HXTAL时钟作为CK_SYS时钟源10:选择CK_PLLP时钟作为CK_SYS时钟源11:保留</td></tr></table>

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>1:0</td><td>SCS[1:0]</td><td>系统时钟选择由软件配置选择系统时钟源。由于CK_SYS的改变存在固有的延迟,因此软件应当读SCSS位来确保时钟源切换是否结束。在从深度睡眠或待机模式中返回时,以及当HXTAL直接或间接作为系统时钟同时HXTAL时钟监视器检测到HXTAL故障时,强制选择IRC16M作为系统时钟。00:选择 CK_IRC16M 时钟作为 CK_SYS 时钟源01:选择 CK_HXTAL 时钟作为 CK_SYS 时钟源10:选择 CK_PLLP 时钟作为 CK_SYS 时钟源11:保留</td></tr></table>

## 5.3.4. 时钟中断寄存器（RCU_INT）

地址偏移：0x0C

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td>PLLSAISTBIC</td><td>PLLI2SSTBIC</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC16MSTBIC</td><td>LXTALSTBIC</td><td>IRC32KSTBIC</td></tr><tr><td colspan="8"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>PLLSAISTBIE</td><td>PLLI2SSTBIE</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC16MSTBIE</td><td>LXTALSTBIE</td><td>IRC32KSTBIE</td><td>CKMIF</td><td>PLLSAISTBIF</td><td>PLLI2SSTBIF</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC16MSTBIF</td><td>LXTALSTBIF</td><td>IRC32KSTBIF</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清零软件写1复位CKMIF标志位0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>PLLSAISTBIC</td><td>PLLSAI时钟稳定中断清零软件写1复位PLLSAISTBIF标志位0:不复位PLLSAISTBIF标志位1:复位PLLSAISTBIF标志位</td></tr><tr><td>21</td><td>PLLI2SSTBIC</td><td>PLLI2S时钟稳定中断清零软件写1复位PLLI2SSTBIF标志位0:不复位PLLI2SSTBIF标志位1:复位PLLI2SSTBIF标志位</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL时钟稳定中断清零软件写1复位PLLSTBIF标志位0:不复位PLLSTBIF标志位</td></tr></table>

<table><tr><td></td><td></td><td>1: 复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清零软件写1复位HXTALSTBIF标志位0: 不复位HXTALSTBIF标志位1: 复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>IRC16MSTBIC</td><td>IRC16M时钟稳定中断清零软件写1复位IRC16MSTBIF标志位0: 不复位IRC16MSTBIF标志位1: 复位IRC16MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清零软件写1复位LXTALSTBIF标志位0: 不复位LXTALSTBIF标志位1: 复位LXTALSTBIF标志位</td></tr><tr><td>16</td><td>IRC32KSTBIC</td><td>IRC32K时钟稳定中断清零软件写1复位IRC32KSTBIF标志位0: 不复位IRC32KSTBIF标志位1: 复位IRC32KSTBIF标志位</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>PLLSAISTBIE</td><td>PLLSAI时钟稳定中断使能软件置位和复位来使能/禁止PLLSAI时钟稳定中断0: 禁止PLLSAI时钟稳定中断1: 使能PLLSAI时钟稳定中断</td></tr><tr><td>13</td><td>PLLI2SSTBIE</td><td>PLLI2S时钟稳定中断使能软件置位和复位来使能/禁止PLLI2S时钟稳定中断0: 禁止PLLI2S时钟稳定中断1: 使能PLLI2S时钟稳定中断</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置位和复位来使能/禁止PLL时钟稳定中断0: 禁止PLL时钟稳定中断1: 使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置位和复位来使能/禁止HXTAL时钟稳定中断0: 禁止HXTAL时钟稳定中断1: 使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC16MSTBIE</td><td>IRC16M时钟稳定中断使能软件置位和复位来使能/禁止IRC16M时钟稳定中断0: 禁止IRC16M时钟稳定中断1: 使能IRC16M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能</td></tr></table>

<table><tr><td></td><td></td><td>软件置位和复位来使能/禁止LXTAL时钟稳定中断0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC32KSTBIE</td><td>IRC32K时钟稳定中断使能软件置位和复位来使能/禁止IRC32K时钟稳定中断0:禁止IRC32K时钟稳定中断1:使能IRC32K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟被阻塞时由硬件置位.软件置位CKMIC位时清除该位0:时钟正常运行1:HXTAL时钟阻塞</td></tr><tr><td>6</td><td>PLLSAISTBIF</td><td>PLLSAI时钟稳定中断标志位当PLLSAI时钟稳定且PLLSAISTBIE位被置1时由硬件置1软件置位PLLSAISTBIC位时清除该位0:无PLLSAI时钟稳定中断产生1:产生PLLSAI时钟稳定中断</td></tr><tr><td>5</td><td>PLLI2SSTBIF</td><td>PLLI2SI时钟稳定中断标志位当PLLI2S时钟稳定且PLLI2SSTBIE位被置1时由硬件置1软件置位PLLI2SSTBIC位时清除该位0:无PLLI2S时钟稳定中断产生1:产生PLLI2S时钟稳定中断</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1软件置位PLLSTBIC位时清除该位0:无PLL时钟稳定中断产生1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当高速4~32MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1软件置位HXTALSTBIC位时清除该位0:无HXTAL时钟稳定中断产生1:产生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC16MSTBIF</td><td>IRC16M时钟稳定中断标志位当内部16MHz RC振荡器时钟稳定且IRC16MSTBIE位被置1时由硬件置1软件置位IRC16MSTBIC位时清除该位0:无IRC16M时钟稳定中断产生1:产生IRC16M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当低速晶体振荡器时钟稳定且LXTALSTBIE位被置1时由硬件置1软件置位LXTALSTBIC位时清除该位0:无LXTAL时钟稳定中断产生1:产生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC32KSTBIF</td><td>IRC32K时钟稳定中断标志位当内部32kHz RC振荡器时钟稳定且IRC32KSTBIE位被置1时由硬件置1软件置位IRC32KSTBIC位时清除该位0:无IRC32K时钟稳定中断产生1:产生IRC32K时钟稳定中断</td></tr></table>

## 5.3.5. AHB1 复位寄存器（RCU_AHB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>USBHSRST</td><td colspan="3">保留</td><td>ENETRST</td><td>保留</td><td>IPARST</td><td>DMA1RST</td><td>DMA0RST</td><td colspan="5">保留</td></tr><tr><td colspan="2"></td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CRCRST</td><td colspan="3">保留</td><td>PIRST</td><td>PHRST</td><td>PGRST</td><td>PFRST</td><td>PERST</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td></tr><tr><td colspan="3"></td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>USBHSRST</td><td>USBHS 复位由软件置位或复位0:无作用1:复位 USBHS</td></tr><tr><td>28:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>ENETRST</td><td>Ethernet 复位由软件置位或复位0:无作用1:复位 ENET</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>IPARST</td><td>IPA 复位由软件置位或复位0:无作用1:复位 IPA</td></tr><tr><td>22</td><td>DMA1RST</td><td>DMA1 复位由软件置位或复位0:无作用</td></tr></table>

<table><tr><td>21</td><td>DMA0RST</td><td>DMA0 复位由软件置位或复位0:无作用1:复位 DMA0</td></tr><tr><td>20:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCRST</td><td>CRC 复位由软件置位或复位0:无作用1:复位 CRC</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>PIRST</td><td>GPIO 端口 I 复位由软件置位或复位0:无作用1:复位 GPIO 端口 I</td></tr><tr><td>7</td><td>PHRST</td><td>GPIO 端口 H 复位由软件置位或复位0:无作用1:复位 GPIO 端口 H</td></tr><tr><td>6</td><td>PGRST</td><td>GPIO 端口 G 复位由软件置位或复位0:无作用1:复位 GPIO 端口 G</td></tr><tr><td>5</td><td>PFRST</td><td>GPIO 端口 F 复位由软件置位或复位0:无作用1:复位 GPIO 端口 F</td></tr><tr><td>4</td><td>PERST</td><td>GPIO 端口 E 复位由软件置位或复位0:无作用1:复位 GPIO 端口 E</td></tr><tr><td>3</td><td>PDRST</td><td>GPIO 端口 D 复位由软件置位或复位0:无作用1:复位 GPIO 端口 D</td></tr><tr><td>2</td><td>PCRST</td><td>GPIO 端口 C 复位由软件置位或复位0:无作用</td></tr><tr><td>1</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>0</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr></table>

## 5.3.6. AHB2 复位寄存器（RCU_AHB2RST）

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>USBFSRST</td><td>TRNGRST</td><td>HAURST</td><td>CAURST</td><td>PKCAURST</td><td colspan="2">保留</td><td>DCIRST</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>USBFSRST</td><td>USBFS 复位由软件置位或复位0:无作用1:复位 USBFS</td></tr><tr><td>6</td><td>TRNGRST</td><td>TRNG 复位由软件置位或复位0:无作用1:复位 TRNG</td></tr><tr><td>5</td><td>HAURST</td><td>HAU 复位由软件置位或复位0:无作用1:复位 HAU</td></tr><tr><td>4</td><td>CAURST</td><td>CAU 复位由软件置位或复位0:无作用1: 复位 CAU</td></tr><tr><td>3</td><td>PKCAURST</td><td>PKCAURST 复位由软件置位或复位0: 无作用1: 复位 PKCAU</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>DCIRST</td><td>DCI 复位由软件置位或复位0: 无作用1: 复位 DCI</td></tr></table>

## 5.3.7. AHB3 复位寄存器（RCU_AHB3RST）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EXMCRST</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EXMCRST</td><td>EXMC 复位由软件置位或复位0:无作用1:复位 EXMC</td></tr></table>

## 5.3.8. APB1 复位寄存器（RCU_APB1RST）

地址偏移：0x20

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7RST</td><td>UART6RST</td><td>DACRST</td><td>PMURST</td><td>保留</td><td>CAN1RST</td><td>CAN0RST</td><td>保留</td><td>I2C2RST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>USART2RST</td><td>USART1RST</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2RST</td><td>SPI1RST</td><td>I2C5RST</td><td>I2C4RST</td><td>WWDGTRST</td><td>I2C3RST</td><td>保留</td><td>TIMER13RST</td><td>TIMER12RST</td><td>TIMER11RST</td><td>TIMER6RST</td><td>TIMER5RST</td><td>TIMER4RST</td><td>TIMER3RST</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UART7RST</td><td>UART7 复位由软件置位或复位0:无作用1:复位 UART7</td></tr><tr><td>30</td><td>UART6RST</td><td>UART6 复位由软件置位或复位0:无作用1:复位 UART6</td></tr><tr><td>29</td><td>DACRST</td><td>DAC 复位由软件置位或复位0:无作用1:复位 DAC</td></tr><tr><td>28</td><td>PMURST</td><td>PMU 复位由软件置位或复位0:无作用1:复位 PMU</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>CAN1RST</td><td>CAN1 复位由软件置位或复位0:无作用1:复位 CAN1</td></tr><tr><td>25</td><td>CAN0RST</td><td>CAN0 复位由软件置位或复位0:无作用1:复位 CAN0</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>I2C2RST</td><td>I2C2 复位由软件置位或复位0:无作用1:复位 I2C2</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1 复位由软件置位或复位0:无作用1:复位 I2C1</td></tr></table>

<table><tr><td>21</td><td>I2C0RST</td><td>I2C0 复位由软件置位或复位0:无作用1:复位 I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4 复位由软件置位或复位0:无作用1:复位 UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3 复位由软件置位或复位0:无作用1:复位 UART3</td></tr><tr><td>18</td><td>USART2RST</td><td>USART2 复位由软件置位或复位0:无作用1:复位 USART2</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1 复位由软件置位或复位0:无作用1:复位 USART1</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2RST</td><td>SPI2 复位由软件置位或复位0:无作用1:复位 SPI2</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1 复位由软件置位或复位0:无作用1:复位 SPI1</td></tr><tr><td>13</td><td>I2C5RST</td><td>I2C5 复位由软件置位或复位0:无作用1:复位 I2C5</td></tr><tr><td>12</td><td>I2C4RST</td><td>I2C4 复位由软件置位或复位0:无作用1:复位 I2C4</td></tr><tr><td>11</td><td>WWDGTRST</td><td>WWDGT 复位由软件置位或复位</td></tr></table>

0: 无作用
1: 复位 WWDGT

10 I2C3RST I2C3 复位
由软件置位或复位
0: 无作用
1: 复位 I2C3

9 保留 必须保持复位值。

8 TIMER13RST TIMER13 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER13

7 TIMER12RST TIMER12 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER12

6 TIMER11RST TIMER11 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER11

5 TIMER6RST TIMER6 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER6

4 TIMER5RST TIMER5 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER5

3 TIMER4RST TIMER4 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER4

2 TIMER3RST TIMER3 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER3

1 TIMER2RST TIMER2 复位
由软件置位或复位
0: 无作用
1: 复位 TIMER2

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>0</td><td>TIMER1RST</td><td>TIMER1 复位由软件置位或复位0:无作用1:复位 TIMER1</td></tr></table>

## 5.3.9. APB2 复位寄存器（RCU_APB2RST）

地址偏移：0x24

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>TLIRST</td><td colspan="3">保留</td><td>SAIRST</td><td>SPI5RST</td><td>SPI4RST</td><td>保留</td><td>TIMER10RST</td><td>TIMER9RST</td><td>TIMER8RST</td></tr><tr><td colspan="9">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SYSCFGRST</td><td>SPI3RST</td><td>SPI0RST</td><td>SDIORST</td><td colspan="2">保留</td><td>ADCRST</td><td colspan="2">保留</td><td>USART5RST</td><td>USART0RST</td><td colspan="2">保留</td><td>TIMER7RST</td><td>TIMER0RST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TLIRST</td><td>TLI 复位由软件置位或复位0:无作用1:复位 TLI</td></tr><tr><td>25:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>SAIRST</td><td>SAI 复位由软件置位或复位0:无作用1:复位 SAI</td></tr><tr><td>21</td><td>SPI5RST</td><td>SPI5 复位由软件置位或复位0:无作用1:复位 SPI5</td></tr><tr><td>20</td><td>SPI4RST</td><td>SPI4 复位由软件置位或复位0:无作用1:复位 SPI4</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>TIMER10RST</td><td>TIMER10 复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位 TIMER10</td></tr><tr><td>17</td><td>TIMER9RST</td><td>TIMER9 复位由软件置位或复位0:无作用1:复位 TIMER9</td></tr><tr><td>16</td><td>TIMER8RST</td><td>TIMER8 复位由软件置位或复位0:无作用1:复位 TIMER8</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SYSCFGRST</td><td>SYSCFG 复位由软件置位或复位0:无作用1:复位 SYSCFG</td></tr><tr><td>13</td><td>SPI3RST</td><td>SPI3 复位由软件置位或复位0:无作用1:复位 SPI3</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0 复位由软件置位或复位0:无作用1:复位 SPI0</td></tr><tr><td>11</td><td>SDIORST</td><td>SDIO 复位由软件置位或复位0:无作用1:复位 SDIO</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>ADCRST</td><td>ADC 复位由软件置位或复位0:无作用1:复位所有 ADC</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5RST</td><td>USART5 复位由软件置位或复位0:无作用1:复位 USART5</td></tr></table>

<table><tr><td>4</td><td>USART0RST</td><td>USART0 复位由软件置位或复位0:无作用1:复位 USART0</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER7RST</td><td>TIMER7 复位由软件置位或复位0:无作用1:复位 TIMER7</td></tr><tr><td>0</td><td>TIMER0RST</td><td>TIMER0 复位由软件置位或复位0:无作用1:复位 TIMER0</td></tr></table>

## 5.3.10. AHB1 使能寄存器（RCU_AHB1EN）

地址偏移：0x30

复位值：0x0010 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>USBHSULPIEN</td><td>USBHSEN</td><td>ENETPTPEN</td><td>ENETRXEN</td><td>ENETTXEN</td><td>ENETEN</td><td>保留</td><td>IPAEN</td><td>DMA1EN</td><td>DMA0EN</td><td>TCMSRAMEN</td><td>保留</td><td>BKPSRAMEN</td><td colspan="2">保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CRCEN</td><td colspan="3">保留</td><td>PIEN</td><td>PHEN</td><td>PGEN</td><td>PFEN</td><td>PEEN</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td></tr><tr><td colspan="3"></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>USBHSULPIEN</td><td>USBHS ULPI 时钟使能由软件置位或复位0: 关闭 USBHS ULPI 时钟1: 开启 USBHS ULPI 时钟</td></tr><tr><td>29</td><td>USBHSEN</td><td>USBHS 时钟使能由软件置位或复位0: 关闭 USBHS 时钟1: 开启 USBHS 时钟</td></tr><tr><td>28</td><td>ENETPTPEN</td><td>以太网 PTP 时钟使能由软件置位或复位0: 关闭以太网 PTP 时钟</td></tr></table>

<table><tr><td></td><td></td><td>1:开启以太网PTP时钟</td></tr><tr><td>27</td><td>ENETRXEN</td><td>以太网RX时钟使能由软件置位或复位0:关闭以太网RX时钟1:开启以太网RX时钟</td></tr><tr><td>26</td><td>ENETTXEN</td><td>以太网TX时钟使能由软件置位或复位0:关闭以太网TX时钟1:开启以太网TX时钟</td></tr><tr><td>25</td><td>ENETEN</td><td>以太网时钟使能由软件置位或复位0:关闭以太网时钟1:开启以太网时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>IPAEN</td><td>IPA时钟使能由软件置位或复位0:关闭IPA时钟1:开启IPA时钟</td></tr><tr><td>22</td><td>DMA1EN</td><td>DMA1时钟使能由软件置位或复位0:关闭DMA1时钟1:开启DMA1时钟</td></tr><tr><td>21</td><td>DMA0EN</td><td>DMA0时钟使能由软件置位或复位0:关闭DMA0时钟1:开启DMA0时钟</td></tr><tr><td>20</td><td>TCMSRAMEN</td><td>TCMSRAM时钟使能由软件置位或复位0:关闭TCMSRAM时钟1:开启TCMSRAM时钟</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>BKPSRAMEN</td><td>BKPSRAM时钟使能由软件置位或复位0:关闭BKPSRAM时钟1:开启BKPSRAM时钟</td></tr><tr><td>17:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCEN</td><td>CRC时钟使能由软件置位或复位0: 关闭 CRC 时钟1: 开启 CRC 时钟</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>PIEN</td><td>GPIO 端口 I 时钟使能由软件置位或复位0: 关闭 GPIO 端口 I 时钟1: 开启 GPIO 端口 I 时钟</td></tr><tr><td>7</td><td>PHEN</td><td>GPIO 端口 H 时钟使能由软件置位或复位0: 关闭 GPIO 端口 H 时钟1: 开启 GPIO 端口 H 时钟</td></tr><tr><td>6</td><td>PGEN</td><td>GPIO 端口 G 时钟使能由软件置位或复位0: 关闭 GPIO 端口 G 时钟1: 开启 GPIO 端口 G 时钟</td></tr><tr><td>5</td><td>PFEN</td><td>GPIO 端口 F 时钟使能由软件置位或复位0: 关闭 GPIO 端口 F 时钟1: 开启 GPIO 端口 F 时钟</td></tr><tr><td>4</td><td>PEEN</td><td>GPIO 端口 E 时钟使能由软件置位或复位0: 关闭 GPIO 端口 E 时钟1: 开启 GPIO 端口 E 时钟</td></tr><tr><td>3</td><td>PDEN</td><td>GPIO 端口 D 时钟使能由软件置位或复位0: 关闭 GPIO 端口 D 时钟1: 开启 GPIO 端口 D 时钟</td></tr><tr><td>2</td><td>PCEN</td><td>GPIO 端口 C 时钟使能由软件置位或复位0: 关闭 GPIO 端口 C 时钟1: 开启 GPIO 端口 C 时钟</td></tr><tr><td>1</td><td>PBEN</td><td>GPIO 端口 B 时钟使能由软件置位或复位0: 关闭 GPIO 端口 B 时钟1: 开启 GPIO 端口 B 时钟</td></tr><tr><td>0</td><td>PAEN</td><td>GPIO 端口 A 时钟使能由软件置位或复位0: 关闭 GPIO 端口 A 时钟1: 开启 GPIO 端口 A 时钟</td></tr></table>

## 5.3.11. AHB2 使能寄存器（RCU_AHB2EN）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">Reserved</td></tr></table>

<table><tr><td colspan="7">Reserved</td><td>USBFSEN</td><td>TRNGEN</td><td>HAUEN</td><td>CAUEN</td><td>PKCAUEN</td><td>Reserved</td><td>DCIEN</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>USBFSEN</td><td>USBFS时钟使能由软件置位或复位0:关闭USBFS时钟1:开启USBFS时钟</td></tr><tr><td>6</td><td>TRNGEN</td><td>TRNG时钟使能由软件置位或复位0:关闭TRNG时钟1:开启TRNG时钟</td></tr><tr><td>5</td><td>HAUEN</td><td>HAU时钟使能由软件置位或复位0:关闭HAU时钟1:开启HAU时钟</td></tr><tr><td>4</td><td>CAUEN</td><td>CAU时钟使能由软件置位或复位0:关闭CAU时钟1:开启CAU时钟</td></tr><tr><td>3</td><td>PKCAUEN</td><td>PKCAU时钟使能由软件置位或复位0:关闭PKCAU时钟1:开启PKCAU时钟</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>DCIEN</td><td>DCI时钟使能由软件置位或复位0:关闭DCI时钟1:开启DCI时钟</td></tr></table>

## 5.3.12. AHB3 使能寄存器（RCU_AHB3EN）

地址偏移：0x38

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EXMCEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EXMCEN</td><td>EXMC时钟使能由软件置位或复位0:关闭EXMC时钟1:开启EXMC时钟</td></tr></table>

## 5.3.13. APB1 使能寄存器（RCU_APB1EN）

地址偏移：0x40

复位值：0x0000 0000


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7EN</td><td>UART6EN</td><td>DACEN</td><td>PMUEN</td><td>Reserved</td><td>CAN1EN</td><td>CAN0EN</td><td>Reserved</td><td>I2C2EN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>USART2EN</td><td>USART1EN</td><td>Reserved</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2EN</td><td>SPI1EN</td><td>I2C5EN</td><td>I2C4EN</td><td>WWDGTEN</td><td>I2C3EN</td><td>Reserved</td><td>TIMER13EN</td><td>TIMER12EN</td><td>TIMER11EN</td><td>TIMER6EN</td><td>TIMER5EN</td><td>TIMER4EN</td><td>TIMER3EN</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UART7EN</td><td>UART7 时钟使能由软件置位或复位0: 关闭 UART7 时钟1: 开启 UART7 时钟</td></tr><tr><td>30</td><td>UART6EN</td><td>UART6 时钟使能由软件置位或复位0: 关闭 UART6 时钟</td></tr></table>

<table><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置位或复位0:关闭DAC时钟1:开启DAC时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置位或复位0:关闭PMU时钟1:开启PMU时钟</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>CAN1EN</td><td>CAN1时钟使能由软件置位或复位0:关闭CAN1时钟1:开启CAN1时钟</td></tr><tr><td>25</td><td>CAN0EN</td><td>CAN0时钟使能由软件置位或复位0:关闭CAN0时钟1:开启CAN0时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>I2C2EN</td><td>I2C2时钟使能由软件置位或复位0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置位或复位0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置位或复位0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置位或复位0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置位或复位0:关闭UART3时钟</td></tr><tr><td>18</td><td>USART2EN</td><td>USART2时钟使能由软件置位或复位0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置位或复位0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2EN</td><td>SPI2时钟使能由软件置位或复位0:关闭SPI2时钟1:开启SPI2时钟</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置位或复位0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13</td><td>I2C5EN</td><td>I2C5时钟使能由软件置位或复位0:关闭I2C5时钟1:开启I2C5时钟</td></tr><tr><td>12</td><td>I2C4EN</td><td>I2C4时钟使能由软件置位或复位0:关闭I2C4时钟1:开启I2C4时钟</td></tr><tr><td>11</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置位或复位0:关闭WWDGT时钟1:开启WWDGT时钟</td></tr><tr><td>10</td><td>I2C3EN</td><td>I2C3时钟使能由软件置位或复位0:关闭I2C3时钟1:开启I2C3时钟</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13EN</td><td>TIMER13时钟使能由软件置位或复位0:关闭TIMER13时钟</td></tr><tr><td>7</td><td>TIMER12EN</td><td>TIMER12时钟使能由软件置位或复位0:关闭 TIMER12 时钟1:开启 TIMER12 时钟</td></tr><tr><td>6</td><td>TIMER11EN</td><td>TIMER11时钟使能由软件置位或复位0:关闭 TIMER11 时钟1:开启 TIMER11 时钟</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6时钟使能由软件置位或复位0:关闭 TIMER6 时钟1:开启 TIMER6 时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5时钟使能由软件置位或复位0:关闭 TIMER5 时钟1:开启 TIMER5 时钟</td></tr><tr><td>3</td><td>TIMER4EN</td><td>TIMER4时钟使能由软件置位或复位0:关闭 TIMER4 时钟1:开启 TIMER4 时钟</td></tr><tr><td>2</td><td>TIMER3EN</td><td>TIMER3时钟使能由软件置位或复位0:关闭 TIMER3 时钟1:开启 TIMER3 时钟</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2时钟使能由软件置位或复位0:关闭 TIMER2 时钟1:开启 TIMER2 时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1时钟使能由软件置位或复位0:关闭 TIMER1 时钟1:开启 TIMER1 时钟</td></tr></table>

## 5.3.14. APB2 使能寄存器（RCU_APB2EN）

地址偏移：0x44

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>TLIEN</td><td colspan="3">保留</td><td>SAIEN</td><td>SPI5EN</td><td>SPI4EN</td><td>保留</td><td>TIMER10EN</td><td>TIMER9EN</td><td>TIMER8EN</td></tr><tr><td colspan="5"></td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SYSCFGEN</td><td>SPI3EN</td><td>SPI0EN</td><td>SDIOEN</td><td>ADC2EN</td><td>ADC1EN</td><td>ADC0EN</td><td colspan="2">保留</td><td>USART5EN</td><td>USART0EN</td><td colspan="2">保留</td><td>TIMER7EN</td><td>TIMER0EN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TLIEN</td><td>TLI时钟使能由软件置位或复位0:关闭TLI时钟1:开启TLI时钟</td></tr><tr><td>25:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>SAIEN</td><td>SAI时钟使能由软件置位或复位0:关闭SAI时钟1:开启SAI时钟</td></tr><tr><td>21</td><td>SPI5EN</td><td>SPI5时钟使能由软件置位或复位0:关闭SPI5时钟1:开启SPI5时钟</td></tr><tr><td>20</td><td>SPI4EN</td><td>SPI4时钟使能由软件置位或复位0:关闭SPI4时钟1:开启SPI4时钟</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>TIMER10EN</td><td>TIMER10时钟使能由软件置位或复位0:关闭TIMER10时钟1:开启TIMER10时钟</td></tr><tr><td>17</td><td>TIMER9EN</td><td>TIMER9时钟使能由软件置位或复位0:关闭TIMER9时钟1:开启TIMER9时钟</td></tr><tr><td>16</td><td>TIMER8EN</td><td>TIMER8时钟使能由软件置位或复位0:关闭TIMER8时钟</td></tr></table>

<table><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SYSCFGEN</td><td>SYSCFG时钟使能由软件置位或复位0:关闭SYSCFG时钟1:开启SYSCFG时钟</td></tr><tr><td>13</td><td>SPI3EN</td><td>SPI3时钟使能由软件置位或复位0:关闭SPI3时钟1:开启SPI3时钟</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0时钟使能由软件置位或复位0:关闭SPI0时钟1:开启SPI0时钟</td></tr><tr><td>11</td><td>SDIOEN</td><td>SDIO时钟使能由软件置位或复位0:关闭SDIO时钟1:开启SDIO时钟</td></tr><tr><td>10</td><td>ADC2EN</td><td>ADC2时钟使能由软件置位或复位0:关闭ADC2时钟1:开启ADC2时钟</td></tr><tr><td>9</td><td>ADC1EN</td><td>ADC1时钟使能由软件置位或复位0:关闭ADC1时钟1:开启ADC1时钟</td></tr><tr><td>8</td><td>ADC0EN</td><td>ADC0时钟使能由软件置位或复位0:关闭ADC0时钟1:开启ADC0时钟</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5EN</td><td>USART5时钟使能由软件置位或复位0:关闭USART5时钟1:开启USART5时钟</td></tr><tr><td>4</td><td>USART0EN</td><td>USART0时钟使能由软件置位或复位0:关闭USART0时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER7EN</td><td>TIMER7 时钟使能由软件置位或复位0:关闭 TIMER7 时钟1:开启 TIMER7 时钟</td></tr><tr><td>0</td><td>TIMER0EN</td><td>TIMER0 时钟使能由软件置位或复位0:关闭 TIMER0 时钟1:开启 TIMER0 时钟</td></tr></table>

## 5.3.15. AHB1 睡眠模式使能寄存器（RCU_AHB1SPEN）

地址偏移：0x50

复位值：0x7EEF 91FF

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>USBHSULPISPEN</td><td>USBHSSPEN</td><td>ENETPTSPEN</td><td>ENETRXSPEN</td><td>ENETTXSPEN</td><td>ENETSPEN</td><td>保留</td><td>IPASPEN</td><td>DMA1SPEN</td><td>DMA0SPEN</td><td>保留</td><td>SRAM2SPEN</td><td>BKPSRAMSPEN</td><td>SRAM1SPEN</td><td>SRAM0SPEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FMCSPEN</td><td colspan="2">保留</td><td>CRCSPEN</td><td colspan="3">保留</td><td>PISPEN</td><td>PHSPEN</td><td>PGSPEN</td><td>PFSPEN</td><td>PESPEN</td><td>PDSPEN</td><td>PCSPEN</td><td>PBSPEN</td><td>PASPEN</td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>USBHSULPISPEN</td><td>在睡眠模式下 USBHS ULPI 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USBHS ULPI 时钟1: 在睡眠模式下开启 USBHS ULPI 时钟</td></tr><tr><td>29</td><td>USBHSSPEN</td><td>在睡眠模式下 USBHS 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USBHS 时钟1: 在睡眠模式下开启 USBHS 时钟</td></tr><tr><td>28</td><td>ENETPTPSPEN</td><td>在睡眠模式下以太网 PTP 时钟使能由软件置位或复位0: 在睡眠模式下关闭以太网 PTP 时钟1: 在睡眠模式下开启以太网 PTP 时钟</td></tr><tr><td>27</td><td>ENETRXSPEN</td><td>在睡眠模式下以太网 RX 时钟使能由软件置位或复位</td></tr></table>

0: 在睡眠模式下关闭以太网 RX 时钟
1: 在睡眠模式下开启以太网 RX 时钟

26 ENETTXSPEN 在睡眠模式下以太网 TX 时钟使能由软件置位或复位
0: 在睡眠模式下关闭以太网 TX 时钟
1: 在睡眠模式下开启以太网 TX 时钟

25 ENETSPEN 在睡眠模式下以太网时钟使能由软件置位或复位
0: 在睡眠模式下关闭以太网时钟
1: 在睡眠模式下开启以太网时钟

24 保留 必须保持复位值。

23 IPASPEN 在睡眠模式下 IPA 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 IPA 时钟
1: 在睡眠模式下开启 IPA 时钟

22 DMA1SPEN 在睡眠模式下 DMA1 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 DMA1 时钟
1: 在睡眠模式下开启 DMA1 时钟

21 DMA0SPEN 在睡眠模式下 DMA0 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 DMA0 时钟
1: 在睡眠模式下开启 DMA0 时钟

20 保留 必须保持复位值。

19 SRAM2SPEN 在睡眠模式下 SRAM2 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 SRAM2 时钟
1: 在睡眠模式下开启 SRAM2 时钟

18 BKPSRAMSPEN 在睡眠模式下 BKPSRAM 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 BKPSRAM 时钟
1: 在睡眠模式下开启 BKPSRAM 时钟

17 SRAM1SPEN 在睡眠模式下 SRAM1 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 SRAM1 时钟
1: 在睡眠模式下开启 SRAM1 时钟

16 SRAM0SPEN 在睡眠模式下 SRAM0 时钟使能由软件置位或复位
0: 在睡眠模式下关闭 SRAM0 时钟

<table><tr><td></td><td></td><td>1:在睡眠模式下开启SRAM0时钟</td></tr><tr><td>15</td><td>FMCSPEN</td><td>在睡眠模式下FMC时钟使能由软件置位或复位0:在睡眠模式下关闭FMC时钟1:在睡眠模式下开启FMC时钟</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCSPEN</td><td>在睡眠模式下CRC时钟使能由软件置位或复位0:在睡眠模式下关闭CRC时钟1:在睡眠模式下开启CRC时钟</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>PISPEN</td><td>在睡眠模式下GPIO端口I时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口I时钟1:在睡眠模式下开启GPIO端口I时钟</td></tr><tr><td>7</td><td>PHSPEN</td><td>在睡眠模式下GPIO端口H时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口H时钟1:在睡眠模式下开启GPIO端口H时钟</td></tr><tr><td>6</td><td>PGSPEN</td><td>在睡眠模式下GPIO端口G时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口G时钟1:在睡眠模式下开启GPIO端口G时钟</td></tr><tr><td>5</td><td>PFSPEN</td><td>在睡眠模式下GPIO端口F时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口F时钟1:在睡眠模式下开启GPIO端口F时钟</td></tr><tr><td>4</td><td>PESPEN</td><td>在睡眠模式下GPIO端口E时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口E时钟1:在睡眠模式下开启GPIO端口E时钟</td></tr><tr><td>3</td><td>PDSPEN</td><td>在睡眠模式下GPIO端口D时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口D时钟1:在睡眠模式下开启GPIO端口D时钟</td></tr><tr><td>2</td><td>PCSPEN</td><td>在睡眠模式下GPIO端口C时钟使能由软件置位或复位0:在睡眠模式下关闭GPIO端口C时钟1: 在睡眠模式下开启 GPIO 端口 C 时钟</td></tr><tr><td>1</td><td>PBSPEN</td><td>在睡眠模式下 GPIO 端口 B 时钟使能由软件置位或复位0: 在睡眠模式下关闭 GPIO 端口 B 时钟1: 在睡眠模式下开启 GPIO 端口 B 时钟</td></tr><tr><td>0</td><td>PASPEN</td><td>在睡眠模式下 GPIO 端口 A 时钟使能由软件置位或复位0: 在睡眠模式下关闭 GPIO 端口 A 时钟1: 在睡眠模式下开启 GPIO 端口 A 时钟</td></tr></table>

## 5.3.16. AHB2 睡眠模式使能寄存器（RCU_AHB2SPEN）

地址偏移：0x54

复位值：0x0000 00F9

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>USBFSS PEN</td><td>TRNGSP EN</td><td>HAUSPE N</td><td>CAUSPEN</td><td>PKCAUSP EN</td><td colspan="2">保留</td><td>DCISPEN</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>USBFSSPEN</td><td>在睡眠模式下 USBFS 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USBFS 时钟1: 在睡眠模式下开启 USBFS 时钟</td></tr><tr><td>6</td><td>TRNGSPEN</td><td>在睡眠模式下 TRNG 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TRNG 时钟1: 在睡眠模式下开启 TRNG 时钟</td></tr><tr><td>5</td><td>HAUSPEN</td><td>在睡眠模式下 HAU 时钟使能由软件置位或复位0: 在睡眠模式下关闭 HAU 时钟1: 在睡眠模式下开启 HAU 时钟</td></tr><tr><td>4</td><td>CAUSPEN</td><td>在睡眠模式下 CAU 时钟使能由软件置位或复位0: 在睡眠模式下关闭 CAU 时钟</td></tr></table>

<table><tr><td>3</td><td>PKCAUSPEN</td><td>在睡眠模式下 PKCAU 时钟使能由软件置位或复位0: 在睡眠模式下关闭 PKCAU 时钟1: 在睡眠模式下开启 PKCAU 时钟</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>DCISPEN</td><td>在睡眠模式下 DCI 时钟使能由软件置位或复位0: 在睡眠模式下关闭 DCI 时钟1: 在睡眠模式下开启 DCI 时钟</td></tr></table>

## 5.3.17. AHB3 睡眠模式使能寄存器（RCU_AHB3SPEN）

地址偏移：0x58

复位值：0x0000 0001


This register can be accessed by byte(8-bit), half-word(16-bit) and word(32-bit).


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EXMCSPEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EXMCSPEN</td><td>在睡眠模式下 EXMC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 EXMC 时钟1: 在睡眠模式下开启 EXMC 时钟</td></tr></table>

## 5.3.18. APB1 睡眠模式使能寄存器（RCU_APB1SPEN）

地址偏移：0x60

复位值：0xF6FE FDFF


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UART7SPEN</td><td>UART6SPEN</td><td>DACSPEN</td><td>PMUSPEN</td><td>保留</td><td>CAN1SPEN</td><td>CAN0SPEN</td><td>保留</td><td>I2C2SPEN</td><td>I2C1SPEN</td><td>I2C0SPEN</td><td>UART4SPEN</td><td>UART3SPEN</td><td>USART2SPEN</td><td>USART1SPEN</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SPI2SPEN</td><td>SPI1SPEN</td><td>I2C5SPEN</td><td>I2C4SPEN</td><td>WWDGTSPEN</td><td>I2C3SPEN</td><td>保留</td><td>TIMER13SPEN</td><td>TIMER12SPEN</td><td>TIMER11SPEN</td><td>TIMER6SPEN</td><td>TIMER5SPEN</td><td>TIMER4SPEN</td><td>TIMER3SPEN</td><td>TIMER2SPEN</td><td>TIMER1SPEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UART7SPEN</td><td>在睡眠模式下 UART7 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART7 时钟1: 在睡眠模式下开启 UART7 时钟</td></tr><tr><td>30</td><td>UART6SPEN</td><td>在睡眠模式下 UART6 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART6 时钟1: 在睡眠模式下开启 UART6 时钟</td></tr><tr><td>29</td><td>DACSPEN</td><td>在睡眠模式下 DAC 时钟使能由软件置位或复位0: 在睡眠模式下关闭 DAC 时钟1: 在睡眠模式下开启 DAC 时钟</td></tr><tr><td>28</td><td>PMUSPEN</td><td>在睡眠模式下 PMU 时钟使能由软件置位或复位0: 在睡眠模式下关闭 PMU 时钟1: 在睡眠模式下开启 PMU 时钟</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>CAN1SPEN</td><td>在睡眠模式下 CAN1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 CAN1 时钟1: 在睡眠模式下开启 CAN1 时钟</td></tr><tr><td>25</td><td>CAN0SPEN</td><td>在睡眠模式下 CAN0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 CAN0 时钟1: 在睡眠模式下开启 CAN0 时钟</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>I2C2SPEN</td><td>在睡眠模式下 I2C2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C2 时钟1: 在睡眠模式下开启 I2C2 时钟</td></tr><tr><td>22</td><td>I2C1SPEN</td><td>在睡眠模式下 I2C1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C1 时钟1: 在睡眠模式下开启 I2C1 时钟</td></tr></table>

<table><tr><td>21</td><td>I2C0SPEN</td><td>在睡眠模式下 I2C0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C0 时钟1: 在睡眠模式下开启 I2C0 时钟</td></tr><tr><td>20</td><td>UART4SPEN</td><td>在睡眠模式下 UART4 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART4 时钟1: 在睡眠模式下开启 UART4 时钟</td></tr><tr><td>19</td><td>UART3SPEN</td><td>在睡眠模式下 UART3 时钟使能由软件置位或复位0: 在睡眠模式下关闭 UART3 时钟1: 在睡眠模式下开启 UART3 时钟</td></tr><tr><td>18</td><td>USART2SPEN</td><td>在睡眠模式下 USART2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART2 时钟1: 在睡眠模式下开启 USART2 时钟</td></tr><tr><td>17</td><td>USART1SPEN</td><td>在睡眠模式下 USART1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART1 时钟1: 在睡眠模式下开启 USART1 时钟</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>SPI2SPEN</td><td>在睡眠模式下 SPI2 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI2 时钟1: 在睡眠模式下开启 SPI2 时钟</td></tr><tr><td>14</td><td>SPI1SPEN</td><td>在睡眠模式下 SPI1 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI1 时钟1: 在睡眠模式下开启 SPI1 时钟</td></tr><tr><td>13</td><td>I2C5SPEN</td><td>在睡眠模式下 I2C5 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C5 时钟1: 在睡眠模式下开启 I2C5 时钟</td></tr><tr><td>12</td><td>I2C4SPEN</td><td>在睡眠模式下 I2C4 时钟使能由软件置位或复位0: 在睡眠模式下关闭 I2C4 时钟1: 在睡眠模式下开启 I2C4 时钟</td></tr><tr><td>11</td><td>WWDGTSPEN</td><td>在睡眠模式下 WWDGT 时钟使能由软件置位或复位0:在睡眠模式下关闭WWDGT时钟1:在睡眠模式下开启WWDGT时钟</td></tr><tr><td>10</td><td>I2C3SPEN</td><td>在睡眠模式下I2C3时钟使能由软件置位或复位0:在睡眠模式下关闭I2C3时钟1:在睡眠模式下开启I2C3时钟</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13SPEN</td><td>在睡眠模式下TIMER13时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER13时钟1:在睡眠模式下开启TIMER13时钟</td></tr><tr><td>7</td><td>TIMER12SPEN</td><td>在睡眠模式下TIMER12时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER12时钟1:在睡眠模式下开启TIMER12时钟</td></tr><tr><td>6</td><td>TIMER11SPEN</td><td>在睡眠模式下TIMER11时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER11时钟1:在睡眠模式下开启TIMER11时钟</td></tr><tr><td>5</td><td>TIMER6SPEN</td><td>在睡眠模式下TIMER6时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER6时钟1:在睡眠模式下开启TIMER6时钟</td></tr><tr><td>4</td><td>TIMER5SPEN</td><td>在睡眠模式下TIMER5时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER5时钟1:在睡眠模式下开启TIMER5时钟</td></tr><tr><td>3</td><td>TIMER4SPEN</td><td>在睡眠模式下TIMER4时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER4时钟1:在睡眠模式下开启TIMER4时钟</td></tr><tr><td>2</td><td>TIMER3SPEN</td><td>在睡眠模式下TIMER3时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER3时钟1:在睡眠模式下开启TIMER3时钟</td></tr><tr><td>1</td><td>TIMER2SPEN</td><td>在睡眠模式下TIMER2时钟使能由软件置位或复位0:在睡眠模式下关闭TIMER2时钟1:在睡眠模式下开启TIMER2时钟</td></tr></table>

0：在睡眠模式下关闭 TIMER1 时钟

1：在睡眠模式下开启 TIMER1 时钟

## 5.3.19. APB2 睡眠模式使能寄存器（RCU_APB2SPEN）

地址偏移：0x64

复位值：0x0477 7F33

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>TLISPEN</td><td colspan="3">保留</td><td>SAISPEN</td><td>SPI5SPEN</td><td>SPI4SPEN</td><td>保留</td><td>TIMER10SPEN</td><td>TIMER9SPEN</td><td>TIMER8SPEN</td></tr><tr><td colspan="5"></td><td colspan="4">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SYSCFGSPEN</td><td>SPI3SPEN</td><td>SPI0SPEN</td><td>SDIOSPEN</td><td>ADC2SPEN</td><td>ADC1SPEN</td><td>ADC0SPEN</td><td colspan="2">保留</td><td>USART5SPEN</td><td>USART0SPEN</td><td colspan="2">保留</td><td>TIMER7SPEN</td><td>TIMER0SPEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TLISPEN</td><td>在睡眠模式下 TLI 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TLI 时钟1: 在睡眠模式下开启 TLI 时钟</td></tr><tr><td>25:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>SAISPEN</td><td>在睡眠模式下 SAI 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SAI 时钟1: 在睡眠模式下开启 SAI 时钟</td></tr><tr><td>21</td><td>SPI5SPEN</td><td>在睡眠模式下 SPI5 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI5 时钟1: 在睡眠模式下开启 SPI5 时钟</td></tr><tr><td>20</td><td>SPI4SPEN</td><td>在睡眠模式下 SPI4 时钟使能由软件置位或复位0: 在睡眠模式下关闭 SPI4 时钟1: 在睡眠模式下开启 SPI4 时钟</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>TIMER10SPEN</td><td>在睡眠模式下 TIMER10 时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:在睡眠模式下关闭 TIMER10 时钟1:在睡眠模式下开启 TIMER10 时钟</td></tr><tr><td>17</td><td>TIMER9SPEN</td><td>在睡眠模式下 TIMER9 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER9 时钟1:在睡眠模式下开启 TIMER9 时钟</td></tr><tr><td>16</td><td>TIMER8SPEN</td><td>在睡眠模式下 TIMER8 时钟使能由软件置位或复位0:在睡眠模式下关闭 TIMER8 时钟1:在睡眠模式下开启 TIMER8 时钟</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>14</td><td>SYSCFGSPEN</td><td>在睡眠模式下 SYSCFG 时钟使能由软件置位或复位0:在睡眠模式下关闭 SYSCFG 时钟1:在睡眠模式下开启 SYSCFG 时钟</td></tr><tr><td>13</td><td>SPI3SPEN</td><td>在睡眠模式下 SPI3 时钟使能由软件置位或复位0:在睡眠模式下关闭 SPI3 时钟1:在睡眠模式下开启 SPI3 时钟</td></tr><tr><td>12</td><td>SPI0SPEN</td><td>在睡眠模式下 SPI0 时钟使能由软件置位或复位0:在睡眠模式下关闭 SPI0 时钟1:在睡眠模式下开启 SPI0 时钟</td></tr><tr><td>11</td><td>SDIOSPEN</td><td>在睡眠模式下 SDIO 时钟使能由软件置位或复位0:在睡眠模式下关闭 SDIO 时钟1:在睡眠模式下开启 SDIO 时钟</td></tr><tr><td>10</td><td>ADC2SPEN</td><td>在睡眠模式下 ADC2 时钟使能由软件置位或复位0:在睡眠模式下关闭 ADC2 时钟1:在睡眠模式下开启 ADC2 时钟</td></tr><tr><td>9</td><td>ADC1SPEN</td><td>在睡眠模式下 ADC1 时钟使能由软件置位或复位0:在睡眠模式下关闭 ADC1 时钟1:在睡眠模式下开启 ADC1 时钟</td></tr><tr><td>8</td><td>ADC0SPEN</td><td>在睡眠模式下 ADC0 时钟使能由软件置位或复位0:在睡眠模式下关闭 ADC0 时钟</td></tr></table>

<table><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>USART5SPEN</td><td>在睡眠模式下 USART5 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART5 时钟1: 在睡眠模式下开启 USART5 时钟</td></tr><tr><td>4</td><td>USART0SPEN</td><td>在睡眠模式下 USART0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 USART0 时钟1: 在睡眠模式下开启 USART0 时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>TIMER7SPEN</td><td>在睡眠模式下 TIMER7 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TIMER7 时钟1: 在睡眠模式下开启 TIMER7 时钟</td></tr><tr><td>0</td><td>TIMER0SPEN</td><td>在睡眠模式下 TIMER0 时钟使能由软件置位或复位0: 在睡眠模式下关闭 TIMER0 时钟1: 在睡眠模式下开启 TIMER0 时钟</td></tr></table>

## 5.3.20. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x70

复位值：0x0000 0000, 只能由备份域复位进行复位

注意：备份域控制寄存器（RCU_BDCTL）的LXTALEN、LXTALBPS、RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="2">w</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置位或复位0:无作用1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟源选择由软件置位或清零来控制RTC的时钟源。一旦RTC的时钟源选择后,除了将备份域复位否则时钟源不能被改变。00:没有时钟01:选择CK_LXTAL时钟作为RTC的时钟源10:选择CK_IRC32K时钟作为RTC的时钟源11:选择CK_HXTAL/RTCDIV时钟作为RTC的时钟源,请参考RCU_CFG0寄存器的RTCDIV位域。</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力由软件置位或复位。当备份域复位时将复位该值00:低驱动能力(复位值)01:中低驱动能力10:中高驱动能力11:高驱动能力注意:LXTALDRI位在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能由软件置位或复位0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>低速晶体振荡器稳定标志位硬件置‘1’来指示LXTAL振荡器时钟是否稳定待用0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL时钟使能由软件置位或复位0:关闭LXTAL时钟1:使能LXTAL时钟</td></tr></table>

## 5.3.21. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x74

复位值：0x0E00 0000, 所有复位标志位仅在电源复位时被清零，RSTFC/IRC32KEN在系统复位时被清零

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>BORRSTF</td><td>RSTFC</td><td colspan="8">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">Reserved</td><td>IRC32KSTB</td><td>IRC32KEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置位向RSTFC位写1来清除该位0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1向RSTFC位写1来清除该位0:无窗口看门狗复位发生1:发生窗口看门狗复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1向RSTFC位写1来清除该位0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1向RSTFC位写1来清除该位0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1向RSTFC位写1来清除该位0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位外部引脚复位发生时由硬件置1向RSTFC位写1来清除该位</td></tr></table>

<table><tr><td>25</td><td>BORRSTF</td><td>欠压复位复位标志位欠压复位复位发生时由硬件置1向RSTFC位写1来清除该位0:无欠压复位复位发生1:发生欠压复位复位</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位0:无作用1:清除所有复位标志位</td></tr><tr><td>23:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>IRC32KSTB</td><td>IRC32K时钟稳定标志位该位由硬件置1指示IRC32K输出时钟是否稳定待用0:IRC32K时钟未稳定1:IRC32K已稳定</td></tr><tr><td>0</td><td>IRC32KEN</td><td>IRC32K使能由软件置位和复位0:关闭IRC32K时钟1:开启IRC32K时钟</td></tr></table>

## 5.3.22. PLL 时钟扩频控制寄存器（RCU_PLLSSCTL）

地址偏移：0x80

复位值：0x0000 0000

扩频调制仅适用于主PLL时钟。

仅当PLL被禁止时，RCU_PLLSSCTL寄存器才可写入。

该寄存器用于配置PLL扩频时钟生成，需按照如下公式：

$$
\begin{array}{l} \text {MODCNT = round(f_{PLLIN} /4 / f_{mod})} \\ \text {MODSTEP = round(mdamp*PLLN*2^{14} /(MODCNT*100))} \end{array}
$$

f 表示PLL输入时钟频率，f 表示扩频调制频率，mdamp表示扩频调制振幅（按百分比表示），PLLN 表示PLL时钟频率倍频因子。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SSCGON</td><td>SS_TYPE</td><td colspan="2">保留</td><td colspan="12">MODSTEP[14:3]</td></tr><tr><td>rw</td><td>rw</td><td colspan="7"></td><td colspan="7">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">MODSTEP[2:0]</td><td colspan="13">MODCNT[12:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SSCGON</td><td>PLL 扩频调制使能0:禁止扩频调制1:使能扩频调制</td></tr><tr><td>30</td><td>SS_TYPE</td><td>PLL 扩频调制类型选择0:选择中心扩频1:选择向下扩频</td></tr><tr><td>29:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:13</td><td>MODSTEP</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件: MODSTEP*MODCNT≤$2^{15}$-1</td></tr><tr><td>12:0</td><td>MODCNT</td><td>这些位配置 PLL 扩频调制曲线振幅和频率。必须满足如下条件: MODSTEP*MODCNT≤$2^{15}$-1</td></tr></table>

## 5.3.23. PLLI2S 寄存器（RCU_PLLI2S）

地址偏移：0x84

复位值：0x2400 3000

配置PLLI2S时钟可参考下列公式：

CK_PLLI2SVCOSRC = CK_PLLSRC / PLLPSC 

CK_PLLI2SVCO = CK_PLLI2SVCOSRC × PLLI2SN 

CK_PLLI2SR = CK_PLLI2SVCO / PLLI2SR 

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="3">PLLI2SR[2:0]</td><td colspan="4">PLLI2SQ[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="9">PLLI2SN[8:0]</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:28</td><td>PLLI2SR[2:0]</td><td>PLLI2S VCO 时钟的分频因子用于 PLLI2SR 时钟输出频率当 PLLI2S 时钟被关闭时由软件置位或复位。这些位用于通过 PLLI2S VCO 时钟(CK_PLLI2SVCO)分频生成 PLLI2SR 输出时钟(CK_PLLI2SR)。CK_PLLI2SR用于生成 I2S 时钟(≤200MHz)。RCU_PLLI2S 寄存器的 PLLI2SN 位域对 CK_PLLI2SVCO 时钟进行了描述。000:保留001:保留010: CK_PLLI2SR = CK_PLLI2SVCO / 2.011: CK_PLLI2SR = CK_PLLI2SVCO / 3100: CK_PLLI2SR = CK_PLLI2SVCO / 4...111: CK_PLLI2SR = CK_PLLI2SVCO / 7</td></tr><tr><td>27:24</td><td>PLLI2SQ[3:0]</td><td>PLLI2S VCO时钟的分频因子用于 PLLI2SQ时钟输出频率当 PLLI2S时钟被关闭时由软件置位或复位。这些位用于通过 PLLI2S VCO时钟(CK_PLLI2SVCO)分频生成 PLLI2SQ输出时钟(CK_PLLI2SR)。RCU_PLLI2S寄存器的 PLLI2SQ位域对 CK_PLLI2SVCO时钟进行了描述。0000:保留0001:保留0010: CK_PLLI2SQ = CK_PLLI2SVCO / 2.0011: CK_PLLI2SQ = CK_PLLI2SVCO / 30100: CK_PLLI2SQ = CK_PLLI2SVCO / 4...1111: CK_PLLI2SQ = CK_PLLI2SVCO / 15</td></tr><tr><td>23:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:6</td><td>PLLI2SN[8:0]</td><td>PLLI2S VCO时钟倍频因子当 PLLI2S被关闭时由软件置位或清零(仅支持全字/半字写操作)这些位域用做将 PLLI2S VCO源时钟(CK_PLLI2SVCOSRC)倍频生成 PLLI2S VCO输出时钟(CK_PLLI2SVCO)。RCU_PLL寄存器的 PLLPSC位域对CK_PLLI2SVCOSRC时钟进行了描述。注意:CK_PLLI2SVCO时钟频率范围必须在100MHz到500MHz之间PLL12SN时钟的值必须为:50≤PLL12SN≤50000000000:保留000000001:保留...000110001:保留000110010: CK_PLLI2SVCO = CK_PLLI2SVCOSRC x 50.000110011: CK_PLLI2SVCO = CK_PLLI2SVCOSRC x 51....111110100: CK_PLLI2SVCO = CK_PLLI2SVCOSRC x 500.111110101:保留...111111111:保留</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.24. PLLSAI 寄存器（RCU_PLLSAI）

地址偏移：0x88复位值：0x2400 3000配置PLLSAI时钟可参考下列公式：CK_PLLSAIVCOSRC = CK_PLLSRC / PLLPSCCK_PLLSAIVCO = CK_ PLLSAIVCOSRC × PLLSAIN


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="3">PLLSAIR[2:0]</td><td colspan="4">PLLSAIQ[3:0]</td><td colspan="6">保留</td><td colspan="2">PLLSAIP[1:0]</td></tr><tr><td></td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="6"></td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="9">PLLSAIN[8:0]</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:28</td><td>PLLSAIR[2:0]</td><td>PLLSAI VCO时钟的分频因子用于PLLSAIR时钟输出频率当PLLSAI时钟被关闭时由软件置位或复位。这些位用于通过PLLSAI VCO时钟(CK_PLLSAIVCO)分频生成PLLSAIR输出时钟(CK_PLLSAIR)。CK_PLLSAIR用于生成TLI时钟(≤216MHz)。RCU_PLLSAI寄存器的PLLSAIN位域对CK_PLLSAIVCO时钟进行了描述。000:保留001:保留010:CK_PLLSAIR=CK_PLLSAIVCO/2011:CK_PLLSAIR=CK_PLLSAIVCO/3100:CK_PLLSAIR=CK_PLLSAIVCO/4...111:CK_PLLSAIR=CK_PLLSAIVCO/7</td></tr><tr><td>27:24</td><td>PLLSAIQ[3:0]</td><td>PLLSAI VCO时钟的分频因子用于PLLSAIQ时钟输出频率当PLLSAI时钟被关闭时由软件置位或复位。这些位用于通过PLLSAI VCO时钟(CK_PLLSAIVCO)分频生成PLLSAIQ输出时钟(CK_PLLSAIR)。RCU_PLLSAI寄存器的PLLSAIQ位域对CK_PLLSAIVCO时钟进行了描述。0000:保留0001:保留0010:CK_PLLSAIQ=CK_PLLSAIVCO/2.0011:CK_PLLSAIQ=CK_PLLSAIVCO/30100:CK_PLLSAIQ=CK_PLLSAIVCO/4...1111:CK_PLLSAIQ=CK_PLLSAIVCO/15</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>PLLSAIP[1:0]</td><td>PLLSAI VCO时钟的分频因子用于PLLSAIP时钟输出频率当PLLSAI时钟被关闭时由软件置位或复位。这些位用于通过PLLSAI VCO时钟(CK_PLLSAIVCO)分频生成PLLSAIP输出时钟(CK_PLLSAIP)。CK_PLLSAIP用于生成UBSFS/USBHS(48MHz),TRNG(48MHz)或SDIO(≤48MHz)的时钟。RCU_PLLSAI寄存器的PLLSAIN位域对CK_PLLSAIVCO时钟进行了描述。00:CK_PLLSAIP=CK_PLLSAIVCO/201: CK_PLLSAIP = CK_PLLSAIVCO / 410: CK_PLLSAIP = CK_PLLSAIVCO / 611: CK_PLLSAIP = CK_PLLSAIVCO / 8</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:6</td><td>PLLSAIN[8:0]</td><td>PLLSAI VCO时钟倍频因子当PLLSAI被关闭时由软件置位或清零(仅支持全字/半字写操作)这些位域用做将PLLSAI VCO源时钟(CK_PLLSAIVCOSRC)倍频生成PLLSAI VCO输出时钟(CK_PLLSAIVCO)。RCU_PLL寄存器的PLLPSC位域对CK_PLLVCOSRC时钟进行了描述。注意:CK_PLLSAIVCO时钟频率范围必须在100MHz到500MHz之间PLL2SN时钟的值必须为:50≤PLLSAIN≤50000000000:保留000000001:保留...000110001:保留000110010: CK_PLLSAIVCO = CK_PLLSAIVCOSRC x 50000110011: CK_PLLSAIVCO = CK_PLLSAIVCOSRC x 51...111110100: CK_PLLSAIVCO = CK_PLLSAIVCOSRC x 50011110101:保留...111111111:保留</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.25. 时钟配置寄存器 1（RCU_CFG1）

地址偏移：0x8C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>TIMERSEL</td><td colspan="2">保留</td><td colspan="2">SAISEL[1:0]</td><td colspan="2">保留</td><td colspan="2">PLLSAIRDIV[1:0]</td></tr><tr><td colspan="10">rw</td><td colspan="4">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">PLLI2SQDIV[4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>TIMERSEL</td><td>TIMER时钟源选择由软件置位或复位 该位定义了所有定时器的时钟源选择</td></tr></table>

0：如果 RCU_CFG0 寄存器的 APB1PSC/APB2PSC 位域的值为 0b0xx（CK_APBx= CK_AHB）或 0b100（CK_APBx = CK_AHB/2），定时器时钟等于 CK_AHB（CK_TIMERx = CK_AHB），否则定时器时钟等于 APB 时钟的两倍（在 APB1 域的定时器： CK_TIMERx = 2 x CK_APB1，在 APB2 域的定时器：CK_TIMERx = 2 xCK_APB2）。

1：如果 RCU_CFG0 寄存器的 APB1PSC/APB2PSC 位域的值为 0b0xx（CK_APBx= CK_AHB），0b100（CK_APBx = CK_AHB/2），或 0b101（CK_APBx = CK_AHB/4）,定时器时钟等于 CK_AHB（CK_TIMERx = CK_AHB）。否则定时器时钟等于 APB 时钟的四倍（在 APB1 域的定时器：CK_TIMERx = 4 x CK_APB1；在 APB2 域的定时器：CK_TIMERx = 4 x CK_APB2）。

23:22 保留 必须保持复位值。

21:20 SAISEL SAI 时钟源选择由软件置位或复位。该位定义了所有定时器的时钟源选择。00：CK_PLLSAIQ01：CK_PLLI2SQ10：I2S_CKIN11：I2S_CKIN

17:16 PLLSAIRDIV[1:0] PLLSAIR 时钟的分频因子当 PLLSAI 时钟被关闭时由软件置位或复位。该位用于生成 TLI 模块的时钟源。00：CK_PLLSAIR / 201：CK_PLLSAIR / 410：CK_PLLSAIR / 811：CK_PLLSAIR / 16

4:0 PLLI2SQDIV[4:0] PLLI2SQ 时钟的分频因子当 PLLI2SQ 时钟被关闭时由软件置位或复位。该位用于生成 SAI 模块的时钟源。00000: CK_PLLI2SQ / 100001: CK_PLLI2SQ / 200010: CK_PLLI2SQ / 3…11111: CK_PLLI2SQ / 32

## 5.3.26. 时钟配置寄存器 2（RCU_CFG2）

地址偏移：0x94

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">I2C5SEL[1:0]</td><td colspan="2">I2C4SEL[1:0]</td><td colspan="2">I2C3SEL[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:4</td><td>I2C5CLKSEL[1:0]</td><td>I2C5时钟源选择由软件置位或清零00:选择CK_APB101:选择CK_PLLSAIR10:选择CK_IRC16M11:保留</td></tr><tr><td>3:2</td><td>I2C4CLKSEL[1:0]</td><td>I2C4时钟源选择由软件置位或清零00:选择CK_APB101:选择CK_PLLSAIR10:选择CK_IRC16M11:保留</td></tr><tr><td>1:0</td><td>I2C3CLKSEL[1:0]</td><td>I2C3时钟源选择由软件置位或清零00:选择CK_APB101:选择CK_PLLSAIR10:选择CK_IRC16M11:保留</td></tr></table>

## 5.3.27. 附加时钟控制寄存器（RCU_ADDCTL）

地址偏移：0xC0

复位值：0xXX00 0000 x表示未定义

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">保留</td><td>IRC48MS TB</td><td>IRC48ME N</td></tr><tr><td colspan="14">r</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>PLL48MS EL</td><td>CK48MSE L</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>IRC48MCALIB[7:0]</td><td>内部 48MHz RC 振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>IRC48MSTB</td><td>内部48MHz RC振荡器时钟稳定标志位硬件置‘1’来指示IRC48M振荡器时钟是否稳定待用0: IRC48M未稳定1: IRC48M已稳定</td></tr><tr><td>16</td><td>IRC48MEN</td><td>内部48MHz RC振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位0: 关闭IRC48M时钟1: 打开IRC48M时钟</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>PLL48MSEL</td><td>PLL48M时钟源选择由软件置位和复位。该位用于选择CK_PLLQ时钟或CK_PLLSAIP时钟作为PLL48M的时钟源0: 选择CK_PLLQ时钟1: 选择CK_PLLSAIP时钟</td></tr><tr><td>0</td><td>CK48MSEL</td><td>48MHz时钟源选择由软件置位和复位。该位用于选择IRC48M时钟或PLL48M时钟作为CK48M时钟源。CK48M时钟为TRNG/SDIO/USBFS/USBHS模块提供时钟。RCU_ADDCTL寄存器的PLL48MSEL位对PLL48M时钟进行了描述。0: 不选择IRC48M时钟(通过PLL48MSEL位选择使用CK_PLLQ时钟或CK_PLLSAIP时钟)1: 选择IRC48M时钟</td></tr></table>

## 5.3.28. 附加时钟中断寄存器（RCU_ADDINT）

地址偏移：0xCC

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>IRC48MS TBIC</td><td colspan="6">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>IRC48MSTBIE</td><td colspan="7">保留</td><td>IRC48MSTBIF</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IRC48MSTBIC</td><td>内部48 MHz RC振荡器稳定中断清零软件写1复位IRC48MSTBIF标志位0:不复位IRC48MSTBIF标志位1:复位IRC48MSTBIF标志位</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>IRC48MSTBIE</td><td>内部48 MHz RC振荡器稳定中断使能由软件置位和复位来使能/禁止IRC48M时钟稳定中断0:禁止IRC48M时钟稳定中断1:使能IRC48M时钟稳定中断</td></tr><tr><td>13:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>IRC48MSTBIF</td><td>IRC48M时钟稳定中断标志位当内部48 MHz RC振荡器时钟稳定且IRC48MSTBIE位被置1时由硬件置1软件置位IRC48MSTBIC位时清除该位0:无IRC48M时钟稳定中断产生1:产生IRC48M时钟稳定中断</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.29. APB1 附加复位寄存器（RCU_ADDAPB1RST）

地址偏移：0xE0

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IREFRST</td><td colspan="3">保留</td><td>CTC RST</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IREFRST</td><td>IREF 复位由软件置位或复位0:无作用1:复位 IREF</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCRST</td><td>CTC 复位由软件置位或复位0:无作用</td></tr></table>

1：复位 CTC

26:0 保留 必须保持复位值。

## 5.3.30. APB1 附加使能寄存器（RCU_ADDAPB1EN）

地址偏移：0xE4

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IREFEN</td><td colspan="3">保留</td><td>CTCEN</td><td colspan="11">保留</td></tr><tr><td>rw</td><td colspan="15">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>IREFEN</td><td>IREF时钟使能由软件置位或复位0:关闭 IREF 时钟1:开启 IREF 时钟</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCEN</td><td>CTC时钟使能由软件置位或复位0:关闭 CTC 时钟1:开启 CTC 时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.31. APB1 附加睡眠模式使能寄存器（RCU_ADDAPB1SPEN）

地址偏移：0xE8

复位值：0x8800 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>IREFSPEN</td><td colspan="3">保留</td><td>CTCSPEN</td><td colspan="11">保留</td></tr><tr><td colspan="4">rw</td><td colspan="12">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>31</td><td>IREFSPEN</td><td>睡眠模式下 IREF 时钟使能由软件置位或复位0:睡眠模式下关闭 IREF 时钟1:睡眠模式下开启 IREF 时钟</td></tr><tr><td>30:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>CTCSPEN</td><td>睡眠模式下 CTC 时钟使能由软件置位或复位0:睡眠模式下关闭 CTC 时钟1:睡眠模式下开启 CTC 时钟</td></tr><tr><td>26:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 5.3.32. 电源解锁寄存器（RCU_VKEY）

地址偏移：0x100

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>RCU_DSV 寄存器解锁这些位仅能被软件写,若读这些位,则全为 0。只有在向 RCC_VKEY 寄存器写 0x1A2B3C4D 后,RCU_DSV 寄存器才能被写。</td></tr></table>

## 5.3.33. 深度睡眠模式电压寄存器（RCU_DSV）

地址偏移：0x134

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DSLPVS[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>DSLPVS[2:0]</td><td>深度睡眠模式电压选择由软件置位和清零这些位000:在深度睡眠模式下内核电压为缺省值001:在深度睡眠模式下内核电压为(缺省值-0.1)V(不建议客户使用)010:在深度睡眠模式下内核电压为(缺省值-0.2)V(不建议客户使用)011:在深度睡眠模式下内核电压为(缺省值-0.3)V(不建议客户使用)100~111:保留</td></tr></table>
