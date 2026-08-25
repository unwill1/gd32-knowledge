## 16.4.5. TIMERx 寄存器(x=9,10,12,13)

TIMER9基地址：0x4001 5000

TIMER10基地址：0x4001 5400

TIMER12基地址：0x4000 1C00

TIMER13基地址：0x4000 2000

## 控制寄存器 0 (TIMERx_CTL0)

地址偏移：0x00

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="2">CKDIV[1:0]</td><td>ARSE</td><td colspan="4">保留</td><td>UPS</td><td>UPDIS</td><td>CEN</td></tr><tr><td colspan="6"></td><td colspan="2">rw</td><td>rw</td><td colspan="4"></td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:8</td><td>CKDIV[1:0]</td><td>时钟分频通过软件配置CKDIV,规定定时器时钟(CK_TIMER)与死区时间和数字滤波器采样时钟(DTS)之间的分频系数。00:<eq>f_{DTS}=f_{CK\_TIMER}</eq>01:<eq>f_{DTS}=f_{CK\_TIMER}/2</eq>10:<eq>f_{DTS}=f_{CK\_TIMER}/4</eq>11:保留</td></tr><tr><td>7</td><td>ARSE</td><td>自动重载影子使能0:禁能 TIMERx_CAR 寄存器的影子寄存器1:使能 TIMERx_CAR 寄存器的影子寄存器</td></tr><tr><td>6:3</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>2</td><td>UPS</td><td>更新请求源软件配置该位,选择更新事件源.0:以下事件均会产生更新中断或DMA请求:UPG位被置1计数器溢出/下溢复位模式产生的更新1:下列事件会产生更新中断或DMA请求:计数器溢出/下溢</td></tr><tr><td>1</td><td>UPDIS</td><td>禁止更新.该位用来使能或禁能更新事件的产生0:更新事件使能.更新事件发生时,相应的影子寄存器被装入预装载值,以下事件</td></tr></table>

均会产生更新事件：

UPG位被置1

计数器溢出/下溢

复位模式产生的更新

1：更新事件禁能.

注意：当该位被置 1 时，UPG位被置 1 或者复位模式不会产生更新事件，但是计数器和预分频器被重新初始化

0 CEN 计数器使能

0：计数器禁能

1：计数器使能

在软件将 CEN位置 1 后，外部时钟、暂停模式和编码器模式才能工作。

## 控制寄存器 1 (TIMERx_CTL1)

地址偏移：0x04

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="9">保留</td><td colspan="3">MMC[2:0]</td><td colspan="4">保留</td></tr></table>

rw 


位/位域 名称 描述


<table><tr><td>15:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>MMC[2:0]</td><td>主模式控制这些位控制TRGO信号的选择,TRGO信号由主定时器发给从定时器用于同步功能000:当产生一个定时器复位事件后,输出一个TRGO信号,定时器复位源为:主定时器产生一个复位事件TIMERx_SWEVG寄存器中UPG位置1001:当产生一个定时器使能事件后,输出一个TRGO信号,定时器使能源为:CEN位置1在暂停模式下,触发输入置1010:当产生一个定时器更新事件后,输出一个TRGO信号,更新事件源由UPDIS和UPS位决定011:当通道0在发生一次捕获或一次比较成功时,主模式控制器产生一个TRGO脉冲100:当产生一次比较事件时,输出一个TRGO信号,比较事件源来自O0CPRE101:保留110:保留111:保留</td></tr><tr><td>3</td><td>保留</td><td>必须保持复位值</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## DMA 和中断使能寄存器 (TIMERx_DMAINTEN)

地址偏移：0x0C

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CH0IE</td><td>UPIE</td></tr></table>


rw rw 


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHOIE</td><td>通道0比较/捕获中断使能0:禁止通道0中断1:使能通道0中断</td></tr><tr><td>0</td><td>UPIE</td><td>更新中断使能0:禁止更新中断1:使能更新中断</td></tr></table>

## 中断标志寄存器 (TIMERx_INTF)

