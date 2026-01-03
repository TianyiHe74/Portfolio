---
title: STM32 Bare‑Metal & FreeRTOS (Drivers + PCB Bring‑Up)
---

# Intro to Embedded Systems — STM32 Bare‑Metal & FreeRTOS + Custom PCB Bring‑Up

## TL;DR
I built a firmware stack in **C** on **STM32** using both **bare-metal** and **FreeRTOS**, writing drivers for **EXTI, timers/PWM, UART, I²C, and ADC**. I integrated multiple peripherals (keypad, LCD, servo, encoder, DC motor) and performed **custom STM32 PCB bring-up** using lab instruments (bench supply, oscilloscope, DMM, logic analyzer).

> **Demo:** (add link)  
> **Code:** (add repo link)

---

## Hardware & peripherals
- STM32 MCU (model: __)
- Peripherals: keypad, LCD, servo, encoder, DC motor
- Interfaces: UART, I²C, ADC, timers/PWM, EXTI interrupts

**Suggested images**
- `assets/stm32/pcb.jpg`
- `assets/stm32/block_diagram.png`

---

## Firmware details
- Implemented drivers:
  - EXTI interrupt handling
  - Timer/PWM generation and capture
  - UART and I²C communication
  - ADC sampling and basic filtering (if applicable)
- Integrated FreeRTOS:
  - tasks + queues/semaphores (as applicable)
  - timing and scheduling structure

**Metrics (add one)**
- Control loop / update rate: **__ Hz**
- Worst-case ISR latency / jitter: **__**
- CPU utilization under full load: **__%**

---

## Bring-up & debugging
- Read schematics, assembled hardware, and debugged bring-up issues using standard lab equipment.
- Verified power rails, clocking, and peripheral IO; validated signal timing with scope/logic analyzer.
