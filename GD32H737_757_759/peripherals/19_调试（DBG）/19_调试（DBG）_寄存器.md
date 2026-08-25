# 19.4. DBG 寄存器

DBG 基地址：0xE00E1000

# 19.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

只读寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 ID_CODE[31:0] DBG ID 寄存器

这些位由软件读取，这些位是不变的常数

# 19.4.2. 控制寄存器 0（DBG_CTL0）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>TRACECLKEN</td><td colspan="2">TRACE_MODE[1:0]</td><td colspan="2">保留</td></tr></table>

rw rw 

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr></table>

rw rw rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:21 保留 必须保持复位值。

20 TRACECLKEN 跟踪时钟使能

0: 跟踪时钟失能

1: 跟踪时钟使能。

<table><tr><td>19:18</td><td>TRACE_MODE[1:0]</td><td>跟踪引脚分配模式</td></tr><tr><td></td><td></td><td>该位由软件置位和复位</td></tr><tr><td></td><td></td><td>00: 跟踪引脚用于异步模式</td></tr></table>

<table><tr><td></td><td></td><td>01: 跟踪引脚用于同步模式且数据长度为1</td></tr><tr><td></td><td></td><td>10: 跟踪引脚用于同步模式且数据长度为2</td></tr><tr><td></td><td></td><td>11: 跟踪引脚用于同步模式且数据长度为4。</td></tr><tr><td>17:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位</td></tr><tr><td></td><td></td><td>该位由软件置位和复位</td></tr><tr><td></td><td></td><td>0: 无影响</td></tr><tr><td></td><td></td><td>1: 在待机模式下,所有工作的时钟继续运行,支持待机模式下调试。</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持</td></tr><tr><td></td><td></td><td>该位由软件置位和复位</td></tr><tr><td></td><td></td><td>0: 无影响</td></tr><tr><td></td><td></td><td>1: 在深度睡眠模式下,所有工作的时钟继续运行,支持深度睡眠模式下调试。</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持位</td></tr><tr><td></td><td></td><td>该位由软件置位和复位</td></tr><tr><td></td><td></td><td>0: 无影响</td></tr><tr><td></td><td></td><td>1: 在睡眠模式下,所有工作时钟继续运行,支持睡眠模式下调试。</td></tr></table>

# 19.4.3. 控制寄存器 1（DBG_CTL1）

地址偏移：0x34

复位值： 0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>WWDGT_HOLD</td><td colspan="6">保留</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>WWDGT_HOLD</td><td>WWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试。</td></tr><tr><td>5:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 19.4.4. 控制寄存器 2（DBG_CTL2）

地址偏移：0x3C

复位值： 0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>I2C3_HOLD</td><td>I2C2_HOLD</td><td>I2C1_HOLD</td><td>I2C0_HOLD</td><td colspan="5">保留</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>TIMER51_HOLD</td><td>TIMER50_HOLD</td><td>TIMER31_HOLD</td><td>TIMER30_HOLD</td><td>TIMER23_HOLD</td><td>TIMER22_HOLD</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td>TIMER4_HOLD</td><td>TIMER3_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>I2C3_HOLD</td><td>I2C3 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C3 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>23</td><td>I2C2_HOLD</td><td>I2C2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>22</td><td>I2C1_HOLD</td><td>I2C1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C1 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>21</td><td>I2C0_HOLD</td><td>I2C0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>20:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>TIMER51_HOLD</td><td>TIMER51 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 51 计数器不变,用于调试。</td></tr><tr><td>10</td><td>TIMER50_HOLD</td><td>TIMER50 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 50 计数器不变,用于调试。</td></tr></table>

<table><tr><td>9</td><td>TIMER31_HOLD</td><td>TIMER31 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器31计数器不变,用于调试。</td></tr><tr><td>8</td><td>TIMER30_HOLD</td><td>TIMER30 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器30计数器不变,用于调试。</td></tr><tr><td>7</td><td>TIMER23_HOLD</td><td>TIMER 23 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器23计数器不变,用于调试。</td></tr><tr><td>6</td><td>TIMER22_HOLD</td><td>TIMER 22 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器22计数器不变,用于调试。</td></tr><tr><td>5</td><td>TIMER6_HOLD</td><td>TIMER 6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器6计数器不变,用于调试。</td></tr><tr><td>4</td><td>TIMER5_HOLD</td><td>TIMER 5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器5计数器不变,用于调试。</td></tr><tr><td>3</td><td>TIMER4_HOLD</td><td>TIMER 4 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器4计数器不变,用于调试。</td></tr><tr><td>2</td><td>TIMER3_HOLD</td><td>TIMER 3 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器3计数器不变,用于调试。</td></tr><tr><td>1</td><td>TIMER2_HOLD</td><td>TIMER 2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器2计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER1_HOLD</td><td>TIMER 1 保持位该位由软件置位和复位0:无影响</td></tr></table>

1: 当内核停止时保持定时器 1 计数器不变，用于调试。

# 19.4.5. 控制寄存器 3（DBG_CTL3）

地址偏移：0x4C

复位值： 0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>TIMER44_HOLD</td><td>TIMER43_HOLD</td><td>TIMER42_HOLD</td><td>TIMER41_HOLD</td><td>TIMER40_HOLD</td><td>TIMER16_HOLD</td><td>TIMER15_HOLD</td><td>TIMER14_HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>CAN2_HOLD</td><td>CAN1_HOLD</td><td>CAN0_HOLD</td><td>TIMER7_HOLD</td><td>TIMER0_HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TIMER44_HOLD</td><td>TIMER44 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器44计数器不变,用于调试。</td></tr><tr><td>22</td><td>TIMER43_HOLD</td><td>TIMER43 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器43计数器不变,用于调试。</td></tr><tr><td>21</td><td>TIMER42_HOLD</td><td>TIMER42 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器42计数器不变,用于调试。</td></tr><tr><td>20</td><td>TIMER41_HOLD</td><td>TIMER41 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器41计数器不变,用于调试。</td></tr><tr><td>19</td><td>TIMER40_HOLD</td><td>TIMER40 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器40计数器不变,用于调试。</td></tr><tr><td>18</td><td>TIMER16_HOLD</td><td>TIMER16 保持位该位由软件置位和复位0:无影响</td></tr></table>

<table><tr><td></td><td></td><td>1: 当内核停止时保持定时器 16 计数器不变,用于调试。</td></tr><tr><td>17</td><td>TIMER15_HOLD</td><td>TIMER15 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 15 计数器不变,用于调试。</td></tr><tr><td>16</td><td>TIMER14_HOLD</td><td>TIMER14 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 14 计数器不变,用于调试。</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>CAN2_HOLD</td><td>CAN2 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN2 接收寄存器停止接收数据。</td></tr><tr><td>3</td><td>CAN1_HOLD</td><td>CAN1 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN1 接收寄存器停止接收数据。</td></tr><tr><td>2</td><td>CAN0_HOLD</td><td>CAN0 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN0 接收寄存器停止接收数据。</td></tr><tr><td>1</td><td>TIMER7_HOLD</td><td>TIMER7 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 7 计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER0_HOLD</td><td>TIMER0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 0 计数器不变,用于调试。</td></tr></table>

# 19.4.6. 控制寄存器 4（DBG_CTL4）

地址偏移：0x54

复位值： 0x0000 0000

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13"></td><td>FWDGT_HOLD</td><td>保留</td><td>RTC_HOLD</td></tr></table>

rw rw 

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>FWDGT_HOLD</td><td>FWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 FWDGT 计数器时钟,用于调试。</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>RTC_HOLD</td><td>RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试。</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
