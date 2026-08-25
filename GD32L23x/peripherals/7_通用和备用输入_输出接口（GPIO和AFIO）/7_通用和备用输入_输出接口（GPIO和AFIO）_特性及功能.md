## 7. 通用和备用输入/输出接口（GPIO 和 AFIO）

## 7.1. 简介

最多可支持 59 个通用 I/O 引脚（GPIO），分别为 PA0 ~ PA15，PB0 ~ PB15，PC0 ~ PC15，PD0 ~ PD6，PD8 ~ PD9，PF0 ~ PF1。各片上设备用其来实现逻辑输入/输出功能。每个 GPIO端口有相关的控制和配置寄存器以满足特定应用的需求。片上设备 GPIO 引脚的外部中断由EXTI 模块的寄存器控制和配置。

GPIO 端口和其他的备用功能（Afs）备用引脚，在特定的封装下获得最大的灵活性。GPIO 引脚通过配置相关的寄存器可以用作备用功能引脚，备用功能输入/输出都可以。

每个 GPIO 引脚可以由软件配置为输出（推挽或开漏）、输入、外设备用功能或者模拟模式。每个 GPIO 引脚都可以配置为上拉、下拉或无上拉/下拉。除模拟模式外，所有的 GPIO 引脚都具备大电流驱动能力。

## 7.2. 主要特征

◼ 输入/输出方向控制；

◼ 施密特触发输入功能使能控制；

◼ 每个引脚都具有弱上拉/下拉功能；

◼ 推挽/开漏输出使能控制；

◼ 置位/复位输出使能；

◼ 可编程的边沿触发外部中断-由 EXTI 寄存器配置；

◼ 模拟输入/输出配置；

◼ 备用功能输入/输出配置；

◼ 端口锁定配置；

◼ 单周期输出翻转功能。

## 7.3. 功能说明

每个通用I/O端口都可以通过32位控制寄存器（GPIOx_CTL）配置为GPIO输入，GPIO输出，AF功能或模拟模式。引脚AFIO输入/输出是通过AFIO功能使能来选择。当端口配置为输出（GPIO输出或AFIO输出）时，可以通过GPIO输出模式寄存器（GPIOx_OMODE）配置为推挽或开漏模式。输出端口的最大速度可以通过GPIO输出速度寄存器（GPIOx_OSPD）配置。每个端口可以通过GPIO上/下拉寄存器（GPIOx_PUD）配置为浮空（无上拉或下拉），上拉或下拉功能。


表 7-1. GPIO 配置表


<table><tr><td colspan="3">PAD TYPE</td><td>CTLy</td><td>Omy</td><td>PUDy</td></tr><tr><td rowspan="3">GPIO输入</td><td rowspan="3">X</td><td>悬空</td><td rowspan="3">00</td><td rowspan="3">X</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td rowspan="6">GPIO输出</td><td rowspan="3">推挽</td><td>悬空</td><td rowspan="6">01</td><td rowspan="3">0</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td rowspan="3">开漏</td><td>悬空</td><td rowspan="3">1</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td rowspan="3">AFIO输入</td><td rowspan="3">X</td><td>悬空</td><td rowspan="3">10</td><td rowspan="3">X</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td rowspan="6">AFIO输出</td><td rowspan="3">推挽</td><td>悬空</td><td rowspan="6">10</td><td rowspan="3">0</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td rowspan="3">开漏</td><td>悬空</td><td rowspan="3">1</td><td>00</td></tr><tr><td>上拉</td><td>01</td></tr><tr><td>下拉</td><td>10</td></tr><tr><td>ANALOG</td><td>X</td><td>X</td><td>11</td><td>X</td><td>XX</td></tr></table>


7-1. GPIO 为标准I/O端口位的基本结构图。



图 7-1. GPIO 端口位的基本结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/d1572ff64f18d80edbc1baad3a0fdbae58066d7579ae44b04f58ea50e272faa1.jpg)


## 7.3.1. GPIO 引脚配置

在复位期间或复位之后，备用功能并未激活，所有 GPIO 端口都被配置成输入浮空模式，这种输入模式禁用上拉（PU）/下拉（PD）电阻。但是复位后，串行线调试为输入 PU/PD 模式。

PA14：SWCLK为PD下拉模式

PA13：SWDIO为PU上拉模式

管脚可以配置为输入或输出。并且所有的 管脚都有一个内部的弱上拉和弱下拉可以选择。当GPIO管脚可配置为输入管脚时，外部管脚上的数据在每个AHB时钟周期时都会装载

到端口输入状态寄存器（GPIOx_ISTAT）。

当GPIO引脚配置为输出引脚，用户可以配置端口的输出速度和选择输出驱动模式：推挽或开漏模式。端口输出控制寄存器（GPIOx_OCTL）的值将会从相应I/O引脚上输出。

