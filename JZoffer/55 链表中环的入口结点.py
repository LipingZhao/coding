# -*- coding:utf-8 -*-
'''
重复结点不保留！！
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        # 难点在于确定第一个结点的位置
        # 做法：添加一个头结点
        head = ListNode(0)
        head.next = pHead
        pre = head
        p = head.next
        while p and p.next:
            if p.val == p.next.val:
                while p.next and p.val == p.next.val:
                    p.next = p.next.next
                pre.next = p.next
            else:
                pre = p   
            p = p.next
        return head.next

# x = ListNode(1)
# x.next = ListNode(1)
# x.next.next = ListNode(1)
# x.next.next.next = ListNode(1)
# x.next.next.next.next = ListNode(4)
# x.next.next.next.next.next = ListNode(4)
# x.next.next.next.next.next.next = ListNode(5)

# res = deleteDuplication(x)
# print(res)