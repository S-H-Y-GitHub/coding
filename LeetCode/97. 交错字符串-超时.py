class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s3) == 0:
      if len(s1) == 0 and len(s2) == 0:
        return True
      else:
        return False
    if len(s1) == 0:
      if s2 == s3:
        return True
      else:
        return False
    if len(s2) == 0:
      if s1 == s3:
        return True
      else:
        return False
    if s1[0] == s3[0]:
      if s2[0] == s3[0]:
        return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
      else:
        return self.isInterleave(s1[1:], s2, s3[1:])
    else:
      if s2[0] == s3[0]:
        return self.isInterleave(s1, s2[1:], s3[1:])
      else:
        return False
