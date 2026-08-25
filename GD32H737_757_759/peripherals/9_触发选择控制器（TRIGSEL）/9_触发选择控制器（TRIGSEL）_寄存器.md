# 9.5. TRIGSEL 寄存器

TRIGSEL 基地址：0x4001 8400

# 9.5.1. EXTOUT 触发选择寄存器 0（TRIGSEL_EXTOUT_0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_0将不能被修改。0: TRIGSEL_EXTOUT_0 寄存器可写可读1: TRIGSEL_EXTOUT_0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT1(外部输出 1)的信号源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT0(外部输出 0)的信号源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.2. EXTOUT 触发选择寄存器 1（TRIGSEL_EXTOUT_1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_1将不能被修改。0: TRIGSEL_EXTOUT_1 寄存器可写可读1: TRIGSEL_EXTOUT_1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT3(外部输出 3)的信号源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT2(外部输出 2)的信号源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.3. EXTOUT 触发选择寄存器 2（TRIGSEL_EXTOUT_2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_2将不能被修改。0: TRIGSEL_EXTOUT_2 寄存器可读可写1: TRIGSEL_EXTOUT_2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT5(外部输出 5)的信号源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT4(外部</td></tr></table>

输出 4）的信号源。关于具体配置请参考 9-1. 。

# 9.5.4. EXTOUT 触发选择寄存器 3（TRIGSEL_EXTOUT_3）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_3将不能被修改。0: TRIGSEL_EXTOUT_3 寄存器可读可写1: TRIGSEL_EXTOUT_3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT7(外部输出 7)的信号源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT6(外部输出 6)的信号源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.5. ADC0 触发选择寄存器（TRIGSEL_ADC0）

地址偏移：0x10

复位值：0x0000 1113

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC0将不能被修改。0: TRIGSEL_ADC0 寄存器可读可写1: TRIGSEL_ADC0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC0_ROUTRG(ADC0 常规序列)的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.6. ADC1 触发选择寄存器（TRIGSEL_ADC1）

地址偏移：0x14

复位值：0x0000 1113

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC1将不能被修改。0: TRIGSEL_ADC1 寄存器可读可写1: TRIGSEL_ADC1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连到接输出 0 的触发输入信号,输出 0 作为 ADC1_ROUTRG(ADC1 常规序列)的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.7. ADC2 触发选择寄存器（TRIGSEL_ADC2）

地址偏移：0x18

复位值：0x0000 1113


该寄存器只能按字（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC2将不能被修改。0: TRIGSEL_ADC2 寄存器可读可写1: TRIGSEL_ADC2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连到接输出 0 的触发输入信号,输出 0 作为 ADC2_ROUTRG(ADC2 常规序列)的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.8. DAC0_OUT0 触发选择寄存器（TRIGSEL_DAC0OUT0）

地址偏移：0x1C

复位值：0x0000 0025


该寄存器只能按位（32位）访问。


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC0OUT0将不能被修改。0: TRIGSEL_DAC0OUT0 寄存器可读可写1: TRIGSEL_DAC0OUT0 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择</td></tr></table>

这些位用来选择连接到输出 0的触发输入信号，输出 0 作为DAC0_OUT0_EXTRIG（DAC0_OUT0 外部触发）的触发源。关于具体配置请参考 9-1.择

# 9.5.9. DAC0_OUT1 触发选择寄存器（TRIGSEL_DAC0OUT1）

地址偏移：0x20

复位值：0x0000 0025

该寄存器只能按位（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC0OUT1将不能被修改。0: TRIGSEL_DAC0OUT1 寄存器可读可写1: TRIGSEL_DAC0OUT1 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC0_OUT1_EXTRIG(DAC0_OUT1 外部触发)的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.10. TIMER0_BRKIN 触发选择寄存器（TRIGSEL_TIMER0BRKIN）

地址偏移：0x24

复位值：0x0023 2221

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

rw 

位/位域 名称 描述

<table><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0BRKIN将不能被修改。0: TRIGSEL_TIMER0BRKIN 寄存器可读可写1: TRIGSEL_TIMER0BRKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 的输入源选择这些位用来选择连接到输出 2 的触发输入信号,输出 2 作为 TIMER0_BRINK2 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TIMER0_BRINK1 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER0_BRINK0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.11. TIMER7_BRKIN 触发选择寄存器（TRIGSEL_TIMER7BRKIN）

地址偏移：0x28

