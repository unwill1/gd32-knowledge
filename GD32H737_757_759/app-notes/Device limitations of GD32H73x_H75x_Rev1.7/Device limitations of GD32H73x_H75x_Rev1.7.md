# GigaDevice Semiconductor Inc.

# Device limitations of GD32H73x/H75x

Errata Sheet 

Revision 1.7 

(Nov. 2025) 

## Table of Contents

Table of Contents....2
List of Figures....4
List of Tables....5
1. Introduction....6
1.1. Revision identification....6
1.2. Summary of device limitations....6
2. Descriptions of device limitations....9
2.1. SYSTEM....9
2.1.1. SysTick is clocked with the system clock (CK_SYS) divided by 2 when using external clock source....9
2.1.2. ECC error due to illegal address access....9
2.1.3. When the system operates at high frequency and both the interrupt vector table and interrupt handling code are placed in ITCM, high-frequency interrupts may probabilistically cause false ITCM ECC error alarm....9
2.2. FMC....10
2.2.1. Protection-removed mass erase function cannot be disabled....10
2.3. PMU....10
2.3.1. Chip damage risk in SMPS mode of the LQFP package....10
2.3.2. VDDSMPS cannot be connected to a low level when not using SMPS....11
2.4. GPIO....11
2.4.1. PXY pin connects to PXY_C pin in standby mode....11
2.4.2. After VDD and VDDA are powered off, if voltage continues to be injected into GPIO (except for PA9 / PA10 / PB12 / PB13), it may lead to an overcurrent risk in the chip's GPIO....11
2.5. TRNG....12
2.5.1. LFSR algorithm failure....12
2.6. DBG....12
2.6.1. SWD and JTAG debug function failure when using low power debug function....12
2.6.2. SWD connection fails when PA15 is low level....12
2.7. ADC....13
2.7.1. The analog watchdog threshold comparison fails when used simultaneously with oversampling in a 14-bit ADC....13
2.8. RTC....13
2.8.1. When using RTC reference clock detection function, PB13 / PB15 will be configured as input floating mode....13
2.8.2. Voltage or temperature changes in the backup domain cannot trigger the tamper function . 13 

2.9. TIMER....14
2.9.1. TIMER interrupt is at risk of triggering by mistake....14
2.10. USART....14
2.10.1. When USART FIFO is enabled, the last byte of the frame cannot be transmitted....14
2.10.2. When USART FIFO is enabled, DMA cannot transmit data....15
2.10.3. Data sample error occurs in LIN mode....15
2.10.4. In mute mode, the parity error caused by non-wake frames will set PERR bit....15
2.11. I2S....16
2.11.1. When I2S1 is used for communication and the GPIO and I2S1 configurations are in a special combination, it will probabilistically cause the I2S1_CK and I2S1_WS pins to continuously output signals....16
2.12. OSPI....16
2.12.1. Interrupt and DMA functions are invalid when OSPI is used in indirect write mode....16
2.12.2. When OSPI sends only data segments, the first clock is lost....17
2.12.3. When OSPI running clock is greater than 100MHz, read external memory status flag abnormal in status polling mode....17
2.13. EXMC....17
2.13.1. Auto refresh function of SDRAM controller is influenced by other EXMC controller....17
2.13.2. The bus may stuck during SDRAM access....18
2.13.3. Does not support unaligned address access....18
2.14. LPDTS....18
2.14.1. The temperature sensor ready flag cannot be cleared after disabling LPDTS....18
2.15. CAN....19
2.15.1. The transmit mailbox may experience transmission failures when exiting inactive mode....19
2.15.2. CAN transmit node performs unwanted automatic calibration....19
2.15.3. The CAN peripheral cannot function without using HXTAL....19
2.15.4. CAN RAM area may be tampered in receiving mailbox processing....20
2.15.5. After Bus off recovery, transmit error count is not cleared automatically....20
2.15.6. The mailbox data is not read in time may result in incorrect data reading for the current and next frames....21
2.15.7. When the CAN operating clock frequency is less than CK_APB2 and an error occurs in DLC segment, which will lead to receiving an incorrect frame ID....21
2.16. USBHS....22
2.16.1. USBHS OTG sensitivity problem....22
2.17. Core....22
3. Revision history....23 

## List of Figures

Figure 1-1. Device revision code of GD32H73x/H75x....6 

## List of Tables

Table 1-1. Applicable products....6
Table 1-2. Device limitations....6
Table 3-1. Revision history....23 

## 1. Introduction

