# Pow(x, n)
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。
"""
"""
    第一种方式是一个简易的求平方函数 正负都可以 0也可以 
        但是加上浮点数怎么办呢? 不用管 因为就是说多来几个0也没事
        超出时间限制了 他喵的
    第二种方式
        思路都一样 就是正负区分呗  用了位运算符呗 就这
"""


class Solution:
    def myPow(self, x, n):
        if x == 0:
            return "0的平方是什么?"
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            res = x
            for i in range(n):
                if i == 0:
                    res *= 1
                else:
                    res *= x
            return res


# a = Solution()
# print(a.myPow(0.00001,2147483647))


class Solution1:
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        track = x
        while n > 0:
            if n & 1:  # 按位于 就是把n和1都换成二进制然后就是按位比较然后返回1或者0 要不要更新值
                res *= track
            track *= track
            # 这个地方的意思就是 下面按位之后其实就是折半了 用的是折半的次数 8的话
            # 折半4 2 1 是不是就是乘以3次了 每次更新track不就可以了吗
            # 也就是 二的二次方 乘以二的二次方吗 不就是二的四次方吗 就这个意思 上面的n&1 就是最后一次折半出来的1(也就是0次方)
            # 确实有点难度
            n >>= 1  # 二进制位右移 就是1010 右移之后是 0101 就是5
        return res


"""
    第二个方法利用的是什么呢 就是 2的十次方是不是就是两个2的五次方相乘啊  直接把时间缩短为一半 是不是很牛逼啊
    还有就是这特么谁想的出来 啊 牛逼
"""

a = Solution1()
print(a.myPow(2, 8))
