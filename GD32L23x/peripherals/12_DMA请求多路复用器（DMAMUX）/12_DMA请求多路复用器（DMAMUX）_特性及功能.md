## 12. DMA 请求多路复用器（DMAMUX）

## 12.1. 简介

DMAMUX是 DMA 请求的传输调度器。可编程的 DMA请求多路复用器 DMAMUX，可在外设和 DMA 控制器之间路由 DMA 请求线路，或者 DMAMUX 也可以将可编程事件连入到输入触发信号上，作为一个 DMAMUX 请求发生器，再由 DMAMUX请求路由器在 DMAMUX 请求生成器产生的 DMA 请求和 DMA控制器之间路由 DMA 请求线路。每个 DMAMUX 请求路由通道选择一条唯一的 DMA 请求线路，无条件地或同步地从它的 DMAMUX 同步输入事件。DMA请求信号会一直挂起，直到 DMA控制器响应它，并且产生一个 DMA确认信号，此时相应的 DMA请求信号被释放。

## 12.2. 主要特征

◼ 7 个可配置的 DMAMUX 请求路由输出通道。

◼ 4 个 DMAMUX 请求生成通道。

◼ 21 路触发输入信号到 DMAMUX请求生成器。

◼ 21 路同步输入信号。

◼ 每个 DMAMUX 请求生成通道包含一个 DMAMUX 请求触发输入选择器，一个 DMAMUX请求生成计数器，和一个指示被选中的 DMAMUX请求触发输入信号的事件溢出标志。

◼ 每个 DMAMUX 请求路由输出通道包含 60 路外设 DMAMUX 请求输入信号，一个同步输入信号选择器，一条 DMA 请求路由输出线路，一个路由事件输出信号用于 DMA 请求级联，一个 DMAMUX 请求路由计数器，和一个指示被选中的同步输入信号的事件溢出标志。

## 12.3. 结构框图


图 12-1. DMAMUX 结构框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/b6ca16980f191415f9780a1659e64a60ea2a7b1cd87852bc23a88fb5dc28b39f.jpg)


## 12.4. 信号描述

DMAMUX 信号描述如下所示：

◼ Reqx_in：DMAMUX 请求路由输入信号，来自外设的请求或者 DMAMUX 请求生成器生成的请求。

◼ Peri_reqx：从外设输入到 DMAMUX 的 DMA 请求线路。

◼ Gen_reqx：DMAMUX 请求生成器生成输出的 DMA 请求信号。

◼ Reqx_out：DMAMUX 请求输出信号到 DMA 控制器。

◼ Trgx_in：DMAMUX 请求触发输入信号到 DMAMUX 请求生成器。

◼ Syncx_in：DMAMUX 同步输入信号到 DMAMUX 请求路由器。

◼ Evtx_out：DMAMUX 请求路由计数器下溢事件输出信号。

## 12.5. 功能说明

如 12-1. DMAMUX 所示，DMAMUX 包含两个子模块：

◼ DMAMUX 请求路由器

DMAMUX 请求路由器输入（Reqx_in）来自两部分：

一部分来自外设请求（Peri_reqx）；

– 另一部分来自 DMAMUX 请求生成器（Gen_reqx）。

DMAMUX 请求路由输出到 DMA 控制器对应的通道（Reqx_out）。

同步输入（Syncx_in）来自内部或外部信号。

◼ DMAMUX 请求生成器

DMAMUX 请求触发输入（Trgx_in）来自内部或外部信号。

## 12.5.1. DMAMUX 请求路由器

DMAMUX 请求路由器可在外设/ DMAMUX 请求生成器，与 DMA 控制器之间路由 DMA 请求线路。DMAMUX 请求路由器由 DMAMUX 请求路由通道组成。DMA请求输入信号并联至所有的 DMAMUX 请求路由通道。每个 DMAMUX 请求路由通道都有一个同步单元。同步输入信号并联至所有 DMAMUX 请求路由通道的同步单元。每个 DMAMUX 请求路由通道都有一个内部的 DMAMUX 请求路由计数器。

## DMAMUX 请求路由通道

DMAMUX 请求路由通道 x 的请求路由输入由 DMAMUX_RM_CHxCFG 寄存器的 MUXID[5:0]/ MUXID[6:0]位域来配置，请求路由输入可选为外设 DMA 请求，或者 DMAMUX 请求生成器产生的 DMA 请求，参考 12-2. DMAMUX 。一个 DMAMUX 请求路由通道与对应的 DMA 控制器通道相连接。

