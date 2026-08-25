## 11.5. CLA 寄存器

CLA基地址：0x4003 8000

## 11.5.1. 全局控制寄存器 (CLA_GCTL)

地址偏移：0x00

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>CLA3EN</td><td>CLA2EN</td><td>CLA1EN</td><td>CLA0EN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>CLA3EN</td><td>CLA3单元使能该位由软件置位和清除0:禁能CAL3单元1:使能CLA3单元</td></tr><tr><td>2</td><td>CLA2EN</td><td>CLA2单元使能该位由软件置位和清除0:禁能CAL2单元1:使能CLA2单元</td></tr><tr><td>1</td><td>CLA1EN</td><td>CLA1单元使能该位由软件置位和清除0:禁能CAL1单元1:使能CLA1单元</td></tr><tr><td>0</td><td>CLA0EN</td><td>CLA0单元使能该位由软件置位和清除0:禁能CAL0单元1:使能CLA0单元</td></tr></table>

## 11.5.2. 中断使能寄存器(CLA_INTE)

地址偏移：0x04

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>CLA3PIE</td><td>CLA3NIE</td><td>CLA2PIE</td><td>CLA2NIE</td><td>CLA1PIE</td><td>CLA1NIE</td><td>CLA0PIE</td><td>CLA0NIE</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>CLA3PIE</td><td>CLA3单元上升沿中断使能该位由软件置位和清除0:禁能CLA3单元上升沿中断1:使能CLA3单元上升沿中断。当CLA3PF位置位时,会产生中断。</td></tr><tr><td>6</td><td>CLA3NIE</td><td>CLA3单元下降沿中断使能该位由软件置位和清除0:禁能CLA3单元下降沿中断1:使能CLA3单元下降沿中断。当CLA3NF位置位时,会产生中断。</td></tr><tr><td>5</td><td>CLA2PIE</td><td>CLA2单元上升沿中断使能该位由软件置位和清除0:禁能CLA2单元上升沿中断1:使能CLA2单元上升沿中断。当CLA2PF位置位时,会产生中断。</td></tr><tr><td>4</td><td>CLA2NIE</td><td>CLA2单元下降沿中断使能该位由软件置位和清除0:禁能CLA2单元下降沿中断1:使能CLA2单元下降沿中断。当CLA2NF位置位时,会产生中断。</td></tr><tr><td>3</td><td>CLA1PIE</td><td>CLA1单元上升沿中断使能该位由软件置位和清除0:禁能CLA1单元上升沿中断1:使能CLA1单元上升沿中断。当CLA1PF位置位时,会产生中断。</td></tr><tr><td>2</td><td>CLA1NIE</td><td>CLA1单元下降沿中断使能该位由软件置位和清除0:禁能CLA1单元下降沿中断1:使能CLA1单元下降沿中断。当CLA1NF位置位时,会产生中断。</td></tr><tr><td>1</td><td>CLA0PIE</td><td>CLA0单元上升沿中断使能该位由软件置位和清除</td></tr></table>

<table><tr><td></td><td></td><td>0:禁能CLA0单元上升沿中断1:使能CLA0单元上升沿中断。当CLA0PF位置位时,会产生中断。</td></tr><tr><td>0</td><td>CLA0NIE</td><td>CLA0单元下降沿中断使能该位由软件置位和清除0:禁能CLA0单元下降沿中断1:使能CLA0单元下降沿中断。当CLA0NF位置位时,会产生中断。</td></tr></table>

## 11.5.3. 中断标志寄存器 (CLA_INTF)

地址偏移：0x08

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>CLA3PF</td><td>CLA3NF</td><td>CLA2PF</td><td>CLA2NF</td><td>CLA1PF</td><td>CLA1NF</td><td>CLA0PF</td><td>CLA0NF</td></tr><tr><td colspan="8"></td><td>rs_w0</td><td>rs_w0</td><td>rs_w0</td><td>rs_w0</td><td>rs_w0</td><td>rs_w0</td><td>rw_w0</td><td>rs_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>CLA3PF</td><td>CLA3单元上升沿标志该位由硬件置位,软件清除0:没有检测到CLA3的上升沿输出1:检测到CLA3的上升沿输出</td></tr><tr><td>6</td><td>CLA3NF</td><td>CLA3单元下降沿标志该位由硬件置位,软件清除0:没有检测到CLA3的下降沿输出1:检测到CLA3的下降沿输出</td></tr><tr><td>5</td><td>CLA2PF</td><td>CLA2单元上升沿标志该位由硬件置位,软件清除0:没有检测到CLA2的上升沿输出1:检测到CLA2的上升沿输出</td></tr><tr><td>4</td><td>CLA2NF</td><td>CLA2单元下降沿标志该位由硬件置位,软件清除0:没有检测到CLA2的下降沿输出1: 检测到CLA2的下降沿输出</td></tr><tr><td>3</td><td>CLA1PF</td><td>CLA1单元上升沿标志该位由硬件置位,软件清除0: 没有检测到CLA1的上升沿输出1: 检测到CLA1的上升沿输出</td></tr><tr><td>2</td><td>CLA1NF</td><td>CLA1单元下降沿标志该位由硬件置位,软件清除0: 没有检测到CLA1的下降沿输出1: 检测到CLA1的下降沿输出</td></tr><tr><td>1</td><td>CLA0PF</td><td>CLA0单元上升沿标志该位由硬件置位,软件清除0: 没有检测到CLA0的上升沿输出1: 检测到CLA0的上升沿输出</td></tr><tr><td>0</td><td>CLA0NF</td><td>CLA0单元下降沿标志该位由硬件置位,软件清除0: 没有检测到CLA0的下降沿输出1: 检测到CLA0的下降沿输出</td></tr></table>

