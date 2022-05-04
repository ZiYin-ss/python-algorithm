# 矩阵置零
"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用原地算法。
"""
"""
    其实最难的不是怎么写 主要是原地算法以及时间复杂度和前面把行列都改了之后那么循环到后面的时候 又改行列可怎么整
    解决方法就是
        当i行j列如果是0 那么把 0行j列改为0 i行0列改为0就可以了啊 反正迟早都要改的啊
        注意此时 0行j列改为0 i行0列改为0之后 你需要做的是  j列改为0 i行改为0 而不是把0行0列全改为0
        还有一个注意点就是
            第0行第0列 如果第0行和第0列对应的位置有0的话 你就要注意需要最后再改变 如果一开始改变的话 是不是就是全0了啊
    总结
        其实一定要明白 0行0列是标志位 不可以直接改
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    zero_row = True if i == 0 else zero_row  # 确定第0行和第0列是否要更改
                    zero_col = True if j == 0 else zero_col
        for j in range(1, n):  # 改变对应的j列为0
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        for i in range(1, m):  # 改变对应的i行为0
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        if zero_row:  # 对应的是第0行
            for j in range(n):
                matrix[0][j] = 0
        if zero_col:  # 第0列
            for i in range(m):
                matrix[i][0] = 0
