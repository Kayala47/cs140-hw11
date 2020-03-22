# cs140-hw11 #

## Compiling ##

You can use the command line to CD into the file holding the Python document and then run the program through the command line by typing "python hw11.py infile.txt outfile.txt". The output will be shown on the command line and the solution will be written to the outfile which you can open after having run the code. 

## Algorithm ## 

The algorithm we implemented follows a dynamic programming model, where the optimal solution can be defined in terms of the optimal solutions to subproblems, which overlap with one another. 
The optimal substructure of our algorithm is evident because by looking at our stack and stackP functions, it is possible to see that we first solve the "subproblem:" finding all possible ways to stack the blocks, to then arrive at the optimal solution: the best possible way to stack the blocks (according to biggest height). 
Our algorithm also incorporates a recursive element (recursive definition), in which the program recursively calls stackP in order to iterate to eventually find the optimal solution. The recrusive definition of our optimal solution would be: optimal solution = max height(all possible towers to build). 
Our dynamic programming table holds these said possible tower solutions, and is filled out by looking at each block one by one and building a respective tower (left to right), and then moving down the table as more towers are built, to eventually find the most optimal tower somewhere in the table.... where is the location of the solution? 

1a) optimal substructure: optimal solutions to the problem
incorporate optimal solutions to related subproblems
¤ convince yourself that there is optimal substructure
1b) recursive definition: use this to recursively define the
value of an optimal solution
2) DP solution: describe the dynamic programming table:
¤ size, initial values, order in which it’s filled in, location of
solution


The program has two main functions, stack and stackP, which perform the main recursive operations in dynamic programming. In this block problem, these include creating a dynamic table which holds all the possible solutions, and then having the program select the max height solution possible. It uses a list called canStackList to hold all the possible blocks you can stack on top of the startingBlock. This canStackList holds these blocks as tuples, which has the dimensions of the block as well as the corresponding height. This way, the program can select the appropriately fitting block, but also the block that maximizes height. 

## Running Time ##

Our program's expected running time is 

 ## How we tested our code ## 

