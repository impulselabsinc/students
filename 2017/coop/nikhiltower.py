import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = block.TNT_EXPLODING
pos = mc.player.getTilePos()
x = pos.x 
y = pos.y
z = pos.z 

mc.setBlocks(x, y + 2, z, x, y + 2, z, myBlock)
