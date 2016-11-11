import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = block.TNT_EXPLODING



myPosition = mc.player.getTilePos()

mc.setBlock(myPosition.x-1, myPosition.y-1, myPosition.z, myBlock)
