# 三数之和
"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""
"""
    这个思路在于你能不能想到两个指针三个数大于0要右边左移 小于0左边右移 
    这类题前面盛水最多的容器也是这个原理 
        最精髓的在于你能不能想到  你多想的都是没有意义的了
"""


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        res = []
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                # 如果下一个i和上一个一样 其实循环的没有意义 都是重复的
                # 必须要大于0的意思是说 加入输入的都是00000 那么你一次都进不来 就防止这个情况的
                continue
            L = i + 1  # 这个其实0也没问题 但是这样写可以去除很多重复的  当-1(从这个开始) 0 1  和-1 0(从这个开始) 1 你会发现重复的
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:  # 这个一样是没有意义的
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1  # 当上面有一样的或者没有一样的 其实这个L在没更新前 都是原来的值
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    # 最牛逼的应该是这个地方了 你要知道 当最小和最大相加都大于0了 你右边不移难道左边移吗 那样恒大于0啊  也没有意义啊
                    # 下面是同理 这个道理和第11题很像 你多想的哪些是没有意义的
                    #  当我领悟到了 多想的都是没有意义的 我就领会到这类题了
                    R -= 1
                else:
                    L += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
a = Solution()
a.threeSum(nums)
