# 整数翻转
"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231,231− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
"""
"""
    这道题没什么好说的 其实比较简单 就是说直接翻转不就可以了呗 正负注意一下呗
    所谓的2的31次方 就是数的大小不能超过这么大
"""


class Solution:
    def reverse(self, n: int) -> int:
        if n > 0:
            a = self.matha(n)
            return a
        else:
            n *= -1
            a = self.matha(n)
            return int(a) * -1

    def matha(self, n):
        a = str(n)
        a = int(a[::-1])
        if a > 2 ** 31:
            return 0
        return a


a = Solution()
print(a.reverse(123))
