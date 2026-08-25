## 8. 直接存储器访问控制器（DMA）

## 8.1. 简介

DMA 控制器提供了一种硬件传输方式，在外设和存储器之间或者存储器和存储器之间传输数据，而无需 CPU 的介入，从而使 CPU 可以专注在处理其他系统功能上。DMA 控制器有 14 个通道（DMA0 有 7 个通道，DMA1 有 7 个通道）。每个通道都是专门用来处理一个或多个外设的存储器访问请求的。DMA 控制器内部实现了一个仲裁器，用来仲裁多个 DMA请求的优先级。

DMA 控制器和 Cortex®-M33 内核共享系统总线。当 DMA 和 CPU 访问同样的地址空间时，DMA访问可能会阻挡 CPU 访问系统总线几个总线周期。总线矩阵中实现了循环仲裁算法来分配 DMA与 CPU 的访问权，它可以确保 CPU 得到至少一半的系统总线带宽。

## 8.2. 主要特征

 传输数据长度可编程配置，最大到 65536；

 14 个通道（DMA0 有 7 个通道，DMA1 有 7 个通道），并且每个通道都可配置；

 AHB和 APB 外设，片上闪存和 SRAM 都可以作为访问的源端和目的端；

 每个通道连接固定的硬件 DMA请求；

 支持 DMA 软件优先级（低、中、高、极高）和硬件优先级（DMA通道 0 的优先级最高，DMA通道 6 的优先级最低）；

 存储器和外设的数据传输宽度可配置：字节，半字，字；

 存储器和外设的数据传输支持固定寻址和增量式寻址；

 支持循环传输模式；

 支持外设到存储器，存储器到外设，存储器到存储器的数据传输；

 每个通道有 3 种类型的事件标志和独立的中断；

 支持中断使能和清除。

## 8.3. 结构框图


图 8-1. DMA 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/92026a392b1f7bb855326fe0035851dde4338df0a972b7e67cd5b6b11d253e60.jpg)


由 8-1. DMA 所示，DMA控制器由 4 部分组成：

 AHB 从接口配置 DMA；

 AHB 主接口进行数据传输，用于存储器访问和外设访问；

 仲裁器进行 DMA请求的优先级管理；

 通道管理用于控制数据/地址选择和数据计数。

## 8.4. 功能说明

## 8.4.1. DMA 操作

DMA传输分为两步操作：从源地址读取数据，之后将读取的数据存储到目的地址。DMA控制器基于 DMA_CHxPADDR、DMA_CHxMADDR、DMA_CHxCTL 寄存器的值计算下一次操作的源/目的地址。DMA_CHxCNT 寄存器用于控制传输的次数。DMA_CHxCTL 寄存器的 PWIDTH 和 MWIDTH位域决定每次发送和接收的字节数（字节/半字/字）。

假设 DMA_CHxCNT 寄存器的值为 4，并且 PNAGA 和 MNAGA 位均置位。结合 PWIDTH 和MWIDTH 的各种配置，DMA 传输的操作详见 8-1. DMA 。


表 8-1. DMA 传输操作


<table><tr><td colspan="2">传输宽度</td><td colspan="2">传输操作</td></tr><tr><td>源</td><td>目标</td><td>源</td><td>目标</td></tr><tr><td>32 bits</td><td>32 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B3B2B1B0[31:0] @0x02: Write B7B6B5B4[31:0] @0x43: Write BBBAB9B8[31:0] @0x84: Write BFBEBDBC[31:0] @0xC</td></tr><tr><td>32 bits</td><td>16 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B1B0[15:0] @0x02: Write B5B4[15:0] @0x23: Write B9B8[15:0] @0x44: Write BDBC[15:0] @0x6</td></tr><tr><td>32 bits</td><td>8 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B0[7:0] @0x02: Write B4[7:0] @0x13: Write B8[7:0] @0x24: Write BC[7:0] @0x3</td></tr><tr><td>16 bits</td><td>32 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write 0000B1B0[31:0] @0x02: Write 0000B3B2[31:0] @0x43: Write 0000B5B4[31:0] @0x84: Write 0000B7B6[31:0] @0xC</td></tr><tr><td>16 bits</td><td>16 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write B1B0[15:0] @0x02: Write B3B2[15:0] @0x23: Write B5B4[15:0] @0x44: Write B7B6[15:0] @0x6</td></tr><tr><td>16 bits</td><td>8 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write B0[7:0] @0x02: Write B2[7:0] @0x13: Write B4[7:0] @0x24: Write B6[7:0] @0x3</td></tr><tr><td>8 bits</td><td>32 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1: Write 000000B0[31:0] @0x02: Write 000000B1[31:0] @0x43: Write 000000B2[31:0] @0x84: Write 000000B3[31:0] @0xC</td></tr><tr><td>8 bits</td><td>16 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1, Write 00B0[15:0] @0x02, Write 00B1[15:0] @0x23, Write 00B2[15:0] @0x44, Write 00B3[15:0] @0x6</td></tr><tr><td>8 bits</td><td>8 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1, Write B0[7:0] @0x02, Write B1[7:0] @0x13, Write B2[7:0] @0x24, Write B3[7:0] @0x3</td></tr></table>

DMA_CHxCNT寄存器的CNT位域必须在CHEN位置位前被配置，该位域控制传输的次数。在传输过程中，CNT位域的值表示还有多少次数据传输将被执行。

将 DMA_CHxCTL 寄存器的 CHEN 位清零，可以停止 DMA 传输。

 若 CHEN 位被清零时 DMA 传输还未完成，重新使能 CHEN 位 DMA 传输将分两种情况：

