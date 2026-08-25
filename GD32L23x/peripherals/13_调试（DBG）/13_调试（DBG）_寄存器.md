## 13.4. DBG 寄存器

DBG基地址：0x4001 5800

## 13.4.1. ID 寄存器（DBG_ID）

地址偏移：0x00

只读寄存器

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器这些位由软件读取,这些位是不变的常数</td></tr></table>

## 13.4.2. 控制寄存器 0（DBG_CTL0）

对于 GD32L233xx 型号

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="5">保留.</td><td>TIMER11_HOLD</td><td colspan="2">保留.</td><td>TIMER8_HOLD</td><td>保留</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td colspan="3">保留</td><td>I2C1_HOLD</td></tr><tr><td colspan="5"></td><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="3"></td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>I2C0_HOLD</td><td>保留</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td><td colspan="2">保留</td><td>WWDGT_HOLD</td><td>FWDGT_HOLD</td><td colspan="5">保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr><tr><td colspan="2">rw</td><td>rw</td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:27</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>26</td><td>TIMER11_HOLD</td><td>TIMER11 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER11 计数器不变,用于调试</td></tr><tr><td>25:24</td><td>保留</td><td>必须保持复位值。</td></tr></table>

<table><tr><td>23</td><td>TIMER8_HOLD</td><td>TIMER8 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER8 计数器不变,用于调试</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER6_HOLD</td><td>TIMER6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER6 计数器不变,用于调试</td></tr><tr><td>20</td><td>TIMER5_HOLD</td><td>TIMER5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER5 计数器不变,用于调试</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>I2C1_HOLD</td><td>I2C1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C1 的 SMBUS 状态不变,用于调试</td></tr><tr><td>15</td><td>I2C0_HOLD</td><td>I2C0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试</td></tr><tr><td>14</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>13</td><td>TIMER2_HOLD</td><td>TIMER2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER2 计数器不变,用于调试</td></tr><tr><td>12</td><td>TIMER1_HOLD</td><td>TIMER1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER1 计数器不变,用于调试</td></tr><tr><td>11:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WWDGT_HOLD</td><td>WWDGT 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试</td></tr><tr><td>8</td><td>FWDGT_HOLD</td><td>FWDGT 保持位该位由软件置位和复位</td></tr></table>

## 0：无影响

<table><tr><td></td><td></td><td>1: 当内核停止时保持 FWDGT 计数器时钟,用于调试</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_IRC16M 提供,当退出待机模式时,产生系统复位</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_IRC16M 提供,当退出待机模式时,产生系统复位</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持位该位由软件置位和复位0:无影响1:在睡眠模式下,AHB 时钟继续运行</td></tr></table>

## 对于 GD32L235xx 型号

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="3">保留</td><td>TIMER40_HOLD</td><td>TIMER14_HOLD</td><td>TIMER11_HOLD</td><td colspan="2">保留</td><td>TIMER8_HOLD</td><td>保留</td><td>TIMER6_HOLD</td><td>TIMER5_HOLD</td><td colspan="3">保留</td><td>I2C1_HOLD</td></tr><tr><td colspan="12">rw</td><td colspan="3">rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>I2C0_HOLD</td><td>CAN_HOLD</td><td>TIMER2_HOLD</td><td>TIMER1_HOLD</td><td>TIMER0_HOLD</td><td>保留</td><td>WWDGT_HOLD</td><td>FWDGT_HOLD</td><td colspan="5">保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr><tr><td colspan="3">rw</td><td colspan="2">rw</td><td>rw</td><td>rw</td><td>rw</td><td colspan="5"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:29</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>28</td><td>TIMER40_HOLD</td><td>TIMER40 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER40 计数器不变,用于调试</td></tr><tr><td>27</td><td>TIMER14_HOLD</td><td>TIMER14 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER14 计数器不变,用于调试</td></tr><tr><td>26</td><td>TIMER11_HOLD</td><td>TIMER11 保持位</td></tr></table>