复位值：0x0051 504F

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7BRKIN将不能被修改。0: TRIGSEL_TIMER7BRKIN 寄存器可读可写1: TRIGSEL_TIMER7BRKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 的输入源选择这些位用来选择连接到输出 2 的触发输入信号,输出 2 作为 TIMER7_BRKIN2 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出1的触发输入信号,输出1作为TIMER7_BRKIN1的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TIMER7_BRKIN0的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.12. TIMER14_BRKIN 触发选择寄存器（TRIGSEL_TIMER14BRKIN）

地址偏移：0x2C

复位值：0x0000 0059

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER14BRKIN将不能被修改。0: TRIGSEL_TIMER14BRKIN 寄存器可读可写1: TRIGSEL_TIMER14BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER14_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr></table>

# 9.5.13. TIMER15_BRKIN 触发选择寄存器（TRIGSEL_TIMER15BRKIN）

地址偏移：0x30

复位值：0x0000 005E

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER15BRKIN将不能被修改。0: TRIGSEL_TIMER15BRKIN 寄存器可读可写1: TRIGSEL_TIMER15BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER15_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.14. TIMER16_BRKIN 触发选择寄存器（TRIGSEL_TIMER16BRKIN）

地址偏移：0x34

复位值：0x0000 0063

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER16BRKIN将不能被修改。0: TRIGSEL_TIMER16BRKIN 寄存器可读可写1: TRIGSEL_TIMER16BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER16_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.15. TIMER40_BRKIN 触发选择寄存器（TRIGSEL_TIMER40BRKIN）

地址偏移：0x38

复位值：0x0000 0082

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER40BRKIN将不能被修改。0: TRIGSEL_TIMER40BRKIN 寄存器可读可写1: TRIGSEL_TIMER40BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER40_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr></table>

# 9.5.16. TIMER41_BRKIN 触发选择寄存器（TRIGSEL_TIMER41BRKIN）

地址偏移：0x3C

复位值：0x0000 0089

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER41BRKIN将不能被修改。0: TRIGSEL_TIMER41BRKIN 寄存器可读可写1: TRIGSEL_TIMER41BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER41_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.17. TIMER42_BRKIN 触发选择寄存器（TRIGSEL_TIMER42BRKIN）

地址偏移：0x40

复位值：0x0000 0090

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER42BRKIN将不能被修改。0: TRIGSEL_TIMER42BRKIN 寄存器可读可写1: TRIGSEL_TIMER42BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER42_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.18. TIMER43_BRKIN 触发选择寄存器（TRIGSEL_TIMER43BRKIN）

地址偏移：0x44

复位值：0x0000 0097

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER43BRKIN将不能被修改。0: TRIGSEL_TIMER43BRKIN 寄存器可读可写1: TRIGSEL_TIMER43BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为TIMER43_BRKINO的触发源。关于具体配置请参考表9-1.触发输入位域选择。</td></tr></table>

# 9.5.19. TIMER44_BRKIN 触发选择寄存器（TRIGSEL_TIMER44BRKIN）

地址偏移：0x48

复位值：0x0000 009e

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER44BRKIN将不能被修改。0: TRIGSEL_TIMER44BRKIN 寄存器可读可写1: TRIGSEL_TIMER44BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER44_BRKIN0 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.20. CAN0 触发选择寄存器（TRIGSEL_CAN0）

地址偏移：0x4C

复位值：0x0000 003d

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN0将不能被修改。0: TRIGSEL_CAN0 寄存器可读可写1: TRIGSEL_CAN0 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 CAN0_EX_TIME_TICK 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.21. CAN1 触发选择寄存器（TRIGSEL_CAN1）

地址偏移：0x50

复位值：0x0000 003d

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN1将不能被修改。0: TRIGSEL_CAN1 寄存器可读可写1: TRIGSEL_CAN1 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 CAN1_EX_TIME_TICK 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.22. CAN2 触发选择寄存器（TRIGSEL_CAN2）

地址偏移：0x54

复位值：0x0000 003d

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_CAN2将不能被修改。0: TRIGSEL_CAN2 寄存器可读可写1: TRIGSEL_CAN2 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 CAN2_EX_TIME_TICK 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.23. LPDTS 触发选择寄存器（TRIGSEL_LPDTS）

地址偏移：0x58

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_LP DTS将不能被修改。0: TRIGSEL_LP DTS 寄存器可读可写1: TRIGSEL_LP DTS 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 LPDTS_TRG 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.24. TIMER0_ETI 触发选择寄存器（TRIGSEL_TIMER0ETI）

