import mcpi.minecraft as minecraft
import mcpi.block as block

mc= minecraft.Minecraft.create()
myblock = block.WOOL_LIME
pos = mc.player.getTilePos()
x = pos.x + 0
y = pos.y
z = pos.z + 0

mc.setBlocks(x,y,z, +11,y+11, z+11, myblock)
