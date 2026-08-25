## 24. 低功耗定时器（LPTIMER）

## 24.1. 简介

LPTIMER 是一个 16 位的定时器，基于多样的时钟源，它能够在除待机模式（Standby mode）以外的所有功耗模式下运行。LPTIMER 提供了灵活的时钟机制，在将功耗降至最低的同时，还可以实现所需的功能和性能。

LPTIMER 可以用作没有内部时钟源的脉冲计数器。LPTIMER 可以将系统从低功耗模式唤醒，非常适合于以极低的功耗实现超时模式的场合。

## 24.2. 主要特征

 计数器宽度：16位

 时钟源可选：

内部时钟源：内部8MHz RC晶振（IRC8M），内部32KHz RC晶振（IRC32K），32.768KHz低速晶振（LXTAL）和APB1时钟（PCLK1）

外部时钟源：来自于LPTIMER_IN0引脚上的时钟源（作为脉冲计数器）

 计数模式：向上计数

 运行模式：连续计数模式或单次计数模式

 可编程的预分频器：3位

 通道输出可配置：可编程的PWM模式，单脉冲模式，置位模式

 自动重装载功能

 中断输出

 可选择的触发：软件触发或硬件输入触发

 译码器模式：译码器模式0和译码器模式1

## 24.3. 结构框图

24-1. LPTIMER 提供了低功耗定时器的内部配置细节。


图 24-1. LPTIMER 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/c02f06306d6d1278526880ba1ce60e0ea108fb7efdc0e41331656f3ca9701f71.jpg)


## 24.4. 功能描述

## 24.4.1. 时钟源配置

LPTIMER 可以由多个时钟源提供时钟，如内部时钟源有：内部 8MHz RC 晶振（IRC8M），内部32KHz RC 晶振（IRC32K），32.768 KHz 低速晶振（LXTAL）和 APB1 时钟（PCLK1），这些时钟源来自于复位和时钟单元 RCU。

LPTIMER 还可以使用外部引脚 LPTIMER_IN0 上的外部时钟信号作为时钟，当使用外部时钟作为时钟源时，LPTIMER 有以下两种配置方式：

Case 0：当LPTIMER由外部信号提供时钟时，还需要APB1或其他晶振（如IRC8M、IRC32K和LXTAL）同时提供内部时钟信号；

 Case 1：LPTIMER的时钟仅由LPTIMER_IN0引脚上外部时钟信号提供。在进入低功耗模式后，所有晶振关闭，此配置可用于实现超时模式或脉冲计数器功能。


图 24-2. LPTIMER 时钟源选择


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/4f64d35329d45f60e0beb1ac654ed5d218c634f5b642962ab55d844c8d403469.jpg)



LPTIMER 可以由内部时钟信号或外部时钟信号（由 LPTIMER_CTL0 寄存器中的 CNTMEN 位和CKSSEL 位控制）驱动。CKSSEL 位用于选择哪个时钟驱动计数器预分频器，默认时钟源为 PCLK1。CNTMEN 位用于选择哪个时钟信号驱动 LPTIMER 计数器。


当 LPTIMER 使用外部时钟信号时，CKPSEL 用于配置计数器的有效边沿。计数器可以由外部时钟的上升沿、下降沿或双边沿更新，具体由 CKPSEL[1:0]位域配置。

需要注意的是，当由外部引脚 LPTIMER_IN0 提供外部时钟信号时，如果有效边沿选择双边沿（CKPSEL=2’b10）或者 LPTIMER_IN0 引脚由数字滤波器采样（ECKFLT≠2’b00），则还需要提供内部时钟信号（Case 0）。在这种情况下，内部时钟信号频率至少是外部时钟频率的 4 倍。

可以根据 CKSSEL 位和 CNTMEN 位的配置，选择以下的时钟模式：

 CKSSEL = 0：LPTIMER时钟由内部时钟信号提供

