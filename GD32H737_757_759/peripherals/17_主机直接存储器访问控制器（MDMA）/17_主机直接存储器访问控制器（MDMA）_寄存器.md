# 17.4. MDMA 寄存器

MDMA 基地址：0x5200 0000

# 17.4.1. 全局中断标志寄存器（MDMA_GINTF）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>GIF15</td><td>GIF14</td><td>GIF13</td><td>GIF12</td><td>GIF11</td><td>GIF10</td><td>GIF9</td><td>GIF8</td><td>GIF7</td><td>GIF6</td><td>GIF5</td><td>GIF4</td><td>GIF3</td><td>GIF2</td><td>GIF1</td><td>GIF0</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>GIFx</td><td>通道 x 全局中断标志(x=0...15)0:通道 x 标志位(BTCF / MBTCF / CHTCF / ERR / TCF)均未置位,或有标志位置位但其相应的中断未使能。1:通道 x BTCF / MBTCF / CHTCF / ERR / TCF 至少有一个标志位置位,并且相应的中断(BTCIE / MBTCIE / CHTCIE / ERRIE / TCIE)已使能。</td></tr></table>

# 17.4.2. 通道 x 状态寄存器 0（MDMA_CHxSTAT0）

x = 0...15，x 为通道编号

地址偏移：0x40 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>REQAF</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>TCF</td><td>BTCF</td><td>MBTCF</td><td>CHTCF</td><td>ERR</td></tr><tr><td colspan="11"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>REQAF</td><td>通道x请求激活标志将MDMA_CHxCTL0寄存器中SWREQ位置1,并且使能CHEN,该位将置1。当</td></tr></table>

<table><tr><td></td><td></td><td>通道x请求完成时,该位由硬件清零。0:通道xMDMA传输未激活。1:通道xMDMA传输激活。</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TCF</td><td>通道x缓冲区传输完成标志硬件置位,软件写MDMA_CHxSTATC相应位为1清零。0:通道x缓冲区传输未完成。1:通道x缓冲区传输完成。</td></tr><tr><td>3</td><td>BTCF</td><td>通道x块传输完成标志硬件置位,软件写MDMA_CHxSTATC相应位为1清零。0:通道x块传输未完成。1:通道x块传输完成。</td></tr><tr><td>2</td><td>MBTCF</td><td>通道x多块传输完成标志硬件置位,软件写MDMA_CHxSTATC相应位为1清零。0:通道x多块传输未完成。1:通道x多块传输完成。</td></tr><tr><td>1</td><td>CHTCF</td><td>通道x通道传输完成标志硬件置位,软件写MDMA_CHxSTATC相应位为1清零。0:通道x传输未完成。1:通道x传输完成。注意:当CHEN写0时,CHTCF位也将置1。</td></tr><tr><td>0</td><td>ERR</td><td>通道x传输错误标志硬件置位,软件写MDMA_CHxSTATC相应位为1清零。0:通道x未发生传输错误。1:通道x发生传输错误。</td></tr></table>

# 17.4.3. 通道 x 状态清除寄存器（MDMA_CHxSTATC）

x = 0...15，x 为通道编号

地址偏移：0x44 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>TCFC</td><td>BTCFC</td><td>MBTCFC</td><td>CHTCFC</td><td>ERRC</td></tr></table>

<table><tr><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td></tr></table>

位/位域 名称 描述

<table><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TCFC</td><td>通道x缓冲区传输完成标志清零0:无影响。1:对该位写1清零MDMA_CHxSTAT0寄存器中TCF位。</td></tr><tr><td>3</td><td>BTCFC</td><td>通道x块传输完成标志清零0:无影响。1:对该位写1清零MDMA_CHxSTAT0寄存器中BTCF位。</td></tr><tr><td>2</td><td>MBTCFC</td><td>通道x多块传输完成标志清零0:无影响。1:对该位写1清零MDMA_CHxSTAT0寄存器中MBTCF位。</td></tr><tr><td>1</td><td>CHTCFC</td><td>通道x传输完成标志清零0:无影响。1:对该位写1清零MDMA_CHxSTAT0寄存器中CHTCF位。</td></tr><tr><td>0</td><td>ERRC</td><td>通道x传输错误标志清零0:无影响。1:对该位写1清零MDMA_CHxSTAT0寄存器中ERR位。</td></tr></table>

