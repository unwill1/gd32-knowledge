## 9.5. DMAMUX 寄存器

DMAMUX基地址：0x4002 0800

## 9.5.1. 请求路由通道 x 配置寄存器（DMAMUX_RM_CHxCFG）

地址偏移：0x00 + 0x04 * x（x = 0...13，其中 x 为通道序号）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="5">SYNCID[4:0]</td><td colspan="5">NBR[4:0]</td><td colspan="2">SYNCP[1:0]</td><td>SYNCEN</td></tr><tr><td colspan="8">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>EVGEN</td><td>SOIE</td><td colspan="8">MUXID[7:0]</td></tr><tr><td colspan="6">rw</td><td colspan="2">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:24</td><td>SYNCID[4:0]</td><td>同步输入标识选择同步输入源。</td></tr><tr><td>23:19</td><td>NBR[4:0]</td><td>传递的DMA请求数量在同步输入事件之后,或者通道事件输出之前,将传递到DMA控制器的DMA请求数量为NBR[4:0]+1。该位域只能在SYNCEN位和EVGEN位都禁能时才能配置。</td></tr><tr><td>18:17</td><td>SYNCP[1:0]</td><td>同步输入极性00:不检测事件01:上升沿10:下降沿11:上升和下降沿</td></tr><tr><td>16</td><td>SYNCEN</td><td>同步模式使能0:禁能同步模式1:使能同步模式</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EVGEN</td><td>事件输出使能0:禁能事件输出1:使能事件输出</td></tr><tr><td>8</td><td>SOIE</td><td>同步溢出中断使能0:禁能中断1:使能中断</td></tr><tr><td>7:0</td><td>MUXID[7:0]</td><td>请求路由标识选择DMAMUX请求路由通道的DMA请求输入源。</td></tr></table>

## 9.5.2. 请求路由通道中断标志位寄存器（DMAMUX_RM_INTF）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SOIF13</td><td>SOIF12</td><td>SOIF11</td><td>SOIF10</td><td>SOIF9</td><td>SOIF8</td><td>SOIF7</td><td>SOIF6</td><td>SOIF5</td><td>SOIF4</td><td>SOIF3</td><td>SOIF2</td><td>SOIF1</td><td>SOIF0</td></tr><tr><td colspan="2"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>SOIFx</td><td>请求路由通道x(x=0..13)的同步溢出事件标志位当DMAMUX请求路由通道x发生了同步输入事件,而此时DMAMUX请求路由计数器值小于NBR[4:0],则该通道的同步溢出标志位置位。通过对DMAMUX_RM_INTC寄存器的SOIFCx位写1来清除相应通道的同步溢出标志。</td></tr></table>

## 9.5.3. 请求路由通道中断标志位清除寄存器（DMAMUX_RM_INTC）

地址偏移：0x084

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>SOIFC13</td><td>SOIFC12</td><td>SOIFC11</td><td>SOIFC10</td><td>SOIFC9</td><td>SOIFC8</td><td>SOIFC7</td><td>SOIFC6</td><td>SOIFC5</td><td>SOIFC4</td><td>SOIFC3</td><td>SOIFC2</td><td>SOIFC1</td><td>SOIFC0</td></tr><tr><td></td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td><td>W</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:12</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>11:0</td><td>SOIFCx</td><td>请求路由通道x(x=0..13)的同步溢出事件标志清除位写1可清除相应通道在DMAMUX_RM_INTF寄存器的同步溢出标志SOIFx。</td></tr></table>

## 9.5.4. 请求生成通道 x 配置寄存器（DMAMUX_RG_CHxCFG）

地址偏移：0x100 + 0x04 * x（x = 0...3，其中 x 为通道序号）

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="5">NBRG[4:0]</td><td colspan="2">RGTP[1:0]</td><td>RGEN</td></tr><tr><td colspan="13">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="7">保留</td><td>TOIE</td><td colspan="3">保留</td><td colspan="5">TID[4:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:19</td><td>NBRG[4:0]</td><td>待产生的DMA请求数量在触发输入事件之后,待产生的DMA请求数量为NBRG[4:0]+1。注意:只有当RGEN位为0时才能写该位域。</td></tr><tr><td>18:17</td><td>RGTP[1:0]</td><td>DMAMUX请求生成触发输入极性00:不检测事件01:上升沿10:下降沿11:上升沿和下降沿</td></tr><tr><td>16</td><td>RGEN</td><td>DMAMUX请求生成通道x使能0:禁能DMAMUX请求生成通道x1:使能DMAMUX请求生成通道x</td></tr><tr><td>15:9</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>8</td><td>TOIE</td><td>触发溢出中断使能0:禁能中断1:使能中断</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4:0</td><td>TID[4:0]</td><td>触发输入标识选择DMAMUX请求生成通道的触发输入源。</td></tr></table>

## 9.5.5. 请求生成通道中断标志位寄存器（DMAMUX_RG_INTF）

地址偏移：0x140

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>TOIF3</td><td>TOIF2</td><td>TOIF1</td><td>TOIF0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>TOIFx</td><td>DMAMUX请求生成通道x(x=0..3)的触发溢出标志位如果在DMAMUX请求生成计数器(通过DMAMUX_RG_CHxCFG寄存的NBRG[4:0]位域配置)发生下溢之前,DMAMUX请求生成通道x发生了一个新的触发输入事件,则该标志位置位。通过对DMAMUX_RG_INTC寄存器的TOIFCx位写1来清除相应通道的触发溢出标志。</td></tr></table>

## 9.5.6. 请求生成通道中断标志位清除寄存器（DMAMUX_RG_INTC）

地址偏移：0x144

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>TOIFC3</td><td>TOIFC2</td><td>TOIFC1</td><td>TOIFC0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3:0</td><td>TOIFCx</td><td>请求生成通道x(x=0..3)的触发溢出事件标志清除位写1可清除相应通道在DMAMUX_RG_INTF寄存器的触发溢出标志TOIFx。</td></tr></table>
