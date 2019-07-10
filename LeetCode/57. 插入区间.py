class Solution:
  def insert(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
    if len(intervals) == 0:
      return [newInterval]
    s = newInterval[0]
    e = newInterval[1]
    i = 0
    res = []
    if e < intervals[0][0]:
      res.append(newInterval)
    while i < len(intervals):
      start = intervals[i][0]
      end = intervals[i][1]
      if s < start <= e:
        start = s
      if s <= end < e:
        end = e
      while i + 1 < len(intervals) and end >= intervals[i + 1][0]:
        i += 1
        if end < intervals[i][1]:
          end = intervals[i][1]
      res.append([start, end])
      if s > end and (i + 1 == len(intervals) or e < intervals[i + 1][0]):
        res.append(newInterval)
      i += 1
    return res
  
