## 24.7. USBD 寄存器

USBD 基地址：0x4000 5C00

## 24.7.1. USBD 控制寄存器 (USBD_CTL)

地址偏移：0x40

复位值：0x0003

该寄存器可半字(16 位)或全字(32 位)访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STIE</td><td>PMOUIE</td><td>ERRIE</td><td>WKUPIE</td><td>SPSIE</td><td>RSTIE</td><td>SOFIE</td><td>ESOFIE</td><td>L1REQIE</td><td>保留</td><td>L1RSREQ</td><td>RSREQ</td><td>SETSPS</td><td>LOWM</td><td>CLOSE</td><td>SETRST</td></tr><tr><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td></td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15</td><td>STIE</td><td>成功传输中断使能</td></tr><tr><td></td><td></td><td>0:禁用成功传输中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的STIF位被置位,产生中断</td></tr><tr><td>14</td><td>PMOUIE</td><td>包缓冲上溢/下溢中断使能</td></tr><tr><td></td><td></td><td>0:当包缓冲上溢/下溢不产生中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的PMOUIF位被置位,产生中断.</td></tr><tr><td>13</td><td>ERRIE</td><td>错误中断使能</td></tr><tr><td></td><td></td><td>0:禁用错误中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的ERRIF位被置位,产生中断</td></tr><tr><td>12</td><td>WKUPIE</td><td>唤醒中断使能</td></tr><tr><td></td><td></td><td>0:禁用唤醒中断</td></tr><tr><td></td><td></td><td>1:当USB_IFR寄存器的WKUPIF位被置位,产生中断</td></tr><tr><td>11</td><td>SPSIE</td><td>挂起状态中断使能</td></tr><tr><td></td><td></td><td>0:禁用挂起状态中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的SPSIF位被置位,产生中断</td></tr><tr><td>10</td><td>RSTIE</td><td>USB复位中断使能</td></tr><tr><td></td><td></td><td>0:禁用USB复位中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的RSTIF位被置位,产生中断</td></tr><tr><td>9</td><td>SOFIE</td><td>帧起始中断使能</td></tr><tr><td></td><td></td><td>0:禁用帧起始中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的SOFIF位被置位,产生中断</td></tr><tr><td>8</td><td>ESOFIE</td><td>预期的帧起始中断使能</td></tr><tr><td></td><td></td><td>0:禁用预期的帧起始中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的ESOFIF位被置位,产生中断</td></tr><tr><td>7</td><td>L1REQIE</td><td>LPM L1状态请求中断使能</td></tr><tr><td></td><td></td><td>0:禁用LPM L1状态请求中断</td></tr><tr><td></td><td></td><td>1:当USBD_INTF寄存器的L1REQ位被置位,产生中断</td></tr><tr><td>6</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>5</td><td>L1RSREQ</td><td>LPM L1恢复请求</td></tr><tr><td></td><td></td><td>MCU可以设置此位来发送一个LPM L1恢复信号给主机。在信号发送过程结束后,硬件会清除此位。</td></tr><tr><td>4</td><td>RSREQ</td><td>恢复请求</td></tr><tr><td></td><td></td><td>软件向USB主机设置一个中断请求,USB主机应该按USB规范驱动这个恢复序列</td></tr><tr><td></td><td></td><td>0:没有恢复请求</td></tr><tr><td></td><td></td><td>1:发送恢复请求</td></tr><tr><td>3</td><td>SETSPS</td><td>设置挂起</td></tr><tr><td></td><td></td><td>当USBD_INTF寄存器的SPSIF位被置位时,软件应该设置挂起状态</td></tr><tr><td></td><td></td><td>0:没有设置挂起状态</td></tr><tr><td></td><td></td><td>1:设置挂起状态</td></tr><tr><td>2</td><td>LOWM</td><td>低功耗状态</td></tr><tr><td></td><td></td><td>当置位这一位时,USB在挂起状态进入低功耗模式。如果从挂起状态恢复,硬件会复位这一位。</td></tr><tr><td></td><td></td><td>0:无影响</td></tr><tr><td></td><td></td><td>1:在挂起模式进入低功耗模式</td></tr><tr><td>1</td><td>CLOSE</td><td>关闭状态</td></tr><tr><td></td><td></td><td>当这一位被置位的时候,USBD进入关闭状态,并且完全关闭USBD,同主机断开</td></tr><tr><td></td><td></td><td>0:不在关断状态</td></tr><tr><td></td><td></td><td>1:在关断状态</td></tr><tr><td>0</td><td>SETRST</td><td>设定复位</td></tr><tr><td></td><td></td><td>当这位置位,USBD外设应该被复位</td></tr><tr><td></td><td></td><td>0:无影响</td></tr><tr><td></td><td></td><td>1:发生复位</td></tr></table>

