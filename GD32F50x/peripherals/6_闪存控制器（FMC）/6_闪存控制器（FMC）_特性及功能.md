## 6. 闪存控制器（FMC）

## 6.1. 简介

闪存控制器（FMC），提供了片上闪存需要的所有功能。在闪存的最大前 256K 字节空间内，CPU执行指令零等待。FMC 也提供了页擦除，整片擦除，以及 32 位整字/16 位半字编程等闪存操作。

## 6.2. 主要特征

 高达1024KB字节的片上闪存可用于存储指令或数据；

在闪存的最大前256K字节空间内，CPU执行指令零等待，在此范围外，CPU读取指令存在较长延时；

 使用了两片闪存，前512KB容量在第一片闪存（bank0）中，后续的容量在第二片闪存（bank1）中；

 Bank0的闪存页大小为2KB，bank1的闪存页大小为4KB；

 支持32位整字/16位半字编程，页擦除和整片擦除操作；

 大小为16字节的选项字节块可根据用户需求配置；

 每次系统复位后选项字节中的内容将重新加载到选项字节控制寄存器中；

 具有安全保护状态，可阻止对代码或数据的非法读访问；

 具有擦除和编程保护状态，可阻止意外写操作。

 18K字节信息块，用于引导装载程序；

 64字节OTP0（一次性编程）块用于用户数据存储。

 128K字节OTP1用于引导入口或用户数据存储。

 256字节OTP2具有写锁和读锁，用于用户数据存储。

 48字节OTP3用于关键安全配置（12字节用户可操作）。

## 6.3. 功能说明

## 6.3.1. 闪存结构

对于 GD32F50x，闪存最多有 256 页的 2K 字节和 128 页的 4K 字节。每一页都可以单独擦除。

闪存结构见 6-1. GD32F50x 。


表 6-1. GD32F50x 闪存基地址和构成


<table><tr><td colspan="2">闪存块</td><td>名称</td><td>地址范围</td><td>大小</td></tr><tr><td rowspan="8">主闪存块</td><td rowspan="4">Bank0512KB</td><td>第0页</td><td>0x0800 0000 - 0x0800 07FF</td><td>2KB</td></tr><tr><td>第1页</td><td>0x0800 0800 - 0x0800 0FFF</td><td>2KB</td></tr><tr><td>...</td><td>...</td><td>...</td></tr><tr><td>第255页</td><td>0x0807 F800 - 0x0807 FFFF</td><td>2KB</td></tr><tr><td rowspan="4">Bank1512KB</td><td>第256页</td><td>0x0808 0000 - 0x0808 0FFF</td><td>4KB</td></tr><tr><td>第257页</td><td>0x0808 1000 - 0x0808 1FFF</td><td>4KB</td></tr><tr><td>...</td><td>...</td><td>...</td></tr><tr><td>第383页</td><td>0x080F F000 - 0x080F FFFF</td><td>4KB</td></tr><tr><td colspan="2">信息块</td><td>Boot loader</td><td>0x1FFF B000- 0x1FFF F7FF</td><td>18KB</td></tr><tr><td colspan="2">选项字节块</td><td>选项字节</td><td>0x1FFF F800 - 0x1FFF F80F</td><td>16B</td></tr><tr><td rowspan="2" colspan="2">OTP0 Block</td><td>数据块</td><td>0x1FFF 7800 - 0x1FFF 783F</td><td>64B</td></tr><tr><td>锁定块</td><td>0x1FFF 7840 - 0x1FFF 787F</td><td>64B</td></tr><tr><td rowspan="2" colspan="2">OTP1 Block</td><td>数据块</td><td>0x1FF0 0000 - 0x1FF1 FFFF</td><td>128KB</td></tr><tr><td>锁定块</td><td>0x1FF2 0100 - 0x1FF2 010F</td><td>16B</td></tr><tr><td rowspan="2" colspan="2">OTP2 Block</td><td>数据块</td><td>0x1FF2 0000 - 0x1FF2 00FF</td><td>256B</td></tr><tr><td>锁定块</td><td>0x1FF2 0110 - 0x1FF2 018F</td><td>128B</td></tr><tr><td rowspan="2" colspan="2">OTP3 Block</td><td>数据块</td><td>0x1FFF 7900 - 0x1FFF 792F</td><td>48B</td></tr><tr><td>锁定块</td><td>0x1FFF 7930 - 0x1FFF 793F</td><td>16B</td></tr></table>


