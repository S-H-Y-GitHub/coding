"""
要求t无重复
"""
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    temp = {}
    for c in t:
      temp[c] = -1
    t = temp
    if len(s) < len(t):
      return ''
    elif len(s) == len(t):
      return s
    for i, char in enumerate(s):
      if char in t:
        start = i
        t[char] = i
        break
    else:
      return ''
    for i in range(start + 1, len(s)):
      if s[i] in t:
        t[s[i]] = i
        if s[i] == s[start]:
          start = min(filter(lambda x: x >= 0, t.values()))
        if all(map(lambda x: x >= 0, t.values())):
          end = i
          break
    else:
      return ''
    min_w = (end - start, start, end)
    cur_w = (end - start, start, end)
    for i in range(end + 1, len(s)):
      if s[i] in t:
        t[s[i]] = i
      if s[i] == s[cur_w[1]]:
        new_start = min(t.values())
        new_end = i
        cur_w = (new_end - new_start, new_start, new_end)
        if new_end - new_start < min_w[0]:
          min_w = cur_w
    return s[min_w[1]:min_w[2] + 1]
