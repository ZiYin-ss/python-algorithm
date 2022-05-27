# 最小覆盖字串
"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
    对于t中重复字符，我们寻找的子字符串中该字符数量必须不少于t中该字符数量。
    如果s中存在这样的子串，我们保证它是唯一的答案。
"""
import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = dict(collections.Counter(t))  # 假如t是"ABBC"那么就会返回 {"A":1,"B":2,"C":1} 就是把字符串里面计数 然后形成一个计数字典
        formed = 0
        slow = 0
        min_str = None
        min_length = sys.maxsize - 1  # 最大值
        for fast in range(len(s)):
            ch = s[fast]
            fast += 1  # 这个地方加1是不会影响for循环的fast的
            if ch not in d:  # 这个是判断ch这个字母 在不在d字典的key里面
                continue
            d[ch] -= 1
            if d[ch] == 0:
                formed += 1
            while formed == len(d) and slow <= fast:
                curr_length = fast - slow
                if curr_length < min_length:
                    min_length = curr_length
                    min_str = s[slow:fast]  # 为什么fast+1 因为这个地方要取值
                ch = s[slow]
                slow += 1
                if ch not in d:
                    continue
                d[ch] += 1
                if d[ch] == 1:
                    formed -= 1
        return min_str if min_str is not None else ""
"""
    这到题肯定是很难的 但是主要还是看方法
        s = "ADOBECODEBANC"
        t = "ABC"
        1.拿s和t来举例 首先遍历s的第0的字符A然后在t里面 把t转换为一个计数字典(某某字符出现了多少次就这)
        2.如果在t里面就把对应的计数减一同时把formed+1(只有计数为0才加一) 如果不在继续下一次就可以啦
        3.重点来了 那么如果formed=字典的元素个数 那么说明都已经出现 接下来就是找最短了的 
        4.在while里面 先把最短的赋值出来 继续从左边开始 如果slow当前位置的字符不在字典里面 那么slow加一就可以了啊(会缩短距离) 会继续循环
        5.如果在(假设是A)那么就把字典对应的key值加一同样while循环会退出 继续往下面走然后如果出现了A同样又会进入while循环 比较大小
        6.如果小自然就更新 继续第4步第五步 如果还是不懂 建议你可以带入自己走一遍就知道了
    如果走懂了 说明也不难
"""

s = "ADOBECODEBANC"
t = "ABC"
a = Solution()
print(a.minWindow(s, t))
