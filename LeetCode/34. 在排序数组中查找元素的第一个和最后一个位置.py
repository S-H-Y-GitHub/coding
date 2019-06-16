class Solution:
  def searchRange(self, nums, target: int):
    if len(nums) == 0:
      return [-1, -1]
    start = 0
    end = len(nums)
    res = [-1, -1]
    while end > start:
      mid = (start + end) // 2
      if nums[mid] == target:
        start2 = start
        end2 = mid + 1
        while start2 < end2:
          mid2 = (start2 + end2) // 2
          if nums[mid2] == target and (mid2 == start or nums[mid2 - 1] < target):
            res[0] = mid2
            break
          elif nums[mid2] < target:
            if start2 != mid2:
              start2 = mid2
            else:
              start2 = mid2 + 1
          else:
            if end2 != mid2:
              end2 = mid2
            else:
              end2 = mid2 - 1
        
        start2 = mid
        end2 = end
        while start2 < end2:
          mid2 = (start2 + end2) // 2
          if nums[mid2] == target and (mid2 == end - 1 or nums[mid2 + 1] > target):
            res[1] = mid2
            break
          elif nums[mid2] > target:
            if end2 != mid2:
              end2 = mid2
            else:
              end2 = mid2 - 1
          else:
            if start2 != mid2:
              start2 = mid2
            else:
              start2 = mid2 + 1
        
        return res
      elif nums[mid] < target:
        if start != mid:
          start = mid
        else:
          start = mid + 1
      elif nums[mid] > target:
        if end != mid:
          end = mid
        else:
          end = mid - 1
    return res
