## 26.4. SAI 寄存器

SAI 基地址：0x4001 5800

## 26.4.1. 同步配置寄存器（SAI_SYNCFG）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">SYNO[1:0]</td><td colspan="2">保留</td><td colspan="2">SYNI[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>SYNO[1:0]</td><td>同步输出该位由软件清零或置位。00:无同步输出信号01:音频模块0与其他SAI进行同步10:音频模块1与其他SAI进行同步11:保留。必须在音频模块1和音频模块2失能时,设置这些位。注意:当音频模块配置成SPDIF模式时,选择无同步输出信号。</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>SYNI[1:0]</td><td>同步输入必须在音频模块0和音频模块1失能时,设置这些位。如果将两个音频模块之一定义为与外部SAI在同步模式下工作(SAI_BxCFG0寄存器中的SYNCMOD[1:0]=10),这些位起作用。</td></tr></table>

## 26.4.2. 子模块 x 配置寄存器 0（SAI_BxCFG0）（x = 0, 1）

地址偏移：0x04 + 0x20 * x

复位值：0x0000 0040

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td>MCLKEN</td><td>MOSPR</td><td colspan="6">MDIV[5:0]</td><td>BYPASS</td><td>保留</td><td>DMAEN</td><td>SAIEN</td></tr><tr><td colspan="4"></td><td>rw</td><td>rw</td><td colspan="6">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>ODRIV</td><td>MONO</td><td colspan="2">SYNCMOD[1:0]</td><td>SAMPEDGE</td><td>SHIFTDIR</td><td colspan="3">DATAWD[2:0]</td><td>保留</td><td colspan="2">PROT[1:0]</td><td colspan="2">OPTMOD[1:0]</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27</td><td>MCLKEN</td><td>主时钟使能0: 主时钟使能1: 主时钟独立于 SAIEN 位使能</td></tr><tr><td>26</td><td>MOSPR</td><td>主时钟过采样率0: MCLK = 256 *$F_{fs}$1: MCLK = 512 *$F_{fs}$</td></tr><tr><td>25:20</td><td>MDIV[5:0]</td><td>主时钟分频器0000: 主分频器逻辑旁路否则,其输出频率请参考章节时钟分频器公式(30-1)计算。注意:当 SAI 配置为从机模式时,该控制字段无效。注意:必须在使能 SAI 之前设置此控制字段。</td></tr><tr><td>19</td><td>BYPASS</td><td>时钟分频器逻辑旁路0: 时钟分频器应用于初级和次级分频器逻辑1: 时钟分频器逻辑被旁路</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>DMAEN</td><td>DMA 使能0: DMA 失能1: DMA 使能注意:如果 SAI 被配置为接收器,则必须在 OPTMOD 控制字段之后设置 DMAEN,以避免不必要的 DMA 请求,因为 SAI 在复位后是发送器。</td></tr><tr><td>16</td><td>SAIEN</td><td>SAI 子模块使能0: SAI 子模块失能1: SAI 子模块使能。当 SPI_STAT 中的 TBE 置位时,将会在相应的 DMA 通道上产生一个 DMA 请求。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>ODRIV</td><td>输出驱动0: 当 SAIEN 置 1 时,驱动 SAI 音频子模块输出1: 当 ODRIV 位置 1 时,立即驱动 SAI 音频子模块输出注意:该控制位必须在 SAI 配置后且使能前置 1。</td></tr><tr><td>12</td><td>MONO</td><td>立体声和单声道模式选择0: 立体声模式1: 单声道模式单声道模式要求 slot 数等于 2,在发送器模式下,第一个 slot 的数据被复制到第二个 slot,而在接收器模式下,第二个 slot 的数据被忽略。</td></tr><tr><td>11:10</td><td>SYNCMOD[1:0]</td><td>同步模式00:与其他子块异步01:与其他子块同步,选择该模式时,用户必须配置工作模式为从机10:音频子块与外部 SAI 嵌入式外设同步。在这种情况下,音频子块应配置为从模式11:保留注意:在音频模块失能的情况下配置该位。注意:如果协议选择为 SPDIF,则模式应配置为异步。</td></tr><tr><td>9</td><td>SAMPEDGE</td><td>采样时钟边沿0:在 SCK 下降沿采样数据1:在 SCK 上升沿采样的数据注意:此控制字段在 SPDIF 模式下被忽略。注意:在音频模块失能的情况下配置该位。</td></tr><tr><td>8</td><td>SHIFTDIR</td><td>数据传输移动方向0:数据传输采用高位在前1:数数据传输采用低位在前注意:此控制字段在 AC’ 97 模式下被忽略,因为数据传输被强制为 MSB:此控制字段在 SPDIF 模式下被忽略,因为数据传输被强制为 LSB。</td></tr><tr><td>7:5</td><td>DATAWD[2:0]</td><td>数据宽度000:保留001:保留010:8 位宽011:10 位宽100:16 位宽101:20 位宽110:24 位宽111:32 位宽在压扩模式下,数据宽度由算法本身固定为 8 位宽度。注意:在音频模块失能的情况下配置该位。注意:此控制字段在 SPDIF 模式下被忽略。注意:如果选择 AC’ 97 协议,则只有 16 位或 20 位是可行的,否则无法保证音频子块的行为。</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:2</td><td>PROT[1:0]</td><td>协议选择00:自由协议01:SPDIF 协议10:AC'97 洗衣10:保留自由协议配置允许用户调整所有帧和帧配置选项,以形成他选择的协议,如 I2S、</td></tr></table>

