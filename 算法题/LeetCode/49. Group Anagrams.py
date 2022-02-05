# 字母异位词分组
"""
    给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
    字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
"""
"""
    解题思路就在于能不能想到用字典 把排序后的字符串作为key 
        strs里面的元素 当他排序之后看看有没有和key是一样的 然后添加到对应的key里面
"""


class Solution:
    def groupAnagrams(self, strs):
        solution = {}
        if len(strs) < 1:
            return strs
        else:
            for i in range(len(strs)):
                reg = strs[i]
                regsort = "".join(sorted(reg))  # 这个reg是字符串 也是可以排序的按照a-z的顺序排序 然后分割为列表
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    solution[regsort] = [reg]
        return list(solution.values())  # 这个字典的.values() 返回的就是字典里面所有值组成的列表但是这个列表不能直接用是字典值我们需要list一下 keys同理


"""
    先说一下题目是什么意思 其实就是 同一个列表里面的字符串 单词要一样 但是排列不一样 而且原列表中还要有 分组出来
        能知道是什么就好 不好说的
"""
"""
    其实看见有分组的思想 就要想到用字典 
    然后字符串也是可以排序的 如果单词一样的话 那么排序之后是不是也是一样的 这个不就可以当key了 
        regsort = "".join(sorted(reg)) 
    然后添加进去呗 
        solution[regsort].append(reg)  存在的话添加进去不就可以了吗
        solution[regsort] = [reg]  这个地方假如没有的话那么这个key的值就是列表
    这个其实不难 就是思想比较重要
"""
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
"""
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
a = Solution()
print(a.groupAnagrams(strs))
