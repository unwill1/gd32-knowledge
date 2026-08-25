## 21. 模数转换器（ADC）

## 21.1. 简介

MCU 片上集成了 12 位逐次逼近式模数转换器模块（ADC），可以采样来自于外部输入通道和内部通道的模拟信号。ADC0有16个外部通道和2个内部通道（温度传感器V<sub>SENSE</sub>和参考电压V<sub>REFINT</sub>），ADC1 有 18 个外部通道，ADC2 有 17 个外部通道。

模拟看门狗允许应用程序来检测输入电压是否超出用户设定的高低阈值。

所有的 ADC 采样通道都支持多种运行模式，采样转换后，转换结果可以按照最低有效位对齐或最高有效位对齐的方式保存在相应的数据寄存器中。

片上的硬件过采样机制可以通过减少来自 MCU 的相关计算负担来提高性能。

## 21.2. 主要特征

 高性能：

ADC采样分辨率：12位、10位、8位、或者6位分辨率；

可编程采样时间；

数据存储模式：最高有效位对齐和最低有效位对齐；

常规和注入序列都支持 DMA 请求。

 模拟输入通道：

ADC0有16个外部模拟输入通道，ADC1有18个外部模拟输入通道，ADC2有17个外部模拟输入通道；

1个内部温度传感器通道（V<sub>SENSE</sub>）；

1个内部参考电压输入通道（V<sub>REFINT</sub>）；

 转换开始的发起：

- 软件；

TRIGSEL触发。

 运行模式：

转换单个通道，或者扫描一序列的通道；

- 单次运行模式，每次触发转换一次选择的输入通道；

连续运行模式，连续转换所选择的输入通道；

间断运行模式；

同步模式（适用于具有两个或多个ADC的设备）。

 转换结果阈值监测功能：模拟看门狗。

 中断产生：

- 序列转换结束；

模拟看门狗事件；

 过采样：

16位的数据寄存器；

可调整的过采样率，从2x到256x；

高达8位的可编程数据移位。

 ADC输入范围：V<sub>REFN</sub> ≤V<sub>IN</sub> ≤V<sub>REFP</sub>。

## 21.3. 引脚和内部信号

21-1. ADC 给出了 ADC 模块框图。 21-1. ADC 给出了 ADC 内部信号。21-2. ADC 给出了 ADC 引脚说明。


表 21-1. ADC 内部信号


<table><tr><td>内部信号名称</td><td>说明</td></tr><tr><td><eq>V_{SENSE}</eq></td><td>内部温度传感器输出电压</td></tr><tr><td><eq>V_{REFINT}</eq></td><td>内部参考输出电压</td></tr></table>


表 21-2. ADC 引脚定义


<table><tr><td>名称</td><td>注释</td></tr><tr><td><eq>V_{DDA}</eq></td><td>模拟电源输入,等于<eq>V_{DD}</eq></td></tr><tr><td><eq>V_{SSA}</eq></td><td>模拟地,等于<eq>V_{SS}</eq></td></tr><tr><td><eq>V_{REFP}</eq></td><td>ADC正参考电压</td></tr><tr><td><eq>V_{REFN}</eq></td><td>ADC负参考电压</td></tr><tr><td>ADCx_IN[17:0]</td><td>多达18路外部通道</td></tr></table>


注意：V<sub>DDA</sub> 和 V<sub>SSA</sub> 必须分别连接到 V<sub>DD</sub> 和 V<sub>SS</sub>。


## 21.4. 功能描述


图 21-1. ADC 模块框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/6564bf36f78053c7048e1f13e65a70de8901b528b08afb76144c2c7827d2ccea.jpg)


## 21.4.1. ADC 时钟

ADC 最大工作时钟频率为 42MHz。CK_ADC 时钟是由时钟控制器提供的，它和 AHB、APB2 时钟保持同步。ADC 时钟可以在 RCU 时钟控制器中进行分频和配置。

想要更多 ADC 时钟产生的信息，可以参考 RCU 章节内容。

## 21.4.2. ADC 使能

ADC_CTL1 寄存器中的 ADCON 位是 ADC 模块的使能开关。如果该位为 0，则 ADC 模块保持复位状态。为了省电，当 ADCON 位为 0 时，ADC 模拟子模块将会进入掉电模式。ADC 使能后需等待 t<sub>SU</sub>时间后才能采样，t<sub>SU</sub>数值详见芯片相关型号 Datasheet。

## 21.4.3. 常规序列和注入序列

通道管理电路把采样通道组织成两个序列：一个常规序列和一个注入序列。

常规序列支持高达 16 个通道，每个通道称为常规通道。ADC_RSQ0 寄存器的 RL[3:0]位规定了整

个常规序列的长度。ADC_RSQ0~ADC_RSQ2 寄存器规定了常规序列的通道选择。

注入序列支持高达 4 个通道，每个通道称为注入通道。ADC_ISQ 寄存器的 IL[1:0]位规定了整个注入序列的长度。ADC_ISQ 寄存器规定了注入序列的通道选择。

注意：尽管 ADC 支持 18 个通道，但常规序列最大长度为 16 个通道，注入序列最大长度为 4 个通道。

