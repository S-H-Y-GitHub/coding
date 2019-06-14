# 居然是贪心算法
class Solution:
  def lengthOfLIS(self, nums) -> int:
    def bi_find(i, tails):
      start = 0
      end = len(tails)
      while end > start:
        mid = (start + end - 1) // 2
        if tails[mid] < i:
          start = mid + 1
          if mid + 1 < len(tails) and tails[mid + 1] >= i:
            return mid + 1
        elif tails[mid] > i:
          end = mid + 1
          if mid - 1 < 0 or tails[mid - 1] < i:
            return mid
        else:
          return mid
    
    if len(nums) < 2:
      return len(nums)
    tails = [nums[0]]
    for i in nums:
      if i < tails[-1]:
        index = bi_find(i, tails)
        tails[index] = i
      elif i > tails[-1]:
        tails.append(i)
    return len(tails)
