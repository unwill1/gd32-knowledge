## 3.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 3.4.1. 控制寄存器 0（PMU_CTL0）

地址偏移：0x00

复位值：0x0002 6000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="2">VUVDVC</td><td colspan="2">VOVDVC</td><td>VUVDEN</td><td>VOVDEN</td><td colspan="2">VAVDVC</td><td>VAVDEN</td><td colspan="2">保留</td><td colspan="2">DSLPVS</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">LDOVS[4:0]</td><td colspan="2">保留</td><td>BKPWEN</td><td colspan="3">LVDT[2:0]</td><td>LVDEN</td><td>STBRST</td><td>WURST</td><td>STBMOD</td><td>LDOLP</td></tr><tr><td colspan="5">Rw</td><td colspan="2"></td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:27</td><td>VUVDVC[1:0]</td><td><eq>V_{CORE}</eq>低压检测器电压等级配置位这些位由软件置位和清除。00: 配置<eq>V_{CORE}</eq>低压检测器电压等级为0.95V01: 配置<eq>V_{CORE}</eq>低压检测器电压等级为0.85V10: 配置<eq>V_{CORE}</eq>低压检测器电压等级为0.75V11: 配置<eq>V_{CORE}</eq>低压检测器电压等级为0.65V</td></tr><tr><td>26:25</td><td>VOVDVC[1:0]</td><td><eq>V_{CORE}</eq>过压检测器电压等级配置位这些位由软件置位和清除。00: 配置<eq>V_{CORE}</eq>过压检测器电压等级为1.25V01: 配置<eq>V_{CORE}</eq>过压检测器电压等级为1.35V10: 配置<eq>V_{CORE}</eq>过压检测器电压等级为1.45V11: 配置<eq>V_{CORE}</eq>过压检测器电压等级为1.55V</td></tr><tr><td>24</td><td>VUVDEN</td><td><eq>V_{CORE}</eq>低压检测器使能位该位由软件置位和清除。0: 失能<eq>V_{CORE}</eq>低压检测器1: 使能 <eq>V_{CORE}</eq>低压检测器</td></tr><tr><td>23</td><td>VOVDEN</td><td><eq>V_{CORE}</eq>过压检测器使能位该位由软件置位和清除。0: 失能<eq>V_{CORE}</eq>过压检测器1:使能VCORE过压检测器</td></tr><tr><td>22:21</td><td>VAVDVC[1:0]</td><td>VDDA模拟电压检测器电压等级配置位这些位由软件置位和清除。00:配置VDDA模拟电压检测器电压等级为1.8V01:配置VDDA模拟电压检测器电压等级为2.2V10:配置VDDA模拟电压检测器电压等级为2.6V11:配置VDDA模拟电压检测器电压等级为2.9V</td></tr><tr><td>20</td><td>VAVDEN</td><td>VDDA模拟电压检测器使能位该位由软件置位和清除。0:失能VDDA模拟电压检测器1:使能VDDA模拟电压检测器</td></tr><tr><td>19:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>DSLPVS</td><td>深度睡眠模式电压选择这些位控制系统睡眠模式时VCORE电压以获得功耗和性能之间的最佳权衡。00:0.8V01:0.9V10:1.0V(默认)11:1.1V</td></tr><tr><td>15:11</td><td>LDOVS[4:0]</td><td>LDO输出电压选择当主锁相环关闭时,这些位由软件设置。当主锁相环使能时,LDOVS位选择的LDO输出电压生效。如果主锁相环闭合,LDO输出电压低模式选择(该位的值不改变)。00000~01011:保留01100:配置VCORE电压为1.1V01101:保留01110:配置VCORE电压为1.15V01111:保留10000:保留10001~11111:保留注意:该位只能配置为1.1V或1.15V,禁止配置为保留。</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>备份域写使能0:禁止对备份域寄存器的写访问。1:允许对备份域寄存器的写访问。复位之后,任何对备份域寄存器的写访问都将被禁止。如需对备份域寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:5</td><td>LVDT[2:0]</td><td>低电压检测器阈值000: 2.15V</td></tr><tr><td></td><td></td><td>001: 2.3V</td></tr><tr><td></td><td></td><td>010: 2.45V</td></tr><tr><td></td><td></td><td>011: 2.6V</td></tr><tr><td></td><td></td><td>100: 2.75V</td></tr><tr><td></td><td></td><td>101: 2.9V</td></tr><tr><td></td><td></td><td>110: 3.0V</td></tr><tr><td></td><td></td><td>111: PA10 外部输入模拟电压 LDO_IN(与 1.2V 进行比较)</td></tr><tr><td>4</td><td>LVDEN</td><td>低电压检测器使能</td></tr><tr><td></td><td></td><td>0: 关闭低电压检测器</td></tr><tr><td></td><td></td><td>1: 开启低电压检测器</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位</td></tr><tr><td></td><td></td><td>0: 无影响</td></tr><tr><td></td><td></td><td>1: 复位待机标志</td></tr><tr><td></td><td></td><td>读该位,始终返回 0。</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位</td></tr><tr><td></td><td></td><td>0: 无影响</td></tr><tr><td></td><td></td><td>1: 复位唤醒标志</td></tr><tr><td></td><td></td><td>读该位,始终返回 0。</td></tr><tr><td>1</td><td>STBMOD</td><td>待机模式选择</td></tr><tr><td></td><td></td><td>0: 当 Cortex®-M33 进入 SLEEPDEEP 模式时,MCU 进入 Deep-sleep 模式。</td></tr><tr><td></td><td></td><td>1: 当 Cortex®-M33 进入 SLEEPDEEP 模式时,MCU 进入待机模式。</td></tr><tr><td>0</td><td>LDOLP</td><td>LDO 低功耗模式</td></tr><tr><td></td><td></td><td>0: 当系统进入深度睡眠模式时,LDO仍正常工作。</td></tr><tr><td></td><td></td><td>1: 当系统进入深度睡眠模式时,LDO 进入低功耗模式。</td></tr></table>

