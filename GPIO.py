# Dummy rpi.gpio implementation
BOARD = 1
OUT = 1
IN = 1

PUD_DOWN = 1
BOTH = 2

def add_event_detect(a, b):
  print 'GPIO dummy add_event_detect'

def add_event_callback(a, b):
  print 'GPIO dummy add_event_callback'

def setmode(a):
  print 'GPIO dummy setmode'
  
def setup(a, b, pull_up_down = 0):
  print a
  
def output(a, b):
  print a
  
def cleanup():
  print 'GPIO dummy cleanup'

def setmode(a):
  print a

def setwarnings(flag):
  print 'False'