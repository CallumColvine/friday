#! /usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from liquor import Liquor

CURRENT_STATE = 'Start up'

# Stepper rotates 1.8 degrees
DIRECTION = 12
STEP = 20
BUTTON = 19
CURRENT_POSITION = -1.0

def pinSetup(num, io=GPIO.OUT):
    GPIO.setup(num, GPIO.OUT)

# Options for amount (GPIO.HIGH, GPIO.LOW)
def pinWrite(num, amount=GPIO.LOW):
    GPIO.output(num, amount)

def main(argv):
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)
    # State 1
    calibrationState()
    prepareDrinkList()


def calibrationState():
    CURRENT_STATE = 'Calibration'
    print CURRENT_STATE

    pinSetup(DIRECTION, GPIO.OUT)
    pinWrite(DIRECTION, GPIO.LOW)

    pinSetup(STEP, GPIO.OUT)
    pinWrite(STEP, GPIO.LOW)
    time.sleep(1)

    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input_state = GPIO.input(BUTTON)
    while input_state:
        print "Stepping"
        pinWrite(STEP, GPIO.HIGH)
        time.sleep(0.005)
        pinWrite(STEP, GPIO.LOW)
        time.sleep(0.005)
        input_state = GPIO.input(BUTTON)

    print "Button pressed. Stepper at 0 point"
    CURRENT_POSITION = 0.0

def initTestDrink():
    drinkList = [
        Liquor(1.0, 30.0, 'gin'),
        Liquor(1.0, 90.0, 'tequila'),
        Liquor(1.0, 60.0, 'tonic')
    ]
    return drinkList

def stepTo(position):
    pinSetup(DIRECTION, GPIO.OUT)
    if position > CURRENT_POSITION:
        pinWrite(DIRECTION, GPIO.HIGH)
    else:
        pinWrite(DIRECTION, GPIO.LOW)
    pinSetup(STEP, GPIO.OUT)
    pinWrite(STEP, GPIO.LOW)
    for x in xrange(0, abs(position)):
        pinWrite(STEP, GPIO.HIGH)
        time.sleep(0.005)
        pinWrite(STEP, GPIO.LOW)
        time.sleep(0.005)
        x += 1.8
        CURRENT_POSITION = x

def pourLiquor(amount):
    for x in xrange(1,1000000):


def prepareDrinkList():
    CURRENT_STATE = 'Drink Prep'
    print CURRENT_STATE
    liquorList = initTestDrink()
    for liquor in liquorList:
        stepTo(liquor.position)
        pourLiquor(liquor.amount)

if __name__ == "__main__":
    main(sys.argv)

# CALIBRATION
# 1. Step away from the switch
# 2. Stop, step towards the switch until button pressed
# DRINK PREP
# 3. Assemble list of required ingredients (objects)
# DRINK ASSEMBLY
# 4. Step to the position of the required liquor
# 5. Dispense some of that liquor until amount reached
#         Do so until list is complete
# CLEANUP
# 6. Rotate to 5 steps from 0 position

# DIRECTION = 12
# STEP = 20
