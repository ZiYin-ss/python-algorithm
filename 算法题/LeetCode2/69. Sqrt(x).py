# x平方根
"""
给你一个非负整数 x ，计算并返回x的算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        for i in range(x // 2 + 1):
            if i == 0:
                continue
            if i ** 2 <= x < (i + 1) ** 2:
                return i


a = Solution()
print(a.mySqrt(36))

# 可以过 但是会超时 why?
class Solution1:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:  # 假如left为2 2的平方是4不大于4的 得再加一就是3 最后得减一
                left = mid + 1
        return left - 1
#  典型得二分法啊 懂? 不难得