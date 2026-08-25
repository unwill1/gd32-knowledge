## 9.4. TRNG 寄存器

TRNG 基地址：0x5006 0800

## 9.4.1. 控制寄存器（TRNG_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>TRNGIE</td><td>TRNGEN</td><td colspan="2">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>TRNGIE</td><td>中断使能位,当DRDY,SEIF或CEIF位被置位时该位控制生成一个中断。0:禁止TRNG中断1:使能TRNG中断</td></tr><tr><td>2</td><td>TRNGEN</td><td>TRNG使能位0:禁止TRNG模块1:使能TRNG模块</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 9.4.2. 状态寄存器（TRNG_STAT）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按字节（8 位）、半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td>SEIF</td><td>CEIF</td><td colspan="2">保留</td><td>SECS</td><td>CECS</td><td>DRDY</td></tr><tr><td colspan="9"></td><td>rc_w0</td><td>rc_w0</td><td colspan="2"></td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>SEIF</td><td>种子错误中断标志位如果超过64个连续位具有相同值或超过32组连续交替的0和1被检测到则此位将置1。0:未检测到错误1:检测到种子错误。写0将清除该位</td></tr><tr><td>5</td><td>CEIF</td><td>时钟错误中断标志位如果TRNG_CLK时钟频率低于HCLK频率的1/16时该位被置位。0:未检测到错误1:检测到时钟错误。写0将清除该位</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>SECS</td><td>种子错误当前状态0:当前未检测到种子错误。如果SEIF=1和SECS=0,说明之前已经检测到种子错误但现在已恢复正常。1:当前检测到种子错误。如果超过64个连续位具有相同值或超过32组连续交替的0和1被检测到时,该位置1。</td></tr><tr><td>1</td><td>CECS</td><td>时钟错误当前状态0:当前未检测到时钟错误。如果CEIF=1和CECS=0,则意味着之前已检测到时钟错误但现在已恢复正常。1:当前检测到时钟错误。此时TRNG_CLK时钟频率低于1/16HCLK频率。</td></tr><tr><td>0</td><td>DRDY</td><td>随机数准备状态位读TRNG_DATA寄存器会清零该位,当一个新的随机数产生时被置位。0:TRNG数据寄存器的内容无效1:TRNG数据寄存器的内容有效</td></tr></table>

## 9.4.3. 数据寄存器（TRNG_DATA）

地址偏移：0x08

复位值：0x0000 0000

在读此寄存器之前，软件必须确保 DRDY位已置 1。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">TRNGDATA[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">TRNGDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>TRNGDATA[31:0]</td><td>32 位随机数据</td></tr></table>
