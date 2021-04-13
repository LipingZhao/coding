# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        p1, n_p1 = pHead1, 0
        p2, n_p2 = pHead2, 0
        while p1:
            p1 = p1.next
            n_p1 += 1
        while p2:
            p2 = p2.next
            n_p2 += 1
        if n_p1 < n_p2:
            p1, p2 = pHead2, pHead1
        else:
            p1, p2 = pHead1, pHead2
        
        for _ in range(abs(n_p1-n_p2)):
            p1 = p1.next
        
        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None