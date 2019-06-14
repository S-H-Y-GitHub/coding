def lcs(a, b):
  if len(a) == 0 or len(b) == 0:
    return 0
  m = [[0] * (len(a)+1)] * (len(b)+1)
  for i in range(len(a)):
    for j in range(len(b)):
      x = max((m[i+1][j], m[i][j], m[i][j+1]))
      if a[i] == b[j]:
        m[i+1][j+1] = x + 1
      else:
        m[i+1][j+1] = x
  return m[-1][-1]
