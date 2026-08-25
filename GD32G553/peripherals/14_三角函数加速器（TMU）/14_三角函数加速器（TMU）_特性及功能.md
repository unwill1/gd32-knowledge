## 14. 三角函数加速器（TMU）

## 14.1. 简介

三角函数加速器（TMU）是一个完全可配置的单元，可执行常见的三角运算和算术运算操作。TMU可以减轻 CPU 的负担，通常应用于电机控制，信号处理和很多其他应用场景。

TMU 可以计算 10 种函数，输入和输出数据支持 q1.31、q1.15 定点格式和 IEEE754 32 位单精度浮点格式。

## 14.2. 主要特征

 10 种函数；

 中断和 DMA 请求；

 可配置的数据格式：q1.31、q1.15 定点格式和 IEEE754 32 位单精度浮点格式；

 可编程的计算精度；

 CORDIC 算法核：支持两种圆周系统和双曲线系统，支持旋转模式和向量模式。

## 14.3. 结构框图

14-1. TMU TMU 模块内部结构细节。


图 14-1. TMU 模块结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/28bf4b71788b18eeb7815833e000eac77bfbf5d9c217332bee31399bea04f4d7.jpg)


预处理模块将输入数据寄存器（TMU_IDATA）中的数据进行转换，得到 CORDIC 算法核需要的初始数据 $( \mathsf { x } _ { 0 } , \mathsf { y } _ { 0 } , \mathsf { z } _ { 0 } )$ 。输入数据寄存器中的数据格式为 q1.31、q1.15 定点格式或 IEEE754 32 位单精度浮点格式。

CORDIC 算法核心模块根据初始数据 $( \mathsf { x } _ { 0 } , \mathsf { y } _ { 0 } , \mathsf { z } _ { 0 } )$ ，经过迭代和运算，得到 $( \mathsf { x } _ { \mathsf { n } } , \mathsf { y } _ { \mathsf { n } } , z _ { \mathsf { n } } )$ 。TMU 算法核心

模块支持圆周系统和双曲线系统，每种系统支持旋转模式和向量模式。

后处理模块对 $( \mathsf { x } _ { \mathsf { n } } , \mathsf { y } _ { \mathsf { n } } , \mathsf { z } _ { \mathsf { n } } )$ 进行数据转换和缩放等处理，并将处理后的数据写入输出数据寄存器（TMU_ODATA）。输出数据寄存器中的数据格式为 q1.31、q1.15 定点格式或 IEEE754 32 位单精度浮点格式。

## 14.4. 功能描述

## 14.4.1. 数据格式和配置

当 IFLTEN / OFLTEN 位复位时，TMU 模块的输入/输出数据是定点有符号整型格式（q1.31、q1.15格式）。当 IFLTEN / OFLTEN 位置位时，TMU 模块的输入/输出数据是 IEEE754 32 位单精度浮点格式。

q1.31 格式中，第 31 位是符号位，0~30 位是小数位，表达数值范围是[-1,1-2<sup>-31</sup>]，对应[0x80000000,0x7FFFFFFF]。

q1.15 格式中，第 15 位是符号位，0~14 位是小数位，表达数值范围是[-1,1-2<sup>-15</sup>]，对应[0x8000,0x7FFF]。

IEEE754 32 位单精度浮点格式的数据范围如 14-3. IEEE754 32 所示。

当输入数据格式为定点时（IFLTEN=0），可以通过 TMU_CS寄存器中的 IWIDTH 位配置输入数据的定点格式。当输入数据格式为浮点时（IFLTEN=1），IWIDTH 位的配置无效。每个模式需要的输入数据的个数有所不同（例如，模式 0 需要两个输入数据，模式 5 只需要一个），可以通过 TMU_CS寄存器的 INUM 位配置输入数据的数量。详细配置参考 14-1. 。

注意：当输入数据配置为 q1.15 格式，如果所配模式需要两个输入数据，只需要写一次 TMU_IDATA寄存器，第一个输入数据在低半字，第二个输入数据在高半字。如果所配模式只需要一个输入数据，则只使用低半字，高半字的不使用。


表 14-1. 输入数据配置


<table><tr><td>IWIDTH 位</td><td>INUM 位</td><td>IFLTEN 位</td><td>数据格式</td><td>写 TMU_IDATA 寄存器</td></tr><tr><td>0</td><td>0</td><td>0</td><td>q1.31 定点</td><td>写一次</td></tr><tr><td>0</td><td>1</td><td>0</td><td>q1.31 定点</td><td>连续写两次</td></tr><tr><td>1</td><td>0</td><td>0</td><td>q1.15 定点</td><td>写一次</td></tr><tr><td>1</td><td>1</td><td>0</td><td>q1.15 定点</td><td>不可用</td></tr><tr><td>X</td><td>0</td><td>1</td><td rowspan="2">IEEE754 32 位单精度浮点</td><td>写一次</td></tr><tr><td>X</td><td>1</td><td>1</td><td>连续写两次</td></tr></table>

当输出数据格式为定点时（OFLTEN=0），可以通过 TMU_CS寄存器的 OWIDTH位配置输出数据的定点格式。当输出数据格式为浮点时（OFLTEN=1），OWIDTH 位的配置无效。每个模式的输出数据的个数有所不同（例如，模式 0 有两个输出数据，模式 8 只有一个），可以通过 TMU_CS 寄存器的 ONUM 位配置输出数据的数量。详细配置参考 14-2. 。

