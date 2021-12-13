# 电话号码的字母组合
"""
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
给出数字到字母的映射如下（与电话按键相同）。注意1不对应任何字母
"""
"""
    解题思路
        for循环是肯定需要的 但是你能不能想到 每次循环完之后都更新result 下次就是每个字符出来加上原来result的值
        这个确实不好理解
"""


class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        d = {
            '0': "0", '1': "1", '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        result = [""]  # 注意必须要是字符
        for i in digits:
            tmp_list = []
            for ch in d[i]:  # 1 abc   2 def
                for str in result:
                    tmp_list.append(str + ch)  # 1 a b c  2 ad bd cd
            result = tmp_list
        return result


"""
    其实这个地方又出来一个很重要的思想 
    当你不知道for循环的层数的时候 你可以先循环最根本的那个 然后在循环第二层(就是正常循环的第二层) 第三层就是循环结果了 每次更新结果 
    上面的方法 真的可以 
"""

a = "23"
b = Solution()
print(b.letterCombinations(a))
