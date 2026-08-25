## 5. 中断/事件控制器（EXTI）

## 5.1. 简介

Cortex<sup>®</sup>-M33 集成了嵌套式矢量型中断控制器（Nested Vectored Interrupt Controller（NVIC））来实现高效的异常和中断处理。NVIC 实现了低延迟的异常和中断处理，以及电源管理控制。它和内核是紧密耦合的。更多关于 NVIC 的说明请参考《Cortex®-M33 技术参考手册》。

EXTI（中断/事件控制器）包括 39 个相互独立的边沿检测电路并且能够向处理器内核产生中断请求或唤醒事件。EXTI 有三种触发类型：上升沿触发、下降沿触发和任意沿触发。EXTI 中的每一个边沿检测电路都可以独立配置和屏蔽。

## 5.2. 主要特性

 Cortex®-M33系统异常；

 多达137种可屏蔽的外设中断；

 4位中断优先级配置位—16个中断优先等级；

 高效的中断处理；

 支持异常抢占和咬尾中断；

 将系统从省电模式唤醒；

 EXTI中有多达39个相互独立的边沿检测电路；

 3种触发类型：上升沿触发、下降沿触发和任意沿触发；

 软件中断或事件触发；

 可配置的触发源。

## 5.3. 功能说明

Arm Cortex®-M33处理器和嵌套式矢量型中断控制器（NVIC）在处理（Handler）模式下对所有异常进行优先级区分以及处理。当异常发生时，系统自动将当前处理器工作状态压栈，在执行完中断服务子程序（ISR）后自动将其出栈。

取向量是和当前工作态压栈并行进行的，从而提高了中断入口效率。处理器支持咬尾中断，可实现背靠背中断，大大削减了反复切换工作态所带来的开销。下表列出了Cortex®-M33中的NVIC异常类型。


表5-1. Cortex®-M33中的NVIC异常类型


<table><tr><td>异常类型</td><td>向量编号</td><td>优先级(a)</td><td>向量地址</td><td>描述</td></tr><tr><td>-</td><td>0</td><td>-</td><td>0x0000_0000</td><td>保留</td></tr><tr><td>复位</td><td>1</td><td>-3</td><td>0x0000_0004</td><td>复位</td></tr></table>


GD32G553 用户手册


<table><tr><td>异常类型</td><td>向量编号</td><td>优先级(a)</td><td>向量地址</td><td>描述</td></tr><tr><td>NMI</td><td>2</td><td>-2</td><td>0x0000_0008</td><td>不可屏蔽中断</td></tr><tr><td>硬件故障</td><td>3</td><td>-1</td><td>0x0000_000C</td><td>各种硬件级别的故障</td></tr><tr><td>存储器管理</td><td>4</td><td>可编程设置</td><td>0x0000_0010</td><td>存储器管理</td></tr><tr><td>总线故障</td><td>5</td><td>可编程设置</td><td>0x0000_0014</td><td>预取指故障,存储器访问故障</td></tr><tr><td>用法故障</td><td>6</td><td>可编程设置</td><td>0x0000_0018</td><td>未定义的指令或非法状态</td></tr><tr><td>-</td><td>7-10</td><td>-</td><td>0x0000_001C - 0x0000_002B</td><td>保留</td></tr><tr><td>SVCall 服务调用</td><td>11</td><td>可编程设置</td><td>0x0000_002C</td><td>通过 SWI 指令实现系统服务调用</td></tr><tr><td>调试监控</td><td>12</td><td>可编程设置</td><td>0x0000_0030</td><td>调试监视器</td></tr><tr><td>-</td><td>13</td><td>-</td><td>0x0000_0034</td><td>保留</td></tr><tr><td>PendSV 挂起服务</td><td>14</td><td>可编程设置</td><td>0x0000_0038</td><td>可挂起的系统服务请求</td></tr><tr><td>SysTick</td><td>15</td><td>可编程设置</td><td>0x0000_003C</td><td>系统节拍定时器</td></tr></table>


