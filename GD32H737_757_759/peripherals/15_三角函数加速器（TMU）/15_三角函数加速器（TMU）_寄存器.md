# 15.5. TMU 寄存器

TMU 基地址：0x4001 0000

# 15.5.1. 控制和状态寄存器（TMU_CS）

地址偏移：0x00

复位值：0x0000 0050

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>ENDF</td><td colspan="8">保留</td><td>IWIDTH</td><td>OWIDTH</td><td>INUM</td><td>ONUM</td><td>WDEN</td><td>RDEN</td><td>RIE</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="3">FACTOR[2:0]</td><td colspan="4">ITRTNUM[3:0]</td><td colspan="4">MODE[3:0]</td></tr><tr><td colspan="5"></td><td colspan="3">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>ENDF</td><td>TMU运算结束标志0: TMU当前无运算或者正在进行运算1: TMU运算结束,结果已经写入TMU_ODATA寄存器当TMU运算结束并且结果已经写入TMU_ODATA寄存器时,该位硬件置1。读TMU_ODATA寄存器(ONUM+1)次,该位硬件清0。注意:当该位为1时,新的TMU运算不会启动。</td></tr><tr><td>30:23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>IWIDTH</td><td>输入数据位宽0: 32-bit1: 16-bit该位决定了输入数据的定点格式。如果配置为32-bit,则写入TMU_IDATA寄存器的数据为q1.31定点格式。如果配置为16-bit,则写入TMU_IDATA寄存器的数据为q1.15定点格式。第一个数据写入TMU_IDATA的低半字,第二个数据写入TMU_IDATA的高半字。</td></tr><tr><td>21</td><td>OWIDTH</td><td>输出数据位宽0: 32-bit1: 16-bit该位决定了输出数据的定点格式。如果配置为32-bit,则TMU_ODATA寄存器包含的输出数据为q1.31定点格式。如果配置为16-bit,则TMU_ODATA寄存器包含的输出数据为q1.15定点格式。第一个输出数据在TMU_ODATA的低半字,第二个输出数据在TMU_IDATA的高半字。</td></tr><tr><td>20</td><td>INUM</td><td>写TMU_IDATA寄存器的次数0:一次32-bit写操作。一次32-bit写TMU_IDATA操作可以启动一次TMU运算。1:两次32-bit写操作。两次连续的32-bit写TMU_IDATA操作可以启动一次TMU运算。注意:当输入数据格式为q1.15(IWIDTH=1)并且TMU模式只需要一个输入数据(INUM=0),TMU_IDATA的高半字不使用。</td></tr><tr><td>19</td><td>ONUM</td><td>写TMU_ODATA寄存器的次数0:一次32-bit读操作。当TMU运算结束,只有一个32-bit运算结果传输进TMU_ODATA寄存器。读一次TMU_ODATA寄存器将清除ENDF标志。1:两次32-bit读操作。当TMU运算结束,有两个32-bit运算结果传输进TMU_ODATA寄存器。读两次TMU_ODATA寄存器将清除ENDF标志。注意:当OWIDTH=1(输出数据格式为q1.15),只需要一个32-bit读操作。</td></tr><tr><td>18</td><td>WDEN</td><td>DMA写请求使能0:禁能1:使能。当无TMU运算挂起时,产生DMA写请求。</td></tr><tr><td>17</td><td>RDEN</td><td>DMA读请求使能0:禁能1:使能。当ENDF置1时,产生DMA读请求。</td></tr><tr><td>16</td><td>RIE</td><td>读中断使能0:禁能1:使能。当ENDF置1时,产生读中断请求。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:8</td><td>FACTOR[2:0]</td><td>缩放因子该位域定义了缩放因子:<eq>2^{FACTOR[2:0]}</eq>。000: <eq>2^0</eq>001: <eq>2^1</eq>010: <eq>2^2</eq>...</td></tr></table>

110：26 

111：27 

当实际输入参数超过规定的输入数据范围[-1,1)，实际输入参数需要除以 2FACTOR[2:0]，并且输出数据需要乘以 2FACTOR[2:0]以得到实际输出结果，细节如下：

TMU_IDATA = 实际输入参数/2FACTOR[2:0]

实际输出结果 = TMU_ODATA*2FACTOR[2:0].

# 注意：

1. 对模式 8 和模式 9，该位域针对不同输入参数推荐了一些配置。对于模式 0、模式 1、模式2 和模式 3，建议该位域配置为 3’b000。对模式5、模式 6 和模式7，该位域建议配置为 3’b001。

2. 输入数据（TMU_IDATA）和输出数据（TMU_ODATA）是 q1.31 或者 q1.15 格式的。

7:4 ITRTNUM[3:0] 迭代次数

该位域定义了CORDIC的迭代次数为：ITRTNUM[3:0]*4.

0000：保留

0001：4次迭代

0010：8次迭代

0110：24次迭代

0111~1111：保留

注意：迭代次数越高，精度越高。

3:0 MODE[3:0] TMU模式

0000：模式0, ?? ∗ ??????(??)

0001：模式1, ?? ∗ ??????(??)

0010：模式2, phase= atan2 (y,x)

0011：模式3, modulus=√x2+y2

0100：模式4, tan-1 (x)

0101：模式5, cosh (x)

0110：模式6, sinh (x)

0111：模式7, tanh-1 (x)

1000：模式8, ln (x)

1001：模式9, √x

1010~1111：保留

# 注意：

x、??：第一个输入数据

y、??：第二个输入数据

# 15.5.2. 输入数据寄存器（TMU_IDATA）

地址偏移：0x04

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDATA[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDATA[15:0]</td></tr></table>


w 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDATA[31:0]</td><td>输入数据</td></tr></table>

输入数据写入该寄存器。细节参考 15-1. 。

# 注意：

1. 当无TMU运算正在进行并且需要的输入参数已经写入该寄存器，将启动一次新的TMU运算。

2. 当TMU正在进行一次运算时，再写入的数据将会被挂起，直到当前的TMU运算结束并且输出数据被读取。在数据挂起期间，如果写入新的数据，则新数据覆盖之前被挂起的数据。

# 15.5.3. 输出数据寄存器（TMU_ODATA）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ODATA[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ODATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ODATA[31:0]</td><td>输出数据当TMU运算结束,结果传输进该寄存器。细节参考表15-2. 输出数据配置。</td></tr></table>

# 注意：

1. 当ENDF位置1时，读取该寄存器可以获得TMU运算结果。

2. 当符合配置的读操作完成，ENDF位被硬件自动清0。
