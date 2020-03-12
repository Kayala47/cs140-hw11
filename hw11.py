import sys

print(sys.argv)

print(sys.argv[1])
print(sys.argv[2])

#open up infile and read data in

infileName = sys.argv[1]
outfileName = sys.argv[2]

infile = open(infileName, 'r')

data = infile.read() #this is one text string with all data


blocks = data.split("\n") #split every line

#trim the first and last elements off
del blocks[0]
del blocks[len(blocks)-1]

print(blocks)

infile.close()


#reorganize blocks into all possible positions

allBlocks = []

for block in blocks:

    dimensions = block.split(" ")
    
    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    dimensions[2] = int(dimensions[2])


    # 0,1,2  = dimensions, 3 = base area
    allBlocks.append([dimensions[0], dimensions[1], dimensions[2], dimensions[0] * dimensions[1]])
    allBlocks.append([dimensions[1], dimensions[2], dimensions[0], dimensions[1] * dimensions[2]])
    allBlocks.append([dimensions[2], dimensions[0], dimensions[1], dimensions[2] * dimensions[0]])


#now we have a list with all the possible orientations of blocks and their respective base areas



#now we have to sort this list from biggest to smallest base
sortedBlocks = sorted(allBlocks, key=lambda x : x[3], reverse=True)
print sortedBlocks


#now we can recursively search the list for paths and find the best combination of blocks

dynamicTable = []

def stack(blockList, currentStack):
    #this adds the best block to the stack
    
    for block in blockList:
        dynamicTable.append(stackP(block))

    maxHeight = 0
    maxBlock = []
    for block in dynamicTable:
        if block[block.len() - 1] > maxHeight:
            maxHeight = block[block.len() - 1]
            maxBlock = block

    #now we have a current maxHeight, which will be added to our currentStack
    currentStack.append(maxBlock)

    return currentStack
        

def stackP(block):
    #finds best combo starting at this block
    #return an array of the blocks chosen with the total height at the end




result = 0
outfile = open(outfileName, 'w')

outfile.write("result")

outfile.close

