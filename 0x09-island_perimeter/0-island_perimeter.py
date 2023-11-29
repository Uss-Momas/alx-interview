#!//usr/bin/python3
"""0-island_perimeter module
"""


def island_perimeter(grid):
    """island_perimeter - calculates the perimeter of an island represented as
    a grid
    Args:
        - grid: list of lists indicating the island, where 0 is water and 1 is
        island
    Returns:
        - perimeter of the island
    """
    row_limit = len(grid)
    column_limit = len(grid[0])
    perimeter = 0
    for i in range(row_limit):
        for j in range(column_limit):
            if grid[i][j] == 0:
                continue
            # we are at the up bound of the filled cell (=1)
            if i - 1 < 0:
                perimeter += 1
                up = -1
            # up value exists
            else:
                up = grid[i - 1][j]
            # we are at the down bound of the filled cell (=1)
            if i + 1 >= row_limit:
                perimeter += 1
                down = -1
            # down value exists
            else:
                down = grid[i + 1][j]
            # we are at the left bound of the filled cell (=1)
            if j - 1 < 0:
                perimeter += 1
                left = -1
            # left value exists
            else:
                left = grid[i][j - 1]
            # we are at the right bound of the filled cell (=1)
            if j + 1 >= column_limit:
                perimeter += 1
                right = -1
            # right value exists
            else:
                right = grid[i][j + 1]

            # if up, down, left, right are surrounded by water
            # we have to increase the perimete by 1
            if up == 0:
                perimeter += 1
            if down == 0:
                perimeter += 1
            if left == 0:
                perimeter += 1
            if right == 0:
                perimeter += 1
    return perimeter
