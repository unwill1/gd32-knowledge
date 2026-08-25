## 33. 外部存储器控制器（EXMC）

## 33.1. 简介

外部存储器控制器EXMC，用来访问各种片外存储器，通过配置寄存器，EXMC可以把AMBA协议转换为专用的片外存储器通信协议，包括SRAM，ROM，NOR Flash，PSRAM。用户还可以调整相关的时间参数来提高通信效率。EXMC的访问空间被划分为许多个块（Bank），每个块支持特定的存储器类型，用户可以通过对Bank的控制寄存器配置来控制外部存储器。

## 33.2. 主要特性

 支持片外存储器类型：

– SRAM – PSRAM – ROM – NOR Flash 

 AMBA协议与各种片外存储器协议转换；

 时序参数可编程可以满足用户特定需求；

 每个Bank有独立的片选信号；

 对于部分存储器类型支持独立的读写时序；

 支持8位，16位总线带宽；

 NOR Flash和PSRAM支持地址总线和数据总线的复用；

 提供写使能和字节选择信号；

 当AMBA总线宽度与外部存储器数据宽度不同时，会自动分割操作；

 写FIFO最多16个字的数据存储。

## 33.3. 功能说明

## 33.3.1. 结构框图

EXMC由4个模块组成：AHB总线接口，EXMC配置寄存器，NOR/ PSRAM控制器，和外部设备接口。AHB时钟（HCLK）是参考时钟。


图 33-1. 系统架构


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/64a06455cdd587076ddb72416e34afdea4718622fc186aaf3b69b83819436592.jpg)


## 33.3.2. EXMC访问基本规范

EXMC 是 AHB 总线至外部设备协议的转换接口。32 位的 AHB读写操作可以转化为几个连续的 8位或 16 位读写操作。在数据传输的过程中，AHB 数据宽度和存储器数据宽度可能不相同。为了保证数据传输的一致性，EXMC 读写访问需要遵从以下规范：

 AHB 访问宽度等于存储器宽度，则没有问题；

 AHB 访问宽度大于存储器宽度，则自动将 AHB 访问分割成几个连续的存储器数据宽度的传输；

AHB 访问宽度小于存储器宽度。如果外部存储设备具有字节选择功能，如 SRAM、ROM、PSRAM，则可通过它的字节通道 EXMC_NBL[1:0]来访问对应的字节。否则禁止写操作，只允许读操作。

## 33.3.3. 外部设备地址映射


图 33-2. EXMC Bank 划分


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/770cea9f0c95efd4913d11fb27201c20db5f873666f51f087f9e278eda2451d1.jpg)


EXMC 将外部存储器分成多个 Bank，每个 Bank 占 256M 字节，仅 Bank0 有效。Bank0 分为 4 个Region，每个 Region 占 64M 字节。

每个 Bank 和 Region 都有独立的片选控制信号，也都能进行独立的配置。

Bank0 用于访问 NOR、PSRAM 设备。

## NOR 和 PSRAM 的地址映射

33-3. Bank0 是 Bank0 四个 Region 的地址映射。AHB 地址线 HADDR[27:26]作为四个 Region 的片选信号。


图 33-3. Bank0 地址映射


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/0a98d0e3c6a2f63195e9f9a00c84bbcba057c326383ab97f309081d4f84d58b4.jpg)


由于 HADDR[25:0]是字节地址，而外部存储器访问有可能不是按字节访问的，所以会出现地址不一致的情况，但 EXMC 能实现对 HADDR 的调整以适应外部存储器的数据宽度。具体规则如下：

如果外部存储器的数据宽度是8位按字节对齐，EXMC内部将HADDR[25:0]与EXMC_A[25:0]相连，然后 EXMC_A[25:0]与外部存储器的地址线相连；

如果外部存储器的数据宽度是 16 位按半字对齐，就需要将 HADDR 的字节地址转化为半字地址之后再连接外存储器。EXMC 内部将 HADDR[25:1]与 EXMC_A[24:0]相连，然后EXMC_A[24:0]与外部存储器的地址线相连。

## 33.3.4. NOR / PSRAM 控制器

