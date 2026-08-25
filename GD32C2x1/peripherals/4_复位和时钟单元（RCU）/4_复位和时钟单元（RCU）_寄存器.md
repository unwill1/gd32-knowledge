## 4.3. RCU 寄存器

RCU 基地址：0x4002 1000

## 4.3.1. 控制寄存器（RCU_CTL0）

地址偏移：0x00

复位值：0x4400 XX43，X 表示未定义。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">HIRCDIV_SYS[2:0]</td><td>HIRC_PEREN</td><td colspan="3">HIRCDIV_PER[2:0]</td><td>HIRCSEL</td><td colspan="4">保留</td><td>CKMEN</td><td>HXTALBPS</td><td>HXTALSTB</td><td>HXTALEN</td></tr><tr><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IRC48MCALIB[7:0]</td><td colspan="6">IRC48MADJ[5:0]</td><td>HIRCSTB</td><td>HIRCEN</td></tr><tr><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>HIRCDIV_SYS[2:0]</td><td>HIRC时钟分频系数用于系统时钟这些位由软件设置HIRC时钟分频器的分频系数,以产生CK_HIRCDIV_SYS时钟。000: CK_HIRCDIV_SYS = CK_HIRC / 1001: CK_HIRCDIV_SYS = CK_HIRC / 2010: CK_HIRCDIV_SYS = CK_HIRC / 4 (复位值)011: CK_HIRCDIV_SYS= CK_HIRC / 8100: CK_HIRCDIV_SYS = CK_HIRC / 16101: CK_HIRCDIV_SYS = CK_HIRC / 32110: CK_HIRCDIV_SYS = CK_HIRC / 64111: CK_HIRCDIV_SYS = CK_HIRC / 128</td></tr><tr><td>28</td><td>HIRC_PEREN</td><td>HIRC时钟提供给外设始终使能。该位由软件设置和清除。置位该位会当MCU在正常工作模式和深度睡眠模式下使能HIRC振荡器,而不考虑HIRCEN位的状态。HIRC时钟只能提供给已配置HIRC为时钟源的USART0, I2C0和I2C1外设。0: HIRC振荡器使能取决于HIRCEN位1: HIRC振荡器在MCU运行模式和深度睡眠模式下都是使能的注意:在深度睡眠模式下保持HIRC使能,可以加速串行接口通信,因为HIRC时钟在退出深度睡眠模式时立即准备就绪。</td></tr><tr><td>27:25</td><td>HIRCDIV_PER[2:0]</td><td>由软件控制的这些位设置外设时钟分频器的分频系数,以产CK_HIRCDIV_PER时钟。000: CK_HIRCDIV_PER = CK_HIRC / 1001: CK_HIRCDIV_PER = CK_HIRC / 2010: CK_HIRCDIV_PER = CK_HIRC / 3(复位值)011: CK_HIRCDIV_PER = CK_HIRC / 4100: CK_HIRCDIV_PER = CK_HIRC / 5101: CK_HIRCDIV_PER = CK_HIRC / 6110: CK_HIRCDIV_PER = CK_HIRC / 7111: CK_HIRCDIV_PER = CK_HIRC / 8</td></tr><tr><td>24</td><td>HIRCSEL</td><td>内部48/12 MHz RC振荡器选择0: 48MHz1: 12MHz注意:软件必须确保在进行Flash擦除/写入操作期间,HIRCSEL配置不能被修改。Flash擦除/写入需要使用CK_HIRC,高速内部振荡器的频率在擦除/写入过程中不能更改。如果在擦除/写入过程中配置HIRCSEL,则该配置不会生效。</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>CKMEN</td><td>HXTAL时钟监视使能0:禁止外部4~48 MHz晶体振荡器(HXTAL)时钟监视器1:使能外部4~48 MHz晶体振荡器(HXTAL)时钟监视器当硬件监测到HXTAL时钟一直停留在低或者高的状态,内部硬件将切换系统时钟到HIRC RC时钟。恢复原来系统时钟的方式有以下几种:外部复位,上电复位,软件清CKMIF位。注意:使能HXTAL时钟监视器以后,硬件无视控制位HIRCEN的状态,自动使能HIRC时钟。</td></tr><tr><td>18</td><td>HXTALBPS</td><td>外部晶体振荡器(HXTAL)时钟旁路模式使能只有在HXTALEN位为0时,HXTALBPS位才可写。0:禁止HXTAL旁路模式1:使能HXTAL旁路模式,HXTAL输出时钟等于输入时钟</td></tr><tr><td>17</td><td>HXTALSTB</td><td>外部晶体振荡器(HXTAL)时钟稳定状态标志位硬件置'1'来指示HXTAL振荡器时钟是否稳定待用。0:HXTAL振荡器未稳定1:HXTAL振荡器已稳定</td></tr><tr><td>16</td><td>HXTALEN</td><td>外部高速振荡器时钟使能软件置'1'或清'0'。如果HXTAL时钟作为系统时钟,该位不能被复位。进入深度睡眠或待机模式时硬件自动复位。0:禁止外部4~48 MHz晶体振荡器1:使能外部4~48 MHz晶体振荡器</td></tr><tr><td>15:8</td><td>IRC48MCALIB[7:0]</td><td>高速内部振荡器校准值寄存器上电时自动加载这些位</td></tr><tr><td>7:2</td><td>IRC48MADJ[5:0]</td><td>高速内部振荡器时钟调整值这些位由软件置位,最终调整值为IRC48MADJ当前值加上IRC48MCALIB[7:0]位的值。最终调整值应该调整IRC48M到48MHz±1%。</td></tr><tr><td>1</td><td>HIRCSTB</td><td>高速内部(HIRC)时钟稳定状态标志位硬件置'1'来指示HIRC振荡器时钟是否稳定待用。0:HIRC振荡器未稳定</td></tr><tr><td>0</td><td>HIRCEN</td><td>高速内部振荡器使能软件复位置位。如果HIRC时钟用作系统时钟时该位不能被复位。当从待机或深度睡眠模式返回或在HXTALCKM置位的情况下用作系统时钟的HXTAL振荡器发生故障时,该位由硬件置1来启动HIRC振荡器。0: 内部48 MHz RC振荡器关闭1: 内部48 MHz RC振荡器开启</td></tr></table>

