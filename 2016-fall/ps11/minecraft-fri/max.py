import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

def safeFeet():
    myPosition = mc.player.getTilePos()

    b = mc.getBlock(myPosition.x, myPosition.y-1, myPosition.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(myPosition.x, myPosition.y-1, myPosition.z, block.MELON.id)

while True:
   safeFeet()
