## 14.4. DAC 寄存器

DAC0 基地址：0x4000 7400

DAC1 基地址：0x4000 D000

## 14.4.1. DACx 控制寄存器（DAC_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器的[31:16]位域仅可用于 DAC0，在 DAC1 中必须保持复位值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DDISC1</td><td>DTSEL1[3]</td><td>DDUDRIE1</td><td>DDMAEN1</td><td colspan="4">DWBW1[3:0]</td><td colspan="2">DWM1[1:0]</td><td colspan="3">DTSEL1[2:0]</td><td>DTEN1</td><td>DBOFF1</td><td>DEN1</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DDISCO</td><td>DTSELO[3]</td><td>DDUDRIE0</td><td>DDMAENO</td><td colspan="4">DWBW0[3:0]</td><td colspan="2">DWM0[1:0]</td><td colspan="3">DTSELO[2:0]</td><td>DTENO</td><td>DBOFF0</td><td>DEN0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DDISC1</td><td>DACx_OUT1 连接 GPIO 选择0: DACx_OUT1 连接到外部管脚和片上外设(CMP)1: 当输出缓冲区关闭时(DBOFF1=1)仅连接到片上外设(CMP),缓冲区打开时连接到外部管脚和片上外设(CMP)</td></tr><tr><td>30</td><td>DTSEL1[3]</td><td>DACx_OUT1 触发源选择的位[3],参考 DTSEL1[2:0]。</td></tr><tr><td>29</td><td>DDUDRIE1</td><td>DACx_OUT1 DMA 欠载中断使能0: DACx_OUT1 DMA 欠载中断禁能1: DACx_OUT1 DMA 欠载中断使能</td></tr><tr><td>28</td><td>DDMAEN1</td><td>DACx_OUT1 DMA 使能0: DACx_OUT1 DMA 模式禁能1: DACx_OUT1 DMA模式使能</td></tr><tr><td>27:24</td><td>DWBW1[3:0]</td><td>DACx_OUT1 噪声波位宽这些位指定了 DACx_OUT1 的噪声波信号的位宽。LFSR 噪声模式下,这些位表示不屏蔽 LFSR 的位[n-1, 0]:三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n为噪声波位宽。0000:波形信号的位宽为10001:波形信号的位宽为20010:波形信号的位宽为30011:波形信号的位宽为40100:波形信号的位宽为5</td></tr><tr><td rowspan="7"></td><td rowspan="7"></td><td>0101:波形信号的位宽为6</td></tr><tr><td>0110:波形信号的位宽为7</td></tr><tr><td>0111:波形信号的位宽为8</td></tr><tr><td>1000:波形信号的位宽为9</td></tr><tr><td>1001:波形信号的位宽为10</td></tr><tr><td>1010:波形信号的位宽为11</td></tr><tr><td>≥1011:波形信号的位宽为12</td></tr><tr><td>23:22</td><td>DWM1[1:0]</td><td>DACx_OUT1 噪声波模式这些位指定了在 DACx_OUT1 外部触发使能(DTEN1=1)的情况下,DACx_OUT1 的噪声波模式的选择。00:波形生成禁能01:LFSR 噪声模式1x:三角噪声模式</td></tr><tr><td>21:19</td><td>DTSEL1[2:0]</td><td>DACx_OUT1 触发选择这些位与DTSEL1[3]位合并,在外部触发使能(DTEN1=1)时,选择触发DAC_OUT1的外部事件。0000:TIMER5 TRGO0001:TIMER2 TRGO(互联型);TIMER7 TRGO(其他类型);0010:TIMER6 TRGO0011:TIMER4 TRGO0100:TIMER1 TRGO0101:TIMER3 TRGO0110:外部中断线90111:软件触发1000:SHRTIMER_DACTRIG01001:SHRTIMER_DACTRIG11010:SHRTIMER_DACTRIG21011:TIMER14 TRGO1100~1111:保留</td></tr><tr><td>18</td><td>DTEN1</td><td>DACx_OUT1 触发使能0:DACx_OUT1 触发禁能1:DACx_OUT1触发使能</td></tr><tr><td>17</td><td>DBOFF1</td><td>DACx_OUT1输出缓冲区关闭0:DACx_OUT1输出缓冲区打开,以降低输出阻抗,提高驱动能力1:DACx_OUT1输出缓冲区关闭</td></tr><tr><td>16</td><td>DEN1</td><td>DACx_OUT1 使能0:DACx_OUT1 禁能1:DACx_OUT1使能</td></tr><tr><td>15</td><td>DDISC0</td><td>DACx_OUT0 连接 GPIO 选择0:DACx_OUT0 连接到外部管脚和片上外设(CMP)1:当输出缓冲区关闭时(DBOFF0=1)仅连接到片上外设(CMP),缓冲区打开时连接到外部管脚和片上外设(CMP)</td></tr><tr><td>14</td><td>DTSEL0[3]</td><td>DACx_OUT0 触发源选择的位[3],参考 DTSEL0[2:0]。</td></tr><tr><td>13</td><td>DDUDRIE0</td><td>DACx_OUT0 DMA 欠载中断使能0: DACx_OUT0 DMA 欠载中断禁能1: DACx_OUT0 DMA 欠载中断使能</td></tr><tr><td>12</td><td>DDMAEN0</td><td>DACx_OUT0 DMA 使能0: DACx_OUT0 DMA 模式禁能1: DACx_OUT0 DMA模式使能</td></tr><tr><td>11:8</td><td>DWBW0[3:0]</td><td>DACx_OUT0 噪声波位宽这些位指定了 DACx_OUT0 的噪声波信号的位宽。LFSR 噪声模式下,这些位表示不屏蔽 LFSR 的位[n-1,0];三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n为噪声波位宽。0000:波形信号的位宽为10001:波形信号的位宽为20010:波形信号的位宽为30011:波形信号的位宽为40100:波形信号的位宽为50101:波形信号的位宽为60110:波形信号的位宽为70111:波形信号的位宽为81000:波形信号的位宽为91001:波形信号的位宽为101010:波形信号的位宽为11≥1011:波形信号的位宽为12</td></tr><tr><td>7:6</td><td>DWM0[1:0]</td><td>DACx_OUT0 噪声波模式这些位指定了在 DACx_OUT0 外部触发使能(DTEN0=1)的情况下,DACx_OUT0 的噪声波模式的选择。00:波形生成禁能01:LFSR 噪声模式1x:三角噪声模式</td></tr><tr><td>5:3</td><td>DTSEL0[2:0]</td><td>DACx_OUT0 触发选择这些位与DTSEL0[3]位合并,在外部触发使能(DTEN0=1)时,选择触发DAC_OUT0的外部事件。0000:TIMER5 TRGO0001:TIMER2 TRGO(互联型);TIMER7 TRGO(其他类型);0010:TIMER6 TRGO0011:TIMER4 TRGO0100:TIMER1 TRGO0101:TIMER3 TRGO0110:外部中断线90111: 软件触发</td></tr><tr><td></td><td></td><td>1000: SHRTIMER_DACTRIG0</td></tr><tr><td></td><td></td><td>1001: SHRTIMER_DACTRIG1</td></tr><tr><td></td><td></td><td>1010: SHRTIMER_DACTRIG2</td></tr><tr><td></td><td></td><td>1011: TIMER14 TRGO</td></tr><tr><td></td><td></td><td>1100~1111: 保留</td></tr><tr><td>2</td><td>DTENO</td><td>DACx_OUT0 触发使能</td></tr><tr><td></td><td></td><td>0: DACx_OUT0 触发禁能</td></tr><tr><td></td><td></td><td>1: DACx_OUT0触发使能</td></tr><tr><td>1</td><td>DBOFF0</td><td>DACx_OUT0输出缓冲区关闭</td></tr><tr><td></td><td></td><td>0: DACx_OUT0输出缓冲区打开,以降低输出阻抗,提高驱动能力</td></tr><tr><td></td><td></td><td>1: DACx_OUT0输出缓冲区关闭</td></tr><tr><td>0</td><td>DEN0</td><td>DACx_OUT0 使能</td></tr><tr><td></td><td></td><td>0: DACx_OUT0 禁能</td></tr><tr><td></td><td></td><td>1: DACx_OUT0使能</td></tr></table>

