class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        res = c.most_common(k)
        r = []
        for i,j in res:
          r.append(i)
        return r