注意： 当 MUXID[5:0] / MUXID[6:0]值为 0 时，没有 DMA 请求线路被映射到 DMAMUX 请求路由通道上。DMAMUX 不允许将同一个 DMA 请求线路（相同 MUXID[5:0] / MUXID[6:0]且非空）映射到两个不同的 DMAMUX 请求路由通道上。

## 当同步模式禁能时

每当连到 DMAMUX 的 DMA 请求被 DMA 控制器服务，这个 DMA 请求将取消挂起，内部的DMAMUX 请 求路 由 计 数 器 将 减 1。 当 DMAMUX 请 求路 由 计 数 器发 生下 溢时，DMAMUX_RM_CHxCFG 寄存器的 NBR[4:0]值将自动重装载到计数器中。如果将 EVGEN 位置位，使能通道事件输出，则通道事件输出前，DMA 请求数量为 NBR[4:0] + 1。

注意：只有当 DMAMUX 请求路由通道 x 的同步使能位 SYNCEN 位和通道事件输出使能位EVGEN 位都为 0 时，才能配置其 NBR[4:0]位域。

## 当同步模式使能时

如果 请求路由通道 工作在同步模式下，当检测到选择的同步输入信号的上升沿或者下降沿时，挂起的DMA请求将被连到DMAMUX请求路由通道x的输出。每当连到DMAMUX的 DMA 请求被 DMA控制器服务，这个 DMA 请求将取消挂起，内部的 DMAMUX 请求路由计数器将减 1。当 DMAMUX 请求路由计数器发生下溢时，DMA 请求线路将断开与 DMAMUX 请求路由通道 x 的输出的连接，并且 DMAMUX_RM_CHxCFG 寄存器的 NBR[4:0]值将自动重装载到计数器中。一个同步事件可传输 NBR[4:0] + 1 个 DMA请求到 DMAMUX 请求路由通道 x的输出上。

12-2. 为当 NBR[4:0] = 4，SYNCEN = 1，EVGEN = 1，SYNCP[1:0] = 0b01 时的举例。


图 12-2. 同步模式


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/3c83dd86e93f86a27bbe7c41bcd74289e5368a772be176caae3079fba51992c7.jpg)


置位 DMAMUX_RM_CHxCFG 寄存器的 SYNCEN 位可使能 DMAMUX 请求路由通道 x 的同步模式。同步输入信号可由 DMAMUX_RM_CHxCFG 寄存器的 SYNCID[4:0]位域来配置，参考 12-5. 。同步输入信号的有效边沿由 DMAMUX_RM_CHxCFG 寄存器的 SYNCP[1:0]位域来配置。

注意：如果同步输入事件发生时，DMAMUX 输入上没有挂起的 DMA 请求，则这个同步输入事件将被忽略，之后如有 DMA 请求被挂起，它将不会被连接到 DMAMUX 请求路由通道 x 的输出，直到发生下一个同步输入事件。

## 通道事件输出

每个 DMAMUX 请求路由通道都有一个通道事件输出信号 Evtx_out，用于 DMAMUX 请求路由计数器的下溢事件输出。Evt0_out ~ Evt3_out 信号可用于 DMA 请求级联。如果通过置位DMAMUX_RM_CHxCFG 寄存器的 EVGEN 位来使能 DMAMUX 请求路由通道 x 的通道事件输出，当 DMAMUX 请求路由计数器自动重装载为 NBR[4:0]值时，发生一个通道事件，输出为一个 AHB时钟周期脉冲。

12-3. 为当 NBR[4:0] = 4，SYNCEN = 0，EVGEN = 1 时的举例。


图 12-3. 通道事件输出


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-24/f61111d3-dcf6-4d0c-9dce-d464c3886439/c4b108e00009d211c6d8c9030c240973797a782650badd11e105037662570a5f.jpg)



注意：如果 EVGEN = 1 且 NBR[4:0] = 0，则每次 DMA 请求被服务时都会输出一个通道事件。


## 同步溢出

如果在 DMAMUX 请求路由计数器下溢之前又发生了新的同步事件，则 DMAMUX_RM_INTF寄存器的同步溢出标志位 SOIFx 位将置位。

