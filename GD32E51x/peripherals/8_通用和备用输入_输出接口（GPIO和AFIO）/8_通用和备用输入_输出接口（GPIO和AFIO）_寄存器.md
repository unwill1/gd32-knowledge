## 8.5. GPIO 寄存器

GPIOA 基地址：0x4001 0800

GPIOB 基地址：0x4001 0C00

GPIOC 基地址：0x4001 1000

GPIOD 基地址：0x4001 1400

GPIOE 基地址：0x4001 1800

GPIOF 基地址：0x4001 1C00

GPIOG 基地址：0x4001 2000

AFIO 基地址：0x4001 0000

## 8.5.1. 端口控制寄存器 0(GPIOx_CTL0，x=A..G)

地址偏移：0x00

复位值：0x4444 4444(x= A, C..G) / 0x4448 4444(x=B)

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CTL7[1:0]</td><td colspan="2">MD7[1:0]</td><td colspan="2">CTL6[1:0]</td><td colspan="2">MD6[1:0]</td><td colspan="2">CTL5[1:0]</td><td colspan="2">MD5[1:0]</td><td colspan="2">CTL4[1:0]</td><td colspan="2">MD4[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CTL3[1:0]</td><td colspan="2">MD3[1:0]</td><td colspan="2">CTL2[1:0]</td><td colspan="2">MD2[1:0]</td><td colspan="2">CTL1[1:0]</td><td colspan="2">MD1[1:0]</td><td colspan="2">CTL0[1:0]</td><td colspan="2">MD0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CTL7[1:0]</td><td>Pin 7 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr><tr><td>29:28</td><td>MD7[1:0]</td><td>Pin 7 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr><tr><td>27:26</td><td>CTL6[1:0]</td><td>Pin 6 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr><tr><td>25:24</td><td>MD6[1:0]</td><td>Pin 6 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr><tr><td>23:22</td><td>CTL5[1:0]</td><td>Pin 5 配置位</td></tr></table>

<table><tr><td>21:20</td><td>MD5[1:0]</td><td>Pin 5 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr></table>

<table><tr><td>19:18</td><td>CTL4[1:0]</td><td>Pin 4 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr></table>

<table><tr><td>17:16</td><td>MD4[1:0]</td><td>Pin 4 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr></table>

<table><tr><td>15:14</td><td>CTL3[1:0]</td><td>Pin 3 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr></table>

<table><tr><td>13:12</td><td>MD3[1:0]</td><td>Pin 3 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr></table>

<table><tr><td>11:10</td><td>CTL2[1:0]</td><td>Pin 2 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr></table>

<table><tr><td>9:8</td><td>MD2[1:0]</td><td>Pin 2 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr></table>

<table><tr><td>7:6</td><td>CTL1[1:0]</td><td>Pin 1 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr></table>

<table><tr><td>5:4</td><td>MD1[1:0]</td><td>Pin 1 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr></table>

3:2 CTL0[1:0] Pin 0 配置位该位由软件置位和清除。输入模式（MD[1:0] = 00）00：模拟输入01：浮空输入10：上拉输入/下拉输入11：保留输出模式（MD[1:0] > 00）00：GPIO 推挽输出01：GPIO 开漏输出

1:0 MD0[1:0] Pin 0 模式位

## 8.5.2. 端口控制寄存器 1(GPIOx_CTL1, x=A..G)

地址偏移：0x04

复位值：0x8884 4444(x=A) / 0x4444 4444(x= B..G)

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CTL15[1:0]</td><td colspan="2">MD15[1:0]</td><td colspan="2">CTL14[1:0]</td><td colspan="2">MD14[1:0]</td><td colspan="2">CTL13[1:0]</td><td colspan="2">MD13[1:0]</td><td colspan="2">CTL12[1:0]</td><td colspan="2">MD12[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CTL11[1:0]</td><td colspan="2">MD11[1:0]</td><td colspan="2">CTL10[1:0]</td><td colspan="2">MD10[1:0]</td><td colspan="2">CTL9[1:0]</td><td colspan="2">MD9[1:0]</td><td colspan="2">CTL8[1:0]</td><td colspan="2">MD8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CTL15[1:0]</td><td>Pin 15 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr><tr><td>29:28</td><td>MD15[1:0]</td><td>Pin 15 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr><tr><td>27:26</td><td>CTL14[1:0]</td><td>Pin 14 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr><tr><td>25:24</td><td>MD14[1:0]</td><td>Pin 14 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr><tr><td>23:22</td><td>CTL13[1:0]</td><td>Pin13 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述。</td></tr><tr><td>21:20</td><td>MD13[1:0]</td><td>Pin 13 模式位该位由软件置位和清除。参考 MD0[1:0]的描述。</td></tr><tr><td>19:18</td><td>CTL12[1:0]</td><td>Pin 12配置位该位由软件置位和清除。参考CTL0[1:0]的描述。</td></tr><tr><td>17:16</td><td>MD12[1:0]</td><td>Pin 12模式位该位由软件置位和清除。参考MD0[1:0]的描述。</td></tr><tr><td>15:14</td><td>CTL11[1:0]</td><td>Pin 11配置位该位由软件置位和清除。参考CTL0[1:0]的描述。</td></tr><tr><td>13:12</td><td>MD11[1:0]</td><td>Pin 11模式位该位由软件置位和清除。参考MD0[1:0]的描述。</td></tr><tr><td>11:10</td><td>CTL10[1:0]</td><td>Pin 10配置位该位由软件置位和清除。参考CTL0[1:0]的描述。</td></tr><tr><td>9:8</td><td>MD10[1:0]</td><td>Pin10模式位该位由软件置位和清除。参考MD0[1:0]的描述。</td></tr><tr><td>7:6</td><td>CTL9[1:0]</td><td>Pin 9配置位该位由软件置位和清除。参考CTL0[1:0]的描述。</td></tr><tr><td>5:4</td><td>MD9[1:0]</td><td>Port 9模式位该位由软件置位和清除。参考MD0[1:0]的描述。</td></tr><tr><td>3:2</td><td>CTL8[1:0]</td><td>Pin8配置位该位由软件置位和清除。参考CTL0[1:0]的描述。</td></tr><tr><td>1:0</td><td>MD8[1:0]</td><td>Pin 8模式位该位由软件置位和清除。参考MD0[1:0]的描述。</td></tr></table>

## 8.5.3. 端口输入状态寄存器(GPIOx_ISTAT，x=A..G)

地址偏移：0x08

复位值：0x0000 XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ISTAT15</td><td>ISTAT14</td><td>ISTAT13</td><td>ISTAT12</td><td>ISTAT11</td><td>ISTAT10</td><td>ISTAT 9</td><td>ISTAT 8</td><td>ISTAT 7</td><td>ISTAT 6</td><td>ISTAT 5</td><td>ISTAT 4</td><td>ISTAT 3</td><td>ISTAT 2</td><td>ISTAT 1</td><td>ISTAT 0</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>ISTATy</td><td>端口输入状态位(<eq>y=0..15</eq>)这些位由硬件置位和清除。0:引脚输入信号为低电平1:引脚输入信号为高电平</td></tr></table>

## 8.5.4. 端口输出控制寄存器(GPIOx_OCTL，x=A..G)

地址偏移：0x0C

复位值: 0x0000 A000（GPIOA_OCTL）

0x0000 0010（GPIOB_OCTL） 

0x0000 0000（GPIOx_OCTL, x=C..G） 


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OCTL15</td><td>OCTL14</td><td>OCTL13</td><td>OCTL12</td><td>OCTL11</td><td>OCTL10</td><td>OCTL9</td><td>OCTL8</td><td>OCTL7</td><td>OCTL6</td><td>OCTL5</td><td>OCTL4</td><td>OCTL3</td><td>OCTL2</td><td>OCTL1</td><td>OCTL0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>OCTLy</td><td>端口输出控制位(<eq>y=0..15</eq>)这些位由软件置位和清除。0:引脚输出低电平1:引脚输出高电平</td></tr></table>

## 8.5.5. 端口位操作寄存器(GPIOx_BOP，x=A..G)

地址偏移：0x10

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BOP15</td><td>BOP14</td><td>BOP13</td><td>BOP12</td><td>BOP11</td><td>BOP10</td><td>BOP9</td><td>BOP8</td><td>BOP7</td><td>BOP6</td><td>BOP5</td><td>BOP4</td><td>BOP3</td><td>BOP2</td><td>BOP1</td><td>BOP0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>CRy</td><td>端口清除位 y (y=0..15)这些位由软件置位和清除。0:相应的OCTLy位没有改变1:清除相应的OCTLy位为0</td></tr><tr><td>15:0</td><td>BOPy</td><td>端口置位位 y (y=0..15)这些位由软件置位和清除。0:相应的OCTLy位没有改变1:设置相应的OCTLy位为1</td></tr></table>

## 8.5.6. 位清除寄存器(GPIOx_BC，x=A..G)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CRy</td><td>端口清除位 y (y=0..15)这些位由软件置位和清除。0:相应OCTLy位没有改变1:清除相应的OCTLy位</td></tr></table>

## 8.5.7. 端口配置锁定寄存器(GPIOx_LOCK，x=A..G)

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>LKK</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>LK15</td><td>LK14</td><td>LK13</td><td>LK12</td><td>LK11</td><td>LK10</td><td>LK9</td><td>LK8</td><td>LK7</td><td>LK6</td><td>LK5</td><td>LK4</td><td>LK3</td><td>LK2</td><td>LK1</td><td>LK0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>LKK</td><td>锁定序列键该位只能通过使用Lock Key写序列设置,始终可读。0: GPIO_LOCK寄存器和端口配置没有锁定1: 直到下一次MCU复位前,GPIO_LOCK寄存器被锁定LOCK Key写序列:写1→写0→写1→读0→读1注意:在LOCK Key写序列期间,LK[15:0]的值必须保持。</td></tr><tr><td>15:0</td><td>LKy</td><td>端口锁定位y(y=0..15)这些位由软件置位和清除。0: 相应的端口位配置没有锁定1: 当LKK位置1时,相应的端口位配置被锁定</td></tr></table>

## 8.5.8. 端口位速度寄存器(GPIOx_ SPD，x=A..G)

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>SPD15</td><td>SPD 14</td><td>SPD 13</td><td>SPD 12</td><td>SPD 11</td><td>SPD 10</td><td>SPD 9</td><td>SPD 8</td><td>SPD 7</td><td>SPD 6</td><td>SPD 5</td><td>SPD 4</td><td>SPD 3</td><td>SPD 2</td><td>SPD 1</td><td>SPD 0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>SPDy</td><td>当 MDx 值为 0b11 时,设置相应端口速度为高速(120MHz)。如果端口输出速度大于 50MHz,该位置 1,同时设置 MDx 值为 0b11。这些位由软件置位和清除。0:没有影响1:最大输出速度大于 50MHz(同时,需要设置 MDx 值为 0b11)注意:当端口输出速度大于 50MHz 时,需要使能 I/O 补偿单元。详见 AFIO_CPSCTL 寄存器中的 CPS_EN 位说明。</td></tr></table>

## 8.5.9. 事件控制寄存器(AFIO_EC)

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>EOE</td><td colspan="3">PORT[2:0]</td><td colspan="4">PIN[3:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td colspan="3">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>EOE</td><td>事件输出使能该位由软件置位和清除。当设置该位后,Cortex®的 EVENTOUT 输出将连接到由PORT[2:0]和 PIN[3:0]位选择的 I/O 口。</td></tr><tr><td>6:4</td><td>PORT[2:0]</td><td>事件输出端口选择这些位由软件置位和清除。选择用于输出 Cortex®的 EVENTOUT 信号的端口。000:选择端口 A001:选择端口 B010:选择端口 C011:选择端口 D100:选择端口 E</td></tr><tr><td>3:0</td><td>PIN[3:0]</td><td>事件输出引脚选择这些位由软件置位和清除。选择用于输出 Cortex®的 EVENTOUT 信号的引脚。0000:选择引脚 00001:选择引脚 10010:选择引脚 2...1111:选择引脚 15</td></tr></table>

## 8.5.10. AFIO 端口配置寄存器 0 (AFIO_PCF0)

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

高密度产品寄存器内存映射和位定义：

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>SPI2_RE MA</td><td>保留</td><td colspan="3">SWJ_CFG[2:0]</td><td>ENET_PHY_SEL</td><td>CAN1_REMAP</td><td>ENET_REMAP</td><td>ADC1_ET RGRT_REMAP</td><td>保留</td><td>ADC0_ET RGRT_REMAP</td><td>保留</td><td>TIMER4CH3_IREMAP</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td colspan="3">w</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PD01_REMAP</td><td colspan="2">CAN0_REMAP [1:0]</td><td>TIMER3_REMAP</td><td colspan="2">TIMER2_REMAP[1:0]</td><td colspan="2">TIMER1_REMAP[1:0]</td><td colspan="2">TIMER0_REMAP[1:0]</td><td colspan="2">USART2_REMAP[1:0]</td><td>USART1_REMAP</td><td>USART0_REMAP</td><td>I2C0_REMAP</td><td>SPI0_REMAP</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>SPI2_REMAP</td><td>SPI2/I2S2 重映射该位由软件置位和清除。0:关闭重映射功能(SPI2_NSS-I2S2_WS/PA15,SPI2_SCK-I2S2_CK/PB3,SPI2_MISO/PB4,SPI2_MOSI-I2S_SD/PB5)1:完全开启重映射功能(SPI2_NSS-I2S2_WS/PA4,SPI2_SCK-I2S2_CK/PC10,SPI2_MISO/PC11,SPI2_MOSI-I2S_SD/PC12)</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>SWJ_CFG[2:0]</td><td>串行线 JTAG 配置这些位只写(读这些位,将返回未定义值)。000:JTAG-DP 使能和 SW-DP 使能(复位状态)001:JTAG-DP 使能和 SW-DP 使能但没有 NJTRST010:JTAG-DP 禁用和 SW-DP 使能100:JTAG-DP 禁用和 SW-DP 禁用其他:未定义</td></tr><tr><td>23</td><td>ENET_PHY_SEL</td><td>以太网 MII 或 RMII PHY 选择该位由软件置位和清除,它配置以太网内部 MAC 使用外部 MII 或 RMII PHY。0:配置以太网 MAC 使用外部 MII PHY1:配置以太网 MAC 使用外部 RMII PHY</td></tr><tr><td>22</td><td>CAN1_REMAP</td><td>CAN1 I/O 重映射该位由软件置位和清除,控制着 CAN1_TX 和 CAN1_RX 引脚。0:关闭重映射功能(CAN1_RX/PB12,CAN1_TX/PB13)1:开启重映射功能(CAN1_RX/PB5,CAN1_TX/PB6)</td></tr><tr><td>21</td><td>ENET_REMAP</td><td>以太网 MAC I/O 重映射该位由软件置位和清除,控制着以太网 MAC 连接到 PHY。0:关闭重映射功能(RX_DV-CRS_DV/PA7,RXD0/PC4,RXD1/PC5,RXD2/PB0,RXD3/PB1)1:开启重映射功能(RX_DV-CRS_DV/PD8,RXD0/PD9,RXD1/PD10,RXD2/PD11,RXD3/PD12)</td></tr><tr><td>20</td><td>ADC1_ETRGRT_REMAP</td><td>ADC 1 常规转换外部触发重映射0:连接ADC1常规转换外部触发与EXTI111:连接ADC1常规转换外部触发与TIM7_TRGO</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>ADC0_ETRGRT_REMAP</td><td>ADC 0常规转换外部触发重映射该位由软件置位和清除。0:连接ADC0常规转换外部触发与EXTI111:连接ADC0常规转换外部触发与TIM7_TRGO</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>TIMER4CH3_IREMAP</td><td>TIMER4通道3内部重映射该位由软件置位和清除。0:连接TIMER4_CH3与PA31:连接TMER4_CH3与IRC40K内部时钟,用于对IRC40K进行校准</td></tr><tr><td>15</td><td>PD01_REMAP</td><td>OSC_IN/OSC_OUT重映射到Port D0/Port D1该位由软件置位和清除。0:关闭重映射功能1:OSC_IN重映射到PD0,OSC_OUT重映射到PD1</td></tr><tr><td>14:13</td><td>CAN0_REMAP[1:0]</td><td>CAN0接口重映射这些位由软件置位和清除。00:关闭重映射功能(CAN0_RX/PA11,CAN0_TX/PA12)01:没有使用10:开启重映射部分功能(CAN0_RX/PB8,CAN0_TX/PB9)11:完全开启重映射功能(CAN0_RX/PD0,CAN0_TX/PD1)</td></tr><tr><td>12</td><td>TIMER3_REMAP</td><td>TIMER3重映射该位由软件置位和清除。0:关闭重映射功能(TIMER3_CH0/PB6,TIMER3_CH1/PB7,TIMER3_CH2/PB8,TIMER3_CH3/PB9)1:完全开启重映射功能(TIMER3_CH0/PD12,TIMER3_CH1/PD13,TIMER3_CH2/PD14,TIMER3_CH3/PD15)</td></tr><tr><td>11:10</td><td>TIMER2_REMAP[1:0]</td><td>TIMER2重映射这些位由软件置位和清除。00:关闭重映射功能(TIMER2_CH0/PA6,TIMER2_CH1/PA7,TIMER2_CH2/PB0,TIMER2_CH3/PB1)01:没有使用10:开启重映射部分功能(TIMER2_CH0/PB4,TIMER2_CH1/PB5,TIMER2_CH2/PB0,TIMER2_CH3/PB1)11:完全开启重映射功能(TIMER2_CH0/PC6,TIMER2_CH1/PC7,TIMER2_CH2/PC8,TIMER2_CH3/PC9)</td></tr><tr><td>9:8</td><td>TIMER1_REMAP[1:0]</td><td>TIMER1重映射这些位由软件置位和清除。00:关闭重映射功能(TIMER1_CH0/TIMER1_ETI/PA0,TIMER1_CH1/PA1,TIMER1_CH2/PA2, TIMER1_CH3/PA3)01:开启重映射部分功能(TIMER1_CH0/TIMER1_ETI/PA15,TIMER1_CH1/PB3,TIMER1_CH2/PA2,TIMER1_CH3/PA3)10:开启重映射部分功能(TIMER1_CH0/TIMER1_ETI/PA0,TIMER1_CH1/PA1,TIMER1_CH2/PB10,TIMER1_CH3/PB11)11:完全开启重映射功能(TIMER1_CH0/TIMER1_ETI/PA15,TIMER1_CH1/PB3,TIMER1_CH2/PB10,TIMER1_CH3/PB11)</td></tr><tr><td>7:6</td><td>TIMER0_REMAP[1:0]</td><td>TIMER0 重映射这些位由软件置位和清除。00:关闭重映射功能(TIMER0_ETI/PA12,TIMER0_CH0/PA8,TIMER0_CH1/PA9,TIMER0_CH2/PA10,TIMER0_CH3/PA11,TIMER0_BRKIN/PB12,TIMER0_CH0_ON/PB13,TIMER0_CH1_ON/PB14,TIMER0_CH2_ON/PB15)01:开启重映射部分功能(TIMER0_ETI/PA12,TIMER0_CH0/PA8,TIMER0_CH1/PA9,TIMER0_CH2/PA10,TIMER0_CH3/PA11,TIMER0_BRKIN/PA6,TIMER0_CH0_ON/PA7,TIMER0_CH1_ON/PB0,TIMER0_CH2_ON/PB1)10:没有使用11:完全开启重映射功能(TIMER0_ETI/PE7,TIMER0_CH0/PE9,TIMER0_CH1/PE11,TIMER0_CH2/PE13,TIMER0_CH3/PE14,TIMER0_BRKIN/PE15,TIMER0_CH0_ON/PE8,TIMER0_CH1_ON/PE10,TIMER0_CH2_ON/PE12)</td></tr><tr><td>5:4</td><td>USART2_REMAP[1:0]</td><td>USART2 重映射这些位由软件置位和清除。00:关闭重映射功能(USART2_TX/PB10,USART2_RX/PB11,USART2_CK/PB12,USART2_CTS/PB13,USART2_RTS/PB14)01:开启重映射部分功能(USART2_TX/PC10,USART2_RX/PC11,USART2_CK/PC12,USART2_CTS/PB13,USART2_RTS/PB14)10:没有使用11:完全开启重映射功能(USART2_TX/PD8,USART2_RX/PD9,USART2_CK/PD10,USART2_CTS/PD11,USART2_RTS/PD12)</td></tr><tr><td>3</td><td>USART1_REMAP</td><td>USART1 重映射该位由软件置位和清除。0:关闭重映射功能(USART1_CTS/PA0,USART1_RTS/PA1,USART1_TX/PA2,USART1_RX/PA3,USART1_CK/PA4)1:开启重映射功能(USART1_CTS/PD3,USART1_RTS/PD4,USART1_TX/PD5,USART1_RX/PD6,USART1_CK/PD7)</td></tr><tr><td>2</td><td>USART0_REMAP</td><td>USART0 重映射该位由软件置位和清除。0:关闭重映射功能(USART0_TX/PA9,USART0_RX/PA10)1:开启重映射功能(USART0_TX/PB6,USART0_RX/PB7)</td></tr><tr><td>1</td><td>I2C0_REMAP</td><td>I2C0 重映射该位由软件置位和清除。0: 关闭重映射功能(I2C0_SCL/PB6,I2C0_SDA/PB7)1: 开启重映射功能(I2C0_SCL/PB8,I2C0_SDA/PB9)</td></tr><tr><td>0</td><td>SPI0_REMAP</td><td>SPI0 重映射该位由软件置位和清除。0: 关闭重映射功能(SPI0_NSS/PA4,SPI0_SCK/PA5,SPI0_MISO/PA6,SPI0_MOSI/PA7,SPI0_IO2/PA2,SPI0_IO3/PA3)1: 开启重映射功能(SPI0_NSS/PA15,SPI0_SCK/PB3,SPI0_MISO/PB4,SPI0_MOSI/PB5,SPI0_IO2/PB6,SPI0_IO3/PB7)</td></tr></table>


互联型产品的寄存器映射和位定义：


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>PTP_PPS_REMAP</td><td>TIMER1IT1_REMAP</td><td>SPI2_REMAP</td><td>保留</td><td colspan="3">SWJ_CFG[2:0]</td><td>ENET_PHY_SEL</td><td>CAN1_REMAP</td><td>ENET_REMAP</td><td colspan="4">保留</td><td>TIMER4CH3_IREMAP</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td>w</td><td></td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PD01_REMAP</td><td colspan="2">CAN0_REMAP[1:0]</td><td>TIMER3_REMAP</td><td colspan="2">TIMER2_REMAP[1:0]</td><td colspan="2">TIMER1_REMAP[1:0]</td><td colspan="2">TIMER0_REMAP[1:0]</td><td colspan="2">USART2_REMAP[1:0]</td><td>USART1_REMAP</td><td>USART0_REMAP</td><td>I2C0_REMAP</td><td>SPI0_REMAP</td></tr><tr><td>rw</td><td colspan="2">rw</td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>PTP_PPS_REMAP</td><td>以太网 PTP PPS 重映射该位由软件置位和清除,使用以太网 MAC_PPS 输出到 PB5 引脚。0: PPT_PPS 没有输出到 PB5 引脚1: PPT_PPS 输出到 PB5 引脚注意:该位只在互联型产品中可用,在其他系列中为保留位。</td></tr><tr><td>29</td><td>TIMER1ITI1_REMAP</td><td>TIMER1 内部触发 1 重映射该位由软件置位和清除,用于控制 TIMER1_ITI1 内部重映射。0: TIMER1_ITI1 内部连接到以太网 PTP 输出,用于校准1: TIMER1_ITI1 内部连接到 USB OTG SOF (起始帧) 输出,用于校准注意:该位只在互联型产品中可用,在其他系列中为保留位。</td></tr><tr><td>28</td><td>SPI2_REMAP</td><td>SPI2/I2S2 重映射该位由软件置位和清除。0: 关闭重映射功能(SPI2_NSS-I2S2_WS/PA15,SPI2_SCK-I2S2_CK/PB3,SPI2_MISO/PB4,SPI2_MOSI-I2S_SD/PB5)1: 完全开启重映射功能(SPI2_NSS-I2S2_WS/PA4,SPI2_SCK-I2S2_CK/PC10,SPI2_MISO/PC11,SPI2_MOSI-I2S_SD/PC12)注意:该位只在互联型产品中可用,在其他系列中为保留位。</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:24</td><td>SWJ_CFG[2:0]</td><td>串行线 JTAG 配置这些位只写(读这些位,将返回未定义值)。000:JTAG-DP使能和SW-DP使能:复位状态001:JTAG-DP使能和SW-DP使能:没有NJTRST010:JTAG-DP禁用和SW-DP使能100:JTAG-DP禁用和SW-DP禁用其他组合:无作用</td></tr><tr><td>23</td><td>ENET_PHY_SEL</td><td>以太网MII或RMII PHY选择该位由软件置位和清除,它配置以太网内部MAC使用外部MII或RMII PHY。0:配置以太网MAC使用外部MII PHY1:配置以太网MAC使用外部RMII PHY注意:该位只在互联型产品中有效,其他产品线中为保留位。</td></tr><tr><td>22</td><td>CAN1_REMAP</td><td>CAN1 I/O重映射该位由软件置位和清除,控制着CAN1_TX和CAN1_RX引脚。0:关闭重映射功能(CAN1_RX/PB12,CAN_TX/PB13)1:开启重映射功能(CAN1_RX/PB5,CAN_TX/PB6)注意:该位只在互联型产品中有效,其他产品线中为保留位。</td></tr><tr><td>21</td><td>ENET_REMAP</td><td>以太网MAC I/O重映射该位由软件置位和清除,控制着以太网MAC连接到PHY。0:关闭重映射功能(RX_DV-CRS_DV/PA7,RXD0/PC4,RXD1/PC5,RXD2/PB0,RXD3/PB1)1:开启重映射功能(RX_DV-CRS_DV/PD8,RXD0/PD9,RXD1/PD10,RXD2/PD11,RXD3/PD12)注意:该位只在互联型产品中有效,其他产品线中为保留位。</td></tr><tr><td>20:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>TIMER4CH3_IREMAP</td><td>TIMER4通道3内部重映射该位由软件置位和清除。0:连接TIMER4_CH3与PA31:连接IRC40K内部振荡器与TIMER4_CH3,用于对IRC40K校准</td></tr><tr><td>15</td><td>PD01_REMAP</td><td>OSC_IN/OSC_OUT重映射到Port D0/Port D1该位由软件置位和清除。0:关闭重映射功能1:OSC_IN重映射到PD0,OSC_OUT重映射到PD1</td></tr><tr><td>14:13</td><td>CAN0_REMAP[1:0]</td><td>CAN0备用功能接口重映射这些位由软件置位和清除。00:关闭重映射功能(CAN0_RX/PA11,CAN0_TX/PA12)01:没有使用10:开启重映射部分功能(CAN0_RX/PB8,CAN0_TX/PB9)11:完全开启重映射功能(CAN0_RX/PD0,CAN0_TX/PD1)</td></tr><tr><td>12</td><td>TIMER3_REMAP</td><td>TIMER3重映射该位由软件置位和清除。0: 关闭重映射功能(TIMER3_CH0/PB6, TIMER3_CH1/PB7, TIMER3_CH2/PB8,TIMER3_CH3/PB9)1: 完全开启重映射功能(TIMER3_CH0/PD12, TIMER3_CH1/PD13,TIMER3_CH2/PD14, TIMER3_CH3/PD15)</td></tr><tr><td>11:10</td><td>TIMER2_REMAP[1:0]</td><td>TIMER2 重映射这些位由软件置位和清除。00: 关闭重映射功能(TIMER2_CH0/PA6, TIMER2_CH1/PA7, TIMER2_CH2/PB0,TIMER2_CH3/PB1)01: 没有使用10: 开启重映射部分功能(TIMER2_CH0/PB4, TIMER2_CH1/PB5,TIMER2_CH2/PB0, TIMER2_CH3/PB1)11: 完全开启重映射功能(TIMER2_CH0/PC6, TIMER2_CH1/PC7,TIMER2_CH2/PC8, TIMER2_CH3/PC9)</td></tr><tr><td>9:8</td><td>TIMER1_REMAP[1:0]</td><td>TIMER1 重映射这些位由软件置位和清除。00: 关闭重映射功能(TIMER1_CH0-TIMER1_ETI/PA0, TIMER1_CH1/PA1,TIMER1_CH2/PA2, TIMER1_CH3/PA3)01: 开启重映射部分功能 0(TIMER1_CH0-TIMER1_ETI/PA15, TIMER1_CH1/PB3,TIMER1_CH2/PA2, TIMER1_CH3/PA3)10: 开启重映射部分功能 1(TIMER1_CH0-TIMER1_ETI/PA0, TIMER1_CH1/PA1,TIMER1_CH2/PB10, TIMER1_CH3/PB11)11: 完全开启重映射功能(TIMER1_CH0-TIMER1_ETI/PA15, TIMER1_CH1/PB3,TIMER1_CH2/PB10, TIMER1_CH3/PB11)</td></tr><tr><td>7:6</td><td>TIMER0_REMAP[1:0]</td><td>TIMER0 重映射这些位由软件置位和清除。00: 关闭重映射功能(TIMER0_ETI/PA12, TIMER0_CH0/ PA8, TIMER0_CH1/PA9,TIMER0_CH2/PA10, TIMER0_CH3/PA11, TIMER0_BRKIN/PB12,TIMER0_CH0_ON/PB13, TIMER0_CH1_ON/PB14, TIMER0_CH2_ON/PB15)01: 开启重映射部分功能 (TIMER0_ETI/PA12, TIMER0_CH0/ PA8,TIMER0_CH1/PA9, TIMER0_CH2/PA10, TIMER0_CH2/PA10, TIMER0_CH3/PA11,TIMER0_BRKIN/PA6, TIMER0_CH0_ON/PA7, TIMER0_CH1_ON/PB0,TIMER0_CH2_ON/PB1)10: 没有使用11: 完全开启重映射功能 (TIMER0_ETI/PE7, TIMER0_CH0/ PE9,TIMER0_CH1/PE11, TIMER0_CH2/PE13, TIMER0_CH3/PE14,TIMER0_BRKIN/PE15, TIMER0_CH0_ON/PE8, TIMER0_CH1_ON/PE10,TIMER0_CH2_ON/PE12)</td></tr><tr><td>5:4</td><td>USART2_REMAP[1:0]</td><td>USART2 重映射这些位由软件置位和清除。00: 关闭重映射功能 (USART2_TX/PB10, USART2_RX /PB11,USART2_CK/PB12, USART2_CTS/PB13, USART2_RTS/PB14)01: 开启重映射部分功能 (USART2_TX/PC10, USART2_RX /PC11,USART2_CK/PC12, USART2_CTS/PB13, USART2_RTS/PB14)10:没有使用11:完全开启重映射功能(USART2_TX/PD8, USART2_RX/PD9, USART2_CK/PD10, USART2_CTS/PD11, USART2_RTS/PD12)</td></tr><tr><td>3</td><td>USART1_REMAP</td><td>USART1 重映射该位由软件置位和清除。0:关闭重映射功能(USART1_CTS/PA0, USART1_RTS/PA1, USART1_TX/PA2, USART1_RX /PA3, USART1_CK/PA4)1:开启重映射功能(USART1_CTS/PD3, USART1_RTS/PD4, USART1_TX/PD5, USART1_RX /PD6, USART1_CK/PD7)</td></tr><tr><td>2</td><td>USART0_REMAP</td><td>USART0 重映射该位由软件置位和清除。0:关闭重映射功能(USART0_TX/PA9, USART0_RX /PA10)1:开启重映射功能(USART0_TX/PB6, USART0_RX /PB7)</td></tr><tr><td>1</td><td>I2C0_REMAP</td><td>I2C0 重映射该位由软件置位和清除。0:关闭重映射功能(I2C0_SCL/PB6, I2C0_SDA /PB7)1:开启重映射功能(I2C0_SCL/PB8, I2C0_SDA /PB9)</td></tr><tr><td>0</td><td>SPI0_REMAP</td><td>SPI0 重映射该位由软件置位和清除。0:关闭重映射功能(SPI0_NSS/PA4, SPI0_SCK /PA5, SPI0_MISO /PA6, SPI0_MOSI /PA7, SPI0_IO2 /PA2, SPI0_IO3 /PA3)1:开启重映射功能(SPI0_NSS/PA15, SPI0_SCK /PB3, SPI0_MISO /PB4, SPI0_MOSI /PB5, SPI0_IO2 /PB6, SPI0_IO3 /PB7)</td></tr></table>

## 8.5.11. EXTI 源选择寄存器 0 寄存器(AFIO_EXTISS0)

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI3_SS [3:0]</td><td colspan="4">EXTI2_SS [3:0]</td><td colspan="4">EXTI1_SS [3:0]</td><td colspan="4">EXTI0_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI3_SS[3:0]</td><td>EXTI 3 源选择0000: PA3 引脚</td></tr></table>

<table><tr><td></td><td></td><td>0001: PB3 引脚</td></tr><tr><td></td><td></td><td>0010: PC3 引脚</td></tr><tr><td></td><td></td><td>0011: PD3 引脚</td></tr><tr><td></td><td></td><td>0100: PE3 引脚</td></tr><tr><td></td><td></td><td>0101: PF3 引脚</td></tr><tr><td></td><td></td><td>0110: PG3 引脚</td></tr><tr><td></td><td></td><td>其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI2_SS[3:0]</td><td>EXTI 2 源选择</td></tr><tr><td></td><td></td><td>0000: PA2 引脚</td></tr><tr><td></td><td></td><td>0001: PB2 引脚</td></tr><tr><td></td><td></td><td>0010: PC2 引脚</td></tr><tr><td></td><td></td><td>0011: PD2 引脚</td></tr><tr><td></td><td></td><td>0100: PE2 引脚</td></tr><tr><td></td><td></td><td>0101: PF2 引脚</td></tr><tr><td></td><td></td><td>0110: PG2 引脚</td></tr><tr><td></td><td></td><td>其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI1_SS[3:0]</td><td>EXTI 1 源选择</td></tr><tr><td></td><td></td><td>0000: PA1 引脚</td></tr><tr><td></td><td></td><td>0001: PB1 引脚</td></tr><tr><td></td><td></td><td>0010: PC1 引脚</td></tr><tr><td></td><td></td><td>0011: PD1 引脚</td></tr><tr><td></td><td></td><td>0100: PE1 引脚</td></tr><tr><td></td><td></td><td>0101: PF1 引脚</td></tr><tr><td></td><td></td><td>0110: PG1 引脚</td></tr><tr><td></td><td></td><td>其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI0_SS[3:0]</td><td>EXTI 0 源选择</td></tr><tr><td></td><td></td><td>0000: PA0 引脚</td></tr><tr><td></td><td></td><td>0001: PB0 引脚</td></tr><tr><td></td><td></td><td>0010: PC0 引脚</td></tr><tr><td></td><td></td><td>0011: PD0 引脚</td></tr><tr><td></td><td></td><td>0100: PE0 引脚</td></tr><tr><td></td><td></td><td>0101: PF0 引脚</td></tr><tr><td></td><td></td><td>0110: PG0 引脚</td></tr><tr><td></td><td></td><td>其他配置保留。</td></tr></table>

## 8.5.12. EXTI 源选择寄存器 1 寄存器(AFIO_EXTISS1)

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI7_SS [3:0]</td><td colspan="4">EXTI6_SS [3:0]</td><td colspan="4">EXTI5_SS [3:0]</td><td colspan="4">EXTI4_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI7_SS[3:0]</td><td>EXTI 7 源选择0000: PA7 引脚0001: PB7 引脚0010: PC7 引脚0011: PD7 引脚0100: PE7 引脚0101: PF7 引脚0110: PG7 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI6_SS[3:0]</td><td>EXTI 6 源选择0000: PA6 引脚0001: PB6 引脚0010: PC6 引脚0011: PD6 引脚0100: PE6 引脚0101: PF6 引脚0110: PG6 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI5_SS[3:0]</td><td>EXTI 5 源选择0000: PA5 引脚0001: PB5 引脚0010: PC5 引脚0011: PD5 引脚0100: PE5 引脚0101: PF5 引脚0110: PG5 引脚其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI4_SS[3:0]</td><td>EXTI 4 源选择0000: PA4 引脚0001: PB4 引脚0010: PC4 引脚0011: PD4 引脚0100: PE4 引脚0101: PF4 引脚0110: PG4 引脚</td></tr></table>

其他配置保留。

## 8.5.13. EXTI 源选择寄存器 2 寄存器(AFIO_EXTISS2)

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI11_SS [3:0]</td><td colspan="4">EXTI10_SS [3:0]</td><td colspan="4">EXTI9_SS [3:0]</td><td colspan="4">EXTI8_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI11_SS[3:0]</td><td>EXTI 11 源选择0000: PA11 引脚0001: PB11 引脚0010: PC11 引脚0011: PD11 引脚0100: PE11 引脚0101: PF11 引脚0110: PG11 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI10_SS[3:0]</td><td>EXTI 10 源选择0000: PA10 引脚0001: PB10 引脚0010: PC10 引脚0011: PD10 引脚0100: PE10 引脚0101: PF10 引脚0110: PG10 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI9_SS[3:0]</td><td>EXTI 9 源选择0000: PA9 引脚0001: PB9 引脚0010: PC9 引脚0011: PD9 引脚0100: PE9 引脚0101: PF9 引脚0110: PG9 引脚</td></tr></table>

<table><tr><td></td><td></td><td>其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI8_SS[3:0]</td><td>EXTI 8 源选择0000: PA8 引脚0001: PB8 引脚0010: PC8 引脚0011: PD8 引脚0100: PE8 引脚0101: PF8 引脚0110: PG8 引脚其他配置保留。</td></tr></table>

## 8.5.14. EXTI 源选择寄存器 3 寄存器(AFIO_EXTISS3)

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI15_SS [3:0]</td><td colspan="4">EXTI14_SS [3:0]</td><td colspan="4">EXTI13_SS [3:0]</td><td colspan="4">EXTI12_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI15_SS[3:0]</td><td>EXTI 15 源选择0000: PA15 引脚0001: PB15 引脚0010: PC15 引脚0011: PD15 引脚0100: PE15 引脚0101: PF15 引脚0110: PG15 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI14_SS[3:0]</td><td>EXTI 14 源选择0000: PA14 引脚0001: PB14 引脚0010: PC14 引脚0011: PD14 引脚0100: PE14 引脚0101: PF14 引脚0110: PG14 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI13_SS[3:0]</td><td>EXTI 13 源选择0000: PA13 引脚0001: PB13 引脚0010: PC13 引脚0011: PD13 引脚0100: PE13 引脚0101: PF13 引脚0110: PG13 引脚其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI12_SS[3:0]</td><td>EXTI 12 源选择0000: PA12 引脚0001: PB12 引脚0010: PC12 引脚0011: PD12 引脚0100: PE12 引脚0101: PF12 引脚0110: PG12 引脚其他配置保留。</td></tr></table>

## 8.5.15. AFIO 端口配置寄存器 1(AFIO_PCF1)

地址偏移：0x1C

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="11">保留</td><td colspan="2">TIMER16_REMAP</td><td colspan="2">TIMER15_REMAP</td><td>TIMER14_REMAP</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4.</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="3">保留</td><td colspan="2">CTC_REMAP[1:0]</td><td>EXMC_NADV</td><td>TIMER13_REMAP</td><td>TIMER12_REMAP</td><td>TIMER10_REMAP</td><td>TIMER9_REMAP</td><td>TIMER8_REMAP</td><td colspan="5">保留</td></tr><tr><td></td><td></td><td></td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20:19</td><td>TIMER16_REMAP[1: 0]</td><td>TIMER16 重映射这些位由软件置位和清除。00: 关闭重映射功能(TIMER16_CH0/PA7, TIMER16_BRKIN /PA10)01: 开启重映射部分功能(TIMER16_CH0/PB5, TIMER16_BRKIN /PB4)10: 没有使用11: 完全开启重映射功能(TIMER16_CH0/PB9, TIMER16_BRKIN /PB4)</td></tr><tr><td>18:17</td><td>TIMER15_REMAP[1: 0]</td><td>TIMER15 重映射这些位由软件置位和清除。00: 关闭重映射功能(TIMER15_CH0/PA6, TIMER15_CH0_ON/PA13)01: 开启重映射部分功能 0 (TIMER15_CH0/PA12, TIMER15_CH0_ON/PA13)10: 开启重映射部分功能 1 (TIMER15_CH0/PB4, TIMER15_CH0_ON/PB6)11: 完全开启重映射功能(TIMER15_CH0/PB8, TIMER15_CH0_ON/PB6)</td></tr><tr><td>16</td><td>TIMER14_REMAP</td><td>TIMER14 重映射该位由软件置位和清除, 控制着将 TIMER14 备用功能重映射到 GPIO 端口。0: 关闭重映射功能(TIMER14_CH0/PB14, TIMER14_CH1/PB15, TIMER14_CH0_ON/PA1, TIMER14_BRKIN/PA9)1: 开启重映射功能(TIMER14_CH0/PA2, TIMER14_CH1/PA3, TIMER14_CH0_ON/PB15, TIMER14_BRKIN/PC5)</td></tr><tr><td>15:13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:11</td><td>CTC_REMAP[1:0]</td><td>CTC 重映射这些位由软件置位和清除, 控制着将 CTC_SYNC 备用功能重映射到 GPIO 端口。00: 关闭重映射功能(PA8)01: 开启重映射功能 0 (PD15)10/11: 开启重映射功能 1 (PF0)</td></tr><tr><td>10</td><td>EXMC_NADV</td><td>EXMC_NADV 连接/不连接该位由软件置位和清除, 控制着可选的 EXMC_NADV 信号0: NADV 信号连接到输出(默认值)1: NADV 信号没有连接, I/O 引脚可以用于其他外设。</td></tr><tr><td>9</td><td>TIMER13_REMAP</td><td>TIMER13 重映射该位由软件置位和清除, 控制着将 TIMER13_CH0 备用功能重映射到 GPIO 端口。0: 关闭重映射功能(PA7)1: 开启重映射功能(PF9)</td></tr><tr><td>8</td><td>TIMER12_REMAP</td><td>TIMER12 重映射该位由软件置位和清除, 控制着将 TIMER12_CH0 备用功能重映射到 GPIO 端口。0: 关闭重映射功能(PA6)1: 开启重映射功能(PF8)</td></tr><tr><td>7</td><td>TIMER10_REMAP</td><td>TIMER10 重映射该位由软件置位和清除, 控制着将 TIMER10_CH0 备用功能重映射到 GPIO 端口。0: 关闭重映射功能(PB9)1: 开启重映射功能(PF7)</td></tr><tr><td>6</td><td>TIMER9_REMAP</td><td>TIMER9 重映射该位由软件置位和清除, 控制着将 TIMER9_CH0 备用功能重映射到 GPIO 端口。0: 关闭重映射功能(PB8)1: 开启重映射功能(PF6)</td></tr><tr><td>5</td><td>TIMER8_REMAP</td><td>TIMER8 重映射该位由软件置位和清除,控制着将 TIMER8_CH0 和 TIMER8_CH1 备用功能重映射到 GPIO 端口。0:关闭重映射功能(TIMER8_CH0 连接到 PA2 和 TIMER8_CH1 连接到 PA3)1:开启重映射功能(TIMER8_CH0 重映射到 PE5 和 TIMER8_CH1 重映射到 PE6)</td></tr><tr><td>4:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 8.5.16. IO 补偿控制寄存器(AFIO_CPSCTL)

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>CPS_RDY</td><td colspan="7">保留</td><td>CPS_EN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>CPS_RDY</td><td>I/O 补偿单元是否准备好,该位只读。0:I/O 补偿单元没有准备好1:I/O 补偿单元准备好</td></tr><tr><td>7:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>CPS_EN</td><td>I/O 补偿单元使能当端口输出速度大于 50MHz 时,需要使能 I/O 补偿单元。0:I/O 补偿单元掉电1:I/O 补偿单元使能</td></tr></table>

## 8.5.17. AFIO 端口配置寄存器 A (AFIO_PCFA)

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>PA15_AFCFG</td><td>PA10_AFCFG[2]</td><td>PA9_AFCFG[2]</td><td>PA13_AFCFG</td><td colspan="3">PA12_AFCFG [2:0]</td><td colspan="2">PA11_AFCFG [1:0]</td><td colspan="2">PA10_AFCFG [1:0]</td><td colspan="2">PA9_AFCFG[1:0]</td><td colspan="2">PA8_AFCFG [1:0]</td></tr><tr><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="3">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PA7_AFCFG</td><td>PA6_AFCFG</td><td colspan="3">保留</td><td>PA5_AFCFG</td><td colspan="2">保留</td><td colspan="2">PA3_AFCFG[1:0]</td><td colspan="2">PA2_AFCFG[1:0]</td><td colspan="2">保留</td><td>PA1_AFCFG</td><td>保留</td></tr><tr><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td><td colspan="2"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2"></td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>PA15_AFCFG</td><td>PA15 AF 功能配置位该位由软件置位和清除。0:不配置 PA15 备用功能到 SHRTIMER1:配置 PA15 备用功能到 SHRTIMER</td></tr><tr><td>29</td><td>PA10_AFCFG[2]</td><td>PA10 AF 功能配置位参考寄存器 AFIO_PCFA 的 20 到 21 位</td></tr><tr><td>28</td><td>PA9_AFCFG[2]</td><td>PA9 AF 功能配置位参考寄存器 AFIO_PCFA 的 18 到 19 位</td></tr><tr><td>27</td><td>PA13_AFCFG</td><td>PA13 AF 功能配置位该位由软件置位和清除。0:不配置 PA13 备用功能到 TIMER151:配置 PA13 备用功能到 TIMER15</td></tr><tr><td>26:24</td><td>PA12_AFCFG[2:0]</td><td>PA12 AF 功能配置位这些位由软件置位和清除。000:不配置 PA12 备用功能到 SHRTIMER/CMP1/USART5/TIMER15001:配置 PA12 备用功能到 CMP1010:配置 PA12 备用功能到 USART5011:配置 PA12 备用功能到 SHRTIMER100:配置 PA12 备用功能到 TIMER15101 - 111:保留</td></tr><tr><td>23:22</td><td>PA11_AFCFG[1:0]</td><td>PA11 AF 功能配置位这些位由软件置位和清除。00:不配置 PA11 备用功能到 SHRTIMER/USART501:配置 PA11 备用功能到 USART510/11:配置 PA11 备用功能到 SHRTIMER</td></tr><tr><td>21:20</td><td>PA10_AFCFG[1:0]</td><td>PA10 AF 功能配置位与寄存器 AFIO_PCFA 的 29 位共同构成功能配置位,由软件置位和清除。000:不配置 PA10 备用功能到 SHRTIMER/CAN2/CMP5/TIMER16001:配置 PA10 备用功能到 CAN2010:配置 PA10 备用功能到 CMP5011:配置 PA10 备用功能到 SHRTIMER100:配置 PA10 备用功能到 TIMER16101 - 111:保留</td></tr></table>


注意：CAN2 只在互联型产品中有效。


<table><tr><td>19:18</td><td>PA9_AFCFG[1:0]</td><td>PA9 AF 功能配置位与寄存器 AFIO_PCFA 的 28 位共同构成功能配置位,由软件置位和清除。000:不配置 PA9 备用功能到 SHRTIMER/CAN2/I2C2/TIMER14001:配置 PA9 备用功能到 CAN2010:配置 PA9 备用功能到 I2C2011:配置 PA9 备用功能到 SHRTIMER100:配置 PA9 备用功能到 TIMER14101 - 111:保留注意:CAN2 只在互联型产品中有效。</td></tr><tr><td>17:16</td><td>PA8_AFCFG[1:0]</td><td>PA8 AF 功能配置位这些位由软件置位和清除。00:不配置 PA8 备用功能到 SHRTIMER/I2C201:配置 PA8 备用功能到 I2C210/11:配置 PA8 备用功能到 SHRTIMER</td></tr><tr><td>15</td><td>PA7_AFCFG</td><td>PA7 AF 功能配置位该位由软件置位和清除。0:不配置 PA7 备用功能到 TIMER161:配置 PA7 备用功能到 TIMER16</td></tr><tr><td>14</td><td>PA6_AFCFG</td><td>PA6 AF 功能配置位该位由软件置位和清除。0:不配置 PA6 备用功能到 TIMER151:配置 PA6 备用功能到 TIMER15</td></tr><tr><td>13:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>PA5_AFCFG</td><td>PA5 AF 功能配置位该位由软件置位和清除。0:不配置 PA5 备用功能到 USBHS1:配置 PA5 备用功能到 USBHS</td></tr><tr><td>9:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:6</td><td>PA3_AFCFG[1:0]</td><td>PA3 AF 功能配置位该位由软件置位和清除。00:不配置 PA3 备用功能到 USBHS/TIMER1401:配置 PA3 备用功能到 USBHS10:配置 PA3 备用功能到 TIMER1411:保留</td></tr><tr><td>5:4</td><td>PA2_AFCFG[1:0]</td><td>PA2 AF 功能配置位该位由软件置位和清除。00:不配置 PA2 备用功能到 CMP1/TIMER1401:配置 PA2 备用功能到 CMP110:配置 PA2 备用功能到 TIMER1411: 保留</td></tr><tr><td>3:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>PA1_AFCFG</td><td>PA1 AF 功能配置位该位由软件置位和清除。0: 不配置 PA1 备用功能到 TIMER141: 配置 PA1 备用功能到 TIMER14</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 8.5.18. AFIO 端口配置寄存器 B (AFIO_PCFB)

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">PB15_AFCFG[1:0]</td><td colspan="2">PB14_AFCFG[1:0]</td><td colspan="2">PB13_AFCFG[1:0]</td><td colspan="2">PB12_AFCFG[1:0]</td><td colspan="2">PB11_AFCFG[1:0]</td><td colspan="2">PB10_AFCFG[1:0]</td><td colspan="2">PB9_AFCFG[1:0]</td><td colspan="2">PB8_AFCFG[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">PB7_AFCFG[1:0]</td><td colspan="2">PB6_AFCFG[1:0]</td><td colspan="2">PB5_AFCFG[2:1]</td><td colspan="3">PB4_AFCFG[2:0]</td><td>PB3_AFCFG</td><td colspan="2">PB2_AFCFG[1:0]</td><td colspan="2">PB1_AFCFG[1:0]</td><td>PB5_AFCFG[0]</td><td>PB0_AFCFG</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>PB15_AFCFG[1:0]</td><td>PB15 AF 功能配置位这些位由软件置位和清除。00: 不配置 PB15 备用功能到 SHRTIMER/TIMER1401: 配置 PB15 备用功能到 SHRTIMER10: 配置 PB15 备用功能到 TIMER14_CH111: 配置 PB15 备用功能到 TIMER14_CH0_ON</td></tr><tr><td>29:28</td><td>PB14_AFCFG[1:0]</td><td>PB14 AF 功能配置位这些位由软件置位和清除。00: 不配置 PB14 备用功能到 SHRTIMER/I2S1/TIMER1401: 配置 PB14 备用功能到 I2S110: 配置 PB14 备用功能到 SHRTIMER11: 配置 PB14 备用功能到 TIMER14_CH0</td></tr><tr><td>27:26</td><td>PB13_AFCFG[1:0]</td><td>PB13 AF 功能配置位这些位由软件置位和清除。00: 不配置 PB13 备用功能到 SHRTIMER/USBHS01/11: 配置 PB13 备用功能到 SHRTIMER10: 配置 PB13 备用功能到 USBHS</td></tr><tr><td>25:24</td><td>PB12_AFCFG[1:0]</td><td>PB12 AF 功能配置位</td></tr></table>

<table><tr><td></td><td></td><td>这些位由软件置位和清除。00:不配置PB12备用功能到SHRTIMER/USBHS01/11:配置B12备用功能到SHRTIMER10:配置PB12备用功能到USBHS</td></tr><tr><td>23:22</td><td>PB11_AFCFG[1:0]</td><td>PB11 AF功能配置位这些位由软件置位和清除。00:不配置PB11备用功能到SHRTIMER/USBHS/CAN201:配置PB11备用功能到CAN210:配置PB11备用功能到USBHS11:配置PB11备用功能到SHRTIMER注意:CAN2只在互联型产品中有效。</td></tr><tr><td>21:20</td><td>PB10_AFCFG[1:0]</td><td>PB10 AF功能配置位这些位由软件置位和清除。00:不配置PB10备用功能到SHRTIMER/USBHS/CAN201:配置PB10备用功能到CAN210:配置PB10备用功能到USBHS11:配置PB10备用功能到SHRTIMER注意:CAN2只在互联型产品中有效。</td></tr><tr><td>19:18</td><td>PB9_AFCFG[1:0]</td><td>PB9 AF功能配置位这些位由软件置位和清除。00:不配置PB9备用功能到SHRTIMER/CMP1/TIMER1601:配置PB9备用功能到CMP110:配置PB9备用功能到SHRTIMER11:配置PB9备用功能到TIMER16</td></tr><tr><td>17:16</td><td>PB8_AFCFG[1:0]</td><td>PB8 AF功能配置位这些位由软件置位和清除。00:不配置PB8备用功能到SHRTIMER/I2C2/TIMER1501:配置PB8备用功能到I2C210:配置B8备用功能到SHRTIMER11:配置B8备用功能到TIMER15</td></tr><tr><td>15:14</td><td>PB7_AFCFG[1:0]</td><td>PB7 AF功能配置位这些位由软件置位和清除。00:不配置PB7备用功能到SHRTIMER/TIMER1601:配置PB7备用功能到SHRTIMER10:配置PB7备用功能到TIMER1611:保留</td></tr><tr><td>13:12</td><td>PB6_AFCFG[1:0]</td><td>PB6 AF功能配置位该位由软件置位和清除。00:不配置PB6备用功能到SHRTIMER/TIMER1501:配置PB6备用功能到SHRTIMER10:配置PB6备用功能到TIMER15</td></tr></table>

<table><tr><td>11:10</td><td>PB5_AFCFG[2:1]</td><td>PB5 AF 功能配置位与寄存器 AFIO_PCFB 的 1 位共同构成功能配置位,由软件置位和清除。000: 不配置 PB5 备用功能到 SHRTIMER/USBHS/I2C2/TIMER15/TIMER16001: 配置 PB5 备用功能到 TIMER15010: 配置 PB5 备用功能到 I2C2011: 配置 PB5 备用功能到 TIMER16100: 配置 PB5 备用功能到 USBHS101: 保留110: 配置 PB5 备用功能到 SHRTIMER111: 保留</td></tr><tr><td>9:7</td><td>PB4_AFCFG[2:0]</td><td>PB4 AF 功能配置位这些位由软件置位和清除。000: 不配置 PB4 备用功能到 SHRTIMER/I2C2/I2S2/TIMER15/TIMER16001: 配置 PB4 备用功能到 TIMER15010: 配置 PB4 备用功能到 I2S2011: 配置 PB4 备用功能到 TIMER16100: 配置 PB4 备用功能到 I2C2101: 保留110: 配置 PB4 备用功能到 SHRTIMER111: 保留</td></tr><tr><td>6</td><td>PB3_AFCFG</td><td>PB3 AF 功能配置位该位由软件置位和清除。0: 不配置 PB3 备用功能到 SHRTIMER1: 配置 PB3 备用功能到 SHRTIMER</td></tr><tr><td>5:4</td><td>PB2_AFCFG[1:0]</td><td>PB2 AF 功能配置位这些位由软件置位和清除。00: 不配置 PB2 备用功能到 SHRTIMER/USBHS10: 配置 PB2 备用功能到 USBHS01/11: 配置 PB2 备用功能到 SHRTIMER</td></tr><tr><td>3:2</td><td>PB1_AFCFG[1:0]</td><td>PB1 AF 功能配置位这些位由软件置位和清除。00: 不配置 PB1 备用功能到 SHRTIMER/USBHS/CMP301: 配置 PB1 备用功能到 CMP310: 配置 PB1 备用功能到 USBHS11: 配置 PB1 备用功能到 SHRTIMER</td></tr><tr><td>1</td><td>PB5_AFCFG[0]</td><td>PB5 AF 功能配置位参考寄存器 AFIO_PCFB 的 10 到 11 位</td></tr><tr><td>0</td><td>PB0_AFCFG</td><td>PB0 AF 功能配置位该位由软件置位和清除。0: 不配置 PB0 备用功能到 USBHS</td></tr></table>

1：配置 PB0 备用功能到 USBHS

## 8.5.19. AFIO 端口配置寄存器 C(AFIO_PCFC)

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>PC12_AFCFG</td><td colspan="2">PC11_AFCFG[1:0]</td><td>保留</td><td>PC10_AFCFG</td><td colspan="2">PC9_AFCFG[1:0]</td><td colspan="2">PC8_AFCFG[1:0]</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">PC7_AFCFG[1:0]</td><td colspan="2">PC6_AFCFG[1:0]</td><td>PC5_AFCFG</td><td colspan="4">保留</td><td>PC3_AFCFG</td><td colspan="2">PC2_AFCFG[1:0]</td><td colspan="3">保留</td><td>PC0_AFCFG</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td colspan="2">rw</td><td colspan="3"></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>PC12_AFCFG</td><td>PC12 AF 功能配置位该位由软件置位和清除。0:不配置 PC12 备用功能到 SHRTIMER1:配置 PC12 备用功能到 SHRTIMER</td></tr><tr><td>23:22</td><td>PC11_AFCFG[1:0]</td><td>PC11 AF 功能配置位这些位由软件置位和清除。00:不配置 PC11 备用功能到 SHRTIMER/I2S201/11:配置 PC11 备用功能到 SHRTIMER10:配置 PC11 备用功能到 I2S2</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PC10_AFCFG</td><td>PC10 AF 功能配置位该位由软件置位和清除。0:不配置 PC10 备用功能到 I2C21:配置 PC10 备用功能到 I2C2</td></tr><tr><td>19:18</td><td>PC9_AFCFG[1:0]</td><td>PC9 AF 功能配置位这些位由软件置位和清除。00:不配置 PC9 备用功能到 SHRTIMER/I2C201/11:配置 PC9 备用功能到 SHRTIMER10:配置 PC9 备用功能到 I2C2</td></tr><tr><td>17:16</td><td>PC8_AFCFG[1:0]</td><td>PC8 AF 功能配置位这些位由软件置位和清除。00:不配置 PC8 备用功能到 SHRTIMER/USART510:配置PC8备用功能到USART501/11:配置PC8备用功能到SHRTIMER</td></tr><tr><td>15:14</td><td>PC7_AFCFG[1:0]</td><td>PC7 AF功能配置位这些位由软件置位和清除。00:不配置PC7备用功能到SHRTIMER/USART501/11:配置PC7备用功能到SHRTIMER10:配置PC7备用功能到USART5</td></tr><tr><td>13:12</td><td>PC6_AFCFG[1:0]</td><td>PC6 AF功能配置位这些位由软件置位和清除。00:不配置PC6备用功能到SHRTIMER/CMP5/USART501:配置PC6备用功能到CMP510:配置PC6备用功能到USART511:配置PC6备用功能到SHRTIMER</td></tr><tr><td>11</td><td>PC5_AFCFG</td><td>PC5 AF功能配置位该位由软件置位和清除。0:不配置PC5备用功能到TIMER141:配置PC5备用功能到TIMER14</td></tr><tr><td>10:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6</td><td>PC3_AFCFG</td><td>PC3 AF功能配置位该位由软件置位和清除。0:不配置PC3备用功能到USBHS1:配置PC3备用功能到USBHS</td></tr><tr><td>5:4</td><td>PC2_AFCFG[1:0]</td><td>PC2 AF功能配置位这些位由软件置位和清除。00:不配置PC2备用功能到USBHS/I2S101/11:配置PC2备用功能到I2S110:配置PC2备用功能到USBHS</td></tr><tr><td>3:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>PC0_AFCFG</td><td>PC0 AF功能配置位该位由软件置位和清除。0:不配置PC0备用功能到USBHS1:配置PC0备用功能到USBHS</td></tr></table>

## 8.5.20. AFIO 端口配置寄存器 D(AFIO_PCFD)

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>PD5_AFCFG</td><td>保留</td><td>PD4_AFCFG</td><td colspan="8">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>PD5_AFCFG</td><td>PD5 AF 功能配置位该位由软件置位和清除。0:不配置 PD5 备用功能到 SHRTIMER1:配置 PD5 备用功能到 SHRTIMER</td></tr><tr><td>9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>PD4_AFCFG</td><td>PD4 AF 功能配置位该位由软件置位和清除。0:不配置 PD4 备用功能到 SHRTIMER1:配置 PD4 备用功能到 SHRTIMER</td></tr><tr><td>7:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 8.5.21. AFIO 端口配置寄存器 E(AFIO_PCFE)

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td>PE13_AFCFG</td><td>保留</td><td>PE12_AFCFG</td><td>保留</td><td>PE11_AFCFG</td><td>保留</td><td>PE10_AFCFG</td><td>保留</td><td>PE9_AFCFG</td><td>保留</td><td>PE8_AFCFG</td></tr><tr><td colspan="5"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="2">PE1_AFCFG[1:0]</td><td colspan="2">PE0_AFCFG[1:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>PE13_AFCFG</td><td>PE13 AF 功能配置位该位由软件置位和清除。0:不配置 PE13 备用功能到 CMP11:配置 PE13 备用功能到 CMP1</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>24</td><td>PE12_AFCFG</td><td>PE12 AF 功能配置位该位由软件置位和清除。0:不配置 PE12 备用功能到 CMP31:配置 PE12 备用功能到 CMP3</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PE11_AFCFG</td><td>PE11 AF 功能配置位该位由软件置位和清除。0:不配置 PE11 备用功能到 CMP51:配置 PE11 备用功能到 CMP5</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PE10_AFCFG</td><td>PE10 AF 功能配置位该位由软件置位和清除。0:不配置 PE10 备用功能到 CMP51:配置 PE10 备用功能到 CMP5</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>PE9_AFCFG</td><td>PE9 AF 功能配置位该位由软件置位和清除。0:不配置 PE9 备用功能到 CMP31:配置 PE9 备用功能到 CMP3</td></tr><tr><td>17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>PE8_AFCFG</td><td>PE8 AF 功能配置位该位由软件置位和清除。0:不配置 PE8 备用功能到 CMP11:配置 PE8 备用功能到 CMP1</td></tr><tr><td>15:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:2</td><td>PE1_AFCFG[1:0]</td><td>PE1 AF 功能配置位这些位由软件置位和清除。00:不配置 PE1 备用功能到 SHRTIMER/CAN201:配置 PE1 备用功能到 CAN210/11:配置 PE1 备用功能到 SHRTIMER注意:CAN2 只在互联型产品中有效。</td></tr><tr><td>1:0</td><td>PE0_AFCFG[1:0]</td><td>PE0 AF 功能配置位这些位由软件置位和清除。00:不配置 PE0 备用功能到 SHRTIMER/CAN201:配置 PE0 备用功能到 CAN210/11:配置 PE0 备用功能到 SHRTIMER注意:CAN2 只在互联型产品中有效。</td></tr></table>

## 8.5.22. AFIO 端口配置寄存器 G (AFIO_PCFG)

地址偏移：0x54

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>PG14_AFCFG</td><td>保留</td><td>PG13_AFCFG</td><td>保留</td><td>PG12_AFCFG</td><td>保留</td><td>PG11_AFCFG</td><td>保留</td><td>PG10_AFCFG</td><td>保留</td><td>PG9_AFCFG</td><td colspan="2">保留</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="3">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">PG7_AFCFG[1:0]</td><td>保留</td><td>PG6_AFCFG</td><td colspan="12">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>PG14_AFCFG</td><td>PG14 AF 功能使能配置位该位由软件置位和清除。0:不配置 PG14 备用功能到 USART51:配置 PG14 备用功能到 USART5</td></tr><tr><td>27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>PG13_AFCFG</td><td>PG13 AF 功能使能配置位该位由软件置位和清除。0:不配置 PG13 备用功能到 SHRTIMER1:配置 PG13 备用功能到 SHRTIMER</td></tr><tr><td>25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>PG12_AFCFG</td><td>PG12 AF 功能使能配置位该位由软件置位和清除。0:不配置 PG12 备用功能到 SHRTIMER1:配置 PG12 备用功能到 SHRTIMER</td></tr><tr><td>23</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>22</td><td>PG11_AFCFG</td><td>PG11 AF 功能使能配置位该位由软件置位和清除。0:不配置 PG11 备用功能到 SHRTIMER1:配置 PG11 备用功能到 SHRTIMER</td></tr><tr><td>21</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>20</td><td>PG10_AFCFG</td><td>PG10 AF 功能使能配置位该位由软件置位和清除。0:不配置 PG10 备用功能到 SHRTIMER</td></tr></table>

<table><tr><td></td><td></td><td>1: 配置 PG10 备用功能到 SHRTIMER</td></tr><tr><td>19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>PG9_AFCFG</td><td>PG9 AF 功能使能配置位该位由软件置位和清除。0: 不配置 PG9 备用功能到 USART51: 配置 PG9 备用功能到 USART5</td></tr><tr><td>17:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:14</td><td>PG7_AFCFG[1:0]</td><td>PG7 AF 功能使能配置位这些位由软件置位和清除。00: 不配置 PG7 备用功能到 SHRTIMER/ USART501: 配置 PG7 备用功能到 USART510/11: 配置 PG7 备用功能到 SHRTIMER</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12</td><td>PG6_AFCFG</td><td>PG6 AF 功能使能配置位该位由软件置位和清除。0: 不配置 PG6 备用功能到 SHRTIMER1: 配置 PG6 备用功能到 SHRTIMER</td></tr><tr><td>11:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
