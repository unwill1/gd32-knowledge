# 12.4. TRNG 寄存器

TRNG 基地址：0x4802 1800

# 12.4.1. 控制寄存器（TRNG_CTL）

地址偏移：0x00

复位值：0x0300 0410

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CTL_LK</td><td>CONDRST</td><td colspan="4">保留</td><td colspan="2">NR[1:0]</td><td colspan="4">保留</td><td colspan="4">CLKDIV[3:0]</td></tr><tr><td>rs</td><td>rw</td><td colspan="10">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>INMOD</td><td>OUTMOD</td><td colspan="2">ALGO[1:0]</td><td>保留</td><td>COND_EN</td><td>PP_EN</td><td>INIT</td><td>RT_EN</td><td>保留</td><td>CED</td><td>MOD_SEL</td><td>IE</td><td>TRNGEN</td><td colspan="2">保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>CTL_LK</td><td>TRNG_CTL 寄存器锁定位该位仅能在模块复位时清 00: 允许写位域[29:4]1: 锁定位域[29:4],且对该位域写操作会被忽略</td></tr><tr><td>30</td><td>CONDRST</td><td>复位逻辑训练单元先置 1 后再清 0 以复位逻辑训练单元。需要注意的是,TRNG_HTCFG 寄存器和 TRNG_CTL 寄存器的位域[29:4]只能在该位为 1 时被改写。</td></tr><tr><td>29:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>NR[1:0]</td><td>TRNG 模块功耗模式,复位值:2b' 1100: 极低01: 低10: 中11: 高</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:16</td><td>CLKDIV[3:0]</td><td>TRNG 时钟分频系数0000: TRNG 时钟 <eq>2^0</eq> 分频0001: TRNG 时钟 <eq>2^1</eq> 分频......1111: TRNG 时钟 <eq>2^{15}</eq> 分频</td></tr><tr><td>15</td><td>INMOD</td><td>随机数种子输入模式选择0: 向训练单元输入 256 比特1: 向训练单元输入 440 比特</td></tr><tr><td>14</td><td>OUTMOD</td><td>随机数输出模式选择0:从训练单元输出128比特1:从训练单元输出256比特</td></tr><tr><td>13:12</td><td>ALGO[1:0]</td><td>训练单元算法选择00:sha1算法01:md5算法10:sha224算法11:sha256算法</td></tr><tr><td>11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>COND_EN</td><td>启动训练单元0:失能训练单元1:使能训练单元</td></tr><tr><td>9</td><td>PP_EN</td><td>启动后处理功能0:失能后处理功能1:使能后处理功能</td></tr><tr><td>8</td><td>INIT</td><td>使能训练单元时初始化哈希算法0:不初始化哈希算法1:初始化哈希算法</td></tr><tr><td>7</td><td>RT_EN</td><td>替换测试使能位0:失能替换测试1:使能替换测试</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>CED</td><td>时钟错误检测0:失能时钟错误检测1:使能时钟错误检测</td></tr><tr><td>4</td><td>MOD_SEL</td><td>TRNG模式选择0:LFSR模式1:NIST模式</td></tr><tr><td>3</td><td>IE</td><td>中断使能位,当DRDY,SEIF,CEIF或ERR_STA位被置位时该位控制生成一个中断。0:禁止TRNG中断1:使能TRNG中断</td></tr><tr><td>2</td><td>TRNGEN</td><td>TRNG使能位0:禁止TRNG模块(降低功耗)1:使能TRNG模块</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 12.4.2. 状态寄存器（TRNG_STAT）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>SEIF</td><td>CEIF</td><td>保留</td><td>ERR_STA</td><td>SECS</td><td>CECS</td><td>DRDY</td></tr></table>


rc_w0 rc_w0 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>SEIF</td><td>种子错误中断标志位如果超过64个连续位具有相同值或超过32组连续交替的0和1被检测到则此位将置1。0:未检测到错误1:检测到种子错误。写0将清除该位</td></tr><tr><td>5</td><td>CEIF</td><td>时钟错误中断标志位如果TRNG_CLK时钟频率低于HCLK频率的1/16时该位被置位。0:未检测到错误1:检测到时钟错误。写0将清除该位</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>ERR_STA</td><td>NIST模式错误标志,该位可以被CONDRST清零0:NIST模式中未出现错误1:NIST模式中出现错误</td></tr><tr><td>2</td><td>SECS</td><td>种子错误当前状态0:当前未检测到种子错误。如果SEIF=1和SECS=0,说明之前已经检测到种子错误但现在已恢复正常。1:当前检测到种子错误。如果超过64个连续位具有相同值或超过32组连续交替的0和1被检测到时,该位置1。</td></tr><tr><td>1</td><td>CECS</td><td>时钟错误当前状态0:当前未检测到时钟错误。如果CEIF=1和CECS=0,则意味着之前已检测到时钟错误但现在已恢复正常。1:当前检测到时钟错误。此时TRNG_CLK时钟频率低于1/16 HCLK频率。</td></tr><tr><td>0</td><td>DRDY</td><td>随机数准备状态位读TRNG_DATA寄存器会清零该位,当一个新的随机数产生时被置位。0:TRNG数据寄存器的内容无效</td></tr></table>