地址偏移：0x10

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td>CH0OF</td><td colspan="7">保留</td><td>CH0IF</td><td>UPIF</td></tr><tr><td colspan="14">rc_w0</td><td>rc_w0</td><td>rc_w0</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9</td><td>CH0OF</td><td>通道0捕获溢出标志当通道0被配置为输入模式时,在CH0IF标志位已经被置1后,捕获事件再次发生时,该标志位可以由硬件置1。该标志位由软件清0.0:无捕获溢出中断发生1:发生了捕获溢出中断</td></tr><tr><td>8:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0IF</td><td>通道0比较/捕获中断标志此标志由硬件置1软件清0。当通道0在输入模式下时,捕获事件发生时此标志位被置1;当通道0在输出模式下时,此标志位在一个比较事件发生时被置1。当通道0在输入模式下时,读TIMERx_CH0CV会将此标志清0。0:无通道0中断发生</td></tr></table>

1：通道 0 中断发生

0 UPIF 

更新中断标志

此位在任何更新事件发生时由硬件置 1，软件清 0。

0：无更新中断发生

1：发生更新中断

## 软件事件产生寄存器 (TIMERx_SWEVG)

地址偏移：0x14

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CH0G</td><td>UPG</td></tr></table>

w w 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0G</td><td>通道0捕获或比较事件发生该位由软件置1,用于在通道0产生一个捕获/比较事件,由硬件自动清0。当此位被置1,CH0IF标志位被置1,若开启对应的中断和DMA,则发出相应的中断和DMA请求。此外,如果通道0配置为输入模式,计数器的当前值被TIMERx_CH0CV寄存器捕获,如果CH0IF标志位已经为1,则CH0OF标志位被置1。0:不产生通道0捕获或比较事件1:发生通道0捕获或比较事件</td></tr><tr><td>0</td><td>UPG</td><td>更新事件产生此位由软件置1,被硬件自动清0。当此位被置1并且向上计数模式,计数器被清0,预分频计数器将同时被清除。0:无更新事件产生1:产生更新事件</td></tr></table>

## 通道控制寄存器 0 (TIMERx_CHCTL0)

地址偏移：0x18

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td rowspan="2" colspan="8">保留</td><td>保留</td><td colspan="3">CH0COMCTL[2:0]</td><td>CH0COMSEN</td><td>CH0COMFEN</td><td rowspan="2" colspan="2">CH0MS[1:0]</td></tr><tr><td colspan="4">CH0CAPFLT[3:0]</td><td colspan="2">CH0CAPPSC[1:0]</td></tr></table>

rw 

rw 

rw 


输出比较模式：


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:7</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>6:4</td><td>CH0COMCTL[2:0]</td><td>通道0输出比较模式此位定义了输出准备信号O0CPRE的输出比较模式,而O0CPRE决定了CH0_O、CH0_ON的值。另外,O0CPRE高电平有效,而CH0_O、CH0_ON通道的极性取决于CH0P、CH0NP位。000:时基。输出比较寄存器TIMERx_CH0CV与计数器TIMERx_CNT间的比较对O0CPRE不起作用001:匹配时设置为高。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为高。010:匹配时设置为低。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE为低。011:匹配时翻转。当计数器的值与捕获/比较值寄存器TIMERx_CH0CV相同时,强制O0CPRE翻转。100:强制为低。强制O0CPRE为低电平101:强制为高。强制O0CPRE为高电平110:PWM模式0。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为高电平,否则为低电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为低电平,否则为高电平。111:PWM模式1。在向上计数时,一旦计数器值小于TIMERx_CH0CV时,O0CPRE为低电平,否则为高电平。在向下计数时,一旦计数器的值大于TIMERx_CH0CV时,O0CPRE为高电平,否则为低电平。如果配置在PWM模式下,只有当输出比较模式从时基模式变为PWM模式或者比较结果改变时,O0CPRE电平才改变。当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=00(比较模式)时此位不能被改变。</td></tr><tr><td>3</td><td>CH0COMSEN</td><td>通道0输出比较影子寄存器使能当此位被置1,TIMERx_CH0CV寄存器的影子寄存器被使能,影子寄存器在每次更新事件时都会被更新。0:禁止通道0输出/比较影子寄存器1:使能通道0输出/比较影子寄存器仅在单脉冲模式下(SPM=1),可以在未确认影子寄存器的情况下使用PWM模式当TIMERx_CCHP寄存器的PROT[1:0]=11且CH0MS=00时此位不能被改变。</td></tr><tr><td>2</td><td>CH0COMFEN</td><td>通道0输出比较快速使能当该位为1时,如果通道配置为PWM0模式或者PWM1模式,会加快捕获/比较输出对触发输入事件的响应。输出通道将触发输入信号的有效边沿作为一个比较匹配,CH0_O被设置为比较电平而与比较结果无关。0:禁止通道0输出比较快速.1:使能通道0输出比较快速。</td></tr><tr><td>1:0</td><td>CH0MS[1:0]</td><td>通道0I/O模式选择这些位定义了通道的工作模式和输入信号的选择。只有当通道关闭</td></tr></table>

