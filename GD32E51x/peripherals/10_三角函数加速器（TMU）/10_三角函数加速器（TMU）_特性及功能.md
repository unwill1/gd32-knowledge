## 10. 三角函数加速器（TMU）

## 10.1. 简介

三角函数加速器（TMU）是一个完全可配置的单元，可执行常见的三角运算和算术运算操作。TMU 总共有 9 种运算操作，其操作数据必须符合 IEEE-32 位单精度浮点格式。

## 10.2. 主要特性

 输入数据和计算结果支持32位单精度浮点格式；

 9种不同的操作模式；


表 10-1. 9 种不同的操作模式


<table><tr><td>模式</td><td>操作</td></tr><tr><td>0</td><td><eq>R0 = x * 2\pi</eq></td></tr><tr><td>1</td><td><eq>R0 = x/2\pi</eq></td></tr><tr><td>2</td><td><eq>R0 = \sqrt{x}</eq></td></tr><tr><td>3</td><td><eq>R0 = \sin(x)</eq></td></tr><tr><td>4</td><td><eq>R0 = \cos(x)</eq></td></tr><tr><td>5</td><td><eq>R0 = \arctan(x)</eq></td></tr><tr><td>6</td><td><eq>R0 = \text{Ratio of X &amp; Y, } R1 = \text{Quadrant value (0.0, ±0.25, ±0.5)}</eq></td></tr><tr><td>7</td><td><eq>R0 = x/y</eq></td></tr><tr><td>8</td><td><eq>R0 = \sqrt{x^2 + y^2}</eq></td></tr></table>

 对于模式0和模式1，完成计算操作需要4个时钟周期，对于其他模式，则需要7个时钟周期；

 可读取状态寄存器中的上溢和下溢错误标志；

 具有可选择使能的计算操作完成中断；

## 10.3. 功能描述

## 10.3.1. TMU 结构图

TMU 模块结构图如 10-1. 所示。


图 10-1. 三角函数加速器模块结构图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/283a1295dbf26d56c0e84502415013e83683e068c99e4db50cce3a1ede63a5d4.jpg)


## 10.3.2. 数据格式

TMU 模块的操作数和计算结果的格式如表。数据格式必须满足 IEEE-32 位单精度浮点格式。


表 10-2. IEEE-32 位单精度浮点格式


<table><tr><td>S [31]</td><td>E [30:23]</td><td>M [22:0]</td><td>数值 (V)</td></tr><tr><td>0</td><td>0</td><td>0</td><td>零 (V = 0)</td></tr><tr><td>1</td><td>0</td><td>0</td><td>负零 (V = -0)</td></tr><tr><td>0 +ve1 -ve</td><td>0</td><td>non zero</td><td>非标准 (V=(-1)s*2(-126)*(0.M))</td></tr><tr><td>0 +ve1 -ve</td><td>1 to 254</td><td>0 to 0x7FFFFFF</td><td>正常范围(V=(-1)*2(E-127)*(1.M))</td></tr><tr><td>0</td><td>254</td><td>0x7FFFFFF</td><td>正最大值(V = +Max)</td></tr><tr><td>1</td><td>254</td><td>0x7FFFFFF</td><td>负最大值(V = -Max)</td></tr><tr><td>0</td><td>max=255</td><td>0</td><td>正无穷(V = +Infinity)</td></tr><tr><td>1</td><td>max=255</td><td>0</td><td>负无穷(V = -Infinity)</td></tr><tr><td>x</td><td>max=255</td><td>non zero</td><td>非数 (V = NaN)</td></tr></table>


TMU 的几种 IEEE浮点数值格式的处理如下：


负零：如果操作的结果是零，TMU 操作只产生一个正零（S=0，E=0，M=0），永远不会产生负零。TMU 将所以的负零操作视为零。

非标准数：TMU 将输入的非标准化操作数（E=0，M！=0）视为零（E=0，M=0）。TMU 操作从不生成非标准化值。

下溢：当计算结果的值太小，无法用给定的浮点格式表示时，会产生下溢。在这种情况下，返回零值。如果 TMU 操作生成下溢条件，则锁存下溢标志（UDRF）设置为 1。UDRF 标志将保持锁定状态，直到下一个新操作启动。

上溢：当计算结果的值太大，无法用给定的浮点格式表示时，会发生上溢。在这种情况下，返回正无穷大或负无穷大。如果 TMU 操作生成溢出条件，则锁存溢出标志（OVRF）设置为 1。OVRF 标志将保持锁定状态，直到下一个新操作开始。

舍入：IEEE 标准支持多种舍入格式。舍入对于 TMU 操作没有意义（舍入是实现中固有的）。因此，TMU 操作会忽略舍入模式。

无穷和非数（NaN）：对于所有的操作，TMU 都将输入一个 NaN 操作数 $\scriptstyle ( \mathsf { E } = \mathsf { m a x } , \mathsf { M } : = 0 )$ 视为无穷大（E=max，M=0）。TMU 操作永远不会生成 NaN 值，而是生成无穷大。