# 17.4.4. 通道 x 状态寄存器 1（MDMA_CHxSTAT1）

x = 0...15，x 为通道编号

地址偏移：0x48 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td>BZERR</td><td>ASERR</td><td>MDTERR</td><td>LDTERR</td><td>TERRD</td><td colspan="7">ERRADDR[6:0]</td></tr><tr><td colspan="4"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="3"></td><td colspan="4">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11</td><td>BZERR</td><td>块大小错误标志当块的大小或BTLEN+1不是源或目标数据大小的整数倍时,该位由硬件置1。将MDMA_CHxSTATC寄存器ERRC位写1可清零该位。0:未发生块大小错误。1:发生了块大小错误。</td></tr><tr><td>10</td><td>ASERR</td><td>地址和大小错误标志当地址与数据大小不匹配时,该位由硬件置1。将MDMA_CHxSTATC寄存器ERRC位写1可清零该位。0:未发生地址和大小错误。1:发生了地址和大小错误。</td></tr><tr><td>9</td><td>MDTERR</td><td>掩码数据错误标志当写入掩码数据产生错误时,该位由硬件置1。将MDMA_CHxSTATC寄存器ERRC位写1可清零该位。0:未发生掩码数据错误。1:发生了掩码数据错误。</td></tr><tr><td>8</td><td>LDTERR</td><td>链路数据错误标志当读取块链路数据结构时产生错误,该位由硬件置1。将MDMA_CHxSTATC寄存器ERRC位写1可清零该位。0:未发生链路数据错误。1:发生了链路数据错误。</td></tr><tr><td>7</td><td>TERRD</td><td>传输错误方向标志当通道上传输错误由写访问产生时,该位由硬件置1。0:传输错误由读访问产生。1:传输错误由写访问产生。</td></tr><tr><td>6:0</td><td>ERRADDR[6:0]</td><td>传输错误地址当传输错误发生时,这些位存储错误地址的低7位。绝对错误地址为ERRADDR+SADDR/DADDR。注意:当重载错误发生时,这些位被忽略。</td></tr></table>

# 17.4.5. 通道 x 控制寄存器 0（MDMA_CHxCTL0）

x = 0...15，x 为通道编号

地址偏移：0x4C + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>SWREQ</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>WES</td><td>HWES</td><td>BES</td><td colspan="3">保留</td><td>SMODEN</td><td colspan="2">PRIO[1:0]</td><td>TCIE</td><td>BTCIE</td><td>MBTCIE</td><td>CHTCIE</td><td>ERRIE</td><td>CHEN</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>SWREQ</td><td>软件请求当通道使能时,将该位置 1 将激活通道 x 的请求,MDMA_CHxSTAT0 寄存器中 REQAF 位将置 1。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>WES</td><td>双字中字的顺序交换0:双字中不交换字的顺序,保持小端字节顺序。1:双字中交换字的顺序。注意:如果目标不是双字,则该位忽略。当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>13</td><td>HWES</td><td>字中半字的顺序交换0:字中不交换半字的顺序,保持小端字节顺序。1:字中交换半字的顺序。注意:如果目标不是字或双字,则该位忽略。当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>12</td><td>BES</td><td>半字中字节的顺序交换0:字中不交换半字的顺序,保持小端字节顺序。1:字中交换半字的顺序。注意:如果目标不是半字、字或双字,则该位忽略。当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>SMODEN</td><td>安全模式使能0:安全模式禁能1:安全模式使能该位仅在AHB从机接口处于安全模式下可写。如果SMODEN为0,当前通道的所有寄存器可写。如果SMODEN为1,当前通道的所有寄存器被写保护。注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>7:6</td><td>PRIO[1:0]</td><td>软件优先级软件置1与清零。00:低01:中10:高11:超高注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>5</td><td>TCIE</td><td>缓冲区传输完成中断使能软件置1与清零。0:缓冲区传输完成中断禁能。1:缓冲区传输完成中断使能。</td></tr><tr><td>4</td><td>BTCIE</td><td>块传输完成中断使能软件置1与清零。0:块传输完成中断禁能。1:块传输完成中断使能。</td></tr><tr><td>3</td><td>MBTCIE</td><td>多块传输完成中断使能软件置1与清零。</td></tr></table>

