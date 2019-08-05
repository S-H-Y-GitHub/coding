class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if len(s) == 0 or len(t) == 0:
      return ''
    start = 0
    end = 0
    from collections import Counter
    t = Counter(t)
    if s[0] in t:
      window = Counter(s[0])
    else:
      window = Counter()
    
    def satisfy(t, window):
      for item in t:
        if window[item] < t[item]:
          return False
      return True
    
    min_window = None
    while True:
      f = False
      while not satisfy(t, window) and end < len(s) - 1:
        end += 1
        if s[end] in t:
          window[s[end]] += 1
      if satisfy(t, window):
        f = True
      while satisfy(t, window) and start <= end:
        if s[start] in t:
          window[s[start]] -= 1
        start += 1
      if f and (min_window is None or min_window[1] - min_window[0] > end - start + 1):
        min_window = (start-1, end)
      if end == len(s) - 1:
        break
    if min_window is None:
      return ''
    return s[min_window[0]:min_window[1] + 1]
