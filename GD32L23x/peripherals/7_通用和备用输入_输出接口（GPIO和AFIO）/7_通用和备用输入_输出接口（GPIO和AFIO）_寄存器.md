## 7.4. GPIO 寄存器

GPIOA基地址：0x4800 0000

GPIOB基地址：0x4800 0400

GPIOC基地址：0x4800 0800

GPIOD基地址：0x4800 0C00

GPIOF基地址：0x4800 1400

## 7.4.1. 端口控制寄存器（GPIOx_CTL，x=A..D，F）

地址偏移：0x00

复位值：端口 A 0x2800 0000；其他端口 0x0000 0000。

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">CTL15[1:0]</td><td colspan="2">CTL14[1:0]</td><td colspan="2">CTL13[1:0]</td><td colspan="2">CTL12[1:0]</td><td colspan="2">CTL11[1:0]</td><td colspan="2">CTL10[1:0]</td><td colspan="2">CTL9[1:0]</td><td colspan="2">CTL8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">CTL7[1:0]</td><td colspan="2">CTL6[1:0]</td><td colspan="2">CTL5[1:0]</td><td colspan="2">CTL4[1:0]</td><td colspan="2">CTL3[1:0]</td><td colspan="2">CTL2[1:0]</td><td colspan="2">CTL1[1:0]</td><td colspan="2">CTL0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>CTL15[1:0]</td><td>Pin 15配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>29:28</td><td>CTL14[1:0]</td><td>Pin 14配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>27:26</td><td>CTL13[1:0]</td><td>Pin 13配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>25:24</td><td>CTL12[1:0]</td><td>Pin 12配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>23:22</td><td>CTL11[1:0]</td><td>Pin 11配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>21:20</td><td>CTL10[1:0]</td><td>Pin 10配置位该位由软件置位和清除。</td></tr></table>

<table><tr><td></td><td></td><td>参照CTL0[1:0]的描述</td></tr><tr><td>19:18</td><td>CTL9[1:0]</td><td>Pin 9配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>17:16</td><td>CTL8[1:0]</td><td>Pin 8配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>15:14</td><td>CTL7[1:0]</td><td>Pin 7配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>13:12</td><td>CTL6[1:0]</td><td>Pin 6配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>11:10</td><td>CTL5[1:0]</td><td>Pin 5配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>9:8</td><td>CTL4[1:0]</td><td>Pin 4配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>7:6</td><td>CTL3[1:0]</td><td>Pin 3配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>5:4</td><td>CTL2[1:0]</td><td>Pin 2配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>3:2</td><td>CTL1[1:0]</td><td>Pin 1配置位该位由软件置位和清除。参照CTL0[1:0]的描述</td></tr><tr><td>1:0</td><td>CTL0[1:0]</td><td>Pin 0配置位该位由软件置位和清除。00: GPIO输入模式(复位值)01: GPIO输出模式10: 备用功能模式11: 模拟模式(输入和输出)</td></tr></table>

## 7.4.2. 端口输出模式寄存器（GPIOx_OMODE，x=A..D，F）

地址偏移：0x04

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OM15</td><td>OM14</td><td>OM13</td><td>OM12</td><td>OM11</td><td>OM10</td><td>OM9</td><td>OM8</td><td>OM7</td><td>OM6</td><td>OM5</td><td>OM4</td><td>OM3</td><td>OM2</td><td>OM1</td><td>OM0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>OM15</td><td>Pin 15输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>14</td><td>OM14</td><td>Pin 14输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>13</td><td>OM13</td><td>Pin 13输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>12</td><td>OM12</td><td>Pin 12输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>11</td><td>OM11</td><td>Pin 11输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>10</td><td>OM10</td><td>Pin 10输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>9</td><td>OM9</td><td>Pin 9输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>8</td><td>OM8</td><td>Pin 8输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>7</td><td>OM7</td><td>Pin 7输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>6</td><td>OM6</td><td>Pin 6输出模式位该位由软件置位和清除。</td></tr><tr><td></td><td></td><td>参考OM0的描述</td></tr><tr><td>5</td><td>OM5</td><td>Pin 5输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>4</td><td>OM4</td><td>Pin 4输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>3</td><td>OM3</td><td>Pin 3输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>2</td><td>OM2</td><td>Pin 2输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>1</td><td>OM1</td><td>Pin 1输出模式位该位由软件置位和清除。参考OM0的描述</td></tr><tr><td>0</td><td>OM0</td><td>Pin 0输出模式位该位由软件置位和清除。0:输出推挽模式(复位值)1:输出开漏模式</td></tr></table>