EXMC 模块的 NOR / PSRAM 控制器控制 Bank0，它可以支持 NOR Flash、PSRAM、SRAM、ROM和CRAM外部存储器。EXMC对Bank0每个Region输出一个唯一的片选信号，NE[x](x=0...3)，用于在 4 个 Region 中进行片选，所有其他的信号都是共享的。每个 Region 都有专门的寄存器控制。

注意：

在异步模式下，所有控制器输出信号在内部 AHB 总线时钟（HCLK）的上升沿改变。

在同步模式下，所有控制器输出数据在外部存储器时钟（EXMC_CLK）的下降沿改变。

## NOR / PSRAM 接口描述


表 33-1. NOR Flash 接口信号描述


<table><tr><td>EXMC 引脚</td><td>传输方向</td><td>模式</td><td>功能描述</td></tr><tr><td>EXMC_CLK</td><td>输出</td><td>同步</td><td>同步时钟信号</td></tr><tr><td>非复用 EXMC_A[25:0]</td><td rowspan="2">输出</td><td rowspan="2">异步/同步</td><td rowspan="2">地址总线</td></tr><tr><td>复用 EXMC_A[25:16]</td></tr><tr><td rowspan="2">EXMC_D[15:0]</td><td>输入/输出</td><td>异步/同步(复用)</td><td>地址/数据总线</td></tr><tr><td>输入/输出</td><td>异步/同步(非复用)</td><td>数据总线</td></tr><tr><td>EXMC_NE[x]</td><td>输出</td><td>异步/同步</td><td>片选,x=0/1/2/3</td></tr><tr><td>EXMC_NOE</td><td>输出</td><td>异步/同步</td><td>读使能</td></tr><tr><td>EXMC_NWE</td><td>输出</td><td>异步/同步</td><td>写使能</td></tr><tr><td>EXMC_NWAIT</td><td>输入</td><td>异步/同步</td><td>等待输入信号</td></tr><tr><td>EXMC_NL(NADV)</td><td>输出</td><td>异步/同步</td><td>地址有效</td></tr></table>


表 33-2. PSRAM 非复用接口信号描述


<table><tr><td>EXMC 引脚</td><td>传输方向</td><td>模式</td><td>功能描述</td></tr><tr><td>EXMC_CLK</td><td>输出</td><td>同步</td><td>同步时钟信号</td></tr><tr><td>EXMC_A[25:0]</td><td>输出</td><td>异步/同步</td><td>地址总线</td></tr><tr><td>EXMC_D[15:0]</td><td>输入/输出</td><td>异步/同步</td><td>数据总线</td></tr><tr><td>EXMC_NE[x]</td><td>输出</td><td>异步/同步</td><td>片选,x=0/1/2/3</td></tr><tr><td>EXMC_NOE</td><td>输出</td><td>异步/同步</td><td>读使能</td></tr><tr><td>EXMC_NWE</td><td>输出</td><td>异步/同步</td><td>写使能</td></tr><tr><td>EXMC_NWAIT</td><td>输入</td><td>异步/同步</td><td>等待输入信号</td></tr><tr><td>EXMC_NL(NADV)</td><td>输出</td><td>异步/同步</td><td>地址锁存信号(地址有效使能,NADV)</td></tr><tr><td>EXMC_NBL[1]</td><td>输出</td><td>异步/同步</td><td>高字节使能</td></tr><tr><td>EXMC_NBL[0]</td><td>输出</td><td>异步/同步</td><td>低字节使能</td></tr></table>

## 支持的存储器访问模式

33-3. 16 和 33-4. 8 列出了当存储器访问总线是 8 位或 16 位时EXMC 对 NOR，PSRAM 和 SRAM 支持的访问模式。


表 33-3. 支持的 16 位传输


