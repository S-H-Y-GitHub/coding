class Solution:
  def subarraySum(self, nums, k: int) -> int:
    from collections import Counter
    s = 0
    c = Counter([0])
    res = 0
    for i in nums:
      s += i
      res += c[s-k]
      c[s] += 1
    return res
