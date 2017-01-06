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
switch_pin = 4 # Relay control pin

# A function to check for user input and return it
def checkInput():
  input=port.readline()
  input=input.strip()
  return input

# Setup GPIO
GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Pin numbering mode

GPIO.setup(switch_pin, GPIO.OUT) # Set pin modes

# Setup serial connection to Arduino
port=serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=0.2)

# Start "OFF"
laststate=0
currstate=0
GPIO.output(switch_pin, currstate)
print datetime.datetime.now(),"Starting universal remote"

# Active loop
while True:

  # Check input
  input=checkInput()

  # If motion, log activity
  if input=="MOTION":
    print datetime.datetime.now(),"Motion detected"
    
  # If remote, analyze input
  if input=="ONE":
    print datetime.datetime.now(),"Input detected: Device 1"
    
  if input=="TWO":
    print datetime.datetime.now(),"Input detected: Device 2"

  if input=="THREE":
    print datetime.datetime.now(),"Input detected: Device 3"
    
  if input=="FOUR":
    print datetime.datetime.now(),"Input detected: Device 4"

  # Check for state change
  if currstate!=laststate:
    laststate=currstate
    GPIO.output(switch_pin, currstate)

  # Wait (tuned off because of serial timeout delay)
  #time.sleep(poll_time)

# Cleanup
# GPIO.cleanup()
