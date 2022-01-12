# 组合总和
"""
给你一个无重复元素的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target的所有不同组合 ，
并以列表形式返回。你可以按任意顺序返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。
如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为target 的不同组合数少于 150 个。
"""
"""
    这道题的解法在于能不能想到递归调用 想到新的target和新的列表 继续调用函数 
    还是说函数的设计比较难 其他的还好
"""


class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)  # 从小到大排序

        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])  # 第一次会走进去四个2 然后 i+1 = 2 不是继续 也不是 一直走到7 返回7 就这意思
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return

        find(0, [], target)

        return ans


"""
    这个题的思想在于你能不能想到重复的找 
    意思 是 先是2 然后进去 接着2 再2 再2 然而最后一个2会退出第四层 然后就是第三层 找3 不行 继续后面找
    依次类推 223 然后接下来就退出i=0这个循环 走i=1的循环 其实走这个循环的时候 此时use就是[]空列表了 能明白吗
    走到最外面的循环的时候 就是都退出来了 此时use就是[] 能明白把 就这个地方不好理解 
    这个其实就是回溯法  或者叫做递归
    再说一遍流程就是说 接着调用这个函数 传递新的列表和target  而这个函数就是一直从第一个数循环呢 很有意思的哦 多想想 不难
"""

candidates = [2, 3, 6, 7]
target = 7

a = Solution()
b = a.combinationSum(candidates, target)
print(b)
