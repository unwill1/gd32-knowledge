GigaDevice Semiconductor Inc. 

Device Limitations of GD32F527 

Errata Sheet 

## Table of Contents

Table of Contents .... 2
List of Figures .... 3
List of Tables .... 4
1. Introduction .... 5
1.1. Revision identification .... 5
1.2. Summary of device limitations .... 5
2. Descriptions of device limitations .... 7
2.1. System .... 7
2.1.1. A Flash ECC error is triggered after the MCU is powered on.... 7
2.1.2. The BOOT0 / BOOT1 pin level is being sampled all the time instead of being sampled only once.... 7
2.2. DBG .... 7
2.2.1. When the STB_HOLD bit in the DBG_CTL0 register is set, exception occurs to the MCU after it enters the debug standby mode.... 7
2.2.2. When the DSLP_HOLD bit in the DBG_CTL0 register is set, exception occurs to the MCU after it enters the debug deep-sleep mode.... 8
2.3. I2C .... 8
2.3.1. When SDA line interference causes garbled data on the I2C bus, it can lead to a stuck in the I2C slave device.... 8
2.4. I2S .... 9
2.4.1. I2S1 / I2S2 has a data transfer error when the audio sampling frequency is 192K.... 9
2.5. Core .... 9
2.5.1. Access permission faults are prioritized over unaligned Device memory faults.... 9
3. Revision history .... 11 

## List of Figures

Figure 1-1. Device revision code of GD32F527 5 

## List of Tables

Table 1-1. Applicable products .... 5
Table 1-2. Device limitations .... 5
Table 3-1. Revision history .... 11 

## 1. Introduction

This document applies to GD32F527 product series, as shown in Table 1-1. Applicable products. It offers technical guidance for using GD32MCU and provides workaround to current device limitations. 


Table 1-1. Applicable products


<table><tr><td>Type</td><td>Part Numbers</td></tr><tr><td>MCU</td><td>GD32F527xx series</td></tr></table>

## 1.1. Revision identification

The device revision can be identified according to the mark on the top of the package. The 1st code on Line 3 of the mark is the product revision code, as shown in Figure 1-1. Device revision code of GD32F527. 


Figure 1-1. Device revision code of GD32F527


<table><tr><td>GD32F527</td></tr><tr><td>IMT7</td></tr><tr><td>A123456</td></tr><tr><td>AC2228</td></tr><tr><td>GigaDevice</td></tr><tr><td>ARM</td></tr></table>

## 1.2. Summary of device limitations

The device limitations of GD32F527 are shown in Table 1-2. Device limitations, please refer to Section 2 for more details. 


Table 1-2. Device limitations


<table><tr><td rowspan="2">Module</td><td rowspan="2">Limitations</td><td>Workaround</td></tr><tr><td>Rev. Code A</td></tr><tr><td rowspan="2">System</td><td>A Flash ECC error is triggered after the MCU is powered on</td><td>Y</td></tr><tr><td>The BOOT0 / BOOT1 pin level is being sampled all the time instead of being sampled only once</td><td>Y</td></tr><tr><td rowspan="2">DBG</td><td>When the STB_HOLD bit in the DBG_CTL0 register is set, exception occurs to the MCU after it enters the debug standby mode</td><td>Y</td></tr><tr><td>When the DSLP_HOLD bit in the DBG_CTL0 register is set, exception occurs to the MCU after it enters the debug deep-sleep mode</td><td>Y</td></tr><tr><td>I2C</td><td>When SDA line interference causes garbled data on the I2C bus, it can lead to a stuck in the I2C slave device</td><td>N</td></tr><tr><td>I2S</td><td>I2S1 / I2S2 has a data transfer error when the audio sampling frequency is 192K</td><td>N</td></tr><tr><td>Core</td><td>Access permission faults are prioritized over unaligned Device memory faults</td><td>N</td></tr></table>

## Note:

Y = Limitation present, workaround available 

N = Limitation present, no workaround available 

'--' = Limitation fixed 

## 2. Descriptions of device limitations

## 2.1. System

