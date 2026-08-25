## 24. VREF

## 24.1. 简介

MCU 有一个精准的内部参考电路，用于为 ADC/DAC 提供基准电压，或由连接到 VREF 引脚的片外电路使用。

## 24.2. 主要特征

精准的内部参考特性描述如下：

◼ 电压稳定，产品修整；

◼ 连接 V<sub>REF</sub>引脚至片外电路；

◼ 提供 2.5V/1.5V 参考电压（对于 GD32L233xx 只有 2.5V）。

## 24.3. 功能描述

通过将 VREF_CS 寄存器中的 VREFEN 位置 1 使能该精准的内部参考（在这之前需要将RCU_APB2EN 寄存器中的 SYSCFGEN 位置 1），产生 2.5V 参考电压并连接到 V<sub>REF</sub>引脚。当VREFEN 被禁用时，可将片外参考电压注入到 V<sub>REF</sub>引脚作为 ADC/DAC 的参考源。如果没有V<sub>REF</sub>引脚（请参阅数据手册），则 V<sub>REF</sub>连接到 V<sub>DDA</sub>，VREFEN 位必须保持 0。

当使用精准的内部参考电压时，建议连接一个 1uF（或 1uF 和 10nF 并联）的旁路电容，并接地。


图 24-1. GD32L233xx VREF 连接


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/726192c0269727ffa78f7c755dc6d26d385b4e533eedf216a6424de772b96356.jpg)



图 24-2. GD32L235xx VREF 连接


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f446fced-1ad7-465d-97c1-5767905fbfdc/98910d85f3c3e3f08d1f5be5964d95c3c555982d4782416915a9a4c266e8a446.jpg)



根据 VREFEN 和 HIPM 位的配置，内部参考电压可以被配置成四种不同的模式。这些模式如下表所示：



表 24-1 VREF 模式


<table><tr><td>VREFEN</td><td>HIPM</td><td>模式</td></tr><tr><td>0</td><td>0</td><td>VREF 失能- <eq>V_{REF}</eq> 引脚下拉到 <eq>V_{SSA}</eq></td></tr><tr><td>0</td><td>1</td><td>外部参考电压模式:- VREF 失能- <eq>V_{REF}</eq> 引脚浮空</td></tr><tr><td>1</td><td>0</td><td>内部参考电压模式:- VREF 使能- <eq>V_{REF}</eq> 引脚连接到 VREF 输出</td></tr><tr><td>1</td><td>1</td><td>保持模式:- VREF 失能- <eq>V_{REF}</eq> 引脚浮空。通过外部电容保持电压- 失能 VREFRDY 位检测,VREFRDY 位保持最后一个状态</td></tr></table>


通过设置 VREFEN 位使能 VREF 和复位 VREF_CS 寄存器中的 HIPM 位后，用户必须等待VREFRDY 位置位，表明参考电压输出达到其期望值。

