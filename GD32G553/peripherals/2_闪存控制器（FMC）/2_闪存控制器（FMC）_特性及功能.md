## 2. 闪存控制器（FMC）

## 2.1. 简介

闪存控制器（FMC），提供了片上闪存需要的所有功能。在闪存的前512K字节空间内，CPU执行指令需要少量等待时间。FMC也提供了页擦除，整片擦除，以及编程操作。

## 2.2. 主要特性

 高达512KB字节的片上闪存可用于存储指令或数据，高达2KB一次性编程块。

- bank0：256KB。 

- bank1：256KB。 

- OTP：2KB。 

- Bootloader：2x13KB。 

- 单bank模式（DBS=0）：128位读取位宽，闪存页大小2KB。

- 双bank模式（DBS=1）：64位读取位宽，闪存页大小1KB。

 ECC支持单个位错误纠正和双位错误检测。

 在闪存空间内，CPU执行指令和读取数据需要0~7个等待时间。

 预取缓冲区以加速读操作。

 CBUS指令缓存区为2KB，由64条缓存线组成，每条缓存线为4x64位或2x128位。

■ CBUS数据缓存区为512B，由16条缓存线组成，每条缓存线为4x64位或2x128位。

 双bank架构支持边读边写(RWW)。

 支持64位双字编程，页擦除和整片擦除操作。

 2K字节OTP块（一次性编程），用于存储用户数据。

 大小为2x48字节的选项字节可根据用户需求配置。

 当系统电源上下电复位时，选项字节被上载到选项字节控制寄存器。

 具有安全保护状态，可阻止对代码或数据的非法读访问。

 具有4块擦写保护区域（当DBS=1时每个bank有2块擦写保护区域，当DBS=0时整个片上闪存有4块擦写保护区域），可阻止意外擦写操作。

 具有 2 块仅执行的专用代码读保护区域（当 DBS=1 时每个 bank 有 1 块擦写保护区域，当DBS=0 时整个片上闪存有 2 块仅执行区域）。

 具有仅执行一次的安全用户区域（当DBS=1时每个bank有1块安全用户区域，当DBS=0时整个片上闪存只有1块安全用户区域）.

 支持低功耗模式。

## 2.3. 功能说明

## 2.3.1. 闪存结构

主存储闪存高达 512KB，双 bank 结构下由 2x256 页组成，每页 1KB，还包含 2x13KB 的用于引导装载程序的信息块。主存储闪存的每页都可以单独擦除。基地址和大小如 2-1.512KB bank闪存基地址和构成所示。


表 2-1. 512KB 双 bank 闪存基地址和构成


<table><tr><td colspan="2">闪存块</td><td>名称</td><td>地址范围</td><td>大小(字节)</td></tr><tr><td rowspan="14">主存储闪存块</td><td rowspan="7">Bank0</td><td>第0页</td><td>0x0800 0000 - 0x0800 03FF</td><td>1KB</td></tr><tr><td>第1页</td><td>0x0800 0400 - 0x0800 07FF</td><td>1KB</td></tr><tr><td>第2页</td><td>0x0800 0800 - 0x0800 0BFF</td><td>1KB</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>第255页</td><td>0x0803 FC00 - 0x0803 FFFF</td><td>1KB</td></tr><tr><td rowspan="7">Bank1</td><td>第0页</td><td>0x0804 0000 - 0x0804 03FF</td><td>1KB</td></tr><tr><td>第1页</td><td>0x0804 0400 - 0x0804 07FF</td><td>1KB</td></tr><tr><td>第2页</td><td>0x0804 0800 - 0x0804 0BFF</td><td>1KB</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>第255页</td><td>0x0807 FC00 - 0x0807 FFFF</td><td>1KB</td></tr><tr><td rowspan="2" colspan="2">信息块</td><td>Bank0 引导装载程序</td><td>0x1FFF 0000 - 0x1FFF 33FF</td><td>13KB</td></tr><tr><td>Bank1 引导装载程序</td><td>0x1FFF 8000 - 0x1FFF B3FF</td><td>13KB</td></tr><tr><td rowspan="2" colspan="2">选项字节块</td><td>选项字节0</td><td>0x1FFF 7800~0x1FFF 782F</td><td>48B</td></tr><tr><td>选项字节1</td><td>0x1FFF F800~0x1FFF F82F</td><td>48B</td></tr><tr><td colspan="2">一次性编程块</td><td>Bank0 一次性编程块</td><td>0x1FFF 7000~0x1FFF 77FF</td><td>2KB</td></tr><tr><td colspan="2">JTAG 一次编程块</td><td>Bank1 一次性编程块</td><td>0x1FFF F000~0x1FFF F00F</td><td>16B</td></tr></table>


注意：对于 256KB 系列产品，闪存页只含第 0 页到第 127 页。对于 128KB 系列产品，闪存页只含第 0 页到第 63 页。BANK0 和 BANK1 地址是连续的。



主存储闪存高达 512KB，单 bank 结构下由 256 页组成，每页 2KB。基地址和大小如 2-2. 512KBbank 所示。



表 2-2. 512KB 单 bank 闪存基地址和构成


<table><tr><td>闪存块</td><td>名称</td><td>地址范围</td><td>大小(字节)</td></tr><tr><td rowspan="8">主存储闪存块</td><td>第0页</td><td>0x0800 0000 - 0x0800 07FF</td><td>2KB</td></tr><tr><td>第1页</td><td>0x0800 0800 - 0x0800 0FFF</td><td>2KB</td></tr><tr><td>第2页</td><td>0x0800 1000 - 0x0800 17FF</td><td>2KB</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td></tr><tr><td>第254页</td><td>0x0807F000 - 0x0807 F7FF</td><td>2KB</td></tr><tr><td>第255页</td><td>0x0807 F800 - 0x0807 FFFF</td><td>2KB</td></tr><tr><td rowspan="2">信息块</td><td>Bank0 引导装载程序</td><td>0x1FFF 0000 - 0x1FFF 33FF</td><td>13KB</td></tr><tr><td>Bank1 引导装载程序</td><td>0x1FFF 8000 - 0x1FFF B3FF</td><td>13KB</td></tr><tr><td rowspan="2">选项字节块</td><td>选项字节0</td><td>0x1FFF 7800~0x1FFF 782F</td><td>48B</td></tr><tr><td>选项字节1</td><td>0x1FFF F800~0x1FFF F82F</td><td>48B</td></tr><tr><td>一次性编程块</td><td>Bank0 一次性编程块</td><td>0x1FFF 7000~0x1FFF 77FF</td><td>2KB</td></tr><tr><td>JTAG 一次编程块</td><td>Bank1 一次性编程块</td><td>0x1FFF F000~0x1FFF F00F</td><td>16B</td></tr></table>


