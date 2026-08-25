## 15. 快速傅里叶变换（FFT）

## 15.1. 简介

快速傅里叶变换（FFT）是离散傅里叶变换（DFT）的高效计算方法。该模块可以进行 FFT 运算，减轻了 CPU 负担。与软件实现相比，该模块可以加速了 FFT 的计算时间。该模块支持 6 个可配置的 FFT 点数，最多 1024，输入和输出数据应为 IEEE-754 单精度浮点复数。

## 15.2. 主要特性

 支持1024/512/256/128/64/32点FFT；

 支持IFFT模式；

 IEEE-754单精度浮点复数输入和输出数据；

 DMA主机加载和存储数据；

 支持在内存中配置的窗函数功能；

 支持输入下采样。

## 15.3. 功能描述

15-1. FFT 提供了FFT模块的内部配置细节。


图 15-1. FFT 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/87ec748a14df463fface1931ddbd45ed9721e46e9071a1d5881a03beff1214c0.jpg)


FFT 模块有 DMA 主机、队列控制子模块、蝶形运算子模块和寄存器组成。该模块是使用的基-2FFT 算法。先从存储中加载 IEEE754 单精度浮点格式的输入数据（包含实部和虚部）和窗函数数据，经过窗函数运算和输入位反运算之后，将结果写入内部 SRAM。旋转因子已经存储在ROM中。

蝶形运算子模块在 FFT 计算中被重复使用，并计算 $N / 2 ^ { \star } \log _ { 2 } \mathsf { N }$ 次。每次计算是相同的地址，也就是说，每次计算的输出数据被写回之前存储输入数据的相同地址。

所有蝶形计算迭代完成后，DMA主机将输出数据从内部 SRAM 传输到内存。

## 15.4. 数据格式

运算数据和计算结果格式如 15-1. IEEE32 所示。这些数据必须符合 IEEE32位单精度浮点格式。


表 15-1. IEEE32 位单精度浮点格式


<table><tr><td>符号位 S[31]</td><td>阶数位 E[30:23]</td><td>尾数位 M[22:0]</td><td>值(V)</td></tr><tr><td>0</td><td>0</td><td>0</td><td>零 (V = 0)</td></tr><tr><td>1</td><td>0</td><td>0</td><td>负零 (V = -0)</td></tr><tr><td>0+ve1-ve</td><td>0</td><td>非零</td><td>非规格数 (V=(-1)s*2(-126)*(0.M))</td></tr><tr><td>0+ve1-ve</td><td>1到254</td><td>0到0x7FFFFFF</td><td>正常范围 (V=(-1)*2(E-127)*(1.M))</td></tr><tr><td>0</td><td>254</td><td>0x7FFFFFF</td><td>V = +Max</td></tr><tr><td>1</td><td>254</td><td>0x7FFFFFF</td><td>V = -Max</td></tr><tr><td>0</td><td>max=255</td><td>0</td><td>正无穷 (V = +Infinity)</td></tr><tr><td>1</td><td>max=255</td><td>0</td><td>负无穷 (V = -Infinity)</td></tr><tr><td>x</td><td>max=255</td><td>非零</td><td>非数字 (V = NaN)</td></tr></table>

本模块的各种 IEEE 浮点数字格式的处理如下：

非规格化数字：非规格数 $\left( \mathsf E { = } 0 , \mathsf M : = 0 \right)$ 输入被视为零（E=O，M=0）。

溢出：当操作生成的值太大而无法以给定的浮点格式表示时，会发生溢出。

非数字（NaN）：NaN 操作数（E=max，M！=0）输入被视为无限 $\scriptstyle ( \mathsf { E } = \mathsf { m a x } , \mathsf { M } = 0 )$ 

## 15.5. 基-2 FFT

FFT 模块使用 DIT（时间抽取）基-2 算法，该算法依赖于将 N 点变换递归分解为两个（N / 2）点变换。为了便于说明，8 点时间抽取算法如 15-2. 8 DIF FFT 所示。


图 15-2. 8 点 DIF 的 FFT 流程图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/c41138a80d2d36a419d88e4e1f5c4aaae69c7640fc94cce7ea955570b4c0129a.jpg)



