## 18.4. DAC 寄存器

DAC0 基地址：0x5000 1000

DAC1 基地址：0x5000 1400

DAC2 基地址：0x5000 1800

DAC3 基地址：0x5000 1C00

## 18.4.1. DACx 控制寄存器 (DAC_CTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DRST MD1</td><td>CALEN1</td><td>DDUDR IE1</td><td>DDMAEN1</td><td colspan="4">DWBW1[3:0]</td><td colspan="2">DWM1[1:0]</td><td colspan="2">保留</td><td colspan="2">DTSEL1[1:0]</td><td>DTEN1</td><td>DEN1</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>DRST MD0</td><td>CALEN0</td><td>DDUDR IE0</td><td>DDMAEN0</td><td colspan="4">DWBW0[3:0]</td><td colspan="2">DWM0[1:0]</td><td colspan="2">保留</td><td colspan="2">DTSEL0[1:0]</td><td>DTEN0</td><td>DEN0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DRSTMD1</td><td>DACx_OUT1 复位模式。该位只会被上电复位所复位。0:普通模式:所有的的复位信号都会复位 DACx_OUT1 相关的寄存器。1:复位保持模式:在除了上电复位之外的其他复位信号到来时,DACx_OUT1 的输出将会保持。</td></tr><tr><td>30</td><td>CLAEN1</td><td>DACx_OUT1校准使能0: DACx_OUT1 DMA校准模式禁能1: DACx_OUT1 DMA 校准模式使能只有 DEN1=0 时,才可对 CALEN1 写 1。</td></tr><tr><td>29</td><td>DDUDRIE1</td><td>DACx_OUT1 DMA欠载中断使能0: DACx_OUT1 DMA欠载中断禁能1: DACx_OUT1 DMA 欠载中断使能</td></tr><tr><td>28</td><td>DDMAEN1</td><td>DACx_OUT1 DMA 使能0: DACx_OUT1 DMA 模式禁能1: DACx_OUT1 DMA 模式使能</td></tr><tr><td>27:24</td><td>DWBW1[3:0]</td><td>DACx_OUT1 噪声波位宽这些位指定了 DACx_OUT1 的噪声波信号的位宽。LFSR 噪声模式下,这些位表示不屏蔽 LFSR 的位[n-1, 0];三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n 为噪声波位宽。0000: 波形信号的位宽为 10001: 波形信号的位宽为 20010: 波形信号的位宽为 30011: 波形信号的位宽为 40100: 波形信号的位宽为 50101: 波形信号的位宽为 60110: 波形信号的位宽为 70111: 波形信号的位宽为 81000: 波形信号的位宽为 91001: 波形信号的位宽为 101010: 波形信号的位宽为 11≥1011: 波形信号的位宽为 12</td></tr><tr><td>23:22</td><td>DWM1[1:0]</td><td>DACx_OUT1 噪声波模式这些位指定了在 DACx_OUT1 外部触发使能(DTEN1=1)的情况下,DACx_OUT1 的噪声波模式的选择。00: 波形生成禁能01: LFSR 噪声模式10: 三角波噪声模式11: 锯齿波噪声模式</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>DTSEL1[1:0]</td><td>DACx_OUT1 触发选择这些位仅在 DTEN=1 并选择用于触发 DAC 的外部事件时使用。00: 来自 TRIGSEL 的外部触发 DACx_OUT1_EXTRIG01: 软件触发其他值: 保留</td></tr><tr><td>17</td><td>DTEN1</td><td>DACx_OUT1 触发使能0: DACx_OUT1 触发禁能1: DACx_OUT1 触发使能</td></tr><tr><td>16</td><td>DEN1</td><td>DACx_OUT1 使能0: DACx_OUT1 禁能1: DACx_OUT1 使能</td></tr><tr><td>15</td><td>DRSTMD0</td><td>DACx_OUT0 复位模式。该位只会被上电复位所复位。0:普通模式:所有的的复位信号都会复位DACx_OUT0相关的寄存器。1:复位保持模式:在除了上电复位之外的其他复位信号到来时,DACx_OUT0的输出将会保持。</td></tr><tr><td>14</td><td>CLAEN0</td><td>DACx_OUT0校准使能0:DACx_OUT0 DMA校准模式禁能1:DACx_OUT0 DMA校准模式使能只有DEN0=0时,才可对CALENO写1。</td></tr><tr><td>13</td><td>DDUDRIE0</td><td>DACx_OUT0 DMA欠载中断使能0:DACx_OUT0 DMA欠载中断禁能1:DACx_OUT0 DMA欠载中断使能</td></tr><tr><td>12</td><td>DDMAEN0</td><td>DACx_OUT0 DMA使能0:DACx_OUT0 DMA模式禁能1:DACx_OUT0 DMA模式使能</td></tr><tr><td>11:8</td><td>DWBW0[3:0]</td><td>DACx_OUT0噪声波位宽这些位指定了DACx_OUT0的噪声波信号的位宽。LFSR噪声模式下,这些位表示不屏蔽LFSR的位[n-1,0];三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n为噪声波位宽。0000:波形信号的位宽为10001:波形信号的位宽为20010:波形信号的位宽为30011:波形信号的位宽为40100:波形信号的位宽为50101:波形信号的位宽为60110:波形信号的位宽为70111:波形信号的位宽为81000:波形信号的位宽为91001:波形信号的位宽为101010:波形信号的位宽为11≥1011:波形信号的位宽为12</td></tr><tr><td>7:6</td><td>DWM0[1:0]</td><td>DACx_OUT0噪声波模式这些位指定了在DACx_OUT0外部触发使能(DTEN0=1)的情况下,DACx_OUT0的噪声波模式的选择。00:波形生成禁能01:LFSR噪声模式10:三角波噪声模式11:锯齿波噪声模式</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:2</td><td>DTSEL0[1:0]</td><td>DACx_OUT0 触发选择这些位仅在 DTEN=1 并选择用于触发 DAC 的外部事件时使用。00: 来自 TRIGSEL 的外部触发 DACx_OUT0_EXTRIG01: 软件触发其他值: 保留</td></tr><tr><td>1</td><td>DTENO</td><td>DACx_OUT0 触发使能0: DACx_OUT0 触发禁能1: DACx_OUT0 触发使能</td></tr><tr><td>0</td><td>DEN0</td><td>DACx_OUT0 使能0: DACx_OUT0 禁能1: DACx_OUT0 使能</td></tr></table>

