# 3.4. FMC 寄存器

FMC基地址：0x5200 2000

# 3.4.1. 解锁寄存器（FMC_KEY）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">KEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">KEY[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>KEY[31:0]</td><td>FMC_CTL 解锁寄存器这些位仅能被软件写。写解锁值到KEY[31:0]可以解锁FMC_CTL寄存器。</td></tr></table>

# 3.4.2. 选项字节操作解锁寄存器（FMC_OBKEY）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">OBKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">OBKEY[15:0]</td></tr></table>


w


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>OBKEY [31:0]</td><td>这些位仅能被软件写写解锁值到OBKEY[31:0]解锁FMC_OBCTL寄存器。</td></tr></table>

# 3.4.3. 控制寄存器（FMC_CTL）

地址偏移：0x0C

复位值：0x0000 0001

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="7">保留</td><td>RSERRIE</td><td>RPERRIE</td><td colspan="4">保留</td><td>PGSERRIE</td><td>WPERRIE</td><td>ENDIE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>START</td><td colspan="2">保留</td><td>PGCHEN</td><td>MER</td><td>SER</td><td>PG</td><td>LK</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>RSERRIE</td><td>读安全错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能读安全错误中断1:使能读安全错误中断</td></tr><tr><td>23</td><td>RPERRIE</td><td>读保护错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能读保护错误中断1:使能读保护错误中断</td></tr><tr><td>22:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>PGSERRIE</td><td>编程顺序错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能编程顺序错误中断1:使能编程顺序错误中断</td></tr><tr><td>17</td><td>WPERRIE</td><td>擦除/删除保护错误中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能擦除/删除保护错误中断1:使能擦除/删除保护错误中断</td></tr><tr><td>16</td><td>ENDIE</td><td>操作结束中断使能位当LK设置为0时,该位才能被软件置1和清0。0:失能操作结束中断1:使能操作结束中断</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>START</td><td>向FMC发送擦除命令位当LK设置为0时,该位才能被软件置1,发送擦除命令到FMC。当BUSY位被清0时,此位由硬件清0。</td></tr><tr><td>6:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>PGCHEN</td><td>编程区域检查使能位当LK设置为0时,该位才能被软件置1和清0。0:编程前不去检查编程区域数据是否为全0xFF1:编程前去检查编程区域数据是否为全0xFF若该位置1,且编程区域数据不全为0xFF时,PGSERR将会置位。且该编程操作无效。</td></tr><tr><td>3</td><td>MER</td><td>整片擦除命令位当LK设置为0时,该位才能被软件置1和清0。0:无作用1:整片擦除命令如果同时请求整片擦除和扇区擦除,则整片擦除将替代扇区擦除操作。</td></tr><tr><td>2</td><td>SER</td><td>扇区擦除命令位当LK设置为0时,该位才能被软件置1和清0。0:无作用1:扇区擦除命令如果同时请求整片擦除和扇区擦除,则整片擦除将替代扇区擦除操作。</td></tr><tr><td>1</td><td>PG</td><td>主存储闪存块编程命令位当LK设置为0时,该位才能被软件置1和清0。0:无作用1:主存储闪存块编程命令</td></tr><tr><td>0</td><td>LK</td><td>FMC_CTL寄存器锁定标志位当正确的序列写入FMC_KEY寄存器,此位由硬件清0。此位可以由软件置1。</td></tr></table>


注意：当相应闪存操作完成后，该寄存器需处于复位状态


