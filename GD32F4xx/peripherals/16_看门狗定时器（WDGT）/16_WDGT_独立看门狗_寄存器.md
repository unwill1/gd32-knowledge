## 16.1.4. FWDGT 寄存器

FWDGT 基地址：0x4000 3000

## 控制寄存器（FWDGT_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CMD[15:0]</td></tr></table>

w 

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>CMD[15:0]</td><td>只可写,写入不同的值来产生不同的功能0x5555:关闭FWDGT_PSC和FWDGT_RLD的写保护0xCCCC:开启独立看门狗定时器定时计数器。计数减到0时产生复位0xAAAA:重装载计数器</td></tr></table>

## 预分频寄存器（FWDGT_PSC）

地址偏移：0x04

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">PSC[2:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2:0</td><td>PSC[2:0]</td><td>独立看门狗定时器计时预分频选择。写这些位之前要通过向FWDGT_CTL寄存器写0x5555去除写保护。在改写这个寄存器的过程中,FWDGT_STAT寄存器的PUD位被置1,此时读取此寄存器的值都是无效的。000: 1 / 4001: 1 / 8</td></tr></table>

<table><tr><td>010:</td><td>1 / 16</td></tr><tr><td>011:</td><td>1 / 32</td></tr><tr><td>100:</td><td>1 / 64</td></tr><tr><td>101:</td><td>1 / 128</td></tr><tr><td>110:</td><td>1 / 256</td></tr><tr><td>111:</td><td>1 / 256</td></tr></table>

如果应用需要使用不同的预分频系数，改变预分频值之前必须等到PUD位被清0。更新了预分频寄存器中的值后，在代码持续执行之前不必等待PUD值被清零（在进入省电模式前需要等待PUD值清零）。

## 重装载寄存器（FWDGT_RLD）

地址偏移：0x08

复位值：0x0000 0FFF

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">保留</td><td colspan="12">RLD [11:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>RLD[11:0]</td><td>独立看门狗定时器定时计数器重装载值,向FWDGT_CTL寄存器写入0xAAAA的时候,这个值会被更新到看门狗定时器计数器中。这些位有写保护功能。在写这些位之前需向FWDGT_CTL寄存器中写0x5555。在改写这个寄存器的过程中,FWDGT_STAT寄存器的RUD位被置1,从此寄存器中读取的任何值都是无效的。如果应用需要使用不同的重装载值,改变重加载值之前必须等到RUD位被清0。更新了重加载寄存器的值后,在代码持续执行之前不必等待RUD值被清零(在进入省电模式前需要等待RUD值清零)。</td></tr></table>

## 状态寄存器（FWDGT_STAT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>RUD</td><td>PUD</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>说明</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>RUD</td><td>独立看门狗定时计数器重装载值更新FWDGT_RLD寄存器写操作时,该位被置1,此时读取FWDGT_RLD寄存器的任何值都是无效的。在FWDGT_RLD寄存器更新后,该位由硬件清零。</td></tr><tr><td>0</td><td>PUD</td><td>独立看门狗定时器预分频值更新FWDGT_PSC寄存器写操作时,该位被置1,此时读取FWDGT_PSC寄存器的任何值都是无效的。在FWDGT_PSC寄存器更新后,该位由硬件清零。</td></tr></table>

