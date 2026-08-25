## 5.4. CTC 寄存器

CTC基地址：0x4000 6C00

## 5.4.1. 控制寄存器 0（CTC_CTL0）

地址偏移：0x00

复位值：0x0000 2000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="7">TRIMVALUE[5:0]</td><td>SWREFPUL</td><td>AUTOTRIM</td><td>CNTEN</td><td>保留</td><td>EREFIE</td><td>ERRIE</td><td>CKWARNIE</td><td>CKOKIE</td></tr><tr><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td>w</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>TRIMVALUE[5:0]</td><td>IRC48M 校准值当 CTC_CTL0 中的 AUTOTRIM 值为 0 时,该位由软件置位和清除,该模式用于软件校准过程。当 CTC_CTL0 中的 AUTOTRIM 值为 1 时,该位只读,由硬件自动修改,该模式用于硬件校准过程。TRIMVALUE 的中间值是 32,当 TRIMVALUE 值加 1 时,IRC48M 时钟频率增加大约 57KHz。当 TRIMVALUE 值减 1 时,IRC48M 时钟频率的减少大约 57KHz。</td></tr><tr><td>7</td><td>SWREFPUL</td><td>软件生成同步参考信号脉冲该位由软件置位,并为 CTC 计数器提供一个同步参考脉冲信号。该位由硬件自动清除,读操作时返回 0。0:没有影响1:软件产生一个同步参考脉冲信号</td></tr><tr><td>6</td><td>AUTOTRIM</td><td>硬件自动校准模式该位由软件置位或清除。当该位置 1 时,硬件自动校准模式使能,通过硬件不断的自动修改 CTC_CTL0 中的 TRIMVALUE 值,直到 IRC48M 的时钟频率达到 48MHz。0:禁止硬件自动校准模式1:使能硬件自动校准模式</td></tr><tr><td>5</td><td>CNTEN</td><td>CTC 计数器使能该位由软件置位或清除,用于使能或禁止 CTC 计数器。当该位置 1 时,不能修改 CTC_CTL1 的值。0:禁止 CTC 计数器</td></tr></table>

1: 使能 CTC 计数器

4 保留 必须保持复位值。

3 EREFIE 期望参考信号中断使能

0: 禁止期望参考信号产生中断

1: 使能期望参考信号产生中断

2 ERRIE 错误中断使能

0: 禁止错误中断

1: 使能错误中断

1 CKWARNIE 时钟校准警告中断使能

0: 禁止时钟校准警告中断

1: 使能时钟校准警告中断

0 CKOKIE 时钟校准完成中断使能

0: 禁止时钟校准完成中断

1: 使能时钟校准完成中断

## 5.4.2. 控制寄存器 1（CTC_CTL1）

地址偏移：0x04

复位值：0x2022 BB7F

该寄存器只能按字（32位）访问。

