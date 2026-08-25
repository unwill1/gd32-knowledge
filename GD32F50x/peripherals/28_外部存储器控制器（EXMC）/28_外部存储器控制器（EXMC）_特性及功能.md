## 28. 外部存储器控制器（EXMC）

## 28.1. 简介

外部存储器控制器 EXMC，用来访问各种片外存储器，通过配置寄存器，EXMC 可以把 AMBA 协议转换为专用的片外存储器通信协议，包括 PSRAM，NOR Flash，NAND Flash。用户还可以调整配置寄存器中的时间参数来提高通信效率。EXMC 的访问空间被划分为许多个块（Bank），每个块支持特定的存储器类型，用户可以通过对 Bank 的控制寄存器配置来控制外部存储器。

## 28.2. 主要特性

 支持片外存储器类型：

PSRAM； 

NOR Flash； 

8 位或 16 位 NAND Flash；

 AMBA协议与各种片外存储器协议转换；

 时序参数可编程可以满足用户特定需求；

 每个 Bank 有独立的片选信号；

 对于部分存储器类型支持独立的读写时序；

 对于 NAND Flash 内置硬件 ECC；

 支持 8 位，16 位或 32 位总线带宽；

 NOR Flash 和 PSRAM 支持地址总线和数据总线的复用；

 提供写使能和字节选择信号；

 当 AMBA 总线宽度与外部存储器数据宽度不同时，会自动分割操作。

## 28.3. 功能描述

## 28.3.1. 结构框图

EXMC 由 5 个模块组成：AHB 总线接口，EXMC 配置寄存器，NOR/PSRAM 控制器，NAND 控制器和外部设备接口。AHB时钟（HCLK）是参考时钟。


图 28-1. 系统架构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/8f53dbcc25b9e43da1577ab6dea4b599957ffe7ed0a39fd9da44919a70d80f52.jpg)


## 28.3.2. EXMC 访问基本规范

EXMC 是 AHB 总线至外部设备协议的转换接口。32 位的 AHB读写操作可以转化为几个连续的 8位或 16 位读写操作。在数据传输的过程中，AHB 数据宽度和存储器数据宽度可能不相同。为了保证数据传输的一致性，EXMC 读写访问需要遵从以下规范：

 AHB 访问宽度等于存储器宽度，则没有问题；

 AHB 访问宽度大于存储器宽度，则自动将 AHB 访问分割成几个连续的存储器数据宽度的传输；

 AHB 访问宽度小于存储器宽度。如果外部存储设备具有字节选择功能，如 PSRAM，则可通过它的字节通道 EXMC_NBL[1:0]来访问对应的字节。否则禁止写操作，只允许读操作。

## 28.3.3. 外部设备地址映射


图 28-2. EXMC Bank 划分


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/9df69c0c8c6c146d174399d4b4ed77d69fe898db1dc5840d54b489cbb37f0aea.jpg)


EXMC 将外部存储器分成多个 Bank，每个 Bank 占 256M 字节，其中 Bank0 又分为 4 个 Region，每个 Region 占 64M 字节。Bank1 被分成 2 个 Section，分别是属性存储空间和通用存储空间。

每个 Bank 或 Region 都有独立的片选控制信号，也都能进行独立的配置。

Bank0 用于访问 NOR、PSRAM 设备。

Bank1 用于连接 NAND Flash。

## NOR 和 PSRAM 的地址映射

28-3. Bank0 是 Bank0 四个 Region 的地址映射。AHB 地址线 HADDR[27:26]作为四个 Region 的片选信号。


图 28-3. Bank0 地址映射


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/69fd0037ccb751d635cee3056c2a426e93e5187a979a0b31cdbdb06581a9d204.jpg)


由于 HADDR[25:0]是字节地址，而外部存储器访问有可能不是按字节访问的，所以会出现地址不一致的情况，但 EXMC 能实现对 HADDR 的调整以适应外部存储器的数据宽度。具体规则如下：

 如果外部存储器的数据宽度是8位按字节对齐，EXMC内部将HADDR[25:0]与EXMC_A[25:0]相连，然后 EXMC_A[25:0]与外部存储器的地址线相连；

