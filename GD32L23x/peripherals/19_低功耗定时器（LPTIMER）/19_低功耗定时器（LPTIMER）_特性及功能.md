## 19. 低功耗定时器（LPTIMER）

## 19.1. 简介

LPTIMER 是一个 32 位（GD32L233）或 16 位（GD32L235）的定时器，它能够在除待机模式（Standby mode）以外的所有功耗模式下运行。LPTIMER 提供了灵活的时钟机制，在将功耗降至最低的同时，还可以实现所需的功能和性能。

LPTIMER 可以用作没有内部时钟源的脉冲计数器。LPTIMER 可以将系统从低功耗模式唤醒，非常适合于以极低的功耗实现超时模式的场合。

## 19.2. 主要特征

◼ 计数器宽度：32位（GD32L233）或16位（GD32L235）

◼ 时钟源可选：

内部时钟源：内部IRC16MDIV，内部32KHz RC晶振（IRC32K），32.768 KHz低速晶振（LXTAL），APB1时钟（PCLK1, GD32L235）和APB2时钟（PCLK2,GD32L233）

外部时钟源：来自于LPTIMER_IN0引脚上的时钟源（作为脉冲计数器）

◼ 计数模式：向上计数

◼ 运行模式：连续计数模式或单次计数模式

◼ 可编程的预分频器：3位

◼ 通道输出可配置：可编程的PWM模式，单脉冲模式，置位模式

◼ 自动重装载功能

◼ 中断输出

◼ 可选择的触发：软件触发或硬件输入触发

◼ 译码器模式：译码器模式0和译码器模式1

## 19.3. 结构框图

19-1. LPTIMER 提供了低功耗定时器的内部配置细节。


图 19-1. LPTIMER 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/0cf1e1c4b69d3924c92dc754571821ecf9ffd02a6e68e76fbd8d89747e19cf47.jpg)


## 19.4. 功能描述

## 19.4.1. 时钟源配置

LPTIMER 可以由多个时钟源提供时钟，如内部时钟源有：IRC16MDIV 时钟，内部 32KHz RC晶振（IRC32K），32.768 KHz 低速晶振（LXTAL），APB1 时钟（PCLK1，GD32L235）和APB2 时钟（PCLK2,GD32L233），这些时钟源来自于复位和时钟单元 RCU。

LPTIMER 还可以使用外部引脚 LPTIMER_IN0 上的外部时钟信号作为时钟，当使用外部时钟作为时钟源时，LPTIMER 有以下两种配置方式：

◼ Case 0：当LPTIMER由外部信号提供时钟时，还需要APB1或其他晶振（如IRC16MDIV、IRC32K和LXTAL）同时提供内部时钟信号；

◼ Case 1：LPTIMER的时钟仅由LPTIMER_IN0引脚上外部时钟信号提供。在进入低功耗模式后，所有晶振关闭，此配置可用于实现超时模式或脉冲计数器功能。


图 19-2. LPTIMER 时钟源选择


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/815304bcc5190e75cebc31e5bfc0cc8ec61a60d2a30bb3f0565f40a0d05aec0f.jpg)


LPTIMER 可以由内部时钟信号或外部时钟信号（由 LPTIMER_CTL0 寄存器中的 CNTMEN 位和 CKSSEL 位控制）驱动。CKSSEL 位用于选择哪个时钟驱动计数器预分频器，默认时钟源为 PCLK1。CNTMEN 位用于选择哪个时钟信号驱动 LPTIMER 计数器。

当 LPTIMER 使用外部时钟信号时，CKPSEL 用于配置计数器的有效边沿。计数器可以由外部时钟的上升沿、下降沿或双边沿更新，具体由 CKPSEL[1:0]位域配置。

需要注意的是，当由外部引脚 LPTIMER_IN0 提供外部时钟信号时，如果有效边沿选择双边沿（CKPSEL=2’b10）或者 LPTIMER_IN0 引脚由数字滤波器采样（ECKFLT≠2’b00），则还需要提供内部时钟信号（Case 0）。在这种情况下，内部时钟信号频率至少是外部时钟频率的 4 倍。

可以根据 CKSSEL 位和 CNTMEN 位的配置，选择以下的时钟模式：

◼ CKSSEL = 0：LPTIMER时钟由内部时钟信号提供

- 内部时钟模式0（CNTMEN = 0）

