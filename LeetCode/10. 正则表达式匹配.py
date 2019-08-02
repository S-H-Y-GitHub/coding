class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    j = 0
    i = 0
    if len(s) == 0:
      while i < len(p):
        if i + 1 < len(p) and p[i + 1] == '*':
          i += 2
        else:
          return False
    while i < len(p):
      if p[i] == '.':
        if i + 1 < len(p) and p[i + 1] == '*':
          return self.isMatch(s[j:], p[i + 2:]) or self.isMatch(s[j + 1:], p[i:])
        else:
          if j >= len(s) > 0:
            return False
          j += 1
          i += 1
      else:
        if i + 1 < len(p) and p[i + 1] == '*':
          if j < len(s) and p[i] == s[j]:
            return self.isMatch(s[j:], p[i + 2:]) or self.isMatch(s[j + 1:], p[i:])
          else:
            i += 2
        else:
          if j >= len(s) > 0:
            return False
          if j < len(s) and p[i] == s[j]:
            j += 1
            i += 1
          else:
            return False
    if j == len(s):
      return True
    else:
      return False