(TIMERx_CHCTL2 寄存器的 CH0EN 位被清 0)时这些位才可写。

00：通道 0 配置为输出

01：通道 0 配置为输入，IS0映射在 CI0FE0 上

10：通道 0 配置为输入，IS0 映射在 CI1FE0 上

11：通道 0 配置为输入，IS0映射在 ITS 上

注意：当 CH0MS[1:0]=11 时，需要通过 TRGS 位（位于 TIMERx_SMCFG 寄存器）选择内部触发输入


输入捕获模式：


<table><tr><td>位/位域</td><td>名称</td><td colspan="3">描述</td></tr><tr><td>15:8</td><td>保留</td><td colspan="3">必须保持复位值。</td></tr><tr><td rowspan="18">7:4</td><td rowspan="18">CH0CAPFLT[3:0]</td><td colspan="3">通道0输入捕获滤波控制CIO输入信号可以通过数字滤波器进行滤波,该位域配置滤波参数。数字滤波器的基本原理:根据<eq>f_{SAMP}</eq>对CIO输入信号进行连续采样,并记录信号相同电平的次数。达到该位配置的滤波参数后,认为是有效电平。滤波器参数配置如下:</td></tr><tr><td>CH0CAPFLT [3:0]</td><td>采样次数</td><td><eq>f_{SAMP}</eq></td></tr><tr><td>4&#x27;b0000</td><td colspan="2">无滤波器</td></tr><tr><td>4&#x27;b0001</td><td>2</td><td rowspan="3"><eq>f_{CK\_TIMER}</eq></td></tr><tr><td>4&#x27;b0010</td><td>4</td></tr><tr><td>4&#x27;b0011</td><td>8</td></tr><tr><td>4&#x27;b0100</td><td>6</td><td rowspan="2"><eq>f_{DTS}/2</eq></td></tr><tr><td>4&#x27;b0101</td><td>8</td></tr><tr><td>4&#x27;b0110</td><td>6</td><td rowspan="2"><eq>f_{DTS}/4</eq></td></tr><tr><td>4&#x27;b0111</td><td>8</td></tr><tr><td>4&#x27;b1000</td><td>6</td><td rowspan="2"><eq>f_{DTS}/8</eq></td></tr><tr><td>4&#x27;b1001</td><td>8</td></tr><tr><td>4&#x27;b1010</td><td>5</td><td rowspan="3"><eq>f_{DTS}/16</eq></td></tr><tr><td>4&#x27;b1011</td><td>6</td></tr><tr><td>4&#x27;b1100</td><td>8</td></tr><tr><td>4&#x27;b1101</td><td>5</td><td rowspan="3"><eq>f_{DTS}/32</eq></td></tr><tr><td>4&#x27;b1110</td><td>6</td></tr><tr><td>4&#x27;b1111</td><td>8</td></tr><tr><td rowspan="16">3:2</td><td rowspan="16">CH0CAPPSC[1:0]</td><td rowspan="16" colspan="3">通道0输入捕获预分频器这2位定义了通道0输入的预分频系数。当TIMERx_CHCTL2寄存器中的CH0EN=0时,则预分频器复位。00:无预分频器,捕获输入口上检测到的每一个边沿都触发一次捕获01:每2个事件触发一次捕获10:每4个事件触发一次捕获11:每8个事件触发一次捕获</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