- 内部时钟模式0（CNTMEN = 0）

LPTIMER由内部时钟信号提供时钟，计数器在内部时钟的每个脉冲进行计数。

内部时钟模式1（CNTMEN = 1）

外部时钟信号（LPTIMER_IN0）由内部时钟进行采样，因此，为了保证不丢失任何事件，外部时钟的变化频率不能超过内部时钟的频率。并且，LPTIMER的内部时钟信号不能预分频（PSC [2:0] = 000）。

##  CKSSEL = 1：LPTIMER时钟由外部时钟信号提供

这种情况下，可以将CNTMEN位置1或清零，LPTIMER不需要使用内部时钟源（除非使能了输入滤波或是选择了双边沿作为外部时钟的有效边沿）。LPTIMER_IN0引脚上的外部信号作为LPTIMER的系统时钟，该情况适用于没有嵌入式晶振的工作情况；

这种情况下，LPTIMER的计数器可以在外部时钟信号的上升沿或下降沿计数，不能在双边沿计数。

由于LPTIMER_IN0引脚上的外部时钟信号也用于驱动LPTIMER的内核逻辑部分，因此，在计数器计数之前会有一些初始延迟（LPTIMER使能之后）。因此，在使能LPTIMER之后，LPTIMER_IN0引脚上的外部时钟信号前5个有效边沿将会丢失。


图 24-3. 内部时钟模式 1（CKSSEL = 0，CNTMEN = 1，PSC[2:0] = 000）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/c8dcd0afe6708aae794ddb7f37ab28c1886cef41444dd7b2ec9426869c72f041.jpg)


## 24.4.2. LPTIMER 使能

LPTIMER_CTL1 寄存器的 LPTEN 位用于使能 LPTIMER 的内核逻辑模块。在 LPTEN 位置 1 后，实际使能 LPTIMER 之前需要延迟两个 LPTIMER_CK 时钟周期。

只有在 LPTIEMR 禁能时，才能修改 LPTIMER_CTL0 和 LPTIMER_INTEN 寄存器（INHLCOIE 位和 HLCMVUPIF 位除外）。

## 24.4.3. 预分频器

预分频器可以将 LPTIMER 的时钟 LPTIMER_CK 除以 2 的乘幂分频为计数器时钟 PSC_CLK。只有在 LPTIEMR 禁能（LPTEN=0）时，才能修改 PSC[2:0]位域。下表列出了所有的分频系数：


表 24-1. 预分频器的分频系数


<table><tr><td>预分频系数</td><td>PSC[2:0]位域</td></tr><tr><td>1/1</td><td>000</td></tr><tr><td>1/2</td><td>001</td></tr><tr><td>1/4</td><td>010</td></tr><tr><td>1/8</td><td>011</td></tr><tr><td>1/16</td><td>100</td></tr><tr><td>1/32</td><td>101</td></tr><tr><td>1/64</td><td>110</td></tr><tr><td>1/128</td><td>111</td></tr></table>

## 24.4.4. 输入滤波

LPTIMER_Inx 引脚上的外部（映射到 GPIO）或内部（映射到片上外设，如比较器）信号需要通过数字滤波器进行滤波，以防止毛刺和噪声干扰在 LPTIMER 中扩散，这可以有效防止误计数和误触发。

在使用数字滤波器之前，需要先给 LPTIMER 提供内部时钟源，这样可以确保滤波器的正确运行。数字滤波器有两种类型：

 第1种：用于保护LPTIMER的外部输入（LPTIMER_IN0/ LPTIMER_IN1），数字滤波器由ECKFLT[1:0]位进行配置；

 第2种：用于保护LPTIMER的触发输入（ETIx），数字滤波器由TFLT[1:0]位进行配置；

注意：相同类型的数字滤波器应该保持相同的配置。