## 10.3.3. 模式 0

模式 0 的运算为 ${ \sf R } 0 = { \sf x } ^ { \star } 2 \pi$ 。x 为输入操作数据，R0 为计算结果。

此操作用于将单位值转换为弧度。在控制应用程序中将单位值表示标准化弧度。使用模式 0 将单位值转换为弧度时，则输入数据应满足[-1,1]的范围：


表 10-3. 模式 0 下单位值与弧度之间的转换


<table><tr><td>Per-unit</td><td>Radians</td></tr><tr><td>1.0</td><td>2π</td></tr><tr><td>0.0</td><td>0</td></tr><tr><td>-1.0</td><td>-2π</td></tr></table>

模式 0 下只有上溢（OVRF）标志位，且下溢标志位（UDRF）始终为零。上溢标志的产生条件如下：

如果浮点数格式表示的 R0 值太大（E>255）时，R0 等于正无穷或负无穷， ${ \mathsf { O V R F } } { = } 1$ 

## 10.3.4. 模式 1

模式 1 的运算为 ${ \sf R } 0 = { \sf x } / 2 ~ \pi$ ，x 为输入操作数据，R0 为计算结果。

此操作用于将弧度转换为单位值。单位值用于表示标准化弧度的控件中。如果模式 1 用于将弧度转换为单位值，则输入数据应满足[-2π, 2π]的范围。


表 10-4. 模式 1 下弧度与单位值之间的转换


<table><tr><td>Per-unit</td><td>Radians</td></tr><tr><td>1.0</td><td>2π</td></tr><tr><td>0.0</td><td>0</td></tr><tr><td>-1.0</td><td>-2π</td></tr></table>

模式 1 下只有下溢（UDRF）标志位，且上溢标志位（OVRF）始终为零。上溢标志的产生条件如下：

如果浮点数格式表示的 R0 值太小（E< 0）时， $\scriptstyle \mathsf { R 0 } = 0 . 0 , \mathsf { O V R F } = 1$ 

## 10.3.5. 模式 2

模式 2 的运算为 ${ \mathsf { R } } 0 = { \sqrt { \mathsf { X } } } { \mathrm { ~ c ~ } }$ 。x 为输入操作数据，R0 为计算结果。

模式 2 下只有上溢（OVRF）标志位，且下溢标志位（UDRF）始终为零。上溢标志的产生条件如下：

/* 检测输入数是否为负数 */

