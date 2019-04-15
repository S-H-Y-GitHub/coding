# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False
        import re
        return re.match(r'\A[+-]?\d*(\.\d+)?([eE][+-]?\d+)?\Z', s)
