## 25.4. SLCD 寄存器

SLCD 基地址：0x4000 2400

## 25.4.1. 控制寄存器（SLCD_CTL）

GD32L233xx 产品

偏移地址：0x00

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>VODEN</td><td>COMS</td><td colspan="2">BIAS[1:0]</td><td colspan="3">DUTY[2:0]</td><td>VSRC</td><td>SLCDON</td></tr><tr><td colspan="7"></td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td></td><td></td><td>011: 1/4 占空比</td></tr><tr><td></td><td></td><td>100: 1/8 占空比</td></tr><tr><td></td><td></td><td>101: 1/6 占空比</td></tr><tr><td></td><td></td><td>110: 保留</td></tr><tr><td></td><td></td><td>111: 保留</td></tr><tr><td>1</td><td>VSRC</td><td>SLCD 电压源</td></tr><tr><td></td><td></td><td>配置该位决定 SLCD 电压源。</td></tr><tr><td></td><td></td><td>0: 内部电压源</td></tr><tr><td></td><td></td><td>1: 外部电压源 (VSLCD 引脚)</td></tr><tr><td>0</td><td>SLCDON</td><td>SLCD 控制器开始</td></tr><tr><td></td><td></td><td>通过软件置 1 该位开始 SLCD 控制器。通过软件清零该位停止 SLCD 控制器,且 SLCD 控制器在下一帧开始时停止。</td></tr><tr><td></td><td></td><td>0: SLCD 控制器停止</td></tr><tr><td></td><td></td><td>1: SLCD 控制器开始</td></tr></table>

GD32L235xx 产品

偏移地址：0x00

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>COMS</td><td colspan="2">BIAS[1:0]</td><td colspan="3">DUTY[2:0]</td><td>VSRC</td><td>SLCDON</td></tr><tr><td colspan="8"></td><td>rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>COMS</td><td>COM/SEG 引脚选择该位用于 COM/SEG 引脚的选择。当占空比选择 1/8 或 1/6 时,SLCD_COM[7:4]总是作为 SLCD_COM[7:4]功能,无论该位有无被置位。0:SLCD_COM[7:4]引脚选择 SLCD_COM[7:4]1:SLCD_COM[7:4]引脚选择 SLCD_SEG[31:28]</td></tr></table>

<table><tr><td>6:5</td><td>BIAS[1:0]</td><td>偏置选择</td></tr><tr><td></td><td></td><td>偏置为驱动 SLCD 时的电压水平参数。它被定义为 1/(驱动 SLCD 显示屏能够使用的电压水平总数-1)。</td></tr><tr><td></td><td></td><td>00: 1/4 偏置(5 个电压水平:VSS,1/4VSLCD,1/2VSLCD,3/4VSLCD,VSLCD)</td></tr><tr><td></td><td></td><td>01: 1/2 偏置(3 个电压水平:VSS,1/2VSLCD,VSLCD)</td></tr><tr><td></td><td></td><td>10: 1/3 偏置(4 个电压水平:VSS,1/3VSLCD,2/3VSLCD,VSLCD)</td></tr><tr><td></td><td></td><td>11: 保留</td></tr><tr><td>4:2</td><td>DUTY[2:0]</td><td>占空比选择这些位决定占空比。占空比定义为1/(SLCD显示屏需要的COM数)000:静态占空比001:1/2占空比010:1/3占空比011:1/4占空比100:1/8占空比101:1/6占空比110:保留111:保留</td></tr><tr><td>1</td><td>VSRC</td><td>SLCD电压源配置该位决定SLCD电压源。0:内部电压源(VDD电压)1:外部电压源(VSLCD引脚)</td></tr><tr><td>0</td><td>SLCDON</td><td>SLCD控制器开始通过软件置1该位开始SLCD控制器。通过软件清零该位停止SLCD控制器,且SLCD控制器在下一帧开始时停止。0:SLCD控制器停止1:SLCD控制器开始</td></tr></table>

## 25.4.2. 配置寄存器（SLCD_CFG）

## GD32L233xx 产品

