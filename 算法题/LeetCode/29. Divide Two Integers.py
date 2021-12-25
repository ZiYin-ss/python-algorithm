# 两数相除
"""
给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""
"""
    第一种自己的解法确实是可以的 但是超出时间限制了
    第二种解法
        能不能想到倍加 相应的商的值也倍加呗 cur += cur 这个确实牛逼 效率提高一半
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return "除数不为0"
        intt = -1
        divi = abs(dividend)
        divs = abs(divisor)
        while divi >= 0:
            divi -= divs
            intt += 1
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return intt
        else:
            return -intt


dividend = 7
divisor = -3
a = Solution()


# print(a.divide(2147483648, 2))


class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:

        # 将被除数和除数转化为正数
        sign = 1
        if divisor * dividend < 0:  # 如果符号不同，则结果返回要变成负数
            sign = -1
            divisor = abs(divisor)
            dividend = abs(dividend)

        elif divisor < 0 and dividend < 0:  # 如果被除数和除数都是负值，结果不修改符号
            divisor = abs(divisor)
            dividend = abs(dividend)

        remain = dividend  # 余数
        result = 0  # 商
        while remain >= divisor:
            cur = 1  # 倍增商
            div = divisor  # 倍增值
            while div + div < remain:
                # 最难的应该是这个循环 因为当你加一个div(是不断变大的) 而当你加一个div小于remain的时候其实 这个cur你就要加上上一个cur
                # 因为 后来会减去div 那么这些div对应的原来的除的话 就是cur 可以明白 但是没法解释
                # 就是3+3小于10 因为我们等会做减div的操作 那么自然这一部分是不是就把这个div对应的cur存起来(其实就是慢慢相减的商)
                cur += cur  # 这个地方真牛逼
                div += div
            remain -= div  # 余数递减
            result += cur  # 商值累计
        """
            这个地方没那么简单的 
                假如是10 3 进来 div会走到6  remain为6 result为2 那么在做 直接第while没法走 也就是 最后remain=0 result=3
                为什么会这样呢 当remain为6的时候 就不说了 因为这个都是正常走法 
                当走remain为6的时候之后 再外层while循环是不是就是 
                    div+div这个不满足是不是就是说 此时remain/div直接小于2了 但肯定大于一 外层控制的 所以最后加上cur即可啊
        """
        if sign == -1:
            result = -result

        if result >= 2 ** 31:
            result = 2 ** 31 - 1

        return result
"""
    上面说的差不多了 我就不说了
"""

a = Solution1()
print(a.divide(10, 3))
