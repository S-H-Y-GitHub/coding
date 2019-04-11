# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        a=set()
        for i in array:
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        return list(a)
