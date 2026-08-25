## 26. 红外接口（IFRP）

## 26.1. 简介

红外接口(IFRP)用于控制红外光 LED，并发送红外数据实现红外遥控。

该模块没有寄存器，由 TIMER15 和 TIMER16 控制。通过将 GPIO 引脚设置为快速模式，可以将模块的输出提高到高电流容量。

## 26.2. 主要特性

 IFRP 输出信号是由 TIMER15_CH0 和 TIMER16_CH0 决定；

 为了得到正确的红外线信号，TIMER15 应产生低频调制包络信号，TIMER16 应产生高频载波信号；

 通过在 SYSCFG_CFG0 中设置 PB9FMPEN，IFRP 输出（PB9）可以控制 LED 接口。

## 26.3. 功能描述

IFRP 能够集成 TIMER15 和 TIMER16 的输出，以生成红外线信号。

1. 对 TIMER15 的 CH0 进行编程，产生低频 PWM 信号，即调制值信号。对 TIMER16 的 CH0进行编程，生成高频率 PWM 信号，即载波信号。在产生这些信号之前，信道需要被激活。

2. 设置 GPIO 重映射寄存器并使能 PIN。


图 26-1. IFRP 输出时序图 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/6fbd7dee70bbeeee94f48aa4228be6d4dc4c1c222405e000489aa1fec1c7debc.jpg)



注意: IFRP_OUT与TIMER16_CH0相比有一个APB时钟延迟。



图 26-2. IFRP 输出时序图 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/ab2c9e4376ecd8bf833eb5368150d5e24450402064c4bf1f0c879838ebd23977.jpg)



注意: 载波(TIMER15_CH0)的占空比可以改变，当TIMER15_CH0占空比较高时，IFRP_OUT与TIMER16_CH0呈反向关系。



图 26-3. IFRP 输出时序图 3


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/0cf2dc53c8a49458127df0b853284eba8688a4310d75e8e1e58905d73ba24ba6.jpg)



注意: IFRP_OUT将保持TIMER16_CH0的完整性，即使包络信号(TIMER15_CH0)不是活动的。

