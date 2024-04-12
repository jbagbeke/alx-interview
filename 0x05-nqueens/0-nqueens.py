#!/usr/bin/python3
"""
N QUEENS PROBLEM MODULE
"""
import sys


def generate_solutions(row, column):
    soln = [[]]
    for queen in range(row):
        soln = place_queen(queen, column, soln)
    return soln


def place_queen(queen, column, prev_soln):
    """
    Check queen function
    """
    safe_pos = []
    for array in prev_soln:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_pos.append(array + [x])
    return safe_pos


def is_safe(q, arr, array):
    """
    Position checking
    """
    if arr in array:
        return (False)
    else:
        return all(abs(array[column] - arr) != q - column
                   for column in range(q))


def init():
    """
    Initialiser
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """
    Main function checker
    """
    n = init()

    solns = generate_solutions(n, n)

    for arr in solns:
        result = []
        for q, x in enumerate(arr):
            result.append([q, x])
        print(result)
