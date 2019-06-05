class Solution:
  def arrayPairSum(self, nums) -> int:
    n = len(nums) // 2
    nums = sorted(nums)
    r = 0
    for i in range(n):
      r += nums[2 * i]
    return r
