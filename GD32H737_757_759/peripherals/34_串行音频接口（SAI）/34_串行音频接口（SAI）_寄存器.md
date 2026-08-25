# 34.4. SAI 寄存器

SAI0 基地址：0x4001 5800

SAI1 基地址：0x4001 5C00

SAI2 基地址：0x4001 6000

# 34.4.1. 同步配置寄存器（SAI_SYNCFG）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">SYNO[1:0]</td><td colspan="2">保留</td><td colspan="2">SYNI[1:0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>SYNO[1:0]</td><td>同步输出该位由软件清零或置位。00:无同步输出信号01:音频模块0与其他SAI进行同步10:音频模块1与其他SAI进行同步11:保留。必须在音频模块1和音频模块2失能时,设置这些位。注意:当音频模块配置成SPDIF模式时,选择无同步输出信号。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>SYNI[1:0]</td><td>同步输入参考表34-2. 外部同步配置。必须在音频模块0和音频模块1失能时,设置这些位。如果将两个音频模块之一定义为与外部SAI在同步模式下工作(SAI_BxCFG0寄存器中的SYNCMOD[1:0]=10),这些位起作用。</td></tr></table>

# 34.4.2. 子模块 x 配置寄存器 0（SAI_BxCFG0）（x = 0, 1）

地址偏移：0x04 + 0x20 * x

复位值：0x0000 0040


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>MCLKEN</td><td>MOSPR</td><td colspan="6">MDIV[5:0]</td><td>BYPASS</td><td>保留</td><td>DMAEN</td><td>SAIEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="6">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>ODRIV</td><td>MONO</td><td colspan="2">SYNCMOD[1:0]</td><td>SAMPEDGE</td><td>SHIFTDIR</td><td colspan="3">DATAWD[2:0]</td><td>保留</td><td colspan="2">PROT[1:0]</td><td colspan="2">OPTMOD[1:0]</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>MCLKEN</td><td>主时钟使能0: 主时钟使能1: 主时钟独立于 SAIEN 位使能</td></tr><tr><td>26</td><td>MOSPR</td><td>主时钟过采样率0: MCLK = 256 * Ffs1: MCLK = 512 *Ffs</td></tr><tr><td>25:20</td><td>MDIV[5:0]</td><td>主时钟分频器0000: 主分频器逻辑旁路否则,其输出频率请参考章节时钟分频器公式(30-1)计算。注意:当 SAI 配置为从机模式时,该控制字段无效。注意:必须在使能 SAI 之前设置此控制字段。</td></tr><tr><td>19</td><td>BYPASS</td><td>时钟分频器逻辑旁路0: 时钟分频器应用于初级和次级分频器逻辑1: 时钟分频器逻辑被旁路</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>DMAEN</td><td>DMA 使能0: DMA 失能1: DMA 使能注意:如果 SAI 被配置为接收器,则必须在 OPTMOD 控制字段之后设置 DMAEN,以避免不必要的 DMA 请求,因为 SAI 在复位后是发送器。</td></tr><tr><td>16</td><td>SAIEN</td><td>SAI 子模块使能0: SAI 子模块失能1: SAI 子模块使能。当 SPI_STAT 中的 TBE 置位时,将会在相应的 DMA 通道上产生一个 DMA 请求。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>ODRIV</td><td>输出驱动0: 当 SAIEN 置 1 时,驱动 SAI 音频子模块输出1: 当 ODRIV 位置 1 时,立即驱动 SAI 音频子模块输出</td></tr></table>

注意：该控制位必须在 SAI 配置后且使能前置 1。

12 MONO 立体声和单声道模式选择

0：立体声模式

1：单声道模式

单声道模式要求 slot 数等于 2，在发送器模式下，第一个 slot 的数据被复制到第二个slot，而在接收器模式下，第二个 slot 的数据被忽略。

11:10 SYNCMOD[1:0] 同步模式

00：与其他子块异步

01：与其他子块同步，选择该模式时，用户必须配置工作模式为从机

10：音频子块与外部 SAI 嵌入式外设同步。 在这种情况下，音频子块应配置为从模式

11：保留

注意：在音频模块失能的情况下配置该位。

注意：如果协议选择为 SPDIF，则模式应配置为异步。

9 SAMPEDGE 采样时钟边沿

0：在 SCK 下降沿采样数据

1：在 SCK 上升沿采样的数据

注意：此控制字段在 SPDIF 模式下被忽略。

注意：在音频模块失能的情况下配置该位。

8 SHIFTDIR 数据传输移动方向

0：数据传输采用高位在前

1：数数据传输采用低位在前

