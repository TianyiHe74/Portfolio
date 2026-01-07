---
title: STM32 Bare‑Metal & FreeRTOS + Custom PCB Bring‑Up
---

# Intro to Embedded Systems — STM32 Bare‑Metal & FreeRTOS + Custom PCB Bring‑Up

## TL;DR
I built a bare-metal + FreeRTOS firmware stack on **STM32**, implemented multiple **peripheral drivers**, and brought up a **custom PCB** using lab instruments (scope/DMM/logic analyzer). The project emphasized reliable real-time behavior and hardware debugging.

> **Code:** (add link if public)  
> **Demo:** (add link if available)

---

## System overview
- **MCU:** STM32
- **RTOS:** FreeRTOS (task scheduling + synchronization)
- **Peripherals:** EXTI, timers/PWM, UART, I²C, ADC
- **Hardware:** custom PCB bring-up + wiring/measurement in lab

---

## What I built
- Driver layer for key peripherals (UART/I²C/ADC/timers/EXTI)
- FreeRTOS task structure (recommended to list 3–5 tasks):
  - sensor/task loop
  - UI/IO task (keypad/LCD)
  - control task (PWM/servo/motor)
  - comm/logging task (UART)
- ISR + task integration (interrupt-safe queues/semaphores)

---

## Bring-up & debugging
- Verified power rails and clocks, validated GPIO behavior
- Used scope/logic analyzer to debug protocol timing and ISR behavior
- Iterated PCB + firmware together to reach a stable demo

---

## Highlights (fill in numbers if you have them)
- Control loop rate: **__ Hz**
- Worst-case ISR latency / jitter: **__**
- PWM frequency/resolution: **__**

---

## Next steps
- Add automated hardware tests (loopback, self-test at boot)
- Improve documentation (pinout, block diagram, bring-up checklist)

---

_Last updated: 2026-01-07_
