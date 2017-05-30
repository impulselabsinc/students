import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()
color = 0

while True:
    hits = mc.events.pollBlockHits()
    if hits:
        for hit in hits:
            mc.postToChat(str(color))
            hitBlock = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
            if hitBlock.id == block.WOOL.id:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.WOOL.id, random.randint(0,15))
    time.sleep(0.1)
