# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, p):
        # write code here
        a=set()
        while(p is not None):
            
            if p in a:
                return p;
            a.add(p)
            p=p.next
        return None
