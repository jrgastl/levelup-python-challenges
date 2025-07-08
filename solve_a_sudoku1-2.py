'''
Briefing:
Create a function to solve a sudoku puzzle.
Input: puzzle
Output: solved puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
'''
def has_empty_cells(puzzle): #Check if there are empty cells in the puzzle
    for row in puzzle:
        if 0 in row:
            return True
    return False

def get_column(puzzle,j): #Retrive the column values given a cell position
    return [row[j] for row in puzzle]

def get_box(puzzle,i,j): #Retrieve the box values given a cell position
    iBox = i // 3 * 3
    jBox = j // 3 * 3
    return [puzzle[i][j] for i in range(iBox,iBox + 3) for j in range(jBox,jBox + 3)]

def check_solutions(puzzle,num,i,j): #Check if the number is a potential solution for that cell
    if num not in puzzle[i] and num not in get_column(puzzle,j) and num not in get_box(puzzle,i,j):
        return True

def solve_sudoku(puzzle):

    solvedPuzzle = puzzle
    while n < 5:
        #Going through the puzzle big boxes and check if any number is the only result for each cell
        for num in range (1,10):
            for iBox in range(0,7,3):
                for jBox in range(0,7,3):
                    solutions = []
                    for i in range(9):
                        for j in range(9):
                            if solvedPuzzle[i][j] == 0:
                                if i in range(iBox,iBox + 3) and j in range(jBox,jBox+3) and check_solutions(solvedPuzzle,num,i,j):
                                    solutions.append([i,j])
                    if len(solutions) == 1:
                        for solution in solutions:
                            solvedPuzzle[solution[0]][solution[1]] = num


        #Going through the puzzle rows and check if any number is the only result for each cell
        for num in range(1,10):
            for i in range(9):
                solutions = []
                for j in range(9):
                    if solvedPuzzle[i][j] == 0 and check_solutions(solvedPuzzle,num,i,j):
                        solutions.append([i,j])
                if len(solutions) == 1:
                    for solution in solutions:
                            solvedPuzzle[solution[0]][solution[1]] = num

        #Going through the puzzle columns and check if any number is the only result for each cell
        for num in range(1,10):
            for col in range(9):
                solutions = []
                for i in range(9):
                    for j in range(9):
                        if j == col and check_solutions(solvedPuzzle,num,i,j):
                                solutions.append([i,j])
                if len(solutions) == 1:
                    for solution in solutions:
                        solvedPuzzle[solution[0]][solution[1]] = num

                    
        #Going through every cell and check possible solutions and adding to a dictionary
        candidates = {}
        for i in range(9):
            for j in range(9):
                if solvedPuzzle[i][j] == 0:
                    solutions = []
                    for num in range(1,10):
                        if check_solutions(solvedPuzzle,num,i,j):
                            solutions.append(num)
                    candidates[(i,j)] = solutions
        for key in candidates.keys():
            if len(candidates[key]) == 1:
                puzzle[key[0]][key[1]] = candidates[key][0]
        for key in candidates.keys():
            for iBox in range(0,7,3):
                for jBox in range(0,7,3):
      

        n += 1
            
    print(solvedPuzzle)
    print(candidates)

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle_master= [[0,4,0,7,2,0,1,0,0],
                 [0,3,0,9,0,0,0,0,0],
                 [6,0,2,0,3,0,8,9,0],
                 [0,0,0,2,0,9,0,0,0],
                 [0,0,3,5,0,0,0,0,0],
                 [9,2,8,0,7,0,6,0,1],
                 [0,0,0,0,0,0,3,0,2],
                 [0,9,0,8,0,0,4,0,0],
                 [0,0,4,0,5,0,0,0,0]]

puzzle_extreme = [[0,5,0,0,8,0,0,6,0],
                 [0,0,1,6,7,0,0,9,0],
                 [0,4,0,0,0,0,0,7,0],
                 [9,0,0,0,2,0,0,8,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,1,0,0,6,0,5,0,0],
                 [0,2,0,0,1,0,3,0,0],
                 [0,0,0,4,0,7,0,0,0],
                 [0,0,4,0,0,2,8,0,0]]

solve_sudoku(puzzle_master)