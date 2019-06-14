class Solution:
  def generateParenthesis(self, n: int):
    left = n
    right = n
    
    def helper(left, right):
      if right >= left > 0 and left + right > 0:
        res = []
        
        l = helper(left - 1, right)
        for i in l:
          i.append(')')
        res.extend(l)
        
        r = helper(left, right - 1)
        for i in r:
          i.append('(')
        res.extend(r)
        return res
      elif left == 0:
        return [['(']*right]
      return []
    res = helper(left, right)
    for i in range(len(res)):
      res[i] = ''.join(res[i])
    return res
