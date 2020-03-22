import sys

print(sys.argv)

print(sys.argv[1])
print(sys.argv[2])

# open up infile and read data in

infileName = sys.argv[1]
outfileName = sys.argv[2]

infile = open(infileName, 'r')

data = infile.read()
#this is one text string with all data


blocks = data.split("\n")  # split every line

# trim the first and last elements off
del blocks[0]
del blocks[len(blocks) - 1]

print(blocks)

infile.close()


# reorganize blocks into all possible positions

allBlocks = []

for block in blocks:

    dimensions = block.split(" ")

    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    dimensions[2] = int(dimensions[2])

    # 0,1,2  = dimensions, 3 = base area
    allBlocks.append([dimensions[0], dimensions[1], dimensions[
                     2]])
    allBlocks.append([dimensions[1], dimensions[2], dimensions[
                     0]])
    allBlocks.append([dimensions[2], dimensions[0], dimensions[
                     1]])


# now we have a list with all the possible orientations of blocks and
# their respective base areas


# now we have to sort this list from biggest to smallest base
sortedBlocks = sorted(allBlocks, key=lambda x: x[2], reverse=True)


# now we can recursively search the list for paths and find the best
# combination of blocks

dynamicTable = []

# blockList refers to sorted blocks


def stack(blockList, outfile):
    # this displays the solutions we got before
    totalHeight = 0
    iterNum = 0

    (lastBlock, totalHeight) = stackP(
        [float("inf"), float("inf"), 0], sortedBlocks, dynamicTable, totalHeight, blockList)

    dynamicTable.reverse()  # this now contains the solution

    outfile = open(outfileName, 'w')
    outfile.write(str(totalHeight))
    outfile.write("\n")

    for block in dynamicTable:
    	outfile.write(str(block[0:3]))
    	outfile.write("\n")
    outfile.close()
	
#defining terms here
def stackP(startBlock, blockList ,towerList, totalHeight, canStackList):

    totalHeight += startBlock[2]

    #returns tuple: (selectedBlock, height added by selectedBlock)
    #print("blocklist = " + str(blockList))
    if (len(canStackList) > 0): #fix base case

        #here, we check every member of the canStackList
        newCanStackList = []

        #currentBlock = canStackList[iterNum] if canStackList[iterNum] != None else [0,0,0]
        #for each block, we need to make a can stack list
        #print("blocklist length = " + str(len(blockList)))
        for block in blockList:
            print("block = " + str(block))
            print("startBlock = " + str(startBlock))

            print(str(startBlock[0] > block[0]) + ": startBlock length > block length. startBlock = " + str(startBlock) + ", block = " + str(block))
            print(str(startBlock[1] > block[1]) + ": startBlock width > block width. startBlock = " + str(startBlock) +  ", block = " + str(block))
            if (startBlock[0] > block[0] and startBlock[1] > block[1]):
                print("both were true")
                newCanStackList.append(block)

            #then, we run stackP on each element that many times
       
        maxHeightAdded = 0

        if len(canStackList) > 0:
            currentMax = canStackList[0][2]
            bestBlock = canStackList[0]

            for i in range(0, len(canStackList)):

            #the goal of this for loop is to go through the blocks that
            #can be stacked on our starting block, and finding the best
            #one to add, by looking recursively through the options

            #get the height that it would add, save it to a running variable,
            #then compare that to the next block so that you get the block
            #that adds the most height

            #for each block, get its height
                heightAdded = canStackList[i][2]
                #this is the ht that each block adds

                (selectedBlock, heightAddedBySB) = stackP(canStackList[i], blockList, towerList, totalHeight + heightAdded, newCanStackList)

                if (heightAddedBySB > currentMax):
                    currentMax = heightAddedBySB
                    bestBlock = selectedBlock

        print("bestBlock = " + str(bestBlock))
        print(blockList)
        blockList.remove(bestBlock)
        towerList.append(bestBlock)
        totalHeight += currentMax

        return (selectedBlock, selectedBlock[2])
        #find the best and choose that for the next step
        
    else:
        #base case, we've checked everything, so just return empty
        return ([0,0,0], 0)

stack(sortedBlocks,outfileName)
