## 16.4. DBG 寄存器

DEBUG 基地址：0xE004 5000

## 16.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

只读寄存器

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器这些位由软件读取,这些位是不变的常数</td></tr></table>

## 16.4.2. 控制寄存器（DBG_CTL）

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td></td><td></td><td colspan="5">保留</td><td>TIMER16_HOLD</td><td>TIMER15_HOLD</td><td>保留</td><td>CAN1_HOLD</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td>TIMER4_HOLD</td><td>TIMER7_HOLD</td><td>I2C1_HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>I2C0_HOLD</td><td>CAN0_HOLD</td><td>TIMER3_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td><td>TIMER0_HOLD</td><td>WWDGT_HOLD</td><td>FWDGT_HOLD</td><td colspan="2">保留</td><td>TRACE_IOEN</td><td colspan="2">保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>TIMER16_HOLD</td><td>TIMER16 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持定时器 16 计数器不变,用于调试</td></tr></table>

23 TIMER15_HOLD TIMER15 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持定时器 15 计数器不变，用于调试
22 保留 必须保持复位值。
21 CAN1_HOLD CAN1 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时 CAN1 接收寄存器停止接收数据
20 TIMER6_HOLD TIMER6 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持定时器 6 计数器不变，用于调试
19 TIMER5_HOLD TIMER5 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持定时器 5 计数器不变，用于调试
18 TIMER4_HOLD TIMER4 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持定时器 4 计数器不变，用于调试
17 TIMER7_HOLD TIMER7 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持定时器 7 计数器不变，用于调试
16 I2C1_HOLD I2C1 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持 I2C1 的 SMBUS 状态不变，用于调试
15 I2C0_HOLD I2C0 保持寄存器
该位由软件置位和复位
0: 无影响
1: 当内核停止时保持 I2C0 的 SMBUS 状态不变，用于调试
14 CAN0_HOLD CAN0 保持寄存器
该位由软件置位和复位
0: 无影响

<table><tr><td>13</td><td>TIMER3_HOLD</td><td>TIMER 3 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持定时器3 计数器不变,用于调试</td></tr><tr><td>12</td><td>TIMER2_HOLD</td><td>TIMER 2 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持定时器2 计数器不变,用于调试</td></tr><tr><td>11</td><td>TIMER1_HOLD</td><td>TIMER 1 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持定时器1 计数器不变,用于调试</td></tr><tr><td>10</td><td>TIMER0_HOLD</td><td>TIMER 0 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持定时器0 计数器不变,用于调试</td></tr><tr><td>9</td><td>WWDGT_HOLD</td><td>WWDG 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持WWDGT计数器时钟,用于调试</td></tr><tr><td>8</td><td>FWDGT_HOLD</td><td>FWDGT 保持寄存器该位由软件置位和复位0:无影响1:当内核停止时保持FWDGT计数器时钟,用于调试</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TRACE_IOEN</td><td>跟踪引脚分配使能该位由软件置位和复位0:跟踪引脚分配禁用1:跟踪引脚分配使能</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持寄存器该位由软件置位和复位0:无影响1:在待机模式下,系统时钟和AHB时钟由CK_IRC8M提供,当退出待机模式时,产生系统复位</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持寄存器该位由软件置位和复位0:无影响1:在深度睡眠模式下,系统时钟和AHB时钟由CK_IRC8M提供</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持寄存器该位由软件置位和复位0:无影响1:在睡眠模式下,AHB时钟继续运行</td></tr></table>
