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
def has_empty_cells(puzzle): #Check if no empty cell in the puzzle
    for row in puzzle:
        if 0 in row:
            return True
    return False

def get_box_values(puzzle,i,j): #Retrieve the box values given a cell position
    box_row = i // 3 * 3
    box_col = j // 3 * 3
    return [puzzle[row][col] for row in range(box_row,box_row+3) for col in range(box_col,box_col+3)]

  
def solve_sudoku(puzzle):
      
    solvedPuzzle = puzzle
    possibleSolutions = {}

    #Going through every cell and check if there is an unique solution
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in range(1,10):
                    if num not in puzzle[i] and num not in [puzzle[row][j] for row in range(9)] and num not in get_box_values(puzzle,i,j):
                       possibleSolutions.setdefault((i,j), set()).add(num)
                             

    #Going through the puzzle big boxes and check if any number is the only result for each cell
    for num in range(1,10): 
        for box_pos_i in range(0,7,3):
            for box_pos_j in range(0,7,3):
                for i in range(9):
                    for j in range(9):
                        if (puzzle[i][j] == 0
                             and i in range(box_pos_i,box_pos_i+3) 
                            and j in range(box_pos_j,box_pos_j+3) 
                            and num not in puzzle[i] 
                            and num not in [puzzle[row][j] for row in range(9)] 
                            and num not in get_box_values(puzzle,i,j)):
                            possibleSolutions.setdefault((i,j), set()).add(num)
    
    print(possibleSolutions)
             
                                
        # #Going through the puzzle rows and check if any number is the only result for each cell
        # for number in range(1,10):
        #     for i,row in enumerate(solvedPuzzle):
        #         for j,cell in enumerate(row):
        #             if check_solutions(solvedPuzzle,cell,number,row,i,j):
        #                 solutions.append([i,j])

        # #Going through the puzzle columns and check if any number is the only result for each cell
        # for number in range(1,10):
        #     for col in range(0,9):
        #         for i,row in enumerate(solvedPuzzle):
        #             for j,cell in enumerate(row):
        #                 if j == col and check_solutions(solvedPuzzle,cell,number,row,i,j):
        #                         solutions.append([i,j])


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

solve_sudoku(puzzle)