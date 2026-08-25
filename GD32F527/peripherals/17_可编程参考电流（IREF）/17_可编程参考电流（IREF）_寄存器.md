## 17.4. IREF 寄存器

IREF 基地址：0x4000 C400

控制寄存器 (IREF_CTL)

偏移地址：0x300

复位值：0x0000 0F00

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CREN</td><td>SSEL</td><td>保留</td><td colspan="5">CPT[4:0]</td><td>SCMOD</td><td>保留</td><td colspan="6">CSDT[5:0]</td></tr><tr><td>rw</td><td>rw</td><td></td><td colspan="4">rw</td><td colspan="3">rw</td><td colspan="6">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CREN</td><td>参考电流使能0:禁用参考电流1:使能参考电流</td></tr><tr><td>14</td><td>SSEL</td><td>步长选择0:低功耗,步长1uA1:大电流,步长8uA</td></tr><tr><td>13</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>12:8</td><td>CPT[4:0]</td><td>电流精度校准0x00:-30%....0x1F:+32%</td></tr><tr><td>7</td><td>SCMOD</td><td>灌电流模式0:源电流模式1:灌电流模式</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5:0</td><td>CSDT[5:0]</td><td>电流步长设置0x00:默认值0x01:Step * 1....0x3F:Step * 63</td></tr></table>
