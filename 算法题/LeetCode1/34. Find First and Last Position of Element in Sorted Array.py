# 在排序数组中查找元素的第一个和最后一个位置
"""
给定一个按照升序排列的整数数组nums，和一个目标值target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。
进阶：
    你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
"""
"""
    也是有简单写法的 但是时间复杂度 要不然没有挑战性
    其实是我们自己想难了 因为这个东西只会返回列表 列表里面两个元素而已
    能不能想得到先从前面找到第一个出现的位置 然后逆序一下 那么这个时候第一个出现的位置不就是列表里面的第二个元素呗
     len(nums) - (list(nums[::-1]).index(target)) - 1 这个就是逆序之后第一个出现的位置 减一就是为了索引对上
     这个数据技巧不难 很常见 只是我们见的很少
"""


class Solution:
    def searchRange(self, nums, target):
        try:
            return [nums.index(target), len(nums) - (list(nums[::-1]).index(target)) - 1]
        except:
            return [-1, -1]
        # left, right = 0, len(nums) - 1
        # res = []
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         res.append(mid)
        #
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # if len(res) == 0:
        #     return [-1, -1]
        # else:
        #     return res
"""
    其实想明白了返回固定的两个值 这道题也会做了
"""

nums = [5, 6, 7, 7, 7, 8, 8, 9, 9, 10]
target = 8
a = Solution()
print(a.searchRange(nums, target))
