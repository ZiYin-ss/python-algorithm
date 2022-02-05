# 解数独
"""
编写一个程序，通过填充空格来解决数独问题。
数独的解法需 遵循如下规则：
    数字1-9在每一行只能出现一次。
    数字1-9在每一列只能出现一次。
    数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
    数独部分空格内已填入了数字，空白格用'.'表示。
"""
"""
    肯定能想到这个用回溯法 但是你能不能想到不断的执行这个函数 这个函数的设计是很难的 其他的到还好
"""

class Solution:
    def solveSudoku(self, board) -> None:

        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        palace = [[set() for _ in range(3)] for _ in range(3)]  # 3*3
        blank = []

        # 初始化，按照行、列、宫 分别存入哈希表
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    blank.append((i, j))
                else:
                    row[i].add(ch)
                    col[j].add(ch)
                    palace[i // 3][j // 3].add(ch)

        def dfs(n):
            if n == len(blank):
                return True
            i, j = blank[n]
            rst = nums - row[i] - col[j] - palace[i // 3][j // 3]  # 剩余的数字
            if not rst:
                return False
            for num in rst:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                palace[i // 3][j // 3].add(num)
                if dfs(n + 1):
                    # 这个地方是什么意思?  这个地方返回true 只有说n已经处理完了 才会长度一样
                    # 这tm就是回溯法  然后再执行的过程中把 不断的加进去 返回false的话 就移除呗 继续加下一个呗
                    # 确实这个思想确实不会 但是这个就是回溯法
                    return True
                row[i].remove(num)
                col[j].remove(num)
                palace[i // 3][j // 3].remove(num)

        dfs(0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

a = Solution()
a.solveSudoku(board)
print(board)

"""
    会不会暂时不要求 确实这个函数的设计是真的很牛逼的 
"""