## 19. 超高分辨率定时器（SHRTIMER）

## 19.1. 简介

SHRTIMER 具有超高分辨率计数时钟，可用于高精度定时。它可以产生 10 个超高分辨率的数字信号来灵活地控制电动机或用于电源管理应用。这 10 个数字信号可以独立输出，也可以耦合成 5 对互补信号输出。

SHRTIMER 具有灵活的捕获功能，可用于捕获输入信号的时序。它具有多个连接到 ADC 和DAC 的内部信号，可用于控制和监视。

为了安全起见，SHRTIMER 可处理各种故障输入。

## 19.2. 主要特征

 超高分辨率定时单元：Master_TIMER，Slave_TIMERx (x=0..4)；

 10个数字信号输出：它们可由任意一个定时单元控制，可独立输出也可耦合成5对互补输出；

 同步输出：作为主机同步外部资源；

 同步输入：作为从机与外部资源同步；

 多个内部信号连接到ADC和DAC；

 多种故障输入保护机制：故障输入通道和系统故障；

 突发模式控制器应用于轻载操作；

 7个中断向量：Master_TIMER中断，Slave_TIMERx（x = 0..4）中断和故障中断；

 6个DMA请求：Master_TIMER请求和Slave_TIMERx（x = 0..4）请求。DMA模式可以更新多个寄存器；

 DMA模式用于多个寄存器的更新。

## 19.3. 结构框图

19-1. SHRTIMER 给出了 SHRTIMER 的内部细节配置。


图 19-1. SHRTIMER 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/03cc83edd5ce5abd6bc84a7f23490fbb11204876fd9912027d543d7b785ea5e3.jpg)


## 19.4. 功能说明

## 19.4.1. Master_TIMER 单元

Master_TIMER 单元由以下模块组成：

 16位计数器

 自动重载寄存器：确定计数周期

 重复计数器

 比较寄存器y(y=0..3)

19-2. Master_TIMER 给出了 Master_TIMER 的内部细节配置。


图 19-2. Master_TIMER 结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/df61559b37da65bb9209d4b7d2af10f4db80fd7cf6adc4fe900f20280edf44d0.jpg)


自动重载寄存器和比较 y（y = 0..3）寄存器具有以下限值：

当 $\mathtt { C N T C K D I V } [ 3 : 0 ] < 4 ^ { \prime } { \bmod { 0 } } 1 0 1$ 或 $\mathtt { C N T C K D I V } [ 3 : 0 ] = 4 ^ { \prime } \mathtt { b } 1 0 0 0$ 

 最小值必须大于或等于3个t<sub>SHRTIMER_CK</sub>周期对应的计数值；

 最大值必须小于或等于（0xFFFF – 1个t<sub>SHRTIMER_CK</sub>周期对应的计数值）。

注意：每个 t<sub>SHRTIMER_CK</sub> 周期对应的计数值 = f<sub>SHRTIMER_PSSCK</sub> / f<sub>SHRTIMER_CK</sub>。

当 CNTCKDIV[3:0] >= 4’b0101(不包括 CNTCKDIV[3:0] = 4’b1000)

 最小值必须大于或等于0x0003；

 最大值必须小于或等于0xFFFE。

具体请见 19-1. y $\textcircled { y = 0 . . 3 }$ 寄存器的限值


表 19-1. 自动重载寄存器和比较 y（y = 0..3）寄存器的限值


<table><tr><td>CNTCKDIV[3:0]</td><td>最小值</td><td>最大值</td></tr><tr><td>4&#x27;b1000</td><td>0x00C0</td><td>0xFFBF</td></tr><tr><td>4&#x27;b0000</td><td>0x0060</td><td>0xFFDF</td></tr><tr><td>4&#x27;b0001</td><td>0x0030</td><td>0xFFEF</td></tr><tr><td>4&#x27;b0010</td><td>0x0018</td><td>0xFFFF7</td></tr><tr><td>4&#x27;b0011</td><td>0x000C</td><td>0xFFFFB</td></tr><tr><td>4&#x27;b0100</td><td>0x0006</td><td>0xFFFFD</td></tr><tr><td>4&#x27;b0101</td><td>0x0003</td><td>0xFFFE</td></tr><tr><td>4&#x27;b0110</td><td>0x0003</td><td>0xFFFE</td></tr><tr><td>4&#x27;b0111</td><td>0x0003</td><td>0xFFFE</td></tr></table>

## 计数器时钟

Master_TIMER 的时钟源可以有两个，分别是由 RCU 模块提供的 CK_APB2 和 CK_SYS。如用户选择使用 CK_APB2 产生 SHRTIMER_CK，需要注意 SHRTIMER_ MTCTL0 寄存器中的CNTCKDIV[2:0]值必须大于或等于 5（预分频比大于或等于 64）；DLL 用于产生超高分辨率时钟 SHRTIMER_HPCK（f<sub>SHRTIMER_HPCK</sub> = 64 * f<sub>SHRTIMER_CK</sub>），此时 SHRTIMER_CK 必须由CK_SYS产生，更多信息请参考 DLL 。

当 SHRTIMER_MTACTL 寄存器中的 CNTCKDIV[3]位为 0 时，预分频器（PSC）将超高分辨率 时 钟 （ SHRTIMER_HPCK ） 除 以 分 频 因 子 2CNTCKDIV[2:0]+1 ， 得 到 计 数 器 时 钟（SHRTIMER_PSCCK）。该分频因子由 SHRTIMER_MTCTL0 寄存器中的 CNTCKDIV[2:0]位域控制。它们之间的频率关系可以表示如下：

$$
f _ {\text { SHRTIMER\_PSCCK }} = f _ {\text { SHRTIMER\_HPCK }} / 2 ^ {\text { CNTCKDIV[2:0]+1}}\tag{19-1}
$$

当 SHRTIMER_MTACTL 寄存器中的 CNTCKDIV[3]位为 1 时，CNTCKDIV[2:0]位只能配置为3’b000， SHRTIMER_PSCCK 和 SHRTIMER_HPCK 之间的频率关系可以表示为：

$$
f _ {\text { SHRTIMER\_PSCCK }} = f _ {\text { SHRTIMER\_HPCK }}\tag{19-2}
$$

注意：一旦 Master_TIMER 使能了，就不能修改时钟分频 CNTCKDIV[3:0]的值。

19-3. 32 显示了将寄存器 SHRTIMER_MTCAR 设置为 0x0104，SHRTIMER_MTCTL0 寄存器中的位域 CNTCKDIV[3: 0]设置为 4'b0100 时计数器的动作。


图 19-3. 分频为 32 时计数器时钟


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/0b742238adab02d2181c7d1d688801357cda9064495b9a063ea07d0ff7fee4fe.jpg)


19-2. fSHRTIMER<sub>_CK</sub> = 180MHz 列出了 f<sub>SHRTIMER_CK</sub> 为 180MHz 时的不同分辨率。


表 19-2. f<sub>SHRTIMER_CK</sub> = 180MHz 的分辨率


<table><tr><td>CNTCKDIV[3:0]</td><td>fSHRTIMER_PSCCK</td><td>分辨率</td></tr><tr><td>4&#x27;b0000</td><td>180*32MHz=5.76GHz</td><td>173.6ps</td></tr><tr><td>4&#x27;b0001</td><td>180*16MHz=2.880GHz</td><td>347.2ps</td></tr><tr><td>4&#x27;b0010</td><td>180*8MHz=1.440GHz</td><td>694.4ps</td></tr><tr><td>4&#x27;b0011</td><td>180*4MHz=720MHz</td><td>1.4ns</td></tr><tr><td>4&#x27;b0100</td><td>180*2MHz=360MHz</td><td>2.8ns</td></tr><tr><td>4&#x27;b0101</td><td>180*1MHz=180MHz</td><td>5.6ns</td></tr><tr><td>4&#x27;b0110</td><td>180/2MHz=90MHz</td><td>11.1ns</td></tr><tr><td>4&#x27;b0111</td><td>180/4MHz=45MHz</td><td>22.2ns</td></tr><tr><td>4&#x27;b1000</td><td>180*64MHz=11.520G</td><td>86.8ps</td></tr></table>

## 向上计数模式

计数器从 0 连续递增到计数器重载值，该值在 SHRTIMER_MTCAR 寄存器中定义。计数器有两种工作模式：单脉冲模式（SHRTIMER_MTCTL0 寄存器中的 CTNM = 0）或连续模式（CTNM= 1）。

在单脉冲模式下，将 SHRTIMER_MTCTL0 寄存器中的 MTCEN 位置 1 后，第一个复位事件将启动计数器。当计数到计数器重载值时，计数器停止并生成周期事件。然后，其他的复位事件将复位并重新启动计数器。在计数过程中，如果 SHRTIMER_MTCTL0 寄存器中的CNTRSTM = 1，则复位事件将复位并重新启动计数器，否则将被忽略。 19-4.显示了单脉冲模式下的计数器运行情况。


图 19-4. 单脉冲模式下计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/67f2439d1b72b841e4909b1415619f6ce2aa375a23118a8e1bd01cf1331d1cbb.jpg)


在连续模式下，一旦 SHRTIMER_MTCTL0 寄存器中的 MTCEN 位置 1，计数器将立即启动。当计数到计数器重载值时，计数器从 0 重新启动，并产生翻转事件。与单脉冲模式不同，随时生成的复位事件将复位并重启计数器。 19-5. 显示了连续模式下的计数器运行情况。


图 19-5. 连续模式下计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/899e94347c9386fb62c2ae270b237a509ec7586601760f95353766a947576b9b.jpg)


## 重复计数器

SHRTIMER_MTCTL0 寄 存 器 中 的 MTCEN 位 置 1 时 ， 重 复 计 数 器 将 加 载SHRTIMER_MTCREP 寄存器的值。当由于复位事件或连续模式下的翻转事件清零计数器时，重复计数器值递减。当重复计数器值达到零时，复位事件或连续模式下的翻转事件将产生一个重复事件并重新加载 SHRTIMER_MTCREP 寄存器的值。

重复事件会将 SHRTIMER_MTINTF 寄存器中的 REPIF 位置 1，如果使能了相应中断或 DMA请求（SHRTIMER_MTDMAINTEN 寄存器中的 REPIE = 1 或 REPDEN = 1），则会产生重复中断和 DMA 请求。可以通过向 SHRTIMER_MTINTFC 寄存器中的 REPIFC 位写 1 来清除重复中断标志。

19-6. 显示了在连续模式下重复计数器的运行情况。


图 19-6. 连续模式下重复计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/866eb0aea7c744aaf37838586873131fec245bb9b4fa8f3045a09f96c580ef87.jpg)



19-7. CNTRSTM = 0 显示了单脉冲模式下，CNTRSTM时重复计数器的运行情况。



图 19-7. 单脉冲模式下，CNTRSTM = 0 时重复计数器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/15c3d0ce81b1b11c1f942bae7c84e1f9437da5a9f4cb7eed8aecd6b249ae8613.jpg)



19-8. CNTRSTM = 1 显示了单脉冲模式下，CNTRSTM= 1 时重复计数器的运行情况。



图 19-8. 单脉冲模式下，CNTRSTM = 1 时重复计数器的动作


<table><tr><td>MTCEN或STxCEN(x=0..4)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>复位事件</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CounterCTNM = 0CNTRSTM = 1</td><td></td><td></td><td></td><td>CARL</td><td></td><td>CARL</td></tr><tr><td>CREP[7:0]</td><td>0x03</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>重复计数器</td><td></td><td>0x03</td><td>0x02</td><td>0x01</td><td>0x00</td><td>0x03</td></tr><tr><td>REPIF位</td><td></td><td></td><td></td><td></td><td></td><td>通过REPIFC位清零</td></tr></table>

## 计数器复位

一旦计数器（MTCEN = 1）使能了，就可以通过软件或同步输入将计数器复位为 0。

将 MTSRST 位置 1（由硬件自动清除）将使计数器复位。

当 SHRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以复位计数器。详细信息请参考 。

当计数器时钟 SHRTIMER_PSCCK 的预分频系数大于 64（CNTCKDIV [3]=1’b0，且CNTCKDIV [2:0] > 3’b101）时，计数器复位事件将延迟到 SHRTIMER_PSCCK 的下一个上升沿。

19-9. 128 显示了连续模式下，CNTCKDIV[3:0] =4’b0110，SHRTIMER_MTCAR = 0x4 时的运行情况。


图 19-9. 当预分频系数为 128时，复位事件重新同步


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/51ff75bb2a305ad76c2e44a6b072adc773e02c3925b7cc8a3a5dd78119734eec.jpg)


## 比较

Master_TIMER 具有四个比较寄存器：SHRTIMER_MTCMPxV（x = 0..3）。当计数器值与比较寄存器值匹配时，将生成一个对应的比较事件。

比较事件会将相应的比较中断标志位置 1（SHRTIMER_MTINTF 寄存器中的 ${ \mathsf { C M P x l F } }$ 位，x =0..3），如果比较中断或 DMA 请求使能（SHRTIMER_MTDMAINTEN 寄存器中的 CMPxIE = 1或 CMPxDEN = 1，x = 0..3），则会产生一个比较中断或 DMA 请求。通过写 1 到SHRTIMER_MTINTFC 中的 CMPxIF 位 $( \mathsf { x } = 0 . . 3 )$ 可以清除比较中断标志。

## 半波模式

当 SHRTIMER_MTCTL0 中的 HALFM 位置 1 时，半波模式使能。此模式将比较 0 有效寄存器的值强制为计数器重载值的一半，但 SHRTIMER_MTCMP0V 寄存器的值不会更新为（SHRTIMER_MTCAR / 2）的值。半波模式主要用于生成固定占空比为 50％的方波。

当 SHRTIMER_MTCTL0 寄存器中的 SHWEN 位置 1 时，将使能影子寄存器，比较 0 有效寄存器的值在更新事件时刷新。反之，比较 0 有效寄存器在新值写入 SHRTIMER_MTCAR 后立即刷新。

## 同步输入启动/复位计数器

当 SHRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以产生计数器复位事件；当 SHRTIMER_MTCTL0 寄存器中的 SYNISTRT 位置 1 时，同步输入可以启动计数器。更多信息请参考 。

