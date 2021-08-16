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
import random
import json
from datetime import datetime

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


def set_ventilator_power(value):
	""" Ajusta la potencia del ventilador """
	print('Ajustando potencia del ventilador...')
	run_marquee_left()
	run_marquee_right()
	print('Potencia ajustada a: {}'.format(value))
	response = {}
	return json.dumps(response)


def set_radiator_power(value):
	""" Ajusta la potencia del rediador """
	print('Ajustando potencia del radiador...')
	run_marquee_left()
	run_marquee_right()
	print('Potencia ajustada a: {}'.format(value))
	response = {}
	return json.dumps(response)


def set_greenhouse_temperature(value):
	""" Ajusta la temperatura del invernadero """
	print('Ajusta la temperatura del invernadero...')
	run_marquee_left()
	run_marquee_right()
	print('Temperatura ajustada a: {}'.format(value))
	response = {}
	return json.dumps(response)


def get_greenhouse_temp(selected_temp):
	response = {}
	response[str(datetime.now())] = random.randint(15, 30)
	run_blink(8)
	return json.dumps(response)
