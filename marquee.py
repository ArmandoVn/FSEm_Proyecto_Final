#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# blink.py
# Blinks a led on pin 32 using Raspberry Pi
#
# Autor: Armando Valderrama Navarro
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

LEDS = [10, 12, 16, 18, 22, 24, 26, 32]

# Set up pin no. 32 as output and default it to low
for led in LEDS:
	GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)


# Blink the led
def run_marquee_right():
    for led in LEDS:
        GPIO.output(led, GPIO.HIGH) # Turn led on
        sleep(0.1)                 # Espera 500ms
        GPIO.output(led, GPIO.LOW) # Turn led off


def run_marquee_left():
    for i in range(len(LEDS)-1, -1, -1):
        GPIO.output(LEDS[i], GPIO.HIGH) # Turn led on
        sleep(0.1)                 # Espera 500ms
        GPIO.output(LEDS[i], GPIO.LOW) # Turn led off