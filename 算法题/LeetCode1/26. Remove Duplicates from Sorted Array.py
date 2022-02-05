# 删除有序数组中的重复项
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
"""
    解题思路 第一种自己写的解题思路是可以实现的 就是太垃圾了 在于你能不能想到 i是在变的时候加 不变不加 
    第二种 
        其实是我们想多了 for循环 直接比较 一样不变  不一样才变 这样返回数就可以 在于你不要想其他的就是返回的只是数字
        其实把前几个值更新就可以了 这个有技术 确实不知道
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        a = nums[0]
        i = 1
        while True:
            try:
                if a == nums[i]:
                    del nums[i]
                else:
                    a = nums[i]
                    i += 1
            except:
                break
        return i


class Solution1:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):  # 不能从1开始 要是只有一个呢
            if nums[count] != nums[i]:  # 不一样的时候才变
                count += 1  # 因为0是第一个元素 不一样肯定要先加一啊
                nums[count] = nums[i]  # 这个才是牛逼的地方 不仅修改了对应位置的值 要没有多占用空间 还可以下一次继续循环 这个真的看经验
        return count + 1


a = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(a))