注意：信息块存储了引导装载程序（boot loader），不能被用户编程或擦除。


## 6.3.2. 读操作

闪存可以像普通存储空间一样直接寻址访问。对闪存取指令和取数据分别使用 CPU 的 CBUS 总

线。

对于代码区为 128KB 和 192KB 的器件，数据区的擦除操作会占用 BUS，此时对代码区的读操作会被阻塞。对于代码区为 256KB 的器件，数据区的擦除操作不会占用 BUS，此时对代码区的读操作不会被阻塞。对于所有器件，编程操作均占用 BUS，此时对代码区的读操作会被阻塞。可将读操作代码放在 SRAM 中规避该问题并避免读闪存区域。不同器件的代码区大小可参考数据手册。

## 6.3.3. FMC_CTLx / FMC_OBCTLx 寄存器解锁

复位后，FMC_CTLx 寄存器无法以写模式访问，且 FMC_CTLx 寄存器中的 LK 位为 1。解锁序列包括两次写操作，向 FMC_KEY0 寄存器写入数据以打开对 FMC_CTL0 寄存器的访问权限。这两次写操作分别是向 FMC_KEY0 寄存器写入 0x45670123 和 0xCDEF89AB。在完成这两次写操作后，FMC_CTL0 寄存器中的 LK位会被硬件复位为 0。软件可以通过将 FMC_CTL0 寄存器中的 LK位设置为 1 来重新锁定 FMC_CTL。任何对 FMC_KEY0 的错误操作都会将 LK 位设置为 1，从而锁定 FMC_CTL0 寄存器，并导致总线错误。

即使 FMC_CTL 已解锁，FMC_OBCTLx（x = 0,1,2）寄存器仍然受到保护。解锁序列包括两次写操作，分别向 FMC_OBKEY 寄存器写入 0x45670123 和 0xCDEF89AB。在完成这两次写操作后，FMC_OBCTL0 寄存器中的 OB_LK 位会被硬件复位为 0。软件可以通过先将 FMC_CTL0 寄存器中的 LK 位设置为 1，再将 FMC_OBCTL0 寄存器中的 OB_LK 位设置为 1 来重新锁定FMC_OBCTLx。

## 6.3.4. 页擦除

FMC 的页擦除功能使得主存储闪存的页内容初始化为高电平。每一页都可以被独立擦除，而不影响其他页内容。FMC 擦除页步骤如下：

1. 确保FMC_CTLx寄存器不处于锁定状态；

2. 检查FMC_STATx寄存器的BUSY位来判定闪存是否正处于擦写访问状态，若BUSY位为1，则需等待该操作结束，BUSY位变为0；

3. 置位 $\mathsf { F M C \_ C T L x }$ 寄存器的PER位；

4. 将待擦除页的绝对地址（0x08XX XXXX）写到FMC_ADDRx寄存器；

5. 通过将FMC_CTLx寄存器的START位置1来发送页擦除命令到FMC；

6. 等待擦除指令执行完毕，FMC_STATx寄存器的BUSY位清0；

7. 如果需要，使用CBUS读并验证该页是否擦除成功。

当页擦除成功执行，FMC_STATx 寄存器的 ENDF 位将置位。若 FMC_CTLx 寄存器的 ENDIE 位被置 1，则 FMC 将触发一个中断。需要注意的是，用户需确保写入的是正确的擦除地址，否则当待擦除页的地址被用来取指令或访问数据时，软件将会跑飞。该情况下，FMC 不会提供任何出错通知。另一方面，对擦写保护的页进行擦除操作将无效。如果 FMC_CTLx 寄存器的 ERRIE 位被置位，该操作将触发操作出错中断。中断服务程序可通过检测 FMC_STATx 寄存器的WPERR 位来判断该中断是否发生。 6-1. 显示了页擦除操作流程。


图 6-1. 页擦除操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/5532884cc8ae002337281fcea4a653b1ba81f2640a60e8833b7b814d8a2af183.jpg)



FMC_STAT0 寄存器反应对 bank0 和选项字节块的操作状态，FMC_STAT1 反应对 bank1 的操作状态。对 bank1 的页擦除操作与对 bank0 的页擦除操作类似。需要注意的是，在安全保护状态下，对 bank1 的页擦除，需将地址同时写至 FMC_ADDR1 和 FMC_ADDR0 寄存器。


