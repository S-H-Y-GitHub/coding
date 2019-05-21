class Solution:
  def summaryRanges(self, nums):
    if len(nums) == 0:
      return []
    
    res = []
    prev = nums[0] - 1
    start = nums[0]
    end = nums[0]
    for num in nums:
      if num == prev + 1:
        end = num
      else:
        res.append('%d->%d'%(start, end) if end > start else str(start))
        start = num
      prev = num
    res.append('%d->%d' % (start, end) if end > start else str(start))
    return res
