import network
import socket
from machine import Pin

# WiFi credentials
ssid = 'FRITZ!Box'
password = '61780260'

# LEDs
red_led = Pin(5, Pin.OUT)       # Red LED on GPIO5 / D5
yellow_led = Pin(18, Pin.OUT)   # Yellow LED on GPIO18 / D18
green_led = Pin(19, Pin.OUT)    # Green LED on GPIO19 / D19
internal_led = Pin(2, Pin.OUT)  # Internal ESP32 LED on GPIO2

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to WiFi...")

while not wifi.isconnected():
    pass

print("Connected!")
print(wifi.ifconfig())

# Create Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running...")

while True:
    client, addr = server.accept()
    print('Client connected from', addr)

    request = client.recv(1024)
    request = str(request)

    print(request)

    # Red LED control
    if '/red_on' in request:
        red_led.on()
    if '/red_off' in request:
        red_led.off()

    # Yellow LED control
    if '/yellow_on' in request:
        yellow_led.on()
    if '/yellow_off' in request:
        yellow_led.off()

    # Green LED control
    if '/green_on' in request:
        green_led.on()
    if '/green_off' in request:
        green_led.off()

    # Internal LED control
    if '/internal_on' in request:
        internal_led.on()
    if '/internal_off' in request:
        internal_led.off()

    html = """
    <html>
    <head>
        <title>ESP32 Smart Home</title>
    </head>
    <body>
        <h1>ESP32 WiFi 4 LEDs Control</h1>

        <h2>Red LED</h2>
        <a href="/red_on"><button>Red ON</button></a>
        <a href="/red_off"><button>Red OFF</button></a>

        <h2>Yellow LED</h2>
        <a href="/yellow_on"><button>Yellow ON</button></a>
        <a href="/yellow_off"><button>Yellow OFF</button></a>

        <h2>Green LED</h2>
        <a href="/green_on"><button>Green ON</button></a>
        <a href="/green_off"><button>Green OFF</button></a>

        <h2>Internal LED</h2>
        <a href="/internal_on"><button>Internal ON</button></a>
        <a href="/internal_off"><button>Internal OFF</button></a>

    </body>
    </html>
    """

    client.send(html)
    client.close()