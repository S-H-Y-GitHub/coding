class Solution:
  def islandPerimeter(self, grid) -> int:
    res = 0
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == 1:
          res += 4
          if i - 1 >= 0 and grid[i - 1][j] == 1:
            res -= 1
          if j - 1 >= 0 and grid[i][j - 1] == 1:
            res -= 1
          if i + 1 < len(grid) and grid[i + 1][j] == 1:
            res -= 1
          if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
            res -= 1
    return res
