import mcpi.minecraft as minecraft
import mcpi.block as block
tnt=block.TNT_EXPleODING
pos=mc.player.getTilepos()
pos=mc.player.getTilePos()
x=pos.x+1
y=pos.y
z=pos.z+1
mc.setBlock(x,y,2,tnt)
