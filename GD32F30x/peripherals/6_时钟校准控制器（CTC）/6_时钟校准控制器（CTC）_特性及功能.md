## 6. 时钟校准控制器（CTC）

## 6.1. 简介

时钟校准控制器（CTC）采用硬件的方式，自动校准内部48MHz RC晶振（IRC48M）。CTC模块基于外部高精度的参考信号源来校准IRC48M的时钟频率，通过自动的或手动的调整校准值，以得到一个精准的IRC48M时钟。

## 6.2. 主要特性

■ 两个外部参考信号源：GPIO（CTC_SYNC），LXTAL时钟；

■ 提供软件参考同步脉冲；

■ 硬件自动校准，无需软件操作；

■ 具有参考信号源捕获和重载功能的16 bits校准计数器；

■ 用于频率评估和自动校准的8 bits时钟校准基值；

■ 标志位和中断，用于指示时钟校准的状态：校准成功状态（CKOKIF），警告状态（CKWARNIF）和错误状态（ERRIF）。

## 6.3. 功能描述

CTC模块的内部结构图如图6-1. CTC简介。


图 6-1. CTC 简介


![image](images/04a63a003d9e.jpg)


## 6.3.1. REF 同步脉冲发生器

首先，通过设置CTC_CTL1寄存器中的REFSEL位来选择参考信号源：GPIO（CTC_SYNC），LXTAL时钟输出。

然后，可以通过设置CTC_CTL1寄存器中的REFPOL位来配置参考信号源同步时的信号极性，通过设置CTC_CTL1寄存器中的REFPSC位来产生一个合适的同步时钟频率信号。

如果需要使用软件参考脉冲信号，则需要设置CTC_CTL0寄存器中的SWREFPUL位为1。软件参考脉冲信号与外部参考脉冲信号最后进行逻辑或操作。

## 6.3.2. CTC 校准计数器

CTC时钟校准计数器由CK_IRC48M提供时钟。在置位CTC_CTL0寄存器中的CNTEN位后，当检测到第一个REF同步脉冲信号，计数器开始从RLVALUE值（RLVALUE在CTC_CTL1寄存器中定义）开始向下计数。每次检测到REF同步脉冲信号时，计数器重载RLVALUE值，同时重新开始向下计数。如果始终检测不到REF同步脉冲信号，计数器会向下计数到零，然后再向上计数到128 x CKLIM（CKLIM在CTC_CTL1中定义），最后停止，直到检测到下一个REF同步脉冲信号。一旦检测到REF同步脉冲信号，当前CTC校准计数器的计数值被捕获存入CTC_STAT寄存器中的REFCAP位，同时，当前计数器的计数方向被存入CTC_STAT寄存器中的REFDIR位。详细内容如图6-2.CTC校准计数器所示。


图 6-2. CTC 校准计数器


![image](images/8287a0fe421c.jpg)


## 6.3.3. 频率评估和自动校准过程

当REF同步脉冲信号出现时，时钟频率评估功能开始执行。如果REF同步脉冲信号出现在计数器向下计数的过程中，说明当前时钟频率比期望时钟频率（频率为48M）慢，需要增大CTC_CTL0中的TRIMVALUE值（时钟校准值）。如果REF同步脉冲信号出现在计数器向上计数的过程中，说明当前时钟频率比期望时钟频率快，需要减小TRIMVALUE值。CTC_STAT中的CKOKIF位，CKWARNIF位，CKERR位和REFMISS位反映了频率评估的状态。

如果CTC_CTL0中的AUTOTRIM（硬件自动校准模式）位置1，硬件自动校准模式使能。在这个模式中，如果REF同步脉冲信号出现在计数器向下计数的过程中，说明当前时钟频率比期望时钟频率慢，CTC_CTL0中的TRIMVALUE值会自动增大，来提高当前的时钟频率。反之，如果REF同步脉冲信号出现在计数器向上计数的过程中，说明当前时钟频率比期望时钟频率快，TRIMVALUE值会自动减小，从而减小当前的时钟频率。

Counter < CKLIM时，检测到REF同步脉冲信号；

CTC_STAT中的CKOKIF位（时钟校准成功标志位）被置位，同时，如果CTC_CTL0中的CKOKIE位（时钟校准完成中断使能位）置1，将会产生一个中断。

如果CTC_CTL0中的AUTOTRIM置1，CTC_CTL0中的TRIMVALUE值不变。

■ CKLIM ≤ Counter < 3 x CKLIM时，检测到REF同步脉冲信号；

CTC_STAT中的CKOKIF位被置位，同时，如果CTC_CTL0中的CKOKIE位置1，将会产生

一个中断。

如果CTC_CTL0中的AUTOTRIM位置1，在计数器向下计数过程中，CTC_CTL0中的TRIMVALUE值将加1，而在向上计数过程中将减1。

■ 3 x CKLIM ≤ Counter < 128 x CKLIM时，检测到REF同步脉冲信号；

CTC_STAT中的CKWARNIF位（时钟校准警告中断位）被置位，同时，如果CTC_CTL0中的CKWARNIE位（时钟校准警告中断使能位）置1，将会产生一个中断。

如果CTC_CTL0中的AUTOTRIM位置1，在计数器向下计数过程中，CTC_CTL0中的TRIMVALUE值将加2，而在向上计数过程中将减2。

Counter ≥ 128 x CKLIM，计数器在向下计数过程中，检测到REF同步脉冲信号；

CTC_STAT中的CKERR位（时钟校准错误位）被置位，同时，如果CTC_CTL0中的ERRIE位（错误中断使能位）置1，将会产生一个中断。

CTC_CTL0中的TRIMVALUE值不变。

Counter = 128 x CKLIM，计数器在向上计数过程中；

CTC_STAT中的REFMISS位（REF同步脉冲丢失位）被置位，同时，如果CTC_CTL0中的ERRIE位置1，将会产生一个中断。

CTC_CTL0中的TRIMVALUE值不变。

如果CTC_CTL0中的TRIMVALUE的校准值大于63，将会发生上溢事件，同时，若TRIMVALUE的校准值小于0，将会发生下溢事件。TRIMVALUE的取值范围为0~63（上溢事件发生时，TRIMVALUE值为63；下溢事件发生时，TRIMVALUE值为0）。然后，CTC_STAT中的TRIMERR位（校准值错误位）将会被置位，如果CTC_CTL0中的ERRIE位置1，将会产生一个中断。

## 6.3.4. 软件编程指南

CTC_CTL1中RLVALUE位和CKLIM位是时钟频率评估和硬件自动校准的关键。它们的数值由期望时钟的频率（IRC48M：48 MHz）和REF同步脉冲信号的频率计算得到。理想状态是REF同步脉冲信号在CTC计数器计数到零时出现，所以RLVALUE的值为：

$$
\text { RLVALUE } = \left(F _ {\text { clock }} \div F _ {\text { REzF }}\right) - 1 \tag {6-1}
$$

CKLIM的值由用户根据时钟的精度来设置，一般建议设为步长的一半，所以CKLIM的值为：

$$
\mathrm{CKLIM} = \left(\mathrm{F} _ {\text { clock }} \div \mathrm{F} _ {\text { REF }}\right) \times 0.12 \% \div 2 \tag{6 - 2}
$$

典型的步长值是 $0.12\%$ ， $\mathsf{F}_{\mathrm{clock}}$ 是期望时钟的频率（IRC48M）， $\mathsf{F}_{\mathrm{REF}}$ 是REF同步脉冲信号的频率。
