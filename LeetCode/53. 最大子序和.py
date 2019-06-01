class Solution:
  def maxSubArray(self, nums: list) -> int:
    max_sum = []
    if len(nums) > 0:
      max_sum.append(nums[0])
    else:
      return 0
    for i in nums[1:]:
      if max_sum[-1] < 0:
        max_sum.append(i)
      else:
        max_sum.append(max_sum[-1] + i)
    return max(max_sum)
