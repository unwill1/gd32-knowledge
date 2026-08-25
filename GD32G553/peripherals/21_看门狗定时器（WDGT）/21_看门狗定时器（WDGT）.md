## 21. 看门狗定时器（WDGT）

看门狗定时器（WDGT）是一个硬件计时电路，用来监测由软件故障导致的系统故障。片上有两个看门狗定时器外设，独立看门狗定时器（FWDGT）和窗口看门狗定时器（WWDGT）。它们使用灵活，并提供了很高的安全水平和精准的时间控制。两个看门狗定时器都是用来解决软件故障问题的。

看门狗定时器在内部计数值达到了预设的门限时，会触发一个复位（对于窗口看门狗定时器来说，会产生一个中断）。当处理器工作在调试模式的时候看门狗定时器定时计数器可以停止计数。

## 21.1. 独立看门狗定时器（FWDGT）

## 21.1.1. 简介

独立看门狗定时器（FWDGT）有独立时钟源（IRC32K）。因此，即使主时钟失效了，它仍然能保持工作状态，这非常适合于需要独立环境且对计时精度要求不高的场合。

当内部向下计数器的计数值达到0或计数器的值大于窗口寄存器的值，刷新计数器，独立看门狗会产生一个复位。使能独立看门狗的寄存器写保护功能可以避免寄存器的值被意外的配置篡改。

## 21.1.2. 主要特征

 独立运行的12位向下计数器。

 如果看门狗定时器被使能，有以下两种情况下会产生复位：

– 当计数器到0时产生复位；

当计数器的值大于窗口寄存器的值时，更新计数器会产生复位。

■ 独立时钟源，独立看门狗定时器在主时钟故障（例如待机和深度睡眠模式下）时仍能工作。

 独立看门狗定时器硬件控制位，可以用来控制是否在上电时自动启动独立看门狗定时器。

 可以配置独立看门狗定时器在调试模式下选择停止还是继续工作。

 通过配置FWDGSPD_STDBY或FWDGSPD_DPSLP, 在待机模式或深度睡眠模式中，FWDGT可以停止工作或唤醒控制器继续工作。

## 21.1.3. 功能说明

独立看门狗定时器带有一个8级预分频器和一个12位的向下递减计数器。参考 21-1.的独立看门狗定时器的功能模块。


图 21-1. 独立看门狗定时器框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/a706ac5c5e3309a98034653d12c6dd564b3c19858b4c8ef04b39b6fbd781525f.jpg)


向控制寄存器（FWDGT_CTL）中写0xCCCC可以开启独立看门狗定时器，计数器开始向下计数。当计数器记到0x000，产生一次复位。

在任何时候向控制寄存器（FWDGT_CTL）中写0xAAAA都可以重装载计数器，重装载值来源于FWDGT_RLD寄存器。软件可以在计数器计数值达到0x000之前可以通过重装载计数器来阻止看门狗定时器复位。

独立看门狗定时器也能够工作在窗口看门狗定时器模式下，只要在FWDGT_WND寄存器中设置适当的值即可。如果重加载操作执行的同时，看门狗定时器计数器的值大于窗口寄存器（FWDGT_WND）中存储的值，也会引起系统复位。FWDGT_WND的默认值是0x00000FFF，所以如果没有改写它，那么窗口选项默认是关闭的。窗口值一旦改变，立即就会引起看门狗定时器计数器的一次重加载动作，将向下递减计数器置为FWDGT_RLD中的值，并复位预分频计数器。

如果在选项字节中打开了“硬件看门狗定时器”功能，那么在上电的时候看门狗定时器就被自动打开。为了避免复位，软件应该在计数器达到0x000之前重装载计数器。

FWDGT_PSC寄存器和FWDGT_RLD寄存器都有写保护功能。在写数据到这些寄存器之前，需要写0x5555到控制寄存器（FWDGT_CTL）中。写其他任何值到控制寄存器中将会再次启动对这些寄存器的写保护。当预分频寄存器（FWDGT_PSC）或者重装载寄存器（FWDGT_RLD）更新时，FWDGT_STAT寄存器的状态位会被置1。

