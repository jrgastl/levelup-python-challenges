'''
So, this was a big challenge for me. I've got stuck on it for days.
I understand that the most "pythonic" solution for it is the backtracking, but the solution from the instructor implements the itertools module as well.
Finally, I left in the first part of the code my attempts to use a logic to solve the problem. If the puzzle is not sovled with the logic, then backtracking is applied.

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
from  collections  import Counter

def match_criteria(i,j,num,puzzle): # Check if number matches the sudoku criteria
    
    if num in [row[j] for row in puzzle]: # If number is already in the same column, return False
        return False
    
    iBox = i // 3 * 3
    jBox = j // 3 * 3
    if num in [puzzle[i][j] for i in range(iBox,iBox + 3) for j in range(jBox,jBox + 3)]: # If number is already in the same box, return False
        return False
    
    if num in puzzle[i]: # If number is already in the same row, return False
        return False

    return True

def backtrack(puzzle):  # Backtracking
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in range(1,10):
                    if  match_criteria(i,j,num,puzzle):
                        puzzle[i][j] = num
                        if backtrack(puzzle):
                            return True
                    puzzle[i][j] = 0
                return False
    return True

def solve_sudoku(puzzle): # Main function
    
    n=  0
    while n < 5:
        # Going through the puzzle big boxes and check if any number is the only result for each cell
        for num in range (1,10):
            for iBox in range(0,7,3):
                for jBox in range(0,7,3):
                    solutions = []
                    for i in range(9):
                        for j in range(9):
                            if puzzle[i][j] == 0:
                                if i in range(iBox,iBox + 3) and j in range(jBox,jBox+3) and match_criteria(i,j,num,puzzle):
                                    solutions.append([i,j])
                    if len(solutions) == 1:
                        for solution in solutions:
                            puzzle[solution[0]][solution[1]] = num

        # Going through the puzzle rows and check if any number is the only result for each cell
        for num in range(1,10):
            for i in range(9):
                solutions = []
                for j in range(9):
                    if puzzle[i][j] == 0 and match_criteria(i,j,num,puzzle):
                        solutions.append([i,j])
                if len(solutions) == 1:
                    for solution in solutions:
                            puzzle[solution[0]][solution[1]] = num

        # Going through the puzzle columns and check if any number is the only result for each cell
        for num in range(1,10):
            for col in range(9):
                solutions = []
                for i in range(9):
                    for j in range(9):
                        if j == col and match_criteria(i,j,num,puzzle):
                                solutions.append([i,j])
                if len(solutions) == 1:
                    for solution in solutions:
                        puzzle[solution[0]][solution[1]] = num

        # Going through every cell and check possible solutions and adding to a dictionary
        candidates = {}
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    solutions = []
                    for num in range(1,10):
                        if match_criteria(i,j,num,puzzle):
                            solutions.append(num)
                    candidates[(i,j)] = solutions

        # Checking in the dictionary for naked pairs in boxes
        for iBox in range(0,7,3):
            for jBox in range(0,7,3): # Going through  all the elements in the box
                doubles = {}
                for pos in candidates:
                    if len(candidates[pos]) == 2 and pos[0] in range(iBox,iBox + 3) and pos[1] in range (jBox,jBox +3):
                        doubles[pos] = tuple(candidates[pos])
                counter = Counter()
                for pair in doubles:
                    counter[doubles[pair]] += 1
                repetitions = dict(counter)
                npNums = set() # set of naked pairs numbers
                npPos = [] # list of naked pairs positions
                for rep,count in repetitions.items():
                    if count == 2:
                        for pair in doubles:
                            if doubles[pair] == rep:
                                npNums.add(rep[0])
                                npNums.add(rep[1])
                                npPos.append(pair)
                for pos in candidates:
                    if pos[0] in range(iBox,iBox + 3) and pos[1] in range (jBox,jBox +3) and pos not in npPos:
                        candidates[pos] = [num for num in candidates[pos] if num not in npNums]
        
        # Checking in the dictionary for naked pairs in rows
        for row in range(9):
            doubles = {}
            for pos in candidates:
                if len(candidates[pos]) == 2 and pos[0] == row:
                    doubles[pos] = tuple(candidates[pos])
            counter = Counter()
            for pair in doubles:
                counter[doubles[pair]] += 1
            repetitions = dict(counter)
            npNums = set() # set of naked pairs numbers
            npPos = [] # list of naked pairs positions
            for rep,count in repetitions.items():
                if count == 2:
                    for pair in doubles:
                        if doubles[pair] == rep:
                            npNums.add(rep[0])
                            npNums.add(rep[1])
                            npPos.append(pair)
            for pos in candidates:
                if pos[0] == row and pos not in npPos:
                    candidates[pos] = [num for num in candidates[pos] if num not in npNums]

        # Checking in the dictionary for naked pairs in columns:
        for col in range(9):
            doubles = {}
            for pos in candidates:
                if len(candidates[pos]) == 2 and pos[1] == col:
                    doubles[pos] = tuple(candidates[pos])
            counter = Counter()
            for pair in doubles:
                counter[doubles[pair]] += 1
            repetitions = dict(counter)
            npNums = set() # set of naked pairs numbers
            npPos = [] # list of naked pairs positions
            for rep,count in repetitions.items():
                if count == 2:
                    for pair in doubles:
                        if doubles[pair] == rep:
                            npNums.add(rep[0])
                            npNums.add(rep[1])
                            npPos.append(pair)
            for pos in candidates:
                if pos[1] == col and pos not in npPos:
                    candidates[pos] = [num for num in candidates[pos] if num not in npNums]

        # Checking in the dictionary for single values and add them to the puzzle
        for pos in candidates:
            if len(candidates[pos]) == 1:
                puzzle[pos[0]][pos[1]] = candidates[pos][0]
        n += 1
    '''
    
    Until this point in the code, the puzzle can be solved, but puzzle master and extreme cannot. This is where I got stuck most of the time trying to figure out how to solve it. Finally, 
    I decided to rely in the backtracking solution, which, to the point where I am writing this code, is still a bit difficult to completely understand. I checked how to do it a few
    times, but I will try to redo now alone.

    '''
    if backtrack(puzzle):
        print(puzzle)




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