注意：当输出数据配置为 q1.15格式，如果所配模式有两个输出数据，只需要读一次 TMU_ODATA寄存器。第一个输出数据在低半字，第二个输出数据在高半字。如果所配模式只有一个输出，则只使用低半字，不使用高半字。


表 14-2. 输出数据配置


<table><tr><td>OWIDTH 位</td><td>ONUM 位</td><td>OFLTEN 位</td><td>数据格式</td><td>读 TMU_ODATA 寄存器</td></tr><tr><td>0</td><td>0</td><td>0</td><td>q1.31 定点</td><td>读一次</td></tr><tr><td>0</td><td>1</td><td>0</td><td>q1.31 定点</td><td>连续读两次</td></tr><tr><td>1</td><td>0</td><td>0</td><td>q1.15 定点</td><td>读一次</td></tr><tr><td>1</td><td>1</td><td>0</td><td>q1.15 定点</td><td>不可用</td></tr><tr><td>X</td><td>0</td><td>1</td><td rowspan="2">IEEE754 32 位单精度浮点</td><td>读一次</td></tr><tr><td>X</td><td>1</td><td>1</td><td>连续读两次</td></tr></table>

## 14.4.2. 浮点数据格式


表 14-3. IEEE754 32 位单精度浮点格式


<table><tr><td>S [31]</td><td>E [30:23]</td><td>M [22:0]</td><td>值(V)</td></tr><tr><td>0</td><td>0</td><td>0</td><td>零(V=0)</td></tr><tr><td>1</td><td>0</td><td>0</td><td>负零(V=-0)</td></tr><tr><td>0+ve1-ve</td><td>0</td><td>非零</td><td>非规格化<eq>(V=(-1)^{s}*2^{(-126)*}(0.M))</eq></td></tr><tr><td>0+ve1-ve</td><td>1 to 254</td><td>0 to 0x7FFFFFF</td><td>正常范围<eq>(V=(-1)^{s}*2^{(E-127)*}(1.M))</eq></td></tr><tr><td>0</td><td>254</td><td>0x7FFFFFF</td><td>正最大值(V=+Max)</td></tr><tr><td>1</td><td>254</td><td>0x7FFFFFF</td><td>负最大值(V=-Max)</td></tr><tr><td>0</td><td>最大值255</td><td>0</td><td>正无穷(V=+Infinity)</td></tr><tr><td>1</td><td>最大值255</td><td>0</td><td>负无穷(V=-Infinity)</td></tr><tr><td>x</td><td>最大值255</td><td>非零</td><td>非数(V=NaN)</td></tr></table>


TMU 对于 IEEE 浮点数据格式中不同的数据处理如下：


负零：如果运算结果是 0，TMU 将会输出正零 $( \mathsf { S } { = } 0 , \mathsf { E } { = } 0 , \mathsf { M } { = } 0 )$ ），不会产生负零。所有的 TMU 运算都将负零当做零处理。

非规格化数：输入的非规格化操作数 $( \mathsf { E } { = } 0 , \mathsf { M } ! { = } 0 )$ 被视为 $0 ( E { = } 0 , \mathsf { M } { = } 0 )$ ）。

非数（NaN）：输入的 NaN 操作数 $( E { = } \mathsf { m a x } , \mathsf { M } { = } 0 )$ 被视为无穷 $( E { = } \mathsf { m a x } , \mathsf { M } { = } 0 )$ o

溢出：当 IFLTEN 和 OFLTEN 位同时被置位时，如果输入数据或者运算中的数据按照既定浮点格式显得过大会产生上溢，在这种情景下，TMU_CS 寄存器的 OVRF 标志位置位。

## 14.4.3. 模式配置

TMU_CS 寄存器的 MODE[3:0]位域用来配置 CORDIC 算法核模块的运行模式。不同的模式使用不同的系统（圆周系统或者双曲线系统）和不同的模式（旋转模式或者向量模式）。详细信息参考14-4. TMU 。


表 14-4. TMU 模式配置


<table><tr><td>模式</td><td>第一个输入数据</td><td>第二个输入数据</td><td>第一个输出数据</td><td>第二个输出数据</td><td>使用的系统和模式</td></tr><tr><td>模式0</td><td>θ</td><td>m</td><td>m*cos(θ)</td><td>m*sin(θ)</td><td>圆周系统,旋转模式</td></tr><tr><td>模式1</td><td>θ</td><td>m</td><td>m*sin(θ)</td><td>m*cos(θ)</td><td>圆周系统,旋转模式</td></tr><tr><td>模式2</td><td>x</td><td>y</td><td>atan2(y,x)</td><td><eq>\sqrt{x^2+y^2}</eq></td><td>圆周系统,向量模式</td></tr><tr><td>模式3</td><td>x</td><td>y</td><td><eq>\sqrt{x^2+y^2}</eq></td><td>atan2(y,x)</td><td>圆周系统,向量模式</td></tr><tr><td>模式4</td><td>x</td><td>无</td><td>tan<eq>^{-1}</eq>(x)</td><td>无</td><td>圆周系统,向量模式</td></tr><tr><td>模式5</td><td>x</td><td>无</td><td>cosh(x)</td><td>sinh(x)</td><td>双曲线系统,旋转模式</td></tr><tr><td>模式6</td><td>x</td><td>无</td><td>sinh(x)</td><td>cosh(x)</td><td>双曲线系统,旋转模式</td></tr><tr><td>模式7</td><td>x</td><td>无</td><td>tanh<eq>^{-1}</eq>(x)</td><td>无</td><td>双曲线系统,向量模式</td></tr><tr><td>模式8</td><td>x</td><td>无</td><td>ln(x)</td><td>无</td><td>双曲线系统,向量模式</td></tr><tr><td>模式9</td><td>x</td><td>无</td><td><eq>\sqrt{x}</eq></td><td>无</td><td>双曲线系统,向量模式</td></tr></table>

