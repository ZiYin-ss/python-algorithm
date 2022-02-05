# 实现strStr()
"""
实现strStr()函数。
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回-1 。
"""
"""
    解题思路就是说 能不能想到直接整体比较 不要拿指针比 这样比较简便
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):  # 当你画图的时候你会发现 就是减去他然后加一就会取到所有的值 写了也没事
            if haystack[i:i + len(needle)] == needle:  # 为什么上面可以取到 因为这个地方 i+len(needle)
                #  说个语法 其实 a[x:xxx] 就算xxx超界也不会报错 只是返回后面所有的值
                return i
        return -1


"""
    解法真的有很多 哪怕一边给一个指针 都能做 但是还是想要最简单的吗
"""