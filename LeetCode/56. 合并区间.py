class Solution:
  def merge(self, intervals: 'List[List[int]]') -> 'List[List[int]]':
    if len(intervals) == 0:
      return []
    intervals = sorted(intervals)
    res = []
    i = 0
    while i < len(intervals):
      start = intervals[i][0]
      end = intervals[i][1]
      while i + 1 < len(intervals) and intervals[i + 1][0] <= end:
        i += 1
        if end < intervals[i][1]:
          end = intervals[i][1]
      res.append([start, end])
      i += 1
    return res
