#gpio pin 16

import RPi.GPIO as GPIO
import time

motor = 16


GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)


#start with leds off
pwm = GPIO.PWM(motor, 100)  # PWM object on our pin at 100 Hz
pwm.start(0)  # start with LED off

dcMin = 0
dcMax = 100
try:
  while True:
    for dc in range(dcMax,dcMin,-1):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(.02)
except KeyboardInterrupt:
  print("bye")
GPIO.cleanup()
