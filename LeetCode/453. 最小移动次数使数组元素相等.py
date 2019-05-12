class Solution:
  def minMoves(self, nums: List[int]) -> int:
    m=0
    min_v = min(nums)
    for i in nums:
      m += i-min_v
    return m
