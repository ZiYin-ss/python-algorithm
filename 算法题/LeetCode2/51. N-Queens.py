# N皇后
"""
    n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
    每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""


class Solution:
    def solveNQueens(self, n: int):
        def generateBoard(n, queens):  # 根据记录queens，生成对应的棋盘
            board = []
            row = ["."] * n  # 记录某一行中 queen 的具体位置（例如，'.Q..' 表示queen位于第1列）
            for i in range(n):  # 遍历n个queen
                row[queens[i]] = "Q"  # 将第i个queen放在列数 queens[i] 上
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(i, n):  # 在第 i 行 [0, n-1] 放置queen
            if i == n:  # 如果此时 i==n了 那么就代表说已经找到了合适的 皇后放置方案 queens里面保存的就是每一行皇后该放置的索引
                res.append(generateBoard(n, queens))
            else:  # 在第 i 行放置queen，
                for j in range(n):  # 遍历该行 [0, n-1] 列看是否存在合适的方案
                    if j in cols or i - j in diag1 or i + j in diag2:
                        continue  # 第 i 个queen不能放置在 j 列，即 (i,j) 处

                    queens[i] = j  # 第 i 个queen可以放置在 (i,j) 处

                    cols.add(j)  # 将当前位置 (i,j) 加入已占用位置信息中
                    diag1.add(i - j)
                    diag2.add(i + j)

                    backtrack(i + 1, n)  # 计算下一行，即第 i+1 行

                    cols.remove(j)  # 回溯：复原
                    diag1.remove(i - j)
                    diag2.remove(i + j)

        res = []
        queens = [-1] * n  # 每个 queen 放的列数 [0, n-1]
        cols = set()  # 记录列
        diag1 = set()
        diag2 = set()  # 其实这两个就是记录下一行 皇后的禁止位置
        backtrack(0, n)  # 从第0行开始放置queen
        return res
"""
    其实这道题很经典 其实也很简单 虽然说是困难难度的题
    递归法加回溯法
    就是行排列不用管他   就列对角线不能有 就是j，i+j和i-j不能有 
    backtrack 这个函数其实就是生成皇后放置方案 queens里面保存的就是每一行皇后该放置的索引
    generateBoard函数就是生成皇后排列的 
    只要j不在行列
"""
"""
    if j in cols or i - j in diag1 or i + j in diag2:
    只需要知道这个 不在理解即可 
    递归和回溯 你没法知道每一层走法  只需要知道 你把限定条件写上 加入和回溯就可以 
    这个就是我一直对递归和回溯 一直觉得不熟的原因 因为就是走不通 很别扭
"""

n = 4
a = Solution()
print(a.solveNQueens(n))
