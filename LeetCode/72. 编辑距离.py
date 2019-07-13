class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    if len(word1) == 0:
      return len(word2)
    if len(word2) == 0:
      return len(word1)
    m = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i, x in enumerate(m):
      x[0] = i
    for j in range(len(m[0])):
      m[0][j] = j
    for i in range(1, len(word1)+1):
      for j in range(1, len(word2)+1):
        if word1[i - 1] == word2[j - 1]:
          m[i][j] = m[i - 1][j - 1]
        else:
          m[i][j] = min(m[i - 1][j - 1], m[i][j - 1], m[i - 1][j]) + 1
    return m[-1][-1]
