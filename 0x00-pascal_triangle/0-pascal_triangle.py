#!/usr/bin/python3
"""
0-pascal_triangle
"""


def handle_new_array(prev_data):
    """creates a new line with correct data"""
    new_line = []
    # append with the first value, it doesnt change
    new_line.append(prev_data[0])

    for index in range(0, len(prev_data)):
        if index + 1 < len(prev_data):
            new_line.append(prev_data[index] + prev_data[index + 1])
        else:
            new_line.append(prev_data[index])
    return new_line


def pascal_triangle(n):
    """Function that returns the list containg the lines of the triangle"""
    if n < 1:
        return []
    # initialize with the first element
    pascal = [[1]]

    # create new array each new line
    for i in range(0, n - 1):
        prev_array = pascal[i]
        new_data = handle_new_array(prev_array)
        pascal.append(new_data)
    return pascal