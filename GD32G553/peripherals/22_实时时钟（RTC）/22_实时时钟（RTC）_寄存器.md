## 22.4. RTC 寄存器

RTC基地址：0x4000 2800

## 22.4.1. 时间寄存器（RTC_TIME）

偏移地址：0x00

系统复位值：当BPSHAD = 0，0x0000 0000

当BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td colspan="9"></td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td></td><td colspan="3">rw</td><td colspan="4">rw</td><td></td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.2. 日期寄存器（RTC_DATE）

偏移地址：0x04

系统复位值：当 BPSHAD = 0，0x0000 2101

当 BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">YRT[3:0]</td><td colspan="4">YRU[3:0]</td></tr><tr><td colspan="8"></td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td>MONT</td><td colspan="4">MONU[2:0]</td><td colspan="2">保留</td><td colspan="2">DAYT</td><td colspan="4">DAYU</td></tr><tr><td colspan="3">rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>YRT[3:0]</td><td>年份十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>YRU[3:0]</td><td>年份个位值,以 BCD 码形式存储</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期0x0:保留0x1:星期一...0x7:星期日</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[2:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.3. 控制寄存器（RTC_CTL）

偏移地址：0x08

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>TAMPCLK</td><td>ITSEN</td><td>COEN</td><td colspan="2">OS[1:0]</td><td>OPOL</td><td>COS</td><td>DSM</td><td>S1H</td><td>A1H</td></tr><tr><td colspan="6"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TSIE</td><td>WTIE</td><td>ALRM1IE</td><td>ALRM0IE</td><td>TSEN</td><td>WTEN</td><td>ALRM1EN</td><td>ALRM0EN</td><td>保留</td><td>CS</td><td>BPSHAD</td><td>REFEN</td><td>TSEG</td><td colspan="3">WTCS[2:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>TAMPCLK</td><td>边沿Tamper需要RTC时钟0:需要RTC时钟1:不需要RTC时钟</td></tr><tr><td>24</td><td>ITSEN</td><td>内部时间戳事件使能0:关闭内部时间戳事件1:使能内部时间戳事件</td></tr><tr><td>23</td><td>COEN</td><td>校准输出使能0:关闭校准输出1:使能校准输出</td></tr><tr><td>22:21</td><td>OS[1:0]</td><td>输出选择该位用来选择输出的标志源。0x00:禁用RTC_ALARM输出0x01:启用闹钟0标志输出0x10:启用闹钟1标志输出0x11:启用唤醒标志输出</td></tr><tr><td>20</td><td>OPOL</td><td>输出极性该位用来反转RTC_ALARM输出。0:禁用反转RTC_ALARM输出1:启用反转RTC_ALARM输出</td></tr><tr><td>19</td><td>COS</td><td>校准输出选择仅当COEN=1并且预分频器是默认值时有效。0:校准输出是512Hz1:校准输出是1Hz</td></tr><tr><td>18</td><td>DSM</td><td>夏令时屏蔽位该位可以通过软件灵活使用。常用来记录夏令时调整。</td></tr><tr><td>17</td><td>S1H</td><td>减1小时(冬季时间变化)当前时间非零的情况下,将当前时间减去一个小时。0:没有影响1:在下一个秒改变时,将减少一个小时</td></tr></table>

<table><tr><td>16</td><td>A1H</td><td>增加1小时(夏季时间变化)将当前时间增加一个小时。0:没有影响1:在下一个秒改变时,将增加一个小时</td></tr><tr><td>15</td><td>TSIE</td><td>时间戳中断使能0:禁用时间戳中断1:启用时间戳中断</td></tr><tr><td>14</td><td>WTIE</td><td>自动唤醒定时器中断使能0:禁用自动唤醒定时器中断1:启用自动唤醒定时器中断</td></tr><tr><td>13</td><td>ALRM1IE</td><td>RTC闹钟1中断使能0:禁用闹钟中断1:启用闹钟中断</td></tr><tr><td>12</td><td>ALRM0IE</td><td>RTC闹钟0中断使能0:禁用闹钟中断1:启用闹钟中断</td></tr><tr><td>11</td><td>TSEN</td><td>时间戳功能使能0:禁用时间戳功能1:启用时间戳功能</td></tr><tr><td>10</td><td>WTEN</td><td>自动唤醒定时器功能使能0:禁用自动唤醒定时器功能1:启用自动唤醒定时器功能</td></tr><tr><td>9</td><td>ALRM1EN</td><td>闹钟1功能使能0:禁用闹钟功能1:启用闹钟功能</td></tr><tr><td>8</td><td>ALRM0EN</td><td>闹钟0功能使能0:禁用闹钟功能1:启用闹钟功能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CS</td><td>时间格式0:24小时制1:12小时制注意:仅能在初始化状态进行写入</td></tr><tr><td>5</td><td>BPSHAD</td><td>禁止影子寄存器0:读取的日历的值来自影子日历寄存器</td></tr></table>

<table><tr><td></td><td></td><td>1:读取的日历的值来自真正日历寄存器注意:如果APB时钟的频率小于RTCCLK频率的7倍,该位必须设为1</td></tr><tr><td>4</td><td>REFEN</td><td>参考时钟检测功能使能0:禁用参考时钟检测功能1:启用参考时钟检测功能注意:仅能在初始化状态进行写入并且FACTOR_S必须为0x00FF</td></tr><tr><td>3</td><td>TSEG</td><td>时间戳事件有效检测边沿0:上升沿是时间戳事件有效检测沿1:下降沿是时间戳事件有效检测沿</td></tr><tr><td>2:0</td><td>WTCS[2:0]</td><td>自动唤醒定时器时钟选择0x0:RTC时钟的16分频0x1:RTC时钟的8分频0x2:RTC时钟的4分频0x3:RTC时钟的2分频0x4,0x5:ck_spre(默认1Hz)时钟0x6,0x7:ck_spre(默认1Hz)时钟并且将唤醒计数器值增加<eq>2^{16}</eq></td></tr></table>

## 22.4.4. 状态寄存器（RTC_STAT）

偏移地址：0x0C

系统复位：仅INITM，INITF和RSYNF位被置0，其他位无影响。

备份域复位值：0x0000 0007

写保护寄存器

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>ITSF</td><td>SCPF</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w0</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TP2F</td><td>TP1F</td><td>TP0F</td><td>TSOVRF</td><td>TSF</td><td>WTF</td><td>ALRM1F</td><td>ALRM0F</td><td>INITM</td><td>INITF</td><td>RSYNF</td><td>YCM</td><td>SOPF</td><td>WTWF</td><td>ALRM1WF</td><td>ALRM0WF</td></tr><tr><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rw</td><td>r</td><td>rc_w0</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>ITSF</td><td>内部时间戳标志当检测到内部时间戳事件时,该位硬件置1。可以通过向该位软件写0来清除,并且和TSF位一起清零。</td></tr><tr><td>16</td><td>SCPF</td><td>平滑校准挂起标志在未进入初始化模式时向RTC_HRFC进行软件写操作,该位被硬件置1。当平滑校准设置开始执行后,该位被硬件清零0。</td></tr><tr><td>15</td><td>TP2F</td><td>RTC_TAMP2事件标志当在tamper2输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>14</td><td>TP1F</td><td>RTC_TAMP1事件标志当在tamper1输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>13</td><td>TP0F</td><td>RTC_TAMP0事件标志当在tamper0输入管脚检测到侵入事件时,该位硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>12</td><td>TSOVRF</td><td>时间戳事件溢出标志如果TSF位已经置位,当再次检测到时间戳事件时,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>11</td><td>TSF</td><td>时间戳事件标志当检测到一个时间戳事件时,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>10</td><td>WTF</td><td>唤醒定时器标志当唤醒定时器减到0时,该位会通过硬件置1。可以通过向该位软件写0来清除。该标志需要在WTF位再次置1之前的1.5个RTC时钟周期前完成软件清除该位。</td></tr><tr><td>9</td><td>ALRM1F</td><td>Alarm1发生标志当现在的时间/日期与闹钟1设置的时间/日期匹配的时候,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>8</td><td>ALRM0F</td><td>Alarm0发生标志当现在的时间/日期与闹钟0设置的时间/日期匹配的时候,该位会通过硬件置1。可以通过向该位软件写0来清除。</td></tr><tr><td>7</td><td>INITM</td><td>进入初始化模式0:自由运行模式1:进入初始化模式设置时间/日期和预分频,计数器将停止运行</td></tr><tr><td>6</td><td>INITF</td><td>初始化状态标志该位被硬件置1,初始化状态时可以设置日历寄存器和预分频器。0:日历寄存器和预分频器的值不能改变1:日历寄存器和预分频器的值可以改变</td></tr><tr><td>5</td><td>RSYNF</td><td>寄存器同步标志每2个RTCCLK将会由硬件置1一次,同时会复制当前日历时间/日期到影子日历寄存器。初始化模式(INITM),移位操作挂起标志(SOPF)或者禁止影子寄存器</td></tr></table>

<table><tr><td></td><td></td><td>模式(BPSHAD=1)会清除该位。该位也可以通过软件写0清除。</td></tr><tr><td></td><td></td><td>0:影子寄存器未同步</td></tr><tr><td></td><td></td><td>1:影子寄存器已同步</td></tr><tr><td>4</td><td>YCM</td><td>年份配置标志</td></tr><tr><td></td><td></td><td>当日历寄存器的年价值不为0时硬件置1</td></tr><tr><td></td><td></td><td>0:日历尚未初始化</td></tr><tr><td></td><td></td><td>1:日历已经初始化</td></tr><tr><td>3</td><td>SOPF</td><td>移位功能操作挂起标志</td></tr><tr><td></td><td></td><td>0:移位操作没有挂起</td></tr><tr><td></td><td></td><td>1:移位操作挂起</td></tr><tr><td>2</td><td>WTWF</td><td>唤醒定时器可写标志</td></tr><tr><td></td><td></td><td>0:不允许更新唤醒定时器</td></tr><tr><td></td><td></td><td>1:允许更新唤醒定时器</td></tr><tr><td>1</td><td>ALRM1WF</td><td>Alarm1 配置可写标志</td></tr><tr><td></td><td></td><td>硬件置位和清零。ALRM1EN=0时,标记alarm是否可写。</td></tr><tr><td></td><td></td><td>0:不允许修改Alarm寄存器设置</td></tr><tr><td></td><td></td><td>1:允许修改Alarm寄存器设置</td></tr><tr><td>0</td><td>ALRM0WF</td><td>Alarm0 配置可写标志</td></tr><tr><td></td><td></td><td>硬件置位和清零。ALRM0EN=0时,标记alarm是否可写。</td></tr><tr><td></td><td></td><td>0:不允许修改Alarm寄存器设置</td></tr><tr><td></td><td></td><td>1:允许修改Alarm寄存器设置</td></tr></table>

## 22.4.5. 预分频寄存器（RTC_PSC）

偏移地址：0x10

系统复位：无影响

备份域复位值：0x007F 00FF

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td colspan="7">FACTOR_A[6:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">FACTOR_S[14:0]</td></tr></table>

<table><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:16</td><td>FACTOR_A[6:0]</td><td>异步预分频系数ck_apre 频率 = RTCCLK 频率/(FACTOR_A+1)</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>FACTOR_S[14:0]</td><td>同步预分频系数ck_spre 频率 = ck_apre 频率/(FACTOR_S+1)</td></tr></table>

## 22.4.6. 唤醒定时器寄存器（RTC_WUT）

偏移地址：0x14

系统复位：无影响

备份域复位值：0x0000 FFFF

写保护寄存器

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WTRV[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>WTRV[15:0]</td><td>自动唤醒定时器重载值当WTEN置1时,每隔(WTRV[15:0]+1)个ck_wut周期,WTF置1一次。ck_wut通过WTCS[2:0]位选择.注意:禁止在WTCS[2:0]=0b 011时配置WTRV=0x0000。该寄存器仅在WTWF=1时才能写操作</td></tr></table>

## 22.4.7. 闹钟 0 时间日期寄存器（RTC_ALRM0TD）

偏移地址：0x1C

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MSKD</td><td>DOWS</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td><td>MSKH</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MSKM</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>MSKS</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MSKD</td><td>闹钟日期位域屏蔽位0:不屏蔽日期/天位域1:屏蔽日期/天位域</td></tr><tr><td>30</td><td>DOWS</td><td>星期选择0:此时 DAYU[3:0]代表日期个位值1:此时 DAYU[3:0]代表星期几,此时 DAYT[1:0]无意义</td></tr><tr><td>29:28</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码格式存储</td></tr><tr><td>27:24</td><td>DAYU[3:0]</td><td>日期个位值或星期天数,以 BCD 码格式存储</td></tr><tr><td>23</td><td>MSKH</td><td>闹钟小时位域屏蔽位0:不屏蔽小时位域1:屏蔽小时位域</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0:AM 或 24 小时制1:PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>MSKM</td><td>闹钟分钟位域屏蔽位0:不屏蔽分钟位域1:屏蔽分钟位域</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>MSKS</td><td>闹钟秒位域屏蔽位0:不屏蔽秒位域1:屏蔽秒位域</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.8. 闹钟 1 时间日期寄存器（RTC_ALRM1TD）

偏移地址：0x20

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MSKD</td><td>DOWS</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td><td>MSKH</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MSKM</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>MSKS</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MSKD</td><td>闹钟日期位域屏蔽位0:不屏蔽日期/天位域1:屏蔽日期/天位域</td></tr><tr><td>30</td><td>DOWS</td><td>星期选择0:此时 DAYU[3:0] 代表日期个位值1:此时 DAYU[3:0] 代表星期几,此时 DAYT[1:0]无意义</td></tr><tr><td>29:28</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码格式存储</td></tr><tr><td>27:24</td><td>DAYU[3:0]</td><td>日期个位值或星期天数,以 BCD 码格式存储</td></tr><tr><td>23</td><td>MSKH</td><td>闹钟小时位域屏蔽位0:不屏蔽小时位域1:屏蔽小时位域</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0:AM 或 24 小时制1:PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>MSKM</td><td>闹钟分钟位域屏蔽位0:不屏蔽分钟位域1:屏蔽分钟位域</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>MSKS</td><td>闹钟秒位域屏蔽位0:不屏蔽秒位域1:屏蔽秒位域</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.9. 写保护钥匙寄存器（RTC_WPK）

偏移地址：0x24

复位值：0x0000 0000


该寄存器只能按字(32位)访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">WPK[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>WPK[7:0]</td><td>写保护的解锁值</td></tr></table>

## 22.4.10. 亚秒寄存器（RTC_SS）

偏移地址：0x28

系统复位值：当BPSHAD = 0，0x0000 0000。

当BPSHAD = 1，无影响。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值</td></tr><tr><td></td><td></td><td>该位值是同步预分频计数器的值。秒的小数部分由下面公式给出:秒的小数部分 = (FACTOR_S - SSC)/(FACTOR_S + 1)</td></tr></table>

## 22.4.11. 移位控制寄存器（RTC_SHIFTCTL）

偏移地址：0x2C

系统复位：无影响

备份域复位值：0x0000 0000

写保护寄存器，仅当SOPF=0，该寄存器可写。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>A1S</td><td colspan="15">保留</td></tr><tr><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SFS[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>A1S</td><td>增加一秒0:无影响1:增加一秒到时钟/日历该位与SFS位一起使用,增加小于一秒到当前时间。</td></tr><tr><td>30:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>SFS[14:0]</td><td>减去小于一秒的一段时间这位的值将增加到同步预分频计数器当仅用SFS时,由于同步预分频器是一个递减计数器,所以时钟将会延迟。延迟(秒)=SFS/(FACTOR_S+1)当A1S和SFS一起使用时,时钟将会提前提前(秒)=(1-(SFS/(FACTOR_S+1)))</td></tr></table>


注意：写入此寄存器会导致 RSYNF 位被清 0。


## 22.4.12. 时间戳时间寄存器（RTC_TTS）

偏移地址：0x30

备份域复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td colspan="2">r</td><td colspan="4">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td></td><td colspan="3">r</td><td colspan="4">r</td><td></td><td colspan="3">r</td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标记0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.13. 时间戳日期寄存器（RTC_DTS）

偏移地址：0x34

备份域复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历日期。

清除TSF位也会清除此寄存器。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td colspan="2">MONT</td><td colspan="3">MONU[3:0]</td><td colspan="2">保留</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td></tr><tr><td colspan="3">r</td><td colspan="2">r</td><td colspan="3">r</td><td colspan="4">r</td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期数</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[3:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:5</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>4:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 22.4.14. 时间戳亚秒寄存器（RTC_SSTS）

偏移地址：0x38

备份域复位：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值</td></tr></table>


TSF 置 1 时记录当时的同步预分频计数器的值。


## 22.4.15. 高精度频率补偿寄存器（RTC_HRFC）

偏移地址：0x3C

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FREQI</td><td>CWND8</td><td>CWND16</td><td colspan="4">保留</td><td colspan="9">CMSK[8:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>FREQI</td><td>RTC频率增加488.5ppm0:无影响1:每<eq>2^{11}</eq>个脉冲增加一个RTCCLK脉冲该位需与CMSK位一起使用。如果输入时钟频率是32.768KHz,在32s校准窗期间,增加的RTCCLK脉冲数是(512* FREQI)- CMSK</td></tr><tr><td>14</td><td>CWND8</td><td>采用8秒校准周期0:无影响1:采用8秒校准周期注意:当CWND8=1,CMSK[1:0]被锁定在“00”。</td></tr><tr><td>13</td><td>CWND16</td><td>采用16秒校准周期0:无影响1:采用16秒校准周期注意:当CWND16=1,CMSK[0]被锁定在“0”.</td></tr><tr><td>12:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>CMSK[8:0]</td><td>校准周期RTCCLK脉冲屏蔽数在<eq>2^{20}</eq>个RTCCLK脉冲之内屏蔽的脉冲数此项功能可以以0.9537 ppm的分辨率来降低日历频率</td></tr></table>

## 22.4.16. 侵入寄存器（RTC_TAMP）

偏移地址：0x40

备份域复位：0x0000 0000

系统复位：无影响

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>TP2IE</td><td>TP1IE</td><td>TP0IE</td><td>保留</td><td>TP2MASK</td><td>TP1MASK</td><td>TP0MASK</td><td>保留</td><td>TP2NOERASE</td><td>TP1NOERASE</td><td>TP0NOERASE</td><td colspan="2">保留</td><td>TP2_DISPIN</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DISPU</td><td colspan="2">PRCH[1:0]</td><td colspan="2">FLT[1:0]</td><td colspan="3">FREQ[2:0]s</td><td>TPTS</td><td>TP2EG</td><td>TP2EN</td><td>TP1EG</td><td>TP1EN</td><td>TPIE</td><td>TP0EG</td><td>TP0EN</td></tr><tr><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>Bits</td><td>Fields</td><td>Descriptions</td></tr><tr><td>31:30</td><td>保留</td><td>Must be kept at reset value.</td></tr><tr><td>29</td><td>TP2IE</td><td>Tamper 2 中断使能0: 禁用侵入 2 中断1: 启用侵入 2 中断</td></tr><tr><td>28</td><td>TP1IE</td><td>Tamper 1 中断使能0: 禁用 Tamper 1 中断1: 启用 Tamper 1 中断</td></tr><tr><td>27</td><td>TP0IE</td><td>侵入 0 中断使能0: 禁用 Tamper 0 中断1: 启用 Tamper 0 中断</td></tr><tr><td>26</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>25</td><td>TP2MASK</td><td>Tamper 2 掩码标志0: Tamper 2事件产生一个触发事件,TP2F必须被软件清除,以允许下一个侵入事件检测1: Tamper 2 事件产生一个触发事件,TP2F 被硬件屏蔽并在内部清除。备份寄存器不会被清除Note: 当 TP2MASK 被置位时,必须禁用 Tamper 2 中断</td></tr><tr><td>24</td><td>TP1MASK</td><td>Tamper1 掩码标志0: Tamper1事件产生一个触发事件,TP2F必须被软件清除,以允许下一个侵入事件检测1: Tamper1 事件产生一个触发事件,TP2F 被硬件屏蔽并在内部清除。备份寄存器不会被清除Note: 当 TP2MASK 被置位时,必须禁用 Tamper 1 中断</td></tr><tr><td>23</td><td>TP0MASK</td><td>Tamper0 掩码标志0: Tamper0事件产生一个触发事件,TP2F必须被软件清除,以允许下一个侵入事件检测1: Tamper0 事件产生一个触发事件,TP2F 被硬件屏蔽并在内部清除。备份寄存器不会被清除Note: 当 TP2MASK 被置位时,必须禁用 Tamper 0 中断</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>21</td><td>TP2 NOERASE</td><td>Tamper2 不擦除0: Tamper2 擦除备份寄存器1: Tamper2 不擦除备份寄存器</td></tr><tr><td>20</td><td>TP1 NOERASE</td><td>Tamper1 不擦除0: Tamper1 擦除备份寄存器1: Tamper1 不擦除备份寄存器</td></tr><tr><td>19</td><td>TP0 NOERASE</td><td>Tamper0 不擦除0: Tamper0 擦除备份寄存器1: Tamper0 不擦除备份寄存器</td></tr><tr><td>18:17</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>16</td><td>TP2_DISPIN</td><td>Tamper2 选择0: 引脚触发 Tamper21: 引脚不触发 Tamper2</td></tr><tr><td>15</td><td>DISPU</td><td>RTC_TAMPx 上拉禁用位0: 使能内部 RTC_TAMPx 引脚上的上拉电阻并在采样前进行预充电1: 禁用预充电功能</td></tr><tr><td>14:13</td><td>PRCH[1:0]</td><td>RTC_TAMPx 的预充电时间该位设置决定了每次采样前的预充电时间0x0: 1 个 RTC 时钟0x1: 2 个 RTC 时钟0x2: 4 个 RTC 时钟0x3: 8 个 RTC 时钟</td></tr><tr><td>12:11</td><td>FLT[1:0]</td><td>RTC_TAMPx 过滤器计数设置该位决定了侵入事件检测模式和在电平检测模式下连续采样的次数。0x0: 用边沿模式检测侵入事件, 预充电功能被自动禁用。0x1: 用电平模式检测侵入事件。连续采样到 2 个有效电平时认为发生侵入事件0x2: 用电平模式检测侵入事件。连续采样到 4 个有效电平时认为发生侵入事件0x3: 用电平模式检测侵入事件。连续采样到 8 个有效电平时认为发生侵入事件</td></tr><tr><td>10:8</td><td>FREQ[2:0]</td><td>侵入事件电平模式检测的采样频率0x0: 每次采样间隔 32768 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 1Hz)0x1: 每次采样间隔 16384 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 2Hz)0x2: 每次采样间隔 8192 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 4Hz)0x3: 每次采样间隔 4096 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 8Hz)0x4: 每次采样间隔 2048 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 16Hz)0x5: 每次采样间隔 1024 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 32Hz)0x6: 每次采样间隔 512 个 RTCCLK(若 RTCCLK=32.768KHz, 频率为 64Hz)</td></tr></table>
位域只读。