## 4.3.2. 配置寄存器 0（RCU_CFG0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td colspan="3">CKOUT0DIV[2:0]</td><td>保留</td><td colspan="3">CKOUT0SEL[2:0]</td><td>保留</td><td colspan="3">CKOUT1DIV[2:0]</td><td>保留</td><td colspan="3">CKOUT1SEL[2:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="3">APBPSC[2:0]</td><td colspan="3">保留</td><td colspan="4">AHBPSC[3:0]</td><td colspan="2">SCSS[1:0]</td><td colspan="2">SCS[1:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="2">r</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30:28</td><td>CKOUT0DIV[2:0]</td><td>CK_OUT0分频器,用来降低CK_OUT0频率CK_OUT0的选择参考RCU_CFG0的26:24位。000: CK_OUT0不分频001: CK_OUT0 2分频010: CK_OUT0 4分频011: CK_OUT0 8分频100: CK_OUT0 16分频101: CK_OUT0 32分频110: CK_OUT0 64分频111: CK_OUT0 128分频</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>CKOUT0SEL[2:0]</td><td>CK_OUT0时钟源选择软件置位或清零。000: 没有时钟被选择001: 选择系统时钟010: 保留011: 选择内部48M RC振荡器时钟100: 选择外部高速振荡器时钟101: 保留</td></tr></table>

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td>110:选择内部32K RC振荡器时钟</td></tr><tr><td>111:选择外部低速振荡器时钟</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:20</td><td>CKOUT1DIV[2:0]</td><td>CK_OUT1分频器,来降低CK_OUT1频率CK_OUT1的选择参考RCU_CFG0的18:16位。000:CK_OUT1不分频001:CK_OUT1 2分频010:CK_OUT1 4分频011:CK_OUT1 8分频100:CK_OUT1 16分频101:CK_OUT1 32分频110:CK_OUT1 64分频111:CK_OUT1 128分频</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>CKOUT1SEL[2:0]</td><td>CK_OUT1时钟源选择软件置位或清零。000:没有时钟被选择001:选择系统时钟010:保留011:选择内部48M RC振荡器时钟100:选择外部高速振荡器时钟101:保留110:选择内部32K RC振荡器时钟111:选择外部低速振荡器时钟</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:11</td><td>APBPSC[2:0]</td><td>APB预分频选择软件置1和清0来控制APB时钟分频因子。0xx:选择AHB时钟不分频100:选择AHB时钟2分频101:选择AHB时钟4分频110:选择AHB时钟8分频111:选择AHB时钟16分频</td></tr><tr><td>10:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>AHBPSC[3:0]</td><td>AHB预分频选择软件设置和清除来控制AHB时钟分频因子。0xxx:选择CK_SYS系统时钟不分频1000:选择CK_SYS系统时钟2分频1001:选择CK_SYS系统时钟4分频1010:选择CK_SYS系统时钟8分频1011:选择CK_SYS系统时钟16分频</td></tr></table>

<table><tr><td></td><td></td><td>1100:选择CK_SYS系统时钟64分频</td></tr><tr><td></td><td></td><td>1101:选择CK_SYS系统时钟128分频</td></tr><tr><td></td><td></td><td>1110:选择CK_SYS系统时钟256分频</td></tr><tr><td></td><td></td><td>1111:选择CK_SYS系统时钟512分频</td></tr><tr><td>3:2</td><td>SCSS[1:0]</td><td>系统时钟转换状态</td></tr><tr><td></td><td></td><td>硬件设置和清除指示系统当前时钟源</td></tr><tr><td></td><td></td><td>00:选择CK_HIRCDIV_SYS作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>01:选择CK_HXTAL作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>10:选择CK_IRC32K作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>11:选择CK_LXTAL作为CK_SYS系统时钟源</td></tr><tr><td>1:0</td><td>SCS[1:0]</td><td>系统时钟转换</td></tr><tr><td></td><td></td><td>软件设置选择系统时钟源。由于CK_SYS的改变有固有的延迟,需要软件读SCSS位来确保转换是否结束。</td></tr><tr><td></td><td></td><td>00:选择CK_HIRCDIV_SYS时钟作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>01:选择HXTAL时钟作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>10:选择IRC32K作为CK_SYS系统时钟源</td></tr><tr><td></td><td></td><td>11:选择LXTAL作为CK_SYS系统时钟源</td></tr></table>