# 3.4.4. 状态寄存器（FMC_STAT）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>OBMERR</td><td colspan="5">保留</td><td>RSERR</td><td>RPERR</td><td colspan="4">保留</td><td>PGSERR</td><td>WPERR</td><td>ENDF</td></tr><tr><td></td><td>rc_w1</td><td></td><td></td><td></td><td></td><td></td><td>rc_w1</td><td>rc_w1</td><td></td><td></td><td></td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">保留</td><td>BUSY</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>OBMERR</td><td>选项字节修改错误标志位该位由硬件置位,软件写1清0。0:未发生选项字节修改错误1:发生选项字节修改错误</td></tr><tr><td>29:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>RSERR</td><td>读安全错误标志位该位由硬件置位,软件写1清0。0:未发生读安全错误1:发生读安全错误</td></tr><tr><td>23</td><td>RPERR</td><td>读保护错误标志位该位由硬件置位,软件写1清0。0:未发生读保护错误1:发生读保护错误</td></tr><tr><td>22:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>PGSERR</td><td>编程顺序错误标志位该位由硬件置位,软件写1清0。0:未发生编程顺序错误1:发生编程顺序错误</td></tr><tr><td>17</td><td>WPERR</td><td>擦除/编程保护错误标志位该位由硬件置位,软件写1清0。0:未发生擦除/编程保护错误1:发生擦除/编程保护错误</td></tr><tr><td>16</td><td>ENDF</td><td>操作结束标志位当操作执行成功,此位被硬件置1。软件写1清0。</td></tr><tr><td>15:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>BUSY</td><td>闪存忙标志位当闪存操作正在进行时,此位被置1。当操作结束或者出错,此位被清0。</td></tr></table>

# 3.4.5. 地址寄存器（FMC_ADDR）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ADDR[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ADDR[31:0]</td><td>闪存擦除地址该位通过软件设置。ADDR 位是闪存擦除命令的地址。</td></tr></table>

# 3.4.6. 选项字节控制寄存器（FMC_OBCTL）

地址偏移：0x18

复位值：0x0000 0001

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>保留</td><td>OBMERRIE</td><td colspan="14">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>OBSTART</td><td>OBLK</td></tr></table>


rs rs 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>30</td><td>OBMERRIE</td><td>选项字节修改错误中断使能位当OBLK设置为0时,该位才能被软件置1和清0。0:失能选项字节修改错误中断1:使能选项字节修改错误中断</td></tr><tr><td>29:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>OBSTART</td><td>发送选项字节命令到FMC仅当OBLK设置为0时,该位才能由软件置1。当BUSY位清0时由硬件清除该位。</td></tr><tr><td>0</td><td>OBLK</td><td>FMC_OBCTL锁定位当往FMC_OBKEY寄存器写值顺序正确时,该位由硬件清0。软件置1。</td></tr></table>

# 3.4.7. 选项字节状态寄存器 0（FMC_OBSTAT0_EFT）

地址偏移：0x1C

复位值：0xXXXX XXXX，出厂值为0x01C6 AAD0

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>IOSPDOPEN</td><td colspan="4">保留</td><td>DTCM1ECCEN</td><td>DTCM0ECCEN</td><td>ITCMECCEN</td><td>SCR</td><td colspan="2">保留</td><td>FWDGSPD_STDBY</td><td>FWDGSPD_DPSLP</td><td>保留</td></tr><tr><td colspan="2"></td><td>r</td><td colspan="4"></td><td>r</td><td>r</td><td>r</td><td>r</td><td colspan="2"></td><td>r</td><td>r</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">SPC[7:0]</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td>保留</td><td>nWDG_HW</td><td colspan="2">BOR_TH[1:0]</td><td colspan="2">保留</td></tr><tr><td colspan="3"></td><td colspan="5">r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td></td><td></td><td></td></tr></table>

位/位域 名称 描述

<table><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>IOSPDOPEN</td><td>低电压下的I/O速度优化功能的允许使能状态位0:芯片工作电压大于2.5V,因此I/O速度优化不被允许1:芯片工作电压低于2.5V,因此I/O速度优化被允许</td></tr><tr><td>28:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>DTCM1ECCEN</td><td>DTCM1的ECC功能使能状态位0:失能DTCM1的ECC功能1:使能DTCM1的ECC功能</td></tr><tr><td>23</td><td>DTCM0ECCEN</td><td>DTCM0的ECC功能使能状态位0:失能DTCM0的ECC功能1:使能DTCM0的ECC功能</td></tr><tr><td>22</td><td>ITCMECCEN</td><td>ITCM的ECC功能使能状态位0:失能ITCM的ECC功能1:使能ITCM的ECC功能</td></tr><tr><td>21</td><td>SCR</td><td>安全模式使能状态位0:失能安全模式1:使能安全模式</td></tr><tr><td>20:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>FWDGSPD_STDBY</td><td>待机模式下独立看门狗(FWDG)暂停选项状态位0:在待机状态下暂停独立看门狗1:在待机状态下运行独立看门狗</td></tr><tr><td>17</td><td>FWDGSPD_DPSLP</td><td>深度睡眠模式下独立看门狗暂停选项状态位0:在深度睡眠状态下暂停独立看门狗1:在深度睡眠状态下运行独立看门狗</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>SPC[7:0]</td><td>安全保护等级状态值0xAA:无保护状态0xCC:安全保护等级高除0xAA或0xCC之外任何值:安全保护等级低</td></tr><tr><td>7</td><td>nRST_STDBY</td><td>进入待机模式复位选项状态位0:进入待机模式时产生复位1:进入待机模式时不产生复位</td></tr><tr><td>6</td><td>nRST_DPSLP</td><td>进入深度睡眠模式复位选项状态位0:进入深度睡眠模式时产生复位1:进入深度睡眠模式时不产生复位</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>nWDG_HW</td><td>看门狗控制状态位</td></tr></table>

