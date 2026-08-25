# 5.4. PMU 寄存器

PMU 基地址：0x5800 5800

# 5.4.1. 控制寄存器 0（PMU_CTL0）

地址偏移：0x00

复位值：0x0000 8000（从待机模式唤醒后复位）

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td>VOVDEN</td><td colspan="2">VAVDVC[1:0]</td><td>VAVDEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">SLDOVS[1:0]</td><td colspan="5">保留</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>STBMOD</td><td>保留</td></tr><tr><td colspan="7">rs</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>VOVDEN</td><td><eq>V_{CORE}</eq>外设电压检测器使能位该位由软件置位和清除。0: 失能<eq>V_{CORE}</eq>外设电压检测器1: 使能<eq>V_{CORE}</eq>外设电压检测器</td></tr><tr><td>18:17</td><td>VAVDVC[1:0]</td><td><eq>V_{DDA}</eq>模拟电压检测器电压等级配置位这些位由软件置位和清除。00: 配置<eq>V_{DDA}</eq>模拟电压检测器电压等级为1.7V01: 配置<eq>V_{DDA}</eq>模拟电压检测器电压等级为2.1V10: 配置<eq>V_{DDA}</eq>模拟电压检测器电压等级为2.5V11: 配置<eq>V_{DDA}</eq>模拟电压检测器电压等级为2.8V</td></tr><tr><td>16</td><td>VAVDEN</td><td><eq>V_{DDA}</eq>模拟电压检测器使能位该位由软件置位和清除。0: 失能<eq>V_{DDA}</eq>模拟电压检测器1: 使能 <eq>V_{DDA}</eq> 模拟电压检测器</td></tr><tr><td>15:14</td><td>SLDOVS[1:0]</td><td>Deep-sleep模式电压选择这些位控制Deep-sleep模式时<eq>V_{CORE}</eq>电压值,以便在性能和功耗之间实现最佳的平衡。00: SLDOVS设置电压为0.6V01: SLDOVS设置电压为0.7V10: SLDOVS设置电压为0.8V(默认)11: SLDOVS设置电压为0.9V</td></tr><tr><td>13:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0:禁止对备份域寄存器的写访问。1:允许对备份域寄存器的写访问。复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000:2.1V001:2.3V010:2.4V011:2.6V100:2.7V101:2.9V110:3.0V111:PB7输入模拟电压(与0.8V进行比较)注意:测量值请参考数据手册。</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0:关闭低电压检测器。1:开启低电压检测器注意:当SYSCFG_LKCTL寄存器里的LVD_LOCK位被置1时,LVDEN和LVDT[2:0]仅可读。</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0:无影响1:复位待机标志读该位,始终返回0。</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0:无影响1:复位唤醒标志读该位,始终返回0。</td></tr><tr><td>1</td><td>STBMOD</td><td>待机模式选择0:当Cortex®-M7进入SLEEPDEEP模式时,MCU进入Deep-sleep模式1:当Cortex®-M7进入SLEEPDEEP模式时,MCU进入待机模式</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 5.4.2. 电源控制和状态寄存器（PMU_CS）

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>保留</td><td></td><td></td><td></td><td></td><td></td><td>VOVDF</td><td>保留</td><td></td><td></td><td>VAVDF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>WUPEN5</td><td>保留</td><td>WUPEN3</td><td>保留</td><td>WUPEN1</td><td>WUPENO</td><td colspan="5">保留</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td></td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>VOVDF</td><td><eq>V_{CORE}</eq>外设电压监控器标志位该位由硬件置位和清除。仅在VOVDEN置位的时候有效0:<eq>V_{CORE}</eq>低于VOVD阈值(1.15V)1:<eq>V_{CORE}</eq>等于或高于VOVD阈值(1.15V)</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>VAVDF</td><td><eq>V_{DDA}</eq>模拟电压检测器标志位该位由硬件置位和清除。仅在VAVDEN置位的时候有效0:VDDA等于或者高于VAVD阈值,阈值由VAVDVC[1:0]配置1:VDDA小于VAVD阈值,阈值由VAVDVC[1:0]配置</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>WUPEN5</td><td>WKUP引脚5(PC1)唤醒使能0:关闭WKUP引脚5唤醒功能。1:开启WKUP引脚5唤醒功能。如果WUPEN5在进入省电模式之前置1,WKUP引脚5的上升沿会将系统从省电模式唤醒。由于WKUP引脚5为高电平有效,WKUP引脚5内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PC13)唤醒使能0:禁能WKUP引脚3唤醒功能。1:使能WKUP引脚3唤醒功能。如果WUPEN3在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PA2)唤醒使能0:关闭WKUP引脚1唤醒功能。1:开启WKUP引脚1唤醒功能。如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模</td></tr></table>

