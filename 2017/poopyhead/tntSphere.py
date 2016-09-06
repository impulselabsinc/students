import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

mc.postToChat("Hallo, here's your sphere")

radius = 6

playerPos = mc.player.getPos()

for x in range(radius*-1,radius):
	for y in range(radius*-1, radius):
		for z in range(radius*-1,radius):
			if x**2 + y**2 + z**2 < radius**2:
				mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, block.TNT)