0：多块传输完成中断禁能。

1：多块传输完成中断使能。

2 CHTCIE 通道传输完成中断使能

软件置 1 与清零。

0：通道传输完成中断禁能。

1：通道传输完成中断使能。

1 ERRIE 传输错误中断使能

软件置 1 与清零。

0：传输错误中断禁能。

1：传输错误中断使能。

0 CHEN 通道使能

软件置 1 与清零。

0：通道禁能。

1：通道使能。

注意：当 MDMA 传输完成、发生 AHB/AXI 总线错误、发生 BZERR 错误或 ASERR错误时，该位由硬件清零。

# 17.4.6. 通道 x 配置寄存器（MDMA_CHxCFG）

x = 0...15，x 为通道编号

地址偏移：0x50 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BWMOD</td><td>SWREQ MOD</td><td colspan="2">TRIGMOD[1:0]</td><td colspan="2">PAMOD[1:0]</td><td>PKEN</td><td colspan="7">BTLEN[6:0]</td><td colspan="2">DBURST[2:1]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DBURST[0]</td><td colspan="3">SBURST[2:0]</td><td colspan="2">DIOS[1:0]</td><td colspan="2">SIOS[1:0]</td><td colspan="2">DWIDTH[1:0]</td><td colspan="2">SWIDTH[1:0]</td><td colspan="2">DIMOD[1:0]</td><td colspan="2">SIMOD[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>


位/位域 名称 描述


<table><tr><td>31</td><td>BWMOD</td><td>可缓冲写模式软件置1与清零。0:不可缓冲写。1:可缓冲写。注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>30</td><td>SWREQMOD</td><td>软件请求模式软件置1与清零。0:响应软件请求和硬件请求。</td></tr></table>

1：只响应软件请求。

注意：修改该位将在当前传输完成后生效。

29:28 

TRIGMOD[1:0] 

触发模式

软件置 1 与清零。

00：软件请求或硬件请求触发缓冲区传输。

01：软件请求或硬件请求触发块传输。

10：软件请求或硬件请求触发多块传输。

11：软件请求或硬件请求触发完整数据传输（如链路模式）。

注意：当通道被使能（CHEN=1）时，该位不能被改写。

27:26 

PAMOD[1:0] 

填充和对齐模式

软件置 1 与清零。

<table><tr><td colspan="2">源数据大小大于目标数据大小</td><td colspan="2">源数据大小小于目标数据大小</td></tr><tr><td>00</td><td>右对齐,将源的低字节部分写入目标地址,高字节部分丢弃</td><td>00</td><td>右对齐,不足的位补0</td></tr><tr><td>01</td><td>保留</td><td>01</td><td>右对齐,符号扩展</td></tr><tr><td>10</td><td>左对齐,将源的高字节部分写入目标地址,低字节部分丢弃</td><td>10</td><td>左对齐,不足的位补0</td></tr><tr><td>11</td><td>保留</td><td>11</td><td>保留</td></tr></table>

注意：当包使能（PKEN=1）或源数据大小等于目标数据大小时，该位域无效。当通道被使能（CHEN=1）时，该位域不能被改写。

25 

PKEN 

包使能

软件置 1 与清零。

0：根据 PAMOD[1:0]位域配置的方式将源数据写入目标地址。

1：将源数据通过打包/解包方式以匹配目标数据大小。

注意：当通道被使能（CHEN=1）时，该位不能被改写。

24:18 

BTLEN[6:0] 

缓冲区传输长度

软件置 1 与清零。

单次传输的字节数请参考 。

注意：BTLEN+1 必须是 DWIDTH 和 SWIDTH 的倍数。

17:15 

DBURST[2:0] 

目标传输突发类型

软件置 1 与清零。

000：单一传输。

001：2 拍增量突发传输。

010：4 拍增量突发传输。

011：8 拍增量突发传输。

100：16 拍增量突发传输。

101：32 拍增量突发传输。

110：64 拍增量突发传输。

111：128 拍增量突发传输。

注意：当通道被使能（CHEN=1）时，该位不能被改写。

14:12 SBURST[2:0] 

源传输突发类型

软件置 1 与清零。

000：单一传输。

001：2 拍增量突发传输。

010：4 拍增量突发传输。

011：8 拍增量突发传输。

100：16 拍增量突发传输。

101：32 拍增量突发传输。

110：64 拍增量突发传输。

111：128 拍增量突发传输。

注意：当通道被使能（CHEN=1）时，该位不能被改写。

11:10 DIOS[1:0] 

目标增量偏移

软件置 1 与清零。

00：8 位

01：16 位

10：32 位

11：64 位

注意：当通道被使能（CHEN=1）时，该位不能被改写。如果 DIOS 小于 DWIDTH且 DIMOD 不为 00，结果将不预测。

9:8 SIOS[1:0] 

源增量偏移

软件置 1 与清零。

00：8 位

01：16 位

10：32 位

11：64 位

注意：当通道被使能（CHEN=1）时，该位不能被改写。如果SIOS 小于 SWIDTH 且SIMOD 不为 00，结果将不预测。

7:6 DWIDTH[1:0] 

目标数据大小

软件置 1 与清零。

00：8 位

01：16 位

10：32 位

11：64 位

注意：当通道被使能（CHEN=1）时，该位不能被改写。

5:4 SWIDTH[1:0] 

源数据大小

软件置 1 与清零。

00：8 位

01：16 位

10：32 位

11：64 位

注意：当通道被使能（CHEN=1）时，该位不能被改写。

3:2 DIMOD[1:0] 

目标增量模式

软件置 1 与清零。

00：无增量

01：保留

10：目标地址增量为 DIOS

11：目标地址减量为 DIOS

注意：当通道被使能（CHEN=1）时，该位不能被改写。

1:0 SIMOD[1:0] 

源增量模式

软件置 1 与清零。

00：无增量

01：保留

10：源地址增量为 SIOS

11：源地址减量为 SIOS

注意：当通道被使能（CHEN=1）时，该位不能被改写。

# 17.4.7. 通道 x 块传输配置寄存器（MDMA_CHxBTCFG）

x = 0...15，x 为通道编号

地址偏移：0x54 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12"></td><td>DADDRU M</td><td>SADDRU M</td><td>保留</td><td>TBNUM[1 6]</td></tr><tr><td colspan="12"></td><td>rw</td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TBNUM[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>BRNUM[11:0]</td><td>待传输多块块数注意:当通道被使能(CHEN=1)时,该位域不能被改写。</td></tr><tr><td>19</td><td>DADDRUM</td><td>在多块传输模式下,目标地址更新模式0:DADDR = DADDR + DADDRUV1:DADDR = DADDR - DADDRUV注意:当通道被使能(CHEN=1)时,该位域不能被改写。</td></tr><tr><td>18</td><td>SADDRUM</td><td>在多块传输模式下,源地址更新模式0:SADDR = SADDR + SADDRUV1:SADDR = SADDR - SADDRUV注意:当通道被使能(CHEN=1)时,该位域不能被改写。</td></tr></table>

17 保留 必须保持复位值。

16:0 TBNUM[16:0] 块中待传输字节数

当前块待传输的字节数（0-65536）。在多块传输模式下，当块传输完成后，该位将自动重载第一次编程的值。

注意：当通道被使能（CHEN=1）时，该位域不能被改写。TBNUM 必须是源和目标数据大小的整数倍。

# 17.4.8. 通道 x 源地址寄存器（MDMA_CHxSADDR）

x = 0...15，x 为通道编号

地址偏移：0x58 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SADDR[31:0]</td><td>源地址</td></tr></table>

# 17.4.9. 通道 x 目的地址寄存器（MDMA_CHxDADDR）

x = 0...15，x 为通道编号

地址偏移： $0 { \times } 5 0 + 0 { \times } 4 0 \times { \times }$ 

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DADDR[31:0]</td><td>目标地址</td></tr></table>

# 17.4.10. 通道 x 多块地址更新寄存器（MDMA_CHxMBADDRU）

x = 0...15，x 为通道编号

地址偏移：0x60 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DADDRUV[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SADDRUV[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>DADDRUV[15:0]</td><td>目标地址更新值该位域用于设置块传输结束后,目标地址的增量或减量。为了使 DADDR 与 DWIDTH 对齐,该位域设置的值必须为 DWIDTH 的整数倍。当 BRNUM=0 时,这些位无效。注意:当通道被使能(CHEN=1)时,该位域不能被改写。</td></tr><tr><td>15:0</td><td>SADDRUV[15:0]</td><td>源地址更新值该位用于设置块传输结束后,源地址的增量或减量。为了使 SADDR 与 SWIDTH 对齐,该位设置的值必须为 SWIDTH 的整数倍。当 BRNUM=0 时,这些位无效。注意:当通道被使能(CHEN=1)时,该位域不能被改写。</td></tr></table>

# 17.4.11. 通道 x 链路地址寄存器（MDMA_CHxLADDR）

x = 0...15，x 为通道编号

地址偏移：0x64 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">LADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>LADDR[31:0]</td><td>链路地址如果该位域的值不为 0,则在块 / 多块传输完成后,当前通道的配置寄存器包括MDMA_CHxCFG,MDMA_CHxBTCFG,MDMA_CHxSADDR,MDMA_CHxDADDR,MDMA_CHxMBADDRU,MDMA_CHxLADDR,MDMA_CHxCTL1,MDMA_CHxMADDR 和 MDMA_CHxMDATA 将使用MDMA_CHxLADDR 寄存器中定义的地址 LADDR[31:0]处的数据结构对配置寄存器进行加载。如果该位域的值为 0,MDMA_CHxSTAT0 寄存器中 CHTCF 位将置 1,且 CHEN 将</td></tr></table>

由硬件清零。

注意：1、当通道被使能（CHEN=1）时，该位域不能被改写。

2、LADDR[31:0]的值必须是双字对齐。

# 17.4.12. 通道 x 控制寄存器 1（MDMA_CHxCTL1）

x = 0...15，x 为通道编号

地址偏移：0x68 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>DBSEL</td><td>SBSEL</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">TRIGSEL[5:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>DBSEL</td><td>目标总线选择该位用于设置在写操作时,选择通道x的目标总线。0:通道x的目标总线时系统总线或AXI总线1:通道x的目标总线时AHB总线或TCM注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>16</td><td>SBSEL</td><td>源总线选择该位用于设置在读操作时,选择通道x的源总线。0:通道x的源总线时系统总线或AXI总线1:通道x的源总线时AHB总线或TCM注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr><tr><td>15:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>TRIGSEL[5:0]</td><td>触发选择该位域用于选择通道x的硬件触发源。如果SWREQMOD位为1,则该位忽略。注意:当通道被使能(CHEN=1)时,该位不能被改写。</td></tr></table>

# 17.4.13. 通道 x 掩码地址寄存器（MDMA_CHxMADDR）

x = 0...15，x 为通道编号

地址偏移：0x70 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MADDR[31:0]</td><td>掩码地址当该位域不为0时,通过对MADDR指定的地址写入MDMA_CHxMDATA寄存器中MDATA值会确认DMA请求。</td></tr></table>

# 17.4.14. 通道 x 掩码数据寄存器（MDMA_CHxMDATA）

x = 0...15，x 为通道编号

地址偏移：0x74 + 0x40 × x

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MDATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">MDATA[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>MDATA[31:0]</td><td>掩码数据</td></tr></table>
