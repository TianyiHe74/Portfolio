---
title: Postpartum Health Air‑Quality Node (Raspberry Pi → Pico 2 W + AWS)
---

# IoT Health Monitoring — Postpartum Health Air‑Quality Node (Raspberry Pi 5 → Pico 2 W + AWS)

## TL;DR
I worked on an environmental sensing substation for a **home health monitoring** concept (postpartum recovery scenario), focusing on **air‑quality telemetry + reliable cloud logging** rather than clinical claims. The air‑quality substation runs on a **Pico 2 W** and reports to a **Raspberry Pi 5 base station**, which forwards time‑stamped records to **AWS DynamoDB**.

> **Code:** https://github.com/CMU-RPCS-2025/Environmental_HW_FW  
> **Demo:** Not available — the hardware kit was returned at the end of the course, so I can’t record a new demo.

---

## System architecture (multi‑substation design)
The overall system is built around a **base station** that aggregates telemetry from multiple wireless “substations” (e.g., ambient conditions/air quality, medication adherence, camera modules) and forwards data to the cloud for storage/analysis.

![Architecture overview](assets/postpartum/architecture_overview.png)

**Base station responsibilities**
- Wireless onboarding/handshake for substations (Bluetooth/Wi‑Fi)
- Data aggregation + local buffering
- Cloud interface (MQTT → cloud storage)

**Substation template**
Each substation follows a common structure: **MCU + wireless + battery power + sensors**, enabling independent modules that can be deployed in multiple rooms.

---

## My focus: Ambient conditions / air quality
I contributed to the **environmental hardware/firmware** workstream and integration for the air‑quality subsystem.

Two environmental approaches were explored during the project:
- **PM-focused node:** particulate matter sensing with a dedicated PM sensor and Wi‑Fi uplink to the base station
- **Enviro+ node:** multi-sensor ambient telemetry (temperature/pressure/humidity/light/noise + gas channels) sent to the base station via Wi‑Fi

### Hardware (air‑quality substation)
- **Gateway / base station:** Raspberry Pi 5  
- **Substation MCU:** Raspberry Pi Pico 2 W  
- **Particulate matter:** **PMSA003I** air quality sensor  
- **Ambient conditions (alternate node):** **Enviro+** breakout

---

## Wireless + messaging protocol
We ran a lightweight trade study across common protocols:

![Wireless protocol trade study](assets/postpartum/wireless_protocol_matrix.png)

**Chosen approach:** Wi‑Fi + **MQTT** for simplicity and clean pub/sub integration with the base station.

---

## Cloud logging (AWS DynamoDB)
The base station forwards readings into DynamoDB as time-series records.

**Table:** `PMCO2_sensors`  
**Primary key design (time-series pattern)**
- **Partition key:** `device_id` (e.g., `raspi-pico-2w`)
- **Sort key:** `timestamp` (ISO 8601 / RFC 3339 string, e.g., `2025-04-18T23:21:22.456Z`)

**Stored measurements (example fields)**
- **CO₂:** `co2_ppm` (plus calibration/compensation fields such as `corrected_ppm`, `corrected_rzero`)
- **Particle counts (bins):** `p03`, `p05`, `p10`, `p25`, `p50`, `p100`
- **PM mass concentrations:** `pm10_std`, `pm25_std`, `pm100_std`, and `pm10_env`, `pm25_env`, `pm100_env`
- **Gas-sensor diagnostics (if present):** `resistance`, `rzero`
- Optional status/health fields: `status`

This schema makes it easy to query “all samples from one node over a time range” efficiently, while keeping each write operation small and append-only.

## Engineering work I contributed
- End-to-end sensing pipeline: sensor acquisition → packetization → wireless publish → base station ingest → cloud write
- Reliability-oriented integration: reconnect logic, buffering, and test runs for stability
- Late-phase coordination: interface agreements, tracking issues, and maintaining documentation

---

## Project artifacts (included in this repo)
These are included under `assets/postpartum/` so reviewers can inspect real engineering work.

### Procurement list (excerpt)
![Procurement list](assets/postpartum/procurement_list.png)

### Software libraries & drivers (excerpt)
![Software libraries](assets/postpartum/software_libraries.png)

### Environmental sensor trade study (excerpt)
![Air-quality sensor trade study](assets/postpartum/air_quality_sensor_matrix.png)

Design artifacts included in the repo: architecture diagrams, trade studies, procurement list, and software/library inventory.

---

_Last updated: 2026-01-07_