同步输入请求会将 SHRTIMER_MTINTF 寄存器中的 SYNIIF 位置 1，如果使能了中断或 DMA请求（SHRTIMER_MTDMAINTEN 寄存器中的 SYNIIE = 1 或 SYNIDEN = 1），会产生相应的中断或 DMA 请求。可以通过写 1 到 SHRTIMER_MTINTFC 寄存器中的 SYNIIFC 位清除同步输入中断标志。

## 更新事件和影子寄存器

Master_TIMER 中的某些寄存器具有影子寄存器。MCU 复位后，影子寄存器被禁用。如果将SHRTIMER_MTCTL0 寄存器中的 SHWEN 位清 0，则将禁用影子寄存器。写入这些寄存器的

值将转移到活动寄存器中并生效。

SHRTIMER_MTCTL0 寄存器中的 SHWEN 位置 1，将使能影子寄存器并预加载这些寄存器。写入这些寄存器的值将被传送到影子寄存器，且不会立即生效。当发生更新事件时，影子寄存器内容将转移到活动寄存器中并立即生效。

注意：当 SHWEN=1 时，才会产生更新事件。

19-3. Master_TIMER 列出了具有影子寄存器的寄存器和相应的更新事件。


表 19-3. Master_TIMER 影子寄存器和更新事件


<table><tr><td>具有影子寄存器的寄存器</td><td>影子寄存器使能位</td><td>更新事件</td></tr><tr><td>SHRTIMER_MTDMAINTEN</td><td rowspan="7">SHRTIMER_MTCTL0 寄存器中的 SHWEN 位</td><td>软件(MTSUP位)</td></tr><tr><td>SHRTIMER_MTCAR</td><td>重复事件(UPREP = 1)</td></tr><tr><td>SHRTIMER_MTCREP</td><td>DMA模式结束事件(UPSEL[1:0] = 2&#x27;b01)</td></tr><tr><td>SHRTIMER_MTCMP0V</td><td rowspan="4">DMA模式结束事件之后的翻转事件(UPSEL[1:0] = 2&#x27;b10)</td></tr><tr><td>SHRTIMER_MTCMP1V</td></tr><tr><td>SHRTIMER_MTCMP2V</td></tr><tr><td>SHRTIMER_MTCMP3V</td></tr></table>

Master_TIMER 有 4 个更新选项：

1. 软件生成更新事件。写 1 到 SHRTIMER_CTL1 寄存器的 MTSUP 位可以产生更新事件。此时，无论 SHRTIMER_MTCTL0 寄存器中的 UPSEL[1:0]位如何配置，所有挂起的硬件更新事件都将被忽略；

2. 重复事件生成更新事件。如果 SHRTIMER_MTCTL0 寄存器中的 UPREP 位置 1，由翻转事件或复位事件引起的重复事件会生成更新事件。SHRTIMER_MTCTL0 寄存器中的$\mathsf { U P S E L } [ 1 : 0 ] = 2 ^ { \prime } \mathsf { b } 1 0$ ，则重复事件不生成更新事件；

3. 当 DMA 模式下的 DMA 传输完成时，生成更新事件。如果 SHRTIMER_MTCTL0 寄存器中的 $\mathsf { U P S E L } [ 1 : 0 ] = 2 ^ { , } \ \mathsf { b 0 } 1$ ，则在 DMA 模式下的 DMA传输完成时，硬件会自动生成更新事件。也可以通过软件或重复事件来生成更新事件。

4. 当 DMA 模 式 下 的 DMA 传输完成后，计数器的翻转会产生更新事件。如果SHRTIMER_MTCTL0 寄存器中的 UPSEL $[ 1 { : } 0 ] = 2 ^ { \prime } \ \mathsf { b } 1 0$ ，则在 DMA 模式下的 DMA 传输完成后，计数器发生翻转事件时，硬件会自动生成更新事件。也可以通过软件生成更新事件。

更新事件会将 SHRTIMER_MTINTF 寄存器中的 UPIF 位置 1，如果使能了相应的中断和 DMA功能（SHRTIMER_MTDMAINTEN 寄存器中的 UPIE = 1 或 UPDEN = 1），则会产生中断或DMA 请求。可以通过将 SHRTIMER_MTINTFC 中的 UPIFC 位写 1，来清除更新事件中断标志。

## DAC 触发

当 Master_TIMER 的 更 新 事 件 发 生 时 ， 如 果 SHRTIMER_MTCTL0 寄 存 器 中 的$\mathsf { D A C T R G S } [ 1 : 0 ] \ ! = \ 2 ^ { \prime } \ \mathsf { b 0 0 }$ ，则在 SHRTIMER_DACTRIGOx（x = 0..3）上生成 DAC 触发请求。如果 SHRTIMER_MTCTL0 寄存器中的 $\mathsf { D A C T R G S } \ [ 1 : 0 ] = 2 ^ { \prime } \ \mathsf { b 0 0 }$ ，则不会生成 DAC 触发请求。SHRTIMER_DACTRIGOx（x = 0..3）是从 Master_TIMER 连接到 DAC 模块的内部信号。有关更多信息，请参考 DAC 。

## 19.4.2. Slave_TIMERx(x=0..4)单元

SHRTIMER 具有 5 个相同结构的从定时器：Slave_TIMERx（x = 0..4）。每个从定时器都由以下组件构成：

 16位计数器

 自动重载寄存器：计数周期值

 重复计数器

 比较寄存器y(y=0..3)

 捕获寄存器y(y=0,1)

 置位/复位交叉开关

 空闲控制级

 通道输出级

19-10. Slave_TIMERx 显示了 Slave_TIMERx 的结构框图。


图 19-10. Slave_TIMERx 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/a919c1780bf79e2a05bdce8ae2f376d8c5ff08bbf6205c0001a061b3ac1ab4dc.jpg)



自动重载寄存器和比较 y（y = 0..3）寄存器具有以下限值：


当 CNTCKDIV[3:0] < 4’b0101 或 CNTCKDIV[3:0] = 4’b1000

 最小值必须大于或等于3个t<sub>SHRTIMER_CK</sub>周期对应的计数值；

 最大值必须小于或等于（0xFFFF – 1个t<sub>SHRTIMER_CK</sub>周期对应的计数值）。

注意：每个 t<sub>SHRTIMER_CK</sub> 周期对应的计数值 = f<sub>SHRTIMER_PSSCK</sub> / f<sub>SHRTIMER_CK</sub>。

$$
\text {当} \mathrm{CNTCKDIV} [ 3: 0 ] > = 4 ^ {\prime} \mathrm{b} 0 1 0 1 (\text {不包括} \mathrm{CNTCKDIV} [ 3: 0 ] = 4 ^ {\prime} \mathrm{b} 1 0 0 0)
$$

 最小值必须大于或等于0x0003；

 最大值必须小于或等于0xFFFE。

具体请见 19-1. y $\textcircled { y = 0 . . 3 }$ 寄存器的限值

计数器和捕获 ${ \tt y } \left( { \tt y } = 0 , 1 \right)$ 寄存器还具有以下限制：对于计数器时钟分频低于 64（CNTCKDIV[3：0] <5），最低有效位忽略。它们不能进行写操作和读操作时值为零。详见 19-4.y(y=0,1) 。


表 19-4. 计数器和捕获 y(y=0,1)寄存器限值


<table><tr><td>CNTCKDIV[3:0]</td><td>无效位</td></tr><tr><td>4&#x27;b1000</td><td>位 5~位 0</td></tr><tr><td>4&#x27;b0000</td><td>位 4~位 0</td></tr><tr><td>4&#x27;b0001</td><td>位 3~位 0</td></tr><tr><td>4&#x27;b0010</td><td>位 2~位 0</td></tr><tr><td>4&#x27;b0011</td><td>位 1~位 0</td></tr><tr><td>4&#x27;b0100</td><td>位 0</td></tr><tr><td>4&#x27;b0101</td><td>x</td></tr><tr><td>4&#x27;b0110</td><td>x</td></tr><tr><td>4&#x27;b0111</td><td>x</td></tr></table>


注意： $\ " { \bf { x } } \warrow$ 表示所有位都有效。


## 计数器时钟

Slave_TIMER 的时钟源可以有两个，分别是由 RCU 模块提供的 CK_APB2 和 CK_SYS。如果用户选择使用 CK_APB2 产生 SHRTIMER_CK，需要注意 SHRTIMER_STxCTL0 寄存器中的 CNTCKDIV[2:0]值必须大于或等于 5（预分频比大于或等于 64）；DLL 用于产生超高分辨率时钟 SHRTIMER_HPCK（f<sub>SHRTIMER_HPCK</sub> = 64 * f<sub>SHRTIMER_CK</sub>），此时 SHRTIMER_CK 必须由CK_SYS产生，更多信息请参考 DLL 。

当 SHRTIMER_STxACTL 寄存器中的 CNTCKDIV[3]位为 0 时，预分频器（PSC）将超高分辨率 时 钟 （ SHRTIMER_HPCK ） 除 以 分 频 因 子 2CNTCKDIV[2:0]+1 ， 得 到 计 数 器 时 钟（SHRTIMER_PSCCK）。该分频因子由 SHRTIMER_STxCTL0 寄存器中的 CNTCKDIV[2:0]位域控制。它们之间的频率关系可以表示如下：

$$
f _ {\text { SHRTIMER\_PSCCK }} = f _ {\text { SHRTIMER\_HPCK }} / 2 ^ {\text { CNTCKDIV[2:0]+1}}\tag{19-3}
$$

当 SHRTIMER_STxACTL 寄存器中的 CNTCKDIV[3]位为 1 时，只能将 CNTCKDIV[2:0]位配置为3’b000，并且SHRTIMER_PSCCK和SHRTIMER_HPCK之间的频率关系可以表示为：

$$
\mathsf {f} _ {\text { SHRTIMER\_PSCCK }} = \mathsf {f} _ {\text { SHRTIMER\_HPCK }}\tag{19-4}
$$

注意：一旦 Slave_TIMERx 使能了，就不能修改时钟分频 CNTCKDIV[3:0]的值。其中，CNTCKDIV[3] 位 在 SHRTIMER_STxACTL 寄 存 器 中 ， CNTCKDIV[2:0] 在SHRTIMER_STxCTL0 寄存器中。

参考 19-3. 32 和 19-2. fSHRTIMER = 180MHz 可得更多细节。

## 向上计数模式

计数器从 0 连续递增到计数器重载值，该值在 SHRTIMER_STxCAR 寄存器中定义。计数器有两种工作模式：单脉冲模式（SHRTIMER_STxCTL0 寄存器中的 CTNM = 0）和连续模式（SHRTIMER_STxCTL0 寄存器中的 CTNM = 1）。

在单脉冲模式下，将 SHRTIMER_MTCTL0 寄存器中的 STxCEN 位置 1 后，第一个复位事件将启动计数器。当计数到计数器重载值时，计数器停止并生成周期事件。然后，其他的复位事件将复位并重新启动计数器。在计数过程中，如果 SHRTIMER_STxCTL0 寄存器中的CNTRSTM = 1，则复位事件将复位并重新启动计数器，否则将被忽略。 19-4.显示了单脉冲模式下的计数器运行情况。

在连续模式下，一旦 SHRTIMER_MTCTL0 寄存器中的 STxCEN 位置 1，计数器将立即启动。当计数到计数器重载值时，计数器从 重新启动，并产生翻转事件。与单脉冲模式不同，随时生成的复位事件将复位并重启计数器。 19-5. 显示了连续模式下的计数器运行情况。

## 重复计数器

SHRTIMER_MTCTL0 寄 存 器 中 的 STxCEN 位 置 1 时 ， 重 复 计 数 器 将 加 载SHRTIMER_STxCREP寄存器的值。当由于复位事件或连续模式下的翻转事件清零计数器时，重复计数器值递减。当重复计数器值达到零时，复位事件或连续模式下的翻转事件将产生一个重复事件并重新加载 SHRTIMER_STxCREP 寄存器的值。

重复事件会将 SHRTIMER_STxINTF 寄存器中的 REPIF 位置 1，如果使能了相应中断或 DMA请求（SHRTIMER_STxDMAINTEN 寄存器中的 REPIE = 1 或 REPDEN = 1），则会产生重复中断和 DMA 请求。可以通过向 SHRTIMER_STxINTFC 寄存器中的 REPIFC 位写 1，清除重复中断标志。

连续模式下重复计数器的运行情况如 19-6. 所示。

单脉冲模式下，CNTRSTM = 0 时重复计数器的运行情况如 19-7. CNTRSTM=0时重复计数器的动作所示。

单脉冲模式下，CNTRSTM = 1 时重复计数器的运行情况如 19-8. CNTRSTM=1时重复计数器的动作所示。

## 计数器复位

计数器可以通过以下三种信号源复位：

1.软件。软件写 1 到 SHRTIMER_CTL1 寄存器的 STxSRST 位。

2.同步输入启动/复位计数器。

3.SHRTIMER_STxCNTRST 寄存器中配置的事件。

所有这些源都是逻辑或，它们可以同时有效。如果在同一 t<sub>SHRTIMER_CK</sub> 周期中发生多个复位事件，则仅最后一个有效。

注意：如果外部事件配置为电平有效，则只能在 SHRTIMER_STxCNTRST 寄存器中启用一个外部事件。

写 1 到 STxSRST 位（由硬件自动清除）使计数器复位。Master_TIMER 和 Slave_TIMERx（x= 0..4）的这些控制位都在 SHRTIMER_CTL1 寄存器中，可以同时复位多个计数器。

当 SHRTIMER_STxCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以复位计数器。请参考 。

可以在 SHRTIMER_STxCNTRST 寄存器中同时配置 30 个事件来复位计数器，这些事件可以分为四类：

 Slave_TIMERx：更新事件，比较1事件和比较3事件；

 其他Slave_TIMERy（例如x = 1，则 $y = 0 , \ 2 . . 4 )$ ：比较0事件，比较1事件和比较3事件；

 Master_TIMER：比较0事件，比较1事件，比较2事件，比较3事件和复位事件；

 外部事件y $( \mathsf { y } = 0 . . 9 )$ ：EXEVy为Slave_TIMERx中的外部事件的滤波信号。

当计数器时钟 SHRTIMER_PSCCK 的预分频系数大于 64（CNTCKDIV [3]=1’b0，且CNTCKDIV [2:0] > 3’b101）时，计数器复位事件将延迟到 SHRTIMER_PSCCK 的下一个上升沿。具体请见 19-9. 128 。