## 通道控制寄存器 2 (TIMERx_CHCTL2)

地址偏移：0x20

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="12">保留..</td><td>CH0NP</td><td>保留</td><td>CH0P</td><td>CH0EN</td></tr><tr><td colspan="12"></td><td>rw</td><td>rw</td><td>rw</td><td></td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:4</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>3</td><td>CH0NP</td><td>通道0互补输出极性当通道0配置为输出模式,此位定义了互补输出信号的极性。0:通道0互补输出高电平为有效电平1:通道0互补输出低电平为有效电平当通道0配置为输入模式时,此位和CH0P联合使用,作为输入信号CI0的极性选择控制信号。当TIMERx_CCHP寄存器的PROT[1:0]=11或10时此位不能被更改。</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CH0P</td><td>通道0极性当通道0配置为输出模式时,此位定义了输出信号极性。0:通道0高电平为有效电平1:通道0低电平为有效电平当通道0配置为输入模式时,此位定义了CI0信号极性[CH0NP, CH0P]将选择CI0FE0或者CI1FE0的有效边沿或者捕获极性[CH0NP==0, CH0P==0]:把CIxFE0的上升沿作为捕获或者从模式下触发的有效信号,并且CIxFE0不会被翻转。[CH0NP==0, CH0P==1]:把CIxFE0的下降沿作为捕获或者从模式下触发的有效信号,并且CIxFE0会被翻转。[CH0NP==1, CH0P==0]:保留。[CH0NP==1, CH0P==1]:保留。当TIMERx_CCHP寄存器的PROT[1:0]=11或10时此位不能被更改保留。</td></tr><tr><td>0</td><td>CH0EN</td><td>通道0捕获/比较使能当通道0配置为输出模式时,将此位置1使能CH0_O信号有效。当通道0配置为输入模式时,将此位置1使能通道0上的捕获事件。0:禁止通道01:使能通道0</td></tr></table>

## 计数器寄存器 (TIMERx_CNT)

地址偏移：0x24

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CNT[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:0</td><td>CNT[15:0]</td><td>这些位是当前的计数值。写操作能改变计数器值。</td></tr></table>

## 预分频寄存器 (TIMERx_PSC)

地址偏移：0x28

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">PSC[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:0</td><td>PSC[15:0]</td><td>计数器时钟预分频值计数器时钟等于 TIMER_CK 时钟除以(PSC+1),每次当更新事件产生时,PSC 的值被装入到对应的影子寄存器。</td></tr></table>

## 计数器自动重载寄存器 (TIMERx_CAR)

地址偏移：0x2C

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CARL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:0</td><td>CARL[15:0]</td><td>计数器自动重载值这些位定义了计数器的自动重载值。注意:在定时器被配置为输入捕获模式时,该寄存器需要被配置成一个大于用户期望值的非0值(例如0xFFFF)。</td></tr></table>

## 通道 0 捕获/比较值寄存器 (TIMERx_CH0CV)

地址偏移：0x34

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="16">CH0VAL[15:0]</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:0</td><td>CH0VAL[15:0]</td><td>通道 0 的捕获或比较值当通道 0 配置为输入模式时,这些位决定了上次捕获事件的计数器值。并且本寄存器为只读。当通道 0 配置为输出模式时,这些位包含了即将和计数器比较的值。使能相应影子寄存器后,影子寄存器值随每次更新事件更新。</td></tr></table>

## 配置寄存器 (TIMERx_CFG)

地址偏移：0xFC

复位值：0x0000

该寄存器可以按半字（16位）或字（32位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="14">保留</td><td>CHVSEL</td><td>保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>CHVSEL</td><td>写捕获比较寄存器选择位此位由软件写1或清0。1:当写入捕获比较寄存器的值与寄存器当前值相等时,写入操作无效0:无影响</td></tr><tr><td>0</td><td>保留</td><td>必须保持复位值。</td></tr></table>

