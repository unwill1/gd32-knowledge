## 25. 高分辨率定时器（HRTIMER）

## 25.1. 简介

HRTIMER 具有高分辨率计数时钟，可用于高精度定时。它可以产生 16 个高分辨率的数字信号来灵活地控制电动机或用于电源管理应用。这 16 个数字信号可以独立输出，也可以耦合成 8 对互补信号输出。

HRTIMER 具有灵活的捕获功能，可用于捕获输入信号的时序。它具有多个连接到 ADC 和 DAC 的内部信号，可用于控制和监视。

为了安全起见，HRTIMER 可处理各种故障输入。

## 25.2. 主要特征

 高分辨率定时单元：Master_TIMER，Slave_TIMERx (x=0..7)；

16个数字信号输出：它们可由任意一个定时单元控制，可独立输出也可耦合成8对互补输出；

 同步输出：作为主机同步外部资源；

 同步输入：作为从机与外部资源同步；

 多个内部信号连接到ADC和DAC；

 多种故障输入保护机制：故障输入通道和系统故障；

 突发模式控制器应用于轻载操作；

 10个中断向量：Master_TIMER中断，Slave_TIMERx（x = 0..7）中断和故障中断；

 9个DMA请求：Master_TIMER请求和Slave_TIMERx（x = 0..7）请求。DMA模式可以更新多个寄存器；

 DMA模式用于多个寄存器的更新。

## 25.3. 结构框图

25-1. HRTIMER 给出了 HRTIMER 的内部细节配置。


图 25-1. HRTIMER 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/971c8c24417ae3132d6d32ae55c16c7adb3adf094792d8d083a289520b82068a.jpg)


## 25.4. 功能说明

## 25.4.1. Master_TIMER 单元

Master_TIMER 单元由以下模块组成：

 16位计数器

 自动重载寄存器：确定计数周期

 重复计数器

 比较寄存器y(y=0..3)

25-2. Master_TIMER 给出了 Master_TIMER 的内部细节配置。


图 25-2. Master_TIMER 结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/b4a01b1e964675bd2958cd7bd74c272862402a7e7fd157b0d9513090228f7262.jpg)


自动重载寄存器和比较 y（y = 0..3）寄存器具有以下限值：

当 CNTCKDIV[2:0] < 3’b101

 最小值必须大于或等于3个t<sub>HRTIMER_CK</sub>周期对应的计数值；

 最大值必须小于或等于（0xFFFF – 1个t<sub>HRTIMER_CK</sub>周期对应的计数值）。

注意：每个t<sub>HRTIMER_CK</sub>周期对应的计数值 = f<sub>HRTIMER_PSSCK</sub> / f<sub>HRTIMER_CK。</sub>

当 CNTCKDIV[2:0] >= 3’b101

 最小值必须大于或等于0x0003；

 最大值必须小于或等于0xFFFE。

具体请见 25-1. y y = 0..3 。


表 25-1. 自动重载寄存器和比较 y（y = 0..3）寄存器的限值


<table><tr><td>CNTCKDIV[2:0]</td><td>最小值</td><td>最大值</td></tr><tr><td>3&#x27;b000</td><td>0x0060</td><td>0xFFDF</td></tr><tr><td>3&#x27;b001</td><td>0x0030</td><td>0xFFEF</td></tr><tr><td>3&#x27;b010</td><td>0x0018</td><td>0xFFFF7</td></tr><tr><td>3&#x27;b011</td><td>0x000C</td><td>0xFFFFB</td></tr><tr><td>3&#x27;b100</td><td>0x0006</td><td>0xFFFFD</td></tr><tr><td>3&#x27;b101</td><td>0x0003</td><td>0xFFFE</td></tr><tr><td>3&#x27;b110</td><td>0x0003</td><td>0xFFFE</td></tr><tr><td>3&#x27;b111</td><td>0x0003</td><td>0xFFFE</td></tr></table>

## 计数器时钟

Master_TIMER 的时钟源是由 RCU 模块提供的 HRTIMER_CK，DLL 用于产生高分辨率时钟HRTIMER_HPCK（f<sub>HRTIMER_HPCK</sub> = 32 * f<sub>HRTIMER_CK</sub>），更多信息请参考 DLL 。

预分频器（PSC）将高分辨率时钟（HRTIMER_HPCK）除以分频因子 2CNTCKDIV[2:0]，得到计数器时钟（HRTIMER_PSCCK）。该分频因子由 HRTIMER_MTCTL0 寄存器中的 CNTCKDIV[2:0]位域控制。它们之间的频率关系可以表示如下：

$$
\mathsf {f} _ {\text { HRTIMER\_PSCCK }} = \mathsf {f} _ {\text { HRTIMER\_HPCK }} / 2 ^ {\text { CNTCKDIV[2:0] }}\tag{25-1}
$$

注意：一旦 Master_TIMER 使能了，就不能修改时钟分频 CNTCKDIV[2:0]的值。

25-3. 16 显示了将寄存器 HRTIMER_MTCAR 设置为 0x0104，HRTIMER_MTCTL0 寄存器中的位域 CNTCKDIV[2: 0]设置为 3'b100 时计数器的动作。


图 25-3. 分频为 16 时计数器时钟


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/46b01c6a97ad8eca72653ceadc73f287c84cc6511b19f225198477864cea5de8.jpg)


25-2. fHRTIMER<sub>_CK</sub> = 216MHz 列出了 f<sub>HRTIMER_CK</sub> 为 216MHz 时的不同分辨率。


表 25-2. f<sub>HRTIMER_CK</sub> = 216MHz 的分辨率


<table><tr><td>CNTCKDIV[2:0]</td><td>fHRTIMER_PSCCK</td><td>分辨率</td></tr><tr><td>3&#x27;b000</td><td>216*32MHz=6.912GHz</td><td>144.68ps</td></tr><tr><td>3&#x27;b001</td><td>216*16MHz=3.456GHz</td><td>289.35ps</td></tr><tr><td>3&#x27;b010</td><td>216*8MHz=1.728GHz</td><td>578.70ps</td></tr><tr><td>3&#x27;b011</td><td>216*4MHz=864MHz</td><td>1.16ns</td></tr><tr><td>3&#x27;b100</td><td>216*2MHz=432MHz</td><td>2.31ns</td></tr><tr><td>3&#x27;b101</td><td>216*1MHz=216MHz</td><td>4.63ns</td></tr><tr><td>3&#x27;b110</td><td>216/2MHz=108MHz</td><td>9.26ns</td></tr><tr><td>3&#x27;b111</td><td>216/4MHz=54MHz</td><td>18.52ns</td></tr></table>

## 向上计数模式

计数器从 0 连续递增到计数器重载值，该值在 HRTIMER_MTCAR 寄存器中定义。计数器有两种工作模式：单脉冲模式（HRTIMER_MTCTL0 寄存器中的 CTNM = 0）或连续模式（CTNM = 1）。

在单脉冲模式下，将 HRTIMER_MTCTL0 寄存器中的 MTCEN 位置 1 后，第一个复位事件将启动计数器。当计数到计数器重载值时，计数器停止并生成周期事件。然后，其他的复位事件将复位并重新启动计数器。在计数过程中，如果 HRTIMER_MTCTL0 寄存器中的 CNTRSTM = 1，则复位事件将复位并重新启动计数器，否则将被忽略。 25-4. 显示了单脉冲模式下的计数器运行情况。


图 25-4. 单脉冲模式下计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/87f7d65ea0cb2a71a80eec378295402e3027cb8c6df983d5e3cb83dad3b90f93.jpg)


在连续模式下，一旦 HRTIMER_MTCTL0 寄存器中的 MTCEN 位置 1，计数器将立即启动。当计数到计数器重载值时，计数器从 0 重新启动，并产生翻转事件。与单脉冲模式不同，随时生成的复位事件将复位并重启计数器。 25-5. 显示了连续模式下的计数器运行情况。


图 25-5. 连续模式下计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/9a7e19cfca3de147ac8c6d085f30b3360332c6284f8c8368006d2981eb5c5220.jpg)


## 重复计数器

HRTIMER_MTCTL0 寄存器中的 MTCEN 位置 1 时，重复计数器将加载 HRTIMER_MTCREP 寄存器的值。当由于复位事件或连续模式下的翻转事件清零计数器时，重复计数器值递减。当重复计数器值达到零时，复位事件或连续模式下的翻转事件将产生一个重复事件并重新加载HRTIMER_MTCREP 寄存器的值。

<table><tr><td>MTCEN或STxCEN(x=0..7)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>复位事件</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CounterCTNM = 0CNTRSTM = 0</td><td></td><td>CARL</td><td></td><td>CARL</td><td></td></tr><tr><td>CREP[7:0]</td><td>0x04</td><td></td><td></td><td></td><td></td></tr><tr><td>重复计数器</td><td></td><td>0x04</td><td></td><td>0x03</td><td>0x02</td></tr></table>

重复事件会将 HRTIMER_MTINTF 寄存器中的 REPIF 位置 1，如果使能了相应中断或 DMA 请求（HRTIMER_MTDMAINTEN 寄存器中的 REPIE = 1 或 REPDEN = 1），则会产生重复中断和 DMA请求。可以通过向 HRTIMER_MTINTFC 寄存器中的 REPIFC 位写 1 来清除重复中断标志。

25-6. 显示了在连续模式下重复计数器的运行情况。


图 25-6. 连续模式下重复计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/60f1d6d95aeb0cafc15434b544c8428a5135656b3cb0b8d1d556eeec30534885.jpg)



25-7. CNTRSTM = 0 显示了单脉冲模式下，CNTRSTM =0 时重复计数器的运行情况。



图 25-7. 单脉冲模式下，CNTRSTM = 0 时重复计数器的动作



25-8. CNTRSTM = 1 显示了单脉冲模式下，CNTRSTM =1 时重复计数器的运行情况。



图 25-8. 单脉冲模式下，CNTRSTM = 1 时重复计数器的动作


<table><tr><td>MTCEN或STxCEN(x=0..7)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>复位事件</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CounterCTNM = 0CNTRSTM = 1</td><td></td><td></td><td></td><td>CARL</td><td></td><td>CARL</td></tr><tr><td>CREP[7:0]</td><td>0x03</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>重复计数器</td><td></td><td>0x03</td><td>0x02</td><td>0x01</td><td>0x00</td><td>0x03</td></tr><tr><td>REPIF位</td><td></td><td></td><td></td><td></td><td></td><td>通过REPIFC位清零</td></tr></table>

## 计数器复位

一旦计数器（MTCEN = 1）使能了，就可以通过软件或同步输入将计数器复位为 0。

将 MTSRST 位置 1（由硬件自动清除）将使计数器复位。

当 HRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以复位计数器。详细信息请参考 。

当计数器时钟 HRTIMER_PSCCK 的预分频系数大于 32（CNTCKDIV [2:0] > 3’b101）时，计数器复位事件将延迟到 HRTIMER_PSCCK 的下一个上升沿。

25-9.  64 显示了连续模式下，CNTCKDIV[2:0] = 3’b110，HRTIMER_MTCAR = 0x4 时的运行情况。


图 25-9. 当预分频系数为 64 时，复位事件重新同步


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/0d624832f1bb1183b3e59d56a45fce7c31f3b5b76e68615c3950e9250f6d14d3.jpg)


## 比较

Master_TIMER 具有四个比较寄存器：HRTIMER_MTCMPxV（x = 0..3）。当计数器值与比较寄存器值匹配时，将生成一个对应的比较事件。

比较事件会将相应的比较中断标志位置 1（HRTIMER_MTINTF 寄存器中的 CMPxIF 位，x = 0..3），如果比较中断或DMA请求使能（HRTIMER_MTDMAINTEN寄存器中的CMPxIE = 1或CMPxDEN= 1，x = 0..3），则会产生一个比较中断或 DMA 请求。通过写 1 到 HRTIMER_MTINTFC 中的CMPxIF 位（x = 0..3）可以清除比较中断标志。

## 半波模式

当 HRTIMER_MTCTL0 中的 HALFM 位置 1 时，半波模式使能。此模式将比较 0 有效寄存器的值强 制 为 计 数 器 重 载 值 的 一 半 ， 但 HRTIMER_MTCMP0V 寄 存 器 的 值 不 会 更 新 为（HRTIMER_MTCAR / 2）的值。半波模式主要用于生成固定占空比为 50％的方波。

当 HRTIMER_MTCTL0 寄存器中的 SHWEN 位置 1 时，将使能影子寄存器，比较 0 有效寄存器的值在更新事件时刷新。反之，比较 0 有效寄存器在新值写入后立即刷新。

## 交错模式

此模式有助于实现与半模式相辅相成的替代拓扑结构。当 HRTIMER_MTCAR 值更新时，比较值寄存器会被自动重新计算。通过 HRTIMER_MTCTL0 和 HRTIMER_STxCTL0 中的 ALTM[1:0]位选择交错模式。


表 25-3. 交错模式选择


<table><tr><td>ALTM[1:0]</td><td>交错模式</td></tr><tr><td>00</td><td>禁止</td></tr><tr><td>01</td><td>三重交错(120°)</td></tr><tr><td>10</td><td>四重交错(90°)</td></tr><tr><td>11</td><td>保留</td></tr></table>

25-4. 显示了交错模式的比较值，比较寄存器的内容将被覆盖，相应的比较事件可用作触发器，以设置或复位从定时器。


表 25-4. 交错模式的比较值


<table><tr><td>模式</td><td>三重交错(120°)</td><td>四重交错(90°)</td></tr><tr><td>HRTIMER_MTCMP0V</td><td>HRTIMER_MTCAR /3</td><td>HRTIMER_MTCAR /4</td></tr><tr><td>HRTIMER_MTCMP1V</td><td>2 x HRTIMER_MTCAR /3</td><td>HRTIMER_MTCAR /2</td></tr><tr><td>HRTIMER_MTCMP2V</td><td>无影响</td><td>3 x HRTIMER_MTCAR /4</td></tr></table>

注意：在交错模式中，比较寄存器由硬件控制，写入这些寄存器时没有影响。然而，预加载寄存器存储了比较值，并且在退出交错模式时将变为活动状态。

## 同步输入启动/复位计数器

当 HRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以产生计数器复位事件；当HRTIMER_MTCTL0 寄存器中的 SYNISTRT 位置 1 时，同步输入可以启动计数器。更多信息请参考 。

同步输入请求会将 HRTIMER_MTINTF 寄存器中的 SYNIIF 位置 1，如果使能了中断或 DMA请求（HRTIMER_MTDMAINTEN 寄存器中的 SYNIIE = 1 或 SYNIDEN = 1），会产生相应的中断或DMA 请求。可以通过写 1 到 HRTIMER_MTINTFC 寄存器中的 SYNIIFC 位清除同步输入中断标志。

## 更新事件和影子寄存器

Master_TIMER 中的某些寄存器具有影子寄存器。MCU 复位后，影子寄存器被禁用。如果将HRTIMER_MTCTL0 寄存器中的 SHWEN 位清 0，则将禁用影子寄存器。写入这些寄存器的值将转移到活动寄存器中并生效。

HRTIMER_MTCTL0 寄存器中的 SHWEN 位置 1，将使能影子寄存器并预加载这些寄存器。写入这些寄存器的值将被传送到影子寄存器，且不会立即生效。当发生更新事件时，影子寄存器内容将转移到活动寄存器中并立即生效。

25-5. Master_TIMER 列出了具有影子寄存器的寄存器和相应的更新事件。


表 25-5. Master_TIMER 影子寄存器和更新事件


<table><tr><td>具有影子寄存器的寄存器</td><td>影子寄存器使能位</td><td>更新事件</td></tr><tr><td>HRTIMER_MTDMAINTEN</td><td rowspan="7">HRTIMER_MTCTL0 寄存器中的 SHWEN 位</td><td>软件(MTSUP位)</td></tr><tr><td>HRTIMER_MTCAR</td><td>重复事件(UPREP = 1)</td></tr><tr><td>HRTIMER_MTCREP</td><td>DMA模式结束事件(UPSEL[1:0] = 2&#x27;b01)</td></tr><tr><td>HRTIMER_MTCMP0V</td><td rowspan="4">DMA模式结束事件之后的翻转事件(UPSEL[1:0] = 2&#x27;b10)</td></tr><tr><td>HRTIMER_MTCMP1V</td></tr><tr><td>HRTIMER_MTCMP2V</td></tr><tr><td>HRTIMER_MTCMP3V</td></tr></table>

Master_TIMER 有 4 个更新选项：

1. 软件生成更新事件。写 1 到 HRTIMER_CTL1 寄存器的 MTSUP 位可以产生更新事件。此时，无论 HRTIMER_MTCTL0 寄存器中的 UPSEL[1:0]位如何配置，所有挂起的硬件更新事件都将被忽略；

2. 重复事件生成更新事件。如果 HRTIMER_MTCTL0 寄存器中的 UPREP 位置 1，由翻转事件或复位事件引起的重复事件会生成更新事件。HRTIMER_MTCTL0 寄存器中的 UPSEL[1:0] =2’b10，则重复事件不生成更新事件；

3. 当 DMA 模式下的 DMA 传输完成时，生成更新事件。如果 HRTIMER_MTCTL0 寄存器中的

UPSEL[1:0] = 2’b01，则在 DMA 模式下的 DMA 传输完成时，硬件会自动生成更新事件。也可以通过软件或重复事件来生成更新事件。

4. 当DMA模式下的DMA传输完成后，计数器的翻转会产生更新事件。如果HRTIMER_MTCTL0寄存器中的 UPSEL [1:0] = 2’b10，则在 DMA 模式下的 DMA传输完成后，计数器发生翻转事件时，硬件会自动生成更新事件。也可以通过软件生成更新事件。

更新事件会将 HRTIMER_MTINTF 寄存器中的 UPIF 位置 1，如果使能了相应的中断和 DMA功能（HRTIMER_MTDMAINTEN 寄存器中的 UPIE = 1 或 UPDEN = 1），则会产生中断或 DMA 请求。可以通过将 HRTIMER_MTINTFC 中的 UPIFC 位写 1，来清除更新事件中断标志。

## DAC 触发

当 Master_TIMER 的更新事件发生时，如果 HRTIMER_MTCTL0 寄存器中的 DACTRGS[1:0] !=2’b00，则在 HRTIMER_DACTRIGOx（x = 0..3）上生成 DAC 触发请求。如果 HRTIMER_MTCTL0寄存器中的 DACTRGS [1:0] = 2’b00，则不会生成 DAC 触发请求。HRTIMER_DACTRIGOx（x =0..3）是从 Master_TIMER 连接到 DAC 模块的内部信号。有关更多信息，请参考 DAC 。

## 25.4.2. Slave_TIMERx(x=0..7)单元

HRTIMER 具有 8 个相同结构的从定时器：Slave_TIMERx $( \mathsf { x } = 0 . . 7 )$ 。每个从定时器都由以下组件构成：

 16位计数器

 自动重载寄存器：计数周期值

 重复计数器

 比较寄存器y(y=0..3)

 捕获寄存器y(y=0,1)

 置位/复位交叉开关

 空闲控制级

 通道输出级

25-10. Slave_TIMERx 显示了 Slave_TIMERx 的结构框图。


图 25-10. Slave_TIMERx 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/73be0ae1b7c7279bf80a2c159d20afe6a74d3a83c66249883e4c26ede82f8ff4.jpg)


