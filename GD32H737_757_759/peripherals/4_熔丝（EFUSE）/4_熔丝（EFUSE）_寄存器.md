# 4.4. EFUSE 寄存器

EFUSE 基地址：0x4002 2800

# 4.4.1. 控制寄存器（EFUSE_CTL）

地址偏移：0x00

复位值：0x7E00 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">AES_KEY_CRC</td><td colspan="4">保留</td><td>PVIE</td><td>RDIE</td><td>PGIE</td><td>IAERRIE</td></tr><tr><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>MPVEN</td><td colspan="13">保留</td><td>EFRW</td><td>EFSTR</td></tr><tr><td>rw</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>AES_KEY_CRC</td><td>AES秘钥的8位CRC计算结果值该位域用于验证EFUSE_AES_KEYx寄存器中的值或熔丝中存储的AES秘钥值。CRC计算是使用标准CRC-8-CCITT算法X8+X2+X+1的8位校验和。如果AESEN为0,则有两种情况将计算AES秘钥的CRC值,并将CRC计算结果存储到此位字段中:(1)将16字节的AES秘钥连续写入偏移地址为0x24、0x28、0x2C和0x30的EFUSE_AES_KEYx寄存器。CRC计算结果将在写入EFUSE_AES_KEY3寄存器(偏移地址0x30)后生成。(2)系统复位后,由MCU从熔丝中自动读出AES值。CRC计算结果将在系统复位完成从熔丝中读出全部AES值后生成。</td></tr><tr><td>23:20</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>19</td><td>PVIE</td><td>编程电压设置错误中断使能位0:失能编程电压设置错误中断1:使能编程电压设置错误中断</td></tr><tr><td>18</td><td>RDIE</td><td>读操作完成中断使能位0:失能读操作完成中断1:使能读操作完成中断</td></tr><tr><td>17</td><td>PGIE</td><td>写操作完成中断使能位0:失能写操作完成中断1:使能写操作完成中断</td></tr><tr><td>16</td><td>IAERRIE</td><td>非法访问错误中断使能位0:失能非法访问错误中断1:使能非法访问错误中断</td></tr></table>

当EFUSE_CTL寄存器中的EFSTR位为1时，该位不可写。

15 MPVEN 监控编程电压功能使能位

0：失能监控编程电压功能

1：使能监控编程电压功能

当EFUSE_CTL寄存器中的EFSTR位为1时，该位不可写。

14:2 保留 必须保持复位值。

1 EFRW 熔丝读写操作选择位

0：读熔丝内容

1：写熔丝内容

当EFUSE_CTL寄存器中的EFSTR位为1时，该位不可写。

0 EFSTR 发送熔丝读/写操作命令位

该位由软件置1，硬件清0

0：无影响

1：开始读/写操作

# 4.4.2. 地址寄存器（EFUSE_ADDR）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>保留</td><td colspan="5">EFSIZE[4:0]</td><td colspan="10">EFADDR[9:0]</td></tr><tr><td colspan="6">rw</td><td colspan="10">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:15</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>14:10</td><td>EFSIZE[4:0]</td><td>读/写熔丝数据大小数据大小的单位是字节。当EFUSE_CTL寄存器中的EFSTR位为1时,该位域不可写。</td></tr><tr><td>9:0</td><td>EFADDR[9:0]</td><td>读/写熔丝数据起始地址EFADDR[9]必须设置为0,因为用户无法访问地址超过512的位的数据,否则EFUSE_STAT寄存器中的IAERRIF位将会置位。当EFUSE_CTL寄存器中的EFSTR位为1时,该位域不可写。</td></tr></table>

