import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
myBlock=block.TNT_EXPLODING

myPosition=mc.player.getTilePos()
mc.setBlock(myPosition.x+0, myPosition.y+0, myPosition.z, myBlock)


