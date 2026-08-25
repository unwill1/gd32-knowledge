## 12.5. TRIGSEL 寄存器

TRIGSEL 基地址：0x4001 4400

## 12.5.1. EXTOUT 触发选择寄存器 0（TRIGSEL_EXTOUT_0）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_0将不能被修改。0: TRIGSEL_EXTOUT_0 寄存器可写可读1: TRIGSEL_EXTOUT_0 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT1(外部输出 1)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT0(外部输出 0)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.2. EXTOUT 触发选择寄存器 1（TRIGSEL_EXTOUT_1）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr><tr><td colspan="8">rw</td><td colspan="8">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_1将不能被修改。0: TRIGSEL_EXTOUT_1 寄存器可写可读1: TRIGSEL_EXTOUT_1 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT3(外部输出 3)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT2(外部输出 2)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.3. EXTOUT 触发选择寄存器 2（TRIGSEL_EXTOUT_2）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_2将不能被修改。0: TRIGSEL_EXTOUT_2 寄存器可读可写1: TRIGSEL_EXTOUT_2 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择</td></tr></table>

这些位用来选择连接到输出 1的触发输入信号，输出 1 作为TRIGSEL_OUT5（外部输出 5）的信号源。关于具体配置请参考 12-1. 。

7:0 INSEL0[7:0] 触发输出 0 的输入源选择

这些位用来选择连接到输出 0的触发输入信号，输出 0 作为TRIGSEL_OUT4（外部输出 4）的信号源。关于具体配置请参考 12-1. 。

## 12.5.4. EXTOUT 触发选择寄存器 3（TRIGSEL_EXTOUT_3）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_EXTOUT_3将不能被修改。0: TRIGSEL_EXTOUT_3 寄存器可读可写1: TRIGSEL_EXTOUT_3 寄存器只读</td></tr><tr><td>30:16</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 的输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TRIGSEL_OUT7(外部输出 7)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_OUT6(外部输出 6)的信号源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.5. TIMER0_ITI 触发选择寄存器（TRIGSEL_TIMER0ITI）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0ITI将不能被修改。0: TRIGSEL_TIMER0ITI 寄存器可读可写1: TRIGSEL_TIMER0ETI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER0_ETI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.6. TIMER1_ITI 触发选择寄存器（TRIGSEL_TIMER1ITI）

地址偏移：0x14

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER1ITI将不能被修改。0: TRIGSEL_TIMER1ITI 寄存器可读可写1: TRIGSEL_TIMER1ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择</td></tr></table>

这些位用来选择连接到输出 0的触发输入信号，输出 0 作为TIMER1_ITI 的触发源。关于具体配置请参考 12-1. 。

## 12.5.7. TIMER2_ITI 触发选择寄存器（TRIGSEL_TIMER2ITI）

地址偏移：0x18

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ITI将不能被修改。0: TRIGSEL_TIMER2ITI 寄存器可读可写1: TRIGSEL_TIMER2ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER2_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.8. TIMER3_ITI 触发选择寄存器（TRIGSEL_TIMER3ITI）

地址偏移：0x1C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER2ITI将不能被修改。0: TRIGSEL_TIMER3ITI 寄存器可读可写1: TRIGSEL_TIMER3ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER3_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.9. TIMER4_ITI 触发选择寄存器（TRIGSEL_TIMER4ITI）

地址偏移：0x20

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER4ITI将不能被修改。0: TRIGSEL_TIMER4ITI 寄存器可读可写1: TRIGSEL_TIMER4ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER4_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.10. TIMER7_ITI 触发选择寄存器（TRIGSEL_TIMER7ITI）

地址偏移：0x24

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td colspan="15"></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7ITI将不能被修改。0: TRIGSEL_TIMER7ITI 寄存器可读可写1: TRIGSEL_TIMER7ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER7_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.11. TIMER15_ITI 触发选择寄存器（TRIGSEL_TIMER15ITI）

地址偏移：0x2C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER15ITI将不能被修改。0: TRIGSEL_TIMER15ITI 寄存器可读可写1: TRIGSEL_TIMER15ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER15_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.12. TIMER16_ITI 触发选择寄存器（TRIGSEL_TIMER16ITI）

地址偏移：0x30

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER16ITI将不能被修改。0: TRIGSEL_TIMER16ITI 寄存器可读可写1: TRIGSEL_TIMER16ITI 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER16_ITI 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.13. DAC 触发选择寄存器（TRIGSEL_DAC）

地址偏移：0x34

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_DAC将不能被修改。0: TRIGSEL_DAC 寄存器可读可写1: TRIGSEL_DAC 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 DAC_OUT_EXTRIG (DAC_OUT 外部触发)的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.14. ADC0_ROUTRG 触发选择寄存器（TRIGSEL_ADC0_ROUTRG）

地址偏移：0x38

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC0_ROUTRG将不能被修改。0: TRIGSEL_ADC0_ROUTRG 寄存器可读可写1: TRIGSEL_ADC0_ROUTRG 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TRIGSEL_ADC0_ROUTRG 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.15. ADC0_INSTRG 触发选择寄存器（TRIGSEL_ADC0_INSTRG）

地址偏移：0x3C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC0_INSTRG将不能被修改。0: TRIGSEL_ADC0_INSTRG 寄存器可读可写1: TRIGSEL_ADC0_INSTRG 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC0_INSTRG 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.16. ADC1_ROUTRG 触发选择寄存器（TRIGSEL_ADC1_ROUTRG）

