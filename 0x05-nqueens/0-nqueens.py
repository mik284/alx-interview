import sys

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("")

def is_valid(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve(board, col, n):
    if col == n:
        print_board(board)
        return

    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = "Q"
            solve(board, col + 1, n)
            board[i][col] = "."

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [["." for _ in range(n)] for _ in range(n)]
solve(board, 0, n)
