## 8.4. BKP 寄存器

BKP 基地址：0x4000 6C00

## 8.4.1. 备份数据寄存器 (BKP_DATAx) (x= 0..41)

地址偏移：0x04 + 0x04*x(x=0..9)，0x40 + 0x04*(x-10)(x=10..41)

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA [15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:0</td><td>DATA[15:0]</td><td>备份数据这些位用来存储一般用户数据。即使从待机模式唤醒或系统复位或电源复位后,BKP_DATAx寄存器的内容仍旧不会丢失。</td></tr></table>

## 8.4.2. RTC 信号输出控制寄存器 (BKP_OCTL)

地址偏移：0x2C

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CALDIR</td><td>CCOSEL</td><td colspan="4">保留</td><td>ROSEL</td><td>ASOEN</td><td>COEN</td><td colspan="7">RCCV[6:0]</td></tr><tr><td>rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>CALDIR</td><td>RTC时钟校方向1:变快该位只能被备份域复位清除。</td></tr><tr><td>14</td><td>CCOSEL</td><td>RTC时钟输出选择0:RTC时钟64分频1:RTC时钟该位只能被上电复位(POR)清除。</td></tr><tr><td>13:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>ROSEL</td><td>RTC输出选择0:RTC输出为闹钟脉冲1:RTC输出为秒脉冲该位只能被备份域复位清除。</td></tr><tr><td>8</td><td>ASOEN</td><td>RTC闹钟或秒信号输出使能0:RTC闹钟或秒信号输出禁止1:RTC闹钟或秒信号输出使能使能后,TAMPER引脚可作为RTC输出。该位只能被备份域复位清除。</td></tr><tr><td>7</td><td>COEN</td><td>RTC时钟校准输出使能0:RTC时钟校准输出禁止1:RTC时钟校准输出使能使能后,TAMPER引脚输出RTC时钟或RTC时钟的64分频。ASOEN位优先于COEN位,当ASOEN位置位时,不管COEN置位与否,TAMPER引脚作为RTC闹钟或秒信号输出。该位只能被上电复位(POR)清除。</td></tr><tr><td>6:0</td><td>RCCV[6:0]</td><td>RTC时钟校准值该值表示在每2^20个时钟脉冲内将有多少个时钟脉冲被忽略。该位只能被备份域复位清除。</td></tr></table>

## 8.4.3. 侵入引脚控制寄存器 (BKP_TPCTL)

地址偏移：0x30

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>TPAL</td><td>TPEN</td></tr><tr><td colspan="14">位/位域</td><td>名称</td><td>描述</td></tr><tr><td colspan="14">31:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td colspan="14">1</td><td>TPAL</td><td>TAMPER 引脚有效电平0:TAMPER 引脚高电平有效1:TAMPER 引脚低电平有效</td></tr><tr><td colspan="14">0</td><td>TPEN</td><td>TAMPER 引脚使能0:TAMPER 引脚作为 GPIO 口使用1:TAMPER 引脚可实现备份复位功能。TAMPER 引脚上的有效电平将复位 BKP_DATAx 寄存器中所有数据。</td></tr></table>

## 8.4.4. 侵入控制状态寄存器 (BKP_TPCS)

地址偏移：0x34

复位值：0x0000 0000

该寄存器可以按半字（16 位）或字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>TIF</td><td>TEF</td><td colspan="5">保留</td><td>TPIE</td><td>TIR</td><td>TER</td></tr><tr><td colspan="6"></td><td>r</td><td>r</td><td colspan="5"></td><td>rw</td><td>w</td><td>w</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>TIF</td><td>侵入中断标志0:没有侵入中断发生1:有侵入中断发生该位可通过TIR位置1或TPIE位置0来清零。</td></tr><tr><td>8</td><td>TEF</td><td>侵入事件标志0:没有侵入事件发生1:有侵入事件发生该位可通过对TER为写1来清零。</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>TPIE</td><td>侵入中断使能0:侵入中断禁用</td></tr></table>

## 1：侵入中断使能

该位仅可通过系统复位或待机模式唤醒后复位。

<table><tr><td>1</td><td>TIR</td><td>侵入中断复位0:不影响1:复位 TIF 位该位一直读为 0。</td></tr><tr><td>0</td><td>TER</td><td>侵入事件复位0:不影响1:复位 TEF 位该位一直读为 0。</td></tr></table>

