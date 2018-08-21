#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import time

def runMotor(outNum):
    # Set the LED GPIO pin as an output
    GPIO.setup(outNum, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(outNum, GPIO.HIGH)

def stopMotor(outNum):
    GPIO.output(outNum, GPIO.LOW)

# def turnOffMotor(outNum):
#     # Turn the GPIO pin off
#     GPIO.output(outNum, False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the LED GPIO numbers
airPumpNum = 21
# redNum = 19

runMotor(airPumpNum)
# Wait 5 seconds
time.sleep(3)
stopMotor(airPumpNum)