数字滤波器的灵敏度取决于 LPTIMER 输入引脚上连续相同采样的数量，并将信号电平变化视为有效。 24-4. ECKFLT=2’b01 显示了输入滤波器 2 次连续采样的示例。


图 24-4. 输入滤波时序图（ECKFLT=2’b01）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/f295427a019dbedbbf5dd889a5ace2c00070854783f0844fed1d6204db741dea.jpg)


注意：如果没有内部时钟信号，则必须禁能数字滤波器（设置 ECKFLT=0，TFLT=0）。这种情况下，可以使用外部模拟滤波器来保证 LPTIMER 的外部输入不受干扰。

## 24.4.5. 外部输入高电平计数器

将 INHLCEN 位置 1 可以使能外部输入 LPTIMER_Inx 的高电平计数器功能，高电平计数器的时钟由内部时钟 CK_LPTIMER 提供。当 LPTIMER_Inx 引脚上出现高电平时，计数器开始计数，一旦出现低电平，计数器清零。

当高电平计数器的计数值等于 INHLCMVAL 位域（在 LPTIMER_INHLCMV 寄存器中）定义的数值时，LPTIMER_INTF 寄存器中的 INHLCOIF 位由硬件置位。若使能了 LPTIMER_INTEN 寄存器中的 INHLCOIE 位，则会产生中断。可以通过向 INTC 寄存器中的 INHLCOIC 位写 1 来清除INHLCOIF 中断标志位。

24-5. 给出了外部输入高电平计数器的示例。


图 24-5. 外部输入高电平计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/60289c541b889e43560fef1ac1520a1bb7a8824aace63dc6612411240c2ecc88.jpg)


APB 总线和 CK_LPTIMER 使用不同的时钟，因此，APB 写操作和 LPTIMER_INHLCMV 寄存器实际使用这些值的时间存在一些延迟。在此延迟时间内，应当避免对该寄存器的任何其他写操作。

LPTIMER_INTF 寄存器中的 HLCMVUPIF 位用于说明对 LPTIMER_INHLCMV 寄存器的写操作何时完成。

## 24.4.6. 计数器启动

LPTIMER的计数器可以通过软件触发或通过检测8个触发输入上的有效边沿来启动。ETMEN [1:0]位域用于配置 LPTIMER 的触发模式：

■ ETMEN[1:0] = 2’b 00：一旦软件置位CTNMST位或SMST位，LPTIMER的计数器就会启动；

ETMEN[1:0] ≠ 2’b00：ETSEL[2:0]位用于选择8个触发输入中的一个来启动LPTIMER。ETMEN[1:0]位域的其余3个非零值用于配置触发输入所使用的有效边沿。一旦检测到有效边沿，LPTIMER计数器就会启动。

外部触发可视为 LPTIMER 的异步信号，因此，一旦检测到触发信号，为了实现同步，在 LPTIMER开始运行之前需要延迟 2 个计数器时钟周期。如果在 LPTIMER 启动后发生新的触发事件，该触发事件将会被忽略（除非使能了超时模式）。

注意：在置位 SMST 位和 CTNMST 位之前，必须将 LPTEN 位置位。当 LPTEN=0 时，对这些位的任何写操作都将被硬件丢弃。

## 24.4.7. 外部触发映射

LPTIMER 外部触发连接的情况如下 24-2. 所示：


表 24-2. 外部触发映射


<table><tr><td>ETSEL[2:0]</td><td>外部触发映射</td></tr><tr><td>ETI0</td><td>GPIO</td></tr><tr><td>ETI1</td><td>RTC闹钟0</td></tr><tr><td>ETI2</td><td>RTC闹钟1</td></tr><tr><td>ETI3</td><td>RTC_TAMP0</td></tr><tr><td>ETI4</td><td>RTC_TAMP1</td></tr><tr><td>ETI5</td><td>RTC_TAMP2</td></tr><tr><td>ETI6</td><td>CMP0_OUT</td></tr><tr><td>ETI7</td><td>CMP1_OUT</td></tr><tr><td>ETI8</td><td>CMP2_OUT</td></tr><tr><td>ETI9</td><td>CMP3_OUT</td></tr><tr><td>ETI10</td><td>CMP4_OUT</td></tr><tr><td>ETI11</td><td>CMP5_OUT</td></tr><tr><td>ETI12</td><td>CMP6_OUT</td></tr><tr><td>ETI13</td><td>CMP7_OUT</td></tr></table>