## 18.4.2. DACx 软件触发寄存器 (DAC_SWT)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td>SWSTTR1</td><td>SWSTTR0</td></tr><tr><td colspan="15">w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>SWTR1</td><td>SWTR0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17</td><td>SWSTTR1</td><td>DACx_OUT1 锯齿波计数器递增/递减软件触发.当DAC触发选择软件触发时,此位写1产生触发信号(锯齿波生成)。由硬件自动清零。0: 软件触发禁能1: 软件触发使能</td></tr><tr><td>16</td><td>SWSTTR0</td><td>DACx_OUT0 锯齿波计数器递增/递减软件触发.当DAC触发选择软件触发时,此位写1产生触发信号(锯齿波生成)。由硬件自动清零。0: 软件触发禁能</td></tr></table>

<table><tr><td></td><td></td><td>1: 软件触发使能</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>SWTR1</td><td>DACx_OUT1转换或者锯齿波复位软件触发,由硬件清除。0: 软件触发禁能1: 软件触发使能</td></tr><tr><td>0</td><td>SWTR0</td><td>DACx_OUT0转换或者锯齿波复位软件触发,由硬件清除。0: 软件触发禁能1: 软件触发使能</td></tr></table>

## 18.4.3. DACx_OUT0 12 位右对齐数据保持寄存器 (DAC_OUT0_R12DH)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

