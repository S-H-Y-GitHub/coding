# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if(len(numbers)==0):
            return False
        import sys
        m=sys.maxsize
        c=0
        a=set()
        for n in numbers:
            if n<m and n>0:
                m = n
            elif n==0:
                c+=1
            if n not in a:
                a.add(n)
            elif n!=0:
                return False
        if(m==sys.maxsize):
            return True
        for m in range(m,max(numbers)):
            if m not in numbers:
                c-=1
        return c>=0
