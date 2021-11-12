def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(60, 21))
"""
    欧几里得算法
        其实就是辗转相除法  求最大公约数
            gcd(60,21) = gcd(21,18) = gcd(18,3) = gcd(3,0) = 3
"""
"""
    利用欧几里得算法实现分数计算 
        实现分数类 支持分数四则运算
        这个是分数相加 然后出来之后还是一个分数 
        所以调用Fraction(fenzi,fenmu)
         这个类的__init__其实就是做的就是一个形成分数的过程 
         只不过用str打印了一下 
"""


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    @staticmethod
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    @staticmethod
    def zgs(a, b):
        # 12 16 ->4 16除12的余数是4
        # 3 * 4 * 4  12/4=3 16/4 = 4 相乘
        x = gcd(a, b)
        return a * b / x

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

    def __add__(self, other):
        #  都说了两个实例相加 会随便调用一个实例的 add方法 自己的a和b 和另外一个实例的a和b
        #  也就是说以后类相加 要把对应的属性可以运算的对应上 其实这个other就是另外一个实例
        #  other.a 就是另外一个实例上的属性 如果有c 还可以.c
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * fenmu / b + c * fenmu / d  # 其实这个地方把 分子扩大的倍数不就是分母扩大的倍数呗 分母扩大的倍数不就fenmu/原分母呗
        #  简单加减没什么好说的
        return Fraction(fenzi, fenmu)


a = Fraction(1, 3)
b = Fraction(1, 2)
print(a + b)  # 假如执行a的 add方法 返回了Fraction这个 因为print所以会执行他的__str__方法
