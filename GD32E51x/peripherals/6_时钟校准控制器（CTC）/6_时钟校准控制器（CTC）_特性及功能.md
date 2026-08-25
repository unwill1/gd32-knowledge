## 6. 时钟校准控制器（CTC）

## 6.1. 简介

时钟校准控制器（CTC）采用硬件的方式，自动校准内部 48MHz RC 晶振（IRC48M）。CTC模块基于外部高精度的参考信号源来校准 IRC48M 的时钟频率，通过自动的或手动的调整校准值，以得到一个精准的 IRC48M 时钟。

## 6.2. 主要特性

 两个外部参考信号源：GPIO（CTC_SYNC），LXTAL时钟；

 提供软件参考同步脉冲；

 硬件自动校准，无需软件操作；

 具有参考信号源捕获和重载功能的16 bits校准计数器；

 用于频率评估和自动校准的8 bits时钟校准基值；

 标志位和中断，用于指示时钟校准的状态：校准成功状态（CKOKIF），警告状态（CKWARNIF）和错误状态（ERRIF）。

## 6.3. 功能描述

CTC 模块的内部结构图如 6-1. CTC 。


图 6-1. CTC 简介


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/27e476be9219bb6a6cd7d1de67d3a2bd6c034838544ea579d0b0e56a2daf0587.jpg)


## 6.3.1. REF同步脉冲发生器

首先，通过设置 CTC_CTL1 寄存器中的 REFSEL 位来选择参考信号源：GPIO（CTC_SYNC）或者 LXTAL 时钟输出。

然后，可以通过设置 CTC_CTL1 寄存器中的 REFPOL 位来配置参考信号源同步时的信号极性，通过设置 CTC_CTL1 寄存器中的 REFPSC 位来产生一个合适的同步时钟频率信号。

如果需要使用软件参考脉冲信号，则需要设置 CTC_CTL0 寄存器中的 SWREFPUL 位为 1。软件参考脉冲信号与外部参考脉冲信号最后进行逻辑或操作。

## 6.3.2. CTC 校准计数器

CTC 时钟校准计数器由 CK_IRC48M 提供时钟。在置位 CTC_CTL0 寄存器中的 CNTEN 位后，当检测到第一个 REF 同步脉冲信号，计数器开始从 RLVALUE 值（RLVALUE 在 CTC_CTL1寄存器中定义）开始向下计数。每次检测到 REF 同步脉冲信号时，计数器重载 RLVALUE 值，同时重新开始向下计数。如果始终检测不到 REF 同步脉冲信号，计数器会向下计数到零，然后再向上计数到 128 x CKLIM（CKLIM 在 CTC_CTL1 中定义），最后停止，直到检测到下一个 REF 同步脉冲信号。一旦检测到 REF 同步脉冲信号，当前 CTC 校准计数器的计数值被捕获存入 CTC_STAT 寄存器中的 REFCAP 位，同时，当前计数器的计数方向被存入 CTC_STAT寄存器中的 REFDIR 位。详细内容如 6-2. CTC 所示。


图 6-2. CTC 校准计数器


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/29414bf1-8bb2-45c6-9aa0-8fcdb9c6beef/567f77616d168499443670d4f923b3f2ad41f6a374b037184146f746507bd107.jpg)


## 6.3.3. 频率评估和自动校准过程

当 REF 同步脉冲信号出现时，时钟频率评估功能开始执行。如果 REF 同步脉冲信号出现在计数器向下计数的过程中，说明当前时钟频率比期望时钟频率（频率为 48M）慢，需要增大CTC_CTL0 中的 TRIMVALUE 值（时钟校准值）。如果 REF 同步脉冲信号出现在计数器向上计数的过程中，说明当前时钟频率比期望时钟频率快，需要减小 TRIMVALUE 值。CTC_STAT中的 CKOKIF 位，CKWARNIF 位，CKERR 位和 REFMISS 位反映了频率评估的状态。

