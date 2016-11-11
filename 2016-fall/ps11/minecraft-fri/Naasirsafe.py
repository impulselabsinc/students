import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc. player.getTilePos()
myBlock = mc.getBlock(pos.x, pos.y-1, pos.z)

print("x="+str(pos.x))
print("y="+str(pos.y))
print("z="+str(pos.z))
print(myBlock)

if myBlock == block.AIR:
 print('Not safe!')
 mc.postToChat('Not safe!')
else:
 print('safe.')
 mc.postToChat('safe.')      
    
