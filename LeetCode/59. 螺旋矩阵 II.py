class Solution:
  def generateMatrix(self, n: int):
    mat = [[0] * n for _ in range(n)]
    dirc = 'r'
    i = 0
    j = 0
    l_bound = 0
    r_bound = n - 1
    t_bound = 0
    b_bound = n - 1
    for num in range(1, n * n + 1):
      mat[i][j] = num
      if j == r_bound and dirc == 'r':
        dirc = 'b'
        t_bound += 1
      elif i == b_bound and dirc == 'b':
        dirc = 'l'
        r_bound -= 1
      elif j == l_bound and dirc == 'l':
        dirc = 't'
        b_bound -= 1
      elif i == t_bound and dirc == 't':
        dirc = 'r'
        l_bound += 1
      if dirc == 'r':
        j += 1
      elif dirc == 'l':
        j -= 1
      elif dirc == 't':
        i -= 1
      elif dirc == 'b':
        i += 1
    return mat
