#!/usr/bin/env python
#Inpiration from:
#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
import RPi.GPIO as GPIO
import subprocess
import keyboard
import time

GPIO.setmode(GPIO.BCM)
#This is to initialize the PIR sensor (on pin 11, GPIO17)
#Activate the internal pull up resistor on this pin.
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

def button_callback(channel):
	keyboard.press_and_release('a')
	#Ligh up an LED:
	GPIO.output(27, GPIO.HIGH)
	#print("detected")

GPIO.add_event_detect(17, GPIO.FALLING, callback=button_callback)

while 1:
	time.sleep(3);
	GPIO.output(27, GPIO.LOW)

#message = input("Press enter to quit\n\n")

GPIO.cleanup()

