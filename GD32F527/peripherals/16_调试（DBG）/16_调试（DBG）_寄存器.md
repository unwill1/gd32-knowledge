## 16.4. DBG 寄存器

DBG 基地址：0xE004 4000U

## 16.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

只读寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器</td></tr></table>


这些位由软件读取，这些位是不变的常数


## 16.4.2. 控制寄存器 0（DBG_CTL0）

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>TRACE_IOEN</td><td colspan="2">保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TRACE_IOEN</td><td>跟踪引脚分配使能该位由软件置位和复位0:跟踪引脚分配禁用1:跟踪引脚分配使能。</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位0:无影响1:在待机模式下,系统时钟和AHB时钟由CK_IRC16M提供,当退出待机模式时,产生系统复位。</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持位该位由软件置位和复位0:无影响1:在深度睡眠模式下,系统时钟和AHB时钟由CK_IRC16M提供。</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持位该位由软件置位和复位0:无影响1:在睡眠模式下,AHB时钟继续运行。</td></tr></table>

## 16.4.3. 控制寄存器 1（DBG_CTL1）

地址偏移：0x08

复位值： 0x0000 0000，仅上电复位


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>CAN1_HOLD</td><td>CAN0_HOLD</td><td>保留.</td><td>I2C2_HOLD</td><td>I2C1_HOLD</td><td>I2C0_HOLD</td><td>I2C5_HOLD</td><td>I2C4_HOLD</td><td>I2C3_HOLD</td><td colspan="2">保留</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>FWDGT_HOLD</td><td>WWDGT_HOLD</td><td>RTC_HOLD</td><td>保留.</td><td>TIMER13_HOLD</td><td>TIMER12_HOLD</td><td>TIMER11_HOLD</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td>TIMER4_HOLD</td><td>TIMER3_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>CAN1_HOLD</td><td>CAN1 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN1 接收寄存器停止接收数据。</td></tr><tr><td>25</td><td>CAN0_HOLD</td><td>CAN0 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN0 接收寄存器停止接收数据。</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>I2C2_HOLD</td><td>I2C2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>22</td><td>I2C1_HOLD</td><td>I2C1 保持位该位由软件置位和复位</td></tr></table>

<table><tr><td></td><td></td><td>0:无影响1:当内核停止时保持I2C1的SMBUS状态不变,用于调试。</td></tr><tr><td>21</td><td>I2C0_HOLD</td><td>I2C0保持位该位由软件置位和复位0:无影响1:当内核停止时保持I2C0的SMBUS状态不变,用于调试。</td></tr><tr><td>23</td><td>I2C5_HOLD</td><td>I2C5保持位该位由软件置位和复位0:无影响1:当内核停止时保持I2C5的SMBUS状态不变,用于调试。</td></tr><tr><td>22</td><td>I2C4_HOLD</td><td>I2C4保持位该位由软件置位和复位0:无影响1:当内核停止时保持I2C4的SMBUS状态不变,用于调试。</td></tr><tr><td>21</td><td>I2C3_HOLD</td><td>I2C3保持位该位由软件置位和复位0:无影响1:当内核停止时保持I2C3的SMBUS状态不变,用于调试。</td></tr><tr><td>17:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>FWDGT_HOLD</td><td>FWDGT保持位该位由软件置位和复位0:无影响1:当内核停止时保持FWDGT计数器时钟,用于调试。</td></tr><tr><td>11</td><td>WWDGT_HOLD</td><td>WWDG保持位该位由软件置位和复位0:无影响1:当内核停止时保持WWDGT计数器时钟,用于调试。</td></tr><tr><td>10</td><td>RTC_HOLD</td><td>RTC保持位该位由软件置位和复位0:无影响1:当内核停止时保持RTC计数器不变,用于调试</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13_HOLD</td><td>TIMER13保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器13计数器不变,用于调试。</td></tr><tr><td>7</td><td>TIMER12_HOLD</td><td>TIMER12保持位该位由软件置位和复位0:无影响</td></tr><tr><td>6</td><td>TIMER11_HOLD</td><td>TIMER 11 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器11计数器不变,用于调试。</td></tr><tr><td>5</td><td>TIMER6_HOLD</td><td>TIMER 6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器6计数器不变,用于调试。</td></tr><tr><td>4</td><td>TIMER5_HOLD</td><td>TIMER 5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器5计数器不变,用于调试。</td></tr><tr><td>3</td><td>TIMER4_HOLD</td><td>TIMER 4 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器4计数器不变,用于调试。</td></tr><tr><td>2</td><td>TIMER3_HOLD</td><td>TIMER 3 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器3计数器不变,用于调试。</td></tr><tr><td>1</td><td>TIMER2_HOLD</td><td>TIMER 2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器2计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER1_HOLD</td><td>TIMER 1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器1计数器不变,用于调试。</td></tr></table>

## 16.4.4. 控制寄存器 2（DBG_CTL2）

地址偏移：0x0C

复位值： 0x0000 0000，仅上电复位


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>TIMER10_HOLD</td><td>TIMER9_HOLD</td><td>TIMER8_HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>TIMER7_HOLD</td><td>TIMER0_HOLD</td></tr><tr><td colspan="14">位/位域</td><td>名称</td><td>描述</td></tr><tr><td colspan="14">31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td colspan="14">18</td><td>TIMER10_HOLD</td><td>TIMER10 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 10 计数器不变,用于调试。</td></tr><tr><td colspan="14">17</td><td>TIMER9_HOLD</td><td>TIMER9 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 9 计数器不变,用于调试。</td></tr><tr><td colspan="14">16</td><td>TIMER8_HOLD</td><td>TIMER8 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 8 计数器不变,用于调试。</td></tr><tr><td colspan="14">15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td colspan="14">1</td><td>TIMER7_HOLD</td><td>TIMER7 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 7 计数器不变,用于调试。</td></tr><tr><td colspan="14">0</td><td>TIMER0_HOLD</td><td>TIMER0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 0 计数器不变,用于调试。</td></tr></table>

## 16.4.5. 控制寄存器 3（DBG_CTL3）

地址偏移：0x10

复位值： 0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">DEVICEID[3: 0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr></table>

DEVICEID[3:0] 

这些位由软件读取和写入。
