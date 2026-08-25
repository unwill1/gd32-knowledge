## 18.1. 高级定时器（TIMERx，x=0）

## 18.1. 1. 简介

高级定时器（TIMER0）是四通道定时器，支持输入捕获和输出比较。可以产生 PWM 信号控制电机和电源管理。高级定时器含有一个 16 位无符号计数器。

高级定时器是可编程的，可以用来计数，其外部事件可以驱动其他定时器。

高级定时器包含了一个死区时间插入模块，非常适合电机控制。

定时器和定时器之间是相互独立，但是它们的计数器可以被同步在一起形成一个更大的定时器。

## 18.1.2. 主要特征

◼ 总通道数：4；

◼ 计数器宽度：16位；

◼ 定时器时钟源可选：内部时钟，内部触发，外部输入，外部触发；

◼ 多种计数模式：向上计数，向下计数和中央计数；

◼ 正交译码器接口：用来追踪运动和分辨旋转方向和位置；

◼ 霍尔传感器接口：用来做三相电机控制；

◼ 可编程的预分频器：16位。运行时可以被改变；

◼ 每个通道可配置：输入捕获模式，输出比较模式，可编程的PWM模式，单脉冲模式；

◼ 可编程的死区时间；

◼ 自动重装载功能；

◼ 可编程的计数器重复功能；

◼ 中止输入功能；

◼ 中断输出和DMA请求：更新事件，触发事件，比较/捕获事件和中止事件；

◼ 多个定时器的菊链使得一个定时器可以同时启动多个定时器；

◼ 定时器的同步允许被选择的定时器在同一个时钟周期开始计数；

◼ 定时器主/从管理。

## 18.1.3. 结构框图

18-1. 提供了高级定时器的内部配置细节。


图 18-1. 高级定时器结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/e7793549045ac5d6cd06aa985cba4db0e08058b2c41cdf1fdd95aa8b0ae1fe23.jpg)


## 18.1.4. 功能说明

## 时钟源选择

高级定时器的时钟源可以是内部时钟源CK_TIMER，或者是由TSCFGy[3:0]位确定的时钟源，TSCFGy[3:0]位于 SYSCFG_TIMER0CFG，（y=0,1…7）。

◼ TSCFGy[3:0] =4’b0000，TSCFGy[3:0]位于SYSCFG_TIMER0CFG，（y=0,1…7），定时器选择内部时钟源（连接到RCU模块的CK_TIMER）

当 TSCFGy[3:0] =4’b0000，TSCFGy[3:0]位于 SYSCFG_TIMER0CFG，（y=0,1…7），默认用来驱动计数器预分频器的是内部时钟源 CK_TIMER。当 CEN 置位，CK_TIMER 经过预分频器（预分频值由 TIMERx_PSC 寄存器确定）产生 PSC_CLK。

这种模式下，驱动预分频器计数的 TIMER_CK 等于来自于 RCU 模块的 CK_TIMER。

◼ 如果TSCFGy[3:0] !=4’b0000，TSCFGy[3:0]位于SYSCFG_TIMER0CFG，（y=0,1,2,6），预分频器被其他时钟源（由TSCFG6[3:0]区域选择）驱动，更多细节在下文说明，当TSCFGy[3:0]（y=3,4,5）设置为有效值时，计数器预分频器时钟源由内部时钟TIMER_CK驱动。


图 18-2. 内部时钟分频为 1时，正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/05f510bdf95809ef2b69d58c0849f00b6dd43eab99bdc64fd2372f0ef51b8e15.jpg)


◼ TSCFG6[3:0] !=4’b0000（外部时钟模式0），定时器选择外部输入引脚作为时钟源。

计数器预分频器可以在 TIMERx_CH0/ TIMERx_CH1 引脚的每个上升沿或下降沿计数。这种模式可以通过设置 TSCFG6[3:0]为 0x5，0x6 或 0x7 来选择。

计数器预分频器也可以在内部触发信号 ITI0/1/2/3 的上升沿计数。这种模式可以通过设置TSCFG6[3:0]为 0x1，0x2，0x3 或者 0x4。

◼ SMC1=1’b1（外部时钟模式1），定时器选择外部输入引脚ETI作为时钟源。

计数器预分频器可以在外部引脚 ETI 的每个上升沿或下降沿计数。这种模式可以通过设置TIMERx_SMCFG寄存器中的SMC1位为1来选择。另一种选择ETI信号作为时钟源方式是，设置 TSCFG6[3:0]为 0x8。注意 ETI 信号是通过数字滤波器采样 ETI 引脚得到的。如果选择ETI 信号为时钟源，触发控制器包括边沿监测电路将在每个 ETI 信号上升沿产生一个时钟脉冲来为计数器预分频器提供时钟。

## 预分频器

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 18-3. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/ecfdc27e6a859e29530d2cdb836a505eee70bb61c96f00b91462e270a4e7ac53.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数。如果设置了重复计数器，在（TIMERx_CREP+1）次上溢后产生更新事件，否则在每次上溢时都会产生更新事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数寄存器，自动重载寄存器，预分频寄存器）都将被更新。

18-4. PSC=0/1 和 18-5. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x63 时，计数器在不同预分频因子下的行为。


图 18-4. 向上计数时序图，PSC=0/1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/40cee38b6f35c6629d7c49dcc27c98d46bc7c9cd90fff975c3bb62b01bf8329c.jpg)