注意：1. 对于 256KB 系列产品，每个 bank 闪存页只含第 0 页到第 127 页。对于 128KB 系列产品，每个 bank 闪存页只含第 0 页到第 63 页。



2. 信息块存储了引导装载程序（boot loader），不能被用户编程或擦除。



3. 2KB（256 双字）OTP（一次性编程）数据区域供用户使用，OTP 区域仅由 bank0 寄存器操作。OTP 数据不能被擦除，只能写一次。如果任何位被写为 0，则该位所在的整个双字都不能被改写。


## 2.3.2. 错误检查与纠正（ECC）

ECC 机制支持：

 单个位错误检测与纠正。

 双位错误检测。

## 双 bank 模式（DBS=1）

当检测到一个错误并纠正时，FMC_ECCCS 寄存器中的 ECCCOR0 位将被置位。如果FMC_ECCCS 寄存器中的 ECCCORIE 位被置位，则会产生中断。ECC 错误位所处的 bank 号保存在 FMC_ECCCS 寄存器的 BK_ECC 中，错误位所在的地址保存在 ECCADDR[18:0]中。

当检测到两个错误时，FMC_ECCCS 寄存器中的 ECCDET0 位会被置位，并产生一个 NMI。错误

位所在的地址保存在 FMC_ECCCS 寄存器的 ECCADDR[18:0]中。

注意：当 bank 交换后，ECC 地址按照交换后的地址报错，例如访问地址 0x08000000，即实际访问 bank1，如果 ECC 报错，ECCADDR 存的地址是 0x08040000。

## 单 bank 模式（DBS=0）

如果 DBS 复位，必须首先检查 SYS_ECC 标志位。SYS_ECC 为 1，BK_ECC 表示引导加载程序的 ECC 错误发生在哪个 bank。

当在 LSB（bits63：0）检测到一个错误并纠正时，FMC_ECCCS 寄存器中的 ECCCOR0 位将被置位。当在 MSB（bits127：64）检测到一个错误并纠正时，FMC_ECCCS 寄存器中的 ECCCOR1位将被置位。如果 FMC_ECCCS 寄存器中的 ECCCORIE位被置位，则会产生中断。错误位所在的地址保存在 ECCADDR[18:0]中。

当在 LSB（bits63：0）检测到两个错误时，FMC_ECCCS 寄存器中的 ECCDET0 位将被置位并产生一个 NMI。当在 MSB（bits127：64）检测到两个错误时，FMC_ECCCS 寄存器中的 ECCDET1位将被置位并产生一个 NMI。错误位所在的地址保存在 FMC_ECCCS 寄存器的 ECCADDR[18:0]中。

注意：1. Flash 内存中的数据保存为 72 位字，每双字（64 位）增加了 8 位纠错码，但增加的 8 位是由硬件自动计算的，用户不能访问。

2. 对于原始数据 0xFF FFFF FFFF FFFF FFFF，不支持 ECC。

3. 当出现新的 ECC 错误时，仅当清除 ECCCOR0/ECCCOR1 和 ECCDET0/ECCDET1 后，才会更新 ECCADDR 和 BK_ECC。当 bank 切换后，ECCADDR 表示的映射地址也随之变化。

4. 当清除ECCDET0/ECCDET1时，SYSCFG_STAT寄存器中的FLASHECCIF位会被同步清除，清除 FLASHECCIF 位会同步清除 ECCDET0/ECCDET1。

5. 预取 buffer 或 cache 读取数据或指令也可能生成 ECC 错误，即使数据或指令未被 CPU 使用。

6. 当编程原始数据为全 F 时，ECC 计算会 bypass 本次操作。不需要擦除，再次编程其他值可正常写入。

## 2.3.3. 读操作

闪存可以像普通存储空间一样直接寻址访问。对闪存取指令和取数据使用 CPU 的 CBUS 总线。

## 增加等待状态

读取闪存时，需要根据 AHB 时钟频率正确配置 FMC_WS 寄存器中的 WSCNT 位。WSCNT 与AHB 时钟频率的关系如 2-3. WSCNT AHB LDO= 1.1V 所示。


表 2-3. WSCNT 与 AHB 时钟频率对应关系（LDO= 1.1V）


<table><tr><td>AHB时钟频率</td><td>WSCNT配置</td></tr><tr><td>&lt;= 10MHz</td><td>0(添加0个等待状态)</td></tr><tr><td>&lt;= 20MHz</td><td>1(添加1个等待状态)</td></tr><tr><td>&lt;= 50MHz</td><td>2(添加2个等待状态)</td></tr><tr><td>&lt;= 70MHz</td><td>3(添加3个等待状态)</td></tr><tr><td>&lt;= 90MHz</td><td>4(添加4个等待状态)</td></tr><tr><td>&lt;= 120MHz</td><td>5(添加5个等待状态)</td></tr><tr><td>&lt;= 150MHz</td><td>6(添加6个等待状态)</td></tr><tr><td>&lt;= 170MHz</td><td>7(添加7个等待状态)</td></tr><tr><td>&lt;= 216MHz</td><td>7(添加7个等待状态)</td></tr></table>

如果发生系统复位，AHB 时钟频率为 8MHz，此时 WSCNT 置为 0。当 AHB 时钟频率大于等于170MHz时，WSCNT 均为 7（添加 7 个等待状态）。

## 注意：

1. 如果希望增加 AHB 时钟频率。首先，参考 2-3. WSCNT AHB LDO=1.1V ，根据目标 AHB时钟频率配置WSCNT 位。然后，增加 AHB时钟频率至目标频率。禁止在配置WSCNT 位之前增加 AHB 时钟频率。

2. 如果希望降低 AHB 时钟频率。首先，降低 AHB 时钟频率至目标频率。然后，参考 2-3. WSCNTAHB LDO= 1.1V ，根据目标 AHB 时钟频率配置 WSCNT 位。禁止在降低AHB 时钟频率之前配置WSCNT 位。

