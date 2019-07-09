class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n > 0:
      if n % 2 == 0:
        f = False
      else:
        if n == 1:
          return x
        n = n - 1
        prev_x = x
        f = True
      if n // 2 > 0:
        n = n // 2
        if n != 0:
          r = self.myPow(x, n)
          x = r * r
      if f:
        x = x * prev_x
      return x
    elif n < 0:
      n = - n
      x = 1 / x
      return self.myPow(x, n)
    else:
      if x == 0:
        return
      else:
        return 1
