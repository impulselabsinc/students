import RPi.GPIO as GPIO
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


try:
    GPIO.output(LED_PIN, False)

finally:
    GPIO.cleanup()
