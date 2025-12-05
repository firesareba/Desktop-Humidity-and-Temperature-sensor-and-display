## **Desktop-Humidity-and-Temperature-sensor-and-display**

A Simple Humidity and Temperature sensor and display using the DHT22 TEMP/HUM sensor displaying on the 0.91" OLED used in the Hackpad aswell as the RP2040 used in the same hackpad. Goes on your desk\!

## **Inspiration**

I wanted to create a highly compact and portable standalone environmental monitor that could provide accurate temperature and humidity readings without needing a host computer. I used the Seeed XIAO RP2040 for its small footprint and native CircuitPython support which made integration with the SSD1306 OLED and DHT22 sensor straightforward.

## **Challenges**

This was my first time making a PCB and Cad Case without a walkthrough guide so it was very fun. I had trouble using Autodesk Fusion until I discovered point to point movement which made things EZPZ. When writing the ReadMe I realized that the DHT22 was OLD and SUCKS but I was too lazy to switch to the DHT20 right now. Hopefully this works :/

THANKS HACK CLUB\!

## **Specifications**

Bill of Materials (BOM):

* 	Microcontroller Module RP2040	U1	1	Seeed Studio XIAO RP2040  $6.52 (SAME AS HACKPAD) https://www.aliexpress.us/item/3256803497572374.html?spm=a2g0o.cart.0.0.7b2f38daLoMOR1&mp=1&pdp_npi=5%40dis%21USD%21USD%208.70%21USD%206.52%21%21USD%206.52%21%21%21%402103123917649589668664735e58c8%2112000046085310555%21ct%21US%213031952535%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D&gatewayAdapt=glo2usa
* 	Temp/Humidity Sensor Module	U2	1	DHT22 $1.99 (AM2302) https://www.aliexpress.us/item/3256810097495479.html?spm=a2g0o.cart.0.0.7b2f38daLoMOR1&mp=1&pdp_npi=5%40dis%21USD%21USD%203.45%21USD%201.99%21%21USD%201.99%21%21%21%402103123917649589668664735e58c8%2112000051781867490%21ct%21US%213031952535%21%211%210&gatewayAdapt=glo2usa
* 	OLED Display I2C (128x32)	DS1	1	SSD1306 Module $5.22 (SAME AS HACKPAD)https://www.aliexpress.us/item/3256806165075447.html?spm=a2g0o.cart.0.0.7b2f38daLoMOR1&mp=1&pdp_npi=5%40dis%21USD%21USD%205.22%21USD%205.22%21%21USD%205.22%21%21%21%402103123917649589668664735e58c8%2112000046260541813%21ct%21US%213031952535%21%211%210&gatewayAdapt=glo2usa
* 	Resistor Pull-up 4.7k Ohm THT	R1	1	Generic 4.7k Ohm $1.94 https://www.aliexpress.us/item/3256808490939217.html?spm=a2g0o.cart.0.0.7b2f38daLoMOR1&mp=1&pdp_npi=5%40dis%21USD%21USD%202.16%21USD%202.16%21%21USD%202.16%21%21%21%402103123917649589668664735e58c8%2112000046202387964%21ct%21US%213031952535%21%211%210&gatewayAdapt=glo2usa
* 	Custom PCB 2-Layer	N/A	1	Custom Fabrication $2.10 (not include shipping) jlcpcb.com
* 	M2 Mounting Hardware Set	N/A	4	M2 Screws and Nuts $1.99 https://www.aliexpress.us/item/3256806973435795.html?spm=a2g0o.productlist.main.2.76db4606oUQ3UL&algo_pvid=0341b1cd-b025-4122-beb1-a285ca46d764&algo_exp_id=0341b1cd-b025-4122-beb1-a285ca46d764-1&pdp_ext_f=%7B%22order%22%3A%223558%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%215.19%211.99%21%21%215.19%211.99%21%4021032f3717649599987684032e59da%2112000039655872513%21sea%21US%213031952535%21X%211%210%21n_tag%3A-29919%3Bd%3Ae6b47bf9%3Bm03_new_user%3A-29895%3BpisId%3A5000000191721587&curPageLogUid=WGOtix9hxv8g&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007159750547%7C_p_origin_prod%3A
* \* A BOM CSV is also included but doesn't account for things outside the PCB