尽管 TMU 算法仅能够直接计算少量的函数，但更多的函数可以通过间接的方法来获得。比如，$\mathtt { e } ^ { \mathsf { x } } = \mathsf { s i n h } \left( \mathsf { x } \right) + \mathsf { c o s h } \left( \mathsf { x } \right)$ 

## 模式 0: m* cos(θ)

该模式用来计算余弦函数，有两个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-5. 0 IFLTEN OFLTEN位均置位时。


表 14-5. 模式 0 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>\frac{\theta}{\pi} \in (-2^{24}, 2^{24})</eq></td><td>角度值θ单位是弧度(rad),超出范围时溢出。</td></tr><tr><td>第二个输入数据</td><td><eq>m \in (-\infty, +\infty)</eq></td><td>超出浮点表示范围时溢出</td></tr><tr><td>第一个输出数据</td><td><eq>m^{*}\cos(\theta) \in (-\infty, +\infty)</eq></td><td>--</td></tr><tr><td>第二个输出数据</td><td><eq>m^{*}\sin(\theta) \in (-\infty, +\infty)</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-6. 0 IFLTEN OFLTEN

位复位时。


表 14-6. 模式 0 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>\frac{\theta}{\pi} \in [-1,1)</eq></td><td>角度值θ单位是弧度(rad),范围 θ∈[-π,π)。软件用θ除以π后,转换为[-1,1)范围内,再按照 q1.31、q1.15 或者 float 格式写入 TMU_IDATA 寄存器</td></tr><tr><td>第二个输入数据</td><td>m ∈ [0,1)</td><td>当0 ≤ m &lt; 1时,直接按照 q1.31、q1.15 或者 float 格式写入 TMU_IDATA 寄存器。当m ≥ 1时,需要先通过软件缩小m到[0,1)范围内,再写入到寄存器中。</td></tr><tr><td>第一个输出数据</td><td>m* cos(θ),范围[-1,1)</td><td rowspan="2">如果之前软件缩小过m,需要对该输出数据进行相应比例的放大,以获得真实结果。</td></tr><tr><td>第二个输出数据</td><td>m* sin(θ),范围[-1,1)</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>


注意：当模长m > 1时，软件缩放的比例是自行选择的。


例如，计算 $1 0 0 ^ { \star } \cos \left( { \frac { \pi } { 2 } } \right)$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件处理角度 $: \frac { \pi } { 2 } \circ \frac { \frac { \pi } { 2 } } { \pi } = \frac { 1 } { 2 } ,$ ，q1.15 格式下数据为 0x4000。

2. 软件处理模长m，将其缩小 128 倍。 $\frac { 1 0 0 } { 1 2 8 } = 0 . 7 8 1 2 5$ ，q1.15 格式下数据为 0x6400。

3. 往寄存器 TMU_IDATA 写第一个输入数据：角度值 0x4000。

4. 往寄存器 TMU_IDATA 写第二个输入数据：模长 0x6400。

5. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据 $y _ { 1 } = { \frac { 1 0 0 } { 1 2 8 } } \cos \left( { \frac { \pi } { 2 } } \right)$ ，再读一次TMU_ODATA 获取第二个输出数据 $y _ { 2 } { = } \frac { 1 0 0 } { 1 2 8 } \star \sin ( \frac { \pi } { 2 } )$ 

6. 结果处理。由于之前对模长m缩小了 128 倍，结果需要再乘以 128，则 $1 0 0 ^ { \star } \cos \left( { \frac { \pi } { 2 } } \right) = 1 2 8 ^ { \star } \mathsf { y } _ { 1 }$ 0

本例（计算 $1 0 0 ^ { \star } \cos \left( \frac { \pi } { 2 } \right) ;$ ）中对模长m和结果处理使用了 128 倍缩放，当然也可以使用其他缩放倍数，比如 101。

## 模式 1: m*sin(θ)

该模式用来计算正弦函数，有两个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-7. 1 IFLTEN OFLTEN

位均置位时


表 14-7. 模式 1 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>\frac{\theta}{\pi} \in (-2^{24}, 2^{24})</eq></td><td>角度值θ单位是弧度(rad),超出范围时溢出。</td></tr><tr><td>第二个输入数据</td><td><eq>m \in (-\infty, +\infty)</eq></td><td>超出浮点表示范围时溢出</td></tr><tr><td>第一个输出数据</td><td><eq>m^{*}\sin(\theta) \in (-\infty, +\infty)</eq></td><td>--</td></tr><tr><td>第二个输出数据</td><td><eq>m^{*}\cos(\theta) \in (-\infty, +\infty)</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-8. 1 IFLTEN OFLTEN位复位时。


