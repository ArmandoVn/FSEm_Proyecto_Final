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
import json

# Simulator functions
from blink import run_blink
from marquee import run_marquee_left, run_marquee_right
from bcd import bcd7
from random import random
import json
from datetime import datetime

last_error = random()

""" Enciende el leds especificados en num, apagando los demás
	(To be developed by the student)
"""
def leds(num):
	run_blink(num)

"""	Despliega en número proporcionado en el display de siete segmentos.
	(To be developed by the student)
"""
def bcd(num):
	bcd7(num)

def get_data():
	with open('values.json') as f:
		data = json.load(f)
	return data

def set_data(data: dict):
	with open("values.json", "w") as f:
		json.dump(data, f)


def temperature_pid(target_temperature):
    global last_error
    print("0")
    kp= 0.5
    kd = 0.2
    current_temperature = get_data()["current_temperature"]
    error = int(target_temperature) - current_temperature
    derivative = error - last_error
    control_variable = (kp*error) + kd*derivative
    current_temperature += control_variable
    last_error = error
    return current_temperature


def set_ventilator_power(value):
	""" Ajusta la potencia del ventilador """
	print('Ajustando potencia del ventilador...')
	run_marquee_left()
	run_marquee_right()
	print('Potencia ajustada a: {}'.format(value))
	response = {}
	return json.dumps(response)


def set_radiator_power(targeted_radiator_power):
	""" Ajusta la potencia del rediador """
	print('Ajustando potencia del radiador...')
	run_marquee_left()
	run_marquee_right()
	print('Potencia ajustada a: {}'.format(value))
	response = {}
	return json.dumps(response)


def set_greenhouse_temperature(target_temperature):
	target_temperature = int(target_temperature)
	""" Ajusta la temperatura del invernadero """
	print('Ajusta la temperatura del invernadero...')
	run_marquee_left()
	run_marquee_right()
	print('Temperatura se acercará a: {}'.format(target_temperature))
	new_temperature = temperature_pid(target_temperature)
	print('Temperatura final es: {}'.format(new_temperature))
	data = get_data()
	data["current_temperature"] = round(new_temperature)
	set_data(data)
	response = {}
	return json.dumps(response)


def get_temperature_response(_=None):
	response = {}
	current_temperature = get_data()["current_temperature"]
	print('Temperatura actual es: {}'.format(current_temperature))
	response[str(datetime.now())] = current_temperature
	run_blink(8)
	return json.dumps(response)

