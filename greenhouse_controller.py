# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Armando Valderrama Navarro
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Simulator functions
from blink import run_blink
from marquee import run_marquee_left, run_marquee_right
from bcd import bcd7
from random import random

last_error = random()
current_temperature = 15

def get_current_temperature():
    return current_temperature

def set_current_temperature(i: int):
    return current_temperature + i

def switch():
    return

def temperature_pid(target_temperature: int):
    global last_error

    kp, kd = 0.5
    current_temperature = get_current_temperature()
    error = target_temperature - current_temperature
    derivative = error - last_error
    control_variable = (kp*error) + kd*derivative
    control_variable = 30 if control_variable > 30 else 15 if control_variable < 15 else control_variable
    set_current_temperature(current_temperature + control_variable)
    last_error = error
    return

def graph():
    return

def radiator():
    return

def ventilator():
    return
