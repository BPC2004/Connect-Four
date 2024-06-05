# Checks for horizontal connextfours
def CheckHorizontal(Row, Board, Coin):
    Counter = 0
    for Col in range(7):
        if Board[Row][Col] == Coin:
            Counter += 1
            if Counter >= 4:
                return True
        else:
            Counter = 0
        Col += 1
    return False

# Checks for vertical connextfours
def CheckVertical(Col, Board, Coin):
    Row = 0
    Counter = 0
    for Row in range(6):
        if Board[Row][Col] == Coin:
            Counter += 1
            if Counter >= 4:
                return True
        else:
            Counter = 0
        Row += 1
    return False

# Checks for diagonal to the left connextfours
def CheckDiagonal(Col, Row, Board, Coin):
    # Check the bottom-left to top-right diagonal
    Counter = 1
    iRow = Row - 1
    jCol = Col + 1
    while iRow >= 0 and jCol < 7:
        if Board[iRow][jCol] == Coin:
            Counter += 1
            if Counter >= 4:
                return True
        else:
            break
        iRow -= 1
        jCol += 1
    
    # Check the top-left to bottom-right diagonal
    Counter = 1
    iRow = Row + 1
    jCol = Col - 1
    while iRow < 6 and jCol >= 0:
        if Board[iRow][jCol] == Coin:
            Counter += 1
            if Counter >= 4:
                return True
        else:
            break
        iRow += 1
        jCol -= 1
    return False