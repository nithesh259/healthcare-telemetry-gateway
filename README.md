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

## 📌 Overview

The **Healthcare Telemetry Gateway** is an open-source hardware and software solution designed to bridge physiological sensors with remote telemetry dashboards. Built around the **ESP32 microcontroller**, it continuously collects vital telemetry (ECG, SpO2, Heart Rate, Temperature), processes signals locally, and transmits encrypted streams over Wi-Fi/MQTT to central monitoring systems.

---

## ⚡ Key Features

| Feature | Description | Tech Stack / Protocol |
| :--- | :--- | :--- |
| 📊 **Real-Time Streaming** | Low-latency physiological data acquisition and processing | MQTT / WebSockets |
| 🛡️ **Reliable Buffer** | Local fail-safe buffering prevents data loss during outage | SPIFFS / TLS 1.3 |
| ⚡ **Low Power** | Optimized battery lifecycle for continuous patient monitoring | ESP32 Sleep Modes |
| 🖥️ **Live Dashboard** | Interactive dashboard with waveform rendering & alerts | React / Grafana |
| 🔌 **Modular Design** | Expandable sensor interface for multi-parameter logging | I2C / SPI / ADC |

---

## 🏗️ System Architecture

```text
+-------------------+        +-------------------------+        +--------------------+
|  Health Sensors   | -----> |  ESP32 Gateway Node     | -----> | Telemetry Backend  |
| (ECG, SpO2, Temp) |        | (Signal Prep & Buffer)  |  MQTT  | (Node.js/Database) |
+-------------------+        +-------------------------+        +--------------------+
                                                                          |
                                                                          v
                                                                +--------------------+
                                                                |   Live Dashboard   |
                                                                +--------------------+
```
## 📊 Live Monitoring Dashboard

Below is a snapshot preview of the telemetry control center displaying real-time signal waveforms, physiological health ranges, and live patient metrics:

| Metric | Normal Range | Live Value | Signal Status | Visual Gauge |
| :--- | :--- | :--- | :--- | :--- |
| **Heart Rate (BPM)** | 60 – 100 BPM | `72 BPM` | 🟢 Stable | `[████████░░] 72%` |
| **SpO2 Level (%)** | 95 – 100 % | `98 %` | 🟢 Optimal | `[█████████░] 98%` |
| **Body Temp (°C)** | 36.5 – 37.5 °C | `36.8 °C` | 🟢 Normal | `[████████░░] 36.8°` |
| **ECG Lead-I** | Standard Range | `Active` | 📈 Streaming | `[~~~~~~~~~~~~]` |

---

## 🖥️ Interactive Dashboard Layout

<p align="left">
  <img src="https://img.shields.io/badge/Status-Live_Streaming-brightgreen?style=for-the-badge&logo=statuspage" alt="Live Status" />
  <img src="https://img.shields.io/badge/Protocol-WebSockets_|_MQTT-blue?style=for-the-badge" alt="Protocol" />
  <img src="https://img.shields.io/badge/Latency-<50ms-orange?style=for-the-badge" alt="Latency" />
</p>

```text
+-----------------------------------------------------------------------------------+
|  🏥 PATIENT TELEMETRY MONITOR — UNIT 402                   [🔴 LIVE STREAMING]   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  📈 ECG Waveform (Lead I) — 25mm/s                                                 |
|  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\         |
| /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \        |
|/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \       |
|                                                                                   |
+----------------------+----------------------+----------------------+--------------+
|  🫀 HEART RATE       |  🩸 SpO2 LEVEL       |  🌡️ BODY TEMP        | 🟢 SYSTEM    |
|  72 BPM              |  98%                 |  36.8 °C             | CONNECTED    |
|  [████████░░] Normal |  [█████████░] Optimal|  [████████░░] Normal | Battery: 94% |
+----------------------+----------------------+----------------------+--------------+
```
## 📋 Prerequisites
* **IDE:** PlatformIO IDE or Arduino IDE 2.x
* **Hardware:** ESP32 Development Board & CP210x/CH340 Drivers
* **Environment:** Node.js (v18+) & npm

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/nithesh259/healthcare-telemetry-gateway.git
cd healthcare-telemetry-gateway
```

### 2. Flash Firmware
```bash
cd firmware/healthcare-gateway
pio run --target upload
```

### 3. Launch Dashboard & Backend
```bash
cd ../../dashboard
npm install
npm start
```

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.
