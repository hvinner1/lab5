import RPi.GPIO as GPIO
import time
import PCF8591

led = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
        
state = 0  
# current position in stator sequence

class photo(PCF8591):

  def __init__(self,address):
    self.PCF8591 = PCF8591(0x48)
   

  def light(self):  
    try:
      self.light = self.PCF8591.read(0)
    except Exception as e:
        print ("Error: %s \n" % e)
    return self.light

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  global state
  state += dir
  if state > 7: state = 0
  elif state < 0: state =  7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)

def moveSteps(steps, dir):
  # move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)

class Stepper:
  def __init__(self,address):
    self.photo = photo(0x40)

  def goAngle(angle):
    moveSteps(angle,1)
  
  def zero():
    GPIO.output(led, 1) # set output to 3.3V
    sensor = photo.light()
    while sensor > 50:
      moveSteps(360,1)
      #move the motor using
    GPIO.output(led, 0) # set output to 0V
    time.sleep(0.1)
    #zero() – turn the motor until the photoresistor is occluded by the cardboard piece. Only actuate the LED while the zeroing process is ongoing.
  
  GPIO.cleanup() 