## 14.4.2. DACx 软件触发寄存器（DAC_SWT）

地址偏移：0x04

复位值：0x0000 0000

该寄存器的[1]位仅可用于 DAC0，在 DAC1 中必须保持复位值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>SWTR1</td><td>SWTR0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>SWTR1</td><td>DACx_OUT1 软件触发,由硬件清除。0:软件触发禁能1:软件触发使能</td></tr><tr><td>0</td><td>SWTR0</td><td>DACx_OUT0 软件触发,由硬件清除。0:软件触发禁能1:软件触发使能</td></tr></table>

## 14.4.3. DACx_OUT0 12 位右对齐数据保持寄存器（DAC_OUT0_R12DH）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

## 14.4.4. DACx_OUT0 12 位左对齐数据保持寄存器（DAC_OUT0_L12DH）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 14.4.5. DACx_OUT0 8 位右对齐数据保持寄存器（DAC_OUT0_R8DH）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT0_DH[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的最高 8 位有效位。</td></tr></table>

## 14.4.6. DACx_OUT1 12 位右对齐数据保持寄存器（DAC_OUT1_R12DH）

地址偏移：0x14

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr></table>

## 14.4.7. DACx_OUT1 12 位左对齐数据保持寄存器（DAC_OUT1_L12DH）

