# Display DHT11 temperature and humidity sensor data on an lcd with the Raspberry Pi 3.

![alt text](https://github.com/PyhaMarkus/dht11-lcd/blob/master/pictures/raspberrypi_lcd.png "Connections")

---

### Parts used:
| Quantity | Part name                             |
| -------- |:-------------:                        |
| 1        | Raspberry Pi 3 Model B                |
| 1        | DHT11 temperature and humidity sensor |
| 1        | 1602 LCD-screen with 16 pins          |
| 2        | 10K potentiometer                     |
| 2        | 330 ohm resistor                      |
| 2        | LED                                   |
| 1        | A large breadboard                    |
| 1        | A small breadboard                    |
| A lot    | Jumper wire                           |

---

### Libraries used:
* time
* sys
* Adafruit_CharLCD
* Adafruit_DHT
* RPi.GPIO

---

### Installation:

**Installing Adafruit DHT libary**

```
sudo apt-get update
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get install build-essential python-dev
sudo python setup.py install
```

**Installing RPLCD library**

```sudo apt-get install python-pip
sudo pip install RPLCD
```

**Download and run the python code**

```
git clone https://github.com/PyhaMarkus/dht11-lcd.git
cd dht11-lcd
```

Make any necessary changes to the code and then run with:

```
python dht11_lcd.py
```
---

### Sources used:
http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
https://pimylifeup.com/raspberry-pi-lcd-16x2/