如果外部存储器的数据宽度是 16 位按半字对齐，就需要将 HADDR 的字节地址转化为半字地址之后再连接外存储器，EXMC 内部将 HADDR[25:1]与 EXMC_A[24:0]相连，然后EXMC_A[24:0]与外部存储器的地址线相连。

## NAND 地址映射

Bank1 用来访问 NAND Flash，Bank1 如 28-4. NAND 被分为多个存储空间。


图 28-4. NAND 地址映射


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/4985f78d223d25ef2123ab9b339ecdbfb8759f156b4decbc518330f0dcfc9183.jpg)


## NAND 地址映射

对于 NAND Flash，通用和属性空间又可以细划分为 3 个区域。 28-5. Bank1 为 Bank1通用存储空间的数据区域，指令区域和地址区域的划分。


图 28-5. Bank1 通用空间


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/cb91c7df8125f3fc3f8e8cc38630638f303d228083a1aded8724e341c1d49e48.jpg)


AHB 利用 HADDR[17:16]来实现对以上三个区的选择：

 HADDR[17:16]=00,即选择数据区；

 HADDR[17:16]=01 即选择命令区；

 HADDR[17:16]=1X 即选择地址区。

应用软件使用这 3 个区访问 NAND Flash。操作规则如下：

指令区：指定 NAND Flash 将要执行的指令，软件在命令区写入指令。在指令传输过程中，EXMC会使能命令锁存信号（CLE），CLE 映射到 EXMC_A[16]。

地址区：指定操作 NAND Flash 的地址，软件在地址区写入地址。在地址传输过程中，EXMC 会使能地址锁存信号（ALE），ALE 映射到 EXMC_A[17]。

数据区：NAND Flash 读写数据，软件在数据区读出或写入数据。当 EXMC 在数据发送模式，软件需要在数据区写入数据，当 EXMC 在数据接收模式，软件需要在数据区读取数据。由于 NANDFlash 会自动累加其内部操作地址，故在读写时不需要软件修改操作地址。

## 28.3.4. NOR/PSRAM 控制器

EXMC 模块的 NOR/PSRAM 控制器控制 Bank0，它可以支持 NOR Flash、PSRAM。EXMC 对Bank0 每个 Region 输出一个唯一的片选信号，EXMC_NE，用于 Region 的片选，所有其他的信号都是共享的。Region 有专门的寄存器控制。

注意：

在异步模式下，所有控制器输出信号在内部 AHB 总线时钟（HCLK）的上升沿改变。

在同步模式下，所有控制器输出数据在外部存储器时钟（EXMC_CLK）的下降沿改变。

## NOR/PSRAM 接口描述


表 28-1. NOR Flash 接口信号描述


<table><tr><td>EXMC 引脚</td><td>传输方向</td><td>模式</td><td>功能描述</td></tr><tr><td>EXMC_CLK</td><td>输出</td><td>同步</td><td>同步时钟信号</td></tr><tr><td>复用 EXMC_A[25:16]</td><td>输出</td><td>异步/同步</td><td>地址总线</td></tr><tr><td>EXMC_D[15:0]</td><td>输入/输出</td><td>异步/同步(复用)</td><td>地址/数据总线</td></tr><tr><td>EXMC_NE</td><td>输出</td><td>异步/同步</td><td>片选</td></tr><tr><td>EXMC_NOE</td><td>输出</td><td>异步/同步</td><td>读使能</td></tr><tr><td>EXMC_NWE</td><td>输出</td><td>异步/同步</td><td>写使能</td></tr><tr><td>EXMC_NWAIT</td><td>输入</td><td>异步/同步</td><td>等待输入信号</td></tr><tr><td>EXMC_NL(NADV)</td><td>输出</td><td>异步/同步</td><td>地址有效</td></tr></table>


表 28-2. PSRAM 复用接口信号描述


