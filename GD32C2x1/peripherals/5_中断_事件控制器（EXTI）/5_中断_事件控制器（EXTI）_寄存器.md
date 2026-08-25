## 5.6. EXTI 寄存器

EXTI基地址：0x4001 0400

## 5.6.1. 中断使能寄存器（EXTI_INTEN）

地址偏移：0x00

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>INTEN23</td><td>INTEN22</td><td>INTEN21</td><td>INTEN20</td><td>INTEN19</td><td>INTEN18</td><td>INTEN17</td><td>INTEN16</td></tr><tr><td colspan="8"></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>INTEN15</td><td>INTEN14</td><td>INTEN13</td><td>INTEN12</td><td>INTEN11</td><td>INTEN10</td><td>INTEN9</td><td>INTEN8</td><td>INTEN7</td><td>INTEN6</td><td>INTEN5</td><td>INTEN4</td><td>INTEN3</td><td>INTEN2</td><td>INTEN1</td><td>INTENO</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>INTENx</td><td>中断使能位x(x=0..23)0:第x中断被禁止1:第x中断被使能</td></tr></table>

## 5.6.2. 事件使能寄存器（EXTI_EVEN）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>EVEN23</td><td>EVEN22</td><td>EVEN21</td><td>EVEN20</td><td>EVEN19</td><td>EVEN18</td><td>EVEN17</td><td>EVEN16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>EVEN15</td><td>EVEN14</td><td>EVEN13</td><td>EVEN12</td><td>EVEN11</td><td>EVEN10</td><td>EVEN9</td><td>EVEN8</td><td>EVEN7</td><td>EVEN6</td><td>EVEN5</td><td>EVEN4</td><td>EVEN3</td><td>EVEN2</td><td>EVEN1</td><td>EVEN0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>EVENx</td><td>事件使能位x(x=0..23)0:第x事件被禁止1:第x事件被使能</td></tr></table>

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>FTEN23</td><td>FTEN22</td><td>FTEN21</td><td>FTEN20</td><td>FTEN19</td><td>FTEN18</td><td>FTEN17</td><td>FTEN16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

## 5.6.3. 上升沿触发使能寄存器（EXTI_RTEN）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>RTEN23</td><td>RTEN22</td><td>RTEN21</td><td>RTEN20</td><td>RTEN19</td><td>RTEN18</td><td>RTEN17</td><td>RTEN16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RTEN15</td><td>RTEN14</td><td>RTEN13</td><td>RTEN12</td><td>RTEN11</td><td>RTEN10</td><td>RTEN9</td><td>RTEN8</td><td>RTEN7</td><td>RTEN6</td><td>RTEN5</td><td>RTEN4</td><td>RTEN3</td><td>RTEN2</td><td>RTEN1</td><td>RTENO</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>RTENx</td><td>上升沿触发使能(x=0..23)0:第x线上升沿触发无效1:第x线上升沿触发有效(中断/事件请求)</td></tr></table>

## 5.6.4. 下降沿触发使能寄存器（EXTI_FTEN）

地址偏移：0x0C

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>FTEN15</td><td>FTEN14</td><td>FTEN13</td><td>FTEN12</td><td>FTEN11</td><td>FTEN10</td><td>FTEN9</td><td>FTEN8</td><td>FTEN7</td><td>FTEN6</td><td>FTEN5</td><td>FTEN4</td><td>FTEN3</td><td>FTEN2</td><td>FTEN1</td><td>FTENO</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>FTENx</td><td>下降沿触发使能(x=0..23)0:第x线下降沿触发无效1:第x线下降沿触发有效(中断/事件请求)</td></tr></table>

## 5.6.5. 软件中断事件寄存器（EXTI_SWIEV）

地址偏移：0x10

复位值：0x0000 0000

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>SWIEV23</td><td>SWIEV22</td><td>SWIEV21</td><td>SWIEV20</td><td>SWIEV19</td><td>SWIEV18</td><td>SWIEV17</td><td>SWIEV16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SWIEV15</td><td>SWIEV14</td><td>SWIEV13</td><td>SWIEV12</td><td>SWIEV11</td><td>SWIEV10</td><td>SWIEV9</td><td>SWIEV8</td><td>SWIEV7</td><td>SWIEV6</td><td>SWIEV5</td><td>SWIEV4</td><td>SWIEV3</td><td>SWIEV2</td><td>SWIEV1</td><td>SWIEV0</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>SWIEVx</td><td>中断/事件软件触发x(x=0..23)0:禁用EXTI线x软件中断/事件请求1:激活EXTI线x软件中断/事件请求</td></tr></table>

## 5.6.6. 挂起寄存器（EXTI_PD）

地址偏移：0x14

复位值：0xXXXX XXXX，X表示未定义。

该寄存器只能按字（32位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="8">保留</td><td>PD23</td><td>PD22</td><td>PD21</td><td>PD20</td><td>PD19</td><td>PD18</td><td>PD17</td><td>PD16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>PD15</td><td>PD14</td><td>PD13</td><td>PD12</td><td>PD11</td><td>PD10</td><td>PD9</td><td>PD8</td><td>PD7</td><td>PD6</td><td>PD5</td><td>PD4</td><td>PD3</td><td>PD2</td><td>PD1</td><td>PD0</td></tr><tr><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td><td>rc_w1</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:24</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>23:0</td><td>PDx</td><td>中断挂起状态x(x=0..23)0:EXTI线x没有被触发1:EXTI线x被触发,对这些位写1,可将其清0。</td></tr></table>
