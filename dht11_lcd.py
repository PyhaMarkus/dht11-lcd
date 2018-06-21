#!/usr/bin/python
# -*- coding: utf-8 -*-
# Display DHT11 temperature and humidity sensor data on an LCD with the Raspberry Pi 3.
# Markus Pyhäranta 2018.

#Import libraries
import time
import sys
import Adafruit_DHT
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

# Define Raspberry Pi pin setup - Note: numbers refer to the GPIO numbers and not the number of the physical pins
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 11
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#Set the naming convention for pins. Refer to pins with their names e.g GPIO23 and not the physical number of the pin.
GPIO.setmode(GPIO.BCM)
#No warning messages on screen
GPIO.setwarnings(False)
#GPIO pins that are used to output data for the LEDs
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


# The actual program starts here - Run this over and over again
while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)

        sensorValue =  'Humidity: {0:0.1f} %\nTemp: {1:0.1f} C'.format(humidity, temperature)

	# Red LED if humidity values are over 45. Blue LED if not.
	if temperature >= 25:
		GPIO.output(23,GPIO.HIGH)
		GPIO.output(24,GPIO.LOW)

	else:
		GPIO.output(24,GPIO.HIGH)
		GPIO.output(23,GPIO.LOW)


	#Text to be displayed on the LCD
	lcd.message(sensorValue)
	#Sleep 5 seconds
	time.sleep(5.0)
	#Clear the screen
	lcd.clear()

# Start over.