当通道 2 配置为输出模式时，这些位包含了即将和计数器比较的值。使能相应的影子寄存器后，影子寄存器值随每次更新事件更新。

当 PWMADMEN = 0 时，CH2VAL[15:0]位域值表示比较值。

当 PWMADMEN = 1 时，CH2VAL[15:0]用于表示比较值的整数部分。

## 22.4.17. 闹钟 0 亚秒寄存器（RTC_ALRM0SS）

偏移地址： 0x44

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器，仅当ALRM0EN=0或INITM=1，可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">MSKSSC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SSC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>MSKSSC[3:0]</td><td>亚秒位域的屏蔽控制位0x0:屏蔽闹钟亚秒设置。当所有其他的闹钟位域匹配的时候,闹钟将会在每一秒钟到达的时刻置1。0x1:SSC[0]位用于时间匹配,其他位被忽略。0x2:SSC[1:0]位用于时间匹配,其他位被忽略。0x3:SSC[2:0]位用于时间匹配,其他位被忽略。0x4:SSC[3:0]位用于时间匹配,其他位被忽略。0x5:SSC[4:0]位用于时间匹配,其他位被忽略。0x6:SSC[5:0]位用于时间匹配,其他位被忽略。0x7:SSC[6:0]位用于时间匹配,其他位被忽略。0x8:SSC[7:0]位用于时间匹配,其他位被忽略。0x9:SSC[8:0]位用于时间匹配,其他位被忽略。0xA:SSC[9:0]位用于时间匹配,其他位被忽略。0xB:SSC[10:0]位用于时间匹配,其他位被忽略。0xC:SSC[11:0]位用于时间匹配,其他位被忽略。0xD:SSC[12:0]位用于时间匹配,其他位被忽略。0xE:SSC[13:0]位用于时间匹配,其他位被忽略。0xF:SSC[14:0]位用于时间匹配,其他位被忽略。注意:同步预分频计数器的第15位(RTC_SS寄存器中的SSC[15])从不被匹配。</td></tr><tr><td>23:15</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>14:0</td><td>SSC[14:0]</td><td>闹钟亚秒值该值为闹钟亚秒值,用于与同步预分频计数器匹配。匹配位数由MSKSSC位控制。</td></tr></table>

