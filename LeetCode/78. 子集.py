class Solution:
  def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
    res = [[]]
    if len(nums) == 0:
      return res
    for i, num in enumerate(nums):
      right = self.subsets(nums[i + 1:])
      for r in right:
        r.append(num)
      res.extend(right)
    return res
