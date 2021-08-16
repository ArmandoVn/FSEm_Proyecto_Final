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

""" Enciende el leds especificados en num, apagando los demás
	(To be developed by the student)
"""
def leds(num):
	run_blink(num)

""" Activa el modo marquesina
	type toma tres valores: left, right y pingpong
	(To be developed by the student)
"""
def marquee(type='pingpong'):
	switcher = {
		'left'     : _marquee_left,
		'right'    : _marquee_right,
		'pingpong' : _marquee_pingpong
	}
	func = switcher.get(type, None)
	if func:
		func()


"""	Despliega en número proporcionado en el display de siete segmentos.
	(To be developed by the student)
"""
def bcd(num):
	bcd7(num)


""" Activa el modo marquesina continua a la izquierda"""
def _marquee_left():
	run_marquee_left()

""" Activa el modo marquesina continua a la derecha"""
def _marquee_right():
	run_marquee_right()

""" Activa el modo marquesina ping-pong"""
def _marquee_pingpong():
	run_marquee_left()
	run_marquee_right()