## 21.4.4. 运行模式

## 单次运行模式

该模式能够运行在常规序列和注入序列。单次运行模式下，ADC_RSQ2 寄存器的 RSQ0[4:0]位或者 ADC_ISQ 寄存器的 ISQ3[4:0]位规定了 ADC 的转换通道。当 ADCON 位被置 1，一旦相应软件触发或者 TRIGSEL 触发发生，ADC 就会采样和转换一个通道。


图 21-2. 单次运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/9ffced4ea2b3273f8493e13b0c80c50a40eb153697fdae8f5cbcf88700700dac.jpg)


常规序列的通道单次转换结束后，转换数据将被存放于 ADC_RDATA寄存器中，EORC 将会置 1。如果 EORCIE 位被置 1，将产生一个中断。

注入序列的通道单次转换结束后，转换数据将被存放于 ADC_IDATA寄存器中，EOIC位将会置1。如果 EOICIE 位被置 1，将产生一个中断。

常规序列单次运行模式的软件流程：

1. 确保ADC_CTL0寄存器的DISRC和SM位以及ADC_CTL1寄存器的CTN位为0；

2. 用模拟通道编号来配置RSQ0[4:0]位域；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，可以配置ADC_CTL1寄存器的ETMRC[1:0]位域；

5. 设置SWRCST位，或者为常规序列产生一个TRIGSEL触发信号；

6. 等到EORC置1；

7. 从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EORC标志位。

注入序列单次运行模式的软件流程：

1. 确保ADC_CTL0寄存器的DISIC和SM位为0；

2. 用模拟通道编号来配置ISQ3[4:0]位域；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，可以配置ADC_CTL1寄存器的ETMIC[1:0]位域；

5. 设置SWICST位，或者为注入序列产生一个TRIGSEL触发信号；

6. 等到EOIC置1；

7. 从ADC_IDATA寄存器中读ADC转换结果；

8. 写0清除EOIC标志位。

## 连续运行模式

该模式能够运行在常规序列。将 ADC_CTL1 寄存器的 CTN 位置 1 可以使能连续运行模式。在此模式下，ADC 执行由 RSQ0[4:0]规定的转换通道。当 ADCON 位被置 1，一旦相应软件触发或者TRIGSEL 触发产生，ADC 就会采样和转换规定的通道。转换数据保存在 ADC_RDATA 寄存器中。


图 21-3. 连续运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/0830daee3dd5bc5057398cace29792a877f73ef48bafff451ef3c4a5a61b4081.jpg)


常规序列连续运行模式的软件流程：

1. 设置ADC_CTL1寄存器的CTN位为1；

2. 根据模拟通道编号配置RSQ0[4:0]；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETMRC[1:0]位域；

5. 设置SWRCST位，或者给常规序列产生一个TRIGSEL触发信号；

6. 等待EORC标志位置1；

7. 从ADC_RDATA寄存器中读ADC转换结果；

8. 写0清除EORC标志位；

9. 只要还需要进行连续转换，重复步骤6~8。

可以使用 DMA 来传输转换数据，不需循环查询 EORC 标志位，软件流程如下：

1. 设置ADC_CTL1寄存器的CTN和RDMA位为1；

2. 根据模拟通道编号配置RSQ0[4:0]；

3. 配置ADC_SAMPTx寄存器；

4. 如果有需要，配置ADC_CTL1寄存器的ETMRC[1:0]位域；

5. 准备DMA模块，用于传输来自ADC_RDATA的数据；

6. 设置SWRCST位，或者给常规序列产生一个TRIGSEL触发。

## 扫描运行模式

扫描运行模式可以通过将 ADC_CTL0 寄存器的 SM 位置 1 来使能。在此模式下，ADC 扫描转换所有被 ADC_RSQ0~ADC_RSQ2 寄存器或 ADC_ISQ 寄存器选中的所有通道。一旦 ADCON 位被置 1，当相应软件触发或者 TRIGSEL 触发产生，ADC 就会一个接一个的采样和转换常规序列或注入序列通道。转换数据存储在 ADC_RDATA 或 ADC_IDATA 寄存器中。常规序列或注入序列转换结束后，EORC 或者 EOIC 位将被置 1。如果 EORCIE 或 EOICIE 位被置 1，将产生中断。当常规或者注入序列工作在扫描模式下时，可以通过 ADC_CTL1 寄存器的 RDMA 或者 IDMA 位置1 使能相应的 DMA功能。

如果 ADC_CTL1 寄存器的 CTN 位也被置 1，则在常规序列转换完之后，这个转换自动重新开始。


图 21-4. 扫描运行模式，且连续运行模式禁能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/0cba766901b7408fce7be99d07861817bb40f52bf43446f399ee62b3fb5b5a7e.jpg)


常规序列扫描运行模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 SM 位和 ADC_CTL1 寄存器的 RDMA 位为 1；

2. 配置 ADC_RSQx 和 ADC_SAMPTx 寄存器；

3. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMRC[1:0]位；

4. 准备 DMA 模块，用于传输来自 ADC_RDATA 的数据；

