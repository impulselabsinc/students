import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
myBlock=block.WOOL_LIME

myposition=mc.player.getTilepos()
mc.setBlock(myPosition.x+1,mYPosition.y+1,myPosition.z,myBlock)                  
