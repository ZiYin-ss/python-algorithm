# 回文数
"""
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""
"""
    这道题比较简单 要是用字符串做的话 
        其实就是把中间的那一个数传进出两边散开找 到最后回文的条件就是 走到最后l=-1 r=len(a)
        或者中间两个数就是把左右都传进去呗  回文条件都一样
    要是不用字符串做的话
       你就得明白折半到最后 余数*10出来的值和你最后的x一样 
       这个地方 思维要求是真的高 
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if len(a) % 2 == 1:
            return self.getlongestpalindrome(a, len(a) // 2, len(a) // 2)
        if len(a) % 2 == 0:
            return self.getlongestpalindrome(a, len(a) // 2 - 1, len(a) // 2)

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        if l == -1 and r == len(s):
            return True
        return False


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            import math
            length = int(math.log(x, 10)) + 1  # 返回这个整型的长度
            reverse_x = 0
            for i in range(length // 2):  # 折半就可
                remainder = x % 10  # 每次会把最后一个余数出来 1  3  2
                x = x // 10  # 余数出来之后就是更新x就可以了 132231==>13223  13223==>1322  1322==>132
                reverse_x = reverse_x * 10 + remainder  # reverse_x = 1  13  132
                #  这个此时你有没有发现就是 x = reverse了
                #  假如要是奇数 x = 1321 reverse_x = 132 啊
                # 当x为奇数时, 只要满足 reverse_x == x//10 即可
            if reverse_x == x or reverse_x == x // 10:
                return True
            else:
                return False


"""
    明白到最后这个x = reverse = 132就可以的                
"""

a = Solution1()
print(a.isPalindrome(132231))

"""
   math.log(64,2) = 6
        这个叫做以2为底64的对数
        log(N,x)
        以x为底N的对数 
   math.log(N,10)
        这个可以理解为10的多少次方取得到N(地板除+1(不懂就理解为公式 也很好理解))
        假如十的三次方是1000那么多的就是3.xxx那么三位不够肯定要四位 加一 并且 一千的时候 为2.999999999这样的数还是加一
         
"""


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = abs(x)
        while a != 0:
            b = a % 10
            num = num * 10 + b
            a = a // 10

        if a >= 0 and x == num:
            return True
        else:
            return False
