## 16. 定时器（TIMERx）


表 16-1. 定时器（TIMERx）分为五种类型


<table><tr><td>定时器</td><td>定时器 0/7</td><td>定时器 1/2/3/4</td><td>定时器 8/11</td><td>定时器 9/10/12/13</td><td>定时器 5/6</td></tr><tr><td>类型</td><td>高级</td><td>通用(L0)</td><td>通用(L1)</td><td>通用(L2)</td><td>基本</td></tr><tr><td>预分频器</td><td>16 位</td><td>16 位</td><td>16 位</td><td>16 位</td><td>16 位</td></tr><tr><td>计数器</td><td>16 位</td><td>16 位</td><td>16 位</td><td>16 位</td><td>16 位</td></tr><tr><td>计数模式</td><td>向上,向下,中央对齐</td><td>向上,向下,中央对齐</td><td>只有向上</td><td>只有向上</td><td>只有向上</td></tr><tr><td>可重复性</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>捕获/比较通道数</td><td>4</td><td>4</td><td>2</td><td>1</td><td>0</td></tr><tr><td>互补和死区时间</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>中止输入</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>单脉冲</td><td>●</td><td>●</td><td>●</td><td>×</td><td>●</td></tr><tr><td>正交译码器</td><td>●</td><td>●</td><td>×</td><td>×</td><td>×</td></tr><tr><td>主-从管理</td><td>●</td><td>●</td><td>●</td><td>×</td><td>×</td></tr><tr><td>内部连接</td><td>●(1)</td><td>●(2)</td><td>●(3)</td><td>×</td><td>TRGO TO DAC</td></tr><tr><td>DMA</td><td>●</td><td>●</td><td>×</td><td>×</td><td>●(4)</td></tr><tr><td>Debug 模式</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

<table><tr><td rowspan="2">(1)</td><td>TIMER0</td><td>ITIO:TIMER4_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td>TIMER7</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER3_TRGO</td><td>ITI3:TIMER4_TRGO</td></tr><tr><td rowspan="4">(2)</td><td>TIMER1</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: 参考注释(5)</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td>TIMER2</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER4_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td>TIMER3</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER7_TRGO</td></tr><tr><td>TIMER4</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER3_TRGO</td><td>ITI3:TIMER7_TRGO</td></tr><tr><td rowspan="2">(3)</td><td>TIMER8</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER9_TRGO</td><td>ITI3:TIMER10_TRGO</td></tr><tr><td>TIMER11</td><td>ITIO: TIMER3_TRGO</td><td>ITI1: TIMER4_TRGO</td><td>ITI2: TIMER12_TRGO</td><td>ITI3:TIMER13_TRGO</td></tr></table>


(4) 只有更新事件可以产生 DMA 请求。但是定时器 5 和定时6 中没有 DMA 配置寄存器。



(5) 在互联型产品中，TIMER1 的 ITI1 由 AFIO 0 (AFIO_ PCF0)中的 TIMER1ITI1_REMAP 位来决定内部连接的信号源；



在非互联型产品中，TIMER1 的 ITI1 内部连接到 TIMER7_TRGO；