偏移地址：0x04

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="4">PSC[3:0]</td><td colspan="4">DIV[3:0]</td><td colspan="2">BLKMOD[1:0]</td></tr><tr><td colspan="10">rw</td><td colspan="4">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">BLKDIV[2:0]</td><td colspan="3">CONR[2:0]</td><td colspan="3">DTD[2:0]</td><td colspan="3">PULSE[2:0]</td><td>UPDIE</td><td>保留</td><td>SOFIE</td><td>HDEN</td></tr><tr><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:22</td><td>PSC[3:0]</td><td>SLCD时钟预分频器配置这些位定义SLCD时钟预分频器。0000:<eq>f_{PSC} = f_{in\_clk}</eq>0001:<eq>f_{PSC} = f_{in\_clk}/2</eq>0010:<eq>f_{PSC} = f_{in\_clk}/4</eq>1111: <eq>f_{PSC} = f_{in\_clk}/32768</eq></td></tr><tr><td>21:18</td><td>DIV[3:0]</td><td>SLCD时钟分频器配置这些位定义DIV分频器的分频因子。0000: <eq>f_{SLCD} = f_{PSC}/16</eq>0001: <eq>f_{SLCD} = f_{PSC}/17</eq>0010: <eq>f_{SLCD} = f_{PSC}/18</eq>...1111: <eq>f_{SLCD} = f_{PSC}/31</eq></td></tr><tr><td>17:16</td><td>BLKMOD[1:0]</td><td>闪烁模式00: 不闪烁01: 闪烁SEG[0]、COM[0](1像素)10: 闪烁SEG[0]和所有COM(由可编程占空比可实现最大8像素)11: 闪烁所有SEG和所有COM(所有像素)</td></tr><tr><td>15:13</td><td>BLKDIV[2:0]</td><td>闪烁分频器000: <eq>f_{BLINK} = f_{SLCD}/8</eq>001: <eq>f_{BLINK} = f_{SLCD}/16</eq>010: <eq>f_{BLINK} = f_{SLCD}/32</eq>011: <eq>f_{BLINK} = f_{SLCD}/64</eq>100: <eq>f_{BLINK} = f_{SLCD}/128</eq>101: <eq>f_{BLINK} = f_{SLCD}/256</eq>110: <eq>f_{BLINK} = f_{SLCD}/512</eq>111: <eq>f_{BLINK} = f_{SLCD}/1024</eq></td></tr><tr><td>12:10</td><td>CONR[2:0]</td><td>对比度当选择内部电压源(VSRC=0)时,这些位表示VSLCD电压,其范围从VSLCD0到VSLCD7(典型值为2.65V到3.67V),VSLCDx值请参考数据手册。当使用外部电压源时(VSRC=1)这些位无效。000: VSLCD0001: VSLCD1010: VSLCD2011: VSLCD3100: VSLCD4101: VSLCD5110: VSLCD6111: VSLCD7</td></tr><tr><td>9:7</td><td>DTD[2:0]</td><td>死区时间配置这些位定义帧间死区时间的长度。000: 无死区时间001: 1相周期死区时间010: 2相周期死区时间...111: 7相周期死区时间</td></tr><tr><td>6:4</td><td>PULSE[2:0]</td><td>脉冲持续时间配置这些位根据PSC脉冲来定义脉冲持续时间。000: 0001: <eq>1/f_{PSC}</eq>010: <eq>2/f_{PSC}</eq>011: <eq>3/f_{PSC}</eq>100: <eq>4/f_{PSC}</eq>101: <eq>5/f_{PSC}</eq>110: <eq>6/f_{PSC}</eq>111: <eq>7/f_{PSC}</eq></td></tr><tr><td>3</td><td>UPDIE</td><td>SLCD更新完成中断使能该位可被软件置1和清零。0:禁用SLCD更新完成中断1:使能SLCD更新完成中断</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SOFIE</td><td>帧开始中断使能该位可被软件置1和清零。0:禁用SLCD帧开始中断1:使能SLCD帧开始中断</td></tr><tr><td>0</td><td>HDEN</td><td>高驱动使能该位可被软件置1和清零。0:禁用持久的高驱动。<eq>R_L</eq>使能的持续时间通过PULSE[2:0]配置1:使能持久的高驱动。<eq>R_L</eq>总是被使能,PULSE[2:0]位无效</td></tr></table>

## GD32L235xx 产品

