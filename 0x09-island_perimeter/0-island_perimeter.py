#!/usr/bin/python3
"""
Island Perimeter Problem solution
"""


def island_perimeter(grid):
    """
    Function definition
    """
    perimeter = 0

    for row in range(len(grid)):
        grid_len = len(grid)
        row_len = len(grid[row])

        for idx in range(row_len):
            if grid[row][idx] == 1:
                perimeter += 4

                if (row - 1) >= 0 and grid[row - 1][idx] == 1:
                    perimeter -= 1
                if (row + 1) < grid_len and grid[row + 1][idx] == 1:
                    perimeter -= 1
                if (idx - 1) >= 0 and grid[row][idx - 1] == 1:
                    perimeter -= 1
                if (idx + 1) < row_len and grid[row][idx + 1] == 1:
                    perimeter -= 1
    return perimeter