图 18-5. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/022ed9946d6f8a6d403d7d27890aa66a68e6d5045789d9e96fc3b61cf9203720.jpg)


## 向下计数模式

在这种模式，计数器的计数方向是向下计数。计数器从自动加载值（定义在 TIMERx_CAR 寄存器中）向下连续计数到 0。一旦计数器计数到 0，计数器会重新从自动加载值开始计数。如果设置了重复计数器，在（TIMERx_CREP+1）次下溢后产生更新事件，否则在每次下溢时都会产生更新事件。在向下计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 1。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被初始化为自动加载值，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

18-6. PSC=0/1 和 18-7. TIMERx_CAR给出了一些例子，当 TIMERx_CAR=0x63 时，计数器在不同时钟频率下的行为。


图 18-6. 向下计数时序图，PSC=0/1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/ed5f7052a5c22d1729eb41e60cc1b2449a8a33b248c8eca0b7046d0dec69b1c5.jpg)



图 18-7. 向下计数时序图，在运行时改变 TIMERx_CAR 寄存器值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/45fd09fcdf0ac41116c88a7ae5bf6b7f4d3944b65340ee2a4109b583ecb946a2.jpg)


## 中央对齐模式

在中央对齐模式下，计数器交替的从 0 开始向上计数到自动加载值，然后再向下计数到 0。向上计数模式中，定时器模块在计数器计数到（TIMERx_CREP -1）时产生一个上溢事件；向下计数模式中，定时器模块在计数器计数到 1 时产生一个下溢事件。在中央计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 只读，表明计数方向。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以初始化计数值为 0，并产生一个更新事件，而无需考虑计数器在中央模式下是向上计数还是向下计数。

上溢或者下溢时，TIMERx_INTF 寄存器中的 UPIF 位都会被置 1。但是 ChxIF 位是否置 1 与TIMERx_CTL0寄存器中CAM的值有关。具体细节参考 18-8. 。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（重复计数器，自动重载寄存器，预分频寄存器）都将被更新。

18-8.            给 出 了 一 些 例 子 ， 当 TIMERx_CAR=0x63，TIMERx_PSC=0x0 时，计数器的时序图。


图 18-8. 中央计数模式计数器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/ff9cfef7998423de6b652751dfee1550395842b8f6ac9f7dc520d92a21c27bbd.jpg)


## 重复计数器

重复计数器是用来在（N+1）个计数周期之后产生更新事件，更新定时器的寄存器，N 为TIMERx_CREP 寄存器的 CREP 位的值。向上计数模式下，重复计数器在每次计数器上溢时递减；向下计数模式下，重复计数器在每次计数器下溢时递减；在中央对齐模式下，重复计数器在计数器上溢和下溢时递减。

将 TIMERx_SWEVG 寄存器的 UPG 位置 1 可以重载 TIMERx_CREP 寄存器中 CREP 的值并产生一个更新事件。

在中央对齐模式下，对于 CREP 为奇数值，更新事件发生在上溢或下溢的时刻取决于奇数值写入 CREP 寄存器和计数器启动的时刻。如果在计数器启动前写入 CREP 寄存器，则在上溢时产生更新事件。如果在计数器启动后写入 CREP 寄存器，则在下溢时产生更新事件。


图 18-9. 中央计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/df50b203333650bb6347d28ff7689e36be8a35d859e55b1f3eb7ccc849db3b64.jpg)



图 18-10. 在向上计数模式下计数器重复时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/6b099e4bb597d9a8d048817800e4316324adb968b84e659b9affe617ccf503d7.jpg)



图 18-11. 在向下计数模式下计数器重复时序图


<table><tr><td>TIMER_CK</td><td></td></tr><tr><td>CEN</td><td></td></tr><tr><td>CNT_CLK</td><td></td></tr><tr><td>CNT_REG 03</td><td>02 01 00 63 62 ... 01 00 63 62 ... 01 00 63 62 ... 01 00 63 62 ... 01 00 63 62</td></tr><tr><td>Underflow</td><td></td></tr><tr><td>Overflow</td><td></td></tr><tr><td>TIMERx_CREP = 0x0</td><td></td></tr><tr><td>UPIF</td><td></td></tr><tr><td>TIMERx_CREP = 0x1</td><td></td></tr><tr><td>UPIF</td><td></td></tr><tr><td>TIMERx_CREP = 0x2</td><td></td></tr><tr><td>UPIF</td><td></td></tr></table>

## 捕获/比较通道

高级定时器拥有四个独立的通道用于捕获输入或比较输出是否匹配。每个通道都围绕一个通道捕获比较寄存器建立，包括一个输入级，通道控制器和输出级。

## 输入捕获模式

输入捕获模式允许通道测量一个波形的时序，频率，周期和占空比等。输入级包括一个数字滤波器，一个通道极性选择，边沿检测和一个通道预分频器。如果在输入引脚上出现被选择的边沿，TIMERx_CHxCV 寄存器会捕获计数器当前的值，同时 ChxIF 位被置 1，若 ChxIE=1 则产生通道中断。


图 18-12. 输入捕获逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/5e67b4a10b8b02bd4096d44c9016d8776abe0e9bd2b9e8be0f00c707c0b39e69.jpg)



通道输入信号 Cix 有两种选择，一种是 TIMERx_CHx 信号，另一种是 TIMERx_CH0，TIMERx_CH1 和 TIMERx_CH2 异或之后的信号。通道输入信号 Cix 先被 TIMER_CK 信号同


