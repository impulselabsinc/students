import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
myBlock = block.TNT


myPosition = mc.player.getTilePos()

mc.setBlock(myPosition.x+0, myPosition.y+2, myPosition.z, myBlock)
