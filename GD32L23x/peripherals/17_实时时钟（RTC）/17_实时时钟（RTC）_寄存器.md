## 17.4. RTC 寄存器

RTC基地址：0x4000 2800

## 17.4.1. 时间寄存器（RTC_TIME）

偏移地址：0x00

系统复位值：当BPSHAD = 0，0x0000 0000

当BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td colspan="9"></td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td></td><td colspan="3">rw</td><td colspan="4">rw</td><td></td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 17.4.2. 日期寄存器（RTC_DATE）

偏移地址：0x04

系统复位值：当 BPSHAD = 0，0x0000 2101

当 BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">YRT[3:0]</td><td colspan="4">YRU[3:0]</td></tr><tr><td colspan="8"></td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td>MONT</td><td colspan="4">MONU[2:0]</td><td colspan="2">保留</td><td colspan="2">DAYT</td><td colspan="4">DAYU</td></tr><tr><td colspan="3">rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>YRT[3:0]</td><td>年份十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>YRU[3:0]</td><td>年份个位值,以 BCD 码形式存储</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期0x0: 保留0x1: 星期一...0x7: 星期日</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[2:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 17.4.3. 控制寄存器（RTC_CTL）

偏移地址：0x08

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>OUT2EN</td><td>LXTALSTBRST</td><td colspan="5">保留</td><td>ITSEN</td><td>COEN</td><td colspan="2">OS[1:0]</td><td>OPOL</td><td>COS</td><td>DSM</td><td>S1H</td><td>A1H</td></tr><tr><td>rw</td><td>w</td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TSIE</td><td>WTIE</td><td>ALRM1IE</td><td>ALRM0IE</td><td>TSEN</td><td>WTEN</td><td>ALRM1EN</td><td>ALRM0EN</td><td>保留</td><td>CS</td><td>BPSHAD</td><td>REFEN</td><td>TSEG</td><td colspan="3">WTCS[2:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>OUT2EN</td><td>RTC_OUT 引脚选择0: RTC_OUT 输出到 PC131: RTC_OUT 输出到 PB2/PB14</td></tr></table>

<table><tr><td>30</td><td>LXTALSTBRST</td><td>低速晶体振荡器稳定标志位复位0:低速晶体振荡器稳定标志位不复位1:低速晶体振荡器稳定标志位复位</td></tr><tr><td>29:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>ITSEN</td><td>内部时间戳事件使能0:关闭内部时间戳事件1:使能内部时间戳事件</td></tr><tr><td>23</td><td>COEN</td><td>校准输出使能0:关闭校准输出1:使能校准输出</td></tr><tr><td>22:21</td><td>OS[1:0]</td><td>输出选择该位用来选择输出的标志源。0x00:禁用RTC_ALARM输出0x01:启用闹钟0标志输出0x10:启用闹钟1标志输出0x11:启用唤醒标志输出</td></tr><tr><td>20</td><td>OPOL</td><td>输出极性该位用来反转RTC_ALARM输出。0:禁用反转RTC_ALARM输出1:启用反转RTC_ALARM输出</td></tr><tr><td>19</td><td>COS</td><td>校准输出选择仅当COEN=1并且预分频器是默认值时有效。0:校准输出是512Hz1:校准输出是1Hz</td></tr><tr><td>18</td><td>DSM</td><td>夏令时屏蔽位该位可以通过软件灵活使用。常用来记录夏令时调整。</td></tr><tr><td>17</td><td>S1H</td><td>减1小时(冬季时间变化)当前时间非零的情况下,将当前时间减去一个小时。0:没有影响1:在下一个秒改变时,将减少一个小时</td></tr><tr><td>16</td><td>A1H</td><td>增加1小时(夏季时间变化)将当前时间增加一个小时。0:没有影响1:在下一个秒改变时,将增加一个小时</td></tr><tr><td>15</td><td>TSIE</td><td>时间戳中断使能0:禁用时间戳中断1:启用时间戳中断</td></tr><tr><td>14</td><td>WTIE</td><td>自动唤醒定时器中断使能0:禁用自动唤醒定时器中断</td></tr></table>

<table><tr><td></td><td></td><td>1: 启用自动唤醒定时器中断</td></tr><tr><td>13</td><td>ALRM1IE</td><td>RTC 闹钟 1 中断使能0: 禁用闹钟中断1: 启用闹钟中断</td></tr><tr><td>12</td><td>ALRM0IE</td><td>RTC 闹钟 0 中断使能0: 禁用闹钟中断1: 启用闹钟中断</td></tr><tr><td>11</td><td>TSEN</td><td>时间戳功能使能0: 禁用时间戳功能1: 启用时间戳功能</td></tr><tr><td>10</td><td>WTEN</td><td>自动唤醒定时器功能使能0: 禁用自动唤醒定时器功能1: 启用自动唤醒定时器功能</td></tr><tr><td>9</td><td>ALRM1EN</td><td>闹钟 1 功能使能0: 禁用闹钟功能1: 启用闹钟功能</td></tr><tr><td>8</td><td>ALRM0EN</td><td>闹钟 0 功能使能0: 禁用闹钟功能1: 启用闹钟功能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CS</td><td>时间格式0: 24 小时制1: 12 小时制注意:仅能在初始化状态进行写入</td></tr><tr><td>5</td><td>BPSHAD</td><td>禁止影子寄存器0: 读取的日历的值来自影子日历寄存器1: 读取的日历的值来自真正日历寄存器注意:如果 APB1 时钟的频率小于 RTCCLK 频率的 7 倍,该位必须设为 1</td></tr><tr><td>4</td><td>REFEN</td><td>参考时钟检测功能使能0: 禁用参考时钟检测功能1: 启用参考时钟检测功能注意:仅能在初始化状态进行写入并且 FACTOR_S 必须为 0x00FF</td></tr><tr><td>3</td><td>TSEG</td><td>时间戳事件有效检测边沿0: 上升沿是时间戳事件有效检测沿1: 下降沿是时间戳事件有效检测沿</td></tr><tr><td>2:0</td><td>WTCS[2:0]</td><td>自动唤醒定时器时钟选择0x0: RTC 时钟的 16 分频0x1: RTC 时钟的 8 分频</td></tr></table>

0x2：RTC 时钟的 4 分频

0x3：RTC 时钟的 2 分频

0x4，0x5：ck_spre（默认 1Hz）时钟

0x6，0x7：ck_spre（默认 1Hz）时钟并且将唤醒计数器值增加 2<sup>16</sup>

## 17.4.4. 状态寄存器（RTC_STAT）

偏移地址：0x0C

系统复位：仅INITM，INITF和RSYNF位被置0，其他位无影响。

备份域复位值：0x0000 0007

写保护寄存器

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>ITSF</td><td>SCPF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w0</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TP2F</td><td>TP1F</td><td>TP0F</td><td>TSOVRF</td><td>TSF</td><td>WTF</td><td>ALRM1F</td><td>ALRM0F</td><td>INITM</td><td>INITF</td><td>RSYNF</td><td>YCM</td><td>SOPF</td><td>WTWF</td><td>ALRM1WF</td><td>ALRM0WF</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rw</td><td>r</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>ITSF</td><td>内部时间戳标志当检测到内部时间戳事件时,该位硬件置1。可以通过向该位软件写0来清除,并且和TSF位一起清零。</td></tr><tr><td>16</td><td>SCPF</td><td>平滑校准挂起标志在未进入初始化模式时向RTC_HRFC进行软件写操作,该位被硬件置1。当平滑校准设置开始执行后,该位被硬件清零0。</td></tr><tr><td>15</td><td>TP2F</td><td>RTC_TAMP2 事件标志当在tamper2输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>14</td><td>TP1F</td><td>RTC_TAMP1 事件标志当在tamper1输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>13</td><td>TP0F</td><td>RTC_TAMP0 事件标志当在tamper0输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>12</td><td>TSOVRF</td><td>时间戳事件溢出标志如果TSF位已经置位,当再次检测到时间戳事件时,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>11</td><td>TSF</td><td>时间戳事件标志当检测到一个时间戳事件时,该位会通过硬件置1。可以通过向该位软件写0来清</td></tr></table>

除。

<table><tr><td>10</td><td>WTF</td><td>唤醒定时器标志当唤醒定时器减到0时,该位会通过硬件置1。可以通过向该位软件写0来清除。该标志需要在WTF位再次置1之前的1.5个RTC时钟周期前完成软件清除该位。</td></tr><tr><td>9</td><td>ALRM1F</td><td>Alarm1发生标志当现在的时间/日期与闹钟1设置的时间/日期匹配的时候,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>8</td><td>ALRM0F</td><td>Alarm0发生标志当现在的时间/日期与闹钟0设置的时间/日期匹配的时候,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>7</td><td>INITM</td><td>进入初始化模式0:自由运行模式1:进入初始化模式设置时间/日期和预分频,计数器将停止运行</td></tr><tr><td>6</td><td>INITF</td><td>初始化状态标志该位被硬件置1,初始化状态时可以设置日历寄存器和预分频器。0:日历寄存器和预分频器的值不能改变1:日历寄存器和预分频器的值可以改变</td></tr><tr><td>5</td><td>RSYNF</td><td>寄存器同步标志每2个RTCCLK将会由硬件置1一次,同时会复制当前日历时间/日期到影子日历寄存器。初始化模式(INITM),移位操作挂起标志(SOPF)或者禁止影子寄存器模式(BPSHAD=1)会清除该位。该位也可以通过软件写0清除。0:影子寄存器未同步1:影子寄存器已同步</td></tr><tr><td>4</td><td>YCM</td><td>年份配置标志当日历寄存器的年份值不为0时硬件置10:日历尚未初始化1:日历已经初始化</td></tr><tr><td>3</td><td>SOPF</td><td>移位功能操作挂起标志0:移位操作没有挂起1:移位操作挂起</td></tr><tr><td>2</td><td>WTWF</td><td>唤醒定时器可写标志0:不允许更新唤醒定时器1:允许更新唤醒定时器</td></tr><tr><td>1</td><td>ALRM1WF</td><td>Alarm1配置可写标志硬件置位和清零。ALRM1EN=0时,标记alarm是否可写。0:不允许修改Alarm寄存器设置1:允许修改Alarm寄存器设置</td></tr><tr><td>0</td><td>ALRM0WF</td><td>Alarm0配置可写标志硬件置位和清零。ALRM0EN=0时,标记alarm是否可写。</td></tr></table>

0：不允许修改 Alarm 寄存器设置

1：允许修改 Alarm 寄存器设置

## 17.4.5. 预分频寄存器（RTC_PSC）

偏移地址：0x10

系统复位：无影响

备份域复位值：0x007F 00FF

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td colspan="7">FACTOR_A[6:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">FACTOR_S[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:16</td><td>FACTOR_A[6:0]</td><td>异步预分频系数ck_apre频率 = RTCCLK 频率/(FACTOR_A+1)</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>FACTOR_S[14:0]</td><td>同步预分频系数ck_spre频率 = ck_apre频率/(FACTOR_S+1)</td></tr></table>

## 17.4.6. 唤醒定时器寄存器（RTC_WUT）

偏移地址：0x14

系统复位：无影响

备份域复位值：0x0000 FFFF

写保护寄存器

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WTRV[15:0]</td></tr></table>

<table><tr><td>15:0</td><td>WTRV[15:0]</td><td>自动唤醒定时器重载值当WTEN置1时,每隔(WTRV[15:0]+1)个ck_wut周期,WTF置1一次。ck_wut通过WTCS[2:0]位选择.注意:禁止在WTCS[2:0]=0b 011时配置WTRV=0x0000。该寄存器仅在WTWF=1时才能写操作</td></tr></table>

## 17.4.7. 闹钟 0 时间日期寄存器（RTC_ALRM0TD）

偏移地址：0x1C

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MSKD</td><td>DOWS</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td><td>MSKH</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MSKM</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>MSKS</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MSKD</td><td>闹钟日期位域屏蔽位0:不屏蔽日期/天位域1:屏蔽日期/天位域</td></tr><tr><td>30</td><td>DOWS</td><td>星期选择0:此时 DAYU[3:0]代表日期个位值1:此时 DAYU[3:0]代表星期几,此时 DAYT[1:0]无意义</td></tr><tr><td>29:28</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码格式存储</td></tr><tr><td>27:24</td><td>DAYU[3:0]</td><td>日期个位值或星期天数,以 BCD 码格式存储</td></tr><tr><td>23</td><td>MSKH</td><td>闹钟小时位域屏蔽位0:不屏蔽小时位域1:屏蔽小时位域</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0:AM 或 24 小时制1:PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>MSKM</td><td>闹钟分钟位域屏蔽位0:不屏蔽分钟位域1: 屏蔽分钟位域</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>MSKS</td><td>闹钟秒位域屏蔽位0: 不屏蔽秒位域1: 屏蔽秒位域</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 17.4.8. 闹钟 1 时间日期寄存器（RTC_ALRM1TD）

偏移地址：0x20

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MSKD</td><td>DOWS</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td><td>MSKH</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MSKM</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>MSKS</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MSKD</td><td>闹钟日期位域屏蔽位0:不屏蔽日期/天位域1:屏蔽日期/天位域</td></tr><tr><td>30</td><td>DOWS</td><td>星期选择0:此时 DAYU[3:0] 代表日期个位值1:此时 DAYU[3:0] 代表星期几,此时 DAYT[1:0]无意义</td></tr><tr><td>29:28</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码格式存储</td></tr><tr><td>27:24</td><td>DAYU[3:0]</td><td>日期个位值或星期天数,以 BCD 码格式存储</td></tr><tr><td>23</td><td>MSKH</td><td>闹钟小时位域屏蔽位0:不屏蔽小时位域1:屏蔽小时位域</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0:AM 或 24 小时制1:PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以BCD码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以BCD码形式存储</td></tr><tr><td>15</td><td>MSKM</td><td>闹钟分钟位域屏蔽位0:不屏蔽分钟位域1:屏蔽分钟位域</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以BCD码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以BCD码形式存储</td></tr><tr><td>7</td><td>MSKS</td><td>闹钟秒位域屏蔽位0:不屏蔽秒位域1:屏蔽秒位域</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以BCD码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以BCD码形式存储</td></tr></table>

## 17.4.9. 写保护钥匙寄存器（RTC_WPK）

偏移地址：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">WPK[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>WPK[7:0]</td><td>写保护的解锁值</td></tr></table>

## 17.4.10. 亚秒寄存器（RTC_SS）

偏移地址：0x28

系统复位值：当BPSHAD = 0，0x0000 0000。

当BPSHAD = 1，无影响。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值该位值是同步预分频计数器的值。秒的小数部分由下面公式给出:秒的小数部分 = (FACTOR_S - SSC) / (FACTOR_S + 1)</td></tr></table>

## 17.4.11. 移位控制寄存器（RTC_SHIFTCTL）

偏移地址：0x2C

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅当SOPF=0，该寄存器可写。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>A1S</td><td colspan="15">保留</td></tr><tr><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SFS[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>A1S</td><td>增加一秒0:无影响1:增加一秒到时钟/日历该位与SFS位一起使用,增加小于一秒到当前时间。</td></tr><tr><td>30:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>SFS[14:0]</td><td>减去小于一秒的一段时间这位的值将增加到同步预分频计数器当仅用SFS时,由于同步预分频器是一个递减计数器,所以时钟将会延迟。延迟(秒)=SFS/(FACTOR_S+1)当A1S和SFS一起使用时,时钟将会提前提前(秒)=(1-(SFS/(FACTOR_S+1)))</td></tr></table>


注意：写入此寄存器会导致 RSYNF 位被清 0。


## 17.4.12. 时间戳时间寄存器（RTC_TTS）

偏移地址：0x30

备份域复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标记0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 17.4.13. 时间戳日期寄存器（RTC_DTS）

偏移地址：0x34

备份域复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历日期。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td colspan="2">MONT</td><td colspan="3">MONU[3:0]</td><td colspan="2">保留</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td></tr><tr><td colspan="3">r</td><td colspan="2">r</td><td colspan="3">r</td><td colspan="2"></td><td colspan="2">r</td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期数</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[3:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 17.4.14. 时间戳亚秒寄存器（RTC_SSTS）

偏移地址：0x38

备份域复位：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值</td></tr></table>


TSF 置 1 时记录当时的同步预分频计数器的值。


## 17.4.15. 高精度频率补偿寄存器（RTC_HRFC）

偏移地址：0x3C

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>FREQI</td><td>CWND8</td><td>CWND16</td><td>保留</td><td>CMSK[8:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>FREQI</td><td>RTC频率增加488.5ppm0:无影响1:每2<eq>^{11}</eq>个脉冲增加一个RTCCLK脉冲该位需与CMSK位一起使用。如果输入时钟频率是32.768KHz,在32s校准窗期间,增加的RTCCLK脉冲数是(512* FREQI)- CMSK</td></tr><tr><td>14</td><td>CWND8</td><td>采用8秒校准周期0:无影响1:采用8秒校准周期注意:当CWND8=1,CMSK[1:0]被锁定在“00”。</td></tr><tr><td>13</td><td>CWND16</td><td>采用16秒校准周期0:无影响1:采用16秒校准周期注意:当CWND16=1,CMSK[0]被锁定在“0”.</td></tr><tr><td>12:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>CMSK[8:0]</td><td>校准周期RTCCLK脉冲屏蔽数在2<eq>^{20}</eq>个RTCCLK脉冲之内屏蔽的脉冲数此项功能可以以0.9537 ppm的分辨率来降低日历频率</td></tr></table>

## 17.4.16. 侵入寄存器（RTC_TAMP）

偏移地址：0x40

备份域复位：0x0000 0000

系统复位：无影响

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>TP2IE</td><td>TP1IE</td><td>TP0IE</td><td>保留</td><td>TP2MASK</td><td>TP1MASK</td><td>TP0MASK</td><td>保留</td><td>TP2NOERASE</td><td>TP1NOERASE</td><td>TP0NOERASE</td><td>ALRMOUTTYPE</td><td colspan="2">保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DISPU</td><td colspan="2">PRCH[1:0]</td><td colspan="2">FLT[1:0]</td><td colspan="3">FREQ[2:0]</td><td>TPTS</td><td>TP2EG</td><td>TP2EN</td><td>TP1EG</td><td>TP1EN</td><td>TPIE</td><td>TP0EG</td><td>TP0EN</td></tr><tr><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>TP2IE</td><td>侵入检测2中断使能0:禁用侵入检测2中断1:启用侵入检测2中断</td></tr><tr><td>28</td><td>TP1IE</td><td>侵入检测1中断使能0:禁用侵入检测1中断1:启用侵入检测1中断</td></tr><tr><td>27</td><td>TP0IE</td><td>侵入检测0中断使能0:禁用侵入检测0中断1:启用侵入检测0中断</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>TP2MASK</td><td>侵入检测2屏蔽位0:Tamper 2引脚产生入侵事件,并且需要软件清除TP2F标志才能允许下一次入侵事件检测1:Tamper 2引脚产生入侵事件,TP2F位不会置位,由内部硬件清零,备份域寄存器不会被擦除注意:当TP2MASK为1时,Tamper2中断不能使能</td></tr><tr><td>24</td><td>TP1MASK</td><td>侵入检测1屏蔽位0:Tamper 1引脚产生入侵事件,并且需要软件清除TP1F标志才能允许下一次入侵事件检测1:Tamper 1引脚产生入侵事件,TP1F位不会置位,由内部硬件清零,备份域寄存器不会被擦除注意:当TP1MASK为1时,Tamper1中断不能使能</td></tr><tr><td>23</td><td>TP0MASK</td><td>侵入检测0屏蔽位0:Tamper 0引脚产生入侵事件,并且需要软件清除TP0F标志才能允许下一次入侵事件检测1:Tamper 0引脚产生入侵事件,TP0F位不会置位,由内部硬件清零,备份域寄存器不会被擦除注意:当TP0MASK为1时,Tamper0中断不能使能</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TP2NOERASE</td><td>Tamper 2不擦除备份域寄存器0:Tamper 2事件将擦除备份域寄存器1:Tamper 2事件不擦除备份域寄存器</td></tr><tr><td>20</td><td>TP1NOERASE</td><td>Tamper 1不擦除备份域寄存器0:Tamper 1事件将擦除备份域寄存器1:Tamper 1事件不擦除备份域寄存器</td></tr><tr><td>19</td><td>TP0NOERASE</td><td>Tamper 0不擦除备份域寄存器0:Tamper 0事件将擦除备份域寄存器1:Tamper 0事件不擦除备份域寄存器</td></tr><tr><td>18</td><td>ALRMOUTTYPE</td><td>RTC_ALARM输出类型0:开漏输出1:推挽输出</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>DISPU</td><td>RTC_TAMPx上拉禁用位0:使能内部RTC_TAMPx引脚上的上拉电阻并在采样前进行预充电1:禁用预充电功能</td></tr><tr><td>14:13</td><td>PRCH[1:0]</td><td>RTC_TAMPx的预充电时间该位设置决定了每次采样前的预充电时间0x0:1个RTC时钟0x1:2个RTC时钟0x2:4个RTC时钟0x3:8个RTC时钟</td></tr><tr><td>12:11</td><td>FLT[1:0]</td><td>RTC_TAMPx过滤器计数设置该位决定了侵入事件检测模式和在电平检测模式下连续采样的次数。0x0:用边沿模式检测侵入事件,预充电功能被自动禁用。0x1:用电平模式检测侵入事件。连续采样到2个有效电平时认为发生侵入事件0x2:用电平模式检测侵入事件。连续采样到4个有效电平时认为发生侵入事件0x3:用电平模式检测侵入事件。连续采样到8个有效电平时认为发生侵入事件</td></tr><tr><td>10:8</td><td>FREQ[2:0]</td><td>侵入事件电平模式检测的采样频率0x0:每次采样间隔32768个RTCCLK(若RTCCLK=32.768KHz,频率为1Hz)0x1:每次采样间隔16384个RTCCLK(若RTCCLK=32.768KHz,频率为2Hz)0x2:每次采样间隔8192个RTCCLK(若RTCCLK=32.768KHz,频率为4Hz)0x3:每次采样间隔4096个RTCCLK(若RTCCLK=32.768KHz,频率为8Hz)0x4:每次采样间隔2048个RTCCLK(若RTCCLK=32.768KHz,频率为16Hz)0x5:每次采样间隔1024个RTCCLK(若RTCCLK=32.768KHz,频率为32Hz)0x6:每次采样间隔512个RTCCLK(若RTCCLK=32.768KHz,频率为64Hz)0x7:每次采样间隔256个RTCCLK(若RTCCLK=32.768KHz,频率为128Hz)</td></tr><tr><td>7</td><td>TPTS</td><td>侵入事件时触发时间戳0:无影响1:当检测到侵入事件时,即使TSEN=0,TSF也会被置位</td></tr><tr><td>6</td><td>TP2EG</td><td>TAMP2输入管脚的侵入事件检测触发沿如果侵入检测处于边沿模式(FLT=0):0:上升沿触发一个侵入检测事件1:下降沿触发一个侵入检测事件如果侵入检测处于电平模式(FLT!=0):0:低电平触发一个侵入检测事件1:高电平触发一个侵入检测事件</td></tr><tr><td>5</td><td>TP2EN</td><td>Tamper2检测使能位0:禁用Tamper2检测功能1:启用Tamper2检测功能</td></tr><tr><td>4</td><td>TP1EG</td><td>TAMP1输入管脚的侵入事件检测触发沿如果侵入检测处于边沿模式(FLT=0):0:上升沿触发一个侵入检测事件</td></tr></table>

<table><tr><td></td><td></td><td>1: 下降沿触发一个侵入检测事件如果侵入检测处于电平模式(FLT !=0):0: 低电平触发一个侵入检测事件1: 高电平触发一个侵入检测事件</td></tr><tr><td>3</td><td>TP1EN</td><td>Tamper1 检测使能位0: 禁用 Tamper1 检测功能1: 启用 Tamper1 检测功能</td></tr><tr><td>2</td><td>TPIE</td><td>侵入检测中断使能0: 禁用侵入中断1: 启用侵入中断</td></tr><tr><td>1</td><td>TP0EG</td><td>TAMP0 输入管脚的侵入事件检测触发沿如果侵入检测处于边沿模式(FLT =0):0: 上升沿触发一个侵入检测事件1: 下降沿触发一个侵入检测事件如果侵入检测处于电平模式(FLT !=0):0: 低电平触发一个侵入检测事件1: 高电平触发一个侵入检测事件</td></tr><tr><td>0</td><td>TP0EN</td><td>Tamper0 检测使能位0: 禁用 Tamper0 检测功能1: 启用 Tamper0 检测功能</td></tr></table>


注意：强烈建议在改变侵入检测配置之前，应该复位 TpxEN位。


## 17.4.17. 闹钟 0 亚秒寄存器（RTC_ALRM0SS）

偏移地址： 0x44

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器，仅当ALRM0EN=0或INITM=1，可以进行写操作。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">MSKSSC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SSC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>MSKSSC[3:0]</td><td>亚秒位域的屏蔽控制位0x0:屏蔽闹钟亚秒设置。当所有其他的闹钟位域匹配的时候,闹钟将会在每一秒钟到达的时刻置1。</td></tr></table>

0x1：SSC[0]位用于时间匹配，其他位被忽略。

0x2：SSC[1：0]位用于时间匹配，其他位被忽略。

0x3：SSC[2：0]位用于时间匹配，其他位被忽略。

0x4：SSC[3：0]位用于时间匹配，其他位被忽略。

0x5：SSC[4：0]位用于时间匹配，其他位被忽略。

0x6：SSC[5：0]位用于时间匹配，其他位被忽略。

0x7：SSC[6：0]位用于时间匹配，其他位被忽略。

0x8：SSC[7：0]位用于时间匹配，其他位被忽略。

0x9：SSC[8：0]位用于时间匹配，其他位被忽略。

0xA：SSC[9：0]位用于时间匹配，其他位被忽略。

0xB：SSC[10：0]位用于时间匹配，其他位被忽略。

0xC：SSC[11：0]位用于时间匹配，其他位被忽略。

0xD：SSC[12：0]位用于时间匹配，其他位被忽略。

0xE：SSC[13：0]位用于时间匹配，其他位被忽略。

0xF：SSC[14：0]位用于时间匹配，其他位被忽略。

注意：同步预分频计数器的第 15 位（RTC_SS 寄存器中的 SSC[15]）从不被匹配。

## 17.4.18. 闹钟 1 亚秒寄存器（RTC_ALRM1SS）

偏移地址：0x48

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器，仅当 ALRM1EN=0 或 INITM=1，可以进行写操作。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">MSKSSC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SSC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>MSKSSC[3:0]</td><td>亚秒位域的屏蔽控制位0x0:屏蔽闹钟亚秒设置。当所有其他的闹钟位域匹配的时候,闹钟将会在每一秒钟到达的时刻置1。0x1:SSC[0]位用于时间匹配,其他位被忽略。0x2: SSC[1: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x3: SSC[2: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x4: SSC[3: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x5: SSC[4: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x6: SSC[5: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x7: SSC[6: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x8: SSC[7: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0x9: SSC[8: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xA: SSC[9: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xB: SSC[10: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xC: SSC[11: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xD: SSC[12: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xE: SSC[13: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>0xF: SSC[14: 0]位用于时间匹配,其他位被忽略。</td></tr><tr><td></td><td></td><td>注意:同步预分频计数器的第15位(RTC_SS寄存器中的SSC[15])从不被匹配。</td></tr><tr><td>23:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>SSC[14:0]</td><td>闹钟亚秒值该值为闹钟亚秒值,用于与同步预分频计数器匹配。匹配位数由MSKSSC位控制。</td></tr></table>

## 17.4.19. 备份寄存器（RTC_BKPx）（x=0..4）

偏移地址： 0x50 到 0x64

备份域复位：0x0000 0000

系统复位：无影响

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>数据软件可读写寄存器。由于此寄存器可由<eq>V_{BAT}</eq>供电,因此寄存器值在省电模式下依然保持有效。当侵入检测标志位TPxF置1,这些寄存器会被复位。当FMC读保护功能禁用时,这些寄存器会被复位。</td></tr></table>
