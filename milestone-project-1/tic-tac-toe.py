# Setup
num_rows = 3
num_cols = 3

board = [["_" for x in range(num_cols)] for y in range(num_rows)]

def printBoard(board):
    for row in board:
        rowString = "|"
        for item in row:
            rowString += item + "|"
        print(rowString)


# Main
printBoard(board)