表 14-8. 模式 1 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>\frac{\theta}{\pi} \in [-1,1)</eq></td><td>角度值θ单位是弧度(rad),范围 θ ∈ [-π,π)。软件用θ除以π后,转换为[-1,1)范围内,再按照 q1.31、q1.15 或者 float 格式写入 TMU_IDATA 寄存器</td></tr><tr><td>第二个输入数据</td><td>m ∈ [0,1)</td><td>当0 ≤ m &lt; 1时,直接按照 q1.31、q1.15 或者 float 格式写入 TMU_IDATA 寄存器。当m ≥ 1时,需要先通过软件缩小m到[0,1)范围内,再写入到寄存器中。</td></tr><tr><td>第一个输出数据</td><td>m* sin(θ),范围[-1,1)</td><td rowspan="2">如果之前软件缩小过m,需要对该输出数据进行相应比例的放大,以获得真实结果。</td></tr><tr><td>第二个输出数据</td><td>m* cos(θ),范围[-1,1)</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>


注意：当模长m > 1时，软件缩放的比例是自行选择的。


例如，计算 $1 0 0 ^ { \star } \sin \left( { \frac { \pi } { 2 } } \right)$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件处理角度 $: \frac { \pi } { 2 } \circ \frac { \frac { \pi } { 2 } } { \pi } = \frac { 1 } { 2 } ,$ ，q1.15 格式下数据为 0x4000。

2. 软件处理模长m，将其缩小 128 倍。 $\frac { 1 0 0 } { 1 2 8 } = 0 . 7 8 1 2 5$ ，q1.15 格式下数据为 0x6400。

3. 往寄存器 TMU_IDATA 写第一个输入数据：角度值 0x4000。

4. 往寄存器 TMU_IDATA 写第二个输入数据：模长 0x6400。

5. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据 $y _ { 1 } = \frac { 1 0 0 } { 1 2 8 } \star \sin ( \frac { \pi } { 2 } )$ ，再读一次TMU_ODATA 获取第二个输出数据 $y _ { 2 } { = } \frac { 1 0 0 } { 1 2 8 } \star \cos \left( \frac { \pi } { 2 } \right)$ 

$$
1 0 0 ^ {*} \sin \left(\frac {\pi}{2}\right) = 1 2 8 ^ {*} y _ {1}
$$

本例（计算 $1 0 0 ^ { \star } \sin \left( { \frac { \pi } { 2 } } \right) .$ ）中对模长m和结果处理使用了 128 倍缩放，当然也可以使用其他缩放倍数，比如 101。

## 模式 2: phase= atan2 (y,x)

该模式用来计算atan2(y,x)函数，有两个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-9. 2 IFLTEN OFLTEN位均置位时


表 14-9. 模式 2 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td rowspan="2"><eq>2^{-24&lt;|y/x|&lt;2^24}</eq></td><td rowspan="2">超出范围时溢出。</td></tr><tr><td>第二个输入数据</td></tr><tr><td>第一个输出数据</td><td>角度 <eq>\theta \in [-1,1)</eq></td><td>坐标位置对应的角度,<eq>[-1,1)</eq>对应<eq>[-\pi,\pi)</eq>。该输出数据乘以<eq>\pi</eq>得到真实角度值。</td></tr><tr><td>第二个输出数据</td><td>模长 <eq>m \in [0,+\infty)</eq></td><td><eq>m=\sqrt{x^{2}+y^{2}}</eq>,超出浮点表示范围时溢出</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-10. 2 IFLTEN OFLTEN位复位时


表 14-10. 模式 2 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>x \in [-1,1)</eq></td><td>笛卡尔坐标系中横坐标值。如果<eq>x \geq 1</eq>或者<eq>x &lt; -1</eq>,则需要进行软件缩放。</td></tr><tr><td>第二个输入数据</td><td><eq>y \in [-1,1)</eq></td><td>笛卡尔坐标系中纵坐标。如果<eq>y \geq 1</eq>或者<eq>x &lt; -1</eq>,则需要进行软件缩放。</td></tr><tr><td>第一个输出数据</td><td>角度<eq>\theta \in [-1,1)</eq></td><td>坐标位置对应的角度,<eq>[-1,1)</eq>对应<eq>[-\pi,\pi)</eq>。该输出数据乘以<eq>\pi</eq>得到真实角度值。</td></tr><tr><td>第二个输出数据</td><td>模长<eq>m \in [0,1)</eq></td><td><eq>m = \sqrt{x^2 + y^2}</eq>。如果之前对<eq>x</eq>和<eq>y</eq>进行了缩放,该模长需要进行等比例放大。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值3&#x27;b000</td></tr></table>

注意：当 IFLTEN 位或 OFLTEN 位复位时，如果x 或 y超出[-1,1)的范围，或者 $\sqrt { x ^ { 2 } + y ^ { 2 } } \geq 1$ ，需要同时对x和y进行同比例缩放，避免出现超出数据范围的情况。不能只缩放一个，这样可以保证缩放前后坐标对应的角度不变。

例如，计算θ=atan2(5,80)，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据(5,80)除以 128，结果为 (0.0390625,0.625)，q1.15 格式下数据为(0x0500,0x5000)。

2. 往寄存器 TMU_IDATA 写入第一个输入数据0x0500。

3. 往寄存器 TMU_IDATA 写入第二个输入数据0x5000。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据θ，再读一次 TMU_ODATA 获取第二个输出数据m。

5. 结果处理。第一个输出数据角度θ乘以π，得到真实弧度。由于之前输入数据缩小了 128 倍，读出的第二个输出数据模长m需要再乘以 128 才是真实模长。

