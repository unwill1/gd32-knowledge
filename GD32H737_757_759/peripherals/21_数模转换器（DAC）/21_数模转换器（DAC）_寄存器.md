# 21.4. DAC 寄存器

DAC0 基地址：0x4000 7400

# 21.4.1. DACx 控制寄存器 (DAC_CTL0)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>CALEN1</td><td>DDUDRIE1</td><td>DDMAEN1</td><td colspan="4">DWBW1[3:0]</td><td colspan="2">DWM1[1:0]</td><td colspan="2">保留</td><td colspan="2">DTSEL1[1:0]</td><td>DTEN1</td><td>DEN1</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td>CALEN0</td><td>DDUDRIE0</td><td>DDMAENO</td><td colspan="4">DWBW0[3:0]</td><td colspan="2">DWM0[1:0]</td><td colspan="2">保留</td><td colspan="2">DTSEL0[1:0]</td><td>DTEN0</td><td>DEN0</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>CLAEN1</td><td>DACx_OUT1校准使能0: DACx_OUT1 DMA校准模式禁能1: DACx_OUT1 DMA 校准模式使能只有 DEN1=0 时,才可对 CALEN1 写 1。</td></tr><tr><td>29</td><td>DDUDRIE1</td><td>DACx_OUT1 DMA欠载中断使能0: DACx_OUT1 DMA欠载中断禁能1: DACx_OUT1 DMA 欠载中断使能</td></tr><tr><td>28</td><td>DDMAEN1</td><td>DACx_OUT1 DMA 使能0: DACx_OUT1 DMA 模式禁能1: DACx_OUT1 DMA 模式使能</td></tr><tr><td>27:24</td><td>DWBW1[3:0]</td><td>DACx_OUT1 噪声波位宽这些位指定了 DACx_OUT1 的噪声波信号的位宽。LFSR 噪声模式下,这些位表示不屏蔽 LFSR 的位[n-1, 0];三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n 为噪声波位宽。0000: 波形信号的位宽为 10001: 波形信号的位宽为 20010: 波形信号的位宽为 30011: 波形信号的位宽为 40100: 波形信号的位宽为 50101: 波形信号的位宽为 60110: 波形信号的位宽为 70111: 波形信号的位宽为 81000:波形信号的位宽为9</td></tr><tr><td rowspan="3"></td><td rowspan="3"></td><td>1001:波形信号的位宽为10</td></tr><tr><td>1010:波形信号的位宽为11</td></tr><tr><td>≥1011:波形信号的位宽为12</td></tr><tr><td>23:22</td><td>DWM1[1:0]</td><td>DACx_OUT1 噪声波模式这些位指定了在 DACx_OUT1 外部触发使能(DTEN1=1)的情况下,DACx_OUT1 的噪声波模式的选择。00:波形生成禁能01:LFSR 噪声模式1x:三角噪声模式</td></tr><tr><td>21:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19:18</td><td>DTSEL1[1:0]</td><td>DACx_OUT1 触发选择这些位仅在 DTEN=1 并选择用于触发 DAC 的外部事件时使用。00:EXTRIG(外部触发来自 TRIGSEL)01:软件触发其他值:保留</td></tr><tr><td>17</td><td>DTEN1</td><td>DACx_OUT1 触发使能0:DACx_OUT1 触发禁能1:DACx_OUT1 触发使能</td></tr><tr><td>16</td><td>DEN1</td><td>DACx_OUT1 使能0:DACx_OUT1 禁能1:DACx_OUT1 使能</td></tr><tr><td>15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14</td><td>CLAEN0</td><td>DACx_OUT0 校准使能0:DACx_OUT0 DMA校准模式禁能1:DACx_OUT0 DMA 校准模式使能只有 DEN0=0 时,才可对 CALEN0 写 1。</td></tr><tr><td>13</td><td>DDUDRIE0</td><td>DACx_OUT0 DMA欠载中断使能0:DACx_OUT0 DMA欠载中断禁能1:DACx_OUT0 DMA 欠载中断使能</td></tr><tr><td>12</td><td>DDMAEN0</td><td>DACx_OUT0 DMA 使能0:DACx_OUT0 DMA 模式禁能1:DACx_OUT0 DMA 模式使能</td></tr><tr><td>11:8</td><td>DWBW0[3:0]</td><td>DACx_OUT0 噪声波位宽这些位指定了 DACx_OUT0 的噪声波信号的位宽。LFSR 噪声模式下,这些位表示不屏蔽 LFSR 的位[n-1,0];三角噪声模式下,这些位表示三角波幅值为(2&lt;&lt;(n-1))-1。其中,n 为噪声波位宽。0000:波形信号的位宽为 10001:波形信号的位宽为 20010:波形信号的位宽为3</td></tr><tr><td></td><td></td><td>0011:波形信号的位宽为4</td></tr><tr><td></td><td></td><td>0100:波形信号的位宽为5</td></tr><tr><td></td><td></td><td>0101:波形信号的位宽为6</td></tr><tr><td></td><td></td><td>0110:波形信号的位宽为7</td></tr><tr><td></td><td></td><td>0111:波形信号的位宽为8</td></tr><tr><td></td><td></td><td>1000:波形信号的位宽为9</td></tr><tr><td></td><td></td><td>1001:波形信号的位宽为10</td></tr><tr><td></td><td></td><td>1010:波形信号的位宽为11</td></tr><tr><td></td><td></td><td>≥1011:波形信号的位宽为12</td></tr><tr><td>7:6</td><td>DWM0[1:0]</td><td>DACx_OUT0 噪声波模式这些位指定了在 DACx_OUT0 外部触发使能(DTEN0=1)的情况下,DACx_OUT0 的噪声波模式的选择。00:波形生成禁能01:LFSR 噪声模式1x:三角噪声模式</td></tr><tr><td>5:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:2</td><td>DTSEL0[1:0]</td><td>DACx_OUT0 触发选择这些位仅在 DTEN=1 并选择用于触发 DAC 的外部事件时使用。00:EXTRIG(外部触发来自 TRIGSEL)01:软件触发其他值:保留</td></tr><tr><td>1</td><td>DTENO</td><td>DACx_OUT0 触发使能0:DACx_OUT0 触发禁能1:DACx_OUT0 触发使能</td></tr><tr><td>0</td><td>DEN0</td><td>DACx_OUT0 使能0:DACx_OUT0 禁能1:DACx_OUT0 使能</td></tr></table>

