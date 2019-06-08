class Solution:
  def combinationSum(self, candidates, target: int, sort=True):
    if sort:
      candidates = sorted(candidates)
    results = []
    for ind, i in enumerate(candidates):
      if i == target:
        results.append([i])
      if i < target:
        temp = self.combinationSum(candidates[ind:], target - i, False)
        for t in temp:
          t.append(i)
        results.extend(temp)
    return results
