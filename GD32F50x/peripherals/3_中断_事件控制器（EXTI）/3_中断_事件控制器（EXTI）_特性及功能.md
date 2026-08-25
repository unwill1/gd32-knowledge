## 3. 中断/事件控制器（EXTI）

## 3.1. 简介

Cortex<sup>®</sup>-M33 集成了嵌套式矢量型中断控制器（Nested Vectored Interrupt Controller（NVIC））来实现高效的异常和中断处理。NVIC 实现了低延迟的异常和中断处理，以及电源管理控制。它和内核是紧密耦合的。更多关于 NVIC 的说明请参考《Cortex®--M33 技术参考手册》。

EXTI（中断/事件控制器）包括 20 个相互独立的边沿检测电路并且能够向处理器内核产生中断请求或唤醒事件。EXTI 有三种触发类型：上升沿触发、下降沿触发和任意沿触发。EXTI 中的每一个边沿检测电路都可以独立配置和屏蔽。

## 3.2. 主要特征

 Cortex<sup>®</sup>--M33 系统异常；

 多达 79 种可屏蔽的外设中断；

 4 位中断优先级配置位—16 个中断优先等级；

 高效的中断处理；

 支持异常抢占和咬尾中断；

 将系统从省电模式唤醒；

 EXTI 中有多达 20 个相互独立的边沿检测电路；

 3 种触发类型：上升沿触发，下降沿触发和任意沿触发；

 软件中断或事件触发；

 可配置的触发源。

## 3.3. 功能说明

Arm Cortex®-M33 处理器和嵌套式矢量型中断控制器（NVIC）在处理（Handler）模式下对所有异常进行优先级区分以及处理。当异常发生时，系统自动将当前处理器工作状态压栈，在执行完中断服务子程序（ISR）后自动将其出栈。

取向量是和当前工作态压栈并行进行的，从而提高了中断入口效率。处理器支持咬尾中断，可实现背靠背中断，大大削减了反复切换工作态所带来的开销。 3-1. Cortex®-M33 NVIC和 3-2. 列出了 Cotrex<sup>®</sup>-M33 中的 NVIC 异常类型。


表 3-1. Cortex<sup>®</sup>-M33 中的 NVIC 异常类型


<table><tr><td>异常类型</td><td>向量编号</td><td>优先级(a)</td><td>向量地址</td><td>描述</td></tr><tr><td>-复位</td><td>01</td><td>--3</td><td>0x0000_00000x0000_0004</td><td>保留复位</td></tr><tr><td>NMI</td><td>2</td><td>-2</td><td>0x0000_0008</td><td>不可屏蔽中断</td></tr><tr><td>硬件故障</td><td>3</td><td>-1</td><td>0x0000_000C</td><td>各种硬件级别的故障</td></tr><tr><td>存储器管理</td><td>4</td><td>可编程设置</td><td>0x0000_0010</td><td>存储器管理</td></tr><tr><td>总线故障</td><td>5</td><td>可编程设置</td><td>0x0000_0014</td><td>预取指故障,存储器访问故障</td></tr><tr><td>用法故障</td><td>6</td><td>可编程设置</td><td>0x0000_0018</td><td>未定义的指令或非法状态</td></tr><tr><td>-</td><td>7-10</td><td>-</td><td>0x0000_001C - 0x0000_002B</td><td>保留</td></tr><tr><td>SVCall 服务调用</td><td>11</td><td>可编程设置</td><td>0x0000_002C</td><td>通过 SWI 指令实现系统服务调用</td></tr><tr><td>调试监控</td><td>12</td><td>可编程设置</td><td>0x0000_0030</td><td>调试监视器</td></tr><tr><td>-</td><td>13</td><td>-</td><td>0x0000_0034</td><td>保留</td></tr><tr><td>PendSV 挂起服务</td><td>14</td><td>可编程设置</td><td>0x0000_0038</td><td>可挂起的系统服务请求</td></tr><tr><td>SysTick</td><td>15</td><td>可编程设置</td><td>0x0000_003C</td><td>系统节拍定时器</td></tr></table>


表 3-2. 中断向量表