0：硬件控制看门狗

1：软件控制看门狗

<table><tr><td>3:2</td><td>BOR_TH[1:0]</td><td>欠压复位(BOR)阈值状态位</td></tr><tr><td></td><td></td><td>00:无BOR功能</td></tr><tr><td></td><td></td><td>01:BOR阈值1</td></tr><tr><td></td><td></td><td>10:BOR阈值2</td></tr><tr><td></td><td></td><td>11:BOR阈值3</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 3.4.8. 选项字节状态寄存器 0（FMC_OBSTAT0_MDF）

地址偏移：0x20

复位值：0xXXXX XXXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td>IOSPDOPEN</td><td colspan="4">保留</td><td>DTCM1ECCEN</td><td>DTCM0ECCEN</td><td>ITCMECCEN</td><td>SCR</td><td colspan="2">保留</td><td>FWDGSPD_STDBY</td><td>FWDGSPD_DPSLP</td><td>保留</td></tr><tr><td colspan="2"></td><td colspan="5">rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">SPC[7:0]</td><td>nRST_STDBY</td><td>nRST_DPSLP</td><td>保留</td><td>nWDG_HW</td><td colspan="2">BOR_TH[1:0]</td><td colspan="2">保留</td></tr><tr><td colspan="3"></td><td colspan="5">rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td colspan="2"></td></tr></table>


位/位域 名称 描述


<table><tr><td>31:30</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>29</td><td>IOSPDOPEN</td><td>低电压下的I/O速度优化功能的允许使能配置位0:芯片工作电压大于2.5V,因此I/O速度优化不被允许1:芯片工作电压低于2.5V,因此I/O速度优化被允许</td></tr><tr><td>28:25</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>24</td><td>DTCM1ECCEN</td><td>DTCM1的ECC功能使能配置位0:失能DTCM1的ECC功能1:使能DTCM1的ECC功能</td></tr><tr><td>23</td><td>DTCM0ECCEN</td><td>DTCM0的ECC功能使能配置位0:失能DTCM0的ECC功能1:使能DTCM0的ECC功能</td></tr><tr><td>22</td><td>ITCMECCEN</td><td>ITCM的ECC功能使能配置位0:失能ITCM的ECC功能1:使能ITCM的ECC功能</td></tr><tr><td>21</td><td>SCR</td><td>安全模式使能配置位0: 失能安全模式1: 使能安全模式</td></tr><tr><td>20:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>FWDGSPD_STDBY</td><td>待机模式下独立看门狗暂停选项配置位0: 在待机状态下暂停独立看门狗1: 在待机状态下运行独立看门狗</td></tr><tr><td>17</td><td>FWDGSPD_DPSLP</td><td>深度睡眠模式下独立看门狗暂停选项配置位0: 在深度睡眠状态下暂停独立看门狗1: 在深度睡眠状态下运行独立看门狗</td></tr><tr><td>16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>SPC[7:0]</td><td>安全保护等级配置值0xAA: 无保护状态0xCC: 安全保护等级高除0xAA或0xCC之外任何值: 安全保护等级低</td></tr><tr><td>7</td><td>nRST_STDBY</td><td>进入待机模式复位选项配置位0: 进入待机模式时产生复位1: 进入待机模式时不产生复位</td></tr><tr><td>6</td><td>nRST_DPSLP</td><td>进入深度睡眠模式复位选项配置位0: 进入深度睡眠模式时产生复位1: 进入深度睡眠模式时不产生复位</td></tr><tr><td>5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>nWDG_HW</td><td>看门狗控制配置位0: 硬件控制看门狗1: 软件控制看门狗</td></tr><tr><td>3:2</td><td>BOR_TH[1:0]</td><td>BOR阈值配置位00: 无BOR功能01: BOR阈值110: BOR阈值211: BOR阈值3</td></tr><tr><td>1:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

