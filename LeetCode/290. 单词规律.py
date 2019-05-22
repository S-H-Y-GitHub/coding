class Solution:
  def wordPattern(self, p: str, s: str) -> bool:
    d = {}
    if len(p) != len(s.split()):
      return False
    for pat, word in zip(p, s.split()):
      if pat not in d:
        if word in d.values():
          return False
        d[pat] = word
      elif d[pat] != word:
        return False
    return True
