## 3.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 3.4.1. 控制寄存器（PMU_CTL）

地址偏移：0x00

复位值：0x0000 C000（从待机模式唤醒后复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="2">LDEN[1:0]</td><td>HDS</td><td>HDEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">LDOVS[1:0]</td><td colspan="2">保留</td><td>LDNP</td><td>LDLP</td><td>保留</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>STBMOD</td><td>LDOLP</td></tr><tr><td colspan="4">rs</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>LDEN[1:0]</td><td>深度睡眠模式下,低驱动模式使能00:在深度睡眠模式下,禁用低驱动模式01:保留10:保留11:在深度睡眠模式下,使能低驱动模式</td></tr><tr><td>17</td><td>HDS</td><td>高驱动模式切换器选择IRC16M或HXTAL作为系统时钟,当HDRF被置位时,由软件将该位置1。该位被置位后,系统进入高驱动模式。可由软件清0,也可在退出深度睡眠模式或HDEN被清0时由硬件清0。0:没有高驱动模式切换器1:有高驱动模式切换器</td></tr><tr><td>16</td><td>HDEN</td><td>高驱动模式使能当系统时钟为IRC16M或HXTAL时,该位由软件置位。当系统退出深度睡眠模式时,该位由软件或硬件清零。0:禁用高驱动模式1:使能高驱动模式</td></tr><tr><td>15:14</td><td>LDOVS[1:0]</td><td>选择LDO输出在PLL关闭时,这些位由软件配置,在主PLL使能后,LDOVS设置的值生效。如果主PLL关闭,LDO输出低电压模式被选中。00:保留(LDO输出低电压模式)01:LDO输出低电压模式10:LDO输出中电压模式11: LDO输出高电压模式</td></tr><tr><td>13:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>LDNP</td><td>使用正常功耗LDO时,工作在低驱动模式0: 使用正常功耗LDO时,工作在正常驱动模式1: 使用正常功耗LDO且LDEN为11时,低驱动模式被使能</td></tr><tr><td>10</td><td>LDLP</td><td>使用低功耗LDO时,工作在低驱动模式0: 使用低功耗LDO时,工作在正常驱动模式1: 使用低功耗LDO且LDEN为11时,低驱动模式被使能</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0: 禁止对备份域寄存器的写访问1: 允许对备份域寄存器的写访问复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000: 2.1V001: 2.3V010: 2.4V011: 2.6V100: 2.7V101: 2.9V110: 3.0V111: 3.1V</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0: 关闭低电压检测器1: 开启低电压检测器</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0: 无影响1: 复位待机标志读该位,始终返回0</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0: 无影响1: 复位唤醒标志读该位,始终返回0</td></tr><tr><td>1</td><td>STBMOD</td><td>待机模式0: 当Cortex®-M4进入SLEEPDEEP模式时,系统进入深度睡眠模式1: 当Cortex®-M4进入SLEEPDEEP模式时,系统进入待机模式</td></tr><tr><td>0</td><td>LDOLP</td><td>LDO低功耗模式</td></tr></table>

0: 当系统进入深度睡眠模式时，LDO 仍正常工作

1: 当系统进入深度睡眠模式时，LDO 进入低功耗模式

## 3.4.2. 电源控制和状态寄存器（PMU_CS）

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="2">LDRF[1:0]</td><td>HDSRF</td><td>HDRF</td></tr><tr><td colspan="14">rc_w1</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LDOVSRF</td><td colspan="4">保留</td><td>BLDOON</td><td>WUPEN</td><td colspan="4">保留</td><td>BLDORF</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td></td><td>r</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>LDRF[1:0]</td><td>低驱动模式就绪标志在深度睡眠模式下,且LDO处于低驱动模式,这些位由硬件设置。软件对这些位写11可以清0。00:深度睡眠模式下,普通驱动模式01:保留10:保留11:深度睡眠模式下,低驱动模式</td></tr><tr><td>17</td><td>HDSRF</td><td>高驱动切换器就绪标志0:高驱动切换器未就绪1:高驱动切换器就绪</td></tr><tr><td>16</td><td>HDRF</td><td>高驱动准备就绪标志0:高驱动未就绪1:高驱动就绪</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LDOVSRF</td><td>LDO电压选择就绪标志0:LDO电压选择未就绪1:LDO电压选择就绪</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>BLDOON</td><td>开启备份SRAM电压选择器当该位由软件置位,开启备份SRAM电压调节器,用于在断开<eq>V_{DD}</eq>时保护备份SRAM中的数据。当断开<eq>V_{DD}</eq>断开,同时该位被清0,备份SRAM中的数据将会丢失。0:关闭备份SRAM电压选择器1:开启备份SRAM电压选择器</td></tr><tr><td>8</td><td>WUPEN</td><td>WKUP引脚唤醒使能0:关闭WKUP引脚唤醒功能1:开启WKUP引脚唤醒功能如果WUPEN在进入省电模式之前置1,WKUP引脚的上升沿会将系统从省电模式唤醒。由于WKUP引脚为高电平有效,WKUP引脚内部被配置为输入下拉模式。当置位该控制位后,当输入为高的时候,将会触发一个唤醒事件。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>BLDORF</td><td>备份域电压选择器就绪标志0:备份域电压选择器未就绪1:备份域电压选择器就绪</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(<eq>V_{DD}</eq>高于设定的LVD阈值)1:低电压事件出现(<eq>V_{DD}</eq>等于或低于LVD阈值)注意:LVD功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式1:设备曾进入过待机模式该位只能由POR/PDR或通过设置PMU_CTL寄存器的STBRST位来清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件1:收到来自WKUP引脚或RTC唤醒事件,包括RTC侵入事件、RTC闹钟事件、RTC时间戳事件或RTC唤醒。该位只能由POR/PDR或通过设置PMU_CTL寄存器的WURST位来清零。</td></tr></table>