步，然后经过数字滤波器采样，产生一个被滤波后的信号。通过边沿检测器，可以选择检测上升沿或者下降沿。通过配置 CHxP选择使用上升沿或者下降沿。通过配置 CHxMS，还可以选择其他通道的输入信号或内部触发信号作为捕获信号。配置 IC 预分频器，使得若干个输入事件后才产生一个有效的捕获事件。捕获事件发生，TIMERx_CHxCV 存储计数器的值。

配置步骤如下：

第一步：滤波器配置（TIMERx_CHCTL0寄存器中CHxCAPFLT）：根据输入信号和请求信号的质量，配置相应的CHxCAPFLT。

第二步：边沿选择（TIMERx_CHCTL2寄存器中CHxP/CHxNP）：配置CHxP/CHxNP选择上升沿或者下降沿。

第三步：捕获源选择（TIMERx_CHCTL0寄存器中CHxMS）：

一旦通过配置CHxMS选 择 输 入 捕 获 源 ， 必 须 确 保 通 道 配 置 在 输 入 模 式（CHxMS!=0x0），而且TIMERx_CHxCV寄存器不能再被写。

第四步：中断使能（TIMERx_DMAINTEN寄存器中ChxIE和CHxDEN）：使能相应中断，可以获得中断和DMA请求。

第五步：捕获使能（TIMERx_CHCTL2寄存器中ChxEN）。

结果：当期望的输入信号发生时，TIMERx_CHxCV被设置成当前计数器的值，ChxIF位置1。如果ChxIF位已经为1，则ChxOF位置1。根据TIMERx_DMAINTEN寄存器中ChxIE和CHxDEN的配置，判断相应的中断和DMA请求是否被提出。

直接产生：软件设置CHxG位，会直接产生中断和DMA请求。

输入捕获模式也可用来测量 TIMERx_CHx 引脚上信号的脉冲波宽度。例如，一个 PWM 波连接到 CI0。配置 TIMERx_CHCTL0 寄存器中 CH0MS 为 2’b01，选择通道 0 的捕获信号为 CI0，同时设置上升沿捕获。配置 TIMERx_CHCTL0 寄存器中 CH1MS 为 2’b10，选择通道 1 捕获信号为 CI0，同时设置下降沿捕获。计数器配置为复位模式，在通道 0 的上升沿复位。TIMERX_CH0CV寄存器测量PWM的周期值，TIMERx_CH1CV寄存器测量PWM占空比值。

## 输出比较模式


图 18-13. 输出比较逻辑（带有互补输出的通道，x=0，1，2）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/1767ff32fa4ce99d8c8e33ac9940c02e44b8ed99ae62bc13ebdc87f0108dd748.jpg)



图 18-14. 输出比较逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/2934c8176d95acbd78329e1bc2fcfb14a4546f618af0dc22a0c3b7686dc5d345.jpg)


18-13. x=0 1 2 和 18-14. 分别给出了输出比较的逻辑电路。通道输出信号 CHx_O/CHx_ON 与 OxCPRE 信号（详情请见通道输出准备信号）的关系描述如下：OxCPRE 信号高电平有效，CHx_O/CHx_ON 的输出情况与 OxCPRE 信号，CHxP/CHxNP 位和 ChxE/ChxNE 位有关（具体情况请见 TIMERx_CHCTL2寄存器中的描述）。例如：

4、 当设置CHxP=0（CHx_O高电平有效，与OxCPRE输出极性相同）、ChxE=1（CHx_O输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_O输出有效（高）电平；

若OxCPRE输出无效（低）电平，则CHx_O输出无效（低）电平。

2）当设置CHxNP=1（CHx_ON低电平有效， $\scriptstyle { \frac { 1 } { \varTheta } } \mathrm { O x C P R E }$ 输出极性相反）、ChxNE=1（CHx_ON输出使能）时：

若OxCPRE输出有效（高）电平，则CHx_ON输出有效（低）电平；

若OxCPRE输出无效（低）电平，则CHx_ON输出无效（高）电平。

当 CH0_O 和 CH0_ON 同时输出时，CH0_O 和 CH0_ON 的具体输出情况还与 TIMERx_CCHP寄存器中的相关位（ROS、IOS、POE和 DTCFG 等位）有关。详情请见 。

在输出比较模式，TIMERx 可以产生时控脉冲，其位置，极性，持续时间和频率都是可编程的。当一个输出通道的TIMERx_CHxCV寄存器与计数器的值匹配时，根据CHxCOMCTL的配置，这个通道的输出可以被置高电平，被置低电平或者反转。当计数器的值与 TIMERx_CHxCV 寄存器的值匹配时，ChxIF 位被置 1，如果 ChxIE = 1 则会产生中断，如果 CxCDE=1 则会产生DMA 请求。

配置步骤如下：

第一步：时钟配置：

配置定时器时钟源，预分频器等。

第二步：比较模式配置：

◼ 设置CHxCOMSEN位来配置输出比较影子寄存器；

◼ 设置CHxCOMCTL位来配置输出模式（置高电平/置低电平/反转）；

◼ 设置CHxP/CHxNP位来选择有效电平的极性；

◼ 设置ChxEN使能输出。

第三步：通过ChxIE/CxCDE位配置中断/DMA请求使能。

第四步：通过TIMERx_CAR寄存器和TIMERx_CHxCV寄存器配置输出比较时基：

