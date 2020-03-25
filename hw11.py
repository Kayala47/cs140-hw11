import sys
import itertools

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

#this section just makes all the correct orientations
for block in blocks:

    dimensions = block.split(" ")

    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    dimensions[2] = int(dimensions[2])

    # 0,1,2  = l,w,h   
    '''
    allBlocks.append([dimensions[0], dimensions[1], dimensions[
                     2]])
    allBlocks.append([dimensions[1], dimensions[2], dimensions[
                     0]])
    allBlocks.append([dimensions[2], dimensions[0], dimensions[
                     1]])
    '''

    allBlocks.append([dimensions[0], dimensions[1], dimensions[
                     2]])
    allBlocks.append([dimensions[0], dimensions[2], dimensions[
                     1]])
    allBlocks.append([dimensions[1], dimensions[2], dimensions[
                     0]])


    #we weren't sure which orientation was correct. We went with the second

# now we have a list with all the possible orientations of blocks and
# their respective base areas


# now we have to sort this list based on the largest dimension
sortedBlocks = sorted(allBlocks, key= lambda x: (max(x[0],x[1]),x[0], x[1] ), reverse = True)

#returns the largest tower one can create starting with a particular block
#blockList = list of blocks sorted in order of decreasing base
#startBlock = the block to start the tower with
def stackDPPrime(blockList, startBlock):

    canStackList = []

    for block in blockList[blockList.index(startBlock):]:
        if (block[0] < startBlock[0] and block[1] < startBlock[1]):
            canStackList.append(block)

    #the above section creates a list of all the blocks that can be possibly stacked on top of our start block

    print("startBlock is " + str(startBlock) + " and canStackList is " + str(canStackList))

    permutationsList = list(itertools.permutations(canStackList)) #mixes up the blocks to create a list of all possible permutations

    possibleTowers = []

    for perm in permutationsList:
        #for each of the permutations, it creates a tower by stacking all the blocks that can be stacked

        tower = []

        tower.append(startBlock)

        previousBlock = startBlock

        for block in perm:

            if (block[0] < previousBlock[0] and block[1] < previousBlock[1]):

                tower.append(block)
                previousBlock = block

        possibleTowers.append(tower)

        #now, all it has to do is find out which tower was the best and return that
    return findTallestTower(possibleTowers)

#creates a DP table based on the tallest tower that can be built from each starting block in blockList
def stackDP(blockList):

    dynamicTable = []

    for block in blockList:
        #fills out the value for each block

        dynamicTable.append(stackDPPrime(blockList, block))

    #now, it just gets the best tower
    return findTallestTower(dynamicTable)

#this function actually just prints the answer to an outfile
def stack(blockList, outfile):
    # this displays the solutions we got before

    totalHeight = 0

    bestTower = stackDP(blockList)

    howManyBlocks = len(bestTower)

    print("bestTower = " + str(bestTower))

    answer = ""

    for block in bestTower:
        answer += (str(block))
        answer += ("\n")
        totalHeight += block[2]

    outfile = open(outfileName, 'w')
    outfile.write(str(howManyBlocks))
    outfile.write("\n")
    outfile.write(answer)

    print("The tallest tower has " + str(howManyBlocks) + " blocks and a height of " + str(totalHeight))
    outfile.close()

#finds the tower with the biggest height given a list of towers
def findTallestTower(towerList):

    maxHeight = 0
    tallestTower = []

    for tower in towerList:
        towerHeight = 0
        for block in tower:
            if (block != None and len(block) > 1):
                towerHeight += block[2]
            else:
                tower.remove(block)
        
        if towerHeight > maxHeight:
            maxHeight = towerHeight
            tallestTower = tower

    return tallestTower

# print(sortedBlocks)

# stack(sortedBlocks,outfileName)
stack(sortedBlocks, outfileName)
print(stackDP(sortedBlocks))