<table><tr><td>中断编号</td><td>向量编号</td><td>外设中断描述</td><td>向量地址</td></tr><tr><td>IRQ 0</td><td>16</td><td>窗口看门狗中断</td><td>0x0000_0040</td></tr><tr><td>IRQ 1</td><td>17</td><td>连接到EXTI线的LVD/VAVD中断</td><td>0x0000_0044</td></tr><tr><td>IRQ 2</td><td>18</td><td>侵入检测中断</td><td>0x0000_0048</td></tr><tr><td>IRQ 3</td><td>19</td><td>RTC全局中断</td><td>0x0000_004C</td></tr><tr><td>IRQ 4</td><td>20</td><td>FMC全局中断</td><td>0x0000_0050</td></tr><tr><td>IRQ 5</td><td>21</td><td>RCU和CTC中断</td><td>0x0000_0054</td></tr><tr><td>IRQ 6</td><td>22</td><td>EXTI线0中断</td><td>0x0000_0058</td></tr><tr><td>IRQ 7</td><td>23</td><td>EXTI线1中断</td><td>0x0000_005C</td></tr><tr><td>IRQ 8</td><td>24</td><td>EXTI线2中断</td><td>0x0000_0060</td></tr><tr><td>IRQ 9</td><td>25</td><td>EXTI线3中断</td><td>0x0000_0064</td></tr><tr><td>IRQ 10</td><td>26</td><td>EXTI线4中断</td><td>0x0000_0068</td></tr><tr><td>IRQ 11</td><td>27</td><td>DMA0通道0全局中断</td><td>0x0000_006C</td></tr><tr><td>IRQ 12</td><td>28</td><td>DMA0通道1全局中断</td><td>0x0000_0070</td></tr><tr><td>IRQ 13</td><td>29</td><td>DMA0通道2全局中断</td><td>0x0000_0074</td></tr><tr><td>IRQ 14</td><td>30</td><td>DMA0通道3全局中断</td><td>0x0000_0078</td></tr><tr><td>IRQ 15</td><td>31</td><td>DMA0通道4全局中断</td><td>0x0000_007C</td></tr><tr><td>IRQ 16</td><td>32</td><td>DMA0通道5全局中断</td><td>0x0000_0080</td></tr><tr><td>IRQ 17</td><td>33</td><td>DMA0通道6全局中断</td><td>0x0000_0084</td></tr><tr><td>IRQ 18</td><td>34</td><td>ADC0和ADC1全局中断</td><td>0x0000_0088</td></tr><tr><td>IRQ 19</td><td>35</td><td>CAN0 发送中断</td><td>0x0000_008C</td></tr><tr><td>IRQ 20</td><td>36</td><td>CAN0 接收 0 中断</td><td>0x0000_0090</td></tr><tr><td>IRQ 21</td><td>37</td><td>CAN0 接收 1 中断</td><td>0x0000_0094</td></tr><tr><td>IRQ 22</td><td>38</td><td>CAN0 EWMC 中断</td><td>0x0000_0098</td></tr><tr><td>IRQ 23</td><td>39</td><td>EXTI 线[9:5]中断</td><td>0x0000_009C</td></tr><tr><td>IRQ 24</td><td>40</td><td>TIMER0 中止中断</td><td>0x0000_00A0</td></tr><tr><td>IRQ 25</td><td>41</td><td>TIMER0 更新中断</td><td>0x0000_00A4</td></tr><tr><td>IRQ 26</td><td>42</td><td>TIMER0 触发与通道换相中断</td><td>0x0000_00A8</td></tr><tr><td>IRQ 27</td><td>43</td><td>TIMER0 通道捕获比较中断</td><td>0x0000_00AC</td></tr><tr><td>IRQ 28</td><td>44</td><td>TIMER1 全局中断</td><td>0x0000_00B0</td></tr><tr><td>IRQ 29</td><td>45</td><td>TIMER2 全局中断</td><td>0x0000_00B4</td></tr><tr><td>IRQ 30</td><td>46</td><td>TIMER3 全局中断</td><td>0x0000_00B8</td></tr><tr><td>IRQ 31</td><td>47</td><td>I2C0 事件中断</td><td>0x0000_00BC</td></tr><tr><td>IRQ 32</td><td>48</td><td>I2C0 错误中断</td><td>0x0000_00C0</td></tr><tr><td>IRQ 33</td><td>49</td><td>I2C1 事件中断</td><td>0x0000_00C4</td></tr><tr><td>IRQ 34</td><td>50</td><td>I2C1 错误中断</td><td>0x0000_00C8</td></tr><tr><td>IRQ 35</td><td>51</td><td>SPI0 全局中断</td><td>0x0000_00CC</td></tr><tr><td>IRQ 36</td><td>52</td><td>SPI1 全局中断</td><td>0x0000_00D0</td></tr><tr><td>IRQ 37</td><td>53</td><td>USART0 全局中断</td><td>0x0000_00D4</td></tr><tr><td>IRQ 38</td><td>54</td><td>USART1 全局中断</td><td>0x0000_00D8</td></tr><tr><td>IRQ 39</td><td>55</td><td>USART2 全局中断</td><td>0x0000_00DC</td></tr><tr><td>IRQ 40</td><td>56</td><td>EXTI 线[15:10]中断</td><td>0x0000_00E0</td></tr><tr><td>IRQ 41</td><td>57</td><td>连接 EXTI 线的 RTC 闹钟中断</td><td>0x0000_00E4</td></tr><tr><td>IRQ 42</td><td>58</td><td>连接 EXTI 线的 USBFS 唤醒中断</td><td>0x0000_00E8</td></tr><tr><td>IRQ 43</td><td>59</td><td>TIMER7 中止中断</td><td>0x0000_00EC</td></tr><tr><td>IRQ 44</td><td>60</td><td>TIMER7 更新中断</td><td>0x0000_00F0</td></tr><tr><td>IRQ 45</td><td>61</td><td>TIMER7 触发与通道换相中断</td><td>0x0000_00F4</td></tr><tr><td>IRQ 46</td><td>62</td><td>TIMER7 通道捕获比较中断</td><td>0x0000_00F8</td></tr><tr><td>IRQ 47</td><td>63</td><td>ADC2 全局中断</td><td>0x0000_00FC</td></tr><tr><td>IRQ 48</td><td>64</td><td>保留</td><td>0x0000_0100</td></tr><tr><td>IRQ 49</td><td>65</td><td>RCU 时钟频率监控中断</td><td>0x0000_0104</td></tr><tr><td>IRQ50</td><td>66</td><td>连接 EXTI 线的 CMP 中断</td><td>0x0000_0108</td></tr><tr><td>IRQ51</td><td>67</td><td>SPI2 全局中断</td><td>0x0000_010C</td></tr><tr><td>IRQ52</td><td>68</td><td>UART3 全局中断</td><td>0x0000_0110</td></tr><tr><td>IRQ53</td><td>69</td><td>UART4 全局中断</td><td>0x0000_0114</td></tr><tr><td>IRQ54</td><td>70</td><td>TIMER5 全局中断</td><td>0x0000_0118</td></tr><tr><td>IRQ55</td><td>71</td><td>TIMER6 全局中断</td><td>0x0000_011C</td></tr><tr><td>IRQ56</td><td>72</td><td>DMA1 通道0全局中断</td><td>0x0000_0120</td></tr><tr><td>IRQ57</td><td>73</td><td>DMA1 通道1全局中断</td><td>0x0000_0124</td></tr><tr><td>IRQ58</td><td>74</td><td>DMA1 通道2全局中断</td><td>0x0000_0128</td></tr><tr><td>IRQ59</td><td>75</td><td>DMA1 通道3全局中断</td><td>0x0000_012C</td></tr><tr><td>IRQ60</td><td>76</td><td>DMA1 通道4全局中断</td><td>0x0000_0130</td></tr><tr><td>IRQ61</td><td>77</td><td>DAC 全局中断</td><td>0x0000_0134</td></tr><tr><td>IRQ62</td><td>78</td><td>VUVD 或 VOVD 中断</td><td>0x0000_0138</td></tr><tr><td>IRQ63</td><td>79</td><td>CAN1 发送中断</td><td>0x0000_013C</td></tr><tr><td>IRQ64</td><td>80</td><td>CAN1 接收0中断</td><td>0x0000_0140</td></tr><tr><td>IRQ65</td><td>81</td><td>CAN1 接收1中断</td><td>0x0000_0144</td></tr><tr><td>IRQ66</td><td>82</td><td>CAN1EWMC 中断</td><td>0x0000_0148</td></tr><tr><td>IRQ67</td><td>83</td><td>SRAM ECC 中断</td><td>0x0000_014C</td></tr><tr><td>IRQ68</td><td>84</td><td>FPU 中断</td><td>0x0000_0150</td></tr><tr><td>IRQ69</td><td>85</td><td>CMP 中断</td><td>0x0000_0154</td></tr><tr><td>IRQ70</td><td>86</td><td>DMAMUX 中断</td><td>0x0000_0158</td></tr><tr><td>IRQ71</td><td>87</td><td>CAU 中断</td><td>0x0000_015C</td></tr><tr><td>IRQ72</td><td>88</td><td>HAU 中断</td><td>0x0000_0160</td></tr><tr><td>IRQ73</td><td>89</td><td>TRNG 中断</td><td>0x0000_0164</td></tr><tr><td>IRQ74</td><td>90</td><td>USBFS 中断</td><td>0x0000_0168</td></tr><tr><td>IRQ75</td><td>91</td><td>TIMER4 中断</td><td>0x0000_016C</td></tr><tr><td>IRQ76</td><td>92</td><td>TIMER15 中断</td><td>0x0000_0170</td></tr><tr><td>IRQ77</td><td>93</td><td>TIMER16 中断</td><td>0x0000_0174</td></tr><tr><td>IRQ78</td><td>94</td><td>TIMER0 通道中止中断</td><td>0x0000_0178</td></tr><tr><td>IRQ79</td><td>95</td><td>TIMER7 通道中止中断</td><td>0x0000_017C</td></tr></table>

