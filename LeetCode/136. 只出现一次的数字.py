class Solution:
  def singleNumber(self, nums) -> int:
    c = 0
    for i in nums:
      c = i ^ c
    return c
