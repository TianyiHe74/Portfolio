---
title: Projects
---

# Tianyi He — Embedded Systems, Biosignal ML, Connected Devices

I build real-time embedded systems for sensing + signal processing, with experience in **wearable biosignals (EMG/IMU)**, **medical device prototyping**, and **IoT telemetry (MQTT + AWS)**.

- Email: hetianyi74@gmail.com  
- LinkedIn: linkedin.com/in/tianyi-he-144809217  
- GitHub: github.com/tianyi-he (add if you want)

---

## Projects

1) **Assistive Wearable Biosignal ML — EMG Sign‑Language Glove (ESP32)**  
**Focus:** real-time biosignal acquisition + embedded ML inference for wearable assistive tech.  
**Stack:** XIAO ESP32‑S3, Grove EMG Detector → ADS1115 (I²C), MPU‑9255 (accel/gyro), MMC5983MA magnetometer (I²C), embedded C, Edge Impulse.  
- [Project page](glove.html)

2) **Connected Medical Devices — Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)**  
**Focus:** deterministic acquisition + low-latency streaming + benchtop validation vs reference instrumentation.  
**Stack:** PSoC 5, Raspberry Pi, USBUART/UART, timer-driven sampling, binary protocol, Python tooling, validation vs TSI 4040.  
- [Project page](resp_ecmo_monitoring.html)

3) **IoT Health Monitoring — Postpartum Health Air‑Quality Node (Raspberry Pi 5 → Pico 2 W + AWS)**  
**Focus:** sensing + wireless edge node + cloud logging for a home-health monitoring scenario (non-clinical).  
**Stack:** Raspberry Pi 5, Pico 2 W, PM/CO₂ sensing, Wi‑Fi, MQTT, AWS DynamoDB.  
- [Project page](postpartum_health.html)

4) **STM32 + FreeRTOS Motor Control (18‑349 Lab 6)**  
**Focus:** real-time control loop + encoder ISR + RTOS task structure + interactive tuning (keypad/LCD).  
**Stack:** STM32 (Cortex‑M), C, FreeRTOS, EXTI (quadrature encoder), PWM timers (motor control), UART, keypad + LCD.  
- [Project page](stm32_freertos.html)