自动重载寄存器和比较 y（y = 0..3）寄存器具有以下限值：

当 $\mathsf { C N T C K D I V } [ 2 : 0 ] < 3 ^ { \prime } 6 1 0 1$ 

 最小值必须大于或等于3个t<sub>HRTIMER_CK</sub>周期对应的计数值；

 最大值必须小于或等于（0xFFFF – 1个t<sub>HRTIMER_CK</sub>周期对应的计数值）。

注意：每个t<sub>HRTIMER_CK</sub>周期对应的计数值 = f<sub>HRTIMER_PSSCK</sub> / f<sub>HRTIMER_CK。</sub>

当 $\mathtt { C N T C K D I V } [ 2 : 0 ] > = 3 ^ { \prime } { \mathsf { b } } 1 0 1$ 

 最小值必须大于或等于0x0003；

 最大值必须小于或等于0xFFFE。

具体请见 25-1. y $\textcircled{1 } = 0 . . 3 )$ 寄存器的限值

计数器和捕获 ${ \sf y } \left( { \sf y } = 0 , 1 \right)$ 寄存器还具有以下限制：对于计数器时钟分频低于 32（CNTCKDIV [2：$0 ] < 5 )$ ），最低有效位忽略。它们不能进行写操作和读操作时值为零。详见 25-6.

y(y=0,1) 。 


表 25-6. 计数器和捕获 y(y=0,1)寄存器限值


<table><tr><td>CNTCKDIV[2:0]</td><td>无效位</td></tr><tr><td>3&#x27;b000</td><td>位 4~位 0</td></tr><tr><td>3&#x27;b001</td><td>位 3~位 0</td></tr><tr><td>3&#x27;b010</td><td>位 2~位 0</td></tr><tr><td>3&#x27;b011</td><td>位 1~位 0</td></tr><tr><td>3&#x27;b100</td><td>位 0</td></tr><tr><td>3&#x27;b101</td><td>x</td></tr><tr><td>3&#x27;b110</td><td>x</td></tr><tr><td>3&#x27;b111</td><td>x</td></tr></table>


注意：“x”表示所有位都有效。


## 计数器时钟

Slave_TIMERx 的时钟源是来自 RCU 模块的 HRTIMER_CK，DLL 用于产生高分辨率时钟HRTIMER_HPCK（f<sub>HRTIMER_HPCK</sub> = 32 * f<sub>HRTIMER_CK</sub>），更多信息请参考 DLL 。

预分频器（PSC）将高分辨率时钟（HRTIMER_HPCK）除以分频因子 2CNTCKDIV[2:0]，得到计数器时钟（HRTIMER_PSCCK）。该分频因子由 HRTIMER_STxCTL0 寄存器中的 CNTCKDIV[2:0]位域控制。它们之间的频率关系可以表示如下：

$$
f _ {\text { HRTIMER\_PSCCK }} = f _ {\text { HRTIMER\_HPCK }} / 2 ^ {\text { CNTCKDIV[2:0] }}\tag{25-2}
$$

注意：一旦 Slave_TIMERx 使能了，就不能修改时钟分频 CNTCKDIV[2:0]的值，CNTCKDIV[2:0]在 HRTIMER_STxCTL0 寄存器中。

参考 25-3. 16 和 25-2. fHRTIMER<sub>_CK</sub> = 216MHz 可得更多细节。

## 向上计数模式

计数器从 0 连续递增到计数器重载值，该值在 HRTIMER_STxCAR 寄存器中定义。计数器有两种工 作 模 式 ： 单 脉 冲 模 式 （ HRTIMER_STxCTL0 寄 存 器 中 的 CTNM = 0 ） 和 连 续 模 式（HRTIMER_STxCTL0 寄存器中的 CTNM = 1）。

在单脉冲模式下，将 HRTIMER_MTCTL0 寄存器中的 STxCEN 位置 1 后，第一个复位事件将启动计数器。当计数到计数器重载值时，计数器停止并生成周期事件。然后，其他的复位事件将复位并重新启动计数器。在计数过程中，如果 HRTIMER_STxCTL0 寄存器中的 CNTRSTM = 1，则复位事件将复位并重新启动计数器，否则将被忽略。 25-4. 显示了单脉冲模式下的计数器运行情况。

在连续模式下，一旦 HRTIMER_MTCTL0 寄存器中的 STxCEN 位置 1，计数器将立即启动。当计

数到计数器重载值时，计数器从 0 重新启动，并产生翻转事件。与单脉冲模式不同，随时生成的复位事件将复位并重启计数器。 25-5. 显示了连续模式下的计数器运行情况。

## 重复计数器

HRTIMER_MTCTL0 寄存器中的 STxCEN 位置 1 时，重复计数器将加载 HRTIMER_STxCREP 寄存器的值。当由于复位事件或连续模式下的翻转事件清零计数器时，重复计数器值递减。当重复计数器值达到零时，复位事件或连续模式下的翻转事件将产生一个重复事件并重新加载HRTIMER_STxCREP 寄存器的值。

重复事件会将 HRTIMER_STxINTF 寄存器中的 REPIF 位置 1，如果使能了相应中断或 DMA请求（HRTIMER_STxDMAINTEN 寄存器中的 REPIE = 1 或 REPDEN = 1），则会产生重复中断和DMA 请求。可以通过向 HRTIMER_STxINTFC 寄存器中的 REPIFC 位写 1，清除重复中断标志。

连续模式下重复计数器的运行情况如 25-6. 所示。

单脉冲模式下，CNTRSTM = 0 时重复计数器的运行情况如 25-7. CNTRSTM =0时重复计数器的动作所示。

单脉冲模式下，CNTRSTM = 1 时重复计数器的运行情况如 25-8. CNTRSTM =1时重复计数器的动作所示。

## 计数器复位

计数器可以通过以下三种信号源复位：

1.软件。软件写 1 到 HRTIMER_CTL1 寄存器的 STxSRST 位。

2.同步输入启动/复位计数器。

3.HRTIMER_STxCNTRST 寄存器和 HRTIMER_STxCNTRSTA 寄存器中配置的事件。

所有这些源都是逻辑或，它们可以同时有效。如果在同一 t<sub>HRTIMER_CK</sub>周期中发生多个复位事件，则仅最后一个有效。

注意：如果外部事件配置为电平有效，则只能在 HRTIMER_STxCNTRST 寄存器中启用一个外部事件。

写 1 到 STxSRST 位（由硬件自动清除）使计数器复位。Master_TIMER 和 Slave_TIMERx（x =0..7）的这些控制位都在 HRTIMER_CTL1 寄存器中，可以同时复位多个计数器。

当 HRTIMER_STxCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以复位计数器。请参考。

可以在 HRTIMER_STxCNTRST 和 HRTIMER_STxCNTRSTA 寄存器中同时配置 39 个事件来复位计数器，这些事件可以分为四类：

 Slave_TIMERx：更新事件，比较1事件和比较3事件；

 其他Slave_TIMERy（例如x = 1，则 $y = 0 , \ 2 . . 7 )$ ：比较0事件，比较1事件和比较3事件；

 Master_TIMER：比较0事件，比较1事件，比较2事件，比较3事件和复位事件；

 外部事件y $( \mathsf { y } = 0 . . 9 )$ ：EXEVy为Slave_TIMERx中的外部事件的滤波信号。

当计数器时钟 HRTIMER_PSCCK 的预分频系数大于 16（CNTCKDIV [2:0] > 3’b101）时，计数器复位事件将延迟到HRTIMER_PSCCK的下一个上升沿。具体请见 25-9. 64复位事件重新同步

计数器复位事件会将 HRTIMER_STxINTF 寄存器中的 RSTIF 位置 1，如果使能了计数器复位中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 RSTIE = 1 或 RSTDEN = 1），则会产生复位中断或 DMA 请求。可通过向 HRTIMER_STxINTFC 中的 RSTIFC 位写 1，清除复位中断标志。

## 捕获

捕获功能不仅使 Slave_TIMERx 实现了脉冲宽度，频率，周期，占空比的测量，而且还可以在延迟模式下（参见 ）更新比较 1 寄存器和比较 3 寄存器的值。

当选定的触发信号发生时，计数器的当前值被捕获到 HRTIMER_STxCAPyV（y = 0,1）寄存器中。同时，HRTIMER_STxINTF 寄存器中的 CAPyIF（y = 0,1）位置 1，如果 HRTIMER_STxDMAINTEN寄存器中的 CAPyIE $( \mathsf { y } = 0 , 1 ) = 1$ 或 CAPyDEN $( \mathsf { y } = 0 , 1 ) = 1$ ，则生成相应的捕获中断和 DMA请求。可以通过写 1 到 HRTIMER_STxINTFC 寄存器中的 CAPyIFC 位来清除捕获中断标志位CAPyIF。

捕 获 0 触 发 事 件 在 HRTIMER_STxCAP0TRG 寄 存 器 中 定 义 ， 捕 获 1 触 发 事 件 在HRTIMER_STxCAP1TRG 寄存器中定义。当选择了多个触发事件时，所有的触发事件是逻辑“或”运算的。

注意： 如 果 将 外 部 事 件 配 置 为 具 有 电 平 有 效 ， 则 只 能 在 HRTIMER_STxCAP0TRG 和HRTIMER_STxCAP1TRG 寄存器中使能一个外部事件。

捕获溢出是无法防止的，即使先前的捕获值未读取或捕获标志未清除，新的捕获仍将被触发，并且新的捕获值将覆盖先前的值。请参考 25-11. EXEV0 EXEV1 0。


图 25-11. EXEV0 和 EXEV1 触发捕获 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/79fe2daacc174c409bb85f5f427fa640c59ba94fafb5b76f0ed75224f2e4afed.jpg)


## 比较

Slave_TIMERx 单元有四个比较寄存器：HRTIMER_STxCMPyV（y = 0..3）。当计数器值与比较寄存器值匹配时，将产生一个比较事件。具体请见 25-12. STxCAR=0x8, STxCMP1V=0x02比较1寄存器的动作

比较事件会将相应的比较中断标志位置 1（HRTIMER_STxINTF 中的 CMPyIF 位，其中 y = 0..3），如果使能了比较中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CMPyIE = 1 或CMPyDEN = 1，其中 y = 0..3），则会生成比较中断或 DMA 请求。通过写 1 到 HRTIMER_STxINTFC中的 CMPyIF 位可以清除比较中断标志。


图 25-12. STxCAR=0x8, STxCMP1V=0x02 时，比较 1 寄存器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/749de79904c7b8bbf661580312882862bbb761c09075dcd63d8127ff2d264dc3.jpg)


## 半波模式

当 HRTIMER_STxCTL0 中的 HALFM 位置 1 时，半波模式使能。此模式将比较 0 有效寄存器的值强 制 为 计 数 器 重 载 值 的 一 半 ， 但 HRTIMER_STxCMP0V 寄 存 器 的 值 不 会 更 新 为（HRTIMER_STxCAR / 2）的值。半波模式主要用于生成固定占空比为 50％的方波。

当 HRTIMER_STxCTL0 寄存器中的 SHWEN 位置 1 时，将使能影子寄存器，比较 0 有效寄存器

的值在更新事件时刷新。反之，比较 0 有效寄存器在新值写入后立即刷新。

## 交错模式

此模式有助于实现与半波模式相辅相成的替代拓扑结构。当 HRTIMER_STxCAR 值更新时，比较值寄存器会被自动重新计算。通过 HRTIMER_STxCTL0 和 HRTIMER_STxCTL0 中的 HALFM 位和 ALTM[1:0]位选择交错模式，交错模式仅在 HALFM 位置 0 时有效。


表 25-7. 交错模式选择


<table><tr><td>ALTM[1:0]</td><td>交错模式</td></tr><tr><td>00</td><td>禁止</td></tr><tr><td>01</td><td>三重交错(120°)</td></tr><tr><td>10</td><td>四重交错(90°)</td></tr><tr><td>11</td><td>保留</td></tr></table>

25-4. 显示了交错模式的有效寄存器比较值，比较有效寄存器的内容将被覆盖，相应的比较事件可用作触发器，以设置或复位从定时器。


表 25-8. 两种交错模式比较值


<table><tr><td>模式</td><td>三重交错模式(120°)</td><td>四重交错模式(90°)</td></tr><tr><td>HRTIMER_STxCMP0V</td><td>HRTIMER_STxCAR /3</td><td>HRTIMER_STxCAR /4</td></tr><tr><td>HRTIMER_STxCMP1V</td><td>2 x HRTIMER_STxCAR /3</td><td>2 x HRTIMER_STxCAR /4</td></tr><tr><td>HRTIMER_STxCMP2V</td><td>无影响</td><td>3 x HRTIMER_STxCAR /4</td></tr></table>

注意：在交错模式中，比较寄存器由硬件控制，软件写入对比较寄存器无效。预装载寄存器保存比较值，并在退出交错模式后生效。

## 空占空比异常情况

HRTIMER 不支持小于 3 个 t<sub>HPTMER_CK</sub> 时钟周期的输出脉冲，具体参考。例如，如果 $\mathsf { C N T C K D I V } [ 2 ; 0 ] = 3 ^ { \prime } \mathsf { b 0 0 0 }$ ，则为 0x60，如果 $\mathsf { C N T C K D I V } [ 2 : 0 ] = 3 ^ { \mathsf { ! } } 6 0 0 1$ ，则为0x30，如果 $\mathsf { C N T C K D I V } [ 2 : 0 ] = 3 ^ { \prime } \mathsf { b } 0 1 0$ ，则为 0x18。小于上述值的脉冲无法正常输出。

通过在 HRTIMER_STxCMP0V 和 HRTIMER_STxCMP2V 中写入空值，并配置以下操作。在HRTIMER 周期中将跳过一个脉冲。

 更新事件生成通道 0 的“置位请求”。

 比较 0（比较 2）事件生成“复位请求”。

 比较 0（比较 2）事件仅在比较事件所属的计时器单元中有效。

在上述应用条件下，重新编写比较值 HRTIMER_STxCMP0V 和 HRTIMER_STxCMP2V，它们之间的差值大于 3，将会恢复正常输出。

## 交换模式

HRTIMER_CTL1 中设置 EXCx，可以交换 Slave timer 的两个输出 CH0 和 CH1，并且两个通道的输出在下一个更新事件发生时生效。在置位和复位之前，两个输出 CH0 和 CH1 将按照以下交叉方式进行：

■ 如果EXCx = 0，则STxCH0SET和STxCH0RST控制CH0的输出，STxCH1SET和STxCH1RST控制CH1的输出。

 如果EXCx = 1，则STxCH0SET和STxCH0RST控制CH1的输出，STxCH1SET和STxCH1RST控制CH0的输出。

注意：交换模式仅影响预装载寄存器；在使用交换模式时，必须启用影子寄存器。

## 比较延迟模式

此模式仅用于比较 y（y = 1,3）寄存器，并由 HRTIMER_STxCTL0 寄存器中的 DELCMPyM[1:0]位域控制。比较寄存器与计数器比较的实际值是重新计算值，该值在捕获 0/1 触发或比较 0/ 2 事件之后重新计算得到，具体如 25-13. 。此模式允许通过硬件将生成的波形与捕获触发同步。


图 25-13. 比较延迟模式框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e6f05dd36eee13bc0d60f0afa2e0b19cf6336ee79e625a312518424141f520b3.jpg)


在延迟模式下，比较 y（y = 1，3）事件从相应的捕获/比较事件发生到周期事件期间有效。当计数器达到周期值时，将禁用比较 y（y = 1，3）事件，直到出现新的捕获/比较事件。

当没有捕获触发或比较事件发生时，不生成比较 y 事件。捕获触发事件发生后，将比较 y 有效寄存器中的值与对应的 HRTIMER_STxCAP0V 或 HRTIMER_STxCAP1V 寄存器值相加，然后将其与计数器进行比较。比较 1 寄存器与捕获 0 寄存器和比较 0 寄存器/比较 2 寄存器关联，而比较 3寄存器与捕获 1 寄存器和比较 0 寄存器/比较 2 寄存器关联。

注意：重新计算的值被传输到一个内部寄存器，且无法读取。

HRTIMER_STxCTL0 寄存器中的 DELCMP1M[1:0]位域（比较 1 事件）和 DELCMP3M[1:0]位域（比较 3 事件）可用于配置延迟模式。下面以 DELCMP1M[1:0]为例：

##  2’b00，比较1延迟模式禁能

比较 1 延迟模式禁用。一旦计数器值等于比较 1 寄存器的值，就会发生比较匹配。参见 25-12.STxCAR=0x8, STxCMP1V=0x02 1 。

##  2’b01，比较1延迟模式0

捕获 0 事件发生后，将重新计算比较 1 寄存器的值（比较 1 有效寄存器值+捕获 0 寄存器值）。一旦计数器值等于重新计算后的比较 1 寄存器值，就会发生比较 1 事件。参见 25-14. 10。


