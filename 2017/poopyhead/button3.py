# Pins to use
# G = GND
# P = 17
# - - - - - - - - - - - - - - - - - - - -
# - - - G P - - - - - - - - - - - - - - -

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
click_count = 0
last_input_state = False

try:
    while True:
        input_state = GPIO.input(17)
        if ((not last_input_state) and input_state):
            click_count = click_count + 1
            print click_count
        last_input_state = input_state
finally:
    GPIO.cleanup()