<table><tr><td>EXMC 引脚</td><td>传输方向</td><td>模式</td><td>功能描述</td></tr><tr><td>EXMC_CLK</td><td>输出</td><td>同步</td><td>同步时钟信号</td></tr><tr><td>复用 EXMC_A[25:16]</td><td>输出</td><td>异步/同步</td><td>地址总线</td></tr><tr><td>EXMC_D[15:0]</td><td>输入/输出</td><td>异步/同步</td><td>地址/数据总线</td></tr><tr><td>EXMC_NE</td><td>输出</td><td>异步/同步</td><td>片选</td></tr><tr><td>EXMC_NOE</td><td>输出</td><td>异步/同步</td><td>读使能</td></tr><tr><td>EXMC_NWE</td><td>输出</td><td>异步/同步</td><td>写使能</td></tr><tr><td>EXMC_NWAIT</td><td>输入</td><td>异步/同步</td><td>等待输入信号</td></tr><tr><td>EXMC_NL(NADV)</td><td>输出</td><td>异步/同步</td><td>地址锁存信号(地址有效使能,NADV)</td></tr><tr><td>EXMC_NBL[1]</td><td>输出</td><td>异步/同步</td><td>高字节使能</td></tr><tr><td>EXMC_NBL[0]</td><td>输出</td><td>异步/同步</td><td>低字节使能</td></tr></table>

## 支持的存储器访问模式

28-3. EXMC Bank0 列出了 EXMC 对 NOR 和 PSRAM 支持的访问模式。


表 28-3. EXMC 的 Bank0 支持的访问模式


<table><tr><td>存储器类型</td><td>访问模式</td><td>读/写</td><td>AHB传输宽度</td><td>存储器传输宽度</td><td>注释</td></tr><tr><td rowspan="2">NOR Flash</td><td>异步</td><td>R</td><td>8</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td rowspan="5"></td><td>异步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>同步</td><td>R</td><td>32</td><td>16</td><td></td></tr><tr><td rowspan="11">PSRAM</td><td>异步</td><td>R</td><td>8</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>16</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>异步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>同步</td><td>R</td><td>32</td><td>16</td><td></td></tr><tr><td>同步</td><td>W</td><td>8</td><td>16</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>同步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>同步</td><td>W</td><td>32</td><td>16</td><td></td></tr></table>

## NOR Flash/PSRAM 控制时序

EXMC 为 PSRAM、NOR Flash 等外部静态存储器提供可编程的时序参数以及多种时序模型以满足不同的需求。


表 28-4. NOR/PSRAM 控制时序参数


<table><tr><td>参数</td><td>功能</td><td>访问模式</td><td>单位</td><td>最小值</td><td>最大值</td></tr><tr><td>CKDIV</td><td>同步时钟分频比</td><td>同步</td><td>HCLK</td><td>2</td><td>16</td></tr><tr><td>DLAT</td><td>数据延迟</td><td>异步</td><td>EXMC_CLK</td><td>2</td><td>17</td></tr><tr><td>BUSLAT</td><td>总线延迟</td><td>异步读写</td><td>HCLK</td><td>1</td><td>16</td></tr><tr><td>DSET</td><td>数据建立时间</td><td>异步</td><td>HCLK</td><td>2</td><td>256</td></tr><tr><td>AHLD</td><td>地址保持时间</td><td>异步(复用)</td><td>HCLK</td><td>2</td><td>16</td></tr><tr><td>ASET</td><td>地址建立时间</td><td>异步</td><td>HCLK</td><td>1</td><td>16</td></tr></table>


表 28-5. EXMC 时序模型


<table><tr><td colspan="2">时序模型</td><td>扩展模式</td><td>模式描述</td><td>写时序参数</td><td>读时序参数</td></tr><tr><td rowspan="4">异步</td><td rowspan="4">模式 AM</td><td rowspan="4">0</td><td rowspan="4">NOR Flash 数据/地址复用</td><td>DSET</td><td>DSET</td></tr><tr><td>AHLD</td><td>AHLD</td></tr><tr><td>ASET</td><td>ASET</td></tr><tr><td>BUSLAT</td><td>BUSLAT</td></tr><tr><td rowspan="2">同步</td><td rowspan="2">模式 SM</td><td rowspan="2">0</td><td rowspan="2">NOR Flash 数据/地址复用</td><td>DLAT</td><td>DLAT</td></tr><tr><td>CKDIV</td><td>CKDIV</td></tr></table>

