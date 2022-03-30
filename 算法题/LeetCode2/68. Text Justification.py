# 文本左右对齐
"""
给定一个单词数组words 和一个长度maxWidth，重新排版单词，使其成为每行恰好有maxWidth个字符，且左右两端对齐的文本。
你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格' '填充，使得每行恰好有 maxWidth个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
注意:
    单词是指由非空格字符组成的字符序列。
    每个单词的长度大于 0，小于等于maxWidth。
    输入单词数组 words至少包含一个单词。
"""


class Solution:
    def fullJustify(self, words, maxWidth: int):
        # res 返回结果
        # line 缓存每一行的单词
        # counter统计当前进入line的单词总长度
        res, line, counter = [], [], 0
        for word in words:
            if counter + len(word) + len(line) > maxWidth:  # 为什么要加上len(line)呢 词之间最少空格数是一个
                for i in range(maxWidth - counter):
                    line[i % max(len(line) - 1, 1)] += ' '  # 其实就说放到前两个数中
                res.append(''.join(line))
                line, counter = [], 0
            line += [word]
            counter += len(word)
        return res + [' '.join(line).ljust(maxWidth)]  # 最后一行左对齐 而且最后一行是不会进入if判断的 ljust默认补空格


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

a = Solution()
print(a.fullJustify(words, maxWidth))

"""
    这是一个典型的贪心算法  就是放尽可能多的  余数用的很妙 而且最后一个还不会插入空格 1-len(line)-1的位置插入空格 牛逼
"""
