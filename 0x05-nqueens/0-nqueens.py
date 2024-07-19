#!/usr/bin/python3
"""
N-Queens puzzle solver.
Usage: nqueens N
"""


import sys


def print_usage_and_exit():
    """
    Print usage message and exit with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(msg):
    """
    Print error message and exit with status 1.

    Args:
        msg (str): The error message to print.
    """
    print(msg)
    sys.exit(1)

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list of list of int): The chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place the queen,
        False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        board (list of list of int):
            The chessboard.
        col (int):
            The current column index to place a queen.

    Returns:
        bool:
            True if a solution is found, False otherwise.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0
    return res

if len(sys.argv) != 2:
    print_usage_and_exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print_error_and_exit("N must be a number")

if N < 4:
    print_error_and_exit("N must be at least 4")

board = [[0 for _ in range(N)] for _ in range(N)]
solutions = []

solve_nqueens(board, 0)

for solution in solutions:
    print(solution)