<table><tr><td>存储器类型</td><td>访问模式</td><td>读/写</td><td>AHB传输宽度</td><td>存储器传输宽度</td><td>注释</td></tr><tr><td rowspan="9">NOR Flash</td><td>异步</td><td>R</td><td>8</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>16</td><td>不支持</td></tr><tr><td>异步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>8</td><td>16</td><td>不支持</td></tr><tr><td>同步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>同步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td rowspan="12">PSRAM</td><td>异步</td><td>R</td><td>8</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>16</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>异步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>8</td><td>16</td><td>不支持</td></tr><tr><td>同步</td><td>R</td><td>16</td><td>15</td><td></td></tr><tr><td>同步</td><td>R</td><td>32</td><td>16</td><td></td></tr><tr><td>同步</td><td>W</td><td>8</td><td>16</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>同步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>同步</td><td>W</td><td>32</td><td>16</td><td></td></tr><tr><td rowspan="6">SRAM和ROM</td><td>异步</td><td>R</td><td>8</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>R</td><td>32</td><td>16</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>8</td><td>16</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>异步</td><td>W</td><td>16</td><td>16</td><td></td></tr><tr><td>异步</td><td>W</td><td>32</td><td>16</td><td></td></tr></table>


表 33-4. 支持的 8 位传输


<table><tr><td>存储器类型</td><td>访问模式</td><td>读/写</td><td>AHB传输宽度</td><td>存储器传输宽度</td><td>注释</td></tr><tr><td rowspan="6">NOR Flash</td><td>异步</td><td>R</td><td>8</td><td>8</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>8</td><td></td></tr><tr><td>异步</td><td>R</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>R</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td>异步同步</td><td>WR</td><td>328</td><td>88</td><td>分成4次EXMC访问</td></tr><tr><td rowspan="2"></td><td>同步</td><td>R</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td rowspan="12">PSRAM</td><td>异步</td><td>R</td><td>8</td><td>8</td><td></td></tr><tr><td>异步</td><td>W</td><td>8</td><td>8</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>异步</td><td>R</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>R</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>8</td><td>8</td><td></td></tr><tr><td>同步</td><td>R</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>R</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td>同步</td><td>W</td><td>8</td><td>8</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>同步</td><td>W</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>同步</td><td>W</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td rowspan="6">SRAM和ROM</td><td>异步</td><td>R</td><td>8</td><td>8</td><td></td></tr><tr><td>异步</td><td>R</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>R</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>8</td><td>8</td><td>使用字节信号NBL[1:0]</td></tr><tr><td>异步</td><td>W</td><td>16</td><td>8</td><td>分成2次EXMC访问</td></tr><tr><td>异步</td><td>W</td><td>32</td><td>8</td><td>分成4次EXMC访问</td></tr></table>


注意：在异步模式下，当一次 EXMC 访问被分成多个 EXMC 访问时，EXMC 可能无法达到最高频率。


## NOR Flash / PSRAM 控制时序

EXMC 为 SRAM、ROM、PSRAM、NOR Flash 等外部静态存储器提供可编程的时序参数以及多种时序模型以满足不同的需求。


表 33-5. NOR / PSRAM 控制时序参数


<table><tr><td>参数</td><td>功能</td><td>访问模式</td><td>单位</td><td>最小值</td><td>最大值</td></tr><tr><td>CKDIV</td><td>同步时钟分频比</td><td>同步</td><td>HCLK</td><td>2</td><td>16</td></tr><tr><td>DLAT</td><td>数据延迟</td><td>同步</td><td>EXMC_CLK</td><td>2</td><td>17</td></tr><tr><td>BUSLAT</td><td>总线延迟</td><td>异步/同步读</td><td>HCLK</td><td>0</td><td>15</td></tr><tr><td>DSET</td><td>数据建立时间</td><td>异步</td><td>HCLK</td><td>1</td><td>255</td></tr><tr><td>AHLD</td><td>地址保持时间</td><td>异步(复用)</td><td>HCLK</td><td>1</td><td>15</td></tr><tr><td>ASET</td><td>地址建立时间</td><td>异步</td><td>HCLK</td><td>0</td><td>15</td></tr><tr><td>BLSET</td><td>字节信号建立时间</td><td>异步</td><td>HCLK</td><td>0</td><td>3</td></tr></table>


表 33-6. EXMC 时序模型


