#eight puzzle solver
import random

#some useful globals
ops = ['up','down','left','right']
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]
puzzles = {
"0": [[1,2,3],
      [4,0,6],
      [7,5,8]],
"1": [[1,2,3],
      [0,4,6],
      [7,5,8]],
"2": [[1,8,2],
      [0,4,3],
      [7,6,5]],
"3": [[2,6,1],
      [0,7,8],
      [3,5,4]],
"impossible": [[1,2,3],
            [4,5,6],
            [8,7,0]]
}

#Puzzle class holds current arrangement of nummbers and the position of the zero
class Puzzle:
    def __init__(self, startPostition):
        self.puzzle = startPostition
        for i in range(len(startPostition)):
            for j in range(len(startPostition[i])):
                if startPostition[i][j] == 0:
                    self.zero = [i,j]
    
    def solved(self):
        return self.puzzle == goal
        
    def print(self):
        for i in range(len(self.puzzle)):
            print(self.puzzle[i])
        print('\n')

#each Node represents a current state of the puzzle and the steps used to get there
class Node:
    def __init__(self, puzzle, steps):
        self.puzzle = puzzle
        self.steps = steps
        
    def move(self,direction):
        #check for illegal moves
        if direction not in ops:
            return False
        if (direction == 'up' and self.puzzle.zero[0] == 0) or (direction == 'down' and self.puzzle.zero[0] == len(self.puzzle)) or (direction == 'left' and self.puzzle.zero[1] == 0) or (direction == 'right' and self.puzzle.zero[1] == len(self.puzzle)):
            return False
        #perform move and return as a new node
        x = self.puzzle.zero[0]
        y = self.puzzle.zero[1]
        new_steps = self.steps
        new_puzzle = self.puzzle
        if direction == 'up':
            new_puzzle.puzzle[x][y], new_puzzle.puzzle[x-1][y] = new_puzzle.puzzle[x-1][y], new_puzzle.puzzle[x][y]
            new_puzzle.zero = [x-1,y]
        if direction == 'down':
            new_puzzle.puzzle[x][y], new_puzzle.puzzle[x+1][y] = new_puzzle.puzzle[x+1][y], new_puzzle.puzzle[x][y]
            new_puzzle.zero = [x+1,y]
        if direction == 'left':
            new_puzzle.puzzle[x][y], new_puzzle.puzzle[x][y-1] = new_puzzle.puzzle[x][y-1], new_puzzle.puzzle[x][y]
            new_puzzle.zero = [x,y-1]
        if direction == 'right':
            new_puzzle.puzzle[x][y], new_puzzle.puzzle[x][y+1] = new_puzzle.puzzle[x][y+1], new_puzzle.puzzle[x][y]
            new_puzzle.zero = [x,y+1]
        return Node(new_puzzle, new_steps.append(direction))
            

#def AStarMisplacedTile():

#def UniformCostSearch():
    

#run the program, collect user input
print("Welcome to Nate Mueller's 8-puzzle solver.")
p = Puzzle(puzzles[str(random.randint(0,3))])
puzzle_choice = input("Type '1' to use a default puzzle, or '2' to enter your own.\n")
#if 2 then create a new puzzle
if puzzle_choice == "2":
    print("Enter your puzzle, using a zero to represent the blank. " +
    "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +
    "the numbers with a space. RET only when finished." + '\n')
    puzzle_row_one = input("Enter the first row: ")
    puzzle_row_two = input("Enter the second row: ")
    puzzle_row_three = input("Enter the third row: ")
    puzzle_row_one = puzzle_row_one.split()
    puzzle_row_two = puzzle_row_two.split()
    puzzle_row_three = puzzle_row_three.split()
    for i in range(0, 3):
        puzzle_row_one[i] = int(puzzle_row_one[i])
        puzzle_row_two[i] = int(puzzle_row_two[i])
        puzzle_row_three[i] = int(puzzle_row_three[i])
    p = Puzzle([puzzle_row_one, puzzle_row_two, puzzle_row_three])

algo_choice = input("Enter your choice of algorithm\n   1. Uniform Cost Search\n   2. A* with the Misplaced Tile heuristic\n   3. A* with the Manhattan distance heuristic\n")



'''
#some tests
p = Puzzle(puzzles['0'])
n1 = Node(p,[])
n1.puzzle.print()
n2 = n1.move('left')
n2.puzzle.print()
n3 = n2.move('up')
n3.puzzle.print()
n4 = n3.move('up')
n4.puzzle.print()
print(n4.steps)
'''