LSB/MSB 对齐、TDM、PCM/DSP 等。注意：在音频模块失能的情况下配置该位。1:0 OPTMOD[1:0] 工作模式选择00：主机发送01：主机接收10：从机发送11：从机接收如果协议选择为 SPDIF，工作模式将被强制配置为主机发送。注意：在音频模块失能的情况下配置该位。

## 26.4.3. 子模块 x 配置寄存器 1（SAI_BxCFG1）（x = 0, 1）

地址偏移：0x08 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CPAMOD[1:0]</td><td colspan="2">CPLMOD</td><td colspan="5">MTFCNT[5:0]</td><td>MTVAL</td><td>MT</td><td>SDOM</td><td>FLUSH</td><td colspan="3">FFTH[2:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:14</td><td>CPAMOD[1:0]</td><td>压缩扩展模式00:不使用压缩扩展模式01:保留.10:Mu-law算法10:A-law算法ITU-T G.711定义了Mu-law和A-law两个主要的压缩扩展算法,它们分别将13位和12位有符号的线性PCM信号编码成8位样本。前者为较高范围信号提供更多分辨率,后者为低信号电平提供更多量化等级。压缩或扩展模式通过OPTMOD[0]控制位进行选择,当音频子模块配置为发送器时,自动应用压缩模式,当音频子模块配置为接收器时,将自动应用扩展模式。补码模式通过CPLMOD控制位进行选择。注意:只有配置TDM协议,才会使用压缩扩展模式</td></tr><tr><td>13</td><td>CPLMOD</td><td>补码模式该控制位用于在压缩扩展模式中选择补码选项0:数据以1的补码表示1:数据以2的补码表示</td></tr><tr><td>12:7</td><td>MTFCNT[5:0]</td><td>静音帧计数器该控制位只有在接收模式中才有用。当接收到连续的静音帧数等于MTFCNT时,MTFDET标志位置位,如果MTFDETIE置'1',则产生中断</td></tr><tr><td>6</td><td>MTVAL</td><td>静音值0:当静音打开时,串行数据线上发送01:当SLOTNUM小于或等于2时,如果静音打开,则在重新数据线上重发上一个帧,否则,在静音帧期间串行数据线上发送0注意:只有当音频子模块配置为发送器时,该控制位才有意义。注意:接收器只能检测0值静音帧,当MTVAL置1并且在静音期间重复发送上一帧时,接收器实际接收了这个值,但静音帧计数器不会计数,同样MTDET标志位也不会置位。</td></tr><tr><td>5</td><td>MT</td><td>静音0:静音模关闭1:静音模式打开注意:只有当音频子模块配置为发送器时,该控制位才有意义,当静音模式打开时,SD的输出取决于MTVAL的配置注意:如果在帧传输期间设置静音模式,静音将会在下个帧生效。</td></tr><tr><td>4</td><td>SDOM</td><td>串行数据输出管理0:在音频帧期间,完全由SAI驱动SD输出1:SD输出在无效slot附近释放注意:如果第一个帧的第一个slot的数据偏移不为0,SD保持释放状态直到第一个有效数据位到达。如果当前帧不是连续传输中的第一个帧,第一个slot的偏移区SD输出是否释放,这取决于上一个帧的最后一个slot的状态。如果上一个slot有效,则驱动偏移区,否则将释放。注意:如果数据偏移区加上数据位宽小于slot宽时,我们将数据最后一位到slot结束之间的区域成为空白区(闲置区),在空白区SD输出是否释放取决于下一个slot是否有效,如果当前slot为最后一个slot,那么它的空白区SD输出行为将取决于当前帧的第一个slot,这与当前帧是否为最后一个帧无关。注意:Slot前的空白区和slot后的偏移区期间SD输出驱动与否,只取决于这个slot。如果这个slot有效,则SD线将被驱动,否则SD线将被释放。</td></tr><tr><td>3</td><td>FLUSH</td><td>FIFO刷新0:无FIFO刷新1:执行FIFO刷新注意:FIFO刷新清除FIFO中的所有数据,并且复位读写指针。当SAI失能时配置FIFO刷新。</td></tr><tr><td>2:0</td><td>FFTH[2:0]</td><td>FIFO阈值000:FIFO为空001:FIFO 1/4满010:FIFO半满011:FIFO 3/4满100:FIFO全满101:保留110:保留</td></tr></table>

111：保留

注意：FIFO阈值和 FIFO 状态（FFSTAT）控制位配合使用来产生 CPU和 DMA 的FIFO 请求（FFREQ）。

## 26.4.4. 子模块 x 帧配置寄存器（SAI_BxFCFG）（x = 0, 1）

地址偏移：0x0C + 0x20 * x

复位值：0x0000 0007

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>FSOST</td><td>FSPL</td><td>FSFUNC</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留.</td><td colspan="7">FSAWD[6:0]</td><td colspan="8">FWD[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>FSOST</td><td>帧同步偏移0: FS有效边沿声明为第一个slot的第一个位开始处1: FS有效边沿声明为当FSOST为0时的FS的前一个位时钟周期。注意:该控制域必须在音频子模块使能之前配置,并且它在AC&#x27;97或SPDIF中是没意义的。</td></tr><tr><td>17</td><td>FSPL</td><td>帧同步有效极性0: FS有效极性为低1: FS有效极性为高注意:该控制位必须在音频子模块使能前配置,并且它在AC&#x27;97或SPDIF中是没意义的。</td></tr><tr><td>16</td><td>FSFUNC</td><td>帧同步功能0: FS只定义帧开始1: FS定义帧开始和通道号注意:该控制位必须在音频子模块使能前配置。注意:当FSFUNC置1时,一个帧中的slot数(SLOTNUM+1)必须为偶数,在这种情况下,一半的slot将会被分派给通道A,另一半的slot被分派给通道B。如果分派到一个通道的所有slot数小于帧宽的一半,则在slot未定义时SD输出线释放,这和SDOM无关。注意:当FSFUNC置1时,FS有效宽度(FSAWD+1)必须配置为帧长的一半。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:8</td><td>FSAWD[6:0]</td><td>帧同步有效宽度注意:该控制位必须在音频子模块使能前配置,并且它在AC&#x27;97模式中是没有意义的。</td></tr></table>

注意：该控制位指定FS 有效宽度为（FSAWD+1）个 SCK时钟周期。

注意：该控制位必须在音频子模块使能前配置，并且它在 AC’97 模式中是没有意义的。

注意：该控制位指定帧宽为（FWD +1）个 SCK 时钟周期，当音频子模块配置为主模式，且 BYPASS=0 时，FWD+1 的值必须等于 8到 256 之间且为 2 的几次幂的一个值。

## 26.4.5. 子模块 x slot 配置寄存器（SAI_BxSCFG）（x = 0, 1）

地址偏移：0x10 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SLOTAV[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="4">SLOTNUM[3:0]</td><td colspan="2">SLOTWD[1:0]</td><td>保留.</td><td colspan="5">DATAOST[4:0]</td></tr><tr><td colspan="8">rw</td><td colspan="3">rw</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>SLOTAV[15:0]</td><td>Slot 激活向量0: Slot 无效1: Slot 有效SLOTAV 向量中的每一个比特位对应到 slot0~15,如果 SLOTNUM 小于 15,则不对 应的比特位被忽略。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在 AC'97 或 SPDIF 模式中没有意义。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:8</td><td>SLOTNUM[3:0]</td><td>一个帧中的 slot 个数一个帧中实际的帧数为(SLOTNUM+1),并且不能超过 16。当 FSFUNC 置 1 时, slot 数必须为偶数,并且均分到两个通道。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在 AC'97 模式中没有意义。</td></tr><tr><td>7:6</td><td>SLOTWD[1:0]</td><td>slot 宽度00: Slot 宽等于数据位宽01: Slot 为 16 位宽10: Slot 为 32 位宽11: 保留.Slot 的位宽必须大于或等于数据位宽才能包含一个数据,否则 SAI 的行为将不能保证正确。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在AC'97或SPDIF模式中没有意义。</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>DATAOST[4:0]</td><td>数据偏移定义了在一个有效slot中第一个数据位的出现位置,在发送模式时,偏移区和空白区的SD输出0或Hi-Z,这取决于SDOM和附近slot的有效状态。在接收模式时,偏移区和空白区的数据内容将会忽略。注意:该控制位必须在音频子模块使能前配置。注意:该控制位在AC'97模式中没有意义。</td></tr></table>

## 26.4.6. 子模块 x 中断使能寄存器（SAI_BxINTEN）（x = 0, 1）

地址偏移：0x14 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FSPDETI E</td><td>FSADETI E</td><td>ACNRDYI E</td><td>FFREQIE</td><td>ERRCKIE</td><td>MTDETIE</td><td>OUERRI E</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FSPDETIE</td><td>帧同步滞后检测中断使能0: 中断失能1: 中断使能如果 FSPDET 和 FSPDETIE 都置 1,则产生中断。注意: 当音频子模块配置为主模式时,该控制位无意义。注意: 该控制位在 AC'97 模式中没有意义。</td></tr><tr><td>5</td><td>FSADETIE</td><td>帧同步提前检测中断使能0: 中断失能1: 中断使能如果 FSADET 和 FSADETIE 都置 1,则产生中断。注意: 当音频子模块配置为主模式时,该控制位无意义。注意: 该控制位在 AC'97 模式中没有意义。</td></tr><tr><td>4</td><td>ACNRDYIE</td><td>音频编解码器未就绪中断使能0: 中断失能1: 中断使能如果 ACNRDY 和 ACNRDYIE 都置 1,则产生中断。注意:当音频子模块配置为接收器时,该控制位才有意义。注意:该控制位只有在选择AC'97模式时才有意义。</td></tr><tr><td>3</td><td>FFREQIE</td><td>FIFO请求中断使能0:中断失能1:中断使能如果FFREQ和FFREQIE都置1,则产生中断。注意:当音频子模块配置为接收器时,OPTMOD必须在FFREQIE使能之前设置,以保证不会产生错误的FIFO请求,因为音频子模块在复位之后默认处于发送模式。</td></tr><tr><td>2</td><td>ERRCKIE</td><td>错误时钟中断使能,该位通过软件置1和清00:中断失能1:中断使能如果ERRCK和ERRCK都置1,则产生中断。注意:该控制位只有当子模块配置为发送器,并且BYPASS置0时才可时钟分频逻辑相关。注意:该控制位只用于TDM模式,在其他模式中是没有意义的。</td></tr><tr><td>1</td><td>MTDETIE</td><td>静音检测中断使能0:中断失能1:中断使能如果MTDET和MTDETIE都置1,则产生中断。注意:该控制位只有在音频子模块配置为接收器时才有意义。</td></tr><tr><td>0</td><td>OUERRIE</td><td>FIFO上溢或下溢中断使能0:中断失能1:中断使能如果OUERR和OUERRIE都置1,则产生中断。</td></tr></table>

## 26.4.7. 子模块 x 状态寄存器（SAI_BxSTAT）（x = 0, 1）

地址偏移：0x18 + 0x20 * x

复位值：0x0000 0008

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td colspan="3">FFSTAT[2:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>FSPDET</td><td>FSADET</td><td>ACNRDY</td><td>FFREQ</td><td>ERRCK</td><td>MTDET</td><td>OUERR</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>FFSTAT[2:0]</td><td>FIFO状态指示FIFO的满/空状态,它由硬件单独控制,根据音频子模块的操作模式有着不同的评估标准。在 OPTMOD 配置为接收器的情况下:000:空001:空</td></tr><tr><td></td><td></td><td>010: 1/4 满011: 1/2 满100: 3/4 满全满101: 全满在 OPTMOD 配置为发送器的情况下:000: 空001: 空&lt; FIFO 级别&lt;= 1/4 满.010: 1/4 满&lt;= FIFO 级别&lt;= 1/2 满011: 1/2 满&lt;= FIFO 级别&lt;= 3/4 满100: 3/4 满&lt;= FIFO 级别&lt; 全满101: 全满</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FSPDET</td><td>帧同步滞后检测0: 收到正确的 FS 边沿1: FS 边沿滞后接收如果 FSPDETIE 置 1, FS 边沿接收滞后将产生中断。该标志位由 FSPDETC 控制位进行清 0。注意: 当音频子模块配置为接收器时,该控制位才有意义</td></tr><tr><td>5</td><td>FSADET</td><td>帧同步提前检测0: 收到正确的 FS 边沿1: FS 边沿提前接收如果 FSADETIE 置 1, FS 边沿接收提前将产生中断。该标志位由 FSADETC 控制位进行清 0。注意: 当音频子模块配置为接收器时,该控制位才有意义。</td></tr><tr><td>4</td><td>ACNRDY</td><td>音频编解码器未就绪0: AC'97 音频编解码器就绪1: AC'97 音频编解码器未就绪每个帧的 TAG slot 的位 15 是 AC'97 音频编解码器就绪指示位,0 表示音频编解码器未就绪,反之,1 表示就绪。如果 ACNRDYIE 置 1, AC'97 音频编解码器未就绪将产生中断。该标志位由 ACNRDYC 控制位进行清 0。注意: 该控制位只有在 AC'97 模式中才有用。</td></tr><tr><td>3</td><td>FFREQ</td><td>FIFO 请求0: 没有 FIFO 请求1: FIFO 写或读请求如果 FFREQIE 置 1, FIFO 请求将产生中断。FIFO 的请求类型取决于音频子模块的配置,当 OPTMOD 配置为发送器,并且所有</td></tr><tr><td>2</td><td>ERRCK</td><td>时钟错误0: 正确的时钟配置1: 错误的时钟配置如果 ERRCKIE 置 1,时钟配置错误将产生中断。该标志位由 ERRCKC 控制位进行清 0。该控制位只有当音频子模块配置为主模式且 BYPASS 置 0 时才有意义。</td></tr><tr><td>1</td><td>MTDET</td><td>静音检测0: 没检测到静音1: 检测到静音如果 MTDETIE 置 1,检测到静音将产生中断。该标志位由 MTDETC 控制位进行清 0。当接收到 slot 全为 0 的帧的个数达到 MTFCNT 中定义的帧数时,静音检测标志位置 1. 当 slot 数小于 2,且 MTVAL 置 1 时,将不能检测到静音,在发送器中,在静音之前的帧将被重复传输。</td></tr><tr><td>0</td><td>OUERR</td><td>上溢或下溢0: 未检测到 FIFO 上溢或下溢1: 检测到 FIFO 上溢或下溢如果 OUERRIE 置 1,FIFO 上溢或下溢将产生中断。该标志位由 OUERRC 控制位进行清 0。当音频子模块配置为接收器时,如果将接收到的数据存入已满 FIFO,则产生 FIFO 上溢。当音频子模块配置为发送时,如果在 FIFO 为空出现传输请求,则产生 FIFO 下溢。</td></tr></table>

## 26.4.8. 子模块 x 中断标志清除寄存器（SAI_BxINTC）（x = 0, 1）

地址偏移：0x1C + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="9">保留</td><td>FSPDET</td><td>FSADET</td><td>ACNRDY</td><td rowspan="2">保留.</td><td rowspan="2">ERRCKC</td><td rowspan="2">MTDETC</td><td rowspan="2">OUERRC</td></tr><tr><td>C</td><td>C</td><td>C</td></tr><tr><td colspan="9"></td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>FSPDETC</td><td>帧同步滞后检测中断清除写1清除FSPDET标志位。注意:该控制位在AC'97模式中没用。注意:读该位将始终返回0。</td></tr><tr><td>5</td><td>FSADETC</td><td>帧同步提前检测中断清除写1清除FSADET标志位。注意:该控制位在AC'97模式中没用。注意:读该位将始终返回0。</td></tr><tr><td>4</td><td>ACNRDYC</td><td>音频编解码器未就绪中断清除写1清除ACNRDY标志位。注意:该控制位只用在AC'97模式中。注意:读该位将始终返回0。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>ERRCKC</td><td>时钟错误中断清除写1清除ERRCK标志位。注意:该控制位只有在音频模块配置为主模式,并且BYPASS置0时才有用。注意:读该位将始终返回0。</td></tr><tr><td>1</td><td>MTDETC</td><td>静音检测中断清除写1清除MTDET标志位。注意:读该位将始终返回0。</td></tr><tr><td>0</td><td>OUERRC</td><td>上溢或下溢中断清除写1清除OUERR标志位。注意:读该位将始终返回0。</td></tr></table>

## 26.4.9. 子模块 x 数据寄存器（SAI_BxDATA）（x = 0, 1）

地址偏移：0x20 + 0x20 * x

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>数据写和读操作直接体现在FIFO中。</td></tr></table>
