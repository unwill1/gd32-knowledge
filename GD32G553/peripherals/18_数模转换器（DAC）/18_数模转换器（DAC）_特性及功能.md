## 18. 数模转换器（DAC）

## 18.1. 简介

数字/模拟转换器可以将 12 位的数字数据转换为外部引脚上的电压输出。数据可以采用 8 位或 12位模式，左对齐或右对齐模式。当使能了外部触发，DMA可被用于更新输入端数字数据。

在输出电压时，可以利用 DAC 输出缓冲区来获得更高的驱动能力。通过校准可提高输出缓冲区的输出精度，采样保持模式可降低 DAC 的功耗。

采样保持模式可以降低 DAC 的功耗。

每个 DAC 的两个单元可以独立或并发工作。

## 18.2. 主要特性

DAC 的主要特征如下：

 8 位或 12 位分辨率；

 数据左对齐或右对齐；

 DMA功能与欠载检测；

 同步更新转换；

 外部事件触发转换；

 可配置的内部缓冲区；

 输入参考电压 V<sub>REFP</sub>；

 输出缓冲区校准；

 低功耗的采样保持功能；

 噪声波生成（LSFR 噪声模式和三角噪声模式）；

 锯齿波生成；

 DACx 双单元并发模式；

 复位保持功能。

18-1. DAC 为 DAC 的结构框图， 18-1. DAC 给出了引脚描述。


图 18-1. DAC 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/79394b9da1a3cb2a3f93e2295f7034033779b2dd64ec41112e77019d890c5b0c.jpg)



表 18-1. DAC 引脚


<table><tr><td>名称</td><td>描述</td><td>信号类型</td></tr><tr><td><eq>V_{DDA}</eq></td><td>模拟电源</td><td>输入,模拟电源</td></tr><tr><td><eq>V_{SSA}</eq></td><td>模拟电源地</td><td>输入,模拟电源地</td></tr><tr><td><eq>V_{REFP}</eq></td><td>DAC 正参考电压</td><td>输入,模拟正参考电压</td></tr><tr><td>DACy_OUTx</td><td>DAC 模拟输出</td><td>模拟输出信号</td></tr></table>


下表详细列出了 DAC 的触发与输出信号。



表 18-2. DAC 触发与输出


<table><tr><td></td><td colspan="2">DAC0</td><td colspan="2">DAC1</td><td colspan="2">DAC2</td><td colspan="2">DAC3</td></tr><tr><td>单元</td><td>单元0</td><td>单元1</td><td>单元0</td><td>单元1</td><td>单元0</td><td>单元1</td><td>单元0</td><td>单元1</td></tr><tr><td>DAC输出I/O</td><td>PA4</td><td>PA5</td><td>PA6</td><td>PA7</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>DAC输出BUFFER功能</td><td>●</td><td>●</td><td>●</td><td>●</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>TRIGSEL触发功能</td><td colspan="2">●</td><td colspan="2">●</td><td colspan="2">●</td><td colspan="2">●</td></tr><tr><td>软件触发功能</td><td colspan="2">●</td><td colspan="2">●</td><td colspan="2">●</td><td colspan="2">●</td></tr><tr><td>最大采样率</td><td colspan="4">1MSPS</td><td colspan="4">15MSPS</td></tr></table>


注意：在使能 DAC 模块前，GPIO 口（DAC 输出 I/O）应配置为模拟模式。


## 18.3. 功能描述

## 18.3.1. DAC 使能

将 DAC_CTL0 寄存器中的 DENx 位置 1，可以给 DAC 模块上电，DAC 子模块完全启动需要等待t<sub>WAKEUP</sub> 时间。

## 18.3.2. DAC 输出缓冲

为了降低输出阻抗，并在没有外部运算放大器的情况下驱动外部负载，每个 DAC 模块内部各集成了一个输出缓冲区。

缺省情况下，输出缓冲区是开启的，可以通过设置 DAC_MDCR 寄存器的 MODEx 位来开启或关闭缓冲区。

注意：DAC2 与 DAC3 无输出缓冲功能。

## 18.3.3. DAC 数据配置

对于 12 位的 DAC 保持数据（OUTx_DH），可以通过对 DAC_OUTx_R12DH、DAC_OUTx_L12DH和 DAC_OUTx_R8DH 中的任意一个寄存器写入数据来配置。当数据被加载到 DAC_OUTx_R8DH寄存器时，只有 8 位最高有效位是可配置，4 位最低有效位被强制置为 4’b0000。

