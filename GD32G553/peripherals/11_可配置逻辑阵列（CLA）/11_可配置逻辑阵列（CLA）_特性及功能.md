## 11. 可配置逻辑阵列（CLA）

## 11.1. 简介

可配置逻辑阵列为外部引脚、CMP、ADC 和定时器提供 256 个可编程数字逻辑操作，而无需 CPU干预。本模块实现了四个独立的 CLA 单元。每个 CLA 单元支持 GPIO 引脚的可配置异步和同步输出。

## 11.2. 主要特性

 四个独立的 CLA 单元，每个 CLA单元具有两个信号选择器，支持 16 个输入信号，包括外部引脚、定时器通道、CMP、ADC 和 CLA异步输出；

 在每个 CLA 单元中实现逻辑配置单元（LCU），提供 256 个可编程数字逻辑功能；

 可编程异步和同步输出；

 可以将 CLA 输出配置为与外部引脚和定时器同步；

 四个 CLA 单元可以组合并支持复杂的逻辑操作。

## 11.3. 模块框图

CLA 接口的内部结构如所示。


图 11-1. CLA 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/9f12d44089f26b5bdc0d40a7f95c31f212817bff06e88455d22e9302099f5c64.jpg)


## 11.4. 功能描述

此模块中包含四个相同的CLA单元。每个CLA单元实现了两个信号选择器。此外，每个CLA还包括一个LCU。

## 11.4.1. CLA 输入信号选择器

每个 CLA 单元包括两个信号选择器：SIGS0 和 SIGS1。每个信号选择器的输入可以为：外部引脚、定时器通道(TIMERx_CHx)、定时器触发信号(TIMERx_TRGO)、ADC 转换信号(ADC_CONV)和 CLA 单元异步输出(CLAx_ASYNC_OUT)。当另一个 CLA 单元的异步输出作为 SIGS 的输入时，可以实现一个复杂的组合逻辑运算。当选择 TIMERx_TRGO 作为 SIGS 的输入时，只有第一个 HCLK 周期有效，其余的 TIMERx_TRGO 高被视为逻辑低。

11-1. CLAxSIGS0 和 11-2. CLAxSIGS1 显示了 CLAxSIGS0 和CLAxSIGS1 的输入选择。TRIGSEL_CLA_IN0~TRIGSEL_CLA_IN11 信号来自如 11-1. CLA所示的 TRIGSEL 模块。


表 11-1. CLAxSIGS0 输入选择


<table><tr><td>SIGS0[3:0]</td><td>CLA0SIGS0</td><td>CLA1SIGS0</td><td>CLA2SIGS0</td><td>CLA3SIGS0</td></tr><tr><td>0000</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td></tr><tr><td>0001</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td></tr><tr><td>0010</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td></tr><tr><td>0011</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td></tr><tr><td>0100</td><td>TRIGSEL_CLA_IN7</td><td>TRIGSEL_CLA_IN8</td><td>TRIGSEL_CLA_IN9</td><td>TRIGSEL_CLA_IN10</td></tr><tr><td>0101</td><td>TRIGSEL_CLA_IN0</td><td>TRIGSEL_CLA_IN0</td><td>TRIGSEL_CLA_IN1</td><td>TRIGSEL_CLA_IN2</td></tr><tr><td>0110</td><td>TRIGSEL_CLA_IN1</td><td>TRIGSEL_CLA_IN3</td><td>TRIGSEL_CLA_IN3</td><td>TRIGSEL_CLA_IN4</td></tr><tr><td>0111</td><td>TRIGSEL_CLA_IN2</td><td>TRIGSEL_CLA_IN4</td><td>TRIGSEL_CLA_IN5</td><td>TRIGSEL_CLA_IN5</td></tr><tr><td>1000</td><td>CLAIN0</td><td>CLAIN4</td><td>CLAIN0</td><td>CLAIN2</td></tr><tr><td>1001</td><td>CLAIN2</td><td>CLAIN5</td><td>CLAIN1</td><td>CLAIN3</td></tr><tr><td>1010</td><td>CLAIN4</td><td>CLAIN8</td><td>CLAIN8</td><td>CLAIN6</td></tr><tr><td>1011</td><td>CLAIN6</td><td>CLAIN10</td><td>CLAIN9</td><td>CLAIN7</td></tr><tr><td>1100</td><td>CLAIN8</td><td>CLAIN12</td><td>CLAIN14</td><td>CLAIN10</td></tr><tr><td>1101</td><td>CLAIN10</td><td>CLAIN13</td><td>CLAIN15</td><td>CLAIN11</td></tr><tr><td>1110</td><td>CLAIN12</td><td>CLAIN16</td><td>CLAIN16</td><td>CLAIN18</td></tr><tr><td>1111</td><td>CLAIN14</td><td>CLAIN18</td><td>CLAIN17</td><td>CLAIN19</td></tr></table>


