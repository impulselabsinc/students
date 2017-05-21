import RPi.GPIO as GPIO
import time

LED_PIN = 17
DUTY_CYCLE_MIN = 0
DUTY_CYCLE_MAX = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pause_interval = 0.02
intensity = DUTY_CYCLE_MIN
increasing = True
increment = 5

led = GPIO.PWM(LED_PIN, 100)
led.start(intensity)


try:
    for x in range(100000):
        if increasing:
            intensity += increment
            time.sleep(pause_interval)
            led.ChangeDutyCycle(intensity)
        else:
            intensity -= increment
            time.sleep(pause_interval)
            led.ChangeDutyCycle(intensity)

        if (intensity == DUTY_CYCLE_MIN):
            increasing = True

        if (intensity == DUTY_CYCLE_MAX):
            increasing = False

        print intensity

finally:
    led.stop()
    GPIO.cleanup()