# 3.4.9. DCRP 地址寄存器（FMC_DCRPADDR_EFT）

地址偏移：0x28

复位值：0xXXXX 0XXX，出厂值为0x0000 00FF

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DCRP_EREN</td><td colspan="4">保留</td><td colspan="11">DCRP_AREA_END[10:0]</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">DCRP_AREA_START[10:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DCRP_EREN</td><td>DCRP 区域擦除使能状态位0: DCRP 不被擦除1: 当 SPC 降级或执行带清除保护的整片擦除操作时, DCRP 区域被擦除。</td></tr><tr><td>30:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:16</td><td>DCRP_AREA_END[10:0]</td><td>DCRP 区域结束地址状态位该位域包含了 DCRP 区域的最后的 4K 字节块。区域最后一个字节地址= ( DCRP_AREA_END[10:0] + 1 )* 4096 - 1 + 0x0800_0000如果 DCRP_AREA_END[10:0]等于 DCRP_AREA_START[10:0], 整个主存储闪存块都是 DCRP 区域。如果 DCRP_AREA_END[10:0]小于 DCRP_AREA_START[10:0], DCRP 区域为空。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>DCRP_AREA_START[10:0]</td><td>DCRP 区域起始地址状态位该位域包含了 DCRP 区域的起始的 4K 字节块。区域第一个字节地址= DCRP_AREA_START[10:0] * 4096 + 0x0800_0000如果 DCRP_AREA_END 等于 DCRP_AREA_START, 整个主存储闪存块都是 DCRP 区域。如果 DCRP_AREA_END 小于 DCRP_AREA_START, DCRP 区域为空。</td></tr></table>

# 3.4.10. DCRP 地址寄存器（FMC_DCRPADDR_MDF）

地址偏移：0x2C

复位值：0xXXXX 0XXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>DCRP_EREN</td><td colspan="4">保留</td><td colspan="11">DCRP_AREA_END[10:0]</td></tr><tr><td colspan="5">rw</td><td colspan="11">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">DCRP_AREA_START[10:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>DCRP_EREN</td><td>DCRP 区域擦除使能选项配置位0: DCRP 不被擦除1: 当 SPC 降级或执行带清除保护的整片擦除操作时, DCRP 被擦除。</td></tr><tr><td>30:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:16</td><td>DCRP_AREA_END[10:0]</td><td>DCRP 区域结束地址配置位该位域包含了 DCRP 区域的最后的 4K 字节块。区域最后一个字节地址= ( DCRP_AREA_END[10:0] + 1 ) * 4096 - 1 + 0x0800_0000如果 DCRP_AREA_END[10:0]等于 DCRP_AREA_START[10:0], 整个主存储闪存块都是 DCRP 区域。如果 DCRP_AREA_END[10:0]小于 DCRP_AREA_START[10:0], DCRP 区域为空。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>DCRP_AREA_START[10:0]</td><td>DCRP 区域起始地址配置位该位域包含了 DCRP 区域的起始的 4K 字节块。区域第一个字节地址= DCRP_AREA_START[10:0] * 4096 + 0x0800_0000如果 DCRP_AREA_END[10:0]等于 DCRP_AREA_START[10:0], 整个主存储闪存块都是 DCRP 区域。如果 DCRP_AREA_END[10:0]小于 DCRP_AREA_START[10:0], DCRP 区域为空。</td></tr></table>

# 3.4.11. 安全用户区域地址寄存器（FMC_SCRADDR_EFT）

地址偏移：0x30

