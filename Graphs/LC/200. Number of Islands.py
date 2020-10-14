# finding the number of islands

"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

"""

"""
we will iterate through each cell and mark the adjacent islands and return if it is an island

recursively
"""


#def numIslands(self, grid: List[List[str]]) -> int:
def numIslands(grid):

    # checking if grid is not None
    if not grid:
        return None
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1': 
        return
    grid[i][j] = '#'
    dfs(grid, i-1, j)
    dfs(grid, i, j-1)
    dfs(grid, i+1, j)
    dfs(grid, i, j+1)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))