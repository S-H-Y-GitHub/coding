class Solution:
  def reorganizeString(self, S: str) -> str:
    from collections import Counter
    s = Counter(S)
    if s.most_common(1)[0][1] > len(S) / 2 + 0.5:
      return ''
    else:
      res = []
      for i in range(0, len(S), 2):
        t=s.most_common(2)
        c1 = t[0][0]
        c2 = t[1][0] if t[1][1] > 0 else None
        res += c1
        s[c1] -= 1
        if c2 is not None:
          res += c2
          s[c2] -= 1
      return ''.join(res)
