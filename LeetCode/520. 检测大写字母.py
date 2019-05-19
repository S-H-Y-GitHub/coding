class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    for i, c in enumerate(word):
      if i == 0:
        lower = c.islower()
      elif i == 1:
        if lower and c.isupper():
          return False
        elif not lower and c.islower():
          lower = True
      else:
        if lower and c.isupper():
          return False
        elif not lower and c.islower():
          return False
    return True
