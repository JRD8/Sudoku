board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(bo):
    for i in range(len(bo)):
        
        if i % 3 == 0 and i != 0: # Every 3rd row (not counting first one), print a horizontal line
            print("-----------------------")
        
        for j in range(len(bo[0])):
            
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8: # If this is the last position of the 9x9 grid, no need for an extra space
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") # If this is not the last position of the 9x9 grid, then also print an extra space


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            
            if bo[i][j] == 0:
                return (i, j) # Position of empty row, col as a tuple


print_board(board)




