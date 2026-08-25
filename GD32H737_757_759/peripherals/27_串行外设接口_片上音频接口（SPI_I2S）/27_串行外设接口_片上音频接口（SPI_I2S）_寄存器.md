# 27.5. SPI / I2S 寄存器

SPI0 / I2S0基地址：0x4001 3000

SPI1 / I2S1基地址：0x4000 3800

SPI2 / I2S2基地址：0x4000 3C00

SPI3基地址：0x4001 3400

SPI4基地址：0x4001 5000

SPI5 / I2S5基地址：0x4001 3800

# 27.5.1. 控制寄存器 0（SPI_CTL0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器可以按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">保留</td><td>IOAFEN</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>TXCRCI</td><td>RXCRCI</td><td>CRCFS</td><td>NSSI</td><td>保留</td><td>MSPDR</td><td>MSTART</td><td>MASP</td><td colspan="7">保留</td><td>SPIEN</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>w</td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td></tr></table>


位/位域


<table><tr><td>31:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>IOAFEN</td><td>相关IO的AF配置功能使能0: 相关IO的AF配置功能使能</td></tr></table>
