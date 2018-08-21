#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import time

def runLED(outNum):

    # Set the LED GPIO pin as an output
    GPIO.setup(outNum, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(outNum, True)

def turnOffLED(outNum):
    # Turn the GPIO pin off
    GPIO.output(outNum, False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the LED GPIO numbers
greenNum = 21
redNum = 19

while(True):
    runLED(greenNum)
    # Wait 5 seconds
    time.sleep(1)
    turnOffLED(greenNum)

    runLED(redNum)
    # Wait 5 seconds
    time.sleep(1)
    turnOffLED(redNum)
