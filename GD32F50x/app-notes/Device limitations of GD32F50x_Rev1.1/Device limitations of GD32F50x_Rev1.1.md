GigaDevice Semiconductor Inc. 

Device limitations of GD32F50x 

Errata Sheet 

Revision 1.1 

(Nov. 2025) 

## Table of Contents

Table of Contents....2
List of Figures....3
List of Tables....4
1. Introduction....5
1.1. Revision identification....5
1.2. Summary of device limitations....5
2. Descriptions of device limitations....7
2.1. I2C....7
2.1.1. When the I2C slave is configured in 10-bit address mode, if the external master does not send a STOP signal after transmitting a frame of data, the I2C slave will be unable to match the slave address in subsequent operations....7
2.2. CAN....7
2.2.1. When TFO bit is set and mailbox 0/1/2 are enabled for simultaneous transmission, aborting the transmission of mailbox 2 will also abort mailbox 1....7
2.2.2. When TFO is cleared and the identifiers of transmission mailbox 1 or 2 are configured as 0x1FFFFFFF, the data in transmission mailbox 1 or 2 cannot be sent....8
2.3. Core....8
2.3.1. Access permission faults are prioritized over unaligned Device memory faults....8
3. Revision history....10 

## List of Figures

Figure 1-1. Device revision code of GD32F50x....5 

## List of Tables

Table 1-1. Applicable products....5
Table 1-2. Device limitations....5
Table 3-1. Revision history....10 

## 1. Introduction

This document applies to GD32F50x product series, as shown in Table 1-1. Applicable products. It offers technical guidance for using GD32 MCU and provides workaround to current device limitations. 


Table 1-1. Applicable products


<table><tr><td>Type</td><td>Part Numbers</td></tr><tr><td rowspan="2">MCU</td><td>GD32F503xx series</td></tr><tr><td>GD32F505xx series</td></tr></table>

## 1.1. Revision identification

The device revision can be identified according to the mark on the top of the package. The 1st code on Line 3 of the mark is the product revision code, as shown in Figure 1-1. Device revision code of GD32F50x. 


Figure 1-1. Device revision code of GD32F50x


<table><tr><td>GD32F505</td></tr><tr><td>VGT6</td></tr><tr><td>AXP0340</td></tr><tr><td>AC2527</td></tr><tr><td>GigaDevice</td></tr><tr><td>ARM</td></tr></table>

## 1.2. Summary of device limitations

The device limitations of GD32F50X are shown in Table 1-2. Device limitations, please refer to Section 2 for more details. 


Table 1-2. Device limitations


<table><tr><td rowspan="2">Module</td><td rowspan="2">Limitations</td><td>Workaround</td></tr><tr><td>Rev. Code A</td></tr><tr><td>I2C</td><td>When the I2C slave is configured in 10-bit address mode, if the external master does not send a STOP signal after transmitting a frame of data, the I2C slave will be unable to match the slave address in subsequent operations</td><td>Y</td></tr><tr><td rowspan="2">CAN</td><td>When TFO bit is set and mailbox 0/1/2 are enabled for simultaneous transmission, aborting the transmission of mailbox 2 will also abort mailbox 1</td><td>Y</td></tr><tr><td>When TFO is cleared and the identifiers of transmission mailbox 1 or 2 are configured as 0x1FFFFFFF, the data in transmission mailbox 1 or 2 cannot be sent</td><td>Y</td></tr><tr><td>Core</td><td>Access permission faults are prioritized over unaligned Device memory faults</td><td>N</td></tr></table>

Note: 

Y = Limitation present, workaround available 

N = Limitation present, no workaround available 

'--' = Limitation fixed 

## 2. Descriptions of device limitations

## 2.1. I2C

### 2.1.1. When the I2C slave is configured in 10-bit address mode, if the external master does not send a STOP signal after transmitting a frame of data, the I2C slave will be unable to match the slave address in subsequent operations

#### Description & impact

When the I2C slave is configured in 10-bit address mode, if the external master does not send a STOP signal after transmitting a frame of data and instead sends a START signal to initiate the transmission of a second frame, the I2C slave will misinterpret the second byte of the slave address (the lower 8 bits of the 10-bit address) as data, and the address match flag (ADDSEND) will not be set. For example, if the slave is in address polling mode, it will continuously wait for an address match and remain stuck in a loop. Similarly, if the slave is in interrupt or DMA mode, it will fail to process subsequent data due to the inability to match the slave address. 

#### Workarounds

When the I2C slave is operating in 10-bit address mode, the external I2C master must send the corresponding STOP signal at the end of each frame transmission. 

## 2.2. CAN

### 2.2.1. When TFO bit is set and mailbox 0/1/2 are enabled for simultaneous transmission, aborting the transmission of mailbox 2 will also abort mailbox 1

#### Description & impact

When TFO bit is set and mailbox 0/1/2 are enabled for simultaneous transmission, aborting the transmission of mailbox 2 will also abort mailbox 1, meaning the data in mailbox 1 will not be transmitted. 

#### Workarounds

Use one of the following solutions: 

1) Before aborting the transmission of mailbox 2, confirm whether mailbox 1 is in the pending state. 

2) After aborting the transmission of mailbox 2, reconfigure mailbox 1/2 for transmission and resend. 

### 2.2.2. When TFO is cleared and the identifiers of transmission mailbox 1 or 2 are configured as 0x1FFFFFFF, the data in transmission mailbox 1 or 2 cannot be sent

#### Description & impact

