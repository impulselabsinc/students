import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.create()
myBlock = block.WOOL_LIME

myPosition= mc.player.getTilepos()
myPosition = mc.player.mc.setBlock(myPosition.x+1, myPosition.z, myBlock)
