
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
tnt = block.TNT_EXPLODING
pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z + 1

mc.setBlock(x, y, z, tnt)


