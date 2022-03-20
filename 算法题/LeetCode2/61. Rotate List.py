# 旋转列表
"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head:
            if head.next:
                if head.next.next:
                    n = 0
                    z = head
                    while z:
                        n += 1
                        z = z.next
                    k = k % n
                    while k > 0:
                        tmp = head.next
                        while tmp.next.next is not None:
                            tmp = tmp.next
                        p = tmp.next
                        p.next = head
                        tmp.next = None
                        head = p
                        k -= 1
                if head.next.next == None:
                    if k % 2 == 1:
                        tmp = head.next
                        tmp.next = head
                        head.next = None
                        head = tmp
        return head
# 可以用了

# 从这个地方开始就不写解题思路了  不需要了 能看的懂题目 也能知道大概什么意思了 有想法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def rotateRight(self, head, k: int):
        if head is None or head.next is None:
            return head
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        k = k % n
        if k == 0:
            return head
        p1, p2 = head, head

        for i in range(k):  # 其实这个地方就是for循环一个转换数
            p2 = p2.next
        while p2 and p2.next:  # 这个地方按照样例理解 其实for之后 偏移就写出了
            p1 = p1.next
            p2 = p2.next
        output = p1.next
        # 为什么要平移 其实是说 要是for四次的话 是不是就是最后一位 那么掐断之 是不是刚好是23451啊 对不 前面和后面相加其实是刚好的
        # 刚好和位置对应把
        p1.next = None
        p2.next = head
        return output


"""
    其实这个是最终版的 
"""