TIMERx_CHxCV可以在运行时根据你所期望的波形而改变。

第五步：设置CEN位使能定时器。

18-15. 显示了三种比较输出模式：反转/置高电平/置低电平，CAR=0x63，CHxVAL=0x3。


图 18-15. 三种输出比较模式


<table><tr><td colspan="101">CNT_CLK</td></tr><tr><td colspan="100">CEN</td><td></td></tr><tr><td colspan="96">CNT_REG</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="96">Overflow</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="91">match toggle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="86">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="82">match set</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">match clear</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">OxCPRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PWM 模式

在 PWM 输出模式下（PWM 模式 0 是配置 CHxCOMCTL 为 3’b110，PWM 模式 1 是配置CHxCOMCTL 为 3’b111），通道根据 TIMERx_CAR 寄存器和 TIMERx_CHxCV 寄存器的值，输出 PWM 波形。

根据计数模式，可以分为两种 PWM 波：EAPWM（边沿对齐 PWM）和 CAPWM（中央对齐PWM）。

EAPWM 的周期由 TIMERx_CAR 寄存器值决定，占空比由 TIMERx_CHxCV 寄存器值决定。18-16. EAPWM 显示了 CAPWM 的输出波形和中断。

CAPWM 的周期由（2*TIMERx_CAR 寄存器值）决定，占空比由（2*TIMERx_CHxCV 寄存器值）决定。 18-17. CAPWM 显示了 CAPWM 的输出波形和中断。

在向上计数模式中， PWM 模式 0 下（CHxCOMCTL=3’b110），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为无效电平；PWM 模式 1 下（CHxCOMCTL=3’b111），如果 TIMERx_CHxCV 寄存器的值大于 TIMERx_CAR 寄存器的值，通道输出一直为有效电平。


图 18-16. EAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/c783e597538689945eb5aab6cd2780221b8d8fb2512f11ab9d3e9d969e54921d.jpg)



图 18-17. CAPWM 时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/d6196b60f6f78a1ca6056046fce589f2f9f6fcf476668df0d6119a2008de4882.jpg)


## 通道输出准备信号

根据 18-13. x=0 1 2 所示，当 TIMERx 用于输出匹配比较模式下，在通道输出信号之前会产生一个中间信号 OxCPRE 信号（通道 x 输出准备信号）。设置 CHxCOMCTL 位可以定义 OxCPRE 信号类型。OxCPRE 信号有若干类型的输出功能，包括，设置 CHxCOMCTL=0x00 可以保持原始电平；设置 CHxCOMCTL=0x01 可以将 OxCPRE 信号设置为高电平；设置 CHxCOMCTL=0x02 可以将 OxCPRE 信号设置为低电平；设置 CHxCOMCTL=0x03，在计数器值和 TIMERx_CHxCV 寄存器的值匹配时，可以翻转

输出信号。

PWM 模式 0 和 PWM 模式 1 是 OxCPRE 的另一种输出类型，设置 CHxCOMCTL 位域为 0x06或0x07可以配置 PWM模式0/PWM 模式1。在这些模式中，根据计数器值和 TIMERx_CHxCV寄存器值的关系以及计数方向，OxCPRE 信号改变其电平。具体细节描述，请参考相应的位。

设置 CHxCOMCTL=0x04 或 0x05 可以实现 OxCPRE 信号的强制输出功能。输出比较信号能够直接由软件强置为有效或无效状态，而不依赖于 TIMERx_CHxCV 的值和计数器值之间的比较结果。

设置 CHxCOMCEN=1，当由外部 ETI 引脚信号产生的 ETIFP 信号为高电平时，OxCPRE 被强制为低电平。在下一次更新事件到来时，OxCPRE 信号才会回到有效电平状态。

## 互补输出

CHx_O 和 CHx_ON 是一对互补输出通道，这两个信号不能同时有效。TIMERx 有四路通道，只有前三路有互补输出通道。互补信号 CHx_O 和 CHx_ON 是由一组参数来决定：TIMERx_CHCTL2 寄存器中的 ChxEN 和 CHxNEN 位，TIMERx_CCHP 寄存器中的 POEN、ROS 和 IOS 位，TIMERx_CTL1 寄存器中的 ISOx 和 ISOxN 位。输出极性由 TIMERx_CHCTL2寄存器中的 CHxP 和 CHxNP 位来决定。


表 18-2. 由参数控制的互补输出表


