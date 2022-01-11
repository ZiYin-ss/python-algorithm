# 组合总和
"""
给你一个无重复元素的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target的所有不同组合 ，
并以列表形式返回。你可以按任意顺序返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。
如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为target 的不同组合数少于 150 个。
"""
"""
    这道题有点难 明天再看把 
"""

class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)  # 从小到大排序

        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c]) # 第一次会走进去四个2 然后 i+1 = 2 不是继续 也不是 一直走到7 返回7 就这意思
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return

        find(0, [], target)

        return ans

"""
    这个题的思想在于你能不能想到重复的找 确实会 现在也不要求 确实难
"""

candidates = [2, 3, 6, 7]
target = 7

a = Solution()
b = a.combinationSum(candidates, target)
print(b)
