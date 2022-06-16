# 子集
"""
    给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
    解集不能包含重复的子集。你可以按任意顺序返回解集。
"""
import itertools


class Solution:
    def subsets(self, nums):
        ans = []  # nums = [1,2,3,4,5]
        for i in range(len(nums) + 1):  # 0是空集 1 2 3 4 5
            for tmp in itertools.combinations(nums, i):  # 返回这个序列里面的长度为多少的子集 全部加进去不就可以了
                ans.append(tmp)
        return ans


class Solution1:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):  # 和上一题一样啊
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res
