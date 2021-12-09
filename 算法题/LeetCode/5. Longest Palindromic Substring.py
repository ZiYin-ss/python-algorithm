# 最长回文子串
"""
    给你一个字符串 s，找到 s 中最长的回文子串。
"""
"""
    这个地方的解题思路在于 中间散开 无论是bb和bab 都是从中间散开找 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP动态规划 每次都把这个最长的回文子串一次一次更新保存
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)

            """
                这个地方是两个情况 但是这两个情况(bab bb) 又没法判断 还不如就直接走呗
                这个地方你不要犹豫说两个条件什么的 就当正常执行程序 bab类型会走上面的得到最大值 bb类型会走到下面的得到最大值
                每个i走完都走到底此时会得到子串看看有没有palindrome大  当把所有i走完自然就知道最大的子串了呗
            """


            len2 = len(self.getlongestpalindrome(s, i, i+1))
            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i+1)
            # 无论走那个条件你都会发现 这个palindrome都是实时保证最大的

        return palindrome

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
        # 这个地方是while之后还会加一减一 然后判断不是 此时l和r都是加减之后的值了得取到l后面一个r前面一个
        # 还有一个关注的边界处理 这个地方也处理好了 -1 和len(s)  返回的不就是 0到len(s)-1呗 边界不是问题