注意：建议在 DMA 控制器对应通道请求被取消时，配置 DMAMUX_RM_CHxCFG 寄存器的SYNCEN 位为 0 来禁能 DMAMUX 请求路由通道 x 的同步模式。否则，当又发生一个新的同步事件时，由于接收不到 DMA的响应信号将会发生同步溢出事件。

## 12.5.2. DMAMUX 请求生成器

DMAMUX 请求生成器在触发输入事件发生时会产生 DMA 请求。DMAMUX 请求生成器由DMAMUX 请求生成通道组成。DMA 请求触发输入信号并联至所有 DMAMUX 请求生成通道。每个 DMAMUX 请求生成通道都有一个内部的 DMAMUX 请求生成计数器。

触发输入信号的有效边沿由 DMAMUX_RG_CHxCFG 寄存器的 RGTP[1:0]位域来配置。DMAMUX 请求生成通道 x 的触发输入信号由 DMAMUX_RG_CHxCFG 寄存器的 TID[4:0]位域来配置，参考 12-4. 。置位 DMAMUX_RG_CHxCFG 寄存器的 RGEN位来使能 DMAMUX 请求生成通道 x。

## DMAMUX 请求生成通道

当发生触发输入事件时，对应的 DMAMUX 请求生成通道 x 开始产生 DMA 请求到通道的输出上，通道输出连到 DMAMUX 请求路由器的输入上。每当 DMAMUX 生成的 DMA 请求被 DMA控制器服务，这个 DMA 请求将取消挂起，内部的 DMAMUX 请求生成计数器将减 1。当DMAMUX 请求生成计数器发生下溢时，DMAMUX请求生成通道将停止产生 DMA 请求，在下一 个 触 发 输 入 事 件 发 生 时 ， DMAMUX 请 求 生 成 计 数 器 将 自 动 重 装 载 为DMAMUX_RG_CHxCFG 寄存器的 NBRG[4:0]位域值。

注意：触发输入事件后产生的 DMA请求数量为 NBRG[4:0] + 1。只有当 DMAMUX 请求生成通道 x 的 RGEN 位为 0 时才可以配置 NBRG[4:0]位域。

## 触发溢出

如果 RGEN 位为 1，DMAMUX 请求生成通道 x 被使能，当一个新的触发输入信号发生了，而此时 DMAMUX 请求生成计数器还未发生下溢，则 DMAMUX_RG_INTF 寄存器的 TOIFx 位将硬件置位以指示发生了触发溢出事件。

注意：建议在 DMA 控制器对应通道请求被取消时，配置 DMAMUX_RG_CHxCFG 寄存器的RGEN 位为 0 来禁能 DMAMUX 请求生成通道 x。否则，当又发生一个新的触发输入事件时，由于接收不到 DMA的响应信号将会发生触发溢出事件。

## 12.5.3. 通道配置

根据以下步骤来配置 DMAMUX的通道 y 和对应的 DMA通道 x：

1. 完整配置 DMA 通道 x 相关参数，除了 DMA通道 x 的使能。

2. 完整配置 DMAMUX 通道 y 相关参数。

3. 设置 DMA_CHxCTL 寄存器的 CHEN 位 1 来使能 DMA 通道 x。

## 12.5.4. 中断

DMAMUX模块有两种类型的中断事件，包括DMAMUX请求路由通道的同步溢出事件，和DMAMUX请求生成通道的触发溢出事件。

每个中断事件都有一个专用的标志位，专用的清除位和专用的使能位。 12-1. 描述了其对应关系。


表 12-1. 中断事件


<table><tr><td>中断事件</td><td>标志位</td><td>清除位</td><td>使能位</td></tr><tr><td>DMAMUX 请求路由通道 x 上的同步溢出事件</td><td>DMAMUX_RM_INTF 寄存器的 SOIFx位</td><td>DMAMUX_RM_INTC 寄存器的 SOIFCx位</td><td>DMAMUX_RM_CHxCFG 寄存器的SOIE 位</td></tr><tr><td>DMAMUX 请求生成通道 y 上的触发溢出事件</td><td>DMAMUX_RG_INTF 寄存器的 TOIFy位</td><td>DMAMUX_RG_INTC 寄存器的 TOIFCy位</td><td>DMAMUX_RG_CHxCFG 寄存器的TOIE 位</td></tr></table>

## 触发溢出中断

