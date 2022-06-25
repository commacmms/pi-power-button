#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
#This is to initialize the PIR sensor (on pin 11, GPIO17)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(17, GPIO.FALLING) #Stay here until the button is pressed after which, run the next line

subprocess.call(['shutdown', '-h', 'now'], shell=False)