注意：此控制字段在 AC’97 模式下被忽略，因为数据传输被强制为 MSB；此控制字段在 SPDIF 模式下被忽略，因为数据传输被强制为 LSB。

7:5 DATAWD[2:0] 数据宽度

000：保留

001：保留

010：8 位宽

011：10 位宽

100：16 位宽

101：20 位宽

110：24 位宽

111：32 位宽

在压扩模式下，数据宽度由算法本身固定为 8 位宽度。

注意：在音频模块失能的情况下配置该位。

注意：此控制字段在 SPDIF 模式下被忽略。

注意：如果选择 AC’97 协议，则只有 16 位或 20 位是可行的，否则无法保证音频子块的行为。

4 保留 必须保持复位值。

3:2 PROT[1:0] 协议选择

00：自由协议

01：SPDIF 协议

10：AC'97 洗衣

10：保留

自由协议配置允许用户调整所有帧和帧配置选项，以形成他选择的协议，如 I2S、LSB/MSB 对齐、TDM、PCM/DSP 等。

注意：在音频模块失能的情况下配置该位。

1:0 OPTMOD[1:0] 工作模式选择

00：主机发送

01：主机接收

10：从机发送

11：从机接收

如果协议选择为 SPDIF，工作模式将被强制配置为主机发送。

注意：在音频模块失能的情况下配置该位。

# 34.4.3. 子模块 x 配置寄存器 1（SAI_BxCFG1）（x = 0, 1）