由于添加了等待状态，读效率非常低（例如：170MHz 时需添加 7 个等待状态）。为了加速读操作，需要用到以下功能。

## 当前缓存区：

当前缓存区总是被使能的。每次从闪存中读取数据时，当前缓存区可以缓存 64 位或 128 位数据。因为 CPU 每次读操作只需要 32 位或 16 位数据。因此在顺序代码下，CPU 所需数据可以从当前缓存区获取而不必重复从闪存中获取。

## 预取缓存区

置位 FMC_WS 寄存器中 PFEN 位来使能预取缓存区。在顺序代码下，当 CPU 执行来自当前缓存区的数据时（64 位），按 32 位执行时需要至少 2 个时钟周期，按 16 位执行时需要至少 4 个时钟周期。在这种情况下，从 flash 闪存中预取下一个双字地址的数据并存储在预取缓存区。当 CPU执行完当前缓存区的数据时，预取缓存区提供下次需要执行的数据。

## 指令缓存区

置位 FMC_WS 寄存器中 ICEN 位来使能指令缓存区。指令缓存区仅在 CBUS 取数据时使用。指

令缓存区为 2KB，由 64 条缓存线组成，每条缓存线为 2 x 128 或 4 x 64 位。

当指令存在于 CBUS 指令缓存区时，CPU 从 CBUS 指令缓存区读取指令无延迟。当指令不存在于 CBUS指令缓存区并且也不存在于当前缓存区/预取缓存区时，CBUS指令缓存区从闪存中读取指令并复制到 CBUS 指令缓存区。当所有指令缓存线被填充，LRU（最近最少使用）策略被用于转移指令缓存线中的代码。

## 数据缓存区

置位 FMC_WS 寄存器中 DCEN 位来使能 CBUS 数据缓存区。CBUS 数据缓存区仅在 CPU 通过CBUS 取数据（不是通过 DMA）时使用，此时选项字节不可缓存。CBUS 数据缓存区为 512B，由 16 条缓存线组成，每条缓存线为 2 x 128 或 4 x 64 位。

当 CBUS 数据存在于 CBUS 数据缓存区时，CPU 从 CBUS 数据缓存区读取数据时无延迟。当CBUS 数据不存在于 CBUS 数据缓存区并且也不存在于当前缓存区/预取缓存区时，数据缓存线从闪存中读取数据并复制到 CBUS 数据缓存区。当所有数据缓存线被填充，LRU（最近最少使用）策略被用于转移数据缓存线中数据。

注意：如果在开启数据缓存的情况下修改 SYSCFG_CFG0 寄存器中的 FMC_SWP 位，可能导致CPU 在第一个周期读取 flash 数据错误，这与访问 flash 序列有关。建议延迟读取 flash 两个 AHB周期，以避免这种情况。关闭数据缓存，修改 FMC_SWP位读取 flash 数据正常。

## 2.3.4. 双 bank 边读边写特性

该闪存具有基于 bank0（256KB）和 bank1（最大 256KB）的双 bank 架构。该结构支持 RWW（边读边写）特性，即当一个 bank 上有读操作操作时，另一个 bank 无需等待其操作完成，就可以进行编程操作。

## 2.3.5. FMC_CTL/FMC_OBCTL 寄存器解锁

复位后，FMC_CTL 寄存器进入锁定状态，LK 位置为 1。通过先后向 FMC_KEY 寄存器写入0x45670123 和 0xCDEF89AB，可以使得 FMC_CTL 解锁。两次写操作后，FMC_CTL 寄存器的LK位被硬件清0。可以通过软件设置FMC_CTL寄存器的LK位为1再次锁定FMC_CTL寄存器。任何对 FMC_KEY 寄存器的错误操作都会将 LK位置 1，从而锁定 FMC_CTL 寄存器，并引发一个总线错误。

FMC_OBCTL 寄存器、FMC_CTL 中的 OBRLD 位和 OBSTART 位在 FMC_CTL 被解锁后仍然处于被保护状态。解锁过程为两次写操作，向 FMC_OBKEY 寄存器先后写入 0x08192A3B 和0x4C5D6E7F，然后硬件将 FMC_OBCTL 寄存器中的 OBLK 位清零。软件可以将 FMC_OBCTL的 OBLK 位置 1 来锁定 FMC_OBCTL 寄存器、FMC_CTL 中的 OBRLD 位和 OBSTART 位。

## 2.3.6. 页擦除

FMC 的页擦除功能使得主存储闪存的页内容初始化为高电平。每一页都可以被独立擦除，而不影响其他页内容。页擦除页操作，寄存器设置具体步骤如下：

 确保 ${ \mathsf { F M C } } \_ { \mathsf { C T L } }$ 寄存器不处于锁定状态。

 检查FMC_STAT寄存器的BUSY位来判定闪存是否正处于擦写访问状态，若BUSY位为1，则需等待该操作结束，BUSY位变为0。

在双bank情况下（DBS位置位），应先置PER位。然后在控制寄存器（FMC_CTL）中选择要擦除的页面（PNSEL）和页面所在的bank（BKSEL）。在单bank情况下（DBS位复位），设置PER位并选择要擦除的页面（PNSEL），控制寄存器 $( \mathsf { F M C \_ C T L } )$ 中的BKSEL位必须保持清除状态。

 通过将FMC_CTL寄存器的START位置1来发送页擦除命令到FMC。

 等待擦除指令执行完毕，FMC_STAT寄存器的BUSY位清0。

 如果需要，使用CBUS读并验证该页是否擦除成功。

当页擦除操作成功执行且使能操作结束中断 (ENDIE = 1)时，FMC_STAT 寄存器中的 ENDF 将被置位。如果 FMC_CTL 寄存器中的 ENDIE 位被置位，FMC 将触发中断。需要注意的是，用户需确保写入的是正确的擦除地址，否则当待擦除页的地址被用来取指令或访问数据时，软件将会“跑飞”。该情况下，FMC 不会有任何出错提示。另一方面，对擦写保护的页进行擦除操作将无效。此时如果 FMC_CTL 寄存器中的 ERRIE 位置位，则 FMC 将触发闪存操作错误中断。页擦除操作流程如 2-1. 所示。


图 2-1. 页擦除操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/85ddfb44cfc97259ee7ab2c858add9f7a4126c772d5dd059a18d03a26a036686.jpg)


## 2.3.7. 整片擦除

