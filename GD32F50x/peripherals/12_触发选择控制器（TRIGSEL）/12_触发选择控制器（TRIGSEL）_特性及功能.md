## 12. 触发选择控制器（TRIGSEL）

## 12.1. 简介

触发选择控制器（TRIGSEL）可通过软件配置的方式，为各种外设选择触发输入信号。TRIGSEL提供了灵活的机制，可以为外设选择不同的触发输入。

使用 TRIGSEL，每个外设最多可以配置 3 路 TRIGSEL 输出作为该外设的触发输入信号。配置相应的触发选择寄存器，可以为外设的指定触发输入选择不同的触发信号。

## 12.2. 主要特征

 支持多达74个触发输入信号；

 每个外设都有专用的触发信号选择寄存器；

 TRIGSEL寄存器最多可以配置3个输出到外围设备;

 触发选择控制器的输入信号可来源于外部输入或外设输出；

 触发选择控制器的输出信号可输出到外部输出或者到外设输入。

## 12.3. 功能说明

支持触发源选择的外设均具有专用 TRIGSEL 寄存器，用来为该外设选择不同的触发输入源。每个TRIGSEL 寄存器可以配置 3 路输出，这些输出连接到外设的触发输入。每路输出均可从不同的触发输入源中选择。

12-1. TRGSEL 显示了 TRIGSEL 的主要组成结构。


图 12-1. TRGSEL 主要组成示例


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/e1a2984b-4cd4-4ea5-9f7e-b33be8bb93cc/3e837c702f1d67ea8536d8e1f46f7d79cdf5923a6b07305d109bc5d96343783c.jpg)


## 12.4. 内部连接

TRIGSEL 允许软件方式为外设选择触发输入。 12-1. 给出了触发输入寄存器的位域值对应的触发输入选择。


表 12-1.触发输入位域选择