地址偏移：0x08 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CPAMOD[1:0]</td><td colspan="2">CPLMOD</td><td colspan="5">MTFCNT[5:0]</td><td>MTVAL</td><td>MT</td><td>SDOM</td><td>FLUSH</td><td colspan="3">FFTH[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:14</td><td>CPAMOD[1:0]</td><td>压缩扩展模式00:不使用压缩扩展模式01:保留.10:Mu-law算法11:A-law算法ITU-T G.711定义了Mu-law和A-law两个主要的压缩扩展算法,它们分别将13位和12位有符号的线性PCM信号编码成8位样本。前者为较高范围信号提供更多分辨率,后者为低信号电平提供更多量化等级。压缩或扩展模式通过OPTMOD[0]控制位进行选择,当音频子模块配置为发送器时,自动应用压缩模式,当音频子模块配置为接收器时,将自动应用扩展模式。补码模式通过CPLMOD控制位进行选择。注意:只有配置TDM协议,才会使用压缩扩展模式</td></tr><tr><td>13</td><td>CPLMOD</td><td>补码模式该控制位用于在压缩扩展模式中选择补码选项</td></tr></table>

0：数据以 1 的补码表示

1：数据以 2 的补码表示

<table><tr><td>12:7</td><td>MTFCNT[5:0]</td><td>静音帧计数器该控制位只有在接收模式中才有用。当接收到连续的静音帧数等于 MTFCNT 时,MTFDET 标志位置位,如果 MTFDETIE 置&#x27;1&#x27;,则产生中断</td></tr><tr><td>6</td><td>MTVAL</td><td>静音值0:当静音打开时,串行数据线上发送 01:当 SLOTNUM 小于或等于 2 时,如果静音打开,则在重新数据线上重发上一个帧,否则,在静音帧期间串行数据线上发送 0注意:只有当音频子模块配置为发送器时,该控制位才有意义。注意:接收器只能检测 0 值静音帧,当 MTVAL 置 1 并且在静音期间重复发送上一帧时,接收器实际接收了这个值,但静音帧计数器不会计数,同样 MTDET 标志位也不会置位。</td></tr><tr><td>5</td><td>MT</td><td>静音0:静音模式打开1:静音模式关闭注意:只有当音频子模块配置为发送器时,该控制位才有意义,当静音模式打开时,SD 的输出取决于 MTVAL 的配置注意:如果在帧传输期间设置静音模式,静音将会在下个帧生效。</td></tr><tr><td>4</td><td>SDOM</td><td>串行数据输出管理0:在音频帧期间,完全由 SAI 驱动 SD 输出1:SD 输出在无效 slot 附近释放注意:如果第一个帧的第一个 slot 的数据偏移不为 0,SD 保持释放状态直到第一个有效数据位到达。如果当前帧不是连续传输中的第一个帧,第一个 slot 的偏移区 SD 输出是否释放,这取决于上一个帧的最后一个 slot 的状态。如果上一个 slot 有效,则驱动偏移区,否则将释放。注意:如果数据偏移区加上数据位宽小于 slot 宽时,我们将数据最后一位到 slot 结束之间的区域成为空白区(闲置区),在空白区 SD 输出是否释放取决于下一个 slot 是否有效,如果当前 slot 为最后一个 slot,那么它的空白区 SD 输出行为将取决于当前帧的第一个 slot,这与当前帧是否为最后一个帧无关。注意:Slot 前的空白区和 slot 后的偏移区期间 SD 输出驱动与否,只取决于这个 slot。如果这个 slot 有效,则 SD 线将被驱动,否则 SD 线将被释放。</td></tr><tr><td>3</td><td>FLUSH</td><td>FIFO 刷新0:无 FIFO 刷新1:执行 FIFO 刷新注意:FIFO 刷新清除 FIFO 中的所有数据,并且复位读写指针。当 SAI 失能时配置 FIFO 刷新。</td></tr><tr><td>2:0</td><td>FFTH[2:0]</td><td>FIFO 阈值000:FIFO 为空001:FIFO 1/4 满010:FIFO 半满</td></tr></table>

011：FIFO 3/4 满

100：FIFO 全满

101：保留

110：保留

111：保留

注意：FIFO阈值和 FIFO 状态（FFSTAT）控制位配合使用来产生 CPU和 DMA 的FIFO 请求（FFREQ）。

# 34.4.4. 子模块 x 帧配置寄存器（SAI_BxFCFG）（x = 0, 1）

地址偏移：0x0C + 0x20 * x

复位值：0x0000 0007

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>FSOST</td><td>FSPL</td><td>FSFUNC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留.</td><td colspan="7">FSAWD[6:0]</td><td colspan="8">FWD[7:0]</td></tr><tr><td></td><td colspan="7">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>FSOST</td><td>帧同步偏移0: FS有效边沿声明为第一个slot的第一个位开始处1: FS有效边沿声明为当FSOST为0时的FS的前一个位时钟周期。注意:该控制域必须在音频子模块使能之前配置,并且它在AC'97或SPDIF中是没意义的。</td></tr><tr><td>17</td><td>FSPL</td><td>帧同步有效极性0: FS有效极性为低1: FS有效极性为高注意:该控制位必须在音频子模块使能前配置,并且它在AC'97或SPDIF中是没意义的。</td></tr><tr><td>16</td><td>FSFUNC</td><td>帧同步功能0: FS只定义帧开始1: FS定义帧开始和通道号注意:该控制位必须在音频子模块使能前配置。注意:当FSFUNC置1时,一个帧中的slot数(SLOTNUM+1)必须为偶数,在这种情况下,一半的slot将会被分派给通道A,另一半的slot被分派给通道B。如果分派到一个通道的所有slot数小于帧宽的一半,则在slot未定义时SD输出线释放,这和SDOM无关。注意:当FSFUNC置1时,FS有效宽度(FSAWD+1)必须配置为帧长的一半。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:8</td><td>FSAWD[6:0]</td><td>帧同步有效宽度注意:该控制位必须在音频子模块使能前配置,并且它在AC'97模式中是没有意义的。注意:该控制位指定FS有效宽度为(FSAWD+1)个SCK时钟周期。</td></tr><tr><td>7:0</td><td>FWD[7:0]</td><td>帧宽度注意:该控制位必须在音频子模块使能前配置,并且它在AC'97模式中是没有意义的。注意:该控制位指定帧宽为(FWD+1)个SCK时钟周期,当音频子模块配置为主模式,且BYPASS=0时,FWD+1的值必须等于8到256之间且为2的几次幂的一个值。</td></tr></table>

# 34.4.5. 子模块 x slot 配置寄存器（SAI_BxSCFG）（x = 0, 1）

地址偏移：0x10 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SLOTAV[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">SLOTNUM[3:0]</td><td colspan="2">SLOTWD[1:0]</td><td colspan="2">保留.</td><td colspan="4">DATAOST[4:0]</td></tr><tr><td colspan="8">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>SLOTAV[15:0]</td><td>Slot 激活向量0: Slot 无效1: Slot 有效SLOTAV 向量中的每一个比特位对应到 slot0~15,如果 SLOTNUM 小于 15,则不对 应的比特位被忽略。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在 AC&#x27;97 或 SPDIF 模式中没有意义。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>SLOTNUM[3:0]</td><td>一个帧中的 slot 个数一个帧中实际的帧数为(SLOTNUM+1),并且不能超过 16。当 FSFUNC 置 1 时, slot 数必须为偶数,并且均分到两个通道。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在 AC&#x27;97 模式中没有意义。</td></tr><tr><td>7:6</td><td>SLOTWD[1:0]</td><td>slot 宽度00: Slot 宽等于数据位宽01: Slot 为 16 位宽</td></tr></table>
