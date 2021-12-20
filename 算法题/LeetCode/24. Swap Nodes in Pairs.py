# 两两交换链表中的节点

"""
    给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""
"""
    解题思路
        这一种在于你能不想到 p.next = tmp.next 这个我没法解释 想知道 自己走一遍就知道
        有其他的解法 而且还比这个简单 但是多了解没坏事
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        new_start = p.next
        while True:
            q = p.next  # q = 2 3 4  p = 1 2 3 4
            tmp = q.next  # tmp = 3 4
            q.next = p  # q = 2 1 2 3 4
            if not tmp or not tmp.next:
                p.next = tmp
                break
            p.next = tmp.next  # p = 1 4  q = 2 1 4 newstart = 2 1 4
            p = tmp
        return new_start

"""
    其实这道题真的想了好久 忘了一个点 就是节点修改 你把这个节点修改了 是不是所有的都修改了啊 
    不要迷啊 不要迷 真的很重要
"""