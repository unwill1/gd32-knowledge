## 18. 定时器（TIMER）


表 18-1. 定时器（TIMERx）分为 7 种类型


<table><tr><td>定时器</td><td>定时器0/7</td><td>定时器1~4</td><td>定时器8/11</td><td>定时器9/10/12/13</td><td>定时器14</td><td>定时器15/16</td><td>定时器5/6</td></tr><tr><td>类型</td><td>高级</td><td>通用(L0)</td><td>通用(L1)</td><td>通用(L2)</td><td>通用L3</td><td>通用L4</td><td>基本</td></tr><tr><td>预分频器</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数器</td><td>16位</td><td>32位(定时器1)16位(定时器2~4)</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数模式</td><td>向上,向下,中央对齐</td><td>向上,向下,中央对齐</td><td>只有向上</td><td>只有向上</td><td>只有向上</td><td>只有向上</td><td>只有向上</td></tr><tr><td>可重复性</td><td>●</td><td>×</td><td>×</td><td>×</td><td>●</td><td>●</td><td>×</td></tr><tr><td>捕获/比较通道数</td><td>4</td><td>4</td><td>2</td><td>1</td><td>2</td><td>1</td><td>0</td></tr><tr><td>互补和死区时间</td><td>●</td><td>×</td><td>×</td><td>×</td><td>●</td><td>●</td><td>×</td></tr><tr><td>中止输入</td><td>●</td><td>×</td><td>×</td><td>×</td><td>●</td><td>●</td><td>×</td></tr><tr><td>单脉冲</td><td>●</td><td>●</td><td>●</td><td>×</td><td>●</td><td>●</td><td>●</td></tr><tr><td>正交译码器</td><td>●</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>主-从管理</td><td>●</td><td>●</td><td>●</td><td>×</td><td>●</td><td>×</td><td>×</td></tr><tr><td>内部连接</td><td>●(1)</td><td>●(2)</td><td>●(3)</td><td>×</td><td>●(3)</td><td>×</td><td>TRGO TODAC</td></tr><tr><td>DMA</td><td>●</td><td>●</td><td>×</td><td>×</td><td>●</td><td>●</td><td>●(5)</td></tr><tr><td>Debug模式</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

<table><tr><td rowspan="2">(1)</td><td>TIMER0</td><td><eq>ITI0:TIMER4_TRGO^{(7)}</eq></td><td><eq>ITI1:TIMER1_TRGO</eq></td><td><eq>ITI2:TIMER2_TRGO</eq></td><td><eq>ITI3:TIMER3_TRGO^{(7)}</eq></td></tr><tr><td>TIMER7</td><td><eq>ITI0:TIMER0_TRGO</eq></td><td><eq>ITI1:TIMER1_TRGO</eq></td><td><eq>ITI2:TIMER3_TRGO</eq></td><td><eq>ITI3:TIMER4_TRGO</eq></td></tr><tr><td rowspan="4">(2)</td><td>TIMER1</td><td><eq>ITI0:TIMER0_TRGO</eq></td><td><eq>ITI1:参考注释(6)</eq></td><td><eq>ITI2:TIMER2_TRGO</eq></td><td><eq>ITI3:TIMER3_TRGO</eq></td></tr><tr><td>TIMER2</td><td><eq>ITI0:TIMER0_TRGO</eq></td><td><eq>ITI1:TIMER1_TRGO</eq></td><td><eq>ITI2:TIMER4_TRGO</eq></td><td><eq>ITI3:TIMER3_TRGO</eq></td></tr><tr><td>TIMER3</td><td><eq>ITI0:TIMER0_TRGO</eq></td><td><eq>ITI1:TIMER1_TRGO</eq></td><td><eq>ITI2:TIMER2_TRGO</eq></td><td><eq>ITI3:TIMER7_TRGO</eq></td></tr><tr><td>TIMER4</td><td><eq>ITI0:TIMER1_TRGO</eq></td><td><eq>ITI1:TIMER2_TRGO</eq></td><td><eq>ITI2:TIMER3_TRGO</eq></td><td><eq>ITI3:TIMER7_TRGO</eq></td></tr><tr><td rowspan="2">(3)</td><td>TIMER8</td><td><eq>ITI0:TIMER1_TRGO</eq></td><td><eq>ITI1:TIMER2_TRGO</eq></td><td><eq>ITI2:TIMER9_TRGO</eq></td><td><eq>ITI3:TIMER10_TRGO</eq></td></tr><tr><td>TIMER11</td><td><eq>ITI0:TIMER3_TRGO</eq></td><td><eq>ITI1:TIMER4_TRGO</eq></td><td><eq>ITI2:TIMER12_TRGO</eq></td><td><eq>ITI3:TIMER13_TRGO</eq></td></tr><tr><td>(4)</td><td>TIMER14</td><td><eq>ITI0:TIMER1_TRGO</eq></td><td><eq>ITI1:TIMER2_TRGO</eq></td><td><eq>ITI2:TIMER15_OC0</eq></td><td><eq>ITI3:TIMER16_OC0</eq></td></tr></table>


(5) 只有更新事件可以产生 DMA 请求。但是定时器 5 和定时6中没有 DMA 配置寄存器。



(6) 在互联型产品中，TIMER1 的 ITI1 由 AFIO 0 (AFIO_PCF0)中的 TIMER1ITI1_REMAP 位来决定


内部连接的信号源；

在非互联型产品中，TIMER1 的 ITI1 内部连接到 TIMER7_TRGO；

(7) 通过配置不同的输入重映射寄存器（TIMERx_IRMP）可配置不同的内部触发。

