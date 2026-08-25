# 2.3. RAMECCMU 寄存器

RAMECCMU Region 0基地址：0x5200 9000

RAMECCMU Region 1基地址：0x4802 3000

# 2.3.1. RAMECCMU 全局中断寄存器（RAMECCMU_INT）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>GEDERR BWIE</td><td>GEDERR IE</td><td>GESERRIE</td><td>GEIE</td></tr><tr><td colspan="12"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>GEDERRBWIE</td><td>全局ECC双比特错误字节写中断使能0:无中断产生1:对RAM进行字节写操作期间发生ECC双比特错误检测时产生中断</td></tr><tr><td>2</td><td>GEDERRIE</td><td>全局ECC双比特错误中断使能0:无中断产生1:从RAM读操作期间发生ECC双比特错误检测时产生中断</td></tr><tr><td>1</td><td>GESERRIE</td><td>全局ECC单比特错误中断使能0:无中断产生1:从RAM读操作期间发生ECC单比特错误时产生中断</td></tr><tr><td>0</td><td>GEIE</td><td>全局ECC中断使能0:无中断产生1:发生GEDERRBWIE、GEDERRIE或GESERRIE错误之一时产生中断</td></tr></table>

# 2.3.2. RAMECCMU 监视器 x 控制寄存器（RAMECCMU_MxCTL）

地址偏移：0x20 * (x+1), (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region 1,x=0..2)

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>ECCERRLATEN</td><td>ECCDERRBWIE</td><td>ECCDERRIE</td><td>ECCSERRIE</td><td colspan="2">保留</td></tr></table>

rw 

rw 

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>ECCERRLATEN</td><td>ECC 错误锁存使能0:当 ECC 错误发生时,没有错误上下文被锁存到各自的寄存器中1:当 ECC 错误发生时,错误上下文被锁存到各自的寄存器中</td></tr><tr><td>4</td><td>ECCDERRBWIE</td><td>ECC 双比特错误字节写中断使能0:无中断产生1:对 RAM 的字节写操作发生 ECC 双比特错误时产生中断</td></tr><tr><td>3</td><td>ECCDERRIE</td><td>ECC 双比特错误中断使能0:无中断产生1:从 RAM 读操作发生 ECC 双比特错误时产生中断</td></tr><tr><td>2</td><td>ECCSERRIE</td><td>ECC 单比特错误中断使能0:无中断产生1:从 RAM 读操作时发生 ECC 单比特错误时产生中断</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 2.3.3. RAMECCMU 监视器 x 状态寄存器（RAMECCMU_MxSTAT）

地址偏移：0x24 + 0x20 * x, (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region 1,x=0..2)复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="13">保留</td><td>ECCDER</td><td>ECCDER</td><td>ECCSERR</td></tr><tr><td>RBWDF</td><td>RDF</td><td>DCF</td></tr></table>

rc_w0 

rc_w0 

rc_w0 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>ECCDERRBWDF</td><td>字节写入时 ECC 双比特错误检测标志该位由硬件置 1,软件写 0 清除。0:当 ECCDERRDF 为 1 时,表示在读时检测到双比特错误</td></tr></table>

1：在非对齐写时检测到双比特错误

<table><tr><td>1</td><td>ECCDERRDF</td><td>ECC 双比特错误检测标志该位由硬件置 1,软件写 0 清除。0:未检测到错误1:检测到错误</td></tr></table>

<table><tr><td>0</td><td>ECCSERRDCF</td><td>ECC 单比特错误检测和纠正标志该位由硬件置 1,软件写 0 清除。0:无错误检测和纠正1:错误被检测和纠正</td></tr></table>

# 2.3.4. RAMECCMU 监视器 x 故障地址寄存器（RAMECCMU_MxFADDR）

地址偏移：0x28 + 0x20 * x, (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region 1,x=0..2)

复位值：0x2400 0000（AXI SRAM）

0x0000 0000（ITCM） 

0x2000 0000（D0TCM） 

0x2000 0004（D1TCM） 

0x2408 0000（ITCM/DTCM/AXI SRAM 共享 RAM）

0x3000 0000（SRAM0） 

0x3000 4000（SRAM1） 

0x3880 0000（BKPSRAM） 

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCFADDR[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCFADDR[15:0]</td></tr></table>

位/位域 名称 描述

31:0 ECCFADDR[31:0] ECC 错误故障地址

该寄存器包含错误发生时 ECC错误生成的地址。

# 2.3.5. RAMECCMU 监视器 x 故障数据低位寄存器（RAMECCMU_MxFDL）

地址偏移：0x2C + 0x20 * x, (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region1,x=0..2)

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCFDL[31:16]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCFDL[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ECCFDL[31:0]</td><td>ECC 故障数据低位该寄存器包含发生错误时由 ECC 错误产生的数据的 LSB 或 32 位 SRAM 的完整存储器字内容。</td></tr></table>

# 2.3.6. RAMECCMU 监视器 x 故障数据高位寄存器（RAMECCMU_MxFDH）

地址偏移： $0 { \times } 3 0 + 0 { \times } 2 0 { \times } ~ \times ,$ (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region 1,x=0..2)

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCFDH[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCFDH[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ECCFDH[31:0]</td><td>ECC 故障数据高位(64-bit)该寄存器包含发生错误时由 ECC 错误产生的数据的 MSB。</td></tr></table>

# 2.3.7. RAMECCMU监视器x故障ECC错误代码寄存器（RAMECCMU_MxFECODE）

地址偏移： $0 { \times } 3 4 + 0 { \times } 2 0 { \times } ~ \times ,$ (x是ECC监视器编号，对于Region 0，x=0..4，而对于Region 1,x=0..2)

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ECCFECODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ECCFECODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

31:0 ECCFECODE[31:0] ECC 故障错误代码

该寄存器包含发生位错误的索引和 ECC代码。
