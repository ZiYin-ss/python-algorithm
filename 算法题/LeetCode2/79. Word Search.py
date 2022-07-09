# 单词搜索
"""
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回true;否则，返回 false。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        """
            题目意思
                当前字母为中心 下个字母出现在当前字母上下左右四个方向都是ok的
                但是当前字母用过之后 不能再回来 ABFB ABF F之后不能回来找B只能找下一个B
            当能把题目读懂之后 一看就知道用DFS深度优先搜索来做 goto搜索整个排列
            还要注意找到起始点-->大部分深度优先搜索都从第一个点搜索 无非就是起始点改到其他地方了
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):  # 做DFS的函数 从word为0的位置开始
                    return True  # 因为一个helper其实就是会找到所有的可能性
        return False

    def helper(self, board, i, j, word, wordIndex):
        if wordIndex == len(word):  # 什么时候返回True 什么时候返回False
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][
            j]:  # 首先是边界处理 最后一个条件是 当前格子位置单词和word对应位置进行比较就可不满足就是false
            return False

        board[i][j] = '#'  # 把当前位置标记为#号 因为找过了吗 不能回来找 给他改为#号就可以了
        # 那么这个地方是什么意思呢 就是 假如当前点是的 找下一个点  一直找到最后一个 看返回的是True还是False
        #  下一行 下个位置的单词和下一个格子的单词进行比较 同一行的下一个
        found = self.helper(board, i + 1, j, word, wordIndex + 1)\
        or self.helper(board, i, j + 1, word, wordIndex + 1)\
        or self.helper(board, i - 1, j, word, wordIndex + 1)\
        or self.helper(board, i, j - 1, word, wordIndex + 1)

        board[i][j] = word[wordIndex]  # 复原
        # 这个地方是这样的 就是函数会生成栈 这个复原的 还是 与之相对应的 ij的#号
        return found

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
a = Solution()
print(a.exist(board,word))