## 24.7.2. USBD 中断标志寄存器 (USBD_INTF)

地址偏移：0x44

复位值：0x0000

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>STIF</td><td>PMOUIF</td><td>ERRIF</td><td>WKUPIF</td><td>SPSIF</td><td>RSTIF</td><td>SOFIF</td><td>ESOFIF</td><td>L1REQ</td><td colspan="2">保留</td><td>DIR</td><td></td><td colspan="3">EPNUM[3:0]</td></tr><tr><td>r</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td>rc_w0</td><td colspan="2"></td><td>r</td><td></td><td colspan="3">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15</td><td>STIF</td><td>成功传输中断标志当一个会话成功完成时,硬件置位该位</td></tr><tr><td>14</td><td>PMOUIF</td><td>包缓冲溢出/下溢中断标志硬件置位该位表示包缓冲区存储不下所有所传输的数据。软件写0清该位</td></tr><tr><td>13</td><td>ERRIF</td><td>错误中断标志当在会话期间有错误发生时,硬件置位该位。软件写0清该位</td></tr><tr><td>12</td><td>WKUPIF</td><td>唤醒中断标志在SUSPEND状态下,当总线上有活动被检测到时,硬件置位该位。软件写0清该位</td></tr><tr><td>11</td><td>SPSIF</td><td>挂起状态中断标志当USB总线无任何活动超过3ms时,硬件置位该位,表明有SUSPEND请求。软件写0清该位</td></tr><tr><td>10</td><td>RSTIF</td><td>USB复位中断标志当检测到USB RESET信号时硬件置位该位。软件写0清该位</td></tr><tr><td>9</td><td>SOFIF</td><td>帧起始中断标志一个新的SOF包到达时硬件置位该位。软件写0清该位</td></tr><tr><td>8</td><td>ESOFIF</td><td>预期的帧起始中断标志硬件置位表示一个SOF被预期但是还没有到达。软件写0清该位</td></tr><tr><td>7</td><td>L1REQ</td><td>当LPM L1事务被正确地接受和响应后,硬件会置位此位。软件写0清该位。</td></tr><tr><td>7:5</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>4</td><td>DIR</td><td>会话传输方向硬件置位表示会话的传输方向0:IN类型1:OUT类型</td></tr><tr><td>3:0</td><td>EPNUM[3:0]</td><td>端点号硬件置位确认当前会话所关联的端点</td></tr></table>

## 24.7.3. USBD 状态寄存器 (USBD_STAT)

地址偏移：0x48

复位值：0x0XXX 这里X是未定义的

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RX_DP</td><td>RX_DM</td><td>LOCK</td><td colspan="2">SOFLN[1:0]</td><td colspan="11">FCNT[10:0]</td></tr><tr><td>r</td><td>r</td><td>r</td><td colspan="2">r</td><td colspan="11">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15</td><td>RX_DP</td><td>接收数据 + 线状态代表DP线的状态</td></tr><tr><td>14</td><td>RX_DM</td><td>接收数据 - 线状态代表DM线的状态</td></tr><tr><td>13</td><td>LOCK</td><td>锁定USB硬件置位表明接收到了至少两个连续SOF包</td></tr><tr><td>12:11</td><td>SOFLN[1:0]</td><td>丢失SOF当每次发生ESOFIF事件时,硬件递增此位,一旦再次接收到SOF则清除该位</td></tr><tr><td>10:0</td><td>FCNT[10:0]</td><td>帧编号计数器每次收到SOF,帧编号计数器将会增加</td></tr></table>

## 24.7.4. USBD 设备地址寄存器 (USBD_ADDR)

地址偏移：0x4C

复位值：0x0000

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td>USBEN</td><td colspan="7">USBDAR[6:0]</td></tr><tr><td colspan="8"></td><td>rw</td><td colspan="7">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7</td><td>USBEN</td><td>USB设备使能通过软件设置该位使能USB设备0: USB设备禁用。没有会话要处理1: USB设备使能</td></tr><tr><td>6:0</td><td>USBDAR[6:0]</td><td>USBD设备地址总线复位之后,地址被复位为0x00。若USB使能位被置位,则从设备会响应功能地址DEV_ADDR的报文。</td></tr></table>

## 24.7.5. USBD 缓冲器地址寄存器 (USBD_BADDR)

地址偏移：0x50