复位值：0xXXXX 0XXX，出厂值为0x0000 00FF

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SCR_EREN</td><td colspan="4">保留</td><td colspan="11">SCR_AREA_END[10:0]</td></tr><tr><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">SCR_AREA_START[10:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SCR_EREN</td><td>安全用户区域擦除使能选项状态位0: 安全用户区域不被擦除1: 当SPC降级或执行带清除保护的整片擦除操作时,安全用户区域被擦除。</td></tr><tr><td>30:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:16</td><td>SCR_AREA_END[10:0]</td><td>安全用户区域结束地址状态位该位域包含了安全用户区域的最后的4K字节块。区域最后一个字节地址= <eq>(SCR\_AREA\_END[10:0] + 1) * 4096 - 1 + 0x0800\_0000</eq>如果 SCR_AREA_END[10:0]等于 SCR_AREA_START[10:0],整个主存储闪存块都是安全用户区域。如果 SCR_AREA_END[10:0]小于 SCR_AREA_START[10:0],安全用户区域为空。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>SCR_AREA_START[10:0]</td><td>安全用户区域起始地址状态位该位域包含了安全用户区域的起始的 4K 字节块。区域第一个字节地址= SCR_AREA_START[10:0] * 4096 + 0x0800_0000如果 SCR_AREA_END[10:0]等于 SCR_AREA_START[10:0],整个主存储闪存块都是安全用户区域。如果 SCR_AREA_END[10:0]小于 SCR_AREA_START[10:0],安全用户区域为空。</td></tr></table>

# 3.4.12. 安全用户区域地址寄存器（FMC_SCRADDR_MDF）

地址偏移：0x34

复位值：0xXXXX 0XXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>SCR_EREN</td><td colspan="4">保留</td><td colspan="11">SCR_AREA_END[10:0]</td></tr><tr><td colspan="5">rw</td><td colspan="11">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">SCR_AREA_START[10:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>SCR_EREN</td><td>安全用户区域擦除使能选项配置位0: 安全用户区域不被擦除1: 当SPC降级或执行带清除保护的整片擦除操作时,安全用户区域被擦除。</td></tr><tr><td>30:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:16</td><td>SCR_AREA_END[10:0]</td><td>安全用户区域结束地址配置位该位域包含了安全用户区域的最后的4K字节块。区域最后一个字节地址=(SCR_AREA_END[10:0]+1)*4096-1+0x0800_0000如果SCR_AREA_END等于SCR_AREA_START,整个主存储闪存块都是安全用户区域。如果SCR_AREA_END小于SCR_AREA_START,安全用户区域为空。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>SCR_AREA_START[10:0]</td><td>安全用户区域起始地址配置位该位域包含了安全用户区域的起始的4K字节块。</td></tr></table>

区域第一个字节地址= SCR_AREA_START[10:0] * 4096 + 0x0800_0000

如果 SCR_AREA_END[10:0]等于 SCR_AREA_START[10:0]，整个主存储闪存块都是安全用户区域。

如果 SCR_AREA_END[10:0]小于 SCR_AREA_START[10:0]，安全用户区域为空。

# 3.4.13. 擦除/编程保护寄存器（FMC_WP_EFT）

地址偏移：0x38

