## 26. 串行音频接口（SAI）

## 26.1. 简介

串行音频接口（SAI）用于支持各种通用的音频协议，如I2S、PCM/DSP、AC’97、LSB或MSB对齐和TDM，它适用于单声道和立体声。

为了初始化这些配置，SAI用了两个完全独立的音频子模块。每个音频子模块包含多达4个IO引脚（SD，SCK，FS和MCLK）。当两个音频子模块配置成相互同步时，部分IO引脚可以共用。

SAI可以配置成主/从、发送/接收的任何组合模式，根据音频子模块同步/异步配置，可以设置其操作模式为全双工/单工。本系列只有一个SAI，所以不支持外部同步模式。

## 26.2. 主要特征

- 两个独立的音频子模块；

- 每个音频子模块可以配置成主/从、发送/接收的任何组合，并都具有一个8字的FIFO；

- 本地时钟分频逻辑用于满足各种音频采样率；

- 可灵活配置的音频协议，如I2S，PCM/DSP，AC’97，LSB或MSB对齐和TDM；

- 具有单声道/立体声音频能力，支持静音设置；

- 帧同步配置（有效电平、有效长度和偏移）；

- 每个音频帧包含多达16个可配置的slot；

- 灵活的配置slot长度，并且可以配置slot为有效或无效；

- 每个slot能够支持一个大小为8位、10位、16位、20位、24位或32位的数据，并且可以配置这些数据的第一位偏移、LSB或MSB传输；

- 串行时钟选通边沿选择（SCK）；

- 错误标志位和中断源：

FIFO上溢和下溢；

从模式时，帧同步提前检测；

从模式时，帧同步滞后检测；

AC’97编解码器未就绪；

时钟配置错误；

- 每个音频子模块都有2个独立的DMA接口，支持频率高达4MHz的从机模式。

## 26.3. 功能描述

## 26.3.1. 模块框图


图 26-1. 模块框图


![image](images/c0e4ba879bf1.jpg)


灵活的音频收发器整合了两个相同的独立子模块，并具有一个连接到输出的IO管理模块。每个音频子模块由三个独立的时域组成，分别为SAI_CK、SCK和PCLK域。定义音频采样率时钟分频逻辑设计在SAI_CK域，它的时钟输出到SCK域。SCK域包含SAI主要功能状态机、压缩/解压、发送 接收逻辑和中断产生逻辑。主要的控制寄存器和同步 位于 域。同步 可以被 C 的 总线或 控制器访问。

每个音频子模块可以配置成主/从、发送/接收两者的任意组合。帧同步（FS）和串行时钟（SCK）在主模式下产生，在从模式下，音频子模块从外部主机或同步模式下另一个音频子模块接收这两个信号。主时钟（MCLK）只有在主模式时才产生，用来供外部DAC/ADC操作。有一个例外，当SAI配成支持AC’97协议时，FS强制变成输出信号，这与主/从配置无关。串行数据（SD）IO引脚在发送时配成输出，接收时配成输入。

管理模块控制每个音频子模块的 引脚，当两个音频子模块被声明为互相同步时， 、和MCLK可以共用，同步子模块的这些引脚被释放，并可用作通用IO。

## 26.3.2. 时钟分频器

SAI的两个音频子模块的时钟分频逻辑只有在当它们配置成主设备时才打开，否则是关闭的，并且MCLK和SCK的输出都保持低电平。分频器的时钟源SAI_CK（参考复位和时钟单元（RCU））推荐采用45.1584MHz和49.152MHz这两个特定值来产生标准的音频采样率。时钟分频逻辑由主时钟分频器和子时钟分频器组成，其中主时钟分频器用于产生所需的主时钟（ ），子时钟分频器用于产生位时钟（SCK）。时钟分频逻辑如图26-2. 时钟分频逻辑所示。


图 26-2. 时钟分频逻辑


![image](images/a0f6797c0a96.jpg)


主时钟分频比 MDIV直接链接到SAI控制寄存器内的主时钟分频比控制字段，其输出频率可通过以下公式获得。