## 2.1.1. A Flash ECC error is triggered after the MCU is powered on

## Description & impact

A Flash ECC error is triggered after the MCU is powered on. The phenomenon is that the ECCEADDR6 bit field value in the SYSCFG_FLASHECC_ADDR register is updated to 0x04, while the ECCMEIF6 bit field value in the SYSCFG_STAT register is still 0 and the corresponding ECC error interrupt is not occured. 

## Workarounds

The software can circumvent this problem by ignoring the Flash ECC address (0x04) triggered after power-on. 

## 2.1.2. The BOOT0 / BOOT1 pin level is being sampled all the time instead of being sampled only once

## Description & impact

After the system is powered on, the BOOT0/BOOT1 pin level is being sampled all the time instead of being sampled only once. 

## Workarounds

The software should use the logical address of each area rather than the area whose logical address starts from 0x00000000. The software can fix the system boot mode by configuring the NBTSB and BTFOSEL bit fields in the EFUSE_CTL register. At this time, the level status of the BOOT0 and BOOT1 pins is ignored. 

## 2.2. DBG

## 2.2.1. When the STB_HOLD bit in the DBG_CTL0 register is set, exception occurs to the MCU after it enters the debug standby mode

## Description & impact

When the STB_HOLD bit in the DBG_CTL0 register is set, if the system clock source is set to CK_PLLP, the MCU cannot be woken up after entering the debug standby mode and debugging operations cannot be performed. If the system clock source is set to CK_HXTAL or CK_IRC16M, the MCU cannot be woken up after entering the debug standby mode but debugging operations can still be performed. 

## Workarounds

When the STB_HOLD bit is set to enable low power debugging, switch the system clock to CK_IRC16M or CK_HXTAL before entering the debug standby mode. 

## 2.2.2. When the DSLP_HOLD bit in the DBG_CTL0 register is set, exception

## occurs to the MCU after it enters the debug deep-sleep mode

## Description & impact

When the DSLP_HOLD bit in the DBG_CTL0 register is set, if the system clock source is set to CK_PLLP, the MCU cannot be woken up after entering the debug deep-sleep mode and debugging operations cannot be performed. However, if the system clock source is set to CK_HXTAL or CK_IRC16M, the MCU can be woken up by non-EXTI interrupts such as systick after entering the debug deep-sleep mode and debugging operations can be performed. 

## Workarounds

When the DSLP_HOLD bit is set to enable low power debugging, switch the system clock to CK_IRC16M or CK_HXTAL and disable all interrupts except for EXTI before entering the debug deep-sleep mode. 

## 2.3. I2C

## 2.3.1. When SDA line interference causes garbled data on the I2C bus, it can

## lead to a stuck in the I2C slave device

## Description & impact

When I2C operates as a slave and is configured in 7-bit addressing mode, if the I2C slave device matches 10-bit address header during the I2C slave addressing phase and interference on the SCL / SDA line that causes the next RESTART signal to be sent early (the 9th SCL clock for sending the ACK was not sent), and then the slave matches the 7-bit address, which can result in the I2C slave pulling the SDA line low, ultimately leading to the I2C slave stuck. 

When I2C operates as a slave and is configured in 10-bit addressing mode, and if there is a mismatch in the 10-bit address header or the lower 8 bits of the 10-bit address during the I2C slave addressing phase, interference on the SCL / SDA line that causes the next RESTART / STOP signal to be sent early can result in the I2C slave pulling the SDA line low, ultimately 

leading to the I2C slave stuck. 

Note: This limitation applies to I2C3/ I2C4 / I2C5. 

Workarounds 

Not available. 

## 2.4. I2S

## 2.4.1. I2S1 / I2S2 has a data transfer error when the audio sampling frequency is 192K

Description & impact 

I2S1 / I2S2 has a data transfer error when the audio sampling frequency is 192K. 

Workarounds 

Not available. When using I2S1 / I2S2, set the audio sampling frequency to a value between 8 KHz and 96 KHz. 

## 2.5. Core

## 2.5.1. Access permission faults are prioritized over unaligned Device memory faults

