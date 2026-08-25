## 13.4. RTC 寄存器

RTC基地址：0x4000 2800

## 13.4.1. 时间寄存器（RTC_TIME）

偏移地址：0x00

系统复位值：当BPSHAD = 0，0x0000 0000

当BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td colspan="9"></td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td></td><td colspan="3">rw</td><td colspan="4">rw</td><td></td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 13.4.2. 日期寄存器（RTC_DATE）

偏移地址：0x04

系统复位值：当 BPSHAD = 0，0x0000 2101

当 BPSHAD = 1，无影响

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="4">YRT[3:0]</td><td colspan="4">YRU[3:0]</td></tr><tr><td colspan="8"></td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td>MONT</td><td colspan="4">MONU[2:0]</td><td colspan="2">保留</td><td colspan="2">DAYT</td><td colspan="4">DAYU</td></tr><tr><td colspan="3">rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:20</td><td>YRT[3:0]</td><td>年份十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>YRU[3:0]</td><td>年份个位值,以 BCD 码形式存储</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期0x0: 保留0x1: 星期一...0x7: 星期日</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[2:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 13.4.3. 控制寄存器（RTC_CTL）

偏移地址：0x08

系统复位：无影响

备份寄存器复位值：0x0000 0000

写保护寄存器

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>OUT1EN</td><td colspan="7">保留</td><td>COEN</td><td colspan="2">OS[1:0]</td><td>OPOL</td><td>COS</td><td>DSM</td><td>S1H</td><td>A1H</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TSIE</td><td colspan="2">保留</td><td>ALRM0IE</td><td>TSEN</td><td colspan="2">保留</td><td>ALRM0EN</td><td>保留</td><td>CS</td><td>BPSHAD</td><td>REFEN</td><td>TSEG</td><td colspan="3">保留</td></tr><tr><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>OUT1EN</td><td>RTC_OUT 引脚选择0: RTC_OUT1 输出失能1: RTC_OUT1 输出使能</td></tr></table>

<table><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>COEN</td><td>校准输出使能0:关闭校准输出1:使能校准输出</td></tr><tr><td>22:21</td><td>OS[1:0]</td><td>输出选择该位用来选择输出的标志源。0x00:禁用RTC_ALARM输出0x01:启用闹钟0标志输出</td></tr><tr><td>20</td><td>OPOL</td><td>输出极性该位用来反转RTC_ALARM输出。0:禁用反转RTC_ALARM输出1:启用反转RTC_ALARM输出</td></tr><tr><td>19</td><td>COS</td><td>校准输出选择仅当COEN=1并且预分频器是默认值时有效。0:校准输出是512Hz1:校准输出是1Hz</td></tr><tr><td>18</td><td>DSM</td><td>夏令时屏蔽位该位可以通过软件灵活使用。常用来记录夏令时调整。</td></tr><tr><td>17</td><td>S1H</td><td>减1小时(冬季时间变化)当前时间非零的情况下,将当前时间减去一个小时。0:没有影响1:在下一个秒改变时,将减少一个小时</td></tr><tr><td>16</td><td>A1H</td><td>增加1小时(夏季时间变化)将当前时间增加一个小时。0:没有影响1:在下一个秒改变时,将增加一个小时</td></tr><tr><td>15</td><td>TSIE</td><td>时间戳中断使能0:禁用时间戳中断1:启用时间戳中断</td></tr><tr><td>14:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>ALRM0IE</td><td>RTC闹钟0中断使能0:禁用闹钟中断1:启用闹钟中断</td></tr><tr><td>11</td><td>TSEN</td><td>时间戳功能使能0:禁用时间戳功能1:启用时间戳功能</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>ALRM0EN</td><td>闹钟0功能使能</td></tr></table>

<table><tr><td></td><td></td><td>0:禁用闹钟功能1:启用闹钟功能</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CS</td><td>时间格式0:24小时制1:12小时制注意:仅能在初始化状态进行写入</td></tr><tr><td>5</td><td>BPSHAD</td><td>禁止影子寄存器0:读取的日历的值来自影子日历寄存器1:读取的日历的值来自真正日历寄存器注意:如果APB时钟的频率小于RTCCLK频率的7倍,该位必须设为1</td></tr><tr><td>4</td><td>REFEN</td><td>参考时钟检测功能使能0:禁用参考时钟检测功能1:启用参考时钟检测功能注意:仅能在初始化状态进行写入并且FACTOR_S必须为0x00FF</td></tr><tr><td>3</td><td>TSEG</td><td>时间戳事件有效检测边沿0:上升沿是时间戳事件有效检测沿1:下降沿是时间戳事件有效检测沿</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 13.4.4. 状态寄存器（RTC_STAT）

偏移地址：0x0C

系统复位：仅INITM，INITF和RSYNF位被置0，其他位无影响。

备份寄存器复位值：0x0000 0007

写保护寄存器

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>SCPF</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>TSOVRF</td><td>TSF</td><td colspan="2">保留</td><td>ALRM0F</td><td>INITM</td><td>INITF</td><td>RSYNF</td><td>YCM</td><td>SOPF</td><td colspan="2">保留</td><td>ALRM0WF</td></tr><tr><td colspan="3"></td><td>rc_w0</td><td>rc_w0</td><td colspan="2"></td><td>rc_w0</td><td>rw</td><td>r</td><td>rc_w0</td><td>r</td><td>r</td><td colspan="2"></td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>SCPF</td><td>平滑校准挂起标志在未进入初始化模式时向RTC_HRFC进行软件写操作,该位被硬件置1。当平滑校准设置开始执行后,该位被硬件清零0。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>TSOVRF</td><td>时间戳事件溢出标志如果 TSF 位已经置位,当再次检测到时间戳事件时,该位会通过硬件置 1。可以通过向该位软件写 0 来清除。</td></tr><tr><td>11</td><td>TSF</td><td>时间戳事件标志当检测到一个时间戳事件时,该位会通过硬件置 1。可以通过向该位软件写 0 来清除。</td></tr><tr><td>10:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>ALRM0F</td><td>Alarm0 发生标志当现在的时间/日期与闹钟 0 设置的时间/日期匹配的时候,该位会通过硬件置 1。可以通过向该位软件写 0 来清除。</td></tr><tr><td>7</td><td>INITM</td><td>进入初始化模式0:自由运行模式1:进入初始化模式设置时间/日期和预分频,计数器将停止运行</td></tr><tr><td>6</td><td>INITF</td><td>初始化状态标志该位被硬件置 1,初始化状态时可以设置日历寄存器和预分频器。0:日历寄存器和预分频器的值不能改变1:日历寄存器和预分频器的值可以改变</td></tr><tr><td>5</td><td>RSYNF</td><td>寄存器同步标志每 2 个 RTCCLK 将会由硬件置 1 一次,同时会复制当前日历时间/日期到影子日历寄存器。初始化模式(INITM),移位操作挂起标志(SOPF)或者禁止影子寄存器模式(BPSHAD = 1)会清除该位。该位也可以通过软件写 0 清除。0:影子寄存器未同步1:影子寄存器已同步</td></tr><tr><td>4</td><td>YCM</td><td>年份配置标志当日历寄存器的年份值不为 0 时硬件置 10:日历尚未初始化1:日历已经初始化</td></tr><tr><td>3</td><td>SOPF</td><td>移位功能操作挂起标志0:移位操作没有挂起1:移位操作挂起</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>ALRM0WF</td><td>Alarm0 配置可写标志硬件置位和清零。ALRM0EN=0 时,标记 alarm 是否可写。0:不允许修改 Alarm 寄存器设置1:允许修改 Alarm 寄存器设置</td></tr></table>

## 13.4.5. 预分频寄存器（RTC_PSC）

偏移地址：0x10

系统复位：无影响

备份寄存器复位值：0x007F 00FF

写保护寄存器，仅在初始化状态可以进行写操作。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td colspan="7">FACTOR_A[6:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">FACTOR_S[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22:16</td><td>FACTOR_A[6:0]</td><td>异步预分频系数ck_apre频率 = RTCCLK 频率/(FACTOR_A+1)</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>FACTOR_S[14:0]</td><td>同步预分频系数ck_spre频率 = ck_apre 频率/(FACTOR_S+1)</td></tr></table>

## 13.4.6. 闹钟 0 时间日期寄存器（RTC_ALRM0TD）

偏移地址：0x1C

系统复位：无影响

备份寄存器复位值：0x0000 0000

写保护寄存器，仅在初始化状态可以进行写操作或者ALRM0WF为1。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>MSKD</td><td>DOWS</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td><td>MSKH</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MSKM</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>MSKS</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr><tr><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>MSKD</td><td>闹钟日期位域屏蔽位0:不屏蔽日期/天位域1:屏蔽日期/天位域</td></tr><tr><td>30</td><td>DOWS</td><td>星期选择0: 此时 DAYU[3: 0]代表日期个位值1: 此时 DAYU[3: 0]代表星期几,此时 DAYT[1: 0]无意义</td></tr><tr><td>29:28</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码格式存储</td></tr><tr><td>27:24</td><td>DAYU[3:0]</td><td>日期个位值或星期天数,以 BCD 码格式存储</td></tr><tr><td>23</td><td>MSKH</td><td>闹钟小时位域屏蔽位0: 不屏蔽小时位域1: 屏蔽小时位域</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标志0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>MSKM</td><td>闹钟分钟位域屏蔽位0: 不屏蔽分钟位域1: 屏蔽分钟位域</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>MSKS</td><td>闹钟秒位域屏蔽位0: 不屏蔽秒位域1: 屏蔽秒位域</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 13.4.7. 写保护钥匙寄存器（RTC_WPK）

偏移地址：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">WPK[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr></table>

7:0 WPK[7:0] 写保护的解锁值

## 13.4.8. 亚秒寄存器（RTC_SS）

偏移地址：0x28

系统复位值：当BPSHAD = 0，0x0000 0000。

当BPSHAD = 1，无影响。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值该位值是同步预分频计数器的值。秒的小数部分由下面公式给出:秒的小数部分 = (FACTOR_S - SSC) / (FACTOR_S + 1)</td></tr></table>

## 13.4.9. 移位控制寄存器（RTC_SHIFTCTL）

偏移地址：0x2C

系统复位：无影响

备份寄存器复位值：0x0000 0000

写保护寄存器，仅当SOPF=0，该寄存器可写。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>A1S</td><td colspan="15">保留</td></tr><tr><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SFS[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>A1S</td><td>增加一秒0:无影响1:增加一秒到时钟/日历该位与SFS位一起使用,增加小于一秒到当前时间。</td></tr><tr><td>30:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:0</td><td>SFS[14:0]</td><td>减去小于一秒的一段时间</td></tr></table>

这位的值将增加到同步预分频计数器

当仅用 SFS 时，由于同步预分频器是一个递减计数器，所以时钟将会延迟。

延迟（秒）= SFS/（FACTOR_S + 1）

当 A1S 和 SFS 一起使用时，时钟将会提前

提前（秒）=（1 -（SFS/（FACTOR_S + 1）））

注意：写入此寄存器会导致 RSYNF 位被清 0。

## 13.4.10. 时间戳时间寄存器（RTC_TTS）

偏移地址：0x30

备份寄存器复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td>PM</td><td colspan="2">HRT[1:0]</td><td colspan="4">HRU[3:0]</td></tr><tr><td colspan="9"></td><td>r</td><td colspan="2">r</td><td colspan="4">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="3">MNT[2:0]</td><td colspan="4">MNU[3:0]</td><td>保留</td><td colspan="3">SCT[2:0]</td><td colspan="4">SCU[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PM</td><td>AM/PM 标记0: AM 或 24 小时制1: PM</td></tr><tr><td>21:20</td><td>HRT[1:0]</td><td>小时十位值,以 BCD 码形式存储</td></tr><tr><td>19:16</td><td>HRU[3:0]</td><td>小时个位值,以 BCD 码形式存储</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:12</td><td>MNT[2:0]</td><td>分钟十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MNU[3:0]</td><td>分钟个位值,以 BCD 码形式存储</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>SCT[2:0]</td><td>秒钟十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>SCU[3:0]</td><td>秒钟个位值,以 BCD 码形式存储</td></tr></table>

## 13.4.11. 时间戳日期寄存器（RTC_DTS）

偏移地址：0x34

备份寄存器复位值：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历日期。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">DOW[2:0]</td><td>MONT</td><td colspan="4">MONU[3:0]</td><td colspan="2">保留</td><td colspan="2">DAYT[1:0]</td><td colspan="4">DAYU[3:0]</td></tr><tr><td colspan="3">r</td><td>r</td><td colspan="6">r</td><td colspan="2">r</td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:13</td><td>DOW[2:0]</td><td>星期数</td></tr><tr><td>12</td><td>MONT</td><td>月份十位值,以 BCD 码形式存储</td></tr><tr><td>11:8</td><td>MONU[3:0]</td><td>月份个位值,以 BCD 码形式存储</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DAYT[1:0]</td><td>日期十位值,以 BCD 码形式存储</td></tr><tr><td>3:0</td><td>DAYU[3:0]</td><td>日期个位值,以 BCD 码形式存储</td></tr></table>

## 13.4.12. 时间戳亚秒寄存器（RTC_SSTS）

偏移地址：0x38

备份寄存器复位：0x0000 0000

系统复位：无影响

当TSF被置1，该位用来记录日历时间。

清除TSF位也会清除此寄存器。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SSC[15:0]</td><td>亚秒值</td></tr></table>

TSF 置 1 时记录当时的同步预分频计数器的值。

## 13.4.13. 高精度频率补偿寄存器（RTC_HRFC）

偏移地址：0x3C

备份寄存器复位：0x0000 0000

系统复位：无影响

写保护寄存器。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FREQI</td><td>CWND8</td><td>CWND16</td><td colspan="4">保留</td><td colspan="9">CMSK[8:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>FREQI</td><td>RTC频率增加488.5ppm0:无影响1:每<eq>2^{11}</eq>个脉冲增加一个RTCCLK脉冲该位需与CMSK位一起使用。如果输入时钟频率是32.768KHz,在32s校准窗期间,增加的RTCCLK脉冲数是(512* FREQI)- CMSK</td></tr><tr><td>14</td><td>CWND8</td><td>采用8秒校准周期0:无影响1:采用8秒校准周期注意:当CWND8=1,CMSK[1:0]被锁定在“00”。</td></tr><tr><td>13</td><td>CWND16</td><td>采用16秒校准周期0:无影响1:采用16秒校准周期注意:当CWND16=1,CMSK[0]被锁定在“0”.</td></tr><tr><td>12:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8:0</td><td>CMSK[8:0]</td><td>校准周期RTCCLK脉冲屏蔽数在<eq>2^{20}</eq>个RTCCLK脉冲之内屏蔽的脉冲数此项功能可以以0.9537 ppm的分辨率来降低日历频率</td></tr></table>

## 13.4.14. 类型寄存器（RTC_TYPE）

偏移地址：0x40

备份寄存器复位：0x0000 0000

系统复位：无影响

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>ALRMOUTTYPE</td><td colspan="2">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DISPU</td><td colspan="15">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>ALRMOUTTYPE</td><td>RTC_ALARM 输出类型0:开漏输出1:推挽输出</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>DISPU</td><td>RTC_ALRM 上拉禁用位0:RTC_ALRM 无输出上拉1:RTC_ALRM 输出上拉</td></tr><tr><td>14:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 13.4.15. 闹钟 0 亚秒寄存器（RTC_ALRM0SS）

偏移地址： 0x44

备份寄存器复位：0x0000 0000

系统复位：无影响

写保护寄存器，仅当ALRM0EN=0或INITM=1，可以进行写操作。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="4">MSKSSC[3:0]</td><td colspan="8">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="15">SSC[14:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>MSKSSC[3:0]</td><td>亚秒位域的屏蔽控制位0x0:屏蔽闹钟亚秒设置。当所有其他的闹钟位域匹配的时候,闹钟将会在每一秒钟到达的时刻置1。0x1:SSC[0]位用于时间匹配,其他位被忽略。0x2:SSC[1:0]位用于时间匹配,其他位被忽略。0x3:SSC[2:0]位用于时间匹配,其他位被忽略。0x4:SSC[3:0]位用于时间匹配,其他位被忽略。0x5:SSC[4:0]位用于时间匹配,其他位被忽略。</td></tr></table>

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

23:15 保留 必须保持复位值。

14:0 SSC[14:0] 闹钟亚秒值

## 13.4.16. 备份寄存器（RTC_BKPx）（x=0..3）

偏移地址：0x50 到 0x5c

备份寄存器复位：0x0000 0000

系统复位：无影响

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:0</td><td>DATA[15:0]</td><td>数据软件可读写寄存器。寄存器值在省电模式下依然保持有效。</td></tr></table>
