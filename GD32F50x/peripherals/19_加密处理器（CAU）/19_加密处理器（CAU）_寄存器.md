## 19.8. CAU 寄存器

CAU 基地址：0x4002 3400

## 19.8.1. 控制寄存器（CAU_CTL）

偏移地址：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CAUEN</td><td colspan="2">FFLUSH</td><td colspan="3">保留</td><td colspan="2">KEYM[1:0]</td><td colspan="2">DATAM[1:0]</td><td colspan="3">ALGM[2:0]</td><td colspan="2">CAUDIR</td><td>保留</td></tr><tr><td>rw</td><td colspan="2">w</td><td colspan="3"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CAUEN</td><td>加密处理器使能0:加密处理器禁用1:加密处理器使能注意:当准备密钥(ALGM=111b)完成后,CAUEN位将硬件自动清零。</td></tr><tr><td>14</td><td>FFLUSH</td><td>FIFO刷新0:不产生影响1:当CAUEN=1时,刷新输入和输出FIFO读取该位时,始终返回0</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>KEYM[1:0]</td><td>AES密钥长度配置,必须在BUSY=0时才可配置00:128位密钥长度01:192位密钥长度10:256位密钥长度11:保留</td></tr><tr><td>7:6</td><td>DATAM[1:0]</td><td>数据交换模式配置,必须在BUSY=0时才可配置00:不交换01:半字交换10:字节交换11:位交换</td></tr><tr><td>5:3</td><td>ALGM[2:0]</td><td>加密/解密算法模式位0到位2000:所有模式关闭。100:AES-ECB(AES电子密码本),使用CAU_KEY0,1,2,3.111:AES解密密钥准备模式。输入密钥必须与加密处理中用的密钥相同。BUSY位将保持置位直到完成密钥的准备,随后CAUEN位会清零。</td></tr><tr><td>2</td><td>CAUDIR</td><td>CAU算法方向,必须在BUSY=0时才可配置0:加密1:解密</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 19.8.2. 状态寄存器 0 (CAU_STAT0)

偏移地址：0x04

复位值：0x0000 0003

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>BUSY</td><td>OFU</td><td>ONE</td><td>INF</td><td>IEM</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>BUSY</td><td>忙碌标志位0:CAU内核空闲,这是由于-CAUEN=0从而CAU内核被禁用,或这处理已完成-正在等待输入数据或输出FIFO有足够的自由空间来处理数据块1:CAU内核忙碌,正在处理数据块或准备密钥</td></tr><tr><td>3</td><td>OFU</td><td>输出FIFO满0:输出FIFO未满1: 输出FIFO满</td></tr><tr><td rowspan="3">2</td><td rowspan="3">ONE</td><td>输出FIFO非空</td></tr><tr><td>0: 输出FIFO为空</td></tr><tr><td>1: 输出FIFO非空</td></tr><tr><td rowspan="3">1</td><td rowspan="3">INF</td><td>输入FIFO未满</td></tr><tr><td>0: 输入FIFO满</td></tr><tr><td>1: 输入FIFO未满</td></tr><tr><td rowspan="3">0</td><td rowspan="3">IEM</td><td>输入FIFO空</td></tr><tr><td>0: 输入FIFO非空</td></tr><tr><td>1: 输入FIFO空</td></tr></table>

## 19.8.3. 数据输入寄存器 (CAU_DI)

偏移地址：0x08

复位值：0x0000 0000

