class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    ways = [[0] * (m + 1)] * (n + 1)
    ways[0][1] = 1
    for i in range(1, n+1):
      for j in range(1, m+1):
        ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
    return ways[-1][-1]
