#!/usr/bin/python3
"""
2D Matrix Rotation implementation
"""


def rotate_2d_matrix(matrix):
    """
    Matrix rotation function
    """
    transposed = zip(*matrix)
    idx = 0
    for t_matrix in transposed:
        matrix[idx] = list(t_matrix)[::-1]
        idx += 1