5. 设置 SWRCST 位，或者给常规序列产生一个 TRIGSEL 触发；

注入序列扫描运行模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 SM 位和 ADC_CTL1 寄存器的 IDMA 位为 1；

2. 配置 ADC_ISQ 和 ADC_SAMPTx 寄存器；

3. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMIC[1:0]位；

4. 设置 SWICST 位，或者给注入序列产生一个 TRIGSEL 触发；

5. 准备 DMA 模块，用于传输来自 ADC_IDATA 的数据；


图 21-5. 扫描运行模式，连续运行模式使能


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/f955a5a217ae597e4f51ce4937967600b121da90bc6f4f06f8dff08e728edc9d.jpg)


## 间断运行模式

对于常规序列，当 ADC_CTL0 寄存器的 DISRC 位置 1 时，常规序列间断运行模式使能。该模式下可以执行一次 n 个通道的短序列转换（n<=8），这个短序列是 ADC_RSQ0~RSQ2 寄存器所选择的转换序列的一部分。数值 n 由 ADC_CTL0 寄存器的 DISNUM[2:0]位给出。当相应的软件触发或 TRIGSEL 触发发生，ADC 就会采样和转换在 ADC_RSQ0~RSQ2 寄存器所选择通道中接下来的 n 个通道，直到常规序列中所有的通道转换完成。每个常规序列转换周期结束后，EORC 位将置 1。如果 EORCIE 位置 1 将产生一个中断。

对于注入序列，当 ADC_CTL0 寄存器的 DISIC 位置 1 时，注入序列间断运行模式使能。该模式下可以执行 ADC_ISQ 寄存器所选择的转换序列的一个通道进行转换。当相应的软件触发或TRIGSEL 触发发生，ADC 就会采样和转换 ADC_ISQ 寄存器中所选择通道的下一个通道，直到注入序列中所有通道转换完成。每个注入序列转换周期结束后，EOIC 位将被置 1。如果 EOICIE 位被置 1 将产生一个中断。

常规序列和注入序列不能同时工作在间断模式，同一时刻只能有一个序列被设置成间断模式。


图 21-6. 间断运行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/d229f4dc6cd6d5eeac567cc709b1eac14f64b54558c57c6c27c92946437376ca.jpg)


常规序列间断模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 DISRC 位和 ADC_CTL1 寄存器的 RDMA 位为 1；

2. 配置 ADC_CTL0 寄存器的 DISNUM[2:0]位；

3. 配置 ADC_RSQx 和 ADC_SAMPTx 寄存器；

4. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMRC[1:0]位；

5. 准备 DMA 模块，用于传输来自 ADC_RDATA 的数据；

6. 设置 SWRCST 位，或者给常规序列产生一个 TRIGSEL 触发；

7. 如果需要，重复步骤 6；

注入序列间断模式的软件流程：

1. 设置 ADC_CTL0 寄存器的 DISIC 位和 ADC_CTL1 寄存器的 IDMA 位为 1；

2. 配置 ADC_ISQ 和 ADC_SAMPTx 寄存器；

3. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMIC[1:0]位；

4. 准备 DMA 模块，用于传输来自 ADC_IDATA 的数据；

5. 设置 SWICST 位，或者给注入序列产生一个 TRIGSEL 触发；

6. 如果需要，重复步骤 5；

## 21.4.5. 注入序列管理

## 自动注入

如果将 ADC_CTL0 寄存器的 ICA位置 1，在常规序列之后，注入序列被自动转换。该模式下注入序列的外部触发不能被使能。该模式可以转换 ADC_RSQ0~ADC_RSQ2 和 ADC_ISQ 寄存器中设置的多至 20 个通道。除了 ICA 位之外，如果 CTN 位也被置 1，常规序列将在注入序列之后被自动转换。


图 21-7. 自动注入，CTN=1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/7297c1094806f0ba7ef215003000ea592c7e312918dfc13cc302aad6274933b8.jpg)



不能同时使用自动注入和间断模式。


## 触发注入

清除 ICA 位，在常规序列转换期间如果注入序列的软件触发或者 TRIGSEL 触发发生，则启动注入序列转换。这种情况下，ADC 取消常规序列中当前正在转换的通道，注入序列进行转换。注入序列转换结束后，ADC 从上次被取消的常规序列通道处重新开始转换。


图 21-8. 触发注入


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/923d165421dcf2f216185e53c828af37749c1f69d647dc6ee8b5fbf375c4f10c.jpg)


## 21.4.6. 转换数据锁存

ADC 拥有 4 个锁存数据寄存器，ADC_LDATAx（x=0…3），这些寄存器可以在常规或注入序列通道转换完成后锁存数据。锁存数据寄存器的控制逻辑如 21-9. 。


图 21-9. 数据锁存


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/9fdb31e8c9f8fe5665fe549d6de33213a1f2e9953d3537177e28d6e740830c7d.jpg)


是从常规序列还是从注入序列中选择要锁存的数据，可以通过ADC_LDCTL寄存器中的SEQSELx（x=0…3）位来决定，而 COVSELx 位则选择要锁存序列中的哪个转换结果。

设置 ADC_LDATAx（x=0…3）寄存器来存储注入序列或常规序列的转换结果，默认存储注入序列的第 x 次转换结果。

因此，除了使用 DMA 从 ADC_RDATA 或 ADC_IDATA 寄存器传输转换数据外，还可以直接从锁存数据寄存器读取数据，这为序列的连续转换提供了更大的灵活性。


图 21-10. ADC_LDATAx 读取序列数据


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/1e3706aa523189ec33780d5a24c0b7009db070f628934f4df57176a46e5507b8.jpg)


<table><tr><td>ADC_LDATA0</td><td>ADC_LDATA1</td><td>ADC_LDATA2</td><td>ADC_LDATA3</td></tr><tr><td>CH9 转换数据</td><td>CH10 转换数据</td><td>CH0 转换数据</td><td>CH1 转换数据</td></tr></table>

触发注入模式下从 ADC_LDATAx 读取序列数据的软件流程：

1. 设置 ADC_CTL0 寄存器的 SM 位；

2. 配置 ADC_RSQx，ADC_ISQ 和 ADC_SAMPTx 寄存器；

3. 配置 ADC_LDCTL 寄存器的 SEQSEL2，COVSEL2[3:0]，SEQSEL3 和 COVSEL3[3:0]位域用于常规序列；

4. 配置 ADC_LDCTL 寄存器的 SEQSEL0，COVSEL0[3:0]，SEQSEL1 和 COVSEL1[3:0]位域用于注入序列；

5. 如果有需要，配置 ADC_CTL1 寄存器中的 ETMRC[1:0]和 ETMIC[1:0]位域；


注入通道数据


6. 设置 SWRCST 位，或者给常规序列产生一个 TRIGSEL 触发；

7. 设置 SWICST 位，或者给注入序列产生一个 TRIGSEL 触发；

8. 等待 EORC 或 EOIC 标志位置 1；

9. 如果 EORC 标志位置 1，从 ADC_LDATA2 和 ADC_LDATA3 寄存器中读常规序列 ADC 转换结果；

10. 写 0 清除 EORC 标志位。

11. 如果 EOIC 标志位置 1，从 ADC_LDATA0 和 ADC_LDATA1 寄存器中读注入序列 ADC 转换结果；

12. 写 0 清除 EOIC 标志位。

## 21.4.7. 转换结果阈值监测功能

## 模拟看门狗 0

ADC_CTL0寄存器的RWD0EN和IWD0EN位置1将分别使能常规序列和注入序列的模拟看门狗0 功能。该功能用于监测转换结果是否超过设定的阈值。如果 ADC 的模拟转换电压低于低阈值或高于高阈值，ADC_STAT 状态寄存器的 WD0E 位将被置 1。如果 WD0EIE 位被置 1，将产生中断。ADC_WD0HT 和 ADC_WD0LT 寄存器用来设定高低阈值。内部数据的比较在对齐之前完成，因此阈值与ADC_CTL1寄存器的DAL 位确定的对齐方式无关。ADC_CTL0寄存器的RWD0EN，IWD0EN，WD0SC 和 WD0CHSEL[4:0]位可以用来选择模拟看门狗 0 监控单一通道或者多通道。

## 21.4.8. 数据存储模式

ADC_CTL1 寄存器的 DAL 位确定转换后数据存储的对齐方式。

注入序列通道转换的数据值已经减去了在 ADC_IOFFx 寄存器中定义的偏移量，因此结果可能是一个负值。符号值是一个扩展值。


图 21-11. 12 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


注入通道数据


<table><tr><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


DAL=0 


<table><tr><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

<table><tr><td>Sign</td><td>D11</td><td>D10</td><td>D9</td><td>D8</td><td>D7</td><td>D6</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td><td>0</td></tr></table>


DAL=1 


6 位分辨率的数据存储模式不同于 12 位/10 位/8 位分辨率数据存储模式，如 21-12. 6


DAL=0



常规通道数据


储模式


图 21-12. 6 位数据存储模式



常规通道数据


<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>


注入通道数据


<table><tr><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td><td>0</td></tr></table>


注入通道数据


<table><tr><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>Sign</td><td>D5</td><td>D4</td><td>D3</td><td>D2</td><td>D1</td><td>D0</td><td>0</td></tr></table>


DAL=1 


## 21.4.9. 采样时间配置

ADC 使用若干个 CK_ADC 周期对输入电压采样，采样周期数目可以通过 ADC_SAMPT0 和ADC_SAMPT1 寄存器的 SPTn[2:0]位更改。每个通道可以用不同的时间采样。在 12 位分辨率的情况下，总采样转换时间=采样时间+12.5 个 CK_ADC 周期。

例如：

CK_ADC = 42MHz，采样时间为 1.5 个周期，那么总的转换时间为：“1.5+12.5”个 CK_ADC 周期，即 0.333us。

## 21.4.10. 外部触发

TRIGSEL 触发输入的上升沿或者软件触发可以触发常规序列或注入序列的转换。ADC_CTL1 寄存器的 ETMRC[1:0]和 ETMIC[1:0]分别控制常规序列或注入序列的触发模式。


