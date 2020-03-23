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


# now we have to sort this list from biggest to smallest length
sortedBlocks = sorted(allBlocks, key=lambda x: x[0], reverse=True)


# now we can recursively search the list for paths and find the best
# combination of blocks



# blockList refers to sorted blocks


def stack(blockList, outfile):
    # this displays the solutions we got before
    totalHeight = 0

    dynamicTable = []

    stackP([float("inf"), float("inf"), 0], sortedBlocks, dynamicTable)

    print("dynamicTable = " + str(dynamicTable))
    bestTower = findTallestTower(dynamicTable)
    print("bestTower = " + str(bestTower))

    answer = ""

    for block in bestTower:
        answer += (str(block))
        answer += ("\n")
        totalHeight += block[2]

    outfile = open(outfileName, 'w')
    outfile.write(str(totalHeight))
    outfile.write("\n")
    outfile.write(answer)

    print("The tallest tower has " + str(len(bestTower)) + " blocks and a height of " + str(totalHeight))
    outfile.close()

def findTallestTower(towerList):

    maxHeight = 0
    tallestTower = []

    for tower in towerList:
        towerHeight = 0
        for block in tower:
            if (block != None):
                towerHeight += block[2]
            else:
                tower.remove(block)
        
        if towerHeight > maxHeight:
            maxHeight = towerHeight
            tallestTower = tower

    return tallestTower
#defining terms here

def stackP(startBlock, blockList, towerList):

    if (len(blockList) < 1):
        return startBlock

    else:

        startIndex = blockList.index(startBlock) + 1 if startBlock != [float("inf"), float("inf"), 0] else 0
        for block in blockList[startIndex:]:

            if (startBlock[0] > block[0] and startBlock[1] > block[1]):
                tower = []
                tower.append(stackP(block, blockList[blockList.index(block) + 1:],towerList))
                print("tower = " + str(tower))
                towerList.append(tower) 

        print("towerList = " + str(towerList))

stack(sortedBlocks,outfileName)
