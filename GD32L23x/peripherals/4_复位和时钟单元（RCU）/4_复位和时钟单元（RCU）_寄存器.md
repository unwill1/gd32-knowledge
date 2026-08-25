## 4.3. RCU 寄存器

RCU基地址：0x4002 1000

## 4.3.1. 控制寄存器（RCU_CTL）

地址偏移：0x00

复位值：0x0000 XX83 X表示未定义。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>PLLSTB</td><td>PLLEN</td><td>LCKMD</td><td>LCKMEN</td><td>IRC48MS TB</td><td>IRC48ME N</td><td>CKMEN</td><td>HXTALB PS</td><td>HXTALST B</td><td>HXTALE N</td></tr><tr><td colspan="6"></td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>r</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC16MCALIB[7:0]</td><td colspan="5">IRC16MADJ[4:0]</td><td>保留.</td><td>IRC16MS TB</td><td>IRC16ME N</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>PLLSTB</td><td>PLL时钟稳定标志位硬件置‘1’来指示PLL输出时钟是否稳定待用。0:PLL没稳定1:PLL稳定</td></tr><tr><td>24</td><td>PLLEN</td><td>PLL使能软件置位或复位。如果PLL时钟作为系统时钟的时候该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:PLL被关闭1:PLL被打开</td></tr><tr><td>23</td><td>LCKMD</td><td>LXTAL时钟故障检测由硬件置位,当外部32 KHz振荡器(LXTAL)上的时钟安全系统检测到故障。可以通过禁用LCKMEN或禁用LXTALEN或LXTAL来清除它。0:LXTAL(32 KHz振荡器)上未检测到故障1:在LXTAL(32 KHz振荡器)上检测到故障</td></tr><tr><td>22</td><td>LCKMEN</td><td>LXTAL时钟监视使能0:禁止LXTAL时钟监视器1:使能LXTAL时钟监视器通过软件设置,启用LXTAL(32 KHz振荡器)上的时钟安全系统。LCKMEN必须在LXTAL已启用(LXTALEN位已启用)和就绪(LXTALSTB标志由硬件设置)</td></tr><tr><td>21</td><td>IRC48MSTB</td><td>内部48MHz RC振荡器时钟稳定标志位硬件置‘1’来指示IRC48M振荡器时钟是否稳定待用0: IRC48M未稳定1: IRC48M已稳定</td></tr><tr><td>20</td><td>IRC48MEN</td><td>内部48MHz RC振荡器使能由软件置位和复位。当进入深度睡眠或待机模式后由硬件复位0: 关闭IRC48M时钟1: 打开IRC48M时钟</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视使能0: 禁止外部4~48MHz晶体振荡器(HXTAL)时钟监视器1: 使能外部4~48MHz晶体振荡器(HXTAL)时钟监视器当硬件监测到HXTAL时钟一直停留在低或者高的状态,内部硬件将切换系统时钟到IRC16M RC时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位IRC16MEN的状态,自动使能IRC16M时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>外部晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时,HXTALBPS位才可写。0: 禁止HXTAL旁路模式1: 使能HXTAL旁路模式,HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>外部晶体振荡器(HXTAL)时钟稳定状态标志位硬件置‘1’来指示HXTAL振荡器时钟是否稳定待用。0: HXTAL振荡器未稳定1: HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>外部高速振荡器时钟使能软件置‘1’或清‘0’。如果HXTAL时钟或者PLL输入时钟作为系统时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0: 禁止外部4~48MHz晶体振荡器1: 使能外部4~48MHz晶体振荡器</td></tr><tr><td>15:8</td><td>IRC16MCALIB[7:0]</td><td>高速内部振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:3</td><td>IRC16MADJ[4:0]</td><td>高速内部振荡器时钟调整值这些位由软件置位,最终调整值为IRC16MADJ当前值加上IRC16MCALIB[7:0]位的值。最终调整值应该调整IRC16M到16 MHz ± 1%。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>1</td><td>IRC16MSTB</td><td>高速内部(IRC16M)时钟稳定状态标志位硬件置‘1’来指示IRC16M振荡器时钟是否稳定待用。0: IRC16M振荡器未稳定1: IRC16M振荡器已稳定</td></tr><tr><td>0</td><td>IRC16MEN</td><td>高速内部振荡器使能软件复位置位。如果IRC16M时钟用作系统时钟时该位不能被复位。当从待机或深</td></tr></table>

度睡眠模式返回或在HXTALCKM置位的情况下用作系统时钟的HXTAL振荡器发生故障时，该位由硬件置1来启动IRC16M振荡器。

0：内部16 MHz RC振荡器关闭

1：内部16 MHz RC振荡器开启

## 4.3.2. 配置寄存器 0（RCU_CFG0）

地址偏移：0x04

复位值：0x003C 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>PLLDV</td><td colspan="3">CKOUTDIV[2:0]</td><td>PLLMF[6]</td><td colspan="3">CKOUTSEL[2:0]</td><td colspan="6">PLLMF[5:0]</td><td colspan="2">PLLSEL</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="6">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">ADCPSC[1:0]</td><td colspan="3">APB2PSC[2:0]</td><td colspan="3">APB1PSC[2:0]</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>PLLDV</td><td>CK_PLL 1或2分频来用作CK_OUT0: CK_PLL 2分频用作CK_OUT1: CK_PLL用作CK_OUT</td></tr><tr><td>30:28</td><td>CKOUTDIV[2:0]</td><td>CK_OUT分频器,来降低CK_OUT频率CK_OUT的选择参考RCU_CFG0的26:24位。000: CK_OUT不分频001: CK_OUT 2分频010: CK_OUT 4分频011: CK_OUT 8分频100: CK_OUT 16分频101: CK_OUT 32分频110: CK_OUT 64分频111: CK_OUT 128分频</td></tr><tr><td>27</td><td>PLLMF[6]</td><td>PLLMF的位6参考RCU_CFG0的位23:18</td></tr><tr><td>26:24</td><td>CKOUTSEL[2:0]</td><td>CK_OUT时钟源选择软件置位或清零。000: 没有时钟被选择001: 选择内部48M RC振荡器时钟010: 选择内部32K RC振荡器时钟011: 选择外部低速振荡器时钟100: 选择系统时钟101: 选择内部16M RC振荡器时钟110: 选择外部高速振荡器时钟</td></tr></table>