LPTIMER由内部时钟信号提供时钟，计数器在内部时钟的每个脉冲进行计数。

- 内部时钟模式1（CNTMEN = 1）

外部时钟信号（LPTIMER_IN0）由内部时钟进行采样，因此，为了保证不丢失任何事件，外部时钟的变化频率不能超过内部时钟的频率。并且，LPTIMER的内部时钟信号不能预分频（PSC [2:0] = 000）。

## ◼ CKSSEL = 1：LPTIMER时钟由外部时钟信号提供

这种情况下，可以将CNTMEN位置1或清零，LPTIMER不需要使用内部时钟源（除非使能了输入滤波或是选择了双边沿作为外部时钟的有效边沿）。LPTIMER_IN0引脚上的外部信号作为LPTIMER的系统时钟，该情况适用于没有嵌入式晶振的工作情况；

这种情况下，LPTIMER的计数器可以在外部时钟信号的上升沿或下降沿计数，不能在双边沿计数。

由于LPTIMER_IN0引脚上的外部时钟信号也用于驱动LPTIMER的内核逻辑部分，因此，在计数器计数之前会有一些初始延迟（LPTIMER使能之后）。因此，在使能LPTIMER之后，LPTIMER_IN0引脚上的外部时钟信号前5个有效边沿将会丢失。


图 19-3. 内部时钟模式 1（CKSSEL = 0，CNTMEN = 1，PSC[2:0] = 000）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/4293078f0f42613727cbb3482c3cf9cd9d77ffcb34a3eeb2d8500f4d74bd8ac2.jpg)


## 19.4.2. LPTIMER 使能

LPTIMER_CTL1 寄存器的 LPTEN 位用于使能 LPTIMER 的内核逻辑模块。在 LPTEN 位置 1后，实际使能 LPTIMER 之前需要延迟两个 LPTIMER_CK 时钟周期。

只有在 LPTIEMR 禁能时，才能修改 LPTIMER_CTL0 和 LPTIMER_INTEN 寄存器（INHLCOIE位和 HLCMVUPIF 位除外）。

## 19.4.3. 预分频器

预分频器可以将LPTIMER的时钟LPTIMER_CK除以2的乘幂分频为计数器时钟PSC_CLK。只有在 LPTIEMR 禁能（LPTEN=0）时，才能修改 PSC[2:0]位域。下表列出了所有的分频系数：


表 19-1. 预分频器的分频系数


<table><tr><td>预分频系数</td><td>PSC[2:0]位域</td></tr><tr><td>1/1</td><td>000</td></tr><tr><td>1/2</td><td>001</td></tr><tr><td>1/4</td><td>010</td></tr><tr><td>1/8</td><td>011</td></tr><tr><td>1/16</td><td>100</td></tr><tr><td>1/32</td><td>101</td></tr><tr><td>1/64</td><td>110</td></tr><tr><td>1/128</td><td>111</td></tr></table>

## 19.4.4. 输入滤波

LPTIMER_Inx 引脚上的外部（映射到 GPIO）或内部（映射到片上外设，如比较器）信号需要通过数字滤波器进行滤波，以防止毛刺和噪声干扰在 LPTIMER 中扩散，这可以有效防止误计数和误触发。

在使用数字滤波器之前，需要先给 LPTIMER 提供内部时钟源，这样可以确保滤波器的正确运行。

数字滤波器有两种类型：

◼ 第1种：用于保护LPTIMER的外部输入（LPTIMER_IN0/ LPTIMER_IN1），数字滤波器由ECKFLT[1:0]位进行配置；

◼ 第2种：用于保护LPTIMER的触发输入（ETIx），数字滤波器由TFLT[1:0]位进行配置；

注意：相同类型的数字滤波器应该保持相同的配置。

数字滤波器的灵敏度取决于 LPTIMER 输入引脚上连续相同采样的数量，并将信号电平变化视为有效。 19-4. ECKFLT=2’b01 显示了输入滤波器 2 次连续采样的示例。


图 19-4. 输入滤波时序图（ECKFLT=2’b01）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/1ffbdf48c567deb16dbdce085b8c9d50376e787cea259d85db30e3cd6b5d10c6.jpg)


注意：如果没有内部时钟信号，则必须禁能数字滤波器（设置 ECKFLT=0，TFLT=0）。这种情况下，可以使用外部模拟滤波器来保证 LPTIMER 的外部输入不受干扰。

