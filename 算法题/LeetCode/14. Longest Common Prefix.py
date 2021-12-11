# 最长公共前缀
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""
"""
    第一种思路
        就是把第一个当标杆 去比较 只不过我tm不知道咋写代码 tm的 唯一注意的就是第一个字符大于后面的或者小于后面的怎么办
    第二个思路就是说你
        能不能想到每个位一样的话 单独把位取出来集合去重
        加进去顺便更新索引一直执行
    核心思想在于每个位
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    # 当当前这个字符不相等的时候返回的肯定是第0个字符的【0：i】位 取不到i
                    # 当这个i大于等于这个长度的时候是不是就已经取不到了 返回的不还是[0:i]吗
                    return strs[0][:i]

        return strs[0]
        # 这个里面还包含了一种情况就是说当第一个比后面的小的时候 如果前面for循环没有return值的话 是不是就是第一个是最长的了啊


strs = ["flo", "flor"]
a = Solution()
print(a.longestCommonPrefix(strs))


class Solution1:
    def longestCommonPrefix(self, strs):
        result = ''
        i = 0
        while True:
            try:
                a = set(string[i] for string in strs)  # 集合是不是去重啊 要是对应的每个位字符一样的话每次是不是就是一啊
                if len(a) == 1:
                    result += strs[0][i]
                    i += 1
                else:
                    break
            except Exception as e:  # 防止[""] 为什么这个不行呢 会一直死循环 None
                break
        return result


strs = [""]
a = Solution1()
print(a.longestCommonPrefix(strs))
