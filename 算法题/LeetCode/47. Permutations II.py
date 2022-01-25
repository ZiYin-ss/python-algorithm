# 全排列2
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""
"""
    解题思路和46一样 就多了你能不能想到去重的条件 能不能想到前面有的 直接就不循环了
"""


class Solution:
    def permuteUnique(self, nums):
        if len(nums) <= 1:  # 为1的判断
            return [nums]

        answer = []

        for i, num in enumerate(nums):
            if nums.index(nums[i]) < i:  # 前面有的就直接不循环了 懂吗?
                continue
            n = nums[:i] + nums[i + 1:]
            for y in self.permuteUnique(n):
                answer.append([num] + y)

        return answer


"""
    [3,3,0,3]  
        第一个3进去之后  303走下一个循环 然后 你有没有发现 第二个3进去之后 还是303 直接continue就可以了啊
        303走进去之后 继续3 03 然后0 3 这样走 返回 
        当走到最后一个3 就不走了 为什么呢3 330 其实走进去之后 产生的数 前面都有
    其实做到这个题 慢慢的也有一点敏感了 对于这些结构 我本来一开始是 nums[i] == nums[i-1] 但是会发现  如果后面还有重复的话  组合还是会有重复的
    因为这个题是全排列 那么 第一个三 是不是就把所有3有关的组合都找出来了啊 
"""

nums = [3, 3, 0, 3]
a = Solution()
print(a.permuteUnique(nums))
