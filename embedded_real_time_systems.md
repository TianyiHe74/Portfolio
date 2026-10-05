---
title: Embedded Linux and real-time scheduling
description: C applications, kernel modules, and execution tracing on Raspberry Pi 4
---

[All projects](./)

In CMU's Embedded Real-Time Systems course, I developed C applications, loadable kernel modules, and custom system calls for real-time scheduling and periodic-task monitoring on Raspberry Pi 4.

## My contribution

- Wrote user-space applications to generate periodic workloads and exercise scheduling behavior.
- Developed kernel components for task monitoring and control, including IOCTL interfaces and custom system calls.
- Used trace-cmd and KernelShark to inspect execution and scheduling behavior.

## Technical work

The coursework included Linux real-time policies such as `SCHED_FIFO` and `SCHED_RR`, CPU affinity, high-resolution timers for periodic wakeups, and multicore task allocation. I used application behavior and execution traces together to investigate what the scheduler was doing.

That distinction matters: configuring a real-time policy does not by itself demonstrate that an application meets its deadlines. Timing claims need measurements under the relevant workload.

## Results and limits

The applications and kernel work were completed as coursework. This page does not publish a benchmark dataset or claim a measured latency, deadline-miss rate, or CPU-overhead improvement. Course solution code is not included in this portfolio.
