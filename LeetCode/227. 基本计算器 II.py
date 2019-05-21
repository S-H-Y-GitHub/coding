class Solution:
  def calculate(self, s: str) -> int:
    symbols1, symbols2 = {'+', '-'}, {'*', '/'}
    parts = []
    temp = []
    flag = False
    for c in s:
      if c in symbols1:
        parts.append(int(''.join(temp)))
        if flag:
          num1 = parts.pop()
          op = parts.pop()
          num2 = parts.pop()
          parts.append(self.cal(num2, num1, op))
        while len(parts) > 1:
          num1 = parts.pop(0)
          op = parts.pop(0)
          num2 = parts.pop(0)
          parts.insert(0, self.cal(num1, num2, op))
          
        parts.append(c)
        flag = False
        temp = []
      elif c in symbols2:
        parts.append(int(''.join(temp)))
        if flag:
          num1 = parts.pop()
          op = parts.pop()
          num2 = parts.pop()
          parts.append(self.cal(num2, num1, op))
        parts.append(c)
        flag = True
        temp = []
      elif c.isdecimal():
        temp.append(c)
    parts.append(int(''.join(temp)))

    if flag:
      num1 = parts.pop()
      op = parts.pop()
      num2 = parts.pop()
      parts.append(self.cal(num2, num1, op))
    while len(parts) > 1:
      num1 = parts.pop(0)
      op = parts.pop(0)
      num2 = parts.pop(0)
      parts.insert(0, self.cal(num1, num2, op))
      
    return parts[0] if len(parts) == 1 else 0
  
  def cal(self, num2, num1, op):
    if op == '+':
      return num2 + num1
    elif op == '-':
      return num2 - num1
    elif op == '*':
      return num2 * num1
    elif op == '/':
      return num2 // num1
