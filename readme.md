## **Desktop-Humidity-and-Temperature-sensor-and-display**

A Simple Humidity and Temperature sensor and display using the DHT22 TEMP/HUM sensor displaying on the 0.91" OLED used in the Hackpad aswell as the RP2040 used in the same hackpad. Goes on your desk\!

## **Inspiration**

I wanted to create a highly compact and portable stand-alone environmental monitor that could provide accurate temperature and humidity readings without needing a host computer. I utilized the powerful yet tiny Seeed XIAO RP2040 for its small footprint and native CircuitPython support which made integration with the SSD1306 OLED and DHT22 sensor straightforward.

## **Challenges**

This was my first time making a PCB and Cad Case without a walkthrough guide so it was very fun. I had trouble using Autodesk Fusion until I discovered point to point movement which made things EZPZ. Hopefully this works :/

THANKS HACK CLUB\!

## **Specifications**

Bill of Materials (BOM):

* 1x Seeed XIAO RP2040 (SAME AS HACKPAD)  
* 1x DHT22 Temperature and Humidity Sensor (4 BENT PIN VARIETY FOR FLAT ON PCB PLACEMENT)  
* 1x SSD1306 4 pin I2C OLED Display (128x32 resolution) (SAME AS HACKPAD)  
* 1x 4.7k Ohm Pull-up Resistor (R1)  
* 4x M2 mounting hardware  
* \* A BOM CSV is also included but doesn't account for things outside the PCB

## **Wiring and Schematic**

The circuit uses the I2C interface for the OLED and a single digital pin for the DHT22 sensor. The 4.7k pull-up resistor R1 is mandatory for reliable DHT22 operation.

## **Visuals**

SchematicPCBCase

## **Firmware Setup (CircuitPython)**

The project runs using the CircuitPython interpreter. The main script reads data performs the conversion and updates the display every three seconds.

### **Code (code.py)**

The core functionality includes Celsius to Fahrenheit conversion using the formula F \= (C \* 1.8) \+ 32\.

### **Required Libraries**

The following Adafruit CircuitPython libraries must be copied into the **lib** folder on the CIRCUITPY drive for the code to run:

* adafruit\_dht  
* adafruit\_ssd1306  
* adafruit\_display\_text  
* Plus other libraries defined in code.py

## **PCB and Mechanical Notes**

* Layout: The design uses a two-layer PCB with all traces manually routed without a full ground plane.  
* Resistor: The 4.7k pull-up resistor R1 is placed immediately adjacent to the DHT22 footprint to reduce noise.  
* Mounting: The PCB uses 2.2mm clearance holes for M2 screws. The corresponding case holes should be 2.4mm for easy assembly tolerance.  
* DHT22 Placement: The DHT22 sensor is mounted vertically near the board edge and requires the mesh face to be exposed to ambient air for accurate readings.

## **Getting Started**

1. Flash Firmware: Double-tap the RESET button on the XIAO to enter bootloader mode and drag the .uf2 CircuitPython firmware file onto the RPI-RP2 drive.  
2. Install Libraries: Copy the required libraries into the CIRCUITPY/lib folder.  
3. Upload Code: Copy the final code.py file to the root of the CIRCUITPY drive.  
4. Test: Monitor the OLED display and the serial console for the temperature and humidity outputs.

**Notes**

* I Might update this in the future to use the DHT20 sensor however the purchase of everything will be on my self if I upgrade and any grants will only be used for this initial version