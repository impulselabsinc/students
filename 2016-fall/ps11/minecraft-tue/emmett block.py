import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
myblock=block.WOOL_LIME
myposition=mc.player.getTilePos()
mc.setBlock(myposition.x+0, myposition.y-1, myposition.z, myblock)
