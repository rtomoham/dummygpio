# Dummy rpi.gpio implementation
MODULE_NAME = "GPIO DUMMY"

MODE_UNKNOWN -1
BOARD        10
BCM          11
SERIAL       40
SPI          41
I2C          42
PWM          43

IN = 1
OUT = 0

PUD_OFF  0
PUD_DOWN 1
PUD_UP   2

RISING  1
FALLING 2
BOTH    3

def add_event_detect(a, b):
  print MODULE_NAME + ' add_event_detect(' + str(a) + ', ' + str(b) + ')'

def add_event_callback(a, b):
  print MODULE_NAME + 'add_event_callback(' + str(a) + ', ' + str(b) + ')'

def setmode(a):
  print MODULE_NAME + ' setmode(' + str(a) + ')'
  
def setup(a, b, pull_up_down = 0):
  print MODULE_NAME + ' setup(' + str(a) + ', ' + str(b) + ', ' + str(pull_up_down) + ')'
  
def output(a, b):
  print MODULE_NAME + ' output(' + str(a) + ', ' + str(b) + ')'
  
def cleanup():
  print MODULE_NAME + ' cleanup()'

def setmode(a):
  print MODULE_NAME + 'setmode(' + str(a) + ')'

def setwarnings(flag):
  print MODULE_NAME + 'setwarnings(' + str(flag) + ')'
