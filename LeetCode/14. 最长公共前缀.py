class Solution:
  def longestCommonPrefix(self, strs: 'List[str]') -> str:
    pre = []
    i = 0
    if len(strs) == 0:
      return ''
    while True:
      if i < len(strs[0]):
        c = strs[0][i]
      else:
        return ''.join(pre)
      for s in range(1, len(strs)):
        if i >= len(strs[s]) or strs[s][i] != c:
          return ''.join(pre)
      pre.append(c)
      i += 1