复位值：0xXXXX XXXX，出厂值为0x3FFF FFFF

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP[21:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">WP[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:0</td><td>WP[21:0]</td><td>扇区擦除/编程保护选项状态位对于 WP[21],每一位反映了对应 64 个扇区的擦除/编程保护状态。0:对应的 64 个扇区受擦除/编程保护1:对应的 64 个扇区不受擦除/编程保护对于 WP[20:16],每一位反映了对应 128 个扇区的擦除/编程保护状态。0:对应的 128 个扇区受擦除/编程保护1:对应的 128 个扇区不受擦除/编程保护对于 WP[15:0],每一位反映了对应 16 个扇区的擦除/编程保护状态。0:对应的 16 个扇区受擦除/编程保护1:对应的 16 个扇区不受擦除/编程保护</td></tr></table>

# 3.4.14. 擦除/编程保护寄存器（FMC_WP_MDF）

地址偏移：0x3C

复位值：0xXXXX XXXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="10">保留</td><td colspan="6">WP[21:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

WP[15:0] 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21:0</td><td>WP[21:0]</td><td>扇区擦除/编程保护选项配置位对于 WP[21],该位可以将对应 64 个扇区设置为擦除/编程保护。0: 将对应的 64 个扇区设置为受擦除/编程保护1: 将对应的 64 个扇区设置为不受擦除/编程保护对于 WP[20:16],每一位可以将对应 128 个扇区设置为擦除/编程保护。0: 将对应的 128 个扇区设置为受擦除/编程保护1: 将对应的 128 个扇区设置为不受擦除/编程保护对于 WP[15:0],每一位可以将对应 16 个扇区设置为擦除/编程保护。0: 将对应的 16 个扇区设置为受擦除/编程保护1: 将对应的 16 个扇区设置为不受擦除/编程保护</td></tr></table>

# 3.4.15. 引导装载地址寄存器（FMC_BTADDR_EFT）

地址偏移：0x40

复位值：0xXXXX XXXX，出厂值为0x1FF0 0800

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">BOOT_ADDR1[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BOOT_ADDR0[15:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>BOOT_ADDR1[15:0]</td><td>引导装载地址 1 状态位如果 BOOT 管脚拉高,引导装载地址的高 16 位为该字域。</td></tr><tr><td>15:0</td><td>BOOT_ADDR0[15:0]</td><td>引导装载地址 0 状态位如果 BOOT 管脚拉低,引导装载地址的高 16 位为该字域。</td></tr></table>

# 3.4.16. 引导装载地址寄存器（FMC_BTADDR_MDF）

地址偏移：0x44

复位值：0xXXXX XXXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">BOOT_ADDR1[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BOOT_ADDR0[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>BOOT_ADDR1[15:0]</td><td>引导装载地址 1 配置位.如果 BOOT 管脚拉高,引导装载地址的高 16 位为该字域。</td></tr><tr><td>15:0</td><td>BOOT_ADDR0[15:0]</td><td>引导装载地址 0 配置位.如果 BOOT 管脚拉低,引导装载地址的高 16 位为该字域。</td></tr></table>

# 3.4.17. 选项字节状态寄存器 1（FMC_OBSTAT1_EFT）

地址偏移：0x50

复位值：0xXXXX 0XXX，出厂值为0x0000 0087

该寄存器是相应选项位的生效值。复位后装载选项字节中的值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[15:0]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">DTCM_SZ_SHRRAM[3:0]</td><td colspan="4">ITCM_SZ_SHRRAM[3:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>DATA[15:0]</td><td>用户定义选项字节状态位</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td rowspan="9">7:4</td><td rowspan="9">DTCM_SZ_SHRRAM[3:0]</td><td>共享 RAM 中的 DTCM 大小状态位</td></tr><tr><td>DTCM + ITCM 大小不能超过 512KB 字节</td></tr><tr><td>0000: 0 字节 DTCM</td></tr><tr><td>0001~0110: 保留</td></tr><tr><td>0111: 64-KB DTCM</td></tr><tr><td>1000: 128-KB DTCM</td></tr><tr><td>1001: 256-KB DTCM</td></tr><tr><td>1010: 512-KB DTCM</td></tr><tr><td>1011~1111: 保留</td></tr><tr><td rowspan="3">3:0</td><td rowspan="3">ITCM_SZ_SHRRAM[3:0]</td><td>共享 RAM 中的 ITCM 大小状态位</td></tr><tr><td>DTCM + ITCM 大小不能超过 512KB 字节</td></tr><tr><td>0000: 0 字节 ITCM</td></tr></table>

0001~0110：保留

0111：64-KB ITCM 

1000：128-KB ITCM 

1001：256-KB ITCM 

1010：512-KB ITCM 

1011~1111：保留

# 3.4.18. 选项字节状态寄存器 1（FMC_OBSTAT1_MDF）

地址偏移：0x54

复位值：0xXXXX 0XXX

该寄存器是相应选项位的修改值。系统复位后的值是相应选项位的生效值。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[15:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">DTCM_SZ_SHRRAM[3:0]</td><td colspan="4">ITCM_SZ_SHRRAM[3:0]</td></tr></table>

<table><tr><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>DATA[15:0]</td><td>用户定义选项字节配置位</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>DTCM_SZ_SHRRAM[3:0]</td><td>共享RAM中的DTCM大小配置位DTCM + ITCM大小不能超过512KB字节0000: 0字节DTCM0001~0110: 保留0111: 64-KB DTCM1000: 128-KB DTCM1001: 256-KB DTCM1010: 512-KB DTCM1011~1111: 保留</td></tr><tr><td>3:0</td><td>ITCM_SZ_SHRRAM[3:0]</td><td>共享RAM中的ITCM大小配置位DTCM + ITCM大小不能超过512KB字节0000: 0字节ITCM0001~0110: 保留0111: 64-KB ITCM1000: 128-KB ITCM1001: 256-KB ITCM1010: 512-KB ITCM1011~1111: 保留</td></tr></table>

# 3.4.19. NO-RTDEC 区域寄存器（FMC_NODEC）

地址偏移：0x60

复位值：0x0000 00FF

当LK位设置为0时，该寄存器才能被访问，只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留</td><td colspan="11">NODEC_AREA_END[10:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td colspan="11">NODEC_AREA_START[10:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26:16</td><td>NODEC_AREA_END[10:0]</td><td>NO-RTDEC 区域结束地址该位域包含了 NO-RTDEC 区域的最后的 4K 字节块。区域最后一字节地址= NODEC_AREA_END[10:0] * 4096 - 1 + 0x0800_0000。如果 NODEC_AREA_END[10:0]等于 NODEC_AREA_START[10:0],整个主存储闪存块在读操作时都不解密。如果 DCRP_AREA_END[10:0]小于 DCRP_AREA_START[10:0],整个主存储闪存块在读操作时都解密。</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10:0</td><td>NODEC_AREA_START[10:0]</td><td>NO-RTDEC 区域起始地址该位域包含了 NO-RTDEC 区域的起始的 4K 字节块。最后一字节地址= NODEC_AREA_START [10:0] * 4096 + 0x0800_0000。如果 NODEC_AREA_END[10:0]等于 NODEC_AREA_START[10:0],整个主存储闪存块在读操作时都不解密。如果 DCRP_AREA_END[10:0]小于 DCRP_AREA_START[10:0],整个主存储闪存块在读操作时都解密。</td></tr></table>

# 3.4.20. AES 初始向量寄存器 x（FMC_AESIVx_EFT）（x = 0…2）

地址偏移：0x68 + 0x4 * x

复位值：0xXXXX XXXX

该寄存器是AES初始向量高96位的生效值。AES初始向量不是选项字节，而是存放在非易失性AES IV存储区内，复位后从该区域中装载。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">AESIV[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

AESIV[15:0] 

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>AESIV[31:0]</td><td>AES 初始向量状态位128 位的 AES 初始向量 AES_IV[127:0] = AESIV[95:0] || 12&#x27;b0 || 读地址[23:4]。其中,96 位的 AESIV[95:0]按照 AESIV2 || AESIV1 || AESIV0 的顺序组成。</td></tr></table>

# 3.4.21. AES 初始向量寄存器 x（FMC_AESIVx_MDF）（x = 0…2）

地址偏移：0x74 + 0x4 * x

复位值：0x0000 0000

该寄存器是AES初始向量高96位的修改值。

当LK位设置为0时，该寄存器才能被访问，只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">AESIV[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AESIV[15:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>AESIV[31:0]</td><td>AES 初始向量配置位128 位的 AES 初始向量 AES_IV[127:0] = AESIV[95:0] || 12&#x27;b0 || 读地址[23:4]。其中,96 位的 AESIV[95:0]按照 AESIV2 || AESIV1 || AESIV0 的顺序组成。在初始向量写入 FMC_AESIV2_MDF 寄存器后,FMC_ASIV0/1/2_MDF 寄存器中的值都将被更新至 AES 初始向量区域中,且 BUSY 位自动置 1。当更新完成后,BUSY 位自动清 0。注意:在写入 FMC_AESIV2_MDF 之前,用户需要确保没有编程、擦除或选项字节修改操作在进行。否则,FMC_AESIV2_MDF 寄存器无法被写入,更新操作也不会进行。</td></tr></table>

# 3.4.22. 产品 ID 寄存器 x（FMC_PIDx）（x = 0，1）

地址偏移：0x100 + 0x4 * x

复位值：0xXXXX XXXX

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">PID[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PID[15:0]</td></tr></table>

r 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>PID[31:0]</td><td>产品保留 ID 寄存器该寄存器为只读上电后这些位始终不会改变,该寄存器在生产过程中被一次性编程。</td></tr></table>
