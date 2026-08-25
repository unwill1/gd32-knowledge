## 12. 调试（DBG）

## 12.1. 简介

GD32F4xx 系列产品提供了各种各样的调试，跟踪和测试功能。这些功能通过 ARM®CoreSight™组件的标准配置和链状连接的 TAP 控制器来实现的。调试和跟踪功能集成在ARM® Cortex®-M4 内核中。调试系统支持串行（SW）调试和跟踪功能，也支持 JTAG 调试。调试和跟踪功能请参考下列文档：

Cortex®-M4技术参考手册；

ARM®调试接口v5结构规范。

调试系统帮助调试者在低功耗模式下调试。当相应的位被置 1，调试系统会在低功耗模式下提供时钟，或者为一些外设保持当前状态，这些外设包括：TIMER、WWDGT、FWDGT、RTC、I2C 和 CAN。

## 12.2. JTAG/SW 功能说明

调试工具可以通过串行（SW）调试接口或者 JTAG 调试接口来访问调试功能。

## 12.2.1. 切换 JTAG/ SW 接口

默认使用 JTAG 调试接口，可以通过下列软件序列从 JTAG 调试切换到 SW调试：

发送50个以上TCK周期的TMS=1信号；

发送16位TMS = 1110011110011110（0xE79E LSB）信号；

发送50个以上TCK周期的TMS=1信号。

切换 SW调试到 JTAG 调试的软件序列：

发送50个以上TCK周期的TMS=1信号；

发送16位TMS = 1110011100111100 （0xE73C LSB）信号；

发送50个以上TCK周期的TMS=1信号。

## 12.2.2. 引脚分配

JTAG 调试提供五个引脚的接口：JTAG 时钟引脚（JTCK），JTAG 模式选择引脚（JTMS），JTAG 数据输入引脚（JTDI），JTAG 数据输出引脚（JTDO），JTAG 复位引脚（NJTRST，低电平有效）。串行调试（SWD）提供两个引脚的接口：数据输入输出引脚（SWDIO）和时钟引脚（SWCLK）。SW调试接口的两个引脚与 JTAG 调试接口的两个引脚复用，SWDIO 和 JTMS复用，SWCLK 和 JTCK 复用。

当异步跟踪功能开启时，JTDO 引脚也用作异步跟踪数据输出（TRACESWO）。


表 12-1. 调试引脚分配


<table><tr><td>引脚</td><td>调试接口</td></tr><tr><td>PA15</td><td>JTDI</td></tr><tr><td>PA14</td><td>JTCK/SWCLK</td></tr><tr><td>PA13</td><td>JTMS/SWDIO</td></tr><tr><td>PB4</td><td>NJTRST</td></tr><tr><td>PB3</td><td>JTDO</td></tr></table>

默认复位后使用五个引脚的 JTAG 调试，用户可以在不使用 NJTRST 引脚情况下正常使用JTAG 功能，此时 PB4 可以用作普通 GPIO 功能（NJTRST 硬件拉高）。如果切换到 SW 调试模式，PA15/PB4/PB3 释放作为普通 GPIO 功能。如果 JTAG 和 SW 调试功能都没有使用，这五个引脚都释放作为普通 GPIO 功能。五个引脚具体配置请参考 /GPIO  AFIO 。

## 12.2.3. JTAG 链状结构

Cortex®-M4 内核的 JTAG TAP 和 MCU TAP 串行连接。MCU JTAG 的 IR（指令寄存器）是 5位，而 Cortex®-M4 内核的 JTAG 的 IR（指令寄存器）是 4 位。所以当 JTAG 进行 IR 移位输入时，首先移位 5 位 BYPASS 指令给 MCU JTAG，然后移位 4 位标准指令给 Cortex®-M4JTAG。当进行数据移位时，数据链只需要额外添加一位，因为 MCUJTAG 已处在 BYPASS模式。

MCU JTAG ID 代码是 0x790007A3。

## 12.2.4. 调试复位

JTAG-DP 和 SW-DP 寄存器位于上电复位域。系统复位初始化了 Cortex®-M4 的绝大部分组件，除了 NVIC，调试逻辑（FPB，DWT，ITM）。NJTRST 能复位 JTAG TAP 控制器。所以，可以在系统复位下实现调试功能。例如：复位后停止，用户在系统复位后配置相应停止位，系统复位释放后处理器会立即停止。

## 12.2.5. JEDEC-106 ID code

Cortex®-M4 集 成 了 JEDEC-106 ID 代 码 。 位 于 ROM 表 中 ， 映 射 地 址 为0xE00FF000_0xE00FFFFF。

## 12.3. 调试保持功能说明

## 12.3.1. 低功耗模式调试支持

当 DBG 控制寄存器 0（DBG_CTL0）的 STB_HOLD 位置 1 并且进入待机模式，AHB 总线时钟和系统时钟由 CK_IRC16M 提供，可以在待机模式下调试。当退出待机模式后，产生系统复位。

当 DBG 控制寄存器 0（DBG_CTL0）的 DSLP_HOLD 位置 1 并且进入深度睡眠模式，AHB

