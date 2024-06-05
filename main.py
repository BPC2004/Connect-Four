# Import the libraries
import numpy as np
import printboard as pb
import placecoin as pc
import placecoinbool as pcb
import checkfourinarow as cf

# Define the board into a 2d array and a 1d array
Board = np.array([[' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                  [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                  [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                  [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                  [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
                  [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']])
NBoard = np.array([' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 '])

# Define the variables
Coin = ' x '
Winner = False
Player = 1
Counter = 1

# Print the empty Board
pb.PrintBoard(Board, NBoard)

while Winner == False:
    # Player input and change it from str to int
    Col = input("Player " + str(Player) + " pick a column (1-7):")
    Col = int(Col) - 1
    
    # Place coin on the board if valid and then print the board
    Row = pc.PlaceCoin(Board, Coin, Col)
    pb.PrintBoard(Board, NBoard)

    # Check for horizontal 4 in a row
    if cf.CheckHorizontal(Row, Board, Coin) == True:
        Winner = True
        ConnectType = " won with a horizontal connect four."

    # Check for vertical 4 in a row
    if cf.CheckVertical(Col, Board, Coin) == True:
        Winner = True
        ConnectType = " won with a vertical connect four."

    # Check for diagonal 4 in a row
    if cf.CheckDiagonal(Col, Row, Board, Coin) == True:
        Winner = True
        ConnectType = " won with a diagonal connect four."


    # Change player and coin on the basis of value of Counter
    if pcb.PlaceCoinBool(Board, Col) == True:
        Counter += 1
        if Counter % 2 == 0:
            Player = 2
            Coin = ' o '
        else:
            Player = 1
            Coin = ' x '
# If winner == true print winner and how he won
print("Player " + str(Player) + ConnectType)
#}
