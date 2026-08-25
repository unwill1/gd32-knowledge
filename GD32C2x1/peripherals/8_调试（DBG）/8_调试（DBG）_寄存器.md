## 8.4. DBG 寄存器

DBG基地址：0x4001 5800

## 8.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

只读寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器</td></tr></table>


这些位由软件读取，这些位是不变的常数。


## 8.4.2. 控制寄存器 0（DBG_CTL0）

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问

<table><tr><td colspan="10">Reserved</td><td>TIMER16_HOLD</td><td>TIMER15_HOLD</td><td colspan="4">Reserved</td></tr><tr><td colspan="10"></td><td>rw</td><td>rw</td><td colspan="4"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>I2C0_HOLD</td><td>Reserved</td><td>TIMER13_HOLD</td><td>TIMER2_HOLD</td><td>TIMER0_HOLD</td><td>Reserved</td><td>WWDGT_HOLD</td><td>FWDGT_HOLD</td><td colspan="5">Reserved</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER16_HOLD</td><td>TIMER16 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER16 计数器不变,用于调试</td></tr><tr><td>20</td><td>TIMER15_HOLD</td><td>TIMER15 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER15 计数器不变,用于调试</td></tr><tr><td>19:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15</td><td>I2C0_HOLD</td><td>I2C0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>TIMER13_HOLD</td><td>TIMER13 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER13 计数器不变,用于调试</td></tr><tr><td>12</td><td>TIMER2_HOLD</td><td>TIMER2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER2 计数器不变,用于调试</td></tr><tr><td>11</td><td>TIMER0_HOLD</td><td>TIMER0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER0 计数器不变,用于调试</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WWDGT_HOLD</td><td>WWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试</td></tr><tr><td>8</td><td>FWDGT_HOLD</td><td>FWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 FWDGT 计数器时钟,用于调试</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_HIRC 提供,当退出待机模式时,产生系统复位</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_HIRC 提供,当退出待机模式时,产生系统复位</td></tr></table>

## 8.4.3. 控制寄存器 1（DBG_CTL1）

地址偏移：0x08

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="5">保留</td><td>RTC_HOLD</td><td colspan="10">保留</td></tr><tr><td colspan="16">rw</td></tr><tr><td>位/位域</td><td colspan="4">名称</td><td colspan="11">描述</td></tr><tr><td>31:11</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr><tr><td>10</td><td colspan="4">RTC_HOLD</td><td colspan="11">RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试。</td></tr><tr><td>9:0</td><td colspan="4">保留</td><td colspan="11">必须保持复位值。</td></tr></table>
