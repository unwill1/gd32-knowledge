## 16. 调试（DBG）

## 16.1. 简介

GD32G553 系列产品提供了各种各样的调试，跟踪和测试功能。这些功能通过 Arm® CoreSight™组件的标准配置和链状连接的 TAP 控制器来实现的。调试和跟踪功能集成在 ARM Cortex®-M33内核中。调试系统支持串行（SW）调试和跟踪功能，也支持 JTAG 调试。调试和跟踪功能请参考下列文档：

 Cortex<sup>®</sup>-M33技术参考手册；

 ARM调试接口v5结构规范。

调试系统帮助调试者在低功耗模式下调试。当相应的位被置 1，调试系统会在低功耗模式下提供时钟，或者为一些外设保持当前状态，这些外设包括：TIMER、WWDGT、 FWDGT、RTC、I2C、RTC、CAN、LPTIMER 和 HRTIMER。

## 16.2. JTAG/SW 功能描述

调试工具可以通过串行（SW）调试接口或者 JTAG 调试接口来访问调试功能。

## 16.2.1. 切换 JTAG / SW 接口

默认使用 JTAG 调试接口，可以通过下列软件序列从 JTAG 调试切换到 SW 调试：

 发送 50 个以上 TCK 周期的 TMS=1 信号；

 发送 16 位 TMS = 1110011110011110（0xE79E LSB）信号；

 发送 50 个以上 TCK 周期的 TMS=1 信号。

切换 SW 调试到 JTAG 调试的软件序列：

 发送 50 个以上 TCK 周期的 TMS=1 信号；

 发送 16 位 TMS = 1110011100111100（0xE73C LSB）信号；

 发送 50 个以上 TCK 周期的 TMS=1 信号。

## 16.2.2. 引脚分配

JTAG 调试提供五个引脚的接口：JTAG 时钟引脚（JTCK），JTAG 模式选择引脚（JTMS），JTAG数据输入引脚（JTDI），JTAG 数据输出引脚（JTDO），JTAG 复位引脚（NJTRST,低电平有效）。串行调试（SWD）提供两个引脚的接口：数据输入输出引脚（SWDIO）和时钟引脚（SWCLK）。SW 调试接口的两个引脚与 JTAG 调试接口的两个引脚复用，SWDIO 和 JTMS 复用，SWCLK和JTCK 复用。

当异步跟踪功能开启时，JTDO 引脚也用作异步跟踪数据输出（TRACESWO）。


表 16-1. 引脚分配


<table><tr><td>引脚</td><td>调试接口</td></tr><tr><td>PA15</td><td>JTDI</td></tr><tr><td>PA14</td><td>JTCK/SWCLK</td></tr><tr><td>PA13</td><td>JTMS/SWDIO</td></tr><tr><td>PB3</td><td>JTDO</td></tr><tr><td>PB4</td><td>NJTRST</td></tr></table>

默认复位后使用五个引脚的 JTAG 调试，用户可以在不使用 NJTRST 引脚情况下正常使用 JTAG功能，此时 PB4 可以用作普通 GPIO 功能（NJTRST 硬件拉高）。如果切换到 SW 调试模式，PA15/PB4/PB3 释放作为普通 GPIO 功能。如果 JTAG 和 SW 调试功能都没有使用，这五个引脚都释放作为普通 GPIO 功能。具体请参考 AF 。

## 16.2.3. JTAG


图 16-1. JTAG 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/00cd5c122faa515ee0979782d8621cadae1a7432cae604fa54aaac9965faf12e.jpg)


## JTAG 链状结构

Cortex®-M33 内核的 JTAG TAP（CPU JTAG）和 MCU JTAG TAP 串行连接。MCU JTAG 的 IR（指令寄存器）是 5 位，而 Cortex®-M33 内核的 JTAG 的 IR（指令寄存器）是 4 位。所以当 JTAG进行 IR 移位输入时，首先移位 5 位 BYPASS 指令给 MCU JTAG，然后移位 4 位标准指令给Cortex®-M33 JTAG。当进行数据移位时，数据链只需要额外添加一位，因为 MCU JTAG 已处在BYPASS 模式。

MCU JTAG ID 代码是 0x790007A3。

## 安全 JTAG

1. 安全 JTAG 只支持 JTAG，不支持 SW

## 2. OTP 配置

OTP 相关位：SWEN, NDBG[1:0], DPx[31:0](x=0,1)


表 16-2. OTP JTAG 字节


