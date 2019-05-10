#注意O(n)可以遍历数组多次，也可以改变原始数组

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    l = len(nums)
    for i in range(l):
      if nums[i] < 0:
        index = -nums[i]
      else:
        index = nums[i]
      if nums[index-1] > 0:
        nums[index-1] = -nums[index-1]
    res = []
    for i, num in enumerate(nums):
      if num > 0:
        res.append(i + 1)
    return res
      
