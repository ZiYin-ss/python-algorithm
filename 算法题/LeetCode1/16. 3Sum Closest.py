# 最接近的三数之和

"""
给你一个长度为 n 的整数数组nums和 一个目标值target。请你从 nums 中选出三个整数，使它们的和与target最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
"""
"""
    这道题的解法和15题一模一样 因为你大于target之后你大值不就左移呗(小值右移有意义吗) 
    不移也不行啊 
    和15题10题的思想一模一样
"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(val - target) <= abs(result - target):
                    result = val
                if val == target:
                    return target
                elif val < target:
                    l += 1
                else:
                    r -= 1
        return result