import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()


tnt=block.TNT_EXPLODING
pos=mc.player.getTilepos()
x=pos.x+1
y=pos.y
z=pos.z+1
mc.setbiock(x,y,z,tnt)
            





