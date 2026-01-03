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
Wearable assistive interfaces need low-latency on-device inference, robust sensing, and repeatable data collection despite biosignal variability.

---

## Hardware & sensing
- **MCU:** ESP32 (Xtensa)
- **Signals:**
  - **EMG** via ADC (front-end: (add your sensor/amp board))
  - **IMU + magnetometer** via I²C (add part number)
- **Packaging:** (add notes)

**Images**
- `assets/glove/device.jpg`
- `assets/glove/block_diagram.png`

---

## Firmware pipeline (embedded C)
- Sensor acquisition + basic pre-processing.
- Reliable streaming and labeling for dataset creation.
- On-device inference integration into the application loop.

**Key parameters (fill in)**
- Sampling rate: **__ Hz**
- Window length: **__ ms** ( __ samples )
- Overlap/stride: **__**
- End-to-end latency (sensor → prediction): **__ ms**

---

## ML workflow (Edge Impulse)
- Data capture & labeling → feature extraction (or raw windows) → model training & evaluation → deployment.

**Dataset / evaluation (fill in)**
- #classes: **__**
- total labeled windows: **__**
- accuracy: **__**
- confusion matrix: `assets/glove/confusion_matrix.png`

---

## Recent updates
- Added **magnetometer**; removed **flex sensors**.
- Training on more words and experimenting with phrase-level decoding.

---

## Next steps
- Session-to-session robustness (calibration, normalization).
- Sequence decoding for phrases (if justified by data).
- Quantify latency/jitter under different sampling settings.