<table><tr><td>23:18</td><td>PLLMF[5:0]</td><td>PLL倍频因子软件写这些位包括RCU_CFG0的27位来确定PLL的倍频因子。0000000~0000001:保留0000010~0001110:(PLL时钟源x(PLLMF[6:0]+2))0001111~1111110::(PLL时钟源x(PLLMF[6:0]+1))1111111:保留注意:PLL输出频率不能超过64MHz。</td></tr><tr><td>17:16</td><td>PLLSEL</td><td>PLL时钟源选择软件置1或清0来控制PLL时钟源00:选择IRC16M二分频为PLL时钟源01:选择HXTAL为PLL时钟源1x:选择IRC48M为PLL时钟源</td></tr><tr><td>15:14</td><td>ADCPSC[1:0]</td><td>ADC时钟预分频选择软件写两位包括RCU_CFG2的31位和30位来确定ADC时钟分频。软件清0和置1。0000:选择APB2时钟2分频0001:选择APB2时钟4分频0010:选择APB2时钟6分频0011:选择APB2时钟8分频0100:选择APB2时钟10分频0101:选择APB2时钟12分频0110:选择APB2时钟14分频0111:选择APB2时钟16分频1000:选择AHB时钟3分频1001:选择AHB时钟5分频1010:选择AHB时钟7分频1011:选择AHB时钟9分频1100:选择AHB时钟11分频1101:选择AHB时钟13分频1110:选择AHB时钟15分频1111:选择AHB时钟17分频</td></tr><tr><td>13:11</td><td>APB2PSC[2:0]</td><td>APB2预分频选择软件置1和清0来控制APB2时钟分频因子。0xx:选择AHB时钟不分频100:选择AHB时钟2分频101:选择AHB时钟4分频110:选择AHB时钟8分频111:选择AHB时钟16分频</td></tr><tr><td>10:8</td><td>APB1PSC[2:0]</td><td>APB1预分频选择软件设置和清除来控制APB1时钟分频因子。0xx:选择AHB时钟不分频</td></tr></table>

<table><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB预分频选择软件设置和清除来控制AHB时钟分频因子。0xxx: 选择CK_SYS系统时钟不分频1000: 选择CK_SYS系统时钟2分频1001: 选择CK_SYS系统时钟4分频1010: 选择CK_SYS系统时钟8分频1011: 选择CK_SYS系统时钟16分频1100: 选择CK_SYS系统时钟64分频1101: 选择CK_SYS系统时钟128分频1110: 选择CK_SYS系统时钟256分频1111: 选择CK_SYS系统时钟512分频</td></tr></table>

## SCSS[1:0]

## 系统时钟转换状态

## GD32L233xx产品

硬件设置和清除指示系统当前时钟源

00：选择CK_IRC16M作为CK_SYS系统时钟源

01：选择CK_HXTAL作为CK_SYS系统时钟源

10：选择CK_PLL作为CK_SYS系统时钟源

11：选择CK_IRC48M作为CK_SYS系统时钟源

## GD32L235xx产品

000：选择CK_IRC16M作为CK_SYS系统时钟源

001：选择CK_HXTAL作为CK_SYS系统时钟源

010：选择CK_PLL作为CK_SYS系统时钟源

011：选择CK_IRC48M作为CK_SYS系统时钟源

1xx：选择CK_IRC32K作为CK_SYS系统时钟源

注意：SCS[2]参考RCU_CFG1寄存器的位17

## SCS[1:0]

## 系统时钟转换

软件设置选择系统时钟源。由于CK_SYS的改变有固有的延迟，需要软件读SCSS位来确保转换是否结束。在从深度睡眠或待机模式中返回时，或作为系统时钟或PLL时钟源的HXTAL出现故障时，强制选择IRC16M作为系统时钟或PLL时钟。

## GD32L233xx产品

00：选择IRC16M时钟作为CK_SYS系统时钟源

01：选择HXTAL时钟作为CK_SYS系统时钟源

10：选择PLL作为CK_SYS系统时钟源

11：选择CK_IRC48M作为CK_SYS系统时钟源

## GD32L235xx产品

000：选择IRC16M时钟作为CK_SYS系统时钟源

001：选择HXTAL时钟作为CK_SYS系统时钟源

010：选择PLL作为CK_SYS系统时钟源

011：选择CK_IRC48M作为CK_SYS系统时钟源

1xx：选择CK_IRC32K作为CK_SYS系统时钟源

注意：SCS[2]参考RCU_CFG1寄存器的位16

## 4.3.3. 中断寄存器（RCU_INT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td>LCKMIC</td><td>IRC48MSTBIC</td><td>PLLSTBIC</td><td>HXTALSTBIC</td><td>IRC16MSTBIC</td><td>LXTALSTBIC</td><td>IRC32KSTBIC</td></tr><tr><td colspan="8"></td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LCKMIE</td><td>IRC48MSTBIE</td><td>PLLSTBIE</td><td>HXTALSTBIE</td><td>IRC16MSTBIE</td><td>LXTALSTBIE</td><td>IRC32KSTBIE</td><td>CKMIF</td><td>LCKMIF</td><td>IRC48MSTBIF</td><td>PLLSTBIF</td><td>HXTALSTBIF</td><td>IRC16MSTBIF</td><td>LXTALSTBIF</td><td>IRC32KSTBIF</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清除软件写1复位CKMIF标志位。0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>LCKMIC</td><td>LXTAL时钟阻塞中断清除软件写1复位LCKMIF标志位。0:不复位LCKMIF标志位1:复位LCKMIF标志位</td></tr><tr><td>21</td><td>IRC48MSTBIC</td><td>IRC48M时钟稳定中断清除软件写1复位IRC48MSTBIF标志位。0:不复位IRC48MSTBIF标志位1:复位IRC48MSTBIF标志位</td></tr><tr><td>20</td><td>PLLSTBIC</td><td>PLL稳定中断清除软件写1复位PLLSTBIF标志位。0:不复位PLLSTBIF标志位1:复位PLLSTBIF标志位</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清除软件写1复位HXTALSTBIF标志位。0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr></table>

<table><tr><td>18</td><td>IRC16MSTBIC</td><td>IRC16M时钟稳定中断清除软件写1复位IRC16MSTBIF标志位。0:不复位IRC16MSTBIF标志位1:复位IRC16MSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清除软件写1复位LXTALSTBIF标志位。0:不复位LXTALSTBIF标志位1:复位LXTALRDYF标志位</td></tr><tr><td>16</td><td>IRC32KSTBIC</td><td>IRC32K时钟稳定中断清除软件写1复位IRC32KSTBIF标志位。0:不复位IRC32KSTBIF标志位1:复位IRC32KSTBIF标志位</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LCKMIE</td><td>LXTAL时钟阻塞中断使能软件置1和清0来使能/禁止LXTAL时钟阻塞中断。0:禁止LXTAL时钟阻塞中断1:使能LXTAL时钟阻塞中断</td></tr><tr><td>13</td><td>IRC48MSTBIE</td><td>IRC48M时钟稳定中断使能软件置1和清0来使能/禁止IRC48M时钟稳定中断。0:禁止IRC48M时钟稳定中断1:使能IRC48M时钟稳定中断</td></tr><tr><td>12</td><td>PLLSTBIE</td><td>PLL时钟稳定中断使能软件置1和清0来使能/禁止PLL时钟稳定中断。0:禁止PLL时钟稳定中断1:使能PLL时钟稳定中断</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置1和清0来使能/禁止HXTAL时钟稳定中断。0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>IRC16MSTBIE</td><td>IRC16M时钟稳定中断使能软件置1和清0来使能/禁止IRC16M时钟稳定中断。0:禁止IRC16M时钟稳定中断1:使能IRC16M时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能LXTAL时钟稳定中断使能/禁止控制。0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC32KSTBIE</td><td>IRC32K时钟稳定中断使能IRC32K时钟稳定中断使能/禁止控制。</td></tr></table>