This document applies to GD32H73x/H75x product series, as shown in Table 1-1. Applicable products. It offers technical guidance for using GD32MCU and provides workaround to current device limitations. 


Table 1-1. Applicable products


<table><tr><td>Type</td><td>Part Numbers</td></tr><tr><td rowspan="3">MCU</td><td>GD32H737xx series</td></tr><tr><td>GD32H757xx series</td></tr><tr><td>GD32H759xx series</td></tr></table>

## 1.1. Revision identification

The device revision can be identified according to the mark on the top of the package. The 1st code on Line 3 of the mark is the product revision code, as shown in Figure 1-1. Device revision code of GD32H73x/H75x. 


Figure 1-1. Device revision code of GD32H73x/H75x


<table><tr><td>GD32H759IMK6A23567MS2330GigaDeviceARM</td><td>Revision Code</td></tr></table>

## 1.2. Summary of device limitations

The device limitations of GD32H73X/H75X are shown in Table 1-2. Device limitations please refer to Section 2 for more details 


Table 1-2. Device limitations


<table><tr><td rowspan="2">Module</td><td rowspan="2">Limitations</td><td colspan="2">Workaround</td></tr><tr><td>Rev. Code A</td><td>Rev. Code C</td></tr><tr><td rowspan="3">SYSTEM</td><td>SysTick is clocked with the system clock (CK_SYS) divided by 2 when using external clock source</td><td>Y</td><td>--</td></tr><tr><td>ECC error due to illegal address access</td><td>Y</td><td>--</td></tr><tr><td>When the system operates at high frequency and both the interrupt vector table and interrupt handling code are placedin ITCM, high-frequency interrupts may probabilistically cause false ITCM ECC error</td><td>Y</td><td>Y</td></tr><tr><td>FMC</td><td>Protection-removed mass erase function cannot be disabled</td><td>N</td><td>--</td></tr><tr><td rowspan="2">PMU</td><td>Chip damage risk in SMPS mode of the LQFP package</td><td>Y</td><td>--</td></tr><tr><td>VDDSMPS cannot be connected to a low level when not using SMPS</td><td>Y</td><td>--</td></tr><tr><td rowspan="2">GPIO</td><td>PXY pin connects to PXY_C pin in standby mode</td><td>Y</td><td>--</td></tr><tr><td>After VDD and VDDA are powered off, if voltage continues to be injected into GPIO (except for PA9 / PA10 / PB12 / PB13), it may lead to an overcurrent risk in the chip's GPIO</td><td>Y</td><td>Y</td></tr><tr><td>TRNG</td><td>LFSR algorithm failure</td><td>Y</td><td>--</td></tr><tr><td rowspan="2">DBG</td><td>SWD and JTAG debug function failure when using low power debug function</td><td>N</td><td>--</td></tr><tr><td>SWD connection fails when PA15 is low level</td><td>Y</td><td>--</td></tr><tr><td>ADC</td><td>The analog watchdog threshold comparison fails when used simultaneously with oversampling in a 14-bit ADC</td><td>Y</td><td>--</td></tr><tr><td rowspan="2">RTC</td><td>When using RTC reference clock detection function, PB13 / PB15 will be configured as input floating mode</td><td>Y</td><td>--</td></tr><tr><td>Voltage or temperature changes in the backup domain cannot trigger the tamper function</td><td>N</td><td>--</td></tr><tr><td>TIMER</td><td>TIMER interrupt is at risk of triggering by mistake</td><td>Y</td><td>Y</td></tr><tr><td rowspan="4">USART</td><td>When USART FIFO is enabled, the last byte of the frame cannot be transmitted</td><td>Y</td><td>--</td></tr><tr><td>When USART FIFO is enabled, DMA cannot transmit data</td><td>Y</td><td>--</td></tr><tr><td>Data sample error occurs in LIN mode</td><td>Y</td><td>Y</td></tr><tr><td>In mute mode, the parity error caused by non-wake frames will set PERR bit</td><td>Y</td><td>Y</td></tr><tr><td>I2S</td><td>When I2S1 is used for communication and the GPIO and I2S1 configurations are in a special combination, it will probabilistically cause the I2S1_CK and I2S1_WS pins to continuously output signals</td><td>Y</td><td>Y</td></tr><tr><td rowspan="3">OSPI</td><td>Interrupt and DMA functions are invalid when OSPI is used in indirect write mode</td><td>Y</td><td>--</td></tr><tr><td>When OSPI sends only data segments, the first clock is lost</td><td>Y</td><td>Y</td></tr><tr><td>When OSPI running clock is greater than 100MHz, read external memory status flag abnormal in status polling mode</td><td>Y</td><td>Y</td></tr><tr><td rowspan="3">EXMC</td><td>Auto refresh function of SDRAM controller is influenced by other EXMC controller</td><td>Y</td><td>--</td></tr><tr><td>The bus may stuck during SDRAM access</td><td>Y</td><td>Y</td></tr><tr><td>Does not support unaligned address access</td><td>Y</td><td>Y</td></tr><tr><td>LPDTS</td><td>The temperature sensor ready flag cannot be cleared after disabling LPDTS</td><td>Y</td><td>--</td></tr><tr><td rowspan="7">CAN</td><td>The transmit mailbox may experience transmission failures when exiting inactive mode</td><td>Y</td><td>--</td></tr><tr><td>CAN transmit node performs unwanted automatic calibration</td><td>Y</td><td>--</td></tr><tr><td>The CAN peripheral cannot function without using HXTAL</td><td>Y</td><td>--</td></tr><tr><td>CAN RAM area may be tampered in receiving mailbox processing</td><td>Y</td><td>Y</td></tr><tr><td>After Bus off recovery, transmit error count is not cleared automatically</td><td>Y</td><td>Y</td></tr><tr><td>The mailbox data is not read in time may result in incorrect data reading for the current and next frames</td><td>Y</td><td>Y</td></tr><tr><td>When the CAN operating clock frequency is less than CK_APB2 and an error occurs in DLC segment, which will lead to receiving an incorrect frame ID</td><td>Y</td><td>Y</td></tr><tr><td>USBHS</td><td>USBHS OTG sensitivity problem</td><td>Y</td><td>--</td></tr></table>


