# 最小路径和
"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return 0
        if not grid[0]:
            return 0
        if len(grid[0]) == 1:
            return grid[0][0]
        # 上面是边界处理

        dp = [[2 ** 32 - 1 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        # 所谓动态规划都是要创建一个dp列表的 而列表的大小和传入的一样 或者大一行一列
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i - 1][j - 1]  # 第一步确定了
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
                # 这个地方是不是就是走到这一步需要的最短路径
                # 而边界就是多的一列啊 而且每次都是最短路径 那么走到最后不都是最短路径
        return dp[-1][-1]


"""
    这个就是非常经典的动态规划  其实真不难 就是你能不能相通怎么走
"""