<table><tr><td colspan="2">时序模型</td><td>扩展模式</td><td>模式描述</td><td>写时序参数</td><td>读时序参数</td></tr><tr><td rowspan="21">异步</td><td rowspan="3">模式1</td><td rowspan="3">0</td><td rowspan="3">SRAM/PSRAM/CRAM</td><td>DSET</td><td>DSET</td></tr><tr><td>ASET</td><td>ASET</td></tr><tr><td>BLSET</td><td>BLSET</td></tr><tr><td rowspan="2">模式2</td><td rowspan="2">0</td><td rowspan="2">NOR Flash</td><td>DSET</td><td>DSET</td></tr><tr><td>ASET</td><td>ASET</td></tr><tr><td rowspan="3">模式A</td><td rowspan="3">1</td><td rowspan="3">SRAM/PSRAM/CRAM 在数据阶段 EXMC_NOE 翻转</td><td>WDSET</td><td>DSET</td></tr><tr><td>WASET</td><td>ASET</td></tr><tr><td>BLSET</td><td>BLSET</td></tr><tr><td rowspan="2">模式B</td><td rowspan="2">1</td><td rowspan="2">NOR Flash</td><td>WDSET</td><td>DSET</td></tr><tr><td>WASET</td><td>ASET</td></tr><tr><td rowspan="2">模式C</td><td rowspan="2">1</td><td rowspan="2">NOR Flash 在数据阶段 EXMC_NOE 翻转</td><td>WDSET</td><td>DSET</td></tr><tr><td>WASET</td><td>ASET</td></tr><tr><td rowspan="4">模式D</td><td rowspan="4">1</td><td rowspan="4">有地址保持功能</td><td>WDSET</td><td>DSET</td></tr><tr><td>WAHLD</td><td>AHLD</td></tr><tr><td>WASET</td><td>ASET</td></tr><tr><td>BLSET</td><td>BLSET</td></tr><tr><td rowspan="5">模式AM</td><td rowspan="5">0</td><td rowspan="5">NOR Flash 数据/地址复用</td><td>DSET</td><td>DSET</td></tr><tr><td>AHLD</td><td>AHLD</td></tr><tr><td>ASET</td><td>ASET</td></tr><tr><td>BUSLAT</td><td>BUSLAT</td></tr><tr><td>BLSET</td><td>BLSET</td></tr><tr><td rowspan="4">同步</td><td rowspan="2">模式E</td><td rowspan="2">0</td><td rowspan="2">NOR/PSRAM/CRAM 同步读 PSRAM/CRAM 同步写</td><td>DLAT</td><td>DLAT</td></tr><tr><td>CKDIV</td><td>CKDIV</td></tr><tr><td rowspan="2">模式SM</td><td rowspan="2">0</td><td rowspan="2">NOR Flash/PSRAM/CRAM 数据/地址复用</td><td>DLAT</td><td>DLAT</td></tr><tr><td>CKDIV</td><td>CKDIV</td></tr></table>

如 33-6. EXMC 所示，EXMC 模块 NOR Flash / PSRAM 控制器可以提供多种时序模型。用户可以通过修改 33-5. NOR / PSRAM 中列出的参数来使之适合不同类型外部存储器的时序以及满足用户的要求。当将寄存器 EXMC_SNCTLx 位 EXMODEN 置 1 使能扩展模式后，可以通过寄存器 EXMC_SNTCFGx 和 EXMC_SNWTCFGx 将读写配置成独立的时序。EXMC_CLK 可以通过 CCK 位来设置。如果 CCK 是 0，当 NOR Flash 使用同步模式时会产生EXMC_CLK；如果 CCK 是 1，当 NOR Flash 同步模式和异步模式都会产生 EXMC_CLK。

## 异步访问时序

模式 1 – SRAM / CRAM


图 33-4. 模式 1 读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/ebab9094c1f7b2bb9e5619ffdade8d9cd02233a7b9639e964b59f510c253ac33.jpg)



图 33-5. 模式 1 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/d5849e475f11f7f95b42a73841f943759a005709505a7267be7d2119e7906cc9.jpg)



表 33-7. 模式 1 相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>取决于用户</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>CPS</td><td>取决于存储器</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于用户</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位 15 为 1 时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>无影响</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>取决于存储器,Nor Flash: 2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x0</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>无影响</td></tr><tr><td>27-24</td><td>DLAT</td><td>无影响</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(写操作为 DSET+1 HCLK 时钟周期,读操作为 DSET+3 HCLK 时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>


模式 A – SRAM / PSRAM(CRAM) OE 翻转


图 33-6. 模式 A 读时序

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/ad7a15ce359b54b11832f189be40245998ba475737348aec969ba4208053e408.jpg)



