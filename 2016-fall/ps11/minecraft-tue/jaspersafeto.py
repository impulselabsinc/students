import mcpi.minecraft as minecraft
import mcpi.block as block
import time


mc = minecraft.Minecraft.create()


x=10
while x > 0:
    x=x-1
    print(x)


    time.sleep(2)


    pos = mc.player.getTilePos()
    myBlock = mc.player(pos.x, pos.y-1, pos.z)
    if myBlock == block.AIR:
        print('Not safe!')
        else:
            print('safe.')
            mc.postToChat('Safe.')