当 DMAMUX 请求生成触发溢出标志位 TOIFx 置位，并且触发溢出中断使能位 TOIE 位置位，则会产生一个触发溢出中断。写 1 到 DMAMUX_RG_INTC 寄存器的对应触发溢出清除位TOIFCx 将会清除触发溢出标志位 TOIFx。

## 同步溢出中断

当 DMAMUX 请求路由同步溢出标志位 SOIFx 置位，并且触发同步溢出中断使能位 SOIE 位置位，则会产生一个同步溢出中断。写 1 到 DMAMUX_RM_INTC 寄存器的对应同步溢出清除位 SOIFCx 将会清除同步溢出标志位 SOIFx。

## 12.5.5. DMAMUX 映射

## DMAMUX请求路由输入映射

DMAMUX 请求路由输入可来自于外设或者 DMAMUX 请求生成器，参考和 12-3. DMAMUXGD32L235xx ，由 DMAMUX_RM_CHxCFG 寄存器的 MUXID[5:0]/ MUXID[6:0]位域配置 DMAMUX 请求路由通道 x 的输入。


表 12-2. DMAMUX 请求路由输入信号映射（GD32L233xx）


<table><tr><td>请求路由通道输入标识MUXID[5:0]</td><td>来源</td></tr><tr><td>1</td><td>Gen_req0</td></tr><tr><td>2</td><td>Gen_req1</td></tr><tr><td>3</td><td>Gen_req2</td></tr><tr><td>4</td><td>Gen_req3</td></tr><tr><td>5</td><td>ADC</td></tr><tr><td>6</td><td>DAC</td></tr><tr><td>7</td><td>保留</td></tr><tr><td>8</td><td>保留</td></tr><tr><td>9</td><td>保留</td></tr><tr><td>10</td><td>I2C0_RX</td></tr><tr><td>11</td><td>I2C0_TX</td></tr><tr><td>12</td><td>I2C1_RX</td></tr><tr><td>13</td><td>I2C1_TX</td></tr><tr><td>14</td><td>I2C2_RX</td></tr><tr><td>15</td><td>I2C2_TX</td></tr><tr><td>16</td><td>SPI0_RX</td></tr><tr><td>17</td><td>SPI0_TX</td></tr><tr><td>18</td><td>SPI1_RX</td></tr><tr><td>19</td><td>SPI1_TX</td></tr><tr><td>20</td><td>保留</td></tr><tr><td>21</td><td>保留</td></tr><tr><td>22</td><td>保留</td></tr><tr><td>23</td><td>保留</td></tr><tr><td>24</td><td>保留</td></tr><tr><td>25</td><td>TIMER1_CH0</td></tr><tr><td>26</td><td>TIMER1_CH1</td></tr><tr><td>27</td><td>TIMER1_CH2</td></tr><tr><td>28</td><td>TIMER1_CH3</td></tr><tr><td>29</td><td>保留</td></tr><tr><td>30</td><td>TIMER1_UP</td></tr><tr><td>31</td><td>保留</td></tr><tr><td>32</td><td>TIMER2_CH0</td></tr><tr><td>33</td><td>TIMER2_CH1</td></tr><tr><td>34</td><td>TIMER2_CH2</td></tr><tr><td>35</td><td>TIMER2_CH3</td></tr><tr><td>36</td><td>TIMER2_TRIG</td></tr><tr><td>37</td><td>TIMER2_UP</td></tr><tr><td>38</td><td>保留</td></tr><tr><td>39</td><td>保留</td></tr><tr><td>40</td><td>保留</td></tr><tr><td>41</td><td>保留</td></tr><tr><td>42</td><td>TIMER5_UP</td></tr><tr><td>43</td><td>TIMER6_UP</td></tr><tr><td>44</td><td>CAU_IN</td></tr><tr><td>45</td><td>CAU_OUT</td></tr><tr><td>46</td><td>保留</td></tr><tr><td>47</td><td>保留</td></tr><tr><td>48</td><td>保留</td></tr><tr><td>49</td><td>保留</td></tr><tr><td>50</td><td>USART0_RX</td></tr><tr><td>51</td><td>USART0_TX</td></tr><tr><td>52</td><td>USART1_RX</td></tr><tr><td>53</td><td>USART1_TX</td></tr><tr><td>54</td><td>UART3_RX</td></tr><tr><td>55</td><td>UART3_TX</td></tr><tr><td>56</td><td>UART4_RX</td></tr><tr><td>57</td><td>UART4_TX</td></tr><tr><td>58</td><td>LPUART_RX</td></tr><tr><td>59</td><td>LPUART_TX</td></tr><tr><td>60</td><td>保留</td></tr><tr><td>61</td><td>保留</td></tr><tr><td>62</td><td>保留</td></tr><tr><td>63</td><td>保留</td></tr></table>


