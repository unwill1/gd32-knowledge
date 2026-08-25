## 29. 控制器局域网络（CAN）

## 29.1. 简介

CAN（Controller Area Network）总线是一种可以在无主机情况下实现微处理器和设备之间相互通信的总线标准。CAN 网络接口支持 CAN 总线协议 2.0A/B、ISO11898-1:2015 规范和 BOSCHCAN-FD 规范。

CAN 总线控制器集成了可灵活配置的邮箱系统用于 CAN 帧的发送和接收。邮箱系统包含一组邮箱，用于存储控制数据，时间戳，消息标识符和消息数据，最大支持 32 个邮箱。可将邮箱配置为接收 FIFO，接收 FIFO 具有标识符过滤的功能，可最大支持 104 个扩展标识符的过滤，或者 208个标准标识符的过滤，或者 416 个对标识符部分 8 位的过滤，最多有 32 个标识符过滤表元素可通过接收 FIFO/邮箱私有过滤寄存器进行配置。

## 29.2. 主要特征

 支持CAN总线协议2.0A/B；

 遵循ISO 11898-1:2015规范；

 支持CAN FD帧，最大64字节数据，通信波特率最大为8 Mbit/s；

 支持CAN常规帧，最大8字节数据，通信波特率最大为1 Mbit/s；

 支持发送和接收时间戳，基于16位内部计数器；

 支持传输延迟补偿，用于CAN FD帧的高速率数据阶段；

 中断可配置屏蔽；

 支持4种通信模式：正常模式，暂停模式，回环静默模式，和监听模式；

 支持2种省电模式：CAN_Disable模式，和虚拟联网模式；

 支持2种从虚拟联网模式唤醒的方式：唤醒匹配事件，和唤醒超时事件；

■ 最大32个邮箱，此时每个邮箱都配置为8字节数据长度，可灵活配置为发送或接收邮箱；

 支持通过一个特殊帧同步全局网络时间。

## 发送

 支持发送中止；

 发送邮箱状态可查看；

 发送帧消息的CRC校验；

 支持发送优先级：最小邮箱号优先，或最高优先级优先。

## 接收

 接收私有过滤寄存器用于每个接收邮箱或者接收FIFO；

 接收邮箱公有过滤寄存器用于接收邮箱，接收FIFO公有过滤寄存器用于接收FIFO；

 支持接收优先级，可配置在匹配阶段的接收邮箱和接收FIFO的优先级；

 接收FIFO的标识符过滤功能支持最大104个扩展标识符的过滤，或者208个标准标识符的过滤，或者416个对标识符部分8位的过滤；

 深度为6帧的接收FIFO，支持DMA功能。

## 29.3. 功能说明

CAN 模块结构框图如 29-1. CAN 所示。


图 29-1. CAN 模块结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/97bfede2217b30d861249d489e136c02183e39ec12e5bd0437825efcc1feb461.jpg)


CAN 模块包含三个部分：

 协议控制器

协议控制器管理CAN总线上的通信，包括：

MAC（介质访问控制器）：

- 位填充/去填充；

- FD帧的填充位计数；

- 添加CRC；

- 构造MAC帧；

- 检测ACK，发送ACK。

PCS（物理编码子层）：

- 位时间；

- 同步；

- TDC（传输延迟补偿）。

虚拟联网接收匹配：

- 在虚拟联网模式下进行接收匹配。

 控制单元

控制单元主要用于发送和接收的RAM管理，包括：

发送仲裁：

- 找出当前优先级最高的帧。

接收匹配：

按配置顺序将接收移位缓存（一个内部描述符）中的帧数据内容与接收邮箱或者Rx FIFO中的域进行匹配。

邮箱系统控制器：

管理发送和接收的RAM分配，控制邮箱描述符CODE，控制Rx FIFO指针，完成总线对RAM的访问申请。

消息存储在CAN模块专用的RAM区。专用RAM的基地址为模块基地址。

移入/移出：

- 在选择的邮箱描述符 / Rx FIFO描述符与发送或者接收移位缓存之间进行数据搬运。

##  CAN寄存器

CAN寄存器负责完成CAN模块与系统总线的交互。

## 29.3.1. 邮箱描述符

邮箱描述符如 29-1. 64 所示，可用于标准帧（11位标识符）和扩展帧（29位标识符）。每个邮箱可由16字节，24字节，40字节或者72字节组成，分别包含8字节，16字节，32字节或者64字节的数据。偏移地址从0x80到0x27F的RAM区域可用作邮箱。


表 29-1. 64 字节数据的邮箱描述符


<table><tr><td></td><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2">MDES0</td><td>FD</td><td>BR</td><td rowspan="2">ESI</td><td rowspan="2">保留</td><td rowspan="2" colspan="4">CODE[3:0]</td><td rowspan="2">保留</td><td rowspan="2">SR</td><td rowspan="2">IDE</td><td rowspan="2">RTR</td><td rowspan="2" colspan="4">DLC[3:0]</td><td rowspan="2" colspan="15">TIMESTAMP[15:0]</td><td></td></tr><tr><td>F</td><td>S</td><td></td></tr><tr><td>MDES1</td><td colspan="3">PRIO[2:0]</td><td colspan="11">ID_STD[10:0]</td><td colspan="17">ID_EXD[17:0]</td><td></td></tr><tr><td>MDES2</td><td colspan="8">DATA_0[7:0]</td><td colspan="8">DATA_1[7:0]</td><td colspan="6">DATA_2[7:0]</td><td colspan="9">DATA_3[7:0]</td><td></td></tr><tr><td>...</td><td colspan="8">...</td><td colspan="8">...</td><td colspan="6">...</td><td colspan="9">...</td><td></td></tr><tr><td>MDES17</td><td colspan="8">DATA_60[7:0]</td><td colspan="8">DATA_61[7:0]</td><td colspan="6">DATA_62[7:0]</td><td colspan="9">DATA_63[7:0]</td><td></td></tr></table>

## MDES0：邮箱描述符字 0