表 11-2. CLAxSIGS1 输入选择


<table><tr><td>SIGS1[3:0]</td><td>CLA0SIGS1</td><td>CLA1SIGS1</td><td>CLA2SIGS1</td><td>CLA3SIGS1</td></tr><tr><td>0000</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td><td>CLA0_ASYNC_OUT</td></tr><tr><td>0001</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td><td>CLA1_ASYNC_OUT</td></tr></table>


GD32G553 用户手册


<table><tr><td>0010</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td><td>CLA2_ASYNC_OUT</td></tr><tr><td>0011</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td><td>CLA3_ASYNC_OUT</td></tr><tr><td>0100</td><td>TRIGSEL_CLA_IN11</td><td>TRIGSEL_CLA_IN11</td><td>TRIGSEL_CLA_IN11</td><td>TRIGSEL_CLA_IN11</td></tr><tr><td>0101</td><td>TRIGSEL_CLA_IN3</td><td>TRIGSEL_CLA_IN1</td><td>TRIGSEL_CLA_IN0</td><td>TRIGSEL_CLA_IN0</td></tr><tr><td>0110</td><td>TRIGSEL_CLA_IN4</td><td>TRIGSEL_CLA_IN2</td><td>TRIGSEL_CLA_IN2</td><td>TRIGSEL_CLA_IN1</td></tr><tr><td>0111</td><td>TRIGSEL_CLA_IN5</td><td>TRIGSEL_CLA_IN5</td><td>TRIGSEL_CLA_IN4</td><td>TRIGSEL_CLA_IN3</td></tr><tr><td>1000</td><td>CLAIN1</td><td>CLAIN6</td><td>CLAIN2</td><td>CLAIN0</td></tr><tr><td>1001</td><td>CLAIN3</td><td>CLAIN7</td><td>CLAIN3</td><td>CLAIN1</td></tr><tr><td>1010</td><td>CLAIN5</td><td>CLAIN9</td><td>CLAIN10</td><td>CLAIN4</td></tr><tr><td>1011</td><td>CLAIN7</td><td>CLAIN11</td><td>CLAIN11</td><td>CLAIN5</td></tr><tr><td>1100</td><td>CLAIN9</td><td>CLAIN14</td><td>CLAIN12</td><td>CLAIN8</td></tr><tr><td>1101</td><td>CLAIN11</td><td>CLAIN15</td><td>CLAIN13</td><td>CLAIN9</td></tr><tr><td>1110</td><td>CLAIN13</td><td>CLAIN17</td><td>CLAIN18</td><td>CLAIN16</td></tr><tr><td>1111</td><td>CLAIN15</td><td>CLAIN19</td><td>CLAIN19</td><td>CLAIN17</td></tr></table>

## 11.4.2. 逻辑控制单元（LCU）控制

每个 CLA 单元都有一个 LCU，LCU 引入了 256 种逻辑组合功能，通过 CLAx_LCUCTL 寄存器的LCU [7:0]位控制。LCU 有三个输入源，当 CLA 单元被禁用时，它们对 LCU 输出没有影响。

 Input0: SIGS0输出

 Input1: SIGS1输出

 Input2: CLA结果来自前一个CLA单元（CLA[x-1]）的LCU结果

如果 CLA 单元被禁用，则 LCU 输入强制为“0”。

LCU [7:0]的 bit7~0 控制 input0(IN0)、input1(IN1)、input2(IN2)的哪个逻辑功能可以影响输出，如11-3. LCU 所示。


表 11-3. LCU 控制


