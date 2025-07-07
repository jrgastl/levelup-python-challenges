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
def check_if_empty(solved_puzzle): #Check if no empty cell in the puzzle
    solved = False
    for row in solved_puzzle:
        for cell in row:
            if cell == 0:
                solved = True
    return solved

def get_column(puzzle,j): #Retrive the column values given a cell position
    return [cell for row in puzzle for l,cell in enumerate(row) if l == j]

def get_box(puzzle,i,j): #Retrieve the box values given a cell position
    rows = [row for k in range(0,7,3) for row in puzzle[k:k+3] if i in range(k,k+3)]        
    box = [cell for l in range(0,7,3) for row in rows for cell in row[l:l+3] if j in range(l,l+3)]
    return box

def check_solutions(solvedPuzzle,cell,number,row,i,j):
    if cell == 0 and number not in row and number not in get_column(solvedPuzzle,j) and number not in get_box(solvedPuzzle,i,j):
        return True
    
def solve_sudoku(puzzle):
      
    solvedPuzzle = puzzle
    solutions = []
    n = 0

    while n < 30:
        #Going through every cell and check if there is an unique solution
        for i,row in enumerate(solvedPuzzle):
            for j,cell in enumerate(row):
                for number in range(1,10):
                    if check_solutions(solvedPuzzle,cell,number,row,i,j):
                        solutions.append([i,j])
                if len(solutions) == 1:
                    row[j] = number
                    solutions = []
                else:
                    solutions = []
        
        #Going through the puzzle big boxes and check if any number is the only result for each cell
        for number in range(1,10): 
            for box_pos_i in range(0,7,3):
                for box_pos_j in range(0,7,3):
                    for i,row in enumerate(solvedPuzzle):
                        for j, cell in enumerate(row):
                            if i in range(box_pos_i,box_pos_i+3) and j in range(box_pos_j,box_pos_j+3) and check_solutions(solvedPuzzle,cell,number,row,i,j):
                                solutions.append([i,j])
                                
            ## Testing if the code works until here
            #         print(f'for number {number} in box {box} there are {solutions} solutions')
            #         box += 1
            #         solutions = []
            # box = 0

                    if len(solutions) == 1:
                        # print(f'{number} and {solutions}')
                        for i,row in enumerate(solvedPuzzle):
                            for solution in solutions:
                                if i == solution [0]:
                                    row[solution[1]] = number
                                    solutions = []
                    else:
                        solutions = []

        #Going through the puzzle rows and check if any number is the only result for each cell
        for number in range(1,10):
            for i,row in enumerate(solvedPuzzle):
                for j,cell in enumerate(row):
                    if check_solutions(solvedPuzzle,cell,number,row,i,j):
                        solutions.append([i,j])

                ## Checking if the code works until here
                # print(f'for number {number} in {i} row there are {solutions} solutions')
                # solutions = []
                if len(solutions) == 1:
                    # print(f'For number {number} in row {i} there are {solutions}  solutions')
                    for solution in solutions:
                            row[solution[1]] = number
                            solutions = []
                else:
                    solutions = []

        #Going through the puzzle columns and check if any number is the only result for each cell
        for number in range(1,10):
            for col in range(0,9):
                for i,row in enumerate(solvedPuzzle):
                    for j,cell in enumerate(row):
                        if j == col and check_solutions(solvedPuzzle,cell,number,row,i,j):
                                solutions.append([i,j])
                ## Checking if the code works until here
                # print(f'for number {number} in {i} row there are {solutions} solutions')
                # solutions = []
                if len(solutions) == 1:
                    # print(f'For number {number} in row {i} there are {solutions}  solutions')
                    for i,row in enumerate(solvedPuzzle):
                        for solution in solutions:
                            if i == solution[0]:
                                row[solution[1]] = number
                                solutions = []
                else:
                    solutions = []
        n += 1

    print(solvedPuzzle)

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

solve_sudoku(puzzle_extreme)