## 7.4.3. 端口输出速度寄存器（GPIOx_OSPD，x=A..D，F）

地址偏移：0x08

复位值：端口 A 0x0C00 0000；其他端口 0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">OSPD15[1:0]</td><td colspan="2">OSPD14[1:0]</td><td colspan="2">OSPD13[1:0]</td><td colspan="2">OSPD12[1:0]</td><td colspan="2">OSPD11[1:0]</td><td colspan="2">OSPD10[1:0]</td><td colspan="2">OSPD9[1:0]</td><td colspan="2">OSPD8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">OSPD7[1:0]</td><td colspan="2">OSPD6[1:0]</td><td colspan="2">OSPD5[1:0]</td><td colspan="2">OSPD4[1:0]</td><td colspan="2">OSPD3[1:0]</td><td colspan="2">OSPD2[1:0]</td><td colspan="2">OSPD1[1:0]</td><td colspan="2">OSPD0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>OSPD15[1:0]</td><td>Pin 15输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>29:28</td><td>OSPD14[1:0]</td><td>Pin 14输出最大速度位该位由软件置位和清除。</td></tr></table>

<table><tr><td></td><td></td><td>参考OSPD0[1:0]的描述</td></tr><tr><td>27:26</td><td>OSPD13[1:0]</td><td>Pin 13输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>25:24</td><td>OSPD12[1:0]</td><td>Pin 12输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>23:22</td><td>OSPD11[1:0]</td><td>Pin 11输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>21:20</td><td>OSPD10[1:0]</td><td>Pin 10输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>19:18</td><td>OSPD9[1:0]</td><td>Pin 9输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>17:16</td><td>OSPD8[1:0]</td><td>Pin 8输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>15:14</td><td>OSPD7[1:0]</td><td>Pin 7输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>13:12</td><td>OSPD6[1:0]</td><td>Pin 6输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>11:10</td><td>OSPD5[1:0]</td><td>Pin 5输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>9:8</td><td>OSPD4[1:0]</td><td>Pin 4输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>7:6</td><td>OSPD3[1:0]</td><td>Pin 3输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>5:4</td><td>OSPD2[1:0]</td><td>Pin 2输出最大速度位该位由软件置位和清除。参考OSPD0[1:0]的描述</td></tr><tr><td>3:2</td><td>OSPD1[1:0]</td><td>Pin 1输出最大速度位</td></tr></table>\
该位由软件置位和清除。

参考OSPD0[1:0]的描述

1:0 OSPD0[1:0] Pin 0输出最大速度位

该位由软件置位和清除。

X0：输出最大速度2M（复位值）

01：输出最大速度10M

11：输出最大速度50M

## 7.4.4. 端口上拉/下拉寄存器（GPIOx_PUD，x=A..D，F）

地址偏移：0x0C

复位值：端口 A 0x2400 0000；其他端口 0x0000 0000。

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">PUD15[1:0]</td><td colspan="2">PUD14[1:0]</td><td colspan="2">PUD13[1:0]</td><td colspan="2">PUD12[1:0]</td><td colspan="2">PUD11[1:0]</td><td colspan="2">PUD10[1:0]</td><td colspan="2">PUD9[1:0]</td><td colspan="2">PUD8[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">PUD7[1:0]</td><td colspan="2">PUD6[1:0]</td><td colspan="2">PUD5[1:0]</td><td colspan="2">PUD4[1:0]</td><td colspan="2">PUD3[1:0]</td><td colspan="2">PUD2[1:0]</td><td colspan="2">PUD1[1:0]</td><td colspan="2">PUD0[1:0]</td></tr><tr><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>PUD15[1:0]</td><td>Pin 15上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>29:28</td><td>PUD14[1:0]</td><td>Pin 14上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>27:26</td><td>PUD13[1:0]</td><td>Pin 13上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>25:24</td><td>PUD12[1:0]</td><td>Pin 12上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>23:22</td><td>PUD11[1:0]</td><td>Pin 11上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>21:20</td><td>PUD10[1:0]</td><td>Pin 10上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>19:18</td><td>PUD9[1:0]</td><td>Pin 9上拉或下拉位</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr></table>