<table><tr><td>LCU[7:0]</td><td>input 0</td><td>input 1</td><td>input 2</td></tr><tr><td>bit 0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>bit 1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>bit 2</td><td>0</td><td>1</td><td>0</td></tr><tr><td>bit 3</td><td>0</td><td>1</td><td>1</td></tr><tr><td>bit 4</td><td>1</td><td>0</td><td>0</td></tr><tr><td>bit 5</td><td>1</td><td>0</td><td>1</td></tr><tr><td>bit 6</td><td>1</td><td>1</td><td>0</td></tr><tr><td>bit 7</td><td>1</td><td>1</td><td>1</td></tr></table>

例如，当{IN0, IN1, IN2} == 3’b000 时，(IN0^IN1^IN2)的结果为 1’b0，所以 LCU[7:0]的 bit 0 为 0；当{IN0, IN1, IN2} == 3’b001 时，(IN0^IN1^IN2)的结果为 1’b1，所以 LCU[7:0]的 bit 1 为 1；当{IN0,

IN1, IN2} == 3’b010 时，(IN0^IN1^IN2)的结果为 1’b1，所以 LCU[7:0]的 bit 2 为 1；当{IN0, IN1,IN2} == 3’b011 时，(IN0^IN1^IN2)的结果为 1’b0，所以 LCU[7:0]的 bit 3 为 0；当{IN0, IN1, IN2}== 3’b100 时，(IN0^IN1^IN2)的结果为 1’b1，所以 LCU[7:0]的 bit 4 为 1；当{IN0, IN1, IN2} ==3’b101 时，(IN0^IN1^IN2)的结果为 1’b0，所以 LCU[7:0]的 bit 5 为 0；当{IN0, IN1, IN2} == 3’b110时，(IN0^IN1^IN2)的结果为 1’b0，所以 LCU[7:0]的 bit 6 为 0；当{IN0, IN1, IN2} == 3’b111 时，(IN0^IN1^IN2)的结果为 1’b1，所以LCU[7:0]的 bit 7 为1。因此，如果要实现逻辑函数(IN0^IN1^IN2)，那么 CLAx_LCUCTL 的 LCU[7:0]应该被配置为 8’b10010110。

## 11.4.3. CLA 输出

每个 CLA 单元都有一个 GPIO 引脚作为其输出，该输出可以是 LCU 的结果，也可以是经过触发器后的 LCU 结果。这可以通过 CLAx_CTL 寄存器的 OSEL 位选择。

触发器的时钟源和时钟极性可以分别通过 CLAx_CTL 寄存器的 CSEL[1:0]位和 CPOL 位来选择。有四个时钟可以作为触发器的时钟源，它们分别是：

 CLA[x-1]的结果：前一个 CLA 单元的 LCU 结果（CLA3 的 LCU 结果发送给 CLA0）

 SIGS0：多路选择器 SIGS0 的输出

HCLK 

 TIMER_TRGO ： TRIGSEL_CLA_IN6 对 应 CLA0 ， TRIGSEL_CLA_IN7 对 应 CLA1 ，TRIGSEL_CLA_IN8 对应 CLA2，TRIGSEL_CLA_IN9 对应 CLA3

给寄存器 CLAx_CTL 的位 FFRST 写 1 可以复位触发器的输出。如果触发器的输出作为 CLA 的输出，建议在使能 CLA 单元之前置位 FFRST。

如果 OEN 位复位，那么 CLAxOE 也复位，对应的 GPIO 引脚输出失能。

每个 CLA 单元都有一个 HCLK同步输出信号 CLAx_TRGO，该信号作为触发信号被发送到发送到TRIGSEL，TRIGSEL 允许软件选择输出到 ADC、DAC 和 SYSCFG。

## 11.4.4. 中断

CLA_INTF 寄存器中有八个中断标志位，它们分别是 CLA3PF、CLA3NF、CLA2PF、CLA2NFCLA1PF、CLA1NF、CLA0PF、CLA0NF。对于每一个标志位，在 CLA_GCTL 寄存器中都有一个对应的中断使能位。CLA 中断逻辑如 11-2. CLA 所示，当检测到标志位置位并且对应的中断使能位使能，就会产生中断。


图 11-2. CLA 中断逻辑


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/f8f80d0855565fdba73bca53bd6d3bb02f831897311ebc7595560cc22a570829.jpg)