Note: 



Y = Limitation present, workaround available 



N = Limitation present, no workaround available 



'--' = Limitation fixed 


## 2. Descriptions of device limitations

## 2.1. SYSTEM

## 2.1.1. SysTick is clocked with the system clock (CK_SYS) divided by 2 when using external clock source

Description & impact 

When SysTick uses external clock source, the SysTick clock is CK_SYS / 2 instead of CK_SYS / 8. 

Workarounds 

Use CK_SYS / 2 to calculate the SysTick time when using external clock source. 

## 2.1.2. ECC error due to illegal address access

Description & impact 

When illegal address is accessed, CPU will generate ECC error. 

Workarounds 

Use one of the following solutions: 

1) Avoid accessing illegal addresses. 

2) Implement software processes to handle ECC errors after accessing an illegal address. 

## 2.1.3. When the system operates at high frequency and both the interrupt vector table and interrupt handling code are placed in ITCM, high-frequency interrupts may probabilistically cause false ITCM ECC error alarm

Description & impact 

When the system clock is configured to a high frequency (e.g., 600MHz), the AXI/AHB clock is configured to half the system clock frequency, and TCM inserts wait states (TCM_WAITSTATE = 1), placing both the interrupt vector table and interrupt handling code in ITCM may probabilistically cause false ITCM ECC error alarm when high-frequency interrupts occur. 

Note: When the system clock exceeds 350MHz, TCM requires wait states to be inserted. 

## Workarounds

Use one of the following solutions: 

1) Place the interrupt vector table in AXISRAM. 

2) Avoid placing both the interrupt vector table and interrupt handling code in the same TCM block. For example, place the interrupt vector table in DTCM and the interrupt handling code in ITCM. 

3) Adopt a frequency reduction scheme. Avoid simultaneous conditions where TCM_WAITSTATE = 1 and the AXI/AHB clock is configured to half the system clock frequency. For instance, configure both the system clock and AXI/AHB clock to 300MHz. 

## 2.2. FMC

## 2.2.1. Protection-removed mass erase function cannot be disabled

## Description & impact

The mass erase operation will only perform the protection-removed function when the following conditions are all satisfied in the protection-removed mass erase sequence: 

1. If a secure user area exists, set the SCR_EREN bit in the FMC_SCRADDR_MD register and ensure that the secure user area end address is less than the secure user area start address by programming SCR_AREA_END < SCR_AREA_START to the FMC_SCRADDR_EFT register. 

2. Set all WP (Write Protection) bits in the FMC_WP_MDF register if any erase/program protected sector exists. 

3. Unlock the FMC_CTL register if necessary.