图 33-7. 模式 A 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/0cb875b8447453738bdef0bea2a35b073e58b5fe1e5bd1eaa8a4048bba97bc03.jpg)


模式 A和模式 1 的区别在于写时序，当两个模式的寄存器有相同的时序配置时，模式 A的写时序独立于读时序。


表 33-8. 模式 A相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>取决于用户</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x1</td></tr></table>


GD32G553 用户手册


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于用户</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位15为1时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>无影响</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>取决于存储器,Nor Flash: 2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x0</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(读)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>无影响</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(读操作为DSET+3 HCLK时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNWTCFGx(写)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>WASYNCMOD</td><td>0x0</td></tr><tr><td>27-20</td><td>保留</td><td>0x0</td></tr><tr><td>19-16</td><td>WBUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>WDSET</td><td>取决于存储器与用户(写操作为WDSET+1 HCLK时钟周期)</td></tr><tr><td>7-4</td><td>WAHLD</td><td>0x0</td></tr><tr><td>3-0</td><td>WASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>


模式 2 / B – NOR Flash



图 33-8. 模式 2 / B 读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/09f8fe81c4ddaf5226a898b2372e6731b7ea699d70679f4ed515d9be9029c9de.jpg)



图 33-9. 模式 2 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/6d0542a942b294998428335ae6fcf527045bc38b2d65011140626b23cb19534b.jpg)



图 33-10. 模式 B 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/49e9175e1885a526d30ae8ccea40f595b0eba697c6dfa61a34f50f11831a4681.jpg)



表 33-9. 模式 2 / B 相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx(模式2,模式B)</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>无影响</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>模式2:0x0,模式B:0x1</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于用户</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位15为1时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>0x1</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>Nor Flash:2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x0</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(模式2读/写操作,模式B读操作)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>模式B:0x1</td></tr><tr><td>27-24</td><td>DLAT</td><td>无影响</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(读操作为DSET+3 HCLK时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>0x0</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNWTCFGx(模式B写操作)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>WASYNCMOD</td><td>模式B:0x1</td></tr><tr><td>27-20</td><td>保留</td><td>0x0</td></tr><tr><td>19-16</td><td>WBUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>WDSET</td><td>取决于存储器与用户(写操作为 WDSET+1 HCLk 时钟周期)</td></tr><tr><td>7-4</td><td>WAHLD</td><td>0x0</td></tr><tr><td>3-0</td><td>WASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>

模式 C – NOR Flash OE 翻转


图 33-11. 模式 C 读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/b1fda6d67d2b5b315c7db0d2f8c4fd0a079a2d8f324f34ae1d0372a497980295.jpg)



图 33-12. 模式 C 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/e93c795d2dcf7f37417d352a651ce4670eab1a2935dab66e8c81ac5224d97b75.jpg)



模式 C 和模式 1 的区别在于写时序，当两个模式的寄存器有相同的时序配置时，模式 C 的写时序独立于读时序并且 NOE和 NADV 的翻转是不同的。



表 33-10. 模式 C 相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>无影响</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x1</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于用户</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位15为1时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>0x1</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>Nor Flash: 2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x0</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(读)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>模式C: 0x2</td></tr><tr><td>27-24</td><td>DLAT</td><td>0x0</td></tr><tr><td>23-20</td><td>CKDIV</td><td>0x0</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户读操作为(DSET+3 HCLk时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>0x0</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNWTCFGx(写)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>WASYNCMOD</td><td>模式C: 0x2</td></tr><tr><td>27-20</td><td>保留</td><td>0x0</td></tr><tr><td>19-16</td><td>WBUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>WDSET</td><td>取决于存储器与用户(写操作为 WDSET+1 HCLK 时钟周期)</td></tr><tr><td>7-4</td><td>WAHLD</td><td>0x0</td></tr><tr><td>3-0</td><td>WASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>

模式 D – 带地址扩展的异步操作


图 33-13. 模式 D 读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/7cfb448840497c6a5592d5bf43a5106cdf13fe020ba25df54d1b290624a3a656.jpg)