## 4.3.3. 中断寄存器（RCU_INT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>CKMIC</td><td>LCKMIC</td><td colspan="2">保留</td><td>HXTALSTBIC</td><td>HIRCSTBIC</td><td>LXTALSTBIC</td><td>IRC32KSTBIC</td></tr><tr><td colspan="8"></td><td>w</td><td>w</td><td colspan="2"></td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>HXTALSTBIE</td><td>HIRCSTBIE</td><td>LXTALSTBIE</td><td>IRC32KSTBIE</td><td>CKMIF</td><td>LCKMIF</td><td colspan="2">保留</td><td>HXTALSTBIF</td><td>HIRCSTBIF</td><td>LXTALSTBIF</td><td>IRC32KSTBIF</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>CKMIC</td><td>HXTAL时钟阻塞中断清除软件写1复位CKMIF标志位。0:不复位CKMIF标志位1:复位CKMIF标志位</td></tr><tr><td>22</td><td>LCKMIC</td><td>LXTAL时钟阻塞中断清除软件写1复位LCKMIF标志位。0:不复位LCKMIF标志位</td></tr></table>

<table><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>HXTALSTBIC</td><td>HXTAL时钟稳定中断清除软件写1复位HXTALSTBIF标志位。0:不复位HXTALSTBIF标志位1:复位HXTALSTBIF标志位</td></tr><tr><td>18</td><td>HIRCSTBIC</td><td>HIRC时钟稳定中断清除软件写1复位HIRCSTBIF标志位。0:不复位HIRCSTBIF标志位1:复位HIRCSTBIF标志位</td></tr><tr><td>17</td><td>LXTALSTBIC</td><td>LXTAL时钟稳定中断清除软件写1复位LXTALSTBIF标志位。0:不复位LXTALSTBIF标志位1:复位LXTALRDYF标志位</td></tr><tr><td>16</td><td>IRC32KSTBIC</td><td>IRC32K时钟稳定中断清除软件写1复位IRC32KSTBIF标志位。0:不复位IRC32KSTBIF标志位1:复位IRC32KSTBIF标志位</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>HXTALSTBIE</td><td>HXTAL时钟稳定中断使能软件置1和清0来使能/禁止HXTAL时钟稳定中断。0:禁止HXTAL时钟稳定中断1:使能HXTAL时钟稳定中断</td></tr><tr><td>10</td><td>HIRCSTBIE</td><td>HIRC时钟稳定中断使能软件置1和清0来使能/禁止HIRC时钟稳定中断。0:禁止HIRC时钟稳定中断1:使能HIRC时钟稳定中断</td></tr><tr><td>9</td><td>LXTALSTBIE</td><td>LXTAL时钟稳定中断使能LXTAL时钟稳定中断使能/禁止控制。0:禁止LXTAL时钟稳定中断1:使能LXTAL时钟稳定中断</td></tr><tr><td>8</td><td>IRC32KSTBIE</td><td>IRC32K时钟稳定中断使能IRC32K时钟稳定中断使能/禁止控制。0:禁止IRC32K时钟稳定中断1:使能IRC32K时钟稳定中断</td></tr><tr><td>7</td><td>CKMIF</td><td>HXTAL时钟阻塞中断标志位当HXTAL时钟阻塞时硬件置1。软件置CKMIC=1时清除该位。0:时钟运行正常</td></tr></table>

<table><tr><td>6</td><td>LCKMIF</td><td>LXTAL时钟阻塞中断标志位当LXTAL时钟阻塞由硬件置1。软件置位LCKMIC时清除该位。0:LXTAL时钟运行正常1:LXTAL时钟阻塞</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>HXTALSTBIF</td><td>HXTAL时钟稳定中断标志位当外部4~48MHz晶体振荡器时钟稳定且HXTALSTBIE位被置1时由硬件置1。软件置HXTALSTBIC=1时清除该位。0:无HXTAL时钟稳定中断发生1:发生HXTAL时钟稳定中断</td></tr><tr><td>2</td><td>HIRCSTBIF</td><td>HIRC时钟稳定中断标志位当内部48MHz RC振荡器时钟稳定且HIRCSTBIE位被置1时由硬件置1。软件置HIRCSTBIC=1时清除该位。0:无HIRC时钟稳定中断产生1:产生HIRC时钟稳定中断</td></tr><tr><td>1</td><td>LXTALSTBIF</td><td>LXTAL时钟稳定中断标志位当外部32.768KHz晶体振荡器时钟稳定且LXTALSTBIE为被置1时由硬件置1。软件置LXTALSTBIC=1时清除该位。0:无LXTAL时钟稳定中断发生1:发生LXTAL时钟稳定中断</td></tr><tr><td>0</td><td>IRC32KSTBIF</td><td>IRC32K时钟稳定中断标志位当内部32KHz RC振荡器时钟稳定且IRC32KSTBIE位被置1时由硬件置1。软件置IRC32KSTBIC=1时清除该位。0:无IRC32K时钟稳定中断产生1:产生IRC32K时钟稳定中断</td></tr></table>

## 4.3.4. AHB1 复位寄存器（RCU_AHB1RST）