SysTick校准值设为25000，SysTick时钟频率配置为CK_SYS*0.125。此时若CK_SYS时钟被配置为200MHz，则SysTick中断会1ms响应一次。



表5-2. 中断向量表


<table><tr><td>中断编号</td><td>向量编号</td><td>外设中断描述</td><td>向量地址</td></tr><tr><td>IRQ 0</td><td>16</td><td>窗口看门狗中断</td><td>0x0000_0040</td></tr><tr><td>IRQ 1</td><td>17</td><td>连接到EXTI线16的LVD/VAVD/VOVD/VUVD中断</td><td>0x0000_0044</td></tr><tr><td>IRQ 2</td><td>18</td><td>连接到EXTI线18的RTC侵入和时间戳中断LXTAL时钟阻塞中断</td><td>0x0000_0048</td></tr><tr><td>IRQ 3</td><td>19</td><td>连接到EXTI线19的RTC唤醒中断</td><td>0x0000_004C</td></tr><tr><td>IRQ 4</td><td>20</td><td>FMC全局中断</td><td>0x0000_0050</td></tr><tr><td>IRQ 5</td><td>21</td><td>RCU全局中断</td><td>0x0000_0054</td></tr><tr><td>IRQ 6</td><td>22</td><td>EXTI线0中断</td><td>0x0000_0058</td></tr><tr><td>IRQ 7</td><td>23</td><td>EXTI线1中断</td><td>0x0000_005C</td></tr><tr><td>IRQ 8</td><td>24</td><td>EXTI线2中断</td><td>0x0000_0060</td></tr><tr><td>IRQ 9</td><td>25</td><td>EXTI线3中断</td><td>0x0000_0064</td></tr><tr><td>IRQ 10</td><td>26</td><td>EXTI线4中断</td><td>0x0000_0068</td></tr><tr><td>IRQ 11</td><td>27</td><td>DMA0通道0全局中断</td><td>0x0000_006C</td></tr><tr><td>IRQ 12</td><td>28</td><td>DMA0通道1全局中断</td><td>0x0000_0070</td></tr><tr><td>IRQ 13</td><td>29</td><td>DMA0通道2全局中断</td><td>0x0000_0074</td></tr><tr><td>IRQ 14</td><td>30</td><td>DMA0通道3全局中断</td><td>0x0000_0078</td></tr><tr><td>IRQ 15</td><td>31</td><td>DMA0通道4全局中断</td><td>0x0000_007C</td></tr><tr><td>IRQ 16</td><td>32</td><td>DMA0通道5全局中断</td><td>0x0000_0080</td></tr></table>


GD32G553 用户手册


