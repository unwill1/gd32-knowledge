## 11. 直接存储器访问控制器（DMA）

## 11.1. 简介

DMA 控制器提供了一种硬件的方式在外设和存储器之间或者存储器和存储器之间传输数据，而无需 CPU 的介入，从而使 CPU 可以专注在处理其他系统功能上。DMA 控制器有 12 个通道（DMA0 有 7 个通道，DMA1 有 5 个通道）。每个通道都是专门用来处理一个或多个外设的存储器访问请求的。DMA 控制器内部实现了一个仲裁器，用来仲裁多个 DMA 请求的优先级。

DMA 控制器和 Cortex®-M33 内核共享系统总线。当 DMA 和 CPU 访问同样的地址空间时，DMA访问可能会阻挡 CPU 访问系统总线几个总线周期。总线矩阵中实现了循环仲裁算法来分配 DMA与 CPU 的访问权，它可以确保 CPU 得到至少一半的系统总线带宽。

## 11.2. 主要特性

 传输数据长度可编程配置，最大到 65536；

 12 个通道，并且每个通道都可配置（DMA0 有 7 个通道，DMA1 有 5 个通道）；

 AHB和 APB外设，片上闪存和 SRAM 都可以作为访问的源端和目的端；

 每个通道连接固定的硬件 DMA请求；

 支持软件优先级（低、中、高、极高）和硬件优先级（通道号越低，优先级越高）；

 存储器和外设的数据传输宽度可配置：字节，半字，字；

 存储器和外设的数据传输支持固定寻址和增量式寻址；

 支持循环传输模式；

 支持外设到存储器，存储器到外设，存储器到存储器的数据传输；

 每个通道有 3 种类型的事件标志和独立的中断；

 支持中断的使能和清除。

## 11.3. 结构框图


图 11-1. DMA 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/12161cd799f494444fdae5a39a978e2b405cbb203044aefb1ead036b7541a036.jpg)



由 11-1. DMA 所示，DMA 控制器由 4 部分组成：


 AHB 从接口配置 DMA

 AHB 主接口进行数据传输

 仲裁器进行 DMA请求的优先级管理

 数据处理和计数

## 11.4. 功能描述

## 11.4.1. DMA 操作

DMA传输分为两步操作：从源地址读取数据，之后将读取的数据存储到目的地址。DMA 控制器基于 DMA_CHxPADDR、DMA_CHxMADDR、DMA_CHxCTL 寄存器的值计算下一次操作的源/目的地址。DMA_CHxCNT 寄存器用于控制传输的次数。DMA_CHxCTL 寄存器的PWIDTH 和 MWIDTH 位域决定每次发送和接收的字节数（字节/半字/字）。

假设 DMA_CHxCNT 寄存器的值为 4，并且 PNAGA 和 MNAGA 位均置位。结合 PWIDTH 和MWIDTH 的各种配置，DMA 传输的操作详见 11-1. DMA 。


表 11-1. DMA 传输操作


<table><tr><td colspan="2">传输宽度</td><td colspan="2">传输操作</td></tr><tr><td>源</td><td>目标</td><td>源</td><td>目标</td></tr><tr><td>32 bits</td><td>32 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B3B2B1B0[31:0] @0x02: Write B7B6B5B4[31:0] @0x43: Write BBBAB9B8[31:0] @0x84: Write BFBEBDBC[31:0] @0xC</td></tr><tr><td>32 bits</td><td>16 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B1B0[15:0] @0x02: Write B5B4[15:0] @0x23: Write B9B8[15:0] @0x44: Write BDBC[5:0] @0x6</td></tr><tr><td>32 bits</td><td>8 bits</td><td>1: Read B3B2B1B0[31:0] @0x02: Read B7B6B5B4[31:0] @0x43: Read BBBAB9B8[31:0] @0x84: Read BFBEBDBC[31:0] @0xC</td><td>1: Write B0[7:0] @0x02: Write B4[7:0] @0x13: Write B8[7:0] @0x24: Write BC[7:0] @0x3</td></tr><tr><td>16 bits</td><td>32 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write 0000B1B0[31:0] @0x02: Write 0000B3B2[31:0] @0x43: Write 0000B5B4[31:0] @0x84: Write 0000B7B6[31:0] @0xC</td></tr><tr><td>16 bits</td><td>16 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write B1B0[15:0] @0x02: Write B3B2[15:0] @0x23: Write B5B4[15:0] @0x44: Write B7B6[15:0] @0x6</td></tr><tr><td>16 bits</td><td>8 bits</td><td>1: Read B1B0[15:0] @0x02: Read B3B2[15:0] @0x23: Read B5B4[15:0] @0x44: Read B7B6[15:0] @0x6</td><td>1: Write B0[7:0] @0x02: Write B2[7:0] @0x13: Write B4[7:0] @0x24: Write B6[7:0] @0x3</td></tr><tr><td>8 bits</td><td>32 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1: Write 000000B0[31:0] @0x02: Write 000000B1[31:0] @0x43: Write 000000B2[31:0] @0x84: Write 000000B3[31:0] @0xC</td></tr><tr><td>8 bits</td><td>16 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1, Write 00B0[15:0] @0x02, Write 00B1[15:0] @0x23, Write 00B2[15:0] @0x44, Write 00B3[15:0] @0x6</td></tr><tr><td>8 bits</td><td>8 bits</td><td>1: Read B0[7:0] @0x02: Read B1[7:0] @0x13: Read B2[7:0] @0x24: Read B3[7:0] @0x3</td><td>1, Write B0[7:0] @0x02, Write B1[7:0] @0x13, Write B2[7:0] @0x24, Write B3[7:0] @0x3</td></tr></table>


