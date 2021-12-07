# 两数之和
"""
    给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
"""


class Solution:
    """
        这个的原理就是列表吗
            前面减的数是j 如果后面有就可以直接if出来
            假如for一直到后面了  那么你到后面的数据减出来的j如果要是前面有的话 是不是前面循环的话就会出来了啊
            比如
                [2,7,11,15]  target = 9
                那么你看前面 9-2=7 7在后面
                要是 9-7=2 你看是不是前面就有
                假如前面出来的j后面没有 那么后面减出来的j前面是不是肯定没有(有的话前面的j就匹配上了)
                明白这个道理不就好了呗
    """

    def twoSum(self, nums, target):
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                return start_index, next_index + temp_nums.index(j)  # 为什么这个地方要这样写 因为索引不能重复万一重复呢
        return "找的值不存在"


class Solution1:
    def binary_search(self, li, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            elif li[mid][0] < val:
                left = mid + 1
        else:
            return None

    def twoSum(self, nums, target):
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                return sorted([new_nums[i][1], new_nums[j][1]])


class Solution2:
    def twoSum1(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:  # 这个地方in比的是key key存在是不是就可以返回啊
                dict[nums[i]] = i  # key是值 value是索引
            else:
                return dict[target - nums[i]], i
        # 这个为什么会快呢 因为其实是 假如有了这个key 就可以直接返回 不像前面你要if一下 肯定快啊

a = Solution2()
a.twoSum1([2,7,11,15],17)