# 21.4.2. DACx 软件触发寄存器 (DAC_SWT)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>SWTR1</td><td>SWTR0</td></tr></table>

w w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>SWTR1</td><td>DACx_OUT1 软件触发,由硬件清除。0:软件触发禁能1:软件触发使能</td></tr><tr><td>0</td><td>SWTR0</td><td>DACx_OUT0 软件触发,由硬件清除。0:软件触发禁能1:软件触发使能</td></tr></table>

# 21.4.3. DAC_OUT0 12 位右对齐数据保持寄存器 (DAC_OUT0_R12DH)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

# 21.4.4. DAC_OUT0 12 位左对齐数据保持寄存器 (DAC_OUT0_L12DH)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

# 21.4.5. DAC_OUT0 8 位右对齐数据保持寄存器 (DAC_OUT0_R8DH)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT0_DH[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的最高 8位有效位。</td></tr></table>

# 21.4.6. DAC_OUT1 12 位右对齐数据保持寄存器 (DAC_OUT1_R12DH)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr></table>

# 21.4.7. DAC_OUT1 12 位左对齐数据保持寄存器 (DAC_OUT1_L12DH)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT1_DH[11:0]</td><td colspan="4">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

# 21.4.8. DAC_OUT1 8 位右对齐数据保持寄存器 (DAC_OUT1_R8DH)

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">OUT1_DH[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr></table>

# 21.4.9. DAC 并发模式 12 位右对齐数据保持寄存器 (DACC_R12DH)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DH[11:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DH[11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>27:16</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>15:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr></table>