表 21-3.外部触发模式和触发类型


<table><tr><td>ETMRC[1:0]/ETMIC[1:0]</td><td>触发模式</td><td>触发类型</td></tr><tr><td>00, 01, 10</td><td>外部触发使能</td><td>硬件触发:来自TRIGSEL的信号</td></tr><tr><td>11</td><td>外部触发禁能</td><td>软件触发:SWRCST/SWICST</td></tr></table>

## 21.4.11. DMA 请求

DMA请求，可以通过设置 ADC_CTL1 寄存器的 RDMA 或者 IDMA位来使能，它用于传输常规或者注入序列多个通道的转换结果。ADC 在常规或者注入序列的一个通道转换结束后产生一个 DMA请求，DMA 接受到请求后可以将转换的数据从 ADC_RDATA 或者 ADC_IDATA 寄存器传输到用户指定的目的地址。

## 21.4.12. ADC 内部通道

将 ADC_CTL1 寄存器的 TSVEN 位置 1 可以使能温度传感器通道（ADC0_IN16），将 ADC_CTL1寄存器的 INREFEN 位置 1 可以使能 V<sub>REFINT</sub>通道（ADC0_IN17）。温度传感器可以用来测量器件周围的温度。传感器输出电压能被 ADC 转换成数字量。建议温度传感器的采样时间至少设置为t<sub>s_temp</sub> µs（具体数值请参考 Datasheet）。温度传感器不用时，复位 TSVREN 位可以将其置于掉电模式。

温度传感器的输出电压随温度会发生线性变化，由于芯片生产过程的多样化，温度变化曲线的偏移在不同的芯片上会有不同（最多相差 $45 \textdegree$ ）。内部温度传感器更适合于检测温度的变化，而不是测量绝对温度。如果需要测量精确的温度，应该使用一个外置的温度传感器来校准这个偏移错误。

使用温度传感器：

1. 配置温度传感器通道（ADC0_IN16）的转换序列和采样时间大于t<sub>s_temp</sub> µs；

2. 置位ADC_CTL1寄存器的TSVEN位，使能温度传感器；

3. 置位ADC_CTL1寄存器的ADCON位，或者由TRIGSEL触发启动ADC转换；

4. 读取内部温度传感器输出电压V<sub>temperature</sub>，并由下面公式计算出实际温度：

$$
\text { 温度 } (^ {\circ} \mathrm{C}) = \frac {\mathrm{V} _ {2 5} - \mathrm{V} _ {\text { temperature }}}{\text { Avg\_Slope }} + 2 5\tag{21-1}
$$

V<sub>temperature</sub>：温度传感器的输出电压。

$\vee _ { 2 5 } \colon$ 内部温度传感器在 $\boldsymbol { 2 5 ^ { \circ } \mathrm { C } }$ 时的输出电压，典型值请参考相关型号 Datasheet。

Avg_Slope：温度与内部温度传感器输出电压曲线的均值斜率，典型值请参考相关型号datasheet。

内部电压参考（V<sub>REFINT</sub>）提供了一个稳定的（带隙基准）电压输出给 ADC 和比较器。V<sub>REFINT</sub>内部连接到 ADC0_IN17 输入通道。

## 21.4.13. 可编程分辨率（DRES）

对寄存器 ADC_OVSAMPCTL 中的 DRES[1:0]位进行编程即可配置分辨率为 6、8、10、12 位。对于那些不需要高精度数据的应用，可以使用较低的分辨率来实现更快速地转换。只有在 ADCON位为 0 时，才能修改 DRES[1:0]的值。ADC 转换的结果只有 12 位，其余没有被用到的低位读出来都是为 $0 _ { \circ }$ 。较低的分辨率能够减少逐次逼近步骤所需的转换时间，如 21-4.tCONV 所示。


表 21-4. 不同分辨率对应的 t<sub>CONV</sub>时间


<table><tr><td>DRES[1:0]bits</td><td>tCONV(ADC clock)cycles)</td><td>tCONV(ns) at fADC=42MHz</td><td>ts(min)(ADC clock)cycles)</td><td>tADC(ADC clock)cycles)</td><td>tADC(ns) at fADC=42MHz</td></tr><tr><td>12</td><td>12.5</td><td>298 ns</td><td>1.5</td><td>14</td><td>333 ns</td></tr><tr><td>10</td><td>10.5</td><td>250 ns</td><td>1.5</td><td>12</td><td>286 ns</td></tr><tr><td>8</td><td>8.5</td><td>202 ns</td><td>1.5</td><td>10</td><td>238 ns</td></tr><tr><td>6</td><td>6.5</td><td>155 ns</td><td>1.5</td><td>8</td><td>190 ns</td></tr></table>

## 21.4.14. 片上硬件过采样

片上硬件过采样单元执行数据预处理以减轻 CPU 负担。它能够处理多个转换，并将多个转换的结果取平均，得出一个 16 位宽的数据。其结果根据如下公式计算得出，其中 N 和 M 的值可以被调整。 $\sf D _ { \sf 0 u t } \mathrm { ~ \boldsymbol ~ ( ~ n ~ ) ~ }$ 是指 ADC 输出的第 n 个数字信号：

