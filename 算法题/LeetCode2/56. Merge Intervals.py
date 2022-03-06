# 合并区间
"""
    以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
    请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
"""

"""
class Solution:
    def merge(self, intervals):
        n = len(intervals)
        i = 0
        result = []
        while i < n:
            if i + 1 < n and intervals[i + 1][1] >= intervals[i][1] >= intervals[i + 1][0] and intervals[i + 1][0] < \
                    intervals[i][0]:
                result.append(intervals[i])
                i += 1
            elif i + 1 < n and intervals[i + 1][1] >= intervals[i][1] >= intervals[i + 1][0]:
                result.append([intervals[i][0], intervals[i + 1][1]])
                i += 1
            else:
                result.append(intervals[i])
            i += 1
        return result
这个代码不能用 只能说是不成熟的想法
"""
"""
    解题思路 就是说 先得把第一个值排序 然后一个一个的比较 要是有包含的话就合并 没有的话就添加 那么下一个过来依然和前面比 这个时候就不会出现问题
"""


class Solution:
    def merge(self, intervals):
        result = []
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if result:
                prev_start, prev_end = result[-1]  # 把结果的最后一个取出来 自动解包了
                hi = min(prev_end, cur_end)  # 找result最后一个的索引和当前 最后的索引的最小值
                lo = cur_start  # 也就是当前元素的起始位置
                if lo <= hi:  # 如果一开始的最大值小于最后面的最大值
                    """这个地方有一个点 就是[2,6][3,4] 那么也就是3<4且 cur_end<prev_end 那么其实是不是result里面的不变啊"""
                    if cur_end > prev_end:  # 且 当前最后一个大于result前面一个
                        result[-1][1] = cur_end
                else:  # 也就是当前一个 开始的索引 大于result的最后面的索引 因为 cur_end > cur_start > prev_end
                    result.append(intervals[i])  # 反之这个地方就是一开始的最大值 大于最后面的值 是不是就是直接加上啊
            else:
                result.append(intervals[i])
            i += 1
        return result


intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
a = Solution()
print(a.merge(intervals))

"""
    这个解题思想前面做过 一个一个比较 while True 最后一个和未比较列表里面第一个比
"""