如果在MCU调试模块中的FWDGT_HOLD位被清0，即使Cortex®-M33内核停止（调试模式下） 独立看门狗定时器依然工作。如果FWDGT_HOLD位被置1，独立看门狗定时器将在调试模式下停止工作。


表 21-1. 独立看门狗定时器在 32kHz (IRC32K)时的最小/最大超时周期


<table><tr><td>预分频系数</td><td>PSC[2:0] 位</td><td>最小超时(ms) RLD [11:0]=0x000</td><td>最大超时(ms) RLD [11:0]=0xFFFF</td></tr><tr><td>1/4</td><td>000</td><td>0.125</td><td>512</td></tr><tr><td>1/8</td><td>001</td><td>0.25</td><td>1024</td></tr></table>


GD32G553 用户手册


<table><tr><td>预分频系数</td><td>PSC[2:0] 位</td><td>最小超时(ms) RLD [11:0]=0x000</td><td>最大超时(ms) RLD [11:0]=0xFFFF</td></tr><tr><td>1/16</td><td>010</td><td>0.5</td><td>2048</td></tr><tr><td>1/32</td><td>011</td><td>1.0</td><td>4096</td></tr><tr><td>1/64</td><td>100</td><td>2.0</td><td>8192</td></tr><tr><td>1/128</td><td>101</td><td>4.0</td><td>16384</td></tr><tr><td>1/256</td><td>110或111</td><td>8.0</td><td>32768</td></tr></table>


通过IRC32K校准可以使独立看门狗定时器超时更加精确。


## 注意：

1. 当执行完喂狗reload操作之后，如需要立即进入deepsleep/standby模式时，必须通过软件设置，在reload命令及deepsleep/standby模式命令中间插入（3个以上）IRC32K时钟间隔。

2. 两次连续喂狗之间需插入7个及以上IRC32K时钟间隔。

## 21.1.4. FWDGT 寄存器

FWDGT 基地址：0x4000 3000

控制寄存器（FWDGT_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CMD[15:0]</td><td>只可写,写入不同的值来产生不同的功能0x5555:关闭FWDGT_PSC和FWDGT_RLD的写保护0xCCCC:开启独立看门狗定时器计数器。计数减到0时产生中断0xAAAA:重装载计数器</td></tr></table>

预分频寄存器（FWDGT_PSC）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">PSC[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>PSC[2:0]</td><td>独立看门狗定时器计时预分频选择。写这些位之前要通过向FWDGT_CTL寄存器写0x5555去除写保护。在改写这个寄存器的过程中,FWDGT_STAT寄存器的PUD位被</td></tr></table>

<table><tr><td>置1,此时读取此寄存器的值都是无效的。</td></tr><tr><td>000: 1/4</td></tr><tr><td>001: 1/8</td></tr><tr><td>010: 1/16</td></tr><tr><td>011: 1/32</td></tr><tr><td>100: 1/64</td></tr><tr><td>101: 1/128</td></tr><tr><td>110: 1/256</td></tr><tr><td>111: 1/256</td></tr><tr><td>如果应用需要使用几个预分频系数,改变预分频值之前必须等到PUD位被清0。更新了预分频寄存器中的值后,在代码持续执行之前不必等待PUD值被清零。</td></tr></table>

## 重装载寄存器（FWDGT_RLD）

地址偏移：0x08

复位值：0x0000 0FFF

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">RLD [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>RLD[11:0]</td><td>独立看门狗定时器计数器重装载值,向FWDGT_CTL寄存器写入0xAAAA的时候,这个值会被更新到看门狗定时器计数器中。这些位有写保护功能。在写这些位之前需向FWDGT_CTL寄存器中写0x5555。在改写这个寄存器的过程中,FWDGT_STAT寄存器的RUD位被置1,从此寄存器中读取的任何值都是无效的。如果应用需要使用几个重装载值,改变重加载值之前必须等到RUD位被清0。更新了重加载寄存器的值后,在代码持续执行之前不必等待RUD值被清零。</td></tr></table>

