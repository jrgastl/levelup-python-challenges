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
def check_if_solved(solved_puzzle):
    solved = True
    for row in solved_puzzle:
        for cell in row:
            if cell == 0:
                solved = False
    return solved

def get_column(puzzle,j_cell):
    return [cell for row in puzzle for l_cell,cell in enumerate(row) if l_cell == j_cell]

def get_box(puzzle,i_row,j_cell):
    rows = [row for k in range(0,3,9) for row in puzzle[k:k+3] if i_row in range(k,k+3) ]        
    box = [cell for l in range(0,3,9) for row in rows for cell in row[l:l+3] if j_cell in range(l,l+3) ]
    return box
    
def solve_sudoku(puzzle):
    solved_puzzle = puzzle
    buffer = []
    while check_if_solved(solved_puzzle) == False:
        for i_row,row in enumerate(solved_puzzle):
            for j_cell, cell in enumerate(row):
                if cell == 0:
                    for number in range(1,10):
                        if number not in row and number not in get_column(solved_puzzle,j_cell) and number not in get_box(solved_puzzle,i_row,j_cell):
                            buffer.append(number)
                            if len(buffer) == 1:
                                row[j_cell] = number
                                solved_puzzle.append(row)
                                buffer = []
                            else:
                                buffer = []
    return solved_puzzle


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(solve_sudoku(puzzle))