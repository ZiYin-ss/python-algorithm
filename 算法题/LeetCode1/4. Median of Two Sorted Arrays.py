# 寻找两个正序数组的中位数
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log(m+n)) 。
"""
"""
    解题思路就在于明白什么是中位数 
        元素个数是奇数的话返回的是列表中间的
        元素个数是偶数的话返回中间两个的平均数 
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        c = nums1 + nums2
        c.sort()
        if len(c) % 2 == 0:
            return (c[len(c) // 2] + c[len(c) // 2 - 1]) / 2
        else:
            return c[len(c) // 2]


"""
    / 这个返回的是浮点型  // 如果两边都是整数返回的是int型 如果有一个是浮点型那么就是浮点型
    这个是可以解决的 执行速度也不慢 但是感觉投机取巧 没有融入算法进去 
        其实融入算法倒也还好 无非不就是把排序改改呗 还好
"""

instance = Solution()
awanser = instance.findMedianSortedArrays([12], [3, 4])
print(awanser)