## 6.3.5. 整片擦除

FMC 提供了整片擦除功能可以初始化主存储闪存块的内容。当设置 FMC_CTL0 寄存器中 MER 为1 时，擦除过程仅作用于 Bank0，当设置 FMC_CTL1 寄存器中 MER 为 1 时，擦除过程仅作用于Bank1，当设置 FMC_CTL0 和 FMC_CTL1 寄存器中 MER 为 1 时，擦除过程作用于整片闪存。整片擦除操作，寄存器设置具体步骤如下：

1. 确保FMC_CTLx寄存器不处于锁定状态；

2. 等待FMC_STATx寄存器的BUSY位变为0；

3. 如果单独擦除Bank0，置位FMC_CTL0寄存器的MER位。如果单独擦除Bank1，置位FMC_CTL1寄存器的MER位。如果整片擦除闪存，同时置位FMC_CTL0和FMC_CTL1寄存器的MER位；

4. 通过将FMC_CTLx寄存器的START位置1来发送整片擦除命令到FMC；

5. 等待擦除指令执行完毕，FMC_STATx寄存器的BUSY位清0；

6. 如果需要，使用CBUS读并验证是否擦除成功。

当整片擦除成功执行，FMC_STATx 寄存器的 ENDF 位置位。若 FMC_CTLx 寄存器的 ENDIE 位被置 1，FMC 将触发一个中断。由于所有的闪存数据都将被复位为 0xFFFF_FFFF，可以通过运行在 SRAM 中的程序或使用调试工具直接访问 FMC 寄存器来实现整片擦除操作。

6-2. 显示了整片擦除操作流程。


图 6-2. 整片擦除操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/d19e9e4d4558864ecdcda81d8d4e95f0c27518849ba1b41f6bcb0dffd0babf48.jpg)


## 6.3.6. 主存储闪存块编程

FMC 提供了一个 32 位整字/16 位半字编程功能，用来修改主存储闪存块内容。编程操作使用各寄存器流程如下：

1. 确保FMC_CTLx寄存器不处于锁定状态；

2. 等待FMC_STATx寄存器的BUSY位变为0；

3. 置位FMC_CTLx寄存器的PG位；

4. CBUS写一个32位整字/16位半字到目的绝对地址（0x08XX XXXX）；

5. 等待编程指令执行完毕，FMC_STATx寄存器的BUSY位清0；

6. 如果需要，使用CBUS读并验证是否编程成功。

当主存储块编程成功执行，FMC_STATx 寄存器的 ENDF 位置位。若 FMC_CTLx 寄存器的 ENDIE位被置 1，FMC 将触发一个中断。需要注意的是，执行整字/半字编程操作时需要检查目的地址是否已经被擦除。如果该地址没有被擦除，对该地址写一个非 0x0 值，FMC_STATx 寄存器的 PGERR位将被置 1，对该地址的编程操作无效（当写内容为 0x0 时，即使目的地址没有被正常擦除，也可以正确编程）。另一方面，如果目的地址在一个处于擦除和编程保护的页中，编程不会成功且FMC_STATx 寄存器的 WPERR 位将会置位。在这两种情形下，如果 FMC_CTLx 寄存器的 ERRIE位被置 1，FMC 将触发一次闪存操作错误中断。在中断服务程序中，可以检查 FMC_STATx 寄存器的 PGERR 位和WPERR 位来判断哪一种错误发生了。 6-3. 显示了主存储块编程操作流程。


图 6-3. 字编程操作流程


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/c3d83ac72e4309d659b682a6d4d85225013103bdbb2ff7c2242ead35da97019b.jpg)



注意：当 CPU 进入省电模式时，对闪存的操作将失败。


## 6.3.7. 选项字节块修改

FMC 提供擦写编程功能用来修改选项字节块内容。选项字节块共有 8 对选项字节。每对选项字节的高字节是低字节的补。当低字节被修改时，FMC 自动生成该选项字节的高字节。字节块编程操作过程如下。

1. 确保FMC_CTL0寄存器不处于锁定状态；

2. 等待FMC_STAT0寄存器的BUSY位变为0；

