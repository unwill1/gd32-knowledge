# 28.4. OSPIM 寄存器

OSPIM基地址：0x5200 B400

# 28.4.1. 端口配置寄存器（OSPIM_PCFGx）（x = 0, 1）

地址偏移：0x04*（x+1）

复位值：0x0301 0111（x = 0），0x0705 0333（x = 1）。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td colspan="2">SRCPHIO[1:0]</td><td>POHEN</td><td colspan="5">保留</td><td colspan="2">SRCPLIO[1:0]</td><td>POLEN</td></tr><tr><td colspan="5"></td><td colspan="2">rw</td><td>rw</td><td colspan="5"></td><td colspan="2">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>SRCPCS</td><td>NCSEN</td><td colspan="6">保留</td><td>SRCPCK</td><td>SCKEN</td></tr><tr><td colspan="5"></td><td>rw</td><td>rw</td><td></td><td colspan="5"></td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:25</td><td>SRCPHIO[1:0]</td><td>端口x的IO[7:4]源选择00:选择OSPI0_IO[3:0]。01:选择OSPI0_IO[7:4]。10:选择OSPI1_IO[3:0]。11:选择OSPI1_IO[7:4]。</td></tr><tr><td>24</td><td>POHEN</td><td>使能端口x的IO[7:4]0:禁用端口x的IO[7:4]。1:使能端口x的IO[7:4]。</td></tr><tr><td>23:19</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>18:17</td><td>SRCPLIO[1:0]</td><td>端口x的IO[3:0]源选择00:选择OSPI0_IO[3:0]。01:选择OSPI0_IO[7:4]。10:选择OSPI1_IO[3:0]。11:选择OSPI1_IO[7:4]。</td></tr><tr><td>16</td><td>POLEN</td><td>使能端口x的IO[3:0]0:禁用端口x的IO[3:0]。1:使能端口x的IO[3:0]。</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>SRCPCS</td><td>端口x的CSN源选择0:CSN源为OSPI0_CSN。1:CSN源为OSPI1_CSN。</td></tr><tr><td>8</td><td>NCSEN</td><td>端口x的CSN使能0:禁用端口x的CSN。1:使能端口x的CSN。</td></tr><tr><td>7:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>SRCPCK</td><td>端口x的SCK源选择0:SCK源为OSPI0_SCK。1:SCK源为OSPI1_SCK。</td></tr><tr><td>0</td><td>SCKEN</td><td>端口x的SCK使能0:禁用端口x的SCK。1:使能端口x的SCK。</td></tr></table>
