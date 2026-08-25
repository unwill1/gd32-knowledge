## 3.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 3.4.1. 控制寄存器 0（PMU_CTL0）

GD32L233xx 产品

地址偏移：0x00

复位值：0x0000 C000（从待机模式唤醒后复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">LDOVS[1:0]</td><td>VCRSEL</td><td>VCEN</td><td>LDNP</td><td>LDNPDS P</td><td>保留</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td colspan="2">LPMOD[1:0]</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>LDOVS[1:0]</td><td>选择 LDO 输出在 PLL 关闭时,这些位由软件配置。在主 PLL 使能后,LDOVS 选择的电压生效。如果主 PLL 关闭,LDO 输出低电压模式被选中(该位的值不变)。0x:LDO 输出低电压模式(0.9V)。1x:LDO 输出高电压模式(1.1V)。</td></tr><tr><td>13</td><td>VCRSEL</td><td>VBAT 电池充电电阻的选择0:5 k 欧姆电阻用于 VBAT 电池充电。1:1.5 k 欧姆电阻用于 VBAT 电池充电。</td></tr><tr><td>12</td><td>VCEN</td><td>VBAT 电池充电使能0:禁能 VBAT 电池充电。1:使能 VBAT 电池充电。</td></tr><tr><td>11</td><td>LDNP</td><td>在运行 / 睡眠模式下使用 NPLDO 时,工作在低驱动模式0:使用 NPLDO 时,工作在正常驱动模式。1:使用 NPLDO 时,低驱动模式被使能。</td></tr><tr><td>10</td><td>LDNPDSP</td><td>在深度睡眠模式下使用 NPLDO 时,工作在低驱动模式0:使用 NPLDO 时,工作在正常驱动模式。1:使用 NPLDO 时,低驱动模式被使能。</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0:禁止对备份域寄存器的写访问。1:允许对备份域寄存器的写访问。复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000:2.1V001:2.3V010:2.4V011:2.6V100:2.7V101:2.9V110:3.0V111:PB7输入模拟电压(与0.8V进行比较)</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0:关闭低电压检测器。1:开启低电压检测器。</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0:无影响1:复位待机标志读该位,始终返回0。</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0:无影响1:复位唤醒标志读该位,始终返回0。</td></tr><tr><td>1:0</td><td>LPMOD[1:0]</td><td>选择Cortex®-M23进入SLEEPDEEP模式,MCU进入的低功耗模式00:深度睡眠模式01:深度睡眠模式110:深度睡眠模式211:待机模式</td></tr></table>

## GD32L235xx 产品

地址偏移：0x00

