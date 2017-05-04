import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

print pos.x
print pos.y
print pos.z

startx = pos.x 
starty = pos.y
startz = pos.z + 2

endx = pos.x
endy = pos.y
endz = pos.z + 10

myBlock = block.BOOKSHELF
mc.setBlocks(startx,starty,startz,endx,endy,endz,myBlock)
