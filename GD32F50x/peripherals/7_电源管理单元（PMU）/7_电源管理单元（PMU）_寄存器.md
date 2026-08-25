## 7.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 7.4.1. 控制寄存器 0（PMU_CTL0）

地址偏移：0x00

复位值：0x1600 7000（从待机模式唤醒后复位）

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>UNLOCK</td><td colspan="2">保留</td><td colspan="2">VUVDVC[1:0]</td><td colspan="2">VOVDVC[1:0]</td><td>VUVDEN</td><td>VOVDEN</td><td colspan="2">VAVDVC[1:0]</td><td>VAVDEN</td><td colspan="2">LDEN[1:0]</td><td colspan="2">保留</td></tr><tr><td>rw</td><td colspan="2"></td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">LDOVS[2:0]</td><td>LDNP</td><td>LDLP</td><td>PDRVS</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>STBMOD</td><td>LDOLP</td></tr><tr><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>UNLOCK</td><td>寄存器 lock0:其他寄存器和位都不可写1:其他寄存器和位都可写</td></tr><tr><td>30:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:27</td><td>VUVDVC[1:0]</td><td><eq>V_{CORE}</eq>低压检测器电压等级配置位这些位由软件置位和清除。00:配置<eq>V_{CORE}</eq>低压检测器电压等级为1.05V01:配置<eq>V_{CORE}</eq>低压检测器电压等级为0.95V1x:配置<eq>V_{CORE}</eq>低压检测器电压等级为0.85V</td></tr><tr><td>26:25</td><td>VOVDVC[1:0]</td><td><eq>V_{CORE}</eq>过压检测器电压等级配置位这些位由软件置位和清除。00:配置<eq>V_{CORE}</eq>过压检测器电压等级为1.25V01:配置<eq>V_{CORE}</eq>过压检测器电压等级为1.30V10:配置<eq>V_{CORE}</eq>过压检测器电压等级为1.35V11:配置<eq>V_{CORE}</eq>过压检测器电压等级为1.40V</td></tr><tr><td>24</td><td>VUVDEN</td><td><eq>V_{CORE}</eq>低压检测器使能位该位由软件置位和清除。0:失能<eq>V_{CORE}</eq>低压检测器1:使能 <eq>V_{CORE}</eq>低压检测器</td></tr><tr><td>23</td><td>VOVDEN</td><td><eq>V_{CORE}</eq>过压检测器使能位该位由软件置位和清除。0: 失能VCORE过压检测器1: 使能VCORE过压检测器</td></tr><tr><td>22:21</td><td>VAVDVC[1:0]</td><td>VDDA模拟电压检测器电压等级配置位这些位由软件置位和清除。00: 配置VDDA模拟电压检测器电压等级为2.3V01: 配置VDDA模拟电压检测器电压等级为2.5V10: 配置VDDA模拟电压检测器电压等级为2.7V11: 配置VDDA模拟电压检测器电压等级为2.9V</td></tr><tr><td>20</td><td>VAVDEN</td><td>VDDA模拟电压检测器使能位该位由软件置位和清除。0: 失能VDDA模拟电压检测器1: 使能VDDA模拟电压检测器</td></tr><tr><td>19:18</td><td>LDEN[1:0]</td><td>深度睡眠模式下,低驱动模式使能00: 在深度睡眠模式下,禁用低驱动模式01: 保留10: 保留11: 在深度睡眠模式下,使能低驱动模式</td></tr><tr><td>17:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>LDOVS[2:0]</td><td>LDO输出电压选择在PLL关闭时,这些位由软件配置,在主PLL使能后,LDOVS设置的值生效。如果主PLL关闭,LDO输出默认值。000: 保留001: 0.9v(不建议客户使用)010: 0.95v(不建议客户使用)011: 1.0v(不建议客户使用)100: 1.05v(不建议客户使用)101: 1.1v110: 1.15v111: 1.2v注意:该位域不支持0b000配置,配置为0b000将会导致不可预知的错误。</td></tr><tr><td>11</td><td>LDNP</td><td>使用正常功耗LDO时,工作在低驱动模式0: 使用正常功耗LDO时,工作在正常驱动模式1: 使用正常功耗LDO且LDEN为11时,低驱动模式被使能</td></tr><tr><td>10</td><td>LDLP</td><td>使用低功耗LDO时,工作在低驱动模式0: 使用低功耗LDO时,工作在正常驱动模式1: 使用低功耗LDO且LDEN为11时,低驱动模式被使能</td></tr><tr><td>9</td><td>PDRVS</td><td>PDR 阈值电压选择0: 2.35V1: 1.8V</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0: 禁止对备份域寄存器的写访问1: 允许对备份域寄存器的写访问复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000: 2.1V001: 2.3V010: 2.4V011: 2.6V100: 2.7V101: 2.8V110: 3.0V111: 3.1V</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0: 关闭低电压检测器1: 开启低电压检测器注意:当SYSCFG_LKCTL寄存器里的LVD_LOCK位被置1时,LVDEN和LVDT[2:0]仅可读。</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0: 无影响1: 复位待机标志读该位,始终返回0</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0: 无影响1: 复位唤醒标志读该位,始终返回0</td></tr><tr><td>1</td><td>STBMOD</td><td>待机模式0: 当Cortex®-M33进入SLEEPDEEP模式时,系统进入深度睡眠模式1: 当Cortex®-M33进入SLEEPDEEP模式时,系统进入待机模式</td></tr><tr><td>0</td><td>LDOLP</td><td>LDO低功耗模式0: 当系统进入深度睡眠模式时,LDO仍正常工作1: 当系统进入深度睡眠模式时,LDO进入低功耗模式</td></tr></table>