3. 解锁FMC_CTL0寄存器的选项字节操作位；

4. 通过编程FMC_OBCTLx寄存器写入新的选项字节内容；

5. 通过在FMC_OBCTL0寄存器中设置OB_START位，向FMC发送选项字节修改命令；

6. 通过检查FMC_STAT0寄存器中BUSY位的值，等待所有操作完成；

7. 如果需要，使用CBUS访问读取并验证闪存。

当选项字节块编程成功执行，FMC_STAT0寄存器的ENDF位置位。若FMC_CTL0寄存器的ENDIE

位被置 1，FMC 将触发一个中断。

注意：修改后的选项字节仅在产生系统复位（应置位 FMC_CTL0 的 NWLDE 位）后生效。

## 6.3.8. 选项字节块说明

每次系统复位（应置位 FMC_CTL0 的 NWLDE 位）后，闪存的选项字节块被重加载到FMC_OBSTAT 和 FMC_WP 寄存器，选项字节生效。选项字节的补字节具体为选项字节取反。当选项字节被重装载时，如果选项字节的补字节和选项字节不匹配，FMC_OBSTAT寄存器的OBERR位将被置 1，选项字节被强制设置为 0xFF。若选项字节和其补字节同为 0xFF，则 OBERR 位不置位。选项字节详情见 6-2. 。


表 6-2. 选项字节


<table><tr><td>地址</td><td>名称</td><td>出厂值</td><td>说明</td></tr><tr><td>0x1fff f800</td><td>SPC</td><td>0xAA</td><td>选项字节安全保护值0xAA:无安全保护0xCC:安全保护级别高除0xAA或0xCC以外的任何值:安全保护级别低。</td></tr><tr><td>0x1fff f801</td><td>SPC_N</td><td>0x55</td><td>SPC补字节</td></tr><tr><td>0x1fff f802</td><td>USER</td><td>0x9F</td><td>[7]:保留[6:5]:NWLD_CLK选择无等待时间区域加载的时钟。00:200M PLL CLK01:160M PLL CLK10:120M PLL CLK11:8M IRC8M CLK[4]:ECC_EN0:禁用SRAM ECC1:启用SRAM ECC[3]:SRAM_RST0:电源复位后初始化SRAM。1:电源复位后不初始化SRAM。[2]:nRST_STDBY0:设置待机模式时产生复位而不是进入待机模式;1:设置待机模式时进入待机模式而不产生复位。[1]:nRST_DPSLP0:设置深度睡眠模式时产生复位而不进入深度睡眠模式1:设置深度睡眠模式时进入深度睡眠模式而不产生复位[0]:nWDG_HW0:硬件使能独立看门狗功能1:软件使能独立看门狗功能</td></tr><tr><td>0x1fff f803</td><td>USER_N</td><td>0x60</td><td>USER补字节值</td></tr><tr><td>0x1fff f804</td><td>DATA[7:0]</td><td>0xFF</td><td>用户定义数据7到0位</td></tr><tr><td>0x1fff f805</td><td>DATA_N[7:0]</td><td>0xFF</td><td>DATA补字节值的7到0位</td></tr><tr><td>0x1fff f806</td><td>DATA[15:8]</td><td>0xFF</td><td>用户定义数据15到8位</td></tr><tr><td>0x1fff f807</td><td>DATA_N[15:8]</td><td>0xFF</td><td>DATA补字节值的15到8位</td></tr><tr><td>0x1fff f808</td><td>WP[7:0]</td><td>0xFF</td><td>页擦除/编程保护值的7到0位0:保护生效1:未保护</td></tr><tr><td>0x1fff f809</td><td>WP_N[7:0]</td><td>0xFF</td><td>WP补字节值的7到0位</td></tr><tr><td>0x1fff f80a</td><td>WP[15:8]</td><td>0xFF</td><td>页擦除/编程的保护值的15到8位</td></tr><tr><td>0x1fff f80b</td><td>WP_N[15:8]</td><td>0xFF</td><td>WP补字节值的15到8位</td></tr><tr><td>0x1fff f80c</td><td>WP[23:16]</td><td>0xFF</td><td>页擦除/编程的保护值的23到16位</td></tr><tr><td>0x1fff f80d</td><td>WP_N[23:16]</td><td>0xFF</td><td>WP补字节值的23到16位</td></tr><tr><td>0x1fff f80e</td><td>WP[31:24]</td><td>0xFF</td><td>页擦除/编程的保护值的31到24位</td></tr><tr><td>0x1fff f80f</td><td>WP_N[31:24]</td><td>0xFF</td><td>WP补字节值的31到24位</td></tr></table>