FMC 提供了整片擦除功能可以初始化主存储闪存块的内容。这种擦除可以通过将 MER0 位设置为1 来仅擦除 bank0，或者通过将 MER1 位设置为 1 来仅擦除 Bank1，或者通过将 MER0 和 MER1位都设置为 1 来擦除整个闪存。整片擦除操作，寄存器设置具体步骤如下：

 确保FMC_CTL寄存器不处于锁定状态。

 检查FMC_STAT寄存器的BUSY位来判定闪存是否正处于擦写访问状态，若BUSY位为1，则需等待该操作结束，BUSY位变为0。

 如果只擦除bank0，则在FMC_CTL寄存器中置位MER0位。如果只擦除bank1，则在FMC_CTL寄存器中置位MER1位。如果要擦除整个闪存，在FMC_CTL寄存器中置位MER0和MER1位。

 通过将FMC_CTL寄存器的START位置1来发送整片擦除命令到FMC。

 等待擦除指令执行完毕，FMC_STAT寄存器的BUSY位清0。

 如果需要，使用CBUS读并验证是否擦除成功。

当整片擦除成功执行且使能操作结束中断 (ENDIE = 1)，FMC_STAT 寄存器的 ENDF 位置位。若FMC_CTL 寄存器的 ENDIE位被置 1，FMC 将触发一个中断。由于所有的闪存数据都将被复位为0xFFFF FFFF，可以通过运行在 SRAM 中的程序或使用调试工具直接访问 FMC 寄存器来实现整片擦除操作。整片擦除操作流程如 2-2. 所示


图 2-2. 整片擦除操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/9aa87617aaa349155b50af13bb8d474439f9ff5aab74f4bdee93a56145f6d67a.jpg)


## 2.3.8. 主存储闪存块编程

FMC提供了一个通过CBUS修改主存储闪存内容的64位双字编程功能（2 x 32 位+ 8 位ECC）。下面的步骤显示了编程操作的寄存器设置顺序。

 确保FMC_CTL寄存器不处于锁定状态。

 检查FMC_STAT寄存器的BUSY位来判定闪存是否正处于擦写访问状态，若BUSY位为1，则需等待该操作结束，BUSY位变为0。

 置位FMC_CTL寄存器的PG位。

 CBUS写数据到目的绝对地址（0x08XX XXXX）。

CBUS 写 2 次组成一个 64 位数据，即可将数据编程入闪存。待编程数据必须双字对齐。

 等待编程指令执行完毕，FMC_STAT寄存器的BUSY位清0。

 如果需要，使用CBUS读并验证是否编程成功。

当主存储块编程执行成功且使能操作结束中断 (ENDIE = 1)时，FMC_STAT 寄存器中的 ENDF 置位，如果 FMC_CTL 寄存器中的 ENDIE 位置位，FMC 将触发中断。双字编程操作之前需要检查目的地址是否已经被擦除。如果该地址没有被擦除，即使编程 0x0，FMC_STAT 寄存器的 PGERR位也将被置 1。另外，在擦写保护页上的编程操作会被忽略，同时 FMC_STAT 中的WPERR 位将置位。在这些情况下，如果 FMC_CTL 寄存器中的 ERRIE 位被置位，则 FMC 将产生一个闪存操作错误中断。软件可以检查 FMC_STAT 寄存器中的 PGERR、PGSERR、PGMERR、PGAERR和 RPERR 位，以检测出现哪种错误。主存储块双字编程操作流程如 2-3. 所示。


图 2-3. 双字编程操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/976255b8-91a3-4446-9f05-9d7580c70d59/dfe606973a6c8d1521a32bac30582aab9ecbf15aecce4cd810714f3ab50796ca.jpg)



注意：避免在同一个 bank 中既进行读操作，又进行擦除 / 编程操作。


当编程一个双字时，从 64 位计算的 ECC 字节将添加在 64 位之后，这样，即使双字节是 0xFFFFFFFF FFFF FFFF，每次编程的总位数也是 72 位。

如果编程 / 擦除操作被掉电、复位等意外中断，闪存中的内容将无法保证并处在一种不确定的状态。因此，应采取适当的措施，以避免由于程序中断 / 擦除而造成数据丢失。

## 2.3.9. OTP 编程

OTP 编程方法与主储存闪存编程相同。OTP 块只能被编程一次并且不能被擦除。

注意：必须确保在 OTP 编程操作时不会发生任何意外中断，例如系统复位或掉电。如果发生意外

中断，闪存中的数据有很小可能性会出错。

## 2.3.10. 选项字节

## 选项字节说明

每次系统上电/下电复位或在 FMC_CTL 寄存器中 OBRLD 位置 1 后，闪存的选项字节寄存器重新加载到相应选项字节块中，选项字节生效。选项补码字节与选项字节相反。当选项字节重新加载时，如果选项字节补码与选项字节不匹配，则 FMC_STAT 寄存器中的 OBERR 位将被置 1。选项字节详情见下表 2-4. 。


表 2-4. 选项字节


