#! /usr/bin/python
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin numbers for stepper
DIRECTION = 12
STEP = 20

def pinSetup(num, io=GPIO.OUT):
    GPIO.setup(num, GPIO.OUT)

# Options for amount (GPIO.HIGH, GPIO.LOW)
def pinWrite(num, amount=GPIO.LOW):
    GPIO.output(num, amount)


pinSetup(DIRECTION, GPIO.OUT)
pinWrite(DIRECTION, GPIO.HIGH)

pinSetup(STEP, GPIO.OUT)
pinWrite(STEP, GPIO.LOW)
time.sleep(1)

# for x in xrange(1, 1000):

# Start stepping
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(19)
    pinWrite(STEP, GPIO.HIGH)
    time.sleep(0.0005)
    pinWrite(STEP, GPIO.LOW)
    time.sleep(0.0005)
    if not input_state:
        print('Button Pressed')
        pinWrite(STEP, GPIO.LOW)
        # time.sleep(0.2)
        break

# pinSetup(STEP, GPIO.OUT)
# pinSetup(DIRECTION, GPIO.OUT)
# pinWrite(DIRECTION, GPIO.LOW)

# for x in xrange(1, 1000):
#     pinWrite(STEP, GPIO.HIGH)
#     time.sleep(0.0005)
#     pinWrite(STEP, GPIO.LOW)
#     time.sleep(0.0005)



# time.sleep(20)
# Stop stepping
pinWrite(STEP, GPIO.LOW)