图 33-14. 模式 D 写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/cbda5da7538d7b7814e1b91be5c6aaa4a76cb2dcf4d55b6d3f350239e3180522.jpg)



表 33-11. 模式 D 相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>取决于用户</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x1</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于用户</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位15为1时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>取决于存储器</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>取决于存储器</td></tr><tr><td>1</td><td>NRMUX</td><td>0x0</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(读)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>模式D:0x3</td></tr><tr><td>27-24</td><td>DLAT</td><td>无关</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(读操作为DSET+3 HCLK时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>取决于存储器与用户</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNWTCFGx(写)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>WASYNCMOD</td><td>模式D:0x3</td></tr><tr><td>27-20</td><td>保留</td><td>0x0</td></tr><tr><td>19-16</td><td>WBUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>WDSET</td><td>取决于存储器与用户(写操作为 WSET+1 HCLk 时钟周期)</td></tr><tr><td>7-4</td><td>WAHLD</td><td>取决于存储器与用户</td></tr><tr><td>3-0</td><td>WASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>

模式 AM – NOR Flash 地址/数据总线复用


图 33-15. 复用模式读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/6f46725121b69fc6cb1421e9d5d1ab16db6adec82d900ef11f7921a9f33f7fff.jpg)



图 33-16. 复用模式写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/f79ee8259580238bbe2efd8138ff63c14ef18a265724696df8f4495b5bb5d765.jpg)



表 33-12. 复用模式相关寄存器配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>取决于用户</td></tr><tr><td>21</td><td>WFIFODIS</td><td>取决于用户</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x0</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>取决于存储器</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>0x0</td></tr><tr><td>12</td><td>WEN</td><td>取决于存储器</td></tr><tr><td>11</td><td>NRWTCFG</td><td>无影响</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>仅当位15为1时有效</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x0</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>0x1</td></tr><tr><td>5-4</td><td>NRW</td><td>取决于存储器</td></tr><tr><td>3-2</td><td>NRTP</td><td>Nor Flash: 2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>无影响</td></tr><tr><td>23-20</td><td>CKDIV</td><td>无影响</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>取决于存储器与用户(写操作为DSET+2 HCLK时钟周期,读操作为DSET+3 HCLK时钟周期)</td></tr><tr><td>7-4</td><td>AHLD</td><td>取决于存储器与用户</td></tr><tr><td>3-0</td><td>ASET</td><td>取决于存储器与用户</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>


异步通信的等待时间：


等待功能由寄存器 EXMC_SNCTL 位 ASYNCWTEN 控制。在访问外部存储器期间，若使能异步

等待功能（ASYNCWTEN=1），数据建立时间将会自动延长。延长时间的计算如下：

若存储器等待信号与 EXMC_NOE / EXMC_NWE 信号对齐：

$$
T _ {\text { DATA\_SETUP }} \geq \max T _ {\text { WAIT\_ASSERTION }} + 4 H C L K\tag{33-1}
$$

若存储器等待信号与 EXMC_NE 信号对齐：

如果

$$
\max T _ {\text { WAIT\_ASSERTION }} \geq T _ {\text { ADDRES\_PHASE }} + T _ {\text { HOLD\_PHASE }}\tag{33-2}
$$

则

$$
T _ {D A T A \_ S E T U P} \geq (\max T _ {W A I T \_ A S S E R T I O N} - T _ {A D D R E S \_ P H A S E} - T _ {H O L D \_ P H A S E}) + 4 H C L K\tag{33-3}
$$

否则

$$
T _ {D A T A \_ S E T U P} \geq 4 H C L K\tag{33-4}
$$


图 33-17. 异步等待有效时的读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/0130b30bb785ae67bcf27f0ec64387ef7d055da5149cce7c3425b2af6a0e6172.jpg)



图 33-18. 异步等待有效时的写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/95ab0bcc2bce8f8fdd9bf753080fc0823d7a37b766480eee96fcf2f868275a3e.jpg)


## 同步访问时序

存储器时钟（EXMC_CLK）与系统时钟（HCLK）关系如下：