# 4.4.3. 状态寄存器（EFUSE_STAT）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="11">保留</td><td>LDO_RDY</td><td>PVIF</td><td>RDIF</td><td>PGIF</td><td>IAERRIF</td></tr><tr><td colspan="11"></td><td>r</td><td>r</td><td>r</td><td>r</td><td>r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>LDO_RDY</td><td>熔丝LDO准备完成信号0:LDO未准备完成1:LDO准备完成注意:不论LDO旁路模式是否使能,该信号都有效。该位在编程开始前由硬件自动置1,在编程完成后由硬件自动清0。</td></tr><tr><td>3</td><td>PVIF</td><td>编程电压设置错误标志位0:编程电压设置在正确范围内1:编程电压未设置在正确范围内</td></tr><tr><td>2</td><td>RDIF</td><td>读操作完成标志位0:读操作未完成1:读操作完成</td></tr><tr><td>1</td><td>PGIF</td><td>写操作完成标志位0:写操作未完成1:写操作完成</td></tr><tr><td>0</td><td>IAERRIF</td><td>非法访问错误标志位0:未发生非法访问错误(越界或访问锁定参数)1:发生非法访问错误(越界或访问锁定参数)</td></tr></table>

# 4.4.4. 状态标志清除寄存器（EFUSE_STATC）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td>PVIC</td><td>RDIC</td><td>PGIC</td><td>IAERRIC</td></tr></table>

rc_w1 rc_w1 rc_w1 rc_w1 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>PVIC</td><td>编程电压设置错误中断标志清除位0:无影响1:清除编程电压设置错误中断标志位</td></tr><tr><td>2</td><td>RDIC</td><td>读操作完成中断标志清除位0:无影响1:清除读操作完成中断标志位</td></tr><tr><td>1</td><td>PGIC</td><td>写操作完成中断标志清除位0:无影响1:清除写操作完成中断标志位</td></tr><tr><td>0</td><td>IAERRIC</td><td>非法访问错误中断标志清除位0:无影响1:清除非法访问错误中断标志位</td></tr></table>

# 4.4.5. 用户控制寄存器（EFUSE_USER_CTL）

地址偏移：0x14

复位值：0xXXXX XXXX，复位后装载熔丝存储单元中的值。

寄存器可读。只有当 SCRLK 位为 0 时，用户才能写入该寄存器的高 16 位。只有当 UCLK 位为 0 时，用户才能写入该寄存器的低位 16 位。但除非成功执行熔丝写操作，否则该寄存器中所有位的修改将不会存至熔丝中。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">SCR_AREA_END[7:0]</td><td colspan="8">SCR_AREA_START[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>SCR</td><td>SPC_H</td><td>SPC_L</td><td>JTAGNSW</td><td colspan="2">NDBG</td><td colspan="3">保留</td><td>UDLK</td><td>AESEN</td><td>UCLK</td><td>SCRLK</td><td>DPLK</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td colspan="3"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>SCR_AREA_END[7:0]</td><td>安全用户区域结束地址该位域出厂值为0。该位域包含了安全用户区域的最后的32K字节块。安全用户区域在熔丝中以32K字节的粒度定义。区域最后一个字节地址=(SCR_AREA_END[7:0]+1)*32768-1+0x0800_0000如果SCR_AREA_END[7:0]及SCR_AREA_START[7:0]都为0,则安全用户区域未定义。如果SCR_AREA_END[7:0]等于SCR_AREA_START[7:0]且不为0,整个主存储闪存块都是安全用户区域。</td></tr></table>

如果SCR_AREA_END[7:0]小于SCR_AREA_START[7:0]，安全用户区域为空。安全用户区域地址配置详见 3-6. 。

