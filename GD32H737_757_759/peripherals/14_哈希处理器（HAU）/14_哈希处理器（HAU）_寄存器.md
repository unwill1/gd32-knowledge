# 14.7. HAU 寄存器

HAU基地址：0x4802 1400

# 14.7.1. 控制寄存器（HAU_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="13">保留</td><td>ALGM[1]</td><td>保留</td><td>KLM</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>MDS</td><td>DINE</td><td colspan="4">NWIF[3:0]</td><td>ALGM[0]</td><td>HMS</td><td colspan="2">DATAM[1:0]</td><td>DMAE</td><td>START</td><td colspan="2">保留</td></tr><tr><td></td><td></td><td>rw</td><td>r</td><td colspan="4">r</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>w</td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>ALGM[1]</td><td>算法选择位1</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>KLM</td><td>密钥长度模式0:密钥长度≤64字节1:密钥长度&gt;64字节注意:必须在非计算期间修改该位</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>MDS</td><td>多DMA选择如果哈希消息为大型文件需要多个DMA传输时,将此位置10:仅需要单次DMA传输,在DMA传输结束时硬件自动将CALEN位置11:需要多次DMA传输,在DMA传输结束时硬件不自动将CALEN位置1</td></tr><tr><td>12</td><td>DINE</td><td>DI寄存器非空0:DI寄存器空1:DI寄存器非空注意:当START位或CALEN位为1时此位会清零</td></tr><tr><td>11:8</td><td>NWIF[3:0]</td><td>输入FIFO中的字数注意:当START位置位时,或开始进行摘要计算时(CALEN位置位,或者DMA传输结束),该位域清零</td></tr><tr><td>7</td><td>ALGM[0]</td><td>算法选择位0该位和CTL寄存器的位18用于选择SHA-1,SHA-224,SHA256或MD5算法:00:选择SHA-1算法01:选择MD5算法</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td>10:选择SHA224算法</td></tr><tr><td>11:选择SHA256算法</td></tr><tr><td rowspan="3">6</td><td rowspan="3">HMS</td><td>HAU模式选择,必须在非计算期间修改该位</td></tr><tr><td>0:选择HASH模式</td></tr><tr><td>1:选择HMAC模式。如果密钥长度大于64字节,则还需配置KLM位。</td></tr><tr><td rowspan="6">5:4</td><td rowspan="6">DATAM[1:0]</td><td>数据交换类型</td></tr><tr><td>定义输入到HAU_DI寄存器中的数据格式</td></tr><tr><td>00:不交换,写入到HAU_DI寄存器的数据将直接送入FIFO,不进行交换</td></tr><tr><td>01:半字交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行半字交换</td></tr><tr><td>10:字节交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行字节交换</td></tr><tr><td>11:位交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行位交换</td></tr><tr><td rowspan="5">3</td><td rowspan="5">DMAE</td><td>DMA使能</td></tr><tr><td>0:禁止DMA传输</td></tr><tr><td>1:使能DMA传输</td></tr><tr><td>注意:1.当DMA传输消息的最后一个数据时,将由硬件清零该位。当START置位时,不会清零该位。</td></tr><tr><td>2.如果DMA正在传输数据,将该位写入0不会中止当前的传输,而直到当前传输结束或START位置为1之后,才会禁止传输。</td></tr><tr><td rowspan="4">2</td><td rowspan="4">START</td><td>开始摘要计算</td></tr><tr><td>0:没有影响</td></tr><tr><td>1:开始新消息的摘要计算</td></tr><tr><td>注意:读取该位将始终返回0</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 14.7.2. 数据输入寄存器（HAU_DI）

地址偏移：0x04

复位值：0x0000 0000