地址偏移：0x10

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>DMAMUXRST</td><td>保留</td><td>DMARST</td><td colspan="5">保留</td></tr><tr><td colspan="9">rw</td><td colspan="7">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CRCRST</td><td colspan="12">保留</td></tr><tr><td colspan="3">位/位域</td><td>名称</td><td colspan="12">描述</td></tr><tr><td colspan="3">31:24</td><td>保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td colspan="3">23</td><td>DMAMUXRST</td><td colspan="12">DMAMUX复位由软件置1或清0。0:无复位1:复位DMAMUX</td></tr><tr><td colspan="3">22</td><td>保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td colspan="3">21</td><td>DMARST</td><td colspan="12">DMA复位由软件置1或清0。0:无复位1:复位DMA</td></tr><tr><td colspan="3">20:13</td><td>保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td colspan="3">12</td><td>CRCRST</td><td colspan="12">CRC复位由软件置1或清0。0:无复位1:复位CRC</td></tr><tr><td colspan="3">11:0</td><td>保留</td><td colspan="12">必须保持复位值。</td></tr></table>

## 4.3.5. AHB2 复位寄存器（RCU_AHB2RST）

地址偏移：0x14

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>PFRST</td><td>保留</td><td>PDRST</td><td>PCRST</td><td>PBRST</td><td>PARST</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:23</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>22</td><td colspan="3">PFRST</td><td colspan="12">GPIO端口F复位由软件置位或复位0:无作用1:复位GPIO端口F</td></tr><tr><td>21</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>20</td><td colspan="3">PDRST</td><td colspan="12">GPIO端口D复位</td></tr></table>

<table><tr><td></td><td></td><td>由软件置位或复位0:无作用1:复位GPIO端口D</td></tr><tr><td>19</td><td>PCRST</td><td>GPIO端口C复位由软件置位或复位0:无作用1:复位GPIO端口C</td></tr><tr><td>18</td><td>PBRST</td><td>GPIO端口B复位由软件置位或复位0:无作用1:复位GPIO端口B</td></tr><tr><td>17</td><td>PARST</td><td>GPIO端口A复位由软件置位或复位0:无作用1:复位GPIO端口A</td></tr><tr><td>16:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.6. APB 复位寄存器（RCU_APBRST）

地址偏移：0x24

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMURST</td><td colspan="5">保留</td><td>I2C1RST</td><td>I2C0RST</td><td>保留</td><td>USART2RST</td><td>TIMER16RST</td><td>TIMER15RST</td><td>TIMER13RST</td></tr><tr><td colspan="3"></td><td>rw</td><td colspan="5"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>USART1RST</td><td>USART0RST</td><td>SPI1RST</td><td>SPI0RST</td><td>TIMER2RST</td><td>TIMER0RST</td><td>ADCRST</td><td>WWDGTRST</td><td colspan="6">保留</td><td>CMPRST</td><td>SYSCFGRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="6"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMURST</td><td>电源控制复位由软件置1或清0。0:无复位1:复位电源控制单元</td></tr><tr><td>27:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1RST</td><td>I2C1复位由软件置1或清0。</td></tr></table>

0: 无复位
1: 复位I2C1

21 I2C0RST I2C0复位
由软件置1或清0。
0: 无复位
1: 复位I2C0

20 保留 必须保持复位值。

19 USART2RST USART2复位
由软件置1或清0。
0: 无复位
1: 复位USART2

18 TIMER16RST TIMER16定时器复位
由软件置1或清0。
0: 无复位
1: 复位TIMER16定时器

17 TIMER15RST TIMER15定时器复位
由软件置1或清0。
0: 无复位
1: 复位TIMER15定时器

16 TIMER13RST TIMER13定时器复位
由软件置1或清0。
0: 无复位
1: 复位TIMER13定时器

15 USART1RST USART1定时器复位
由软件置1或清0。
0: 无复位
1: 复位USART1定时器

14 USART0RST USART0定时器复位
由软件置1或清0。
0: 无复位
1: 复位USART0定时器

13 SPI1RST SPI1复位
由软件置1或清0。
0: 无复位
1: 复位SPI1

12 SPI0RST SPI0复位
由软件置1或清0。
0: 无复位
1: 复位SPI0

<table><tr><td>11</td><td>TIMER2RST</td><td>TIMER2定时器复位由软件置1或清0。0:无复位1:复位TIMER2定时器</td></tr><tr><td>10</td><td>TIMER0RST</td><td>TIMER0定时器复位由软件置1或清0。0:无复位1:复位TIMER0定时器</td></tr><tr><td>9</td><td>ADCRST</td><td>ADC复位由软件置1或清0。0:无复位1:复位ADC</td></tr><tr><td>8</td><td>WWDGTRST</td><td>WWDGT复位由软件置1或清0。0:无复位1:复位WWDGT</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPRST</td><td>CMP复位由软件置1或清0。0:无复位1:复位CMP</td></tr><tr><td>0</td><td>SYSCFGRST</td><td>系统配置复位由软件置1或清0。0:无复位1:复位系统配置</td></tr></table>

## 4.3.7. AHB1 使能寄存器（RCU_AHB1EN）

地址偏移：0x30