本例（计算θ=atan2(5,80)）中对输入和模长使用了 128 倍缩放，当然也可以使用其他缩放倍数，比如 81。

## 模式 3: modulus=√x<sup>2</sup>+y<sup>2</sup>

该模式用来计算 $\sqrt { x ^ { 2 } + y ^ { 2 } }$ 函数，有两个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-11. 3 IFLTEN OFLTEN位均置位时


表 14-11. 模式 3 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td rowspan="2"><eq>2^{-24&lt;|y/x|&lt;2^24}</eq></td><td rowspan="2">超出范围时溢出</td></tr><tr><td>第二个输入数据</td></tr><tr><td>第一个输出数据</td><td>模长 <eq>m \in [0,+\infty)</eq></td><td>角度值θ单位是弧度(rad)</td></tr><tr><td>第二个输出数据</td><td>角度 θ∈[-1,1)</td><td>坐标位置对应的角度,[-1,1)对应[-π,π)。该输出数据乘以π得到真实角度值。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-12. 3 IFLTEN OFLTEN位复位时


表 14-12. 模式 3 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>第一个输入数据</td><td><eq>x \in [-1,1)</eq></td><td>笛卡尔坐标系中横坐标值。如果<eq>x \geq 1</eq>或者<eq>x \leq -1</eq>,则需要进行软件缩放。</td></tr><tr><td>第二个输入数据</td><td><eq>y \in [-1,1)</eq></td><td>笛卡尔坐标系中纵坐标。如果<eq>y \geq 1</eq>或者<eq>x \leq -1</eq>,则需要进行软件缩放。</td></tr><tr><td>第一个输出数据</td><td>模长<eq>m \in [0,1)</eq></td><td>模长,<eq>m = \sqrt{x^2 + y^2}</eq>。如果之前对x和y进行了缩放,该模长需要进行等比例放大。</td></tr><tr><td>第二个输出数据</td><td>角度 θ ∈ [-1,1)</td><td>坐标位置对应的角度,[-1,1)对应[-π,π)。该输出数据乘以π得到真实角度值。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3'b000</td></tr></table>

注意：当 IFLTEN 位或 OFLTEN 位复位时，如果x 或 y超出[-1,1)的范围，或者 $\sqrt { x ^ { 2 } + y ^ { 2 } } \geq 1$ ，需要同时对x和y进行同比例缩放，避免出现超出数据范围的情况。不能只缩放一个，这样可以保证缩放前后坐标对应的角度不变。

例如，计算 $\sqrt { 5 ^ { 2 } + 8 0 ^ { 2 } }$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据(5,80)除以 128，结果为(0.0390625,0.625)，q1.15 格式下数据为(0x0500,0x5000)。

2. 往寄存器 TMU_IDATA 写入第一个输入数据0x0500。

3. 往寄存器 TMU_IDATA 写入第二个输入数据0x5000，TMU 启动计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据m，再读一次 TMU_ODATA 获取第二个输出数据θ。

5. 软件结果处理。由于之前输入数据缩小了 128 倍，读出的第一个输出数据模长m需要再乘以128 才是真实模长。第二个输出数据角度θ乘以π，得到真实弧度。

本例（计算 ${ \sqrt { 5 ^ { 2 } + 8 0 ^ { 2 } } } ~ ,$ ）中对输入和模长使用了 128 倍缩放，当然也可以使用其他缩放倍数，比如81。

## 模式 4: $\tan ^ { - 1 } \left( \mathbf { x } \right)$

该模式用来计算 $\tan ^ { - 1 } ( x )$ 函数，有一个输入数据和一个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-13. 4 IFLTEN OFLTEN位均置位时。


表 14-13. 模式 4 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in (-2^7, 2^7)</eq></td><td>超出范围时溢出</td></tr><tr><td>输出数据</td><td><eq>\theta \in (-\frac{1}{2}, \frac{1}{2})</eq></td><td>坐标位置对应的角度,<eq>[-1,1)</eq>对应<eq>[-\pi, \pi)</eq>。该输出数据乘以<eq>\pi</eq>得到真实角度值。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-14. 4 IFLTEN OFLTEN

位复位时。


表 14-14. 模式 4 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2^f} \in [-1,1)</eq></td><td>当 <eq>x \in [-1,1]</eq>时,不需要缩放处理,<eq>f=0</eq>。如果x超出[-1,1]范围,需要软件缩放,缩放后要保证<eq>-1 \leq x^{*} 2^{-f} &lt; 1</eq>,f为缩放因子,把缩放后的数据<eq>\frac{x}{2^f}</eq>以 q1.15、q1.31 或者浮点格式写入 TMU_IDATA寄存器。</td></tr><tr><td>输出数据</td><td><eq>\frac{\theta}{2^f} \in (-\frac{1}{2}, \frac{1}{2})</eq></td><td>[-1,1)对应[-π,π)。该输出数据乘以π和<eq>2^f</eq>得到真实角度值。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td><eq>f \in [0,7]</eq></td><td>FACTOR[2:0]配置为 f</td></tr></table>


注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]需要配置。


例如，计算 $\tan ^ { - 1 } ( 1 0 0 )$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据100除以 128（缩放因子f $= 7 = 3 6 1 1 1 1$ ），得0.78125，q1.15 格式下数据为0x6400。

