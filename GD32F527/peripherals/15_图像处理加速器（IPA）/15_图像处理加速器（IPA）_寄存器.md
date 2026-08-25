## 15.6. IPA 寄存器

IPA基地址：0x4002 B000

## 15.6.1. 控制寄存器（IPA_CTL）

偏移地址：0x00

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留</td><td colspan="2">PFCM[1:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td>WCFIE</td><td>LLFIE</td><td>LACIE</td><td>TLMIE</td><td>FTFIE</td><td>TAEIE</td><td colspan="5">保留</td><td>TST</td><td>THU</td><td>TEN</td></tr><tr><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td><td>rs</td><td>rw</td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:16</td><td>PFCM[1:0]</td><td>像素格式转换模式软件置位和清除.00:前景层存储区到目标存储区无像素格式转换01:前景层存储区到目标存储区有像素格式转换10:混合前景层和背景层存储区到目标存储区11:用特定的颜色填充目标存储区当TEN为‘1’时,该位不可写。</td></tr><tr><td>15:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13</td><td>WCFIE</td><td>配置错误中断使能位软件置位和清除0:配置错误中断禁止1:配置错误中断使能</td></tr><tr><td>12</td><td>LLFIE</td><td>LUT加载完成中断使能位软件置位和清除0:LUT加载完成中断禁止1:LUT加载完成中断使能</td></tr><tr><td>11</td><td>LACIE</td><td>LUT访问冲突中断使能位软件置位和清除0:LUT访问冲突中断禁止1:LUT访问冲突中断使能</td></tr><tr><td>10</td><td>TLMIE</td><td>传输行标记中断使能位软件置位和清除0:传输行标记中断禁止1:传输行标记中断使能</td></tr><tr><td>9</td><td>FTFIE</td><td>传输完成中断使能位软件置位和清除0:传输完成中断禁止1:传输完成中断使能</td></tr><tr><td>8</td><td>TAEIE</td><td>传输访问错误中断使能位软件置位和清除0:传输访问错误中断禁止1:传输访问错误中断使能</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>TST</td><td>传输停止软件置位,软件和硬件清除0:无影响1:停止当前的传输当该位使能后,当前传输停止。当当前传输停止后,该位立即被硬件自动清0。</td></tr><tr><td>1</td><td>THU</td><td>传输挂起软件置位,软件和硬件清除.0:无影响1:挂起当前传输当该位使能后,当前传输暂停。当该位清0后,当前传输继续。当当前传输被停止时,该位立即被硬件自动清0。</td></tr><tr><td>0</td><td>TEN</td><td>传输使能软件置位,硬件清除0:传输禁止1:传输使能当该位使能后,IPA传输开始。当下述情况之一发生时,该位自动清0。- 使能TST位停止当前传输- 传输完全完成- 检测到配置错误或传输访问错误- 前景层LUT或背景层LUT正在自动加载(IPA_FPCTL寄存器的FLLEN或IPA_BPCTL寄存器的BLLEN位为‘1’)</td></tr></table>

## 15.6.2. 中断状态寄存器（IPA_INTF）

偏移地址：0x04

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>WCFIF</td><td>LLFIF</td><td>LACIF</td><td>TLMIF</td><td>FTFIF</td><td>TAEIF</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>WCFIF</td><td>配置错误中断标志硬件置位,软件置位IPA_INTC 寄存器的‘WCFIFC’位清除该位。0:当IPA传输完成或LUT加载使能时,没检测到配置错误1:当IPA传输完成或LUT加载使能时,检测到配置错误</td></tr><tr><td>4</td><td>LLFIF</td><td>LUT加载完成中断标志LUT硬件置位,软件置位IPA_INTC 寄存器的‘LLFIFC’位清除该位。0:没检测到LUT加载完成1:检测到一个LUT加载完成</td></tr><tr><td>3</td><td>LACIF</td><td>LUT访问冲突中断标志位硬件置位,软件置位IPA_INTC 寄存器的‘LACIFC’位清除该位。0:没检测到LUT访问冲突1:检测到一个LUT访问冲突</td></tr><tr><td>2</td><td>TLMIF</td><td>传输行标记中断标志硬件置位,软件置位IPA_INTC 寄存器的‘CTCLIF’位清除该位。0:传输的像素数目,没有准确的达到标记行1:传输的像素数目,准确的达到标记行</td></tr><tr><td>1</td><td>FTFIF</td><td>传输完成中断标志硬件置位,软件置位IPA_INTC 寄存器的‘CTFIF’位清除该位。0:没检测到传输完成1:检测到传输完成</td></tr><tr><td>0</td><td>TAEIF</td><td>传输访问错误中断标志硬件置位,软件置位IPA_INTC 寄存器的‘CTEIF’位清除该位。0:没检测到传输访问错误1:检测到传输访问错误</td></tr></table>

## 15.6.3. 中断标志清除寄存器（IPA_INTC）

偏移地址：0x08

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>WCFIFC</td><td>LLFIFC</td><td>LACIFC</td><td>TLMIFC</td><td>FTFIFC</td><td>TAEIFC</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>WCFIFC</td><td>配置错误中断标志清除位软件置位,硬件清除0:无影响1:清除配置错误中断标志</td></tr><tr><td>4</td><td>LLFIFC</td><td>LUT加载完成中断标志清除位软件置位,硬件清除0:无影响1:清除LUT加载完成中断标志</td></tr><tr><td>3</td><td>LACIFC</td><td>LUT访问冲突中断标志清除位软件置位,硬件清除0:无影响1:清除LUT访问冲突中断标志</td></tr><tr><td>2</td><td>TLMIFC</td><td>传输行标记中断标志清除位软件置位,硬件清除0:无影响1:清除传输行标记中断标志</td></tr><tr><td>1</td><td>FTFIFC</td><td>传输完成中断标志清除位软件置位,硬件清除0:无影响1:清除传输完成中断标志</td></tr><tr><td>0</td><td>TAEIFC</td><td>传输访问错误中断标志清除位软件置位,硬件清除0:无影响1:清除传输访问错误中断标志</td></tr></table>

## 15.6.4. 前景层存储区基地址寄存器（IPA_FMADDR）

偏移地址：0x0C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">FMADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>FMADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FMADDR[31:0]</td><td>前景层存储区基地址这些位必须是8位,16位,32位对齐,具体对齐方式与前景层像素格式相对应。如果前景层像素格式是ARGB8888,这些位必须是32位对齐,如果前景层像素格式是RGB565, ARGB1555, ARGB4444或AL88,这些位必须是16位对齐,如果违背以上对齐规则,当传输使能时,将产生配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.5. 前景层行偏移寄存器（IPA_FLOFF）

偏移地址：0x10

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">FLOFF[13:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13:0</td><td>FLOFF[13:0]</td><td>前景层行偏移该位表明当前行最后一个像素和下一行第一个像素之间的像素数目。如果前景层像素格式是A4或L4,FLOFF 必须被配置成一个偶数,否则当传输使能的时候将检测到一个配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.6. 背景层存储区基地址寄存器（IPA_BMADDR）

偏移地址：0x14

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">BMADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BMADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>BMADDR[31:0]</td><td>背景层存储区基地址这些位必须是8位,16位,32位对齐,具体对齐方式与背景层像素格式相对应。如果背景层像素格式是ARGB8888,这些位必须是32位对齐,如果背景层像素格式是RGB565, ARGB1555, ARGB4444或AL88,这些位必须是16位对齐,如果违背以上对齐规则,当传输使能时,将产生配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.7. 背景层行偏移寄存器（IPA_BLOFF）

偏移地址：0x18

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">BLOFF[13:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13:0</td><td>BLOFF[13:0]</td><td>背景层行偏移该位表明当前行最后一个像素和下一行第一个像素之间的像素数目。如果背景层像素格式是A4或L4,BLOFF 必须被配置成一个偶数,否则当传输使能的时候将检测到一个配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.8. 前景层像素控制寄存器（IPA_FPCTL）

偏移地址：0x1C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">FPDAV[7:0]</td><td colspan="6">保留</td><td colspan="2">FAVCA[1:0]</td></tr><tr><td colspan="14">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">FCNP[7:0]</td><td colspan="2">保留</td><td>FLLEN</td><td>FLPF</td><td colspan="4">FPF[3:0]</td></tr><tr><td colspan="8">rw</td><td colspan="2">rc_w1</td><td colspan="2">rw</td><td colspan="4">rw</td></tr></table>

<table><tr><td>31:24</td><td>FPDAV[7:0]</td><td>前景层预定义alpha通道值软件置位和清除该位域预定义前景层的alpha通道值。该位域结合从前景层存储区或前景层LUT读取的alpha数据根据前景层alpha计算算法计算前景层的alpha通道值。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:16</td><td>FAVCA[1:0]</td><td>前景层alpha值计算算法软件置位和清除00:无影响01:FPDAV[7:0]被选作前景层alpha通道值10:FPDAV[7:0]乘以从前景层存储区或前景层LUT读取的alpha数据除以255作为前景层alpha通道值。11:保留当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>15:8</td><td>FCNP[7:0]</td><td>前景层 LUT 像素数目软件置位和清除前景层LUT的像素数目等于FCNP + 1.当FLLEN为‘1’时,该位不可写。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>FLLEN</td><td>前景层 LUT加载使能软件置位,硬件清除0:禁止前景层 LUT 加载1:使能前景层 LUT 加载当该位使能,前景层LUT自动加载开始,当下述情况之一发生时,该位自动清0-使能TST位停止当前传输-前景层LUT自动加载完成-检测到配置错误或传输错误-IPA传输或背景层LUT自动加载正在进行</td></tr><tr><td>4</td><td>FLPF</td><td>前景层LUT像素格式软件置位和清除0:ARGB88881:RGB888当FLLEN为‘1’时,该位不可写。</td></tr><tr><td>3:0</td><td>FPF[3:0]</td><td>前景层像素格式软件置位和清除0000:ARGB88880001:RGB8880010:RGB5650011:ARGB15550100:ARGB44440101:L8</td></tr></table>

当IPA_CTL寄存器的TEN位为‘1’时，该位不可写。

## 15.6.9. 前景层像素值寄存器（IPA_FPV）

偏移地址：0x20

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">FPDRV[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">FPDGV[7:0]</td><td colspan="8">FPDBV[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>FPDRV[7:0]</td><td>前景层预定义红色值当前景层像素格式是A4或A8时,该位域被用作前景层红色值。当IPA_CTL寄存器的TEN位为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>15:8</td><td>FPDGV[7:0]</td><td>前景层预定义绿色值当前景层像素格式是A4或A8时,该位域被用作前景层绿色值。当IPA_CTL寄存器的TEN位为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>7:0</td><td>FPDBV[7:0]</td><td>前景层预定义蓝色值当前景层像素格式是A4或A8时,该位域被用作前景层蓝色值。当IPA_CTL寄存器的TEN位为&#x27;1&#x27;时,该位不可写。</td></tr></table>

## 15.6.10. 背景层像素控制寄存器（IPA_BPCTL）

偏移地址：0x24

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">BPDAV[7:0]</td><td colspan="6">保留</td><td colspan="2">BAVCA[1:0]</td></tr><tr><td colspan="14">rw</td><td colspan="2">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>BCNP[7:0]</td><td>保留</td><td>BLLEN</td><td>BLPF</td><td>BPF[3:0]</td></tr><tr><td>rw</td><td>rc_w1</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>BPDAV[7:0]</td><td>背景层预定义alpha通道值软件置位和清除该位域预定义背景层的alpha通道值。该位域结合从背景层存储区和背景层LUT读取的alpha数据根据背景层alpha计算算法计算背景层alpha通道值。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>23:18</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>17:16</td><td>BAVCA[1:0]</td><td>背景层alpha值计算算法软件置位和清除00:无影响01:BPDAV [7:0] 被选作背景层alpha值10:BPDAV [7:0] 乘以从背景层存储区或背景层LUT读取的alpha数据除以255作为背景层alpha值。11:保留当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>15:8</td><td>BCNP[7:0]</td><td>背景层LUT像素数目软件置位和清除背景层LUT的像素数目等于BCNP + 1.当BLLEN为‘1’时,该位不可写。</td></tr><tr><td>7:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>BLLEN</td><td>背景层LUT加载使能软件置位,硬件清除.0:禁止背景层LUT加载1:使能背景层LUT加载当该位使能,背景层LUT加载开始,当下述情况之一发生时,该位自动清0。-使能TST停止当前传输-背景层 LUT加载完成-检测到配置错误或传输错误IPA传输或背景层LUT自动加载正在进行</td></tr><tr><td>4</td><td>BLPF</td><td>背景层LUT像素格式软件置位和清除0:ARGB88881:RGB888当BLLEN为‘1’时,该位不可写。</td></tr><tr><td>3:0</td><td>BPF[3:0]</td><td>背景层像素格式软件置位和清除0000:ARGB8888</td></tr></table>

## 15.6.11. 背景层像素值寄存器（IPA_BPV）

偏移地址：0x28

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td colspan="8">BPDRV[7:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">BPDGV[7:0]</td><td colspan="8">BPDBV[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>BPDRV[7:0]</td><td>背景层预定义红色值当背景层像素格式是A4或A8时,该位域被用作背景层红色值。当IPA_CTL寄存器的TEN为‘1’时,该位不可写。</td></tr><tr><td>15:8</td><td>BPDGV[7:0]</td><td>背景层预定义绿色值当背景层像素格式是A4或A8时,该位域被用作背景层绿色值。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>7:0</td><td>BPDBV[7:0]</td><td>背景层预定义蓝色值当背景层像素格式是A4或A8时,该位域被用作背景层蓝色值。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.12. 前景层 LUT 存储区基地址寄存器（IPA_FLMADDR）

偏移地址：0x2C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">FLMADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">FLMADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>FLMADDR[31:0]</td><td>前景层 LUT 存储区基地址软件置位和清除这些位必须是8位,16位,32位对齐,具体对齐方式与前景层LUT像素格式相对应。如果前景层LUT像素格式是ARGB8888,这些位必须是32位对齐。如果违背以上对齐规则,当前景层LUT加载使能时,将产生配置错误。当IPA_FPCTL 寄存器的FLLEN 位为‘1’的时候,该位域不可写。</td></tr></table>

## 15.6.13. 背景层 LUT 存储区基地址寄存器（IPA_BLMADDR）

偏移地址：0x30

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">BLMADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">BLMADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>BLMADDR[31:0]</td><td>背景层 LUT 存储区基地址软件置位和清除这些位必须是8位,16位,32位对齐,具体对齐方式与背景层LUT像素格式相对应。如果背景层LUT像素格式是ARGB8888,这些位必须是32位对齐。如果违背以上对齐规则,当背景层LUT加载使能时,将产生配置错误。当IPA_BPCTL寄存器的BLLEN 位为‘1’的时候,该位域不可写。</td></tr></table>

## 15.6.14. 目标像素控制寄存器（IPA_DPCTL）

偏移地址：0x34

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td colspan="3">DPF[2:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2:0</td><td>DPF[2:0]</td><td>目标像素格式</td></tr><tr><td></td><td></td><td>软件置位和清除</td></tr><tr><td></td><td></td><td>000: ARGB8888</td></tr><tr><td></td><td></td><td>001: RGB888</td></tr><tr><td></td><td></td><td>010: RGB565</td></tr><tr><td></td><td></td><td>011: ARGB1555</td></tr><tr><td></td><td></td><td>100: ARGB4444</td></tr><tr><td></td><td></td><td>101~111: 保留</td></tr><tr><td></td><td></td><td>当IPA_CTL寄存器的TEN位为&#x27;1&#x27;时,该位不可写。</td></tr></table>

## 15.6.15. 目标像素值寄存器（IPA_DPV）

偏移地址：0x38

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">DPDAV[7:0]</td><td colspan="8">DPDRV[7:0]</td></tr><tr><td colspan="8">MEANINGLESS</td><td colspan="8">DPDRV[7:0]</td></tr><tr><td colspan="16">MEANINGLESS</td></tr><tr><td colspan="16">MEANINGLESS</td></tr><tr><td colspan="16">MEANINGLESS</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">DPDGV[7:0]</td><td colspan="8">DPDBV[7:0]</td></tr><tr><td colspan="8">DPDGV[7:0]</td><td colspan="8">DPDBV[7:0]</td></tr><tr><td colspan="5">DPDRV[4:0]</td><td colspan="6">DPDGV[5:0]</td><td colspan="5">DPDBV[4:0]</td></tr><tr><td>DPDAV</td><td colspan="5">DPDRV[4:0]</td><td colspan="5">DPDGV[4:0]</td><td colspan="5">DPDBV[4:0]</td></tr><tr><td colspan="4">DPDAV[3:0]</td><td colspan="4">DPDRV[3:0]</td><td colspan="4">DPDGV[3:0]</td><td colspan="4">DPDBV[3:0]</td></tr><tr><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td><td colspan="4">rw</td></tr></table>

当目标像素格式是 ARGB8888 时，第一行有效。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>DPDAV[7:0]</td><td>目标层预定义alpha值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层alpha值。当IPA_CTL寄存器的TEN位的值为‘1’时,该位不可写。</td></tr><tr><td>23:16</td><td>DPDRV[7:0]</td><td>目标层预定义红色值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层红色值。当IPA_CTL寄存器的TEN位的值为‘1’时,该位不可写。</td></tr><tr><td>15:8</td><td>DPDGV[7:0]</td><td>目标层预定义绿色值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层绿色值。当IPA_CTL寄存器的TEN位的值为‘1’时,该位不可写。</td></tr><tr><td>7:0</td><td>DPDBV[7:0]</td><td>目标层预定义蓝色值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层蓝色值。当IPA_CTL寄存器的TEN 的值为‘1’时,该位不可写。</td></tr></table>

当目标像素格式是 RGB888 时，第 2 行有效。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>Meaningless</td><td>该位域可以软件置位和清除,但当目标像素格式是RGB888时,这些位没有意义。</td></tr><tr><td>23:16</td><td>DPDRV[7:0]</td><td>目标层预定义红色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层红色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>15:8</td><td>DPDGV[7:0]</td><td>目标层预定义绿色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层绿色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>7:0</td><td>DPDBV[7:0]</td><td>目标层预定义蓝色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层蓝色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr></table>

当目标像素格式是 RGB565 时，第 3 行有效。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>Meaningless</td><td>该位域可以软件置位和清除,但当目标像素格式是RGB565时,这些位没有意义。</td></tr><tr><td>15:11</td><td>DPDRV[4:0]</td><td>目标层预定义红色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层红色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr><tr><td>10:5</td><td>DPDGV[5:0]</td><td>目标层预定义绿色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层绿色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr><tr><td>4:0</td><td>DPDBV[4:0]</td><td>目标层预定义蓝色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层蓝色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr></table>


当目标像素格式是 ARGB1555 时，第 4 行有效。


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>Meaningless</td><td>该位域可以软件置位和清除,但当目标像素格式是ARGB1555时,这些位没有意义。</td></tr><tr><td>15</td><td>DPDAV</td><td>目标层预定义alpha值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层alpha值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>14:10</td><td>DPDRV[4:0]</td><td>目标层预定义红色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层红色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>9:5</td><td>DPDGV[4:0]</td><td>目标层预定义绿色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层绿色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr><tr><td>4:0</td><td>DPDBV[4:0]</td><td>目标层预定义蓝色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层蓝色值。当IPA_CTL寄存器的TEN位的值为&#x27;1&#x27;时,该位不可写。</td></tr></table>

当目标像素格式是 ARGB4444 时，第 5 行有效。

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>Meaningless</td><td>该位域可以软件置位和清除,但当目标像素格式是ARGB4444时,这些位没有意义。</td></tr><tr><td>15:12</td><td>DPDAV[3:0]</td><td>目标层预定义alpha值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层alpha值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr><tr><td>11:8</td><td>DPDRV[3:0]</td><td>目标层预定义红色值软件置位和清除当IPA配置为用特定的颜色填充目标存储区的时候,这些位用作目标层红色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr><tr><td>7:4</td><td>DPDGV[3:0]</td><td>目标层预定义绿色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层绿色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr><tr><td>3:0</td><td>DPDBV[3:0]</td><td>目标层预定义蓝色值软件置位和清除当 IPA 配置为用特定的颜色填充目标存储区的时候,这些位用作目标层蓝色值。当IPA_CTL寄存器的TEN位的值为'1'时,该位不可写。</td></tr></table>

## 15.6.16. 目标存储区基地址寄存器（IPA_DMADDR）

偏移地址：0x3C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DMADDR[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DMADDR[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DMADDR[31:0]</td><td>目标存储区基地址软件置位和清除如果目标层像素格式是ARGB8888,这些位必须是32位对齐,如果目标层像素格式是RGB565, ARGB1555或ARGB4444,这些位必须是16位对齐,如果违背以上对齐规则,当传输使能的时候,将检测到一个配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.17. 目标行偏移寄存器（IPA_DLOFF）

偏移地址：0x40

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="2">保留</td><td colspan="14">DLOFF[13:0]</td></tr></table>

<table><tr><td>31:14</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>13:0</td><td>DLOFF[13:0]</td><td>目标行偏移该位表明当前行最后一个像素和下一行第一个像素之间的像素数目。当IPA_CTL寄存器的PFCM配置为“00”时,如果前景层像素格式是A4或L4,DLOFF 必须被配置成一个偶数,否则当传输使能的时候将检测到一个配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr></table>

## 15.6.18. 图像大小寄存器（IPA_IMS）

偏移地址：0x44

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="2">保留</td><td colspan="14">WIDTH[13:0]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">HEIGHT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:30</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>29:16</td><td>WIDTH[13:0]</td><td>待处理的图像的宽度软件置位和清除该位域表示待处理的图像每行像素的数目。如果背景层或前景层像素格式是A4或L4,这些位必须配置成偶数,否则当传输使能的时候将检测到一个配置错误。当IPA_CTL寄存器的TEN位为‘1’时,该位不可写。</td></tr><tr><td>15:0</td><td>HEIGHT[15:0]</td><td>待处理图像的高度软件置位和清除该位域表明待处理图像的行数。当IPA_CTL寄存器的TEN为‘1’时,该位不可写。</td></tr></table>

## 15.6.19. 行标记寄存器（IPA_LM）

偏移地址：0x48

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">LM[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>LM[15:0]</td><td>行标记软件置位和清除该位域定义了一个行号以表明传输的进度,当且仅当标记行的最后一个像素已经写入了目标存储区,传输行标记中断标志位将置位。当IPA_CTL寄存器的TEN位为&#x27;1&#x27;时,该位不可写。</td></tr></table>

## 15.6.20. 内部定时器控制寄存器（IPA_ITCTL）

偏移地址：0x4C

复位值：0x0000 0000

该寄存器可以按字节（8位）、半字（16位）或字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">NCCI[7:0]</td><td colspan="7">保留</td><td>ITEN</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>NCCI[7:0]</td><td>间隔时钟周期数软件置位和清除如果ITEN等于‘0’,该位域没有意义。如果ITEN等于‘1’,该位域表示两个连续的AHB请求之间插入的时钟周期数的最小值。</td></tr><tr><td>7:1</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>0</td><td>ITEN</td><td>内部定时器使能IPA使用一个内部定时器用来减少AHB总线使用带宽。0:禁止内部定时器1:使能内部定时器</td></tr></table>