$$
\text { Result } = \frac {1}{M} * \sum_ {n = 0} ^ {N - 1} D _ {\text { out }} (n)\tag{21-2}
$$

片上硬件过采样单元执行两个功能：求和和位右移。过采样率 N 是在 ADC_OVSAMPCTL 寄存器的 OVSR[2:0]位定义，它的取值范围为 2x 到 256x。除法系数 M 定义一个多达 8 位的右移，它通过 ADC_OVSAMPCTL 寄存器 OVSS[3:0]位进行配置。

求和单元能够生成一个多达 20 位（256*12 位）的值。首先，将这个值要进行右移，将移位后剩余的部分再通过取整转化一个近似值，最后将高位会被截断，仅保留最低 16 位有效位作为最终值传入对应的数据寄存器中。


图 21-13. 20 位到 16 位的结果截断


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/1cf4fa597436eb8f531a62e8462c00ff2f34940cb9a1880f3d10b5b5e914bc27.jpg)



注意：如果移位后的中间结果还是超过 16 位，那么该结果的高位就会被直接截掉。


21-14. 5 描述一个从原始 20 位的累积数值处理成 16 位结果值的例子。


图 21-14. 右移 5 位和取整的数例


<table><tr><td>19</td><td>15</td><td>11</td><td>7</td><td>3</td><td>0</td></tr><tr><td>2</td><td>A</td><td>C</td><td>D</td><td>6</td><td></td></tr></table>

<table><tr><td></td><td>15</td><td>11</td><td>7</td><td>3</td><td>0</td></tr><tr><td>四舍五入取近似值以及右移5位之后的结果</td><td>1</td><td>5</td><td>6</td><td>6</td><td></td></tr></table>

21-5. N M 给出了 N 和 M 各种组合的数据格式，初始转换值为 0xFFF。


表 21-5. N 和 M 的最大输出值（灰色部分表示截断）


<table><tr><td>Oversampling ratio</td><td>Max Raw data</td><td>No-shift OVSS=0000</td><td>1-bit shift OVSS=0001</td><td>2-bit shift OVSS=0010</td><td>3-bit shift OVSS=0011</td><td>4-bit shift OVSS=0100</td><td>5-bit shift OVSS=0101</td><td>6-bit shift OVSS=0110</td><td>7-bit shift OVSS=0111</td><td>8-bit shift OVSS=1000</td></tr><tr><td>2x</td><td>0x1FFE</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td><td>0x003F</td><td>0x001F</td></tr><tr><td>4x</td><td>0x3FFC</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td><td>0x003F</td></tr><tr><td>8x</td><td>0x7FF8</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td><td>0x007F</td></tr><tr><td>16x</td><td>0xFFFF0</td><td>0xFFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td><td>0x00FF</td></tr><tr><td>32x</td><td>0x1FFE0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td><td>0x01FF</td></tr><tr><td>64x</td><td>0x3FFC0</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td><td>0x03FF</td></tr><tr><td>128x</td><td>0x7FF80</td><td>0xFF80</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td><td>0x07FF</td></tr><tr><td>256x</td><td>0xFFFF00</td><td>0xFF00</td><td>0xFF80</td><td>0xFFC0</td><td>0xFFE0</td><td>0xFFF0</td><td>0x7FF8</td><td>0x3FFC</td><td>0x1FFE</td><td>0x0FFF</td></tr></table>

和标准的运行模式相比，过采样模式的转换时间不会改变：在整个过采样序列的过程中采样时间仍然保持相等。每 N 个转换就会产生一个新的数据，一个等价的延迟为：

$$
N \times t _ {A D C} = N \times (t _ {S M P L} + t _ {C O N V})\tag{21-3}
$$

## 21.5. ADC 同步模式

在具有两个或三个 ADC 的设备上，可以使用 ADC 同步模式。

在 ADC 同步模式下，根据 ADC0_CTL0 寄存器中 SYNCM[3:0]位所选的模式，转换的启动可以是

ADC0 主和 ADC1 从的交替触发或同步触发。在同步模式下，ADC0 配置为 TRIGSEL 触发转换时，ADC1 必须配置为软件触发。

ADC 同步模式如 21-6. ADC 所示。

在 ADC 同步模式下，即使不使用 DMA 功能，也要将 RDMA 置位。ADC1 的转换数据可以通过ADC0 的常规数据寄存器（ADC0_RDATA）读取。


表 21-6. ADC 同步模式表