<table><tr><td>位域名称</td><td>位域值</td><td>触发输入选择</td></tr><tr><td rowspan="14">INSELx</td><td>0x00</td><td><eq>V_{ss}</eq></td></tr><tr><td>0x01</td><td><eq>V_{DD}</eq></td></tr><tr><td>0x02</td><td>TRIGSEL_IN0</td></tr><tr><td>0x03</td><td>TRIGSEL_IN1</td></tr><tr><td>0x04</td><td>TRIGSEL_IN2</td></tr><tr><td>0x05</td><td>TRIGSEL_IN3</td></tr><tr><td>0x06</td><td>TRIGSEL_IN4</td></tr><tr><td>0x07</td><td>TRIGSEL_IN5</td></tr><tr><td>0x08</td><td>TRIGSEL_IN6</td></tr><tr><td>0x09</td><td>TRIGSEL_IN7</td></tr><tr><td>0x0a</td><td>TIMER0_TRGO</td></tr><tr><td>0x0b</td><td>TIMER0_CH0</td></tr><tr><td>0x0c</td><td>TIMER0_CH1</td></tr><tr><td>0x0d0x0e</td><td>TIMER0_CH2TIMER0_CH3</td></tr><tr><td rowspan="36"></td><td>0x0f</td><td>TIMER7_TRGO</td></tr><tr><td>0x10</td><td>TIMER7_CH0</td></tr><tr><td>0x11</td><td>TIMER7_CH1</td></tr><tr><td>0x12</td><td>TIMER7_CH2</td></tr><tr><td>0x13</td><td>TIMER7_CH3</td></tr><tr><td>0x14</td><td>TIMER5_TRGO</td></tr><tr><td>0x15</td><td>TIMER6_TRGO</td></tr><tr><td>0x16</td><td>TIMER1_TRGO</td></tr><tr><td>0x17</td><td>TIMER1_CH0</td></tr><tr><td>0x18</td><td>TIMER1_CH1</td></tr><tr><td>0x19</td><td>TIMER1_CH2</td></tr><tr><td>0x1a</td><td>TIMER1_CH3</td></tr><tr><td>0x1b</td><td>TIMER2_TRGO</td></tr><tr><td>0x1c</td><td>TIMER2_CH0</td></tr><tr><td>0x1d</td><td>TIMER2_CH1</td></tr><tr><td>0x1e</td><td>TIMER2_CH2</td></tr><tr><td>0x1f</td><td>TIMER2_CH3</td></tr><tr><td>0x20</td><td>TIMER3_TRGO</td></tr><tr><td>0x21</td><td>TIMER3_CH0</td></tr><tr><td>0x22</td><td>TIMER3_CH1</td></tr><tr><td>0x23</td><td>TIMER3_CH2</td></tr><tr><td>0x24</td><td>TIMER3_CH3</td></tr><tr><td>0x25</td><td>TIMER4_TRGO</td></tr><tr><td>0x26</td><td>TIMER4_CH0</td></tr><tr><td>0x27</td><td>TIMER4_CH1</td></tr><tr><td>0x28</td><td>TIMER4_CH2</td></tr><tr><td>0x29</td><td>TIMER4_CH3</td></tr><tr><td>0x2f</td><td>TIMER15_TRGO</td></tr><tr><td>0x30</td><td>TIMER15_CH0</td></tr><tr><td>0x31</td><td>TIMER15_CH1</td></tr><tr><td>0x32</td><td>TIMER15_MCH0</td></tr><tr><td>0x33</td><td>TIMER16_TRGO</td></tr><tr><td>0x34</td><td>TIMER16_CH0</td></tr><tr><td>0x35</td><td>TIMER16_CH1</td></tr><tr><td>0x36</td><td>TIMER16_MCH0</td></tr><tr><td>0x37</td><td>ADC0_WD0_OUT</td></tr><tr><td rowspan="23"></td><td>0x38</td><td>保留</td></tr><tr><td>0x39</td><td>保留</td></tr><tr><td>0x3a</td><td>ADC1_WD0_OUT</td></tr><tr><td>0x3b</td><td>保留</td></tr><tr><td>0x3c</td><td>保留</td></tr><tr><td>0x3d</td><td>ADC2_WD0_OUT</td></tr><tr><td>0x3e</td><td>保留</td></tr><tr><td>0x3f</td><td>保留</td></tr><tr><td>0x40</td><td>CMP0_OUT</td></tr><tr><td>0x41</td><td>CK_OUT</td></tr><tr><td>0x42</td><td>TIMER0_BKIN</td></tr><tr><td>0x43</td><td>TIMER0_CH0BKIN</td></tr><tr><td>0x44</td><td>TIMER0_CH1BKIN</td></tr><tr><td>0x45</td><td>TIMER0_CH2BKIN</td></tr><tr><td>0x46</td><td>TIMER7_BKIN</td></tr><tr><td>0x47</td><td>TIMER7_CH0BKIN</td></tr><tr><td>0x48</td><td>TIMER7_CH1BKIN</td></tr><tr><td>0x49</td><td>TIMER7_CH2BKIN</td></tr><tr><td>0x4a</td><td>TIMER15_BKIN</td></tr><tr><td>0x4b</td><td>TIMER16_BKIN</td></tr><tr><td>0x4c</td><td>EXTI9</td></tr><tr><td>0x4d</td><td>EXTI11</td></tr><tr><td>0x4e</td><td>EXTI15</td></tr></table>


如 12-2. TRIGSEL 所示，表明了 TRIGSEL 输入输出之间的连接关系。通过TRIGSEL 寄存器的 INSELx[7:0]位域，可以给 TRIGSEL 的输出选择一个输入触发源。每个TRIGSEL 寄存器可以配置 3 路输出，这些输出连接到对应的外设。



表 12-2. TRIGSEL 输入输出映射关系