复位值：0x0000 0010

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>DMAMUXEN</td><td>保留</td><td>DMAEN</td><td colspan="5">保留</td></tr><tr><td colspan="9">rw</td><td colspan="7">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>CRCEN</td><td colspan="7">保留</td><td>FMCEN</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXEN</td><td>DMAMUX时钟使能由软件置1或清0。0: DMAMUX时钟关闭1: DMAMUX时钟开启</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>DMAEN</td><td>DMA时钟使能由软件置1或清0。0: DMA时钟关闭1: DMA时钟开启</td></tr><tr><td>20:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCEN</td><td>CRC时钟使能由软件置1或清0。0: CRC时钟关闭1: CRC时钟开启</td></tr><tr><td>11:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCEN</td><td>FMC时钟使能由软件置1或清0。0: FMC时钟关闭1: FMC时钟开启</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.8. AHB2 使能寄存器（RCU_AHB2EN）

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td>PFEN</td><td>保留</td><td>PDEN</td><td>PCEN</td><td>PBEN</td><td>PAEN</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PFEN</td><td>GPIOF时钟使能由软件置1或清0。0: GPIOF时钟关闭</td></tr></table>

<table><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PDEN</td><td>GPIOD时钟使能由软件置1或清0。0: GPIOD时钟关闭1: GPIOD时钟开启</td></tr><tr><td>19</td><td>PCEN</td><td>GPIOC时钟使能由软件置1或清0。0: GPIOC时钟关闭1: GPIOC时钟开启</td></tr><tr><td>18</td><td>PBEN</td><td>GPIOB时钟使能由软件置1或清0。0: GPIOB时钟关闭1: GPIOB时钟开启</td></tr><tr><td>17</td><td>PAEN</td><td>GPIOA时钟使能由软件置1或清0。0: GPIOA时钟关闭1: GPIOA时钟开启</td></tr><tr><td>16:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.9. APB 使能寄存器（RCU_APBEN）

地址偏移：0x44

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMUEN</td><td>DBGEN</td><td colspan="4">保留</td><td>I2C1EN</td><td>I2C0EN</td><td>保留</td><td>USART2EN</td><td>TIMER16EN</td><td>TIMER15EN</td><td>TIMER13EN</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>USART1EN</td><td>USART0EN</td><td>SPI1EN</td><td>SPI0EN</td><td>TIMER2EN</td><td>TIMER0EN</td><td>ADCEN</td><td>WWDGTEN</td><td colspan="6">保留</td><td>CMPEN</td><td>SYSCFGEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="6"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMUEN</td><td>PMU时钟使能由软件置1或清0。0:关闭PMU时钟</td></tr></table>

<table><tr><td>27</td><td>DBGEN</td><td>DBG时钟使能由软件置1或清0。0:关闭DBG时钟1:开启DBG时钟</td></tr><tr><td>26:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1EN</td><td>TIMER14定时器时钟使能由软件置1或清0。0:关闭TIMER14定时器时钟1:开启TIMER14定时器时钟</td></tr><tr><td>21</td><td>I2C0EN</td><td>I2C0时钟使能由软件置1或清0。0:关闭I2C0时钟1:开启I2C0时钟</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>USART2EN</td><td>USART2时钟使能由软件置1或清0。0:关闭USART2时钟1:开启USART2时钟</td></tr><tr><td>18</td><td>TIMER16EN</td><td>TIMER16定时器时钟使能由软件置1或清0。0:关闭TIMER16定时器时钟1:开启TIMER16定时器时钟</td></tr><tr><td>17</td><td>TIMER15EN</td><td>TIMER15定时器时钟使能由软件置1或清0。0:关闭TIMER15定时器时钟1:开启TIMER15定时器时钟</td></tr><tr><td>16</td><td>TIMER13EN</td><td>TIMER13定时器时钟使能由软件置1或清0。0:关闭TIMER13定时器时钟1:开启TIMER13定时器时钟</td></tr><tr><td>15</td><td>USART1EN</td><td>USART1时钟使能由软件置1或清0。0:关闭USART1时钟1:开启USART1时钟</td></tr><tr><td>14</td><td>USART0EN</td><td>USART0时钟使能由软件置1或清0。0:关闭USART0时钟</td></tr></table>

<table><tr><td>13</td><td>SPI1EN</td><td>SPI1时钟使能由软件置1或清0。0:关闭SPI1时钟1:开启SPI1时钟</td></tr><tr><td>12</td><td>SPI0EN</td><td>SPI0时钟使能由软件置1或清0。0:关闭SPI0时钟1:开启SPI0时钟</td></tr><tr><td>11</td><td>TIMER2EN</td><td>TIMER2定时器时钟使能由软件置1或清0。0:关闭TIMER2定时器时钟1:开启TIMER2定时器时钟</td></tr><tr><td>10</td><td>TIMER0EN</td><td>TIMER0定时器时钟使能由软件置1或清0。0:关闭TIMER0定时器时钟1:开启TIMER0定时器时钟</td></tr><tr><td>9</td><td>ADCEN</td><td>ADC时钟使能由软件置1或清0。0:关闭ADC时钟1:开启ADC时钟</td></tr><tr><td>8</td><td>WWDGTEN</td><td>WWDGT时钟使能由软件置1或清0。0:关闭WWDGT时钟1:开启WWDGT时钟注意:WWDGTEN使能后,需要系统复位清0。</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPEN</td><td>CMP模块时钟使能由软件置1或清0。0:关闭CMP模块时钟1:开启CMP模块时钟</td></tr><tr><td>0</td><td>SYSCFGEN</td><td>系统配置时钟使能由软件置1或清0。0:关闭系统配置时钟1:开启系统配置时钟</td></tr></table>

