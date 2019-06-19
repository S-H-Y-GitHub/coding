class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    left = {'[', '(', '{'}
    pair = {']': '[', ')': '(', '}': '{'}
    for c in s:
      if c in left:
        stack.append(c)
      else:
        if len(stack) == 0:
          return False
        top = stack.pop()
        if top != pair[c]:
          return False
    if len(stack) == 0:
      return True
    return False
