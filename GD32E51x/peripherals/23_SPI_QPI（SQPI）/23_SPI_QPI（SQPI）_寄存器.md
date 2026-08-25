## 23.4. SQPI 寄存器

SQPI 基地址：0xA000 1000

## 23.4.1. 初始化寄存器 (SQPI_INIT)

偏移地址：0x00

系统复位值：0x1805 0000

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPI_PL</td><td colspan="2">SQPI_IDLEN[1:0]</td><td colspan="5">SQPI_ADDRBIT[4:0]</td><td colspan="6">SQPI_CLKDIV[5:0]</td><td colspan="2">SQPI_CMDBIT[1:0]</td></tr><tr><td>rw</td><td colspan="2">rw</td><td colspan="5">rw</td><td colspan="6">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPI_PL</td><td>读数据采样极性0:上升沿采样数据(默认)1:下降沿采样数据</td></tr><tr><td>30:29</td><td>SQPI_IDLEN[1:0]</td><td>外部存储器ID长度00:64位01:32位10:16位11:8位</td></tr><tr><td>28:24</td><td>SQPI_ADDRBIT[4:0]</td><td>地址阶段的位数默认:24位</td></tr><tr><td>23:18</td><td>SQPI_CLKDIV[5:0]</td><td>SQPI时钟分频0x0无效.输出时钟频率等于<eq>f_{hclk}/(SQPI\_CLKDIV+1)</eq>注意:当SQPI_CLKDIV为偶数时,输出时钟高电平比低电平多一个AHB时钟周期</td></tr><tr><td>17:16</td><td>SQPI_CMDBIT[1:0]</td><td>SQPI命令阶段的位数00:4位01:8位(默认)10:16位11:保留</td></tr><tr><td>15:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 23.4.2. 读命令寄存器 (SQPI_RCMD)

偏移地址： 0x04

系统复位值：0x0010 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPI_RID</td><td colspan="8">保留</td><td colspan="3">SQPI_RMODE[2:0]</td><td colspan="4">SQPI_RWAITCYCLE[3:0]</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SQPI_RCMD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPI_RID</td><td>发送读 ID 命令,命令来自 SQPI_RCMD 位域</td></tr><tr><td>30:23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:20</td><td>SQPI_RMODE[2:0]</td><td>SQPI 读命令模式000:SSQ 模式001:SSS 模式010:SSQ 模式011:QQQ 模式100:SSD 模式101:SDD 模式</td></tr><tr><td>19:16</td><td>SQPI_RWAITCYCLE [3:0]</td><td>SQPI 在地址阶段之后的读命令等待周期个数</td></tr><tr><td>15:0</td><td>SQPI_RCMD[15:0]</td><td>用于 SQPI 读操作时的 AHB 总线发送的命令当 SQPI_CMDBIT=00 时,SQPI_RCMD[3:0]有效当 SQPI_CMDBIT=01 时,SQPI_RCMD[7:0]有效当 SQPI_CMDBIT=10 时,SQPI_RCMD[15:0]有效</td></tr></table>

## 23.4.3. 写命令寄存器 (SQPI_WCMD)

偏移地址：0x08

系统复位：0x0010 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SQPI_SCMD</td><td colspan="8">保留</td><td colspan="3">SQPI_WMODE [2:0]</td><td colspan="4">SQPI_WWAITCYCLE [3:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">rw</td><td colspan="4">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SQPI_WCMD[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SQPI_SCMD</td><td>发送没有地址阶段和数据阶段的特殊命令,命令来自 SQPI_WCMD.</td></tr><tr><td>30:23</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>22:20</td><td>SQPI_WMODE[2:0]</td><td>SQPI 写命令模式:000:SSQ 模式001:SSS 模式010:SQQ 模式011:QQQ 模式100:SSD 模式101:SDD 模式</td></tr><tr><td>19:16</td><td>SQPI_WWAITCYCLE[3:0]</td><td>SQPI 在地址阶段之后的写命令等待周期个数</td></tr><tr><td>15:0</td><td>SPI_WCMD[15:0]</td><td>用于 SQPI 写操作时的 AHB 总线发送的命令</td></tr></table>

## 23.4.4. ID 低位寄存器 (SQPI_IDL)

偏移地址：0x0C

系统复位：0x0000 0000


该寄存器只能按字(32 位)访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">SQPI_IDL [31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">SQPI_IDL [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SQPI_IDL[31:0]</td><td>使用 SQPI 读 ID 命令时,返回的 ID 低位数据当 SQPI_IDLEN=10 时,SQPI_IDL[15:0]有效当 SQPI_IDLEN=11 时,SQPI_IDL[7:0]有效</td></tr></table>

## 23.4.5. ID 高位寄存器 (SQPI_IDH)

偏移地址： 0x10

系统复位：0x0000 0000

<table><tr><td colspan="16">该寄存器只能按字(32位)访问</td></tr><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="15">SQPI_IDH[31:16]</td><td></td></tr><tr><td colspan="15">r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">SQPI_IDH[15:0]</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>SQPI_IDH[31:0]</td><td>使用 SQPI 读 ID 命令时,返回的 ID 高位数据只有当 SQPI_IDLEN = 00 时,该寄存器有效</td></tr></table>
