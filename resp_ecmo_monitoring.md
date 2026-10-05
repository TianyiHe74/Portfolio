---
title: TeleLine gas-flow sensing
description: Firmware timing, USB telemetry, and benchtop validation
---

[All projects](./)

At CMU's Biorobotics Lab, I worked on firmware and data acquisition for a gas-flow sensing research prototype from June through December 2025. My focus was making sampling more repeatable and making the data easier to inspect and test.

**Platform:** PSoC 5LP, USB serial (CDC), Raspberry Pi, C, and Python.

## Sampling and timing

I replaced software-delay loops with PSoC hardware timers. In SYNC mode, BME sampling increased from roughly **15 Hz to a fixed 21.7 Hz**. I also added a selectable FAST mode with independent SDP pressure updates at **100 Hz** and BME updates at **20.8 Hz**.

The modes served different acquisition needs. Keeping their rates explicit made it possible to test the device's behavior and interpret the logged data without assuming that all sensors updated together.

## Telemetry and test tools

I implemented a versioned binary USB protocol with COBS framing, CRC-32, device timestamps, and sample-loss diagnostics. I built Python tools for session logging, live plots, automated rate sweeps, and hour-long timing tests.

These tools let me examine both the measurements and how they arrived. A changing value, a missed sample, and an irregular update interval are different problems; the telemetry needed to help distinguish them.

## Benchtop testing and handoff

I led **more than 20 hours of gas-flow testing** against a **TSI 4040 reference flow meter** across multiple parameter settings. I documented the firmware setup and data protocol so the dashboard team had an interface to work from.

This work established a repeatable acquisition and testing workflow. It does not establish clinical performance or a numerical sensing-accuracy improvement, and I do not claim either here.

## Public scope

The research code and raw data are not public. I can discuss the general sampling architecture, protocol design, and testing approach within the lab's sharing restrictions.