写入 DAC_OUTx_R12DH, DAC_OUTx_L12DH or DAC_OUTx_R8DH 寄存器的数据默认以无符号格式处理，也可以通过设置 DAC_MDCR 寄存器的 DHFMTx 位为 1，配置成有符号格式（二进制补码，如 Q1.15, Q1.11 or Q1.7 格式）。

无论有符号或者无符号数据格式，DAC 输出电压范围都是 0 到 V<sub>REFP</sub>。并且传输到 DAC_OUTx_DO寄存器的数据将被转换成无符号格式，如下表所示。


表 18-3. DAC 数据格式（12-bit 数据）


<table><tr><td>DHFMTx位</td><td>写入 DAC_OUTx_DH寄存器的数据</td><td>十进制值</td><td>传输到DAC_OUTx_DO 寄存器的数据</td><td>输出电压</td></tr><tr><td>0</td><td>0x000</td><td>0</td><td>0x000</td><td>0</td></tr><tr><td>0</td><td>0xFFFF</td><td>4095</td><td>0xFFFF</td><td><eq>V_{REFP}</eq></td></tr><tr><td>1</td><td>0x7FF</td><td>2047</td><td>0xFFFF</td><td><eq>V_{REFP}</eq></td></tr><tr><td>1</td><td>0x000</td><td>0</td><td>0x800</td><td><eq>\frac{V_{REFP}}{2}</eq></td></tr><tr><td>1</td><td>0xFFFF</td><td>-1</td><td>0x7FF</td><td><eq>\frac{V_{REFP}}{2}-\frac{V_{REFP}}{4096}</eq></td></tr><tr><td>1</td><td>0x800</td><td>-2048</td><td>0x000</td><td>0</td></tr></table>

## 18.3.4. DAC 触发

DAC 可以通过软件或者外部信号的上升沿触发。外部触发可以通过设置 DAC_CTL0 寄存器中DTENx 位来使能。触发源可以通过 DAC_CTL0 寄存器中 DTSELx 位来进行选择，如 18-4. DAC外部触发所示。


表 18-4. DAC 外部触发


<table><tr><td>DTSELx[1:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>2b&#x27;00</td><td>来自 TRIGSEL 的外部触发DAC_OUTx_EXTRIG</td><td>硬件触发</td></tr><tr><td>2b&#x27;01</td><td>DAC_SWT 寄存器的 SWTRx</td><td>软件触发</td></tr><tr><td>2b&#x27;10</td><td rowspan="2">保留</td><td rowspan="2">保留</td></tr><tr><td>2b&#x27;11</td></tr></table>


外部触发信号由触发选择控制器(TRIGSEL)产生, 而软件触发是通过设置 DAC_SWT 寄存器的SWTRx 位生成的。


## 18.3.5. DAC 转换

如果使能了外部触发（通过设置 DAC_CTL0 寄存器的 DTENx 位），当已经选择的触发事件发生，DAC 保持数据（OUTx_DH）会被转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。而在外部触发未使能的情况下，DAC 保持数据（OUTx_DH）会被自动转移到 DAC 数据输出寄存器（DAC_OUTx_DO）。

当 DAC 保持数据（OUTx_DH）加载到 DAC_OUTx_DO 寄存器时，经过 t<sub>SETTLING</sub> 时间之后，模拟输出变得有效，t<sub>SETTLING</sub>的值与电源电压和模拟输出负载有关。

## 18.3.6. DAC 噪声波

有两种方式可以将噪声波加载到 DAC 输出数据：LFSR 噪声波和三角波。噪声波模式可以通过DAC_CTL0寄存器的 DWMx 位来进行选择。噪声的幅值可以通过配置 DAC_CTL0 寄存器的 DAC噪声波位宽（DWBWx）位来进行设置。

LFSR 噪声模式：在 DAC 控制逻辑中有一个线性反馈移位寄存器（LFSR）。在此模式下，LFSR的值与 OUTx_DH 值相加后，被写入到 DAC 数据输出寄存器（DAC_OUTx_DO）。当配置的 DAC噪声波位宽小于 12 时，LFSR 的值等于 LFSR 寄存器最低的 DWBWx 位，高位被屏蔽。


图 18-2. DAC LFSR 算法


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/7837ee7ebc077430eb248d8738a53a43546cf67d248870bd5993bbe51b593ba6.jpg)



