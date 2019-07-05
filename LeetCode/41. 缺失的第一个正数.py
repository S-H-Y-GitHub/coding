class Solution:
  def firstMissingPositive(self, nums: 'List[int]') -> int:
    if len(nums) == 0:
      return 1
    for i in range(len(nums)):
      if nums[i] <= 0:
        nums[i] = len(nums) + 2
    i = 0
    num = nums[i]
    while True:
      if num <= 0 or num > len(nums):
        i += 1
        if i == len(nums):
          break
        num = nums[i]
        continue
      if nums[num - 1] > 0:
        nums[num - 1] = -nums[num - 1]
        num = -nums[num - 1]
      else:
        i += 1
        if i == len(nums):
          break
        num = nums[i]
    for i, num in enumerate(nums):
      if num > 0:
        return i + 1
    return len(nums)+1