## 19.4.5. 外部输入高电平计数器

将 INHLCEN 位置 1 可以使能外部输入 LPTIMER_Inx 的高电平计数器功能，高电平计数器的时钟由内部时钟 CK_LPTIMER 提供。当 LPTIMER_Inx 引脚上出现高电平时，计数器开始计数，一旦出现低电平，计数器清零。

当高电平计数器的计数值等于 INHLCMVAL 位域（在 LPTIMER_INHLCMV 寄存器中）定义的数值时，LPTIMER_INTF 寄存器中的 INHLCOIF 位由硬件置位。若使能了 LPTIMER_INTEN寄存器中的 INHLCOIE 位，则会产生中断。可以通过向 INTC 寄存器中的 INHLCOIC 位写 1来清除 INHLCOIF 中断标志位。

19-5. 给出了外部输入高电平计数器的示例。


图 19-5. 外部输入高电平计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/2f11e2277179d8154b2713e0b8dd8e63e18db6ad1477051bb0ea55d6a202e83a.jpg)


APB 总线和 CK_LPTIMER 使用不同的时钟，因此，APB 写操作和 LPTIMER_INHLCMV 寄存器实际使用这些值的时间存在一些延迟。在此延迟时间内，应当避免对该寄存器的任何其他写操作。

LPTIMER_INTF 寄存器中的 HLCMVUPIF 位用于说明对 LPTIMER_INHLCMV 寄存器的写操作何时完成。

## 19.4.6. 计数器启动

LPTIMER 的计数器可以通过软件触发或通过检测 8 个触发输入上的有效边沿来启动。ETMEN[1:0]位域用于配置 LPTIMER 的触发模式：

◼ ETMEN[1:0] = 2’b 00：一旦软件置位CTNMST位或SMST位，LPTIMER的计数器就启动了；

◼ ETMEN[1:0] ≠ 2’b00：ETSEL[2:0]位用于选择8个触发输入中的一个来启动LPTIMER。ETMEN[1:0]位域的其余3个非零值用于配置触发输入所使用的有效边沿。一旦检测到有效边沿，LPTIMER计数器就会启动。

外部触发可视为 LPTIMER 的异步信号，因此，一旦检测到触发信号，为了实现同步，在LPTIMER 开始运行之前需要延迟 2 个计数器时钟周期。如果在 LPTIMER 启动后发生新的触发事件，该触发事件将会被忽略（除非使能了超时模式）。

注意：在置位 SMST 位和 CTNMST 位之前，必须将 LPTEN 位置位。当 LPTEN=0 时，对这些位的任何写操作都将被硬件丢弃。

## 19.4.7. 外部触发映射

LPTIMER 外部触发连接的情况如下 19-2. 所示：


表 19-2. 外部触发映射


<table><tr><td>ETSEL[2:0]</td><td>外部触发映射</td></tr><tr><td>ETI0</td><td>GPIO</td></tr><tr><td>ETI1</td><td>RTC闹钟0</td></tr><tr><td>ETI2</td><td>RTC闹钟1</td></tr><tr><td>ETI3</td><td>RTC_TAMP0</td></tr><tr><td>ETI4</td><td>RTC_TAMP1</td></tr><tr><td>ETI5</td><td>RTC_TAMP2</td></tr><tr><td>ETI6</td><td>CMP0_OUT</td></tr><tr><td>ETI7</td><td>CMP1_OUT</td></tr></table>

## 19.4.8. 计数器运行模式

LPTIMER计数器运行在两种模式下：

1 连续计数模式：LPTIMER计数器由触发事件启动（软件触发或外部触发）后连续运行，直到LPTIMER禁能后才会停止；

◼ 单次计数模式：LPTIMER计数器由触发事件启动（软件触发或外部触发），在计数到CARL

位域（在LPTIMER_CAR寄存器中）定义的值后停止；

## 单次计数模式

将 LPTIMER_CTL0 寄存器中的 SMST 位置 1，可以使能 LPTIMER 计数器的单次计数模式。该模式下，一次新的触发事件将重新启动 LPTIMER 计数器。在计数器启动之后且计数器达到CARL 位域定义的值之前发生的任何触发事件都将被忽略。