三角 噪声 模 式：三角 波 幅值与 OUTx_DH 值相 加后 ，被 写 入到 DAC 数据 输出 寄 存器（DAC_OUTx_DO）。三角波幅值的最小值为 0，最大值为(2 << DWBWx) - 1。



图 18-3. DAC 三角噪声模式生成的波形


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/9896856cf7ce1ca223cb8c6960132cdff654ed8be8666d9ec4dc008e5f063118.jpg)


## 18.3.7. DAC 锯齿波

为了产生锯齿波，模块实现了一个带复位触发和递增/递减触发的 16 位锯齿波计数器。

计数器初始值由 DAC_OUTx_SAW 寄存器的 SAWINITx[11:0]位指定，寄存器的高 12 到 15 位被设为 4b’0000。

计数器的步进方向由 DAC_OUTx_SAW 寄存器的 SAWDIRx 位定义，此位决定计数器向上或者向下计数。

计数器的步进值由 DAC_OUTx_SAW 寄存器的 SAWSTEPx[15:0]位定义。锯齿波计数器的高 12位将被传输到 DAC_OUTx_DO 寄存器用以转换输出电压。

锯齿波计数器在每个步进（复位）触发信号上升沿递增/递减（复位）。递增/递减（复位）触发信号分别由 DAC_SAWMDR 寄存器的 SAWRSTTSELx 位和 SAWSTEPTSELx 位选择。


表 18-5. DAC 锯齿波复位触发信号


<table><tr><td>SAWRSTTSELx[1:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>2b&#x27;00</td><td>来自 TRIGSEL 的外部触发DAC_OUTx_EXTRIG</td><td>硬件触发</td></tr><tr><td>2b&#x27;01</td><td>DAC_SWT 寄存器的 SWTRx</td><td>软件触发</td></tr><tr><td>2b&#x27;10</td><td rowspan="2">保留</td><td rowspan="2">保留</td></tr><tr><td>2b&#x27;11</td></tr></table>


表 18-6. DAC 锯齿波步进触发信号


<table><tr><td>SAWSTEPTSELx[1:0]</td><td>触发源</td><td>触发类型</td></tr><tr><td>2b&#x27;00</td><td>来自 TRIGSEL 的外部触发DAC_OUTx_ST_EXTRIG</td><td>硬件触发</td></tr><tr><td>2b&#x27;01</td><td>DAC_SWT 寄存器的 SWSTTRx</td><td>软件触发</td></tr><tr><td>2b&#x27;10</td><td rowspan="2">保留</td><td rowspan="2">保留</td></tr><tr><td>2b&#x27;11</td></tr></table>


图 18-4. DAC 锯齿波（SAWDIRx = 1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/3b4480171319e1b35802bd50c90067fba45896182e23a273bf0f3a1b4b46cd31.jpg)



图 18-5. DAC 锯齿波（SAWDIRx = 0）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/46a0fc5293c55b42c44eb5c5b4f2d18a3681b0f86c7c5e79f3276e12a6b1d34d.jpg)


## 18.3.8. DAC输出电压

DAC 引脚上的模拟输出电压取决于下面的等式：

$$
V _ {D A C \_ O U T} = V _ {R E F P} * O U T x \_ D O / 4 0 9 6\tag{18-1}
$$

数字输入被线性地转换成模拟输出电压，输出范围为 0 到 $V _ { R E F P }$ 

## 18.3.9. DMA 请求

在外部触发使能的情况下，通过设置 DAC_CTL0 寄存器的 DDMAENx 位来使能 DMA请求。当有外部硬件触发的时候（不是软件触发），则产生一个 DMA请求。

如果在前一个请求响应之前第二个外部触发到达，则不响应新到的触发请求，并且发生欠载错误事件。DAC_STAT0 寄存器中的 DDUDRx 位置 1，如果 DAC_CTL0 寄存器中的 DDUDRIEx 位置 1，则会产生中断。

## 18.3.10. DAC 并发转换

当 DAC 的两个单元同时工作时，为了在特定应用中最大限度利用总线带宽，DAC 的两个单元可以被配置为并发模式。在并发模式中，DAC 的 OUTx_DH 和 DAC_OUTx_DO 寄存器值将同时被更新。

有 3 个并发寄存器可用于加载 OUTx_DH 的值，分别是：DACC_R8DH、DACC_R12DH 和DACC_L12DH 寄存器，配置其中的任意一个寄存器都可实现同时驱动 DAC 的两个单元。

