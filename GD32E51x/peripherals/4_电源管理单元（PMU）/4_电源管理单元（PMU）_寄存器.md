## 4.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 4.4.1. 控制寄存器 0（PMU_CTL0）

地址偏移：0x00

复位值：0x0000 C000（从待机模式唤醒后复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="2">LDEN[1:0]</td><td>HDS</td><td>HDEN</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>LDNP</td><td>LDLP</td><td>保留</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>STBMOD</td><td>LDOLP</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td></td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:18</td><td>LDEN[1:0]</td><td>深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,低驱动模式使能00:在深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,禁用低驱动模式01:保留10:保留11:在深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,使能低驱动模式</td></tr><tr><td>17</td><td>HDS</td><td>高驱动模式切换器选择 IRC8M 或 HXTAL 作为系统时钟,当 HDRF 被置位时,由软件将该位置 1。该位被置位后,系统进入高驱动模式。可由软件清 0,也可在退出深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 或 HDEN 被清 0 时由硬件清 0。0:没有高驱动模式切换器1:有高驱动模式切换器</td></tr><tr><td>16</td><td>HDEN</td><td>高驱动模式使能当系统时钟为 IRC8M 或 HXTAL 时,该位由软件置位。该位可由软件清零或当系统退出深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 由硬件清零。0:禁用高驱动模式1:使能高驱动模式</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11</td><td>LDNP</td><td>使用正常功耗 LDO 时,工作在低驱动模式0:使用正常功耗 LDO 时,工作在正常驱动模式1:使用正常功耗 LDO 且 LDEN 为 11 时,低驱动模式被使能</td></tr><tr><td>10</td><td>LDLP</td><td>使用低功耗 LDO 时,工作在低驱动模式0:使用低功耗 LDO 时,工作在正常驱动模式1:使用低功耗LDO且LDEN为11时,低驱动模式被使能</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0:禁止对备份域寄存器的写访问1:允许对备份域寄存器的写访问复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000:2.1V001:2.3V010:2.4V011:2.6V100:2.7V101:2.9V110:3.0V111:3.1V</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0:关闭低电压检测器1:开启低电压检测器</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0:无影响1:复位待机标志读该位,始终返回0</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0:无影响1:复位唤醒标志读该位,始终返回0</td></tr><tr><td>1</td><td>STBMOD</td><td>待机模式0:当Cortex®-M33进入SLEEPDEEP模式时,系统进入深度睡眠模式/深度睡眠模式1/深度睡眠模式21:当Cortex®-M33进入SLEEPDEEP模式时,系统进入待机模式</td></tr><tr><td>0</td><td>LDOLP</td><td>LDO低功耗模式0:当系统进入深度睡眠模式/深度睡眠模式1/深度睡眠模式2时,LDO仍正常工作1:当系统进入深度睡眠模式/深度睡眠模式1/深度睡眠模式2时,LDO进入低功耗模式注意:在深度睡眠模式下,个别外设可能会开启IRC8M时钟来做一些工作。在这种情况下,如果LDO正处于低功耗模式,LDO会自动从低功耗模式切换到正常工作模式,并保持正常工作模式,直到外设工作完毕。</td></tr></table>

## 4.4.2. 电源控制和状态寄存器 0（PMU_CS0）

地址偏移：0x04