## 3.4. 外部中断及事件（EXTI）框图


图 3-1. EXTI 框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-16/4afea6b1-9bfe-4233-8875-cad534b1d7ed/9275e39e7a20287e239f8129ed02fed5347c21e1d355cfc11bbf224ca59d3dd6.jpg)


## 3.5. 外部中断及事件功能概述

EXTI 包含多达 20 个相互独立的边沿检测电路并且可以向处理器产生中断请求或事件唤醒。EXTI提供 3 种触发类型：上升沿触发，下降沿触发和任意沿触发。EXTI 中每个边沿检测电路都可以分别予以配置或屏蔽。

EXTI 触发源包括来自 I/O 管脚的 16 根线以及来自内部模块的 4 根线具体细节参考 3-3. EXTI。通过配置 GPIO 模块的 AFIO_EXTISSx 寄存器，所有的 GPIO 管脚都可以被选作 EXT的触发源，具体细节请参考 / GPIO AFIO 章节。

除了中断，EXTI 还可以向处理器提供事件信号。The Cortex®-M33 内核完全支持等待中断（WFI），等待事件（WFE）和发送事件（SEV）指令。芯片内部有一个唤醒中断控制器（WIC），用户可以放心的让处理器和 NVIC 进入功耗极低的省电模式，由 WIC 来识别中断和事件以及判断优先级。当某些预期的事件发生时，例如一个特定的 I/O 管脚电平翻转或者 RTC 闹钟动作，EXTI 能唤醒处理器及整个系统。