<table><tr><td colspan="5">互补参数</td><td colspan="2">输出状态</td></tr><tr><td>POEN</td><td>ROS</td><td>IOS</td><td>ChxEN</td><td>CHxNEN</td><td>CHx_O</td><td>CHx_ON</td></tr><tr><td rowspan="5">0</td><td rowspan="5">0/1</td><td rowspan="4">0</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O / CHx_ON = LOWCHx_O / CHx_ON 输出禁能(1)</td></tr><tr><td>1</td><td colspan="2" rowspan="3">CHx_O/CHx_ON输出关闭状态(2):通道先输出无效电平: CHx_O = CHxP, CHx_ON = CHxNP); 如果死区产生时钟未失效, 在死区时间之后:CHx_O = ISOx, CHx_ON = ISOxN(3)</td></tr><tr><td rowspan="2">1</td><td>0</td></tr><tr><td>1</td></tr><tr><td>1</td><td>x</td><td>x</td><td colspan="2">CHx_O/CHx_ON输出关闭状态:通道先输出无效电平: CHx_O = CHxP, CHx_ON = CHxNP); 如果死区产生时钟未失效, 在死区时间之后:CHx_O = ISOx, CHx_ON = ISOxN</td></tr><tr><td rowspan="5">1</td><td rowspan="4">0</td><td rowspan="5">0/1</td><td rowspan="2">0</td><td>0</td><td colspan="2">CHx_O/CHx_ON = LOWCHx_O/CHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O = LOWCHx_O输出禁能</td><td>CHx_ON=OxCPRE⊕(4)CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON = LOWCHx_ON输出禁能</td></tr><tr><td>1</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON=(I OxCPRE)(5)⊕CHxNPCHx_ON输出使能</td></tr><tr><td>1</td><td>0</td><td>01</td><td>CHx_O = CHxPCHx_O输出关闭状态CHx_O = CHxPCHx_O输出关闭状态</td><td>CHx_ON = CHxNPCHx_ON输出关闭状态CHx_O=OxCPRE⊕CHxNPCHx_ON输出使能</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">1</td><td>0</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON = CHxNPCHx_ON输出关闭状态</td></tr><tr><td>1</td><td>CHx_O=OxCPRE⊕CHxPCHx_O输出使能</td><td>CHx_ON=(!OxCPRE)⊕CHxNPCHx_ON输出使能</td></tr></table>


注意：



（1） 输出禁能：CHx_O / CHx_ON 输出与对应引脚断开，对应引脚电平受 GPIO 上下拉配置控制，无上下拉时为悬空高阻态；



（2） 输出关闭状态：CHx_O / CHx_ON 输出无效电平（CHx_O = 0⊕CHxP = CHxP）；


（3） 详情见中止模式章节。

（4） ⊕：异或操作；

（5） (!OxCPRE)：OxCPRE 信号的互补信号。

## 死区时间插入

设置 ChxEN 和 CHxNEN 为 1’b1 的同时，设置 POEN 为 1，死区插入就会被使能。DTCFG位域定义了死区时间，死区时间对除了通道 3 以外的通道有效。死区时间的细节，请参考TIMERx_CCHP 寄存器。

死区时间的插入，确保了通道互补的两路信号不会同时有效。

在 PWM 模式 0，当通道 x 匹配事件发生时（TIMERx 计数器=CHxVAL），OxCPRE 反转。在18-18. 中的 A 点，CHx_O 信号在死区时间内为低电平，直到死区时间过后才变为高电平，而 CHx_ON 信号立刻变为低电平。同样，在 B 点，通道 x 匹配事件再次发生（TIMERx 计数器=CHxVAL），OxCPRE 信号被清 0，CHx_O 信号被立即清零，CHx_ON 信号在死区时间内仍然是低电平，在死区时间过后才变为高电平。

有时会有一些极端事件发生，例如：如果死区延时大于或者等于 CHx_ON 信号的占空比，CHx_ON 信号一直为无效值（参考 18-18. ）。


图 18-18. 带死区时间的互补输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/89beaf282972f28c219b753cf3c1592224809c3bf2cf2f55dc0e866a799cac01.jpg)


## 中止功能

使用中止功能时，输出 CHx_O 和 CHx_ON 的信号电平被以下位控制，TIMERx_CCHP 寄存器的 POEN，IOS 和 ROS 位，TIMERx_CTL1 寄存器的 ISOx 和 ISOxN 位。任何情况下，CHx_O 和 CHx_ON 信号输出不能同时设置为有效电平。中止源可以选择中止输入引脚，也可以选择 HXTAL 时钟失效事件，时钟失效事件由 RCU 中的时钟监视器（CKM）产生。将TIMERx_CCHP 寄存器的 BRKEN 位置 1 可以使能中止功能。TIMERx_CCHP 寄存器的 BRKP位决定了中止输入极性。

发生中止时，POEN 位被异步清除，一旦 POEN 位为 0，CHx_O 和 CHx_ON 的输出电平由TIMERx_CTL1 寄存器中的 ISOx 位和 ISOxN 位决定。如果 IOS=0，定时器释放输出使能，否则输出使能仍然为高。起初互补输出被置于复位状态，然后死区时间产生器重新被激活，以便在一个死区时间后驱动输出，输出电平由 ISOx 和 ISOxN 位配置。

发生中止时，TIMERx_INTF 寄存器的 BRKIF 位被置 1。如果 BRKIE=1，中断产生。


图 18-19. 通道响应中止输入（高电平有效）时，输出信号的行为


<table><tr><td rowspan="2"></td><td>BRKIN</td><td></td><td></td><td></td></tr><tr><td>OxCPRE</td><td></td><td></td><td></td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 1CHxP : 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td colspan="2">= ISOx</td></tr><tr><td>CHx_ON</td><td></td><td colspan="2">= ISOxN</td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP: 0 CHxNP : 0ISOx = ~ISOxN</td><td>CHx_O</td><td></td><td colspan="2">= ISOx</td></tr><tr><td>CHx_ON</td><td></td><td colspan="2">= ISOxN</td></tr><tr><td rowspan="2">CHxEN: 1 CHxNEN: 0CHxP : 0 CHxNP : 0ISOx = ISOxN</td><td>CHx_O</td><td></td><td></td><td></td></tr><tr><td>CHx_ON</td><td></td><td></td><td></td></tr></table>

## 正交译码器