图 25-14. 比较 1 延迟模式 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/73c19ec4805ea4b1dd51d349665b1fd84127a24cf69c30120f31fffce63b2efb.jpg)


##  2’b10，比较1延迟模式1

在捕获 0 事件或比较 0 事件之后，将重新计算比较 1 寄存器的值。

发生捕获0事件时，比较1寄存器的重新计算值 = 比较1有效寄存器值 + 捕获0事件的捕获值。

发生比较0事件时，比较1寄存器的重新计算值 = 比较1有效寄存器值 + 比较0有效寄存器值。

一旦计数器值等于重新计算的比较 1 寄存器值，就会发生比较 1 事件。如果捕获 0 事件先发生，则比较 0 事件将被忽略。同样，如果先发生比较 0 事件，则将忽略捕获 0 事件。详情请见 25-15.1 1。


图 25-15. 比较 1 延迟模式 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/af101778d9b855c0070e58ffce21b29204180529b63ee1bc70eb327bc91cb870.jpg)


##  2’b11，比较1延迟模式2

该模式与比较 1 延迟模式 1 相同。在捕获 0 事件或比较 2 事件之后，重新计算比较 1 寄存器的值。

$$
\text {发生捕获} 0 \text {事件时, 比较} 1 \text {寄存器的重新计算值} = \text {比较} 1 \text {有效寄存器值} + \text {捕获} 0 \text {事件的捕获值。}
$$

发生比较2事件时，比较1寄存器的重新计算值 = 比较1有效寄存器值 + 比较2有效寄存器值。

一旦计数器值等于重新计算的比较 1 寄存器值，就会发生比较 1 事件。如果捕获 0 事件先发生，则比较 2 事件将被忽略。同样，如果先发生比较 2 事件，则将忽略捕获 0 事件。详见 25-15.1 1。

影子寄存器（SHWEN = 0）禁能时，即使在发生捕获事件后修改 HRTIMER_STxCMP0V 位或HRTIMER_STxCMP2V 位的值，新的比较值也会立即被带入有效寄存器。 25-16.SHWEN=0 显示了一个示例：

在 t0 处发生捕获事件，C1 值被捕获到寄存器中，重新计算的值 = 比较有效寄存器的值 + C1。在 t1 处将新的比较值（C2）写入比较寄存器，则重新计算的值 = C2 + C1。


图 25-16.比较延迟模式（SHWEN=0）


<table><tr><td colspan="5">MTCEN或STxCEN(x=0..4)</td></tr><tr><td colspan="5">(前值+C1)</td></tr><tr><td colspan="5">(C2+C1)</td></tr><tr><td colspan="2">CounterCTNM=1</td><td colspan="2">预装载值=前值有效值=前值+C1</td><td>更新事件</td></tr><tr><td colspan="2">捕获事件</td><td colspan="2"></td><td></td></tr><tr><td>捕获寄存器</td><td>前值</td><td colspan="2">C1</td><td></td></tr><tr><td>比较寄存器</td><td>前值</td><td>预装载值=前值有效值=前值重计算值=前值+C1</td><td>预装载值=C2有效值=C2重计算值=C2+C1</td><td>预装载值=C2有效值=C2重计算值=无效</td></tr><tr><td>比较事件</td><td></td><td>t0</td><td>t1</td><td></td></tr></table>


使用延迟模式（DELCMP3M [1:0] = 01，10,11），可以防止捕获溢出发生。在同一个计数周期（由HRTIMER_STxCAR 确定）内，仅考虑第一个捕获事件。新的捕获事件在以下三种情况下有效：


 当比较寄存器的重新计算值与计数器值匹配时；

 发生了周期事件；

 计数器复位。

## 可变频率半波模式

可变频率半波模式是半波模式的补充，该模式允许调节输出信号频率，同时保持 180°相位移。该模式的主要原理是主从模式，从定时器（Slave_TIMERy）通过主定时器（Slave_TIMERx）的捕获事件不断进行调整。

主 定 时 器 （ Slave_TIMERx ） 产 生 捕 获 事 件 后 ， 硬 件 自 动 将 捕 获 值 的 一 半 存 储 在HRTIMER_STxCMP1V 中。从定时器（Slave_TIMERy）置位或复位事件可以由主定时器（Slave_TIMERx）的比较 1 事件触发。

通 过 在 HRTIMER_STxCTL1 中 设 置 TRGHALFM ， 可 启 用 可 变 频 率 半 波 模 式 ， 当HRTIMER_MTCTL0 中的 STxCEN 置位时，此位不能更改。

用户可以写入 HRTIMER_STyCMP1V 的初始值，当第一次捕获发生时，初始值将被忽略。并且当HRTIMER_STxCTL1 中的 TRGHALFM 被复位时，HRTIMER_STyCMP1V 将不会被预加载。\
图 25-17.可变频率半波模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/bdc84a9f10807167065206e7b8680f9652c27442b586a7a13fcec8c05474e8ee.jpg)



如 25-17. 所示。


HRTIMER_STxCH0 由外部事件 0（EXEV0）置位，并由外部事件 1（EXEV1）复位，同时外部事件 0 触发产生捕获事件。

 HRTIMER_STyCH0由HRTIMER_STxCMP1V置位，并由EXEV2复位

 HRTIMER_STxCH1由HRTIMER_STxCMP0V置位，并由HRTIMER_STxCMP1V复位

## 立即更新模式

HRTIMER 的立即更新模式适用于比较 0 复 位 事 件 和 比 较 2 复 位 事 件 ， 并 通 过 在HRTIMER_STxCTL1 寄存器中设置 IMUPDxV 位来启用此模式。当启用立即更新模式时，PWM波形会立即更新，而无需等待当前周期结束。在以下情况下，PWM 波形会立即更改。

 在运行过程中更改比较值时，如果新的比较值小于计数器值且当前比较值大于计数器值，则会立即复位输出PWM波形。

 在运行过程中更改比较值时，如果新的比较值大于计数器值且当前比较值大于计数器值，则会立即设置输出PWM波形。

 当新的比较值和当前值均小于计数器值时，输出PWM波形不会更改。


图 25-18. 当 IMPUD2V = 1 和 IMPUD2V = 0 时输出的 PWM 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/60f53a9bd5526edb5427d4029a1ac21cfffc370a4248db268ba530c25f88af8c.jpg)


## 置位/复位交叉开关

通道输出波形功能由三个部分实现：

 置位/复位交叉开关

 空闲控制

 通道输出级

25-19. 显示了这三个部分的结构。


图 25-19. 通道输出结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/0817e3740e950578bb7a8dd378d2bfd72bd8c3a7e3cbbb12e37baafe13f18b4c.jpg)



交叉开关模块有三种输出模式：常规模式，死区时间模式和均衡模式，输出时只能选择其中一种模式。


## 向上计数模式下输出准备信号

Slave_TIMERx 有一个置位/复位输出模块。该模块可以生成两个输出准备信号：O0PRE和O1PRE。其中，O0PRE 由 HRTIMER_STxCH0SET 和 HRTIMER_STxCH0RST 寄存器控制。O1PRE 由HRTIMER_STxCH1SET 和 HRTIMER_STxCH1RST 寄存器控制。OyPRE（y = 0,1）的高电平为有效电平，低电平为无效电平。

当 HRTIMER_STxCHySET 寄存器中配置的事件发生时，此模块将产生置位请求，并使 OyPRE 输出高电平。当 HRTIMER_STxCHyRST 寄存器中配置的事件发生时，此模块会产生复位请求，并使 OyPRE 输出低电平。如果在 HRTIMER_STxCHySET 和 HRTIMER_STxCHyRST 寄存器中配置了相同的事件，则此模块会生成输出翻转请求，并在配置的事件发生时使 OyPRE 输出翻转。

注意：如果 HRTIMER_STxCTL0 和 HRTIMER_STxACTL 寄存器中的 CNTCKDIV[2:0]位域等于3’b110 或 3’b111，则不得同时设置 HRTIMER_STxCH0SET 和 HRTIMER_STxCH0RST 寄存器中的同一事件。

25-20. O0PRE CMP0 CMP1 显示了以下配置时的 O0PRE 输出波形：

 HRTIMER_STxCTL0寄存器中的CNTCKDIV [2:0] = 3’b000；

 HRTIMER_STxCH0SET= 0x0000 0008：比较0事件产生置位请求，O0PRE将输出高电平；

 HRTIMER_STxCH0RST= 0x0000 0010：比较1事件产生复位请求，O0PRE将输出低电平；

 HRTIMER_STxCMP0V = 0x00A0； 

 HRTIMER_STxCMP1V = 0x01C0。 

## 图 25-20. O0PRE 波形：CMP0 事件置位，CMP1 事件复位

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/2b4f2aed012254ac2bca0fc77d8ea1164e39fd6c19bd9b6d6eaa438fa506edda.jpg)


OyPRE（y = 0,1）最多可以选择 34 个事件：

 Slave_TIMERx：更新事件，复位事件，周期事件和比较y（y = 0..3）事件；

 Master_TIMER：周期事件，比较y（y = 0..3）事件；

Slave_TIMERx互连事件：其他Slave_TIMERy有11个互连事件（例如x = 1，然后y = 0，2..7）,参见 25-9. Slave_TIMER ；

 外部事件y（y = 0..9）：EXEVy为Slave_TIMERx中的外部事件的滤波信号；

 软件事件。

无论 STxCEN 位是否为 1，软件事件始终有效。但是，只有 STxCEN 为 1 时，才会考虑其他事件。


表 25-9. Slave_TIMER 内部连接事件


<table><tr><td colspan="2">内部连接</td><td>到 ST0</td><td>到 ST1</td><td>到 ST2</td><td>到 ST3</td><td>到 ST4</td><td>到 ST5</td><td>到 ST6</td><td>到 ST7</td></tr><tr><td rowspan="4">来自 ST0</td><td>CMP0</td><td>x</td><td>0</td><td>x</td><td>0</td><td>x</td><td>x</td><td>x</td><td>0</td></tr><tr><td>CMP1</td><td>x</td><td>1</td><td>0</td><td>x</td><td>x</td><td>x</td><td>0</td><td>x</td></tr><tr><td>CMP2</td><td>x</td><td>x</td><td>1</td><td>x</td><td>x</td><td>0</td><td>x</td><td>x</td></tr><tr><td>CMP3</td><td>x</td><td>x</td><td>x</td><td>1</td><td>0</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="4">来自 ST1</td><td>CMP0</td><td>0</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>x</td><td>1</td></tr><tr><td>CMP1</td><td>1</td><td>x</td><td>2</td><td>2</td><td>x</td><td>x</td><td>x</td><td>2</td></tr><tr><td>CMP2</td><td>x</td><td>x</td><td>3</td><td>x</td><td>1</td><td>x</td><td>1</td><td>x</td></tr><tr><td>CMP3</td><td>x</td><td>x</td><td>x</td><td>3</td><td>2</td><td>2</td><td>2</td><td>x</td></tr><tr><td rowspan="4">来自 ST2</td><td>CMP0</td><td>x</td><td>x</td><td>x</td><td>x</td><td>3</td><td>3</td><td>3</td><td>x</td></tr><tr><td>CMP1</td><td>2</td><td>x</td><td>x</td><td>x</td><td>4</td><td>x</td><td>x</td><td>x</td></tr><tr><td>CMP2</td><td>3</td><td>2</td><td>x</td><td>x</td><td>x</td><td>x</td><td>4</td><td>3</td></tr><tr><td>CMP3</td><td>x</td><td>3</td><td>x</td><td>4</td><td>x</td><td>4</td><td>x</td><td>4</td></tr><tr><td rowspan="4">来自 ST3</td><td>CMP0</td><td>4</td><td>x</td><td>x</td><td>x</td><td>5</td><td>x</td><td>5</td><td>x</td></tr><tr><td>CMP1</td><td>5</td><td>x</td><td>4</td><td>x</td><td>6</td><td>x</td><td>6</td><td>5</td></tr><tr><td>CMP2</td><td>x</td><td>4</td><td>x</td><td>x</td><td>x</td><td>5</td><td>x</td><td>x</td></tr><tr><td>CMP3</td><td>x</td><td>5</td><td>5</td><td>x</td><td>x</td><td>6</td><td>x</td><td>6</td></tr><tr><td rowspan="4">来自 ST4</td><td>CMP0</td><td>x</td><td>6</td><td>x</td><td>5</td><td>x</td><td>x</td><td>x</td><td>7</td></tr><tr><td>CMP1</td><td>x</td><td>7</td><td>x</td><td>x</td><td>x</td><td>7</td><td>7</td><td>x</td></tr><tr><td>CMP2</td><td>6</td><td>x</td><td>6</td><td>x</td><td>x</td><td>8</td><td>8</td><td>x</td></tr><tr><td>CMP3</td><td>7</td><td>x</td><td>7</td><td>6</td><td>x</td><td>x</td><td>x</td><td>8</td></tr><tr><td rowspan="4">来自 ST5</td><td>CMP0</td><td>x</td><td>x</td><td>x</td><td>7</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>CMP1</td><td>x</td><td>x</td><td>8</td><td>x</td><td>x</td><td>x</td><td>x</td><td>9</td></tr><tr><td>CMP2</td><td>x</td><td>8</td><td>x</td><td>8</td><td>7</td><td>x</td><td>9</td><td>x</td></tr><tr><td>CMP3</td><td>8</td><td>x</td><td>x</td><td>x</td><td>8</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="4">来自 ST6</td><td>CMP0</td><td>x</td><td>x</td><td>9</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>CMP1</td><td>x</td><td>9</td><td>x</td><td>9</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>CMP2</td><td>9</td><td>x</td><td>x</td><td>x</td><td>9</td><td>x</td><td>x</td><td>10</td></tr><tr><td>CMP3</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>9</td><td>x</td><td>x</td></tr><tr><td rowspan="4">来自 ST7</td><td>CMP0</td><td>x</td><td>x</td><td>x</td><td>10</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>CMP1</td><td>x</td><td>x</td><td>10</td><td>x</td><td>10</td><td>x</td><td>10</td><td>x</td></tr><tr><td>CMP2</td><td>x</td><td>10</td><td>x</td><td>x</td><td>x</td><td>10</td><td>x</td><td>x</td></tr><tr><td>CMP3</td><td>10</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr></table>


注意：（1）表中的数字表示 Slave_TIMERx 互连事件。


（2）“x”代表无效。

可以同时选择多个事件源（进行逻辑或运算），并且当它们在同一 t<sub>HPTMER_CK</sub> 周期内发生时，将执

行仲裁。

## 中央对齐模式下输出准备信号

在中央对齐计数模式下，计数器从 0 计数到计数器重载值，然后从该值减少到 0。通过在HRTIMER_STxCTL1 中设置 CAM 位来启用该模式，中央对齐计数模式仅适用于 Slave_TIMERx（x = 0..7），而不适用于 Master_TIMER。

只有在发生周期事件或复位事件时，Slave_TIMERx 的周期 HRTIMER_STxCAR 的预装载值会被更新。

当在 HRTIMER_STxCHySET 寄存器中配置的事件发生时，此模块产生一个置位请求，并使OyPRE 在上升计数期间保持高电平，在下降计数期间保持低电平。当在 HRTIMER_STxCHyRST中配置的事件发生时，此模块产生一个复位请求，并使 OyPRE 在上升计数期间保持低电平，在下降 计 数 期 间 保 持 高 电 平 。 如 果 将 相 同 的 事 件 配 置 在 HRTIMER_STxCHySET 和HRTIMER_STxCHyRST寄存器中，此模块将产生一个翻转请求，并在配置的事件发生时使OyPRE输出翻转。

有多达 34 个事件可用于选择 OyPRE(y=0,1)，参考 。


图 25-21. 中央对齐模式下 OyPRE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/d9205efcbd2024616970e5f5ea1693f8f250258432a6c3d1d75a3d5dd1a8919a.jpg)


中央对齐模式可以在半波模式、死区模式、均衡模式、延迟空闲模式、突发模式和立即更新模式中使用。

HRTIMER_STxCAPyV （ x=0..7 ， y=0..3 ） 的 捕 获 值 在 向 上 计 数 时 参 考 起 始 值 ，HRTIMER_STxCAPyV = HRTIMER_STxCNT，HRTIMER_STxCAPyV（x=0..7，y=0..3）的捕获值 在 向 下 计 数 时 参 考 自 动 重 载 值 ， HRTIMER_STxCAPyV = HRTIMER_STxCAR -HRTIMER_STxCNT。HRTIMER_STxCAPyV 寄存器中的 DIR 显示计数方向。用于置位或复位OxPRE 的周期事件在 HRTIMER_STxCTL1 寄存器中由 ROVM[1:0]位定义。当 ROVM[1:0] = 2b00时，周期事件在计数器等于 0 或等于 HRTIMER_STxCAR 值时生成；当 ROVM[1:0] = 2b01 时，周期事件在计数器等于 0 时生成；当 ROVM[1:0] = 2b10 时，周期事件在计数器等于HRTIMER_STxCAR 时生成。


图 25-22. 中央对齐模式下重复计数器值 CREP[7:0]和 ROVM[1:0]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/300c95957fadb6541e8655b9a5efe533dd0d53a74a460863fdcdee381fabbdbb.jpg)


HRTIMER 具有消隐模式和窗口模式，在向上计数模式和中央对齐模式中，消隐时间和窗口时间不同。


表 25-10. 消隐模式和窗口模式在向上计数模式和中央对齐模式


<table><tr><td>EXEV0FM[4:0]</td><td>向上计数模式</td><td>中央对齐模式</td></tr><tr><td>00010</td><td>消隐从周期事件到比较1事件</td><td>消隐从比较0事件到比较1事件,仅在中央对齐模式向上计数有效</td></tr><tr><td>00100</td><td>消隐从周期事件到比较3事件</td><td>消隐从比较2事件到比较1事件,仅在中央对齐模式向上计数有效</td></tr><tr><td>01101</td><td>窗口从周期事件到比较1事件</td><td>窗口从比较1事件到比较2事件,仅在中央对齐模式向上计数有效</td></tr><tr><td>01110</td><td>窗口从周期事件到比较2事件</td><td>窗口从比较1事件到比较2事件,仅在中央对齐模式向下计数有效</td></tr></table>


