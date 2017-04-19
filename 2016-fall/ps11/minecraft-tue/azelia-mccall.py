import mcpi.mincraft as mincraft
import mcpi.block as block

mc=mincraft.Mincraft.create()
tnt = block.TNT_EXPLODING
pos = mc.player.getTilepos()
x = pos.x + 1
y = pos.y
z = z + 1

mc.setblock(x,y,z,tnt)
