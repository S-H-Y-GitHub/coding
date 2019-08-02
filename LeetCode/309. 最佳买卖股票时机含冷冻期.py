class Solution:
  def maxProfit(self, prices: 'List[int]') -> int:
    import sys
    hold_prev = -sys.maxsize
    release_prev = 0
    cool_prev = -sys.maxsize
    release_now = 0
    for p in prices:
      hold_now = max(hold_prev, release_prev - p)
      release_now = max(release_prev, cool_prev)
      
      cool_prev = hold_prev + p
      hold_prev = hold_now
      release_prev = release_now
    return max(release_now, cool_prev)