复位值：0x0000 C000（从待机模式唤醒后复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>LDOVS[1:0]</td><td>VCRSEL</td><td>VCEN</td><td>LDNP</td><td>LDNPDS P</td><td>保留</td><td>BKPWEN</td><td>LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>LPMOD[1:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rc_w1</td><td>rc_w1</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>LDOVS[1:0]</td><td>选择 LDO 输出在 PLL 关闭时,这些位由软件配置。在主 PLL 使能后,LDOVS 选择的电压生效。如果主 PLL 关闭,LDO 输出低电压模式被选中(该位的值不变)。0x:保留。10:温度自适应模式(1.1V)。11:LDO 输出高电压模式(1.1V)。注意:温度自适应模式适用于对电压稳定性要求较高的应用场景。</td></tr><tr><td>13</td><td>VCRSEL</td><td>VBAT 电池充电电阻的选择0:5k 欧姆电阻用于 VBAT 电池充电。1:1.5k 欧姆电阻用于 VBAT 电池充电。</td></tr><tr><td>12</td><td>VCEN</td><td>VBAT 电池充电使能0:禁能 VBAT 电池充电。1:使能 VBAT 电池充电。</td></tr><tr><td>11</td><td>LDNP</td><td>在运行 / 睡眠模式下使用 NPLDO 时,工作在低驱动模式0:使用 NPLDO 时,工作在正常驱动模式。1:使用 NPLDO 时,低驱动模式被使能。</td></tr><tr><td>10</td><td>LDNPDSP</td><td>在深度睡眠模式下使用 NPLDO 时,工作在低驱动模式0:使用 NPLDO 时,工作在正常驱动模式。1:使用 NPLDO 时,低驱动模式被使能。</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0:禁止对备份域寄存器的写访问。1:允许对备份域寄存器的写访问。复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置 1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000:2.1V001:2.3V010:2.4V011:2.6V100:2.7V101:2.9V110:3.0V</td></tr></table>

<table><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能0:关闭低电压检测器。1:开启低电压检测器。</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0:无影响1:复位待机标志读该位,始终返回0。</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0:无影响1:复位唤醒标志读该位,始终返回0。</td></tr><tr><td>1:0</td><td>LPMOD[1:0]</td><td>选择 Cortex®-M23 进入 SLEEPDEEP 模式,MCU 进入的低功耗模式00:深度睡眠模式01:深度睡眠模式 110:深度睡眠模式 211:待机模式</td></tr></table>

## 3.4.2. 电源控制和状态寄存器（PMU_CS）

GD32L233xx 产品

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>NPRDY</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LDOVSRF</td><td>保留</td><td>WUPEN4</td><td>WUPEN3</td><td>WUPEN2</td><td>WUPEN1</td><td>WUPENO</td><td colspan="5">保留</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td></td><td>r</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>NPRDY</td><td>NPLDO 就绪标志0:NPLDO 未就绪。1:NPLDO 就绪。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LDOVSRF</td><td>LDO 电压选择就绪标志0: LDO电压选择未就绪。1: LDO电压选择就绪。</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>WUPEN4</td><td>WKUP引脚4(PC6)唤醒使能0:禁能WKUP引脚4唤醒功能。1:使能WKUP引脚4唤醒功能。如果WUPEN4在进入省电模式之前置1,WKUP引脚4的上升沿会将系统从省电模式唤醒。由于WKUP引脚4为高电平有效,WKUP引脚4内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PB2)唤醒使能0:禁能WKUP引脚3唤醒功能。1:使能WKUP引脚3唤醒功能。如果WUPEN4在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>WUPEN2</td><td>WKUP引脚2(PA2)唤醒使能0:关闭WKUP引脚2唤醒功能。1:开启WKUP引脚2唤醒功能。如果WUPEN2在进入省电模式之前置1,WKUP引脚2的上升沿会将系统从省电模式唤醒。由于WKUP引脚2为高电平有效,WKUP引脚2内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PC13)唤醒使能0:关闭WKUP引脚1唤醒功能。1:开启WKUP引脚1唤醒功能。如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>8</td><td>WUPENO</td><td>WKUP引脚0(PA0)唤醒使能0:关闭WKUP引脚0唤醒功能。1:开启WKUP引脚0唤醒功能。如果WUPENO在进入省电模式之前置1,WKUP引脚0的上升沿会将系统从省电模式唤醒。由于WKUP引脚0为高电平有效,WKUP引脚0内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(<eq>V_{DD}</eq>高于设定的LVD阈值)。1:低电压事件出现(<eq>V_{DD}</eq>等于或低于LVD阈值)。注意:LVD功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式。</td></tr></table>

1：设备曾进入过待机模式。

该位只能由 POR / PDR 或通过置位 PMU_CTL0 寄存器的 STBRST 位来清零。

0 WUF 唤醒标志

0：没有收到唤醒事件。

1：唤醒事件由 WKUP 引脚或 RTC 事件包括 RTC 闹钟事件，时间戳事件，侵入事件和自动唤醒事件触发。

该位只能由 POR / PDR 或通过设置 PMU_CTL0 寄存器的 WURST 位来清零。

