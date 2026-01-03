---
title: Postpartum Health Air‑Quality Node (Raspberry Pi → Pico 2 W + AWS)
---

# IoT Health Monitoring — Postpartum Health Air‑Quality Node (Raspberry Pi 5 → Pico 2 W + AWS)

## TL;DR
I built an environmental sensing node for a **home health monitoring** concept (postpartum recovery scenario), focusing on **air-quality sensing + reliable data logging** rather than clinical claims. The system uses a **Pico 2 W** substation for sensor acquisition and a **Raspberry Pi 5** gateway that forwards readings to **AWS DynamoDB** for storage and downstream visualization.

> **Demo / dashboard:** 
> **Code:** https://github.com/CMU-RPCS-2025/Environmental_HW_FW

---

## System architecture
The overall project architecture supports multiple “substations” (e.g., air-quality, medication, camera), connected to a base station. This page focuses on the **air-quality subsystem**.

![Architecture overview](assets/postpartum/architecture_overview.png)

### Key decisions
- Use a small MCU node (**Pico 2 W**) for sensing and wireless networking.
- Use a gateway (**Raspberry Pi 5**) for aggregation + buffering + cloud write.
- Use **MQTT** for lightweight pub/sub messaging between nodes and gateway.

---

## Hardware & sensors (air-quality substation)
**Gateway / base station**
- **Raspberry Pi 5 (16GB)**

**Substation**
- **Raspberry Pi Pico 2 W**

**Sensors**
- **Particulate matter:** **PMSA003I** air quality sensor (PM2.5/PM10 sensor family)
- **Gas/VOC proxy:** **MQ-135** (broad gas sensor; useful as a low-cost proxy / trend signal)

> Note: we also evaluated alternative environmental sensor platforms (e.g., Enviro+), and iterated across versions during the project.

---

## Wireless + messaging protocol
We ran a lightweight trade study across common protocols.

![Wireless protocol trade study](assets/postpartum/wireless_protocol_matrix.png)

**Chosen approach:** Wi‑Fi + MQTT for simplicity and adequate bandwidth for multi-sensor telemetry.

---

## Cloud logging (AWS DynamoDB)
The gateway forwards readings into DynamoDB as time-series records.
- Designed a schema with a **node identifier** and **timestamp** as primary indexing keys (typical DynamoDB time-series pattern).
- Gateway buffers locally to reduce data loss during connectivity interruptions.

*(If you tell me your exact DynamoDB key names, I can write the schema precisely.)*

---

## Engineering work I contributed
- End-to-end pipeline: sensor acquisition → packetization → wireless publish → gateway ingest → cloud write.
- Reliability-oriented design: buffering, reconnect logic, and structured test runs.
- Integration support: interface agreements, test planning, and documentation updates.

---

## Design + implementation artifacts (included)
These are included under `assets/postpartum/` so readers can inspect the underlying engineering work.

### Diagrams (editable draw.io)
- `assets/postpartum/topology_mqtt.drawio` (base station + substations topology with MQTT)
- `assets/postpartum/pico_wiring_pm_mq135.drawio` (Pico ↔ PMSA003I ↔ MQ-135 wiring)
- `assets/postpartum/air_conditions_enviroplus.drawio` (earlier environmental subsystem version)

### Procurement list (excerpt)
![Procurement list](assets/postpartum/procurement_list.png)

### Software libraries & drivers (excerpt)
![Software libraries](assets/postpartum/software_libraries.png)

### Air-quality sensor trade study (excerpt)
![Air-quality sensor trade study](assets/postpartum/air_quality_sensor_matrix.png)

Raw spreadsheets:
- `assets/postpartum/design_matrices.xlsx`
- `assets/postpartum/software_libraries.xlsx`
- `assets/postpartum/procurement_list.xlsx`

---

## Next steps
- If true CO₂ accuracy is required, replace proxy sensing with an NDIR CO₂ sensor.
- Add automated calibration checks and periodic self-tests.
- Add dashboards for trend/threshold alerts (with appropriate disclaimers).

---

_Last updated: 2026-01-03_
