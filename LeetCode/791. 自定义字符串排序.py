class Solution:
  def customSortString(self, S: str, T: str) -> str:
    from collections import Counter
    t = Counter(T)
    a = []
    for char in S:
      a.append(char * t[char])
      del t[char]
    a.extend((char * t[char] for char in t))
    return ''.join(a)