## 22.4.18. 闹钟 1 亚秒寄存器（RTC_ALRM1SS）

偏移地址：0x48

备份域复位：0x0000 0000

系统复位：无影响

写保护寄存器，仅当 ALRM1EN=0 或 INITM=1，可以进行写操作。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">MSKSSC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SSC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>MSKSSC[3:0]</td><td>亚秒位域的屏蔽控制位0x0:屏蔽闹钟亚秒设置。当所有其他的闹钟位域匹配的时候,闹钟将会在每一秒钟到达的时刻置1。0x1:SSC[0]位用于时间匹配,其他位被忽略。0x2:SSC[1:0]位用于时间匹配,其他位被忽略。0x3:SSC[2:0]位用于时间匹配,其他位被忽略。0x4:SSC[3:0]位用于时间匹配,其他位被忽略。0x5:SSC[4:0]位用于时间匹配,其他位被忽略。0x6:SSC[5:0]位用于时间匹配,其他位被忽略。0x7:SSC[6:0]位用于时间匹配,其他位被忽略。0x8:SSC[7:0]位用于时间匹配,其他位被忽略。0x9:SSC[8:0]位用于时间匹配,其他位被忽略。0xA:SSC[9:0]位用于时间匹配,其他位被忽略。0xB:SSC[10:0]位用于时间匹配,其他位被忽略。0xC:SSC[11:0]位用于时间匹配,其他位被忽略。0xD:SSC[12:0]位用于时间匹配,其他位被忽略。0xE:SSC[13:0]位用于时间匹配,其他位被忽略。0xF:SSC[14:0]位用于时间匹配,其他位被忽略。注意:同步预分频计数器的第15位(RTC_SS寄存器中的SSC[15])从不被匹配。</td></tr><tr><td>23:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>SSC[14:0]</td><td>闹钟亚秒值该值为闹钟亚秒值,用于与同步预分频计数器匹配。匹配位数由MSKSSC位控制。</td></tr></table>

## 22.4.19. 配置寄存器（RTC_CFG）

偏移地址：0x4C

备份域复位：0x0000 0000

系统复位：无影响

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>OUT2EN</td><td>ALRMOU TTYPE</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OUT2EN</td><td>RTC_OUT 引脚选择0: RTC_OUT 输出到 PC131: RTC_OUT 输出到 PB2</td></tr><tr><td>0</td><td>ALRMOUTTYPE</td><td>RTC_ALARM 输出类型0: 开漏输出1: 推挽输出</td></tr></table>

## 22.4.20. 备份寄存器（RTC_BKPx）（x=0..31）

偏移地址： 0x50 到 0xCC

备份域复位：0x0000 0000

系统复位：无影响

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td colspan="3">DATA[15:0]</td></tr><tr><td colspan="3">rw</td></tr><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>数据软件可读写寄存器。由于此寄存器可由<eq>V_{BAT}</eq>供电,因此寄存器值在省电模式下依然保持有效。当侵入检测标志位TPxF置1,这些寄存器会被复位。当FMC读保护功能禁用时,这些寄存器会被复位。</td></tr></table>