计数器复位事件会将 SHRTIMER_STxINTF 寄存器中的 RSTIF 位置 1，如果使能了计数器复位中断或 DMA 请求（SHRTIMER_STxDMAINTEN 寄存器中的 RSTIE = 1 或 RSTDEN = 1），则会产生复位中断或 DMA 请求。可通过向 SHRTIMER_STxINTFC 中的 RSTIFC 位写 1，清除复位中断标志。

## 捕获

捕获功能不仅使 Slave_TIMERx 实现了脉冲宽度，频率，周期，占空比的测量，而且还可以在延迟模式下（参见 ）更新比较 1 寄存器和比较 3 寄存器的值。

当选定的触发信号发生时，计数器的当前值被捕获到 SHRTIMER_STxCAPyV（y = 0,1）寄存器 中 。 同 时 ，SHRTIMER_STxINTF 寄 存 器 中 的 CAPyIF $( \textsf { y } = \textsf { 0 } , 1 \ )$ 位 置 1， 如 果SHRTIMER_STxDMAINTEN 寄存器中的 CAPyIE $( \mathsf { y } = 0 , 1 ) = 1$ 或 CAPyDEN $( \mathsf { y } = 0 , 1 ) =$ 1，则生成相应的捕获中断和 DMA 请求。可以通过写 1 到 SHRTIMER_STxINTFC 寄存器中的 CAPyIFC 位来清除捕获中断标志位 CAPyIF。

捕获 0 触发事件在 SHRTIMER_STxCAP0TRG 寄存器中定义，捕获 1 触发事件在SHRTIMER_STxCAP1TRG 寄存器中定义。当选择了多个触发事件时，所有的触发事件是逻辑“或”运算的。

注意：如果将外部事件配置为具有电平有效，则只能在 SHRTIMER_STxCAP0TRG 和

SHRTIMER_STxCAP1TRG 寄存器中使能一个外部事件。

捕获溢出是无法防止的，即使先前的捕获值未读取或捕获标志未清除，新的捕获仍将被触发，并且新的捕获值将覆盖先前的值。请参考 19-11. EXEV0 EXEV1 0。


图 19-11. EXEV0 和 EXEV1 触发捕获 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/223430240e9251685671e30a2e1f06d00282d66fa39342fe2ac38d6a44c3e131.jpg)


## 比较

Slave_TIMERx 单元有四个比较寄存器：SHRTIMER_STxCMPyV（y = 0..3）。当计数器值与比较寄存器值匹配时，将产生一个比较事件。具体请见 19-12. STxCAR=0x8,STxCMP1V=0x02 1 。

比较事件会将相应的比较中断标志位置 1（SHRTIMER_STxINTF 中的 CMPyIF 位，其中 y =0..3），如果使能了比较中断或 DMA 请求（SHRTIMER_STxDMAINTEN 寄存器中的 CMPyIE= 1 或 CMPyDEN = 1，其中 y = 0..3），则会生成比较中断或 DMA 请求。通过写 1 到SHRTIMER_STxINTFC 中的 CMPyIF 位可以清除比较中断标志。


图 19-12. STxCAR=0x8, STxCMP1V=0x02 时，比较 1 寄存器的动作


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/9d7daaab26c541e45e2c8fd16f74cf5b3e1fff3e3a2088fe44208dd49b97b3a0.jpg)


## 半波模式

当 SHRTIMER_MTCTL0 中的 HALFM 位置 1 时，半波模式使能。此模式将比较 0 有效寄存器的值强制为计数器重载值的一半，但 SHRTIMER_MTCMP0V 寄存器的值不会更新为（SHRTIMER_MTCAR / 2）的值。半波模式主要用于生成固定占空比为 50％的方波。

当 SHRTIMER_MTCTL0 寄存器中的 SHWEN 位置 1 时，将使能影子寄存器，比较 0 有效寄存器的值在更新事件时刷新。反之，比较 0 有效寄存器在新值写入 SHRTIMER_MTCAR 后立即刷新。

## 比较延迟模式

此模式仅用于比较（y y = 1,3）寄存器，并由 SHRTIMER_STxCTL0寄存器中的 DELCMPyM[1:0]位域控制。比较寄存器与计数器比较的实际值是重新计算值，该值在捕获 0/1 触发或比较 0/ 2事件之后重新计算得到，具体如 19-13. 。此模式允许通过硬件将生成的波形与捕获触发同步。


图 19-13. 比较延迟模式框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/3cccbd9022852b8dd1a8fdf4668fcba0aa331cd1ef7d501e8edcb8f70624c3e9.jpg)


在延迟模式下，比较 y（y = 1，3）事件从相应的捕获/比较事件发生到周期事件期间有效。当计数器达到周期值时，将禁用比较 y（y = 1，3）事件，直到出现新的捕获/比较事件。

当没有捕获触发或比较事件发生时，不生成比较 y事件。捕获触发事件发生后，将比较 y有效寄存器中的值与对应的 SHRTIMER_STxCAP0V 或 SHRTIMER_STxCAP1V 寄存器值相加，然后将其与计数器进行比较。比较 1 寄存器与捕获 0 寄存器和比较 0 寄存器/比较 2 寄存器关联，而比较 3 寄存器与捕获 1 寄存器和比较 0 寄存器/比较 2 寄存器关联。

注意：重新计算的值被传输到一个内部寄存器，且无法读取。

SHRTIMER_STxCTL0 寄存器中的 DELCMP1M[1:0]位域（比较 1 事件）和 DELCMP3M[1:0]位域（比较 3 事件）可用于配置延迟模式。下面以 DELCMP1M[1:0]为例：

 2’b00，比较1延迟模式禁能

比较 1 延迟模式禁用。一旦计数器值等于比较 1 寄存器的值，就会发生比较匹配。参见 19-12.STxCAR=0x8, STxCMP1V=0x02 1 。

 2’b01，比较1延迟模式0

捕获 0 事件发生后，将重新计算比较 1 寄存器的值（比较 1 有效寄存器值+捕获 0 寄存器值）。一旦计数器值等于重新计算后的比较 1 寄存器值，就会发生比较 1 事件。参见 19-14.1 0。


图 19-14. 比较 1 延迟模式 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/9bc2b4dae64c4417cb99e91818429b2812b98d8cfe7963c9e58361c83e2fcaf8.jpg)



 2’b10，比较1延迟模式1


在捕获 0 事件或比较 0 事件之后，将重新计算比较 1 寄存器的值。

发生捕获 0 事件时，比较 1 寄存器的重新计算值 = 比较 1 有效寄存器值 + 捕获 0 事件的捕获值。

发生比较 0 事件时，比较 1 寄存器的重新计算值 = 比较 1 有效寄存器值 + 比较 0 有效寄存器值。

一旦计数器值等于重新计算的比较 1 寄存器值，就会发生比较 1 事件。如果捕获 0 事件先发生，则比较 0 事件将被忽略。同样，如果先发生比较 0 事件，则将忽略捕获 0 事件。详情请见19-15. 1 1。


图 19-15. 比较 1 延迟模式 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/99c47c9b3d3a933d509148c84f7178b39b54c5123f106fec03cf18579fc597a7.jpg)



 2’b11，比较1延迟模式2


该模式与比较 1 延迟模式 1 相同。在捕获 0 事件或比较 2 事件之后，重新计算比较 1 寄存器的值。

发生捕获 0 事件时，比较 1 寄存器的重新计算值 = 比较 1 有效寄存器值 + 捕获 0 事件的捕获值。

发生比较 2 事件时，比较 1 寄存器的重新计算值 = 比较 1 有效寄存器值 + 比较 2 有效寄存器值。

一旦计数器值等于重新计算的比较 1 寄存器值，就会发生比较 1 事件。如果捕获 0 事件先发生，则比较 2 事件将被忽略。同样，如果先发生比较 2 事件，则将忽略捕获 0 事件。详见19-15. 1 1。

影子寄存器（SHWEN = 0）禁能时，即使在发生捕获事件后修改 SHRTIMER_STxCMP0V 位或 SHRTIMER_STxCMP2V 位的值，新的比较值也会立即被带入有效寄存器。 19-16.SHWEN=0 显示了一个示例：

在t0处发生捕获事件，C1值被捕获到寄存器中，重新计算的值 = 比较有效寄存器的值 + C1。在 t1 处将新的比较值（C2）写入比较寄存器，则重新计算的值 = C2 + C1。


图 19-16.比较延迟模式（SHWEN=0）


<table><tr><td colspan="5">MTCEN或STxCEN(x=0..4)</td></tr><tr><td colspan="5">(前值+C1)</td></tr><tr><td colspan="5">(C2+C1)</td></tr><tr><td colspan="2">CounterCTNM=1</td><td colspan="2">预装载值=前值有效值=C1</td><td>更新事件</td></tr><tr><td colspan="2">捕获事件</td><td colspan="2"></td><td></td></tr><tr><td>捕获寄存器</td><td>前值</td><td colspan="2">C1</td><td></td></tr><tr><td>比较寄存器</td><td>前值</td><td colspan="2">预装载值=前值有效值=C1</td><td>预装载值=C2有效值=C2重计算值=C2+C1</td></tr><tr><td>比较事件</td><td></td><td>t0</td><td>t1</td><td></td></tr></table>

使用延迟模式（DELCMP3M [1:0] = 01，10,11），可以防止捕获溢出发生。在同一个计数周期（由 SHRTIMER_STxCAR 确定）内，仅考虑第一个捕获事件。新的捕获事件在以下三种情况下有效：

 当比较寄存器的重新计算值与计数器值匹配时；

 发生了周期事件；

 计数器复位。

## 置位/复位交叉开关

通道输出波形功能由三个部分实现：

 置位/复位交叉开关

 空闲控制

 通道输出级

19-17. 显示了这三个部分的结构。


图 19-17. 通道输出结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/6eea43b688466ef4d70ac93e6236ba5c186256d4caa12ddd3222c2c70cff64bf.jpg)


交叉开关模块有三种输出模式：常规模式，死区时间模式和均衡模式，输出时只能选择其中一种模式。

## 输出准备信号

Slave_TIMERx 有一个置位/复位输出模块。该模块可以生成两个输出准备信号：O0PRE 和O1PRE。其中，O0PRE 由 SHRTIMER_STxCH0SET 和 SHRTIMER_STxCH0RST 寄存器控制。O1PRE 由 SHRTIMER_STxCH1SET 和 SHRTIMER_STxCH1RST 寄存器控制。OyPRE（y = 0,1）的高电平为有效电平，低电平为无效电平。

当 SHRTIMER_STxCHySET 寄存器中配置的事件发生时，此模块将产生置位请求，并使OyPRE 输出高电平。当 SHRTIMER_STxCHyRST 寄存器中配置的事件发生时，此模块会产生 复 位 请 求 ， 并 使 OyPRE 输 出 低 电 平 。 如 果 在 SHRTIMER_STxCHySET 和SHRTIMER_STxCHyRST 寄存器中配置了相同的事件，则此模块会生成输出翻转请求，并在配置的事件发生时使 OyPRE 输出翻转。

注意：如果 SHRTIMER_STxCTL0 和 SHRTIMER_STxACTL 寄存器中的 CNTCKDIV[3:0]位域 等 于 4’b0110 或 4’b0111 ， 则 不 得 同 时 设 置 SHRTIMER_STxCH0SET 和SHRTIMER_STxCH0RST 寄存器中的同一事件。

19-18. O0PRE CMP0 CMP1 显示了以下配置时的O0PRE输出波形：

 SHRTIMER_STxCTL0寄存器中的CNTCKDIV [2:0] = 3’b000；

SHRTIMER_STxCH0SET= 0x0000 0008：比较0事件产生置位请求，O0PRE将输出高电平；

 SHRTIMER_STxCH0RST= 0x0000 0010：比较1事件产生复位请求，O0PRE将输出低电平；

 SHRTIMER_STxCMP0V = 0x00A0； 

 SHRTIMER_STxCMP1V = 0x01C0。 


图 19-18. O0PRE 波形：CMP0 事件置位，CMP1 事件复位


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/5c9cdf3fe0ca93caf26e1834daa3ab9bfa594c7409e5b98582aacb11b3ffe315.jpg)


OyPRE（y = 0,1）最多可以选择 32 个事件：

 Slave_TIMERx：更新事件，复位事件，周期事件和比较y（y = 0..3）事件；

 Master_TIMER：周期事件，比较y（y = 0..3）事件；

Slave_TIMERx互连事件：其他Slave_TIMERy有9个互连事件（例如x = 1，然后y = 0，2..4）,参见 19-5. Slave_TIMER ；

 外部事件y（y = 0..9）：EXEVy为Slave_TIMERx中的外部事件的滤波信号；

 软件事件。

无论 STxCEN 位是否为 1，软件事件始终有效。但是，只有 STxCEN 为 1 时，才会考虑其他事件。


表 19-5. Slave_TIMER 内部连接事件


<table><tr><td rowspan="2">内部连接</td><td colspan="4">来自ST0</td><td colspan="4">来自ST1</td><td colspan="4">来自ST2</td><td colspan="4">来自ST3</td><td colspan="4">来自ST4</td></tr><tr><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td><td>CMP0</td><td>CMP1</td><td>CMP2</td><td>CMP3</td></tr><tr><td>到ST0</td><td>x</td><td>x</td><td>x</td><td>x</td><td>0</td><td>1</td><td>x</td><td>2</td><td>x</td><td>3</td><td>x</td><td>x</td><td>5</td><td>6</td><td>x</td><td>x</td><td>x</td><td>x</td><td>7</td><td>8</td></tr><tr><td>到ST1</td><td>0</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>3</td><td>4</td><td>x</td><td>x</td><td>5</td><td>6</td><td>7</td><td>x</td><td>x</td><td>x</td></tr><tr><td>到ST2</td><td>x</td><td>x</td><td>1</td><td>x</td><td>x</td><td>2</td><td>3</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>4</td><td>x</td><td>5</td><td>x</td><td>6</td><td>7</td><td>8</td></tr><tr><td>到ST3</td><td>0</td><td>x</td><td>x</td><td>1</td><td>x</td><td>2</td><td>x</td><td>3</td><td>4</td><td>x</td><td>5</td><td>6</td><td>x</td><td>x</td><td>x</td><td>x</td><td>7</td><td>x</td><td>x</td><td>8</td></tr><tr><td>到ST4</td><td>x</td><td>x</td><td>0</td><td>1</td><td>x</td><td>x</td><td>2</td><td>3</td><td>4</td><td>5</td><td>x</td><td>x</td><td>6</td><td>7</td><td>x</td><td>8</td><td>x</td><td>x</td><td>x</td><td>x</td></tr></table>


