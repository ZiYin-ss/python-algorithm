# 盛最多水的容器
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。
在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
"""
"""
    第一个方法没有思路 有手都会写
    第二个方法
        解题思路就在于 
            如果移动之后还是短 你会发现最大的面积就是最开始的时候
            如果移动之后大的话 那么会和原来的右端继续乘面积比较 
            假如更新长端之后 高度不还是短端吗(或者更短的那端此时就没有意思)
"""


class Solution:
    """
        这个方法可以是可以 但是 tm超出时间限制了 tm
    """

    def maxArea(self, height):
        max = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                hg = height[i] if height[i] < height[j] else height[j]
                a = hg * (j - i)
                if a > max:
                    max = a
        return max


class Solution1:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])

            if area > max:
                max = area

            if height[left] < height[right]:  # 这个才是重点
                left += 1
            else:
                right -= 1
        return max
"""
    你能不能想得到比较过后 更新比较短的那一端的指针
    其实这道题 我们会好奇 不全局比的话 要是其他情况大怎么办
        其实可以想到 在移动短端的时候 
            假设短端是左端
            如果移动之后还是短 你会发现最大的面积就是最开始的时候
            如果移动之后大的话 那么会和原来的右端继续乘面积比较 
    看OneNote图就知道了 你所想的每一种情况都包括了 
"""

a = Solution1()
print(a.maxArea([4, 3, 2, 1, 4]))