## 6.3.9. 页擦除/编程保护

FMC 的页擦除/编程保护功能可以阻止对闪存的意外操作。当 FMC 对被保护页进行页擦除或编程操作时，操作本身无效且 FMC_STATx 寄存器的WPERR 位将被置 1。如果WPERR 位被置 1 且FMC_CTL 寄存器的 ERRIE位也被置 1 来使能相应的中断，FMC 将触发闪存操作出错中断，等待CPU 处理。配置选项字节块的WP[31:0]某位为 0 可以单独使能某几页的保护功能。如果在选项字节块执行了擦除操作，所有的闪存页擦除和编程保护功能都将失效。当选项字节的 WP被改变时，需要系统复位使之生效。


表 6-3. 页保护 WP 位


<table><tr><td>WP 位</td><td>所保护的页</td></tr><tr><td>WP[0]</td><td>Page0, Page1</td></tr><tr><td>WP[1]</td><td>Page2, Page3</td></tr><tr><td>...</td><td>...</td></tr><tr><td>WP[29]</td><td>Page58, Page59</td></tr><tr><td>WP[30]</td><td>Page60, Page61</td></tr><tr><td>WP[31]</td><td>Page62 - Page383</td></tr></table>

## 6.3.10. OTP 闪存块编程

OTP 编程方法与 Bank0 相同，使用 FMC_CTL0 和 FMC_STAT0 寄存器。所有 OTP 只能编程一次，且无法擦除。锁定块的每个字节只能从 0xFF 编程为 0x00，不能设置为其他值。

FMC 提 供 了 一 个 32 位 整 字 / 16 位 半 字 / 8 位 字 节 的 编 程 功 能 ， 用 于 修 改OTP0/OTP1/OTP2/OTP3 的内容。可用的编程宽度如 6-4. OTP 。


表 6-4. OTP 可用编程位宽


<table><tr><td rowspan="2">块</td><td rowspan="2">名称</td><td rowspan="2">大小</td><td colspan="3">可用编程位宽</td></tr><tr><td>32位</td><td>16位</td><td>8位</td></tr><tr><td rowspan="2">OTP0</td><td>数据区</td><td>64*1字节</td><td>-</td><td>-</td><td>1</td></tr><tr><td>锁定区</td><td>1*64字节</td><td>-</td><td>-</td><td>1</td></tr><tr><td rowspan="2">OTP1</td><td>数据区</td><td>16*8K字节</td><td>1</td><td>1</td><td>1</td></tr><tr><td>锁定区</td><td>1*16字节</td><td>-</td><td>-</td><td>1</td></tr><tr><td rowspan="2">OTP2</td><td>数据区</td><td>64*4字节</td><td>1</td><td>1</td><td>1</td></tr><tr><td>锁定区</td><td>1*128字节</td><td>-</td><td>-</td><td>1</td></tr><tr><td rowspan="2">OTP3</td><td>数据区</td><td>3*4字节</td><td>1</td><td>-</td><td>-</td></tr><tr><td>锁定区</td><td>3*4字节</td><td>1</td><td>-</td><td>-</td></tr></table>

注意：如果使用 BootLoader 修改 OTP1 和 OTP2 的内容，只支持 32 位整字的编程功能，并且 4字节对齐。

OTP0 块可以划分为 64 个数据块（每块包含 1 字节）和 1 个锁定块（包含 64 字节）。锁定块的地址范围为 0x1FFF 7840 到 0x1FFF 787F。数据块的地址范围为 0x1FFF 7800 到 0x1FFF 783F。每个锁定字节（0x00：锁定，0xFF：不锁定）可以锁定对应的数据块，从而防止对该数据块进行编程。位于地址 0x1FFF 7840 的锁定字节 0 锁定地址 0x1FFF 7800 的数据块 0，以此类推。编程被锁定的数据块将会导致WPERR 位编程保护错误。


表 6-5. OTP0 锁


