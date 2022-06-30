#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
	subprocess.call('vcgencmd display_power 1', shell = True)
	keyboard.press_and_release('a')

GPIO.add_event_detect(15, GPIO.FALLING, callback=button_callback)

while 1:
	time.sleep(.1)
