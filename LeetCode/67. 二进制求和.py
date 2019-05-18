class Solution:
  def addBinary(self, a: str, b: str) -> str:
    i = 0
    la = len(a) - 1
    lb = len(b) - 1
    res = ''
    temp = None
    while True:
      cur = []
      if i <= la:
        cur.append(a[la-i])
      if i <= lb:
        cur.append(b[lb-i])
      if temp is not None:
        cur.append(temp)
      count1 = 0
      for c in cur:
        if c == '1':
          count1 += 1
      if count1 == 0:
        temp = '0'
        res = '0' + res
      elif count1 == 1:
        temp = '0'
        res = '1' + res
      elif count1 == 2:
        temp = '1'
        res = '0' + res
      elif count1 == 3:
        temp = '1'
        res = '1' +res
      i += 1
      if i > la and i > lb and temp != '1':
        return res