注意：（1）表中的数字表示 Slave_TIMERx 互连事件。


（2）“x”代表无效。

可以同时选择多个事件源（进行逻辑或运算），并且当它们在同一 t<sub>HPTMER_CK</sub>周期内发生时，将执行仲裁。

## 仲裁机制

当 SHRTIMER_STxCH1SET 和 SHRTIMER_STxCH1RST 寄存器中配置的多个事件发生在同一个 t<sub>HPTMER_CK</sub>周期内时，将执行仲裁过程，且只有一个事件有效，可以更改 OyPRE（y =0,1）的输出。

这 32 个事件可以分为四种类型：

 Slave_TIMERx：比较y（y = 0..3）事件，周期事件。

 Master_TIMER：比较y（y = 0..3）事件，周期事件。

 Slave_TIMERx互连事件：互连事件y（y = 0..8）

低精度事件：Slave_TIMERx的更新事件和复位事件，外部事件 $( \mathsf { y } = 0 . . 9 )$ ，软件事件。具体的仲裁过程 19-19. tSHRTMER<sub>_CK</sub> 所示。


图 19-19. 每个 t<sub>SHRTMER_CK</sub> 周期的仲裁机制过程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/8877dd9b57fe8fd74c74f805acdfc82bafc268a663f137de9af70decc43b3459.jpg)


三个仲裁器的功能如下：

 仲裁器 0 的优先级顺序（从最高优先级到最低优先级）：

比较 3 事件 > 比较 2 事件 > 比较 1 事件 > 比较 0 事件 > 周期事件。

 仲裁器 1 根据事件在 t<sub>HPTMER_CK</sub>期间的延迟来仲裁优先级：

延迟越小，优先级越高。

 仲裁器 2 根据事件对 OyPRE（y = 0,1）输出的影响来仲裁优先级：

复位请求 > 输出翻转请求 > 置位请求。

以 Slave_TIMER0 中的 O0PRE 输出为例，配置如下：

 SHRTIMER_STxCH0SET = 0x0060 5898，选定产生置位请求的事件是：

Master_TIMER：比较 2 事件，周期事件；

Slave_TIMER0：比较 1 事件，比较 0 事件；

Slave_TIMER0 的互连事件：互连事件 0（Slave_TIMER1 比较 0 事件），互连事件 2（Slave_TIMER1 比较 3 事件）；

低精度事件：外部事件 0（EXEV0），外部事件 1（EXEV1）。

 SHRTIMER_STxCH0RST = 0x0198 0344，选定产生置位请求的事件是：

Master_TIMER：比较 0 事件，比较 1 事件；

Slave_TIMER0：比较 3 事件，周期事件；

Slave_TIMER0 的互连事件：互连事件 7（Slave_TIMER4 比较 2 事件），互连事件 8（Slave_TIMER4 比较 3 事件）；

低精度事件：外部事件 2（EXEV2），外部事件 3（EXEV3）。

 延迟：Slave_TIMER4 比较 $3 < \mathsf { S l a v e \_ T I M E R 0 }$ 比较 3

上述选定的事件如果在同一个 t 周期内发生，则仲裁过程和结果如 19-20.所示。最终，Slave_TIMER4 比较 3 事件产生的复位请求在该 t 期间有效，并且 O0PRE 将被设置为低电平。


图 19-20. 仲裁机制示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/33363769e51466e2b60f0b6131191010cb763bdda269a9a9a409e7c74b9dec93.jpg)


## 输出准备信号：窄脉冲管理

当几个输出置位和/或复位请求在 3 个连续的 t<sub>SHRTMER_CK</sub>周期内发生时，OyPRE（y = 0,1）输出信号是一个窄脉冲。窄脉冲的输出管理由SHRTIMER_STxCTL0寄存器中的CNTCKDIV[3:0]位域配置，有以下两种情形：

 情形0： $\mathsf { C N T C K D I V } [ 3 ; 0 ] < 4 ^ { \prime } ~ \mathsf { b O 1 0 1 } \ni \mathsf { I \Xi } \mathsf { E N T C K D I V } [ 3 ; 0 ] = 4 ^ { \prime } ~ \mathsf { b } 1 0 0 0$ 

 情形1：CNTCKDIV[3:0] >= 4’b0101，CNTCKDIV[3] = 0

## 情形 0：CNTCKDIV[3:0] < 4’b0101 或 CNTCKDIV[3:0] = 4’b1000

如果输出置位和复位请求在两个连续的t<sub>SHRTMER_CK</sub>周期内产生，则会生成脉宽为1个t<sub>HPTMER_CK</sub>周期的脉冲。具体如 19-21. 1 tSHRTMER<sub>_CK</sub> 所示。


图 19-21. 脉冲宽度为 1 个 t<sub>SHRTMER_CK</sub> 周期


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/6a817d5ac3d4aca181e64a544550c96968224e83cbb725bf868891e5bd7e25ec.jpg)



如果输出置位和复位请求的时间间隔包括一个完整的 t<sub>SHRTMER_CK</sub> 周期，则会生成脉宽为 2 个t 周期的脉冲。具体如 19-22. 2 tSHRTMER 所示。



图 19-22.脉冲宽度为 2 个 t<sub>SHRTMER_CK</sub> 周期


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/3d09e8c6902e902ff4be7963f4783be5f9cdd9f398c1caa7e21041b64099fa98.jpg)



如果输出置位和复位请求的时间间隔大于两个完整的 t<sub>HPTMER_CK</sub>周期，则需要使用超高分辨率时钟。具体如 19-23. OxPRE 所示。



图 19-23. 超高分辨率 OxPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/3a2458d4d9fe643068f8f65d7e704c164a3a96cdfb463340be7def379223c7f4.jpg)



情形 1: CNTCKDIV[3:0] >= 4’b0101，CNTCKDIV[3] = 0



这种情况下，即使在每个 t<sub>SHRTIMER_CK</sub>周期内执行仲裁，发生在 1 个 SHRTIMER_PSCCK 周期


内的输出置位或复位请求，都会延迟到 SHRTIMER_PSCCK 时钟的下一个有效边沿。

当来自不同事件源的置位请求和复位请求在 1 个 t<sub>SHRTIMER_CK</sub>周期中同时发生时，复位请求具有最高优先级，详见 19-24. CNTCKDIV[3:0] = 4 b0110 OxPRE 。


图 19-24. CNTCKDIV[3:0] = 4’b0110 时的 OxPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/d98eac36f0acdffc9332cc0667622d2b83336e4a6d0723a87bd6de6f807f59ae.jpg)


## 常规模式

当 SHRTIMER_STxCHOCTL 寄存器中的 DTEN = 0，SHRTIMER_STxCTL0 寄存器中的BLNMEN = 0 时，置位/复位交叉开关以常规模式运行。

该模式中，C0OPRE和C1OPRE是独立的。C0OPRE（C1OPRE）直接连接到O0PRE（O1PRE）。当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，SHRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，SHRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0ONAIFC 位可以清除CH0ONAIF 中断标志。

通道 1 与通道 0 输出情况相同。

19-25. C0OPRE 显示了以下配置时的 C0OPRE 波形：

 SHRTIMER_STxCTL0寄存器中的CNTCKDIV[3:0] = 4’b0000；

 SHRTIMER_STxCH0SET = 0x0000 0008：比较0事件产生置位请求，O0PRE输出高电平；

 SHRTIMER_STxCH0RST = 0x0000 0010：比较1事件产生复位请求，O0PRE输出低电平；

 SHRTIMER $S \mathsf { T x C M P 0 V } = 0 { \times } 0 0 6 0$ ； 

 SHRTIMER $S \mathsf { T x C M P 1 V } = 0 { \times } 0 0 \mathsf { E 0 }$ 


图 19-25. 常规模式下的 C0OPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/c5a73a98701ca548a9f2739009a918f596ab85a2a6f314c77e9b6cff63e54a53.jpg)


## 死区时间模式

当 SHRTIMER_STxCHOCTL 寄存器中的 DTEN = 1，SHRTIMER_STxCTL0 寄存器中的BLNMEN = 0 时，置位/复位交叉开关在死区模式下运行。

死区模式中，只对 O0PRE 进行编程，以驱动 C0OPRE 和 C1OPRE 的输出。C0OPRE 和C1OPRE 是一对互补信号，在有效状态转换之间插入可编程的死区时间。

死区时间值是由 SHRTIMER_STxDTCTL 寄存器中的 DTFCFG [15:0]位域和 DTRCFG [15:0]位域确定的。DTFCFG [15:0]位域定义在 O0PRE 下降沿之后的死区时间，而 DTRCFG [15:0]位域定义在 O0PRE 上升沿之后的死区时间。

注意：DTFCFG [8:0]和 DTRCFG [8:0]位域在 SHRTIMER_STxDTCTL 寄存器中，DTFCFG[15:9]和 DTRCFG [15:9]位域在 SHRTIMER_STxACTL 寄存器中

死区时间值可以由 SHRTIMER_STxDTCTL 寄存器中的 DTRS 位和 DTFS 位配置为正或负。当需要某些波重叠时，可以定义负的死区时间值。

死区时间由 SHRTIMER_STxDTCTL 寄存器中的 DTGCKDIV [3:0]位域定义的时钟确定。

注意：DTGCKDIV[2:0]位域在 SHRTIMER_STxDTCTL 寄存器中，而 DTGCKDIV[3]位在SHRTIMER_STxACTL 寄存器中。

当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，SHRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，SHRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0ONAIFC 位可以清除CH0ONAIF 中断标志。

通道 1 与通道 0 输出情况相同。

19-26. C0OPRE C1OPRE 显示了 O0PRE 脉冲宽度大于死区时间时的 C0OPRE 和 C1OPRE 波形。


图 19-26. 具有死区时间的 C0OPRE 和 C1OPRE 互补输出波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/a0db84644f934921cda94982373424557a477f2bb171f62e03a6f594de707f93.jpg)



19-27. 显示了 O0PRE 脉冲宽度小于死区时间时的C0OPRE 和 C1OPRE 互补波形。



图 19-27. 脉宽小于死区时间时的互补波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/efd8a1eece2d81906136751d4ea06b82c2357eca4b40fe857468d5f9d429c2ca.jpg)


## 均衡模式

当 SHRTIMER_STxCHOCTL 寄存器中的 DTEN = 0，SHRTIMER_STxCTL0 寄存器中的BLNMEN = 1 时，置位/复位交叉开关在均衡模式下运行。当计数器在连续模式下运行时才能使用均衡模式，并且一旦使能了计数器就不得使其复位。

19-28. 显示了均衡模式的信号控制过程。


图 19-28. 均衡模式的结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/972ad379aa327e700baaba4befc3328db20e925c51c2de45730e613ecb0d202e.jpg)


一旦接收到翻转事件，翻转逻辑模块的输出就会翻转。当翻转逻辑模块的输出为 1（高电平）时，C0OPRE 连接到 O0PRE，C1OPRE 为无效电平（低电平）。当翻转逻辑模块的输出为 0（低电平）时，C1OPRE 连接到 O1PRE，C0OPRE 为无效电平（低电平）。

建议配置 SHRTIMER_STxCH0SET = SHRTIMER_STxCH1SET，SHRTIMER_STxCH0RST= SHRTIMER_STxCH1RST，实现相同波形的均衡操作。在进行其他应用时，也可以对两个输出进行不同的配置。

均衡模式禁能时，SHRTIMER_STxINTF 寄存器中的 CBLNF 位将复位，该位用于指示当前哪个通道正在输出信号（O0PRE 或 O1PRE）。

当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从无效状态变为有效状态时，SHRTIMER_STxINTF 寄存器中的 CH0OAIF 位将被设置为 1。如果使能了中断或 DMA请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0OAIE = 1 或 CH0OADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0OAIFC 位可以清除 CH0OAIF 中断标志。

当 Slave_TIMERx（x = 0..4）运行在 RUN 或 IDLE 状态下，C0OPRE 从有效状态变为无效状态时，SHRTIMER_STxINTF 寄存器中的 CH0ONAIF 位将置 1，如果使能了中断或 DMA 请求（SHRTIMER_STxDMAINTEN 寄存器中的 CH0ONAIE = 1 或 CH0ONADEN = 1），则产生相应的中断或 DMA 请求。通过将 1 写到 SHRTIMER_STxINTFC 中的 CH0ONAIFC 位可以清除CH0ONAIF 中断标志。

通道 1 与通道 0 输出情况相同。

19-29. C0OPRE C1OPRE 显示了以下配置时的 C0OPRE 和C1OPRE 波形：

 SHRTIMER_STxCH0SET = SHRTIMER_STxCH1SET = 0x0000 0004：周期事件产生置位请求，O0PRE和O1PRE输出高电平；

 SHRTIMER_STxCH0RST = SHRTIMER_STxCH1RST = 0x0000 0008：比较0事件产生复位请求，O0PRE和O1PRE输出低电平。


图 19-29. 均衡模式下的 C0OPRE 和 C1OPRE 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/dc828e484d35d0951ba0cfa6283453e6c3f4de8a46b506c8132fe9a8551afd03.jpg)


## 空闲控制

空闲控制级有三种控制空闲状态的方式：

 延迟空闲模式

 均衡空闲模式

 突发模式控制的空闲模式

延迟空闲和均衡空闲模式不能同时使用。均衡空闲仅在均衡模式下可用。延迟空闲或均衡空闲可以与突发模式控制的空闲模式同时使用，但突发模式的优先级最低。当置位/复位开关在不同模式下操作时，可以使用不同的空闲控制模式，详见 19-6. 。


表 19-6. 交叉开关和空闲控制同时运行


<table><tr><td>置位/复位交叉开关运行模式</td><td>IDLE 控制级运行模式</td></tr><tr><td>常规模式</td><td>延迟空闲,突发模式控制的空闲</td></tr><tr><td>死区时间模式</td><td>延迟空闲,突发模式控制的空闲</td></tr><tr><td>均衡模式</td><td>延迟空闲,均衡控制和突发模式控制空闲</td></tr></table>


SHRTIMER_STxINTF 寄存器中的 CHyF(y=0,1)位，指示了 CHyOPRE 的输出电平。


