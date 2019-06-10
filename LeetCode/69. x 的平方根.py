"""
暴力法，很慢
"""
class Solution:
  def mySqrt(self, x: int) -> int:
    i = 2
    prev = 0
    while True:
      if i * i > x:
        break
      else:
        prev = i
        i = i * i
    for i in range(prev, x+1):
      if i * i > x:
        return i - 1
    return x