<table><tr><td>中断编号</td><td>向量编号</td><td>外设中断描述</td><td>向量地址</td></tr><tr><td>IRQ 17</td><td>33</td><td>DMA0通道6全局中断</td><td>0x0000_0084</td></tr><tr><td>IRQ 18</td><td>34</td><td>ADC0和ADC1中断</td><td>0x0000_0088</td></tr><tr><td>IRQ 19-22</td><td>35-38</td><td>保留</td><td>0x0000_008C-0x0000_0098</td></tr><tr><td>IRQ 23</td><td>39</td><td>EXTI线[9:5]中断</td><td>0x0000_009C</td></tr><tr><td>IRQ 24</td><td>40</td><td>TIMER0中止中断</td><td>0x0000_00A0</td></tr><tr><td>IRQ 25</td><td>41</td><td>TIMER0更新中断</td><td>0x0000_00A4</td></tr><tr><td>IRQ 26</td><td>42</td><td>TIMER0触发,换相和索引中断</td><td>0x0000_00A8</td></tr><tr><td>IRQ 27</td><td>43</td><td>TIMER0捕获比较中断</td><td>0x0000_00AC</td></tr><tr><td>IRQ 28</td><td>44</td><td>TIMER1全局中断</td><td>0x0000_00B0</td></tr><tr><td>IRQ 29</td><td>45</td><td>TIMER2全局中断</td><td>0x0000_00B4</td></tr><tr><td>IRQ 30</td><td>46</td><td>TIMER3全局中断</td><td>0x0000_00B8</td></tr><tr><td>IRQ 31</td><td>47</td><td>连接到EXTI线31的I2C0事件和唤醒中断</td><td>0x0000_00BC</td></tr><tr><td>IRQ 32</td><td>48</td><td>I2C0错误中断</td><td>0x0000_00C0</td></tr><tr><td>IRQ 33</td><td>49</td><td>连接到EXTI线32的I2C1事件和唤醒中断</td><td>0x0000_00C4</td></tr><tr><td>IRQ 34</td><td>50</td><td>I2C1错误中断</td><td>0x0000_00C8</td></tr><tr><td>IRQ 35</td><td>51</td><td>SPI0全局中断</td><td>0x0000_00CC</td></tr><tr><td>IRQ 36</td><td>52</td><td>SPI1全局中断</td><td>0x0000_00D0</td></tr><tr><td>IRQ 37</td><td>53</td><td>连接到EXTI线28的USART0全局和唤醒中断</td><td>0x0000_00D4</td></tr><tr><td>IRQ 38</td><td>54</td><td>连接到EXTI线29的USART1全局和唤醒中断</td><td>0x0000_00D8</td></tr><tr><td>IRQ 39</td><td>55</td><td>连接到EXTI线30的USART2全局和唤醒中断</td><td>0x0000_00DC</td></tr><tr><td>IRQ 40</td><td>56</td><td>EXTI线[15:10]中断</td><td>0x0000_00E0</td></tr><tr><td>IRQ 41</td><td>57</td><td>连接到EXTI线17的RTC闹钟中断</td><td>0x0000_00E4</td></tr><tr><td>IRQ 42</td><td>58</td><td>保留</td><td>0x0000_00E8</td></tr><tr><td>IRQ 43</td><td>59</td><td>TIMER7中止,传输和索引错误中断</td><td>0x0000_00EC</td></tr><tr><td>IRQ 44</td><td>60</td><td>TIMER7更新中断</td><td>0x0000_00F0</td></tr><tr><td>IRQ 45</td><td>61</td><td>TIMER7触发,换相和索引中断</td><td>0x0000_00F4</td></tr><tr><td>IRQ 46</td><td>62</td><td>TIMER7捕获比较中断</td><td>0x0000_00F8</td></tr><tr><td>IRQ 47</td><td>63</td><td>ADC2全局中断</td><td>0x0000_00FC</td></tr><tr><td>IRQ 48</td><td>64</td><td>SYSCFG全局中断</td><td>0x0000_0100</td></tr><tr><td>IRQ 49</td><td>65</td><td>连接到EXTI线35的LPTIMER全局和唤醒中断</td><td>0x0000_0104</td></tr><tr><td>IRQ 50</td><td>66</td><td>TIMER4全局中断</td><td>0x0000_0108</td></tr><tr><td>IRQ 51</td><td>67</td><td>SPI2全局中断</td><td>0x0000_010C</td></tr><tr><td>IRQ 52</td><td>68</td><td>UART3全局中断</td><td>0x0000_0110</td></tr><tr><td>IRQ 53</td><td>69</td><td>UART4全局中断</td><td>0x0000_0114</td></tr><tr><td>IRQ 54</td><td>70</td><td>TIMER5全局中断DAC2,DAC0下溢错误中断</td><td>0x0000_0118</td></tr><tr><td>IRQ 55</td><td>71</td><td>TIMER6全局中断DAC3, DAC1 下溢错误中断</td><td>0x0000_011C</td></tr><tr><td>IRQ 56</td><td>72</td><td>DMA1 通道0全局中断</td><td>0x0000_0120</td></tr><tr><td>IRQ 57</td><td>73</td><td>DMA1 通道1全局中断</td><td>0x0000_0124</td></tr><tr><td>IRQ 58</td><td>74</td><td>DMA1 通道2全局中断</td><td>0x0000_0128</td></tr><tr><td>IRQ 59</td><td>75</td><td>DMA1 通道3全局中断</td><td>0x0000_012C</td></tr><tr><td>IRQ 60</td><td>76</td><td>DMA1 通道4全局中断</td><td>0x0000_0130</td></tr><tr><td>IRQ 61</td><td>77</td><td>ADC3 全局中断</td><td>0x0000_0134</td></tr><tr><td>IRQ 62</td><td>78</td><td>保留</td><td>0x0000_0138</td></tr><tr><td>IRQ 63</td><td>79</td><td>VUVD1, VOVD1 中断</td><td>0x0000_013C</td></tr><tr><td>IRQ 64</td><td>80</td><td>连接到EXTI线20/21/22/23的CMP0/CMP1/CMP2/CMP3中断</td><td>0x0000_0140</td></tr><tr><td>IRQ 65</td><td>81</td><td>连接到EXTI线24/36/37/38的CMP4/CMP5/CMP6/CMP7中断</td><td>0x0000_0144</td></tr><tr><td>IRQ 66</td><td>82</td><td>CMP 全局中断</td><td>0x0000_0148</td></tr><tr><td>IRQ 67</td><td>83</td><td>HRTIMER 中断0</td><td>0x0000_014C</td></tr><tr><td>IRQ 68</td><td>84</td><td>HRTIMER 中断1</td><td>0x0000_0150</td></tr><tr><td>IRQ 69</td><td>85</td><td>HRTIMER 中断2</td><td>0x0000_0154</td></tr><tr><td>IRQ 70</td><td>86</td><td>HRTIMER 中断3</td><td>0x0000_0158</td></tr><tr><td>IRQ 71</td><td>87</td><td>HRTIMER 中断4</td><td>0x0000_015C</td></tr><tr><td>IRQ 72</td><td>88</td><td>HRTIMER 中断5</td><td>0x0000_0160</td></tr><tr><td>IRQ 73</td><td>89</td><td>HRTIMER 中断6</td><td>0x0000_0164</td></tr><tr><td>IRQ 74</td><td>90</td><td>HRTIMER 中断7</td><td>0x0000_0168</td></tr><tr><td>IRQ 75</td><td>91</td><td>HRTIMER 中断8</td><td>0x0000_016C</td></tr><tr><td>IRQ 76</td><td>92</td><td>HRTIMER 中断9</td><td>0x0000_0170</td></tr><tr><td>IRQ 77</td><td>93</td><td>TIMER19 中止,传输和索引错误中断</td><td>0x0000_0174</td></tr><tr><td>IRQ 78</td><td>94</td><td>TIMER19 更新中断</td><td>0x0000_0178</td></tr><tr><td>IRQ 79</td><td>95</td><td>TIMER19 触发,换相和索引中断</td><td>0x0000_017C</td></tr><tr><td>IRQ 80</td><td>96</td><td>TIMER19 捕获比较中断</td><td>0x0000_0180</td></tr><tr><td>IRQ 81</td><td>97</td><td>FPU 全局中断</td><td>0x0000_0184</td></tr><tr><td>IRQ 82</td><td>98</td><td>连接到EXTI线33的I2C2事件和唤醒中断</td><td>0x0000_0188</td></tr><tr><td>IRQ 83</td><td>99</td><td>I2C2 错误中断</td><td>0x0000_018C</td></tr><tr><td>IRQ 84</td><td>100</td><td>保留</td><td>0x0000_0190</td></tr><tr><td>IRQ 85</td><td>101</td><td>CAU 全局中断</td><td>0x0000_0194</td></tr><tr><td>IRQ 86-89</td><td>102-105</td><td>保留</td><td>0x0000_0198-0x0000_01A4</td></tr><tr><td>IRQ 90</td><td>106</td><td>TRNG 全局中断</td><td>0x0000_01A8</td></tr><tr><td>IRQ 91</td><td>107</td><td>保留</td><td>0x0000_01AC</td></tr><tr><td>IRQ 92</td><td>108</td><td>连接到EXTI线34的I2C3事件和唤醒中断</td><td>0x0000_01B0</td></tr><tr><td>IRQ 93</td><td>109</td><td>I2C3 错误中断</td><td>0x0000_01B4</td></tr><tr><td>IRQ 94</td><td>110</td><td>DMAMUX 上溢中断</td><td>0x0000_01B8</td></tr><tr><td>IRQ 95</td><td>111</td><td>QSPI 全局中断</td><td>0x0000_01BC</td></tr><tr><td>IRQ 96</td><td>112</td><td>FFT 全局中断</td><td>0x0000_01C0</td></tr><tr><td>IRQ 97</td><td>113</td><td>DMA1 通道5 全局中断</td><td>0x0000_01C4</td></tr><tr><td>IRQ 98</td><td>114</td><td>DMA1 通道6 全局中断</td><td>0x0000_01C8</td></tr><tr><td>IRQ 99</td><td>115</td><td>CLA 全局中断</td><td>0x0000_01CC</td></tr><tr><td>IRQ 100</td><td>116</td><td>TMU 全局中断</td><td>0x0000_01D0</td></tr><tr><td>IRQ 101</td><td>117</td><td>FAC 全局中断</td><td>0x0000_01D4</td></tr><tr><td>IRQ 102</td><td>118</td><td>HPDF 全局中断0</td><td>0x0000_01D8</td></tr><tr><td>IRQ 103</td><td>119</td><td>HPDF 全局中断1</td><td>0x0000_01DC</td></tr><tr><td>IRQ 104</td><td>120</td><td>HPDF 全局中断2</td><td>0x0000_01E0</td></tr><tr><td>IRQ 105</td><td>121</td><td>HPDF 全局中断3</td><td>0x0000_01E4</td></tr><tr><td>IRQ 106</td><td>122</td><td>TIMER14 全局中断</td><td>0x0000_01E8</td></tr><tr><td>IRQ 107</td><td>123</td><td>TIMER15 全局中断</td><td>0x0000_01EC</td></tr><tr><td>IRQ 108</td><td>124</td><td>TIMER16 全局中断</td><td>0x0000_01F0</td></tr><tr><td>IRQ 109</td><td>125</td><td>连接到EXTI 线25 的CAN 唤醒中断</td><td>0x0000_01F4</td></tr><tr><td>IRQ 110</td><td>126</td><td>CAN0 消息缓冲区中断</td><td>0x0000_01F8</td></tr><tr><td>IRQ 111</td><td>127</td><td>CAN0 总线关闭/总线关闭完成中断</td><td>0x0000_01FC</td></tr><tr><td>IRQ 112</td><td>128</td><td>CAN0 错误中断</td><td>0x0000_0200</td></tr><tr><td>IRQ 113</td><td>129</td><td>CAN0 快速传输错误中断</td><td>0x0000_0204</td></tr><tr><td>IRQ 114</td><td>130</td><td>CAN0 发送警告中断</td><td>0x0000_0208</td></tr><tr><td>IRQ 115</td><td>131</td><td>CAN0 接收警告中断</td><td>0x0000_020C</td></tr><tr><td>IRQ 116</td><td>132</td><td>连接到EXTI 线的CAN1 唤醒中断</td><td>0x0000_0210</td></tr><tr><td>IRQ 117</td><td>133</td><td>CAN1 消息缓冲区中断</td><td>0x0000_0214</td></tr><tr><td>IRQ 118</td><td>134</td><td>CAN1 总线关闭/总线关闭完成中断</td><td>0x0000_0218</td></tr><tr><td>IRQ 119</td><td>135</td><td>CAN1 错误中断</td><td>0x0000_021C</td></tr><tr><td>IRQ 120</td><td>136</td><td>CAN1 快速传输错误中断</td><td>0x0000_0220</td></tr><tr><td>IRQ 121</td><td>137</td><td>CAN1 发送警告中断</td><td>0x0000_0224</td></tr><tr><td>IRQ 122</td><td>138</td><td>CAN1 接收警告中断</td><td>0x0000_0228</td></tr><tr><td>IRQ 123</td><td>139</td><td>连接到EXTI 线27 的CAN2 唤醒中断</td><td>0x0000_022C</td></tr><tr><td>IRQ 124</td><td>140</td><td>CAN2 消息缓冲区中断</td><td>0x0000_0230</td></tr><tr><td>IRQ 125</td><td>141</td><td>CAN2 总线关闭/总线关闭完成中断</td><td>0x0000_0234</td></tr><tr><td>IRQ 126</td><td>142</td><td>CAN2 错误中断</td><td>0x0000_0238</td></tr><tr><td>IRQ 127</td><td>143</td><td>CAN2 快速传输错误中断</td><td>0x0000_023C</td></tr><tr><td>IRQ 128</td><td>144</td><td>CAN2 发送警告中断</td><td>0x0000_0240</td></tr><tr><td>IRQ 129</td><td>145</td><td>CAN2 接收警告中断</td><td>0x0000_0244</td></tr><tr><td>IRQ 130</td><td>146</td><td>TIMER0 DEC 中断</td><td>0x0000_0248</td></tr><tr><td>IRQ 131</td><td>147</td><td>TIMER1 DEC 中断</td><td>0x0000_024C</td></tr><tr><td>IRQ 132</td><td>148</td><td>TIMER2 DEC 中断</td><td>0x0000_0250</td></tr><tr><td>IRQ 133</td><td>149</td><td>TIMER3 DEC 中断</td><td>0x0000_0254</td></tr><tr><td>IRQ 134</td><td>150</td><td>TIMER4 DEC 中断</td><td>0x0000_0258</td></tr><tr><td>IRQ 135</td><td>151</td><td>TIMER7 DEC 中断</td><td>0x0000_025C</td></tr><tr><td>IRQ 136</td><td>152</td><td>TIMER19 DEC 中断</td><td>0x0000_0260</td></tr></table>

