# 搜索插入位置
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""
"""
    第一种情况你能不能想到无论有没有
        插入之后 重新排序那么target位置索引就会是你插入之后的位置索引 或者有的时候返回的索引
    第二个是能不能想到分类讨论
    
"""


class Solution1(object):
    def searchInsert(self, nums, target):
        """
            这样也可以写 你让我咋整 TM的
        """
        nums.append(target)
        nums.sort()
        return nums.index(target)


class Solution:
    def searchInsert(self, nums, target: int):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < target < nums[i + 1]:
                return i + 1
        """
            这个地方是先二分查找 然后没有的话就返回插入索引 
            也挺快的 不难
        """


nums = [1, 3, 5, 6]
target = 4
a = Solution()
print(a.searchInsert(nums, target))
