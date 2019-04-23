def rand_partition(a, p, r):
  i = np.random.randint(p, r + 1)
  x = a[i]
  m = p - 1
  n = p - 1
  for j in range(p, r + 1):
    if a[j] < x:
      m += 1
      n += 1
      a[m], a[j] = a[j], a[m]
      a[n], a[m] = a[m], a[n]
    elif a[j] == x:
      m += 1
      a[m], a[j] = a[j], a[m]
  
  return m + 1, n + 1


def quick_sort(a, p, r):
  if p < r:
    m, n = rand_partition(a, p, r)
    quick_sort(a, p, n - 1)
    quick_sort(a, m, r)
