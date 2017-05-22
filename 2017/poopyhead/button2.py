# Pins to use
# G = GND
# P = 17
# - - - - - - - - - - - - - - - - - - - -
# - - - G P - - - - - - - - - - - - - - -

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
click_count = 0

try:
    while True:
        input_state = GPIO.input(17)
        if input_state == False:
            click_count = click_count + 1
            print click_count
finally:
    GPIO.cleanup()