<table><tr><td></td><td></td><td>0:禁止IRC32K时钟稳定中断1:使能IRC32K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟阻塞时硬件置1。软件置CKMIC=1时清除该位。0:时钟运行正常1:HXTAL时钟阻塞</td></tr><tr><td>6</td><td>LCKMIF</td><td>LXTAL时钟阻塞中断标志位当LXTAL时钟阻塞由硬件置1。软件置位LCKMIC时清除该位。0:LXTAL时钟运行正常1:LXTAL时钟阻塞</td></tr><tr><td>5</td><td>IRC48MSTBIF</td><td>IRC48M时钟稳定中断标志位当IRC48M时钟稳定且IRC48MSTBIE位被置1时由硬件置1。软件置IRC48MSTBIC=1时清除该位。0:无IRC48M时钟稳定中断产生1:IRC48M时钟稳定中断发生</td></tr><tr><td>4</td><td>PLLSTBIF</td><td>PLL时钟稳定中断标志位当PLL时钟稳定且PLLSTBIE位被置1时由硬件置1。软件置PLLSTBIC=1时清除该位。0:无PLL时钟稳定中断产生1:产生PLL时钟稳定中断</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当外部4~48MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1。软件置HXTALSTBIC=1时清除该位。0:无HXTAL时钟稳定中断发生1:发生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>IRC16MSTBIF</td><td>IRC16M时钟稳定中断标志位当内部16MHz RC振荡器时钟稳定且IRC16MSTBIE位被置1时由硬件置1。软件置IRC16MSTBIC=1时清除该位。0:无IRC16M时钟稳定中断产生1:产生IRC16M时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当外部32.768KHz晶体振荡器时钟稳定且LXTALSTBIE为被置1时由硬件置1。软件置LXTALSTBIC=1时清除该位。0:无LXTAL时钟稳定中断发生1:发生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC32KSTBIF</td><td>IRC32K时钟稳定中断标志位当内部32KHz RC振荡器时钟稳定且IRC32KSTBIE位被置1时由硬件置1。软件置IRC32KSTBIC=1时清除该位。</td></tr></table>

0：无IRC32K时钟稳定中断产生

1：产生IRC32K时钟稳定中断

## 4.3.4. APB2 复位寄存器（RCU_APB2RST）

GD32L233xx 产品

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0RST</td><td>保留</td><td>SPI0RST</td><td>TIMER8RST</td><td>保留</td><td>ADCRST</td><td colspan="7">保留</td><td>CMPRST</td><td>SYSCFGRST</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0复位由软件置1或清0。0:无复位1:复位USART0</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0复位由软件置1或清0。0:无复位1:复位SPI0</td></tr><tr><td>11</td><td>TIMER8RST</td><td>TIMER8定时器复位由软件置1或清0。0:无复位1:复位TIMER8定时器</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>ADCRST</td><td>ADC复位由软件置1或清0。0:无复位1:复位ADC</td></tr></table>

<table><tr><td>8:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPRST</td><td>比较器复位由软件置1或清0。0:无复位1:复位比较器模块</td></tr><tr><td>0</td><td>SYSCFGRST</td><td>系统配置复位由软件置1或清0。0:无复位1:复位系统配置和比较器模块</td></tr></table>

## GD32L235xx 产品

地址偏移：0x0C

复位值：0x0000 0000


该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>TIMER40RST</td><td>TIMER14RST</td></tr><tr><td colspan="14"></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0RST</td><td>保留</td><td>SPI0RST</td><td>TIMER8RST</td><td>TIMER0RST</td><td>ADCRST</td><td colspan="7">保留</td><td>CMPRST</td><td>SYSCFGRST</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>TIMER40RST</td><td>TIMER40复位由软件置1或清0。0:无复位1:复位TIMER40</td></tr><tr><td>16</td><td>TIMER14RST</td><td>TIMER14复位由软件置1或清0。0:无复位1:复位TIMER14</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USART0RST</td><td>USART0复位由软件置1或清0。0:无复位1:复位USART0</td></tr></table>

<table><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0RST</td><td>SPI0复位由软件置1或清0。0:无复位1:复位SPI0</td></tr><tr><td>11</td><td>TIMER8RST</td><td>TIMER8定时器复位由软件置1或清0。0:无复位1:复位TIMER8定时器</td></tr><tr><td>10</td><td>TIMER0RST</td><td>TIMER0复位由软件置1或清0。0:无复位1:复位TIMER0</td></tr><tr><td>9</td><td>ADCRST</td><td>ADC复位由软件置1或清0。0:无复位1:复位ADC</td></tr><tr><td>8:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPRST</td><td>比较器复位由软件置1或清0。0:无复位1:复位比较器模块</td></tr><tr><td>0</td><td>SYSCFGRST</td><td>系统配置复位由软件置1或清0。0:无复位1:复位系统配置和比较器模块</td></tr></table>

## 4.3.5. APB1 复位寄存器（RCU_APB1RST）

GD32L233xx 产品

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>CTCRST</td><td>DACRST</td><td>PMURST</td><td colspan="3">保留</td><td>I2C2RST</td><td>USBDRST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RS T</td><td>LPUARTR ST</td><td>USART1 RST</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>SPI1RST</td><td>保留</td><td>WWDGTRST</td><td>SLCDRS T</td><td>LPTIMER RST</td><td>TIMER11 RST</td><td>保留</td><td>TIMER6R ST</td><td>TIMER5R ST</td><td>保留</td><td>TIMER2R ST</td><td>TIMER1R ST</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>CTCRST</td><td>CTC复位由软件置1或清0。0:无复位1:复位CTC</td></tr><tr><td>29</td><td>DACRST</td><td>DAC复位由软件置1或清0。0:无复位1:复位DAC</td></tr><tr><td>28</td><td>PMURST</td><td>电源控制复位由软件置1或清0。0:无复位1:复位电源控制单元</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C2RST</td><td>I2C2复位由软件置1或清0。0:无复位1:复位I2C2</td></tr><tr><td>23</td><td>USBDRST</td><td>USBD复位由软件置1或清0。0:无复位1:复位USBD</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1复位由软件置1或清0。0:无复位1:复位I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0复位由软件置1或清0。0:无复位1:复位I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4复位由软件置1或清0。0:无复位1:复位UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3复位由软件置1或清0。0:无复位1:复位UART3</td></tr><tr><td>18</td><td>LPUARTRST</td><td>LPUART复位由软件置1或清0。0:无复位1:复位LPUART</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1复位由软件置1或清0。0:无复位1:复位USART1</td></tr><tr><td>16:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1复位由软件置1或清0。0:无复位1:复位SPI1</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTRST</td><td>窗口看门狗定时器复位由软件置1或清0。0:无复位1:复位窗口看门狗定时器</td></tr><tr><td>10</td><td>SLCDRST</td><td>SLCD复位由软件置1或清0。0:无复位1:复位SLCD</td></tr><tr><td>9</td><td>LPTIMERRST</td><td>LPTIMER定时器复位由软件置1或清0。0:无复位1:复位LPTIMER定时器</td></tr><tr><td>8</td><td>TIMER11RST</td><td>TIMER11定时器复位由软件置1或清0。0:无复位1:复位TIMER11定时器</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6定时器复位由软件置1或清0。0:无复位1:复位TIMER6定时器</td></tr></table>

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>4</td><td>TIMER5RST</td><td>TIMER5定时器复位由软件置1或清0。0:无复位1:复位TIMER5定时器</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2定时器复位由软件置1或清0。0:无复位1:复位TIMER2定时器</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1定时器复位由软件置1或清0。0:无复位1:复位TIMER1定时器</td></tr></table>

