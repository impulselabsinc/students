import mcpi.minecraft as mincraft
import mcpi.block as block
tnt=block.TNT_EXPLODING
mc=minecraft.Minecraft.creat()
pos=mc.player.getTilePose()
x=pos.x+1
y=pos.yz=pos.z+1
mc.setBlock9x,y,z,tnt
