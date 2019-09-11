class Solution:
  def maxProfit(self, nums) -> int:
    dp1 = [0] * len(nums)
    current_min = None
    for i in range(len(nums)):
      if current_min is None:
        current_min = nums[i]
      if nums[i] < current_min:
        current_min = nums[i]
      if i > 0:
        if dp1[i - 1] < nums[i] - current_min:
          dp1[i] = nums[i] - current_min
        else:
          dp1[i] = dp1[i - 1]
  
    dp2 = [0] * len(nums)
    current_max = None
    for i in range(len(nums) - 1, -1, -1):
      if current_max is None:
        current_max = nums[i]
      if nums[i] > current_max:
        current_max = nums[i]
      if i < len(nums) - 1:
        if dp2[i + 1] < current_max - nums[i]:
          dp2[i] = current_max - nums[i]
        else:
          dp2[i] = dp2[i + 1]
  
    max_res = 0
    for i in range(len(nums) - 1):
      if dp1[i] + dp2[i + 1] > max_res:
        max_res = dp1[i] + dp2[i + 1]
      if dp1[i + 1] > max_res:
        max_res = dp1[i + 1]
    return max_res
