# 有效的数独
"""
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
注意：
    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    空白格用'.'表示。
"""
"""
    注意算法一定要学着可以解释 自己写的算法你都看不懂 其实没有什么意义哪怕是最优的也没有意义
    这个道题不难 就在于思想 你能不能想到 把每一行 以及每一列 每一块的数字 变成集合求长度 
    就是推导式那语法是真不知道 其他的不难 
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board)

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            # *board是什么意思 你不会不懂把 board里面的每个元素是列表 把里面的元素都取出来就是一个一个列表 按照元素合并就可以了啊
            # [1,2,3] [1,2,3] [1,2,3] [1,1,1] [2,2,2] [3,3,3] 是个技巧
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
                # 会生成这样的形式 要是不知道 记住就可以了啊 也就是说整数形式 元组 列表下标之类的 都是两层嵌套
                # 字典就是单独循环
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
