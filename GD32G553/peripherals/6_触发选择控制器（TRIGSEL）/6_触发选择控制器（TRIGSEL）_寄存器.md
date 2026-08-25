## 6.5. TRIGSEL 寄存器

TRIGSEL 基地址：0x4001 8400

## 6.5.1. EXTOUT 触发选择寄存器 0（TRIGSEL_EXTOUT_0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_0将不能被修改。0: TRIGSEL_EXTOUT_0 寄存器可写可读1: TRIGSEL_EXTOUT_0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT1(外部输出 1)的信号源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT0(外部输出 0)的信号源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.2. EXTOUT 触发选择寄存器 1（TRIGSEL_EXTOUT_1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_1将不能被修改。0: TRIGSEL_EXTOUT_1 寄存器可写可读1: TRIGSEL_EXTOUT_1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT3(外部输出 3)的信号源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT2(外部输出 2)的信号源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.3. EXTOUT 触发选择寄存器 2（TRIGSEL_EXTOUT_2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_2将不能被修改。0: TRIGSEL_EXTOUT_2 寄存器可写可读1: TRIGSEL_EXTOUT_2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出1的输入源选择这些位用来选择连接到输出1的触发输入信号,输出1作为TRIGSEL_OUT5(外部输出5)的信号源。关于具体配置请参考表6-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TRIGSEL_OUT4(外部输出4)的信号源。关于具体配置请参考表6-1.触发输入位域选择。</td></tr></table>

## 6.5.4. EXTOUT3 触发选择寄存器 3（TRIGSEL_EXTOUT_3）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_3将不能被修改。0: TRIGSEL_EXTOUT_3 寄存器可写可读1: TRIGSEL_EXTOUT_3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT7(外部输出 7)的信号源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT6(外部输出 6)的信号源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.5. ADC0 触发选择寄存器（TRIGSEL_ADC0）

地址偏移：0x10

复位值：0x0000 1012

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC0将不能被修改。0: TRIGSEL_ADC0 寄存器可写可读1: TRIGSEL_ADC0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC0_ROUTRG(ADC0 常规序列)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.6. ADC1 触发选择寄存器（TRGSEL_ADC1）

地址偏移：0x14

复位值：0x0000 1012

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC1将不能被修改。0: TRIGSEL_ADC1 寄存器可写可读1: TRIGSEL_ADC1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC1_ROUTRG(ADC1 常规序列)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.7. ADC2 触发选择寄存器（TRIGSEL_ADC2）

地址偏移：0x18

复位值：0x0000 1028

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC2将不能被修改。0: TRIGSEL_ADC2 寄存器可写可读1: TRIGSEL_ADC2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC2_ROUTRG(ADC2 常规序列)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.8. ADC3 触发选择寄存器（TRIGSEL_ADC3）

地址偏移：0x1C

复位值：0x0000 1028

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC3将不能被修改。0: TRIGSEL_ADC3 寄存器可写可读1: TRIGSEL_ADC3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC3_ROUTRG(ADC3 常规序列)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.9. TIMER0_BRKIN 触发选择寄存器（TRIGSEL_TIMER0BRKIN）

地址偏移：0x2C

复位值：0x006F 616D

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0BRIKIN将不能被修改。0: TRIGSEL_TIMER0BRIKIN 寄存器可写可读1: TRIGSEL_TIMER0BRIKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 的输入源选择这些位用来选择连接到输出 2 的触发输入信号, 输出 2 作为 TIMER0BRKIN2 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号, 输出 1 作为 TIMER0BRKIN1 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号, 输出 0 作为 TIMER0BRKIN0 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.10. TIMER7_BRKIN 触发选择寄存器（TRIGSEL_TIMER7BRKIN）

地址偏移：0x30

复位值：0x0072 7170

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7BRIKIN将不能被修改。0: TRIGSEL_TIMER7BRIKIN 寄存器可写可读1: TRIGSEL_TIMER7BRIKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 的输入源选择这些位用来选择连接到输出 2 的触发输入信号,输出 2 作为 TIMER7BRKIN2 的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TIMER7BRKIN1 的触发源。关于具体配置请参考表6-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TIMER7BRKIN0的触发源。关于具体配置请参考表6-1.触发输入位域选择。</td></tr></table>

## 6.5.11. TIMER14_BRKIN 触发选择寄存器（TRIGSEL_TIMER14BRKIN）

地址偏移：0x34

复位值：0x0000 0073

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER14BRIKIN将不能被修改。0: TRIGSEL_TIMER14BRIKIN 寄存器可写可读1: TRIGSEL_TIMER14BRIKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER14BRKIN0 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.12. TIMER15_BRKIN 触发选择寄存器（TRIGSEL_TIMER15BRKIN）

地址偏移：0x38