状态寄存器（FWDGT_STAT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13"></td><td>WUD</td><td>RUD</td><td>PUD</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>WUD</td><td>独立看门狗定时器计数器窗口值更新FWDGT_WND寄存器写操作时,该位被置1,此时读取FWDGT_WND寄存器的任何值都是无效的。</td></tr><tr><td>1</td><td>RUD</td><td>独立看门狗定时器计数器重装载值更新FWDGT_RLD寄存器写操作时,该位被置1,此时读取FWDGT_RLD寄存器的任何值都是无效的。在FWDGT_RLD寄存器更新后,该位由硬件清零。</td></tr><tr><td>0</td><td>PUD</td><td>独立看门狗定时器预分频值更新FWDGT_PSC寄存器写操作时,该位被置1,此时读取FWDGT_PSC寄存器的任何值都是无效的。在FWDGT_PSC寄存器更新后,该位由硬件清零。</td></tr></table>

## 窗口寄存器（FWDGT_WND）

地址偏移：0x10

复位值：0x0000 0FFF

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">WND[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>WND</td><td>独立看门狗定时器计数器窗口值。这些位将用来将窗口值的上限值与向下递减计数器进行比较。当计数值大于WND[11:0]中值,重装载操作会引起复位,若要改变重装载值,FWDGT_STAT寄存器中的WUD位必须保持复位状态。这些位有写保护功能。在写这些位之前需向FWDGT_CTL寄存器中写0x5555。</td></tr></table>

如果应用需要使用几个窗口值，改变窗口值之前必须等到WUD位被清0。除了在进入低功耗模式下，更新了窗口值后，在代码持续执行之前不必等待WUD值被清零。

## 21.2. 窗口看门狗定时器（WWDGT）

## 21.2.1. 简介

窗口看门狗定时器（WWDGT）用来监测由软件故障导致的系统故障。窗口看门狗定时器开启后，7位向下递减计数器值逐渐减小。计数值达到0x3F时会产生复位（CNT[6]位被清0）。在计数器计数值达到窗口寄存器值之前，计数器的更新也会产生复位。因此软件需要在给定的区间内更新计数器。窗口看门狗定时器在计数器计数值达到0x40，都会产生一个提前唤醒标志，如果使能中断也将会产生中断。

窗口看门狗定时器时钟是由APB1时钟预分频而来。窗口看门狗定时器适用于需要精确计时的场合。

## 21.2.2. 主要特征

 可编程的7位自由运行向下递减计数器。

 当窗口看门狗使能后，有以下两种情况会产生复位：

当计数器达到0x3F时产生复位；

当计数器的值大于窗口寄存器的值时，更新计数器会产生复位。

 提前唤醒中断（EWI）：如果看门狗定时器打开，支持中断，当计数值达到0x40时，会产生中断。

 可以配置窗口看门狗定时器在调试模式下选择停止还是继续工作。

## 21.2.3. 功能说明

如果窗口看门狗定时器使能（将WWDGT_CTL寄存器的WDGTEN位置1），计数值达到0x3F的时候产生复位（CNT[6]位被清0），或者，在计数值达到窗口寄存器值之前，更新计数器也会产生复位。


图 21-2. 窗口看门狗定时器框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/4f2ff47c46514a22e1aa1c214e9a1d3bc92968eb8eef148190161c7bc494341e.jpg)



上电复位之后看门狗定时器总是关闭的。软件可以向WWDGT_CTL的WDGTEN写1开启看门狗定


时器。窗口看门狗定时器打开后，计数器始终递减计数，计数器配置的值应该大于0x3F，也就是说CNT[6:0]位应该被置1。CNT[6:0]决定了两次重装载之间的最大间隔时间。计数器的递减速度取决于APB1时钟和预分频器(WWDGT_CFG寄存器的PSC[1:0]位)。

配置寄存器（WWDGT_CFG）中的WIN[6:0]位用来设定窗口值。当计数器的值小于窗口值，且大于0x3F的时候，重装载向下计数器可以避免复位，否则在其他时候进行重加载就会引起复位。

对WWDGT_CFG寄存器的EWIE位置1可以使能提前唤醒中断（EWI），当计数值达到0x40的时候该中断产生。同时可以用相应的中断服务程序（ISR）来触发特定的行为（例如通信或数据记录），来分析软件故障的原因以及在器件复位的时候挽救重要数据。此外，在ISR中软件可以重装载计数器来管理软件系统检查等。在这种情况下，窗口看门狗定时器将永远不会复位但是可以用于其他地方。

