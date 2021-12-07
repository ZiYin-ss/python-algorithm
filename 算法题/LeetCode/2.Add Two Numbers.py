#两数相加
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""
class Solution:
    def addTwoNumbers(self, l1,l2):
        """
        其实这个方法也挺快的 也可以按照题目的输入 但是你会错意了 他说必须要列表节点 你这样写类型都通不过啊
        """
        a = int(''.join(map(str,l1)))
        b = int(''.join(map(str,l2)))
        c = a+b
        d = list(str(c))
        d.reverse()
        c = list(map(int,d))
        return c


a = Solution()
l1 = [0]
l2 = [0]

b = a.addTwoNumbers(l1,l2)

print(b)