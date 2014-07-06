__author__ = 'Taimoor Chatha'
#!/usr/bin/env python3

import sys
import random
import math
from datetime import datetime
import itertools
import copy

from itertools import product

def prompt():
    print "Pick an n for your n^2 x n^2 board."
    print "Warning: Larger n's might mean boards will be developed by the time you're dead."
    print "You want to see it solved don't ya?"

    while True:
        try:
            n = int(raw_input("Enter an n:"))
            if(1<=n<=3):
                print "Should be snappy!"
            else:
                print "Gonna have to give me a minute..."
            break
        except ValueError:
            print("That's not a number!")


    print n, "is your n!"

    print "How hard do you want your sudoku to be?"
    print "1.Hard"
    print "2.Medium"
    print "3.Easy"

    while True:
        try:
            difficulty = int(raw_input("Enter 1,2,3:"))
            if difficulty == 1:
                print "Playing it dangerous. You chose 1. Hard"
                difficulty = "H"
                break
            elif difficulty == 2:
                print "Taking it one step at a time. You chose 2. Medium"
                difficulty = "M"
                break
            elif difficulty == 3:
                print "We all have to start somewhere. You chose 3. Easy"
                difficulty = "E"
                break

        except ValueError:
            print "Invalid Option, choose option 1, 2, or 3!"

    return n, difficulty

def generator(n):

    #Keep in mind that 17 is the minimum amount of cells given that will
    #return a unique solution, for a 9x9 grid. That means around 21%
    #is the cutoff line for general. I hope that's the case at least.
    #I should probably up that number to 25% for boards bigger than 16x16
    #just to make sure.
    MyList = list(range(1, n*n +1))

    random.shuffle(MyList)
    row1 = ""
    banned = []
    for i in MyList:

        if i not in banned:
            row1 += str(i) + " "
            banned.append(i)

    random.shuffle(MyList)
    grid = [[0 for x in xrange(n*n)] for x in xrange(n*n)]
    count = 0
    randomspots = []
    for i in range(len(grid)):
        randomspots.append((random.choice((range(len(grid)))), random.choice((range(len(grid))))))

    random.shuffle(randomspots)
    for i in range(len(grid)):
        grid[randomspots[i][0]][randomspots[i][1]] = MyList[i]
        count += 1
    random.shuffle(MyList)
    test = copy.deepcopy(MyList)
    for i in test:
        if isValid(grid, i, 0, test.index(i)):
            grid[0][test.index(i)] = i



    # print toString(grid)


    row1 += "\n"
    # print grid
    # print grid[0]
    #grid[i] is the row number i.

    for x in xrange(n*n-1):
        for y in xrange(n*n):
            row1 += ". "
        row1+= "\n"

    stringGrid = ""
    for i in grid:
        line = ""
        for s in i:
            line += str(s) + " "

        #print line
        stringGrid+= line + "\n"
    #basic backtracking to generate a board
    #
    # recSolve(grid)
    # print toString(grid)
    # print "---"
    recSolve(grid)
    print toString(grid)


    # print "test:"
    # print stringGrid
    return grid

def altGenrator(n):

    #Keep in mind that 17 is the minimum amount of cells given that will
    #return a unique solution, for a 9x9 grid. That means around 21%
    #is the cutoff line for general. I hope that's the case at least.
    #I should probably up that number to 25% for boards bigger than 16x16
    #just to make sure.
    MyList = list(range(1, n +1))

    random.shuffle(MyList)
    row1 = ""
    banned = []
    for i in MyList:

        if i not in banned:
            row1 += str(i) + " "
            banned.append(i)




    random.shuffle(MyList)
    grid = [[0 for x in xrange(n)] for x in xrange(n)]
    count = 0

    # randomspots = []
    # while count < n:
    #     X, Y = random.choice((range(n))), random.choice((range(n)))
    #     print (X,Y)
    #     if (X,Y) not in randomspots:
    #         print "yes"
    #         randomspots.append((X,Y))
    #         count += 1
    # count = 0
    # print randomspots
    #
    # random.shuffle(randomspots)
    # for i in range(len(grid)):
    #     print randomspots[i][0], ",", randomspots[i][1]
    #     grid[randomspots[i][0]][randomspots[i][1]] = MyList[i]
    #     count += 1
    random.shuffle(MyList)
    test = copy.deepcopy(MyList)
    for i in test:
        grid[0][test.index(i)] = i



    print toString(grid)


    row1 += "\n"
    # print grid
    # print grid[0]
    #grid[i] is the row number i.

    for x in xrange(n-1):
        for y in xrange(n):
            row1 += ". "
        row1+= "\n"

    stringGrid = ""
    for i in grid:
        line = ""
        for s in i:
            line += str(s) + " "

        #print line
        stringGrid+= line + "\n"
        #basic backtracking to generate a board
    #
    # recSolve(grid)
    # print toString(grid)
    # print "---"
    evenRecSolve(grid)
    print toString(grid)


    # print "test:"
    # print stringGrid
    return grid

