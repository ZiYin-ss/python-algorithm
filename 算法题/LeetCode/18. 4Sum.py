# 四数之和
"""
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
"""
"""
    这个思路在于你能不能想到 循环两次  
"""

class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        ans = set()  # 为了去重
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                now = nums[i] + nums[j]
                q = len(nums) - 1
                p = j + 1
                while p < q:
                    if nums[p] + nums[q] + now == target:
                        if (nums[i], nums[j], nums[p], nums[q]) not in ans:
                            ans.add((nums[i], nums[j], nums[p], nums[q]))
                    if nums[p] + nums[q] + now > target:
                        q -= 1
                    else:
                        p += 1
        return list(ans)

"""
    这个思想和三数之和很像 可以说一模一样   没什么好说的
"""