当使能了外部触发时，DAC 两个单元的 DTENx 位都需要置 1，需要配置 DTSEL0/1 相同来保证同时触发。

当使能了 DMA 功能时，DAC 任一单元的 DDMAENx 位置 1 即可。

噪声模式和噪声位宽可以根据使用情况配置为相同或不同。

## 18.3.11. DAC 复位保持模式

通过设置 DAC_CTL0 寄存器的 DRSTMDx 位使能 DAC 的复位保持模式，在除了上电复位之外的其他复位信号到来时，DAC 单元的输出将会保持。

当 DRSTMDx 位置 1 时，寄存器 DAC_CTL0(DRSTMDx, DTENx, DBOFFx and DENx), OUTx_DH,DAC_OUTx_DO 只能被上电复位清零。

注意：当 DAC 使用内部参考电压（VREF_EN = 1）时，需要使能 VREF 的复位保持功能来实现此模式。

## 18.3.12. DAC 输出缓冲区校准

当 DAC 使用缓冲区时，输出电压可能会发生偏移，因此需要对输出电压进行补偿。

DAC 校准函数为：

$$
V _ {\text { out }} = (D / 2 ^ {N - 1}) ^ {*} G ^ {*} V _ {\text { REFP }} + V _ {\text { of }}\tag{18-2}
$$

式中，N 是 DAC 的有效位数，D 是 DAC 的数字输入，G 是增益， $V _ { R E F P }$ 是 DAC 的参考电压， $\mathsf { V } _ { \mathsf { o f } }$ 是偏移电压，对于理想 DAC，G是 1， $\mathsf { V } _ { \mathsf { o f } } .$ 是 0。

当缓冲区启用时，校准将生效，在校准过程中：

 缓冲区与外部引脚和片上外设断开连接并进入三态。

 缓冲区将用作比较器来检测中间码值 0x800，并通过内部电桥与 $\mathsf { V } _ { \mathsf { R E F P } } / 2$ 进行对比，DAC_STAT0 寄存器的 CALFx 位会根据比较结果置 1 或清零。

有两种校准方法可用：

 出厂校准(始终使能)

DAC 缓冲区偏移在工厂进行校准，当 DAC 复位时，自动加载 DAC_CALR 寄存器OTV0[4:0]的默认值。

 用户校准

如果用户工作条件与工厂校准条件不同，特别是 VDDA, $V _ { R E F P }$ 和温度发生改变时，用户可在应用过程中通过软件进行校准。

用户校准过程为：

 DAC_CTL0 寄存器中 DENx 位写 0 以禁能 DAC 输出。

 DAC_CTL0 寄存器中 CALENx 位置 1 使能 DAC 校准。

 执行校准算法

– 从 0x00000b 开始写入 OTVx[4:0]。

– 等待 $\mathsf { T } _ { \mathsf { c a l } }$ 时间。

– 检查 DAC_STAT0 寄存器中的 CALFx 位。

– 当 CALFx 位置 1，证明正确的校准值已找到，否则码值加 1 直至找到正确的校准值。通过使用逐次逼近或二分法技术，可以更快地计算 OTVx[4:0]的值。

注意：校准过程后，CALENx 应写入 0，然后将 DENx 写入 1，从而在正常模式下使用 DAC。禁止同时将 DENx 和 CALENx 设置为 1。

## 18.3.13. DAC 模式

DAC两个单元可以配置为普通模式和采样保持模式。DAC 输出可连接到外部引脚或片上外设。

## 普通模式

通过设置 DAC_MDCR 寄存器的 MODEx[2]位为 0，DAC 工作在普通模式。

## 采样保持模式

通过设置 DAC_MDCR 寄存器的 MODEx[2]位为 1，DAC 工作在采样保持模式。DAC 内核在触发转换后对数据进行转换，并将转换后的电压在电容上保持。当不转换时，DAC 内核在两次采样之间保持关闭状态。并且 DAC 输出为三态，因此可以降低整体功耗。在此模式下，DAC 内核和所有相应的逻辑以及寄存器均由 IRC32K驱动。因此，DAC 可在深度睡眠模式下使用。

采样保持模式可分为三个阶段：

## 采样阶段