复位值：0x0000

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="13">BAR[12:0]</td><td colspan="3">保留</td></tr></table>


rw


<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:3</td><td>BAR[12:0]</td><td>缓冲器地址所分配缓冲器(512byte on-chip SRAM)的起始地址,用来保存缓冲描述符表以及包缓冲</td></tr><tr><td>2:0</td><td>保留</td><td>必须保持复位值</td></tr></table>

## 24.7.6. USBD 端点 x 控制/状态寄存器 (USB_EPxCS), x=[0..7]

地址偏移：0x00 to 0x1C

复位值：0x0000

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>RX_ST</td><td>RX_DTG</td><td colspan="2">RX_STA[1:0]</td><td>SETUP</td><td colspan="2">EP_CTL[1:0]</td><td>EP_KCTL</td><td>TX_ST</td><td>TX_DTG</td><td colspan="2">TX_STA[1:0]</td><td colspan="4">EP_AR[3:0]</td></tr><tr><td>rc_w0</td><td>t</td><td colspan="2">t</td><td>r</td><td colspan="2">rw</td><td>rw</td><td>rc_w0</td><td>t</td><td colspan="2">t</td><td colspan="4">rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15</td><td>RX_ST</td><td>正确接收当一个成功的OUT/SETUP会话完成时,硬件置位此位通过软件写0清该位</td></tr><tr><td>14</td><td>RX_DTG</td><td>接收数据PID翻转位本标志位代表非同步端点的翻转数据位(0=DATA0, 1=DATA1)用来实现双缓冲端点的流控功能用于同步端点的缓冲区交换</td></tr><tr><td>13:12</td><td>RX_STA[1:0]</td><td>接收状态位通过软件写1翻转写0保持不变参考下表</td></tr><tr><td>11</td><td>SETUP</td><td>Setup会话完成当一个SETUP会话完成时,硬件置位此位</td></tr><tr><td>10:9</td><td>EP_CTL[1:0]</td><td>端点类型控制I</td></tr></table>

<table><tr><td></td><td></td><td>参考下表</td></tr><tr><td>8</td><td>EP_KCTL</td><td>端点类别控制其具体含义取决于端点类型的设置参考下表</td></tr><tr><td>7</td><td>TX_ST</td><td>正确发送当一个IN会话成功完成时,硬件置位此位软件清0</td></tr><tr><td>6</td><td>TX_DTG</td><td>发送数据PID翻转位本标志位代表非同步端点的翻转数据位(0=DATA0, 1=DATA1)用来实现双缓冲端点的流控功能用于同步端点的缓冲区交换</td></tr><tr><td>5:4</td><td>TX_STA[1:0]</td><td>发送状态位参考下表</td></tr><tr><td>3:0</td><td>EP_AR</td><td>端点地址用来指示会话的目标端点</td></tr></table>


表 24-1 接收状态编码


<table><tr><td>RX_STA[1:0]</td><td>含义</td></tr><tr><td>00</td><td>DISABLED:忽略此端点的所有接收请求</td></tr><tr><td>01</td><td>STALL:握手状态为STALL</td></tr><tr><td>10</td><td>NAK:握手状态为NAK</td></tr><tr><td>11</td><td>VALID:使能端点的接收</td></tr></table>


表 24-2. 端点类型编码


<table><tr><td>EP_CTL[1:0]</td><td>含义</td></tr><tr><td>00</td><td>BULK:批量端点</td></tr><tr><td>01</td><td>CONTROL:控制端点</td></tr><tr><td>10</td><td>ISO:同步端点</td></tr><tr><td>11</td><td>INTERRUPT:中断端点</td></tr></table>


表 24-3. 端点类别编码


<table><tr><td colspan="2">EP_KCTL[1:0]</td><td>EP_KCTL 含义</td></tr><tr><td>00</td><td>BULK</td><td>DBL_BUF</td></tr><tr><td>01</td><td>CONTROL</td><td>STATUS_OUT</td></tr></table>


表 24-4. 发送状态编码


<table><tr><td>TX_STA[1:0]</td><td>含义</td></tr><tr><td>00</td><td>DISABLED:忽略端点的所有发送请求</td></tr><tr><td>01</td><td>STALL:握手包状态为 STALL</td></tr><tr><td>10</td><td>NAK:握手包状态为 NAK</td></tr></table>

11 VALID:使能端点的发送

## 24.7.7. USBD 端点 x 发送缓冲地址寄存器 (USBD_EPxTBADDR), $\mathbf { x } { = } [ 0 \ldots 7 ]$

地址偏移：[USBD_BADDR] + x * 16