# 21.4.10. DAC 并发模式 12 位左对齐数据保持寄存器 (DACC_L12DH)

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="12">OUT1_DH[11:0]</td><td colspan="4">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">OUT0_DH[11:0]</td><td colspan="4">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:20</td><td>OUT1_DH[11:0]</td><td>DACx_OUT1 12 位左对齐数据这些位指定了将由 DACx_OUT1 转换的数据。</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:4</td><td>OUT0_DH[11:0]</td><td>DACx_OUT0 12 位左对齐数据这些位指定了将由 DACx_OUT0 转换的数据。</td></tr><tr><td>3:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

# 21.4.11. DAC 并发模式 8 位右对齐数据保持寄存器 (DACC_R8DH)

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">OUT1_DH [7:0]</td><td colspan="8">OUT0_DH [7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>OUT1_DH[7:0]</td><td>DACx_OUT1 8位右对齐数据这些位指定了将由 DACx_OUT1 转换的数据的 8 位最高有效位。</td></tr><tr><td>7:0</td><td>OUT0_DH[7:0]</td><td>DACx_OUT0 8位右对齐数据这些位指定了将由 DACx_OUT0 转换的数据的 8 位最高有效位。</td></tr></table>

# 21.4.12. DAC_OUT0 数据输出寄存器 (DAC_OUT0_DO)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT0_DO [11:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT0_DO [11:0]</td><td>DACx_OUT0 数据输出。这些位为只读类型,存储由 DACx_OUT0 转换的数据。</td></tr></table>

# 21.4.13. DAC_OUT1 数据输出寄存器 (DAC_OUT1_DO)

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">OUT1_DO [11:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>11:0</td><td>OUT1_DO [11:0]</td><td>DACx_OUT1 数据输出。这些位为只读类型,存储由 DACx_OUT1 转换的数据。</td></tr></table>

# 21.4.14. DAC 状态寄存器 0 (DAC_STAT0)

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>BWT1</td><td>CALF1</td><td>DDUDR1</td><td colspan="13">保留</td></tr><tr><td>r</td><td>r</td><td>rc_w1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BWT0</td><td>CALF0</td><td>DDUDR0</td><td colspan="13">保留</td></tr></table>

rc_w1 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>BWT1</td><td>DACx_OUT1当使能采样保持模式后,该位由系统设置,当 DACx_SKSTR1 正在执行写操作时,该位置 1;当完成写操作后,硬件清零。0: DAC_SKSTR1 没有进行写操作1: DAC_SKSTR1 正在进行行写操作</td></tr><tr><td>30</td><td>CALF1</td><td>DACx_OUT1 校准偏移标志,该位由硬件置 1 和清零。0: 校准值低于偏移校正值。1: 校准值等于或大于偏移校正值</td></tr><tr><td>29</td><td>DDUDR1</td><td>DACx_OUT1 DMA 欠载标志位,硬件置位,软件写 1 清零。0: 没有欠载发生1: 发生欠载(DAC 触发产生速度快于 DMA 传输速度)</td></tr><tr><td>28:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>BWT0</td><td>DACx_OUT0当使能采样保持模式后,该位由系统设置,当 DAC_SKSTR0 正在执行写操作时,该位置 1;当完成写操作后,硬件清零。0: DAC_SKSTR0 没有进行写操作1: DAC_SKSTR0 正在进行行写操作</td></tr></table>

14 CALF0 DACx_OUT0 校准偏移标志，该位由硬件置 1 和清零。

0：校准值低于偏移校正值

1：校准值等于或大于偏移校正值

13 DDUDR0 DACx_OUT0 DMA 欠载标志位，硬件置位，软件写 1 清零。

0：没有欠载发生

1：发生欠载（DAC触发产生速度快于 DMA 传输速度）

12:0 保留 必须保持复位值。

# 21.4.15. DAC 校准寄存器 (DAC_CALR)

地址偏移：0x38

