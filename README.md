# cs140-hw11 #

## Compiling ##

You can use the command line to CD into the file holding the Python document and then run the program through the command line by typing "python hw11.py infile.txt outfile.txt". The output will be shown on the command line and the solution will be written to the outfile which you can open after having run the code. 

## Algorithm ## 

Our algorithm is a DP solution that fills out a table based on how high the tower can reach if we start at a particular block. Our stackDP function fills out this DP table based on repeatedly calling stackDPPrime, which itself finds the tallest tower you can make given a starting block and a list of blocks.

Our method for finding the tallest tower from any given block is as follows:
Make a list of all the blocks that can be stacked on top of our startblock
Find all possible permutations of the above list and iterate through them, making a tower from each permutation and placing it in a list containing all the possible towers that can be built
Find the tallest of those possible towers and report that as the max height tower. 

This algorithm works naively; it doesn’t have to worry about the interaction within several blocks (ie, choosing one block might preclude another taller block from being stacked) because it just tries all possibilities. The key is that it still checks base heights of every block it wants to stack, so it only makes legitimate towers. Due to the large size of the permutations, however, we might expect it to be slower than other algorithms. 

We know that this algorithm is correct because it is able to account for every possible permutation of the blocks and choose the best one, which means we have considered all other possibilities and have found the maximum. Using this method, it shouldn't be possible to find any other solutions that are better.

## Interesting design decision ## 

We struggled to find a recursive implementation that would work, and were similarly stumped about a DP solution because we couldn't figure out a way to make sure that every possibility was accounted for, especially in regards to skipping some blocks in favor of stacking others. Our solution was to make a list of permutations that would allow us to account for every single possibility in ordering of the blocks. This means that we run our block list through a permutation function in order to get all possibilities, then make a tower from each and finally choose the largest tower in order to place that in our DP list. 

## Running Time ##

Our program's expected running time is O(n^2). In stackDPPrime, we use two nested for loops to search for every possible permutation. There is some large constant in front of that because a) we are working with 3x the number of data points given just because of the different orientations and b) trying out every possible permutation means we are sorting through a huge list. 

 ## How we tested our code ## 
 We ran our code through different scenarios which it passed. We were unable to open the testfiles given, as neither of us could find a program to open them with. Through print statements, we were able to interrogate each of our functions separately to make sure that they worked as intended, and we were able to see the process live. 
 
 ## Acknowledgments ## 
 
 We are thankful to Professor Kauchak for his help, especially in helping us realize that our initial sorting of elements was wrong. 

