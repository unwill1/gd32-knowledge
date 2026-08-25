## 11.4. PKCAU 寄存器

PKCAU 基地址：0x5006 1000

## 11.4.1. 控制寄存器 (PKCAU_CTL)

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>ADDRERRIE</td><td>RAMERRIE</td><td>保留</td><td>ENDIE</td><td>保留</td></tr><tr><td colspan="12">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="6">MODESEL[5:0]</td><td colspan="6">保留</td><td>START</td><td>PKCAUEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ADDRERRIE</td><td>地址错误中断使能0: 地址错误中断禁能。1: 地址错误中断使能。</td></tr><tr><td>19</td><td>RAMERRIE</td><td>RAM 错误中断使能0: RAM 错误中断禁能。1: RAM 错误中断使能。</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>ENDIE</td><td>运算结束中断使能0: 运算结束中断禁能。1: 运算结束中断使能。</td></tr><tr><td>16:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13:8</td><td>MODESEL</td><td>PKCAU 运算模式选择000000: 蒙哥马利参数计算然后模幂。000001: 只进行蒙哥马利参数计算。000010: 只进行模幂运算(蒙哥马利参数必须预先加载)。000111: RSA CRT 求幂。001000: 模逆运算。001001: 算术加法。001010: 算术减法。001011: 算术乘法。001100:算术比较。</td></tr><tr><td></td><td></td><td>001101:取模。</td></tr><tr><td></td><td></td><td>001110:模加法。</td></tr><tr><td></td><td></td><td>001111:模减法。</td></tr><tr><td></td><td></td><td>010000:蒙哥马利乘法。</td></tr><tr><td></td><td></td><td>100000:先进行蒙哥马利参数计算,然后进行ECC标量乘法。</td></tr><tr><td></td><td></td><td>100010:只进行ECC标量乘法(蒙哥马利参数必须预先加载)。</td></tr><tr><td></td><td></td><td>100100:ECDSA签名。</td></tr><tr><td></td><td></td><td>100110:ECDSA验证。</td></tr><tr><td></td><td></td><td>101000:椭圆曲线Fp上点的检查。</td></tr><tr><td></td><td></td><td>其他值保留。</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>START</td><td>PKCAU开始运算该位由软件置1来启动PKCAU运算,运算模式在PKCAU_CTL寄存器的MODSEL[5:0]中指定的。当PKCAU_STAT寄存器中BUSY位为1,对该位写1无效。</td></tr><tr><td>0</td><td>PKCAUEN</td><td>PKCAU使能0:PKCAU禁能1:PKCAU使能</td></tr></table>

## 11.4.2. 状态寄存器 (PKCAU_STAT)

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>ADDRERR</td><td>RAMERR</td><td>保留</td><td>ENDF</td><td>BUSY</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>r</td><td></td><td>r</td><td>r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ADDRERR</td><td>地址错误0:无地址错误。1:访问的 PKCAU RAM 地址超出预期范围,产生地址错误。</td></tr><tr><td>19</td><td>RAMERR</td><td>PKCAU RAM 错误0:未产生 PKCAU RAM 错误1: 当 PKCAU 内核在使用 PKCAU RAM 时,AHB 也在访问 PKCAU RAM,将产生 PKCAU RAM 错误。</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>ENDF</td><td>PKCAU 运算结束标志当运算执行完成,该位由硬件置 1。</td></tr><tr><td>16</td><td>BUSY</td><td>忙标志当 PKCAU_CTL 寄存器中 START 位置 1,该位由硬件置 1。当 PKCAU 运算结束,该位由硬件清 0。</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 11.4.3. 状态清除寄存器 (PKCAU_STATC)

地址偏移：0x08

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td>ADDRERRC</td><td>RAMERRC</td><td>保留</td><td>ENDFC</td><td>保留</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td></td><td>w</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>ADDRERRC</td><td>地址错误标志清除软件对该位写1可以清除PKCAU_STAT寄存器中ADDRERR位。</td></tr><tr><td>19</td><td>RAMERRC</td><td>PKCAU RAM错误标志清除软件对该位写1可以清除PKCAU_STAT寄存器中RAMERR位。</td></tr><tr><td>18</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>17</td><td>ENDFC</td><td>PKCAU运算结束标志清除软件对该位写1可以清除PKCAU_STAT寄存器中ENDF位。</td></tr><tr><td>16:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
