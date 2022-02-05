# 删除链表的倒数第N个节点
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
"""
    解题思路
        第一种 在于你能不能想到 获取整个长度然后不就是减去n 不就达到了正向删除呗
        第二种 在于你能不能想到第一个(left)和n(reft)差多少 那么最后left是不是就是倒数的位置(当n走完了)
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 获取链表长度
        temp = head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        # 当删除最前面的节点时
        if n == i:
            return head.next
        # 删除节点
        else:
            exec("head" + ".next" * (i - n) + "=" + "head" + ".next" * (i - n + 1))
            return head

class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        leftNode = rightNode = head
        for i in range(n):
            rightNode = rightNode.next
        if not rightNode:
            return head.next  # 这里别忘了要特判
        while rightNode.next:
            rightNode = rightNode.next
            leftNode = leftNode.next
        leftNode.next = leftNode.next.next
        return head

