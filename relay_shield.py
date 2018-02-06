#!/usr/bin/env Python

# relay_shield.py

# Implements functions for working with the RoboGaia relay shield:
# https://www.robogaia.com/4-relays-raspberry-pi-plateshield.html

# Author: Andy Tracy <adtme11@gmail.com>

import RPi.GPIO as GPIO

class GPIOPins(object):
  def __init__(self):
    # Relay controlled devices
    self.devices = {"ONE": {"pin": 4, "state": False}, 
      "TWO": {"pin": 17, "state": False},
      "THREE": {"pin": 27, "state": False},
      "FOUR": {"pin":22, "state": False}}

    # Setup GPIO
    GPIO.setwarnings(False) # Disable warnings
    GPIO.setmode(GPIO.BCM) # Pin numbering mode

    # Set pin modes to output and start "OFF"
    for dev, info in self.devices.iteritems():
      pin = info["pin"]
      state = info["state"]

      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, state)
  
  def get_device_state(self, device):
    return self.devices[device]["state"]

  def toggle_device_state(self, device):
    pin = self.devices[device]["pin"]
    new_state = not self.devices[device]["state"]

    self.devices[device]["state"] = new_state
    GPIO.output(pin, new_state)

  # Cleanup
  def cleanup_gpio():
    GPIO.cleanup()
