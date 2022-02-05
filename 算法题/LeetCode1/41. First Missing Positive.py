# 缺失的第一个正数
"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""
"""
    能不能想的到假如1在里面的话找到从1开始 排序之后找到最小的 
    原理就是利用  if nums[i] != j: 因为一开始j是1 那么开始和列表比较 不一样肯定返回j啊 一样说明列表有 j就加一
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if 1 not in nums:  # 1是最小正整数
            return 1
        else:
            start = nums.index(1)  # 找到大于0的数
        j = 1
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 防止重复比较
                continue
            if nums[i] != j:  # nums[i] 与j比较 不一样 那说明j是最小正整数
                return j
            j += 1  # 一样的话 不就加一呗
        return j


"""
    虽然是困难题 但是还是比较简单的 
"""
