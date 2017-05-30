import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilepos()

print ("x = " + str(pos.x))
print ("y = " + str(pos.y))
print ("z = " + str(pos.z))

