import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()


pos = mc.player.getTilePos()


def fastTravel(pos):
    print " I am currently at " +"\n"+ str(pos.x)
    + "\n"+ str(pos.y) +"\n"+str(pos.z)
    mc.player.setTilePos(pos.x+10,pos.y,pos.z)
    pos = mc.player.getTilePos()
    print " I am currently at " +"\n"+ str(pos.x)
    + "\n"+ str(pos.y) +"\n"+str(pos.z)
    

fastTravel(pos)


    