地址偏移：0x5C

复位值：0x0000 0024

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0ETI将不能被修改。0: TRIGSEL_TIMER0ETI 寄存器可读可写1: TRIGSEL_TIMER0ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER0_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.25. TIMER1_ETI 触发选择寄存器（TRIGSEL_TIMER1ETI）

地址偏移：0x60

复位值：0x0000 002a

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER1ETI将不能被修改。0: TRIGSEL_TIMER1ETI 寄存器可读可写1: TRIGSEL_TIMER1ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出的触发输入信号,输出0作为TIMER1_ETI的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.26. TIMER2_ETI 触发选择寄存器（TRIGSEL_TIMER2ETI）

地址偏移：0x64

复位值：0x0000 0030

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ETI将不能被修改。0: TRIGSEL_TIMER2ETI 寄存器可读可写1: TRIGSEL_TIMER2ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER2_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.27. TIMER3_ETI 触发选择寄存器（TRIGSEL_TIMER3ETI）

地址偏移：0x68

复位值：0x0000 0036

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER3ETI将不能被修改。0: TRIGSEL_TIMER3ETI 寄存器可读可写1: TRIGSEL_TIMER3ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER3_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.28. TIMER4_ETI 触发选择寄存器（TRIGSEL_TIMER4ETI）

地址偏移：0x6C

复位值：0x0000 003c

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER4ETI将不能被修改。0: TRIGSEL_TIMER4ETI 寄存器可读可写1: TRIGSEL_TIMER4ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER4_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.29. TIMER7_ETI 触发选择寄存器（TRIGSEL_TIMER7ETI）

地址偏移：0x70

复位值：0x0000 0052

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7ETI将不能被修改。0: TRIGSEL_TIMER7ETI 寄存器可读可写1: TRIGSEL_TIMER7ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER7_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.30. TIMER22_ETI 触发选择寄存器（TRIGSEL_TIMER22ETI）

地址偏移：0x74

复位值：0x0000 0069

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER22ETI将不能被修改。0: TRIGSEL_TIMER22ETI 寄存器可读可写1: TRIGSEL_TIMER22ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER22_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.31. TIMER23_ETI 触发选择寄存器（TRIGSEL_TIMER23ETI）

地址偏移：0x78

复位值：0x0000 006f

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER23ETI将不能被修改。0: TRIGSEL_TIMER23ETI 寄存器可读可写1: TRIGSEL_TIMER23ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER23_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr></table>

# 9.5.32. TIMER30_ETI 触发选择寄存器（TRIGSEL_TIMER30ETI）

地址偏移：0x7C

复位值：0x0000 0075

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER30ETI将不能被修改。0: TRIGSEL_TIMER30ETI 寄存器可读可写1: TRIGSEL_TIMER30ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出的触发输入信号,输出0作为TIMER30_ETI的触发源。关于具体配置请参考表9-1.触发输入位域选择。</td></tr></table>

# 9.5.33. TIMER31_ETI 触发选择寄存器（TRIGSEL_TIMER31ETI）

地址偏移：0x80

复位值：0x0000 007b

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER31ETI将不能被修改。0: TRIGSEL_TIMER31ETI 寄存器可读可写1: TRIGSEL_TIMER31ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER31_ETI 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.34. EDOUT 触发选择寄存器（TRIGSEL_EDOUT）

地址偏移：0x84

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EDOUT将不能被修改。0: TRIGSEL_EDOUT 寄存器可读可写1: TRIGSEL_EDOUT 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 EDOUT_TRG 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.35. HPDF 触发选择寄存器（TRIGSEL_HPDF）

地址偏移：0x88

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_HPDF将不能被修改。0: TRIGSEL_HPDF 寄存器可读可写1: TRIGSEL_HPDF 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 HPDF_ITRG 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.36. TIMER0_ITI14 触发选择寄存器（TRIGSEL_TIMER0ITI14）

地址偏移：0x8C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0ITI14将不能被修改。0: TRIGSEL_TIMER0ITI14 寄存器可读可写1: TRIGSEL_TIMER0ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER0_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.37. TIMER1_ITI14 触发选择寄存器（TRIGSEL_TIMER1ITI14）

地址偏移：0x90

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER1ITI14将不能被修改。0: TRIGSEL_TIMER1ITI14 寄存器可读可写1: TRIGSEL_TIMER1ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER1_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.38. TIMER2_ITI14 触发选择寄存器（TRIGSEL_TIMER2ITI14）

