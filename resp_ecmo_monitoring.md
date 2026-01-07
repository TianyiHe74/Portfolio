---
title: Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)
---

# Connected Medical Devices — Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)

## TL;DR
I contributed to firmware and tooling for sensor-based respiratory/ECMO monitoring prototypes, focusing on **deterministic sampling**, **low-latency streaming**, and **bench validation** against reference instrumentation.

> **Code:** (private / available upon request)  
> **Demo:** (add link if available)

---

## System overview
- **MCU:** PSoC 5 (sensor acquisition + timing-critical firmware)
- **Gateway / host:** Raspberry Pi (stream ingest + logging + analysis)
- **Links:** USBUART/UART; redesigned protocol to reduce overhead and improve latency

**Architecture (recommended)**
- Sensors → PSoC timer-driven sampling → binary packetization → USBUART → Pi logging/analysis

---

## What I did
- Reworked firmware toward **timer-driven, deterministic sampling** (reduce jitter vs ad-hoc loops)
- Implemented / integrated a **binary protocol** (replacing ASCII) to reduce transmission overhead and improve parsing robustness
- Wrote **Python tooling** to capture, parse, and validate data against reference measurements (e.g., TSI 4040)
- Ran extended **benchtop collection** sessions and documented procedures/results for iteration

---

## Validation & test setup
- Bench validation against a reference instrument (**TSI 4040**) across multiple parameter settings
- Built a repeatable test setup (including hardware actuation to simulate breathing patterns)

---

## Highlights (fill in numbers if you have them)
- Sampling rate: **__ Hz**
- Packet format: **__ bytes / sample**, with framing + checksum
- Latency improvement: **__ ms** (ASCII → binary)
- Long-run test duration: **20+ hours** benchtop collection (from project notes)

---

## Next steps
- Add automated regression checks for sensor calibration drift
- Add fault injection tests for dropped packets / reconnect behavior
- Expand documentation for reproducibility and handoff

---

_Last updated: 2026-01-07_
