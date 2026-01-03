---
title: Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)
---

# Connected Medical Devices — Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)

## TL;DR
I developed firmware and test infrastructure for respiratory/ECMO monitoring prototypes using **PSoC 5 + Raspberry Pi**, focusing on **deterministic sampling**, **low‑latency data streaming**, and **benchtop validation** against reference instrumentation (e.g., **TSI 4040**). I also integrated and debugged a **Transonic OEM flow sensor** over UART to support reliable data streaming.
 
> **Demo and Code:** Cannot share due to confidentiality

---

## System overview
- **MCU:** PSoC 5
- **Companion compute:** Raspberry Pi (embedded Linux)
- **Comms:** USBUART, UART
- **Validation:** compared outputs vs reference instrument (TSI 4040) across multiple operating points

---

## Firmware work (PSoC 5)
- Refactored to **timer-driven sampling** to improve determinism.
- Designed a **binary USBUART protocol** (replacing ASCII) to reduce overhead and transmission latency.
- Built reliable acquisition + error handling.

**Key metrics (fill in)**
- Sampling rate: **__ Hz**
- Packet size (ASCII → binary): **__ → __ bytes**
- End-to-end latency improvement: **__%** or **__ ms**
- Sampling jitter (before/after): **__ → __**

---

## Tooling + validation (Python)
- Wrote Python scripts to capture/parse logs and automate comparisons vs reference data.
- Ran **20+ hours** of benchtop collection and validation across multiple settings.

---

## Sensor integration
- Integrated and debugged **Transonic OEM flow sensor** over UART.
- Supported stable streaming for research use (details available upon request).