地址偏移：0x40

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>3130:8</td><td>LK保留</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC1_ROUTRG 将不能被修改。0: TRIGSEL_ADC1_ROUTRG 寄存器可读可写1: TRIGSEL_ADC1_ROUTRG 寄存器只读必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出0的输入源选择这些位用来选择连接到输出0的触发输入信号,输出0作为ADC1_ROUTRG的触发源。关于具体配置请参考表12-1.触发输入位域选择。</td></tr></table>

## 12.5.17. ADC1_INSTRG 触发选择寄存器（TRIGSEL_ADC1_INSTRG）

地址偏移：0x44

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC1_INSTRG将不能被修改。0: TRIGSEL_ADC1_INSTRG 寄存器可读可写1: TRIGSEL_ADC1_INSTRG 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC1_INSTRG 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.18. ADC2_ROUTRG 触发选择寄存器（TRIGSEL_ADC2_ROUTRG）

地址偏移：0x48

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC2_ROUTRG将不能被修改。0: TRIGSEL_ADC2_ROUTRG 寄存器可读可写1: TRIGSEL_ADC2_ROUTRG 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC2_ROUTRG 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.19. ADC2_INSTRG 触发选择寄存器（TRIGSEL_ADC2_INSTRG）

地址偏移：0x4C

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_ADC2_INSTRG将不能被修改。0: TRIGSEL_ADC2_INSTRG 寄存器可读可写1: TRIGSEL_ADC2_INSTRG 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 ADC2_INSTRG 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.20. TIMER0_BRKIN 触发选择寄存器（TRIGSEL_TIMER0BRKIN）

地址偏移：0x50

复位值：0x0000 0042

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0BRKIN将不能被修改。0: TRIGSEL_TIMER0BRKIN 寄存器可读可写1: TRIGSEL_TIMER0BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER0_BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.21. TIMER0_CHBRKIN 触发选择寄存器（TRIGSEL_TIMER0CHBRKIN）

地址偏移：0x54

复位值：0x0045 4443

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER0CHBRKIN将不能被修改。0: TRIGSEL_TIMER0BRKIN 寄存器可读可写1: TRIGSEL_TIMER0BRKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 输入源选择这些位用来选择连接到输出 2 的触发输入信号, 输出 2 作为 TIMER0_CH2BRINK 的触发源。关于具体配置请参考表12-1.触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 输入源选择这些位用来选择连接到输出 1 的触发输入信号, 输出 1 作为 TIMER0_CH1BRINK 的触发源。关于具体配置请参考表12-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号, 输出 0 作为 TIMER0_CH0BRINK 的触发源。关于具体配置请参考表12-1.触发输入位域选择。</td></tr></table>

## 12.5.22. TIMER7_BRKIN 触发选择寄存器（TRIGSEL_TIMER7BRKIN）

地址偏移：0x58

复位值：0x0000 0046

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7BRKIN将不能被修改。0: TRIGSEL_TIMER7BRKIN 寄存器可读可写1: TRIGSEL_TIMER7BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER7_BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.23. TIMER7_CHBRKIN 触发选择寄存器（TRIGSEL_TIMER7CHBRKIN）

地址偏移：0x5C

复位值：0x0049 4847

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="7">保留</td><td colspan="8">INSEL2[7:0]</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="8">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">INSEL1[7:0]</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER7CHBRKIN将不能被修改。0: TRIGSEL_TIMER7BRKIN 寄存器可读可写1: TRIGSEL_TIMER7BRKIN 寄存器只读</td></tr><tr><td>30:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:16</td><td>INSEL2[7:0]</td><td>触发输出 2 输入源选择这些位用来选择连接到输出 2 的触发输入信号,输出 2 作为 TIMER7_CH2BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr><tr><td>15:8</td><td>INSEL1[7:0]</td><td>触发输出 1 输入源选择这些位用来选择连接到输出 1 的触发输入信号,输出 1 作为 TIMER7_CH1BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER7_CH0BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.24. TIMER15_BRKIN 触发选择寄存器（TRIGSEL_TIMER15BRKIN）

地址偏移：0x60

复位值：0x0000 004A

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>保留</td><td>INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER15BRKIN将不能被修改。0: TRIGSEL_TIMER15BRKIN 寄存器可读可写1: TRIGSEL_TIMER15BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER15_BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>

## 12.5.25. TIMER16_BRKIN 触发选择寄存器（TRIGSEL_TIMER16BRKIN）

地址偏移：0x64

复位值：0x0000 004B

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td>LK</td><td colspan="15">保留</td></tr><tr><td>rs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">INSEL0[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31</td><td>LK</td><td>TRIGSEL 寄存器锁定标志位该位通过软件置位,通过系统复位清除。该位置位后,TRIGSEL_TIMER16BRKIN将不能被修改。0: TRIGSEL_TIMER16BRKIN 寄存器可读可写1: TRIGSEL_TIMER16BRKIN 寄存器只读</td></tr><tr><td>30:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:0</td><td>INSEL0[7:0]</td><td>触发输出 0 的输入源选择这些位用来选择连接到输出 0 的触发输入信号,输出 0 作为 TIMER16_BRINK 的触发源。关于具体配置请参考表 12-1.触发输入位域选择。</td></tr></table>