<table><tr><td>SYNCM[3: 0]</td><td>模式</td></tr><tr><td>0000</td><td>独立模式。所有的ADC都独立工作。</td></tr><tr><td>0001</td><td>ADC0和ADC1工作在常规并行和注入并行组合模式。</td></tr><tr><td>0010</td><td>ADC0和ADC1工作在常规并行和注入交替触发组合模式。</td></tr><tr><td>0011</td><td>ADC0和ADC1工作在注入并行和常规快速交叉组合模式。</td></tr><tr><td>0100</td><td>ADC0和ADC1工作在注入并行和常规慢速交叉组合模式。</td></tr><tr><td>0101</td><td>ADC0和ADC1工作在注入并行模式。</td></tr><tr><td>0110</td><td>ADC0和ADC1工作在常规并行模式。</td></tr><tr><td>0111</td><td>ADC0和ADC1工作在常规快速交叉模式。</td></tr><tr><td>1000</td><td>ADC0和ADC1工作在常规慢速交叉模式。</td></tr><tr><td>1001</td><td>ADC0和ADC1工作在注入交替触发模式。</td></tr></table>

当 ADC 工作在同步模式，而非独立模式时，如果需要再将 ADC 配置成其他同步模式，则需要在配置成其他同步模式前，首先将 ADC 配置成独立模式。

ADC 同步框图如 21-15. ADC 所示。


图 21-15. ADC 同步框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/a0be6e26f62b126d88beda81e6a697b87cdbc5e9cc21885d506e66428d968816.jpg)


## 21.5.1. 独立模式

在这种模式下，ADC 同步是忽略的，每个 ADC 都独立工作。

## 21.5.2. 常规并行模式

设置 ADC0_CTL0 寄存器中 SYNCM[3:0]位为 0110，使能常规并行模式。在常规并行模式中，根据 ADC0 中选择的外部触发，ADC0 和 ADC1 并行的转换常规通道。触发选择由 ADC0 的ADC_CTL1 寄存器 ETMRC[1:0]位进行配置。

在转换结束时产生 EORC 中断（如果 ADC 使能了该中断）。常规并行模式的行为如 21-16.于16个通道的常规并行模式所示。

32 位 ADC0_RDATA 寄存器包含上半字（由 ADC1 转换的数据构成）和下半字（由 ADC0 转换的数据构成），32 位的 DMA 被用来将 ADC0_RDATA 中的数据传送到 SRAM。


图 21-16. 基于 16 个通道的常规并行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/6f07f484077b502c483861e0fc6a0b49be6c10257d280acde2d8d3e66f821ea6.jpg)


注意：

1. 两个 ADC 不能同时转换同一个通道。（当两个 ADC 转换同一通道时，采样时间不可重叠）

2. 在并行模式下，ADC0 和 ADC1 并行采样的两个通道需要设置为相同的采样时间。

3. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.3. 注入并行模式

设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 0101，使能注入并行模式。在注入并行模式中，根据ADC0 中选择的外部触发，ADC0 和 ADC1 并行的转换注入通道。触发选择由 ADC0 的 ADC_CTL1寄存器 ETMIC[1:0]位进行配置。

在注入序列转换结束时产生 EOIC 中断（如果 ADC 使能了该中断）。转换的数据都存储在每个 ADC的 ADC_IDATA 寄存器中。注入并行模式的行为如 21-17. 4 所示。


图 21-17. 4 个通道的注入并行模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/ee1bb04478de31609a7274dcbb428fece6c9c37c1d0cc77365f991afb9a56ad7.jpg)


注意：

1. 两个 ADC 不能同时转换同一个通道。（当两个 ADC 转换同一通道时，采样时间不可重叠）

2. 在并行模式下，ADC0 和 ADC1 并行采样的两个通道需要设置为相同的采样时间。

## 21.5.4. 常规快速交叉模式

此模式应用于 ADC 的常规序列（通常采样同一个通道），设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 0111，使能快速交叉模式。ADC0 中选择的外部触发产生时，ADC1 立刻启动，而 ADC0 在7 个 ADC 时钟周期后启动。触发选择由 ADC0 的 ADC_CTL1 寄存器 ETMRC[1:0]位进行配置。

如果 ADC0 和 ADC1 的 CTN 位被置位，所选的常规序列通道将在两个 ADC 中被不停的转换。

32 位 ADC0_RDATA 寄存器包含上半字（由 ADC1 转换的数据构成）和下半字（由 ADC0 转换的数据构成），在 ADC0 产生 EORC 中断后（如果 ADC 使能了该中断），可通过 32 位 DMA 将ADC0_RDATA 中数据传送到 SRAM。


图 21-18. 常规序列上的快速交叉模式（两个 ADC 的 CTN=1）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/2c44939055059483647b2f4a1f729cc602b80949d07b94966b4789aa3bbb6258.jpg)


## 注意：

1. 可允许的最大采样时间必须小于 7 个 CK_ADC 采样时钟，从而避免 ADC0 和 ADC1 在采样相同通道时出现采样时间重叠。

2. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.5. 常规慢速交叉模式

此模式应用于 ADC 的常规序列（通常采样同一个通道），设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 1000，使能慢速交叉模式。ADC0 中选择的外部触发产生时，ADC1 立刻启动，而 ADC0 在14 个 ADC 时钟周期后启动，在 ADC0 启动后的 14 个时钟周期，ADC1 再次启动。触发选择由ADC0 的 ADC_CTL1 寄存器 ETMRC[1:0]位进行配置。

在这种模式下，不能使用连续运行模式，因为在这种模式下所选的常规序列通道在两个 ADC 中被不停的转换，如 21-19. 所示。

