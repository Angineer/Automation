#!/usr/bin/env Python

# Control2.py

# This is a script for running an automation system developed by Andy Tracy
# on the Raspberry Pi. It will switch external devices depending on input
# from environmental sensors and user controllers. It is an updated version
# of Control.py, with the "auto" feature removed and additional user inputs.

# Author: Andy Tracy <adtme11@gmail.com>

import relay_shield
import fauxmo
import serial
import time
import datetime

# A function to check for user input and return it
def checkInput():
  input=port.readline()
  input=input.strip()
  return input

# Handler function for fauxmo device
class local_gpio(object):
  def __init__(self, shield, dev):
    self.shield = shield
    self.dev = dev

  def on(self):
    if self.shield.get_device_state(self.dev) == False:
      self.shield.toggle_device_state(self.dev)
    return True

  def off(self):
    if self.shield.get_device_state(self.dev) == True:
      self.shield.toggle_device_state(self.dev)
    return True

# Setup serial connection to Arduino
port=serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=0.2)

# Setup relay shield
shield = relay_shield.GPIOPins()

# Setup to respond to Alexa
# Each entry contains [name, handler, port #].
# Port number needs to be set for Alexa to find the device between power cycles,
# but requires running as root

fauxmo_devs = [
  ['lights', local_gpio(shield, "ONE"), 100]
]

p = fauxmo.poller()
u = fauxmo.upnp_broadcast_responder()
u.init_socket()
p.add(u)

for one_faux in fauxmo_devs:
  if len(one_faux) == 2:
    # If no fixed port, use a dynamic one
    one_faux.append(0)
  switch = fauxmo.fauxmo(one_faux[0], u, p, None, one_faux[2], action_handler = one_faux[1])

# Active loop
print datetime.datetime.now(),"Starting universal remote"

while True:
  try:
    # Poll fauxmo
    p.poll(100)

    # Check input
    input=checkInput()

    if input != "":
      print datetime.datetime.now(),"Input detected: " + input
    
      # If remote, analyze input
      if input=="HOME":
        pass
    
      if input in ["ONE", "TWO", "THREE", "FOUR"]:
        shield.toggle_device_state(input)

  except Exception, e:
    fauxmo.dbg(e)
    break
