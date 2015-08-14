import RPi.GPIO as GPIO

# Disable warnings
GPIO.setwarnings(False)

# Pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set pins to output mode
for n in (4, 17, 22, 27):
  GPIO.setup(n, GPIO.OUT, initial=0)

# Turn all relays off
def allOff():
    for n in (4, 17, 27, 22):
        GPIO.output(n, 0)

# Turn all relays on
def allOn():
    for n in (4, 17, 27, 22):
        GPIO.output(n, 1)

# Turn one relay off
def oneOff(relay):
    GPIO.output(relay, 0)

# Turn one relay on
def oneOn(relay):
    GPIO.output(relay, 1)

# Cleanup
# GPIO.cleanup()