GD32G553 用户手册


<table><tr><td>EXEV0FM[4:0]</td><td>向上计数模式</td><td>中央对齐模式</td></tr><tr><td>01111</td><td>窗口从周期事件来自其他定时器</td><td>窗口从比较1事件(向上计数)到比较2事件(向下计数),仅在中央对齐模式有效</td></tr></table>

## 仲裁机制

当 HRTIMER_STxCH1SET 和 HRTIMER_STxCH1RST 寄存器中配置的多个事件发生在同一个t<sub>HPTMER_CK</sub>周期内时，将执行仲裁过程，且只有一个事件有效，可以更改 OyPRE（y = 0,1）的输出。

这 35 个事件可以分为五种类型：

 Slave_TIMERx：比较y（y = 0..3）事件，周期事件。

 Master_TIMER：比较y（y = 0..3）事件，周期事件。

 Slave_TIMERx互连事件：互连事件y（y = 0..10）

■ 低精度事件：Slave_TIMERx的更新事件和复位事件，外部事件y（y = 0..9），软件事件。

 计数器复位事件：使用最大延时。

具体的仲裁过程 25-23. tHRTMER<sub>_CK</sub> 所示。


图 25-23. 每个 t<sub>HRTMER_CK</sub> 周期的仲裁机制过程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/be803b441daab8d813e9c8fd98486a01ed4fa0bf1b3ae3eb3b8c1d1cca0c0936.jpg)



三个仲裁器的功能如下：


 仲裁器 0 的优先级顺序（从最高优先级到最低优先级）：

比较 3 事件 > 比较 2 事件 > 比较 1 事件 > 比较 0 事件 > 周期事件。

 仲裁器 1 根据事件在 t<sub>HPTMER_CK</sub>期间的延迟来仲裁优先级：

延迟越小，优先级越高。

 仲裁器 2 根据事件对 OyPRE（y = 0,1）输出的影响来仲裁优先级：

复位请求 > 输出翻转请求 > 置位请求。

以 Slave_TIMER0 中的 O0PRE 输出为例，配置如下：

 HRTIMER_STxCH0SET = 0x0060 5898，选定产生置位请求的事件是：

Master_TIMER：比较 2 事件，周期事件；

Slave_TIMER0：比较 1 事件，比较 0 事件；

Slave_TIMER0 的互连事件：互连事件 0（Slave_TIMER1 比较 0 事件），互连事件 2（Slave_TIMER1比较 3 事件）；

低精度事件：外部事件 0（EXEV0），外部事件 1（EXEV1）。

计数器复位事件。

 HRTIMER_STxCH0RST = 0x0198 0344，选定产生复位请求的事件是：

Master_TIMER：比较 0 事件，比较 1 事件；

Slave_TIMER0：比较 3 事件，周期事件；

Slave_TIMER0 的互连事件：互连事件 7（Slave_TIMER4 比较 2 事件），互连事件 8（Slave_TIMER4比较 3 事件）；

低精度事件：外部事件 2（EXEV2），外部事件 3（EXEV3）。

 延迟：Slave_TIMER4 比较 3 < Slave_TIMER0 比较 3

上述选定的事件如果在同一个 t<sub>HRTMER_CK</sub> 周期内发生，则仲裁过程和结果如Slave_TIMER4 3 tHRTMER<sub>_CK</sub> 期间有效，并且 O0PRE 将被设置为低电平。

图 25-24. 仲裁机制示例所示。最终，Slave_TIMER4 比较 3 事件产生的复位请求在该 t<sub>HRTMER_CK</sub>期间有效，并且 O0PRE 将被设置为低电平。


图 25-24. 仲裁机制示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/37326e7d82369bb4322770a75ddcece7a8e9c956faed66bd1a93ae1173061c88.jpg)


## 输出准备信号：窄脉冲管理

当几个输出置位和/或复位请求在 3 个连续的 t<sub>HRTMER_CK</sub> 周期内发生时，OyPRE（y = 0,1）输出信号是一个窄脉冲。窄脉冲的输出管理由 HRTIMER_STxCTL0 寄存器中的 CNTCKDIV[2:0]位域配置，有以下两种情形：

 情形0：CNTCKDIV[2:0] < 3’b101

 情形1：CNTCKDIV[2:0] >= 3’b101

## 情形 0：CNTCKDIV[2:0] < 3’b101

如果输出置位和复位请求在两个连续的 t<sub>HRTMER_CK</sub>周期内产生，则会生成脉宽为 1 个 t<sub>HPTMER_CK</sub>周期的脉冲。具体如 25-25. 1 tHRTMER<sub>_CK</sub> 所示。


图 25-25. 脉冲宽度为 1 个 t<sub>HRTMER_CK</sub> 周期


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/991f96c02c69f74cfa08d3bd4a1155d3b5c01a210cbd1daace8c3fd36620d48f.jpg)


如果输出置位和复位请求的时间间隔包括一个完整的 t<sub>HRTMER_CK</sub> 周期，则会生成脉宽为 2 个t<sub>HRTMER_CK</sub> 周期的脉冲。具体如 25-26. 2  tHRTMER<sub>_CK</sub> 所示。


图 25-26.脉冲宽度为 2 个 t<sub>HRTMER_CK</sub> 周期


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/ecf5367dcd03b58c503b87c5f800213e1421c00430fbfd03182b31b073367dfa.jpg)


如果输出置位和复位请求的时间间隔大于两个完整的 t<sub>HPTMER_CK</sub>周期，则需要使用超高分辨率时钟。具体如 25-27. OxPRE 所示。


图 25-27. 高分辨率 OxPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/4f3d6283c6e419d2234142c13583eb5ca1282e4b5654a1351a5b1c42673619a7.jpg)



情形 1: CNTCKDIV[2:0] >= 3’b101


这种情况下，即使在每个 t<sub>HRTIMER_CK</sub>周期内执行仲裁，发生在 1 个 HRTIMER_PSCCK 周期内的输出置位或复位请求，都会延迟到 HRTIMER_PSCCK 时钟的下一个有效边沿。

当来自不同事件源的置位请求和复位请求在 1 个 t 周期中同时发生时，复位请求具有最高优先级，详见 25-28. CNTCKDIV[2:0] = 3’b110 OxPRE 。


图 25-28. CNTCKDIV[2:0] = 3’b110 时的 OxPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/89745545c331924ffd1b72ffa7757f36efe92b6074a76c3f7d3fd5e29cd08ea5.jpg)


## 常规模式

当 HRTIMER_STxCHOCTL 寄存器中的 DTEN = 0，HRTIMER_STxCTL0 寄存器中的 BLNMEN= 0 时，置位/复位交叉开关以常规模式运行。

该模式中，C0OPRE 和 C1OPRE 是独立的。C0OPRE（C1OPRE）直接连接到 O0PRE（O1PRE）。当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，HRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 HRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，HRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或 DMA请求。通过将 1 写到 HRTIMER_STxINTFC中的 CH0ONAIFC 位可以清除 CH0ONAIF中断标志。

通道 1 与通道 0 输出情况相同。

25-29. C0OPRE 显示了以下配置时的 C0OPRE 波形：

 HRTIMER_STxCTL0寄存器中的 $\mathsf { I C N T C K D I V } [ 2 : 0 ] = 3 ^ { \prime } \mathsf { b 0 0 0 } ;$ ；

 HRTIMER $S \mathsf { T } \times C \mathsf { H 0 S E T } = 0 \times 0 0 0 0 0 0 0 0 0$ ：比较0事件产生置位请求，O0PRE输出高电平；

 HRTIMER $S \mathsf { T } \times C \mathsf { H 0 R S 7 } = 0 \times 0 0 0 0 0 0 0 1 0$ ：比较1事件产生复位请求，O0PRE输出低电平；

 HRTIMER $S \mathsf { T x C M P 0 V } = 0 \times 0 0 6 0 \vdots$ 

 HRTIMER_ $S { \mathsf { T } } { \boldsymbol { \times } } C { \mathsf { M P } } { \boldsymbol { 1 } } { \mathsf { V } } = 0 { \boldsymbol { \times } } 0 0 { \mathsf { E } } 0$ 


图 25-29. 常规模式下的 C0OPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/30e33af107198470c44f43d38012bc13429a84b5453012b6c0ea86ad3ff52898.jpg)


## 死区时间模式

当 HRTIMER_STxCHOCTL 寄存器中的 DTEN = 1，HRTIMER_STxCTL0 寄存器中的 BLNMEN= 0 时，置位/复位交叉开关在死区模式下运行。

死区模式中，只对 O0PRE 进行编程，以驱动 C0OPRE 和 C1OPRE 的输出。C0OPRE 和 C1OPRE是一对互补信号，在有效状态转换之间插入可编程的死区时间。

死区时间值是由 HRTIMER_STxDTCTL 寄存器中的 DTFCFG [15:0]位域和 DTRCFG [15:0]位域确定的。DTFCFG [15:0]位域定义在 O0PRE 下降沿之后的死区时间，而 DTRCFG [15:0]位域定义在 O0PRE 上升沿之后的死区时间。

注意：DTFCFG [8:0]和 DTRCFG [8:0]位域在 HRTIMER_STxDTCTL 寄存器中，DTFCFG [15:9]和 DTRCFG [15:9]位域在 HRTIMER_STxACTL 寄存器中

死区时间值可以由 HRTIMER_STxDTCTL 寄存器中的 DTRS 位和 DTFS 位配置为正或负。当需要某些波重叠时，可以定义负的死区时间值。

死区时间由 HRTIMER_STxDTCTL 寄存器中的 DTGCKDIV [3:0]位域定义的时钟确定。

注意：DTGCKDIV[3:0]位域在 HRTIMER_STxDTCTL 寄存器中。

当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，HRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 HRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，HRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或DMA请求。通过将 1写到HRTIMER_STxINTFC中的CH0ONAIFC位可以清除CH0ONAIF中断标志。

通道 1 与通道 0 输出情况相同。

25-30. C0OPRE C1OPRE 显示了 O0PRE 脉冲宽度大于死区时间时的 C0OPRE 和 C1OPRE 波形。


图 25-30. 具有死区时间的 C0OPRE 和 C1OPRE 互补输出波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/623625190ca878efc380a80b5a889b8766e437ff0522fb8b83342a753a613d23.jpg)



25-31. 显示了 O0PRE 脉冲宽度小于死区时间时的 C0OPRE和 C1OPRE 互补波形。



图 25-31. 脉宽小于死区时间时的互补波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/3ba8302e85fb047ac8d4068aa77e351755abfdfd97c17df6903d8ab09a6bb2dc.jpg)


## 均衡模式

当 HRTIMER_STxCHOCTL 寄存器中的 DTEN = 0，HRTIMER_STxCTL0 寄存器中的 BLNMEN= 1 时，置位/复位交叉开关在均衡模式下运行。当计数器在连续模式下运行时才能使用均衡模式，并且一旦使能了计数器就不得使其复位。

25-32. 显示了均衡模式的信号控制过程。


图 25-32. 均衡模式的结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/cc612f3bfc9808813a1894116bbe86cb40698b0afa8c4e4468dc1c7fa5c51325.jpg)



一旦接收到翻转事件，翻转逻辑模块的输出就会翻转。当翻转逻辑模块的输出为 1（高电平）时，


C0OPRE 连接到 O0PRE，C1OPRE 为无效电平（低电平）。当翻转逻辑模块的输出为 0（低电平）时，C1OPRE 连接到 O1PRE，C0OPRE 为无效电平（低电平）。

建 议 配 置 HRTIMER_STxCH0SET = HRTIMER_STxCH1SET ， HRTIMER_STxCH0RST =HRTIMER_STxCH1RST，实现相同波形的均衡操作。在进行其他应用时，也可以对两个输出进行不同的配置。

均衡模式禁能时，HRTIMER_STxINTF 寄存器中的 CBLNF 位将复位，该位用于指示当前哪个通道正在输出信号（O0PRE 或 O1PRE）。

当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，HRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 HRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..7）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，HRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（HRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或DMA请求。通过将 1写到HRTIMER_STxINTFC中的CH0ONAIFC位可以清除CH0ONAIF中断标志。

通道 1 与通道 0 输出情况相同。

25-33. C0OPRE C1OPRE 显示了以下配置时的 C0OPRE 和 C1OPRE波形：

HRTIMER_STxCH0SET = HRTIMER_STxCH1SET = 0x0000 0004：周期事件产生置位请求，O0PRE和O1PRE输出高电平；

■ HRTIMER_STxCH0RST = HRTIMER_STxCH1RST = 0x0000 0008：比较0事件产生复位请求，O0PRE和O1PRE输出低电平。


图 25-33. 均衡模式下的 C0OPRE 和 C1OPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/b987e264937a1a49236ab68ff3ec383f7ac2bb0cfd93aa3803d2cdfedfe4fa9d.jpg)


## 空闲控制

空闲控制级有三种控制空闲状态的方式：

 延迟空闲模式

 均衡空闲模式

 突发模式控制的空闲模式

延迟空闲和均衡空闲模式不能同时使用。均衡空闲仅在均衡模式下可用。延迟空闲或均衡空闲可以与突发模式控制的空闲模式同时使用，但突发模式的优先级最低。当置位/复位开关在不同模式下操作时，可以使用不同的空闲控制模式，详见 25-11. 。


表 25-11. 交叉开关和空闲控制同时运行


<table><tr><td>置位/复位交叉开关运行模式</td><td>IDLE 控制级运行模式</td></tr><tr><td>常规模式</td><td>延迟空闲,突发模式控制的空闲</td></tr><tr><td>死区时间模式</td><td>延迟空闲,突发模式控制的空闲</td></tr><tr><td>均衡模式</td><td>延迟空闲,均衡控制和突发模式控制空闲</td></tr></table>


HRTIMER_STxINTF 寄存器中的 CHyF(y=0,1)位，指示了 CHyOPRE 的输出电平。


## 延迟空闲

在 延 迟 空 闲 模 式 ， 所 选 外 部 事 件 （ 对 于 Slave_TIMER0/ 1/ 2 为 EXEV5/ 6 ， 对 于Slave_TIMER3/4/5/6/7 为 EXEV7/ 8）之后的置位请求或复位请求会导致 CHyOPRE（y = 0，1）输出进入空闲状态。具体情况与 HRTIMER_STxCHOCTL 寄存器中的 ISOy/ CHyP（y = 0,1）有关，详见 25-12. 。ISOy 位用于定义空闲状态时 CHyOPRE 的输出电平。空闲模式会永久保持，计数器将继续运行，直到重新使能输出才退出该模式。将 STxCH0EN和 STxCH1EN 位重新置 1 后，通过置位请求或复位请求可以重新使能延迟空闲模式。


表 25-12. 进入和退出空闲状态的请求


<table><tr><td>ISOy/CHyP (y=0,1)值</td><td>进入空闲状态的请求</td><td>退出空闲状态的请求</td></tr><tr><td>ISOy = 0CHyP = 0</td><td>复位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 1CHyP = 0</td><td>置位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 0CHyP = 1</td><td>置位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 1CHyP = 1</td><td>复位请求</td><td>置位请求和复位请求</td></tr></table>

延迟空闲模式可以应用于单个输出（CHyOPRE）或两个输出（CH0OPRE 和 CH1OPRE）情况（由 HRTIMER_STxCHOCTL 寄存器中的 DLYISCH[2:0]位域定义）：

 DLYISCH[2:0] = 3’b000：延迟空闲模式应用于CH0OPRE；

 DLYISCH[2:0] = 3’b001：延迟空闲模式应用于CH1OPRE；

 DLYISCH[2:0] = 3’b010：延迟空闲模式应用于CH0OPRE和CH1OPRE。

一旦选定的外部事件（EXEV5/ 6 或 EXEV7/ 8）到达，HRTIMER_STxINTF 寄存器中的 DLYIIF 位置 1，如果使能了相应的中断和 DMA（HRTIMER_STxDMAINTEN 寄存器中的 DLYIIE = 1 或DLYIDEN = 1），则产生中断或 DMA 请求。通过写 1 到 HRTIMER_STxINTFC 寄存器中的 DLYIIFC位可以清除中断标志。

当选定的外部事件（EXEV5 / 6 或 EXEV7/ 8）触发延迟空闲模式时，HRTIMER_STxINTF 寄存器中的 CHyDLYF（y = 0,1）位可以指示 CHyOPRE 信号的状态。

下面四张图显示了延迟空闲模式中的 CH0OPRE 波形：

 C0OPRE 运 行 在 常 规 模 式 ： HRTIMER_STxCHOCTL 寄 存 器 中 的 $\mathsf { D T E N } ~ = ~ 0$ HRTIMER_STxCTL0寄存器中的BLNMEN = 0；

 比较0事件产生置位请求；

 比较1事件产生复位请求。


图 25-34. 延迟空闲模式，ISO0 = 0 和 CHOP = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/d4b0c072e57d9e1d0f9aa6ef2ba0e2d118da0635c6ba1978d10699ad8f2fc2a0.jpg)



图 25-35. 延迟空闲模式，ISO0 = 1 和 CHOP = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/96d01ffed941352895976945f81b13768dee0506e8609173f416d00e39d80216.jpg)



图 25-36. 延迟空闲模式，ISO0 = 0 和 CHOP = 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/a651267b9cf46b760f77b3c201a94f7c5bcd17c047f9d17a041b6df3ada3911d.jpg)



图 25-37. 延迟空闲模式，ISO0 = 1 和 CHOP = 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/12f032761c41cf01d2d85e1520db4f26ccf2568460731a4a7af72b922c071176.jpg)


## 均衡空闲

均衡空闲模式仅在均衡模式下可用。通过将 HRTIMER_STxCHOCTL 寄存器的 DLYISCH[2:0]位域设为 3’bx011，使能均衡空闲模式。Slave_TIMER0/1/2 的外部事件 5/6（EXEV5/6）和Slave_TIMER3/4/5/6/7 的外部事件 7/8（EXEV7/8）可使用均衡空闲模式。

