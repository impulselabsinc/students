import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = WOOL_PURPLE

myPosition =mc.player.getTilePos()
mc.setBlock( myPosition.y-1, myPosition.z myBlock)
