## 16.4. DBG 寄存器

DBG 基地址：0xE004 4000

## 16.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

复位值：0xXXXX XXXX

只读寄存器

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器这些位由软件读取,这些位是不变的常数</td></tr></table>

## 16.4.2. 控制寄存器 0（DBG_CTL0）

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字(32 位)访问。

<table><tr><td></td><td></td><td>0: 跟踪引脚分配禁用1: 跟踪引脚分配使能。</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位0: 无影响1: 在待机模式下,所有工作的时钟继续运行,支持待机模式下调试。</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持该位由软件置位和复位0: 无影响1: 在深度睡眠模式下,所有工作的时钟继续运行,支持深度睡眠模式下调试。</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持位该位由软件置位和复位0: 无影响1: 在睡眠模式下,所有工作时钟继续运行,支持睡眠模式下调试。</td></tr></table>

## 16.4.3. 控制寄存器 1（DBG_CTL1）

地址偏移：0x08

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LPTIMER HOLD</td><td colspan="6">保留</td><td>I2C3_HOLD</td><td>I2C2_HOLD</td><td>I2C1_HOLD</td><td>I2C0_HOLD</td><td colspan="5">保留</td></tr><tr><td colspan="7">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>FWDGT_HOLD</td><td>WWDGT_HOLD</td><td>RTC_HOLD</td><td colspan="4">保留</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td>TIMER4_HOLD</td><td>TIMER3_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LPTIMER_HOLD</td><td>LPTIMER 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 LPTIMER 计数器不变,用于调试。</td></tr><tr><td>30:25</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>24</td><td>I2C3_HOLD</td><td>I2C3 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 I2C3 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>23</td><td>I2C2_HOLD</td><td>I2C2 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>22</td><td>I2C1_HOLD</td><td>I2C1 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 I2C1 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>21</td><td>I2C0_HOLD</td><td>I2C0 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>20:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>FWDGT_HOLD</td><td>FWDGT 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 FWDGT 计数器时钟,用于调试。</td></tr><tr><td>11</td><td>WWDGT_HOLD</td><td>WWDG 保持寄存器该位由软件置位和复位。0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试。</td></tr><tr><td>10</td><td>RTC_HOLD</td><td>RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试。</td></tr><tr><td>9:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TIMER6_HOLD</td><td>TIMER6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 6 计数器不变,用于调试。</td></tr><tr><td>4</td><td>TIMER5_HOLD</td><td>TIMER5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器5计数器不变,用于调试。</td></tr><tr><td>3</td><td>TIMER4_HOLD</td><td>TIMER4 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器4计数器不变,用于调试。</td></tr><tr><td>2</td><td>TIMER3_HOLD</td><td>TIMER3 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器3计数器不变,用于调试。</td></tr><tr><td>1</td><td>TIMER2_HOLD</td><td>TIMER2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器2计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER1_HOLD</td><td>TIMER1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器1计数器不变,用于调试。</td></tr></table>

## 16.4.4. 控制寄存器 2（DBG_CTL2）

地址偏移：0x0C

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>HRTIMER HOLD</td><td colspan="5">保留</td><td>TIMER19 HOLD</td><td>保留</td><td>TIMER16 HOLD</td><td>TIMER15 HOLD</td><td>TIMER14 HOLD</td></tr><tr><td colspan="11">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>TIMER7 HOLD</td><td>保留</td><td>TIMER0 HOLD</td><td colspan="8">保留</td><td>CAN2 HOLD</td><td>CAN1 HOLD</td><td>CAN0 HOLD</td></tr><tr><td colspan="4">rw</td><td colspan="9">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>HRTIMER_HOLD</td><td>HRTIMER 保持位</td></tr></table>

<table><tr><td></td><td></td><td>该位由软件置位和复位0:无影响1:当内核停止时保持HRTIMER计数器不变,用于调试。</td></tr><tr><td>25:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>TIMER19_HOLD</td><td>TIMER19保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器19计数器不变,用于调试。</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>TIMER16_HOLD</td><td>TIMER16保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器16计数器不变,用于调试。</td></tr><tr><td>17</td><td>TIMER15_HOLD</td><td>TIMER15保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器15计数器不变,用于调试。</td></tr><tr><td>16</td><td>TIMER14_HOLD</td><td>TIMER14保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器14计数器不变,用于调试。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>TIMER7_HOLD</td><td>TIMER7保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器7计数器不变,用于调试。</td></tr><tr><td>12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>TIMER0_HOLD</td><td>TIMER0保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器0计数器不变,用于调试。</td></tr><tr><td>10:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>CAN2_HOLD</td><td>CAN2保持位该位由软件置位和复位0:无影响</td></tr></table>

<table><tr><td></td><td></td><td>1: 当内核停止时 CAN2 接收寄存器停止接收数据。</td></tr><tr><td>1</td><td>CAN1_HOLD</td><td>CAN1 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN1 接收寄存器停止接收数据。</td></tr><tr><td>0</td><td>CAN0_HOLD</td><td>CAN0 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN0 接收寄存器停止接收数据。</td></tr></table>