## 4.3.10. AHB1 睡眠和深度睡眠使能寄存器（RCU_AHB1SPDPEN）

地址偏移：0x050

复位值：0x00A0 1014


该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>DMAMUXSPDPEN</td><td>保留</td><td>DMASPD PEN</td><td colspan="5">保留</td></tr></table>

<table><tr><td>保留</td><td>CRCSPDPEN</td><td>保留</td><td>FMCSPDPEN</td><td>保留</td><td>SRAMSPDPEN</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>DMAMUXSPDPEN</td><td>在睡眠和深度睡眠模式下 DMAMUX 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 DMAMUX 时钟1: 在睡眠和深度睡眠模式下开启 DMAMUX 时钟</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>DMASPDPEN</td><td>在睡眠和深度睡眠模式下 DMA 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 DMA 时钟1: 在睡眠和深度睡眠模式下开启 DMA 时钟</td></tr><tr><td>20:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>CRCSPDPEN</td><td>在睡眠和深度睡眠模式下 CRC 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 CRC 时钟1: 在睡眠和深度睡眠模式下开启 CRC 时钟</td></tr><tr><td>11:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>FMCSPDPEN</td><td>在睡眠和深度睡眠模式下 FMC 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 FMC 时钟1: 在睡眠和深度睡眠模式下开启 FMC 时钟</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SRAMSPDPEN</td><td>在睡眠和深度睡眠模式下 SRAM 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 SRAM 时钟1: 在睡眠和深度睡眠模式下开启 SRAM 时钟</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.11. AHB2 睡眠和深度睡眠使能寄存器（RCU_AHB2SPDPEN）

地址偏移：0x054

复位值：0x005E 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PFSPDPEN</td><td>保留</td><td>PDSPDPEN</td><td>PCSPDPEN</td><td>PBSPDPEN</td><td>PASPDPEN</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PFSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 F 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 F 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 F 时钟</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PDSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 D 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 D 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 D 时钟</td></tr><tr><td>19</td><td>PCSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 C 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 C 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 C 时钟</td></tr><tr><td>18</td><td>PBSPDPEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 B 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 B 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 B 时钟</td></tr><tr><td>17</td><td>PASPDEN</td><td>在睡眠和深度睡眠模式下 GPIO 端口 A 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 GPIO 端口 A 时钟1: 在睡眠和深度睡眠模式下开启 GPIO 端口 A 时钟</td></tr><tr><td>16:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 4.3.12. APB 睡眠和深度睡眠使能寄存器（RCU_APBSPDPEN）

地址偏移：0x64

复位值：0x106F FF03

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PMUSPD PEN</td><td colspan="5">保留</td><td>I2C1SPD PEN</td><td>I2C0SPD PEN</td><td>保留</td><td>USART2 SPDPEN</td><td>TIMER16 SPDPEN</td><td>TIMER15 SPDPEN</td><td>TIMER13 SPDPEN</td></tr><tr><td colspan="3"></td><td colspan="6">rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>USART1 SPDPEN</td><td>USART0 SPDPEN</td><td>SPI1SPD PEN</td><td>SPI0SPD PEN</td><td>TIMER2S PDPEN</td><td>TIMER0S PDPEN</td><td>ADCSPD PEN</td><td>WWDGT SPDPEN</td><td colspan="6">保留</td><td>CMPSPD PEN</td><td>SYSCFG SPDPEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="6"></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PMUSPDPEN</td><td>在睡眠和深度睡眠模式下 PMU 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 PMU 时钟1: 在睡眠和深度睡眠模式下开启 PMU 时钟</td></tr><tr><td>27:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>I2C1SPDPEN</td><td>在睡眠和深度睡眠模式下 I2C1 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 I2C1 时钟1: 在睡眠和深度睡眠模式下开启 I2C1 时钟</td></tr><tr><td>21</td><td>I2C0SPDPEN</td><td>在睡眠和深度睡眠模式下 I2C0 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 I2C0 时钟1: 在睡眠和深度睡眠模式下开启 I2C0 时钟</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>USART2SPDPEN</td><td>在睡眠和深度睡眠模式下 USART2 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 USART2 时钟1: 在睡眠和深度睡眠模式下开启 USART2 时钟</td></tr><tr><td>18</td><td>TIMER16SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER16 时钟使能由软件置位或复位0: 在睡眠和深度睡眠模式下关闭 TIMER16 时钟1: 在睡眠和深度睡眠模式下开启 TIMER16 时钟</td></tr><tr><td>17</td><td>TIMER15SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER15 时钟使能由软件置位或复位</td></tr></table>

