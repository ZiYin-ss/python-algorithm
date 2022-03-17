# 排列序列
"""
给出集合[1,2,3,...,n]，其所有元素共有n!种排列。
按大小顺序列出所有排列情况，并一一标记，当n=3 时, 所有排列如下：
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
给定n和k，返回第k个排列。
输入：n = 3, k = 3
输出："213"
"""
"""
计算当前k处于哪一个分支内（第一层一共n个分支）：每个分支对应（n-1）！条路径，因此，k/（n-1）!取整能得出k处在哪个分支
    比如4 那么n-1的阶乘是6  但是4的阶乘是不是24   那么6乘以4个分支 不就是24吗  找第9个 不就是找第9条路吗 
    9/6 = 1 这个不就是第1个分支呗(从0开始)   
remainder = k/（n-1）!取余，remainder即为当前分支内第几条路径，同样使用1的方法求解
循环n次，可得每次路径，拼接后即为第k个排列
"""

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        digits = [i for i in range(1, n + 1)]
        for i in range(n - 1, -1, -1):  # 假入n是4 n-1=3 k=9
            curBase = math.factorial(i)  # 阶乘是6
            curIndex = (k - 1) // curBase  # 为什么k-1因为是9是取8  是不是就是1
            ans += str(digits[curIndex])  # 就是找到了那一条路啊
            digits.remove(digits[curIndex])  # 添加进来就要移除 要不然重复了啊
            k = k - curIndex * curBase
        return ans
"""
    有点难现在不要求
"""

a = Solution()
a.getPermutation(4, 9)
