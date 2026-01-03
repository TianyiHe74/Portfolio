---
title: Embedded Real‑Time Systems (Embedded Linux & Scheduling)
---

# Embedded Real‑Time Systems — Embedded Linux & Real‑Time Scheduling (Raspberry Pi)

## TL;DR
I built user-space and kernel-level components on Raspberry Pi Linux to support experiments in **real-time scheduling**, **task monitoring**, and **performance tracing**. Work included C test applications, **loadable kernel modules**, and **custom system calls**, with trace analysis using **trace-cmd** and **KernelShark**.

> **Demo/logs:** (add link)  
> **Code:** (add repo link or “available on request”)

---

## What I built
- **C user-space test applications** to generate and measure periodic workloads.
- **Kernel modules** for task monitoring and control (e.g., IOCTL interfaces).
- **Custom syscalls** supporting real-time task management.
- **Tracing + analysis** workflows with trace-cmd / KernelShark.

---

## Key technical areas
- Real-time scheduling policies: **SCHED_FIFO / RR** (and experiments as applicable)
- CPU affinity + multicore allocation strategies
- High-resolution timers (**hrtimer**) for periodic wakeups
- Basic bin-packing heuristics and energy-aware considerations (cpufreq governors)

---

## Metrics (add at least one)
- Measured scheduling latency / deadline miss rate under load: **__**
- Reduced monitoring overhead to **__% CPU** or **__ µs/event**
- Demonstrated improved periodicity (jitter) from **__ → __ ms**