## GD32L235xx 产品

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>NPRDY</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>LDOVSRF</td><td>WUPEN5</td><td>WUPEN4</td><td>WUPEN3</td><td>WUPEN2</td><td>WUPEN1</td><td>WUPENO</td><td>保留</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td></td><td>r</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>NPRDY</td><td>NPLDO 就绪标志0:NPLDO 未就绪。1:NPLDO 就绪。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LDOVSRF</td><td>LDO 电压选择就绪标志0:LDO 电压选择未就绪。1:LDO 电压选择就绪。</td></tr><tr><td>13</td><td>WUPEN5</td><td>WKUP 引脚 5(PB5)唤醒使能0:禁能 WKUP 引脚 4 唤醒功能。1:使能 WKUP 引脚 4 唤醒功能。如果 WUPEN5 在进入省电模式之前置 1,WKUP 引脚 5 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚 5 为高电平有效,WKUP 引脚 5 内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>12</td><td>WUPEN4</td><td>WKUP 引脚 4(PC6)唤醒使能0:禁能 WKUP 引脚 4 唤醒功能。1:使能 WKUP 引脚 4 唤醒功能。如果 WUPEN4 在进入省电模式之前置 1,WKUP 引脚 4 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚 4 为高电平有效,WKUP 引脚 4 内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PB2)唤醒使能0:禁能WKUP引脚3唤醒功能。1:使能WKUP引脚3唤醒功能。如果WUPEN4在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>WUPEN2</td><td>WKUP引脚2(PA2)唤醒使能0:关闭WKUP引脚2唤醒功能。1:开启WKUP引脚2唤醒功能。如果WUPEN2在进入省电模式之前置1,WKUP引脚2的上升沿会将系统从省电模式唤醒。由于WKUP引脚2为高电平有效,WKUP引脚2内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PC13)唤醒使能0:关闭WKUP引脚1唤醒功能。1:开启WKUP引脚1唤醒功能。如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>8</td><td>WUPENO</td><td>WKUP引脚0(PA0)唤醒使能0:关闭WKUP引脚0唤醒功能。1:开启WKUP引脚0唤醒功能。如果WUPENO在进入省电模式之前置1,WKUP引脚0的上升沿会将系统从省电模式唤醒。由于WKUP引脚0为高电平有效,WKUP引脚0内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(<eq>V_{DD}</eq>高于设定的LVD阈值)。1:低电压事件出现(<eq>V_{DD}</eq>等于或低于LVD阈值)。注意:LVD功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式。1:设备曾进入过待机模式。该位只能由POR/PDR或通过置位PMU_CTL0寄存器的STBRST位来清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件。1:唤醒事件由WKUP引脚或RTC事件包括RTC闹钟事件,时间戳事件,侵入事件和自动唤醒事件触发。该位只能由POR/PDR或通过设置PMU_CTL0寄存器的WURST位来清零。</td></tr></table>

## 3.4.3. 控制寄存器 1（PMU_CTL1）

GD32L233xx 产品

地址偏移：0x08

复位值：0x0001 0000（从待机模式唤醒后复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>SRAM1PD2</td><td>NRRD2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>CORE1WAKE</td><td>CORE1SLEEP</td><td colspan="2">保留</td><td>SRAM1PWAKE</td><td>SRAM1PSLEEP</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SRAM1PD2</td><td>进入深度睡眠模式2时,SRAM1电源状态0:SRAM1掉电。1:SRAM1电源状态与运行/运行1/运行模式2一样。注意:当从深度睡眠2模式唤醒时,SRAM1电源状态与进入深度睡眠2模式之前一致。</td></tr><tr><td>16</td><td>NRRD2</td><td>在深度睡眠2模式下没有保留寄存器0:CPU有保留寄存器。1:没有保留寄存器。</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CORE1WAKE</td><td>COREOFF1域唤醒当MCU处于运行/运行1/运行模式2下,并且COREOFF1处于睡眠模式,该位可以由软件置1。该位由硬件清零。</td></tr><tr><td>4</td><td>CORE1SLEEP</td><td>COREOFF1域掉电当MCU处于运行/运行1/运行模式2下,并且COREOFF1处于运行模式,该位可以由软件置1。该位由硬件清零。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SRAM1PWAKE</td><td>SRAM1唤醒当MCU处于运行/运行1/运行模式2下,并且SRAM1处于睡眠模式,该位可以由软件置1。该位由硬件清零。</td></tr></table>

