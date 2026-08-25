## 9.4. CRC 寄存器

CRC 基地址：0x4002 3000

## 9.4.1. 数据寄存器（CRC_DATA）

地址偏移：0x00

复位值：0xFFFF FFFF

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">DATA[31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">DATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>DATA[31:0]</td><td>CRC 计算结果位软件可读可写。该寄存器用于接收待计算的新数据,直接将其写入即可。刚写入的数据不能被读出来因为读取该寄存器得到的是上次 CRC 计算的结果。</td></tr></table>

## 9.4.2. 独立数据寄存器（CRC_FDATA）

地址偏移：0x04

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="8">FDATA[7:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7:0</td><td>FDATA[7:0]</td><td>独立数据寄存器位软件可读可写。这些位与CRC计算无关。该字节能被任何其他外设用于其他任何目的。该字节不受CRC_CTL寄存器的影响。</td></tr></table>

## 9.4.3. 控制寄存器（CRC_CTL）

地址偏移：0x08

复位值：0x0000 0000

该寄存器只能按字（32 位）访问。

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr></table>

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>REV_O</td><td colspan="2">REV_I[1:0]</td><td colspan="2">PS[1:0]</td><td colspan="2">保留</td><td>RST</td></tr><tr><td colspan="8"></td><td>rw</td><td colspan="2">rw</td><td colspan="2">rw</td><td colspan="2"></td><td>rs</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:8</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>7</td><td>REV_O</td><td>按位顺序翻转输出数据功能0:输出数据不翻转1:输出数据按位顺序翻转</td></tr><tr><td>6:5</td><td>REV_I[1:0]</td><td>翻转输入数据功能0:输入数据不翻转1:输入数据按字节翻转2:输入数据按半字翻转3:输入数据按字翻转</td></tr><tr><td>4:3</td><td>PS[1:0]</td><td>多项式长度0:32位1:16(POLY[15:0]用于计数)位2:8(POLY[7:0]用于计数)位3:7(POLY[6:0]用于计数)位</td></tr><tr><td>2:1</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>0</td><td>RST</td><td>软件可读写该位用来复位CRC_DATA寄存器。置位时,CRC_DATA寄存器的值将自动初始化为CRC_IDATA寄存器中的值,然后自动清零。该位对CRC_FDATA寄存器没有影响。</td></tr></table>

## 9.4.4. 初值寄存器（CRC_IDATA）

地址偏移：0x10

复位值：0xFFFF FFFF

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">IDATA [31:16]rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">IDATA[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>IDATA[31:0]</td><td>配置 CRC 初值CRC_CTL 寄存器的 RST 位置位后,CRC_DATA 寄存器的值将被更新为此寄存器的值。</td></tr></table>

## 9.4.5. 多项式寄存器（CRC_POLY）

地址偏移：0x14

复位值：0x04C1 1DB7


该寄存器只能按字（32 位）访问


<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">POLY [31:16]</td></tr><tr><td colspan="16">rw</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">POLY[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>POLY[31:0]</td><td>配置多项式值配合PS[1:0]使用。</td></tr></table>
