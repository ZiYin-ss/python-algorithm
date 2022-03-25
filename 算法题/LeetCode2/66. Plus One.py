# 加一
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution:
    def plusOne(self, digits):
        lst = list(map(str, digits))
        lst1 = list(str(int(''.join(lst)) + 1))
        return list(map(int, lst1))


a = Solution()
print(a.plusOne([1, 2, 3]))
