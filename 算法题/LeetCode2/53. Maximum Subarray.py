# 最大子数组合
"""
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    子数组 是数组中的一个连续部分。
"""
"""
    这道题就在于你能不能想到用局部最大值和整体最大值 本来要求返回的就是数而不是组合 懂吗
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)

        return global_max


"""
    这道题其实特别简单 就是思路的问题 
        就一个一个过来 然后一个一个加 最后看是最大的
    有一个注意的点 这个for循环里面 当前面的local_max小于0的话 你会发现更新local_max为0 因为必有一个大于0的吗 这个地方是个技巧
        假如 nums = [-2,1,-3,4,-1,2,1,-5,4] 那么其实前3个走完之后 local_max还是0 global_max还是0 相当于重新开始 就这个意思
        说我没法表示 但是看走的流程就知道了
    max函数是可以接收多个参数的 max(1,2,......) 是可以找出最大值的 不仅可以放列表
    其实写算法 最重要的其实是把样例写出来 其实你就会了
"""