## 5.4. 外部中断及事件（EXTI）框图


图5-1. EXTI框图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-17/50457709-dd32-4835-b12d-50ae1e799633/5b77ed5cd0d78f6667cf609e3fe924ecf5081203c6a8c1b98db187ecc96d7562.jpg)


## 5.5. 外部中断及事件功能概述

EXTI 包含多达 39 个相互独立的边沿检测电路并且可以向处理器产生中断请求或事件唤醒。EXT提供 3 种触发类型：上升沿触发，下降沿触发和任意沿触发。EXTI 中每个边沿检测电路都可以分别予以配置或屏蔽。

EXTI 触发源包括来自 I/O 管脚的 16 根线以及来自内部模块的 23 根线，（包括 LVD，RTC 闹钟，RTC 侵入和时间戳，LXTAL 时钟阻塞，RTC 唤醒，CMP，CAN，USART 唤醒，I2C 唤醒，LPTIM唤醒，OVD）。通过配置 SYSCFG 模块的 SYSCFG_EXTISSx 寄存器，所有的 GPIO 管脚都可以被选作 EXTI 的触发源，具体细节请参考 SYSCFG 。

除了中断，EXTI 还可以向处理器提供事件信号。Cortex®-M33 内核完全支持等待中断（WFI），等待事件（WFE）和发送事件（SEV）指令。芯片内部有一个唤醒中断控制器（WIC），用户可以放心的让处理器和 NVIC 进入功耗极低的省电模式，由 WIC 来识别中断和事件以及判断优先级。当某些预期的事件发生时，例如一个特定的 I/O 管脚电平翻转或者 RTC 闹钟动作，EXTI 能唤醒处理器及整个系统。


