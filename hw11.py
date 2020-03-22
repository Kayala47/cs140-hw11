import sys

# open up infile and read data in

#infileName = sys.argv[1]
infileName = "infile.txt"
#outfileName = sys.argv[2]
outfileName = "outfile.txt"

infile = open(infileName, 'r')

data = infile.read()
#this is one text string with all data


blocks = data.split("\n")  # split every line

# trim the first and last elements off
del blocks[0]
del blocks[len(blocks) - 1]

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

towerList = []

# blockList refers to sorted blocks


def stack(blockList, outfile):
    # this displays the solutions we got before
    totalHeight = 0

    (firstBlock, totalHeight) = stackP(
        [float("inf"), float("inf"), 0], sortedBlocks, towerList, totalHeight, blockList)

    towerList.reverse()  # this now contains the solution

    outfile = open(outfileName, 'w')
    outfile.write(str(totalHeight))
    outfile.write("\n")

    for block in towerList:
        outfile.write(str(block))
        outfile.write("\n")

    print("The tallest tower has " + str(len(towerList)) + " blocks and a height of " + str(totalHeight))
    outfile.close()
    
#defining terms here
def stackP(startBlock, blockList,towerList, totalHeight, canStackList):

    # totalHeight += startBlock[2]

    # print("startBlock = " + str(startBlock))
    
    #returns tuple: (selectedBlock, height added by selectedBlock)
    #print("blocklist = " + str(blockList))
    if (len(canStackList) > 0): 

        #here, we check every member of the canStackList
        newCanStackList = []

        #currentBlock = canStackList[iterNum] if canStackList[iterNum] != None else [0,0,0]
        #for each block, we need to make a can stack list
        #print("blocklist length = " + str(len(blockList)))
        for block in blockList:
            # print("block = " + str(block))
            # print(str(startBlock[0] > block[0]) + ": startBlock length > block length. startBlock = " + str(startBlock) + ", block = " + str(block))
            # print(str(startBlock[1] > block[1]) + ": startBlock width > block width. startBlock = " + str(startBlock) +  ", block = " + str(block))
            if (startBlock[0] > block[0]):
                print(startBlock[0])
                print(block[0])
                print("pass [0]")
                if (startBlock[1] > block[1]):
                    print(startBlock[1])
                    print(block[1])
                    print("pass [1]")
                    if (block not in towerList):
                        print(block not in towerList)
                        print("pass block not in tower list")
                # print("both were true")
                        newCanStackList.append(block)
                # print("block appended = " + str(block))

            #then, we run stackP on each element that many times
            # print("new can stack list = " + str(newCanStackList))
        maxHeightAdded = 0

        if len(canStackList) > 0:
            

            dynamicTable = []
            
            for block in canStackList:

            #the goal of this for loop is to go through the blocks that
            #can be stacked on our starting block, and finding the best
            #one to add, by looking recursively through the options

            #get the height that it would add, save it to a running variable,
            #then compare that to the next block so that you get the block
            #that adds the most height

            #for each block, get its height
                heightAdded = block[2]
                #this is the ht that each block adds

                # print("len of new csl = " + str(len(newCanStackList)))
                # print("new can stack list = " + str(newCanStackList))

                (selectedBlock, heightIfChooseThis) = stackP(block, newCanStackList, towerList, totalHeight + heightAdded, newCanStackList)

                if (selectedBlock not in towerList and startBlock[0] > selectedBlock[0] and startBlock[1] > selectedBlock[1]):
                    dynamicTable.append((selectedBlock, heightIfChooseThis))
                
            
            currentMax = canStackList[0][2]
        
            bestBlock = canStackList[0]
            print("best Block at allocation = " + str(bestBlock))
            # print("current max1 =" + str(currentMax))
            #now goes through dynamic table and picks the best one to adds
            for (block, possibleHeight) in dynamicTable:
                
                print(block, possibleHeight)
                # print("current max2 =" + str(currentMax))
                if possibleHeight > currentMax:
                    # print("current max3 =" + str(currentMax))
                    bestBlock = block
                    currentMax = possibleHeight
            
            if (bestBlock not in towerList):
                if (startBlock[0] > bestBlock[0]):
                    if (startBlock[1] > bestBlock[1]):
                        towerList.append(bestBlock)
                        print("stacked " + str(bestBlock) + " on the tower")
                
            
            # print("bestBlock = " + str(bestBlock))
            # print(blockList)
            #blockList.remove(bestBlock)
            #towerList.append(startBlock)
            # print("dynamic table so far = " + str(dynamicTable))
            #towerList.append(bestBlock)
            totalHeight += currentMax

            return (selectedBlock, totalHeight)
            #find the best and choose that for the next step
        
    else:
        #base case, we've checked everything, so just return empty
        return (startBlock, totalHeight)

stack(sortedBlocks,outfileName)