<table><tr><td></td><td></td><td>0:在睡眠和深度睡眠模式下关闭 TIMER15 时钟1:在睡眠和深度睡眠模式下开启 TIMER15 时钟</td></tr><tr><td>16</td><td>TIMER13SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER13 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TIMER13 时钟1:在睡眠和深度睡眠模式下开启 TIMER13 时钟</td></tr><tr><td>15</td><td>USART1SPDPEN</td><td>在睡眠和深度睡眠模式下 USART1 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 USART1 时钟1:在睡眠和深度睡眠模式下开启 USART1 时钟</td></tr><tr><td>14</td><td>USART0SPDPEN</td><td>在睡眠和深度睡眠模式下 USART0 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 USART0 时钟1:在睡眠和深度睡眠模式下开启 USART0 时钟</td></tr><tr><td>13</td><td>SPI1SPDPEN</td><td>在睡眠和深度睡眠模式下 SPI1 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 SPI1 时钟1:在睡眠和深度睡眠模式下开启 SPI1 时钟</td></tr><tr><td>12</td><td>SPI0SPDPEN</td><td>在睡眠和深度睡眠模式下 SPI0 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 SPI0 时钟1:在睡眠和深度睡眠模式下开启 SPI0 时钟</td></tr><tr><td>11</td><td>TIMER2SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER2 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TIMER2 时钟1:在睡眠和深度睡眠模式下开启 TIMER2 时钟</td></tr><tr><td>10</td><td>TIMER0SPDPEN</td><td>在睡眠和深度睡眠模式下 TIMER0 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 TIMER0 时钟1:在睡眠和深度睡眠模式下开启 TIMER0 时钟</td></tr><tr><td>9</td><td>ADCSPDPEN</td><td>在睡眠和深度睡眠模式下 ADC 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 ADC 时钟1:在睡眠和深度睡眠模式下开启 ADC 时钟</td></tr><tr><td>8</td><td>WWDGTSPDPEN</td><td>在睡眠和深度睡眠模式下 WWDGT 时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭 WWDGT 时钟1:在睡眠和深度睡眠模式下开启 WWDGT 时钟</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CMPSPDPEN</td><td>在睡眠和深度睡眠模式下CMP时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭CMP时钟1:在睡眠和深度睡眠模式下开启CMP时钟</td></tr><tr><td>0</td><td>SYSCFGSPDPEN</td><td>在睡眠和深度睡眠模式下系统配置时钟使能由软件置位或复位0:在睡眠和深度睡眠模式下关闭系统配置时钟1:在睡眠和深度睡眠模式下开启系统配置时钟</td></tr></table>

## 4.3.13. 控制寄存器 1（RCU_CTL1）

地址偏移：0x70

复位值：0x0000 0008，由备份寄存器复位电路复位

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

注意：控制寄存器 1（RCU_CTL1）的 LXTALEN, LXTALBPS, RTCSRC 和 RTCEN 位仅在备份寄存器（V<sub>CORE_STB</sub>）复位后才清 0。只有在电源控制寄存器（PMU_CTL0）中的 BKPWEN 位置 1 后才能对这些位进行改动。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>LSCKOU TSEL</td><td>LSCKOU TEN</td><td colspan="7">保留</td><td>BKPRST</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTCEN</td><td colspan="5">保留</td><td colspan="2">RTCSRC[1:0]</td><td>LXTALSTBRST</td><td>LCKMD</td><td>LCKMEN</td><td>保留</td><td>LXTALDRI</td><td>LXTALBPS</td><td>LXTALSTB</td><td>LXTALEN</td></tr><tr><td colspan="6">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>r</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>LSCKOUTSEL</td><td>低速时钟输出选择0: IRC32K1: LXTAL</td></tr><tr><td>24</td><td>LSCKOUTEN</td><td>低速时钟输出使能0: 低速时钟输出失能1: 低速时钟输出使能</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPRST</td><td>备份寄存器复位由软件置位或复位0: 无作用1: 复位备份寄存器</td></tr><tr><td>15</td><td>RTCEN</td><td>RTC时钟使能由软件置位或复位0:关闭RTC时钟1:开启RTC时钟</td></tr><tr><td>14:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>RTCSRC[1:0]</td><td>RTC时钟入口选择软件置位或清除来控制RTC时钟源。00:没有时钟01:选择LXTAL时钟作为RTC时钟源10:选择IRC32K时钟作为RTC时钟源11:选择HXTAL时钟32分频作为RTC时钟源</td></tr><tr><td>7</td><td>LXTALSTBRST</td><td>低速晶体振荡器稳定标志位复位0:低速晶体振荡器稳定标志位不复位1:低速晶体振荡器稳定标志位复位</td></tr><tr><td>6</td><td>LCKMD</td><td>LXTAL时钟故障检测当外部32kHz振荡器(LXTAL)上的时钟安全系统检测到故障,硬件置位。当LCKMEN或LXTALEN关闭时,该位清零。0:LXTAL(32kHz振荡器)上未检测到故障1:在LXTAL(32kHz振荡器)上检测到故障</td></tr><tr><td>5</td><td>LCKMEN</td><td>LXTAL时钟监视器使能0:禁止LXTAL时1:使能LXTAL时钟监视器通过软件设置,启用LXTAL(32kHz振荡器)上的时钟安全系统。LXTALEN必须在LXTAL已启用(LXTALEN位已启用)和就绪(LXTALSTB标志由硬件设置)。</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>LXTALDRI</td><td>LXTAL驱动能力软件置位或清除。当复位备份寄存器时,会重装载缺省值。0:低驱动能力1:高驱动能力(复位后的缺省值)注意:LXTALDRI在旁路模式下无效</td></tr><tr><td>2</td><td>LXTALBPS</td><td>LXTAL旁路模式使能软件置1和清0。0:禁止LXTAL旁路模式1:使能LXTAL旁路模式</td></tr><tr><td>1</td><td>LXTALSTB</td><td>外部低速振荡器稳定状态位硬件置1来指示LXTAL输出时钟是否稳定待用。0:LXTAL未稳定1:LXTAL已稳定</td></tr><tr><td>0</td><td>LXTALEN</td><td>LXTAL使能</td></tr></table>

