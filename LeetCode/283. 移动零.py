class Solution:
  def moveZeroes(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zerocount = 0
    c = 0
    for i in range(len(nums)):
      if nums[i] == 0:
        zerocount += 1
      else:
        nums[i-zerocount] = nums[i]
    for j in range(len(nums) - zerocount, len(nums)):
      nums[j] = 0