如果 CTC_CTL0 中的 AUTOTRIM（硬件自动校准模式）位置 1，硬件自动校准模式使能。在这个模式中，如果 REF 同步脉冲信号出现在计数器向下计数的过程中，说明当前时钟频率比期望时钟频率慢，CTC_CTL0 中的 TRIMVALUE 值会自动增大，来提高当前的时钟频率。反之，如果 REF 同步脉冲信号出现在计数器向上计数的过程中，说明当前时钟频率比期望时钟频率快，TRIMVALUE 值会自动减小，从而减小当前的时钟频率。

 Counter < CKLIM时，检测到REF同步脉冲信号；

CTC_STAT 中的 CKOKIF 位（时钟校准成功标志位）被置位，同时，如果 CTC_CTL0 中的CKOKIE 位（时钟校准完成中断使能位）置 1，将会产生一个中断。

如果 CTC_CTL0 中的 AUTOTRIM 置 1，CTC_CTL0 中的 TRIMVALUE 值不变。

 CKLIM ≤ Counter < 3 x CKLIM时，检测到REF同步脉冲信号；

CTC_STAT 中的 CKOKIF 位被置位，同时，如果 CTC_CTL0 中的 CKOKIE 位置 1，将会产生一个中断。

如果 CTC_CTL0 中的 AUTOTRIM 位置 1，在计数器向下计数过程中，CTC_CTL0 中的

TRIMVALUE 值将加 1，而在向上计数过程中将减 1。

 3 x CKLIM ≤ Counter < 128 x CKLIM时，检测到REF同步脉冲信号；

CTC_STAT 中的 CKWARNIF 位（时钟校准警告中断位）被置位，同时，如果 CTC_CTL0 中的 CKWARNIE 位（时钟校准警告中断使能位）置 1，将会产生一个中断。

如果 CTC_CTL0 中的 AUTOTRIM 位置 1，在计数器向下计数过程中，CTC_CTL0 中的TRIMVALUE 值将加 2，而在向上计数过程中将减 2。

 Counter ≥ 128 x CKLIM，计数器在向下计数过程中，检测到REF同步脉冲信号；

CTC_STAT 中的 CKERR 位（时钟校准错误位）被置位，同时，如果 CTC_CTL0 中的 ERRIE位（错误中断使能位）置 1，将会产生一个中断。

CTC_CTL0 中的 TRIMVALUE 值不变。

 Counter = 128 x CKLIM，计数器在向上计数过程中；

CTC_STAT 中的 REFMISS 位（REF 同步脉冲丢失位）被置位，同时，如果 CTC_CTL0 中的ERRIE位置 1，将会产生一个中断。

CTC_CTL0 中的 TRIMVALUE 值不变。

如果CTC_CTL0中的TRIMVALUE的校准值大于63，将会发生上溢事件，同时，若TRIMVALUE的校准值小于 0，将会发生下溢事件。TRIMVALUE 的取值范围为 0~63（上溢事件发生时，TRIMVALUE 值为 63；下溢事件发生时，TRIMVALUE 值为 0）。然后，CTC_STAT 中的TRIMERR 位（校准值错误位）将会被置位，如果 CTC_CTL0 中的 ERRIE 位置 1，将会产生一个中断。

## 6.3.4. 软件编程指南

CTC_CTL1 中 RLVALUE位和 CKLIM 位是时钟频率评估和硬件自动校准的关键。它们的数值由期望时钟的频率（IRC48M：48 MHz）和 REF 同步脉冲信号的频率计算得到。理想状态是REF 同步脉冲信号在 CTC 计数器计数到零时出现，所以 RLVALUE 的值为：

$$
\mathrm{RLVALUE} = \left(\mathrm{F} _ {\text { clock }} \div \mathrm{F} _ {\text { REzF }}\right) - 1\tag{6-1}
$$

CKLIM 的值由用户根据时钟的精度来设置，一般建议设为步长的一半，所以 CKLIM 的值为：

$$
\mathrm{CKLIM} = \left(\mathrm{F} _ {\text { clock }} \div \mathrm{F} _ {\text { REF }}\right) \times 0.12 \% \div 2\tag{6-2}
$$

典型的步长值是 0.12%， $\mathsf { F } _ { \mathsf { c l o c k } }$ 是期望时钟的频率（IRC48M）， $\mathsf { F } _ { \mathsf { R E F } }$ 是 REF 同步脉冲信号的频率。