$$
\text { EXMC\_CLK } = \frac {\text { HCLK }}{\text { CKDIV } + 1}\tag{33-5}
$$

其中 CKDIV是同步时钟分频比，通过配置寄存器 EXMC_SNTCFGx 中的 CKDIV 位来设置不同的值。

## 1. 数据延迟与 NOR Flash 延迟

数据延迟 DLAT 是指在采样数据之前需要等待的 EXMC_CLK 周期数。它和 NOR 闪存延迟的关系如下：

NOR 闪存延迟不包含 EXMC_NADV，二者之间的关系为：

$$
\mathrm{NOR} \text {闪存延迟} = \mathrm{DLAT} + 2\tag{33-6}
$$

NOR 闪存延迟包含 EXMC_NADV，二者之间的关系为：

$$
\text { NOR   闪存延迟 } = \mathrm{DLAT} + 3\tag{33-7}
$$

注意：

在读访问时，数据延迟由 EXMC_SNTCFGx 寄存器中 DLAT 和 EXMC_SNLATDECx 寄存器中的LATDEC共同决定。具体请参考SRAM / NOR Flash EXMC_SNLATDECxx=0, 1, 2, 3 。

## 2. 数据等待

用户需要保证 EXMC_NWAIT 信号与外部设备一致。该信号通过寄存器 EXMC_SNCTLx 来设置，位 NRWTEN 使能，位 NRWTCFG 决定 EXMC_NWAIT 信号是等待状态同时有效，或者比等待状态提前一个时钟周期有效，位 NRWTPOL 设置 EXMC_NWAIT 信号极性。

在 NOR Flash 的同步突发模式中，当寄存器 EXMC_SNCTLx 位 NRWTEN 置 1，在数据延迟之后后检测到 EXMC_NWAIT 信号。如果 EXMC_NWAIT 有效，在 EXMC_NWAIT 无效之前会一直插入等待时钟。

EXMC_NWAIT 有效极性：

$$
\mathrm{NRWTPOL} = 1, \text { EXMC\_NWAIT   高电平有效 }
$$

$$
\mathrm{NRWTPOL} = 0, \text { EXMC\_NWAIT   低电平有效 }
$$

在同步突发模式中，EXMC_NWAIT 信号有两种配置：

NRWTCFG = 1，EXMC_NWAIT 信号有效时，当前时钟周期数据无效

NRWTCFG = 0，EXMC_NWAIT 信号有效时，下一个时钟周期数据无效，这是复位后的默认配置。

在 EXMC_NWAIT 信号有效的等待周期内，EXMC 会持续的给存储器发送时钟信号，保持片选和输出使能有效，并且忽视总线上的无效数据。

## 3. CRAM 页边界突发传输的自动分组

CRAM1.5中禁止突发传输跨越页边界，EXMC 遇到边界会进行传输的自动分组。为了保证正确的突发分组操作，用户需要在寄存器 EXMC_SNCTLx 位 CPS 中需要设定 CRAM 的页大小。

## 4. 模式 SM – 单次突发传输

对于同步突发传输，如果 AHB 需要的数据为 16 位，则 EXMC 会执行一次长度为 1 的成组传输；如果 AHB 需要的数据为 32 位，则 EXMC 会把这次传输分成 2 次 16 位的传输，即执行一次长度为 2 的突发传输。

对于其他配置，请参考 。

同步复用突发读时序 – NOR, PSRAM(CRAM)


图 33-19. 同步复用突发传输读时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/548bb26406500bbc17ada6b0b4255ab0a7e4e04767ecdbe1e833af3c35d4f3eb.jpg)



表 33-13. 同步复用模式读时序配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr><tr><td>23-22</td><td>BLSET</td><td>无影响</td></tr><tr><td>21</td><td>WFIFODIS</td><td>无影响</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>无影响</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>ASYNCWTEN</td><td>0x0</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>取决于存储器</td></tr><tr><td>12</td><td>WEN</td><td>无影响</td></tr><tr><td>11</td><td>NRWTCFG</td><td>取决于存储器</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NRWTPOL</td><td>取决于存储器</td></tr><tr><td>8</td><td>SBRSTEN</td><td>0x1,突发读使能</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>取决于存储器</td></tr><tr><td>5-4</td><td>NRW</td><td>0x1</td></tr><tr><td>3-2</td><td>NRTP</td><td>取决于存储器,0x1/0x2</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1,取决于存储器与用户</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(读)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>数据延迟</td></tr><tr><td>23-20</td><td>CKDIV</td><td>图33-19.同步复用突发传输读时序设置:0x1, EXMC_CLK=2HCLK</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>无影响</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>无影响</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>取决于存储器与用户</td></tr></table>