<table><tr><td>触发源</td><td>触发选择</td><td>TRIGSEL 寄存器</td><td>TRIGSEL输出</td><td>外设</td></tr><tr><td>0</td><td rowspan="8">INSELx[7:0]</td><td rowspan="4">TRIGSEL_EXTOUT0</td><td>输出 0</td><td>TRIGSEL_OUT0</td></tr><tr><td>1</td><td rowspan="3">输出 1</td><td rowspan="3">TRIGSEL_OUT1</td></tr><tr><td>TRIGSEL_IN0</td></tr><tr><td>TRIGSEL_IN1</td></tr><tr><td>TRIGSEL_IN2</td><td rowspan="4">TRIGSEL_EXTOUT1</td><td>输出 0</td><td>TRIGSEL_OUT2</td></tr><tr><td>TRIGSEL_IN3</td><td rowspan="3">输出 1</td><td rowspan="3">TRIGSEL_OUT3</td></tr><tr><td>TRIGSEL_IN4</td></tr><tr><td>TRIGSEL_IN5</td></tr><tr><td>TRIGSEL_IN6</td><td></td><td rowspan="4">TRIGSEL_EXTOUT2</td><td rowspan="4">输出0输出1</td><td rowspan="4">TRIGSEL_OUT4TRIGSEL_OUT5</td></tr><tr><td>TRIGSEL_IN7</td><td></td></tr><tr><td>TIMER0_TRGO</td><td></td></tr><tr><td>TIMER0_CH0</td><td></td></tr><tr><td>TIMER0_CH1</td><td></td><td rowspan="3">TRIGSEL_EXTOUT3</td><td rowspan="3">输出0输出1</td><td rowspan="3">TRIGSEL_OUT6TRIGSEL_OUT7</td></tr><tr><td>TIMER0_CH2</td><td></td></tr><tr><td>TIMER0_CH3</td><td></td></tr><tr><td>TIMER7_TRGO</td><td></td><td rowspan="5">TRIGSEL_TIMER0ITI</td><td rowspan="5">输出0</td><td rowspan="5">TIMER0_ITI</td></tr><tr><td>TIMER7_CH0</td><td></td></tr><tr><td>TIMER7_CH1</td><td></td></tr><tr><td>TIMER7_CH2</td><td></td></tr><tr><td>TIMER7_CH3</td><td></td></tr><tr><td>TIMER5_TRGO</td><td></td><td rowspan="3">TRIGSEL_TIMER1ITI</td><td rowspan="3">输出0</td><td rowspan="3">TIMER1_ITI</td></tr><tr><td>TIMER6_TRGO</td><td></td></tr><tr><td>TIMER1_TRGO</td><td></td></tr><tr><td>TIMER1_CH0</td><td></td><td rowspan="4">TRIGSEL_TIMER2ITI</td><td rowspan="4">输出0</td><td rowspan="4">TIMER2_ITI</td></tr><tr><td>TIMER1_CH1</td><td></td></tr><tr><td>TIMER1_CH2</td><td></td></tr><tr><td>TIMER1_CH3</td><td></td></tr><tr><td>TIMER2_TRGO</td><td></td><td rowspan="5">TRIGSEL_TIMER3ITI</td><td rowspan="5">输出0</td><td rowspan="5">TIMER3_ITI</td></tr><tr><td>TIMER2_CH0</td><td></td></tr><tr><td>TIMER2_CH1</td><td></td></tr><tr><td>TIMER2_CH2</td><td></td></tr><tr><td>TIMER2_CH3</td><td></td></tr><tr><td>TIMER3_TRGO</td><td></td><td rowspan="5">TRIGSEL_TIMER4ITI</td><td rowspan="5">输出0</td><td rowspan="5">TIMER4_ITI</td></tr><tr><td>TIMER3_CH0</td><td></td></tr><tr><td>TIMER3_CH1</td><td></td></tr><tr><td>TIMER3_CH2</td><td></td></tr><tr><td>TIMER3_CH3</td><td></td></tr><tr><td>TIMER4_TRGO</td><td></td><td rowspan="4">TRIGSEL_TIMER7ITI</td><td rowspan="4">输出0</td><td rowspan="4">TIMER7_ITI</td></tr><tr><td>TIMER4_CH0</td><td></td></tr><tr><td>TIMER4_CH1</td><td></td></tr><tr><td>TIMER4_CH2</td><td></td></tr><tr><td>TIMER4_CH3</td><td></td><td rowspan="3">TRIGSEL_TIMER15ITI</td><td rowspan="3">输出0</td><td rowspan="3">TIMER15_ITI</td></tr><tr><td>TIMER15_TRGO</td><td></td></tr><tr><td>TIMER15_CH0</td><td></td></tr><tr><td>TIMER15_CH1</td><td></td><td rowspan="3">TRIGSEL_TIMER16I TI</td><td rowspan="3">输出 0</td><td rowspan="3">TIMER16_ITI</td></tr><tr><td>TIMER15_MCH0</td><td></td></tr><tr><td>TIMER16_TRGO</td><td></td></tr><tr><td>TIMER16_CH0</td><td></td><td rowspan="5">TRIGSEL_DAC</td><td rowspan="5">输出 0</td><td rowspan="5">DAC0_OUT_EXTRG</td></tr><tr><td>TIMER16_CH1</td><td></td></tr><tr><td>TIMER16_MCH0</td><td></td></tr><tr><td>ADC0_WD0_OUT</td><td></td></tr><tr><td>ADC1_WD0_OUT</td><td></td></tr><tr><td>ADC2_WD0_OUT</td><td></td><td rowspan="3">TRIGSEL_ADC0_RO UTRG</td><td rowspan="3">输出 0</td><td rowspan="3">ADC0_ROUTRG</td></tr><tr><td>CMP0_OUT</td><td></td></tr><tr><td>CK_OUT</td><td></td></tr><tr><td>TIMER0_BKIN</td><td></td><td rowspan="4">TRIGSEL_ADC0_INS TRG</td><td rowspan="4">输出 0</td><td rowspan="4">ADC0_INSTRG</td></tr><tr><td>TIMER0_CH0BKIN</td><td></td></tr><tr><td>TIMER0_CH1BKIN</td><td></td></tr><tr><td>TIMER0_CH2BKIN</td><td></td></tr><tr><td>TIMER7_BKIN</td><td></td><td rowspan="5">TRIGSEL_ADC1_RO UTRG</td><td rowspan="5">输出 0</td><td rowspan="5">ADC1_ROUTRG</td></tr><tr><td>TIMER7_CH0BKIN</td><td></td></tr><tr><td>TIMER7_CH1BKIN</td><td></td></tr><tr><td>TIMER7_CH2BKIN</td><td></td></tr><tr><td>TIMER15_BKIN</td><td></td></tr><tr><td>TIMER16_BKIN</td><td></td><td rowspan="4">TRIGSEL_ADC1_INS TRG</td><td rowspan="4">输出 0</td><td rowspan="4">ADC1_INSTRG</td></tr><tr><td>EXTI9</td><td></td></tr><tr><td>EXTI11</td><td></td></tr><tr><td>EXTI15</td><td></td></tr><tr><td></td><td></td><td>TRIGSEL_ADC2_RO UTRG</td><td>输出 0</td><td>ADC2_ROUTRG</td></tr><tr><td></td><td></td><td>TRIGSEL_ADC2_INS TRG</td><td>输出 0</td><td>ADC2_INSTRG</td></tr><tr><td></td><td></td><td>TRIGSEL_TIMER0BR KIN</td><td>输出 0</td><td>TIMER0_BRKIN</td></tr><tr><td rowspan="5"></td><td rowspan="5"></td><td>TRIGSEL_TIMER0CHBRKIN</td><td>输出 0输出 1输出 2</td><td>TIMER0_CH0BRKINTIMER0_CH1BRKINTIMER0_CH2BRKIN</td></tr><tr><td>TRIGSEL_TIMER7BRKIN</td><td>输出 0</td><td>TIMER7_BRKIN</td></tr><tr><td>TRIGSEL_TIMER7CHBRKIN</td><td>输出 0输出 1输出 2</td><td>TIMER7_CH0BRKINTIMER7_CH1BRKINTIMER7_CH2BRKIN</td></tr><tr><td>TRIGSEL_TIMER15BRKIN</td><td>输出 0</td><td>TIMER15_BRKIN</td></tr><tr><td>TRIGSEL_TIMER16BRKIN</td><td>输出 0</td><td>TIMER16_BRKIN</td></tr></table>


注意：



1. TRIGSEL_OUTx (x=0,…,7) 不能选择任何 TRIGSEL_INy $( \mathsf { y } { = } 0 , . . . , 7 )$ 作为触发源。



2. TIMERx_ITI $( \mathsf { x } { = } 0 , \ldots , 4 , 7 )$ 不能选择来自其自身模块的信号 (TIMERx_TRGO \ TIMERx_CH0\ TIMERx_CH1 \ TIMERx_CH2 \ TIMERx_CH3) 作为触发源，TIMERx_ITI (x= 15,16) 不能选 择 来 自 其 自 身 模 块 的 信 号 (TIMERx_TRGO \ TIMERx_CH0 \ TIMERx_CH1 \TIMERx_MCH0) 作为触发源。



3. 除1、2所述之外，所有输出都可以选择所有输入作为触发源。



触发输入选择 INSELx[7:0]位域值配置为 0x00 时，TRIGSEL 触发输入选择为低电平；配置为 0x01时，TRIGSEL 触发输入选择为高电平。当选择了非法触发输入时，其输出将被强制选择为 0。

