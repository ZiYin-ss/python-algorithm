# 螺旋矩阵2
"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
"""
    这道题其实真的是超级简单的好不呢 就是在于你能不能想到 当顺时针转一圈之后 就是你的n*n的列表 缩小了一圈  
        比如就是3*3缩小了一圈是不是就是1*1了 左边索引加1 右边索引减1 无非就是找四个点给他标志着呗
"""


class Solution:
    def generateMatrix(self, n: int):
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        rowBegin = 0  # 行首
        rowEnd = n - 1  # 行尾
        colBegin = 0  # 列首
        colEnd = n - 1  # 列尾
        number = 1  # 计数呗 其实就是缩小一圈以后 对应的再转的话 那么number是不是也是对应的值  当循环一圈以后 不就是8 该写9了
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):  # 控制列 列变
                matrix[rowBegin][i] = number
                number += 1
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):  # 控制行 行变
                matrix[i][colEnd] = number
                number += 1
            colEnd -= 1
            if rowBegin <= rowEnd:
                # 这个判断 其实是防止 输入一个2的时候  包括最后是2*2的时候的判断 注意必须要小于等于 因为等于的时候 还没有写上对应位置的数
                for i in range(colEnd, colBegin - 1, -1):  # 倒序 就算只有一个 为0 那么for循环就走一个0呗
                    matrix[rowEnd][i] = number
                    number += 1
                rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = number
                    number += 1
                colBegin += 1
        return matrix


"""
    这道题确实不难 最恶心的地方就是你需要判断  if colBegin <= colEnd: 这个东西  不知道该放在那 
"""
