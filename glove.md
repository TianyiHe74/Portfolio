---
layout: portfolio
title: Gesture-classification glove
description: EMG and motion sensing, C firmware, and on-device inference on ESP32-S3.
---

<div class="shell"><a class="back-link" href="index.html#projects"><span aria-hidden="true">←</span> All projects</a></div>
<section class="case-hero shell photo-hero"><div><p class="eyebrow">Case study 05 / Embedded machine learning</p><h1>Gesture-classification<br>glove</h1><p class="case-intro">Our team built a wearable prototype to classify a small set of gestures. I worked on C firmware, sensor integration, data collection, model training and evaluation, and deployment to the device.</p><div class="tags"><span>C</span><span>ESP32-S3</span><span>EMG &amp; motion sensing</span><span>Edge Impulse</span></div></div><figure class="case-picture prototype-photo"><a href="assets/glove/class-prototype.jpeg" aria-label="Open full-size image: Our class prototype worn on a hand, with sensors, wiring, and breadboards attached."><img src="assets/glove/class-prototype.jpeg" alt="Our class prototype worn on a hand, with sensors, wiring, and breadboards attached." loading="lazy"></a><figcaption>Class-demo prototype · original sensor configuration</figcaption></figure></section>
<section class="case-overview shell" aria-label="Project at a glance"><div><p class="eyebrow">Context</p><p>Embedded Machine Learning<br>Team course project</p></div><div><p class="eyebrow">My contribution</p><p>Firmware, sensors, data collection,<br>model training, evaluation, and deployment</p></div><div><p class="eyebrow">Scope</p><p>Limited gesture vocabulary<br>Class results and later hardware kept separate</p></div></section>
<section class="project-overview shell" aria-labelledby="inference-title"><div class="section-heading"><div><p class="eyebrow">Class-version pipeline</p><h2 id="inference-title">From sensor samples to gesture output</h2></div></div><div class="data-flow inference-flow"><div><span class="eyebrow">Sample</span><h3>100 Hz</h3><p>Sensor channels</p></div><span aria-hidden="true">→</span><div><span class="eyebrow">Window</span><h3>1,000 ms</h3><p>300 ms stride</p></div><span aria-hidden="true">→</span><div><span class="eyebrow">Classify</span><h3>On-device inference</h3><p>Confidence gating and cooldown</p></div></div><p class="overview-note">The window duration is one part of response time. Complete-system latency is not reported here.</p></section>
<div class="case-body shell"><aside class="case-nav" aria-label="On this page"><p class="eyebrow">In this case study</p><a href="#section-1">01 / Sensors and my contribution</a><a href="#section-2">02 / Firmware and inference</a><a href="#section-3">03 / Class-demo results</a><a href="#section-4">04 / Later hardware revision</a><a href="#section-5">05 / Limitations and next steps</a></aside><div class="case-sections"><section id="section-1"><p class="eyebrow">01 / Embedded machine learning</p><h2>Sensors and my contribution</h2><p>The project explores a camera-free input method for assistive communication. It is a limited-vocabulary prototype, not a general sign-language translator.</p><p>The class prototype used an <strong>ESP32-S3</strong>, EMG, an IMU, a magnetometer, and flex sensors. My work connected sensor acquisition through analog inputs and I²C to the data-collection and embedded inference workflow.</p>
<details class="artifact"><summary>Class-demo system design and sensor inputs<span aria-hidden="true">+</span></summary><div class="artifact-content"><figure class="case-picture "><a href="assets/glove/demo_page_03.png" aria-label="Open full-size image: Class-demo system design and sensor inputs"><img src="assets/glove/demo_page_03.png" alt="Class-demo system design and sensor inputs" loading="lazy"></a><figcaption>Class-demo slide · original sensor configuration</figcaption></figure></div></details>
<details class="artifact"><summary>Edge Impulse workflow used in the class project<span aria-hidden="true">+</span></summary><div class="artifact-content"><figure class="case-picture "><a href="assets/glove/demo_page_04.png" aria-label="Open full-size image: Edge Impulse workflow used in the class project"><img src="assets/glove/demo_page_04.png" alt="Edge Impulse workflow used in the class project" loading="lazy"></a><figcaption>Class-demo slide · original sensor configuration</figcaption></figure></div></details>
<p>I also documented calibration procedures for the prototype.</p></section>
<section id="section-2"><p class="eyebrow">02 / Embedded machine learning</p><h2>Firmware and inference</h2><p>The documented pipeline samples sensor channels at <strong>100 Hz</strong>, forms <strong>1,000 ms windows</strong>, and advances by a <strong>300 ms stride</strong>. An Edge Impulse model classifies each window, with confidence gating and a cooldown to reduce ambiguous or repeated outputs.</p>
<p>The gesture labels are <code>I_LOVE_YOU</code>, <code>GOODBYE</code>, <code>HELLO</code>, <code>PLEASE</code>, <code>THANK_YOU</code>, and <code>YES</code>, alongside <code>IDLE</code> and <code>OTHER</code>. <code>UNCERTAIN</code> is an abstention output when confidence is insufficient.</p>
<p>A one-second input window and model computation time are different parts of the response time. I do not report a measured end-to-end latency for the complete system here.</p>
</section>
<section id="section-3"><p class="eyebrow">03 / Embedded machine learning</p><h2>Class-demo results</h2><div class="table-scroll"><table>
<thead>
<tr>
<th>Evaluation</th>
<th>Reported result</th>
</tr>
</thead>
<tbody><tr>
<td>Validation accuracy</td>
<td>94.6%</td>
</tr>
<tr>
<td>Validation loss</td>
<td>0.17</td>
</tr>
<tr>
<td>Test accuracy</td>
<td>93.06%</td>
</tr>
</tbody></table></div>
<p>These are the results shown in the class-demo slides below. They apply to that model and dataset; they do not demonstrate accuracy across new users or later hardware revisions.</p>
<details class="artifact"><summary>Validation accuracy, loss, and per-class confusion matrix<span aria-hidden="true">+</span></summary><div class="artifact-content"><figure class="case-picture "><a href="assets/glove/demo_page_05.png" aria-label="Open full-size image: Validation accuracy, loss, and per-class confusion matrix"><img src="assets/glove/demo_page_05.png" alt="Validation accuracy, loss, and per-class confusion matrix" loading="lazy"></a><figcaption>Class-demo slide · original sensor configuration</figcaption></figure></div></details>
<details class="artifact"><summary>Test accuracy and confusion matrix, including uncertain outputs<span aria-hidden="true">+</span></summary><div class="artifact-content"><figure class="case-picture "><a href="assets/glove/demo_page_06.png" aria-label="Open full-size image: Test accuracy and confusion matrix, including uncertain outputs"><img src="assets/glove/demo_page_06.png" alt="Test accuracy and confusion matrix, including uncertain outputs" loading="lazy"></a><figcaption>Class-demo slide · original sensor configuration</figcaption></figure></div></details>
<p>The <code>OTHER</code> category and ambiguous gestures account for several of the errors. The test matrix also shows abstentions. That makes confidence handling part of the interface behavior, rather than just an overall accuracy number.</p>
<details class="artifact"><summary>Class prototype deployed on a glove<span aria-hidden="true">+</span></summary><div class="artifact-content"><figure class="case-picture "><a href="assets/glove/demo_page_07.png" aria-label="Open full-size image: Class prototype deployed on a glove"><img src="assets/glove/demo_page_07.png" alt="Class prototype deployed on a glove" loading="lazy"></a><figcaption>Class-demo slide · original sensor configuration</figcaption></figure></div></details>
<p><a href="assets/glove/Demo.pdf">View the class-demo slides</a></p>
</section>
<section id="section-4"><p class="eyebrow">04 / Embedded machine learning</p><h2>Later hardware revision</h2><p>After the class project, I revised the sensing setup to remove the flex sensors and use an external <strong>MMC5983MA magnetometer</strong>. The revised hardware includes:</p>
<ul>
<li>Seeed XIAO ESP32-S3.</li>
<li>Grove EMG Detector with an ADS1115 I²C ADC.</li>
<li>MPU-9255 accelerometer and gyroscope.</li>
<li>MMC5983MA magnetometer in place of the IMU&#39;s internal magnetometer.</li>
</ul>
<p>The diagrams and evaluation screenshots above describe the class version, which included flex sensors. I have not published a new accuracy evaluation for the revised sensor set on this page.</p>
</section>
<section id="section-5"><p class="eyebrow">05 / Embedded machine learning</p><h2>Limitations and next steps</h2><p>EMG changes with electrode placement and between sessions, and movement can introduce noise. Magnetic disturbances also affect orientation measurements. Expanding the vocabulary and exploring phrase-level output are further work, not demonstrated capabilities of the class prototype.</p>
<p>The next useful evaluation would separate training and testing across sessions and users, then report per-class precision and recall as well as complete-system latency. Source code is not publicly accessible through this portfolio; the demo slides and diagrams are the available artifacts.</p>
</section></div></div>
<section class="next-project shell"><p class="eyebrow">Next project</p><a href="postpartum_health.html"><h2>Environmental sensing for home health</h2><span aria-hidden="true">↗</span></a><p>Wi-Fi data collection, a Raspberry Pi receiver, and DynamoDB logging.</p></section>
