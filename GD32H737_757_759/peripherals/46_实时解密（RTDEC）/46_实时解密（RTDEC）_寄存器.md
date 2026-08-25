# 46.5. RTDEC 寄存器

RTDEC0基地址: 0x5200 B800

RTDEC1基地址: 0x5200 BC00

# 46.5.1. 区域 x 配置寄存器（RTDEC_AREx_CFG）

地址偏移：0x20 + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_FMVER[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">ARE_K_CRC[7:0]</td><td colspan="2">保留</td><td colspan="2">MODE[1:0]</td><td>保留</td><td>ARE_K_LK</td><td>ARE_CFG_LK</td><td>ARE_EN</td></tr><tr><td colspan="10">r</td><td colspan="3">rw</td><td>rs</td><td>rs</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>ARE_FMVER[15:0]</td><td>区域固件版本在RTDEC_AREx_CFG寄存器中的ARE_EN位使能之前,需要先配置好区域固件版本。</td></tr><tr><td>15:8</td><td>ARE_K_CRC[7:0]</td><td>区域密钥的8位CRC当ARE_K_LK=0时,如果用户按照KEY0-&gt;KEY1-&gt;KEY2-&gt;KEY3的顺序加载该区域的密钥,则ARE_K_CRC[7:0]将由硬件自动计算。当启动新的有效序列时,立即开始新的计算。直到有效序列完成前,取ARE_K_CRC[7:0]值都将为0。当ARE_K_LK=1时,直到下一次复位前,ARE_K_CRC值保持不变。CRC计算采用标准CRC-8-CCITT算法X8+X2+X+1,计算结果为8位校验和。这些位是只读位。注意:当密钥的最后一位写入后,才会更新CRC信息。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:4</td><td>MODE[1:0]</td><td>RTDEC模式位这些位配置此区域的RTDEC操作模式:00:仅对代码访问进行解密。01:仅解密数据访问。10:所有读访问都被解密(代码或数据)。11:保留。当MODE[1:0]位改变时,区域的密钥和相关的CRC被硬件自动清除。</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>ARE_K_LK</td><td>区域密钥锁定位0:允许对RTDEC_AREx_KEY寄存器写入。1:禁止对RTDEC_AREx_KEY寄存器写入,ARE_K_CRC[7:0]也被锁定。该位只能由软件置位一次,且RTDEC复位之前无法清除。当该位被设置时,它禁止对该区域密钥寄存器的写访问。</td></tr><tr><td>1</td><td>ARE_CFG_LK</td><td>区域配置锁定位0:允许对RTDEC_AREx_CFG、RTDEC_AREx_SADDR、RTDEC_AREx_EADDR、RTDEC_AREx_NONCE0~1、RTDEC_AREx_KEY0~3寄存器的写入。1:禁止对RTDEC_AREx_CFG、RTDEC_AREx_SADDR、RTDEC_AREx_EADDR、RTDEC_AREx_NONCE0~1、RTDEC_AREx_KEY0~3寄存器的写入。ARE_K_CRC[7:0]也被锁定该位只能由软件置位一次,且RTDEC复位之前无法清除。当该位置1时,ARE_K_LK位被强制为1时,它禁止对该区域配置、起始地址、结束地址和随机数寄存器的写访问。</td></tr><tr><td>0</td><td>ARE_EN</td><td>0:禁能区域实时解密。1:使能区域实时解密。在该位置位之前,区域配置信息必须有效。</td></tr></table>

# 46.5.2. 区域 x 起始地址寄存器（RTDEC_AREx_SADDR）

地址偏移：0x24 + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_SADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_SADDR[15:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_SADDR[31:0]</td><td>区域x起始地址位必须在RTDEC_AREx_CFG寄存器中的ARE_EN位置1前写入这些位。如果RTDEC_AREx_CFG寄存器中的ARE_CFG_LK位置1,则写入这些位无效。注意:确定区域时,低12位(LSB)和高4位(MSB)将被忽略。读取该寄存器时,4个MSB位和12个LSB位返回0。</td></tr></table>

# 46.5.3. 区域 x 结束地址寄存器（RTDEC_AREx_EADDR）

地址偏移：0x28 + 0x30 * x（x = 0~3）

复位值：0x0000 0FFF

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_EADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_EADDR[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_EADDR[31:0]</td><td>区域x结束地址位必须在RTDEC_AREx_CFG寄存器中的ARE_EN位置1前写入这些位,且ARE_EADDR不能小于ARE_SADDR。如果RTDEC_AREx_CFG寄存器中的ARE_CFG_LK位置1,则写入这些位无效。注意:确定区域时,低12位(LSB)和高4位(MSB)将被忽略。读取该寄存器时,4个MSB位和12个LSB位返回1。</td></tr></table>

# 46.5.4. 区域 x 随机数寄存器 0（RTDEC_AREx_NONCE0）

地址偏移： $0 { \times } 2 0 + 0 { \times } 3 0 ^ { \star } \times ( \mathsf { x } = 0 { \sim } 3 )$ ）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_NONCE0[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_NONCE0[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_NONCE0[31:0]</td><td>区域x随机数寄存器位,对应ARE_NONCE[31:0]。必须在RTDEC_AREx_CFG寄存器中的ARE_EN位置1前写入这些位。如果RTDEC_AREx_CFG寄存器中的ARE_CFG_LK位置1,则写入这些位无效。</td></tr></table>

# 46.5.5. 区域 x 随机数寄存器 1（RTDEC_AREx_NONCE1）

地址偏移：0x30 + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_NONCE1[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_NONCE1[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_NONCE1[31:0]</td><td>区域x随机数寄存器位。对应ARE_NONCE[63:32]。参考ARE_NONCE0[31:0]描述</td></tr></table>

# 46.5.6. 区域 x 秘钥寄存器 0（RTDEC_AREx_KEY0）

地址偏移： $0 { \times } 3 4 + 0 { \times } 3 0 ^ { \star } \times ~ ( \times = 0 { - } 3 )$ 

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_KEY0[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_KEY0[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_KEY0[31:0]</td><td>区域x密钥位, ARE_KEY[31:0].必须在RTDEC_AREx_CFG寄存器中的ARE_EN位置1前写入这些位。如果RTDEC_AREx_CFG寄存器中的ARE_CFG_LK位或ARE_K_LK位置1,则写入这些位无效。当读取这些位时,返回0。注意:当应用程序成功更改RTDEC_AREx_CFG寄存器中的MODE[1:0]位时,RTDEC_AREx_KEY0寄存器和相关的ARE_K_CRC将被擦除。</td></tr></table>

# 46.5.7. 区域 x 秘钥寄存器 1（RTDEC_AREx_KEY1）

地址偏移：0x38 + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_KEY1[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_KEY1[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_KEY1[31:0]</td><td>区域x密钥位, ARE_KEY[63:32]。参考ARE_KEY0[31:0]描述</td></tr></table>

# 46.5.8. 区域 x 秘钥寄存器 2（RTDEC_AREx_KEY2）

地址偏移：0x3C + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_KEY2[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_KEY2[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_KEY2[31:0]</td><td>区域x密钥位,对应ARE_KEY[95:64]。参考ARE_KEY0[31:0]描述</td></tr></table>

# 46.5.9. 区域 x 秘钥寄存器 3（RTDEC_AREx_KEY3）

地址偏移：0x40 + 0x30 * x（x = 0~3）

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ARE_KEY3[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ARE_KEY3[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ARE_KEY3[31:0]</td><td>区域x密钥位,对应ARE_KEY[127:96]。参考ARE_KEY0[31:0]描述</td></tr></table>

# 46.5.10. 中断标志寄存器（RTDEC_INTF）

地址偏移：0x300

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>KEF</td><td>ECONEF</td><td>SECEF</td></tr></table>

r r r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>KEF</td><td>密钥错误中断标志位0:未检测到密钥错误1:检测到密钥错误。中止事件后在使能的加密区域上检测到读取访问。如果RTDEC_INTEN寄存器中的KEIE位置1,则产生中断。由于发生中止事件(篡改检测、未授权的调试器连接、不受信的引导、SPC级别低至无保护降级)重置密钥寄存器后,在加密区和非加密区上发生读访问时,该位由硬件置位。该位通过向RTDEC_INTC寄存器中的KEC位写1清零。KEF位置1后,后续对加密区域和非加密区域的读取都将返回0。直到再次初始化RTDEC密钥前,该位将一直保持置位。</td></tr><tr><td>1</td><td>ECONEF</td><td>只执行或从不执行错误中断标志0:未检测到只执行错误或从不执行错误。1:检测到只执行错误或从不执行错误。在MODE[1:0]设置为00的区域上检测到读取访问,或在MODE[1:0]设置为01的区域上检测到执行访问。如果RTDEC_INTEN寄存器中的ECONIE位置1,则产生中断。当在MODE[1:0]设置为00的任何加密区域上检测到读数据而不是取指令访问时,或当在MODE[1:0]设置为00的任何加密区域上检测到取指令而不是读数据访问时,该位都将由硬件置1。通过向RTDEC_INTC寄存器中的ECONEC位写1清零。注意:对于非法访问,RTDEC返回0。</td></tr><tr><td>0</td><td>SECEF</td><td>安全错误中断标志0:未检测到安全错误1:检测到安全错误。如果RTDEC_INTEN寄存器中的SECEIE位置1,则产生中断。当检测到至少一个安全错误(非法访问密钥、配置锁定后的非法写入)时,由硬件置1。通过向RTDEC_INTC寄存器中的SECEC位写1清零。</td></tr></table>

# 46.5.11. 中断标志清除寄存器（RTDEC_INTC）

地址偏移：0x304

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>KEC</td><td>ECONEC</td><td>SECEC</td></tr></table>

w w w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>KEC</td><td>密钥错误标志位清除位0:无影响1:清除密钥错误标志注意:RTDEC密钥寄存器应正确重新初始化,而不仅仅是清除KEF,以便能再次读取或执行任何加密区域。</td></tr><tr><td>1</td><td>ECONEC</td><td>只执行或从不执行错误标志清除位0:无影响1:清除只执行或从不执行错误标志</td></tr><tr><td>0</td><td>SECEC</td><td>安全错误标志清除位0:无影响1:清除安全错误标志</td></tr></table>

# 46.5.12. 中断使能寄存器（RTDEC_INTEN）

地址偏移：0x308

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>KEIE</td><td>ECONEIE</td><td>SECEIE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>KEIE</td><td>密钥错误中断使能位软件置位和清除0:禁能密钥错误中断1:使能密钥错误中断</td></tr><tr><td>1</td><td>ECONEIE</td><td>仅执行或从不执行错误中断使能位软件置位和清除0:禁能仅执行或从不执行错误中断1:使能仅执行或从不执行错误中断</td></tr><tr><td>0</td><td>SECEIE</td><td>安全错误中断使能位软件置位和清除</td></tr></table>

0：禁能安全错误中断

1：使能安全错误中断
