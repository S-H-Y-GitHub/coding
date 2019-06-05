class Solution:
  def canCompleteCircuit(self, gas, cost) -> int:
    left = 0
    a = 0
    mi = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
      if left < 0:
        left = 0
        mi = i
      left += g-c
      a += g-c
    if a >= 0 and left >= 0:
      return mi
    else:
      return -1
