---
title: Tianyi He
description: Embedded firmware, hardware bring-up, and sensor systems
---

I am an M.S. student in Electrical and Computer Engineering at Carnegie Mellon, with expected program completion in **May 2027**. I work mainly in **C**, with Python for testing and data collection. My projects span MCU firmware, real-time scheduling, PCB bring-up, and sensor integration.

I like working on problems where building a useful physical system can make a real difference. These pages explain what I contributed, how I tested it, and what still needs work.

[Email](mailto:hetianyi74@gmail.com) · [LinkedIn](https://www.linkedin.com/in/tianyi-he-144809217/) · [GitHub](https://github.com/TianyiHe74)

## Selected projects

### [Medical-gas pipeline monitoring](esab.html)

**Sensor systems · Requirements and design · Hardware testing**

Research work with CMU's Biorobotics Lab and ESAB. I contribute to embedded firmware, sensor evaluation, board design, and a testbed for medical-gas monitoring. This page is a high-level summary; project code, designs, and data are confidential.

### [TeleLine: gas-flow sensing and data acquisition](resp_ecmo_monitoring.html)

**C · PSoC 5LP · USB serial · Python · Bench testing**

I replaced firmware delay loops with hardware timers, implemented binary telemetry, and built logging and test tools. The case study connects the sampling changes to timing checks and more than 20 hours of reference-instrument testing.

### [STM32 firmware, PCB bring-up, and FreeRTOS motor control](stm32_freertos.html)

**C · Device drivers · PCB layout · FreeRTOS · PWM and encoders**

I captured the course-provided schematic, designed the PCB layout, assembled and debugged the board, and wrote bare-metal and RTOS firmware. The motor-control example includes the task structure, control parameters, and remaining improvements.

### [Embedded Linux and real-time scheduling](embedded_real_time_systems.html)

**C · Linux kernel modules · System calls · trace-cmd and KernelShark**

I built applications and kernel components on Raspberry Pi 4 for periodic-task monitoring and scheduling experiments, then examined execution traces. The page describes the implementation and the limits of the available timing evidence.

### [Gesture-classification glove](glove.html)

**C · ESP32-S3 · EMG and motion sensors · Edge Impulse**

A team prototype for recognizing a small set of gestures on the device. I contributed firmware, sensor integration, data collection, model training, and deployment. Demo results and later hardware revisions are described separately.

### [Environmental sensing for a home-health prototype](postpartum_health.html)

**Python · Raspberry Pi · Wi-Fi and HTTP · AWS DynamoDB**

Our team used decision matrices to compare controllers, sensors, and communication options. I worked on the environmental hardware and firmware, including a Pi receiver that combines sensor readings and writes timestamped records to DynamoDB. The page links the public implementation, matrices, and system diagrams.

## Technical focus

My strongest programming language is C; I also use Python and supporting C++. I work with STM32, PSoC, ESP32, and Raspberry Pi, and use oscilloscopes, logic analyzers, multimeters, and bench supplies to connect firmware behavior to what the hardware is actually doing.

For research and course projects, I share only the material permitted for public use. Team contributions are identified on each page.
