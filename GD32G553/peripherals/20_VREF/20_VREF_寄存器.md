## 20.4. VREF 寄存器

VREF 基地址：0x4001 7800

当 DACx（x=0,1,2,3）中任一个的 DRSTMDy（y=0,1）位置 1，VREF 寄存器将在除 POR 以外的所有复位事件中保持。

## 20.4.1. 控制状态寄存器（VREF_CS）

地址偏移：0x00

复位值：0x0000 0002

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="2">VREFS[1:0]</td><td>VREFRDY</td><td>保留</td><td>HIPM</td><td>VREFEN</td></tr><tr><td colspan="10"></td><td colspan="2">rw</td><td colspan="2">r</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:4</td><td>VREFS[1:0]</td><td>参考电压选择这些位定义了VREF产生的参考电压的数值。00: 参考电压在2.048V左右01: 参考电压在2.5V左右10: 参考电压在2.9V左右11: 保留此位只有在 VREF 失能(VREFEN 位为 0)的时候可以被更改。</td></tr><tr><td>3</td><td>VREFRDY</td><td>VREF就绪0: VREF输出未就绪1: VREF 输出就绪</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>HIPM</td><td>高阻抗模式0: VREFP 引脚内部连接到 VREF 输出1: VREFP 引脚为高阻抗模式</td></tr><tr><td>0</td><td>VREFEN</td><td>VREF使能0: VREF失能</td></tr></table>

## 1：VREF 使能

## 20.4.2. 校准寄存器（VREF_CALIB）

地址偏移：0x04

复位值：0x0000 00XX

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td colspan="6">VREFCAL[5:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5:0</td><td>VREFCAL</td><td>VREF校准值复位时,或者所选的参考电压改变时(由VREFS[1:0]位域控制)这些位将被自动初始化为在生产测试期间存储在Flash中的校准值。写入这些位也可调节内部VREF电压。写入这些位后,如果所选的参考电压改变,VREF校准值将不会被自动初始化知道MCU复位。注意:如果用户执行校准程序,则校准值必须从0x00递增到0x3F。</td></tr></table>