如果选择了外部触发来启动 LPTIMER 计数器，则当 SMST 位置 1 时，在计数器停止计数后（CNT 位域的值为 0）到达的每一个外部触发事件都将启动计数器进行新的计数周期计数，具体如 19-6. LPTIMER SMST = 1 32 所示。


图 19-6. LPTIMER 输出（SMST = 1，32 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/96405b1808fb676011f219a032b47cfe59357c3ef7da702a0c3a310c378b782e.jpg)


将 LPTIMER_CTL0 寄存器中的 OMSEL 位置 1，可以使能 LPTIMER 的置位模式。该模式下，LPTIMER 的计数器仅在第一次触发后启动，之后的所有触发事件都将被忽略，具体如 19-7.LPTIMER OMSEL = 1 32 所示。


图 19-7. LPTIMER 输出（OMSEL = 1，32 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/931d6a932e4292b9c5e5c10866882b37dc6d158f8a55eed4a6f1b33f845566c2.jpg)


当 ETMEN[1:0] = 2’b 00 时，软件触发使能，将 SMST 位置 1，LPTIMER 以单次计数模式启动。

## 连续计数模式

将 LPTIMER_CTL0 寄存器中的 CTNMST 位置 1，可以使能 LPTIMER 计数器的连续计数模式。

如果选择了外部触发来启动 LPTIMER 计数器，则在 CTNMST 为置 1 之后到达的外部触发事件将启动计数器的连续计数模式，在 LPTIMER 启动后到达的任何触发事件都将被忽略，具体如 19-8. LPTIMER CTNMST = 1 32 所示。

当 ETMEN[1:0] = 2’b 00 时，软件触发使能，将 CTNMST 位置 1，LPTIMER 以连续计数模式启动。


图 19-8. LPTIMER 输出（CTNMST = 1，32 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/9a00bb43a73802bf813de87cbc97b97e41136e1df6439ca80384e66a6d50260a.jpg)


只有当 LPTIMER 使能（LPTEN=1）时，才能修改 SMST 位和 CTNMST 位，单次计数模式和连续计数模式可以实时进行修改。

若 LPTIMER 工作在连续计数模式，将 SMST 位置 1 后将切换到单次计数模式。计数器计数到CARL 位域定义的值之后将停止计数。

若 LPTIMER 工作在单次计数模式，将 CTNMST 位置 1 后将切换到连续计数模式。计数器计数到 CARL 位域定义的值之后将重新开始计数。

## 19.4.9. 输出模式

通过配置 LPTIMER_CARL 寄存器和 LPTIMER_CMPV 寄存器，LPTIMER 可以输出几种不同的波形。

LPTIMER 可以输出以下 3 种波形：

◼ PWM模式：当LPTIMER_CNT的值和LPTIMER_CMPV寄存器的值匹配时，LPTIMER输出置位。当LPTIMER_CNT的值和LPTIMER_CAR寄存器的值匹配时，LPTIMER输出复位；

◼ 单脉冲模式：输出波形与PWM模式的第一个脉冲相同，之后始终输出复位；

1 置位模式：输出波形与单脉冲模式类似，输出保持为信号的最后电平（具体由LPTIMER_CTL0寄存器中的OPSEL位确定）。

这三种输出模式都要求 LPTIMER_CAR 寄存器的值大于 LPTIMER_CMPV 寄存器的值。

LPTIMER_CTL0 寄存器中的 OMSEL 位用于选择这三种输出模式。

■ OMSEL = 0：LPTIMER输出为PWM模式或单脉冲模式（具体由CTNMST位或SPMST位配置）；

◼ OMSEL = 1：LPTIMER输出置位模式。

OPSEL 位用于配置 LPTIMER 的输出极性，修改该位立即生效。因此，在使能 LPTIMER 之前，只要修改极性配置位，输出默认值就会立即改变。

LPTIMER 输出波形的最大频率为 LPTIMER 时钟频率的二分之一， 19-9. LPTIMER_OOPSEL=0/1 32 所示为 LPTIMER 输出的三种波形，和 OPSEL 位的值对输出波形极性的影响。


图 19-9. LPTIMER_O 输出（OPSEL=0/1，32 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/2ffb93d6ec05b434fc3bf2d7834150b1f92bce97a3a0c2bf80ef8a8ed83fde75.jpg)


## 19.4.10. 超时模式

将 TIMEOUT 位置 1，可以通过在选定触发输入上检测到的有效边沿来复位 LPTIMER。第 1个触发事件将用于启动 LPTIMER，之后的触发事件将复位和重新启动 LPTIMER。

