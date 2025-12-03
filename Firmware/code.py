import time
import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_ssd1306
import adafruit_dht

# --- Configuration ---
DHT_PIN = board.GP8
SCL_PIN = board.GP7
SDA_PIN = board.GP6
OLED_ADDRESS = 0x3C
OLED_WIDTH = 128
OLED_HEIGHT = 32

# --- Initialization ---
try:
    dht_device = adafruit_dht.DHT22(DHT_PIN)
except RuntimeError as e:
    print(f"Error initializing DHT: {e}")

displayio.release_displays()
i2c = busio.I2C(SCL_PIN, SDA_PIN)
display_bus = displayio.I2CDisplay(i2c, device_address=OLED_ADDRESS)
display = adafruit_ssd1306.SSD1306(display_bus, width=OLED_WIDTH, height=OLED_HEIGHT)

splash = displayio.Group()
display.show(splash)

# Setup Display Text
temp_text = label.Label(terminalio.FONT, text="Temp: -- F" color=0xFFFFFF)
temp_text.x = 0
temp_text.y = 8
splash.append(temp_text)

humidity_text = label.Label(terminalio.FONT, text="Humi: -- %" color=0xFFFFFF)
humidity_text.x = 0
humidity_text.y = 24
splash.append(humidity_text)

print("CircuitPython Running")

# --- Main Loop ---
while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        if temperature_c is not None and humidity is not None:
            # Fahrenheit conversion: F = (C * 1.8) + 32
            temperature_f = (temperature_c * 1.8) + 32

            temp_text.text = f"Temp: {temperature_f:.1f} F"
            humidity_text.text = f"Humi: {humidity:.1f} %"

            print(f"Temp F: {temperature_f:.1f} | Humi: {humidity:.1f} %")

        else:
            temp_text.text = "Temp: Read Failed"
            humidity_text.text = "Humi: Read Failed"

    except RuntimeError as error:
        # Sensor timed out or CRC error
        print(f"DHT Runtime Error: {error.args[0]}")
        temp_text.text = "Temp: Error"
        humidity_text.text = "Humi: Check Wiring"

    except Exception as e:
        print(f"Unexpected error: {e}")
        temp_text.text = "Temp: Fatal Error"
        humidity_text.text = "Humi: Please Reset"

    time.sleep(3) # Wait 3 seconds