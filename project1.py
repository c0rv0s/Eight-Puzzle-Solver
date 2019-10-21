#eight puzzle solver
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]
puzzles = {
"easy": [[1,2,3],
       [4,5,6],
       [7,8,0]],
"puzzle2": [[1,2,3],
          [0,4,6],
          [7,5,8]],
"puzzle3": [[1,8,2],
          [0,4,3],
          [7,6,5]],
"puzzle4": [[2,6,1],
          [0,7,8],
          [3,5,4]],
"impossible": [[1,2,3],
            [4,5,6],
            [8,7,0]]
}

print("Welcome to Nate Mueller's 8-puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own.")
puzzle_choice = input()
print("Enter your choice of algorithm\n   1. Uniform Cost Search\n   2. A* with the Misplaced Tile heuristic\n   3. A* with the Manhattan distance heuristic")
algo_choice = input()


