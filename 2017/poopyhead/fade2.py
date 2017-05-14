import wiringpi as wiringpi
import time

LED_PIN = 17
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(LED_PIN,2)
wiringpi.pwmWrite(LED_PIN,1000)
time.sleep(1)
wiringpi.pwmWrite(LED_PIN,0)