## 24.4.8. 计数器运行模式

LPTIMER计数器运行在两种模式下：

连续计数模式：LPTIMER计数器由触发事件启动（软件触发或外部触发）后连续运行，直到LPTIMER禁能后才会停止；

 单次计数模式：LPTIMER计数器由触发事件启动（软件触发或外部触发），在计数到CARL位域（在LPTIMER_CAR寄存器中）定义的值后停止；

## 单次计数模式

将 LPTIMER_CTL0 寄存器中的 SMST 位置 1，可以使能 LPTIMER 计数器的单次计数模式。该模式下，一次新的触发事件将重新启动 LPTIMER 计数器。在计数器启动之后且计数器达到 CARL 位域定义的值之前发生的任何触发事件都将被忽略。

如果选择了外部触发来启动 LPTIMER 计数器，则当 SMST 位置 1 时，在计数器停止计数后（CNT位域的值为 0）到达的每一个外部触发事件都将启动计数器进行新的计数周期计数，具体如 24-6.LPTIMER SMST = 1 16 所示。

当 ETMEN[1:0] = 2’b 00 时，软件触发使能，将 SMST 位置 1，LPTIMER 以单次计数模式启动。


图 24-6. LPTIMER 输出（SMST = 1，16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/21162391974485a792aadcf552baa1dd62f667f741fe5f7e24c40ce6eb9a0df0.jpg)


将 LPTIMER_CTL0 寄存器中的 OMSEL 位置 1，可以使能 LPTIMER 的置位模式。该模式下，LPTIMER 的计数器仅在第一次触发后启动，之后的所有触发事件都将被忽略，具体如 24-7.LPTIMER OMSEL = 1 16 所示。


图 24-7. LPTIMER 输出（OMSEL = 1，16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/527b7a984027d213e2b41f45e9ab3b10b73bc6c9f096b376cf4c86d0f8885066.jpg)


## 连续计数模式

将 LPTIMER_CTL0 寄存器中的 CTNMST 位置 1，可以使能 LPTIMER 计数器的连续计数模式。

如果选择了外部触发来启动 LPTIMER 计数器，则在 CTNMST 为置 1 之后到达的外部触发事件将启动计数器的连续计数模式，在 LPTIMER 启动后到达的任何触发事件都将被忽略，具体如 24-8.LPTIMER CTNMST = 1 16 所示。

当 ETMEN[1:0] = 2’b 00 时，软件触发使能，将 CTNMST 位置 1，LPTIMER 以连续计数模式启动。


图 24-8. LPTIMER 输出（CTNMST = 1，16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/b3b2ea17136e02c462de71ee36c837fd1f041f3d428da20487d26006f4f4cd6a.jpg)


只有当 LPTIMER 使能（LPTEN=1）时，才能修改 SMST 位和 CTNMST 位，单次计数模式和连续计数模式可以实时进行修改。

若 LPTIMER 工作在连续计数模式，将 SMST 位置 1 后将切换到单次计数模式。计数器计数到CARL 位域定义的值之后将停止计数。

若 LPTIMER 工作在单次计数模式，将 CTNMST 位置 1 后将切换到连续计数模式。计数器计数到CARL 位域定义的值之后将重新开始计数。

## 24.4.9. 计数器复位

LPTIMER 的计数器可以通过软件异步或者同步复位为 0。两种复位方式的详情如下：