## 延迟空闲

在延迟空闲模式，所选外部事件（对于 Slave_TIMER0/ 1/ 2 为 EXEV5/ 6，对于 Slave_TIMER3/4 为 EXEV7/ 8）之后的置位请求或复位请求会导致 CHyOPRE（y = 0，1）输出进入空闲状态。具体情况与 SHRTIMER_STxCHOCTL 寄存器中的 ISOy/ CHyP（y = 0,1）有关，详见19-7. 。ISOy 位用于定义空闲状态时 CHyOPRE 的输出电平。空闲模式会永久保持，计数器将继续运行，直到重新使能输出才退出该模式。将 STxCH0EN 和STxCH1EN 位重新置 1 后，通过置位请求或复位请求可以重新使能延迟空闲模式。


表 19-7. 进入和退出空闲状态的请求


<table><tr><td>ISOy/CHyP (y=0,1)值</td><td>进入空闲状态的请求</td><td>退出空闲状态的请求</td></tr><tr><td>ISOy = 0CHyP = 0</td><td>复位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 1CHyP = 0</td><td>置位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 0CHyP = 1</td><td>置位请求</td><td>置位请求和复位请求</td></tr><tr><td>ISOy = 1CHyP = 1</td><td>复位请求</td><td>置位请求和复位请求</td></tr></table>

延迟空闲模式可以应用于单个输出（CHyOPRE）或两个输出（CH0OPRE 和 CH1OPRE）情况（由 SHRTIMER_STxCHOCTL 寄存器中的 DLYISCH[2:0]位域定义）：

 DLYISCH[2:0] = 3’b000：延迟空闲模式应用于CH0OPRE；

 DLYISCH[2:0] = 3’b001：延迟空闲模式应用于CH1OPRE；

 DLYISCH[2:0] = 3’b010：延迟空闲模式应用于CH0OPRE和CH1OPRE。

一旦选定的外部事件（EXEV5/ 6 或 EXEV7/ 8）到达，SHRTIMER_STxINTF 寄存器中的 DLYIIF位置 1，如果使能了相应的中断和 DMA（SHRTIMER_STxDMAINTEN 寄存器中的 DLYIIE =1 或 DLYIDEN = 1），则产生中断或 DMA 请求。通过写 1 到 SHRTIMER_STxINTFC 寄存器中的 DLYIIFC 位可以清除中断标志。

当选定的外部事件（EXEV5 / 6 或 EXEV7/ 8）触发延迟空闲模式时，SHRTIMER_STxINTF 寄

存器中的 CHyDLYF（y = 0,1）位可以指示 CHyOPRE 信号的状态。

下面四张图显示了延迟空闲模式中的 CH0OPRE 波形：

■ C0OPRE 运 行 在 常 规 模 式 ： SHRTIMER_STxCHOCTL 寄 存 器 中 的 DTEN = 0 ，SHRTIMER_STxCTL0寄存器中的BLNMEN = 0；

 比较0事件产生置位请求；

 比较1事件产生复位请求。


图 19-30. 延迟空闲模式，ISO0 = 0 和 CHOP = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/ccceef774a4539b8cc0bee97b1b0061dc7960d8e150e9cfe605de0719f779bb2.jpg)



图 19-31. 延迟空闲模式，ISO0 = 1 和 CHOP = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/2cb88703c403729fb0e75012fe503334454fae2d0db8b6e25abbf76b27f9e6c9.jpg)



图 19-32. 延迟空闲模式，ISO0 = 0 和 CHOP = 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/b69a5e0e18bb3bde54eb2fccea88c018c44e85924e84cd0c76039870a9ba6929.jpg)



图 19-33. 延迟空闲模式，ISO0 = 1 和 CHOP = 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/4640f81cd48610ad971454e02d647149a5ab46c25e66f39810e318eb700bd785.jpg)


## 均衡空闲

均衡空闲模式仅在均衡模式下可用。通过将 SHRTIMER_STxCHOCTL 寄存器的 DLYISCH[2:0]位域设为 3’bx11，使能均衡空闲模式。Slave_TIMER0/1/2 的外部事件 5/6（EXEV5/6）和Slave_TIMER3/4 的外部事件 7/8（EXEV7/8）可使用均衡空闲模式。

外部事件发生时，CHyOPRE（y = 0,1）进入空闲状态，并输出由 SHRTIMER_STxCHOCTL寄存器中的 ISOy 位定义的电平，且 SHRTIMER_STxINTF 寄存器中的 DLYIIF 位置 1。该外部事件触发捕获，将计数器值捕获到比较 3 有效寄存器中（该值用户不可访问）。均衡模式会再维持一个周期，使互补输出 CHzOPRE（z = 0，1 且 z≠y）可以重复 CHyOPRE 上的短脉冲： 19-34. ISO0 = 0 ISO1 = 0 显示了均衡空闲模式下 Slave_TIMER0的 CH0OPRE/ CH1OPRE 波形，配置如下：

■ C0OPRE 处 于 均 衡 模 式 ： SHRTIMER_STxCHOCTL 寄 存 器 中 的 DTEN = 0 ，SHRTIMER_STxCTL0寄存器中的BLNMEN = 1；

 比较0事件产生置位请求；

 比较1事件产生复位请求；

 在外部事件6发生时，通道0和通道1输出为均衡空闲模式：Slave_TIMER0的DLYISCH [2：0] = 111。


图 19-34. 均衡空闲模式，ISO0 = 0 和 ISO1 = 0


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/5b8437f3ac8726dea6f892cf0ce0735b75e4fa09a30236c8c0f35b6dcebbb3cf.jpg)


SHRTIMER_STxINTF 寄存器中的 BLNIF 位指示了发生均衡空闲模式时哪个通道正在输出信号。如 19-34. ISO0 = 0 ISO1 = 0，外部事件 6（EXEV6）到来时，通道0 输出信号，通道 1 输出无效，且 BLNIF 位复位为零。

在计数器继续运行时，IDLE 模式将永久保持，直到重新使能输出才退出均衡空闲模式。将STxCH0EN 和 STxCH1EN 位重新置 1 后，通过置位请求或复位请求可以重新使能均衡空闲模式。

在以下情况下，均衡空闲模式可以与突发模式一起使用：

■ BMSTx位必须复位（保持计数器时钟SHRTIMER_PSCCK，且计数器正常运行）；

 当输出配置为突发模式控制的空闲状态时，不会触发均衡空闲模式。

## 突发模式控制的空闲模式

在突发模式中，空闲状态由突发模式控制器控制。具体请参考 。

均衡空闲和延迟空闲的优先级高于突发模式：一旦触发均衡空闲和延迟空闲模式，任何突发模式的退出请求都将被丢弃。相反，如果在均衡空闲或延迟空闲退出时，突发模式仍有效，则突发模式将正常恢复。

突发模式控制器可以对任意两个输出 CHyOPRE（y = 0,1）进行控制。见 19-8.，SHRTIMER_STxCHOCTL 寄存器中的 ISOy 位和 BMCHyIEN（y =0,1）位可以对突发模式控制的空闲模式期间的每个输出的状态进行配置。


表 19-8. 突发模式控制的空闲状态时的输出


<table><tr><td>ISOy</td><td>BMCHyIEN</td><td>CHyOPRE (y=0,1)</td></tr><tr><td>x</td><td>0</td><td>无影响:输出不受突发模式控制器影响</td></tr><tr><td>0</td><td>1</td><td>在突发模式控制的空闲模式中输出复位电平</td></tr><tr><td>1</td><td>1</td><td>在突发模式控制的空闲模式中输出置位电平</td></tr></table>

## 通道输出级

每个 Slave_TIMERx 可以控制一对输出（STxCH0_O 和 ${ \mathsf { S T x C H 1 \_ O ) } }$ 。输出级由三种工作状态：

 运行状态： ${ \mathsf { S T x C H y \_ O } } \ ( \ y = 0 , 1 )$ 输出CHyOPRE（y = 0,1）的电平。

 空闲状态： ${ \mathsf { S T x C H y \_ O } } \ ( { \mathsf { y } } = 0 , 1 )$ 输出由SHRTIMER_STxCHOCTL寄存器中ISOy位定义的电平。

 故障状态：STxCHy_O（y = 0,1）可以永久有效，无效或Hi-Z（由SHRTIMER_STxCHOCTL寄存器的CHyFLTOS位定义）。详见 。

SHRTIMER_CHOUTEN 寄存器中的 STxCHyEN 位和 SHRTIMER_CHOUTDISF 寄存器中的STxCHyDISF 位可以指示输出的状态，如 19-9. $( x { = } 0 . . 4 , \ y { = } 0 , 1 )$ 所述。


表 19-9. 输出级状态编程（x=0..4, y=0,1）


<table><tr><td>STxCHyEN</td><td>STxCHyDISF</td><td>输出级状态</td></tr><tr><td>1</td><td>x</td><td>运行状态</td></tr><tr><td>0</td><td>0</td><td>空闲状态</td></tr><tr><td>0</td><td>1</td><td>故障状态</td></tr></table>

将 SHRTIMER_CHOUTDIS 寄存器中的 STxCHyDIS 位置 1，输出禁能，并使输出进入空闲状态。三种工作状态的优先级顺序为：空闲状态 > 故障状态 > 运行状态。

SHRTIMER_STxCHOCTL 寄存器中的 CHyP 位可以设置输出极性。当 ${ \mathsf { C H y P } } = 0$ 时，输出极性为高电平有效。当 CHyP = 1 时，输出极性为低电平有效。详见 19-35. CHyP=0 CHyP=1STxCHy_O 。


图 19-35. CHyP=0 或 CHyP=1 时的 STxCHy_O 波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/1f3b95e8d6df8956a343d71c81263bdb92d63520034ce6710937f5393ed03233.jpg)


使用 SHRTIMER_STxCHOCTL 寄存器中的 CHyFLTOS [1:0]位域可以配置故障状态下的输出电平，如下所示：

 $_ { 2 } \cdot$ b00：输出永远不会进入故障状态，并保持运行或空闲状态；

 $_ { 2 } \cdot$ b01：故障状态时，输出有效电平；

 $_ { 2 } \cdot$ b10：故障状态时，输出无效电平；

 $_ { 2 } \cdot$ b11：故障状态时，输出为三态。

使用 SHRTIMER_STxCHOCTL 寄存器中的 ISOy位配置处于空闲状态的输出电平，如下：

 $_ { 2 } \cdot$ b0：空闲状态时，输出无效电平；

 $_ { 2 } \cdot$ b1：空闲状态时，输出有效电平。

## 载波信号模式

可以在OyPRE(y=0,1)信号顶部添加一个高频载波信号，如 19-36. 所示。


图 19-36. 载波信号结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/5078be4fb92a2dedf8a087eb4bfbacf3b9cd0ca31f51ec5bbfc7cbb377186e18.jpg)


载波信号模式中，可以在载波信号开始之前定义一个特定的脉冲宽度。载波信号的频率和占空比是可配置的。详见 19-37. SHRTIMER 。

将 SHRTIMER_STxCHOCTL 寄存器中的 CH0CSEN 和 CH1CSEN 位置 1，可以分别在通道0 和 1 上使能载波信号模式。

第一个脉冲的脉冲宽度由 SHRTIMER_STxCSCTL 寄存器中的 CSFSTPW [3:0]位域配置，公式如下：

$$
t _ {\text { CSFSTPW }} = (\text { CSFSTPW } [ 3: 0 ] + 1) ^ {*} t _ {\text { SHRTIMER\_CSGCK }}, \text { 其中 } t _ {\text { SHRTIMER\_CSGCK }} = 1 6 ^ {*} t _ {\text { SHRTIMER\_CK }}
$$

载波信号的频率由 SHRTIMER_STxCSCTL 寄存器中的 CSPRD [3:0]位域配置，公式如下：

$$
t _ {\text { CSPRD }} = (\text { CSPRD } [ 3: 0 ] + 1) ^ {*} t _ {\text { SHRTIMER\_CSGCK }}, \text { 其中 } t _ {\text { SHRTIMER\_CSGCK }} = 1 6 ^ {*} t _ {\text { SHRTIMER\_CK }}
$$

载波信号的占空比由 SHRTIMER_STxCSCTL 寄存器中的 CSDTY[2:0]位域配置，步长为12.5％。

载波信号模式中，载波信号发生器的输出与 OyPRE 逻辑与运算后输出。OyPRE（y = 0,1）输出无效时，载波信号会立即停止，即使当前的载波周期未完成。具体请参考 19-37.SHRTIMER 。


图 19-37. 载波模式使能时的 SHRTIMER 输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/ea4bd8308c9bda2a659520afbb39819c532681f16db98f84eccd6bb140e6b135.jpg)


## 同步输入启动/复位计数器

当 SHRTIMER_MTCTL0 寄存器中的 SYNIRST 位置 1 时，同步输入可以产生计数器复位事件；当 SHRTIMER_MTCTL0 寄存器中的 SYNISTRT 位置 1 时，同步输入可以启动计数器。详见 。

同步输入请求会将 SHRTIMER_MTINTF 寄存器中的 SYNIIF 位置 1，如果使能了中断或 DMA请求（SHRTIMER_MTDMAINTEN 寄存器中的 SYNIIE = 1 或 SYNIDEN = 1），会产生相应的中断或 DMA 请求。可以通过写 1 到 SHRTIMER_MTINTFC 寄存器中的 SYNIIFC 位，来清除同步输入中断标志。

## 更新事件和影子寄存器

Slave_TIMERx 中的某些寄存器具有影子寄存器。MCU 复位后，影子寄存器被禁能。如果将SHRTIMER_STxCTL0 寄存器中的 SHWEN 位清 0，则禁能影子寄存器。写入这些寄存器的值

将立即转移到有效寄存器中并生效。

如果 SHRTIMER_STxCTL0 寄存器中的 SHWEN 位置 1，则使能影子寄存器， 19-10.Slave_TIMERx 中列出的寄存器被预加载。写入这些寄存器的值将被传送到影子寄存器，且不会立即生效。当发生更新事件时，影子寄存器内容将转移到有效寄存器中并立即生效。

注意：当 SHWEN=1 时，才会产生更新事件。

19-10. Slave_TIMERx 列出了具有影子寄存器的寄存器和相应的更新事件。


表 19-10. Slave_TIMERx 影子寄存器和更新事件


