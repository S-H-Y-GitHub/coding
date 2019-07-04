class Solution:
  def longestValidParentheses(self, s: str) -> int:
    m = [0] * len(s)
    unclosed = []
    for i, char in enumerate(s):
      if char == '(':
        unclosed.append(i)
      elif char == ')' and len(unclosed) > 0:
        index = unclosed.pop()
        m[i] = m[index - 1] + i - index+1
    return max(m) if len(m) > 0 else 0