SRAM1PSLEEP SRAM1 掉电

当 MCU处于运行 / 运行 1/ 运行模式 2 下，并且 SRAM1处于运行模式，该位可以由软件置 1。

该位由硬件清零。

## GD32L235xx 产品

地址偏移：0x08

复位值：0x0001 0000（从待机模式唤醒后复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>SRAM1PD2</td><td>保留</td></tr><tr><td colspan="15">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>EFDSPSLEEP</td><td>EFPSLEE P</td><td colspan="2">保留</td><td>SRAM1PWAKE</td><td>SRAM1PSLEEP</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>SRAM1PD2</td><td>进入深度睡眠模式2时,SRAM1电源状态0:SRAM1掉电。1:SRAM1电源状态与运行一样。注意:当从深度睡眠2模式唤醒时,SRAM1电源状态与进入深度睡眠2模式之前一致。</td></tr><tr><td>16:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EFDSPSLEEP</td><td>深度睡眠 / 深度睡眠1 /深度睡眠2下EFLASH电源控制。0:深度睡眠 / 深度睡眠1 /深度睡眠2下EFLASH电源打开。1:深度睡眠 / 深度睡眠1 /深度睡眠2下EFLASH电源关闭。</td></tr><tr><td>4</td><td>EFPSLEEP</td><td>运行模式下EFLASH电源控制。0:运行模式下EFLASH电源打开。1:运行模式下EFLASH电源关闭。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SRAM1PWAKE</td><td>SRAM1唤醒当MCU处于运行模式下,并且SRAM1处于睡眠模式,该位可以由软件置1。该位由硬件清零。</td></tr><tr><td>0</td><td>SRAM1PSLEEP</td><td>SRAM1掉电当MCU处于运行模式下,并且SRAM1处于运行模式,该位可以由软件置1。该位由硬件清零。</td></tr></table>

## 3.4.4. 状态寄存器（PMU_STAT）

GD32L233xx 产品

地址偏移：0x0C

复位值：0x0000 0018（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>CORE1P S_ACTIVE</td><td>CORE1P S_SLEEP</td><td>SRAM1P S_ACTIVE</td><td>SRAM1P S_SLEEP</td><td>DPF2</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CORE1PS_ACTIVE</td><td>COREOFF1 域处于运行状态。</td></tr><tr><td>4</td><td>CORE1PS_SLEEP</td><td>COREOFF1 域处于睡眠状态。</td></tr><tr><td>3</td><td>SRAM1PS_ACTIVE</td><td>SRAM1 处于运行状态。</td></tr><tr><td>2</td><td>SRAM1PS_SLEEP</td><td>SRAM1 处于睡眠状态。</td></tr><tr><td>1</td><td>DPF2</td><td>深度睡眠模式 2 状态标志位。当进入深度睡眠模式 2 时该位由硬件置位。软件写 0 清除该位。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## GD32L235xx 产品

地址偏移：0x0C

复位值：0x0000 0028（从待机模式唤醒后不复位）

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>EFLASHPS_ACTIVE</td><td>EFLASHPS_SLEEP</td><td>SRAM1PS_ACTIVE</td><td>SRAM1PS_SLEEP</td><td>DPF2</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EFLASHPS_ACTIVE</td><td>EFLASH 处于运行状态。</td></tr><tr><td>4</td><td>EFLASHPS_SLEEP</td><td>EFLASH 处于睡眠状态。</td></tr><tr><td>3</td><td>SRAM1PS_ACTIVE</td><td>SRAM1 处于运行状态。</td></tr><tr><td>2</td><td>SRAM1PS_SLEEP</td><td>SRAM1 处于睡眠状态。</td></tr><tr><td>1</td><td>DPF2</td><td>深度睡眠模式 2 状态标志位。当进入深度睡眠模式 2 时该位由硬件置位。软件写 0 清除该位。</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 3.4.5. 参数寄存器（PMU_PAR）