## GD32L235xx 产品

地址偏移：0x10

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>CTCRST</td><td>DACRST</td><td>PMURST</td><td colspan="2">保留</td><td>LPUART1RST</td><td>I2C2RST</td><td>USBDRST</td><td>I2C1RST</td><td>I2C0RST</td><td>UART4RST</td><td>UART3RST</td><td>LPUART0RST</td><td>USART1RST</td><td>CANRST</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SPI1RST</td><td>保留</td><td>LPTIMER1RST</td><td>WWDGTRST</td><td>SLCDRS T</td><td>LPTIMER0RST</td><td>TIMER11RST</td><td colspan="2">保留</td><td>TIMER6RST</td><td>TIMER5RST</td><td colspan="2">保留</td><td>TIMER2RST</td><td>TIMER1RST</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>CTCRST</td><td>CTC复位由软件置1或清0。0:无复位1:复位CTC</td></tr><tr><td>29</td><td>DACRST</td><td>DAC复位由软件置1或清0。0:无复位1:复位DAC</td></tr><tr><td>28</td><td>PMURST</td><td>电源控制复位由软件置1或清0。0:无复位</td></tr></table>

<table><tr><td>27:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>LPUART1RST</td><td>LPUART1复位由软件置1或清0。0:无复位1:复位LPUART1</td></tr><tr><td>24</td><td>I2C2RST</td><td>I2C2复位由软件置1或清0。0:无复位1:复位I2C2</td></tr><tr><td>23</td><td>USBDRST</td><td>USBD复位由软件置1或清0。0:无复位1:复位USBD</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1复位由软件置1或清0。0:无复位1:复位I2C1</td></tr><tr><td>21</td><td>I2C0RST</td><td>I2C0复位由软件置1或清0。0:无复位1:复位I2C0</td></tr><tr><td>20</td><td>UART4RST</td><td>UART4复位由软件置1或清0。0:无复位1:复位UART4</td></tr><tr><td>19</td><td>UART3RST</td><td>UART3复位由软件置1或清0。0:无复位1:复位UART3</td></tr><tr><td>18</td><td>LPUART0RST</td><td>LPUART0复位由软件置1或清0。0:无复位1:复位LPUART0</td></tr><tr><td>17</td><td>USART1RST</td><td>USART1复位由软件置1或清0。0:无复位1:复位USART1</td></tr><tr><td>16</td><td>CANRST</td><td>CAN复位由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位CAN</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SPI1RST</td><td>SPI1复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位SPI1</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>LPTIMER1RST</td><td>LPTIMER1定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位LPTIMER1定时器</td></tr><tr><td>11</td><td>WWDGTRST</td><td>窗口看门狗定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位窗口看门狗定时器</td></tr><tr><td>10</td><td>SLCDRST</td><td>SLCD复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位SLCD</td></tr><tr><td>9</td><td>LPTIMER0RST</td><td>LPTIMER0定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位LPTIMER0定时器</td></tr><tr><td>8</td><td>TIMER11RST</td><td>TIMER11定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位TIMER11定时器</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6RST</td><td>TIMER6定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位TIMER6定时器</td></tr><tr><td>4</td><td>TIMER5RST</td><td>TIMER5定时器复位</td></tr><tr><td></td><td></td><td>由软件置1或清0。</td></tr><tr><td></td><td></td><td>0:无复位</td></tr><tr><td></td><td></td><td>1:复位TIMER5定时器</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER2RST</td><td>TIMER2定时器复位由软件置1或清0。0:无复位1:复位TIMER2定时器</td></tr><tr><td>0</td><td>TIMER1RST</td><td>TIMER1定时器复位由软件置1或清0。0:无复位1:复位TIMER1定时器</td></tr></table>

## 4.3.6. AHB 使能寄存器（RCU_AHBEN）

地址偏移：0x14

复位值：0x0000 0014

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td>PFEN</td><td>保留</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>SRAM1SPEN</td><td>CRCEN</td><td>保留</td><td>FMCSPEN</td><td>保留</td><td>SRAM0SPEN</td><td>保留</td><td>DMAEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PFEN</td><td>GPIOF时钟使能由软件置1或清0。0: GPIOF时钟关闭1: GPIOF时钟开启</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PDEN</td><td>GPIOD时钟使能由软件置1或清0。0: GPIOD时钟关闭1: GPIOD时钟开启</td></tr><tr><td>19</td><td>PCEN</td><td>GPIOC时钟使能由软件置1或清0。0: GPIOC时钟关闭1: GPIOC时钟开启</td></tr><tr><td>18</td><td>PBEN</td><td>GPIOB时钟使能由软件置1或清0。0: GPIOB时钟关闭</td></tr></table>

<table><tr><td></td><td></td><td>1: GPIOB时钟开启</td></tr><tr><td>17</td><td>PAEN</td><td>GPIOA时钟使能由软件置1或清0。0: GPIOA时钟关闭1: GPIOA时钟开启</td></tr><tr><td>16:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>SRAM1SPEN</td><td>SRAM1接口时钟使能由软件置1或清0来开启/关闭在睡眠模式下的SRAM1时钟。0: 关闭睡眠模式下的SRAM1接口时钟1: 开启睡眠模式下的SRAM1接口时钟</td></tr><tr><td>6</td><td>CRCEN</td><td>CRC时钟使能由软件置1或清0。0: CRC时钟关闭1: CRC时钟开启</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCSPEN</td><td>FMC时钟使能由软件置1或清0来开启/关闭在睡眠模式下的FMC时钟。0: 关闭睡眠模式下的FMC时钟1: 开启睡眠模式下的FMC时钟</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAM0SPEN</td><td>SRAM0接口时钟使能由软件置1或清0来开启/关闭在睡眠模式下的SRAM0时钟。0: 关闭睡眠模式下的SRAM0接口时钟1: 开启睡眠模式下的SRAM0接口时钟</td></tr><tr><td>1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>DMAEN</td><td>DMA时钟使能由软件置1或清0。0: 关闭DMA时钟1: 开启DMA时钟</td></tr></table>

## 4.3.7. APB2 使能寄存器（RCU_APB2EN）

## GD32L233xx 产品

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>保留</td><td>DBGMCUEN</td><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0EN</td><td>保留</td><td>SPI0EN</td><td>TIMER8EN</td><td>保留</td><td>ADCEN</td><td colspan="7">保留</td><td>CMPEN</td><td>SYSCFGEN</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>DBGMCUEN</td><td>DBGMCU时钟使能由软件置1或清0。0:关闭DBGMCU时钟1:开启DBGMCU时钟</td></tr><tr><td>21:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置1或清0。0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0时钟使能由软件置1或清0。0:关闭SPI0时钟1:开启SPI0时钟</td></tr><tr><td>11</td><td>TIMER8EN</td><td>TIMER8定时器时钟使能由软件置1或清0。0:关闭TIMER8定时器时钟1:开启TIMER8定时器时钟</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>ADCEN</td><td>ADC接口时钟使能由软件置1或清0。0:关闭ADC接口时钟1:开启ADC接口时钟</td></tr><tr><td>8:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPEN</td><td>CMP模块时钟使能由软件置1或清0。0:关闭CMP模块时钟1:开启CMP模块时钟</td></tr><tr><td>0</td><td>SYSCFGEN</td><td>系统配置时钟使能</td></tr></table>