当需要对GPIOx_OCTL进行按位写操作时不需关中断，用户可以通过写‘1’到位操作寄存器（GPIOx_BOP，或用于清0的GPIOx_BC，或用于翻转操作的GPIOx_TG）修改一位或几位，该过程仅需要一个最小的AHB写访问周期，而其他位不受影响。

## 7.3.2. 外部中断及事件

所有的端口都有外部中断的能力，如果想使用端口的外部中断功能，需要配置为输入模式。

## 7.3.3. 备用功能（AF）

当端口配置为AFIO（设置GPIOx_CTL寄存器中的CTLy值为“0b10”）时，该端口用作外设备用功能。通过配置GPIO备用功能选择寄存器（GPIOx_AFSELy（y=0..1）），每个端口可以配置16个备用功能。端口备用功能分配的详细介绍见芯片数据手册。

## 7.3.4. 附加功能

有些引脚具有附加功能，它们优先于标准GPIO寄存器中的配置。当用作ADC，DAC，CMP或附加功能时，引脚必须配置成模拟模式。当引脚用作RTC、WKUPx和振荡器附加功能时，端口类型通过相关的RTC、PMU和RCU寄存器自动设置。当附加功能禁用时，这些端口可用作普通GPIO。

## 7.3.5. 输入配置

当GPIO引脚配置为输入时：

◼ 施密特触发输入使能；

◼ 可选择的弱上拉和下拉电阻；

◼ 当前I/O引脚上的数据在每个AHB时钟周期都会被采样并存入端口输入状态寄存器；

◼ 输出缓冲器禁用。

7-2. 是I/O引脚的输入配置。


图 7-2. 输入配置的基本结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/036fb03f8fe4e71c0da9ddf17b60bf5b16e7d7d86afe160205706709647dff13.jpg)


## 7.3.6. 输出配置

当GPIO配置为输出时：

◼ 施密特触发输入使能；

◼ 可选择的弱上拉和下拉电阻；

◼ 开漏模式：输出控制寄存器设置为“0”时，相应引脚输出低电平；输出控制寄存器设置为“1”，相应管脚处于高阻状态；

◼ 推挽模式：输出控制寄存器设置为“0”时，相应引脚输出低电平；输出控制寄存器设置为“1”，相应引脚输出高电平；

◼ 在推挽模式下，对端口输出控制寄存器的读访问将返回上次写入的值；

◼ 在开漏模式下，对端口输入状态寄存器的读访问将返回I/O的状态。

7-3. 是 I/O 端口的输出配置。


图7-3. 输出配置的基本结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/03ed4a5a8a0ffbb1dab269d76dbdbfcf0b73639c11e02f5dd93ead9f09480374.jpg)


## 7.3.7. 模拟配置

当GPIO引脚用于模拟模式时：

◼ 弱上拉和下拉电阻禁用；

◼ 输出缓冲器禁用；

◼ 施密特触发输入禁用；

◼ 读端口输入状态寄存器返回“0”。

7-4. 是I/O端口的模拟高阻配置。


图 7-4. 模拟配置的基本结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/f078c118b29c7ef0f68a0277ba8d1c5b94cb885d0ce8970a1ee56f58100d942c.jpg)


## 7.3.8. 备用功能（AF）配置

为了适应不同的器件封装，GPIO端口支持软件配置将一些备用功能应用到其他引脚上。

当引脚配置为备用功能时：

◼ 输出缓冲器启用开漏或者推挽功能；

◼ 输出缓冲器由外设驱动；

◼ 施密特触发输入使能；

◼ 可选择的弱上拉/下拉电阻；

◼ I/O引脚上的数据在每个AHB时钟周期采样并存入端口输入状态寄存器；

◼ 对端口输入状态寄存器进行读操作，将获得I/O口的状态；

◼ 对端口输出控制寄存器进行读操作，将返回上次写入的值。

7-5. 是I/O端口备用功能配置图。


图7-5. 备用功能配置的基本结构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/8d648b6e-5442-4614-9a47-3d6af8a5e122/b0e6c11d1bbfcfcb9b7fe2e02b0a03cb312c452b782fd9a1297d2d4f9d044b29.jpg)


## 7.3.9. GPIO 锁定功能

GPIO的锁定机制可以保护I/O端口的配置。

被 保 护 的 寄 存 器 有 ：GPIOx_CTL，GPIOx_OMODE，GPIOx_OSPD ，GPIOx_PUD和GPIOx_AFSELy（y=0..1）。通过配置32位锁定寄存器（GPIOx_LOCK）可以锁定I/O端口的配置。当特定LOCK序列写到位于GPIOx_LOCK寄存器的LKK位上，并且Lky被置位，那么对应的端口配置直到下一次复位前将不能改变。建议在电源驱动模块驱动的配置时使用锁定功能。

## 7.3.10. GPIO 单周期输出翻转功能

通过将GPIOx_TG寄存器中对应的位写1，GPIO可以在一个AHB时钟周期内翻转I/O的输出电平。输出信号的频率可以达到AHB时钟的一半。
