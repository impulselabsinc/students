import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

myblock = block.WOOL_LIME


myposition = mc.ployer.getTilepos()
mc.setblock(myposition.x+1, myposition.y+1, myposition.z, myblock)
