"""
执行用时 : 48 ms, 在Partition Labels的Python3提交中击败了100.00% 的用户
内存消耗 : 12.7 MB, 在Partition Labels的Python3提交中击败了100.00% 的用户
"""

class Solution:
  def partitionLabels(self, s: str):
    index = {}
    for i, c in enumerate(s):
      if c not in index:
        index[c] = [i, i]
      else:
        index[c][1] = i
    res = []
    i = 0
    while i < len(s):
      c = s[i]
      c_set = {c}
      low = index[c][0]
      high = index[c][1]
      while True:
        r = set(s[low: high + 1]) - c_set
        if len(r) > 0:
          for c in r:
            break
          c_set.add(c)
          if high < index[c][1]:
            high = index[c][1]
        else:
          res.append(high - low + 1)
          break
      i = high + 1
    return res