由软件置1或清0。

0：关闭系统配置时钟

1：开启系统配置时钟

## GD32L235xx 产品

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>DBGMCUEN</td><td colspan="4">保留</td><td>TIMER40EN</td><td>TIMER14EN</td></tr><tr><td colspan="14">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>USART0EN</td><td>保留</td><td>SPI0EN</td><td>TIMER8EN</td><td>TIMER0EN</td><td>ADCEN</td><td colspan="7">保留</td><td>CMPEN</td><td>SYSCFGEN</td></tr><tr><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="7"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>DBGMCUEN</td><td>DBGMCU时钟使能由软件置1或清0。0:关闭DBGMCU时钟1:开启DBGMCU时钟</td></tr><tr><td>21:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>TIMER40EN</td><td>TIMER40定时器时钟使能由软件置1或清0。0:关闭TIMER40定时器时钟1:开启TIMER40定时器时钟</td></tr><tr><td>16</td><td>TIMER14EN</td><td>TIMER14定时器时钟使能由软件置1或清0。0:关闭TIMER14定时器时钟1:开启TIMER14定时器时钟</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置1或清0。0:关闭USART0时钟1:开启USART0时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>1:开启SPI0时钟</td></tr><tr><td>11</td><td>TIMER8EN</td><td>TIMER8定时器时钟使能由软件置1或清0。0:关闭TIMER8定时器时钟1:开启TIMER8定时器时钟</td></tr><tr><td>10</td><td>TIMER0EN</td><td>TIMER0定时器时钟使能由软件置1或清0。0:关闭TIMER0定时器时钟1:开启TIMER0定时器时钟</td></tr><tr><td>9</td><td>ADCEN</td><td>ADC接口时钟使能由软件置1或清0。0:关闭ADC接口时钟1:开启ADC接口时钟</td></tr><tr><td>8:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPEN</td><td>CMP模块时钟使能由软件置1或清0。0:关闭CMP模块时钟1:开启CMP模块时钟</td></tr><tr><td>0</td><td>SYSCFGEN</td><td>系统配置时钟使能由软件置1或清0。0:关闭系统配置时钟1:开启系统配置时钟</td></tr></table>

## 4.3.8. APB1 使能寄存器（RCU_APB1EN）

GD32L233xx 产品

地址偏移：0x1C

复位值：0x1000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BKPEN</td><td>CTCEN</td><td>DACEN</td><td>PMUEN</td><td colspan="3">保留</td><td>I2C2EN</td><td>USBDEN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>LPUARTEN</td><td>USART1EN</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SPI1EN</td><td colspan="2">保留</td><td>WWDGTEN</td><td>SLCDEN</td><td>LPTIMEREN</td><td>TIMER11EN</td><td colspan="2">保留</td><td>TIMER6EN</td><td>TIMER5EN</td><td colspan="2">保留</td><td>TIMER2EN</td><td>TIMER1EN</td></tr></table>

<table><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BKPEN</td><td>BKP(RTC)时钟使能由软件置1或清0。0:关闭BKT(RTC)时钟1:开启BKP(RTC)时钟</td></tr><tr><td>30</td><td>CTCEN</td><td>CTC时钟使能由软件置1或清0。0:关闭CTC时钟1:开启CTC时钟</td></tr><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置1或清0。0:关闭DAC时钟1:开启DAC时钟</td></tr><tr><td>28</td><td>PMUEN</td><td>电源接口时钟使能由软件置1或清0。0:关闭电源接口时钟1:开启电源接口时钟</td></tr><tr><td>27:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C2EN</td><td>I2C2时钟使能由软件置1或清0。0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>23</td><td>USBDEN</td><td>USBD时钟使能由软件置1或清0。0:关闭USBD时钟1:开启USBD时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置1或清0。0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置1或清0。0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置1或清0。0:关闭UART4时钟1:开启UART4时钟</td></tr></table>

<table><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置1或清0。0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>LPUARTEN</td><td>LPUART时钟使能由软件置1或清0。0:关闭LPUART时钟1:开启LPUART时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置1或清0。0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>16:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置1或清0。0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WWDGTEN</td><td>窗口看门狗定时器时钟使能由软件置1或清0。0:关闭窗口看门狗定时器时钟1:开启窗口看门狗定时器时钟</td></tr><tr><td>10</td><td>SLCDEN</td><td>SLCD时钟使能由软件置1或清0。0:关闭SLCD时钟1:开启SLCD时钟</td></tr><tr><td>9</td><td>LPTIMEREN</td><td>LPTIMER时钟使能由软件置1或清0。0:关闭LPTIMER时钟1:开启LPTIMER时钟</td></tr><tr><td>8</td><td>TIMER11EN</td><td>TIMER11定时器时钟使能由软件置1或清0。0:关闭TIMER11定时器时钟1:开启TIMER11定时器时钟</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6定时器时钟使能由软件置1或清0。0:关闭TIMER6定时器时钟1:开启TIMER6定时器时钟</td></tr></table>

<table><tr><td>4</td><td>TIMER5EN</td><td>TIMER5定时器时钟使能由软件置1或清0。0:关闭TIMER5定时器时钟1:开启TIMER5定时器时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2定时器时钟使能由软件置1或清0。0:关闭TIMER2定时器时钟1:开启TIMER2定时器时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1定时器时钟使能由软件置1或清0。0:关闭TIMER1定时器时钟1:开启TIMER1定时器时钟</td></tr></table>

## GD32L235xx 产品

地址偏移：0x1C

复位值：0x1000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BKPEN</td><td>CTCEN</td><td>DACEN</td><td>PMUEN</td><td colspan="2">保留</td><td>LPUART1EN</td><td>I2C2EN</td><td>USBDEN</td><td>I2C1EN</td><td>I2C0EN</td><td>UART4EN</td><td>UART3EN</td><td>LPUART0EN</td><td>USART1EN</td><td>CANEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>SPI1EN</td><td>保留</td><td>LPTIMER1EN</td><td>WWDGTEN</td><td>SLCDEN</td><td>LPTIMER0EN</td><td>TIMER11EN</td><td colspan="2">保留</td><td>TIMER6EN</td><td>TIMER5EN</td><td colspan="2">保留</td><td>TIMER2EN</td><td>TIMER1EN</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BKPEN</td><td>BKP(RTC)时钟使能由软件置1或清0。0:关闭BKT(RTC)时钟1:开启BKP(RTC)时钟</td></tr><tr><td>30</td><td>CTCEN</td><td>CTC时钟使能由软件置1或清0。0:关闭CTC时钟1:开启CTC时钟</td></tr><tr><td>29</td><td>DACEN</td><td>DAC时钟使能由软件置1或清0。0:关闭DAC时钟1:开启DAC时钟</td></tr></table>