<table><tr><td>地址</td><td>名称</td><td>说明</td></tr><tr><td>0x1fff 7800</td><td>SPC</td><td>选项字节安全保护值0xAA:未保护状态除0xAA和0xCC外的任何值:保护级别低0xCC:保护级别高</td></tr><tr><td>0x1fff 7801</td><td>OB_USER[7:0]</td><td>[7]:FMC_SWP FMC存储器映射切换。0:主FLASH存储器的Bank0被映射到地址0x0804 0000,主FLASH存储器的Bank1被映射到地址0x0800 00001:主FLASH存储器的Bank0映射到地址0x0800 0000,主FLASH存储器的Bank1映射到地址0x0804 0000[6]:保留[5]:nRST_STDBY0:进入待机模式时产生复位1:进入待机模式时不产生复位[4]:nRST_DPSLP0:设置深度睡眠模式时产生复位而不进入深度睡眠模式1:设置深度睡眠模式时进入深度睡眠模式而不产生复位[3:2]:保留[1:0]:BOR_TH(BOR复位阈值)00:BOR功能关闭。01:BOR阈值1。阈值约2.2V。10:BOR阈值2。阈值约2.5V。11:BOR阈值3。阈值约2.8V。</td></tr><tr><td>0x1fff 7802</td><td>OB_USER[15:8]</td><td>[7]:nBOOT10:BOOT1为11:BOOT1为0它与BOOT0引脚共同决定boot模式[6]: DBS0: 单 bank 模式,128 位读取位宽1: 双 bank 模式,64 位读取位宽仅当 DCRP0/1 失能时该位可写。[5]: 保留[4]: BB0: 当配置从主存储块启动时,从 bank0 启动(出厂值)1: 从 bank1 启动,若 bank1 无启动程序,则从 bank0 启动[3]: 保留[2]: FWDGSPD_STDBY0: 在系统待机模式下独立看门狗暂停1: 在系统待机模式下独立看门狗运行[1]: FWDGSPD_DPSLP0: 在系统深度睡眠模式下独立看门狗暂停1: 在系统深度睡眠模式下独立看门狗运行[0]: nFWDG_HW0: 硬件使能独立看门狗功能1: 软件使能独立看门狗功能</td></tr><tr><td>0x1fff 7803</td><td>OB_USER[23:16]</td><td>[7:6]: 保留[5:4]: NRST_MDSEL00: NRST 引脚配置为复位输入/输出模式01: NRST 引脚上的低电平可以复位系统,内部复位不能驱动NRST 引脚10: NRST 引脚功能与普通 GPIO 相同,只有内部复位11: NRST 引脚配置为复位输入/输出模式[3]: nBOOT00: BOOT0 为 11: BOOT0 为 0[2]: nSWBT00: BOOT0 取决于选项位 nBOOT01: BOOT0 取决于 PB8/BOOT0 引脚[1]: TCMSRAM_ERS0: 系统复位后,TCM SRAM 被擦除1: 当系统复位时,TCM SRAM 不会被擦除[0]: SRAM_ECCEN0: SRAM 与 TCM SRAM ECC 使能1: SRAM 与 TCM SRAM ECC 失能</td></tr><tr><td>0x1fff 7804</td><td>SPC_N</td><td>SPC 补码字节</td></tr><tr><td>0x1fff 7805</td><td>OB_USER_N[7:0]</td><td>OB_USER 补码字节 7 到 0 位</td></tr></table>


GD32G553 用户手册


<table><tr><td>地址</td><td>名称</td><td>说明</td></tr><tr><td>0x1fff 7806</td><td>OB_USER_N[15:8]</td><td>OB_USER补码字节15到8位</td></tr><tr><td>0x1fff 7807</td><td>OB_USER_N[23:16]</td><td>OB_USER补码字节23到16位</td></tr><tr><td>0x1fff 7808</td><td>DCRP_SADDR0[7:0]</td><td>Bank0的DCRP区域起始地址</td></tr><tr><td>0x1fff 7809</td><td>DCRP_SADDR0[14:8]</td><td>[7]:保留[6:0]: Bank0的DCRP区域起始地址</td></tr><tr><td>0x1fff 780c</td><td>DCRP_SADDR0_N[7:0]</td><td>DCRP_SADDR0补码字节7到0位</td></tr><tr><td>0x1fff 780d</td><td>DCRP_SADDR0_N[14:8]</td><td>[7]:保留[6:0]: DCRP_SADDR0补码字节14到8位</td></tr><tr><td>0x1fff 7810</td><td>DCRP_EADDR0[7:0]</td><td>Bank0的DCRP区域结束地址</td></tr><tr><td>0x1fff 7811</td><td>DCRP_EADDR0[14:8]</td><td>[7]:保留[6:0]: Bank0的DCRP区域结束地址</td></tr><tr><td>0x1fff 7813</td><td>DCRP0_EREN</td><td>[7]: DCRP0_EREN0:当SPC等级从1降低到0时,DCRP不会被擦除1:当SPC等级从1降低到0时,DCRP会被擦除[6:0]:保留</td></tr><tr><td>0x1fff 7814</td><td>DCRP_EADDR0_N[7:0]</td><td>DCRP_EADDR0补码字节7到0位</td></tr><tr><td>0x1fff 7815</td><td>DCRP_EADDR0_N[14:8]</td><td>[7]:保留[6:0]: DCRP_EADDR0补码字节14到8位</td></tr><tr><td>0x1fff 7817</td><td>DCRP0_EREN_N</td><td>DCRP0_EREN补码字节</td></tr><tr><td>0x1fff 7818</td><td>BK0WP0_SADDR[7:0]</td><td>DBS=1BK0WP0_SADDR[7:0]包含在bank0的第1个WP区域的首页DBS=0BK0WP0_SADDR[7:0]包含在主存储闪存的第1个WP区域的首页</td></tr><tr><td>0x1fff 781a</td><td>BK0WP0_EADDR[7:0]</td><td>DBS=1BK0WP0_EADDR[7:0]包含在bank0的第1个WP区域的尾页DBS=0BK0WP0_EADDR[7:0]包含在主存储闪存的第1个WP区域的尾页</td></tr><tr><td>0x1fff 781c</td><td>BK0WP0_SADDR_N[7:0]</td><td>BK0WP0_SADDR补码字节7到0位</td></tr><tr><td>0x1fff 781e</td><td>BK0WP0_EADDR_N[7:0]</td><td>BK0WP0_EADDR补码字节7到0位</td></tr><tr><td>0x1fff 7820</td><td>BK0WP1_SADDR[7:0]</td><td>DBS=1BK0WP1_SADDR[7:0]包含在bank0的第2个WP区域的首页DBS=0BK0WP1_SADDR[7:0]包含在主存储闪存的第2个WP区域的首页</td></tr><tr><td>0x1fff 7822</td><td>BK0WP1_EADDR[7:0]</td><td>DBS=1</td></tr></table>


GD32G553 用户手册


