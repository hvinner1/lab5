#!/usr/bin/python3
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
#controls the led and motor steps
import RPi.GPIO as GPIO
import time
import Stepper
import PCF8591
import json


while True:
    with open("lab5.txt", 'r') as f:
      data = json.load(f)
      slider = int(data['angle'])
      sub = int(data['submit'])
      zero = int(data['zero'])
      if sub == 1:
        Stepper.moveAngle(slider)
        #call angle.stepper
        time.sleep(0.1)
      elif zero == 1:
        Stepper.zero()
  


