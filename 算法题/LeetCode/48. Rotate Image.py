# 旋转图像
"""
给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
"""
    第一种解法 就是用新列表 
        因为
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
            输出：[[7,4,1],[8,5,2],[9,6,3]]  
            按照行列划分 原矩阵的第一列倒序就是新矩阵的第一行
        当找到这个规律了之后 就很好写了
        ress.append(matrix[-(j + 1)][i])
        外层i确定第二个位置 内层j确定第几个列表 这个就能抽出来的
    第二种解法 就是旧的列是新的行 索引减去旧的行是新的列
        能不能想到是置换四个点的 这个比较难  
        也就是说 下次看见置换或者什么的 一对一不好置换 你可以多往前面看几步 大局观要有
"""


class Solution:
    def rotate(self, matrix) -> list:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        res = []
        while i < n:
            ress = []
            for j in range(n):
                ress.append(matrix[-(j + 1)][i])
            i += 1
            res.append(ress)
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
a = Solution()
print(a.rotate(matrix))


class Solution1:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        n = h - 1

        for i in range(h // 2):  # 0
            for j in range(i, n - i):  # 1
                tmp = matrix[i][j]  # [0][1] 为什么想不到 tmp临时变量
                matrix[i][j] = matrix[n - j][i]  # [0][1] = [2][0]
                matrix[n - j][i] = matrix[n - i][n - j]  # [2][0] = [3][2]
                matrix[n - i][n - j] = matrix[j][n - i]  # [3][2] = [1][3]
                matrix[j][n - i] = tmp  # [1][3]=[0][1]
        return matrix


"""
    这个地方解法的规律就在于 旧的列是新的行 索引减去旧的行是新的列 其实和上面一样 就是在原先列表上面更改
    还有就是循环一半是可以提高效率的 因为 对半换吗 为什么改四个呢 其实是以四个顶点为标识的  还有就是你可以发现 只能一次换四个这样的换 才不会产生多的数据
    有难度
"""

matrix1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
a = Solution1()
print(a.rotate(matrix1))