复位值：0x00XX 00XX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="5">OTV1</td></tr><tr><td colspan="11">rw</td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td colspan="5">OTV0</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:16</td><td>OTV1[4:0]</td><td>DACx_OUT1 偏移校准值。</td></tr><tr><td>15:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>OTV0[4:0]</td><td>DACx_OUT0 偏移校准值。</td></tr></table>

# 21.4.16. DAC 模式寄存器 (DAC_MDCR)

地址偏移：0x3C

复位值：0x00XX 00XX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td colspan="3">MODE1[2:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">MODE0[2:0]</td></tr></table>

rw 

位/位域 名称 描述

<table><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18:16</td><td>MODE1[2:0]</td><td>DACx_OUT1模式当 DAC_CTL0 寄存器中 DEN1=0 和 CALEN1=0 时才可对这些位进行写操作。当 DAC_CTL0 寄存器中 DEN1=1 或 CALEN1=1,写操作被忽略。-普通模式下 DACx_OUT1000:DACx_OUT1 连接到外部引脚,缓冲区启用。001: DACx_OUT1 连接到外部引脚和片上外设,缓冲区启用。010: DACx_OUT1 连接到外部引脚,缓冲区禁用。011: DACx_OUT1 连接到片上外设,缓冲区禁用。-采样保持模式下 DACx_OUT1100: DACx_OUT1 连接到外部引脚,缓冲区启用。101: DACx_OUT1 连接到外部引脚和片上外设,缓冲区启用。110: DACx_OUT1 连接到外部引脚和片上外设,缓冲区禁用。111: DACx_OUT1 连接到片上外设,缓冲区禁用。</td></tr><tr><td>15:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>MODE0[2:0]</td><td>DACx_OUT0模式当 DAC_CTL0 寄存器中 DEN0=0 和 CALEN0=0 可进行写操作。当 DAC_CTL0 寄存器中 DEN0=1 或 CALEN0=1,写操作被忽略)。-普通模式下 DAxC_OUT0000: DACx_OUT0 连接到外部引脚,缓冲区启用。001: DACx_OUT0 连接到外部引脚和片上外设,缓冲区启用。010: DACx_OUT0 连接到外部引脚,缓冲区禁用。011: DACx_OUT0 连接到片上外设,缓冲区禁用。-采样保持模式下 DACx_OUT0100: DACx_OUT0 连接到外部引脚,缓冲区启用。101: DACx_OUT0 连接到外部引脚和片上外设,缓冲区启用。110: DACx_OUT0 连接到外部引脚和片上外设,缓冲区禁用。111: DACx_OUT0 连接到片上外设,缓冲区禁用。</td></tr></table>

# 21.4.17. DAC 采样保持模式采样时间寄存器 0 (DAC_SKSTR0)

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TSAMP0[9:0]</td></tr></table>

rw 

位/位域 名称 描述

<table><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TSAMP0[9:0]</td><td>DACx_OUT0 采样时间。</td></tr></table>

# 21.4.18. DAC 采样保持模式采样时间寄存器 1 (DAC_SKSTR1)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TSAMP1[9:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TSAMP1[9:0]</td><td>DACx_OUT1 采样时间。</td></tr></table>

# 21.4.19. DAC 采样保持模式保持时间寄存器 (DAC_SKKTR)

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="6">保留</td><td colspan="10">TKEEP1[9:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">TKEEP0[9:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:26</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>25:16</td><td>TKEEP1[9:0]</td><td>DACx_OUT1 保持时间(仅在采样保持模式有效)。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>TKEEP0[9:0]</td><td>DACx_OUT0 保持时间(仅在采样保持模式有效)。</td></tr></table>

# 21.4.20. DAC 采样保持模式刷新时间寄存器 (DAC_SKRTR)

地址偏移：0x4C

复位值：0x0001 0001

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">TREF1[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">TREF0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>TREF1[7:0]</td><td>DACx_OUT1刷新时间(仅在采样保持模式有效)。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>TREF0[7:0]</td><td>DACx_OUT0刷新时间(仅在采样保持模式有效)。</td></tr></table>
