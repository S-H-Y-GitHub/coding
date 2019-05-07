class Solution:
  def numDecodings(self, s: str) -> int:
    res = [1] if s[0]!='0' else [0]
    for i in range(len(s)-1):
      t = 0
      if 10 <= int(s[i:i+2]) <= 26:
        t+=res[-2] if len(res) > 1 else 1
      if s[i+1] != '0':
        t+=res[-1]
      res.append(t)
    return res[-1]
  
