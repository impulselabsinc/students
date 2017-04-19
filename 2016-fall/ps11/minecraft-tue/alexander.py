import mcpi.minecraft as minecraft
import mcpi.block as block


mc =minecraft.MINECRAFT.create()
tnt =block.TNT_EXPLODING
POS =MC.player.gettilepos{}
x =pos.x +1
y =pos.y
z =pos.z +1


mc.setBlOCK{x, y, z, tnt}
