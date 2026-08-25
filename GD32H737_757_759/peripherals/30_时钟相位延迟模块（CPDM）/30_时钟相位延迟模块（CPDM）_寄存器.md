# 30.4. CPDM 寄存器

CPDM(SDIO0)基地址：0x5200 8000

CPDM(SDIO1)基地址：0x4802 2800

# 30.4.1. 控制寄存器（CPDM_CTL）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>DLSEN</td><td>CPDMEN</td></tr></table>


rw rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>DLSEN</td><td>延迟线采样模块使能位0:禁能 CPDM 延迟线采样模块1:使能 CPDM 延迟线采样模块</td></tr><tr><td>0</td><td>CPDMEN</td><td>CPDM 使能位0:禁能 CPDM1:使能 CPDM</td></tr></table>

# 30.4.2. 配置寄存器（CPDM_CFG）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DLLENF</td><td colspan="3">保留</td><td colspan="12">DLLEN[11:0]</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="7">DLSTCNT[6:0]</td><td colspan="4">保留</td><td colspan="4">CPSEL[3:0]</td></tr><tr><td></td><td colspan="7">rw</td><td colspan="4"></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DLLENF</td><td>延迟线长度有效标志</td></tr></table>

0：DLLEN[11:0]中的长度值无效。

1：DLLEN[11:0]中的长度值有效。

30:28 保留 必须保持复位值。

27:16 DLLEN[11:0] 延迟线长度值

在输入时钟的上升沿采样的 12个单位延迟值。

仅在 DLLENF = 1 时有效。

15 保留 必须保持复位值。

14:8 DLSTCNT[6:0] 定义一个单位延迟单元的所需的延迟步长的计数值

仅当 DLSEN = 1 时，才可写入。

0000000：单位延迟 = 初始延迟

0000001：单位延迟 = 初始延迟+ 1 *延迟步长

1111111：单位延迟 = 初始延迟+ 127 *延迟步长

7:4 保留 必须保持复位值。

3:0 CPSEL[3:0] 输出时钟相位选择

仅当 DLSEN = 1 时，才可写入。

输出时钟的相位 = 输入时钟 + CPSEL * 单位延迟

0000：输出时钟的相位 = 输入时钟

0001：输出时钟的相位 = 输入时钟 + 1 * 单位延迟

1100：输出时钟的相位 = 输入时钟 + 12 * 单位延迟

1101 ~ 1111：保留