## **Wiring and Schematic**

The circuit uses the IIC interface for the OLED and a single digital pin for the DHT22 sensor. You can't drop the 4.7k Pull Up resistor as you need it to run the DHT22.

## **Visuals**
<img width="1245" height="955" alt="Screenshot 2025-12-02 210005" src="https://github.com/user-attachments/assets/4dc7df91-602e-4da3-a5de-aba487a7f845" />
<img width="1671" height="631" alt="Screenshot 2025-12-02 192022" src="https://github.com/user-attachments/assets/65350ea7-3e79-45dc-830e-ad3cab0d8c85" />
<img width="1275" height="942" alt="Screenshot 2025-12-02 192240" src="https://github.com/user-attachments/assets/80d8092e-06f6-4a51-b2f0-a1b48b149c27" />
<img width="1241" height="647" alt="Screenshot 2025-12-02 192101" src="https://github.com/user-attachments/assets/a19d970b-018c-467b-9711-0a89b54a89e6" />
<img width="1166" height="1104" alt="Screenshot 2025-12-02 192051" src="https://github.com/user-attachments/assets/c67fe96a-2501-4144-b020-2c2fbfd7e51c" />
<img width="1353" height="1015" alt="Screenshot 2025-12-02 192037" src="https://github.com/user-attachments/assets/f76420f0-7cfb-4983-9678-60b9b27785cc" />
<img width="1482" height="1044" alt="Screenshot 2025-12-02 192704" src="https://github.com/user-attachments/assets/942aba56-df0c-4bd7-bf97-99c706269aa2" />
<img width="1336" height="1119" alt="Screenshot 2025-12-02 192612" src="https://github.com/user-attachments/assets/0e8f1394-f14b-495d-856b-62ab594ebfb1" />
<img width="1452" height="1084" alt="Screenshot 2025-12-02 192307" src="https://github.com/user-attachments/assets/01aaea9d-16a9-4cb2-84a4-ec094d7f98da" />
<img width="3507" height="2480" alt="image" src="https://github.com/user-attachments/assets/0d730607-c7be-432b-9813-d19380d968d8" />
<img width="2447" height="823" alt="image" src="https://github.com/user-attachments/assets/54eeb2d4-a18a-4198-9855-39386a6ee651" />
<img width="492" height="712" alt="image" src="https://github.com/user-attachments/assets/586d4754-60ba-49da-b832-c27724a0c047" />



## **Firmware Setup (CircuitPython)**

The project runs using CircuitPython.
### **Code (code.py)**

I also included Celsius to Fahrenheit conversion.

### **Required Libraries**

The following Adafruit CircuitPython libraries must be copied into the **lib** folder on the CIRCUITPY drive for the code to run, these are included in the provided ZIP in Firmware:

* adafruit\_dht  
* adafruit\_ssd1306  
* adafruit\_display\_text  
* Plus other libraries defined in code.py

## **PCB and Mechanical Notes**

* Layout: The design uses a two-layer PCB with all traces manually routed.  
* DHT22 Placement: The DHT22 sensor is mounted vertically near the board edge and requires the mesh face to be exposed to ambient air for accurate readings.

## **Getting Started**

1. Flash Firmware: Double-tap the RESET button on the XIAO to enter bootloader mode and drag the .uf2 CircuitPython firmware file onto the RPI-RP2 drive.  
2. Install Libraries: Copy the required libraries into the CIRCUITPY/lib folder.  
3. Upload Code: Copy the final code.py file to the root of the CIRCUITPY drive.  
4. Test: Monitor the OLED display and the serial console for the temperature and humidity outputs.

**Notes**

* I Might update this in the future to use the DHT20 sensor however the purchase of everything will be on my self if I upgrade and any grants will only be used for this initial version
* Some 3d models on the PCB are inaccurate to the footprints, The 3d models used are for visual purposes only and should not be taken literally.