外部事件发生时，CHyOPRE（y = 0,1）进入空闲状态，并输出由 HRTIMER_STxCHOCTL 寄存器中的 ISOy 位定义的电平，且 HRTIMER_STxINTF 寄存器中的 DLYIIF 位置 1。该外部事件触发捕获，将计数器值捕获到比较 3 有效寄存器中（该值用户不可访问）。均衡模式会再维持一个周期，使互补输出 CHzOPRE（z = 0，1 且 z≠y）可以重复 CHyOPRE 上的短脉冲： 25-38.ISO0 = 0 ISO1 = 0 显示了均衡空闲模式下 Slave_TIMER0 的 CH0OPRE/ CH1OPRE波形，配置如下：

 C0OPRE 处 于 均 衡 模 式 ： HRTIMER_STxCHOCTL 寄 存 器 中 的 DTEN = 0 ，HRTIMER_STxCTL0寄存器中的BLNMEN = 1；

 比较0事件产生置位请求；

 比较1事件产生复位请求；

 在外部事件6发生时，通道0和通道1输出为均衡空闲模式：Slave_TIMER0的DLYISCH [2：0]= 3’b111。


图 25-38. 均衡空闲模式，ISO0 = 0 和 ISO1 = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/49040e71f56746a2918c63b02c08b2da030217b45016979a6e12eb85d96277a5.jpg)


HRTIMER_STxINTF 寄存器中的 BLNIF 位指示了发生均衡空闲模式时哪个通道正在输出信号。如图25-38. 均衡空闲模式， $I S O 0 = 0 \ Z I I S O 1 = 0$ ，外部事件 6（EXEV6）到来时，通道 0 输出信

号，通道 1 输出无效，且 BLNIF 位复位为零。

在计数器继续运行时，IDLE 模式将永久保持，直到重新使能输出才退出均衡空闲模式。将STxCH0EN 和 STxCH1EN 位同时重新置 1 后，通过置位请求或复位请求可以重新使能均衡空闲模式。

在以下情况下，均衡空闲模式可以与突发模式一起使用：

 BMSTx位必须复位（保持计数器时钟HRTIMER_PSCCK，且计数器正常运行）；

 当输出配置为突发模式控制的空闲状态时，不会触发均衡空闲模式。

## 均衡空闲自动恢复模式

C0OPRE 和 C1OPRE 在设置 BALIAR 时可以自动从均衡空闲中恢复，并且在 DLYISCH[2:0] =0x011或0x111时可以使用均衡空闲自动恢复模式，该位位于HRTIMER_STxCHOCTL寄存器中。当窄脉冲已加载到输出寄存器时，C0OPRE 和 C1OPRE 的脉冲将恢复为正常输出。

均衡空闲自动恢复模式只能在 HRTIMER_STxCAR 中的计数器自动重载值 CARL[15:0]大于 6 个t<sub>HRTIMER_CK</sub>周期时使用，例如当 CNTCKDIV[2:0] = 0 时为 0xC0，当 CNTCKDIV[2:0] = 1 时为 0x60。

## 突发模式控制的空闲模式

在突发模式中，空闲状态由突发模式控制器控制。具体请参考 。

均衡空闲和延迟空闲的优先级高于突发模式：一旦触发均衡空闲和延迟空闲模式，任何突发模式的退出请求都将被丢弃。相反，如果在均衡空闲或延迟空闲退出时，突发模式仍有效，则突发模式将正常恢复。

突发模式控制器可以对任意两个输出 CHyOPRE（y = 0,1）进行控制。见 25-13.，HRTIMER_STxCHOCTL 寄存器中的 ISOy 位和 BMCHyIEN（y = 0,1）位可以对突发模式控制的空闲模式期间的每个输出的状态进行配置。


表 25-13. 突发模式控制的空闲状态时的输出


<table><tr><td>ISOy</td><td>BMCHyIEN</td><td>CHyOPRE (y=0,1)</td></tr><tr><td>x</td><td>0</td><td>无影响:输出不受突发模式控制器影响</td></tr><tr><td>0</td><td>1</td><td>在突发模式控制的空闲模式中输出复位电平</td></tr><tr><td>1</td><td>1</td><td>在突发模式控制的空闲模式中输出置位电平</td></tr></table>

## 通道输出级

每个 Slave_TIMERx 可以控制一对输出（STxCH0_O 和 ${ \mathsf { S T x C H 1 } } _ { - } \subset \supset$ ）。输出级有三种工作状态：

 运行状态： ${ \mathsf { S T x C H y \_ O } } \ ( \ y = 0 , 1 )$ 输出 $\mathsf { C H y O P R E } \ ( \mathsf { y } = 0 , 1 )$ ）的电平。

 空闲状态： ${ \mathsf { S T x C H y \_ O } } \ ( \mathsf { y } = 0 , 1 )$ 输出由HRTIMER_STxCHOCTL寄存器中ISOy位定义的电平。

故障状态： ${ \mathsf { S T x C H y \_ O } } \ ( { \mathsf { y } } = 0 , 1 )$ 可以永久有效，无效或Hi-Z（由HRTIMER_STxCHOCTL寄

存器的CHyFLTOS位定义）。详见 。

HRTIMER_CHOUTEN 寄存器中的 STxCHyEN 位和 HRTIMER_CHOUTDISF 寄存器中的STxCHyDISF 位可以指示输出的状态，如 25-14. x=0..7, y=0,1 所述。


表 25-14. 输出级状态编程（x=0..7, y=0,1）


<table><tr><td>STxCHyEN</td><td>STxCHyDISF</td><td>输出级状态</td></tr><tr><td>1</td><td>x</td><td>运行状态</td></tr><tr><td>0</td><td>0</td><td>空闲状态</td></tr><tr><td>0</td><td>1</td><td>故障状态</td></tr></table>

将 HRTIMER_CHOUTDIS 寄存器中的 STxCHyDIS 位置 1，输出禁能，并使输出进入空闲状态。三种工作状态的优先级顺序为：空闲状态 > 故障状态 > 运行状态。

HRTIMER_STxCHOCTL 寄存器中的 CHyP 位可以设置输出极性。当 CHyP = 0 时，输出极性为高电平有效。当 CHyP = 1 时，输出极性为低电平有效。详见 25-39. CHyP=0 CHyP=1STxCHy_O 。


图 25-39. CHyP=0 或 CHyP=1 时的 STxCHy_O 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/b79735e9381bdc0b34500c18c291e0d5ee61f2a72299beff770d5616248d5649.jpg)


使用 HRTIMER_STxCHOCTL 寄存器中的 CHyFLTOS [1:0]位域可以配置故障状态下的输出电平，如下所示：

 2’b00：输出永远不会进入故障状态，并保持运行或空闲状态；

 2’b01：故障状态时，输出有效电平；

 2’b10：故障状态时，输出无效电平；

 2’b11：故障状态时，输出为三态。

使用 HRTIMER_STxCHOCTL 寄存器中的 ISOy位配置处于空闲状态的输出电平，如下：

 2’b0：空闲状态时，输出无效电平；

 2’b1：空闲状态时，输出有效电平。

## 载波信号模式

可以在 ${ \mathsf { O y P R E } } ( { \mathsf { y } } { = } 0 , 1 )$ 信号顶部添加一个高频载波信号，如 25-40. 所示。


图 25-40. 载波信号结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/3572dabce6d7b7072db8cb92376305cc1eee1bdd32a8e41a4288c449468a1b2d.jpg)


载波信号模式中，可以在载波信号开始之前定义一个特定的脉冲宽度。载波信号的频率和占空比是可配置的。详见 25-41. HRTIMER 。

将 HRTIMER_STxCHOCTL 寄存器中的 CH0CSEN 和 CH1CSEN 位置 1，可以分别在通道 0 和 1上使能载波信号模式。

第一个脉冲的脉冲宽度由 HRTIMER_STxCSCTL 寄存器中的 CSFSTPW [3:0]位域配置，公式如下：

$$
t _ {C S F S T P W} = (C S F S T P W [ 3: 0 ] + 1) ^ {*} t _ {H R T I M E R \_ C S G C K}, \text {其中} t _ {H R T I M E R \_ C S G C K} = 1 6 * t _ {H R T I M E R \_ C K}
$$

载波信号的频率由 HRTIMER_STxCSCTL 寄存器中的 CSPRD [3:0]位域配置，公式如下：

$$
t _ {\text { CSPRD }} = (\text { CSPRD } [ 3: 0 ] + 1) ^ {*} t _ {\text { HRTIMER\_CSGCK }}, \text { 其中 } t _ {\text { HRTIMER\_CSGCK }} = 1 6 ^ {*} t _ {\text { HRTIMER\_CK }}
$$

载波信号的占空比由 HRTIMER_STxCSCTL 寄存器中的 CSDTY[2:0]位域配置，步长为 12.5％。载波信号模式中，载波信号发生器的输出与 ${ \tt O y P R E }$ 逻辑与运算后输出。 $\mathsf { O y P R E } \ ( \mathsf { y } = 0 , 1 )$ 输出无效时，载波信号会立即停止，即使当前的载波周期未完成。具体请参考 25-41.HRTIMER 。


图 25-41. 载波模式使能时的 HRTIMER 输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/880c00a1e80079c974fbeff809effc95090fdd1ed584a1f9692a42bf2feb1df1.jpg)


## 同步输入启动/复位计数器

当 HRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以产生计数器复位事件；当HRTIMER_MTCTL0 寄存器中的 SYNISTRT 位置 1 时，同步输入可以启动计数器。详见。

同步输入请求会将 HRTIMER_MTINTF 寄存器中的 SYNIIF 位置 1，如果使能了中断或 DMA请求（HRTIMER_MTDMAINTEN 寄存器中的 SYNIIE = 1 或 SYNIDEN = 1），会产生相应的中断或DMA 请求。可以通过写 1 到 HRTIMER_MTINTFC 寄存器中的 SYNIIFC 位，来清除同步输入中断标志。

## 更新事件和影子寄存器

Slave_TIMER 中的某些寄存器具有影子寄存器。MCU 复位后，影子寄存器被禁能。如果将HRTIMER_STxCTL0 寄存器中的 SHWEN 位清 0，则禁能影子寄存器。写入这些寄存器的值将立即转移到有效寄存器中并生效。

如果 HRTIMER_STxCTL0 寄存器中的 SHWEN 位置 1，则使能影子寄存器， 25-15.Slave_TIMERx 中列出的寄存器被预加载。写入这些寄存器的值将被传送到影子寄存器，且不会立即生效。当发生更新事件时，影子寄存器内容将转移到有效寄存器中并立即生效。

注意：当 SHWEN=1 时，才会产生更新事件。

25-15. Slave_TIMERx 列出了具有影子寄存器的寄存器和相应的更新事件。


表 25-15. Slave_TIMERx 影子寄存器和通用寄存器和更新事件


<table><tr><td>具有影子寄存器的寄存器</td><td>影子寄存器使能位</td><td>更新事件</td></tr><tr><td>HRTIMER_STxDMAINTEN</td><td rowspan="16">HRTIMER_STxCTL0寄存器中的SHWEN位</td><td rowspan="16">软件(STxSUP位)重复事件(UPREP=1)计数器复位或翻转事件(UPRST=1)来自其他定时器的更新事件(Slave_TIMERx是UPBSTX,Master_TIMER是UPBMT)DMA模式结束事件(UPSEL[3:0]=4&#x27;b0001)DMA模式结束事件之后的更新事件(UPSEL[3:0]=4&#x27;b0010)STxUPINy(y=0..2)的上升沿产生更新事件STxUPINy(y=0..2)的上升沿之后产生更新事件</td></tr><tr><td>HRTIMER_STxCAR</td></tr><tr><td>HRTIMER_STxCREP</td></tr><tr><td>HRTIMER_STxCMP0V</td></tr><tr><td>HRTIMER_STxCMP0CP</td></tr><tr><td>HRTIMER_STxCMP1V</td></tr><tr><td>HRTIMER_STxCMP2V</td></tr><tr><td>HRTIMER_STxCMP3V</td></tr><tr><td>HRTIMER_STxDTCTL</td></tr><tr><td>HRTIMER_STxCH0SET</td></tr><tr><td>HRTIMER_STxCH0RST</td></tr><tr><td>HRTIMER_STxCH1SET</td></tr><tr><td>HRTIMER_STxCH1RST</td></tr><tr><td>HRTIMER_STxCNTRST</td></tr><tr><td>HRTIMER_STxCNTRSTA</td></tr><tr><td>HRTIMER_STxACTL寄存器中的DTFCFG[15:9]和DTRCFG[15:9]</td></tr><tr><td>HETIMER_ADCTRIGS0HETIMER_ADCTRIGS0AHETIMER_ADCTRIGS1HETIMER_ADCTRIGS1AHETIMER_ADCTRIGS2HETIMER_ADCTRIGS2AHETIMER_ADCTRIGS3HETIMER_ADCTRIGS3A</td><td colspan="2">Master_TIMER或Slave_TIMERx(x=0..7)的更新事件,由HRTIMER_MTCTL0或HRTIMER_STxCTL0中的SHWEN位域</td></tr></table>

更新使能输入 STxUPINy（y = 0..2）是来自通用定时器的芯片内部信号，上升沿有效。具体请见25-16. STxUPINy y=0..2 。


表 25-16. STxUPINy（y=0..2）和芯片内部信号


<table><tr><td>更新使能输入 STxUPINy (y = 0..2)</td><td>芯片内部信号</td></tr><tr><td>STxUPIN0</td><td>TIMER15_CH0_O</td></tr><tr><td>STxUPIN1</td><td>TIMER16_CH0_O</td></tr><tr><td>STxUPIN2</td><td>TIMER5_TRGO</td></tr></table>

## 外部事件滤波

外部事件 EXEVyC（y = 0..9）在指定时间内被滤波，有两种滤波模式：

 消隐模式：在指定时间内发生的外部事件被忽略；

 窗口模式：在指定时间内发生的外部事件有效。

具体请见 25-42. 。


图 25-42. 消隐模式和窗口模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/1e9f84c6270244ae26669579ed2c2d520a83352b1e824eb7e020e1a8efe87f45.jpg)



参考 章节可得更多关于外部事件 EXEVyC(y=0..9)的信息。


## 消隐模式

消隐模式中，在指定时间内发生的外部事件 EXEVyC（y = 0..9）被忽略，其他时间发生的外部事件有效。在指定的时间内，消隐信号为低电平。该模式由 EXEVyFM [4:0]位域配置，范围从 4’b0001到 4’b1100。

消隐信号源有两种类型：

Slave_TIMERx本身：指定的时间是指从计数器复位到比较事件发生持续的时间。（EXEVyFM$[ 4 ; 0 ] = 5 5 6 0 0 0 0 1 { \sim } 5 5 6 0 0 1 0 0$ ，用于设置比较0~比较3事件）；

来自其他Slave_TIMER单元 $( \mathsf { E X E V y F M } \left[ 5 ; 0 \right] = 5 \mathsf { b 0 0 } 1 0 1 \sim 5 \mathsf { b 0 } 1 1 0 0 )$ 的STBLKSRCz（z =0..9）：指定的时间是指从选定的Slave_TIMER计数器复位到比较事件发生持续的时间。也可以是选定Slave_TIMER中的CH1OPRE信号（在这种情况下，只要CH1OPRE为低电平，事件将被忽略）具体请见 25-17. 。


表 25-17. 消隐模式下的滤波信号映射


<table><tr><td colspan="2"></td><td>到ST0</td><td>到ST1</td><td>到ST2</td><td>到ST3</td><td>到ST4</td><td>到ST5</td><td>到ST6</td><td>到ST7</td></tr><tr><td rowspan="4">来自ST0</td><td>CMP0</td><td>×</td><td>STBLK SRC0</td><td>×</td><td>STBLK SRC0</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC0</td></tr><tr><td>CMP1</td><td>×</td><td>×</td><td>STBLK SRC0</td><td>×</td><td>STBLK SRC0</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CMP3</td><td>×</td><td>STBLK SRC1</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC0</td><td>×</td><td>×</td></tr><tr><td>CH1OPRE</td><td>×</td><td>STBLK SRC2</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC0</td><td>×</td></tr><tr><td rowspan="4">来自ST1</td><td>CMP0</td><td>STBLK SRC0</td><td>×</td><td>STBLK SRC1</td><td>×</td><td>STBLK SRC1</td><td>×</td><td>STBLK SRC1</td><td>×</td></tr><tr><td>CMP1</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC1</td><td>×</td><td>STBLK SRC1</td><td>×</td><td>STBLK SRC1</td></tr><tr><td>CMP3</td><td>STBLK SRC1</td><td>×</td><td>STBLK SRC2</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CH1OPRE</td><td>STBLK SRC2</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td rowspan="4">来自ST2</td><td>CMP0</td><td>STBLK SRC3</td><td>STBLK SRC3</td><td>×</td><td>STBLK SRC2</td><td>STBLK SRC2</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CMP1</td><td>×</td><td>STBLK SRC4</td><td>×</td><td>STBLK SRC3</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CMP3</td><td>STBLK SRC4</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC2</td><td>×</td><td>STBLK SRC2</td></tr><tr><td>CH1OPRE</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC4</td><td>×</td><td>×</td><td>STBLK SRC2</td><td>×</td></tr><tr><td rowspan="4">来自ST3</td><td>CMP0</td><td>STBLK SRC6</td><td>×</td><td>STBLK SRC4</td><td>×</td><td>STBLK SRC5</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CMP1</td><td>×</td><td>STBLK SRC6</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC3</td><td>STBLK SRC3</td><td>×</td></tr><tr><td>CMP3</td><td>×</td><td>×</td><td>STBLK SRC5</td><td>×</td><td>STBLK SRC6</td><td>STBLK SRC4</td><td>×</td><td>STBLK SRC3</td></tr><tr><td>CH1OPRE</td><td>×</td><td>×</td><td>STBLK SRC6</td><td>×</td><td>STBLK SRC7</td><td>×</td><td>×</td><td>×</td></tr><tr><td rowspan="3">来自ST4</td><td>CMP0</td><td>×</td><td>STBLK SRC7</td><td>×</td><td>STBLK SRC5</td><td>×</td><td>STBLK SRC5</td><td>×</td><td>×</td></tr><tr><td>CMP1</td><td>STBLK SRC7</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC4</td></tr><tr><td>CMP3</td><td>×</td><td>×</td><td>STBLKSRC7</td><td>STBLKSRC6</td><td>×</td><td>STBLKSRC6</td><td>STBLKSRC4</td><td>×</td></tr><tr><td></td><td>CH1OPRE</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC7</td><td>×</td><td>×</td></tr><tr><td rowspan="4">来自 ST5</td><td>CMP0</td><td>STBLK SRC5</td><td>×</td><td>STBLK SRC3</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC5</td><td>STBLK SRC5</td></tr><tr><td>CMP1</td><td>×</td><td>STBLK SRC5</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CMP3</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC7</td><td>STBLK SRC3</td><td>×</td><td>STBLK SRC6</td><td>STBLK SRC6</td></tr><tr><td>CH1OPRE</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC4</td><td>×</td><td>STBLK SRC7</td><td>×</td></tr><tr><td rowspan="4">来自 ST6</td><td>CMP0</td><td>×</td><td>STBLK SRC8</td><td>×</td><td>STBLK SRC8</td><td>×</td><td>STBLK SRC8</td><td>×</td><td>STBLK SRC7</td></tr><tr><td>CMP1</td><td>STBLK SRC8</td><td>×</td><td>STBLK SRC8</td><td>×</td><td>STBLK SRC8</td><td>×</td><td>×</td><td>STBLK SRC8</td></tr><tr><td>CMP3</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CH1OPRE</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>STBLK SRC9</td></tr><tr><td rowspan="4">来自 ST7</td><td>CMP0</td><td>STBLK SRC9</td><td>×</td><td>STBLK SRC9</td><td>×</td><td>STBLK SRC9</td><td>×</td><td>STBLK SRC8</td><td>×</td></tr><tr><td>CMP1</td><td>×</td><td>STBLK SRC9</td><td>×</td><td>STBLK SRC9</td><td>×</td><td>STBLK SRC9</td><td>STBLK SRC9</td><td>×</td></tr><tr><td>CMP3</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>CH1OPRE</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr></table>


