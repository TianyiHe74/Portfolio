---
title: Postpartum Health Air‑Quality Node (Raspberry Pi → Pico 2 W + AWS)
---

# IoT Health Monitoring — Postpartum Health Air‑Quality Node (Raspberry Pi 5 → Pico 2 W + AWS)

## TL;DR
I designed and implemented an embedded air‑quality sensing node to support a **postpartum home‑recovery** monitoring scenario. The system connects a **Raspberry Pi 5** to a **Pico 2 W** for sensor acquisition and wireless communication, then logs data to the cloud using **AWS DynamoDB** for later analysis/visualization.

> **Demo/dashboard:** (add link if you have one)  
> **Code:** (add repo link or “available on request”)

---

## What problem it addresses
Home recovery can benefit from passive monitoring of environmental factors (e.g., particulate matter, CO₂) that affect comfort and respiratory health. This project focused on building a reliable sensing + logging pipeline.

---

## System architecture
- **Edge compute:** Raspberry Pi 5
- **MCU node:** Pico 2 W (Wi‑Fi)
- **Sensors:** particulate matter + CO₂ (add part numbers)
- **Cloud:** AWS DynamoDB for time‑series logging (and optional downstream analysis)

**Suggested images**
- `assets/postpartum/block_diagram.png`
- `assets/postpartum/device.jpg`
- `assets/postpartum/sample_plot.png`

---

## Implementation details (fill in)
- Sensor sampling rate: **__ Hz**
- Data packet format: **__**
- Wireless link: **__** (Wi‑Fi protocol / message format)
- Cloud schema (DynamoDB): partition key **__**, sort key **__**, attributes **__**

**Reliability/latency (add one)**
- Uptime over a multi‑hour run: **__%**
- End-to-end ingestion latency: **__ ms** (edge → cloud)
- Data loss rate: **__%**

---

## Team / leadership
- Served as **team lead** for phase 3: coordinated integration, communicated updates, and tracked milestones.

---

## Why it’s relevant to neurotech/medical devices
- Real-time sensing + robust data collection
- Edge–cloud pipelines for health monitoring
- Practical engineering tradeoffs (latency, reliability, calibration)
