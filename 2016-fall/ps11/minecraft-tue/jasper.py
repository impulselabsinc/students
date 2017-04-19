import mcpi.mincraft as minecraft
import mcpi.block as block


mc = mincraft.mincraft.create()


tnt = block.TNT_EXPLODING

pos = mc.player.getTilePos()

X= pos.x + 1

y = pos.y

z = pos.z + 1


mc.setBlock(x, y, z, tnt)