When TFO is cleared and the identifiers of transmission mailbox 1 or 2 are configured as 0x1FFFFFFF, the data in transmission mailbox 1 or 2 cannot be sent. For example, when TFO is set to 0 and the ID of transmission mailbox 1 is configured as 0x1FFFFFFF, the data in transmission mailbox 1 cannot be sent. 

#### Workarounds

Use one of the following solutions: 

1) When the identifier is 0x1FFFFFF, use transmission mailbox 0 for data frame transmission. 

2) Use first-in-first-out (FIFO) transmission order, i.e., set TFO = 1. 

## 2.3. Core

About Cortex-M33 limitations, please refer to “Cortex-M33 AT623 and Cortex-M33 with FPU AT624 Software Developer Errata Notice”. This document can be downloaded on ARM officia wbesite. 

### 2.3.1. Access permission faults are prioritized over unaligned Device memory faults

This limitation refers to Arm ID number 1080541 in “Cortex-M33 AT623 and Cortex-M33 with FPU AT624 Software Developer Errata Notice”. 

#### Description & impact

A load or store which causes an unaligned access to Device memory will result in an UNALIGNED UsageFault exception. However, if the region is not accessible because of the MPU access permissions (as specified in MPU_RBAR.AP), then the resulting MemManage fault will be prioritized over the UsageFault. 

This erratum affects all configurations of the Cortex-M33 processor with the MPU enabled. 

The failure occurring conditions are as follows: 

The MPU is enabled and: 

- A load/store access occurs to an address which is not aligned to the data type specified in the instruction.
- The memory access hits one region only.
- The region attributes (specified in the MAIR register) mark the location as Device memory.
- The region access permissions prevent the access (that is, unprivileged or write not allowed).

The implications of this limitation is that the MemManage fault caused by the access permission violation will be prioritized over the UNALIGNED UsageFault exception because of the memory attributes. 

#### Workarounds

Not available. However, it is expected that no existing software is relying on this behavior since it was permitted in Armv7-M.(The CM33 is Armv8-M). 

## 3. Revision history


Table 3-1. Revision history


<table><tr><td>Revision No.</td><td>Description</td><td>Date</td></tr><tr><td>1.0</td><td>Initial Release</td><td>Aug.8 2025</td></tr><tr><td>1.1</td><td>1. Add limitations of CAN, refer to When TFO bit is set and mailbox 0/1/2 are enabled for simultaneous transmission, aborting the transmission of mailbox 2 will also abort mailbox 1<br>2. Add limitations of CAN, refer to When TFO is cleared and the identifiers of transmission mailbox 1 or 2 are configured as 0x1FFFFFFF, the data in transmission mailbox 1 or 2 cannot be sent</td><td>Nov.5 2025</td></tr></table>

## Important Notice

This document is the property of GigaDevice Semiconductor Inc. and its subsidiaries (the "Company"). This document, including any product of the Company described in this document (the “Product”), is owned by the Company according to the laws of the People’s Republic of China and other applicable laws. The Company reserves all rights under such laws and no Intellectual Property Rights are transferred (either wholly or partially) or licensed by the Company (either expressly or impliedly) herein. The names and brands of third party referred thereto (if any) are the property of their respective owner and referred to for identification purposes only. 

To the maximum extent permitted by applicable law, the Company makes no representations or warranties of any kind, express or implied, with regard to the merchantability and the fitness for a particular purpose of the Product, nor does the Company assume any liability arising out of the application or use of any Product. Any information provided in this document is provided only for reference purposes. It is the sole responsibility of the user of this document to determine whether the Product is suitable and fit for its applications and products planned, and properly design, program, and test the functionality and safety of its applications and products planned using the Product. The Product is designed, developed, and/or manufactured for ordinary business, industrial, personal, and/or household applications only, and the Product is not designed or intended for use in (i) safety critical applications such as weapons systems, nuclear facilities, atomic energy controller, combustion controller, aeronautic or aerospace applications, traffic signal instruments, pollution control or hazardous substance management; (ii) life-support systems, other medical equipment or systems (including life support equipment and surgical implants); (iii) automotive applications or environments, including but not limited to applications for active and passive safety of automobiles (regardless of front market or aftermarket), for example, EPS, braking, ADAS (camera/fusion), EMS, TCU, BMS, BSG, TPMS, Airbag, Suspension, DMS, ICMS, Domain, ESC, DCDC, e-clutch, advanced-lighting, etc.. Automobile herein means a vehicle propelled by a selfcontained motor, engine or the like, such as, without limitation, cars, trucks, motorcycles, electric cars, and other transportation devices; and/or (iv) other uses where the failure of the device or the Product can reasonably be expected to result in personal injury, death, or severe property or environmental damage (collectively "Unintended Uses"). Customers shall take any and all actions to ensure the Product meets the applicable laws and regulations. The Company is not liable for, in whole or in part, and customers shall hereby release the Company as well as its suppliers and/o distributors from, any claim, damage, or other liability arising from or related to all Unintended Uses of the Product. Customers shall indemnify and hold the Company, and its officers, employees, subsidiaries, affiliates as well as its suppliers and/or distributors harmless from and against all claims, costs, damages, and other liabilities, including claims for personal injury or death, arising from or related to any Unintended Uses of the Product. 

Information in this document is provided solely in connection with the Product. The Company reserves the right to make changes, corrections, modifications or improvements to this document and the Product described herein at any time without notice. The Company shall have no responsibility whatsoever for conflicts or incompatibilities arising from future changes to them. Information in this document supersedes and replaces information previously supplied in any prior versions of this document. 
