---
title: EMG Sign‑Language Glove (ESP32)
---

# Assistive Wearable Biosignal ML — EMG Sign‑Language Glove (ESP32)

## TL;DR
I built an ESP32-based wearable that acquires **EMG** plus **9‑axis motion** (IMU + magnetometer), and runs **on‑device sign-language classification** in **embedded C**. I used **Edge Impulse** to create an end‑to‑end embedded ML workflow for dataset collection, training, evaluation, and deployment. Recently, I **integrated a magnetometer** and **eliminated flex sensors**, and I am expanding from single words toward **more words and phrase-level decoding**.

> **Demo:** (add link)  
> **Code:** (add repo link)

---

## Problem / motivation
Wearable assistive interfaces need:
- low-latency inference on-device (privacy + usability),
- robust sensing (biosignal variability + motion),
- repeatable data collection and calibration.

This project is a practical platform to iterate on those constraints.

---

## Hardware & sensing
- **MCU:** ESP32 (Xtensa)
- **Signals:**
  - **EMG** via ADC (front-end: (add your sensor/amp board))
  - **IMU + magnetometer** via I²C (add part number)
- **Power & packaging:** (add battery / enclosure notes if applicable)

**Images**
- Device photo: `assets/glove/device.jpg`
- Wiring / block diagram: `assets/glove/block_diagram.png`

---

## Firmware & real-time pipeline
- Implemented sensor acquisition and pre-processing in **C**.
- Streamed and labeled training data reliably for model development.
- Integrated on-device inference outputs into an application loop (add how you display/output results).

**Key parameters (fill in)**
- Sampling rate: **__ Hz**
- Window length: **__ ms** ( __ samples )
- Overlap / stride: **__**
- End-to-end latency (sensor → prediction): **__ ms**

---

## ML workflow (Edge Impulse)
- Built an end-to-end pipeline:
  1. data capture & labeling,
  2. feature extraction (or raw windows),
  3. model training & evaluation,
  4. deployment to ESP32.

**Dataset / evaluation (fill in)**
- #classes: **__**
- total labeled windows: **__**
- accuracy: **__**
- confusion matrix: `assets/glove/confusion_matrix.png`

---

## What I improved recently
- Added **magnetometer** to improve orientation/heading information.
- Removed **flex sensors** to simplify hardware and focus on EMG + inertial sensing.
- Expanded training to cover **more words** and started **phrase-level decoding** experiments.

---

## Next steps
- Session-to-session robustness: normalization, calibration routines, and domain adaptation.
- Better temporal decoding for phrases: HMM/CTC-style decoding or sequence models (if justified by data).
- Quantify latency/jitter under different sampling/communication configurations.

---

## Resume bullets (for reference)
- ESP32 wearable acquiring EMG + motion sensors; on-device classification in C.
- Edge Impulse pipeline; expanding vocabulary and prototyping phrase-level decoding.
- Calibration + documented collection protocol to improve repeatability.
