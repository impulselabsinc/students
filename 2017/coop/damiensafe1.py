import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
print ("x = " + str(pos.x))
print ("y = " + str(pos.y))
print ("z = " + str(pos.z))

myBlock = mc.getBlock(pos.x, pos.y - 1, pos.z)

if myBlock == block.AIR:
    print("Not safe!")
    mc.postToChat("Not safe!")
else:
    print("Safe.")
    mc.postToChat("Safe.")
