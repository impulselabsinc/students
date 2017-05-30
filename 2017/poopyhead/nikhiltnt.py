import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if hits:
        print "hits"
        for hit in hits:
            mc.postToChat("Hit")
            hitBlock = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
            if hitBlock.id == block.TNT.id:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.TNT_EXPLODING)
            if hitBlock.id == block.WOOL.id:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.WOOL.id, random.randint(0,15))
            if hitBlock.id == block.DIRT.id:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.TNT_EXPLODING)
    time.sleep(0.1)
