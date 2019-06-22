class Solution:
  def maxArea(self, height) -> int:
    max_size = -1
    start = 0
    end = len(height) - 1
    while end > start:
      size = min(height[start], height[end]) * (end - start)
      if max_size < size:
        max_size = size
      if height[start] < height[end]:
        start += 1
      else:
        end -= 1
    return max_size
