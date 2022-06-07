# 组合
"""
给定两个整数n和k，返回范围 [1, n]中所有可能的k个数的组合。
你可以按 任何顺序 返回答案。
"""
import itertools


class Solution:
    def combine(self, n: int, k: int):
        ans = []  # 最终答案列表
        nums = [i + 1 for i in range(n)]  # 生成1-n之间的数据

        def dfs(last, now):  # 直接深度优先就可以了
            if len(now) == k:
                ans.append(now)
            for i in range(len(last)):
                dfs(last[i + 1:], now + [last[i]])

        dfs(nums, [])
        return ans

    """
        n = 4 k =2
        nums = [1,2,3,4]
        深搜流程
            dfs([1,2,3,4],[])
                dfs([2,3,4],[1])   
                    dfs([3,4],[1,2]) -->[1,2]会加ans里面去
                        dfs([4],[1,2,3])  -->无意义
                            dfs([],[1,2,3,4])  # 列表为空 len([])==0 其实不会走循环里面
                    dfs([4],[1,3]) -->[1,3]会加ans里面去
                        dfs([],[1,3,4])
                    dfs([],[1,4]) --> [1,4]会加ans里面去
                dfs([3,4],[2])    -->[2,3][2,4]会加ans进去
                dfs([4],[3])      -->[3,4]会加ans里面
                dfs([],[4])
        一道典型的深度优先的题目，这个循环是每个情况都会遍历到 只有当len(now)值为2的时候才会 加入ans里面
        思想就是拿当前这个i索引上的值，和接下来的每个值都组合一下
        
    """


class Solution1:
    def combine(self, n: int, k: int):
        return list(itertools.combinations(range(1, n + 1), k))

    """
    创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复),r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度。
    Python还是有很多稀奇古怪的库的 ，挺好用
    """