表5-3. EXTI触发源


<table><tr><td>EXTI 线编号</td><td>触发源</td></tr><tr><td>0</td><td>PA0 / PB0 / PC0 / PD0 / PE0 / PF0 / PG0</td></tr><tr><td>1</td><td>PA1 / PB1 / PC1 / PD1 / PE1 / PF1 / PG1</td></tr><tr><td>2</td><td>PA2 / PB2 / PC2 / PD2 / PE2 / PF2 / PG2</td></tr><tr><td>3</td><td>PA3 / PB3 / PC3 / PD3 / PE3 / PF3 / PG3</td></tr><tr><td>4</td><td>PA4 / PB4 / PC4 / PD4 / PE4 / PF4 / PG4</td></tr><tr><td>5</td><td>PA5 / PB5 / PC5 / PD5 / PE5 / PF5 / PG5</td></tr><tr><td>6</td><td>PA6 / PB6 / PC6 / PD6 / PE6 / PF6 / PG6</td></tr><tr><td>7</td><td>PA7 / PB7 / PC7 / PD7 / PE7 / PF7 / PG7</td></tr><tr><td>8</td><td>PA8 / PB8 / PC8 / PD8 / PE8 / PF8 / PG8</td></tr><tr><td>9</td><td>PA9 / PB9 / PC9 / PD9 / PE9 / PF9 / PG9</td></tr><tr><td>10</td><td>PA10 / PB10 / PC10 / PD10 / PE10 / PF10 / PG10</td></tr><tr><td>11</td><td>PA11 / PB11 / PC11 / PD11 / PE11 / PF11</td></tr><tr><td>12</td><td>PA12 / PB12 / PC12 / PD12 / PE12 / PF12</td></tr><tr><td>13</td><td>PA13 / PB13 / PC13 / PD13 / PE13 / PF13</td></tr><tr><td>14</td><td>PA14 / PB14 / PC14 / PD14 / PE14 / PF14</td></tr><tr><td>15</td><td>PA15 / PB15 / PC15 / PD15 / PE15 / PF15</td></tr><tr><td>16</td><td>LVD, VAVD, VOVD 和 VUVD</td></tr><tr><td>17</td><td>RTC 闹钟</td></tr><tr><td>18</td><td>RTC 侵入和时间戳事件, LXTAL 时钟阻塞</td></tr><tr><td>19</td><td>RTC 唤醒</td></tr><tr><td>20</td><td>CMP0 输出</td></tr><tr><td>21</td><td>CMP1 输出</td></tr><tr><td>22</td><td>CMP2 输出</td></tr><tr><td>23</td><td>CMP3 输出</td></tr><tr><td>24</td><td>CMP4 输出</td></tr><tr><td>25</td><td>CAN0 唤醒</td></tr><tr><td>26</td><td>CAN1 唤醒</td></tr></table>


GD32G553 用户手册


<table><tr><td>EXTI 线编号</td><td>触发源</td></tr><tr><td>27</td><td>CAN2 唤醒</td></tr><tr><td>28</td><td>USART0 唤醒</td></tr><tr><td>29</td><td>USART1 唤醒</td></tr><tr><td>30</td><td>USART2 唤醒</td></tr><tr><td>31</td><td>I2C0 唤醒</td></tr><tr><td>32</td><td>I2C1 唤醒</td></tr><tr><td>33</td><td>I2C2 唤醒</td></tr><tr><td>34</td><td>I2C3 唤醒</td></tr><tr><td>35</td><td>LPTIM 唤醒</td></tr><tr><td>36</td><td>CMP5 输出</td></tr><tr><td>37</td><td>CMP6 输出</td></tr><tr><td>38</td><td>CMP7 输出</td></tr></table>
