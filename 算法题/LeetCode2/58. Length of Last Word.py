# 最后一个单词长度
"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        summ = 0
        for i in s:
            if i == " ":
                count = 0
            else:
                count += 1
                summ = count

        return summ

s = "   fly me   to   the moon  "
a = Solution()
print(a.lengthOfLastWord(s))


"""
    这道题总不用说了把
"""