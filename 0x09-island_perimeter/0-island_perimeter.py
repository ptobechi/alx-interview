#!/usr/bin/python3
"""
Module to calculate the perimeter of an
island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in
    the given grid.

    Args:
        grid (list of list of int):
        The grid representing the map,
        where 1 is land and 0 is water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell initially adds 4
                # to the perimeter
                perimeter += 4
                
                # Check the cell above
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                
                # Check the cell to the left
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