复位值：0x0000 0074

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER15BRIKIN将不能被修改。0: TRIGSEL_TIMER15BRIKIN 寄存器可写可读1: TRIGSEL_TIMER15BRIKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER15BRKIN0 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.13. TIMER16_BRKIN 触发寄存器（TRIGSEL_TIMER16BRKIN）

地址偏移：0x3C

复位值：0x0000 0075

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER16BRIKIN将不能被修改。0: TRIGSEL_TIMER16BRIKIN 寄存器可写可读1: TRIGSEL_TIMER16BRIKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER16BRKIN0 的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.14. TIMER19_BRKIN 触发选择寄存器（TRIGSEL_TIMER19BRKIN）

地址偏移：0x40

复位值：0x0078 7776

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER19BRIKIN将不能被修改。0: TRIGSEL_TIMER19BRIKIN 寄存器可写可读1: TRIGSEL_TIMER19BRIKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER19BRKIN0 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.15. CAN0 触发选择寄存器（TRIGSEL_CAN0）

地址偏移：0x44

复位值：0x0000 0039

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN0将不能被修改。0: TRIGSEL_CAN0 寄存器可写可读1: TRIGSEL_CAN0 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 CAN0_EX_TIME_TICK的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.16. CAN1 触发选择寄存器（TRIGSEL_CAN1）

地址偏移：0x48

复位值：0x0000 0039

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN1将不能被修改。0: TRIGSEL_CAN1 寄存器可写可读1: TRIGSEL_CAN1 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 CAN1_EX_TIME_TICK的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.17. CAN2 触发选择寄存器（TRIGSEL_CAN2）

地址偏移：0x4C

复位值：0x0000 0039

该寄存器只能按字（32 位）访问。

<table><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN2将不能被修改。0: TRIGSEL_CAN2 寄存器可写可读1: TRIGSEL_CAN2 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 CAN2_EX_TIME_TICK的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.18. TIMER0_ETI 触发选择寄存器（TRIGSEL_TIMER0ETI）

地址偏移：0x50

复位值：0x0000 0020

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0ETI将不能被修改。0: TRIGSEL_TIMER0ETI 寄存器可写可读1: TRIGSEL_TIMER0ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择</td></tr></table>

这些位用来选择连接到输出 0的触发输入信号，输出 0 作为 TIMER0_ETI 的触发源。关于具体配置请参考 6-1. 。

## 6.5.19. TIMER1_ETI 触发选择寄存器（TRIGSEL_TIMER1ETI）

地址偏移：0x54

复位值：0x0000 0026

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER1ETI将不能被修改。0: TRIGSEL_TIMER1ETI 寄存器可写可读1: TRIGSEL_TIMER1ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER1_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.20. TIMER2_ETI 触发选择寄存器（TRIGSEL_TIMER2ETI）

地址偏移：0x58

复位值：0x0000 002C

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ETI将不能被修改。0: TRIGSEL_TIMER2ETI 寄存器可写可读1: TRIGSEL_TIMER2ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER2_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.21. TIMER3_ETI 触发选择寄存器（TRIGSEL_TIMER3ETI）

地址偏移：0x5C

复位值：0x0000 0032

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER3ETI将不能被修改。0: TRIGSEL_TIMER3ETI 寄存器可写可读1: TRIGSEL_TIMER3ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER3_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.22. TIMER4_ETI 触发选择寄存器（TRIGSEL_TIMER4ETI）

地址偏移：0x60

复位值：0x0000 0038

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER4ETI将不能被修改。0: TRIGSEL_TIMER4ETI 寄存器可写可读1: TRIGSEL_TIMER4ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER4_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.23. TIMER7_ETI 触发选择寄存器（TRIGSEL_TIMER7ETI）

地址偏移：0x64

复位值：0x0000 004B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7ETI将不能被修改。0: TRIGSEL_TIMER7ETI 寄存器可写可读</td></tr><tr><td></td><td></td><td>1: TRIGSEL_TIMER7ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER7_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.24. TIMER19_ETI 触发选择寄存器（TRIGSEL_TIMER19ETI）

地址偏移：0x68

复位值：0x0000 006C

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER19ETI将不能被修改。0: TRIGSEL_TIMER19ETI 寄存器可写可读1: TRIGSEL_TIMER0ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER19_ETI 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.25. HPDF_ITRG 触发选择控制寄存器（TRIGSEL_HPDF）

地址偏移：0x6C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_HPDF将不能被修改。0: TRIGSEL_HPDF 寄存器可写可读1: TRIGSEL_HPDF 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 HPDF_ITRG 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.26. TIMER0_ITI14 触发选择寄存器（TRIGSEL_TIMER0ITI14）

