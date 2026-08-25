## 18. 定时器（TIMER）


表 18-1. 定时器（TIMERx）分为六种类型


<table><tr><td>定时器</td><td>定时器0</td><td>定时器1/2</td><td>定时器8/11</td><td>定时器14/40</td><td>定时器5/6</td></tr><tr><td>类型</td><td>高级</td><td>通用L0</td><td>通用L1</td><td>通用L3</td><td>基本</td></tr><tr><td>预分频器</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数器</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数模式</td><td>向上,向下,中央对齐</td><td>向上,向下,中央对齐</td><td>只有向上</td><td>只有向上</td><td>只有向上</td></tr><tr><td>可重复性</td><td>●</td><td>×</td><td>×</td><td>●</td><td>×</td></tr><tr><td>捕获/比较通道数</td><td>4</td><td>4</td><td>2</td><td>2</td><td>0</td></tr><tr><td>互补和死区时间</td><td>3</td><td>×</td><td>×</td><td>1</td><td>×</td></tr><tr><td>中止输入</td><td>●</td><td>×</td><td>×</td><td>●</td><td>×</td></tr><tr><td>单脉冲</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>正交译码器</td><td>●</td><td>●</td><td>×</td><td>×</td><td>×</td></tr><tr><td>主-从管理</td><td>●</td><td>●</td><td>●</td><td>●</td><td>×</td></tr><tr><td>内部连接</td><td>●(1)</td><td>●(2)</td><td>●(3)</td><td>●(4)</td><td>TRGO TO DAC</td></tr><tr><td>DMA</td><td>●</td><td>●</td><td>×</td><td>●</td><td>●(5)</td></tr><tr><td>Debug模式</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

<table><tr><td>(1)</td><td>TIMER0</td><td>ITIO: TIMER14_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3: TIMER40_TRGO</td></tr><tr><td rowspan="2">(2)</td><td>TIMER1</td><td>ITIO: TIMER2_TRGO</td><td>ITI1: TIMER14_TRGO<eq>^{(6)}</eq></td><td>ITI2: TIMER40_TRGO<eq>^{(6)}</eq></td><td>ITI3: TIMER0_TRGO<eq>^{(6)}</eq></td></tr><tr><td>TIMER2</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER0_TRGO<eq>^{(6)}</eq></td><td>ITI2: TIMER14_TRGO<eq>^{(6)}</eq></td><td>ITI3: TIMER40_TRGO<eq>^{(6)}</eq></td></tr><tr><td rowspan="2">(3)</td><td>TIMER8</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER0_TRGO<eq>^{(6)}</eq></td><td>ITI3: TIMER14_TRGO<eq>^{(6)}</eq></td></tr><tr><td>TIMER11</td><td>ITIO: TIMER0_TRGO<eq>^{(6)}</eq></td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3: TIMER14_TRGO<eq>^{(6)}</eq></td></tr><tr><td rowspan="2">(4)</td><td>TIMER14</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER0_TRGO</td><td>ITI3: TIMER40_TRGO</td></tr><tr><td>TIMER40</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER14_TRGO</td><td>ITI3: TIMER0_TRGO</td></tr></table>


（5） 只有更新事件可以产生 DMA 请求。但是定时器 5 和定时6 中没有 DMA 配置寄存器。



（6） 只适用于 GD32L235。
