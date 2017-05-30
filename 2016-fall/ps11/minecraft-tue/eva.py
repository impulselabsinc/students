import mcpi.minecraft as minecraft
mc = minecraft.minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(pos.x)
mc.postToChat(pos.y)                                                                                                    
mc.postToChat(pos.z)

a = (pos.y)

if (a == -2)
mc.postToChat ("you did it!!!")
 zx
