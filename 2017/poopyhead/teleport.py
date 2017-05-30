import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

## Use the code below to figure out where to build your portal
## Always put the teleport exit in front of the portal so as not to get caught in the loop
#pos = mc.player.getTilePos()
#print pos.x
#print pos.y
#print pos.z

diamondPortalExit = (65, -1, 6)
goldPortalExit = (83, -1, 21)

def teleport(portal):
    mc.player.setPos(portal)

while True:
    time.sleep(0.1)
    pos = mc.player.getTilePos()
    if pos.x == 83 and pos.y == -1 and pos.z == 19:
        teleport(diamondPortalExit)
    if pos.x == 63 and pos.y == -1 and pos.z == 6:
        teleport(goldPortalExit)