<table><tr><td></td><td></td><td>该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>17:16</td><td>PUD8[1:0]</td><td>Pin 8上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>15:14</td><td>PUD7[1:0]</td><td>Pin 7上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>13:12</td><td>PUD6[1:0]</td><td>Pin 6上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>11:10</td><td>PUD5[1:0]</td><td>Pin 5上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>9:8</td><td>PUD4[1:0]</td><td>Pin 4上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>7:6</td><td>PUD3[1:0]</td><td>Pin 3上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>5:4</td><td>PUD2[1:0]</td><td>Pin 2上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>3:2</td><td>PUD1[1:0]</td><td>Pin 1上拉或下拉位该位由软件置位和清除。参照PUD0[1:0]的描述</td></tr><tr><td>1:0</td><td>PUD0[1:0]</td><td>Pin 0上拉或下拉位该位由软件置位和清除。00:悬空模式,无上拉和下拉(复位值)01:端口上拉模式10:端口下拉模式11:保留</td></tr></table>

## 7.4.5. 端口输入状态寄存器（GPIOx_ISTAT，x=A..D，F）

地址偏移：0x10

复位值：0x0000 XXXX

该寄存器只能按字（32位）访问

<table><tr><td>保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>ISTAT15</td><td>ISTAT14</td><td>ISTAT13</td><td>ISTAT12</td><td>ISTAT11</td><td>ISTAT10</td><td>ISTAT9</td><td>ISTAT8</td><td>ISTAT7</td><td>ISTAT6</td><td>ISTAT5</td><td>ISTAT4</td><td>ISTAT3</td><td>ISTAT2</td><td>ISTAT1</td><td>ISTATO</td></tr><tr><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>ISTATy</td><td>端口输入状态位(y=0..15)这些位由软件置位和清除。0:引脚输入信号为低电平1:引脚输入信号为高电平</td></tr></table>

## 7.4.6. 端口输出控制寄存器（GPIOx_OCTL，x=A..D，F）

地址偏移：0x14

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OCTL15</td><td>OCTL14</td><td>OCTL13</td><td>OCTL12</td><td>OCTL11</td><td>OCTL10</td><td>OCTL9</td><td>OCTL8</td><td>OCTL7</td><td>OCTL6</td><td>OCTL5</td><td>OCTL4</td><td>OCTL3</td><td>OCTL2</td><td>OCTL1</td><td>OCTL0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>OCTLy</td><td>端口输出控制位(y=0..15)该位由软件置位和清除。0:引脚输出低电平1:引脚输出高电平</td></tr></table>

## 7.4.7. 端口位操作寄存器（GPIOx_BOP，x=A..D，F）

地址偏移：0x18

复位值：0x0000 0000


该寄存器只能按字（32位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BOP15</td><td>BOP14</td><td>BOP13</td><td>BOP12</td><td>BOP11</td><td>BOP10</td><td>BOP9</td><td>BOP8</td><td>BOP7</td><td>BOP6</td><td>BOP5</td><td>BOP4</td><td>BOP3</td><td>BOP2</td><td>BOP1</td><td>BOP0</td></tr><tr><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>Cry</td><td>端口清除位y(y=0..15)该位由软件置位和清除。0:相应的OCTLy位没有改变1:清除相应的OCTLy位为0</td></tr><tr><td>15:0</td><td>BOPy[15:0]</td><td>端口置位位y(y=0..15)该位由软件置位和清除。0:相应的OCTLy位没有改变1:设置相应的OCTLy位为1</td></tr></table>

## 7.4.8. 端口配置锁定寄存器（GPIOx_LOCK，x=A..D，F）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>LKK</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>LK15</td><td>LK14</td><td>LK13</td><td>LK12</td><td>LK11</td><td>LK10</td><td>LK9</td><td>LK8</td><td>LK7</td><td>LK6</td><td>LK5</td><td>LK4</td><td>LK3</td><td>LK2</td><td>LK1</td><td>LK0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>LKK</td><td>锁定键该位只能通过Lock Key写序列置位,始终可读。0: GPIOx_LOCK寄存器和端口配置没有锁定1: 直到下一次MCU复位前, GPIOx_LOCK寄存器被锁定LOCK key写序列:写1→写0→写1→读0→读1注意: 在LOCK Key写序列期间,LK y (y=0..15)的值必须保持。</td></tr><tr><td>15:0</td><td>Lky</td><td>端口锁定位y (y=0..15)该位由软件置位和清除。0: 端口配置没有锁定1: 端口配置锁定</td></tr></table>

