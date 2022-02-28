# 螺旋矩阵
"""
给你一个m行n列的矩阵matrix ，请按照顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
"""
    解题思路就是能不能想到 从左到右然后从上到下然后从前到后然后从下到上 走完的就把走过的序列索引都删掉 
"""

class Solution:
    def spiralOrder(self, matrix):
        x1, y1, x2, y2 = 0, len(matrix[0]), 0, len(matrix)
        # x1代表第几列(就是是matrix[0][0]还是matrix[0][1])
        # x2代表第几行(就是是matrix[0]还是matrix[1])
        # y1代表一行的索引(就是matrix[0]里面的长度) 也就是多少列
        # y2代表一列的长度(就是matrix的长度) 也就是多少行
        n = y1 * y2  # 总体长度
        res = []
        while True:
            if len(res) < n:
                for i in range(x1, y1):
                    res.append(matrix[x2][i])
            else:
                break
            x2 += 1
            if len(res) < n:
                for i in range(x2, y2):
                    res.append(matrix[i][y1 - 1])
            else:
                break
            y1 -= 1
            if len(res) < n:
                for i in range(y1 - 1, x1 - 1, -1):
                    res.append(matrix[y2 - 1][i])
            else:
                break
            y2 -= 1
            if len(res) < n:
                for i in range(y2 - 1, x2 - 1, -1):
                    res.append(matrix[i][x1])
            x1 += 1
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = Solution()
print(a.spiralOrder(matrix))

"""
    其实这道题真的很简单 就是一开始就陷入到了思维误区 想着x++ x-- 其实不是这样的
    你可以按照上面的方法来处理 一个一个的走 四个标志代表行，列，第几行，第几列 走完一层把对应的数减一个不就是的呢 
    多想多练
"""