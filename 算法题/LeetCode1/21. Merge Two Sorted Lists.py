# 合并两个有序链表
"""
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
"""
    这道题的解题思路在于你能不能想到
        假如l1小了 把l1的val放到新链表里面去 更新l1(l2千万不要动)
        反之亦然 
        因为你想啊 假如l1第一个和l2第一个比要是小了 那么l1第二个应该和l2的第一个比啊 这样才能确保有序啊
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        while list1 and list2:
            if list1.val < list2.val:
                p.next = ListNode(list1.val)
                p = p.next
                list1 = list1.next
            else:
                p.next = ListNode(list2.val)
                p = p.next
                list2 = list2.next
        while list1:
            p.next = ListNode(list1.val)
            p = p.next
            list1 = list1.next
        while list2:
            p.next = ListNode(list2.val)
            p = p.next
            list2 = list2.next
        return head.next
"""
    其实这道题确实不难 就在于有一个点你能不能想明白 只更新一个
    因为只有这样才能确保两个链表有序
    就写两个升序列表 自己比这玩就可以啦
"""