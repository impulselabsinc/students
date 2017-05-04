import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

print pos.x
print pos.y
print pos.z

startx = pos.x 
starty = pos.y + 2
startz = pos.z

myBlock = block.BOOKSHELF
mc.setBlock(x, y, z, myBlock)