<table><tr><td>锁字节</td><td>锁字节地址</td><td>被锁数据块</td><td>被锁数据地址</td></tr><tr><td>0</td><td>0x1FFF 7840</td><td>0</td><td>0x1FFF 7800</td></tr><tr><td>1</td><td>0x1FFF 7841</td><td>1</td><td>0x1FFF 7801</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>62</td><td>0x1FFF 787E</td><td>62</td><td>0x1FFF 783E</td></tr><tr><td>63</td><td>0x1FFF 787F</td><td>63</td><td>0x1FFF 783F</td></tr></table>

OTP1 块可以划分为 16 个数据块（每块包含 8K 字节）和 1 个锁定块（包含 16 字节）。数据块的地址范围为 0x1FF0 0000 到 0x1FF1 FFFF。锁定块的地址范围为 0x1FF2 0100 到 0x1FF2 010F。每个锁定字节（0x00：锁定，0xFF：不锁定）可以锁定对应的数据块，从而防止对该数据块进行编程。编程被锁定的数据块将会导致 WPERR 位编程保护错误。OTP1 数据块是否可读由FMC_OTP1CFG 寄存器中的 OTP1REN[15:0]决定。读取被保护的数据块将会导致总线错误。


表 6-6. OTP1 锁


<table><tr><td>锁字节</td><td>锁字节地址</td><td>被锁数据块</td><td>被锁数据地址</td></tr><tr><td>0</td><td>0x1FF2 0100</td><td>0</td><td>0x1FF0 0000 - 0x1FF0 1FFF</td></tr><tr><td>1</td><td>0x1FF2 0101</td><td>1</td><td>0x1FF0 2000 - 0x1FF0 3FFF</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>14</td><td>0x1FF2 010E</td><td>14</td><td>0x1FF1 C000 - 0x1FF1 DFFF</td></tr><tr><td>15</td><td>0x1FF2 010F</td><td>15</td><td>0x1FF1 E000 - 0x1FF1 FFFF</td></tr></table>

OTP2 块可以划分为 64 个数据块（每块包含 4 字节）和 1 个锁定块（包含 128 字节）。数据块的地址范围为 0x1FF2 0000 到 0x1FF2 00FF。写锁定块的地址范围为 0x1FF2 0110 到 0x1FF2 014F。每个锁定字节（0x00：锁定，0xFF：不锁定）可以锁定对应的数据块，从而防止对该数据块进行编程。位于地址 0x1FF2 0110 的锁定字节 0 锁定数据块 0，以此类推。编程被锁定的数据块将会导致WPERR 位编程保护错误。

读锁定块的地址范围为 0x1FF2 0150 到 0x1FF2 018F。每个锁定字节（0x00：锁定，0xFF：不锁定）可以锁定对应的数据块，从而防止读取。位于地址 0x1FF2 0150 的读锁定字节 64 锁定数据块 0，以此类推。

当 FMC_CTL0 寄存器中的 RLBE 位被置位时，OTP2 数据块中对应于读锁定块的数据将无法读取。例如，安全验证数据存储在 OTP2 中，且从 OTP1 开始的安全启动程序可以读取 OTP2 信息进行验证。在完成验证后，RLBE被设置，然后跳转到其他程序。在下次复位之前，与读锁定块对应的 OTP2 数据块都无法读取。读取被锁定的数据块将会导致总线错误。


表 6-7. OTP2 锁


<table><tr><td>写锁字节</td><td>写锁字节地址</td><td>读锁字节</td><td>读锁字节地址</td><td>被锁数据块</td><td>被锁数据地址</td></tr><tr><td>0</td><td>0x1FF2 0110</td><td>64</td><td>0x1FF2 0150</td><td>0</td><td>0x1FF2 0000 - 0x1FF2 0003</td></tr><tr><td>1</td><td>0x1FF2 0111</td><td>65</td><td>0x1FF2 0151</td><td>1</td><td>0x1FF2 0004 - 0x1FF2 0007</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>63</td><td>0x1FF2 014F</td><td>127</td><td>0x1FF2 018F</td><td>63</td><td>0x1FF2 00FC - 0x1FF2 00FF</td></tr></table>

