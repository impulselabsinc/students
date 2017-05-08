import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


try:
    for x in range(0,10):
        print x
        GPIO.output(LED_PIN, True)
        time.sleep(0.2)
        GPIO.output(LED_PIN, False)

finally:
    GPIO.cleanup()