注意：当CNTEN为1时，不能修改该寄存器的值。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>REFPOL</td><td>保留</td><td colspan="2">REFSEL[1:0]</td><td>保留</td><td colspan="3">REFPSC[2:0]</td><td colspan="8">CKLIM[7:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="2">rw</td><td></td><td colspan="3">rw</td><td colspan="3"></td><td colspan="3">rw</td><td colspan="2"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RLVALUE[15:0]</td></tr></table>


rw



位/位域 名称 描述


<table><tr><td>31</td><td>REFPOL</td><td>参考信号源极性该位由软件置位或清除,用于选择参考信号源的同步极性0:选择上升沿1:选择下降沿</td></tr><tr><td>30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29:28</td><td>REFSEL[1:0]</td><td>参考信号源选择该位由软件置位或清除,用于选择参考信号源00:选择 GPIO(CTC_SYNC)输入信号01:选择 LXTAL 时钟</td></tr></table>

<table><tr><td></td><td></td><td>10:保留11:保留</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>REFPSC[2:0]</td><td>参考信号源预分频该位由软件置位或清除000:参考信号不分频001:参考信号2分频010:参考信号4分频011:参考信号8分频100:参考信号16分频101:参考信号32分频110:参考信号64分频111:参考信号128分频</td></tr><tr><td>23:16</td><td>CKLIM[7:0]</td><td>时钟校准时基限值该位由软件置位或清除,用于定义时钟校准时基限值。该位用于频率评估和自动校准过程,详细情况请参考频率评估和自动校准过程。</td></tr><tr><td>15:0</td><td>RLVALUE[15:0]</td><td>CTC计数器重载值该位由软件置位或清除,用于定义CTC计数器的重载值,当检测到一个同步参考脉冲时,该值将重载到CTC校准计数器中。</td></tr></table>

## 5.4.3. 状态寄存器（CTC_STAT）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 bit）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">REFCAP[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>REFDIR</td><td colspan="4">保留</td><td>TRIMERR</td><td>REFMISS</td><td>CKERR</td><td colspan="4">保留</td><td>EREFIF</td><td>ERRIF</td><td>CKWARNIF</td><td>CKOKIF</td></tr><tr><td colspan="5">r</td><td>r</td><td>r</td><td colspan="5">r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>REFCAP[15:0]</td><td>CTC计数器捕获值当检测到一个同步参考脉冲信号时,CTC校准计数器中的计数值被存入到REFCAP位中。</td></tr><tr><td>15</td><td>REFDIR</td><td>CTC校准时钟计数方向当检测到一个同步参考脉冲信号时,CTC校准计数器的计数方向被存入REFDIR位中。0:向上计数1:向下计数</td></tr><tr><td>14:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>TRIMERR</td><td>校准值错误位当CTC_CTL0中的TRIMVALUE值发生上溢或下溢时,该位由硬件置位。若CTC_CTL0中的ERRIE位置1,则会产生一个中断。通过写1到CTC_INTC中的ERRIC位,可以将TRIMERR位清零。0:无校准值错误发生1:发生校准值错误</td></tr><tr><td>9</td><td>REFMISS</td><td>同步参考脉冲信号丢失当同步参考脉冲信号丢失时,该位由硬件置位。当CTC校准计数器在增计数的过程中计数到128xCKLIM都没有检测到同步参考脉冲信号时,REFMISS位置位。说明当前时钟太快,无法校准到期望频率值,或者有其他错误产生。通过写1到CTC_INTC中的ERRIC位,可以将REFMISS位清零。0:无同步参考脉冲信号丢失1:同步参考脉冲信号丢失</td></tr><tr><td>8</td><td>CKERR</td><td>时钟校准错误位当时钟校准错误产生时,该位由硬件置位。当CTC校准计数器计数值在减计数的过程中大于或等于128xCKLIM,并检测到同步参考脉冲信号时,CKERR置位,说明当前时钟太慢,无法校准到期望频率值。当CTC_CTL0中的ERRIE置1时,产生一个中断。通过写1到CTC_INTC中的ERRIC位,可以将CKERR位清零。0:无时钟校准错误发生1:发生时钟校准错误</td></tr><tr><td>7:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>EREFIF</td><td>期望参考中断标志位当CTC校准时钟计数器计数到0时,该位由硬件置位。当CTC_CTL0中的EREFIE置1时,产生一个中断。通过写1到CTC_INTC中的EREFIC位,可以将EREFIF位清零。0:无期望参考信号产生1:期望参考信号产生</td></tr><tr><td>2</td><td>ERRIF</td><td>错误中断标志位当发生一个错误时,该位由硬件置位。只要有TRIMERR,REFMISS或者CKERR错误发生时,该位置位。当CTC_CTL0中的ERRIE置位时,产生一个中断。通过写1到CTC_INTC中的ERRIC位,可以将ERRIF位清零。0:无错误发生1:发生错误</td></tr><tr><td>1</td><td>CKWARNIF</td><td>时钟校准警告中断标志位当时钟校准警告产生时,该位由硬件置位。当CTC校准计数器计数值大于或等于3xCKLIM且小于128xCKLIM,并检测到同步参考脉冲信号时,CKWARNIF置位。</td></tr></table>

这说明当前时钟频率太慢或者太快，但可以通过校准达到期望频率值。当时钟校准警告产生时，TRIMVALUE 值加 2 或者减 2。当 CTC_CTL0 中的 CKWARNIE 置 1 时，产生一个中断。通过写 1 到 CTC_INTC 中的 CKWARNIC 位，可以将 CKWARNIF 位清零。

0: 无时钟校准警告发生

1: 有时钟校准警告发生

0 CKOKIF 

时钟校准成功中断标志位

当时钟校准成功时，该位由硬件置位。若在 CTC 校准计数器计数值小于 3 x CKLIM 时，检测当同步参考脉冲信号，CKOKIF 置位。说明当前时钟频率正常，可以使用，不需要通过 TRIMVALUE 值进行时钟校准。当 CTC_CTL0 中的 CKOKIE 置 1 时，产生一个中断。通过写 1 到 CTC_INTC 中的 CKOKIE 位，可以将 CKOKIF 位清零。

0: 时钟校准未成功

1: 时钟校准成功

## 5.4.4. 中断清除寄存器（CTC_INTC）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 bit）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>EREFIC</td><td>ERRIC</td><td>CKWARNIC</td><td>CKOKIC</td></tr></table>


W W W W 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>EREFIC</td><td>EREFIF 中断清除位该位只能由软件写,读操作返回 0。写 1 可以清除 CTC_STAT 中的 EREFIF 位,写 0 没影响。</td></tr><tr><td>2</td><td>ERRIC</td><td>ERRIF 中断清除位该位只能由软件写,读操作返回 0。写 1 可以清除 CTC_STAT 中的 ERRIF 位,TRIMERR 位,REFMISS 位和 CKERR 位,写 0 没影响。</td></tr><tr><td>1</td><td>CKWARNIC</td><td>CKWARNIF 中断清除位该位只能由软件写,读操作返回 0。写 1 可以清除 CTC_STAT 中的 CKWARNIF 位,写 0 没影响。</td></tr><tr><td>0</td><td>CKOKIC</td><td>CKOKIF 中断清除位该位只能由软件写,读操作返回 0。写 1 可以清除 CTC_STAT 中的 CKOKIF 位,写</td></tr></table>

0 没影响。
