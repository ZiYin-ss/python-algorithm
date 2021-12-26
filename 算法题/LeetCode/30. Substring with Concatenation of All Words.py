# 串联所有单词的子串
"""
给定一个字符串s和一些 长度相同的单词words 。找出 s中恰好可以由words中所有单词串联形成的子串的起始位置。
注意子串要与words中的单词完全匹配，中间不能有其他字符 ，但不需要考虑words中单词串联的顺序。
"""
"""
    先说解题思路 就是从字符串0的位置开始循环 按照words里面单词长度来循环  一个start 一个移动的指针 每次移动word的长度 
    那个移动的指针移动后会把start到移动的地方都保存下来 看看和words是不是一样 不一样就 先移动移动的指针再移动start 
    一样的就保存start的值 0循环完之后从1继续循环 以此类推
    其实里面有个无意义的地方 就是一定要明白为什么先移动移动的指针在移动start 这样才可以保证每个情况都访问到  注意这个点还可以的
    能不能想到按照word长度循环
"""


class Solution:
    def findSubstring(self, s: str, words):
        if len(words) == 0:  # 特判
            return []
        unilen = len(words[0])  # 判断words里面元素的长度
        res, sets = [], {}
        for word in words:  # 给words里面的单词什么的 就计数 什么单词出现了几次
            sets[word] = sets.setdefault(word, 0) + 1  # setdefault这个是取不到值给默认值 还有get也一样
        for i in range(unilen):
            # 为什么循环单词的长度就行了呢  因为当i是0 unilen是3的时候 那么 其实第四位的数是不是在i为0的时候已经遍历过了啊  每次加三 不就是第四位的吗
            # 同理12后面的都会遍历的啊  不用想走到最后怎么怎么样 走到最后也是一样的
            count, start, match_set = len(words), i, {}
            for j in range(i, len(s), unilen):  # 从0开始循环 步长为长度
                substr = s[j:j + unilen]  # 切割一下
                if substr in sets:  # 判断在不在里面
                    match_set[substr] = match_set.setdefault(substr, 0) + 1
                    count -= 1
                    while (match_set[substr] > sets[substr]):  # 这个地方就是我们匹配的set的数量多于sets的数量要把start后移
                        remove = s[start:start + unilen]
                        start += unilen
                        match_set[remove] -= 1
                        count += 1
                    if count == 0:  # count等于0刚好匹配自然就加入start里面的啊
                        res.append(start)
                else:
                    count, start, match_set = len(words), j + unilen, {}  # 这个地方做的就是说要是不在的话更新start 同样下次的j也是加上了unilen的
        return res