正交译码器功能使用由 TIMERx_CH0 和 TIMERx_CH1 引脚生成的 CI0 和 CI1 正交信号各自相互作用产生计数值。通过设置 TSCFGy[3:0] != 4’b0000（y=0,1,2）来选择是仅由 CI0，仅由CI1，或者由 CI0 和 CI1 来决定定时器的计数方向。在每个方向选择源的电平改变期间，DIR位改变。计数器计数方向改变的机制如 18-3. 所示。正交译码器可以当作一个带有方向选择的外部时钟，这意味着计数器会在 0 和自动加载值之间连续的计数。因此，用户必须在计数器开始计数前配置 TIMERx_CAR 寄存器。


表 18-3. 计数方向与正交译码器信号之间的关系


<table><tr><td rowspan="2">计数模式</td><td rowspan="2">电平</td><td colspan="2">CI0FE0</td><td colspan="2">CI1FE1</td></tr><tr><td>上升</td><td>下降</td><td>上升</td><td>下降</td></tr><tr><td rowspan="2">只有 CI0</td><td>CI1FE1=1</td><td>Down</td><td>Up</td><td>-</td><td>-</td></tr><tr><td>CI1FE1=0</td><td>Up</td><td>Down</td><td>-</td><td>-</td></tr><tr><td rowspan="2">只有 CI1</td><td>CI0FE0=1</td><td>-</td><td>-</td><td>Up</td><td>Down</td></tr><tr><td>CI0FE0=0</td><td>-</td><td>-</td><td>Down</td><td>Up</td></tr><tr><td rowspan="4">CI0 和 CI1</td><td>CI1FE1=1</td><td>Down</td><td>Up</td><td>X</td><td>X</td></tr><tr><td>CI1FE1=0</td><td>Up</td><td>Down</td><td>X</td><td>X</td></tr><tr><td>CI0FE0=1</td><td>X</td><td>X</td><td>Up</td><td>Down</td></tr><tr><td>CI0FE0=0</td><td>X</td><td>X</td><td>Down</td><td>Up</td></tr></table>

注意：”-“ 意思是”无计数”; “X” 意思是不可能。


图 18-20. 正交译码器接口模式下计数器运行例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/467642a7440f54fb553e1d8fe7ef422d1597577559992ea88be5ad48bb94d03b.jpg)



图 18-21. CI0FE0 极性反相的正交译码器接口模式下的例子


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/9b826fd56069bce38cba9b4e07b44b830dfd95a898eeb3e82093a28435f59830.jpg)


## 霍尔传感器接口功能

高级定时器支持霍尔传感器接口功能，该功能可以用来控制 BLDC 电机。

18-22. BLDC 是定时器和电机的连接示意图。众所周知，我们要两个定时器。TIMER_in 定时器（可以是高级定时器或者通用 L0 定时器）接收来自电机霍尔传感器的三路信号，这三路信号是电机转子的位置信号。

三个霍尔传感器与 TIMER_in 定时器的三路输入捕获引脚一一对应连接，每个霍尔传感器输入一路波形到输入引脚，分析三路霍尔信号可以计算出转子的位置和速度。

通过定时器内部连接功能（TRGO-ITIx），TIMER_in 定时器和 TIMER_out 定时器可以连接在一起。TIMER_out 定时器根据 ITIx 触发信号输出 PWM 波，驱动 BLDC 电机，控制 BLDC 电机的速度。这样，TIMER_in 定时器和 TIMER_out 定时器的连接形成了一个反馈电路，可以根据需求改变配置。

高级定时器和通用 L0 定时器具有输入异或功能，可作为 TIMER_in 定时器。同时，高级定时器具备互补输出和死区插入功能，可作为 TIMER_out 定时器。

另外，根据定时器的内部互连关系，可以选择成对的互连定时器，例如：

TIMER_in（TIMER2）-> TIMER_out（TIMER0 ITI2） 

选择好合适的互连定时器，线路也已经连接好，就可以配置定时器。有以下关键配置：

◼ 通过设置TI0S，来使能异或功能。三路输入信号的任何一路发生变化，CI0都会反转，CH0VAL此时会捕获计数器的当前值。

◼ 通过设置CCUC和CCSE，来选择ITIx触发换相。

◼ 根据需求配置PWM参数。


图 18-22. 霍尔传感器用在 BLDC 电机控制中


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/624d8b14431ad7e14f039dbf278be29890776400a6101646d06f59e268934840.jpg)



图 18-23. 两个定时器之间的霍尔传感器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/5db2a9c55fdb4288968bd5633a67f73bc5dc16fd83334bf005d3e348b3fcaaaa.jpg)


## 主从管理

TIMERx 能在多种模式下同步外部触发，包括复位模式，暂停模式和事件模式，可以通过设置SYSCFG_TIMER0CFG（x=3,4,5）寄存器中的 TSCFGy[3:0]配置这些模式。


表 18-4. 从模式示例


