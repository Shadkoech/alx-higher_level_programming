#!/usr/bin/python3
"""The N queens is a challenge of placing N non-attacking queens on an NxN
chessboard. The following program aims to solve it"""

import sys


def is_safe(board, row, col, n):
    """This function simply ascertains if it is safe to place a queen
        at a particular position on the chessboard. If so, return true
        otherwise return false"""

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """The very beginning is to check if n is actually an integer
    and it is a value more than 4. If this is not the case, the
    program exits with value 1 showing error and failure"""

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def nqueens_util(col):
        if col == n:
            solutions.append(board[:])  # Add a copy of the board to solutions
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                nqueens_util(col + 1)
                board[i][col] = 0  # Backtrack

    nqueens_util(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
