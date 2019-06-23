class Solution:
  def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
    nums = sorted(nums)
    res = set()
    if len(nums) < 3:
      return []
    for p2 in range(1, len(nums) - 1):
      p1 = 0
      p3 = len(nums) - 1
      while p1 < p2 < p3:
        s = nums[p1] + nums[p2] + nums[p3]
        if s < 0:
          p1 += 1
        elif s > 0:
          p3 -= 1
        else:
          res.add((nums[p1], nums[p2], nums[p3]))
          p1 += 1
          p3 -= 1
    return list(res)