数据输入寄存器用于传输明文或密文数据块到输入 FIFO 中进行处理。首先写入 FIFO 的是数据块的 MSB，最后才是 LSB。当 CAUEN 位为 0，并且输入 FIFO 非空时，读取该寄存器时返回 FIFO中的首个字。当 CAUEN 位为 1 时，读取该寄存器返回一个不确定的值。一旦执行了读操作，则必须要刷新 FIFO 以处理新数据块。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DI[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DI[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DI[31:0]</td><td>数据输入写这些位,数据会写入输入FIFO。当CAUEN位为0时,读这些位将返回输入FIFO中的值,否则将返回不确定的值。</td></tr></table>

## 19.8.4. 数据输出寄存器 (CAU_DO)

偏移地址：0x0C

复位值：0x0000 0000

数据输出寄存器是只读寄存器，用于接收来自输出 FIFO 的明文或密文处理结果。与 CAU_DI 类

似，读取时首先读取的是数据块的 MSB，最后才是 LSB。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DO[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DO[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DO[31:0]</td><td>数据输出这些位为只读,读这些位将返回输出FIFO中的值</td></tr></table>

## 19.8.5. DMA 使能寄存器 (CAU_DMAEN)

偏移地址：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>DMAOEN</td><td>DMAIEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>DMAOEN</td><td>DMA 输出使能0:禁用用于输出 FIFO 数据传输的 DMA1:使能用于输出 FIFO 数据传输的 DMA</td></tr><tr><td>0</td><td>DMAIEN</td><td>DMA 输入使能0:禁用用于输入 FIFO 数据传输的 DMA1:使能用于输入 FIFO 数据传输的 DMA</td></tr></table>

## 19.8.6. 中断使能寄存器 (CAU_INTEN)

偏移地址：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>OINTEN</td><td>IINTEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OINTEN</td><td>输出FIFO中断使能0:禁用输出FIFO中断1:使能输出FIFO中断</td></tr><tr><td>0</td><td>IINTEN</td><td>输入FIFO中断使能0:禁用输入FIFO中断1:使能输入FIFO中断</td></tr></table>

## 19.8.7. 状态寄存器 1 (CAU_STAT1)

偏移地址：0x18

复位值：0x0000 0001


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>OSTA</td><td>ISTA</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OSTA</td><td>输出FIFO状态0:输出FIFO状态未挂起1:输出FIFO状态挂起</td></tr><tr><td>0</td><td>ISTA</td><td>输入FIFO状态0:输入FIFO状态未挂起1:输入FIFO状态挂起</td></tr></table>

## 19.8.8. 中断标志寄存器 (CAU_INTF)

偏移地址：0x1C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>OINTF</td><td>IINTF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OINTF</td><td>输出 FIFO 中断标志0: 输出 FIFO 中断状态未挂起1: 输出 FIFO 中断状态挂起</td></tr><tr><td>0</td><td>IINTF</td><td>输入 FIFO 中断标志0: 输入 FIFO 中断状态未挂起1: 当 CAUEN 位为 1 时输入 FIFO 中断状态挂起</td></tr></table>

## 19.8.9. 密钥寄存器 (CAU_KEY0..3(H/L))

偏移地址：0x20~0x3C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问，必须在 BUSY位为 0 时写这些寄存器。

在 AES-128 模式下，KEY2H[31:0]和 KEY2L[31:0]分别对应于 AES_KEY[0:63]的高 32 位与低 32位，而 KEY3H[31:0]和 KEY3L[31:0]分别对应于 AES_KEY[64:127]的高 32 位与低 32 位。

在 AES-192 模式下，KEY1H[31:0]和 KEY1L[31:0]分别对应于 AES_KEY[0:63]的高 32 位与低 32位，KEY2H[31:0]和 KEY2L[31:0]分别对应于 AES_KEY[64:127]的高 32 位与低 32 位，KEY3H[31:0]和 KEY3L[31:0]分别对应于 AES_KEY[128:191]的高 32 位与低 32 位。

在 AES-256 模式下，KEY0H[31:0]和 KEY0L[31:0]分别对应于 AES_KEY[0:63]的高 32 位与低 32位，KEY1H[31:0]和 KEY1L[31:0]分别对应于 AES_KEY[64:127]的高 32 位与低 32 位，KEY2H[31:0]和KEY2L[31:0]分别对应于 AES_KEY[128:191]的高32 位与低32位，KEY3H[31:0]和KEY3L[31:0]分别对应于 AES_KEY[192:255]的高 32 位与低 32 位。

## CAU_KEY0H

偏移地址：0x20

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY0H[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY0H[15:0]</td></tr></table>

## CAU_KEY0L

偏移地址：0x24

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY0L[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY0L[15:0]</td></tr></table>

## CAU_KEY1H

偏移地址：0x28

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY1H[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY1H[15:0]</td></tr></table>

## CAU_KEY1L

偏移地址：0x2C

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY1L[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY1L[15:0]</td></tr></table>

## CAU_KEY2H

偏移地址：0x30

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY2H[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY2H[15:0]</td></tr></table>

## CAU_KEY2L

偏移地址：0x34

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY2L[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY2L[15:0]</td></tr></table>

## CAU_KEY3H

偏移地址：0x38

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY3H[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY3H[15:0]</td></tr></table>

## CAU_KEY3L

偏移地址：0x3C

复位值：0x0000 0000

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY3L[31:16]</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY3L[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY0...3(H/L)</td><td>用于 DES 或 TDES 或 AES 的密钥</td></tr></table>

