# 组合总和2
"""
给你一个由候选元素组成的集合 candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates 中的每个元素在每个组合中只能使用一次 。
注意：解集不能包含重复的组合。
"""
"""
    解题思路略过 看分析 没法说
"""


class Solution:
    def combinationSum2(self, candidates, target: int) -> List[List[int]]:
        def backtrack(tmp, cur, index):
            if cur > target:
                return
            if cur == target:
                res.append(tmp)
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:  # 重复元素不要
                    continue
                backtrack(tmp + [candidates[i]], cur + candidates[i], i + 1)

        res = []
        n = len(candidates)
        candidates.sort()
        backtrack([], 0, 0)
        return res


"""
    这个解法要从整体上面理解 就是说你有没有发现一开始是第一个元素 我们直接加进去就是的了 然后一直加 如果等于 代表符合 就加入到res里面了
    如果要是不等于 是不是就是说 这个函数return掉了 就是不执行了 然后for循环下一个了
    1-也就是说 从第一个元素开始找 然后递归调用 第一个加进去 加第二个 依次类推 有了就把解加到res里面 
    2-如果上面没有找到  我们是不是就开始找第二个了啊从第二个往后面找
    还有就是说 如果第一个和最后一个加起来一样是什么原理呢
        就是说 里面依然按照1和2开始循环了 里面就是说 从2开始找 然后没有 走下一个 这个意思知道吗
"""
"""
    回溯法和动态规划都是一种思想 就是说你设计的东西 满足要求而且还去重 这个东西解释是真的没法解释 字面意思其实就是的了 得理解
    看上面的分析 有没有发现 还是递归调用 最难的还是函数的设计
"""

candidates = [2, 5, 2, 1, 2]
target = 5
a = Solution()
print(a.combinationSum2(candidates, target))
