---
layout: portfolio
title: Embedded systems portfolio
description: C and Python, embedded firmware, hardware bring-up, and sensor systems. Engineering projects by Tianyi He, CMU M.S. ECE.
home: true
---

<div class="project-home">
<section class="home-intro shell">
  <p class="home-context">Carnegie Mellon University · M.S. ECE · May 2027</p>
  <div class="home-intro-columns">
    <h1>Embedded firmware<br>&amp; hardware bring-up</h1>
    <p class="home-description">I work mainly in C and Python, developing device drivers, integrating sensors, and testing hardware and firmware together.</p>
  </div>
</section>

<section class="home-projects shell" id="projects" aria-labelledby="work-title">
  <span id="selected-projects" aria-hidden="true"></span>
  <div class="home-section-heading"><h2 id="work-title">Projects</h2><p>My contributions, implementation details, and how I tested the work.</p></div>
  <div class="project-gallery">
    <a class="gallery-project" href="automotive_can.html">
      <div class="project-visual visual-can">
        <span class="visual-label">Controller PCB</span>
        <div class="board-crop"><img src="assets/automotive-can/pcb-top.png" alt="KiCad render of the four-layer automotive controller board, shown horizontally." width="1568" height="1064"></div>
        <span class="visual-caption">KiCad render · design artifact</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">CMU 18-649 · Team project</p>
        <div class="gallery-title"><h3>Drive-by-wire over redundant CAN</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">My work on a three-person automotive prototype: firmware integration, CAN fault diagnosis, automated tests and a four-layer PCB design.</p>
        <p class="gallery-tools">C / Zephyr · STM32 + Pi · CAN / Raft · KiCad</p>
      </div>
    </a>
    <a class="gallery-project" href="esab.html">
      <div class="project-visual visual-research">
        <span class="visual-label">Areas of contribution</span>
        <div class="research-map" role="img" aria-label="Three areas of contribution: sensor firmware, hardware integration, and testbed development.">
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="12" width="24" height="24" rx="3"/><path d="M18 12V6m12 6V6M18 36v6m12-6v6M12 18H6m6 12H6m30-12h6m-6 12h6"/><path d="m22 19-5 5 5 5m4-10 5 5-5 5"/></svg><span>Sensor<br>firmware</span></div>
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="8" y="8" width="32" height="32" rx="3"/><rect x="15" y="14" width="12" height="12" rx="1"/><path d="M27 19h7v14H18v-7M8 32h10"/><circle cx="34" cy="14" r="1.5"/><circle cx="14" cy="33" r="1.5"/></svg><span>Hardware<br>integration</span></div>
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="9" width="36" height="25" rx="3"/><path d="M11 24h7l4-9 5 14 3-8h7M18 40h12M24 34v6"/></svg><span>Testbed<br>development</span></div>
        </div>
        <span class="visual-caption">Public research summary</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">CMU Biorobotics Lab × ESAB</p>
        <div class="gallery-title"><h3>Medical-gas pipeline monitoring</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">I contributed to firmware, sensor evaluation, board design, and a medical-gas testbed. This is a high-level summary because implementation details are confidential.</p>
        <p class="gallery-tools">Sensor systems · PCB design · Hardware testing</p>
      </div>
    </a>
    <a class="gallery-project" href="resp_ecmo_monitoring.html">
      <div class="project-visual visual-acquisition">
        <span class="visual-label">Sampling &amp; data acquisition</span>
        <div class="acquisition-map" role="img" aria-label="SDP pressure and BME sensors feed the PSoC 5LP, which sends USB telemetry to Python tools.">
          <div class="sensor-inputs"><span>SDP pressure</span><span>BME</span></div><span class="diagram-arrow" aria-hidden="true">→</span>
          <div class="acquisition-node"><strong>PSoC 5LP</strong><span>Hardware timers</span></div><span class="diagram-arrow" aria-hidden="true">→</span>
          <div class="acquisition-output"><strong>Python</strong><span>Logs &amp; tests</span></div>
        </div>
        <span class="visual-caption">Timer-driven sampling → USB telemetry → inspection</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">CMU Biorobotics Lab</p>
        <div class="gallery-title"><h3>TeleLine: gas-flow sensing</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">I replaced delay loops with hardware timers and built telemetry and test tools to make sampling more repeatable.</p>
        <p class="gallery-tools">C · PSoC 5LP · USB serial · Python</p>
      </div>
    </a>
    <a class="gallery-project" href="embedded_real_time_systems.html">
      <div class="project-visual visual-linux">
        <span class="visual-label">Raspberry Pi 4 / Linux</span>
        <div class="kernel-map" role="img" aria-label="User-space C workloads, kernel modules and system calls, and execution analysis using trace-cmd and KernelShark.">
          <div><span>User space</span><strong>Periodic C workloads</strong></div>
          <div><span>Kernel space</span><strong>Modules &amp; system calls</strong></div>
          <div><span>Analysis</span><strong>trace-cmd / KernelShark</strong></div>
        </div>
        <span class="visual-caption">Workloads, kernel interfaces &amp; execution traces</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">CMU coursework</p>
        <div class="gallery-title"><h3>Embedded Linux &amp; real-time scheduling</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">I built applications and kernel components on Raspberry Pi 4 for periodic-task monitoring and scheduling experiments, then used execution traces to investigate their behavior.</p>
        <p class="gallery-tools">C · Linux kernel modules · System calls · Execution tracing</p>
      </div>
    </a>
    <a class="gallery-project" href="glove.html">
      <div class="project-visual visual-glove">
        <img src="assets/glove/class-prototype.jpeg" width="688" height="914" alt="Our wearable prototype with sensors and wiring on a glove, connected to a laptop during a demonstration." loading="lazy">
        <div class="glove-path" aria-hidden="true"><span>Sensor inputs</span><i>↓</i><strong>ESP32-S3</strong><i>↓</i><span>On-device<br>classification</span></div>
        <span class="visual-caption">Team prototype</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">Team course project</p>
        <div class="gallery-title"><h3>Gesture-classification glove</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">Our team built a wearable prototype that recognizes a small set of gestures on the device. I contributed firmware, sensor integration, data collection, model training, and deployment.</p>
        <p class="gallery-tools">C · ESP32-S3 · EMG and motion sensors · Edge Impulse</p>
      </div>
    </a>
    <a class="gallery-project" href="postpartum_health.html">
      <div class="project-visual visual-environment">
        <span class="visual-label">PM / gas sensing path</span>
        <div class="environment-map" role="img" aria-label="A Pico 2 W sensor node sends data over Wi-Fi and HTTP to a Raspberry Pi 5 receiver, followed by periodic uploads to DynamoDB.">
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="10" y="8" width="28" height="32" rx="3"/><rect x="17" y="17" width="14" height="14"/><path d="M6 15h4m-4 9h4m-4 9h4m28-18h4m-4 9h4m-4 9h4"/></svg><strong>Pico 2 W</strong><span>Sensor node</span></div>
          <span class="diagram-arrow" aria-hidden="true">→</span>
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="8" y="10" width="32" height="28" rx="3"/><path d="M14 17h20M14 24h20M14 31h10"/></svg><strong>Pi 5</strong><span>HTTP receiver</span></div>
          <span class="diagram-arrow" aria-hidden="true">→</span>
          <div><svg viewBox="0 0 48 48" aria-hidden="true"><ellipse cx="24" cy="12" rx="15" ry="6"/><path d="M9 12v23c0 8 30 8 30 0V12M9 24c0 8 30 8 30 0"/></svg><strong>DynamoDB</strong><span>Records</span></div>
        </div>
        <span class="visual-caption">Sensor node → base station → cloud storage</span>
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">Team course project</p>
        <div class="gallery-title"><h3>Environmental sensing for home health</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">Our team used decision matrices to compare controllers, sensors, and communication options. I worked on environmental hardware and firmware, including the Pi receiver and cloud-logging path.</p>
        <p class="gallery-tools">Python · Raspberry Pi · Wi-Fi / HTTP · DynamoDB</p>
      </div>
    </a>
    <a class="gallery-project" href="stm32_freertos.html">
      <div class="project-visual visual-control">
        <span class="visual-label">Position control / STM32</span>
        <img src="assets/stm32/control-study.svg" width="540" height="340" alt="Conceptual control loop: encoder feedback enters a FreeRTOS PID task, which drives the motor using PWM." loading="lazy">
      </div>
      <div class="gallery-copy">
        <p class="gallery-context">CMU coursework</p>
        <div class="gallery-title"><h3>STM32 firmware &amp; motor control</h3><span aria-hidden="true">↗</span></div>
        <p class="gallery-description">I laid out and brought up a board from a course-provided schematic, then wrote its bare-metal and FreeRTOS firmware for motor control.</p>
        <p class="gallery-tools">C · Device drivers · PCB layout · FreeRTOS</p>
      </div>
    </a>
  </div>
</section>
<section class="home-about shell" id="about" aria-labelledby="about-title">
  <img class="about-photo" src="assets/profile/tianyi-he.jpg" width="480" height="719" alt="Portrait of Tianyi He." loading="lazy" decoding="async">
  <h2 id="about-title">About me</h2>
  <div class="home-about-copy"><p>I’m an M.S. student in Electrical and Computer Engineering at Carnegie Mellon, completing my program in May 2027. I mainly work in C and Python.</p><p>I like working on problems where building a useful physical system can make a real difference. Here, I explain what I contributed, how I tested it, and what still needs work.</p><a class="text-link" href="mailto:hetianyi74@gmail.com">Contact me <span aria-hidden="true">↗</span></a></div>
</section>
</div>
