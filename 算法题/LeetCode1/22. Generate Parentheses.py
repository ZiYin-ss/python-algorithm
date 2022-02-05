# 括号生成
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
"""
    其实这道题的思想在于能不能想到要递归
        只要右边剩余小于左边就终止
"""


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result):
        if r < l:  # 这个地方是重点 其实可以画图看 只要右边的")" 小于左边的"(" 必错
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l - 1, r, item + '(', result)
        if r > 0:
            self.helper(l, r - 1, item + ')', result)

"""
    递归是真的想不到 
    其实你一定要明白 做算法题一定是有某些条件是你要找到的 不可能说没有什么关键条件 
    还有就是思想的应用 确实牛逼 
"""