GD32L233xx 产品

地址偏移：0x10

复位值：0x040A 2064

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TWKEN</td><td>TWKSRAM1EN</td><td>TWKCORE1EN</td><td colspan="8">TWK_CORE1[7:0]</td><td colspan="5">TSW_IRC16MCNT[4:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td colspan="9">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">TWK_SRAM1[7:0]</td><td colspan="8">TWK_CORE0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TWKEN</td><td>唤醒深度睡眠模式2时是否使用软件值0:在唤醒深度睡眠模式2时,使用硬件应答信号。1:在唤醒深度睡眠模式2时,使用软件设定值,该值由<eq>TWK\_CORE0[7:0]</eq>来设定。</td></tr><tr><td>30</td><td>TWKSRAM1EN</td><td>唤醒SRAM1电源域时是否使用软件值0:唤醒SRAM1时,使用硬件应答信号。1:唤醒SRAM1时,使用软件设定值,该值由<eq>TWK\_SRAM1[7:0]</eq>来设定。</td></tr><tr><td>29</td><td>TWKCORE1EN</td><td>唤醒COREOFF1时是否使用软件值0:唤醒COREOFF1时,使用硬件应答信号。1:唤醒COREOFF1时,使用软件设定值,该值由<eq>TWK\_CORE1[7:0]</eq>来设定。</td></tr><tr><td>28:21</td><td>TWK_CORE1[7:0]</td><td>COREOFF1域电源开关唤醒时间。步长为4个时钟,最大64us。</td></tr><tr><td>20:16</td><td>TSW_IRC16MCNT[4:0]</td><td>当进入深度睡眠模式时,切换到IRC16M时钟。等待IRC16M计数后设置深度睡眠状态。默认值为10个IRC16M时钟。</td></tr></table>

15:8 TWK_SRAM1[7:0] SRAM1 域电源开关的唤醒时间。步长为 4 个 IRC16M 时钟，最大 64us。

7:0 TWK_CORE0[7:0] COREOFF0 域电源开关的唤醒时间。步长为 2 个 IRC16M 时钟，最大 32us。

GD32L235xx 产品

地址偏移：0x10

复位值：0x000A 2064

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>TWKEN</td><td colspan="2">保留</td><td colspan="8">TWK_EFLASH[7:0]</td><td colspan="5">TSW_IRC16MCNT[4:0]</td></tr><tr><td colspan="3">rw</td><td colspan="8">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">TWK_SRAM1[7:0]</td><td colspan="8">TWK_CORE0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>TWKEN</td><td>唤醒深度睡眠模式2时是否使用软件值0:在唤醒深度睡眠模式2时,使用硬件应答信号。1:在唤醒深度睡眠模式2时,使用软件设定值,该值由<eq>TWK\_CORE0[7:0]</eq>来设定。</td></tr><tr><td>30:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:21</td><td><eq>TWK\_EFLASH[7:0]</eq></td><td>EFLASH唤醒计数EFLASH电源开关唤醒时间,<eq>TWK\_EFLASH</eq>个IRC16M时钟。</td></tr><tr><td>20:16</td><td><eq>TSW\_IRC16MCNT[4:0]</eq></td><td>当进入深度睡眠模式时,切换到IRC16M时钟。等待IRC16M计数后设置深度睡眠状态。默认值为10个IRC16M时钟。</td></tr><tr><td>15:8</td><td><eq>TWK\_SRAM1[7:0]</eq></td><td>SRAM1域电源开关的唤醒时间。步长为4个IRC16M时钟,最大64us。</td></tr><tr><td>7:0</td><td><eq>TWK\_CORE0[7:0]</eq></td><td>COREOFF0域电源开关的唤醒时间。步长为2个IRC16M时钟,最大32us。</td></tr></table>