偏移地址：0x04

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="2">RSEL</td><td colspan="4">PSC[3:0]</td><td colspan="4">DIV[3:0]</td><td colspan="2">BLKMOD[1:0]</td></tr><tr><td colspan="6">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">BLKDIV[2:0]</td><td colspan="3">保留</td><td colspan="3">DTD[2:0]</td><td colspan="3">PULSE[2:0]</td><td>UPDIE</td><td>保留</td><td>SOFIE</td><td>HDEN</td></tr><tr><td colspan="6">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>27:26</td><td>RSEL[1:0]</td><td>弱驱动电阻选择00: 6M01: 4M10:2M11:1M</td></tr><tr><td>25:22</td><td>PSC[3:0]</td><td>SLCD时钟预分频器配置这些位定义SLCD时钟预分频器。0000:<eq>f_{PSC} = f_{in\_clk}</eq>0001:<eq>f_{PSC} = f_{in\_clk}/2</eq>0010:<eq>f_{PSC} = f_{in\_clk}/4</eq>...1111:<eq>f_{PSC} = f_{in\_clk}/32768</eq></td></tr><tr><td>21:18</td><td>DIV[3:0]</td><td>SLCD时钟分频器配置这些位定义DIV分频器的分频因子。0000:<eq>f_{SLCD} = f_{PSC}/16</eq>0001:<eq>f_{SLCD} = f_{PSC}/17</eq>0010:<eq>f_{SLCD} = f_{PSC}/18</eq>...1111:<eq>f_{SLCD} = f_{PSC}/31</eq></td></tr><tr><td>17:16</td><td>BLKMOD[1:0]</td><td>闪烁模式00:不闪烁01:闪烁SEG[0]、COM[0](1像素)10:闪烁SEG[0]和所有COM(由可编程占空比可实现最大8像素)11:闪烁所有SEG和所有COM(所有像素)</td></tr><tr><td>15:13</td><td>BLKDIV[2:0]</td><td>闪烁分频器000:<eq>f_{BLINK} = f_{SLCD}/8</eq>001:<eq>f_{BLINK} = f_{SLCD}/16</eq>010:<eq>f_{BLINK} = f_{SLCD}/32</eq>011:<eq>f_{BLINK} = f_{SLCD}/64</eq>100:<eq>f_{BLINK} = f_{SLCD}/128</eq>101:<eq>f_{BLINK} = f_{SLCD}/256</eq>110:<eq>f_{BLINK} = f_{SLCD}/512</eq>111:<eq>f_{BLINK} = f_{SLCD}/1024</eq></td></tr><tr><td>12:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:7</td><td>DTD[2:0]</td><td>死区时间配置这些位定义帧间死区时间的长度。000:无死区时间001:1相周期死区时间010:2相周期死区时间...111:7相周期死区时间</td></tr><tr><td>6:4</td><td>PULSE[2:0]</td><td>脉冲持续时间配置这些位根据PSC脉冲来定义脉冲持续时间。000:0001: 1/fPSC</td></tr><tr><td></td><td></td><td>010: 2/fPSC</td></tr><tr><td></td><td></td><td>011: 3/fPSC</td></tr><tr><td></td><td></td><td>100: 4/fPSC</td></tr><tr><td></td><td></td><td>101: 5/fPSC</td></tr><tr><td></td><td></td><td>110: 6/fPSC</td></tr><tr><td></td><td></td><td>111: 7/fPSC</td></tr><tr><td>3</td><td>UPDIE</td><td>SLCD 更新完成中断使能该位可被软件置1和清零。</td></tr><tr><td></td><td></td><td>0: 禁用SLCD更新完成中断</td></tr><tr><td></td><td></td><td>1: 使能SLCD更新完成中断</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SOFIE</td><td>帧开始中断使能该位可被软件置1和清零。</td></tr><tr><td></td><td></td><td>0: 禁用SLCD帧开始中断</td></tr><tr><td></td><td></td><td>1: 使能SLCD帧开始中断</td></tr><tr><td>0</td><td>HDEN</td><td>高驱动使能该位可被软件置1和清零。</td></tr><tr><td></td><td></td><td>0: 禁用持久的高驱动。RL使能的持续时间通过PULSE[2:0]配置</td></tr><tr><td></td><td></td><td>1: 使能持久的高驱动。RL总是被使能,PULSE[2:0]位无效</td></tr></table>

## 25.4.3. 状态标志寄存器（SLCD_STAT）

GD32L233xx 产品

偏移地址：0x08