## 7.4.2. 电源控制和状态寄存器（PMU_CS）

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="2">LDRF[1:0]</td><td colspan="2">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LDOVSRF</td><td colspan="5">保留</td><td>WUPEN</td><td>VUVDF1</td><td>VOVDF</td><td>保留</td><td>VUVDF0</td><td>VAVDF</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>LDRF[1:0]</td><td>低驱动模式就绪标志在深度睡眠模式下,且LDO处于低驱动模式,这些位由硬件设置。软件对这些位写11可以清0。00:深度睡眠模式下,普通驱动模式01:保留10:保留11:深度睡眠模式下,低驱动模式</td></tr><tr><td>17:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LDOVSRF</td><td>LDO电压选择就绪标志0:LDO电压选择未就绪1:LDO电压选择就绪</td></tr><tr><td>13:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>WUPEN</td><td>WKUP引脚唤醒使能0:关闭WKUP引脚唤醒功能1:开启WKUP引脚唤醒功能如果WUPEN在进入待机模式之前置1,WKUP引脚的上升沿会将系统从待机模式唤醒。由于WKUP引脚为高电平有效,WKUP引脚内部被配置为输入下拉模式。当置位该控制位后,当输入为高的时候,将会触发一个唤醒事件。</td></tr><tr><td>7</td><td>VUVDF1</td><td>数字滤波后VCORE低电压检测器标志位由硬件设置和清除,仅当VUVDEN使能时有效0:VCORE大于VUVD阈值。1:VCORE小于等于VUVD阈值。</td></tr><tr><td>6</td><td>VOVDF</td><td>数字滤波后VCORE过电压检测器标志位由硬件设置和清除,仅当VOVDEN使能时有效0:VCORE小于VOVDVC[1:0]阈值。1:VCORE大于等于VOVDVC[1:0]阈值。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>VUVDF0</td><td>数字滤波后VCORE低电压检测器标志位由硬件设置和清除,仅当VUVDEN使能时有效0:VCORE大于VUVD阈值。1:VCORE小于等于VUVD阈值。</td></tr><tr><td>3</td><td>VAVDF</td><td>VDDA模拟电压检测器输出标志位由硬件设置和清除,仅当VAVDEN使能时有效0:VDDA大于等于由VAVDVC位配置的VAVD阈值。1:VDDA小于由VAVDVC位配置的VAVD阈值。</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(VDD高于设定的LVD阈值)1:低电压事件出现(VDD等于或低于LVD阈值)注意:LVD功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式1:设备曾进入过待机模式该位只能由POR/PDR或通过设置PMU_CTL0寄存器的STBRST位来清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件1:收到来自WKUP引脚或RTC闹钟事件。该位只能由POR/PDR或通过设置PMU_CTL0寄存器的WURST位来清零。</td></tr></table>

## 7.4.3. 控制寄存器 1（PMU_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>VUVDO_DNF[7:0]</td><td>VOVDO_DNF[7:0]</td></tr><tr><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>VUVDO_DNF[7:0]</td><td>VUVD模拟输出数字噪声滤波器这些位用于配置VUVD模拟输出上的数字噪声滤波器,数字滤波器将滤波峰值的长度高达<eq>VUVDO_DNF[7:0] \times 1024 \times T_{PCLK1}</eq>0:关闭数字滤波器1:开启数字滤波器,滤波峰值长度高达<eq>1024 \times T_{PCLK1}</eq>...255:开启数字滤波器,滤波峰值长度高达<eq>255 \times 1024 \times T_{PCLK1}</eq></td></tr><tr><td>7:0</td><td>VOVDO_DNF[7:0]</td><td>VOVD模拟输出数字噪声滤波器这些位用于配置VOVD模拟输出上的数字噪声滤波器,数字滤波器将滤波峰值的长度高达<eq>VOVDO_DNF[7:0] \times 1024 \times T_{PCLK1}</eq>0:关闭数字滤波器1:开启数字滤波器,滤波峰值长度高达<eq>1024 \times T_{PCLK1}</eq>...255:开启数字滤波器,滤波峰值长度高达<eq>255 \times 1024 \times T_{PCLK1}</eq></td></tr></table>
