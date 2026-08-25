## 20.6. HAU 寄存器

HAU 基地址：0x4002 3800

## 20.6.1. 控制寄存器（HAU_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>MDS</td><td>DINE</td><td colspan="4">NWIF[3:0]</td><td colspan="2">保留</td><td colspan="2">DATAM[1:0]</td><td>DMAE</td><td>START</td><td colspan="2">保留</td></tr><tr><td colspan="2"></td><td>rw</td><td>r</td><td colspan="4">r</td><td colspan="2"></td><td colspan="2">rw</td><td>rw</td><td>w</td><td colspan="2"></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>MDS</td><td>多DMA选择如果哈希消息为大型文件需要多个DMA传输时,将此位置10:仅需要单次DMA传输,在DMA传输结束时硬件自动将CALEN位置11:需要多次DMA传输,在DMA传输结束时硬件不自动将CALEN位置1</td></tr><tr><td>12</td><td>DINE</td><td>DI寄存器非空0:DI寄存器空1:DI寄存器非空注意:当START位或CALEN位为1时此位会清零</td></tr><tr><td>11:8</td><td>NWIF[3:0]</td><td>输入FIFO中的字数注意:当START位置位时,或开始进行摘要计算时(CALEN位置位,或者DMA传输结束),该位域清零</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>DATAM[1:0]</td><td>数据交换类型定义输入到HAU_DI寄存器中的数据格式00:不交换,写入到HAU_DI寄存器的数据将直接送入FIFO,不进行交换01:半字交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行半字交换10:字节交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行字节交换11:位交换。写入到HAU_DI寄存器的数据在送入FIFO前,需要进行位交换</td></tr><tr><td>3</td><td>DMAE</td><td>DMA使能</td></tr></table>

## 0：禁止DMA传输

1：使能DMA传输

注意：1.当DMA传输消息的最后一个数据时，将由硬件清零该位。当START置位时，不会清零该位。

2.如果DMA正在传输数据，将该位写入0不会中止当前的传输，而直到当前传输结束或START位置为1之后，才会禁止传输。

2 START 开始摘要计算

0：没有影响

1：开始新消息的摘要计算

注意：读取该位将始终返回0

1:0 保留 必须保持复位值。

## 20.6.2. 数据输入寄存器（HAU_DI）

地址偏移：0x04

复位值：0x0000 0000

该数据输入寄存器用于将 512 位的数据块送入输入 FIFO 进行处理。当正在进行摘要计算时，所有对该寄存器的新的写访问将被延迟，直到计算完成。

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DI[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DI[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DI[31:0]</td><td>消息数据输入当数据写入这些寄存器时,寄存器中当前的内容被推入输入FIFO中同时更新为新的值。当读寄存器时,返回寄存器的当前内容。</td></tr></table>

## 20.6.3. 配置寄存器 (HAU_CFG)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CALEN</td><td colspan="3">保留</td><td colspan="5">VBL[4:0]</td></tr><tr><td colspan="11">w</td><td colspan="5">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CALEN</td><td>使能摘要计算0:不计算1:先使用VBL位域对数据进行数据填充,然后开始计算最终消息摘要注意:读该位将返回0</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>VBL[4:0]</td><td>消息的最后一个字中的有效位数0x00:对于写入HAU_DI寄存器的最后一个数据,所有32位(在数据交换后)均有效。0x01:对于写入HAU_DI寄存器的最后一个数据,仅位[31](在数据交换后)有效。0x02:对于写入HAU_DI寄存器的最后一个数据,仅位[31:30](在数据交换后)有效。0x03:对于写入HAU_DI寄存器的最后一个数据,仅位[31:29](在数据交换后)有效。...0x1F:对于写入HAU_DI寄存器的最后一个数据,仅位[31:1](在数据交换后)有效。注意:必须在置位CALEN位之前配置该位。</td></tr></table>

## 20.6.4. 数据输出寄存器 (HAU_DO0..7)

数据输出寄存器为只读寄存器，用于从输出 FIFO 中接收计算结果。置位 START 位将复位该寄存器。当正在进行摘要计算时，所有对该寄存器的新的读访问将被延迟，直到计算完成。

HAU_DO0 

地址偏移：0x0C 和 0x310

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO0[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO0[15:0]</td></tr></table>

HAU_DO1 

地址偏移：0x10 和 0x314

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO1[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO1[15:0]</td></tr></table>

## HAU_DO2

地址偏移：0x14 和 0x318

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO2[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO2[15:0]</td></tr></table>

HAU_DO3 

地址偏移：0x18 和 0x31C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO3[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO3[15:0]</td></tr></table>

## HAU_DO4

地址偏移：0x1C 和 0x320

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO4[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO4[15:0]</td></tr></table>

## HAU_DO5

地址偏移：0x324

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO5[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO5[15:0]</td></tr></table>

HAU_DO6 

地址偏移：0x328

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO6[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO6[15:0]</td></tr></table>

## HAU_DO7

地址偏移：0x32C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO7[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO7[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DO0..7[31:0]</td><td>消息摘要结果</td></tr></table>

## 20.6.5. 中断使能寄存器 (HAU_INTEN)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CCIE</td><td>DIIE</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CCIE</td><td>计算完成中断使能0:禁止计算完成中断1:使能计算完成中断</td></tr><tr><td>0</td><td>DIIE</td><td>数据输入中断使能0:禁止数据输入中断1:使能数据输入中断</td></tr></table>

## 20.6.6. 状态与标志寄存器 (HAU_STAT)

地址偏移：0x24

复位值：0x0000 0001

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>BUSY</td><td>DMAS</td><td>CCF</td><td>DIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>BUSY</td><td>忙标志位0:未处理任何块1:正在处理某个数据块</td></tr><tr><td>2</td><td>DMAS</td><td>DMA状态标志0:DMA接口被禁用(DMAE=0)并且未在进行任何传输1:DMA接口被使能(DMAE=1)并且未在进行任何传输</td></tr><tr><td>1</td><td>CCF</td><td>计算完成状态标志0:计算未完成1:所有消息摘要计算完成</td></tr><tr><td>0</td><td>DIF</td><td>数据输入状态标志0:有一个字数据写入数据输入寄存器1:完成一个字数据的初步处理(只有在输入FIFO中的数据才会被处理)</td></tr></table>