Otherwise, the protection-removed mass erase function cannot be disabled. Information regarding the protection-removed mass erase can be found in Chapter 3.3.5 of the user manual. 

## Workarounds

Not available. 

## 2.3. PMU

## 2.3.1. Chip damage risk in SMPS mode of the LQFP package

## Description & impact

In the LQFP package, there is a risk of chip damage due to leakage when the junction temperature (Tj) exceeds 125°C in SMPS mode. 

Note: This limitation applies to LQFP176 package. 

Workarounds 

Avoid using SMPS mode in the LQFP package. 

## 2.3.2. VDDSMPS cannot be connected to a low level when not using SMPS

## Description & impact

VDDSMPS cannot be connected to a low level when not using SMPS. 

Note: This limitation applies to LQFP176 and BGA176 package. 

Workarounds 

Connect VDDSMPS pin to a high level or leave it floating when SMPS mode is not used. 

## 2.4. GPIO

## 2.4.1. PXY pin connects to PXY_C pin in standby mode

## Description & impact

When the MCU enters standby mode, the PXY pin will connect to the PXY_C pin, which includes PA0 / PA0_C, PA1 / PA1_C, PC2 / PC2_C, and PC3 / PC3_C. 

## Workarounds

Evaluate the impact based on application scenarios, such as using PA0 as wakeup pin in standby mode. 

## 2.4.2. After VDD and VDDA are powered off, if voltage continues to be injected into GPIO (except for PA9 / PA10 / PB12 / PB13), it may lead to an overcurrent risk in the chip's GPIO

## Description & impact

When the chip's VDD and VDDA are powered off, if voltage (Vin) continues to be injected externally into the GPIO (except for PA9 / PA10 / PB12 / PB13), due to the ESD protection circuit of the GPIO, the externally injected voltage may leak to VDD, forming a voltage of Vin-0.7V. If Vin-0.7V is near the POR (1.6V), it may satisfy the POR conditions for the chip. However, due to the limited overcurrent capacity of the GPIO, this may lead to repeated POR/PDR events in the system, resulting in unpredictable risks for the system. 

## Workarounds

In system design, an undervoltage reset chip should be externally connected between the chip's VDD and NRST to ensure that when the voltage leaked from GPIO to VDD is below the threshold voltage of the undervoltage reset chip, it can directly pull down NRST to avoid erroneous operations. For a specific solution, you can refer to the "AN225 GD32H7xx Power Bypass Mode User Guide". 

## 2.5. TRNG

## 2.5.1. LFSR algorithm failure

## Description & impact

The LFSR (Linear Feedback Shift Register) algorithm for generating random numbers is not functioning. 

## Workarounds

Do not use LFSR; instead, use the NIST (National Institute of Standards and Technology) algorithm. 

## 2.6. DBG

## 2.6.1. SWD and JTAG debug function failure when using low power debug function

## Description & impact

When using the low power debug function (set STB_HOLD / DSLP_HOLD / SLP_HOLD bit), the debug function will fail. 

## Workarounds

Do not use low power debug function. 

## 2.6.2. SWD connection fails when PA15 is low level

## Description & impact

After power-on, if the level of PA15 is low, the SWD connection will fail. 

## Workarounds

Use one of the following solutions: 

1) Do not drive PA15 to a low level when using SWD debug. 

2) Do not configure PA15 as an AF0 function. 

## 2.7. ADC

## 2.7.1. The analog watchdog threshold comparison fails when used simultaneously with oversampling in a 14-bit ADC

## Description & impact

When the oversample function is enabled in a 14-bit ADC (ADC0/ADC1), the analog watchdog function fails because it does not compare the accumulated sum with the low threshold. 

## Workarounds

Do not use the analog watchdog function simultaneously with oversampling in a 14-bit ADC. 

## 2.8. RTC

## 2.8.1. When using RTC reference clock detection function, PB13 / PB15 will be configured as input floating mode

## Description & impact

When using the RTC reference clock detection function (by setting the REFEN bit in the RTC_CTL register), PB13/PB15 pins will be set to input floating mode. 

## Workarounds

Use one of the following solutions: 

1) Do not use the RTC reference clock detection function. 

2) When using the RTC reference clock detection function, set PB13/PB15 to input floating mode. 

## 2.8.2. Voltage or temperature changes in the backup domain cannot trigger the tamper function

## Description & impact

When the backup domain supply is VBAT due to VDD power down, voltage and temperature changes cannot trigger the tamper function. 

## Workarounds

Not available. 

## 2.9. TIMER