<table><tr><td>地址</td><td>名称</td><td>属性</td><td>描述</td></tr><tr><td>0x1fff f000</td><td>DP0[31:0]</td><td>w</td><td>安全 JTAG 密码 0出厂值: 0xFFFFFFFF</td></tr><tr><td>0x1fff f004</td><td>DP1[31:0]</td><td>w</td><td>安全 JTAG 密码 1出厂值: 0xFFFFFFFF</td></tr><tr><td>0x1fff f008</td><td>OTP_USER[31:0]</td><td>rw</td><td>[31:16]: LK写秘钥值 0x3CC3 上锁 OTP JTAG 字节, 其它值解锁出厂值: 0xFFFF[15:3]: 保留[2:1]: NDBG0x: 无调试10: 安全 JTAG11: 无安全 JTAG(出厂值)[0] : SWEN0: SW 失能1: SW 使能(出厂值)</td></tr><tr><td>0x1fff f00c</td><td>-</td><td>-</td><td>保留</td></tr></table>


注意：OTP JTAG bytes 保持出厂值，全 FFFF，设置 LK[31:16] 秘钥值 0x3cc3 之后，保护 OTPJTAG bytes 的值不被修改。如果 OTP JTAG bytes 的值已经修改过，设置 LK[31:16] 为 0x3cc3 的值将没有作用。


## 3. 安全 JTAG 的使用

a) 配置 OTP 为安全 JTAG：首先配置 JTAG 安全密码 DPx[31:0]（x = 0，1），再配置 NDBG[1:0]= 2b’10。

b) 电源复位：电源复位后，JTAG 处于安全状态，secure_jtag 为 1，此时无法通过 JTAG 操作 CPU。

c) 安全 JTAG 解除：JTAG 主机依次将以下两个密码写入 MCU JTAG 以解除安全模式。此时secure_jtag 为 0，可通过 JTAG 对 CPU 进行操作。

IR：写入 5’b10101，DR：写入 DP0[31:0]。

IR：写入 5’b10110，DR：写入 DP2[31:0]。

## 注意：

1 如果密码输入错误，则需电源复位。

2 发生任何错误的输入序列后，若想重新解密都需要电源复位。

d) 读取写入值和 JTAG 状态。

IR：写入 5’b11000，DR：可读出 IR 为 5’b10101 写入的值，检查写入值是否正确。

IR：写入 5’b11001，DR：可读出 IR 为 5’b10110 写入的值，检查写入值是否正确。

IR：写入 5’b11010，DR：可读出{30‘b0, wrong_seq, secure_jtag}。secure_jtag 表示 JTAG状态，其中：

1：无法通过 JTAG 操作 CPU；

0：可以通过 JTAG 操作 CPU。

wrong_seq 表示解密过程错误标志，其中：

1：解密过程发生错误；

0：解密过程未发生错误。

## 16.2.4. 调试复位

JTAG-DP 和 SW-DP 寄存器位于上电复位域。系统复位初始化了 Cortex®-M33 的绝大部分组件，除了 NVIC，调试逻辑（FPB，DWT，ITM）。NJTRST 能复位 JTAG TAP 控制器。所以，可以在系统复位下实现调试功能。例如：复位后停止，用户在系统复位后配置相应停止位，系统复位释放后处理器会立即停止。

## 16.2.5. JEDEC-106 ID code

Cortex®-M33 集 成 了 JEDEC-106 ID 代 码 。 位 于 ROM 表 中 ， 映 射 地 址 为0xE00FF000_0xE00FFFFF。

## 16.3. 调试保持功能描述

## 16.3.1. 低功耗模式调试支持

当 DBG 控制寄存器 0（DBG_CTL0）的 STB_HOLD 位置 1 并且进入待机模式，AHB 总线时钟和系统时钟由 CK_IRC8M 提供，可以在待机模式下调试。当退出待机模式后，产生系统复位。

当 DBG 控制寄存器 0（DBG_CTL0）的 DSLP_HOLD 位置 1 并且进入深度睡眠模式，AHB 总线时钟和系统时钟由 CK_IRC8M 提供，可以在深度睡眠模式下调试，退出深度睡眠时，PLL 关闭，

系统时钟切换到 IRC8M。

当 DBG 控制寄存器 0（DBG_CTL0）的 SLP_HOLD 位置 1 并且进入睡眠模式，AHB 总线时钟没有关闭，可以在睡眠模式下调试。

## 16.3.2. TIMER, I2C, WWDGT, FWDGT, RTC, CAN, LPTIMER 和 HRTIMER 外设调试支持

当内核停止，并且 DBG 控制寄存器 x（DBG_CTLx，x=0，1，2）中的相应位置 1。对于不同外设，有不同动作：

对于 TIMER/LPTIMER/HRTIMER 外设，TIMER 计数器停止并进行调试；

对于 I2C 外设，SMBUS 保持状态并进行调试；

对于WWDGT 或者 FWDGT 外设， 计数器时钟停止并进行调试；

对于 RTC 外设，计数器停止并进行调试；

对于 CAN 外设，接收寄存器停止计数并进行调试。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>TRACE_I OEN</td><td colspan="2">保留</td><td>STB_ HOLD</td><td>DSLP_ HOLD</td><td>SLP_ HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:6</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>5</td><td colspan="3">TRACE_IOEN</td><td colspan="12">跟踪引脚分配使能该位由软件置位和复位。</td></tr></table>
