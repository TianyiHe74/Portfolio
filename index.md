---
title: Tianyi He
description: Embedded firmware, hardware bring-up, and sensor systems
home: true
---

<div class="intro" markdown="1">
I am an M.S. student in Electrical and Computer Engineering at Carnegie Mellon, completing my program in **May 2027**. I work mainly in **C**, with Python for testing and data collection.

I like working on problems where building a useful physical system can make a real difference. These pages explain what I contributed, how I tested it, and what still needs work.
</div>

<section class="project-list" aria-labelledby="selected-projects">
  <h2 id="selected-projects">Selected projects</h2>

  <article class="project">
    <div class="project-summary">
      <h3><a href="esab.html">Medical-gas pipeline monitoring</a></h3>
      <p class="project-tools">Sensor systems · Requirements and design · Hardware testing</p>
      <p>Research with CMU’s Biorobotics Lab and ESAB. I contribute to firmware, sensor evaluation, board design, and a medical-gas testbed; the project page is a high-level summary because the implementation is confidential.</p>
    </div>
  </article>

  <article class="project">
    <div class="project-summary">
      <h3><a href="resp_ecmo_monitoring.html">TeleLine: gas-flow sensing and data acquisition</a></h3>
      <p class="project-tools">C · PSoC 5LP · USB serial · Python · Bench testing</p>
      <p>I replaced delay loops with hardware timers and built telemetry and test tools to make sampling more repeatable. The project page connects those changes to timing checks and reference-instrument testing.</p>
    </div>
  </article>

  <article class="project project-with-preview">
    <div class="project-summary">
      <h3><a href="stm32_freertos.html">STM32 firmware, PCB bring-up, and motor control</a></h3>
      <p class="project-tools">C · Device drivers · PCB layout · FreeRTOS</p>
      <p>I laid out and brought up a board from a course-provided schematic, then wrote its bare-metal and RTOS firmware. A motor controller brought the drivers, encoder feedback, and task timing together.</p>
    </div>
    <figure class="project-preview">
      <a href="stm32_freertos.html" aria-label="Read the STM32 motor-control project">
        <img src="assets/stm32/control-loop.svg" alt="Encoder feedback feeds a FreeRTOS PID task, which drives the motor through PWM." width="420" height="340" loading="lazy">
      </a>
      <figcaption>Motor-control loop</figcaption>
    </figure>
  </article>

  <article class="project">
    <div class="project-summary">
      <h3><a href="embedded_real_time_systems.html">Embedded Linux and real-time scheduling</a></h3>
      <p class="project-tools">C · Linux kernel modules · System calls · Execution tracing</p>
      <p>I built applications and kernel components on Raspberry Pi 4 for periodic-task monitoring and scheduling experiments, then used execution traces to investigate their behavior.</p>
    </div>
  </article>

  <article class="project project-with-preview">
    <div class="project-summary">
      <h3><a href="glove.html">Gesture-classification glove</a></h3>
      <p class="project-tools">C · ESP32-S3 · EMG and motion sensors · Edge Impulse</p>
      <p>Our team built a wearable prototype that recognizes a small set of gestures on the device. I contributed firmware, sensor integration, data collection, model training, and deployment.</p>
    </div>
    <figure class="project-preview glove-preview">
      <a href="glove.html" aria-label="Read the gesture-classification glove project">
        <img src="assets/glove/class-prototype.jpeg" alt="The class prototype worn on a hand, with flex sensors, wiring, and breadboards attached to the glove." width="688" height="914" loading="lazy">
      </a>
      <figcaption>Our class-demo prototype</figcaption>
    </figure>
  </article>

  <article class="project">
    <div class="project-summary">
      <h3><a href="postpartum_health.html">Environmental sensing for a home-health prototype</a></h3>
      <p class="project-tools">Python · Raspberry Pi · Wi-Fi and HTTP · AWS DynamoDB</p>
      <p>Our team used decision matrices to compare controllers, sensors, and communication options. I worked on environmental hardware and firmware, including the Pi receiver and cloud-logging path.</p>
    </div>
  </article>
</section>

<p class="sharing-note">Team contributions and sharing limits are identified on each project page.</p>