<table><tr><td>地址</td><td>名称</td><td>说明</td></tr><tr><td></td><td></td><td>BK0WP1_EADDR[7:0]包含在bank0的第2个WP区域的尾页DBS=0BK0WP1_EADDR[7:0]包含在主存储闪存的第2个WP区域的尾页</td></tr><tr><td>0x1fff 7824</td><td>BK0WP1_SADDR_N[7:0]</td><td>BK0WP1_SADDR补码字节7到0位</td></tr><tr><td>0x1fff 7826</td><td>BK0WP1_EADDR_N[7:0]</td><td>BK0WP1_EADDR补码字节7到0位</td></tr><tr><td>0x1fff 7828</td><td>SCR_PAGE_CNT0[7:0]</td><td>[7:0]:配置bank0安全用户区域的页数</td></tr><tr><td>0x1fff 7829</td><td>SCR_PAGE_CNT0[8]</td><td>[0]:SCR_PAGE_CNT0[8]</td></tr><tr><td>0x1fff 782a</td><td>BOOTLK</td><td>[0]:该位置1后强制从用户闪存区启动0:支持闪存,ram和系统启动1:只能从主闪存启动</td></tr><tr><td>0x1fff 782c</td><td>SCR_PAGE_CNT0_N[7:0]</td><td>SCR_PAGE_CNT0补码字节7到0位</td></tr><tr><td>0x1fff 782d</td><td>SCR_PAGE_CNT0_N[8]</td><td>SCR_PAGE_CNT0补码第8位</td></tr><tr><td>0x1fff 782e</td><td>BOOTLK_N</td><td>BOOTLK补码字节比特0位</td></tr><tr><td>0x1fff f808</td><td>DCRP_SADDR1[7:0]</td><td>bank1的DCRP区域起始地址</td></tr><tr><td>0x1fff f809</td><td>DCRP_SADDR1[14:8]</td><td>[7]:保留[6:0]:bank1的DCRP区域起始地址</td></tr><tr><td>0x1fff f80c</td><td>DCRP_SADDR1_N[7:0]</td><td>DCRP_SADDR1补码字节7到0位</td></tr><tr><td>0x1fff f80d</td><td>DCRP_SADDR1_N[14:8]</td><td>[7]:保留[6:0]:DCRP_SADDR1补码字节14到8位</td></tr><tr><td>0x1fff f810</td><td>DCRP_EADDR1[7:0]</td><td>bank1的DCRP区域结束地址</td></tr><tr><td>0x1fff f811</td><td>DCRP_EADDR1[14:8]</td><td>[7]:保留[6:0]:bank1的DCRP区域结束地址</td></tr><tr><td>0x1fff f814</td><td>DCRP_EADDR1_N[7:0]</td><td>DCRP_EADDR1补码字节7到0位</td></tr><tr><td>0x1fff f815</td><td>DCRP_EADDR1_N[14:8]</td><td>[7]:保留[6:0]:DCRP_EADDR1补码字节14到8位</td></tr><tr><td>0x1fff f818</td><td>BK1WP0_SADDR[7:0]</td><td>DBS=1BK1WP0_SADDR[7:0]包含在bank1的第1个WP区域的首页DBS=0BK1WP0_SADDR[7:0]包含在主存储闪存的第1个WP区域的首页</td></tr><tr><td>0x1fff f81a</td><td>BK1WP0_EADDR[7:0]</td><td>DBS=1BK1WP0_EADDR[7:0]包含在bank1的第1个WP区域的尾页DBS=0BK1WP0_EADDR[7:0]包含在主存储闪存的第3个WP区域的</td></tr></table>


GD32G553 用户手册


<table><tr><td>地址</td><td>名称</td><td>说明</td></tr><tr><td></td><td></td><td>尾页</td></tr><tr><td>0x1fff f81c</td><td>BK1WP0_SADDR_N[7:0]</td><td>BK1WP0_SADDR补码字节7到0位</td></tr><tr><td>0x1fff f81e</td><td>BK1WP0_EADDR_N[7:0]</td><td>BK1WP0_EADDR补码字节7到0位</td></tr><tr><td>0x1fff f820</td><td>BK1WP1_SADDR[7:0]</td><td>DBS=1BK1WP1_SADDR[7:0]包含在bank1的第2个WP区域的首页DBS=0BK1WP1_SADDR[7:0]包含在主存储闪存的第4个WP区域的首页</td></tr><tr><td>0x1fff f822</td><td>BK1WP1_EADDR[7:0]</td><td>DBS=1BK1WP1_EADDR[7:0]包含在bank1的第2个WP区域的尾页DBS=0BK1WP1_EADDR[7:0]包含在主存储闪存的第4个WP区域的尾页</td></tr><tr><td>0x1fff f824</td><td>BK1WP1_SADDR_N[7:0]</td><td>BK1WP1_SADDR补码字节7到0位</td></tr><tr><td>0x1fff f826</td><td>BK1WP1_EADDR_N[7:0]</td><td>BK1WP1_EADDR补码字节7到0位</td></tr><tr><td>0x1fff f828</td><td>SCR_PAGE_CNT1[7:0]</td><td>[7:0]:配置在bank1的安全用户区域的页数</td></tr><tr><td>0x1fff f829</td><td>SCR_PAGE_CNT1[8]</td><td>[0]:SCR_PAGE_CNT1[8]</td></tr><tr><td>0x1fff f82c</td><td>SCR_PAGE_CNT1_N[7:0]</td><td>SCR_PAGE_CNT1补码字节7到0位</td></tr><tr><td>0x1fff f82d</td><td>SCR_PAGE_CNT1_N[8]</td><td>SCR_PAGE_CNT1补码第8位</td></tr></table>


表 2-5. 出厂值


<table><tr><td>地址</td><td>出厂值</td></tr><tr><td>0x1fff 7800</td><td>0x0010 0355 FFEF FCAA</td></tr><tr><td>0x1fff 7808</td><td>0x0000 0000 FFFF FFFF</td></tr><tr><td>0x1fff 7810</td><td>0xFF00 FFFF 00FF 0000</td></tr><tr><td>0x1fff 7818</td><td>0x01FF 0000 FE00 FFFF</td></tr><tr><td>0x1fff 7820</td><td>0x01FF 0000 FE00 FFFF</td></tr><tr><td>0x1fff 7828</td><td>0x00FF 03FF FF00 FC00</td></tr><tr><td>...</td><td>...</td></tr><tr><td>0x1FFFF800</td><td>0x0000 0000 FFFF FFFF</td></tr><tr><td>0x1FFFF808</td><td>0x0000 0000 FFFF FFFF</td></tr><tr><td>0x1FFFF810</td><td>0xFF00 FFFF 00FF 0000</td></tr><tr><td>0x1FFFF818</td><td>0x01FF 0000 FE00 FFFF</td></tr><tr><td>0x1FFFF820</td><td>0x01FF 0000 FE00 FFFF</td></tr><tr><td>0x1FFFF828</td><td>0x00FF 01FF FF00 FE00</td></tr></table>

## 选项字节编程

