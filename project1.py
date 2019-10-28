#eight puzzle solver
import random
import copy
from collections import deque

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
"3": [[7,6,2],
      [5,0,1],
      [4,3,8]],
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

#make the specified move and return as a new node
def move(n,direction):
    #check for illegal moves
    if direction not in ops:
        return False
    max_size = len(n.puzzle.puzzle) - 1
    if (direction == 'up' and n.puzzle.zero[0] == 0) or (direction == 'down' and n.puzzle.zero[0] == max_size) or (direction == 'left' and n.puzzle.zero[1] == 0) or (direction == 'right' and n.puzzle.zero[1] == max_size):
        return False
    #perform move and return as a new node
    x = n.puzzle.zero[0]
    y = n.puzzle.zero[1]
    new_steps = copy.deepcopy(n.steps)
    new_steps.append(direction)
    new_puzzle = Puzzle(copy.deepcopy(n.puzzle.puzzle))
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
    return Node(new_puzzle, new_steps)
            
def UniformCostSearch(n):
    visited = deque([])
    leaves = deque([])
    while(not n.puzzle.solved()):
        visited.append(copy.deepcopy(n.puzzle.puzzle))
        for o in ops:
            s = move(n,o)
            if s and s.puzzle.puzzle not in visited:
                leaves.append(copy.deepcopy(s))
        leaves = deque(sorted(leaves, key=lambda x: len(x.steps), reverse=False))
        n = leaves.popleft()
    print("goal state reached in " + str(len(n.steps)) + " steps:\n",n.steps)
    
#def AStarMisplacedTile(root):
    

#def AStarManhattan(root):
    
    

#run the program, collect user input
print("Welcome to Nathan Mueller's 8-puzzle solver.")

p = Puzzle(puzzles[str(random.randint(0,3))])
if input("Type '1' to use a default puzzle, or '2' to enter your own.\n") == "2":
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

print("Puzzle is: ")
p.print()

algo_choice = input("Enter your choice of algorithm\n   1. Uniform Cost Search\n   2. A* with the Misplaced Tile heuristic\n   3. A* with the Manhattan distance heuristic\n")

if algo_choice == "1":
    UniformCostSearch(Node(p,[]))
'''
if algo_choice == "2":
    AStarMisplacedTile(Node(p,[]))
if algo_choice == "3":
    AStarManhattan(Node(p,[]))
'''
