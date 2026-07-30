def print_board(board):
    print()

    for row in board:
        print(" ".join(row))

    print()


def is_safe(board, row, col, n):

    
    for j in range(n):
        if board[row][j] == 'Q':
            return False

    
    for i in range(n):
        if board[i][col] == 'Q':
            return False

   
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

  
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

  
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

   
    i, j = row, col
    while i < n and j < n:
        if board[i][j] == 'Q':
            return False
        i += 1
        j += 1

    return True




n = 4

board = [['.' for _ in range(n)] for _ in range(n)]

queens = 0

while queens < n:

    print_board(board)

    row = int(input("Enter row (0-3): "))
    col = int(input("Enter column (0-3): "))

  
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid Position!\n")
        continue


    if board[row][col] == 'Q':
        print("There is already a queen there!\n")
        continue

   
    if is_safe(board, row, col, n):
        board[row][col] = 'Q'
        queens += 1
        print("Queen Placed Successfully!\n")
    else:
        print("Invalid Move! Queen will attack another queen.\n")

print_board(board)
print("Congratulations! You placed all", n, "queens.")