OTP3 块可以划分为 3 个数据块（每块包含 4 字节）和 3 个锁定块（每块包含 4 字节）。锁定块的地址分别为 0x1FFF 7930、0x1FFF 7934 和 0x1FFF 7938。数据块的地址分别为 0x1FFF 7900、0x1FFF 7910 和 0x1FFF 7920。每个锁定字（全 0：锁定，全 1：不锁定）可以锁定对应的数据块，从而防止对该数据块进行编程。地址范围 0x1FFF 7930 - 0x1FFF 7933 的锁定块 0 锁定地址范围 0x1FFF 7900 - 0x1FFF 7903 的数据块 0，以此类推。OTP3 只可写读无效，在成功编程后将立即生效，可通过 FMC_OTP3_STAT 寄存器对应位域读取结果。


表 6-8. OTP3 锁


<table><tr><td>锁块</td><td>锁块地址只可写</td><td>名称全0有效</td><td>数据块</td><td>被锁数据地址只可写</td><td>名称全0有效</td></tr><tr><td>0</td><td>0x1FFF 7930 - 0x1FFF 7933</td><td>NDBG_LK</td><td>0</td><td>0x1FFF 7900 - 0x1FFF 7903</td><td>NDBG</td></tr><tr><td>1</td><td>0x1FFF 7934 - 0x1FFF 7937</td><td>NBTSB_LK</td><td>1</td><td>0x1FFF 7910 - 0x1FFF 7913</td><td>NBTSB</td></tr><tr><td>2</td><td>0x1FFF 7938 - 0x1FFF 793B</td><td>BTFOSEL_LK</td><td>2</td><td>0x1FFF 7920 - 0x1FFF 7923</td><td>BTFOSEL</td></tr></table>

## 6.3.11. 安全保护

FMC 提供了一个安全保护功能来阻止非法读取闪存。此功能可以很好地保护软件和固件免受非法的用户操作。 6-9. 表示不同配置的安全保护等级，安全保护等级划分三等。

无保护状态：当 SPC 字节设置为 0xAA，闪存将处于非安全保护状态。主存储块和选项字节可以被所有操作模式访问。

保护等级低：当设置 SPC 字节为除 0xAA或 0xCC 外的任何值，激活低安全保护等级。主存储闪存块仅能被用户代码访问。在调试模式或者从 SRAM 中启动或者从 bootloader 模式启动时，这些模式下对主存储块的操作都被禁止。无论是在调试模式或者从 SRAM 中启动，还是从 bootloader模式启动，如果对主存储块执行一次读操作，将会产生一个总线错误。在调试模式或者从 SRAM中启动时或者从 bootloader 模式启动，如果对主存储块执行一次编程/擦除操作，FMC_STATx 寄存器中的 WPERR 位会被置位。在低安全保护等级下，对于选项字节的所有操作都被允许。如果通过设置 SPC 字节为 0xAA 进入无保护状态，主存储闪存块将执行一次整片擦除操作。

保护等级高：当设置 SPC 字节为 0xCC，激活高安全保护等级。当编程选择该保护等级时，调试模式，从 SRAM 中启动，或者从 bootloader 启动都被禁止。主存储闪存块可由用户代码的所有操作进行访问。SPC 字节禁止再次编程。所以，如果高保护等级被激活，将不能再降回到低保护等级或无保护等级。


表 6-9. 安全保护


<table><tr><td>SPC[7:0]</td><td>安全保护</td></tr><tr><td>0xAA</td><td>无保护</td></tr><tr><td>除0xAA或0xCC之外</td><td>保护等级低</td></tr><tr><td>0xCC</td><td>保护等级高</td></tr></table>

## 6.3.12. 频率控制

FMC 模块使用时钟为 CK_FMC 访问 sip flash，与 AHB 时钟 CK_AHB 需要满足一定的频率关系，CK_FMC 需要不慢于时钟 CK_AHB，但不高于 AHB 时钟的 7 倍：

$$
\mathrm {CK\_FMC} \geqslant \mathrm {CK\_AHB} \geqslant 1 / 7 \mathrm {CK\_FMC}
$$

推荐的切频配置方法如下：

如果升频：

1. 需要保持CK_FMC选择时钟源为时钟CK_AHB，同时将CK_FMC与CK_AHB的频率提高；

2. 再根据需要单独提高CK_FMC频率；

如果降频：

1. 先将CK_FMC选择时钟源为AHB时钟CK_AHB；

2. CK_FMC与CK_AHB同步降频。