计数器异步复位：当设置LPTIMER_CTL1寄存器的RDRSTEN位为1时，LPTIMER_CNT寄存器会在每次读访问后被复位为0。

计数器同步复位：LPTIMER计数器可以通过LPTIMER_CTL1寄存器的CNTRST位写1来同步复位。同步复位意味着复位操作需要3个LPTIMER内核时钟周期来同步，当LPTIMER使用异步时钟（与APB时钟异步）来计数时。在同步过程中，计数器依旧保持计数。在计数器复位操作完成后，CNTRST位被硬件自动清零。

注意: 两种复位方式不能同时使用。CNTRST 位只能在已经被硬件清 0 后才能再次写 1。软件需要在试图对 CNTRST 写 1 时检查 CNTRST 是否已经被清零。

## 24.4.10. 输出模式

通过配置 LPTIMER_CARL 寄存器和 LPTIMER_CMPV 寄存器，LPTIMER 可以输出几种不同的波形。

LPTIMER 可以输出以下 3 种波形：

■ PWM模式：当LPTIMER_CNT的值和LPTIMER_CMPV寄存器的值匹配时，LPTIMER输出置

位。当LPTIMER_CNT的值和LPTIMER_CAR寄存器的值匹配时，LPTIMER输出复位；

 单脉冲模式：输出波形与PWM模式的第一个脉冲相同，之后始终输出复位；

 置位模式：输出波形与单脉冲模式类似，输出保持为信号的最后电平（具体由LPTIMER_CTL0寄存器中的OPSEL位确定）。

这三种输出模式都要求 LPTIMER_CAR 寄存器的值大于 LPTIMER_CMPV 寄存器的值。

LPTIMER_CTL0 寄存器中的 OMSEL 位用于选择这三种输出模式。

 OMSEL = 0：LPTIMER输出为PWM模式或单脉冲模式（具体由CTNMST位或SPMST位配置）； OMSEL = 1：LPTIMER输出置位模式。

OPSEL 位用于配置 LPTIMER 的输出极性，修改该位立即生效。因此，在使能 LPTIMER 之前，只要修改极性配置位，输出默认值就会立即改变。

LPTIMER 输出波形的最大频率为 LPTIMER 时钟频率的二分之一， 24-9. LPTIMER_OOPSEL=0/1 16 所示为 LPTIMER 输出的三种波形，和 OPSEL 位的值对输出波形极性的影响。


图 24-9. LPTIMER_O 输出（OPSEL=0/1，16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/0672a94a4495a7cdf63b8b8c51bfa1ab1721e3a0856f72a3802266d4fdd245f7.jpg)


## 24.4.11. 超时模式

将 TIMEOUT 位置 1，可以通过在选定触发输入上检测到的有效边沿来复位 LPTIMER。第 1 个触发事件将用于启动 LPTIMER，之后的触发事件将复位和重新启动 LPTIMER。

LPTIMER 可以实现低功耗的超时模式，超时值可由 LPTIMER_CMPV 寄存器的值进行配置。

在配置好的比较寄存器值范围内若没有触发发生，当计数器计数到比较寄存器值时，将产生比较匹配中断唤醒 MCU。


图 24-10. LPTIMER 超时模式（16 位）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/570f9c7c910a56a787e983a48d0f8234c347d31da91752abe2599885f60d18c8.jpg)


## 24.4.12. 译码器模式

LPTIMER由两种译码器模式：

 译码器模式0：LPTIMER_IN0和LPTIMER_IN1输入正交信号，当DECMEN=1且DECMSEL=0使能该模式；

 译码器模式1：LPTIMER_IN0和LPTIMER_IN1输入非交信号，当DECMEN=1且DECMSEL=1使能该模式。

## 译码器模式 0

译码器模式 0 用于 LPTIMER_IN0 和 LPTIMER_IN1 输入为正交信号的情况，两个正交信号相互作用产生计数。