$$
f _ {\text {MCLK}} = \left\{ \begin{array}{l} \frac {f _ {\text {SAI\_CK}}}{\text {MDIV}}, \text {MDIV} \neq 0 \\ f _ {\text {SAI\_CK}}, \text {MDIV} = 0 \end{array} \right.\tag{26-1}
$$

注意：以上公式仅在 BYPASS无效、SAI开启且 MCKEN开启时成立，否则 MCLK保持低电平。

辅助时钟分频器的比率 MDIV连接到SAI控制寄存器内的帧长度（FWD）和MCLK过采样率（MOSPR）控制字段。以下公式决定了 $\mathsf { S A l \_ C K }$ 与位时钟（SCK）采样率之间的关系。

$$
f _ {S C K} = \frac {f _ {S A I \_ C K} \times (F W D + 1)}{M D I V \times (M O S P R + 1) \times 2 5 6}\tag{26-2}
$$

帧同步频率 $\mathsf { f } _ { \mathsf { F S } } .$ 

$$
f _ {F S} = \frac {f _ {S A I \_ C K}}{M D I V \times (M O S P R + 1) \times 2 5 6}\tag{26-3}
$$

当 BYPASS 置位时，主时钟（MCLK）以固定输出值 0 关闭，而位时钟（SCK）取决于 MDIV。另外，帧长值没有限制，只要帧长大于等于 8 即可。

当 BYPASS 清零时，需要设置（FWD + 1）等于 master模式下基数为 2 的指数函数的结果，以保证 SCK 可被 MCLK整除。

26 1 列出了帧长度为 2 6 位时一些常用的音频采样率配置。

## 表26-1. 常用的音频采用率

<table><tr><td>SAI_CK时钟频率</td><td>标准音频采样率</td><td>主时钟分频率</td></tr><tr><td rowspan="5">192kHz x 256</td><td>192 kHz</td><td>MDIV = 1</td></tr><tr><td>96 kHz</td><td>MDIV = 2</td></tr><tr><td>48 kHz</td><td>MDIV = 4</td></tr><tr><td>16 kHz</td><td>MDIV = 12</td></tr><tr><td>8 kHz</td><td>MDIV = 24</td></tr><tr><td rowspan="3">44.1kHz x 256</td><td>44.1 kHz</td><td>MDIV = 1</td></tr><tr><td>22.05 kHz</td><td>MDIV = 2</td></tr><tr><td>11.025 kHz</td><td>MDIV = 4</td></tr></table>

## 26.3.3. 操作模式

SAI音频子模块可以独立的配置成主/从、发送/接收任何组合的操作模式。

## 主设备

帧同步（FS）是由主设备在FIFO不为空且帧开始时生成，它用来协调帧开始或通道识别。串行时钟（SCK）和主时钟（MCLK）都是由主设备生成的信号，SCK信号专门被从设备用来作为位时钟。和FS不同，SCK和MCLK的产生不受FIFO是否为空的制约，只要音频子模块被使能，他们就会生成。

## 从设备

从设备接收来自主设备的FS和SCK信号，这些信号的来源取决于音频子模块是声明为同步还是异步。当选择异步模式时，FS和SCK信号源被直接关联到芯片级IO端口。当选择同步模式时，FS和SCK信号源被连接到另一个音频子模块的FS和SCK信号端。用户必须在使能主设备前先使能从设备，否则从设备将不能完整地接收主设备的数据。

## 发送器

当音频子模块被配置成发送器时，串行数据（SD）为输出。如果在音频子模块使能之后FIFO还是为空，则会发送数值0，并产生下溢标志（OUERR）。

## 接收器

当音频子模块被配置成接收器时，串行数据（SD）为输入。从接收器总会监测FS信号，当检测到第一个有效边沿时，音频子模块存储接收到的数据，然后由内部有限态机器处理后续数据的接收。当SAI失能时，接收器会在帧结束时才停止接收。

## 26.3.4. 同步模式

该系列在音频子块级别支持内部同步模式。

## 内部同步

内部同步模式具有减少通信时占用外部引脚数量的优点，即SAI子模块SAI_B0和SAI_B1可以

同步运行，二者将共用SAI_FS和SAI_SCK信号，从而释放SCKx、FSx和MCLKx的GPIO引脚。

内部同步模式下的SAI子模块在全双工通信中可以配置为如下几种模式：

1. 子模块0（或者1）配置为主模块，子模块1（或者0）配置为从模块；

2. 子模块0和子模块1都配置为从模块；

3. 子模块0（或者1）配置为异步模块，子模块1（或者0）配置为同步模块。

注意：由于存在内部重新同步阶段，因此PCLK APB频率必须大于比特率时钟频率的二倍。

本系列只有一个SAI，所以不支持外部同步模式（SAI_SYNCFG中的SYNO和SYNI位需要设置为复位值，SAI_BxCFG0中的SYNCMOD不能设置为2’b10）。

当 SAI 子模块配置为从机模式时，存在同步信号方向限制：该从机子模块只能接收同步信号，无法提供帧同步(FS)信号给其他 SAI 子模块。

从机子模块不能作为同步信号源，只能接收来自主机模块的 FS和 SCK 信号。

在系统设计阶段应充分考虑此限制，合理规划 SAI 模块的主从关系和引脚分配。

## 26.3.5. 帧配置

## 帧同步

帧同步信号是主设备和从设备之间初始化一个传输的协调信号。许多参数用于控制它的波形。

帧同步提前

帧同步有效边沿可以和第一个slot中第一个比特位的开始或者其前一个SCK位时钟对齐，这取决于SAI_SxFCFG寄存器中FSOST控制字段。图26-3. FS有效宽度展示了FS波形是如何改变的。

## 帧同步有效宽度

26-3. FS 中帧同步信号的有效宽度取决于SAI_BxFCFG寄存器的FSAWD控制字段的配置，它的实际宽度等于（FSAWD+1）个SCK时钟周期，且其最小值为1个SCK时钟周期，最大值为 个 时钟周期，即为最大帧宽的一半。当 置 时， 信号不仅表示帧开始，还能表示通道识别，这种情况下，（FSAWD+1）必须等于帧宽的一半，否则音频子模块的功能将不能得到保证。


图 26-3. FS 有效宽度


![image](images/aa6156a4d598.jpg)


## 帧同步极性

帧同步有效电平可以通过SAI_BxFCFG寄存器的FSPL控制字段配置，如图26-4. FS极性所示。


图 26-4. FS 极性


![image](images/eb17313d5f70.jpg)


## 帧同步功能

帧同步功能的定义通过SAI_BxFCFG寄存器的FSFUNC控制字段进行配置。有两个指定的功能可被选择，当FSFUNC置1时，FS不仅表示帧开始还表示通道编号的识别，在这种情况下，帧同步有效宽度（FSAWD+1）应该配置成帧宽的一半，如图26-5. FS功能所示，否则音频子模块的行为将不能得到保证。当FSFUNC为0时，FS只表示帧开始。


图 26-5. FS 功能


![image](images/70dcf3df17f0.jpg)


## 帧宽

帧宽不能小于8位（相当于一个字节的数据），也不能大于256位。

在主模式中，如果BYPASS清0，帧宽（FWD+1）的值应该设置为8到256之间且等于2的几次幂的值，以保证每个SCK时钟周期包含整数个MCLK时钟周期，这是外部DAC/ADC能正确操作的必须要求，否则SAI_BxINTEN寄存器中的错误时钟标志位（ERRCK）会置位，若还使能了SAI_BxINTEN寄存器的错误时钟中断位（ERRCKIE），则产生一个中断。在主模式中，如果BYPASS置1，这将对帧宽的配置没有约束，主时钟自动关闭。

在从模式中，帧宽配置用于配合内部有限状态机来获取有效帧的开始和结束。它还有另一个用途，就是用于检测帧同步信号的提前或滞后，如果出现帧同步提前或滞后现象，则一个错误标志位会被置位，如果使能了相应的中断，则产生一个中断，具体可以参考错误标志位和中断章节。

## 26.3.6. Slot 配置

每个 帧逻辑上最多分为 个 ，每个 的有效状态和它们的分布通过 配置寄存器进一步控制。Slot宽度可以通过SAI_BxSCFG寄存器的SLOTWD控制字段配成16位、32位或是和数据宽度一致。

## Slot 激活

每个slot的激活状态可以通过SAI_BxSCFG寄存器的slot激活向量（SLOTAV）独立配置。SLOTAV是一个16位宽的控制字段，每个比特位控制相应的一个slot的激活状态。Slot的逻辑划

分如图26-6. Slot激活所示。


图 26-6. Slot 激活


![image](images/b07f9d9edf83.jpg)


## Slot 分布

在slot个数和slot宽度的乘积小于帧宽的特殊情况下，存在非slot的分布。Slot部分即为有slot分布的部分，其他的为无效部分。当FSFUNC为0时，FS仅表示信号帧的开始，从最后一个slot结束到下一个帧的开始之间为slot的无效部分，如图26-7. 当FSFUNC=0时 slot分布所示。


图 26-7. 当 FSFUNC=0 时，slot 分布


![image](images/5deee60f9e53.jpg)


当FSFUNC=1，FS不仅表示帧开始，还表示通道识别，slot部分和无效部分均匀分布在两个通道上。无效部分为从当前通道的最后一个slot到下一个通道的slot开始之间的部分。


图 26-8. 当 FSFUNC=1 时，slot 分布


![image](images/6154f6af8d66.jpg)



在无效 slot上的串行数据输出管理


在无效slot附近的串行数据（SD）输出行为可以根据SAI_BxCFG1寄存器中的串行数据输出模式（SDOM）定义的管策略来决定是SAI释放还是驱动输出0、SD输出行为、偏移和空闲区域这三项需要特别注意。在该用户手册中，将slot部分规定为偏移区、数据区和闲置区，具体描述如图26-9. Slot部分的规定所示。


图 26-9. Slot 部分的规定


![image](images/d421f30e4b34.jpg)


首先，偏移区域的SD输出由SDOM决定,SDOM为1，那么SAI将会释放SD的输出，否则SD输出0，其区别如

26-10. 所示。


图 26-10. 偏移区的处理


![image](images/7c7e8df45f77.jpg)


其次，当SDOM为1时，一个帧的最后一个slot的闲置区期间SD输出行为将参考第一个slot的有效状态。如果slot0是无效的时候，SD输出为释放状态，否则如果slot0是有效的，则SD输出0。当SDOM为0时，则SD的输出0，这和其他slot的有效状态无关。

最后，位于帧中间的slot的偏移区和闲置区的SD输出参考它们上一个slot和下一个slot的有效状态。如果上一个 是无效的，并且存在偏移区，那么当 时， 输出线释放，当时，SD输出0。同样，如果下一个slot是无效的，且存在闲置区，那么当SDOM=1时，SD线释放，当SDOM=0时，SD输出0。在有效slot和无效slot附近的偏移区和闲置区的SD输出行为如26-11. SD 所示。


图 26-11. SD 输出管理


![image](images/c5f371e81c06.jpg)


## 26.3.7. 数据配置

数据宽度也是灵活的，它可以通过 SAI_BxCFG0 寄存器的 DATAWD 位将其配置成 8 位、10位、16 位、20 位、24 位和 32 位宽。通过设置 SAI_BxSCFG 寄存器的数据偏移（DATAOST）位，可以将有效 slot 中的数据向前移或是向后移。如部分(帧配置节)所描述的那样，一个 slot开始处与里面数据的第一个比特位之间的空间称为偏移区，数据的最后一个比特位和 slot 结束处之间的空间称为闲置区。当音频子模块配置成发送器，且存在偏移区或闲置区，那么在这些区期间，SD 输出 0。SD 线的实际行为不仅取决于输出值，还取决于线管理条件和附近 slot 的有效状态。当音频子模块配置成接收器，且存在偏移区或闲置区，那么在这些区期间的数据接收将会被忽略。数据发送和接收如图26-12. 数据配置所示。


图 26-12. 数据配置


![image](images/8e0f9874047d.jpg)


## 26.3.8. 同步 FIFO

在每个SAI音频子模块内部独立应用一个8字深的同步FIFO以提高传输效率。这些FIFO可以被C 或是 访问， O请求中断机制用于请求C 和 访问。 O请求的产生取决于操作模式、FIFO阈值、FIFO状态和DMA突发传输大小。FIFO请求中断的产生概括在表26-2. FIFO中，如果根本条件不满足，则中断请求就会被清除。


表 26-2. FIFO 请求的产生条件


<table><tr><td colspan="4">发送: OPTMOD[0] = 0</td><td colspan="4">接收: OPTMOD[0] = 1</td></tr><tr><td>FIFO 阈值</td><td>FFTH</td><td>FIFO状态</td><td>FFSTAT</td><td>FIFO阈值</td><td>FFTH</td><td>FIFO状态</td><td>FFSTAT</td></tr><tr><td>空</td><td>= 000</td><td>空</td><td>= 000</td><td>空</td><td>= 000</td><td>不空</td><td>≥ 001</td></tr><tr><td>1/4 满</td><td>= 001</td><td>&lt;1/4满</td><td>&lt;010</td><td>1/4满</td><td>= 001</td><td>≥ 1/4满</td><td>≥ 010</td></tr><tr><td>1/2满</td><td>= 010</td><td>&lt;1/2满</td><td>&lt;011</td><td>1/2满</td><td>= 010</td><td>≥ 1/2满</td><td>≥ 011</td></tr><tr><td>3/4满</td><td>= 011</td><td>&lt;3/4满</td><td>&lt;100</td><td>3/4满</td><td>= 011</td><td>≥ 3/4满</td><td>≥ 100</td></tr><tr><td>全满</td><td>= 100</td><td>不满</td><td>&lt;101</td><td>全满</td><td>= 100</td><td>全满</td><td>= 101</td></tr></table>


通过设置SAI_BxCFG1寄存器的FLUSH控制字段可以实现FIFO刷新，当FLUSH置1时，FIFO中的所有数据内容将被清除，读写指针复位到0。


注意：DMA请求的产生取决于FIFO请求，DMA接口章节会给出详细信息。

## 26.3.9. AC’97 链路控制器

AC’97链路控制器模式是通过SAI_BxCFG0寄存器的PROT位配置的。当选择了这个协议，有许多配置字段会被忽略，包括数据移位方向、数据宽度、帧和slot的大部分配置以及部分中断控制字段，具体可以参考寄存器定义部分的描述。

AC’97协议的帧宽固定为256位，每个帧被分成13个slot，第一个slot固定为16位宽，其他的12个slot的宽度固定为20位。用户必须设置SAI_BxCFG0寄存器的数据宽度（DATAWD）控制字段为16位或20位，否则将不能保证音频子模块的行为。

TAG（即Slot0）中的位2为保留位，无论写什么值到TAG中，位2均会被写0。

TAG（slot 0）中的位3到位14为自由协议的slot激活向量（SLOTAV），其中TAG slot（即slot 0）总为有效，位3对应slot12，位14对应slot1.

TAG（slot 0）的位15是编解码就绪状态指示位，当音频子模块配置为接收时，接收到的TAG（slot0）的位15为0，则表明音频编解码器没有就绪，相应的ACNRDY标志位置1。如果ACNRDY标志位和音频编解码器未就绪中断使能位（ACNRDYIE）都置1，则产生一个中断。

帧同步有效边沿被声明为数据的第一个比特位的前一个时钟周期，如图26-13. AC’97的slot划所示。


图 26-13. AC’97 的 slot 划分


![image](images/fdd9fad8db96.jpg)



26-14. AC’97 TAG 给出了AC’97slot划分的综述。



图 26-14. AC’97 TAG 定义


![image](images/a2f5a9cdd00f.jpg)


26-3. AC’97 slot 和 26-4. AC’97 slot 概括了每个slot的定义和意义。

当AC’97链路控制器作为发送器时。


表 26-3. AC’97 发送 slot 定义


<table><tr><td>Slot</td><td>名称</td><td>描述</td></tr><tr><td>0</td><td>输出目标</td><td>高位指示哪个slot包含有效数据,低位指示传达编解码器ID</td></tr><tr><td>1</td><td>命令地址端口</td><td>读/写命令和7位的编解码器寄存器地址</td></tr><tr><td>2</td><td>命令数据端口</td><td>16位命令寄存器写数据</td></tr><tr><td>3,4</td><td>PCM回放</td><td>左右声道输入的16、18、20位PCM数据</td></tr><tr><td>5</td><td>Modem Line1 DAC</td><td>Modem line1输出的16位Modem数据</td></tr><tr><td>6,7,8,9</td><td>中置,左右环绕,LEF数据</td><td>中置,左右环绕与LEF通道的16、18、20位PCM数据</td></tr><tr><td>10</td><td>Modem Line2 DAC</td><td>Modem line2输出的16位Modem数据</td></tr><tr><td>11</td><td>Modem听筒</td><td>听筒的16位Modem数据</td></tr><tr><td>12</td><td>Modem IO控制</td><td>用于Modem控制的GPIO写端口I</td></tr><tr><td>10-11</td><td>SPDIF输出</td><td>AC-link可选SPDIF输出带宽</td></tr><tr><td>6-12</td><td>双倍音频数据</td><td>88.2或者96kHz的AC-link可选左,中,右声道带宽。实际使用时间片由DRSS位控制</td></tr></table>


当AC’97链路控制器作为接收器时。



表 26-4. AC’97 接收 slot 定义


<table><tr><td>Slot</td><td>Name</td><td>Description</td></tr><tr><td>0</td><td>输入目标</td><td>高位指示哪个slot包含有效数据;</td></tr><tr><td>1</td><td>状态地址端口</td><td>高位指示寄存器地址,低位指示请求数据的时间片</td></tr><tr><td>2</td><td>状态数据端口</td><td>读取到的16位寄存器数据</td></tr><tr><td>3,4</td><td>PCM录音</td><td>左右声道输出的16、18、20位PCM数据</td></tr><tr><td>5</td><td>Modem Line 1 ADC</td><td>Modem line1输入的16位Modem数据</td></tr><tr><td>6</td><td>话筒专用ADC</td><td>用于第三个可选ADC的16、18、20位PCM数据</td></tr><tr><td>7,8,9</td><td>供应商保留</td><td>供应商特定(增强的输入扩充口,或者麦克风阵列等)</td></tr><tr><td>10</td><td>Modem Line 2 ADC</td><td>Modem line2输入的16位Modem数据</td></tr><tr><td>11</td><td>Modem话筒ADC</td><td>话筒的16位Modem数据</td></tr><tr><td>12</td><td>Modem IO状态</td><td>Modem状态读取GPIO端口</td></tr></table>

## 26.3.10. SPDIF 输出

SPDIF（索尼/飞利浦数字接口）是一种用于消费音频设备的数字音频互连，用于在合理的短距离内输出音频。 SPDIF 支持 IEC 60958 标准。

26-15. SPDIF 显示了 SPDIF 块格式和子帧格式。


图 26-15. SPDIF 数据格式


<table><tr><td colspan="101">块 N</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="100">帧 0</td><td colspan="100">块 N+1</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>M</td><td>Channel A</td><td>W</td><td>Channel B</td><td>M</td><td>Channel A</td><td>W</td><td>Channel B</td><td>M</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td>B</td><td>Channel A</td><td>W</td><td>Channel B</td><td colspan="100">24位音频采样数据状态位28位信息位同步报头B,M,W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="100">子帧</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

每个 SPDIF 块包含 192 帧数据，每个帧由左通道子帧（32 位）和右通道子帧（32 位）组成，每个子帧由 4bit 的 SOPD 模式、24bit 的数据信息和 4bit 的状态信息组成。

SOPD 模式编码参考表26-5. SOPD 模式。


表 26-5. SOPD 模式


<table><tr><td>预先状态(前一个半比特值)</td><td>0</td><td>1</td><td rowspan="2">描述</td></tr><tr><td>报头</td><td colspan="2">编码</td></tr><tr><td>B</td><td>11101000</td><td>00010111</td><td>通道A,且为一个块的起始子帧</td></tr><tr><td>W</td><td>11100100</td><td>00011011</td><td>通道B</td></tr><tr><td>M</td><td>11100010</td><td>00011101</td><td>通道A</td></tr></table>

SPDIF 的数据传输在 SAI_BxDATA 寄存器的数据填充应遵循：SAI_BxDATA[26:24]包含通道状态位、用户位和有效性位，SAI_BxDATA[23:0]包含所考虑通道的 24 位数据。

注意：如果数据大小为 20/16 位，应将数据映射到 SAI_BxDATA[23:4] /SAI_BxDATA[23:8]上。

通过配置 SAI_BxCFG0 寄存器中 OPTMOD[1]位为 0，强制选择为主模式，同时将忽略SAI_BxCFG0 寄存器中 DATAWD[2:0]数据位宽设置，强制设置为 24 位，通过时钟发生器配置符号率，并通过曼彻斯特协议进行编码。

SAI 首先在块中发送每个子帧的适当报头。随后在 SD 线上发送 SAI_BxDATA（以曼彻斯特协议进行编码）。SAI 通过传输按表26-6. 校验位奇数奇偶校验位来结束子帧。


表 26-6. 校验位奇数


<table><tr><td>SAI_BxDATA [26:0]</td><td>传输校验位 P 的值</td></tr><tr><td>奇数个 0</td><td>0</td></tr><tr><td>奇数个 1</td><td>1</td></tr></table>

对于 SPDIF 发生器，SAI 应提供一个符号率两倍的位时钟。通常情况下，音频采样率（F ）和比特时钟率 $( \mathsf { F s c k \_ x } )$ 之间的关系由以下公式给出：

$$
F _ {s} = \frac {F _ {S C K \_ x}}{1 2 8}\tag{34-6}
$$

比特时钟率由以下公式给出:

$$
F _ {S C K \_ x} = \frac {F _ {S A I \_ C K \_ x}}{M D I V}\tag{34-7}
$$

注意：仅当 SAI_BxCFG0 寄存器中 BYPASS 设置为 1 时，上述公式才有效。

## 26.3.11. 立体声/单声道

SAI音频子模块通过设置SAI_BxCFG0寄存器的MONO位进行立体声和单声道模式的转换。注意，如果选择单声道，则slot的个数必须配置为2，否则音频子模块的行为将不能保证。

当音频子模块配置为发送器时，在第一个slot（slot0）期间发送的数据将会复制到第二个slot（slot1），在这种情况下，FIFO的访问次数是立体声模式的一半。

当音频子模块配置成接收器时，在第一个slot期间接收到的数据被放入 $. F 1 \mathsf { F O }$ ，第二个slot期间接

收的数据将会被丢弃。

## 26.3.12. 静音

用户可以在一个帧传输期间的任何时候设置静音属性，这通过SAI_BxCFG1寄存器的MT位来配置，但是静音只会到下一个帧才生效。

如果SAI音频子模块作为发送器且已配置静音，当静音在下一个帧生效时，数据照常会从FIFO中取出，然后送入移位寄存器。唯一不同的是，SD输出是否强制为一个特定值，这个值由SAI_BxCFG1寄存器的MTVAL位决定。当MTVAL位为0时，在静音帧期间SD强制输出0，相反，当MTVAL置1时，SD输出行为得进一步根据slot总个数的配置。当slot总数小于或等于2时，静音有效的前一个帧内容会被赋值到当前静音帧。当slot总数大于2时，SD强制输出0。

配置成接收器的SAI音频子模块能够检测静音帧和产生相应的中断。一个静音帧计数器被应用到每个音频子模块上，如果接收到每个有效slot都为0的帧，那么这个帧就会被视为一个静音帧，内部的静音帧计数器增1。当SAI音频子模块使能或接收到一个非静音帧时，这个静音计数器就会复位。如果连续接收到的静音帧的个数达到SAI_BxCFG1寄存器MTFCNT位定义的值，则SAI_BxSTAT寄存器中的MTDET静音检测标志位就会置1，同时，如果使能了SAI_BxINTEN寄存器的MTDETIE位，则产生一个中断。

静音帧有效如图26-16. 静音帧有效所示。


图 26-16. 静音帧有效


![image](images/ebd954bc1daa.jpg)



不同配置下SD输出行为概括在表26-7. 静音帧输出值中。



表 26-7. 静音帧输出值


<table><tr><td>Slot个数</td><td>MTVAL=1</td><td>MTVAL=0</td></tr><tr><td>≤2</td><td>静音有效前的一个帧内容被赋值到SD线上输出</td><td>强制为0</td></tr><tr><td>&gt;2</td><td>强制为0</td><td>强制为0</td></tr></table>

## 26.3.13. 压缩扩展器

压缩扩展器仅仅是一个系统，里面的信息首先经过压缩，然后在一个有限带宽的通道上传输，最后在接收端进行扩展。它常被用于减小传输电话优质语音所需的带宽，它能将 位数据压缩成8位密语，该密语由1位符号位，3位量化级以及4位分量组成。有两个支持将信号数据编码成8位编码的国际标准：A-law和Mu-law。A-law是欧洲所公认的标准，Mu-law是美国和日本所公

认的标准。

A-law和Mu-law都可以应用在SAI上，这需要通过对SAI_BxCFG1寄存器进行配置来选择。音频子模块根据操作模式（OPTMOD）来选择压缩还是扩展。当音频子模块配置为发送器时，即选择压缩，相反，如果配成接收器，则选择扩展。用户可以通过设置SAI_BxCFG1寄存器的补码模式（CPLMOD）来选择1或者2的补码作为默认的数据表示。在发送模式时，无论选择哪种压缩模式，硬件首先将补码表示转换成符号量值表示，然后再送入压缩扩展器。在接收模式时，线性输出的数据从符号量值表示转换成补码表示，然后存储到FIFO中。


图 26-17. 压缩扩展数据通路


![image](images/985c63b6b86d.jpg)


## A-law 压缩扩展

A-law是CCITT推荐的压缩扩展标准，在欧洲被广泛地使用，它将线性样本值限制在12位量级。26-8. A-law 阐述了A-law编码算法，线性输入数据用符号量表示，用S代指这个符号，之后的12位表示量级。编码后输出8位宽，且按MSB表示这个符号，下表中两端的符号位S不是同一个值。A、B、C、D取0或1，x代表不关心。


表 26-8. A-law 编码


<table><tr><td colspan="13">线性输入数据</td><td colspan="8">A-law编码输出</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>S</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>S</td><td>0</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>S</td><td>0</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>S</td><td>1</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>S</td><td>1</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>S</td><td>1</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>S</td><td>1</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr></table>

输入的数据在经过表中定义的逻辑编码后，一个反向模式应用到这个8位编码上来增加传输线上的转变密度，这对硬件性能有益。8位编码与0x55异或后再应用这个反向模式。

对A-law编码的数据进行解码从本质上来说是编码步骤的颠倒问题。表26-9. A-law解码说明了A-law解码算法，它在反向模式颠倒之后应用。在编码过程中丢弃的最低有效位近似的取间隔的中间值。这在线性输出数据中体现为D后紧接着的1…0。


表 26-9. A-law 解码


<table><tr><td colspan="8">A-law编码输入</td><td colspan="13">线性输出数据</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td></tr><tr><td>S</td><td>0</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td></tr><tr><td>S</td><td>0</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>S</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## Mu-Law 压缩扩压

美国和日本使用Mu-law压缩扩压标准，将线性样本值限制在13位量级。Mu-law的编码和解码过程和A-law类似，不过还是有一些值得注意的差异：

1. Mu-law编码器一般操作在13位量级数据，而A-law为12位量级数据；

2. 在量化级计算之前，一个值为33的偏差被加到线性输入数据的绝对值上，用来简化量化值和分量的计算；

3. 符号位的定义是相反的，也就说，输入符号位和输出符号位相反；

4. 反向模式应用在8位编码的所有比特位上。

26-10. Mu-law 阐述了Mu-law编码算法，线性输入数据的符号位S取编码数据符号位的相反值。


表 26-10. Mu-law 编码


<table><tr><td colspan="14">线性输入数据</td><td colspan="8">Mu-law编码输出</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>~S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>0</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>0</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>1</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>1</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>1</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>S</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>~S</td><td>1</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td></tr></table>

输入数据通过上表定义的算法编码之后，一个反向模式应用到这个8位编码上来增加传输线上的密度，这对硬件性能有益。8位编码与0xFF异或后再应用这个反向模式。

的解码本质上是编码步骤的颠倒问题。表 解码说明了 解码过程，它应用在反向模式颠倒之后。在编码处理中丢弃的最低有效位近似等于这个间隔的中间值。这在线性输出数据中体现为D后紧接着的1…0。


表 26-11. Mu-law 解码


<table><tr><td colspan="8">Mu-law 编码输入</td><td colspan="13">线性输出数据</td><td></td></tr><tr><td>S</td><td>0</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td></tr><tr><td>S</td><td>0</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td></tr><tr><td>S</td><td>0</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>0</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>1</td><td>0</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>0</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>1</td><td>1</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>~S</td><td>1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## 26.3.14. 输出驱动

SAI可以根据SAI使能状态独立驱动每个音频子模块的帧同步（FS）、串行时钟（SCK）和串行数据（SD），这通过配置SAI_BxCFG0寄存器的输出驱动（ODRIV）来实现。

输出驱动的设定必须在SAI寄存器配置之后、SAI使能之前进行配置。

## 26.3.15. IO 管理

管理模块连接 的两个音频子模块，它也是两者进行连接的唯一中介。当通过设置SAI_BxCFG0寄存器的同步模式位（SYNCMOD）将音频子模块配置成与另一个子模块同步时，它们的FS、SCK和MCLK引脚会共用，同步子模块的这些引脚会释放，并可用作通用IO。当一个音频模块配置为与另一个音频模块同步时，那么它必须配成从设备。

当一个音频子模块作为发送器，且与另一个作为接收器的音频子模块同步的时候，如果它被配置为主设备，那么同步子模块会通过 管理模块接收来自异步模块的 和 信号，如果它被配置为从设备，那么会接收来自外部IO的FS和SCK信号。这个功能在双工模式中是非常有用的。

## 26.3.16. DMA 接口

每一个音频子模块都拥有自己的 接口。 访问的使能通过 寄存器的使能位（DMAEN）进行配置。DMA请求和FIFO请求（FFREQ）一起产生，而FIFO请求产生状态取决于FIFO阈值（FFTH）和FIFO状态（FFSTAT），这在使用DMA突发传输时是非常重要的。当音频子模块配成发送模式时，FIFO阈值必须设成一个特定的值，以保证在最坏的情况下也有足够的剩余空间来实现一个完整的DMA突发写操作，否则有可能出现FIFO上溢错误。当音频子模块配成接收模式时，FIFO阈值必须设成一个特定的值，以保证FIFO中有足够的数据来实现一个完整的DMA突发读操作，从而避免出现FIFO下溢错误。

的方向和音频子模块的操作配置相关。当配置为发送器时， 请求将数据从数据寄存器SAI_BxDATA中加载到内部FIFO中。当配置为接收器时，DMA请求将数据从内部FIFO读到数据寄存器 中。

注意：DMA SAI通道必须在SAI寄存器配置之后使能。

## 26.3.17. 使能/失能

SAI音频子模块通过设置SI_BxCFG0寄存器的SAIEN位来使能，用户必须确保这个操作在音频子模块配置之后进行， 不支持在已经使能后再进行配置，否则将不能保证硬件行为的正确。

从音频子模块必须在主音频模块使能前使能。

用户可以在有效帧传输期间的任何时候失能音频子模块，只是必须等到当前帧结束后才完全失能。

## 26.3.18. 错误标志位

## 时钟错误配置检查

时钟错误配置检测机制只有在音频子模块配置为主设备，并且时钟分频旁路（BYPASS）为0时才会使能。在这个操作模式下，用户必须保证帧宽（FWD+1）等于8到256之间且等于2的几次幂的一个值，否则状态寄存器SAI_BxSTAT中的时钟错误标志位（ERRCK）将会被置位。帧宽必须设置为2的几次幂，这是为确保在每个位时钟周期（SCK）中包含整数个主时钟（MCLK），以使得声音质量更好。

如果将中断使能寄存器SAI_BxINTEN中的时钟错误配置检测中断使能位（ERRCKIE）置1，则在出现时钟错误配置时会产生中断。

当检测到时钟错误时，SAI音频子模块将自动失能，即SAI_BxCFG0寄存器的SAIEN位被硬件清零。

## 音频编解码器未就绪检测

音频子模块只有在使用AC’97协议，并选择为接收器时才会检测音频编解码器未就绪状态。音频子模块从 G（ ）中读取音频编解码器就绪状态标志，当接收到的 G的位 为 时，状态寄存器SAI_BxSTAT寄存器的ACNRDY会被置1，如果设置了SAI_BxINTEN中断使能寄存器中的ACNRDYIE音频编解码未就绪中断位，则产生一个中断。当检测到音频编解码器未就绪时，当前帧的后续slot的内容将不会被送入FIFO中。

音频编解码器未就绪检测标志位通过设置SAI_BxINTC寄存器的ACNRDYC位来清除。

## 帧同步提前检测

音频子模块只有在配置为从设备时，才会使能帧同步提前检测机制，由于从设备才接收FS信号，FS信号到达时间对当前数据的解析至关重要。帧同步提前检测是可能的，因为帧宽、帧有效极性和帧偏移在音频子模块使能前已经确定。

帧同步提前对当前帧是没有影响的，因为FS有效边沿只有在帧结束时才能预料到。

当状态寄存器SAI_BxSTAT中的帧同步提前检测标志位（FSDET）和中断使能寄存器SAI_bxINTEN中的帧同步提前检测中断使能位都置1时，产生中断。

在出现帧同步提前后，需要按照下面的步骤来进行重新同步：

1. 失能音频子模块，用户必须等到相应的音频子模块的SAIEN控制字段完全失能；

2. 设置FLUSH控制字段刷新内部FIFO；

3. 设置SAIEN再一次使能音频子模块；

4. 等待FS重新同步。

注意： 在AC’97配置模式中，这个标志位不会产生，因为SAI仅作为一个链路控制器，即使音

频子模块配置为从设备，也会生成FS信号。


图26-18. 帧同步提前检测示意图


![image](images/48f95e93fed0.jpg)


## 帧同步滞后检测

音频子模块只有在配置为从设备时，才会使能帧同步滞后检测机制，由于从设备才接收FS信号，FS信号到达时间对当前数据的解析至关重要。帧同步滞后检测是可能的，因为帧宽、帧有效极性和帧偏移在音频子模块使能前已经确定。

帧同步滞后可能的原因有主设备的延迟产生、外因延迟、噪音感应故障。错误的FS时序将会破坏音频子模块内部有限状态机，从而影响数据的正确传输。

当状态寄存器SAI_BxSTAT中的帧滞后提前检测标志位（FSPDET）和中断使能寄存器SAI_bxINTEN中的帧同步滞后检测中断使能位都置1时，产生中断。

为了和主设备重新同步，需要应用重新同步的步骤。

注意： 在AC’97配置模式中，这个标志位不会产生，因为SAI仅作为一个链路控制器，即使音频子模块配置为从设备，也会生成FS信号。


图26-19. 帧同步滞后检测示意图


![image](images/ab776ff6f887.jpg)


## FIFO上溢或下溢检测

FIFO上溢和下溢标志位（OUERR）在SAI_BxSTAT状态寄存器中占同一个位，因为每个音频子模块只能配置成发送或接收。

当音频子模块配置成发送器时，在有效帧传输过程中如果FIFO为空，并且发送一个空的数据的slot，则产生下溢。如果中断使能寄存器SAI_BxINTEN的上溢或下溢中断使能位（OUERRIE）置位，则产生中断。如果发生下溢，一个重新同步过程需要按如下所示步骤进行：

失能音频子模块，用户必须等到相应的音频子模块的 控制字段完全失能；

2. 设置FLUSH控制字段刷新内部FIFO；

3. 将要发送的数据填充到FIFO中；

4. 设置SAIEN再一次使能音频子模块。

通过设置SAI_BxINTC寄存器的OUERRC位来清除下溢标志位。

当音频子模块配置为接收器时，在帧传输过程中如果FIFO已满，并有一个新的slot数据接收时，发生上溢。当上溢发生时，最新接收的数据将被丢弃，也不会写值到FIFO。如果中断使能寄存器SAI_BxINTEN的上溢或下溢中断使能位（OUERRIE）置位，则产生中断。

通过设置SAI_BxINTC寄存器的OUERRC位来清除上溢标志位

注意：当DMA使能时，用户必须保证正确的DMA配置，尤其是使用DMA突发操作的时候，否则上溢和下溢都可能发生在发送或接收操作模式中。

## 26.3.19. 中断

26-12. 概括了每个音频子模块出现的所有中断源


表 26-12. 中断控制


<table><tr><td>中断源</td><td>中断划分</td><td>中断出现条件</td><td>中断使能控制</td><td>中断清除控制</td></tr><tr><td>FFREQ</td><td>请求</td><td>OPTMOD为任意值</td><td>FFREQIE</td><td>读或写SAI_BxDATA</td></tr><tr><td>MTDET</td><td>静音</td><td>OPTMOD为接收方</td><td>MTDETIE</td><td>MTDETC</td></tr><tr><td>ERRCK</td><td>错误</td><td>OPTMOD为主模式; BYPASS = 0</td><td>ERRCKIE</td><td>ERRCKC</td></tr><tr><td>ACNRDY</td><td>错误</td><td>OPTMOD为从模式; PROT = AC&#x27;97</td><td>ACNRDYIE</td><td>ACNRDYC</td></tr><tr><td>FSADET</td><td>错误</td><td>OPTMOD为从模式; PROT ≠AC&#x27;97</td><td>FSADETIE</td><td>FSADETC</td></tr><tr><td>FSPDET</td><td>错误</td><td>OPTMOD为从模式; PROT ≠AC&#x27;97</td><td>FSPDETIE</td><td>FSPDETC</td></tr><tr><td>OUERR</td><td>错误</td><td>OPTMOD为任意值</td><td>OUERRIE</td><td>OUERRC</td></tr></table>

使用下面所列的过程可以使得音频子模块从错误中断中恢复：

1. 使能相应的中断；

2. 配置SAI功能寄存器；

3. 使能中断；

4. 使能SAI音频子模块。
