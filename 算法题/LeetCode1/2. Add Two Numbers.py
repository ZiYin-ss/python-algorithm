# 两数相加
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""


class Solution1:
    def addTwoNumbers1(self, l1, l2):
        """
        其实这个方法也挺快的 也可以按照题目的输入 但是你会错意了 他说必须要列表节点 你这样写类型都通不过啊
        """
        a = int(''.join(map(str, l1)))
        b = int(''.join(map(str, l2)))
        c = a + b
        d = list(str(c))
        d.reverse()
        c = list(map(int, d))
        return c


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)

        return dummy.next

"""
    其实这道题我昨天夜晚画的是不是也画出来了 
    但是我在第一个while里面做了两个if  其实没有必要 因为设置一个carry就可以了为0呗都加不影响的 
    其实这个地方你要理解链表你就知道是为什么了 
        每个节点加起来放到一个新节点里面 next一下就可以呗
    注意返回的是 dummy的下一个节点 因为第一个节点是0没有一样 为什么这样写是因为你不这样写你还能怎么写?
    然后就是carry位的处理 首先while里面都加起来的 就算这次加完carry有值在单个中一样用 就这了
    最后要是carry是1是不是还要多一个节点啊 就这 返回dummy下一个
    
    其实这个真不难
"""