当 EXEVyMEEN 位置 1 时，将使能外部事件的存储功能，外部事件不会立即生效。一旦指定的时间完成，该外部事件将被存储并生成。


## 窗口模式

窗口模式中，在指定时间内发生的外部事件 EXEVyC（y = 0..9）有效，其他时间发生的则被忽略。在指定的时间内，窗口信号为高电平。此模式由 EXEVyFM[4:0]位域配置，范围从 5’b01101 到5’b01111。

如果在指定时间内未发生外部事件 EXEVyC(y=0..9)，则在指定时间结束时将产生超时事件。

窗口信号源有两种类型：

 Slave_TIMERx本身：指定的时间是指从计数器复位到比较事件发生持续的时间。（EXEVyFM[4:0] = 5’b01101和5’b01110，用于分别设置比较1和比较2事件）；

 来自其他Slave_TIMER单元 $( \mathsf { E X E V y F M } [ 4 ; 0 ] = 5 \mathsf { b 0 0 } 1 0 1 \sim 5 \mathsf { b 0 } 1 1 0 0 )$ 的STWDSRC：指定的时间是指从选定的Slave_TIMER计数器复位到比较事件发生持续的时间。具体请见 25-18.窗口模式的滤波信号映射


表 25-18. 窗口模式的滤波信号映射


<table><tr><td>到来自</td><td>T0 ST0</td><td>T0 ST1</td><td>T0 ST2</td><td>T0 ST3</td><td>T0 ST4</td><td>T0 ST5</td><td>T0 ST6</td><td>T0 ST7</td></tr><tr><td>STWDSRC</td><td>Slave_TIMER1 比较 1 事件</td><td>Slave_TIMER0 比较 1 事件</td><td>Slave_TIMER3 比较 1 事件</td><td>Slave_TIMER2 比较 1 事件</td><td>Slave_TIMER5 比较 1 事件</td><td>Slave_TIMER4 比较 1 事件</td><td>Slave_TIMER7 比较 1 事件</td><td>Slave_TIMER6 比较 1 事件</td></tr></table>


当 EXEVyMEEN 位置 1 时，将使能外部事件的存储功能，外部事件不会立即生效。一旦指定的时间完成，该外部事件将被存储并生成。


## 外部事件计数

10 个外部事件可以由外部事件 X 计数模块进行过滤。如 25-43. X 所示。


图 25-43. 外部事件 X 计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/3ca89df9a32e895e9cbac455e69bb059d749b4254f383b9f481c373b2cf29c8b.jpg)



外部事件 X 计数器通过在 HRTIMER_STxEXEVFCFG2 寄存器中使能 EXEVXCEN 位启用。仅当EXEVXCNT[5:0]的值大于或等于 EXEVXCNTTHR[5:0] + 1 时，外部事件才被视为有效。


当 EXEVXRSTM 位复位时，发生复位和更新事件时，EXEVXCNT[5:0]位被复位,外部事件仅在其在一个 PWM 周期内发生多次时被视为有效。当 EXEVXRSTM 位置位时，在每个 PWM 周期内生成外部事件时，EXEVXCNT[5:0]位会累积，并且在上一个 PWM 周期内没有外部事件出现时，EXEVXCNT[5:0]位将被复位。

在写入 EXEVXCNTTHR[5:0]位之后应置位 EXEVXCEN 位，且在启用外部事件 X 计数器时可以更改 EXEVXCNTTHR[5:0]位。新值 EXEVXCNTTHR[5:0]将在下一个周期生效。在启用外部事件 X计数器时不能更改 EXEVXSEL[3:0]。


图 25-44. 当 EXEVXCEN 为 1 和 EXEVXCNTTHR[5:0]为 2 时外部事件 X 计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/544baa78114887b88de8dd9b3f02edcd04725f29f174c880695bc12500106af5.jpg)


## 快速外部事件模式

可以根据实际需求动态调整外部事件的处理时间。当在 HRTIMER_EXEVCFG0 寄存器中将EXEVxFAST 位复位时，需要在生效之前重新采样外部事件，从而增加一些延迟，并且可以生成高分辨率的脉冲。当在 HRTIMER_EXEVCFG0 寄存器中设置 EXEVxFAST 位时，启用了快速外部事件模式。在此模式下，将延迟最小化。

快速外部事件模式仅对电平事件有效，不适用于边沿事件，因此 HRTIMER_EXEVCFG0 寄存器中的 EXEVxEG[1:0] 位必须为 0x00。在此模式下，可以使用外部事件过滤，并且必须禁用外部事件锁存。

同一事件不能同时配置在 HRTIMER_STxCHySET 和 HRTIMER_STxCHyRST 寄存器中，当复位事件和置位事件同时发生时，复位事件具有更高的优先级。

在快速外部事件模式下，当外部事件发生并生效时，其他在 11 个 t<sub>HRTIMER_CK</sub> 内发生的外部事件无效。

## 25.4.3. DLL 校准

DLL 可以产生并校准高分辨率时钟 HRTIMER_HPCK（f<sub>HRTIMER_HPCK</sub> = 32 * f<sub>HRTIMER_CK</sub>）。DLL 模块可以一次或定期校准高分辨率时钟 HRTIMER_HPCK。

当 HRTIMER_DLLCCTL 寄存器中的 CLBPEREN 位置 1 时，使能定期的 DLL 校准，CLBPER [1:0]位域配置校准周期。DLL 将在整个 HRTIMER 运行期间定期校准时钟。

当 HRTIMER_DLLCCTL 寄存器中的 CLBPEREN 位清 0 时，将 CLBSTRT 置 1，DLL 只校准一

次高分辨率时钟 HRTIMER_HPCK。

注意：仅当系统时钟频率在 150MHz到 216MHz 时，DLL 校准有效。

## 25.4.4. 突发模式

突发模式控制器允许通过硬件使 CHyOPRE（y = 0,1）交替输出空闲和运行状态。该模式由HRTIMER_BMCTL 寄存器中的 BMEN 位使能，通常在轻载情况中使用。

突发模式控制器包括：

 1个计数器（BM-counter）；

 1个比较寄存器：HRTIMER_BMCMPV，用于定义空闲状态的持续时间；

 1个周期寄存器：HRTIMER_BMCAR，用于定义空闲和运行状态持续时间的总和。

## BM-counter 的计数模式

BM-counter 可以运行在连续模式或单脉冲模式下。

当 BMCTN = 1 时，BM-counter 运行在连续模式下。BM-counter 从 0 连续计数到计数器重载值（HRTIMER_BMCAR）。当计数到计数器重载值时，计数器将从 0 重新启动。突发模式过程一直持续到 HRTIMER_BMCTL 中的 BMOPTF 位被复位。

当 BMCTN = 0 时，BM-counter 运行在单脉冲模式下。BM-counter 从 0 连续计数到计数器重载值（HRTIMER_BMCAR）。当计数到计数器重载值时，BM-counter 停止计数。

当计数到计数器重载值（HRTIMER_BMCAR）时，HRTIMER_INTF 寄存器中的 BMPERIF 位置1，如果 BMPERIE = 1（在 HRTIMER_INTEN 寄存器中），则突发模式控制器产生突发模式周期中断请求。可以写 1 到 HRTIMER_INTC 中的 BMPERIFC 位来清除 BMPERIF 位。

## 突发模式的时序

BM-counter 由几个时钟源提供时钟，可以通过 HRTIMER_BMCTL 寄存器中的 BMCLKS[3:0]位选择。当选定的时钟源信号的上升沿到达时，BM-counter 计数值加 1。

当 BMCLKS[3:0] = 4’b1010 时，BM-counter 的时钟源是 f<sub>HRTIMER_CK</sub> 分频后得到的，分频系数由HRTIMER_BMCTL 寄存器中的 BMPSC [3:0]位域定义。

当 BMCLKS[3:0] = 4’b0110~4’b1001 时，BM-counter 的时钟源是芯片内部信号：BMCLKy（y =0..3），具体请见 25-19. 。


表 25-19. 突发模式的芯片内部信号


<table><tr><td>BMCLKy(y=0..3)</td><td>芯片内部信号</td></tr><tr><td>BMCLK0</td><td>TIMER15_CH0_O</td></tr><tr><td>BMCLK1</td><td>TIMER16_CH0_O</td></tr><tr><td>BMCLK2</td><td>TIMER6_TRGO</td></tr><tr><td>BMCLK3</td><td>保留</td></tr></table>

空闲状态的持续时间由 HRTIMER_BMCMPV 寄存器定义，并且 HRTIMER_BMCAR 寄存器定义了突发模式的周期，该周期值是空闲状态和运行状态持续时间之和，具体请见 25-45.时序图


图 25-45. 突发模式时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/7b284ccc272c04a6721fb5f4bbd8d2fe609a67afd0b614ff01d3df4ecc347aff.jpg)


当 BMSE 置位时，HRTIMER_BMCMPV 和 HRTIMER_BMCAR 寄存器是预装载，在下列情形下会从预装载传输到有效寄存器：

 当使能突发模式时（BMEN=1）；

 当突发模式周期结束时。

注意：当写 HRTIMER_BMCAR 后会暂时禁能更新，直到写 HRTIMER_BMCMPV 寄存器后才恢复更新。

## 突发模式进入

HRTIMER_BMSTRG 寄存器和 HRTIMER_BMSTRGA 寄存器中定义了 44 个可触发突发模式的事件。这些触发事件可以同时选择，然后再进行逻辑或运算。而在 BM-counter 的计数过程中，这些触发事件被忽略。这些触发事件分为七种：

1. Master_TIMER 事件：重复事件，复位/翻转事件，比较 0/1/2/3 事件；

2. Slave_TIMERx 事件：重复事件，复位/翻转事件，比较 0 和比较 1 事件；

3.外部事件：EXEV6 和 EXEV7；

4. EXEV6 事件之后的 Slave_TIMER0 周期事件；

5. EXEV7 事件之后的 Slave_TIMER3 周期事件；

6.芯片内部信号：TIMER6_TRGO；

7.软件：写 1 到 HRTIMER_BMSTRG 寄存器的 SWTRG 位。

触发事件发生时，有两种进入突发模式的方式：常规进入和延迟进入。

常规进入

当 HRTIMER_STxCHOCTL 寄存器中的 BMCHyDTI（y = 0，1）位为 0 时，突发模式是常规进入模式。选定事件发生后的第一个 BM-counter 计数时钟到来时，输出将进入突发模式，并输出空闲电平（根据 ISO0 位和 ISO1 位设置）。

25-46. 显示了在以下配置时，Slave_TIMER0 中的 CHyOPRE 波形：

 CyOPRE 处 于 常 规 模 式 ： HRTIMER_ST0CHOCTL 寄 存 器 中 的 DTEN = 0 ，HRTIMER_ST0CTL0寄存器中的BLNMEN = 0；

 周期事件产生置位请求；

 比较1事件产生复位请求；

 BM-counter的时钟源是Slave_TIMER0的翻转事件：BMCLKS [3:0] = 4’b0001。


图 25-46. 突发模式的常规进入


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/b5ffb335e2f0c33d46465f7837ba8b1cec68df7414ee2908987d2601d2420019.jpg)


## 延迟进入

当 HRTIMER_STxCHOCTL 寄存器中的 BMCHyDTI（y = 0,1）位为 1 时，突发模式的进入被延迟。在进入突发模式之前，CHyOPRE 被强制插入死区时间。

每个 CHyOPRE 都有自己的死区插入值：

 BMCH0DTI = 1时，DTRCFG[15:0]用于配置CH0OPRE的死区时间；

 BMCH1DTI = 1时，DTFCFG[15:0]用于配置CH1OPRE的死区时间。

延迟进入模式适用于以下情况：CHyOPRE(y=0,1)之一具有有效的空闲电平（ISOy = 1），且死区时间为正（DTRS /DTFS 设置为 0）。

在常规死区时间内，突发模式被触发，当前死区过程中止，将重新开始新的死区插入过程。详见25-47. 。


图 25-47. 突发模式的延迟进入


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/425631545ff18fbdce7db84bdadff188c17376ece697dc731e2ec6ec0d1dfb31.jpg)


## 突发模式退出

在连续模式下，突发模式由软件强制退出。BMOPTF 或 BMEN 位重写为 0 后，发生输出置位/复位请求时，会退出突发模式。详情请见 25-46. 和 25-47.迟进入。

在单脉冲模式下，一旦经过空闲周期，就退出突发模式。

## 突发模式的时钟

可以在突发模式工作（运行，空闲）期间停止并复位 Master_TIMER 和 Slave_TIMERx（x = 0..7）

单元的计数器，可通过 HRTIMER_BMCTL 寄存器中的 BMMT 位和 BMSTx（x = 0..7）位进行配置：

 BMMT或BMSTx（x = 0..7）= 0：保持Master_TIMER或Slave_TIMERx（x = 0..7）的计数器时钟（HRTIMER_PSCCK），且计数器正常运行；

 BMMT或BMSTx（x = 0..7）= 1：Master_TIMER或Slave_TIMERx（x = 0..7）计数器时钟（HRTIMER_PSCCK）停止，并复位计数器。

## 使用 HRTIMER_STxCMP0CP 寄存器模拟突发模式

可以使用 HRTIMER_STxCMP0CP 寄存器来生成类似于突发模式控制的波形，配置如下：

 比较0事件用于产生复位请求；

 周期事件用于产生置位请求；

 使用DMA（重复事件）连续将两个32位数据写入HRTIMER_STxCMP0CP寄存器，如下所示：

HRTIMER_STxCMP0CP = {CREP [7:0] =运行周期数-1；CMP0VAL [15:0] =占空比}

HRTIMER_STxCMP0CP = {CREP [7:0] =空闲周期数-1；CMP0VAL [15:0] = 0}

例如，要生成每 5 个周期中有 2 个周期输出置位的 PWM 波，可进行如下配置：

 运行：HRTIMER_STxCMP0CP = {0x0001; 0x0020}；

 空闲：HRTIMER_ $\mathsf { S T x C M P 0 C P } = \{ 0 { \times } 0 0 0 2 ; 0 { \times } 0 0 0 0 \}$ 


图 25-48. 模拟突发模式示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/f9e09d489b22159ba7c1974835c7992e7f1bf197c66cbe42d48caf16a4053e02.jpg)


## 25.4.5. 同步输入/输出

同步电路在 Master_TIMER 内部：

 同步输出：HRTIMER可以作为主机产生同步信号；

 同步输入：HRTIMER也可以作为从机等待触发同步。

## 同步输出

可以将 HRTIMER 配置为主机，同步外部资源；

可以配置 HRTIMER_MTCTL0 寄存器中的 SYNOSRC[1:0]位域，选择发送到同步输出上的源。有以下四个源：

 2’b00：Master_TIMER启动事件。在以下三种情况下可以将生成的启动事件用作同步输出，当MTCEN位置1时，当计数器在单脉冲模式下达到周期值后重新启动时，还有当CTNM或CNTRSTM位置1时，在计数期间发生的复位事件；

 2’b01：Master_TIMER比较0事件；

2’b10：Slave_TIMER0复位和启动事件。它与Master_TIMER启动事件类似，除以下情况外：连续模式下的计数器翻转，在CNTRSTM = 0时的单脉冲模式下放弃的复位请求；

 2’b11：Slave_TIMER0比较0事件。

HRTIMER_MTCTL0 寄存器中的 SYNOPLS[1:0]位域确定同步输出信号的极性：

 2’b00：脉冲产生禁能。同步输出引脚HRTIMER_SCOUT上没有脉冲；

 2’b01：保留；

 2’b10：在同步输出引脚HRTIMER_SCOUT上生成正脉冲。正脉冲的长度为16 t<sub>HRTIMER_CK</sub>个周期；

 2’b11：在同步输出引脚HRTIMER_SCOUT上生成负脉冲。负脉冲的长度为16 t<sub>HRTIMER_CK</sub>个周期。

