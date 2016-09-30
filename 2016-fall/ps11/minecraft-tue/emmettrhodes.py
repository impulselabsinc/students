import mcpi.mincraft as mincraft
import mvpi.block as bloack
mc=mincraft.minecraft.create()
tnt=block.TNT_EXPLODING
pos=mc.player.gettilepos()
x=pos.x + 1
y=pos.y
z=pos.z + 1
mc.setblock(x,y,z, tnt)


































