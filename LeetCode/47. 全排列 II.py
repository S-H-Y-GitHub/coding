class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
          return []
        if len(nums) == 1:
          return[nums]
        nums = sorted(nums)
        
        def helper(l):
          if len(l) == 1:
            return [l]
          prev = None
          res = []
          for i, num in enumerate(l):
            if num == prev:
              continue
            prev = num
            right = helper(l[:i]+l[i+1:])
            for permute in right:
              permute.insert(0, num)
            res.extend(right)
          return res
        return helper(nums)
