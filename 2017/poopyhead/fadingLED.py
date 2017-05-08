import wiringpi as wiringpi
import time

LED_PIN = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(LED_PIN,2)



wiringpi.pwmWrite(LED_PIN,1024)
value = 1024
increment = 4
increasing = False
count = 0
 
while count < 100000:
    wiringpi.pwmWrite(LED_PIN,value)

    if increasing:
        value += increment
        time.sleep(0.002)
    else:
        value -= increment
        time.sleep(0.002)

    if (value >=1024):
        increasing = False

    if (value <= 0):
        increasing = True

    time.sleep(0.002)
    count = count + 1