## 7.4.9. 备用功能选择寄存器 0（GPIOx_AFSEL0，x=A..D，F）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">SEL7[3:0]</td><td colspan="4">SEL6[3:0]</td><td colspan="4">SEL5[3:0]</td><td colspan="4">SEL4[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">SEL3[3:0]</td><td colspan="4">SEL2[3:0]</td><td colspan="4">SEL1[3:0]</td><td colspan="4">SEL0[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>SEL7[3:0]</td><td>Pin 7选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>27:24</td><td>SEL6[3:0]</td><td>Pin 6选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>23:20</td><td>SEL5[3:0]</td><td>Pin 5选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>19:16</td><td>SEL4[3:0]</td><td>Pin 4选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>15:12</td><td>SEL3[3:0]</td><td>Pin 3选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>11:8</td><td>SEL2[3:0]</td><td>Pin 2选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>7:4</td><td>SEL1[3:0]</td><td>Pin 1选择备用功能该位由软件置位和清除。参照SEL0 [3:0]的描述</td></tr><tr><td>3:0</td><td>SEL0[3:0]</td><td>Pin 0选择备用功能该位由软件置位和清除。0000:选择AF0功能(复位值)0001:选择AF1功能0010:选择AF2功能0011:选择AF3功能0100:选择AF4功能0101:选择AF5功能0110:选择AF6功能</td></tr></table>

0111：选择AF7功能

1000：选择AF8功能

1001：选择AF9功能

1111：选择AF15功能

## 7.4.10. 备用功能选择寄存器 1（GPIOx_AFSEL1，x=A..D，F）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="4">SEL15[3:0]</td><td colspan="4">SEL14[3:0]</td><td colspan="4">SEL13[3:0]</td><td colspan="4">SEL12[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">SEL11[3:0]</td><td colspan="4">SEL10[3:0]</td><td colspan="4">SEL9[3:0]</td><td colspan="4">SEL8[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:28</td><td>SEL15[3:0]</td><td>Pin 15选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>27:24</td><td>SEL14[3:0]</td><td>Pin 14选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>23:20</td><td>SEL13[3:0]</td><td>Pin 13选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>19:16</td><td>SEL12[3:0]</td><td>Pin 12选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>15:12</td><td>SEL11[3:0]</td><td>Pin 1选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>11:8</td><td>SEL10[3:0]</td><td>Pin 10选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>7:4</td><td>SEL9[3:0]</td><td>Pin 9选择备用功能该位由软件置位和清除。参照SEL8[3:0]的描述</td></tr><tr><td>3:0</td><td>SEL8[3:0]</td><td>Pin 8选择备用功能</td></tr><tr><td></td><td></td><td>该位由软件置位和清除。</td></tr><tr><td></td><td></td><td>0000:选择AF0功能(复位值)</td></tr><tr><td></td><td></td><td>0001:选择AF1功能</td></tr><tr><td></td><td></td><td>0010:选择AF2功能</td></tr><tr><td></td><td></td><td>0011:选择AF3功能</td></tr><tr><td></td><td></td><td>0100:选择AF4功能</td></tr><tr><td></td><td></td><td>0101:选择AF5功能</td></tr><tr><td></td><td></td><td>0110:选择AF6功能</td></tr><tr><td></td><td></td><td>0111:选择AF7功能</td></tr><tr><td></td><td></td><td>1000:选择AF8功能</td></tr><tr><td></td><td></td><td>1001:选择AF9功能</td></tr><tr><td></td><td></td><td>1111:选择AF15功能</td></tr></table>

## 7.4.11. 位清除寄存器（GPIOx_BC，x=A..D，F）

地址偏移：0x28

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CR15</td><td>CR14</td><td>CR13</td><td>CR12</td><td>CR11</td><td>CR10</td><td>CR9</td><td>CR8</td><td>CR7</td><td>CR6</td><td>CR5</td><td>CR4</td><td>CR3</td><td>CR2</td><td>CR1</td><td>CR0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>Cry</td><td>端口清除位y(y=0..15)该位由软件置位和清除。0:相应OCTLy位没有改变1:清除相应的OCTLy位</td></tr></table>

## 7.4.12. 端口位翻转寄存器（GPIOx_TG，x=A..D，F）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TG15</td><td>TG14</td><td>TG13</td><td>TG12</td><td>TG11</td><td>TG10</td><td>TG9</td><td>TG8</td><td>TG7</td><td>TG6</td><td>TG5</td><td>TG4</td><td>TG3</td><td>TG2</td><td>TG1</td><td>TG0</td></tr><tr><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td><td>w</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31:16</td><td colspan="4">保留</td><td colspan="11">必须保持复位值</td></tr><tr><td>15:0</td><td colspan="4">Tgy</td><td colspan="11">端口翻转位y(y=0..15)该位由软件置位和清除。0:相应OCTLy位没有改变t1:翻转相应的OCTLy位</td></tr></table>