## 2.9.1. TIMER interrupt is at risk of triggering by mistake

## Description & impact

When the TIMER interrupt is enabled and the MCU operates at a high frequency, there is a risk that the corresponding TIMER interrupt flag may not be cleared in time due to the high code execution speed and the time required to clear the interrupt flag, leading to the risk of repeatedly entering the TIMER interrupt. 

## Workarounds

Clear the corresponding TIMER interrupt flag at the beginning of the TIMER interrupt handling function, and maintain more than 20 instruction cycles before exiting the interrupt. 

## 2.10. USART

## 2.10.1. When USART FIFO is enabled, the last byte of the frame cannot be transmitted

## Description & impact

When USART FIFO function is enabled, USART will not transmit the last byte of a frame. For example, when transmitting ten characters '0123456789', the character '9' will not be transmitted. 

## Workarounds

Fill an invalid byte at the end of a transmit frame, such as '\n' in '0123456789\n', and to ensure proper transmission, the following operation needs to be executed before every data transmit. 

1) Disable fifo 

2) Disable usart 

3) Transmit data flush request (set TXFCMD bit) 

4) Enable fifo 

5) Enable usart 

## 2.10.2. When USART FIFO is enabled, DMA cannot transmit data

## Description & impact

When both USART FIFO and USART DMA functions are enabled, DMA can transmit data only once. 

## Workarounds

Use one of the following solutions: 

1) Use USART DMA only; do not use USART FIFO. 

2) Use USART FIFO only; do not use USART DMA. 

## 2.10.3. Data sample error occurs in LIN mode

## Description & impact

When USART is in LIN mode as a receiver, data sample errors occur because the autobaud rate detection function is enabled before receiving the break frame. 

## Workarounds

1) Disable the autobaud rate detection function before receiving the break frame. 

2) Enable the autobaud rate detection function after the LIN break detected flag (LBDF) is set. 

## 2.10.4. In mute mode, the parity error caused by non-wake frames will set PERR bit

## Description & impact

In mute mode, a parity error caused by a non-wake frame will result in a parity error (the PERR bit in the USART_STAT register is set) when no parity error is found in the wake frame. 

## Workarounds

The software ignores the parity error flag generated in this case. 

## 2.11. I2S

## 2.11.1. When I2S1 is used for communication and the GPIO and I2S1 configurations are in a special combination, it will probabilistically cause the I2S1_CK and I2S1_WS pins to continuously output signals

### Description & impact

I2S1_CK and I2S1_WS pins will probabilistically output signals continuously when I2S1 is used for communication and GPIO and I2S1 are configured in a special combination. The specific configuration and phenomenon are as follows: 

<table><tr><td>GPIO configuration</td><td>I2S1 configuration</td><td>Phenomenon</td></tr><tr><td>GPIO_PUPD_PULLDOWN</td><td>I2S_CKPL_HIGH</td><td>I2S1_CK and I2S1_WS output signals continuously</td></tr><tr><td>GPIO_PUPD_NONE</td><td>I2S_CKPL_HIGH</td><td>I2S1_CK and I2S1_WS output signals continuously</td></tr><tr><td>GPIO_PUPD_PULLUP</td><td>I2S_CKPL_HIGH</td><td>I2S1 works normally</td></tr><tr><td>GPIO_PUPD_PULLDOWN</td><td>I2S_CKPL_LOW</td><td>I2S1 works normally</td></tr><tr><td>GPIO_PUPD_PULLUP</td><td>I2S_CKPL_LOW</td><td>I2S1 works normally</td></tr><tr><td>GPIO_PUPD_NONE</td><td>I2S_CKPL_LOW</td><td>I2S1 works normally</td></tr></table>

### Workarounds

Please refer to the above for proper configuration of GPIO and I2S1. 

## 2.12. OSPI

## 2.12.1. Interrupt and DMA functions are invalid when OSPI is used in indirect write mode

Description & impact 

When using OSPI indirect write mode, interrupt and DMA functions are invalid because the FIFO threshold flag (FT) cannot be set. 

Workarounds 

Use polling mode instead of indirect write mode. 

## 2.12.2. When OSPI sends only data segments, the first clock is lost

## Description & impact

When OSPI sends only data segments, the first clock is lost, which results in the first data loss. 

## Workarounds

Send the first data as a command. 

## 2.12.3. When OSPI running clock is greater than 100MHz, read external memory status flag abnormal in status polling mode

## Description & impact

