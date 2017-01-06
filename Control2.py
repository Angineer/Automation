#!/usr/bin/env Python

# Control2.py

# This is a script for running an automation system developed by Andy Tracy
# on the Raspberry Pi. It will switch external devices depending on input
# from environmental sensors and user controllers. It is an updated version
# of Control.py, with the "auto" feature removed and additional user inputs.

# Author: Andy Tracy <adtme11@gmail.com>

import RPi.GPIO as GPIO
import serial
import time
import datetime

# Settings
poll_time = 0.1 # Time in seconds between checking for inputs
# Relay control pins
pins = {"d1": 4, 
  "d2": 17,
  "d3": 27,
  "d4": 22}

# A function to check for user input and return it
def checkInput():
  input=port.readline()
  input=input.strip()
  return input

# Setup GPIO
GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Pin numbering mode

# Set pin modes to output
for device, pin in pins.items():
  GPIO.setup(pin, GPIO.OUT)

# Setup serial connection to Arduino
port=serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=0.2)

# Relay states (start "OFF")
laststate = {"d1": False,
  "d2": False,
  "d3": False,
  "d4": False}
currstate = {"d1": False,
  "d2": False,
  "d3": False,
  "d4": False}
for device, pin in pins.items():
  GPIO.output(pin, currstate[device])
  
print datetime.datetime.now(),"Starting universal remote"

# Active loop
while True:

  # Check input
  input=checkInput()

  # If motion, log activity
  if input=="MOTION":
    print datetime.datetime.now(),"Motion detected"
    
  # If remote, analyze input
  if input=="HOME":
    print datetime.datetime.now(),"Input detected: Home"
    for device in currstate:
      currstate[device] = True
    
  if input=="ONE":
    print datetime.datetime.now(),"Input detected: Device 1"
    currstate["d1"] = not laststate["d1"]
    
  if input=="TWO":
    print datetime.datetime.now(),"Input detected: Device 2"
    currstate["d2"] = not laststate["d2"]

  if input=="THREE":
    print datetime.datetime.now(),"Input detected: Device 3"
    currstate["d3"] = not laststate["d3"]
    
  if input=="FOUR":
    print datetime.datetime.now(),"Input detected: Device 4"
    currstate["d4"] = not laststate["d4"]

  # Check for state change
  for device, state in currstate.items():
    if currstate[device]!=laststate[device]:
      print "Turning device",device,"to state",currstate[device]
      laststate[device]=currstate[device]
      GPIO.output(pins[device], currstate[device])

  # Wait (tuned off because of serial timeout delay)
  #time.sleep(poll_time)

# Cleanup
# GPIO.cleanup()