<table><tr><td>28</td><td>PMUEN</td><td>电源接口时钟使能由软件置1或清0。0:关闭电源接口时钟1:开启电源接口时钟</td></tr><tr><td>27:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>LPUART1EN</td><td>LPUART1时钟使能由软件置1或清0。0:关闭LPUART1时钟1:开启LPUART1时钟</td></tr><tr><td>24</td><td>I2C2EN</td><td>I2C2时钟使能由软件置1或清0。0:关闭I2C2时钟1:开启I2C2时钟</td></tr><tr><td>23</td><td>USBDEN</td><td>USBD时钟使能由软件置1或清0。0:关闭USBD时钟1:开启USBD时钟</td></tr><tr><td>22</td><td>I2C1EN</td><td>I2C1时钟使能由软件置1或清0。0:关闭I2C1时钟1:开启I2C1时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置1或清0。0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>UART4EN</td><td>UART4时钟使能由软件置1或清0。0:关闭UART4时钟1:开启UART4时钟</td></tr><tr><td>19</td><td>UART3EN</td><td>UART3时钟使能由软件置1或清0。0:关闭UART3时钟1:开启UART3时钟</td></tr><tr><td>18</td><td>LPUART0EN</td><td>LPUART0时钟使能由软件置1或清0。0:关闭LPUART0时钟1:开启LPUART0时钟</td></tr><tr><td>17</td><td>USART1EN</td><td>USART1时钟使能由软件置1或清0。</td></tr></table>

<table><tr><td></td><td></td><td>1:开启USART1时钟</td></tr><tr><td>16</td><td>CANEN</td><td>CAN时钟使能由软件置1或清0。0:关闭CAN时钟1:开启CAN时钟</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>SPI1EN</td><td>SPI1时钟使能由软件置1或清0。0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>LPTIMER1EN</td><td>LPTIMER1时钟使能由软件置1或清0。0:关闭LPTIMER1时钟1:开启LPTIMER1时钟</td></tr><tr><td>11</td><td>WWDGTEN</td><td>窗口看门狗定时器时钟使能由软件置1或清0。0:关闭窗口看门狗定时器时钟1:开启窗口看门狗定时器时钟</td></tr><tr><td>10</td><td>SLCDEN</td><td>SLCD时钟使能由软件置1或清0。0:关闭SLCD时钟1:开启SLCD时钟</td></tr><tr><td>9</td><td>LPTIMER0EN</td><td>LPTIMER0时钟使能由软件置1或清0。0:关闭LPTIMER0时钟1:开启LPTIMER0时钟</td></tr><tr><td>8</td><td>TIMER11EN</td><td>TIMER11定时器时钟使能由软件置1或清0。0:关闭TIMER11定时器时钟1:开启TIMER11定时器时钟</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6EN</td><td>TIMER6定时器时钟使能由软件置1或清0。0:关闭TIMER6定时器时钟1:开启TIMER6定时器时钟</td></tr><tr><td>4</td><td>TIMER5EN</td><td>TIMER5定时器时钟使能</td></tr></table>

<table><tr><td></td><td></td><td>由软件置1或清0。0:关闭TIMER5定时器时钟1:开启TIMER5定时器时钟</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER2EN</td><td>TIMER2定时器时钟使能由软件置1或清0。0:关闭TIMER2定时器时钟1:开启TIMER2定时器时钟</td></tr><tr><td>0</td><td>TIMER1EN</td><td>TIMER1定时器时钟使能由软件置1或清0。0:关闭TIMER1定时器时钟1:开启TIMER1定时器时钟</td></tr></table>

## 4.3.9. 备份域控制寄存器（RCU_BDCTL）

地址偏移：0x20

复位值：0x0000 0018，由备份域复位电路复位

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

注意：备份域控制寄存器（BDCTL）的LXTALEN, LXTALBPS, RTCSRC和RTCEN位仅在备份域复位后才清0。只有在电源控制寄存器（PMU_CTL）中的BKPWEN位置1后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>BKPRST</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td colspan="3">保留</td><td colspan="2">LXTALDRI[1:0]</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份域复位由软件置1或清0。0:无复位1:复位备份域</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置1或清0。0:关闭RTC时钟1:开启RTC时钟</td></tr></table>

<table><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟入口选择软件置位或清除来控制RTC时钟源。00:没有时钟01:选择LXTAL时钟作为RTC时钟源10:选择IRC32K时钟作为RTC时钟源11:选择HXTAL时钟32分频作为RTC时钟源</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:3</td><td>LXTALDRI[1:0]</td><td>LXTAL驱动能力软件置位或清除。当复位备份域时,会重装载缺省值。00:弱驱动能力01:中低驱动能力10:中高驱动能力11:强驱动能力(复位后的缺省值)注意:LXTALDRI在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能软件置1和清0。0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>外部低速振荡器稳定状态位硬件置1来指示LXTAL输出时钟是否稳定待用。0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL使能软件置1和清0。0:关闭LXTAL1:开启LXTAL</td></tr></table>

## 4.3.10. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x24

复位值：0x0C80 0000，除复位标志外由系统复位清除，复位标志只能由电源复位清除。

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>保留</td><td>RSTFC</td><td>V11RSTF</td><td colspan="7">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td>rw</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC32KSTB</td><td>IRC32KEN</td></tr></table>


描述


<table><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位深度睡眠/待机复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无窗口看门狗定时器复位发生1:发生窗口看门狗定时器复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位电源复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位当有外部引脚复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位。0:无作用1:清除复位标志位</td></tr><tr><td>23</td><td>V11RSTF</td><td>1.1V域电源复位标志位当有1.1V域电源复位发生时由硬件置1。</td></tr></table>

<table><tr><td></td><td></td><td>由软件通过写1到RSTFC位来清除该位。0:无1.1V域电源复位发生1:发生1.1V域电源复位</td></tr><tr><td>22:2</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>1</td><td>IRC32KSTB</td><td>IRC32K时钟稳定状态位该位由硬件置1指示IRC32K输出时钟是否稳定待用。0:IRC32K时钟未稳定1:IRC32K时钟已稳定</td></tr><tr><td>0</td><td>IRC32KEN</td><td>IRC32K时钟使能软件置1和清0。0:关闭IRC32K时钟1:开启IRC32K时钟</td></tr></table>

## 4.3.11. AHB 复位寄存器（RCU_AHBRST）

地址偏移：0x28

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PFRST</td><td>保留</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>CRCRST</td><td colspan="6">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PFRST</td><td>GPIOF复位由软件置1或清0。0:无作用1:复位GPIOF口</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PDRST</td><td>GPIOD复位由软件置1或清0。0:无作用1:复位GPIOD口</td></tr><tr><td>19</td><td>PCRST</td><td>GPIOC复位由软件置1或清0。0:无作用1: 复位GPIOC口</td></tr><tr><td>18</td><td>PBRST</td><td>GPIOB复位由软件置1或清0。0: 无作用1: 复位GPIOB口</td></tr><tr><td>17</td><td>PARST</td><td>GPIOA复位由软件置1或清0。0: 无作用1: 复位GPIOA口</td></tr><tr><td>16:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CRCRST</td><td>CRC复位由软件置1或清0。0: 无作用1: 复位CRC</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.12. 配置寄存器 1（RCU_CFG1）