## 同步输入

HRTIMER 可以作为从机等待触发同步。可以通过 HRTIMER_MTCTL0 寄存器中的 SYNISRC [1:0]位域选择同步输入源。有四个输入触发源可选：

 2’b00：同步输入禁能；

 2’b01：保留；

 2’b10：芯片内部信号。高级定时器TIMER0的TIMER0_TRGO信号；

 2’b11：芯片外部引脚。芯片外部引脚（HRTIMER_SCIN）上的正脉冲（上升沿有效）。

Master_TIMER 由 HRTIMER_MTCTL0 寄存器中的 SYNISTRT 位和 SYNIRST 位配置。Slave_TIMERx 由 HRTIMER_STxCTL0 寄存器中的 SYNISTRT 位和 SYNIRST 位配置。

当 SYNISTRT 置 1 时，必须先使能定时器（将 STxCEN 位或 MTCEN 位置 1），则同步输入信号将启动计数器。在连续模式下，即使 STxCEN 位或 MTCEN 位被置 1，计数器也不会启动，只有在同步输入信号到达后才会启动。

当 SYNIRST 置 1 时，同步输入信号将复位计数器，并像其他任何重置事件一样递减重复计数器。

## 25.4.6. 外部事件

10 个外部事件可以同时用于 8 个 Slave_TIMER 中的任意 1 个。通过 HRTIMER_EXEVCFG0 寄存器配置外部事件 $\texttt { y ( y = 0 . 4 ) }$ ），通过 HRTIMER_EXEVCFG1 和 HRTIMER_EXEVDFCTL 寄存器配置外部事件 $y ( y = 5 . . 9 )$ ）。

处理外部事件 $\texttt { y ( y = 0 . 4 ) }$ 的过程如 25-49. y $( y = 0 . 4 )$ 处理过程框图所示。


图 25-49. 外部事件 y（y=0..4）处理过程框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/08b0320376b552fd0a43e60e44165091ff35d3cce7facceda111909a997cd0d0.jpg)


外部事件 $\texttt { y ( y = 0 . 4 ) }$ 的配置如下：

 4个源：通过EXEVySRC[1:0]位域进行配置；

 有效沿选择：通过EXEVyEG[1:0]位域进行配置。可以是电平有效的或边沿有效（上升沿，下降沿或两者兼有）；

 极性选择：在电平有效（EXEVyEG [1:0] = 2’b00）时，由 $| \mathsf { E X E V y P }$ 位进行配置。

 当EXEVyFAST位置1时，外部事件工作在异步模式。

处理外部事件 $y \ ( y = 5 . . 9 )$ 的过程如 25-50. y $( y = 5 , 9 )$ 处理过程框图所示。


图 25-50. 外部事件 y（y=5..9）处理过程框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/ba08644c030bcb05553affb10324d831908cd1e57a7b3f5da55587a69fadbeb4.jpg)


外部事件 $y ( y = 5 . . 9 )$ 的配置如下：

 4个源：通过EXEVySRC[1:0]位域进行配置；

 有效沿选择：通过EXEVyEG[1:0]位域进行配置。可以是电平有效的或边沿有效（上升沿，下降沿或两者兼有）；

 极性选择：在电平有效 $\left( \mathsf { E X E V y E G } \left[ 1 : 0 \right] = 2 : \mathsf { b 0 0 } \right)$ 时，由 $\mathsf { E X E V O P }$ 位进行配置；

 数字滤波配置：配置HRTIMER_EXEVDFCTL寄存器中的 $\mathsf E \mathsf { X } \mathsf E \mathsf { V } \mathsf { y } \mathsf { F } \mathsf C [ 3 { : } 0 ]$ 位域。

数字滤波器的采样时钟 f<sub>HRTIMER_EXEVFCK</sub>由 HRTIMER_EXEVDFCTL 寄存器中的 EXEVFDIV[2:0]位

域定义。

这些外部事件源 EXEVySRCz（y = 0..9，z = 0..4）可以来自比较器、数字输入引脚、ADC 的模拟看门狗和 TIMER_TRGO。具体请参考 25-20. 。


表 25-20. 外部事件映射


<table><tr><td>外部事件</td><td>EXEVySRC0</td><td>EXEVySRC1</td><td>EXEVySRC2</td><td>EXEVySRC3</td></tr><tr><td>外部事件 0</td><td>PC12</td><td>比较器 1</td><td>TIMER0_TRGO</td><td>ADC0_WD0_OUT</td></tr><tr><td>外部事件 1</td><td>PC11</td><td>比较器 3</td><td>TIMER1_TRGO</td><td>ADC0_WD1_OUT</td></tr><tr><td>外部事件 2</td><td>PB7</td><td>比较器 5</td><td>TIMER2_TRGO</td><td>ADC0_WD2_OUT</td></tr><tr><td>外部事件 3</td><td>PB6</td><td>比较器 0</td><td>比较器 4</td><td>ADC1_WD0_OUT</td></tr><tr><td>外部事件 4</td><td>PB9</td><td>比较器 2</td><td>比较器 6</td><td>ADC1_WD1_OUT</td></tr><tr><td>外部事件 5</td><td>PB5</td><td>比较器 1</td><td>比较器 0</td><td>ADC1_WD2_OUT</td></tr><tr><td>外部事件 6</td><td>PB4</td><td>比较器 3</td><td>TIMER6_TRGO</td><td>ADC2_WD0_OUT</td></tr><tr><td>外部事件 7</td><td>PB8</td><td>比较器 5</td><td>比较器 2</td><td>ADC3_WD0_OUT</td></tr><tr><td>外部事件 8</td><td>PB3</td><td>比较器 4</td><td>TIMER14_TRGO</td><td>比较器 3</td></tr><tr><td>外部事件 9</td><td>PC5/PC6</td><td>比较器 6</td><td>TIMER5_TRGO</td><td>ADC3_WD0_OUT</td></tr></table>


注意：“×”表示不可用。


可以直接使用外部事件 y（y = 0..9），也可以对其进行滤波处理（以在指定时间内限制其操作）。具体参考 。

## 25.4.7. 故障输入

HRTIMER 具有故障保护机制，可用于每个 Slave_TIMERx。具体请参考 25-51.。

发生故障事件时，输出（STxCHy_O，x = 0..7，y = 0,1）为预置的电平。

预置电平由 HRTIMER_STxCHOCTL 寄存器中的 CHyFLTOS[1:0]位域配置，保护机制可以处理三种类型的故障源：

 故障通道：来自数字输入引脚或比较器的故障事件；

 系统故障：来自MCU内部的信号，例如SRAM奇偶校验器；

 故障事件：故障事件来自外部事件y(y=0..9)。


图 25-51. 故障输入结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/cc52e09f97a4a311e9cd7f0038c2365e91f7e0c6038498a5e5cf4cbf45ad459f.jpg)


通过 HRTIMER_STxFLTCTL 寄存器中的 FLTyEN 位使能故障输入。对 HRTIMER_STxFLTCTL 寄存器中的 FLTENPROT 位的一次写入可以保护 FLTyEN 位。当 FLTENPROT 位置 1 时，FLTyEN位写保护（只读）。

## 故障通道

可以通过 HRTIMER_FLTINCFG0 和 HRTIMER_FLTINCFG1 寄存器配置所有的故障通道。

FLTyINSRC（y = 0..7）位用于选择故障通道源，即可以是数字输入引脚，也可以是比较器输出或外部事件。每个 Slave_TIMERx 都有 8 个故障通道（故障通道 0-7）可以使用。具体请见 25-21.故障通道映射。


表 25-21. 故障通道映射


<table><tr><td>故障通道</td><td>FLTyINSRC = 00 (外部引脚)</td><td>FLTyINSRC = 01 (内部信号)</td><td>FLTyINSRC = 10 (外部事件)</td></tr><tr><td>故障通道 0</td><td>PA12</td><td>比较器 1</td><td>外部事件 0</td></tr><tr><td>故障通道 1</td><td>PA15</td><td>比较器 3</td><td>外部事件 1</td></tr><tr><td>故障通道2</td><td>PB10</td><td>比较器5</td><td>外部事件2</td></tr><tr><td>故障通道3</td><td>PB11</td><td>比较器0</td><td>外部事件3</td></tr><tr><td>故障通道4</td><td>PB0/PC7</td><td>比较器2</td><td>外部事件4</td></tr><tr><td>故障通道5</td><td>PC10</td><td>比较器4</td><td>外部事件5</td></tr><tr><td>故障通道6</td><td>PC3</td><td>比较器6</td><td>外部事件6</td></tr><tr><td>故障通道7</td><td>PC4</td><td>比较器7</td><td>外部事件7</td></tr></table>


注意：“×”表示不可用。


可以通过 HRTIMER_FLTINCFG0 和 HRTIMER_FLTINCFG1 寄存器中的 FLTyINP 位来配置故障信号的极性。如果 FLTyINP = 0，信号低电平有效；如果 FLTyINP = 1，则高电平有效。

可通过 HRTIMER_FLTINCFG0 和 HRTIMER_FLTINCFG1 寄存器中的 FLTyINFC[3:0]位域，对设置 极 性 后 的 数 字 信 号 滤 波 器 进 行 配 置 。 数 字 滤 波 器 采 样 时 钟 f<sub>HRTIMER_FLTFCK</sub> 由HRTIMER_FLTINCFG1 寄存器中的 FLTFDIV[2:0]位域定义。

可通过 HRTIMER_FLTINCFG0 和 HRTIMER_FLTINCFG1 寄存器中的 FLTyINEN 位来使能故障通道 y（y = 0..7），所有通道可同时使能。

对 HRTIMER_FLTINCFG0 和 HRTIMER_FLTINCFG1 寄存器中 FLTyINPROT 位的一次写入，可保护 FLT0INEN 位，FLT0INP 位，FLT0INSRC 位和 FLT0INFC [3:0]位域。当 FLTyINPROT 位置1 时，这些位写保护（只读）。

## 故障消隐

在故障消隐模式下，在指定时间内发生的故障通道将被忽略，请参考 25-22. 。


表 25-22. 故障通道消隐


<table><tr><td rowspan="2">故障通道</td><td colspan="2">FLTxBLKS = 0,复位和比较窗口</td><td colspan="2">FLTxBLKS = 1,比较和比较窗口</td></tr><tr><td>消隐开始</td><td>消隐结束</td><td>消隐开始</td><td>消隐结束</td></tr><tr><td>故障通道0</td><td>Slave_TIMER0 复位 / 更新</td><td>Slave_TIMER0 比较2</td><td>Slave_TIMER0 比较3</td><td>Slave_TIMER0 比较2</td></tr><tr><td>故障通道1</td><td>Slave_TIMER1 复位 / 更新</td><td>Slave_TIMER1 比较2</td><td>Slave_TIMER1 比较3</td><td>Slave_TIMER1 比较2</td></tr><tr><td>故障通道2</td><td>Slave_TIMER2 复位 / 更新</td><td>Slave_TIMER2 比较2</td><td>Slave_TIMER2 比较3</td><td>Slave_TIMER2 比较2</td></tr><tr><td>故障通道3</td><td>Slave_TIMER3 复位 / 更新</td><td>Slave_TIMER3 比较2</td><td>Slave_TIMER3 比较3</td><td>Slave_TIMER3 比较2</td></tr><tr><td>故障通道4</td><td>Slave_TIMER4 复位 / 更新</td><td>Slave_TIMER4 比较2</td><td>Slave_TIMER4 比较3</td><td>Slave_TIMER4 比较2</td></tr><tr><td>故障通道5</td><td>Slave_TIMER5 复位 / 更新</td><td>Slave_TIMER5 比较 2</td><td>Slave_TIMER5 比较 3</td><td>Slave_TIMER5 比较 2</td></tr><tr><td>故障通道 6</td><td>Slave_TIMER6 复位 / 更新</td><td>Slave_TIMER6 比较 2</td><td>Slave_TIMER6 比较 3</td><td>Slave_TIMER6 比较 2</td></tr><tr><td>故障通道 7</td><td>Slave_TIMER7 复位 / 更新</td><td>Slave_TIMER7 比较 2</td><td>Slave_TIMER7 比较 3</td><td>Slave_TIMER7 比较 2</td></tr></table>

故 障 计 数 阈 值 由 HRTIMER_FLTINCFG2 寄 存 器 和 HRTIMER_FLTINCFG3 寄 存 器 中 的FLTyCNT[3:0] $( \mathsf { y } = 0 . . 7 )$ 配置。当故障通道事件的数量等于(FLTyCNT[3:0]+1) 时，故障生效。

FLTxRST 位复位，当复位或翻转事件发生时，故障计数器被复位，可参考 25-23.。

当 FLTxRST 位 置 位 时 ， 故 障 计 数 器 复 位 模 式 由 HRTIMER_FLTRECCTL 决 定 。 当HRTIMER_FLTRECCTL 寄存器中的 FLTRECCTL 位置 0 时，故障计数器仅在没有故障事件处于有效状态时，每次复位/翻转事件时复位。当 HRTIMER_FLTRECCTL 寄存器中的 FLTRECCTL 位置 1 时，故障计数器仅在一个周期内没有发生故障事件时，每次复位/翻转事件时复位。

注意：当 FLTxRST 位复位，故障计数器复位源取决于 25-23. 。当 FLTxRST位置位时，故障计数器复位源来自与故障通道连接的 Slave_TIMERx，与故障通道连接的Slave_TIMERx 的复位/翻转事件用于复位故障计数器。


图 25-52. 当 FLTxRST 为 1，FLTRECCTL 为 1 和 FLTxCNT[3:0] = 0x03 时故障计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/31109c276ae4fec1e968e69792edb674142ac05d3a8018c39ebfec9705b23ef4.jpg)



表 25-23. 故障通道复位源


<table><tr><td>故障通道</td><td>故障计数器复位源</td></tr><tr><td>故障通道 0</td><td>Slave_TIMER0 复位 / 翻转</td></tr><tr><td>故障通道 1</td><td>Slave_TIMER1 复位 / 翻转</td></tr><tr><td>故障通道 2</td><td>Slave_TIMER2 复位 / 翻转</td></tr><tr><td>故障通道 3</td><td>Slave_TIMER3 复位 / 翻转</td></tr><tr><td>故障通道 4</td><td>Slave_TIMER4 复位 / 翻转</td></tr><tr><td>故障通道 5</td><td>Slave_TIMER5 复位 / 翻转</td></tr><tr><td>故障通道 6</td><td>Slave_TIMER6 复位 / 翻转</td></tr><tr><td>故障通道 7</td><td>Slave_TIMER7 复位 / 翻转</td></tr></table>

## 故障恢复

## 故障硬件自动恢复

当故障源消失后，HRTIMER 通道恢复 PWM 波输出。

HRTIMER_STxACTL 寄 存 器 中 的 FLTAR 位 ， HRTIMER_FLTINCFG2 寄 存 器 和HRTIMER_FLTINCFG3 寄存器中的 FLTxRST 位同时使用，即同时置位 FLTxRST（x = 0..7）和FLTAR 位，能够实现故障消失后，下周期通道自动恢复 PWM 波输出。


图 25-53. 当 FLTxRST 为 1 和 FLTAR 为 1 时故障自动恢复


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/4a6a593c6f9d8a49c543a36846f356b099fc501c4d5d9451fc228730ee618f31.jpg)


## 故障恢复保护

当 FLTxRST（x = 0..7）位置 1 和 FLTRECCTL 位置 0 时，故障事件没有消失前，软件不能恢复PWM 输出。直到故障源消失且重新使能通道输出（置位 HRTIMER_CHOUTEN 寄存器的STxCHyEN 位, x = 0..7, y = 0,1）才能恢复 PWM 输出。

注意：HRTIMER_CHOUTEN 寄存器中的 STxCHyEN 位无法正确指示对应通道的实际输出状态。具体问题如下：

1）在硬件故障自动恢复后，PWM 通道恢复输出且 PWM波形恢复正常，但 STxCHyEN 位仍错误

地保持为 0，而不是恢复为 1。

2）在故障有效时，即使通过软件手动设置 STxCHyEN 位，PWM 输出仍保持禁用状态，而STxCHyEN 位却错误地显示为 1。

由于这些问题，在使用故障输入功能时，STxCHyEN 位无法可靠地指示通道状态。因此，建议避免依赖读取该位进行状态验证。

## 系统故障

系统故障来自芯片内部的信号：

 时钟监视生成的HXTAL故障事件；

 Cortex<sup>®</sup>-M33锁定信号；

 低压检测器（LVD）的输出。

当 HRTIMER_STxFLTCTL 寄存器中的 FLTyEN 位置 1 时，系统故障才有效。系统故障可以覆盖故障通道输入（逻辑或）。

## 25.4.8. ADC 触发

TRIGSEL可以触发ADC，10个独立的ADC触发（HRTIMER_ADCTRIG0 - HRTIMER_ADCTRIG9）可用于使能 ADC 的常规组。具体请参考 25-54. ADC 。


图 25-54. ADC 触发源选择图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/392dea22d95b1cc1e8c68ee81cbd15dbe00b237c20817a79ec39aff4875ac44d.jpg)


对于 ADC 触发 0 到 3（HRTIMER_ADCTRIG0 - HRTIMER_ADCTRIG3），每个触发输出最多可以连接（逻辑或运算）47 个事件。32 个事件在 HRTIMER_ADCTRIGSy（y = 0..3）寄存器中定义，15 个事件在 HRTIMER_ADCTRIGSyA（y = 0..3）寄存器中定义。

对于 ADC 触发 4 到 9（HRTIMER_ADCTRIG4 - HRTIMER_ADCTRIG9），每个触发输出一次只能连接 1 个事件（从 47 个事件中选择一个）。47 个事件在 HRTIMER_ADCEXTTRG、HRTIMER_ADCEXTTRGA 寄存器中定义。