在重新使能 DMA通道前，未对该通道的相关寄存器进行操作，则 DMA将继续完成上次的传输；

在重新使能 DMA 通道前，对相应通道的 DMA_CHxCNT、DMA_CHxPADDR 或DMA_CHxMADDR 寄存器进行了操作，则 DMA 将开始一次新的传输。

若清零 CHEN 位时，DMA 传输已经完成，之后未对相应通道的 DMA_CHxCNT、DMA_CHxPADDR 或 DMA_CHxMADDR 寄存器进行操作前便使能 DMA 通道，则不会触发任何 DMA 传输。

## 8.4.2. 外设握手

为了保证数据的有效传输，DMA控制器中引入了外设和存储器的握手机制，包括请求信号和应答信号：

 请求信号：由外设发出，表明外设已经准备好发送或接收数据；

 应答信号：由 DMA控制器响应，表明 DMA 控制器已经发送 AHB 命令去访问外设。

8-2. 中详细描述了DMA控制器与外设之间的握手机制。


图 8-2. 握手机制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/a1eb4ddfd42a81be6fd7ee6167159e112167cd46b55353f18017bd8c9f507124.jpg)


## 8.4.3. 仲裁

当DMA控制器在同一时间接收到多个外设请求时，仲裁器将根据外设请求的优先级来决定响应哪一个外设请求。优先级包括软件优先级和硬件优先级，优先级规则如下：

软件优先级：分为4级，低，中，高和极高。可以通过寄存器DMA_CHxCTL的PRIO位域来配置；

硬件优先级：当通道具有相同的软件优先级时，编号低的通道优先级高。例：通道0和通道2配置为相同的软件优先级时，通道0的优先级高于通道2。

## 8.4.4. 地址生成

存储器和外设都独立的支持两种地址生成算法：固定模式和增量模式。寄存器DMA_CHxCTL的PNAGA和MNAGA位分别用来设置存储器和外设的地址生成算法。

在固定模式中，地址一直固定为初始化的基地址（DMA_CHxPADDR，DMA_CHxMADDR）。

在增量模式中，下一次传输数据的地址是当前地址加1（或者2，4），这个值取决于数据传输宽度。

## 8.4.5. 循环模式

循环模式用来处理连续的外设请求（如ADC扫描模式）。将DMA_CHxCTL寄存器的CMEN位置位可以使能循环模式。

在循环模式中，当每次DMA传输完成后，CNT值会被重新载入，且传输完成标志位会被置1。DMA会一直响应外设的请求，直到通道使能位（DMA_CHxCTL寄存器的CHEN位）被清0。

## 8.4.6. 存储器到存储器模式

将DMA_CHxCTL寄存器的M2M位置位可以使能存储器到存储器模式。在此模式下，DMA通道传输数据时不依赖外设的请求信号。一旦DMA_CHxCTL寄存器的CHEN位被置1，DMA通道就立即开始传输数据，直到DMA_CHxCNT寄存器达到0，DMA传输才会停止。

## 8.4.7. 通道配置

要启动一次新的 DMA 数据传输，建议遵循以下步骤进行操作：

1. 读取 CHEN 位，如果为 1（通道已使能），清零该位。当 CHEN 为 0 时，请按照下列步骤配置DMA开始新的传输；

2. 配置 DMA_CHxCTL 寄存器的 M2M 及 DIR 位，选择传输模式；

3. 配置 DMA_CHxCTL 寄存器的 CMEN 位，选择是否使能循环模式；

4. 配置 DMA_CHxCTL 寄存器的 PRIO 位域，选择该通道的软件优先级；

5. 通过 DMA_CHxCTL 寄存器配置存储器和外设的传输宽度以及存储器和外设地址生成算法；

6. 通过 DMA_CHxCTL 寄存器配置传输完成中断，半传输完成中断，传输错误中断的使能位；

7. 通过 DMA_CHxPADDR 寄存器配置外设基地址；

8. 通过 DMA_CHxMADDR 寄存器配置存储器基地址；

9. 通过 DMA_CHxCNT 寄存器配置数据传输总量；

10. 将 DMA_CHxCTL 寄存器的 CHEN 位置 1，使能 DMA 通道。

## 8.4.8. 中断

每个DMA通道都有一个专用的中断。中断事件有三种类型：传输完成，半传输完成和传输错误。

每一个中断事件在DMA_INTF寄存器中有专用的标志位，在DMA_INTC寄存器中有专用的清除位，在DMA_CHxCTL寄存器中有专用的使能位。 8-2. 描述了其对应关系。


表 8-2. 中断事件


<table><tr><td rowspan="2">中断事件</td><td>标志位</td><td>清除位</td><td>使能位</td></tr><tr><td>DMA_INTF</td><td>DMA_INTC</td><td>DMA_CHxCTL</td></tr><tr><td>传输完成</td><td>FTFIF</td><td>FTFIFC</td><td>FTFIE</td></tr><tr><td>传输半完成</td><td>HTFIF</td><td>HTFIFC</td><td>HTFIE</td></tr><tr><td>传输错误</td><td>ERRIF</td><td>ERRIFC</td><td>ERRIE</td></tr></table>

DMA中断逻辑如 8-3. DMA 所示，任何类型中断使能时，产生了相应中断事件均会产生中断。


图 8-3. DMA 中断逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/c1c20f7ce9545887b86f5195e2355249f02227b260895586a87a5ee840feebba.jpg)



注意：“x” 表示通道数（对应x=0…6）


## 8.4.9. DMA 请求映射

每个 DMA 通道的请求都连接至由 DMAMUX 请求复用器的对应通道输出来转发的 AHB / APB 外设请求，参考 9-3. DMAMUX 。
