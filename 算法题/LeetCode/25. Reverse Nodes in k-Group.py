# k个一组翻转链表
"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
    你可以设计一个只使用常数额外空间的算法来解决此问题吗？
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
"""
    有难度的 
    解题思路在于你能不能想到 swap的for循环怎么写(里面的逻辑到还好) 还有就是while的for循环 这个思路是怎么处理的
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        dump = ListNode(10086)
        dump.next = head
        end = prev = dump

        def swap(prev, k, end):  # prev.next 到end 就是翻转的元素
            after = end.next
            move = prev.next
            prev.next = end  # 这个地方是说把最后一个元素给到第一个位置  都是翻转元组的前提下
            temp = move.next
            end = move  # 这个地方结合下面end.next = after 看就知道只是把要移动的第一个元素放到了最后
            for i in range(k - 1):
                # 重点  为什么这样for循环呢 因为假如4个剩下是不是3(有一个外面移动了)个 移动三(k-1)次 以此类推
                # 这个是从x2到x4  那么从x4到x2肯定也可以的
                tnext = temp.next
                temp.next = move
                move = temp
                #  这个地方是这个意思  前面第一次移动只是 把x2的下一个是x1 做了这个改变
                #  但是for循环啊 哥哥 第二次for循环开始的时候 move是x2 temp是x3 走入for循环 把x4给了tnext x3的下一个是x2 做了这个改变
                #  第三次for循环(k为4)之前 temp = x4 move是不是就是x3 x4的下一个是不是就是x3了
                #  走完其实move和temp和tnext都没用了
                temp = tnext
            end.next = after
            return end

        while True:
            try:
                for _ in range(k):  # 这个地方其实就是 for循环之后 end走到了第k个地方
                    end = end.next  # 假如k是4 那么for走完之后 end指向的就是第四个节点
                prev = end = swap(prev, k, end)  # 这个函数会返回end  就是最后那个位置 也就是下一个的prev
                # 这个地方就不需要判断剩下多的了 没了其实没有改
            except:
                break
        return dump.next
"""
     有个思想 就是说 k组 你是不是就是把整体 可以先for循环把k个取出来啊 然后只是做这几个节点的处理啊 
     相对于链表来说 这几个节点处理是不会影响整体的啊(因为在里面我们把end.next取出来放到该放的地方了啊)
     整体到局部 一般到特殊 就是这个思想 
     确实有难度 
     其实动态规划要是会的话 这个比动态规划难
"""