2. 缩放因子 $\tan 3 6 7 = 3 3 6 7 1 1$ 写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x6400，TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取输出数据 $\frac { \theta } { 2 ^ { 7 } }$ 。

5. 结果处理。输出数据 $\frac { \theta } { 2 ^ { 7 } }$ 需要乘以π和 $2 ^ { 7 }$ 得到真实弧度。

## 模式 5: cosh (x)

该模式用来计算cosh(x)函数，有一个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-15. 5 IFLTEN OFLTEN位均置位时。


表 14-15. 模式 5 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in [-1.118, 1.118]</eq></td><td>超出范围时溢出</td></tr><tr><td>第一个输出数据</td><td><eq>\cosh(x) \in [1, 1.692]</eq></td><td>--</td></tr><tr><td>第二个输出数据</td><td><eq>\sinh(x) \in [-1.366, 1.366]</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-16. 5 IFLTEN OFLTEN

位复位时。


表 14-16. 模式 5 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2} \in [-0.559, 0.559]</eq></td><td>x∈[-1.118,1.118],需要软件将x除以2,然后以q1.15、q1.31或浮点格式写入TMU_IDATA寄存器。</td></tr><tr><td>第一个输出数据</td><td><eq>\frac{\cosh(x)}{2} \in [0.5, 0.846)</eq></td><td>该输出数据乘以2可以得到双曲余弦cosh(x)的值。</td></tr><tr><td>第二个输出数据</td><td><eq>\frac{\sinh(x)}{2} \in [-0.683, 0.683]</eq></td><td>该输出数据乘以2可以得到双曲正弦sinh(x)的值</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>f=1</td><td>FACTOR[2:0]配置为3&#x27;b001</td></tr></table>


注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]只能配置为 3’b001。


例如，计算cosh(1.0)，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据 1.0 除以 $2 ( 1 { = } 3 { \dot { \mathsf { b } } } 0 0 1 { \dot { \mathsf { \Omega } } }$ ），结果为 0.5，q1.15 格式下数据为0x4000。

2. 将缩放因子f=3<sup>'</sup>b001写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x4000, TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据 $\mathsf { y } _ { 1 } = \frac { \mathsf { c o s h } ( 1 . 0 ) } { 2 }$ ，再读一次获取第二个输出数据 $\begin{array} { r } { { \frac { \mathbf { \sigma } _ { 1 } } { \mathbf { \sigma } _ { 1 } } } = { \frac { \sin \mathbf { h } \left( 1 . 0 \right) } { 2 } } } \end{array}$ o

5. 结果处理。两个输出数据都乘以 2，得到双曲余弦cosh(x)和双曲正弦sinh(x)。

## 模式 6: sinh (x)

该模式用来计算sinh(x)函数。有一个输入数据和两个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-18. 6 IFLTEN OFLTEN位复位时。


表 14-17. 模式 6 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in [-1.118, 1.118]</eq></td><td>超出范围时溢出</td></tr><tr><td>第一个输出数据</td><td><eq>\sinh(x) \in [-1.366, 1.366]</eq></td><td>--</td></tr><tr><td>第二个输出数据</td><td><eq>\cosh(x) \in [1, 1.692]</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-18. 6 IFLTEN OFLTEN

位复位时。


表 14-18. 模式 6 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2} \in [-0.559, 0.559]</eq></td><td>x∈[-1.118,1.118],需要软件将x除以2,然后以q1.15、q1.31或浮点格式写入TMU_IDATA寄存器。</td></tr><tr><td>第一个输出数据</td><td><eq>\frac{\sinh(x)}{2} \in [-0.683, 0.683]</eq></td><td>输出数据乘以2得到双曲正弦sinh(x)。</td></tr><tr><td>第二个输出数据</td><td><eq>\frac{\cosh(x)}{2} \in [0.5, 0.846)</eq></td><td>输出数据乘以2得到双曲余弦cosh(x)</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>f=1</td><td>FACTOR[2:0]配置为3&#x27;b001</td></tr></table>

注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]只能配置为 3’b001。

例如，计算sinh (1.0)，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据 1.0 除以 $2 ( 1 { = } 3 ^ { \cdot } \mathrm { b } 0 0 1 )$ ），结果为 0.5，q1.15 格式下数据为0x4000。

2. 将缩放因子f=3<sup>'</sup>b001写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x4000, TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取第一个输出数据 $\mathsf { y } _ { 1 } = \frac { \mathsf { s i n h } \left( 1 . 0 \right) } { 2 }$ ，再读一次获取第二个输出数据 $\mathsf { y } _ { 2 } ^ { } = \frac { \mathsf { c o s h } \left( 1 . 0 \right) } { 2 }$ 。这两个数据都是 q1.15 格式。

5. 结果处理。两个输出数据都乘以 2，得到双曲正弦sinh(x)和双曲余弦cosh(x)。

## 模式 7: $\tan \mathsf { h } ^ { - 1 } \left( \mathsf { x } \right)$

该模式用来计算 $\tan \mathsf { h } ^ { - 1 } \left( \mathsf { x } \right)$ 函数，有一个输入数据和一个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-19. 7 IFLTEN OFLTEN位均置位时。


表 14-19. 模式 7 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in [-0.806, 0.806]</eq></td><td>超出范围时溢出</td></tr><tr><td>输出数据</td><td><eq>\tanh^{-1}(x) \in [-1.118, 1.118]</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-20. 7 IFLTEN OFLTEN