式。当在输入已经为高的时候置位该控制位，将会触发一个唤醒事件。

8 WUPEN0 

WKUP 引脚 0（PA0）唤醒使能

0：关闭 WKUP 引脚0 唤醒功能。

1：开启 WKUP 引脚0 唤醒功能。

如果 WUPEN0 在进入省电模式之前置 1，WKUP 引脚 0 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚0 为高电平有效，WKUP 引脚 0 内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位，将会触发一个唤醒事件。

7:3 保留

必须保持复位值。

2 LVDF 

低电压状态标志

0：低电压事件没出现（VDD高于设定的 LVD 阈值）。

1：低电压事件出现 $( \mathsf { V } _ { \mathsf { D } \mathsf { D } }$ 等于或低于 LVD 阈值）。

注意：LVD 功能在待机模式被禁用。

1 STBF 

待机标志

0：设备没进入过待机模式。

1：设备曾进入过待机模式。

该位只能由 POR / PDR 或通过置位 PMU_CTL0 寄存器的 STBRST 位来清零。

0 WUF 

唤醒标志

0：没有收到唤醒事件。

1：唤醒事件由 WKUP 引脚或 RTC 事件包括 RTC 闹钟事件，时间戳事件，侵入事件和自动唤醒事件触发。

该位只能由 POR / PDR 或通过设置 PMU_CTL0 寄存器的 WURST 位来清零。

# 5.4.3. 控制寄存器 1（PMU_CTL1）

地址偏移：0x08

复位值：0x0000 0000（从待机模式唤醒后复位）

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>TEMPHF</td><td>TEMPLF</td><td>VBATHF</td><td>VBATLF</td><td colspan="3">保留</td><td>BKPVSRF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td></td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>VBTMEN</td><td colspan="3">保留</td><td>BKPVSE N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td></tr></table>

位/位域 名称

描述

31:24 保留

必须保持复位值。

23 TEMPHF 

温度监测高阈值标志位

0：温度低于温度监测的高阈值

1：温度等于或高于温度监测的高阈值

<table><tr><td>22</td><td>TEMPLF</td><td>温度监测低阈值标志位0:温度低于温度监测的低阈值1:温度等于或高于温度监测的低阈值</td></tr><tr><td>21</td><td>VBATHF</td><td><eq>V_{BAT}</eq>监测高阈值标志位0:<eq>V_{BAT}</eq>电压低于<eq>V_{BAT}</eq>监测的高阈值1:<eq>V_{BAT}</eq>电压等于或高于<eq>V_{BAT}</eq>监测的高阈值</td></tr><tr><td>20</td><td>VBATLF</td><td><eq>V_{BAT}</eq>监测低阈值标志位0:<eq>V_{BAT}</eq>电压低于<eq>V_{BAT}</eq>监测的低阈值1:<eq>V_{BAT}</eq>电压等于或高于<eq>V_{BAT}</eq>监测的低阈值</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPVSRF</td><td>备份域电压稳压器就绪标志位该位由硬件置位用于指示备份域电压稳压器是否就绪。0:备份域电压稳压器未就绪1:备份域电压稳压器已就绪</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>VBTMEN</td><td><eq>V_{BAT}</eq>和温度监测器使能位当该位置位将使能<eq>V_{BAT}</eq>供电电压监测和温度监测。0:失能<eq>V_{BAT}</eq>和温度监测器1:使能<eq>V_{BAT}</eq>和温度监测器注意:<eq>V_{BAT}</eq>和温度监测器只有在BKPVSRF置位时才有效</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BKPVSEN</td><td>备份域电压稳压器使能位该位由软件置位和清除。置位后将使能备份域稳压器(能够在待机模式和电池供电模式时保持RAM内容)。没有置位是备份域电压稳压器将失能,RAM能够在普通运行模式和Deep-sleep模式时保持内容,但无法在待机模式和<eq>V_{BAT}</eq>模式时保持内容。如果使能,需要在BKPVSRF置位后才能写入数据到SRAM,这样才能在待机模式和电池供电模式下保持SRAM内容。0:失能备份域电压稳压器1:使能备份域电压稳压器</td></tr></table>

# 5.4.4. 控制寄存器 2（PMU_CTL2）

地址偏移：0x10

复位值：0x0000 0046（从待机模式唤醒后复位）

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>USB33RF</td><td>USBSEN</td><td>VUSB33DEN</td><td colspan="7">保留</td><td>DVSRF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>r</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>VCRSEL</td><td>VCEN</td><td colspan="5">保留</td><td>DVSEN</td><td>LDOEN</td><td>BYPASS</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>USB33RF</td><td>USB供电电压就绪标志位0: USB33供电电压未就绪1: USB33 供电电压已就绪</td></tr><tr><td>25</td><td>USBSEN</td><td>USB电压稳压器使能位该位由软件件置位和清除。0: 失能USB电压稳压器1: 使能USB电压稳压器</td></tr><tr><td>24</td><td>VUSB33DEN</td><td><eq>V_{DD33USB}</eq>电压监控器使能位该位由软件件置位和清除。0: 失能<eq>V_{DD33USB}</eq>电压监控器1: 使能<eq>V_{DD33USB}</eq>电压监控器</td></tr><tr><td>23:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>DVSRF</td><td>降压稳压器就绪标志位该位由硬件置位用于指示供电来源降压稳压器的外部供电是否就绪。0: 外部供电未就绪1: 外部供电已就绪</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>VCRSEL</td><td><eq>V_{BAT}</eq>电池充电电阻的选择0: 5k欧姆电阻用于<eq>V_{BAT}</eq>电池充电。1: 1.5k欧姆电阻用于<eq>V_{BAT}</eq>电池充电。</td></tr><tr><td>8</td><td>VCEN</td><td><eq>V_{BAT}</eq>电池充电使能0: 禁能<eq>V_{BAT}</eq>电池充电。1: 使能<eq>V_{BAT}</eq>电池充电。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>DVSEN</td><td>降压稳压器使能位该位由软件置位和清除。0: 失能降压稳压器1: 使能降压稳压器</td></tr><tr><td>1</td><td>LDOEN</td><td>LDO使能位该位由软件置位和清除。0: LDO失能</td></tr></table>

1：LDO使能

0 BYPASS 电源管理单元旁路控制位

该位由软件置位和清除。

0：电源管理单元正常工作

1：电源管理单元旁路，电压检测依然有效

# 5.4.5. 控制寄存器 3（PMU_CTL3）

地址偏移：0x14

复位值：0x0000 2000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>VOVRF</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">LDOVS[2:0]</td><td colspan="12">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>VOVRF</td><td><eq>V_{CORE}</eq>电源电压就绪标志位该位由硬件置位用于指示 <eq>V_{CORE}</eq> 供电电压是否就绪。0:<eq>V_{CORE}</eq>供电电压未就绪1:<eq>V_{CORE}</eq> 供电电压已就绪</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>LDOVS[2:0]</td><td>选择 LDO 输出这些位控制 <eq>V_{CORE}</eq> 电压水平,不同的电压等级和系统时钟频率会使得 MCU 具有不同的性能,当准备降低 MCU 性能时应当先降低系统时钟频率,再改变 LDO 输出电压值,与之相反在准备提升 MCU 性能时应当先改变 LDO 输出电压值,再提升系统时钟频率。000:LDO 输出 0.8V 电压001:LDO 输出 0.85V 电压010:LDO 输出 0.9V 电压(默认)011:LDO 输出 0.95V 电压100:LDO 输出 0.975V 电压101:LDO输出1V电压其它:保留。</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 5.4.6. 参数寄存器（PMU_PAR）

地址偏移：0x18

复位值：0x000A0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">TSW_IRCCNT[4:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">PMU_CNT[11:0]</td></tr></table>


rc_w0 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>TSW_IRCCNT[4:0]</td><td>当进入 Deep-sleep,切换到 LPIRC4M / IRC64M(由 DSPWUSSEL 确认)时钟。等待时钟计数后设置深度睡眠状态。默认值为 10 个时钟。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>PMU_CNT[11:0]</td><td>退出深度睡眠模式时等待时间配置位在退出深度睡眠模式,开启系统时钟之前,推荐等待 5us~50us。</td></tr></table>
