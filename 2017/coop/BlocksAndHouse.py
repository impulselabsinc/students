
#DO NOT TOUCH ANYTHING IN HERE
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


currentPosition = mc.player.getTilePos()
# DO NOT TOUCH ANYTHING UP HERE












#mc.setBlock(  currentPosition.x,  currentPosition.y+10  ,  currentPosition.z  ,  block.WATER_FLOWING.id  )
#UNCOMMENT THE  LINE ABOVE THIS (DELETE THE HASHTAG)

#What part of the code affects what block is being placed?
#If block.LAVA_FLOWING.id is lava, how do I make lava appear above me?




#try it yourself! Make Lava appear above your head
#place your code between here



#place your code between here



#REMEMBER TO ADD THE HASH SYMBOLS BACK ONCE YOU ARE DONE.






















#Now that we know how to make a block appear, let's try to make a tower appear




#mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+5,  currentPosition.y+10  ,currentPosition.z  ,block.GOLD_ORE.id )
#UNCOMMENT THE LINE ABOVE THIS(DELETE THE HASHTAG)



#Try to understand what is happening
#We are saying that between currentPositionY and currentPositionY+10 place a series of Gold Ore Blocks.
#The X value and the Z value don't change, so nothing is being put between them.
#WHEN YOU ARE DONE ADD THE HASHTAG BACK
























#try it yourself! Make a rectangle, it takes only one setBlocks ( hint: the z-axis isn't changing, only the x and y are.)



#(remember, our x,y, and z  are currentPosition.x,currentPosition.y,currentPosition.z)
#place your code between here



#place your code between here


























#If you have finished the tower, then it is time to try to make a wall

#mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z  ,block.GOLD_ORE.id )
#UNCOMMENT THE LINE ABOVE THIS(DELETE THE HASHTAG)



#As you can see the code is very similar except for one thing
# We changed the ""Ending X"" to currentPosition.x+15, so we are saying that between currentPosition.x+5 and currentPosition,x+15 place a line of gold blocks, AND
#within currentPosition.y, and currentPosition+10, place gold blocks as well.

#ADD THE HASHTAG BACK ONCE YOU ARE DONE.




























#Now that we have a wall let's try to set up the four walls of a house.

#mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z  ,block.GOLD_ORE.id )
#mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z+10,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )
#mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+5,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )
#mc.setBlocks(currentPosition.x+15,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )
#UNCOMMENT THE LINES ABOVE THIS(DELETE THE HASHTAG)

##Can you figure out how to add a roof?
## Here is a hint! it is a square on top of everything
## Try to figure it out on your own


#Add this to the last four lines!!( don't forget to take off the hashtag.)
#mc.setBlocks(currentPosition.x+5,  currentPosition.y+10,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )


