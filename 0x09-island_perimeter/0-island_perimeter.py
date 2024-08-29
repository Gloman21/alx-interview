#!/usr/bin/python3
"""island perimeter computing
"""


def island_perimeter(grid):
    """compute the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m= len(row)
        for h, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > h and grid[i - 1][h] == 0),
                h == m - 1 or (m > h + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > h and grid[i + 1][h] == 0),
                h == 0 or row[h - 1] == 0,
            )
            perimeter += sum(edges)
        return perimeter