地址偏移：0x94

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ITI14将不能被修改。0: TRIGSEL_TIMER2ITI14 寄存器可读可写1: TRIGSEL_TIMER2ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER2_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.39. TIMER3_ITI14 触发选择寄存器（TRIGSEL_TIMER3ITI14）

地址偏移：0x98

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER3ITI14将不能被修改。0: TRIGSEL_TIMER3ITI14 寄存器可读可写1: TRIGSEL_TIMER3ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出的触发输入信号,输出0作为TIMER3_ITI14的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.40. TIMER4_ITI14 触发选择寄存器（TRIGSEL_TIMER4ITI14）

地址偏移：0x9C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER4ITI14将不能被修改。0: TRIGSEL_TIMER4ITI14 寄存器可读可写1: TRIGSEL_TIMER4ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER4_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.41. TIMER7_ITI14 触发选择寄存器（TRIGSEL_TIMER7ITI14）

地址偏移：0xA0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7ITI14将不能被修改。0: TRIGSEL_TIMER7ITI14 寄存器可读可写1: TRIGSEL_TIMER7ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER7_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.42. TIMER14_ITI14 触发选择寄存器（TRIGSEL_TIMER14ITI14）

地址偏移：0xA4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER14ITI14将不能被修改。0: TRIGSEL_TIMER14ITI14 寄存器可读可写1: TRIGSEL_TIMER14ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER14_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.43. TIMER22_ITI14 触发选择寄存器（TRIGSEL_TIMER22ITI14）

地址偏移：0xA8

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER22ITI14将不能被修改。0: TRIGSEL_TIMER22ITI14 寄存器可读可写1: TRIGSEL_TIMER22ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER22_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.44. TIMER23_ITI14 触发选择寄存器（TRIGSEL_TIMER23ITI14）

地址偏移：0xAC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER23ITI14将不能被修改。0: TRIGSEL_TIMER23ITI14 寄存器可读可写1: TRIGSEL_TIMER23ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER23_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择</td></tr></table>

# 9.5.45. TIMER30_ITI14 触发选择寄存器（TRIGSEL_TIMER30ITI14）

地址偏移：0xB0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER30ITI14将不能被修改。0: TRIGSEL_TIMER30ITI14 寄存器可读可写1: TRIGSEL_TIMER30ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER30_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.46. TIMER31_ITI14 触发选择寄存器（TRIGSEL_TIMER31ITI14）

地址偏移：0xB4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER31ITI14将不能被修改。0: TRIGSEL_TIMER31ITI14 寄存器可读可写1: TRIGSEL_TIMER31ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER31_ITI14 的触发源。关于具体配置请参考表 9-1. 触发输入位域选择。</td></tr></table>

# 9.5.47. TIMER40_ITI14 触发选择寄存器（TRIGSEL_TIMER40ITI14）

地址偏移：0xB8

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER40ITI14将不能被修改。0: TRIGSEL_TIMER40ITI14 寄存器可读可写1: TRIGSEL_TIMER40ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER40_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.48. TIMER41_ITI14 触发选择寄存器（TRIGSEL_TIMER41ITI14）

地址偏移：0xBC

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER41ITI14将不能被修改。0: TRIGSEL_TIMER41ITI14 寄存器可读可写1: TRIGSEL_TIMER41ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER41_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.49. TIMER42_ITI14 触发选择寄存器（TRIGSEL_TIMER42ITI14）

地址偏移：0xC0

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER42ITI14将不能被修改。0: TRIGSEL_TIMER42ITI14 寄存器可读可写1: TRIGSEL_TIMER42ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER42_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.50. TIMER43_ITI14 触发选择寄存器（TRIGSEL_TIMER43ITI14）

地址偏移：0xC4

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="14">保留</td><td></td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER43ITI14将不能被修改。0: TRIGSEL_TIMER43ITI14 寄存器可读可写1: TRIGSEL_TIMER43ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER43_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>

# 9.5.51. TIMER44_ITI14 触发选择寄存器（TRIGSEL_TIMER44ITI14）

地址偏移：0xC8

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER44ITI14将不能被修改。0: TRIGSEL_TIMER44ITI14 寄存器可读可写1: TRIGSEL_TIMER44ITI14 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出的触发输入信号,输出 0 作为 TIMER44_ITI14 的触发源。关于具体配置请参考表9-1. 触发输入位域选择。</td></tr></table>
