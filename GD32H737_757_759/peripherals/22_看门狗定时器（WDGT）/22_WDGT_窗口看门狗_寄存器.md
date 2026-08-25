# 22.2.4. WWDGT 寄存器

WWDGT 基地址：0x5000 3000

# 控制寄存器（WWDGT_CTL）

地址偏移：0x00

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>WDGTEN</td><td colspan="7">CNT[6:0]</td></tr><tr><td colspan="9">rs</td><td colspan="7">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>WDGTEN</td><td>开启窗口看门狗定时器,硬件复位的时候清0,写0无效。0:关闭窗口看门狗定时器1:开启窗口看门狗定时器</td></tr><tr><td>6:0</td><td>CNT[6:0]</td><td>看门狗定时器计数器的值。当计数值从0x40降到0x3F时,产生看门狗定时器复位。当计数器值高于窗口值的时候,写计数器可以产生看门狗定时器复位。</td></tr></table>

# 配置寄存器（WWDGT_CFG）

地址偏移：0x04

复位值：0x0000 007F

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>EWIE</td><td colspan="2">PSC[1:0]</td><td colspan="7">WIN[6:0]</td></tr><tr><td colspan="6"></td><td>rs</td><td colspan="2">rw</td><td colspan="2"></td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EWIE</td><td>提前唤醒中断使能。如果该位被置1,计数值达到0x40时触发中断,能触发中断。该位由硬件复位清0,或通过RCU模块的WWDGT软件复位来清0。写0没有任何作用。</td></tr><tr><td>8:7</td><td>PSC[1:0]</td><td>预分频器,看门狗定时器的时间基准。00:(PCLK3 / 4096) / 1</td></tr></table>

01：(PCLK3 / 4096) / 2 

10：(PCLK3 / 4096) / 4 

11：(PCLK3 / 4096) / 8 

6:0 WIN[6:0] 

窗口值，当看门狗定时器计数器的值大于窗口值时，写看门狗定时器计数器（WWDGT_CTL的CNT位）会产生复位。

# 状态寄存器（WWDGT_STAT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>EWIF</td></tr></table>

rc_w0 

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>EWIF</td><td>提前唤醒中断标志位。当计数值达到0x40或达到窗口值之前,更新计数器,即使中断没有被使能(WWDGT_CFG中的EWIE位为0)该位也会被硬件置1。这个bit可以通过写0清零,写1无效。</td></tr></table>
