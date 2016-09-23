importmcpi.mincraftasmincraft
importmcpi.block
mc=mincraft.mincraft.create()
pos=mc.player.gettilepos()
x=pos.x+1
y=pos.y
z=z+1
mc.setblock(x,y,z,tnt)
