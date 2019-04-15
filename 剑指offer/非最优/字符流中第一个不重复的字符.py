# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.a=set()
        self.b=set()
        self.l=[]
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for c in self.l:
            if c not in self.b:
                return c
        return '#'
        
        
    def Insert(self, char):
        # write code here
        self.l.append(char)
        if char in self.a:
            self.b.add(char)
        self.a.add(char)
        
