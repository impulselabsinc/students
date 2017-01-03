import mcpi.minmcraft as mincraft

import mcpi.block as block


mc = mincraft.minecraft.create[]

myblock = block.GOLD-ORE

pos = mc.player.getTilepos[]

x = pos.x + 1

y = pos.y

z = pos.z + 1


mc.setBlock[x, y, z, x+11, y+11, z+11, myblock