## 11.5.4. 状态寄存器 (CLA_STAT)

地址偏移：0x0C

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>CLA3OUT</td><td>CLA2OUT</td><td>CLA1OUT</td><td>CLA0OUT</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>CLA3OUT</td><td>CLA3单元输出状态该位由硬件置位和清除0: CLA3单元的当前逻辑电平为低1: CLA3单元的当前逻辑电平为高</td></tr><tr><td>2</td><td>CLA2OUT</td><td>CLA2单元输出状态该位由硬件置位和清除0: CLA2单元的当前逻辑电平为低1: CLA2单元的当前逻辑电平为高</td></tr><tr><td>1</td><td>CLA1OUT</td><td>CLA1单元输出状态该位由硬件置位和清除0: CLA1单元的当前逻辑电平为低1: CLA1单元的当前逻辑电平为高</td></tr><tr><td>0</td><td>CLA0OUT</td><td>CLA0单元输出状态该位由硬件置位和清除0: CLA0单元的当前逻辑电平为低1: CLA0单元的当前逻辑电平为高</td></tr></table>

## 11.5.5. 信号选择寄存器 (CLAx_SIGS)(x=0..3)

地址偏移：0x10 + 0x0C * x

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">SIGS0[3:0]</td><td colspan="4">SIGS1[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:4</td><td>SIGS0[3:0]</td><td>信号选择器0输入选择该位由软件置位和清除这些位选择信号选择器0的输入。请参考表11-1.CLxSIGS0输入选择</td></tr><tr><td>3:0</td><td>SIGS1[3:0]</td><td>信号选择器1输入选择该位由软件置位和清除这些位选择信号选择器1的输入。请参考表11-2.CLxSIGS1输入选择</td></tr></table>

## 11.5.6. LCU 控制寄存器 (CLAx_LCUCTL)(x=0..3)

地址偏移：0x14 + 0x0C * x

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">LCU[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>LCU[7:0]</td><td>LCU控制由软件置位和清除这些位控制input0、input1、input2的哪个逻辑函数会对输出产生影响。例如:IN1 | IN2: LCU = 8&#x27;b11101110IN0 &amp; (IN1^IN2): LCU = 8&#x27;b01100000</td></tr></table>

## 11.5.7. 控制寄存器 (CLAx_CTL)(x=0..3)

地址偏移：0x18 + 0x0C * x

复位值：0x0000 0000（必须是power reset）

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>OSEL</td><td>OEN</td><td colspan="2">保留</td><td>FFRST</td><td>CPOL</td><td colspan="2">CSEL[1:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td colspan="2"></td><td>w</td><td>rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>OSEL</td><td>输出选择由软件置位和清除0:触发器的输出作为CLAx的输出</td></tr></table>

<table><tr><td>6</td><td>OEN</td><td>输出使能由软件置位和清除0: CLAx输出禁能1: CLAx输出使能</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3</td><td>FFRST</td><td>触发器输出复位0: 没有作用1: 复位触发器输出异步</td></tr><tr><td>2</td><td>CPOL</td><td>触发器时钟极性选择由软件置位和清除当CLAx使能时(CLAxEN = 1)禁止修改该位域0: 时钟上升沿有效1: 时钟下降沿有效</td></tr><tr><td>1:0</td><td>CSEL[1:0]</td><td>触发器时钟源选择由软件置位和清除当CLAx使能时(CLAxEN = 1)禁止修改该位域00: CLA[x-1] LCU的结果01: SIGS0输出10: HCLK11: TIMER_TRGO</td></tr></table>