表 12-3. DMAMUX 请求路由输入信号映射（GD32L235xx）


<table><tr><td>请求路由通道输入标识MUXID[6:0]</td><td>Source</td></tr><tr><td>1</td><td>Gen_reqx0</td></tr><tr><td>2</td><td>Gen_reqx1</td></tr><tr><td>3</td><td>Gen_reqx2</td></tr><tr><td>4</td><td>Gen_reqx3</td></tr><tr><td>5</td><td>ADC</td></tr><tr><td>6</td><td>DAC_CH0</td></tr><tr><td>7</td><td>保留</td></tr><tr><td>8</td><td>保留</td></tr><tr><td>9</td><td>保留</td></tr><tr><td>10</td><td>I2C0_RX</td></tr><tr><td>11</td><td>I2C0_TX</td></tr><tr><td>12</td><td>I2C1_RX</td></tr><tr><td>13</td><td>I2C1_TX</td></tr><tr><td>14</td><td>I2C2_RX</td></tr><tr><td>15</td><td>I2C2_TX</td></tr><tr><td>16</td><td>SPI0_RX</td></tr><tr><td>17</td><td>SPI0_TX</td></tr><tr><td>18</td><td>SPI1_RX</td></tr><tr><td>19</td><td>SPI1_TX</td></tr><tr><td>20</td><td>保留</td></tr><tr><td>21</td><td>保留</td></tr><tr><td>22</td><td>保留</td></tr><tr><td>23</td><td>保留</td></tr><tr><td>24</td><td>保留</td></tr><tr><td>25</td><td>TIMER1_CH0</td></tr><tr><td>26</td><td>TIMER1_CH1</td></tr><tr><td>27</td><td>TIMER1_CH2</td></tr><tr><td>28</td><td>TIMER1_CH3</td></tr><tr><td>29</td><td>TIMER1_TRIG</td></tr><tr><td>30</td><td>TIMER1_UP</td></tr><tr><td>31</td><td>保留</td></tr><tr><td>32</td><td>TIMER2_CH0</td></tr><tr><td>33</td><td>TIMER2_CH1</td></tr><tr><td>34</td><td>TIMER2_CH2</td></tr><tr><td>35</td><td>TIMER2_CH3</td></tr><tr><td>36</td><td>TIMER2_TRIG</td></tr><tr><td>37</td><td>TIMER2_UP</td></tr><tr><td>38</td><td>保留</td></tr><tr><td>39</td><td>保留</td></tr><tr><td>40</td><td>保留</td></tr><tr><td>41</td><td>保留</td></tr><tr><td>42</td><td>TIMER5_UP</td></tr><tr><td>43</td><td>TIMER6_UP</td></tr><tr><td>44</td><td>CAU_IN</td></tr><tr><td>45</td><td>CAU_OUT</td></tr><tr><td>46</td><td>保留</td></tr><tr><td>47</td><td>保留</td></tr><tr><td>48</td><td>保留</td></tr><tr><td>49</td><td>保留</td></tr><tr><td>50</td><td>USART0_RX</td></tr><tr><td>51</td><td>USART0_TX</td></tr><tr><td>52</td><td>USART1_RX</td></tr><tr><td>53</td><td>USART1_TX</td></tr><tr><td>54</td><td>UART3_RX</td></tr><tr><td>55</td><td>UART3_TX</td></tr><tr><td>56</td><td>UART4_RX</td></tr><tr><td>57</td><td>UART4_TX</td></tr><tr><td>58</td><td>LPUART0_RX</td></tr><tr><td>59</td><td>LPUART0_TX</td></tr><tr><td>60</td><td>LPUART1_RX</td></tr><tr><td>61</td><td>LPUART1_TX</td></tr><tr><td>62</td><td>保留</td></tr><tr><td>63</td><td>保留</td></tr><tr><td>64</td><td>TIMER0_CH0</td></tr><tr><td>65</td><td>TIMER0_CH1</td></tr><tr><td>66</td><td>TIMER0_CH2</td></tr><tr><td>67</td><td>TIMER0_CH3</td></tr><tr><td>68</td><td>TIMER0_TRIG</td></tr><tr><td>69</td><td>TIMER0_UP</td></tr><tr><td>70</td><td>TIMER0_COM</td></tr><tr><td>71</td><td>TIMER14_CH0</td></tr><tr><td>72</td><td>TIMER14_CH1</td></tr><tr><td>73</td><td>TIMER14_TRIG</td></tr><tr><td>74</td><td>TIMER14_UP</td></tr><tr><td>75</td><td>TIMER14_COM</td></tr><tr><td>76</td><td>TIMER40_CH0</td></tr><tr><td>77</td><td>TIMER40_CH1</td></tr><tr><td>78</td><td>TIMER40_TRIG</td></tr><tr><td>79</td><td>TIMER40_UP</td></tr><tr><td>80</td><td>TIMER40_COM</td></tr></table>

