#!/usr/bin/python3
"""rotate_2d_matrix"""


def reverse(list_item):
    """reverse a list"""
    return list_item[::-1]


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function
    rotate matrix in 90 degrees clockwise

    Solution for the problem is quiet easy:
        - First Transpose the matrix
        - Then make a reverse of each list in the matrix
    """
    length = len(matrix)

    for i in range(0, length):
        matrix[i]
        for j in range(i, length):
            # part responsible for making the exchange of the values for the
            # tranpose
            # swaps 2 elements
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i] = reverse(matrix[i])
