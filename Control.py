# Control

# This is a script for running an automation system developed by Andy Tracy
# on the Raspberry Pi. It will switch external devices depending on input
# from environmental sensors and user controllers.

# Author: Andy Tracy <adtme11@gmail.com>

import RPi.GPIO as GPIO
import lirc
import time
import datetime

# Settings
on_time = 30 # Time in seconds that the device stays on when triggered
poll_time = 0.2 # Time in seconds between checking for inputs
switch_pin = 4 # Relay control pin
sensor_pin = 7 # Passive IR sensor pin

# A function to check for user input and return it
def checkInput():
  input=lirc.nextcode()
  if input!=[]: # We want to exhaust the queue every time it checks
    temp=["Temp"]
    while temp!=[]:
      temp=lirc.nextcode()
  return input

# Setup GPIO
GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Pin numbering mode

GPIO.setup(switch_pin, GPIO.OUT) # Set pin modes
GPIO.setup(sensor_pin, GPIO.IN)

# Setup LIRC
sockid = lirc.init("control", blocking=False)

# Start "OFF" in "Auto" mode
max_timer=on_time/poll_time # Convert from seconds to polling intervals
timer=max_timer

laststate=0
currstate=0
mode=["Auto"]
GPIO.output(switch_pin, currstate)
print datetime.datetime.now(),"Starting in Auto mode"

# 2 modes:
#  - Auto/motion detecting mode
#  - Manual mode

# Active loop
while True:
  # Auto Mode
  while mode==["Auto"]:
    
    # Check timer
    if timer>0:
      timer-=1
      if timer==0:
        currstate=0
        print datetime.datetime.now(),"Resuming monitor mode"


    # Check sensor
    if GPIO.input(sensor_pin)==0:
      print datetime.datetime.now(),"Motion detected"
      currstate=1
      timer=max_timer
      
    # Check remote
    input=checkInput()
    if input==["Power"]:
      print datetime.datetime.now(),"Input detected"
      currstate=1
      timer=max_timer
    if input==["Manual"]:
      mode=["Manual"]
      timer=0
      print datetime.datetime.now(),"Entering Manual mode"

    # Check for state change
    if currstate!=laststate:
      laststate=currstate
      GPIO.output(switch_pin, currstate)
    
    # Wait
    time.sleep(poll_time)

  # Manual Mode
  while mode==["Manual"]:

    # Check remote
    input=checkInput()
    if input==["Power"]:
      if currstate==1:
        currstate=0
      else:
        currstate=1
      print datetime.datetime.now(),"Input detected"
    if input==["Auto"]:
      mode=["Auto"]
      print datetime.datetime.now(),"Entering Auto mode"

    # Check for state change
    if currstate!=laststate:
      laststate=currstate
      GPIO.output(switch_pin, currstate)

    # Wait
    time.sleep(poll_time)

# Cleanup
# GPIO.cleanup()
