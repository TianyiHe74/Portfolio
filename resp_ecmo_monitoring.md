---
title: Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)
---

# Connected Medical Devices — Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)

## TL;DR
I developed firmware and test infrastructure for respiratory/ECMO monitoring prototypes using **PSoC 5 + Raspberry Pi**, focusing on **deterministic sampling**, **low‑latency data streaming**, and **benchtop validation** against reference instrumentation (e.g., **TSI 4040**). I also integrated and debugged a **Transonic OEM flow sensor** over UART to support data streaming for a sheep ECMO study.

> **Demo / logs:** (add link if shareable)  
> **Code:** (add repo link, if shareable)

---

## Context
Work performed with the **CMU Biorobotics Lab** in a pre-clinical research setting.  
(If any part is not public, keep code private and publish only high-level architecture + results.)

---

## System overview
- **MCU:** PSoC 5
- **Companion compute:** Raspberry Pi (embedded Linux)
- **Sensors:** gas-flow + pressure/flow components (add part numbers if you can share)
- **Comms:** USBUART, UART

**Suggested images**
- System block diagram: `assets/resp_ecmo/block_diagram.png`
- Test setup photo: `assets/resp_ecmo/testbench.jpg`

---

## Firmware work (PSoC 5)
- Refactored firmware to **timer-driven sampling** to improve determinism.
- Designed a **binary USBUART protocol** (replacing ASCII) to reduce payload overhead and latency.
- Implemented robust acquisition loop and basic validation/error handling (add details).

**Key metrics (fill in)**
- Sampling rate: **__ Hz**
- Typical packet size (ASCII → binary): **__ → __ bytes**
- End-to-end latency improvement: **__%** or **__ ms**
- Sampling jitter (before/after): **__ → __**

---

## Raspberry Pi + tooling
- Wrote **Python tooling** for data capture/parsing and validation workflows.
- Automated comparison of sensor outputs vs **TSI 4040** across multiple operating points.

**Validation notes (fill in)**
- Total benchtop validation time: **20+ hours** (already stated on resume)
- Operating points tested: (flow ranges / conditions)
- Primary error metric: (MAE, percent error, correlation, etc.)

---

## Sensor integration
- Integrated and debugged **Transonic OEM flow sensor** over UART.
- Supported setup and reliable data streaming for a sheep ECMO study (details as permitted).

---

## Next steps
- Expanded automated test plan (fault injection, disconnects, drift checks).
- Timestamping + clock sync between MCU/RPi (if needed).
- Structured experiment logs and reproducible calibration pipeline.

---

## Resume bullets (for reference)
- Firmware + test infrastructure for respiratory/ECMO monitoring (PSoC 5 & Raspberry Pi).
- 20+ hours benchtop validation; Python tooling; cross-validation vs TSI 4040.
- Timer-driven sampling + binary USBUART protocol to reduce overhead/latency.
- Transonic OEM flow sensor integration over UART; supported sheep ECMO study streaming.