该数据输入寄存器用于将512位的数据块送入输入FIFO进行处理。当正在进行摘要计算时，所有对该寄存器的新的写访问将被延迟，直到计算完成。

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DI[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DI[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DI[31:0]</td><td>消息数据输入当数据写入这些寄存器时,寄存器中当前的内容被推入输入FIFO中同时更新为新的值。当读寄存器时,返回寄存器的当前内容。</td></tr></table>

# 14.7.3. 配置寄存器 (HAU_CFG)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CALEN</td><td colspan="3">保留</td><td colspan="5">VBL[4:0]</td></tr></table>

w 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CALEN</td><td>使能摘要计算0:不计算1:先使用VBL位域对数据进行数据填充,然后开始计算最终消息摘要注意:读该位将返回0</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>VBL[4:0]</td><td>消息的最后一个字中的有效位数0x00:对于写入HAU_DI寄存器的最后一个数据,所有32位(在数据交换后)均有效。0x01:对于写入HAU_DI寄存器的最后一个数据,仅位[31](在数据交换后)有效。0x02:对于写入HAU_DI寄存器的最后一个数据,仅位[31:30](在数据交换后)有效。0x03:对于写入HAU_DI寄存器的最后一个数据,仅位[31:29](在数据交换后)有效。...0x1F:对于写入HAU_DI寄存器的最后一个数据,仅位[31:1](在数据交换后)有效。注意:必须在置位CALEN位之前配置该位。</td></tr></table>

# 14.7.4. 数据输出寄存器 (HAU_DO0..7)

数据输出寄存器为只读寄存器，用于从输出FIFO中接收计算结果。置位START位将复位该寄存器。当正在进行摘要计算时，所有对该寄存器的新的读访问将被延迟，直到计算完成。

在SHA-1模式中，使用HAU_DO0…4

在MD5模式中，使用HAU_DO0…3

在SHA-224模式中，使用HAU_DO0…6

在SHA-256模式中，使用HAU_DO0…7

# HAU_DO0

地址偏移：0x0C和0x310

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO0[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO0[15:0]</td></tr></table>

r 

# HAU_DO1

地址偏移：0x10和0x314

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO1[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO1[15:0]</td></tr></table>

r 

# HAU_DO2

地址偏移：0x14和0x318

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO2[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO2[15:0]</td></tr></table>

r 

# HAU_DO3

地址偏移：0x18和0x31C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO3[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO3[15:0]</td></tr></table>

r 

# HAU_DO4

地址偏移：0x1C和0x320

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO4[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO4[15:0]</td></tr></table>

# HAU_DO5

地址偏移：0x324

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO5[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO5[15:0]</td></tr></table>

# HAU_DO6

地址偏移：0x328

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO6[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO6[15:0]</td></tr></table>

r 

# HAU_DO7

地址偏移：0x32C

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO7[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO7[15:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DO0..7[31:0]</td><td>消息摘要结果</td></tr></table>

# 14.7.5. 中断使能寄存器 (HAU_INTEN)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CCIE</td><td>DIIE</td></tr></table>

rw rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CCIE</td><td>计算完成中断使能0:禁止计算完成中断1:使能计算完成中断</td></tr><tr><td>0</td><td>DIIE</td><td>数据输入中断使能0:禁止数据输入中断1:使能数据输入中断</td></tr></table>

# 14.7.6. 状态与标志寄存器 (HAU_STAT)

地址偏移：0x24

复位值：0x0000 0001

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>BUSY</td><td>DMAS</td><td>CCF</td><td>DIF</td></tr><tr><td colspan="12"></td><td>r</td><td>r</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>BUSY</td><td>忙标志位0:未处理任何块1:正在处理某个数据块</td></tr><tr><td>2</td><td>DMAS</td><td>DMA状态标志0:DMA接口被禁用(DMAE=0)并且未在进行任何传输1:DMA接口被使能(DMAE=1)并且未在进行任何传输</td></tr><tr><td>1</td><td>CCF</td><td>计算完成状态标志0:计算未完成1:所有消息摘要计算完成</td></tr><tr><td>0</td><td>DIF</td><td>数据输入状态标志0:有一个字数据写入数据输入寄存器1:完成一个字数据的初步处理(只有在输入FIFO中的数据才会被处理)</td></tr></table>

# 14.7.7. 上下文交换寄存器 x (HAU_CTXSx) (x=0...53)

地址偏移：0xF8 + 0x04 × x, (x = 0...53)

复位值：0x0000 0002（当x=0），0x0000 0000（当x = 1…53）

该寄存器只能按字(32位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">CTXx[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CTXx[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>CTXx[31:0]</td><td>HAU处理器完整的内部状态信息。当有一个更高优先级的任务需要处理时,读取并保存这些寄存器的数据,恢复的时候将保存的数据写回到这些寄存器从而恢复前面被挂起的任务。</td></tr></table>
