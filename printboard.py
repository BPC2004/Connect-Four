import numpy as np
# Define the board and print it
def PrintBoard(Board, NBoard):
    # Align elements in each row of the Board array
    aligned_board = np.char.ljust(Board.astype(str), width=4)
    # Calculate the maximum width for each column in the Board
    max_widths = np.max([list(map(len, row)) for row in aligned_board.T], axis=1)
    # Print the aligned Board
    for row in aligned_board:
        print(' '.join([elem.ljust(width) for elem, width in zip(row, max_widths)]))
    # Print the NBoard with corresponding alignment
    print(' '.join([num.ljust(width) for num, width in zip(NBoard, max_widths)]))