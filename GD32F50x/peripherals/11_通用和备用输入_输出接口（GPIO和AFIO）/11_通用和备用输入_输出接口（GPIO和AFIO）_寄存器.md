## 11.4. GPIO 寄存器

GPIOA 基地址：0x4001 0800

GPIOB 基地址：0x4001 0C00

GPIOC 基地址：0x4001 1000

GPIOD 基地址：0x4001 1400

GPIOE 基地址：0x4001 1800

AFIO 基地址：0x4001 0000

## 11.4.1. 端口控制寄存器 0（GPIOx_CTL, x=A...E）

地址偏移：0x00

复位值：端口 A 0xABFF FFFF；端口 B 0xFFFF FE8F；其他端口 0xFFFF FFFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CTL15[1:0]</td><td colspan="2">CTL14[1:0]</td><td colspan="2">CTL13[1:0]</td><td colspan="2">CTL12[1:0]</td><td colspan="2">CTL11[1:0]</td><td colspan="2">CTL10[1:0]</td><td colspan="2">CTL9[1:0]</td><td colspan="2">CTL8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CTL7[1:0]</td><td colspan="2">CTL6[1:0]</td><td colspan="2">CTL5[1:0]</td><td colspan="2">CTL4[1:0]</td><td colspan="2">CTL3[1:0]</td><td colspan="2">CTL2[1:0]</td><td colspan="2">CTL1[1:0]</td><td colspan="2">CTL0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CTL15[1:0]</td><td>Pin 15 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述</td></tr><tr><td>29:28</td><td>CTL14[1:0]</td><td>Pin 14 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述</td></tr><tr><td>27:26</td><td>CTL13[1:0]</td><td>Pin 13 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述</td></tr><tr><td>25:24</td><td>CTL12[1:0]</td><td>Pin 12 配置位该位由软件置位和清除。参考 CTL0[1:0]的描述</td></tr><tr><td>23:22</td><td>CTL11[1:0]</td><td>Pin 11 配置位</td></tr></table>

<table><tr><td></td><td></td><td>该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>21:20</td><td>CTL10[1:0]</td><td>Pin 10配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>19:18</td><td>CTL9[1:0]</td><td>Pin 9配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>17:16</td><td>CTL8[1:0]</td><td>Pin 8配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>15:14</td><td>CTL7[1:0]</td><td>Pin 7配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>13:12</td><td>CTL6[1:0]</td><td>Pin 6配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>11:10</td><td>CTL5[1:0]</td><td>Pin 5配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>9:8</td><td>CTL4[1:0]</td><td>Pin 4配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>7:6</td><td>CTL3[1:0]</td><td>Pin 3配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>5:4</td><td>CTL2[1:0]</td><td>Pin 2配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>3:2</td><td>CTL1[1:0]</td><td>Pin 1配置位该位由软件置位和清除。参考CTL0[1:0]的描述</td></tr><tr><td>1:0</td><td>CTL0[1:0]</td><td>Pin 0配置位该位由软件置位和清除。00: GPIO输入模式01: GPIO输出模式</td></tr></table>

10：备用功能描述

11：模拟模式（输入和输出）（复位值）

## 11.4.2. 端口输出模式寄存器（GPIOx_OMODE, x=A…E）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OM15</td><td>OM14</td><td>OM13</td><td>OM12</td><td>OM11</td><td>OM10</td><td>OM9</td><td>OM8</td><td>OM7</td><td>OM6</td><td>OM5</td><td>OM4</td><td>OM3</td><td>OM2</td><td>OM1</td><td>OM0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>OM15</td><td>Pin 15 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>14</td><td>OM14</td><td>Pin 14 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>13</td><td>OM13</td><td>Pin 13 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>12</td><td>OM12</td><td>Pin 12 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>11</td><td>OM11</td><td>Pin 11 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>10</td><td>OM10</td><td>Pin 10 输出模式位该位由软件置位和清除。参考 OMO 的描述</td></tr><tr><td>9</td><td>OM9</td><td>Pin 9 输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>8</td><td>OM8</td><td>Pin 8输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>7</td><td>OM7</td><td>Pin 7输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>6</td><td>OM6</td><td>Pin 6输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>5</td><td>OM5</td><td>Pin 5输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>4</td><td>OM4</td><td>Pin 4输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>3</td><td>OM3</td><td>Pin 3输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>2</td><td>OM2</td><td>Pin 2输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>1</td><td>OM1</td><td>Pin 1输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>0</td><td>OM0</td><td>Pin 0输出模式位该位由软件置位和清除。0:端口输出推挽模式(复位值)1:端口输出开漏模式</td></tr></table>