地址偏移：0x80

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>FDF</td><td>BRS</td><td>ESI</td><td>保留</td><td colspan="4">CODE[3:0]</td><td>保留</td><td>SRR</td><td>IDE</td><td>RTR</td><td colspan="4">DLC[3:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="4">rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TIMESTAMP[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>FDF</td><td>FD 格式指示</td></tr></table>

该位用于区分 CAN常规帧和 CAN FD 帧。

<table><tr><td></td><td></td><td>对于接收邮箱,不需要配置该位,该位用于存储CAN总线上接收到的该位值。</td></tr><tr><td>30</td><td>BRS</td><td>位速率切换该位用于定义CAN FD帧中位速率是否切换到更高的速率。对于接收邮箱,不需要配置该位,该位用于存储CAN总线上接收到的该位值。</td></tr><tr><td>29</td><td>ESI</td><td>错误状态指示位该位指示发送节点是主动错误状态或者被动错误状态。在CAN常规帧中该位保留。对于发送邮箱,主动错误节点发送为显性位,被动错误节点发送为隐性位。对于接收邮箱,不需要配置该位,该位用于存储CAN总线上接收到的该位值。</td></tr><tr><td>28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:24</td><td>CODE[3:0]</td><td>邮箱代码(CODE)该位域可被CPU和CAN模块访问,作为邮箱发送仲裁和接收匹配流程的一部分。代码取值可参考表29-3.接收邮箱CODE和表29-4.发送邮箱CODE。</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>SRR</td><td>替代远程请求该位仅用于扩展帧格式。对于发送邮箱,该位须设置为1(隐性),如果总线发送该位为0(显性),表示该节点发生了仲裁丢失。对于接收邮箱,该位用于存储CAN总线上接收到的该位值。0:在扩展帧中,无效的发送1:在扩展帧中强制发送&#x27;1&#x27;</td></tr><tr><td>21</td><td>IDE</td><td>标识符扩展位该位指示该帧是标准帧还是扩展帧。对于接收邮箱,该位用于存储CAN总线上接收到的该位值。0:帧格式为标准帧1:帧格式为扩展帧</td></tr><tr><td>20</td><td>RTR</td><td>远程传输请求对于发送邮箱:当该位设置为1(隐性),而总线发送该位为0(显性),表示该节点发生了仲裁丢失;当该位设置为0(显性),而总线发送该位为1(隐性),表示发生了位错误;当配置的位值与发送的位值相同,表示一个成功的位传输。对于接收邮箱,该位用于存储CAN总线上接收到的该位值。0:对于发送邮箱,表示当前邮箱有一个数据帧要发送。对于接收邮箱,该位将参与匹配过程。1:对于发送邮箱,表示当前邮箱有一个远程请求帧要发送。对于接收邮箱,表示可能接收到一个远程请求帧。注意:当配置为CAN FD帧时,该位必须配置为0。该位只能用于CAN常规帧。</td></tr><tr><td>19:16</td><td>DLC[3:0]</td><td>数据字节长度代码</td></tr></table>

该位域表示发送帧和接收帧的数据字节长度。

对于接收邮箱，不需要配置该位，该位域将被 CAN总线上接收到的 DLC 域值改写。对于发送邮箱，表示要发送的帧数据字节长度。当 RTR 位为 1 时，有一个远程请求帧要发送，没有数据场，忽略该位域。

该位域是在发送帧或者接收帧的标识符域出现在 CAN总线的时刻，抓取到的内部计数器的值。


表 29-2. DLC 表示的数据字节长度


<table><tr><td>DLC</td><td>数据字节大小</td></tr><tr><td>i (0≤i≤8)</td><td>i (0≤i≤8)</td></tr><tr><td>9</td><td>12</td></tr><tr><td>10</td><td>16</td></tr><tr><td>11</td><td>20</td></tr><tr><td>12</td><td>24</td></tr><tr><td>13</td><td>32</td></tr><tr><td>14</td><td>48</td></tr><tr><td>15</td><td>64</td></tr></table>


表 29-3. 接收邮箱 CODE


<table><tr><td>CODE</td><td>含义</td><td>接收后的CODE</td><td>完成服务(1)</td><td>RRFRMS(2)</td><td>描述</td></tr><tr><td>0b0000</td><td>INACTIVE</td><td>-</td><td>-</td><td>-</td><td>邮箱不参与匹配过程。</td></tr><tr><td>0b0100</td><td>EMPTY</td><td>FULL</td><td>-</td><td>-</td><td>当成功接收了一个帧后(在移入过程之后),CODE域自动更新为FULL。</td></tr><tr><td rowspan="2">0b0010</td><td rowspan="2">FULL</td><td>FULL</td><td>是</td><td rowspan="2">-</td><td>保持为FULL。如果新的一帧在该邮箱完成服务之后移入该邮箱,则邮箱代码保持为FULL。</td></tr><tr><td>OVERRUN</td><td>否</td><td>如果邮箱代码已经为FULL,而在该邮箱完成服务之前又有新的一帧移入该邮箱,则邮箱代码自动更新为OVERRUN。</td></tr><tr><td rowspan="2">0b0110</td><td rowspan="2">OVERRUN</td><td>FULL</td><td>是</td><td rowspan="2">-</td><td>如果邮箱代码为OVERRUN,在邮箱完成服务之后有新的一帧移入了该邮箱,则邮箱代码更新为FULL。</td></tr><tr><td>OVERRUN</td><td>否</td><td>如果邮箱代码为OVERRUN,而有新的一帧必须移入,则该邮箱将再次被覆盖,邮箱代码保持为OVERRUN。</td></tr><tr><td rowspan="2">0b1010</td><td rowspan="2">RANSWER(3)</td><td>TANSWER(0x1110)</td><td rowspan="2">-</td><td>0</td><td>邮箱代码为RANSWER的邮箱用于远程请求帧接收的识别。在接收远程请求帧之后,如果CAN_CTL2寄存器的RRFRMS位为0,则该邮箱将自动设置发送一个响应帧,邮箱代码自动修改为TANSWER。</td></tr><tr><td>-</td><td>1</td><td>邮箱在接收匹配和发送仲裁过程中被忽略。</td></tr><tr><td rowspan="2">CODE[0] = 1</td><td rowspan="2"><eq>BUSY^{(4)}</eq></td><td>FULL</td><td rowspan="2">-</td><td rowspan="2">-</td><td rowspan="2">表示邮箱正在更新。</td></tr><tr><td>OVERRUN</td></tr></table>


1. 完成服务：邮箱被CPU读取过，并且通过读取CAN_TIMER寄存器或者读取其他邮箱的方式解锁了该邮箱。



2. 远程请求帧存储位，参考 2 CAN_CTL2 。



3. 邮箱代码为0b1010的不可被中止。


4. 对于接收邮箱，如果CODE[0]位置位，则对应的邮箱将不参与接收匹配过程。注意，对于Tx邮箱，读取时应该忽略BUSY位，除非设置了CAN_CTL0寄存器中的MST位。


表 29-4. 发送邮箱 CODE


<table><tr><td>CODE</td><td>含义</td><td>发送后的CODE</td><td>RTR</td><td>描述</td></tr><tr><td>0b1000</td><td>INACTIVE</td><td>-</td><td>-</td><td>邮箱不参与发送仲裁过程。</td></tr><tr><td>0b1001</td><td>ABORT</td><td>-</td><td>-</td><td>邮箱不参与发送仲裁过程。</td></tr><tr><td rowspan="2">0b1100</td><td>DATA</td><td>INACTIVE</td><td>0</td><td>发送数据帧。在发送之后,该邮箱自动更新为INACTIVE状态。</td></tr><tr><td>REMOTE</td><td>EMPTY</td><td>1</td><td>发送远程请求帧。在发送之后,该邮箱自动变为相同标识符的接收空邮箱。</td></tr><tr><td>0b1110</td><td>TANSWER</td><td>RANSWER</td><td>-</td><td>当接收到一个匹配的远程请求帧,控制单元会自动改写邮箱的CODE到一个中间态CODE,TANSWER。在发送远程应答帧之后,邮箱将自动恢复到RANSWER状态。对邮箱手动设置TANSWER会有相同的效果。根据RTR位的值,远程应答帧可以是一个数据帧或者新的一个远程请求帧。</td></tr></table>

## MDES1：邮箱描述符字 1

地址偏移：0x84

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">PRIO[2:0]</td><td colspan="11">ID_STD[10:0]</td><td colspan="2">ID_EXD[17:16]</td></tr><tr><td colspan="3">rw</td><td colspan="11">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_EXD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>PRIO[2:0]</td><td>本地优先级该位域只有当CAN_CTL0寄存器的LAPRIOEN位为1时才适用。该位域仅用于发送邮箱,但在发送消息时不发送这些位,它们附加到标识符之前,共同用作发送优先级的判断。</td></tr><tr><td>28:18</td><td>ID_STD[10:0]</td><td>标准帧的标识符对于标准帧,这11个有效意义位用作发送接收帧的标识符。邮箱描述符字1的低18位忽略不用。</td></tr><tr><td>17:0</td><td>ID_EXD[17:0]</td><td>扩展帧的标识符对于扩展帧,ID_STD[10:0]和这18位共同用作发送接收帧的标识符。</td></tr></table>

## MDESx：邮箱描述符字 x（x = 2..17）

地址偏移：0x80 + 0x04 * x（x = 2..17）

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DATA_i[7:0]</td><td colspan="8">DATA_i+1[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DATA_i+2[7:0]</td><td colspan="8">DATA_i+3[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DATA_i[7:0]</td><td>数据字节i(i=4*x-8)参考 DATA_i+3[7:0]描述。</td></tr><tr><td>23:16</td><td>DATA_i+1[7:0]</td><td>数据字节i+1(i=4*x-8)参考 DATA_i+3[7:0]描述。</td></tr><tr><td>15:8</td><td>DATA_i+2[7:0]</td><td>数据字节i+2(i=4*x-8)参考 DATA_i+3[7:0]描述。</td></tr><tr><td>7:0</td><td>DATA_i+3[7:0]</td><td>数据字节i+3(i=4*x-8)一个数据帧最大包含64个字节数据,主要由邮箱的DLC值决定。对于接收帧,该位域用于存储CAN总线上接收到的数据。</td></tr></table>

## 邮箱编号

当接收FIFO禁能时，专用的RAM空间只被邮箱占用，因此邮箱编号与邮箱描述符编号相同，邮箱描述符编号按整个邮箱描述符为单位递增，每个邮箱描述符的数据可以是8字节，16字节，32字节或者64字节。

当接收FIFO使能时（CAN FD模式处于禁能状态，因此数据是8字节长度），专用的RAM空间同时被邮箱和FIFO占用，因此统一以8字节数据的邮箱描述符为单位进行描述符计数编号，那么邮箱编号就是邮箱描述符所占用的计数编号。

## CAN FD 模式下邮箱数目

当CAN FD模式使能时，由CAN_FDCTL寄存器的MDSZ[1:0]位域来配置邮箱的数目，决定512字节的RAM空间的分配。


表 29-5. 邮箱数目


<table><tr><td>MDSZ[1:0]</td><td>数据字节大小</td><td>邮箱数目</td></tr><tr><td>0b00</td><td>8</td><td>32</td></tr><tr><td>0b01</td><td>16</td><td>21</td></tr><tr><td>0b10</td><td>32</td><td>12</td></tr><tr><td>0b11</td><td>64</td><td>7</td></tr></table>

## 29.3.2. 接收 FIFO描述符

接收FIFO描述符如 29-6. FIFO 所示。

当CAN_CTL0寄存器的RFEN位为1时，按8字节的数据载荷计数，通常被邮箱编号0-5占用的RAM空间被用于接收FIFO。FDES0 – FDES3包含最早接收到的还未被CPU读取的消息。偏移地址从0x90到0xDC的RAM空间保留给FIFO内部使用。

当CAN_CTL0寄存器的RFEN位为1时，按8字节的数据载荷计数，通常被邮箱编号6-31占用的RAM空间被用作标识符过滤器表（可配置为8到104个过滤元素），用于FIFO接收匹配过程。

复位时默认标识符过滤表包含8个过滤元素，从FDES4到FDES11。


表 29-6. 接收 FIFO 描述符


<table><tr><td>FDES0</td><td colspan="3">IDFMN[8:0]</td><td>SRR</td><td>IDE</td><td>RTR</td><td colspan="2">DLC[3:0]</td><td colspan="2">TIMESTAMP[15:0]</td></tr><tr><td>FDES1</td><td>保留</td><td colspan="6">ID_STD[10:0]</td><td colspan="3">ID_EXD[17:0]</td></tr><tr><td>FDES2</td><td colspan="2">DATA_0[7:0]</td><td colspan="5">DATA_1[7:0]</td><td colspan="2">DATA_2[7:0]</td><td>DATA_3[7:0]</td></tr><tr><td>FDES3</td><td colspan="2">DATA_4[7:0]</td><td colspan="5">DATA_5[7:0]</td><td colspan="2">DATA_6[7:0]</td><td>DATA_7[7:0]</td></tr><tr><td>0x90-0xDC</td><td colspan="10">保留</td></tr><tr><td>FDES4</td><td colspan="10">标识符过滤元素0</td></tr><tr><td>...</td><td colspan="10">...</td></tr><tr><td>FDES107</td><td colspan="10">标识符过滤元素103</td></tr></table>

## FDES0：接收 FIFO 描述符字 0

地址偏移：0x80

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4"></td><td colspan="5">IDFMN[8:0]</td><td>SRR</td><td>IDE</td><td>RTR</td><td></td><td colspan="3">DLC[3:0]</td></tr><tr><td colspan="4"></td><td colspan="5">r</td><td>r</td><td>r</td><td>r</td><td></td><td colspan="3">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TIMESTAMP[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>IDFMN[8:0]</td><td>标识符过滤元素匹配序号该位域表示在接收FIFO输出中的消息是与哪个标识符过滤元素相匹配。</td></tr><tr><td>22</td><td>SRR</td><td>替代远程请求该位仅用于扩展帧格式。对于接收,该位将存储CAN总线上接收到的该位值。</td></tr><tr><td>21</td><td>IDE</td><td>标识符扩展位该位指示了该帧是标准帧还是扩展帧。0: 帧格式为标准帧1: 帧格式为扩展帧</td></tr><tr><td>20</td><td>RTR</td><td>远程传输请求0: 接收数据帧1: 接收远程帧</td></tr><tr><td>19:16</td><td>DLC[3:0]</td><td>数据字节长度代码该位域表示接收帧的数据字节长度。对于接收邮箱,不需要配置该位,该位域将被CAN总线上接收到的DLC域值改写。</td></tr><tr><td>15:0</td><td>TIMESTAMP[15:0]</td><td>时间戳该位域是在接收帧的标识符域出现在CAN总线的时刻,抓取到的内部计数器的值。</td></tr></table>


FDES1：接收 FIFO 描述符字 1



地址偏移：0x84


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="11">ID_STD[10:0]</td><td colspan="2">ID_EXD[17:16]</td></tr><tr><td colspan="3"></td><td colspan="11">r</td><td colspan="2">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_EXD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:18</td><td>ID_STD[10:0]</td><td>标准帧的标识符对于标准帧,这11个有效意义位用作接收帧的标识符。邮箱描述符字1的低18位忽略不用。</td></tr><tr><td>17:0</td><td>ID_EXD[17:0]</td><td>扩展帧的标识符对于扩展帧,ID_STD[10:0]和这18位共同用作接收帧的标识符。</td></tr></table>

## FDES2：接收 FIFO 描述符字 2

地址偏移：0x88

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DATA_0[7:0]</td><td colspan="8">DATA_1[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DATA_2[7:0]</td><td colspan="8">DATA_3[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DATA_0[7:0]</td><td>数据字节 0参考 DATA_3[7:0]描述。</td></tr><tr><td>23:16</td><td>DATA_1[7:0]</td><td>数据字节 1参考 DATA_3[7:0]描述。</td></tr><tr><td>15:8</td><td>DATA_2[7:0]</td><td>数据字节 2参考 DATA_3[7:0]描述。</td></tr><tr><td>7:0</td><td>DATA_3[7:0]</td><td>数据字节 3一个数据帧最大包含 8 个字节数据,主要由邮箱的 DLC 值决定。接收 FIFO 不支持接收 FD 帧。</td></tr></table>


FDES3：接收 FIFO 描述符字 3



地址偏移：0x8C


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DATA_4[7:0]</td><td colspan="8">DATA_5[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DATA_6[7:0]</td><td colspan="8">DATA_7[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DATA_4[7:0]</td><td>数据字节 4参考 DATA_7[7:0]描述。</td></tr><tr><td>23:16</td><td>DATA_5[7:0]</td><td>数据字节 5参考 DATA_7[7:0]描述。</td></tr><tr><td>15:8</td><td>DATA_6[7:0]</td><td>数据字节 6参考 DATA_7[7:0]描述。</td></tr><tr><td>7:0</td><td>DATA_7[7:0]</td><td>数据字节 7一个数据帧最大包含 8 个字节数据,主要由邮箱的 DLC 值决定。接收 FIFO 不支持接收 FD 帧。</td></tr></table>

## FDESx：接收 FIFO 描述符字 x（x = 4..107）

地址偏移：0xE0 + 4 * (x - 4)

该描述符字给出了标识符过滤元素的3种不同格式，可以通过CAN_CTL0寄存器的FS[1:0]位域来配置。

注意：所有的标识符过滤元素只能同时使用同一种格式，不同的格式不能混合在一个标识符过滤器表中使用。

格式A模式：

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">RTR_A</td><td rowspan="2">IDE_A</td><td rowspan="2">保留</td><td colspan="11">ID_STD_A[10:0]</td><td colspan="2">保留</td></tr><tr><td colspan="13">ID_EXD_A[28:16]</td></tr><tr><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">ID_EXD_A[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>RTR_A</td><td>格式A远程帧该位指示了是否接收匹配的远程帧到FIFO。0: 远程帧都被拒绝,只存储数据帧1: 数据帧都被拒绝,只存储远程帧</td></tr><tr><td>30</td><td>IDE_A</td><td>格式A标识符扩展位该位指示了是否接收匹配的扩展帧到FIFO。0: 扩展帧都被拒绝,只存储标准帧1: 标准帧都被拒绝,只存储扩展帧</td></tr><tr><td>29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:0</td><td>ID_STD_A[10:0]/ID_EXD_A[28:0]</td><td>格式A标识符该位域指示一个用于接收FIFO匹配过程的完整的标识符(标准格式或者扩展格式)。如果IDE_A为0,则18到28位用作标准格式标识符,其余位保留;否则,所有位用作扩展格式标识符。</td></tr></table>


格式B模式：


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td rowspan="2">RTR_B0</td><td rowspan="2">IDE_B0</td><td colspan="11">ID_STD_B_0[10:0]</td><td colspan="3">保留</td></tr><tr><td colspan="14">ID_EXD_B_0[13:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="14">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2">RTR_B1</td><td rowspan="2">IDE_B1</td><td colspan="11">ID_STD_B_1[10:0]</td><td colspan="3">保留</td></tr><tr><td colspan="14">ID_EXD_B_1[13:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>RTR_B0</td><td>格式B远程帧0该位指示了是否接收匹配的远程帧到FIFO。0:远程帧都被拒绝,只存储数据帧1:数据帧都被拒绝,只存储远程帧</td></tr><tr><td>30</td><td>IDE_B0</td><td>格式B标识符扩展位0该位指示了是否接收匹配的扩展帧到FIFO。0:扩展帧都被拒绝,只存储标准帧1:标准帧都被拒绝,只存储扩展帧</td></tr><tr><td>29:16</td><td>ID_STD_B_0[10:0]/ID_EXD_B_0[13:0]</td><td>格式B标识符0该位域指示一个用于接收FIFO匹配过程的完整的标准格式标识符或者扩展格式标识符其中14位。如果IDE_B0位为0,则19到29位用作标准格式标识符,其余位保留;否则,这些位都用作扩展格式标识符其中14位,其与接收到的标识符的最高有效14位进行比较。</td></tr><tr><td>15</td><td>RTR_B1</td><td>格式B远程帧1参考RTR_B0描述。</td></tr><tr><td>14</td><td>IDE_B1</td><td>格式B标识符扩展位1参考IDE_B0描述。</td></tr></table>

13:0 

ID_STD_B_1[10:0]/ 格式 B 标识符 1

ID_EXD_B_1[13:0] 参考 ID_STD_B_0[10:0]/ ID_EXD_B_0[13:0]描述。

格式C模式：

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">ID_C_0[7:0]</td><td colspan="8">ID_C_1[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>rw</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ID_C_2[7:0]</td><td colspan="8">ID_C_3[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>ID_C_0[7:0]</td><td>格式C标识符0该位域指示一个用于接收FIFO匹配过程的标准格式标识符其中8位,或者扩展格式标识符其中8位。在标准格式帧和扩展格式帧中,这8位都是与其接收到的标识符的最高有效8位进行比较。</td></tr><tr><td>23:16</td><td>ID_C_1[7:0]</td><td>格式C标识符1参考ID_C_0[7:0]描述。</td></tr><tr><td>15:8</td><td>ID_C_2[7:0]</td><td>格式C标识符2参考ID_C_0[7:0]描述。</td></tr><tr><td>7:0</td><td>ID_C_3[7:0]</td><td>格式C标识符3参考ID_C_0[7:0]描述。</td></tr></table>

## 29.3.3. 通信模式

CAN接口有四种通信模式：

 正常模式

 暂停模式

 回环静默模式

 监听模式

## 正常模式

在正常模式，消息的接收、发送，以及错误都正常处理，所有的CAN协议功能都使能。

## 暂停模式

为了进入暂停模式，需要将CAN_CTL0寄存器的INAMOD位置位，然后置位CAN_CTL0寄存器的HALT位或者设置芯片进入Debug模式。

当CAN模块发出进入暂停模式的请求后，在INAS位置位前执行了如下几个步骤：

1. 等待总线上连续11位隐性位。

2. 等待当前发送或者接收流程完成，也就是所有内部活动比如仲裁、匹配、移入和移出都完成。挂起的移入流程不影响暂停模式的进入。

3. Tx发送管脚驱动为’1’（隐性电平）。

4. 停止预分频器。

5. 使能CAN_ERR0寄存器的写访问，该寄存器在其他模式中为只读。

6. 置位CAN_CTL0寄存器中的NRDY和INAS位。

当进入了暂停模式时，CAN_CTL0寄存器的INAS位由CAN模块置位。

在暂停模式中，不能发送接收消息，CAN模块预分频器停止工作，所有寄存器都可访问。

为了退出暂停模式，有以下两种方式：

 清除CAN_CTL0寄存器的INAMOD位。

 清除CAN_CTL0寄存器的HALT位，或者芯片退出Debug模式。

当CAN模块发出退出暂停模式的请求后，则在CAN预分频器恢复工作之后，CAN_CTL0寄存器的INAS位被清零。退出暂停模式后，CAN模块通过等待11个连续隐性位尝试恢复与CAN总线的同步。

注意：在暂停模式时，发出进入CAN_Disable模式的请求，或者发出进入虚拟联网模式的请求，会导致CAN_CTL0寄存器的INAS位清零并且CAN_CTL0寄存器的LPS位置位。

## 回环静默模式

为了进入该模式，置位CAN_CTL1寄存器的LSCMOD位。在该模式下，所有发送的消息将内部输回到接收管脚，并且将忽略ACK场中的ACK间隙发送位，以确保能接收到自己发送的消息，同时发送和接收中断都能正常产生。

回环静默模式由于模块自检。Rx接收管脚被忽略，Tx管脚保持为隐性电平。

## 监听模式

为了进入该模式，置位CAN_CTL1寄存器的MMOD位。

在监听模式下，CAN_ERR1寄存器的ERRSI[1:0]位域由CAN模块设为0b01来指示模块此时工作在被动错误状态。在该模式下，所有的错误计数器都被冻结。

在该模式下，发送被禁止，只有被其他CAN节点应答了的消息才能被接收，如果CAN模块检测到一个没有被应答的消息，则位显性错误标志将置位，同时不改变CAN_ERR0寄存器中的

RECNT[7:0]和REFCNT[7:0]位域。

## 29.3.4. 省电模式

CAN接口有两种省电模式：

 CAN_Disable模式

 虚拟联网模式

在这两种省电模式下，专用的RAM以及处于SRAM的寄存器都不能访问。

## CAN_Disable 模式

通过配置CAN_CTL0寄存器的CANDIS位来使能或失能CAN模块。

为了减少电源能耗，当置位CANDIS位来禁能CAN模块时，CAN模块将延迟一段时间后进入CAN_Disable模式，此时CAN_CTL0寄存器的LPS位和NRDY位均置位。

当CAN模块失能时，协议控制器和控制单元的时钟都关闭，寄存器除了CAN_RMPUBF，CAN_RFIFOPUBF，CAN_RFIFOIFMN和CAN_RFIFOMPFx（x = 0..31）都仍可访问，同时专用的RAM也不可访问。

在CAN模块使能后，仍然需要延迟一段时间等待CAN_CTL0寄存器的LPS位清零，以通知协议控制器，CAN模块将请求协议控制器和控制单元恢复时钟。

## 虚拟联网模式

虚拟联网模式用于在省电模式下接收唤醒帧。该模式可与芯片深度睡眠模式一起使用。

为了进入虚拟联网模式，设置CAN_CTL0寄存器的PNMOD位和PNEN位为1，如需要，可以设置MCU进入深度睡眠模式。

在发出虚拟联网模式请求后，执行如下几个步骤：

1. 等待总线处于空闲状态，或者等待帧间隔的第三个位并检查为隐性位。

2. 置位CAN_CTL0寄存器的LPS和PNS位。

3. 请求关闭控制单元的时钟，保持协议控制器时钟运行。

在虚拟联网模式下，控制单元时钟被关闭，而协议控制器保持运行（如果MCU也进入了深度睡眠模式，则需要事先将CAN协议控制器的时钟源配置为IRC8M，否则CAN协议控制器将丢失时钟而无法继续运行），从而可以继续接收并过滤消息。在该模式下不进行匹配、仲裁、移入和移出流程。

为了退出虚拟联网模式，可按以下方式：

 当检测到一个唤醒事件，发生了唤醒中断。清除CAN_CTL0寄存器的PNMOD位和PNEN位。

 清除CAN_CTL0寄存器的PNMOD位和PNEN位。

当CAN模块发出退出虚拟联网模式请求后，CAN模块将等待总线处于空闲状态或者等待帧间隔的第三个位到来时清零CAN_CTL0寄存器的LPS位和PNS位，恢复到正常模式，CAN模块将重新与CAN总线同步。

## 29.3.5. 数据发送

对于发送，应用了仲裁机制来决定发送邮箱的优先级是根据消息标识符（PRIO域也可配置参与到发送仲裁中）还是邮箱编号。

CAN FD模式下的邮箱数目由CAN_FDCTL寄存器的MDSZ[1:0]位域来决定，参考 29-5.。

## 发送流程

为了发送一个CAN帧，需要按如下步骤准备一个发送邮箱：

1. 检查相应邮箱在CAN_STAT寄存器的状态MSx位是否置位，并清除位。

2. 如果邮箱是激活状态（不论是发送邮箱还是接收邮箱），则按 或来失活该邮箱。当执行了发送邮箱失活操作，则按后续的步骤继续操作。如果执行了接收邮箱失活操作，跳到步骤6。如果邮箱是失活状态（不论是发送邮箱还是接收邮箱），则跳到步骤6。

3. 轮询CAN_STAT寄存器，等待相应MSx位置位，或者置位CAN_INTEN寄存器中相应的MIEx位使能相应的中断，通过中断请求处理。

4. 读CODE域来获取邮箱状态（中止的，或者已发送）。

5. 清零CAN_STAT寄存器的相应标志位MSx位。

6. 写邮箱MDES1字的标识符域（当CAN_CTL0寄存器的LAPRIOEN位置位时，也包括邮箱的PRIO域）。

7. 写邮箱MDESx（x = 2..17）字的载荷数据字节。

8. 配置邮箱MDES0字的IDE，RTR，FDF，BRS，ESI和DLC域。

9. 设置邮箱CODE域为0b1100，来激活邮箱发送帧。当邮箱被激活后，它将会参与仲裁过程，并根据其优先级最终发送到总线上。当邮箱的数据字节数目小于邮箱的DLC域值，CAN会附加一些常数字节0xCC以匹配期望的DLC值。

在一次成功的帧发送之后，CODE域将自动更新，并且TIMESTAMP域也将自动更新为内部计数器的值；CRC寄存器（CAN_CRCC寄存器和CAN_CRCCFD寄存器）将自动更新，CAN_STAT寄存器中相应的MSx位将置位，如果CAN_INTEN寄存器中相应的MIEx中断使能位置位了，则将产生一个中断。

## 仲裁过程

如果有多个发送邮箱处于挂起状态，则仲裁机制将会从最小邮箱编号到最大邮箱编号的方向进行搜索，找到最大优先级的邮箱进行发送。仲裁算法由CAN_CTL1寄存器的MTO位来控制选择。

当满足下列情况中任意一种，则开始一次仲裁过程：

 CAN总线上的CRC场：CRC场第一个位后，延迟ASD[4:0]（在CAN_CTL2寄存器中）个CAN位。

 CAN总线上错误界定符或者过载界定符。

CAN总线从离线状态恢复：在TECNT[7:0]计数器计到124之后，延迟ASD[4:0]（在CAN_CTL2寄存器中）个CAN位。从离线状态恢复需要128次连续的11位隐性位，而这是由CAN_ERR0寄存器的TECNT[7:0]计数器来计数的。

 退出暂停模式，或者退出省电模式（CAN_Disable模式和虚拟联网模式）。

 重写仲裁获胜（暂时获胜或者最终获胜）邮箱MDES0字。

重写搜索过的（仲裁正在进行中）邮箱MDES0字：如果搜索完毕之后没有找到获胜邮箱，则仲裁将马上重新开始；否则，仲裁过程结束。

写任意邮箱的MDES0字：如果没有仲裁正在进行，并且没有仲裁获胜邮箱存在，同时CAN总线不在数据帧/远程帧的SOF-DATA / SOF-Control或者错误帧/过载帧的错误标志/过载标志，则开始仲裁过程。

CAN节点进入总线集成状态（参考 ）：进入该状态后，延迟ASD[4:0]（在CAN_CTL2寄存器中）个CAN位。

当满足下列情况中任意一种，则停止仲裁过程：

 所有邮箱都被搜索过。

■ 当CAN_CTL1寄存器MTO位置位，最小邮箱编号优先时，找到了一个激活的发送邮箱。

 CAN总线上错误标志或者过载标志。

 CAN总线上下一帧的SOF。

 当发出进入暂停模式，CAN_Disable模式或者虚拟联网模式请求。

## 最小邮箱编号优先

如果CAN_CTL1寄存器的MTO位置位，则最小邮箱编号优先发送，此时CAN_CTL0寄存器的LAPRIOEN位不起作用。

## 最高优先级优先

如果CAN_CTL1寄存器的MTO位清零，则最高优先级的邮箱优先发送。最高优先级的发送邮箱在所有发送邮箱中具有最小的仲裁值（参考 29-7. 32 和29-8. 35 ）。如果有超过一个邮箱具有相等的仲裁值，则更小邮箱编号的邮箱为仲裁获胜者。

当CAN_CTL0寄存器的LAPRIOEN位清零，本地优先级禁用时，参与到仲裁过程的位都将最终被发送到CAN总线上，如 29-7. 32 所示。

当CAN_CTL0寄存器的LAPRIOEN位置位，本地优先级使能时，则邮箱PRIO域将参与到内部仲裁过程。如 29-8. 35 所示，邮箱PRIO域为仲裁值的最高有效位部分，因此具有低PRIO域值的邮箱比高PRIO域值的邮箱具有更高的优先级，忽略剩余的仲

裁值，但PRIO域不会最终发送到CAN总线上。


表 29-7. 当本地优先级禁用时的邮箱仲裁值（32 位）


<table><tr><td>ID_STD[10:0]</td><td>RTR</td><td>IDE</td><td colspan="2">保留</td></tr><tr><td>ID_EXD[28:18]</td><td>SRR</td><td>IDE</td><td>ID_EXD[17:0]</td><td>RTR</td></tr></table>


表 29-8. 当本地优先级使能时的邮箱仲裁值（35 位）



IDE 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0


<table><tr><td>0</td><td>PRIO[2:0]</td><td>ID_STD[10:0]</td><td>RTR</td><td>IDE</td><td colspan="2">保留</td></tr><tr><td>1</td><td>PRIO[2:0]</td><td>ID_EXD[28:18]</td><td>SRR</td><td>IDE</td><td>ID_EXD[17:0]</td><td>RTR</td></tr></table>

## 仲裁启动延迟

仲裁启动延迟由CAN_CTL2寄存器的ASD[4:0]位域来配置，用于优化当仲裁过程结束的太早，可能导致仲裁获胜的发送邮箱被CPU重写，从而导致仲裁过程被重启，因而不能及时地发送出去的过程。

## 移出

移出过程是在找到仲裁获胜邮箱后，将获胜发送邮箱中的内容拷贝到发送移位缓存（一个内部邮箱描述符）的过程。发送移位缓存中的消息将按照CAN协议规则进行发送。

当移出过程完成后，即使CAN_CTL0寄存器的MST位置位，对相应发送邮箱的MDES0字的写操作都将被阻塞。当符合下述中的一种情形时，将恢复对相应发送邮箱的MDES0字的写操作：

 在邮箱发送完毕，并且CAN_STAT寄存器中相应的标志位MSx被清零。

 CAN节点进入暂停模式或者离线状态。

 CAN节点在总线仲裁中失利，或者在发送过程中发生了一个错误。

当符合下述中的一种情形时，将启动移出过程：

 CAN总线上帧间隔的第一个位。

 处于总线空闲状态。

 处于等待总线空闲状态。

在移出过程中，CPU在总线空闲状态可优先访问相应的内存，移出操作对相应的内存具有较低的访问权限。

## 中止

为了请求发送中止，推荐的操作为首先置位CAN_CTL0寄存器的MST位，然后对邮箱的CODE域写ABORT（0b1001）。

如果邮箱不是仲裁获胜邮箱，或者邮箱是仲裁获胜邮箱，但还未完成移出过程，则对该邮箱MDES0字写ABORT（0b1001）的操作可以成功，CAN_STAT寄存器中对应的MSx位将置位。

如果邮箱是仲裁获胜邮箱，且移出过程已经完成，或者邮箱正在发送，则对邮箱MDES0字写ABORT（0b1001）的操作将被阻塞。在这种情况下，发送中止请求会被保存并保持挂起，直到帧被成功发送出去或者发送失败：

帧被成功发送，邮箱未被中止：如果帧最终发送成功，则挂起的中止请求会自动清除，CAN_STAT寄存器中对应的MSx位将置位，如果CAN_INTEN寄存器的MIEx位置位，则会触发一个中断。

发送失败，邮箱被中止：如果帧最终发送失败，则挂起的中止请求会收到应答信号，对邮箱的写操作将会恢复，邮箱的MDES0字被改写为ABORT，CAN_STAT寄存器中对应的MSx位将置位，如果CAN_INTEN寄存器的MIEx位置位，则会触发一个中断。

当符合下述中的一种情形时，帧发送失败：

- 总线仲裁失利。

- 发送过程中发生一个错误。

- 进入离线状态。

- 总线有一个过载帧。

## 发送邮箱失活

发送邮箱失活的操作：

 对发送邮箱的MDES0字CODE域写ABORT。这是推荐的邮箱失活操作，不会造成不可知的发送。

该操作必须首先确保CAN_CTL0寄存器的MST位置位。

## 29.3.6. 数据接收

对于CAN常规帧，支持通过FIFO和邮箱来接收帧。

对于CAN FD帧，仅支持通过邮箱来接收帧。

## 邮箱接收

对于邮箱接收，只有当帧的标识符与邮箱标识符域中配置的ID（或者当使用了过滤寄存器时，是一组邮箱ID）相匹配时，才会将帧接收存储到邮箱中。

为了将CAN帧接收到邮箱中去，必须按如下步骤准备一个接收邮箱：

1. 如果邮箱是激活状态（不论是发送邮箱还是接收邮箱），则按 或来失活该邮箱。当执行了发送邮箱失活操作，则按后续的步骤继续操作。如果执行了接收邮箱失活操作，跳到步骤4。如果邮箱是失活状态（不论是发送邮箱还是接收邮箱），则跳到步骤4。

2. 轮询CAN_STAT寄存器，等待相应MSx位置位，或者置位CAN_INTEN寄存器中相应的MIEx位使能相应的中断，通过中断请求处理。

3. 读回CODE域来确保邮箱状态是已中止，还是已发送。

4. 清零CAN_STAT寄存器的相应标志位MSx位。

5. 写邮箱MDES1字的标识符域，如果需要，配置MDES0字的IDE，RTR域。

6. 设置邮箱MDES0字CODE域为EMPTY（0b0100）来激活邮箱。

在一次成功的接收之后，邮箱描述符所有位（DATA，ID，TIMESTAMP，SRR，IDE，RTR，FDF，BRS，ESI，DLC，CODE）都存储为总线上接收到的相应位或者进行了自动更新，CAN_STAT寄存器的相应标志位MSx位置位，如果CAN_INTEN寄存器中相应的MIEx中断使能位置位了，则将产生一个中断。TIMESTAMP域将自动更新为帧的标识符域第二位时刻的内部计数器的值。

为了服务（读）接收邮箱，推荐的操作步骤如下所示：

1. 轮询CAN_STAT寄存器，等待相应MSx位置位，或者置位CAN_INTEN寄存器中相应的MIEx位使能相应的中断，通过中断请求处理。

2. 读邮箱MDES0字，轮询CODE域BUSY位，等待其清零。当BUSY位为0时，读邮箱操作将会锁定邮箱，而使邮箱不会被改写。

3. 读邮箱内容。

4. 清零CAN_STAT寄存器的相应标志位MSx位。

5. 读取CAN_TIMER寄存器来解锁邮箱。

## 邮箱锁定

锁定机制仅适用于接收邮箱：对于CODE域为接收FULL或者接收OVERRUN的邮箱，CPU对邮箱MDES0字的读操作将会锁定该邮箱，从而阻止新的一个匹配报文对邮箱内容进行改写。

通过读CAN_TIMER寄存器（全局解锁操作）或者对其他邮箱MDES0字的读操作可以解锁邮箱。当邮箱被解锁后，如果有未处理的报文，则将开始一个移入过程（在暂停模式下具有相同解锁功能，而当CAN_CTL0寄存器的LPS位置位时解锁邮箱，将要等到LPS位清零才会开始一个移入过程）。

如果邮箱没有及时地解锁，而又接收到一个新的匹配报文，则新的报文将会覆盖接收移位缓存，并且邮箱CODE不会有报文丢失的提示，也没有相应的错误状态的记录。

注意：邮箱失活（对邮箱CODE写接收INACTIVE或者发送ABORT）相比于邮箱锁定具有更高的优先级。

## 接收邮箱失活

失活接收邮箱的方式：

 对接收邮箱MDES0字CODE域写INACTIVE（接收INACTIVE或者发送INACTIVE）。但这个操作可能会导致一个新的匹配报文的丢失且没有相应提示。

注意：接收邮箱失活操作将会自动解锁该邮箱。接收FIFO没有相应的锁定写保护机制。

## Rx FIFO 接收

Rx FIFO深度为6帧。当CAN_CTL0寄存器的RFEN位置位时，使能Rx FIFO用于帧接收。Rx FIFO只能用于接收，且不能在CAN FD模式使能的时候使用。Rx FIFO描述符参考 29-6. FIFO。CAN过滤系统提供了对一组标识符的过滤功能，有效地降低中断服务的负担。Rx FIFO过滤器的数目可通过CAN_CTL2寄存器的RFFN[3:0]位域来配置，最大支持32个过滤器，对应的过滤器相关参数可通过CAN_RFIFOMPFx（x = 0..31）寄存器（如果CAN_CTL0寄存器的RPFQEN位置位），或者CAN_RFIFOPUBF和CAN_RFIFOMPFx（x = 0..31）寄存器（如果CAN_CTL0寄存器的RPFQEN位清零）来配置。

Rx FIFO有未读消息时：如果CAN_STAT寄存器的MS5_RFNE位置位，则可通过FDES0-FDES3字来读取接收到的消息。当CAN_STAT寄存器的MS5_RFNE位置位，意味着Rx FIFO中至少有一个可读的消息。如果CAN_INTEN寄存器相应的中断使能位MIEx置位，则将产生一个中断；如果CAN_CTL0寄存器的DMAEN位置位，MS5_RFNE位将会产生一个DMA传输请求，而不会产生RxFIFO中断。

 通过CPU方式服务（读取）Rx FIFO，推荐按如下步骤操作：

1. 轮询CAN_STAT寄存器，直到MS5_RFNE标志置位，或者置位CAN_INTEN寄存器中MIE5位使能中断，通过中断请求处理。

2. 读取Rx FIFO的FDES0-FDES3字，并按需要来读取CAN_RFIFOIFMN寄存器。

3. 清除CAN_STAT寄存器的MS5_RFNE标志位。如果Rx FIFO中包含多个消息，则对MS5_RFNE标志位的清除操作会将Rx FIFO的FDES0-FDES3字更新为下一个消息，而CAN_RFIFOIFMN寄存器也在同时更新，MS5_RFNE标志位仍然保持置位，如果使能了中断，则会又产生一个中断，重复步骤2-3来读取接收到的消息。

 通过DMA方式服务（读取）Rx FIFO，推荐按如下步骤操作：

1. 配置DMA控制器并使能相应通道用于Rx FIFO消息接收。

2. 通过CPU方式服务（读取）Rx FIFO，直到CAN_STAT寄存器的MS5_RFNE标志被清零，以避免在DMA使能后有额外的DMA请求产生。

3. 使能CAN_CTL0寄存器的DMAEN位来使能DMA请求。

4. 等待DMA请求。当CAN_STAT寄存器的MS5_RFNE标志位置位时将产生一个DMA请求。

5. 在接收到DMA请求后，DMA控制器将会自动读取Rx FIFO的FDES0-FDES3字。必须读取FDES3字才能清除CAN_STAT寄存器的MS5_RFNE标志位，如果Rx FIFO中包含多个消息，读FDES3字的操作会使Rx FIFO的FDES0-FDES3字更新为下一个消息，而CAN_RFIFOIFMN寄存器（需要在读FDES3字之前读取）也会同时更新，MS5_RFNE标志位仍然保持置位，并再次产生一个DMA请求。重复步骤4-5。

## DMA 模式

当CAN_CTL0寄存器的RFEN位和DMAEN位都置位时，可使用DMA模式来处理Rx FIFO接收。当使能了DMA模式时，就不能再使用CPU方式来读取Rx FIFO。

当使能了DMA模式时，如果Rx FIFO中有未读消息，DMA控制器将会自动读取Rx FIFO的FDES0-FDES3字来读取接收的消息。在这种模式下，CAN_STAT寄存器中的Rx FIFO警告标志位MS6_RFW和Rx FIFO溢出标志位MS7_RFO都用作保留位。

在通过清零CAN_CTL0寄存器的DMAEN位来禁能DMA模式之前，必须执行一个清FIFO内容的操作（当CAN_CTL0寄存器的RFEN位置位时，在暂停模式下对CAN_STAT寄存器的MS0位写1）。清FIFO的操作将会清除CAN_STAT寄存器的MS5_RFNE位，并取消DMA请求。

## 清 FIFO

当Rx FIFO使能（CAN_CTL0寄存器的RFEN位置位）后，通过在暂停模式下对CAN_STAT寄存器的MS0位写1来清除Rx FIFO的内容，但Rx FIFO的标志位不会被清除（DMA模式下除外）。因此在清FIFO操作之前，需要通过读取Rx FIFO直到将CAN_STAT寄存器的MS5_RFNE标志位清零。

## 标志

## Rx FIFO非空

当CAN_STAT寄存器的MS5_RFNE位置位时，表示Rx FIFO中至少有一个可读消息。

## Rx FIFO警告

当CAN_STAT寄存器的MS6_RFW位置位时，表示Rx FIFO又接收到了一条消息，未读消息从4个增加到了5个，FIFO即将满了。

## Rx FIFO溢出

当CAN_STAT寄存器的MS7_RFO位置位时，表示Rx FIFO又接收到了一条消息，然后由于FIFO已满，因而有一个消息丢失了。

## 匹配过程

匹配过程是通过搜索查找与CAN总线上帧标识符相匹配的接收邮箱或接收FIFO（如果使能了FIFO）来完成，IDE域和RTR域也参与匹配过程。

当完成DLC字段的接收，则开始匹配过程。

邮箱的匹配受到RPFQEN位的影响，如果RPFQEN位为0，则第一个匹配到的邮箱就是匹配获胜者，无论其是否为空或非空状态。如果RPFQEN位为1，则第一个匹配到的空邮箱就是匹配获胜者或者最后一个非空状态的匹配邮箱为获胜者。

## 搜索过程

 如果使能了Rx FIFO，则CAN_CTL2寄存器的RFO位控制了搜索顺序。

如果RFO位置位，则匹配过程从接收邮箱开始搜索，然后再搜索Rx FIFO。接收邮箱从邮箱编号低到高的方向进行搜索。

首先，搜索匹配的可用于接收的邮箱。如果RPFQEN位为0，则第一个匹配到的邮箱就是获胜者，无论其是否为空或非空状态。如果RPFQEN位为1，则第一个匹配到的空邮箱就是匹配获胜者。两种情况下均不再搜索Rx FIFO。

然后，如果RPFQEN位为1时，没有匹配到空邮箱，但找到了一个匹配的非空邮箱，则还要搜索Rx FIFO来确定匹配获胜者：如果找到了匹配的Rx FIFO并且FIFO未满，则RxFIFO就是匹配获胜者；否则，最后一个找到的匹配的可用于接收的非空邮箱就是匹配获胜者（会导致邮箱CODE码OVERRUN）。

最后，如果没有找到匹配的接收邮箱（即没有匹配的可用于接收的空邮箱，也没有匹配的可用于接收的非空邮箱），则搜索Rx FIFO。在这种情况下，如果Rx FIFO是匹配的但是FIFO满了，将会导致Rx FIFO溢出；如果Rx FIFO不匹配（不管FIFO是否是满的），则消息不会被接收进来。

- 如果RFO位清零，则匹配过程从Rx FIFO开始搜索，然后再搜索接收邮箱。

如果Rx FIFO是匹配的且FIFO未满，则Rx FIFO就是匹配获胜者。

如果Rx FIFO不匹配或者FIFO满了，则还要搜索接收邮箱。邮箱的匹配受到RPFQEN位的影响，如果RPFQEN位为0，则第一个匹配到的邮箱就是匹配获胜者，无论其是否为空或非空状态。如果RPFQEN位为1，则第一个匹配到的空邮箱就是匹配获胜者，如果没有搜索到空邮箱，则最后一个非空状态的匹配邮箱为获胜者。

 如果禁能了Rx FIFO，则匹配过程只搜索接收邮箱，参考前述的邮箱匹配描述。

可用于接收的空邮箱有以下两种情形：

对于数据帧的接收，或者当CAN_CTL2寄存器的RRFRMS位为1时的远程帧接收，可用于接收的空邮箱为：邮箱CODE域为EMPTY；邮箱CODE域为FULL或者OVERRUN，同时已经服务（读）过并解锁的。

 对于当CAN_CTL2寄存器的RRFRMS位为0时的远程帧接收，可用于接收的空邮箱为：邮箱CODE域为RANSWER。

## 接收邮箱的搜索匹配条件

对接收邮箱的搜索匹配条件，参考 29-9. ：

如果接收移位缓存中是一个数据帧（即RTR域为0），则将搜索CODE为EMPTY，FULL或者OVERRUN的接收邮箱：

如果CAN_CTL2寄存器的IDERTR_RMF位为0，表示需要匹配IDE域，不用匹配RTR域（忽略相关过滤寄存器的位30和位31）。ID域需要使用相关过滤寄存器的位0到位28过滤数据配置来进行过滤匹配。

如果CAN_CTL2寄存器的IDERTR_RMF位为1，表示IDE，RTR和ID域都需要分别使用相关过滤寄存器的位30，位31和位0到位28过滤数据配置来进行过滤匹配。

 如果接收移位缓存中是一个远程帧（即RTR域为1）：

如果CAN_CTL2寄存器中的RRFRMS位为0，表示将要查找CODE为RANSWER的接收邮箱，并且IDE，和ID域都需要分别使用相关过滤寄存器的位30，和位0到位28过滤数据配置来进行过滤匹配。

如果CAN_CTL2寄存器中的RRFRMS位为1，则搜索匹配过程与数据帧相同，将搜索CODE为EMPTY，FULL或者OVERRUN的接收邮箱：

如果CAN_CTL2寄存器的IDERTR_RMF位为0，表示需要匹配IDE域，不用匹配RTR域（忽略相关过滤寄存器的位30和位31）。ID域需要使用相关过滤寄存器的位0到位28过滤数据配置来进行过滤匹配。

如果CAN_CTL2寄存器的IDERTR_RMF位为1，表示IDE，RTR和ID域都需要分别使用相关过滤寄存器的位30，位31和位0到位28过滤数据配置来进行过滤匹配。


表 29-9. 接收邮箱匹配


<table><tr><td>接收到的位</td><td colspan="2">配置位</td><td colspan="4">邮箱描述符中用于匹配的域</td></tr><tr><td>RTR</td><td>IDERTR_RMF(在CAN_CTL2寄存器)</td><td>RRFRMS(在CAN_CTL2寄存器)</td><td>IDE</td><td>RTR</td><td>ID</td><td>CODE</td></tr><tr><td rowspan="2">0</td><td>0</td><td rowspan="2">-</td><td><eq>匹配^{(1)}</eq></td><td>从不<eq>^{(2)}</eq></td><td><eq>过滤匹配^{(3)}</eq></td><td>EMPTY / FULL /OVERRUN</td></tr><tr><td>1</td><td colspan="3">过滤匹配</td><td>EMPTY / FULL /OVERRUN</td></tr><tr><td rowspan="3">1</td><td>-</td><td>0</td><td>匹配</td><td>从不</td><td>匹配</td><td>RANSWER</td></tr><tr><td>0</td><td rowspan="2">1</td><td>匹配</td><td>从不</td><td>过滤匹配</td><td>EMPTY / FULL /OVERRUN</td></tr><tr><td>1</td><td colspan="3">过滤匹配</td><td>EMPTY / FULL /OVERRUN</td></tr></table>


1. 匹配：邮箱描述符中的域始终需要与接收到的位进行匹配比较，忽略相关过滤寄存器中的过滤数据配置。



2. 从不：邮箱描述符中的域始终不与接收到的位进行匹配比较，忽略相关过滤寄存器中的过滤数据配置。


3. 过滤匹配：邮箱描述符中的域需要使用相关过滤寄存器中的过滤数据配置，与接收到的位进行匹配比较。

## Rx FIFO 的搜索匹配条件

对Rx FIFO的搜索匹配条件，参考 29-10. Rx FIFO ：

如果CAN_CTL0寄存器的FS[1:0]位域值为0或者1，表示标识符过滤元素格式采用格式A或者格式B，并且IDE，RTR和ID域都需要使用相关过滤寄存器的位0到位31过滤数据配置来进行过滤匹配。

如果CAN_CTL0寄存器的FS[1:0]位域值为2，表示标识符过滤元素格式采用格式C，并且IDE，RTR域不进行匹配比较（FIFO描述符中没有这些位域），ID域需要使用相关过滤寄存器的位0到位31过滤数据配置来进行过滤匹配。

 如果CAN_CTL0寄存器的FS[1:0]位域值为3，表示标识符过滤元素格式采用格式D，不接受所有帧。


表 29-10. Rx FIFO 匹配


<table><tr><td>配置位</td><td colspan="3">Rx FIFO描述符中用于匹配的域</td></tr><tr><td>FS[1:0](在CAN_CTL0寄存器)</td><td>IDE</td><td>RTR</td><td>ID</td></tr><tr><td>0</td><td colspan="3">过滤匹配</td></tr><tr><td>1</td><td colspan="3">过滤匹配</td></tr><tr><td>2</td><td colspan="2">从不</td><td>过滤匹配</td></tr><tr><td>3</td><td colspan="3">不匹配的(1)</td></tr></table>


(1) 不匹配的：拒绝接收所有的帧。


## 移入

移入过程是在找到匹配的接收邮箱或者Rx FIFO之后，将接收移位缓存（一个内部描述符）中的内容拷贝到接收邮箱或者Rx FIFO的过程。

当找到匹配的接收邮箱或者Rx FIFO时，将挂起一个移入操作。当符合下述所有条件时，将开始移入操作：

 接收移位缓存中的帧有找到匹配的获胜邮箱或Rx FIFO。

 CAN总线处于：

- 帧间隔第二个位。

- 过载帧的第一个位。

 目标邮箱未被锁定。

如果目标邮箱有一个挂起的移入操作，而邮箱在暂停模式下解锁了，则开始移入操作；如果邮箱在CAN_CTL0寄存器LPS位为1时解锁了，挂起的移入操作将等到LPS位清0时才会开始。

当接收邮箱上正在进行一个移位过程，目标邮箱的的BUSY位（CODE[0]）将置位用于指示当前邮箱正在更新。

接收邮箱上的移入操作可以被取消，而Rx FIFO上的移入操作无法被取消。当符合下述中的一种情形时，接收邮箱的移入操作将被取消：

当CAN总线在到达接收移位缓存中存储的帧之后的帧间隔第一个位之后，目标邮箱被失活了，并且已经完成匹配过程。

 接收移位缓存中存储了一帧CAN节点自己发送的帧，而CAN_CTL0寄存器中SRDIS位为1，禁能了自接收功能。

 发生了一个CAN协议错误。

当完成了移入操作，接收邮箱描述符或者Rx FIFO描述符（如果使能了Rx FIFO）将更新为接收到的帧，如果是移入到Rx FIFO，则CAN_RFIFOIFMN寄存器也会更新，如果是移入到接收邮箱，则

接收邮箱描述符的CODE域也会更新。

## 过滤数据配置

## 当禁能Rx FIFO时：

 如果CAN_CTL0寄存器的RPFQEN位为0，则使用CAN_RMPUBF寄存器来配置所有接收邮箱的过滤数据配置。

 如果CAN_CTL0寄存器的RPFQEN位为1，则使用CAN_RFIFOMPFx（x = 0..31）寄存器来分别配置接收邮箱的过滤数据配置。

## 当使能Rx FIFO时：

 如果CAN_CTL0寄存器的RPFQEN位为0，则使用CAN_RMPUBF寄存器来配置所有接收邮箱的过滤数据配置，使用CAN_RFIFOPUBF和CAN_RFIFOMPFx（x = 0..31）寄存器来配置所有Rx FIFO标识符过滤表元素，并且所有这些寄存器的值的配置必须相同。

如果CAN_CTL0寄存器的RPFQEN位为1，则使用CAN_RFIFOMPFx（x=0..31）寄存器来配置由CAN_CTL2寄存器RFFN[3:0]位域设置的Rx FIFO标识符过滤表元素以及接收邮箱（由于接收邮箱描述符和Rx FIFO描述符不能同时占用同一个区域的RAM，因此用一组寄存器进行独立控制过滤数据的配置），由CAN_RFIFOPUBF寄存器来配置剩余所有的Rx FIFO标识符过滤表元素。

## 自接收

当CAN_CTL0寄存器的SRDIS位置位时，自接收功能被禁止，从而不接收所有由本节点发送的帧，即使已经找到了相匹配的接收邮箱或者Rx FIFO，并且不会有任何的标志或者中断产生。当SRDIS位清零时，允许将本节点发送的帧接收到相匹配的描述符中去。

## 29.3.7. 在虚拟联网模式下的数据接收

当设置CAN_CTL0寄存器的PNEN位和PNMOD位为1时，使能虚拟联网模式，CAN模块可以在MCU睡眠模式下接收帧。一个唤醒事件可以将CAN模块从虚拟联网模式唤醒。

有四组寄存器用于匹配的消息存储：CAN_PN_RWMxCS，CAN_PN_RWMxI，CAN_PN_RWMxD0和CAN_PN_RWMxD1寄存器，组号x从0到3。因此最多可以存储4帧消息（当CAN_PN_CTL0寄存器的NMM[7:0]位域值大于等于4时），并且只存储最新的消息。组号x表示消息到达的顺序。如果NMM[7:0]位域值小于4，则只存储NMM[7:0]个消息，存放在组号0到NMM[7:0]减1的寄存器组中。

如果要存储的消息的数据长度小于8个字节，则在接收到的DATA域后填充若干常数0字节到CAN_PN_RWMxD0和CAN_PN_RWMxD1（x = 0..3）寄存器中。对于匹配的唤醒帧不存储时间戳值。

注意：当处于虚拟联网模式时将忽略CAN FD格式的消息帧。

## 唤醒中断

有两种类型的唤醒中断事件，包括匹配唤醒事件，和超时唤醒事件。每个中断事件在CAN_PN_STAT寄存器中都有专门的标志位，在CAN_PN_CTL0寄存器组中有专门的使能位。它们的关系如 29-11. 所示。

当任意一种唤醒中断被使能，并且发生了相应的事件，则会产生一个唤醒中断。

## 超时唤醒事件

当CAN达到了超时事件，则发生一个超时唤醒事件。超时时间由CAN_PN_TO的WTO[15:0]位域来配置。

注意：即使到达了超时时间，在CPU真正唤醒之前CAN模块仍然不会停止消息的接收过滤。

## 匹配唤醒事件

当CAN在超时时间之内接收到了一个或一组匹配的唤醒帧，则发生一个匹配唤醒事件。CAN_PN_STAT 寄存器的MMCNT[7:0]位域指示了从进入虚拟联网模式开始到CPU被唤醒的时间内所接收到的所有匹配帧的数目。

注意：即使CAN接收到了一个或一组匹配的唤醒帧，在CPU真正唤醒之前超时计数器不会停止计数。

## 帧匹配

参与唤醒匹配过程的帧域有IDE，RTR，ID，DLC和DATA域。

如果CAN_PN_CTL0寄存器的FFT[1:0]位域配置为0，则当接收到一个帧除了DATA，DLC域之外的其他域（即IDE，RTR和ID域）都匹配时，发生一个匹配唤醒事件。

 如果CAN_PN_CTL0寄存器的FFT[1:0]位域配置为1，则当接收到一个帧所有域（即IDE，RTR，ID，DLC和DATA域）都匹配时，发生一个匹配唤醒事件。

如果CAN_PN_CTL0寄存器的FFT[1:0]位域配置为2，则当接收到一组帧（帧数量由CAN_PN_CTL0寄存器的NMM[7:0]位域来配置）除了DATA，DLC域之外的其他域（即IDE，RTR和ID域）都匹配时，发生一个匹配唤醒事件。

如果CAN_PN_CTL0寄存器的FFT[1:0]位域配置为3，则当接收到一组帧（帧数量由CAN_PN_CTL0寄存器的NMM[7:0]位域来配置）所有域（即IDE，RTR，ID，DLC和DATA域）都匹配时，发生一个匹配唤醒事件。

## IDE 域匹配

一个匹配的IDE域是使用CAN_PN_IFEID1寄存器中的过滤数据配置时，接收的帧IDE域与CAN_PN_EID0寄存器中配置的期望IDE域一致。

## RTR 域匹配

一个匹配的RTR域是使用CAN_PN_IFEID1寄存器中的过滤数据配置时，接收的帧RTR域与CAN_PN_EID0寄存器中配置的期望RTR域一致。

## ID 域匹配

当 CAN_PN_CTL0 寄 存 器 的 IDFT[1:0] 位 域 配 置 为 0 ， 则 一 个 匹 配 的 ID 域 是 使 用CAN_PN_IFEID1寄存器中的过滤数据配置时，接收的帧ID域与CAN_PN_EID0寄存器中配置的期望ID域一致。

 当CAN_PN_CTL0寄存器的IDFT[1:0]位域配置为1，则一个匹配的ID域是接收的帧ID域大于等于CAN_PN_EID0寄存器中配置的期望ID域。没有使用CAN_PN_IFEID1寄存器。

 当CAN_PN_CTL0寄存器的IDFT[1:0]位域配置为2，则一个匹配的ID域是接收的帧ID域小于等于CAN_PN_EID0寄存器中配置的期望ID域。没有使用CAN_PN_IFEID1寄存器。

当CAN_PN_CTL0寄存器的IDFT[1:0]位域配置为3，则一个匹配的ID域是接收的帧ID域大于等于CAN_PN_EID0寄存器中配置的期望ID域，并且小于等于CAN_PN_IFEID1寄存器中配置的期望ID域。

## DLC域匹配

 一个匹配的DLC域是接收的帧DLC域大于等于CAN_PN_EDLC寄存器中DLCELT[3:0]位域配置的期望DLC域下限值，并且小于等于CAN_PN_EDLC寄存器中DLCEHT[3:0]位域配置的期望DLC域上限值。

## DATA域匹配

当CAN_PN_CTL0寄存器的DATAFT[1:0]位域配置为0，则一个匹配的DATA域是使用CAN_PN_DF0EDH0寄存器和CAN_PN_DF1EDH1寄存器中的过滤数据配置时，接收的帧DATA域与CAN_PN_EDLx（x = 0,1）寄存器中配置的期望DATA域一致。

当CAN_PN_CTL0寄存器的DATAFT[1:0]位域配置为1，则一个匹配的DATA域是接收的帧DATA 域 大 于 等 于 CAN_PN_EDLx （ x = 0,1 ） 寄 存 器 中 配 置 的 期 望 DATA 域 。CAN_PN_DF0EDH0寄存器和CAN_PN_DF1EDH1寄存器保留不使用。

当CAN_PN_CTL0寄存器的DATAFT[1:0]位域配置为2，则一个匹配的DATA域是接收的帧DATA 域 小 于 等 于 CAN_PN_EDLx （ x = 0,1 ） 寄 存 器 中 配 置 的 期 望 DATA 域 。CAN_PN_DF0EDH0寄存器和CAN_PN_DF1EDH1寄存器保留不使用。

当CAN_PN_CTL0寄存器的DATAFT[1:0]位域配置为3，则一个匹配的DATA域是接收的帧DATA域大于等于CAN_PN_EDLx（x = 0,1）寄存器中配置的期望DATA域，并且小于等于CAN_PN_DF0EDH0寄存器和CAN_PN_DF1EDH1寄存器中配置的期望DATA域。

注意：在这种情况下，这两个8字节的期望数据寄存器都需要配置，当接收到的帧DLC域小于

8个字节（DLC域已匹配），则在DATA域匹配时，是将接收的帧DATA域加上若干常数0填充字节，再与期望的DATA域进行比较。

## 29.3.8. CAN FD 操作

通过配置CAN_CTL2寄存器的ISO位，可以选择CAN FD功能支持ISO CAN FD（ISO11898-1规范）或非ISO CAN FD（Bosch CAN FD规范V1.0），这两种规范彼此不兼容。相比于非ISO CAN FD协议，ISO CAN FD协议引入了一个3位的计数器和一个奇偶校验位，因此错误检测能力有所提升。

CAN FD模式同时支持CAN常规帧和CAN FD帧的收发。FDF位（在常规帧中该位为保留位）用于区分当前帧是FD帧还是常规帧。当FDF位为隐性’1’，表示是CAN FD帧；如果为显性，表示是常规帧。相比于常规帧，CAN FD帧不支持Rx FIFO，不支持Rx FIFO DMA功能，也不支持虚拟联网模式。

通过将CAN_CTL0寄存器的FDEN位置位，可以使能CAN FD模式。

## CAN FD BRS

在CAN FD模式下，最多可以支持64字节数据，当BRS位为隐性时，波特率在数据阶段（从BRS位到CRC界定符的第一个采样点，或者当发生错误时到错误帧的SOF）可达到最大8 Mbit/s，详情请参考ISO11898-1或Bosch CAN FD规范V1.0。

当设置CAN_FDCTL寄存器的BRSEN位为1（在下一帧起作用），并且发送邮箱的BRS位配置为隐性位’1’时，在CAN FD帧的数据阶段将使用更高波特率（称为数据波特率），其他位使用正常波特率来通信。波特率将在BRS位的采样点进行切换。数据波特率由CAN_FDBT寄存器来配置，正常波特率由CAN_BT寄存器来配置。

当设置CAN_FDCTL寄存器的BRSEN位为0，或者发送邮箱的BRS位配置为显性位’0’，则在整个CAN FD帧传输期间都使用正常波特率。

注意：整个CAN FD帧的时间单元的大小应保持一致，以避免帧在通信过程中总线发生相位错误。

对于FD帧，所有节点都需要接收2位长的显性ACK应答字段作为一个有效的ACK，用以补偿与接收节点之间的相位偏移。详情请参考ISO11898-1规范。

## CAN FD ESI

由发送邮箱的MDES0字的ESI域，以及CAN_ERR1寄存器的ERRSI[1:0]位域来控制ESI位（在DLC域之前的位，请参考ISO11898-1或Bosch CAN FD规范V1.0）的发送。如果MDES0字中的ESI域为0，则根据CAN_ERR1寄存器的ERRSI[1:0]位域，主动错误节点发送为显性位，被动错误节点发送为隐性位。如果MDES0字中的ESI域为1，则节点发送MSED0字中的ESI域值。

## CAN FD CRC

不同帧格式使用不同的 CRC 多项式，汉明距离都为 6：

 多项式 CRC_15 用于常规帧：0xC599

$$
\mathsf {x} ^ {1 5} + \mathsf {x} ^ {1 4} + \mathsf {x} ^ {1 0} + \mathsf {x} ^ {8} + \mathsf {x} ^ {7} + \mathsf {x} ^ {4} + \mathsf {x} ^ {3} + 1
$$

 多项式 CRC_17 用于不超过 16 字节 DATA 域的 CAN FD 帧：0x3685B

$$
\mathsf {X} ^ {1 7} + \mathsf {X} ^ {1 6} + \mathsf {X} ^ {1 4} + \mathsf {X} ^ {1 3} + \mathsf {X} ^ {1 1} + \mathsf {X} ^ {6} + \mathsf {X} ^ {4} + \mathsf {X} ^ {3} + \mathsf {X} ^ {1} + 1
$$

 多项式 CRC_21 用于超过 16 字节 DATA 域的 CAN FD 帧：0x302899

$$
\mathsf {x} ^ {2 1} + \mathsf {x} ^ {2 0} + \mathsf {x} ^ {1 3} + \mathsf {x} ^ {1 1} + \mathsf {x} ^ {7} + \mathsf {x} ^ {4} + \mathsf {x} ^ {3} + 1
$$

对于发送，将在帧SOF时同时使用这三种CRC多项式进行CRC计算，最终发送的CRC由帧的FDF域和DLC域来确定。在成功发送帧后，当CAN_STAT寄存器的MSx位置位时，CAN_CRCCFD寄存器将同时更新为发送消息的CRC计算结果。CAN_CRCCFD同时用于FD帧和非FD帧。CAN_CRCC寄存器只存储常规帧的CRC计算结果。

对于接收，用于CRC校验的CRC多项式由接收到的FDF域和DLC域来确定。

注意：在常规帧中，CRC界定符为单个隐性位。在FD帧中，CRC界定符可能包含一到两个隐性位。发送节点应只发送一个隐性位作为CRC界定符，但接收时应在ACK应答位前的隐性位到显性位边沿到来之前接收2个隐性位。接收节点应在第一个CRC界定符之后发送ACK位。详情请参考ISO11898-1规范。

## 位填充

CAN FD帧的位填充功能不同于常规帧的位填充功能。

对于CAN FD帧的发送，将会在CRC场第一个位（忽略其他位填充条件）之前插入一个固定的填充位，另外在CRC场每4位（不包括固定的填充位）后都将插入一个固定的填充位。这些固定填充位的值都是它们前面的位的取反值。请参考ISO11898-1规范。

对于CAN FD帧的接收，将忽略这些固定的填充位。如果发现固定填充位的值与它前面位的值相同，则发生一个位填充错误。

注意：对于CAN FD帧，这些固定的填充位都将参与到CRC计算。对于常规帧，填充位不参与CRC计算。

## 再同步

CAN FD帧和常规帧的再同步以及硬件同步机制是相同的。正在发送CAN FD帧的节点在发送该帧的数据阶段时不执行再同步。

## 传输延迟补偿

当CAN FD帧的BRS域为隐性位时，发送CAN FD帧的数据阶段的位时间长度小于CAN收发器内部回路延迟的限定值，因此使用传输延迟补偿机制来避免当采样点到来时发送节点还没有收到自己发出的位，从而报位错误的情况发生。对CAN收发器内部回路延迟的测量是从发送的FDF位下降沿到接收的FDF位的下降沿，如 29-2. 所示。

传输延迟补偿机制定义了次级采样点SSP。当应用了传输延迟补偿，则发送节点应忽略在采样点检测到的位错误。当配置CAN_FDCTL寄存器的TDCEN位为1，使能了传输延迟补偿机制，则位检查将在真正接收到的位与延迟了（这个延迟的计算是基于收发器内部回路的延迟）的发送位之间进行比较。

传输延迟补偿值按下述公式进行计算：

$$
t _ {\text { compensation }} = t _ {\text { measure }} + t _ {\text { offset }}\tag{29-1}
$$

其中：

$$
t _ {\text { offset }} = \text { TDCO } [ 4: 0 ] \times t _ {\text { CANCLK }}\tag{29-2}
$$

$$
t _ {\text { offset }} ^ {\prime} = t _ {\text { PBS1\_FD }} + t _ {\text { PTS\_FD }} + t _ {\text { SYNC\_SEG }}\tag{29-3}
$$

$$
\mathsf {t} _ {\mathsf {P B S 1 \_ F D}} = (\mathsf {D P B S 1 [ 2 : 0 ] + 1}) \times \mathsf {t} _ {\mathsf {q \_ F D}}\tag{29-4}
$$

$$
\mathsf {t} _ {\mathsf {P T S \_ F D}} = \mathsf {D P T S} [ 4: 0 ] \times \mathsf {t} _ {\mathsf {q \_ F D}}\tag{29-5}
$$

$$
t _ {q \_ F D} = (D B A U D P S C [ 9: 0 ] + 1) \times t _ {C A N C L K}\tag{29-6}
$$

上述公式中 $\mathtt { t } _ { \mathtt { m e a s u r e } }$ 是测量的传输延迟； $\mathfrak { t } _ { \mathtt { o f f s e t } }$ 是传输延迟补偿偏置，存储在CAN_FDCTL寄存器的TDCO[4:0]位域中，以 $\mathsf { t } _ { \mathsf { C A N C L K } }$ 为单位存储， $\mathfrak { t } _ { \mathtt { o f f s e t } }$ 不可大于CAN数据阶段的位时间； $\mathsf { t ^ { \prime } } _ { \mathsf { o f f s e t } }$ 是传输延迟补偿偏置的理论值，用户可以根据 $\mathbf { t } _ { \mathsf { o f f s e t } } ^ { \prime }$ 来设置 $\mathfrak { t } _ { \mathtt { o f f s e t } }$ 。 t<sub>compensation</sub>是传输延迟补偿值，保存在CAN_FDCTL寄存器的TDCV[5:0]位域中，以 $\mathsf { t } _ { \mathsf { C A N C L K } }$ 为单位存储。

在上述公式中，DPBS1[2:0]，DPTS[4:0]，和DBAUDPSC[9:0]位域都在CAN_FDBT寄存器中配置。


图 29-2. 传输延迟


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/683352274bdf441ea0197971e083a7ea3f604ca276ec9d2d4f329f707f058adc.jpg)



$\mathsf { t _ { c o m p e n s a t i o n } }$ 最大值为(3 × data bit time - $2 \times t _ { { \tt q } _ { \tt L } \tt F D } )$ 。如果超过这个值，就无法补偿这个传输延迟了，从而CAN_FDCTL寄存器中TDCS位将置位。传输延迟补偿应至少补偿2个数据阶段位时间长度。


## 29.3.9. 错误和状态

发送错误计数器（CAN_ERR0寄存器中的TECNT[7:0]位域）和接收错误计数器（CAN_ERR0寄存器中的RECNT[7:0]位域）将FD帧和非FD帧的错误都进行了统计，在错误条件触发时增加或减少相应的计数。关于TECNT[7:0]和RECNT[7:0]错误计数管理的详细信息请参考CAN协议相关章节。

对于CAN FD帧，数据阶段的发送错误计数器（CAN_ERR0寄存器的TEFCNT[7:0]位域）和数据阶段的接收错误计数器（CAN_ERR0寄存器的REFCNT[7:0]位域）只有在帧BRS域为隐性位时才起作用。这些错误计数器在离线状态停止计数并保持计数值，直到离线状态恢复为主动错误状态才重新从0开始计数。

注意：在虚拟联网模式下，接收错误计数器RECNT[7:0]和数据阶段的接收错误计数器REFCNT[7:0]都继续计数，并且保存相应的错误标志，发送错误计数器TECNT[7:0]和数据阶段的发送错误计数器TEFCNT[7:0]停止计数并保持计数值。当返回正常模式时，CAN_ERR0寄存器和CAN_ERR1寄存器将更新计数器值以及保存的错误标志位。

## 状态

## 被动错误状态

当CAN_ERR0寄存器的TECNT[7:0]或RECNT[7:0]计数值增加到大于127时，CAN_ERR1寄存器的ERRSI[1:0]位域更新为1（被动错误状态）。

## 主动错误状态

当节点为被动错误状态，并且当CAN_ERR0寄存器的TECNT[7:0]或RECNT[7:0]计数值其中一个已满足小于等于127的条件，而另一个也减少到小于等于127时，CAN_ERR1寄存器的ERRSI[1:0]位域更新为0（主动错误状态）。

## 离线状态

如果CAN_ERR0寄存器的TECNT[7:0]计数值增加到大于255，则CAN_ERR1寄存器的ERRSI[1:0]位域更新为0b1x（离线状态），并且CAN_ERR1寄存器的BOF位将置位，如果CAN_CTL1寄存器的BOIE位置位，则将产生一个中断。随后TECNT[7:0]计数值复位为0。

## 离线恢复：

离线恢复要求CAN总线能检测到CAN协议所定义的离线恢复序列（在CAN_RX检测到128次连续11个位的隐性位）。当CAN_ERR0寄存器的TECNT[7:0]计数值达到128时，CAN_ERR1寄存器的ERRSI[1:0]位域更新为0（主动错误状态），并且CAN_ERR0寄存器的TECNT[7:0]和RECNT[7:0]计数值都复位为0。

可通过配置CAN_CTL1寄存器的ABORDIS位来控制当检测到离线恢复序列后是自动恢复还是保持在离线状态。

如果ABORDIS位为0，使能了自动离线恢复，则CAN总线在检测到离线恢复序列后将自动恢复。如果在检测到离线恢复序列后ABORDIS位才变为0，则CAN总线需要再检测到11个连续的隐性位后才恢复与总线的同步。

如果ABORDIS位为1，禁能了自动离线恢复。如果在CAN节点进入离线状态之后ABORDIS位才变为1，则在下一次CAN节点进入离线状态才禁用自动离线恢复功能。

## 总线集成状态

如果节点检测到了协议异常事件（当CAN_CTL0寄存器的FDEN位为0时，如果收到了一个FD帧的FDF位），或在离线恢复过程中开始协议操作，则节点进入总线集成状态。在该状态，CAN节点与总线脱离同步。当节点检测到总线空闲条件（11个连续的隐性位）时，节点退出总线集成状态。请参考CAN协议ISO11898-1规范。

协议异常的监测由CAN_CTL2寄存器的PREEN位来控制。

可通过CAN_CTL2寄存器的EFDIS位来配置边沿滤波，用于总线集成状态。当使能了边沿滤波，在硬件同步的边沿检测时需要检测到连续两个正常时间单元的显性电平。当发生了硬件同步，对总线空闲条件（11个连续的隐性位）的检测将重新开始。如果应用了边沿滤波，小于一个正常时间单元（FD帧中数据阶段的位）的总线显性电平将被忽略，以避免误触发总线空闲条件。请参考CAN协议ISO11898-1规范。

注意：建议保持EFDIS位为0来使能边沿滤波，以避免总线空闲条件被误检测。

## 错误

如果至少有一个错误标志位置位（CAN_ERR1寄存器中的ACKERR，BRERR，BDERR，CRCERR，FMERR和STFERR），则CAN_ERR1寄存器的ERRSF位将置位。如果CAN_CTL1寄存器的ERRSIE位为1，将产生一个错误中断。

如果至少有一个错误标志位置位（CAN_ERR1寄存器中的BRFERR，BDFERR，CRCFERR，FMFERR和STFFERR），则CAN_ERR1寄存器中的ERRFSF位将置位。如果CAN_CTL2寄存器的ERRFSIE位为1，将产生一个FD帧BRS位为隐性位时数据阶段的错误中断。

## ACK错误

如果连接中只存在一个节点，则在每次发送帧的时候都会导致CAN_ERR0寄存器的TECNT[7:0]计数器值增加（由ACK错误引起，最大到128），并且发生一个ACK错误，由CAN_ERR1寄存器的ACKERR位指示。

## 位隐性错误

如果至少有一个位发送为’1’，接收为’0’，则发生了一个位隐性错误。参考CAN_ERR1寄存器的BRFERR和BRERR位。

## 位显性错误

如果至少有一个位发送为’0’，接收为’1’，则发生了一个位显性错误。参考CAN_ERR1寄存器的BDFERR和BDERR位。

## CRC错误

如果计算的CRC校验值与接收帧的CRC字段值不同，则发生了一个CRC错误。请参考CAN_ERR1寄存器的CRCFERR和CRCERR位。

## 格式错误

如果固定格式的字段包含至少一个非法的位，则发生了一个格式错误。请参考CAN_ERR1寄存器的FMFERR和FMERR位。

## 填充错误

请参考CAN_ERR1寄存器的STFFERR和STFERR位。

## 29.3.10. 通信参数

位时间

CAN协议控制器将位时间分为三个部分：

同步段（SYNC_SEG）：期望在该段检测到有效跳变沿。该段占用1个时间单元（1×t<sub>q</sub>）。

位段1（BS1）：该段包括CAN协议中的传播时间段和相位缓冲段1。该段可自动延长来补偿网络节点的频率不同引起的相位正漂移。

位段2（BS2）：该段定义了采样点。该段同样可以自动缩短来补偿相位负漂移。该段占用的时间单元不可少于2个。

注意：位时间的配置范围必须符合CAN协议规范ISO 11898-1。

位时间如 29-3. CAN 所示。


图 29-3. CAN 位时间


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/5e5f5636-5985-46be-a2ae-17e79b264a50/5beab1c4d35de016334df1bf42c73390d24bc17b6b7b8993bef34b4dda3fed4b.jpg)


再同步补偿宽度（SJW）：可延长或缩短再同步补偿宽度来补偿CAN网络节点的同步误差。通过CAN_BT寄存器的SJW[4:0]来配置正常位时间下的再同步补偿宽度，通过CAN_FDBT寄存器的DSJW[2:0]来配置数据位时间下的再同步补偿宽度。

有效跳变沿定义为只有当在前一个采样点检测到的总线状态为隐性（recessive）时，一个位时间

内从隐性位到显性位的第一次转变。

如果有效跳变沿在BS1期间被检测到，而不是在SYNC_SEG期间，BS1将最多被延长SJW，因此采样点延迟。

相反，如果有效跳变在BS2期间被检测到，而不是SYNC_SEG期间，BS2将会最多被缩短SJW，因此采样点提前。

注：有关硬同步和再同步的详细说明，请参考ISO 11898标准。

## 位采样

通过CAN_CTL1寄存器的BSPMOD位来定义Rx接收引脚上的采样模式。

当BSPMOD位为0，则只采样一次（即采样点）。

当BSPMOD位为1，则采样3次来决定接收的位电平，包括采样点，以及2次在采样点之前的采样。注意：该位在CAN FD模式时不能为1。

## 波特率

CAN模块有两个时钟域：

 控制单元、CAN寄存器的时钟来自APB2总线时钟。

协议控制器的时钟（CANCLK）由RCU_CFG2寄存器的CANxSEL[1:0]位域来配置，可配置为外部晶振时钟，或者APB2总线时钟，或者APB2总线时钟除以2，或者IRC64MDIV内部时钟。

CAN波特率计算如下：

$$
\text { BaudRate } = \frac {1}{\text { CAN   Bit   Time }}\tag{29-7}
$$

$$
\text { CAN   Bit   Time } = t _ {\text { SYNC\_SEG }} + t _ {\text { PTS }} + t _ {\text { PBS1 }} + t _ {\text { PBS2 }}\tag{29-8}
$$

其中：

$$
t _ {\text {SYNC\_SEG}} = 1 \times t _ {q}\tag{29-9}
$$

$$
t _ {P T S} = (N _ {P T S} + 1) \times t _ {q} \text {or} t _ {P T S} = N _ {D P T S} \times t _ {q}\tag{29-10}
$$

$$
t _ {P B S 1} = (N _ {P B S 1} + 1) \times t _ {q}\tag{29-11}
$$

$$
t _ {P B S 2} = (N _ {P B S 2} + 1) \times t _ {q}\tag{29-12}
$$

$$
t _ {q} = \left(N _ {\text { BAUDPSC }} + 1\right) \times t _ {\text { CANCLK }}\tag{29-13}
$$

在公式中，对于正常波特率：

$N _ { \mathsf { P T S } }$ $\Nu _ { \tt P B S 1 }$ $\Nu _ { \tt P B S 2 }$ 和 $N _ { B A U D P S C }$ 分别由CAN_BT寄存器的PTS[5:0]，PBS1[4:0]，PBS2[4:0]和

BAUDPSC[9:0]位域来配置。

对于数据波特率：

N<sub>DPTS</sub>，N<sub>PBS1</sub>，N<sub>PBS2</sub>和N<sub>BAUDPSC</sub>分别由CAN_FDBT寄存器的DPTS[4:0]，DPBS1[2:0]，DPBS2[2:0]和DBAUDPSC[9:0]位域来配置。

## 时间戳

CAN硬件支持一个16位的内部计数器（计数值可通过CAN_TIMER寄存器来读写）用于生成时间戳。在一次成功的发送或者接收之后，将在CAN总线的SOF场抓取内部计数器的值，并写入到MDES0或者FDES0字的TIMESTAMP位域中。

在暂停模式下或者当 CAN_CTL0 寄存器的 LPS 位为 1 时，内部计数器停止计数。

## 内部计数器时钟源

如果 CAN_CTL2 寄存器的 ITSRC 位为 1，则选择 TRIGSEL 的输出 CANx_EX_TIME_TICK 作为内部计数器的递增条件。其中 CANx_EX_TIME_TICK 和 APB2 总线时钟属于同一时钟域，为了保证内部计数器能够有效递增，CANx_EX_TIME_TICK 信号源的脉冲宽度需要大于等于 APB2 总线时钟周期。

如果 CAN_CTL2 寄存器的 ITSRC 位为 0，则选择 CAN 波特率作为内部计数器的递增条件，即每发送或接收一个位，计数值加 1。当总线上没有消息时，则计数器按前一次配置的 CAN 波特率进行计数。

## 时间同步

如果 CAN_CTL1 寄存器的 TSYNC 位为 1，当第一个邮箱描述符成功接收到了任意报文时，则将内部计数器值复位来完成网络时间的同步。

## 29.3.11. 中断

CAN中断事件与标志如 29-11. 所示。


表 29-11. 中断事件


<table><tr><td colspan="2" rowspan="2">中断事件</td><td colspan="3">标志</td><td colspan="4">使能控制</td></tr><tr><td colspan="2">位</td><td>寄存器</td><td>使能位</td><td>控制位</td><td>使能寄存器</td><td>控制寄存器</td></tr><tr><td colspan="2">离线</td><td colspan="2">BOF</td><td rowspan="7">CAN_ERR1</td><td colspan="2">BOIE</td><td colspan="2">CAN_CTL1</td></tr><tr><td colspan="2">离线恢复</td><td colspan="2">BORF</td><td colspan="2">BORIE</td><td colspan="2">CAN_CTL2</td></tr><tr><td rowspan="5">错误汇总</td><td>位隐性错误</td><td rowspan="5">ERRSF</td><td>BRERR</td><td colspan="2" rowspan="5">ERRSIE</td><td colspan="2" rowspan="5">CAN_CTL1</td></tr><tr><td>位显性错误</td><td>BDERR</td></tr><tr><td>ACK错误</td><td>ACKERR</td></tr><tr><td>CRC错误</td><td>CRCERR</td></tr><tr><td>格式错误填充错误</td><td>FMERRSTFERR</td></tr><tr><td rowspan="5">FD帧数据位时间的错误汇总</td><td>位隐性错误</td><td rowspan="5">ERRFSF</td><td>BRFERR</td><td rowspan="7"></td><td colspan="2" rowspan="5">ERRFSIE</td><td colspan="2" rowspan="5">CAN_CTL2</td></tr><tr><td>位显性错误</td><td>BDFERR</td></tr><tr><td>CRC错误</td><td>CRCFERR</td></tr><tr><td>格式错误</td><td>FMFERR</td></tr><tr><td>填充错误</td><td>STFFERR</td></tr><tr><td colspan="2">Tx错误警告</td><td colspan="2">TWERRIF</td><td>TWERRIE</td><td rowspan="2">WERREN</td><td rowspan="2">CAN_CTL1</td><td rowspan="2">CAN_CTL0</td></tr><tr><td colspan="2">Rx错误警告</td><td colspan="2">RWERRIF</td><td>RWERRIE</td></tr><tr><td colspan="2">匹配唤醒</td><td colspan="2">WMS</td><td rowspan="2">CAN_PN_STAT</td><td colspan="2">WMIE</td><td colspan="2" rowspan="2">CAN_PN_CTL0</td></tr><tr><td colspan="2">超时唤醒</td><td colspan="2">WTOS</td><td colspan="2">WTOIE</td></tr><tr><td colspan="2" rowspan="2">邮箱成功发送或接收帧</td><td colspan="2">所有位</td><td rowspan="5">CAN_STAT</td><td>所有位</td><td>RFEN = 0</td><td rowspan="5">CAN_INTE N</td><td rowspan="5">CAN_CTL0</td></tr><tr><td colspan="2">MSx</td><td>MIEx</td><td>RFEN = 1</td></tr><tr><td colspan="2">Rx FIFO非空</td><td colspan="2">MS5_RFNE</td><td>MIE5</td><td rowspan="3">RFEN = 1 &amp; DMAEN = 0</td></tr><tr><td colspan="2">Rx FIFO警告</td><td colspan="2">MS6_RFW</td><td>MIE6</td></tr><tr><td colspan="2">Rx FIFO溢出</td><td colspan="2">MS7_RFO</td><td>MIE7</td></tr></table>

## 29.4. 典型的 CAN 配置流程示例

在上电复位或系统复位之后，应用程序可按以下的典型操作流程来配置并启动CAN模块：

配置CAN模块的时钟源CANCLK，并使能CAN模块时钟

配置RCU_CFG2寄存器的CANxSEL[1:0]位来选择CAN模块的时钟源。配置RCU_APB2EN寄存器来使能CAN模块时钟。

 配置通讯接口

配置GPIO和AFIO模块，将相应的功能引脚映射到复用功能上。

 进入暂停模式

由于INAMOD位，HALT位，NRDY位和INAS位在上电复位或系统复位后默认置位，因此CAN将自动进入暂停模式，用以进行CAN寄存器的配置。

 处理CAN_STAT寄存器中置位的标志位

读取接收邮箱描述符或者Rx FIFO描述符的内容，清除CAN_STAT寄存器中相关标志位，然后读取CAN_TIMER寄存器来完成标志位的处理服务。如果使能了Rx FIFO，通过将CAN_STAT寄存器的MS0位置位来进行清FIFO操作。同样进行发送邮箱的置位的标志位的处理。

 初始化邮箱描述符或者Rx FIFO描述符的物理内存空间

通过CAN_CTL0寄存器的MSZ[4:0]位域来配置邮箱描述符或者Rx FIFO描述符的物理内存空间。

 配置通信参数

1）在CAN_BT寄存器中的PTS[5:0]，PBS1[4:0]，PBS2[4:0]，SJW[4:0]和BAUDPSC[9:0]位域来配置CAN的正常波特率。

2）如果需要，可通过CAN_CTL1寄存器的BSPMOD位来配置采样模式。

3）如果需要，可通过配置PREEN和EFDIS位用于总线集成状态。

##  配置发送相关的控制参数

1）通过CAN_CTL1的MTO位和CAN_CTL0寄存器的LAPRIOEN位来配置仲裁优先级。

2）如果需要，可通过CAN_CTL2寄存器的ASD[4:0]位域来配置仲裁启动延迟。

3）通过配置CAN_CTL0寄存器的MST位来使能发送邮箱描述符的发送中止功能。

##  配置接收相关的控制参数

1）通过CAN_CTL0寄存器的RFEN位来选择是否使用Rx FIFO，通过DMAEN位来选择是否使用Rx FIFO DMA功能。

2）通过CAN_CTL0寄存器的RPFQEN位来配置接收私有过滤器&接收邮箱队列功能。

3）通过CAN_CTL2寄存器的RFO，RRFRMS和IDERTR_RMF位来配置接收过滤相关参数。

4）通过CAN_RMPUBF，CAN_RFIFOPUBF和CAN_RFIFOMPFx（x = 0..31）寄存器来进行接收邮箱和Rx FIFO过滤数据的配置。如果使能了Rx FIFO，还要通过CAN_CTL0寄存器的FS[1:0]位域来配置Rx FIFO标识符过滤表元素格式，通过CAN_CTL2寄存器的RFFN[3:0]位域来配置Rx FIFO标识符过滤表元素数目。

##  如果需要CAN FD操作

1）通过CAN_CTL2寄存器的ISO位进行CAN FD协议的选择。

2）通过CAN_CTL0寄存器的FDEN位来使能CAN FD模式。

3）通过CAN_FDCTL寄存器的MDSZ[1:0]位域来配置邮箱数目。

4）如果需要，通过CAN_FDCTL寄存器的TDCEN和TDCO[4:0]来进行CAN FD的传输延迟补偿功能配置。

5 ） 通 过 CAN_FDBT 寄 存 器 的 DPTS[4:0] ， DPBS1[2:0] ， DPBS2[2:0] ， DSJW[2:0] 和DBAUDPSC[9:0]来进行CAN数据波特率的配置。

##  配置中断

通过CAN_CTL0，CAN_CTL1，CAN_CTL2和CAN_INTEN寄存器来使能需要的中断。

##  初始化发送/接收邮箱描述符

1）如果需要发送，初始化发送邮箱描述符。

2）如果需要接收，初始化接收邮箱描述符，如果使能了Rx FIFO，则还需初始化Rx FIFO描述符，以及Rx FIFO标识符过滤表元素。

 如果需要进入虚拟联网模式，置位CAN_CTL0寄存器的PNEN位和SLEPMOD位，并配置相关用于唤醒的寄存器。

##  退出暂停模式

通过清除CAN_CTL0寄存器的HALT位来退出暂停模式，随后CAN节点将恢复与CAN总线的同步。