复位值：0x0000 0020

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYNF</td><td>VRDYF</td><td>UPDF</td><td>UPRF</td><td>SOF</td><td>ONF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>SYNF</td><td>SLCD_CFG 寄存器同步标志当 SLCD_CFG 寄存器更新到 SLCD 时钟域时,该位置 1。当写 SLCD_CFG 寄存器时,通过硬件清零该位。0: SLCD_CFG 寄存器尚未同步1: SLCD_CFG 寄存器已与 SLCD 时钟域同步</td></tr><tr><td>4</td><td>VRDYF</td><td>SLCD 电压就绪标志该位根据 SLCD 电压由硬件置位或清零。0: SLCD 电压未就绪1: 升压转换器已使能并准备提供准确电压</td></tr><tr><td>3</td><td>UPDF</td><td>更新 SLCD 数据完成标志当更新完成 SLCD 数据时,该位通过硬件置位。通过向 SLCD_STATC 寄存器的 UPDC 位写 1 来清零该位。0: 无影响1: SLCD 数据更新完成</td></tr><tr><td>2</td><td>UPRF</td><td>更新 SLCD 数据请求标志通过 SLCD_DATAx 寄存器组修改第一缓冲区后,应用程序应当置位该位将数据传输到第二缓冲区中。该位将保持置位直到传输完成,在这段时间 SLCD_DATAx 寄存器组为写保护状态。0: 无影响1: 请求 SLCD 数据更新</td></tr><tr><td>1</td><td>SOF</td><td>帧开始标志在一个新帧开始时,该位通过硬件置 1。通过往 SLCD_STATC 寄存器中 SOFC 位写 1 来清零该位。0: 无影响1: 帧开始标志</td></tr><tr><td>0</td><td>ONF</td><td>SLCD 控制器开启标志当 SLCDON 为 1 时,该位通过硬件置 1。在 SLCDON 位被清零并且最后的帧被显示后,该位通过硬件清零。0: SLCD 控制器关闭1: SLCD 控制器开启</td></tr></table>

## GD32L235xx 产品

偏移地址：0x08

复位值：0x0000 0020

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>SYNF</td><td>保留</td><td>UPDF</td><td>UPRF</td><td>SOF</td><td>ONF</td></tr><tr><td colspan="12">保留</td><td>UPDC</td><td>保留</td><td>SOFC</td><td>保留</td></tr></table>

<table><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>SYNF</td><td>SLCD_CFG 寄存器同步标志当 SLCD_CFG 寄存器更新到 SLCD 时钟域时,该位置 1。当写 SLCD_CFG 寄存器时,通过硬件清零该位。0: SLCD_CFG 寄存器尚未同步1: SLCD_CFG 寄存器已与 SLCD 时钟域同步</td></tr><tr><td>4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>UPDF</td><td>更新 SLCD 数据完成标志当更新完成 SLCD 数据时,该位通过硬件置位。通过向 SLCD_STATC 寄存器的 UPDC 位写 1 来清零该位。0:无影响1: SLCD 数据更新完成</td></tr><tr><td>2</td><td>UPRF</td><td>更新 SLCD 数据请求标志通过 SLCD_DATAx 寄存器组修改第一缓冲区后,应用程序应当置位该位将数据传输到第二缓冲区中。该位将保持置位直到传输完成,在这段时间 SLCD_DATAx 寄存器组为写保护状态。0:无影响1: 请求 SLCD 数据更新</td></tr><tr><td>1</td><td>SOF</td><td>帧开始标志在一个新帧开始时,该位通过硬件置 1。通过往 SLCD_STATC 寄存器中 SOFC 位写 1 来清零该位。0:无影响1: 帧开始标志</td></tr><tr><td>0</td><td>ONF</td><td>SLCD 控制器开启标志当 SLCDON 为 1 时,该位通过硬件置 1。在 SLCDON 位被清零并且最后的帧被显示后,该位通过硬件清零。0: SLCD 控制器关闭1: SLCD 控制器开启</td></tr></table>

## 25.4.4. 状态标志清除寄存器（SLCD_STATC）

偏移地址：0x0C

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。


rc_w1 rc_w1 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>UPDC</td><td>SLCD 数据更新完成清除位置 1 该位清除 SLCD_STAT 寄存器中的 UPDF 标志。0:无影响1:清除 UPDF 标志</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SOFC</td><td>帧开始标志清除置 1 该位清除 SLCD_STAT 寄存器中的 SOF 标志。0:无影响1:清除 UPDF 标志</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 25.4.5. 显示数据寄存器（SLCD_DATAx）（x=0…7）

偏移地址：0x14 + 0x08 * x

复位值：0x0000 0000

该寄存器可以按半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATAx[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATAx[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SEG_DATAx[31:0]</td><td>每一位对应一个像素来显示。0:该像素无效1:该像素有效</td></tr></table>