首先，将 CTNMST 位置 1 使能连续计数模式，同时 DECMEN 位置 1 使能译码器模式。设置DECMSEL = 0 选择译码器模式 0，然后设置 CKPSEL[1:0] = 2’b00、2’b01 或 2’b10 来选择计数器上升沿、下降沿或双边沿计数。

在 IN0F（LPTIMER_IN0 滤波信号）信号和 IN1F（LPTIMER_IN1 滤波信号）信号电平变化期间，硬件会自动改变计数方向。计数方向变化机制如 24-3. 所示。译码器可以看作是一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动重载值之间连续的计数。

因此，必须在计数器计数之前配置 LPTIMER_CAR 寄存器。

当计数器计数方向改变时，相应的标志位会置 1。当计数器从向上计数改为向下计数时，DOWNIF位置 1；当计数器从向下计数改为向上计数时，UPIF 位置 1。当寄存器中的 DOWNIE = 1 或 UPIE= 1 时，相应的中断产生。


表 24-3. 计数方向与译码器信号之间的关系


<table><tr><td rowspan="2">计数模式(CKPSEL[1:0])</td><td rowspan="2">电平</td><td colspan="2">INOF</td><td colspan="2">IN1F</td></tr><tr><td>上升沿</td><td>下降沿</td><td>上升沿</td><td>下降沿</td></tr><tr><td rowspan="4">上升沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>向上</td><td>-</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>向下</td><td>-</td></tr><tr><td>IN1F=1</td><td>向下</td><td>-</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>向上</td><td>-</td><td>x</td><td>x</td></tr><tr><td rowspan="4">下降沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>-</td><td>向下</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>-</td><td>向上</td></tr><tr><td>IN1F=1</td><td>-</td><td>向上</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>-</td><td>向下</td><td>x</td><td>x</td></tr><tr><td rowspan="4">双边沿计数</td><td>INOF=1</td><td>x</td><td>x</td><td>向上</td><td>向下</td></tr><tr><td>INOF=0</td><td>x</td><td>x</td><td>向下</td><td>向上</td></tr><tr><td>IN1F=1</td><td>向下</td><td>向上</td><td>x</td><td>x</td></tr><tr><td>IN1F=0</td><td>向上</td><td>向下</td><td>x</td><td>x</td></tr></table>


注意：“-”是不计数；“x”是不可能。


图24-11.计数器运行在译码器模式0（上升沿计数）和图24-12. 计数器运行在译码器模式0（下降分别给出了上升沿计数和下降沿计数的示例。


图 24-11. 计数器运行在译码器模式 0（上升沿计数）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/b72a1101dcca9877ddd5ba783525f5c59a7623e3f658634c3f4fea46ede8d44c.jpg)



图 24-12. 计数器运行在译码器模式 0（下降沿计数）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/d0ef067e86b2c1b48973352858ed03c2d7907c928565ada0c0f607e7295d6996.jpg)


## 译码器模式 1

译码器模式 1 用于 LPTIMER_IN0 和 LPTIMER_IN1 输入为非交信号的情况，两个非交信号相互作用产生计数。

首先，将 CTNMST 位置 1 使能连续计数模式，同时 DECMEN 位置 1 使能译码器模式。设置DECMSEL = 1 选择译码器模式 1，然后设置 CKPSEL[1:0] = 2‘b00、2’b01 来选择 LPTIMER_IN0和 LPTIMER_IN1 输入同相或反相。

当 IN0F 信号和 IN1F 信号依次出现两个不重叠脉冲时，计数器增计数一次。 24-13.1 所示在译码器模式 1 下正确计数的信号波形时序图。IN0F 信号和 IN1F信号的高电平不重叠。

译码器可以看作是一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动重载值之间连续的计数。因此，必须在计数器计数之前配置 LPTIMER_CAR 寄存器。


图 24-13. 计数器运行在译码器模式 1（同相）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/c5128d415cd6ac788fd2bd017290962778dd1afc4c5ddeae6c6e38bf2bae038b.jpg)


