## 22. 定时器（TIMERx）


表 22-1. 定时器（TIMERx）分为五种类型


<table><tr><td>定时器</td><td>定时器 0/7</td><td>定时器 1~4</td><td>定时器 8/11</td><td>定时器 9/10/12/13</td><td>定时器 5/6</td></tr><tr><td>类型</td><td>高级</td><td>通用(L0)</td><td>通用(L1)</td><td>通用(L2)</td><td>基本</td></tr><tr><td>预分频器</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数器</td><td>16位</td><td>32位(定时器 1/4)16位(定时器 2/3)</td><td>16位</td><td>16位</td><td>16位</td></tr><tr><td>计数模式</td><td>向上,向下,中央对齐</td><td>向上,向下,中央对齐</td><td>只有向上</td><td>只有向上</td><td>只有向上</td></tr><tr><td>可重复性</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>捕获/比较通道数</td><td>4</td><td>4</td><td>2</td><td>1</td><td>0</td></tr><tr><td>互补和死区时间</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>中止输入</td><td>●</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>单脉冲</td><td>●</td><td>●</td><td>●</td><td>×</td><td>●</td></tr><tr><td>正交译码器</td><td>●</td><td>●</td><td>×</td><td>×</td><td>×</td></tr><tr><td>主-从管理</td><td>●</td><td>●</td><td>●</td><td>×</td><td>×</td></tr><tr><td>内部连接</td><td>●(1)</td><td>●(2)</td><td>●(3)</td><td>×</td><td>TRGO TO DAC</td></tr><tr><td>DMA</td><td>●</td><td>●</td><td>×</td><td>×</td><td>●(4)</td></tr><tr><td>Debug 模式</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

<table><tr><td rowspan="3">(1)</td><td>TIMER0</td><td>ITIO:TIMER4_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td>TIMER7</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER3_TRGO</td><td>ITI3:TIMER4_TRGO</td></tr><tr><td>TIMER1</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER7_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td rowspan="3">(2)</td><td>TIMER2</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER4_TRGO</td><td>ITI3:TIMER3_TRGO</td></tr><tr><td>TIMER3</td><td>ITIO: TIMER0_TRGO</td><td>ITI1: TIMER1_TRGO</td><td>ITI2: TIMER2_TRGO</td><td>ITI3:TIMER7_TRGO</td></tr><tr><td>TIMER4</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER3_TRGO</td><td>ITI3:TIMER7_TRGO</td></tr><tr><td rowspan="2">(3)</td><td>TIMER8</td><td>ITIO: TIMER1_TRGO</td><td>ITI1: TIMER2_TRGO</td><td>ITI2: TIMER9_TRGO</td><td>ITI3:TIMER10_TRGO</td></tr><tr><td>TIMER11</td><td>ITIO: TIMER3_TRGO</td><td>ITI1: TIMER4_TRGO</td><td>ITI2: TIMER12_TRGO</td><td>ITI3:TIMER13_TRGO</td></tr></table>


（4） 只有更新事件可以产生 DMA 请求。但是定时器 5 和定时6中没有 DMA 配置寄存器。

## 文件导航

| 类型 | 实例 | 特性及功能 | 寄存器 |
|---|---|---|---|
| 高级 | TIMER0/7 | [打开](22_TIMER_高级_特性及功能.md) | [打开](22_TIMER_高级_寄存器.md) |
| 通用L0 | TIMER1/2/3/4 | [打开](22_TIMER_通用L0_特性及功能.md) | [打开](22_TIMER_通用L0_寄存器.md) |
| 通用L1 | TIMER8/11 | [打开](22_TIMER_通用L1_特性及功能.md) | [打开](22_TIMER_通用L1_寄存器.md) |
| 通用L2 | TIMER9/10/12/13 | [打开](22_TIMER_通用L2_特性及功能.md) | [打开](22_TIMER_通用L2_寄存器.md) |
| 基本 | TIMER5/6 | [打开](22_TIMER_基本_特性及功能.md) | [打开](22_TIMER_基本_寄存器.md) |
