## 24.4. VREF 寄存器

VREF 基地址：0x4001 0030

## 24.4.1. 控制和状态寄存器（VREF_CS）

GD32L233xx 产品

地址偏移：0x00

复位值：0x0000 0002

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>VREFRDY</td><td>保留</td><td>HIPM</td><td>VREFEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>VREFRDY</td><td>VREF就绪0: VREF输出未就绪1: VREF输出就绪</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>1</td><td>HIPM</td><td>高阻抗模式0: <eq>V_{REF+}</eq>内部连接到VREF输出1: <eq>V_{REF+}</eq>引脚为高阻抗</td></tr><tr><td>0</td><td>VREFEN</td><td>VREF使能0: VREF失能1: VREF使能</td></tr></table>

GD32L235xx 产品

地址偏移：0x00

复位值：0x0000 0002

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>VREFRDY</td><td>VREFS</td><td>HIPM</td><td>VREFEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>VREFRDY</td><td>VREF就绪0: VREF输出未就绪1: VREF输出就绪</td></tr><tr><td>2</td><td>VREFS</td><td>参考电压选择该位定义了VREF产生的参考电压的数值0: 参考电压在1.5V左右1: 参考电压在2.5V左右</td></tr><tr><td>1</td><td>HIPM</td><td>高阻抗模式0: <eq>V_{REF+}</eq>内部连接到VREF输出1: <eq>V_{REF+}</eq>引脚为高阻抗</td></tr><tr><td>0</td><td>VREFEN</td><td>VREF使能0: VREF失能1: VREF使能</td></tr></table>

## 24.4.2. 校准寄存器（VREF_CALIB）

地址偏移：0x04

复位值：0x0000 00xx

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">VREFCAL[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>VREFCAL</td><td>VREF校准复位后,这些位将在生产测试期间使用存储在FLASH中的修整值自动初始化。写入这些位可调节内部<eq>V_{REF}</eq>电压。</td></tr></table>
