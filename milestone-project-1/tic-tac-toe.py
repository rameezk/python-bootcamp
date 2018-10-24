# Setup
num_rows = 3
num_cols = 3

board = [["_" for x in range(num_cols)] for y in range(num_rows)]

player1 = None
player2 = None

def printBoard(board):
    for row in board:
        rowString = "|"
        for item in row:
            rowString += item + "|"
        print(rowString)

def setupPlayers():
    print("Player1, would you like to be 'X' or 'O'?")
    player1 = input("(X/O)--> ")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    print(f"Player1 is {player1}")
    print(f"Player2 is {player2}")

def getCoords(gridNumber):
    lookup = {
        "1": (0,0),
        "2": (1,0),
        "3": (2,0),
        "4": (0,1),
        "5": (1,1),
        "6": (2,1),
        "7": (0,2),
        "8": (1,2),
        "9": (2,2),
    }
    return lookup[gridNumber]


# Main
setupPlayers()
printBoard(board)
print(getCoords("1"))
