## 23.5. 基本定时器（TIMERx, x = 5, 6）

## 23.5.1. 简介

基本定时器（TIMER5 / 6）包含一个无符号 16 位计数器。可以被用作通用定时器和为 DAC（数字到模拟转换器）提供时钟。基本定时器可以配置产生 DMA请求，TRGO0 触发连接到 DAC。

## 23.5.2. 主要特征

 计数器宽度：16位（TIMER5 / 6）；

 时钟源只有内部时钟；

 计数模式：向上计数；

 可编程的预分频器：16位，运行时可以被改变；

 自动重装载功能；

 中断输出和DMA请求：更新事件。

## 23.5.3. 结构框图

23-141. 提供了基本定时器内部配置的细节。


图 23-141. 基本定时器结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/4c62056567858fb3e6fa5af98f1e8f14f1deb748af8d2d8baca9283d0edd2037.jpg)


## 23.5.4. 功能描述

## 时钟源选择

基本定时器只能由内部时钟源CK_TIMER驱动（来自RCU模块）。

TIMER_CK用来驱动计数器预分频器。当CEN置位，TIMER_CK经过预分频器（预分频值由TIMERx_PSC寄存器确定）产生PSC_CLK。


图 23-142. 内部时钟分频为 1 时正常模式下的控制电路


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/302fa131333707f6fc6bd8a40a0451236633ec1a66a1b044d815581f575da656.jpg)


## 预分频

预分频器可以将定时器的时钟（TIMER_CK）频率按 1 到 65536 之间的任意值分频，分频后的时钟 PSC_CLK 驱动计数器计数。分频系数受预分频寄存器 TIMERx_PSC 控制，这个控制寄存器带有缓冲器，它能够在运行时被改变。新的预分频器的参数在下一次更新事件到来时被采用。


图 23-143. 当预分频器的参数从 1 变到 2 时，计数器的时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e48feecee4be55e83743b6c401136fff3410ad35941956f0f06d9b3baff2f1d0.jpg)


## 向上计数模式

在这种模式，计数器的计数方向是向上计数。计数器从 0 开始向上连续计数到自动加载值（定义在 TIMERx_CAR 寄存器中），一旦计数器计数到自动加载值，会重新从 0 开始向上计数并产生上溢事件。在向上计数模式中，TIMERx_CTL0 寄存器中的计数方向控制位 DIR 应该被设置成 0。

当通过 TIMERx_SWEVG 寄存器的 UPG 位置 1 来设置更新事件时，计数值会被清 0，并产生更新事件。

如果 TIMERx_CTL0 寄存器的 UPDIS 置 1，则禁止更新事件。

当发生更新事件时，所有的寄存器（自动重载寄存器，预分频寄存器）都将被更新。

下面这些图给出了一些例子，当 TIMERx_CAR = 0x99 时，计数器在不同预分频因子下的行为。


图 23-144. 向上计数时序图，PSC = 0 / 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/e45566fe346132d1a6b98c87e7a8e8f736f2079596cbd1b67ed7ed931ee9dc9e.jpg)



图 23-145. 向上计数时序图，在运行时改变 TIMERx_CAR 寄存器的值


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/78b9eef83673df4636505b31cc3e69dc57931ae7c7c4fda919fa06305f60eccb.jpg)


## 微调模式

通过配置TIMERx_CTL0寄存器中的ADMEN位为1，可以使能微调模式。该模式可以提高输出PWM波的有效分辨率，通过TIMERx_CHxCV寄存器中的CHxVAL[19:0]位域可以提高占空比分辨率，通过TIMERx_CAR寄存器中的CARL[19:0]位域可以提高PWM频率的分辨率。

当微调模式使能时，CHxVAL位域和CARL位域的低16位[15:0]用于整数部分，高4位[19:16]用于微调的小数部分。通过预定义的方式，在连续16个周期内对CHxVAL值或CARL值进行微调（每次调整不超过一个TIMER时钟周期），可增加16倍的分辨率。


图 23-146. 微调模式：数据格式和寄存器位域


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/5425f1399594e783349a8af53017e20f153c9f58912401a21c66402472bf6312.jpg)


根据ADMEN位的配置（置位或清零），CHxVAL位域和CARL位域将自动更新。当需要对ADMEN位进行清零时，需要遵循以下步骤：

1. CEN位和ARSE位必须清零；

2. CARL[19:16]位域必须清零；

3. ADMEN位必须清零；

4. CHxIF位必须清零；

5. 可以将CEN位置1。

以下公式可以计算PWM分辨率：

$$
\text { Resolution } = f _ {\text { PSC\_CLK }} / f _ {\text { pwm }}\tag{23-12}
$$

由式(23-12)可得，微调模式禁能时（ADMEN=0），PWM的最小频率 $\mathsf { f } _ { \mathsf { p w m } }$ ：

$$
(f _ {p w m}) _ {\min} = f _ {P S C \_ C L K} / 6 5 5 3 6\tag{23-13}
$$

微调模式使能时（ADMEN=1），

$$
\left(f _ {p w m}\right) _ {\min} = f _ {P S C \_ C L K} / (6 5 5 3 5 + 1 5 / 1 6)\tag{23-14}
$$

当微调模式使能时，CHxVAL[19:0]位域和CARL[19:0]位域的最大值为0xFFFFE（整数部分为0xFFFE，小数部分为0xF）。

在连续16个周期内，占空比和周期的变化情况，具体如 23-147. PWM 和 23-24.CHxVAL CARL 所示。


图 23-147. PWM 微调模式原理


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/e6d2714b-24e2-4226-902a-8eae5da73f29/d50036fcbe0b13250e7dca5fc4012bde87f9f8ba719e2b41980adca348ea79eb.jpg)



表 23-24. 边沿对齐模式中 CHxVAL 和 CARL 位域的变化


<table><tr><td rowspan="2">CHxVAL[19:16]/CARL[19:16]</td><td colspan="16">周期</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>0000</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0001</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0010</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0011</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0100</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0101</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0110</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0111</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1000</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1001</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1010</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1011</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>1100</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1101</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1110</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr><tr><td>1111</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>-</td></tr></table>

## UPIF 位备份功能

可以通过配置TIMERx_CTL0寄存器中的UPIFBUEN位来使能UPIF位的备份功能，UPIF和UPIFBU位之间没有延迟，两者完全同步。

使能该功能后，TIMERx_INTF寄存器中的UPIF位将会被实时备份到TIMERx_CNT寄存器中的UPIFBU位。这可以避免在读计数器和中断处理时产生冲突的情况。

## 定时器调试模式

当Cortex<sup>®</sup>-M33内核停止，DBG_CTL0寄存器中的TIMERx_HOLD配置位被置1，定时器计数器停止。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>ADMEN</td><td>UPIFBUEN</td><td colspan="3">保留</td><td>ARSE</td><td colspan="3">保留</td><td>SPM</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="3"></td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

