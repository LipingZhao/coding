# -*- coding:utf-8 -*-
'''
题目描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 用程序实现深拷贝 不能直接赋值，否则会返回空
        if pHead is None:
            return None
        #1. 完成链表结点赋值和指针重指向
        p = pHead
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = p.next.next
        #2. 复制random指针
        p = pHead
        while p:
            # random有可能是None!!!
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        #3. 分离两个链表 【p2不能动】
        p1 = pHead
        p2 = pHead.next
        p3 = pHead.next
        while p1:
            p1.next = p1.next.next
            if p3.next:
                p3.next = p3.next.next
                p3 = p3.next
            p1 = p1.next
        return p2


    
