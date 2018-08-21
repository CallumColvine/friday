# Connect ground to top
# Connect pi.IO to bottom

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(19)
    if not input_state:
        print('Button Pressed')
        time.sleep(0.2)
