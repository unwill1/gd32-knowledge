## 34.4. HPDF 寄存器

HPDF 访问基地址：0x4001 7000

## 34.4.1. HPDF 通道 x 寄存器（x = 0…7）

通道 x 控制寄存器（HPDF_CHxCTL）

地址偏移：0x00 + 0x20 * x，（x = 0…7）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>HPDFEN</td><td>CKOUTS EL</td><td>CKOUTD M</td><td colspan="5">保留</td><td colspan="8">CKOUTDIV[7:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="8">rw</td><td colspan="6">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">DPM[1:0]</td><td colspan="2">CMSD[1:0]</td><td colspan="3">保留</td><td>CHPINSE L</td><td>CHEN</td><td>CKLEN</td><td>MMEN</td><td>保留</td><td colspan="2">SPICKSS[1:0]</td><td colspan="2">SITYP[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>HPDFEN</td><td>HPDF 全局使能0:禁止 HPDF1:使能 HPDF如果 HPDFEN=0,则复位 HPDF_FLTySTAT 寄存器和 HPDF_FLTyTMSTAT 寄存器。此位仅在 HPDF_CH0CTL 寄存器中有效。</td></tr><tr><td>30</td><td>CKOUTSEL</td><td>串行输出时钟源选择0:CK_HPDF 时钟作为串行输出时钟源1:CK_HPDFAUDIO 时钟作为串行输出时钟源此位仅在 HPDF_CH0CTL 寄存器中有效。</td></tr><tr><td>29</td><td>CKOUTDM</td><td>串行时钟输出占空比模式0:禁止串行时钟输出占空比模式1:使能串行时钟输出占空比模式,占空比为 1:1。当 HPDFEN=0,此位才能修改。此位仅在 HPDF_CH0CTL 寄存器中有效。</td></tr><tr><td>28:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>CKOUTDIV[7:0]</td><td>串行输出时钟预分频器0:禁止串行输出时钟1~255:串行输出时钟的分频系数为 CKOUTDIV+1CKOUTDIV 还定义了时钟丢失检测的阈值。当 HPDF 被禁止时 HPDENF=0,才能修改 CKOUTDIV 的值。HPDF 禁止后,在个 HPDF 时钟内,输出时钟信号(CKOUT)变为低电平状态。此位仅在 HPDF_CH0CTL 寄存器中有效。</td></tr><tr><td>15:14</td><td>DPM[1:0]</td><td>并行输入数据封装模式00:标准模式01:交错模式10:双通道模式11:保留数据封装模式的详细介绍请参考并行数据封装模式只有当 CHEN=0 时,此位域才能被修改。</td></tr><tr><td>13:12</td><td>CMSD[1:0]</td><td>选择复用通道 x 输入数据源00:串行输入作为复用通道 x 输入数据源01:内部模数转换器 ADCx 作为复用通道 x 输入数据源10:HPDF_CHxPDI 寄存器中内部数据作为复用通道 x 输入数据源11:保留当此位域的值为零时,HPDF_CHxPDI 寄存器被写保护。只有当 CHEN=0 时,此位域才能修改。</td></tr><tr><td>11:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CHPINSEL</td><td>通道输入引脚选择0:选择当前通道 x 的引脚作为通道输入引脚1:选择下个通道 x+1 的引脚作为通道输入引脚只有当 CHEN=0 时,此位才能被修改。</td></tr><tr><td>7</td><td>CHEN</td><td>通道 x 使能0:禁止通道 x1:使能通道 x如果通道 x 使能,该通道会根据已有的配置开始接收串行数据。</td></tr><tr><td>6</td><td>CKLEN</td><td>时钟丢失检测使能0:禁止时钟丢失检测1:使能时钟丢失检测</td></tr><tr><td>5</td><td>MMEN</td><td>故障监视器使能0:禁止故障监视器1:使能故障监视器</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:2</td><td>SPICKSS[1:0]</td><td>SPI接口时钟源选择00:选择外部输入时钟(CKINx)作为SPI时钟源-由SITYP[1:0]位域决定采样点01:选择内部输出时钟(CKOUT)作为SPI时钟源-由SITYP[1:0]位域决定采样点10:选择内部输出时钟(CKOUT)作为SPI时钟源-采样点在CKOUT信号每第二个下降沿11:选择内部输出时钟(CKOUT)作为SPI时钟源-采样点在CKOUT信号每第二个上升沿只有当CHEN=0时,此位域才能被修改。</td></tr><tr><td>1:0</td><td>SITYP[1:0]</td><td>串行接口类型00:SPI接口,上升沿采样数据。01:SPI接口,下降沿采样数据。10:曼切斯特编码接口:上升沿=逻辑0,下降沿=逻辑1。11:曼切斯特编码接口:上升沿=逻辑1,下降沿=逻辑0。只有当CHEN=0时,此位域才能修改。</td></tr></table>

## 通道 x 配置寄存器 0（HPDF_CHxCFG0）

地址偏移：0x04 + 0x20 * x，（x = 0…7）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CALOFF[23:8]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">CALOFF[7:0]</td><td colspan="5">DTRS[4:0]</td><td colspan="3">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>CALOFF[23:0]</td><td>24 位偏移校正通道的每一次转换数据后必须执行偏移校正。此位域值由软件写入</td></tr><tr><td>7:3</td><td>DTRS[4:0]</td><td>数据右移位数0~31:该值表示数据执行右移的位数数据移位在偏移校正之间执行,数据移位将结果四舍五入到最接近的整数值,并保留符号位。只有当 HPDF_CHxCTL 寄存器中的 CHEN=0 时,此位域才能被修改。</td></tr></table>

<table><tr><td>2:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

通道 x 配置寄存器 1（HPDF_CHxCFG1）

地址偏移： $0 { \times } 0 8 + 0 { \times } 2 0 ^ { \star } { \bf x } , ~ ( { \bf x } = 0 . . . 7 )$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="2">TMSFO[1:0]</td><td>保留</td><td colspan="5">TMFOR[4:0]</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">MMBSD[3:0]</td><td colspan="4">保留</td><td colspan="8">MMCT[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:22</td><td>TMSFO[1:0]</td><td>阈值监视器 Sinc 滤波器阶数00: FastSinc 滤波器01: <eq>Sinc^1</eq> 滤波器10: <eq>Sinc^2</eq> 滤波器11: <eq>Sinc^3</eq> 滤波器只有当 HPDF_CHxCTL 寄存器中的 CHEN=0 时,此位域才能被修改。</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>TMFOR[4:0]</td><td>阈值监视器 Sinc 滤波器过采样率(抽取率)0~31: 滤波器的抽取率为 TMFOR[4:0] + 1如果 TMFOR=0,则滤波器被旁路只有当 HPDF_CHxCTL 寄存器中的 CHEN=0 时,此位域才能被修改。</td></tr><tr><td>15:12</td><td>MMBSD[3:0]</td><td>故障监视器断路信号分配MMBSD[i] = 0: 断路信号 BREAK[i]未分配至通道 x 故障监视器。MMBSD[i] = 1: 断路信号 BREAK[i]已分配至通道 x 故障监视器。</td></tr><tr><td>11:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>MMCT[7:0]</td><td>故障监视器阈值此位域的值表示故障监视器的计数器阈值,该值由软件写入。如果故障监视器的计数器值达到阈值,则通道上产生故障监视事件。</td></tr></table>

## 通道 x阈值监视器滤波器数据寄存器（HPDF_CHxTMFDT）

地址偏移：0x0C + 0x20 * x，（x = 0…7）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TMDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>TMDATA[15:0]</td><td>阈值监视器数据此数据来自阈值监视器的滤波器,该通道进行连续的数据转换。</td></tr></table>

## 通道 x 并行数据输入寄存器（HPDF_CHxPDI）

地址偏移：0x10 + 0x20 * x，（x = 0…7）

复位值：0x0000 0000

该寄存器只能按半字（16 位）或字（32 位）访问。

HPDF 模块的滤波器将对该寄存包含的 16 位数据进行滤波处理。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATAIN1[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATAIN0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>DATAIN1[15:0]</td><td>通道 x 或通道 x+1 的输入数据通过 CPU/DMA 的方式写入数据如果 DPM[1:0]=0(标准模式),DATAIN1[15:0]被写保护。如果 DPM[1:0]=1(交错模式),通道 x 的第二采样数据被保存到 DATAIN1[15:0]。通道 x 的第一个采样被保存到 DATAIN0[15:0]。HPDF_FTLx 滤波器依次读取两个采样。如果 DPM[1:0]=2(双通道模式):通道 0:DATAIN1[15:0]中保存的采样数据被自动复制到通道 1 的 DATAIN0[15:0]位域中。通道1:DATAIN1[15:0]被写保护。并行数据的详细操作模式请参考并行数据封装模式。DATAIN1[15:0]采用16位有符号格式。</td></tr><tr><td>15:0</td><td>DATAIN0[15:0]</td><td>通道x的输入数据通过CPU/DMA的方式写入数据如果DPM[1:0]=0(标准模式),通道x的数据采样保存在DATAIN0[15:0]位域。如果DPM[1:0]=1(交错模式),通道x的第二采样数据被保存到DATAIN1[15:0]。通道x的第一个采样被保存到DATAIN0[15:0]。HPDF_FTLx滤波器依次读取两个采样。如果DPM[1:0]=2(双通道模式):通道0:DATAIN0[15:0]位域的数据用于当前通道x。通道1:DATAIN0[15:0]被写保护。并行数据的详细操作模式请参考并行数据封装模式。DATAIN0[15:0]采用16位有符号格式。</td></tr></table>

## 通道 x 跳频寄存器（HPDF_CHxPS）

地址偏移：0x14 + 0x20 * x，（x = 0…7）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">PLSK[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>PLSK[5:0]</td><td>输入数据跳频功能0~63:该值表示将要跳过的串行输入采样当此位域被写入非零的值时,跳频功能会立即执行。读取该位域,返回当前跳频剩余未执行的值。当PLSK[5:0]不为零时,仍可更新其值。</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>TMFM</td><td>FAST</td><td colspan="2">保留</td><td colspan="3">RCS[2:0]</td><td colspan="2">保留</td><td>RCDMAEN</td><td>保留</td><td>RCSYN</td><td>RCCM</td><td>SRCS</td><td>保留</td></tr><tr><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rt_w</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="2">ICTEEN[1:0]</td><td colspan="5">ICTSSEL[4:0]</td><td colspan="2">保留</td><td>ICDMAEN</td><td>SCMOD</td><td>ICSYN</td><td>保留</td><td>SICC</td><td>FLTEN</td></tr><tr><td></td><td colspan="4">rw</td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rt_w</td><td>rw</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>30</td><td colspan="4">TMFM</td><td colspan="11">阈值监视器快速模式0:阈值监视器监视的数据为最终数据,最终数据为执行过偏移校正和右移位后的数据。1:阈值监视器监视的数据为通道串行输入数据</td></tr><tr><td>29</td><td colspan="4">FAST</td><td colspan="11">规则转换的快速转换模式0:禁止快速转换模式1:使能快速转换模式如果使能快速转换模式,在规则转换的连续模式下,每次转换速度快于标志转换速度,但首次转换除外。该位对非连续转换没有影响。只有当 FLTEN=0 时,此位才能被修改。</td></tr><tr><td>28:27</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>26:24</td><td colspan="4">RCS[2:0]</td><td colspan="11">选择规则转换通道0:通道 0 作为规则转换通道1:通道 1 作为规则转换通道...7:通道 7 作为规则转换通道当 RCPF=1 时,写此位,被选中的通道在下一个规则转换开始转换。</td></tr><tr><td>23:22</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr></table>

## 34.4.2. HPDF 滤波器 y 寄存器（y = 0…3）

滤波器 y 控制寄存器 0（HPDF_FLTyCTL0）

地址偏移：0x100 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>21</td><td>RCDMAEN</td><td>使能读取规则转换数据的DMA0:禁止DMA读取规则转换数据1:使能DMA读取规则转换数据只有当FLTEN=0时,此位才能被修改。</td></tr><tr><td>20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>RCSYN</td><td>同步启动规则转换0:禁止同步启动规则转换1:使用同步启动规则转换如果HPDF_FLT0CTL0寄存器中的RCSYN=1,其他HPDF_FLTyCTL0中RCSYN=1的规则通道同步启动。只有当FLTEN=0时,此位才能被修改。</td></tr><tr><td>18</td><td>RCCM</td><td>规则转换连续模式0:每个规则转换请求,只执行一次规则通道转换1:每个规则转换请求,重复执行规则通道转换在规则转换的连续模式下,清零此位,连续模式立即停止。</td></tr><tr><td>17</td><td>SRCS</td><td>软件启动规则转换0:无影响1:产生一个启动规则转换请求如果RCPF=1,对此位的写操操作是无效的。如果RCSYN=1,此位置1将启动同步规则转换。读此位,得到的值始终为零</td></tr><tr><td>16:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:13</td><td>ICTEEN[1:0]</td><td>注入转换触发边沿使能00:禁止触发检测01:触发信号的每个上升沿产生启动注入转换请求10:触发信号的每个下降沿产生启动注入转换请求11:触发信号的每个边沿(上升沿和下降沿)产生启动注入转换请求只有当FLTEN=0时,此位域才能被修改。</td></tr><tr><td>12:8</td><td>ICTSSEL[4:0]</td><td>注入转换触发信号选择0x00~0x1F:该值表示选择不同的触发信号开始转换产生一个触发信号到同步启动触发的最大延迟为1个fHPDFCLK时钟周期,异步触发延时为2-3个fHPDFCLK时钟周期。只有当FLTEN=0时,此位域才能被修改。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ICDMAEN</td><td>使能读取注入转换数据的DMA0:禁止DMA读取注入转换数据1:使能DMA读取注入转换数据只有当FLTEN=0时,此位才能被修改。</td></tr><tr><td>4</td><td>SCMOD</td><td>注入转换扫描转换模式0:对注入组通道执行一次转换,然后选中注入组的下一个通道1:选择注入组最小编号通道开始,对注入组通道依次执行连续转换如果SCMOD=0,对IGCSEL位写操作将会导致通道选择复位为注入组中的最小通道。只有当FLTEN=0时,此位才能被修改。</td></tr><tr><td>3</td><td>ICSYN</td><td>同步启动注入转换0:禁止启动与HPDF_FLT0CTL0同步注入的转换1:在HPDF_FLT0CTL0中SICC触发时,在HPDF_FLTy中同步启动注入转换。只有当FLTEN=0时,此位才能被修改。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SICC</td><td>启动注入组转换0:没有影响1:产生一个注入组转换请求如果ICPF=1,对此位写操作是无效的。如果ICSYN=1,此位置1,将启动同步注入组转换。读此位,得到的值始终为零</td></tr><tr><td>0</td><td>FLTEN</td><td>滤波器y使能0:禁止滤波器y1:使能滤波器y如果滤波器y使能,滤波器y根据配置立即开始工作。如果滤波器y禁止,滤波器y所有的转换和功能都立即停止,同时HPDF_FLTySTAT和HPDF_FLTyTMSTAT寄存器都被复位。</td></tr></table>

## 滤波器 y 控制寄存器 1（HPDF_FLTyCTL1）

地址偏移：0x104 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">TMCHEN[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">EMCS[7:0]</td><td>保留</td><td>CKLIE</td><td>MMIE</td><td>TMIE</td><td>RCDOIE</td><td>ICDOIE</td><td>RCEIE</td><td>ICEIE</td></tr><tr><td colspan="8">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>TMCHEN[7:0]</td><td>阈值监视器通道使能此位域决定阈值监视器持续监视的通道TMCHEN[x] = 0:使能阈值监视器y监视通道xTMCHEN[x] = 1:禁止阈值监视器y监视通道x</td></tr><tr><td>15:8</td><td>EMCS[7:0]</td><td>极值监视器通道选择此位域决定极值监视器要采样的通道EMCS[x] = 0:极值监视器y不监视通道x的数据EMCS[x] = 1:极值监视器y监视通道x的数据</td></tr><tr><td>7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>CKLIE</td><td>时钟丢失中断使能0:禁止时钟丢失中断1:使能时钟丢失中断此位仅在HPDF_FLT0CTL1寄存器中有效。</td></tr><tr><td>5</td><td>MMIE</td><td>故障监视器中断使能0:禁止故障监视器中断1:使能故障监视器中断此位仅在HPDF_FLT0CTL1寄存器中有效。</td></tr><tr><td>4</td><td>TMIE</td><td>阈值监视器中断使能0:禁止阈值监视器中断1:使能阈值监视器中断</td></tr><tr><td>3</td><td>RCDOIE</td><td>规则转换数据溢出中断使能0:禁止规则转换数据溢出中断1:使能规则转换数据溢出中断</td></tr><tr><td>2</td><td>ICDOIE</td><td>注入转换数据溢出中断使能0:禁止注入转换数据溢出中断1:使能注入转换数据溢出中断</td></tr><tr><td>1</td><td>RCEIE</td><td>规则转换结束中断使能0:禁止规则转换结束中断1:使能规则转换结束中断</td></tr><tr><td>0</td><td>ICEIE</td><td>注入转换结束中断使能0:禁止注入转换结束中断1:使能注入转换结束中断</td></tr></table>

## 滤波器 y 状态寄存器（HPDF_FLTySTAT）

地址偏移：0x108 + 0x80 * y，（y = 0…3）

复位值：0x0003 0000

该寄存器只能按字（32 位）访问。

当 FTLEN=0 时，HPDF_FLTySTAT 寄存器被复位。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">MMF[7:0]</td><td colspan="8">CKLF[7:0]</td></tr><tr><td colspan="8">r</td><td colspan="8">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>RCPF</td><td>ICPF</td><td colspan="8">保留</td><td>TMEOF</td><td>RCDOF</td><td>ICDOF</td><td>RCEF</td><td>ICEF</td></tr><tr><td>r</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>MMF[7:0]</td><td>故障监视器标志MMF[x]=0:通道x没有产生故障事件MMF[x]=1:通道x产生故障事件此位域由硬件置位,可通过HPDF_FLTyINTC中的MMFC[7:0]位域清零。通过禁止通道CHEN=0,该位域由硬件清零。此位域仅在HPDF_FTL0STAT寄存器中有效。</td></tr><tr><td>23:16</td><td>CKLF[7:0]</td><td>时钟丢失标志CKLF[x]=0:通道x的时钟未丢失CKLF[x]=1:通道x的时钟丢失当CHEN=0时或串行接口尚未同步时,由硬件保持置位状态。串行接口同步完成后,若通道x的时钟丢失,CKLF[7:0]位域中相应的位由硬件置位。通过置位HPDF_FLTyINTC中的CKLFC[7:0]位域,可清除CKLF[7:0]位域中相应的位。此位仅在HPDF_FTL0STAT寄存器中有效。</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>RCPF</td><td>规则转换正在进行标志0:没有规则转换请求产生1:规则转换正在进行或一个规则转换请求被挂起如果RCPF=1,将忽略启动规则转换的请求。当向SRCS位写1,RCPF被立即置位。</td></tr><tr><td>13</td><td>ICPF</td><td>注入转换正在进行标志0:没有注入转换请求产生(软件或触发方式均未有)1:规注入转换正在进行或一个注入转换请求被挂起如果ICPF=1,将忽略启动注入转换的请求。当向SICC位写1,ICPF被立即置位。</td></tr><tr><td>12:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>TMEOF</td><td>阈值监视器事件产生标志0:没有阈值监视器事件产生1:当检测数据超过阈值,阈值监视器产生阈值监视器事件此位由硬件置位,通过清零 HPDF_FLTyTMSTAT 寄存器中的 HTF[7:0]和 LTF[7:0]位域将此位清零。</td></tr><tr><td>3</td><td>RCDOF</td><td>规则转换数据溢出标志0:没有规则转换数据溢出产生1:产生规则转换数据溢出如果此位置位,表示规则转换已经完成,RCEF 也已经置位,FLTyRDATA 不受溢出影响。此位由硬件置位,通过置位 HPDF_FLTyINTC 中的 RCDOFC 位,可清除此位。</td></tr><tr><td>2</td><td>ICDOF</td><td>注入转换溢出标志0:没有注入转换数据溢出产生1:产生注入转换数据溢出如果此位置位,表示规则转换已经完成,ICEF 也已经置位,FLTyIDATA 不受溢出影响。此位由硬件置位,通过置位 HPDF_FLTyINTC 中的 ICDOFC 位,可清除此位。.</td></tr><tr><td>1</td><td>RCEF</td><td>规则转结束标志0:未完成规则转换1:完成规则转换如果 RCEF=1,表示转换数据可以被读取此位由硬件置 1,当通过软件或 DMA 方式读 HPDF_FLTyRDATA 寄存器时,此位被清零。</td></tr><tr><td>0</td><td>ICEF</td><td>注入转结束标志0:未完成注入转换1:完成注入转换如果 ICEF=1,表示转换数据可以被读取此位由硬件置 1,当通过软件或 DMA 方式读 HPDF_FLTyIDATA 寄存器时,此位被清零。</td></tr></table>

## 滤波器 y 中断标志清除寄存器（HPDF_FLTyINTC）

地址偏移：0x10C + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

注：读 HPDF_FLTyINTC 寄存器中的位，得到值始终为 0。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">MMFC[7:0]</td><td colspan="8">CKLFC[7:0]</td></tr><tr><td colspan="8">rc_w1</td><td colspan="8">rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>RCDOFC</td><td>ICDOFC</td><td colspan="2">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>MMFC[7:0]</td><td>清除故障监视器标志MMFC[x]=0:没有影响MMFC[x]=1:清除通道x的故障监视器标志此位仅在HPDF_FLT0INTC寄存器中有效(滤波器y=0)</td></tr><tr><td>23:16</td><td>CKLFC[7:0]</td><td>清除时钟丢失标志CKLFC[x]=0:没有影响CKLFC[x]=1:清除通道x的时钟丢失标志当串行接口尚未完成时钟同步,时钟丢失标志被置位,此时不能通过CKLFC[7:0]清除时钟丢失标志。此位仅在HPDF_FLT0INTC寄存器中有效(滤波器y=0)</td></tr><tr><td>15:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>RCDOFC</td><td>清除规则转换数据溢出标志0:没有影响1:清除规则转换数据溢出标志RCDOF</td></tr><tr><td>2</td><td>ICDOFC</td><td>清除注入转换数据溢出标志0:没有影响1:清除注入转换数据溢出标志ICDOF</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>


滤波器 y 注入组通道选择寄存器（HPDF_FLTyIGCS）



地址偏移： $0 { \times } 1 1 0 + 0 { \times } 8 0 ^ { \star } \ y , ~ ( \ y = 0 . . . 3 )$



复位值：0x0000 0001



该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>15</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">IGCSEL[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>IGCSEL[7:0]</td><td>注入组通道选择ICGSEL[x]=0:通道x不属于注入组ICGSEL[x]=1:通道x属于注入组如果SCMOD=1,由最小编号的通道开始,依次转换每一个所选通道。如果SCMOD=0,只转换其中一个所选通道,然后选择下一个通道。当SCMOD=0时,对IGCSEL[7:0]写操作将通道选择复位为最小编号通道。注入组中必须至少有1个通道,所有将IGCSEL[7:0]变为0的写操作都被忽略。</td></tr></table>

## 滤波器 y SINC 滤波器配置寄存器（HPDF_FLTySFCFG）

地址偏移：0x114 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">SFO[2:0]</td><td colspan="3">保留</td><td colspan="10">SFOR[9:0]</td></tr><tr><td colspan="6">rw</td><td colspan="10">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">IOR[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td rowspan="9">31:29</td><td rowspan="9">SFO[2:0]</td><td>滤波器阶数</td></tr><tr><td>000: FastSinc 滤波器</td></tr><tr><td>001: Sinc<eq>^{1}</eq> 滤波器</td></tr><tr><td>010: Sinc<eq>^{2}</eq> 滤波器</td></tr><tr><td>011: Sinc<eq>^{3}</eq> 滤波器</td></tr><tr><td>100: Sinc<eq>^{4}</eq> 滤波器</td></tr><tr><td>101: Sinc<eq>^{5}</eq> 滤波器</td></tr><tr><td>110~111: 保留</td></tr><tr><td>只有当 HPDF_FLTyCTL0 寄存器中的 FLTEN=0 时,此位域才能被修改。</td></tr><tr><td>28:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td rowspan="3">25:16</td><td rowspan="3">SFOR[9:0]</td><td>Sinc 滤波器过采样率(抽取率)</td></tr><tr><td>0~1023: Sinc 滤波器过采样率 SFOR= SFOR[9:0] +1</td></tr><tr><td>如果 SFOR[9:0]=0,即过采样率为 SFOR=1,表示滤波器被旁路只有当 HPDF_FLTyCTL0 寄存器中的 FLTEN=0 时,此位域才能被修改。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>IOR[7:0]</td><td>积分器过采样率0~255:积分器过采样率 IOR=IOR[7:0]+1积分器的数据输出速率将减去该值如果 IOR[7:0]=0,即过采样率为 IOR=1,表示积分器被旁路。只有当 HPDF_FLTyCTL0 寄存器中的 FLTEN=0 时,此位域才能被修改。</td></tr></table>

## 滤波器 y 注入组转换数据寄存器（HPDF_FLTyIDATA）

地址偏移：0x118 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按半字（16 位）或字（32 位）访问。

注意：可使用半字访问只读取转换数据的高 16 位有效数据，读该寄存器可清除 ICEF 位。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDATA[23:8]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">IDATA[7:0]</td><td colspan="5">保留</td><td colspan="3">ICCH[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>IDATA[23:0]</td><td>注入通道转换数据当每个注入中的一个通道转换完成,数据被保存在此位域。当ICEF=1时,转换数据为有效的。读此寄存器清除RCEF位。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>ICCH[2:0]</td><td>最近转换的注入通道每个注入组通道转换完成时,ICCH[2:0]被更新,指示哪个通道完成了规则转换。故IDATA[23:0]中的数据对应为该通道的值。</td></tr></table>

滤波器 y 规则通道转换数据寄存器（HPDF_FLTyRDATA）

地址偏移：0x11C + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按半字（16 位）或字（32 位）访问。

注意：可使用半字访问只读取转换数据的高 16 位有效数据，读该寄存器可清除 RCEF 位。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RDATA[23:8]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">RDATA[7:0]</td><td colspan="3">保留</td><td>RCHPDT</td><td>保留</td><td colspan="3">RCCH[2:0]</td></tr><tr><td colspan="8">r</td><td colspan="3">r</td><td colspan="5">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>RDATA[23:0]</td><td>规则通道转换数据当每个规则转换完成,数据被保存在此位域。当 RCEF=1 时,转换数据为有效的。读此寄存器清除 RCEF 位。</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>RCHPDT</td><td>规则通道等待处理数据在规则转换期间,被注入转换请求中断,导致 RDATA[23:0]中的规则转换数据被延迟处理。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>RCCH[2:0]</td><td>最近转换的规则通道每个规则转换完成时,RCCH[2:0]被更新,指示哪个通道完成了规则转换。故 RDATA[23:0]中的数据对应为该通道的值。</td></tr></table>


滤波器 y 阈值监视器上限阈值寄存器（HPDF_FLTyTMHT）



地址偏移：0x120 + 0x80 * y，（y = 0…3）



复位值：0x0000 0000



该寄存器只能按字（32 位）访问。


<table><tr><td colspan="16">HTVAL[23:8]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">HTVAL[7:0]</td><td colspan="4">保留</td><td colspan="4">HTBSD[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>HTVAL[23:0]</td><td>阈值监视器上限阈值此位域通过软写入阈值监视器的上限阈值在阈值监视器快速模式下(TMFM=1),此位域的高16位定义上限阈值,并与阈值监视器数据寄存器中的TMDATA[15:0]值比较。此时HTVAL[7:0]被忽略。</td></tr></table>

<table><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>HTBSD[3:0]</td><td>上限阈值事件断路信号分配HTBSD[i] = 0: 断路信号 x 未分配到阈值监视器上限阈值事件。HTBSD[i] = 1: 断路信号 x 分配到阈值监视器上限阈值事件。</td></tr></table>

## 滤波器 y 阈值监视器下限阈值寄存器（HPDF_FLTyTMLT）

地址偏移：0x124 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">LTVAL[23:8]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">LTVAL[7:0]</td><td colspan="4">保留</td><td colspan="4">LTBSD[3:0]</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>LTVAL[23:0]</td><td>阈值监视器下限阈值此位域通过软写入阈值监视器的下限阈值在阈值监视器快速模式下(TMFM=1),此位域的高16位定义下限阈值,并与阈值监视器数据寄存器中的TMDATA[15:0]值比较。此时LTVAL[7:0]被忽略。</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>LTBSD[3:0]</td><td>下限阈值事件断路信号分配LTBSD[i] = 0: 断路信号i未分配到阈值监视器下限阈值事件LTBSD[i] = 1: 断路信号i分配到阈值监视器下限阈值事件</td></tr></table>

## 滤波器 y 阈值监视器状态寄存器（HPDF_FLTyTMSTAT）

地址偏移：0x128 + 0x80 * y，（y = 0…3）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">HTF[7:0]</td><td colspan="8">LTF[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>HTF[7:0]</td><td>阈值监视器上限阈值标志HTF[x]=0:通道x未超出上限阈值HTF[x]=1:通道x超出上限阈值此位域由硬件置位,可通过置位HPDF_FLTyTMFC寄存器HTFC[7:0]位域中相应的位,清除对应的阈值监视器上限阈值标志。</td></tr><tr><td>7:0</td><td>LTF[7:0]</td><td>阈值监视器下限阈值标志LTF[x]=0:通道x未超出下限阈值LTF[x]=1:通道x超出下限阈值此位域由硬件置位,可通过置位HPDF_FLTyTMFC寄存器LTFC[7:0]位域中相应的位,清除对应的阈值监视器下限阈值标志。</td></tr></table>

## 滤波器 y 阈值监视器标志清除寄存器（HPDF_FLTyTMFC）

地址偏移： $0 { \times } 1 2 { \mathsf C } + 0 { \times } 8 0 ^ { \star } \mathsf y , ~ ( \mathsf y = 0 . . . 3 )$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">HTFC[7:0]</td><td colspan="8">LTFC[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>HTFC[7:0]</td><td>清除阈值监视器上限阈值标志HTFC[x]=0:没有影响HTFC[x]=1:清除通道x的阈值监视器上限阈值标志</td></tr><tr><td>7:0</td><td>LTFC[7:0]</td><td>清除阈值监视器下限阈值标志LTFC[x]=0:没有影响LTFC[x]=1:清除通道x的阈值监视器下限阈值标志</td></tr></table>

滤波器 y 极值监视器最大值寄存器（HPDF_FLTyEMMAX）

地址偏移： $0 { \times } 1 3 0 + 0 { \times } 8 0 ^ { \star } { \bf y } , ~ ( { \bf y } = 0 . . . 3 )$ 

复位值：0x8000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MAXVAL[23:8]</td></tr><tr><td colspan="16">rc_r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">MAXVAL[7:0]</td><td colspan="5">保留</td><td colspan="3">MAXDC[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>MAXVAL[23:0]</td><td>极值监视器最大值此位域通过硬件置位,表示 HPDF_FLTy 所转换的最大值。读取该寄存器。此位域被复位。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>MAXDC[2:0]</td><td>极值监视器最大值数据通道该位域表示哪个通道的值被保存在 MAXVAL[23:0]位域中。读取该寄存器此位被清 0</td></tr></table>

## 滤波器 y 极值监视器最小值寄存器（HPDF_FLTyEMMIN）

地址偏移：0x134 + 0x80 * y，（y = 0…3）

复位值：0x7FFF FF00

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">MINVAL[23:8]</td></tr><tr><td colspan="16">rs</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">MINVAL[7:0]</td><td colspan="5">保留</td><td colspan="3">MINDC[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>MINVAL[23:0]</td><td>极值监视器最小值此位域通过硬件置位,表示 HPDF_FLTy 所转换的最小值。读取该寄存器。此位域被复位。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>MINDC[2:0]</td><td>极值监视器最小值数据通道该位域表示哪个通道的值被保存在 MINVAL[23:0]位域中。</td></tr></table>

读取该寄存器。此位被清零。

## 滤波器 y 转换定时器寄存器（HPDF_FLTyCT）

地址偏移： $0 { \times } 1 3 8 + 0 { \times } 8 0 ^ { \star } \ y , ( \mathsf { y } = 0 . . . 3 )$ 

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CTCNT[31:12]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">CTCNT[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>CTCNT[27:0]</td><td>28 位定时器计数转换时间 <eq>t = \text{CNVCNT}[27:0] / f_{\text{HPDFCLK}}</eq>定时器的输入时钟来自 HPDF 时钟(系统时钟 <eq>f_{\text{HPDFCLK}}</eq>)。转换时间测量始于每次转换开始,并止于每 36 次转换结束(即第一次和最后一次串行采样之间的间隔)。只有在滤波器旁路时(SFOR[9:0]=0),转换时间测量才会停止,且 CNVCNT[27:0]=0.时间计时如下:如果 FAST=0 (或者 FAST=1 连续模式下的第一次转换):<eq>t = [\text{SFOR}^{*} (\text{IOR-1} + \text{SFO}) + \text{SFO}] / f_{\text{CKIN}}</eq>(适用于 <eq>\text{Sinc}^{\text{X}}</eq> 滤波器)<eq>t = [\text{SFOR}^{*} (\text{IOR-1} + 4) + 2] / f_{\text{CKIN}}</eq>(适用于 FastSinc 滤波器)如果在连续模式下 FAST=1 (第一次转换除外):<eq>t = [\text{SFOR}^{*} \text{IOR-1}] / f_{\text{CKIN}}</eq>如果 SFOR = SFOR[9:0]+1 = 1(滤波器旁路,仅积分器有效):CNVCNT = 0 (时间计时停止,转换时间:<eq>t = \text{IOR} / f_{\text{CKIN}}</eq>)其中,<eq>f_{\text{CKIN}}</eq> 为给定通道 CKINy 引脚上的通道输入时钟频率;在并行数据输入来自内部 ADC 或者来自 CPU/DMA 写操作的情况下,表示输入数据速率。当转换被中断时(如禁能/使能所选通道)定时器也将该中断时间计算在内</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