位复位时。


表 14-20. 模式 7 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2} \in [-0.403, 0.403]</eq></td><td>x∈[-0.806,0.806],软件将x除以2,然后以q1.15、q1.31或浮点格式写入TMU_IDATA寄存器。</td></tr><tr><td>输出数据</td><td><eq>\frac{\tanh^{-1}(x)}{2} \in [-0.559, 0.559]</eq></td><td>输出数据乘以2得到反双曲正切<eq>tanh^{-1}(x)</eq>。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>f=1</td><td>FACTOR[2:0]配置为3&#x27;b001</td></tr></table>


注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]只能配置为 3’b001。


例如，计算 $\cdot \tan \mathsf { h } ^ { - 1 } ( 0 . 5 )$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据 0.5 除以 2 $( \mathsf { f } = 3 \mathsf { b } 0 0 1 )$ ），结果为 0.25，q1.15 格式下数据为0x2000。

2. 将缩放因子f=3<sup>'</sup>b001写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x2000，TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取输出数据 $\mathsf { y } = \frac { \mathsf { t a n h } ^ { - 1 } \left( 0 . 5 \right) } { 2 } \mathrm { , }$ 

5. 结果处理。输出数据乘以 2，得到反双曲正切tanh<sup>-1</sup>(0.5)。

## 模式 8：ln (x)

该模式用来计算ln(x)函数，有一个输入数据和一个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-21. 8 IFLTEN OFLTEN位均置位时


表 14-21. 模式 8 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in [0.107,9.35]</eq></td><td>超出范围时溢出</td></tr><tr><td>输出数据</td><td><eq>\ln(x) \in (-2.235,2.235)</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-22. 8 IFLTEN OFLTEN位复位时。


表 14-22. 模式 8 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2^f} \in [0.0535, 0.875]</eq></td><td><eq>x \in [0.107, 9.35]</eq>,需要软件缩放,保证<eq>\frac{x}{2^f} &lt; (1 - \frac{1}{2^f})</eq>其中f为缩放因子,然后将<eq>\frac{x}{2^f}</eq>以q1.15、q1.31或者浮点格式写入TMU_IDATA寄存器。</td></tr><tr><td>输出数据</td><td><eq>\frac{\ln(x)}{2^{(f+1)}}\in[-0.558,0.137]</eq></td><td>输出数据乘以<eq>2^{(f+1)}</eq>得到自然对数ln(x)。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>f∈[1,4]</td><td>FACTOR[2:0]配置为f</td></tr></table>


注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]需要配置。


例如，计算ln(8)，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据 8 除以 16（缩放因子 $\scriptstyle \cdot \mathbf { \vec { f } } = 3 ^ { \prime } \mathbf { b } 1 0 0 )$ ），结果为0.5，q1.15 格式下数据为0x4000。

2. 将缩放因子f=3'b100写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x4000，TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取输出数据 $\mathsf { y } = \frac { \mathsf { I n } \left( \mathsf { x } \right) } { 2 ^ { \left( 4 + 1 \right) } } \mathsf { c }$ 

5. 结果处理。输出数据乘以2<sup>(4+1)</sup>，得到自然对数ln (x)。

为保证计算精度，对于不同输入推荐使用 14-23. 8 中的缩放因子。


表 14-23. 模式 8 推荐的缩放因子


<table><tr><td>输入 x 范围</td><td>缩放因子 FACTOR[2:0]</td><td>输入数据范围</td></tr><tr><td><eq>0.107 \leq x &lt; 1</eq></td><td>3&#x27;b001</td><td>[0.0535,0.5)</td></tr><tr><td><eq>1 \leq x &lt; 3</eq></td><td>3&#x27;b010</td><td>[0.25,0.75)</td></tr><tr><td><eq>3 \leq x &lt; 7</eq></td><td>3&#x27;b011</td><td>[0.375,0.875)</td></tr><tr><td><eq>7 \leq x &lt; 9.35</eq></td><td>3&#x27;b100</td><td>[0.4375,0.584)</td></tr></table>

模式 9: $\sqrt { \pmb { x } }$ 

该模式用来计算 $\sqrt { \mathsf { x } } \mathrm { i }$ 函数，有一个输入数据和一个输出数据。

当 IFLTEN 位和 OFLTEN 位均置位时，详细信息参考 14-24. 9 IFLTEN OFLTEN位均置位时。


表 14-24. 模式 9 描述，IFLTEN 位和 OFLTEN 位均置位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>x \in [0, +\infty)</eq></td><td>超出范围时溢出</td></tr><tr><td>输出数据</td><td><eq>\sqrt{x} \in [0, +\infty)</eq></td><td>--</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td>不可用</td><td>保持复位值 3&#x27;b000</td></tr></table>

当 IFLTEN 位或 OFLTEN 位复位时，详细信息参考 14-25. 9 IFLTEN OFLTEN

位复位时。


表 14-25. 模式 9 描述，IFLTEN 位或 OFLTEN 位复位时


