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

def setupPlayers():
    print("Player1, would you like to be 'X' or 'O'?")
    player1 = input("(X/O)--> ")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"Player1 is {player1}")
    print(f"Player2 is {player2}")
    return {
        "1": player1,
        "2": player2
    }

def getCoords(gridNumber):
    lookup = {
        "1": (0,0),
        "2": (0,1),
        "3": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "7": (2,0),
        "8": (2,1),
        "9": (2,2),
    }
    return lookup[gridNumber]

def playTurn(player, gridNumber, board):
    coord = getCoords(gridNumber)
    board[coord[0]][coord[1]] = player

def togglePlayer(currentPlayer, players):
    if currentPlayer == players["1"]:
        return players["2"]
    else:
        return players["1"]

def checkForWinner(board, players):
    #check horizontals
    for row in board:
        rowString = "".join(row)
        if rowString == "XXX" or rowString == "OOO":
            return True

    #check verticals
    for i in range(num_cols):
        colString = "".join([row[i] for row in board])
        if colString == 'XXX' or colString == 'OOO':
            return True

    #check diagonals
    diag1Str = "".join([board[0][0], board[1][1], board[2][2]])
    diag2Str = "".join([board[2][0], board[1][1], board[0][2]])
    if diag1Str == "XXX" or diag1Str == "OOO":
        return True
    if diag2Str == "XXX" or diag2Str == "OOO":
        return True

    return False



# Main
players = setupPlayers()

turn_counter = 0
max_turns = num_cols * num_rows

current_player = players["1"]

while turn_counter < max_turns:

    print("Choose grid number:")
    selectedGridNumber = input('--> ')

    playTurn(current_player, selectedGridNumber, board)

    printBoard(board)

    if checkForWinner(board, players):
        print("Winner!!!")
        break

    current_player = togglePlayer(current_player, players)

    print("")
    print("------------------------------------------------")
    print("")

    turn_counter += 1
