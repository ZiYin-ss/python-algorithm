# 搜索二维矩阵
"""
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
"""


class Solution:  # 方法1
    def searchMatrix(self, matrix, target):
        if matrix[0][0] == target:  # 特判只有一个值
            return True
        li = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                li.append(matrix[i][j])
        res = self.binary_search(li, target)  # 直接用二分查找就可以了啊
        if res == 0 or res:
            return True
        else:
            return False

    def binary_search(self, li, val):
        left = 0
        right = len(li) - 1
        while left <= right:  # 候选区有值
            mid = (left + right) // 2
            if li[mid] == val:
                return mid
            elif li[mid] > val:
                right = mid - 1
            elif li[mid] < val:
                left = mid + 1
        else:
            return None


class Solution1:  # 方法2
    def searchMatrix(self, matrix, target):
        li = []  # 因为二维列表 不可以直接 target in li 需要转换为一维列表才可以 也比较快
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                li.append(matrix[i][j])
        if target in li:
            return True
        return False