采样保持原件被充电到所需电压，充电时间取决于电容值，采样时间由 DAC_SKSTRx 寄存器中的 TSAMPx[9:0]位配置。当对 TSAMPx[9:0]位进行写操作时，DAC_SATA0 寄存器中的 BWTx 位会自动置 1，用以指示 AHB 时钟和 IRC32K 时钟正在同步。当写操作完成时，BWTx 位由硬件自动清零，用户可以再次对 TSAMPx[9:0]位执行写操作。在 DAC 正常输出过程中，可通过软件更改TSAMPx[9:0]。

## 保持阶段：

在保持阶段，DAC 内核在保持阶段处于关闭状态，从而降低系统功耗，保持时间由 DAC_SKKTR寄存器中的 TKEEPx[9:0]位配置，该模式下 DAC 输出为三态。

## 刷新阶段：

在刷新阶段，DAC 内核再次打开，将下降的电压充电至目标值。刷新时间由 DAC_SKRTR 寄存器中的 TREFx[7:0]位配置。

当新的 OUTx_DH 更新时（DTENx=1 时触发或 DTENx=0 时更新），操作阶段将进入采样阶段，同时 DAC 内核将新数据转换为所需电压，在采样保持模式下，两个连续的数据更新操作之间需要3 个以上的 IRC32K 时钟周期才能同步。

## 注意:

如果在采样保持模式下选择锯齿波生成（ $\mathsf { P W M X = } 2 ^ { \prime } \mathsf { b } 1 1 $ ），SAWRSTTSELx and DTSELx $( \mathsf { x } \mathsf { = } 0 , 1 )$ 配置需要保持一致。

## 时间计算

上述三个阶段的时间计算均基于IRC32K时钟周期。为了配置足够的采样和刷新时间，参考下面的公式：


表 18-7. 采样和刷新时间计算公式


<table><tr><td>缓冲状态</td><td><eq>t_{sample}^{(1)}</eq> (2)</td><td><eq>t_{refresh}^{(1)}</eq> (2) (3)</td><td><eq>t_{keep}^{(3)}</eq></td></tr><tr><td>开启</td><td><eq>t_{wakeup} + R_{BON}*C_{SK}*ln(2^{N+1})</eq></td><td><eq>t_{wakeup} + R_{BON}*C_{SK}*ln(2*N_{LSB})</eq></td><td><eq>(V_{REFP}/2^{N})*N_{LSB}*C_{SK}/I_{leak}</eq></td></tr><tr><td>关闭</td><td><eq>t_{wakeup} + R_{BOFF}*C_{SK}*ln(2^{N+1})</eq></td><td><eq>t_{wakeup} + R_{BOFF}*C_{SK}*ln(2*N_{LSB})</eq></td><td><eq>(V_{REFP}/2^{N})*N_{LSB}*C_{SK}/I_{leak}</eq></td></tr></table>

## 注意:

(1) 上述公式， $\scriptstyle \mathbf { t } _ { w a k e u p }$ 是DAC从关闭状态唤醒到输出达到最终设置值的时间，充电时间计算于电容电压重新充电到设定输出1/2 LSB误差以内的时间。N是DAC分辨率，12位或8位。

(2) R<sub>BON</sub>/R<sub>BOFF</sub>是输出缓冲打开或者关闭的输出阻抗，C<sub>SK</sub>是采样保持电容(内部或外部)。当DAC_MDCR寄存器的MODEx[2:0]位是3’b111时，内部电容用于保持DAC输出到片上外设的电压。

(3) 保持时间取决于容许的电压下降值，保持阶段采样保持电容会因输出漏电流放电导致电压下降。N<sub>LSB</sub>代表电压下降的位数，I<sub>leak</sub>是输出漏电流。

(4) R<sub>BON</sub>，R<sub>BOFF</sub>，C<sub>SK</sub>以及t<sub>wakeup</sub>的值请参考器件数据手册。

采样保持阶段框图如下所示。


图 18-6. DAC 采样保持


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/6e5fff67d8dcc42dae40d1a61ffd3d83a30748989a72a9a011e759988fad5374.jpg)


## 18.3.14. DAC 低功耗模式

## 睡眠模式

在睡眠模式中，DAC 可正常工作，并且可以与 DMA 一起使用。

## 深度睡眠模式

在深度睡眠模式中，若在进入深度睡眠模式前，采样保持功能使能，DAC 可保持静态输出，否则DAC 停止工作。

## 待机模式

在待机模式中，DAC 停止工作，退出待机模式并重新初始化 DAC，DAC 可再次工作。