## 18.4.4. DACx_OUT0 12 位左对齐数据保持寄存器 (DAC_OUT0_L12DH)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 18.4.5. DACx_OUT0 8 位右对齐数据保持寄存器 (DAC_OUT0_R8DH)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT0_DH[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的最高 8 位有效位。</td></tr></table>

## 18.4.6. DACx_OUT1 12 位右对齐数据保持寄存器 (DAC_OUT1_R12DH)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr></table>

## 18.4.7. DACx_OUT1 12 位左对齐数据保持寄存器 (DAC_OUT1_L12DH)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT1_DH[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 18.4.8. DACx_OUT1 8 位右对齐数据保持寄存器 (DAC_OUT1_R8DH)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT1_DH[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr></table>

## 18.4.9. DACx 并发模式 12 位右对齐数据保持寄存器 (DACC_R12DH)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27:16</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

## 18.4.10. DACx 并发模式 12 位左对齐数据保持寄存器 (DACC_L12DH)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">OUT1_DH[11:0]</td><td colspan="4">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 18.4.11. DACx 并发模式 8 位右对齐数据保持寄存器 (DACC_R8DH)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">OUT1_DH[7:0]</td><td colspan="8">OUT0_DH[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的 8 位最高有效位。</td></tr></table>

## 18.4.12. DACx_OUT0 数据输出寄存器 (DAC_OUT0_DO)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DO[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DO[11:0]</td><td>DACx_OUT0 数据输出。</td></tr></table>


这些位为只读类型，存储由 DACx_OUT0 转换的数据。


## 18.4.13. DACx_OUT1 数据输出寄存器 (DAC_OUT1_DO)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DO[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DO[11:0]</td><td>DACx_OUT1 数据输出。这些位为只读类型,存储由 DACx_OUT1 转换的数据。</td></tr></table>

## 18.4.14. DACx 状态寄存器 0 (DAC_STAT0)

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BWT1</td><td>CALF1</td><td>DDUDR1</td><td colspan="13">保留</td></tr><tr><td>r</td><td>r</td><td>rc_w1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>BWT0</td><td>CALF0</td><td>DDUDR0</td><td>保留</td></tr><tr><td>r</td><td>r</td><td>rc_w1</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BWT1</td><td>DACx_OUT1 TSAMP1[9:0]写忙标志。当使能采样保持模式后,该位由系统设置,当TSAMP1[9:0]正在执行写操作时,该位置1:当完成写操作后,硬件清零。0:TSAMP1[9:0]没有进行写操作1:TSAMP1[9:0]正在进行行写操作</td></tr><tr><td>30</td><td>CALF1</td><td>DACx_OUT1校准偏移标志,该位由硬件置1和清零。0:校准值低于偏移校正值。1:校准值等于或大于偏移校正值</td></tr><tr><td>29</td><td>DDUDR1</td><td>DACx_OUT1 DMA欠载标志位,硬件置位,软件写1清零。0:没有欠载发生1:发生欠载(DAC触发产生速度快于DMA传输速度)</td></tr><tr><td>28:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>BWT0</td><td>DACx_OUT0 TSAMP0[9:0]写忙标志。当使能采样保持模式后,该位由系统设置,当TSAMP0[9:0]正在执行写操作时,该位置1:当完成写操作后,硬件清零。0:TSAMP0[9:0]没有进行写操作1:TSAMP0[9:0]正在进行行写操作</td></tr><tr><td>14</td><td>CALF0</td><td>DACx_OUT0校准偏移标志,该位由硬件置1和清零。0:校准值低于偏移校正值1:校准值等于或大于偏移校正值</td></tr><tr><td>13</td><td>DDUDR0</td><td>DACx_OUT0 DMA欠载标志位,硬件置位,软件写1清零。0:没有欠载发生1:发生欠载(DAC触发产生速度快于DMA传输速度)</td></tr><tr><td>12:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 18.4.15. DACx 校准寄存器 (DAC_CALR)

地址偏移：0x38