FMC 提供了选项字节编程功能，可用来修改选项字节内容。编程操作过程如下：

 若FMC_CTL寄存器处于锁定状态则解锁FCM_CTL寄存器。

 检查FMC_STAT1寄存器的BUSY位来判定闪存是否正处于擦写访问状态，若BUSY位为1，则需等待该操作结束，BUSY位变为0。

 将正确的序列写入FMC_OBKEY寄存器来解锁FMC_CTL寄存器中的OBLK位。

 等待FMC_CTL寄存器的OBLK位清0。

 在选项字节寄存器中写选项字节值到对应的寄存器地址。

 置位FMC_CTL寄存器中的OBSTART位来发送选项字节编程命令。

 检查FMC_STAT寄存器中BUSY位的值，若BUSY位为1，则需等待该操作结束。

 启动系统上电/下电复位(或从待机模式退出)或设置FMC_CTL寄存器中的OBRLD位来加载到选项字节。

## 注意：

1. 一旦执行了一个选项字节的修改，首先两个 bank 的用户选项字节将自动擦除。当操作执行成功时，FMC_STAT 寄存器中的 ENDF 被置位，如果 FMC_CTL 寄存器中的 ENDIE 位被置位，FMC将触发中断。

2. Bits 63:32 是 Bits 31:0 的补码。每个选项字节位在相应的补码中都有它的补位。当选项字节加载时，ECC 先检查选项字节。只有当选项字节与其补码匹配时，才可以将选项字节写入相应的寄存器。

3. 如果选项字节与它的补码不匹配，则 FMC_STAT 寄存器中的 OBERR 位将置位。所有的OB_USER 字节都强制为 0xFF，除了 BOR_TH 是 0b000，WP 页面的状态为“无保护”，DCRP 的状态是“所有区域受保护”。

## 切换单/双 bank模式

强烈建议从 SRAM 中执行代码来执行从一种闪存模式切换到另一种闪存模式时。闪存中的数据也必须重新编程，因为在更改存储模式后闪存中的数据会被损坏。切换步骤如下所示。

 如果指令缓存、数据缓存和预取被启用，清除 FMC_WS 寄存器中的 ICEN、DCEN 和 PFEN位。

 置位 FMC_WS 寄存器中的 DCRST 位和 ICRST 位来刷新指令和数据缓存。

 清除所有 WP 页面，再 DBS 位置 1 或清 0。置位 FMC_CTL 寄存器中的 OBSTART 位来发送选项字节编程命令。然后设置 OBRLD 位来加载选项字节。

 在重新加载选项字节后擦除整个闪存。重新编程代码并设置所需的 WP 页面。然后根据需要在 FMC_WS 寄存器中设置 ICEN、DCEN 和 PFEN 位。

## 2.3.11. 仅执行区域（DCRP）

在主闪存块中，FMC 可以定义仅可执行区域，只允许来自系统的指令事务，而不允许数据访问。它允许在 DBS 位置位时为每个 bank 指定一个 DCRP 区域，或者在 DBS 位清 0 时指定两个不同的 DCRP 区域。

注意：当使用仅可执行区域功能时，用户需要相应地使用仅执行选项去编译其原生代码。

DCRP区域由起始地址偏移量和结束地址偏移量来定义。如果选择单 bank 模式，DCRP 区域最小为 32 字节。DCRP 区域 x（x= 0,1）如下定义：

 从 bank 基 地 址 + [FMC_DCRP_SADDRx x 16] （ 包 含 ） 到 bank 基 地 址 +[(FMC_DCRP_EADDRx + 1) x 16]（不包含）。

DCRP 区域由起始地址偏移量和结束地址偏移量定义。如果选择双 bank 模式，最小 DCRP 区域为 16 字节。DCRP 区域 x（x= 0,1）如下定义：

 从 bank 基 地 址 + [FMC_DCRP_SADDRx x 8] （ 包 含 ） 到 bank 基 地 址 +[(FMC_DCRP_EADDRx + 1) x 8] （不包含）。

例如，当选择双 bank 模式（DBS = 1）时，为了通过 DCRP从地址 0x0802 6B40（包含）保护到地址 0x0803 2004（包含），选项字节应如下设置：

 FMC_DCRP_SADDR0 = 0x4D68。 

 FMC_DCRP_EADDR0 = 0x6400。 

如果将两个 bank 交换，则应对 bank1 应用保护，选项字节应如下设置：

 FMC_DCRP_SADDR1 = 0x4D68. 

 FMC_DCRP_EADDR1 = 0x6400. 

在此区域执行代码时，将忽略调试事件。只有 CPU 可以访问 DCRP区域，只使用指令读取任务。在所有其他情况下，访问 DCRP 区域都是非法的。例如，读操作将返回 0 并置位 FMC_STAT 寄存器中的 RPERR 标志，而写操作将被忽略并置位 FMC_STAT 寄存器中的WPERR 标志。

DCRP区域受擦除保护，无法擦除该区域内的页。如果设置了有效的 DCRP 区域，则除非执行 SPC保护等级低到无保护状态的降级擦除，否则无法执行整片擦除。

只有 CPU 可以修改 DCRP 区域定义位和 DCRP_EREN 位。如果 DCRP 区域有效，在 SPC 等级低到无保护降级期间，DCRP_EREN 置 0，则 DCRP 区域不被擦除，否则该区域将被擦除。

注意：失效 DCRP 区域的唯一方法：当 DCRP_EREN 置 1 时，将 SPC 等级从低降到无保护。直接修改 DCRP选项字节来减小 DCRP 区域不起作用，但是增大 DCRP区域起作用。

## 2.3.12. 页擦除 / 编程保护（WP）

FMC 的扇区擦除/编程保护功能可以阻止对闪存的意外操作。当 FMC 对被保护扇区进行扇区擦除或编程操作时，操作本身无效且 FMC_STAT 寄存器的 WPERR 位将被置 1。WP区域由起始地址偏移量和结束地址偏移量定义。页面保护功能可以通过配置 WP 地址寄存器分别启用：FMC_BK0WPx（x = 0,1）和 FMC_BK1WPx （x = 0,1）。

如果选择单 bank 模式（DBS = 0），则可以在 bank 中定义 4 个 WP 区域，粒度为 2Kbytes。WP区域定义如下：

 从 bank 基 地 址 + [(BKxWPy_SADDR [7:0]) x 0x800] （ 包 含 ） 到 bank 基 地 址 +[(BKxWPy_EADDR [7:0] + 1) x 0x800]（不包含）。

