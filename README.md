# ESP32 WiFi Smart Lighting System

##  Deutsche Version

## Projektbeschreibung

Dieses Projekt demonstriert ein Smart Home Beleuchtungssystem mit ESP32 und MicroPython.

Der ESP32 verbindet sich mit dem WLAN und erstellt einen lokalen Webserver.  
Über ein Smartphone oder einen Browser können mehrere LEDs drahtlos gesteuert werden.

Das Projekt zeigt die Grundlagen von:

- ESP32 Mikrocontroller
- WiFi Kommunikation
- Web Server
- Smart Home Systeme
- GPIO Steuerung
- Parallel LED Verbindung
- IoT Grundlagen
- MicroPython Programmierung

---

## Systemübersicht

Das System enthält:

- 🔴 1 rote LED
- 🟡 2 gelbe LEDs
- 🟢 3 grüne LEDs
- 🔵 1 interne ESP32 LED

Alle LEDs werden über WLAN gesteuert.

---

## Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | WiFi Mikrocontroller |
| LEDs | Lichtausgabe |
| Widerstände | Schutz der LEDs |
| Breadboard | Schaltungsaufbau |
| Jumper Kabel | Elektrische Verbindungen |
| MicroPython | Programmiersprache |

---

## GPIO Belegung

| GPIO | Funktion |
|---|---|
| GPIO5 | Rote LED |
| GPIO18 | Gelbe LEDs |
| GPIO19 | Grüne LEDs |
| GPIO2 | Interne ESP32 LED |

---

## Schaltungslogik

Mehrere LEDs wurden parallel verbunden.

Jede LED besitzt einen eigenen Widerstand für sichere Strombegrenzung und stabile Funktion.

---

## Funktionen

- WiFi Verbindung
- Steuerung über Smartphone Browser
- Mehrere LED Zonen
- Webserver mit HTTP Kommunikation
- Gleichzeitige Steuerung mehrerer LEDs

---

## Python Code

```python
import network
import socket
from machine import Pin

ssid = 'Your_WiFi_Name'
password = 'Your_WiFi_Password'

red_led = Pin(5, Pin.OUT)
yellow_led = Pin(18, Pin.OUT)
green_led = Pin(19, Pin.OUT)
internal_led = Pin(2, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

while True:

    client, addr = server.accept()

    request = client.recv(1024)
    request = str(request)

    if '/red_on' in request:
        red_led.on()

    if '/red_off' in request:
        red_led.off()

    if '/yellow_on' in request:
        yellow_led.on()

    if '/yellow_off' in request:
        yellow_led.off()

    if '/green_on' in request:
        green_led.on()

    if '/green_off' in request:
        green_led.off()

    if '/internal_on' in request:
        internal_led.on()

    if '/internal_off' in request:
        internal_led.off()

    client.close()
```

---

#  English Version

## Project Description

This project demonstrates a Smart Home Lighting System using ESP32 and MicroPython.

The ESP32 connects to WiFi and creates a local web server.  
Using a smartphone or browser, multiple LEDs can be controlled wirelessly.

The project demonstrates:

- ESP32 microcontroller basics
- WiFi communication
- Web server creation
- Smart home systems
- GPIO control
- Parallel LED connections
- IoT fundamentals
- MicroPython programming

---

## System Overview

The system includes:

- 🔴 1 Red LED
- 🟡 2 Yellow LEDs
- 🟢 3 Green LEDs
- 🔵 1 Internal ESP32 LED

All LEDs are controlled over WiFi.

---

## Components Used

| Component | Description |
|---|---|
| ESP32 DevKit V1 | WiFi microcontroller |
| LEDs | Light output |
| Resistors | LED protection |
| Breadboard | Circuit prototyping |
| Jumper Wires | Electrical connections |
| MicroPython | Programming language |

---

## GPIO Configuration

| GPIO | Function |
|---|---|
| GPIO5 | Red LED |
| GPIO18 | Yellow LEDs |
| GPIO19 | Green LEDs |
| GPIO2 | Internal ESP32 LED |

---

## Circuit Logic

Multiple LEDs are connected in parallel.

Each LED uses its own resistor for safe current limiting and stable operation.

---

## Features

- WiFi connection
- Smartphone browser control
- Multiple LED zones
- HTTP web server
- Simultaneous LED control

---

## Future Improvements

- Temperature sensors
- Humidity monitoring
- Relay modules
- Smart energy systems
- Solar energy automation
- Mobile app control
- AI-based automation

---

# Author

## Ahmad Azroun

Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer
