class Solution:
  def findAnagrams(self, s: str, p: str) -> list:
    if len(s) < len(p):
      return []
    from collections import Counter
    pc = Counter(p)
    res = []
      
    for i in range(len(s)):
      if s[i] in pc:
        pc[s[i]] -= 1
      if i >= len(p) and s[i-len(p)] in pc:
        pc[s[i-len(p)]] += 1
      if len(+pc) == 0:
        res.append(i-len(p)+1)
    return res
