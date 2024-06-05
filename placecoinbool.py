# Check whether the coin can be placed in that row and if not do not switch player and print Invalid Column
def PlaceCoinBool(Board, Col):
    Row = 5
    while Row >= 0:
        if Board[Row][Col] == ' - ':
            return True
        Row -= 1
    print("Invalid Column")
    return False