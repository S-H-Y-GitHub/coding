# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, p):
        # write code here
        s=[]
        a=[p]
        i=0
        while True:
            b=[]
            s2=[]
            for p in a:
                if p is not None:
                    s2.append(p.val)
                    b.append(p.left)
                    b.append(p.right)
            if len(s2) == 0:
                break
            a=b
            if i == 0:
                s.append(s2)
                i=1
            else:
                s.append(list(reversed(s2)))
                i=0
        return s