LPTIMER 可以实现低功耗的超时模式，超时值可由 LPTIMER_CMPV 寄存器的值进行配置。

在配置好的比较寄存器值范围内若没有触发发生，当计数器计数到比较寄存器值时，将产生比较匹配中断唤醒 MCU。


图 19-10. LPTIMER 超时模式（32 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/8ec973ea882b561d5226b03249778f580f3315ae8a8fdc011fa23e9cf8e4c0d3.jpg)


## 19.4.11. 译码器模式

LPTIMER由两种译码器模式：

◼ 译 码 器 模 式 0 ： LPTIMER_IN0 和 LPTIMER_IN1 输 入 正 交 信 号 ， 当 DECMEN=1 且DECMSEL=0使能该模式；

◼ 译 码 器 模 式 1 ： LPTIMER_IN0 和 LPTIMER_IN1 输 入 非 交 信 号 ， 当 DECMEN=1 且DECMSEL=1使能该模式。

## 译码器模式0

译码器模式 0 用于 LPTIMER_IN0 和 LPTIMER_IN1 输入为正交信号的情况，两个正交信号相互作用产生计数。

首先，将 CTNMST 位置 1 使能连续计数模式，同时 DECMEN 位置 1 使能译码器模式。设置DECMSEL = 0 选择译码器模式 0，然后设置 CKPSEL[1:0] = 2b’00、2b’01 或 2b’10 来选择计数器上升沿、下降沿或双边沿计数。

在 IN0F（LPTIMER_IN0 滤波信号）信号和 IN1F（LPTIMER_IN1 滤波信号）信号电平变化期间，硬件会自动改变计数方向。计数方向变化机制如 19-3.所示。译码器可以看作是一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动重载值之间连续的计数。

因此，必须在计数器计数之前配置 LPTIMER_CAR 寄存器。

当计数器计数方向改变时，相应的标志位会置 1。当计数器从向上计数改为向下计数时，DOWNIF 位置 1；当计数器从向下计数改为向上计数时，UPIF 位置 1。当寄存器中的 DOWNIE

= 1 或 UPIE = 1 时，相应的中断产生。


表 19-3. 计数方向与译码器信号之间的关系


<table><tr><td rowspan="2">计数模式(CKPSEL[1:0])</td><td rowspan="2">电平</td><td colspan="2">INOF</td><td colspan="2">IN1F</td></tr><tr><td>上升沿</td><td>下降沿</td><td>上升沿</td><td>下降沿</td></tr><tr><td rowspan="4">上升沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>向上</td><td>-</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>向下</td><td>-</td></tr><tr><td>IN1F=1</td><td>向下</td><td>-</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>向上</td><td>-</td><td>x</td><td>x</td></tr><tr><td rowspan="4">下降沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>-</td><td>向下</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>-</td><td>向上</td></tr><tr><td>IN1F=1</td><td>-</td><td>向上</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>-</td><td>向下</td><td>x</td><td>x</td></tr><tr><td rowspan="4">双边沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>向上</td><td>向下</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>向下</td><td>向上</td></tr><tr><td>IN1F=1</td><td>向下</td><td>向上</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>向上</td><td>向下</td><td>x</td><td>x</td></tr></table>


注意：“-”是不计数；“x”是不可能。


19-11. 0 和 19-12. 0分别给出了上升沿计数和下降沿计数的示例。


图 19-11. 计数器运行在译码器模式 0（上升沿计数）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/3620e713adde1f734edd0950b0958adffe8e68c3232847e4c21e32fcacbf7d40.jpg)



图 19-12. 计数器运行在译码器模式 0（下降沿计数）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/eaff08488e050a63ae3f2fbf5b5b7f5a9e71a11b387e3d6e8d84453dad0ea902.jpg)


## 译码器模式 1

译码器模式 0 用于 LPTIMER_IN0 和 LPTIMER_IN1 输入为非交信号的情况，两个非交信号相互作用产生计数。

首先，将 CTNMST 位置 1 使能连续计数模式，同时 DECMEN 位置 1 使能译码器模式。设置DECMSEL = 1 选择译码器模式 1，然后设置 CKPSEL[1:0] = 2b’00、2b’01 来选择LPTIMER_IN0 和 LPTIMER_IN1 输入同相或反相。

