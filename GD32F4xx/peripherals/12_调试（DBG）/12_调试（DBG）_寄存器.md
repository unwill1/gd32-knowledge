## 12.4. DBG 寄存器

DBG 基地址：0xE0042000U

## 12.4.1. ID 寄存器 (DBG_ID)

地址偏移：0x00

只读寄存器

该寄存器只能按字（32 位）访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">ID_CODE[31:16]</td></tr><tr><td colspan="16">r</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">ID_CODE[15:0]</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:0</td><td>ID_CODE[31:0]</td><td>DBG ID 寄存器这些位由软件读取,这些位是不变的常数</td></tr></table>

## 12.4.2. 控制寄存器 0（DBG_CTL0)

地址偏移：0x04

复位值：0x0000 0000，仅上电复位

该寄存器只能按字(32 位)访问

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td></tr><tr><td colspan="16">保留</td></tr><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="10">保留</td><td>TRACE_IOEN</td><td colspan="2">保留</td><td>STB_HOLD</td><td>DSLP_HOLD</td><td>SLP_HOLD</td></tr><tr><td colspan="10"></td><td>rw</td><td colspan="2"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>31:6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>TRACE_IOEN</td><td>跟踪引脚分配使能该位由软件置位和复位0:跟踪引脚分配禁用1:跟踪引脚分配使能。</td></tr><tr><td>4:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>STB_HOLD</td><td>待机模式保持位该位由软件置位和复位</td></tr></table>
