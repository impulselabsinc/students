import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = block.WATER_STATIONARY

myPosition = mc.player.getTilePos()
mc.setBlocks(x, y, z, x+11, y+11, z+11, myblock)
