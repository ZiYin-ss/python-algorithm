# 组合总和2
"""
给你一个由候选元素组成的集合 candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates 中的每个元素在每个组合中只能使用一次 。
注意：解集不能包含重复的组合。
"""


class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates = sorted(candidates)
        ans = []
        # 必须要用回溯法做 因为这是一个思想 很重要的 必须要知道
        return


candidates = [2, 5, 2, 1, 2]
target = 5
a = Solution()
print(a.combinationSum2(candidates, target))