<table><tr><td>具有影子寄存器的寄存器</td><td>影子寄存器使能位</td><td>更新事件</td></tr><tr><td>SHRTIMER_STxDMAINTEN</td><td rowspan="15">SHRTIMER_STxCTL0寄存器中的SHWEN位</td><td>软件(STxSUP位)</td></tr><tr><td>SHRTIMER_STxCAR</td><td>重复事件(UPREP=1)</td></tr><tr><td>SHRTIMER_STxCREP</td><td>计数器复位或翻转事件(UPRST=1)</td></tr><tr><td>SHRTIMER_STxCMP0V</td><td>来自其他定时器的更新事件(Slave_TIMERx是UPBSTX,Master_TIMER是UPBMT)</td></tr><tr><td>SHRTIMER_STxCMP0CP</td><td rowspan="3">DMA模式结束事件(UPSEL[3:0]=4&#x27;b0001)</td></tr><tr><td>SHRTIMER_STxCMP1V</td></tr><tr><td>SHRTIMER_STxCMP2V</td></tr><tr><td>SHRTIMER_STxCMP3V</td><td rowspan="3">DMA模式结束事件之后的更新事件(UPSEL[3:0]=4&#x27;b0010)</td></tr><tr><td>SHRTIMER_STxDTCTL</td></tr><tr><td>SHRTIMER_STxCH0SET</td></tr><tr><td>SHRTIMER_STxCH0RST</td><td rowspan="2">STxUPINy(y=0..2)的上升沿产生更新事件</td></tr><tr><td>SHRTIMER_STxCH1SET</td></tr><tr><td>SHRTIMER_STxCH1RST</td><td rowspan="3">STxUPINy(y=0..2)的上升沿之后产生更新事件</td></tr><tr><td>SHRTIMER_STxCNTRST</td></tr><tr><td>SHRTIMER_STxACTL寄存器中的DTFCFG[15:9]和DTRCFG[15:9]</td></tr></table>


更新使能输入 STxUPINy（y = 0..2）是来自通用定时器的芯片内部信号，上升沿有效。具体请见 19-11. STxUPINy y=0..2 。



表 19-11. STxUPINy（y=0..2）和芯片内部信号


<table><tr><td>更新使能输入 STxUPINy (y = 0..2)</td><td>芯片内部信号</td></tr><tr><td>STxUPIN0</td><td>保留</td></tr><tr><td>STxUPIN1</td><td>保留</td></tr><tr><td>STxUPIN2</td><td>TIMER5_TRGO</td></tr></table>

## 外部事件滤波

外部事件 EXEVyC（y = 0..9）在指定时间内被滤波，有两种滤波模式：

 消隐模式：在指定时间内发生的外部事件被忽略；

 窗口模式：在指定时间内发生的外部事件有效。

具体请见 19-38. 。


图 19-38. 消隐模式和窗口模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/23d44c3537d844e5758c9e72039a7d42a21a75d15e04ad22b84c7a55219a4ff7.jpg)



参考 章节可得更多关于外部事件 EXEVyC(y=0..9)的信息。


## 消隐模式

消隐模式中，在指定时间内发生的外部事件 EXEVyC（y = 0..9）被忽略，其他时间发生的外部事件有效。在指定的时间内，消隐信号为低电平。该模式由 EXEVyFM [3:0]位域配置，范围从4’b0001 到 4’b1100。

消隐信号源有两种类型：

1 Slave_TIMERx本身：指定的时间是指从计数器复位到比较事件发生持续的时间。（EXEVyFM [3:0] = 4’b0001~4’b0100，用于设置比较0~比较3事件）；

来自其他Slave_TIMER单元（EXEVyFM [3:0] = 4’b0101~4’b1100）的STBLKSRCz（z= 0..7）：指定的时间是指从选定的Slave_TIMER计数器复位到比较事件发生持续的时间。也可以是选定Slave_TIMER中的CH1OPRE信号（在这种情况下，只要CH1OPRE为低电平，事件将被忽略）具体请见 19-12. 。


表 19-12. 消隐模式下的滤波信号映射


<table><tr><td>到来自</td><td>Slave_TIMER0</td><td>Slave_TIMER1</td><td>Slave_TIMER2</td><td>Slave_TIMER3</td><td>Slave_TIMER4</td></tr><tr><td>STBLKSRC0</td><td>Slave_TIMER1比较 0</td><td>Slave_TIMER0比较 0</td><td>Slave_TIMER0比较 1</td><td>Slave_TIMER0比较 0</td><td>Slave_TIMER0比较 1</td></tr><tr><td>STBLKSRC1</td><td>Slave_TIMER1比较 3</td><td>Slave_TIMER0比较 3</td><td>Slave_TIMER1比较 0</td><td>Slave_TIMER1比较 1</td><td>Slave_TIMER1比较 0</td></tr><tr><td>STBLKSRC2</td><td>Slave_TIMER1CH1OPRE</td><td>Slave_TIMER0CH1OPRE</td><td>Slave_TIMER1比较 3</td><td>Slave_TIMER2比较 0</td><td>Slave_TIMER2比较 0</td></tr><tr><td>STBLKSRC3</td><td>Slave_TIMER2比较 0</td><td>Slave_TIMER2比较 0</td><td>Slave_TIMER1CH1OPRE</td><td>Slave_TIMER2比较 1</td><td>Slave_TIMER2比较 3</td></tr><tr><td>STBLKSRC4</td><td>Slave_TIMER2比较 3</td><td>Slave_TIMER2比较 1</td><td>Slave_TIMER3比较 0</td><td>Slave_TIMER2CH1OPRE</td><td>Slave_TIMER2CH1OPRE</td></tr><tr><td>STBLKSRC5</td><td>Slave_TIMER2CH1OPRE</td><td>Slave_TIMER2CH1OPRE</td><td>Slave_TIMER3比较 3</td><td>Slave_TIMER4比较 0</td><td>Slave_TIMER3比较 0</td></tr><tr><td>STBLKSRC6</td><td>Slave_TIMER3比较 0</td><td>Slave_TIMER3比较 1</td><td>Slave_TIMER3CH1OPRE</td><td>Slave_TIMER4比较 3</td><td>Slave_TIMER3比较 3</td></tr><tr><td>STBLKSRC7</td><td>Slave_TIMER4比较 1</td><td>Slave_TIMER4比较 0</td><td>Slave_TIMER3比较 3</td><td>Slave_TIMER4CH1OPRE</td><td>Slave_TIMER3CH1OPRE</td></tr></table>


当 EXEVyMEEN 位置 1 时，将使能外部事件的存储功能，外部事件不会立即生效。一旦指定的时间完成，该外部事件将被存储并生成。


## 窗口模式

窗口模式中，在指定时间内发生的外部事件 EXEVyC（y = 0..9）有效，其他时间发生的则被忽略。在指定的时间内，窗口信号为高电平。此模式由 EXEVyFM[3:0]位域配置，范围从 4’b1101到 4’b1111。

如果在指定时间内未发生外部事件 $\mathsf { E X E V y C } ( \mathsf { y } = 0 . . 9 )$ ，则在指定时间结束时将产生超时事件。

窗口信号源有两种类型：

 Slave_TIMERx本身：指定的时间是指从计数器复位到比较事件发生持续的时间。（EXEVyFM [3:0] = 4’b1101和4’b1110，用于分别设置比较1和比较2事件）；

厂 来自其他Slave_TIMER单元 $( \mathsf { E X E V y F M } \ [ 3 : 0 ] = 4 ^ { \prime } \ \mathsf { b 0 1 0 1 } \sim 4 ^ { \prime } \ \mathsf { b 1 } \ 1 0 0 )$ 的STWDSRC：指定的时间是指从选定的Slave_TIMER计数器复位到比较事件发生持续的时间。具体请见 19-13. 。


表 19-13. 窗口模式的滤波信号映射


<table><tr><td>到来自</td><td>Slave_TIMER0</td><td>Slave_TIMER1</td><td>Slave_TIMER2</td><td>Slave_TIMER3</td><td>Slave_TIMER4</td></tr><tr><td>STWDSRC</td><td>Slave_TIMER1比较 1</td><td>Slave_TIMER0比较 1</td><td>Slave_TIMER3比较 1</td><td>Slave_TIMER2比较 1</td><td>Slave_TIMER3比较 1</td></tr></table>


当 EXEVyMEEN 位置 1 时，将使能外部事件的存储功能，外部事件不会立即生效。一旦指定的时间完成，该外部事件将被存储并生成。


## DAC 触发

当 Slave_TIMERx 的更新事件发生时，如果 SHRTIMER_STxCTL0 寄存器中的 DACTRGS[1:0]！= 2’b00，则在 SHRTIMER_DACTRIGOx（x = 0..3）上生成 DAC 触发请求。如果DACTRGS $[ 1 { : } 0 ] ~ = ~ 2 ^ { \prime } ~ { \mathsf { b } } 0 0$ ， 则 Slave_TIMERx 不 会 生 成 DAC 触 发 请 求 。SHRTIMER_DACTRIGOx（x = 0..3）是从 Slave_TIMERx 连接到 DAC 模块的内部信号。具体请参考 DAC 章节。

## 19.4.3. DLL 校准

DLL 可以产生并校准超高分辨率时钟 SHRTIMER_HPCK（f<sub>SHRTIMER_HPCK</sub> = 64 * f<sub>SHRTIMER_CK</sub>）。DLL 模块可以一次或定期校准超高分辨率时钟 SHRTIMER_HPCK。

当 SHRTIMER_DLLCCTL 寄存器中的 CLBPEREN 位置 1 时，使能定期的 DLL 校准，CLBPER[1:0]位域配置校准周期。DLL 将在整个 SHRTIMER 运行期间定期校准时钟。

当 SHRTIMER_DLLCCTL 寄存器中的 CLBPEREN 位清 0 时，将 CLBSTRT 置 1，DLL 只校准一次超高分辨率时钟 SHRTIMER_HPCK。

## 19.4.4. 突发模式

突发模式控制器允许通过硬件使 CHyOPRE（y = 0,1）交替输出空闲和运行状态。该模式由SHRTIMER_BMCTL 寄存器中的 BMEN 位使能，通常在轻载情况中使用。

突发模式控制器包括：

 1个计数器（BM-counter）；

 1个比较寄存器：SHRTIMER_BMCMPV，用于定义空闲状态的持续时间；

 1个周期寄存器：SHRTIMER_BMCAR，用于定义空闲和运行状态持续时间的总和。

## BM-counter 的计数模式

BM-counter 可以运行在连续模式或单脉冲模式下。

当 BMCTN = 1 时，BM-counter 运行在连续模式下。BM-counter 从 0 连续计数到计数器重载值（SHRTIMER_BMCAR）。当计数到计数器重载值时，计数器将从 0 重新启动。突发模式过程一直持续到 SHRTIMER_BMCTL 中的 BMOPTF 位被复位。

当 BMCTN = 0 时，BM-counter 运行在单脉冲模式下。BM-counter 从 0 连续计数到计数器重载值（SHRTIMER_BMCAR）。当计数到计数器重载值时，BM-counter 停止计数。

当计数到计数器重载值（SHRTIMER_BMCAR）时，SHRTIMER_INTF 寄存器中的 BMPERIF位置 1，如果 BMPERIE = 1（在 SHRTIMER_INTEN 寄存器中），则突发模式控制器产生突发模式周期中断请求。可以写 1 到 SHRTIMER_INTC 中的 BMPERIFC 位来清除 BMPERIF 位。

## 突发模式的时序

BM-counter 由几个时钟源提供时钟，可以通过 SHRTIMER_BMCTL 寄存器中的 BMCLKS[3:0]位选择。当选定的时钟源信号的上升沿到达时，BM-counter 计数值加 1。

当 BMCLKS[3:0] = 4’b1010 时，BM-counter 的时钟源是 f<sub>SHRTIMER_CK</sub> 分频后得到的，分频系数由 SHRTIMER_BMCTL 寄存器中的 BMPSC [3:0]位域定义。

当 BMCLKS[3:0] = 4’b0110~4’b1001 时，BM-counter 的时钟源是芯片内部信号：BMCLKy$( \mathsf { y } = 0 . . 3 )$ ），具体请见 19-14. 。


表 19-14. 突发模式的芯片内部信号


<table><tr><td>BMCLKy(y=0..3)</td><td>芯片内部信号</td></tr><tr><td>BMCLK0</td><td>保留</td></tr><tr><td>BMCLK1</td><td>保留</td></tr><tr><td>BMCLK2</td><td>TIMER6_TRGO</td></tr><tr><td>BMCLK3</td><td>保留</td></tr></table>

空闲状态的持续时间由 SHRTIMER_BMCMPV 寄存器定义，并且 SHRTIMER_BMCAR 寄存器定义了突发模式的周期，该周期值是空闲状态和运行状态持续时间之和，具体请见 19-39.突发模式时序图


图 19-39. 突发模式时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/2213201b2b98f5382a1bc1f5fec78b7ee92075256c2732e1b9e765a0660dcaf6.jpg)


当 BMSE 置位时，SHRTIMER_BMCMPV 和 SHRTIMER_BMCAR 寄存器是预装载，在下列情形下会从预装载传输到有效寄存器：

 当使能突发模式时（BMEN=1）；

 当突发模式周期结束时。

注意：当写 SHRTIMER_BMCAR 后会暂时禁能更新，直到写 SHRTIMER_BMCMPV 寄存器后才恢复更新。

## 突发模式进入

SHRTIMER_BMSTRG 寄存器中定义了 32 个可触发突发模式的事件。这些触发事件可以同时选择，然后再进行逻辑或运算。而在 BM-counter 的计数过程中，这些触发事件被忽略。这些触发事件分为七种：

1. Master_TIMER 事件：重复事件，复位/翻转事件，比较 0/1/2/3 事件；

2. Slave_TIMERx 事件：重复事件，复位/翻转事件，比较 0 和比较 1 事件；

3.外部事件：EXEV6 和 EXEV7；

4. EXEV6 事件之后的 Slave_TIMER0 周期事件；

5. EXEV7 事件之后的 Slave_TIMER3 周期事件；

6.芯片内部信号：TIMER6_TRGO；

7.软件：写 1 到 SHRTIMER_BMSTRG 寄存器的 SWTRG 位。

触发事件发生时，有两种进入突发模式的方式：常规进入和延迟进入。

## 常规进入

