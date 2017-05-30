import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
mc = minecraft.Minecraft.create()
tnt = block.TNT_EXPLODING
click_count = 0
last_input_state = False

try:
    while True:
        input_state = GPIO.input(17)
        print click_count
        if ((not last_input_state) and input_state):
            click_count = click_count + 1
            pos = mc.player.getTilePos()
            x = pos.x + 1
            y = pos.y - 1 + click_count
            z = pos.z + 1
            mc.setBlock(x, y, z, tnt)
        last_input_state = input_state
finally:
    GPIO.cleanup()
