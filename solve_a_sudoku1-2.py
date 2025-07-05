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


def check_if_solved(solved_puzzle): # Function to check if puzzle is solved
    solved = True
    for row in solved_puzzle: # Loop through the puzzle to find zero
        for cell in row:
            if cell == 0:
                solved = False # If a zero is found the function returns false
    return solved

def get_column(puzzle,j): # Function to get all the cells of a column
    return [cell for row in puzzle for l,cell in enumerate(row) if l == j]

def get_box_values(puzzle,i,j): # Function to get each box of the sudoku table
    rows = [row for k in range(0,9,3) for row in puzzle[k:k+3] if i in range(k,k+3) ] #i and j are the positions of the cell being assessed. As the boxes are 3x3, the loop step i 3.    
    box = [cell for l in range(0,9,3) for row in rows for cell in row[l:l+3] if j in range(l,l+3) ]
    return box

                         
def solve_sudoku(puzzle): # Function to get the solved puzzle 
    solved_puzzle = puzzle
    solutions = []
    for i_box in range(0,7,3):
        for j_box in range(0,7,3):
            for number in range(1,10):
                for i,row in enumerate(solved_puzzle[i_box:i_box+3]):
                    for j,cell in enumerate(row[j_box,:j_box+3]):
                        if cell == 0 and cell != number:
                            if number not in row and number not in get_column(puzzle,j) and number not in get_box_values(puzzle,i,j):
                                solutions.append([i,j])
                if len(solutions) == 1:
                    for solution in solutions:
                        for solved_puzzle[solution[0]] =

                   
                
    print(solved_puzzle)




puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle_2 = [[0,0,0,0,0,2,0,0,0],
            [7,3,0,0,5,0,1,0,0],
            [0,1,0,0,0,0,5,3,0],
            [5,0,0,0,4,0,0,0,0],
            [3,4,2,0,0,0,0,0,0],
            [0,0,0,8,6,0,0,5,0],
            [9,0,0,0,0,1,0,0,0],
            [0,0,0,4,3,0,0,0,6],
            [0,0,0,0,0,0,8,0,0]]

solve_sudoku(puzzle)