当 IN0F 信号和 IN1F 信号波形不满足 24-13. 1 所示的时序关系时，计数器不能计数。根据两个信号输入波形的情况，相应的标志位（IN1EIF，IN0EIF，INRFOEIF，INHLOEIF）将置位，若 LPTIMER_INTEN 寄存器中的 IN1EIE 位、IN0EIE 位、INRFOEIE 位和INHLOEIE 位置 1，则将产生相应的中断。


图 24-14. 计数器运行在译码器模式 1（同相，IN1EIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/7338e60b9001b236e29b934e05d9f48d2ca9104396fa6a07335c10276c753b80.jpg)



图 24-15. 计数器运行在译码器模式 1（同相，IN0EIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/18c7e97a4c40227314e6174434b8c4ce5a61781bc80438e6bff345e9049cf200.jpg)



图 24-16. 计数器运行在译码器模式 1（同相，INRFOEIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/dd35b9a2442768967d68bac97b36ea5fcf3a0c6daedc548ff7f401bc07e0cf84.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/f8b4411a832cbbaa2b3b57e3fecc27f20325e82cfc2b2329f1bd4038a399d83f.jpg)



图 24-17. 计数器运行在译码器模式 1（同相，INHLOEIF）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/dc89dce430b8257136c8cce19af1f1d7eee2482dfa54e01a11f7d9396e3df8b0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/db5156b7bf177b863bd989fddbcb3e7fa609385a10080b172e90c1e83a3f960e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/286f9196b2ae343f461fedc133ecd73ce91a605279e6168e341f513a7476b5ab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/fe41be0ba17f40efd7e5943149be8b81fcf4b81b77315419c14a7a4e89c5309c.jpg)



注意，LPTIMER 使用译码器模式时，还应提供一个内部时钟信号（CKSSEL = 0），且该时钟信号不能进行预分频（PSC[2:0] = 000）。在这种情况下，内部时钟信号的频率至少是外部时钟信号频率的四倍。


## 24.4.13. 寄存器更新操作

LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器在 APB 总线完成写操作之后立即更新，或当LPTIMER 启动后在当前周期完成后更新。SHWEN 位用于配置 LPTIMER_CAR 寄存器和LPTIMER_CMPV 寄存器的更新情况：

 SHWEN = 0：在APB总线写操作后，LPTIMER_CAR寄存器和LPTIMER_CMPV寄存器立即更新；

 SHWEN = 1：当LPTIMER启动之后，LPTIMER_CAR寄存器和LPTIMER_CMPV寄存器在当前周期完成后更新。

APB 总线和 CK_LPTIMER 使用不同的时钟，因此，APB 写操作和 LPTIMER_CAR 寄存器和LPTIMER_CMPV 寄存器实际使用这些值的时间存在一些延迟。在此延迟时间内，应当避免对这些寄存器的任何其他写操作。

LPTIMER_INTF 寄存器中的 CARUPIF 位和 CMPVUPIF 位分别用于说明 LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器的写操作何时完成。

在写 LPTIMER_CAR 寄存器和 LPTIMER_CMPV 寄存器之后，只有完成了当前的写操作，才能对同一寄存器进行新的写操作。在 CMPVUPIF 标志位和 CARUPIF 标志位分别置 1 前，任何连续的写操作将造成不可预测的结果。

## 24.4.14. 低功耗模式

LPTIMER 具有多种时钟源，可以在除待机模式（Standby mode）以外的所有功耗模式下保持运行。LPTIMER 可以将系统从低功耗模式唤醒，非常适合于以极低的功耗实现超时模式的场合。


表 24-4. LPTIMER 工作在低功耗模式