<table><tr><td></td><td>模式选择</td><td>触发源选择</td><td>极性选择</td><td>滤波和预分频</td></tr><tr><td>列举</td><td>TSCFGy[3:0]y=3(复位模式)y=4(暂停模式)y=5(事件模式)</td><td>TSCFGy[3:0]0001: ITI00010: ITI10011: ITI20100: ITI30101: CI0F_ED0110: CI0FE00111: CI1FE11000: ETIFP</td><td>如果触发源是CI0FE0或者CI1FE1,配置CHxP和CHxNP来选择极性和反相。如果触发源是ETIFP,配置ETP选择极性和反相。</td><td>若触发源为ITIx,滤波和预分频不可用。若触发源为Cix,可配置CHxCAPFLT设置滤波,预分频不可用。若触发源为ETIFP,滤波和预分频均可用。</td></tr><tr><td rowspan="2">例1</td><td>复位模式当触发输入上升沿到来时,计数器清零重启。</td><td>TSCFG3[3:0] = 4'b0001 选择 ITIO 为触发源。</td><td>若触发源是 ITIO,极性选择不可用。</td><td>若触发源是 ITIO,滤波和预分频不可用。</td></tr><tr><td colspan="4">图18-24. 复位模式</td></tr><tr><td rowspan="2">例2</td><td>暂停模式当触发输入为低的时候,计数器暂停计数,当触发输入为高时,计数器计数。</td><td>TSCFG4[3:0] = 4'b0110选择 CI0FE0 为触发源。</td><td>TIOS=0(非异或)[CHONP=0,CHOP=0]CI0FE0 不反相。捕获发生在上升沿。</td><td>在这个例子中滤波被旁路。</td></tr><tr><td colspan="4">图18-25. 暂停模式<img src="https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/1802961792c2316b3adb37897333b15ecf40e178e0605b1e52a79437f2cec941.jpg"/></td></tr><tr><td rowspan="2">例3</td><td>事件模式触发输入的上升沿计数器开始计数。</td><td>TSCFG5[3:0] = 4'b1000选择 ETIFP 为触发源。</td><td>ETP = 0,ETI 极性不改变。</td><td>ETPSC = 1,ETI 2 分频。ETFC = 0,ETI 无滤波。</td></tr><tr><td colspan="4">图18-26. 事件模式</td></tr></table>

## 单脉冲模式

设置 TIMERx_CTL0 寄存器的 SPM 位置 1，使能单脉冲模式。当 SPM 置 1，计数器在下次更新事件到来后清零并停止计数。为了得到脉冲波，可以通过设置 CHxCOMCTL 配置 TIMERx为 PWM 模式或者比较模式。

一旦设置定时器运行在单脉冲模式下，没有必要设置 TIMERx_CTL0 寄存器的定时器使能位CEN=1 来使能计数器。触发信号沿或者软件写 CEN=1 都可以产生一个脉冲，此后 CEN 位一直保持为 1 直到更新事件发生或者 CEN 位被软件写 0。如果 CEN 位被软件清 0，计数器停止工作， 计数值被保持。

在单脉冲模式下，有效的外部触发边沿会将 CEN 位置 1，使能计数器。然而，执行计数值和TIMERx_CHxCV 寄存器值的比较结果依然存在一些时钟延迟。为了最大限度减少延迟，用户可以将 TIMERx_CHCTL0/1 寄存器的 CHxCOMFEN 位置 1。单脉冲模式下，触发上升沿产生之后，OxCPRE 信号将被立即强制转换为与发生比较匹配时相同的电平，但是不用考虑比较结果。只有输出通道配置为 PWM 模式 0 或 PWM 模式 1 时 CHxCOMFEN 位才可用，触发源来源于触发信号。


图 18-27. 单脉冲模式，TIMERx_CHxCV = 0x04，TIMERx_CAR=0x60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/dae3273f6bddbea82615cf552325eb38ce89ac9ed2234a5171d2602ab1d55b67.jpg)


## 定时器互连

定时器之间的相互连接可以实现定时器的级联或者同步。可以通过配置一个定时器工作在主模式，另一个定时器工作在从模式来实现。

## 定时器 2 作为定时器 0 的预分频器

1. 配置定时器2为主模式，选择其更新事件（UPE）为触发输出（配置TIMER2_CTL1寄存器的MMC=3’b010）。定时器2在每次计数器溢出产生更新事件时，输出一个周期信号；

2. 配置定时器2周期（TIMER2_CAR寄存器）；

3. 配 置 定 时 器 0 在 外 部 时 钟 模 式 0 ， 选 择 定 时 器 0 输 入 触 发 源 为 定 时 器 2 ，（ 配 置SYSCFG_TIMERxCFG寄存器的TSCFG6[3:0] = 4’b 0001）；

4. 写 1 到 CEN 位 启 动 定 时 器 0 （ TIMER0_CTL0 寄 存 器 ）； 写 1 到 CEN 位 启 动 定 时 器 2（TIMER2_CTL0寄存器）。

## 用定时器 2 的使能/更新信号来启动定时器 0

用定时器 2 的使能信号来启动定时器 0，见 18-28. 2 0。在定时器 2 使能信号输出后，定时器 0 按照分频后的内部时钟从当前值开始计数。

当定时器 0 接收到触发信号，它的 CEN 位被自动置 1，计数器计数直到禁能定时器 0。两个定时器的计数器频率都是 TIMER_CK 经过预分频器 3 分频后的频率 $( \mathsf { f } _ { \mathsf { P S C } _ { - } \mathsf { C L K } } = \mathsf { f } _ { \mathsf { T I M E R } _ { - } \mathsf { C K } } / 3 )$ ）。步骤如下：

1. 配置定时器2为主模式，发送它的使能信号作为触发输出，配置定时器0选择输入触发来自定时器2（配置SYSCFG_TIMERxCFG寄存器的TSCFG5[3:0] = 4’b 0011）；

2. 写1到CEN来开启定时器2（TIMER2_CTL0寄存器）。


