class Solution:
  def jump(self, nums: 'List[int]') -> int:
    step = 0
    start = 0
    end = 0
    while end < len(nums)-1:
      step += 1
      new_start = end + 1
      for i in range(start, end + 1):
        if nums[i] + i > end:
          end = nums[i] + i
      start = new_start
    return step
