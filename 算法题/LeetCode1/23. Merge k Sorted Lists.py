# 合并k个有序链表
"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
"""
    解法1 
        这个解法在于你能不能知道 直接两个两个的合并
        第一次进来和空节点比较 然后值给result 第二次开始result和循环的元素合并
    解法2
        优化解法1的代码
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    这个方法其实是可以的 就是太慢了 超出时间显示
"""


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        result = None
        for i in range(0, len(lists)):
            curr = lists[i]
            if i == 0:
                heada = ListNode(0)
                p = heada.next
                result = self.hebin2(p, curr)
            else:
                result = self.hebin2(result, curr)
        return result

    def hebin2(self, result, curr):
        head = ListNode(0)
        p = head
        while result and curr:
            if result.val < curr.val:
                p.next = ListNode(result.val)
                p = p.next
                result = result.next
            else:
                p.next = ListNode(curr.val)
                p = p.next
                curr = curr.next
        while result:
            p.next = ListNode(result.val)
            p = p.next
            result = result.next
        while curr:
            p.next = ListNode(curr.val)
            p = p.next
            curr = curr.next
        return head.next


class Solution1:
    def mergeKLists(self, lists) -> ListNode:
        result = None
        for i in lists:
            result = self.hebin2(result,i)
        return result

    def hebin2(self, l1, l2):
        d = c = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                c.next, l1 = l1, l1.next
            else:
                c.next, l2 = l2, l2.next
            c = c.next
        c.next = l1 if l1 else l2

        return d.next
"""
    其实算法之路确实浩瀚如海
        以前我能想出来思路 就觉得很牛逼了 写出来代码更nice
        但是你有没有想过可以把自己的代码优化呢
    优化的步骤
        if else里面重复的代码能不能拿出来呢 
        三目运算符 是不是可以考虑用一用
        在上面优化的地方看 
            l1本来就是ListNode链表节点我们当初为什么要创建呢
            优化不香吗
            直接给他不香吗
        d = a  c = b 为什么不 c = b = a呢
        优化也是技术活
    注意一个点
        if 里面执行了某某 如果不return 下面的代码(if外面)会继续走  
            
"""