当 SHRTIMER_STxCHOCTL 寄存器中的 BMCHyDTI（y = 0，1）位为 0 时，突发模式是常规进入模式。选定事件发生后的第一个 BM-counter 计数时钟到来时，输出将进入突发模式，并输出空闲电平（根据 ISO0 位和 ISO1 位设置）。

19-40. 显示了在以下配置时，Slave_TIMER0 中的 CHyOPRE 波形：

 CyOPRE 处 于 常 规 模 式 ： SHRTIMER_ST0CHOCTL 寄 存 器 中 的 DTEN = 0 ，SHRTIMER_ST0CTL0寄存器中的BLNMEN = 0；

 周期事件产生置位请求；

 比较1事件产生复位请求；

 BM-counter的时钟源是Slave_TIMER0的翻转事件：BMCLKS [3:0] = 4’b0001。


图 19-40. 突发模式的常规进入


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/d8e62b77c07c144f177f27a0a0df173c646c1b7faca297517242ee9033764c69.jpg)


## 延迟进入

当 SHRTIMER_STxCHOCTL 寄存器中的 BMCHyDTI（y = 0,1）位为 1 时，突发模式的进入被延迟。在进入突发模式之前，CHyOPRE 被强制插入死区时间。

每个 CHyOPRE 都有自己的死区插入值：

 BMCH0DTI = 1时，DTRCFG[15:0]用于配置CH0OPRE的死区时间；

 BMCH1DTI = 1时，DTFCFG[15:0]用于配置CH1OPRE的死区时间。

延迟进入模式适用于以下情况：CHyOPRE(y=0,1)之一具有有效的空闲电平 $( | \mathsf { S O y } = 1 )$ ），且死区时间为正（DTRS /DTFS 设置为 0）。

在常规死区时间内，突发模式被触发，当前死区过程中止，将重新开始新的死区插入过程。详见 19-41. 。


图 19-41. 突发模式的延迟进入


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/78519237353953f34f4ad6fb277634cb8633678b6c419778d31f9569c03b144f.jpg)


## 突发模式退出

在连续模式下，突发模式由软件强制退出。BMOPTF 或 BMEN 位重写为 0 后，发生输出置位/复位请求时，会退出突发模式。详情请见 19-40. 和 19-41.式的延迟进入。

在单脉冲模式下，一旦经过空闲周期，就退出突发模式。

## 突发模式的时钟

可以在突发模式工作（运行，空闲）期间停止并复位 Master_TIMER 和 Slave_TIMERx（x =0..4）单元的计数器，可通过 SHRTIMER_BMCTL 寄存器中的 BMMT 位和 BMSTx $( \mathsf { X } = 0 . . 4 )$ 位进行配置：

 BMMT或BMSTx $( { \bf \times } = 0 . . 4 ) = 0$ ：保持Master_TIMER或Slave_TIMERx $( \mathsf { X } = 0 . . 4 )$ 的计数器时钟（SHRTIMER_PSCCK），且计数器正常运行；

 BMMT或BMSTx $( \times = 0 . . 4 ) = 1$ ：Master_TIMER或Slave_TIMERx $( \mathsf { X } = 0 . . 4 )$ 计数器时钟（SHRTIMER_PSCCK）停止，并复位计数器。

## 使用 SHRTIMER_STxCMP0CP 寄存器模拟突发模式

可以使用 SHRTIMER_STxCMP0CP 寄存器来生成类似于突发模式控制的波形，配置如下：

 比较0事件用于产生复位请求；

 周期事件用于产生置位请求；

 使用DMA（重复事件）连续将两个32位数据写入SHRTIMER_STxCMP0CP寄存器，如下所示：

SHRTIMER_STxCMP0CP = {CREP [7:0] =运行周期数-1；CMP0VAL [15:0] =占空比}

SHRTIMER_STxCMP0CP = {CREP [7:0] =空闲周期数-1；CMP0VAL [15:0] = 0}

例如，要生成每 5 个周期中有 2 个周期输出置位的 PWM 波，可进行如下配置：

 运行：SHRTIMER_STxCMP0CP = {0x0001; 0x0020}；

 空闲：SHRTIMER_STxCMP0CP = {0x0002; 0x0000}。


图 19-42. 模拟突发模式示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/5036610e73f703c99fccb4ee5f26418c3fab354521bfa6319bbfe3b83513b3ea.jpg)


## 19.4.5. 同步输入/输出

同步电路在 Master_TIMER 内部：

 同步输出：SHRTIMER可以作为主机产生同步信号；

 同步输入：SHRTIMER也可以作为从机等待触发同步。

## 同步输出

可以将 SHRTIMER 配置为主机，同步外部资源；

可以配置 SHRTIMER_MTCTL0 寄存器中的 SYNOSRC[1:0]位域，选择发送到同步输出上的源。有以下四个源：

 2’b00：Master_TIMER启动事件。在以下三种情况下可以将生成的启动事件用作同步输出，当MTCEN位置1时，当计数器在单脉冲模式下达到周期值后重新启动时，还有当CTNM或CNTRSTM位置1时，在计数期间发生的复位事件；

 2’b01：Master_TIMER比较0事件；

 2’b10：Slave_TIMER0复位和启动事件。它与Master_TIMER启动事件类似，除以下情

况外：连续模式下的计数器翻转，在CNTRSTM = 0时的单脉冲模式下放弃的复位请求； $_ { 2 } \cdot$ b11：Slave_TIMER0比较0事件。

SHRTIMER_MTCTL0 寄存器中的 SYNOPLS[1:0]位域确定同步输出信号的极性：

 $_ { 2 } \cdot$ b00：脉冲产生禁能。同步输出引脚SHRTIMER_SCOUT上没有脉冲；

 $_ { 2 } \cdot$ b01：保留；

 $_ { 2 } \cdot$ b10：在同步输出引脚SHRTIMER_SCOUT上生成正脉冲。正脉冲的长度为16t<sub>SHRTIMER_CK</sub>个周期；

$_ { 2 } \cdot$ b11：在同步输出引脚SHRTIMER_SCOUT上生成负脉冲。负脉冲的长度为16t<sub>SHRTIMER_CK</sub>个周期。

## 同步输入

SHRTIMER 可以作为从机等待触发同步。可以通过 SHRTIMER_MTCTL0 寄存器中的SYNISRC [1:0]位域选择同步输入源。有四个输入触发源可选：

 $_ { 2 } \cdot$ b00：同步输入禁能；

厂 $_ { 2 } \cdot$ b01：保留；

 $_ { 2 } \cdot$ b10：芯片内部信号。高级定时器TIMER0的TIMER0_TRGO信号；

 $_ { 2 } \cdot$ b11：芯片外部引脚。芯片外部引脚（SHRTIMER_SCIN）上的正脉冲（上升沿有效）。

Master_TIMER 由 SHRTIMER_MTCTL0 寄存器中的 SYNISTRT 位和 SYNIRST 位配置。Slave_TIMERx 由 SHRTIMER_STxCTL0 寄存器中的 SYNISTRT 位和 SYNIRST 位配置。

当 SYNISTRT 置 1 时，必须先使能定时器（将 STxCEN 位或 MTCEN 位置 1），则同步输入信号将启动计数器。在连续模式下，即使 STxCEN 位或 MTCEN 位被置 1，计数器也不会启动，只有在同步输入信号到达后才会启动。

当 SYNIRST 置 1 时，同步输入信号将复位计数器，并像其他任何重置事件一样递减重复计数器。

## 19.4.6. 外部事件

10 个外部事件可以同时用于 5 个 Slave_TIMER 中的任意 1 个。通过 SHRTIMER_EXEVCFG0寄存器配置外部事件 （y y = 0..4），通过 SHRTIMER_EXEVCFG0 和 SHRTIMER_EXEVDFCTL寄存器配置外部事件 y（y = 5..9）。

处理外部事件 y（y = 0..4）的过程如 19-43. y y=0..4 所示。


图 19-43. 外部事件 y（y=0..4）处理过程框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/4dc2d1bec35cf585eb9a83c0f343444859d963e30ffb053de32ce630387f7858.jpg)


外部事件 $\texttt { y ( y = 0 . 4 ) }$ 的配置如下：

 4个源：通过EXEVySRC[1:0]位域进行配置；

 有效沿选择：通过EXEVyEG[1:0]位域进行配置。可以是电平有效的或边沿有效（上升沿，下降沿或两者兼有）；

 极性选择：在电平有效 $( \mathsf E \mathsf { X } \mathsf E \mathsf { V } \mathsf { Y } \mathsf E \mathsf { G } [ 1 : 0 ] = 2 ^ { \prime } \mathsf { b } 0 0 )$ 时，由EXEV0P位进行配置。

处理外部事件 $y \ ( y = 5 . . 9 )$ 的过程如 19-44. y y=5..9 所示。


图 19-44. 外部事件 y（y=5..9）处理过程框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/c995c338d105487489f5d6dbf3f103c5627273174f82a491811da6d29e3dcedc.jpg)


外部事件 y（y=5..9）的配置如下：

 4个源：通过EXEVySRC[1:0]位域进行配置；

 有效沿选择：通过EXEVyEG[1:0]位域进行配置。可以是电平有效的或边沿有效（上升沿，下降沿或两者兼有）；

 极性选择：在电平有效 $( \mathsf E \mathsf { X } \mathsf E \mathsf { V } \mathsf { Y } \mathsf E \mathsf { G } [ 1 : 0 ] = 2 ^ { \prime } \mathsf { b } 0 0 )$ 时，由EXEV0P位进行配置；

 数字滤波配置：配置SHRTIMER_EXEVDFCTL寄存器中的EXEVyFC[3:0]位域。

数 字 滤 波 器 的 采 样 时 钟 f<sub>SHRTIMER_EXEVFCK</sub> 由 SHRTIMER_EXEVDFCTL 寄 存 器 中 的EXEVFDIV[2:0]位域定义。

这些外部事件源 EXEVySRCz $( \mathsf { y } = 0 . . 9 , \mathsf { z } = 0 . . 4 )$ 可以来自比较器、数字输入引脚、ADC 的模拟看门狗和 TIMER_TRGO。具体请参考 19-15. 。


表 19-15. 外部事件映射


<table><tr><td>外部事件</td><td>EXEVySRC0</td><td>EXEVySRC1</td><td>EXEVySRC2</td><td>EXEVySRC3</td></tr><tr><td>外部事件 0</td><td>PC12</td><td>比较器 1</td><td>TIMER0_TRGO</td><td>ADC0_AWD0</td></tr><tr><td>外部事件 1</td><td>PC11</td><td>比较器 3</td><td>TIMER1_TRGO</td><td>ADC0_AWD1</td></tr><tr><td>外部事件 2</td><td>PB7/PD5</td><td>比较器 5</td><td>TIMER2_TRGO</td><td>ADC0_AWD2</td></tr><tr><td>外部事件 3</td><td>PB6/PG11</td><td>x</td><td>x</td><td>ADC1_AWD0</td></tr><tr><td>外部事件 4</td><td>PB9/PG12</td><td>x</td><td>x</td><td>ADC1_AWD1</td></tr><tr><td>外部事件 5</td><td>PB5</td><td>比较器 1</td><td>TIMER5_TRGO</td><td>ADC1_AWD2</td></tr><tr><td>外部事件 6</td><td>PB4</td><td>比较器 3</td><td>TIMER6_TRGO</td><td>x</td></tr><tr><td>外部事件 7</td><td>PB8</td><td>比较器 5</td><td>x</td><td>x</td></tr><tr><td>外部事件 8</td><td>PB3</td><td>x</td><td>x</td><td>x</td></tr><tr><td>外部事件 9</td><td>PC6/PG13</td><td>x</td><td>x</td><td>x</td></tr></table>


注意：“×”表示不可用。


可以直接使用外部事件 y（y = 0..9），也可以对其进行滤波处理（以在指定时间内限制其操作）。具体参考 。

## 19.4.7. 故障输入

SHRTIMER 具有故障保护机制，可用于每个 Slave_TIMERx。具体请参考 19-45.结构图

发生故障事件时，输出（STxCHy_O，x = 0..4，y = 0,1）为预置的电平，该电平将一直保持到软件重新使能输出（写 1 到 STxCHyEN 位）时为止。

预置电平由 SHRTIMER_STxCHOCTL 寄存器中的 CHyFLTOS[1:0]位域配置，保护机制可以处理两种类型的故障源：

 故障通道：来自数字输入引脚或比较器的故障事件；

 系统故障：来自MCU内部的信号，例如SRAM奇偶校验器。


图 19-45. 故障输入结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/0bba38271ecec3ad7a1a7197391517fba13cf99d7bfc99b40257750759753c24.jpg)



通 过 SHRTIMER_STxFLTCTL 寄 存 器 中 的 FLTyEN 位 使 能 故 障 输 入 。 对SHRTIMER_STxFLTCTL 寄存器中的 FLTENPROT 位的一次写入可以保护 FLTyEN 位。当FLTENPROT 位置 1 时，FLTyEN 位写保护（只读）。


## 故障通道

可以通过 SHRTIMER_FLTINCFG0 和 SHRTIMER_FLTINCFG1 寄存器配置所有的故障通道。FLTyINSRC（y = 0..4）位用于选择故障通道源，即可以是数字输入引脚，也可以是比较器输出。具体请见 19-16. 。


表 19-16. 故障通道映射


<table><tr><td>故障通道</td><td><eq>FLTyINSRC = 0</eq>(输入引脚)</td><td><eq>FLTyINSRC = 1</eq>(比较器)</td></tr><tr><td>故障通道 0</td><td>PA12</td><td>比较器 1</td></tr><tr><td>故障通道 1</td><td>PA15</td><td>比较器 3</td></tr><tr><td>故障通道 2</td><td>PB10 / PD4</td><td>比较器 5</td></tr><tr><td>故障通道 3</td><td>PB11</td><td>x</td></tr><tr><td>故障通道 4</td><td>PC7 / PG10</td><td>x</td></tr></table>


注意：“×”表示不可用。


可以通过 SHRTIMER_FLTINCFG0 和 SHRTIMER_FLTINCFG1 寄存器中的 FLTyINP 位来配置故障信号的极性。如果 FLTyINP = 0，信号低电平有效；如果 FLTyINP = 1，则高电平有效。

可通过 SHRTIMER_FLTINCFG0 和 SHRTIMER_FLTINCFG1 寄存器中的 FLTyINFC[3:0]位域，对设置极性后的数字信号滤波器进行配置。数字滤波器采样时钟 f<sub>SHRTIMER_FLTFCK</sub> 由