地址偏移：0x70

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0ITI14将不能被修改。0: TRIGSEL_TIMER0ITI14 寄存器可写可读1: TRIGSEL_TIMER0ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER0_ITI14 的触发</td></tr></table>

源。关于具体配置请参考 6-1. 。

## 6.5.27. TIMER1_ITI14 触发选择寄存器（TRIGSEL_TIMER1ITI14）

地址偏移：0x74

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER1ITI14将不能被修改。0: TRIGSEL_TIMER1ITI14 寄存器可写可读1: TRIGSEL_TIMER1ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER1_ITI14 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.28. TIMER2_ITI14 触发选择寄存器（TRIGSEL_TIMER2ITI14）

地址偏移：0x78

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ITI14将不能被修改。0: TRIGSEL_TIMER2ITI14 寄存器可写可读1: TRIGSEL_TIMER2ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER2_ITI14 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.29. TIMER3_ITI14 触发选择寄存器（TRIGSEL_TIMER3ITI14）

地址偏移：0x7C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER3ITI14将不能被修改。0: TRIGSEL_TIMER3ITI14 寄存器可写可读1: TRIGSEL_TIMER3ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER3_ITI14 的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.30. TIMER4_ITI14 触发选择寄存器（TRIGSEL_TIMER4ITI14）

地址偏移：0x80

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER4ITI14将不能被修改。0: TRIGSEL_TIMER4ITI14 寄存器可写可读1: TRIGSEL_TIMER4ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER4_ITI14 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.31. TIMER7_ITI14 触发选择寄存器（TRIGSEL_TIMER7ITI14）

地址偏移：0x84

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7ITI14将不能被修改。0: TRIGSEL_TIMER7ITI14 寄存器可写可读1: TRIGSEL_TIMER7ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER7_ITI14 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.32. TIMER14_ITI14 触发选择寄存器（TRIGSEL_TIMER14ITI14）

地址偏移：0x88

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER14ITI14将不能被修改。0: TRIGSEL_TIMER14ITI14 寄存器可写可读1: TRIGSEL_TIMER14ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER14_ITI14 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.33. TIMER19_ITI14 触发选择寄存器（TRIGSEL_TIMER19ITI14）

地址偏移：0x8C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER19ITI14将不能被修改。0: TRIGSEL_TIMER19ITI14 寄存器可写可读1: TRIGSEL_TIMER19ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER19_ITI14 的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.34. DAC0 触发选择寄存器（TRIGSEL_DAC0）