如果选择双 bank 模式（DBS = 1），则可以在每个 bank 中定义 2 个WP区域，粒度为 1Kbytes。WP 区域定义如下：

 从 bank 基 地 址 + [(BKxWPy_SADDR [7:0]) x 0x400] （ 包 含 ） 到 bank 基 地 址 +[(BKxWPy_EADDR [7:0] + 1) x 0x400]（不包含）。

例如，当选择双 bank 模式(DBS = 1)时，要保护从 0x0802 2800（包含）到 0x0803 07FF（包含）的地址，则选项字节应当如下设置：

 BK0WP0_SADDR [7:0] = 0x8A. 

 BK0WP0_EADDR [7:0] = 0xC1. 

如果将两个 bank 交换，则应当如下设置：

 BK1WP0_SADDR [7:0] = 0x8A. 

 BK1WP0_SADDR [7:0] = 0xC1. 

擦除/编程保护页既不能擦除也不能编程。因此，如果一个页面受到擦除/编程保护，则不能执行整片擦除操作。

如果设置的 SPC 级别为“高”，则不能修改WP 区域，否则可以不受限制地修改WP区域。

注意：DCRP或安全用户区域受到擦除/编程保护。


表 2-6. WP 保护


<table><tr><td>WP寄存器值(x,y=0,1)</td><td>WP区域</td></tr><tr><td>BKxWPy_SADDR = BKxWPy_EADDR</td><td>页BKxWPy_SADDR被WP保护</td></tr><tr><td>BKxWPy_SADDR &gt; BKxWPy_EADDR</td><td>无WP区域</td></tr><tr><td>BKxWPy_SADDR &lt; BKxWPy_EADDR</td><td>从BKxWPy_SADDR到BKxWPy_EADDR的页被WP保护</td></tr></table>

## 2.3.13. 安全保护（SPC）

FMC 提供了一个安全保护功能来阻止非法读取闪存。此功能可以很好地保护软件和固件免受非法的用户操作。

安全保护等级划分为以下三种：

未保护状态：当将 SPC 字节及其补字节被设置为 0xAA55，系统复位以后，闪存将处于非安全保护状态。主存储块和选项字节可以被所有操作模式访问。

低等级保护：当设置 SPC 字节值为任何除 0xAA 或 0xCC 外的值，系统复位以后，低安全保护状态生效。注意，如果在调试器保持连接到 JTAG/SWD 设备时执行了 SPC 修改，则应该进行电源重置，而不是系统重置。在低等级保护下，主 flash 只能通过用户代码访问。在调试模式下，从SRAM 或引导加载程序模式启动，禁止对主 flash 进行所有操作。如果在调试模式、从 SRAM 启动或引导加载程序模式下对主 flash 进行读操作、擦写操作，则会产生总线错误。但这些模式下都可以对选项字节进行操作，从而可以通过该方式失能安全保护功能。通过将 SPC 字节及其补码值设置为 0xAA55，返回到无保护级别，然后自动触发一次整片擦除操作。如果 TCMSRAM 的某些页受保护，整个 TCMSRAM 将被擦除。注意如果配置了低级别保护且没有定义 DCRP 区域，则必须设置 DCRP_EREN 位。

高等级保护：将 SPC 字节及其补字节设置为 0xCC33 时，激活高等级安全保护。当编程选择该保护等级时，调试模式，从 SRAM 中启动，或者从 boot loader 启动都被禁止。主存储闪存块可由用户代码的所有操作进行访问。SPC 字节及其补字节禁止再次编程。所以，如果高等级保护被激活，将不能再降回到低等级保护或未保护状态。

## 2.3.14. 安全用户区域（SCR）

在主闪存块中，FMC 可以定义安全用户区域，这些安全用户区域只能在引导时执行一次，除非发生复位，否则不会再次执行。

安全用户区域可以将安全代码与应用程序非安全代码隔离开来。安全用户区域可用于保护自定义安全引导库、固件更新代码或第三方安全库。当使能了安全区域（FMC_CTL 寄存器中的 SCR0（或SCR1）置位）时，读安全用户区域操作将置 RDERR 位，擦写安全用户区域操作将置WPERR 位。

安全用户区域的大小由 FMC_BK0SCR(或 FMC_BK1SCR)寄存器的 SCR_PAGE_CNT0 [8:0] (或SCR_PAGE_CNT1 [8:0]位定义。只能在 SPC 级为无保护下修改。安全用户区域的内容在从 SPC低保护等级更改为 SPC 无保护等级时被擦除，即使它与 DCRP页面重叠。

安全用户区域定义如下：

 如果选择单bank模式（DBS = 0），则从bank基地址到bank基地址+ [(SCR_PAGE_CNT0[8:0])x 0x800]（不包含）。

 如果选择双 bank 模式（DBS = 0），则从 bank0 基地址（包含）到 bank0 基地址（包含）+[(SCR_PAGE_CNT0[8:0]) x 0x400]（不包含）和从 bank1 基地地址（包含）到 bank1 基地地址+ [(SCR_PAGE_CNT1[8:0]) x 0x400]（不包含）。

## 2.3.15. 禁用核心调试访问

在安全用户区域执行敏感代码或访问敏感数据时，可以暂时禁用对核心的调试访问。当 SPC 级别没有保护或低级别保护时，调试器可以通过软件清除在 FMC_WS 寄存器中的 DBGEN 位来禁用核心调试访问。

## 2.3.16. 强制从闪存启动

FMC_BK0SCR 寄存器中的 BOOTLK位可以配置强制系统从主闪存引导启动。该位只能在以下情况下复位：

1. SPC 为无保护等级。

2. SPC 为低保护级别，发出无保护等级修改请求后执行了全片擦除。

## 2.3.17. FMC 中断

FMC 中断事件和标志如 2-7. FMC 所示。


表 2-7. FMC 中断请求


<table><tr><td>标志</td><td>描述</td><td>清除条件</td><td>中断使能位</td></tr><tr><td>ENDF</td><td>操作结束</td><td rowspan="3">写1到FMC_STAT寄存器中对应的位</td><td>ENDIE</td></tr><tr><td>OPRERR</td><td>操作失败错误</td><td>ERRIE</td></tr><tr><td>RPERR</td><td>读保护错误</td><td>RPERRIE</td></tr><tr><td>ECCOR0/ECCOR1</td><td>ECC修正</td><td>写1到FMC_ECCCS寄存器对应的位</td><td>ECCORIE</td></tr></table>