def evenRecSolve(grid, r= 0, c = 0):

    while r < len(grid)-1:
        if grid[r][c] != 0:
            c += 1
            if c == len(grid):
                c = 0
                if r+1 != len(grid):
                    r += 1
        else:
            break
    if r == len(grid)-1:
        c = 0
        while c < len(grid):
            if grid[r][c] != 0:
                c+=1
            else:
                break

    for x in xrange(1, len(grid)+1):
        if isEvenValid(grid, x, r, c):
            grid[r][c] = x

            if evenRecSolve(grid, r, c):
                return True

            grid[r][c] = 0
    if r == len(grid)-1:

        return True

    return False

#Note: Need to fix the in nxn grid. Also need to fix why sometimes it doesn't go through
#Also work more on generator:
#We need to apply to 3x3. Make sure same thing works
#Also need to figure out how to vary difficulty
#1.Fix the dots, because I am getting some even now.
#once I fix that, I'll probably fix the nxn grids much easier.
#2.Fix the nxn.
#3.Vary difficulty, so actually removing clues etc. Make it symmetric?

#4/18 worked for 4.5 hours ish.

def recSolve(grid, r =0, c = 0):
#--------------



    while r < len(grid)-1:
        if grid[r][c] != 0:
            c += 1
            if c == len(grid):
              c = 0
              if r+1 != len(grid):
                r += 1
        else:
            break
    if r == len(grid)-1:
        c = 0
        while c < len(grid):
            if grid[r][c] != 0:
                c+=1
            else:
                break

    for x in xrange(1, len(grid)+1):
        if isValid(grid, x, r, c):
            grid[r][c] = x

            if recSolve(grid, r, c):
                return True

            grid[r][c] = 0
    if r == len(grid)-1:

        return True

    return False


def checkAll(grid, num):
    x,y = 0,0
    while x<len(grid):
        while y < len(grid):
            if isValid(grid, num, x, y):
                return "Yup"
            y+=1
        x+=1


def findBlank(grid):
    for i in grid:
        for j in i:
            if j == 0:
                return True
    return False
#so grid[0] returns first row.
#so to check an entire column, we need a static j. and a rotating
#row number. so grid[i][static]
def inRow(grid, num, rowNum):
    for i in grid[rowNum]:

       if i == num:
            return True
    else:
        return False


def inCol(grid, num, colNum):
    for c in grid:

        if c[colNum] == (num):
            return True

    return False


def inEvenPanel(grid, startRow, startCol, num):
    for row in xrange(0, 2):
        for col in xrange(0, len(grid)/2):
            if grid[row+startRow][col+startCol] == num:

                return True
    return False

def inNGrid(grid, startRow, startCol, num):

    for row in xrange(0, int(math.sqrt(len(grid)))):
        for col in xrange(0, int(math.sqrt(len(grid)))):
            if grid[row+startRow][col+startCol] == num:

                return True

    return False


def isEvenValid(grid, num, x, y):

    if inRow(grid, num, x):
        return False
    if inCol(grid, num, y):
        return False



    if inEvenPanel(grid, (x-x % 2), (y-(y % (len(grid)/2))), num):
        return False
        #print num, "is in neither row or columns or square"
    return True


def isValid(grid, num, x, y):

    if inRow(grid, num, x):
        return False
    if inCol(grid, num, y):
        return False
    if inNGrid(grid, (x-x % (int(math.sqrt(len(grid))))), (y-y % int((math.sqrt(len(grid))))), num):
        return False
        #print num, "is in neither row or columns or square"
    return True

def toString(grid):
    stringGrid = ""
    for i in grid:
        line = ""
        for s in i:
            line += str(s) + " "

        #print line
        stringGrid+= line + "\n"
    return stringGrid

