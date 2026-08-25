## 10.5. TMU 寄存器

TMU 基地址：0x4008 0000

## 10.5.1. 输入数据 0 寄存器 (TMU_IDATA0)

地址偏移：0x00

复位值：0x3F80 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDATA0[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDATA0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDATA0[31:0]</td><td>输入的数值模式 0~5: 只使用 TMU_IDATA0模式 6: TMU_IDATA0 用于存放 X 的值模式 7: TMU_IDATA0 用于存放被除数模式 8: TMU_IDATA0 用于存放 X 或 Y 的值TMU_IDATA0 必须符合 IEEE-32 位单精度浮点格式。</td></tr></table>

## 10.5.2. 输入数据 1 寄存器(TMU_IDATA1)

地址偏移：0x04

复位值：0x3F80 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDATA1[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDATA1[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDATA1[31:0]</td><td>输入的数值模式 0~5: 不使用 TMU_IDATA1模式 6: TMU_IDATA1 用于存放 Y 的值模式 7: TMU_IDATA1 用于存放除数的值模式 8: IDATA1 用于存放 X 或 Y 的值</td></tr></table>

TMU_IDATA1 必须符合 IEEE-32 位单精度浮点格式。

## 10.5.3. 控制寄存器(TMU_CTL)

地址偏移：0x08

复位值：0x0000 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>CFIF</td><td>CFIE</td><td colspan="4">MODE</td><td>TMUEN</td></tr><tr><td colspan="9"></td><td>ro</td><td>rw</td><td></td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6</td><td>CFIF</td><td>计算完成标志位当 CFIE 使能时,一旦计算完成,此位被置 1 并产生中断信号。读取 TMU_DATA0、TMU_DATA1 或 TMU_STAT 寄存器,此位被清零。</td></tr><tr><td>5</td><td>CFIE</td><td>计算完成中断使能位1:使能计算完成中断0:禁止计算完成中断</td></tr><tr><td>4:1</td><td>MODE[3:0]</td><td>配置 TMU 操作模式:0000: R0 = x*2π0001: R0 = x/2π0010: R0 = <eq>\sqrt{x}</eq>0011: R0 = sin(x)0100: R0 = cos(x)0101: R0 = arctan(x)0110: R0 = Ratio of X &amp; Y, R1 = Quadrant value0111: R0 = x/y1000: R0 = <eq>\sqrt{x^2 + y^2}</eq>1001~1111: 保留</td></tr><tr><td>0</td><td>TMUEN</td><td>TMU 使能位该位置 1,开始 TMU 模块计算功能,当完成计算时,该位被硬件清零。</td></tr></table>

## 10.5.4. 数据 0 寄存器(TMU_DATA0)

地址偏移：0x0C复位值：0x3400 0000该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA0[31:16]</td></tr><tr><td colspan="16">ro</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA0[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA0[31:0]</td><td>计算结果模式 0~5,7,8: 只使用 TMU_DATA0模式 6: TMU_DATA0 存放 X 和 Y 的比值结果TMU_DATA0 必须符合 IEEE-32 位单精度浮点格式。</td></tr></table>

## 10.5.5. 数据 1 寄存器(TMU_DATA1)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA1[31:16]</td></tr><tr><td colspan="16">ro</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA1[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA1[31:0]</td><td>计算结果模式 0~5,7,8: 不使用 TMU_DATA1模式 6: TMU_DATA1= Quadrant value (0.0, ±0.25, ±0.5)TMU_DATA1 必须符合 IEEE-32 位单精度浮点格式。</td></tr></table>

## 10.5.6. 状态寄存器(TMU_STAT)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>UDRF</td><td>OVRF</td></tr><tr><td colspan="14">位/位域</td><td>名称</td><td>描述</td></tr><tr><td colspan="14">31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td colspan="14">1</td><td>UDRF</td><td>下溢标志位0:没有下溢1:产生下溢该位由硬件清零或置位,当启动下一次TMU计算时,该位被硬件清零。</td></tr><tr><td colspan="14">0</td><td>OVRF</td><td>上溢标志位0:没有上溢1:产生上溢该位由硬件清零或置位,当启动下一次TMU计算时,该位被硬件清零。</td></tr></table>
