import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

WHITE          = 0
ORANGE         = 1
MAGENTA        = 2
LIGHTBLUE      = 3
YELLOW         = 4
LIME           = 5
PINK           = 6
GRAY           = 7
LIGHTGRAY      = 8
CYAN           = 9
PURPLE         = 10
BLUE           = 11
BROWN          = 12
GREEN          = 13
RED            = 14
BLACK          = 15

#create the minecraft api
mc = minecraft.Minecraft.create()

#create the minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#get the players position
pos = mc.player.getTilePos()


mcdrawing.drawLine(pos.x,
                   pos.y,
                   pos.z,
                   pos.x,
                   pos.y,
                   pos.z,
                   block.WOOL.id, MAGENTA   )
