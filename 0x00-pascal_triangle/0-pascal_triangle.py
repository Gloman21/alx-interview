#!/usr/bin/python3
"""interview prep"""


def pascal_triangle(n):
    """
    generate Pascal's triangle up to the given number of rows.

    parameters:
        n (int): The number of rows in Pascal's triangle.

    returns:
        list: A list of lists representing Pascal's triangle.
          Each inner list represents a row of the triangle.

    example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    # initialize the first row of Pascal's Triangle
    arrOld = [[1]]

    for j in range(1, n):
        arr = []  # creates a new row
        for i in range(0, j + 1):
            if i == 0 or i == j:
                arr.append(1)
            else:
                arr.append(arrOld[j-1][i-1] + arrOld[j-1][i])
        arrOld.append(arr)  # adds the new row to Pascal's Triangle

    return arrOld