<table><tr><td>参数</td><td>范围</td><td>描述</td></tr><tr><td>输入数据</td><td><eq>\frac{x}{2^f} \in [0.027, 0.875]</eq></td><td><eq>x \in [0.027, 2.34]</eq>。软件进行缩放处理,保证<eq>\frac{x}{2^f} &lt; (1 - \frac{1}{2^{f+2}})</eq>,其中 f 为缩放因子。然后将<eq>\frac{x}{2^f}</eq>以 q1.15 或者 q1.31 写入 TMU_IDATA 寄存器。</td></tr><tr><td>输出数据</td><td><eq>\frac{\sqrt{x}}{2^f} \in [0.164, 0.866]</eq></td><td>输出数据乘以<eq>2^f</eq>得到<eq>\sqrt{x}</eq>。</td></tr><tr><td>缩放因子FACTOR[2:0]</td><td><eq>f \in [0, 2]</eq></td><td>FACTOR[2:0]配置为 f</td></tr></table>


注意：当 IFLTEN 位或 OFLTEN 位复位时，缩放因子 FACTOR[2:0]需要配置。


例如，计算 ${ \sqrt { 2 } } ,$ ，当 IFLTEN 位和 OFLTEN 位均复位，IWIDTH 位和 OWIDTH 位均置位时，输入输出数据均为 q1.15 格式。可以按照以下步骤进行：

1. 软件缩放。输入数据 2 除以 4（缩放因子f=3'b010），结果为0.5，q1.15 格式下数据为0x4000。

2. 将缩放因子f=3'b010写入 TMU_CS 寄存器的 FACTOR[2:0]位域。

3. 往寄存器 TMU_IDATA 写入输入数据0x4000，TMU 开始计算。

4. 等待 ENDF 标志置 1，读 TMU_ODATA 获取输出数据 $y _ { 1 } = \frac { \sqrt { 2 } } { 2 ^ { 2 } }$ 

5. 结果处理。输出数据乘以 $\cdot 2 ^ { 2 }$ ，得到 $\sqrt { 2 }$ 。

为保证计算精度，对于不同输入推荐使用 14-26. 9 中的缩放因子。


表 14-26. 模式 9 推荐的缩放因子


<table><tr><td>输入x范围</td><td>缩放因子 FACTOR[2:0]</td><td>输入数据范围</td></tr><tr><td>0.0273&#x27;b000[0.027,0.75)</td><td>3&#x27;b000</td><td>[0.027,0.75)</td></tr><tr><td>0.75≤x&lt;1.75</td><td>3&#x27;b001</td><td>[0.375,0.875)</td></tr><tr><td>1.75≤x&lt;2.341</td><td>3&#x27;b010</td><td>[0.4375,0.585)</td></tr></table>

## 14.4.4. TMU运算挂起

如果当前正在执行 TMU 运算，可以写 TMU_CS 和 TMU_IDATA 寄存器，写入的内容将被挂起。当 TMU 运算完成（结果被读取，ENDF 标志清零）时，如果挂起的输入数据数量符合配置（定义在被挂起的 TMU_CS中），TMU 模块将按照挂起的配置和数据开始新一次 TMU 运算。

例如，如果配置的 TMU 模式需要两个 32-bit 输入数据（IWIDTH=0,INUM=1），当往 TMU_IDATA寄存器写入两个 32-bit 的数据后，TMU 启动一次运算。如果第二个输入参数在下一次 TMU 运算中不改变，此时可以修改 INUM=0。当前一次 TMU 运算结束后，往 TMU_IDATA 寄存器写入一个输入数据，TMU 启动运算，只要 TMU 模式没有改变，第二个参数仍使用之前的数值。

注意：复位后，第二个数值为+1（0x7FFFFFF）。

如果当前已经存在挂起的 TMU 数据，再往 TMU_CS 和 TMU_IDATA 寄存器写入新的数据，则新数据覆盖原来数据，新的 TMU 数据被挂起，原数据的挂起失效。

## 14.4.5. 零开销

当一个 TMU 运算开始后，可以直接读取输出数据寄存器，在结果返回之前总线会自动插入等待周期。可以按照以下步骤进行：

1. 根据需要 TMU_CS 寄存器。

2. 往 TMU_IDATA 写入需要的参数，启动一个 TMU 运算。

3. 根据需要配置下一次 TMU 模式，并往 TMU_IDATA 写入下一次需要的数据。

4. 读取 TMU_ODATA。总线自动插入等待周期。当读取 TMU_ODATA 操作完成后，在第 3 步骤中配置得 TMU 操作会自动启动。

5. 返回第 3 步。

## 14.4.6. 中断和 DMA

当 ENDF 标志位置 1 时，如果 TMU_CS寄存器中的 RIE 为 1，则产生中断请求。ENDF 标志清 0后，中断请求也清除。

当 OVRF 标志设置为 1 时，如果 TMU_CS 寄存器中的 OVRIE 位为 1，则产生中断请求。当 OVRF标志被清 0 后，中断请求也被清除。

如果 TMU_CS 寄存器中的 WDEN 为 1 并且此时没有 TMU 挂起，则产生 DMA 请求，DMA 请求的数量却决于 TMU_CS 寄存器中的 INUM 位。如果 TMU_CS 寄存器中的 INUM=0，产生一次DMA传输请求。如果 TMU_CS寄存器中的 INUM=1，产生两次 DMA 传输请求。

当 ENDF 标志位置 1 时，如果 TMU_CS 寄存器中的 RDEN 为 1，则产生 DMA 请求，DMA 请求的数量 TMU_CS 寄存器中的 ONUM 位。如果 TMU_CS 寄存器中的 ONUM=0，产生一次 DMA 传输请求。如果 TMU_CS 寄存器中的 ONUM=1，产生两次 DMA传输请求。
