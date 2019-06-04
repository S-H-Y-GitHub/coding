class Solution:
  def frequencySort(self, s: str) -> str:
    from collections import Counter
    c = Counter(s)
    res = []
    for char, count in c.most_common():
      res.extend([char] * count)
    return ''.join(res)
