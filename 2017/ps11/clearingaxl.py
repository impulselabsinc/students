# Import specific Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


# Set lower half of world to Sandstone
mc.setBlocks(-128,0,-128,128,-128,128,block.SANDSTONE.id)

# Set upper half to air
mc.setBlocks(-128,1,-128,128,128,128,block.AIR.id)  