地址偏移：0x18

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>OUT1_DH[11:0]</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 14.4.8. DACx_OUT1 8 位右对齐数据保持寄存器（DAC_OUT1_R8DH）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT1_DH[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr></table>

## 14.4.9. DACx 并发模式 12 位右对齐数据保持寄存器（DACC_R12DH）

地址偏移：0x20

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27:16</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

## 14.4.10. DACx 并发模式 12 位左对齐数据保持寄存器（DACC_L12DH）

地址偏移：0x24

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">OUT1_DH[11:0]</td><td colspan="4">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 14.4.11. DACx 并发模式 8 位右对齐数据保持寄存器（DACC_R8DH）

地址偏移：0x28

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">OUT1_DH [7:0]</td><td colspan="8">OUT0_DH [7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的 8 位最高有效位。</td></tr></table>

## 14.4.12. DACx_OUT0 数据输出寄存器（DAC_OUT0_DO）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DO [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DO [11:0]</td><td>DACx_OUT0 数据输出。</td></tr></table>

## 14.4.13. DACx_OUT1 数据输出寄存器（DAC_OUT1_DO）

地址偏移：0x30

复位值：0x0000 0000

该寄存器仅可用于 DAC0。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DO [11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DO [11:0]</td><td>DACx_OUT1 数据输出。这些位为只读类型,存储由 DACx_OUT1 转换的数据。</td></tr></table>

## 14.4.14. DACx 状态寄存器 0（DAC_STAT0）

地址偏移：0x34

复位值：0x0000 0000

该寄存器的[29]位域仅可用于 DAC0，在 DAC1 中必须保持复位值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>DDUDR1</td><td colspan="13">保留</td></tr><tr><td colspan="16">rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>DDUDR0</td><td colspan="13">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>DDUDR1</td><td>DACx_OUT1 DMA欠载标志位,硬件置位,软件写1清零。0:没有欠载发生1:发生欠载(DAC触发产生速度快于DMA传输速度)</td></tr><tr><td>28:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>DDUDR0</td><td>DACx_OUT0 DMA欠载标志位,硬件置位,软件写1清零。0:没有欠载发生1:发生欠载(DAC触发产生速度快于DMA传输速度)</td></tr><tr><td>12:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 14.4.15. DACx 控制寄存器 1（DAC_CTL1）

地址偏移：0x80

复位值：0x0000 0000

该寄存器的[18:16]位域仅可用于 DAC0，在 DAC1 中必须保持复位值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>FIFOUDRIE1</td><td>FIFOOVRIE1</td><td>FIFOEN1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>FIFOUDRIE0</td><td>FIFOOVRIE0</td><td>FIFOENO</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>18</td><td>FIFOUDRIE1</td><td>DACx_OUT1 FIFO欠载中断使能0: DACx_OUT1 FIFO欠载中断禁能1: DACx_OUT1 FIFO欠载中断使能</td></tr><tr><td>17</td><td>FIFOOVRIE1</td><td>DACx_OUT1 FIFO过载中断使能0: DACx_OUT1 FIFO过载中断禁能1: DACx_OUT1 FIFO过载中断使能</td></tr><tr><td>16</td><td>FIFOEN1</td><td>DACx_OUT1数据FIFO使能。当FIFOEN1位置1时,需要软件设置DDMAEN1=0和DTEN1=1。0: DACx_OUT1数据FIFO禁能1: DACx_OUT1数据FIFO使能</td></tr><tr><td>15:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>FIFOUDRIE0</td><td>DACx_OUT0 FIFO欠载中断使能0: DACx_OUT0 FIFO欠载中断禁能1: DACx_OUT0 FIFO欠载中断使能</td></tr><tr><td>1</td><td>FIFOOVRIE0</td><td>DACx_OUT0 FIFO过载中断使能0: DACx_OUT0 FIFO过载中断禁能1: DACx_OUT0 FIFO过载中断使能</td></tr><tr><td>0</td><td>FIFOEN0</td><td>DACx_OUT0数据FIFO使能。当FIFOEN0位置1时,需要软件设置DDMAEN0=0和DTEN0=1。0: DACx_OUT0数据FIFO禁能1: DACx_OUT0数据FIFO使能</td></tr></table>

## 14.4.16. DACx 状态寄存器 1（DAC_STAT1）

地址偏移：0x84

复位值：0x0002 0002

该寄存器的[22:16]位域仅可用于 DAC0，在 DAC1 中必须保持复位值。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="9">保留</td><td colspan="3">FIFONUM1</td><td>FIFOUDR1</td><td>FIFOOVR1</td><td>FIFOE1</td><td>FIFOF1</td></tr></table>

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>rc_w1</td><td>rc_w1</td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td></tr><tr><td colspan="9">保留</td><td colspan="2">FIFONUMO</td><td>FIFOUDR0</td><td>FIFOOVR0</td><td>FIFOE0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>rc_w1</td><td>rc_w1</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:20</td><td>FIFONUM1</td><td>DACx_OUT1 FIFO的数据个数000:数据个数为0001:数据个数为1010:数据个数为2011:数据个数为3100:数据个数为4101~111:保留</td></tr><tr><td>19</td><td>FIFOUDR1</td><td>DACx_OUT1 FIFO欠载标志位0: DACx_OUT1 FIFO没有欠载1: DACx_OUT1 FIFO欠载</td></tr><tr><td>18</td><td>FIFOOVR1</td><td>DACx_OUT1 FIFO过载标志位0: DACx_OUT1 FIFO没有过载1: DACx_OUT1 FIFO过载</td></tr><tr><td>17</td><td>FIFOE1</td><td>DACx_OUT1 FIFO空载0: DACx_OUT1 FIFO没有空载1: DACx_OUT1 FIFO空载</td></tr><tr><td>16</td><td>FIFOF1</td><td>DACx_OUT1 FIFO满载标志位0: DACx_OUT1 FIFO没有满载1: DACx_OUT1 FIFO满载</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>6:4</td><td>FIFONUM0</td><td>DACx_OUT0 FIFO的数据个数000:数据个数为0001:数据个数为1010:数据个数为2011:数据个数为3100:数据个数为4101~111:保留</td></tr><tr><td>3</td><td>FIFOUDR0</td><td>DACx_OUT0 FIFO欠载标志位0: DACx_OUT0 FIFO没有欠载1: DACx_OUT0 FIFO欠载</td></tr><tr><td>2</td><td>FIFOOVR0</td><td>DACx_OUT0 FIFO过载标志位0: DACx_OUT0 FIFO没有过载</td></tr></table>

<table><tr><td></td><td></td><td>1: DACx_OUT0 FIFO 过载</td></tr><tr><td>1</td><td>FIFOE0</td><td>DACx_OUT0 FIFO 空载标志位0: DACx_OUT0 FIFO 没有空载1: DACx_OUT0 FIFO 空载</td></tr><tr><td>0</td><td>FIFOF0</td><td>DACx_OUT0 FIFO 满载0: DACx_OUT0 FIFO 没有满载1: DACx_OUT0 FIFO 满载</td></tr></table>