# def createEvenPuzzle(grid, difficulty):
#     #Amount of givens per level: Easy = Range(36-60) hints given, Medium= Range(32-35) hints given, Hard = Range(31-22) hints given
#     #Lower bound of given cells in each row and column: Easy = 5,4; Medium = 3; Hard = 2-0
#
#     if difficulty == "H":
#         givens = random.choice(range(int(math.ceil(.30*(len(grid)**2))), int(math.ceil(.41*(len(grid)**2)))))
#         lowerBound = (0,int(math.ceil(.25*(len(grid)))))
#     elif difficulty == "M":
#         givens = random.choice(range(int(math.ceil(.43*(len(grid)**2))), int(math.ceil(.45*(len(grid)**2)))))
#         lowerBound = (int(math.ceil(.25(len(grid)))), int(math.ceil(.46*(len(grid)))))
#     elif difficulty == "E":
#         givens = random.choice(range(int(math.ceil(.46*(len(grid)**2))), int(math.ceil(.80*(len(grid)**2)))))
#         lowerBound = ((int(math.ceil(.46*(len(grid)))), int(math.ceil(.58*(len(grid))))))
#
#     origGrid = copy.deepcopy(grid)
#     testGrid = copy.deepcopy(grid)
#
#
#     digRow = {}
#     digCol = {}
#     for i in range(len(grid)):
#         digRow[i] = 0
#         digCol[i] = 0
#
#
#
#     elements = list(itertools.product(range(len(grid)), range(len(grid))))
#     #list of all possible digging options
#     digged = []
#     nodig = []
#
#     solutions = []
#     print len(testGrid)**2 - givens
#     while len(digged) < (len(testGrid)**2 - givens) or len(elements) > 0:
#         print len(digged)
#
#         location = random.choice(elements)
#         if digCol[location[1]] < lowerBound[1] and digRow[location[0]] < lowerBound[1]:
#
#             save = testGrid[location[0]][location[1]]
#
#
#             testGrid[location[0]][location[1]]= 0
#             testGrid2 = copy.deepcopy(testGrid)
#             counter = 0
#
#
#
#             while len(solutions) < 2 and counter < 100:
#                 evenRecSolve(testGrid2)
#                 finishGrid = copy.deepcopy(testGrid2)
#                 if len(solutions) == 0:
#                     solutions.append(finishGrid)
#                 if solutions[0] != finishGrid:
#                     solutions.append(finishGrid)
#
#                     #Need to fix this: So we need to check prevous solutions to newer ones. If the previous
#                     #ones don't match the newer ones, we won't get specific results.
#                     #Fix it, by incorporating previous solutions.Too tired to figure it out now.
#                 counter += 1
#             if len(solutions) == 1:
#                 # digRow[location[0]] += 1
#                 # digCol[location[1]] += 1
#                 elements.remove(location)
#                 digged.append(location)
#             else:
#                 testGrid[location[0]][location[1]] = save
#                 solutions.pop()
#                 elements.remove(location)
#                 nodig.append(location)
#
#
#
#
#
#     return testGrid
def createPuzzle(grid, difficulty):
    #Amount of givens per level: Easy = Range(36-60) hints given, Medium= Range(32-35) hints given, Hard = Range(31-22) hints given
    #Lower bound of given cells in each row and column: Easy = 5,4; Medium = 3; Hard = 2-0

    if difficulty == "H":
        givens = random.choice(range(int(math.ceil(.25*(len(grid)**2))), int(math.ceil(.41*(len(grid)**2)))))
        lowerBound = (0,int(math.ceil(.25*(len(grid)))))
    elif difficulty == "M":
        givens = random.choice(range(int(math.ceil(.42*(len(grid)**2))), int(math.ceil(.45*(len(grid)**2)))))

    elif difficulty == "E":
        givens = random.choice(range(int(math.ceil(.46*(len(grid)**2))), int(math.ceil(.75*(len(grid)**2)))))
        lowerBound = ((int(math.ceil(.46*(len(grid)))), int(math.ceil(.58*(len(grid))))))

    origGrid = copy.deepcopy(grid)
    testGrid = copy.deepcopy(grid)

    #so we need to remove values
    #We also need to randomize the selection of cells. We need to keep track of cells we removed
    #There are 81 potential values to remove. So we take n^4 - givens.
    #We also need to check the lower bound is met.
    #So, we can randomly choose a lower bound for each row, and column
    #So at each spot, check first: How many more empty spots are needed. If empty spots != n^4-givens, then move on
    #Check lower bounds for current row and column
    #Should have a dictionary that links each row, and column with a tuple that has lower bound
    #and also the current total of givens in that row/column.
    #Have a list of tuples that say which spots are digged
    #Have a list of tuples that say which spots cannot be digged because they give multiple solutions
    #If lower bound is reached for column
    #move on to the next column
    #If lower bound is reached for row
    #can't dig, move element to nodig
    #So remove the hole at random spot: x,y
    #Rec Solve, first one should not be a problem
    #We need to check this a lot of times. I'm going to make it 100, and increase ti from there.
    #Add the solutions to a list.
    #Restrict it so duplicate solutions are not added to the same list
    #If there is more than 1 solutoin in the array, then we cannot dig this hole.
    #If we get a case like that, add random spot x,y to the banned list
    #Move on to the next column
    #len(grid) == n^2(will change for different sudokus)



    digRow = {}
    digCol = {}
    for i in range(len(grid)):
            digRow[i] = 0
            digCol[i] = 0



    elements = list(itertools.product(range(len(grid)), range(len(grid))))
    #list of all possible digging options
    digged = []
    nodig = []

    solutions = []
    while len(elements) != givens:


        random.shuffle(elements)
        location = elements.pop()
        save = testGrid[location[0]][location[1]]


        testGrid[location[0]][location[1]]= 0
        digged.append(location)

    return testGrid


def main():
    info = prompt()


if __name__ == "__main__":
    main()


