# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = pHead
        slow = pHead
        while True:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                break
        
        p = pHead
        while p!=slow:
            p = p.next
            slow = slow.next
        return p
        
                