## 3.4. PMU 寄存器

PMU 基地址：0x4000 7000

## 3.4.1. 控制寄存器 0（PMU_CTL0）

地址偏移：0x00

复位值：0x0002 9000（从待机模式唤醒后复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13"></td><td>LPLDOEN</td><td colspan="2">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="2">DSMODVS[1:0]</td><td colspan="3">保留</td><td>BKPWEN</td><td colspan="4">保留</td><td>STBRST</td><td>WURST</td><td colspan="2">LPMOD[1:0]</td></tr><tr><td colspan="2"></td><td colspan="2">rw</td><td colspan="3"></td><td>rw</td><td colspan="4"></td><td>rc_w1</td><td>rc_w1</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>LPLDOEN</td><td>使能低功耗LDO。该位置位时,LDO将从正常功耗LDO切换为低功耗LDO。0:不使用LPLDO1:使用LPLDO</td></tr><tr><td>17:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:12</td><td>DSMODVS[1:0]</td><td>选择深度睡眠模式下的电压该位控制深度睡眠/深度睡眠1模式下的VCORE电压,以获得最佳的功耗和性能平衡。00:0.9V01:1.0V(默认值)10:1.1V11:1.2V注意:0.9V仅在NPLDO关闭时有效。</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>BKPWEN</td><td>RTC备份寄存器写使能0:禁止对RTC备份寄存器的写访问。1:允许对RTC备份寄存器的写访问。复位之后,任何对备份寄存器的写访问都将被禁止。如需对备份寄存器做写访问,需先将该位置1。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>STBRST</td><td>待机标志复位0:无影响1:复位待机标志读该位,始终返回0。</td></tr><tr><td>2</td><td>WURST</td><td>唤醒标志复位0:无影响1:复位唤醒标志读该位,始终返回0。</td></tr><tr><td>1:0</td><td>LPMOD[1:0]</td><td>选择 Cortex®-M23 进入 SLEEPDEEP 模式,MCU 进入的低功耗模式00:深度睡眠模式01:深度睡眠模式 110:保留11:待机模式</td></tr></table>

## 3.4.2. 电源控制和状态寄存器（PMU_CS）

地址偏移：0x04

复位值：0x0000 0000（从待机模式唤醒后不复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>NPRDY</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>LDOVSRF</td><td>WUPEN5</td><td>保留</td><td>WUPEN3</td><td>WUPEN2</td><td>WUPEN1</td><td>WUPENO</td><td colspan="6">保留</td><td>STBF</td><td>WUF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>NPRDY</td><td>NPLDO 就绪标志0:NPLDO 未就绪。1:NPLDO 就绪。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>LDOVSRF</td><td>LDO 电压选择就绪标志0:LDO 电压选择未就绪。1:LDO 电压选择就绪。</td></tr><tr><td>1312</td><td>WUPEN5保留</td><td>WKUP 引脚 5(PB5)唤醒使能0:禁能 WKUP 引脚 5 唤醒功能。1:使能 WKUP 引脚 5 唤醒功能。如果 WUPEN5 在进入省电模式之前置 1,WKUP 引脚 5 的上升沿会将系统从省电模式唤醒。由于 WKUP 引脚 5 为高电平有效,WKUP 引脚 5 内部被配置为输入下拉模必须保持复位值。</td></tr><tr><td>11</td><td>WUPEN3</td><td>WKUP引脚3(PA2)唤醒使能0:禁能WKUP引脚3唤醒功能。1:使能WKUP引脚3唤醒功能。如果WUPEN4在进入省电模式之前置1,WKUP引脚3的上升沿会将系统从省电模式唤醒。由于WKUP引脚3为高电平有效,WKUP引脚3内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>10</td><td>WUPEN2</td><td>WKUP引脚2(PB6)唤醒使能0:关闭WKUP引脚2唤醒功能。1:开启WKUP引脚2唤醒功能。如果WUPEN2在进入省电模式之前置1,WKUP引脚2的上升沿会将系统从省电模式唤醒。由于WKUP引脚2为高电平有效,WKUP引脚2内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>9</td><td>WUPEN1</td><td>WKUP引脚1(PC13/PA4)唤醒使能0:关闭WKUP引脚1唤醒功能。1:开启WKUP引脚1唤醒功能。如果WUPEN1在进入省电模式之前置1,WKUP引脚1的上升沿会将系统从省电模式唤醒。由于WKUP引脚1为高电平有效,WKUP引脚1内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。注意:LQFP48、QFN48封装下只有PC13可用。</td></tr><tr><td>8</td><td>WUPENO</td><td>WKUP引脚0(PA0)唤醒使能0:关闭WKUP引脚0唤醒功能。1:开启WKUP引脚0唤醒功能。如果WUPENO在进入省电模式之前置1,WKUP引脚0的上升沿会将系统从省电模式唤醒。由于WKUP引脚0为高电平有效,WKUP引脚0内部被配置为输入下拉模式。当在输入已经为高的时候置位该控制位,将会触发一个唤醒事件。</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>STBF</td><td>待机标志0:设备没进入过待机模式。1:设备曾进入过待机模式。该位只能由POR/PDR或通过置位PMU_CTL0寄存器的STBRST位来清零。当STBRST置位,经过3个CK_APB后,STBF标志位清零。</td></tr><tr><td>0</td><td>WUF</td><td>唤醒标志0:没有收到唤醒事件。1:唤醒事件由WKUP引脚或RTC事件包括RTC闹钟事件,时间戳事件,侵入事件和自动唤醒事件触发。该位只能由POR/PDR或通过设置PMU_CTL0寄存器的WURST位来清零。当WURST置位,经过3个CK_APB后,WUF标志位清零。</td></tr></table>

## 3.4.3. 控制寄存器 1（PMU_CTL1）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>EFDSPSLEEP</td><td>EFPSLEEP</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EFDSPSLEEP</td><td>深度睡眠模式/深度睡眠模式1下,EFLASH掉电控制该位仅在深度睡眠模式/深度睡眠模式1下由软件置1。0:EFLASH上电。1:EFLASH掉电。</td></tr><tr><td>4</td><td>EFPSLEEP</td><td>运行模式/运行模式1下,EFLASH掉电控制该位仅在运行模式/运行模式1下由软件置1。0:EFLASH上电。1:EFLASH掉电。注意:EFLASH掉电后,不能对其进行任何操作。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 3.4.4. 状态寄存器（PMU_STAT）

地址偏移：0x0C

复位值：0x00C0 0020（从待机模式唤醒后不复位）

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>EFLASHPS_ACTIVE</td><td>EFLASHPS_SLEEPP</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>EFLASHPS_ACTIVE</td><td>EFLASH 处于运行状态</td></tr><tr><td>4</td><td>EFLASHPS_SLEEP</td><td>EFLASH 处于睡眠状态。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 3.4.5. 参数寄存器（PMU_PAR）

地址偏移：0x10

复位值：0x190A 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="8">TWK_EFLASH[7:0]</td><td colspan="5">TSW_HIRCCNT[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:21</td><td>TWK_EFLASH[7:0]</td><td>EFLASH 从深度睡眠模式/深度睡眠模式 1 唤醒计数器。当从深度睡眠模式/深度睡眠模式 1 唤醒时,等待 TWK_EFLASH 个 HIRC 时钟周期。默认值为 200。</td></tr><tr><td>20:16</td><td>TSW_HIRCCNT[4:0]</td><td>当进入深度睡眠模式/深度睡眠模式 1 时,切换到 HIRC 时钟。等待 HIRC 计数后设置深度睡眠状态。默认值为 10 个 HIRC 时钟。</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