$$
\text { If } (x <   0. 0 \text {   or   } x = = - \text { Infinity }) \{
$$

```c
/* 返回 0 */
S = 0;
E = 0;
M = 0;
/*上溢标志位置 1 */
OVRF = 1;
}
If( x == +Infinity ) {
/*返回无穷*/
S = 0;
E = 255;
M = 0;
/*上溢标志位置 1 */
OVRF = 1;
}
```

## 10.3.6. 模式 3

模式 3 的操作等效以下操作：

1. 令 PerUnit 取输入操作数 x 的小数部分，即 PerUnit = fraction(x)。

2. $R0 = \sin(\text{PerUnit} * 2\pi)$ 。 

在应用时，弧度通常被标准化为-1.0 到 1.0 的范围，而 PerUnit * 2π 值的范围是(-2π, 2π)。

模式 3 下只使用输入操作数 x 的小数部分，因为正弦函数的周期为 2π，x 的整数部分对结果没有影响。

此模式既没有下溢标志（UDRF）也没有上溢标志（OVRF）。如果计算结果太小，则返回 0。

## 10.3.7. 模式 4

模式 4 的操作等效以下操作：

1. 令 PerUnit 取输入操作数 x 的小数部分，即 PerUnit = fraction(x)。

2. $R0 = \cos(\text{PerUnit} * 2\pi)$ 。 

在应用时，弧度通常被标准化为-1.0 到 1.0 的范围，而 PerUnit * 2π 值的范围是(-2π, 2π)。

模式 4 下只使用输入操作数 x 的小数部分，因为正弦函数的周期为 2π，x 的整数部分对结果没有影响。

此模式既没有 UDRF 也没有 OVRF。如果结果太小，则返回 0。

## 10.3.8. 模式 5

模式 5 用于计算给定值的反正切，并以单位值的形式返回结果： ${ \mathsf { R } } 0 = { \mathsf { P e r U n i t } } = \arctan ( \mathsf { x } ) / 2 \pi$ 。

该操作将输入值 x 的输入范围限制在[-1,1]之间。

超出此范围的值返回 0.125，如下表所示：


表 10-5. 模式 5 下输入的操作数与 R0 值的范围


<table><tr><td>x</td><td>Per Unit</td><td>Radians</td><td>R0 Value</td><td>OVRF</td></tr><tr><td>&gt;1.0</td><td>0.125</td><td>pi/4</td><td>0.125</td><td>1</td></tr><tr><td>1.0</td><td>0.125</td><td>pi/4</td><td>0.125</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-1.0</td><td>-0.125</td><td>-pi/4</td><td>-0.125</td><td>0</td></tr><tr><td>&lt;-1.0</td><td>-0.125</td><td>-pi/4</td><td>-0.125</td><td>1</td></tr></table>

模式 5 下只有上溢（OVRF）标志位，且下溢标志位（UDRF）始终为零。当输入的操作数 x 超出[-1,1]范围时，上溢标志位置位。

## 10.3.9. 模式 6

模式 6 操作与 arctan（x）一起用于计算整圆的 arctan(x)。整圆 $\mathsf { a r c t a n } ( \mathsf { x } ) = \mathsf { R } \mathsf { 1 } + \mathsf { a r c t a n } ( \mathsf { R } 0 )$ 。R0 和 R1 运算结果如下：

$$
X = x \text {value}.
$$

Y = y value. 

$$
R 0 = \text { Ratio   of } X \& Y.
$$

$$
R 1 = \text { Quadrant   value } (0. 0, \pm 0. 2 5, \pm 0. 5).
$$

此模式的运算规则如下：

$$
\text { If } ((\text { fabs } (Y) = = 0. 0) \& (\text { fabs } (X) = = 0. 0)) \{
$$

R1( Quadrant ) = 0.0; 

$$
R 0 (\text {   Ratio   }) = 0. 0;
$$

$$
\} \text { else   if   (  fabs(Y) <   = fabs(X)  )   \{}
$$

$$
R 0 (\text {   Ratio   }) = Y / X;
$$

$$
\text { If } (X > = 0. 0)
$$

$$
R 1 (\text {   Quadrant   }) = 0. 0;
$$

else { 

$$
\text { If } (Y > = 0. 0)
$$

```txt
R1( Quadrant ) = 0.5;
else
R1( Quadrant ) = -0.5;
}
} else {
R0( Ratio ) = -X / Y;
if( Y >= 0.0 )
R1( Quadrant ) = 0.25;
else
R1( Quadrant ) = -0.25;
} 
```

10-2. X Y R0 R1 展示了如何根据 X 与 Y 比值计算 R0 和 R1 的值。


图 10-2. 基于 X 与 Y 的比值计算 R0 和 R1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/d8ca71552a4e33fe6c49e1b3ef91bacd0364272eb6ebcd9174c20ba4ed3d55e4.jpg)



模式 6 下具有下溢标志（UDRF）和上溢标志（OVRF）。产生 UDRF 和 OVRF 的条件如下表：



表 10-6. 模式 6 下产生 UDRF 和 OVRF 的条件


<table><tr><td>Division(Ratio of X &amp; Y)</td><td>R0</td><td>OVRF</td><td>UDRF</td></tr><tr><td>0/0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0/Inf</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Inf/Inf</td><td>inf</td><td>0</td><td>1</td></tr><tr><td>Normal/Inf</td><td>0</td><td>0</td><td>1</td></tr></table>

## 10.3.10. 模式 7

模式 7 的运算为 R0 = x/y。x 和 y为输入操作数据，R0 为计算结果。

此模式下具有下溢标志（UDRF）和上溢标志（OVRF）。产生 UDRF 和 OVRF 的条件如下表：


表 10-7. 模式 7 下产生 UDRF 和 OVRF 的条件


<table><tr><td>Division( X/Y)</td><td>R0</td><td>OVRF</td><td>UDRF</td></tr><tr><td>0/0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0/Inf</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Inf/Normal</td><td>inf</td><td>1</td><td>0</td></tr><tr><td>Inf/0</td><td>inf</td><td>1</td><td>0</td></tr><tr><td>Inf/Inf</td><td>inf</td><td>0</td><td>1</td></tr><tr><td>Normal/0</td><td>inf</td><td>1</td><td>0</td></tr><tr><td>Normal/Inf</td><td>0</td><td>0</td><td>1</td></tr></table>

## 10.3.11. 模式 8

模式 8 的运算为 $R 0 = \sqrt { x ^ { 2 } + y ^ { 2 } }$ 。x 和 y为输入操作数据，R0 为计算结果。

此模式只有上溢（OVRF）标志位，且下溢标志位（UDRF）始终为零。上溢标志的产生条件如下：

如果浮点数格式表示的 R0 值太大（E>255）时，R0 等于正无穷或负无穷，OVRF=1。

## 10.4. 软件流程

建议使用以下步骤读取 TMU 结果：

1. 写入 TMU IDATA0 寄存器，如果模式为 6、7 或 8，需要再写入 TMU IDATA1 寄存器。

2. 配置操作模式和中断启用位，将 TMUEN 位置 1，开始计算。

3. 如果中断使能为 1，则在计算完成后立即产生中断，否则软件应轮询 TMUEN 位并等待TMUEN 位为 0。

4. 读取 TMU 数据 0 寄存器，如果模式为 6，也应读取 TMU 数据 1 寄存器。

5. 读取 UDRF 和 OVRF 位，确保没有错误发生。

TMU 程序指南如 10-3. TMU 所示。


图 10-3. TMU 软件流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/0800d6494fd33b7a997dce69b00d02eee79990432f5717eaa803285042472a4a.jpg)

