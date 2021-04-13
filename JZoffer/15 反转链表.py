# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        if not pHead:
            return None
        beg = None
        mid = pHead
        end = pHead.next
        while True:
            mid.next = beg
            if end is None:
                break
            beg = mid
            mid = end
            end = end.next
        return mid