当 IN0F 信号和 IN1F 信号依次出现两个不重叠脉冲时，计数器增计数一次。 19-13.1 所示在译码器模式 1 下正确计数的信号波形时序图。IN0F 信号和IN1F 信号的高电平不重叠。

译码器可以看作是一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动重载值之间连续的计数。因此，必须在计数器计数之前配置 LPTIMER_CAR 寄存器。


图 19-13. 计数器运行在译码器模式 1（同相）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/8be17af2fd8c5bbdb82f13e31645a5537c9ac10b0ad2d0ea7fc5c4e52678b494.jpg)


当 IN0F 信号和 IN1F 信号波形不满足 19-13. 1 所示的时序关系时，计数器不能计数。根据两个信号输入波形的情况，相应的标志位（IN1EIF，IN0EIF，INRFOEIF，INHLOEIF）将置位，若 LPTIMER_INTEN 寄存器中的 IN1EIE 位、IN0EIE 位、INRFOEIE 位和 INHLOEIE 位置 1，则将产生相应的中断。


图 19-14. 计数器运行在译码器模式 1（同相，IN1EIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/ac039e6d1fb6fd341349e190b3e1a41864781e9883ecce1a3bca3db4c7bd9fe4.jpg)



图 19-15. 计数器运行在译码器模式 1（同相，IN0EIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/7cc03c8346efe1ba77d9f94dcd969c0177908a9a8b516bfd20a8633b369d3fa4.jpg)



图 19-16. 计数器运行在译码器模式 1（同相，INRFOEIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/e68a580e12338d64a3f45ed1f3bc725133358fbc0e3a1ce0808224d5d9daf93d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/ee26d6a4f8d348fdc83bc95760021e2fe634fd472ddbe6da1ea979e347b469dc.jpg)



图 19-17. 计数器运行在译码器模式 1（同相，INHLOEIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/6232be3c613720dd566c37a5aea50f36007678c5967d9e14bca86658f2fc339b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/05e7cb6c509008034660089e7cc8bc9d43aa61b6dfa9ba5a5a53d70ff15864b5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/9ad25014ebaaa33c2e9378fa8a4f3d68cd375325e27e849fdddcc8d369f746e5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/b4ebc877-242d-4e50-8072-e3ef8caf304f/b3a3dadbe481d275b23f6d792c810b01f8187cc32b53249920ef8401dc3667fc.jpg)



注意，LPTIMER 使用译码器模式时，还应提供一个内部时钟信号 $( \mathsf { C K S S E L } = 0 )$ ），且该时钟信号不能进行预分频 $( \mathsf { P S C } [ 2 : 0 ] = 0 0 0 )$ ）。在这种情况下，内部时钟信号的频率至少是外部时钟


信号频率的四倍。

## 19.4.12. 寄存器更新操作

LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器在 APB 总线完成写操作之后立即更新，或当 LPTIMER 启动后在当前周期完成后更新。SHWEN 位用于配置 LPTIMER_CAR 寄存器和LPTIMER_CMPV 寄存器的更新情况：

◼ SHWEN = 0：在APB总线写操作后，LPTIMER_CAR寄存器和LPTIMER_CMPV寄存器立即更新；

◼ SHWEN = 1：当LPTIMER启动之后，LPTIMER_CAR寄存器和LPTIMER_CMPV寄存器在当前周期完成后更新。

APB 总线和 CK_LPTIMER 使用不同的时钟，因此，APB 写操作和 LPTIMER_CAR 寄存器和LPTIMER_CMPV 寄存器实际使用这些值的时间存在一些延迟。在此延迟时间内，应当避免对这些寄存器的任何其他写操作。

LPTIMER_INTF 寄存器中的 CARUPIF 位和 CMPVUPIF 位分别用于说明 LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器的写操作何时完成。

在写 LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器之后，只有完成了当前的写操作，才能对同一寄存器进行新的写操作。在 CMPVUPIF 标志位和 CARUPIF 标志位分别置 1 前，任何连续的写操作将造成不可预测的结果。

## 19.4.13. 低功耗模式

LPTIMER 具有多种时钟源，可以在除待机模式（Standby mode）以外的所有功耗模式下保持运行。LPTIMER 可以将系统从低功耗模式唤醒，非常适合于以极低的功耗实现超时模式的场合。


