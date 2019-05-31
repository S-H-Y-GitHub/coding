class Solution:
  def maxProfit(self, prices) -> int:
    min_p = None
    profits = [0]
    for p in prices:
      if min_p is None:
        min_p = p
      elif p < min_p:
        min_p = p
      profits.append(p-min_p)
    return max(profits)
