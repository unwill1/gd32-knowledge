## 15.12. FFT 寄存器

FFT 基地址： 0x4002 5000

## 15.12.1. 控制和状态寄存器（FFT_CSR）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DMABSY</td><td>CCF</td><td>CCIE</td><td>TAEIF</td><td>TAEIE</td><td colspan="11">保留</td></tr><tr><td>r</td><td>rc_w1</td><td>rw</td><td>rc_w1</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="2">IMSEL[1:0]</td><td colspan="3">DOWNSAMP[3:0]</td><td>WINEN</td><td colspan="3">保留</td><td>IFFTMODE</td><td colspan="3">NUMPT[2:0]</td><td colspan="2">FFTEN</td></tr><tr><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td colspan="3">rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DMABSY</td><td>DMA忙该位表示DMA是否在忙。该位只读。0: DMA不忙1: DMA在忙</td></tr><tr><td>30</td><td>CCF</td><td>FFT计算完成标志该位写1清0。0: FFT正在进行计算1: FFT计算完成</td></tr><tr><td>29</td><td>CCIE</td><td>使能FFT计算完成中断0: 禁能计算完成中断1: 使能计算完成中断</td></tr><tr><td>28</td><td>TAEIF</td><td>传输访问错误中断标志该位写1清0。0: 未检测到传输访问错误1: 检测到传输访问错误</td></tr><tr><td>27</td><td>TAEIE</td><td>使能传输访问错误中断0: 禁能传输访问错误中断1: 使能传输访问错误中断</td></tr></table>

<table><tr><td>26:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:13</td><td>IMSEL[1:0]</td><td>虚部输入源选择00: 虚部输入来源于 FFT_IMSADDR01: 虚部输入是 010: 虚部输入是与 FFT_IMSADDR 中的虚部数据符号相反的值</td></tr><tr><td>12:9</td><td>DOWNSAMP[3:0]</td><td>输入数据下采样选择0000: 下采样 10001: 下采样 20010: 下采样 30011: 下采样 40100: 下采样 50101: 下采样 60110: 下采样 70111: 下采样 81000: 下采样 91001: 下采样 101010: 下采样 111011: 下采样 121100: 下采样 131101: 下采样 141110: 下采样 151111: 下采样 16当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr><tr><td>8</td><td>WINEN</td><td>使能窗函数0: 无窗函数1: 窗函数使能。窗函数来源于 FFT_WSADDR。当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>IFFTMODE</td><td>使能 IFFT 模式0: FFT 模式1: IFFT 模式(FFT 逆变换)当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr><tr><td>3:1</td><td>NUMPT[2:0]</td><td>FFT点数000: 32001: 64010: 128011: 256</td></tr></table>

<table><tr><td></td><td></td><td>100: 512</td></tr><tr><td></td><td></td><td>101: 1024</td></tr><tr><td></td><td></td><td>其他: 保留</td></tr><tr><td></td><td></td><td>当FFT_CSR寄存器的FFTEN位为1时,该位不可写。</td></tr><tr><td>0</td><td>FFTEN</td><td>使能FFT</td></tr><tr><td></td><td></td><td>当FFT计算结束时,该位被自动清0。软件不要清零该位。</td></tr><tr><td></td><td></td><td>0: 禁能FFT</td></tr><tr><td></td><td></td><td>1: 使能 FFT</td></tr></table>

## 15.12.2. 实部基地址寄存器（FFT_RESADDR）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">RESADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">RESADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>RESADDR[31:0]</td><td>FFT 实部基地址该地址必须按照32位格式对齐。当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr></table>

## 15.12.3. 虚部基地址寄存器（FFT_IMSADDR）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IMSADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IMSADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IMSADDR[31:0]</td><td>FFT 虚部基地址该地址必须按照32位格式对齐。当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr></table>

## 15.12.4. 窗函数基地址寄存器（FFT_WSADDR）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">WSADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WSADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>WSADDR[31:0]</td><td>FFT 窗函数基地址该地址必须按照32位格式对齐。当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr></table>

## 15.12.5. 输出基地址寄存器（FFT_OSADDR）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td colspan="16">OSADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OSADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OSADDR[31:0]</td><td>FFT 输出结果基地址该地址必须按照32位格式对齐。当 FFT_CSR 寄存器的 FFTEN 位为 1 时,该位不可写。</td></tr></table>

## 15.12.6. 循环长度寄存器（FFT_LOOPLEN）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字(32 位)访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">INDEX[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LENGTH[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>INDEX[15:0]</td><td>DMA循环缓冲区索引索引值不能超过LENGTH[15:0],其范围在0~LENGTH[15:0]。每次结束时加1,当增加到LENGTH[15:0]时归零。实际的实部DMA起始地址 = FFT_RESADDR + { INDEX, 2&#x27;b00}。实际的虚部DMA起始址 = FFT_IMSADDR + {INDEX, 2&#x27;b00}。</td></tr><tr><td>15:0</td><td>LENGTH[15:0]</td><td>FFT输入数据的DMA循环缓冲区长度当FFT_CSR寄存器的FFTEN位为1时,该位不可写。</td></tr></table>
