# 字符串相乘
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式
"""

"""
    第一种方式就不说了 因为都不让用
    第二种方式就是能不能明白乘法的规律 
        个位*个位=个位 个位*十位=十位 个位*百位=百位 十位*十位=百位 十位*百位=千位 百位*百位=万位
        0+0=0       0+1=1       0+2=2       1+1=2        1+2=3      2+2=4  能不能明白这个规律
        刚好对应的就是 列表中对应的位置 懂? [个,十,百,千,万]
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        mul = [0] * (len(num1) + len(num2) + 1)
        res = ""
        for k1, v1 in enumerate(num1[::-1]):
            for k2, v2 in enumerate(num2[::-1]):
                mul[k1 + k2] += int(v1) * int(v2)
        for k, v in enumerate(mul):  # 这个里面的代码 其实很简单 就是说 本来是逆序的 然后就是
            if v < 9:
                res = str(v) + res  # 这个地方顺序正常过来的
            else:
                res = str(v % 10) + res  # 这个地方就是说 算大小 大于10了前面就要进位
                mul[k + 1] += v // 10
        return res.lstrip('0')  # 前面的0不要


"""
以 123 456 为例
18  15  12 
    12  10  8
        6   5   4
18  27  28  23  4   0   0

        4   5   6
        1   2   3   *
        -------------
        12   15   18 
    8   10   12
4   5    6

再™明白这个过程是什么意思吗  要找规律知道吗 第0位和第0位乘的位置永远在第0位啊 第0位和第1位乘 不就在第1位吗  依次类推啊 第三位与第三位乘不就是第五位吗
倒序无非不就是前面的先加到字符串里面 后面的加上前面的呗  res = str(v) + res 
而 前面一位多了往后面进位不就是的呢  一定要明白规律 这道题就好做了
"""
num1 = "123"
num2 = "456"
a = Solution1()
print(a.multiply(num1, num2))
