# 18.6. DMAMUX 寄存器

DMAMUX 基地址：0x4002 0800

# 18.6.1. 请求路由通道 x 配置寄存器（DMAMUX_RM_CHxCFG）

x = 0...15，其中 x 为通道序号

地址偏移：0x00 + 0x04 * x

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td colspan="5">SYNCID[4:0]</td><td colspan="5">NBR[4:0]</td><td colspan="2">SYNCP[1:0]</td><td>SYNCEN</td></tr><tr><td colspan="3"></td><td colspan="5">rw</td><td colspan="5">rw</td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>EVGEN</td><td>SOIE</td><td colspan="8">MUXID[7:0]</td></tr><tr><td colspan="3"></td><td colspan="2">rw</td><td colspan="3">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28:24</td><td>SYNCID[4:0]</td><td>同步输入标识选择同步输入源。</td></tr><tr><td>23:19</td><td>NBR[4:0]</td><td>传递的DMA请求数量在同步输入事件之后,或者通道事件输出之前,将传递到DMA控制器的DMA请求数量为NBR[4:0]+1。该位域只能在SYNCEN位和EVGEN位都禁能时才能配置。</td></tr><tr><td>18:17</td><td>SYNCP[1:0]</td><td>同步输入极性00:不检测事件01:上升沿10:下降沿11:上升和下降沿</td></tr><tr><td>16</td><td>SYNCEN</td><td>同步模式使能0:禁能同步模式1:使能同步模式</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>EVGEN</td><td>事件输出使能0:禁能事件输出1:使能事件输出</td></tr><tr><td>8</td><td>SOIE</td><td>同步溢出中断使能0:禁能中断</td></tr></table>
