def check(t):
  if len(t) == 0:
    return []
  res = []
  for i, word in enumerate(t):
    right = check(t[i+1:])
    for per in right:
      per.append(word)
    res.extend(right)
  for word in t:
    res.append([word])
  
  return res
