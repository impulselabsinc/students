import mcpi.minecraft as minecraft
import mcpi.block as block
import time
 
mc = minecraft.Minecraft.create()

mc.setBlock(10,1,0,block.TNT)
mc.setBlock(21,1,0,block.TNT)
while True:

    pos = mc.player.getTilePos()

    if pos.x == 10 and pos.y == 2 and pos.z ==0:
        mc.player.setPos(20,2,0)


    elif pos.x == 21 and pos.y == 2 and pos.z ==0:
        mc.player.setPos(9,2,0)











