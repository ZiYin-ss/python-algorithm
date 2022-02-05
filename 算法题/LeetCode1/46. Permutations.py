# 全排列
"""
给定一个不含重复数字的数组nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。
"""
"""
    解题思路 能不能想的到用递归 把循环的数抽出来 然后继续调用这个函数 直至len为1的时候 返回 num+y就是的了
    n = nums[:i] + nums[i + 1:]  这个地方这样写 其实很好理解 就是把循环的数抽出来 然后继续执行呗 就是第一次见
    其实还是对递归不熟 递归用于都是走到最后返回一个值的地方返回 
        其他地方就是我们自己设计模式了 for循环的设计模式 递归函数的调用时间
    看我下面的分析把
"""


class Solution:
    def permute(self, nums):
        if len(nums) <= 1:  # 为1的判断
            return [nums]

        answer = []

        for i, num in enumerate(nums):  # 这个地方就是 循环一下这个nums呗
            n = nums[:i] + nums[i + 1:]  # 这个地方才是精髓 你看这个n是什么 是不是除了当前循环的数之外所有nums的值啊
            for y in self.permute(n):  # 把n放进去这个函数 循环执行
                answer.append([num] + y)  # 这个地方会是走到最后 if len <= 1的时候 返回的值 加上了
                
        return answer


nums = [1, 2, 3]
"""
    先是1 然后[2,3] 走这个permute函数了 
        这个里面2又去掉了 3走这个函数 返回了nums 然后这个y是不是就是3 然后num其实是2 
        这个时候 answer里面是[[2,3]]然后再3出来了2进去这个函数返回2 answer里面是[[2,3],[3,2]]这个就是返回值
        然后再返回 不就是answer不就是[[1,2,3],[1,3,2]]
    然后2走for循环 是不是一样的啊 
        [1,3]进函数 然后执行上面一样的步骤啊 
    
    其实是真不难 但是算法里面难的从来就不是代码而是思维
"""
a = Solution()
print(a.permute(nums))
