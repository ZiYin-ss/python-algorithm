# 编辑距离
"""
给你两个单词word1和word2，请返回将word1转换成word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""
"""
dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
    所以，
        当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
        当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
        注意，针对第一行，第一列要单独考虑，我们引入 '' 下图所示：
    因为对于下一个来说无非就是上一个好了 下一个是怎么样的
    https://leetcode-cn.com/problems/edit-distance/solution/shi-pin-jiang-jie-bian-ji-ju-chi-dong-tai-gui-hua-/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # print(dp)
        return dp[-1][-1]