图 18-28. 用定时器 2 的使能信号触发定时器 0


<table><tr><td colspan="6">TIMER2</td></tr><tr><td></td><td>TIMER_CK</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>CEN</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>CNT_REG</td><td>61</td><td>62</td><td>63</td><td></td></tr><tr><td colspan="6">TIMER0</td></tr><tr><td></td><td>TRGIF</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>CNT_REG</td><td>11</td><td>12</td><td>13</td><td>14</td></tr></table>

在这个例子中，也可以使用更新事件代替使能信号作为触发源。见 18-29. 20，按以下步骤进行：

1. 配置定时器2为主模式，发送它的更新事件（UPE）作为触发输出（配置TIMER2_CTL1寄存器的MMC=3’b010）；

2. 配置定时器2的周期（TIMER2_CARL寄存器）；

3. 配置定时器0选择输入触发来自定时器2，配置定时器0在事件模式（配 置SYSCFG_TIMERxCFG寄存器的TSCFG5[3:0] =4’b0011）；

4. 写1到CEN来开启定时器2（TIMER2_CTL0寄存器）。


图 18-29. 用定时器 2 的更新事件来触发定时器 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/53560dab5d28f4005a79c55581b1e996a4caa388e7c4963112d4aad17f84adeb.jpg)



使用定时器 2 的使能/O0CPRE 信号来使能定时器 0 计数。


在这个例子中，使用定时器 2 的使能信号来使能定时器 0。如 18-30. 20 ，在定时器 2 被使能后，定时器 0 在内部分频的时钟上开始计数。两个计数器的时钟频率都是由 TIMER_CK 时钟 3 分频得来 $( \mathsf { f } _ { \mathsf { P S C } _ { - } \mathsf { C L K } } = \mathsf { f } _ { \mathsf { T I M E R } _ { - } \mathsf { C K } } / 3 )$ ），步骤如下：

1. 配置定时器2在主模式，配置其输出使能信号作为触发输出（配置TIMER2_CTL1寄存器的MMC=3’b001）；

2. 配置定时器0从定时器2获取输入触发，配置定时器0工 作 在 暂 停 模 式（配 置SYSCFG_TIMERxCFG寄存器的TSCFG5[3:0] = 4’b 0011）；

3. 写1到CEN位来使能定时器0（TIMER0_CTL0寄存器）；

4. 写1到CEN位来启动定时器2（TIMER0_CTL0寄存器）；

5. 写0到CEN位来停止定时器2（TIMER0_CTL0寄存器）。


图 18-30. 用定时器 2 的使能信号来控制定时器 0 的暂停模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/cc459ef0620e33db9c00fd4255e5f61ddad0de1818a96c0c90c0c50271cb38be.jpg)


这个例子中，我们也可以使用定时器 2 的 O0CPRE 信号代替其使能信号输出作为触发源。步骤如下：

1. 配置定时器2在主模式下，配置O0CPRE信号为触发输出（配置TIMER2_CTL1寄存器的MMS=3’b100）；

2. 配置定时器2的O0CPRE波形（TIMER2_CHCTL0寄存器）；

3. 配置定时器0获取来自定时器2的输入触发，配置定时器0工作在暂停模式（配置SYSCFG_TIMERxCFG寄存器TSCFG5[3:0] = 4’b 0011）；

4. 写1到CEN位来使能定时器0（TIMER0_CTL0寄存器）；

5. 写1到CEN位来开启定时器2（TIMER0_CTL0寄存器）。


图 18-31. 用定时器 2 的 O0CPRE 信号控制定时器 0 的暂停模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/6ebc2e3c135193d742f899ca6bed25c347df229524d1ff1db25826d778100da7.jpg)


## 定时器 DMA模式

定时器 DMA 模式是指通过 DMA 模块配置定时器的寄存器。有两个跟定时器 DMA 模式相关的寄存器：TIMERx_DMACFG 和 TIMERx_DMATB。必须使能相应的 DMA 请求位，一些内部中断事件才可以产生 DMA 请求。当中断事件发生，TIMERx 会给 DMA 发送请求。DMA配置成 M2P（传输方向为从内存到外设）模式，PADDR（外设基地址）为 TIMERx_DMATB 寄存器地址，DMA 就会访问 TIMERx_DMATB 寄存器。实际上，TIMERx_DMATB 寄存器只是一个缓冲，定时器会将 TIMERx_DMATB 映射到一个内部寄存器，这个内部寄存器由TIMERx_DMACFG 寄存器中的 DMATA 来指定。如果 TIMERx_DMACFG 寄存器的 DMATC位域值为 0，表示 1 次传输，定时器发送 1 个 DMA请求就可以完成。如果 TIMERx_DMACFG寄存器的 DMATC 位域值不为 1，例如其值为 3，表示 4 次传输，定时器就需要再多发 3 次DMA请求。在这 3 次请求下，DMA对 TIMERx_DMATB 寄存器的访问会映射到访问定时器的DMATA+0x4，DMATA+0x8，DMATA+0xC 寄存器。总之，发生一次 DMA 内部中断请求，定时器会连续发送（DMATC+1）次请求。

如果再来 1 次 DMA请求事件，TIMERx 将会重复上面的过程。

## 定时器调试模式

当 Cortex™-M3 内核停止，DBG_CTL0 寄存器中的 TIMERx_HOLD 配置位被置 1，定时器计数器停止。
