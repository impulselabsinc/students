
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myblock = block.GOLD_ORE
pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z + 1

mc.setBlocks(x, y, z, x+11, y+11, z+11, myblock)