复位值：0x00XX 00XX

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">OTV1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">OTV0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>OTV1[4:0]</td><td>DACx_OUT1 偏移校准值。</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>OTV0[4:0]</td><td>DACx_OUT0 偏移校准值。</td></tr></table>

## 18.4.16. DACx 模式寄存器 (DAC_MDCR)

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td>DHFMT1</td><td colspan="6">保留</td><td colspan="3">MODE1[2:0]</td></tr><tr><td colspan="13">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>DHFMT0</td><td colspan="6">保留</td><td colspan="3">MODE0[2:0]</td></tr><tr><td colspan="13">rw</td><td colspan="3">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25</td><td>DHFMT1</td><td>DACx_OUT1 写入数据保持寄存器数据格式0:写入的数据以无符号格式处理1:写入的数据以有符号(二进制补码)格式处理</td></tr><tr><td>24:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>MODE1[2:0]</td><td>DACx_OUT1 模式当 DAC_CTL0 寄存器中 DEN1=0 和 CALEN1=0 时才可对这些位进行写操作。当 DAC_CTL0 寄存器中 DEN1=1 或 CALEN1=1,写操作无效。-普通模式下 DACx_OUT1000:DACx_OUT1 连接到外部引脚,缓冲区启用。001: DACx_OUT1 连接到外部引脚和片上外设,缓冲区启用。010:DACx_OUT1 连接到外部引脚,缓冲区禁用。011: DACx_OUT1 连接到片上外设,缓冲区禁用。-采样保持模式下 DACx_OUT1100:DACx_OUT1 连接到外部引脚,缓冲区启用。101: DACx_OUT1 连接到外部引脚和片上外设,缓冲区启用。110: DACx_OUT1 连接到外部引脚和片上外设,缓冲区禁用。111: DACx_OUT1 连接到片上外设,缓冲区禁用。注意:对于无输出缓冲的 DACx(x=2,3),只有 MODE1[2]位是可用的,用于选择正常模式或者采样保持模式。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>DHFMT0</td><td>DACx_OUT0 写入数据保持寄存器数据格式0:写入的数据以无符号格式处理1:写入的数据以有符号(二进制补码)格式处理</td></tr><tr><td>8:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>MODE0[2:0]</td><td>DACx_OUT0 模式当 DAC_CTL0 寄存器中 DEN0=0 和 CALEN0=0 可进行写操作。当 DAC_CTL0 寄存器中 DEN0=1 或 CALEN0=1,写操作被忽略)。-普通模式下 DAxC_OUT0000:DACx_OUT0 连接到外部引脚,缓冲区启用。001: DACx_OUT0 连接到外部引脚和片上外设,缓冲区启用。010: DACx_OUT0 连接到外部引脚,缓冲区禁用。011: DACx_OUT0 连接到片上外设,缓冲区禁用。-采样保持模式下 DACx_OUT0100:DACx_OUT0 连接到外部引脚,缓冲区启用。101: DACx_OUT0 连接到外部引脚和片上外设,缓冲区启用。110: DACx_OUT0 连接到外部引脚和片上外设,缓冲区禁用。111: DACx_OUT0 连接到片上外设,缓冲区禁用。注意:对于无输出缓冲的 DACx(x=2,3),只有 MODE0[2]位是可用的,用于选择正常模式或者采样保持模式。</td></tr></table>

