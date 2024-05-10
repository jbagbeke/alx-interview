#!/usr/bin/python3
"""
Island Perimeter Problem solution
"""

def island_perimeter(grid):
    """
    Function definition
    """
    perimeter = 0
    
    for row_idx in range(len(grid)):
        row_prev = row_idx - 1
        row_next = row_idx + 1 if row_idx < len(grid) else -1
        row_len = len(grid[row_idx])

        for idx in range(row_len):
            prev = idx - 1
            next = idx + 1 if idx < row_len else -1
            
            if grid[row_idx][idx] == 1:
                if row_prev >= 0:
                    if grid[row_prev][idx] == 0:
                        perimeter += 1
                if prev >= 0:
                    if grid[row_idx][prev] == 0:
                        perimeter += 1
                if row_next > 0:
                    if grid[row_next][idx] == 0:
                        perimeter += 1
                if next > 0:
                    if grid[row_idx][next] == 0:
                        perimeter += 1
    return perimeter
