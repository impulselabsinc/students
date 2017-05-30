import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

diamondPortalExit = (65, 1, 6)
goldPortalExit = (83, 1, 21)

goldPortalLoc = (83,1,19)
diamondPortalLoc = (63,1,6)

def teleport(portal):
    mc.player.setPos(portal)

myPosition = mc.player.getTilePos()
teleport(diamondPortalLoc)
mc.setBlock(83,1,19, block.MELON.id)

print myPosition.x
print myPosition.y
print myPosition.z
