import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

blockId = 1

while True:
    hits = mc.events.pollBlockHits()
    if hits:
        for hit in hits:
            mc.postToChat(str(blockId))
            hitBlock = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
            mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, blockId, 0)
            blockId = blockId + 1
    time.sleep(0.1)
    