表 19-4. LPTIMER 工作在低功耗模式


<table><tr><td>模式</td><td>描述</td></tr><tr><td>睡眠模式</td><td>正常运行,LPTIMER的中断会使设备退出睡眠模式</td></tr><tr><td>运行2模式</td><td>正常运行</td></tr><tr><td>睡眠2模式</td><td>正常运行,LPTIMER的中断会使设备退出低功耗睡眠模式</td></tr><tr><td>深度睡眠0/1模式</td><td>当LPTIMER由LXTAL或内部低速晶振提供时钟时,LPTIMER的中断会使设备退出深度睡眠0/1模式。</td></tr><tr><td>深度睡眠2模式</td><td>LPTIMER的中断会使设备退出深度睡眠模式2</td></tr></table>

## 19.4.14. 中断

若在 LPTIMER_INTEN 寄存器中使能了相应的位，下面的事件可以产生中断或唤醒事件：

◼ LPTIMER_IN1错误

◼ LPTIMER_IN0错误

◼ LPTIMER_IN0和LPTIMER_IN1下降沿和上升沿重叠错误

◼ LPTIMER_IN0和LPTIMER_IN1高电平重叠错误

◼ LPTIMER_Inx（x=0,1）高电平计数器溢出

◼ 输入高电平计数最大值寄存器更新中断标志位

◼ LPTIMER计数器由向上计数改为向下计数

◼ LPTIMER计数器由向下计数改为向上计数

◼ 计数器自动重载寄存器更新

◼ 比较寄存器更新

◼ 外部触发边沿事件

◼ 计数器自动重载寄存器匹配

◼ 比较寄存器匹配

如果 LPTIMER_INTF 寄存器中的中断标志位在相应的中断使能位置 1（LPTIMER_INTEN 寄存器中）前置位了，则该中断无效。


表 19-5. LPTIMER 中断事件


<table><tr><td>中断事件</td><td>描述</td></tr><tr><td>LPTIMER_IN1错误</td><td>当LPTIMER_IN1信号不在LPTIMER_IN0信号的两个连续上升沿之间发生跳变时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0错误</td><td>当LPTIMER_IN0信号不在LPTIMER_IN1信号的两个连续上升沿之间发生跳变时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0和LPTIMER_IN1下降沿和上升沿重叠</td><td>当LPTIMER_IN0下降沿和LPTIMER_IN1上升沿同时发生或者LPTIMER_IN0上升沿和LPTIMER_IN1下降沿同时发生时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0和LPTIMER_IN1高电平重叠</td><td>当LPTIMER_IN0和LPTIMER_IN1的高电平重叠时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_Inx(x=0,1)高电平计数器溢出</td><td>当LPTIMER_Inx的高电平计数器与外部输入高电平计数最大值寄存器(LPTIMER_INHLCMV)值相等时,该标志位置1。</td></tr><tr><td>输入高电平计数最大值寄存器更新</td><td>当APB总线完成对LPTIMER_INHLCMV寄存器的写操作时,该标志位置1。</td></tr><tr><td>LPTIMER计数器由向上计数改为向下计数</td><td>在译码器模式中,当计数器由向上计数改为向下计数时,该标志位置1。</td></tr><tr><td>LPTIMER计数器由向下计数改为向上计数</td><td>在译码器模式中,当计数器由向下计数改为向上计数时,该标志位置1。</td></tr><tr><td>计数器自动重载寄存器更新</td><td>当APB总线完成对LPTIMER_CAR寄存器的写操作时,该标志位置1。</td></tr><tr><td>比较寄存器更新</td><td>当APB总线完成对LPTIMER_CMPV寄存器的写操作时,该标志位置1。</td></tr><tr><td>外部触发边沿事件</td><td>当外部触发的有效边沿发生时,该标志位置1。</td></tr><tr><td>计数器自动重载寄存器匹配</td><td>当LPTIMER_CNT的值与LPTIMER_CAR寄存器的值相等时,该标志位置1。</td></tr><tr><td>比较寄存器匹配</td><td>当LPTIMER_CNT的值与LPTIMER_CMPV寄存器的值相等时,该标志位置1。</td></tr></table>

## 19.4.15. LPTIMER 调试模式

当Cortex™-M23内核停止时，DBG_CTL1寄存器中相应的LPTIMER_HOLD配置位被置1，

LPTIMER的计数器停止。
