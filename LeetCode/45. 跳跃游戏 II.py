"""
动态规划解法，n2的复杂度，可以用贪心法优化
"""

class Solution:
  def jump(self, nums: 'List[int]') -> int:
    m = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
      for j in range(i + 1, len(nums)):
        if j - i <= nums[i]:
          m[i][j] = 1
        else:
          import sys
          m[i][j] = min([m[i+k][j] for k in range(1, nums[i]+1)]+[sys.maxsize]) + 1
    return m[0][-1] if len(m) > 0 else 0
