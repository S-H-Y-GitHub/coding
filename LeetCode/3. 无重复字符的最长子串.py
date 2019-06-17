class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    max_length = 0
    ctoi = {}
    temp = 0
    for i, char in enumerate(s):
      if char not in ctoi:
        ctoi[char] = i
        temp += 1
      else:
        for j in range(i-temp, ctoi[char]):
          del ctoi[s[j]]
        if max_length < temp:
          max_length = temp
        temp = i - ctoi[char]
        ctoi[char] = i
    if max_length < temp:
      max_length = temp
    return max_length
