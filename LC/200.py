# Pass 1 

def numIslands(grid):
    """
    Counts the number of islands in a given grid.

    Args:
        grid (List[List[str]]): A 2D grid represented as a list of lists of characters.
            '1' represents land, '0' represents water.

    Returns:
        int: The number of islands in the grid.
    """

    if not grid:
        return 0

    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'  # Mark the current cell as visited

        # Recursively visit all adjacent cells
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(grid, i, j)

    return num_islands


# Pass 2 


def numIslands(self, grid):
    """
    Counts the number of islands in a given grid.

    Args:
        grid (List[List[str]]): A 2D grid of '1's (land) and '0's (water).

    Returns:
        int: The number of islands in the grid.

    """
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))