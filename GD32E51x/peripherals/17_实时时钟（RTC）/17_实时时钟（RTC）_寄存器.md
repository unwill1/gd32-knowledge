## 17.4. RTC 寄存器

RTC 基地址：0x4000 2800

## 17.4.1. RTC 中断使能寄存器(RTC_INTEN)

偏移地址：0x00

复位值：0x0000

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">保留</td><td>OVIE</td><td>ALRMIE</td><td>SCIE</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2</td><td>OVIE</td><td>溢出中断使能0:禁用溢出中断1:使能溢出中断</td></tr><tr><td>1</td><td>ALRMIE</td><td>闹钟中断使能0:禁用闹钟中断1:使能闹钟中断</td></tr><tr><td>0</td><td>SCIE</td><td>秒中断使能0:禁用秒中断1:使能秒中断</td></tr></table>

## 17.4.2. RTC 控制寄存器(RTC_CTL)

偏移地址：0x04

复位值：0x0020


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>LWOFF</td><td>CMF</td><td>RSYNF</td><td>OVIF</td><td>ALRMIF</td><td>SCIF</td></tr><tr><td colspan="10"></td><td>r</td><td>rw</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>5</td><td>LWOFF</td><td>上次对RTC寄存器写操作标志0:上次对RTC寄存器写操作没有完成1:上次对RTC寄存器写操作已经完成</td></tr><tr><td>4</td><td>CMF</td><td>配置模式标志0:退出配置模式1:进入配置模式</td></tr><tr><td>3</td><td>RSYNF</td><td>寄存器同步标志0:寄存器没有与APB1时钟同步1:寄存器已经与APB1时钟同步</td></tr><tr><td>2</td><td>OVIF</td><td>溢出中断标志0:没有检测到溢出事件1:检测到溢出事件。当RTC_INTEN寄存器的OVIE位被置1,中断发生。</td></tr><tr><td>1</td><td>ALRMIF</td><td>闹钟中断标志0:没有检测到闹钟事件1:检测到闹钟事件。当RTC_INTEN寄存器的ALRMIE位被置1,RTC全局中断发生。并且当EXTI17被使能中断模式,发生RTC闹钟中断。</td></tr><tr><td>0</td><td>SCIF</td><td>秒中断标志0:没有检测到秒事件1:检测到秒事件。当RTC_INTEN寄存器的SCIE位被置1,中断发生。当分频器重加载RTC_PSC值时,硬件将该位置1,从而累加RTC计数器。</td></tr></table>

## 17.4.3. RTC 预分频寄存器高位(RTC_PSCH)

偏移地址：0x08

复位值：0x0000


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">PSC[19:16]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:0</td><td>PSC[19:16]</td><td>RTC 预分频器高位值</td></tr></table>

## 17.4.4. RTC 预分频寄存器低位(RTC_PSCL)

偏移地址：0x0C

复位值：0x8000

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>RTC 预分频器低位值SC_CLK 的频率是 RTCCLK 的频率除以(PSC[19:0]+1)</td></tr></table>

## 17.4.5. RTC 分频器高位(RTC_DIVH)

偏移地址：0x10

复位值：0x0000


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留</td><td colspan="4">DIV[19:16]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:4</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>3:0</td><td>DIV[19:16]</td><td>RTC 分频器高位</td></tr></table>

## 17.4.6. RTC 分频器低位(RTC_DIVL)

偏移地址：0x14

复位值：0x8000


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>DIV[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>DIV[15:0]</td><td>RTC 分频器低位当 RTC 预分频寄存器或者 RTC 计数寄存器更新时,RTC 分频器寄存器会由硬件自动加载</td></tr></table>

## 17.4.7. RTC 计数寄存器高位(RTC_CNTH)

偏移地址：0x18

复位值：0x0000


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[31:16]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[31:16]</td><td>RTC 计数寄存器高位</td></tr></table>

## 17.4.8. RTC 计数寄存器低位(RTC_CNTL)

偏移地址：0x1C

复位值：0x0000


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>RTC计数寄存器低位</td></tr></table>

## 17.4.9. RTC 闹钟寄存器高位(RTC_ALRMH)

偏移地址：0x20

复位值：0xFFFF

该寄存器可以按半字（16 位）或字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALRM[31:16]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>ALRM[31:16]</td><td>RTC 闹钟值高位</td></tr></table>

## 17.4.10. RTC 闹钟寄存器低位(RTC_ALRML)

偏移地址：0x24

复位值：0xFFFF


该寄存器可以按半字（16 位）或字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ALRM[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:0</td><td>ALRM[15:0]</td><td>RTC 闹钟值低位</td></tr></table>