地址偏移：0x90

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC0将不能被修改。0: TRIGSEL_DAC0 寄存器可写可读1: TRIGSEL_DAC0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 DAC0_OUT1_EXTRIG(DAC0_OUT1 外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为DAC0_OUT0_EXTRIG(DAC0_OUT0 外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.35. DAC1 触发选择寄存器（TRIGSEL_DAC1）

地址偏移：0x94

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC1将不能被修改。0: TRIGSEL_DAC1 寄存器可写可读1: TRIGSEL_DAC1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 DAC1_OUT1_EXTRIG(DAC1_OUT1 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC1_OUT0_EXTRIG(DAC1_OUT0 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.36. DAC2 触发选择寄存器（TRIGSEL_DAC2）

地址偏移：0x98

复位值：0x0000 1010

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC2将不能被修改。0: TRIGSEL_DAC2 寄存器可写可读1: TRIGSEL_DAC2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 DAC2_OUT1_EXTRIG(DAC2_OUT1 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC2_OUT0_EXTRIG(DAC2_OUT0 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.37. DAC3 触发选择寄存器（TRIGSEL_DAC3）

地址偏移：0x9C

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>INSEL1[7:0]</td><td>INSEL0[7:0]</td></tr><tr><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC3将不能被修改。0: TRIGSEL_DAC3 寄存器可写可读1: TRIGSEL_DAC3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 DAC3_OUT1_EXTRIG(DAC3_OUT1 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC3_OUT0_EXTRIG(DAC3_OUT0 外部触发)的触发源。关于具体配置请参考表 6-1. 触发输入位域选择。</td></tr></table>

## 6.5.38. DAC0 触发选择扩展寄存器（TRIGSEL_EXTDAC0）

地址偏移：0xA0

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTDAC0将不能被修改。0: TRIGSEL_EXTDAC0 寄存器可写可读1: TRIGSEL_EXTDAC0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出1的输入源选择这些位用来选择连接到输出1的触发输入信号,输出1作为DAC0_OUT1_ST_EXTRIG(DAC0_OUT1锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为DAC0_OUT0_ST_EXTRIG(DAC0_OUT0锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.39. DAC1 触发选择扩展寄存器（TRIGSEL_EXTDAC1）

地址偏移：0xA4

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTDAC1将不能被修改。0: TRIGSEL_EXTDAC1 寄存器可写可读1: TRIGSEL_EXTDAC1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为DAC1_OUT1_ST_EXTRIG(DAC1_OUT1 锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为DAC1_OUT0_ST_EXTRIG(DAC1_OUT0 锯齿递增/递减外部触发)的触发源。关</td></tr></table>

于具体配置请参考 6-1. 。

## 6.5.40. DAC2 触发选择扩展寄存器（TRIGSEL_EXTDAC2）

地址偏移：0xA8

复位值：0x0000 1010

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTDAC2将不能被修改。0: TRIGSEL_EXTDAC2 寄存器可写可读1: TRIGSEL_EXTDAC2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为DAC2_OUT1_ST_EXTRIG(DAC2_OUT1 锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为DAC2_OUT0_ST_EXTRIG(DAC2_OUT0 锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.41. DAC3 触发选择扩展寄存器（TRIGSEL_EXTDAC3）

地址偏移：0xAC

复位值：0x0000 3B3B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTDAC3将不能被修改。0: TRIGSEL_EXTDAC3 寄存器可写可读1: TRIGSEL_EXTDAC3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 DAC3_OUT1_ST_EXTRIG(DAC3_OUT1 锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC0_OUT3_ST_EXTRIG(DAC3_OUT0 锯齿递增/递减外部触发)的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.42. CLA 触发选择寄存器 0（TRIGSEL_CLA_0）

地址偏移：0xB0

复位值：0x00C1 C0BF

该寄存器的复位取决于 SYSCFG_CFG2 中的 TRIGSEL_RSTMD 位。若 TRIGSEL_RSTMD = 0，该寄存器将在系统复位后复位。若 TRIGSEL_RSTMD = 1，该寄存器只能在 POR 复位后复位。

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL寄存器锁定标志位该位通过软件置位,通过系统复位或POR复位(取决于TRIGSEL_RSTMD的值)清除。该位置位后,TRIGSEL_CLA_0将不能被修改。0: TRIGSEL_CLA_0 寄存器可写可读1: TRIGSEL_CLA_0 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出2的输入源选择这些位用来选择连接到输出2的触发输入信号,输出2作为TRIGSEL_CLA_IN2的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出1的输入源选择这些位用来选择连接到输出1的触发输入信号,输出1作为TRIGSEL_CLA_IN1的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TRIGSEL_CLA_IN0的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.43. CLA 触发选择寄存器 1（TRIGSEL_CLA_1）

地址偏移：0xB4

复位值：0x00C4 C3C2

该寄存器的复位取决于 SYSCFG_CFG2 中的 TRIGSEL_RSTMD 位。若 TRIGSEL_RSTMD = 0，该寄存器将在系统复位后复位。若 TRIGSEL_RSTMD = 1，该寄存器只能在 POR 复位后复位。该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位或POR复位(取决于TRIGSEL_RSTMD的值)清除。该位置位后,TRIGSEL_CLA_1将不能被修改。0: TRIGSEL_CLA_1 寄存器可写可读1: TRIGSEL_CLA_1 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出2的输入源选择这些位用来选择连接到输出2的触发输入信号,输出2作为TRIGSEL_CLA_IN5的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出1的输入源选择这些位用来选择连接到输出1的触发输入信号,输出1作为TRIGSEL_CLA_IN4的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TRIGSEL_CLA_IN3的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.44. CLA 触发选择寄存器 2（TRIGSEL_CLA_2）

地址偏移：0xB8

复位值：0x0027 2110

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="5">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CLA_2将不能被修改。0: TRIGSEL_CLA_2 寄存器可写可读1: TRIGSEL_CLA_2 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 的输入源选择这些位用来选择连接到输出 2 的触发输入信号,输出 2 作为 TRIGSEL_CLA_IN8 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_CLA_IN7 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择</td></tr></table>

这些位用来选择连接到输出 0 的触发输入信号，输出 0 作为 TRIGSEL_CLA_IN6 的触发源。关于具体配置请参考 6-1. 。

## 6.5.45. CLA 触发选择寄存器 3（TRIGSEL_CLA_3）

地址偏移：0xBC

复位值：0x0000 3A39

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CLA_3将不能被修改。0: TRIGSEL_CLA_3 寄存器可写可读1: TRIGSEL_CLA_3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_CLA_IN10 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_CLA_IN9 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>

## 6.5.46. CLA 触发选择寄存器 4（TRIGSEL_CLA_4）

地址偏移：0xC0

复位值：0x0000 00EF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CLA_4将不能被修改。0: TRIGSEL_CLA_4 寄存器可写可读1: TRIGSEL_CLA_4 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_CLA_IN11 的触发源。关于具体配置请参考表6-1. 触发输入位域选择。</td></tr></table>
