import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = block.WOOL_LIGHTBLUE


myPosition = mc.player.getTilePos()
mc.setBlock(myPosition.x+0, myPosition.y-1, myPosition.z, myBlock)
