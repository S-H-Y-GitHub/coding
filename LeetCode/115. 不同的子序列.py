class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    if len(t) == 0 or s == t:
      return 1
    if len(s) == 0:
      return 0
    dp = [[0 for j in range(len(t))] for i in range(len(s))]
    for i in range(len(s)):
      if s[i] == t[0]:
        dp[i][0] = dp[i - 1][0] + 1
      else:
        dp[i][0] = dp[i - 1][0] if i - 1 >= 0 else 0
    for i in range(1, len(s)):
      for j in range(1, len(t)):
        if s[i] == t[j]:
          dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
          dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]
