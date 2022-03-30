# 爬楼梯
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # 找到规律db[i] = db[i-1] + db[i-2]
        # db[0] = 1 , db[1] = 1, 零阶和一阶都是一次
        # db[]的长度为n+1，因为列表头多了一个零阶
        db = [0 for item in range(n+1)]
        db[0] = db[1] = 1

        for i in range(2,n+1):
            db[i] = db[i-1] + db[i-2]
        return db[-1]

"""
    超级简单的动态规划  多了一个零阶其实就是动态规划的思想 就是大一个数 
"""