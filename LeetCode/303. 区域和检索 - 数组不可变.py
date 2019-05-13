class NumArray:
  
  def __init__(self, nums):
    self.nums = nums
    self.caled_sum = {}
  
  def sumRange(self, i: int, j: int) -> int:
    if i > j:
      return 0
    s = 0
    for pair in self.caled_sum:
      if pair[0] >= i and pair[1] <= j:
        s += self.caled_sum[pair]
        s += self.sumRange(i, pair[0] - 1)
        s += self.sumRange(pair[1] + 1, j)
        return s
    
    return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