## 触发输入映射

DMAMUX 请求生成通道 x 的触发输入可由 DMAMUX_RG_CHxCFG 寄存器的 TID[4:0]位域来配置，参考 12-4. 。


表 12-4. 触发输入信号映射


<table><tr><td>触发输入标识TID[4:0]</td><td>来源</td></tr><tr><td>0</td><td>EXTI_0</td></tr><tr><td>1</td><td>EXTI_1</td></tr><tr><td>2</td><td>EXTI_2</td></tr><tr><td>3</td><td>EXTI_3</td></tr><tr><td>4</td><td>EXTI_4</td></tr><tr><td>5</td><td>EXTI_5</td></tr><tr><td>6</td><td>EXTI_6</td></tr><tr><td>7</td><td>EXTI_7</td></tr><tr><td>8</td><td>EXTI_8</td></tr><tr><td>9</td><td>EXTI_9</td></tr><tr><td>10</td><td>EXTI_10</td></tr><tr><td>11</td><td>EXTI_11</td></tr><tr><td>12</td><td>EXTI_12</td></tr><tr><td>13</td><td>EXTI_13</td></tr><tr><td>14</td><td>EXTI_14</td></tr><tr><td>15</td><td>EXTI_15</td></tr><tr><td>16</td><td>Evt0_out</td></tr><tr><td>17</td><td>Evt1_out</td></tr><tr><td>18</td><td>Evt2_out</td></tr><tr><td>19</td><td>Evt3_out</td></tr><tr><td>20</td><td>保留</td></tr><tr><td>21</td><td>保留</td></tr><tr><td>22</td><td>TIMER11_CH0_O</td></tr><tr><td>23</td><td>保留</td></tr></table>

## 同步输入映射

同步输入由 DMAMUX_RM_CHxCFG 寄存器的 SYNCID[4:0]位域来配置，参考 12-5.输入信号映射


表 12-5. 同步输入信号映射


<table><tr><td>同步输入标识SYNCID[4:0]</td><td>来源</td></tr><tr><td>0</td><td>EXTI_0</td></tr><tr><td>1</td><td>EXTI_1</td></tr><tr><td>2</td><td>EXTI_2</td></tr><tr><td>3</td><td>EXTI_3</td></tr><tr><td>4</td><td>EXTI_4</td></tr><tr><td>5</td><td>EXTI_5</td></tr><tr><td>6</td><td>EXTI_6</td></tr><tr><td>7</td><td>EXTI_7</td></tr><tr><td>8</td><td>EXTI_8</td></tr><tr><td>9</td><td>EXTI_9</td></tr><tr><td>10</td><td>EXTI_10</td></tr><tr><td>11</td><td>EXTI_11</td></tr><tr><td>12</td><td>EXTI_12</td></tr><tr><td>13</td><td>EXTI_13</td></tr><tr><td>14</td><td>EXTI_14</td></tr><tr><td>15</td><td>EXTI_15</td></tr><tr><td>16</td><td>Evt0_out</td></tr><tr><td>17</td><td>Evt1_out</td></tr><tr><td>18</td><td>Evt2_out</td></tr><tr><td>19</td><td>Evt3_out</td></tr><tr><td>20</td><td>保留</td></tr><tr><td>21</td><td>保留</td></tr><tr><td>22</td><td>TIMER11_CH0_O</td></tr><tr><td>23</td><td>保留</td></tr></table>