<table><tr><td></td><td></td><td>该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER11 计数器不变,用于调试</td></tr><tr><td>25:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23</td><td>TIMER8_HOLD</td><td>TIMER8 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER8 计数器不变,用于调试</td></tr><tr><td>22</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>21</td><td>TIMER6_HOLD</td><td>TIMER6 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER6 计数器不变,用于调试</td></tr><tr><td>20</td><td>TIMER5_HOLD</td><td>TIMER5 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER5 计数器不变,用于调试</td></tr><tr><td>19:17</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>16</td><td>I2C1_HOLD</td><td>I2C1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C1 的 SMBUS 状态不变,用于调试</td></tr><tr><td>15</td><td>I2C0_HOLD</td><td>I2C0 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C0 的 SMBUS 状态不变,用于调试</td></tr><tr><td>14</td><td>CAN_HOLD</td><td>CAN 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 CAN 计数器状态不变,用于调试</td></tr><tr><td>13</td><td>TIMER2_HOLD</td><td>TIMER2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER2 计数器不变,用于调试</td></tr><tr><td>12</td><td>TIMER1_HOLD</td><td>TIMER1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER1 计数器不变,用于调试</td></tr></table>

<table><tr><td>11</td><td>TIMER0_HOLD</td><td>TIMER0保持位该位由软件置位和复位0:无影响1:当内核停止时保持 TIMER0计数器不变,用于调试</td></tr><tr><td>10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>WWDGT_HOLD</td><td>WWDGT保持位该位由软件置位和复位0:无影响1:当内核停止时保持 WWDGT 计数器时钟,用于调试</td></tr><tr><td>8</td><td>FWDGT_HOLD</td><td>FWDGT保持位该位由软件置位和复位0:无影响1:当内核停止时保持 FWDGT 计数器时钟,用于调试</td></tr><tr><td>7:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_IRC16M 提供,当退出待机模式时,产生系统复位</td></tr><tr><td>1</td><td>DSLP_HOLD</td><td>深度睡眠模式保持位该位由软件置位和复位0:无影响1:在待机模式下系统时钟和 AHB 时钟由 CK_IRC16M 提供,当退出待机模式时,产生系统复位</td></tr><tr><td>0</td><td>SLP_HOLD</td><td>睡眠模式保持位该位由软件置位和复位0:无影响1:在睡眠模式下,AHB 时钟继续运行</td></tr></table>

## 13.4.3. 控制寄存器 1（DBG_CTL1）

对于 GD32L233xx 型号

地址偏移：0x08

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="14">保留.</td><td>I2C2_HOLD</td><td>LPTIMER_HOLD</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>RTC_HOLD</td><td>保留</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>I2C2_HOLD</td><td>I2C2 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试</td></tr><tr><td>16</td><td>LPTIMER_HOLD</td><td>LPTIMER 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 LPTIMER 计数器不变,用于调试</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>RTC_HOLD</td><td>RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试</td></tr><tr><td>9:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

## 对于 GD32L235xx 型号

地址偏移：0x08

复位值：0x0000 0000，仅上电复位

该寄存器只能按字（32 位）访问。

<table><tr><td colspan="13">Reserved.</td><td>LPTIMER1_HOLD</td><td>I2C2_HOLD</td><td>LPTIMER0_HOLD</td></tr><tr><td colspan="13"></td><td></td><td>rw</td><td>rw</td></tr><tr><td colspan="5">Reserved</td><td>RTC_HOLD</td><td colspan="10">Reserved</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:19</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>18</td><td>LPTIMER1_HOLD</td><td>LPTIMER1 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 LPTIMER1 计数器不变,用于调试</td></tr><tr><td>17</td><td>I2C2_HOLD</td><td>I2C2 保持位该位由软件置位和复位0:无影响</td></tr></table>

<table><tr><td></td><td></td><td>1: 当内核停止时保持 I2C2 的 SMBUS 状态不变,用于调试</td></tr><tr><td>16</td><td>LPTIMER0_HOLD</td><td>LPTIMER 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 LPTIMER 计数器不变,用于调试</td></tr><tr><td>15:11</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>10</td><td>RTC_HOLD</td><td>RTC 保持位该位由软件置位和复位0:无影响1:当内核停止时保持 RTC 计数器不变,用于调试</td></tr><tr><td>9:0</td><td>保留</td><td>必须保持复位值。</td></tr></table>
