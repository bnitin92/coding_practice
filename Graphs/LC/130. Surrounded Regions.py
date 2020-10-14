# find the surrounded regions

"""
Input:
'X' 'X' 'X' 'X'
'X' O O 'X'
'X' 'X' O 'X'
'X' O 'X' 'X'

Output:
'X' 'X' 'X' 'X'
'X' 'X' 'X' 'X'
'X' 'X' 'X' 'X'
'X' O 'X' 'X'

"""

"""
steps:
first i will go thorough the borders and see if any zeros are there and make it one 
first row, last row, first column, last column if any one converted, repeat the row and column with -1 

then going each row by row we will convert all the 0 to 'X' 
then going each row by row convert all the ones to zero

"""

#def solve(self, board: List[List[str]]) -> None:
def solve(board):
    changed_any = 0
    def convertingtoone(board, fr, lr, fc, lc):
        for i in range(len(board[fr])):
            if board[fr][i] == 0: board[fr][i] = 1
        for i in range(len(board[lr])):
            if board[lr][i] == 0: board[lr][i] = 1
        for i in range(len(board[fr])):
            if board[i][fc] == 0: board[i][fc] = 1
        for i in range(len(board[lr])):
            if board[i][lc] == 0: board[i][lc] = 1

        return board

    board = convertingtoone(board, 0, len(board)-1, 0, len(board)-1)

    return board

board = [['X', 'X', 'X', 'X'],
         ['X', 0, 0, 'X'],
         ['X', 'X', 0, 'X'],
         ['X', 0, 'X', 'X']]
print(solve(board))