软件置1和清0。

0：关闭LXTAL

1：开启LXTAL

## 4.3.14. 复位源/时钟寄存器（RCU_RSTSCK）

地址偏移：0x74

复位值：0xXX00 0000，除复位标志外由系统复位清除，复位标志只能由电源复位清除。

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPRSTF</td><td>WWDGTRSTF</td><td>FWDGTRSTF</td><td>SWRSTF</td><td>PORRSTF</td><td>EPRSTF</td><td>保留</td><td>RSTFC</td><td>OBLRRSTF</td><td colspan="7">保留</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>rw</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>IRC32KSTB</td><td>IRC32KEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPRSTF</td><td>低功耗复位标志位当产生深度睡眠或待机重置时,由硬件设置。深度睡眠/待机复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无低功耗管理复位发生1:发生低功耗管理复位</td></tr><tr><td>30</td><td>WWDGTRSTF</td><td>窗口看门狗定时器复位标志位窗口看门狗定时器复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无窗口看门狗定时器复位发生1:发生窗口看门狗定时器复位</td></tr><tr><td>29</td><td>FWDGTRSTF</td><td>独立看门狗定时器复位标志位独立看门狗复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无独立看门狗定时器复位发生1:发生独立看门狗定时器复位</td></tr><tr><td>28</td><td>SWRSTF</td><td>软件复位标志位软件复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无软件复位发生1:发生软件复位</td></tr><tr><td>27</td><td>PORRSTF</td><td>电源复位标志位</td></tr></table>

<table><tr><td></td><td></td><td>电源复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无电源复位发生1:发生电源复位</td></tr><tr><td>26</td><td>EPRSTF</td><td>外部引脚复位标志位当有外部引脚复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无外部引脚复位发生1:发生外部引脚复位</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>RSTFC</td><td>清除复位标志位由软件置1来清除所有复位标志位。0:无作用1:清除复位标志位</td></tr><tr><td>23</td><td>OBLRSTF</td><td>选项字节重载复位标志位当有选项字节重载复位发生时由硬件置1。由软件通过写1到RSTFC位来清除该位。0:无选项字节重载复位发生1:发生选项字节重载复位</td></tr><tr><td>22:2</td><td>保留</td><td>必须保持复位值。.</td></tr><tr><td>1</td><td>IRC32KSTB</td><td>IRC32K时钟稳定状态位该位由硬件置1指示IRC32K输出时钟是否稳定待用。0:IRC32K时钟未稳定1:IRC32K时钟已稳定</td></tr><tr><td>0</td><td>IRC32KEN</td><td>IRC32K时钟使能软件置1和清0。0:关闭IRC32K时钟1:开启IRC32K时钟</td></tr></table>

## 4.3.15. 配置寄存器 1（RCU_CFG1）

地址偏移：0x8C

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>I2SSEL[1:0]</td><td colspan="2">保留</td><td colspan="4">ADCPSC[3:0]</td><td>ADCSEL</td><td colspan="2">保留</td><td colspan="2">I2C1SEL[1:0]</td><td colspan="2">I2C0SEL[1:0]</td><td colspan="2">USART0SEL[1:0]</td></tr><tr><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>I2SSEL[1:0]</td><td>I2S时钟源选择由软件置1或清0。00:I2S时钟选择CK_SYS01:保留10:I2S钟选择CK_HIRCDIV_PER11:I2S钟选择I2S_CKIN</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:9</td><td>ADCPSC[3:0]</td><td>ADC时钟预分频选择。这些位是由软件编写的并定义ADC时钟预分频。由软件设置和清除。0000:输出ADC时钟不分频0001:输出ADC时钟2分频0010:输出ADC时钟4分频0011:输出ADC时钟6分频0100:输出ADC时钟8分频0101:输出ADC时钟10分频0110:输出ADC时钟12分频0111:输出ADC时钟16分频1000:输出ADC时钟32分频1001:输出ADC时钟64分频1010:输出ADC时钟128分频1011:输出ADC时钟256分频其他:保留</td></tr><tr><td>8</td><td>ADCSEL</td><td>ADC时钟源选择由软件置1或清0。0:选择CK_SYS时钟作为时钟源1:选择CK_HIRCDIV_PER作为时钟源</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>I2C1SEL[1:0]</td><td>I2C1时钟源选择由软件置1或清0。00:选择CK_APB时钟作为时钟源01:选择CK_SYS作为时钟源10/11:选择CK_HIRCDIV_PER作为时钟源</td></tr><tr><td>3:2</td><td>I2C0SEL[1:0]</td><td>I2C0时钟源选择由软件置1或清0。00:选择CK_APB时钟作为时钟源01:选择CK_SYS作为时钟源</td></tr></table>

10/11：选择CK_HIRCDIV_PER作为时钟源

1:0 USART0SEL[1:0] USART0时钟源选择

由软件置1或清0。

00：选择CK_APB时钟作为时钟源

01：选择CK_SYS作为时钟源

11：选择CK_LXTAL作为时钟源

10：选择CK_HIRCDIV_PER作为时钟源
