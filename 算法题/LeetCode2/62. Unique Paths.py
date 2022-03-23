# 不同路径
"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""


# python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


"""
    这个东西就是简单得动态规划啊 就是走完第一行之后其实都是1啊 走第二行不就是上面的步数加上左边的步数不就是走到这个有几种情况呗
    而第一行第一列你怎么走不都是一种情况呗(按照题目中的走法) 
    [[1,1,1,1,1,1]
     [1,2,3,4,5,6]
     [1,3,6,10,15,21]]
     其实这个地方你得明白不是走几步 而是几条路 不在乎你一步走多少 而是说怎么走
     那走到这个格子不就前面的路径加上上面的路径不就可以了呗 就这呗
"""