<table><tr><td>23:16</td><td>SCR_AREA_START[7:0]</td><td>安全用户区域起始地址该位域出厂值为0。该位域包含了安全用户区域的起始的32K字节块。安全用户区域在熔丝中以32K字节的粒度定义。区域最后一个字节地址= SCR_AREA_END[7:0] * 32768 - 1 + 0x0800_0000如果SCR_AREA_END[7:0]及SCR_AREA_START[7:0]都为0,则安全用户区域未定义。如果SCR_AREA_END[7:0]等于SCR_AREA_START[7:0]且不为0,整个主存储闪存块都是安全用户区域。如果SCR_AREA_END[7:0]小于SCR_AREA_START[7:0],安全用户区域为空。安全用户区域地址配置详见表3-6. 安全用户区域配置。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>SCR</td><td>安全模式使能该位出厂值为0。0:失能安全模式。1:使能安全模式。注意:只要该位或选项字节中的SCR位为1,安全模式就将启用。</td></tr><tr><td>12</td><td>SPC_H</td><td>将安全保护等级配置为保护等级高该位出厂值为0。如果熔丝中的SPC_H和SPC_L位都为1,则SPC为保护等级高。安全保护等级配置详见表3-4. SPC保护等级配置。</td></tr><tr><td>11</td><td>SPC_L</td><td>将安全保护配置为保护等级低该位出厂值为0。注意:如果熔丝中的SPC_L设置为1,则禁止SPC保护等级低到无保护状态的降级。如果熔丝中的SPC_H和SPC_L位都为1,则SPC为保护等级高。安全保护等级配置详见表3-4. SPC保护等级配置。</td></tr><tr><td>10</td><td>JTAGNSW</td><td>SW或JTAG调试器选择该位出厂值为0。0:SW1:JTAG注意:当NDBG[1:0]选择为无调试功能时,JTAGNSW位无效,调试功能关闭。</td></tr><tr><td>9:8</td><td>NDBG[1:0]</td><td>调试权限设置该位出厂值为0。00:普通JTAG(仅在JTAGNSW为1时有效,否则为SW调试)01:安全JTAG(仅在JTAGNSW为1时有效,否则为SW调试)10~11:无调试功能(无论JTAGNSW取值,调试功能都关闭)</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>UDLK</td><td>EFUSE_USER_DATAx寄存器锁定位该位出厂值为0。0:解锁EFUSE_USER_DATAx寄存器,寄存器内容可以被修改1:锁定EFUSE_USER_DATAx寄存器,寄存器内容不可以被修改</td></tr><tr><td>3</td><td>AESEN</td><td>EFUSE_AES_KEYx寄存器锁定及AES加解密功能使能位该位出厂值为0。0:失能AES加解密功能,EFUSE_AES_KEYx寄存器可以写数据1:使能AES加解密功能并锁定EFUSE_AES_KEYx寄存器,寄存器内容不可改写</td></tr><tr><td>2</td><td>UCLK</td><td>EFUSE_USER_CTL寄存器低16位锁定位该位出厂值为0。0:解锁EFUSE_USER_CTL寄存器中的低16位,寄存器低16位可以被修改1:锁定EFUSE_USER_CTL寄存器中的低16位,寄存器低16位不可被修改UCLK位置1后,EFUSE_USER_CTL寄存器中的其他锁定位将无法进行修改,用户需要对该位谨慎操作。注意:当UCLK位为1时,如果想要修改熔丝中用户控制段的高16位,起始地址必须设置为10'd16(此时EFSIZE[4:0]=1或2)或10'd24(此时EFSIZE[4:0]只能设置为1)。否则会产生非法访问错误。</td></tr><tr><td>1</td><td>SCRLK</td><td>安全区域地址锁存位该位出厂值为0。0:解锁EFUSE_USER_CTL寄存器中的高16位,寄存器高16位可以被修改1:锁定EFUSE_USER_CTL寄存器中的高16位,寄存器高16位不可被修改注意:当SCRLK位为1时,如果想要修改熔丝中用户控制段的低16位,起始地址必须设置为10'd0(此时EFSIZE[4:0]=1或2)或10'd8(此时EFSIZE[4:0]只能设置为1)。否则会产生非法访问错误。</td></tr><tr><td>0</td><td>DPLK</td><td>EFUSE_DPx寄存器锁定位该位出厂值为0。0:解锁EFUSE_DPx寄存器,寄存器内容可读可写。1:锁定EFUSE_DPx寄存器,寄存器内容不可写。该位为1时,只有当JTAGNSW位为1,且NDBG[1:0]位为2b'01或2b'11时,寄存器不可读。其他情况下,寄存器可读。</td></tr></table>

