# 颜色分类
"""
给定一个包含红色、白色和蓝色、共n个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。
"""


class Solution:  # 题目要求自己写一个排序不就可以了
    def sortColors(self, nums) -> None:
        for i in range(len(nums) - 1):  # 少排一趟
            min_loc = i  # 设置最小位置的下标  这个是无序区的第一个呢
            for j in range(i + 1, len(nums)):  # 和后面的比 加一是一个可做可不做的
                if nums[j] < nums[min_loc]:  # 这个遍历完之后 是不是把最小位置的下标给了min
                    min_loc = j  # 这个时候min_loc 不就是最小下标了吗
            nums[i], nums[min_loc] = nums[min_loc], nums[i]  # 在这个地方做了替换呢


nums = [2, 0, 2, 1, 1, 0]
a = Solution()
a.sortColors(nums)
print(nums)