复位值：0x0000 0000 (从待机模式唤醒后不复位)

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">保留</td><td colspan="2">LDRF[1:0]</td><td>HDSRF</td><td>HDRF</td></tr><tr><td colspan="14">rc_w1</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>WUPEN7</td><td>保留</td><td>WUPEN5</td><td>WUPEN4</td><td>WUPEN3</td><td>WUPEN2</td><td>WUPEN1</td><td>WUPENO</td><td>WUPEN6</td><td colspan="4">保留</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>19:18</td><td>LDRF[1:0]</td><td>低驱动模式就绪标志在深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,且 LDO 处于低驱动模式,这些位由硬件设置。软件对这些位写 11 可以清 0。00: 深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,普通驱动模式01: 保留10: 保留11: 深度睡眠模式 / 深度睡眠模式 1 / 深度睡眠模式 2 下,低驱动模式</td></tr><tr><td>17</td><td>HDSRF</td><td>高驱动切换器就绪标志0: 高驱动切换器未就绪1: 高驱动切换器就绪</td></tr><tr><td>16</td><td>HDRF</td><td>高驱动准备就绪标志0: 高驱动未就绪1: 高驱动就绪</td></tr><tr><td>15</td><td>WUPEN7</td><td>WKUP 引脚 7(PF8)唤醒使能0: 关闭 WKUP 引脚 7 唤醒功能1: 开启 WKUP 引脚 7 唤醒功能如果 WUPEN7 在进入省电模式之前置 1, WKUP 引脚 7 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚 7 为高电平有效,WKUP 引脚 7 内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>WUPEN5</td><td>WKUP 引脚 5(PB5)唤醒使能0: 关闭 WKUP 引脚 5 唤醒功能1: 开启 WKUP 引脚 5 唤醒功能如果 WUPEN5 在进入省电模式之前置 1, WKUP 引脚 5 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚 5 为高电平有效,WKUP 引脚 5 内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>12</td><td>WUPEN4</td><td>WKUP引脚4(PC5)唤醒使能0:关闭WKUP引脚4唤醒功能1:开启WKUP引脚4唤醒功能如果WUPEN4在进入省电模式之前置1,WKUP引脚4的上升沿会将系统从省电模式唤醒。由于WKUP引脚4为高电平有效,WKUP引脚4内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PA2)唤醒使能0:关闭WKUP引脚3唤醒功能1:开启WKUP引脚3唤醒功能如果WUPEN3在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>WUPEN2</td><td>WKUP引脚2(PE6)唤醒使能0:关闭WKUP引脚2唤醒功能1:开启WKUP引脚2唤醒功能如果WUPEN2在进入省电模式之前置1,WKUP引脚2的上升沿会将系统从省电模式唤醒。由于WKUP引脚2为高电平有效,WKUP引脚2内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PC13)唤醒使能0:关闭WKUP引脚1唤醒功能1:开启WKUP引脚1唤醒功能如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>8</td><td>WUPEN0</td><td>WKUP引脚0(PA0)唤醒使能0:关闭WKUP引脚0唤醒功能1:开启WKUP引脚0唤醒功能如果WUPEN0在进入省电模式之前置1,WKUP引脚0的上升沿会将系统从省电模式唤醒。由于WKUP引脚0为高电平有效,WKUP引脚0内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>7</td><td>WUPEN6</td><td>WKUP引脚6(PB15)唤醒使能0:关闭WKUP引脚6唤醒功能1:开启WKUP引脚6唤醒功能如果WUPEN6在进入省电模式之前置1,WKUP引脚6的上升沿会将系统从省电模式唤醒。由于WKUP引脚6为高电平有效,WKUP引脚6内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>6:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(<eq>V_{DD}</eq>高于设定的LVD阈值)1:低电压事件出现(<eq>V_{DD}</eq>等于或低于LVD阈值)注意:LVD 功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式1:设备曾进入过待机模式该位只能由POR/PDR或通过置位PMU_CTL0寄存器的STBRST位来清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件1:收到来自WKUP引脚或RTC闹钟事件该位只能由POR/PDR或通过设置PMU_CTL0寄存器的WURST位来清零。</td></tr></table>

## 4.4.3. 控制寄存器 1（PMU_CTL1）

地址偏移：0x08

复位值：0x0000 0000（从待机模式唤醒后复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>DPMOD2</td><td>DPMOD1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>DPMOD2</td><td>深度睡眠模式2使能0:无作用1:当SLEEPDEEP位为1,STBMOD位为0时,进入深度睡眠模式2</td></tr><tr><td>0</td><td>DPMOD1</td><td>深度睡眠模式1使能0:无作用1:当SLEEPDEEP位为1,STBMOD位为0,且DPMOD2位为0时,进入深度睡眠模式1</td></tr></table>

## 4.4.4. 电源控制和状态寄存器 1（PMU_CS1）

地址偏移：0x0C

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>DPF2</td><td>DPF1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>DPF2</td><td>深度睡眠模式 2 状态标志位。当进入深度睡眠模式 2 时该位由硬件置位。软件写 0 清除该位。</td></tr><tr><td>0</td><td>DPF1</td><td>深度睡眠模式 1 状态标志位。当进入深度睡眠模式 1 时该位由硬件置位。软件写 0 清除该位。</td></tr></table>