# 4.4.6. MCU 保留寄存器（EFUSE_MCU_RSV）

地址偏移：0x18

复位值：0xXXXX XXXX，复位后装载熔丝存储单元中的值。

寄存器可读。只有当DCRPLK位为0时，用户才能写入该寄存器的高16位。只有当MCURSVLK位为 0 时，用户才能写入该寄存器的低位 16 位。但除非成功执行熔丝写操作，否则该寄存器中所有位的修改将不会存至熔丝中。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DCRP_AREA_END[7:0]</td><td colspan="8">DCRP_AREA_START[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>MCU_RSV[5:0]</td><td>DCRPLK</td><td>MCURSVLK</td><td>VFIMG</td><td>DISLFI</td><td>保留</td><td>AESNCAU</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DCRP_AREA_END[7:0]</td><td>DCRP区域结束地址该位域出厂值为0。该位域包含了DCRP区域的最后的32K字节块。DCRP区域在熔丝中以32K字节的粒度定义。区域最后一个字节地址=(DCRP_AREA_END[7:0]+1)*32768-1+0x0800_0000如果DCRP_AREA_END[7:0]及DCRP_AREA_START[7:0]都为0,则DCRP区域未定义。如果DCRP_AREA_END[7:0]等于DCRP_AREA_START[7:0]且不为0,整个主存储闪存块都是DCRP区域。如果DCRP_AREA_END[7:0]小于DCRP_AREA_START[7:0],DCRP区域为空。DCRP地址配置详见表3-5.DCRP区域配置。</td></tr><tr><td>23:16</td><td>DCRP_AREA_START[7:0]</td><td>DCRP区域起始地址该位域出厂值为0。该位域包含了DCRP区域的起始的32K字节块。DCRP区域在熔丝中以32K字节的粒度定义。如果DCRP_AREA_END[7:0]及DCRP_AREA_START[7:0]都为0,则DCRP区域未定义。如果SCR_AREA_END[7:0]等于SCR_AREA_START[7:0]且不为0,整个主存储闪存块都是DCRP区域。如果SCR_AREA_END[7:0]小于SCR_AREA_START[7:0],DCRP访问区域为空。DCRP地址配置详见表3-5.DCRP区域配置。</td></tr><tr><td>15:10</td><td>MCU_RSV[5:0]</td><td>熔丝MCU保留数据该位域出厂值为0。</td></tr><tr><td>9</td><td>DCRPLK</td><td>DCRP区域地址锁存位该位出厂值为0。0:解锁EFUSE_MCU_RSV寄存器中的高16位,寄存器高16位可以被修改1:锁定EFUSE_MCU_RSV寄存器中的高16位,寄存器高16位不可被修改注意:当DCRPLK位为1时,如果想要修改熔丝中MCU保留段的低16位,起始地址必须设置为10&#x27;d32(此时EFSIZE[4:0]=1或2)或10&#x27;d40(此时EFSIZE[4:0]只能设置为1)。否则会产生非法访问错误。</td></tr><tr><td>8</td><td>MCURSVLK</td><td>EFUSE_MCU_RSV寄存器低16位锁定位该位出厂值为0。0:解锁EFUSE_MCU_RSV寄存器中的低16位,寄存器低16位可以被修改1:锁定EFUSE_MCU_RSV寄存器中的低16位,寄存器低16位不可被修改MCURSVLK位置1后,EFUSE_MCU_RSV寄存器中的其他锁定位将无法进行修改,用户需要对该位谨慎操作。</td></tr></table>

注意：当MCURSVLK位为1时，如果想要修改熔丝中MCU保留段的高16位，起始地址必须设置为10'd48（此时EFSIZE[4:0]= 1或2）或10'd56（此时EFSIZE[4:0]需设置为1）。否则会产生非法访问错误。

<table><tr><td>7</td><td>VFIMG</td><td>验证固件镜像使能位该位出厂值为0。0:失能固件镜像认证功能1:使能固件镜像认证功能</td></tr><tr><td>6</td><td>DISLFI</td><td>授权固件安装功能设置该位出厂值为0。0:使能授权固件安装1:失能授权固件安装</td></tr><tr><td>5:1</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>0</td><td>AESNCAU</td><td>用于CAU的AES秘钥配置位该位出厂值为0。0:AES秘钥用于CAU1:AES秘钥不用于CAU</td></tr></table>

# 4.4.7. 调试秘钥寄存器（EFUSE_DPx）（x = 0，1）

地址偏移： $0 { \times } 1 { \mathsf C } + 0 { \times } 4 ^ { \star } \mathsf X$ 

复位值：0xXXXX XXXX，复位后装载熔丝存储单元中的值。

当 JTAGNSW = 1，且 NDBG[1:0] = 2b’01 或 2b’11 时，该参数作为调试验证秘钥，用于调试服务。否则，该参数将被用作用户数据使用。

作为调试密钥时：仅当 DPLK 位为 0 时，寄存器才可读。仅当 DPLK 位为 0 时，寄存器可写。但除非成功执行熔丝写操作，否则该寄存器中所有位的修改将不会存至熔丝中。

作为用户数据时：无论 DPLK 位为 0 或 1，寄存器都可读。仅当 DPLK 位为 0 时，寄存器可写。但除非成功执行熔丝写操作，否则该寄存器中所有位的修改将不会存至熔丝中。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DP[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DP[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DP[31:0]</td><td>熔丝中调试秘钥字段值该位域出厂值为0。</td></tr></table>

# 4.4.8. 固件 AES 秘钥寄存器 （EFUSE_AES_KEYx）（x = 0…3）

地址偏移：0x24 + 0x4 * x

复位值：0xXXXX XXXX，复位后装载熔丝存储单元中的值。

寄存器不可读。只有当 AESEN 位为 0 时，寄存器可写。但除非成功执行熔丝写操作，否则该寄存器中所有位的修改将不会存至熔丝中。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">AESKEY[31:16]</td></tr><tr><td colspan="16">w</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">AESKEY[15:0]</td></tr></table>

w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>AESKEY[31:0]</td><td>熔丝中AES秘钥字段值该位域出厂值为0。用户必须将完整的16字节AESKEY[127:0]连续写入EFUSE_AES_KEYx寄存器。该寄存器只能按照字(32位)写访问,每个寄存器中的4个字节是按照由低字节到高字节的顺序存储的(即AESKEY的低字节对应寄存器的低位)。同时,AESKEY[31:0]写入EFUSE_AES_KEY0寄存器(偏移地址0x24),AESKEY[63:32]写入EFUSE_AES_KEY1寄存器(偏移地址0x28),AESKEY[95:64]写入EFUSE_AES_KEY2寄存器(偏移地址0x2C),AESKEY[127:96]写入EFUSE_AES_KEY3寄存器(偏移地址0x30)。CRC计算结果将在写入EFUSE_AES_KEY3寄存器(偏移地址0x30)后生成。</td></tr></table>

# 4.4.9. 用户数据寄存器 （EFUSE_USER_DATAx）（x = 0…3）

地址偏移：0x34 + 0x4 * x

复位值：0xXXXX XXXX，复位后装载熔丝存储单元中的值。

寄存器可读。只有当 UDLK 位为 0 时，寄存器可写。但修改后的寄存器值不会存储在熔丝中，除非成功执行熔丝写操作。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">USERDATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">USERDATA[15:0]</td></tr></table>

rw 

位/位域 名称 描述

31:0 

USERDATA[31:0] 

熔丝中用户自定义数据字段值

该位域出厂值为0。
