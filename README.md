<div align="center">

# 🩺 Healthcare Telemetry Gateway

<p align="center">
  <b>A low-cost, ESP32-powered physiological data acquisition gateway for reliable, real-time remote patient monitoring.</b>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ESP32](https://img.shields.io/badge/Hardware-ESP32-red.svg?logo=espressif&logoColor=white)](https://github.com/nithesh259/healthcare-telemetry-gateway)
[![C++](https://img.shields.io/badge/Language-C%2B%2B-blue.svg?logo=c%2B%2B&logoColor=white)](https://github.com/nithesh259/healthcare-telemetry-gateway)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/nithesh259/healthcare-telemetry-gateway/pulls)

</div>

---


### Low-Cost ESP32-Powered Physiological Data Acquisition Gateway for Real-Time Remote Patient Monitoring

A modular healthcare telemetry system designed to acquire physiological parameters from low-cost sensors, process the data at an **ESP32 edge gateway**, and transmit telemetry to a remote monitoring platform.

The project currently includes a **Python-based physiological sensor simulator, Flask telemetry backend, and real-time web dashboard**, allowing the complete software pipeline to be developed and tested before connecting the physical MAX30102 sensor.

---

## 📌 Project Overview

Remote patient monitoring systems require reliable acquisition and transmission of physiological data such as:

- ❤️ Heart Rate
- 🫁 Blood Oxygen Saturation (SpO₂)
- 🌡️ Temperature
- 📡 Device connectivity and telemetry status

This project explores a low-cost architecture using an **ESP32-CAM as the edge gateway** and the **MAX30102 optical sensor** for heart-rate and SpO₂ acquisition.

The system is designed with a modular architecture so that simulated data can be replaced by real sensor data without changing the dashboard or backend architecture.

---

## 🏗️ System Architecture

### Current Development Pipeline

```mermaid
flowchart LR

    A[Python MAX30102 Simulator]
    B[Flask Backend]
    C[REST API]
    D[Web Dashboard]

    A -->|HTTP POST| B
    B --> C
    C --> D
