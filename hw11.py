import sys

print(sys.argv)

print(sys.argv[1])
print(sys.argv[2])

# open up infile and read data in

infileName = sys.argv[1]
outfileName = sys.argv[2]

infile = open(infileName, 'r')

data = infile.read()  # this is one text string with all data


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
                     2], dimensions[0] * dimensions[1]])
    allBlocks.append([dimensions[1], dimensions[2], dimensions[
                     0], dimensions[1] * dimensions[2]])
    allBlocks.append([dimensions[2], dimensions[0], dimensions[
                     1], dimensions[2] * dimensions[0]])


# now we have a list with all the possible orientations of blocks and
# their respective base areas


# now we have to sort this list from biggest to smallest base
sortedBlocks = sorted(allBlocks, key=lambda x: x[3], reverse=True)


# now we can recursively search the list for paths and find the best
# combination of blocks

dynamicTable = []

# blockList refers to sorted blocks


def stack(blockList, outfile):
    # this displays the solutions we got before

    (lastBlock, totalHeight) = stackP(
        blockList[0], dynamicTable, sortedBlocks, 0)

    dynamicTable.reverse()  # this now contains the solution

    outfile = open(outfileName, 'w')
    outfile.write(str(totalHeight))

    for block in dynamicTable:
    	outfile.write(str(block))
    	outfile.write("\n")
    outfile.close()
	# print out all the blocks, in order

    # return block combo and total height

    '''
    for block in blockList:
        dynamicTable.append(stackP(block))

    maxHeight = 0
    maxBlock = []
    for block in dynamicTable:
        if block[block.len() - 1] > maxHeight:
            maxHeight = block[block.len() - 1]
            maxBlock = block

    # now we have a current maxHeight, which will be added to our currentStack
    currentStack.append(maxBlock)

    return currentStack
    '''
# startBlock is the block we want to place on the bottom
# towerList is our dynamic table
# blockList is our sorted block list


def stackP(startBlock, towerList, blockList, totalHeight):
    # finds best combo starting at this block
    # return an array of the blocks chosen with the total height at the end

    # returns solution in tuple pair, where first part is block and second is
    # height
    canStackList = []

    for block in sortedBlocks:
    	# for each remaining block, find best solution, only looking to the right
    	# of start

    	# recursing through and finding the best solution for each
    	if (startBlock[0] > block[0] and startBlock[1] > block[1]):
    		canStackList.append(block)

    	# at the end, we should have a list of all the blocks that can be stacked

    if (len(canStackList) <= 0):  # base case - no blocks left to stack
    	# we can't add anything else, so that's the max ht
    	return (None, startBlock[2])
    elif(len(canStackList) == 1):
		# second base case - one block left to stack
		# we know that it has to be that block
        return startBlock[2] + canStackList[0][2]
    else:
        # recursion step - call itself to find the most height it can add
        maxSolution = [float("inf"), float("inf"), float("-inf")]
        #best block

        for block in canStackList:
	    	# for each remaining block, find best solution, only looking to the right of start
            (currentBlock, currentHeight) = stackP(block, towerList, blockList, startBlock[2])

            #recursively check each block for biggest height
            if(currentBlock != None):
                totalHeight += currentBlock[2]
            if (totalHeight > maxSolution[2]):
                    maxSolution = currentBlock


	    # generate solution "max" and assign the best possible block to that
        towerList.append(maxSolution) #the list will be reversed
        return (maxSolution, totalHeight)


stack(sortedBlocks,outfileName)