This limitation refers to Arm ID number 1080541 in “Cortex-M33 AT623 and Cortex-M33 with FPU AT624 Software Developer Errata Notice”. 

## Description & impact

A load or store which causes an unaligned access to Device memory will result in an UNALIGNED UsageFault exception. However, if the region is not accessible because of the MPU access permissions (as specified in MPU_RBAR.AP), then the resulting MemManage fault will be prioritized over the UsageFault. 

This erratum affects all configurations of the Cortex-M33 processor with the MPU enabled. 

The failure occurring conditions are as follows: 

The MPU is enabled and: 

 A load/store access occurs to an address which is not aligned to the data type specified in the instruction. 

<sup></sup> The memory access hits one region only. 

<sup></sup> The region attributes (specified in the MAIR register) mark the location as Device memory. 

The region access permissions prevent the access (that is, unprivileged or write not allowed). 

The implications of this limitation is that the MemManage fault caused by the access permission violation will be prioritized over the UNALIGNED UsageFault exception because of the memory attributes. 

## Workarounds

Not available. However, it is expected that no existing software is relying on this behavior since it was permitted in Armv7-M.(The CM33 is Armv8-M). 

## 3. Revision history


Table 3-1. Revision history


<table><tr><td>Revision No.</td><td>Description</td><td>Date</td></tr><tr><td>1.0</td><td>Initial Release</td><td>Jan.23, 2024</td></tr><tr><td>1.1</td><td>Update the description of System limitation, refer toA Flash ECC error is triggered after the MCU is powered onUpdate the Workarounds of DBG limitation, refer toWhen the STB HOLD bit in the DBG CTL0 register is set, exception occurs to the MCU after it enters the debug standby mode andWhen the DSLP HOLD bit in the DBG CTL0 register is set, exception occurs to the MCU after it enters the debug deep-sleep modeUpdate the description of I2C limitation, refer toWhen SDA line interference causes garbled data on the I2C bus, it can lead to a stuck in the I2C slave device</td><td>Sep.1 2024</td></tr></table>

## Important Notice

This document is the property of GigaDevice Semiconductor Inc. and its subsidiaries (the "Company"). This document, including any product of the Company described in this document (the “Product”), is owned by the Company under the intellectual property laws and treaties of the People’s Republic of China and other jurisdictions worldwide. The Company reserves all rights under such laws and treaties and does not grant any license under its patents, copyrights, trademarks, or other intellectual property rights. The names and brands of third party referred thereto (if any) are the property of their respective owner and referred to for identification purposes only. 

The Company makes no warranty of any kind, express or implied, with regard to this document or any Product, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The Company does not assume any liability arising out of the application or use of any Product described in this document. Any information provided in this document is provided only for reference purposes. It is the responsibility of the user of this document to properly design, program, and test the functionality and safety of any application made of this information and any resulting product. Except for customized products which has been expressly identified in the applicable agreement, the Products are designed, developed, and/or manufactured for ordinary business, industrial, personal, and/or household applications only. The Products are not designed, intended, or authorized for use as components in systems designed or intended for the operation of weapons, weapons systems, nuclear installations, atomic energy control instruments, combustion control instruments, airplane or spaceship instruments, transportation instruments, traffic signal instruments, life-support devices or systems, other medical devices or systems (including resuscitation equipment and surgical implants), pollution control or hazardous substances management, or other uses where the failure of the device or Product could cause personal injury, death, property or environmental damage ("Unintended Uses"). Customers shall take any and all actions to ensure using and sellin the Products in accordance with the applicable laws and regulations. The Company is not liable, in whole or in part, and customers shall and hereby do release the Company as well as its suppliers and/or distributors from any claim, damage, or other liability arising from or related to all Unintended Uses of the Products. Customers shall indemnify and hold the Company as well as its suppliers and/or distributors harmless from and against all claims, costs, damages, and other liabilities, including claims for personal injury or death, arising from or related to any Unintended Uses of the Products. 

Information in this document is provided solely in connection with the Products. The Company reserves the right to make changes, corrections, modifications or improvements to this document and Products and services described herein at any time, without notice. 