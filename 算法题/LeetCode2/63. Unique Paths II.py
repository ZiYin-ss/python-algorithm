# 不同路径2
"""
一个机器人位于一个m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * n for _ in range(m)]
        cache[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cache[i][j] = 0
                else:
                    if i > 0:
                        cache[i][j] += cache[i - 1][j]
                    if j > 0:
                        cache[i][j] += cache[i][j - 1]
        return cache[-1][-1]


"""
    这道题思路和62是一样的 只不过就是说 你要把石块位置的路标0就可以了
    还是上面加前面
"""