通过将WWDGT_STAT寄存器的EWIF位写0可以清除EWI中断。


图 21-3. 窗口看门狗定时器时序图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/2660ccd3-374c-4409-9a1d-80e08ca01452/dae0b643ccccde839728529ce43d3a783a3d5ac1ed39c75d160963cef3548e13.jpg)


窗口看门狗定时器超时的计算公式如下：

$$
t _ {W W D G T} = t _ {P C L K 1} \times 4 0 9 6 \times 2 ^ {P S C} \times (C N T [ 6: 0 ] + 1) (m s)\tag{21-1}
$$

其中：

t<sub>WWDGT</sub>：窗口看门狗定时器的超时时间t<sub>PCLK1</sub>： APB1以ms为单位的时钟周期

t<sub>WWDGT</sub>的最大值和最小值请参考 21-2. 216MHz (fPCLK1) / 。


表 21-2. 在 216MHz (f<sub>PCLK1</sub>)时的最大/最小超时值


<table><tr><td>预分频系数</td><td>PSC[1:0]</td><td>最小超时CNT[6:0] =0x40</td><td>最大超时CNT[6:0]=0x7F</td></tr><tr><td>1/1</td><td>00</td><td>18.96 μs</td><td>1.21 ms</td></tr><tr><td>1/2</td><td>01</td><td>37.93 μs</td><td>2.43 ms</td></tr><tr><td>1/4</td><td>10</td><td>75.85 μs</td><td>4.85 ms</td></tr><tr><td>1/8</td><td>11</td><td>151.70μs</td><td>9.71 ms</td></tr></table>

如果DBG模块中的WWDGT_HOLD位被清0，即使Cortex<sup>®</sup>-M33内核停止工作(调试模式下)，窗口看门狗定时器也可以继续工作。当WWDGT_HOLD位被置1时，窗口看门狗定时器会随着内核停止工作而停止计数。

## 21.2.4. WWDGT 寄存器

WWDGT 基地址：0x40002C00

## 控制寄存器（WWDGT_CTL）

地址偏移：0x00

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>WDGTEN</td><td colspan="7">CNT[6:0]</td></tr><tr><td colspan="8"></td><td>rs</td><td colspan="7">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>WDGTEN</td><td>开启窗口看门狗定时器,硬件复位的时候清0,写0无效。0:关闭窗口看门狗定时器1:开启窗口看门狗定时器</td></tr><tr><td>6:0</td><td>CNT[6:0]</td><td>看门狗定时器计数器的值。当计数值从0x40降到0x3F时,产生看门狗定时器复位。当计数器值高于窗口值的时候,写计数器可以产生看门狗定时器复位。</td></tr></table>

配置寄存器（WWDGT_CFG）

地址偏移：0x04

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>EWIE</td><td colspan="2">PSC[1:0]</td><td colspan="7">WIN[6:0]</td></tr><tr><td colspan="6"></td><td>rs</td><td colspan="2">rw</td><td colspan="7">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EWIE</td><td>提前唤醒中断使能。如果该位被置1,计数值达到0x40时触发中断,能触发中断。该位由硬件复位清0,或通过RCU模块的WWDGT软件复位来清0。写0没有任何作用。</td></tr><tr><td>8:7</td><td>PSC[1:0]</td><td>预分频器,看门狗定时器的时间基准。00:(PCLK1 / 4096) / 101:(PCLK1 / 4096) / 210:(PCLK1 / 4096) / 411:(PCLK1 / 4096) / 8</td></tr><tr><td>6:0</td><td>WIN[6:0]</td><td>窗口值,当看门狗定时器计数器的值大于窗口值时,写看门狗定时器计数器(WWDGT_CTL的CNT位)会产生复位。</td></tr></table>

## 状态寄存器（WWDGT_STAT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EWIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EWIF</td><td>提前唤醒中断标志位。当计数值达到0x40,更新计数器,即使中断没有被使能(WWDGT_CFG中的EWIE位为0)该位也会被硬件置1。这个bit可以通过写0清零,写1无效。</td></tr></table>
