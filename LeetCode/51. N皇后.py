class Solution:
  def solveNQueens(self, n: int) -> 'List[List[str]]':
    res = []
    if n == 0:
      return res
    
    def gen_line(k):
      line = []
      for i in range(n):
        if i == k:
          line.append('Q')
        else:
          line.append('.')
      return ''.join(line)
    
    def helper(mt):
      # get possible selections
      if len(mt) == n:
        return mt
      poss = [1] * n
      for i, line in enumerate(mt):
        j = line.index('Q')
        poss[j] = 0
        if 0 <= j - (len(mt) - i) < n:
          poss[j - (len(mt) - i)] = 0
        if 0 <= j + (len(mt) - i) < n:
          poss[j + (len(mt) - i)] = 0
      # 进行下一步搜索
      for i, p in enumerate(poss):
        if p == 1:
          new_line = gen_line(i)
          tmp = mt.copy()
          tmp.append(new_line)
          r = helper(tmp)
          if r is not None:
            res.append(r)
      return None
    for i in range(n):
      r = helper([gen_line(i)])
      if r is not None:
        res.append(r)
    return res