同步复用突发写时序 – NOR, PSRAM(CRAM)



图 33-20. 同步复用突发传输写时序


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/98249216-7c91-4a27-bc58-9f400fc40df5/4b5d2397724d6664971fd3a8258da34ae7fedc3ca5ca9ee0f01c1d794a4177e3.jpg)



表 33-14. 同步复用模式写时序配置


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td colspan="3">EXMC_SNCTLx</td></tr><tr><td>31-24</td><td>保留</td><td>0x00</td></tr></table>


GD32G553 用户手册


<table><tr><td>位域/位</td><td>名称</td><td>参考设定值</td></tr><tr><td>23-22</td><td>BLSET</td><td>无影响</td></tr><tr><td>21</td><td>WFIFODIS</td><td>无影响</td></tr><tr><td>20</td><td>CCK</td><td>取决于用户</td></tr><tr><td>19</td><td>SYNCWR</td><td>0x1,同步写使能</td></tr><tr><td>18-16</td><td>保留</td><td>0x0</td></tr><tr><td>15</td><td>AYSNCWAIT</td><td>0x0</td></tr><tr><td>14</td><td>EXMODEN</td><td>0x0</td></tr><tr><td>13</td><td>NRWTEN</td><td>取决于存储器</td></tr><tr><td>12</td><td>WEN</td><td>0x1</td></tr><tr><td>11</td><td>NRWTCFG</td><td>0x0(这里必须为0)</td></tr><tr><td>10</td><td>WRAPEN</td><td>0x0</td></tr><tr><td>9</td><td>NTWTPOL</td><td>取决于存储器</td></tr><tr><td>8</td><td>SBRSTEN</td><td>无影响</td></tr><tr><td>7</td><td>保留</td><td>0x1</td></tr><tr><td>6</td><td>NREN</td><td>取决于存储器</td></tr><tr><td>5-4</td><td>NRW</td><td>0x1</td></tr><tr><td>3-2</td><td>NRTP</td><td>0x1</td></tr><tr><td>1</td><td>NRMUX</td><td>0x1,取决于用户</td></tr><tr><td>0</td><td>NRBKEN</td><td>0x1</td></tr><tr><td colspan="3">EXMC_SNTCFGx(写)</td></tr><tr><td>31-30</td><td>保留</td><td>0x0</td></tr><tr><td>29-28</td><td>ASYNCMOD</td><td>0x0</td></tr><tr><td>27-24</td><td>DLAT</td><td>数据延迟</td></tr><tr><td>23-20</td><td>CKDIV</td><td>图33-20.同步复用突发传输写时序设置:0x1, EXMC_CLK=2HCLK</td></tr><tr><td>19-16</td><td>BUSLAT</td><td>EXMC_NE[x]上升沿到下降沿的时间</td></tr><tr><td>15-8</td><td>DSET</td><td>无影响</td></tr><tr><td>7-4</td><td>AHLD</td><td>无影响</td></tr><tr><td>3-0</td><td>ASET</td><td>无影响</td></tr><tr><td colspan="3">EXMC_SNLATDECx</td></tr><tr><td>31-3</td><td>保留</td><td>0x0</td></tr><tr><td>2-0</td><td>LATDEC</td><td>无影响</td></tr></table>

## 写 FIFO 支持

写数据 FIFO 用于加速 AHB对外部存储器的写访问，详细信息请参阅 EXMC_SNCTL 寄存器中的WFIFODIS 位。

由于 FIFO 的最大深度为 16，建议使用不大于 16 的突发大小。在 FIFO 模式下（默认模式），当

FIFO 不为空时，所有控制寄存器的值都不能改变。
