class Solution:
  def permute(self, nums: 'List[int]') -> 'List[List[int]]':
    if len(nums) <= 1:
      return [nums]
    res = []
    for i in range(len(nums)):
      r = self.permute(nums[:i]+nums[i+1:])
      for p in r:
        p.append(nums[i])
      res.extend(r)
    return res
