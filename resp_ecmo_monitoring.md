---
title: Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)
---

# Connected Medical Devices — Respiratory & ECMO Monitoring (PSoC 5 + Raspberry Pi)

## TL;DR
I contributed firmware and tooling for sensor-based respiratory/ECMO monitoring prototypes, focusing on **deterministic sampling**, **low-latency streaming**, and **benchtop validation** against reference instrumentation.

- **Code/data:** Not public due to research lab confidentiality (available upon request).  
- **Demo:** Not available — the physical setup was in-lab and is no longer accessible to re-record.

---

## System overview
- **MCU:** PSoC 5 (timing-critical acquisition + protocol)
- **Host:** Raspberry Pi (ingest + logging + analysis)
- **Links:** USBUART/UART
- **Validation:** compared measurements against a reference instrument (**TSI 4040**) across multiple parameter settings

---

## What I did
- Reworked firmware toward **timer-driven, deterministic sampling** to reduce jitter and improve repeatability
- Designed and implemented a **binary communication protocol** (replacing ASCII) to reduce overhead and improve parsing robustness
- Built **Python tooling** to capture, parse, and validate data against reference measurements
- Supported repeatable bench experiments (including extended data collection runs) and documented results for iteration

---

## Engineering highlights
- Deterministic acquisition path from sensor sampling → packetization → USBUART streaming → Pi-side logging
- Validation mindset: **capture, parse, compare**, and iterate until measurements match reference behavior
- Practical instrumentation: oscilloscope/DMM measurements used during debugging and validation

---

## What I can discuss in interviews
Even though the repo is not public, I can walk through:
- protocol framing choices and error handling
- sampling architecture and timing tradeoffs
- validation methodology vs reference instrumentation
- how I structured parsing + logging scripts for fast iteration

---

_Last updated: 2026-01-07_