DMA_CHxCNT 寄存器的 CNT 位域必须在 CHEN 位置位前被配置，其控制传输的次数。在传输过程中，CNT 位域的值表示还有多少次数据传输将被执行。


将 DMA_CHxCTL 寄存器的 CHEN 位清零，可以停止 DMA 传输。

若 CHEN 位被清零时 DMA 传输还未完成，重新使能 CHEN 位将分两种情况：在重新使能 DMA 通道前，未对该通道的相关寄存器进行操作，则 DMA 将继续完成上次的传输。

在重新使能 DMA 通道前，对相应通道的 DMA_CHxCNT、DMA_CHxPADDR 或DMA_CHxMADDR 寄存器进行了操作，则 DMA 将开始一次新的传输。

 若清零 CHEN 位时，DMA 传输已经完成，之后未对相应通道的 DMA_CHxCNT、DMA_CHxPADDR 或 DMA_CHxMADDR 寄存器进行操作前便使能 DMA 通道，则不会触发任何 DMA传输。

## 11.4.2. 外设握手

为了保证数据的有效传输，DMA 控制器中引入了外设和存储器的握手机制，包括请求信号和应答信号：

 请求信号：由外设发出，表明外设已经准备好发送或接收数据；

■ 应答信号：由 DMA控制器响应，表明 DMA控制器已经发送 AHB 命令去访问外设。

11-2. 中详细描述了DMA控制器与外设之间的握手机制。


图 11-2. 握手机制


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/0d0aec6809e8aceabca38126bd4f39fd21f6ba956c383107b246a78137b804f3.jpg)


## 11.4.3. 仲裁

当 DMA 控制器在同一时间接收到多个外设请求时，仲裁器将根据外设请求的优先级来决定响应哪一个外设请求。优先级包括软件优先级和硬件优先级，优先级规则如下：

 软件优先级：分为4级，低，中，高和极高。可以通过寄存器DMA_CHxCTL的PRIO位域来配置。

 硬件优先级：当通道具有相同的软件优先级时，编号低的通道优先级高。例：通道0和通道2配置为相同的软件优先级时，通道0的优先级高于通道2。

## 11.4.4. 地址生成

存储器和外设都独立的支持两种地址生成算法：固定模式和增量模式。寄存器 DMA_CHxCTL的 PNAGA 和 MNAGA 位用来设置存储器和外设的地址生成算法。

在固定模式中，地址一直固定为初始化的基地址（DMA_CHxPADDR，DMA_CHxMADDR）。在增量模式中，下一次传输数据的地址是当前地址加 1（或者 2，4），这个值取决于数据传输宽度。

## 11.4.5. 循环模式

循环模式用来处理连续的外设请求(如 ADC 扫描模式)。将 DMA_CHxCTL 寄存器的 CMEN 位置位可以使能循环模式。

在循环模式中，当每次 DMA传输完成后，CNT 值会被重新载入，且传输完成标志位会被置 1。DMA会一直响应外设的请求，直到通道使能位（DMA_CHxCTL 寄存器的 CHEN 位）被清 0。

## 11.4.6. 存储器到存储器模式