When the OSPI running clock is greater than 100MHz, the external memory may not be ready due to the hardware continuous polling interval is not enough, then OSPI will perform subsequent operations, which results in an exception. 

## Workarounds

Add a hardware delay (such as 20ms delay) before each poll of memory state. 

## 2.13. EXMC

## 2.13.1. Auto refresh function of SDRAM controller is influenced by other EXMC controller

## Description & impact

Auto refresh function of SDRAM controller is influenced by other EXMC controller. When SDRAM controller execute auto refresh command, if the SDRAM bank is active, the precharge command shall be generated, which need EXMC_A10 port be 1. At that time, EXMC_A10 port is used in other EXMC controller, then the SDRAM auto refresh command execute abnormally which lead SDRAM data error. 

## Workarounds

Step1: enable EXMC SDRAM controller works simultaneously with other controllers after EXMC initialization. 

```c
/* code example */
REG32(EXMC + 0x184U) = 0x9EF02310U;
EXMC_SDRSCTL |= BIT(9); 
```

Step 2:

Method 1: When SDRAM controller selects the BANK address of the operation, the pin output does not use the AF function and accesses the corresponding BANK directly through GPIO to drive the BANK address. 

Method 2: Before EXMC operates on NAND FLASH, the global precharge instruction of SDRAM is added, so that the self-refresh operation of SDRAM does not need to rely on the original precharge instruction, so even if the self-refresh and nand occur at the same time, there is no error. 

```txt
/* code example */
REG32(0xA0000150U) = (uint32_t)0x00000012U;
while(0x00000000 != (REG32(0xA0000158U) & 0x00000020)) {
} 
```

## 2.13.2. The bus may stuck during SDRAM access

## Description & impact

When accessing SDRAM, if the SDRAM data bit width is 32 bits, the bus sends two 8-bit or two 16-bit accesses, and then sends a 64-bit access, if the 64-bit access data happens to be composed of the previous two 8-bit or 16-bit accesses, the bus may stuck. 

## Workarounds

Use one of the following solutions: 

1) Disable burst access to SDRAM (clear BRSTRD bit of EXMC_SDCTL0/1 register) 

2) Enable the CPU cache function 

## 2.13.3. Does not support unaligned address access

## Description & impact

The bus does not support unaligned address access to SDRAM. 

## Workarounds

Enable the cache function of the CPU before accessing SDRAM. 

## 2.14. LPDTS

## 2.14.1. The temperature sensor ready flag cannot be cleared after disabling LPDTS

## Description & impact

The temperature sensor ready flag (TSRF) cannot be cleared after disabling LPDTS (Low power digital temperature sensor). 

## Workarounds

Reset the LPDTS peripheral before enabling LPDTS. 

## 2.15. CAN

## 2.15.1. The transmit mailbox may experience transmission failures when exiting inactive mode

## Description & impact

If a mailbox is configured as the Tx mailbox in inactive mode, it may not be sent due to the absence of an internal trigger after exiting inactive mode. 

## Workarounds

Use one of the following solutions: 

1) Another node sends a frame. 

2) Software writes to an invalid mailbox. 

## 2.15.2. CAN transmit node performs unwanted automatic calibration

## Description & impact

When the delay (from TX to RX readback + 2 * CK_CAN) exceeds a Tq time, CAN wil automatically perform calibration, which results in transmitted dominant level extension and errors. 

## Workarounds

Use the GD32 MCU CAN transmission software solution, referring to “AN222 GD32A5x3 software evasion of CAN bit time problem”. 

## 2.15.3. The CAN peripheral cannot function without using HXTAL

## Description & impact

The CAN peripheral cannot work when the HXTAL clock is not enabled. 

## Workarounds

Turn on the HXTAL clock and wait for HXTAL clock stabilization before configuring the CAN peripheral clock source, then you can shut down the HXTAL clock as needed. 

## 2.15.4. CAN RAM area may be tampered in receiving mailbox processing

## Description & impact

If the global mailbox unlocking operation is not performed in the receiving mailbox processing routine (due to incorrect operation in the software), there is a certain probability that the CAN RAM area will be tampered, which will cause data transmission and reception exceptions. 

## Workarounds

Wait for the sending completion flag in CAN_STAT register to be set instead of judging by the CODE segment value of the sent mailbox before every data transmission. The reference code 

is as follow: 

