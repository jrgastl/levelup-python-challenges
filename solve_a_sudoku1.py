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
def check_if_no_empty(solved_puzzle):
    solved = True
    for row in solved_puzzle:
        for cell in row:
            if cell == 0:
                solved = False
    return solved

def get_column(puzzle,j):
    return [cell for row in puzzle for l,cell in enumerate(row) if l == j]

def get_box(puzzle,i,j):
    rows = [row for k in range(0,7,3) for row in puzzle[k:k+3] if i in range(k,k+3)]        
    box = [cell for l in range(0,7,3) for row in rows for cell in row[l:l+3] if j in range(l,l+3)]
    return box
    
def solve_sudoku(puzzle):

    #going through the puzzle big boxes and check if any number is the only result for each cell
    puzzleBoxes = puzzle
    solutions = []
    box=0
    for number in range(1,10):
        for i_box in range(0,7,3):
             for j_box in range(0,7,3):
                for i,row in enumerate(puzzleBoxes):
                    for j, cell in enumerate(row):
                        if i in range(i_box,i_box+3) and j in range(j_box,j_box+3) and cell == 0 and number not in row and number not in get_column(puzzleBoxes,j) and number not in get_box(puzzleBoxes,i,j):
                            solutions.append([i,j])
        #         print(f'for number {number} in box {box} there are {solutions} solutions')
        #         box += 1
        #         solutions = []
        # box = 0
                if len(solutions) == 1:
                    # print(f'{number} and {solutions}')
                    for i,row in enumerate(puzzleBoxes):
                        for j, cell in enumerate(row):
                            for solution in solutions:
                                if solution[0] == i and solution[1] == j:
                                    row[j] = number
                                    solutions = []
                else:
                    solutions = []
    #going through the puzzle rows and check if any number is the only result for each cell
    puzzleRows = puzzleBoxes
    solutions = []
    for number in range(1,10):
        for i,row in enumerate(puzzleRows):
            for j,cell in enumerate(row):
                if i in range(i_box,i_box+3) and j in range(j_box,j_box+3) and cell == 0 and number not in row and number not in get_column(puzzleBoxes,j) and number not in get_box(puzzleBoxes,i,j):
                            solutions.append([i,j])
            # print(f'for number {number} in {i} row there are {solutions} solutions')
            # solutions = []
            if len(solutions) == 1:
                for solution in solutions:
                    if solution[0] == i and solution[1] == j:
                        row[j] = number
                        solutions = []
            else:
                solutions = []
    print(puzzleRows)

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve_sudoku(puzzle)