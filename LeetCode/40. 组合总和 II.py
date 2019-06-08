class Solution:
  def combinationSum2(self, candidates, target: int, sort=True):
    if sort:
      candidates = sorted(candidates)
    results = []
    t1 = None
    for ind, i in enumerate(candidates):
      if i == t1:
        continue
      t1 = i
      if i == target:
        results.append([i])
      if i < target:
        temp = self.combinationSum2(candidates[ind+1:], target - i, False)
        for t in temp:
          t.append(i)
        results.extend(temp)
    return results
