# 搜索旋转排序数组
"""
整数数组nums按升序排列，数组中的值互不相同 。

在传递给函数之前nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。

给你旋转后的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值target ，则返回它的下标，否则返回-1
"""

"""
    你有没有发现一个事情 就是这个target就是nums里面的数 无非就是让你找数返回索引 懂吗
    第一种解法就不说了 猪都知道
    第二种解法 用二分法 但是你能不能想到他旋转之后 你怎么判断这个target在nums的左侧还是右侧
"""

"""如果不考虑时间复杂度是完全可以这样写的"""


class Solution1:
    def search(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:  # 这里面所有的0 全部改为left 是会快一点的  还有就是 写0和写left是一样的 只不过 范围多少而已
                if nums[0] <= nums[mid] < target:  # 说明一直到mid位一直是升序的
                    left = mid + 1
                else:  # 其实上面的走完了之后 走到这来了 其实说明值就是在左半边 懂吗
                    right = mid - 1
            else:  # target < nums[0]
                if nums[mid] >= nums[0] or target > nums[mid]:  # 在右边的情况
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


"""
    最难的地方在于 怎么判断 target在nums的左侧还是右侧
    if target >= nums[0]: 
        if nums[0] <= nums[mid] < target:  # 说明一直到mid位一直是升序的
    else:  # target < nums[0]
        if nums[mid] >= nums[0] or target > nums[mid]:  # 在右边的情况
"""
