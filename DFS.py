import copy
from collections import deque
class State:
    def __init__(self, board, newValue, location):
        self.board = board
        self.newValue = newValue
        self.location = location
    def PrintState(self):
        print("Add", self.newValue)
        print("Row number:", self.location[0])
        print("Column number:", self.location[1])
        PrintBoard(self.board)

def PrintBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " "),
            if j in [2, 5]:
                print("|", end = " ")
        print()
        if i in [2, 5]:
            for n in range(11):
                print("-", end = " ")
            print()

def PrintStack(stack, step):
    if len(stack) == 0:
        return
    state = stack.pop()
    PrintStack(stack, step - 1)
    print("step:", step)
    state.PrintState()
    print()

def IsValidAssign(board, row, column, number):
    # Check in row
    for j in range(9):
        if board[row][j] == number:
            return False
    # check in column
    for i in range(9):
        if board[i][column] == number:
            return False
    # check in square
    startRow = row - row % 3
    startColumn = column - column % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startColumn] == number:
                return False
    return True

def FindEmptyLocation(board, location):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                location[0] = row
                location[1] = column
                return True
    return False

def SolveSudoku(board, stack):
    location = [0, 0]
    if not FindEmptyLocation(board, location):
        return True
    row = location[0]
    column = location[1]
    for number in range(1, 10):
        if IsValidAssign(board, row, column, number):
            board[row][column] = number
            stack.append(State(copy.deepcopy(board), number, [row, column]))
            if (SolveSudoku(board, stack)):
                return True
            board[row][column] = 0
            stack.pop()
    return False

board = [
    [0, 0, 0, 9, 0, 8, 0, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 9],
    [0, 0, 2, 0, 0, 0, 8, 0, 0],
    [0, 8, 0, 7, 0, 3, 0, 1, 0],
    [0, 0, 0, 2, 0, 6, 0, 0, 0],
    [0, 3, 0, 0, 5, 0, 0, 6, 0],
    [0, 5, 0, 6, 0, 7, 0, 8, 0],
    [0, 2, 0, 5, 0, 9, 0, 3, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
]
initialBoard = copy.deepcopy(board)
stack = deque()
if SolveSudoku(board, stack):
    print("Initial board:")
    PrintBoard(initialBoard)
    print()
    PrintStack(stack, len(stack))
else:
    print("No Solution Found")