8 点输入序列相对于输出以比特倒序出现，如 15-2. 8 所示。



表 15-2. 8 点输入位倒序操作


<table><tr><td>索引值</td><td>二进制索引值</td><td>二进制位反索引值</td><td>位反索引值</td></tr><tr><td>0</td><td>000</td><td>000</td><td>0</td></tr><tr><td>1</td><td>001</td><td>100</td><td>4</td></tr><tr><td>2</td><td>010</td><td>010</td><td>2</td></tr><tr><td>3</td><td>011</td><td>110</td><td>6</td></tr><tr><td>4</td><td>100</td><td>001</td><td>1</td></tr><tr><td>5</td><td>101</td><td>101</td><td>5</td></tr><tr><td>6</td><td>110</td><td>011</td><td>3</td></tr><tr><td>7</td><td>111</td><td>111</td><td>7</td></tr></table>

## 15.6. 蝶形运算单元

蝶形运算单元式 FFT 计算的基本元素，其过程如 15-3. 所示。


图 15-3. 蝶形运算框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/984b345c334c8b6fe4fb50c6239e0ec0c1dbf1410cb301f297284643fee0a625.jpg)


$$
A ^ {\prime} = A + B W = R e (A) + R e (B W) + j [ I m (A) + I m (B W) ]
$$

$$
B ^ {\prime} = A - B W = R e (A) - R e (B W) + j [ I m (A) - I m (B W) ]
$$

其中 $W = W _ { N } ^ { \mathrm { k } } { = } \Theta ^ { \mathrm { - } j \frac { 2 \pi } { N } \mathrm { k } }$ 

## 15.7. IFFT 模式

IFFT 转换频域矢量信号到时域矢量信号，FFT 与 IFFT 在是线上的主要区别有：

 旋转因子共轭

 结果除以N，其中N为FFT的点数

## 15.8. FFT SRAM

当 FFT_CSR 寄存器的 FFTEN 位为 0 时，可以通过 AHB 访问 FFT 的 8KB SRAM 空间（0x40025800~0x40027FFF）。

注意:

 当 FFT_CSR 寄存器的 FFTEN 位为 1 时，通过 AHB 访问 FFT SRAM 会发生总线错误。

 如果 FFT 模块未使能，该 FFT SRAM 可以用作其他用途。

## 15.9. FFT 循环模式

FFT 支持循环模式。每次 FFTEN 置位，会启动一次运算，当 FFT 运算完 INDEX[15:0]索引加 1。

当每次 FFT 运算完，实部和虚部地址会增加，指向下一组输入数据。也就是说，每次 FFT 运算完成，FFT_LOOPLEN 寄 存器的 INDEX[15:0]加 1 。实部的起始地址是 FFT_RESADDR +{INDEX[15:0], 2’b00}，虚部的起始地址是 FFT_IMSADDR + {INDEX[15:0], 2’b00}。当 INDEX[15:0]增加到 LENGTH[15:0]，会自动清零。

注意：对应地址的输入数据要准备好。

## 15.10. 操作指南

该部分介绍 FFT 的推荐操作指南。

1. 如果需要，配置FFT_IMSADDR寄存器来设置FFT虚部的基地址，即虚部数据不为零。

2. 配置FFT_RESADDR寄存器来设置FFT实部基地址。

3. 如果需要，配置WINEN位和FFT_WSADDR寄存器来设置FFT窗函数的基地址。

4. 配置FFT_OSADDR寄存器来设置FFT输出结果的基地址。

5. 如果需要，配置FFT_LOOPLEN寄存器。

6. 如果需要，配置IFFTMODE。

7. 配置FFT_CSR寄存器中的NUMPT[2:0]位域来设置FFT点的数量。

8. 配置FFTEN位。

9. 等待FFTEN清零，或者CCF位置1。

## 15.11. FFT 中断

以下任一个标志发生都可以产生中断：

 FFT计算完成标志；

 传输访问错误中断标志模拟看门狗事件。

这些标志都被映射到同一个中断向量 IRQ96。