```c
Flagstatus can_tx_status = RESET;
{
    if((RESET == can_tx_state) || (SET == can_flag_get(CAN1, CAN_FLAG_MB1))){
    can_tx_state = SET;
    can_flag_clear(CAN1, CAN_FLAG_MB1);
    /* transmit message */
    can_mailbox_config(CAN1, 1, &transmit_message);
    /* user code */
    }
} 
```

## 2.15.5. After Bus off recovery, transmit error count is not cleared automatically

## Description & impact

After Bus off recovery, transmit error count (TECNT) is not cleared automatically by hardware. 

## Workarounds

After Bus off recovery, using software method to clear the transmit error count (TECNT). Taking CAN1 as an example, the reference code is as follow. 

```c
/* bus off recovery flag is set */
if(RESET != can_flag_get(CAN1, CAN_FLAG_BUSOFF_RECOVERY))
{
    /* enter inactive mode */
    can_operation_mode_enter(CAN1, CAN_INACTIVE_MODE);
    /* clear transmit error count */
    CAN_ERR0(CAN1) &= ~(CAN_ERR0_TECNT);
    /* enter normal mode */
    can_operation_mode_enter(CAN1, CAN_NORMAL_MODE);
    can_flag_clear(CAN1, CAN_FLAG_BUSOFF_RECOVERY);
} 
```

## 2.15.6. The mailbox data is not read in time may result in incorrect data reading for the current and next frames

## Description & impact

When handling mailbox receive, if a new CAN frame (the next frame) is moved into the receive mailbox while reading this receive mailbox data (the current frame), it may lead to incorrect reading of the current frame and the next frame data. 

Note: Only the current frame and the next frame are affected. 

## Workarounds

Use one of the following solutions: 

1) Use mailbox reception interrupt and configure it to highest priority. When a receive mailbox interrupt occurs, promptly read and process the mailbox data (before the end of the next frame). 

2) Use CAN FIFO reception instead of mailbox reception. 

3) Enable the mailbox queue by setting the RPFQEN bit and set the mailbox reception interrupt to the highest priority. 

## 2.15.7. When the CAN operating clock frequency is less than CK_APB2 and an error occurs in DLC segment, which will lead to receiving an incorrect frame ID

## Description & impact

When the CAN operating clock frequency is less than CK_APB2, if external interference on the CAN bus causes an error frame to be sent due to an error detected in the DLC segment while receiving a frame, this will result in the subsequent frame receiving the error frame ID (even if this error frame ID is filtered by the CAN filter). 

## Workarounds

Use one of the following solutions: 

1) The software configures CAN clock source as CK_APB2. Taking CAN1 as an example, the reference code is as follow: 

```c
{
    /* configure the CAN1 clock source as CK_APB2 */
    rcu_can_clock_config(IDX_CAN1, RCU_CANSRC_APB2);
} 
```

2) Software checks the frame ID (applicable when the CAN operating clock frequency is less than CK_APB2). When the CAN mailbox receives a non-target frame ID and an error occurs, the software needs to reconfigure the CAN reception mailbox parameters. The specific configuration steps are as follows: 

a) Enter inactive mode 

b) Reconfigure the reception mailbox parameters 

c) Enter normal mode 

## 2.16. USBHS

## 2.16.1. USBHS OTG sensitivity problem

## Description & impact

USBHS OTG can function normally but fails to pass the sensitivity test. 

## Workarounds

Configure the USBHS internal corresponding reserved register to avoid the issue. 

## 2.17. Core

About Cortex-M7 limitations, please refer to “Cortex-M7 (AT610) and Cortex-M7 with FPU (AT611) Software Developer Errata Notice”. This document can be downloaded on ARM official wbesite. 

## 3. Revision history


Table 3-1. Revision history