## 3.4.2. 电源控制和状态寄存器（PMU_CS）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>WUPEN4</td><td>WUPEN3</td><td>WUPEN2</td><td>WUPEN1</td><td>WUPENO</td><td>VUVDF1</td><td>VOVDF1</td><td>VUVDF0</td><td>VOVDF0</td><td>VAVDF</td><td>LVDF</td><td>STBF</td><td>WUF</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>WUPEN4</td><td>WKUP引脚4(PC5)唤醒使能0:关闭WKUP引脚4唤醒功能。1:开启WKUP引脚4唤醒功能。如果WUPEN4在进入省电模式之前置1,WKUP引脚4的上升沿会将系统从省电模式唤醒。由于WKUP引脚4为高电平有效,WKUP引脚4内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PA2)唤醒使能0:关闭WKUP引脚3唤醒功能。1:开启WKUP引脚3唤醒功能。如果WUPEN3在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>WUPEN2</td><td>WKUP引脚2(PE6)唤醒使能0:关闭WKUP引脚2唤醒功能。1:开启WKUP引脚2唤醒功能。如果WUPEN2在进入省电模式之前置1,WKUP引脚2的上升沿会将系统从省电模式唤醒。由于WKUP引脚2为高电平有效,WKUP引脚2内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PC13)唤醒使能0:关闭WKUP引脚1唤醒功能。1:开启WKUP引脚1唤醒功能。如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>8</td><td>WUPEN0</td><td>WKUP引脚0(PA0)唤醒使能0:关闭WKUP引脚0唤醒功能。1:开启WKUP引脚0唤醒功能。如果WUPEN0在进入省电模式之前置1,WKUP引脚0的上升沿会将系统从省电模式唤醒。由于WKUP引脚0为高电平有效,WKUP引脚0内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>7</td><td>VUVDF1</td><td>数字滤波后<eq>V_{CORE}</eq>低电压检测器标志位由硬件设置和清除,仅当VUVDEN使能时有效<eq>V_{CORE}</eq>大于VUVD阈值。<eq>V_{CORE}</eq>小于等于VUVD阈值。</td></tr><tr><td>6</td><td>VOVDF1</td><td>数字滤波后<eq>V_{CORE}</eq>过电压检测器标志位由硬件设置和清除,仅当VOVDEN使能时有效0:VCORE小于VOVD阈值。1:VCORE大于等于VOVD阈值。</td></tr><tr><td>5</td><td>VUVDF0</td><td>数字滤波后VCORE低电压检测器标志位由硬件设置和清除,仅当VUVDEN使能时有效0:VCORE大于VUVD阈值。1:VCORE小于等于VUVD阈值。</td></tr><tr><td>4</td><td>VOVDF0</td><td>数字滤波后VCORE过电压检测器标志位由硬件设置和清除,仅当VOVDEN使能时有效0:VCORE小于VOVD阈值。1:VCORE大于等于VOVD阈值。</td></tr><tr><td>3</td><td>VAVDF</td><td>VDDA模拟电压检测器输出标志位由硬件设置和清除,仅当VAVDEN使能时有效0:VDDA大于等于由VAVDVC位配置的VAVD阈值。1:VDDA小于由VAVDVC位配置的VAVD阈值。</td></tr><tr><td>2</td><td>LVDF</td><td>低电压状态标志0:低电压事件没出现(VDD高于设定的LVD阈值)。1:低电压事件出现(VDD等于或低于LVD阈值)。注意:LVD功能在待机模式被禁用。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式。1:设备曾进入过待机模式。该位只能由POR/PDR或通过置位PMU_CTL0寄存器的STBRST位来清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件。1:唤醒事件由WKUP引脚或RTC事件包括RTC闹钟事件,时间戳事件,侵入事件和自动唤醒事件触发。该位只能由POR/PDR或通过设置PMU_CTL0寄存器的WURST位来清零。</td></tr></table>

