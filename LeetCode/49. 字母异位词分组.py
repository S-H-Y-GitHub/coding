class Solution:
  def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
    from collections import Counter
    pat = []
    res = []
    for word in strs:
      wc = Counter(word)
      if wc not in pat:
        pat.append(wc)
        res.append([word])
      else:
        i = pat.index(wc)
        res[i].append(word)
    return res