如 28-5. EXMC 所示，EXMC 模块 NOR Flash/PSRAM 控制器可以提供多种时序模型。用户可以通过修改 28-4. NOR/PSRAM 中列出的参数来使之适合不同类型外部存储器的时序以及满足用户的要求。

## 异步访问时序

模式 AM – NOR Flash 地址/数据总线复用


图 28-6. 复用模式读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/0c67c0883bb66315b186721037fbfa2d19ae94db2846f8a65a8830abd48d0e2a.jpg)



图 28-7. 复用模式写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/ebbd3e7128cdea7b353013e03db2eabc1b5ad75d89864c243561993905897b29.jpg)



表 28-6. 复用模式相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_PNCTL</td></tr><tr><td>31-20</td><td>保留</td><td>0x000</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>CPS</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>保留</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于存储器</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位 15 为 1 时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>0x1</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>0x2: NOR Flash</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_PNTCFG</td></tr><tr><td>31-28</td><td>保留</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>无影响</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE 上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(写操作为 DSET+2HCLK 时钟周期,读操作为 DSET+3HCLK 时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>取决于存储器与用户</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr></table>

异步通信的等待时间：

等待功能由寄存器 EXMC_PNCTLx 位 ASYNCWAIT 控制。在访问外部存储器期间，若使能异步等待功能（ASYNCWAIT=1），数据建立时间将会自动延长。延长时间的计算如下：

若存储器等待信号与 EXMC_NOE/ EXMC_NWE 信号对齐：

$$
T _ {D A T A \_ S E T U P} \geq \max T _ {W A I T \_ A S S E R T I O N} + 4 H C L K\tag{27-1}
$$

若存储器等待信号与 EXMC_NE 信号对齐：

如果

$$
\max T _ {\text { WAIT\_ASSERTION }} \geq T _ {\text { ADDRES\_PHASE }} + T _ {\text { HOLD\_PHASE }}\tag{27-2}
$$

则

$$
T _ {\text { DATA\_SETUP }} \geq (\max T _ {\text { WAIT\_ASSERTION }} - T _ {\text { ADDRES\_PHASE }} - T _ {\text { HOLD\_PHASE }}) + 4 H C L K\tag{27-3}
$$

否则

$$
T _ {D A T A \_ S E T U P} \geq 4 H C L K\tag{27-4}
$$


图 28-8. 异步等待有效时的读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/30c49299ea94bce2f470c11d5a0763d70d2eebb4483169f3dcdd47812fcff24d.jpg)



图 28-9. 异步等待有效时的写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/e3765a64f91e51309b1d33312ab5432f02443b0ef126635a09224e81699e6d14.jpg)


## 同步访问时序

同步访问模式中，存储器时钟（ $\mathsf { \Pi } _ { \mathsf { E X M C \_ C L K } } )$ 与系统时钟（HCLK）关系如下：

$$
\text { EXMC\_CLK } = \frac {\text { HCLK }}{\text { CKDIV } + 1}\tag{27-5}
$$

其中 CKDIV 是同步时钟分频比，通过配置寄存器 EXMC_PNTCFG 中的 CKDIV 位来设置不同的值。

## 1. 数据延迟与 NOR Flash 延迟

数据延迟 DLAT 是指在采样数据之前需要等待的 EXMC_CLK 周期数。它和 NOR 闪存延迟的关系

如下：

NOR 闪存延迟不包含 NADV，二者之间的关系为：

$$
\mathrm{NOR} \text {闪存延迟} = \mathrm{DLAT} + 2\tag{27-6}
$$

NOR 闪存延迟包含 NADV，二者之间的关系为：

$$
\text { NOR   闪存延迟 } = \mathrm{DLAT} + 3\tag{27-7}
$$

## 2. 数据等待

用户需要保证 EXMC_NWAIT 信号与外部设备一致。该信号通过寄存器 EXMC_PNCTL 来设置，位 NRWTEN 使能，位 NRWTCFG 决定 EXMC_NWAIT 信号是等待状态同时有效，或者比等待状态提前一个时钟周期有效，位 NRWTPOL 设置 EXMC_NWAIT 信号极性。