将 DMA_CHxCTL 寄存器的 M2M 位置位可以使能存储器到存储器模式。在此模式下，DMA 通道传输数据时不依赖外设的请求信号。一旦 DMA_CHxCTL 寄存器的 CHEN 位被置 1，DMA通道就立即开始传输数据，直到 DMA_CHxCNT 寄存器达到 0，DMA 通道才会停止。

## 11.4.7. 通道配置

要启动一次新的 DMA 数据传输，建议遵循以下步骤进行操作：

1. 读取 CHEN 位，如果为 1（通道已使能），清零该位。当 CHEN 为 0 时，请按照下列步骤配置 DMA 开始新的传输；

2. 配置 DMA_CHxCTL 寄存器的 M2M 及 DIR 位，选择传输模式；

3. 配置 DMA_CHxCTL 寄存器的 CMEN 位，选择是否使能循环模式；

4. 配置 DMA_CHxCTL 寄存器的 PRIO 位域，选择该通道的软件优先级；

5. 通过 DMA_CHxCTL 寄存器配置存储器和外设的传输宽度以及存储器和外设地址生成算法；

6. 通过 DMA_CHxCTL 寄存器配置传输完成中断，半传输完成中断，传输错误中断的使能位；

7. 通过 DMA_CHxPADDR 寄存器配置外设基地址；

8. 通过 DMA_CHxMADDR 寄存器配置存储器基地址；

9. 通过 DMA_CHxCNT 寄存器配置数据传输总量；

10. 将 DMA_CHxCTL 寄存器的 CHEN 位置 1，使能 DMA 通道。

## 11.4.8. 中断

每个 DMA 通道都有一个专用的中断。中断事件有三种类型：传输完成，半传输完成和传输错误。

每一个中断事件在 DMA_INTF 寄存器中有专用的标志位，在 DMA_INTC 寄存器中有专用的清除位，在 DMA_CHxCTL 寄存器中有专用的使能位。 11-2. 描述了其对应关系。


表 11-2. 中断事件


<table><tr><td rowspan="2">中断事件</td><td>标志位</td><td>清除位</td><td>使能位</td></tr><tr><td>DMA_INTF</td><td>DMA_INTC</td><td>DMA_CHxCTL</td></tr><tr><td>传输完成</td><td>FTFIF</td><td>FTFIFC</td><td>FTFIE</td></tr><tr><td>半传输完成</td><td>HTFIF</td><td>HTFIFC</td><td>HTFIE</td></tr><tr><td>传输错误</td><td>ERRIF</td><td>ERRIFC</td><td>ERRIE</td></tr></table>

DMA中断逻辑如 11-3. DMA0 所示，任何类型中断使能时，产生了相应中断事件均会产生中断。


图 11-3. DMA 中断逻辑图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/40dcd87b8823985e54714f43ceba26ed71190a2963637af5fdb87c7390373985.jpg)



注意：“x” 表示通道数（DMA0对应x=0…6；DMA1对应x=0…4）


## 11.4.9. DMA请求映射

多个外设请求被映射到同一个 通道。这些请求信号在经过逻辑或后进入 。详情可见11-4. DMA0 和 11-5. DMA1 。通过配置对应外设的寄存器，每个外设的请求均可以独立的开启或关闭。用户必须确保同一时间，在同一个通道上仅有一个外设的请求被开启。 11-3. DMA0 列举了 DMA0 的每个通道所支持的外设请求， 11-4.DMA1 列举了 DMA1 的每个通道所支持的外设请求。


图 11-4. DMA0 请求映射


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/0cb9d022a3f96abdb86486cefd2279200d20766815638bf97f05668fb284011d.jpg)



表 11-3. DMA0 各通道请求表