## 硬件触发

硬件触发被用来检测外部或内部信号的电压变化。软件需要按如下步骤配置来使用这项功能：

1. 根据应用需要配置 AFIO 模块中的 EXTI 触发源；

2. 配置 EXTI_RTEN 寄存器和 EXTI_FTEN 寄存器以使能相应引脚的上升沿或下降沿检测（软件应当同时配置引脚对应的 RTENx 和 FTENx 位以检测该引脚上升沿和下降沿的变化）；

3. 通过配置引脚对应的 EXTI_INTEN 或 EXTI_EVEN 位，使能中断或事件；

4. EXTI 开始检测被配置的引脚上的电平变化，当这些引脚上期望的变化被检测到时，使能的中断或事件将被触发。如果为中断触发，则对应的 PD 位将立刻被置 1；如果为事件触发，则对应的 PD 位不被置 1。软件需要响应该中断或事件并清除相应 PDx 位。

## 软件触发

按照如下步骤软件也可以触发 EXTI 中断或事件：

1. 配置对应的 EXTI_INTEN 或 EXTI_EVEN 位使能中断或事件；

2. 配置EXTI_SWIEV寄存器的对应SWIEVx位，使能的中断或事件将被立即触发。如果为中断触发，则对应的PD位将立刻被置1；如果为事件触发，则对应的PD位不被置1。软件需要响应该中断或事件并清除相应PDx位。


表 3-3. EXTI 触发源


<table><tr><td>EXTI 线编号</td><td>触发源</td></tr><tr><td>0</td><td>PA0 / PB0 / PC0 / PD0 / PE0</td></tr><tr><td>1</td><td>PA1 / PB1 / PC1 / PD1 / PE1</td></tr><tr><td>2</td><td>PA2 / PB2 / PC2 / PD2 / PE2</td></tr><tr><td>3</td><td>PA3 / PB3 / PC3 / PD3 / PE3</td></tr><tr><td>4</td><td>PA4 / PB4 / PC4 / PD4 / PE4</td></tr><tr><td>5</td><td>PA5 / PB5 / PC5 / PD5 / PE5</td></tr><tr><td>6</td><td>PA6 / PB6 / PC6 / PD6 / PE6</td></tr><tr><td>7</td><td>PA7 / PB7 / PC7 / PD7 / PE7</td></tr><tr><td>8</td><td>PA8 / PB8 / PC8 / PD8 / PE8</td></tr><tr><td>9</td><td>PA9 / PB9 / PC9 / PD9 / PE9</td></tr><tr><td>10</td><td>PA10 / PB10 / PC10 / PD10 / PE10</td></tr><tr><td>11</td><td>PA11 / PB11 / PC11 / PD11 / PE11</td></tr><tr><td>12</td><td>PA12 / PB12 / PC12 / PD12 / PE12</td></tr><tr><td>13</td><td>PA13 / PB13 / PC13 / PD13 / PE13</td></tr><tr><td>14</td><td>PA14 / PB14 / PC14 / PD14 / PE14</td></tr><tr><td>15</td><td>PA15 / PB15 / PC15 / PD15 / PE15</td></tr><tr><td>16</td><td>LVD / VAVD</td></tr><tr><td>17</td><td>RTC 闹钟</td></tr><tr><td>18</td><td>CMP 唤醒</td></tr><tr><td>19</td><td>USBFS 唤醒</td></tr></table>