在 NOR Flash 的同步突发模式中，当寄存器 EXMC_PNCTL 位 NRWTEN 置 1，在数据延迟之后后检测到 EXMC_NWAIT 信号。如果 EXMC_NWAIT 有效，在 EXMC_NWAIT 无效之前会一直插入等待时钟。

 EXMC_NWAIT 有效极性：

$$
\mathrm{NRWTPOL} = 1, \text { EXMC\_NWAIT   高电平有效 }
$$

NRWTPOL = 0，EXMC_NWAIT 低电平有效

 在同步突发模式中，EXMC_NWAIT 信号有两种配置：

$$
\mathrm{NRWTCFG} = 1, \text { EXMC\_NWAIT   信号有效时，当前时钟周期数据无效 }
$$

NRWTCFG = 0，EXMC_NWAIT 信号有效时，下一个时钟周期数据无效，这是复位后的默认配置。

在 EXMC_NWAIT 信号有效的等待周期内，EXMC 会持续的给存储器发送时钟信号，保持片选和输出使能有效，并且忽视总线上的无效数据。

## 3. CRAM 页边界突发传输的自动分组

CRAM1.5中禁止突发传输跨越页边界，EXMC 遇到边界会进行传输的自动分组。为了保证正确的突发分组操作，用户需要在寄存器 EXMC_PNCTL 位 CPS中需要设定 CRAM 的页大小。

## 4. 模式 SM – 单次突发传输

对于同步突发传输，如果 AHB 需要的数据为 16 位，则 EXMC 会执行一次长度为 1 的成组传输；如果 AHB 需要的数据为 32 位，则 EXMC 会把这次传输分成 2 次 16 位的传输，即执行一次长度为 2 的突发传输。

对于其他的配置，请参考 28-3. EXMC Bank0 。

同步复用突发读时序 – NOR,PSRAM(CRAM)


图 28-10. 同步复用突发传输读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/0ad2971052cf4696c75bbaeacda35e18af6e56f3779e58c2e0ca601162b8f7a4.jpg)



表 28-7. 同步复用模式读时序配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_PNCTL</td></tr><tr><td>31-20</td><td>保留</td><td>0x000</td></tr><tr><td>19</td><td>SYNCWR</td><td>无影响</td></tr><tr><td>18-16</td><td>CPS</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>0x0</td></tr><tr><td>14</td><td>保留</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>取决于存储器</td></tr><tr><td>12</td><td>WEN</td><td>无影响</td></tr><tr><td>11</td><td>NRWTCFG</td><td>取决于存储器</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>取决于存储器</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x1,突发读使能</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>取决于存储器</td></tr><tr><td>5-4</td><td>NRW</td><td>0x1</td></tr><tr><td>3-2</td><td>NRTP</td><td>取决于存储器,0x1/0x2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1,取决于存储器与用户</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_PNTCFG(Read)</td></tr><tr><td>31-28</td><td>保留</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>数据延迟</td></tr><tr><td>23-20</td><td>CKDIV</td><td>上图设置: 0x1, EXMC_CLK=2HCLK</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE 上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>无影响</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>无影响</td></tr></table>


同步复用突发写时序 – NOR,PSRAM(CRAM)



图 28-11. 同步复用突发传输写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/f8495f5174f3394849ec39a5e3c468e399b5d1e244df41d4049f1734a3833cc3.jpg)



表 28-8. 同步复用模式写时序配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_PNCTL</td></tr><tr><td>31-20</td><td>保留</td><td>0x000</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x1,同步写使能</td></tr><tr><td>18-16</td><td>CPS</td><td>0x0</td></tr><tr><td>15</td><td>AYSNCWAIT</td><td>0x0</td></tr><tr><td>14</td><td>保留</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>取决于存储器</td></tr><tr><td>12</td><td>WREN</td><td>0x1</td></tr><tr><td>11</td><td>NRWTCFG</td><td>0x0(这里必须为0)</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NTWTPOL</td><td>取决于存储器</td></tr><tr><td>8</td><td>SBRSTEN</td><td>无影响</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>取决于存储器</td></tr><tr><td>5-4</td><td>NRW</td><td>0x1</td></tr><tr><td>3-2</td><td>NRTP</td><td>0x1</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1,取决于用户</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_PNTCFG(Write)</td></tr><tr><td>31-28</td><td>保留</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>数据延迟</td></tr><tr><td>23-20</td><td>CKDIV</td><td>上图设置:0x1,EXMC_CLK=2HCLK</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>无影响</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>无影响</td></tr></table>