HRTIMER_ADCTRIGSy（y = 0..3）寄存器，HRTIMER_ADCTRIGSyA（y = 0..3）寄存器，HRTIMER_ADCEXTTRG 寄存器和 HRTIMER_ADCEXTTRGA 寄存器使能预加载，并可以使用与其相关的定时器进行同步更新。更新源由 HRTIMER_CTL0 寄存器和 HRTIMER_ADCTRGUPD寄存器中的 ADTGyUSRC[3:0]位域定义。例如，ADTGyUSRC [3:0] = 3’b0001，Slaver_TIMER0是更新源：

 如果HRTIMER_STxCTL0寄存器中的SHWEN = 1，HRTIMER_ADCTRIGSy（y = 0..3）寄存器和HRTIMER_ADCTRIGSyA（y = 0..3）被预加载，可以与Slaver_TIMER0同步更新；

 如果HRTIMER_STxCTL0寄存器中的SHWEN = 0，HRTIMER_ADCTRIGSy（y = 0..3）寄存器和HRTIMER_ADCTRIGSyA（y = 0..3）不会被预加载，写访问将使触发源立即更新。HRTIMER_ADCTRIGS0- HRTIMER_ADCTRIGS9为了更兼容ADC触发，设置了触发分频等功能，需要注意的是，这几种触发源连接到TRIGSEL，具体触发什么模块由TRIGSEL决定。

## ADC 触发分频

ADC 的触发频率可以通过配置 HRTIMER_ADCPSCRy（y=0,1）寄存器来进行调整。具体的配置涉及设置 HRTIMER_ADCPSCRy 寄存器中的 ADCxPSC[4:0] 位。

在向上计数模式下，触发频率仅与 HRTIMER_ADCPSCRy 寄存器中的 ADCxPSC[4:0] 位有关。然而，在中央对齐计数模式下，ADC 触发频率不仅受到 ADCxPSC[4:0]的影响，还受到HRTIMER_STxCTL1 寄存器中的 ADCROVM[1:0] 位的影响。ADCROVM[1:0] 的不同配置如下：

 ADCROVM[1:0] = 00：计数器在向上计数和向下计数方向时生成 ADC 触发事件。

 ADCROVM[1:0] = 01: 计数器在向下计数方向时生成 ADC 触发事件。

 ADCROVM[1:0] = 10：计数器在向上计数方向时生成 ADC 触发事件。


图 25-55. 向上计数模式下 ADC 触发分频


<table><tr><td colspan="2">Counter</td></tr><tr><td rowspan="2">ADCxPSC[4:0] = 0</td><td>↑</td></tr><tr><td>↓</td></tr><tr><td rowspan="2">ADCxPSC[4:0] = 1</td><td>↑</td></tr><tr><td>↓</td></tr><tr><td rowspan="2">ADCxPSC[4:0] = 2</td><td>↑</td></tr><tr><td>↓</td></tr><tr><td rowspan="2">ADCxPSC[4:0] = 3</td><td>↑</td></tr><tr><td>↓</td></tr><tr><td>ADCxPSC[4:0] = 4</td><td>↑</td></tr></table>


图 25-56. 中央对齐计数模式下 ADC 触发分频


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/62c80856c69ac0265194a572e792f142c5c068f5fa52c376aa15a64ef2ad5a86.jpg)


## 25.4.9. DAC 触发

HRTIMER 允许使用定时器更新同步更新片上 DAC。Master_TIMER 和 Slave_TIMERx 的更新事件可以在 HRTIMER_DACTRIGy（y = 0..2）上生成 DAC 更新触发。

HRTIMER_MTCTL0 和 HRTIMER_STxCTL0 寄存器中的 DACTRGS [1:0]位域配置如下：

 00：没有DAC触发事件发生；

 01：在HRTIMER_DACTRIG0上生成DAC触发事件；

 10：在HRTIMER_DACTRIG1上生成DAC触发事件；

 11：在HRTIMER_DACTRIG2上生成DAC触发事件。

HRTIMER_DACTRG0- HRTIMER_DACTRG2兼容DAC触发，需要注意的是，这几种触发源连接到TRIGSEL，具体触发什么模块由TRIGSEL决定。

在多个计时器中使能 DACTRGS [1:0]位域时，HRTIMER_DACTRIGy（y = 0..2）将由所有定时器的更新事件或组成。具体请参考 25-57. DAC 。


图 25-57. DAC 触发源选择图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/f45042b2ea99fedcb56a95ba2b634e32ec89afbdfec34b1acd4c12cc9cbd1e5d.jpg)


在 DAC 触发输出上生成一个持续 32 个 f<sub>APB2</sub> 时钟周期的脉冲。同步脉冲在这 32 个 APB2 时钟周期的空闲期，在此期间，任何新的 DAC 更新请求都将被忽略。因此，最大同步频率为 f<sub>APB2</sub>/ 64。

HRTIMER_DACTRIG0- HRTIMER_DACTRIG2 触发源连接到 TRIGSEL，具体触发什么模块由TRIGSEL 决定。

## 25.4.10. 双通道触发模式

启用双通道触发模式需要设置 HRTIMER_STxCTL1 寄存器中的 TRIGEN 位。并且定时器运行中(STxCEN 位置位)，就无法更改 TRIGEN 位。此时 HRTIMER_STxCTL1 寄存器中的 TRIG0M 和TRIG1M 配置 Slave_TIMERx 输出的触发信号 TRIG0 和 TRIG1 连接到 TRIGSEL（在 TRIGSEL模 块 分 别 为 HRTIMER_STx_TRIG0 和 HRTIMER_STx_TRIG1 ）， 可 通 过 配 置HRTIMER_STxCTL1 寄存器中的 TRIG0M 位和 TRIG1M 位，选择触发信号源。

TRIG0 信号通过 TRIG0M 进行配置。

 TRIG0M = 0 : 比较1事件生成TRIG0触发信号。

 TRIG0M = 1 : 输出0复位事件生成TRIG0触发信号。

TRIG1 信号通过 TRIG1M 进行配置。

 TRIG1M = 0 : 计数器复位或翻转事件生成TRIG1触发信号。

 TRIG1M = 1 : 输出0置位事件生成TRIG1触发信号。

下面以 DAC 为例来说明双通道触发模式的使用场景，通过双通道触发模式可以轻松实现斜坡补偿技术和滞环控制。在此模式下，DAC 输出一个逐渐减小的锯齿信号，锯齿波的周期与 PWM 波的

周期同步。

注意：在双通道触发模式下，当 TRIG0M = 0 和 TRIG1M = 0 时，只有 Slave timer 0 和 Slave timer3 支持硬件斜坡补偿，但比较 1 寄存器具有以下限制：

$$
\text { 当 } \mathrm{CNTCKDIV} [ 2: 0 ] <   3 ^ {\prime} \mathrm{b} 1 0 1
$$

 最小值必须大于或等于8个t<sub>HRTIMER_CK</sub>周期对应的计数值；

注意：每个t<sub>HRTIMER_CK</sub>周期对应的计数值 = f<sub>HRTIMER_PSSCK</sub> / f<sub>HRTIMER_CK。</sub>

当 CNTCKDIV[2:0] >= 3’b101

 最小值必须大于或等于0x0008。

DAC 模块可根据来自 TRIGSEL 的触发信号自定义选择哪个信号触发 DAC 产生步进或者复位信号。此处举例描述以来自 HRTIMER 的 TRIG0 产生步进信号，TRIG1 产生复位信号。需要注意的是触发 DAC 步进或复位的信号不仅仅是这两个信号，凡是来自 TRIGSEL 的信号均可触发。


图 25-58. 当 TRIG0M= 0 和 TRIG1M = 0 时 DAC 触发


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/5877018c4afc3836a622c5bf9f4cd07b6c057a5dffd67f8dfefaab1098fdc10c.jpg)



TRIG1M = 0, the trigger is generated on counter reset or roll-over event TRIGoM = 0,the trigger is generated on compare 1 event



图 25-59. 当 TRIG0M = 1 和 TRIG1M = 1 时 DAC 触发


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/0ae6bbd106ec4bd8af971b4ac5dac457c8f072ec757afe3d4d5086bbcbe72abc.jpg)


## 25.4.11. 中断

大多数事件可以生成中断请求，所有的中断请求可分组到 10 个中断向量(HRTIMER_IRQy，y=0..9)。详见 25-24. 。


表 25-24. 中断映射


<table><tr><td>中断号</td><td>事件</td><td>Control bit</td></tr><tr><td rowspan="7">Master_TIMER:HRTIMER_IRQ0</td><td>更新事件</td><td>HRTIMER_MTDMAINTEN 中的 UPIE 位</td></tr><tr><td>同步输入事件</td><td>HRTIMER_MTDMAINTEN 中的 SYNIIE 位</td></tr><tr><td>重复事件</td><td>HRTIMER_MTDMAINTEN 中的 REPIE 位</td></tr><tr><td>比较 0 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP0IE 位</td></tr><tr><td>比较 1 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP1IE 位</td></tr><tr><td>比较 2 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP2IE 位</td></tr><tr><td>比较 3 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP3IE 位</td></tr><tr><td rowspan="4">Slave_TIMER0:HRTIMER_IRQ1Slave_TIMER1:HRTIMER_IRQ2Slave_TIMER2:</td><td>延迟空闲模式进入</td><td>HRTIMER_STxDMAINTEN 中的 DLYIIE 位</td></tr><tr><td>计数器复位事件</td><td>HRTIMER_STxDMAINTEN 中的 RSTIE 位</td></tr><tr><td>C1OPRE 从有效到无效</td><td>HRTIMER_STxDMAINTEN 中的 CH1ONAIE 位</td></tr><tr><td>C1OPRE 从无效到有效</td><td>HRTIMER_STxDMAINTEN 中的 CH1OAIE 位</td></tr></table>


GD32G553 用户手册


<table><tr><td>中断号</td><td>事件</td><td>Control bit</td></tr><tr><td rowspan="10">HRTIMER_IRQ3 Slave_TIMER3: HRTIMER_IRQ4 Slave_TIMER4: HRTIMER_IRQ5 Slave_TIMER5: HRTIMER_IRQ6 Slave_TIMER6: HRTIMER_IRQ7 Slave_TIMER7: HRTIMER_IRQ8</td><td>C0OPRE 从有效到无效</td><td>HRTIMER_STxDMAINTEN 中的 CH0ONAIE 位</td></tr><tr><td>C0OPRE 从无效到有效</td><td>HRTIMER_STxDMAINTEN 中的 CH0OAIE 位</td></tr><tr><td>捕获 1 事件</td><td>HRTIMER_STxDMAINTEN 中的 CAP1IE 位</td></tr><tr><td>捕获 0 事件</td><td>HRTIMER_STxDMAINTEN 中的 CAP0IE 位</td></tr><tr><td>更新事件</td><td>HRTIMER_STxDMAINTEN 中的 UPIE 位</td></tr><tr><td>重复事件</td><td>HRTIMER_STxDMAINTEN 中的 REPIE 位</td></tr><tr><td>比较 3 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP3IE 位</td></tr><tr><td>比较 2 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP2IE 位</td></tr><tr><td>比较 1 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP1IE 位</td></tr><tr><td>比较 0 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP0IE 位</td></tr><tr><td rowspan="2">HRTIMER_IRQ0</td><td>突发模式周期事件</td><td>HRTIMER_INTEN 中的 BMPERIE 位</td></tr><tr><td>DLL 校准完成</td><td>HRTIMER_INTEN 中的 DLLCALIE 位</td></tr><tr><td rowspan="2">HRTIMER_IRQ9</td><td>系统故障</td><td>HRTIMER_INTEN 中的 SYSFLTIE 位</td></tr><tr><td>故障 x (x = 0..7)</td><td>HRTIMER_INTEN 中的 FLTxIE (x = 0..7)位</td></tr></table>

## 25.4.12. DMA 请求

大多数事件可以生成 DMA 请求，每个定时器对应一个 DMA通道，详见 25-25. DMA 。


表 25-25. DMA 请求映射


<table><tr><td>DMA channel</td><td>Event</td><td>Control bit</td></tr><tr><td rowspan="7">Master_TIMER:</td><td>更新事件</td><td>HRTIMER_MTDMAINTEN 中的 UPDEN 位</td></tr><tr><td>同步输入事件</td><td>HRTIMER_MTDMAINTEN 中的 SYNIDEN 位</td></tr><tr><td>重复事件</td><td>HRTIMER_MTDMAINTEN 中的 REPDEN 位</td></tr><tr><td>比较 0 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP0DEN 位</td></tr><tr><td>比较 1 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP1DEN 位</td></tr><tr><td>比较 2 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP2DEN 位</td></tr><tr><td>比较 3 事件</td><td>HRTIMER_MTDMAINTEN 中的 CMP3DEN 位</td></tr><tr><td rowspan="10">Slave_TIMER0: Slave_TIMER1: Slave_TIMER2: Slave_TIMER3: Slave_TIMER4: Slave_TIMER5: Slave_TIMER6: Slave_TIMER7:</td><td>延迟空闲模式进入</td><td>HRTIMER_STxDMAINTEN 中的 DLYIDEN 位</td></tr><tr><td>计数器复位事件</td><td>HRTIMER_STxDMAINTEN 中的 RSTDEN 位</td></tr><tr><td>C1OPRE 从有效到无效</td><td>HRTIMER_STxDMAINTEN 中的 CH1ONADEN 位</td></tr><tr><td>C1OPRE 从无效到有效</td><td>HRTIMER_STxDMAINTEN 中的 CH1OADEN 位</td></tr><tr><td>C0OPRE 从有效到无效</td><td>HRTIMER_STxDMAINTEN 中的 CH0ONADEN 位</td></tr><tr><td>C0OPRE 从无效到有效</td><td>HRTIMER_STxDMAINTEN 中的 CH0OADEN 位</td></tr><tr><td>捕获 1 事件</td><td>HRTIMER_STxDMAINTEN 中的 CAP1DEN 位</td></tr><tr><td>捕获 0 事件</td><td>HRTIMER_STxDMAINTEN 中的 CAP0DEN 位</td></tr><tr><td>更新事件</td><td>HRTIMER_STxDMAINTEN 中的 UPDEN 位</td></tr><tr><td>重复事件比较 3 事件</td><td>HRTIMER_STxDMAINTEN 中的 REPDEN 位HRTIMER_STxDMAINTEN 中的 CMP3DEN 位</td></tr><tr><td rowspan="3"></td><td>比较 2 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP2DEN 位</td></tr><tr><td>比较 1 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP1DEN 位</td></tr><tr><td>比较 0 事件</td><td>HRTIMER_STxDMAINTEN 中的 CMP0DEN 位</td></tr></table>


注意：必须先禁能 DMA控制器，然后再禁能 DMA请求。


## 25.4.13. DMA 模式

定时器的DMA模式是通过DMA模块，实现单个DMA请求配置HRTIMER的多个寄存器的功能。相关的寄存器（总共十个寄存器）如下：

 HRTIMER_DMAUPMTR：定义更新Master_TIMER中的哪些寄存器。Master_TIMER的大多数控制和数据寄存器都与一个选择位关联。如果该选择位置位，则写访问将重定向到关联的寄存器；

HRTIMER_DMAUPSTxR(x=0..7) ： 定 义 更 新 Slave_TIMERx 中 的 哪 些 寄 存 器 。 大 多 数Slave_TIMERx控制和数据寄存器都与一个选择位相关联。如果该选择位被置位，则写访问将重定向到关联的寄存器。

HRTIMER_DMATB：DMA传输缓冲区寄存器。只需要将指向HRTIMER_DMATB寄存器的DMA模块作为目标，并禁能外设增量模式的外设配置。所有对该寄存器的写访问都将通过重定向机制在内部重新传输到最终目标寄存器。

DMA 模式是永久使能的（没有使能位）。通过对 HRTIMER_DMATB 寄存器的首次写访问来启动DMA 操作。

发生 DMA 请求时，HRTIMER 会生成多个 32 位 DMA 请求并解析要更新的寄存器（在HRTIMER_DMAUPMTR 和 HRTIMER_DMAUPSTxR 寄存器中定义）。如果选择位置 1，则写访问将重定向到关联的寄存器。如果选择位为 0，则跳过相关寄存器更新，并继续进行寄存器解析，直到检测到新的位置 1，触发新的 DMA 请求。9 个寄存器（HRTIMER_DMAUPMTR 和HRTIMER_DMAUPSTxR 寄存器）全部解析后，DMA 模式完成，系统已准备好等待下一个 DMA触发。若再有 DMA 请求事件发生，则 HRTIMER 将重复上述过程。详见 25-60. DMA流程图


图 25-60. DMA 模式运行流程图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/1af05897-7530-43aa-be20-5e8118b0ecd7/6b442bab5eedf57864d9adef69f96f2c40833c60ecd31382c711b6ff1ef4913f.jpg)


## 25.4.14. Debug 模式

当 Cortex<sup>®</sup>-M33 内核暂停时，DBG_CTL0 寄存器中的 HRTIMER_HOLD 位决定了计数器是否停止运行。

## HRTIMER_HOLD = 0

若 HRTIMER_HOLD = 0，则 HRTIMER 继续正常运行。

## HRTIMER_HOLD = 1

若 HRTIMER_HOLD = 1，则将停止 Master_TIMER 和所有 Slave_TIMERx 中的计数器。

如 果 CHyFLTOS[1:0] = 2’b01 、 2’b10 、 2’b11 ， 则 输 出 进 入 FAULT 状 态 。 可 以 通 过 将HRTIMER_CHOUTEN 寄存器中的 STxCHyEN 位置 1，清零 HRTIMER_HOLD 位来再次使能输出。如果 CHyFLTOS [1:0] = 2’b00，则输出保持其当前状态。退出调试模式时，输出将返回其原始状态。

所有计数器的复位/启动和捕获触发功能都禁能。除 ADC 触发外，所有外部事件的触发都被禁能。更新事件将被丢弃。突发模式电路被冻结：触发都被忽略，突发模式计数器停止。

DLL 校准正常运行。在运行模式下驱动正常输出的单元不受调试影响，例如死区时间单元，载波信号和置位/复位交叉开关等。