<table><tr><td>模式</td><td>描述</td></tr><tr><td>睡眠模式</td><td>正常运行,LPTIMER的中断会使设备退出睡眠模式</td></tr><tr><td>深度睡眠模式</td><td>当LPTIMER由LXTAL或内部低速RC振荡器提供时钟时,LPTIMER的中断会使设备退出深度睡眠模式。</td></tr></table>

## 24.4.15. 中断

若在 LPTIMER_INTEN 寄存器中使能了相应的位，下面的事件可以产生中断或唤醒事件：

 LPTIMER_IN1错误

 LPTIMER_IN0错误

 LPTIMER_IN0和LPTIMER_IN1下降沿和上升沿重叠错误

 LPTIMER_IN0和LPTIMER_IN1高电平重叠错误

 LPTIMER_Inx（x=0,1）高电平计数器溢出

 输入高电平计数最大值寄存器更新中断标志位

 LPTIMER计数器由向上计数改为向下计数

 LPTIMER计数器由向下计数改为向上计数

 计数器自动重载寄存器更新

 比较寄存器更新

 外部触发边沿事件

 计数器自动重载寄存器匹配

 比较寄存器匹配

如果 LPTIMER_INTF 寄存器中的中断标志位在相应的中断使能位置 1（LPTIMER_INTEN 寄存器中）前置位了，则该中断无效。


表 24-5. LPTIMER 中断事件


<table><tr><td>中断事件</td><td>描述</td></tr><tr><td>LPTIMER_IN1错误</td><td>当LPTIMER_IN1信号不在LPTIMER_IN0信号的两个连续上升沿之间发生跳变时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0错误</td><td>当LPTIMER_IN0信号不在LPTIMER_IN1信号的两个连续上升沿之间发生跳变时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0和LPTIMER_IN1下</td><td>当LPTIMER_IN0下降沿和LPTIMER_IN1上升沿同时发生或者</td></tr><tr><td>降沿和上升沿重叠</td><td>LPTIMER_IN0上升沿和LPTIMER_IN1下降沿同时发生时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_IN0和LPTIMER_IN1高电平重叠</td><td>当LPTIMER_IN0和LPTIMER_IN1的高电平重叠时,该标志位置1(仅用于译码器模式1)。</td></tr><tr><td>LPTIMER_Inx(x=0,1)高电平计数器溢出</td><td>当LPTIMER_Inx的高电平计数器与外部输入高电平计数最大值寄存器(LPTIMER_INHLCMV)值相等时,该标志位置1。</td></tr><tr><td>输入高电平计数最大值寄存器更新</td><td>当APB总线完成对LPTIMER_INHLCMV寄存器的写操作时,该标志位置1。</td></tr><tr><td>LPTIMER计数器由向上计数改为向下计数</td><td>在译码器模式中,当计数器由向上计数改为向下计数时,该标志位置1。</td></tr><tr><td>LPTIMER计数器由向下计数改为向上计数</td><td>在译码器模式中,当计数器由向下计数改为向上计数时,该标志位置1。</td></tr><tr><td>计数器自动重载寄存器更新</td><td>当APB总线完成对LPTIMER_CAR寄存器的写操作时,该标志位置1。</td></tr><tr><td>比较寄存器更新</td><td>当APB总线完成对LPTIMER_CMPV寄存器的写操作时,该标志位置1。</td></tr><tr><td>外部触发边沿事件</td><td>当外部触发的有效边沿发生时,该标志位置1。</td></tr><tr><td>计数器自动重载寄存器匹配</td><td>当LPTIMER_CNT的值与LPTIMER_CAR寄存器的值相等时,该标志位置1。</td></tr><tr><td>比较寄存器匹配</td><td>当LPTIMER_CNT的值与LPTIMER_CMPV寄存器的值相等时,该标志位置1。</td></tr></table>

## 24.4.16. LPTIMER 调试模式

当Cortex™-M33内核停止时，DBG_CTL1寄存器中相应的LPTIMER_HOLD配置位被置1，LPTIMER的计数器停止。