## 28.3.5. NAND Flash 控制器

EXMC 模块 Bank1 支持 NAND Flash。对于 Bank1，EXMC 提供独立的寄存器来配置访问时序，支持 8 位、16 位的 NAND Flash。对于 NAND Flash，EXMC 还提供 ECC 计算模块，保证数据传输和保存的鲁棒性。

## NAND Flash 接口功能


表 28-9. 8 位/16 位 NAND 接口信号描述


<table><tr><td>EXMC 引脚</td><td>传输方向</td><td>功能描述</td></tr><tr><td>EXMC_A[17]</td><td>输出</td><td>NAND Flash 地址锁存(ALE)</td></tr><tr><td>EXMC_A[16]</td><td>输出</td><td>NAND Flash 命令锁存(CLE)</td></tr><tr><td rowspan="2">EXMC_D[7:0]/EXMC_D[15:0]</td><td rowspan="2">输入 /输出</td><td>8 位复用,双向地址/数据总线</td></tr><tr><td>16 位复用,双向地址/数据总线</td></tr><tr><td>EXMC_NCE</td><td>输出</td><td>片选</td></tr><tr><td>EXMC_NOE(NRE)</td><td>输出</td><td>输出使能</td></tr><tr><td>EXMC_NWE</td><td>输出</td><td>写使能</td></tr><tr><td>EXMC_NWAIT</td><td>输入</td><td>NAND Flash 就绪/忙输入信号 EXMC</td></tr></table>

## 支持的存储器访问模式


表 28-10. Bank1 支持的访问模式


<table><tr><td>存储器</td><td>模式</td><td>读/写</td><td>AHB传输宽度</td><td>注释</td></tr><tr><td rowspan="6">8位NAND</td><td>异步</td><td>R</td><td>8</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td></td></tr><tr><td>异步</td><td>R</td><td>16</td><td rowspan="2">分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>16</td></tr><tr><td>异步</td><td>R</td><td>32</td><td rowspan="2">分成4次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td></tr><tr><td rowspan="6">16位NAND</td><td>异步</td><td>R</td><td>8</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>不支持此操作</td></tr><tr><td>异步</td><td>R</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td rowspan="2">分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td></tr></table>

## NAND Flash 的控制时序

EXMC 能够为 NAND Flash 设备产生合适的时序信号。每个 Bank 都有相应的寄存器来对外部存储器进行管理和控制，EXMC_NCTL、EXMC_NSTAT、EXMC_NCTCFG、EXMC_NATCFG、EXMC_NECC，其中寄存器 EXMC_NCTCFG、EXMC_NATCFG 都可以配置 4 个时序参数，可以根据用户需求和外部存储器的特性来进行相应的配置。


表 28-11. NADN Flash 可编程参数


<table><tr><td rowspan="2">参数</td><td rowspan="2">读/写</td><td rowspan="2">单位</td><td rowspan="2">功能描述</td><td colspan="2">NAND Flash</td></tr><tr><td>最小值</td><td>最大值</td></tr><tr><td>存储器数据总线高阻时间(HIZ)</td><td>W/R</td><td>HCLK</td><td>启动写操作之后保持数据总线为高阻态的时间</td><td>0</td><td>255</td></tr><tr><td>存储器保持时间(HLD)</td><td>W/R</td><td>HCLK</td><td>在发送命令结束后保持地址的(HCLK)时钟周期数目,写操作时也是数据的保持时间</td><td>1</td><td>254</td></tr><tr><td>存储器等待时间(WAIT)</td><td>W/R</td><td>HCLK</td><td>发出命令的最短持续时间(HCLK)时钟周期数目</td><td>2</td><td>256</td></tr><tr><td>存储器建立时间(SET)</td><td>W/R</td><td>HCLK</td><td>发出命令之前建立地址的(HCLK)时钟周期数目</td><td>1</td><td>255</td></tr></table>

