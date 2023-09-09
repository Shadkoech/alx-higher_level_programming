#!/usr/bin/python3
# The N queens puzzle

"""The N queens is a challenge of placing N non-attacking queens on an NxN
chessboard. The following program aims to solve it"""

import sys


def crack_nqueens(n):
    """The very beginning is to check if n is actually an integer
    and it is a value more than 4. If this is not the case, the
    program exits with value 1 showing error and failure"""

    if type(n) is not int:
        print("N must be an integer")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def isit_safe(board, row, col):
        """This function simply ascertains if it is safe to place a queen
        at a particular position on the chessboard. If so, return True,
        otherwise return False"""

        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True

    def crack_util(board, row):
        """For this function, if row is equal to the value n that
        means all queens have been placed"""

        if row == n:
            solns.append(board.copy())
            return

        for col in range(n):
            if isit_safe(board, row, col):
                board[row] = col
                crack_util(board, row + 1)
                board[row] = -1

    # Initializing the chessboard and an empty list to store solutions
    board = [-1] * n
    solns = []
    crack_util(board, 0)

    # Representing the solution by printing in the desired format
    for soln in solns:
        format_soln = [[i, soln[i]] for i in range(n)]
        print(format_soln)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    crack_nqueens(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)