地址偏移：0x2C

复位值：0x0000 0007

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>SSCS[2]</td><td>SCS[2]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">PREDV[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SSCS[2]</td><td>SSCS的位2,仅适用于GD32L235xx产品参考RCU_CFG0的位3:2</td></tr><tr><td>16</td><td>SCS[2]</td><td>SCS的位2,仅适用于GD32L235xx产品参考RCU_CFG0的位1:0</td></tr><tr><td>15:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>PREDV[3:0]</td><td>PLL输入源分频因子由软件置1或清0。这些位仅能在PLL关闭时改写。时钟分频因子为(PREDV + 1)。0000:PRDEV输入时钟源不分频</td></tr></table>

<table><tr><td>0001: PRDEV输入时钟源2分频</td></tr><tr><td>0010: PRDEV输入时钟源3分频</td></tr><tr><td>0011: PRDEV输入时钟源4分频</td></tr><tr><td>0100: PRDEV输入时钟源5分频</td></tr><tr><td>0101: PRDEV输入时钟源6分频</td></tr><tr><td>0110: PRDEV输入时钟源7分频</td></tr><tr><td>0111: PRDEV输入时钟源8分频</td></tr><tr><td>1000: PRDEV输入时钟源9分频</td></tr><tr><td>1001: PRDEV输入时钟源10分频</td></tr><tr><td>1010: PRDEV输入时钟源11分频</td></tr><tr><td>1011: PRDEV输入时钟源12分频</td></tr><tr><td>1100: PRDEV输入时钟源13分频</td></tr><tr><td>1101: PRDEV输入时钟源14分频</td></tr><tr><td>1110: PRDEV输入时钟源15分频</td></tr><tr><td>1111: PRDEV输入时钟源16分频</td></tr></table>

## 4.3.13. 配置寄存器 2（RCU_CFG2）

GD32L233xx 产品

地址偏移：0x30

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">ADCPS</td><td rowspan="2" colspan="9">保留</td><td rowspan="2" colspan="3">IRC16MDIV</td><td rowspan="2" colspan="2">USART1SEL[1:0]</td></tr><tr><td colspan="2">C[3:2]</td></tr><tr><td colspan="11">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>USBDSEL</td><td colspan="2">LPUART[1:0]</td><td colspan="2">LPTIMERSEL[1:0]</td><td>ADCSEL</td><td colspan="2">I2C2SEL[1:0]</td><td colspan="2">I2C1SEL[1:0]</td><td colspan="2">I2C0SEL[1:0]</td><td colspan="2">USART0SEL[1:0]</td></tr><tr><td colspan="2"></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>ADCPSC[3:2]</td><td>ADCPSC的位3和位2参考RCU_CFG0的位15:14</td></tr><tr><td>29:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:18</td><td>IRC16MDIV</td><td>CK_IRC16M时钟分频选择作为CK_IRC16MDIV时钟0xx:选择CK_IRC16M作为CK_IRC16MDIV时钟100:选择CK_IRC16M/2作为CK_IRC16MDIV时钟101:选择CK_IRC16M/4作为CK_IRC16MDIV时钟110:选择CK_IRC16M/8作为CK_IRC16MDIV时钟111:选择CK_IRC16M/16作为CK_IRC16MDIV时钟</td></tr><tr><td>17:16</td><td>USART1SEL[1:0]</td><td>USART1时钟源选择由软件置1或清0。00:USART1时钟选择CK_APB101:USART1时钟选择CK_SYS10:USART1钟选择CK_LXTAL11:USART1钟选择CK_IRC16M</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>USBDSEL</td><td>USBD时钟源选择由软件置1或清0。0:USART时钟选择IRC48M1:USART时钟选择CK_PLL</td></tr><tr><td>12:11</td><td>LPUARTSEL[1:0]</td><td>LPUART时钟源选择由软件置1或清0。00:LPUART时钟选择CK_APB101:LPUART时钟选择CK_SYS10:LPUART钟选择CK_LXTAL11:LPUART钟选择CK_IRC16MDIV</td></tr><tr><td>10:9</td><td>LPTIMERSEL[1:0]</td><td>LPTIMER时钟源选择由软件置1或清0。00:LPTIMER时钟选择CK_APB201:LPTIMER时钟选择CK_IRC32K10:LPTIMER钟选择CK_LXTAL11:LPTIMER钟选择CK_IRC16MDIV</td></tr><tr><td>8</td><td>ADCSEL</td><td>ADC时钟源选择由软件置1或清0。0:ADC时钟源选择IRC16M时钟1:ADC时钟源选择由APB2时钟经2、4、6、8、10、12、14、16分频或由AHB时钟经3、5、7、9、11、13、15、17分频</td></tr><tr><td>7:6</td><td>I2C2SEL[1:0]</td><td>CK_I2C2时钟源选择00:CK_I2C2时钟选择CK_APB101:CK_I2C2时钟选择CK_SYS10/11:CK_I2C2时钟选择CK_IRC16MDIV</td></tr><tr><td>5:4</td><td>I2C1SEL[1:0]</td><td>CK_I2C1时钟源选择00:CK_I2C1时钟选择CK_APB101:CK_I2C1时钟选择CK_SYS10/11:CK_I2C1时钟选择CK_IRC16MDIV</td></tr><tr><td>3:2</td><td>I2C0SEL[1:0]</td><td>CK_I2C0时钟源选择00:CK_I2C0时钟选择CK_APB101:CK_I2C0时钟选择CK_SYS10/11:CK_I2C0时钟选择CK_IRC16MDIV</td></tr><tr><td>1:0</td><td>USART0SEL[1:0]</td><td>USART0时钟源选择</td></tr></table>

由软件置1或清0。

00：USART0时钟选择APB2时钟

01：USART0时钟选择CK_SYS

10：USART0时钟选择LXTAL时钟

11：USART0时钟选择IRC16MDIV时钟

## GD32L235xx 产品