28-12. NAND flash 显示了在公共存储空间操作中定义的可编程参数。属性存储空间的可编程参数也已定义。


图 28-12. NAND flash 通用空间操作时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/31f49eeb9d2d906bcaee4dc581d67728409566b5cc3e03b0084cdcacf12fad72.jpg)


## NAND Flash 操作

EXMC 在对 NAND Flash 发送命令或地址时，需要利用其命令锁存信号（A[16]）或地址锁存信号（A[17]）这两条地址线，即 CPU 需要在特定的地址进行写操作。

示例：NAND Flash 读操作步骤：

1. 配置 EXMC_NCTL、EXMC_NCTCFG，若需要预等待功能，还需配置 EXMC_NATCFG；

2. 往通用空间写入 NAND Flash 读数据命令，即在 EXMC_NCE 和 EXMC_NWE 有效期间，EXMC_CLE（A[16]）变为有效电平（高），则被 NAND 认为写入命令；

3. 往通用空间写入读操作的起始地址，即在 EXMC_NCE 和 EXMC_NWE 有效期间，EXMC_ALE（A[17]）变为有效电平（高），则被 NAND 认为写入地址；

4. 等待 NAND 就绪信号，NAND 控制器会在这期间将和 EXMC_NCE 一直保持有效；

5. 从通用空间的数据区逐字节的读出数据；

6. 在不写入新的命令和地址，可以自动读出 NAND 下一页数据；或转到 3）写入新的地址进行下一页的读取；或转到 2）写入新的命令和地址。

## NAND Flash 预等待功能

某些 NAND Flash 要求在输入最后一个地址字节后，控制器等待 NAND Flash 就绪，并且还有一些对 EXMC_NCE 敏感型的 NAND Flash 还要求在其就绪前 NCE 必须保持有效。

下面以 TOSHIBA128M*8bit NADN Flash 为例：


图 28-13. NCE 敏感 NAND Flash 访问时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/5f568f16-f94d-40ca-beef-250eb1c1e00f/065e49a47cfffad13aaec0a2aff810686335185e0bd93ce39d4dd1f4eab7f79c.jpg)


1. 往 NAND 的通用空间命令区写入命令 CMD02. 往 NAND 的通用空间地址区写入操作地址 ADD03. 往 NAND 的通用空间地址区写入操作地址 ADD14. 往 NAND 的通用空间地址区写入操作地址 ADD25. 往 NAND 的通用空间地址区写入操作地址 ADD36. 往 NAND 的属性空间命令区写入命令 CMD1

在6)中写命令操作，EXMC使用的是寄存器EXMC_NATCFG定义的时序。经过ATTHLD时间后，NAND Flash 等待 EXMC_NWAIT 信号，ATTHLD 要大于 t<sub>WB</sub>（EXMC_NWE 高到 EXMC_NWAIT低）。对于那些对 EXMC_NCE 敏感的 NAND Flash，

对于那些对片选信号敏感的 NAND Flash，在地址字节之后的第一个地址字节输入后，一直到 B/NB就绪状态到来的这段时间中，要求片选信号 NCE 一直保持低电平。这里可以通过配置属性存储空间的 ATTHT 的值来满足 t<sub>WB</sub>的时序，这样 CPU 只有在地址字节之后写入第一个命令字节时才使用属性存储空间的时序，而在其他时候都使用通用存储空间的时序。

## NAND Flash 的 ECC 计数模块

EXMC 模块中的 Bank1 有一个 ECC 计算的硬件模块，用户可以根据 EXMC_NCTL 中的 ECCSZ来选择 ECC 计算的页面大小，通过 ECC 计算可以矫正 1 个 bit 的错误并且能检测 2 个 bit 的错误。

当 NAND 存储器块使能，ECC 模块就会检测 D[15:0]以及 EXMC_NCE、EXMC_NWE 信号。当已经完成 ECCSZ 大小字节的读写操作时，软件必须读出 EXMC_NECC 中的结果值。如果需要再次开始 ECC 计算，软件需要先将 EXMC_NECC 中 ECCEN 清 0 来清除 EXMC_NCTL 中的值，再将 ECCEN 置 1 来重新启动 ECC 计算。

