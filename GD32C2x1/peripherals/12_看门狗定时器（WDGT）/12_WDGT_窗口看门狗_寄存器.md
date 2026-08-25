## 12.2.4. WWDGT 寄存器

WWDGT 基地址：0x4000 2C00

控制寄存器（WWDGT_CTL）

地址偏移：0x00

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>WDGTEN</td><td>开启窗口看门狗定时器,硬件复位的时候清0,写0无效。0:关闭窗口看门狗定时器。1:开启窗口看门狗定时器。</td></tr><tr><td>6:0</td><td>CNT[6:0]</td><td>看门狗定时器计数器的值。当计数值从0x40降到0x3F时,产生看门狗定时器复位。当计数器值高于窗口值的时候,写计数器可以产生看门狗定时器系统复位。</td></tr></table>

## 配置寄存器（WWDGT_CFG）

地址偏移：0x04

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">PSC[3:2]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>EWIE</td><td colspan="2">PSC[1:0]</td><td colspan="7">WIN[6:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>PSC[3:2]</td><td>预分频器,这些位和PSC[1:0]共同决定看门狗定时器的时间基准。0000:(PCLK1 / 4096) / 10001:(PCLK1 / 4096) / 20010:(PCLK1 / 4096) / 40011: (PCLK1/4096)/8</td></tr><tr><td></td><td></td><td>0100: (PCLK1/4096)/16</td></tr><tr><td></td><td></td><td>0101: (PCLK1/4096)/32</td></tr><tr><td></td><td></td><td>0110: (PCLK1/4096)/64</td></tr><tr><td></td><td></td><td>0111: (PCLK1/4096)/128</td></tr><tr><td></td><td></td><td>1000: (PCLK1/4096)/256</td></tr><tr><td></td><td></td><td>1001: (PCLK1/4096)/512</td></tr><tr><td></td><td></td><td>1010: (PCLK1/4096)/1024</td></tr><tr><td></td><td></td><td>1011: (PCLK1/4096)/2048</td></tr><tr><td></td><td></td><td>1100: (PCLK1/4096)/4096</td></tr><tr><td></td><td></td><td>1101: (PCLK1/4096)/8192</td></tr><tr><td></td><td></td><td>1110: (PCLK1/4096)/1</td></tr><tr><td></td><td></td><td>1111: (PCLK1/4096)/1</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EWIE</td><td>提前唤醒中断使能。如果该位被置1,计数值达到0x40时触发中断。该位由硬件复位清0,或通过置位RCU模块的WWDGTRST位进行软件复位。写0没有任何作用。</td></tr><tr><td>8:7</td><td>PSC[1:0]</td><td>预分频器,这些位和PSC[3:2]共同决定看门狗定时器的时间基准。</td></tr><tr><td>6:0</td><td>WIN[6:0]</td><td>窗口值,当看门狗定时器计数器的值大于窗口值时,写看门狗定时器计数器(WWDGT_CTL的CNT位)会产生系统复位。</td></tr></table>

## 状态寄存器（WWDGT_STAT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EWIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EWIF</td><td>提前唤醒中断标志位。当计数值达到0x40,即使中断没有被使能(WWDGT_CFG中的EWIE位为0)该位也会被硬件置1。这个bit可以通过写0清零,写1无效。</td></tr></table>