总线时钟和系统时钟由 CK_IRC16M 提供，可以在深度睡眠模式下调试。

当 DBG 控制寄存器 0（DBG_CTL0）的 SLP_HOLD 位置 1 并且进入睡眠模式，AHB 总线时钟没有关闭，可以在睡眠模式下调试。

## 12.3.2. TIMER, I2C, RTC, WWDGT, FWDGT 和 CAN 外设调试支持

当内核停止，并且 DBG 控制寄存器 1（DBG_CTL1）或 DBG 控制寄存器 2（DBG_CTL2）中的相应位置 1。对于不同外设，有不同动作：

对于 TIMER 外设，TIMER 计数器停止并进行调试；

对于 I2C 外设，SMBUS 保持状态并进行调试；

对于 WWDGT 或者 FWDGT 外设，计数器时钟停止并进行调试；

对于 RTC 外设，计数器停止并进行调试；

对于 CAN 外设，接收寄存器停止计数并进行调试。

## 0：无影响

1：在待机模式下, 系统时钟和AHB 时钟由 CK_IRC16M 提供, 当退出待机模式时，产生系统复位。

1 DSLP_HOLD 

深度睡眠模式保持位

该位由软件置位和复位

0：无影响

1：在深度睡眠模式下, 系统时钟和 AHB 时钟由 CK_IRC16M 提供。

0 SLP_HOLD 

睡眠模式保持位

该位由软件置位和复位

0：无影响

1：在睡眠模式下, AHB 时钟继续运行。

## 12.4.3. 控制寄存器 1 (DBG_CTL1)

地址偏移：0x08

复位值： 0x0000 0000，仅上电复位


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>CAN1_HOLD</td><td>CAN0_HOLD</td><td>保留.</td><td>I2C2_HOLD</td><td>I2C1_HOLD</td><td>I2C0_HOLD</td><td colspan="5">保留</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>FWDGT_HOLD</td><td>WWDGT_HOLD</td><td>RTC_HOLD</td><td>保留.</td><td>TIMER13_HOLD</td><td>TIMER12_HOLD</td><td>TIMER11_HOLD</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td>TIMER4_HOLD</td><td>TIMER3_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>


位/位域 名称



描述


<table><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>CAN1_HOLD</td><td>CAN1 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN1 接收寄存器停止接收数据。</td></tr><tr><td>25</td><td>CAN0_HOLD</td><td>CAN0 保持位该位由软件置位和复位0:无影响1:当内核停止时 CAN0 接收寄存器停止接收数据。</td></tr><tr><td>24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>I2C2_HOLD</td><td>I2C2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>22</td><td>I2C1_HOLD</td><td>I2C1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C1 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>21</td><td>I2C0_HOLD</td><td>I2C0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试。</td></tr><tr><td>20:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>FWDGT_HOLD</td><td>FWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 FWDGT 计数器时钟,用于调试。</td></tr><tr><td>11</td><td>WWDGT_HOLD</td><td>WWDG 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试。</td></tr><tr><td>10</td><td>RTC_HOLD</td><td>RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TIMER13_HOLD</td><td>TIMER13 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 13 计数器不变,用于调试。</td></tr><tr><td>7</td><td>TIMER12_HOLD</td><td>TIMER 12 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 12 计数器不变,用于调试。</td></tr><tr><td>6</td><td>TIMER11_HOLD</td><td>TIMER 11 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 11 计数器不变,用于调试。</td></tr><tr><td>5</td><td>TIMER6_HOLD</td><td>TIMER 6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 6 计数器不变,用于调试。</td></tr><tr><td>4</td><td>TIMER5_HOLD</td><td>TIMER 5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器5计数器不变,用于调试。</td></tr><tr><td>3</td><td>TIMER4_HOLD</td><td>TIMER 4 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器4计数器不变,用于调试。</td></tr><tr><td>2</td><td>TIMER3_HOLD</td><td>TIMER 3 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器3计数器不变,用于调试。</td></tr><tr><td>1</td><td>TIMER2_HOLD</td><td>TIMER 2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器2计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER1_HOLD</td><td>TIMER 1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器1计数器不变,用于调试。</td></tr></table>

## 12.4.4. 控制寄存器 (DBG_CTL2)

地址偏移：0x0C

复位值： 0x0000 0000，仅上电复位


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>TIMER10 _HOLD</td><td>TIMER9_ HOLD</td><td>TIMER8_ HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>TIMER7_ HOLD</td><td>TIMER0_ HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>TIMER10_HOLD</td><td>TIMER10 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器 10 计数器不变,用于调试。</td></tr><tr><td>17</td><td>TIMER9_HOLD</td><td>TIMER9 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器9计数器不变,用于调试。</td></tr><tr><td>16</td><td>TIMER8_HOLD</td><td>TIMER8 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器8计数器不变,用于调试。</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>TIMER7_HOLD</td><td>TIMER7 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器7计数器不变,用于调试。</td></tr><tr><td>0</td><td>TIMER0_HOLD</td><td>TIMER0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持定时器0计数器不变,用于调试。</td></tr></table>