32 位 ADC0_RDATA 寄存器包含上半字（由 ADC1 转换的数据构成）和下半字（由 ADC0 转换的数据构成），在 ADC0 产生 EORC 中断后（如果 ADC 使能了该中断），可通过 32 位 DMA 将ADC0_RDATA 中数据传送到 SRAM。


图 21-19. 常规序列上的慢速交叉模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/96612b6f2d8ee5726bdf81e0a671f00ee3ca549f22e6419d35703635608f5c2f.jpg)


注意：

1. 可允许的最大采样时间必须小于 14 个 CK_ADC 采样时钟，从而避免 ADC0 和 ADC1 在转换相同通道时出现采样时间重叠。

2. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.6. 注入交替触发模式

此模式应用于注入序列，设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 1001，使能注入交替触发模式。如果 ADC0 和 ADC1 注入序列间断运行模式禁能，ADC0 中选择的外部触发第一次产生时，ADC0 注入序列的所有通道被转换，当第二次触发产生，ADC1 注入序列的所有通道被转换。触发选择由 ADC0 的 ADC_CTL1 寄存器 ETMIC[1:0]位进行配置。

在注入序列转换结束时产生 EOIC 中断（如果 ADC 使能了该中断）。注入交替触发模式在 DISIC=0时的行为如 21-20. DISIC=0, IL=1 所示。


图 21-20. 注入交替触发模式：DISIC=0, IL=1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/167c5931a0d7537d8ade93a06601317333a84510ed185e05bc219f46b2c07044.jpg)


如果 ADC0 和 ADC1 注入序列间断运行模式使能，当第一次触发发生，ADC0 转换第一个注入通道。当第二次触发发生，ADC1 转换第一个注入通道。然后，ADC0 转换第二个注入通道，ADC1转换第二个通道，以此类推。注入交替触发模式在 DISIC=1 时的行为如 21-21.DISIC=1, IL=1 所示。


图 21-21. 注入交替触发模式：DISIC=1, IL=1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/064c34ae3ae2356195b4bef284594e5446300c0d06f416490bf96e51efd710ca.jpg)


## 注意：

1. 两个 ADC 不能同时转换同一个通道。（当两个 ADC 转换同一通道时，采样时间不可重叠）

2. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.7. 常规并行和注入并行组合模式

设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 0001，使能常规并行和注入并行组合模式。在常规并行和注入并行组合同步模式中，注入序列的并行转换可以中断常规并行转换。

在常规序列转换结束时产生 EORC 中断（如果 ADC 使能了该中断）。

在注入序列转换结束时产生 EOIC 中断（如果 ADC 使能了该中断）。

注意：

1. 在常规并行和注入并行组合模式下，ADC0 和 ADC1 并行采样的两个通道需要设置为相同的采样时间。

2. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.8. 常规并行和注入交替触发组合模式

设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 0010，使能常规并行和交替触发组合模式。在常规并行和注入交替触发组合模式中，注入序列的交替触发转换可以中断常规并行转换。当注入序列触发出现时，ADC 的注入序列转换立即开始。当常规序列转换被中断，ADC 的常规序列转换会停止在注入序列触发的时刻，并且在注入序列转换结束时，从被中断的位置恢复到并行模式。常规序列转换被注入交替触发中断的行为如 21-22. 所示。

在常规序列转换结束时产生 EORC 中断（如果 ADC 使能了该中断）。

在注入序列转换结束时产生 EOIC 中断（如果 ADC 使能了该中断）。


图 21-22. 常规并行和交替触发组合模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/116b9c3eda0581856b1fe178f9d16add25e562cb011ecc4f5d4649ecfae96515.jpg)


如果在一个注入序列转换期间，另一个注入触发出现，那么后面的这个触发将会被忽略，如 21-23.在注入序列转换过程中注入触发出现所示。


图 21-23. 在注入序列转换过程中注入触发出现


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/e2184494c8afb4da173a1bf65a9718051c0a674e1878e8e7298e5bff572dd726.jpg)


注意：

1. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.5.9. 注入并行和交叉组合模式

设置 ADC_CTL0 寄存器中 SYNCM[3:0]位为 0011 或 0100，使能注入并行和快速（慢速）交叉组合模式。

注入并行转换可以中断（快速和慢速）交叉转换，当注入触发发生时，交叉转换被中断，注入序列转换启动。在注入序列转换完成后，交叉转换恢复，如 21-24.所示。


图 21-24. 单通道交叉转换被注入序列中断


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/173a4e9c-fd42-447b-b1a6-bf537b6a66b0/b212b09ad5b2795aef9fd2b275f43ea19689ed2f94ddfc0ff0a4dbc2d4721ecb.jpg)


注意：

1. 确保设置 ADCON 位为 1 前先进行 ADC 模块复位。

## 21.6. 中断

以下任一个事件发生都可以产生中断：

 常规序列和注入序列转换结束；

 模拟看门狗事件；

单独的中断使能位可使得使用更灵活。ADC0、ADC1 被映射到同一个中断向量 IRQ18。ADC2 都被映射到中断向量 IRQ47。
