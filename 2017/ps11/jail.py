import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create("192.168.1.2")


mc.setBlocks(-5,-5,-5,5,5,5,block.TNT_EXPLODING)
mc.setBlocks(-4,-4,-4,4,4,4,block.AIR)
lol = mc.getPlayerEntityIds()

ugh = 0

for x in lol:
    mc.entity.setTilePos(x,ugh,0,0)
    ugh+=1

#192.167.1.4/5
                          