## 3.4.3. 控制寄存器 1（PMU_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>TEMPHF</td><td>TEMPLF</td><td>VBATHF</td><td>VBATLF</td><td colspan="3">保留</td><td>BKPVSRF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td></td><td></td><td></td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>VBTMEN</td><td colspan="3">保留</td><td>BKPVSE N</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TEMPHF</td><td>温度监测高阈值标志位0: 温度低于温度监测的高阈值1: 温度等于或高于温度监测的高阈值</td></tr><tr><td>22</td><td>TEMPLF</td><td>温度监测低阈值标志位0: 温度低于温度监测的低阈值1: 温度等于或高于温度监测的低阈值</td></tr><tr><td>21</td><td>VBATHF</td><td><eq>V_{BAT}</eq>监测高阈值标志位0: <eq>V_{BAT}</eq>电压低于<eq>V_{BAT}</eq>监测的高阈值1: <eq>V_{BAT}</eq>电压等于或高于<eq>V_{BAT}</eq>监测的高阈值</td></tr><tr><td>20</td><td>VBATLF</td><td><eq>V_{BAT}</eq>监测低阈值标志位0: <eq>V_{BAT}</eq>电压低于<eq>V_{BAT}</eq>监测的低阈值1: <eq>V_{BAT}</eq>电压等于或高于<eq>V_{BAT}</eq>监测的低阈值</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>BKPVSRF</td><td>备份域电压稳压器就绪标志位该位由硬件置位用于指示备份域电压稳压器是否就绪。0: 备份域电压稳压器未就绪1: 备份域电压稳压器已就绪</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>VBTMEN</td><td><eq>V_{BAT}</eq>和温度监测器使能位当该位置位将使能<eq>V_{BAT}</eq>供电电压监测和温度监测。0: 失能<eq>V_{BAT}</eq>和温度监测器1: 使能<eq>V_{BAT}</eq>和温度监测器</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BKPVSEN</td><td>BGR电路使能位0: 失能BGR参考电路1: 使能BGR参考电路</td></tr></table>

## 3.4.4. 控制寄存器 2（PMU_CTL2）

地址偏移：0x0C

复位值：0x0000 0000（仅上电复位后复位）

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>VCRSEL</td><td>VCEN</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>VCRSEL</td><td><eq>V_{BAT}</eq>电池充电电阻的选择0:5k欧姆电阻用于<eq>V_{BAT}</eq>电池充电。1:1.5k欧姆电阻用于<eq>V_{BAT}</eq>电池充电。</td></tr><tr><td>8</td><td>VCEN</td><td><eq>V_{BAT}</eq>电池充电使能0:禁能<eq>V_{BAT}</eq>电池充电。1:使能<eq>V_{BAT}</eq>电池充电。</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 3.4.5. 控制寄存器 3（PMU_CTL3）

地址偏移：0x18

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">VUVDO_DNF</td><td colspan="8">VOVDO_DNF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>VUVDO_DNF</td><td>VUVD 模拟输出数字噪声滤波器这些位用于配置 VUVD 模拟输出上的数字噪声滤波器,数字滤波器将滤波峰值的长度高达 VUVDO_DNF[7:0] * 1024 * TPCLK0:关闭数字滤波器1:开启数字滤波器,滤波峰值长度高达 1024 * TPCLK...255:开启数字滤波器,滤波峰值长度高达 255 * 1024 * TPCLK</td></tr><tr><td>7:0</td><td>VOVDO_DNF</td><td>VOVD 模拟输出数字噪声滤波器这些位用于配置 VOVD 模拟输出上的数字噪声滤波器,数字滤波器将滤波峰值的长度高达 VOVDO_DNF[7:0] * 1024 * TPCLK0:关闭数字滤波器1:开启数字滤波器,滤波峰值长度高达1024 * TPCLK...255:开启数字滤波器,滤波峰值长度高达255 * 1024 * TPCLK</td></tr></table>
