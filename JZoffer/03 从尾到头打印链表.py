# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 先反转链表再打印
        if listNode is None:
            return []
        beg = None
        mid = listNode
        end = listNode.next
        while True:
            mid.next = beg
            if end is None:
                break
            beg = mid
            mid = end
            end = end.next
        
        res = []
        while mid is not None:
            res.append(mid.val)
            mid = mid.next
        return res

