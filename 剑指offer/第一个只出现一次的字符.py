# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        a={}
        for i, ch in enumerate(s):
            if ch not in a:
                a[ch] = i
            else:
                import sys
                a[ch] = sys.maxsize
        if len(a)>0:
            return min(a.values())
        else:
            return -1
