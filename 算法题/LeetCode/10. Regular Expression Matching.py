# 正则表达式匹配
"""
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串
"""
"""
    这道题的解题思路就在于 前置的为空匹配 
    当进入第二个if的时候 *号的处理 
    这道题暂时不要求 确实难 
    但是通过这道题知道了动态规划的精髓也是不亏的 
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        cache[0][0] = True
        for i in range(1, len(p)):
            cache[i + 1][0] = cache[i - 1][0] and p[i] == '*'  # 其实这一行就是p对s的空匹配 匹配的条件就是p的下一个为*(0个或多个匹配0个是空 )
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    cache[i + 1][j + 1] = cache[i][j + 1] or cache[i - 1][j + 1]
                    # 这个地方就是匹配*号的0位或多位 当是0位或一位的时候下面的更新对应的True 其实就是①的前置条件
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        cache[i + 1][j + 1] |= cache[i + 1][j]
                        #  碰到*的时候(要匹配多个的时候) 看前面(一列)那一位匹配上了没有(匹配条件上面说了)    ①
                        #  换句话说 其实就是遇到是* 而且开始匹配多个 进了这个if里面之后 就是看前一列是true不是
                else:
                    cache[i + 1][j + 1] = cache[i][j] and (p[i] == s[j] or p[i] == '.')  # cache[i][j] 右上方都匹配不过来可咋整啊
        return cache[-1][-1]


a = Solution()
print(a.isMatch("abbba", "ab*a"))