<table><tr><td>Peripheral</td><td>Channel 0</td><td>Channel 1</td><td>Channel 2</td><td>Channel 3</td><td>Channel 4</td><td>Channel 5</td><td>Channel 6</td></tr><tr><td>TIMER0</td><td>●</td><td>TIMER0_CH0</td><td>TIMER0_CH1</td><td>TIMER0_CH3TIMER0_TGTIMER0_CMT</td><td>TIMER0_UP</td><td>TIMER0_CH2</td><td>●</td></tr><tr><td>TIMER1</td><td>TIMER1_CH2</td><td>TIMER1_UP</td><td>●</td><td>●</td><td>TIMER1_CH0</td><td>●</td><td>TIMER1_CH1TIMER1_CH3</td></tr><tr><td>TIMER2</td><td>●</td><td>TIMER2_CH2</td><td>TIMER2_CH3 TIMER2_UP</td><td>●</td><td>●</td><td>TIMER2_CH0 TIMER2_TG</td><td>●</td></tr><tr><td>TIMER3</td><td>TIMER3_CH0</td><td>●</td><td>●</td><td>TIMER3_CH1</td><td>TIMER3_CH2</td><td>●</td><td>TIMER3_UP</td></tr><tr><td>ADC0</td><td>ADC0</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>SPI/I2S</td><td>●</td><td>SPI0_RX</td><td>SPI0_TX</td><td>SPI1/I2S1_RX</td><td>SPI1/I2S1_TX</td><td>I2S1ADD_RX</td><td>I2S1ADD_TX</td></tr><tr><td>USART</td><td>●</td><td>USART2_TX</td><td>USART2_RX</td><td>USART0_TX</td><td>USART0_RX</td><td>USART1_RX</td><td>USART1_TX</td></tr><tr><td>I2C</td><td>●</td><td>●</td><td>●</td><td>I2C1_TX I2C2_TX</td><td>I2C1_RX I2C2_RX</td><td>I2C0_TX</td><td>I2C0_RX</td></tr><tr><td>SHRTIMER</td><td>●</td><td>SHRTIMER_M</td><td>SHRTIMER_0</td><td>SHRTIMER_1</td><td>SHRTIMER_2</td><td>SHRTIMER_3</td><td>SHRTIMER_4</td></tr><tr><td>TIMER14</td><td>●</td><td>●</td><td>●</td><td>●</td><td>TIMER14_CH0 TIMER14_UP TIMER14_TG TIMER14_COM</td><td>●</td><td>●</td></tr><tr><td>TIMER15</td><td>●</td><td>●</td><td>TIMER15_CH0 TIMER15_UP</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>TIMER16</td><td>TIMER16_CH0 TIMER16_UP</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>


图 11-5. DMA1 请求映射


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/57f361e2-ad2e-48cc-8966-381023c49c5e/a0fab411f10f5285721efceb1bf6bc9be271cbca262e62302d2b34b1bf1cf45a.jpg)



表 11-4. DMA1 各通道请求表


<table><tr><td>Peripheral</td><td>Channel 0</td><td>Channel 1</td><td>Channel 2</td><td>Channel 3</td><td>Channel 4</td></tr><tr><td rowspan="2">TIMER4</td><td>TIMER4_CH3</td><td>TIMER4_CH2</td><td rowspan="2">●</td><td rowspan="2">TIMER4_CH1</td><td rowspan="2">TIMER4_CH0</td></tr><tr><td>TIMER4_TG</td><td>TIMER4_UP</td></tr><tr><td>TIMER5</td><td>●</td><td>●</td><td>TIMER5_UP</td><td>●</td><td>●</td></tr><tr><td>TIMER6</td><td>●</td><td>●</td><td>●</td><td>TIMER6_UP</td><td>●</td></tr><tr><td rowspan="3">TIMER7</td><td>TIMER7_CH2</td><td>TIMER7_CH3</td><td rowspan="3">TIMER7_CH0</td><td rowspan="3">●</td><td rowspan="3">TIMER7_CH1</td></tr><tr><td rowspan="2">TIMER7_UP</td><td>TIMER7_TG</td></tr><tr><td>TIMER7_CMT</td></tr><tr><td>ADC2</td><td>●</td><td>●</td><td>●</td><td>●</td><td>ADC2</td></tr><tr><td>DAC0</td><td>●</td><td>●</td><td>DAC0_OUT0</td><td>DAC0_OUT1</td><td>●</td></tr><tr><td>SPI/I2S</td><td>SPI2/I2S2_R</td><td>SPI2/I2S2_TX</td><td>I2S2ADD_RX</td><td>I2S2ADD_TX</td><td>●</td></tr><tr><td>USART</td><td>●</td><td>●</td><td>UART3_RXUSART5_RX</td><td>●</td><td>UART3_TXUSART5_TX</td></tr><tr><td>SDIO</td><td>●</td><td>●</td><td>●</td><td>SDIO</td><td>●</td></tr><tr><td>DAC1</td><td>●</td><td>●</td><td>●</td><td>●</td><td>DAC1_OUT0</td></tr></table>
