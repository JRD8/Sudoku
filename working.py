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

    return None # If no empty squares


def valid(bo, num, pos):

    # Check the row 
    for i in range(len(bo[0])): # Loop through the designated pos row, ie pos[0] of the tuple
        if bo[pos[0]][i] == num and pos[1] != i: # The second element is to make sure it's not the same element as the one we just inserted. 
            return False

    # Check the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 box
    box_x = pos[1] // 3 # Identify which of 0, 1, 3 boxes the pos[col] is in
    box_y = pos[0] // 3 # Identify which of 0, 1, 3 boxes the pos[row] is in

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True # If make it to the end, then it is valid


def solve(bo):

    find = find_empty(bo) # Looks for a 0 or an empty space
    
    if not find: # If find = None (i.e., no more zeros or no empty spaces)
        return True # then return True or there are no more empties
    else:
        col, row = find # There are still some empties

    for i in range(1, 10): # Check numbers from 1-9, excluding 10
        if valid(bo, i, (row, col)): # Does adding that given number into board give valid solution?
            bo[row][col] = i # If yes/valid, add into the board

            if solve(bo): # And then try and finish the solution, by calling solve() again
                return True # 

            bo[row][col] = 0 # Reset last element because that can't be correct if we get here.

    return False # If we loop through all the bumbers and none of them are valid...



print_board(board)
solve(board)
print("*************")
print("SOLVED")
print("*************")
print_board(board)