## 11.4.3. 端口输出速度寄存器（GPIOx_OSPD, x=A…E）

地址偏移：0x08

复位值：端口 A 0x0C00 0000；端口 B 0x0000 00C0；其他端口 0x0000 0000。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td>OSPD15[1:0]</td><td>OSPD14[1:0]</td><td>OSPD13[1:0]</td><td>OSPD12[1:0]</td><td>OSPD11[1:0]</td><td>OSPD10[1:0]</td><td>OSPD9[1:0]</td><td>OSPD8[1:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15 14</td><td>13 12</td><td>11 10</td><td>9 8</td><td>7 6</td><td>5 4</td><td>3 2</td><td>1 0</td></tr><tr><td>OSPD7[1:0]</td><td>OSPD6[1:0]</td><td>OSPD5[1:0]</td><td>OSPD4[1:0]</td><td>OSPD3[1:0]</td><td>OSPD2[1:0]</td><td>OSPD1[1:0]</td><td>OSPD0[1:0]</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>OSPD15[1:0]</td><td>Pin 15 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>29:28</td><td>OSPD14[1:0]</td><td>Pin 14 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>27:26</td><td>OSPD13[1:0]</td><td>Pin 13 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>25:24</td><td>OSPD12[1:0]</td><td>Pin 12 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>23:22</td><td>OSPD11[1:0]</td><td>Pin 11 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>21:20</td><td>OSPD10[1:0]</td><td>Pin 10 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>19:18</td><td>OSPD9[1:0]</td><td>Pin 9 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>17:16</td><td>OSPD8[1:0]</td><td>Pin 8 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>15:14</td><td>OSPD7[1:0]</td><td>Pin 7 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>13:12</td><td>OSPD6[1:0]</td><td>Pin 6 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>11:10</td><td>OSPD5[1:0]</td><td>Pin 5 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>9:8</td><td>OSPD4[1:0]</td><td>Pin 4 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>7:6</td><td>OSPD3[1:0]</td><td>Pin 3 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>5:4</td><td>OSPD2[1:0]</td><td>Pin 2 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>3:2</td><td>OSPD1[1:0]</td><td>Pin 1 输出最大速度位该位由软件置位和清除。参考 OSPD0[1:0]的描述</td></tr><tr><td>1:0</td><td>OSPD0[1:0]</td><td>Pin 0 输出最大速度位该位由软件置位和清除。00:输出速度等级 0(复位值)01:输出速度等级 110:输出速度等级 211:输出速度等级 3</td></tr></table>

## 11.4.4. 端口上拉/下拉寄存器（GPIOx_PUD, x=A…E）

地址偏移：0x0C

复位值：端口 A 0x6400 0000；端口 B 0x0000 0100；其他端口 0x0000 0000。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">PUD15[1:0]</td><td colspan="2">PUD14[1:0]</td><td colspan="2">PUD13[1:0]</td><td colspan="2">PUD12[1:0]</td><td colspan="2">PUD11[1:0]</td><td colspan="2">PUD10[1:0]</td><td colspan="2">PUD9[1:0]</td><td colspan="2">PUD8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">PUD7[1:0]</td><td colspan="2">PUD6[1:0]</td><td colspan="2">PUD5[1:0]</td><td colspan="2">PUD4[1:0]</td><td colspan="2">PUD3[1:0]</td><td colspan="2">PUD2[1:0]</td><td colspan="2">PUD1[1:0]</td><td colspan="2">PUD0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>PUD15[1:0]</td><td>Pin 15 上拉/下拉位</td></tr></table>

<table><tr><td></td><td></td><td>该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>29:28</td><td>PUD14[1:0]</td><td>Pin 14 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>27:26</td><td>PUD13[1:0]</td><td>Pin 13 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>25:24</td><td>PUD12[1:0]</td><td>Pin 12 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>23:22</td><td>PUD11[1:0]</td><td>Pin 11 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>21:20</td><td>PUD10[1:0]</td><td>Pin 10 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>19:18</td><td>PUD9[1:0]</td><td>Pin 9 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>17:16</td><td>PUD8[1:0]</td><td>Pin 8 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>15:14</td><td>PUD7[1:0]</td><td>Pin 7 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>13:12</td><td>PUD6[1:0]</td><td>Pin 6 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>11:10</td><td>PUD5[1:0]</td><td>Pin 5 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>9:8</td><td>PUD4[1:0]</td><td>Pin 4 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr></table>

<table><tr><td>7:6</td><td>PUD3[1:0]</td><td>Pin 3 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>5:4</td><td>PUD2[1:0]</td><td>Pin 2 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>3:2</td><td>PUD1[1:0]</td><td>Pin 1 上拉/下拉位该位由软件置位和清除。参考 PUD0[1:0]的描述</td></tr><tr><td>1:0</td><td>PUD0[1:0]</td><td>Pin 0 上拉/下拉位该位由软件置位和清除。00:浮空模式,无上拉/下拉(复位值)01:端口上拉模式10:端口下拉模式11:保留</td></tr></table>

## 11.4.5. 端口输入状态寄存器（GPIOx_ISTAT, x=A...E）

地址偏移：0x10

复位值：0x0000 XXXX

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>ISTAT15</td><td>ISTAT14</td><td>ISTAT13</td><td>ISTAT12</td><td>ISTAT11</td><td>ISTAT10</td><td>ISTAT 9</td><td>ISTAT 8</td><td>ISTAT 7</td><td>ISTAT 6</td><td>ISTAT 5</td><td>ISTAT 4</td><td>ISTAT 3</td><td>ISTAT 2</td><td>ISTAT 1</td><td>ISTAT 0</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>ISTATy</td><td>端口输入状态位(<eq>y=0..15</eq>)这些位由硬件置位和清除。0:引脚输入信号为低电平1:引脚输入信号为高电平</td></tr></table>

## 11.4.6. 端口输出控制寄存器（GPIOx_OCTL, x=A...E）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OCTL15</td><td>OCTL14</td><td>OCTL13</td><td>OCTL12</td><td>OCTL11</td><td>OCTL10</td><td>OCTL9</td><td>OCTL8</td><td>OCTL7</td><td>OCTL6</td><td>OCTL5</td><td>OCTL4</td><td>OCTL3</td><td>OCTL2</td><td>OCTL1</td><td>OCTL0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>OCTLy</td><td>端口输出控制位(y=0..15)这些位由软件置位和清除。0:引脚输出低电平1:引脚输出高电平</td></tr></table>

## 11.4.7. 端口位操作寄存器（GPIOx_BOP, x=A...E）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BOP15</td><td>BOP14</td><td>BOP13</td><td>BOP12</td><td>BOP11</td><td>BOP10</td><td>BOP9</td><td>BOP8</td><td>BOP7</td><td>BOP6</td><td>BOP5</td><td>BOP4</td><td>BOP3</td><td>BOP2</td><td>BOP1</td><td>BOP0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31:16</td><td colspan="4">CRy</td><td colspan="11">端口清除位 y (y=0..15)这些位由软件置位和清除。0:相应的OCTLy位没有改变1:清除相应的OCTLy位为0</td></tr><tr><td>15:0</td><td colspan="4">BOPy</td><td colspan="11">端口置位位 y (y=0..15)这些位由软件置位和清除。0:相应的OCTLy位没有改变1:设置相应的OCTLy位为1</td></tr></table>

## 11.4.8. 端口配置锁定寄存器 （GPIOx_LOCK, x=A...E）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>LKK</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>LK15</td><td>LK14</td><td>LK13</td><td>LK12</td><td>LK11</td><td>LK10</td><td>LK9</td><td>LK8</td><td>LK7</td><td>LK6</td><td>LK5</td><td>LK4</td><td>LK3</td><td>LK2</td><td>LK1</td><td>LK0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>LKK</td><td>锁定序列键该位只能通过使用Lock Key写序列设置,始终可读。0: GPIO_LOCK寄存器和端口配置没有锁定1: 直到下一次MCU复位前,GPIO_LOCK寄存器被锁定LOCK Key写序列:写1→写0→写1→读0→读1注意:在LOCK Key写序列期间,LK[15:0]的值必须保持。</td></tr><tr><td>15:0</td><td>LKy</td><td>端口锁定位y(y=0..15)这些位由软件置位和清除。0: 相应的端口位配置没有锁定1: 当LKK位置1时,相应的端口位配置被锁定</td></tr></table>

## 11.4.9. 备用功能选择寄存器 0（GPIOx_AFSEL0, x=A…E）

地址偏移：0x20

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">SEL7[3:0]</td><td colspan="4">SEL6[3:0]</td><td colspan="4">SEL5[3:0]</td><td colspan="4">SEL4[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">SEL3[3:0]</td><td colspan="4">SEL2[3:0]</td><td colspan="4">SEL1[3:0]</td><td colspan="4">SEL0[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>31:28</td><td>SEL7[3:0]</td><td>Pin 7 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>27:24</td><td>SEL6[3:0]</td><td>Pin 6 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>23:20</td><td>SEL5[3:0]</td><td>Pin 5 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>19:16</td><td>SEL4[3:0]</td><td>Pin 4 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>15:12</td><td>SEL3[3:0]</td><td>Pin 3 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>11:8</td><td>SEL2[3:0]</td><td>Pin 2 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>7:4</td><td>SEL1[3:0]</td><td>Pin 1 备用功能选择该位由软件置位和清除。参考 SEL0 [3:0]的描述</td></tr><tr><td>3:0</td><td>SEL0[3:0]</td><td>Pin 0 备用功能选择该位由软件置位和清除。0000:选择 AF0 功能(复位值)0001:选择 AF1 功能0010:选择 AF2 功能0011:选择 AF3 功能0100:选择 AF4 功能0101:选择 AF5 功能0110:选择 AF6 功能0111:选择 AF7 功能1000:选择 AF8 功能...1001~1111:保留</td></tr></table>

## 11.4.10. 备用功能选择寄存器 1（GPIOx_AFSEL1, x=A…E）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">SEL15[3:0]</td><td colspan="4">SEL14[3:0]</td><td colspan="4">SEL13[3:0]</td><td colspan="4">SEL12[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">SEL11[3:0]</td><td colspan="4">SEL10[3:0]</td><td colspan="4">SEL9[3:0]</td><td colspan="4">SEL8[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>SEL15[3:0]</td><td>Pin 15 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>27:24</td><td>SEL14[3:0]</td><td>Pin 14 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>23:20</td><td>SEL13[3:0]</td><td>Pin 13 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>19:16</td><td>SEL12[3:0]</td><td>Pin 12 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>15:12</td><td>SEL11[3:0]</td><td>Pin 11 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>11:8</td><td>SEL10[3:0]</td><td>Pin 10 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>7:4</td><td>SEL9[3:0]</td><td>Pin 9 备用功能选择该位由软件置位和清除。参考 SEL8[3:0]的描述</td></tr><tr><td>3:0</td><td>SEL8[3:0]</td><td>Pin 8 备用功能选择该位由软件置位和清除。0000: 选择 AF0 功能(复位值)</td></tr></table>

0001：选择 AF1 功能0010：选择 AF2 功能0011：选择 AF3 功能0100：选择 AF4 功能0101：选择 AF5 功能0110：选择 AF6 功能0111：选择 AF7 功能1000：选择 AF8 功能…1001~1111：保留

## 11.4.11. 位清除寄存器（GPIOx_BC, x=A…E）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>位/位域</td><td colspan="3">名称</td><td colspan="12">描述</td></tr><tr><td>31:16</td><td colspan="3">保留</td><td colspan="12">必须保持复位值。</td></tr><tr><td>15:0</td><td colspan="3">CRy</td><td colspan="12">端口清除位 y (y=0..15)这些位由软件置位和清除。0:相应OCTLy位没有改变1:清除相应的OCTLy位</td></tr></table>

## 11.4.12. EXTI 源选择寄存器 0 寄存器（AFIO_EXTISS0）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td colspan="2">EXTI3_SS[3:0]</td><td>EXTI2_SS[3:0]</td><td>EXTI1_SS[3:0]</td><td>EXTI0_SS[3:0]</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>位/位域</td><td>名称</td><td>描述</td><td></td><td></td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td><td></td><td></td></tr><tr><td>15:12</td><td>EXTI3_SS[3:0]</td><td>EXTI 3 源选择0000: PA3 引脚0001: PB3 引脚0010: PC3 引脚0011: PD3 引脚0100: PE3 引脚其他配置保留。</td><td></td><td></td></tr><tr><td>11:8</td><td>EXTI2_SS[3:0]</td><td>EXTI 2 源选择0000: PA2 引脚0001: PB2 引脚0010: PC2 引脚0011: PD2 引脚0100: PE2 引脚其他配置保留。</td><td></td><td></td></tr><tr><td>7:4</td><td>EXTI1_SS[3:0]</td><td>EXTI 1 源选择0000: PA1 引脚0001: PB1 引脚0010: PC1 引脚0011: PD1 引脚0100: PE1 引脚其他配置保留。</td><td></td><td></td></tr><tr><td>3:0</td><td>EXTI0_SS[3:0]</td><td>EXTI 0 源选择0000: PA0 引脚0001: PB0 引脚0010: PC0 引脚0011: PD0 引脚0100: PE0 引脚其他配置保留。</td><td></td><td></td></tr></table>

## 11.4.13. EXTI 源选择寄存器 1 寄存器（AFIO_EXTISS1）

地址偏移：0x0C

复位值：0x0000 0000


该寄存器只能按字（32 位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI7_SS [3:0]</td><td colspan="4">EXTI6_SS [3:0]</td><td colspan="4">EXTI5_SS [3:0]</td><td colspan="4">EXTI4_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI7_SS[3:0]</td><td>EXTI 7 源选择0000: PA7 引脚0001: PB7 引脚0010: PC7 引脚0011: PD7 引脚0100: PE7 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI6_SS[3:0]</td><td>EXTI 6 源选择0000: PA6 引脚0001: PB6 引脚0010: PC6 引脚0011: PD6 引脚0100: PE6 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI5_SS[3:0]</td><td>EXTI 5 源选择0000: PA5 引脚0001: PB5 引脚0010: PC5 引脚0011: PD5 引脚0100: PE5 引脚其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI4_SS[3:0]</td><td>EXTI 4 源选择0000: PA4 引脚0001: PB4 引脚0010: PC4 引脚0011: PD4 引脚0100: PE4 引脚其他配置保留。</td></tr></table>

## 11.4.14. EXTI 源选择寄存器 2 寄存器（AFIO_EXTISS2）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI11_SS [3:0]</td><td colspan="4">EXTI10_SS [3:0]</td><td colspan="4">EXTI9_SS [3:0]</td><td colspan="4">EXTI8_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI11_SS[3:0]</td><td>EXTI 11 源选择0000: PA11 引脚0001: PB11 引脚0010: PC11 引脚0011: PD11 引脚0100: PE11 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI10_SS[3:0]</td><td>EXTI 10 源选择0000: PA10 引脚0001: PB10 引脚0010: PC10 引脚0011: PD10 引脚0100: PE10 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI9_SS[3:0]</td><td>EXTI 9 源选择0000: PA9 引脚0001: PB9 引脚0010: PC9 引脚0011: PD9 引脚0100: PE9 引脚其他配置保留。</td></tr><tr><td>3:0</td><td>EXTI8_SS[3:0]</td><td>EXTI 8 源选择0000: PA8 引脚0001: PB8 引脚</td></tr></table>

0010：PC8 引脚0011：PD8 引脚0100：PE8 引脚其他配置保留。

## 11.4.15. EXTI 源选择寄存器 3 寄存器（AFIO_EXTISS3）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">EXTI15_SS [3:0]</td><td colspan="4">EXTI14_SS [3:0]</td><td colspan="4">EXTI13_SS [3:0]</td><td colspan="4">EXTI12_SS [3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:12</td><td>EXTI15_SS[3:0]</td><td>EXTI 15 源选择0000: PA15 引脚0001: PB15 引脚0010: PC15 引脚0011: PD15 引脚0100: PE15 引脚其他配置保留。</td></tr><tr><td>11:8</td><td>EXTI14_SS[3:0]</td><td>EXTI 14 源选择0000: PA14 引脚0001: PB14 引脚0010: PC14 引脚0011: PD14 引脚0100: PE14 引脚其他配置保留。</td></tr><tr><td>7:4</td><td>EXTI13_SS[3:0]</td><td>EXTI 13 源选择0000: PA13 引脚0001: PB13 引脚0010: PC13 引脚0011: PD13 引脚0100: PE13 引脚</td></tr></table>

其他配置保留。

3:0 

EXTI12_SS[3:0] 

EXTI 12 源选择

0000：PA12 引脚

0001：PB12 引脚

0010：PC12 引脚

0011：PD12 引脚

0100：PE12 引脚

其他配置保留。