地址偏移：0x30

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">ADCPSC[3:2]</td><td colspan="4">保留</td><td colspan="2">LPUART1SEL[1:0]</td><td>保留</td><td colspan="2">LPTIMER1SEL[1:0]</td><td colspan="3">IRC16MDIVSEL</td><td colspan="2">USART1SEL[1:0]</td></tr><tr><td colspan="6">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>USBDSEL</td><td colspan="2">LPUART0SEL[1:0]</td><td colspan="2">LPTIMER0SEL[1:0]</td><td>ADCSEL</td><td colspan="2">I2C2SEL[1:0]</td><td colspan="2">I2C1SEL[1:0]</td><td colspan="2">I2C0SEL[1:0]</td><td colspan="2">USART0SEL[1:0]</td></tr><tr><td colspan="2"></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>ADCPSC[3:2]</td><td>ADCPSC的位3和位2参考RCU_CFG0的位15:14</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>LPUART1SEL[1:0]</td><td>LPUART1时钟源选择由软件置1或清0。00:LPUART1时钟选择CK_APB101:LPUART1时钟选择CK_SYS10:LPUART1钟选择CK_LXTAL11:LPUART1钟选择CK_IRC16MDIV</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:21</td><td>LPTIMER1SEL[1:0]</td><td>LPTIMER1时钟源选择由软件置1或清0。00:LPTIMER1时钟选择CK_APB101:LPTIMER1时钟选择CK_IRC32K10:LPTIMER1钟选择CK_LXTAL11:LPTIMER1钟选择CK_IRC16MDIV</td></tr><tr><td>20:18</td><td>IRC16MDIV</td><td>CK_IRC16M时钟分频选择作为CK_IRC16MDIV时钟0xx:选择CK_IRC16M作为CK_IRC16MDIV时钟100:选择CK_IRC16M/2作为CK_IRC16MDIV时钟101:选择CK_IRC16M/4作为CK_IRC16MDIV时钟110:选择CK_IRC16M/8作为CK_IRC16MDIV时钟</td></tr><tr><td>17:16</td><td>USART1SEL[1:0]</td><td>USART1时钟源选择由软件置1或清0。00: USART1时钟选择CK_APB101: USART1时钟选择CK_SYS10: USART1钟选择CK_LXTAL11: USART1钟选择CK_IRC16M</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>USBDSEL</td><td>USBD时钟源选择由软件置1或清0。0: USBD时钟选择IRC48M1: USBD时钟选择CK_PLL</td></tr><tr><td>12:11</td><td>LPUART0SEL[1:0]</td><td>LPUART0时钟源选择由软件置1或清0。00: LPUART0时钟选择CK_APB101: LPUART0时钟选择CK_SYS10: LPUART0钟选择CK_LXTAL11: LPUART0钟选择CK_IRC16MDIV</td></tr><tr><td>10:9</td><td>LPTIMER0SEL[1:0]</td><td>LPTIMER0时钟源选择由软件置1或清0。00: LPTIMER0时钟选择CK_APB101: LPTIMER0时钟选择CK_IRC32K10: LPTIMER0钟选择CK_LXTAL11: LPTIMER0钟选择CK_IRC16MDIV</td></tr><tr><td>8</td><td>ADCSEL</td><td>ADC时钟源选择由软件置1或清0。0: ADC时钟源选择IRC16M时钟1: ADC时钟源选择由APB2时钟经2、4、6、8、10、12、14、16分频或由AHB时钟经3、5、7、9、11、13、15、17分频</td></tr><tr><td>7:6</td><td>I2C2SEL[1:0]</td><td>CK_I2C2时钟源选择00: CK_I2C2时钟选择CK_APB101: CK_I2C2时钟选择CK_SYS10/11: CK_I2C2时钟选择CK_IRC16MDIV</td></tr><tr><td>5:4</td><td>I2C1SEL[1:0]</td><td>CK_I2C1时钟源选择00: CK_I2C1时钟选择CK_APB101: CK_I2C1时钟选择CK_SYS10/11: CK_I2C1时钟选择CK_IRC16MDIV</td></tr><tr><td>3:2</td><td>I2C0SEL[1:0]</td><td>CK_I2C0时钟源选择00: CK_I2C0时钟选择CK_APB101: CK_I2C0时钟选择CK_SYS</td></tr></table>

10/11：CK_I2C0时钟选择CK_IRC16MDIV

由软件置1或清0。

## 4.3.14. AHB2 使能寄存器（RCU_AHB2EN）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12"></td><td>TRNGEN</td><td>保留</td><td>CAUEN</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>TRNGEN</td><td>TRNG时钟使能由软件置1或清0。0: TRNG时钟关闭1: TRNG时钟开启</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CAUEN</td><td>CAU时钟使能由软件置1或清0。0: CAU时钟关闭1: CAU时钟开启</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.15. AHB2 复位寄存器（RCU_AHB2RST）

地址偏移：0x38

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12"></td><td>TRNGRST</td><td>保留</td><td>CAURST</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>TRNGRST</td><td>TRNG复位由软件置1或清0。0:无作用1:复位TRNG</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CAURST</td><td>CAU复位由软件置1或清0。0:无作用1:复位CAU</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.16. 电源解锁寄存器（RCU_VKEY）

地址偏移：0x100

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>GD32L233xx产品RCU_LP寄存器解锁这些位只能被软件写,读的话全是0。只有在向RCU_VKEY寄存器写0x1A2B3C4D后,RCU_LP寄存器才能被写。</td></tr><tr><td></td><td></td><td>GD32L235xx产品RCU_LP寄存器解锁这些位只能被软件写,读的话全是0。只有在向RCU_VKEY寄存器写0x00007432后,RCU_LP寄存器才能被写。</td></tr></table>

## 4.3.17. 低功耗模式寄存器（RCU_LPB）

GD32L233xx 产品

地址偏移：0x12C

复位值：0x0000 0007

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">LPBMSEL[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>LPBMSEL[2:0]</td><td>低功耗模式选择信号。控制采样保持电路保持相的时间长度。该位域只能在RCU_VKEY寄存器中写入正确的秘钥值,才可以写入。011:保持相的时间长度为典型值3.2ms,32个时钟周期010:保持相的时间长度为典型值6.4ms,64个时钟周期001:保持相的时间长度为典型值12.8ms,128个时钟周期000:保持相的时间长度为典型值25.6ms,256个时钟周期111:保持相的时间长度为典型值51.2ms,512个时钟周期110:保持相的时间长度为典型值102.4ms,1024个时钟周期101:保持相的时间长度为典型值204.8ms,2048个时钟周期100:保持相的时间长度为典型值204.8ms,2048个时钟周期</td></tr></table>

GD32L235xx 产品

地址偏移：0x12C

复位值：0x0000 000F

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">LPBMSEL[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>LPBMSEL[3:0]</td><td>低功耗模式选择信号。控制采样保持电路保持相的时间长度。</td></tr></table>

该位域只能在RCU_VKEY寄存器中写入正确的秘钥值，才可以写入。

1011：保持相的时间长度为典型值3.2ms，32个时钟周期

1010：保持相的时间长度为典型值6.4ms，64个时钟周期

1001：保持相的时间长度为典型值12.8ms，128个时钟周期

1000：保持相的时间长度为典型值25.6ms，256个时钟周期

1111：保持相的时间长度为典型值51.2ms，512个时钟周期

1110：保持相的时间长度为典型值102.4ms，1024个时钟周期

1101：保持相的时间长度为典型值204.8ms，2048个时钟周期

1100：保持相的时间长度为典型值307.2ms，3072个时钟周期

0011：保持相的时间长度为典型值409.6ms，4096个时钟周期

0010：保持相的时间长度为典型值512ms，5120个时钟周期

0001：保持相的时间长度为典型值614.4ms，6144个时钟周期

0000：保持相的时间长度为典型值716.8ms，7168个时钟周期

0111：保持相的时间长度为典型值819.2ms，8192个时钟周期

0110：保持相的时间长度为典型值1024ms，10240个时钟周期

0101：保持相的时间长度为典型值1228.8ms，12288个时钟周期

0100：保持相的时间长度为典型值1638.4ms，16384个时钟周期
