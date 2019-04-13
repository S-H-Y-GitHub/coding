# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        t=0
        if n<1 or m<1:
            return -1
        a=[i for i in range(n)]
        while True:
            if len(a)==1:
                return a[0]
            i=0
            while i < len(a):
                if t==m-1:
                    del a[i]
                    i-=1
                    t=-1
                t+=1
                i+=1
         
