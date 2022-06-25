#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
#This is to initialize the PIR sensor (on pin 11, GPIO17)
#Activate the internal pull up resistor on this pin.
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#subprocess.call(['shutdown', '-h', 'now'], shell=False)

def button_callback(channel):
	print("detected")

GPIO.add_event_detect(17,GPIO.FALLING,callback=button_callback)

message = input("Press enter to quit\n\n")

GPIO.cleanup()

