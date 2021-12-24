# 移除元素
"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
"""
    这个解题思路 
        第一种方式 前面那一题我的del 这个地方也是可以用的呢  但是太慢了
        第二种方式 就是你能不能想到前后交换 我其实想到了一点 把last的值更新 要是一样的话
"""


class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]  #这个是核心
                last -= 1  # 不是真正删除 但是说最后一个永远访问不到了 每这样循环一下就多一个
            else:
                i += 1

        return last + 1

"""
    这个地方最最重要的你能不能想到 前后交换 两个指针
    tips：
        nums[i], nums[last] = nums[last], nums[i] 这样交换元素 与中间有个变量的那种是一样的
        
"""

