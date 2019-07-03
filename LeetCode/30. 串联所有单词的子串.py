class Solution:
  def findSubstring(self, s: str, words: 'List[str]') -> 'List[int]':
    res = []
    if len(words) == 0:
      return res
    words_size = len(words[0]) * len(words)
    word_size = len(words[0])
    if len(s) < words_size:
      return res
    from collections import Counter
    words = Counter(words)
    for i in range(len(s) - words_size + 1):
      st = s[i:i + words_size]
      words_in_st = [st[j:j + word_size] for j in range(0, len(st), word_size)]
      if Counter(words_in_st) == words:
        res.append(i)
    return res