## 18.4.17. DACx 采样保持模式采样时间寄存器 0 (DAC_SKSTR0)

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TSAMP0[9:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TSAMP0[9:0]</td><td>DACx_OUT0 采样时间。</td></tr></table>

## 18.4.18. DACx 采样保持模式采样时间寄存器 1 (DAC_SKSTR1)

地址偏移：0x44

复位值：0x0000 0000


该寄存器只能按字(32 位)访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TSAMP1[9:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TSAMP1[9:0]</td><td>DACx_OUT1 采样时间。</td></tr></table>

## 18.4.19. DACx 采样保持模式保持时间寄存器 (DAC_SKKTR)

地址偏移：0x48

复位值：0x0000 0000


该寄存器只能按字(32 位)访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">TKEEP1[9:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TKEEP0[9:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:16</td><td>TKEEP1[9:0]</td><td>DACx_OUT1 保持时间(仅在采样保持模式有效)。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TKEEP0[9:0]</td><td>DACx_OUT0 保持时间(仅在采样保持模式有效)。</td></tr></table>

## 18.4.20. DACx 采样保持模式刷新时间寄存器 (DAC_SKRTR)

地址偏移：0x4C

复位值：0x0001 0001

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">TREF1[7:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">TREF0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>TREF1[7:0]</td><td>DACx_OUT1刷新时间(仅在采样保持模式有效)。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>TREF0[7:0]</td><td>DACx_OUT0刷新时间(仅在采样保持模式有效)。</td></tr></table>

## 18.4.21. DACx_OUT0 锯齿波寄存器(DAC_OUT0_SAW)

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SAWSTEP0[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>SAWDIR0</td><td colspan="12">SAWINIT0[11:0]</td></tr><tr><td colspan="3">位/位域</td><td>名称</td><td colspan="12">描述</td></tr><tr><td colspan="3">31:16</td><td>SAWSTEP0[15:0]</td><td colspan="12">DACx_OUT0锯齿波步长值。</td></tr><tr><td colspan="3">15:13</td><td>保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td colspan="3">12</td><td>SAWDIR0</td><td colspan="12">DACx_OUT0锯齿波步进方向。软件写此位选择锯齿波步进方向。0:向下递减1:向上递增</td></tr><tr><td colspan="3">11:0</td><td>SAWINIT0[11:0]</td><td colspan="12">DACx_OUT0锯齿波初始值。</td></tr></table>

## 18.4.22. DACx_OUT1 锯齿波寄存器(DAC_OUT1_SAW)

地址偏移：0x5C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SAWSTEP1[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td>SAWDIR1</td><td colspan="12">SAWINIT1[11:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>SAWSTEP1[15:0]</td><td>DACx_OUT1锯齿波步长值。</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>SAWDIR1</td><td>DACx_OUT1锯齿波步进方向。软件写此位选择锯齿波步进方向。0:向下递减1:向上递增</td></tr><tr><td>11:0</td><td>SAWINIT1[11:0]</td><td>DACx_OUT1锯齿波初始值</td></tr></table>

## 18.4.23. DACx 锯齿波模式寄存器 (DAC_SAWMDR)

地址偏移：0x60

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>


GD32G553 用户手册


<table><tr><td colspan="6">保留</td><td colspan="2">SAWSTEPTSEL1[1:0]</td><td colspan="6">保留</td><td colspan="2">SAWRSTTSEL1[1:0]</td></tr><tr><td colspan="14">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">SAWSTEPTSEL0[1:0]</td><td colspan="6">保留</td><td colspan="2">SAWRSTTSEL0[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:24</td><td>STEPTSEL1[1:0]</td><td>DACx_OUT1 锯齿波递增/递减触发选择。00: 来自 TRIGSEL 的外部触发 DACx_OUT1_ST_EXTRIG01: 软件触发其他值: 保留</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17:16</td><td>RSTTSEL1[1:0]</td><td>DACx_OUT1 锯齿波复位触发选择。00: 来自 TRIGSEL 的外部触发 DACx_OUT1_EXTRIG01: 软件触发其他值: 保留</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>STEPTSEL0[1:0]</td><td>DACx_OUT0 锯齿波递增/递减触发选择。00: 来自 TRIGSEL 的外部触发 DACx_OUT0_ST_EXTRIG01: 软件触发其他值: 保留</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1:0</td><td>RSTTSEL0[1:0]</td><td>DACx_OUT0 锯齿波复位触发选择。00: 来自 TRIGSEL 的外部触发 DACx_OUT0_EXTRIG01: 软件触发其他值: 保留</td></tr></table>