SHRTIMER_FLTINCFG1 寄存器中的 FLTFDIV[2:0]位域定义。

可通过 SHRTIMER_FLTINCFG0 和 SHRTIMER_FLTINCFG1 寄存器中的 FLTyINEN 位来使能故障通道 $\texttt { y ( y = 0 . 4 ) }$ ），所有通道可同时使能。

对 SHRTIMER_FLTINCFG0 和 SHRTIMER_FLTINCFG1 寄存器中 FLTyINPROT 位的一次写入，可保护 FLT0INEN 位，FLT0INP 位，FLT0INSRC 位和 FLT0INFC [3:0]位域。当 FLTyINPROT位置 1 时，这些位写保护（只读）。

## 系统故障

系统故障来自芯片内部的信号：

 时钟监视生成的HXTAL故障事件；

 Cortex<sup>®</sup>-M33锁定信号；

 低压检测器（LVD）的输出。

当 SHRTIMER_STxFLTCTL 寄存器中的 FLTyEN 位置 1 时，系统故障才有效。系统故障可以覆盖故障通道输入（逻辑或）。

## 19.4.8. ADC 触发

Master_TIMER 和 Slave_TIMERx 可以触发 ADC，4 个独立的触发（SHRTIMER_ADCTRIGy，y = 0..3）可用于使能 ADC 常规序列。具体请参考 19-46. ADC 。


图 19-46. ADC 触发源选择图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/0a2920a73f0d7bef9896a7860ef7ba8ee36a9afb91043f916ceb9527f98be76e.jpg)



每个触发输出最多可以连接（逻辑或运算）32 个事件。它们在 SHRTIMER_ADCTRIGSy（y= 0..3）寄存器中定义。


SHRTIMER_ADCTRIGSy（y = 0..3）寄存器使能预加载，并可以使用与其相关的定时器进行同步更新。更新源由 SHRTIMER_CTL0 寄存器中的 ADTGyUSRC[2:0]位域定义。例如，ADTGyUSRC [2:0] = 3’b001，Slaver_TIMER0 是更新源：

 如果SHRTIMER_STxCTL0寄存器中的SHWEN = 1，SHRTIMER_ADCTRIGSy（y = 0..3）寄存器被预加载，可以与Slaver_TIMER0同步更新；

 如果SHRTIMER_STxCTL0寄存器中的SHWEN = 0，SHRTIMER_ADCTRIGSy（y = 0..3）寄存器不会被预加载，写访问将使触发源立即更新。

## 19.4.9. DAC 触发

SHRTIMER 允许使用定时器更新同步更新片上 DAC。Master_TIMER 和 Slave_TIMERx 的更新事件可以在 SHRTIMER_DACTRIGy（y = 0..2）上生成 DAC 更新触发。

SHRTIMER_MTCTL0 和 SHRTIMER_STxCTL0 寄存器中的 DACTRGS [1:0]位域配置如下：

 00：没有DAC触发事件发生；

 01：在SHRTIMER_DACTRIG0上生成DAC触发事件；

 10：在SHRTIMER_DACTRIG1上生成DAC触发事件；

 11：在SHRTIMER_DACTRIG2上生成DAC触发事件。

在多个计时器中使能 DACTRGS [1:0]位域时，SHRTIMER_DACTRIGy（y = 0..2）将由所有定时器的更新事件或组成。具体请参考 19-47. DAC 。


图 19-47. DAC 触发源选择图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/649b7b0254be49f64b57470b2b0a70b83c44b04658e17cd9f33a588fb1740e6f.jpg)


## 19.4.10. 中断

大多数事件可以生成中断请求，所有的中断请求可分组到 7 个中断向量(SHRTIMER_IRQy，y=0..6)。详见 19-17. 。


表 19-17. 中断映射


<table><tr><td>中断号</td><td>事件</td><td>Control bit</td></tr><tr><td>Master_TIMER:</td><td>更新事件</td><td>SHRTIMER_MTDMAINTEN 中的 UPIE 位</td></tr><tr><td rowspan="6">SHRTIMER_IRQ0</td><td>同步输入事件</td><td>SHRTIMER_MTDMAINTEN 中的 SYNIIE 位</td></tr><tr><td>重复事件</td><td>SHRTIMER_MTDMAINTEN 中的 REPIE 位</td></tr><tr><td>比较 0 事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP0IE 位</td></tr><tr><td>比较 1 事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP1IE 位</td></tr><tr><td>比较 2 事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP2IE 位</td></tr><tr><td>比较 3 事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP3IE 位</td></tr><tr><td rowspan="3">Slave_TIMER0:SHRTIMER_IRQ1</td><td>延迟空闲模式进入</td><td>SHRTIMER_STxDMAINTEN 中的 DLYIIIE 位</td></tr><tr><td>计数器复位事件</td><td>SHRTIMER_STxDMAINTEN 中的 RSTIE 位</td></tr><tr><td>C1OPRE 从有效到无效</td><td>SHRTIMER_STxDMAINTEN 中的 CH1ONAIE 位</td></tr><tr><td rowspan="2">Slave_TIMER1:SHRTIMER_IRQ2</td><td>C1OPRE 从无效到有效</td><td>SHRTIMER_STxDMAINTEN 中的 CH1OAIE 位</td></tr><tr><td>C0OPRE 从有效到无效</td><td>SHRTIMER_STxDMAINTEN 中的 CH0ONAIE 位</td></tr><tr><td rowspan="2">Slave_TIMER2:SHRTIMER_IRQ3</td><td>C0OPRE 从无效到有效</td><td>SHRTIMER_STxDMAINTEN 中的 CH0OAIE 位</td></tr><tr><td>捕获 1 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CAP1IE 位</td></tr><tr><td rowspan="2">Slave_TIMER3:SHRTIMER_IRQ4</td><td>捕获 0 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CAP0IE 位</td></tr><tr><td>更新事件</td><td>SHRTIMER_STxDMAINTEN 中的 UPIE 位</td></tr><tr><td rowspan="5">Slave_TIMER4:SHRTIMER_IRQ5</td><td>重复事件</td><td>SHRTIMER_STxDMAINTEN 中的 REPIE 位</td></tr><tr><td>比较 3 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CMP3IE 位</td></tr><tr><td>比较 2 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CMP2IE 位</td></tr><tr><td>比较 1 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CMP1IE 位</td></tr><tr><td>比较 0 事件</td><td>SHRTIMER_STxDMAINTEN 中的 CMP0IE 位</td></tr><tr><td rowspan="2">SHRTIMER_IRQ0</td><td>突发模式周期事件</td><td>SHRTIMER_INTEN 中的 BMPERIE 位</td></tr><tr><td>DLL 校准完成</td><td>SHRTIMER_INTEN 中的 DLLCALIE 位</td></tr><tr><td rowspan="6">SHRTIMER_IRQ6</td><td>系统故障</td><td>SHRTIMER_INTEN 中的 SYSFLTIE 位</td></tr><tr><td>故障 4</td><td>SHRTIMER_INTEN 中的 FLT4IE 位</td></tr><tr><td>故障 3</td><td>SHRTIMER_INTEN 中的 FLT3IE 位</td></tr><tr><td>故障 2</td><td>SHRTIMER_INTEN 中的 FLT2IE 位</td></tr><tr><td>故障 1</td><td>SHRTIMER_INTEN 中的 FLT1IE 位</td></tr><tr><td>故障 0</td><td>SHRTIMER_INTEN 中的 FLT0IE 位</td></tr></table>

## 19.4.11. DMA 请求

大多数事件可以生成 DMA 请求，每个定时器对应一个 DMA 通道，详见 19-18. DMA。


表 19-18. DMA 请求映射


<table><tr><td>DMA channel</td><td>Event</td><td>Control bit</td></tr><tr><td rowspan="5">Master_TIMER: DMA0_Channel1</td><td>更新事件</td><td>SHRTIMER_MTDMAINTEN 中的 UPDEN 位</td></tr><tr><td>同步输入事件</td><td>SHRTIMER_MTDMAINTEN 中的 SYNIDEN 位</td></tr><tr><td>重复事件</td><td>SHRTIMER_MTDMAINTEN 中的 REPDEN 位</td></tr><tr><td>比较 0 事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP0DEN 位</td></tr><tr><td>比较 1 事件比较2事件</td><td>SHRTIMER_MTDMAINTEN 中的 CMP1DEN 位SHRTIMER_MTDMAINTEN中的CMP2DEN位</td></tr><tr><td></td><td>比较3事件</td><td>SHRTIMER_MTDMAINTEN中的CMP3DEN位</td></tr><tr><td rowspan="3">Slave_TIMER0: DMA0_Channel2</td><td>延迟空闲模式进入</td><td>SHRTIMER_STxDMAINTEN中的DLYIDEN位</td></tr><tr><td>计数器复位事件</td><td>SHRTIMER_STxDMAINTEN中的RSTDEN位</td></tr><tr><td>C1OPRE从有效到无效</td><td>SHRTIMER_STxDMAINTEN中的CH1ONADEN位</td></tr><tr><td rowspan="2">Slave_TIMER1: DMA0_Channel3</td><td>C1OPRE从无效到有效</td><td>SHRTIMER_STxDMAINTEN中的CH1OADEN位</td></tr><tr><td>C0OPRE从有效到无效</td><td>SHRTIMER_STxDMAINTEN中的CH0ONADEN位</td></tr><tr><td rowspan="3">Slave_TIMER2: DMA0_Channel4</td><td>C0OPRE从无效到有效</td><td>SHRTIMER_STxDMAINTEN中的CH0OADEN位</td></tr><tr><td>捕获1事件</td><td>SHRTIMER_STxDMAINTEN中的CAP1DEN位</td></tr><tr><td>捕获0事件</td><td>SHRTIMER_STxDMAINTEN中的CAP0DEN位</td></tr><tr><td rowspan="2">Slave_TIMER3: DMA0_Channel5</td><td>更新事件</td><td>SHRTIMER_STxDMAINTEN中的UPDEN位</td></tr><tr><td>重复事件</td><td>SHRTIMER_STxDMAINTEN中的REPDEN位</td></tr><tr><td rowspan="4">Slave_TIMER4: DMA0_Channel6</td><td>比较3事件</td><td>SHRTIMER_STxDMAINTEN中的CMP3DEN位</td></tr><tr><td>比较2事件</td><td>SHRTIMER_STxDMAINTEN中的CMP2DEN位</td></tr><tr><td>比较1事件</td><td>SHRTIMER_STxDMAINTEN中的CMP1DEN位</td></tr><tr><td>比较0事件</td><td>SHRTIMER_STxDMAINTEN中的CMP0DEN位</td></tr></table>


注意：必须先禁能 DMA控制器，然后再禁能 DMA请求。


## 19.4.12. DMA 模式

定时器的 DMA 模式是通过 DMA模块，实现单个 DMA 请求配置 SHRTIMER 的多个寄存器的功能。相关的寄存器（总共七个寄存器）如下：

 SHRTIMER_DMAUPMTR：定义更新Master_TIMER中的哪些寄存器。Master_TIMER的大多数控制和数据寄存器都与一个选择位关联。如果该选择位置位，则写访问将重定向到关联的寄存器；

 SHRTIMER_DMAUPSTxR ： 定 义 更 新 Slave_TIMERx 中 的 哪 些 寄 存 器 。 大 多 数Slave_TIMERx控制和数据寄存器都与一个选择位相关联。如果该选择位被置位，则写访问将重定向到关联的寄存器。

 SHRTIMER_DMATB：DMA传输缓冲区寄存器。只需要将指向SHRTIMER_DMATB寄存器的DMA模块作为目标，并禁能外设增量模式的外设配置。所有对该寄存器的写访问都将通过重定向机制在内部重新传输到最终目标寄存器。

DMA模式功能仅适用于一个 DMA 通道，6 个通道中的任何一个都进行 DMA传输。

DMA 模式是永久使能的（没有使能位）。通过对 SHRTIMER_DMATB 寄存器的首次写访问来启动 DMA操作。

发生 DMA 请求时，SHRTIMER 会生成多个 32 位 DMA 请求并解析要更新的寄存器（在SHRTIMER_DMAUPMTR 和 SHRTIMER_DMAUPSTxR 寄存器中定义）。如果选择位置 1，则写访问将重定向到关联的寄存器。如果选择位为 0，则跳过相关寄存器更新，并继续进行寄存器解析，直到检测到新的位置1，触发新的DMA请求。6个寄存器（SHRTIMER_DMAUPMTR和 SHRTIMER_DMAUPSTxR 寄存器）全部解析后，DMA模式完成，系统已准备好等待下一个 DMA 触发。若再有 DMA 请求事件发生，则 SHRTIMER 将重复上述过程。详见 19-48.DMA 。


图 19-48. DMA 模式运行流程图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/d1290233-f7db-4838-b6a3-56ac5937f190/d75ac7734f8b63f0f18137c5cd4b6332660d1cad8f0af55d9b5ce258490c4def.jpg)


## 19.4.13. Debug 模式

当 Cortex<sup>®</sup>-M33 内核暂停时，DBG_CTL0 寄存器中的 SHRTIMER_HOLD 位决定了计数器是否停止运行。

## SHRTIMER_HOLD = 0

若 SHRTIMER_HOLD = 0，则 SHRTIMER 继续正常运行。

## SHRTIMER_HOLD = 1

若 SHRTIMER_HOLD = 1，则将停止 Master_TIMER 和所有 Slave_TIMERx 中的计数器。

如果 CHyFLTOS[1:0] = 2’b01、2’b10、2’b11，则输出进入 FAULT 状态。可以通过将SHRTIMER_CHOUTEN 寄存器中的 STxCHyEN 位置 1，清零 SHRTIMER_HOLD 位来再次使能输出。如果 CHyFLTOS [1:0] = 2’b00，则输出保持其当前状态。退出调试模式时，输出将返回其原始状态。

所有计数器的复位/启动和捕获触发功能都禁能。除 ADC 触发外，所有外部事件的触发都被禁能。更新事件将被丢弃。突发模式电路被冻结：触发都被忽略，突发模式计数器停止。

DLL 校准正常运行。在运行模式下驱动正常输出的单元不受调试影响，例如死区时间单元，载波信号和置位/复位交叉开关等。
