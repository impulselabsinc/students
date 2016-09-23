import mepi.minecraft as minecraft
import mepi.block as block
tnt=block.TNT_EXPLODING
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
x=pos.x+1
y=pos.y
z=pos.z+1
mc.setBlock(x,y,z,tnt)
