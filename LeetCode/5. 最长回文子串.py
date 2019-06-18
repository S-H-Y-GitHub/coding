# 远非最优
class Solution:
  def longestPalindrome(self, s: str) -> str:
    is_pal = [[-1] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
      is_pal[i][i] = 1
      if i + 1 < len(s):
        if s[i] == s[i + 1]:
          is_pal[i][i + 1] = 2
        else:
          is_pal[i][i + 1] = 0
    for i in range(len(s) - 2, -1, -1):
      for j in range(i + 2, len(s)):
        # assert is_pal[i + 1][j - 1] >= 0
        if is_pal[i + 1][j - 1] > 0:
          if s[i] == s[j]:
            is_pal[i][j] = j - i + 1
          else:
            is_pal[i][j] = 0
        else:
          is_pal[i][j] = 0
    max_i = -1
    max_l = -1
    for i in range(len(s)):
      for j in range(i, len(s)):
        if is_pal[i][j] > max_l:
          max_l = is_pal[i][j]
          max_i = i
    # assert max_i >= 0 and max_l > 0
    return s[max_i:max_i + max_l]
