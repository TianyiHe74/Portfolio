---
layout: portfolio
title: Embedded Linux and real-time scheduling
description: C applications, kernel modules, and execution tracing on Raspberry Pi 4.
---

<div class="shell"><a class="back-link" href="index.html#projects"><span aria-hidden="true">←</span> All projects</a></div>
<section class="case-hero shell "><div><p class="eyebrow">Case study 04 / Systems</p><h1>Embedded Linux<br>&amp; real-time scheduling</h1><p class="case-intro">In CMU’s Embedded Real-Time Systems course, I developed C applications, loadable kernel modules, and custom system calls for real-time scheduling and periodic-task monitoring on Raspberry Pi 4.</p><div class="tags"><span>C</span><span>Linux kernel</span><span>Raspberry Pi 4</span><span>trace-cmd</span><span>KernelShark</span></div></div></section>
<section class="case-overview shell" aria-label="Project at a glance"><div><p class="eyebrow">Context</p><p>CMU coursework<br>Embedded Real-Time Systems</p></div><div><p class="eyebrow">My contribution</p><p>User-space workloads, kernel components,<br>and execution-trace analysis</p></div><div><p class="eyebrow">Public materials</p><p>Implementation summary<br>Course solution code is not distributed</p></div></section>
<section class="project-overview shell" aria-labelledby="linux-scope"><div class="section-heading"><div><p class="eyebrow">Implementation overview</p><h2 id="linux-scope">Workloads, kernel interfaces, and traces</h2></div></div><div class="linux-stack"><div class="stack-row"><span class="eyebrow">User space</span><h3>Periodic workloads</h3><p>C applications to exercise scheduling behavior.</p></div><div class="stack-row"><span class="eyebrow">Kernel space</span><h3>Task monitoring & control</h3><p>Loadable modules, IOCTL interfaces, and custom system calls.</p></div><div class="stack-row"><span class="eyebrow">Analysis tools</span><h3>Execution tracing</h3><p>trace-cmd and KernelShark to inspect execution and scheduling.</p></div></div><p class="overview-note">This is a summary of the coursework, not a benchmark or timing measurement.</p></section>
<div class="case-body shell"><aside class="case-nav" aria-label="On this page"><p class="eyebrow">In this case study</p><a href="#section-1">01 / My contribution</a><a href="#section-2">02 / Scheduling policies and timing</a><a href="#section-3">03 / Completed work and limitations</a></aside><div class="case-sections"><section id="section-1"><p class="eyebrow">01 / Systems</p><h2>My contribution</h2><ul>
<li>Wrote user-space applications to generate periodic workloads and exercise scheduling behavior.</li>
<li>Developed kernel components for task monitoring and control, including IOCTL interfaces and custom system calls.</li>
<li>Used trace-cmd and KernelShark to inspect execution and scheduling behavior.</li>
</ul>
</section>
<section id="section-2"><p class="eyebrow">02 / Systems</p><h2>Scheduling policies and timing</h2><p>The coursework included Linux real-time policies such as <code>SCHED_FIFO</code> and <code>SCHED_RR</code>, CPU affinity, high-resolution timers for periodic wakeups, and multicore task allocation. I used application behavior and execution traces together to investigate what the scheduler was doing.</p>
<p>That distinction matters: configuring a real-time policy does not by itself demonstrate that an application meets its deadlines. Timing claims need measurements under the relevant workload.</p>
</section>
<section id="section-3"><p class="eyebrow">03 / Systems</p><h2>Completed work and limitations</h2><p>The applications and kernel work were completed as coursework. This page does not publish a benchmark dataset or claim a measured latency, deadline-miss rate, or CPU-overhead improvement. Course solution code is not included in this portfolio.</p>
</section></div></div>
<section class="next-project shell"><p class="eyebrow">Next project</p><a href="glove.html"><h2>Gesture-classification glove</h2><span aria-hidden="true">↗</span></a><p>Sensor acquisition and on-device inference on ESP32-S3.</p></section>