<table><tr><td>Revision No.</td><td>Description</td><td>Date</td></tr><tr><td>1.0</td><td>Initial Release</td><td>Sep.12 2023</td></tr><tr><td>1.1</td><td>Update descriptions of contents</td><td>Sep.26 2023</td></tr><tr><td>1.2</td><td>Add limitations of Rev. Code C.Add USART / OSPI / EXMC peripherals limitations.</td><td>Apr.20 2024</td></tr><tr><td>1.3</td><td>Update description and workarounds of EXMC, refer toAuto refresh function of SDRAM controller is influenced by other EXMC controller.Add limitations, refer toTIMER is at risk of triggering an interrupt by mistake.Add limitations, refer toCAN RAM area may be tampered in receiving mailbox processing.Update workarounds of CAN, refer toAs a transmitting node, CAN executes unexpected self-calibration function.</td><td>Aug.5 2024</td></tr><tr><td>1.4</td><td>Update the description of PMU limitation, refer toChip damage risk in SMPS mode of the LQFP packageandVDDSMPS cannot be connected to a low level when not using SMPSUpdate the description of TIMER limitation, refer toTIMER interrupt is at risk of triggering by mistake</td><td>Sep.1 2024</td></tr><tr><td>1.5</td><td>Add limitations of CAN, refer toAfter Bus off recovery, transmit error count is not cleared automatically.Add limitations of CAN, refer toThe mailbox data is not read in time may result in incorrect data reading for the current and next frames.Add limitations of CAN, refer toWhen the CAN operating clock frequency is less than CK APB2 and an error occurs in DLC segment, which will lead to receiving an incorrect frame ID</td><td>Dec.15 2024</td></tr><tr><td>1.6</td><td>Add limitations of GPIO, refer toAfter VDD andVDDA are powered off, if voltage continues to be injected into GPIO (except for PA9 / PA10 / PB12 / PB13), it may lead to an overcurrent risk in the chip's GPIO</td><td>Jan.13 2025</td></tr><tr><td>1.7</td><td>1) Add limitations of I2S, refer toWhen I2S1 is used for communication and the GPIO and I2S1 configurations are in a special combination, it will probabilistically cause the I2S1 CK and I2S1 WS pins to continuously output signals2) Add limitations of SYSTEM, refer toWhen the system operates at high frequency and both the interrupt vector table and interrupt handling code are placed in ITCM, high-frequency interrupts may probabilistically cause false ITCM ECC error alarm3) Add limitations notice of Core</td><td>Nov.15 2025</td></tr></table>

## Important Notice

This document is the property of GigaDevice Semiconductor Inc. and its subsidiaries (the "Company"). This document, including any product of the Company described in this document (the “Product”), is owned by the Company according to the laws of the People’s Republic of China and other applicable laws. The Company reserves all rights under such laws and no Intellectual Property Rights are transferred (either wholly or partially) or licensed by the Company (either expressly or impliedly) herein. The names and brands of third party referred thereto (if any) are the property of their respective owner and referred to for identification purposes only. 

To the maximum extent permitted by applicable law, the Company makes no representations or warranties of any kind, express or implied, with regard to the merchantability and the fitness for a particular purpose of the Product, nor does the Company assume any liability arising out of the application or use of any Product. Any information provided in this document is provided only for reference purposes. It is the sole responsibility of the user of this document to determine whether the Product is suitable and fit for its applications and products planned, and properly design, program, and test the functionality and safety of its applications and products planned using the Product. The Product is designed, developed, and/or manufactured for ordinary business, industrial, personal, and/or household applications only, and the Product is not designed or intended for use in (i) safety critical applications such as weapons systems, nuclear facilities, atomic energy controller, combustion controller, aeronautic or aerospace applications, traffic signal instruments, pollution control or hazardous substance management; (ii) life-support systems, other medical equipment or systems (including life support equipment and surgical implants); (iii) automotive applications or environments, including but not limited to applications for active and passive safety of automobiles (regardless of front market or aftermarket), fo example, EPS, braking, ADAS (camera/fusion), EMS, TCU, BMS, BSG, TPMS, Airbag, Suspension, DMS, ICMS, Domain, ESC, DCDC, e-clutch, advanced-lighting, etc.. Automobile herein means a vehicle propelled by a selfcontained motor, engine or the like, such as, without limitation, cars, trucks, motorcycles, electric cars, and other transportation devices; and/or (iv) other uses where the failure of the device or the Product can reasonably be expected to result in personal injury, death, or severe property or environmental damage (collectively "Unintended Uses"). Customers shall take any and all actions to ensure the Product meets the applicable laws and regulations. The Company is not liable for, in whole or in part, and customers shall hereby release the Company as well as its suppliers and/or distributors from, any claim, damage, or other liability arising from or related to all Unintended Uses of the Product. Customers shall indemnify and hold the Company, and its officers, employees, subsidiaries, affiliates as well as its suppliers and/or distributors harmless from and against all claims, costs, damages, and other liabilities, including claims for personal injury or death, arising from or related to any Unintended Uses of the Product. 

Information in this document is provided solely in connection with the Product. The Company reserves the right to make changes, corrections, modifications or improvements to this document and the Product described herein at any time without notice. The Company shall have no responsibility whatsoever for conflicts or incompatibilities arising from future changes to them. Information in this document supersedes and replaces information previously supplied in any prior versions of this document. 