USB本地地址： $[ \mathsf { U S B D \_ B A D D R } ] + \mathsf { x } ^ { \star } \otimes$ 

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">EPTXBAR[15:1]</td><td>EPTXBAR[0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:1</td><td>EPTXBAR[15:1]</td><td>发送缓冲地址在收到下一个IN分组时,需要发送的数据所在的缓冲区起始地址</td></tr><tr><td>0</td><td>EPTXBAR[0]</td><td>必须设为0</td></tr></table>

## 24.7.8. USBD 端点 x 发送缓冲区字节数目寄存器 (USBD_EPxTBCNT) $\mathbf { x } { = } [ 0 \ldots 7 ]$

地址偏移：[USBD_BADDR] + x * 16 + 4

USB本地地址： $[ \mathsf { U S B D \_ B A D D R } ] + \mathsf { x } ^ { \star } \thinspace 8 + 2$ 

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="6">保留</td><td colspan="10">EPTXCNT[9:0]</td></tr></table>

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:10</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>9:0</td><td>EPTXCNT[9:0]</td><td>发送字节数在收到下一个IN令牌后,将发送的字节数</td></tr></table>

## 24.7.9. USBD 端点 x 接收缓冲器地址寄存器 (USBD_EPxRBADDR) $\mathbf { x } { = } [ 0 \ldots 7 ]$

地址偏移：[USBD_BADDR] + x * 16 + 8

USB本地地址：[USBD $\mathsf { B A D D R } ] + \mathsf { x } ^ { \star } \mathsf { 8 } + 4$ 

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="15">EPRBAR[15:1]</td><td>EPRBAR[0]</td></tr></table>

rw 

rw 

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:1</td><td>EPRBAR[15:1]</td><td>接收缓冲器地址收到下一个OUT或者SETUP分组时,用于保存数据的缓冲区起始地址。</td></tr><tr><td>0</td><td>EPRBAR[0]</td><td>必须设为0</td></tr></table>

# 24.7.10. USBD 端点 x 接收缓冲区字节数目寄存器 n (USBD_EPxRBCNT) x=[0…7]

地址偏移：[USBD_BADDR] + x * 16 + 12

USB本地地址：[USBD_BADDR] + x * 8 + 6

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>BLKSIZ</td><td colspan="5">BLKNUM[4:0]</td><td colspan="10">EPRCNT[9:0]</td></tr><tr><td>rw</td><td colspan="5">rw</td><td colspan="10">r</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15</td><td>BLKSIZ</td><td>块的大小0: 块大小是2字节1: 块大小是32字节</td></tr><tr><td>14:10</td><td>BLKNUM[4:0]</td><td>块数目包缓冲区所分配的块的数目</td></tr><tr><td>9:0</td><td>EPRCNT[9:0]</td><td>接收字节数在收到下一个OUT/SETUP令牌后,接收到数据的字节数</td></tr></table>

## 24.7.11. USBD LPM 控制和状态寄存器 (USBD_LPMCS)

地址偏移：0x54

复位值：0x0000

该寄存器可半字（16 位）或全字（32 位）访问

<table><tr><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">保留</td><td colspan="4">BLSTAT[3:0]</td><td>REMWK</td><td>保留</td><td>LPMACK</td><td>LPMEN</td></tr><tr><td colspan="8"></td><td colspan="4">r</td><td colspan="2">r</td><td>rw</td><td>rw</td></tr></table>

<table><tr><td>位/位域</td><td>名称</td><td>描述</td></tr><tr><td>15:8</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>7:4</td><td>BLSTAT[3:0]</td><td>bLinkState值</td></tr><tr><td></td><td></td><td>此位域包含最后一个LPM令牌包被确认后产生的bLinkState值</td></tr><tr><td>3</td><td>REMWK</td><td>bRemoteWake值此位域包含最后一个LPM令牌包被确认后产生的bRemoteWake值</td></tr><tr><td>2</td><td>保留</td><td>必须保持复位值。</td></tr><tr><td>1</td><td>LPMACK</td><td>LPM令牌包响应使能0:有效的LPM令牌包将响应NYET1:有效的LPM令牌包将响应ACKNYET/ACK仅仅在LPM事务成功后才被返回:EXT令牌与LPM令牌都没有错误(否则错误)等于0001B(L1)的有效bLinkState被接收(否则STALL)</td></tr><tr><td>0</td><td>LPMEN</td><td>LPM支持使能软件设置此位来使能USB设备的LPM支持。如果此位为0,将不会有LPM事务被处理</td></tr></table>
