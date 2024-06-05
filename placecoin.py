def PlaceCoin(Board, Coin, Col):
    Col -= 1
    Row = 5
    while Row >= 0:
        if Board[Row][Col] == ' - ':
            Board[Row][Col] = Coin
            return Row
        Row -= 1
    print("Invalid Column")
    return -1