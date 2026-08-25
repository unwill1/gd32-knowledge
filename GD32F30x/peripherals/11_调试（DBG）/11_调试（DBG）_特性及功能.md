## 11. 调试（DBG）

## 11.1. 简介

GD32F30x 系列产品提供了各种各样的调试，跟踪和测试功能。这些功能通过 Arm®CoreSight组件的标准配置和链状连接的 TAP 控制器来实现的。调试和跟踪功能集成在 Arm® Cortex®-M4 内核中。调试系统支持串行（SW）调试和跟踪功能，也支持 JTAG 调试。调试和跟踪功能请参考下列文档：

Cortex-M4技术参考手册；

Arm®调试接口v5结构规范。

调试系统帮助调试者在低功耗模式下调试或者一些外设调试。当相应的位被置 1，调试系统会在低功耗模式下提供时钟，或者为一些外设保持当前状态，这些外设包括：TIMER、WWDGT、FWDGT、I2C 和 CAN。

## 11.2. JTAG / SW 功能描述

调试工具可以通过串行（SW）调试接口或者 JTAG 调试接口来访问调试功能。

## 11.2.1. 切换 JTAG / SW 接口

默认使用 JTAG 调试接口，可以通过下列软件序列从 JTAG 调试切换到 SW 调试：

发送50个以上TCK周期的TMS=1信号；

发送16位TMS = 1110011110011110 (0xE79E LSB)信号；

发送50个以上TCK周期的TMS=1信号。

切换 SW 调试到 JTAG 调试的软件序列：

发送50个以上TCK周期的TMS=1信号；

发送16位TMS = 1110011100111100 (0xE73C LSB)信号；

发送50个以上TCK周期的TMS=1信号。

## 11.2.2. 引脚分配

JTAG 调试提供五个引脚的接口：JTAG 时钟引脚（JTCK），JTAG 模式选择引脚（JTMS），JTAG 数据输入引脚（JTDI），JTAG 数据输出引脚（JTDO），JTAG 复位引脚（NJTRST,低电平有效）。串行调试（SWD）提供两个引脚的接口：数据输入输出引脚（SWDIO）和时钟引脚（SWCLK）。SW 调试接口的两个引脚与 JTAG 调试接口的两个引脚复用，SWDIO 和 JTMS复用，SWCLK 和 JTCK 复用。

当异步跟踪功能开启时，JTDO 引脚也用作异步跟踪数据输出（TRACESWO）。


表 10-5. 调试引脚分配


<table><tr><td>引脚</td><td>调试接口</td></tr><tr><td>PA15</td><td>JTDI</td></tr><tr><td>PA14</td><td>JTCK/SWCLK</td></tr><tr><td>PA13</td><td>JTMS/SWDIO</td></tr><tr><td>PB4</td><td>NJTRST</td></tr><tr><td>PB3</td><td>JTDO</td></tr></table>

默认复位后使用五个引脚的 JTAG 调试，用户可以在不使用 NJTRST 引脚情况下正常使用JTAG 功能，此时 PB4 可以用作普通 GPIO 功能（NJTRST 硬件拉高）。如果切换到 SW 调试模式，PA15/PB4/PB3 释放作为普通 GPIO 功能。如果 JTAG 和 SW 调试功能都没有使用，这五个引脚都释放作为普通GPIO功能。五个引脚具体配置请参考JTAG/SWD 。

## 11.2.3. JTAG 链状结构

Cortex-M4 内核的 JTAG TAP 和 MCU JTAG TAP 串行连接。MCU JTAG 的 IR（指令寄存器）是 5 位，而 Cortex-M4 内核的 JTAG 的 IR（指令寄存器）是 4 位。所以当 JTAG 进行 IR 移位输入时，首先移位 5 位 BYPASS 指令给 MCU JTAG，然后移位 4 位标准指令给 Cortext-M4JTAG。当进行数据移位时，数据链只需要额外添加一位，因为 MCU JTAG 已处在 BYPASS 模式。

MCU JTAG ID 代码是 0x790007A3。

## 11.2.4. 调试复位

JTAG-DP和SW-DP寄存器位于上电复位域。系统复位初始化了Cortex-M4的绝大部分组件，除了 NVIC，调试逻辑（FPB，DWT，ITM）。NJTRST 能复位 JTAG TAP 控制器。所以，可以在系统复位下实现调试功能。例如：复位后停止，用户在系统复位后配置相应停止位，系统复位释放后处理器会立即停止。

## 11.2.5. JEDEC-106 ID code

Cortex-M4 集 成 了 JEDEC-106 ID 代 码 。 位 于 ROM 表 中 ， 映 射 地 址 为0xE00FF000_0xE00FFFFF。

## 11.3. 调试保持功能描述

## 11.3.1. 低功耗模式调试支持

当 DBG 控制寄存器 0（DBG_CTL0）的 STB_HOLD 位置 1 并且进入待机模式，AHB 总线时钟和系统时钟由 CK_IRC8M 提供，可以在待机模式下调试。当退出待机模式后，产生系统复位。

当 DBG 控制寄存器 0（DBG_CTL0）的 DSLP_HOLD 位置 1 并且进入深度睡眠模式，AHB总线时钟和系统时钟由 CK_IRC8M 提供，可以在深度睡眠模式下调试。

当 DBG 控制寄存器 0（DBG_CTL0）的 SLP_HOLD 位置 1 并且进入睡眠模式，AHB 总线时钟没有关闭，可以在睡眠模式下调试。

## 11.3.2. TIMER, I2C, WWDGT, FWDGT 和 CAN 外设调试支持

当内核停止，并且 DBG 控制寄存器 1（DBG_CTL0）中的相应位置 1。对于不同外设，有不同动作：

对于 TIMER 外设，TIMER 计数器停止并进行调试；

对于 I2C 外设，SMBUS 保持状态并进行调试；

对于WWDGT 或者 FWDGT 外设，计数器时钟停止并进行调试；

对于 CAN 外设，接收寄存器停止计数并进行调试。
