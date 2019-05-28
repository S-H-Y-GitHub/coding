class Solution:
  def generate(self, numRows: int):
    res = []
    if numRows <= 0:
      return res
    for i in range(numRows):
      if i == 0:
        res.append([1])
        continue
      temp = []
      
      for j in range(i+1):
        if j-1 < 0:
          a = 0
        else:
          a = res[-1][j-1]
        if j > len(res[-1]) - 1:
          b = 0
        else:
          b = res[-1][j]
        temp.append(a+b)
      res.append(temp)
    return res
