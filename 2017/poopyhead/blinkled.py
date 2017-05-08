#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import RPi.GPIO as GPIO

blockId = block.WOOL_PINK.id
blockData = block.WOOL_PINK.data
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def drawCarpet(locx, locy, locz, size, blockId, blockData):
    mc.setBlocks(locx + 1, locy - 1, locz + 1, locx + size, locy - 1, locz + size, blockId, blockData)


mc = minecraft.Minecraft.create()
orig = mc.player.getTilePos()
drawCarpet( orig.x, orig.y, orig.z, 3, blockId, blockData)

try:
    while True:
        time.sleep(0.1)
        pos = mc.player.getTilePos()
        if pos.x > orig.x and pos.x < orig.x + 3 + 1 and pos.z > orig.z and pos.z < orig.z + 3 + 1:
            print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
            mc.postToChat("Welcome to the pink carpet!")
            GPIO.output(LED_PIN, True)
        else:
            GPIO.output(LED_PIN, False)

finally:
    GPIO.cleanup()
